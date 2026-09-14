# -*- coding: utf-8 -*-
"""bt_extract_foreshadow.py — 회차델타에서 복선 구조화 초안을 뽑는다

동결 구간(EP068~101)의 복선이 약어로만 남아 있다. 각 회차델타의
`foreshadow:` 블록에는 원문이 살아 있으므로, 기계로 뽑히는 필드를 채운
**초안**을 만들어 사람이 판정만 하게 한다.

사용:
    python tools/bt_extract_foreshadow.py --range 77 92
    python tools/bt_extract_foreshadow.py --range 77 92 --out draft.yaml
    python tools/bt_extract_foreshadow.py --range 77 92 --summary

기계로 뽑는 것:
    planted_at        델타의 `(NN)` 표기 또는 해당 회차
    surface_reading   항목 원문
    weight            ★ 개수
    next_window       `→ EPnn` 화살표
    last_progressed   이후 회차 델타에서 같은 이름이 다시 나온 마지막 회차
    status            회수/완성 표현이 있으면 RESOLVED 후보

사람이 판정할 것 (TODO로 남긴다):
    id · line · secret_layer · allowed_reveal_now · prohibited_reveal_now

    ★ 마지막 두 필드는 「지금 어디까지 써도 되나」라는 추적기의 실사용
      목적 전부다. 추정으로 채우면 틀린 봉인 정보를 정본으로 만드는
      것이라 동결보다 나쁘다. 반드시 비워서 내보낸다.
"""
import argparse
import glob
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EPROOT = os.path.join(ROOT, "10_회차")

CLOSE_WORDS = ("회수 완료", "회수완료", "완성", "종료", "소진", "폐기", "발동")
NEW_WORDS = ("신규",)


def delta_path(ep):
    hits = glob.glob(os.path.join(EPROOT, "*_EP%03d_*" % ep))
    if not hits:
        return None
    p = os.path.join(hits[0], "Black_Titan_EP%03d_회차델타_v1.0.yaml" % ep)
    return p if os.path.isfile(p) else None


def foreshadow_items(ep):
    """해당 회차 델타의 foreshadow: 항목 원문 목록."""
    path = delta_path(ep)
    if not path:
        return []
    out, cap = [], False
    with open(path, encoding="utf-8") as fh:
        for line in fh.read().split("\n"):
            if line.startswith("foreshadow:"):
                cap = True
                continue
            if cap and re.match(r"^[a-z_]+:", line):
                break
            if cap and line.strip().startswith("- "):
                out.append(line.strip()[2:].strip().strip('"'))
    return out


def thread_name(item):
    m = re.search(r"FS-([^(:.·]+)", item)
    if not m:
        return None
    return re.sub(r"\*+", "", m.group(1)).strip().rstrip(":").strip()


def parse_item(ep, item):
    name = thread_name(item)
    if not name:
        return None
    planted = ep
    m = re.search(r"\((\d{2,3})\)", item)
    if m and 1 <= int(m.group(1)) <= 200:
        planted = int(m.group(1))
    m = re.search(r"\((\d{2,3})\s*→", item)
    if m:
        planted = int(m.group(1))
    nxt = None
    m = re.search(r"→\s*\*{0,2}EP\s*(\d{2,3})", item)
    if m:
        nxt = "EP%03d" % int(m.group(1))
    return {
        "name": name,
        "planted_at": planted,
        "weight": item.count("★"),
        "is_new": any(w in item for w in NEW_WORDS),
        "closing": any(w in item for w in CLOSE_WORDS),
        "next_window": nxt,
        "surface_reading": re.sub(r"\s+", " ", item).strip(),
        "first_ep": ep,
    }


def scan_progression(name, lo, hi):
    """이후 회차에서 같은 이름이 다시 언급된 회차들."""
    key = name.replace(" ", "")
    eps = []
    for ep in range(lo, hi + 1):
        for item in foreshadow_items(ep):
            if key in item.replace(" ", ""):
                eps.append(ep)
                break
    return eps


