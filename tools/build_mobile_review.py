# -*- coding: utf-8 -*-
"""승인 본문과 작업 중 문서를 모바일 첨삭기 HTML 한 장으로 묶는다.

승인완료 폴더를 자동으로 훑으므로, 회차가 늘거나 본문이 고쳐지면
다시 실행하기만 하면 된다. 출력은 tools/black_titan_review.html.

작업 중 문서는 `NN_EPxxx`(승인완료가 아닌) 폴더 가운데 **가장 최근
회차 하나만** 싣는다. 브리프·Level 6·초고 순서이며, 목록에서 승인
본문과 분리해 보여 준다. 회차가 승인되어 폴더가 `_승인완료`로 바뀌면
작업 중 칸은 저절로 비고 승인 목록으로 옮겨 간다.

사용:
    python tools/build_mobile_review.py

발행(같은 주소 유지):
    Artifact 도구에 이 파일 경로와 함께
    url = https://claude.ai/code/artifact/a8be889d-2461-4e8b-804e-b4be0532cd68
"""
import os
import re
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 2026-08-21 폴더 정리 — 회차 폴더가 10_회차/ 하위로 이동했다.
# 회차 스캔은 EPROOT를, 산출물 경로는 ROOT를 쓴다.
EPROOT = os.path.join(ROOT, "10_회차")
if not os.path.isdir(EPROOT):
    EPROOT = ROOT  # 구조 이전 호환
OUT = os.path.join(ROOT, "tools", "black_titan_review.html")
ARTIFACT_URL = "https://claude.ai/code/artifact/a8be889d-2461-4e8b-804e-b4be0532cd68"


def find_episodes():
    """`NN_EPxxx_승인완료` 폴더에서 Gate D 승인 본문을 찾는다."""
    found = []
    names = []
    for name in os.listdir(EPROOT):
        m = re.match(r"^(\d{2,3})_(EP\d{3})_승인완료$", name)
        if m:
            names.append((int(m.group(1)), name, m.group(2)))
    for _, name, eid in sorted(names):
        m = re.match(r"^\d{2,3}_(EP\d{3})_승인완료$", name)
        folder = os.path.join(EPROOT, name)
        for f in sorted(os.listdir(folder)):
            # 본문만 — 검증서·델타·브리프는 제목에 `화_`가 없다
            if f.endswith("_GateD승인.md") and re.search(r"_\d+화_", f):
                found.append((m.group(1), os.path.join(name, f).replace("\\", "/")))
                break
    return found


def find_working():
    """승인 전 `NN_EPxxx` 폴더 가운데 가장 최근 회차의 작업 문서를 찾는다.

    반환: (회차 ID, [(구분, 상대경로), ...]) 또는 None.
    구분별 파일 규칙은 지금까지 써 온 파일명 관례를 따른다.
    """
    folders = []
    for name in os.listdir(EPROOT):
        m = re.match(r"^(\d{2,3})_(EP\d{3})$", name)
        if m and os.path.isdir(os.path.join(EPROOT, name)):
            folders.append((int(m.group(1)), name, m.group(2)))
    if not folders:
        return None

    folders.sort()
    _, name, eid = folders[-1]       # 번호가 제일 큰 = 지금 쓰는 회차
    folder = os.path.join(EPROOT, name)
    picks = []
    for kind, pattern in (
        ("브리프", r"회차브리프"),
        ("Level 6", r"Level6"),
        ("초고", r"_\d+화_"),
    ):
        matches = [
            f for f in sorted(os.listdir(folder))
            if f.endswith(".md") and re.search(pattern, f)
        ]
        if matches:
            # 버전 접미사가 정렬 뒤로 가므로 마지막 매치 = 최신본
            picks.append((kind, os.path.join(name, matches[-1]).replace("\\", "/")))
    return (eid, picks) if picks else None


