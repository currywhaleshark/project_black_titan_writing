---
name: write-black-titan-serial
description: Plan, draft, revise, validate, and continue the Korean long-form web serial Project Black Titan while preserving accumulated state, current-canon authority, standing guards (speech levels, combat tone, battlefield structure), character voices, and the user-approved C-style prose adapter. Use for Project Black Titan chapter outlines, scene writing, chapter drafting, prose/style revision, continuity checks, state compression, chapter deltas, arc capsules, memory updates, or old-manuscript style retrieval.
---

# Write Project Black Titan

Write from current canon, not remembered canon. Treat the old manuscript as a
style corpus only. Preserve long-range causality through structured state
updates after every finished chapter.

## Load the right references

Always read [project-state.md](references/project-state.md) first, then
[standing-guards.md](references/standing-guards.md) — the guards accumulated
from user corrections. Most errors in this project are guard violations, not
invention failures.

Then, in the workspace, read the two documents that carry what the bundle
cannot: the **handoff** (`05_문체_상태_인계/…새세션_인계서…`) for where the
work stands, and the **precedent ledger** (`05_문체_상태_인계/…선례대장…`)
for facts already established on the page — speech levels, house layout,
sortie route, battlefield history, the wording of promises. Checking the
ledger costs one read; guessing costs a retrofit across approved chapters.

When the project workspace contains a newer versioned handoff, approved
outline, chapter, delta, or state snapshot than the bundled reference summary,
read the exact workspace artifact and let it override the older bundled
summary. Use bundled references only as portable fallbacks; never downgrade a
verified current project artifact to match the skill package.

- For any planning, drafting, revision, or state update, also read
  [production-pipeline.md](references/production-pipeline.md).
- For planning or drafting, also read
  [memory-pipeline.md](references/memory-pipeline.md).
- For any outline, brief, prose, knowledge audit, or continuity check, also
  read
  [naming-knowledge-g0-approved.md](references/naming-knowledge-g0-approved.md).
- For work in the approved March–May spring block, also read
  [spring-level3-approved.md](references/spring-level3-approved.md).
- For any monster search, retrieval, binding, transport, or spring combat
  planning, also read
  [search-lineage-g0-approved.md](references/search-lineage-g0-approved.md).
- For EP1–6 briefs or drafts, or any spring work beginning at EP7, also read
  [s1-gateb-approved.md](references/s1-gateb-approved.md).
- For EP7–12 briefs or drafts, or any spring work beginning at EP13, also read
  [s2-gateb-approved.md](references/s2-gateb-approved.md).
- For EP13–18 briefs or drafts, or any spring work beginning at EP19, also read
  [s3-gateb-approved.md](references/s3-gateb-approved.md).
- For EP19–24 briefs or drafts, or any spring work beginning at EP25, also read
  [s4-gateb-approved.md](references/s4-gateb-approved.md).
- For EP25–29 briefs or drafts, or any spring work beginning at EP30, also read
  [s5-gateb-approved.md](references/s5-gateb-approved.md).
- For EP30–35 briefs or drafts, read the exact current approved S6 artifact
  named in [project-state.md](references/project-state.md).
- For EP36–40 briefs or drafts, or any spring-closing work, read the exact
  current approved S7 artifact named in
  [project-state.md](references/project-state.md).
- For EP41 onward (the summer season), also read
  [summer-level3-approved.md](references/summer-level3-approved.md), and read
  the exact current approved sub-arc outline named in
  [project-state.md](references/project-state.md) (S8 covers EP41–50).
- For any COMBAT chapter, lock the battlefield structure before writing —
  see `standing-guards.md` §4. Check the battlefield history in the precedent
  ledger first: a location may have been spent (the drowned apartment estate
  used up all its cover in EP45).
- For any outline, brief, prose, revision, or state update containing both
  Dana and Seong-ho, also read
  [dana-seongho-rivalry.md](references/dana-seongho-rivalry.md).
- For prose generation or style revision, also read
  [style-profile.md](references/style-profile.md) and
  [approved-style-anchor.md](references/approved-style-anchor.md). For spring
  chapters, also read [narration-style-card.md](references/narration-style-card.md)
  and only the appearing characters from
  [voice-cards-spring.md](references/voice-cards-spring.md).
- **For any Lucy-POV chapter (EP121 onward), you MUST also read
  [narration-lucy-pov.md](references/narration-lucy-pov.md).** The voice card
  governs her dialogue only; her narration follows different rules and the
  voice card alone will produce the wrong prose.
- For any use of old manuscripts, continuity validation, or finalization, also
  read [source-firewall.md](references/source-firewall.md).

If the current canon source or latest serial state is unavailable, ask the user
to attach or identify it. Do not reconstruct missing canon from model memory,
past summaries, old manuscripts, or web search.

When continuing from a new-conversation handoff, verify its approval claims
against `project-state.md` and the relevant approved references. A handoff
summary restores the working set but does not override canon or turn an
unapproved proposal into canon.

## Establish source authority

Apply this order:

1. User correction in the current request
2. Current canonical setting and plot documents
3. Latest approved serial state, ledger, and chapter text
4. Current chapter brief
5. Old manuscript, revision samples, and approved style anchor as `STYLE_ONLY`

Let higher sources override lower sources. Never resolve a conflict by blending
versions.

For a requested canon or overall-plot change, use
`assets/templates/document-registry.yaml` to run Gate 0 before editing
downstream outlines or state. List affected artifacts and classify each as
`KEEP`, `REVISE`, `RETIRE`, or `REBUILD`.

## Choose the operation

### Plan a chapter

1. Confirm that the relevant season, month, and episode outline have passed the
   approval gates in [production-pipeline.md](references/production-pipeline.md).
