# -*- coding: utf-8 -*-
"""merge_s11_foreshadow.py — S11 복선 제안본을 SNAP-142에 병합한다 (1회성)

동결 구간 EP077~092의 복선이 약어로만 남아 있던 것을, 승인된 제안본의
구조화 항목으로 현행 추적기에 넣는다.

    python tools/merge_s11_foreshadow.py --dry-run
    python tools/merge_s11_foreshadow.py --apply

원칙:
  - **SNAP-142만 고친다.** SNAP-102~141은 소급하지 않는다(사용자 결정
    2026-09-14). 대신 그 사실을 파일 안에 명기한다.
  - 기존 항목은 한 줄도 건드리지 않는다. 각 절 끝에 덧붙이기만 한다.
  - 검토용 필드(`_근거`·`_확신도`)는 제거하고 넣는다.
  - YAML 덤프로 전체를 다시 쓰지 않는다 — 주석과 서식이 날아간다.
    앵커를 찾아 텍스트로 삽입한다.

원본 백업: 99_묶음백업/2026-09-14_S11복선병합_전/
"""
import argparse
import os
import sys

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(ROOT, "05_문체_상태_인계",
                      "Black_Titan_복선추적기_SNAP-142_v1.0.yaml")
SOURCE = os.path.join(ROOT, "tmp", "s11복구", "S11_복선_제안본_v0.1.yaml")

REVIEW_FIELDS = ("_근거", "_확신도")

STAMP = ("EP142 Gate D 승인 · **★★★★★★ S15 개막(현서 과거)** — 신규 4건"
         "(현서 전사 · 고래상어형=지휘개체 원형 · 카버 얕음 · 같은 재료 전투근거)"
         " / **★★★ 2026-09-14 S11 복구** — EP077~092 동결 구간 복선 18건 구조화"
         "(active 8 · resolved 9 · retired 1). 근거 = 각 회차 회차델타 foreshadow 블록")

BANNER = [
    "",
    "# ═══ 2026-09-14 S11 복구분 (EP077~092) ═══════════════════════════",
    "# 동결 구간(복선추적기 SNAP-068~101)에서 약어로만 남아 있던 복선을",
    "# 각 회차 회차델타의 foreshadow 블록을 근거로 구조화해 넣었다.",
    "# ★ 이 복구는 SNAP-142에만 반영한다. SNAP-102~141은 소급하지 않았다",
    "#   (사용자 결정 2026-09-14) — 실사용은 최신본 하나이기 때문이다.",
    "#   그 구간의 과거 스냅샷을 읽을 때는 이 절이 없다는 것을 감안할 것.",
    "# ★ SNAP-068~101 자체는 payload_frozen: true 로 표시돼 있다.",
]


def render(entries):
    """{id: dict} 를 2칸 들여쓴 YAML 텍스트 줄 목록으로."""
    out = []
    for key, val in entries.items():
        body = {k: v for k, v in val.items() if k not in REVIEW_FIELDS}
        text = yaml.safe_dump({key: body}, allow_unicode=True,
                              sort_keys=False, default_flow_style=False,
                              width=10 ** 6)
        out.extend(("  " + ln) if ln.strip() else ln
                   for ln in text.rstrip("\n").split("\n"))
    return out


def main():
    ap = argparse.ArgumentParser(description="S11 복선 제안본 → SNAP-142 병합")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    with open(SOURCE, encoding="utf-8") as fh:
        src = yaml.safe_load(fh)
    with open(TARGET, encoding="utf-8") as fh:
        cur = yaml.safe_load(fh)

    # 충돌 검사 — 같은 id 가 이미 있으면 중단한다.
    existing = set()
    for sec in ("active", "resolved", "retired"):
        existing |= set((cur.get(sec) or {}).keys())
    clash = sorted(k for sec in ("active", "resolved", "retired")
                   for k in (src.get(sec) or {}) if k in existing)
    if clash:
        sys.stderr.write("id 충돌 — 중단: %s\n" % ", ".join(clash))
        return 1

    with open(TARGET, encoding="utf-8", newline="") as fh:
        raw = fh.read()
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.split(nl)

    def find(prefix):
        for i, ln in enumerate(lines):
            if ln.startswith(prefix):
                return i
        raise SystemExit("앵커를 못 찾음: %s" % prefix)

    counts = {s: len(src.get(s) or {}) for s in ("active", "resolved", "retired")}

    # 뒤에서부터 삽입해야 앞쪽 줄번호가 안 밀린다.
    i_ret = find("retired:")
    ret_block = BANNER + render(src.get("retired") or {})
    if lines[i_ret].strip() == "retired: {}":
        lines[i_ret:i_ret + 1] = ["retired:"] + ret_block
    else:
        lines[i_ret + 1:i_ret + 1] = ret_block

    i_res = find("retired:")          # 갱신된 위치 — resolved 절의 끝
    lines[i_res:i_res] = BANNER + render(src.get("resolved") or {}) + [""]

    i_act = find("resolved:")         # active 절의 끝
    lines[i_act:i_act] = BANNER + render(src.get("active") or {}) + [""]

    i_stamp = find("last_updated_by:")
    lines[i_stamp] = "last_updated_by: %s" % STAMP

    text = nl.join(lines)

    # 검증 — 파싱되는가, 기존 항목이 그대로 있는가, 신규가 다 들어갔는가.
    new = yaml.safe_load(text)
    for sec in ("active", "resolved", "retired"):
        before = set((cur.get(sec) or {}).keys())
        after = set((new.get(sec) or {}).keys())
        lost = before - after
        if lost:
            sys.stderr.write("기존 항목 소실 — 중단: %s\n" % ", ".join(sorted(lost)))
            return 1
        added = after - before
        want = set((src.get(sec) or {}).keys())
        if added != want:
            sys.stderr.write("삽입 불일치 %s: 넣으려던 %d, 들어간 %d\n"
                             % (sec, len(want), len(added)))
            return 1
        print("  %-9s 기존 %3d + 신규 %2d = %3d" % (sec, len(before), len(added), len(after)))
    if (new.get("ep_log_068_102") or {}) != (cur.get("ep_log_068_102") or {}):
        sys.stderr.write("ep_log_068_102 변형 — 중단\n")
        return 1

    if args.apply:
        with open(TARGET, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
        print("\n적용 완료: %s" % os.path.basename(TARGET))
    else:
        print("\n예행 — 검증 통과. 파일은 안 건드렸다. (신규 %d건)" % sum(counts.values()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
