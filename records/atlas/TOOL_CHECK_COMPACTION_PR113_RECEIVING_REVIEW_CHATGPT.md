# PR #113 — independent receiving review of the compaction checker

**Date:** 29 October 2026. **Reviewer:** ChatGPT, Atlas co-owner.
**Status:** [SESSION] / tooling review, not owner-science adoption.
**Object:** PR #113 at `740496b9d6d1f605ad9f8e125c41efd598338d3b`; base `b0dc6dbea3d9dc6ba148c7a1046bbfbeeebd0583`.
**Verdict: REVISE — two required fixes in one batch.** The two producer-reported defects are real and the proposed direction is useful, but the new history-region contract remains bypassable and the hash relaxation introduces a default-profile regression. No canonical DSN change is requested.

## 1. Evidence and actual execution

Read: the complete 722-line proposed checker; its complete 125-line new test; the complete checker diff; `records/atlas/TOOL_CHECK_COMPACTION_RTG_OFN_HISTORY_APPENDIX.md`; changed-file inventory; current `records/ofn/OFN_v0_11_RELEASE_RECORD.md` §7 at PR #112 head `e9b7e2a91aaa6c7a05233b0e114f69eb3adb1b1c`; repository `CONVENTIONS.md`.

The connector-delivered source was materialized locally and checked against GitHub Git-blob identities. The base was materialized using the inverse inspected diff and checked against both its recorded SHA-256 and GitHub blob identity. Thus the executed files are byte-identified source files, not independently rewritten checker implementations.

| Executed file | SHA-256 | Git blob |
|---|---|---|
| PR #113 checker | `a93cec005f3ce85b5d2cc4941c1595cbf0a31187b0a17806271f9327a0626971` | `8f53936f4d9fb5adb9514d6f06441b8c9da55187` |
| Base checker | `2ba2a4093391d069b38325783823ea48217a3a4637c252a2c9a517d89f087306` | `06ded2752c01ca55c707817b5a3de8a911dc1909` |
| Producer profile test | `e6c938a8f24ffdd0f998623595d7dc41ea382cbbe0409ca28f5ca4f5ced63d54` | `ca169444a6f307912c59e19853af417e1050515b` |

**EV-BYTES / EV-HASH / EV-CODE / EV-RUN:** producer tests independently replayed: proposed tool **9/9 expected outcomes** (3 positive, 6 negative); base misses **N1/N2/N4/N5/N6**, exactly as reported. This is an independent execution of the same fixtures, not an independent implementation of those fixtures.

**EV-INDEP / EV-RUN:** six additional synthetic negatives and one positive were authored and executed against both byte-identified tools. Every candidate is derived exactly from its declared map; base, candidate and archive hashes are recomputed correctly. These are not invalid-hash or unrelated mutation tests.

**EV-NOT-RERUN:** the six historical stream harnesses and the complete OFN build/owner guards were not independently replayed here. Their prior results remain producer-reported. The repository could be read through the connector, but a full local Git snapshot was not available; no all-corpus regression claim is made. No scientific certificate campaign was rerun.

## 2. Additional executed controls

Reproducer: `evidence/atlas/tools/pr113_receiving_chatgpt/test_pr113_receiving.py` (uses the unchanged upstream `tools/test_check_compaction_profile.py` as its synthetic base fixture, then applies independently authored mutations).

| Test | Expected | Base | PR #113 |
|---|---|---|---|
| P0: ordinary producer-positive fixture | PASS | PASS | PASS |
| N1: candidate renames C to D; history names phantom RID | FAIL | PASS | PASS |
| N2: history replacement adds a new live section with a new tagged theorem | FAIL | PASS | PASS |
| N3: history replacement consumes following live Appendix D and deletes its theorem; its RID reference survives elsewhere | FAIL | PASS | PASS |
| N4: second Appendix C makes the phantom RID self-resolve | FAIL | PASS | PASS |
| N5: history names synthetic `RTG-OPEN-X` absent from live text | FAIL | PASS | PASS |
| N6: default profile deletes a live proof-source hash paragraph; the hash already exists in Appendix A | FAIL | FAIL | PASS |

N1–N5 are residual gaps, not claimed to be newly introduced failures. **N6 is a new acceptance regression.** Test identifiers containing PHANTOM, ALPHA or BETA, and `RTG-OPEN-X`, are synthetic tokens, not proposed owner RIDs.

## 3. Required fixes

### CCP113-R1 — P1, required: validate the history region and operation boundaries, not a heading prefix

**Locations at reviewed head:** `tools/check_compaction.py` L86–102 (`split_regions`), L435–458 (`check_op`), especially L96–98 and L451–456.

`history_appendix` currently uses the first matching prefix, silently returns no history region when the candidate heading is absent, and does not reject duplicate headings. The operation check only tests `start.startswith('## Appendix C')`; it does not establish that the removed or inserted span is exactly the declared appendix.

