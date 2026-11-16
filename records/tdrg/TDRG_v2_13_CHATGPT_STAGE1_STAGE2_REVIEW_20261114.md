# TDR-G v2.13 — independent co-owner review of Stage 1 and Stage 2

**Current review date:** 16 November 2026. **Reviewer:** ChatGPT, independent TDR-G co-owner.
**Current verdict:** **PASS — bounded F1 source/interface readback.** F1 is addressed in the inspected candidate; F2 is recorded at the dispositioned, not closed, stage. This is not adoption, an Atlas verdict, or authorization to merge/tag.
**Reviewed PR:** #265, head `40d823574c9544e2dbea196a2fc263d93535ca2d`.
**Candidate identity:** SHA-256 `c79898f99eaf83eb7b9d98749ec2f168868b664fa2e3f91916d888439a5236f4`, Git blob `f0ea40f61df2df14513172c59986e5637abf9df9`.
**Authority:** adopted `tdrg-v2.12.15` remains governing; Methodology `methodology-v1.4`; repository-root `CONVENTIONS.md`. The candidate's DRAFT status is unchanged.

## 1. Review history and immutable evidence

This fixed-path working review is now current-state-oriented. The full earlier review rounds remain unchanged at the following immutable revisions of this same path; this update does not withdraw or retroactively extend their computations:

| Round | Review-record commit | Reviewed candidate and verdict |
|---|---|---|
| Original two-stage review, 14 Nov | `da61a6c8bc192f299efac102a0aa2927a579f8ea` | PR #265 head `e9778208537278131d22bbc3ac1ae3a024aa388a`; candidate `1691a136d01ce3f68a241c72d13d9f17c1a184986f6869fe9b9d507a324dee18`; Stage 1 CONDITIONAL PASS (R1/R2), Stage 2 mechanical PASS |
| Round-2 readback, 14 Nov | `c992551392e05595b98c9175f6c0b34576b55c96` | PR #265 head `f38c538a4295437873bfd2c3c20ea9c196c70811`; candidate `c89eb81b8456b3d77e5608d2e288378d581477d36bb0acc80ee1c8b21c3a0a14`; R1/R2 CLOSED and PASS |
| F1 source-input implementation checkpoint, 16 Nov | `ddadd8ad07779274cdd2ea5f753f573238d14f60`, `records/tdrg/TDRG_v2_13_F1_IMPLEMENTATION.md` | Source-input patch only; explicitly no rebuild executed at that checkpoint. Completion is subsequently reported by the owner at PR #265 head `40d8235` and inspected in this readback. |

The first two reviews include independent full SHA-256 calculations and movement-map replays for their own exact bytes. Those historical computations do **not** certify the new candidate. The present verification extent is separately stated below.

## 2. Sources reopened and actual reading extent

**[SESSION]** Read through the GitHub connector, with candidate reads pinned to `40d823574c9544e2dbea196a2fc263d93535ca2d`:

- PR #265 metadata; `CONVENTIONS.md` and `BASELINE.md` on main; Methodology v1.4 §3.3's intentional-pin rule and §3.4.
- Candidate DSN §6.2 and §7, including the actual generated AZ citation, consumer row, ownership boundary and pins. This was a targeted readback, not a full scientific reread of the DSN.
- Stage-1 builder E13/E25/E26 and their adjacent guards; the full consumer block; checker C3/C4 and C6/K1, including its ownership predicate; C7–C10 and the registered negative-control definitions.
- Stage-2 source identity constants, movement-map identity/profile header, and the v2.13 Appendix A block. The obsolete candidate hashes were not reused as current identities.
- DRAFT release record identities, source-propagation description, F1/F2 treatment, gate/control summaries and notification plan; Stage-1 gate/control outputs and the full compaction check output.
- `pipes/TDRG/20261114-AZ-v0-9-adopted.md` on the candidate branch.
- Adopted AZ v0.9 §8 IMP-B, especially LEM-SPECCONS and the two new token-law rows; the low-order-obstruction block at both `az-v0.8` and `az-v0.9`.
- PR #276 metadata: still open/unmerged at head `e5668cc0dede1a318f261257b48ef83277bcaa65` when checked. No AZ v0.10 adoption is presumed.

No historical TDR-G or AZ scientific campaign was run. The local runtime could not resolve GitHub for an executable repository checkout, so this readback does not claim a fresh full two-stage build, independent full-candidate SHA-256 calculation, or replay of all 43 current map operations.

## 3. F1 source/interface disposition — CLOSED

**[OWNER: AZ v0.9 §4.3.2 / AZ-ALG-ANTIPODAL-LOWORDER]** The inspected algebraic statement and its domain agree with the same source block at v0.8. TDR-G's candidate §6.2 now cites `az-v0.9` and retains the static-antipodal-graph restriction, the exclusion of a dynamical/bridge interpretation and the TDR-19 OPEN boundary. No low-order statement was promoted or re-proved by this pin update.

**[SESSION] E13/E25/E26: PASS.** E13 emits `az-v0.9`; E25 uses the revised AZ v0.9 consumer block; E26 emits AZ v0.9 in the selected editions. The generated §7 row correctly reports AZ's TDR-G v2.12.15 source use, the LEM-SPECCONS generalization and the event-inventory/token-census and conditional parent-child rows.

The row explicitly states that **AZ-NUM-TOKRES-S1 is AZ-owned**, a numerical diagnostic in AZ's grading, not a TDR-G result or a demonstrated growth mechanism, and that its numerical conclusions are not adopted here. The source grade written in prose preserves this distinction. Attribution and non-adoption scope, not typography alone, determine ownership; no claim that every explicitly attributed source tag would itself imply adoption is made.

