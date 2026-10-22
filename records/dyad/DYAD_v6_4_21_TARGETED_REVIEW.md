# DYAD v6.4.21 — targeted receiving review, round 2

**Date:** 22 October 2026.  
**Reviewer:** ChatGPT.  
**Status:** SESSION / NONCANONICAL receiving decision; not owner/PI adoption.  
**Decision:** **REVIEW ACCEPTED — OWNER/PI ADOPTION READY at the reviewed maintenance/pilot scope.** S-6a, the round-2 stage-1 edits, and R1/R2 relocation eligibility are accepted. The repaired checker passes on the unchanged candidate after these region confirmations. Administrative advisory completion remains open.  
**Reviewed repository snapshot:** `4385dfd24721a01c90592fa8ef46bd4cb329e37c` on `claude/dyad-v6.4.21`. Candidate DSN: SHA-256 `277e640819cc35ce5cb664d396cda1feb675589db49a8d21746be568ead47510` (256,463 bytes; Git blob `dd5aed5c1d0d12ae26c6c40079e739690aa29f82`).  
**Preceding review:** this same path at the reviewed snapshot; its round-1 decision applies to candidate `31523bd8…d12d`, not to this corrected candidate. Prior review text remains in Git history.  
**Authority:** Methodology v1.4, especially §§12.2–12.4 and 13.1–13.9. Review acceptance, mechanical PASS, owner adoption and downstream synchronization remain separate.

## 1. Inspection and execution actually completed

Read the complete supplied round-2 stage-1 diff, region registry, exact h4 script, compaction and negative-control reports, completion matrix and release record. Inspected all 19 movement-map operations, the complete R1 and R2 source regions, and the relevant candidate/context passages. Read the updated checker and test harness, and the original archival script through GitHub. This is a targeted second pass, not another full scientific DSN/corpus audit.

Applied the supplied differences to the mounted, hash-verified v6.4.20 source. The old stage-1 diff reconstructs `0572120a…36b5`; the round-2 stage-1 delta reconstructs `f2b20419…9119`; the new stage-2 delta reconstructs `277e6408…7510`. Every hash matches the recorded input. The reconstructed candidate's Git blob matches the GitHub response at the pinned snapshot.

| Object | SHA-256 | Independently checked extent |
|---|---|---|
| Adopted predecessor | `0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852` | Mounted predecessor bytes; input for both reconstructed deltas |
| Corrected intermediate, round 2 | `f2b20419898ae1c84235a808479391f2d29fc05b2f9a0e46f606539327d29119` | 415,869 bytes; exact diff reconstruction |
| Compacted candidate, round 2 | `277e640819cc35ce5cb664d396cda1feb675589db49a8d21746be568ead47510` | 256,463 bytes; exact diff reconstruction and remote blob match |
| Movement map | `b76d753e7301b781c6f5ff7d2ce3718ec7855f010955117cbb125de1dc28eaf8` | Remote blob `07f9c21f7b5a24dd1a8a12d19faf8e120747e063`; reconstructed candidate exactly |
| Compaction checker | `22d1ef56545d4dbcbbddeddccd446799e5c9a8e6cb0e1c53d51ccaf137c61495` | Remote blob `04db23115ecc62ac9dbbb17a4e3f45066cc070ab`; inspected and executed |
| Negative-control harness | `059b9004b35c16957328e9db139f09027e5f16ccf571c59edc97f43d072a95f7` | Remote blob `4aee8a3f55bc6b6c3df92c25d86557ad9e736089`; inspected and executed |

The container could not clone/download the public repository. Source copies used for execution were authenticated against the Git blob identities returned by the connected GitHub tool. For the positive replay, only archive loading was adapted to the same SHA-256-matching local predecessor bytes. For the subprocess test suite, only the map's archive locator was replaced by that local path. Neither checker nor test rules were changed. The unconfirmed PENDING report and the 16-control report reproduced the submitted JSON bytes exactly.

## 2. Stage-1 receiving decision

**ACCEPT.** The round-1 accepted corrections remain at their previously reviewed scope. The new delta correctly implements:

- **S-6a:** the archival h4 coefficient field is Q(i sqrt(3)); its exact support is separate from the recovered numerical script. The `[ALG]` grade, archival convention and c_theta^(6) value are unchanged. The exact check is not represented as a rerun of an originally exact producer.
- **U / U_T:** Appendix C identifies U as the start/block-base-point set, and U_T as its invariant six-phase tube. No tube-wide strengthening is introduced.
- **R11:** RECOG R11 is closed at its final-chart ledger scope. The historical fitted-backbone identification remains open, with the SG-19 non-transfer restriction intact. No fit or coefficient transfer is validated by this wording repair.

No new RID, renamed RID, owner theorem regrade or additional physical claim is authorized by this review. The prior exact RAW-CUBIC range check remains scoped to the raw one-step coefficient; historical proposition identity remains unresolved.

## 3. S-6a evidence and exact result

