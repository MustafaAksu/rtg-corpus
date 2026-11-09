# PR #113 — round-3 receiving readback

**Date:** 9 November 2026. **Reviewer:** ChatGPT, Atlas co-owner.
**Status:** [SESSION] tool review, not scientific adoption or merge authorization.
**Decision:** **REVISE, narrowly confined to CCP113-R2 source-region binding.** Both named round-2 counterexamples are fixed, but header/footer declarations still authorize a different, undeclared live deletion. No broad tool redesign or owner-science campaign is requested.
**Object:** PR #113 head `74ca65eacf9e6a516776aaebd45a4513f74b230f`.
**Prior receiving record:** `records/atlas/TOOL_CHECK_COMPACTION_PR113_RECEIVING_REVIEW_CHATGPT.md` §6, at PR #114 head `b977b8aaff73f301c4d1692f91368e7c533e8c7a`. That historical record is unchanged. This readback is the latest disposition for the round-3 object.

## 1. Reading and execution identity

Read the complete 798-line checker, complete current producer fixture module, both unchanged receiving harnesses, the producer record (especially §7), prior receiving record §6, the round-3 commit changes, current CONVENTIONS, adopted Methodology v1.4 §§12.4 and 13.1–13.6, and Atlas Method v0.2 §§1–7. This is a bounded tool readback, not a complete scientific review of the Atlas or its owners.

[EV-BYTES / EV-HASH] Source text was obtained through the authorized GitHub connector, materialized locally, and checked against the GitHub Git-blob identity before execution. No implementation was rewritten for the replay. Python 3.13.5; all fixture work was in temporary/local directories. Direct shell access to GitHub failed DNS; a repository clone was not used.

| Executed file | SHA-256 | Git blob |
|---|---|---|
| `tools/check_compaction.py` (40,107 bytes) | `afcfe064a178d90a3557629c530b60a41c376990b01a4b9451c0bd83e1f3e3ae` | `e61d67cc6985832c8f814ec39279dc7ccd41849a` |
| `tools/test_check_compaction_profile.py` | `45c3cbb5d28d550f2ddae00620b4c759c6aefa51384588c87b6977f951f78ec7` | `225ee26ff32681d47082e0d6222ee72c79161b36` |
| Original receiving harness | `831f262c0a30fd4d2ee4716a9a02f6d53114e1963380090bb7e45eb448458dd1` | `e05f07c7853d99803454acac1871957e08f96a1c` |
| Round-2 binding harness | `066265928741f44b9c411bcf32ccf73f41729b0f2e1c092787798b9af4314935` | `8bc3ccb8f155fcd884baafa689339db9b4f2d61b` |

## 2. Actual results

[EV-RUN] The existing tests and expected verdicts were not changed:

| Suite | Observed result | Process exit |
|---|---|---:|
| Producer profile suite | 19/19 expected outcomes | 0 |
| Original receiving suite using current fixture module | 7/7 expected outcomes | 0 |
| Unchanged round-2 binding suite | 3/3 expected outcomes | 0 |
| New paired metadata-source controls | 2 positive matches; 2 false-positive negatives | 1 |

Specifically, `N_WRONG_OPERATION` and `N_FOOTER_TARGET` now FAIL as required, and `P_DECLARED` passes. R1's history-boundary repairs, the single-character RID case and the default-profile hash guard remain passing regressions. Suite counts overlap; they are not 29 independent mathematical results.

[EV-NOT-RERUN] The six historical stream harnesses, full OFN triple/owner guards and scientific certificates were not independently rerun. Their round-3 results remain producer-reported. No demonstration of a defect in an adopted OFN or Atlas document is made.

## 3. Remaining CCP113-R2 case: metadata is outside live text

**Location:** round-3 checker integrity block, `at = BASE_TEXT.find(gone)`, `in_hist`, and `ok` in the `relocate_hashes` loop (approximately lines 372–388). The checker excludes the history operation and a span starting in history, but does not exclude the header or footer. Its own `live_text` explicitly excludes both.

The previous acceptance criterion already said a header/footer replacement must not authorize an unrelated live deletion (prior receiving record §6.2). This is a remaining source-region case of that contract, not a demand for unrestricted semantic equivalence.

**N_HEADER_AUTHORIZATION — expected FAIL, observed PASS/exit 0.** Add the same draft hash to a metadata line in the base header. Delete the actual live draft paragraph without `relocate_hashes`. Remove the header metadata line with `replace-header`, placing the declaration on that header operation. The candidate history correctly contains the hash. All checks PASS, including source-hash preservation: the header net removal has incorrectly authorized the separate live removal.

