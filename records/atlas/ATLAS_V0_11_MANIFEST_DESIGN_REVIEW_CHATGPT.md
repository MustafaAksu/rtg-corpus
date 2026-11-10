# Atlas v0.11 preservation manifest — ChatGPT receiving review

**Date:** 10 November 2026. **Status:** [SESSION], NONCANONICAL tool review; no scientific adoption, compaction acceptance or merge authorization.
**Object:** PR #202 implementation revision 3, head `1f33166` (successor of rev.2 `ccc5c0a35d0c344b84a66993c7612955c2900506`).
**Decision:** **ACCEPT SCOPED for D3 mechanical-pilot use.** The two rev.2 compound-route residuals are discharged by source inspection and producer-recorded replay; no new blocking preservation-contract issue was found in the bounded delta. This is not scientific equivalence, Atlas adoption or compaction-release approval. The rev.2 REVISE record remains in Git history. The five preceding receiving mismatches are fixed: the current producer self-test gives 30/30 expected outcomes, and the unchanged preceding receiving suite gives 11/11 plus its separate observation. Two paired route checks expose (i) a changed-line route that drops the context-review obligation and (ii) one candidate field occurrence consumed twice. D3 preparation may continue; this revision is not yet accepted as its preservation gate.
**History:** the prior review at this fixed path remains in Git at `f80a4e884b2e372cbe25fd00fee1127a550b4f86`; the draft-0 review is at `134e420a3dc6722992da32487095f91280676260`. Their original scripts and outputs are unchanged. #113/#114 stay closed.

## 1. Sources, identity and actual execution

Read the complete current 246-line tool (including all self-tests), the revised design §8 and adjacent duplicate-classification material, the complete preceding receiving record and 11-control harness, and current CONVENTIONS in full. Compared the changed context, source-binding and field-consumption paths with the revision-1 source already inspected. No new full Atlas/owner read, full-Atlas extraction or owner-certificate campaign was performed.

[EV-BYTES / EV-HASH / EV-RUN] GitHub connector text was materialized locally and matched to its source identity before executing the unchanged tool under Python 3.13.5:

| File | SHA-256 | Git blob |
|---|---|---|
| `tools/atlas_preservation.py`, 23,354 bytes / 246 lines | `c6e6660b4d57c39a81bda9ad5c476db684ee74c962794a58cae2e1a9d5fed0e1` | `dda7d60000267442708e3030911f45223be03c6a` |
| Preceding `check_rev1_contract.py`, 8,063 bytes | `39b1441121c74f184428fcb302b04beeb87a2a0c4adb7321bd455258681554ea` | `66881e777f2d7ca9e2021d81c720c070c778da4a` |

Only the preceding harness's two target identity constants were reassigned **in memory**; neither its source nor its cases/expectations changed. Source materialization was byte-verified, not a rewritten implementation. Direct shell GitHub retrieval failed DNS; connector delivery and local execution remained available.

| Completed run | Observed result | Exit |
|---|---|---:|
| Current producer self-test, unchanged by reviewer | 30/30 expected outcomes | 0 |
| Previous receiving controls, cases unchanged | 11/11; separate context observation reproduced | 0 |
| Two new paired route checks | 2 positive matches; 2 negative mismatches | 1 for combined receiving runner |

Execution captured at `2026-11-10T07:23:46.949120+00:00`. Suite counts overlap and are not independent scientific results. The producer's full-Atlas identity result (1,427 EXACT) was not rerun here and remains source-reported.

## 2. Discharged preceding cases

- **AP-R1 heading construction:** explicit levels give D/B, not D/A/B, for skipped-level siblings. The preceding negative is closed.
- **AP-R2 original order/home examples:** two scopes swapped across two statements now fail without a reorder declaration; a declared reorder stays pending. The raw continuation cannot silently move from X to Y. The added undeclared record-order control also passes.
- **AP-R3 original delete/insert examples:** same-identity grade and diagnostic-class changes now fail before map routing. A declared duplicate-occurrence removal still becomes pending rather than a false grade failure.
- **Exact-byte context move:** the old/new heading contexts are exposed in `obligations.context_reviews`; the ordinary context-move positive passes.
- The producer changed its own prior moved-record positive to put the record after the raw line, so the raw line retains its anchor. This is consistent with the new rule, not a relaxation of the independent receiving expectations.

