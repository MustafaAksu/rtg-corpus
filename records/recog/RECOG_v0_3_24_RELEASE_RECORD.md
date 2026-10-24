# RECOG v0.3.24 — Release record (stage 1 reviewed; stage 2 built; not adopted)

**Study:** RECOG · **Base (governing edition):** `recog-v0.3.23`, DSN SHA-256 `0d5834003ce8f6819a760ac02ec4e1b65c4d34a0eb13381d0fe4e175af9ca31a` (281,915 bytes).
**Stage-1 intermediate (round 2):** `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` on `claude/recog-v0.3.24-stage1`, SHA-256 `881be125201180b987e1f430390507c10f4167df29c19c0b19fbd07eb6dee03c`. Round 1 (commit `5312dd3`): `3ef2dfd03a63eecbf3394a224909285117b9ca25ee588bb86f51921393400984` (294,370 bytes), reviewed in #5639519847; round 2 applies that review's three text corrections in place (§2a). A build stage, not an edition: header identity lines, status summary and footer are untouched; the Appendix A entry is a DRAFT line.
**Date:** 24 October 2026 · **Builder:** RECOG co-owner (Claude). **Method:** DSN Methodology v1.4 two-stage release; CONVENTIONS.md.
**Decision basis:** PI decisions of 23–24 Oct 2026 (`START A1b/A1c`, `A3 AUTHORIZED`, `PREPARE A1B THEOREM CANDIDATE — APPROVED`); receiving review #5638910665 on PR #30 (`A1B/A1C CANDIDATE ACCEPTED — STAGE-1 PREPARATION RECOMMENDED`), which also set the grouping below: **three scientific acceptance decisions (A1b, A1c, A3) and one structural-maintenance acceptance**, each separate.

## 1. Groups and their acceptance decisions

