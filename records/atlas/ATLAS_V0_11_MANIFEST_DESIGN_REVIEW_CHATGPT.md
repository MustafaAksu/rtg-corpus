# Atlas v0.11 preservation manifest — ChatGPT receiving review

**Date:** 10 November 2026. **Status:** [SESSION], NONCANONICAL tooling review; no scientific adoption, compaction acceptance or merge authorization.
**Object:** PR #202, implementation revision 1, head `e71382de2e408c15b781b0dbcc6046df8e06a513`.
**Decision:** **REVISE — three bounded implementation groups before this comparator is used as the D3 preservation gate.** The original byte-offset and CRLF defects are fixed. The producer's 21/21 result independently reproduces. Remaining issues are order/home binding, heading-context construction, and the documented hard invariants' delete/insert route. D3 planning and source classification may proceed, but a clean report from this revision is not yet sufficient for compaction acceptance.
**Previous review:** this same path at `134e420a3dc6722992da32487095f91280676260` preserves the complete draft-0 review. Its original probe script/output are unchanged; the current file records the latest inspected object, not an edit to frozen evidence. #113/#114 remain closed and are not reopened.

## 1. Sources and actual execution

Read the complete 205-line `tools/atlas_preservation.py`, including the comparator and all self-tests; design §7 and its 13-identifier classification; `rev1/atlas_v0_10_extract_summary.json`; current CONVENTIONS in full; and Atlas v0.10 lines 1–45 for real source/header/L0 context. Prior design and Methodology/Atlas Method scope remains as recorded in the previous review. No new full reading of the 18 owners, full Atlas extraction replay, owner-certificate campaign, or D3 compaction was performed.

[EV-BYTES / EV-HASH / EV-RUN] The connector-delivered tool was materialized without changing its source and verified against both its declared SHA-256 and Git blob before execution:

- Commit: `e71382de2e408c15b781b0dbcc6046df8e06a513`.
- SHA-256: `c78be1f29bae55642704bbeaaeef86c06b17983423a2c819ac8c2fe574a8b75a`.
- Git blob: `67a16432b19e771d40e8d27f7b16130952929f54`.
- Size: 17,564 bytes, 205 physical lines; Python 3.13.5.
- Direct shell retrieval of GitHub failed DNS. Authorized connector retrieval plus local byte-identity verification was used; this is actual execution of the unchanged tool, not an implementation reconstructed from its algorithm.

| Run | Actual result | Meaning |
|---|---|---|
| Unchanged producer `selftest` | 21/21 expected, exit 0 | Producer's stated result confirmed |
| Independent bounded receiving controls | 6/11 matched; 5 mismatches, exit 1 | Three groups in §§2–4; not a runtime error |
| Separate context-move observation | 1/1 reported behavior reproduced | Documented `MAPPED_EXACT` byte movement, not counted as a failing producer contract test (§5) |

Positive receiving cases confirm identity comparison, changed-field pending status, rejection of a wrong source hash, rejection of an inline edge-pin swap, an explicit same-context move, and UTF-8/CRLF byte slices. The LF separators omitted from individual spans reconstruct the original bytes exactly when reinserted between regions. That representation is distinguishable from saying the individual spans alone are a disjoint cover of every byte.

The producer's full-Atlas counts (1,543 regions; 560 nodes, 117 diagnostics, 615 raw, 135 headings, 116 blank; 340 untyped fields) and identity comparison remain **EV-SRC-READ / EV-NOT-RERUN** here. The 13 classified identifiers are a useful inventory, not proof that each repeated occurrence is interchangeable; one artifact identifier has three occurrences.

## 2. AP-R2 — preserve ordered qualified homes, not bags of equal fragments

**Required. Locations:** `compare` lines 92–100 (raw exact-match pool) and 119–123 (node field Counter).

**N_FIELD_ORDER_BINDING.** A mapped record, with no declared field edits, changes:

```text
Local family | sc: q>0 | P(q) holds | sc: q<0 | R(q) holds
```

to:

```text
Local family | sc: q<0 | P(q) holds | sc: q>0 | R(q) holds
```

The tool reports `MECHANICAL PASS`, eight `EXACT`, zero pending. Each field's own hash is unchanged, but the typed scopes have changed association with the opaque statements. The Counter forgets field sequence and position. A record declaration alone must not authorize an undeclared rearrangement of qualified content. This is the original correct-home/association requirement, not a request to prove the formulas' truth.

**N_RAW_OWNER_BINDING.** The raw line `The preceding claim requires q>0.` is moved from immediately after `TEST-ALG-X` to immediately after `TEST-ALG-Y`, under the same heading, with an empty movement map. All bytes and heading hashes remain in the document. The tool reports four `EXACT`, zero pending, `MECHANICAL PASS`. The raw pool keys only text hash and heading context, not its qualified home, neighbors or sequence. Keeping unsupported text byte-identical is safe only if its binding is also preserved or the move is explicitly reviewed.

**Acceptance:** keep field occurrences/sequence and raw-region home or anchors in the mapping. Unexplained changes to their association fail; explicitly described rearrangements remain pending for review unless an exact, reviewed association-preserving transformation is checked. A fallback need not understand opaque science: conservatively require an unchanged contiguous qualified block or a mapped review obligation. Preserve inline edge bytes and all current positive cases. This does not require normalizing all Atlas records or adding a mathematical parser.

