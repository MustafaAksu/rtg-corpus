# RTG Relational Recognition DSN v0.3.23 — release record

**Status:** DRAFT — stage 1 built and checked; under review. Not adopted. This record is completed at adoption (Methodology v1.4 §13.7) and frozen then.
**Prepared by:** RECOG co-owner (Claude), at the PI's direction of 23 October 2026 ("Go for stage 1 of RECOG v0.3.23").
**Reviews requested:** change-focused review of stage 1 by the second RECOG co-owner (ChatGPT); the advisory rows checked by the atlas owner; a separate verdict on the FC-21 science block (§4).
**Governing methodology:** DSN Methodology v1.4 (tag `methodology-v1.4`, `cdacab5f…f2df`). v0.3.22 was adopted under v1.3; the migration is a successor action.
**Predecessor:** v0.3.22, tag `recog-v0.3.22`, SHA-256 `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9`; release record `records/recog/RECOG_v0_3_22_RELEASE_RECORD.md`.
**Instructions implemented:**
- the atlas advisory `records/recog/ATLAS_ADVISORY_RECOG_v0_3_22.md` (FINAL PROPOSAL v1.0, `5c888118…dd85`);
- the two owner dispositions, `RECOG_OWNER_DISPOSITION_ATLAS_ADVISORY_v0_3_22_COOWNER_CLAUDE_20261023.md` (`49f1eb20…e8bd`) and `RECOG_ATLAS_ADVISORY_OWNER_DISPOSITION_20261023.md` (`be286088…8b91`);
- the reconciliation record with the PI decisions of 23 Oct 2026, `ATLAS_ADVISORY_RECOG_v0_3_22_DISPOSITION_RECONCILIATION.md` §5 (`9bc7a57c…f30e`): FB-13 two new RIDs; notice states unchanged; F5 not in this release; version v0.3.23; build on `claude/recog-v0.3.23-stage1`;
- the post-release maintenance note `RECOG_v0_3_22_POST_RELEASE_MAINTENANCE_NOTE.md` (`b5b9131c…eab0`), erratum E-0322-1.