def current_entries(path):
    """현행 추적기의 구조화 항목을 {id: 본문텍스트}로."""
    import yaml
    with open(path, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    out = {}
    for sec in ("active", "resolved"):
        for k, v in (doc.get(sec) or {}).items():
            body = k
            if isinstance(v, dict):
                body += " " + " ".join(str(x) for x in v.values())
            out[k] = body.replace(" ", "")
    return out


def find_successors(name, entries):
    """S11 스레드가 어느 현행 항목 안으로 접혀 들어갔나."""
    key = name.replace(" ", "")
    return [k for k, body in entries.items() if key in body]


def slug(ep, idx):
    return "FS-S11-%03d%s" % (ep, "ABCDEFGH"[idx])


def main():
    ap = argparse.ArgumentParser(description="회차델타 → 복선 구조화 초안")
    ap.add_argument("--range", nargs=2, type=int, metavar=("FROM", "TO"), required=True)
    ap.add_argument("--scan-to", type=int, default=142, help="진행 추적 상한 회차")
    ap.add_argument("--out", help="초안 YAML 저장 경로")
    ap.add_argument("--summary", action="store_true", help="표만 출력")
    ap.add_argument("--all", action="store_true", help="신규가 아닌 진전 항목도 포함")
    args = ap.parse_args()

    lo, hi = args.range
    cur = os.path.join(ROOT, "05_문체_상태_인계",
                       "Black_Titan_복선추적기_SNAP-142_v1.0.yaml")
    entries = current_entries(cur) if os.path.isfile(cur) else {}
    rows = []
    for ep in range(lo, hi + 1):
        idx = 0
        for item in foreshadow_items(ep):
            rec = parse_item(ep, item)
            if not rec:
                continue
            if not rec["is_new"] and not args.all:
                continue
            rec["id"] = slug(ep, idx)
            idx += 1
            later = scan_progression(rec["name"], hi + 1, args.scan_to)
            rec["last_progressed"] = later[-1] if later else ep
            rec["later_eps"] = later
            rec["successors"] = find_successors(rec["name"], entries)
            # 자동 추적 실패를 「소멸」로 읽히게 하지 않는다 — 판정은 사람 몫.
            if rec["closing"]:
                rec["status"] = "RESOLVED?"
            elif later or rec["successors"]:
                rec["status"] = "SIMMERING?"
            else:
                rec["status"] = "TODO"
            rows.append(rec)

    if args.summary or not args.out:
        print("EP%03d~EP%03d 신규 복선 %d건 (진행추적 ~EP%d)\n" % (lo, hi, len(rows), args.scan_to))
        print("%-15s %-4s %-4s %-11s %-24s %s" % ("id", "심김", "별", "상태", "현행 후속 항목", "이름"))
        print("-" * 108)
        for r in rows:
            suc = r["successors"]
            tag = suc[0] if len(suc) == 1 else ("%s 외 %d" % (suc[0], len(suc) - 1) if suc else "—")
            print("%-15s %-4d %-4s %-11s %-24s %s" % (
                r["id"], r["planted_at"], "★" * min(r["weight"], 3),
                r["status"], tag[:24], r["name"]))
        res = sum(1 for r in rows if r["status"] == "RESOLVED?")
        sim = sum(1 for r in rows if r["status"] == "SIMMERING?")
        todo = sum(1 for r in rows if r["status"] == "TODO")
        print("\n합계 %d건 — 종결 후보 %d · 후속 확인됨 %d · 미확인 %d"
              % (len(rows), res, sim, todo))
        print("※ 상태는 전부 제안일 뿐이다. 확정과 봉인 판정은 사람이 한다.")

    if args.out:
        lines = ["# 자동 생성 초안 — bt_extract_foreshadow.py",
                 "# ★ allowed/prohibited_reveal_now 는 사람이 채운다. 추정 금지.",
                 "active:"]
        for r in rows:
            lines += [
                "  %s:" % r["id"],
                "    name: %s" % r["name"],
                "    line: TODO",
                "    secret_layer: TODO",
                "    planted_at: %d" % r["planted_at"],
                "    surface_reading: '%s'" % r["surface_reading"].replace("'", "''"),
                "    allowed_reveal_now: TODO",
                "    prohibited_reveal_now: TODO",
                "    last_progressed: %d" % r["last_progressed"],
                "    next_window: %s" % (r["next_window"] or "TODO"),
                "    status: %s" % r["status"],
            ]
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print("\n초안 저장: %s (%d건)" % (args.out, len(rows)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
