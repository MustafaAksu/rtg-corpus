# RECOG v0.3.25 — Release record (DRAFT; stage 1 built, not adopted)

**Study:** RECOG · **Base (governing edition):** `recog-v0.3.24`, DSN SHA-256 `8c64bea231b3691b737f4143f6f4105030ee183fcc90d7f604ec83a4c869e7c1` (295,325 bytes).
**Stage-1 intermediate (round 2):** `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` on `claude/recog-v0.3.25-stage1`, SHA-256 `657cf302052ea2390ad170d9c03924ce6442b93cc85d076484c769bb0de9fe72` (331,077 bytes). Round 1 (commit `e9988b9`): `aecffdd109a987ae17078880aa818b107dd2c7851b1552b4ce8a17c93e3b5fa6` (330,024 bytes), reviewed in #5664297178; round 2 applies that review's two required corrections in place (§2a). A build stage, not an edition: header identity lines, status summary and footer are untouched; the Appendix A entry is a DRAFT line.
**Date:** 27 October 2026 · **Builder:** RECOG co-owner (Claude). **Method:** DSN Methodology v1.4 (§13.1, §13.6, §13.7); CONVENTIONS.md §4.
**Decision basis:** PI decision of 26 Oct 2026 — one consolidated maintenance and adoption-candidate package for the open cell PRs (#48, #49, #51, #53, #54, #59, #61, #63, #64, #71, #75), with the PI's grade classification (consolidated record §0); the co-owner (ChatGPT) session reviews of each PR (§6). **Four scientific acceptance decisions** (B1, A1c-E, A1c-D, A1c-Q), each separate; no structural-maintenance group in this release.

## 1. Groups and their acceptance decisions

| Group | Kind | Content | New RIDs | Source cells and reviews | Decision (PI) |
|---|---|---|---|---|---|
| **B1** | scientific | §6.13a sharpened R9 rows: `[ALG]` summation lemma $\sum_mq_m^3\le(1+q_0)q_0^2$; `[THM]` rows $(259.2,\tfrac1{400})$, $(81.49,\tfrac1{1600})$ from adopted statements (windows ×2); `[THM]` `[assuming: $C_7\le85.1/27.7$]` rows $(221.4,\tfrac1{400})$, $(75.69,\tfrac1{1600})$; adopted rows stay in force; §1 clause; §7 NF-REM uses | RECOG-ALG-R9-SUM-LEMMA; RECOG-THM-R9-SHARPENED-ROWS; RECOG-THM-R9-SHARPENED-ROWS-C7; RECOG-ART-R9-SHARPENED-ROWS | PR #48 Stage A v0.2.1 (`c15d1a0d…c4e6`; reviews 5640076782, 5640170089, 5640354759); PR #53 v0.1 (`8f746e92…6a11`; review 5640350431) | pending |
| **A1c-E** | scientific | §6.13b known-$a$ sharpened schedule: `[ALG]` harmonic tail bounds with the universal ceiling $E'\le0.31$ (`[ALG via IA]`); `[ALG]` in-block angle law and partial block; `[ALG]` exact combined-tail identity; `[THM]` `[assuming: (D5)]` sharpened schedule with the declared-data envelope $E'''=O_a((1+\log(a+M_k))/(a+M_k))$ and its centred form; A1b "Not supplied" status in place; §1 clause; §7 LPHASE/NF-REM uses | RECOG-ALG-A1C-TAIL-HARMONICS; RECOG-ALG-A1C-INBLOCK-ANGLE; RECOG-ALG-A1C-COMBINED-TAIL; RECOG-THM-A1C-SHARPENED-SCHEDULE; RECOG-ART-A1C-SHARPENED-SCHEDULE | PR #51 v0.2 (superseded; `3e946365…9747`; reviews 5640174052, 5640354476); PR #54 v0.2.1 (`41aa0309…447b`; 5643261362, 5643539166, 5643704955); PR #63 v0.2 (`614f7602…37d1`; 5645118795, 5649337542); PR #64 v0.2 (`8c77f541…d0bb`; 5649356071, 5651241407) | pending |
| **A1c-D** | scientific (requires A1c-E) | §6.16e record-only decoder: `[ALG]` admissible region / first finite interval / box enclosures; `[ALG]` start offset (sector $n_0\le7$; signed offset `[assuming: (D5)]`; start angle via R9); `[ALG]` joint contractor (true $a$ never an input; circular arcs; outer enclosure; no uniqueness) with `[NUM]` per-record widths; OPEN R6 A1c-decoder answered in bounded form (✓); §5 guard; A1b "Not supplied" and A1c RESULT clause in place; §1 clause; §7 PRIM-CTR use | RECOG-ALG-A1C-ADMISSIBLE-REGION; RECOG-ALG-A1C-START-OFFSET; RECOG-ALG-A1C-JOINT-CONTRACTOR; RECOG-ART-A1C-DECODER | PR #59 v0.2.1 (`356299ef…9a1a`; 5643708178, 5643815967, 5645113197); PR #71 v0.2 (`52343d4d…6ac6`; 5651241772, 5653208909); PR #75 v0.2 (`ee790103…861a`; 5653209785, 5658493941) | pending |
| **A1c-Q** | scientific | §6.16e record fibers: `[ALG]` threshold coding of the record; `[ALG]` (scope-limited) $C^1$ asymptotic phase and fibers on one $C^1$ level curve (empty interior; connectedness open); exact reduction of Q1′; OPEN R6 A1c-Q1′ reworded, stays `[OPEN]`; the slip-margin criterion stays `[SESSION/HEUR]` in the cell; §1 clause; §7 NF-INV use | RECOG-ALG-A1C-THRESHOLD-CODING; RECOG-ALG-A1C-PHASE-C1-FIBER; RECOG-ART-A1C-Q1PRIME-FIBER | PR #61 v0.2 (`ac996a51…86ad`; 5643821080, 5645113367) | pending |
| (#49) | editorial | A2 session record v0.2.1 wording of $J$; no DSN edit | none | PR #49 (`78b9b533…fd1c`; review 5640168643) | pending (merge with the package) |

No RID renamed or regraded; no OPEN status word changed (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED). The (D5) proof constants and the $C_7$ certificate ceilings remain `[assuming:]` (Dyadic has not registered them); nothing becomes unconditional. Not in stage 1: NUMGEN `numgen-v1.21` repin (separate maintenance after its own claim audit); layout compaction (none proposed).

## 2. Build

- Builder: `evidence/recog/scripts/build_recog_v0_3_25_stage1.py` (assertion-gated; modes `str`, `line`; Appendix A masked for live edits; `--only GROUP` builds a decoupling variant; A1CD cannot be built without A1CE). Base kept as `evidence/recog/v0.3.25/base_v0_3_24.md` (= `git show recog-v0.3.24:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`).
- Edit log: `evidence/recog/v0.3.25/stage1_edit_log.json` (24 edits, old and new text with hashes).
- Decoupling variants (`evidence/recog/v0.3.25/variants/`, round 2): B1 alone `ff5e4226…02cb` (5 edits); A1CE alone `dcc2f31a…4c84` (7); A1CQ alone `8d3ebfd0…5086` (6); A1CE+A1CD `edcc01c7…f1c1` (15). Round-1 values: A1CE `877fba99…a7f5`, A1CE+A1CD `f6bdb132…adac` (B1 and A1CQ unchanged). Each carries exactly its own new RIDs (checker C18); every variant passes the checker (`variants/check_only_*.txt`).

| Key | Group | Location | Mode |
|---|---|---|---|
| S1-B1 | B1 | §1 lattice paragraph: sharpened R9 rows clause | str |
| S1-A1CE | A1CE | §1 A1b sentence: sharpened schedule sentence | str |
| S1-A1CD | A1CD | §1: record-only decoder sentence | str |
| S1-A1CQ | A1CQ | §1: record-fiber sentence | str |
| S2-R6-Q1P | A1CQ | §2 OPEN R6 sub-item A1c-Q1′ reworded (stays `[OPEN]`) | line |
| S2-R6-DEC | A1CD | §2 OPEN R6 sub-item A1c-decoder answered in bounded form (✓) | line |
| S5-DEC | A1CD | §5 event-rule row: decoder guard (windows, not identification) | str |
| S613a-B1 | B1 | §6.13a: sharpened-rows block after the row-table paragraph | str |
| S613b-A1B-NS | A1CE | §6.13b A1b "Not supplied": computable envelope now supplied (status in place) | str |
| S613b-A1B-NS2 | A1CD | §6.13b A1b "Not supplied": outer window for $a$ now supplied (status in place) | str |
| S613b-A1CE | A1CE | §6.13b: known-$a$ sharpened schedule block before §6.14 | str |
| S616e-RESULT | A1CD | §6.16e RESULT: unknown-$a$ clause (status in place) | str |
| S616e-A1CQ | A1CQ | §6.16e: record-fiber block before §6.16f | str |
| S616e-A1CD | A1CD | §6.16e: record-only decoder block before §6.16f | str |
| S7-NFREM-B1, S7-NFREM-A1CE | B1, A1CE | §7 DYAD-THM-NF-REM row: new uses appended | line |
| S7-LPHASE-A1CE | A1CE | §7 DYAD-THM-LPHASE-ROWA-REMAINDER row: (D5) proof constants under `[assuming:]` | line |
| S7-NFINV-A1CQ | A1CQ | §7 DYAD-THM-NF-INV row: fiber use | line |
| S7-PRIMCTR-A1CD | A1CD | §7 DYAD-THM-PRIM-CTR row: tube bound in the sector | line |
| S8-B1, S8-A1CE, S8-A1CD, S8-A1CQ | each | §8 artifact rows after RECOG-ART-A3-QUADRATURE-TYPING (file order B1, A1c-E, A1c-D, A1c-Q) | line |
| A-1 | all | Appendix A: v0.3.25 DRAFT entry (per variant) | str |

In-place status edits inside adopted blocks (for the review's attention; the theorem statements themselves are unchanged, checker C13): the A1b "Not supplied" items (two clauses), the A1c RESULT's "no window with $a$ unknown" clause, the §5 guard, the two OPEN R6 sub-items. No `[RESULT]` block is added; the four `[THM]`/`[ALG]` families are paired to their cells by `[proof:]` and `Depends on:` lines.

## 2a. Round 2 — corrections from the stage-1 review (#5664297178 on `e9988b9`: `CONDITIONAL ACCEPTANCE — TARGETED CORRECTION`; B1 ACCEPTABLE, A1c-E ACCEPTABLE WITH TARGETED WORDING FIX, A1c-D ACCEPTABLE AS A CONDITIONAL OUTER DECODER, A1c-Q ACCEPTABLE at its scope)

| Item | Correction | Edits |
|---|---|---|
| R83-1 | the sharpened schedule's centre $c'''_k(a)=\tau\psi(a+M_k)-(k-1)\tfrac\pi3+\tfrac{\sqrt3}8(a+M_k)^{-1/2}+\tfrac\tau2(a+M_k)^{-1}$ needs the known $a$; it was called "record-only centre" in §1 and Appendix A. Now "known-$a$ / declared-data centre" (computed from the known $a$ and the record's $(M_k,r_k)$), with the explicit statement that nothing in RECOG-THM-A1C-SHARPENED-SCHEDULE is record-only and that the record-only operation with $a$ unknown is RECOG-ALG-A1C-JOINT-CONTRACTOR (A1c-D); the §6.13b theorem now displays $c'''_k(a)$ by name; the R6 A1c-decoder line says "not record-only" for the known-$a$ majorant and "record-only interval contractor" for the unknown-$a$ enclosure | S1-A1CE, S613b-A1CE, S2-R6-DEC, A-1 |
| R83-2 | the (D5) dependence is spelled out at every consequential use: the decoder blocks' `[assuming:]` now read "the Dyadic (D5) row-A bridge proof constants, as RECOG-THM-A1C-SHARPENED-SCHEDULE" (previously "as RECOG-THM-A1C-SHARPENED-SCHEDULE"); the A1c-decoder closure is explicitly limited to certified **outer** admissibility windows on the stated $U$, for records with at least two usable slips ($M_k\ge1$), under the (D5) `[assuming:]` — no identification, no uniqueness, no write mechanism, no Q1′ conclusion (§2 line and Appendix A) | S616e-A1CD (two qualifiers), S2-R6-DEC, A-1 |
| checker | gate C24 (R83-1: the centre is never called record-only in §1 or §6.13b; the decoder closure line carries the scope words) and controls NC26 ("record-only centre" reintroduced), NC27 (closure scope dropped) added | — |

No theorem statement, grade or RID changed between the rounds; B1 and A1c-Q texts and variants are byte-identical to round 1. Certificates not rerun.

## 3. Checks

- `evidence/recog/scripts/check_recog_v0_3_25_stage1.py` — 25 gates C0–C24 **all PASS**; 27 negative controls each caught by its target gate (`evidence/recog/v0.3.25/stage1_check_output.txt`). Gates of note: C6 every OPEN-registry `Status:` line byte-identical; C13 the RECOG-THM-R9-MEMORY statement line, its row table, the (c) row table and the whole RECOG-THM-A1B-SLIP-SCHEDULE-U statement (tag line through proof sketch) unchanged; C16 every file named in §8 exists and every quoted SHA-256 (full or abbreviated) is the hash of the named file (37 hashes); C17 the R6 sub-item A1c-Q1′ ends in `[OPEN]`; C19 the displayed constants agree with the certificate JSONs (B1: $259.2/81.49/221.4/75.69$, windows, $K_\Phi$; A1c-E: $0.74850$, $1.0753$, $E'\le0.31$ with box maximum $0.3095$, $c_\delta=0.793$, $1.9396$, $c_J^R=0.5008$, $c_7^R=100.23$, $0.3720$, the $E'''$ grid values; A1c-D: $\beta(625)=0.799$, the 12-record widths, boxes and containment flags; A1c-Q: $c_\Psi=11.13$, $\Xi=0.027$, $q^*$); C22 every source-conditioned new block carries a backticked `[assuming:]` naming the Dyadic source and no unconditional block carries one; C23 record paths exist and §8 record versions match the records' status lines; C24 (round 2) the known-$a$ centre is never called record-only and the decoder closure is scoped.
- Claim audit `evidence/recog/scripts/recog_v0_3_25_claim_audit.py` → `evidence/recog/v0.3.25/claim_audit.json`: the owner statements the new blocks rely on are present in the current sources at their tags — Dyadic `dyad-v6.4.22` (`2363ca40…8c29`): NF-REM rows, one-orbit contraction and certificate values $85.07/27.60$; the (D5) constants $0.79246$, $0.36915$ in the LPHASE row-A proof and DYAD-ART-LPHASE-ROWA; branch (B) $0.04654$ and $\tfrac{403}{250}$; PRIM-CTR with $2209$; NF-INV $\tfrac{256}{225}$ and NF6; RECOG `recog-v0.3.24`: the R9 rows, the A1b statement, the A1c readout and the two R6 sub-items. ALL PRESENT (presence at the cited RID; not a comparison with earlier editions).
- Certificates (not rerun for this build; unchanged since their cells, hashes in §8 of the intermediate): `recog_b1_l1l2_sharpened_rows_cert.py` (G1–G4, NC1–NC2), `recog_a1c_tail_averaging_cert.py` (G1–G6, NC1–NC2), `recog_a1c_inblock_angular_cert.py` (G1–G5, NC1–NC2), `recog_a1c_combined_tail_cert.py` (G1–G5, G4b, NC1–NC2), `recog_a1c_unknown_a_interval_cert.py` (G1–G4, NC1–NC3), `recog_a1c_start_offset_cert.py` (G1–G5, NC1–NC2), `recog_a1c_joint_transfer_cert.py` (G1–G3, JT1–JT2, NC1–NC2), `recog_a1c_q1prime_fiber_cert.py` (G1–G4, NC1–NC2).
- Vocabulary: no READ/WRITE/DECODE in the DSN (C11); the new blocks speak of records, enclosures, windows and readout. `tools/dsn_lint.py` informational report: `evidence/recog/v0.3.25/dsn_lint_stage1.txt` (growth $35{,}752$ bytes, $12.1$ %, 17 new RIDs counted by the lint: the 16 RECOG RIDs plus the cited Dyadic artifact RID).

## 4. Notices (prepared; separate states; none sent)

As the consolidated record §4: Dyadic (two requests — (D5) constants and $C_7$ ceilings as owner statements — and one informational item), NUMGEN (informational), consumers OFN/RRF/RER (informational: widened R9 windows, new RIDs), Atlas (row update at release). Routed through the PI; no notice state is recorded before a real dispatch; the v0.3.24 notices remain in their recorded states (§7.2 paragraph unchanged, checker C20).

## 5. Stage 2

Not built. No passage is removed or relocated; the growth is new science and registry rows. If the PI asks for a layout compaction, it follows the v0.3.24 pattern (`tools/check_compaction.py`, movement map, must-stay-live list) as a separate stage with its own review.

## 6. Reviews and adoption

| Stage | Reviewer / decision | Outcome |
|---|---|---|
| Cells (session level) | co-owner (ChatGPT): #48 5640354759; #49 5640168643; #51 5640354476; #53 5640350431; #54 5643704955; #59 5645113197; #61 5645113367; #63 5649337542; #64 5651241407; #71 5653208909; #75 5658493941 | all ACCEPTED at session level with their stated conditions (consolidated record §3) |
| Stage 1 — group B1 | co-owner (ChatGPT), review #5664297178 on `e9988b9` | ACCEPTABLE (L1 unconditional; L2 conditional on the owner-validated $C_7$ ceilings) |
| Stage 1 — group A1c-E | same | ACCEPTABLE WITH TARGETED WORDING FIX (R83-1, applied in round 2) — (D5) assumptions retained |
| Stage 1 — group A1c-D | same | ACCEPTABLE AS A CONDITIONAL OUTER DECODER, not identification (R83-2 scope wording applied in round 2) |
| Stage 1 — group A1c-Q | same | ACCEPTABLE at the $C^1$ phase-fiber / threshold-coding scope; Q1′ injectivity OPEN |
| Stage 1 overall | review #5664297178: `CONDITIONAL ACCEPTANCE — TARGETED CORRECTION`; round 2 (this build) applies R83-1 and R83-2; targeted re-check of the changed text requested | round 2 pending review |
| Stage 1 — atlas row check | atlas owner | pending (PI may defer, as for v0.3.24) |
| Adoption | PI — four separate decisions | pending |

Requested of the stage-1 review: (i) each science block against its accepted cell (no strengthening in transit: the `[assuming:]` scope of every (D5)-dependent block; the CT-1 order; IB-1's grid restriction; SO-1/SO-2; JT-1/JT-2; the Q1′ exact/heuristic separation; no uniqueness in the decoder blocks); (ii) the in-place status edits of §2 (checker C13 on the theorem statements; C6 on the status lines); (iii) the §7 import-row uses and the claim audit; (iv) the four variant hashes.

## 7. Records and evidence of this release

- `records/recog/RECOG_v0_3_25_CONSOLIDATED_CANDIDATE.md` — frame, results chain, decision matrix, notices.
- Cell records (unchanged, merged into the candidate tree): the eleven records of §1 with the hashes given there.
- Stage-1 build and checks: `evidence/recog/scripts/build_recog_v0_3_25_stage1.py`, `check_recog_v0_3_25_stage1.py`, `recog_v0_3_25_claim_audit.py`; `evidence/recog/v0.3.25/` (base, edit log, variants with their check outputs, check output, claim audit, lint).
- The branch `claude/recog-v0.3.25-stage1` contains the merged cell branches of PRs #48, #49, #51, #53, #54, #59, #61, #63, #64, #71 and #75 (their files are cited by §8 of the intermediate and checked by C16).

## 8. Adoption

Pending. The PI's decisions per group, the adopted file's publication-metadata hash, the merge (merge commit, not squash; the branch carries the merged cell branches) and the annotated tag `recog-v0.3.25` are recorded here when they happen. Until then `recog-v0.3.24` is the governing edition.
