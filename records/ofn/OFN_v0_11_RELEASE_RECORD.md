# Ontological Foundations (OFN) v0.11 — Release Record

**Status:** ADOPTED by the PI on 30 October 2026 (§8). Published file `38a2f444…e9e4` = the accepted candidate `df3c465f…00eb` plus the adoption-state lines only. The edition governs once the PI has merged PR #112 and created the tag `ofn-v0.11`; until then `ofn-v0.10` is the tagged edition.
**Date:** 29 October 2026
**Prepared by:** Claude, OFN co-owner session `claude012ZC8x` (builder), on branch `claude/ofn-v0.11`.
**Record update:** 30 October 2026 — ChatGPT, OFN co-owner: Atlas receipt, prerequisite-record merges and nonblocking dispositions; candidate bytes unchanged.
**Edition:** v0.11, one successor built in two stages, under DSN Methodology v1.4. Stage 1 carries content and contract changes; stage 2 is layout only, checked by `tools/check_compaction.py` against the stage-1 hash.
**Predecessor:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.10`, tag `ofn-v0.10`, SHA-256 `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa`.

Fields marked *(to be filled)* depend on steps that have not happened yet. This record invents no hash, approval or review identifier. Every hash below was computed on the branch files.

## 1. Authorization and reviews

| Step | Source | State |
|---|---|---|
| Advisories | `records/ofn/ATLAS_ADVISORY_OFN_v0_10.md`, `…_INDEPENDENT_CHATGPT.md`, `…_RECONCILIATION.md` (§3 is the 29-row list; §5 is the correction) | merged (#103, #106, #107) |
| Owner dispositions | `records/ofn/OFN_OWNER_DISPOSITION_ADVISORY_v0_10_claude012ZC8x_20261029.md` (PR #108); `…_chatgpt_20261029.md` (PR #109) | merged; exact heads and merge commits below |
| Joint reconciliation | `records/ofn/OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md` (PR #110; both co-owners confirmed; receiving review `records/ofn/OFN_RECONCILIATION_CHATGPT_REVIEW_20261029.md`) | merged; confirmed reconciliation read at `5e23fc4`, final reviewed PR head `6a0b898` |
| PI start | "başla" (29 Oct 2026), given in the OFN session on the reconciliation plan; the PI also authorized the custody intake `upload/ofn-records/` | given |
| Custody intake | branch `upload/ofn-records`, commit `c6fd574`; `upload/ofn-records/SHA256SUMS.txt` lists 20 files; Atlas hash check `records/ofn/OFN_UPLOAD_HASH_CHECK_20261030.md` | 20/20 verified by Atlas; PR #116 merged; originals remain unchanged under `upload/ofn-records/` |
| Change-focused review | `records/ofn/OFN_v0_11_CHATGPT_REVIEW.md` (ChatGPT, commit `5a7ed089`; PR #112 review `5704664058`), on head `b408cef`: ACCEPT SCOPED for the scientific/contract delta; R112-C1 and R112-C2 required, R112-N1 recommended | given |
| Round-2 correction and receiving review | R112-C1, R112-C2 and R112-N1 applied in the stage-1 content build; stage 2 rebuilt unchanged against the new intermediate (§3a). ChatGPT PR #112 review `5704839026`, anchored to `e9b7e2a91aaa6c7a05233b0e114f69eb3adb1b1c` (29 October 2026) | ACCEPT SCOPED; all three findings CLOSED; no further co-owner correction requested in that round; Atlas receipt now recorded in §3b; PI adoption pending |
| Atlas row check and build replay | `records/ofn/ATLAS_ROW_CHECK_OFN_v0_11.md`, PR #115 head `8621e565f4454073d0a832af392895da5752ebc5`, reviewing PR #112 head `ba61f5195a21e31d9c7fe5b047d55c400f95683a` | ACCEPT FOR ADOPTION (Atlas side); independently replayed by Atlas; record and evidence merged in #115; received by ChatGPT without claiming another replay (§3b) |
| Adoption | PI, in the OFN session, 30 October 2026, 00:22 +03:00: "ontology DSN'i bu şekliyle benimsiyorum" — on candidate `df3c465f…00eb` as presented with the co-owner and Atlas acceptances | **adopted** (§8) |
| Publication finalization | `evidence/ofn/scripts/release_ofn_v0_11.py`, adoption-state lines only; gates P1–P6 PASS, controls X1–X5 caught | done; published SHA-256 `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4` |
| Publication merge of PR #112; tag `ofn-v0.11` | PI (merge commit; annotated tag with the published hash in the message) | pending |

**Prerequisite merge receipt — 30 October 2026.** On the PI's current request, ChatGPT executed the following server-side merge commits in the stated order, with each PR head pinned by the merge request. No squash, rebase, force-push or branch deletion was used. These are record/intake merges, not adoption of v0.11.

| PR | Pinned head | Merge commit on `main` |
|---|---|---|
| #108 | `e11aa3a3e45f92ef9b0589c55a932ca17eb830fa` | `2861b16b92e0d79c44e6b254036126d79895ab26` |
| #109 | `14bf27be7809d8203c56bbbb3c28b2696b7572f5` | `d2fecb79d9a34f84dc75e4fe4a65b7903e990307` |
| #110 | `6a0b89826ee53114b28585ea1cefda0bde915576` | `c82c606c0642fc2a1407e4e6276582036cc548a2` |
| #111 | `71f708916bebba012a3ab45509ffe22b9fd8ce48` | `e1e88514daef4b4ddfb86bc2f0d2a7d0f978d42e` |
| #116 | `c6fd5743dea3e5e2b6162d1242d03cad2bba1078` | `d906cd217e71e89ea8bfa74f6d6569b2030849bc` |
| #115 (Atlas review/evidence) | `8621e565f4454073d0a832af392895da5752ebc5` | `520abadab996981ca2e2edf56c48efdf194fdba1` |

The Atlas §4.1 publication condition is therefore met: the disposition, reconciliation, finding and intake records are on `main` before PR #112. The review evidence is on `main` as well. PR #112 remains unmerged and unadopted; the separate tool PR #113 is not merged or required by this release.

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
| **Stage-2 candidate (accepted and adopted object)** | output of the stage-2 builder (was `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` at `8ec6338`) | `df3c465fb79f049f686f07635d889613e8ab112895cdbcd5af7af029e97400eb` |
| **Published v0.11 (adopted; final)** | `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` | `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4` |
| Publication transform and checker | `evidence/ofn/scripts/release_ofn_v0_11.py` | `8300fa2d9499a9fc7886abc9fa0bbfdd1d6b113144686dde36a6d20fdd402cd8` |
| Publication check output (P1–P6, X1–X5) | `evidence/ofn/v0.11/release_check_output.txt` | `625778e9bf4d96c9c939c1f3c3dbf30c2de23164e746898520873edb3f28bb9b` |
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

**Receiving delta review — ChatGPT, 29 October 2026:** **ACCEPT SCOPED; R112-C1, R112-C2 and R112-N1 CLOSED.** PR #112 review `5704839026` is anchored to `e9b7e2a91aaa6c7a05233b0e114f69eb3adb1b1c`, compared with the preceding reviewed head `5a7ed0892d0ff5b77dbba2f4572f0d0ec976966a`. The reviewer read all four candidate replacement hunks, the corresponding builder/checker delta and this release record. GitHub's comparison reports four replaced lines in each of the stage-1 intermediate and stage-2 candidate. The original review file remains the round-1 snapshot; this receipt closes its findings without rewriting that history. The scientific/contract acceptance is retained; no further correction is requested by this co-owner in this round.

**Verification boundary for this receipt:** `EV-SRC-READ` / `EV-CODE`, not a complete build replay. The PR, this record and the movement-map header were checked to agree on stage 1 `9f31badfa0e7a70a037c3ede3e7f55f852d09f2288508ef38edf343a5172a822` and candidate `df3c465fb79f049f686f07635d889613e8ab112895cdbcd5af7af029e97400eb`; these are builder-computed SHA-256 values, not independently rehashed by the receiving reviewer in this round. C15–C17 and their K7/K8 coverage were inspected. The full builders, gates and fixtures were not rerun by this reviewer; their PASS counts above remain builder-reported. Atlas's separate row check and build/hash replay remain pending.

This receipt changes neither the candidate nor the movement map, and does not add `history_appendix: "C"` in anticipation of PR #113. It makes no adoption, merge, tag or inbox-state change. The prerequisite-record merges, custody intake and PI adoption remain separate gates.

## 3b. Atlas receipt and bounded dispositions — 30 October 2026

**Received:** `records/ofn/ATLAS_ROW_CHECK_OFN_v0_11.md` and `records/ofn/OFN_UPLOAD_HASH_CHECK_20261030.md`, read in full by ChatGPT at PR #115 head `8621e565f4454073d0a832af392895da5752ebc5`, then merged as recorded in §1. Atlas's verdict is **ACCEPT FOR ADOPTION** for exactly `df3c465fb79f049f686f07635d889613e8ab112895cdbcd5af7af029e97400eb`. This receipt supersedes the pending-Atlas state of the dated §3a receipt; it does not rewrite that earlier review.

**Evidence attribution:** Atlas independently rebuilt both stages and their logs/map byte-identically, reran K1–K9/C1–C17 and G0–G10/F1–F14, checked the shared tool, and recomputed the 13 artifact hashes in §2. The execution records are under `evidence/atlas/rowcheck/ofn_v0_11/`. ChatGPT receives those inspected records as Atlas execution, not as a second execution by ChatGPT. No historical owner campaign is reopened. The upload audit also preserves its exact limit: Draft 1 → Draft 2 → v0.10 output bytes were reproduced, but the v0.10 release script's later predecessor-file post-check stopped because v0.9 bytes were unavailable; the v0.9 → Draft 1 leg was not replayed.

**Disposition of Atlas §4.2–4.5:**

1. **RID retention, OFN11-C02:** `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT` retains its identity because the amendment revises the admitted-regularity field of the same versioned genuine-triad model-selection contract, preserving its referent, Q1–Q6 and custody; it is explicitly recorded as a contract amendment, not as equivalence of the old analytic and new smooth test domains or as a new theorem. The old field remains recoverable at `ofn-v0.10`. Consumers must assess the versioned amendment rather than infer unchanged scope from the retained RID (Methodology v1.4 §4.4). Both OFN11-C01 and OFN11-C02 are named in the planned Genesis, RRF and FMS/ER-2B notices in §6.
2. **Retained live-file exception:** IMP-O10-05's phrase "not re-verified line by line for this draft" is deliberately retained as the evidence-access qualification for this reviewed candidate; it is not a claim of a new proof replay or a remaining scientific gate. No extra canonical-text edit is inserted into the status-only finalization. A later source-maintenance pass may update that wording together with its actual verification scope.
3. **Optional tool profile:** do not add `history_appendix: "C"` for this release. The committed map, shared-tool baseline and owner guards remain the accepted check package. Atlas's passing PR #113 run is not approval of that tool: the independent receiving review in PR #114 requests two fixes to PR #113 (`CCP113-R1`, history boundaries; `CCP113-R2`, hash-relocation regression). PR #113 remains separate and unmerged; neither this tool review nor the optional profile changes the OFN candidate.
4. **Adoption object and finalization:** keep candidate `df3c465f…00eb`; only the §8 adoption-state lines may change after a distinct PI adoption decision. At publication, BASELINE must name the final published SHA-256, `ofn-v0.11` and this release record. These operations have not been performed by this receipt.

**Co-owner disposition:** retain ACCEPT SCOPED / adoption-ready for the reviewed candidate. No further scientific correction or build round is requested. The record-only dispositions above do not adopt the candidate, alter its contract decisions, send the future notices, close inbox items or authorize a publication tag.

## 4. Custody (row 24)

| Artifact | SHA-256 | State |
|---|---|---|
| v0.10 release record (with N-O10-1–4) | `10a1ec6b…0844` | unchanged intake merged in PR #116 under `upload/ofn-records/` |
| `build_ofn_v0_10_draft1.py`, `build_ofn_v0_10_draft2.py`, `release_ofn_v0_10.py` | `6a4fe7af…58ff`, `930b0aef…5c82`, `2aca119f…4f5f` | unchanged intake merged in PR #116 |
| Draft 1, Draft 2 | `d94e1e39…8c36`, `58e2dec5…3610` | unchanged intake merged in PR #116 |
| SESSION scripts: `iso_check.py`, `iso_quadratic_nogo.py`, `transported_pq.py`, `transported_sim.py`, `basin_test.py`, `OFN_PSI_KAPPA_EXTENSION_v0_1.py`, `OFN_PSI_KAPPA_ALL_MINOR_CHECK_v0_1.py`, `OFN_PSI_INVARIANT_C_CHECK_v0_1.py`, `OFN_PSI_INVARIANT_C_GAUGE_CHECK_v0_1.py`, `OFN_PSI_REFLECTION_AUDIT_v0_1.py`, `OFN_STAB_F3_CHECK_v0_1.py` (11 of 12), plus `k3_six_step_factor_check.py` | as listed in `SHA256SUMS.txt`, equal to the prefixes printed in OFN | unchanged intake merged in PR #116 |
| v0.8 input reviews `OFN_SOURCE_REVIEW_ER2B_GEN288_OPEN3_v0_1_1.md`, `…_ADDENDUM_…_v0_1.md` | `8d18640f…0944`, `f86cd483…c5b8` | unchanged intake merged in PR #116 |
| `RTG_ONTOLOGICAL_FOUNDATIONS_v0_8_RELEASE_RECORD.md` | `0015347c…0848` | held by the ChatGPT session; not uploaded |
| `transported_chiral_pq.py` (`09129ffc…73ac`) | — | **missing** (neither OFN session holds it) |
| FMS ψ scripts (`ad44f66a…`, `5af23da9…`); ER-2B v0.3.1 (`711e427a…81b4`, reported) | — | missing from both OFN sessions; to be asked of FMS and the PI |
| `REVIEW_FINDINGS.md`, `OFN_TDRG_FINDING_A_HANDOFF.md`, `OFN_v0_9_PROGRAMME_AND_OWNER_SYNC_REQUEST.md`, v0.9 release record and validation files | — | missing from both OFN sessions |
| RECOG v0.3.20 freeze record | `5c00f66d…9b55` | placed (`records/recog/`) |

No historical record is reconstructed. The unchanged v0.10 release record is now available on `main` at `upload/ofn-records/RTG_ONTOLOGICAL_FOUNDATIONS_v0_10_RELEASE_RECORD.md`; this is intake placement, not a silent move to `records/ofn/`. BASELINE's authority row can cite it, or this v0.11 release record after the successor is adopted and tagged. Unrecovered items retain the earlier custody limitations.

## 5. Inbox `pipes/OFN/`

| Item | Disposition | State |
|---|---|---|
| `20261026-NUMGEN-v1-21-adopted.md` | `2026-10-29 · accept · records/ofn/OFN_OWNER_DISPOSITION_RECONCILIATION_v0_10.md` (rows 12, 13) | dispositioned (PR #110 merged); closed after the tag |
| `20261028-TDRG-v2-12-14-adopted.md` | the same (rows 7–11) | dispositioned; closed after the tag |
| `20261029-RECOG-v0-3-26-adopted.md` | the same (rows 14, 15, 23) | dispositioned; closed after the tag |

Filed by OFN: `pipes/TDRG/20261029-OFN-token-sum-gauge-label.md` (`kind: finding`; PR #111 merged). Filing is not TDR-G acceptance.

## 6. Affected consumers (what would be notified after the tag)

| Consumer | Notice content |
|---|---|
| DYAD | Receipts of N4, N6 and N14. Adopted use of `DYAD-THM-SMOOTH-EMBEDDING`, `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` and `DYAD-DEF-PRIMITIVE-MAP` (IMP-O10-06/07, IMP-O08-12) |
| GEN | G-20 existence note received; C2 used through the DYAD chart; imports repinned to `gen-v2.9`. Explicitly notify OFN11-C01 (`RTG-OFN-DEF-STANDARD-C` quantifier correction) and OFN11-C02 (`RTG-OFN-DEF-TRIAD-MODEL-CONTRACT` regularity amendment), since IF32 consumes §5.5; no silent consumer adoption |
| RRF | §6.2a received. Upon OFN v0.11 adoption, "OFN has not separately adopted" needs synchronization at §5.5.4 scope; the readout entry is accepted as the representation-level readout contract. Explicitly notify OFN11-C01 and OFN11-C02 and the retained, version-qualified contract RIDs; RRF decides its own consumer update |
| TDR-G | Finding A receipt state recorded. Owner RIDs used. REQ-O09-05 endpoint component closed. The label finding is filed separately (PR #111) |
| NUMGEN | REQ-O09-03 closed; consumer rows moved to v1.21 |
| RECOG | REQ-O09-02 closed through the freeze record; imports at `recog-v0.3.26`; A1c witnesses recorded by claim |
| FMS / ER-2B | Class C now has a real $C^\infty$ mathematical realization; analytic realization and physical selection stay open. Standard C is corrected by OFN11-C01 and the test class widened by OFN11-C02; their co-owners update their own wording (row 27) |
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

These limits are tracked by tool PR #113. Its separate receiving review (PR #114, `records/atlas/TOOL_CHECK_COMPACTION_PR113_RECEIVING_REVIEW_CHATGPT.md`, reviewed head `740496b9d6d1f605ad9f8e125c41efd598338d3b`) requests two required fixes; a PASS on this genuine OFN candidate does not resolve those synthetic negative-control failures. No tool change or optional profile-key addition is made here (§3b).

**Size (`dsn_lint`, informational):**
- 192,142 bytes and 1,581 lines.
- Against stage 1: −21,785 bytes (−10.2 %).
- Against `ofn-v0.10`: −3,318 bytes (−1.7 %).

No claim, RID, grade, status or OPEN changes in stage 2.

**Reproduce stage 2.** Run from the repository root:
1. `python3 -I evidence/ofn/scripts/build_ofn_v0_11_stage2.py evidence/ofn/v0.11/stage1_intermediate.md OUT.md MAP.json` writes `df3c465f…00eb` and the map.
2. `python3 -I tools/check_compaction.py evidence/ofn/v0.11/stage1_intermediate.md OUT.md evidence/ofn/v0.11/movement_map.json`
3. `python3 -I evidence/ofn/scripts/check_ofn_v0_11_stage2.py evidence/ofn/v0.11/stage1_intermediate.md OUT.md evidence/ofn/v0.11/movement_map.json --fixtures`

## 8. Adoption

**Decision.** Mustafa (PI), in the OFN session, 30 October 2026, 00:22 +03:00: "ontology DSN'i bu şekliyle benimsiyorum" ("I adopt the ontology DSN in this form").

The decision was given after the PI had received:
- the co-owner disposition "accept / adoption-ready";
- the Atlas verdict ACCEPT FOR ADOPTION;
- the prerequisite merges (§1).

All three name the candidate `df3c465fb79f049f686f07635d889613e8ab112895cdbcd5af7af029e97400eb`. The adopted object is that candidate, together with its row dispositions (§3), round-2 corrections (§3a) and dispositions (§3b).

**Finalization.** The transform is `python3 -I evidence/ofn/scripts/release_ofn_v0_11.py CANDIDATE OUT "30 October 2026"`. It changes exactly eight lines:
- the header Date, Document status and Supersedes lines ("on adoption" dropped);
- the §0.3 label "*v0.11 (adoption pending):*" → "*v0.11:*";
- the §12.3 six-DEF row → "Registered v0.11 … Registered 30 Oct 2026";
- the Appendix B heading → "Adopted v0.11 records — 30 October 2026";
- the Appendix C v0.11 heading → "ADOPTED";
- the footer.

The header Date line follows the NUMGEN v1.21 publication precedent; the other seven are the lines listed in this section before adoption. The IMP-O10-05 wording exception (§3b) is not touched.

The `--check --controls` run gives:
- P1: candidate hash;
- P2: rebuild identical;
- P3: exactly the 8 declared lines differ;
- P4: the reverse transform recovers the candidate;
- P5: no draft or pending marker remains;
- P6: every other line is byte-identical, and the claim-tag, RID and math census is unchanged.

All six gates pass, and the five controls (an extra live change, a status-summary edit, a draft footer, a changed claim tag, an added RID) are all caught.

**Published file:** `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`, SHA-256 `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4`. The candidate hash `df3c465f…00eb` and the published hash are separate identities.

**BASELINE.** The OFN row names v0.11, the published hash, this record and the tag `ofn-v0.11`, which the PI creates. The previous row is kept as the predecessor (`acb70a8c…5dfa`, `ofn-v0.10`).

**After this record:**
1. The PI merges PR #112 with a merge commit and creates the annotated tag `ofn-v0.11` on that merge commit. The tag message carries `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4`.
2. The co-owners close the three `pipes/OFN/` items (§5).
3. They file the §6 notices as `pipes/` items. The Genesis, RRF and FMS/ER-2B notices name OFN11-C01 and OFN11-C02 (§3b).
4. "Sync now" is run in the Claude project.

This record is frozen at adoption, except for the merge-commit and tag fields in §1, which the PI may fill in.
