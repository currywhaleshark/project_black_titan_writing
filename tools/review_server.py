# -*- coding: utf-8 -*-
"""Project Black Titan 첨삭 도구 — 로컬 서버.

원고를 문단 단위로 열어 직접 고치거나 특정 구절에 코멘트를 달고,
원문과 나란히 비교한 뒤 프로젝트 폴더에 저장한다.

사용:
    python tools/review_server.py            # 기본 포트 8787 (이 PC에서만)
    python tools/review_server.py --port 9000
    python tools/review_server.py --lan      # 같은 와이파이의 휴대폰에서도 접속
"""
import argparse
import json
import os
import re
import socket
import sys
import threading
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "review.html")

def scan_dirs():
    """첨삭 대상 폴더를 동적으로 찾는다.

    에피소드 폴더는 이름이 바뀌고(진행중→승인완료) 새로 생기므로
    하드코딩하지 않는다. 저장은 항상 사본(_첨삭본)으로 한다.

    승인 전 폴더는 접미사가 없다(`18_EP013`). 승인되면 뒤에 붙는다
    (`18_EP013_승인완료`). 둘 다 잡아야 쓰는 중인 회차가 보인다.
    """
    dirs = []
    for name in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, name)
        if not os.path.isdir(full):
            continue
        if re.match(r"^\d{2}_EP\d{3}(_|$)", name) or name.startswith("90_NONCANON"):
            dirs.append(name)
    return dirs


def list_documents():
    docs = []
    for d in scan_dirs():
        full = os.path.join(ROOT, d)
        for name in sorted(os.listdir(full)):
            if not name.endswith(".md"):
                continue
            # 첨삭 결과물은 원본이 아니므로 목록에서 뺀다.
            # 이걸 다시 열어 저장하면 사본의 사본이 생긴다.
            if "_첨삭본" in name:
                continue
            rel = os.path.join(d, name).replace("\\", "/")
            path = os.path.join(full, name)
            docs.append({
                "rel": rel,
                "name": name,
                "dir": d,
                "size": os.path.getsize(path),
                "mtime": os.path.getmtime(path),
                "rank": rank_document(name),
            })
    # 초고 본문 → 승인 본문 → 나머지. 같은 등급이면 최근 것 먼저.
    docs.sort(key=lambda x: (x["rank"], -x["mtime"]))
    return docs


def rank_document(name):
    """첨삭 대상으로 자주 여는 순서.

    지금 고치는 초고가 맨 위여야 한다. 파일명에 `_초고_`를 붙이는
    관례와, 붙이지 않은 미승인 본문(`..._13화_사월의시간표_v0.1.md`)을
    모두 초고로 본다.
    """
    if re.search(r"_초고_v[\d.]+", name):
        return 0
    if re.search(r"_\d+화_", name):
        return 1 if "GateD승인" in name else 0
    return 2


def safe_path(rel):
    """프로젝트 밖으로 나가는 경로를 막는다."""
    full = os.path.normpath(os.path.join(ROOT, rel))
    if not full.startswith(ROOT):
        raise ValueError("경로가 프로젝트 밖을 가리킨다: %s" % rel)
    return full


