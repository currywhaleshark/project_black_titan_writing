# Project state

## Contents

- [Authority](#authority)
- [Current project workspace](#current-project-workspace)
- [Approval state](#approval-state)
- [Current serial state](#current-serial-state)
- [Active constraints](#active-constraints)
- [Bundled reference policy](#bundled-reference-policy)
- [Style corpus](#style-corpus)
- [Production process](#production-process)

## Authority

Write from current canon, not remembered canon.

Apply this order:

1. User correction in the current request
2. Project_Black_Titan_통합설정집_v2.3.docx
3. Project Black Titan 전체 플롯 v2.2.docx
4. Exact approved Gate 0, Level 3, and Level 4 project artifacts
5. Latest approved chapter text, delta, state snapshot, and foreshadow tracker
6. Current approved chapter brief and content lock
7. Bundled summaries in this skill
8. Old manuscripts and experiments as STYLE_ONLY

The handoff restores working position but does not override canon. Verify its
claims against the exact approved project files.

## Current project workspace

The maintained Google Drive workspace is:

https://drive.google.com/drive/folders/1_BOebogPCwQfYAR0ofS9_eHtPi03RMEf

Its main folders are:

## Workspace layout (reorganized 2026-08-21)

Top level was 120 entries; 104 of them were chapter folders burying everything
else, and four number collisions (02/21/90/99) made the planning folders hard
to find. Chapters now live under **`10_회차/`** and the planning folders are
renumbered without gaps:

```
00_핵심정사              canon (설정집 v2.3 + v2.4 증보, 전체 플롯 v2.2)
01_Gate0_설정변경         G0-001 ~ G0-019, 소급 정정
02_봄편_기획              spring Level 3
03_여름편_기획            summer Level 3 + S8~S12 outlines
04_가을편_기획            ★ autumn — L3 골격 · S13 개요 · 검토서 4종
05_문체_상태_인계          SNAP-NNN, 복선추적기, 인물등장장부, 아크캡슐
06_조연외형_시각자료
07_시각바이블
08_CODEX_이관             ★ skill canon (sync-skill.ps1 edits here only)
09_회차별_삽화
10_회차                   ★ all NN_EPxxx(_승인완료) folders
90_NONCANON_실험초고
99_묶음백업               ★ 폴더정리 이동목록 + 되돌리기 스크립트
tools / docs / game / tmp
```

`tools/build_mobile_review.py` now scans `EPROOT = ROOT/10_회차` (falls back to
ROOT if that folder is absent). Nothing else needed changing — `00_핵심정사`,
`05_문체_상태_인계` and `08_CODEX_이관` kept their names.

**Autumn planning previously had no Level 3 skeleton** (spring and summer both
do). It now exists at
`04_가을편_기획/Black_Titan_가을편_Level3_골격_v1.0.md`, consolidating what had
been scattered across the plot review, the setting-book cross-check, G0-019,
the cast reshuffle, the name list and the S13 outline. On conflict the order is
**G0-019 > 통합설정집 > that skeleton**.

- 00_핵심정사
- 01_Gate0_설정변경
- 02_봄편_GateB_승인
- 03_EP001_승인완료
- 04_EP002_승인완료
- 05_문체_상태_인계
- 06_조연외형_시각자료
- 07_EP003_승인완료
- 08_CODEX_이관
- 90_NONCANON_실험초고
- 99_묶음백업

Start a new session with 05_문체_상태_인계/Black_Titan_새세션_인계서_v1.8.md
(v1.7 and earlier are obsolete). The official current state is
Black_Titan_SNAP-067_EP067후_v1.0.yaml.

## Approval state

### Canon and upper planning

- Integrated setting v2.3: current canon
- Full plot v2.2: current canon
- Spring Level 3 monthly plot and seven sub-arcs v3.2: GATE_A_PASS
- G0-002 search-lineage and Titan cancellation: approved
- G0-003 internal proper-name knowledge asymmetry: approved
- G0-004 semi-direct motion, cover control, and bypass synchronization:
  approved and reflected in canon v2.3/v2.2
- G0-005 supporting-character appearance and visual standard: approved
- G0-006 EP1–2 VR first disclosure and sleep-learning correction: approved
- G0-007 underground sortie line and submerged-station launch: approved 2026-08-02
- G0-008 lobster retrieval unit appearance lock: approved 2026-08-02
- G0-009 eye-glow system (kaiju green / Black Titan orange / White Sentinel blue slit): approved 2026-08-02
- G0-010 field invisibility and audio design lock: approved 2026-08-02

- G0-011 kaiju corpse dissolution (old-canon restoration): approved 2026-08-03.
  A destroyed kaiju's binding field collapses; the body melts red on water
  contact, leaving nothing to salvage or analyze. Narrate the phenomenon only —
  the cause stays sealed with the field until autumn.

Canon docs v2.3/v2.2 do not yet contain G0-007 through G0-011. A v2.4 revision
is outstanding. Until it lands, read those requests in 01_Gate0_설정변경
alongside the bible. v2.4 must also fix a hanja typo: 역장 is 力場 (force
field), not 逆場 as v2.3 [650] currently prints.

### Spring Level 4

- S1 EP001–006 v3.7: GATE_B_PASS
- S2 EP007–012 v3.5: GATE_B_PASS
- S3 EP013–018 v3.3: GATE_B_PASS
- S4 EP019–024 v3.5: GATE_B_PASS
- S5 EP025–029 v3.1: GATE_B_PASS
- S6 EP030–035 v1.4: GATE_B_PASS
- S7 EP036–040 v1.3: GATE_B_PASS
- Spring daily-life reinforcement integrated review v1.0: approved

For current work, use the exact files in 02_봄편_GateB_승인. Some bundled
S1–S5 summaries predate the versions above and are fallback context only.

### Revised serial

- EP1 벚꽃과 사이렌 v1.0: GATE_D_PASS, delta and Gate E applied
- EP2 격납고 v1.0: GATE_D_PASS, delta and Gate E applied
- Official current snapshot: SNAP-002
- Latest canonical chapter: EP2
- EP3 v1.0 through EP36 v1.0: all GATE_D_PASS with delta and Gate E applied
  — S1~S6 arcs closed; **S7 in progress (1/5)**
- **Official current snapshot: SNAP-067** (Black_Titan_SNAP-067_EP067후_v1.0.yaml);
  foreshadow tracker SNAP-067; appearance ledger **v1.63**.
- **S8 「재검과 재래」 CLOSED at EP50** (10/10). Exit-ledger audit 8/8
  (one over-delivery: Sua's record work grew past the outline), arc
  capsules **S1–S9** written. **S9 「고철의 재간」 is CLOSED (11/11)** —
  see `05_문체_상태_인계/Black_Titan_아크캡슐_S9_v1.0.md` and the closing
  ledger in `66_EP061_승인완료/`.
  **The arc was compressed from 12 chapters to 11 by the user on 2026-08-14.**
  EP51–EP61 are GATE_D_PASS. **S10 「통증과 균열」 Level 4 outline is
  approved** — `02_여름편_기획/Black_Titan_S10_EP062-076_화별개요_v1.2_승인.md`
  (EP62–076). **EP62–EP67 are GATE_D_PASS** (6/15 of the arc); next is
  **EP68 「한 마리」** (7/13 Wed, key chapter, 톡토기형·학교 파손).
- **All 67 approved chapters pass check_voice and check_translationese**,
  including the narration-reference rule (`저 사람`/`그 노인` → `할아버지`).
- **★ FULL-SERIES CONTINUITY AUDIT ran 2026-08-16** — every approved chapter
  (EP1–EP67) was read against the guards, ledger, and calendar. Report:
  `05_문체_상태_인계/Black_Titan_전수감사_보고서_2026-08-16_v1.0.md`.
  **Three correction passes were applied in place**, each with its own record
  in `05_문체_상태_인계/`:
  - **1批** (mechanical) — elevator/stairs in 8 chapters (the G0-013 retrofit
    had missed EP4·9·13·28·33·34·43·58), four surviving 존댓말 lines
    (EP30·34·35·39), EP61's Thursday→Friday truck, EP61 `~해` to 기태,
    EP67's header date (7/12 was a Tuesday → **7/11**), calendar rows for
    EP62–67.
  - **2批** (narrative judgment) — EP30's two sentences (the EP34–35 stillness
    insight was pre-empted; `밀렸다`→**`당겨졌다`** so EP35's push/pull test
    has a real basis), **재호 → 장우진** in EP58·63 (문재호 is 3학년),
    unreleased pain vocabulary (EP53 `저렸다`, EP44 `아프고`), time drift
    (EP44·45·50·30·35), EP56's missing school handling, EP62's collapsed
    shop/hangar geography.
  - **3批** (state documents) — foreshadow trackers SNAP-062~067 had been
    **byte-identical copies of SNAP-061**; rebuilt from each chapter's Gate-E
    record (S10 threads 간격·몸살·호승심·군기록·여론·계통재파견·계획표 added,
    **A-S9 resolution registered**). Procurement inventory in SNAP-057~067
    still said the big-truck load was **미수령** when EP57 delivered it.
    Guard misattribution fixed: `무서운 게 정상이다` is **EP46**, not EP44.
  - **4항 정본 회의 CLOSED 2026-08-16 (user decisions)** —
    ① **narration reference follows the scene's viewpoint**: 단아/수아
    밀착 → `할아버지`, 영진 밀착·중립(군·정경) → `영진`. Spring (EP1–54)
    keeps its `영진` convention; **only clear violations inside a
    close-viewpoint scene get changed** (EP65 had two).
    ② `계단 한 칸` → **`한 단`** everywhere (EP63·65·66), and that one step
    is `내려서다`/`나가다`, never `내려가다`.
    ③ **`잘 했다` first lands at EP64** — EP64's own narration says it was
    `순서에 없는 말`, so the two spring instances (EP16·EP39) became
    **`수고했다`**.
    ④ Numbers split on **written vs counted**: records/instruments/numbers
    and quoted documents in Arabic (`13초 1`, `0.5초`, `7번`, the rota's
    `저녁 8시`); clock times and counted quantities in Hangul
    (`새벽 한 시`, `사 분을 셌어`). Seven narration clock times were
    converted (EP5·9·10·14×2·17·51).
  **Still open**: the MED residue in the report's C절 (EP21 arm tally,
  EP24 relay premise, EP54↔56 table timing, EP2↔3 hangar posture, EP41
  ledger date).
- **Fourth standing guard (user 2026-08-10): check the visual-bible LOC
  sheets before writing any scene in a mapped location.** Completed
  sheets (binding): LOC-01 cockpit, LOC-02 hangar, LOC-03 classroom,
  LOC-05 repair-shop-house. LOC-04 city master is UNFINISHED — not
  binding; approved prose wins there. LOC-05 essentials: single-story
  촌집 — no upstairs, no stair landing; living area ↔ shop through a
  sliding door (floor one step higher; the door-gap light rule); the
  ONLY staircase is behind the basement steel door; inner room has a
  low table, TV, floor cushions (no sofa).
- **Third standing style guard (user re-correction 2026-08-10, in 인계서
  §6): 수아 must never read prickly.** Snappy comebacks and tit-for-tat
  are 단아's register only — the moment 수아 banters she becomes a
  "little 단아". 수아 = one step back, others before herself, reserved;
  smart like her mother, thinks deep for her age, reads people's hearts.
  Praised → itchy, deflects the topic toward worrying about someone
  else. Thanks = quietly naming the other person's effort (`할아버지
  어제 늦게 잤어요?`). In disputes she doesn't contest — she records.
  Uses 요-체 to 영진 consistently.
- **S4 「포박」 (EP19–24) is CLOSED.** Ledger check passed 7/7 lines +
  13/13 states (Black_Titan_S4_종료장부_대조서_v1.0.md in
  29_EP024_승인완료); arc capsule at
  05_문체_상태_인계/Black_Titan_아크캡슐_S4_v1.0.md — S5 entry conditions
  live in its Next-arc section. Four user function-preserving corrections
  recorded (standing-up rescue physics, anchor-drop flip physics, the
  sneaky-movement taunt replacing `기록 조작`, taunt target = the EP17
  last-runner runoff).
- **Two retro passes applied in place to approved texts** (state docs
  unaffected): 2026-08-08 consistency fixes (EP1 military-failure beat with
  the user-locked field impression rule — hits land, zero damage, `바위를
  쏘는 것 같았다`; EP2 dialogue; EP4 route; EP6 tense; EP9 washer/count;
  EP12 giant count) and 2026-08-09 combat-tone pass over nine battle
  chapters (EP3·8·9·10·15·16·20·21·22; EP4 kept untouched as the reference
  chapter). Records: 05_문체_상태_인계/Black_Titan_소급정정_*.md
- **Two standing style guards (user-locked 2026-08-09, in 인계서 §6):**
  ① Dana must not read cool/veteran in combat — calm is *earned by
  counting*; 2-3 kid-cracks per chapter (dry mouth, trembling hands,
  childish self-talk like `침착하자, 도단아`, delayed emotional bills).
  ② Combat-cognition trichotomy: **단아 = learns by colliding bodily**
  (action before thought, bad at counting — counting mainly restrains the
  body; insights arrive body-first, head half a beat late), **수아 =
  draws with her head** (notebook, lists, deferral), **루시 = trained**
  (post-midpoint; hooks into her planned "mimics machines in combat"
  card). The three must never share one combat-prose rhythm.
- **S3 「영웅의 시간표」 (EP13–18) is CLOSED.** Ledger check passed 7/7
  lines + 8/8 states (Black_Titan_S3_종료장부_대조서_v1.0.md in
  23_EP018_승인완료); arc capsule at
  05_문체_상태_인계/Black_Titan_아크캡슐_S3_v1.0.md — S4 entry conditions
  live in its Next-arc section. Three user method-corrections recorded
  (wall-pin subdual, dawn-rain dissolution, wordless responsibility
  statement) — function-preserving, not retcons.
- **S2 「우리 동네 거인」 (EP7–12) is CLOSED.** Ledger check passed 8/8
  lines + 7/7 states (Black_Titan_S2_종료장부_대조서_v1.0.md in
  17_EP012_승인완료); arc capsule at
  05_문체_상태_인계/Black_Titan_아크캡슐_S2_v1.0.md — S3 entry conditions
  live in its Next-arc section.
- Narration style card is now v0.9: **§6-8 viewpoint-based address** —
  third person, but address terms follow the scene's viewpoint character
  (단아 scene: `기태 아저씨`/`선생님`; 영진 scene: `기태`/`배 선장`;
  military: rank forms; neutral/silent scenes: full names) — plus
  **§6-9 re-introduction reminder**: any character returning after a gap
  of one mini-arc (~6 eps) or more gets a one-beat reminder (role phrase
  or anchor), judged from the appearance ledger's last ● episode. **§7-6
  style-drift guard is ACTIVE from S3**: Level 6 must pull function-matched
  excerpts from the last 2–3 approved chapters as style baseline.
- **Backlog cleared 2026-08-04:** handoff v1.5 written (새세션 인계서 —
  v1.4 obsolete); EP1–5 line-break retrofit DONE (all 12 approved chapters
  now follow §6-7; 교열2 note in each header); bible supplement
  **00_핵심정사/Black_Titan_통합설정집_v2.4_증보_v1.0.md** consolidates
  G0-007~012 + errata (力場) + world facts — canon = v2.3 docx + this
  supplement (docx v2.4 proper remains optional).
- **Class size fixed (user, 2026-08-04): Dana's class has 26 students.**
  All classroom counts (eyes, papers, seats) must derive from 26.
- **Mobile review artifact — republish at every Gate E.** The user reads
  and annotates approved chapters on their phone at
  https://claude.ai/code/artifact/a8be889d-2461-4e8b-804e-b4be0532cd68
  (works with the PC off; annotations live in that phone's localStorage).
  After any chapter is approved or edited, run
  `python tools/build_mobile_review.py` (auto-scans `NN_EPxxx_승인완료`)
  and publish `tools/black_titan_review.html` with **`url:` set to that
  same artifact URL** — omitting the url mints a new address and breaks
  the user's home-screen shortcut. Edit `tools/review_mobile_template.html`
  for UI changes, then rebuild. Exported JSON matches the desktop
  `_첨삭메모.json` schema (`changed`/`comments`/`n`), so apply it the
  same way.
- **World guard (user-confirmed at EP11): the internet is LOST — only the
  Cheonghae intranet (청해 내부망) operates. Never write `인터넷` in prose
  or dialogue.** Also confirmed: 청해남초 lunches are cafeteria-style
  (급식실), not classroom service; separate soup bowls are rare.
- G0-012 urchin-type appearance lock approved (hemispherical black body 40m
  exposed, spines up to 30m, barnacle texture, green point-lights in the
  hollows between spine roots, silent, immobile).
- **S1 「첫 침공」 (EP1–6) is CLOSED.** Ledger check passed 7/7 lines + 6/6
  sub-arc states (Black_Titan_S1_종료장부_대조서_v1.0.md in
  11_EP006_승인완료); arc capsule at
  05_문체_상태_인계/Black_Titan_아크캡슐_S1_v1.0.md.
- Approved-episode folders: 07_EP003_승인완료 / 09_EP004_승인완료 /
  10_EP005_승인완료 / 11_EP006_승인완료. Drafts live in each folder's
  _superseded — never reuse.
- Narration style card is now v0.8 (adds §6-6 character first-exposure rule
  and §6-7 dialogue/narration line-separation rule — both from EP6 review,
  2026-08-03; line separation applies from EP6 onward, EP1–5 retrofit is an
  open decision).
- Character appearance ledger exists:
  05_문체_상태_인계/Black_Titan_인물등장장부_v1.0_EP006초고기준.md —
  update it at every Gate E. Known facts: 김주호 is the homeroom teacher
  (EP1 text); 윤서진 first appears EP5; 강한결 confirmed 반장 in EP6 but has
  never appeared on-page (mention only).

EP5 locked in: the flashback cold open (18 years ago, the estranged Hyunseo
arriving half-mad — "우리도, 우리 괴물을 만들어야 해요") turned out to be
Young-jin's explanation, relayed via Dana echoing "우리 괴물." The cover story
was reconciled: prototype stolen solo by Young-jin ~30y ago, then retrofitted
(개수) together by father and daughter from 18y ago. Disclosure ceiling:
"도영진·도현서 부녀가 블랙 타이탄을 준비했다" — why she left / where she is /
the father / why Dana all stay closed questions. Hyunseo exists on-page only in
flashback; 윤서진 대위 debuted per her G0-005 card. FS-001 baseline set (the
post-battle fatigue was accepted as normal).

EP6 「교실의 거인」 locked in: the classroom hero-myth comedy (나래's wrong
throw-comic, Dana's one mechanics fix hidden behind athletic fame, 성호
worship + 도릴라 juxtaposition), the family rule made explicit over dinner
(기체 압수·영진 체포·양육 이관 → "셋이 같이 못 산다"), and the hook
`너, 진짜 어디 아픈 거 아니지?` — Hyejeong spent her one direct question
(no repeat within spring). New facts: 강한결 = 반장 (mention only, never yet
on-page); 장우진·최나래 first on-page; 예진's awareness of Hyejeong's short
replies is deliberately uncertified (recoverable either way in summer).

EP7 「물이 잘린 아침」 locked in (S2 opener, 12_EP007_승인완료): harbor-zone
anomaly shown as daily-life chain only (cut nets with clean edges, pushed
boats, static sonar, cultured-meat school lunches); 박기태·오미란·배정호
first on-page; hook = radio rumor of a spiny black rock that never sinks.
New user-confirmed facts: 영진's neighborhood title is **도 박사**; cultured
meat (배양육) is the everyday protein of this near future; 기태 already
knows the family via repair-shop visits (mutual acquaintance — his supply
deal with 영진 still starts at EP12). 동진호's fish-finder sits in the
repair shop, tested fine — silent proof the water itself is wrong.

EP8 「방파제의 가시」 locked in (13_EP008_승인완료): urchin-type visually
confirmed via command-room zoom (G0-012 on-page), harbor closure official,
naval shells pushed off-target (phenomenon only — no field vocabulary),
military gathered seabed charts + tide tables (EP10 seed), school chatter
reignited ("검은 거인은 언제 나오는데?"), and 영진 fixed the plan:
"이건 싸움이 아니다. 철거다." Sortie set for the weekend spring low tide
(circled twice on the fisherman's calendar, D-3). Dana's third resolve is
practical, not desperate — she stood up without a speech.

EP9 「철거 작업」 locked in (14_EP009_승인완료): the frontal pull failed
correctly — Dana's grip slid off the body (cause unnamed), pulling sent
vibration back up her arms from the breakwater, and she let go to save the
harbor. Dock cracks confirmed only afterward via a news brief ("저 금,
내가 만든 거다"). **FS-003-BIO-SEEP planted**: 영진's midnight solo
maintenance reads as his meticulous prep-for-tomorrow routine (parts
inventory count = EP12 procurement seed); the re-darkening armor seam is
narrated as "덜 닦인 모양" — no source-implying vocabulary, the burned rag
is the only lingering tell. Spine fragment stored under a shelf (prop).
Left hand did first grip and last release, unremarked — the drone footage
of it is EP10's 왼손잡이설 source.

EP10 「간조」 locked in (15_EP010_승인완료, S2 climax): the piggyback win —
the military's desperation-born seabed-collapse op ("기다리는 게 계획일
수는 없잖나") could only tilt the urchin (it re-anchored every time; "저
문은 몇 초짜리다"), so Dana rolled it through the tilt window, drum-barrel
rhythm, breakwater untouched, and it tumbled down the old sluice valley —
removed, not killed ("치웠다, 가 맞는 말이었다"). Harbor reopened. **`우리
동네 거인` was born on 미란's hand-painted sign**; the military filed
"현재로서는 적대할 이유가 없다" (서진's wording); hook landed with 성호's
first-ever correct analysis: "손이 언제나 왼쪽부터 나간다" (user changed
주먹→손). 영진 calls 정호 "배 선장". Urchin never returns (author-side:
displaced = function lost; death unconfirmed; EP12 logs 시도 02 실패).

EP11 「오른손의 급식」 locked in (16_EP011_승인완료): Dana's two-day
right-hand operation failed everywhere it could (worm-writing, dropped
명태전, dodgeball ball caught by 성호 followed by an instant counter-hit —
user fixed the rule: caught balls aren't outs), she chose to lose rather
than expose the left hand, and a reflexive left-hand tray catch voided it
all — "내일부터는 그냥 왼손으로 살기로 했다." B1 advanced hard: 혜정
misreads it as a hidden hand injury, helps by doing (two copies of notes,
scissors, band-aid tin), spends direct question #2 ("너 손, 진짜 안 다친
거지?" — deliberate echo of EP6's hook), and resolves to WATCH: "안 나으면
그때는 묻는다. 그때는 밥 두 그릇으로도 못 넘어간다" (summer shadow).
Both direct questions are now spent for spring. 성호's phantom profile
grew (32, three deployments, 185cm from "cockpit size").

EP12 「기록되는 것들」 locked in (17_EP012_승인완료, S2 closer): four
records of the same March — Dana's essay `우리 동네 거인` (erasing and
rewriting the subject; "사실만 골라 쓴 글"), the parts ledger becoming
기태's first covert order ("기태야" snapping him to attention; his only
question "언제까지요"; "삼십 년 만에 처음, 이 일에 바깥 손이 하나
들어왔다"), the 남방사 settlement (서진 distilling grumbles; the shared
old photo of young 고명준 + young 도영진 surfacing while he fetches ink —
seen, not sought; "인주 갑을 든 채로, 사진을 잠깐 보았다"), and the
subjectless deep-sea log ("시도 02: 실패") ending on eight legs unfolding.
**FS-003 and C3 are twin ACTIVE_BURIED plants sharing the mute-scene
grammar.** 수아's soft-reproach line was user-tuned ("말했는데, 언니가 못
들었나 봐").

EP13 「사월의 시간표」 locked in (18_EP013_승인완료, S3 opener): the April
timetable becomes a structure — 학교 / 수리점 / 훈련 three cells Dana writes
into a notebook, the third labelled `집안일` (the lie she told Hye-jeong,
now filed as a document); a fourth burden (`부품 가는 날`) added when 기태's
first shipment arrives as three piles — usable / needs grinding (largest) /
scrap. **B1 flipped from question to labour**: `집안일` gets `어.` and
nothing else; Hye-jeong bundles Dana's supplies twice that week, second bag
carrying an unexplained circle. **B3 placed 수아's own world** — Friday
violin after-school with 이하랑 (different class, user-confirmed; contact is
the class only; 3rd grade ends an hour earlier, which is why she enrolled —
Young-jin's call, her instrument pick), plus one long unwitnessed look into
the open cockpit. Hook: classroom light + research-complex tower beacon
blinking three times at the same interval over the held last note (Sua POV).
User-fixed facts: **year = 2050** (author-side; never printed) → 체육대회 =
April 27 Wednesday. Training stayed inside the submerged station — no
open-water sortie, no military record. C1 fully silent. §7-6 first run
passed.

EP14 「정전 파도」 locked in (19_EP014_승인완료, S3 pressure): the
multi-legged creature crossed the flood barrier and seized the
heat-exchange tower — on-page military name **`다각 보행체`** (`거미게형`
stays author-side); leg-angle changes scramble sensors and the safety
system sheds power/cooling blocks → **rolling-outage regime** (발전소 무손상,
`없음 세 개` elimination). **C1's first deniable signal since EP1**: one
corridor beat — focus lagging half a step + a brief temple prick as lights
return; self-read as outage jitters, forgotten, no witness, no recurrence,
strictly scene-separated from the creature. B2: 고명준 chose evacuation /
grid isolation / drop-zone control, held fire (tower collapse risk), and
broadcast structural-load warnings on the open emergency band — "잡히라고
트는 거다. 듣는 쪽이 있으면 좋겠군" (kept out of the record). 영진's ceiling
guess: `전기를 먹는 게 아니다. 높은 데서 뭘 찾는 거다.` + `그건 모른다`;
user-added beat — Dana registers that `모른다` has become a frequent word
this past month (new texture on the C2 strain). Life: rehearsals cut
30→15 min (Dana finally stays to the end), 수아's after-school suspended,
repair-shop outage rush, hand-copied rotation chart (`냉장고 문 열지 말
것`). Hook: at midnight the silhouette re-angles its legs toward 구래동 —
and the hangar lights come on.

EP15 「수직의 싸움」 locked in (20_EP015_승인완료, S3 first failure,
important chapter): the correct failure landed in three ordered causes —
avoidance climbs (twice, then a grab: the leg wouldn't move but the tower's
support bolts sang first, 방파제 déjà vu one sentence), a walking leg's
shove (path-clearing, not attack; user added the beat "어어……?"), and the
grabbed tower tilting from the Titan's own weight. **Dana abandoned pursuit
in one standalone sentence and braced the tower from the ground** (user
edit: 내려와 땅을 딛고 서서) — interior handled as counting (load 40%,
blocks left, damped burden, time), the submerged-station training paying
off (`나가지 않는 날의 훈련이, 나온 날을 받치고 있었다`). Pattern fact
went on page exactly once: `가까이 가면 버리고, 더 높은 데로 간다` — no
reason given. **수아's first observation completed**: soundless monitor,
distance-scale guess, fold-order noted (outer legs first), three timestamps
(0:47/0:58/1:11) written in her *violin notebook* under the lesson-supply
list, zero speech, and the deliberately preserved gap — `달아나는 것도
싸우는 것도 아니면 무엇인지, 그 낱말을 아직 갖고 있지 않았다`. Military
side: two-line record, new filing category **`방어 협조 관측`**, drop zones
kept empty; EP14's open-band broadcast paid off (Dana memorised 40%/300m
and used them — neither side names it cooperation). Hook: with shutdown
complete, the creature spread all eight legs at once toward the city and
the last live block's alarm sounded. C1 stayed fully silent through combat;
FS-004 phrasing untouched at the fall.

EP16 「오를 곳을 없애는 법」 locked in (21_EP016_승인완료, S3 climax): the
herding win — replayed cockpit footage (the **flight recorder is new
canon**: Young-jin's maintenance feature, user addition) confirmed only the
fact of avoidance; Dana matched it to **dodgeball muscle memory** (user
addition — passing with defenders to erase escape lanes: `코트가 연구단지,
공 대신 거인일 뿐`), then closed search lanes by approach radius
(넷→셋→둘→하나 in hangul rhythm) until the creature perched on the
de-powered maintenance tower — its fourth leg groping air and finding
nothing. She toppled the tower into the empty basin (braced, angle-lowered
like weekend part-grinding; stepped back before the point of no return —
no co-fall), then on flat ground **pinned the body against the basin wall**
(user physics correction replacing the outline's roll-over: legs fold
between wall and body, the wall tilts it belly-out — terrain used three
ways: tower, floor, wall), pressed the soft plate under the belly, and the
green points went out in reverse order. At dawn, spring rain hit the
carcass and it melted red into the drain (user decision — kills the
salvage thread; G0-011 phenomenon-only; the military logged its third
`수거물 없음`). The military knowingly kept the broadcast running (`방송
끊지 마라. 저쪽이 쓰고 있다`) — cooperation never named. Day fixed:
battle night was Friday→**Saturday** (so EP14's school day = Friday).
Victory cost on page: auxiliary blocks damaged, days of rolling outages,
and the rotation chart read out over the open band with 청해남초등학교 and
구래동 in it. C1 stayed silent through combat (rest lock held).

EP17 「불 꺼진 교실」 locked in (22_EP017_승인완료, S3 aftermath): the
victory bill paid in daily-life currency — chalk lessons and popular
outdoor classes, lukewarm milk, Yejin's curry prophecy landing (`우연이
두 번이면 법칙`), the rumor market (braced it / threw it / drowned it —
Dana corrects nothing: `제일 안전한 자리는 틀린 소문 옆`). **B1 turned:
Hye-jeong is Dana's April deskmate (user addition — monthly seat lottery,
consistent with EP11's nameless partner and EP12 Sua's swap); in the dark
classroom she slides her notes over and says one line (`병원 가 봐. 안경
바꿀 때 된 거 아니야?`) and Dana — for the first time — accepts:
`……고마워.`** B4's inversion beat: 성호's first-ever straight-line logic
defending the giant (the class goes quiet; he sits down early and adds
`거인 욕은 우리 반에서는 금지`) while Dana holds a double silence — both
sides of the gratitude/complaint pair are right, and her hand is in the
tower damage (`각주가 있는 사람은 본문에 밑줄을 긋기 어렵다`). Relay paid
off: Dana wins the runoff (성호's taunt kept playful per user tone-lock —
`가을 운동회 때 정식으로`, then volunteers as third runner with the
thickest arrow on his own leg). B3: powerless violin (`전기 안 쓰니까`),
memorised passages, timestamps recopied to a fresh page (`답이 없는
숫자는 답이 생길 때까지 두면 됐다`). Power back Wednesday afternoon; hook
= the lit e-board doesn't retire the glasses-push gesture, and 김주호 lays
the vision-test notice with his fixed phrasing **`집에 갖다 드려라`**
(user correction — he knows the household; the wording stays uniform for
everyone).

EP18 「도수」 locked in (23_EP018_승인완료, S3 closer, approved without
annotation — user: `이번에 좋다`): the clinic day — honest-but-safe
verdict (worsened myopia/accommodation; explainable by growth + fatigue +
old prescription; no lesion; recheck in June), **same round frames with
new lenses** (the city that repairs things), the guardian box reading 조부,
the truthful pen. Dana's VR joke met Young-jin's **wordless apology** —
`……보정 시험이 무리를 줬을 수 있다. 내 계산이 짧았다.` — two sentences
inside his own cover story (the voice-card ban on `미안하다` held); Dana
answered `다음엔 계산 길게 해` and their strides matched uninvited. B1
closed its grammar (`이제 칠판 보여?` → `그럼 됐어` → prep sheet — the
measured boundary line both now stand easy on). The notebook got its
fourth entry (`안과 재검. 6월.`) and the arc's three lessons: timetables
grow even when kept; winning leaves chores; cells appear unasked. Hook:
a larger sac, jointless arms flowing with a black model, wrapping waist
and limbs in one motion — and holding still. Dates fixed: clinic Sat
4/23, new lenses Mon 4/25, sports day Wed 4/27 (D-2), recheck June.

EP19 「운동장의 선」 locked in (24_EP019_승인완료, S4 opener): the sports
day held and cut — a whole day with **zero clock-times on the page**
(EP13's inversion; `방학 같던 하루`). Rivalry fully restored through a
three-combination day (same team in dodgeball → different squads in the
obstacle race → same class for the relay): the finger-count out-tally
war, the ricochet-ownership dispute, and **강한결's first on-page
appearance** (13 chapters after his EP6 mention) — the class president
who ends arguments with ten steps and one word (`동점.`), on a tally
sheet deliberately written so it can't be recounted. **Mirrored caring
loaded** (the S4 guilt keystone): 성호 claims the crawl-net section
before a nervous squadmate can speak (`그물 내 거` — then crawls loudest
and laughs muddiest), 단아 runs two legs for an injured runner in the
half-beat before anyone volunteers; each sees only the other's kindness
and picks a fight over it (`그건 작전이고 내 건 관종이고?` / `어.
정확해.`). 우진 reappeared (gap-11 reminder honored) yelling `둘이
사귀냐` — answered by a simultaneous `안 사귀거든!`. Two user
corrections: dodgeball is intra-class so the duel became an out-count
war; the relay heats became an **obstacle race** (mixed-grade squads,
section-picking). Hook: instead of the starting gun, the coastal
evacuation siren — and the drainage channel flowing the wrong way,
toward the school. The relay showdown is now three-times deferred
(동점 → siren → EP24's `깁스 풀리면 다시 붙자`).

EP20 「여덟 개의 팔」 locked in (25_EP020_승인완료, S4 stage 2, important
chapter): the binding begins. Evacuation by grade lines — 김주호's
hands-on relay of small kids (`손이 먼저 가는 인솔`), 성호 copying him
into the tail without ever naming what he's doing (`생각했으면 아마 안
했을 것이다`); Dana slips away on the adjusted excuse `수아네 줄에 가
볼게. 할아버지랑 만나기로 했어` and **혜정 covers the roll-call gap**
(user annotation — `선생님께는 내가 말씀드릴게`; one more debt on the
misread ledger). First exposure: the creature comes **without breaking
anything** — stepping-and-gripping locomotion through the flooded blocks,
heading Gurae-dong way (user annotation) — until Black Titan appears and
all eight arms pivot at once (`저건 도시를 보러 온 게 아니다`). Binding
grammar established on page: four arms on body (head camera / elbow /
knee / waist), four traction arms suction-anchored (seawall,
flood-barrier, steel frame, farther), covered cameras never return, a
freed arm re-wraps somewhere worse, and **body-four and ground-four are
one body — pulling here tightens there** (`이쪽을 당기면 저쪽이
당겨졌다`), the injury bridge. The wrong-answer conviction is planted
for EP21: `팔은 여덟. 몸에 넷, 땅에 넷. 힘으로 하나씩 풀면 된다.`
Military: 상황실 재등장 with rank anchors honored, civilian evacuation
running (user annotation — hillside shelters past half, Gurae-dong
cleared first as it sat on the approach line), record name **`다완
흡착체`** entered by 윤서진, zero engagement orders (`대응할 수단이
생기면 그때 물어라`). The stair scene runs in 성호's POV: `괜찮아. 쟤 진
적 없어`, the seawall shock through the wet steps, the kid pushed inside
the rail, the misstep, `억.` one syllable — sprain not fracture (`일어
서지는 것과 디뎌지는 것은 다른 문제`), 혜정's bag-to-front two-hands
habit, 주호's `업힌다. 잡아라.`, and no resentment — what he sees below
is `이기는 모습도, 지는 모습도 아닌 — 그냥 버티는 모습`. Asymmetric
witnessing locked: Dana passed 성호's last visible moment thinking
nothing; she cannot know about the ankle (S4 school scenes are 성호-POV;
her view was covering over). Hook: the last screen fragment's strange
clarity, then full blackout — `켜지 않은 어둠` vs `덮인 어둠` — counting
what remains (knees, waist, soles, 영진's voice) while being hauled:
`바다 쪽이었다. 그것만은 발바닥이 알려 주고 있었다.` Three user
annotations applied (roll-call cover / heading report / civilian
evacuation); FS-004 watch passed (zero 관통·꿰뚫), C1 blindness kept
purely physical.

EP21 「붙잡힌 거인」 locked in (26_EP021_승인완료, S4 stage 3, important
chapter, approved without annotation — user: `좋네 바로 가도 되겠다`):
spring's first near-loss, written as arithmetic going wrong rather than
defeat narration. The wrong answer executes with full rationality
(`두 달치 이력이 전부 한 방향` — `다른 가능성은 셈에 넣지 않았다`):
unwinding frees the left arm once (`당기지 않았다. 벗겼다.`), then the
freed arm re-wraps elbow-and-neck before the fist lands — reconstructed
blind (`무게의 모양이 감김이었다`). The speed-loop fails (`멈추면 지는
것이고, 도는 동안은 아직 하는 중이었으니까`); split traction defeats
bracing (`합치면 바다였지만, 따로따로는 바다가 아니었다`); passing the
flood-barrier is felt as lost load behind the back (`두 달 동안 이 벽은
등 뒤에 두는 것이었다`), and the tally lands dry: `주먹을 낸 횟수를
셌다. 영.` The all-cockpit scenes run with ZERO visual narration —
senses and instruments only. 수아's first live-sortie presence in the
maintenance room stays inside the B3 cap: black squares vs broadcast,
spare-power handle checked three times by eye, sealant, three towels
(`돌아오면, 이 아니라 돌아올 때`), remembering — not writing down —
영진's capped half-line `부수려는 놈이 아니야. ……모르겠다. 뭐가
다른지.` Military: `수상 진입 가능 장비 없음. 수중은 더 없습니다` →
`보고만 계속해`; the flooded-district map frozen five years ago is now
canon. Underwater the creature's grip-swapping has an asymmetric sound
(attach silent, release delayed through water) — planted as EP22's
discovery material, unread by Dana. Final resistance answered only by
the neck arm re-settling; Dana reaches the question (`내 힘은 어디에
쓰이고 있는 것인가`) but NOT the answer — `다른 방향` stays sealed for
EP22. Hook: the artificial-horizon's ground line sinks and doesn't
return; depth climbs one notch at a time. New canon: independent cockpit
instruments (power gauge, pressure needle, horizon+depth), maintenance-
room battle station under 수아's care.

EP22 「끌리는 쪽」 locked in (27_EP022_승인완료, S4 stage 4, important
chapter): the arithmetic swap and the two returns. The gap discovered as
a by-product of counting (`세다가, 걸렸다` — release sounds mean release
moments; the four tensions are always three-and-one), confirmed three
times solo. The commitment beat: half-relaxing fails (the body refills
it), so `어중간한 용기보다 큰 용기가 쉬운 날` + a dodgeball half-cut
(walking toward the ball is less scary). **User physics addition: a
launch needs footing** — mud `버티기에는 못 쓰고 떠나기에는 쓸 수 있는
바닥`, so the trigger is double (`소리. / 발바닥에, 바닥. / 지금.`).
The charge INTO the pull meets no resistance (`세상에서 제일 가벼운
것이 된 느낌`), wraps slacken, she rams the body — and **stands up**
(user-locked physics: not buoyancy; the towing posture breaks, feet find
bottom, `52미터보다 깊지는 않았다 / 키로 이긴 것이다`), resolving
EP21's tilt-vs-water-sound contradiction (`서고 나서야 읽히는 답`).
Survival not victory: legs/waist still wrapped, mud won't hold a brace.
Screens return irregularly; the feed shows the B2 empty-zone list
(`비어 있는 곳들의 목록` — zero orders) and then **`청해남초 대피 중
학생 1명 이송`** — read three times, answered only with `겹쳤다` (the
next thought deliberately left out of the count), `이송이면 병원이다`
three-sentence stepping. 영진 sees the same line and takes his hand off
the transmit switch (`읽은 아이에게 얹을 말이, 살아온 세월을 다 뒤져도
없었다`). Hook: `단아야. 기울기.` goes unanswered while she reads the
line a third time — and the arm wraps her waist again, `기다렸던
것처럼, 정확하게`. User annotations: `두 화면` (an author-unit leak)
purged in 11 places; four line edits (incl. 쉰두 미터→52미터, adjusted
from user's `52m` to match canon orthography, reported). New canon:
three-and-one traction structure, pier cluster = the stripped elevated
road from before the flooding, mud footing physics.

EP23 「끌려가지 않는 법」 locked in (28_EP023_승인완료, S4 stage 5,
important chapter): the title is the answer — 끌려가지 않는 법 = 끌리는
길을 고르는 것. She KEEPS the shallow binding (`줄은 양쪽 끝을 가진
물건`), lures by heading alone through the pier forest (`잡는 것은
저쪽의 습관이고, 어디를 잡게 되는지만 이쪽이 정했다`; the trap `상대가
성실해야 짜이는 물건` — she must let it grab, `침착하자, 도단아`), the
lines cross (`당기는 힘이 당기는 힘을 잡고 있었다`), and the
user-corrected anchor-drop physics resolves the flip: once the bases are
hugged, the creature ITSELF releases the pier arms to re-grab her — its
grabbing habit both wove the net and pulled its own anchors — leaving
the body attached to nothing for the half-beat in which she flips it
onto the dry slope. Green dots die outward from her palm; `멎었다.`
Tone-guard layers ran first time as standard: 오기-not-plan framing,
`몸이 먼저, 머리가 반 박자 뒤`, delayed bills (`무서움. 피로. 약
오름.`), a smaller-than-expected voice on `멎었어`. Inference reached
(shared: 영진 `죽이려는 동작이, 처음부터 끝까지 한 번도 없었다` → Dana
`싸우러 온 게 아니야. 나를 끌고 가려던 거야.`) — why/where stay open
questions; C4 now SIMMERING until S6. First question after victory is
the injured kid; 영진 can't answer (`무엇을 대신 말했는지는, 단아도
아직 몰랐다`); the school notice lands at night: `이성호 학생 보호자
인계 완료.` — she reads it once, reads the name once more, cut. New
canon: line-crossing tactic (habit-dependent), anchor-drop behavior,
central locomotive organ, school group-notice channel. The carcass sits
on the slope (dawn-rain dissolution stays off-page; military's fourth
`수거물 없음` is EP24 background).

EP24 「깁스」 locked in (29_EP024_승인완료, S4 closer, approved without
annotation): the cost comes back to the classroom. Monday 5/2 return —
compressed interim (the loud kid's empty desk lowering the room's
volume a notch; rumor inflation of the fourth victory; radio's fourth
`수거물 없음`; the weight that gained a direction once the name
appeared). Crutch-sound entrance and stage-creature welcome (a wobbling
crutch demo halving its own credibility); the was-it-the-giant question
answered with the defense he's given for two months and then, in a
half-beat that isn't his lecture voice, **`그래도 우리를 지켰다`** —
Dana's inverted practice: hiding that the swagger DIDN'T rise. 주호
widens the aisle; 한결 finishes it without a single word — almost. The
heart beat: the one bag his sweep missed, moved by her foot (`미안하다는
말은 어디다 넣는 걸까. 넣을 자리가 없어서, 발끝에 넣었다`), the
perfect crime failing because a kid on crutches watches from his seat;
the corrected taunt (three elements of sneakiness + retroactive
suspicion of the EP17 last-runner runoff, `통계적으로`, his own past
coolness flipped shamelessly) — and indignation outrunning guilt
(`뭔가 한 건 네 다리가 느렸던 거고!`), the aftertaste doubled by the
fact that the race was honest and the sneaking was real. Rivalry rhythm
restored = the room's volume moving back up a floor, her voice loudest
in the move. B1 lands (paleness noted, questions skipped, both names
kept on the re-scheduled sheet — `적혀 있지 않다는 것이 곧 대답`); C1
rests in living language (chalkboard legible, the healthiest body in
the room); the hero-view turn completes in her own counting idiom
(`셈이 맞았는데 답이 이상하면, 셈에서 빠진 항이 있는 것` → `누가 안
다쳤는지 끝까지 세는 것까지가 싸움`) plus a private first line for the
new timetable (evacuation stairs before the fight). Hook delivered
verbatim and cut on her comeback. **S4 CLOSED** — ledger 7/7+13/13,
capsule filed, relay rematch now four-times deferred, new unpaid prop:
the cast's first inscription line.

EP25 「어린이날」 locked in (30_EP025_승인완료, S5 opener, standard):
the no-monster guarding chapter. First heat, the wave of failing old
coolers, the promise folded to `정오까지만` (elderly and small diners
first). The trichotomy staged in daily life — Dana body-first (knows
which end is heavy after lifting it; a yogurt held in her teeth), 수아
head-first (a table that reads like a map; catching the duplicate
order and the missing contact), one crossing where weight-counting and
table-drawing reach the same house (`언니는 도착하면 소리 내어
자랑했고, 동생은 도착한 것을 표에 적었다`). **B3's first recognition
delivered:** `가져오지 말고. 네가 봐라.` — the invisible stair between
making and confirming; the sheet goes into her own pocket. The alarm
silence lands as unfamiliarity only (`기다릴 것이 없어진 자리는
허전했다`). Flood-barrier shade lunch (kimbap-end competition), the
hand-built phones refitted between other people's fridges — orange
case for Dana, sky-blue for 수아, hand-worked corners; Dana's teasing
(`투박해`) and 수아's thanks-by-reading-effort (`이거 손으로 다듬으
려면 오래 걸렸겠다. 할아버지 어제 늦게 잤어요?` — this beat replaced
a prickly tit-for-tat after the user's re-correction; the 수아 tone
guard was instituted from this chapter). Dana's day-count: `아무것도
쓰러뜨리지 않았는데 뭔가를 지킨 날.` Hook delivered verbatim; she
starts typing a reply (content unshown — EP26's opening). New canon:
phone cases/serials, 구래동 living geography (대성슈퍼, 방앗간 noose
knot, third-floor grandmother), shutter-side tomorrow-list custom.

EP26 「늦는다는 말」 locked in (31_EP026_승인완료, S5 stage 2,
standard; date structure user-confirmed: Fri 5/6 discretionary holiday
+ Mon 5/9 school): the chapter of sentences. The habitual
`갑자기 일이 생겼다` typed in two seconds, then — `보내면, 받는
쪽에서 무엇이 시작되는지는 생각해 본 적이 없었다` — erased letter by
letter and replaced with `가게 짐 받고 있어. 20분 늦어.` (disclosure
capped at `가게 짐`), answered by a two-character `ㅇㅋ` (`무게는
이쪽에만 있었던 모양이다`). The rule lands dry-warm: three skewers
still hot (re-bought to arrival time), `이십 분 맞네. 시간 잘
지켰어`, and `못 오는 것보다, 아무 말 없이 기다리게 하는 게 싫은
거야` → `오래 갈 규칙은 싱겁게 생기는 법`. 기태 returned via the
other-session annotations as a KNOWN face (repair-shop regular the
sisters used to hide from — not the EP7-flashback framing), bellowing
them out of the crane radius to exactly two steps outside the danger
line, snapping straight at 영진's `기태야`, calling him **`박사님`**
(the EP12-established address; the town's `도박사님` nickname family —
NOT new canon), picking the shaded waiting spot; 영진's verdict:
`항구에서 제일 시끄럽고 제일 사고 안 나는 자리가 저 녀석 자리다.`
B4 fully baseline (wind-correction and curry-correction sophistry, the
sheet snatched back, `깁스만 풀리면 전부 다시 잰다`, statistics
sourced from his own head). Hook delivered: first blank `할아버지` in
half a beat; the second blank stops the pencil — `쓴 적이 없어서 지울
것도 없는 칸` (no mother-word on page). User micro-fixes: `7번 상자`
(label digits), `꼭 갈게` (three-character count fix). New canon:
contact rule, 기태-sisters acquaintance, quiet Parents-Day custom
(grilled mackerel), 혜정's grown-up shopping basket.

EP27 「빈자리」 locked in (32_EP027_승인완료, S5 stage 3, important
chapter; user corrections: SAME-DAY Mon 5/9 continuation from EP26's
stopped pencil — no two-day worksheet — and LOC-05 spatial compliance,
which instituted the location guard): the absence-activation chapter,
no new truth or evidence. Three hands carry it. The pencil: at home
(worksheet was take-home), she writes `왜 맨날 최악부터 생각하느냐`,
finds it comfortable (`진짜 질문은 쓰고 나서 편해지지 않는다`), knows
the answer already (`최악을 겪어 본 사람이 최악부터 생각한다`), and —
with 수아's folding sounds carrying `엄마 것도 있어야 하는 것 같아서`
through the wall — the eraser moves first: **`왜 우리를 혼자
키웠느냐`**, `동생의 두 번째 꽃이 꺼내 준 문장`. The scissors: two
carnations, nail-pressed folds, `국에 간을 맞추는 것처럼` matter-of-
fact. The empty hand: asked person-first by 수아 (voice practiced to
sound ordinary) and point-blank by Dana (`십삼 년 만에 처음 입 밖에
낸 질문`), 영진 half-turns toward his room — the longest half-beat
this house has seen — comes back empty-handed, grips the table edge:
**`……내가 대신 끝내 줄 이야기는 아니다.`** (`끝내 줄 이야기가
아니라는 말은, 뒤집으면 끝나지 않은 이야기라는 말`). The kids don't
push; 수아 pulls the two flowers half a span closer. Warm dinner
(crumpled carnation worn all through it, the worst-first arithmetic
gag `그러니까 다행인 거다`), and the void gets named: `……우리 상이
원래 이렇게 넓었나` — the fourth seat (`이름이 생긴 빈자리는 그냥 빈
것과는 달랐다`). Hook: floorboard-quiet night, the crumpled flower
still on his chest, and through the sliding-door gap, on the shop
windowsill, the unaddressed second carnation facing the street —
`꽃은 치워지지 않았다. 다음 날 아침에도, 그 자리에 있었다.` New
canon: EP26–27 one day (5/9), LOC-05 compliance set (floorboards,
sliding-door light rule reversed at night), two carnations as standing
props, the worst-first proverb.

EP28 「확인자」 locked in (33_EP028_승인완료, S5 stage 4, important
chapter; 20 user annotations applied in v0.2, then approved): the
series' FIRST full 수아-attached POV chapter (brief §6 adopted
수아-attachment with the rows-and-boxes eye — she scans whether the
world is in order before she looks for people; narration keeps her
half-step-behind grammar throughout). School: the 일인일역 rota hangs
by two magnets (user canon: 자석 not 압정; morning 일기장 not 알림장),
수아's hand goes to 유림's crooked rota and 재호's forgotten recorder
first, and 담임 임유정 (first appearance, flat-temperature short-
spoken) cuts it kindly — **`수아야. … 네 것부터 끝냈어?`** / `남의 것
해 주는 거, 나쁜 거 아니야. 근데 네 이름 있는 칸부터.` 유림 and 재호
finish their own work themselves; 수아 discovers her own box was the
empty one. Violin with 하랑 (anchor served; USER CANON FIX: they
started violin TOGETHER, not 하랑 three months earlier): rests and
entries — `쉼표가 제일 잘 세야 하는 거야` / `쉼표도 음표니까. 소리 안
나는 음표.` Shop evening (수아's spot = OUTSIDE the yellow safety
line, user-fixed): copying the return log (smudged-stroke guessing +
question-mark rule), she finds cooling checks slipping behind sealing
— re-check marks `여섯 장에서 넷. 매번이었다` — bridges it through the
rest-metaphor, and offers a TABLE, not talk: redrawn order with one
arrow, **`냉각 확인을 밀봉 전으로 옮기면, 두 번 안 열어도 돼요.`**
Her hand trembles offering it; 영진's danger-first sentence dies at
the arrow (`수아야. 여기 일은 네가 하기—`), he silently tries the new
order (외장→관절→냉각→밀봉 is now shop canon), re-checks vanish, and
the sheet STAYS taped to the workbench — the basement's grammar of
praise. FS-003 one beat spent: `덜 씻긴 얼룩`, observation only,
`오늘 본 것 중에 제일 중요한 것은 그게 아니었다`. Delegation with the
three conditions — **`혼자서는 안 한다. 전원은 안 올린다. 조종석에는
안 간다.`** — 수아 hands them back one by one (`…조종석 안 갈게요`),
영진 forms the misreading `기록만 맡기면 전투 가능성에 접근하지 않을
수 있음`. Dana: `글씨가 작아졌네` → sees the repetition was her own
body being opened twice → **`다음에 내가 돌아오면, 네가 먼저 봐 줘.`**
— a request from beside, not permission from above (trichotomy stated:
표는 수아가 보고 무게는 언니가 들면 됐다). Hook: in the never-filled
**확인자** box she writes 도수아 small in the corner; 영진 adds beside
it **`전원 차단 후 확인.`** — two handwritings sharing one box; stairs
(basement→shop, LOC-05-safe) and the soup-is-getting-cold shout. New
canon: EP28 = Tue 5/10 one day; rota/magnets/일기장 classroom details;
임유정 core; 하랑 same-start; inspection-order canon; new ledger with
확인자 box as standing prop; violin recital next week (minor unpaid).

EP29 「아무 일도 없는 날」 locked in (34_EP029_승인완료, **S5 FINALE —
arc closed** with 종료장부 대조서 8/8+11/11 and 아크캡슐 S5): the
unbroken-day chapter, Dana-attached again. School: leftover sports-day
events in a regular PE period — 성호 owns the stopwatch and claims
**`한 박자 늦게 눌러 준 기록이다`** (new wording, no EP24 reuse), Dana
crushes it with 13초 1 (`달리지도 못하는 기록원이 말만 빠르네` /
`기록원은 원래 입으로 일하는 직업이야`) — loud rivalry fully restored
in front of the class; kid-crack: she can't press her grin down
(혜정: `너 웃음 참는 거 다 보여`), rights his fallen crutches without
looking (`바람이겠지`). 주호 quietly removes one accommodation
(`이번 주부터 너도 금요일까지다`, no explanation) — "the most
grown-up kind of looking-after." B1 completed form: Dana tells 혜정
first, texts at the promised time, 혜정 replies with ONE PHOTO of
tomorrow's supplies (`니가 오키라고 하고 안 챙긴 게 이번 학년만 세
번`), evening phone call replays the day — narrator line: **`그 두
가지만 빼고 다른 건 다 말하는 애였다`** (the banter-guard thesis).
Shop evening: chores split three ways, first squall of the year
(season hinge), then the shop's buoy terminal (canon: neighborhood
notice-board device, buoys 7/5/2 = far sea → mid → seawall) logs
sequential dropouts sea→land during the squall; 영진 blames rain but
leaves the screen on, later reads matching narrow smooth humps in the
water-displacement graphs (`큰 것이 물속으로 지나가면 이런 산이
생긴다`), says nothing at dinner (counting gag: 수아's `네 번째요`).
Hook: on the recovered screen one trace won't wash out — a short line
from open sea toward the seawall, CUT OFF partway; **영진 raises the
half-lowered shutter back up.** The kids know nothing. User passes:
22 annotations (v0.2 — **Arabic-numeral rule established**: concrete
figures like 13초 1·0.5초·7번·3교시·4월·15분 in Arabic; clock hours
`일곱 시`, approximations, and life-units stay Korean) and a tone
note "혜정 is too monosyllabic lately" (v0.3 — banter restored in 5
spots + **retro pass over 8 approved chapters** EP5·6·7·8·18·19·24·26,
documented in 소급정정 2026-08-10 혜정수다; deliberately terse
chapters EP4/11/13/17/25/27 untouched). Drawer photo: confirmed
DEFERRED past S5 (outline B2 military-rest lock outranks the old
"S5 residue" memo — user approved).

EP30 「폐허 아래의 관」 locked in (35_EP030_승인완료, **S6 「멈춰야
사는 바다」 opener**, important chapter; user pass: 4 annotations +
one physicality catch): the series' first ambush hit. Thin Thursday
(혜정's seat-lottery probability theories, 성호's ground-condition
correction theory), then the shutter half-open at 3 PM — 영진's
sleepless night (**one-arm fix now canon: he sits with ONE hand on
his knee, never 팔짱/two-hand gestures**). Family share: `어제 비 올
때, 바다에 뭐가 지나갔다` — 수아 transcribes the dropout times
(`간격이 같아요`; "같은 간격으로 움직이는 것은 파도가 아니다" hangs
unsaid). Military notices arrive via the PUBLIC NET (user canon):
zone clearances + submerged-structure data, 고명준's two official
sentences (anchor served); drone readout `미상 구조물 — 폐허 잔해와
구분 곤란`. Sortie decision: `접촉하기 전에 경로를 알아야 한다…
가서 확인만 하고 온다`; one extra bowl of rice (sortie-day grammar);
gym clothes. B1 live: three drafts erased, fourth sent — **`오늘은
약속 못 지킬 수도 있어. 기다리지 마`** → `어. 말해 줘서 고마워`
(the girl who argued three seat-lottery proofs at lunch sends one
line at night). 수아's send-off = ledger laid open + `돌아오면 내가
먼저 볼게`. 영진's charge: `발 딛는 데를 믿지 마라. 저 아래는 전부
무너진 것들 위다.` Sunken downtown (first canon physicality:
seabed road, tilted lampposts, half-eaten signs, bus-stop roof,
buildings missing second floors; headlights die a few steps out;
nothing to grab — lampposts pull out, roofs collapse). Tubes knock
back concrete sound that proves nothing; kid-cracks: dry mouth
underwater, `침착하자, 도단아` (and knowing the need for the words
disproves them), **shoulders loosening by themselves — "풀렸다는 걸
알아챘다. 그게 제일 무서웠다"**; the sixth tube's contraction
misread as current. Contact: `맞은 게 아니었다. 잡힌 거였다` —
jaw-only strike on the right ankle, world tips over, drag begins
("잡은 것을 놓칠 걱정을 안 하는 힘"); April's arms were VISIBLE,
this time **the road bit**. Hook: slime threads herd concrete
shards onto ankle→calf, bricklayer-steady, a tube mouth building
itself around the leg — close-up cut, no comms, no rescue. Chapter
ends MID-CRISIS: **SNAP-030 is a sustained-crisis snapshot; EP31
enters with ZERO time skip** (S4 EP20–23 serial-battle pattern).

EP31 「부러진 턱」 locked in (36_EP031_승인완료, important chapter;
TWO structural user passes + one consistency catch): first escape,
first voluntary retreat. Cold open in the crisis. Futility chain
rebuilt JAW-CENTRIC per user note ("focus on wrestling the jaw, not
slime description"): ① pulling — hooks bite deeper the way you pull
② two-handed prying — wet boulders, hands slide ③ debris lever —
snaps; hardening demoted to background half-beat (`조용한 뒷공사`).
**CRITICAL user correction now standing: the stillness insight
("stop moving and it stops hardening") belongs to EP34–35's static
battle and must NOT appear before then** — EP31's realization capped
at "pulling straight only hooks you deeper" (`갈고리는 원래 그렇다`);
even OBSERVATIONS of threads slackening are banned through EP32–33.
Climax physics per user's staging: the jaw NEVER releases the ankle
— it slackens only to re-grip deeper; as the maw opens around her
trapped ankle, both hands JAM INTO THE GAP (`물릴 자리에 제 팔을
먼저 채워 넣은 모양새`), inside-prying fails, then she abandons
prying, hooks the jaw root over the tube's concrete rim and CRUSHES
DOWN with arm strength plus the whole weight of her caught leg —
`물려 있다는 것이 처음으로 이쪽 무기가 됐다` — LEFT jaw breaks at
the root (same-entity marker for EP34's asymmetric regrowth); only
then arm out, leg out. Kid-cracks: own breathing filling the
cockpit, counting that dies at two, fake-hope spike (`희망은
물속에서 제일 비싼 낭비였다`), `"빠졌어요!"` as a burst not a
report, wobbling legs a half-beat too slow, `대답이 너무 빨랐던 게
조금 분했다`. Retreat = presence only (dust, one seaward surge,
fading vibration); aftertaste unresolved (`이건 5승인가.
무승부인가`). Military log = REMOTE READOUT ONLY (user consistency
catch): drone-based marker record, **`실물 잔류물은 미확보`** — the
broken jaw tip and slime clot exist ONLY on 영진's tray (canon:
kills any military-analysis plot; the sole eye on the evidence is
영진). Log's last line: `검은 거인, 자력 이탈 확인.` Hook delivered:
the slime clot cracks open on the tray and concrete dust aligns
itself along thread-like structures — 영진 watches, zero narration.
수아's first live checker run: transcription + a small-hand margin
note (`그건 항목에 없네` — off-ledger observation begins).

EP32 「아프면 아프다고」 locked in (37_EP032_승인완료, standard
chapter, approved WITHOUT annotations; two user corrections landed
at the brief stage): the safety map is an AFTER-SCHOOL group
assignment (a town-survey task can't happen in class — user catch;
fieldwork done off-page over the weekend, today is drawing day,
submission Monday with Dana carrying it), and the rumor is built
with ZERO witnesses (user catch: the battle was underwater at
night) — public-net clearance notice via a fishing family's kid →
quiet morning lift → adults' "괴수가 나왔다더라" → the classroom
completes `괴수가 우리 동네 거인을 보고 달아났다` from the mere
fact that nothing happened; the tale EVOLVES by recess (went away →
faced off → established fact minus witnesses), 성호 running
distribution (`목격자가 없다는 게 제일 확실한 증거야`), 주호's
one-line closure. Dana's dissonance held to one inner half-beat
("도망은 맞다. 보고 도망간 건 아니다" — and she alone knows nobody
saw anything). Stair-path scene: her shortcut (forty-odd steps,
relay-training pride) marked safe → 성호 (staying anyway in his
cast-pickup wait) objects with the lock line → her lock retort →
the kids themselves reroute to ramps/wide alleys (stroller,
grandmother, `다친 사람도. 지금 여기 하나 있잖아`) — "자기한테
안전한 길이 남한테도 안전한 건 아니라는" first lesson; walking the
survey showed her curbs and puddles a runner never sees. B1 heart
in a two-person half-beat (예진 off fetching water): `너 오늘 좀
피곤해 보여` → lock line → `진짜 아프면 먼저 말할게` — narrator
thesis: 혜정's worry grows into RULES, not questions (`물을 수 있는
자리를 하나씩 만들어 두는 것`); weight held short, banter resumes
(gull-drawing voted down 2-1). B4 close: brag with self-sourced
statistics → `다 나으면 지도보다 운동장 기록부터 고쳐` — rematch
mutually "예약해 놨다". 한결 half-beat anchor served (silent
tidier). Hook: suspicious rock-paper-scissors makes Dana the
carrier; 혜정 folds the map grain-aware and hands it over with the
lock line; Dana answers with her hands only — corners squared
twice, front pocket, zipper shut ("마을 하나가 들어 있는 무게치고는
가벼웠고, 약속 하나가 들어 있는 무게치고는 묵직했다"). New canon:
safety-map physicality (blue/red, two shelters, breakwater
hatching, corner sun, erased stair-path trace), stair path = forty
steps school→post office, rumor-formation pipeline, 혜정's
rule-making worry grammar. Grep note: `조사해서` (homework survey
context) logged as false positive.

EP33 「닦이지 않는 흔적」 locked in (38_EP033_승인완료, standard
chapter; brief-stage corrections: INDUSTRIAL-scale wash per user
("호스·솔 수준 금지" — scaffolding, chisel-and-hammer two-person
teamwork for the one-armed 영진, grinder on a rest, pressure washer
whose recoil Dana's body absorbs, rain-sound filling the hangar —
half a day for one ankle), and the term is **점액 띠** not 고리
(user: "ring" reads too literally). Shop morning: waterlogged
machines queue up ("괴수의 흔적은… 물 먹은 무전기와 밀린 일감으로.
소문은 학교에서 자라고, 일감은 수리점으로 왔다"); 기태 anchor
(`박사님`, haggling pump deadline, `어이, 조수. 그 펌프 함부로 들지
마라` / `이미 들었는데요`), 미란 anchor (fan pickup + new sensor).
B3's first live catch, watched through Dana's eyes: 수아's pencil
stalls on an EMPTY cell — `오른발목 하부 점액 제거 뒤 구동저항
재측정` — question-grammar only (`이 칸은 나중에 적어요?`); recheck
(`……확인 해 보마` — user line) finds a mineralized slime BAND inside
the ankle-armor seam where even the pressure washer couldn't reach
(the title's first meaning); quiet promotion: `다음부터 이 칸은 네가
불러라` ("칭찬이었으면 사렸을 텐데, 절차라서 받을 수 있는 것
같았다"); sister exchange canonizes the trichotomy — `칸이 비어
있으면 그냥 보여. 까만 데에 흰 게 있는 것처럼` / `언니는 무거운 게
보이잖아` — Dana's verdict: "같은 편이라서 그랬다." Rule half-beat:
re-send (`통화하기로 한 시간` — user fix), photo reply (recorder +
folded safety map = two naggings in one photo), `니 리코더도 있는지
확인해 봐` / `……있음` (three minutes, tactfully unmentioned). Hook
(영진 alone): **military data-drop canon (user addition): `거인이
자기들 자료를 쓴다는 걸 눈치챘는지, 요즘 군은 매번 자료를
뿌려댔다`** — the army KNOWS the giant reads its public-net drops
and feeds it deliberately (B2 tacit-support made explicit); drone
footage — MORE tubes than were destroyed, a head briefly out, left
jaw regrown short/thick/crooked (tray comparison cut), tubes
swelling `숨을 내쉬듯` venting murky threads between sunken roads,
the crooked jaw catching the last frame and vanishing — "저것은
그저께 도망친 것이 아니라, 돌아와서 무언가를 하고 있었다." Kids
know nothing. New canon: industrial wash procedure + `세척 후
구동저항 재측정 = 수아 호출` checklist line; slime-band term;
military deliberate data-drops; `물 먹은 기계한테는 요일이 없다`.

EP34 「움직일수록 굳는다」 locked in (39_EP034_승인완료, important
chapter, approved WITHOUT annotations; the stillness-insight unlock
chapter): 승부욕 seed (`돌아왔네` before fear; "기분이 좋다는 게
이럴 때 좋은 신호가 아니라는 것까지는 셈이 안 됐다"), the broken
tteokbokki promise canonized (Sun 3 PM, 예진's hijacked plan —
`오늘도 약속 못 지킬 수도 있어` / `어. 컵볶이는 도망 안 가`, NEW
UNPAID item), rampage heard not seen, floating debris observed
correctly but READ wrong (three misreadings + the EP31 bait `부서지기
전에 찾으면 된다`), the charge past 영진's half-beat `……단아야`.
The ladder of awareness (gauntlet→wrist→knee→waist), the left arm
lost to its own habit ("왼팔이 제일 먼저 굳는 건 왼손잡이가 제
손으로 정한 순서"), escape route silted shut, the late realization
("이쪽이 이긴 방법을, 저쪽이 제일 열심히 공부했다"). The mandated
armor-joint paragraph delivered ("팔은 멀쩡했다… 멀쩡한 팔로 돌이 된
팔을 입고 있는 것"). The shrinking-list device ("지워지는 쪽을 세는
셈은 셀수록 손이 차가워졌다"); the right arm = "평생 왼손 뒤에 세워
두기만 한 손." The unlock in locked order: exhaustion-stop → slowdown
seen → one-finger test (and the resisted urge to double-check: "한
번 보고 믿어야 하는 것도 있었다") → `나를 붙잡는 건 점액만이 아니다.
점액 속에서 움직이는 나 자신이다` → fist held at the entry line →
`저 안 움직일래요` / 영진's `그래. 그게 맞다. ……잘 찾았다`. "태어나서
제일 힘든 가만히." Hook: pressure wave, reflex half-inch, three
pebbles, dissolution — "온 것도 없는데 값만 치렀다." **SNAP-034 is
sustained-crisis snapshot #2: EP35 enters at ZERO time skip.**

EP35 「한 번만 움직인다」 locked in (40_EP035_승인완료, important
chapter — **S6 FINALE, arc closed** with 종료장부 대조서 8/8 and
아크캡슐 S6; one user correction: the carcass DISSOLVES): the wait
(the unfair trade — "저쪽은 보내는 값이 없어 보였고, 이쪽은 받을
때마다 값을 냈다"; stillness redefined as saving one right hand),
letting go of four things (the left hand's empty place, the clumsy
right's doubt, the urge to smash a tube, the alarms), the tell
discovered ("밀어내는 건 가짜다") and the REAL tell recovered from
EP30's misread current — "틀린 답을 제일 비싸게 산 사람이 그 답을
제일 잘 기억하는 법" — 영진's quiet surrender on comms (`……그래.
그거였구나`). "와라가 아니다. 오면, 이다." The counter: inhaled
water, both jaws (crooked left included) fully open, whole-body
launch — right fist straight in ONCE ("하루 종일 한 자리에 두는
것으로 조준을 미리 다 해 놨고"), freeze at extension, the entity's
momentum grinds itself apart on the fist, the last kid-crack is the
war against pulling out — weight settles on the arm, `"저 잘
서 있죠." / "잘 서 있다."` **USER CANON FIX: the carcass then melts
off the still-extended fist** (EP4/16 dissolution lineage — "빼지
않은 주먹 위에서 상대가 없어져 갔다"), leaving only debris; military
log adds `용해 확인. 수거물 없음` (5th straight no-recovery) and
`검은 거인, 자력 귀환.` C1 first window delivered per outline:
right index/middle fingertips dull for tens of seconds → normal —
self-reported (`둔했어요`; "크기가 작을 때 말하는 게 말하기 제일
쉬운 법"; the promise moved before her mouth — inner beat only);
영진 records WITH TIMESTAMPS ("무엇인지 모르는 것일수록 언제였는지
라도 정확해야"); 수아 adds the hand-sensation line, pencil half a
beat slow. Hook: two lines on the open-sea screen — different
bearing than EP29, then an opposite-side second — never meeting,
moving toward 청해 in parallel. Kids know nothing. S6 = 5/12–5/15,
four days, two battles, one entity, zero recoveries.

EP40 「마지막 회수」 locked in (45_EP040_승인완료, IMPORTANT
chapter, S7 5/5) — **THE SPRING SEASON (EP1–40) IS COMPLETE.** Two
user directives reshaped the final text: (1) the class-notes photos
are NOT absent-friend care — Hyejeong is Dana's DESKMATE (new
canon), and the text reads `아까 보니까 니 공책 반이 백지더라. 보고
베껴 놔. 내일 보자. 성호가 내일 기어코 마지막 한 판 한대` — she
watched the half-blank notebook all day, said nothing in class, and
sends her notes at night ("옆자리는 못 속이는 자리였다"); (2) the
early-summer hook was DELETED — no enemy tease, season-1-finale
ending: Yeongjin closes the spring ledger (one volume, late March
to 5/18, ending on `이상 없음`), decides tomorrow is soon enough to
start a new one, and "봄이 그렇게 끝났다." The speed-type
silhouette, three-digit speed cell, Iron-Anchor need, and the
reclassification review all moved to an AUTHOR-ONLY HOLDING BIN —
summer's flow is explicitly UNDECIDED. In-chapter: the patience
finish (watch one full haul cycle — "다섯 번의 싸움이었으면 벌써
치고 있었을 것이다"; "저 틈은 저놈이 직접 벌려 준다"), fingers into
the self-lifted deck plate, wrestling flip stealing the carrier's
own pull, exposed underside, membranes pulled apart two ways —
function kill #2, BOTH entities dissolve (nothing recovered, as all
spring). Military spring settlement: sequential behavior records
only, identity/base/pilot unknown, `미식별 검은 거인`. C1 spring
line: all ten fingertips felt, grip/gait/vision normal, `이상
없음` plus deliberately blank lines — no diagnosis. Rule #3 paid in
full (`끝났어`; "세 자리가 다 찬 것은 오늘이 처음이었다"). Next day:
scoreboard chalk war, Juho's one-swing condition nobody believed,
Seong-ho's last at-bat = 14m — **54:54 TIE** (three tape
measurements; "화낼 데가 없으면 화가 웃음이 된다"), rivalry fully
restored, rematch-of-the-rematch (+ a footrace demand) banked for
summer. Tteokbokki debt from EP34 paid ("고혜정 은행 — 예금은 안
받고 대출만"). SPRING CLOSE-OUT COMPLETE: S7 ledger audit 8/8 (6
match, 2 APPROVED DEVIATIONS: B1's school
evacuation-prep beat dissolved by the EP38 relocation; the
early-summer hook deleted), arc capsule S7 v1.0 (with the
summer-planning gate checklist), appearance ledger v1.38 (summer
restart memo: recount all gaps, Harang anchor mandatory, deskmate
canon).

EP43 「낯익은 신호」 locked in (48_EP043_승인완료, STANDARD chapter,
S8 3/10 — the TURN): Sat 6/11–Mon 6/13. Yeongjin runs the comparison
between customers ("일상과 대조를 한 책상에서 같이 하는 것도 봄에
익힌 기술"), waveforms hit 3 with the gap shrinking from under a
day to half a day ("오는 데 부지런한 놈은 봄에 없었다"), and the
matching page is mid-April — its last annotation, fainter than the
rest: **이후 기록 없음**. Sunday's family briefing re-runs the
spring grammar (the open sliding door as summons; "돌려 말하지
않는다. 무섭게 말하지도 않는다"; `모른다` given as `모른다` —
"아는 척은 봄에도 없었다") and stops at the ceiling line **`봄
기록하고 겹치는 데가 있다`**. Then the DOUBLE SILENCE: Sua rises
without a word, fetches the tub from the bottom shelf and sets it
on the workbench (spine fragment — lid unopened, "필요해지면 여기
있다는 배치"); Yeongjin looks at the tub, then at her — "문장으로
옮기지 않은 채로 전달이 끝나 있었다"; only Dana lags half a beat
and then goes cold. Flag collected: the `계속 이랬으면 좋겠다` wish
lasted two weeks and change, and "바람치고는 알찬 바람이었다" →
`온다면, 받아 준다`. Monday: public notice reinstates outer-zone
control, and the classroom METABOLIZES it — Seong-ho's three-day
theory (sample size five), Hyejeong mapping detour routes on the
chalkboard, "무서워하는 법도 는다"; **Hyejeong's semi-conscious
notch #1** — she's fast at this because of spring, and "아무도 묻지
않았고, 본인도 묻지 않았다". Preparation resumes (two hill runs,
Sua's blue-spring/red-summer overlay "더우니까", cockpit warm-up
with zero start-up, `보수할 데는 없다. 언제든 나갈 수 있다`), and
Hyejeong's rule-reactivating text **`또 시작인가 보네. 알지? 늦으면
늦는다고`** → `알지`; Dana starts chasing what else that could mean
and stops herself. Hook: 22:30, the watch screen "calls the eyes"
— a hemispherical silhouette cutting water, passing buoy zones 7
and 5 WITHOUT STOPPING (spring's all stopped somewhere), the 이후
기록 없음 being erased on screen, Yeongjin's hand moving toward the
comm — it comes straight on. Three annotations: 학교→**시립**
수영장 (×2), and `화 하나`→`하루 하나` — **new page-level ban
registered: the author-side unit `화` must never appear in prose.**

EP44 「다른 여름」 locked in (49_EP044_승인완료, IMPORTANT chapter,
S8 4/10 — the first engagement of summer): the same Monday night,
zero elapsed time. **A NEW STANDING PROCEDURE was created by the
user mid-draft: lock the BATTLEFIELD STRUCTURE before writing any
combat chapter** — (1) water depth, (2) cover and its DURABILITY
(a consumable resource, not scenery), (3) sightlines and light,
(4) movement constraints, (5) how exposed the enemy is, and
(6) HEIGHT/MASS COHERENCE. The first draft was written as an
underwater fight and had to be rebuilt entirely. Canon now: the
outer-wall ground is the **drowned old city — an apartment estate
in thigh-deep water** (the machine's whole upper body is above the
surface; underwater vocabulary is banned), lower five or six floors
submerged, **ten-to-twenty-odd floors still standing above water**
(the machine is 52m ≈ a 17-storey block, so three-storey ruins are
not cover). Cover does not vanish — **it gets SHORTER**: harpoon
tips tear the top floors off, so a block drops from above-the-head
to shoulder to chest to waist, and Sua's terrain screen — which
labels each block with the floors remaining above water (열여덟,
스물둘, 아홉) — turns from geography into a BALANCE. Mass coherence:
no rolling, no diving, no quick dodges; the machine shoves off a
wall and slides sideways, "무거운 몸이라 빨리는 안 됐다"; four
strides between blocks.

The chapter itself: Yeongjin's call (`단아야. 내려가자.` — the house
is single-storey, so the summons is DOWN to the basement, and Dana
crosses to the shop through the sliding door, never stairs), the
spring urchin returns REFITTED (spines re-aligned to even length and
spacing, thickened bases, **tips split like harpoons** — "뾰족한
것은 찌르라고 있는 것이고, 갈라진 것은 박히면 안 빠지라고 있는
것이다"), and it MOVES, taking its own angle. Then it FIRES. First
hit: half a step back, foot scraping the bottom, water bursting,
the cockpit shaking, the seat-back hitting her spine — **it did not
pierce**, and that is as far as the page goes: `몇 번까지 버티지`
(the null is author-side; Dana and the reader never get the
guarantee). What lands harder is INTENT — spring's monsters wanted
to carry her off, "끌려간다는 건 저쪽이 나를 온전한 채로 원한다는
뜻"; this one wants her broken: **`봄이 끝났다는 걸, 단아는 통지문이
아니라 어깨로 알았다`**. Three approaches, three stops: "팔이 짧아서가
아니라 거리가 멀어서 지는 싸움" — and one wish for "팔보다 긴 게"
(the ANCHOR SEED, unnamed, folded away as a tantrum, not a plan).
Hook: with her count broken, her body counts instead — fire, pause,
fire — **`간격이 있다`**, and she starts fitting her strides to it.
Annotations: `발목을 노렸고`→`뽑으려다 실패했고` (spring recall),
`내려와라`→`내려가자`, `계단을 내려가니`→`미닫이를 열어 보니`
(LOC-05 single-storey coherence — **the `내려와/계단` family is now
banned inside Dana's house**).

Tooling: the mobile annotation app was rebuilt to anchor notes by
PARAGRAPH CONTENT (hash + nearest-paragraph search) instead of
paragraph ordinal, which had been silently shifting annotations onto
the wrong paragraphs and double-rendering applied edits.

EP45 「빗속을 걷는 법」 locked in (50_EP045_승인완료, STANDARD chapter,
S8 5/10 — summer's FIRST KILL): the same night, continuous. Dana's
count is half a beat off, so she counts what is left instead —
FIVE blocks above water, "한 채가 서너 발", twenty shots and the
cover is gone. She overturns spring's verdict: pushing it away was
not a solution, "그건 오늘로 미뤄 둔 것이었다" → **`…이번에는 부술
거야.`**, and she notes that she said it while still afraid. Then
the SQUALL: rain arrives all at once, the surface boils white, and
the interval she had just earned is buried under the noise ("아,
진짜." — the childish grievance is the point). So the count moves
from EAR to SHOULDER: the quiet stretch is exactly as long as it
takes her pushed body to straighten, "한 번은 맞아 봐야 알 수 있는
셈이었다."

THROWING (the user's addition, and the ANCHOR's causal seed): she
reaches underwater and comes up with a dozen sunken cars — GRAVEL
in her palm, scattered for nothing: `"…너무 작다."` She re-picks —
a whole wall face torn from a collapsed block — and throws. It does
not break: **it ROCKS the thing**, aim slipping, spines going out a
beat late. She recognises it instantly because it is what has been
happening to her all night. But the lesson is the other half:
**손을 떠난 것은 저쪽에 닿는 순간 이미 이쪽 것이 아니었다. 밀 수는
있는데, 부술 수는 없었다** → what she needs is something longer than
her arm THAT SHE DOES NOT HAVE TO LET GO OF. "없다는 것과 필요하다는
것은 다른 이야기" — no naming, no request (S9 pays this off).

The approach lands only when the resource is spent: the last block
drops to waist height, the thing is rocked a beat late, and four
strides becomes three. Spines: thick bases, so she twists and puts
her weight in; the second goes faster; the last few she GRABS IN A
BUNCH and snaps at once. The refit is confirmed by touch — "자로
잰 것 같았다… 편했다. 편하다는 게 이상했다." Then the KILL, which
is the starting point of the whole melee-growth curve: she does not
know how to hit. "주먹을 어떻게 쥐어야 하는지도 제대로 몰랐다." She
raises the arm and brings it down until it breaks, loses count, and
cannot tell fear from wanting to win. Held things break what thrown
things only push. Dissolution: 검붉은 것 spreads and unwinds, and
the spine still in her hand runs out between her fingers — **zero
recovered material, confirmed visually**. "이겼는데 이긴 것 같지
않았다."

RETURN (restructured on the user's note — the family meets her in
the HANGAR, not the shop): Yeongjin waits at the ladder with a
towel and one line, `"오래 걸렸다." … "오래 걸릴 만한 일이었다."`
Sua is already at the machine's feet with a flashlight and a
clipboard — the post-sortie inspection has been HERS since spring
and she has never handed it off — counting hits aloud: `"오른쪽
어깨." "자국 늘었어. 다섯 개였는데 여덟 개."` … `"많이 맞았어."`
Not comfort; a count. Dana realises her sister counted what she
lost count of. Then up the stairs, through the iron door, into the
shop: the tub is opened for the first time, spring's plain-tipped
fragment set beside the frozen frame of tonight's split tip, and
Sua concludes in one sentence — **`"봄 거랑 같은 데서 나온 건데."
… "가시만 나중에 바뀐 거야."`** (fact only; who and why stay at
zero). New canon: **Sua NEVER uses honorifics to Dana** (only to
Yeongjin — checked against all 44 approved chapters, zero
violations); the hangar-return protocol; the dissolution's
held-fragment detail; and the throwing rule.

EP46 「기록의 온도」 locked in (51_EP046_승인완료, STANDARD chapter,
S8 6/10 — the price of winning is silence): Tuesday 6/14, the day
after. Two STANDING RULES were established by the user mid-chapter
and applied retroactively.

**(1) Family speech levels.** Dana speaks BANMAL to Yeongjin — the
EP1 baseline is `할아버지, 이거 언제 만든 거야?` — and that holds in
comms and status reports too. Recent summer chapters had drifted
into honorifics; RETROFITTED: EP44 four lines (`얕은 데야?`,
`버티고 있어.`, `안 뚫렸어. 근데 밀려. 맞을 때마다 뒤로 가.`,
`아직 멀어. 가릴 게 줄어.`) and EP45 two (`보여.`, `…응.`).
Sua is the mirror: HONORIFICS to Yeongjin, banmal to Dana, and in
mixed scenes she splits by ADDRESSEE with the switch visible on the
page (report to grandfather, then turn her head to her sister).

**(2) Sua never works alone.** The first of the three conditions
attached when she was given the inspection job in EP28 —
`혼자서는 안 한다. 전원은 안 올린다. 조종석에는 안 간다.` A
companion must be visible on the page in any inspection scene; here
the underside check happens with Yeongjin (`그 시간에 할아버지는 위에
있었다`), which retroactively explains why she deferred it in EP45.

**(3) Where the rumour comes from** (also a user note): EP44–45 were
fought at night, in rain, outside the flood wall, with ZERO
witnesses on the page — so the chapter had to establish the chain.
Canon: the fight is witnessed ONLY as **light and sound** — the
sparks off each hit, seen from high floors inside the wall with the
shape erased by rain; the pounding heard in the near neighbourhoods;
the control order itself as evidence something happened; concrete
debris washed south by morning (the creature leaves NOTHING —
dissolution canon holds). No night fishing (the water was under
control order). The kid-chain carries it to school. Because they saw
only flashes, the reading is **`공격당했다더라`** — it was being HIT
— and nobody knows who won, which is exactly why the rumour turns
from fear into WORRY: "무섭다는 건 재미있다는 뜻이기도 해서, 애들은
늘 조금씩 웃었다" → **오늘은 웃는 애가 없었다** → `그 거인 안 오면
어떡해.` Seong-ho then becomes useful for the first time, moving
from counting flashes to citing EVIDENCE: `통제 오늘 아침에
풀렸잖아. 안 끝나면 안 풀어.` — the opening and closing of the
control order is the city's ONLY public scoreboard. The room
lightens. Dana says nothing: **`할 말이 없어서가 아니라, 할 수 있는
말이 없어서.`**

The military scene is written as a DOCUMENT: the same blanks as all
spring (미확인. 미확인. 미확인.), one line changed — `접촉 시도` →
**`원거리 공격 확인.`** — and the description shrunk twice, because
`판단은 문서의 일이 아니었다`. Myeongjun signs off on
`민간 목격 신고 다수 — 발광 및 소음. 형체 확인 없음.` (`신고가
있었다는 건 확인된 사실이다`), and Yun Seojin (captain, aide —
gap 25, reminder discharged) then scrolls the intranet list past
**ONE LINE of foreign news**: a port in some distant city closed for
three days, no reason given, "routine inspection" is all the local
authority says. Two sentences. He reads it in under five seconds and
moves on. That is rung one of the WHITE SENTINEL ladder (new thread
FS-C5, seeded at 46: no name, no photo, no machine, no country, no
character's interpretation). Yeongjin's summer ledger is six pages
in a week where spring took three, Dana finally says `어제. 무서웠어.`
and gets `무서운 게 정상이다`, and the hook: the south buoy shows a
line that does not come straight in from deep water but hugs the
shallows along the coastline, unhurried — **`가는 게 아니라 훑는
것처럼 보였다`**.

EP47 「집게」 locked in (52_EP047_승인완료, STANDARD chapter, S8 7/10
— the first fight on ground the ENEMY chose): Wednesday 6/15, afternoon,
the first daytime battle of summer. New battlefield, locked before writing:
the tidal flat outside the flood wall — water below the KNEE (dry patches
in places), **zero cover**, mud, and an incoming tide that softens the
ground over about two hours. The physics is the fight: **a bipedal 52m mass
lands on two feet and SINKS**, so every step has to be pulled free and the
pulling pins her in place, while eight legs spread the same weight and stay
on top. Dana gets there by feel, not by physics: `쟤는 왜 안 빠져.` →
**`여덟 개로 나눠 디디니까`**.

The sortie route now carries the theme: outside the drowned station it is
still deep water, and as she walks toward shore it drops chest, waist, knee
— **`걸을수록 몸에서 물이 빠져나갔고, 빠져나가는 만큼 몸이 무거워졌다.
물이 받쳐 주고 있었다는 걸 물이 없어지면서 알았다.`** The creature does not
hide: flat low body about hip height, ONE claw the size of its whole body,
a small one on the other side that stays folded and **never moves once**
(reserved for EP48), eight legs, sidewise gait. The big claw does
everything — strike, block, shove, sweep, jab — but it is SLOW: the shadow
arrives at her feet before the claw does, and it comes at a speed spring
would have let her step out of. She cannot, because her feet are in the mud.
That is EP44's `오는 것이 보이는데 못 피한다` again, from a different cause.

The block lands as sound before impact — `낮고, 길고, 배 속을 누르는 소리`
— and then **`무거운 것이 무거운 것을 친 충격이 몸 안쪽에서 두 번 울렸다.
한 번은 부딪힐 때, 한 번은 부딪힌 게 지나가고 나서.`** Zero penetration,
large displacement; her feet stay pinned and only her upper body goes, so
she falls. Falling is NOT new (EP30, ankle seized, underwater) — what is new
is **how long getting up takes**: the hand she plants sinks, and
**`힘이 모자란 게 아니었다. 힘은 남았다. 그래도 못 일어났다.`** She works
out two things on the spot: plant the arm SPREAD WIDE instead of on a point,
and drag the leg up rather than pull the foot. Meanwhile the flood wall is
lined with people — the shape being visible is nothing new (spring had
daytime fights), but today what the city watches is a losing one. Hook: half
risen, the big claw goes up again, slowly, exactly as before, **and her feet
are still half-buried**.

Two rules were added here. **Sua does not speak on combat comms** — her place
is observation, inspection and terrain BEFORE and AFTER a sortie; tide,
status and warnings all come through Yeongjin (`있다. 두 시간쯤 본다.` /
`그 안에 끝내라.` / `아까보다 빠르다` — "급할 때도 급하다고 말하지 않는
사람이 속도를 두 번 말했다"). The single exception in the whole series is
EP38's `언니, 큰 건 눈이 없어. 꽃이 눈이야.`, and that line's weight must not
be diluted by routine chatter. And the first siren is canon-corrected: it was
heard on a **March field trip**, not in a classroom.

Tooling and skill work shipped alongside: `scripts/check_voice.py` (speech-
level drift checker, first applied here, WARN 0), the workspace **precedent
ledger** (facts already on the page — speech levels, house layout, sortie
route, battlefield history), and a skill update adding `standing-guards.md`,
`summer-level3-approved.md`, summer routing, the battlefield-lock step, the
expansion-pass reality, the three-check sequence and the nine finalization
outputs. A full-series sweep also retrofitted **44 lines** where Dana had
been speaking honorifically to Yeongjin (EP29–45, combat comms included).

EP48 「꺾이지 않는 방향」 locked in (53_EP048_승인완료, IMPORTANT
chapter, S8 8/10 — the first hand-to-hand fight, and the chapter that
decides WHERE Dana's fighting comes from): same afternoon, continuous,
tide still rising.

She does not block this time — she angles the shoulder and lets the claw
slide off (`"안 받아."`), because "정면으로 받으면 뒤로 가고, 비스듬히
받으면 옆으로 간다. 옆은 넘어지는 방향이 아니다." Then she closes first,
grabs the big claw two-handed, and **does not get pushed back** — the mass
that has been burying her feet all day is an advantage the moment the fight
becomes a hold, while eight legs have nothing to brace against. That
premature confidence is the setup.

The reversal: the big claw bites the ELBOW — the folding place, not the
shell — and then the small claw, folded and motionless through all of EP47,
opens for the first time and takes the joint. **They twist together.** No
penetration, NO PAIN: what she feels is 어긋남, her arm going somewhere it
should not go, slowly, patiently. She tries yesterday's answer (`"놔." …
"놓으라고."`) and hammering does nothing — "세게 치면 다 되는 줄 알았다.
그건 어제 통했던 거지 오늘 통하는 게 아니었다." The EP20 octopus is invoked
only as CONTRAST: that one wrapped her wide to hold her; this one picked one
spot to break her — **"넓게 잡은 게 무섭다고 생각했는데, 좁게 잡는 게 더
무서웠다."**

So she braces two-armed, and bracing pulls the two bodies together until the
faces are close — and only then does she see the **green eye-stalks**, which
pays off EP47's "눈이 어디 있는지는 여전히 몰랐지만". What arrives next is
memory, four sentences, no sentiment: a playground, behind the slide, a big
boy who made Sua cry, both of them rolling in the dirt, dirt in his eyes,
**and a headbutt right after that bloodied his nose**. His name is gone.
"그때는 이쪽이 작았다." And crucially — **"떠올랐다기보다, 손이 먼저 갔다."**

The finish runs in four beats: crush an eye-stalk → the creature makes its
first sound ever, a metal scream, and Dana reads it (`저놈은 이 상황이
마음에 들지 않는다. 뭔가 해냈다는 뜻이다`) → in the slack she takes the
small claw and folds it the way it folded her (`"너도 이렇게 했잖아."`) →
then the big one, the direction that does NOT fold, with her buried foot
finally used as a FLOOR → and when it tries to flee (the claw still held in
the black hand) she pulls it in and drives her head into it. Twice. She was
never taught how: "그냥 어릴 때 그렇게 해 본 적이 있었다." Dissolution,
nothing recovered, and her left arm works fine but the wrong-direction
feeling stays in it.

Process notes worth carrying forward. The user rejected the first draft's
RHYTHM — "너무 서술이 나열되어 있어서 읽는 리듬이 별로다" — and the fix was
eleven muttered lines and six sound descriptions plus splitting long
narration (dialogue 7.1% → 13.0%, paragraphs 141 → 169). Treat that density
as the DEFAULT for combat chapters from now on. One sentence is deliberately
in PRESENT tense amid past-tense prose (`꺾인 집게는 아직 검은 손이 잡고
있다`) — user-confirmed, a freeze-frame device, not to be repeated casually.

EP49 「여름의 셈」 locked in (54_EP049_승인완료, STANDARD chapter,
S8 9/10 — paying for two days of fighting): the return, then the next
day at school. Two user additions shaped it.

**The asymmetry of debts.** In the hangar Dana taps her sister's head
twice and says `"네 덕분이야."` — and **Sua has no idea what she means**.
The terrain map was yesterday's, she stayed off combat comms, the tide
numbers were just a table she copied. So she did nothing today. And she
DOES NOT ASK: `물어보면 언니가 대답해야 한다. 대답하려면 뭔가를 다시
떠올려야 하고, 오늘 있었던 일 중에 떠올려서 좋을 게 몇이나 될지는 알
수 없었다.` The playground is never spoken aloud anywhere in the
chapter — only the reader knows why the thanks exists. It inverts EP40,
where the same gesture paid a debt Sua understood.

**The broadcast axis came back.** The user caught that EP9 「철거작업」
established a TV drone (`통제선 밖 상공에서, 가까이 오지도 물러나지도
않는 거리를 지키며`) plus earlier photos on a board — and that summer
had silently dropped it, even though EP47–48 were fought in daylight on
open ground next to the flood wall. So: footage exists. It goes up on
the intranet board, the kids pass it around, and EP47's `통제선 바깥에도
뭔가가 서 있었다` turns out to have been the outside-broadcast van
(no approved text needed changing). The footage shows the MACHINE only —
bad quality, far away, no sound, no cockpit, no pilot. The public's
reaction is now stage three: rumour (fear) → worry (EP46, they could not
see) → **split interpretation** (they all saw the same thing and say
different things: it won / it nearly died / that is not fighting, that is
flailing / `"안에 사람이 있긴 해?"`). And Dana watches it beside them:
**`할 수 있는 말이 없어서가 아니라, 하면 안 되는 말밖에 없어서였다.`**

**A scale correction worth remembering.** The first draft washed the
machine like a person-sized robot — hand rags, seven small fragments in
the sole. The user flagged it, and EP33 「닦이지 않는 흔적」 already had
the canon: washing is INDUSTRIAL — a high-pressure gun whose recoil you
take in the shoulder (Dana's job), scaffolding, Sua outside the safety
line with the progress sheet, a raised hand meaning "next item", and
**half a day per ankle**. Rewritten accordingly: mud comes off in
body-sized slabs, the ankle seam is a gap your FOREARM goes into, the
sole holds concrete blocks you carry with both arms plus rebar, and
tonight they only get the feet and shins done. Registered as a standing
guard (`standing-guards.md` §4 and the precedent ledger §6): **it is not
only combat that is 52m** — maintenance, inspection and repair scenes
break the scale just as fast. Also: upper-body damage is seen from the
MAINTENANCE DECK, not by flashlight from the feet.

Yeongjin closes the chapter by writing the gap between the two
appearances into the summer ledger, pulling the spring ledger out of the
drawer, and setting the two numbers side by side. **봄보다 짧았다.**
`한 번이면 우연이고 두 번이면 그냥 그럴 수도 있는데, 장부는 두 번까지만
적혀 있었다. 세 번째가 오면 그때는 우연이 아니게 된다.`

EP50 「간격」 locked in (55_EP050_승인완료, STANDARD chapter,
**S8 10/10 — ARC CLOSE**). Six scenes, no combat.

**The procurement list is the chapter's engine, and it is written to
hide.** The author-only setting the user fixed before drafting: the
cell-origin material has to be cultured using equipment Hyunseo left
behind, and the reason it ends up on an ANCHOR is simply that the anchor
was the biggest, hardest lump of iron on the list — the material is
grown onto its surface. **None of that reaches the page. Ever.** The
permitted maximum is a hint that the surface texture changed. So the
list is written in three layers: (a) a crowd of vague lines — `쇠사슬.
굵기 상관없음. 길수록 좋음.` / `도르래. 있는 대로.`; (b) the one that
matters buried as an ordinary line — **`닻.` / `제일 큰 쇳덩이로.`**,
no emphasis, no reaction, nobody looks twice; (c) the ONLY precise line
is the one that needs a supplier — `구명줄 발사기. 인양용. 줄 감기까지
붙은 걸로.` followed by `기태.` and a circle. **The precise line takes
the reader's eye, which is exactly why the important thing is not on
it.** Yeongjin's answers stay half-sized: `"모아 두는 거다."` /
**`"만들 걸 정하고 모으는 게 아니다."`** Register this as a reusable
technique (concealment by specificity displacement).

**The military crosses from observation into judgement in one line.**
The June bundle's conclusion field changes to `출현 간격 단축 및 공격
행동 확인. 대응 방침 재검토 요함.` — `"관측만 적던 칸이었습니다."` /
**`"관측만 적을 수 있을 때는 그랬다."`** The subject field is still
blank (origin/identity/operator unknown, `미식별 검은 거인`), four
months running. No operations, no force numbers, no timing.

**Sua's records get institutionalised.** One sheet becomes FOUR
(기체 / 개체 / 관측 / 집안일), because `안 보이는 기록은 없는 기록이나
마찬가지`. Then she rules an extra box under 개체 with a title and
nothing in it: `"아직 없어."` / **`"생길 것 같아서."`** — and two lines
under the title, meaning a place to write more than once.

**Dana's training changes species.** Fast was for Seongho; what she does
now is HOLD — arms out, ten, then eight, then six. And she cannot say
why: `아무것도 안 하는 것보다는 나을 것 같았고, 사실은 그 정도가
이유의 전부였다.`

**The silence changed quality, not size.** `답을 못 들었는데 이상하게
안 불안했다` — in spring not being told was frightening; now it reads as
"he is preparing something". **The debt itself is NOT settled**; only how
the same silence lands.

Two user edits closed it. `저 사람` → **`할아버지`** twice (narration in
Dana's POV; the second slipped past a first sweep — see the tooling note
below). And the vacation date: school calendars are PUBLIC, so "nobody
knew when vacation was" is not a thing that can happen. **방학식 =
2050년 7월 22일**, printed on the sheet handed out at term start and
still taped inside lockers — the kids argue about how many days are left
and nobody gets up to check. That pays off the `방학식 날짜` debt and
fixes the summer clock: EP50 is mid-June, so **about four weeks remain**
before vacation, and S9 plus the front of S10 have to fit inside them.

**Tooling:** check_voice.py now also scans NARRATION for third-person
references to Yeongjin (`저 사람`, `그 노인`, `그 양반`, bare `노인이`)
and flags bare `그 사람` for review — dialogue is exempt, because a
speaker may legitimately mean someone else. Speaker attribution was also
fixed to prefer the ADJACENT paragraph over an attributed one two blocks
away (that bug had mislabelled Sua's polite lines as Dana's in EP25 and
EP46), and the polite-context test now reads the raw window instead of a
summarised hit list (so `미란 아줌마가 선풍기를 찾으러 왔다` counts).
All 50 approved chapters pass. Separately, 23 archived state snapshots
(SNAP-025 through SNAP-049) were not valid YAML — a flow-style line with
commas at block level — and were repaired; every YAML in
05_문체_상태_인계 now parses.

EP51 「인양장」 locked in (56_EP051_승인완료, STANDARD chapter,
**S9 1/12 — the arc opens on procurement, not on a fight**). Yeongjin
takes the list to the Gurae port salvage yard; Dana comes along because
somebody has to carry things.

**Gitae comes back after a seventeen-chapter gap, and the user corrected
my instinct twice — usefully both times.** First: Dana is still afraid of
him. Being acquainted for years does not wear fear down; his face and his
voice are what they are. So nothing about him softens. What changes is
the SITUATION — `오늘은 피할 데가 없었다`. EP7's escape (`수리점에 올
때는 안쪽 방으로 피하면 됐다`) is closed off, because today the yard is
his and she has to work beside him all morning. Second: he is
**건들건들 껄렁**, and the beat where Yeongjin's single `기태야` freezes
him is canon but does NOT get repeated every appearance — skipped here.

**His grammar is telling, not asking.** He reads the vague scrap lines
without a word — there is nothing to ask about scrap — and stops on the
one precise line: `"이건 고철이 아닌데요."` Then the real objection:
**`"이건 장부에 남아요."`** Scrap leaves by weight and that is the end of
it; EQUIPMENT leaves a paper trail. That is Yeongjin's actual problem,
and it pays off EP50's three-layer list from the other side. Yeongjin's
answer stays half-sized (`"남으면 남는 거지."`) and **Gitae does not ask
again** — which Dana watches: `이 집 안에서만 그런 줄 알았는데 밖에서도
그랬다`. His care arrives disguised as procedure: he calls the loading
order like a professional, and following it leaves Dana with only the
light pieces.

**The anchor got buried three ways, per the user's correction.** It is
not handed over alone — it comes with a whole pile of unsellable scrap
(`"저쪽 건 다 그냥 가져가세요. 어차피 안 나가요."`, no item-by-item
haggling), it appears as one word inside a list (`도르래가 크기별로.
그리고 닻이 하나.`), and **it does not even get loaded that day** — a
large truck comes Thursday. No hand laid on it, no lingering look, no
`제일 큰` modifier (EP50's list already used that phrase; repeating it
would let a reader join the two lines). Standard to hold: **if it later
turns out to have been the point, a reread of this chapter must find no
clue.**

**A systemic error worth remembering: first ON-PAGE appearance is not
first meeting.** I wrote `봄에 알았고` for Gitae — but EP7's own text
calls him someone the sisters slink into the back room to avoid *every
time he comes by*. They have known him for years. The same root produced
three more slips (the truck's starter, the passenger door, and how well
Dana knows the yard's fence — EP7 has `늘 담장 밖에서 구경만 했다 …
등하굣길의 오랜 놀이`). All corrected; a sweep of all fifty approved
chapters found no further instances. Registered as 선례대장 §0-A:
**this world existed before spring — do not date everything to it.**

Also corrected: I had banned EP33 sentence reuse so hard that I avoided
the NICKNAME too. **`어이, 조수` is a speech habit and must recur.**
Better still, let Dana notice the pattern rather than hide it —
`하지 마라, 그러다 어떻게 된다. 문장이 늘 그 순서였다` — which turns
repetition into lineage and dovetails with §0-A.

**Canon added off-page:** the repair shop's front-yard concrete is the
lid of the old rolling-stock depot's MATERIALS HATCH, with the hangar's
old heavy crane underneath (LOC-02 §2.2-B). Three existing facts already
pointed at it — the hangar is a converted depot, it has a large
industrial crane, and the front yard is a concrete working surface that
takes trucks — so nothing new had to be invented. It also retro-explains
why Yeongjin settled here: **the underneath came first, not the house.**
EP51 does not open it and does not say how anything got down there.

The hook is two numbers: `7번이 아니었다. / 5번이었다.`

EP52 「밀려오는 것」 locked in (57_EP052_승인완료, STANDARD chapter,
**S9 2/12 — rung two, FOOTING. She loses**). Five rounds of brief
correction came from the user before a word was drafted, and each one
made the chapter harder and better.

**The enemy switches targets, on the page.** It was NOT passing through
— it was walking toward the sluice gate, meaning INTO the city. Dana
steps into its line and it stops for one beat and then **turns**: the
belly turns first and the rest follows, the left edge arriving before
the right, and **the whole turn is visible because it is that wide**.
That is priority one giving way to priority two, shown without a word of
explanation. Dana's read stops at `저건 원래 청해로 들어가려던 거였다.
내가 앞에 서니까 나로 바꾼 거다.` → **`바꿀 수 있다는 게 무서웠다`**.

**Rung two is a floor, not a strength problem.** The user cut my
cleverness twice here. First: no tail-spike gimmick — **mass alone is
the method**, a big heavy thing coming on like a big heavy thing. The
contrast is anatomy, not technique: it lies **spread flat and low**
while she stands **narrow and tall on two feet**, so the same push moves
whoever is standing on less floor. That is EP47's `이족 하중은 두 발에
박히고 다족은 뜬다` seen from the other side — the mud made her feet
STICK, the mossy slab makes them **not catch**. The chapter's phrase for
it: **`밀리는 게 아니라 실려 가는 것에 가까웠다`**, and the self-own
`세게 딛는 만큼 발바닥이 바닥을 문질렀고, 문지르니까 더 갔다`.
EP48's slip-and-deflect fails outright: at twice her width, **the side
she would deflect toward also has the thing in it**.

**The kill in EP53 is the old draft's ground collapse, brought forward
by the user — but a wide-contact enemy does not just fall through.** The
old version shot an anchor into an underground car park and stirred; S9
has no anchor yet. So the collapse needs an INDUCER, and the inducer
turns out to be the same anatomy that lost her the fight: **a narrow
foot concentrates load on one point, which a broad flat thing can never
do.** Under the reclamation flats run drainage culverts, mostly open,
**some stretches decked over** — hollow underneath. She walks the enemy
onto a decked stretch and **breaks the deck with her own feet, by
stamping**, which is labour rather than technique. Then its low centre
of gravity, the thing that made it unpushable, is what keeps it from
climbing out.

**How she learns it is split along the trichotomy, deliberately.**
Reading terrain is Sua's domain, but combat comms are closed to her and
**EP38's one exception is worth keeping at exactly one**. So Sua hands
over a paper BEFORE the sortie — shallow here, firm there, and one line
reading `물 빠지는 데`, drawn darker because it was gone over several
times. It is a maintenance record (`물 표 만들다가 같이 그렸어`, sourced
from the repair invoices) and **she does not know it is a weapon**. Dana
skims it and thinks `물이 빠지든 말든 지금 알 바 아니었다`. In EP52 the
seed is planted and NOT understood: a foot breaks through and the sound
underneath is wrong — hollow, like a struck drum — and `들었는데 그게
다였다`, buried under irritation at the ground breaking. Sua supplies the
material; Dana assembles it in EP53. Note this is the mirror of EP49,
not a repeat: there Sua gave a value she did not know she gave, here she
knowingly drew something whose USE she does not know.

**A systemic leak, caught by the user's edit.** I wrote `봄에 문어형을
밀 때`; the user changed it to **`3월의 첫 괴수를 밀 때`**. Author-side
taxon labels must never reach the page — characters do not classify
these things — and the rule is simply that **the suffix `-형` makes it
author-only**, while using `가재`/`문어` as a plain likeness is fine. A
sweep found the same leak in three APPROVED chapters, seven places total
(EP9 ×2, EP10 ×4, EP48 ×1), all corrected with the reference swapped and
nothing else touched; the EP10 one sits in a military document so it
became `대상`. The reason it survived this long: the banned-term list had
only `성게형` and `농게형` in it. `check_draft.py` now carries
**`CREATURE_TAXA`, nineteen entries**, and the roster and that list must
be updated together. Record: 05_문체_상태_인계/Black_Titan_소급정정_
2026-08-13_개체명칭_v1.0.md.

Also fixed by the user: the city is called **청해** even inside Dana's
own narration; Yeongjin says `버텨야 한다`, not `버텨라`; the thing means
to **깔아뭉개다**, not to lay weight on her arms; and a paragraph of
retreat was added so the standoff visibly resets (`결국 아까 상황의
재현이다`).

EP53 「버틸 데」 locked in (58_EP053_승인완료, STANDARD chapter,
**S9 3/12 — the kill**). Continuous with EP52: it opens on `또 갔다.`
with no recap of any kind.

**The assembly is deliberately slow, because a fast one would make Dana
into Sua.** Six beats, in order: the hollow sound comes AGAIN → it is
merely IRRITATING, not a discovery (`지금 그럴 때가 아닌데`) → something
snags (`숙제 안 한 게 생각날 때랑 비슷했다`) → she gropes for it →
it arrives: the line on Sua's paper, **`물 빠지는 데`** → and she is
NOT sure (`말이 되는 것 같기만 했다`). Certainty comes afterwards for
this character, never before.

**The winning move is a reversal of a technique that failed.** EP48's
deflection was blocked in EP52 because the thing is twice her width;
here that failure flips into **흘릴 수 없으면 같이 간다** — she stops
resisting the push and only steers where she is pushed. The user's edit
tied it to EP23 「끌려가지 않는 법」: `팔 여덟 개짜리 괴수와 마찬가지다.
그때도 끌려가는 방향을 내가 정했다.` And it costs — steering sideways
means going backward too, two steps becoming four.

**The collapse inducer is her own anatomy, inverted.** A broad
flat-contact enemy will not fall through a deck by walking over it, so
the collapse has to be INDUCED, and with no anchor yet the only tool is
a **narrow foot concentrating load on one point — the exact property
that lost her EP52.** She stamps the deck of the drainage culvert while
being pushed along it, and refuses to count how many times (counting
would be calculation, and calculation is Sua's grammar). Then the
collapse runs in five stages so it does not read as luck: left side
drops → **the thing does not notice and keeps pushing** → its own push
drives it deeper → the whole width follows → and its low centre of
gravity, the reason it could not be shoved, is now the reason it cannot
climb out.

**Guard against reading the kill as growth.** One strike, on the belly
side that was never armoured — but `기술이 는 게 아니었다. 칠 자리가
나와 있었을 뿐이다` and `이겼다는 말이 안 나왔다`. Summer's mid-season
break needs her competence to stay unearned here.

**The user flagged that Yeongjin had become useless, and they were
right.** I had narrowed combat comms to "warnings and clock" and got an
adult who does nothing. New standing guard (`standing-guards.md` §2-B):
**he is a mechanic, not a strategist.** He CAN give technical advice
(machines, structure, materials, load), the body knowledge of decades of
handling things, observation support (the screen looks down; the cockpit
only looks forward), procedure when nothing can be confirmed, and plain
support — `물은 다시 빼면 된다`, which is a fact rather than comfort.
He CANNOT give tactics, infer the enemy's intent, make operational
calls, or supply the answer. When he does not know, he says why and then
hands the decision over: **`여기 도면은 나한테 없다.` → `네 발이
도면이다.` → `네가 안에 있다.`** Emotional support is his own kind and
**must not be laid on thick**. Dialogue went 15.6% → 19.1% and the
chapter is better for it.

**Paying Sua, inverted from EP49.** There the debt was spoken and Sua
did not understand it; here **nothing is said and Sua understands.**
Dana marks the paper — a dot on the thickened line, and beside it
**`소리 다름.`**, in handwriting so much bigger and more crooked than
Sua's that it runs past the column. Sua looks at the dot, looks at the
writing, **looks twice because it is crooked**, then folds the sheet
under her inspection form. `아무 말도 안 했다. 그건 이 집 사람들이 다
할 줄 아는 일이었다.` This is the first time Dana's hand appears in
Sua's records.

Also corrected by the user: **왼팔** does the finishing blow (which now
agrees with the anchor going on the LEFT forearm), and `봄이었으면 여러
번 쳤을 것이다` became `전에는 여러 번 쳤다` — the beating-until-it-
breaks was EP45, which is summer, not spring. And the return had to move
to the HANGAR: canon (선례대장 §2) says they meet her there, so Sua
belongs at the control station with the inspection sheet, not at the
table indoors.

The cost is the point: the drainage culvert is destroyed, so **the water
does not drain.** Knee-deep becomes mid-shin and keeps rising.
`이런 건 이기고 나서 알게 된다.`

EP54 「값」 locked in (59_EP054_승인완료, STANDARD chapter,
**S9 4/12 — the bill comes in**). No fighting. Last night's win is
invoiced this morning and the whole day is one payment schedule.

**A setting correction from the user first, because it shapes the
chapter.** There is no farmland in Cheonghae — it is a drowned city and
there is no reason to put rice fields outside the flood wall. So the
reclaimed flat holds **warehouses, storage yards, the sluice control
building and the pump house: a place people WORK, not live**. I had
written `안에는 논이 있고` into EP52's approved text; that is corrected
to `안에는 창고가 있고 야적장이 있고`, and the consequences are all
good ones — **nobody was hurt**, which is exactly why no one blames her
yet; the damage is **goods and equipment**, which is why work arrives at
the repair shop; and Miran, who does fisheries-association business, has
gear in one of those warehouses.

**The water gets six different faces, one per scene**: three trucks of
men heading out at dawn → the classroom turning it into talk → **that
same ground wedged in the machine's sole** → a line in Sua's table →
soaked equipment on the counter → one more line in the ledger. Dana
never apologises and never says the word guilt: `미안한 건 아니었다`
(the sluice would have gone) / `그런데 안 미안한 것도 아니었다` /
**`자기가 한 일인데 자기가 못 치우는 일이 됐다`**.

**The city's fifth stage is the discovery of cost, and it arrives as a
joke.** `이겼대. 근데 거기 창고들 다 잠겼대.` → **`그럼 이긴 거야,
진 거야?`** — a kid says it to be funny and several kids laugh. No
accusation, no complaint; **S10's school damage is where that belongs**
and spending it here would weaken it. Dana does not laugh, and cannot
answer: `이겼다고 말하고 나면 물이 안 빠지는 건 어떻게 설명하나. 이긴
사람이 부순 건데.`

**Washing becomes a confession.** EP49 did ankles and shins; this time
it is **soles and toe joints**, because she spent a night stamping
concrete. Blocks you carry with both arms, rebar as thick as a forearm
with its **end mashed flat** — `뭉개졌다는 건 밟혔다는 뜻이다` — and
she reaches into the tread groove, which is a gap her whole forearm
enters. `이건 내가 밟아서 깬 거다. 내가 깨고, 내가 밟고, 내가 여기
끼워서 걸어 온 거다. 지금은 내가 빼고 있다.`

**EP50's reserved blank box is opened: its heading is `남은 것`.**
Sua did not know what would be left — `몰랐어. 그냥 생길 것 같았어.` —
and she was right, because **in spring nothing was ever left**
(everything dissolved, no salvage) and summer has started leaving
things. First entry: `배수로. 물 안 빠짐.` Nothing about when or who or
how much. And the naming gate stops being an authorial rule and becomes
the character's own position:

    "그냥 아무렇게나 붙이면 되잖아."
    "붙이면 그렇게 부르게 돼."

**Miran returns after a twenty-chapter gap** with three reminders only
(yellow rubber gloves straight from the market / fisheries-association
business, which is why the flooding is not somebody else's problem /
the repair-shop relationship, `박사님`). Her sentence breaks where the
anger has nowhere to go — `근데 물이 안 빠져서, 그게.` — and she gives
Dana worry disguised as nagging. The user also trimmed her address for
Dana: `수리점 손녀` at the market, **`손녀`** inside the repair shop —
**what the location already says gets dropped from the name.**

Yeongjin adds one line to the procurement list, and it is not an answer:
**`발에 뭐라도.`** He does not know either, so it stays as vague as the
rest. (Author-only irony, never on the page: the answer will come from
the ARM.) Dana sees it and does not ask.

Other user fixes: `저것은 녹아내렸고` (dissolution had been in the delta
but never on the page), `밀기만 함` → **`밀고 깔아뭉갬`** to match EP52,
the classroom scene moved to the SCHOOL GATE so the chatter walks in
with them, and `손전등을 받아 들고` → **`손전등을 맡기고`** — a man who
came to get something repaired does not carry it back out.

Next: **EP55 「붙은 것들」** — the barnacles, and **it does not start
with an alarm.** The buoys were quiet and the ledger has nothing; a
person saw it first. EP54's hook is the door: `본 사람이 오늘 안
나왔어요. 들은 사람이 말한 거라 확실한 건 아니고.` Cone shells clamped
to the flood wall's outer face and the sluice seams, eating the
concrete, not attacking and not moving. Fingers do not fit, and hitting
them **breaks the wall first** — rung three, TENSION. Daylight, right up
against the city, so witnessing reaches stage three (people see the
SHAPE) and public feeling crosses into **unease**. Hook: **nobody knows
how long they had been there.**

**S9 「고철의 재간」 outline v1.0 is `LEVEL4_PASS`** (2026-08-13),
at `02_여름편_기획/Black_Titan_S9_EP051-062_화별개요_v1.0_승인.md`.
EP51–61, eleven chapters, 6/19 (Sun) – 6/28 (Tue). The next operation is
**EP51 「인양장」's chapter brief (Gate C)**.

**The arc's spine is a bare-hands ladder that was already latent in the
L3 skeleton.** What Dana lacks is not one thing but three, and each has
its own bodily sensation:

| rung | opponent | what is missing | how the anchor solves it |
| --- | --- | --- | --- |
| 1 (already set, EP44–45) | urchin | **reach** | **launch** (rocket drive) |
| 2 (EP52–53) | horseshoe crab | **footing** — she gets PUSHED | **bite in and hold** (what an anchor is for) |
| 3 (EP55–56) | barnacles | **tension** — nothing to pry with | **hook and haul** (the chain) |

One object closes all three, so the anchor reads as a SUM, not an
invention. And EP50's `버티는 시간` (arms out, ten then eight then six)
pays off in EP61: **the arm she raised to hold with is the arm that gets
longer.**

**Anchor modes — the user corrected a mistake here, and the correction
improved the design.** Claw is NOT a grapple; it is a **striking aid, a
knuckle**, continuing EP48's brawling line. Hooking and hauling works
with the anchor simply held in the hand. Therefore **rocket drive comes
first**, because reach is the only rung it solves and without it the
best anchor in the world still only works at arm's length. S9 = rocket
mode only; **claw does not appear and is not mentioned.**

**Enemy motive, formalised (author-only, user 2026-08-13).** Priority
one is **searching for their own kind**; priority two is **destroying
the obstacle** (Black Titan), and two only fires when it blocks one.
Extending the search past the flood wall means getting over the wall —
but moving loudly triggers priority two. So they **test a quiet
excavation**: the barnacles. This shows the enemy LEARNING without
raising its intelligence — it is trial and error, and **this trial
fails** (the Titan comes out anyway). They take that result too, which
is how S10's springtail type crossing into the school connects.
On the page: the words purpose, learning and test never appear. Only
three assembling materials — it made no sound, nobody knows how long it
had been there, and of all places it is the wall.

Three consequences worth holding: the barnacle event is the **first
failure of the observation system** (too quiet for the buoys — a PERSON
sees it first, and Sua's observation sheet gets a line it cannot fill);
it is the **first fight where `이겼다` does not attach** (they get them
all off, but the wall is already eaten, and the trial was theirs, not
hers); and public feeling crosses from worry into **unease**, because a
flood wall corroding is a different species of fear from a wave.

Other locks: naming `아이언 앵커` waits for EP62 and stays a family-
internal name; the isopod fight is a **clear defeat in EP60** — strength
left over, no voluntary withdrawal, a series first — before the EP61
debut; the Hyunseo envelope shows **its exterior only** (postmark,
stamp, addressee — no sender, no contents); sentinel rung 2 is two lines
of intranet news in EP57; Seongho's rematch stays unpaid into S10.
Author-only sealing is unchanged: culture medium, Hyunseo's equipment,
the anchor's surface.

## Current serial state

The authoritative snapshot is **SNAP-050**
(05_문체_상태_인계/Black_Titan_SNAP-050_EP050후_v1.0.yaml). Read that file for
the live state; the list below is the EP2 baseline kept only as a record of
what the early-spring disclosure order established.

At the end of EP2:

- Dana and Sua have seen the 52 m Black Titan.
- Dana, Sua, and Young-jin know the internal names 블랙 타이탄 and 타이탄.
  Outside family characters, residents, and the military do not.
- Young-jin's military disaster-response prototype account is a family cover
  story, not narrator-certified truth.
- EP2 first revealed that the VR session five months earlier collected Dana's
  EMG and movement-intent calibration data.
- The timeline of the VR session and Dana's worsening vision is juxtaposed,
  but direct causation is not disclosed.
- Sleep-learning and repeated game-like training were revealed as control
  preparation.
- Dana chose to sortie after seeing the projected route toward Cheonghaenam
  Elementary School and Gurae-dong.
- Dana raised the activation switch. Black Titan has not yet moved in official
  canon.
- Dana–Young-jin is STRAINED_BY_REVEALED_DECEPTION.
- Dana has no new injury or acute neurological symptom.

(EP3 onward have since been approved; see SNAP-050 for what is true now.)

## Active constraints

- Spring monsters search for and attempt to recover the first-giant lineage.
  They do not recognize Black Titan as kin or as the recovery target.
- With Dana aboard, Black Titan's second-lineage field cancels the search wave
  around her. Keep this author-only in early spring.
- Basic limb and torso movement uses EMG and movement intent with about 0.5 s
  delay. It is not full-body motion capture.
- Dana may naturally grip the control handles as posture support. The handles
  do not cause basic Titan movement. No external weapon is connected in spring.
- Normal force feedback returns attenuated contact, pressure, joint load, and
  posture while suppressing pain. Pain leakage under emotional escalation and
  cumulative neurological injury are separate phenomena.
- Black Titan is unarmed in early spring. Do not introduce the Iron Anchor.
- The reverse field is invisible and must not be narrated at all before autumn.
  Show only the results: shells leave no mark, impact still pushes the body,
  and Black Titan can transfer real force. Never name or explain the cause.
- Eye glow is the only visible lineage marker. Kaiju green, Black Titan orange,
  White Sentinel blue slit. Sightless units such as the S7 chiton type have none.
- Black Titan has footfall and armor sounds only — no motor, hydraulic, or
  biological sound. The kaiju may make a metal-scraping sound for threat or death.
- Giant-mass action never uses speed, agility, or leaping. Fast is relative
  between two giants only. Build scale from inertia, shockwave, displaced water,
  and sound arriving a beat late — the last one only from external viewpoints,
  never from inside the cockpit. See narration-style-card §5.
- Do not damage the school building in spring.
- Keep Dana's spring neurological signals deniable; no objective collapse or
  confirmed diagnosis.
- Sua may offer one decisive observation in S7, but her control suitability,
  synchronization, and first sortie remain unproven until summer.
- Hye-jeong leads with concern, not interrogation. Investigation, tailing, and
  physical evidence belong to summer.
- Dana and Seong-ho are mutually antagonistic athletic rivals because they are
  alike. Never frame them as future romance.
- EP1 cold-open sentences must not be repeated in EP3.
- Old-manuscript hangar, first-sortie, weapon, institution, and military
  pursuit events remain non-canon.

## Bundled reference policy

The bundled references are portable summaries and style aids. Exact current
workspace files override them when the versions differ.

- s1-gateb-approved.md through s5-gateb-approved.md may be older than the
  current exact Level 4 files listed above.
- naming-knowledge-g0-approved.md, search-lineage-g0-approved.md, and
  dana-seongho-rivalry.md remain active constraint summaries.
- Before drafting, load the exact approved brief, latest state snapshot, two or
  three recent deltas, and only the voice cards for appearing characters.

If the exact current canon or state file is unavailable, ask the user to attach
or identify it. Never reconstruct missing canon from summaries or memory.

## Style corpus

- Old complete prose: chapters 1–43 only
- June-file chapters 44–50: exclude because they are outlines or notes
- 3월re prologue–chapter 6: later revision sample
- Approved baseline: C-style adapter with two to four short
  function-matched examples
- narration-style-card.md and voice-cards-spring.md: STYLE_ONLY

Retrieve style by scene function, never by shared plot content. Approval of
cadence or voice never canonizes the event carrying the example.

## Production process

Use production-pipeline.md v1.2:

canon → full plot → season → month → episode outline → chapter brief → content
lock and style retrieval → draft and edit → Gate D approval → delta and Gate E
state update.

Require explicit user approval before applying generated prose or its delta to
official state. Preserve unapproved prose as NONCANON_EXPERIMENT.

## S9 — EP55 through EP57 (added 2026-08-14)

**The user redesigned the EP55/56 pair mid-arc, and the redesign is the
important thing to carry forward.** EP55 was written once as a combat chapter
and discarded. The objection: nothing that has appeared so far looks like
this, so **nobody would call it a kaiju**, and a thing stuck to critical
infrastructure means **the city investigates first**. So the pair split into
an investigation chapter and a combat chapter.

The creature was relocked at the same time. It is **four or five wide flat
plates, each the size of a bus and thin**, with a **lid** on top that opens
slowly so a **rake** of feeler-limbs can sweep the water and withdraw. Rhythm,
and **no sound at all** — every sound in both chapters comes from the human
side.

### EP55 「모르는 것」 (60_EP055_승인완료, STANDARD, S9 5/12 — no combat, no sortie)

The word `괴수` appears twice: once as a negation in scene 1 (`셋 중에 괴수라는
말은 없었다`) and once at dinner when Sua finally says it. The city calls it a
`부착물` and treats it as a **structural-safety** matter. City hall canvasses
the alleys and stops at the repair shop on the way — **not because Yeongjin is
an authority**, just because a neighbour mentioned it. He shows three days of
flat buoy traces and says there is nothing; they write one line and leave. The
buoy principle gets its first page statement: **it catches things that pass**,
so `붙어 있는 건 지나가지 않는다`, and the harbour log proves it — `배는 잡히고
저건 안 잡혔다`.

**The self-blame is deliberately withheld until after the reveal.** In the
morning the blank column means nothing. In the evening the same line means
**`아무것도 못 봤다는 뜻`**. One fact, read twice, inside one chapter.

**The reveal is an accident, not a deduction.** A lid opens, the rake comes
out, and an inspector gets his arm wound up and dragged in. He lives. **How
they got him out is hidden** — all Dana knows is that it took a long time.
That withholding is paid off in EP56.

Two canon re-confirmations landed here: the buoy terminal is **one unit in the
shop** (EP29) showing three traces, not three screens, and the buoys are
**7, 5 and 2**, with 2 closest to the flood wall (EP30).

### EP56 「붙은 것들」 (61_EP056_승인완료, KEY chapter, S9 6/12 — sub-arc closes)

Morning: four sources are checked against each other, split by the trichotomy
— Dana's green (she saw it and said nothing), the **previous ledger volume**,
Sua's **creature table** (she built it, backfilled earlier entries from memory,
and `전부 녹색이에요`), and a **military classification notice, two sentences**,
arriving as `어딘가의 거인에게 보라는 듯 정보만 뿌렸다`. Then the name changes
— **and the classification means nobody is coming.** `부착물은 시청 일이고
괴수는 이쪽 일이다.`

**Threat and difficulty are deliberately separated** (user's call). The rake is
lethal to a person and **negligible to the machine**. What that produces is not
danger but recognition: `저건 사람을 죽일 수 있고 나는 안 죽는다`, one line, no
resolve speech. Pulling tightens it and **pushing in releases it**, learned by
poking rather than by being in trouble — and that is when yesterday becomes
legible. `알아도 말할 데가 없었다.`

Rung three of the ladder is **nothing to hook**: fingers do not fit, the palm
slides off a flat plate, hammering **breaks the wall first**. `셋 다 안 됐는데
셋이 다 다른 이유로 안 됐다.`

**The bottle-opener is the arc's grammar in miniature** (user's design). The
first plate takes forever and tears the wall out with it — and leaves a thin,
hard plate in her hand. Yeongjin closes it in three words plus one: **`손에 든
거 다시 봐. 그게 뭐로 보이나.`** When you have no tool, you use what you just
tore off. It goes in where fingers would not, twists, catches, and **the wall
does not break.** Rehearsal for EP61. The ladder survives because a
bottle-opener **pushes** rather than pulls and works **one at a time**.

**Cleanup is half the labour, and it is canon now.** Dropped plates drift off
and reattach, so every plate is carried to dry ground. Then each is pressed
until the soft underside gives — **with no resistance at all, unlike tearing
them off** — and what falls into the sea **dissolves dark red**. This locks the
flip side of EP5's report (`사체는 착수 후 붉게 풀려 확산·소실`): **they only
dissolve once dead**, which is why they must be crushed.

Sighting tier three completes (photo → video → **in daylight, under 200 metres,
with their own eyes**) and public feeling crosses into **unease**. Still no
cockpit, no pilot, no blame.

**The chapter refuses `이겼다`.** Every plate is off and the wall is still
eaten; **the place she worked before she knew and the places she worked after
sit side by side on the wall.** `분하려면 상대가 있어야 하는데 저건 끝까지
이쪽을 안 봤다.`

**The ledger closes the arc's spine.** Yeongjin writes `떼어낼 것이 없다.` under
`버틸 것이 없다.`, looks at the two, and then **inserts a line above them** —
`닿을 것이 없다.`, the June one he never wrote down. Three lines in a row, and
in the margin **`이건 관측에 안 걸렸다.`** He is the one who put them side by
side; that act is the seed of EP61. Dana watches and does not ask.

### EP57 「우편물」 (62_EP057_승인완료, STANDARD, S9 7/12 — no combat)

Three things arrive and **nobody explains any of them**: a truck of scrap, a
handwritten envelope, and a cleared corner of the hangar. The Level 6 lock
carried a **mandatory re-read audit** and the Gate-D sheet records all three
passes.

**The anchor** appears **once**, third in a list of six, mid-paragraph. No
modifier, no pause, no separate handling. The weight of the passage is pushed
onto the **pulleys** instead — they get the dialogue and get spun. Later the
scrap is half gone and the trail stops: `긁힌 자국은 마당 안쪽으로 갔다가
거기서 끊겼다`.

**The yard crane got registered as canon here** (LOC-05 **v3.1**) after the
user pointed out it existed in the settings but had been dropped from the
spatial bible. A **post-mounted jib crane** — how a neighbourhood shop receives
boat engines at all, which is *why Yeongjin has been able to do this work*, with
controls **one hand can work**. Author-only: its swing radius covers the
**materials hatch**, so the means of lowering heavy cargo underground has been
standing in the yard the whole time. On the page it is only a shop fixture.

**The envelope** stops at the outside: handwriting, smudged postmark, faded
stamp, `도영진` as addressee. The sender's line is not concealed by the
narration — **Dana has no reason to turn it over**, so she doesn't. `현서`
never appears.

**Yeongjin's reaction is one gesture** — he wipes his greasy hands twice and
puts it in the **top cabinet shelf** instead of the bench. (He does **not** wear
glasses; that is Dana. The brief listed a glasses gesture and was corrected.)
**And that gesture is why nobody asks:** `손을 두 번 닦고 받는 걸 봤으면
그다음은 안 묻게 된다.` The house's not-asking stopped being a rule and became
an observation.

**The workshop is built without a single prohibition.** `자리 좀 만든다` /
`넓게 쓰려고` / `저쪽이 어둡잖아` — all true. What happens is that the spot
where Dana sat after training now has boxes on it.

**A correction worth carrying:** the `남은 것` column is a record of **what the
win left behind**, not of salvage. EP54's first line was `배수로. 물 안 빠짐.`,
so EP57's second is `방재벽 바깥면. 삭음.` The draft had Sua hesitating because
nothing physical remained; the user caught it and the scene became her writing
the line. `이긴 것마다 한 줄씩이었다.` It rhymes with the ledger's three lines
and **nobody connects them.**

**Speech-level canon settled here** (from user edits): Yeongjin speaks to Gitae
in **하게체** (`도르래가 많군.` / `쓸 만한가?` / `점심 먹고 하게.`), dropping to
해라체 only in short replies as in EP51; and **Sua uses 반말 to Dana** — her
존댓말 is for Yeongjin only, so a scene with both must split by addressee.

Sentinel tier two sits as **two lines in the corner of a classroom scrapbook**
with nothing written under them, surrounded by other clippings. No name, no
country, no reaction.

Hook: **the light does not go out.** The sliding door is open a hand's width
and the light comes through it **from the shop side** — the reverse of EP7. The
iron door at the end of the passage is open, one regular sound comes up, and she
does not go down: `급한 걸 하는 사람한테는 안 묻는 게 낫다.`

Next: **EP58 「안 맞는다」** — the prototype, and its first failure.

### Working note

`08_CODEX_이관/write-black-titan-serial/` is the **source of truth**; the
`.claude/skills/` copy is derived and overwritten wholesale by `sync-skill.ps1`.
Edit the CODEX copy, then sync — editing the installed copy loses the change.

## S9 — EP58 and the arc compression (added 2026-08-14)

**The user restructured the back half of the arc before EP58 was drafted, and
the reasoning is worth keeping.** EP58 (prototype fails) and EP59 (coaching,
success) were going to be two hangar chapters back to back, right after two
non-combat chapters — four of six with no action. Merging them was the obvious
fix but would have cost the hook `내일 다시 한다`, which is not a sign-off but
**the failure surviving overnight**, tied back to EP50.

What the user chose instead: **the enemy arrives on that next day.** EP58 keeps
its failure and its hook; EP59 is that morning, going out with a weapon that
does not work; EP60 is the coaching line landing **mid-fight**. The arc drops
from 12 chapters to 11 (EP51–61), the naming beat moves to EP61, and two
separate defeats (prototype failure + a later loss) collapse into one
escalation.

Then a second correction: **EP59 does not withdraw.** A fast creature heading
for the city cannot be left for tomorrow — that reads as leisure. EP59 ends
**mid-crisis** and EP60 resumes the same engagement, no time gap, never back to
the hangar. That also changed what losing means. Not `defeated and retreated`
but **`it won't fight you`**: block it and it goes around, chase it and you
can't keep up. And it makes the chokepoint in EP60 stop being a tactic — the
buildings are **what it has to pass to reach the city.**

### The rig (BT-01A, v0.1 → v0.3 across one day)

Locked from a reference image plus three follow-ups. **Left-forearm launcher;
a two-fluke anchor held in front of it; a chain over the shoulder to a
cover-plated winch backpack.** Then: **cold launch, then rocket ignition** —
nozzles beside the shank near the head. Then: **controls are three switches on
the stick** — lock / fire / rewind. No angle, no power setting, **no sights at
all.**

That two-stage launch is the single most load-bearing detail in the arc. It
gives EP58 its physics (`던진 건 나가면서 느려진다 … 이건 반대였다` — it leaves
the tube weak, *falls*, then lights up and accelerates, so the hand cannot know
where it will go), it explains why Sua's perfectly correct trajectory drawing
still fails (`불 붙는 데가 매번 달라` — the ignition point is in the hand, and
that cannot be drawn), and it makes EP60's `왼팔이 길어진다고 생각해` **the only
possible operating method rather than a metaphor.**

Mounting was upgraded to **construction scale** on user note — overhead crane,
chain block, platform, **two hours** — which then explains why nothing is
removed in the field: she carries it home on her back.

### EP58 「안 맞는다」 (63_EP058_승인완료, STANDARD, S9 8/11 — no combat)

Monday. Seong-ho asks a **third time** about the hundred metres and Dana cannot
name a date, because she cannot name the reason. **Ye-jin steps in and defends
her with a reason that is false** (the city inspectors at the shop). Seong-ho
reads cowardice, Ye-jin reads family trouble, **both are wrong and neither can
be corrected** — `고쳐 주려면 진짜를 말해야 하고, 진짜는 말할 수 있는 게
아니다.` Ye-jin returns after eight chapters and does exactly what her card
says: she is the one character whose sentences get longer in a conflict.

The prototype is simply **there** when she gets home — no process, no drawings,
no parts history, same withholding as EP57's iron door. Nine shots at a
collapsed warehouse wall, none of them land. Sua watches **from the shop, over
the screen** (an earlier draft had a ten-year-old alone in a restricted zone at
night — user caught it) and holds her drawing up to the camera.

**No one turns the problem into a sentence.** `셋 다 각자 뭐가 문제인지
어렴풋이 아는 것 같았다. 그런데 아무도 그걸 말로 만들지 않았다.` That silence
is what EP60's one line breaks.

**Sua's four prohibitions were set here** (user): **잘난척, 남 탓, 변명, 말
끊기.** The draft had `내 그림이 틀린 게 아니라…`, which read as an excuse or
as blaming Dana/the equipment; it became `아냐. 내 그림이 틀렸나 봐.` — *when
her calculation was right and the result still isn't, she looks at herself
first* — with Dana recognising it: `언니 탓도 장비 탓도 할 수 없는 게 수아
성격이라는 걸 알기에 단아는 잠자코 들었다.` Registered in standing-guards, the
precedent ledger, and memory.

**A dating error was caught by the user:** the arm-holding training started in
**EP50, the night of 6/18**, not in spring. EP58 is 6/27 — **nine days.** The
correction improved the beat, because EP50's own numbers could be carried over
(`두 번째가 여덟, 세 번째는 여섯`) and nine days of visible progress being
useless today stings more than a vague season of it. `버티는 건 되는데 보내는
게 안 된다.` No consolation, no `그래도 헛되지 않았다`.

**Tooling:** `check_translationese` F-5 (`-적 N` chains) was matching `표적`
because the regex `[가-힣]적` swallowed the stem. Fixed with a stem-exclusion
lookahead and regression-tested across all 57 approved chapters. **Edit the
08_CODEX copy** — the `.claude/skills/` one is overwritten by sync.

Next: **EP59 「보이지 않는다」** — going out with a weapon that doesn't work.

## S9 — EP59 (added 2026-08-14)

**The first chapter that does not end.** No withdrawal, no resolve, no
diagnosis — it stops mid-engagement and EP60 resumes with zero elapsed time.
The Level 6 lock carried a **mandatory last-three-paragraphs re-read** for
exactly those three failure modes, and the state files follow suit: SNAP-059
has an `engagement_open` block recording the creature's position, the machine's
accumulated scrapes, and the half-paid-out chain, because **this snapshot is a
photograph taken during a fight.**

**The isopod's speed is mass-bearing** (user's correction). Half the machine's
height still means tens of metres, so it must not flit. It passes and **the wave
arrives long after**; it turns and **the water stands up like a wall, the
exposed roadbed tears in an arc, and the sound comes afterwards.** `가벼워서
빠른 게 아니었다.` And crucially: **paying that turning cost still leaves it
faster** — `값을 치르는 쪽이 값을 안 치르는 쪽보다 빨랐다.` That physics is
what makes EP60's chokepoint necessary rather than clever: **between buildings
the turning cost goes up, so it can only go straight.**

**`안 보인다` was redefined**: not that the form is invisible but that
**reaction cannot keep up.** `눈으로 따라가는데 눈이 뒤에 있었다` / **`본 게
늘 지나간 것이었다.`**

**The user's key note: the enemy's behaviour must be legible every moment.**
The first draft had it streak past and then somehow be blocked again, which
does not parse. Fixed by giving it a pattern — **it does not leave the area; it
passes, loops wide, and comes back**, so the block is possible. Fixing that
also exposed a contradiction: `이쪽을 부수려고 하지 않는다` conflicted with the
outline's second-purpose canon (`타이탄이 막아서면 2목적으로 이행한다`). Both
resolved by redefining the attack: **it does not come head-on; it turns off the
centreline, comes in from the side, and scrapes as it goes.** That *is* its
fight, because **it knows that stopping means losing.**

The defeat therefore has a new texture. Never pushed back, never solidly hit —
**only the scrape marks accumulate** (shoulder, waist, left calf) — and
`힘이 남았는데 쓸 데가 없었다.` The two-stage launch is worse in combat than on
the range: the silent coast phase is where the target relocates, so all three
shots hit empty water.

**And the enemy calculates.** On the sixth pass it **does not close the loop** —
it straightens out and leaves for the city, having worked out in six tries that
this thing cannot catch it. First time in the series an enemy has withdrawn by
reasoning rather than by being driven off or dying.

EP9 is recalled from the other side (user note): the same drained streets, the
same puddles — `웅덩이는 그때랑 똑같았다` — but **no birds.** Back then there
was room to walk and apologise to them.

**Tooling, two fixes.** `집게형` was missing from `CREATURE_TAXA` and slipped
into a draft. And the regression run flagged `군부형`/`성게형` in EP38/EP44,
which turned out to be the documents' own **front-matter change-log rows**, not
prose — so `read_text` now strips everything before the first standalone `---`.
Side effect: **length counts are ~230 chars more accurate** (the header table no
longer counts). All 58 approved chapters re-checked clean.

Next: **EP60 「길목」** — same fight, same water, and the coaching line lands
mid-engagement.

## S9 — EP60 (added 2026-08-14)

**The arc's spine closes here.** Launch (distance), plant-and-hold (support),
hook-and-pull (tension) all land in one action — **and nobody counts them.**
No `three became one` sentence exists; the reader joins it.

**The answer was to stop chasing.** The isopod **pushes** with its legs, so deep
water costs it — it rides the shallow line of the old road ridges and therefore
**goes around.** The machine is slower but can walk chest-deep in a straight
line. **The fast one detours and the slow one cuts across.** Yeongjin reads the
terrain from the military's broadcast survey (first dropped EP30 on 5/12,
routine since EP33) — **and only the terrain.** His sentence breaks at
`너한테는…` because Dana has already turned toward the water. The decision is
hers.

**The trap:** anchor into one wall, and **the machine is the other post** —
`기둥이 둘 필요한데 하나밖에 없으면 나머지 하나를 자기가 하면 된다`. Chain
strung at **leg height**, because several legs catching at once takes the whole
body over.

**The rubber band** (user's spec): the hold is **1–2 seconds and only feels
long.** Sensations stack in short sentences — foot slides, arm extends, shoulder
pulls back, neck drags forward, wall comes to the face — then the reversal is
**one sentence**: `뒤집혔다.` And immediately after, the gap: **`짧았다. 걸리고
뒤집힐 때까지가 짧았다. 길게 느껴진 것하고 안 맞았다.`** That is also what makes
EP50's nine days of arm-holding honest — it was trained long and spent in an
instant, and **the causal link is never stated**; the text stops at `팔이 안
떨렸다`.

**Terrain blunts the weapon.** Unbeatable in the open, helpless in a corridor —
`달라진 건 저것도 이쪽도 아니고 서 있는 자리였다`. The hard roadbed that
favoured the many-legged thing in EP59 is what her feet bite into here; same
property, other face, same grammar as EP4's mudflat and EP53's narrow footprint.

**Two things the user corrected that improved the chapter.** First, the idea has
to arrive *before* the shooting — `여기서 발을 걸면 넘어지지 않을까` comes
suddenly, because the slack chain is hanging in view; without it, scene 4 starts
with an unexplained shot. Second, **ruins leave no bill**: this is a drowned
district with nobody to repair it, so the EP54-style invoice does not appear —
**`처음으로 부수고도 값이 안 나왔다`**, which lands right beside the emotional
close.

**The body changed, not the arsenal.** `팔이 하나 더 생긴 게 아니라 팔이 길어진
거였다.` When it caught, what got pulled was the arm, not the chain — and she
**never once thought about letting go**. Tracked on FS-001 but explicitly **not
a symptom**: this is the price of acceptance. And the victory register now has
three steps — hands shaking (first win, spring), hollowness (the flood wall),
and today: **`아무것도 아니었다. 아무것도 아닌 게 제일 이상했다.`**

Yeongjin offers no congratulation. `그런 말이 나왔으면 오히려 이상했을 것이다.`

Next: **EP61 「고철의 값」** — the arc closer. Settling up with Gitae, a new row
in Sua's table, and **the thing finally gets a name inside the family.**

## S9 closed — EP61 and the arc (added 2026-08-14)

**EP61 「고철의 값」** settles up, writes it down, and names it. No combat.

**Payment goes the way that leaves nothing on paper** — Yeongjin will fix
Gitae's winch and generator next week instead of paying cash, so the sheet ends
up holding only a weight and a date. Gitae, who has every reason to ask what all
that scrap became, doesn't: `쓸 데가 있었으니까 썼지` and that's the end of it.
He is the sort who points out what needs pointing out and doesn't ask the rest.

**The absence has consequences.** Yeongjin told the homeroom teacher she was
sick; the group chat is full of Hyejeong from before first period. And buried in
it, EP32's promise comes back: `아프면 아프다고 하기로 했잖아.` **Dana did not
break it** — she wasn't sick, so there was nothing to say first. But from
Hyejeong's side it is broken, **and it cannot be corrected.** That makes three:
Seong-ho reads cowardice, Ye-jin reads family trouble, Hyejeong reads a broken
promise. `셋 다 틀렸다.` Hyejeong's reply is the worst of it — `그럼 됐어` —
because **`화를 냈으면 차라리 나았을 것이다. 화를 내면 미안한 게 뭔지가
정해진다.`**

**The name arrives because a column needs filling.** Sua rules a new row into
the machine table — the first new row since spring — and can't label it: writing
`닻` would not distinguish it from the anchor that sat in the yard. So **Dana
pulls out her phone and looks up 쇠 and 닻**. `아이언 앵커.` It is flatly
literal and **everyone knows it isn't good**: Yeongjin never comments on such
things, Sua just writes down what her sister decided, and Dana knows perfectly
well — she simply can't think of anything else, and Sua is waiting with the
pencil. **Nobody says a word about it.** That silence is the household, and it
is where the chapter's humour lives. `적혔으니까 그게 이름이 됐다.` It is a
**family-internal name only** — `밖에 나가서 쓸 이름은 아니었다.` EP54's
`붙이면 그렇게 부르게 돼` comes back from the other side: then it was a reason
*not* to name; today they named.

**Sua sees the change first, from the table.** `봄에 온 것들은 다 타이탄을
잡아가려고 했는데 요즘은 전혀 안 그래` — spines, then trying to break an arm,
then crushing, and now **not even engaging.** `수아는 표를 보다가 그런 걸
알아챈다. 단아는 그 안에 있었는데도 몰랐다.` The trichotomy lands one more time
at the arc's close, and **no reason and no countermeasure carry into S10.**

**The `남은 것` column did not grow for the first time** — `폐허니까.`

**The arc is not summarised.** Only objects: the chain from the salvage yard,
what came on Thursday's truck, what sat in the yard for days, the weekends when
the light stayed on. **`만든 게 아니라 모은 거였다.`** And the close is a body,
not an arsenal: `없어지면 그다음에는 그게 그냥 팔이 된다` — **`그게 좋은 건지는
잘 모르겠다.`**

### Arc-level canon carried into S10

Rig spec (BT-01A v0.3), the three-rung ladder and its single-action resolution,
the trap physics and the rubber band, **Sua's four prohibitions**, **Yeongjin
wears no glasses**, 하게체 to Gitae, **Sua speaks 반말 to Dana** (this leaked
repeatedly — check it in every mixed scene), **Sua's station is the hangar
screen**, the military **broadcasts rather than sends**, `남은 것` as a
lingering-damage column with a ruins exception, and the naming gate now open
family-internally only.

### Working notes

- `08_CODEX_이관/write-black-titan-serial/` is the **source of truth**; the
  `.claude/skills/` copy is overwritten by `sync-skill.ps1`. Edit CODEX, then sync.
- Tool fixes made during S9: `집게형` added to `CREATURE_TAXA`; front-matter
  tables excluded from body checks (`strip_front_matter`, ~230 chars more
  accurate); `check_translationese` F-5 no longer false-positives on `표적`.

Next: **S10 Level 4** — the outline does not exist yet.

## Calendar correction v1.0 (added 2026-08-15)

The EP41–61 consistency audit that followed S9's close found the work was
running **two calendars**. Weekday-stamped chapters checked against the real
2050 calendar: spring's 23 matched exactly, summer's 21 were **all off by
exactly −2 days**. The split is EP40 (5/18 Wed, correct) → EP41.

Worse, **EP41 contradicted itself on the page**: it opens `6월 첫 월요일`,
its ledger scene writes `6월 2일`, and SNAP-041 called it Tuesday. The brief
had said 6/1 Monday and the draft said 6/2; nobody reconciled them.

**Resolution (user-approved): unify on the real 2050 calendar.** Every summer
date shifts **+5 days**; since −2 ≡ +5 (mod 7), **not one weekday label
changes** — Friday's recital, the weekend build, the Tuesday absence all hold.
**Graduation-day assembly moves 7/15 → 7/22 (Fri)**, because the shift alone
would have cut EP61→방학식 from 22 to 17 days and squeezed S10; 7/22 restores
24 days.

**Only three lines of manuscript changed**: EP41's opening (`6월 첫 월요일` →
**`6월 첫 화요일`** — 2050-06-07 really is June's first Tuesday), EP41's
ledger (`6월 2일` → `6월 7일`), and EP50's `방학식은 7월 15일이었다` →
`7월 22일`. Everything else was state and record documents: 6 pre-fixes plus
**501 substitutions across 126 files**, then 10 stale range/duration
statements. Full record: `05_문체_상태_인계/Black_Titan_달력정정서_v1.0.md`.

**★ Trap for any future bulk date edit.** `M/D` dates are formally identical
to this project's arc counters — `S8 7/10`, `S9 6/12`, `S6 완결(6/6)`,
`진행 중(6/10)`, `Level 6/7`, `종료장부 7/7·8/8`, and the buoy triple
`7/5/2`. A blind regex destroys all of them; a classifier excluded 91 such
hits. Read 달력정정서 §2-C before touching dates in bulk.

Verified: **44 chapters, 0 weekday mismatches.** EP41 passes check_draft
(5,021) and check_voice. Spring dates (4/27 Wed, 5/18 Wed) untouched.

**New standing rule** (registered in 선례대장 §달력 and standing-guards):
canon calendar = the real 2050 Gregorian calendar; compute and check the
weekday before pinning any new date.

**S10 clock: EP61 = 6/28 (Tue) → 방학식 7/22 (Fri) = 24 days, three and a
half weeks.**

**A full in-story calendar now exists**:
`05_문체_상태_인계/Black_Titan_작중달력_v1.0.md` — March 2050 through February
2051 as month grids, with chapter numbers marked on their days, plus a
chapter-to-date table for EP1–61, the fixed points (sports day 4/27 Wed,
term-end assembly 7/22 Fri), the solar public holidays, and the EP1–17 range
that was deliberately never pinned. **Consult it before setting any new
date**, then carry that date unchanged through brief → Level 6 → draft → SNAP.
Lunar holidays (Seollal, Chuseok, Buddha's Birthday) are still unset and will
matter in autumn.

## S10 outline approved (2026-08-15)

`02_여름편_기획/Black_Titan_S10_EP062-076_화별개요_v1.0_승인.md` is
**LEVEL4_PASS**. S10 「통증과 균열」 = **EP62–76, fifteen chapters,
6/29 (Wed) – 7/22 (Fri), 24 days**, closing on the term-end assembly.

**The arc's spine is what the enemy is here for.** Spring: they came to
**take the Titan away**. S9: they **stopped engaging it**. S10: they come
**to destroy it** — the Titan is the priority target. **No character ever
explains this.** Five fights, each arriving from a different direction —
far (딱총새우, shockwave before contact), below (갯지렁이, the ground goes),
in numbers (톡토기), head-on (공작갯가재, first real pain), unseen
(갑오징어, inside the harbour) — and the intervals run **6, 5, 4, 3, 2 days**.
Only Sua sees that, in a new column on her table. At first it reads as an
advantage: Dana is getting better. She isn't; they're getting more frequent.

**The school falls because Dana misses one.** The 톡토기 swarm has **one
outrider that never joins the fight** — it slips toward town, and because it
never attacks, it never registers. She kills it, late, at the school. So the
minority who say `저것들은 타이탄 있는 데로 온다` are **wrong** — and she
cannot correct them, because the correct sentence is `내가 놓쳤다`.

**★ Public opinion does NOT turn** (user, explicit). Most people still like
their local giant; the criticism is a few lines. What changes is **whose
voice she hears**. And **being defended hurts more than being blamed** —
`없었으면 더 부서졌지` is true and leaves nothing to answer, exactly like
Hyejeong's `그럼 됐어` in EP61. **Seong-ho opens that lineage in EP63**: he
wins the long-owed 100m, feels wrong about it, and voids the result himself.
Not kindness — he's just uneasy. Dana can read it as being spared. The debt
is settled and a new one quietly opens.

**The illness starts on a running track, not a battlefield** — one moment of
vertigo during that race, written as heat. Scattered twice more (EP66 fever,
EP69 numbness), then **sharply worse right after 공작갯가재** (EP70); EP71
begins the instant she gets back and **runs past midnight into the next day**,
because this is the first time a fight doesn't end when it ends.

**The military speaks again**, picking up the fuse lit in EP50
(`출현 간격 단축 및 공격 행동 확인. 대응 방침 재검토`): EP65 adds a line to
the public observation sheet — `미확인 대형체`, no name, just coordinates
(Yeongjin alone knows what it means: **they are being written down now**);
EP69 someone brings that sheet as proof; EP76 the evacuation wording changes
to `미확인 대형체 인근`, arriving on the same paper that used to carry the
school calendar. **No troops move. No countermeasure.**

Sealed through S10: cell origin, Hyeonseo's equipment, anchor-surface
culture, Lucy, Hyejeong reaching the truth (she gets as far as equipment).

Next: **EP62 brief (Gate C)**.

## EP62 approved — S10 opens (2026-08-15)

**EP62 「좁아진다」** (`67_EP062_승인완료`, standard, 5,978 chars, 6/29 Wed)
is `GATE_D_PASS`. Official state = **SNAP-062**, tracker SNAP-062, ledger
**v1.57**. S10 is **1/15**.

**The arc does not open on an event.** All EP62 leaves behind is **one new
column on Sua's table** — `간격`, the gap between one arrival and the next —
backfilled as **2, 5, 3, 5** and going nowhere: `고르지가 않네` … `몰라.
지금은 안 보여.` Dana glances at it and moves on. Fifteen chapters later it
reads 6·5·4·3·2; today it is four numbers.

**★ The table is incomplete from the start.** Sua puts a **question mark**
on the third row, because **the barnacle-type is dated by the day it was
found, not the day it arrived** — `이건 온 날이 아니라 본 날이라서.` She
does not erase it. Same principle as leaving the identity column blank. **That
question mark survives to EP76**, so even when the numbers finally mean
something, the record is honest rather than complete.

**Naming pays off by going ordinary.** Four days on, `아이언 앵커` has
shortened to **`앵커`** and attaches to 감개, 사슬, 기름. Nobody remarks on it.

**Sua does not nag** (user correction, now in memory + this file): she places
a want once and steps back — `저번에 발표회 날 사 온 수박, 맛있었어요` —
then lets it go. **Dana is the one who pushes.** Sua's thanks is an action,
not a sentence: the side dish with the egg roll slides half a hand toward her
sister. A first draft had Sua pestering to fix a speech-level error; the
grammar was right and the person was wrong.

**The absence does not close.** Hyejeong asks everything except `어디` and
`왜`. EP32's promise stays unrecovered — Dana didn't break it, but saying so
would take one more lie. `말할 수 없는 게 아니라 말할 자리가 없었다.`

### ★ G0-013 — the descent is an elevator, not stairs

The hangar sits **at least twenty storeys down**; walking it was never
possible. LOC-02 §2.3 already had a person-lift with a **keyed floor
selector** — its origin was simply moved up to the iron door, giving **three
stops: door level, hangar floor, chest-height maintenance deck**. An emergency
stair exists alongside but stays **off the page** until a blackout or
breakdown makes it worth one scene. **Seven lines across five approved
chapters were rewritten** (EP1 ×2, EP5, EP37, EP45, EP57 ×2); all five still
pass check_voice. Most improved: stairs can be counted, a lift cannot, and
hiding the depth suits the place. See
`01_Gate0_설정변경/Black_Titan_G0-013_...APPROVED.yaml`.

**Two standing guards added**: concealment is a *location* rule (rig and
機體 never leave the hangar; the front yard holds procurement stock only —
this leaks in domestic scenes, not combat ones), and the descent is an
elevator.

Next: **EP63 「무효」** (7/1 Fri) — Seong-ho's 100m finally runs, **the first
symptom arrives on a running track rather than a battlefield** (one moment of
vertigo, written as heat), and **Seong-ho voids his own win** because it felt
wrong. Not kindness — unease. Dana can read it as being spared. Watch
`past_run`: EP62 closed at 8, the top of the warning band.

## EP63 approved — two lineages open (2026-08-16)

**EP63 「무효」** (`68_EP063_승인완료`, standard, 5,001 chars, 7/1 Fri) is
`GATE_D_PASS`. State = **SNAP-063**, tracker SNAP-063, ledger **v1.58**.
S10 is **2/15**. `past_run` closed at **6** — EP62's warning-band 8 is cleared.

**The illness begins on a running track.** Seong-ho's long-owed 100m finally
runs; halfway through, one moment of vertigo, half a step off, no fall and no
stop. **One sentence, never revisited**, and **Dana decides for herself that
it was the heat** before anyone else can name it. Because it happens on a
school field rather than in a cockpit, nobody connects it to anything.

**Seong-ho wins and voids his own win.** `이긴 것 같지가 않아서.` /
`그건 내가 정해.` He never says what he saw — the page never uses `봤다`,
because the annulment *is* the evidence — and he scuffs out his own finish
line with his toe. Debts 1–3 die; **a fourth quietly opens** (`다음에 다시
하자고`, no date).

**★ Two flow corrections came from the user and both were right.**

*Seong-ho does not press.* EP58 has him saying **`나 계속 물어보는 거 나도
좀 그렇거든`** and then backing off when Ye-jin invented a cover story. Having
him push again in EP62 and again in EP63 made him deaf to his own words. So
**EP62 was retroactively rewritten** (Scene 2 is now a corridor near-miss)
and EP63's Seong-ho says `오늘 금요일이야` and then just stands there. The
debt changes character: `물어보면 안 된다고 하면 되는데, 안 물어보니까 안
된다고 할 자리가 없었다` — untouchable rather than nagging.

*Dana is the one who asks.* Her motive is **the debt to Ye-jin**: she was
covered by a false reason she could not correct, and `오늘도 안 된다고 하면
(…) 예진은 또 어디선가 이유를 만들어 줄 것이다. 그러면 틀린 게 하나 더
쌓인다.` **So §1-E completes a full circle inside this chapter** — she runs to
pay off being wrongly defended, the result is annulled, and Hyejeong
immediately misreads it: `야 이성호, 너 지금 봐주는 거야?` `이 얘기는 앞으로
이런 식으로만 돌아다닐 것이다.` (EP62 already carried the recap, so three
paragraphs of restatement were cut from EP63.)

### Two standing guards added

- **The observation terminal is in the shop, not the hangar.** Going to look
  at buoy graphs means stepping *out* to the shop; living room to shop is
  **one step** (the floor sits slightly higher). Going *down* is for
  maintenance only. Written after making this mistake twice.
- **Do not bury Dana's competitiveness under circumstance.** She is not
  someone who ducks a race. When a reason not to compete appears, write the
  wanting-to as well — `이유가 없다면 단아도 당연히 뛰고 싶다.` **S10 makes
  her sicker every arc-beat, so this will recur.**

Next: **EP64 「먼저 온다」** (7/4 Mon, KEY, 5,800) — 딱총새우형. It hits
before contact; sound and light arrive first and the impact second, the order
inverted. **It passes the installations and comes at her** — a way of fighting
that exists in neither spring nor S9, and nobody puts it into words. The
two-stage anchor launch feels slow for the first time. No illness beat here;
the next scatter is EP66.

## G0-014 — air, not water (2026-08-16)

Two settings decisions landed while previewing EP64. Outline is now
**S10 v1.1**; request filed as `01_Gate0_설정변경/…G0-014…APPROVED.yaml`.

**딱총새우형 fires compressed air, not a cavitation bubble.** The inverted
order stays — light and sound first, impact after — and **the impulse is much
larger than the urchin-type's**. But it is the **same lineage**: EP10's spines
cut grooves that had to be filled and ground down and never reached anything
functional. **The shockwave does no real damage either — and neither Dana nor
the reader is told that.** Write it frightening and leave the machine intact;
no all-clear verdict, no relieved line, no pointed absence of a damage list.
Maintenance still happens the way maintenance always happens. **The dread in
EP64 is not injury, it's notice**: she is hit before contact, and the thing
came for *her*.

**★ No underwater combat until autumn.** Mudflat, thigh-to-chest shallows,
the drained hours of the sunken district, inside the seawall — the S9 range —
all fine. Diving, full submersion, fighting below the surface — not until the
season turns. **Reason (author-side): autumn is where the anchor's rocket
fails to ignite underwater**, and that failure is what drives the new-weapon
arc. Spending a water fight now spends the card early. This binds
**갑오징어형 (EP73) too**: its concealment runs on murky water and structures
with the torso above the surface, not on being submerged. 공작갯가재형's
"물속에서" line was cut accordingly.

Practical rule going forward: **fix the depth of the battlefield first**
(the existing 전장 구조 6+1 lock). Past shallows is already a violation.

## The pain is a price, not an injury (2026-08-16) — outline now S10 v1.2

New axis from the user, filed as outline **§1-I**. It supplies the *cause*
the illness curve was missing.

Once the creatures start coming **openly for the Titan**, Dana isn't only
frightened — **she gets riled.** The confidence curve running since EP37 picks
up a competitive edge on top: she closes more, holds longer, hits harder
(EP64 → EP66 → EP68). **At 공작갯가재 (EP70) she crosses a line** — wanting
to win outruns wanting to be careful. **That is why the fever turns continuous
right after that fight** and not somewhere else.

**Author-side mechanism, never on the page**: crossing that line **deepens
synchronisation** — the bypass filter thins and raw sensation and pain get
through less filtered. `동조`·`적합`·`계통` stay forbidden words (G0-004
seals the real mechanism until after the last day of summer break). **The page
carries only behaviour and pain.** Dana doesn't know what she crossed;
Yeongjin guesses and says nothing.

**Why this matters for character**: written as a disaster arriving from
outside, the illness flattens Dana into a victim. Written as **the price of
her own competitiveness**, she stays standing — same root as the guard
「단아의 승부욕을 사정으로 덮지 말 것」.

**Forbidden-word scope clarified** while checking this: `무효`·`소용없`·
`끄떡없` are barred **in combat-verdict context only** — don't tell the reader
an attack didn't work (same intent as G0-014). EP63's title 「무효」 is a
voided footrace and is fine.

## EP64 approved — S10's first fight (2026-08-16)

**EP64 「먼저 온다」** (`69_EP064_승인완료`, KEY, 5,234 chars, 7/4 Mon) is
`GATE_D_PASS`. State = **SNAP-064**, tracker SNAP-064, ledger **v1.59**.
S10 is **3/15**. Interval sequence opens at **6 days**.

**Three things happen for the first time in one chapter.**

**It comes for her.** The shockwave flattens a warehouse only because the
warehouse sat on the line. `그러니까 저건 여기 뭘 부수러 온 게 아니다.` And
that is where it stops — `저거 나만 봐` / `그런 것 같다`. Nothing is
concluded. Sound, then light, then impact: **she knows it's coming and still
can't move**, in clear weather, at two hundred metres. `맞은 데가 없다. 없는데
온몸이 안다.` **The machine is fine and nobody knows that — the reader
included.** Maintenance runs exactly as it always does.

**EP44 comes back.** `팔보다 긴 게. 저기까지 닿는 게.` — that wish became
the anchor, and here the anchor fails, because **two hundred metres is the
first time**; every previous use was up close. The answer is not a longer
reach but **no distance at all**. She closes, and since the thing fires *by
closing its claw*, she jams the chain into it and **winds two more turns to
lock it**. The launcher's own rule (`the arm is unusable while winching`)
stretches to the whole fight: the chain tangles and **the left arm never comes
free**. So the finish is knee to the joint and a **right straight** — and
**Dana is left-handed** (EP10's `왼손잡이 특수요원` profile, EP11 titled
「오른손의 급식」). It works because it's point-blank. **No self-awareness on
the page**, and the profile contradiction goes unclaimed.

**She laughs.** Mid-fight, holding the claw shut: `못 쏜다. 지금 저건 못
쏜다.` **That is §1-I lighting** — it burns until EP70. And **she wins by
hitting**, which she has never done; she has always braced, pried, pushed.

**Yeongjin says `잘 했다`.** The no-congratulation streak breaks for the first
time and Dana can only manage `어`. `잘 했다는 말은 순서에 없는 말이었다.`
Closing line: `마지막의 부서지는 감촉이 아직 남아 있었다. 하지만 손등에는
아무것도 없었다.`

### Guard added: pain vocabulary is sealed until EP70

Not just `저림`/`흐림`/`마비` — **`아프다`·`아팠다` too**, even in combat
recollection. Use **`느낌이 왔다`**. Pain gets its name at 공작갯가재 (EP70);
spending the word earlier cheapens that chapter. (Caught in 첨삭 — I had
written `부딪친 자리가 아팠고`.)

**Also caught by check_draft**: I leaked `성게형`/`투구게형` into prose during
expansion. Author-only taxa — say `봄에도 했고 지난달에도 했다`.

Next: **EP65 「적히기 시작한다」** (7/5 Tue, standard, no combat) — the
military shows its face (고명준 ●, gap 8; 오미란 ●, gap 10, same scene), and
**one line is added to the public observation sheet: `미확인 대형체`**, no
name, only coordinates. **Only Yeongjin knows what it means** — they are being
written down now — and he says nothing. Opinion has not turned yet; it only
cracks. Recovery targets: `past_run` closed at 8, dialogue at 34.4%.

## EP65 approved + supporting-cast audit (2026-08-16)

**EP65 「적히기 시작한다」** (`70_EP065_승인완료`, standard, 5,296 chars,
7/5 Tue) is `GATE_D_PASS`. State = **SNAP-065**, tracker SNAP-065, ledger
**v1.60**. S10 is **4/15** — sub-arc ① closes.

**The event is one line added to a table.** `미확인 대형체`, coordinates and
time only. Myeongjun has Seojin overlay every arrival point since March, and
the cluster **is not the harbour** — `저 거인이 있던 자리입니다`, which he
does not correct. So the giant's position became a variable, and variables get
written down. Public sheet says `미확인 대형체`; internal filing keeps EP5's
`소속 불명 전략무력`. `괴수가 아니라고 쓸 근거도 없잖나.` The scene closes
the way this lineage always closes — **on what Seojin does not write**:
`저게 어디 서 있느냐가—` … `됐다. 적을 것만 적어.`

**Yeongjin's hand stops for one beat** at that row and moves on. Dana sees the
stop and does not know what she saw. That is the whole event on the family
side.

### ★★ Supporting-cast audit — the real work of this chapter

At the user's direction I ran a full census of 16 supporting characters. Two
findings, both real.

**1. Hyejeong and Seong-ho had swapped places.** Card canon: Hyejeong
`짧게 찌른다`, forbidden `만연체`; Seong-ho `수치·고유명사·비교급이 쏟아진다`,
`정보량 최다`. Measured: spring Seong-ho 26.7 chars/line > Yejin 19.2 >
Hyejeong 16.4. Summer: **Hyejeong 24.8 (longest 113) > Yejin 21.8 >
Seong-ho 15.2.** Exactly inverted. Cause (a): I over-corrected the
「단답 금지」 memory into run-on speeches — **talking a lot means jabbing
repeatedly, not one long block**. Cause (b): Seong-ho's giant-obsession thread
**died at EP43** (21 chapters), so his numbers and hyperbole had nowhere to go.
Side effect: length is *Yejin's* instrument (`길이가 곧 완충`), and Hyejeong
had taken it. **Fixed 5 places across EP57/62/63** (→ 19.1); left EP42's
111-char speech (narration marks it as an exception and snaps back to a joke)
and EP62's Yejin (functioning as buffer).

**2. Summer lost the town.** Spring ran on shopkeepers, fishery co-op,
military, homeroom teacher. Summer had been running on **family 3 + school 3**.
Kim Juho 16→3 chapters, Myeongjun 11→3, Seojin 6→2, Miran 8→3, and
**Bae Jeongho / Jang Woojin / Choi Narae 12→0** — Narae unseen for 57 chapters,
Woojin 41, Jeongho 36. EP65 reopens military and co-op (**Seojin returns after
a gap of 59**); **Narae is booked for EP69**.

**Two standing guards added**: Seong-ho is the giant's chronicler (notebook,
profile, statistics — he does not walk past giant-related screens or rumours);
Narae is the giant's cartoonist (EP6 — the class's fads pass through her
notebook, and **her drawings follow what Dana actually does**, so by now the
chain on the left arm should be in there).

**Retro insert, EP57**: EP56 exposed the Titan at its closest — daylight, near
town, `난간이 있고, 옥상이 있고, 언덕이 있다`. Seong-ho would not have missed
it, and EP57 already had Hyejeong saying `본 사람은?` / `없어. 그게 웃긴
거지.` — so he cuts in with **`있는데.`** and gives an eyewitness account that
is entirely correct, which is why Dana says nothing. `사 분을 셌다고?` /
**`세야 알지.`** now rhymes with EP65. EP57: 5,090 → 5,591.

Recovery targets from EP64 both met: dialogue 34.4% → **56.5%**, `past_run`
8 → **6**.

Next: **EP66 「밑」** (7/9 Sat) — 갯지렁이형, interval **5**, the ground gives
way and weight becomes a liability for the first time; the anchor gets driven
in to hold. **First scattered illness beat** (fever, read as summer cold) —
`아프다` vocabulary still sealed until EP70.

## EP66 approved (2026-08-16)

**EP66 「밑」** (`71_EP066_승인완료`, standard, 5,950 chars, 7/9 Sat) is
`GATE_D_PASS`. State = **SNAP-066**, tracker SNAP-066, ledger **v1.61**.
S10 is **5/15** — sub-arc ② opens. Interval 6 → **5**.

**The ground was the enemy.** Natural terrain, not reclaimed land — the
landfill was spent at 투구게 (EP52–53), so this is a mud flat with bedrock on
the city side. It builds the chapter by itself: hard ground behind, soft
ground ahead, and **the only place to fall back to is the city**.

**Weight became a liability for the first time.** Foot sinks, pulling it
sinks the other, then the knee. `버틸수록 깊어진다` — and the fix is
counter-intuitive: **stop pushing**. `힘 주면 더 들어간다. 빼.`

**★ The EP52–53 answer failed.** Her body reached for `밀릴지는 내가 정한다`
before she did, and **nothing pushed back**. Correction the user made to my
draft: at 투구게 **Dana was the one pushed** — weight won for the *other*
side. So the line is **`밀리는 데는 방향이 있고 가라앉는 데는 없다`.**

**★ The anchor gets driven into rock; the chain becomes a lifeline.** Usage
#3. `무기로 쓰던 걸 오늘은 줄로 쓰고 있었다` — she stands on her arm, not her
feet. Then she reverses the reel and uses it to **pull the enemy in**.

**★★ Spring lineage recognition — first on the page.** This is a 갯지렁이형,
same face as the 관갯지렁이 of EP31/35, and **the left jaw is intact**
(Dana broke it in spring — EP31's title is 「부러진 턱」). So: `같은 얼굴에
성한 턱을 달고, 하는 짓만 달라져서 왔다.` **Then it was walking off with
her; now it digs underneath to drop her.** This is the first page-level
instance of the L3 line **`낯익은 놈이 다르게 온다`** (re-dispatch by taxon).
성게형·바닷가재형 remain.

**Jaws open left-right, so she grabs left-right** — both arms, and slams it
down. In spring (EP35) her left arm was pinned and one right fist was all she
had. **Now she has both.** The growth curve shows inside the same taxon. The
slam carries scale: tremor before sound, bedrock splitting, fragments thrown
person-high, `발밑이 흔들렸다. 흔들리는데 안 꺼졌다`. She finishes by pulling
the driven anchor free and cutting on the second swing.

**★★ `속이 안 좋았다. 그리고 그것보다 이긴 게 더 컸다`** — §1-I stage ②
on the page. Nausea loses to winning.

**★ And she had backed toward the city.** She went out to get *away* from
it and came back to survive. Beat 1, after driving the anchor:
`다른 방법이 없다는 게 이유가 되는지는 몰랐다`. Beat 2, after the coast road
subsides: **`저것이 여기로 온 건 단아가 끌고 왔기 때문이었다`.** Beat 3, at
the sink: `근데 그 설 데가 도시 쪽이었어` / **`그럼 어디였어야 하냐`** —
and she does not answer, `대답을 하면 그게 무슨 말이 되는지 알 것 같아서`.
**This lays a rail to EP69.**

**Illness scatter ①**: fever that evening, filed by herself as a summer cold
(three hours in water, sweat). **No link drawn to EP63.** Sua feels her
forehead, sets cold water beside the table, says nothing about drinking it.

**Correction, standing guard**: you cannot smell anything from inside the
cockpit. Draft had `냄새가 났다` / `그 냄새에`; fixed to `미끈거려 보였다` /
`그 모습에`. **No olfactory narration in the cockpit.**

Next: **EP67** (7/11 Mon, standard, no combat) — **이하랑 ●** closes a gap of
24 (Sua's after-school violin), and **Hyejeong starts to notice the pattern**:
the absences line up with the sea. Sua's interval column now reads 5 under 6
and she says nothing. Seong-ho arrives Monday with a weekend's worth of
questions stored up.

## EP67 approved (2026-08-16)

**EP67 「표」** (`72_EP067_승인완료`, standard, 6,294 chars, 7/11 Mon,
**no combat**) is `GATE_D_PASS`. State = **SNAP-067**, tracker SNAP-067,
ledger **v1.62**. S10 is **6/15**.

**Four tables point the same way.** The military's public sheet (EP65), Sua's
interval column, Seong-ho's notebook, and Dana's blank vacation planner. Nobody
compared them; the direction matches anyway, and **the far end of it is the
Do house.**

### ★★ The axis: the evening phone call

Spring canon (EP4/29/30/33): a nightly call, thirty minutes; when Dana ran
late she sent **`오늘 좀 늦어짐. 한 시간 정도`**, and Hyejeong answered with
**a photo, no words** — and **`어디가 늦는지, 왜 늦는지는 이번에도 사진
어디에도 없었다`**.

**「이번에도」 is the root of this chapter.** Hyejeong has been *declining to
ask* since spring. So what happens here is not a discovery — it is **the
restraint overflowing**.

**Measured: 26 summer chapters (EP41–66) with zero call on the page.** At the
user's direction that gap is recovered as an *event*, not patched as an
omission: spring's messages are long, summer's are `늦어짐` alone — **the
"how late" has dropped off.** And **7/9's slot is empty** — she had a fever
and just slept, so **not even the word went out**. First time since spring
that nothing came at all. **Hyejeong never mentions it.** Dana sees it alone.

**Seong-ho is the trigger.** He missed Saturday (bus, far side of town), so
Monday he recites dates — pure boasting. **He counts the giant; Hyejeong
counts `늦어짐`.** Same table, different column. Her laugh lands half a beat
late at `지난 토요일`, and the narration does not explain why.

**The refusal to ask holds.** At break she nags instead (planner, locker key,
indoor shoes), goes to the threshold once — **`너 요즘—`** — and closes it
with **`아니다`**.

**★★ The overflow arrives as a photo with no text**, per EP33's grammar: her
own message list, dates visible, and one line beneath —
**`이번 주는 계속 오늘처럼 통화하자.`**

**★ One ending carries it.** Hyejeong issues orders: `전화해` · `들어가면
전화해` · `계획표 내` · `리코더 있는지 확인해 봐`. **`-하자` is a rare
thing from her**, and the rarity is the tell. No `보고 싶다`, no `왜 없냐`.

**Dana's reply**: she deletes 미안하다 (that would mean she won't be late) and
그럴게 (that would just add a line to the photo), and sends **`알았어`** —
**knowing she can't keep it. That debt is what EP69 spends.**

### ★ Harang — the one who couldn't count, and learned without noticing

User correction, and it made the scene. In spring **Harang could not count
rests**: on a three-rest bar her arm came up around two, Sua would lower her
bow and say let's go again, Harang laughed and went again. **All spring.**

Today she doesn't miss. And **she doesn't know she got better**:
`근데 나 세는 거 아니야` / `발로 셌잖아` / **`세는 거면 숫자가 있어야지.
나 숫자 안 세.`** / `밟으면 알지.` Closing: **`하랑은 그걸 언제 배웠는지
몰랐다. 배웠다는 것도 몰랐다.`**

**★★ The counting trichotomy gains a member.** Dana learns through the body,
Sua draws it in her head, Lucy was trained — **Harang is body too.** Sua, who
counts, watches someone know without counting for the first time, and that
night she lifts the pencil off the interval column she cannot fill.

### ★★ Canon corrections — seven, all user-flagged

Supporting-cast placement was wrong in five places, a direct after-effect of
the summer cast-loss diagnosed at EP65.

1. **Kim Juho written as a classmate** — he is a **40s male teacher, Dana's
   homeroom** (G0-005 §3.6). Now runs morning roll.
2. **Im Yujeong ran Dana's homeroom** — she is the **3rd-grade** homeroom
   (Sua's). Removed.
3. **Moon Jaeho / Bae Yurim placed in Dana's class** — **both are 3rd grade**.
   All lines moved to **Jang Woojin** (gap 42 closed; big gestures, one hand
   in the hoodie pocket).
4. **Seong-ho talking straight at Dana** — they are **rivals and everyday
   antagonists**. He now boasts to the others and Dana overhears; one clash
   only (`안 갔으면 못 보지` / **`도릴라 너 진짜`**), and he turns back
   because there is nothing to win.
5. **`옥상에서 봤고`** — EP57 has him at **`그 위 언덕은 안 막았어`**, and the
   *rooftop* witness is a different kid whose account **collapsed** (`그 집
   옥상에서는 벽이 안 보인다`). I had moved him into the discredited seat.
   Also aligned **`사 분`** spelling to EP57's page (3 places).
6. **Safety map treated as unsubmitted** — **submitted at EP36**, and Juho
   received it. Replaced with the **summer vacation planner**: another table,
   this one for **what you'll do next**, and its circle is empty. Same problem
   as Sua's unfillable next cell.
7. **Tteokbokki interest still running** — **settled at EP41** for three fish
   cakes. Replaced with the vacation-plan exchange, which supplies **the reason
   the photo gets sent**: `방학에 뭐 할 거냐고` / `몰라` / **`그때 가 봐야
   알지`** — **the line Seong-ho used that morning, that Hyejeong mocked and
   the class laughed at. This time Hyejeong doesn't laugh.** `그래.` Then
   silence, then `잠깐만`, then the photo.

**Two adults who don't ask**: Juho stops at Dana's name over last week's early
dismissal, asks only whether she's well, and moves on — `왜 조퇴했는지는
봄부터 한 번도 물은 적이 없었다`. One keeps not asking; the other overflows
tonight.

Next: **EP68 「한 마리」** (7/13 Wed, **key chapter 5,800**, interval **4**) —
톡토기형, many, leaping, blinding by covering. **One breaks off toward town and
does not attack, so it never registers — Dana misses it.** She learns only
after clearing the swarm; it is already at the school (gym, part of a
classroom). She chases it down in the same chapter. **She wins and it does not
feel like winning.** Do not stage the miss as her error — nobody could have
caught it; **only she thinks otherwise.** Last night's `알았어` gains weight
here.

## Process hardening after the full audit (2026-08-17)

The EP1–67 full audit (`Black_Titan_전수감사_보고서_2026-08-16_v1.0.md`, all
batches applied) traced the recurring mistakes to three roots, and each now
has a standing countermeasure. **These are pipeline rules from EP68 on.**

1. **Canon wasn't in front of me while drafting** (cast placement, speech
   levels, sealed vocabulary all existed in G0-005/ledger/guards but I drafted
   from memory, and memory serves spring impressions before canon). →
   **`05_문체_상태_인계/Black_Titan_집필전_정본카드_v1.0.md`** — a one-page
   card of *only the things actually gotten wrong*: class-placement matrix
   (Dana's class: teacher Kim Juho + 혜정·예진·성호·장우진·최나래·강한결; Sua's
   3rd grade: teacher Im Yujeong + 문재호·배유림; 이하랑 = different 3rd-grade
   class), speech-level matrix, current vocabulary seals, number rules, POV
   naming, top-10 repeated factual errors. **Read it at Gate C and again at
   Level 7, every episode.** Maintenance: an error type that recurs twice gets
   added; three months clean and it comes off — the card must stay one page.
2. **Retro-corrections were applied to "the episodes I remembered"** (the
   elevator fix missed 8 chapters). → **Every G0 correction triggers an
   immediate grep sweep across ALL approved chapters**, never a hand-picked
   subset.
3. **The machine checks didn't cover the layers that actually broke.** →
   **`scripts/check_continuity.py`** added to the skill; the standard battery
   is now **five checks**: check_draft / check_voice / check_translationese /
   forbidden-grep / **check_continuity**. The new one reports (a) a character
   watchlist that fires on every named appearance with the canon note
   (placement/register/relationship), (b) every relative time word for manual
   calendar collation, (c) sealed vocabulary by episode number (hard=FAIL:
   신경 어휘·계단·갯벌·인트라넷; soft=WARN needing subject/context judgment:
   아프- forms, 팔짱), (d) verbatim duplicate sentences (≥18 chars) against
   the whole approved corpus plus tic-density (`반 박자`, `한동안`, etc.).
   WARNs are deliberately noisy — they exist to put canon in front of the eye
   at the moment of writing, not to gate.

Closing checklist addition: after every approval, verify state-document
freshness (SNAP and tracker actually regenerated — byte-identical files mean
a freeze like B-1), run sync-skill.ps1, and post the date to the in-world
calendar.

## EP68 approved (2026-08-17)

**EP68 「한 마리」** (`73_EP068_승인완료`, **key chapter**, 5,645 chars,
7/13 Wed) is `GATE_D_PASS`. State = **SNAP-068**, tracker SNAP-068, ledger
**v1.63**, calendar updated. S10 is **7/15** — sub-arc ② closes. Interval
6 → 5 → **4**.

**She misses one, for the first time in the series.** Springtails, many,
leaping, sticking. The swarm goes for the Titan; **one does not** — it drops
low, does not attack, and leaves through the **covered drainage channel**
toward town, where **no buoy and no camera reaches**.

**★★ The heart of the chapter: the fix and the blind spot are the same
motion.** Peeling them off one at a time fails (they re-stick), so she backs
into a sluice pillar and **scrubs her back against it** — like a dog on a
tree. `52미터짜리가 할 짓은 아니었는데, 그 순간에는 그것 말고 방법이
없었다.` Concrete grinds off, a frame tears loose — **`부수면서 하는
방법이었다. 그것도 알고 있었다.`** Then she scrubs **once more, to be sure**.

**`그동안 앞쪽만 봤다.`**

The narration does not say what she failed to see. **It is the price of the
method, not an error.**

**Four locks so the miss cannot read as carelessness**: (1) the count was
never knowable — `세 개가 걸렸는데 세 마리라는 뜻은 아니었다`, they are
`뭉쳐 있다`; (2) sight was erased — left, then up, then half the front, with
**`장갑을 갉아 대는 소리`** filling in useless information; (3) that one never
attacked, so it emitted no threat signal; (4) the covered channel is a grey
band on the display. **She does not discover it — the school files a notice.**

**★ Warning-order correction (user).** The draft ran alarm → sortie → buoys,
which erases the family's information edge. Canon: **buoys ring audibly in the
shop** (EP59), so at school she can't hear them. EP64 had the broadcast first
because that was the **harbour**; today is **inside the seawall**, so the buoy
comes first. Rewritten: mid-5th-period her pocket buzzes, two characters —
**`부표`** — no number, no location, because **`그걸 칠 사람이 화면 앞에
없다는 뜻`**. The broadcast catches her halfway across the yard, from behind.
**This makes the chapter worse for her, correctly**: she left before anyone
and still missed it. Early warning does not hand you a count.

**The school was empty; she doesn't know that until she arrives.** The gate is
open `열어 놓을 시간밖에 없었던 것처럼`; a shoe bag is half-trodden. **LOC-03
broken to spec** — the right-hand window wall, the 26 lockers, the smart board.
**`교실은 안에서 밖을 보는 데다`** — and this morning the window row looked out
first, as always. Her desk is over; **the one beside it is still standing.
That is Hyejeong's.** She finishes it on **the EP19–23 playground**, where
`그때는 사람이 너무 많아서 그게 문제였다` and today no one is there and the
lines are washed out. Anchor pre-strikes the landing point (EP44 lineage —
`뛰는 것들은 뛰기 전에 반드시 웅크린다`), then the hand, **then one more hit
she knows is pointless.**

**Yeongjin's exoneration doesn't land as one**: `저기는 화면에 안 잡힌다`
is simply true, but `못 봤다는 말을 못 볼 수밖에 없었다는 말로 바꿔 주는
소리로 들렸고, 그건 위로였고, 위로를 받을 만한 일을 한 기억이 없었다.`
Then **`아무도 모른다는 건, 다음에도 모른다는 뜻이었다.`**

**★ Hyejeong calls first.** Dana can't — what she must hide is not that she
was at the school but that **she left saying "bathroom" and never came back**,
which is the only hole Hyejeong can actually see. Hyejeong talks about windows,
lockers, an umbrella, assembly, Seong-ho's camera angle. **Never once about the
giant.** `내일도 해.` — **she proposed "every day this week" on Monday, and she
is the one keeping it on day three.**

Sua writes **4** in the interval column (`한 획이었다`), leaves the next cell
blank **without even touching the pencil to it**, and registers that
**`오늘 못 센 게 하나 더 있었다. 그건 표에 적을 칸이 없었다`** — she tried to
count the swarm and lost the number at the second one.

### ★★ First run of the five-check battery — it caught four things

`check_continuity.py` earned its place immediately:

1. `저 사람은 원래 사실만 말한다` — POV naming (check_voice).
2. `아픈 데가 어디라고` — sealed-vocabulary WARN; negated construction but a
   **positive noun phrase**, still sealed until EP70.
3. **`수아는 상 위에 표를 펴 놓고 있었다.`** — verbatim identical to EP67.
   Same pattern as the EP60↔61 incident. Varied.
4. **`할아버지는 대답하지 않았다.` ×2 in one chapter** — which exposed a gap:
   [4] only compared against *other* chapters. **Self-duplication detection
   added**, and it fired on the first run. Split the register: scene 4 is the
   **link going quiet** (`잡음이 한 번 지나갔고, 그게 다였다`), scene 5 is a
   **person declining to answer**, so the line rings exactly once.

**Also added as hard FAIL: `[『』《》〈〉]`.** I had marked comms dialogue with
corner brackets in this chapter alone; all 67 prior chapters use plain double
quotes. **It was corrupting the metrics** — check_draft counts only paragraphs
starting with `"` as dialogue, so the chapter read 30.2% when it was actually
**41.8%**, and I kept expanding comms to hit a band I was already inside.

Other user corrections: **scale must stay in the machine's frame** (`이 기체
기준으로 팔 길이면 사실 버스보다 크다`, and later `버스 두 대 / 작은 비행기`,
never "finger-sized to a person"); **`봄에도` → `지난달에도`** (the
`팔보다 긴 게` line is EP44 = 6/13, exactly one month back); **5th period is
1:30**, not 2:30; **`물에 녹고 있었고`** (dissolution is canon — EP5, EP54);
`공지 왔다`; 4th floor; `『단아야.』`→`"단아야."` ×3.

Next: **EP69 「들리는 것」** (7/14 Thu, key chapter) — temporary classroom.
**Most people still like it** (`없었으면 더 부서졌지` — true, which is why it
stops being audible). **The criticism is only a few lines**: a board post and
one voice from behind — `저것들은 타이탄 있는 데로 온다`, **wrong, and
irrefutable**, because correcting it requires the true sentence, and the true
sentence is **「내가 놓쳤다」**. One of those few lines brings military data
(§1-H ②) that was never meant that way. **★ Choi Narae ●** at gap 56 — the
giant's cartoonist; **the chain on the left arm should be in her notebook by
now**; one line only, no approach to the truth, and Dana must not correct her
drawing again (that was EP6). Im Yujeong ◐, Kang Hangyeol ◐, **illness scatter
② (sensory)**. Do not make the critic a villain, and do not give them page
count.

## EP69 approved (2026-08-17)

**EP69 「들리는 것」** (`74_EP069_승인완료`, **key chapter**, 6,160 chars,
7/14 Thu, **no combat**) is `GATE_D_PASS`. State = **SNAP-069**, tracker
SNAP-069, ledger **v1.64**, calendar updated. S10 is **8/15**.

**Ten things were said. Nine were grateful. One is what she remembers.**

The support is the majority and it is all *correct* — a neighbour's `그래도
애들 있을 때 안 온 게 어디야`, the classroom's `없었으면 더 부서졌지`,
Seong-ho counting yesterday's swarm, Woojin miming the back-scrub to laughter.
**The reason none of it lands is never stated as such**; it is put once, flat:
`막은 얘기는 다 잘 들렸다. 잘 들리는데 남지가 않았다. **남는 건 못 막은 쪽
얘기일 텐데 그 얘기를 하는 사람이 교실에 없었다.**`

**Criticism is two lines total, with no face, name, or page count.** A board
post Hyejeong scrolls past — **`저것들은 거인 있는 데로 온다`**, `글자 수로
치면 열몇 자였다. 오늘 아침부터 지금까지 들은 말 중에 제일 짧았다` — and one
unattributed corridor voice (§1-H ②) citing the military sheet:
`저것 근처가 위험하다고. 좌표까지 있대.` **Dana never hears the second one.
Sua does.**

### ★★ Three people know, and none of it reaches

This is the chapter's spine:

- **Seong-ho**: `스물몇은 거기 있었는데 하나만 왔잖아. 하나만 온 게
  이상하다고.` He states the anomaly and produces no answer, so the class
  moves on.
- **Yejin**: reconstructs the back-scrub correctly — `벽은 도구였던 셈` —
  which **ends the laughter**, and `단아는 그 틈에 웃는 얼굴을 내려놨다.
  예진이 그렇게 해 준 건데 예진은 그걸 몰랐다.`
- **Sua**: she has actually *read* the sheet. The coordinates were not written
  to mean danger, they were written to mean it was there.
  **`표를 읽을 줄 아는 사람이 그 복도에 하나뿐이었는데, 그 하나가 아무 말도
  못 하는 사람이었다.`**

**Correcting it requires answering "how do you know," and neither sister can.**
The same lock is on both of them at once.

**Hyejeong stops herself.** The window row she has predicted since EP30
(`창가 줄이 유력하다는 근거를 세 개나 댔는데, 세 개 다 작년에 틀린 근거였다`)
and re-argued in EP67 (`근거는 틀려도 결론은 맞았다고 우겼다`) **finally comes
true** — `내가 창가라 그랬지` / `이게 자리 바꾸기야?` / **`자리가 바뀌었잖아.`**
Then the laugh curdles: the seats changed because the classroom broke, and
**`혜정도 그 생각이 났는지 그다음 말은 안 했다.`** That half-beat is what keeps
her off the criticism side for the rest of the arc.

**★★ Choi Narae ● — gap 56 closed.** EP6 spec honoured: bob, gold pin,
**stub pencil**, notebook never shielded, Seong-ho's special agent still alive
in the corner. **The comic tracks reality**: the chain is drawn on the left
arm **with the winding direction correct** — `영상에 잡힌 건 멀리서 찍힌
것뿐이고 사슬이 어디서부터 감기는지까지는 안 나온다. / 그런데 그려져 있었다.`
And yesterday's back-scrub is in there too: **`교실에서는 웃겼다. / 여기서는
안 웃겼다.`** The narration does not analyse why — the lines just are.
Her one line, at an erasure she started and abandoned:
**`얘는 잘못 안 했는데.`** It is about the character in the comic; she knows
nothing about the board or the mood. `그런데 그 한 줄이 오늘 들은 말 중에
제일 오래 갔다.`

**Illness scatter ②** — a stub pencil handed over, `받았다고 생각했다`, and it
hits the floor. **Left hand.** Normal a few seconds later:
**`방금 것만 이상했다.`** Filed by her as lack of sleep. **No link drawn to
EP63 or EP66.** Witnessed only by Narae, who picks it up and says nothing.

Closing: she builds a rebuttal and stops at `그 하나는—`, because
`그 뒤를 채우면 무슨 문장이 나오는지 알 것 같아서 안 채웠다.`

### Corrections this round

1. **★ Naming leak** — the board post read `저것들은 타이탄 있는 데로 온다`.
   **`타이탄` is family-only** (Dana/Sua/Yeongjin); check_draft's knowledge
   warning caught it. User settled on the bare **`거인`** — shortest is
   sharpest, and an affectionate qualifier would have explained the poster's
   attitude.
2. **★ Scale, second offence** — `발로 밀어 놨는지 흐릿했다` for a crater a
   52m machine pressed and an anchor struck. Now: a half-finished excavator
   job, spoil heaped beside it, **`파인 자리는 아직 사람 키보다 깊었다`**,
   an extra cordon. **Same class of error as EP68's `손가락만 한 것`, so it
   is now item 11 on the precheck card**, alongside a new item 12 for the
   naming gate.
3. **Blocking** — Dana sits in a middle row; she would never pass the window
   row going for water. **Hyejeong now crosses over every break and perches on
   the corner of Dana's desk** — `두 줄 건너가 먼 게 아니라는 걸 증명하려는
   사람처럼` — which also makes the phone screen naturally visible. The next
   break she *doesn't* come over (held up by the window row), **which is what
   gives Narae the seat time.**
4. **Yejin given real page count** (user request), in three places that all
   look like they're going nowhere and all land: the storeroom guess (quoted
   back by Hyejeong that night — `예진이가 창고였을 거랬잖아`), the mime
   analysis, the science-room smell (`물어보면 십 분이야`). **The words nobody
   needs stick; the one that matters doesn't.**
5. `안 막은` → **`못 막은`**; `그런 걸` → **`이런 걸`** (they are looking at
   the screen together).

Next: **EP70 「울린다」** (7/16 Sat, key chapter, interval **3**) —
공작갯가재형, striking head-on, coming **through** the armour. **★★ This is
the chapter where `아프다` unseals** — sealed since EP32 「아프면 아프다고」.
What she has been calling "it rings, it isn't pain" stops working. **§1-I
crosses the line**: past EP66's stage (nausea losing to the win) into wanting
it badly enough to overreach. **Illness intensity rises sharply from here on**
(user-confirmed: after the 공작갯가재 fight). EP71 starts the same day,
immediately post-return, and runs into the next.

## EP70 approved (2026-08-17) — the unsealing

**EP70 「울린다」** (`75_EP070_승인완료`, **key chapter**, 6,400 chars,
7/16 Sat) is `GATE_D_PASS`. State = **SNAP-070**, tracker SNAP-070, ledger
**v1.65**, calendar updated. S10 is **9/15**. Interval **3**.

**`아프다` is unsealed here** — held since EP32 「아프면 아프다고」, where
Hyejeong made the rule: `늦으면 늦는다고 했으니까 됐어. 그런데 아프면
아프다고도 해.` Zero positive uses on the page since.

**The order matters: she crosses the line first, and the pain is the price.**
Not hit and therefore hurt — **walked into it and therefore hurt.** The ground
gives her no excuse this time (EP66 sank, EP68 had a blind spot; this is hard,
flat, fully open, with **room to fall back**).

### The trigger — it copies her (restored at user direction)

The cause of the sync-depth shift is *emotion*, so **something has to be on
the page to set it off.** The old draft's mimicry taunt is back, and the
physical basis was already in the creature: **the folded arm snapping out
traces the same line as her own front finish** (EP64 onward).

Three overlaps: the mid-air demo (`아무것도 안 맞았는데 잠시 후 터지는
소리가 났다` / `어디서 본 것 같았다`), fist-clench syncing with arm-fold
(`한 번은 우연이었다`), and finally **the stop** — `똑같이 멈췄다. 반 초쯤.`
plus **`녹색 안광이 번득이는 눈자루가 마치 재어 보듯 까딱였다`**.

**★ It is never adjudicated (§1-A).** Yeongjin: `구조가 그런 거다. 팔이
그렇게 접히면 그렇게 나온다.` Dana: `아니야.` **His explanation is never
corrected.** The adult stated a fact; the child picked the version that made
her angry. **Do not resolve this later.**

Rage stays child-sized — no shouting. `숨이 코로만 나갔다. 어금니가 저절로
맞물렸고, 오른손은 쥐라고 하지도 않았는데 쥐어져 있었다.` /
**`무서운 건 아직 있었다. 그 위에 다른 게 얹혔다.`** One line only:
**`따라 하지 마.`** — inaudible to the creature, not on comms. Mid-brawl it
inverts to **`따라 해 봐.`**

**The line:** she reasons all the way to the right answer — `물러나는 게
맞고, 벽은 벽이고, 그러면 오늘 안 다치고 끝난다` — and **`발이 안 갔다.`**
To the second `물러서라` she answers **`싫어.`**, then: `이유를 대야 하는
자리에서 이유가 아닌 걸 댔다` / `그런데 다시 말해도 그 말이 나올 것 같았다.`
Three reasons in parallel, unjudged: `벽 뒤에 도시가 있고, 여기서 밀리기
싫었고, 물러나면 저것이 하는 대로 하는 게 됐다.`

### The unsealing itself

Canon (LOC-01 §4.1): contact location, pressure and joint load return through
**attenuated force feedback**; **in normal operation it is dull pressure and
load, not impact pain.** This chapter exceeds that ceiling. **Position was
always accurate — only the intensity changed**, seeded in scene 3:
`맞은 데에 느낌이 오는 건 원래 그랬다. 알라고 만들어 놓은 거니까.` /
**`오늘은 둔하지가 않았다.`** No mechanism vocabulary on the page
(**우회 신경동조 stays sealed until autumn**, §4.2).

> 울린다, 라고 부르려던 것이 부르기 전에 끝나지 않았다.
>
> **아팠다.**

Straight into action after — no commentary. And the close **generates EP71's
title**: `어디는 알았다. 가슴이었다. 원래 그렇게 오게 되어 있다. (…)`
**`알아야 하는 만큼만 오게 되어 있었는데.`** Then the user's addition —
**`"……아프잖아."`** Third instance, but a different kind: the first two are
narration; **this is the first time it leaves her mouth. She keeps Hyejeong's
rule eight months late, with nobody there to hear it.**

### Six user corrections, and one of them improved the fight

1. **Joint-reversal finish is spent** — it was the 농게형 결착 (EP47–48) and
   again EP64. Replaced with a **brawl**. **★ And the brawl became tactics**:
   the forelimbs *parry*, so — **`빗겨내려면 그쪽 다리를 써야 했다. 쓰는
   동안은 그 다리로 못 친다.`** The counter changes what she counts:
   `세지는 건 저 두 짝뿐. **저게 언제 늦는지만** 세고 있었다.` The left one
   lags half a beat. **The angry choice won**, which is what makes §1-I
   frightening. And she cannot stop on her own — she keeps hitting a corpse
   until **`"끝났다."`**, and `목소리가 들어오고 나서야 멈췄다는 게, 멈추고
   나서 알렸다.`
2. **Anatomy to life** — the gloss is the **carapace**; segments are plentiful
   but **hidden behind the two folded forelimbs**. **`저게 방패이면서
   무기였다.`**
3. **Scale from canon** — **EP19 has 「보폭 20미터」** verbatim. Facing
   distance **이백** (EP59 call-out register), wall at five strides,
   closing distance sixty = three strides.
4. **The seawall is where she pried barnacles off** (EP56), not built —
   `뗀 자리마다 둥근 테두리가 남았고 안쪽이 누렇게 삭아 있었다` /
   **`뗀다고 돌아오는 게 아니었다.`**
5. **Walking up is not new** (EP8 lobster, EP47 fiddler) — what's new is
   **it never accelerates.**
6. **Geometry** — Dana stands between it and the wall, so **the wall is never
   struck**; the demo is mid-air, and being pushed back *is* the wall getting
   closer.

### ★★ Sirens and drones — and the footage exists now

The user flagged that a creature walking in openly, this close to town, with
no alarm made no sense — especially three days after the school. Added: a
**long siren** (`짧은 건 대피고 긴 건 이동이었다`) and **broadcast drones**.
EP9's drone sentence was reused verbatim and **check_continuity caught it**;
varied into something better — **`봄에는 하나였다. / 오늘은 그 옆에 하나가
더 있다.`**

**★ FS-영상 is now open.** Her field of view had narrowed to two forelimbs;
the price is `아까 그 점 둘이 아직 있었다. (…) **중간에 한 번이라도 저걸
봤는지도 기억이 안 났다.**` **The brawl was filmed, including hitting
something already down.** This is the bridge between §1-E (opinion) and §1-I
(the will to win) — material for EP72–73.

### Checker gap closed

**`톡토기 무리` passed** — the taxa list held only `톡토기형`, so the bare
stem slipped through. Added stems: **톡토기 · 공작갯가재 · 딱총새우 ·
갯민숭달팽이 · 투구게**, with an in-code note on the ones deliberately
excluded (문어·집게·가재·농게·성게·크릴·갑오징어·가오리·**따개비**) because
they are ordinary words and would false-positive. EP66/68/69 regression clean.

**Precheck card updated**: `아프다` now unsealed but **not to be spread thin**;
`저림`·`욱신`·`쑤심` stay sealed **until EP72**; taxa names banned **with the
「형」 removed too**; joint-reversal finish marked spent; seawall/stride facts
added.

Next: **EP71 「그렇게 되어 있었는데」** (7/16 Sat night → 7/17 Sun) — opens
**immediately on return: hangar, before wash-down, still seated.** The
**설정값 항의** fires straight out of EP70's closing line: it was supposed to
come only as much as she needed to know. **Yeongjin does not answer. Sua has
no column to write it in.** Then it **crosses midnight** — she sleeps and it
is still there. **The chapter spanning two dates is itself the property of the
pain**: what used to end when the fight ended does not. Interval 3 gets
written here; **illness intensity begins its sharp rise.**

## EP71 approved (2026-08-17)

**EP71 「그렇게 되어 있었는데」** (`76_EP071_승인완료`, standard, 4,947 chars,
7/16 Sat night → 7/17 Sun morning) is `GATE_D_PASS`. State = **SNAP-071**,
tracker SNAP-071, ledger **v1.66**, calendar updated. S10 is **10/15** —
sub-arc ③ closes.

**The chapter spanning two dates is itself the event.** Everything
pain-adjacent used to end when the fight ended. This one is still there after
a night: **`전투는 어제였다. 어제 것이 오늘까지 온 적은 없었다.`**

### The protest, and the silence that answers it

It fires straight out of EP70's last line — she is still in the seat, hasn't
come down. Five statements, and what answers each is a **sound**: the hose
being uncoiled, the hose dragging, the water starting.

**★ The pressure point is the fourth:** `내가 잘못 기억하는 거야?` →
**`아니다.`** — the only answer that comes, **and nothing follows it.**
`잘못 기억하는 게 아니면 설명이 있어야 하는 자리인데, 설명 대신 물소리가
시작됐다.` Then `그렇게 되어 있었는데 왜 아파.` → the hose stops, one beat,
starts again. **`그게 대답의 전부였다.`**

**Author-side (zero on the page):** answering means either **lying** (blame
the machine) or **breaking the seal** (우회 신경동조, sealed until autumn).
He can do neither. **Do not have him answer this later.**

And she isn't angry: `화는 싸우면서 다 썼는지, 남은 건 화보다 무거운 다른
것이었다.` **`이름을 모르는 것이었다.`**

**Yeongjin's silence is not coldness** — the wash runs long, the jet lingers
in one spot, **the inspection starts at the chest plate** (it always started
at the arms), he pushes the beans across, he makes seaweed soup for someone
whose spoon only went to broth, and on Sunday morning the yard has tool noise
with nothing urgent in it — **`손을 어딘가에 두고 있는 소리였다.`**

### Sua — the confirmer, and two corrections

First draft had her **three pages behind**; the user rejected it —
**Sua does not fall behind.** Second attempt explained it away with night
battles; also wrong (most fights are daytime, and EP28 canon has her taking
the numbers directly with Dana signing off on her verification). Final:
`봄부터 하던 일이었다. 귀환하면 내려와서 수치를 받아 적고, 항목을 대조하고,
맨 아래 확인자 칸에 이름을 적는 것.` / **`하던 일을 하는 자리였다. 하던
일을 하는 사이에 보이는 것들이 있었다.`** **This is better for the
side-glance design** — she isn't there specially, she's where she always is,
so nobody (least of all Dana) can find it odd. **One retro line added to
EP70** so her presence needs no setup.

> **장부, 기체, 언니, 장부.**
> 장부에 있을 때가 제일 길고 언니에게 있을 때가 제일 짧았다.

She catches the grip held too long, the half-beat standing still, **the step
that breaks on the stair landing** — and **`본 것들은 어디에도 안 적혔다.`**
Checking off "외장 세척" early is cover: `손이 뭐라도 하고 있어야 눈이
자유로웠다.`

**The protest has no column.** Putting it under 특이사항 makes it *the
machine's*. **She does not add a column** — `만들면 기록이 되고, 기록이 되면
있었던 일이 된다. 있었던 일인 건 맞는데, 장부에 있을 일인지는 다른
문제였다.` The confirmer's signature covers only what can be confirmed:
**`확인 안 되는 것은 서명 바깥에 있었다.`** (User correction: **the interval
3 belongs to the table, not the ledger** — it gets written in scene 4.)

Closing: **a very small dot in the margin beside the empty cell.** `점은 칸
밖에 있었다. (…) 무엇이었는지는 점을 찍은 사람만 알면 됐다.` And from the
alley: **`똑같이 서 있는 집 안에 어제까지 없던 것이 하나 있었고, 그건 표에도
장부에도 없고, 점 하나로만 있었다.`**

### Craft notes

- **Date change with no scene break**, one sentence: `잠들었다 깨는 사이에
  날짜가 바뀌어 있었다.` No midnight timestamp.
- **Nothing is visible.** No bruise, nothing to the hand — `보이면 설명이
  되는 것이었다. (…) 안 보여서 설명이 안 됐다.` **`안에만 있는 것이었다.`**
- **The body learns caution in a day**, shown only as actions: washing the
  back first, leaning on the right shoulder in the elevator, carrying one
  dish with two hands, rice in soup, a **sequence** required to get up.
  **`몸이 알아서 하는 조심들이 하루 사이에 몇 개 늘어 있었다.`**
- **★ `알리다` was overused** (user): four instances of an unusual verb kept
  snagging. Kept **one anchor** at the meal (`가슴이 알려 왔다. 알라고 오는
  거라던 그것이…` — same word as EP70's protest) and varied the rest:
  `가슴이 따라왔다` (lying) / **`거기가 대답했다`** (checking in the dark) /
  `거기가 먼저 아니까` (the porch). **The name for it keeps changing, which
  matches the state.**
- Dialogue came in at **23.3%** against a 35–45% target. **Left it.** This is
  a chapter where the absence of an answer is the event; padding it would kill
  the design. Noted as intentional in the Gate-D memo.
- Phone call replaced by text — **`오늘 늦었다. 먼저 자`** / **`어`**.
  Hyejeong isn't reading anything into it: Saturday, a giant day, those days
  run late. **Second time this week the "every day" promise broke, and both
  times she couldn't say why.**

Next: **EP72 「연속」** (7/17 Sun, standard) — **illness intensity rises
sharply; scattered becomes continuous.** 열·저림·흐림. **★ `저림` and `흐림`
unseal here** (sealed through EP71). **Read as overwork and a summer cold** —
nobody connects it to the fights. **No school on Sunday, so all that's left
is: it's a rest day and it isn't getting better.** The setting-value question
stays unanswered.

## EP72 approved (2026-08-18) — the sisters have never been ill

**EP72 「연속」** (`77_EP072_승인완료`, standard, 5,299 chars, 7/17 Sun) is
`GATE_D_PASS`. State = **SNAP-072**, tracker SNAP-072, ledger **v1.67**,
calendar updated. S10 is **11/15**.

**Four things overlap in one day** — the chest, **37.4 fever**, **three bouts
of numbness in the left hand**, **one blurring of vision** at night.
**Every one of them has a separate explanation** (Saturday's hit, summer cold,
overwork, no sleep). `설명이 없는 건 하나도 없었다.` **Nobody stacks them.**

### ★★★ The chapter's biggest correction (user, in three stages)

1. Draft had `5월에 팔에 깁스` in her recall — **the cast is Seong-ho's**
   (EP24, crutches, announcing the diagnosis). Misattribution.
2. Replaced with `지난달에도 하루를 통으로 앓고` — also wrong:
   **EP61's "she's sick" was a lie to cover an absence.**
3. Then `수아가 감기에 걸리면 그랬다` — wrong too. **Sua likewise.**

**Canon now: neither sister has ever been ill.** Zero history of colds or
fevers, both of them. So the two-day rule is **borrowed from other people**
(Hyejeong, classmates), and:

> 단아는 아파 본 적이 없었다. (…) 지난달에 할아버지가 학교에 아프다고
> 전화한 날이 있긴 했는데, **그날은 아픈 게 아니었다. 아프다는 말을
> 그런 데에 먼저 써 버렸다.**
>
> **수아도 안 걸렸다.** 3학년이 되도록 감기 한 번을 안 했다. 겨울에 반이
> 통째로 앓아누울 때도 혼자 멀쩡히 다녔고, **그때는 그게 다행이라고만
> 생각했다.**

**★ That last clause is the seal's hinge** — the characters know the fact and
**do not find it strange**. The origin (the neural-sync lineage) stays sealed
until autumn, so nothing in the narration asks why. **Only the reader trips.**

**Two ironies fall out**: the girl who spent the word "sick" on a lie has
nowhere to spend it when it's true; and after telling Hyejeong `감기.` —
`감기라고 대답할 자격 같은 게 자기한테 있는지. 걸려 본 적이 없어서 이게
감기인지 아닌지도 모르면서, 제일 만만한 말을 꺼내 쓴 것이었다.`

**And there is nobody to ask**: `이 집에서 감기를 앓아 본 사람은
할아버지뿐이고, 할아버지의 감기하고 열세 살의 감기가 같은 건지는 알 수
없었다. **수아한테 물어봐야 수아도 모른다.**` — **"nobody connects it to the
fights" is no longer ignorance but structural impossibility.** The one person
who does know (Yeongjin) already failed to answer in EP71.

**→ Filed on the precheck card as §6-12-B** under the two-strikes rule
(EP24 misattribution, then the EP61 misreading).

### Unsealing 저림 / 흐림

**Lineage corrected (user):** the first instance is **EP69 Thursday** (Narae's
pencil), not yesterday — now stated on the page. The unsealing:

> **목요일에는 잡았다고 생각했는데 안 잡혀 있었다. 오늘은 잡기 전부터
> 알았다.**
>
> **저렸다.**

Three bouts stack, and **the third comes while she is doing nothing** —
`뭘 하려던 것도 아닌데 오는 건 처음이었다.` Counting creates the continuity:
`세어진다는 건 오는 간격이 있다는 뜻이었다` / **`간격을 세는 건 수아가
표에서 하는 일이었다. 자기 손에 대고 그걸 하게 될 줄은 몰랐다.`**
Why she can't go to a doctor: Sunday, low fever, and the hand is fine *now* —
**`보여줄 게 없는 몸을 들고 갈 수는 없는 일이었다.`**
Blurring is one beat after the call, edge of the phone screen, two blinks.
**No collapse, no blackout.** Counts: 저리다 2, 흐리다 1, 아프다 3 (the extra
one is *history* — "never been ill" — not a naming of present pain; noted in
the Gate-D memo).

### ★★ Hyejeong gets there first

Kindergarten-long friendship is the instrument:

> 「너가?」 / 「왜.」 / **「너 감기 걸리는 애 아니잖아.」**
> 유치원 때부터 같은 반이었고, 같은 겨울을 여섯 번쯤 났고 (…)
> **못 본 걸 세고 있었던 것도 아닌데 안 봤다는 건 알고 있었다.**
> 「걸렸어.」 / 「진짜?」 / 「진짜.」
> **한 박자 있었다.**
> 「……여름감기 오래간다?」

She names it exactly, Dana insists, she backs off — **and the half-beat and
the ellipsis stay.** What's left on her side isn't shown (Dana's POV);
**EP73 collects it.** The new setting is thus verified twice on the page: once
in narration, once by an outsider's mouth.

Other fixes: **`안 물었다` relocated** to just after the Yeongjin exchange, so
there is now a chance to ask that she doesn't take — `둘밖에 없었고, 시간도
있었고, 물소리도 없었다` (yesterday the water covered it; today nothing does);
`불기 전에 차렸어야지`; `세 끼니째`; **`아픈 건 어제부터다`** (Saturday);
`안 셌어`; `왼손은 요즘 무리해서고`.

**The house nurses her without anyone calling it that** — the shop stays shut
on a Sunday it usually half-opens, the table softens 미역국→국수→죽,
**김가루 on the porridge** (`환자 밥이 아니라 그냥 맛있는 밥처럼 보였고`),
dishes cleared from her side first, **a fresh cup moved to her right hand**,
`뭐 필요한 거 있냐`, the thermometer set within reach instead of away, and
**a goodnight through the door that Sua never gives.**

Closing: she counts the four, then — `겹쳐 보려면 넷을 한 줄에 놓아야 하고,
한 줄에 놓으면 시작점이 보이고, **시작점은 넷 다 같은 날이었다.** /
**거기까지 가기 전에 멈췄다.**` And her own deadline: **`내일 아침에 안
나았으면, 그건 감기가 아니다.`** The morning is not shown.

Next: **EP73 「안 보인다」** (7/18 Mon, key chapter, interval **2**) —
갑오징어형 stealth fight, inside the harbour. **She goes out sick**: the
deadline arrives in the morning and **the fight arrives first**.
**★★ At the same hour Hyejeong comes to the house** — nobody home, **the
hangar open**, **something she must not see. Two things are hidden.**
EP72's half-beat is what moves her: they said 「내일 봐」 and Dana didn't come.

**Casting debt for the last five chapters:** military axis is booked for EP76;
**Ki-tae is at gap 11** and **Bae Jeongho at 62** (the only unresolved one from
the EP65 census). **EP74–75 are the only windows.**

## EP73 approved (2026-08-18) — first Hyejeong POV, and the anchor punches through

**EP73 「안 보인다」** (`78_EP073_승인완료`, **key chapter**, 5,728 chars,
7/18 Mon) is `GATE_D_PASS`. State = **SNAP-073**, tracker SNAP-073, ledger
**v1.68**, calendar updated. S10 is **12/15** — sub-arc ④ closes, and the
**interval sequence 6·5·4·3·2 is complete.**

**The title covers both lines**: in the harbour the creature can't be seen; at
the house something that must not be seen is.

### The structure was rebuilt at the user's correction

Draft had Yeongjin driving out to the cordon because the inner harbour is a
sensor blind spot, emptying the house. **Wrong** — canon is that the Titan's
feed is **shared to the hangar screen**; he stays underground.

Confirmed instead: **when she sorties, the whole family is underground, and
from down there nobody knows who comes to the surface.** The house has always
been enterable unnoticed; **today was the first time a door stood open.**

**★★ And the door is open because of her body.** Morning order: Yeongjin down
first → Sua off to school → **Dana last, and she forgot to shut the iron
door.** One daily motion dropped because of illness, and **that one dropped
motion is what Hyejeong sees.** The illness *causes* the B-line — not
coincidence, a price. On the page the forgetting is **not narrated when it
happens**; the descent is listed and the door is simply missing from the list.
It comes back in scene 6: **`기억이 안 나는 게 대답이었다.`**

### A-line

**Camouflage is learned by being hit** (user correction): first there is
nothing, she circles looking deeper, **it comes from the side**, and turning
back she finds a dock pillar — **`기둥 옆에 기둥 색이 하나 더 있었다`** /
`움직이니까 보였고, 멈추니까 다시 없어졌다.` Spring lineage:
`숨어 다니는 상대는 봄에 점액을 뿜던 긴 놈뿐이었다. **그때는 적어도 관 속에
있다는 건 알았다.**` → **`항 안의 모든 것이 낯설게 보였다`** — "plenty of
cover" flips into "everything is suspect."

Buoys corrected: **they do not resolve shapes**, only that something passed,
and only after it passed — and they're seeded seaward, so once it's inside
they have nothing left to say.

Body penalties throughout: buckle slipping from the left hand, **two half-beat
anchor delays**, **one blurring mid-aim**, shallow breathing, slow turns —
`지금 되는 것과 필요할 때 되는 것이 다르다는 걸 알면서 출발했다.`
Break: `보는 것을 그만두니까 보였다` — reading the water's disturbed grain
(no reuse of the stillness insight).

**★★ Avoidance of close range appears for the first time**: `가까이 가서
끝내는 그림이 먼저 그려졌다. 그려지는데 **가슴이 싫다고 했다**` /
**`아는 몸은 처음이었다.`**

**★★ The anchor punches through** (user-specified): `사출, 하강, 그리고
점화` / `거리가 가까워 가속이 충분할까 하는 생각이 잠시 들었다` →
**`걸리라고 쏜 것이었다. 걸리지 않고 허공에 멈췄다. 로켓 불꽃이 터져
나오고 잠시 후, 앵커는 갑작스레 그 자리를 그대로 통과했다.`**
The reason — deepened sync from EP70 — is **zero on the page and unknown to
her**. What remains is bewilderment: **`앵커는 거는 물건이었다. 봄부터
그랬다. 걸고, 감고, 박고. 뚫은 적은 없었다.`** Yeongjin's non-answer sits in
the answer's place: `뚫리는 거였어?` / `……` / **`고생했다. 나와라.`**
The creature is only visible **as it dies.**

### ★★★ B-line — the first Hyejeong POV in the series

Her narrative register: **the girl who doesn't make lines has a line make
itself.** `혜정은 줄을 안 만드는 애였다 (…) **오늘은 줄이 저절로
만들어졌다.**` The word "worry" never appears — `앉아 있는 게 안 됐다`
(mirroring Dana's `발이 안 갔다`).

She **skips school in the morning** (moved from after-class, per the outline's
"at the same hour"): `감기래` lands twice from Kim Juho, **`감기요?`** escapes
her first, Yejin comes over from the middle row and bounces off it — **only
Hyejeong can't move past it.** **She leaves her bag and doesn't file for early
dismissal — the first rule she has ever broken.** The convenience-store bag is
**the form of a visit used to explain her own truancy to herself.**

**★★ House blocking rebuilt against LOC-05** (user caught it): the iron door
is **not in the yard** but at the end of the narrow passage beside the
workbench, inside the shop. Route: **back garden (plot, laundry line)** →
calling → no answer → **the sliding door half-open** (the sortie's trace) →
setting the bag on the porch edge and, standing up, **seeing straight through**
→ room into shop → **the passage and the open iron door.** She **takes her
shoes off** to step up; the shutter is down even from inside so it's dark at
midday, and **the spanners hang in size order on the tool wall**. At the
threshold: a freight-sized lift, **the indicator pointing down**, and
**`이 집 밑에 뭔가 있었다`** — that is the entire reach (no giant, no
equipment, no identification). **`들어가면 알 수 있을 것 같았고, 알 수 있을
것 같아서 안 들어갔다.`** On the way out she **moves the bag from the porch to
the door handle** because it shows better there — set beside `아무것도 안
만졌고 아무것도 안 옮겼다`.

Also corrected: seating (**Hyejeong window row, Dana/Yejin middle** since
EP69), so Yejin comes over rather than speaking from behind.

### The crossing

The bag, lukewarm. The iron door clanging shut. Yeongjin **knows from the
order who left it open and doesn't ask.** Dana can't reply because
`고맙다고 보내면 왔다 간 걸 아는 게 되고, 왔다 간 걸 알면 집이 비어 있던 걸
아는 게 된다.` → **`봉지는 왔는데 말이 안 왔다.`** And:
**`반쪽짜리 앎이 식구 수만큼 있었다.`** Sua stops in front of the shut iron
door for no reason (`멈춘 이유는 본인만 알았다`), writes **2**, and
**`다음 칸이 가리키는 숫자를 수아는 적지 않았다.`**

check_continuity caught three more: a `계단` slip (single-storey house), a
verbatim EP71 line, and a self-duplicate.

Next: **EP74 「덮는다」** (7/19 Tue) — containment. **The family doesn't know
what Hyejeong saw, and Hyejeong doesn't know what she saw.** Reach stays at
**equipment level, zero identification.**
**★ Casting alarm: EP76 is booked for the military axis, so EP74–75 are the
only windows left for 기태 (gap 12) and 배정호 (gap 63).**

## EP74 approved (2026-08-18) — nobody reaches the truth

**EP74 「덮는다」** (`79_EP074_승인완료`, standard, 4,930 chars, 7/19 Tue) is
`GATE_D_PASS`. State = **SNAP-074**, tracker SNAP-074, ledger **v1.69**,
calendar updated. S10 is **13/15**.

**Three subjects do the covering**: the family covers the fact that a door
stood open (no meeting, no mention), Hyejeong covers what she saw (executing
EP73's `아무 데도 안 꺼내기로 했다`), and the body covers pain with routine
(`이틀 빠지면 무슨 일 있냐가 된다`). **Nobody reaches identification** —
this is not an exposure chapter but one where **people shield each other
without knowing what they're shielding.**

### Seong-ho points at the answer and skips past it

EP73 was filmed (user-confirmed: alarm-then-harbour, two drones since EP70).
He frame-counts the punch-through and states the anomaly precisely —
`쟤가 원래 뚫는 물건이 아니거든. 처음 나왔을 때부터 내가 다 봤는데 건 적밖에
없어. (…) 그런데 뚫었단 말이야.` — then closes it: `업그레이드했겠지.
봄부터 계속 세지고 있어. 내가 표로 만들어 봤는데—`

**`틀린 설명이 제일 가까운 설명이었다.`** Once it explains, nobody asks
again. **This is how the arc stays undetected.** **Do not correct him later.**
There is a vertical line drawn in his table where "before and after differ" —
**he and Sua are watching the same thing with different instruments and
neither knows.** Against Narae: `성호가 프레임을 세는 동안 나래는 선을 긋고
있었다. (…) 정작 그 장면 속에 있던 사람은 둘 사이를 지나서 자리에 앉았다.`

### The bag conversation, and Yejin reading the gaps

「잘 먹었어」/「어」/「죽도」/「어」 — and the reason it's short is on the page:
`길게 하려면 언제 먹었는지가 나오고, 언제 먹었는지가 나오면 언제 받았는지가
나온다.` From Hyejeong's side: `어디 갔었냐는 말은 봄부터 안 하는 애였다.
오늘 안 하는 건 봄의 그것과 같은 모양인데 무게가 달랐고, **무게가 다른 걸
아는 사람은 이 교실에 둘뿐이었다.**` One crack at the shoe rack:
**「몸조리 잘해.」**, said to the shoe rack rather than to her.

**★ Yejin knows by absence, not by words** — `끼어들 데가 없이 대화가
끝났다. (…) 오늘은 얹을 데가 없었다.` /
**`뭔지 모르는 채로, 뭔가라는 것만 알았다.`** No conclusion, no probing.
**This is the charge for EP75's bridge role.**

### ★★★ Ki-tae: speech levels corrected (gap 12 closed)

First draft had the two adults on **mutual 반말**; user: `사람이 너무
달라졌다`. EP61 canon: **Ki-tae speaks up to Yeongjin** (`거의 다 쓰셨네`,
`이건 그냥 무게로 하죠`, `그럼 저희가 손해인데요`), Yeongjin uses 하게체
(`고철로 하게`, `그러지`), and **to Dana he is casual and calls her 「조수」**
(`어이, 조수.` / `살아 있네.`).

Scene 3 rewritten, and the entry order flipped — **「어이, 조수.」 reaches
the porch first**, then the adult business starts, because Dana is this
house's first face to him. Second correction: **delete the price talk** —
the winch and generator are **the ones Yeongjin agreed to fix in lieu of
scrap payment back in EP61**. `셈이 이미 끝난 일이라, 오늘은 부품이 왔다는
것만 새 일이었다.` **This lands on the theme**: settled with Ki-tae,
newly unsettled with Hyejeong. Parts talk became practical —
**`부품이야 맞춰 넣으면 돌아가게 돼 있네`**, the same register as the door
he fixes that evening. Barley tea drunk **leaning, not sitting on the porch**,
looking into the shop — and **`철문 쪽도 지나갔는데, 지나가는 눈이었다.
벽을 보는 눈과 문을 보는 눈이 다르지 않았다.`** Exactly where Hyejeong stood
still yesterday. **→ Filed on the precheck card's speech matrix.**

### ★★ The self-closing door

Instead of a lock or an unspoken new rule, **he fits a closer so it shuts even
if forgotten**: **`사람을 고치는 대신 문을 고친 것이었다. 누가 안 닫았느냐를
따지면 안 닫은 사람이 생긴다. 문이 저절로 닫히면 안 닫은 사람이라는 게
없어진다.`** Dana pulls the handle instead of apologising (`혼자 미안하다고
하면, 그건 잘못한 사람이 있었다는 걸 만드는 일이 됐다`). Sua, who stopped in
front of that door yesterday, **doesn't stop today** — `안 멈추는 게 오히려
걸음에 티가 났다` — and at dinner says **「편하겠네요.」** rather than "why"
(user correction: asking why demands an answer, and **nobody in this house
demands answers**). `편하지.` **Both dodge the real reason and arrive at the
same place.**

Closing: a **tteokbokki date for the last day of term** (with Yejin) —
`갚는다는 말은 안 붙였다. 붙이면 뭘 갚는지가 나오니까`; the call where
**`안 꺼내는 게 저쪽에도 있는 것 같은 통화는 처음이었다`**; and
**`덮는 게 지키는 거랑 같은 말이 되는 집이 있었다.`**

Next: **EP75 「묻지 않는 쪽」** (7/21 Thu) — **Hyejeong's self-blame**,
**Yejin's bridge role** (charged in EP74), **EP61's `그럼 됐어` collected**,
and **Dana is ill with nowhere to say it again.**
**★★ Bae Jeongho (gap 64) — EP75 is the last window**; EP76 belongs to the
military axis.

## EP75 approved (2026-08-18) — the circle of 「그럼 됐어」 closes

**EP75 「묻지 않는 쪽」** (`80_EP075_승인완료`, standard, 5,119 chars,
7/21 Thu; Wednesday summarized in one line) is `GATE_D_PASS`. State =
**SNAP-075**, tracker SNAP-075, ledger **v1.70**, calendar updated. S10 is
**14/15**. **The summer cast-loss debt is fully cleared** — 우진 (EP67),
나래 (EP69), and now **배정호 (gap 64, EP75)**.

### The EP61 line comes back with the speakers reversed

Canon: EP61, Hyejeong's instant reply `그럼 됐어. 필기 다 해 놨으니까 걱정
말고.` and the residue `그 말이 제일 걸렸다.` This chapter: at the windows
after cleaning, Hyejeong starts `저번에—` and folds it herself —
**`아니다.`** (the EP67 lineage; user fix — `그럼 됐어` can't answer an
unfinished `저번에` directly). Then:

> **늘 혜정이 접고 단아가 모른 척 넘어가는 순서였다.**
> **이번에는 넘어가는 대신 받았다.**
> **「그럼 됐어.」**

No awareness in the act (`말할 수 있는 것 중에 제일 짧은 게 그거였다`), and
then two months arrive: `그럼 됐어는 안 물어보겠다는 뜻이었다. (…) 배려인
동시에 **안 듣겠다는 뜻이기도 했다.**` The symmetry lands clean —
`정확히 같은 이유로 정확히 같은 문을 닫았다. / **닫히는 쪽에서는 그게
어떻게 들리는지, 이제 알았다.**` Hyejeong answers `……어.` and the narration
never names the sound of a door closing.

### Yejin per the voice card (user correction)

I had written `예진은 원래 말이 많은 애` — the card says the opposite:
**she is the only character whose sentences lengthen in conflict; length IS
the buffering.** Fixed to: `예진은 평소에 말이 긴 애가 아니었다. (…)
**오늘 예진이 계속 말하고 있다는 것 자체가, 예진이 뭔가를 느꼈다는
뜻이었다.**` — and Hyejeong likely noticed and played dumb out of gratitude.
She swaps the cleaning trio with zero explanation, talks the whole time so
the two silences don't show, and asks exactly one thing at the shoe rack:
`진짜 괜찮아?` / `어.` / `그래.` —
`모르는 채로 안 묻는 것과 알면서 안 묻는 것이 오늘 신발장 앞에 나란히
서 있었다.`

### Bae Jeongho — the fisherman's instrument (two user corrections)

1. **No water discoloration** — G0-011: dissolution is *loss*, nothing
   remains to tint the water.
2. **He knows about the fight** — it was daytime, public, alarmed, on the
   news. `왜 그런지 모른다` was impossible.

Final shape — **a difference only someone who knows the fights can measure**:

> 「월요일에 그, 항 안에서 한판 했지 않습니까.」 (no hesitation — the whole
> town knows)
> 「싸움이야 봄부터 봤으니까 그러려니 하는데. **고기가 사흘째 안
> 돌아옵니다.**」
> 「봄에는 안 그랬어요. (…) **물고기가 미련해서, 놀라도 금방 잊어요.**」
> 「**사흘째 빈 바다입니다.**」

**★★ The spring/summer shift (§1-A) gets its first external confirmation —
measured by fish.** And Dana's unsayable thing #4 becomes *what changed*:

> 봄의 그것들과 여름의 그것들은 다르게 왔다. **잡으러 왔던 것들과 부수러
> 오는 것들.** 그 차이를 단아는 몸으로 알았고 수아는 표로 알았고, **이제
> 물고기들도 아는 모양이었다. 사람 중에 그걸 말로 하는 사람만 없었다.**

The §1-A top-level ban (never explain the shift in dialogue/narration) holds;
this paragraph is the arc in miniature. **New standing rule: characters may
not be ignorant of public battles** (alarms + broadcast).

Three adults, three ways of not-seeing: Ki-tae's passing glance (EP74),
Jeongho **not looking around at all** (`둘 다 아무것도 못 봤는데 못 본
방식이 달랐다`), and Hyejeong who looked (EP73).

### Closing

The three questions gather: `좀 어떠냐, 체육 하지 마, 몸조리 잘해.` →
**`누구도 안 물어서 못 하는 게 아니었다. 물어 줬는데 못 하는 것이었다.`**
Vacation arithmetic: nobody will ask for forty-some days —
`그게 편할 거라고 생각했다. **편할 거라고 생각한 게 오늘 제일 안 좋은
생각이었다.**` Sua finishes the spring notebook (3/2–5/18, two months of
copying), **empty cells carried over as empty** (`봄의 자기가 안 적은 것을
여름의 자기가 지어내서 채울 수는 없었다`), and has nobody to tell —
**`이 집에는 말 안 하는 사람이 하나씩 더 늘고 있었다.`**

Next: **EP76 「방학」** (7/22 Fri, **key chapter 5,800 — S10 finale**) —
graduation-day assembly by classroom broadcast; **military axis ③ (§1-H):
the evacuation notice text actually changes**, from coastline-based to
**`미확인 대형체 인근`-based** (hand-off to S11); **명준·윤서진·오미란 ●**
(gap 10); the tteokbokki promise kept (혜정·예진); and **the vacation arrives
with her body still wrong → S11 「꺾임」.** The cheer of the last school day
against the state of her body closes the arc.

## G0-015 approved (2026-08-18) — flood chronology and place-name tiers

A user observation ("sea level rise is still ongoing") turned into a canon
consolidation. **Nothing about the enemy changed — the two facts are
deliberately unlinked.**

### Chronology

**대수몰** (the Great Submergence) drowned the **old downtown** — this is where
수몰역 / 수몰 도로 / 수몰 화물부두 sit, and where the underground launch line
(G0-007) runs. **Afterwards the 방재벽 was built to the worst-case forecast**,
which means that at the time **there was still dry land and a village outside
it** — the wall was drawn with margin. **Five years ago the water reached that
limit line and the remaining outside strip was fully evacuated.** Not a
disaster; closer to an administrative procedure — the water simply arrived at
the line someone had already drawn.

**★ Which means there is no margin left.** The wall is now the water's edge,
and by design **there is no next line to fall back to.** Nothing in the
approved chapters changes, but everything about the wall gets heavier
retroactively: barnacles eating it (EP55–56), something climbing over it
(EP68), something already inside the harbour (EP73).

**The gap between 대수몰 and five years ago is deliberately undefined.**

### Place-name tiers

| Referent | Military/admin | Residents |
| --- | --- | --- |
| everything underwater | 침수구역 | 물 밑 |
| old downtown (대수몰) | 수몰 구도심 | **구도심** |
| strip evacuated 5 yrs ago | **소개지구** | **벽 바깥** |
| that village's old name | — | **하구래** |

**하구래** is the fishing village below 구래동, outside the wall — the name
alone shows the two were once one place. **Residents never say 소개지구; they
say 벽 바깥.** Geography: wall → 소개지구 (old 하구래) → 수몰 구도심 —
**two empty layers**, and the creatures come across both.

**오미란 is from 하구래**, evacuated five years ago. This is **not yet on the
page and must not be revealed without approval** — a one-line origin, not a
relationship line or a secret (G0-005 background-cast rule holds). It does
recolor an existing approved line for free: EP65's `오 년 전에 저런 게 왔으면
크레인만 접혔겠어요?` is now **a woman who emptied her own village saying it**,
with no text change. Same for EP76's `오 년 전을 기억하는 사람들은 웬만한
일에는 웃을 수 있는 모양이었다`.

### Retroactive fix (EP21 — one line)

EP21 and EP22 named the same location two ways: EP21 called it `오 년 전에
버린 동네` while EP22 calls it `구도심`. Since the downtown drowned in the
대수몰, that clashed. **Fixed by deleting the timestamp only:**
`오 년 전에 버린 동네였다.` → **`버린 동네였다.`** (The next sentence is
`버린 동네의 지도는 갱신되지 않는다`, so the repetition actually improves it.)
**Grep-verified: `오 년 전` now appears in exactly one place, EP65's 미란** —
so five-years-ago means the evacuation and nothing else.

### Page rules — internal setting

No chronology, no figures, no exposition. When it surfaces at all it is
**half a line from an adult, as temperature rather than explanation.**
Children, Dana and Sua included, know it as "the way things are."
**Never tie the water to the creatures**: the sea has been rising for
decades, the creatures started the year before last, and **nobody in the
story connects the two — there is no reason to.**

`check_continuity` now watches 소개지구 / 하구래 / 대수몰 and flags `오 년 전`
as a soft check against pointing at the wrong event.

## EP76 approved (2026-08-18) — S10 closes, summer arc complete

**EP76 「방학」** (`81_EP076_승인완료`, key chapter, 5,034 chars, 7/22 Fri) is
`GATE_D_PASS`. State = **SNAP-076 (S10마감)**, tracker SNAP-076, ledger
**v1.71**, calendar carries the vacation block. **S10 「통증과 균열」 is
complete at 15/15 — and with it the whole summer block (S8·S9·S10,
EP41–76).**

### Two endings cross

Above ground the term ends — broadcast assembly, report cards, tteokbokki,
cheerful. In the 남방사 지휘통제실 a record becomes a regulation: what EP65
**started writing down** changes the evacuation notice three months later,
from coastline-based to **`대피 시 해안 및 미확인 대형체 인근을 피해 이동`**,
and goes out to citizens and every school's parent-notice bundle the same day.
`넉 달 걸려 표에 오른 이름이 반나절 만에 온 도시로 퍼지는 것을, 적기 시작한
사람은 특별하게 여기지 않았다. **문서는 원래 그렇게 돈다.**`

**★★★ The paper and the child ride home in the same bag and nobody connects
them.** The one person who could: `저 여섯 글자가 누구 얘기인지 아는 사람은
이 교실에 자기뿐이라는 것까지 생각하고, 거기서 접었다. **종이도 생각도.**`
She files it in **her own drawer**, not the room where Sua's chart lives.

### Myeongjun stays light (user directive)

Directive: `봄쪽 보면서 명준이 너무 무거워지지 않도록`. The voice card is
**공적 언어와 사적 투덜의 이중창** — so: public `기준이 하나 느는 거다`,
signature, then the mutter — **`정체도 모르는 걸 안내문 기준으로 삼는 군대라.
짬밥 먹은 이래 이런 결재는 처음이군.`** Then his own three questions across
the seasons: `봄에는 저걸 잡을 수 있냐고 물었지` / `여름에는 저걸 적어야
하냐고 물었고` / **`이제 저걸 피해 다니라고 시민들한테 안내를 하는군`** →
**`결론을 낼 계제가 아니라는 게 결론이었다.`** Defence by humour, never by
weight. (User fixes: `오 년을 입었는데` → `짬밥 먹은 이래` — five years is
too short for a brigadier; 남방사 지휘통제실; citizens notified alongside.)

### ★★ Seojin's third omission (EP5 · 65 · 76)

`인근이 몇 미터입니까. 현장에서 물어볼 겁니다.` /
**`정할 수가 없다. 저것이 어디 설지를 모르는데.`** / `그럼 반경 없이
갑니까.` / `반경 없이 나간다.` — **`서진은 그것을 적지 않았다. 반경이
없다는 것은 문서에 적을 수 있는 종류의 사실이 아니었다.`** A radius-less
standard ships to every school. In the corridor: `기준 자체가 움직이는 것인
안내문은 처음이었다.` **This is where S11's checkpoints start.**

### The rest

Report cards are **elementary 3-tier** (매우잘함/잘함/보통, by domain — user
fix; no ranks or scores): `나 왜 수와 연산이 보통이야?` / **`니 수행평가
점수를 봐라.`** / `꼴찌 아니야. 세 개 중에 세 번째지.` — Yejin's comfort
isn't comfort and Hyejeong takes it as comfort anyway. Hyejeong is **herself
only at that table** (`봄부터 알던 혜정`). **No daily-call promise** —
`꺼내면 못 지킬 걸 셋 다 알았다` — just a dateless `또 보자` and her
imperative returning: **「방학이라고 연락 끊지 마.」** / `안 끊어.` →
**`지킬 수 있는 것만 약속하는 사이가 됐다.`** One crack: laughing until her
chest follows, so she **halves the laugh** — `소리는 끝까지 내고 숨만 얕게
바꾸는 요령` — and nobody sees.

Miran (gap 11) gives iced sikhye and `할아버지한테 전해라. 어민회에서
고맙다고` / 「크레인이요?」 / **「크레인도 그렇고.」** — `다음이 없는 게 이
동네 어른들의 화법`. Seong-ho plans forty days of observation
(**`안 나온 것도 기록이야`** → `세는 애들은 학년이 달라도 같은 말을 했다`).
Sua rules a line under the interval column and **the chart loses an eye** —
`방학에는 결석이 없다` / **`그 눈이 혜정 언니였다는 걸 수아는 몰랐고,
알았어도 표에는 적을 데가 없었을 것이다.`**

Close: `방학은 시작하는 날이 정해져 있고, 끝나는 날도 정해져 있다. /
**이건 시작한 날은 아는데, 끝나는 날이 없었다.**`

### ★★ S11 「꺾임과 검문」 entry state (locked)

- **Vacation 2050/7/23–8/31 (40 days), school resumes 9/1**
- Dana: symptoms unchanged at day seven, cause unknown, **no baseline of her
  own to compare against**
- **The observation window closes** — no school means no absence signal;
  Sua's chart runs on buoys alone
- Hyejeong holds what she saw in silence; her `아니다` is multiplying
- A **radius-less standard** is now in citizens' hands — field questions will
  come
- Seong-ho's forty-day plan; **his wrong explanation (`업그레이드`) stands**
- **★ Design against G0-015**: the seawall is the worst-case line with **zero
  margin left** — that changes what a checkpoint on it means
- Held back, unpublished: 하구래 / Miran's origin, why the anchor punched
  through, the unanswered config question, the sisters' lack of illness

## Arc capsule S10 written (2026-08-18)

`05_문체_상태_인계/Black_Titan_아크캡슐_S10_v1.0.md` — S10 「통증과 균열」
(EP62–76, 6/29–7/22) in the S1–S9 capsule series. One-liner: pain enters the
body and a witness enters the house, **and both fail to become words before
vacation arrives** — while a name that took four months to reach a chart
becomes regulation in half a day and is delivered into that child's bag.

Key locked content: entry→exit state table (7 axes), 7 irreversible events,
knowledge-movement table (who knows what, and that Seong-ho self-sealed with
`업그레이드`), thread carry-over with **S11 design constraints**: Dana starts
at day seven and breaks to **nerve damage / no-sortie mid-S11** (confidence-arc
memory), the school observation window is closed (neighborhood/market/harbor/
Harang's yard are the substitute cast windows; 배유림 gap-48 recovery via the
Sua axis), G0-015 zero-margin wall recontextualizes checkpoints, and all
standing seals hold. **Next: S11 「꺾임과 검문」 Level 3 skeleton.**

## S11 outline approved (2026-08-18) — 「꺾임과 검문」 EP77–92

`02_여름편_기획/Black_Titan_S11_EP077-092_화별개요_v1.0_승인.md` is
**LEVEL4_PASS**: **16 chapters, 7/23 Sat – 8/19 Fri** (all weekdays verified
against the real 2050 calendar). One-liner: the body breaks and gives up its
seat, the younger sister who takes it is too good at it, and a checkpoint line
tightens around the house that hides them both.

**Sub-arcs:** ① 방학의 모양 77–79 (vacation opens; **EP78 = overtraining
collapse** — the pressure is all on-page (broken school, notice in the bag,
enemies that come to destroy), spring's training-schedule descriptions return
as an in-story fact (no time to train all summer), and the REAL cause is
**boarding accumulation** while everyone — Dana, Yeongjin, Sua — settles for
"she overdid it": the `업그레이드` fallacy happening inside the house;
author-level only, page 0) · ② 자리 80–82 (**EP80 grounding order; EP81
lobster-remnant appears, Dana is half-conscious, Yeongjin can't decide — and
Sua appears wearing the gym clothes**, the canonical sortie outfit since
spring, resolve shown by clothing before words → consent after conflict;
instant-response anomaly sealed as "calibration") · ③ 가시 83–87 (the
stutter curve: **EP83 cone-snail-type** — harpoon-grade spines that knock you
down, but the anchor answers at range, short win that looks like recovery;
EP84 relapse + barb 1; EP85 ray-type, Sua's trajectory-math zenith; EP86 life
chapter at Harang's yard, **배유림 recovered**; **EP87 sea-robin-type, the
series' FIRST fish** — walks on fin-rays, swallows-to-crush, won by punching
out from inside, shallow-water staging preserves the no-underwater seal —
brutal win, re-break confirmed) · ④ 검문 88–90 (Hyejeong tails once and sees
military-grade equipment; uncle consult; **the radius-less standard from EP76
becomes the administrative basis for the Gurae-dong checkpoints**; the shop
search is barely covered; **no confirmation — only dread**) · ⑤ 91–92
(**krill-type: the military's first win via high explosives** — Myeongjun's
resolve toward the E-phase seizure; close: the army won and the house is worse
off → S12 「여름방학 마지막 날」, twelve days to school).

**Roster rule (user): every enemy carries one distinct threat** — lobster
claws / harpoon spines / flight / swallowing / swarm. Level-5 carryovers:
sea-robin scale (at G0 shape-lock), EP78 training details, checkpoint
procedure. All standing seals hold, including instant-response cause and
Myeongjun↔Yeongjin no-meeting.

## EP77 approved (2026-08-18) — S11 opens

**EP77 「첫날」** (`82_EP077_승인완료`, standard, 4,941 chars, 7/23 Sat) is
`GATE_D_PASS`. State = **SNAP-077**, tracker SNAP-077, ledger **v1.72**,
calendar carries the vacation chapters. **S11 「꺾임과 검문」 is 1/16.**

### Getting better and not being reassured, in one body

She sleeps all day as planned and **improves** — measurable things only: rice
goes down without soup, the walk from room to porch is short. Everyone reads
it as sleep and vacation: `잠이 일을 한 것이었다.` **★★★ Author-level seal:
the real reason is five days off the machine** (last sortie 7/18). **Zero page
explanation** — readers reconstruct it backwards from EP78–79. This is the
first button on the boarding-accumulation thread, and it is what makes EP78's
"she overdid it" survivable as an explanation.

### The unease is about order, not length (user correction)

The draft said a five-day gap was unprecedented since spring. **Interval
arithmetic disproves it:** battle days **6/29 · 7/4 · 7/9 · 7/13 · 7/16 ·
7/18** → gaps **6·5·4·3·2**, so six- and five-day gaps existed in early
summer. Corrected to:

> 닷새가 긴 건 아니다. 여름 초에는 엿새도 있었고 닷새도 있었다.
> **긴 게 문제가 아니라, 순서가 문제였다.** (…)
> **줄어들던 것이 늘어난 건 처음이었다.**

This lands better because it matches Sua's chart logic exactly — `저 빈칸에
들어갈 숫자는 이미 5를 넘겼고, 그러면 규칙이 깨진 게 된다. **규칙이 깨진 건
적을 데가 없었다.**` **Three people sense the same break through three
instruments** (unwitting resonance intact): Dana by body (`부표 소리를
기다리고 있었다` — she corrects herself to "preparing," and the body does the
same thing anyway), Sua by chart, Seong-ho by notebook (leafing backwards:
`줄어들던 것이 늘어난 게 언제 이후 처음인지, 아니면 아예 처음인지`).
Tension phrased as `쉬는 날을 받으면서 이자가 붙는 기분` and a silence that
became `출제 범위를 안 알려 주는 시험`. **Battle-day list and the "heatwave
started early-to-mid July" fact are now canon (calendar doc).**

### The heat is two weeks old; what's new is her vantage (user correction)

Rewrote every "summer started today" beat. The AC repair rush has been running
for days — `그걸 오늘 처음 봤다. **평일 낮에 가게에 있어 본 게 오랜만이라서,
이 가게가 요즘 이렇게 바쁜 줄을 몰랐다.**` The same move repeats three times
(tin-roof smell, Yeongjin's hands — `저녁에 돌아와서 보는 건 하루가 끝난
손이지, 하루가 밀리는 중인 손이 아니었다` — and the evening hose), which
turned into the chapter's grammar: **vacation isn't new things appearing, it's
seeing what was already there.** One observation window closes (the outside
eye on Dana) and another opens (her eye on the house).

Also: she works the intake desk (`순서대로 해 드려요` — Yeongjin's own line),
and **heavy work is removed by task assignment, never by prohibition**; a
customer drops **「조용할 때 고쳐 놔야지」** about a fan, which doesn't only
sound like a fan; Sua already has a timetable (Harang's yard Mon/Wed/Fri from
7/25 — **EP86 warm-up**) while Dana's vacation is still blank; the call covers
**only the plan** for the valley (user fix — she hasn't gone), Hyejeong picks
**the lightest available reading** of `목소리가 낮네`, and `그럼 됐어` appears
once in a place where it snags on nothing.

Close: `서른아홉 밤이 남았다. / 바다는 닷새째 조용했다. / **조용한 날을 세는
사람이 이 집에 둘이었다.**`

### Ledger note

**Vacation closes the school window.** 우진·나래·한결·주호 have no natural
venue until 9/1 — widening gaps are **correct**, and forcing appearances would
read false. Live venues: house, hill (Seong-ho's 40 days), phone, market,
harbor, 인양장 (Ki-tae owes a day's wage in tteokbokki, EP74), and **Harang's
yard — where 배유림 (gap 49) is to be recovered at EP86.**

Next: **EP78 「무리한 훈련」** (7/25 Mon) — pressure (broken school, the notice
in the bag, enemies that come to destroy, **plus the broken interval rule**)
→ **spring's training schedule restored** (summer had no room for it because
fights were frequent — recovered as in-story fact) → overtraining → she can't
get up. **The real cause is boarding accumulation, but "she overdid it" is the
one explanation that fits that day, so all three settle for it.**

## EP78 approved (2026-08-18) — the overtraining collapse

**EP78 「연습」** (`83_EP078_승인완료`, standard, 5,151 chars, 7/25 Mon) is
`GATE_D_PASS`. State = **SNAP-078**, tracker SNAP-078, ledger **v1.73**.
**S11 is 2/16.**

**The training, re-sited (user fix):** the flooded-station platform only
allows in-place drills (ceiling and pillars — which retroactively explains why
spring training WAS in-place drills). `다음. 나가자.` → through the watertight
bulkhead to the standing point and the **old reclaimed flats** — wide, empty,
unseen at night; Yeongjin sets a time limit from the start. Night outings are
not new — **the anchor-practice nights precede this** (user fix): `그때는 배울
게 있어서 나왔고, 오늘은 잊지 않으려고 나왔다.`

**Stage 3 is the mantis-shrimp shadow-fight** (user addition): her feet pick
the spot before her head does (`발이 기억하고 있었다`), the logic is `아팠던
걸 다시 하면, 다음에는 덜 아플 것 같았다`, and `한 세트 더` ×3 because a
fight with no opponent has no way to be won (`모자란 데가 자리를 옮겨 가면서
계속 하나씩 있었다`). Violence made visible: the night sea splitting, moonlight
shattering, mud booming underfoot — and Yeongjin straightening in his chair.
He cuts it at the third `더` and spends the night on `내가 늦게 끊었다`,
in repairman's terms: `멀쩡한 소리는 멀쩡하다는 증거가 아니라 아직 안 났다는
소리일 뿐` — known for forty years at the bench, forgotten in front of people.

**The bucket of sweat (user addition)** is the physical evidence: gym clothes
stuck to her back though her hands never left the controls (`몸은 다 뛴 것으로
치고 있었다 (…) 몸은 속지 않았다` — phenomenon only, zero mechanism), a towel
half-soaked, the wet clothes left on top of the laundry as next morning's
proof. Crash comes one beat late: fine on landing, then the spoon slows, a
knee buckles, she's asleep before finishing dinner, and **Sua finds her
unresponsive to shaking** — takes off her glasses (user detail), leaves the
phone by her pillow: **one missed call from Hyejeong** (`오늘 못 받은 쪽은
안 끊겠다던 쪽이었다`).

**★★★ The "she overdid it" consensus** — real cause is boarding accumulation
(page 0); each of the three arrives by their own logic (Yeongjin's guilt,
Sua's `언니는 원래 한 세트 더 하는 사람`, Dana's own verdict deferred to EP79
since she slept through it). **The classroom's `업그레이드` fallacy now has
its in-house twin, and the narration corrects neither.** Readers hold the
EP77/EP78 pair — six days off = recovery, one boarding = collapse — and are
the only ones with the right answer. Sua's version doesn't quite close:
`무리했네, 로 정리한 칸에 다 안 들어가고 조금 남았다` — **the leftover
fragment she decides to carry** (it will grow). Her checkup-and-ledger routine
runs even for training (user fix): inspection done, 비고 「훈련」, and the
interval chart untouched — `장부에는 적히고 표에는 안 적히는 날` /
**`적히는 것과 괜찮은 것이 다른 날이 있다.`**

Canon added: flooded-station drill limits; reclaimed-flats training ground;
training triggers the checkup/ledger routine; gap comparison must use SUMMER
maxima (spring gaps were longer — user fix): `엿새면 여름 들어 제일 길었던
공백과 같아졌다. 내일이면 넘는다.`

Close: `준비를 했는데, 준비가 줄어든 것 같은 밤이었다.`

Next: **EP79 「악화」** (7/26 Tue) — she stays down; **"overdid it" arithmetic
fails for the first time** (overdoing heals with a day of rest); vacation
means nobody outside knows; Sua (home on Tuesdays) watches her fragment grow;
Dana's own `무리했나 보다` gets spoken and then shaken; the missed call gets
answered somehow; **Yeongjin's night ends in the grounding decision** → EP80.

## EP79 approved (2026-08-18) — the explanation expires

**EP79 「하루로 안 끝난다」** (`84_EP079_승인완료`, standard, 4,873 chars,
7/26 Tue) is `GATE_D_PASS`. State = **SNAP-079**, tracker SNAP-079, ledger
**v1.74**. **S11 is 3/16 — sub-arc ① complete.**

**The chapter runs on the shape of the excuse:** overdoing it heals in a day.
So the morning holds (`무리했나 보다` is *reassuring* — `이유가 있는 건
무서운 게 아니었다`, with the stiff salt-dried gym clothes as proof), and the
evening cracks: `무리했으면, 오늘쯤은 나아져야 하는 거 아닌가` →
**`그 생각을 도로 눕혔다. 하루 더 자면.`** Never said aloud. She can't reach
the intake desk, so **Yeongjin says `순서대로 해 드립니다` again** — the seat
went back to its owner in one day. Vacation means nobody outside notices.

**★★★ Sua gets closest.** Her observations rule out a cold (no fever, cough,
or runny nose — `감기의 표시가 하나도 없는데 감기보다 더 안 움직였다`), the
one-day math fails (`이틀째는 무리가 아니었다. 그럼 뭔지는 적을 데가
없었다`), and she arrives at: **`싸워서 이렇게 된 게 아니었다. 안 싸운 동안
이렇게 됐다.` / `이상한데 틀린 데가 없었다.`** The spring rule (bad day
follows a fight) fails for the first time — `이번에는 표에 아무것도 없는데
언니가 저랬다`. **The blinded chart pays off here.** She acts only with her
hands (barley tea, fan angle, three half-built questions) and tells nobody.

**★★ New: the half-message.** From the user's `「어, 수아한테 들었어.」` —
Sua answered Hyejeong for her sister last night and **wrote only `자고 있다`,
deleting `무리했다`, and can't explain why, then or now.** So **Hyejeong's
information is half** — EP88–90's investigation will run on a deficit. Three
people not saying things, plus one trimming what she passes on:
`밖에서 보면 그냥 조용한 집이었다.`

**★★ Yeongjin decides** (announcement is EP80): the repairman's order —
`원인을 못 찾으면 더 안 돌린다. 그게 순서다. (…) **사람 앞에서만 그 순서를
자꾸 미뤘다.**` The hospital card closes (spring's clean re-exam:
`나오면 안 되는 것이 있어서 못 보여 주는 쪽`). Every reason to reverse the
decision turns out to be `전부 남의 집 일`. **`다음 경보에는 안 내보낸다.`**
Then he doesn't switch off the console: **`안 내보내면 그다음이 있어야 했다.
그다음이 뭔지는 아직 안 봤다. 안 본 게 아니라 안 보고 있었다.`** — readers
already know EP81's answer is singular.

Hyejeong's last call before the valley (7/27–28, mountain signal uncertain)
asks only `요즘 잠이 많네, 너` — half a step, where spring-Hyejeong asked
three times. `방학이잖아` is now used as a **shield** rather than an answer.
Sea silent seven days — a new summer maximum.

Close: `무리했다는 말은 하루짜리 말이었다. / **그 하루가 오늘로 끝났는데,
이 집에는 그 말을 대신할 말이 없었다.**`

### Style management (new)

`셈` was running 6–7 times per chapter (EP77, EP78) — a tic of mine, flagged
by the user. EP79 now uses **0** (replaced with 앞뒤 / 헤아리다 — and
`앞뒤가 맞는다` actually suits this chapter's theme better). **`셈`,
`그러니까`, `어차피` are now in `check_continuity`'s TICS list** (WARN at 3+),
and the precheck card caps `셈` at 2 per chapter with a replacement set
(계산·산수·앞뒤·아귀·이치·헤아리다·따지다·순서·짐작·말이 된다). The word is
still usable — just mixed, not defaulted to. **Retroactive cleanup of EP77–78
is deferred** (user will decide later).

Next: **EP80 「정지」** — the grounding is announced to both sisters; Dana's
protest and helplessness; the buoys are not quiet; **Hyejeong is away in the
valley while the house breaks** → EP81, Sua's first sortie in the gym clothes.

## EP80 approved (2026-08-18) — the grounding

**EP80 「정지」** (`85_EP080_승인완료`, standard, 5,576 chars, 7/27 Wed) is
`GATE_D_PASS`. State = **SNAP-080**, tracker SNAP-080, ledger **v1.75**.
**S11 is 4/16.**

**The wording was settled with the user: 「당분간」, not 「다음 경보에는」.**
EP79's private resolution was event-shaped, but the repairman logic in the
same chapter (`원인을 못 찾으면 더 안 돌린다`) is duration-shaped — so the
night's work is that **a one-time call turns out not to fit once he has to
say it out loud.** At the breakfast table, subjectless: **`당분간 안
나간다.`** / `얼마나.` / **`모른다.`** He can't say "until you're better"
because **there is no standard for better** — cause unknown. Dana's protest
dies in two moves, three ways over: her `나 괜찮아` is disproved by her own
voice, `그래` refuses to argue (agreeing changes nothing), and
`오면 그때 생각한다` admits there is no plan. And **neither answer helps her**
— `아프지 않다고 하면 거짓말이 되고, 아프다고 하면 안 나간다는 쪽을
도와주는 말이 됐다.` She folds 「당분간」 down to "just skip the next one"
to make it bearable; it unfolds at night.

**★ Silence loses its meaning (user correction).** My draft had the quiet
lengthening the grounding — wrong, since 「당분간」 runs regardless of alarms.
Corrected: `조용해도 안 나가고, 울려도 안 나간다. (…) **세는 버릇만 남고
셀 이유가 없어졌다.**` **The three read the same eight days differently:**
Dana = no meaning (excluded from waiting), Sua = **reprieve** (`나오면 그때부터
물어야 할 게 생긴다` — grateful and frightened), Yeongjin = **untested**
(his decision hasn't been challenged yet). This cashes in the "body looking
seaward" motif built across EP77–79.

**★★★ The unasked question.** `그럼 누가 나가.` reaches her throat at the
table and is swallowed; at night the real reason arrives — **she thinks she
knows the answer**: `말이 되면 생각할 수 있는 것이 되고, 생각할 수 있는
것이 되면 언젠가 하게 되는 것이 된다. / **물어보면 대답이 되고, 대답이 되면
진짜가 된다. / 그래서 아무도 안 물었다.**` Sua's half of it: `그 말은 언니가
하면 반발이 되고 자기가 하면 다른 게 됐다` — **carried in her mouth all day,
neither put down nor said.** **EP81's premise is now complete: the answer
nobody spoke walks in wearing gym clothes.**

**★★ Yejin's call (user addition)** — three academies, the shuttle, and
`엄마가 방학이 기회래. **매년 그래.**` (user edit: making it an annual
routine, so it carries no weight and Dana has no opening). Listening is
*easy*: `편해서 좋았고, 좋은 게 이상했다. (…) **자기 얘기를 할 자리가 안
생기니까.**` The check-in comes as the shuttle arrives — `그냥 있어` /
`부럽다, 진짜` → **`선택이 아닌 그냥 있음은 부러운 게 아니었다.`** And the
EP75 lineage inverts: **`말할 자리를 못 찾은 게 아니라 안 찾은 거였다.`**
Closing three lines: `예진이는 원래 잘 알아채는 애였다. **최근에도** 화요일에
한 번, 신발장 앞에서 한 번. **그런데 지금은 셔틀이 왔다.**` →
**★★ Both outside eyes close in the same week** (Hyejeong in the mountains,
Yejin on the shuttle) — the observation window is now failing person by
person, not just school-wide. **This is the groundwork for EP88's delayed
discovery.**

Also: at breakfast only Dana has nothing to contribute (`할 일이 없는 사람은
아침에 할 말도 없었다`); Yeongjin can promise a repair date but not the other
thing (`모레.` / `확실하오.`); `아무것도 안 했어` / `그럼 됐다` →
`목표라는 게 없어졌다`; and how the order becomes law — `반박 없이 하루를
넘긴 말은 그다음 날부터 규칙이 됐다.`

**Word-lifespan trilogy complete:** EP76 `끝나는 날이 없었다` → EP79
`무리했다는 말은 하루짜리 말이었다` → EP80 **`당분간은 끝나는 날이 없는
말이었다`**, closing on `끝을 모르는 것 두 개가 서로를 붙들고 있었다.`
(`셈` tic held to 1 use.)

Next: **EP81 「그다음」** (7/28 Thu) — the lobster-remnant surfaces, Dana can't
get up, **Yeongjin cannot decide** (the man who knows the risk, handless at
the console), and **Sua appears in the gym clothes**; consent after conflict,
then her first sortie (terrain / chain / anchor-trajectory math, with the
short reaction lag accepted as calibration, cause sealed). **Note Hyejeong
returns from the valley the same day** — placement to be settled in the brief.

## EP81 approved (2026-08-19) — Sua's first sortie

**EP81 「그다음」** (`86_EP081_승인완료`, key chapter, 5,876 chars, 7/28 Thu)
is `GATE_D_PASS`. State = **SNAP-081**, tracker SNAP-081, ledger **v1.76**.
**S11 is 5/16.**

### ★★★ 보정값 is a fiction — canon restored (user correction)

Context loss had me writing Yeongjin *changing calibration values*. **There
is no such thing as a calibration value.** EP2's "the values are set to Dana"
was **an excuse to keep Sua out of the cockpit** — an in-family + in-reader
device only. **Filed as precheck-card 12-C and a `check_continuity` hard rule
(`보정값을 바꾸/되돌리/조정` → FAIL), which immediately caught a leftover I'd
missed.** Never stage value manipulation.

**The catch is what ISN'T said.** Yeongjin refuses with human reasons only —
`너는 어려` / `열 살이에요` / **`열두 살도 어렸다`** (a reply that slips out
closer to regret than argument) / `운동신경도 언니만 못하고`. Then:

> **`보정값 얘기는 안 하시네요.`** (his hand stops on the console)
> **`봄에는 그것 때문에 언니만 된다고 하셨는데.`**

`진짜로 보정값이 문제라면 그 말이 제일 먼저 나왔어야 했다. (…) **안 나온
말이 제일 큰 말이었다.**` / **`거짓말이었네요, 라고는 하지 않았다.
말하지 않아도 그 뜻이 됐다.`** — no accusation, no edge (Sua tone guard).
Yeongjin's side: `봄에는 위험하다는 말을 애한테 할 수가 없어서 기계 얘기를
했다. 오늘은 기계 얘기를 쓸 수가 없어서 나이 얘기를 했다. **댈 수 있는
이유가 처음부터 끝까지 핑계뿐이었다는 게, 핑계가 떨어지고 나서야 드러났다.**`
**Consent is staged as touching nothing** — he never opens a values screen,
just runs the launch sequence, and **Sua notices that nothing was changed.**

### ★★★ The instant-response problem answers itself

The user asked how to sell Sua's *better* reaction with a fake explanation.
The answer: **nobody needs selling.** Sua has no baseline (first ride, thinks
it's normal), Dana never sees the numbers, and Yeongjin — the only one who
knows — is the most silent person in the house.
`대답을 만들 필요가 없다는 게, 오늘 이 방에서 제일 무거운 일이었다. (…)
**봄에 만든 것이 하나 있었고, 오늘 낮에 그게 수명을 다했다.** 새것을 만들
자리는 아직 안 왔고, **오는 날이 안 왔으면 좋겠다는 것까지가 오늘의
생각이었다.**` (This runs on a separate line from the boarding-accumulation
thread.)

### Canon added

- **Sleep-learning is common to both sisters** — verified against EP2, where
  **Sua herself explains it** (`언니, 자기 전에 듣던 거. (…) 경고음 뒤에
  순서 외우는 거`). So `저도 같은 걸 들었는데요` now does double duty: the
  basis for her catch, and why her hands know the procedure.
  **The anchor is NOT in sleep-learning** (recent equipment — learned by
  watching Dana practice).
- **Anchor operating sequence:** left-stick two-stage switches (release lock →
  launch) → drop → **rocket ignition** → winch recovery. `팔이 늘어난다고
  생각해라` is inherited secondhand from EP60.
- **Comms use plain double quotes** — 「」 drift eliminated (the EP68 lesson).

### The fight

Flooded-downtown avenue, **knee-deep** (no-underwater seal holds), under a
half-collapsed overpass (8 piers). She copies Dana's style, thinks
`저걸 흘리면 된다`, and **fails** — `화면으로는 안 보이던 것들이 다 들어
있었다` (water gripping the feet, weight shifts, pressure half a beat before
the move) → **`언니는 이걸 다 몸으로 알고 있었던 것이다.`** One body hit,
then the pivot: **`눈이 지나가는 대로 지형이 머릿속에 적혔다. 표에 적듯이.
지도를 그리듯이.`** Lures it under the overpass, anchors the cracked third
pier, **drops the deck on it** (thousands of tons; knee-deep water surges to
mid-calf), then — `모기 한 마리 잡는 것도 주저하던 수아였지만` … `언니와
할아버지, 하랑이, 도시의 알고 있는 모든 사람들이 위험하다. **그 생각이
수아의 등을 밀었다**` — puts the anchor **dead center in the head socket.**
**No punch-through** (contrast with EP73 — an indirect index of sync depth,
never explained). Sensation: **`떨리는 손과 정확한 눈이 한 몸에 있었다`**,
frightened and nauseated, **and her body feels light** —
`가벼운 게 뭔지는 생각하지 않기로 했다` (unnamed; deepens in sub-arc ③).

Around it: Dana can't stand when the alarm sounds (`일어나지지 않는 몸으로는
반박이 안 됐다`) and says **`조심해`** — `말리는 말이 아니라 보내는 말이었다.
말해 놓고 나서야 자기가 방금 동생을 보냈다는 걸 알았다`; her `잘하더라` comes
with a face that `안심만 있는 얼굴은 아니었다` (**EP82 seed**). `잘했다`
arrives on day one because there was no chance to hoard it. Sua signs **both
the inspector and the pilot line** of the ledger and writes **9** in the
interval column. Yeongjin saves the log rather than deleting it —
`지우면 오늘이 없던 일이 되고, 저장하면 다음이 있다는 뜻`.

Close: `그럼 누가 나가, 라고 아무도 묻지 않았다. (…) **물은 사람이 없는데
대답이 먼저 나와 버렸다.**`

Next: **EP82 「같은 장면」** (7/29 Fri) — relief and inferiority sharing one
scene for Dana; pride and a **hidden pleasure** for Sua (still unnamed);
Yeongjin's guilt at what his protection has made; and **Hyejeong's first call
since the valley — on half information.** Then sub-arc ③ 「가시」.

## EP82 approved (2026-08-19) — two feelings each, one admitted

**EP82 「같은 장면」** (`87_EP082_승인완료`, standard, 4,680 chars, 7/29 Fri)
is `GATE_D_PASS`. State = **SNAP-082**, tracker SNAP-082, ledger **v1.77**.
**S11 is 6/16 — sub-arc ② complete.**

Each of the three replays yesterday and carries away something different:
Dana admits relief and not inferiority, Sua admits pride and not pleasure,
Yeongjin admits necessity and not guilt.

**★★★ Dana's `내가 없어도 되는구나` cuts both ways** — this is the chapter's
real find: `내가 없어도 되면 안 나가도 된다. 안 나가도 되면 아파도 된다.
아파도 되는 자리가 생기는 건 이번 여름 내내 없던 일이었다. /
**놓여나는 것과 밀려나는 것이 같은 문장으로 왔다.**` She watches alone
because `셋이 같이 보자는 말을 아무도 안 꺼냈기 때문`; the footage runs
`저건 나였다` (the copied stance, and it hurts to watch it get hit) →
**`저건 내가 아니었다`** (the scanning eyes) → the overpass drop, which she
replays twice and still can't picture herself inventing: `나는 부수는 걸
몸으로 하는데, 저 애는 재서 한다.` EP81's `잘하더라` comes back as
`진심이었다. 진심이 아닌 것도 조금 섞여 있었다.` And: `표는 표고 싸움은
싸움이었다. / **어제 표가 싸움이 됐다.**`

**★★ Sua now has two things she doesn't measure** — the lightness
(`떠올리면 지금도 조금 그랬다` / **`왜 안 세는지도 안 셌다`**) and the fact
that killing didn't leave a mark (`남지 않는 게 이상한 건지 아닌지도 수아는
재지 않았다. **오늘 안 재는 것이 두 개가 됐다**`). Pride, by contrast,
`셈이 되는 감정이었다`. Harang catches it — `수아 오늘 기분 좋아 보여` —
and the late `아니야` **is not an answer and she knows it.** At breakfast she
notes there's no column for sortie counts: `나가는 사람이 하나면 몇 번
나갔는지가 곧 그 사람 얘기였다. **둘이 되면 달라진다.**`

**★★★ The cockpit modification (user correction).** I had him fitting the
seat *to Sua* — that would make it **hers alone**. Corrected to **widening the
adjustment range**: rail extended two notches, two extra belt-lock holes.
`**되돌릴 수 있는 조정이 아니었다.** (…) **이 조종석은 오늘부터 두 사람
자리였다.**` The guilt sharpens accordingly — `뺏는 거면 차라리 나았을
것이다. **늘린 것이었다**` / `막을 수 있었던 사람은 나뿐이었는데, 지금
자리를 하나 더 만들고 있는 것도 나다.` He can't stop working because
`어긋난 자리에 애가 앉는다`, and `유일하게 할 수 있는 게 그것뿐일 때 사람은
그걸 사랑이라고 부르기도 했다`. Test run: `큰애 자리에서 작은애 자리까지
한 번에 갔다가 한 번에 돌아왔다. / **잘 됐다. 잘 된 게 제일 나빴다.**`
(Canon: cockpit is now 2-person capable; **never stage person-specific
fitting**.)

**★★ Hyejeong's return call runs two days behind.** She's bright about the
valley, says `이틀 동안 세상이 안 돌아간 것 같았어` (**`세상은 돌아갔다`**),
and asks **Tuesday's question** — `너 이제 좀 괜찮아?` — because all she has
is Sua's one-line text. Dana's `어, 괜찮아` is double: her body IS better
(she hasn't sortied), but **`괜찮은 게 좋은 일이 아닌 상태가 있다는 걸 지금
알았다. 나가지 않아서 나아지는 몸을 괜찮다고 말하면, 그 괜찮음은 안 나가는
것에 붙어 있는 괜찮음이었다.`** Hyejeong stalls at `목소리가 좀 이상한데`
because `이상하다는 느낌만 가지고는 질문을 만들 수 없었다`, the tteokbokki
invitation is declined without a reason (`그 규칙을 만든 게 자기라는 걸
단아는 알고 있었다`), and the deficit gets measured: `저쪽 달력은 아직
화요일에 있었다` → **`이틀치가 아니라 넉 달치였다.`**

Small: Yeongjin sets the soup down **in front of Sua first** (it was always
Dana, since spring) and Dana sees it; Sua's stiffness is explicitly marked as
normal (`이유가 있는 아픔과 이유가 없는 아픔은 같은 자리에 와도 다른
것이었다`); Dana avoids looking at the cockpit. `check_voice` caught a speech-
level error in my draft (an unattributed Sua line reading as Dana using
honorifics to her grandfather).

Close: `같은 장면을 셋이 다시 봤다. / **가져 나온 게 다 달랐고, 가져 나온
걸 아무도 말하지 않았다.**`

Next: **sub-arc ③ 「가시」 (EP83–87)** — EP83 Dana's first comeback fight
(cone-snail type, harpoon spines, **won short at anchor range** so it looks
like recovery) → EP84 relapse + first barb → EP85 ray-type (Sua's second) →
EP86 Harang's yard (**배유림 recovered**, second barb) → **EP87 sea-robin
type: swallowed, punches out from inside, brutal win, re-break confirmed.**

## EP83 approved (2026-08-19) — the comeback that looks like one

**EP83 「돌아온 것처럼」** (`88_EP083_승인완료`, standard, 5,524 chars,
8/3 Wed, with 7/30–8/2 compressed) is `GATE_D_PASS`. State = **SNAP-083**,
tracker SNAP-083, ledger **v1.78**. **S11 is 7/16 — sub-arc ③ begins.**

Six days off the machine and she is genuinely better — kitchen and back
without resting, intake desk, a full bowl, and **she starts counting again**
(counting is the recovery signal; you stop counting when you're bad). The
soup bowl goes back to her first. Hyejeong hears it too: `너 목소리 돌아왔네`
/ **`지난번엔 물에 만 목소리였어`** — recovery confirmed by someone else,
tteokbokki penciled in for next week. Author-level: it's the **non-boarding
accumulation** again (last ride 7/25); on the page it's "rest" and "a summer
cold that passed."

**The grounding lifts on its own terms.** The buoy sounds and her body starts
spring's sequence **without stopping**, so `"내가 갈게."` arrives after the
body has half-proved it (the inverse of EP81). Yeongjin has six days of data
and admits `당분간`에는 출구가 필요했다, setting one condition —
**`"길어지면 끊는다."`** — without defining how long, because defining it
would delay the launch. **Sua doesn't put on the gym clothes**; she takes the
monitor seat with the checklist and says **`"조심해."`** — handing back the
word her sister gave her six days ago. `자리라는 건 이렇게 오가는 것이었다.`

### The sniper (user concept) and the ricochet (user addition)

A seamless cylinder half-buried in mud, immobile; **the shell lifts at the
bottom, a barrel comes out, one shot, and it closes.** Velocity staged as:
`그걸 봤다고 생각한 순간에는 이미 맞아 있었다` → **`맞고 나서 소리가
도착했다. (…) 가시가 지나온 궤적을 따라 뻘과 물이 줄지어 솟구쳤다`** (user
edit adds the spear bouncing off her chest, spinning through the air, landing
in the mud). It **ricochets off armor but buries itself in a tetrapod** and
punches the wreck's hull like paper.

**★★★ Her textbook answer fails:** she times the reload gap, fires clean,
and **the anchor skates off** — `"둥글어서 그렇다. **어디를 맞혀도 비스듬히
맞는 거다."**` → `둥근 것에는 정면이 없었다. (…) **힘이 모자란 게 아니라
각도가 없는 것이었다.**` Sloped-armor physics in the characters' own words,
and the cover keeps shrinking while she works it out — **short fight, but not
an easy one.**

The rule that solves it: **`열리는 걸 보고 쏘면 늦는다. 열리기 전에 쏴서,
열릴 때 도착해야 했다. / 앵커가 나는 시간과 저쪽이 여는 시간. 두 개를
겹치는 싸움이었다.`** June's urchin fight comes back (user fix — that was
June, not spring): `같은 흐름이었다. 답만 달랐다. **그때는 틈에 달렸고,
지금은 틈에 쏜다.**` **Canon fix: the anchor is FIRED, never thrown** (lock
release → launch → ignition, per EP81); the log reads `쏜 건 두 번이었다.
한 번은 튕겼고 한 번은 박혔다.`

### ★★★ Three warnings for the reader only

1. **The déjà-vu:** `운동하고 난 개운함이랑 같은 계열이었다` (deliberate
   EP78 reuse — the checker flags it, it stays) plus **`이 개운함을 어디서
   느껴 봤는지는 생각하지 않았다. 좋은 감각에 출처를 묻는 사람은 없었다.`**
2. **Why the fight was short:** she reads it as her body being back; the
   reader sees **zero close-quarters exchange = low boarding load.**
3. **Yeongjin stops one inch from the answer:** `길이와 다음 날 사이에 무슨
   관계가 있는 것 같기도 했는데, **오늘은 좋은 날이라 그 생각을 오래 붙들지
   않았다.**`

Also: Dana re-affirms her own method (`수아라면 쟀을 것이다. (…) **자기
것으로 하는 게 맞았다**` — a quiet answer to EP82's inferiority); Sua has
been silently counting her sister's recovery (`나아지는 걸 말로 짚으면
나아지는 게 멈출 것 같은, 근거 없는 조심성`), crumples the checklist when
Dana is hit, and gives the win away — **`조심하라고 해 준 덕분이다`** (user
edit). Her drawer of unnamed things is now three deep: **`열면 한꺼번에
보이는 물건이었다.`** A calendar check caught my error on vacation days
remaining (twenty → **twenty-eight**).

Close: `돌아온 것 같았다. / **같았다, 까지가 오늘 말할 수 있는 전부였다.**`

Next: **EP84 「이틀」** (8/4–5) — **the recovery doesn't last two days →
relapse** (first trough of the stutter curve); **the price of that
open-feeling comes due** (EP78 → EP83 → EP84); **`길어지면 끊는다` proves
useless because short fights do it too**; and the first barb, from Sua's
side, in the tail of a sentence only.

## EP84 approved (2026-08-19) — the excuse runs out

**EP84 「이틀」** (`89_EP084_승인완료`, standard, 4,686 chars, 8/4–5) is
`GATE_D_PASS`. State = **SNAP-084**, tracker SNAP-084, ledger **v1.79**.
**S11 is 8/16.**

Thursday morning is fine — she even sets a date with Hyejeong (`정할 수 있다는
건 그때까지 괜찮을 거라고 생각한다는 뜻`). By lunch the spoon slows (the EP78
curve, third reuse), the nap makes it worse, and Friday is spent lying down,
back at exactly the 7/29 baseline. **This time there is no "she overdid it."**
She runs her grandfather's diagnostic method — `되는 것부터 지우고, 남는 데를
본다` — and erases overwork, cold (no fever), sleep, heat, food, ending
**empty-handed**. EP79 inverts: `이유가 있는 건 무서운 게 아니라고 지난주에
생각했었다. / **이유가 없는 게 이런 거였다.**` →
**`이유가 없으면 대책도 없었다. (…) 아무것도 할 게 없는 것이었다.`**
The open feeling from EP83 finally snags: **`개운했다가 그냥 무너지는
것이었다.`**

**★★ Hyejeong breaks the shield.** `방학이라 그래` fails for the first time
(`방학은 지난주에도 방학이었어`), and the cold excuse dies on **`열은?`** /
`없어.` / **`열 없는 감기가 어디 있어.`** — `봄에는 세 번 물었고 요즘은 한
번 묻는데, **한 번 물을 때는 대신 정확한 데를 물었다.**` She still can't
push further (half information), but **EP88's investigation is now fully
primed.** Dana notices her own arithmetic doesn't work — four days until
Tuesday when the last recovery took six — `안 맞는 걸 알면서 화요일에 보자고
했다`.

**★★ The first barb.** Sua's care is flawless (`어제 것보다 묽게 했어.
넘기기 편하라고` — and per user edit, this caretaking is an **old role**:
she covered for her scatterbrained sister whenever their grandfather was ill),
and then, at the door: **`언니는 쉬어. 나가는 건 내가 하면 되니까.`**
She hears her own tail half a beat late — `나쁜 뜻이 아니었다. (…) **그런데
나쁜 뜻이 아니라고 하기에는 어딘가 들떠 있었다**` — the **first leak of the
unnamed pleasure**. Then she builds the sequence explicitly (sister sick → I
go out → the feeling comes again) and **looks away from it**: `못 본 척하는
것도 안 재는 것의 한 종류였다.` Dana receives it with a late `고마워`
(`늦은 만큼이 들었다는 뜻`) and lands on: **`그 말이 틀린 말이 아니라는 게
제일 걸렸다. 틀린 말이면 아니라고 하면 된다. 맞는 말이라서 고맙다고 해야
했다.`** She doesn't call for the porridge to be reheated — a second sentence
like that would hurt more.

**★★★ Yeongjin loses his only handle.** Two log lines (long training →
next day; short fight → two days later). The common factor is there but
**`그게 뭔지 말로 안 만들어졌다. 너무 당연한 것들은 원래 이름을 안 붙이고
지나간다.`** Then: `길면 끊으면 된다고 생각했다. / **짧았는데 왔다.** (…)
**남는 건 태우느냐, 안 태우느냐.**` And every option is a child — elder,
younger, or **`남의 집 애라고 부르는 순간 셈이 아주 나빠졌다`** (user fix:
it's **the seawall** that breaks, not the harbor — G0-015's zero-margin line).
**★★★ And the real reason he can't reach the cause surfaces:**
`타는 것 자체가 문제라면.` → **`그게 문제면 지금까지 태운 넉 달은 뭐가
되는가.`** — **it isn't logic blocking him, it's what the answer would cost.**
Fatigue from an alarm-less night arrives before the thought finishes.

Also: a wordless dinner where all three are silent for different reasons
(nothing to say / nothing to log — `짧았는데` / `말하면 셈이 시작되는데 셈의
끝이 안 보여서`); Sua pulls out blank paper for a new chart and puts it back
(**`모르는 걸 적는 표는 만들 수가 없었다`**); Yeongjin at the shutter —
`언제부터 안 나왔는지를 세어 보려다가 그만뒀다`.

Close: `돌아오는 데 엿새였다. / 무너지는 데 이틀이었다. / **다음에 돌아오는
데는 며칠이 걸릴지, 그건 아무 데도 적혀 있지 않았다.**`

Next: **EP85 「사거리」** (8/8 Mon) — ray-type, airborne; **Sua's second
sortie and the peak of her trajectory math** (measuring space instead of
terrain); **reaction lag shortens further** (cause still sealed); the physical
lightness deepens, still unnamed; Dana watches from the monitor again.

## EP85 approved (2026-08-19) — the bomber comes down

**EP85 「사거리」** (`90_EP085_승인완료`, standard, 4,845 chars, 8/8 Mon) is
`GATE_D_PASS`. State = **SNAP-085**, tracker SNAP-085, ledger **v1.80**.
**S11 is 10/16.**

**★★ The buoys stay silent (user fix).** Airborne approach = the buoy
system's blind spot: `부표는 울리지 않았다. (…) 오늘은 사이렌뿐이었다.
**물을 지나오지 않고 오는 것이 있다는 뜻이었다.**` Yeongjin: `처음인 것은
늘 준비 밖에서 왔다.` Canon: buoys are water-only; airborne contacts arrive
via siren/public net first. Sua's chart inherits the same blind spot.

**The handover happens in silence.** Dana gets to her elbows and no further
(`시도한 걸 아는 사람은 이 방에 자기뿐이었다`); gym clothes, launch sequence,
monitor seat — no argument at all. `한 번 있었던 일은 두 번째부터 순서가
됐다.` / `지난번에는 내가 갈게, 라는 말이라도 했다. **오늘은 그 말이 성립을
안 했다.**` Yeongjin runs the sequence with the answer still unmade: `손은
머리보다 먼저 결정을 내리는 물건이었다.`

**The bomber fight (user concept, aquarium-observed).** High circling out of
anchor range (one ranging shot confirms it), then bombing runs: **drum-sized
hardened lumps poured out in streams**, wind-roar then mud columns in
salvos. Her first dodge is by instinct (`언니 방식은 자기 몸에 없었다` — and
terror from above has nowhere to hide). Then the pivot: `떨어지는 건 빨랐다.
그런데 **떨어지기 시작하는 건 보였다.**` / **`저쪽의 높이가 저쪽의
약점이었다`** → the scatter pattern repeats (`덮는 모양이 정해져 있다`) →
**standing in advance where the blanket doesn't fall.** And the shadow:
`맞을까 봐 무서운 건 없어졌다. 대신 이게 다 계산대로 된다는 것이 어딘가
다른 종류의 것을 데리고 왔는데, **그게 뭔지는 안 봤다.**`

**★★ The luring:** `**못 맞히는 폭격기는 내려온다. 내려오는 것 말고 방법이
없게 만들었다.**` Control sees danger, cockpit sees opportunity;
`겨냥하는 것은 겨냥당하는 줄 몰랐다.` The intercept solves time AND height
at one point (EP83's grammar, new axis), priced with failure cost (`첫 번에
하는 게 맞았다`), fired ahead of the dive; the hit is known **through the
chain before the eyes** (`사슬을 타고 오는 저항의 결`). Wing joint, splash,
head finish.

**★★★ The lightness now outlasts the ride.** Ladder, hangar floor, dinner
table — still there. The fourth item goes into the drawer **stiffly**
(`남아 있는 것을 넣으려니까 서랍이 뻑뻑했다`), and the sentence `서랍이 넷이
되면, 여는 날이 온다` is **cut off before it forms** — she turns off the
light instead. `어둠 속에서 몸은 아직 조금 가벼웠다.` `잘했다` arrives 2-for-2
(vs her sister's months of waiting — filed under things-not-thought-about);
Yeongjin's voice is `같게 내는 데 힘이 들어간 목소리`, which Sua doesn't hear.

**Dana's side:** watching skill become expected — `**잘하는 걸 보는 일이
익숙해졌다는 것이, 오늘 제일 아픈 것이었다**`; she learns at the monitor that
her own method has a ceiling (`닿지 않는 상대라는 게 있다는 걸`); the
tteokbokki text never gets sent (`좁은 길은 낼수록 더 좁아졌다`).

Closing couplet: 수아 `사거리 밖에 있던 것을 사거리 안으로 끌어내렸다. 그런
걸 할 수 있게 됐다.` ↔ 단아 **`사거리 밖으로 밀려난 것도 있었다. 그건
아무도 끌어 내려 주지 않았다.`**

Next: **EP86 「마당」** (8/10 Wed) — Harang's yard proper (four warm-ups
cashed in); **★★ 배유림 recovered (gap 50, the last high-gap debt, via the
Sua axis)**; the second barb (Dana's side); the aftermath of the broken
tteokbokki date. Then **EP87: the sea-robin** — swallowed, out from inside,
re-break confirmed.

## EP86 approved (2026-08-19) — the yard, and the barb comes back

**EP86 「마당」** (`91_EP086_승인완료`, standard, 4,831 chars, 8/10 Wed) is
`GATE_D_PASS`. State = **SNAP-086**, tracker SNAP-086, ledger **v1.81**.
**S11 is 11/16 — and with 배유림 recovered at gap 50, every high-gap cast
debt is now clear.**

**Yurim joins over the wall** — `하랑이지?` — because she and Harang were in
the same class **last year** (user fix): `작년에 같은 반이었던 사이는 담을
넘는 사이이기도 한 모양이었다.` Three edges, three ways (Sua–Yurim current
class, Harang–Yurim last year, Sua–Harang after-school). Her EP28 canon
carries: oversized handwriting, doing her own tasks, `심심했는데, 가 인사인
애`, a diary she prepped by **writing only the weather every day** (`머리
좋지?`), a plant she killed by watering daily (`열심히 해서 죽는 것도 있다는
걸 유림은 처음 듣는 눈치였다`). The payoff: **the first peer noise since
school vanished.**

**★★ Harang and Sua teach each other (user fix)** — my draft had Harang
one-way coaching, but EP67 canon has Harang worse at rests. Now: **Sua reads
the score** (`여기 쉼표 있어` — counting is hers), **Harang owns bow and
fingering** (`힘 빼. 활은 잡는 게 아니라 얹는 거야` — the body-knowledge is
hers), and `**한쪽은 종이로 알고 한쪽은 몸으로 알았다**`. Structurally this
re-runs the sisters' split (Dana = body, Sua = paper) **but in the yard it
combines instead of dividing** — with Yurim judging by ear.

**「오늘 좀 멍하다?」** — Yurim can only say *today*, having not seen her all
vacation. Harang, who has watched her every Mon/Wed/Fri, says nothing:
**`아는 사람이 말을 안 하고, 모르는 사람이 말을 했다.`** She lowers the bow
tip and raises it again — `묻지 않는 것도 물을 때를 고르는 애였다.` Sua
answers `어제 늦게 잤어` (true, and not an answer), and earlier catches
herself saying **`그냥 있어`** — *her sister's* deflection now in her own
mouth: `그 말은 원래 뭘 가리고 있을 때 쓰는 말이었다.` Walking home she
**sorts what can be brought into the house and what can't.**

**★★★ The barb returns, reversed.** Sua brings the yard home, bright and
unmixed, and Dana listens, laughs — then: **`좋았겠네. 넌 나갔다 올 데라도
있어서.`** `좋았겠네, 까지는 하려던 말이었다. (…) **사실이라서 더 안 좋은
말이 됐다.**` She can't take it back because `**반쯤 맞는 말은 아니라고 할
수가 없었다**`. That night EP84 decodes retroactively: `그 말을 하고 나서
동생 얼굴이 잠깐 이상했던 게 이제야 생각났다. (…) **아프게 하고 나서야
읽히는 것들이 있었다.**` Sua files it separately: `**서랍은 모르는 걸 넣는
데다.** (…) **아는 건 그냥 상한 채로 두는 수밖에 없었다**` — with no place
yet for where those pile up. And a limit: `상한 것 하나가 좋았던 것 전부를
상하게 하지는 않았다. (…) **언니한테는 지금 좋았던 것 쪽이 며칠째 없었다.**`

**★★ Hyejeong is counting.** The cancellation text (`몸이 좀 안 좋아서` —
the shortest true thing) gets **`또?`**, then **`나았다며.`**:
`화가 났으면 차라리 길었을 것이다. **또, 라는 글자는 앞에 온 것들을 다
세어 본 사람만 쓸 수 있는 글자였다.**` Two days without a reply (`미안`
deleted, `다음엔 꼭` deleted — `쓰고 나서 감당할 수 있는 말이 없었다`).
**This is EP88's ignition point.**

Small: Dana now sorts her days (intake day / porch day / room day —
`마루의 날이라는 게 있다는 걸 한 달 전의 자기는 몰랐다`), and `갔다 와`
acquires a back side. Canon: **watermelon belongs to the recital episode** —
this chapter uses steamed corn a customer left instead (user fix).

Close: `같은 모양의 말이 이 집에 두 번 지나갔다. / **두 번 다, 한 말이 들은
말보다 늦게 아팠다.**`

Next: **EP87 「안에서」** (8/12 Fri, sub-arc ③ finale) — the sea-robin, the
series' first fish, walking on fin-rays; **swallowed, then out from inside**;
a brutal win that still confirms the **re-break** — then sub-arc ④ 「검문」
(EP88–90).

## EP87 approved (2026-08-19) — swallowed, and out; sub-arc ③ closes

**EP87 「안에서」** (`92_EP087_승인완료`, key chapter, 4,988 chars, 8/12 Fri)
is `GATE_D_PASS`. State = **SNAP-087**, tracker SNAP-087, ledger **v1.82**.
**S11 is 12/16 — sub-arc ③ 「가시」 complete; ④ 「검문」 (EP88–90) begins.**

**The sea-robin** (user specs): the biggest thing yet — mistaken for terrain
(`능선이 움직였다`), body the size of a seawall section, **slow because size
removed the need for speed**, walking on fin-rays through **waist-deep**
water. Nothing works: strikes sink into bulk (`벽은 아프기라도 하지`), the
anchor lands without pain, gaps close at a walk. Yeongjin's order includes a
first: **`방재벽까지 오게 두더라도.`** — something now outranks the wall.

**★★★ Suction, not biting** (user concept): the mouth is half the body, and
opening it makes **the world's water flow toward it** — `피하는 공격이
아니었다. 버티는 공격이었다.` First intake she anchors to sunken breakwater
rubble and holds (the chain **sings**); second intake **pulls the rubble out
whole** — `피할 방향 자체가 없었다` — and she goes in with the water.

**Two darknesses:** the hangar gets video blackout with sound intact
(`근거 있는 상상이 제일 나쁜 상상이었다`; `"언니야?" / "숨소리다."` —
one fact held between two people; Yeongjin's hand with **nothing to press**,
the EP81 inverse). Inside: full-body crush **reawakens the pain** (EP70
lineage), and `무섭고 화가 났다. 순서대로가 아니라 같이 왔다` — topped by
(user edit) **`이대로 끝난다면 집에 두 사람은 마지막 소리만 듣게 될 거라는
데에 제일 화가 났다.`** Cold head in the dark: `조임에도 간격이 있다. (…)
여기까지 온 생각의 길이 봄부터 걸어온 길이었다.`

**★★★ The red interior (user addition — the chapter's peak):** zero-range
anchor shot into the palate, ignition *inside*, and the rocket light shows:

> **온통 붉은 빛에 물든 사방은 거대한 파쇄기를 방불케 하는 설비들로
> 가득했다. 오직 타이탄을 부수기 위해 존재하는 세상이었다.**

**The most explicit visual evidence yet of §1-A** — it came to destroy, not
to eat. No explanation; **Dana is the only witness**; the hangar screen goes
black → **red** (the camera catching ignition light — user fix). She climbs
out through the wound (`앵커가 박힌 자리가 위였다` — the only coordinate),
into waist water, sunlight, breath: `**숨이라는 게 공기의 일이 아니라 빛의
일이기도 하다는 걸, 어두운 데 들어갔다 나온 사람만 알았다.**` And
**`"언니!!"`** (user fix on address) — Sua's first shout into the comms.

**Re-break, accelerated:** Yeongjin can't pick a word (`고를 수 있는 말이 다
작았다` — hand on shoulder instead); Sua grabs her sleeve (EP1 lineage) and
does **the inspection of someone who only heard it** (each dent arrives with
its sound). Dinner impossible; collapse **before nightfall** —
`지난번에는 이틀이 걸렸다. 이번에는 밤이 오기 전에 왔다.` /
**`무너지는 데 걸리는 시간이 줄고 있었다`** — two people counting, neither
speaking. Day's motion inverted by night: out-through-to-light vs.
closing-inward, breath shallow again.

**Hyejeong:** the reply finally sent — `미안. **나중에 다 말할게.**` (the
first promise of a "later": `가리는 말들은 다 지금을 가리는 말이었다`) →
**`그래. 기다릴게.`** — `세던 사람이 기다리는 사람이 됐다.` **First
reservation on the autumn confession line.**

Canon: sea-robin specs (max size, fin-walking, suction, strike-absorbing,
red machinery-like interior sighted); waist depth as the suction condition
(no-underwater seal still holds). Checker caught nothing new; author-name
leak (`청자고둥`/`가오리` in narration) was user-fixed to `창을 쏘던 것` /
`날아다니던 것`.

Close: `안에서 밖으로 나오는 데는 성공했다. / **나온 몸이 어디로 가는지는
아무도 몰랐다.**`

Next: **sub-arc ④ 「검문」 — EP88 「따라간 길」** (8/13 Sat): Hyejeong's one
tail-job, the military-grade equipment glimpsed near the shop, Yejin's
restraint, **pattern recognition complete** (vanishes at every appearance,
sick the day after — the `또?` tally becomes action) → EP89 uncle consult &
Gurae-dong checkpoints → EP90 the shop search, barely covered, **no
confirmation**.

## G0-016 approved (2026-08-19) — 박우석 restored as the quiet supply line

User proposed recovering an old-draft asset, and it fits a real gap: Yeongjin
is canonically **기계공학 · 과학기술전문사관 · 국방과학연구소 · 예비역 중령**
(CH-04), yet the only sourcing line in current canon was Ki-tae's scrapyard.
After EP85 exposed **the buoys' blind spot overhead**, something had to fill
it. **`박우석` is now removed from `source-firewall.md`'s banned old-draft
names** (that one line only; the rest stand).

**The relationship:** Yeongjin's junior from the research institute, who owes
him from long ago and **sends what the list says without asking what it's
for**. Not a debt that gets repaid — one that can't be. The risk is mutual, so
deliveries are unmarked, small, quiet. **Speech level: Yeongjin uses 하게체**
(same register as with Ki-tae) — user fix, filed on the precheck card.

**The EP88 shipment is radar-class surveillance gear**, answering EP85. On the
page: **no such word, no Wooseok, no name** — Hyejeong sees only *a thing that
has no business arriving at a house.* Her "military-grade" read is **correct**,
and she still can't reach what it is.

**Seeded backward (user request):** EP86 gains one overheard call in the scene
where Dana listens to the shop from the porch — it opens like a parts order,
then drops in volume: **`오랜만일세. 그 목록 말인데. 급한 건 아니고, 빠르면
좋고. 아니, 그건 안 물어봐도 되네.`** The relationship states itself without
the man appearing. And Dana's reaction folds into the arc: `안 물어봐도 된다는
말이 좀 이상했다. (…) **이 집에 안 물어봐도 되는 것이 요즘 한둘이
아니었다**` — she stops listening and goes to her room. **The girl from the
house that doesn't ask doesn't ask either.** (EP86 now 5,059 chars, still in
band; logged in `소급정정_2026-08-19_G0-016`.)

**Seals:** Wooseok doesn't know what any of it is for; **his line and
Myeongjun's must never connect** (two military-adjacent channels ignorant of
each other is the arc's new tension); the institute-era backstory stays shut
(Gate B). **Design payoff:** EP89–90's checkpoints now have physical stakes —
the army approaches a shop with **military-channel hardware sitting in the
yard**, so Yeongjin's concealment is doubled, underground and above.

## EP88 approved (2026-08-19) — the counterexample starts the investigation

**EP88 「따라간 길」** (`93_EP088_승인완료`, standard, 4,768 chars, 8/13 Sat,
**Hyejeong POV — second in the series after EP73**) is `GATE_D_PASS`. State =
**SNAP-088**, tracker SNAP-088, ledger **v1.83**. **S11 is 13/16; sub-arc ④
「검문」 has begun.**

**Seeing them all at once is the event:** `하나씩 보면 다 넘어갈 수 있는
것들이었다. (…) **오늘 아침에 처음으로 하나씩이 아니라 한꺼번에 봤고,
한꺼번에 보니까 다른 것이 됐다.**` First hypothesis — *she vanishes on alarm
days* — fits almost everything. **Then the counterexample** (user's catch):
**7/25 was a quiet night**, no siren, nothing on the news (she checks), and
Dana still didn't answer and was sick the next day. **The exception doesn't
weaken the theory, it makes it worse:** `경보 때문이라면 차라리 나았다. (…)
**저것들이 안 나온 밤에도 나가는 밤이 있다는 뜻이었다.**` Revised:
**`경보가 문제가 아니었다. 연락이 끊기는 밤이 있고, 방학 들어서는 그 다음
날에는 앓았다.`** The picture degrades in a specific direction — `처음
그림에서 단아는 **숨는 애**였다. (…) 다시 그린 그림에서 단아는 **나가는
애**였다.` The gap that remains is Sua's edited text: she knows **the nights
exist** and nothing about **what happens in them** — `열 살이 그런 문자를
보내는 법을 알고 있다는 게, 지금 생각하니 그것도 이상한 일이었다.`

Also: waiting gets redefined — `기다림에는 조건이 하나 있다. **기다리는 동안
상대가 무사해야 한다는 것.**`

**Yejin** confirms she's seen it too (EP74 recovered): `이상한 건 나도 알아`
/ `**원래 너네는 한 마디 하면 세 마디가 돌아오는데**` — someone was counting
from the side. She argues for waiting (`너나 나나 단아랑 하루이틀 알고
지냈냐`), loses to `**기다렸어. 넉 달 기다렸어**`, and sets a condition that
becomes EP90's hinge: **`보고 이상하면, 이상하다고 나한테만 말해. 걔한테
말고.`** Plus `복숭아. 걔 복숭아 좋아해` — *the girl who knows her favorite
fruit and the girl drawing a four-month chart, over the same friend.*

**★★★ The sighting is a verdict, not an event.** Hyejeong has been in and out
of that yard since before school, so she knows the baseline: a company name on
the truck, a loud **`박사님 계세요, 물건 왔습니다`** (canon address per EP12/14
— user fix), paperwork, and cargo left sitting in the yard. **Today all four
are missing** — unmarked truck, blank coveralls, **dark green iron-cornered
crates with locks**, `**딱 안 보이는 속도라는 게 있다면 저 속도였다**`, and
everything goes straight inside. A neighbor glances and walks on:
**`아무것도 아닌 장면이었다. 아무것도 아닌 걸로 보려면 아무 생각이 없어야
했다.`** Her "military-looking" read gets evidence rather than instinct — the
**dark green boxes she saw at her uncle's base visitor center** (user
addition). **And the biggest tell isn't cargo:** `할아버지가 허리를 편 채
반듯하게 서서 그걸 보고 있었다는 건, **저 물건들이 저 집 일이라는
뜻이었다**` — not the posture of receiving a delivery, the posture of
inspecting one. She turns back before the house: `**보러 왔는데, 본 것이
보려던 것보다 컸다**`, carrying undelivered peaches home (`병문안 쪽이기를
바랐다`).

**The uncle stays unrung.** Mother is ruled out (`걱정이 동네를 돈다` → Dana
would hide deeper). The counterexample forces the conclusion — quiet nights
mean *ordered, called, or self-sent*, and **all three imply an adult**:
`열두 살이 혼자 정해서 하는 일의 모양이 아니었다.` She finds **큰삼촌**'s
number (user's address fix; the man who laughs `군인 비슷한 거` and says he'll
explain when she's grown) and stops before pressing: `군인한테 묻는 건
어른한테 묻는 것과 다른 일일 수 있었다. (…) **오늘 본 궤짝이 너무 컸다.**`

**Dana never appears in this chapter** — she exists only as an unread message.
(`check_continuity` caught my `팔짱` phrasing — impossible for Yeongjin — and
it was removed.)

Close: `기다리겠다고 했다. / **기다리는 것과 알아보는 것이 다른 일이라는 걸,
오늘 언덕에서 알았다.**`

Next: **EP89 「물어본 것」** (8/14 Sun) — the consult (`군에서 어린애에게
위험한 일을 시키는 경우도 있느냐`), **Myeongjun noticing the overlap** between
absence dates, Gurae-dong reports, and operation logs → **checkpoints ordered,
justified by EP76's radius-less standard** — the thing Seojin didn't write
coming back as a net. **And the two military-adjacent channels still don't
know about each other** (Myeongjun ↔ Wooseok, sealed by G0-016).

## EP89 approved (2026-08-19) — the name is blocked, the place name gets through

**EP89 「구래동」** (`94_EP089_승인완료`, important, 5,021 chars, 8/14 Sun,
**Hyejeong ↔ Myeongjun cross-cut**) is `GATE_D_PASS`. State = **SNAP-089**,
tracker SNAP-089, ledger **v1.84**. **S11 is 14/16; sub-arc ④ is 2/3.**

**User's design (the spine of the chapter):** *the moment 도영진's name reaches
Myeongjun's ear he identifies him instantly* — so the consult must NOT land as
a serious report. Myeongjun half-listens to his niece, and what stays with him
is **one place name**. Executed exactly: **Hyejeong never says a name** — not
her friend's, not 도영진's, not the shop's. She asks about circumstances, not
people: `군에서 어린애한테 위험한 일을 시키는 경우도 있어요?` Yejin is
consulted first (EP88's condition `나한테만 말해` actually functioning). The
uncle answers honestly — the army does not do that — and **erasing one answer
makes the remaining space worse**: `군에서 시키는 게 아니면, 안 시키는데도
그런다는 뜻이고, 그건 더 이상한 얘기였다.`

**Why he doesn't take the consult seriously:** `드문 일에도 이유는 있는
법이고 열두 살의 이유는 대개 열두 살짜리다.` Correct common sense, precisely
wrong. What he *does* take is **구래동** — a name that keeps catching in his
ear lately. Three stacks converge on one point: operation logs, sighting
reports, and geography. **Gurae-dong is a headland** (user fix — replacing a
"fewest casualties" line that contradicted it being Hyejeong and Dana's own
neighborhood): shallowest, closest to the port, on the road to the sunken old
city, **and a spur jutting out of the city** — whatever comes ashore reaches it
first. `저것들이 거기로 오는 이유는 지리로 다 설명이 됐다.`

**★★ The jurisdiction fix (user catch): the army cannot run checkpoints in
town.** `저희 순찰은 해안선까지입니다` / `시내는 저희 관할이 아닙니다` /
`그러니까 협조를 요청해야지.` Checkpoints are police work, road control is the
city's, and the army's reach ends at **requesting**. So EP76's radius-less
standard now goes **outbound**: Seojin's fourth consecutive act of not-writing
is a formal request — **`미확인 대형체 인근 지역 예방적 관리 강화 요청`** —
and he flags it once more (`저쪽에서 반경을 물어볼 텐데요` / `물어보면 그때
대답한다`). Such a request passes as a matter of course: **no agency refuses
"strengthened management of a hazard area."** The single buffer is that the
uniforms on the street will not be military ones — `동네 사람들은 순찰차가 한
대 더 도는 걸 보게 될 것이고, 대부분은 요즘 세상이 하도 험하니, 하고 넘길
것이다. **넘기지 않는 사람이 몇이나 될지는 아무도 세지 않았다.**` No extra
personnel are requested (asking would require a reason, and a reason invites
questions from above) — and he cannot state his own reason: `모르겠다. 찾을 게
있는지도 모르겠고.`

**★★ New: Seojin notices** (user addition). `다만 눈은 봤다. **그 다섯 달
동안 손에 쥔 게 없어서 투덜거림만 늘었던 사령관의 눈에 오늘은 뭔가 돌아
있었다. 뭐가 있긴 한 거다.**` He doesn't press — not out of deference, but
because a genuine `모르겠다` yields nothing under questioning. **There is now
one subordinate in that room who knows something is there.**

**★ Seong-ho is already in the army's paperwork** — `언덕에서 봤다는 신고를
여름 내내 넣은 학생 하나` / `성실한 목격자는 어느 조사에서나 반가운
이름이었다.` Filed, not yet used.

**Dana does not appear for the second chapter running** (EP88–89, deliberate).
Time is marked only by peaches softening in a fridge.

Canon added: **고명준 = 남방사 사령관** (post confirmed on the page),
**윤 대위 = Seojin**, **Gurae-dong = headland**, and the jurisdiction rule
(checkpoints = police / road control = city / army = request only).

Close: `조카는 친구 이름을 대지 않았고, 삼촌은 지명 하나를 가져갔다. / **둘
다 자기가 무엇을 한 건지 몰랐다.**`

Next: **EP90 「접근」** (8/15 Mon~) — sub-arc ④ closes. The cooperation
request takes effect and **police** patrols/checkpoints reach Gurae-dong; the
shop is approached and **barely stays concealed**; the army **fails to
confirm**; Hyejeong blames herself for asking; and **Yejin holds the
relationship together** (EP88's condition recovered). Then EP91–92 (krill-type
— the army's first kill, Myeongjun's turning point) close S11.

## EP90 approved (2026-08-19) — nobody lied and everyone is worse off

**EP90 「접근」** (`95_EP090_승인완료`, important, 5,514 chars, 8/16 Tue,
four-POV cross-cut: Seojin → Dana → Yeongjin → Seojin → Hyejeong) is
`GATE_D_PASS`. State = **SNAP-090**, tracker SNAP-090, ledger **v1.85**.
**S11 is 15/16; sub-arc ④ 「검문」 closes.**

**8/15 is Liberation Day**, so the request sat for a day — the paperwork's own
delay, felt from the inside: `하루 늦은 게 누구한테 좋은 일인지 알 수
없었다.` Then **the radius question actually arrives** (EP89's setup): the
police-agency desk asks `구체적으로 어디까지입니까`, and Seojin, with no
instruction to narrow and no grounds to narrow, answers **`해당 지역 전역`**.
The blank he didn't fill now works in the *widening* direction — `반경을 안
썼기 때문에 반경이 없어졌고, 반경이 없으니까 전부가 됐다.` Internal army
documents circulate fine with blanks; outbound ones don't, because the
receiving side has to decide where to put its people. **User fix:** the
recipient is the **경찰청**, not 경찰서 — a command-level request goes to the
agency, not a precinct — and EP89's three mentions were **retroactively
corrected** (`Black_Titan_소급정정_2026-08-19_협조공문_수신기관_v1.0.md`).
The chain is 남방사 → 경찰청 → 경찰서 → **구래파출소**, and that three-step
distance is why the men who reach the yard don't know why they're there.

**Dana returns after two chapters absent** — day four post-collapse, fine
sitting, **only the stairs show it**, tingling halved. **★★ The change is that
improvement now registers as welcome:** `봄에는 아침에 일어나서 몸 상태를
확인하지 않았다.` She sees an extra patrol car and files it under **`요즘
세상이 하도 험하니까`** — the girl who is the reason has no line connecting
the two. Sua looks longer and says `아무것도` (immediate-mobilization seal
intact).

**★★★ The yard scene runs on zero lies.** The police say **`사장님`** — the
neighborhood says 박사님/도 박사님/도 씨, so the address itself is proof they
came in blind. Yeongjin's four-step concealment grammar: (1) **make them walk
before they ask** — a prepared question order falls apart mid-walk, and people
who saw with their own feet feel nothing was hidden; (2) **open the ledger** —
one book, kept true, so showing it needs no preparation (`두 권을 쓰면 두
권을 기억해야 하고, 기억하는 사람은 언젠가 틀린다`); (3) **never deny** the
unusual-vehicle question, just push sideways with facts (`요즘은 부품 구하기가
힘들어서요`); (4) **the basement never comes up** — `오래된 수리점에 지하가
있는 건 이상한 일이 아니었다. 이상하지 않은 것은 질문이 되지 않는다.`

**★★ "Barely" is luck, not skill.** The older officer takes **two steps toward
the dark green crate** — the one Hyejeong saw. **Yeongjin does not call him
back:** `부르면 저기 볼 게 있다는 뜻이 된다.` What turns the man around is his
partner's wristwatch: three more sites to go. Afterward Yeongjin isn't
frightened, he's **tired** — `손이 아니라 등이 먼저 알았다` — because this is a
body that knows how such procedures run, including that they find nothing today
**and that they find something if they keep coming**. Close: `오늘은 안 진
것이었다. / 이긴 게 아니었다.`

**Confirmation fails and changes nothing.** Twelve sites, zero vehicle hits,
zero statements, `특이사항 없음` — and Myeongjun reads it as `없다는 건 안
봤다는 뜻일 수도 있다`, keeping the checkpoint line with **no end date** (`기간
미정은 기간이 아니다`). **The line is now a constant through S11–S12.** Seojin
observes a second time: what was in the commander's eye yesterday is halved
today but not gone — `없어졌으면 기간을 정했을 것이다.`

**Hyejeong can never confirm the causation** — only the timing (asked Sunday,
patrols Tuesday). Both thoughts arrive together and neither wins; confirming
would mean telling her uncle what she withheld on Sunday. `알아보는 것과
망치는 것의 경계가 안 보인다. / 그 경계를 아는 사람이 어른이라고 생각했는데,
어른한테 물어봤더니 이렇게 됐다.` **Yejin doesn't console — she takes the
verdict off her:** `네가 물어본 거랑 순찰차랑 무슨 상관이야` / `상관 있어도
그게 네 잘못이야?` / **`대답 못 하면 네 잘못 아닌 거야.`** (User fix: `나한테는
말하랬지` — receiving, not exclusionary; and `그것 때문일까` instead of a date,
so the anxiety lands rather than an argument.) The peaches all went soft, so
they buy new ones and **go together tomorrow** — `둘이 가면 병문안이야`.

Close: `아무도 거짓말을 하지 않았고 아무도 아무것도 확인하지 못했는데, 넷의
자리가 전부 조금씩 나빠졌다.`

Next: **EP91 크릴형 (krill-type)** (8/18 Thu) — sub-arc ⑤ 「군의 첫 승리」:
swarm rather than a single body, **evacuation obstruction** as the threat,
anchor strikes useless → **high-explosive rounds effective**, **the army's
first kill on its own**, and Myeongjun's turning point toward the E-phase
seizure judgment. The checkpoint line stays up throughout — victory and
tightening arrive together — then EP92 closes S11 into S12 「여름방학 마지막
날」 (school resumes 9/1).

## EP91 approved (2026-08-20) — they won and nobody knows why

**EP91 「한 마리」** (`96_EP091_승인완료`, important, 5,708 chars, 8/18 Thu,
Dana POV with Myeongjun closing) is `GATE_D_PASS`. State = **SNAP-091**,
tracker SNAP-091, ledger **v1.86**. **S11 is 15/16** (S11 = EP77–92; the
earlier 12/16–15/16 labels were off by one and are corrected from here).

**★★★ The radar pays off** (G0-016's four-step chain completes: EP85 buoy
silence → EP86 phone hint → EP88 delivery/sighting → **EP91 first reading**).
Buoys read wave disturbance and say only *something passed*; the new unit gives
**count and size**. So the screen shows **an area, not a point** — and Yeongjin
suspects the equipment first: `처음 잡은 그림이 이렇게 나오면 장비를 의심하는
게 순서다.` A five-year-old buoy net and a two-month-old box disagreeing means
you believe the old one. **Sua notices the real tell** (`부표는 아직 안
울었는데요`) and **Dana overturns it** (`부표는 물결이 지나가야 우는 거잖아.
아직 안 지나간 거 아냐?`); the city's evacuation broadcast confirms it. The
observation sheet has a species column and a size column and **no count
column** — nobody ever needed one. Sua writes a question mark in the margin.

**★★★ The anchor hits and it doesn't matter.** The head is narrow but it's
still an area, so each shot skewers or crushes a handful — `대여섯쯤 됐다` —
**and then the cycle kills it**: fire, reel in, reload, while hundreds walk
past. `잘 맞았는데 아무 일도 안 일어났다. (…) **맞고 통했는데 아무 소용이
없는 건 처음이었다.**` They also **go into gaps** rather than biting — knee
joint, elbow, neck — so the first thing Dana does is **pick them off by hand**:
`싸우는 게 아니었다. 털어내고 있었다.` The tear-off is nearly resistance-free,
which teaches its own lesson: `약한 것과 안 죽는 것은 다른 얘기.` Her fix is
**invented by the body first**: she fires the anchor, doesn't reel it, pays out
the chain and swings — point becomes line, tens per revolution. `앵커는 하나를
뚫으라고 만든 물건이다. (…) **사슬은 원래 회수용이었다.**`

**★★★ And they never look at her.** Every creature so far came *at* her; these
climb over and keep going. `앞에 있으면 타고 넘어갔고, 넘어가면서 틈으로
들어갔고, 그러고 지나갔다.` Being ignored is more helpless than losing. At the
seawall they **pile on each other** — not climbing, *being pushed up* — and she
smashes the heap with the chain again and again: `무너뜨리는 시간보다 쌓이는
시간이 짧았다.` Then `**안 돼**` out loud, and she learns they crossed **by
sound**, from the far side. (Not a first — EP14's spider-crab bridged the wall
on its legs; user's note produced `두 번 빼고는 다 하나였으니까`.)

**★★★ The army fires for the first time in five months.** Since March they've
known rounds don't kill, so they stopped opening up at all — dispersal and
control only. Today the wall is being crossed, and Myeongjun's calculus is
plain: `남은 걸 다 써서 못 막으면 다 쓰고 못 막은 것이고, 안 쓰고 못 막으면
안 쓰고 못 막은 것이다. **둘 중에 나중에 설명이 되는 쪽은 하나뿐이었다.**`
Self-propelled guns, then naval guns (Dana sees the warship — nothing like the
fishing boats, and it is aiming at her), then **the held-back card: the
helicopters.** (User first wrote fighter-bombers; canon v2.3 says no fixed-wing
and few pilots, so it became rotary — and the reason for hoarding doubled:
`항공유는 다시 안 들어온다. 조종사는 더 안 들어온다.`) Loudspeaker and radio
both order the giant to clear the firing zone; **Dana hears none of it** —
`여태 저쪽이 이쪽에 말을 건 적이 없었다` — and pulls back only when the first
shell lands, ending up with **her back against the wall she came to defend**,
feeling it ring through her spine. **The area is erased.** Rounds don't
penetrate but momentum does, and these are small and light enough that internal
shock is enough (canon; **never stated on the page** per G0-010). The water
turns red and is water again.

**★★★ The last one.** With the pushing pressure gone, the ones over the wall
come back out and are finished on the ramp. Dana watches, then **steps on a
single straggler passing under her foot.** She tries to count the day's kills
and can't: `마구잡이로 한 것들이었다. 세려고 하면 손에 잡히는 게 없었다. /
**확실한 건 마지막 하나뿐이었다.**` Relief lands first (nobody died), then:
`**내가 한 게 아니었다.**`

**★★★ Myeongjun's seizure judgment becomes inevitable** — four things seen in
one day: the wall was crossed; the giant couldn't stop it; **the giant ignored
our order to withdraw**; and the last card is spent. He refuses to let a guess
into the report — `짐작을 보고서에 쓰면 그게 다음에 근거가 된다. 근거가 되면
다음에 또 통할 거라고 생각하고 나간다` → **`나도 모른다. 그렇게 써라`** —
which keeps G0-010 sealed while leaving the fear intact. Conclusion is not
"it's useful, take it" but **`통제 밖의 전력이 도시 안에 있다`**. Checkpoints
stay up. Seojin fills a reason column that has been blank for four months.
Close: `이긴 날인데 방을 나서면서 기분이 좋지 않았다.`

**Continuity fixes this chapter:** `check_continuity` caught a **G0-013**
violation (stairs — the house is single-storey and the basement is reached by
lift), fixed in EP91 and **retroactively in EP90's approved text**
(`Black_Titan_소급정정_2026-08-20_계단-승강기_v1.0.md`); two verbatim overlaps
were also rewritten, including a full-sentence repeat of EP90's double-glazing
line.

Next: **EP92 closes S11** (8/19 Fri) — **the army won and the house is in more
danger**: checkpoints still up, Dana's body, the thorn between the sisters,
Hyejeong's silence, and Myeongjun's seizure judgment going to paper. Then
**S12 「여름방학 마지막 날」** — twelve days to the 9/1 school year, the fully
combat-form synthetic, and Sua's spinal injury.

## EP92 approved (2026-08-20) — S11 closes; nobody lied and the house has less

**EP92 「열두 밤」** (`97_EP092_승인완료`, important, 5,088 chars, 8/19 Fri,
five POVs) is `GATE_D_PASS`. State = **SNAP-092**, tracker SNAP-092, ledger
**v1.87**, **arc capsule S11 written**. **S11 「꺾임과 검문」 (EP77–92) is
complete.**

**★★ The problem changes category.** Dana doesn't collapse — only her shoulder
and back are stiff from swinging the chain. Everything else is fine, and that
is worse: `무너질 만큼 안 했다는 뜻이다. **무너질 만큼 안 했는데 못 막았다는
뜻이기도 했다.**` Up to yesterday the obstacle was her body; today her body is
fine and yesterday she still lost. **User catch:** the wash is a scaffold and a
high-pressure gun (EP49/54 canon), not a rag — which turned the scene sharper,
because the gun **must be braced on the shoulder** and that is exactly the joint
that won't lift. She's pushed back two steps, Yeongjin takes the wand without a
word, and she ends up **holding the progress sheet — Sua's usual job.**

**★★★ Thorn #3 reverses direction.** EP84 and EP86 had Dana pricking Sua;
here Sua does it to Dana, with no ill intent at all. She's been holding her
admiration for the chain-swing since yesterday — and then the calculation
follows the admiration out of her mouth: **`그거 처음부터 했으면 더 많이
잡았을 텐데.`** Same device as EP86: `한 박자 뒤에 수아 귀가 그걸 들었다.`
**Per user's correction, Sua knows immediately what she did** — she just can't
fix it, because apologizing would make it nothing while leaving the not-nothing
behind. Dana answers `응, 그러네` with no anger and goes to her room.

**★★★ And the real thing that snags Sua isn't the sentence.** When she watched
her sister being overrun yesterday, the first thing she thought was not
*I'm scared* but **`저렇게 하면 안 되는데`** — the fear came, but second. She
notices the ordering today, and **cannot name it**: `요즘 내가 좀.` is where
the sentence stops, because naming it requires knowing what's wrong and she
doesn't. Unexplained, it gets covered — and **what fills the vacated space is
planning**: *what do we do if something like that comes again*. `그 생각은 잘
됐다. **잘 되는 게 이상하다는 생각은 하지 않았다.**` (Combat-pleasure
awareness and immediate-mobilization remain at zero — this is the last tremor
before S12.)

**★★★ Yeongjin cuts the supply line himself.** Patrols are up a second day and
the main road is permanently manned, so he calls (`선배님` — the junior from
his institute days; the neighborhood's `박사님` is a different register) and
says **`당분간 보내지 말게`**, giving no reason. The other man doesn't ask —
he never has. **The decision doesn't add up and he knows it**: the wall was
crossed yesterday, which means more observation is needed, and half the list
including two items he actually needs hasn't arrived. But `트럭이 검문선을
두 번 지나갈 수는 없었다` — once is luck, twice is a record. Also: `다음에
급할 때 다시 걸어야 한다면 그때는 오늘보다 나쁜 통화가 될 것이다.` Moving one
crate inside one-handed takes twenty minutes; two hands would be five.

**★★ Hyejeong has nowhere left to ask.** The broadcast said only `해안 방면
위협 저지. 시민 피해 없음.` — and she catches herself wondering whether Dana
counts as a citizen. Uncle is closed (asking means telling him Sunday's
withheld half), Dana is closed (`하나를 물으려면 전부를 물어야 하는 질문`),
and Yejin can listen but **took the verdict, not supplied an answer**. So she
waits without an object: `기다린다는 게 뭘 기다리는 건지는 이번에는 잘
몰랐다` — and, for the first time, **doesn't text when a reply would come.**

**★★★ Myeongjun writes the judgment down but stops one line short.** On paper
that goes nowhere: `통제 밖의 전력이 도시 안에 있다` and `다음에 같은 규모가
오면 같은 방법을 쓸 수 없다`. The third line — **`확보해야 한다`** — he does
not write, because writing it makes it a request, a request gets forwarded, and
forwarding invites the question he can't answer: all he has is one place name,
four months of coordinates, and one thing that didn't leave the firing zone.
Seojin, transcribing, knows the type: **`아무 데도 안 가는 문서는 대개 나중에
어디로 간다.`** The paper says only `구래동`.

Close: Dana counts **twelve nights** to the 9/1 opening (Thursday), and EP76's
`자고 나면 나을 것이고` is formally retired — she now **pre-drafts what to say
when classmates ask about her vacation**, and `미리 정해 두게 됐다는 게 제일
달라진 점이었다.`

**Continuity fixes:** the rag-scale wash (above) and a **nonexistent upper
floor** — the house is single-storey with a basement and holds three people;
`지하에 계속 사람이 있었고 밤에는 위층에서` was replaced with the three of them
going to bed without speaking.

Next: **S12 「여름방학 마지막 날」** (8/20–8/31, twelve nights). Canon v2.3
sets the ending: a **fully combat-form synthetic** feigns weakness, and the
moment Sua turns away believing she's won, **a sea-snake piercing organ goes
through the lumbar** — dark red circulatory fluid makes "it is not a robot"
plain for the first time, **Sua's spinal sensation burns out**, Lucy and White
Sentinel intervene with XLG-5, and **Myeongjun seizes the site** (E phase).
**A Level 4 outline needs approval before drafting** — chapter count, event
placement, POV design, and how Lucy/White Sentinel enter.

## S12 outline approved (2026-08-20) — with G0-017 and G0-018

**S12 「여름방학 마지막 날」** (`Black_Titan_S12_EP093-103_화별개요_v0.4.md`)
is `LEVEL4_PASS`: **EP93–103, 11 chapters, 8/20 Sat – 8/31 Wed.** Split as
**everyday 4 / eve 3 / August 31st itself 4** (decision / dominance /
impalement / dissolution) — the ten canon-fixed events of that day do not fit
in one chapter.

**Arc line:** 언니가 못 나가서 동생을 내보낸 하루가 이 가족의 마지막 하루가
된다. The core lock is that **`오늘은 네가 나가라` has three motives at once**
(her body genuinely isn't ready; the enemy genuinely looks weak; and she
genuinely hates watching her sister be good at it) — **all three true, so none
of them works as an excuse afterward.**

**G0-017 — the August 31st enemy is replaced.** Canon v2.3 had a
crab+sea-snake synthetic; per user, that one moves to **EP95** (mid-size, Dana
piloting, and the canonical "improved version returns in autumn" now reads
naturally), and 8/31's enemy becomes a **nautilus + cone-snail synthetic**.
It looks like nothing but a big nautilus — spiral shell, long tentacle mass,
crawls and grabs and bites, **no visible muzzle**. The barrel is folded inside
the shell, and **this one does not fire**: it **drives the barrel in at close
range**, trading reach for certainty. Combat grammar: **sweep the incoming
tentacles aside with a spun anchor, then break shell in a continuous follow-up**
— Sua using EP91's chain-swing better than Dana did. **The lineage is the
foreshadowing**: EP83's cone-snail was a sniper that hid in its shell and fired
one precise round, beaten by timing the muzzle's exposure — and nobody
recognizes that lineage here because the outside is a nautilus. Readers who
know the old grammar read distance as safety, and **the knowledge itself is the
trap**.

**G0-018 — the force field depends on the pilot's consciousness.** Canon says
these bodies form a field at the cell surface; G0-018 adds that **it needs
someone forming it.** Sua is impaled, her spinal sensation burns out, she loses
consciousness — the brain goes out, the field goes out, and **the hatch cuts
open easily**, the thing that no ordnance has scratched since EP3. **Nothing on
the page explains this** (G0-010 stays sealed); the reader only sees that what
never worked before works today. Consequences: the capture needs **no force at
all** — it's less a war prize than salvage from an accident, which is what lets
EP103 be a chapter about dissolution rather than defeat. And **Yeongjin and
Dana never consider fleeing** — Sua is inside, unconscious, so **escape is not
a choice that exists.** They are taken *because* they are family. Destinations
fixed: **Sua → hospital, Dana → protective custody, Yeongjin → arrest.**

**Deferred to the next arc (user):** any US contact (Lucy speaks not at all in
S12 — the White Sentinel simply intervenes in EP102 and a silhouette stands on
it in EP103), the **Myeongjun ↔ Yeongjin meeting** (the capture happens but the
two never come face to face), cockpit/disguise-system analysis, and the arrest
and custody procedures themselves. **The biological reveal stays out of public
view** — the dark red fluid is seen by the people on site only; no broadcast,
no released drone footage. EP103's POV stays with the family coming apart, and
the army appears only as **the procedure that separates them**.

Next: **EP93** (8/20 Sat) — the household under a permanent checkpoint,
maintenance without resupply, and Sua going a whole day without poking at her
sister (thorn #3 aftermath).

## EP93 approved (2026-08-20) — S12 opens; four people being careful

**EP93 「조심」** (`98_EP093_승인완료`, standard, 4,773 chars, 8/20 Sat, Dana
POV throughout) is `GATE_D_PASS`. State = **SNAP-093**, tracker SNAP-093,
ledger **v1.88**. **S12 is 1/11.**

**Yesterday's cut bill arrives today.** The crawlers scratched the *inside* of
the joint plates, and there is **no part that fits** — user's correction killed
the word "정품": in this city almost nothing is newly made, so everything is
pulled from somewhere, dredged up, or recombined, and `규격이 맞으면 운이 좋은
거였다`. Yeongjin files a mismatched part down (one-handed, so bench-vise
setup splits a single motion into three), and **defers one**: an observation-
system component, `오늘은 된다` — which means only today. The box goes under
the shelf. **This is the chapter's tightening, and the likely gap on 8/31.**

**★★★ Nothing the creatures leave behind survives** (user catch — G0-011: they
dissolve). My draft had a broken leg wedged in the plates and tweezers picking
it out; both the persistence and the scale were wrong. Rewritten so **only the
marks remain**: `긁은 것은 아무 데도 없었다. (…) 판 사이를 그렇게 긁어 놨는데
긁은 쪽은 흔적도 없고, 자국만 자국대로 남아 있었다. / **자국을 보고 있으면
그날이 그대로 있는 것 같은데, 그날 있던 것은 하나도 안 남아 있었다.**` The
fix improved the chapter — the dissolution rule is now felt in *maintenance*
rather than combat. (Also: the frame operates underwater, so **rust was never a
concern** — replaced with access difficulty.)

**Dana's morning check reaches stage three.** EP83 she started counting again,
EP90 she stopped counting, and now **she measures and records it nowhere** —
not even on Sua's sheet: `안 적으면 아는 사람이 하나가 된다.` Her role is also
fixed in place: the gun wand and the big wrench are impossible, so she carries
**the progress sheet — Sua's paper**. And she doesn't ask why no part can be
found, because `안 물어봐도 되는 것들이 하나씩 늘었고, 늘어난 것들은 다
그대로 있었다`.

**★★ Care becomes distance.** Sua chooses her words all day (visible — `열 살이
고르면 티가 난다`) and never apologizes; Dana won't say `괜찮은데`, because
saying it makes it a not-okay thing. Why she can't even be angry: `틀린 말은
아니라고 하면 된다. **맞는 말은 아니라고 할 수가 없다.**` — and the user's
addition sharpens it further: **`벽을 못 넘게 할 수 있었을지도 모른다.`** Both
of them are being kind and the house gets quieter for it. Close: `조심하는
사람이 셋이면 집이 조용해지는 게 아니었다. / **비어 있는 것처럼 됐다. 셋이 다
안에 있는데도 그랬다.**`

**★★ The checkpoint has become furniture.** Ten days in, people step half a
pace around the patrol car without being told, kids play beside it and get gum
from the officer, and Miran (recovered at gap 17, with a one-line trace of her
Ha-Gurae origin — `우리 살던 데는 저런 것도 없었어`) says **`이제 저기 서
있는 게 안 이상해`**. Dana snags on it: the first three days everyone asked,
nobody answered, and people stop asking — **`이상하지 않으면 아무도 왜 저기
있느냐고 안 묻는다`**, which means it has no reason to be lifted either. The
household feels it materially too: twenty minutes per stop on the main road →
market stock halved → **one fewer dish at dinner.**

Next: **EP94** (8/22 Mon) — the Hyejeong/Yejin axis. Objectless waiting shifts
onto **preparing for the new term**, Yejin's cram-school session ends, and the
three of them **make a plan to meet before school starts** — a promise that
will not be kept.

## EP94 approved (2026-08-20) — a date on the calendar, and it is the 31st

**EP94 「약속」** (`99_EP094_승인완료`, standard, 4,843 chars, 8/22 Mon,
**Hyejeong close-POV, third in the series** after EP73/88) is `GATE_D_PASS`.
State = **SNAP-094**, tracker SNAP-094, ledger **v1.89**. **S12 is 2/11.**

**Objectless waiting doesn't hold.** Four days in she works out why: `기다리려면
기다릴 게 있어야 한다` — and people make an object. Yejin's seven-week cram
session ends (억울함 + 신남 = her longest-sentence day), proposes they meet
before term starts, and **user's line makes the wound precise**: `방학에
**병문안 한 번으로** 끝나면 좀 그렇잖아` → `방학답게 함께 모여 걱정 없이 논
날은 하루도 없었다.` Last year they saw each other every day.

**★★★ The date is August 31st — the day before term, at the 분식집.** It is
**the retry of the tteokbokki that fell through on 8/9** (EP85/86), and
Hyejeong picks the place instantly because `또?` and `나았다며` are still
sitting in her: too late to apologize, and raising it would make that day
bigger than she wants it. `그래서 같은 데를 다시 가기로 하는 걸로 대신했다.
**같은 데서 같은 걸 먹으면 그날이 없던 날처럼 될 것 같았다.**` The reader
knows what the 31st is; **nothing on the page hints at it.**

**★★★ Why she's counting down to the new term** (never said to Yejin): school
is an **observation window**. `매일 보면 하루 안 보이는 게 눈에 띈다. 눈에
띄면 물어봐도 되는 게 된다. **왜 어제 안 왔어, 는 이상한 질문이 아니다.**`
EP76's "vacation = forty days nobody asks" flips exactly. Also `개학은
아무한테도 안 물어도 온다` — the one thing this summer that needs no
permission. **She does not get to that first day.**

**★★ The relief has no basis and she declines to check.** Dana's reply comes
**immediately and without hedges** — all summer they carried `봐서`, `아마`,
`될 것 같은데`, and those meant it wouldn't happen. Today: `그래 그때 보자.`
→ `괜찮은가 보다`, and she starts to test the reasoning and stops: `오늘은
그냥 그렇게 두기로 했다.` She only notices at night that she didn't think
about the patrol car once all day.

**Two corrections of fact from the user, both improvements.** (1) *Yejin
already knows* — EP90 had Hyejeong tell her everything, so "nothing I could
say" was wrong; the problem is not secrecy but emptiness: `걱정한 걸 방학에 한
일이라고 부를 수는 없었다. 그런데 걱정 말고 한 게 없으면, **팔월에 한 게
걱정뿐이라는 얘기가 된다.**` (2) *She did go to the valley* — EP76 plan →
EP77 excitement → EP79 packing → EP82 aftermath (ice water, three seconds
ankle-deep, the cousin slipping), **7/27–28**. Restored, it splits the summer
in half: `계곡에 갔다 왔다. 그건 있었다. (…) **그게 칠월이었다.** / 팔월에 뭐
했냐고 물으면 대답이 없다.` The split lands exactly where Dana's decline
began — **Hyejeong has never laid it out that way.**

Next: **EP95** (8/24 Wed) — the **crab + sea-snake synthetic** (G0-017,
mid-size, **Dana pilots and wins**). The last proof of the "a day when the body
is fine" exception: she wins, and the curve is worse the next day. Also the
advance placement for autumn's improved version.

## EP95 approved (2026-08-20) — the first composite, and winning changes nothing

**EP95 「감긴다」** (`100_EP095_승인완료`, important, 5,201 chars, 8/24 Wed →
8/25 Thu, Dana POV) is `GATE_D_PASS`. State = **SNAP-095**, tracker SNAP-095,
ledger **v1.90**. **S12 is 3/11.**

**★★★ The first composite creature** (G0-017 — crab + sea-snake; the taxon
names never appear). Only the upper body is above water: carapace and a pair of
huge claws, **one much larger than the other** — and per the user's line, that
asymmetry is *familiar*: **`뻘밭에서 부러뜨렸던 집게다`**. So Dana reads it as
a known opponent, and the first exchange goes exactly as trained — spacing,
release-lock, launch, ignite, **hit**. Then: `그런데 밀리지가 않았다. (…)
**안 밀리려면 어디를 붙잡고 있어야 한다.**` Below the surface there is a long
smooth trunk and tail. Her framing (never the word "합성"): everything until
now was **one sea creature imitated and then exaggerated somewhere** — a claw,
a shell, a spine. `이건 둘이 붙어 있었다.`

**★★★ A structural weakness surfaces for the first time.** Tail → knee → waist
→ chest, and once wrapped, **the release lock is pinned** (user's correction:
it is a mechanism, not a hand motion). `앵커는 순서대로 하는 물건이다. (…)
첫 번째가 안 되면 두 번째가 없다.` EP91's chain swing is out too — you need an
arm to swing it. And then the claws come in at a range she cannot leave:
`조이는 것만이면 빠져나가면 된다. 때리는 것만이면 피하면 된다. **둘이 같이
오니까 아무것도 못 했다.**`

**★★★ The escape is two-stage** (user's revision, and it made the scene). She
notices the claw's arc has *shortened* — because it has to be close to squeeze,
which means **its own trunk is inside its own reach**. (1) She twists half a
handspan; the claw hits its own body; the coil loosens **half a turn only** —
`아직이다`. (2) The next blow comes to the chest at an angle she can't shed, so
she **drops her head and shoulders forward into it**, using her face to press
the claw down into the wrapped trunk — `자기도 모르게 나온 자세였다`. Then the
left arm is free (anchor is the left-side system), the shot goes into the seam
where carapace meets smooth, **the rocket keeps burning after impact and drives
deeper**, and the reel-in **drags the insides out with it**. Two iron-scraping
cries (G0-010's canon sound).

**Sua's sheet stops fitting reality**: one species column, two things to write.
`두 줄로 쓰면 두 마리가 돼요.` She rules a slash and writes **`큰 집게 / 뱀
같은 거`** — `칸을 그은 사람은 하나가 하나로 오는 것만 봤을 테니까`.

**★★★ And then Thursday.** Sitting up needs the sequence again — the one from
early August, which her body remembered after two weeks unused. Nothing
explains it: she didn't overdo it (under an hour), wasn't badly hit (`안쪽까지는
안 갔다`), didn't ride long. `**잘 싸운 날 나빠지면 잘 싸운 게 아무 상관이
없다는 뜻이 된다.**` The curve is now independent of winning, losing, doing
well, doing badly — **a day ridden has a day after it.** Her own conclusion:
**`나가지 않는 것밖에 없다`** — and she already knows it works (late July,
ten days off, she got better), and **she went out anyway.** This is the
psychological ground for `오늘은 네가 나가라` on the 31st. She circles the 31st
on the calendar and repeats EP86's error exactly: seven nights should be
enough — she once decided four would be — `될 수도 있다는 건 안 될 수도 있다는
뜻이었다.`

Canon added: **release-lock is a mechanism**, the anchor is the **left-arm**
system, its **rocket burns past impact**, and **enemies are imitations of sea
life with one feature exaggerated** — which is what makes a composite legible
as a category break.

Tooling: `tools/build_mobile_review.py` was matching only two-digit folder
prefixes and sorting names as strings, so `100_EP095` vanished from the review
and would have mis-ordered approved chapters at 100. Fixed to `\d{2,3}` with
integer sort.

Next: **EP96** (8/26 Fri) — the army. Myeongjun stops short of the third line
once more; ten days of checkpoint fatigue; the receiving agencies ask how long
this runs; and **Seojin nearly states an opinion for the first time** (the next
step after EP92's `제 생각은 안 적었습니다`). **No US element** — sealed to the
next arc.

## EP96 approved (2026-08-20) — the reason arrived by accident

**EP96 「둘이 되면」** (`101_EP096_승인완료`, standard, 4,773 chars, 8/26 Fri,
**army-only chapter** — the family never appears) is `GATE_D_PASS`. State =
**SNAP-096**, tracker SNAP-096, ledger **v1.91**. **S12 is 4/11; sub-arc ①
closes.**

**Eleven days, eleven identical lines.** `한 번 적히면 사실이고, 두세 번
적히면 확인이고, 열한 번 적히면 그건 다른 뜻이 된다. / 여기 아무것도 없다는
뜻이거나, 아니면 우리가 못 찾는다는 뜻이었다. / **없는 것과 못 찾는 것은 종이
위에서 똑같이 생겼다.**` Eighty-two premises re-checked — the repair shop among
them, visited twice and then **written off as clear**; the concealment is now
complete *in the record*. Both receiving agencies write in (electronically —
user's fix), politely, asking the same thing: **how long?** This is EP89's
deferred question arriving: `물어보면 그때 대답한다` — and the time is now.

**★★★ The species column comes up blank.** Two observation posts, 2 km and
4 km apart, independently report an upper body and a lower body that look like
different species. **User's catch:** a two-species day already happened in
spring (EP37–40) — so the line is now about the *difference*: `그때는 줄을 두
개 썼다. 두 마리니까 두 줄이면 됐다. / **이번엔 한 마리다.** (…) 표는 마리
수를 세게 만들어져 있고, **한 마리 안에 종류가 둘일 수 있다는 건 계산에
없었다.**` Seojin's phrasing lands exactly where Sua's did in EP95 —
`하나를 쓰면 반만 쓰는 게 되고, 둘을 쓰면 두 마리가 됩니다` — **two tables
hitting the same wall, neither side knowing about the other.** Myeongjun's rule
for the entry: record only what was seen, no interpretation — `해석을 붙이면
다음 사람이 그 해석부터 읽는다`.

**★★★ And the reason to keep the net arrives by accident.** Eleven days of
nothing means fold; but Tuesday's appearance — again near Gurae-dong — makes
`해당 지역 인근 출현 지속. 관리 강화 유지 필요` writable. `화요일에 그것이 그
근처에 안 나왔으면 오늘 접었다.` Myeongjun cannot feel relieved: **the answer
he wanted came from the accident side, not from his hand.** So the third line
stays unwritten for a fourth day, now for a second reason: **`근거가 상황에
매여 있으면 그건 근거가 아니라 운이다`** — and `운이 끝나는 날에 그 자리에 서
있는 건 결재한 사람이다`. He also notices what he is doing: `쓸 수 있으려면
무슨 일이 있어야 하는지를 생각하다가, 생각이 어디까지 갔는지 알고 거기서
멈췄다. (…) **여태 기다린 건 저것들이 오는 날이었다. 오늘 기다리는 건 그게
아니었다.**` **August 31st becomes the thing he was waiting for.**

**★★★ Seojin nearly agrees, and that is why he is cut off.** `저도` and no
further — he isn't sure afterward whether the commander stopped him or he
stopped himself. Myeongjun's reason completes EP92's rule: one person thinking
something is odd is a private thought; **two makes it an assessment**, an
assessment enters a document, a document becomes grounds, **and grounds are
what you stand people up with.** `자네가 본 게 뭔지는 안 물어보겠다. 나도 내가
본 게 뭔지 설명이 안 되니까.` In the corridor Seojin is relieved and, oddly,
disappointed — `물어봐 줬으면 했던 것 같기도 했다`. **The restraint holding the
seizure back is now explicit, and it is Myeongjun's own; the day it lifts is
the E phase.**

One crack in "또 거기": four months of position entries lean one way (not March;
from May a little, visible from July), and the geography explains it perfectly —
`설명이 되는 것과 납득이 되는 건 달랐다. / **저것들이 지리를 보고 오는 게
아닐 수도 있었다.**`

Next: **EP97** (8/28 Sun) — sub-arc ② 「전야」 opens. Dana's body goes back
down (the 8/24 aftermath) with four days to the new term, and **the promise for
the 31st starts looking unlikely.** Then EP98 (8/29 — **Sua offers to go
first**, Dana says not today), EP99 (8/30 — an evening where nothing happens),
and **EP100–103 = August 31st**.

## EP97 approved (2026-08-20) — flat, which is worse than falling

**EP97 「그대로」** (`102_EP097_승인완료`, standard, 4,692 chars, 8/28 Sun,
Dana POV) is `GATE_D_PASS`. State = **SNAP-097**, tracker SNAP-097, ledger
**v1.92**. **S12 is 5/11; sub-arc ② 「전야」 opens.**

**Four days identical.** Since the 8/25 drop, the 26th, 27th and 28th are the
same: the sitting-up sequence, twelve steps to the floor room (it used to be
eight), two hands for a bowl, half a dinner, and the naps that arrive while
sitting and leave her unrested. `나빠지는 건 무섭지만 방향이 있다. 방향이
있으면 어디까지 갈지 짐작이라도 한다. / **그대로인 건 방향이 없었다.**` She
recognizes the shape from late July — once it settles on the floor, it stays.
**The morning check regresses**: EP93 had her measuring and recording nowhere;
now she measures and **compares to yesterday** — `비교하면 세는 거였다`.

**★★★ Sua starts keeping a record with no title.** She asks first (`요즘 계속
늦게 나오잖아` / `그저께는 더 늦었어` — user's fix makes the observation a
*span*, not a day), explains how she knows (`밥 차려 놓고 기다리니까 알게 돼`),
then brings out a sheet that is **not one of the four tables**: dates written
down the left, 25 · 26 · 27 · 28, and the right side blank. `수아는 뭘 적을 때
제목부터 쓰는 애다. (…) **이건 제목을 뭐라고 붙일지 못 정한 것 같았다.**`
Dana can't take it away — being asked *why* would need an answer she doesn't
have, and forbidding it would make it a thing worth hiding. `몇 줄부터 다른 게
되는지는 아무도 안 정해 놨다.`

**★★★ Yeongjin cannot say the sentence.** In late July he said `당분간 안
나간다` — and, per the user's correction, **there had been no alert for a long
while**, so the words changed nothing in practice. Now she went out four days
ago and won, so saying it drags something behind it: **`그러면 누가 나가나.`**
So he asks about rice, water, sleep — the three things left — and `가방은
싸냐` / **`천천히 해라`**, which lands on her as *it's all right if it isn't
done in four days*. He stops half a second at the doorway and says nothing.
**This is the adult-side ground for `오늘은 네가 나가라` on the 31st.**

**★★★ She cannot answer Hyejeong.** The text is deliberately light (`개학 나흘
남았다. 문제집 아직 반 남음. 큰일.`) and therefore harder to answer: saying
she's fine is a lie, saying she isn't shakes the 31st, and writing `봐서` is
**the word she used all summer** — the very absence of which Hyejeong took as
reassurance in EP94. So she leaves it: **the read receipt turns on and no reply
goes.** The reason for delaying is hope — `사흘이면 나을 수도 있었다. 나으면
그때 가겠다고 쓰면 된다.` Close: `지우지 않는 것과 갈 수 있는 것은 다른
일이었다. 그건 알았다. / **알면서 안 지웠다.**` And Sua's light is on down the
hall; she doesn't ask what for.

**Date audit (and a retroactive fix).** Checking that 8/28 → 8/31 is **three
nights** surfaced an error in EP95: 8/25 → 8/31 is **six**, not seven. EP93
(eleven) and EP94 (nine) were correct. **EP95's approved text was corrected in
three places**, and the arithmetic now closes properly — `저번에 엿새 걸린
적이 있으니까 **딱 맞겠다**`.

**Process note:** after EP95's missed honorifics, Sua's dialogue is now checked
**scene by scene** at draft close — 16 lines verified here. `check_voice.py`
cannot catch Sua's register because it can't identify the listener.

Next: **EP98** (8/29 Mon) — the sisters talk head-on rather than pricking each
other. **Sua offers first — `내가 나갈게`** — and Dana says **not today**.
She does not say anything about tomorrow.

## EP98 approved (2026-08-20) — the rehearsal for the 31st

**EP98 「오늘은」** (`103_EP098_승인완료`, important, 4,936 chars, 8/29 Mon,
Dana POV) is `GATE_D_PASS`. State = **SNAP-098**, tracker SNAP-098, ledger
**v1.93**. **S12 is 6/11.**

**★★★ Sua's untitled sheet reaches a conclusion.** Five dated rows with times
filled in, and above them **one blank row: August 24th**. User's correction
made that blank far better — the 24th isn't unrecordable, it's the day she
**got up fine**: `적을 게 없어서 비워 둔 게 아니라 **적을 이유가 없어서** 비워
둔 자리였다. **그날은 잘 일어났다.**` The last normal morning survives as an
empty line.

**Wake times were rescaled 8 → 10 o'clock** (user: half past eight isn't a
lie-in during vacation). The point stops being lateness and becomes
**consistency**: `방학에 10시면 늦잠이라고 할 것도 없다. (…) **늦잠은 어쩌다
자는 거였다.** / 이건 닷새가 같았다. 10시 10분, 10시, 10시 20분, 10시 5분,
10시 15분. **늦잠이면 이렇게 안 나온다.**` Baseline moved to *8 o'clock at the
start of vacation* (vacation-to-vacation comparison), and the knock-ons went
with it — she can't claim she's able while being someone who got up at 10:15,
and **she wonders for the first time whether she can climb the hill on the
first day of term** (she'd only been counting to the 31st).

**★★★ Sua reads it out, and there is nowhere to put the anger.** No accusation,
no temper — the same voice she uses for the tables, because she is reading a
table: 7/25 after training, after 8/3, after 8/12, and now. **`나간 다음
날부터야.`** Dana can't argue: she reached the same conclusion herself in EP95.
`혼자 생각한 건 접어 둘 수 있었다. 생각은 접으면 안 보인다. / **수아가
말하니까 안 접혔다. 말은 나오고 나면 방에 남는다.**` And: `저번엔 나쁜 뜻이
없어서 아팠고 **오늘은 아예 뜻이 없었다. 있는 걸 읽었을 뿐이다.**`

**★★★ Then she offers, first, unprompted: `그러니까 내가 나갈게.`** Every
previous sortie was granted to her or forced by circumstance; this one she
raises **with no alert in progress**. Her grounds: `언니가 안 나가면 안
나빠지잖아` — **`두 번. 둘 다 이겼어`** (7/28 and 8/8, corrected from a wrong
"six"; canon has exactly two) — **`그리고 나는 다음 날 안 아파`**. She also
**kept the order**: she didn't ask her grandfather first, because asking him
would turn this into a notification for her sister. `존중받으니까 더
곤란해졌다.` (Nieces' ages corrected too: **three years apart**, 6th grade and
3rd.)

**★★★ Dana's answer is the title.** She has no refusal left — not age (three
years, and she's an elementary student herself), not danger (she's the one who
also collapses after), not competence (`10시 15분에 일어난 사람이 할 말이
아니었다`). So: **`오늘은 안 돼.`** Because there is no alert today, and
**that is true**, so Sua can't argue either. Neither of them says anything
about tomorrow. At night: `안 된다고 하면 거기서 끝인데, 오늘은 안 된다고 하면
오늘이 지나간 다음이 남는다. **남겨 놓은 것은 언젠가 쓰게 된다.** / 쓰려고
남긴 건 아니었다. 그건 확실했다. / **확실한데도 남긴 건 남긴 거였다.**`
**The consent given on the 31st is manufactured here.**

**Numeral policy changed (user):** dates and clock times are now **Arabic
numerals** (`8월 31일`, `10시 15분`), while spans stay in hangul (`닷새`,
`두 밤`, `넉 달`) because those are how a character counts, not measurements.
**EP93–97 were retro-fixed — 21 instances**, all five chapters still inside
their length bands with `check_continuity` clean
(`Black_Titan_소급정정_2026-08-20_숫자표기_v1.0.md`). The showcase is EP97's
sheet: `이십오. 이십육. 이십칠. 이십팔.` → **`25. 26. 27. 28.`** — hangul reads
as prose, numerals read as a table, and "writing it down binds it together" is
the point of both chapters.

Next: **EP99** (8/30 Tue) — **an evening where nothing happens.** Term
preparations, a family dinner, and the last ordinary day, which only the reader
knows is the last. Then **EP100–103 = August 31st**.

## EP99 approved (2026-08-20) — the day that got better was the last one

**EP99 「갈게」** (`104_EP099_승인완료`, standard, 4,735 chars, 8/30 Tue, Dana
POV) is `GATE_D_PASS`. State = **SNAP-099**, tracker SNAP-099, ledger **v1.94**.
**S12 is 7/11; sub-arc ② 「전야」 closes.**

**★★★ Six days flat, and then she wakes at 9.** Ten steps to the floor room
instead of twelve, one fewer stage in the sitting-up sequence, dinner finished.
Her own verdict is exact: `나은 거면 원래대로 돌아온 거고, **덜 나쁜 건 나쁜
자리에서 조금 옮겨 온 것뿐이다.**` She even recalls the precedent — `8월
3일에도 덜 나빴다. 그때 나은 줄 알고 나갔고, 나가고 나서 이틀 만에 도로
내려앉았다` — and then: **`그 생각은 오래 안 했다.`** This recovery is exactly
what makes "I could go out" available as material on the 31st.

**The bag opens for the first time since 7/22.** Vacation homework untouched;
the reading log gets a self-serving reading (`읽은 만큼 써 오라`, so nothing
read means nothing owed — user's line), and the diary is the real problem: ten
entries, and **the only usable day is the hospital visit**. `나머지는 쓸 수가
없었다. (…) 쓰면 안 되는 거라서 못 쓴다. (…) **다른 점이 있다면 이쪽은 진짜로
있었던 일을 빼고 쓴다는 것뿐이었다.**` Also the safety notice: `이 종이를 쓴
사람은 그 방송이 나오는 동안 어디에 있는지 생각해 본 적이 없을 것이다.`

**★ EP68 closes here.** In place of a flat "same class in the second term"
(user cut it as obvious), the classroom repair lands — and the duration was
corrected twice: the roof broke on **7/13** and the vacation started **7/22**,
so the temporary room on the special-rooms floor lasted **nine days**. `임시
교실은 창문이 반대쪽에 있어서 오후에 해가 안 들어왔고, **애들이 그 아흐레
동안 그걸 계속 불평했다.**` Nine days of annoyance is exactly what that
disaster became for the other children — during the same nine days Dana's pain
was unsealed (EP70).

**★★★ And she finally answers, with no hedge.** `**답장 보내는 거 깜빡했다.
미안. 내일 갈게.**` (User's fix: with the read receipt lit three times over
three days, "I saw it late" is a lie that gets caught; "I forgot to reply" is
the kind both sides let pass.) No `봐서`, no `아마`, no `될 것 같은데` — `붙일
필요가 없어서 안 붙인 거였다`. **EP94's reassurance signal is now genuine, and
that is why it hurts.** Hyejeong answers instantly: `ㅇㅋ. 내일 봐.`

**★★ The dinner table comes back for one night.** Loudest of the summer,
quieter than spring: the October recital, whether a chosen-but-unannounced
piece counts as chosen, Sua insisting she prefers playing second (`앞은 틀리면
다 보여`) while Dana privately knows she wants first — and decides not to say
so, because naming it makes her stop mentioning it. `둘 다 그만해라` fails, as
it always did in this house. **Nobody mentions her body**: `어제까지는 물어볼
게 있었는데 아무도 안 물었다. 오늘은 물어볼 게 없어서 아무도 안 물었다.
**겉으로는 똑같은데 안이 달랐다.**` Yeongjin watches the bowl empty and ladles
more soup without saying to eat more.

Close, with **zero foreshadowing of the 31st** (locked): `여름에는 아무 일도
없는 날이 이상한 날이었다. (…) **오늘은 그냥 반가웠다. 내일 할 일이 정해져
있으면 오늘 조용한 게 무섭지 않았다.**`

Next: **EP100–103 — August 31st across four chapters.** **EP100 the decision**
(a weak-looking enemy, her body, and `오늘은 네가 나가라` with all three
excuses true at once) → **EP101 dominance** (Sua at near-full sync, the best
she has ever fought) → **EP102 the impalement** (the feint, the turn, the barrel
driven in, dark red fluid, the spine, and Lucy with the White Sentinel firing
XLG-5) → **EP103 the family comes apart** (hospital / protective custody /
arrest, per G0-018).

## EP100 approved (2026-08-21) — the decision

**EP100 「네가 나가라」** (`105_EP100_승인완료`, important, 5,154 chars, 8/31
Wed afternoon, Dana POV) is `GATE_D_PASS`. State = **SNAP-100**, tracker
SNAP-100, ledger **v1.95**. **S12 is 8/11 — canon-fixed event ① complete.**

**Two days of improvement, which is what makes it a choice.** She wakes at
8:50, nine steps to the floor room (eight is normal — one to go), sharpens six
pencils for tomorrow. Not complete: fingertips still tingle, standing long
still shows. But: **she could have gone.** Going would have cost her the first
day of term, and *accepting that cost, she could have gone.*

**The alert catches her with her shoes on** — 2:30, half an hour before a 3
o'clock meeting. **User's structural note fixed the motif**: the lift is reached
through the shop, so shoes are correct; the point is different — `가게를 지나서
승강기를 타야 하니까 신발은 신는 게 맞다. **문제는 이게 나가려고 신은
신발이라는 거였다.**` (Also corrected: nobody calls her from the basement —
voices don't carry that far and the routine needs no calling.)

**★★ The radar tells them only what EP96 established** — count and size, never
shape. One, small, slow, still far: **it looks easy.** And `합성 여부는 확인할
방법이 없다` — EP95's experience is useless here, because nothing on that screen
can show it.

**★★★ Three excuses, all true.** (1) *Term starts tomorrow and going costs it*
— spoken, and immediately after: **`수아도 내일 개학이라는 건 뒤늦게
떠올랐다`** (user's line, which quietly dismantles the excuse). (2) *It's small
and slow* — spoken. (3) *I hate watching my sister be good at this* — **never
spoken**, and in her head **it came first**: `그 생각이 앞의 두 개보다 먼저
왔다. 순서가 그랬다는 걸 단아는 알았다. (…) 알고 나서도 그 자리에 그대로
있었다.` Why she can't say it: Sua would understand, and might start hiding
what she's good at — `잘하는 애가 잘하는 걸 숨기게 만드는 건 언니가 할 일이
아니다`.

**★★★ And the contradiction gets named as unnameable** (user's prompt): `보기
싫으면 안 보내면 된다. (…) **그런데 안 나가고 내보냈다.** (…) 심술 같은 건가
싶었는데, 심술이면 뭐가 심술인지가 있어야 하는데 그것도 잘 안 잡혔다. /
**이름을 못 붙이는 게 요즘 하나 더 늘었다.**` Since EP92 that condition
belonged to Sua; now both sisters carry one unnamed thing into August 31st.

**★★★ The cancellation window, unused.** Between saying it and Sua leaving to
change, there was time. `세어 볼 만큼 길지는 않았고, 말하기에는 충분한
길이였다. / 단아는 그 시간을 안 썼다. / **못 쓴 게 아니었다. 쓸 수 있었는데
안 썼다.**` Yeongjin doesn't object — there is nothing to object with, since
both spoken reasons are true — and says only `장비 점검하고 나가라`, the
ordinary sentence that is the one ordinary thing in the room. Sua takes the
answer without surprise or pleasure.

**The appointment is cancelled by the alert, not by her.** Hyejeong texts
`경보 났네` and **`내일 학교에서 보자`**; Dana answers `응. 내일 봐.` — **no lie
required**, all summer's first such exchange, and `만들 게 없어서 편한 게
이상하다`. (Precedent corrected per user: the spring event that was cut short
was the **sports day**, EP24, whose rescheduling notice simply appeared on the
board — `묻는 게 아니라 아는 거였다`.) Then the excuses are struck one by one:
not the appointment (the alert erased it, and the order was reversed anyway),
not the body (two good days, she could have gone) — and what remains is one
thing. She takes off the shoes she put on to go out, having gone nowhere:
`경보 때문에 못 간 사람들하고 자기는 달랐다. / **그게 자기가 정한 거였다.**`

**Foreshadowing discipline held: zero.** Two slips were caught and removed
mid-draft (`나중에 세어 보게 된다`, `나중에도 잘 모르겠다`); the final text has
no future-tense narration, no `마지막`, no dread. The reader's knowledge does
all the work.

## EP101 approved (2026-08-21) — dominance

**EP101 「가볍다」** (`106_EP101_승인완료`, important, 6,038 chars, 8/31 Wed
afternoon continuous, Sua POV with one observation-room crossing) is
`GATE_D_PASS`. State = **SNAP-101**, tracker SNAP-101, ledger **v1.96**. **S12
is 9/11 — canon-fixed event ② complete.**

**★★★ The chapter's top-level device is a style switch, explained nowhere.**
Scenes 1–2 use the ordinary control vocabulary (`앵커를 걸었다`, `결속 해제`,
`계기`). At the chain swing in scene 3 it changes, and from there to the end of
the chapter **every control word is gone from Sua's sections** — verified by
script: zero instances of 앵커/결속/사출/점화/되감기/기체/조종간/계기/콕핏/
해치/조종석. What replaces them is the body: **팔을 휘둘렀다 · 쳐냈다 · 손이
닿았다 · 발로 밀었다.** The reader ends up reading her as fighting with her own
body, and **no causal sentence is spent on it.** Dana's observation-room
section keeps the control words — from outside it is still a machine.

**★★★ The return point is EP102, immediately after the impalement** (user's
call: the impalement must land at peak sync, so the body-prose must still be
running when it happens; the control words coming back is what reveals it was
never her body).

**Near-full sync, shown as phenomena only** — no cause, no system-compatibility,
no name for the pleasure. The lag: half a beat on 7/28, narrower on 8/8, **not
visible on 8/31** (`고칠 게 없었다`). The body: `팔을 들면 팔이 들렸다`, five
fingers closing at once. And **it is light** — she knows that makes no sense,
so **she doesn't say it**: `무겁다고 하면 걱정할 사람이 있는데 가볍다고 하면
뭐라고 할지 몰랐다`. She never thinks *good*; she thinks **잘 된다**, and the
chapter closes on `오늘 좀 되네`.

**★★ The chain swing is inherited.** Sua watched EP91 on the monitor twice —
once plainly, once to see *how* — and got as far as knowing it is swung
sideways, not overhand. She has never done it, not even in training. **It works
better for her**: the circle doesn't buckle, there is no stopped moment to
recover from, and she resizes it with her wrist. `그리는 것과 되는 것 사이가
없었다.`

**★★★ User's terrain constraints (set for EP102–103).** Reclamation-flat
tidal ground outside a broken seawall. **Water below knee height** — it must
stay low enough that the dark red fluid pouring out is visible next chapter —
and it **drops further during the fight** (the waterline on the wreckage rises
a hand's width). The bottom is **hard-packed: a vehicle could drive in once the
tide is out**, which is how EP103's convoy arrives. Sua has the thought about
vehicles once and puts it aside.

**★★★ Two user corrections rebuilt Dana's section.** (1) *There is no wide
shot* — nothing films the battlefield except the cockpit, so the observation
room has **two screens** (cockpit view, machine status) and Dana can only watch
through her sister's eyes. (2) *The view doesn't rotate* — the body stands
still and only the arm swings. So what the screen shows is **the chain crossing
the top of the view once per revolution**, and Dana **counts the interval**.
She can read it because she has swung one: when the circle buckles the interval
slips, and recovering costs a full turn. `8월 18일에 자기 것은 여러 번
어긋났을 것이다. (…) 못 봤지만 어긋났을 것은 안다.` / **`동생 것은 안
어긋났다. 몇 번을 세도 같은 간격이었다.`** The girl who couldn't count her own
kills in EP91 counts her sister's revolutions exactly.

**★★★ Dana's order is the EP82 mirror, completed.** Her shoulder drops before
she knows it was raised; **relief comes first**; and then something else —
`보기 싫은 건 아니었다. 보고 있으면 눈을 떼고 싶고, 떼면 다시 보게 됐다.` She
does not name it, and **says nothing** (Yeongjin is beside her, watching
pressure, temperature, coupling — **sync depth is not on the list of things
anyone looks at**).

**★★ The creature, exterior only** (G0-017, species names zero on the page): a
large smooth spiral shell with **no opening anywhere** — Sua checks it in the
same order she reads the instruments and finds `볼 데가 없었다` — long
tentacles, eight or more, and a beak inside the mouth of the shell. **No barrel,
no hint of the feint.** She reads it correctly as a grappler (`잡히면 지는
것`), answers `안 잡혀요` for the first time instead of `알겠어요`, and never
closes inside chain range: `사슬이 닿는 데까지가 이쪽 자리`.

**★★★ New canon, three items.** (1) The observation room has **two screens and
no external camera**. (2) The chain swing is **sideways**, and on-screen it
reads as **interval**. (3) **The chain tip goes supersonic** — user's addition,
kept in full but moved into body-prose since `앵커` is a banned word after the
switch: `손목은 아까와 똑같이 도는데 끝은 그보다 훨씬 크게 돌아서, 어느 지점을
지날 때마다 쩡, 하는 소리가 났다. 소리가 난 자리에 희뿌연 것이 한 겹 생겼다가
흩어졌다. / **그 소리는 처음 듣는 것이었다.**` Whip physics, and it lets the
chapter close on an upward curve.

**Foreshadowing discipline: zero.** The two `몰랐다` hits are both present-tense
ignorance (nothing to say it to; no name for the feeling), not narration that
knows what comes.

## EP102 approved (2026-08-21) — the impalement

**EP102 「돌아선다」** (`107_EP102_승인완료`, important, 5,840 chars, 8/31 Wed
afternoon continuous, Sua POV with one observation-room crossing) is
`GATE_D_PASS`. State = **SNAP-102**, tracker SNAP-102, ledger **v1.97**. **S12
is 10/11 — canon-fixed event ③ complete.**

**★★★ The user rebuilt the chapter's shape at brief stage**: the fight had been
at chain range all along, so the kill has to be made **close**. She drives the
anchor deep, **walks up to it, pulls it out with both hands** (a foot braced on
the shell, one slip, then it comes free), confirms the thing is dead **four
separate ways** — no movement, no tentacles, the beak stopped open, **no
sound** — and turns to walk back. **She is struck from behind.** Her reason for
closing is that she breaks her own EP101 rule (`사슬이 닿는 데까지가 이쪽
자리`) on evidence that is entirely reasonable: the circle only ever cracked the
**outside** of the shell, all eight tentacles are lying slack, and Yeongjin
doesn't forbid it — he only demands the check (`촉수 확인하고 가라` →
`천천히 가라`).

**★★★ And nobody sees it — because of the canon EP101 established.** There is
no external camera; the observation room sees only what the cockpit sees. So
when the user caught the remaining inconsistency (*if Sua saw the thing come
out of her belly, Dana and Yeongjin saw it too*), the fix was the other option
he offered: **she feels it and cannot look down.**

> 보려고 했다. / **고개가 안 내려갔다.** / 내려다보면 되는 것이었다. 아래를
> 보라고 하는데 아래가 안 왔다. 하려는 것과 되는 것 사이에 뭔가가 있었고,
> **그건 아침부터 지금까지 한 번도 없던 것이었다.**

**That inverts EP101's proof of dominance exactly** — the absence of lag was
the sign; its return is the first mark of the spine, and the word *spine* is
never used. It widens in scene 5 (her neck won't turn: `그 사이에 있는 게
넓어져 있었다`). **What everyone sees instead is the water at her feet going
dark red** — `어디서 나오는지는 안 보였다`. Sua, Dana, Yeongjin and the reader
all watch the same screen and none of them sees it happen.

**Note the distinction (user's):** what is missing is **the sight, not the
facts**. What happened will be told afterward — by Sua, by the damage to the
machine, by the army's examination. Only the moment itself goes unwitnessed. So
Dana's guilt takes the shape of **"I was in front of the screen and I did not
see it,"** not "I didn't know" — and every later explanation sharpens what she
missed.

**★★★ The style device closes.** The control vocabulary, dropped in EP101 scene
3 and absent for about a chapter and a half, comes back all at once at the head
of scene 4 — alarms, every instrument red, a coupling indicator that goes dark,
`조종석 안이 붉었다`. **The return is the event; not one sentence explains it.**
Then the order of knowing: **아프다** (the name arrives and drags everything
that already hurt in with it) → she puts a hand on her stomach, **and the hand
goes** — nothing is pierced → **it doesn't stop hurting** → `여긴 내 몸이
아닌데`. `손으로 만지는 자리와 아픈 자리가 같은 자리인데, 하나는 멀쩡하고
하나는 아팠다. 둘 다 자기 배였다. / **아까까지는 그게 하나였다.**`

**★★ Dana's crossing (user's correction).** Not the chain interval — after the
close-quarters shift there is nothing to count. It is **the walk**: the frame
swaying naturally over the flats **lurches once, hard, and stops.** She saw the
impalement and could not read it — `그게 무슨 흔들림인지는 몰랐다. 걷다가 뭘
밟아도 화면은 흔들렸다.` She stands up, which changes nothing, because there is
nowhere for an answer to come from. Her only line is **her sister's name**.
Yeongjin, for the first time, looks at the part of the display that was never
on his list.

**★★ Then, still with nothing visible**: something streaks past the edge of the
view toward the rear **trailing a single wire**; the explosion arrives as a
shove in the back **before** it arrives as sound; and a **하얀 거인** walks in
from the left, unhurried, water refusing to push ahead of it, **with the gait
of something that already knows what is here.** Name, affiliation, armament,
face and voice: **zero**. Sua knows only that it is white, and the view starts
receding while her eyes are still open.

**★ Two new canon items.** (1) **Dissolution is depth-dependent** — `녹지는
않는데요` / **`물이 얕으니 시간이 걸릴 거다`**; this is why wreckage is still
there for the army in EP103. (2) **Cockpit scale is measured against the
machine's own forearm** — "a person's height" is not a usable unit (EP101's
beak was retro-corrected to `벌어지면 이쪽 팔이 통째로 들어가고도 남을 폭`).

## ★★★ Tracker freeze, found and repaired (2026-08-21)

**The foreshadow tracker had been frozen since EP067.** `SNAP-068` through
`SNAP-102` — 35 files — were byte-identical to SNAP-067 except for the ID
string. Cause: the chapter-close scripts patched a key named `approval_note:`,
which **this file does not have** (`last_updated_by:` plays that role). `re.sub`
matched nothing, returned the text unchanged, and the only verification run was
`yaml.safe_load`, which passed. Every "tracker updated" report in that stretch
was wrong. (The file's own header records the *same* accident happening once
before, at SNAP-062~067.)

**Repaired:** `SNAP-102` is now rebuilt from the 35 Gate-E state reports —
`as_of_episode: 102`, all 18 pre-existing entries re-advanced, **9 new S11–S12
entries** added (sync-style device, unwitnessed, one lurch, turning words, own
rule broken, no-lag inverted, wire, dissolution depth, inherited chain spin),
and an `ep_log_068_102:` block carrying each chapter's Gate-E summary verbatim.
SNAP-068~101 keep their frozen content but now carry a header note saying so.

**★ Verification to run at every chapter close** (not just `yaml.safe_load`):

```
as_of_episode == this chapter number
```

If it doesn't, the tracker did not update.

## EP103 approved (2026-08-21) — the family comes apart (S12 and arc close)

**EP103 「각각」** (`108_EP103_승인완료`, important, 5,697 chars, 8/31 Wed
afternoon→evening continuous, **Dana single POV**) is `GATE_D_PASS`. State =
**SNAP-103**, tracker **SNAP-103 (`as_of_episode: 103`)**, ledger **v1.98**,
plus **arc capsule S12**. **The summer arc is closed.**

**★★★ The user reshaped this chapter twice at brief stage.** First: *신병 확보
후 신원확인이 이뤄져야 다음이 있는데 갑자기 잡아가면 안 되지* — so the army
has an **unidentified child** and nothing to check her against, and the family
walking up to the line is what supplies the identity. Then: *영진이 자진해서
잡혀들어가는 모양새가 되어야겠다. 이미 늦어서 군이 수아를 확보한 것을 본 이상,
조사가 아이들이 아닌 자신을 향하도록 돌려놔야 하니까.* That became the
chapter's spine.

**Yeongjin speaks before he is asked**, from a distance where they may not even
hear him: `내가 만든 겁니다` / `내가 만들었고, 내가 태웠습니다. 책임자는 나요`
/ `내가 내보냈으니까 알지요`. **No lie** — this serial's standing rule — and
crucially **he never mentions the children at all**; talking only about himself
is how he keeps them out of it, and **that reasoning never appears on the
page.** He hands over his ID unasked (one-handed, as always), **does not take
Dana's side** when she asks to ride along (siding with her would point the
relationship back at the child), never once looks at her during the wait, and
at the word 체포 — which appears exactly once — **puts his hand out before they
reach for it.** `이렇게 될 걸 알고 있었던 사람의 동작이었고, 단아는 그게
언제부터 알고 있었던 건지를 생각하다가 그만뒀다.`

**Dana supplies the identity without knowing it.** `"수아야!"` — `참으려던 게
아니었다. (…) 그냥 나왔다` — and heads turn inside the line. That is the second
utterance in four chapters to cause the thing it causes (after `오늘은 네가
나가라`), and **neither is ever assigned blame on the page.**

**★★★ The pose (user-specified):** knees driven into the flat, arms hanging
slack with the backs of the hands in the mud, torso tipped forward at an angle
that goes no further either way — `넘어진 게 아니라 앉아 있는 것 같았다` /
`멈출 힘은 있었는데 일어날 힘은 없었던 것처럼` — **while the white giant
stands.** `하나는 꿇었고 하나는 섰다`, and the contrast is never summarized.
Tipped forward, **the back is visible**, which is the angle the cockpit feed
never had: `관측석에 앉은 사람은 등이 어떻게 생겼는지 볼 일이 없다`. The
gouge the knees plowed shows which way it was heading — **`돌아가는 쪽이었다`**.

**★ User's line edits carried three canon items.** (1) The wound is **a hole
dead center in the waist**, armor curled inward, punched **back to front** —
EP102's direction confirmed from outside for the first time. (2) Sua is
**uninjured**: `얼굴에도 옷에도 아무것도 안 묻어 있었고, 어디도 다치지
않았다` → **`다친 데도 없는데 왜 눈을 뜨지 못하는 걸까`** — the spine line gets
its on-page evidence without ever being named. (3) **The white giant is simply
gone** — `흰 거인은 어느샌가 사라지고 보이지 않았다`; nobody saw it leave,
nobody spoke to it. Also: a **shirted man**, not a uniform, arrives late to read
the name — **the arrest is not the army alone**.

**A caught error worth remembering:** the draft gave Dana's age as sixteen.
Canon says **단아도 아직 초등학생 — 6학년**, with **Sua in 3학년** (three years
apart). Corrected to `"몇 학년이니?" / "6학년이요."`, and the brief's "열세
살짜리" became **"초등학교 3학년짜리"**. It makes Yeongjin's motive heavier:
left alone, the investigation lands on a third-grader, and the only remaining
guardian is a sixth-grader.

**The close is the tide.** Ebb ends, the wreckage finally starts dissolving
(EP102's depth rule paying off), crews let go and step back: **`놓은 자리에
물이 들어왔다. 들어온 데는 다시 안 나왔다.`** Last line of the summer:
`뻘이 안 보이는 쪽으로 들어섰다`. **Foreshadowing stayed at zero to the end.**

**★★★ Tracker verification is now in force.** The freeze repair set the rule,
and this close was the first to apply it: `assert as_of_episode == 103` — it
passed. `yaml.safe_load` alone would not have caught the old failure. Tracker
now carries **32 active / 11 resolved**, including the closed arc entry
`A-S12-LAST-DAY-OF-SUMMER`.

Next: **S13, autumn.** No Level 4 outline exists yet — that is the next
document. The arc leaves: **Sua in a hospital Dana cannot name**, **Dana in
protective custody**, **Yeongjin in detention**, the machine in army hands with
a hole in its waist, and **whether his diversion worked left undecided** — that
is the opening stake. Still sealed into the next arc: **Myeongjun must not meet
Yeongjin, US contact stays at zero, Lucy does not speak, the field is never
named, and what went through Sua stays off the page.**

## S13 autumn opens — EP104–109 approved (2026-08-21/22), sub-arc ① closed

**Level 3 skeleton and the S13 outline exist now.** Autumn runs **80 chapters
across S13–S17** (`04_가을편_기획/Black_Titan_가을편_Level3_골격_v1.0.md`), and
**S13 「흩어진 이름」 is EP104–120 (17 chapters)**, `LEVEL4_PASS`. Supporting
approvals from the same planning block: **G0-019** (10 items — Sua is
right-handed, Lucy is 8 but looks ~17 and knows what she is, Yeongjin already
knows Myeongjun commands the southern command, Hyeonseo's team rode the carrier
*Carver*), the autumn **stage structure**, the autumn **name list** (12 named +
22 reserve), the **cast reshuffle**, and **voice cards for autumn** (Lucy and
Hyeonseo in detail). A retroactive correction also landed: **the arrest was made
by a detective, not the army** — civilians are not arrested by soldiers.

**Sub-arc ① 「흩어진 뒤」 (EP104–109) is closed.** All six are `GATE_D_PASS`
with delta and Gate E applied. State = **SNAP-109**, tracker SNAP-109
(`as_of_episode: 109` verified), ledger **v2.04**. Folders `110_EP104_승인완료`
through `115_EP109_승인완료`.

| EP | Title | POV | Chars |
| --- | --- | --- | --- |
| 104 | 목록 | Dana | 4,947 |
| 105 | 집안 사정 | Hyejeong | 4,851 |
| 106 | 순서 | Sua | 4,972 |
| 107 | 모레 | Dana | 4,694 |
| 108 | 안 부른 말 | Dana | 4,959 |
| **109** | **먼저 부른다** | **Sua → Dana** | **6,004** |

**The shape of the sub-arc: everyone hits the same wall separately.** EP104 and
EP106 are deliberately parallel — the resident adult knows the procedure and
does not know the person, both girls get the same answer, both miss the start
of term. EP105 keeps the school thread alive without spending it: Juho says
only `집안 사정이 있어서 당분간 못 나온다`, the class moves on, and **only
Hyejeong doesn't.** EP107 establishes that nobody at the facility knows
Yeongjin. EP108 brings the mother.

**★★★ EP109 is where one thing finally opens — and the one who opens it is the
younger sister.** Hyeonseo cannot say it herself (`엄마가` self-reference is
barred by her voice card, and she cannot apologize), so **she only gives her
name — 「도현서」 — and Sua does the arithmetic.** The chain runs on real Korean
practice, per the user: **spouses do not change surnames**, so a mother usually
has a different surname from her children; 도씨 is uncommon (Dana and Sua are
the only two in the school); **the grandfather is the mother's father, which Sua
has always known** and which the page treats as unremarkable; therefore the
grandfather's daughter is still 도 — **mother or aunt**; 고모 is ruled out
(`수아는 아빠 쪽 사람을 한 번도 본 적이 없다`), and **이모 is ruled out by
guardianship** — medical information goes only to `직계이거나 지금 키워 주고
있는 사람`, and the doctor told this woman about the legs.

So Hyeonseo does not reveal herself; **she is caught.** `"아줌마 누구예요."` →
silence → **`"엄마예요?"`** → **`"…응."`** Everything after that is material Sua
never asked for. **Sua does not believe, she checks** — the cognition
trichotomy on the page: `언니는 먼저 느낀다. (…) 수아는 반대다. 먼저 알고
나중에 느낀다`, and she does not cry because `아직 다 안 끝난 것 같았다`.

**★★★ The first use of 「엄마」 sits in front of a request.** `엄마.` →
**`언니 좀 데려와 주세요.`** — Sua did not gain a mother, she gained someone who
might bring her sister, and the answer is `해 볼게`, the same construction as
EP108's `해 뒀어` (meaning: not yet). The comfort line **`이제 더 이상 안 싸워도
돼` is refused** — `언니는요.` — because exemption granted to one person is not
exemption; the page uses cleaning duty: `한 명만 빠지면 그건 그냥 그 한 명이
나쁜 거였다`.

**★★★ The sisters now mis-know each other in both directions, and neither gap
is narrated.** Sua reads the silence after `언니한테도 말했어요?` as *언니는
아직 모르는구나* — **wrong**; Dana learned yesterday and simply did not call her
anything. Dana, for her part, **does not know her sister called the woman
mother**, and the text never says she doesn't — the piece is just absent while
she builds her conclusion. Tracker entries: `FS-S13-CALLED-MOTHER-DONE`
(reveal after the sisters meet, S14↑) and the earlier `FS-S13-NO-TRACE-VISIT`.

**That earlier one matters for how EP108 now reads.** The user fixed the nature
of Hyeonseo's first hospital visit: **she watched from a distance and left
without speaking, because she could not bring herself to.** No contradiction on
the page — she said `다녀왔으니까`, never that she met anyone — and **EP106 had
already planted it**: `왔다 간 자국이 방에 없었다. 꽃도 없고 가방도 없고 옷도
없었다`, the same trait as arriving at the visiting room **empty-handed**.
EP108's line was retrofitted to `그러면 병실에 들어가서 봤다는 뜻이기도 했다`
so it reads as Dana's inference rather than fact.

**★★ It is also why Hyeonseo comes back the same evening** — yesterday she was
not called anything, today she was — **and why she cannot say so.** Steering
around the unsayable, something else leaks: **「수아는 이제 안 나가도 돼.」** The
sentence she meant was *너도*, which would have been a lie, **so she changed the
subject.** Dana catches three things: **나가다** (only someone who knows they
rode says it), **이제** (so there was a before), and **수아는** (which means *not
me*). She does not challenge it — `물어보면 대답이 나올 것 같았고, 대답이
나오면 그게 진짜가 되니까`.

**★★★ Which delivers the layer-2 wrong answer: `엄마가 우리한테 뭘 한 거다.`**
Wrong but persuasive — nobody did anything to them; they were born this way, and
**S15 6-7 turns it worse.** Two of the user's line edits sharpened it. First,
**sleep-learning was recovered** — it is canon from EP002 and appears on the page
in EP081 (`수면학습으로 뇌에 심어진 절차`) — so Dana's memory becomes `처음부터
손이 저절로 스위치를 찾아갔다. 수면학습으로 조종법을 머리에 넣었다고 했다.
단아와 수아, 둘만.` **The axis is no longer *how* but *why only us*:** `왜
우리한테만 넣어 놨을까.` / `다른 사람도 아니고 우리한테만.` Second, **the summer
symptoms belong to Dana, not Sua** — corrected twice by the user: **몸살, 미열,
손 저림, and no nosebleed**, after every sortie, **and she was never taken to a
hospital** (`자고 나면 낫는다고 했다`). That squares with EP100's guilt item ①
(`몸 — 이틀 연속 회복 → 나갈 수 있었다`) and gives the wrong answer its best
evidence: **`검사를 받았으면 뭔가 나왔을까.`** against Sua's `검사에서는 안
나와요`. **The numbness is in the same nerve family as Sua's legs, and the very
next paragraph is `단아는 손을 봤다`.**

**The close refuses to state the gap.** `부르려고 하면 안 나오는데 가리키려고
하니까 나왔다. / 같은 두 글자인데 그랬다.` — the younger sister used it as a
name, the elder as a pointer. A late user edit made the pairing tighter still:
**`도씨는 학교에서 언니와 수아, 둘뿐이었다`** in scene 2 rhymes with **`단아와
수아, 둘만`** in scene 5 — the same *two*, inverted.

**One `check_continuity` FAIL is deliberate and stays:** 「수아는 이제 안 나가도
돼」 appears twice, once spoken and once as the sentence Dana takes apart. The
three `check_voice` `저 사람` warnings are false positives — that guard is for
Yeongjin (who must be `할아버지`), and here the phrase is Dana still having no
name for this woman.

Next: **sub-arc ② 「이름」 (EP110–115)** opens with **EP110** (9/9 Fri,
**Myeongjun POV**) — the comparison result reaches his desk and **he is the only
one who is surprised**; no meeting yet. Then EP111 Yeongjin's silence, EP112
Hyejeong asks her uncle, EP113 the Americans and `세 사람`, **EP114 the
Myeongjun ↔ Yeongjin meeting** (the season's peak, unsealed at last), EP115 the
terms. **Still sealed:** the mechanism, the word 타이탄 in dialogue, the field's
name, Lucy speaking (EP116), and secret layer 3. **Open question for the EP111–115
briefs: what exactly Dana is suspected of** — that is the second-stage reason her
phone stops being a thing anyone can fetch.

## EP110 approved (2026-08-22) — the name (sub-arc ② opens)

**EP110 「이름」** (`116_EP110_승인완료`, important, 5,859 chars, 9/9 Fri,
**Myeongjun POV — the series' first close third on him**) is `GATE_D_PASS`.
State = **SNAP-110**, tracker SNAP-110 (`as_of_episode: 110` verified, 51
active), ledger **v2.05**.

**Four continuity corrections came from the user and are now canon for every
future flashback to August 31st.** (1) There was **no evacuation** — the siren
sent everyone indoors (EP100: `경보가 나면 시장이 닫고 가게가 닫고 다들 집으로
들어간다`), so no returning residents, no power or water restoration. (2) The
city took **no damage**: zero injured, zero dead, a stretch of breakwater and
two warehouses, because the whole fight happened out on the flats and ended the
same evening. The page makes that strange rather than reassuring —
`싸움이 물 쪽에서만 났기 때문이다` → **`안 들어온 건지 못 들어온 건지는 아무도
안 적었다. 적을 칸이 없었다`**, which rhymes with the blank disposition field
later. (3) **The machine's interior was entered on the day** — EP103 already
shows the back plate cut open, two men going down, and Sua carried out — so the
draft's "nobody has seen inside" was a flat contradiction and was replaced:
nine days of measuring and photographing produced a thick list where
`뭐가 있는지는 적었고 그게 뭐 하는 건지는 못 적었다`. (4) **What they cannot do
is switch it on** — `"안 켜집니다"`, damage confined to the waist, so
**`멀쩡한데 안 움직인다`** — deliberately the same sentence Dana used about
Sua's legs in EP109, with the reason sealed on both sides. They have the thing
and cannot turn it on, which is why "whose is it" has no answer yet.

**Recognition does not run through the name.** Myeongjun knows it instantly —
EP012 put a photograph of the two of them in his desk drawer, and the user
fixed the rest: **he thought Yeongjin was dead.** Accident → discharge → the
deluge → the war → no word. `죽었다고 확인한 적은 없었다. 확인이 필요한
시절이 아니었다` / **`없어진 사람이 너무 많아서 찾는 쪽이 이상한 일이 됐다`**
— so for thirty years that name was not a living person's name, and his eye
slides past it. **The address is what stops him.**

**★★★ And the address stops him twice, which is the user's other correction.**
Not just that a dead man is living twenty minutes away, but that **it is the
neighborhood he himself flagged in EP089** — where he had Yun order up three
months of coordinates, sightings and control records on `구래동`, could only
justify it as `인근이다`, and let her write **`미확인 대형체 인근 지역 예방적
관리 강화 요청`** into the reason field because the real reason was an
observation, not a ground. Nothing came of it for six weeks and he forgot.
**`맞혔다는 얘기였다.` (…) `맞혔는데 하나도 좋지 않았다.`** EP089 closed on
`적을 수 없는 이유로 움직이는 일이 이 방에서 두 번째였다`; EP110 moves that
counter to **세 번째** and adds **`이번에는 시킬 것도 없었다`**.

**The photograph leaves the drawer for the first time in 98 chapters** —
`손톱으로 밀어 올려야 나왔다. 위에 얹힌 것들이 삼십 년치 무게로 눌러 놓고
있었다` — and **the man in it has both arms**, taken before the accident, so it
cannot be matched against a record whose only physical note is
`좌상지 주관절 이하 결손` (ten characters, as the user counted). The comparison
result carries no photo; **requesting one would confirm it, and confirmation
would require doing something**, so he does not request it. `그래서 안 갔다.
**안 가기로 한 게 아니라 안 갔다.**` What actually snags him is not the
accident — `안 꺼내는 걸 정리라고 부르기로 한 지도 오래됐다` — but
**`살아 있었으면 삼십 년이다. (…) 한 번도 안 왔다는 얘기가 된다`**, which is
the question EP114 exists to ask.

**He says one word about the file: 「보류.」** Yun does not ask why —
`이유가 있는 걸 물으면 그 이유를 같이 져야 한다` — and **an order he never
gave stops the paperwork**, tracked as `FS-S13-HOLD-ORDER` (part of Dana's
delay originates here; **never connect the two lines on the page**). The file
goes to the left side of the desk, a spot kept empty for thirty years. The
close is the user's rewrite and it ends on a question rather than a
formulation: `저게 그 도영진의 것이라고 한다` /
**`물어보고 싶은 것은 많은데 무엇부터 물어봐야 할지는 모르겠다`** /
`모르는 동안은 아무것도 안 해도 되고, 아무것도 안 하면 아무것도 안 틀린다` /
**`질문은 아무한테도 말하지 않았다`** — the same shape as Dana unable to ask
Hyeonseo anything in EP108.

**G0-021 was approved before drafting** and defines the pair: Yeongjin
commissioned through the **science-technology officer** track and developed
**military exoskeletons** at the ADD; Myeongjun was a lieutenant a few years in,
assigned as the **test wearer** — which is why a twenty-year age gap still
produces EP012's `오래 같이 지낸 사람들의 간격`, since fitting, measuring,
adjusting and refitting repeat for years. **The accident: Myeongjun was trapped
inside, the normal release failed, Yeongjin reached in by hand, and the machine
closed** — the thing he built took his arm, thirty years before
`내가 만든 겁니다`. Only one of them paid. Discharge was a choice, not a
disqualification. **The lineage matters: what Yeongjin built his whole life is
a machine a person wears**, so the Black Titan is closer to worn than piloted,
and EP109's `처음부터 손이 저절로 스위치를 찾아갔다` sits on top of it — but
**the mechanism seal is untouched; G0-021 opens the lineage, not the how.**
Everything in it stays at **zero on the page until EP114**, and the **Bak
Useok line stays separated from Myeongjun permanently**.

**Also approved this block: G0-020** (law frozen at 2020 by the deluge, so
**there is no statute that fits** — Dana is a 촉법소년 at 12, **Sua at 9 falls
outside the Juvenile Act entirely**, and the charge is never named because
nobody can find a box to write it in; the phone moves from *waiting* to
**seized as evidence** to *forbidden*; and the southern command **is not
covering anything up** — it simply keeps announcements minimal because public
opinion favors the giant, which is exactly the leverage Myeongjun will hold in
EP115). The canon supplement now registers **G0-017 through G0-021** (the
017/018 rows had been missing).

Next: **EP111 「묵비」** (9/10 Sat, Yeongjin POV) — Bak Gihun (detective), **An
Seungu** (military police, *has something he cannot ask*), Eom Taeseok (public
defender), and **he does not talk about the children**. The paperwork Myeongjun
froze slows the investigation, **and Yeongjin does not know why**.

## EP111 approved (2026-08-22) — silence, and the sweep that caught it

**EP111 「묵비」** (`117_EP111_승인완료`, important, 5,588 chars, 9/10 Sat,
**Yeongjin POV**) is `GATE_D_PASS`. State = **SNAP-111**, tracker SNAP-111
(`as_of_episode: 111` verified, 53 active), ledger **v2.06**.

**A process change landed first and it changed the chapter.** After six
continuity errors across EP109–110 — all of which had their answers sitting in
approved prose — the user said: *"항상 관련 정본을 확인하고 서술하자 / 자꾸
찐빠나면 놓치는게 생긴다."* Reading the canon had already been the rule and the
rule had not held, so it is now a tool: **`tools/precheck.py`** sweeps all
approved chapter bodies for a keyword and returns **first appearance plus recent
prose**. `production-pipeline.md` **§8-2** makes running it mandatory before a
brief, and `chapter-brief.md` **§0** refuses a brief without the sweep results
**quoted verbatim** — summarizing is what loses things. Minimum six keyword
classes: every character present, any first-appearing or first-POV character
(`--all`), locations, the events being recalled, props, and repeated phrasing.

**The sweep immediately caught four things on this chapter.** (1) Scanning the
`pov:` field across every delta showed **Yeongjin already had scenes in EP090
and EP092**, so "first Yeongjin POV" would have been wrong — it is his first
*solo* chapter. (2) **EP012** carries `한 달 전 이 식탁에서 **압수와 체포와
분리의 순서**를 들었다`, a line whose original scene was never dramatized; it
became this chapter's closing movement. (3) **EP090** holds both the body that
knows procedure — `이런 절차가 어떻게 굴러가는지 아는 몸이었다 (…) **그래도
계속되면 언젠가 찾는다는 것도 알았다**` — and the **honorific ladder**
(`도 씨` / `박사님` / `사장님`). (4) `중령` appears **zero times** in 110
chapters while the voice card mandates *"「도 중령님」 호칭에는 반드시 언짢은
반응"*, making that address available as this chapter's peak.

**The chapter's premise: 묵비 is not silence, it is editing.** He answers
everything — name, address, movements, ownership, funding — **and never talks
about the children**. He does not stall, does not demand a lawyer, does not
invoke the right to remain silent (`거부할 게 없다`). The voice card says he
answers questions halfway; **here he answers fully, and the broken habit is the
defense**: `다 답하면 다음 질문이 안 온다 / 절반만 답하면 나머지 절반을 물으러
온다. (…) 방향이 정해지면 그 방향에 뭐가 있는지 보인다.` He lies three times
in ten days, **all three where a person's name would have surfaced** — Bak Useok
is never named even under the funding questions.

**And he reads EP110 from the other side without knowing what he is reading.**
`조사하는 사람이 뭘 물어도 되는지를 아는가. / 물어도 되는 범위는 위에서 정해서
내려온다. 안 내려오면 못 묻는다. / **열흘째인데 아직 안 내려온 거였다.**` An
Seungu asks what Bak Gihun already asked an hour earlier, stops mid-sentence at
`…내부 구조에 대해서`, and leaves with `…다음에 하겠습니다` without saying when.
The cause — Myeongjun's **「보류」** — stays at zero on the page. Yeongjin's read
on him is generous: `나쁜 사람은 그런 걸 안 묻는다. (…) 자기가 지금 뭘 하고
있는지가 마음에 안 드는 사람이다.` The warrant does carry a charge, which he
reads and dismisses — `칸을 채우려고 넣은 거였다` — satisfying G0-020's
no-named-charge rule while conveying its absurdity.

**★★★ The user's correction rewrote the final scene.** The spring table was not
a prophecy, it was a gag order: **Dana had come home bragging that she fixed the
throwing panel in Narae's comic** — EP006's `던지는 컷이 완전 엉터리인 거야. (…)
그래서 내가 고쳐 줬지. 발은 이렇게 앞뒤로—` — and Yeongjin heard it for what it
was: **`무게를 몸으로 받아 본 사람만 아는 말이었고, 그 말을 반에서 한 거였다`**.
He put his spoon down and named the three things. **`겁을 주려던 건 아니었다.
입을 다물게 하려던 거였다.`** And Sua's line, which the user also fixed, means
what he needed it to mean: **「저도 마찬가지네요」 = 말하면 안 되는 게 언니만이
아니라는 뜻** — she counted her own share instead of being frightened, and
`알아들었으면 다행이었다`. That makes the close far worse than a fulfilled
prophecy: **`입 다물게 하려고 세워 놓은 세 개였는데 세 개가 다 왔다. / 입은
다물었는데 그건 그대로 왔다.`** The gag order worked and changed nothing — and
**one thing that was not on the list came anyway**, a sentence he refuses to
finish: `만들어 놓으면 그다음부터는 그게 계속 있게 된다 / **안 만들었다**`.
(EP011's `혹시 나래가 만화에 그리면` was Dana's version of the same fear;
EP006 is now recovered 105 chapters later.)

**A third correction built a five-rung ladder.** A detective interrogating a
suspect would not say `사장님`, so Bak Gihun says **`도영진 씨`** — and the
change of address becomes the change of status: `지난달에 동네를 돌던 사람들은
사장님이라고 불렀다. (…) **씨는 이름을 아는 사람이 부르는 말이다. 종이에
이름이 올라간 다음부터 그렇게 부른다.**` The rungs now run 도 씨 → 박사님 →
사장님 → **도영진 씨** → **도 중령님**, and this chapter drops two of them.
Tracked as `FS-S13-HONORIFIC-LADDER`: **whichever one Myeongjun reaches for in
EP114 is the answer to that relationship.**

**Also of note:** the closes of EP110 and EP111 rhyme on *left* — a file placed
on a desk-left kept empty for thirty years, and **`왼쪽에는 아무것도 없었다`** —
with no connecting narration. Detention staging is now fixed (구치소, 6am lights,
7am meals, quiet Saturdays, an interview room with one high window; **no visits,
no deliveries in ten days**; 9/10 is when transfer to the prosecution should
happen and **is stalled**), closing the "미설계" row in the autumn stage
document. New characters Bak Gihun, An Seungu and Eom Taeseok exhaust reserve
name list ④.

Next: **EP112 「집안 사정」** (9/12 Mon, **Hyejeong POV**) — the school's "family
circumstances" does not line up with the August 31st siren, she asks her uncle
**`단아 어디 있어요`**, and **Myeongjun cannot answer**. EP110 had him skim past
the children's names with no reaction; **that bill comes due when his niece says
one of them out loud.**

## EP112 approved (2026-08-22) — the name said out loud, and two process fixes

**EP112 「이름을 댄다」** (`118_EP112_승인완료`, important, 5,027 chars, 9/12 Mon,
**Hyejeong POV**, her fourth close third) is `GATE_D_PASS`. State =
**SNAP-112**, tracker SNAP-112 (`as_of_episode: 112` verified, 54 active),
ledger **v2.07**.

**This chapter's first draft was written without checking canon and had to be
rebuilt.** The sweep results were pasted into §0 and then **the source chapters
were never opened**, which is worse than not sweeping — it looks done. Four
rounds of user corrections followed, and two of them changed the pipeline.

**Round one, five factual errors.** (1) The shutter: EP001 says
`**평소라면** 하나씩 안으로 들이고 덮개까지 씌웠을 사람이었다`, so it is
normally *open* and closing it on the first sortie was the exception. The draft
had it backwards. (2) With that fixed, the right first reaction to an emptied
shop is **moving house** — `이사를 가면 셔터를 내리고 간다. **문을 열어 놓고
가는 이사는 없다**` and then `**이사한 집에 줄을 치지는 않는다**`. (3) The kids
walk to school; the bus ride was invented. (4) Hyejeong's two summer visits are
on the page — EP088 (turned back after seeing the unmarked truck) and EP090
(peaches, with Yejin, the one day out of forty) — not the errand the draft made
up. (5) The EP089 call was **`군에서 어린애한테 위험한 일 시키는 경우가
있어요?`**, answered with *없다* plus the reporting number, and **she gave no
name**.

**★★★ Round two was a character violation, and it is the important one.** The
draft made Hyejeong a girl who counts. **EP088 defines her as the opposite:**
`혜정은 **세는 애가 아니었다.** (…) 그런데 **잊는 애도 아니었다.** 특히 친구
일은 안 잊었다. 안 잊은 것들이 머릿속에 **날짜 순서로 쌓여** 있었고, 오늘
아침에 그것들이 **저 혼자 줄을 섰다.** (…) 하나씩 보면 다 넘어갈 수 있는
것들이었다. (…) **한꺼번에 보니까 다른 것이 됐다.**` The cause was checking her
**latest** appearance (EP105) instead of the one that **defines** her.
Everything countable came out — the tallies, the `하나, 둘, 셋. 넷`, "weight
can't be counted" — and was replaced with accumulation: `혜정은 하나도 안
지웠다`, `날짜 순서로 다 있었다`. **The close now re-runs EP088's own
structure**: the teacher's phrase, twelve unread messages, an open shutter over
an emptied shop, the yellow tape, the unmarked white car, and the two sentences
her uncle said — `하나씩 보면 다 넘어갈 수 있었다` → **`혜정은 한꺼번에 안
보려고 했다`** → **`안 보려고 하는 것도 이번이 두 번째였다. 첫 번째는
실패했다.`**

**→ Fix #1, now in `production-pipeline.md` §8-2 and ledger §6-23:** sweep every
POV character and major supporting character with **`--all`** and find the
**defining** paragraph, not the most recent one. §6-23 tabulates them
(Hyejeong = EP088, Yeongjin = EP090 + card §6, Myeongjun = EP012 + card §7,
Sua = EP106/109, Dana = EP104/108, Yejin = card §4, Hyeonseo = autumn card §2).

**Round three recovered something the user had also forgotten.** EP105's rule
was not "one a day" — it was `답이 없으면 한 번 더 보내고, **두 번째에도 없으면
그때는 그만뒀다**`, and that night she declined to send the second one and
**`내일 보내기로 했다`**, then `그 뒤는 안 정했다`. So twelve days of daily
messages are twelve days of **deferring the quitting clause**, which the page
now says outright: **`하루에 하나는 규칙이 아니었다. 그만둔다는 걸 하루씩
미루는 거였고, 미루는 걸 매일 하고 있으면 그건 규칙처럼 보인다. 혜정도 그걸
알고 있었다. 알면서 매일 미룬다.`** The close repeats the shape — `내일 것을
보낼지 말지는 오늘 안 정하기로 했다. 그것도 열이틀째 같은 식이었다`.

**Round four: two logic fixes and a compression note.** `아는 사람은 **뒤에** 걸
말한다` (in that sentence pair the guess comes first and the certainty second —
the draft had it inverted), and the guess about *where* became a judgment about
**range of knowledge** — `큰삼촌이 아는 곳이라면 어떻게 지내는지도 안다. 모르는
곳이라면 어디인지도 모른다` — which also keeps the hospital off the page.

**→ Fix #2, also in §8-2: compress recall.** The draft explained the EP089 call
**twice at length**, once in the lunch scene and again during the call. Recalled
material gets only enough for recognition, explained once, never twice in the
same chapter — and **the space saved goes to the present scene** (looking inside
the shop for the first time, `잡힌 쪽 팔이 좀 따뜻해졌다`, `아무 일도 없는
통화를 하려고 방문을 닫은 건 아니었다`).

**What the chapter does.** She will not read the notice — `학교에서 그걸 아는
애가 자기 하나가 된다` — and the green boxes going into an unmarked white car
land on top of two older memories (the summer truck, her uncle's base). Then the
title: **`단아 어디 있어요.`** EP089's line, set by Yejin, was *이름은 대지 마*,
on the reasoning that a name handed to an adult turns a worried-about kid into
an investigated one. EP112 breaks it because **`토요일에 본 것 중에 조사가 아닌
게 하나도 없었다` → `지킬 게 없어졌다는 뜻이었다`** — and Yejin, now arguing the
other way, gets **`그때는 이름을 안 댔으니까`**. Myeongjun appears as voice only:
`글쎄다`, a long silence, a voice that **drops rather than quiets**, and
**`그건 삼촌이 말해 줄 수 있는 게 아니야`** — never *모르겠다*, which is the
tell: **`말해 줄 수 없으려면 먼저 알아야 한다`**. She swallows the follow-up
because `그러면 이 전화가 끝난다`, hangs up first, and it wins her nothing. The
name he skimmed past on a form in EP110 has now been said aloud by his niece,
with **no narration connecting the two lines**.

Next: **EP113 「세 사람」** (9/13 Tue, Myeongjun POV) — Marcus Hale, the joint-asset
demand, and **Yeongjin's self-sacrifice failing at the international line**. It
falls the day after he could not answer his niece.

## EP113 approved (2026-08-22) — the Americans, and a word that does not fit

**EP113 「세 사람」** (`119_EP113_승인완료`, important, 6,202 chars, 9/13 Tue,
**Myeongjun POV**, his second) is `GATE_D_PASS`. State = **SNAP-113**, tracker
SNAP-113 (`as_of_episode: 113` verified, 56 active), ledger **v2.08**.

**Marcus Hale is the first American on the page** — liaison officer, 40,
**field-grade** (exact rank withheld, at the user's correction), no uniform, one
bag, **and he never opens it**. His Korean works the way the L6 card fixed it:
**memorized sentences are flawless and everything spontaneous goes through the
interpreter**. He reads all three names without looking at paper. **No threat,
no deadline, no next appointment, no article numbers** — `번호를 대면 이쪽이 그
번호를 들고 법무에 간다`. Myeongjun's read: **`이 사람은 이기려고 온 게
아니었다`**, and not setting a deadline is the worst part, because
**`쥔 걸 못 쓰는 사람은 시간이 갈수록 약해진다`**.

**★★★★ The chapter's spine is that EP110's 「보류」 turns out to be one-sided.**
`필요한 서류는 이미 양쪽에 다 있습니다` — the file has sat on his desk-left for
four days, never leaving the room, and Hale recites the ages and the hospital
ward anyway. **`나흘 동안 아무것도 안 하면서 이걸 지키고 있다고 생각했다.
지키고 있었던 게 아니라 그냥 안 움직이고 있었던 거였다.`** Then the three
names, and the detail that matters: **on the Korean form one name is large at
the top and two are small underneath, and on theirs there is no such
difference** — `그 크기 차이가 지금까지 뭔가를 막고 있었는데`. He says
**`그건 아이들입니다`** and Hale **does not disagree**, which removes the place
to push from. The term arrives: **공동 자산**. Offered a softer wording,
Myeongjun refuses it — `그러면 그냥 쓰시죠` — because accepting a courtesy makes
the next demand harder.

**★★★ The user caught that this negotiation is above a field command's pay
grade, and the fix became the best material in the chapter.** Canon supplies the
constraint: **there is no real-time link to Sinseoul; a monthly liaison ship
carries administration**, and `신서울 중앙정부는 (…) 즉시 대응할 능력이 없다.
(…) **고명준과 청해시청, 에너지 연구진이 사실상 즉시 결정을 내린다**`. So
Myeongjun says **`이건 제 권한이 아닙니다 / 그런 얘기는 신서울에 하셔야
합니다`** and Hale answers **`했습니다`** — talks last month, a document early
this month, no reply yet. **He cannot verify any of it in the room.** This
month's ship sailed last week; jumping the queue on the limited long-range
circuit requires writing a justification, **and a justification becomes a
document that leaves this office** — poison for a man who froze a file precisely
to avoid that. Then the door closes: **`현장 사안은 여기서 결정되는 걸로 알고
있습니다`**. `신서울은 법과 화폐와 국가 이름을 갖고 있고, 청해는 결정을 갖고
있다. **편할 때는 그게 편했다. 지금은 아니었다.** 권한이 없다고 물러설 수가
없었다.` The combined-command body that would normally handle this **exists only
on paper** — the American seats emptied when they pulled back for domestic
disaster relief — **`그래서 사람이 직접 오는 거였다`** (no organization name on
the page; the setting bible does not define one).

**★★★★★ And the second user catch reshaped the opening: 조의 is for the dead,
and nobody died.** EP110 had already fixed `부상자 0. 사망자 0` on the page. So
instead of swapping the word out, Myeongjun challenges it: **`사망자는
없습니다`** — a figure he has been briefed on repeatedly and found strange every
time (`그런 교전이 어디 있나`) — and Hale answers **`알고 있습니다`** **and does
not correct himself**. `유감이라든지 위로라든지, 쓸 말은 있었다. 외울 정도의
사람이면 그 차이를 모를 리가 없었다. **모르고 썼으면 실수고, 알고 썼으면
실수가 아니다. 방금 알고 있다고 했다.**` Tracked as `FS-S13-CONDOLENCE`, layer
1 — **the meaning stays unassigned**: `고명준은 그게 무슨 뜻인지 정하지 않기로
했다. (…) **다만 잊어버리지는 않기로 했다.**` **The narrator must never
interpret it for him.**

**Not asking is the chapter's grammar.** He asks where the data came from
knowing no answer will come (asking is how this side registers that it did
something), and he deliberately **does not ask about the white one** —
confirming it would put their involvement in a document and make that document
the basis for the claim, denying it could not be disproved. His anger about it
does reach the page for the first time, in narration only: `언제 어떻게
만들었는지도 모를 자기들 거인을 한 번 밀어넣고는 여태껏 연락은 그게
전부였다`. The public-opinion card he holds is examined and left unplayed —
**`카드를 쓰려면 말을 해야 하고, 말을 하면 카드가 없어진다`**.

**The close finally lets him read the shape of Yeongjin's confession** —
`그때는 그냥 자백으로 읽었다. **지금 보니 자백이 아니었다**` — responsibility
piled in one place so the rest weighs less, which worked here: on the Korean
file the children sit small at the bottom, and **`정하지 못한 걸 다행이라고
생각한 적도 있었다. 칸이 없는 게 보호가 되고 있었다`**. **The purpose and the
thirty-year-old connection remain at zero.** He needs to ask, and asking means
going — **`간다는 게 무슨 뜻인지는 오늘 밤에 생각하기로 했다`**, with no
decision stated. Last beat: two giants sit in that tidal flat and **neither came
up in the meeting** — `자기들 것 얘기도 안 했다. **사람 얘기만 했다. 그리고 맨
처음에 조의를 표했다.**`

**Dana has now existed as a name only for three consecutive chapters** —
Yeongjin's silence (111), Hyejeong's question (112), a foreign officer's list
(113).

Next: **EP114 「왼팔」** (9/15 Thu) — **the first meeting**, the season's peak,
the test-range accident, and **Yeongjin already knew**. EP110–113 all converge
here: the photograph in the drawer, the interrogation nobody is allowed to
conduct, the niece's question, and the side that already knows everything.
**G0-021 partially unseals in that chapter.**

### EP113 retrofit — the incursion of the night before (2026-08-22)

The user caught a hole: **thirteen days after August 31st with no further
attack** reads as if the kaiju are waiting for the humans to sort themselves
out. The fix had to stay small — **Lucy has not appeared yet**, so the White
Sentinel could only be shown **in passing, one line, dispatching something
easily**. A sweep confirmed no alert is mentioned anywhere in EP104–113, so the
insertion went into **EP113's morning briefing** and no other approved chapter
needed touching.

**It sits on the night of 9/12, which is the night before Hale arrives.** Buoy
at 1:20 a.m., open water outside the control zone, coastal-only alert,
mid-sized. The southern command **got as far as preparing to launch and it was
over before they left** — `"흰 쪽입니다. 부표에서 종료까지 사십이 분입니다."` /
**`사십이 분이었다.`** Against 8/31, which ran from afternoon to evening and
**left something in the flats**: `이번엔 남은 것도 없었다`. No report comes from
the American side — `"저쪽에서 온 보고는." / "없습니다." / **"그렇겠지."**` —
no close description, no Lucy, no creature name.

**★★ It also supplies the physical reason for Hale's patience.** He does not set
a deadline because his side can handle these alone; the timing reads as a
demonstration whether or not it was meant as one. Myeongjun's anger updates to
match: `자기들 거인을 **두 번 내보내놓고, 두 번 다 말 한마디 없이 치우고
갔다.** 그러고 오는 건 내용 없는 연락 한 건이었다.` (The earlier "no-content
contact" is now `지난주에 한 번 온 건`, keeping EP110's Gubonsik line intact.)

Approved-file length is **~6,520 chars** of body; note that `check_draft.py` run
against an approved file counts the ~800-char header table too and will report a
band overrun — **measure the draft in `_superseded/` for the true number.**

## EP114 approved (2026-08-22) — the left arm (S13's peak)

**EP114 「왼팔」** (`120_EP114_승인완료`, 5,205 chars, 9/15 Thu, **Myeongjun POV**)
is `GATE_D_PASS` and is **the season's peak**. State = **SNAP-114**, tracker
SNAP-114 (`as_of_episode: 114` verified, 58 active), ledger **v2.09**.

**★★★★★ A canon error nearly shaped the chapter and the user caught it.** The
brief was built on EP005's line — `시제기는 30년 전 물건이다. 만들다 폐기된 걸
내가 혼자 빼돌렸다` — treated as fact. **It is Yeongjin's cover story for the
children.** Canon is the setting bible: **§202** (Hyeonseo sets out to grow a
human-side 거체; the first one forms a self and is destroyed) and **§919**
(`블랙 타이탄은 수아 쪽 거체야`). What EP005 is actually good for is its **first
half** — eighteen years ago, a daughter who has not written in years, papers
spilling out of shaking hands, and **`우리도, 우리 괴물을 만들어야 해요`**.
**→ `production-pipeline.md` §8-2 now carries 「인물의 설명은 정본이 아니다」**:
check who said it to whom, whether that speaker uses cover stories, whether the
bible covers the same item, and **if it does, the bible wins.** In this serial
**Yeongjin's explanations are cover stories by default**, with a different
version per audience.

**That correction is what gave the chapter its shape.** Yeongjin has **nothing
he can say to Myeongjun** — the prototype story collapses instantly against a
man who worked that program and can pull the disposal records, and the truth is
further out of reach. So he goes silent, and **the silence is a wall, not the
editing he did in EP111**. Which turns out to be the answer: `왜 안 알렸느냐고
물었는데, **대답이 안 오는 것 자체가 대답이었다.** **이 사람은 원래 안
말한다.**`

**The comparison Myeongjun deferred in EP110 ends in three seconds.** Ten
characters on a form, a photograph with both arms, and a folded sleeve across
the table — **`보름 동안 안 한 확인이 삼 초 만에 끝났다. 그리고 삼 초 만에
끝날 일을 보름 동안 안 하고 있었다는 것도 같이 확인됐다. 두 번째 쪽이 더 오래
남을 것 같았다.`** Yeongjin is not surprised — **`오실 줄 알았습니다`** (G0-019
§2) — so the only person startled in that room is the one who came to look.

**★★★★ The honorific ladder resolves off the ladder: 「박사님」.** `동네
사람들은 저 사람이 뭘 고칠 줄 아니까 그렇게 부른다. **고명준은 저 사람이 뭘
만들 줄 알아서 그렇게 불렀었다.**` Same word as the neighborhood's, different
origin — and **his hand does not stop**, where the MP investigator's 「도
중령님」 had stopped it (EP111's report, which Myeongjun had read and thought
pointless to record: `지금 보니까 적을 만했다`).

**★★★★★ The analysis lands here, filling the one gap in a thread that was
already seeded.** The user flagged that the machine's biological nature should
be known to the military by now and that kaiju bleeding the same fluid should
have been laid in all along — a sweep showed **the seeding exists**: EP009
(wiped clean and **dark red again**, then `소각로 앞에서, 영진은 검붉게 젖은
걸레를 오래 보았다`), EP045, EP048, EP056 for the kaiju, and **EP102 `검붉었다`
/ EP103 `검붉은 것이 굳어 가는 중이었다`** for the Titan, in identical wording.
What was missing was **the army noticing**. Sample taken from the waist hole at
recovery; **it could not go outside** — the research complex does fusion, and
sending it out would itself become an incident — so **the base medical unit**
looked at it and produced an **opinion**, not a result: not lubricant or
coolant / organic tissue, cell-like structures / **`현 장비로는 분류 불가.
참고할 만한 자료 없음`** / **`채취 시점에 죽어 있지 않았던 것으로 보임`**
(`살아 있었다고는 못 쓰겠답니다`). **The reason it cannot be classified is now
double — nothing matches, and there is nothing here to look with**, which is
also what this city is. Tracked as `FS-S13-ORGANIC`; **the kaiju comparison
stays at zero** (samples dissolve, G0-011) and **why this one did not dissolve
is asked and not answered.**

**Both questions go unanswered — and he does not lie either.** Shown the
opinion sheet, **Yeongjin does not react**: `놀라는 사람은 모르던 사람이다. 이
사람은 알고 있었다.` **The wall cracks exactly twice.** First at 공동 자산,
where he starts a sentence and cannot finish it — **`…그건`** — and second when
**he asks a question first**: **`큰애는 어디 있습니까`**, which he had not asked
in fifteen days of interrogation. Told where both girls are, **he lowers his
head slightly**, the only time. And one line of explanation arrives, thirty
years late: `몰랐습니다` (his fastest answer in the room), `우리 쪽만
봤습니다`, **`…내가 걸 수 있는 게 그것뿐이었습니다`**.

Also fixed by the user: **`반 년 걸리신 걸 하룻밤에 합니다`** — the comparison
is spring-through-summer against last night's forty-two minutes, not half a day,
which rhymes with Hale's condolence for `3월부터 지금까지`. The exoskeleton
program is confirmed **ended** (`끝났지요`), **and no lineage is drawn between
it and any "oversized prototype"** — that was part of the cover story. Sample
came from the **waist hole**; the machine has been cut open but **still cannot
be dragged off the flats** — `이도 저도 안 됐다`.

**Dana has now been a name only for four consecutive chapters** — and in this
one **her grandfather is the one who says it first.** Close: the desk-left,
empty for thirty years, **now holds two.**

A **backlog document** was also created this session —
`05_문체_상태_인계/Black_Titan_미결과제_목록_v1.0.md` — to be reviewed at each
chapter close. It carries two retrofits the user wants later: **more kaiju-fluid
seeding in past battles where something was cut or pierced** (user will supply
via the annotation tool), and **the research complex as the kaiju's apparent
target** — the misdirection that was supposed to hide why they come to Cheonghae
at all, which slipped away after EP018.

Next: **EP115 「조건」** (9/16 Fri, Myeongjun POV) — treatment, protection,
contact and jurisdiction against combat cooperation; **Myeongjun becomes the
buffer.** It closes sub-arc ②, and **what exactly Dana is suspected of** has to
be settled there.

## EP115 approved (2026-08-22) — the terms (sub-arc ② closes)

**EP115 「조건」** (`121_EP115_승인완료`, 6,337 chars, 9/16 Fri, **Myeongjun
POV, 4th and last of the run**) is `GATE_D_PASS` and closes sub-arc ②
「이름」. State = **SNAP-115**, tracker SNAP-115 (`as_of_episode: 115`
verified, 62 active), ledger **v2.10**.

**Myeongjun has nothing to sell.** The other side asked for three people; the
only thing this side can offer is combat cooperation, and the substance of that
is a fifty-metre thing kneeling in the flats that **has not switched on in
sixteen days**. So he counts what it would take to switch it on: **one who
built it, one who rides it. Two.** The other side named **three**. **One is
left over** — `셋에서 둘을 빼면 하나다. 그건 만 열두 살도 알 것이다` — and the
leftover goes nowhere, stays on their paperwork, because this unit cannot
justify holding someone it has no use for. **`남기는 손이 이 손이었다.`** That
is why Hale set no deadline (EP113): wait, and this side does the sorting
itself.

**★★★★★ And the user caught that the arithmetic's raw material comes from the
other side.** The draft had Myeongjun knowing who rode how many times. He does
not. **The only 조서 this unit holds is Yeongjin's, and Yeongjin is silent**;
the girls have produced **zero pages**. What is directly known is one boarding
— the child pulled out of the cockpit on 8/31 (EP110). That **the older one
rode, repeatedly, is Hale's statement** (EP113 `그 전에도 여러 차례 있었던
것으로 파악하고 있습니다` — `파악하고 있다고 했다. 어떻게 파악했는지는 안
말했다`), and **that line is not in this side's file**. Which makes the whole
thing worse: count only what you know and the pool is one child who cannot
walk, so there is nothing to offer; take their word and the pool is two, and
two means you get to choose. **`그러니까 저쪽 말을 믿는 쪽이 이쪽에
유리했다.`** Believing them is what serves this side, and believing them means
running their board. The self-accusation therefore gets one line longer than
「공동 자산」 alone would give: **`그 전제를 자기가 놨다. 놓으라고 준 걸
놨다.`** Three days after telling Hale `사람한테 쓰는 말은 아닌 것 같은데요`,
he is building the same table — and it keeps filling, because `안다고 멈추면
아무것도 안 정해지고, 아무것도 안 정해지면 저 아이들은 저기 그대로 있는다`.

**Two more user corrections, both load-bearing.** Conscription is still in
force, so `전부 자원했고` was wrong: `순번이 돼서 온 애들이 태반이고, 그중
대부분이 갓 스물을 넘겼다. 그래도 나이는 찼다.` — **`나이가 차야 부를 수
있다는 게 이 나라가 삼십 년 동안 지킨 마지막 선이었다. 다른 건 다 밀렸는데
그건 안 밀렸다.`** In a world whose law stopped in 2020 (G0-020), the one thing
that did not slip is **age**, and this case sits outside that line. And
**Yeongjin is held by the police, not this unit** — CORR-2026-08-21 puts
civilian custody with the police, EP114's `사령부에 돌아와서` already agrees.
Correcting it produced the chapter's coldest count: **`만든 사람은 경찰이
데리고 있고, 큰애는 시설에 있고, 작은애는 병원에 있다. 셋 중에 이 부대에 있는
사람이 하나도 없었다. 그런데 셋을 달라는 얘기는 이 방으로 왔다.`** Hale picked
this headquarters not because it holds the three but because **this is where
things get decided** (EP113). Date deixis was also wrong throughout and is
fixed in seven places: **Hale = 사흘 전, Hyejeong's call = 나흘 전, Yeongjin =
어제.**

**The summer phone call comes back.** Parked outside the hospital and **not
going in** — `그 말을 만 아홉 살한테 하는 문장으로 옮길 수가 없었다` — he
remembers his niece asking whether the army ever gives dangerous work to
children, and answering **`없다`** on the spot, reading out a report number for
good measure. She would not name the friend, and **`그때는 첫 번째 쪽으로
알아들었다`** (not really a friend / the friend said not to). It was a true
answer then and it is true now; **`다만 그 참말을 자기가 지금 깨러 가고
있었다. 그 두 개가 같이 있었다.`**

**Also new:** the engineer corps filed a **「해체 처리 가능성 검토」** — three
stages, **반출 미정**, `앞의 둘까지는 됩니다`. Cutting is reversible-proof;
Myeongjun holds it and **cannot write the reason** (`검토 중이라고 적어` / `그건
사유가 아니지` / `알면 됐어`). **Gu Bonsik starts to say what it would take to
switch the machine on and doesn't** — a different silence from Yeongjin's, same
shape in the room. And 완충 is redefined: not standing between and sharing the
load but **`양쪽 힘을 다 받고도 그 자리에서 안 비키는 것`** — which is what
Yeongjin did for thirty years, except `그 사람은 그 판이 얼마나 작은지를
몰랐다. 이쪽은 알고 있었다`.

**The scene where he must write a name, he leaves blank.** `지금까지 비어 있던
칸은 다 적을 게 없어서 비어 있었다. 이번은 칸이 있고 적을 것도 있었다. 안
적었다.` Close: the desk-left now holds **three**, `밀린 게 아니라 쌓인 거였다`
— and he fills in the 접견 신청서 사유란 that he could not fill yesterday.
**One line, contents withheld.** `지울 이유가 없어서 안 지웠다.`

**★★★ A tooling defect surfaced and was fixed.** The user noticed scene
dividers had vanished from the mobile build: the prose loader in
`tools/build_mobile_review.py` recognised only `***` as a scene break and
**discarded `---`**, which is what every approved chapter from EP107 on
actually uses (`***` count: zero). The notation changed at some point and the
tool never followed. Line 106 now accepts both — **510 dividers restored across
the whole archive**. Worth remembering as a class of error: **the tools need
re-checking against the manuscript too, not just the canon.**

Next: **EP116 「흰 것이 사람으로 온다」** (9/19 Mon, Dana POV) — **Lucy's first
appearance**, dialogue unsealed, opening sub-arc ③ 「같은 부류」. Before drafting:
refresh the character watchlist (the 「명준·영진 대면 금지」 entry was released at
EP114 and still fires as a WARN), settle where guilt-item ⑤ lands within
EP116–120, and write Lucy's voice/POV card.

## EP116 approved (2026-08-23) — the white one comes as a person

**EP116 「흰 것이 사람으로 온다」** (`122_EP116_승인완료`, 5,831 chars, 9/19 Mon,
**Dana POV, back after eleven days off-page**) is `GATE_D_PASS` and opens sub-arc
③ 「같은 부류」. State = **SNAP-116**, tracker SNAP-116 (`as_of_episode: 116`
verified, 66 active), ledger **v2.11**. **Lucy Carver appears and speaks for the
first time.**

**★★★★★ A new G0 came out of one user observation** — *"여기서 화이트
센티널이라는 이름이 처음 등장하겠군"*. A sweep confirmed **「센티널」 and
「화이트」 were at zero across EP001–115** and G0-003 covers only the black side.
And Lucy has no reason to talk around it: she is the machine's official operator
and speaks by procedure, so **「그날 바다에 있던 흰 것」 is Dana's vocabulary,
not hers.** Which makes the return question unavoidable — the Americans do not
know the other name either (Hale said only `대형체` throughout EP113) — so she
asks: **`그쪽 기체의 명칭은 무엇입니까.`** **G0-022** now records the exchange:
Lucy names hers with zero hesitation and **Dana cannot memorize it after three
tellings** (`머리에서 미끄러졌다`), while Dana names hers **with enormous
reluctance**. G0-003's `future_holder_rule` is satisfied by this scene, making
**Lucy the fourth holder**; the route onward (Lucy → US reporting → Hale →
남방사) is **not opened in S13 but is no longer sealed**, and that is the point
of the decision.

**The reluctance is physical first, and that matters.** The user asked for
"굉장히 주저하는, 진짜 말해도 되나 싶은", and the anchor turned out to be in
EP111's spring dinner table: Yeongjin put down his spoon and said **압수하고,
체포하고, 갈라놓는다고** — once, never twice. **All three have now happened**
(the machine is in the flats, he has been held nineteen days, the three of them
are in a facility, a hospital, and a police station). So keeping the silence has
lost its reason, but that is not the same as being allowed to break it:
**`소용이 없는 건 알겠는데, 그러면 말해도 되는 건지는 모르겠다`** — and **the
person she would ask is inside the third item.** But the body comes before any
of that reasoning: `턱이 안 움직였다. 소리를 내려고 하는데 목에서 안
올라왔다`, tied back to EP109's 「엄마」 with **`이건 그거하고 또 달랐다. 이건
가리키는 것도 안 됐다`**. She counts who knows — three, four if she says it —
**and then looks at the door and it is five**, because Jiyeong is sitting there.
Lucy does not write it down, does not look like she is memorizing, just says
`확인했습니다` and moves on: **`같은 자리에서 두 번 있었던 일인데 한 번만
무거웠다.`**

**★★★★★ Lucy came to the wrong person, and the mistake is not an error in her
file.** The US paperwork says 「그 전에도 여러 차례」 (EP113) — **true** — and
only that one day was different. Asked **`당신이 그날 조종했습니까`**, Dana
cannot answer: saying no leads to who did, which leads to why she didn't, which
is guilt items ①–④. **`수아 이름을 여기서 말하면 안 됐다. 왜 안 되는지는
몰랐다. 그냥 안 됐다.`** Lucy waits — briefly, shorter than she waited for the
name — and **processes the silence as a yes**. **`블랙 타이탄은 나왔는데
아니요는 안 나왔다.`** EP117–118 run on top of this misreading (the
bypass-piloting exposure still lands, since that part *was* Dana), and **EP120
turns it over.**

**★★★★★ The biggest correction was to Dana herself.** The user: *"사실 단아는
좀 더 단순한 애인데 최근 회차에서는 그런 경향이 늘었네"*. Level 6 v0.1 had
anchored her on the **translate-what-adults-say** figure — peeling `말은 해
뒀어` down to `아직 안 됐다는 뜻` — which is a **facility-era overgrowth
(EP104–109) mistaken for her baseline**. Spring/summer pages show the real one:
**`무거워지는 것은 계기가 아니라 몸이 먼저 알았다`** / **`단아는 숫자에서 눈을
떼고, 다시 몸으로 돌아왔다`** (EP022) — body first, words after, and thought
that **rolls forward** rather than doubling back. **And the voice card's table of
contents said it outright: `2. 도단아 — 몸이 먼저, 말은 그다음`.** Reading one
line would have prevented it. The failure shape: **the new character's card got
read, the 103-chapter character's did not, because you think you already know
her** — the same failure as §8-2's 「인물은 `--all`로」, with the target moved
from pages to cards. **→ `production-pipeline.md` §8-2 now carries 「말투 카드는
Level 6에서 같이 연다」**: every appearing character, and when the recent
chapters disagree with the card, **say so and restore the baseline if the cause
was situational**. The chapter now opens by putting that overgrowth on the page
as a symptom rather than a trait: `봄에는 몸이 먼저 알았다. (…) **여기서는 몸이
아무 말도 안 한다. 말해 줄 게 없으니까 그렇다.** 대신 머리가 자꾸 돌았다. (…)
**단아는 그게 싫었다.**`

**Two more page corrections from the user.** The scene belongs in the **1층
면회실**, not the common room — and EP108 puts **Jiyeong in the room** (`나도
여기 있어야 해` / `미성년자는 그렇게 돼 있어`), which is what turned four into
five, and she **never asks about the name afterward**. And a seventeen-ish
stranger is **「언니」** to a twelve-year-old, not 「여자애」; only the first three
lines keep 「애」 as the switch-over point. That produced an unplanned pairing:
**Lucy calls her `도단아` in full, Dana calls her `언니` because she cannot hold
the name — one addresses by name, the other by relation.**

Lucy's voice follows the autumn card exactly: over-precise rather than broken,
zero contractions, **English only where feeling would go** — `그쪽하고 저는
같은—` breaks off into English and Dana catches one word, **`세임`**, `뭐가
같다는 건지는 안 들렸다`. She also names a number the user approved keeping:
**`저는 여섯 살 때 시작했습니다`** — which reads as eleven years ago against a
seventeen-year-old face and is **actually two**.

Close: `내일 하면 된다` — and then Dana notices **`그게 여기 어른들이 하는
말하고 똑같다`**.

Next: **EP117 「말이 안 통한다」** (9/19 Mon, same day, Dana POV) — the
mismatched conversation, and **a second chance to say no**.

## EP117 approved (2026-08-23) — the words don't get through

**EP117 「말이 안 통한다」** (`123_EP117_승인완료`, 5,007 chars, 9/19 Mon
**afternoon — same day as EP116**, Dana POV) is `GATE_D_PASS`. State =
**SNAP-117**, tracker SNAP-117 (`as_of_episode: 117` verified, 69 active),
ledger **v2.12**.

**A premise was discarded before drafting.** The brief first had Lucy coming to
check whether Dana suffers — which presumes knowledge Lucy does not have. The
user: *"루시는 화이트 센티널이 자기 몸이니까 단아 같은 신경손상 경험은 없음.
전투 후에 저리거나 하는 건 전혀 없을 것이니 물어볼 이유도 없음 — 모르니까."*
White Sentinel shares her neural origin; it is **her own body**, so there is no
immune rejection and **no concept of nerve damage to ask about**. What she comes
for instead is **combat experience**: she has fought **twice** (8/31 and the
9/12 open-water kill, EP113); Dana has fought **십수 번** since March. The
senior party, by record, is the twelve-year-old — and Lucy is a person who
confirms her own worth by rank and by being best at something, so wanting to
learn and not wanting to concede sit in her at once. She cannot say any of that,
so she calls it **`확인 항목이 있습니다`** and arrives with nothing in her
hands — no papers, for a visit about confirming things.

**★★★★★ The mismatch is not just missing probabilities — the descriptions come
from a different body.** The user's refinement: Dana speaks in
**semi-direct-motion terms** and Lucy, who has no such thing, first takes it for
vocabulary she hasn't learned, then feels something off — *"흥미진진하게 듣다가
조금씩 이상해지는 것."* Canon supports it exactly: **`닿은 자리와 압력, 관절에
걸리는 힘은 약한 감각으로 돌아온다`** (EP002) and **`감쇠를 거쳐 오는 압박`**
(EP022). Dana's sensation is filtered one layer, so everything she says is an
approximation. Four catches, escalating: `압력이 약하게 왔거든요` → **`그 표현은
이해하지 못했습니다`**; `화면에서 봤어요` → **`화면을 왜 봅니까`**; `무겁게
느껴졌어요` → **`무거웠던 것입니까, 느껴진 것입니까`** (where **Dana stops for
the first time** — `그게 다른 건 줄 몰랐다`); and `가벼워진 것 같은 느낌이
와요`. **The first two Lucy files under her own Korean** — that is her alibi.

**★★★★★ And then the alibi runs out, because 세미다이렉트모션 is English.**
The user saw it: *"영어라 루시가 알아듣는데 「세미」가 왜 붙는지를 이해하지
못하는 느낌."* She cannot say `그 표현은 이해하지 못했습니다` about a word she
knows better than the Korean ones. To her, piloting is **Direct** — half-direct
leaves a half unaccounted for. `세미.` / `네?` / `왜 세미입니까.` / `반쯤이라는
뜻입니다.` / `그건 아는데요.` / **`왜 반쯤입니까.`** **And Dana cannot answer
either**: it is a name, her grandfather called it that, **`이름은 원래
물어보는 게 아니다`** — so **she does not know what half it is either.** Double
incomprehension: one has no concept, the other has only a name. Which makes
**`그때 아프지 않았습니까`** not a separate question but the next square —
half → the other half → something arrives lessened → therefore. **She does not
reach the conclusion; EP118 does.**

**★★★★★ The user also caught that the combat recall went in without a canon
check** — *"전투회상은 정본 대조하는걸 잊지마"* — and three things were wrong.
The limbs are **팔 여덟 개**, not legs (`물속에서, 팔이 올라왔다`). Dana did not
push; **she had done nothing but hold** for two months (`밀리면 버티고, 잡히면
버티고, 끌리면 버텼다`). And the solution was the opposite of force: **she let
go** — `개체의 힘과 단아의 힘이 같은 방향을 향하자 물속에 마찰이 사라졌다. (…)
세상에서 제일 **가벼운 것이 된 느낌**이었다`. **The correction is what produced
the fourth catch**, and with it the road into 「왜 세미입니까」. Also corrected:
the tally is kept in **Sua's table** (`수아는 여름에 표를 만들었다`), not the
grandfather's ledger — so **Lucy asks how many times and this side's record says
what came**, two different things being written from the start.

**And a layer appeared while checking canon.** Why was EP022 "the hardest"? It
resolved fine in EP023. It was hard because a ticker read **학생 1명. 이송.**,
she read it three times while the radio calling her `지나갔다 어딘가 먼 데를`,
and **that is when it took her by the waist**; the name came later (**이성호**,
EP023). **Dana does not say this.** She deflects exactly as her voice card
predicts — sentence lengthens, unnecessary detail attaches (`수심이 원래 그
정도까지는 안 가는데 그날은 갔고, 그러니까 저기 방재벽 바깥쪽이 원래 더
얕거든요?`) until Lucy cuts it with `알겠습니다`, not looking like she
understood. **In this chapter Dana withholds too** — the failure to connect runs
both ways.

**Dana's own gain: her body wakes up after nineteen days.** Nobody had asked her
about any of it — `할아버지는 어디를 맞았는지를 물었지 어땠는지를 안 물었다.
수아는 화면으로 다 봤으니까 물을 게 없었다. **물어본 사람이 없었다는 걸 지금
알았다.**` Telling it, her hand goes to the table and draws ahead of her words:
`이렇게 움직인 게 열아흐레 만이었다.` **Her exclamations come back too** —
**`아, 잠깐만요. 그게 아니고.`**, the first in six facility chapters — and the
anger arrives in the card's native form, as a counter-question: **`왜 자꾸
나한테 물어보시는데요.`** / `이겼는데요.`

Close: **`확인했습니다` appears zero times all afternoon** (it was constant in
the morning), replaced by **`확인이 안 끝났습니다`** — `안 채워진 칸이 있다는
뜻이었다`. Jiyeong checks the clock twice, **forty minutes is up, and Lucy does
not stand** — so **EP118 continues in the same seats.** Three visits would have
been strange; **one visit that does not end** is the shape. Dana had two chances
to say no today: **아침에는 말이 안 나왔고, 오후에는 물어보질 않았다** — the
second is worse, `안 나오는 건 다음에 나올 수도 있는데, 안 물어보면 나올 데가
없다`. And the strangest residue: **it had been fun**, while her grandfather is
in a police station and her sister is in a hospital.

**Three new procedures got their first run this chapter** (§8-2): open the
**spatial bible at brief stage** (LOC-06 gave the 40-minute rule that became the
EP117–118 hinge), open the **voice cards at Level 6**, and **publish to mobile
before asking for approval**. Without the first two this would again have been
caught after drafting.

Next: **EP118 「왜 안전장치 뒤에 있습니까」** — same seats, same day. It owes
three things: **the answer to 「왜 세미입니까」**, **guilt item ⑤ arriving**, and
**「같은 부류」**, whose only S13 slot is here.

## EP118 approved (2026-08-23) — why are you behind a safety catch

**EP118 「왜 안전장치 뒤에 있습니까」** (`124_EP118_승인완료`, 5,177 chars,
9/19 Mon afternoon, **continuing straight out of EP117 in the same seats**,
Dana POV) is `GATE_D_PASS`. State = **SNAP-118**, tracker SNAP-118
(`as_of_episode: 118` verified, 71 active), ledger **v2.13**. **The bypass-piloting
exposure lands and guilt item ⑤ arrives.**

**Lucy receives no new information.** She restates what she heard in EP117 —
`당신은 화면을 봅니다. / 느낌이라고 말합니다. / 반쯤이라고 부릅니다. / 그리고
아프지 않습니다.` — and Dana hears it as **`읽는 것 같았다. 종이는 없는데 읽는
것 같았다.`** / **`따로 있을 때는 그냥 말이었는데 붙여 놓으니까 뭔가가 됐다.`**
The clincher is **the half-second** (G0-004): `움직이려고 생각한 것과 실제로
움직이는 것 사이에 시간이 있습니까` / `…조금요` / `반 초 정도입니까` — and then
**`그 시간이 저에게는 없습니다.`** Dana raises her own hand to check, and `지금
뭘 확인한 건지 알고 나서 속이 이상해졌다`. Then: **`당신은 직접 연결되어 있지
않습니다. 사이에 뭔가가 있습니다.`** → **`왜 안전장치 뒤에 있습니까.`**

**★★★★★ The user's key contribution: Dana's rebuttals are all evidence.** *"단아도
실제로 맞을 때 통증이 바로 온 적이 두 번 있었고 (…) 그게 안전장치의 존재를
역으로 증명하는 느낌."* She protests — `저 아팠어요. 진짜로 아팠어요.` — and
Lucy asks **`몇 번입니까.`** July once, August once; she counts again looking for
more and there isn't. **`세지 말걸 그랬다.`** Lucy says the number *before she
does* — `두 번입니다` — and when asked how she knew: **`세는 데 시간이
걸렸습니다.`** `많으면 세는 데 시간이 안 걸린다. (…) 저쪽은 그걸 보고 있었다.`
Everything she reaches for to defend herself has already been established
canon: **EP070** (`알아야 하는 만큼만 오게 되어 있었는데` — she already knew a
governor existed, she just heard it as *safe*), **EP070/EP087** (two
breakthroughs — and breaking through means it is normally blocked), and above
all **EP071 「그렇게 되어 있었는데」**, where she asked her grandfather `그렇게
되어 있었는데 왜 아파` and **got no answer** — `호스 소리가 멈췄다. 한 박자.
다시 났다. 그게 대답의 전부였다.` Two months later: **`지금 그 대답이 오고
있었다. 물어본 사람은 여기 없다. 대답하는 사람은 오늘 처음 본 사람이다. 대답이
오는 방식은 설명이 아니었다. 두 달 동안 안 온 게 오늘 오는데, 오는 게 반갑지가
않았다.`** She reaches for her grandfather as a shield and stops — saying *he
built it, he made me ride* is **the exact sentence that put him in a police
station**, so `그 말을 여기서 한 번 더 하는 게 된다`.

**Exposure boundary held.** What appears: not directly connected / something in
between / it reduces sensation / **안전장치** / the half-second. What does not:
**근전도, filter, 심리적 신체상, 계통 적합성, and the words 「우회」·「위장」
themselves.** Lucy does not know the mechanism either — she reads the result and
names its purpose. **「당신은 같은 것으로 만들어졌는데」** appears once,
unfinished, and `뭐랑 같은 건데요` gets **no answer** (S15). And **the
misidentification is not cleared**: one sentence would end it, but saying it
means naming who did ride, so **Dana fails to say it for the third time today**.

**Three user edits changed the chapter's spine.** 「조종자가 아닙니다」 became
**`고통을 감수하지 않는 사람은 싸울 수 없습니다`** — piloting is a technical
word and made the verdict sound like a licence question; **fighting** is the
only scale this character measures anyone by, and `아파야 싸워요?` sits far
better in a twelve-year-old's mouth. 「거기서는 말이 안 됐다」 became **`거기서
동생은 말로 만들어지지 못한 소리를 냈다`**, which takes EP102's `통신에서
소리가 났다. 말이 아니었다` head-on (Dana took a direct hit to the chest and did
*not* make that sound — `같은 기계였다`; and then `굴러가려는 걸 몸이 먼저
막았다`, leaving the rest for EP120). And **`그랬다면 이렇게 되지 않았다`** was
added after the four familiar regrets — which is what makes the fifth land,
because **the fifth gets no closing sentence at all.**

**★★★★★ Guilt item ⑤ arrives with causation removed** (EP103's own figure):
`작은 게 올라왔다. **불렀다. 봤다. 왔다. 말했다.**` / `놓아도 순서가 안
바뀌었다. 앞뒤를 바꿔 보려고 해도 안 바뀌었다.` / **`안 불렀으면.`** / **`거기까지만
나오고 뒷말이 안 나왔다. 뒷말을 안 만들어도 알겠어서 안 만들었다.`** The words
「내 탓」 never appear. The first four are things she *didn't* do; the fifth is
something she *did*.

**The hand tracks the arc across three chapters:** cold (EP116) → moving ahead
of her words (EP117) → **not moving at all** (EP118), `손이 다시 손이 됐다`. The
exclamations that came back in EP117 go away again with it.

Two Level 6 rules were relaxed by the edits — **「동생」 is now allowed** (the
sentence does not stand without a referent) and the 「내 탓」 ban **permits
conditionals**. Also worth noting: the card-forbidden **`셈이었다`** slipped into
the draft and **the forbidden-term grep caught it**, which is what putting the
card's three prohibitions into L6 was for.

Next: **EP119 「오늘은 세 번」** (9/20 Tue, **Sua POV**) — rehab begins with Kwon
Doyun, and it is **the first transfer, not the first step** (discharge in S16 is
in a wheelchair). **The day after her sister breaks, the younger one gets out of
the room** — laid side by side one day apart, not cross-cut.

## EP119 approved (2026-08-23) — three times today

**EP119 「오늘은 세 번」** (`125_EP119_승인완료`, 5,146 chars, 9/20 Tue, **Sua
POV, first since EP106 — seventeen days**) is `GATE_D_PASS`. State =
**SNAP-119**, tracker SNAP-119 (`as_of_episode: 119` verified, 73 active),
ledger **v2.14**. **Rehab begins, and it is the first transfer, not the first
step.**

**The user asked for the rehab room to be pinned down before drafting** — *"재활실
미리 정해놓자 공간"* — and **LOC-07B** was written into the LOC-07 blockout
notes: below the ward (glass door → corridor → elevator), matted and unmatted
floor, four fixed fixtures, adults and elderly only, **and it is not quiet**
(`병실이 조용했다는 걸 수아는 여기 와서 알았다`). One fixture made the chapter:
**a full-length mirror.** The ward's single room has none — so **Sua sees
herself for the first time in seventeen days**, and `없다는 걸 오늘까지 몰랐다.
없는 걸 찾은 적이 없어서 없는 줄도 몰랐던 거였다.` What she sees: `기억보다 말라
보였다`, `오랜만에 보니 이렇게 작은 줄은 몰랐다` — **`저 큰 것 안에 있을 때는 커
보였다`** — and when she tries her toes, **`안 움직이는 걸 마주 보는 건
처음이었다`** (under a blanket you cannot watch it fail). The **parallel bars**
do the other job: visible, asked about once, `나중에요` — which keeps **「첫
걸음」 at zero while showing why.** The `걷` grep returns 0 for the whole
chapter.

**The chapter's engine is that Sua counts.** EP106 established it — `세로로
여섯 개, 가로로 넷` and **`세고 나니까 그게 어디 있는 얼룩인지 말할 수 있게
됐다`** — so counting is how this child gives a thing a name. Today she counts
something she did instead of something someone else installed: `세 번 중에 한
번.` `천장은 세도 스물넷이고 다음 날도 스물넷이었다. 세도 안 늘었다. **이건 늘
수 있는 숫자였다.**` **And that sets up the exact mirror of yesterday**: Dana
was asked **`몇 번입니까`**, counted to two, and thought **`세지 말걸
그랬다`**; Sua counts to three and can finally say what it is. **The same act
is evidence of guilt on one side and a first gain on the other** — laid one day
apart, never cross-cut, and **Sua does not know what happened yesterday.**

Also landing here: **`다리로 하는 게 아니었다`.** Listening to the transfer
sequence — arms, trunk, hands — she notices **legs are never mentioned**, and
`넓어진 게 좋은 건지는 아직 몰랐다`. **Kwon Doyun** (33, first appearance) works
exactly to his card: **`수아 씨`** where everyone else says 수아야 (`씨는
어른한테 붙이는 거였다`), goals as numbers, **no praise** — **one clap** and
`오늘 세 번 했습니다` (`여러 번 치면 잘했다는 뜻이 되는데 한 번만 치니까 다른 뜻
같았다`), and **he does not catch her** when she is not actually going to fall.
Jo Mingyeong gives the chapter's other keeper: **`안 나오는 거하고 없는 거는
달라. 우리가 볼 줄 아는 것만 나와.`** — `못 보는 걸 못 본다고 말해 주는 어른은
많지 않았다.` Close: seventeen days with nothing of her own decided, and today
**one thing** — tomorrow, twice. `안 되면 그건 그때 세면 됐다.`

**★★★★★ Two voice failures were caught by the user, and both are worth
remembering.** First: *"「뭘요」「어떻게 달라요」「그게 뭔데요」 이런 말투들이
수아보다는 단아 같은데"* — **correct, and I had opened both cards and still
blended them.** Dana's card is **반문형 불평**; Sua's is **한 박자 침묵 후
완성된 문장** and **「왜」를 속으로 묻고 답이 나오면 그때 입을 연다**. **Sua does
not fire questions back.** Every such line was rewritten to one of three moves —
**wait** (`안 물어도 알려 줄 것 같아서 기다렸다`), **state** (`검사에서는 아직
없죠.` / `저쪽은 매트가 깔려 있네요.`), or **confirm** (`내일도 세 번이에요?`) —
and the card's one sanctioned leak, **「부러움은 질문의 형태로 샌다」**, was kept
for a single spot: the parallel bars, where **`묻고 나서 수아는 자기가 물은 걸
알았다`**. Second, spotted via the edit 「그 말이 마음에 들었다」: **`받아 놨다`
appeared four times** — that is **Myeongjun's narration figure** (EP110/113/114)
carried in by the momentum of four straight chapters in his and Dana's heads,
and **two of the four were duplicate reactions to the same line.** Sua does not
receive-and-set-aside; **she puts a thing down and looks at it again**
(`대답하고 나서 수아는 아까 그 말을 한 번 더 놓아 봤다`). **Lesson for the
procedure: opening the cards is not the same as reading each character's card
separately.** Also fixed: **`어떤 할아버지`** (in a chapter with no Yeongjin, a
bare 「할아버지」 in narration reads as him — three spots disambiguated), 「한
번째」→**「첫 번째」**, and the closing violin figure made concrete as **여름에
했던 합주곡의 넷째 줄**.

Next: **EP120 「그럼 수아가 아팠던 건」** — **the S13 finale, 17/17**, Dana POV.
**The misidentification turns over**, the whole summer gets re-read, and
**the grandfather knew.**

## EP120 approved (2026-08-23) — **S13 complete, 17/17**

**EP120 「그럼 수아가 아팠던 건」** (`126_EP120_승인완료`, 5,126 chars, 9/21 Wed,
Dana POV) is `GATE_D_PASS` and **closes S13**. State = **SNAP-120**, tracker
SNAP-120 (`as_of_episode: 120` verified, 75 active), ledger **v2.15**.

**The chapter introduces no new information.** One thing Lucy said yesterday
re-reads the entire summer. Dana spends a day alone with it — dialogue is 0.5%,
the only spoken line is a remembered **`"저는 없습니다."`** — and every
recollection arrives already-read, then turns over: `잘하더라`(EP081) becomes
**a wrong thing to have said**; `그거 처음부터 했으면 더 많이 잡았을
텐데`(EP092), which only hurt at the time, becomes proof that **`밖에서 보는
쪽이 안에 있는 쪽보다 먼저 알았다`**; the seat rail and harness being the only
things ever adjusted becomes **the machine was never touched**; and the hand
that stopped on the console — **twice**, in EP002 and EP081 — becomes the signal
of someone who cannot answer. Dana was standing right there in EP002 and
**`딴 데를 보고 있었다. 들리기는 다 들렸다.`**

**★★★★★ The heart is a line she draws without causation.** What she saw the
night of 8/31 (a puncture through the waist, dark red setting) and what she was
told fourteen days later (the legs don't move) get set side by side with nothing
joining them: `기계가 뚫렸는데 사람이 안 움직인다` → **`오십 미터짜리한테 온 게
아홉 살한테 그대로 온다는 뜻이었다.`** And the title's sentence never finishes
— **`그럼 그때의 소리는, 동생이 아팠던 건.`** — because `만들면 그게 되어
버려서`. She also notices the tense is wrong: **`아팠던 건 그날이고, 지금 것은
아직 안 끝났다.`**

**★★★★★★ And her conclusion is wrong — deliberately.** The user set the canon:
*"여기서 단아는 오해해도 괜찮지만 실제로는 안전장치는 둘 다에게 적용되는 것 /
다만 수아가 예상치 못하게 빠르게 동조해 버렸다는 것 / 그리고 통증이나 수아와
같은 신체적 손상을 막으려 한 거지 단아의 신경손상은 예상하지 못했다는 것."* So
Dana reasons correctly from her observations (the calibration story *was* a
pretext — `어리다고 막을 거였으면 어리다고 하면 됐다. 먼저 나온 말이 제일 큰
말이다`) to a conclusion that is false: **that he knew the two of them were
different from March.** EP081's `진짜 이유는 하나였다. 위험하다는 것` is already
on the page for readers who kept it. **No narratorial correction appears** —
that is S15 6-7's work — and instead the misreading is framed by the chapter's
real subject: **`물어볼 데가 없으면 혼자 답을 만들게 된다. (…) 혼자 만든 답이
맞는지는 아무도 안 알려 준다.`** Anger is blocked twice (the man is in custody
**because of her own voice**, EP118; and there is no one left to ask), so what
accumulates is **four questions in one day** instead. Guilt becomes five: **`내가
안 나가서 더 아프게 될 쪽이 나갔다`**, and `몰라서 그랬다`는 게 변명이 안 되는
이유가 붙는다 — **`아는 사람이 하나 있었고, 그 사람도 안 말했다.`**

**Three user interventions fixed real errors.** First, **the delay is between
Dana and the Titan, not in her body** — I had written her timing her own hand,
contradicting EP118's `지금 이 손은 바로 올라간다`; scene 2 was rewritten so that
**`늦는 건 저 안에서만이었다`**. Second, *"여기는 회상이 많이 나오니까 관련
정본을 긁어봐야 함"* — and the sweep found **three inventions**: the chain
technique had been attributed to the grandfather when EP091 says the exact
opposite (**`이건 배운 적이 없었다. 하려고 생각한 적도 없었다. 몸이 먼저 그렇게
했고`**), the EP092 conversation had been paraphrased when the original is far
better, and Sua's table had been misdated (it is from spring, EP085). The chain
correction is what gave the chapter its sharpest line: **`둘 다 안 배웠는데
하나만 끝까지 갔다.`** Third, *"너무 설명이 길어서 줄일 수 있는 건 좀 줄여도
좋겠다. 회상에서 그대로 인용하는 부분들"* — **§8-2's own 「회상은 압축한다」 rule
had been written and then ignored**; about 450 characters came out across six
recollections and six narration blocks, and the recollections stopped being
quotations and became **things that snag**. Two date errors were also caught: the
footage is **8/31** (8/18 is when Dana herself swung the chain) and the count is
**스무하루**, not 스물이레.

**「수아」 appears exactly once in the body — the last line.** Everywhere else she
is 「동생」, which the user's edit (`동생이 아팠던 건`) preserved; the title says
수아 and the prose does not, because the title is for the reader and the prose is
inside Dana's head. EP118 closed with `그날 이후로 그 이름을 소리 내어 불러 본
적이 없었다`, and that holds all the way through until: `오늘은 부르고 싶었다. /
**수아야.** / 입 밖으로는 안 나왔다. / 여기서는 아무도 안 듣는다.`

---

## S13 complete — 17 chapters (EP104–120)

Autumn's first season is done: **흩어진 뒤**(104–109) → **이름**(110–115) →
**같은 부류**(116–120). Sixty-odd days of story time compressed into three weeks
of it, with **no combat on the page after 8/31** — the season runs entirely on
rooms: a facility, a headquarters office, a visiting room, a ward, a rehab hall.

**Procedures added this season** (all now in `production-pipeline.md` §8-2):
정본 스윕 tooling (`precheck.py`), **인물은 `--all`로**, **인물의 설명은 정본이
아니다**, 회상 압축, **공간 바이블은 브리프에서**, **말투 카드는 Level 6에서**,
**승인 요청 전 모바일 발행**. Two tool defects were found and fixed: the mobile
builder was **discarding `---` scene dividers** (510 restored) and the character
watchlist carried stale prohibitions. **New canon:** G0-020 (법제 정체·소년법),
G0-021 (영진·명준 외골격), **G0-022 (명명 교환)**, LOC-07B (재활실), plus the
backlog document.

**Recurring failure worth remembering:** three separate times a character's
voice was contaminated by the momentum of preceding chapters — 단아's card
mistaken for her facility-era overgrowth, 명준's `받아 놨다` bleeding into a Sua
chapter, 단아's 반문형 bleeding into Sua's dialogue. Opening the cards is not the
same as **reading each character's card separately**.

Next: **S14 「루시의 계절」** (6-4~6-6, EP121–140, 20 chapters) — **Lucy's POV
opens.** Before drafting: **S14 화별개요** and a **루시 시점 서술 카드** are both
unwritten, and the two retrofits (괴수 체액 밑밥, 연구단지 오해 장치) plus the
역장 unseal timing are still open.

---

## S14 opens — EP121 approved (2026-08-24), Lucy's POV begins

**S14 「루시의 계절」 outline is `LEVEL4_PASS`** (EP121–140, 20 chapters,
9/22–10/16), and every prerequisite it listed is now closed: the **루시 시점
서술 카드** (`narration-lucy-pov.md` v1.1), the **안전가옥 LOC 시트**
(LOC-08), the **역장 unseal** (G0-023), the **괴수 체액 retrofit** (20 edits
across 16 chapters), and a **Lucy pass in `check_voice.py`**.

**The narration card is the load-bearing piece, and its first rule is the
whole thing: her dialogue is stiff and her narration is fluent.** The
textbook Korean is her *language*, not her *mind* — she learned it for the
mission, and she thinks in her own. Readers met a rigid person in EP116–118;
the moment her POV opens, that impression inverts with no announcement.
Everything else follows from it: she measures before she describes, she
processes in order, she **closes finished items**, and **emotion is recorded
as degraded performance** (`항목이 안 닫힌다`, never 미안했다). Her force
field runs through the machine, so in combat narration **the Sentinel is
never the subject** — it is her body. And what other POVs observed about her
(the cap brim, the short nails, the big hands) is **their** material: her own
appearance never appears, and mirror scenes are banned outright.

**G0-023 reshaped the season, not just the seal.** The unseal moved from
EP137 to **EP124, in Lucy's POV** — two force fields colliding shows nothing,
and EP137 is Dana's chapter anyway. What came with it matters more: the
canonical armament (shoulder guns and forearm CIWS = **suppression only**;
the wire-guided **XLG-5 alone does real damage**) turns the season's
accusations into physics. EP126 destroys a residential block **with the
weapon that cannot hurt kaiju**; EP135's bombardment is not an attempt to
kill but to **herd** the target into wire range; EP137's blockade breaks the
herd, which is why the kaiju escapes and why Lucy's `왜 막았습니까` is
**correct rather than merely angry**. It also retro-explains spring: the
standing guard **`손을 떠난 것은 이쪽 것이 아니다`** is the same law — Dana
holds with a hand, Lucy holds with a wire. The cultivated-metal warhead stays
sealed; **Lucy is a user, not a builder**, and the blank is Hyunseo's to fill
in S15.

**EP121 「조용한 것이 이상하다」** ran the card clean: zero simile, zero named
emotion, zero honorific narration, **zero Myeongjun-style adjudication** —
the anti-example set in Level 6 held. The chapter's spine is an item that
will not close: the report was filed three days ago, all twelve fields
answered, and it still does not move to closed. She logs the cause as noise.
Two things are missing from the form — **12초**, the time Dana took to say
「블랙 타이탄」, and **what Dana did afterwards**. She reads the emptied house
with a ruler (four rectangles on the wallpaper, nine pencil marks 41cm apart,
a mirror **taken down rather than fallen**) and gets the numbers without the
meaning; the reader gets the reverse.

**Two canon corrections during drafting.** The US document says **`미확인
대형체`**, not 블랙 타이탄 — which became an asset, since Lucy knows the name
and the form does not. And **clock units are Arabic** (`10시`·`15분`·`5초`)
while **counts and distances stay in Hangul** (`열두 걸음`·`쉰두 미터`); the
draft had spelled out the times.

**Tool work this session.** The mobile builder gained a **기획 lane** — it was
only scanning `10_회차/`, so outlines never appeared no matter how often the
artifact was republished; it now collects 화별개요·Level 3 골격 from every
`\d\d_*기획/` folder, newest season first. The **clear-all button was dead**:
artifacts run in a sandboxed iframe where `confirm()` is blocked and returns
false, so `if(!confirm(...)) return;` killed it — replaced with a two-step
in-page confirm. `check_voice.py` gained Lucy dialogue and Lucy-POV narration
scans, and fixing the resulting regression exposed **three pre-existing false
positives**: Dana's 존댓말 to adults flagged as violations, `저 사람` assumed
to mean Yeongjin, and — the sharpest one — **a vocative test that ignored
particles**, so `할아버지는요.` (asking Hyunseo *about* him) read as speaking
*to* him. All 120 approved chapters now run WARN-free.

**One canon lesson worth keeping:** the rolling blackouts in
`CITY_GEOGRAPHY_NOTES` are **spring-only** — a recovery measure after the heat
exchanger tower (EP16: `복구 기간 순환정전 시행`), long over by September. A
geography note written without a time stamp reads as a standing institution;
that one is now stamped, and `check_continuity.py` warns on 정전.

Next: **EP122 「구래동」** (9/24 토, Lucy) — the market, `이것은 얼마입니까`,
미란, and a bargaining ritual she has no concept for. Still open: the
**연구단지 오해 장치** retrofit, and S15–S17 outlines.

**EP122 「계산이 안 맞았다」** put the same-neighbourhood device to work. Miran
returns — her first page since 8/30 — and drops one line at the tail of a
complaint about water pressure: **`박사님네가 닫아서 요새 다들 그냥 참고 살아`**.
The word 수리점 never appears; only the canonical **`박사님`** (EP012 onward),
so Lucy files it as one record about a person whose title she cannot classify,
and the reader gets everything. She also declines to ask, because **not
enlarging the pending list is procedure**.

Two corrections were worth their weight. A user comment caught that Korean coin
sizes *do* follow denomination order, and fixing the error produced
**`규칙에 맞는 것을 여기 와서 처음 봤다`** — which sets the chapter's axis in its
first scene, since everything afterwards (three prices for one item, words with
no meaning, laughter with no locatable cause) has no rule. And **「목이 좋은
자리」 was a card violation**: that is a market trader's concept, lifted straight
from EP007 without asking whether it belongs to *this* narrator. When borrowing
from canon, check whose vocabulary it is — sharing a location does not mean
sharing the words for it.

Drafting note: both Lucy chapters came in short and needed three expansion
passes each, and EP122's second pass pushed `past_run` to 11 against a band of
8 — broken by inserting present-tense standing-fact sentences, which suits this
narrator anyway. The closing shape is now a series: EP121 ends on an item that
will not close, EP122 on one that cannot be removed from a list it was never
on.

**EP123 「보내는 사람」** brought the POV back to Dana after two Lucy chapters,
and the Level 6 anti-example table — actual sentences from EP121/122 set beside
what Dana would write instead — held: **zero itemising, zero numbers-first,
zero adjudication.** Three earlier voice contaminations in this project came
from exactly this kind of momentum; this one did not happen.

The chapter's spine came from canon, not the outline. **The outline's 「혜정
문자」 is impossible** — EP104 established Dana left her phone at home on 8/31
and the house is sealed. But she *knows* the family numbers (home, grandfather,
Sua), so the shape became **three numbers she can dial and nobody to answer
any of them**, with friends' numbers the ones she never memorised. The letter
stops at 보내는 사람 because **the return address would say everything at once**
— and since she cannot write it, she cannot ask for it either. Meanwhile
Hyejeong had already gone to the shop (EP112) and called the command twice
(EP115), and Miran had said `박사님네가 닫아서` (EP122). **None of it reaches
her, and the page never points at that.**

**A roster omission surfaced, flagged by the user.** 정다은 had appeared in
seven chapters (25 hits) and was **absent from the SNAP character table**; the
brief had called her nearly-new because the sweep used her full name. Her real
signature is not silence but **not asking** — `묻지는 않았다. 한 번도` (EP107)
— and she fills that space with her own day instead. `precheck.py` now warns
when a three-syllable name returns ≤3 hits and the two-syllable form returns
more (정다은 1 → 다은 25; 오미란 3 → 미란 42).

**Drafting note worth acting on:** three consecutive drafts landed at 55–60% of
target and needed two or three expansion passes each, and two of those passes
pushed `past_run` over its band. Write long from the start.

**EP124 「여덟이 왔다」 opened the armament on the page**, and the whole point
was that the reveal arrives as a *state*, not an event: four weapon systems
enter canon with **zero spec description** and **not one sentence taking
「센티널」 as its subject**. The wire principle gets a single line —
`소리가 나는 동안은 아직 이쪽 것이다` — which retro-explains spring, since the
standing guard **`손을 떠난 것은 이쪽 것이 아니다`** is the same law with a
hand instead of a wire. The page never draws the comparison.

Four user corrections reshaped the chapter, and each one improved it.
**The Sentinel is sealed out of underwater combat too**, so the battlefield had
to be shallow — which plants the autumn torpedo development without a word of
foreshadowing. **The kaiju line is built for closing distance against the
Titan**, so 6-4's 「never lost」 becomes physics rather than character, and Lucy
misreads it as her own performance. **Open sea means no civilians**, so the
「예상 4 · 실제 4」 moved to EP126 — the same form filled the same way with a
different number will land harder there. And **the 20밀리 cannot damage kaiju
at all**: removing the leg-severing produced a better fight, where the creature
loses by its own design — every limb it extends is a limb not holding it up,
and nothing the Sentinel fires actually kills until the XLG-5.

**The fifth note fixed a card, not a chapter.** 「뭔가 묘사가 두루뭉술한 느낌이
있어」 — I had over-applied my own "no spec description" rule and flattened the
*actions* along with the specifications. **Lucy is a soldier: she does not
recall calibres, but her hands know the procedure.** `포탑이 돌았다` became
`포탑을 돌리고 포신을 내려 각을 맞추었다`; `등이 열렸다` became `등 뒤의
발사관에 사격제원을 입력했다`. Recorded as **§3-1B** in the narration card with
a corrected test: the question 「why is she recalling this now」 **always has an
answer for an action** — she is doing it. Only specs and history lack one.

**Canon added this session:** G0-023 v1.2 (armament, wire, force field, the
underwater seal, the matchup, and **8-inch guns overriding the settings book** —
a 55m machine holding a 5-inch gun scales to a person with a 4mm airgun),
**WS-01** (the Sentinel's first mech sheet, including which weapons are exposed
versus stowed, so 「어깨를 열었다」 is now a known error), and **KJ-03**
(synthesis No.4, mantis shrimp + octopus — the line runs 1호 농게+바다뱀,
2호 앵무조개+청자고둥, 3호 undescribed, and each one is a *different* design
rather than an iteration).

**Three chapters running, the outline has collided with canon** — Hyejeong's
text (EP123), the first solo sortie (EP124), the civilian count. The outline was
written without sweeping the approved text; the brief-stage sweep catches it
every time. That is the procedure working, not failing.

---

## EP122–125 approved (2026-08-24) — S14 5/20, and the expansion pass became a tool

**EP125 「정한 것」** (`131_EP125_승인완료`, 4,981 chars, 9/30 Fri, **Sua POV**,
no combat) is `GATE_D_PASS`. State = **SNAP-125**, tracker SNAP-125
(`as_of_episode: 125` verified, 88 active), ledger **v2.20**.

**The real output of this chapter is not the chapter.** After five straight
drafts landing at 55–68% of target, every one of them needed two or three
expansion passes, and the user called it: 「뭔가 확장패스 사용감이 나빠졌는데 /
비슷한 묘사가 중언부언되는 느낌」. The diagnosis held up under measurement —
`그건 ~것이다` ×17, judgement-deferral ×6, `~라는 뜻이다` ×5 in one draft.
**The expansion pass had been imitating the draft's own rhythm and cloning its
sentence frames instead of adding facts.**

Worse, `check_continuity.py` [4] caught **four verbatim collisions of 18+
characters with approved chapters** (EP109 ×2, EP119, EP106). EP109 is the
moment of learning and EP125 is twenty-two days of nothing changing; **if the
angle differs the sentence must differ.** All four rewritten. The one survivor
is Do-yun's signature 「손뼉을 한 번 쳤다」, which is *supposed* to recur.

**So it was turned into a metric.** Measured across all 124 approved chapters,
`check_draft.py` now reports two per-mille rates over narration only, banded at
the corpus p97:

| metric | what | median | p90 | **band** |
| --- | --- | --- | --- | --- |
| `deictic` | demonstrative sentence openers (`그건`·`그게`·…) | 11.6 | 24.2 | **29.4** |
| `closer` | judgement closers (`것이다`·`뜻이다`·`모른다`·…) | 26.1 | 51.5 | **67.5** |

**The first metric attempted was wrong and worth recording.** Ranking the most
frequent sentence-opening word finds the *character subject* every time
(`단아는`, up to 22 in an approved chapter) — that is normal prose, not
pathology. The illness lives only in demonstratives and judgement closers.
Regression: EP121/123/124 all sit inside both bands; only the EP125 draft
(30.9 / 72.2) broke them. **The metric agrees with the reader.**

The band is a ceiling, not a target: Sua's canonical three-step is 관찰 → 판단
보류 → 그만두기, so driving judgement closers toward zero destroys her. The
closing couplet was left alone. Guard registered as **production-pipeline §8-2**
with three checklist items in §12. The root fix is upstream — **write to target
in the first draft**; the expansion pass is a recovery tool, not a stage.

**Two corrections found during finalization.** The draft counted 9/8→9/30 as
「스무하루」 three times; it is **22 days**, and Sua is the character who must
not get arithmetic wrong — she does subtraction out loud in the same chapter.
And SNAP-124's `sua` block was still **spring state** (집, 6/21, 건강) — never
updated after 8/31. Rebuilt in SNAP-125 with a new **`does_not_know`** field,
since knowledge asymmetry is this arc's axis and the snapshot had no slot for
it: Sua knows nothing of Dana's facility, of Jeong Da-eun, of Lucy, or of why
her mother has not come.

**The user's five inline edits included one that was canon-correct in a way I
had missed.** My paragraph 「왜 여기로 오는지는 안 물었다 / 물으면 답이 올
것이다」 was itself a clone of EP119's 「왜 서 있는지도 안 물었다. 물으면
대답을 할 텐데」. The replacement — 「병실 앞을 지키는 아저씨들이 소아과 병동에
있다면 분명 이상할 것이다」 — removes the clone *and* uses established canon:
EP109 already has 「밖에 있는 아저씨」, the same word. It also registers
accumulated cognition: in EP119 Sua did not know whether they were guarding, and
by EP125 they are simply 「지키는 아저씨들」. Twenty-two days shown in one noun.

**Canon added:** hospital floor structure (rehab below the ward, **not the first
floor**, paediatrics above, Sua in a **single room**) — needs folding into
LOC-07B. **Foreshadow seeded ×5**, of which **FS-S14-SITTING-ONLY** is the
heavy one: the rehabilitation goal is a wheelchair, not walking (S16 discharge),
and **the character is not told**. On-page allowance stops at curriculum
observation; the sentence 「걷지 못한다」 stays at zero.

Next: **EP126 주택가** — civilian casualties **예상 4 · 실제 4**, moved here from
EP124. **The same form filled the same way with a different number.** EP128
closes 6-4, and Gaon's 「한 단어를 고쳐 옮긴다」 has now gone four chapters unused.

---

## EP126 approved (2026-08-24) — the first recovered corpse, and a beat-count that was wrong

**EP126 「값이 맞았다」** (`132_EP126_승인완료`, 6,339 chars, 10/2 Sun, **Lucy POV**,
one land engagement) is `GATE_D_PASS`. State = **SNAP-126**, tracker SNAP-126
(`as_of_episode: 126` verified, 92 active), ledger **v2.21**.

**The chapter broke a five-month-old canon line, and the user's own question found it.**
Asked 「죽은 적은 물에 닿으면 녹음 / 여기서는 수거 가능한가?」, G0-011 turned out to
specify the condition exactly: the corpse dissolves **from wherever it touches water**.
EP126 is the first land engagement in the series. **There is no water.** My draft had
it dissolving anyway — a straight canon violation — and the rewrite produces the first
recovered specimen since EP005. 「수거물 없음」 runs through EP012, 016, 024, 035, 040,
and EP024 even notes that the townspeople were getting used to hearing it. **Lucy does
not know any of that.** She has been here ten days; on the page she experiences it only
as a form field whose default she overwrites, which opens three more fields underneath —
수량, 상태, 인계처. The reader counts it; she doesn't. Whether this opens an analysis
thread is left as a separate decision.

**The beat sheet had its first real test and the coefficient was wrong.** Level 6 said
「돌게 되면 그것은 비트 표가 틀렸다는 뜻이다」, and the first draft landed at 4,802 —
80% of target — despite 60 beats being staged. The per-scene measurement is unambiguous:

| scene | kind | chars/beat |
| --- | --- | --- |
| 1, 5 | deskwork, judgement | **102, 88** |
| 2 | combat opening | 90 |
| **3, 4** | **combat action** | **67, 58** |

**A combat beat is one motion and finishes in one paragraph** — `첫 발이 나갔다` is
twenty characters. A beat like 「신고 셋을 읽는다」 carries several paragraphs. So the
rule now splits: **100 chars/beat for everything except combat action, 65 for that** —
roughly 1.5× the beats for a fight scene. **The process didn't fail; the constant did.
And it was visible in the first draft** instead of after two or three expansion passes,
which is the whole point of staging beats at all.

**Verbatim overlap with EP124 came out at zero.** L6 §3-1 had named self-cloning as the
chapter's largest risk — same POV, same sortie-fight-report shape — and split what must
match (the form's structure, the way her hands move) from what must differ (every
sentence). Only one line was allowed back: 「값이 맞으면 확인할 것이 없다」.

**Close third person overcorrected before it settled.** EP121–124 had run at 0.0%
POV-subject density; this draft first came out at **18.3%**, double the 8–10% target.
Cut back to 8.3%.

**Canon settled this chapter:** the **방재벽** is the accounting line (outside the wall is
the 소개지구 and not counted; inside is), the cockpit view is live and cannot be paused
or rewound, the Sentinel stows aboard ship (fourteen-step stowage, fifteen with damage),
and **units now run in two sets** — metric for operations, imperial for daily life. That
last one is the user's, and it costs no retro work: EP124 already had Lucy in metres
(미터 103 occurrences across the corpus; 야드, zero), and US ground operations are metric
anyway. The friction is saved for the market, which sells by 근 — 600g against a pound's
454g, with the form demanding kilograms. **Three scales that do not line up.** EP122 is
not a retro target: Lucy took 근 at face value and only compared the two prices.

Next: **EP127 못 알아듣는 말** (10/3 Mon, Lucy) — 「검은 건 지켰는데」, and the first time
she is hurt by something that is not a weapon. **EP126 laid every bit of the groundwork:**
zero casualties, four houses, all four brought down by the Sentinel, and **the creature
did not break one** — a contrast the chapter deliberately never states, so it arrives
first in a civilian's mouth.

---

## EP127 approved (2026-08-24) — the beat coefficient is retired

**EP127 「못 알아듣는 말」** (`133_EP127_승인완료`, 5,246 chars, 10/3 Mon — a public
holiday, **Lucy POV**, no combat) is `GATE_D_PASS`. State = **SNAP-127**, tracker
SNAP-127 (`as_of_episode: 127` verified, 95 active), ledger **v2.22**.

**The chapter's process lesson outweighs its content lesson.** The beat-per-character
coefficient introduced two chapters ago has now missed twice, and the second miss killed
the whole approach:

| chapter | beats staged | predicted | first draft | hit rate |
| --- | --- | --- | --- | --- |
| EP126 | 60 | 6,000 | 4,802 | **80%** |
| **EP127** | 58 | 5,800 | **3,112** | **54%** |

EP126's fix had been "65 chars per combat beat, 100 for everything else." **EP127 has no
combat at all** and still came in at 44–71 per beat. The same category — deskwork scenes —
produced 102 chars/beat in EP126 and 59 in EP127. **The real variable is that beats are
not uniform in size**: `8시에 차가 안 왔다` is one sentence and twenty characters, while
`신고 셋을 읽는다` is a whole passage, and both were counted as one beat. No constant
survives that. Paragraph count failed the same test — 24.2 to 43.1 chars per paragraph
across the last 25 approved chapters (σ 4.74). **There is no reliable pre-draft length
predictor.**

**So prediction is abandoned and the correction cycle is shortened instead.** Measure at
the end of *each scene*; if that scene is under 80% of its target, add beats there before
moving on. Both chapters would have caught it early — EP126 at scene 3 (67%), **EP127 at
the very first scene (59%)**. The failure mode all along was writing the whole draft and
then running expansion passes, which is exactly what produced the frame-cloning of §8-2.
Shortening the loop addresses both. The beat sheet itself stays, with its role narrowed
to **material coverage** and **filling the closing scene first**.

**Content-wise, the user caught me repeating a canon misreading I had already documented.**
EP020's 「짚고 넘어가고 우회했으며」 describes the octopus-type creature, not the black
giant — G0-024 records that correction, and the draft made it anyway. Fixing it produced
a better scene than the error: Lucy opens the black giant's engagement records to refute
「검은 건 지켰는데」 and **the building-damage field simply is not there**. Not zero — not
tabulated. The creature files have damage records; the black giant's have a termination
time and a return status. **You cannot refute what is not recorded.** That lands exactly on
EP113's 「도시가 지켜졌다고 사람들이 생각하고 있었다」 — belief, not record. **What people
know is not in the files.** A second note then had me cut my own explanation of the
misreading, which was three paragraphs of Lucy noticing something she has no reason to
notice.

**A three-chapter object finally got an origin.** The shrimp in the freezer came from
Miran, given as change she did not have — EP122 receives it, EP124 has 「오늘도 안 꺼냈다」,
EP127 now reads 「냉동실로 옮긴 후 아직 안 꺼냈다」. **And today Lucy walks past that woman,
who looks at her for three seconds and says nothing.** In EP122 the other party always
spoke first.

**Emotion has now dropped below even the performance-degradation layer.** EP126 logged it
as 「왼팔 반응이 0.4초 늦다」; EP127 logs nothing — 「반응 지연 없음. 조작 오류 없음. (…)
전부 정상이었다」. The only trace is that her pacing comes out wrong at exactly one spot,
three of four sites measuring right on the first try, and **she does not record having
measured three times.** The narrator never calls it a trace either.

Next: **EP128**, closing 6-4 (10/5 Wed, Lucy) — Gaon corrects one word, 「그건 여기선
그렇게 안 해요」. **Six chapters unused; it lands here.** EP127 set the conditions: two
things Lucy has no field for, and the person who fixes her wording arrives in two days.

---

## EP128 approved (2026-08-24) — 6-4 closes, and the scene-level correction works

**EP128 「그럴 땐」** (`134_EP128_승인완료`, 5,003 chars, 10/5 Wed, **Lucy POV**, no
combat) is `GATE_D_PASS` and **closes sub-arc 6-4 「혼자 나가는 사람」** (EP121–128).
State = **SNAP-128**, tracker SNAP-128 (`as_of_episode: 128` verified, 98 active),
ledger **v2.23**.

**The process change introduced last chapter proved out on first use.** The draft came in
at 3,455 (59%), and instead of running expansion passes over the whole thing, each scene
was measured and filled in place:

| scene | first | final |
| --- | --- | --- |
| 1 | **41%** | 81% |
| 2 | **45%** | 87% |
| 3 | 67% | 88% |
| 4 | **53%** | 83% |
| 5 | 85% | 90% |

**And the frame-cloning did not appear**: `deictic` 3.5 against a band of 29.4, `closer`
24.3 against 67.5, verbatim overlap zero. **Shortening the correction cycle fixed §8-2's
problem as a side effect** — there is no long undifferentiated pass to clone rhythm during.
The coefficient missed again (59%), which is now expected: dialogue-heavy chapters run at
21.5 chars/paragraph, a value no constant reaches.

**A six-chapter unused asset finally landed.** Gaon's 「한 단어를 고쳐 옮긴다」 had sat
since EP122; reading the voice card showed what it actually is — **interpretation**. Lucy
speaks in form-language and Gaon relays it as human speech. She says 「판단은 해당 부서
소관입니다」 and Gaon turns to the resident with 「처리 계획은 담당 부서에서 잡고 있고요,
오늘 오후에 한 번 더 확인해서 알려 드릴게요」. **The word 「소관」 is gone and a time that
Lucy never said has been added** — 「그건 제가 알아본 거예요」, and why it was added goes
unexplained, per EP122's signature.

**The user caught a recognition hole before it was drafted.** My first plan had a resident
addressing Lucy directly, but **outside the machine she is a seventeen-year-old foreigner**
— EP127's 「아무도 이쪽을 보지 않았다」 exists for that reason. So the resident asks *Gaon*,
Gaon relays both directions, and **the nod at the end goes to Gaon.** Lucy is a party to the
conversation that no one looks at.

**And the closing line came from the user:** 「그럴 땐 그냥 감사합니다 하면 돼」. It pairs
exactly with Gaon — **he gives her what not to do** (「그건 여기선 그렇게 안 해요. 이유는……
저도 몰라요」), **Miran gives her what to do.** EP127 had already set the socket: 「인사를
해야 하는 자리인지 아닌지를 판단할 근거가 없었다. 인사에는 조건이 있고 조건을 배운 적이
없다.」 But Miran only said 「그럴 땐」. **Lucy learns in condition→response pairs, and the
condition field stays empty** — she does not delete the row.

**「루시 씨」 is first spoken here**, at the gate, matching EP122's 「백가온은 대문 앞에서
갔다」. Followed by 「오늘 그거, 잘못하신 거 아니에요」, with what wasn't wrong left unsaid.

**6-4's shape, in one line:** for eight chapters Lucy kept meeting places where the numbers
were right and nothing followed. **Here something finally works, and she didn't make it** —
the sentence in the form field is Gaon's. And the thing that closed has nothing inside it.

Next: **6-5 「조건」** (EP129–134), opening with **Myeongjun's POV** (EP129, his only
chapter in S14) — Dana's conditional return, and the obstacle that **direct neural sync now
summons what Sua went through, so the machine will not move.**

---

## S14 outline corrected to v1.1 (2026-08-24) — the missing link in Dana's return

**The user caught a structural hole spanning the whole sub-arc**: as written, **Dana has no
reason to return.** Lucy is holding the line alone and holding it well; moving the machine
somewhere is not a reason to put a pilot back in it. The master plot has the link and the
S14 outline had dropped it:

> **[전체 플롯 v2.2 §6-4 말미]** 그녀는 **전력 보강을 명분으로 블랙 타이탄의 재참전을
> 강하게 요구한다.** 실제로는 **단아와 겨뤄 자신의 우월함을 확인하고, 시민에게도
> 영웅으로 인정받고 싶기 때문이다.**

**Lucy is the one who demands Dana's return.** Outline v1.0 opened EP129 with 「협상이
끝난다」 and never said why negotiations resumed — the first link of the chain was gone.
Restored as **§3-1** in v1.1.

**Nothing is retro-fixed in EP121–128, and that is deliberate.** Lucy cannot name her own
need for recognition (settings book, narration card §2-3), so in her own POV the demand
would register only as a staffing judgement — 「전력 보강」. **EP128's remaining nameless
item is that demand**, and the reader learns it backwards in EP129, from Myeongjun, who
judges for a living and finds the request odd.

**This also supplies the reason the conditions exist.** Negotiations had been deadlocked
since EP115, where Myeongjun noted 「이쪽이 받겠다고 적은 것 중에 이 부대로 오는 물건이
하나도 없다」. Now **the other side wants something**, which is leverage — and since he
cannot verify why they suddenly want it, he blocks with conditions instead: voluntary
consent, treatment guarantee, family contact, no unilateral US control.

Tracked as **FS-S14-THE-DEMAND** (tracker SNAP-128, 99 active).

---

## Retrofits (2026-08-24) — the cap and the combat AI

Two settings-book items had been missing from the drafted chapters, both caught by the user.

**The cap.** The settings book lists it as **상징 장비 — 금색으로 USS CARVER DDG-501이
수놓인 감색 캡모자**, and the same entry gives Lucy's 핵심 가치 as 「타인의 명령에서
벗어나 자신의 욕구와 감정을 발견하는 과정」. **She wears her own provenance on her head**,
which is exactly the opposite of where the arc goes — so taking it off is an event, not a
costume note. The narration card had said 「모자챙은 긴장 디테일이라 **행동으로는 나오되
의미가 안 붙는다**」 and I read only the "남의 시점 자산" half, so **EP121–128 ran eight
chapters with no cap at all.** Retrofitted one sentence each into EP121, 122, 124, 126, 127,
128 — phrased differently every time, as EP116–118 had done. Combat scenes were left alone:
in operations she wears **카키색 커버올과 인이어 헤드셋**, not the cap. Card is now **v1.5**
with §3-3B; the embroidery itself stays off-page (self-appearance is barred by §3-3) and will
surface from someone else's POV later.

**The combat AI.** 통합설정집 v2.3 specifies **조종 — 루시의 신경동조 + AI 보조 제어**, and
adds the line that matters: **「AI는 루시의 자아를 보호하지만 동시에 완전동조와 정서적
자유를 통제한다.」** Protection and control are the same function and Lucy cannot tell them
apart — which is what she rejects in winter. Registered as **WS-01 §3-2B**.

**Callsign: 「딘」**, the user's choice, from **Dinkinesh** — the Amharic name for the same
fossil that is called Lucy. **Lucy and Din are two names for one thing**, so the AI that
guards her selfhood is her own other name, and refusing it in winter means pushing away her
other half. **The etymology is permanently off-page**; it lives in the sheet. Collision check
came back clean — the 102 hits for 「딘」 in the corpus are all fragments of 「어딘가」.

Retrofitted a few exchanges into the two combat chapters. EP124 gets 「딘, 접적 예정 좌표」
and the observation that **딘은 없는 것을 만들지 않는다** — late values that are usually
right. EP126 gets the sharper one: 「딘, 접촉.」 / 「없습니다.」 / 「장비 상태.」 /
「정상입니다.」 — **the AI cannot find it either**, and reports that fact as calmly as
everything else. Both chapters still pass all checks.

Narration card **v1.6** adds **§1-A**: Lucy's speech to Din is her most mechanical register
— imperatives, two words, no thanks — and that sits at the **opposite pole from §1-B**, where
she speaks English with Hyeonseo and the sentences finally run free. **The full range of one
character's dialogue lives between those two.**

---

## EP129 approved (2026-08-25) — 6-5 opens, and the comic register finally works

**EP129 「구경」** (`135_EP129_승인완료`, 5,192 chars, 10/6 Thu, **Lucy POV**, no combat) is
**a chapter that did not exist yesterday.** The user caught the hole: 「현재 루시와 화이트
센티널이 있어서 단아의 복귀명분이 없음. 기체를 옮기는 것 외에 전투에 나설 이유가 없음.
원래 루시가 타이탄과 센티널을 비교하는걸 듣고 (…) 타이탄 복귀를 굳이 요구하는 흐름이
있었는데 어느 단계에서인가 빠져버렸네.」 S14 outline v1.0 had 6-5 start with the demand
already in Myeongjun's inbox — **the cause had fallen out somewhere between the overall plot
and the season outline**, and nothing downstream noticed because every chapter after it still
read fine. It only shows when you ask *why*.

So the outline went to **v1.2**: EP129 inserted, 6-5 grown from six chapters to seven,
EP130–141 renumbered, and **only 6-5 slides a day** — 6-6's dates hold.

**The user designed the chapter.** 「루시의 구래동 생활도 조금 더 보여줄 겸, 여가시간이
비는데 이 시간에 뭘 할지를 몰라서 싸돌아다니면서 좌충우돌하는 일상의 하루, 그러다 마지막에
동네 카페에서 우연히 뒷자리에 앉은 성호와 우진이 요전번 전투에 대해 이야기하는걸 듣는거지.」
And the shape of it: 「중요한 장면은 4,5지만 2,3에서는 코믹 에피소드처럼 보이는 우습고 귀여운
부적응 삽화들이 들어가면 재밌겠네. **마지막에 뚝 떨어지는거지.**」

### The comic register, on the ninth try

Eight prior Lucy chapters and none of them were funny. This one is, and **nothing about the
prose changed to make it happen.** No narrator commentary, no 「우스웠다」, no 「당황했다」 —
zero. The mechanism is the settings book's own: **일상에서는 사람을 흉내내고 전투에서는
기계를 흉내낸다.** She folds her arms because the man ahead of her did. She laughs a beat
after the group laughs. She orders what the person in front ordered. **Card §2-4-2: the
awkwardness is visible only in other people's reactions** — the laughter stops first, the
answer comes half a beat late — and Lucy registers the delay without knowing its cause.

**She is completely serious the whole time. That is the joke.** And it means the drop at the
end needs no bridge: one sentence, and the same deadpan that was funny is not.

### 「감사합니다」 three times, and she doesn't know if any of them landed

EP128 gave her Miran's rule — 「그럴 땐 그냥 감사합니다 하면 돼」 — and left the condition
blank. **She uses it three times here and the blank is the whole point.** Third time she says
it alone and no one hears it. **FS-S14-WHEN-IS-THAT progressed without being answered.**

### 닥터 도 — first appearance, twenty-nine chapters after Lucy arrived

The user: 「루시와 현서의 유사모녀관계(전체 플롯)가 드러난 바가 없는데 여기서 나와도 되겠다.」
**G0-024 §4-3 opens partially** — that they are in contact, the name 「닥터 도」, that Hyeonseo
answers. Sealed: the nature of the relationship, who Hyeonseo is, her connection to Dana and
Sua. **Nothing is explained. It shows in the register alone** — the conversation is in English,
so this is the one place in the series where **Lucy's dialogue is fluent** (card §1-B). She
asks a follow-up question. Her sentences run to the end. `check_voice` flagged the
contractions and I overrode every one by eye, exactly as §1-B provides for.

The advice: 「일단 동네 구경이라도 해 보는 건 어때.」 And the line that sends her out the
door — **`절차가 없다는 것이 절차였다.`**

Also: **she does not say 「박사님」.** The 「박사님」 Lucy knows is Yeongjin, and she cannot
connect the two.

### The turn

Two kids at the next table — **Seong-ho and Woojin, unnamed on the page**, identified only by
청록 바람막이 / 주황 후드집업 / the battle notebook, per the user: 「지면상에 이름은 말 안해도
외형 특징을 서술하면 누구인지 독자가 알아볼 수 있겠다.」 They start on the white one and she
listens without meaning to. Then it turns into a comparison, and:

- 「검은 건 집을 안 부쉈잖아」 — **she has nothing to say against it**
- 「교실 부순 건?」 / **「그건 거인이 아니라 괴물이 한 거잖아」** — the kids have that
  distinction and **her forms do not.** There is no column for who broke it. There was never
  any need for one. (New thread: **FS-S14-WHO-BROKE-IT**.)
- Then **the kids change the subject and stay another while.** For them it was a passing
  topic. **For her it stayed.**

She walks back and opens 운용 건의 · 전력, a field untouched in twelve days, and files
**「전력 보강을 건의함」.** Three grounds, all of them true. And:
**`왜 오늘 이 칸을 열었는지는 적는 자리가 없다.`**

**EP130 receives it as a document.** Myeongjun will read a staffing request. **The gap between
the two POVs is 6-5.**

### Dates: seven wrong, and fixing them made the chapter better

I wrote every EP127 reference as 「어제」. The user: 「어제는 앞에서 가 아니구나, 며칠 되지
않았나.」 EP126 is **나흘 전**, EP127 **사흘 전**, EP128 alone is 어제. That produced the
contrast the ending needed: **어제 것은 들어갔다. 어제는 문의였고 답변란이 있었다. 오늘 것은
문의가 아니다.** Fourteen temporal deictics checked against the calendar.

Also: the flyer chasers are **crows, not pigeons** — 「비둘기는 전단지에 관심이 없을거고
반짝이 스티커가 붙은 전단지라 까마귀들이 따라오는게 자연스럽겠군.」 She becomes **the one
being followed**.

### Scene-level correction, second run

3,651 chars at first pass (63%) → **5,192**. Every scene was under 80% at its own close and
got filled there. **Two chapters in a row now** (EP128: 3,455 → 5,003). And unlike the
coefficient it replaced, **it does not have to predict anything** — it measures what is
already on the page. `deictic` 3.1 (band 29.4), `closer` 37.4 (band 67.5), verbatim
repetition 0. **Filling the room did not duplicate the sentence shapes.**

Next: **EP130** (10/7 Fri, **Myeongjun** — his only chapter in S14). The demand arrives as a
document. He judges that 전력 보강 is not all of it and **has no way to check.** So he does not
refuse; **he attaches conditions** — 자발적 동의 · 치료 보장 · 가족 접촉 · 단독통제 금지, the
EP115 condition sheet signed at last. **EP115 inverts: this time the other side wants
something.**

---

## EP130 approved (2026-08-25) — the terms are signed, and the clause has two sides

**EP130 「동의」** (`136_EP130_승인완료`, 5,780 chars, 10/7 Fri, **Myeongjun POV** — his
fifth, and **his only chapter in S14**) is `GATE_D_PASS`. State = **SNAP-130**, tracker
SNAP-130 (`as_of_episode: 130` verified, **106 active**), ledger **v2.25**.

**This chapter is EP115 run backwards.** EP115 built a table, couldn't price the left
column, and **folded the paper with the child's cell blank** — deliberately, noting that
folding it neatly means you can see the crease later. EP130 unfolds it. Every EP113/115
constant inverts, and the prose does it with the *same sentence shapes*:

| EP113 / EP115 | EP130 |
| --- | --- |
| the bag was never opened, never even looked like opening | **he opens it** |
| no deadline was mentioned | **a date, in the English copy only** |
| no next appointment | **2 p.m.** |
| the left column was empty | **they filled it themselves and mailed it** |
| folded it neatly | **unfolds it** |
| left the child's cell blank | **writes a sentence where the name goes** |
| 「그 애들 어떻게 됩니까」 | **it was decided today, and today she doesn't ask** |

### The three absences

The request's stated ground is one line — 「현 전력으로는 방어 밀도가 충분하지 않음」 — and
Myeongjun, who thinks by counting, counts. **The number of sorties equals the number of
sorties not lost.** The side that is winning is asking for reinforcement. So there must be a
second ground, and there is one available: **October 2nd, four civilian houses.** Two
machines means one herds and one blocks, which means less shelling, which means fewer houses.
It is the strongest argument in existence and **it is not in the document.** `제일 좋은 근거를
안 쓰는 경우는 둘이다. 그 얘기를 꺼내면 안 되는 사정이 있거나, 근거가 필요 없다고 보거나.`

Second: **there is no age field.** The Korean forms carry all three ages at the top — 만
일흔다섯, 만 열두 살, 만 아홉 살 — and everything below is determined by those numbers. The
other side's form simply has no such column. **`칸이 없으면 안 적는 게 아니라 애초에
물어보지 않는다.`** This deepens EP113's observation (one name large, two small, versus no
difference at all) by one turn: **not a difference, an absence.** And it is the chapter's
cleanest trick — **Lucy's sealed age becomes a page device without the seal moving an inch.**

Third, from Bonsik: **nowhere to stand it.** Fifty-odd metres, no building in the country.

### 「블랙 타이탄」 is written on their paper

Three things came out of drafting that the brief did not have, and this is the best one. The
Korean side has been writing 「미식별 검은 거인」 since spring with the subject field blank —
**the name has never once been written on a Korean document.** It is on theirs. So: `저쪽이
물어봤고 누가 대답했다는 소리였다. 대답할 수 있는 사람은 셋뿐이다.` And then the line that
is both a misreading and exactly true:

**`이쪽하고는 아무도 말을 안 하는데 저쪽하고는 누가 말을 했다.`**

**The reader knows it was EP116** — two children in a visiting room telling each other what
their machines are called. **Myeongjun reads a security breach.** The season's stated form —
「두 시점의 낙차」 — completes here for the first time.

The other two: **the Korean and English copies differ in two places** (title: 협의 요청 /
closer to 통보; and the English one ends with a bare date), which Yun Seojin collated
**without being told** — the card's 「절차를 한 단계 더 밟아 준다」 firing once. And at the end
of the day she puts down **a second, unrequested document**: the 「보호」 item he struck from
the table that morning, prepared down to the reason field. 「이건 왜.」 / **「올려 두면 필요할
때 서명만 하시면 됩니다.」** EP115's question gets its answer this way — **she doesn't ask;
she puts down a piece of paper.**

### Three offered, four signed

He goes in with three, having cut 「보호」 (not the other side's business — his own
signature blocks that) and deliberately withheld the stalled data-sharing request, because
**offering four gives them something to shave.** Hale shaves nothing. He takes all three.

**And that is the worst signal in the chapter.** `급해서 받거나, 그게 저쪽한테 아무 손해도
아니어서 받거나.` There is no way to tell which. **`확인할 수 없는 걸 막는 방법은
하나뿐이다. 못 움직이게 묶는 것.`** So he adds a fourth on the spot — **자발적 동의**, no
proxy consent, not the guardian and not this unit.

Then Hale says one memorised sentence without the interpreter: **「장군님. 저희가 먼저 한
요청이 아닙니다.」** It costs him — admitting the request came from below reduces its
weight. `무게를 줄이면서까지 말한 거였다. / 왜 그랬는지는 몰랐다.` **The one free thing
anyone hands Myeongjun all day, and he cannot spend it.**

### The clause has two sides and he sees both

> 동의라는 건 물어야 성립한다. 물어야 성립하는 것은 물으면 대개 나온다. **어른이 정복 입고
> 앉아서 아이한테 물으면 아이는 하겠다고 한다.**

So the clause does not block them; it blocks only his own side from deciding unilaterally.
And then the second turn — what the answer becomes once it is written down: **「본인이
원했다.」** `편지에도 그 줄이 들어간다. 삼십 년 동안 그 줄이 들어간 편지를 몇 통 봤고 몇 통
썼다. 그 줄이 있으면 받는 쪽이 조금 낫다. 쓰는 쪽도 낫다.` **The clause manufactures that
line in advance.** He knows, and keeps it: `아이가 정하는 것보다 나은 건 아무도 안 태우는
건데, 그건 오늘 표에 없었다. / **없는 것보다 낫다. 오늘 받아 낸 것 중에 그게 제일 정직한
평가였다.**`

And the third side, the one that is about him: **it means he never has to write a name in
that cell.** `적는 손은 자기 손인데 정한 건 자기가 아니게 된다.` **`두 개가 같은
문장이었다.` (…) `갈라 쓸 방법이 없었다.`**

The ending puts a sentence where the name goes — **「본인이 하겠다고 할 것.」** — then adds
one more row, 「누가 가서 묻는가」, and fills it. **The man who sat in a hospital car park in
EP115 and could not go in is going.**

> **이 표에서 이름이 적힌 칸은 그게 처음이었다.**

### Craft

**Scene-level correction, third run — and this time nothing needed correcting.** 5,780 on
the first pass, expansion passes zero. Setting per-scene targets and filling from the closing
scene backwards has become the default motion.

**`closer` = 6.9**, against a band of 67.5 — a tenth of it, in a *judging character's judging
chapter*, where 「것이다·뜻이다·셈이다」 is the natural failure mode. The substitutes are
worth registering: **「~거였다」 · 「~라는 얘기였다」 · 「~였다」**. This chapter is now the
reference sample for that.

One user edit, and it was the only speech-level slip in the chapter: 「국문입니까 영문입니까」 →
**「국문이야 영문이야」**. A full audit followed — Myeongjun's subordinate register is clean
everywhere else (`해` `말해` `무슨 날짜인가` `읽어 봐` `없어` `고맙다`), and 존댓말 survives
only in the Hale scene. Four elapsed-time corrections were also made against the calendar.

**SNAP maintenance:** the `myeongjun` block had been sitting in its spring state (봄 결산
보고 · 민간 복귀) all through EP110–129. Rebuilt from scratch; `seojin` refreshed; **`hale`
added** (21 characters).

Next: **EP131 「묻는다」** (10/8 Sat, **Dana**) — **the first time anyone asks her.** It is
S13's collection point (명단 · 왼쪽 · 안 물어서 안 했다), and **the reader already knows where
her answer is going to be filed.**

---

## EP131 approved (2026-08-25) — the first time anyone asks her

**EP131 「묻는다」** (`137_EP131_승인완료`, 5,363 chars, 10/8 Sat, **Dana POV**) is
`GATE_D_PASS`. State = **SNAP-131**, tracker SNAP-131 (`as_of_episode: 131` verified, **110
active**), ledger **v2.26**.

**Ko Myeongjun and Do Dana are in the same room for the first time in 130 chapters.** He wears
dress uniform — a private visit would not satisfy the clause, so **the clause he wrote
yesterday put him in uniform.** From her side that reads as: `어른이 자기한테 존댓말을 쓰고
있었다. (…) 병원에서도 여기서도 다들 해라체였다. 단아야, 이거 할까, 저기 앉을래. 그건
애한테 하는 말이었다. / 이건 그게 아니었다. / **이건 어른한테 하는 말이었다.**` EP130's
judgement — 「어른이 정복 입고 앉아서 아이한테 물으면 아이는 하겠다고 한다」 — executes on
the page and **the narrator never points at it.** Three chapters running now, the season's
stated form (「두 시점의 낙차」) has done the work: EP129 → EP130 → EP131.

**And the room is not new.** Two people have sat across that table before: **her mother**
(EP108, whom she never once called by any name across forty minutes) and **the one who came
as a person** (EP116–117, who asked and asked). Today is the third. He asks **「그걸 탈 줄
압니까」**, she says 「알아요」, and he **nods and stops** — no how many times, no who put you
in it. **Of the three, only one didn't demand an answer.**

### 「지금은요.」

The chapter's spine came out of drafting, not the brief. She asks **「수아한테도 물어봐요?」**
He answers 「지금 타는 사람은 하나입니다.」 / 「누구요.」 / 「도단아 씨입니다.」 And she hears
the first word again:

> **"지금은요."** / **"…예."**
>
> **아니라고 안 했다.** 아니라고 할 자리였는데 안 했다. (…)
> **`아니라고 안 한 건 아닌 게 아니라는 뜻이었다.`**

**EP115's arithmetic — 저쪽 셋 − 이쪽 둘 = 하나가 남는다 — gets caught by a
thirteen-year-old.** It works because EP130 spent a whole chapter establishing that this man
does not lie, so **he cannot deny it here.** And that, not the conditions, is what produces
「할게요」: `지금은, 이라는 말은 나중에는 다를 수도 있다는 말이었다. (…) **저쪽은 지금 못
걷는다.** / **여름에 몇 번 그랬다. 자기가 안 나갔고 그날 나간 건 수아였다.**` EP119–120's
guilt reignites with **zero explanation attached.**

Two more things came out of drafting. **「합의」** — the only one she has ever been part of is
a classroom vote (EP032, the sunset was voted down and they settled on one small sun in the
corner of the map): `그때는 그 자리에 자기가 있었다. 손을 들었고 셌고 졌다. / **이번 것은
자기가 없는 데서 됐다.**` And the silence: `여기 어른들은 조용해지면 뭘 채운다. 괜찮아,
천천히 해, 급한 거 아니야. (…) **이 사람은 안 채웠다.**`

The ending pairs with EP129 across two POVs. Lucy: **왜 오늘 이 칸을 열었는지는 적는 자리가
없다.** Dana: **이름 쓰는 칸은 있었다. 왜 그렇게 했는지 쓰는 칸은 없었다.** Different
sentences, same form — **two children in front of the same paperwork, sitting apart.** Then
the order she only notices afterwards (treatment → the list → danger → *for now, one* → the
question → yes), and the letter under the pillow: `오늘은 생겼다. / 생겼는데 이건 더 못 쓰는
거였다. 군인이 와서 물어봤고 자기가 한다고 했다는 걸 종이에 적어서 부칠 수는 없었다.` The
sender field is still blank. **`오늘 이름을 한 번 썼다. 쓰라고 한 데다 썼다. / 쓰고 싶은
데는 아직 못 썼다.`**

### Three canon misreadings, all from one gap in the sweep

The user's twelve edits included three real corrections, and **all three came from the same
omission**: the brief swept 「면회」 but never asked *who had been in that room*.

1. I wrote that the people who interrogated her in the visiting room were **investigators**.
   They were not. **Only her mother and Lucy have ever sat there.** Corrected to **「전에 온
   언니는 잔뜩 물었다」** — which is far better, because it puts all three visitors on one
   axis.
2. I had her **deducing** Sua's condition alone. **Her mother told her** (EP108). What was
   new today is the *other* half — **「방금 그 사람이 반쪽을 알려 줬다. 잡혀있는 쪽.」**
3. I wrote that Sua **is not** being treated. She is (EP125, rehab). The condition is
   therefore **「치료를 계속 받습니다」**, and the frightening reading is **「앞으로 안 받을
   수도 있다는 뜻이었다」** — which is sharper and feeds the closing arithmetic (`조건 안에
   있는 건 조건이 없어지면 같이 없어진다`).

Also: adults address Dana in **해라체**, not 해요체; and he introduces himself as **「사령관
고명준」**. And the two names on the visiting list are now fixed: **엄마라는 사람 · 외국인
언니** — `찾아온 둘 중 누구도 단아가 원했던 사람은 아니었다. (…) **명단에 드디어 단아가
원했던 사람이 들어온다.**` That closes EP108 whole: she still has no name to call that woman
by, while **Sua called her 「엄마」 twice in EP125 and the second time was easier.** The
chapter does not point at it.

### Craft — the scene-fill rule found its counterexample

**First pass came in at 2,877 — fifty percent.** EP130 had landed inside the band on the
first pass; this one landed at half. Scene fills brought it to 5,363 with every scene ≥83%.

**The cause is now clear: a dialogue-driven scene's beat is short.** Every beat from the
brief was present; a line of dialogue just doesn't reach ten characters where a narration
beat runs past a hundred. **New rule candidate for §8-2: when a scene is dialogue-led, budget
1.5× the beats.** Without scene-level correction this chapter would have finished under
3,000.

`past_run` came in at 12 and was repaired to 8 by turning one sentence present-tense (「이
방에서 제일 안 놀라는 애가 **다은이다**」) — deliberately *not* the 순서 list, whose anaphora
is the point. Narration's 「그 사람」 went 14 → 9 via subject-dropping; the remainder is
design, since **she was told his name and still has no name to call him.** Dana's card
prohibitions (self-analysis, 관조체, 「~인 셈이었다」) come back zero.

**SNAP maintenance:** `dana.location` had been stuck at **「집(6/28 밤)」** since summer.
Corrected, with `myeongjun` and `mother` relations added. The eighty-eight-entry summer body
log is kept — that record is a long-range asset.

Next: **EP132** (10/10 Mon, **Dana·Yeongjin**) — **the person added to the list yesterday
actually arrives.** It collects **삼십 년의 왼쪽** (EP114) and the list itself (EP107·115·116·131).
**The family sits down together for the first time since August 31st** — and Dana signed
yesterday, which Yeongjin does not know.

---

## EP132 approved (2026-08-25) — two hands, five seconds

**EP132 「손이 하나」** (`138_EP132_승인완료`, 5,372 chars, 10/10 Mon, **two-part POV —
Dana for scenes 1–3, Yeongjin for 4–6, no bridging sentence**) is `GATE_D_PASS`. State =
**SNAP-132**, tracker SNAP-132 (`as_of_episode: 132` verified, **114 active**), ledger
**v2.27**.

**Forty days after August 31st the family sits down together.** And the visit is one
**Yeongjin never asked for** — EP111 gave the reason in his own words: `물어보면 대답이
온다. 대답이 오면 그걸 들고 있어야 한다`, which is why he said nothing when Myeongjun
raised it in EP114 (`면회 신청을 안 묻는다 — 물었으면 넣어 줬을 자리`). **Today that rule
breaks.** He asks one question and has to carry the answer.

Dana leaves the facility for the first time since September 1st — three sign-outs to get
through the door, shoes that have gotten a little small, autumn going past instead of
standing still (`서서 보는 가을은 안 움직인다. 오늘 것은 뒤로 흘러갔다`). Where they stop is
not a police station and **she has no name for it.** In the waiting room everyone is holding
a bag and she is not: **`뭘 가져와야 하는 건지 아무도 안 알려 줬다. 알려 줄 사람이 없었다는
게 더 맞았다.`**

Across forty minutes she brings out **none of the three questions she prepared** — and this
is a different failure from EP131. There she could not produce an *answer*; here she cannot
get a *sentence started*, because starting it means starting from 「내가 하겠다고 했어」. What
she gets instead is **「손톱 깎았냐」** — asked about a hand that never came above the table —
and then his right hand goes up onto it. **`집에서는 손이 빈 적이 별로 없었다. (…) 여기서는
아무것도 안 들고 있었다. / 빈손이 탁자 위에 그냥 있었다.`** Then: **「단아야.」 / 「하겠다고
했냐.」 / 「…응.」** He does not stop her, does not ask why, does not say she did well. He
answers with an object — **「그거 손보려면 시간이 좀 걸린다.」** — and she understands it with
no explanation attached, because **`그 말을 할 수 있는 사람은 하나뿐이었다`**.

### Part two: he already knew

The notice was two lines with no reason field, and **a body that knows procedure runs the
sum backwards**: `스무닷새 동안 안 되던 게 갑자기 되면, 되게 만든 사람이 있다는 뜻이다. (…)
그 사람이 공짜로 할 리가 없었다.` → **`값이 붙었을 것이다.`** → one machine to stand up, one
seat to fill, two candidates, one of whom cannot walk → **`그러면 남는 게 하나다.`**

**EP115 (Myeongjun), EP131 (Dana) and EP132 (Yeongjin) have now each arrived at the same
arithmetic, independently, without ever discussing it.**

### The seal violation, and why the fix was better

The draft had him unable to stop her because **someone had once given him those same three
reasons thirty years ago and he hadn't listened.** The user caught it in one line: **「30년
전에 대 줬다는건 새로운 내용인데」**. It was — an invented person and an invented event, in the
exact area Level 6 §2 had sealed as permanent zero.

**Re-sweeping found the material already on the page.** EP081: `봄에는 위험하다는 말을 애한테
할 수가 없어서 기계 얘기를 했다. 오늘은 기계 얘기를 쓸 수가 없어서 나이 얘기를 했다. **댈 수
있는 이유가 처음부터 끝까지 핑계뿐이었다**`. EP028: `위험하다는 말부터 하는 사람이 승낙을
말하는 방식이, **조건이라는 것**`. So the rewrite:

> 셋 다 전에 써 본 것들이었다. (…) **둘 다 핑계였다. 핑계인 걸 그때도 알았다.**
> 그리고 두 번 다 결국 보냈다. **조건을 붙여서 보냈다.**
> **오늘 저쪽이 한 것도 그거였다. 조건을 넷 붙이고 승낙했다.** / **같은 모양이었다.**

**This is strictly better.** Instead of a person who does not exist, it puts **what Myeongjun
did yesterday and what Yeongjin did in spring into the same shape**, which lands EP028's
「조건을 붙여 승낙하는 방식」 directly on top of EP130's four conditions — the season's own
axis (6-5 「조건」).

**§8-2 gained a rule from this.** The seal list is *lexical*: `배양금속`, `현서`, `역장` all
trip the grep. **A sentence that invents a new fact contains none of those words** — 「삼십 년
전에 자기한테 대 준 사람이 있었다」 trips nothing, and all five checks passed. So: **for any
chapter that grazes a sealed area, pull every sentence in that area and cite a canon chapter
for each. No citation means it is invention.** Danger phrasings to watch: 「~한 사람이
있었다」, 「그때 ~하기로 정했다」, 「나중에 알았다」, 「~한 적이 있다」. And the general
lesson: **the places where invention feels necessary are usually places the sweep didn't
finish.**

### Thirty years, three times, none of them about the work

The closing recovers **the left arm from Yeongjin's side.** EP114 had it as Myeongjun's
comparison (photo with an arm / ten characters on a form / a folded sleeve). EP111 had it as
**visibility** — fold it and it doesn't catch, don't and people look. EP132 makes it
**capability**: her glasses sat crooked for the whole forty minutes, and fixing them needs
one hand on the frame and one on the hinge. `봄에 그렇게 해 줬다. **그때는 작업대가 있었다.**
(…) **받침이 왼손 노릇을 했다.** (…) **삼십 년 동안 하나씩 만든 것들이었다.** / 여기에는
아무것도 없었다.` Then: `삼십 년 동안 이 손으로 못 하는 일이 몇 개 있었다. **세면 목록이 되고
목록은 들고 다녀야 하니까 안 셌다.**` — and **`도구를 만드는 데 삼십 년이 들었을 뿐이다`**,
and the last line: **`두 손이면 오 초면 되는 일이었다.`**

**「삼십 년」 appears three times and not one of them is about the work** — tools, a list, and
time. The seal never moves and the weight arrives anyway.

### Craft: the new rule paid off in one chapter

**EP131's lesson — budget 1.5× beats for a dialogue-led scene — went straight into this
brief.** Scene 3 (the forty minutes) got fourteen beats and **came in at 71% on the first
pass**; EP131's equivalent scene had come in at 40%.

| chapter | first pass | scene type |
| --- | --- | --- |
| EP130 | 100% | narration-led |
| EP131 | **50%** | dialogue-led, **no rule** |
| **EP132** | **75%** | dialogue-led, **rule applied** |

`check_voice` returned **CHECK 4 — the series low** (four characters, every form of address
straight from canon). Dialogue ratio is **15.1%**, the lowest in a long while, which is right
for a chapter whose subject is what does not get said. `past_run` 11→8 was repaired with one
present-tense sentence; `deictic` came down 30.0 → 27.6 as the scene fills went in.

**SNAP maintenance:** `youngjin.location` had been sitting at **「수리점(6/21 밤 —
장부·접수)」** for four months. Rebuilt. With Myeongjun (SNAP-130), Dana (SNAP-131) and
Yeongjin (SNAP-132), the main character blocks are now current.

Next: **EP133 「못 움직인다」** (10/12 Wed, **Dana**) — **reactivation, and she cannot move.**
Not fear: **something comes up.** She rode it when she didn't know there was a safety on it;
now that she knows, she can't. **She said yes two days ago and today her body does not.**

---

## EP133 approved (2026-08-25) — it turns on, and it does not move

**EP133 「하던 대로」** (`139_EP133_승인완료`, 5,600 chars, 10/12 Wed, **Dana POV**, third
consecutive) is `GATE_D_PASS`. State = **SNAP-133**, tracker SNAP-133 (`as_of_episode: 133`
verified, **119 active**), ledger **v2.28**.

**Forty-two days on, it comes on.** Dana goes inside the machine for the first time — she has
seen that spot twice and **both times from outside** (EP101–102 through a screen, EP103 at
night while they cut the hatch open). The mudflat still holds the gouge from the knees,
and it is pushed **toward the city, not the sea**: `그날 여기서 뭘 하고 있었는지는 안다.
화면으로 다 봤다. 그런데 **끝난 다음에 어디로 가려고 했는지는 화면에 안 나왔다.** /
**자국에는 나와 있었다.**`

She goes in through the **left round hatch** — heavier than usual, because a hatch that opens
inward fights you when the machine is tilted — along a corridor that runs from the left shell
to the chest centre, over one bulkhead whose handrail has **worn through the paint in the
shape of a hand**, and across two metal plates to the seat. Shoulder strap first, waist strap
second: `순서가 몸에 있었다.` The seat light goes amber, then green.

**Then her left hand goes to the cover and presses what's under it.** `눌러 본 지
마흔이틀이었는데 **손이 자리를 안 찾았다. 처음부터 알고 갔다.**` The radio outside stops all
at once and Dana does not know why — `원래 이러는 거였다`. Later she is told nobody has been
able to start it in forty-two days, and it doesn't land: `켜는 게 어려운 거라고 생각해 본
적이 없었다. (…) **그 사람들이 앉았을 때는 안 켜졌다.**`

And then it does not move. **The cause is two things at once, and she cannot separate them.**

**① She doesn't know how.** `여름 내내 이걸 했는데 **이게 뭔지를 몰랐다.** / 몰라도
됐으니까. 하면 됐으니까.` EP118's line finally acquires a value fifteen days later — 「왜
안전장치 뒤에 있습니까」 means **there is somewhere that isn't behind it**, and `단아는 그걸
해 본 적이 없었다`. No one taught her and there is nobody to ask: **`그 말을 한 사람은 여기
없다. 할아버지는 아직 안 왔다.`**

**② Her body refuses, and she doesn't know that's what's happening.** `무서우면 심장이
빨라지는데 안 빨라졌다.` What arrives instead is August 31st — the screen shaking once and
stopping — and this time: **`지금은 등 뒤의 구멍이 생긴 순간이라는 걸 안다`** (the user's
line, inverting EP102's 「봤지만 뭔지 모른다」). **She never connects that to the failure. The
reader does.** Outside, nobody gets angry, and `**아무도 화를 안 내면 그건 처음부터 안 되는
걸로 되어 있었다는 뜻이 된다.**` Closing: `이 몸은 봄부터 여름까지 시키기 전에 먼저 했다. /
**오늘은 시켜도 못 했다.**`

### Four canon violations in one chapter, and the checkers caught none of them

This chapter produced the clearest lesson of the run so far.

**① Control mechanism — style card §2-9.** The draft had her physically raising her arm and
the machine following. That is whole-body motion capture, which §2-9 and LOC-01 §4.4 both
forbid. Corrected to intent-input: `자기 팔을 올리려 생각하면 기계가 신호를 받아서
움직인다`, with **「팔을 직접 움직여 봤다」 made a separate verifying action** — which
sharpens it into *the body is fine, only the signal isn't going*, and puts it back in line
with EP001's 「마음먹은 대로 움직인다더니」.

**② LOC-01 was never opened.** The user's correction was three words: **「조종석은 loc에
있음」**. Five things were wrong — hatch location, the harness, **the covered ignition
switch**, the panorama screen, the control sticks. The switch mattered most: 「앉으니까
켜졌다」 became **「덮개를 젖히고 그 아래를 눌렀다」**, and the mystery got *tighter* — anyone
can press a switch, and it still only starts for her.

**③ Invention.** A sheet of paper with the startup order on it, taped inside — except the
order went in by sleep-learning (EP109). Replaced with `배운 기억이 없는데 손이 아는 것들이
여기 많았다.`

**④ Physics, twice.** A hatch that opens inward does not swing further open when tilted, and
a kneeling machine tips its occupant **forward**, not back.

**And then the sheet itself turned out to be wrong.** LOC-01 v0.1 said the space inside the
hatch was 「한 사람이 간신히 지나는 짧은 통로」, and the user's judgement was that **fifty-two
metres of machine needs distance between the left shell and the chest centre**. Re-reading
EP002 found the reconciliation: 「**통로 끝에** 작은 해치」 (outside the hatch) and 「금속
발판을 건너 좌석까지」 (the last stretch inside) are **two different segments that v0.1 had
collapsed into one**. **LOC-01 is now v0.2** with the two-segment structure, the bulkhead and
its hand-worn rail, hatch resistance under tilt, and a separate field-access route.

### §8-2 gained two rules

**Checker-invisible violations, in three kinds:** ① new people/events (no sealed vocabulary
appears), ② a character's realisation moved earlier (a *state*, not a word), ③ descriptions
that contradict canon mechanics or space (physics, not forbidden terms). Level 6 now carries
three counters: **seal-area sentence audit with a chapter citation each**, **a knows /
doesn't-yet-know table**, and **§2-8·§2-9 copied in verbatim whenever a control scene
exists.**

**And LOC comparison is now a mandatory §0 item alongside the sweep** — the rule 「공간
바이블은 브리프에서」 already existed and still failed, because there was no slot in which to
execute it. With a rider: **opening the sheet and trusting the sheet are different things.**
Open it, check it against the page canon, check the physics, and **fix the sheet when it
doesn't hold.**

### Craft

**First pass 3,369 (56%), four fill rounds to 5,600.** EP132's dialogue-led rule had just
worked, so this was a surprise — and it exposes the real variable. **It isn't
dialogue-versus-narration; it's whether anyone is talking.** EP130 (narration, people
talking) came in at 100%; EP133 (narration, alone in a box) at 56%. **A chapter where the
character is alone runs short regardless of mode.**

`closer` 11.0 and dialogue 10.9% are both series lows, which is right for a chapter whose
whole event is one person failing to do something in silence.

Next: **EP134** (10/13 Thu, **Sua**) — discharge comes up, and **a wheelchair**. Dana couldn't
move yesterday and **Sua doesn't know that.**

---

## EP134 approved (2026-08-25) — discharge is not good news

**EP134 「화요일하고 금요일」** (`140_EP134_승인완료`, 5,034 chars, 10/13 Thu, **Sua POV**,
her second in S14) is `GATE_D_PASS`. State = **SNAP-134**, tracker SNAP-134
(`as_of_episode: 134` verified, **123 active**), ledger **v2.29**.

**The user's question set the chapter: 「호전 없는 퇴원은 좋은 소식이 될 수 있을까」.** It
cannot, so the chapter never pretends. `나으면 나가는 거라고 생각했었다. (…) **순서가
반대였다.** / **여기서 할 게 없어지면 나가는 거였다. 나아서 나가는 게 아니었다.**` The
causation was already on the page in EP106 — 「검사에서는 안 나와요. 그게 지금 제일
문제예요」 — and twenty-four days later it still hasn't acquired a name: `안 붙은 걸 계속
입원시켜 놓고 볼 수는 없는 모양이었다. **침대는 아픈 사람이 쓰는 거고, 아픈 데가 어디인지
안 나오면 그 침대를 계속 쓸 이유를 못 댄다.**`

**The second user correction is what gives the chapter its blade: 「나가라 끝이 아니라
퇴원하고 통원하라 정도겠네 특히 재활은」.** Rehab continues — **Tuesdays and Fridays, 10
a.m.** So **EP130's condition ① is honoured on paper.** But an appointment schedule presumes
two things: somewhere to live, and someone to bring her on those days. **Neither exists.**
`이 종이를 만든 사람은 그게 되는 걸로 알고 적었을 것이다. **대개는 되니까 그렇게 적는다.**`

**★★★★★★ What Myeongjun negotiated was 「치료를 계속 받는다」, not 「다닐 데가 있다」.**
The condition holds and the thing still doesn't move — which is exactly the right ending for
6-5's last Sua chapter.

### The guardian blank

EP115's unfillable field arrives on the child's side twenty-five days later. The user
corrected my reading of 직계 (I had 이모 in it):

> **직계라는 건 엄마, 아빠, 할아버지, 할머니다. 수아에게는 그중에 하나밖에 없다.**
> **키워 주는 사람도 할아버지다. 그 밖에는 없다.**

**Both criteria collapse onto one person, and she doesn't know where he is** (EP106 asked;
no answer has arrived on the page since). Not a shortage of candidates — **there was only
ever one, and he's missing.** The three she drew in a 2학년 family-drawing assignment become
the list: 할아버지 · 언니 · 수아. `**더 그리라고 했으면 못 그렸다.**`

### The caregiver came back

**The user caught that she had vanished after EP106**, and her card line turns out to be the
chapter's own structure: **절차는 알고 사람은 모른다.** She reads the discharge list
fluently, knows how wheelchair rental works, knows the appointment days — and **cannot fill
the one field that matters.** She is not a guardian. `**퇴원하면 이 사람도 없어진다. 병원에
있는 사람이지 수아한테 붙어 있는 사람이 아니다.** / **여기 있는 것 중에 같이 갈 수 있는 게
하나도 없었다.**` It closes as EP106 inverted: `모르는 사람한테 모르는 걸 물은 거였다` →
**`아는 사람인데 해 줄 수 있는 게 없었다`**.

### Five canon violations — and one the checker caught first

**① Speech level.** Jo Mingyeong speaks to Sua in **평어**, and I wrote her in 해요체. The
cause was the card: her example line is 「검사에서는 안 나와요」, and **I read one example
sentence as a register rule.** The card already says otherwise — 「대사 예시는 모방 기준이지
재사용 문장이 아니다」 and 「이 카드가 정하는 것은 발화 리듬, 관심사, 감정 우회 방식, 호칭
기본값이다」. **The card sets rhythm, not register, and an example may be that character
speaking to someone else.** Eight corrections; and **`check_voice` went CHECK 5 → 2**, which
means a good share of "speaker unknown" warnings had been symptoms of the register error.

**② 직계.** **③ Curriculum arithmetic** — I wrote 「종목이 하나도 안 늘었다」 while scene 5
had her pushing eight times; corrected to **one item added**, which is sharper: `**늘긴
늘었는데 앉아서 하는 것에서 앉아서 하는 것으로 늘었다.**` **④ Voice bleed** — 「수아 씨」 is
Kwon Doyun's marker and had leaked into Jo Mingyeong (same lineage as EP119, where
Myeongjun's 「받아 놨다」 leaked into a Sua chapter).

**⑤ 계단 — and this one the checker caught before I did**, flagging G0-013 (the house is
single-storey, stairs stay off-page). The fix improved it: 「집에 **턱** 있으면 미리 봐 둬야
하고」 → `마루에서 마당으로 나가는 데다. **낮아서 걸어 다닐 때는 있는 줄도 몰랐다.** (…)
**바퀴로 넘으려면 그것도 턱이다.** / **턱이 하나뿐인 집인데 그 집에 지금 아무도 없다.**`

### §8-2 gained two more rules

**「말투 카드의 대사 예시는 화계 근거가 아니다」** — pull register from the page, per
counterpart, and record it in Level 6 as **「A → B 화계」**, because register changes with who
is being addressed.

**「대화가 아니라 주고받는가」** — EP131's dialogue-led 1.5× rule met its exception here.
Scene 3 has dialogue and came in at 46%, because **Sua barely answers.** The doctor talks and
the child returns 「네」 and 「…」. The real variable isn't whether there's dialogue but
**whether it's exchanged.** The beat-length table now reads: narration with people talking
100+ chars; dialogue exchanged 1.5×; **one-sided dialogue 1.5× plus narration beats**; and
**alone in a room runs short regardless** (EP133).

Next: **EP135** (10/14 Fri, **Dana**) — **it comes, and she doesn't know why.**
(Superseded plan: the joint sortie was scrapped in S14 v1.4 — the machine still can't stand.)

---

## EP135 approved (2026-08-25) — it comes, and she doesn't know why

**EP135 「열 번에 세 번」** (`141_EP135_승인완료`, 5,154 chars, 10/14 Fri, **Dana POV**,
combat 0) — **6-5 「조건」 7/9 · S14 15/23.**

Third day of the drive out. The right arm **comes up** for the first time since EP133 —
and it's **slower than spring**: `밀다가 걸리고 밀다가 걸리는 것 같았다. 뭔가에 걸리는 게
아니라 미는 쪽이 자꾸 놓치는 것 같았다.` She isn't glad. Before gladness comes the search
for what was different, and she can't find it. Then the count: **three in ten.** In spring
it was ten in ten.

> `되는 것과 안 되는 것 사이에서 자기가 한 일이 똑같았다.`
> `그러면 이건 자기가 하는 게 아니었다.`
> `거기까지 생각하고 멈췄다. 그다음을 어떻게 생각해야 하는지 몰랐다.`

She knows what it means: **`열 번에 세 번이면 나가서는 못 쓴다. 그건 세 본 적이 없어도
알았다.`** Outside it gets written down as four syllables — **반응 확인** — and EP131's
form comes back around: `이름 쓰는 칸은 있는데 왜 그렇게 했는지 쓰는 칸은 없었다` →
**`칸이 있는 것만 남는다.`** Closing: **`팔은 올라간다. / 그다음에 뭘 하는지는 아직 안
배웠다.`**

### ★★★★★★ The author-side rule is now fixed (page-level 0)

User decision, 2026-08-25. The **old method — 「내가 의도하면 기체가 움직인다」, two steps —
no longer works**, because she has already learned the piloting method is a fiction. What
works is **cutting the middle step: feeling 「내가 움직인다」.** And because it has to be
*felt*, **the harder she consciously tries, the less it comes.**

**On the page this appears only as placement.** Write what she was doing in that moment;
**never write the causation.** The five that came were all moments she wasn't trying:
because it was the order of things · while listening to something else · distracted by
counting · right after counting got boring · after she gave up looking for the difference.

**★★★ Dana's own verdict is the rule's shadow** — the observation is exact, the conclusion
exactly inverted. **「단순한 조종기술이 아니다」 remains un-reached.** Recovery is scheduled
for **EP140**, where standing in front of something makes the condition true by itself —
**and the causation stays unwritten there too.**

### Craft

**First pass came in at 2,442 chars — 42%, the lowest on record**, below EP133's 56% under
the same alone-in-a-cockpit condition. Four fill rounds. **Level 6's C item worked for the
first time**: copying style-card §2-8·§2-9 verbatim into the lock prevented a repeat of
EP133's full-body-motion violation. `closer` came in at **16.0** — lowest band — even though
「모른다」 is the chapter's theme word, because verdicts were withheld and only observation
written. Two verbatim-repeat hits were caught and varied.

To make the first attempt read as unconsidered, **three blocks of self-aware narration were
moved from scene 3 (before the first attempt) to scene 4 (after the second).** The place
where awareness attaches is the place where it stops working.

Next: **EP136** (10/17 Mon, **Sua**, standard 5,500) — **the answer to the EP109 promise.**
Thirty-nine days.

---

## EP136 approved (2026-08-26) — the answer comes, and it's half

**EP136 「해 볼게」** (`142_EP136_승인완료`, 5,206 chars, 10/17 Mon, **Sua POV**, combat 0)
— **6-5 「조건」 8/10 · S14 16/24.**

Thirty-nine days after EP109's 「…해 볼게」, the mother comes back. Grandfather gets out
**this week**; discharge is **Thursday morning** — a date neither the aide nor the attending
physician has yet. And then: **「언니는 아직이야.」**

> `해 볼게는 안 하고 있어도 할 수 있는 말이다.`
> **`아직이라고 하려면 하고 있어야 한다.`**
> **`그리고 아직은 언젠가 끝난다. (…) 해 볼게에는 끝이 없었다.`**

**Half an answer, and the half is better than last time.** Sua updates her own EP109 verdict.

She nearly stops counting and doesn't: **`그만두면 안 온 게 아니라 없는 게 된다.`** She
can't say the two syllables when the woman arrives and says them at the door instead —
**`쉬워졌던 게 다시 어려워질 수 있다는 걸 몰랐다`** — and the narration's naming shifts
`그 사람` → `엄마` there, then back to `이 사람` in the last scene. Closer to further.

Then the count that matters: the woman knows **four things** the three people who come here
every day don't, and her name is on the visitor list. **`이 사람은 어떻게 알까.`** She
doesn't ask — `물으면 안 온다는 건 안 물으면 온다는 뜻인데, 그러면 안 묻는 게 조건이 된다`.
Closing: forty-seven days since she last saw her sister. **`서른아흐레보다 컸다.`**

### ★★★★★★ Two user catches

**① 「…말했어」 was fabricated.** What Hyeonseo actually relayed to Dana in EP109 was Sua's
**condition** (eating, legs) — EP131 confirms the boundary. Nothing licensed "I told her you
miss her." **Flipping it to 「…아니」 improved the chapter**: the woman meets them one at a
time and carries news in one direction only. Sua doesn't ask why — `물어 봐야 안 갔다는 게
갔던 걸로 바뀌지 않는다` — and **asks for something instead**: 「말해 주세요」 ·
**「언니한테 괜찮냐고는 묻지 마세요. 괜찮냐고 물으면 괜찮다고 할 거예요」** ·
**「밥 먹었냐고 물어보세요. 그건 그냥 대답해요」** → **「…그럴게.」**

**② The voice read as aggressive.** Counting them: **ten questions from Sua, four
consecutive in scene 3.** She had become an interrogator. Cut to seven, the run broken
(Hyeonseo volunteers what Sua had been asking; Sua answers 「…네」), and **scene 4 converted
from interrogation to request.** Sua's signature is *knows first, feels later* — she learns
by listening and matching, not by asking. **New §8-2 rule candidate: a run of question marks
changes a character's register.**

### ★★★★★★ S14 v1.5 — one chapter added

> **「부탁을 회수하려면 현서가 단아를 만나야겠군」** (user, 2026-08-26)

**EP137 「부탁」** (10/19 Wed, **Dana**, important 5,800). 23 → **24 chapters**; 6-5 becomes
EP129~138, 6-6 renumbers to **EP139~144**; Dana POV 8 → **9**.

**The heart of it:** Sua called her 「엄마」 in EP109 and again in EP136. **Dana has met her
twice and never once called her that — across more than 130 chapters.** That's the chapter.
The request arrives **as placement only**: Hyeonseo asks about food, **and Dana doesn't know
why. Only the reader does.**

Next: **EP137** (10/19 Wed, **Dana**, important 5,800) — **v1.5 new.**

---

## EP137 approved (2026-08-26) — the request lands, and Dana doesn't know it did

**EP137 「밥 먹었어」** (`143_EP137_승인완료`, 5,557 chars, 10/19 Wed, **Dana POV**, combat 0)
— **6-5 「조건」 9/10 · S14 17/24.** The v1.5 insertion.

Hyeonseo comes to the facility forty-one days after EP109, and **for the first time she is
the one asking**: food, sleep, glasses. `이 사람이 뭘 물은 건 처음이었다` ·
**`묻는 쪽하고 대답하는 쪽이 바뀌었다`**. Dana notices the shape of it without the reason:

> **`이 사람은 괜찮으냐고 안 물었다.`** (…) **`대답할 수 있는 것만 물었다.`**
> `그런데 안경까지 갔다. 안경은 여기 사람들도 안 묻는 거였다.`
> 왜 그러는지는 모르겠다. / **`모르는데 편했다.`**

**Sua's request from EP136 is never stated on the page.** Same technique as EP135: write what
was happening, never the causation. **Neither sister knows this line exists. Only the reader.**

**Second payoff: EP108's 「말은 해 뒀어」.** Forty-one days later — **「내일 병원에 가.」**

> **`빈 칸에 오늘 뭐가 들어갔다.`** / **`안 믿었는데 됐다.`**
> **`믿었으면 기다렸을 것이고 기다렸으면 한 달이 길었을 것이다. 안 믿어서 안 기다렸고 안 기다려서 안 길었다.`**

**Access count, per the user's 「약간 늘리는걸로」:** Fri 3 · Mon 4 · **Tue 2** · Wed 5.
Deliberately not monotone — **`넷을 다 보면 올라간다. 두 개씩 잘라 보면 안 올라간다`**, and
the gain is useless: `늘어난 이유를 알면 그걸 더 하면 되는데, 모르니까 할 게 없다`.

**Closing.** EP108 said `나올 뻔한 적도 없었다`. This time it reaches her throat and stops —
and **the reason has changed**: `뭐라고 부르는지는 아는데 부르면 그게 정해진 게 된다` ·
**`부르고 나면 그 사람은 그게 된다. 안 부르면 아직 아무것도 아니다`** ·
**`부른 말은 오늘도 없었다.`**

### ★★★★★★ User catch: date collision

**「퇴원은 내일인데 병원을 모레 가는건 시간이 안 맞는데」** — correct. Sua discharges 10/20;
a 10/21 visit puts Dana at an empty room, **and it collided with S14 v1.5's own EP138
(10/20 Thu, all three in one place)**. The error originated in the brief, not the draft — §4-2
had scheduled it as 「모레」. All instances moved to 「내일」, which added material: the visit
now lands on discharge day (`나오는 걸 보러 가는 건지 나오기 전에 가는 건지는 안 나왔다`) and
collides with the access schedule (`하루를 빼도 되는 모양이었다. (…) 빼기로 한 건 저쪽이었다`).

**A brief-stage date must be checked against the season outline's own calendar, not just the
previous chapter's.**

### Edits and two EP108 recoveries

The 「키 언제 쟀냐」 edit pointed at real canon — **EP108 has Hyeonseo asking Dana's height,
and Dana not answering** (`단아는 대답할까 하다가 안 했다`). That became the sharper contrast:
`그리고 그때는 대답을 안 했다. 대답할까 하다가 말았다.` Checking that passage surfaced a
**second Hyeonseo tic that had been missing from the chapter — she taps the table twice**
(톡, 톡) before saying something. Added to scene 3.

### Craft

**First pass 3,202 (55%), with scenes 2–4 at 45–48% despite being dialogue scenes.** The cause
is the **one-sided** case in §8-2: Dana speaks very little (EP108 precedent: about ten lines),
so exchanged-dialogue beat math doesn't apply. **Budget one-sided dialogue like narration.**

The fill pass then pushed **`deictic` to 29.6, over the 29.4 band**, and the checker named it
exactly: `an expansion pass likely cloned frames`. Eight 「그런데/그리고/그러면」 openers were
rewritten → 21.0. **Re-read sentence openers after every fill pass.** One 계단 token also slipped
in — against a rule this chapter's own brief had written down.

Next: **EP138** (10/20 Thu, **Sua**, peak 6,000) — **6-5 closes.**

---

## EP138 approved (2026-08-26) — 6-5 「조건」 closes

**EP138 「같이 못 간다」** (`144_EP138_승인완료`, 5,307 chars, 10/20 Thu, **Sua POV**, combat 0)
— **★ 6-5 「조건」 close, 10/10 · S14 18/24.**

**What the conditions gave and what they didn't arrive on the same day.** Sua discharges,
Youngjin walks in released, **the guardian line gets filled** — his name goes in twice, once as
guardian and once as the person who brings her to outpatient. Then, at the entrance, two cars.

> **`오늘 채워진 게 둘이다. 오늘 만난 게 둘이다. 오늘 같이 가는 게 하나다.`**
> **`같이 살면 같이 가는 거고, 같이 가면 같이 사는 거였다. 여름에는 그게 하나였다.`**

### ★★★★★★ The glasses — a two-handed job done by three people

User direction: **「안경은 이번에 고쳐주자 / 도구 대신 단아한테 안경 잡으라고 해서」**. EP132 had
established both that Youngjin knows how to do it and why he can't: `그때는 작업대가 있었다.
(…) **받침이 왼손 노릇을 했다**` · `두 손이면 오 초면 되는 일이었다`. The hospital has no
workbench. So the brace becomes a person:

> 「잡아라.」 / 「알 쪽. 두 손으로.」 → **`단아 손이 받침이 됐다`**
> **「…조금 더.」** / 「어느 쪽.」 / **「오른쪽이요. 아직 낮아요.」** ← Sua supplies the angle
> 「어떠냐.」 / 「…됐어.」 / **「…고마워.」**

**No summarizing line.** What Sua notices instead is the thank-you: `언니는 할아버지한테
고맙다고 하는 애가 아니었다. (…) 그 집에서는 그런 걸 안 했다.`

### 「일찍 일어났어?」

User direction: **「떨어지기 직전까지 수아가 단아 일어나는 시간을 체크하고있었으니」** — and the
canon was there: EP100's **`수아가 시계를 보고 종이에 적었다. 31, 8시 50분.`** · `그 여섯 줄이
지금 마루 상 위에 적혀 있다`. Fifty days later the first question resumes that log. The answer
is **「여섯 시 반.」**, and Sua files it without a verdict — `그 사이에 뭐가 있었는지를 수아는
모른다`. **Note what kind of question it is: not 「괜찮냐」 but one that can be answered — the
exact method Sua asked Hyeonseo for in EP136, with no line on the page connecting the two.**

Closing: **`적을 게 하나 생겼는데, 적을 사람이 옆에 없었다.`**

### User catch: speech level

**단아 → 영진 is 반말** (standing canon) and the draft had her in 존댓말 through the whole
glasses scene. Corrected to 「…어디를.」 · 「안 움직여.」 · 「…됐어.」 · 「…고마워.」, then all
honorific-ending lines were audited — **all four remaining belong to Sua.** `check_voice` 10 → 7.

Also corrected: 「여덟 살 때부터 알았고」 was invented (the arm predates Sua's birth by decades)
→ 「원래부터」; the crooked glasses date from EP123, not summer. And the farewell to the aide
changed from a wave to **`수아는 고개를 숙였다. 지금 몸으로는 허리를 숙여 인사하는 것도 불편하다는
걸 이제야 알았다.`** — the injury enters without any sealed vocabulary, and she learns it on day
thirty-one because there was never anyone to bow to in a hospital room.

### ★★★★★★ 6-5 「조건」 in full (EP129–138, ten chapters, 10/3–10/20)

**Four conditions get attached, get honored, and still don't move.**

| | |
| --- | --- |
| ① treatment continues | EP130 settled → **EP134 honored on paper, nowhere to go** → **EP138 somewhere to go** |
| ② family contact | EP131 Myeongjun · EP132 Youngjin visit · **EP138 all three** |
| ③ machine repaired | **still not standing** (10/25) |
| ④ her own consent | **EP135 「오늘도 하시겠습니까」, every morning** |

**What's left is one body — three in ten, then five in ten.** The section's last face is that
they meet and cannot leave together.

### Craft notes

**`check_continuity` caught an intra-chapter duplicate** (「들어와서 침대 옆에 섰다」 twice) —
the checker audits the draft against itself, not only against the approved corpus. **Short-sentence
ratio broke the band at 72%** and came down to 67.9% by lengthening narration beats. And one fill
block landed **before** the interpretive sentence it belonged after, cutting the beat in half —
**insert fills after a complete meaning unit, not merely between paragraphs.**

---

## G0-025 approved (2026-08-26) — Dana's legal status, fixed before 6-6

User: **「단아의 처분을 이제 정해놓고 들어가야할듯」** · **「영진은 불구속 송치되었고 단아는
아직 안끝난 상황이지」**

**G0-020 had already fixed half of this** (촉법소년 at 12; **the charge is deliberately never
settled** — "쓸 칸을 못 찾았다"; 임시조치 위탁 possible). What was missing was the outcome
*after* the EP130 settlement. Now fixed:

**Youngjin — 불구속 송치, not 「불구속 전환」.** Police investigation closed and the file went to
the prosecutor; **he is out of custody, not out of the case.** Charging decision and trial remain.
The EP110 「보류」 is what had been holding it. **Corrected retroactively across 12 files** —
EP137/EP138 deltas, SNAP-135~138, S14 v1.4/v1.5, the character ledger.

**Dana — 소년부 송치 완료, 심리 미종결, 임시조치로 아동보호시설 위탁 중.** No disposition, **no
hearing date set.** 소년분류심사원 was avoided (that was a gain from EP130).

### ★★★★★★ Why a guardian appearing doesn't get her out — three layers

1. **The court releases an 임시조치, not a guardian.** Those are different procedures.
2. **Absent guardian was one ground, not the only one** — she is a party to the case.
3. **★ That guardian is a man who was just 불구속 송치 on the same case.** A court does not
   readily place the juvenile of a case into the home of that case's defendant.

**So Youngjin getting out is itself part of why Dana can't go.** And EP115 completes:

> 큰애는 걷는다. **만 열두 살이고 사법절차 안에 들어와 있다.**
> 작은애는 아직 못 걷는다. **만 아홉 살이고, 그 나이에는 손댈 조문이 아예 없다.**

**The one who can walk can't go; the one who can't walk goes.** That is the root of EP138.

### ★★★★★ Riding and disposition — structural only, no bargain

**Myeongjun never proposed anything.** But: he asks every morning and the answer is **written
down** (EP135), it rises into the report as **「반응 확인」**, and a record of cooperation reads as
favorable in a juvenile protection case. **Nobody tells Dana this.**

Her EP135 read — **`적는 데가 있는 것 같았다`** · `안 하겠다고 할 수 있는 자리이기는 한 모양이었다`
— was right, and half-right: she didn't get to **"and if I decline, nothing gets written."**

**★★★ Nobody did anything wrong and the child still can't leave.** That's the register of this
line. Condition ④ institutionalized the right to refuse; the institution simply doesn't record
refusals.

**Page rules:** 「송치」·「기소」·「검찰」·「불구속」 = zero. 「촉법소년」·「보호처분」·「임시조치」·「소년부」
= adult dialogue only. **Why she can't go = zero** (already handled that way in EP138). Children
see it as 「나왔다」, 「또 불려 간다」, 「아직」.

**★★★ EP141 (앞에 선다) must be a place with no relation to the disposition.** If she calculates
before stepping forward, this line breaks.

### ★★★★★★ §4-A Disclosure allocation (same-day user correction)

> **「너무 숨겨두면 읽는 입장에서 이상하게 생각되니 좀 흘려두기는 해야할듯」**

**"No explanation" is not "no information."** Sealed all the way down, the reader stalls at
"why can't she go?" The working principle is the one this series already uses (EP131 「명단」,
EP134 「직계」): **the child repeats an adult sentence she doesn't understand, and the meaning
completes on the reader's side.**

| **Leak** | **Still withhold** |
| --- | --- |
| something has to be **decided** | who decides |
| there **is** a place that decides | 「법원」·「소년부」 as words |
| it **hasn't** been decided | date, charge, statute |
| **the adult knows and won't say** | riding ↔ disposition |
| Youngjin isn't finished either | 「송치」·「기소」·「불구속」 |

**EP138 was retroactively extended (v1.1)** with four beats at the parting:

> 「…언제 와?」 / **「정해지면 온대.」**
> **`정해지면이라는 건 아직 안 정해졌다는 뜻이다. 정할 데가 어딘가 있고 거기서 아직 안 정한 거다.`**
> **`누가 정하는지는 언니도 모르는 것 같았다. (…) 아는 사람은 누가 정한다고 말한다.`**
> 할아버지는 그 말에 아무것도 안 보탰다.
> **`아까 병실에서는 안 묻는 쪽이었는데 지금은 말 안 하는 쪽이었다.`**

**Three layers stand at once:** ① a procedure exists ② **both children are outside it**
③ **★ the adult is inside it and is choosing silence.** ③ is what carries it — the reader
lands on "there's something he can't say," and no statute was ever named. It reuses the
「해 볼게」/「아직」 move (EP109·136), so it reads as the sisters' grammar rather than exposition.

5,307 → 5,474 chars, all five checks re-passed. **Two intra-chapter verbatim duplicates appeared
during the insertion and both were varied** — the checker caught each one.

**Remaining schedule:** one beat in EP140~141 (Youngjin **「또 불려 간다」**), then the hearing
date lands early in S15 as the new clock.

---

---

## EP139 replanned (2026-08-26) — the premise was wrong, and G0-026

**User:** 「처음부터 그렇게 예상하고 계획하기는 힘들것임 매번 다른 특성을 가진 적이 나오는건
경험해봤고 예상도 힘드니까」 · **「피난구역에 겹치는 포격은 현장판단」**

The v0.1 brief had Lucy computing a herding fire pattern the day before and getting it approved
— which would mean **she fired knowing**, and that destroys EP142's 「왜 막았습니까」. Replaced:

| | |
| --- | --- |
| planning | **role split only — Titan forward, Sentinel rear** |
| evacuation zone | **follows precedent**, not a fresh calculation |
| new | **temporary hangar for both units, completed** |
| new | **★ Lucy and Dana meet once before the operation** |
| combat | Titan can't move → Lucy covers alone → **superiority and irritation** |
| **the fire that overlaps the zone** | **★★★ a field judgment** |

**This makes Lucy someone who did her best in the moment**, and makes what Dana blocks **a
moment rather than a plan.**

### The meeting is now the chapter's heart

It's their **second** encounter — Lucy visited the facility in EP116·117, and EP131 records it
from Dana's side: **`전에 온 언니는 잔뜩 물었다`**. She asks a lot again, but different things:
call sign, braking distance, top walking speed, arm reach. **Dana can't answer. She was never
taught.** Then the form question arrives — **「가동 상태 이상 없습니까」** — and Dana says 「네」.

**Same lineage as EP135's 「오늘도 하시겠습니까」: the form decides the answer.** Five-in-ten never
gets said, because adults are present, procedure is moving, and the question is yes/no.

**Lucy writes it down herself: 「가동 가능」.** Four syllables become the whole of the other unit's
condition — the EP135 「반응 확인」 move, this time **from the side doing the writing.** Her
assessment is accurate (untrained, doesn't know the specs, **has combat experience**), and it
being accurate is what makes it dangerous.

## G0-026 approved — Cheonghae naval pier, hangar site, XLG-5 resupply

**User:** 「격납고 위치는 카버 함 정박지와 가까워야하니 군항 위치를 이참에 정해놓고 그곳 부지로」 ·
**「미사일은 126에서 모두 소진했으니 이번에 보충」**

**The pier was already on the page — it just had no name.** EP121: **`부두 초소에서 두 번
멈췄다. 첫 번째는 미측 초소였고 두 번째는 한국 측이었다`** · **`부두에서 시가지까지 26분`** ·
road widening, due November. The sweep also shows 항구 (fishing harbor: crates, breakwater) and
부두 (this) were **already distinct in the text**. Fixed as: south-coast joint-use pier, double
checkpoint, 26 minutes to town, **CARVER berthed there**. **The word 「군항」 stays off the page** —
it remains 「부두」.

**The temporary hangar sits in that yard, near the quay**, because **XLG-5 resupply comes off the
ship.** The Titan was moved there from the tidal flat during the 10/21–25 gap; on the page that's
just "it came in yesterday."

**XLG-5 history:** EP124 two rounds → **EP126 `발사관이 비었다. 잔여 0`** → **empty for nearly two
months** → **EP139 resupply to a full four** (VLS 2×2). **More rounds doesn't change the tether**,
so 「견제로는 안 끝납니다」 still holds. This also retro-fits EP129: she wasn't asking because she
had no weapon — **she'd been holding the line without one, and a café conversation was the
trigger.** That causation is never stated.

---

Next: **EP139** (10/26 Wed, **Lucy Carver**, important 5,800) — **6-6 opens.**

---

## EP139 approved (2026-08-26) — what the form cannot hold

**EP139 「가동 가능」** (`145_EP139_승인완료`, 5,428 chars, 10/26 Wed, **Lucy POV**, combat 0)
— **6-6 「앞에 선다」 opens, 1/6 · S14 19/24.**

Two units under one roof for the first time, in the temporary hangar at the naval pier. XLG-5
resupplied to four after twenty-six days at zero — and **`잔여가 0인 채로 며칠을 보냈는지 적는
칸도 없다`**. The document designation finally changed, and the reason matters:

> **`이름을 알게 된 것으로는 안 바뀌었다.`** (…) **`같이 나가게 되니까 바뀌었다.`**
> **`부를 일이 생겨야 이름이 문서에 오른다.`**

Then Lucy meets Dana for the second time and runs the spec questions. Call sign: none. Anchor
purpose: she can answer. **Range, cruise speed, braking distance, arm reach: four blanks.**
**She knows how to use it and doesn't know the numbers.** Lucy's summary: `제일 쉬운 것을 안 한
사람이 제일 어려운 것을 하고 있었다`.

And the last line of the form:

> 「가동 상태 이상 없습니까.」 / **「…그런데 있잖아요.」**
> 「그게, 제가 요즘…」 / **「그건 서식에 없습니다. 예 아니오로 답하십시오.」** / **「…예.」**

**Dana didn't choose silence — she started to speak and procedure cut it off.** Lucy followed the
form. **Nobody did anything wrong**, and Lucy writes **「가동 가능」** into the status field
herself, because the other unit's maintenance chain is different so the observer fills it in, and
today the observer was her. **That is the cause of EP142.**

### User catches (four)

**Knife.** 「실타격 수단 없이」 was wrong — EP126 has **`근접전용 나이프의 날이 허공을 갈랐다`** ·
`나이프는 쓴 것으로 치지 않았다. 뽑았고 두 번 휘둘렀는데 닿은 데가 없다`. Rewritten to **`남은
것은 나이프였다. 나이프는 붙어야 쓴다`** — three weapons, not two.

**EP116 misread.** 「그때는 앉아서 물었고 상대는 거의 대답하지 않았다」 — the canon says both were
standing and the answers came. Replaced, and the edit put something better there: **`조종 방식이
이상하다는 것도 그때 알았다`**.

**Unit names.** Six 「검은 것/검은 쪽/저것」 → 블랙 타이탄; 「흑색기/백색기」 → full designations.
「화이트 센티널」 appears twice, both inside dialogue or the form — **the card rule (never the
subject of a narration sentence) holds**, and the contrast sharpens.

**「아이언 앵커」 typo**, plus the note that **Dana named it** (EP061·062, where the household has
already shortened it to 「앵커」). Planted by erasure: **`명칭 칸에 그대로 옮겼다. 제식명인지
아닌지는 안 물었다. 서식에 그 칸이 없다.`**

### Craft — a correction has to be measured, not just aimed

Lucy-POV card §0-B was copied into the Level 6 lock, and the draft still came out at **28.4%
viewpoint-subject density against an 8–16% band** — EP121·122·124 had been **0.0%**. **Aimed
right, overshot.** Fixed to 16.0% by expanding narration beats rather than deleting subjects.
`deictic` also climbed to 29.3 during fills (same pattern as EP137·138) → six openers rewritten →
19.5.

Next: **EP140** (10/27 Thu, **Dana**) — she goes out and **can't move.**

---

## 6-6 combat design approved (2026-08-26) — KJ-05 합성 6호

User replaced my first draft outright: **「단아가 막아서는 바람에 적이 도주하는 전개로 이어지니까
빠른 놈이어야함」** · **「등각류형이 있었는데 얘는 빠른것 말고는 없어서 졌거든」** · **「등각류와
성게의 합성」**. Canon backed it twice over — the summer ladder reads **투구게형(mass) → 따개비형
→ 등각류형(speed — anchor debut) → 딱총새우형**, so my 투구게 was a repeat *and* the isopod is
**the creature the anchor debuted against**. 「이전처럼 앵커를 걸면 된다」 has EP059~061 behind it.

**KJ-05 = 등각류 + 성게** (both recombinations of existing creatures, same as KJ-03/04). Low,
long, many legs, **spines massed forward — they actually punch through**, so nothing can meet it
head-on. Light, for speed. **Direct hits don't land; near-misses stagger it**, and it veers away
from the blast — **but it can't turn tight.** That's the only opening, and **the herding comes out
of the creature, not out of the plot.**

**Herding is part of the kill, not an alternative:** shells build a path → **the front unit waits
at the end of it** → anchor → it trips on its own speed → belly up → XLG-5. **Break any one link
and the whole procedure fails.** The failure has an exact shape: **길은 만들었는데 길 끝에 아무도
없었다.**

**The 방재벽** (EP133 canon — the tidal-flat site is *outside* it, the city inside; EP004 gives it
gates, ledges, reinforced sections Dana once climbed) does three things at once when the creature
goes over: **it slows down** (the only chance at a direct hit), **it gains height for the first
time**, and **where it falls is the low ground.** It breaks several legs going over, gets up, and
leaves — slowed — which is what's in the city in EP143.

**And the evacuation-zone overlap is the finishing shot, not the herding pattern.** A pattern can
be walked around a zone; **a downed target's position can't be chosen**, and **if it stands up you
don't get another.** 「그 한 발만 참으면」 does not apply.

Sheet at `07_시각바이블/괴수시트/KJ-05_synth_06/`, design at
`04_가을편_기획/Black_Titan_6-6_전투설계_KJ-05_v1.1_APPROVED.md` (**v1.1 = sea escape**).

---

## EP140 approved (2026-08-26) — 「길 끝」

**EP140 「길 끝」** (`146_EP140_승인완료`, 4,992 chars, 10/27 Thu, **Dana POV**, **combat 1**)
— **6-6 2/6 · S14 20/24.** First real engagement since 8/31 — **fifty-seven days.**

**The call sign lands first.** 「블랙」 — she knows the word, it's half her machine's name, **and
she can't tell whether it's calling the machine or her.** Grandfather always said 단아야 over
comms and never addressed the machine. **`기체하고 자기가 갈려 있었다. 여름에는 안 갈려 있었다.`**
· `여기 앉은 사람이 누구든 블랙이다. 이름을 안 부르는 게 아니라 이름이 필요 없는 거였다.`

Then the vocabulary: 이격, 축선. **Lucy rephrases** — no irritation, no repeat question — and
**that's what stings**: `못 알아들은 게 확인된 거였다` · **`그게 쉬운 말이라서 그런 줄 알았는데
아니었다. 아는 사람끼리라서 그런 거였다.`**

**Lucy is still generous here.** She asks whether Dana remembers how the last fast one was handled,
confirms the answer, and names the rock to anchor to. **The plan has nothing wrong with it.**

**Then the move doesn't come — three times.** `여기는 없다` — unlike the training range there's no
time to retry. **`…안 가요.`** / **「무엇이 안 갑니까.」** and she has no answer: `저번에는
말하려는데 못 하게 했다. 이번에는 말해도 되는데 할 말이 없었다` — the reverse face of EP139.

**The anchor works halfway.** Release is a control-stick switch and it fires: `손으로 하는 건
된다`. Aiming needs the arm, and **the left arm stops at chest height.** Each retry gives
**`움찔거리는 느낌은 있지만 아무 일도 안 일어난다`** — the signal went, something moved, nothing
happened. **`다 안 되는 것보다 이게 더 이상했다.`**

So she watches the herding **on screen**: `포탄이 벽이고 그 사이가 길이다` · the creature thinks
it's choosing · **`단아는 그게 좀 무서웠다. 무서운 데가 저것이 아니라 흰 쪽이었다.`** And the
line the chapter is built for:

> **`밖에서 보면 저건 안 하는 걸로 보일 것이다.`**
> **`안 하는 것하고 못 하는 것을 밖에서 가를 방법이 없다. 안에 앉은 사람만 안다.`**

**EP139's 「가동 가능」 starts paying here.** Closing: `거기까지 해 줬는데 못 갔다.` · **`못 갔다는
걸 말할 데가 아까 있었고, 그때 말을 못 했다.`**

### Canon corrections this chapter forced

**Speech level.** `단아 → 루시 | 반말(또래로 인식)` in the card — **but EP139's page is already
all 해요체**, and the user confirms she reads Lucy as older. Card §5 updated; same failure mode as
EP136's 「수아 → 현서 미정」. Also re-pinned: **「도단아」, not 「도단아 씨」.**

**Anchor location.** EP139 had fixed it as **좌완 하박** and the draft put it on the back as a
winch. Corrected — and the fix improves the scene: **push works, lift doesn't, in the same arm.**

**Observation seat.** 「화면 보면서 아무것도 안 한 적은 없었다」 was wrong; EP101·102 have her
watching Sua from one. **`하지만 해야 할 때 아무것도 하지 못하는 건 달랐다.`**

### Craft

**First pass 2,818 (49%)** — combat chapters run short; four fill rounds. Narration beats lengthened
until **short-sentence ratio hit 49.8%**, unusually low for combat. And **`check_continuity` flagged
a deliberate bookend** (「벽 안쪽은 여기서 안 보인다」 in scenes 2 and 6) as an intra-chapter
duplicate — **intentional repetition is still caught; one side has to be varied.**

Next: **EP141** (10/27 Thu, **Dana**, **season peak**).

---

## EP141 approved (2026-08-26) — 「넘는다」, the season peak

**EP141 「넘는다」** (`147_EP141_승인완료`, 5,158 chars, 10/27 Thu, **Dana POV**, combat 1)
— **★ season peak · 6-6 3/6 · S14 21/24.**

The creature reaches the seawall and **stands up for the first time**, giving up the low profile
that had made it unhittable — and in that moment the naval gun connects. **`빨라서 안 맞던 것이
느려지니까 맞았다. 그게 하필이면 가장 닿지 말았으면 하는 위치, 방재벽 위다.`** And the sharper
line: **`기다렸던 건 사슬이 저것의 발을 잡아채는 순간이고, 그 순간은 단아가 만들지 못한 것이다.`**

It goes over, **four legs break** (Dana counts them by sound), and **neither unit can see inside**
— White calls the observation posts (EP096). **`등이 열렸다`**, and the other side can fire without
seeing; Dana only registers that much (`브이 뭐라고 하는 약자라 이해를 못 했다`).

**Then October comes back.** A facility living room, a television nobody was watching, children
saying four houses were gone. **`애들은 남 얘기하듯 했는데, 남 얘기가 맞으니까 그랬다`** ·
**`구래동에서 온 건 단아뿐이었다`**. Then — on the user's reordering, so the threat lands before
the objects do — **`지금 저 안에서 그게 또 일어난다.` / `저게 터지면 또 집이 무너진다.`** and the
list assembles itself: **대성슈퍼** (twice in the ledger, Children's Day, the wife and husband
booking the same fan separately — EP025 canon), **the bench with one short leg**, the woman who
weighed ice, the alley too narrow for two adults. **`그 선풍기가 없어진다.`** ·
**`간단한 계산이다. 최대 여덟 가족이 집을 잃는다.`**

**And the body goes while the memory is arriving.** No decision on the page:
**`생각을 하는 사이에 갑자기 몸이 움직였다.`** · `걸어왔다기보다는 뛰어들어온 느낌이다.` ·
**하마터면 부딪힐 뻔했다.** G0-025's condition is satisfied by itself, **with the causation never
written.**

「쏘지 마세요.」 · **「확실해요? 저기 노인분들도 많이 살아요.」** → **「제가 넘어갈게요.」** — three
grounds: **the anchor has to be aimed by sight**, **she climbed that wall in spring** (EP004), and
**★ 「그래도 폭발은 안 하니까요.」** — which ties straight back to the four houses, since it was an
explosion that took them. `말하고 보니 그게 이유가 되어 있었다`.

Lucy's answer is exact and unanswerable: **「아까는 못 움직였습니다.」** And Dana knows what she's
offering: **`그러면 내 책임이다. 대성슈퍼와 건물 몇 채를 지키려다가 동네를 다 날릴 수도 있었다.`**
Closing: **`…한 번만요.`** · `해 볼 수 있는 사람이 하는 말이 아니라 못 해 본 사람이 하는 말이었다.`

### ★★★★★★ Beat shortfall — a rule that existed and wasn't followed

**User:** 「비트가 모자랐던것같다 / 애초에 기획 단계에서 한 화에 쓸 재료가 너무 모자랐던가 /
분량 늘린 티가 많이 나서 좀 다듬었음」

First pass **2,733 chars (46%)**, four fill rounds, **44 edits**. §8-2 already says **target ÷ 100 =
required beats** and **a short brief doesn't go to draft** — 6,000 chars needed **60 beats**; the
brief had **34**. Registered as **§8-2 「세지 않으면 비트 표가 없는 것이다」**, with three causes:
writing it as "scene materials" instead of a beat sheet, **not writing the number down**
(`필요 60 / 확보 34`), and — most dangerous — **excusing the shortfall as chapter type.** EP140 was
49%, EP141 46%. **Two in a row is a brief problem, not a genre trait.**

**The edits are the proof:** my fills re-counted information already on the page; the user's edits
put new information in. **「분량 늘린 티」 is not cloned syntax — it's stalled information**, a layer
the older rule (「확장 패스는 문형을 복제하지 않는다」) doesn't catch.

### Canon fixed here

**Comms register** (voice-card §5-A, new): **음슴체 is the default** — HQ, observation posts, and
**Lucy talking to control** (`관측 요청.` · `일어나려 시도 중.`). **Lucy speaks in full polite
sentences only to Dana.** She accommodates twice — **once in register, once in vocabulary**
(EP140's 「말을 바꿔 준다」) — **and Dana doesn't recognize either as accommodation.** She's
embarrassed instead.

Also: **대성슈퍼's fan is canon** (EP025; my draft had invented a refrigerator), and **White
Sentinel's face — a horizontal slit with blue light — enters the page.**

Next: **EP142 「놓쳤다」** (10/27 Thu, **Lucy Carver**) — the shot doesn't happen, the creature gets
up on broken legs and reaches the city. **`왜 막았습니까`는 감정이 아니라 정확한 지적이다** — and it
now cuts deeper, because Dana **said she would do it and then couldn't.**

---

## 6-6 ending revised (2026-08-27) — **the creature escapes to sea**

**User:** 「적은 바다로 도주 / 재등장 예약」

The design had the creature **settling into the city**. It now **passes through the city and reaches
open water**, and **the operation ends in failure.**

### Why the sea closes the chase — canon already supplied the physics

**G0-023: the 8-inch guns, the 20밀리, and XLG-5 are all unusable underwater.** Once it's in the
water there is no way to follow. **「놓쳤다」 stops being a delay and becomes a verdict** — there is
no next attempt. Precedent exists: in **EP124 a creature withdrew on its own.**

### Why it leaves, and why the route runs through the city

**Four legs are broken** — for a creature whose only asset is speed, that's everything. Isopods
live in water; **land was where it was heading, not what it wanted.** It was already **inside the
seawall**, and **it can't climb back out** — it was intact on the way in. So it goes low: **the
sluice gate** (EP004 canon) or the river mouth, **and that route crosses the city.**

**It must be shown failing at the wall once** — grabbing on and sliding off — because that
observation, not inference, is what tells both pilots which way it will go.

**★ So EP143 gets worse:** they lose it, and they lose it **because they were fighting each other.**
The fight ends and the target is simply gone.

### Reserved return

**KJ-05 is alive** — four legs damaged, spines intact, **untrackable**. Registered in the
foreshadow tracker as **`KJ05-STILL-OUT-THERE`** (status `RESERVED`, window S15).
**On the page: no foreshadowing at all.** 「놓쳤다」 and nothing past it — no narrator who knows
what's coming, no "it will heal." **「바다 쪽으로 갔다」 is an observation post's assessment**, not
the narrator's knowledge.

**This is the first creature in the series to survive and be scheduled to return.**

### Documents

`6-6 전투설계 KJ-05 **v1.1**` §7-A · `KJ-05 시트 **v1.1**` §9 · `S14 화별개요 **v1.6**` ·
foreshadow tracker SNAP-141 · EP141 delta/SNAP/verification `next` fields corrected.

---

## EP142 approved (2026-08-27) — the form that won't close

**EP142 「놓쳤다」** (`148_EP142_승인완료`, **6,088 chars**, 10/27 Thu, **Lucy Carver POV**, combat)
ends 6-6's fourth chapter with the operation **failed**: the creature reaches open water off the
dock and **G0-023 makes it unfollowable** — every weapon is unusable underwater.

### ★★★★★★ The spine is EP126 inverted

> **[EP126]** 값이 맞았다. **맞으면 확인할 것이 없다.** (…) **열일곱 개가 다 닫혔다.**

Today: 개체 처리 = **판정 불가**, 사상자 = **빈칸** (`0은 확인한 값이고 저기는 확인한 것이 없다` —
the low ground was outside the zone map), 교전 시간 = **종료 없음**, XLG-5 = **잔여 넷, 받은 것을
그대로 갖고 돌아간다.** Registered as **`LUCY-FORM`** (BURNING).

### Din carries the chapter's second job

Sixteen exchanges, and **four of them are「없다」**. Twice it's **`해당 기체 자료 없음`** — Lucy only
has what she asked for on the form yesterday, and she cut the sentence that began `그런데 있잖아요`
(EP139). So when she concludes **`할 수 있는데 안 했다`**, **Din doesn't back it** — and the narrator
never corrects her. That's how a wrong conclusion stands on the page with zero authorial comment.

### Vision, and what it forces

The user's constraint — **동조 상태라 화면을 보는 걸로 인식하지 않는다**, and **EP141 already fixed
that 관측반 gives numbers, not video** — restructured scenes 3 and 4. Lucy sees only what clears the
wall: **the torso, the outstretched left arm, the chain going taut and then slack**, and **spines
rising above the wall twice, the second lower than the first.** Why the chain went slack arrives as
**`…다리 하나 분리.`** Registered as narration card **§3-4** (three layers: 동조 시야 → `봤다`,
표시 정보 → `화면에 떴다`, 관측반 → `들었다`), with **영상 공유 요청 = 0.**

**★ So §3's third reason stops being figurative:** Lucy never once sees that low ground until scene 5,
and by then it's too late.

### ★★★★★★ The edit that fixed a card

> ~~`화가 났다. 화가 나면 말이 정확해진다. 루시는 그것을 알고 있어서…`~~
> **`뭔가가 속에서 올라왔다. (…) 하지만 루시는 그 느낌이 뭔지 모른다.`**

The draft made Lucy someone who **knows her own reaction pattern**. The cause: voice card §1's
「화가 나면 말이 더 정확해진다」 copied straight into POV narration — but **that is what's visible
from outside** (§3-3). New narration card **§2-3B: 감정에 이름을 안 붙인다** — 몸 → 빈도
(`처음은 아닐 것이다`) → **`뭔지 모른다`, and it ends there.** Voice card §1 now carries the caveat.
**Third time the page has outrun a card.**

### The beat sheet worked

|  | EP140 | EP141 | **EP142** |
| --- | --- | --- | --- |
| required / secured | — | 60 / **34** | 58 / **70** |
| first pass | 49% | 46% | **63%** |
| fill rounds | — | four | **two** |

**EP141's diagnosis came back as a number.** Both expansions added new information — the three
morning attempts, Din's grounds, the low ground itself, the form's fields, and **`시간은 지켰다`**
(28 seconds of 30): Dana did everything asked, on time, **and none of it worked.**

Also fixed here: **「사슬」 is the canon word** for the anchor line (not 「줄」), the seawall is
**slightly above White Sentinel's eye level**, and the escape point is the **dock** — the same
ground as EP144's hangar.

Next: **EP143 「도시 한복판」** (both POVs) — the creature is **leaving, not settling**; no
artillery inside the wall; **the two machines collide**; Myeongjun orders a halt; and the creature
slips to sea while they fight. **The fight ends and the target is simply gone.**

---

## EP140-142 RETIRED (2026-08-27) — 6-6 compressed to two chapters

**User:** the events are simple, the chapter count was inflated, **and the approved chapters carry
real padding.** 「진행이 답답해서 안되겠다 / 적은 사건으로 늘여쓰니 비트를 늘려도 종종걸음같음.」

**Three approved chapters, 16,238 chars, four events.** EP140 (4,992), EP141 (5,158), EP142 (6,088)
plus the EP143 brief are now under
`90_NONCANON_실험초고/G0-027_폐기_6-6_구판_EP140-143/`. Canon rolls back to **SNAP-139**,
foreshadow tracker SNAP-139, ledger **v2.34**, **139 approved chapters**.

### ★★★★★★ What the compression removes is one whole layer

「포격 저지 후 **기회를 놓치고** 적은 일어나 도주」 — so everything between the block and the
escape goes: **「제가 넘어갈게요」**, 「…한 번만요」, 「30초 드리겠습니다」, the 22-second wall climb,
the anchor shot, **「…다리 하나 분리」**, 「시간은 지켰다」, and the spines cresting the wall twice.

**That round trip — Dana crosses, hooks, and it comes to nothing — ate an entire chapter and
arrived at the same place: 「그래도 놓쳤다」.** After the block she simply loses it.

### The new two

| | POV | span |
| --- | --- | --- |
| **EP140 「길 끝」** | **Dana alone** | 개전 → 포격 저지 · **season peak** |
| **EP141 「놓쳤다」** | **★ both, alternating by scene** | 놓침 → 도주 → **밀침** → 몸싸움 → 중지명령 → 격납고 → **폭로 클리프행어** |

**S14 = EP121~141, 21 chapters.**

### ★★★★★★ The shove replaces the manufactured collision

The retired EP143 brief had to **invent** a reason for two machines to fight (a wall Lucy stepped
on). A shove needs none: **the angle is open only now, an allied unit is in the line, she said move
and it didn't.** Per the user — **「지금 쏴야한다는 판단에서 나온 반사」.** The judgment was real and
it came out through her hands, **so she never regrets it.** And the creature gets up right after,
which makes the shove pointless inside the same motion. **「왜 막았습니까」 moves to after the
grapple** — hands went first.

### The hangar keeps its canon slot

S14 outline §67 already put the **birth revelation at EP141's close, in the hangar, fragment only**,
with 현서's full account held for S15 6-7. Short scene, **멱살잡이 between the two of them (Dana
grabs; Lucy speaks while held)**, **one sentence**, cut there. G0-019: to Lucy the birth truth is
**background, not a secret** — **the revelation comes from ignorance, not malice.** The old
「루시가 파편을 던진다」 is dropped: **the fragment is the sentence.**

### Survives the retirement

The four cards earned while writing the old EP142 stay: **딘 §4-A**, **루시 시각 §3-4**,
**감정 명명 금지 §2-3B**, 교신 §5-A — plus **바다 도주 · 재등장 예약**, 「사슬」, and the dock as
the exit point. Retired prose is kept as **material**, not deleted (G0-027 §5 maps each salvaged
passage to its new home).

Documents: **G0-027 v1.0 APPROVED** · **S14 화별개요 v2.0** · **6-6 전투설계 v1.2**.

---

## EP140 approved (2026-08-28) — the compression works

**EP140 「길 끝」** (`146_EP140_승인완료`, **5,595 chars**, 10/27 Thu AM, **Dana POV**, combat) is the
rewrite under G0-027. **Every metric lands inside band** — dialogue 16.7%, past_run 8, short 63.3%,
deictic 8.0, closer 13.3, continuity FAIL 0 **WARN 0**, banned terms 0. First pass **67%** (vs the
retired EP141's 46%), two fill rounds.

### ★★★★★★ Three orders, each asking for less

① go to the rock (judgment + movement) ② coordinates and a clock (movement only) ③ **「바닥에라도
거십시오. 팔만 들면 됩니다.」** — nothing to move at all.

> **`조종간의 버튼을 눌렀다. 앵커를 물고 있던 고정쇠가 풀리는 게 보였다.`**
> **`거기까지는 됐다.`** / **`팔이 안 올라갔다.`** / **`누르는 건 되고 올리는 건 안 됐다. 같은 팔이었다.`**

And Lucy's voice never rises. Then, with nobody ordering anything: **`생각을 하는 사이에 갑자기
몸이 움직였다.`** G0-025's condition satisfies itself with **zero causal narration.**

### ★★★★★★ The edit that reassigned the wound

The draft read EP103's **`허리 정중앙에 구멍`** — machine damage — as Dana's body. It wasn't.
**On August 31 the one who was hurt is 수아**, and the canon was already on the page: the wheelchair
(EP119, 125, 134, 138). Corrected to **`그때 수아는 돌아가는 중이었다`** · **`말이 되지 못한 소리가
들렸었다`** · **`그 후로 수아는 아직 다리가 움직이지 않는다`** — with the lexical seal on
「하반신」/「마비」/「걷지 못한다」 intact.

**That inverts the pain.** **`내 옆구리가 찔린 게 아니다. 하지만 느껴지는 건 진짜다.`** She feels
it, nothing is there, and **she doesn't find it strange** — `이따금 그럴 때가 있었다`. Registered as
voice card **§4-B**, together with EP118's two lines landing here (**「고통을 감수하지 않는 사람은
싸울 수 없습니다」** · **「왜 안전장치 뒤에 있습니까」**) and what follows them: **`그 말을 들어서였을까,
이후 타이탄을 움직일 때면 무언가가 사라진 느낌이 든다.`** **What is gone stays off-page** —
`그 말을 들어서였을까` is the whole causal claim.

### The staging card earned its keep

**Combat staging card v1.0** (new, standing document) went in verbatim: 20mm as **`부우우욱`** with
**빛나는 선**, and「튕긴다」shown rather than stated — **`닿은 자리에서 옆으로 꺾여서 계속
날아갔다`**. Naval guns **recoil**, smoke is sparse, and the casing is **`뭔가가 앞으로 튀어나왔다`**
because Dana doesn't know the word. The creature's turn proves its size: **`올라온 게 벽 같았다 (…)
저것 키보다 높이 섰다가 무너졌다`** → **`그게 저것 크기였다.`** Gulls scatter on each report and
**come back down once it's over** — that's how the page measures silence. October is **짧고 청명한
가을** per the settings doc: sea fog at the start, gone by the wall.

Also fixed here: **launch procedure** (no lift yet — a ladder truck, hatch, seat, harness,
**커버를 젖히고 스위치**), the anchor as **조종간의 버튼 + 고정쇠**, **「루시 언니」** as Dana's
narration term for Lucy, and **수아** as the one who found the fan entry in EP025's ledger.

New threads: **`D-CANT-GO`** (BURNING → EP141), **`D-PAIN-NO-WOUND`**, **`D-SOMETHING-GONE`**.

Next: **EP141 「놓쳤다」** — **both POVs, alternating by scene**, and **S14 closes there**. The angle
shuts, the creature reaches open water, **Lucy shoves** (a judgment that came out through her hands),
they grapple with **no weapons** while houses go under their feet, **Myeongjun invokes the EP131
clause**, and in the hangar Dana grabs her collar and Lucy answers with **one sentence.**

---

## EP141 approved (2026-08-28) — **S14 closes at 21 chapters**

**EP141 「놓쳤다」** (`147_EP141_승인완료`, **5,236 chars**, 10/27 Thu, **both POVs alternating by
scene**, combat) ends 6-6 and the season. All checks pass; continuity **FAIL 0 WARN 0**.

### ★★★★★★ The shove is undone inside the same motion

**`값이 없으면 기다린다. 그게 절차다.`** / **`기다리면 9초가 지나간다.`** / **`지금이다.`** /
**`밀었다.`** — and on Dana's side, **`아까는 뽑으려고 해도 안 나오던 발이었다. (…) 지금은
뽑으려고 하지도 않았는데 나왔다.`** She grabs on the way back. Then the creature stands, the angle
closes, the cell covers come down, **and four missiles stay in the rack.**

Neither of them lets go after there's nothing left to shoot: **`놓을 이유가 생겼는데 아무도 안
놓았다.`** The knife gets a hand on it and stops — **`조건이 맞는데 대상이 아니다`**.

**EP131's clause fires for the first time:** 「양 기체 교전 중지. 즉시.」 / 「근거.」 /
**「협정 제3항. 출동 결정과 중지 명령은 이쪽에서 낸다.」** Lucy catches on the word 교전 —
**`밖에서 보면 그렇게 보인다는 뜻이었다`** — and **Carver's control raises no objection** on an
open channel.

### ★★★★★★ The revelation got a fuse

The user's edit put **「왜 막았습니까.」** in front of it, and Dana answers: **「…그 밑에, 사람이
살아요.」** → **미간이 좁혀지는 것이 보였다** → **「우리는 저들과 같은 인간이 아닌데 왜
그렇게까지 합니까.」** → 「모르셨습니까.」 → **「우리는 저 밖의 괴물들에게서 왔습니다.」**

**Until she hears the answer, Lucy doesn't know why.** So the crack's trigger is now fixed:
**not being contradicted — hearing something she can't parse.**

### Six layers, not one

The draft had one tell (the hand). The edit made it six: **걸음 → 입가 → 멱살 → 입술 → 손 →
손이 풀렸다 다시 들어감**, with the observer negating **「화난 얼굴이 아니다」** twice while finding
one more mismatch each time. **That repetition is the grammar of the crack** — one tell alone reads
as a slip. Registered in narration card **§2-3C**, along with the rule that Lucy grabs **and doesn't
know why**, and that it only happens **around Dana**.

### EP116 settled two things

Its header already says 장소 = **1층 면회실**, **호칭 = 언니**, and **8/31 목격 = 수아의 시야를
화면으로**. So **「루시 언니」 is EP116 canon, not new**, and **Dana watched August 31 on a screen** —
she wasn't the one hurt. Voice card §5 corrected, §4-B given its source.

### ★★★★★★ A new craft finding: beat count isn't enough

Required 60, secured 72 — and the first pass still came in at **41%** (EP140 hit 67% on the same
target). The cause isn't the beat table; it's that **EP141's scenes each carry one short event**
(shove, grab, angle closes, it leaves), and written in clipped sentences the beats all land without
the characters accumulating. **The brief should carry an expected char-count per beat, not just a
count** — beats are not interchangeable units.

### S14 closes

**EP121~141, 21 chapters** (24 → 21 under G0-027). 6-4 (8) · 6-5 (10) · **6-6 (3)**. The operation
ends **failed**: creature alive, untrackable. Season ends on the revelation, mid-sentence.

New threads: **`L-REVELATION`** (BURNING → S15 ch.1), **`L-CRACK`** (BURNING → winter),
**`KJ05-STILL-OUT-THERE`** (SIMMERING).

Next: **S15 opens on Dana's reaction**, right there in the hangar. 현서's full account is **6-7**
(G0-019 layer 3). KJ-05's return is **after S15, timing open, zero foreshadowing on the page.**

---

## EP142 approved (2026-09-04) — S15 opens on a flashback, and the prose gets a de-hedging budget

**EP142** (`148_EP142_승인완료`, **6,530 chars**, **Hyeonseo POV — first time in 141 chapters**, a
**past chapter**) opens S15. It's an inset: the present line (2050/10/27, right after the hangar
reveal) does not move, so the current-state snapshot carries over from SNAP-141 unchanged. What
changes is what the **reader** now knows.

### The backstory, on the page at last

Chasing a **pre-eruption low-frequency signal** (nineteen new post-대수몰 volcanoes share the same
six-hours-out waveform), Hyeonseo goes down and watches the crust split and a **whale-shark-shaped
machine-organism push out from inside** — by eye; the crew only see it on screen. As a marine
bio-engineer she IDs it in two seconds, then can't classify it (metal plating, slit gills, a green
glow where the eye should be). Two years later Morgan finds the **Pacific island** where a
seafloor incubator, buried under a mountain that grew over it across ages, was **uncovered as the
sea rose and the peak eroded** — same material, dormant until water reached it. The five-line
finding: metal-bearing tissue, cultured, **immune to outside force but able to interfere with each
other** (you cut one with another) → **only the same thing can stop the same thing.** Carver
follows to there and no further (`어디까지 만듭니까` — Hyeonseo doesn't answer). The report is
buried because **only the one who saw it by eye could write the last three pages.** Team dissolves,
sample hidden (a bag; heaviest thing in it is the notebook), and in **2036 she climbs the 구래동
hill and knocks at 10 p.m.** — first line planned as `부탁이 있어요`. This answers EP001's
`바위를 쏘는 것 같았다` and grounds why the titans fight with anchor/knife/grapple.

All permanent seals held (엑소포밍/가지/허브/인큐베이터 vocabulary = 0, 1500 as a number = 0,
1차거체/단아/수아/출생 = EP145, 루시/IRONSHORE = EP152, mother's last words = later). New threads:
`HYEONSEO-ORIGIN-BACKSTORY`, `WHALESHARK-COMMANDER` (= the 7-5 command creature's origin),
`CARVER-SHALLOW`, `SAME-MATERIAL-COMBAT`.

### ★ New standing rule: the de-hedging budget

The user named a long-standing feel — **"the sentences keep talking around things and omitting
something, especially demonstratives."** Diagnosed as: '돌려말하기' = the reversal ("A가 아니라
B다") plus meta-cognition commentary having become the **default** sentence shape; '생략' =
demonstratives ('그것/저것/그건') deferring their nouns. Codified in narration-style-card **§2-10
(지시대명사 착지, deictic 실목표 ≤18), §2-11 (추상 종결 착지, closer ≤30), §2-12 (메타 논평 억제),
§2-A (the budget: keep one reversal per scene and the load-bearing observer/theme lines, cut the
rest), §3-8/9 (detection), §4-⑩ (prompt)**. Applied a 17-edit pass to EP142 as the baseline demo:
**deictic 22.5→19.6, closer 39.3→30.7**, all checks still passing, each scene's one keeper reversal
intact. The budget auto-applies from EP143's brief onward.

Also carried the EP141 craft finding forward: **budget char-count per beat, not just a beat count**
— EP142 used 110 chars/beat (Hyeonseo's long past-tense sentences) instead of the flat 100, needed
52 beats, and the역산 held on the first try.

Next: **EP143 「그 뒤」** — present line resumes, Dana/Lucy, right after the hangar reveal.

## EP143 approved (2026-09-23) — the grandfather who didn't deny it

**EP143 「그 뒤」** (`149_EP143_승인완료`, **4,958 chars**, 2050/10/27 Thu night, **Dana/Lucy
alternating**, 6 scenes) resumes the present line. Artifacts: approved text v1.0, delta v1.0,
**SNAP-143**, **foreshadow tracker SNAP-143**, **character ledger v2.38**, Gate-DE report.

### What happens

The reveal lands as a fragment. Dana knows every word and can't parse the sentence; her body locks
first (glasses slide down and her hand won't rise). Lucy logs `판단 오류 한 건` — she assumed Dana
knew — and orders her fingers to open; they don't. **Yeongjin unhooks Lucy's wrist one-handed, says
`가자.`, and says nothing about the reveal.** Dana reads the missing denial as confirmation (he's the
man who cuts wrong things off on the spot). He **stops at the hangar threshold** and lets go — Dana
leaves in the **grey military car with 윤서진** (EP133 canon; G0-025 — a suspect under 불구속 송치
can't take her; no on-page explanation). `고칠 게 있다.` / `내일 보자.` Lucy asks 딘 for her own
hand's grip log (`해당 시각 기록 없습니다` — de-synced), sees **the comm line was open the whole
time**, and **doesn't open the new log line**; she's put on standby, will own the push and not
retract it, and can't fill a reason field for the grab. At the facility: `밥은.` / a carton of milk /
한지영's `그 너머는 나도 잘 몰라` / 다은's `왔어?`. The **「원래 그런 것」 axis** opens (grandfather's
arm, two sisters, no mother — if one wasn't "just how it is", the others might not be). At night
「우리」 is deferred to tomorrow (Sua) and 「저 밖」 becomes the question: **`저 밖에는 어떤 사람들이
있어요.`** The one person to ask is the one who keeps her word (EP108 `또 올게` · EP137) — but asking
means calling her, and calling decides it. **The two syllables stop in her throat again.**

### Corrections made between draft and approval

- **Canon errors: 2 caught by the user + 6 found in review** — Sua's 24 ceiling panels (Sua-POV only,
  Dana can't know), the grandfather's truck (→ grey car/윤서진), counting attributed to Sua (it's
  Dana's own habit, EP137), telling grandfather about facility kids (he was detained from 9/1),
  "never been outside the wall" (she fights there in the titan), a limp for Yeongjin, an invented
  ledger detail, and "put her name on the list" (EP137: she *arranged* it).
- **My own misjudgment, reversed:** I removed `또 올게 / 정해지면 알린다` as "not canon" after
  checking only EP137 — it is EP108 canon (lines 410/416). Restored. **Lesson: when a quoted line
  isn't found, sweep every episode the brief cites before calling it invented.**
- **Naming (user):** Dana's narration calls Lucy **「루시 언니」** (voice-cards-autumn §5) — the brief
  and Level 6 had wrongly locked 「저 언니」, which is why it repeated 12×; both fixed. In Lucy's POV
  her own machine is unnamed (「기체」, card §3-1) and Dana's is **「블랙 타이탄」** (§6), never
  「흰 것/검은 기체」.
- **Length (user):** after de-hedging the honest length was ~4.6k → **band lowered 정점 → 표준**.
  Gaps filled only with objects/actions, never thoughts.

### ★ New standing rule: §2-13 주어·목적어 착지

The user: "subjects and objects are omitted so often it feels vague and floating." v0.2 had
**deictic 7.0** and still floated — demonstrative metrics can't see this. Codified as
narration-style-card **§2-13** (+ §2-A diagnosis, §4-⑪): if a subject/object can't be recovered from
the previous sentence alone, write it; always name the subject at a scene's first sentence, right
after a POV switch, and in paragraphs with two or more people; give 「아까 ~한 것」 its what/where;
unquote cited words that land in subject position (「우리는」 → 「우리라는 말은」). Same-subject action
chains stay elided.

### State housekeeping

- **SNAP-142's Yeongjin block was frozen at EP132** (「청해구치소 · 수아 못 봤다」). Restored in SNAP-143
  from EP138 canon (불구속 송치, home, maintaining the titan at the harbour hangar, met Sua at the
  hospital). Check other character blocks for similar freezes when next touched.
- Tracker: L-REVELATION / L-CRACK / D7-CALLING-HER → 143; new **D-OUTSIDE-QUESTION,
  D-ALWAYS-LIKE-THAT, YJ-NO-DENIAL, L-LOG-UNOPENED**. **L-CRACK's "no 'doesn't know why' narration"
  ban was relaxed** by the Gate-C-approved EP143 brief §5 (up to 「설명할 수 없었다」; naming the cause
  stays sealed until winter).

Next: **EP144** — Hyeonseo comes on her own (the log reaches her · G0-028 §6) · does 「우리」 include
Sua · `내일 데려오세요`. Then EP145 (hear it together · lineage · immune rejection) → EP146 (Sua POV).

## Style rules reorganised (2026-09-23) — locks vs. defaults

The user asked whether the sheer number of prohibitions was making the prose vague. Counted: in the
style/POV/voice cards, ban-shaped clauses outnumber "write this" clauses roughly ten to one, and
EP143 showed the balloon effect (v0.1 26% negated sentences; v0.2 hit deictic 7.0 by dropping
subjects/objects wholesale). Approved fix, now in force:

- **narration-style-card v1.0 §0** — two layers and a priority order: **① canon locks** (seals,
  facts, speech levels/names, body canon, name rights, character signatures — stay as bans)
  **② clarity** (outside sealed spots, beats every style rule; the blurrier a sealed spot, the
  sharper its neighbours) **③ style defaults B1–B9** (who-did-what, body reaction + next action for
  emotion, one seen/felt/done for thought, re-use the noun, close on image/action, positive
  statements, name variation, fill gaps with objects/actions) **④ numeric warning bands only** —
  the deictic ≤18 / closer ≤30 targets are **abolished**.
- POV cards (Lucy v1.7, Sua v1.1, Hyeonseo v1.1): "금지 목록" → **「잠금과 기본값」** tables tagged
  `[잠금]`/`[기본값]`; voice-cards-autumn gets a reading note.
- **Brief template:** a **visible-scene list** (who / does what / where / what's seen) now comes
  before seals and bans; a style-layer field and name-canon field added.
- Also cleared: the spring-era 「외부 밀착 시점 = 검은 거인」 line conflicted with Lucy's card
  (post-EP116 = 「블랙 타이탄」); §0-4 records the override.

## EP144 approved (2026-09-23) — she came before she was called

**EP144 「수아도 같냐고」** (`150_EP144_승인완료`, **4,705 chars**, 2050/10/28 Fri, **Dana single
POV**) — the **first chapter written under narration-style-card v1.0 §0** (locks vs. defaults,
visible-scene list first, no numeric targets) and it passed Gate D with **zero edits** ("훨씬
좋아졌다 / 이대로 가자"). Artifacts: approved text, delta, Gate-DE report, **SNAP-144**, **tracker
SNAP-144**, **ledger v2.39**.

What happens: the grey car doesn't come (`오늘은 차 안 온대. 대기래.` — grandfather's `내일 보자`
goes unkept; no reason on the page). Dana spends the day in the facility's 1층 안쪽 방 for the first
time since the linkups began and writes `저 밖에는 어떤 사람들이 있어요` on the back of a worksheet,
into her pocket. At 7 p.m.: `손님 오셨어.` — **the person she couldn't call is already in the
visiting room, and this time not empty-handed: a printed copy of the hangar log.** 한지영 steps out,
door left open (EP131). `뭐라고 들었어. 정확하게.` → **Dana says the sentence aloud herself** (Lucy's
합니다체 and all) → `…한 글자도 안 틀렸네.` Reading upside down she sees **her own name on line three**
and her own words (`그 밑에 사람이 살아요`). The tap stops at one. `그 말은—` / **`수아도 같아요?`** /
**`…그래.`** / `수아가 나중에 들으면, 수아만 나중이잖아요.` (summer: Sua did the checks while Dana
lay ill) / **`내일 데려오세요.`** / `할아버지한테 말하면 데려와요.` / `…알았어.` Hyeonseo, out of
words, falls back to `밥 먹었어?`; Dana answers truthfully this time (`반 먹었어요. 카레요.`). 한지영
already knows about tomorrow (`알아.`). The worksheet goes under the pillow unread; Dana plans to go
first and move a chair so the wheelchair fits. `토요일. 수아. 그 사람.`

Process note: the first draft came out at **3,038 chars** (beats compressed to ~46 chars each); it
was filled only with objects/actions/dialogue, never thoughts. **Two more frozen SNAP blocks were
restored before drafting** (Sua: hospital → discharged 10/20 and home; Hyeonseo: spring "unknown" →
visits + 「닥터 도」) — three freezes total with Yeongjin. Also fixed: EP143 brief/Level 6 had
「한지영 → 단아 = 존댓말」; canon is 반말.

Tracker: L-REVELATION / D7 / D-OUTSIDE-QUESTION / L-LOG-UNOPENED → 144; new **D-SUA-TOO,
D-NAME-IN-RECORD, OPS-STANDBY**.

Next: **EP145 「같이 듣는다」** (10/29 Sat, Dana·Sua) — flashback cross-cutting, lineage, immune
rejection, what "out there" is. The brief must settle venue (visiting room?), who brings Sua
(Yeongjin is a 불구속 송치 suspect; Hyeonseo), and the wheelchair route.

## S15 outline v1.1 (2026-09-23) — EP145 「문」 inserted

User's idea, approved: **Hyeonseo fetches Sua herself**, which forces her to the 구래동 house and
into **the first father–daughter meeting in nine years** (effectively estranged since she missed her
mother's deathbed; he "opposed and helped" — G0-028 §6/§8). Sua's only registered 직계 is the
grandfather (EP134) and he is her 보호자 (EP138), so the causality holds. **Sua POV** — she has never
seen them together, counts the silences without knowing why; the reader knows from EP142. Payoff:
**「두 손이면 오 초」 (EP132)** — folding the wheelchair into the car takes two hands; his one hand
and hers, wordlessly. **No rapprochement** — the 기일 chapter (now EP152) owns 「부녀가 조금
다가간다」. Seals: 「의절」 word 0, the mother's last words = later, "Yeongjin knows everything" = 0.

**Renumbering: new EP145 = 「문」; old EP145–162 → EP146–163. 6-7 = 6 chapters (EP142–147), S15 =
22 chapters.** New file `04_가을편_기획/Black_Titan_S15_EP142-163_화별개요_v1.1_승인.md` (old v1.0
moved to `_superseded`). EP refs shifted +1 with a header note in G0-028/029/030, the Hyeonseo POV
card, SNAP-144 and tracker SNAP-144 (e.g. Lucy's birth reveal EP152 → **EP153**; full explanation
→ **EP146**). Older approved docs/logs keep old numbers as history.

## EP145 approved (2026-09-23) — 「문」, nine years at the threshold

**EP145 「문」** (`151_EP145_승인완료`, **5,050 chars**, 10/28 night–10/29 Sat morning, **Sua POV**).
Sua hears only the grandfather's side of a night call (`어.` `…몇 시.` `…그래.`); next morning
`…네 엄마가 온다.` — the first time she has heard him say 엄마. At 10, a double knock at the house
door (shutter still down); `아버지.` — no answer, **eight** counted seconds, neither crosses the
threshold; Hyeonseo looks down at the ramp and bricks (she can tell who made it) and once toward the
workbench side (the basement, unexplained). `…데리고 가라.` — Sua reads it as the way out for her,
not the way in for her mother. The wheelchair won't fold one-handed; Hyeonseo takes the other side:
**five**. He stays at the door, raises one hand. In the car: seven words passed between them all
day, `아버지` once; `밥은 반 먹었대` (secondhand now). Visiting room: **a chair pushed to the wall,
Dana beside it — `언니.`**

**User corrections → new canon:** (1) the family table was always a **low floor table** — so
Yeongjin **built a wheelchair-height table** on 10/22 from shop plywood and four battens (the floor
table is folded against the wall; the six-line paper moved to the new table's edge); the doorway
**plank ramp on two bricks** dates from 10/21. Both registered in **LOC-05**. (2) **One-handed
people can do buttons, not shoelace knots** — the grandfather buttons Sua's coat; Sua ties her laces.
Memory file rewritten with the rule: only actions needing two points held *simultaneously* are
impossible (knots, folding the wheelchair, folding arms); with a ledge/brace/body to anchor one
side, it's doable.

SNAP-145: Yeongjin's `hyunseo` relation was still frozen at 「영구 봉인 · 지면 0」 — now the EP145
meeting. Tracker: new **YJ-HS-DOOR** (→ EP152 기일, where they may draw slightly closer),
**HS-GLANCE-WORKBENCH** (→ EP146), **SUA-SEVENTH-LINE** (`6시 반`, undated → EP147),
**SUA-TWO-UNKNOWNS**.

Next: **EP146 「같이 듣는다」** — the visiting room, both sisters, flashback cross-cutting, lineage,
immune rejection, what "out there" is, the basement, why she left.

## EP146 approved (2026-09-23) — 「같이 듣는다」, the 6-7 peak

**EP146** (`152_EP146_승인완료`, **5,694 chars**, 10/29 Sat, **Dana/Sua alternating**). Hyeonseo tells
both daughters, one fragment at a time, each fragment calling up a memory from their lived time:
out there people do live (신서울, inland) — 「괴물」 meant the mud creatures, and 「저 밖」 is the
seabed they came from; the 대수몰 was their doing and they are turning inhabited land into sea;
cannons don't work, only their own kind can hurt them; their cells grow into whatever you grow
them into — she brought some back and **cultured the same thing, to stop them**, under 「그 집」;
it began thinking for itself and wouldn't obey; she had built an **incineration device** into it
and burned it; the **nerve cells** survived; idea → hypothesis (combine with **her egg → a
fertilized egg**; `난자가 뭔지는 배웠니?` / `…학교에서요.`) → animals first (the hamster **호두**,
there from Dana's first memory) → **her own body, without certainty, because there was no other
way** → **`그렇게 단아를 낳았어. 내 몸으로. 내 딸이야.`** → seeing the fetus grow, the second
culture → **`그 검은 거하고, 너. 너도 내가 낳았어.`** → hospital: `가면 알게 되니까` → **`왜 떠났어요.`
→ a US intelligence agency, knowing her work: take her, leave the two girls free; she couldn't
refuse; she went to America.** Sua catches the grandfather's two covers: not a 30-year-old military
prototype (EP002/005), and the calibration was never "set to Dana" (EP081 — he flew Sua without
touching it). Dana: `그런 게 어딨어요.`; Sua takes her hand first; the 8/31 line.

**Craft:** first use of the **clarity guard** — every term followed by a gloss, nine must-restate
sentences on the page, the POV character "catches" every clipped line, every 그것 landed.
Five rounds of user notes shaped it (see Gate-DE report). **Immune rejection is not explained**
(G0-030 — Hyeonseo herself doesn't know until 6-10); the S15 outline row was corrected, and
SNAP-145's Hyeonseo `knows` (which wrongly listed immune rejection) was fixed in SNAP-146.
LOC-02 now has the inner iron door by the maintenance area (gauge needle always at 0 = the culture
room). Tracker: resolved L-REVELATION, D-SUA-TOO, D-OUTSIDE-QUESTION, HS-GLANCE-WORKBENCH; new
YJ-COVER-EXPOSED (6-8), D-LUCY-AMERICA (`미국` → Lucy's face → EP153), D-HODU (6-9).

Next: **EP147 「순서가 뒤집힌다」** (Sua POV · 8/31 · it wasn't her fault).

## EP147 approved (2026-09-23) — 「순서가 뒤집힌다」, closing 6-7

**EP147** (`153_EP147_승인완료`, **5,050 chars**, 10/29 Sat afternoon–night, **Sua POV**). Approved
as drafted. Hyeonseo keeps the EP145 promise and drives Sua home. At the facility door the EP138
positions are reversed: this time Sua leaves and Dana watches from inside the threshold (`…가.` /
`응.`). Hyeonseo folds the wheelchair alone, two hands (three steps; that morning it took two people
five). In the car Sua raises her legs herself for the first time (`제 다리도 그거 때문이에요?`) and,
for the first time, says aloud the order she has carried for two months (EP106 `자기가 안다고
생각했다`): what came in from behind passed through *her*, broke something inside that doesn't
show on scans, and *because she was hurt* the Titan stopped and everything scattered. Hyeonseo pulls
onto the shoulder, hazards on: **it was the Titan that was pierced, in the back of the waist** (the
monster feigned weakness and waited for her to turn); same origin → riding links them (`그날은 그게
아주 깊었어`; `타이탄은 너한테 따로 맞출 게 없었어` — why it fit from the first ride); **the wound
transferred to her body** — `허리에서 다리로 가는 신경`, glossed as the path that carries "move" to
the legs (catching EP106's "the word never reached the knee"); **scans show nothing because her
body has no wound; her body was not hurt first** → not her fault. `…나아요?` → `…모르겠어. 이렇게
된 사람은 너밖에 없어서` (the rehab goal stays hidden). `언니도 알아요?` `아니.` / `언니한테 말해도
돼요?` `네가 정해.` Home: Yeongjin's hand is on the handle before the ramp tips; `…왔냐.`; Hyeonseo
bows slightly, he nods once, no words; 된장국. At the table Sua almost writes beside the 8/31 line,
then doesn't: the paper was right; the order in her head was wrong. Counts three: one name, one
unknown, one decision.

Seals held: 하반신·마비·걷지 못한다, 요추·척수 (신경 once, glossed), immune rejection, Sentinel
identity, the cone-snail lineage / observation-sheet guilt. Tracker: **FS-S13-NO-INJURY resolved**
(cause; no diagnosis name; prognosis unknown), FS-S13-NO-SEQUENCE progressed, SUA-SEVENTH-LINE
progressed; new **SUA-TELL-DANA** (6-8). Ledger v2.42, SNAP-147.

Next: **6-8 「같은 방」 EP148~157** — EP148 (10/31, both POVs): **징계** — the collar grab = assault,
the unit collision = disobeying orders.

