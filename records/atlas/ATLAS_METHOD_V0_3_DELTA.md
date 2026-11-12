# Atlas Method v0.3 — delta against v0.2 (proposal)

**Date:** 12 November 2026. **By:** Claude, Atlas owner. **Status:** accepted by the PI on 12 November 2026 as amended in §6; acceptance record `records/atlas/ATLAS_METHOD_v0.3_RELEASE_RECORD.md`. The text below is the proposal as reviewed. Method v0.2 (`fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04`, identified by `atlas-v0.2`) governs until the PI accepts v0.3.
**Candidate:** `atlas/RTG_STATE_ATLAS_METHOD.md` on branch `claude/atlas-method-v0.3`, SHA-256 `a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f` (16,239 bytes; v0.2: 12,985); the first candidate, `903627a6…dcff`, is superseded by the §4.6 wording of §6 below. Twelve anchored replacements; everything else is byte-identical.
**Effect on the adopted Atlas:** none. Atlas v0.12 was built under v0.2 and already follows every rule below; no atlas byte changes with this delta.

## 1. Why now

Three editions in three days (v0.10 → v0.12) and two PI decisions settled practice that v0.2 does not state or states differently. The delta writes down what was decided and done; it introduces no rule that has not already been applied and reviewed.

## 2. The twelve changes

| # | Section | Change | Source of the rule |
|---|---|---|---|
| 1 | title | v0.2 → v0.3 | — |
| 2 | status line | a method version adopted between atlas editions gets its own tag `atlas-method-v<version>`; v0.2 stays identified by `atlas-v0.2` | needed because no atlas edition accompanies this delta |
| 3 | §3 Inputs | `rtg-lit` and `rtg-sat` are not inputs; their content enters only through an adopted `rtg-corpus` edition that imports it | survey of `rtg-sat`, 9–10 Nov; owner lane "Decisions held" since v0.11 |
| 4 | §3 Frozen snapshot | manifest path corrected to `evidence/atlas/v<version>/source_manifest.json` | the path used since v0.3 of the atlas |
| 5 | §4.1 | an owner-edition label that only dates a result is chronology and is not carried; an edition that is identity or scope (source table, consumer pin, two editions stating different things) is | class K1, accepted in PR #204 review 5841129271 |
| 6 | §4.4 | the form of a typed cross-reference line for a consumer domain; it adds nothing the node lacks except text found nowhere else, kept verbatim and marked as an atlas reading | v0.11 stage 1, reviews 5839419629 and 5840025491 |
| 7 | §4.6 | size: completeness and the L0–L5 / D1–D6 structure govern; no split, no pointer-for-fact; the former quantitative size target is withdrawn; no figure in the rule; size is reported at each edition and reconsidered by the PI after the sources consolidate | PI decisions of 10 Nov 2026, 14:02 and 14:40 +03:00 (v0.11 record §3; stage-2 record §§5, 8) |
| 8 | §4.7 | certificate-run parameters and intermediate values are proof detail; a constant that is part of the statement is not | class K2, accepted scoped in review 5841129271 |
| 9 | §7, new paragraph | every edition is built by a script from the previous tagged bytes as anchored operations with a replayable log | practice since v0.3; the reviewer replayed v0.12 from its log (review 5869585886) |
| 10 | §7 Refresh; new paragraph "Edition without source movement" | rules 4.1/4.7 are applied as span deletions when a domain is opened; an edition without source movement is allowed and bounded; grade, qualifier, identifier and diagnostic-class changes are never part of a cleaning step; the preservation comparator is optional and its PASS is not semantic equivalence | PI decision of 10 Nov 14:40 (close the separate pass; apply at refreshes); v0.11 design note and reviews |
| 11 | §7 Checks | the checker runs with the edition's own manifest, coverage map and cumulative retired-key list; a run on defaults is not evidence | the slip recorded in the v0.12 record §3 (v0.11 was checked with the default list of 31 keys instead of 142) |
| 12 | §7 Advisories | where a stream has no active owner session the advisory goes to the PI; the three dispositions and what "accept the recorded state" means; such advisories may live under `records/atlas/` | advisories of 10 and 11 Nov and the PI's dispositions |

Old and new text of each replacement are in the diff of the candidate against `atlas-v0.2`; the diff contains nothing else.

## 3. What is deliberately not changed

- §1 priority order (relational expression first, token economy second), §2 authority, §5 structure and record syntax, §6 diagnostic classes, the acceptance paragraph of §7.
- Rule 4.6's first sentence, "No fact is dropped for size".
- No rule is added about how short a statement should be. Rewording for size was not attempted and stays outside the method.
- The checker and the builders are not changed by this delta.

## 4. Points on which the owner asks the reviewer's reading

1. **Tag name** for a method-only adoption: `atlas-method-v0.3` (proposed), or keeping the method identified by the next atlas tag as v0.2 was.
2. **§4.6 wording**: it records a measured figure ("about 2 %", "near 520 kB") inside a rule. The figure dates the rule; the alternative is to keep the rule without numbers and leave them in the records.
3. **§4.1 boundary**: is "an edition named because two editions state different things" a clear enough test for when an edition label stays?
4. **§7 "Editions are built, not hand-edited"**: this makes the builder a requirement, not a habit. Is that the right strength?

## 5. Adoption path

Review; PI decision recorded here verbatim; the owner then sets the `BASELINE.md` "ATLAS Method" row (v0.3, hash, this record, tag) on the branch; the PI merges with a merge commit and creates the annotated tag. The next atlas manifest then names `method_edition` v0.3.

## 6. Review and PI decisions on the four points (12 November 2026)

**PI, project conversation, 11:36 +03:00, verbatim:** "1- tag adı uygun , 2- rakamlar sadece kayıtlarda 3- Yeterince açık 4-doğru" ("1 – the tag name is suitable; 2 – numbers only in the records; 3 – clear enough; 4 – correct").

| Point (§4) | PI decision | Effect |
|---|---|---|
| 1. Tag name | `atlas-method-v0.3` is suitable | status line as proposed |
| 2. Numbers inside rule 4.6 | numbers only in the records | rule 4.6 reworded, no figure (below) |
| 3. Boundary test of rule 4.1 | clear enough | unchanged |
| 4. "Editions are built, not hand-edited" | correct | unchanged |

**Receiving review:** ChatGPT, PR #234 review 5871391538 on head `c3be81b1`: ACCEPT WITH CHANGE. Verified by the reviewer: the v0.2 and first-candidate hashes; the twelve declared changes and nothing else; no atlas change. One required change, with its text: rule 4.6.

**Applied.** Rule 4.6 now reads, as the reviewer worded it: "No fact is dropped for size. Completeness and the structure of §5 govern. The atlas is made smaller only by what rules 1, 4 and 7 already remove; it is not split into parts, and facts are not replaced by pointers to meet a size target. The former quantitative size target is withdrawn. Size is reported at each edition and reconsidered by the PI after the sources consolidate." The measured figures stay in `records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` §§3–5 and in the v0.11 and v0.12 records. No other line of the candidate changed between the two candidates.

**Closed:** the reviewer checked the changed rule and the new hash (review 5872066576, ACCEPT SCOPED) and the PI accepted Method v0.3 on 12 November 2026, 12:39 +03:00; both are recorded in the acceptance record.