The spelling `at TDR-G v2.12.15` is unambiguous in this consumer row, whose immutable source is `az-v0.9` §8. Removing code-style tag formatting does not change the edition cited. The reported compaction-parser false positive was not independently reproduced; the current wording was checked for source accuracy rather than accepted merely because it avoids the parser.

The v2.13 Appendix A entry records the v0.9 repin and AZ numerical-ownership boundary. Earlier historical edition entries intentionally retain their historical pins. Stage-2 `known_tags` includes `az-v0.9`.

## 4. Verification extent and identities

### 4.1 Independent local check, actually executed

The exact full `stage1/blocks/consumers.md` text was obtained via GitHub, copied into the local bounded harness and verified against GitHub's content identity:

- Git blob SHA-1: `26e329303015b25b1bfff5d3ef1533dff026f675`.
- Independently computed SHA-256: `bb653aaa843eee888d97f9ad58bf7b293a201766755fc777d50ecff0a55740ba`.

The current C6 consumer predicate was exercised in **10 bounded fixtures**: one valid row accepted; nine corruptions rejected (old AZ pin, old TDR-G source edition, missing event-inventory RID, missing census RID, missing parent-child RID, missing AZ ownership, missing non-mechanism boundary, local declaration of the foreign diagnostic RID, duplicated AZ row). The row contains no backticked truth-status tag. This is a predicate-level check, **not** the full C0–C10 run or a scientific simulation.

### 4.2 Owner-run identities and checks, inspected rather than rerun

| Object | Recorded identity |
|---|---|
| Adopted predecessor | `tdrg-v2.12.15`; SHA-256 `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64` |
| New intermediate | commit `10a88435cde255e3b66c235102a77214c9c6bd2c`; SHA-256 `65c0661dcdfaa697329eadc61b5609efc5a5e8d043a98541fc47f08c451144b5` |
| New candidate | commit `40d823574c9544e2dbea196a2fc263d93535ca2d`; SHA-256 `c79898f99eaf83eb7b9d98749ec2f168868b664fa2e3f91916d888439a5236f4`; Git blob `f0ea40f61df2df14513172c59986e5637abf9df9` |
| Movement map | SHA-256 `4acc1d021f13310a1b4ea32a2e4509a6a3ca9569c977aa3cd94d3ae4dad8da55` |

The intermediate/candidate hashes agree among the release record, Stage-2 constants/map and stored run outputs. The full SHA-256 values in this table are **owner-reported and cross-checked across those sources**, not independently recomputed here.

Stored Stage-1 results: 29 edits, 11/11 gates, 10/10 negative controls. K1 now regresses v0.9 to v0.8. C6 checks the four AZ source editions, current consumer edition and explicit ownership guard. C3 allows two new foreign references, `AZ-NUM-TOKRES-S1` and `RTG-OFN-OPEN-DISC-INTERACTION`, not new TDR-G result registrations. C4's truth-tag accounting is unchanged by the prose source grade.

Stored Stage-2 results: 43 operations, PASS, 268 qualified blocks (244 identical, 24 declared, zero unexplained), 8/8 negative controls. The owner's clean-worktree replay is source-reported. This scoped reviewer acceptance does not replace the Atlas owner's requested independent F1/F2 recheck.

## 5. F2 and release metadata

**[SESSION] F2: addressed on the candidate branch.** The AZ v0.9 notice is `dispositioned`, with `2026-11-16 · accept` pointing to the DRAFT release record. It is not yet closed; closure is explicitly after the tag. Release §7 no longer describes an empty current inbox and the planned AZ notification names v0.9. Accepting the notice and source synchronization does not adopt AZ's numerical result into TDR-G.

Two metadata items remain for the ordinary publication preparation, not a new DSN correction round:

1. PR #265's body still described F1 as rebuild-pending when this review began, despite its updated title and generated files. It must describe the completed owner rebuild and this bounded readback rather than the obsolete source-only checkpoint.
2. The DRAFT release-record header/rows still lead with the pre-F1 round-2 review. Add this F1 readback and the new Atlas disposition before adoption; preserve the earlier reviews at their exact candidate identities.

BASELINE remains a publication-stage change against current main. Do not overwrite newer rows for other streams. No merge, tag, pipe closure or adoption follows from this reviewer PASS.

## 6. Newer AZ editions and final decision

**[OWNER: Methodology v1.4 §3.3]** A newer owner edition does not automatically invalidate an intentionally pinned older import. The current source choice is the adopted `az-v0.9`; PR #276 is not itself a governing edition.

**[SESSION — recommendation, not PI authorization]** If AZ v0.10 is adopted before TDR-G v2.13, inspect only the affected imported claim and consumer-use clauses. If those remain compatible, retain v0.9 as an explicitly selected use pin and record the newer source plus deferred synchronization. Do not keep describing v0.9 as the newest governing AZ edition after that becomes false. If the imported proposition or permitted use actually changes, a substantive source disposition is still required. Avoid an automatic repin/rebuild loop based only on version numbers.

**Final reviewer disposition: PASS / F1 READBACK CLOSED** for candidate `c79898f99eaf83eb7b9d98749ec2f168868b664fa2e3f91916d888439a5236f4`, with F2 correctly dispositioned on the branch. This is a bounded source/interface review supported by targeted local checks and inspected owner-run outputs, not an independent full-build certificate. Next: Atlas F1/F2 recheck, PI adoption, then publication preparation and separately authorized merge/tag. TDR-19, XFER-O08-01, crystallization grade reconciliation and TDR-6 physical-observable selection remain outside this maintenance readback.