These results are accepted; the remaining findings do not reopen the five old counterexamples.

## 3. AP-R2 / context obligation: changed-line routing drops inherited scope

**Location:** `compare`, lines 124–130 versus 131–156. Context comparison is performed only when the entire mapped line has an identical SHA-256. Field comparison of a nonidentical node line does not record its enclosing-context change.

**Paired positive P_EXACT_CONTEXT_QUEUE.** Move `TEST-THM-X THM | P(q) holds | @TEST§1` from `## Only for q>0` to `## All real q`, with an explicit record mapping. The report correctly gives one MAPPED_EXACT and one context obligation with the two different context chains.

**Negative N_WHITESPACE_CONTEXT_BYPASS.** Make the same move and change only the space after `THM` from one to two. All scientific field bytes remain equal. The whole-line hash differs, so the comparison enters the field path and reports:

```text
MECHANICAL PASS {'EXACT': 5}
obligations = {'pending_review': 0, 'context_reviews': []}
```

The inherited scope changed exactly as in the paired positive, but the formatting change suppresses its review obligation. This is a false clean preservation signal, not a request that the tool prove the theorem or interpret the heading's mathematics.

**Required correction:** determine changed context/anchor once for every matched source/target region, independently of whether line bytes are equal, fields are exact, or some field edit is pending. A changed inherited context must either fail or retain its explicit old/new review obligation. The byte-status label may stay EXACT at field level; it must not erase the enclosing-context obligation.

## 4. AP-R2 / occurrence accounting: one target field consumed twice

**Location:** `compare` lines 135–156. Exact field matching consumes a position via `tfree`; declared replacement matching decrements only `tpool`. The same candidate position remains free for a later exact match. Its Counter then becomes negative, and the final `range(n)` loop does not report that as a failure.

Source fields inside one record:

```text
local | sc: q>0 | sc: q<0 | @T§1
```

The map declares **only** an edit of the first scope, `sc: q>0` to `sc: q<0`; it declares no deletion or deduplication.

**Paired positive P_DISTINCT_REPLACEMENT_OCCURRENCES:** candidate has two separate `sc: q<0` occurrences. The pending edit and the unchanged second scope can legitimately use distinct targets. The current result is MECHANICAL PASS, four EXACT and one pending edit.

**Negative N_REPLACEMENT_TARGET_DOUBLE_USE:** candidate has only **one** `sc: q<0` occurrence. It is consumed first as the replacement target and again as the exact unchanged second scope. The tool returns the **same report counts** as the positive: MECHANICAL PASS, four EXACT and one pending edit, with no missing-occurrence failure.

This case is not all-EXACT: the first scope edit is visibly pending. The defect is more specific: the report certifies the second source occurrence as EXACT without a distinct available target. One occurrence was removed without any corresponding removal/deduplication declaration.

**Required correction:** use one occurrence-consumption mechanism for exact matches and declared replacements, including ordered matching. Every selected target position is consumed once; a second use fails. Maintain consistent order bookkeeping and reject negative/inconsistent consumption counts. Legitimate two-target edits and separately declared deletions/deduplications remain reviewable; this does not ban equal field text.

## 5. Bounded completion and reproduction

Implement the two local corrections together. Preserve the now-passing 30 self-tests and 11 receiving cases. In the four paired controls, both positives must remain accepted within their stated review obligations; the whitespace/context case must fail or queue the correct old/new context, and the missing-target-occurrence case must fail. No global parser rewrite, new owner science, Methodology release or repeated historical compaction campaign is requested.

New evidence (under `evidence/atlas/v0.11_design_receiving/`):

- `check_compound_routes.py`: SHA-256 `b179a06e15e0234e3fa4ad46a62264a5707740cc68656bad4a84fadf8325ee4a`. Replays the unchanged suites and the four paired cases, with hash-pinned inputs.
- `rev2_receiving_output.txt`: SHA-256 `264c36d258e2993812bc959dc10f45fe7fd2cf06319cdea9e9a79ddc661be6ce`. Actual combined stdout, not an inferred or producer-reported result.
- Detailed base/candidate text, movement maps and comparator reports are generated into the new output directory. The current receiving exit 1 denotes the two unmet expectations, not a runtime failure.

