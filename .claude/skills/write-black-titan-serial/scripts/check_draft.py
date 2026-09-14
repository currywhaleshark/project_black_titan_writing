#!/usr/bin/env python3
"""Check a Project Black Titan draft for source-firewall and style signals."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


DEFAULT_WARNINGS = (
    "국방정보본부 제6국",
    "미확인 위협 대응 조사단",
    "서인태",
    "김유찬",
    "이도훈",
    "박우석",
    "윤혜린",
    "민기준",
    "강철원",
    "이현수",
    "단목항",
    "황산지구",
)

# 작가용 개체 분류 표기. 지면에는 절대 나오지 않는다 — 등장인물은
# 저것들을 분류해서 부르지 않는다. `가재`·`문어`·`성게` 같은 생물
# 이름을 비유로 쓰는 것은 정상이고, **`-형`이 붙는 순간 작가용**이다.
# EP52 초고에서 `문어형`이 샜고, 승인본에서도 EP9·EP10·EP48에서
# 같은 유출이 발견됐다(2026-08-13).
CREATURE_TAXA = (
    "성게형",
    "집게형",
    "문어형",
    "가재형",
    "바닷가재형",
    "농게형",
    "갯지렁이형",
    "관갯지렁이",
    "군부형",
    "투구게형",
    "따개비형",
    "등각류",
    "딱총새우형",
    "톡토기형",
    "공작갯가재형",
    "크릴형",
    "갯민숭달팽이형",
    "갑오징어형",
    "가오리형",
    "바다나리",
    # ── 「형」 없는 어간도 유출이다 (EP70에서 `톡토기 무리`가 통과했다) ──
    # 일반 어휘로도 쓰이는 것(문어·집게·가재·농게·성게·크릴·갑오징어·가오리·따개비)은
    # 오탐이 나므로 제외한다. 인물은 `그 긴 거`·`도약하던 놈`처럼 부른다.
    "톡토기",
    "공작갯가재",
    "딱총새우",
    "갯민숭달팽이",
    "투구게",
)

QUOTE_STARTS = ("“", "\"", "‘", "'")

CLICHE_ACTIONS = (
    "이를 악물",
    "입술을 깨물",
    "주먹을 쥐",
    "숨을 삼켰",
    "숨을 삼키",
    "마른침",
    "눈을 질끈 감",
)

ONOMATOPOEIA = (
    "쾅",
    "쿵",
    "쿠웅",
    "콰앙",
    "철컥",
    "끼익",
    "우지끈",
    "퍼억",
    "퍽",
    "탕",
    "삑",
    "부우웅",
)

CONTRAST_PAIR = re.compile(
    r"(?:않았다|아니었다|못했다|없었다|몰랐다)"
    r"[^.!?\n]{0,24}[.!?]?\s*"
    r"(?:그래도|그런데도|오히려|하지만)"
)


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    raw = Path(path).read_text(encoding="utf-8")
    return strip_front_matter(raw)


def strip_front_matter(raw: str) -> str:
    """머리말 표(문서 ID·상태·정정 반영 등)를 본문 검사에서 뺀다.

    그 표는 작가용 메타데이터라서 `군부형`·`성게형` 같은 작가용 명칭이
    정당하게 들어간다. 2026-08-14 회귀 검사에서 EP38·EP44의 `정정 반영`
    칸이 지면 유출로 잡혀 확인한 결과 **본문에는 0건**이었다.
    본문 시작 = 첫 번째 단독 `---` 구분선 다음.
    """
    lines = raw.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "---" and i > 0:
            return "\n".join(lines[i + 1:])
    return raw


def load_extra_terms(path: str | None) -> list[str]:
    if not path:
        return []
    return [
        line.strip()
        for line in Path(path).read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def analyze(
    text: str,
    warnings: list[str],
    target_characters: int,
    tolerance: float,
) -> dict[str, object]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    compact = re.sub(r"\s+", "", text)
    dialogue = [p for p in paragraphs if p.startswith(QUOTE_STARTS)]
    short = [p for p in paragraphs if len(re.sub(r"\s+", "", p)) <= 20]
    hits = [
        {"term": term, "count": text.count(term)}
        for term in warnings
        if term in text
    ]
    anchor_hits = [
        {"term": "아이언 앵커", "count": text.count("아이언 앵커"),
         "note": "Verify current-canon introduction timing."}
        for _ in [0]
        if "아이언 앵커" in text
    ]
    naming_hits = [
        {
            "term": term,
            "count": text.count(term),
            "note": (
                "Verify speaker, viewpoint, and record owner. Only current "
                "family name-holders or neutral author narration may use it."
            ),
        }
        for term in ("블랙 타이탄", "타이탄")
        if term in text
    ]
    naming_hits += [
        {
            "term": term,
            "count": text.count(term),
            "note": (
                "AUTHOR-ONLY TAXON — must not appear in prose. Use a "
                "sensory description, `그것`, or a month + `괴수`."
            ),
        }
        for term in CREATURE_TAXA
        if term in text
    ]
    cliche_hits = [
        {"term": term, "count": text.count(term)}
        for term in CLICHE_ACTIONS
        if term in text
    ]
    onomatopoeia_hits = [
        {"term": term, "count": len(re.findall(re.escape(term), text))}
        for term in ONOMATOPOEIA
        if term in text
    ]
    contrast_pair_count = len(CONTRAST_PAIR.findall(text))
    past_ending_run = longest_past_ending_run(text)
    repetition = repetition_rates(text)
    style_warnings = []
    if contrast_pair_count > 3:
        style_warnings.append(
            f"contrast-pair count {contrast_pair_count} exceeds warning band 3"
        )
    for hit in cliche_hits:
        if hit["count"] >= 2:
            style_warnings.append(
                f"cliche action repeated: {hit['term']} ({hit['count']})"
            )
    if sum(hit["count"] for hit in onomatopoeia_hits) > 12:
        style_warnings.append("onomatopoeia density is high; inspect by scene")
    if repetition["deictic_rate"] > 29.4:
        style_warnings.append(
            "deictic-opener rate {deictic_rate} per-mille exceeds band 29.4"
            " ({deictic} sentences); an expansion pass likely cloned frames"
            .format(**repetition)
        )
    if repetition["closer_rate"] > 67.5:
        style_warnings.append(
            "judgement-closer rate {closer_rate} per-mille exceeds band 67.5"
            " ({closer} sentences); vary how the narration settles"
            .format(**repetition)
        )
    if past_ending_run > 8:
        style_warnings.append(
            f"past-tense ending run {past_ending_run} exceeds warning band 8"
        )

    total_paragraphs = len(paragraphs)
    character_count = len(compact)
    minimum = round(target_characters * (1 - tolerance))
    maximum = round(target_characters * (1 + tolerance))
    length_pass = minimum <= character_count <= maximum
    return {
        "characters_no_space": character_count,
        "target_character_range": [minimum, maximum],
        "length_pass": length_pass,
        "paragraphs": total_paragraphs,
        "average_paragraph_characters": (
            round(len(compact) / total_paragraphs, 2) if total_paragraphs else 0
        ),
        "dialogue_paragraph_ratio": (
            round(len(dialogue) / total_paragraphs, 4) if total_paragraphs else 0
        ),
        "short_paragraph_ratio": (
            round(len(short) / total_paragraphs, 4) if total_paragraphs else 0
        ),
        "forbidden_term_hits": hits,
        "timing_warnings": anchor_hits,
        "knowledge_warnings": naming_hits,
        "style_diagnostics": {
            "contrast_pair_count": contrast_pair_count,
            "cliche_action_hits": cliche_hits,
            "onomatopoeia_hits": onomatopoeia_hits,
            "longest_past_ending_run": past_ending_run,
            "repetition_rates": repetition,
            "warnings": style_warnings,
        },
        "lexical_firewall_pass": not hits,
        "last_paragraph": paragraphs[-1] if paragraphs else "",
    }


DEICTIC_OPENER = re.compile(r"^(그건|그게|그것도|그것은|그거는)(?= |$)")
SPECIAL_CLOSER = re.compile(
    r"(것이다|뜻이다|셀이다|모른다|모르겠다"
    r"|것이었다|뜻이었다)\.$"
)


def repetition_rates(text: str) -> dict:
    """Narration-only rate of deictic openers and judgement closers.

    Both are the signature of an expansion pass that copied the draft's own
    sentence frames instead of adding new information. Bands are the 97th
    percentile measured across the approved corpus.
    """
    sentences = [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+|\n+", text)
        if len(sentence.strip()) > 4
    ]
    narration = [
        sentence
        for sentence in sentences
        if not sentence.startswith(('"', "“"))
    ]
    total = len(narration)
    if not total:
        return {"deictic": 0, "closer": 0, "deictic_rate": 0.0, "closer_rate": 0.0}
    deictic = sum(1 for s in narration if DEICTIC_OPENER.search(s))
    closer = sum(1 for s in narration if SPECIAL_CLOSER.search(s))
    return {
        "deictic": deictic,
        "closer": closer,
        "deictic_rate": round(deictic * 1000 / total, 1),
        "closer_rate": round(closer * 1000 / total, 1),
    }


def longest_past_ending_run(text: str) -> int:
    sentences = [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+|\n+", text)
        if sentence.strip()
    ]
    longest = 0
    current = 0
    for sentence in sentences:
        normalized = sentence.rstrip("”’\"' ")
        if re.search(r"(?:았다|었다|였다|했다)\.$", normalized):
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="UTF-8 text files or - for stdin")
    parser.add_argument("--forbidden-file", help="One extra warning term per line")
    parser.add_argument("--target-chars", type=int, default=5500)
    parser.add_argument("--tolerance", type=float, default=0.15)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    warnings = list(DEFAULT_WARNINGS)
    warnings.extend(load_extra_terms(args.forbidden_file))
    results = []
    failed = False

    for path in args.paths:
        result = analyze(
            read_text(path),
            warnings,
            args.target_chars,
            args.tolerance,
        )
        result["path"] = path
        results.append(result)
        failed = failed or not (
            bool(result["lexical_firewall_pass"])
            and bool(result["length_pass"])
        )

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for result in results:
            status = (
                "PASS"
                if result["lexical_firewall_pass"] and result["length_pass"]
                else "FAIL"
            )
            print(f"[{status}] {result['path']}")
            print(
                "  chars={characters_no_space} paragraphs={paragraphs} "
                "avg_para={average_paragraph_characters} "
                "dialogue={dialogue_paragraph_ratio:.1%} "
                "short={short_paragraph_ratio:.1%}".format(**result)
            )
            for hit in result["forbidden_term_hits"]:
                print(f"  forbidden: {hit['term']} ({hit['count']})")
            for warning in result["timing_warnings"]:
                print(f"  timing: {warning['term']} — {warning['note']}")
            for warning in result["knowledge_warnings"]:
                print(
                    f"  knowledge: {warning['term']} ({warning['count']})"
                    f" — {warning['note']}"
                )
            diagnostics = result["style_diagnostics"]
            print(
                "  style: contrast={contrast_pair_count} "
                "past_run={longest_past_ending_run} "
                "deictic={0[deictic_rate]} closer={0[closer_rate]}".format(
                    diagnostics["repetition_rates"], **diagnostics
                )
            )
            for warning in diagnostics["warnings"]:
                print(f"  style warning: {warning}")
            if not result["length_pass"]:
                low, high = result["target_character_range"]
                print(
                    f"  length: {result['characters_no_space']} "
                    f"(required {low}–{high})"
                )
            print(f"  ending sample: {result['last_paragraph'][:160]}")

    return 2 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