Consequences reproduced by N1–N4:
- Rename the candidate heading C to D: the new history is counted as live; `DYAD-THM-PHANTOM` then validates against its own occurrence, recreating the reported tautology.
- Add `## 9. Added live claim` and a new `[THM] [RID: DYAD-THM-PHANTOM]` inside the replacement: the parser ends history at that heading and treats the injected claim as live; the operation returns PASS.
- Start at C with `end: null` when a live Appendix D follows: a tagged theorem in D is deleted. Keeping its RID in an earlier citation satisfies global RID-set preservation; the checker reports the lost claim as a declared change and returns PASS.
- A duplicate C heading gives the same self-reference failure.

**Acceptance criteria:** validate the profile value and one exact history heading in both base and candidate; missing/duplicate/ambiguous regions must fail closed. Bind the actual removed and inserted spans to the parsed history boundaries. Preserve following live sections; reject injected live sections. A terminal footer can be preserved or handled by a separately validated footer operation, but must not become an arbitrary tail exemption. N1–N4 must fail while genuine OFN C compaction remains accepted. Historical-region identification is still a reviewed profile decision, not semantic proof by the checker.

### CCP113-R2 — P1, required: scope hash-relocation permission explicitly; preserve default checks

**Location:** `tools/check_compaction.py` L313–319.

The replacement of `hb <= hc` by `not (hb - hc - hist)` is unconditional, including maps with no `history_appendix` key. It treats mere membership of a hash in candidate history as evidence that a live hash was relocated.

N6 has no history operation and no profile opt-in. A current proof-source paragraph contains the hash and the word `historical`; a duplicate already exists in Appendix A. Removing only the live paragraph is rejected by the base and accepted by PR #113, which reports the hash as 'relocated' although nothing was added or moved into history. This is a structural false-positive, independently of whether a reviewer can understand the lost prose.

**Acceptance criteria:** keep the old default live-hash invariant unless relocation is explicitly opted into and justified by the map. Authorize exact historical hash relocations by source/operation and destination, rather than blanket set membership; retain active evidence references. Record legitimate OFN baseline/Draft-2 hash movements explicitly. N6 must fail and the three valid OFN historical movements must still pass. A pre-existing history duplicate alone is not relocation authorization.

## 4. Nonblocking notes and scope

**CCP113-N1 (P2):** L49 requires at least two characters after the first RTG segment. Consequently synthetic `RTG-OPEN-X` is not tracked although the documented category/description grammar imposes no two-character minimum. `RTG-OFN-DEF-X` does match because its regex remainder is `DEF-X`. Add a single-character programme test or declare a defensible grammar limitation; keep bare `RTG-OFN` excluded. This is not an assertion that a current adopted owner uses the synthetic RID. The separately disclosed PL/L0L1/L2 gaps and legacy aliases need not expand this patch into a namespace migration.

**CCP113-N2 (execution identity):** the PR #113 record tests OFN at `b408cef`, intermediate `cf38b61b…7ce3`, candidate `709d613e…4887`. At this read, PR #112 has advanced to `e9b7e2a…`: intermediate `9f31badfa0e7a70a037c3ede3e7f55f852d09f2288508ef38edf343a5172a822`, candidate `df3c465fb79f049f686f07635d889613e8ab112895cdbcd5af7af029e97400eb`. The old runs remain valid for the old bytes; do not relabel them as checks of round 2. The final bounded receiving run should use the actual frozen triple. This observation does not request another scientific campaign.

**OFN boundary:** these are synthetic checker counterexamples, not demonstrated defects in either OFN candidate. The owner's G0–G10/F1–F14 safeguards remain separate evidence, not independently replayed in this review. No candidate-byte change follows merely from this tooling review. An OFN map adopting `history_appendix: C` and its report should identify the final accepted checker hash and be rechecked at that scope.

## 5. One correction batch and replay

Fix R1/R2 together; include N1 if convenient. Extend the existing test suite with the supplied negatives, retain the producer's 9 controls, and replay the six bounded historical harnesses plus the current OFN triple. Keep earlier outputs as historical evidence. Neither old PASS logs nor the presence of a movement map alone certifies the strengthened safety contracts.

Example execution after obtaining the upstream fixture and checker files (paths may point to separate checkouts):

```sh
python3 -I evidence/atlas/tools/pr113_receiving_chatgpt/test_pr113_receiving.py \
  --fixtures tools/test_check_compaction_profile.py \
  --checker tools/check_compaction.py \
  --report receiving_controls.json
```

On the reviewed PR #113 tool this exits 1 with six mismatches; after correction it should exit 0. Testing both old and reviewed checkers with repeated `--checker` gives 11 mismatches in total (5 old, 6 proposed). The recorded output is `evidence/atlas/tools/pr113_receiving_chatgpt/receiving_controls_output.txt`.

No production tool, OFN scientific text, adoption record or tag was changed by this review. PR #113 should not be merged as a completed closure of these checker gaps until R1/R2 are addressed.
