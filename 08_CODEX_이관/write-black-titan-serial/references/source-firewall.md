# Source firewall

## Source labels

- `CANON`: current setting, current plot, and explicit user correction
- `CURRENT_STATE`: approved serial facts through the latest chapter
- `STYLE_ONLY`: old manuscript and revision examples
- `NONCANON_EXPERIMENT`: generated tests and rejected alternatives

Every retrieved passage must have one label before it enters a prompt.

## Content lock

Before consulting `STYLE_ONLY` material, write a content lock containing:

- setting facts used
- characters present
- location and time
- scene events in order
- information revealed or withheld
- initial and final state
- equipment available
- prohibited old facts

Do not alter the content lock merely because an old example contains a
convenient event.

## Allowed transfer from old prose

- sentence and paragraph cadence
- dialogue length and turn-taking
- action–reaction–explanation order
- humor mechanism
- combat spatial explanation
- viewpoint distance
- chapter-ending technique

## Forbidden transfer from old prose

- names, organizations, ranks, places, dates, and chronology
- injuries, investigations, moves, relationships, promises, and past events
- monster purpose, battle outcome, or weapon availability
- old information-disclosure order
- old military and intelligence subplot scale
- old characterization when a current source differs

Even a retained character name gives no authority to that character's old
rank, history, relationship, or knowledge.

## Known lexical warnings

Flag these unless independently present in a current source and required by the
chapter brief:

- 국방정보본부 제6국
- 미확인 위협 대응 조사단
- 서인태
- 김유찬
- 이도훈
- 윤혜린
- 민기준
- 강철원
- 이현수
- 단목항
- 황산지구

Flag `아이언 앵커` when the scene occurs before its current-canon
early-summer introduction.

Flag `블랙 타이탄` and `타이탄` for a knowledge-holder review. They are valid
in family dialogue, family-close narration, neutral author narration, and
author-facing metadata, but invalid in an outsider's dialogue, internal
monologue, report, or close-POV lexicon before an approved name reveal. Apply
[naming-knowledge-g0-approved.md](naming-knowledge-g0-approved.md).

The list is a warning aid, not a complete semantic firewall.

## Review questions

1. Can every story fact be cited to current canon, current state, or the chapter
   brief?
2. Did a style example introduce a person, place, relationship, injury,
   institution, weapon, or solution?
3. Did a retained name bring its old history with it?
4. Did an old battle determine the new enemy's tactics or outcome?
5. Did military pursuit expand beyond its current supporting role?
6. Did the final paragraph summarize a theme instead of landing on a concrete
   beat?
7. Is the generated scene explicitly approved before its delta is applied?
8. Does every use of `블랙 타이탄` or `타이탄` belong to a current internal-name
   holder or clearly neutral author narration?

Run `scripts/check_draft.py DRAFT_PATH` before this semantic review.

**해제 이력:** `박우석` — **G0-016(2026-08-19) 승인으로 복원.**
영진의 국과연 후배 · 비공식 조달선. 화계 = 영진 → 하게체.
봉인: 우석은 영진의 목적을 모른다 · 명준 축과 연결 금지 ·
국과연 시절 서사는 Gate B 고정선(과거 공개 금지) 유지.