## 3. AP-R1 — the heading chain must follow actual heading levels

**Required. Location:** `extract` line 50.

**N_SKIPPED_LEVEL_SIBLING_CONTEXT.** For `# D`, then `### Branch A`, then `### Branch B`, the two level-3 headings are siblings. The current depth-as-list-length calculation gives the B node the chain `[D, A, B]`; the correct enclosing context is `[D, B]`. A Markdown file need not include every intermediate heading level. This is an extractor identity error even though the source bytes remain present.

**Acceptance:** track heading levels explicitly, pop all headings at a level greater than or equal to the incoming heading, and then push the new heading. Test skipped levels and siblings. Keep raw bytes as the identity source, and retain the now-passing non-ASCII and CRLF checks. If a heading layout is deliberately unsupported instead, fail it explicitly rather than emit an incorrect context chain.

## 4. AP-R3 — hard invariants must not depend on mapping-route choice

**Required for the documented contract. Locations:** the deletion shortcut at line 107, protected-node checks at 116–118, and insertion handling at 136–139.

**N_GRADE_DELETE_INSERT_ROUTE:** the same `TEST-ALG-X#1` changes from grade `ALG` to `THM`. A direct record mapping fails, correctly. However, declaring deletion of the old occurrence and insertion of the new occurrence returns `MECHANICAL PASS` with two `DECLARED_PENDING_REVIEW` rows.

**N_DIAGNOSTIC_DELETE_INSERT_ROUTE:** the same `F1#1` changes from `D-PROOF` to `D-LINK` through the same route, again returning `MECHANICAL PASS` with two pending rows.

These are **not silent EXACT preservation**: the pending status is visible, and must not be misreported as scientific adoption. Nevertheless design §7 and the tool's own contract say a changed grade/qualifier or diagnostic class always FAILs in pure compaction. Enforce that invariant for surviving protected identities before dispatching map operations, including delete+insert. A declaration cannot convert a required stage-1 change into an ordinary compaction review item. Do not ban legitimate explicit deletion or exact-duplicate-to-reference accounting; the two tests concern an identical protected key surviving with a changed grade/class.

## 5. Context-changing byte moves — record a separate review obligation

**O_CONTEXT_CHANGE_IS_ONLY_A_BYTE_MOVE** intentionally reproduces the documented behavior rather than counting it as a failed unit test. Moving an unchanged `TEST-THM-X` from a section `Only for q>0` to `All real q`, with an explicit record move, yields one `MAPPED_EXACT` and no pending fields. That is correct as a byte-movement description but is not an assertion that inherited scope survived.

Before the D3 release workflow treats a zero-pending report as sufficient, changed enclosing contexts must be reviewed separately or appear in a context-review queue. The report should expose the old/new context identities. `MAPPED_EXACT` may remain the byte-status label; no need to redefine every harmless same-context move as a failure. This clarification can be incorporated in the same implementation pass, not a separate policy or Methodology release.

## 6. One correction pass, then D3

Implement AP-R1/R2/R3 together, preserve the current 21 self-test expectations, and replay the attached 11 receiving controls. The independent script also retains the one explicitly classified context-movement observation, not a mathematical-equivalence verdict. Proposed comparator changes may add a review-obligation flag without weakening the safety expectations. No full owner campaign, new Atlas tag or renewed #113/#114 review is needed.

Evidence:

- `evidence/atlas/v0.11_design_receiving/check_rev1_contract.py` (SHA-256 `39b1441121c74f184428fcb302b04beeb87a2a0c4adb7321bd455258681554ea`).
- `evidence/atlas/v0.11_design_receiving/rev1_receiving_output.txt` (actual combined output and execution identity).
- Full local JSON report is reproducible with the command below; it records all base/candidate fixture text, exact file hashes, mappings and comparator rows.

```bash
python3 -I tools/atlas_preservation.py selftest
python3 -I evidence/atlas/v0.11_design_receiving/check_rev1_contract.py \
  tools/atlas_preservation.py /tmp/atlas-preservation-receiving.json
```

Use a fresh output path. The receiving script pins this reviewed implementation; on a successor change only the target identity pins after inspecting the code delta, not the fixtures or their meanings. Its current exit 1 is the expected record of five mismatches, not a tool startup failure.

**Continuation:** Atlas owner applies the bounded comparator correction; reviewer checks that delta and the unchanged controls; D3 pilot then supplies its explicit movement map, context-review obligations, and reviewed stage-1 baseline only if needed. Keep Method v0.3 separate and the PI's order 1 → 2 → 3. The 13-identifier classification need not be expanded into a global cleanup before D3.

**Reviewer lane text offered to the Atlas owner (only this reviewer's words):** Checked 10 November 2026, PR #202 head e71382d. Original tool byte identity verified; 21/21 self-tests independently pass. Receiving review on PR #203 identifies order/home binding, skipped-level heading context and delete/insert invariant-route cases (6/11 controls matched; one context-move observation separately recorded). Next: scoped correction/readback, then D3; no owner science or Atlas bytes changed. #113/#114 remain completed.

No producer file, Atlas/Method, owner DSN, pipe state, main, release tag or another co-owner's lane was modified by this review.