# Atlas v0.11 — preservation manifest: design (draft 0, revised 10 Nov after review)

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
| Typed fields | 1,722 (statement 685, locator 435, negative 128, cert 105, scope 104, consumer 91, dep 75, alias 56, derived 27, premise 8, tension 4, evidence 3, collision 1) |
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

## 7. Revision 1 (10 November 2026, after the receiving review of draft 0)

The review (PR #203; PR #202 review 5837804086) accepted the direction and asked for three corrections. They are implemented together in `tools/atlas_preservation.py` (SHA-256 `c78be1f29bae55642704bbeaaeef86c06b17983423a2c819ac8c2fe574a8b75a`), which supersedes the draft extractor of §§2–3; the draft file stays as history. Where this section and §§2–4 differ, this section governs.

**R1 — bytes, and the whole file.** The tool reads and hashes bytes. Every line of the file is a region with its byte span and SHA-256 (headings, tables, index and L0/L4 lines, raw lines, records); the tool asserts that the regions cover the file exactly and that `SHA256(B[a:b])` equals every recorded hash, for regions and fields alike. CRLF is preserved. Each region carries its heading context (the chain of enclosing heading hashes), so a record that changes section is not silently "unchanged".

**R2 — declared is not preserved.** Statuses are mechanical: `EXACT` (same bytes, same record occurrence, same heading context), `MAPPED_EXACT` (same bytes, declared move), `DECLARED_PENDING_REVIEW` (any declared edit, deletion or insertion) and `FAIL`. Equal RID, pin, marker or number lists never upgrade a changed field; those lists are kept as review aids only. An untyped segment is matched only inside its own record occurrence, so text that reappears under another record is a FAIL. A changed grade or qualifier, record identifier or diagnostic class always fails: such a change is not a compaction and needs its own reviewed stage-1 delta, against whose hashed output the compaction is then compared. The result word is `MECHANICAL PASS`, and the report says that pending items are not preserved content.

**R3 — occurrences and bound relations.** Records are keyed by identifier and occurrence (`ID#k`); deleting one of two lines with the same identifier fails. RID, pin and marker lists keep order and multiplicity. An edge field is compared by its exact bytes, which binds target, edge type and the consumer's pin together. Identifier kinds are separated (`scientific`, `artifact`, `pseudo` for `*STREAM:` records, `l5-key`, `headline`). `explicit_condition_marker` replaces `conditional` and means only that a recognised marker was found.

**Answers adopted from the review.** No up-front normalization of the whole Atlas: extraction is lossless on the unchanged v0.10 and unsupported forms are carried byte-identical; a re-segmentation, where a pilot needs it, is its own assertion-gated step. In a pure compaction the semantic qualifiers are fixed (`·c`, `·s`, `·dx`, `nc`, premises, quantifiers, domain, convention, negative limits, custody). The comparator is an Atlas-specific tool in `tools/`; the DSN checker is not relaxed.

**Runs** (`evidence/atlas/v0.11_design/rev1/`):
- `selftest`: 21 controls as expected — 15 negatives (dropped premise, `q<1`→`q>1`, swapped pins, removed custody marker, merged-away negative, untyped condition moved to another record, deleted second occurrence, removed heading, undeclared section move, grade change, unexplained insertion, diagnostic class change, and three "record mapped but field not declared" cases) and 6 positives (identity; declared edit stays pending; declared move is MAPPED_EXACT; CRLF identity; non-ASCII byte spans; marker flag).
- `atlas-v0.10` extract: 1,543 regions (135 headings, 560 typed nodes, 117 diagnostics, 615 raw lines, 116 blank), 521,243 bytes fully covered; 340 untyped segments. The stricter record head leaves more lines raw than draft 0 did; raw lines are protected byte for byte.
- `atlas-v0.10` against itself with an empty map: MECHANICAL PASS, 1,427 EXACT.

**Identifiers on more than one line: 13, classified once** (draft 0 said 15; two were artefacts of its looser head pattern).

| Identifier | Kind | Occurrences (line: grade, bytes) | Same statement text? |
|---|---|---|---|
| `*GEN:phase-drift-law` | pseudo | L1059: ALG, 399; L1205: ALG, 375 | no |
| `*GEN:plateau-bridge` | pseudo | L1057: ALG·s, 201; L1202: ALG·s, 211 | no |
| `*GEN:rank-obstruction` | pseudo | L1043: THM, 236; L1137: THM, 166 | no |
| `*GEN:uniform-phase-sink` | pseudo | L1054: ALG, 177; L1201: ALG, 202 | no |
| `*NUMGEN:C7B-T1..T4` | pseudo | L523: RES[ALG], 550; L1344: ALG, 297 | no |
| `GEN-ART-JQ-PHASEDRIFT` | artifact | L1058: ALG, 157; L1203: ALG, 164 | no |
| `GEN-ART-SATURATION` | artifact | L541: NUM, 110; L1060: RES, 505; L1206: RES, 513 | no |
| `NUMGEN-N3D-FINITE-CHAR` | scientific | L511: THM, 286; L1351: THM, 196 | no |
| `RECOG-ALG-CHART-LAWS` | scientific | L373: ALG, 323; L744: ALG, 562 | no |
| `RECOG-ALG-NU3-CLOSED-FORM` | scientific | L462: ALG, 341; L702: ALG, 550 | no |
| `RECOG-THM-P2-C0-FIRST` | scientific | L420: THM, 142; L753: THM, 829 | no |
| `RECOG-THM-P2-HET` | scientific | L419: THM, 110; L752: THM, 831 | no |
| `RECOG-THM-R9-MEMORY` | scientific | L392: THM, 345; L718: THM, 1370 | no |

None of the pairs repeats the same statement text. Reading: the five `*GEN:`/`*NUMGEN:` pseudo records and the two artifact rows are D4a/D4b or D2/D5 double homes of RID-less owner material; the six scientific rows are a short D2 edge record and a full D3 or D5 node. Per the review, only those the pilot touches or that block mapping are resolved in v0.11; the rest are a recorded, deferred debt. The six RECOG/NUMGEN scientific pairs fall inside or beside the D3 pilot and will be decided there (one home plus a typed cross-reference, as for birth symmetry in v0.10).

**Next:** D3 pilot under these rules — stage-1 dispositions if any, then the compaction with its movement map, the comparator report and the list of pending items for review.

## 8. Revision 2 (10 November 2026, after the receiving review of the tool)

The review of revision 1 (PR #203 `f80a4e8`; PR #202 review 5837996742) confirmed the byte and CRLF handling and the 21 self-tests, and found three gaps in the comparator. All three are fixed in one pass; tool SHA-256 `c6e6660b4d57c39a81bda9ad5c476db684ee74c962794a58cae2e1a9d5fed0e1`. Where §7 and this section differ, this section governs.

**AP-R1 — heading context.** Headings are kept on a stack with explicit levels; a new heading pops every heading of the same or deeper level. Sibling headings after a skipped level no longer nest (`# D / ### A / ### B` gives `D/B`).

**AP-R2 — relations between preserved pieces.**
- Inside a mapped record, fields are matched in order. A field whose bytes are unchanged but whose position relative to the other fields changed is a FAIL, or `DECLARED_PENDING_REVIEW` when the record declares `"reorder": true`. Exchanging two scopes between two statements of one record is therefore never all-EXACT.
- A raw line is bound to its anchor, the record it follows inside its heading. Moving it under another record changes the anchor: undeclared, it fails.
- Unchanged regions must keep their relative order. An undeclared swap of two unchanged records fails; a declared move is `MAPPED_EXACT`.
- `MAPPED_EXACT` certifies bytes only. When the heading context or the anchor changes, the row says so and the report lists the move under `obligations.context_reviews`, with old and new context. Zero pending items is not a statement that inherited scope survived.

**AP-R3 — invariants before mapping.** For every identifier present in base and candidate, the candidate may not carry a grade/qualifier (records) or a class (diagnostics) that the base did not carry for that identifier, whatever the map declares. Delete-plus-insert no longer routes around the rule. Deleting one of several occurrences, or turning a duplicate into a cross-reference, stays possible and is pending review.

**Runs** (`evidence/atlas/v0.11_design/rev2/`): self-test 30 controls as expected; the reviewer's revision-1 harness, unchanged except its two identity pins, 11/11 with its observation reproduced; `atlas-v0.10` identity compare MECHANICAL PASS, 1,427 EXACT, no context review.

## 9. Revision 3 (10 November 2026, after the receiving review of revision 2)

The review of revision 2 (PR #203 `a3e709a`; PR #202 review 5838164468) confirmed the 30 self-tests and its 11 earlier controls and found two defects in compound routes. Both are fixed locally; tool SHA-256 `6a4047b0dd3e10e15feeb9262d8b09816e82fa2f85a6d7ce939cc69d580e1d62`.

- **Context on every mapped pair.** The heading context and the anchor of a mapped base/candidate pair are compared before, and independently of, any byte comparison. A moved record whose line also changed (for example by one space) keeps its entry in `obligations.context_reviews` and gets a pending row "record edited and moved"; equal field bytes cannot remove the obligation.
- **One consumption mechanism for target fields.** Exact matches and declared replacements take target occurrences through the same routine; each target field occurrence is used once and the order pointer is shared. A candidate with one `sc: q<0` can no longer satisfy both a declared edit of `sc: q>0` and the unchanged `sc: q<0`; a candidate with two can. Leftover target fields are reported from the same free list.

**Runs** (`evidence/atlas/v0.11_design/rev3/`): self-test 33 controls; the reviewer's compound-route harness with only its tool pins moved — producer self-test, the 11 earlier controls and the 4 paired routes all as expected, exit 0; `atlas-v0.10` identity compare 1,427 EXACT, no context review.