def find_plans():
    """기획 폴더의 화별개요·골격 문서를 최신 판만 모은다.

    회차 폴더 바깥이라 EPROOT가 아니라 ROOT 기준이다. 같은 문서의
    버전이 여럿이면 접미사를 떼고 묶어 제일 높은 판만 싣는다.
    """
    def ver(name):
        m = re.search(r"_v(\d+)\.(\d+)", name)
        return (int(m.group(1)), int(m.group(2))) if m else (0, 0)

    picks = {}
    for d in sorted(os.listdir(ROOT)):
        if not re.match(r"^\d\d_.*기획$", d):
            continue
        if not os.path.isdir(os.path.join(ROOT, d)):
            continue
        for f in sorted(os.listdir(os.path.join(ROOT, d))):
            if not f.endswith(".md") or not re.search(r"화별개요|Level3_골격", f):
                continue
            stem = re.sub(r"_v[\d.]+.*$", "", f)
            key = (d, stem)
            if key not in picks or ver(f) > picks[key][0]:
                picks[key] = (ver(f), os.path.join(d, f).replace("\\", "/"))

    out = []
    for (d, stem), (_, path) in picks.items():
        m = re.search(r"_(S\d+)_EP(\d+)", stem)
        no = m.group(1) if m else "골격"
        start = int(m.group(2)) if m else -1
        kind = "골격" if "골격" in stem else "개요"
        out.append((d, start, no, kind, stem, path))
    # 폴더 역순(가을→봄) · 폴더 안에서는 회차 역순. 골격은 그 계절 끝에 붙는다
    out.sort(key=lambda r: (r[0], r[1]), reverse=True)
    return [(no, kind, stem, path) for _, _, no, kind, stem, path in out]


def plan_title(text, stem, no=None):
    """개요 문서의 표시 제목. H1에서 프로젝트 접두를 떼고 쓴다.

    목록에서 왼쪽 뱃지가 이미 `S14`를 보여 주므로, 제목이 같은 시즌
    표기로 시작하면 그만큼 떼어 낸다.
    """
    m = re.search(r"^#\s*Project Black Titan\s*[—-]\s*(.+?)\s*$", text, re.M)
    if not m:
        m = re.search(r"^#\s*(.+?)\s*$", text, re.M)
    title = m.group(1).strip() if m else stem
    if no and no != "골격":
        title = re.sub(r"^%s\s+" % re.escape(no), "", title)
    return title


def title_of(text, fallback):
    m = re.search(r"^#\s*Project Black Titan\s*[—-]\s*(\d+화)\s*[「\"'](.+?)[」\"']", text, re.M)
    if m:
        return m.group(1), m.group(2).strip()
    m = re.search(r"^##\s*(\d+화)\.\s*(.+?)\s*$", text, re.M)
    if m:
        return m.group(1), m.group(2).strip()
    return fallback, fallback


def load(path, base=None):
    text = open(os.path.join(base or EPROOT, path), encoding="utf-8").read()
    blocks = []
    for raw in text.split("\n\n"):
        p = raw.strip()
        if not p:
            continue
        if p in ("***", "---") or re.fullmatch(r"#{2,3}\s*\d+", p):
            if blocks and blocks[-1]["k"] != "div":
                blocks.append({"k": "div"})
            continue
        if p.startswith(("#", ">", "|")):
            continue
        blocks.append({"k": "p", "t": p})
    while blocks and blocks[0]["k"] == "div":
        blocks.pop(0)
    while blocks and blocks[-1]["k"] == "div":
        blocks.pop()
    return text, blocks


def load_doc(path, base=None):
    """브리프·Level 6처럼 표와 목록으로 짜인 문서를 구조를 살려 읽는다.

    본문(초고)은 load()를 그대로 쓴다. 이쪽은 제목·표·목록이 곧 내용이라
    버리면 남는 게 없다.
    """
    text = open(os.path.join(base or EPROOT, path), encoding="utf-8").read()
    blocks, para, fence = [], [], None
    cont = [None]      # 들여쓴 줄을 이어 붙일 직전 블록

    def clean(s):
        return re.sub(r"\*\*(.+?)\*\*", r"\1", s).strip()

    def flush():
        if para:
            # 줄바꿈을 넘어가는 강조도 이어 붙인 뒤 한 번 더 벗긴다
            blocks.append({"k": "p", "t": clean(" ".join(para))})
            del para[:]

    for raw in text.split("\n"):
        line = raw.rstrip()
        s = line.strip()

        if s.startswith("```"):
            if fence is None:
                flush()
                fence = []
            else:
                blocks.append({"k": "pre", "t": "\n".join(fence)})
                fence = None
            cont[0] = None
            continue
        if fence is not None:
            fence.append(line)
            continue

        if not s:
            flush()
            cont[0] = None
            continue
        if s == "---":
            flush()
            if blocks and blocks[-1]["k"] != "div":
                blocks.append({"k": "div"})
            cont[0] = None
            continue

        # 목록·인용의 이어지는 줄 — 들여쓰기로 판정해 앞 항목에 붙인다
        if cont[0] is not None and raw[:1] in (" ", "\t") and not re.match(r"^\s*([-*]|\d+\.)\s", raw):
            cont[0]["t"] = clean(cont[0]["t"] + " " + s)
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            flush()
            blocks.append({"k": "h", "lv": min(len(m.group(1)), 4), "t": clean(m.group(2))})
            cont[0] = None
            continue

        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue          # 표 구분선
            flush()
            blocks.append({"k": "tr", "t": "  ·  ".join(clean(c) for c in cells if c)})
            cont[0] = None
            continue

        if s.startswith(">"):
            flush()
            blocks.append({"k": "q", "t": clean(s.lstrip("> "))})
            cont[0] = blocks[-1]
            continue

        m = re.match(r"^([-*]|\d+\.)\s+(.*)$", s)
        if m:
            flush()
            body = clean(m.group(2))
            body = re.sub(r"^\[( |x|X)\]\s*", lambda g: "☐ " if g.group(1) == " " else "☑ ", body)
            blocks.append({"k": "li", "t": body})
            cont[0] = blocks[-1]
            continue

        para.append(clean(s))
        cont[0] = None

    flush()
    while blocks and blocks[0]["k"] == "div":
        blocks.pop(0)
    while blocks and blocks[-1]["k"] == "div":
        blocks.pop()
    return text, blocks