**Branch base.** The PI asked for a build from tag `recog-v0.3.22`. The tag commit predates `tools/` and `records/`, so the branch starts at `main` `fd5026a` (merge of PR #18). On that commit `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` is byte-identical to the tag. The builder reads the base from the tag (`git show recog-v0.3.22:…`) and asserts its SHA-256, so the base is the tagged edition either way.

## 1. Build stages (branch `claude/recog-v0.3.23-stage1`)

| Stage | File SHA-256 | Builder | Check |
|---|---|---|---|
| Adopted v0.3.22 (tag `recog-v0.3.22`) | `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` | — | — |
| **1 — corrected intermediate, with FC-21** (build stage, not an edition; this is `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` on the branch) | `6a1bdfb062c9233ea56da15760878b73f41f067eea512ddff5ea267b17b4ec06` | `evidence/recog/scripts/build_recog_v0_3_23_stage1.py` (116 assertion-gated edits; Appendix A masked except the new entry) | `check_recog_v0_3_23_stage1.py`: 22/22 gates PASS, 22/22 negative controls caught by their target gate |
| 1′ — same, without FC-21 (decoupling variant; not committed as a file) | `5cb316674ff2aff875af238166119326530f53366f2d7198a9ab0aa9b3f54345` | same builder, `--without-fc21` (110 edits) | 21/21 gates PASS (C18 applies only to the with-FC-21 variant) |
| 2 — compacted candidate | — | not started; layout only, after the stage-1 review (FA-01) | `tools/check_compaction.py` against the intermediate |

**Reproduce** (repository root; the redirection must be byte-exact, so on Windows use `cmd /c`, not PowerShell `>`):

```
cmd /c "git show recog-v0.3.22:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md > base.md"
python -I evidence/recog/scripts/build_recog_v0_3_23_stage1.py base.md inter.md edits.json
python -I evidence/recog/scripts/build_recog_v0_3_23_stage1.py base.md inter_nofc.md edits_nofc.json --without-fc21
python -I evidence/recog/scripts/check_recog_v0_3_23_stage1.py base.md inter.md edits.json --controls
python -I evidence/recog/scripts/recog_v0_3_23_claim_audit.py claim_audit.json
python -I evidence/recog/scripts/recog_v0_3_23_value_checks.py value_checks.json
python tools/dsn_lint.py inter.md --prev base.md
```
`inter.md` must equal `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` (`6a1bdfb0…ec06`). Diff: `git diff recog-v0.3.22 -- dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` on the branch.

## 2. Changes (stage 1)

Edit keys refer to `evidence/recog/v0.3.23/stage1_edits.json`, which holds each edit's location, old and new text and their hashes.

**Tier A**

| Row | Edit keys | Location | Change |
|---|---|---|---|
| FA-01 (status part only) | S616-1, S616-2, S616-3, S616a-R1 (part), S616b-1, S616c-1 | §6.16–§6.16c | stale F2 follow-ons now point to the results (F2(b) §6.16a, F2(a) §6.16b, F2(c0)/(c1) §6.16c–d); the compaction itself is stage 2 |
| FA-02 | H-3, S613b-3, S613b-4, S7-10, S7-11, S7-12 | header; §6.13b; §7 | NUMGEN $D_M$ and INF-1 imported by RID at `numgen-v1.20.8` (`NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-INF1`); INF-1 "Depends on" names L-BACKBONE, L-PHASE, L-MONO by RID; the lift by `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`; $U$ vs $U\cap U_{\rm NUMGEN}$ kept. A1a-G1 governance text and the tracking keys `A1A-NG-D-DEF`, `A1A-NG-INF1` leave the live rows (they stay at the tag) |
| FA-03 | S3-1, S613-2, S614-3, S4-1, S3-2, S3-3 | SG-R10; §6.13; §6.14; §4; SG-R14 | guard kept (leading amplitude is not a finite-$q_0$ bound); stale routing "(R9/R10/R11)" replaced by the R9 rows: $\lvert M-c_{\rm iso}q_0\rvert\le\lvert G\rvert q_0+C_2q_0^2$, hence $\lvert M\rvert\le(\lvert c_{\rm iso}\rvert+\lvert G\rvert)q_0+C_2q_0^2$ (from RECOG-THM-R9-MEMORY and $\max_\Theta\lvert\Lambda_1\rvert=\lvert G\rvert$; checked in value check A4/A7), per row, $C_z$ track, normalized $q$; $2C_7q_0^2$ named the degree-≥7 partial budget, its thresholds use $\lvert G\rvert$; §4 marks $c_\theta^{(6)}$ and backbones as non-chart objects; SG-R14: T1/T2 in adopted use |
| FA-04 | S63-1 | §6.3 | the Dyadic v6.4.22 §1 fixed-point table answers the flag |
| FA-05 | H-4, S72-1, S73-1 … S73-8 | header; §7.2; §7.3 | N11 recorded as adopted use (as Dyadic v6.4.22 §7 records it); §7.3 consumers at the current tags (Dyadic v6.4.22, RRF v0.8.4, OFN v0.10, RER v0.2) and two new consumer rows (RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, RECOG-ALG-P2-C0-WHITNEY-FOLD) |
| FA-06 | H-5, H-6, H-7, S613b-2 | header; §6.13b | Methodology v1.4 (§3.4, key M13-C04 unchanged) |
| FA-07, FB-20 | S8-1, S8-2 | §8 | repository locations; every §8 file name is in the repository except the Dyadic-side harness `dyad_referee_p2b_v2.py` (checker gate C16); items cited by hash only and missing are listed; recovery list referenced |
| FA-08 | S64-2, S66-1, S615-R1…R3, S616-R1, S616-R2, S616a-R1, S616b-R1, S616d-R1…R3, S616e-R1…R3, S616f-R1, S616f-R2, S616g-R1, S616g-R2 | §§6.4–6.16g | per-block ledger in §3 below |
| FA-09 | S5-2 | §5 | $6\gamma t^6+O(t^8)$ |

**Tier B**

| Row | Edit keys | Location | Change |
|---|---|---|---|
| FB-10 | S7-2 … S7-5, S7-16, S615c-1 | §7; §6.15c | Dyadic RIDs registered v6.4.11/v6.4.20 cited by claim (`DYAD-DEF-PRIMITIVE-MAP`, `DYAD-DEF-CRITICAL-CURVE`, `DYAD-ALG-QC-CRITICAL-AMPLITUDE`, `DYAD-ALG-ISP-MAPS`, `DYAD-ALG-SIXSTEP-CUBIC-JET`, `DYAD-ALG-RAW-ANGULAR-MEAN`); objects without a Dyadic RID named (non-symplecticity, winding invisibility, escape law, $J$, $\det J$, fixed points, block recurrences); process sentence removed |
| FB-11 | H-1, H-2, S2-3, S613b-5 … S613b-13, S614-1, S7-1, S7-7 … S7-9, S7-13 … S7-15, S72-2 | header; R6; §6.13b; §6.14; §7; §7.2 | claim-level audit (§5 below) at `dyad-v6.4.22` and `numgen-v1.20.8`: 34/34 rows unchanged; the five Dyadic line pins ("lines 806–809" twice, "lines 843–850" once in §6.13b; two §7 rows) replaced by RID + section; current owner tag forms quoted (`[THM]` `[assuming: RECOG-THM-R9-MEMORY]`; `[ALG]` `[scope: formal second order; remainder certified separately, OPEN 21]`), with the v6.4.18 form named; producer editions named; the A1a-E2 v6.4.18 check kept as historical evidence. The inline NUMGEN v1.15 pins of §6.2 and §6.5 are valid producer pins and stay; their §7 rows name the current edition |
| FB-12 | S1-1, S1-2, S615-1 | §1; §6.15 | §1 RECOG-OPEN-INTERSECTION tagged `[HYP]` as in §6.5 (the RID word is identity text); LEADING-RETURN-EQUIVARIANCE points to §6.12; `E2C-ENG-SPLIT-REFINEMENT` gets the custody note "a RECOG artifact", no rename |
| FB-13 | S64-1, S613a-2, S613a-3, S1-5, S69-1, S1-4, S610-3, S611-1 | §6.4; §6.13a; §1; §6.9; §6.10; §6.11 | two new RIDs (PI decision): `RECOG-THM-R9-COMPARATOR-INCOMPLETENESS` (§6.13a corollary, cited in §1 and §6.9) and `RECOG-ALG-SWAP-ODD-RHO` (§6.4 lemma); statements unchanged. Named sub-statements: the radial identity $\Re(\bar\lambda\nu_3)=-\sin^2(\theta/2)$ under RECOG-ALG-NU3-CLOSED-FORM ($Z$-frame); the $C_0$-avoidance corollary under RECOG-THM-P2-HET. Deferred, no consumer citation yet: radial-fate law, fixed-point inventory, finite ledger $\mu_5,\mu_7$, uncoupled pair, finite-block identity (stays internal) |
| FB-14 | S613-1, S613a-1, S613a-4, S613a-5, S614-3 | §6.13; §6.13a; §6.14 | frame labels and $\approx$ displays; correction record in §6 below |
| FB-15 | S1-3, S2-2, S4-1, S62-1, S610-1 | §1; R2; §4; §6.2; §6.10 | `DYAD-ALG-KP-FRAME-SCALE` cited ($W_p=i\cot(\pi/p)Z$, $\nu_3^Z=\cot^2(\pi/p)\nu_3^{W_p}$, factor 3 at $p=6$); exports tagged $Z$-frame; §6.2 frame-independence restricted to tangent-to-identity changes, linear rescaling referred to the frame rule |
| FB-16 | S614-2 | §6.14 | $j^6S_h=j^6R_0$; DYAD-THM-SMOOTH-EMBEDDING (E4) at germ scope; the advisory's "must not" list stated; R1, RRF OPEN-A, OPEN-OFN-OPA stay open |
| FB-17 | S72-3 | §7.2 | current notice paragraph (states unchanged, §7 below); RF-1 marked fulfilled as a content state; the audit and notice history move to records in stage 2 |
| FB-18 | S2-1, S610-2, S7-6 | R2; §6.10; §7 | one custody statement: DYAD-ALG-BRIDGE-LEMMA is Dyadic's; the general-$p$ proof is RECOG's; "recommended for Dyadic" and "ownership offered" removed |
| FB-19 | S613b-1 | §6.13b | notation line only (block count $M$ vs memories $M(z_0)$, $M_W$; $N$ where both occur) |

**Extra stage-1 items (both dispositions)**

| Item | Edit keys | Change |
|---|---|---|
| R10 wording | S2-4 | "**CLOSED (v0.3.2) — delivered and accepted**" (was "DELIVERED and ACCEPTED"); census unchanged |
| Dyadic v6.4.21+ tag forms | S3-2, S613b-8, S613b-10, S613b-11, S7-13 … S7-15, S73-3 | quoted as the owner prints them now |
| Five Dyadic line pins | S613b-8, S613b-11, S613b-12, S7-14, S7-15 | RID + section |
| E-0322-1 | H-8 | v0.3.21 is "prior adopted edition, historical" |
| RF-1 | S72-3, S73-6 | fulfilled by RRF v0.8.4 §6.3 (W3 verbatim with RID; inter-space transport an `[OPEN]` RRF extension); recorded separately from notice state |
| VF-1 | S616f-1 | cites `DYAD-ALG-NF6-DEG10` (registered in RRF v0.8 as VF-1) |
| Appendix A entry | A-1 | compact draft entry for v0.3.23; the publication commit sets its heading |

**Deferred or routed (no edit):** FC-22 (missing: first-passage index definition, eventual monotonicity of $\Theta_m$, vanishing overshoot); FC-24 (missing: frame match of $S_h$ and $R$ at second order in the B-section frame); FC-23 routed to GEN; GAP-LOCK Lemma 3 use and the explicit-domain inputs routed to NUMGEN, the phase-moment retest to GEN (informational, via the PI); R6 F5 not in this release (PI decision 3). Header identity lines, the stacked status summaries, the freeze history, closed-OPEN specifications, §9, the SG order and Appendix A compaction are stage 2 (FA-01).

## 3. FA-08 — per-block `[RESULT]` ledger

Method: Methodology v1.4 §3.4 — `[RESULT]` is paired with exactly one canonical status, that of the conclusion's load-bearing input; heterogeneous conclusions are split. Wording is kept, except the two splits and the stale F2(a) pointer inside block 8. No grade is promoted: a bare `[RESULT]` carried no canonical status before. Line numbers are those of v0.3.22.

| # | v0.3.22 line | Block | Decision | Load-bearing input |
|---|---|---|---|---|
| 1 | 487 | §6.4 stationarity reframed | `[from: ALG conditional]` → `[from: ALG]` [assumes: pole-swap covariance of the radial row; certified $A=DT(P_1)$] | canonical spelling of the local alias (Local Tag Aliases); proved implication under the listed assumptions |
| 2 | 548 | §6.6a R5 restated | `[from: ALG]` [assumes: the twisted-cocycle premise] | RECOG-ALG-SHEAR-COCYCLE-CLASSIFICATION, -WEIGHT-IDENTIFICATION, -ORIENTATION-CONJUGACY |
| 3 | 837 | §6.15a radial access ⇏ rank-side entry | `[from: THM]` [scope: diagnostic twin $T_s$, SG-R4] | RECOG-THM-TWIN-RADIAL-ACCESS, RECOG-THM-TWIN-STAGE2-NONUNIVERSAL; the E3A-1 sentence is a stated nonclaim |
| 4 | 853 | §6.15b three R7 statements decided | `[from: THM]` [scope: $T_s$, SG-R4] | the three R7 theorems |
| 5 | 865 | RECOG-RESULT-TWIN-QC-DEGENERACY | `[from: ALG]` | RECOG-ALG-TWIN-CROSSING-RANK-SAFE |
| 6 | 873 | RECOG-RESULT-EVENT-UNDERDETERMINATION | `[from: THM]` [scope: registry-relative; the currently registered candidate structures] | the theorem-grade refutation in the first ledger row (R9 window inside the rank-safe tube); one refuted implication suffices for non-identification |
| 7 | 905 | F1 conclusion | `[from: THM]` [scope: registry-relative] | block 6 |
| 8 | 927 | tokenisation consequence | **split**: `[from: NUM strong]` (token side; F2(b) campaign, 12 orbits, 87 slips; leading-order law RECOG-ALG-CHART-SHADOW) and `[from: ALG]` (schema side); "remaining F2(a) question" → "settled by F2(a) (§6.16b)" | `[from: NUM strong, ALG]` was a combined label |
| 9 | 956 | F2(a) conclusion | `[from: ALG]` [scope: registry-relative] | RECOG-ALG-BTOKEN-TRANSPORT and the representation ledger |
| 10 | 995 | RECOG-RESULT-P2-FOLD-NO-REGISTERED-RETENTION | `[from: ALG]` [scope: registry-relative; current registered carrier inventory] | fold certificate (§6.16c, `[ALG]`) and the carrier audit |
| 11 | 999 | criterion-5 classification | `[from: ALG]` [scope: registry-relative] | as 10 |
| 12 | 1003 | separation of R and E axes | **split**: `[from: THM]` (retention side, RECOG-THM-R9-MEMORY) and `[from: ALG]` [scope: registry-relative] (transition and token side; the selection-principle sentence) | `[from: THM, ALG, RESULT]` was a combined label |
| 13 | 1019 | B/7-gap: $R_{\log}$ only | `[from: ALG]` [scope: registry-relative; anti-tautology guard] | RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE (`[ALG]`) |
| 14 | 1021 | completed criterion table | `[from: ALG]` [scope: registry-relative] | blocks 9–13 |
| 15 | 1030 | coupling gap | `[from: ALG]` [scope: registry-relative] | the criterion table; "potentially a coupling" and the next question kept as written |
| 16 | 1052 | RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH | `[from: ALG]` [scope: registry-relative] | RECOG-ALG-CONTINUOUS-CARRIER-NOWRITE applied to R9's carrier |
| 17 | 1054 | ladder outcome, R6 endpoint | `[from: ALG]` [scope: registry-relative] | the F3 ladder |
| 18 | 1108 | RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS | `[from: DEF]` [scope: registry-relative] | identification/inheritance ledger only, no dynamics (§6.16g guard) |
| 19 | 1110 | cross-owner alignment | `[from: DEF]` [scope: registry-relative; no import] | as 18 |

Checker gate C9: 0 unpaired or combined line-leading `[RESULT]` blocks in §§1–6 (base calibration: 19, as the advisory counted).

## 4. New science — FC-21 (separately marked; own verdict)

- **RID:** `RECOG-THM-A1A-PHASE-EXISTENCE-U` `[THM]` (§6.13b), with artifact `RECOG-ART-A1A-EXISTENCE-U` (§8).
- **Content:** for every $x_0\in U=\{0<Q_0\le\tfrac1{625}\}$, H-NG holds and $C_D^{\rm ext}=\tau H(a)+\tau\sum_m(Q_m-\tfrac1{a+m})-\sum_mr_m$ with $H(a)=-\psi(a)$, $a=Q_0^{-1}$; hence the asymptotic phase exists on all of $U$ without R9 and without NUMGEN INF-1. Premise: `DYAD-THM-LPHASE-ROWA-REMAINDER` (row A; not conditional on R9).
- **Proof cell:** `records/recog/RECOG_v0_3_23_FC21_PROOF_CELL.md` — statement, premises quoted from `dyad-v6.4.22`, the four checks (lift branch, domain, indexing, amplitude inversion), proof, scope.
- **Placement edits (group `FC21`):** S1-6 (§1), S5-1 (§5 high-risk row), S613b-14 (block and scope item (i)), S7-17 (§7 import row), S8-3 (§8 artifact), A-2 (Appendix A line).
- **Unchanged:** RECOG-RESULT-A1A-PHASE-EXISTENCE-NG and RECOG-RESULT-A1A-CD-AGREEMENT (NUMGEN route); RECOG-THM-A1A-CD-IDENTIFICATION (R9 route).
- **Not supplied:** see the proof cell §5.
- **Decoupling rule (PI decision):** if this block's review is not finished when the maintenance rows are ready, v0.3.23 is released as the `--without-fc21` build (`5cb31667…4345`, gates PASS), and FC-21 follows in its own release.
- **Review verdict:** pending.

## 5. FB-11 — claim-level audit at the tags

Tool: `evidence/recog/scripts/recog_v0_3_23_claim_audit.py`, output `evidence/recog/v0.3.23/claim_audit.json`. Sources: `dyad-v6.4.22` (`2363ca40…8c29`) and `numgen-v1.20.8` (`835a56f8…7e2f`), read with `git show` and hash-asserted. For every row the RID or section anchor and the statement strings RECOG quotes must occur in the owner text. This is a source-read check of quoted statements (`EV-SRC-READ`); no owner certificate was rerun. Class **U** = statement unchanged at the current tag.

| key | RECOG use | owner RID or section | v0.3.22 pin | current owner tag form | class |
|---|---|---|---|---|---|
| C21 | §7 row; §6.2 | `DYAD-THM-C21` | v6.4.10 §6.2, §6.7 | [THM] | U |
| NF6 | §7 row; §6.14 | `DYAD-ALG-NF6` | v6.4.10 §6.14 | [ALG] | U |
| NF6-OBS | §7 row; §6.14 | `DYAD-ALG-NF6-OBS` | v6.4.10 §6.14 | [ALG] | U |
| PRIM-CTR | §7 row; §6.13b; §6.14 | `DYAD-THM-PRIM-CTR` | v6.4.10 / v6.4.16 §6.14 | [THM] | U |
| NF-INV | §7 row; §6.13b; §6.14 | `DYAD-THM-NF-INV` | v6.4.10 / v6.4.16 §6.14 | [THM] | U |
| NF-REM | §7 row; §6.14 | `DYAD-THM-NF-REM` | v6.4.10 §6.14 | [THM] | U |
| BRIDGE | §7 rows; §6.10 | `DYAD-ALG-BRIDGE-LEMMA` | Dyadic §6.9 | [ALG] | U |
| KP-FRAME | §1; §2 R2; §4; §6.2; §6.10 (new citation) | `DYAD-ALG-KP-FRAME-SCALE` | (not cited in v0.3.22) | [ALG] | U |
| FACEFLUX | §7 row | `DYAD-ALG-P6-FACEFLUX` | Dyadic §6.2 | [ALG] | U |
| PRIMITIVE-MAP | §7 row (§6.1 block) | `DYAD-DEF-PRIMITIVE-MAP` | Dyadic §6.1 | [DEF] | U |
| CRITICAL-CURVE | §7 row (§6.1 block) | `DYAD-DEF-CRITICAL-CURVE` | Dyadic §6.1 (no RID then) | [DEF] | U |
| QC | §7 row (§6.4 block); §6.15c | `DYAD-ALG-QC-CRITICAL-AMPLITUDE` | v6.4.10 §4 / §6.4 (no RID then) | [ALG] | U |
| ISP | §7 row (§6.4 block) | `DYAD-ALG-ISP-MAPS` | Dyadic §6.4 (no RID then) | [ALG] | U |
| SIXSTEP-JET | §7 row (§6.7/§6.8 block) | `DYAD-ALG-SIXSTEP-CUBIC-JET` | Dyadic §6.7–6.8 (no RID then) | [ALG] | U |
| RAW-MEAN | §7 row (§6.5) | `DYAD-ALG-RAW-ANGULAR-MEAN` | v6.4.10 §6.5 (no RID then) | [ALG] | U |
| LIEGAUGE | §7 row | `DYAD-ALG-LIEGAUGE-NORM` | Dyadic §6.9 | [ALG] [conv: Lie strict-kernel gauge] | U |
| ALIAS | §7 row | `DYAD-ALG-ALIAS-PHASE` | Dyadic OPEN 16 | [ALG] | U |
| CONSTANTS | §7 row (Dyadic §6.3); §6.13 lattice clock | Dyadic §6.3 constants (no RID) | Dyadic §6.3 | [ALG] | U |
| H2 | §7 row (Dyadic §6.2 $h_2$); §6.13 frame correction | `DYAD-ALG-NF6 ($h_2$ entry; no separate RID)` | Dyadic §6.2 | [ALG] | U |
| FIXED-POINTS | §6.3 (FA-04) | §1 fixed-point scope table | Dyadic §6.1 | [ALG] | U |
| OFFSET | §6.13b; §7 row | `DYAD-ALG-OPEN3-PHASE-OFFSET` | v6.4.16 §6.14 (v6.4.15 entries); primitive-variable form v6.4.18 lines 806–809 | [ALG]; primitive-variable form [ALG] [scope: formal second order; remainder certified separately, OPEN 21] | U |
| OFFSET-BOUNDS | §6.13b; §7 row | `DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS` | v6.4.16 §6.14 | [THM] | U |
| T1T2 | §3 SG-R14; §6.13b; §7 row | `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` | v6.4.15 / v6.4.16 §6.14 | T1 [THM] [assuming: RECOG-THM-R9-MEMORY]; T2 [THM] [assuming: T1] | U |
| OPEN21 | §6.13b; §7 row | `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` | v6.4.18 §6.14 lines 843–850 | [THM] [assuming: RECOG-THM-R9-MEMORY] | U |
| LPHASE-ROWA | §6.13b RECOG-THM-A1A-PHASE-EXISTENCE-U (FC-21; new import) | `DYAD-THM-LPHASE-ROWA-REMAINDER` | (not cited in v0.3.22) | [THM] [scope: block base points in U; row A] | U |
| SH-R0 | §6.14 (FB-16) | §6.15 Relation to S_h; DYAD-THM-SMOOTH-EMBEDDING | (not cited in v0.3.22) | [DEF]; [THM] [scope: C-infinity local germs] | U |
| NF6-DEG10 | VF-1 citation (routed item) | `DYAD-ALG-NF6-DEG10` | (RRF label VF-1) | [ALG] | U |
| NG-DEFECT | §6.13b; §7 row (A1a) | `NUMGEN-DEF-N5AS1-DEFECT` | v1.20.7 §6.6, RID unavailable | [DEF] | U |
| NG-LIFT | §6.13b (definition of the lift) | `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT` | (no RID in v1.20.7) | [DEF] | U |
| NG-INF1 | §6.13b; §7 row (A1a) | `NUMGEN-RESULT-N5AS1-INF1` | v1.20.7 §6.6, RID unavailable | [RESULT] [from: ALG] | U |
| NG-RATIO | §6.13; §7 row | `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` | v1.20.7 | [RESULT] [from: ALG] | U |
| NG-L1 | §6.2; §7 row | `NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION` | v1.15 (source pin), v1.20.7 current at v0.3.22 | [ALG] | U |
| NG-N1C | §6.5; §7 row | `NUMGEN-OPEN-N1C` | v1.15 (source pin), v1.20.7 current at v0.3.22 | CLOSED [RESULT][from: ALG] | U |
| NG-GAPLOCK3 | §2 R6 (HEUR cross-reference); §6.16e | GAP-LOCK Lemma 3 (no RID) | v1.20.7 | [ALG] (owner) | U |

## 6. FB-14 — correction record

- **§6.13, `RECOG-ALG-LATTICE-STRENGTH` paragraph, original sentence:** "No amplitude $Q_{\rm lat}$ at which anisotropic and isotropic quintic content cross exists (both $\propto Q^2$); the "leading-crossing" value $\lvert\mu\rvert/\lvert c_{05}\rvert\approx41.3$ is outside the local regime." **Why ambiguous:** the paragraph works in the post-$H_2$ frame, but $41.3$ is the raw six-step ratio $\lvert\mu\rvert/\lvert c_{05}^{\rm raw}\rvert=41.2694355\ldots$; the post-$H_2$ ratio is $\lvert\mu\rvert/\lvert a_{05}\rvert=59.1194304\ldots$. **Now:** both values with their frames; the conclusion (outside the local regime) holds in either frame.
- **§6.13a, $\lvert G\rvert=0.0076520$** was a rounded equality. Now $\lvert G\rvert=\tfrac{\sqrt{481897}}{90720}\approx0.0076520$ ($=0.0076519842909811940\ldots$). Windows: $\lvert G\rvert/517\approx1.4800743\times10^{-5}$, $\lvert G\rvert/163\approx4.6944689\times10^{-5}$ (were "$=1.48\times10^{-5}$", "$=4.69\times10^{-5}$"). The bounds "$\le0.007652\,Q_0$" and "$\le0.0076520$" elsewhere are valid upper bounds and stay.
- **§6.14 R9 budget:** the threshold was written $\lvert\Lambda_1\rvert/(2C_7)$ with a phase-dependent $\Lambda_1(\Theta)$; it is now $\lvert G\rvert/(2C_7)\approx3.83\times10^{-5}$, $\approx1.28\times10^{-4}$ (same numbers, since $\max_\Theta\lvert\Lambda_1\rvert=\lvert G\rvert$), kept distinct from the windows $\lvert G\rvert/C_2$.
- **Values checked:** `evidence/recog/scripts/recog_v0_3_23_value_checks.py` Part A (exact sympy): A1–A7 PASS.

## 7. Notices

**No notice state changes in this release** (PI decision 2, 23 Oct 2026). Current states as printed in §7.2: G3 to RER as recorded by RER v0.2 §G9 r4.11 (received by the RER preparer via the PI, 21 Oct 2026, `53341b9a…b4b5`); G3 to OFN and to RRF prepared; v0.3.22 notices N-D, N-NG, N-O/R/E prepared; Dyadic N19 and N21 to RECOG prepared by Dyadic and not sent, used as input only. A separate structure for cross-stream notices is to be set up later by the PI.

**§7.3 notification rule — open point for the PI.** The rule asks for pre-release notice of any change to the statement, hypotheses, domain, rows, constants, track or grade of a listed RID. This release:
- changes no statement, hypothesis, domain, row, constant or track of a listed RID;
- adds the pairing tag to two consumed `[RESULT]` RIDs: `RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS` `[from: DEF]` (consumers RRF v0.8.4 §6.3, RER v0.2 G9, OFN v0.10) and `RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH` `[from: ALG]` (OFN v0.10). The pairing records the existing canonical status and does not grade the claim up or down;
- adds RIDs (two maintenance, one FC-21) and the $\approx$ displays of $\lvert G\rvert$, an R9 object, with unchanged value.

Recommendation: treat these as additive or grammatical and notify on release with the hash. If the PI reads the pairing as a grade change, the two consumers are notified before the release.

## 8. Checks

| Check | Tool | Result |
|---|---|---|
| Build, exact-once, base hash asserted | `build_recog_v0_3_23_stage1.py` | 116 edits; intermediate `6a1bdfb0…ec06`; without FC-21: 110 edits, `5cb31667…4345` |
| Stage-1 gates C0–C21 | `check_recog_v0_3_23_stage1.py` | 22/22 PASS (`evidence/recog/v0.3.23/check_stage1_output.txt`); without-FC-21 variant 21/21 PASS (`check_stage1_without_fc21_output.txt`) |
| Negative controls NC01–NC22 | same, `--controls` | 22/22 caught by their target gate: RID removed (C7), RID attached elsewhere (C8), bare and combined RESULT (C9), scope deleted and evidence pointer deleted (C10), OPEN status altered (C6), stale `RID unavailable` and line pin (C12), R9 constant and OPEN 21 rows (C13), header identity (C14), vocabulary (C11), Appendix A history (C3), §8 file name (C16), must-stay-live item (C17), notice state (C20), value display (C19), heading (C15), grade change outside the spans (C21), undeclared RID (C7), old tag form restored (C12) |
| Claim-level audit | `recog_v0_3_23_claim_audit.py` | 34/34 rows U (§5) |
| Values | `recog_v0_3_23_value_checks.py` | Part A exact A1–A7 PASS; Part B `[NUM]` illustration of FC-21 PASS (12 starts, 20000 blocks; not a proof input) |
| Size report (informational, no gate) | `tools/dsn_lint.py --prev` | 345,383 bytes (+16,235, +4.9 %); 1,609 lines; §1 1,286 words; 24 stacked status summaries in the header — compaction is stage 2 (`dsn_lint_stage1.txt`) |

Calibration notes. The checker's RECOG profile was built for this file: header identity lines, heading/anchor list, the RECOG `[RID: …]` grammar with after-text attachment, local alias `[assumes: …]`, OPEN `Status:` lines, §8 file names. C1 BUILD catches every byte change by construction; the controls therefore report which semantic gate catches each mutation. A passing check authorizes nothing.

## 9. Records and evidence of this release

| File | SHA-256 |
|---|---|
| `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` (stage-1 intermediate) | `6a1bdfb062c9233ea56da15760878b73f41f067eea512ddff5ea267b17b4ec06` |
| `records/recog/RECOG_v0_3_23_FC21_PROOF_CELL.md` | `82c2e20400673343ec35ddf8d830d7919cd8a169c222ac994a79529246b50365` |
| `evidence/recog/scripts/build_recog_v0_3_23_stage1.py` | `bf7b4255c8f388e1d9bc061c09df6bc55fdea06c227446f582a05b017577bb3b` |
| `evidence/recog/scripts/check_recog_v0_3_23_stage1.py` | `88fdb80bd7393d80ebdddb2f75cbcefb4504b24257c55d0b653337e4ef87ddb8` |
| `evidence/recog/scripts/recog_v0_3_23_claim_audit.py` | `fcdfd1ef0774b9f1e267833889ad2fbe09ccb972f013e4763303872cd7b96cec` |
| `evidence/recog/scripts/recog_v0_3_23_value_checks.py` | `09a46b96aa6efb48a11ca479496d7b0baa9dee22df0ebf273f20e8c321aa8137` |
| `evidence/recog/v0.3.23/stage1_edits.json` | `8adadb3969127749188bf3d538abd9a93ba9b2ba0a7631087ce98ea4c273266e` |
| `evidence/recog/v0.3.23/stage1_edits_without_fc21.json` | `215188d6c002bc63e6498e99d8841a65f694f892f4eba510fdccf038ac6d1de9` |
| `evidence/recog/v0.3.23/check_stage1_output.txt` | `97d9ea4fbee5824b8799fb1152a085b840c0b1df94016a8994729a300378ad12` |
| `evidence/recog/v0.3.23/check_stage1_without_fc21_output.txt` | `491168c1e2c965925da0ecfcaf4121e794baff8ab37637f12eae5bf0f1eec899` |
| `evidence/recog/v0.3.23/claim_audit.json` | `df4a433c3165aa876f0ff9caf7e6ac22738146f7aa8fc65aa5ea13709f336405` |
| `evidence/recog/v0.3.23/claim_audit_output.txt` | `cb7e489b9545c488c95cdbfeaf7173a11fee6b1bbcf51f6ac7f90dd2ebedd7cd` |
| `evidence/recog/v0.3.23/value_checks.json` | `eb8df08a7fa77c99cc05d4a92cbe25450052c6e44b977f6c505f864cd6fb70fe` |
| `evidence/recog/v0.3.23/value_checks_output.txt` | `20dbcdc90f738c37d0eca8cc921a3e8c4773a7efac936570742204f5ae68697c` |
| `evidence/recog/v0.3.23/dsn_lint_stage1.txt` | `1eac14bbfb08f3fa22ef20512ab761c187a1f2924427a7407886321227b92527` |

Environment: Python 3.13, sympy 1.14, mpmath 1.3; Linux workspace of the RECOG co-owner session. Part B of the value checks is float64; its numbers can differ in the last digits on another platform; its pass thresholds do not depend on them.

## 10. Reviews and adoption

| Step | State |
|---|---|
| Stage-1 change-focused review (co-owner, ChatGPT) | requested |
| Advisory-row check (atlas owner) | requested |
| FC-21 block verdict | requested |
| Stage 2 (compaction, FA-01) | not started; after the stage-1 review |
| PI adoption | — |
| Publication transform, merge, tag `recog-v0.3.23` | — (PI) |
