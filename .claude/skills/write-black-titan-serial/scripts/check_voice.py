# -*- coding: utf-8 -*-
"""화계(존댓말/반말) 드리프트 점검기.

EP44~45에서 단아가 영진에게 존댓말을 쓰는 드리프트가 났고, 초고
단계에서 아무도 못 잡았다. 그 종류는 기계로 잡힌다.

정본 화계
    단아 → 영진   반말   (EP1 `할아버지, 이거 언제 만든 거야?`)
    단아 → 교사·의사·낯선 어른  존댓말
    수아 → 영진   존댓말
    수아 → 단아   반말
    혜정·예진·성호 등 또래끼리  반말

이 스크립트는 대사 앞뒤의 서술에서 화자를 추정한다. 추정이므로
확정 판정을 하지 않고 **검토 목록**을 만든다. WARN만 눈으로 보면
한 회차에 열 줄 안쪽이다.

사용:
    python check_voice.py <초고.md> [...]
    python check_voice.py <초고.md> --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# 존댓말 종결 — 대사 끝에서만 본다.
# `…다니까`처럼 반말인데 `니까`로 끝나는 것을 걸러야 하므로
# 합니다체는 `습니다/ㅂ니다/습니까` 형태로만 잡는다.
HONORIFIC = re.compile(
    r"(요|습니다|ㅂ니다|입니다|습니까|ㅂ니까|입니까|세요|셔요|십시오)"
    r"[.?!…]*$"
)
# 대사 안의 호칭 — 청자를 직접 알려 주는 가장 강한 단서
ADDRESS = {
    "언니": "단아",
    "할아버지": "영진",
    "선생님": "어른",
    "누나": "단아",
}
# 화자 단서 — 대사 바로 앞뒤 서술에서 찾는다
SPEAKERS = ("단아", "수아", "영진", "혜정", "예진", "성호", "한결",
            "하랑", "주호", "명준", "서진", "기태",
            "루시", "가온", "도윤", "현서", "헤일")
# 존댓말이 정상인 청자
POLITE_OK_FOR_DANA = ("선생님", "의사", "간호사", "아저씨", "아주머니",
                      "대위", "사령관", "어른")
# 이 이름들이 주변에 있으면 존댓말이 정상이다(손님·거래처·심판 등)
POLITE_CONTEXT = ("기태", "미란", "정호", "우진", "나래", "아줌마", "아저씨",
                  "손님", "심판", "선생님", "의사", "간호사", "대위",
                  # 가을 신규(2026-08-24) — 아이들에게 낯선 어른이라 존댓말이 정상이다
                  "루시", "가온", "도윤", "현서", "헤일", "치료사", "언니")

QUOTE = ('"', "“", "‘", "'")

# 서술문 안의 3인칭 지칭 — 단아·수아 시점에서 영진은 `할아버지`다.
# EP50에서 `저 사람`이 두 번 새어 나갔고 화계 검사가 대사만 보고
# 있어서 못 잡았다. 대사 안은 검사하지 않는다(화자가 가리키는
# 대상이 영진이 아닐 수 있다 — `이건 그 사람한테 물어야 한다`).
# `저 사람들`(구경하는 사람들)처럼 복수형은 영진 지칭이 아니므로 뺀다.
REFERENCE_BAD = (r"저 사람(?!들)", r"그 노인", r"그 양반", r"그 늙은이",
                 r"노인[은이]\s")
REFERENCE_CHECK = (r"그 사람(?!들)",)


# ── 루시 (2026-08-24 신설) ──────────────────────────────────────────
# 대사는 말투 카드 가을 v1.0 §1이, 서술은 narration-lucy-pov.md가 맡는다.
# 여기서 잡는 것은 그 카드들의 금지 항목 가운데 기계로 걸리는 것들이다.

# 루시 대사 — 교과서체다. 축약·반문·감탄사·말줄임이 없다.
LUCY_SAY = (
    (r"[…]|\.\.\.", "말줄임 — 루시는 문장을 끝낸다"),
    (r"^(아|어|음|와|야|에이|헐|우와|어머)[,\s]", "감탄사 — 루시 금지"),
    (r"잖아|그치|맞죠|거든|겠죠|네요\?", "반문·동의 구하기 — 루시 금지"),
    (r"뭐야|뭐예요|어때\?|어딨|어딘가|이런\b", "축약·구어 — 루시는 축약을 안 한다"),
    (r"처럼|마치|~듯", "비유 — 루시는 비유로 말하지 않는다"),
    (r"(?<!블랙 )타이탄", "약칭 「타이탄」은 가족 전용(G0-022)"),
    (r"수아 씨", "★ 「수아 씨」는 권도윤의 인장이다(EP119) — 루시 아님"),
)

# 루시 시점 서술 — 대사와 규칙이 다르다. 유창하되 비유가 없고,
# 감정에 이름이 안 붙고, 자기 몸을 이름으로 안 부른다.
LUCY_NARR = (
    (r"(습니다|입니다|습니까|십시오)[.?!]?$",
     "서술문에 경어체 — 대사 자산이 샜다(서술 카드 §1)"),
    (r"처럼|마치|듯이", "비유 — 루시는 비유로 생각하지 않는다(§4)"),
    (r"부러[웠운]|외로[웠운]|질투|서운|샘이 났|부끄러",
     "★ 감정 명명 — 루시는 자기 감정에 이름을 못 붙인다(§2-3)"),
    (r"센티널[이가은는]", "전투 서술의 주어가 「센티널」 — 자기 몸이다(§3-1)"),
    (r"(?<!블랙 )타이탄", "약칭 「타이탄」은 가족 전용(G0-022)"),
    (r"[…]|\.\.\.", "말줄임 — 루시 서술에는 없다(§7)"),
    (r"배양|탄두.{0,6}도포", "★★ 배양 공정은 루시도 모른다(G0-023 §4-2)"),
    (r"수리점", "★ 루시는 수리점을 모른다(LOC-08 §2)"),
)

# 루시 시점 판정 — 서술문에서 단아를 `도단아`라고 부르는 사람은 루시뿐이다.
LUCY_POV_MARK = re.compile(r"도단아")


def load_body(path: str) -> list[str]:
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


def is_dialogue(p: str) -> bool:
    return p.startswith(QUOTE)


ATTRIB = (r"(말했다|물었다|불렀다|대답했다|덧붙였다|중얼|받았다|"
          r"목소리|하고 말|이었다|였다)")


def nearest_speaker(blocks: list[str], i: int) -> tuple[str, str]:
    """대사 블록 i의 화자를 추정한다. (화자, 근거)

    1차: 바로 붙은 서술(i-1, i+1)의 귀속 표현(`수아가 말했다`).
    2차: 바로 붙은 서술의 인물 이름(약한 단서).
    3차: 두 칸 떨어진 서술의 귀속 표현(약한 단서).

    거리를 먼저 좁힌다. 두 칸 떨어진 `단아가 말했다`가 바로 위의
    `수아는 설정 화면을 열었다`를 이기면 안 된다 — EP25·EP46이
    그렇게 오판됐다.
    """
    def attrib_in(b: str) -> str:
        for s in SPEAKERS:
            if re.search(s + r"[가이는은]?\s*[^.]{0,14}" + ATTRIB, b):
                return s
        return ""

    def name_in(b: str) -> str:
        # 이름이 여럿이면 SPEAKERS 나열 순서가 아니라 문장에 먼저
        # 나오는 쪽을 쓴다. 서술의 주어가 대개 앞에 온다.
        found = sorted((b.index(s), s) for s in SPEAKERS if s in b)
        return found[0][1] if found else ""

    def block(j: int) -> str:
        if not (0 <= j < len(blocks)) or is_dialogue(blocks[j]):
            return ""
        return blocks[j]

    for j in (i - 1, i + 1):
        b = block(j)
        if b and attrib_in(b):
            return attrib_in(b), b[:40]
    for j in (i - 1, i + 1):
        b = block(j)
        if b and name_in(b):
            return name_in(b), "(약한 단서) " + b[:34]
    for j in (i - 2, i + 2):
        b = block(j)
        if b and attrib_in(b):
            return attrib_in(b), "(약한 단서) " + b[:34]
    return "", ""


# 호칭 뒤에 이 조사가 붙으면 청자가 아니라 화제다.
# EP108 `할아버지는요.`— 현서에게 영진을 묻는 말이다(2026-08-24).
TOPIC_JOSA = re.compile(r"^(은|는|이|가|을|를|도|의|한테|께서|랑|과|와|보다|처럼|만)")


def addressee(line: str) -> str:
    """대사 안의 호칭으로 청자를 직접 읽는다.

    호격에만 쓴다 — 조사가 붙은 것은 그 사람을 **가리키는** 말이지
    그 사람에게 **하는** 말이 아니다.
    """
    for word, who in ADDRESS.items():
        for m in re.finditer(re.escape(word), line):
            if not TOPIC_JOSA.match(line[m.end():]):
                return who
    return ""


def window_text(blocks: list[str], i: int) -> str:
    return " ".join(blocks[max(0, i - 2):i + 3])


def audience_hint(blocks: list[str], i: int) -> str:
    window = window_text(blocks, i)
    hits = [s for s in SPEAKERS if s in window]
    hits += [s for s in POLITE_OK_FOR_DANA if s in window]
    return "/".join(dict.fromkeys(hits))


def scan_reference(blocks: list[str]) -> list[dict]:
    """서술문의 3인칭 지칭을 훑는다. 대사는 건드리지 않는다."""
    rows = []
    for p in blocks:
        if is_dialogue(p):
            continue
        for pat in REFERENCE_BAD:
            m = re.search(pat, p)
            if m:
                # 가드의 취지는 「손자가 조부를 3인칭 물건처럼 부르는 것」이다.
                # 낯선 사람을 `저 사람`이라 하는 것은 정상이므로
                # 영진 단서가 같은 문단에 있을 때만 WARN을 준다.
                near = bool(re.search(r"할아버지|영진", p))
                rows.append({
                    "line": p[:60], "speaker": "서술", "around": m.group(0),
                    "level": "WARN" if near else "CHECK",
                    "note": "서술문의 `%s` — %s"
                            % (m.group(0),
                               "단아·수아 시점에서 영진은 `할아버지`" if near
                               else "가리키는 대상 확인 — 영진이면 `할아버지`"),
                    "evidence": ""})
        for pat in REFERENCE_CHECK:
            m = re.search(pat, p)
            if m:
                rows.append({
                    "line": p[:60], "speaker": "서술", "around": m.group(0),
                    "level": "CHECK",
                    "note": "서술문의 `%s` — 가리키는 대상 확인" % m.group(0),
                    "evidence": ""})
    return rows


def strip_quoted(p: str) -> str:
    """서술문 안에 낀 인용 부분을 뺀다. 서술 검사는 서술만 본다."""
    return re.sub(r"[\"“][^\"”]*[\"”]", " ", p)


def is_lucy_pov(blocks: list[str], path: str) -> bool:
    """서술문에서 단아를 `도단아`로 반복해 부르면 루시 시점이다.

    풀네임 호칭은 루시 카드에만 있다(narration-lucy-pov.md §6).
    다만 인물 첫 노출 규칙(서술규칙편 §6-6)도 풀네임을 쓰므로
    봄편이 통째로 오탐됐다(2026-08-24). 두 가지로 좀힌다:
    **EP121 이후**이고 **서술문에 두 번 이상** 나올 때만.
    """
    m = re.search(r"EP(\d{3})", path)
    if not m or int(m.group(1)) < 121:
        return False
    n = sum(1 for p in blocks
            if not is_dialogue(p) and LUCY_POV_MARK.search(strip_quoted(p)))
    return n >= 2


def scan_lucy(blocks: list[str], pov: str, path: str) -> list[dict]:
    """루시 대사와 루시 시점 서술을 카드 금지 항목으로 훑는다."""
    rows = []
    lucy_pov = (pov == "lucy") or (pov == "auto" and is_lucy_pov(blocks, path))

    for i, p in enumerate(blocks):
        if is_dialogue(p):
            speaker, why = nearest_speaker(blocks, i)
            # 루시 시점 회차에서는 화자 미상 대사도 루시일 확률이 높지만
            # 단정하지 않는다 — 이름이 잡힌 것만 본다.
            # 루시 시점 회차에서는 본인 대사에 화자가 안 붙는다.
            # 이름이 잡힐 것은 WARN, 미상은 CHECK로 내려서 둔다.
            if speaker == "루시":
                lv = "WARN"
            elif lucy_pov and not speaker:
                lv, why = "CHECK", "루시 시점 · 화자 미상 — 루시인지 확인"
            else:
                continue
            line = p.strip().strip('"“”')
            for pat, note in LUCY_SAY:
                if re.search(pat, line):
                    rows.append({"line": line[:60], "speaker": "루시",
                                 "around": "", "level": lv,
                                 "note": note, "evidence": why})
        elif lucy_pov:
            text = strip_quoted(p).strip()
            if not text:
                continue
            for pat, note in LUCY_NARR:
                if re.search(pat, text, re.M):
                    rows.append({"line": text[:60], "speaker": "서술",
                                 "around": "", "level": "WARN",
                                 "note": note, "evidence": "루시 시점"})
    if lucy_pov:
        rows.append({"line": "(회차 판정)", "speaker": "서술", "around": "",
                     "level": "OK", "note": "루시 시점으로 보고 서술 검사를 돌렸다",
                     "evidence": "도단아" if pov == "auto" else "--pov lucy"})
    return rows

def analyze(path: str, pov: str = "auto") -> dict:
    blocks = load_body(path)
    rows = scan_reference(blocks)
    rows += scan_lucy(blocks, pov, path)
    for i, p in enumerate(blocks):
        if not is_dialogue(p):
            continue
        line = p.strip().strip('"“”')
        polite = bool(HONORIFIC.search(line))
        speaker, why = nearest_speaker(blocks, i)
        around = audience_hint(blocks, i)
        # POLITE_CONTEXT는 요약된 around가 아니라 서술 원문에서 찾는다.
        # `미란 아줌마가 선풍기를 찾으러 왔다`는 around에 안 남는다.
        window = window_text(blocks, i)
        to = addressee(line)
        weak = why.startswith("(약한 단서)")

        level = None
        note = ""
        if polite and speaker == "단아":
            if to == "영진":
                level, note = "WARN", "단아가 할아버지에게 존댓말 — 반말이어야 한다"
            elif to in ("어른",) or any(w in window for w in POLITE_CONTEXT):
                level, note = "OK", "단아 존댓말 — 어른 청자(정상)"
            elif weak:
                level, note = "CHECK", "단아 존댓말(화자 추정 약함) — 청자 확인"
            elif re.search(r"할아버지|영진", window):
                level, note = "WARN", "단아 존댓말 — 영진에게라면 반말이어야 한다"
            else:
                # S13~ 단아는 어른과만 말하는 회차가 많다.
                # 청자 단서가 없을 때까지 WARN을 주면 전부 오탐이 된다.
                level, note = "CHECK", "단아 존댓말 — 청자 확인(어른 상대면 정상)"
        elif polite and any(w in window for w in POLITE_CONTEXT):
            level, note = "OK", "존댓말 — 어른·거래처 청자 단서 있음"
        elif polite and speaker in ("혜정", "예진", "성호", "한결"):
            level, note = "CHECK", "또래 존댓말 — 청자 확인(장난·상급자일 수 있음)"
        elif not polite and speaker == "수아":
            if to == "단아":
                level, note = "OK", "수아 반말 — 언니에게(정상)"
            elif re.search(r"영진에게|할아버지에게", " ".join(blocks[max(0, i-1):i+2])):
                level, note = "WARN", "수아가 영진에게 반말 — 존댓말이어야 한다"
        elif polite and speaker == "수아":
            level, note = "OK", "수아 존댓말"
        elif polite and not speaker:
            level, note = "CHECK", "존댓말인데 화자 미상 — 눈으로 확인"

        if level:
            rows.append({"line": line[:60], "speaker": speaker or "?",
                         "around": around, "level": level, "note": note,
                         "evidence": why})
    counts = {}
    for r in rows:
        counts[r["level"]] = counts.get(r["level"], 0) + 1
    return {"path": path, "rows": rows, "counts": counts,
            "warn": counts.get("WARN", 0)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--pov", default="auto",
                    choices=["auto", "lucy", "other"])
    args = ap.parse_args()

    failed = False
    results = [analyze(p, args.pov) for p in args.paths]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            status = "WARN" if r["warn"] else "PASS"
            print("[%s] %s" % (status, r["path"]))
            print("  " + "  ".join("%s=%d" % kv for kv in sorted(r["counts"].items())))
            for row in r["rows"]:
                if row["level"] in ("WARN", "CHECK"):
                    print("  %-5s %-4s %s" % (row["level"], row["speaker"], row["line"]))
                    print("        · %s" % row["note"])
                    if row["around"]:
                        print("        · 주변: %s" % row["around"])
    failed = any(r["warn"] for r in results)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