def doc_title(text, kind, eid):
    """작업 문서의 표시 제목. 회차 제목이 있으면 붙인다."""
    m = re.search(r"[「\"'](.+?)[」\"']", text.split("\n")[0])
    return "%s · %s" % (kind, m.group(1).strip()) if m else "%s · %s" % (kind, eid)


def entry(eid, no, title, path, blocks, wip=False, kind=None, plan=False):
    body = [b for b in blocks if b["k"] != "div"]
    return {"id": (eid + "-" + kind) if kind else eid, "no": no, "title": title,
            "src": path, "wip": wip, "plan": plan, "kind": kind or "본문",
            "chars": sum(len(b.get("t", "")) for b in body),
            "paras": len(body), "blocks": blocks}


def build():
    data = []
    for eid, path in find_episodes():
        text, blocks = load(path)
        no, title = title_of(text, eid)
        e = entry(eid, no, title, path, blocks)
        data.append(e)
        print("%s %-14s 문단 %3d  %s자" % (eid, title, e["paras"], format(e["chars"], ",")))

    plans = find_plans()
    if plans:
        print("\n기획 문서 — %d건" % len(plans))
        for no, kind, stem, path in plans:
            text, blocks = load_doc(path, base=ROOT)
            e = entry("PLAN-" + stem, no, plan_title(text, stem, no), path, blocks,
                      wip=True, kind=kind, plan=True)
            data.append(e)
            print("  %-4s %-6s %-46s 항목 %3d  %s자"
                  % (no, kind, e["title"][:46], e["paras"], format(e["chars"], ",")))

    wip = find_working()
    if wip:
        eid, picks = wip
        print("\n작업 중 — %s" % eid)
        for kind, path in picks:
            if kind == "초고":
                text, blocks = load(path)
                no, title = title_of(text, eid)
                e = entry(eid, no, "초고 · " + title, path, blocks, wip=True, kind=kind)
            else:
                text, blocks = load_doc(path)
                e = entry(eid, eid.replace("EP0", "").replace("EP", "") + "화",
                          doc_title(text, kind, eid), path, blocks, wip=True, kind=kind)
            data.append(e)
            print("  %-8s %-22s 항목 %3d  %s자"
                  % (kind, e["title"], e["paras"], format(e["chars"], ",")))

    tpl = open(os.path.join(ROOT, "tools", "review_mobile_template.html"), encoding="utf-8").read()
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    open(OUT, "w", encoding="utf-8", newline="\n").write(tpl.replace("__DATA__", payload))
    n_ok = sum(1 for d in data if not d["wip"])
    n_plan = sum(1 for d in data if d.get("plan"))
    n_wip = sum(1 for d in data if d["wip"]) - n_plan
    print("\n승인 %d화 + 기획 %d건 + 작업 중 %d건 → %s (%s bytes)"
          % (n_ok, n_plan, n_wip, OUT, format(os.path.getsize(OUT), ",")))
    print("발행 시 url: %s" % ARTIFACT_URL)


if __name__ == "__main__":
    build()
