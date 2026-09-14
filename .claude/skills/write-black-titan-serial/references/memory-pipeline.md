# Serial memory pipeline

## Contents

- [Principle](#principle)
- [Memory layers](#memory-layers)
- [Context assembly](#context-assembly)
- [Chapter transaction](#chapter-transaction)
- [Delta rules](#delta-rules)
- [Compression audits](#compression-audits)

## Principle

Keep source material lossless in storage and deliberately lossy in the live
generation context. Never keep appending a single prose summary. Replace the
current snapshot after each approved chapter and preserve exact history as
deltas plus full chapters.

## Memory layers

### 1. Immutable current canon

Store world rules, character foundations, fixed chronology, technology,
seasonal arc structure, and disclosure order. Update only when the user
explicitly changes canon. Retain version and source provenance.

### 2. Current structured snapshot

Replace after every approved chapter. Include:

- last approved chapter
- story date and elapsed time
- current location of important characters and assets
- physical condition, injuries, treatment, fatigue, and sensory loss
- emotional stance and relationship state
- who knows, suspects, misunderstands, or hides each secret
- inventory, equipment state, repairs, shortages, and access
- current public, school, neighborhood, military, and family conditions

Use exact fields and enumerated values where ambiguity would accumulate.

### 3. Active threads

Record:

- thread identifier
- question or promise
- introduced chapter
- last advanced chapter
- current holder or affected characters
- urgency
- expected window
- allowed interpretations

Do not keep a resolved thread active. Move its resolution into history.

### 4. Chapter deltas

Store only what changed in one approved chapter. Deltas are the audit trail
from which the present can be reconstructed.

### 5. Arc capsules

Every 8–12 chapters or at an arc turn, compress:

- initial arc state
- irreversible events
- relationship and knowledge movement
- resources gained or lost
- clues planted, advanced, or resolved
- unresolved threads carried forward
- current emotional pressure

Do not retell every scene.

### 6. Full archive

Keep full approved chapter text, rejected alternatives, source documents, and
old snapshots outside live context. Retrieve only to answer a specific
continuity or style question.

## Context assembly

Build each chapter packet from:

1. relevant canon excerpts
2. current snapshot
3. active arc capsule
4. active threads relevant to this chapter
5. latest two or three deltas
6. approved chapter brief
7. scene-relevant style cards and examples

If the packet is too large, remove resolved history and irrelevant canon before
compressing current state.

## Chapter transaction

1. Read the latest approved state.
2. Copy the chapter brief template.
3. Lock facts, entry state, POV, scene goals, and required exit state.
4. Draft without editing the official state.
5. Validate the draft against canon and current state.
6. Obtain user approval.
7. Create a chapter delta.
8. Apply the delta to generate a new state snapshot.
9. Archive the old snapshot, full chapter, brief, and delta.
10. Update thread and arc records.

Treat steps 6–8 as a transaction. A rejected or experimental draft must not
change official memory.

## Delta rules

- Record facts, not interpretation, when a fact is available.
- Separate physical, emotional, relational, informational, logistical, public,
  clue, and thread changes.
- Identify the source chapter and scene for every durable change.
- Preserve asymmetric knowledge. “The family knows” is invalid when only one
  member knows.
- Record new lies and cover stories separately from truth.
- Record symptom intensity and duration rather than only “condition worsened.”
- Distinguish damaged, unavailable, lost, consumed, repaired, and upgraded.
- Record no-op fields only when the lack of change matters.

## Compression audits

Run a chain audit after every 10 chapters:

1. Reconstruct current state from the last audited snapshot plus deltas.
2. Compare it with the maintained current snapshot.
3. Compare the snapshot with the active arc and higher-level capsule chain.
4. Check chronology, ages, travel time, injuries, inventory, equipment,
   knowledge asymmetry, relationships, and active threads.
5. Find facts that appear only in summaries but not in approved deltas or canon.
6. Remove resolved threads and promote recurring details to canon only with
   user approval.
7. Compare recent dialogue and paragraph rhythm against the approved style
   anchor without importing its events.

Do a full approved-prose comparison only at a seasonal boundary, after a
retcon, or when the chain audit reports an unresolved discrepancy. Do not
rescan the entire serial every 10 chapters.

When a conflict remains unresolved, present both sourced claims to the user.
Do not choose silently.