2. For a new Level 4 outline, copy
   `assets/templates/episode-outline.md`. For Level 5, copy
   `assets/templates/chapter-brief.md`.
3. Lock the chapter's initial state and required final change.
4. Define each scene by POV, immediate want, obstacle, revealed information,
   and state change.
5. Check that at least one relationship, knowledge state, active thread, or
   living condition changes.
6. Confirm every fact against current canon and latest state before writing
   prose.

### Draft a chapter

1. Freeze the approved chapter brief before style retrieval.
2. Retrieve at most two to four short old-manuscript passages by scene
   function, never by shared plot content.
3. Extract only cadence, dialogue behavior, action ordering, humor mechanism,
   or closing technique from those passages.
4. For a combat chapter, confirm the battlefield structure block is locked in
   the Level 6 document (`standing-guards.md` §4). Prose written before that
   lock has had to be rebuilt from scratch.
5. Draft in the user-approved C style. Treat voice-card and narration-card
   example sentences as `STYLE_ONLY`; they never authorize their events.
   Decide who each line is spoken TO before writing it; speech level follows
   the listener.
6. Expect the first pass to land at roughly 55–65% of the target length. That
   is normal for this project, not a failure — plan two to four EXPANSION
   passes that add texture and interiority rather than new events. Do not pad
   with plot the brief did not authorize.
7. Run the checks in order:
   - `scripts/check_draft.py <draft> --target-chars <target>` (length band,
     past-tense run, contrast signal)
   - `scripts/check_voice.py <draft>` (speech-level drift in dialogue AND
     third-person references to Yeongjin in narration; expect `WARN 0`)
   - `scripts/check_translationese.py <draft>` (translationese and
     essay-register bleed; expect `WARN 0`). Its thresholds are calibrated so
     that all 50 approved chapters pass — any WARN is real drift, not noise.
   - a banned-term grep from `standing-guards.md` §7 plus anything the chapter
     lock adds
   Do not submit a draft with a `FAIL`.
8. Run a separate Gate D cross-check against current state, knowledge
   asymmetry, fixed disclosure lines, terminology, length, scene count, and
   ending hook.
9. Perform the semantic firewall review in
   [source-firewall.md](references/source-firewall.md); lexical scanning alone
   is insufficient.

### Revise prose

Preserve fixed events, causality, information timing, and state changes unless
the user authorizes story changes. Diagnose the mismatch as one or more of:

- paragraph rhythm
- scene-focused viewpoint
- dialogue voice
- exposition placement
- concrete action and sensory anchoring
- humor temperature
- combat causality
- closing beat

Revise only the relevant layer. Do not import an old event to make the prose
feel more familiar.

### Finalize a chapter

1. Confirm user approval. Keep unapproved prose as `NONCANON_EXPERIMENT`.
2. Validate canon, chronology, knowledge asymmetry, injuries, inventory,
   relationships, active clues, and location.
3. Copy `assets/templates/chapter-delta.yaml` and record only changes caused by
   this chapter.
4. Apply the delta to a fresh copy of
   `assets/templates/current-state.yaml` or the existing state file.
5. Apply clue changes to
   `assets/templates/foreshadow-tracker.yaml`.
6. Preserve the old state and full chapter in the archive; replace only the
   context-facing current snapshot.
7. Update an arc capsule with `assets/templates/arc-capsule.md` every 8–12
   chapters or at an arc turn.

In this workspace a finished chapter produces a fixed set, and skipping one
breaks the next chapter's inputs:

1. approved text (`…_v1.0_GateD승인.md`) in a `NN_EPxxx_승인완료` folder,
   with earlier drafts moved to `_superseded/`
2. Gate-D validation record
3. chapter delta
4. the next state snapshot (`SNAP-xxx`)
5. the next foreshadow tracker snapshot
6. the next appearance-ledger version (this is what catches a character who
   has been off the page too long)
7. Gate-E state-application record
8. `project-state.md` updated, then `sync-skill.ps1` run so the installed
   skill copy matches
9. the mobile review page rebuilt and republished to its fixed URL

If a new rule came out of the chapter, add it to BOTH `standing-guards.md`
and the workspace handoff §6, and add any new fact to the precedent ledger.

Do not silently mark experimental prose as canonical. Ask for approval before
applying its delta to the official state.

## Assemble generation context

Use the smallest sufficient packet, in this order:

1. Relevant current-canon excerpts
2. Latest structured state snapshot
3. Active arc capsule and unresolved threads
4. Recent two or three chapter deltas
5. Approved chapter brief
6. Relevant voice card and style rules
7. Two to four short `STYLE_ONLY` examples if needed

Keep full archives out of the live generation context. Retrieve them only to
answer a specific continuity or style question.

## Output expectations

- Lead with the requested plan, scene, chapter, or revision.
- Distinguish `CANON`, `CURRENT_STATE`, `STYLE_ONLY`, and
  `NONCANON_EXPERIMENT` when presenting mixed materials.
- After a full draft, report detected continuity risks separately from prose.
- After an approved final chapter, provide its structured delta and list any
  thread whose urgency changed.
- Normalize spelling, spacing, punctuation, and quotation marks. Do not imitate
  source typos.
- Treat numeric style thresholds as warning bands. Do not add or delete a
  sentence merely to satisfy a quota without reading the scene in context.
- When the user corrects something, assume the error is systemic until proven
  otherwise: sweep the approved chapters for the same mistake before moving
  on. The speech-level drift found in EP44 turned out to span 44 lines across
  thirteen chapters.
- Never write a fact from memory when an approved chapter holds it. If it is
  not in the precedent ledger, open the chapter.
