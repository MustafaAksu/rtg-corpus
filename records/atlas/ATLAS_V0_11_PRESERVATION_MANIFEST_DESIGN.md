# Atlas v0.11 — preservation manifest: design draft 0

**Date:** 10 November 2026. **By:** Claude, Atlas owner. **Status:** [SESSION] design proposal for review. It changes no Atlas byte, adopts nothing and is not a release tool. `atlas-v0.10` governs.
**Files:** `evidence/atlas/v0.11_design/atlas_manifest_draft.py` (SHA-256 `5809873f…`, draft extractor), `sample_manifest.json` (eight representative records), `full_run_summary.json` (counts on the whole Atlas).

## 1. What the manifest is for

v0.11 is planned as a compaction edition: no source movement, no semantic change. Method v0.2 §4(6) forbids dropping a fact for size, and its size target (≈60–90k tokens) yields to completeness. `tools/check_compaction.py` is written for DSNs (backticked claim tags, DSN header/footer, history appendix); it does not read Atlas records. The manifest is the Atlas-side contract: what must be shown unchanged, per record and per field, before and after the compaction.

Same node and edge identifiers do not imply the same content. The protected content of a node is its claim, grade and qualifiers, premises, scope, convention data, evidence and custody limits, and negative constraints; of an edge, its type and the consumer's actual pin.

## 2. Schema (draft 0)

One entry per Atlas line that carries content.

| Kind | Key | Bound content |
|---|---|---|
| `node` | owner RID or `*STREAM:slug` | grade with qualifiers; `fields[]`, each with `cls`, byte `span` in the line, `sha256` of the exact field text, the RIDs, edition pins, evidence/custody markers and (for statement, scope, premise, negative) the numerals found in it; `line_sha256` |
| `diagnostic` | L5 key or H number | diagnostic class, RIDs, pins, markers, `body_sha256`, `line_sha256` |
| `UNPARSED` | line number | `line_sha256`, RIDs found, first 60 characters |

Field classes: `statement`, `scope` (`sc:`), `premise` (`if:`, `[assuming:`, `import:`), `dep` (`<`), `consumer` (`>`), `negative` (`¬`), `cert`, `locator` (`@`), `alias` (`≡`), `derived` (`~`), `tension` (`!`), `collision` (`⊥`), `evidence`, and `UNVERIFIED` for any segment the parser cannot type.

Two rules carry the design:
1. **Every field is bound to source text.** A structured value is only a view; the span and hash of the exact text are the evidence. A parser that skips a premise before and after proves nothing, so an untyped segment is kept as `UNVERIFIED` with its hash, never dropped, and an empty field set is not a PASS.
2. **Two tiers of proof.** Tier A: typed fields compared one to one (text hash equal, or a declared edit whose RIDs, pins, markers and numerals are equal as multisets). Tier B: everything else (`UNVERIFIED` fields, `UNPARSED` lines) is covered only by exact-text movement: the text appears unchanged in the candidate, or the movement map declares the edit and it goes to the change-focused review. Tier B is never reported as field-preserved.

## 3. What the draft extractor found on `atlas-v0.10`

| Measure | Count |
|---|---|
| Content lines | 1,292 |
| Parsed as typed nodes | 687 |
| Parsed as L5/H diagnostics | 117 |
| `UNPARSED` | 488 |
| Typed fields | 1,719 (statement 685, locator 435, negative 128, cert 105, scope 104, consumer 91, dep 75, alias 56, derived 27, premise 8, tension 4, evidence 3, collision 1) |
| `UNVERIFIED` fields | 545, in 373 of the 687 nodes |
| Nodes with every field typed | 314 |

Consequences for the plan:
- **Tier A covers about half today.** The 488 unparsed lines are index lines (252 "topic · RID (domain)" lines), RID-led records with a non-standard grade position (110, e.g. `… THM (v6.4.23) |`, `… node ALG(SESSION…)`), `*STREAM:` records without a grade (78), tables, `⊥` lines and the eight `*ATLAS:checked-*` lines. Either the parser learns these forms before the compaction, or the compaction leaves them byte-identical. Both are acceptable; the choice is recorded per form.
- **The 545 untyped segments are mostly second statement segments** (the record syntax allows one statement, the Atlas often writes two or three). A compaction that merges them needs a declared edit each time. Normalizing the record syntax first (a pure re-segmentation with identical text) would move most of them to Tier A.
- **Fifteen node identifiers occur on two lines** (for example `RECOG-THM-R9-MEMORY`, `GEN-ART-SATURATION`, `*GEN:phase-drift-law`). Method §4(4) asks for one node per claim; the v0.10 review fixed one such case (birth symmetry). Each of the fifteen needs a decision: one home and a cross-reference, or a recorded reason. This is content work, not layout, and belongs in the v0.11 dispositions.
- **Conditional markers are thin in the syntax.** Only 25 nodes carry `·c` or a typed premise; conditions also live in statement text. The marker list (custody, `[indep-…]`, `EV-…`, "not a recovery", `[assuming:`) is therefore compared on every field, typed or not.

## 4. Acceptance criteria proposed for the v0.11 build

1. Source snapshot frozen first; all 18 sources byte-equal to v0.10 (asserted).
2. Base manifest and candidate manifest produced by the same reviewed extractor; extractor hash recorded.
3. Node key set equal; diagnostic key set equal, except keys retired or added by a recorded disposition.
4. Tier A: every typed field PRESERVED (hash equal) or DECLARED (movement map entry) with equal RID, pin, marker and numeral multisets; grade and qualifiers equal unless a disposition says otherwise.
5. Tier B: every `UNVERIFIED` field and `UNPARSED` line is found verbatim in the candidate or is DECLARED; the report gives the Tier B count, never folded into PASS.
6. `*ATLAS:checked-*` records: the run history may move to `evidence/`, but the current result, its scope and its "not rerun / source-reported" limit stay on the Atlas record.
7. Negative controls on the compare stage: a dropped premise, a changed numeral, a consumer pin silently repinned, a custody marker removed, a negative constraint merged away, a field moved to another node.
8. Two byte-identical builds; `tools/atlas_check.py` 0 FAIL; change-focused review of every DECLARED edit.
9. Size is reported, not gated. "About half" is an aim.

Out of scope for the manifest: Method v0.3 (compaction trigger, satellite repositories out of scope) is a separate method delta with its own review.

## 5. Open questions for the review

- Normalize record syntax first (one statement field, typed secondary segments) as its own byte-level step, or keep Tier B large?
- Is the marker list sufficient, and should `·s`, `·dx`, `nc` changes be forbidden outright in a compaction?
- For duplicate identifiers: fix all fifteen in v0.11, or only those the compaction touches?
- Should the compare stage live in `tools/` beside `atlas_check.py`, with a receiving harness as for `orient.py`?

## 6. Next steps

1. Review of this draft (Atlas co-owner).
2. Extractor to cover the non-standard grade forms and index lines; compare stage with the §4.7 controls.
3. A pilot on one domain (proposal: D3, recognition) to measure the achievable reduction under these rules before committing to the whole file.
