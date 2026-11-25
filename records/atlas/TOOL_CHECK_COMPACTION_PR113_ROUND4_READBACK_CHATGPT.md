# PR #113 — round-4 receiving readback

**Date:** 10 November 2026. **Reviewer:** ChatGPT, Atlas co-owner.
**Status:** [SESSION] tool receiving review; neither scientific adoption nor merge authorization.
**Decision:** **ACCEPT SCOPED — no blocking finding in the requested correction.** The remaining CCP113-R2 metadata-source cases are discharged; the earlier history-boundary, source/destination-binding and default-profile controls still give the expected outcomes. No further correction round is requested for this scope.
**Object:** PR #113 head `70e9e3a3924325d263100658b083cf14e5c106d9`.
**Prior record:** `records/atlas/TOOL_CHECK_COMPACTION_PR113_ROUND3_READBACK_CHATGPT.md`, at receiving PR #114 head `1efd709accfb1ac75cd033ad97f3ce8f2e822eba`. That record and every earlier script/output remain unchanged. This record is the receiving disposition for the round-4 object, not a retrospective PASS for earlier bytes.

## 1. Reading, identities and exact delta

Read the complete 816-line round-4 checker, the unchanged complete producer fixture module, both earlier receiving harnesses and the four-case metadata harness. Re-read the round-3 acceptance criteria, current CONVENTIONS (including working-memory §9), the producer's round-4 README and the relevant source-region code. This is a change-focused tool review, not an Atlas or owner-science rereview.

[EV-BYTES / EV-HASH] Authorized GitHub content was materialized locally and its Git blob identity matched before execution. The checker was not rewritten or patched. The previously supplied metadata-harness file was likewise matched to its repository blob. Shell GitHub access failed DNS; no clone or full historical corpus is claimed. Python 3.13.5 was used.

| Object | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| Round-4 checker | 41,255 | `d2977b3e24fd54a1d85fe53ea88f65dd51a9e26890b56b17ab5855716b57d87c` | `623e103b147c2e060ad3c5efce1d6da7602d0765` |
| Producer fixture module | 9,422 | `45c3cbb5d28d550f2ddae00620b4c759c6aefa51384588c87b6977f951f78ec7` | `225ee26ff32681d47082e0d6222ee72c79161b36` |
| Original receiving harness | 6,244 | `831f262c0a30fd4d2ee4716a9a02f6d53114e1963380090bb7e45eb448458dd1` | `e05f07c7853d99803454acac1871957e08f96a1c` |
| Round-2 binding harness | 5,105 | `066265928741f44b9c411bcf32ccf73f41729b0f2e1c092787798b9af4314935` | `8bc3ccb8f155fcd884baafa689339db9b4f2d61b` |
| Round-3 metadata harness | 6,145 | `7366e17a7db3159846f58ad0f4a23d6e8465add1d2e0785b194b4bf78b9e1c29` | `d912486a835ae14ba313864217687a0951f8ccff` |

**Delta bound:** reversing only the added metadata-operation rejection, the live-occurrence count substitution and its docstring change restores the exact round-3 checker SHA-256 `afcfe064a178d90a3557629c530b60a41c376990b01a4b9451c0bd83e1f3e3ae`. Thus the rest of the checker, including destination and default-profile logic, is byte-unchanged. The fixture hash is unchanged.

## 2. Executed results

[EV-RUN / independent execution, same test implementations] Test cases and expected outcomes were unchanged. Only `CHECKER_SHA256` in the round-3 metadata harness was reassigned in memory by the hash-checking wrapper; its source file and fixture pin were not edited.

| Suite | Observed | Exit |
|---|---|---:|
| Producer profile | 19/19 expected outcomes | 0 |
| Original receiving, current fixtures | 7/7 expected outcomes | 0 |
| Round-2 binding | 3/3 expected outcomes | 0 |
| Round-3 metadata-source pairs | 4/4 expected outcomes | 0 |

Counts overlap; these are 33 executed case outcomes, not 33 independent mathematical results or an exhaustive proof of the checker.

The two metadata negatives now fail at `source hashes preserved in live text` with an invalid declaration on the HEADER/FOOTER operation:
- `N_HEADER_AUTHORIZATION`: expected FAIL, observed FAIL, checker exit 1.
- `N_FOOTER_AUTHORIZATION`: expected FAIL, observed FAIL, checker exit 1.
- `P_HEADER_LIVE_DECL` and `P_FOOTER_LIVE_DECL`: expected PASS, observed PASS, checker exit 0. Metadata cleanup is still permitted when the actual live deletion carries the declaration.

`N_WRONG_OPERATION` and `N_FOOTER_TARGET` continue to FAIL; `P_DECLARED` continues to PASS. The existing history-region, RID and default-profile tests remain satisfied.