| Group | Kind | Content | New RIDs | Source cell and reviews | Decision (PI) |
|---|---|---|---|---|---|
| **A1b** | scientific | `[THM]` slip schedule on explicit $U$ (§6.13b): (A) events = lift crossings; (C′) six-step deficit $0.927\tau Q<\Delta<\tau Q+1.82Q^{3/2}$ on $U_T$; (B) alphabet $\{6,7\}$, $s(M)=\tfrac{3\tau}\pi\log M+O(1)$; (S) $\tau\psi(a+M_k)-(k-1)\tfrac\pi3=L+\varepsilon_k$ with explicit ceiling | RECOG-THM-A1B-SLIP-SCHEDULE-U; RECOG-ART-A1B-SIXSTEP-DEFICIT | PR #23 cell v0.2.2 (`1ef20de`, `205c68ef…eb23`); PR #30 candidate v0.2.1 (`01de252f…333d`; v0.2 at `9777685`, `4d1719ba…9fbb`); reviews #5630982748, #5631395296, #5634312954 (ACCEPTED), #5638820480, #5638910665 | pending |
| **A1c** | scientific | `[RESULT]` `[from: THM]` infinite-record phase readout (§6.16e); two OPEN R6 sub-items (A1c-Q1′ injectivity; A1c-decoder); §5 readout guard | RECOG-RESULT-A1C-RECORD-PHASE-READOUT | same cell §3; reviews as above (limited corrections of #5638820480 applied in candidate v0.2 and cell v0.2.2) | pending |
| **A3** | scientific | `[ALG]` quadrature typing (§6.5): extremal radial transfer; $\Omega$-area-neutral locus relative to the declared Haar form; type not chart-invariant (explicit charts); no multiplier signature forced. `[ALG]` pole-stratum periodic inventory (§6.3): $e^\rho-1=m\pi$, new odd-$m$ period-2 family. R4 sub-item 1 answered in reframed form; R4 ACTIVE | RECOG-ALG-QUADRATURE-TYPING; RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY; RECOG-ART-A3-QUADRATURE-TYPING | PR #28 record v0.2 (`0ab5ff5`, `262e2529…1d17`); reviews #5634320866, #5638545763 (`A3 SCIENTIFIC SESSION ACCEPTED`) | pending |
| **MNT** | structural maintenance | follow-up obligation of the v0.3.23 release record §11 (stage-1 part): current status at the point of use; the tagged history stays at `recog-v0.3.23` and is pointed to — R8 and R9 v0.3.2 specifications, the former R11 text with its `[OPEN]` sub-items, the R7 heading over closed items, the §7.1/§7.2 audit tables and the G2 "unchanged" sentence of §6.13b, §9 archive line, §7 synchronization note pointer | none | this record; checker gate C22 | pending |

Not in stage 1: the SG reorder (R13 and R14 before R12) — a layout move for stage 2 (`tools/check_compaction.py`). No RID renamed or regraded; no OPEN status word changed (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED).

## 2. Build

- Builder: `evidence/recog/scripts/build_recog_v0_3_24_stage1.py` (assertion-gated; modes `str`, `line`, `span`; Appendix A masked for live edits; `--only GROUP` builds a single-group variant). Base file kept as `evidence/recog/v0.3.24/base_v0_3_23.md` (= `git show recog-v0.3.23:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`).
- Edit log: `evidence/recog/v0.3.24/stage1_edit_log.json` (29 edits, old and new text with hashes).
- Decoupling variants (`evidence/recog/v0.3.24/variants/`, round 2): A1B alone `5508f2a6…27a0` (8 edits); A1C alone `0e918314…e326` (4); A3 alone `699c9a7b…9460` (8); MNT alone `07a1d910…07ee` (12). Round-1 values: A1C `54566c63…4bd4`, MNT `edb48503…d615`. Each carries exactly its own new RIDs (checker C18).

| Key | Group | Location | Mode |
|---|---|---|---|
| S1-A1B | A1B | §1 A1a paragraph: slip schedule summary | str |
| S1-A3a | A3 | §1 fixed points: pole-stratum periodic inventory | str |
| S1-A3b | A3 | §1 candidate strata: quadrature content | str |
| S2-R4 | A3 | §2 OPEN R4 sub-items (R4 stays ACTIVE) | str |
| S2-R6 | A1C | §2 OPEN R6: three new sub-items after CELL-F4 (one ✓ RESULT pointer, two `[OPEN]`) | str |
| M-R8a | MNT | §2 R8 status sentence: specification is history at the tag | str |
| M-R8b | MNT | §2 R8: v0.3.2 target block replaced by a pointer | span |
| M-R9a | MNT | §2 R9 status sentence: specification is history at the tag; certified pointers | str |
| M-R9b | MNT | §2 R9: v0.3.2 specification block (incl. degree-7 budget) replaced by a pointer; retired-route sentence kept | span |
| M-R11 | MNT | §2 R11: former v0.3.1 text with its five `[OPEN]` sub-items replaced by a pointer | span |
| M-R7 | MNT | §2 R7: "Active sub-items" heading over closed items relabelled | str |
| S3-SGR3 | A3 | §3 SG-R3 violation line: pointer to the typing record | str |
| S5-R6 | A1C | §5 event-rule row: readout guard | str |
| S63-A3 | A3 | §6.3: pole-stratum periodic inventory block | str |
| S65-A3 | A3 | §6.5: quadrature typing block after the discriminant | str |
| S613-G2 | MNT | §6.13b: G2 "unchanged" sentence to history | str |
| S613-A1B | A1B | §6.13b: A1b theorem block after the FC-21 scope paragraph | str |
| S616e-A1C | A1C | §6.16e: A1c readout result before §6.16f; round 2: separate `[NUM]` sentence for the record-only decoder-error measurement | str |
| S7-note | MNT | §7 synchronization note: §7.1–§7.2 are summaries | str |
| S7-C21, S7-PRIMCTR, S7-NFREM, S7-LPHASE | A1B | §7 import rows: new A1b uses (C21; PRIM-CTR; NF-REM ingredients; LPHASE row A / branch (B)) | str |
| M-71 | MNT | §7.1: v0.3.18 audit table, consumer-direction note and OFN notices → summary + pointer; round 2: exact RID spellings | span |
| M-72 | MNT | §7.2: v0.3.21 audit table and scope notes → summary + pointer (receipts table and outbound-notices paragraph unchanged) | span |
| S8-A1B | A1B | §8 artifact row RECOG-ART-A1B-SIXSTEP-DEFICIT | line |
| S8-A3 | A3 | §8 artifact row RECOG-ART-A3-QUADRATURE-TYPING | str |
| S9-arch | MNT | §9 archive line | str |
| A-1 | all | Appendix A: v0.3.24 DRAFT entry (per variant) | str |

Per-group `[RESULT]` pairing: the one new `[RESULT]` block (A1c) is paired `[from: THM]` with `Depends on:` the same-release THM (Methodology v1.4 §3.4); no existing block touched.

## 2a. Round 2 — corrections from the stage-1 review (#5639519847 on `5312dd3`: `STAGE-1 TWO GROUPS ACCEPTED (A1B, A3); TWO GROUPS CONDITIONALLY ACCEPTED (A1C, MNT)`)

| Item | Correction | Edit |
|---|---|---|
| A1C-1 | the "factor 2–6" figure is the absolute error of the fitted record-only pair decoder on four sampled comparator-fiber pairs (cell §5: $2.1$–$5.6$), not a finite-prefix window bound; removed from the `[RESULT]` sentence and stated as a separate `[NUM]` sentence (Methodology v1.4 §3.4) | S616e-A1C |
| A1C-2 | "Known: record level sets have empty interior" removed from the OPEN R6 sub-item; marked as a `[SESSION]` conjectural observation with an open proof obligation; neither answer established | S2-R6 |
| MNT-1 | §7.1 summary names the exact owner RIDs `RECOG-DEF-POLE-COMPARATOR` and `RECOG-DEF-STATE-COMPARATOR`; checker gate C23 and control NC21 added | M-71 |
| process | atlas row check recorded as PI-DEFERRED (§6); no atlas edit or PR | — |

The theorem candidate record was aligned in the same two sentences (v0.2.1). A1b and A3 texts unchanged. Certificates not rerun.

## 3. Checks

- `evidence/recog/scripts/check_recog_v0_3_24_stage1.py` — 24 gates C0–C23 **all PASS**; 21 negative controls each caught by its target gate (`evidence/recog/v0.3.24/stage1_check_output.txt`). Gates of note: C6 status words unchanged (only the two declared R8/R9 history sentences differ); C7/C8 RID set and attachments; C16 every file named in §8 exists in the repository and every SHA-256 quoted in the new §8 rows is the hash of the named file; C19 the displayed constants agree with the certificate JSONs (A1b: $H<1.783$, $1.8170$, $1.7876$, $0.92725$; A3: chart instances, 18 orbits, 11 uncertified, none on the quadrature); C20 the §7.2 outbound-notices paragraph is unchanged; C22 every MNT pointer names `recog-v0.3.23` and the moved passages exist there.
- Claim audit `evidence/recog/scripts/recog_v0_3_24_claim_audit.py` → `evidence/recog/v0.3.24/claim_audit.json`: the quoted owner statements are present in the current source at its tag — Dyadic `dyad-v6.4.22` (`2363ca40…8c29`): LPHASE row A with branch $\varepsilon\le0.04654$ and $\tfrac{403}{250}$; NF-REM ingredients (vector ceilings, tail $332000|W|^{10}$ on $|W|\le\tfrac1{16}$); PRIM-CTR; C21; §1 winding fixed points; RECOG `recog-v0.3.23`: the A1a RIDs, the token schema and the pole-comparator definition; RRF `rrf-v0.8.4`: the wrapped profile name. ALL PRESENT. (Presence at the cited RID in the current source; not a comparison with earlier editions.)
- Certificates (not rerun for this build; unchanged since their cells): `recog_a1b_sixstep_deficit_cert.py` (10/10 gates), `recog_a3_quadrature_typing.py` (8/8 gates + probe); hashes in §8 of the intermediate and in the §1 table above.
- Vocabulary: no READ/WRITE/DECODE in the DSN (C11); the scientific blocks speak of crossings, records and readout.

## 4. Notices (prepared; separate states; none sent)

| Recipient | Kind | Content | State |
|---|---|---|---|
| NUMGEN | informational | explicit-$U$ instance of the GAP-LOCK slip law (RECOG-THM-A1B-SLIP-SCHEDULE-U) with identified constant $L$ and error order; custody unchanged; NUMGEN's adopted domain and grades untouched | prepared, not sent |
| Dyadic | use notice | new RECOG uses: DYAD-THM-LPHASE-ROWA-REMAINDER (branch (B)), DYAD-THM-NF-REM ingredients (tail and vector ceilings), DYAD-THM-PRIM-CTR, DYAD-THM-C21 (the A1b certificate reproduces C21 and the §6.2 quartic real-ray value — a free cross-check, not a Dyadic RID) | prepared, not sent |
| RRF | interface question (informational) | whether the multiplicative Haar form $\Omega=d\bar\zeta\wedge d\zeta/(2i|\zeta|^2)$ on the wrapped native ratio is to be registered as a derived object of the wrapped profile; RECOG-ALG-QUADRATURE-TYPING (2c) stays `[scope: relative to declared Ω]` until answered; no OPEN-A bearing | prepared, not sent |
| Atlas | row update | new RIDs; R4 and R6 sub-item changes; census | at release |

Routed through the PI; no notice state is recorded before a real dispatch. The v0.3.23 notices remain in their recorded states.

## 5. Stage 2 — layout-only compaction (built; PI decision `STAGE-2 PREPARATION APPROVED`, 24 Oct 2026)

**Base:** the reviewed stage-1 round-2 intermediate `881be125…e03c` (commit `e42c81c`; kept as `evidence/recog/v0.3.24/stage1_intermediate_round2.md`). **Candidate:** `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`, SHA-256 `63f36a9e4826e92ce6986f9fe722d3a08ac13ff050ce5fbcef2d1ea10866cc35`. Builder `evidence/recog/scripts/build_recog_v0_3_24_stage2.py`; movement map `evidence/recog/v0.3.24/movement_map.json`.

| Op | Kind | What moves | Where it now is |
|---|---|---|---|
| M01 | move (class reorder) | the scope guard **SG-R12** (522 bytes, byte-identical), formerly after SG-R14 | §3, in its numerical place before SG-R13 |

Nothing else changes: no archive is named because nothing is removed or relocated out of the live text (the stage-1 pointers to `recog-v0.3.23` were verified by stage-1 gate C22; see the map's `archives_note` for why naming that tag as an archive here would misread the version strings of those pointer sentences). Header identity lines, status summary and the Appendix A DRAFT entry stay as in stage 1; the release script sets them at adoption, as for v0.3.23.

**Checker extension (general-purpose, byte-preserving).** `tools/check_compaction.py` gains the operation `move` (class `reorder`): one whole blank-line-delimited block is cut and reinserted byte-identical before a unique anchor that itself starts a block, inside the same `##`/`###` section of the live text; the operation carries no old/new text, so it can change no prose, tag, qualifier, RID, math or hash (re-derivation; block-multiset test; header excluded; section test). Regression: the DYAD v6.4.21 triple still PASSES with 16/16 controls rejected (`dyad_regression_test_check_compaction.txt`); the RECOG v0.3.23 triple (`97b0425` → `4e7efd9`) still PASSES with 17/17 (`recog_v0_3_23_regression_test_check_compaction.txt`). No existing check was removed or relaxed.

**Checks.** `tools/check_compaction.py` on the triple: PASS (`check_compaction_output.txt`, `check_compaction_report.json`): re-derivation byte-exact; 456 claim blocks in the base live text, 456 byte-identical; RID set, heading anchors, source hashes, qualifier tags preserved; references resolve; presentation. **Move-specific negative controls** `evidence/recog/scripts/test_check_compaction_move.py`: 12/12 rejected — a word changed inside the moved block (candidate only; and with the declared block changed to match), block moved into another section, into the header, duplicated, deleted under a declared move, anchor splitting a paragraph, anchor not unique, declared block off by one byte, a second undeclared reorder, wrong class, a grade changed outside the move (`negative_controls_move_output.txt`, `_report.json`). `tools/dsn_lint.py` informational report: `dsn_lint_stage2.txt`.

**Must-stay-live list (FA-RECOG-01, as for v0.3.23):** F2(a3) selection question, registry-relative limits, RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH and the R6 remaining question, W1–W5, the R6 status line — all byte-identical (claim-block check: 456/456).

## 6. Reviews and adoption

| Stage | Reviewer / decision | Outcome |
|---|---|---|
| Stage 1 — group A1b | co-owner (ChatGPT), review #5639519847 on `5312dd3` | ACCEPTED |
| Stage 1 — group A1c | same | CONDITIONAL ACCEPTANCE — A1C-1, A1C-2 applied in round 2; limited-diff check pending |
| Stage 1 — group A3 | same | ACCEPTED |
| Stage 1 — group MNT | same | CONDITIONAL ACCEPTANCE — MNT-1 applied in round 2; limited-diff check pending |
| Stage 1 — atlas row check | atlas owner | PI-DEFERRED (the PI postponed atlas changes; not a stage-1 gate; no atlas edit or PR) |
| Stage 2 (compaction) | co-owner (ChatGPT), mechanical review | pending |
| Adoption | PI | — |

Requested of the stage-1 review: (i) each science block against its accepted cell (no strengthening in transit; the Q1′ scope note and the finite-prefix wording as corrected); (ii) the MNT pointers against `recog-v0.3.23` (checker C22) and the must-stay-live list (F2(a3), W1–W5, R6 ACTIVE, registry-relative limits, no write-through; C17); (iii) the §7 import-row uses; (iv) the four variant hashes.

## 7. Records and evidence of this release

- `records/recog/RECOG_A1B_A1C_SESSION_v0_1.md` v0.2.2 — `205c68ef56e432bd98267efccaab3975b2daca7e94ca3bd545277b268c9feb23`
- `records/recog/RECOG_A1B_THEOREM_CANDIDATE_v0_1.md` v0.2.1 — `01de252f33757cfc003635785a7bbf826c57960a59925cd6943f7b06af97333d` (v0.2: `4d1719ba…9fbb`)
- `records/recog/RECOG_A3_QUADRATURE_TYPING_SESSION_v0_1.md` v0.2 — `262e2529a9288ddf56e1842f074a12bcaf66f43e96cc53f3cd12b939c1cd1d17`
- `evidence/recog/scripts/recog_a1b_sixstep_deficit_cert.py` — `b418af086dfb7515faff5d266a7ea1d2e7f76efb74421021268c14495a1b35b0`; output `evidence/recog/a1b_a1c/a1b_sixstep_deficit_cert.json` — `cc1f7e30def4defd8d8cb7af89aafe75b4207d3d6d0ab571e0ca20d78ce7c8f1`
- `evidence/recog/scripts/recog_a1b_a1c_explicit_u.py` — `cc964a51ee746f2cb6d8be6f85765fab8dd5766f212f097075e547d56b7be2c2`; output `evidence/recog/a1b_a1c/a1b_a1c_explicit_u_2e6.json` — `0ea54e81cfbe7a9b528eb121aba054023ad0726fdcd85b4aec3f68f2fc988dcb`
- `evidence/recog/scripts/recog_a3_quadrature_typing.py` — `936d4c97950b53085b019411616324450a79b3c762b19a5688c06e53acb93e6b`; output `evidence/recog/a3_quadrature/a3_quadrature_typing.json` — `65475ba57b48e17055b810dace404aaf964e194d79c2a63626fccd5965291e70`
- Stage-1 build and checks: `evidence/recog/scripts/build_recog_v0_3_24_stage1.py`, `check_recog_v0_3_24_stage1.py`, `recog_v0_3_24_claim_audit.py`; `evidence/recog/v0.3.24/` (base, edit log, variants, check output, claim audit).
- Stage-2 build and checks: `evidence/recog/scripts/build_recog_v0_3_24_stage2.py`, `test_check_compaction_move.py`; `tools/check_compaction.py` (move operation); `evidence/recog/v0.3.24/` (stage-1 round-2 intermediate, movement map, checker report and output, move controls, DYAD and RECOG v0.3.23 regression outputs, lint).
- The branch `claude/recog-v0.3.24-stage1` contains the merged cell branches of PRs #23, #28 and #30 (their files are cited by §8 of the intermediate and checked by C16).

## 8. Adoption

Not adopted. (To be completed by the PI after the stage-1 and stage-2 reviews: decision text, adopted hash, per-group scope, publication, notices.)
