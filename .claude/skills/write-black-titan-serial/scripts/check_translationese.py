# -*- coding: utf-8 -*-
"""번역투 점검기 — 소설 산문용.

출처: im-not-ai(humanize-korean v2.3, MIT)의 AI 티 분류 중
**소설 서술에도 유효한 것만** 골라 옮겼다. 원 도구는 칼럼·리포트·
블로그용이라 규칙 상당수가 이 작품과 충돌한다. 특히 다음은
**의도적으로 가져오지 않았다**:

    E-1  문단마다 100자+ 장문 하나   → 서술규칙편의 단문 리듬과 정면 충돌
    E-2  동일 종결어미 4문장+ 금지   → 과거형 연속은 밴드 8까지 의도적 허용
    D-5  의인화 추상 주어 제거       → `일상이 소문보다 빨랐다`가 이 작품의 목소리
    C-*  불릿·이모지·번호·콜론 헤딩  → 소설 본문에 존재하지 않음
    J-*  볼드 강조                   → 위와 같음

남긴 것은 **번역투와 문어체 침투**뿐이다. 이건 장르와 무관하게
초고에 스며들고, 스며들면 문장이 남의 말투가 된다.

BLOCK = 한 번이라도 나오면 WARN. SOFT = 회차당 한계치를 넘으면 WARN.
한계치는 승인 50화가 전부 통과하도록 잡았다(= 지금까지의 문체가 기준선).

사용:
    python check_translationese.py <원고.md> [...]
    python check_translationese.py <원고.md> --json
    python check_translationese.py <원고.md> --calibrate   # 한계치 조정용 집계
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# ── BLOCK: 한 번이라도 나오면 안 되는 것 ────────────────────────────
BLOCK = [
    ("A-8  이중 피동",
     r"되어지|되어진|지게 된다|보여지|불려지|쓰여지|잊혀지|나뉘어지|"
     r"짜여지|모여지|갈려지",
     "이중 피동. 능동이나 단일 피동으로(`판단되어진다`→`판단된다`)"),
    ("A-9  ~에 의해 피동",
     r"에 의해|에 의하여|에 의한",
     "행위자를 주어로(`파도에 의해 밀렸다`→`파도가 밀었다`)"),
    ("A-7  가지고 있다",
     r"가지고 있|지니고 있",
     "형용사·동사로 환원(`힘을 가지고 있다`→`힘이 세다`)"),
    ("A-16 그녀",
     r"그녀",
     "이 작품은 이름과 호칭을 쓴다. `그녀`는 번역투"),
    ("A-19 이중 조사",
     r"에서의|으로의|에로의|으로부터의|에의 ",
     "절·구로 풀어쓰기(`바다에서의 싸움`→`바다에서 싸운 일`)"),
    ("A-15 만능 동사",
     r"제공한|제공했|제공하는|시사한|반영한다|의미한다",
     "구체 동사로. 추상 주어 + 만능 동사는 번역투"),
    ("D-1  결산 lexicon",
     r"결론적으로|요약하면|그러므로|이를 통해",
     "논설 어휘. 서술에 넣지 않는다"),
]

# ── 가져왔다가 되돌린 규칙 ─────────────────────────────────────────
# 승인 50화로 검증했더니 전부 오탐이거나 의도된 문체였다. 남겨 두면
# 진짜 신호를 덮는다.
#
#   A-3  `~에 있어서`   2/2 오탐 — `자리에 있어서 둘은`처럼 존재의
#                       `있다 + 어서`를 구분할 방법이 없다
#   I-3  `~다는 뜻이다` 5/5 의도 — 단아의 추론 목소리 그 자체다.
#                       `뭔가 해냈다는 뜻이다`(EP48)는 사용자가 직접
#                       쓴 문장이다
#   D-1  `정리하자면`   EP15에서 곧바로 `정리하고 나니 이상한 점이`로
#                       받아 치는 의도된 자리

# ── SOFT: 회차당 한계치 ─────────────────────────────────────────────
# 승인 50화 실측 최댓값 + 여유 1~2를 한계치로 잡았다.
SOFT = [
    ("A-1  ~에 대해/대한", r"에 대해|에 대한|에 대하여", 4,
     "한국어에서 자연스럽지만 몰리면 문어체가 된다"),
    ("A-2  ~를 통해", r"를 통해|을 통해|통하여", 2,
     "일부를 `~로`·`~해서`로 분산"),
    ("H-1  문두 접속사", r"(?m)^(또한|따라서|즉|나아가|아울러|게다가|더욱이)[ ,]", 2,
     "문장 자체가 흐름을 잡게 둔다"),
    ("G-1  추측 종결", r"것으로 보인다|로 판단된|라고 여겨|인 듯하다|로 보여", 2,
     "단언할 수 있는 곳은 단언"),
    # `표적`·`넓적`·`흔적`처럼 어간이 통째로 명사/형용사인 말은 -적 파생이 아니다.
    # EP58에서 `표적`(사격 훈련) 5회가 통째로 오탐돼 한계를 넘겼다 — 어간 제외로 막는다.
    ("F-5  -적 N 체인",
     r"(?:(?!표|넓|흔|기|면|목|실|업|유|자|사|추|정)[가-힣])적(?=[ 가-힣])", 6,
     "한자어 명사화 누적. 어근으로 환원"),
    ("I-4  권고형 결말", r"해야 한다|할 필요가 있다", 2,
     "구체 동사 단언으로"),
]

QUOTE = ('"', "“", "‘", "'")


def load_body(path: str) -> list[str]:
    """머리표를 떼고 문단만 남긴다. check_voice와 같은 규칙."""
    text = Path(path).read_text(encoding="utf-8")
    if "---\n\n" in text:
        text = text.split("---\n\n", 1)[1]
    blocks = []
    for raw in text.split("\n\n"):
        p = raw.strip()
        if not p or p.startswith(("#", "|", ">")) or p == "---":
            continue
        blocks.append(p)
    return blocks


def analyze(path: str) -> dict:
    blocks = load_body(path)
    body = "\n\n".join(blocks)
    rows = []

    for name, pat, fix in BLOCK:
        for m in re.finditer(pat, body):
            s = max(0, m.start() - 22)
            rows.append({"level": "WARN", "rule": name, "hit": m.group(0),
                         "context": body[s:m.end() + 22].replace("\n", " "),
                         "fix": fix})

    counts = {}
    for name, pat, limit, fix in SOFT:
        n = len(re.findall(pat, body))
        counts[name] = n
        if n > limit:
            rows.append({"level": "WARN", "rule": name, "hit": "%d회 (한계 %d)" % (n, limit),
                         "context": "", "fix": fix})

    warn = sum(1 for r in rows if r["level"] == "WARN")
    return {"path": path, "rows": rows, "soft_counts": counts, "warn": warn,
            "chars": len(body)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--calibrate", action="store_true",
                    help="SOFT 항목의 실측 최댓값을 뽑는다(한계치 조정용)")
    args = ap.parse_args()

    results = [analyze(p) for p in args.paths]

    if args.calibrate:
        peak = {}
        for r in results:
            for k, v in r["soft_counts"].items():
                if v > peak.get(k, (-1, ""))[0]:
                    peak[k] = (v, Path(r["path"]).name)
        print("SOFT 실측 최댓값 (%d개 문서)" % len(results))
        for k in sorted(peak):
            v, who = peak[k]
            print("  %-22s %3d   %s" % (k, v, who))
        return 0

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 1 if any(r["warn"] for r in results) else 0

    for r in results:
        print("[%s] %s" % ("WARN" if r["warn"] else "PASS", r["path"]))
        for row in r["rows"]:
            print("  %-22s %s" % (row["rule"], row["hit"]))
            if row["context"]:
                print("      · …%s…" % row["context"])
            print("      → %s" % row["fix"])
    return 1 if any(r["warn"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
