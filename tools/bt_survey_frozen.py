# -*- coding: utf-8 -*-
"""bt_survey_frozen.py — 동결 구간 전체 복구 범위 산정 (1회성 조사)

EP068~101 회차델타의 foreshadow 항목을 전수 집계하고, 현행 추적기
SNAP-142에 구조화돼 있는지 대조해 남은 작업량을 낸다.

    python tools/bt_survey_frozen.py
    python tools/bt_survey_frozen.py --from 68 --to 101

분류:
  [A] 구조화됨   현행 active/resolved/retired 에 항목이 있다
  [B] 약어만     ep_log_068_102 에만 흔적이 있다
  [C] 없음       어디에도 없다
"""
import argparse
import collections
import glob
import os
import re
import sys

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EPROOT = os.path.join(ROOT, "10_회차")
TRACKER = os.path.join(ROOT, "05_문체_상태_인계",
                       "Black_Titan_복선추적기_SNAP-142_v1.0.yaml")

# 아크 경계 — 아크캡슐 S10~S12 의 「범위」 행에서 확정
ARCS = [("S10", 62, 76), ("S11", 77, 92), ("S12", 93, 103)]


def arc_of(ep):
    for name, lo, hi in ARCS:
        if lo <= ep <= hi:
            return name
    return "?"


def items(ep):
    hits = glob.glob(os.path.join(EPROOT, "*_EP%03d_*" % ep))
    if not hits:
        return []
    path = os.path.join(hits[0], "Black_Titan_EP%03d_회차델타_v1.0.yaml" % ep)
    if not os.path.isfile(path):
        return []
    out, cap = [], False
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.startswith("foreshadow:"):
            cap = True
            continue
        if cap and re.match(r"^[a-z_]+:", line):
            break
        if cap and line.strip().startswith("- "):
            out.append(line.strip()[2:].strip().strip('"'))
    return out


def name_of(item):
    m = re.search(r"FS-([^(:.·]+)", item)
    return re.sub(r"\*+", "", m.group(1)).strip().rstrip(":").strip() if m else None


# 「새로 심겼다」는 표기가 회차대에 따라 다르다.
# EP068~076 = 개시·신설·해금 / EP077~ = 신규 로 통일됐다.
# 한 표기만 보면 앞 구간이 통째로 0으로 나온다.
NEW_MARKS = ("신규", "개시", "신설", "해금")


def is_new(item):
    return any(w in item for w in NEW_MARKS)


def mark_of(item):
    for w in NEW_MARKS:
        if w in item:
            return w
    return "—"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="lo", type=int, default=68)
    ap.add_argument("--to", dest="hi", type=int, default=101)
    args = ap.parse_args()

    doc = yaml.safe_load(open(TRACKER, encoding="utf-8"))
    struct = ""
    for sec in ("active", "resolved", "retired"):
        for k, v in (doc.get(sec) or {}).items():
            struct += k + " " + (" ".join(str(x) for x in v.values())
                                 if isinstance(v, dict) else "")
    struct = struct.replace(" ", "")
    eplog = " ".join(str(v) for v in (doc.get("ep_log_068_102") or {}).values()).replace(" ", "")

    rows = []
    for ep in range(args.lo, args.hi + 1):
        for it in items(ep):
            nm = name_of(it)
            if not nm:
                continue
            key = nm.replace(" ", "")
            cls = "A" if key in struct else ("B" if key in eplog else "C")
            rows.append({
                "ep": ep, "arc": arc_of(ep), "name": nm,
                "new": is_new(it), "mark": mark_of(it),
                "w": min(it.count("★"), 3), "cls": cls,
            })

    print("동결 구간 EP%03d~EP%03d — 회차델타 복선 항목 전수 %d건\n" % (args.lo, args.hi, len(rows)))

    print("── 아크 × 분류 (신규만) ─────────────────────────────────")
    print("%-6s %-8s %5s %5s %5s %6s" % ("아크", "회차", "[A]", "[B]", "[C]", "신규계"))
    for name, lo, hi in ARCS:
        sub = [r for r in rows if r["arc"] == name and r["new"]]
        if not sub:
            continue
        c = collections.Counter(r["cls"] for r in sub)
        eps = sorted({r["ep"] for r in sub})
        print("%-6s %-8s %5d %5d %5d %6d" % (
            name, "EP%d~%d" % (eps[0], eps[-1]),
            c["A"], c["B"], c["C"], len(sub)))
    allnew = [r for r in rows if r["new"]]
    c = collections.Counter(r["cls"] for r in allnew)
    print("%-6s %-8s %5d %5d %5d %6d" % ("계", "", c["A"], c["B"], c["C"], len(allnew)))

    print("\n── 남은 작업(= [B]+[C]) 등급별 ──────────────────────────")
    print("%-6s %5s %5s %5s %6s" % ("아크", "★★★", "★★", "★", "소계"))
    tot = collections.Counter()
    for name, lo, hi in ARCS:
        sub = [r for r in rows if r["arc"] == name and r["new"] and r["cls"] in "BC"]
        if not sub:
            continue
        c = collections.Counter(r["w"] for r in sub)
        tot.update(c)
        print("%-6s %5d %5d %5d %6d" % (name, c[3], c[2], c[1] + c[0], len(sub)))
    left = [r for r in allnew if r["cls"] in "BC"]
    print("%-6s %5d %5d %5d %6d" % ("계", tot[3], tot[2], tot[1] + tot[0], len(left)))

    print("\n── 회차별 남은 신규 ─────────────────────────────────────")
    per = collections.Counter(r["ep"] for r in left)
    line = []
    for ep in range(args.lo, args.hi + 1):
        line.append("%d:%d" % (ep, per.get(ep, 0)))
    for i in range(0, len(line), 12):
        print("   " + "  ".join(line[i:i + 12]))

    print("\n── 신규 표기 분포 (회차대별 어휘 차이) ──────────────────")
    mk = collections.Counter((r["arc"], r["mark"]) for r in rows if r["new"])
    for (arc, m), n in sorted(mk.items()):
        print("   %-5s %-4s %3d건" % (arc, m, n))

    prog = [r for r in rows if not r["new"]]
    print("\n※ 신규 외 진전 항목 %d건은 별도. 기존 스레드의 last_progressed 갱신용이며"
          "\n   새 항목을 만들지 않는다." % len(prog))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
