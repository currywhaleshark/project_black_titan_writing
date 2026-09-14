# -*- coding: utf-8 -*-
"""check_continuity.py — 전수감사(2026-08-16)에서 기계 검사가 못 잡던 층위를 잡는다.

usage: python check_continuity.py <draft.md> [--ep N]

4개 검사:
  [1] 인물 감시목록 — 이름이 나오면 반 배치·역할·화계를 경고로 띄운다 (판단은 사람이)
  [2] 시간 지시어 추출 — 어제/그저께/지난주/N일 만 전부 나열 (달력 대조는 사람이)
  [3] 봉인 어휘 — 회차 번호 기준 해금 전 어휘 (통증 긍정형은 EP70 해금)
  [4] 축자 중복 — 승인 전 회차 코퍼스와 18자 이상 문장 완전 일치 + 틱 어휘 밀도

전부 WARN이다. FAIL은 [3]의 봉인 어휘뿐. 나머지는 눈으로 확인하라고 꺼내 놓는 것.
"""
import io
import glob
import os
import re
import sys

# ── [1] 인물 감시목록 — 전수감사에서 실제로 틀렸던 것 위주 ──────────────
# (이름, 경고문)  이름이 지면에 있으면 무조건 띄운다. 맞게 썼어도 띄운다.
WATCHLIST = [
    ("소개지구",  "행정·군 용어(G0-015). 주민·아이들 대사면 오용 — 주민은 「벽 바깥」"),
    ("하구래",    "5년 전 소개된 벽 바깥 어촌(G0-015). **미란 출신은 아직 미공개** — 밝히려면 승인"),
    ("대수몰",    "구도심 침수 사건(G0-015). 「5년 전」과 다른 시점 — 혼동 금지"),
    ("문재호",  "3학년(수아 반). 단아 교실 장면이면 오배치 — 단아 반은 장우진"),
    ("재호",    "3학년(수아 반). 단아 교실 장면이면 오배치 — 단아 반은 장우진"),
    ("배유림",  "3학년(수아 반). 단아 교실 장면이면 오배치"),
    ("유림",    "3학년(수아 반). 단아 교실 장면이면 오배치"),
    ("임유정",  "3학년 담임(수아네). 단아네 조회·수업이면 오배치 — 단아네 담임은 김주호"),
    ("김주호",  "단아네 담임(40대 남교사). 학생·반 친구로 쓰면 오배치. 사정 안 캐묻는 인물"),
    ("주호",    "단아네 담임(40대 남교사). 학생·반 친구로 쓰면 오배치"),
    ("이하랑",  "3학년·수아와 다른 반·바이올린. 비밀 직감 금지. 케이스는 가로로"),
    ("하랑",    "3학년·다른 반. 비밀 직감 금지. 봄에 쉼표 못 셌음(EP67에서 터득)"),
    ("성호",    "단아와 라이벌·앙숙 — 친한 친구처럼 직접 수다 금지. 거인 기록원(관련 화면·소문 앞 무반응 금지). EP57 목격 = 언덕(옥상 아님)"),
    ("혜정",    "짧게 여러 번(19자 내외·만연체 금지). 어디·왜는 안 묻는다. 잔소리는 명령형"),
    ("예진",    "길이가 완충 도구(설명이 길어도 됨). 단아·수아에게 반말 정본 확인"),
    ("장우진",  "단아 반. 큰 손짓·후드 주머니 한 손. 실제 경보 때 입 닫힘"),
    ("최나래",  "단아 반. 거인 만화가(공책·몽당연필·결론만 한 줄). 만화는 실제를 따라온다"),
    ("강한결",  "단아 반"),
    ("배정호",  "동네 조연 — 간격 장부 확인"),
    ("박기태",  "영진→기태 = 하게체(~하게/~잖나/~되나). `~해` 명령형 금지. 단아→기태 존댓말"),
    ("기태",    "영진→기태 = 하게체. `~해` 명령형 금지"),
    ("오미란",  "영진→미란 화계 = 존댓말 쪽 정본(EP33 `~습니다`). 해라체 주의"),
    ("미란",    "영진→미란 화계 = 존댓말 쪽 정본. 해라체 주의"),
    ("명준",    "영진 대면 해금(EP114). 셋 중 이 부대에 있는 사람 0 — 영진=경찰·단아=시설·수아=병원"),
    ("윤서진",  "명준의 부관. 새 참모 만들지 말고 이 사람을 쓴다. 안 묻는 얼굴은 EP115에서 회수됨"),
    ("도현서",  "EP108부터 실물 등장 허용. `엄마가` 자칭 금지 · 사과 금지"),
    ("수아",    "재활 목표는 걷기가 아니라 휠체어(S16 퇴원). EP119는 첫 걸음이 아니라 첫 이동"),
    ("단아",    "★ 단순한 애다. 몸이 먼저 알고 말이 나중에 붙는다 / 앞으로 굴러가지 뒤로 되짚지 않는다 / 자기 분석·요약 정리 금지. 시설 회차(104~109)의 분석 과잉은 상황 탓이지 기본값 아님"),
    ("루시",    "EP116 등장·대사 해금. 교과서체·축약 0·관용구 0 / 감정은 영어로 샌다 / 시점 개시는 EP121 / ★ EP124부터 무장·역장을 담담하게 말한다(G0-023) — 단, 배양 공정은 루시도 모른다 / 출생 폭로는 S15"),
]

