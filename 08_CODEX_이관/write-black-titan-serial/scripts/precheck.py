# -*- coding: utf-8 -*-
"""집필 전 정본 스윕 — 승인본 전수 그렙

브리프를 쓰기 전에 반드시 돌린다. 인물·장소·소품·회고 사건 키워드를 받아
승인 회차 본문 전체에서 찾아 **최초 등장**과 **최근 지면**을 뽑는다.

사용:
    python tools/precheck.py 안승우 박기훈 구치소
    python tools/precheck.py --recent 5 사진 서랍
    python tools/precheck.py --all 도현서        # 전 회차 목록

왜 필요한가 (2026-08-22 신설):
    EP109~110에서 정합 오류 6건이 났고 전부 승인본 지면에 답이 있었다.
    EP012 사진 · EP089 구래동 · EP103 해치 · EP100 경보.
    「정독한다」로는 안 지켜져서 도구로 강제한다.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EPROOT = os.path.join(ROOT, "10_회차")
if not os.path.isdir(EPROOT):
    EPROOT = ROOT

EP_RE = re.compile(r"EP(\d{3})")


def approved_chapters():
    """승인본 본문 경로를 회차 순으로."""
    out = []
    for name in os.listdir(EPROOT):
        d = os.path.join(EPROOT, name)
        if not os.path.isdir(d) or "승인완료" not in name:
            continue
        m = EP_RE.search(name)
        if not m:
            continue
        no = int(m.group(1))
        for fn in os.listdir(d):
            if fn.endswith("GateD승인.md") and "화_" in fn:
                out.append((no, os.path.join(d, fn)))
                break
    out.sort()
    return out


def paragraphs(path):
    text = io.open(path, encoding="utf-8").read()
    # 헤더 표 제거 — 첫 --- 이후만 본문
    parts = text.split("\n---\n", 1)
    body = parts[1] if len(parts) > 1 else text
    return [p.strip() for p in body.split("\n\n") if p.strip()]


def sweep(keyword, chapters, recent, show_all):
    hits = []          # (회차, 문단)
    for no, path in chapters:
        for p in paragraphs(path):
            if keyword in p:
                hits.append((no, p))
    if not hits:
        print("  등장 0 — 신규이거나 표기가 다르다")
        return
    eps = sorted({no for no, _ in hits})
    print("  등장 %d회 · %d개 회차" % (len(hits), len(eps)))
    print("  회차: %s" % ", ".join("EP%03d" % e for e in eps))

    def show(label, items):
        for no, p in items:
            body = p.replace("\n", " ")
            if len(body) > 160:
                body = body[:160] + "…"
            print("    [%s EP%03d] %s" % (label, no, body))

    if show_all:
        show("전수", hits)
        return
    first_ep = eps[0]
    first = [h for h in hits if h[0] == first_ep][:2]
    print("  ── 최초 등장")
    show("최초", first)
    tail = [h for h in hits if h[0] != first_ep][-recent:]
    if tail:
        print("  ── 최근")
        show("최근", tail)


def main(argv):
    recent = 3
    show_all = False
    words = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--recent":
            i += 1
            recent = int(argv[i])
        elif a == "--all":
            show_all = True
        else:
            words.append(a)
        i += 1

    if not words:
        print(__doc__)
        return 1

    chapters = approved_chapters()
    if not chapters:
        print("승인본을 못 찾았다: %s" % EPROOT)
        return 2
    print("승인본 %d화 (EP%03d~EP%03d)" % (
        len(chapters), chapters[0][0], chapters[-1][0]))
    for w in words:
        print("\n" + "=" * 58)
        print("■ %s" % w)
        print("=" * 58)
        sweep(w, chapters, recent, show_all)
    print("\n" + "-" * 58)
    print("★ 브리프 §0에 이 결과를 인용으로 붙이기 전에는 브리프가 완성이 아니다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
