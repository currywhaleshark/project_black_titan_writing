# -*- coding: utf-8 -*-
"""mark_frozen_trackers.py — 동결된 복선추적기에 사실을 명시한다 (A안 · 1회성)

복선추적기 SNAP-068~101(34개)은 페이로드가 SNAP-067 단계에 굳어 있다.
내용을 고치는 것이 아니라 **굳어 있다는 사실을 파일에 적는다.**

    payload_frozen: true
    payload_as_of: 67
    frozen_note: "…"

★ 스탬프(`as_of_episode`)는 건드리지 않는다. 내용이 EP067인 파일에
  EP101 도장을 찍으면 동결이 정상으로 위장된다 — 2026-08-21의 실수가
  그것이었다.

사용:
    python tools/mark_frozen_trackers.py --dry-run
    python tools/mark_frozen_trackers.py --apply

원본 백업: 99_묶음백업/2026-09-14_복선추적기_동결표시_전/
"""
import argparse
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "05_문체_상태_인계")

FIRST, LAST = 68, 101
PAYLOAD_AS_OF = 67
ANCHOR = "as_of_episode:"

NOTE = (
    "EP068~101 구간 미반영 — 페이로드는 SNAP-067 단계에서 동결됐다. "
    "2026-08-21 복구는 SNAP-102 이후에 ep_log_068_102 요약을 붙이는 데 "
    "그쳤고 이 파일들은 다시 쓰이지 않았다. "
    "복구 근거는 각 회차 회차델타의 foreshadow 블록"
    "(10_회차/*_EP0NN_승인완료/Black_Titan_EP0NN_회차델타_v1.0.yaml). "
    "★ as_of_episode만 고쳐 정상으로 위장하지 말 것."
)

BLOCK = [
    "# ★ 2026-09-14 동결 확인 — bt_doctor.py 검사1·2 적발. 내용 미복구 상태를 명시한다.",
    "payload_frozen: true",
    "payload_as_of: %d" % PAYLOAD_AS_OF,
    "frozen_note: >-",
]


def wrap_note(text, width=72, indent="  "):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(indent + cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(indent + cur)
    return lines


def process(path, apply_):
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()

    if "payload_frozen:" in text:
        return "SKIP (이미 표시됨)"

    nl = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(nl)

    idx = next((i for i, ln in enumerate(lines) if ln.startswith(ANCHOR)), None)
    if idx is None:
        return "FAIL (%s 줄을 못 찾음)" % ANCHOR

    block = BLOCK + wrap_note(NOTE)
    lines[idx + 1:idx + 1] = block

    if apply_:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(nl.join(lines))
    return "OK (+%d줄, %s 뒤)" % (len(block), ANCHOR)


def main():
    ap = argparse.ArgumentParser(description="동결 복선추적기에 표시를 넣는다")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true", help="바꾸지 않고 결과만")
    g.add_argument("--apply", action="store_true", help="실제로 쓴다")
    args = ap.parse_args()

    ok = bad = 0
    for n in range(FIRST, LAST + 1):
        name = "Black_Titan_복선추적기_SNAP-%03d_v1.0.yaml" % n
        path = os.path.join(STATE, name)
        if not os.path.isfile(path):
            print("  없음  %s" % name)
            bad += 1
            continue
        res = process(path, args.apply)
        print("  %-28s %s" % ("SNAP-%03d" % n, res))
        if res.startswith("FAIL"):
            bad += 1
        else:
            ok += 1

    mode = "적용" if args.apply else "예행"
    print("\n== %s: 정상 %d건, 문제 %d건 ==" % (mode, ok, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
