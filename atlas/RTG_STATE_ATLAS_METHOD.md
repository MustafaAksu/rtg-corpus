# RTG State Atlas — Method v0.1

**Status:** working method, 21 October 2026. Owner of the method and of the atlas: Claude (atlas owner), under PI (Mustafa) authority. Not a DSN; not governed by the DSN release cycle. Amend by new version of this file.

## 1. Purpose

The RTG State Atlas is one file that lets an AI session grasp the entire current RTG scope in a single read: what exists, what is established at which grade and scope, what depends on what, what is open and what blocks it, and where the corpus is inconsistent or has unnoticed links.

Reader: AI only. Human readability is secondary.

Priority order of optimization:
1. relational expression (objects, claims and the edges between them);
2. token economy, only after (1) is satisfied.

## 2. Status and authority

- The atlas is **derived and noncanonical**. It is never the source of a claim. Every node cites its owner document and RID. On any conflict the owner DSN wins.
- The atlas owner has **no authority** over any stream. It reports and advises; stream owners decide; the PI holds final decision.
- The atlas header lists the exact source versions it was built from, so staleness is visible at a glance.

## 3. Inputs

All canonical DSNs and registries in the project root, plus the noncanonical working documents the PI includes (currently ER-2B consolidated study, RER registry draft, FMS session ledger), each tagged `noncanonical` at node level. DSN_METHODOLOGY contributes tag semantics to L0 only.

Reading order for the first pass: GEN (pilot, done) → DYAD → RECOG → TRIAD → NUMGEN → RRF → RER → OFN → FMS → ER-2B → OPEN-M → DART → Arithmetic/Zeta → Discrete Genesis → L0/L1/L2 Bridge → Pre-Legacy → Programme Overview → Methodology.

## 4. Content rules

1. **Current state only.** Version history, review verdicts, draft rounds, adoption records and hashes are excluded; they stay in the DSNs, release records and archive.
2. **Rejected claims are current state.** FAIL / RETRACTED entries are kept as live constraints ("this route is closed"), compactly.
3. **One node per object and per claim.** An imported claim is not restated; the consumer gets an edge to the owner's node.
4. **No stream partitioning.** Stream labels (DYAD, GEN, …) mark provenance only, never structure.
5. **No fact is dropped for size.** The size target (≈60–90k tokens) yields to completeness.
6. **Proofs are not summarized.** A claim carries at most a one-line method pointer; full proofs stay in the owner DSN.
7. **Facts that are clearly wrong** against the rest of the established corpus are not used as nodes. They are recorded as one L5 line (claim, location, conflicting evidence), never silently dropped. Unproved or uncertain facts are included at their stated grade.
8. **Atlas-derived links** (identities, dependencies or equivalences the atlas notices but no owner records) are marked `~` and must be verified before use.
9. **Language:** English.

## 5. Output structure

```
L0 KEY        grades, qualifiers, record syntax, edge operators, global scope rules
L1 OBJECTS    every mathematical object defined once; aliases (≡); symbol collisions (⊥)
L2 CLAIMS     one record per claim, grouped by topic (not by stream)
L3 FRONTIER   OPEN items in dependency order: what each blocks and is blocked by
L4 CONSTRAINTS scope guards and firewalls as rules; exportability; required bridges
L5 DIAGNOSTICS inconsistencies, gaps, collisions, pin drift, unnoticed links; passed checks
```

A short headline list of the most consequential L5 items is placed directly after L0, so a reader sees critical problems first; the full L5 stays at the end.

Record syntax:

```
ID GRADE | statement | sc: scope | if: premises | <dep | >used-by | ¬ not-claimed | cert | @owner§
```

- `ID` = owner RID; `*STREAM:slug` when the owner gives no RID (this is itself an L5 item).
- grades: THM ALG DEF CAND HYP RES NUM HEUR INTERP OPEN FAIL RET CONV; qualifiers `·c` conditional, `·s` structural, `·dx` diagnostic only.
- edges: `<` depends on · `>` consumed by · `≡` same object · `⊥` symbol collision · `!` tension/conflict · `~` atlas-derived link.
- formulas in LaTeX-like plain text; exact values kept exactly.

## 6. Diagnostic classes (L5)

| Class | Meaning |
|---|---|
| D-RID | claim without RID; duplicate RID; RID heading two entries |
| D-PROOF | adopted THM/ALG whose proof source or certificate is missing |
| D-GRADE | grade inconsistent with premises (e.g. THM resting on OPEN/HYP), or same claim at different grades in different places |
| D-CONV | sign, normalization or convention conflict between sites |
| D-SYM | symbol collision or undefined symbol |
| D-PIN | consumer pins an outdated owner version, or cites a value without its RID |
| D-STALE | frontier/registry entries whose stated status contradicts the entry body |
| D-SCOPE | scope label missing where two sites differ only by scope |
| D-LINK | unrecorded identity, equivalence or dependency between claims (often cross-stream) |
| D-WRONG | fact excluded as clearly wrong (rule 4.7) |
| PASS | atlas-verified consistency checks (exact arithmetic re-done) |

## 7. Process

**Pass 1: extraction.** Each source is read in full and transcribed into the atlas format. The slice is merged into the master atlas, unifying objects and collapsing imports to owner nodes. Diagnostics are recorded as found.

**Pass 2: owner consultation.** For each stream the atlas owner issues an **Atlas Advisory Note** to that stream's owner:
- one row per finding: class, location, observation, suggested fix, and whether it is editorial or scientific;
- the stream owner records a disposition for each row (accept / reject / defer, with reason);
- accepted fixes are made by the stream owner in the DSN through its normal draft → review → adoption cycle. The atlas never edits a DSN;
- the atlas is updated from the adopted DSN, not from the note.

Typical disciplining targets are missing RIDs, missing proof sources, untyped conventions and stale pins.

**Pass 3: automation.** Once the corpus is disciplined (RIDs complete, proof sources registered), add machine checks:
- a coverage gate: every live owner RID and every exact formula appears in the atlas;
- link integrity: every edge target exists;
- grade propagation: no THM rests on an OPEN or HYP premise without a `·c` qualifier;
- pin freshness against the source version list.

**Regeneration.** On each adopted release of any source, re-extract that source's slice and refresh the version list. A full rebuild is done when the method changes.

## 8. Current state of work

- Pass 1 complete (2026-10-21): 18 sources sliced and merged into `RTG_STATE_ATLAS_v0_1.md` (≈424k chars). Body grouped in seven subject domains: D1 foundations/governance/representation · D2 dyad core and resonance arithmetic · D3 recognition/return/memory · D4a triad, primitive K₃/K₄ and model families · D4b geometry/metric/network/UV · D5 discrete branch and graph diagnostics · D6 historical provenance. Header: source edition table, L0 key, headline L5 (H1–H12), D-WRONG list, cross-domain object index.
- Size exceeds the 60–90k-token target; per rule 4.5 completeness was kept. A later wording-compression pass (no fact removal) is possible.
- Next: Pass 2 — Atlas Advisory Notes, one per stream, rows keyed by the L5 IDs (STREAM.<id>). Coverage gate still deferred to Pass 3.
