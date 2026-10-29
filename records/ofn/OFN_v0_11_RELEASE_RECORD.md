# Ontological Foundations (OFN) v0.11 — Release Record

**Status:** DRAFT. Stage 1 is frozen; stage 2 (layout only) is built and checked; the stage-2 file is the adoption candidate. Nothing here is adopted. Until the PI adopts and the tag exists, `ofn-v0.10` remains the governing edition.
**Date:** 29 October 2026
**Prepared by:** Claude, OFN co-owner session `claude012ZC8x` (builder), on branch `claude/ofn-v0.11`.
**Edition:** v0.11, one successor built in two stages, under DSN Methodology v1.4. Stage 1 carries content and contract changes; stage 2 is layout only, checked by `tools/check_compaction.py` against the stage-1 hash.
**Predecessor:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.10`, tag `ofn-v0.10`, SHA-256 `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa`.

Fields marked *(to be filled)* depend on steps that have not happened yet. This record invents no hash, approval or review identifier. Every hash below was computed on the branch files.

## 1. Authorization and reviews

| Step | Source | State |
|---|---|---|
| Advisories | `records/ofn/ATLAS_ADVISORY_OFN_v0_10.md`, `…_INDEPENDENT_CHATGPT.md`, `…_RECONCILIATION.md` (§3 is the 29-row list; §5 is the correction) | merged (#103, #106, #107) |
| Owner dispositions | `records/ofn/OFN_OWNER_DISPOSITION_ADVISORY_v0_10_claude012ZC8x_20261029.md` (PR #108); `…_chatgpt_20261029.md` (PR #109) | open PRs |
| Joint reconciliation | `records/ofn/OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md` (PR #110; both co-owners confirmed; receiving review `records/ofn/OFN_RECONCILIATION_CHATGPT_REVIEW_20261029.md`) | open PR; read at `5e23fc4` |
| PI start | "başla" (29 Oct 2026), given in the OFN session on the reconciliation plan; the PI also authorized the custody intake `upload/ofn-records/` | given |
| Custody intake | branch `upload/ofn-records`, commit `c6fd574`; `upload/ofn-records/SHA256SUMS.txt` lists 20 files (verified 20/20 with `sha256sum -c`) | pushed; atlas hash check and merge pending |
| Change-focused review | `records/ofn/OFN_v0_11_CHATGPT_REVIEW.md` (ChatGPT, commit `5a7ed089`; PR #112 review `5704664058`), on head `b408cef`: ACCEPT SCOPED for the scientific/contract delta; R112-C1 and R112-C2 required, R112-N1 recommended | given |
| Round-2 correction | R112-C1, R112-C2 and R112-N1 applied in the stage-1 content build; stage 2 rebuilt unchanged against the new intermediate (§3a) | done; delta check by the reviewer pending |
| Atlas row check and build replay | `records/ofn/ATLAS_ROW_CHECK_OFN_v0_11.md` | *(to be filled)* |
| Adoption | PI | *(to be filled)* |
| Merge commits; tag `ofn-v0.11` | PI | *(to be filled)* |

The PI will merge PRs #108–#111 before adoption, so that the records this edition cites are on `main` (PI, 29 Oct 2026).

## 2. Identities

| Object | Path | SHA-256 |
|---|---|---|
| Base (adopted v0.10) | `git show ofn-v0.10:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` | `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa` |
| Stage-1 intermediate, round 1 (superseded by round 2; kept in Git history) | `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` at commit `762d273` | `cf38b61b5cd3e268e412dbd10b28a2117f86f1c7423fd2dd33f466a8e5437ce3` |
| **Stage-1 intermediate, round 2 (frozen)** | `evidence/ofn/v0.11/stage1_intermediate.md` (archived byte-exact; the stage-2 base) | `9f31badfa0e7a70a037c3ede3e7f55f852d09f2288508ef38edf343a5172a822` |
| Stage-1 builder | `evidence/ofn/scripts/build_ofn_v0_11_stage1.py` | `b72ebf3c8e50d8bcc88dbb4487f278b33b0e6e4a8b22de37848b5f1f10123361` |
| Stage-1 checker | `evidence/ofn/scripts/check_ofn_v0_11_stage1.py` | `fb31276e41a9ddc036ccbf92f723dafac9bcd88ce5eb5dd57196be74853d0499` |
| Stage-1 edit log (165 edits; old and new text with hashes; document hash chain) | `evidence/ofn/v0.11/stage1_edit_log.json` | `9dda88f1dc1bf51d3a11592909ed4e781642fa0147334ac9fab3e867a0adbea5` |
| Stage-1 checker output (gates and controls) | `evidence/ofn/v0.11/stage1_check_output.txt` | `e5e7450fc7acb6729adfcc65aa5264a0ad0d4c2f76d9c2e295a039aba726eef9` |
| **Stage-2 candidate (v0.11 adoption candidate)** | `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` | `df3c465fb79f049f686f07635d889613e8ab112895cdbcd5af7af029e97400eb` |
| Stage-2 builder | `evidence/ofn/scripts/build_ofn_v0_11_stage2.py` | `15991efcfbda9f27469830bde691456857f73f20d110d5758832cb8fddbec420` |
| Stage-2 owner guards and fixtures | `evidence/ofn/scripts/check_ofn_v0_11_stage2.py` | `518fb68b5b2dc4baa0ca29671cf82878dd8c6d7c76592fb2d5c5f3eb88282ecb` |
| Movement map (16 operations) | `evidence/ofn/v0.11/movement_map.json` | `2e9ea570f56fef4f72907a92bb7a925fe9966e7aaae51dc67fbffa9ec17e3fd4` |
| `tools/check_compaction.py` output and report | `evidence/ofn/v0.11/check_compaction_output.txt`, `…/check_compaction_report.json` | `269a303c871ca705a2f8956117fcb564a30c4556624e2ab9e267a54d067505b0`, `b58ac755ce77157fb5281671a63ee48a064ac09f2b69f78dbf882606b3ee3adf` |
| Stage-2 guard and fixture output | `evidence/ofn/v0.11/stage2_check_output.txt` | `a9737f0aaf1f54376d29c38fba68c8615603c74e17084fb24c2f6f889401d93d` |
| `dsn_lint` stage-2 report (informational) | `evidence/ofn/v0.11/dsn_lint_stage2.txt` | `01970e6ac75051a80922a2ab01673db98b725b73847236668ad6700eb75bb20c` |

**Reproduce stage 1.**
1. `git show ofn-v0.10:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md > base.md`
2. `python3 -I evidence/ofn/scripts/build_ofn_v0_11_stage1.py base.md OUT.md LOG.json` writes `9f31badf…a822` and the log.
3. `python3 -I evidence/ofn/scripts/check_ofn_v0_11_stage1.py base.md OUT.md LOG.json --controls`, run from the repository root.

**Stage-1 gates (all PASS):**
- K1: base identity.
- K2: deterministic rebuild and an intact hash chain.
- K3: all 37 v0.10 OFN RIDs and all 95 anchors kept.
- K4: the 21 OPEN status lines unchanged (20 ACTIVE, 1 PARTIAL).
- K5: the only new OFN RIDs are the six DEF RIDs, each declared once.
- K6: every DYAD, GEN, TDRG, RECOG and NUMGEN RID the file cites is declared at its governing tag.
- K7: no stale phrase in the live text.
- K8: the required statements are present.
- K9: Appendix A, Appendix B up to the v0.10 records, and the inherited Appendix C entries are byte-identical.

**Negative controls (17/17 caught).** Each reintroduces a defect, and the gates must catch it:
- C1 a stale "conditional on DYAD OPEN 20";
- C2 "freeze-candidate";
- C3 the singleton-satisfiable Standard C wording;
- C4 a false Finding A custody transfer;
- C5 a smooth-to-analytic promotion;
- C6 a missing (H_spec);
- C7 transport of the finite-chart bounds;
- C8 a compound `[from: THM + ALG]`;
- C9 a changed OPEN status;
- C10 a dropped v0.10 RID;
- C11 an invented OFN RID;
- C12 an unresolved owner RID;
- C13 an edited history record;
- C14 a compound dash tag.
- C15 the stale map-custody sentence (R112-C1);
- C16 the v0.8.2 handoff as the sole current input (R112-C2);
- C17 the unqualified algebraic-sufficiency sentence (R112-N1).

`tools/dsn_lint.py` was run for information only: +17,695 bytes (+9.1 %) and 26 new RID mentions; it applies no gate.

## 3. Edits by disposition (stage 1)

Row numbers are those of the reconciliation's §3. The fixed dispositions are in `OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md`.

| Row | Fixed disposition | Edits | What changed |
|---|---|---|---|
| 1 | accept: consume the smooth realization | R01a–R01q, R04a | New ledger entries IMP-O10-06 `DYAD-THM-SMOOTH-EMBEDDING` and IMP-O10-07 `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (`dyad-v6.4.22`). A five-row regularity table in §5.5.4. The OFN-local `[ALG]` deduction that the lock surfaces of $\mathcal F_{\kappa,\Phi}$ are real $C^\infty$. The class-C disposition becomes "primary realized smooth mathematical candidate family". The nine sites are restated, including §5.5.3 (ii), IMP-O10-04, OPEN-3B (a $C^\infty$ witness, not closure), OPEN-OPA and OPEN-TRIAD-CLASS |
| 2 | accept with change: widen the test class (contract amendment) | R02a, R21g | §5.5.1 Regularity: real $C^\infty$ germs, with real-analytic laws as a distinguished subclass; Q6-REG stays $C^3$; recorded as OFN11-C02 |
| 3 | accept with change: `[COR]` | R03a–R03c, R21g | `RTG-OFN-DEF-STANDARD-C` is now the local $C^3$ manifold-germ test (the reconciliation's text). Q3a wording aligned. §5.5.5 A2 "loopholes" replaced. Old and new text are in Appendix B as OFN11-C01 |
| 4 | accept | R04a, R01p | SG-19 at the point of use; constants stay edgewise in the dyad chart and are qualitative in Φ; R9 is kept as a stated assumption |
| 5 | accept with change | R05a–R05d, R01m, G10 | RRF §6.2a received as the model-contract row and as the representation-level readout contract; the OPEN-TRIAD-CLASS next artifact and closure criterion updated; no mandatory sign scalar |
| 6 | accept with change | R06a, R01e | One κ table in §5.5.4 carrying the reconciliation's boundaries; γ≡κ is a parameter convention |
| 7 | accept | S03, R07a–R07g, R08d | Finding A: statement accepted by TDR-G and used in SG-14; custody XFER-O08-01 deferred to TDR-G v2.13; the RID stays OFN's |
| 8 | accept with change | R09i, R08a–R08d, R09o, R07d | REQ-O09-05 endpoint component answered at the owner's scope (canonical branch; finite N=24 check; `largest_center` exception). The six-constraint list is still not recovered |
| 9 | accept | G01, G02, R09a–R09q, R09-IMP-O08-* | TDR-G imports repinned to `tdrg-v2.12.14` with the owner RIDs. OFN's caveat on `TDRG-DEF-PHYSICAL-STATE` is kept; `[conv: v18]` and `EV-NOT-RERUN` are kept |
| 10 | accept | R09j, R09k, IMP-O08-07 | OFN08-C12 fulfilled; the OFN statement is unchanged |
| 11 | accept with change (merged text) | R11a | §10 token-sum row: nonconservation at star events, plus the reconciliation's boundary; the TDR-G label question is referred to TDR-G (PR #111) |
| 12, 13 | accept | G07, R12a–R12g | REQ-O09-03 fulfilled (`NUMGEN-RESULT-N5AS1-L-BACKBONE`; $q_m$ typed); consumer rows moved to v1.21; NG-7A changes navigation only |
| 14 | accept | G03, G04, R14a–R14h | REQ-O09-02 fulfilled by the freeze record (`5c00f66d…9b55`). The "freeze candidate" qualification is removed from the live text. RECOG imports repinned to `recog-v0.3.26` (row 23) |
| 15 | accept with change | R15a | RECOG A1c witnesses recorded by exact claim; no event principle; no use of the retracted sentences |
| 16 | accept | G06, R16a–R16h | IMP-O08-12 now cites `DYAD-DEF-PRIMITIVE-MAP`, with the GEN alias; CUST-O09-01 and REQ-O09-04 closed; DYAD v6.4.10 pins moved to v6.4.22 (statements checked) |
| 17 | accept (no action) | — | REQ-O09-06 and REQ-O08-01 unchanged |
| 18 | accept with change | R18a | Q3b route C-a now points to RRF-CND-01 Identity/Action: necessary, not sufficient |
| 19 | accept with change | R19a, R19b | $\chi=S/N_{\rm ch}$ and $N_{\rm ch}$ replace $\rho$ and $N$ in the chiral paragraph; formulas unchanged |
| 20 | accept | G08, R20a–R20e | Triadic v1.6.1 repin; the OFN half of "pass two" recorded in RF-O08-02; Genesis v2.8.5 reference pins labelled as claim-level pins not re-read at `gen-v2.9` |
| 21 (content) | accept with change | H01, H02, S01, S02, R21a–R21k, F01 | Header in v1.4 form; tag-language sentence; v1.4 qualifier spellings; narrow-Q6 `[from: ALG]` (OFN11-C03); count of twenty-one; the stale v0.10 sentence in §0.3 corrected; Appendix B v0.11 records; Appendix C v0.11 entry; footer |
| 22 | accept with change | R22a–R22i | Six DEF RIDs for unchanged bodies; two OPEN blocks pointed to FRUSTRATION / HOLONOMY-RANK and IQP; OPEN-C19-L stays a label |
| 23 | accept with change | G01–G11, H01, S05, R23b–R23e | A governing-editions line in §11.1; repins only where the statement was checked (Dyadic, Genesis imports, TDR-G, RECOG, NUMGEN, RRF, Triadic, Programme, Methodology); unchecked older pins are labelled |
| 24 | accept with change | R24a | The §12.1 evidence row points to `upload/ofn-records/`; custody table in §4 below |
| 25 | defer (v0.3.1) plus scoped v0.3 citation | R25a | RF-O10-03 cites `er2b-v0.3` for its three checked uses; v0.3.1 stays reported, with authentication deferred |
| 26 | accept with change | S04 | One sentence in §0.4 naming the appendix map; no relettering |
| 27, 28 | accept | R28a–R28d, R07e | Receipts of DYAD N4, N6 and N14, Genesis IF32 and RRF §6.2a recorded in §11 and §12.3; notices follow after the tag (§6) |
| 29 | accept | (PR #110) | The three `pipes/OFN/` notices are dispositioned `accept`; they are closed after the tag |

**Live-file exceptions kept on purpose in stage 1 and removed as layout in stage 2 (§7):**
- the v0.9 boundary paragraph in §0.1;
- the v0.8, v0.9 and v0.10 adoption paragraphs in §0.3;
- the "*v0.10:*" paragraph in §9;
- the "Reconciliation input (v0.10)" labels;
- the v0.9 release narrative and the v0.10 assembly text in §§12.1, 12.2 and 12.5;
- the Draft entries in Appendix C.

## 3a. Round 2: corrections from the change-focused review

The review (`records/ofn/OFN_v0_11_CHATGPT_REVIEW.md`) accepted the scientific and contract delta and found two current-state inconsistencies plus one clarification. Each was checked against the round-1 intermediate before it was applied.

All three are applied in the stage-1 content build, not in the layout stage or in finalization. The round-1 intermediate `cf38b61b…7ce3` stays in Git history (commit `762d273`).

| Finding | Edit | Site | Change |
|---|---|---|---|
| R112-C1 (required) | R16i (row 16) | §11.2 IMP-O08-13 | "separate map-definition custody remains unresolved" is replaced. Custody is now resolved separately: `DYAD-DEF-PRIMITIVE-MAP`, with the `GEN-DEF-PRIMITIVE-MAP` alias, via IMP-O08-12, CUST-O09-01 and REQ-O09-04. The order-six result stays distinct from map custody and generator selection |
| R112-C2 (required) | R21l (row 21) | §5.5 "Source and status" | v0.8.2 becomes "historical integration input for v0.10", keeping its hash and the v0.10 registration. The v0.11 changes are governed by the joint reconciliation and this record (OFN11-C01/C02; IMP-O10-06/07) |
| R112-C2 (required) | R21m (row 21) | §12.1 handoff row | The Consequence cell becomes "historical single integration input for v0.10 §5.5", amended in v0.11; it keeps "co-owner handoff acceptance, not adoption" |
| R112-N1 (recommended) | R03e (row 3) | §5.5.2 physical-isolation scope | $I_e\equiv0$ satisfies the order-four bound only on a regime that meets the manifold, nontriviality, domain and clock requirements. Algebraic cancellation alone establishes neither those requirements nor physical isolation |

**Effect on the file:** four lines change between round 1 and round 2. No RID, status, grade, OPEN or contract decision changes.

**Checks:**
- K7 and K8 carry the new phrases.
- Controls C15–C17 are added; the stage-1 checker now reports K1–K9 PASS and 17/17 controls caught.
- The stage-2 builder is unchanged apart from its base-hash constant, and it reruns cleanly on round 2.

## 4. Custody (row 24)

| Artifact | SHA-256 | State |
|---|---|---|
| v0.10 release record (with N-O10-1–4) | `10a1ec6b…0844` | uploaded to `upload/ofn-records/` (not yet merged) |
| `build_ofn_v0_10_draft1.py`, `build_ofn_v0_10_draft2.py`, `release_ofn_v0_10.py` | `6a4fe7af…58ff`, `930b0aef…5c82`, `2aca119f…4f5f` | uploaded |
| Draft 1, Draft 2 | `d94e1e39…8c36`, `58e2dec5…3610` | uploaded |
| SESSION scripts: `iso_check.py`, `iso_quadratic_nogo.py`, `transported_pq.py`, `transported_sim.py`, `basin_test.py`, `OFN_PSI_KAPPA_EXTENSION_v0_1.py`, `OFN_PSI_KAPPA_ALL_MINOR_CHECK_v0_1.py`, `OFN_PSI_INVARIANT_C_CHECK_v0_1.py`, `OFN_PSI_INVARIANT_C_GAUGE_CHECK_v0_1.py`, `OFN_PSI_REFLECTION_AUDIT_v0_1.py`, `OFN_STAB_F3_CHECK_v0_1.py` (11 of 12), plus `k3_six_step_factor_check.py` | as listed in `SHA256SUMS.txt`, equal to the prefixes printed in OFN | uploaded |
| v0.8 input reviews `OFN_SOURCE_REVIEW_ER2B_GEN288_OPEN3_v0_1_1.md`, `…_ADDENDUM_…_v0_1.md` | `8d18640f…0944`, `f86cd483…c5b8` | uploaded |
| `RTG_ONTOLOGICAL_FOUNDATIONS_v0_8_RELEASE_RECORD.md` | `0015347c…0848` | held by the ChatGPT session; not uploaded |
| `transported_chiral_pq.py` (`09129ffc…73ac`) | — | **missing** (neither OFN session holds it) |
| FMS ψ scripts (`ad44f66a…`, `5af23da9…`); ER-2B v0.3.1 (`711e427a…81b4`, reported) | — | missing from both OFN sessions; to be asked of FMS and the PI |
| `REVIEW_FINDINGS.md`, `OFN_TDRG_FINDING_A_HANDOFF.md`, `OFN_v0_9_PROGRAMME_AND_OWNER_SYNC_REQUEST.md`, v0.9 release record and validation files | — | missing from both OFN sessions |
| RECOG v0.3.20 freeze record | `5c00f66d…9b55` | placed (`records/recog/`) |

No historical record is reconstructed. Once the v0.10 release record is placed, BASELINE's authority row for OFN can point to it.

## 5. Inbox `pipes/OFN/`

| Item | Disposition | State |
|---|---|---|
| `20261026-NUMGEN-v1-21-adopted.md` | `2026-10-29 · accept · records/ofn/OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md` (rows 12, 13) | dispositioned (PR #110); closed after the tag |
| `20261028-TDRG-v2-12-14-adopted.md` | the same (rows 7–11) | dispositioned; closed after the tag |
| `20261029-RECOG-v0-3-26-adopted.md` | the same (rows 14, 15, 23) | dispositioned; closed after the tag |

Filed by OFN: `pipes/TDRG/20261029-OFN-token-sum-gauge-label.md` (`kind: finding`; PR #111).

## 6. Affected consumers (what would be notified after the tag)

| Consumer | Notice content |
|---|---|
| DYAD | Receipts of N4, N6 and N14. Adopted use of `DYAD-THM-SMOOTH-EMBEDDING`, `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` and `DYAD-DEF-PRIMITIVE-MAP` (IMP-O10-06/07, IMP-O08-12) |
| GEN | G-20 existence note received; C2 used through the DYAD chart; imports repinned to `gen-v2.9` |
| RRF | §6.2a received. The phrase "OFN has not separately adopted" is now stale, because OFN adopts the $C^\infty$ class-C reading at §5.5.4 scope. The readout entry is accepted as the representation-level readout contract |
| TDR-G | Finding A receipt state recorded. Owner RIDs used. REQ-O09-05 endpoint component closed. The label finding is filed separately (PR #111) |
| NUMGEN | REQ-O09-03 closed; consumer rows moved to v1.21 |
| RECOG | REQ-O09-02 closed through the freeze record; imports at `recog-v0.3.26`; A1c witnesses recorded by claim |
| FMS / ER-2B | Class C now has a real $C^\infty$ mathematical realization; analytic realization and physical selection stay open. Standard C has been corrected and the test class widened; their co-owners update their own wording (row 27) |
| Programme | OFN v0.11 is the criteria home for P0 and P2B; repin at the Programme's next edition |

## 7. Stage 2 (layout only)

**Base:** the frozen stage-1 intermediate, round 2, `9f31badf…a822`. It is also the only archive, committed byte-exact; every removed byte is in it. The tag `ofn-v0.10` holds the v0.10 and earlier history verbatim, and the live pointers name that tag.

**Operations** (`evidence/ofn/v0.11/movement_map.json`):

| Op | Class | What moves |
|---|---|---|
| S2-H | replace-header | The Document status line only (stage-1 wording becomes stage-2 wording). The status summary and the other fields are unchanged |
| S2-E01 | history-removal | §0.1 v0.9 revision-boundary paragraph |
| S2-E02 | history-removal | §0.3 v0.8/v0.9 and v0.10 adoption paragraphs; the Draft-2 hash moves to the Appendix C v0.10 entry |
| S2-E03 | history-removal | §6.4 closing history sentence |
| S2-E04 | history-removal | §9 "*v0.10:*" paragraph. The current count (twenty-one; twenty ACTIVE, one PARTIAL) stays in the paragraph above it |
| S2-E05–E07 | history-removal | " (v0.10)" in the three "Reconciliation input" labels |
| S2-E08, E09 | history-removal | §12.3 sentence on the adopted v0.9 release; resolved RECOG/NUMGEN mismatch sentence |
| S2-E10, E11 | history-removal | §12.4 REQ-O08-07 history sentence; the clause naming the v0.9 reconciliation |
| S2-S1 | history-section | §12.1: the v0.9 register becomes a pointer. The RECOG row and the four evidence rows still cited are kept byte-identical apart from the removed "*v0.10:* " labels; the v0.8 baseline hash moves to the Appendix C v0.9 entry |
| S2-S2 | history-section | §12.2: v0.9 adoption narrative becomes a pointer |
| S2-S5 | history-section | §12.5: v0.10 decision table and assembly record become a pointer (heading "Edition Decisions") |
| S2-T | history-appendix | Appendix C keeps its letter and becomes "Compact Version History": one entry per edition (the v0.11 bullets unchanged plus a layout line; v0.10, v0.9, v0.8 and v0.7 compact; v0.1–v0.6 one line); the footer becomes one line. Profile key `base_history_from: "## Appendix C — Version History"` |

**`tools/check_compaction.py`: PASS.**
- Re-derivation is exact.
- All 16 operations pass their class rules.
- 188/188 claim blocks are byte-identical.
- RIDs, heading anchors, source hashes and qualifiers are preserved.
- References resolve.
- Header and footer pass.

**Owner guards (`check_ofn_v0_11_stage2.py`): G0–G10 PASS.**
- G1: rebuild identical.
- G2: 43 RTG-OFN RIDs and 43 declarations kept, and every §§0–11 mention kept.
- G3: 100 anchors kept.
- G4: 21 OPEN status lines unchanged.
- G5: in §§0–11, 134 claim tags, 13 qualifiers and 471 math spans unchanged.
- G6: 31 register rows of §§12.3–12.4 kept.
- G7: Appendices A and B byte-identical.
- G8: only the Document status line differs in the header.
- G9: the history region is relocated, and every identifier in the new Appendix C occurs outside it.

**Fixtures:** 14 of 14 caught (F1–F14).

**Two tool limits, covered by owner guards:**
1. The tool's RID pattern does not track `RTG-OFN-*`, because it skips a prefix preceded by "RTG-". G2 and G6 carry that check (fixtures F11 and F12).
2. OFN's history appendix is Appendix C, and the tool counts Appendix C as live text. Its history-appendix identifier test therefore finds each identifier in the new entry itself and cannot fail. G9 carries that check (fixture F5).

These limits are worth a note to the tool owner; no tool change is made here.

**Size (`dsn_lint`, informational):**
- 192,142 bytes and 1,581 lines.
- Against stage 1: −21,785 bytes (−10.2 %).
- Against `ofn-v0.10`: −3,318 bytes (−1.7 %).

No claim, RID, grade, status or OPEN changes in stage 2.

**Reproduce stage 2.** Run from the repository root:
1. `python3 -I evidence/ofn/scripts/build_ofn_v0_11_stage2.py evidence/ofn/v0.11/stage1_intermediate.md OUT.md MAP.json` writes `df3c465f…00eb` and the map.
2. `python3 -I tools/check_compaction.py evidence/ofn/v0.11/stage1_intermediate.md dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md evidence/ofn/v0.11/movement_map.json`
3. `python3 -I evidence/ofn/scripts/check_ofn_v0_11_stage2.py evidence/ofn/v0.11/stage1_intermediate.md dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md evidence/ofn/v0.11/movement_map.json --fixtures`

## 8. Adoption *(to be filled)*

The PI adopts the stage-2 candidate, or a candidate revised after review. A finalization step then changes the adoption-state wording only, and a checker confirms that nothing else differs. It touches:
- the Document status line and Supersedes ("on adoption");
- the §0.3 "*v0.11 (adoption pending):*" label;
- the §12.3 six-DEF row;
- the Appendix B "(adoption pending)" heading;
- the Appendix C v0.11 heading;
- the footer.

After that step:
1. The PI merges and tags `ofn-v0.11`.
2. The three `pipes/OFN/` items are closed.
3. The §6 notices are filed.