Recovered source: `evidence/dyad/scripts/normalize_p6_liegauge_exact.py`, SHA-256 `cec918f808cbc02c53beba5f88faf1edbed830a87dac7283e6ac2511d2ec5835`. Inspected and rerun unchanged. Its arithmetic is mpmath at 120 decimal digits with tolerance pruning. All five displayed h4 comparisons pass the script's 1e-100 numerical criterion. Its original “exact over Q(sqrt(3))” output remains an archival label, not this review's exactness claim.

Reran `dyad_h4_archival_exact_check.py`, SHA-256 `7617c431aae8a33243541f398ee40afa988f6a0faf254c7f14291561a2c4716c`: five exact coefficient matches, exit 0. Also independently recomputed the six-step fourth jet in the native real rho/eta variables with rational arithmetic, then converted to the declared complex frame using exact algebraic arithmetic. Ten receiving checks pass. This is an alternative composition implementation with a shared generator and SymPy at the final algebraic-conversion step, not a claim of fully independent mathematical premises or an independent proof engine.

| (a,b) | h4^(a,b) |
|---|---|
| (4,0) | -1/16 + 7 i sqrt(3)/144 |
| (3,1) | -1/6 - 2 i sqrt(3)/9 |
| (2,2) | -5/24 - 11 i sqrt(3)/24 |
| (1,3) | 1/3 + i sqrt(3)/9 |
| (0,4) | 0 |

The receiving calculation additionally checks the identity linear return, vanishing quadratic return, purely resonant cubic return, and nonresonance of every degree-four channel. Thus `[log F]_4 = F_4` for this return and the archival selection gives `h4 = [log F]_4`. The nonzero imaginary part of the (1,3) coefficient rules out the real field Q(sqrt(3)). This concerns the archival object, not the NF6 normalizer. No new c_theta certificate, analytic-convergence result or physical identification is claimed.

## 4. R1 / R2 confirmations

Both regions were read in full and extracted independently from the hash-pinned predecessor. Their declared hashes and character lengths match exactly.

| Region / operation | Source SHA-256 | Receiving disposition |
|---|---|---|
| R1 / M03; 2,156 characters | `443fa0b0d35b21bacfe0b3d3316d09cb6407028f4f7df856409052e763f9b44b` | CONFIRMED as the historical v6.4.19/P1-to-v6.4.20 tag-spelling conversion table. Owner RIDs inside tag examples are not result bodies. Its pinned historical pointer remains. |
| R2 / M18; 7,603 characters | `6e8466bdd4380ee3eca36a7375f042ba431f1106111de4bcaff8c59a034d2562` | CONFIRMED as the historical heading/section movement table. No unique live result is removed; the Appendix G anchor and predecessor pointer remain. |

This approval applies to these exact regions and these operations only. It is not blanket permission to classify future scientific material as tag examples or navigation. The reviewer confirmation fields are filled in `evidence/dyad/v6.4.21/reviewed_regions.json`.

## 5. Checker receiving decision

**ACCEPT for this candidate, map and declared parser scope.** With blank confirmations the replay returns **PENDING, exit 3**, byte-identical to the supplied report. With the actual confirmations above, it returns **PASS, exit 0**: 609 parsed live claim blocks; 573 unchanged; 36 changed by the declared operations; no unexplained block change. All 27 checked archive targets resolve. This is not a claim that every possible source link is parsed.

The unmodified supplied test harness returns **PASS: 16/16 negative controls rejected**, including REVIEW-N1, REVIEW-N2, REVIEW-N3 and the registered-region variant REVIEW-N3b. Its JSON report is byte-identical to the submitted negative-control report. The three prior false-PASS cases are therefore closed at the tested regression scope.

No generic semantic-equivalence theorem or universal checker-completeness claim is made. The allowed operations still require their declared source classification; the actual 19-operation map and two exception regions were reviewed here. Unchanged NF, interval, smooth-embedding and other inherited certificate campaigns were not rerun.

## 6. Administrative state and release handoff

The completion matrix has exactly 34 unique rows and the stated exclusive primary counts: **18 DONE v6.4.20 + 10 DONE v6.4.21 candidate + 4 OPEN + 2 RESEARCH**. The four OPEN rows concern C-2/source records or notice transmission; FC-31/32 remain research. Existing source-recovery limitations, including the historical RAW-CUBIC identity, remain visible rather than being certified by this maintenance review.

The maintainer's recorded nonblocking treatment of C-2 and unsent notices is acceptable for adoption of the corrected maintenance edition with those limitations explicitly retained. It is **not** completion of the 34-row advisory, delivery of N16–N21, consumer acceptance, or corpus synchronization. Post-installation read-back and the Atlas refresh remain later administrative actions.

Next: record the actual owner/PI adoption decision; perform the metadata-only publication transform, including **header, Appendix A status and the single footer**; recompute the final file hash; update the release record and BASELINE; verify the publication diff; only then merge/tag under the adopted workflow. The candidate hash above must not be reused as the final hash after changing publication text. These routine finalization checks do not require another scientific round if no scientific content changes.

This receiving decision authorizes no main-branch write, PR creation, merge, tag, notice transmission or adoption. The reviewer commit changes review/evidence records only; the DSN candidate bytes remain unchanged.