**N_FOOTER_AUTHORIZATION — expected FAIL, observed PASS/exit 0.** Put the duplicate draft hash in the base footer. Delete its live paragraph without a declaration; retain the hash in the actual candidate history. Strip the footer duplicate using `replace-footer` with the declaration attached there. Again all checks PASS. This differs from the now-fixed `N_FOOTER_TARGET`: the destination is legitimate history, but the authorizing source operation is the footer.

**Paired positives:** `P_HEADER_LIVE_DECL` and `P_FOOTER_LIVE_DECL` make the same metadata edits but attach the declaration to the live paragraph's actual removal. Both PASS. The defect therefore is not a ban on metadata cleanup or on legitimate hash relocation.

**Required local correction:** bind each declaration to an actual net removal in an eligible live source span, excluding header, history and footer regions. At minimum the two metadata operation types must not grant that permission; validate the source span rather than inferring live membership from being outside the history appendix. Keep the existing parsed-history destination test and default-profile behavior.

**Acceptance:** both new negatives FAIL while their paired positives and the existing 19 + 7 + 3 suites retain expected outcomes. No new owner certificate campaign. Do not weaken the assertions or relabel the metadata source as live to pass the tests.

## 4. Reproduction

New test: `evidence/atlas/tools/pr113_receiving_chatgpt/round3/test_metadata_binding.py`, SHA-256 `7366e17a7db3159846f58ad0f4a23d6e8465add1d2e0785b194b4bf78b9e1c29`. It pins the current checker and fixture bytes; when reviewing a successor, update only the target identity pins, not the cases or expectations.

```sh
python3 -I tools/test_check_compaction_profile.py
python3 -I evidence/atlas/tools/pr113_receiving_chatgpt/test_pr113_receiving.py --fixtures tools/test_check_compaction_profile.py --checker tools/check_compaction.py --report /tmp/pr113-original.json
python3 -I evidence/atlas/tools/pr113_receiving_chatgpt/round2/test_pr113_round2_binding.py --fixtures tools/test_check_compaction_profile.py --checker tools/check_compaction.py --report /tmp/pr113-binding.json
python3 -I evidence/atlas/tools/pr113_receiving_chatgpt/round3/test_metadata_binding.py --fixtures tools/test_check_compaction_profile.py --checker tools/check_compaction.py --out /tmp/pr113-metadata-new
```

Use a fresh output directory for the last command. Actual combined stdout: `round3/receiving_output.txt` in the same evidence tree. It reports the process exit codes explicitly. The unchanged round-2 harness retains its historical `review_date` field; execution of it in this readback occurred on 9 November, not 30 October.

## 5. Atlas continuation checkpoint and scope of the next stage

The PI selected order **1 → 2 → 3**: close the shared-tool readback, then prepare an Atlas compaction edition, then issue one batched advisory on dormant-owner issues. The priority decision is not merge/tag authorization.

**Resume:** tool owner repairs only the metadata-source case; reviewer replays the pinned suites above. PR #114 preserves the prior records and this continuation. No new independent review PR or repeated scientific campaign is needed.

**Compaction boundary:** closing #113 will not prove preservation of the Atlas graph. This checker is DSN-profiled: it recognizes DSN claim syntax, selected RID prefixes and DSN headers/footers. Atlas bare grade fields, `*STREAM:` records, typed edges, actual consumer pins and complete qualifier payloads need an explicit Atlas-aware preservation check and source/destination map. A generic RID set or same node/edge IDs alone does not prove unchanged statements, assumptions, domains, conventions, clocks, evidence states or negative constraints. This is a preparation requirement for stage 2, not an additional #113 blocker.

**Method proposal:** a compaction trigger and any satellite-scope clarification belong in a separately reviewed Method v0.3 delta; do not classify changed method semantics as layout-only Atlas work. Keep the source snapshot fixed during compaction; new owner editions are declared divergence for the later impact refresh. The approximate half-size target is advisory, not permission to remove load-bearing content. Moving detailed check logs into evidence must leave the current result, scope and evidence limitations visible at the relevant Atlas home.

No production checker, owner DSN, adopted Atlas/Method, source tag, pipe item or main branch was modified by this receiving review. Both PRs remain open; merge and adoption remain with the PI.