# ── [3] 봉인 어휘 (해금 회차, 패턴, 설명) ──────────────────────────────
# (해금 회차, 패턴, 설명, 심각도)  hard=FAIL / soft=WARN(주체·문맥 판단 필요)
SEALED = [
    (70, re.compile(r"아[프팠픈]"), "통증 어휘 — EP70 해금. 부정형(`아픈 건 아니고`)이면 통과 — 문맥 확인", "soft"),
    (70, re.compile(r"저리|저렸|저림|욱신|쑤시|쑤셨"), "신경 증상 어휘 — EP70 해금", "hard"),
    # ★ 재활실 훈련용 계단 모형은 기구이지 건물 동선이 아니다(LOC-07B 정본 · 2026-08-24)
    (9999, re.compile(r"(?<![가-힣])계단(?!\s*모형)(?![가-힣])"), "지하 동선 = 승강기(G0-013). 집·가게는 단층 — 계단 지면 노출 원칙 금지", "hard"),
    (9999, re.compile(r"정전|정전표|순번표"), "★ 순환정전은 봄 한때(열교환탑 복구) — 여름·가을에 끌어다 쓰면 오류", "soft"),
    (9999, re.compile(r"갯벌"), "어휘 분리 — 지면은 `뻘` 계열", "hard"),
    (116, re.compile(r"센티널|화이트"), "화이트 센티널 — EP116 해금(G0-022). 루시·미측 발화만. 단아는 못 외운 상태 유지", "soft"),
    (9999, re.compile(r"인트라넷"), "정본 대체어 = 내부망", "hard"),
    (9999, re.compile(r"오 년 전"), "5년 전 = 벽 바깥 소개(G0-015). 구도심·대수몰을 가리키면 오류", "soft"),
    (9999, re.compile(r"[『』《》〈〉]"), "대사 부호 드리프트 — 정본은 교신·회상 포함 전부 큰따옴표", "hard"),
    (9999, re.compile(r"보정값[을이] (바꾸|되돌|고치|조정|입력)"), "보정값 = 실체 없는 위장 설명(정본카드 12-C) — 값 조작 연출 금지", "hard"),
    (9999, re.compile(r"팔짱"), "영진이면 왼팔 결손 위반. 성호·혜정이면 통과 — 주체 확인", "soft"),
    (9999, re.compile(r"역장|동종성"), "역장 — EP124 해금(G0-023). ★ 루시 시점만. 단아·수아 시점이면 위반", "soft"),
    (9999, re.compile(r"XLG|근접요격|이십 밀리|20mm"), "센티널 무장 — EP124 해금(G0-023). 루시 시점만", "soft"),
    (9999, re.compile(r"배양금속|탄두.{0,6}도포|도포.{0,6}탄두"), "★ 배양 공정은 영구 봉인(§7-B) — 루시도 모른다. 앵커 원리를 역산당한다", "hard"),
]

# ── [2] 시간 지시어 ────────────────────────────────────────────────────
TIME_WORDS = re.compile(
    r"그끄저께|그저께|어제|엊그제|오늘|내일|모레|지난주|지난달|이번 주|다음 주|"
    r"[이사나]틀 ?[만전째]|사흘|나흘|닷새|엿새|이레|보름|"
    r"\d+일 ?[만전째]|[한두세네]? ?[주달] ?[만전째]|2주|3주|일주일"
)

TICS = ["반 박자", "한동안", "소리만 났다", "그게 다였다", "그게 전부였다",
        "셈", "그러니까", "어차피"]
# `셈` 2026-08-18 등재 — EP77(6)·EP78(7) 급증. 대체어:
#   계산 / 산수 / 앞뒤 / 아귀 / 이치 / 헤아리다 / 따지다 / 순서 / 짐작 / 말이 된다


