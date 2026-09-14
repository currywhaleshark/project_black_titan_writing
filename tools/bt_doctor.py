# -*- coding: utf-8 -*-
"""bt_doctor.py — 상태 문서 무결성 검사

`05_문체_상태_인계`의 스냅샷 계열이 「조용히 동결」되는 사고를 기계가 잡는다.

사용:
    python tools/bt_doctor.py              # 전체 검사
    python tools/bt_doctor.py --only stamp # 검사 1만
    python tools/bt_doctor.py --quiet      # 실패만 출력

검사 (설계안 v1.0 §2):
    [1] 스탬프 — 파일명 회차 == as_of_episode / through_chapter
    [2] 동결   — 연속 스냅샷의 페이로드가 동일한가 (주석 무시)

왜 필요한가 (2026-09-14 신설):
    복선추적기 SNAP-068~101(34개)이 첫 줄 주석만 다르고 페이로드가
    바이트 동일한 채 `as_of_episode: 67`로 굳어 있었다. 2026-08-16과
    2026-08-21 두 번의 복구 기록이 남아 있는데도 재발했다 —
    재발 방지책이 「마감 시 사람이 확인할 것」이었기 때문이다.

    동결이 확인·용인된 파일은 `payload_frozen: true`를 달아 둔다.
    그런 파일은 FAIL이 아니라 KNOWN으로 집계한다. **스탬프만 고쳐
    정상으로 위장하지 말 것** — 그것이 2026-08-21의 실수였다.
"""
import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML이 필요하다: pip install pyyaml\n")
    raise SystemExit(2)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "05_문체_상태_인계")

FROZEN_KEY = "payload_frozen"
MARKER_KEYS = (FROZEN_KEY, "payload_as_of", "frozen_note")

# (표시명, 파일 글롭 정규식, 회차 스탬프 키)
FAMILIES = [
    ("SNAP(본상태)", re.compile(r"^Black_Titan_SNAP-(\d+)_.*\.yaml$"), "through_chapter"),
    ("복선추적기", re.compile(r"^Black_Titan_복선추적기_SNAP-(\d+)_.*\.yaml$"), "as_of_episode"),
]


_CACHE = {}


def load(path):
    """검사마다 다시 파싱하지 않는다 — 285개 × 검사 수만큼 느려진다."""
    if path not in _CACHE:
        with open(path, encoding="utf-8") as fh:
            _CACHE[path] = yaml.safe_load(fh)
    return _CACHE[path]


def collect(pattern):
    """(회차번호, 파일명, 경로) 목록을 회차 순으로."""
    out = []
    for name in sorted(os.listdir(STATE)):
        m = pattern.match(name)
        if m:
            out.append((int(m.group(1)), name, os.path.join(STATE, name)))
    out.sort(key=lambda r: r[0])
    return out


def payload_signature(doc):
    """주석·동결표식을 뺀 내용 지문. 주석은 safe_load 단계에서 이미 사라진다."""
    if not isinstance(doc, dict):
        return repr(doc)
    body = {k: v for k, v in doc.items() if k not in MARKER_KEYS}
    return yaml.safe_dump(body, allow_unicode=True, sort_keys=True, default_flow_style=False)


def check_stamp(label, files, stamp_key):
    """[1] 파일명 회차와 스탬프 값이 같은가."""
    fails, knowns = [], []
    for no, name, path in files:
        doc = load(path)
        if not isinstance(doc, dict):
            fails.append((name, "YAML 최상위가 매핑이 아니다"))
            continue
        got = doc.get(stamp_key)
        if got == no:
            continue
        msg = "%s=%r (파일=%d)" % (stamp_key, got, no)
        (knowns if doc.get(FROZEN_KEY) else fails).append((name, msg))
    return fails, knowns


def check_freeze(label, files, strict=False):
    """[2] 연속 스냅샷의 페이로드가 동일한가.

    동결 여부는 **자기 자신의 표식**으로 판정한다. `payload_frozen: true`가
    붙은 파일은 「내 내용은 갱신 안 됐다」고 스스로 선언한 것이므로, 앞
    파일과 같아도 FAIL이 아니다. 앞 파일까지 표식을 요구하면 동결 구간의
    첫 파일이 영원히 FAIL로 남는다(SNAP-068이 그랬다).

    `--strict`는 표식을 무시하고 날것의 그림을 보여 준다.
    """
    fails, knowns = [], []
    prev_sig = prev_name = None
    for no, name, path in files:
        doc = load(path)
        sig = payload_signature(doc)
        frozen = bool(isinstance(doc, dict) and doc.get(FROZEN_KEY))
        if prev_sig is not None and sig == prev_sig:
            msg = "%s 와 페이로드 동일" % prev_name
            (knowns if (frozen and not strict) else fails).append((name, msg))
        prev_sig, prev_name = sig, name
    return fails, knowns


def report(title, fails, knowns, quiet):
    status = "FAIL" if fails else "PASS"
    if fails or not quiet:
        print("[%s] %s — 실패 %d건, 확인된 동결 %d건" % (status, title, len(fails), len(knowns)))
    for name, msg in fails:
        print("    FAIL  %s : %s" % (name, msg))
    if knowns and not quiet:
        if len(knowns) <= 3:
            for name, msg in knowns:
                print("    KNOWN %s : %s" % (name, msg))
        else:
            print("    KNOWN %s … 외 %d건 (payload_frozen 표시됨)"
                  % (knowns[0][0], len(knowns) - 1))
    return len(fails)


def main():
    ap = argparse.ArgumentParser(description="상태 문서 무결성 검사")
    ap.add_argument("--only", choices=["stamp", "freeze"], help="검사 하나만 실행")
    ap.add_argument("--quiet", action="store_true", help="실패만 출력")
    ap.add_argument("--strict", action="store_true",
                    help="payload_frozen 표식을 무시하고 날것으로 검사")
    args = ap.parse_args()

    if not os.path.isdir(STATE):
        sys.stderr.write("상태 폴더를 못 찾았다: %s\n" % STATE)
        return 2

    total = 0
    for label, pattern, stamp_key in FAMILIES:
        files = collect(pattern)
        if not files:
            print("[SKIP] %s — 파일 없음" % label)
            continue
        if not args.quiet:
            print("\n── %s (%d개, EP%d~EP%d)" % (label, len(files), files[0][0], files[-1][0]))
        if args.only in (None, "stamp"):
            total += report("검사1 스탬프 / %s" % label, *check_stamp(label, files, stamp_key),
                            quiet=args.quiet)
        if args.only in (None, "freeze"):
            total += report("검사2 동결 / %s" % label,
                            *check_freeze(label, files, strict=args.strict),
                            quiet=args.quiet)

    print("\n== 총 실패 %d건 ==" % total)
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