```sh
python3 -I evidence/atlas/v0.11_design_receiving/check_compound_routes.py \
  tools/atlas_preservation.py \
  evidence/atlas/v0.11_design_receiving/check_rev1_contract.py \
  /tmp/atlas-preservation-rev2-readback
```

Use a new output directory. When evaluating a successor, inspect its delta and update only the tool identity pins; retain cases and expectations.

**Continuation:** D3 classification and movement-map preparation may continue, but do not treat this comparator as its accepted gate yet. Keep the two residuals in this existing PR/review cycle. Method v0.3 stays separate. Prior accepted working-memory/reporting work and #113/#114 are not reopened.

**Reviewer checkpoint offered for the owner to install verbatim:** Checked 10 November 2026, #202 ccc5c0a. Tool hash/blob verified; current self-test 30/30 and unchanged prior receiving controls 11/11 independently pass. Five preceding mismatches closed. PR #203 records two residual compound-route cases: context obligations disappear on a whitespace-edited moved node; declared replacement and exact matching reuse one target field. New paired controls: two positives pass, two negatives mismatch. Next: one local correction/readback before D3 gating; preparation may continue. No Atlas or owner science changed.

No producer source, Atlas/Method, owner DSN, pipe state, main, release tag or another co-owner's lane was modified by this review.


## 6. Revision-3 bounded readback — 10 November 2026

**[SESSION] Object:** PR #202 head `1f33166`; tool SHA-256 `6a4047b0dd3e10e15feeb9262d8b09816e82fa2f85a6d7ce939cc69d580e1d62`, Git blob `927a1420422a39ebc229e22c4114b58ba05e67aa`.

The inspected delta from `ccc5c0a` is one commit. It changes only `tools/atlas_preservation.py`, the design record, and rev.3 evidence. The two requested routes are corrected directly in the source:

1. **Context/anchor is route-independent.** For every declared base/candidate pair, context and raw-anchor differences are computed before line-byte comparison. The resulting obligation survives both MAPPED_EXACT and edited-record paths; an edited-and-moved node also receives a DECLARED_PENDING_REVIEW row.
2. **Target-field occurrences are consumed once.** Exact and declared replacement matching now use the same `take()` routine with one free-position array and shared order pointer. A target occurrence selected as a replacement cannot later satisfy an exact source occurrence.

[EV-SRC-READ / EV-SRC-REPORTED] The producer's rev.3 evidence records: self-test **33/33**, unchanged prior receiving controls **11/11**, four compound-route checks **4/4**, combined exit 0, and atlas-v0.10 identity comparison **1,427 EXACT** with no context review. The recorded rev.3 runner changes only the tool identity pins from the reviewer's prior harness.

[EV-NOT-RERUN] In this readback the reviewer did **not** independently execute those Python suites: the local shell could not resolve github.com and the connector does not materialize repository files into the execution environment. The decision therefore rests on inspected source delta plus producer-run evidence; it must not be relabelled EV-RUN by this reviewer.

**Disposition:** **ACCEPT SCOPED** as the mechanical gate for the planned D3 pilot. The tool still proves only byte/accounting properties. Every DECLARED_PENDING_REVIEW item and every `obligations.context_reviews` item remains a mandatory change-focused review obligation; MECHANICAL PASS is not semantic equivalence.

**D3 entry condition:** use a frozen base, explicit movement map, comparator report with zero FAIL, and enumerate all pending/context obligations. Any grade/qualifier/identity/diagnostic-class change belongs to a separately reviewed stage-1 baseline. If the real pilot exposes a new route not covered by this contract, record it as a bounded tool issue rather than weakening an invariant.

**Reviewer checkpoint offered to the owner to install verbatim:** Checked 10 November 2026, PR #202 head `1f33166`. Revision-3 source delta inspected; the two rev.2 compound-route residuals are closed. Producer evidence reports self-test 33/33, prior receiving 11/11 and compound routes 4/4, exit 0; this reviewer did not rerun them because the local shell lacked GitHub network materialization. Verdict: ACCEPT SCOPED for the D3 mechanical pilot, not semantic equivalence or Atlas adoption. Next: D3 frozen-base pilot with zero FAIL and every pending/context obligation reviewed; Method v0.3 remains separate.