def load_corpus(root, exclude_path):
    """승인 전 회차의 문장 집합 (18자 이상, 표·헤더 제외)"""
    sents = {}
    for f in glob.glob(os.path.join(root, "*_EP*_승인완료", "*GateD승인.md")):
        if os.path.abspath(f) == os.path.abspath(exclude_path):
            continue
        ep = os.path.basename(os.path.dirname(f))
        text = io.open(f, encoding="utf-8").read()
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith(("|", "#", "-", "`", ">")):
                continue
            for s in re.split(r"(?<=[.!?])\s+", line):
                s = s.strip().strip('"“”')
                if len(s) >= 18:
                    sents.setdefault(s, ep)
    return sents


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path = sys.argv[1]
    ep = 0
    if "--ep" in sys.argv:
        ep = int(sys.argv[sys.argv.index("--ep") + 1])
    else:
        m = re.search(r"EP(\d+)", os.path.basename(path))
        if m:
            ep = int(m.group(1))

    text = io.open(path, encoding="utf-8").read()
    # 헤더 표 제거(본문만)
    body_lines = [l for l in text.splitlines() if not l.startswith(("|", "#"))]
    fails = 0

    print("=" * 60)
    print("[1] 인물 감시목록")
    seen = set()
    for name, note in WATCHLIST:
        if any(name in seen_n for seen_n in seen):
            continue
        hits = [i + 1 for i, l in enumerate(text.splitlines()) if name in l and not l.startswith(("|", "#"))]
        if hits:
            seen.add(name)
            print("  WARN %-6s L%s — %s" % (name, ",".join(map(str, hits[:6])), note))
    if not seen:
        print("  (없음)")

    print("=" * 60)
    print("[2] 시간 지시어 — 작중달력과 대조할 것")
    n = 0
    for i, l in enumerate(text.splitlines()):
        if l.startswith(("|", "#")):
            continue
        for m in TIME_WORDS.finditer(l):
            a = max(0, m.start() - 14)
            print("  L%-4d …%s…" % (i + 1, l[a:m.end() + 14].strip()))
            n += 1
    if not n:
        print("  (없음)")

    print("=" * 60)
    print("[3] 봉인 어휘 (해금 전 = FAIL)")
    for unlock, pat, note, sev in SEALED:
        for i, l in enumerate(text.splitlines()):
            if l.startswith(("|", "#")):
                continue
            m = pat.search(l)
            if m:
                sealed_now = ep < unlock
                if sealed_now and sev == "hard":
                    tag = "FAIL"
                    fails += 1
                elif sealed_now:
                    tag = "WARN"
                else:
                    tag = "info"
                a = max(0, m.start() - 10)
                print("  %s L%-4d …%s… — %s" % (tag, i + 1, l[a:m.end() + 10].strip(), note))

    print("=" * 60)
    print("[4] 축자 중복 (승인 코퍼스와 18자+ 완전 일치)")
    root = os.path.dirname(os.path.dirname(os.path.abspath(path))) \
        if "_EP" in os.path.basename(os.path.dirname(path)) \
        else os.path.dirname(os.path.abspath(path))
    # 프로젝트 루트 탐색: 승인 폴더가 보이는 곳까지 상향
    probe = os.path.dirname(os.path.abspath(path))
    for _ in range(3):
        if glob.glob(os.path.join(probe, "*_EP*_승인완료")):
            root = probe
            break
        probe = os.path.dirname(probe)
    corpus = load_corpus(root, path)
    dup = 0
    for line in body_lines:
        line = line.strip()
        for s in re.split(r"(?<=[.!?])\s+", line):
            s = s.strip().strip('"“”')
            if len(s) >= 18 and s in corpus:
                print("  WARN [%s] %s" % (corpus[s], s[:56]))
                dup += 1
    if not dup:
        print("  (없음)")
    # 파일 내부 중복 (같은 화 안에서 같은 문장 2회)
    self_seen = {}
    self_dup = 0
    for line in body_lines:
        line = line.strip()
        for s in re.split(r"(?<=[.!?])\s+", line):
            s = s.strip().strip('"“”')
            if len(s) >= 14:
                self_seen[s] = self_seen.get(s, 0) + 1
    for s, c in self_seen.items():
        if c > 1:
            print("  FAIL [같은 화 내부 x%d] %s" % (c, s[:56]))
            self_dup += 1
    fails += self_dup

    for w in TICS:
        c = text.count(w)
        if c >= 3:
            print("  WARN 틱 `%s` × %d — 밀도 확인" % (w, c))

    print("=" * 60)
    print("[FAIL]" if fails else "[PASS]", os.path.basename(path),
          "— FAIL %d건 (WARN은 눈으로 판정)" % fails)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