def split_document(text):
    """머리말 블록과 본문 문단을 나눈다."""
    lines = text.split("\n")
    head = []
    i = 0
    # 제목(#)과 인용 블록(>)으로 이루어진 머리말을 본문에서 분리한다
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("#") or s.startswith(">") or s == "":
            head.append(lines[i])
            i += 1
            # 머리말이 끝났는지: 다음 비어있지 않은 줄이 본문이면 중단
            rest = [l for l in lines[i:] if l.strip()]
            if rest and not (rest[0].strip().startswith("#") or rest[0].strip().startswith(">")):
                break
        else:
            break
    body = "\n".join(lines[i:])
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    return "\n".join(head).rstrip(), paras


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_HEAD(self):
        """프리뷰·헬스체크가 HEAD로 준비 상태를 확인한다."""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        u = urlparse(self.path)
        if u.path in ("/", "/index.html"):
            with open(HTML_PATH, encoding="utf-8") as f:
                return self._send(200, f.read(), "text/html; charset=utf-8")

        if u.path == "/api/docs":
            return self._send(200, json.dumps(list_documents(), ensure_ascii=False))

        if u.path == "/api/doc":
            rel = parse_qs(u.query).get("rel", [""])[0]
            try:
                full = safe_path(rel)
                with open(full, encoding="utf-8") as f:
                    text = f.read()
            except Exception as e:
                return self._send(400, json.dumps({"error": str(e)}, ensure_ascii=False))
            head, paras = split_document(text)
            # 이전 첨삭이 있으면 함께 돌려준다
            memo = {}
            memo_path = self._memo_path(full)
            if os.path.exists(memo_path):
                try:
                    with open(memo_path, encoding="utf-8") as f:
                        memo = json.load(f)
                except Exception:
                    memo = {}
            return self._send(200, json.dumps({
                "rel": rel, "head": head, "paragraphs": paras, "memo": memo,
            }, ensure_ascii=False))

        return self._send(404, json.dumps({"error": "not found"}))

    @staticmethod
    def _memo_path(full):
        base, _ = os.path.splitext(full)
        return base + "_첨삭메모.json"

    @staticmethod
    def _out_path(full):
        base, _ = os.path.splitext(full)
        return base + "_첨삭본.md"

    def do_POST(self):
        if urlparse(self.path).path != "/api/save":
            return self._send(404, json.dumps({"error": "not found"}))

        n = int(self.headers.get("Content-Length", 0))
        try:
            payload = json.loads(self.rfile.read(n).decode("utf-8"))
        except Exception as e:
            return self._send(400, json.dumps({"error": "잘못된 요청: %s" % e}, ensure_ascii=False))

        try:
            full = safe_path(payload["rel"])
        except Exception as e:
            return self._send(400, json.dumps({"error": str(e)}, ensure_ascii=False))

        head = payload.get("head", "")
        paras = payload.get("paragraphs", [])
        originals = payload.get("originals", [])
        comments = payload.get("comments", [])
        overall = payload.get("overall", "").strip()

        out_path = self._out_path(full)
        memo_path = self._memo_path(full)

        # 편집 중 문단 안에 빈 줄이 생기면 별도 문단으로 갈라 준다
        parts = []
        for p in paras:
            for seg in re.split(r"\n\s*\n", p.strip()):
                if seg.strip():
                    parts.append(seg.strip())
        body = "\n\n".join(parts)
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(head.rstrip() + "\n\n" + body + "\n")

        changed = []
        for i, (o, e) in enumerate(zip(originals, paras)):
            if o.strip() != e.strip():
                changed.append({"n": i + 1, "original": o, "edited": e})

        memo = {
            "source": payload["rel"],
            "output": os.path.relpath(out_path, ROOT).replace("\\", "/"),
            "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "paragraph_count": len(paras),
            "changed_count": len(changed),
            "comment_count": len(comments),
            "overall": overall,
            "changed": changed,
            "comments": comments,
        }
        with open(memo_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(memo, f, ensure_ascii=False, indent=2)

        return self._send(200, json.dumps({
            "ok": True,
            "output": memo["output"],
            "memo": os.path.relpath(memo_path, ROOT).replace("\\", "/"),
            "changed": len(changed),
            "comments": len(comments),
            "overall": bool(overall),
        }, ensure_ascii=False))


class LocalServer(HTTPServer):
    """루프백 전용 서버.

    allow_reuse_address를 끈다. Windows에서 이 옵션이 켜져 있으면
    이미 쓰는 포트에 두 번째 서버가 그대로 붙어버려, 낡은 서버가
    살아 있는 줄 모르고 계속 쓰게 된다.
    """
    allow_reuse_address = False


class LocalServer6(LocalServer):
    """브라우저가 localhost를 ::1로 먼저 해석하는 경우를 위한 IPv6 창구."""
    address_family = socket.AF_INET6


def lan_ip():
    """이 PC의 사설망 주소를 알아낸다(패킷은 나가지 않는다)."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        return s.getsockname()[0]
    except OSError:
        return None
    finally:
        s.close()


def main():
    ap = argparse.ArgumentParser()
    # PORT 환경변수가 있으면 그것을 기본값으로 쓴다(프리뷰 자동 포트 지원).
    default_port = int(os.environ.get("PORT", "8787"))
    ap.add_argument("--port", type=int, default=default_port)
    ap.add_argument("--lan", action="store_true",
                    help="같은 네트워크(와이파이)의 다른 기기에서도 접속을 받는다")
    args = ap.parse_args()

    host4 = "0.0.0.0" if args.lan else "127.0.0.1"
    try:
        srv4 = LocalServer((host4, args.port), Handler)
    except OSError as e:
        print("포트 %d를 열 수 없다: %s" % (args.port, e))
        print("이미 첨삭 서버가 떠 있는지 확인하거나 --port 로 다른 번호를 쓴다.")
        print("떠 있는 서버 찾기:  netstat -ano | findstr :%d" % args.port)
        sys.exit(1)

    # ::1은 별도 소켓으로 받는다. ::1에 바인딩한 소켓은 IPv4를 받지 못하고,
    # ::(전체)에 바인딩하면 외부에까지 열리므로 둘을 따로 연다.
    # (--lan일 때는 IPv4 쪽이 이미 전체를 받으므로 ::1은 보조일 뿐이다.)
    srv6 = None
    try:
        srv6 = LocalServer6(("::1", args.port), Handler)
        threading.Thread(target=srv6.serve_forever, daemon=True).start()
    except OSError:
        pass

    print("첨삭 도구: http://localhost:%d" % args.port)
    print("           http://127.0.0.1:%d" % args.port)
    if args.lan:
        ip = lan_ip()
        if ip:
            print()
            print("휴대폰(같은 와이파이): http://%s:%d" % (ip, args.port))
            print()
        print("[주의] --lan 모드: 같은 네트워크의 모든 기기가 이 첨삭 도구에")
        print("       접속해 원고를 읽고 첨삭본을 저장할 수 있다. 집 와이파이에서만 쓸 것.")
    print("연결 창구: IPv4%s%s" % ("(전체)" if args.lan else "", " + IPv6" if srv6 else ""))
    print("프로젝트 루트: %s" % ROOT)
    print("중단하려면 Ctrl+C")
    try:
        srv4.serve_forever()
    except KeyboardInterrupt:
        print("\n종료")
    finally:
        srv4.server_close()
        if srv6:
            srv6.server_close()


if __name__ == "__main__":
    main()
