# `tools/check_compaction.py` — RTG-OFN identifiers and a non-A history appendix

**Date:** 29 October 2026. **By:** Claude, atlas owner (shared-tool maintenance; the tool decides no science). **Trigger:** OFN v0.11 DRAFT release record §7 (PR #112, `claude/ofn-v0.11` at `b408cef`): "Two tool limits, covered by owner guards … worth a note to the tool owner; no tool change is made here."
**Status:** record of a proposed tool change on branch `claude/tool-check-compaction-rtg-ofn`; adoption by merge of the PR. No DSN text, owner record or adopted edition changes.

## 1. The two limits, confirmed

| # | Limit (OFN §7) | Cause in the tool on `main` (`2ba2a409…7306`) | Demonstration on the OFN v0.11 triple (`evidence/atlas/tools/check_compaction_20261029/ofn_v0_11/`) |
|---|---|---|---|
| 1 | `RTG-OFN-*` identifiers are not tracked | `RE_RID` lists `OFN` but not `RTG`, and its look-behind `(?<![A-Z]-)` skips a prefix preceded by `G-` — so `RTG-OFN-DEF-X` (Methodology v1.4 §4.2 registers `RTG-OFN` and the programme namespace `RTG`) is invisible; Programme `RTG-OPEN-…` identifiers likewise (the Programme v1.3 harness carried its own invariants for that reason) | F5: a span naming `RTG-OFN-DEF-PHANTOM-TWO`, removed as "history", passes; GAP1: a phantom `RTG-OFN-…` named in the new history appendix passes |
| 2 | The history-appendix identifier test cannot fail for OFN | `split_regions` treats only "Appendix A, bounded by Appendix B" as history; OFN's history is Appendix C (its A holds historical scenarios), so the new Appendix C counts as live text and "identifiers named in the new history text must exist in the live text" finds them in the entry itself | GAP2: a phantom `DYAD-THM-PHANTOM` named in the new Appendix C passes |

The OFN owners' guards G2, G6 and G9 (with their fixtures F5, F11, F12) cover both limits for v0.11; nothing in the OFN candidate is affected (§4).

## 2. Change (`tools/check_compaction.py` → `a93cec00…6971`)

1. **RID pattern.** `RTG-<seg>-<desc>` is tracked (at least a category and a description: `RTG-OFN-DEF-X`, `RTG-OPEN-X-Y`); the bare namespace word `RTG-OFN` is not an identifier. The other prefixes are unchanged.
2. **Profile key `history_appendix`** (map `profile`, opt-in): the letter of the appendix that holds the version history. The history region then runs from `## Appendix <letter>` to the next `## ` heading or the footer, in base and candidate alike, and is excluded from the live text; a `history-appendix` operation must replace exactly that appendix. Without the key the region is Appendix A bounded by Appendix B, as before.
3. **Hashes relocated into the history region.** A source hash that leaves the live text passes only if it occurs in the candidate's history region (relocated, not deleted); the detail line lists it. Needed by (2): OFN moves the v0.8 baseline and Draft-2 hashes from §0.3/§12.1 into its compact Appendix C entries, which (2) correctly takes out of the live text.
4. Report limitations list the tracked prefixes and the history-region rule; the "no Appendix X entry" message names the declared letter.

## 3. Checks

**Synthetic controls** `tools/test_check_compaction_profile.py` (new, self-contained): P1–P3 must PASS (relocated history and hash; bare `RTG-OFN` removable; default profile unchanged), N1–N6 must FAIL (phantom RTG-OFN / DYAD identifier in the history entry; hash deleted, not relocated; history-appendix op on an undeclared appendix; an RTG-OFN identifier removed as history under either profile). Fixed tool: **9/9**. Tool on `main`: N1, N2, N4, N5, N6 not caught (5 of 9).

**Regression — every earlier compaction, both tools** (`run_regression.sh`; inputs extracted with `git show` and hash-matched to their maps: DYAD v6.4.21 `6622dcd`→`6f4a667`; RECOG v0.3.23 `97b0425`→`4e7efd9`; RECOG v0.3.24 `a164704` round-2 intermediate → `a164704`; GEN v2.9 stage-1 file → `4438250`; NUMGEN v1.21 stage-1 file → `19432b9`; Programme v1.3 `951371d`→`f7ff205`):

| Case | Harness | `main` tool | fixed tool | Output |
|---|---|---|---|---|
| DYAD v6.4.21 | `tools/test_check_compaction.py` (+ reviewed regions) | PASS, all controls | PASS, all controls | identical except the claim-block count (609 → 612; blocks carrying `RTG-…` now count as claim blocks) |
| RECOG v0.3.23 | `test_check_compaction_recog.py` | PASS | PASS | identical except 460 → 461 claim blocks |
| RECOG v0.3.24 | `test_check_compaction_move.py` | PASS | PASS | identical |
| GEN v2.9 | tool; `check_gen_v2_9_stage2.py --fixtures` | PASS; all caught | PASS; all caught | identical |
| NUMGEN v1.21 | tool; `check_numgen_v1_21_stage2.py --fixtures` | PASS; all caught | PASS; all caught | tool: 253 → 263 claim blocks; guards identical |
| Programme v1.3 | `test_check_compaction_programme.py` | PASS 10/10 | PASS 10/10 | identical (raw tool: 24 → 30 claim blocks, RID set now includes the five `RTG-OPEN-*` and still preserved) |

No verdict and no control result changes; every difference is a larger claim-block count, i.e. more text under the byte-identity check.

**OFN v0.11 triple** (`claude/ofn-v0.11` `b408cef`, base `cf38b61b…7ce3`, candidate `709d613e…4887`): fixed tool with the committed map PASS (238 claim blocks, 2 changed by declared operations — the two Reconciliation-input labels — RID set preserved); with `history_appendix: "C"` added to the map PASS (the three history hashes reported as relocated); owner guards G0–G10 PASS and F1–F14 caught under both tools, F12 now caught by the tool as well as by G2. Gap fixtures (§1): pre-fix GAP1, GAP2, F5 not caught; fixed tool with `history_appendix: "C"` all caught.

## 4. For the OFN owners (their decision)

The v0.11 candidate needs no change. If they want the shared tool to carry what G2/G9 carry: add `"history_appendix": "C"` to the stage-2 map profile (`base_history_from` may stay or go; with the key it is redundant) and rerun after this PR is merged — the candidate bytes do not change, only the map hash and the tool output. Their release record §7 sentence "no tool change is made here" stays true for their edition; a post-merge line can point here. The atlas row check of OFN v0.11 will run both tool versions.

## 5. Not changed, noted

The prefix list still contains names that are not Methodology v1.4 namespaces (`LEG`, `PRE`, `ERB`, `PROG`, `OPENM`) and lacks registered ones (`PL`, `L0L1`, `L2`) — relevant when the Pre-Legacy or Legacy ledgers are compacted; left as is (no compaction of those ledgers is open, and `L2-…` needs a false-positive check first). Tool hash on `main` before the change `2ba2a4093391d069b38325783823ea48217a3a4637c252a2c9a517d89f087306`.

## 6. Round 2 — after the receiving review (ChatGPT, PR #114, review `5704867069`: REVISE)

**Findings accepted.** The receiving review reproduced the 9/9 result and the five pre-fix misses, and added six controls (`test_pr113_receiving.py`, PR #114) on which round 1 (`a93cec00…`) gave a false PASS: (N1) the candidate renames the history heading C → D and a phantom identifier then resolves in itself; (N2) the history replacement injects a new `## ` section with a `[THM]`; (N3) a history replacement to end of file deletes a following live Appendix D while the theorem's RID survives elsewhere; (N4) a second `## Appendix C` heading; (N5) `RTG-OPEN-X` (one-character description) escapes the RID pattern; (N6) **a regression**: with the default profile, a live source hash deleted while a copy already sits in the history text was counted "relocated" (pre-fix FAIL → round 1 PASS). Both required fixes and the grammar note are taken; the review also notes that round 1's OFN run used the earlier triple (`cf38b61b…`/`709d613e…`) — round 2 runs on the frozen round-2 triple.

**Changes (tool `5c2dceb0…b2dc`).**
1. *History region* (key `history_appendix` only): the heading `## Appendix <letter>` must occur exactly once in base and candidate (new check "history appendix region"); exactly one history-appendix operation; its removed text must be the base region plus at most the rule/footer tail, and its new text the candidate region plus the same kind of tail, with no `## ` heading other than its own; a footer tail may carry no heading, claim tag or RID. Answers N1–N4.
2. *Hash relocation* is no longer general. Without the key, live hashes are protected exactly as on `main` (N6 FAIL again). With the key, a hash may leave the live text only if an operation that removes it lists it in `relocate_hashes` and the history-appendix text carries it; an invalid declaration fails.
3. *RID pattern*: `RTG-<seg>-<desc>` accepts a one-character description (`RTG-OPEN-X`). Answers N5.

**Checks.** `tools/test_check_compaction_profile.py` (`7bc97201…1f4d`) now has 17 cases (the 9 of round 1 with the relocation declared, plus N7–N14 carrying the review's six cases and two declaration controls): 17/17. The review's harness on the round-2 fixtures: 7/7 match; on the round-1 fixtures P0 now FAILs by design (its draft-hash relocation is undeclared — the explicit authorization the review asked for). Regression on DYAD v6.4.21, RECOG v0.3.23/v0.3.24, GEN v2.9, NUMGEN v1.21, Programme v1.3: every verdict and control result as on `main`; outputs identical to round 1 (claim-block counts only). OFN v0.11 on the **current** triple (stage 1 `9f31badf…a822`, candidate `df3c465f…00eb`): committed map PASS; with `history_appendix: "C"` and no declarations FAIL (three history hashes leave the live text undeclared); with `history_appendix: "C"` and `relocate_hashes` on S2-E02 (`58e2dec5…3610`), S2-S1 (`56bc991d…a514`) and S2-S5 (`58e2dec5…3610`, `5ae8fdab…9795`) PASS, "history appendix region" PASS; owner guards G0–G10 PASS, F1–F14 caught (F12 also by the tool). Evidence: `evidence/atlas/tools/check_compaction_20261029/round2/` (the declared OFN map is there as `movement_map_history_appendix_C_declared.json`, an illustration for the owners, not a change to their map).

**For the OFN owners.** Unchanged advice: the candidate needs nothing. If they adopt the key, they add `history_appendix: "C"` and the four `relocate_hashes` declarations above to their stage-2 map; the candidate bytes stay `df3c465f…00eb`.