**Execution custody:** two combined host-command attempts hit wall-clock limits. No interrupted suite was scored. Completed producer/receiving/binding outputs were retained, and the metadata suite was completed separately with the unchanged harness. The committed receiving output explicitly distinguishes these execution windows and contains each completed suite's actual stdout and exit. The old date fields inside unchanged harness-generated JSON are historical fixture metadata, not this run's date.

## 3. Scope of acceptance and remaining limitations

The revised gate rejects declarations on `replace-header` and `replace-footer`. Other declarations require a net removal counted only at eligible source occurrences after the header, outside the parsed history region and off footer lines. The target remains the parsed candidate history region, not its footer. This addresses the requested source-region contract and the four paired controls without weakening test expectations.

[EV-SRC-REPORTED / EV-NOT-RERUN] The producer's round-4 README reports eight historical regression executions, exit 0 and byte-identical outputs. They were not rerun by this reviewer. The producer explicitly did not rerun the OFN v0.11 campaign in round 4 because the inputs were unavailable; this reviewer did not rerun it either. Earlier OFN results must not be relabelled as round-4 execution. No scientific certificate campaign was run.

Known parser/profile limits remain: regular-expression discovery, incomplete namespace coverage and no proof of unrestricted prose equivalence. In particular this DSN checker is not an Atlas typed-record preservation checker. These are documented limits, not newly imposed #113 gates. Acceptance is not a claim of universal checker completeness or of preservation of an as-yet-unbuilt Atlas candidate.

## 4. Reproduction and evidence

New files in `evidence/atlas/tools/pr113_receiving_chatgpt/round4/`:
- `replay_metadata_round4.py`: 1,439 bytes; SHA-256 `dcc322372e1c31bb9dcb6a37e4e86857dbfc48b08dbf7858e7256b98458d4ecd`.
- `receiving_output.txt`: 8,148 bytes; SHA-256 `eeca79a113feb25caf667b88dc3f76cc57b76ffc34f3c77e33e9c3f4d3230b1e`.

With the pinned checker and fixture together in a temporary directory (the producer suite locates its checker next to itself), and the existing receiving files available from PR #114:

```bash
# TOOL_DIR contains byte-verified round-4 check_compaction.py and its unchanged fixture.
# R is the existing receiving evidence directory from PR #114; OUT is a fresh output directory.
python3 -I "$TOOL_DIR/test_check_compaction_profile.py"
python3 -I "$R/test_pr113_receiving.py" --fixtures "$TOOL_DIR/test_check_compaction_profile.py" --checker "$TOOL_DIR/check_compaction.py" --report "$OUT/original.json"
python3 -I "$R/round2/test_pr113_round2_binding.py" --fixtures "$TOOL_DIR/test_check_compaction_profile.py" --checker "$TOOL_DIR/check_compaction.py" --report "$OUT/binding.json"
python3 -I "$R/round4/replay_metadata_round4.py" --harness "$R/round3/test_metadata_binding.py" --checker "$TOOL_DIR/check_compaction.py" --fixtures "$TOOL_DIR/test_check_compaction_profile.py" --out "$OUT/metadata"
```

The final directory must not already exist. The wrapper verifies all three input hashes, changes only the checker pin in memory and invokes the original main function. No prior evidence is overwritten.

## 5. Durable continuation and Atlas v0.11

**Held decision:** known CCP113-R1/R2 receiving blockers are discharged for `70e9e3a…`. #113 and #114 are ready for the PI's integration/merge decision at this scope; current-base mergeability is a separate repository operation. No merge, tag or force-push was performed by this review. If synchronization changes protected checker bytes, identify and review that delta rather than silently transfer this verdict.

**Next eligible action:** the Atlas owner may prepare the v0.11 preservation-manifest schema as a draft now, without waiting idly. It is not an accepted schema or an authorized Atlas publication. Keep the source snapshot frozen and the Method v0.3 delta separate. A bounded sample should cover RID and unnumbered records, conditional claims, typed edges with actual consumer pins, negative constraints, evidence/custody limits and unparsed content. Account for every source span; report unparsed fields as UNVERIFIED rather than treating empty extraction as preservation. Exact qualified duplicate-to-pointer mappings require one surviving live home.

A structured before/after comparison must be tied back to raw record spans and hashes; the same parser omitting a field twice is not proof that field was preserved. The approximate half-size target is advisory. This is preparation for the PI-selected order 1 (tool) -> 2 (Atlas compaction) -> 3 (one dormant-owner advisory), not a new #113 review cycle.

No production checker, owner DSN, adopted Atlas/Method, source tag or pipe item was modified by this receiving review. Previous records and original tests/outputs remain intact.
