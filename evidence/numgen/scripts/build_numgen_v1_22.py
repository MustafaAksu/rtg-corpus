#!/usr/bin/env python3
"""Number Genesis v1.22 — one content stage (receiving and synchronization) on the adopted v1.21.

usage: build_numgen_v1_22.py BASE OUT EDITLOG_JSON
  BASE = `git show numgen-v1.21:dsn/RTG_NUMBER_GENESIS_DSN.md` (asserted SHA-256 4805760d…5701)

Each edit replaces one exact substring that occurs exactly once in the current text (asserted), in the order listed.
The log records key, group, row, old, new and their SHA-256. Scope: the v1.22 receiving ledger
(records/numgen/NUMGEN_v1_22_RECEIVING_LEDGER.md), the S1 record (records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md)
and the owner disposition of the 23 Nov advisory. No grade, OPEN status, claim scope or RID allocation changes; one
`[NUM]` evidence block is added (S1). Round 2 applies the four scoped review repairs (PR #377, review 6041922508); the round-1 candidate is preserved in Git and the log records its hash.
"""
import hashlib, json, sys

BASE_SHA = "4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701"
PRED = BASE_SHA
ROUND1_SHA = "8ccc8e38f0ad054d68f59bf5d95c9364afa093f02cb3e418295625db3763148a"
REL = "`records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md`"
S1 = "`records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md`"
LEDGER = "`records/numgen/NUMGEN_v1_22_RECEIVING_LEDGER.md`"

E = []
def e(key, group, row, old, new): E.append((key, group, row, old, new))

# ---- header (current state only) -------------------------------------------------------------------------------
e("H1", "header", "title", "# RTG_NUMBER_GENESIS_DSN_v1.21\n", "# RTG_NUMBER_GENESIS_DSN_v1.22\n")
e("H2", "header", "Date", "**Date:** 26 October 2026  \n", "**Date:** 24 November 2026  \n")
e("H3", "header", "Document status",
  "**Document status:** ADOPTED — PI, 26 October 2026 (corrections of the reconciled v1.20.8 advisory and Methodology v1.4 compaction; stage 1 and stage 2 reviewed). Release record: `records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md`.  \n",
  f"**Document status:** DRAFT — v1.22 candidate (one content stage: receiving and synchronization), not adopted; v1.21 governs until PI adoption. Release record (DRAFT): {REL}.  \n")
e("H4", "header", "Supersedes",
  "**Supersedes:** `RTG_NUMBER_GENESIS_DSN_v1.20.8` (SHA-256 `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e`; tag `numgen-v1.20.8`).",
  f"**Supersedes:** `RTG_NUMBER_GENESIS_DSN_v1.21` (SHA-256 `{PRED}`; tag `numgen-v1.21`).")
e("H5", "header", "Release record",
  "**Release record:** `records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md`. Version history: Appendix A.",
  f"**Release record:** {REL} (DRAFT). Version history: Appendix A.")

# ---- §1.1 TDR-G imports: producer RIDs (P01) -----------------------------------------------------------------------
e("I1", "P01 RIDs", "§1.1 TDR-G state space",
  "`[DEF]` `[import: RTG_DISCRETE_GENESIS_DSN_v2.12.13 §6.1 | RID unavailable]` **Finite phase support — state space.**",
  "`[DEF]` `[import: RTG_DISCRETE_GENESIS_DSN_v2.13 §6.1 | TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE]` **Finite phase support — state space.**")
e("I2", "P01 RIDs", "§1.1 TDR-G recurrence",
  "`[THM]` `[import: RTG_DISCRETE_GENESIS_DSN_v2.12.13 §6.2 | RID unavailable]`",
  "`[THM]` `[import: RTG_DISCRETE_GENESIS_DSN_v2.13 §6.2 | TDRG-THM-RECURRENCE]`")
e("I3", "P01 RIDs", "§1.1 firewall",
  "RTG_PROGRAMME_OVERVIEW_v1.3 SG-PROG-1 | RID unavailable]` **Cross-branch firewall.**",
  "RTG_PROGRAMME_OVERVIEW_v1.3 SG-PROG-1 | guard citations, no RID; SG-10 and SG-PROG-1 unchanged at tdrg-v2.13 and programme-v1.4]` **Cross-branch firewall.**")

# ---- §2 item 1: C7C-M4 hold reason (F1) ----------------------------------------------------------------------------
e("Q1", "F1 hold", "§2 item 1 v1.20 sentence",
  "M-4 realization search HOLD pending the Discrete-owner P2 policy.",
  "M-4 realization search HOLD (reason below).")
e("Q2", "F1 hold", "§2 item 1 campaign hold",
  "**Campaign hold:** design/algebra may proceed, but the first C7C-M realization search (M-4) is not opened until the Discrete-Genesis owner resolves the P2 antipodal-endpoint presentation-covariance policy used by the current SWAP/P3 implementation. **TDR-G dependency:** the request for TDR-G's orientation-policy disposition at `S=0`, `|E|=N/2` is filed as `pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md` (`blocks: C7C-M4`); before any status change, the 40 convention-exposed DISC-2 witnesses (§6.6 P2 audit) receive a sensitivity audit under the policy TDR-G adopts. The abstract WD-DOM design continues meanwhile.",
  "**Campaign hold:** design/algebra may proceed; the first C7C-M realization search (M-4) stays on HOLD. The P2 policy question is answered: TDR-G adopted `TDRG-DEF-ORIENT` (`tdrg-v2.12.14`, unchanged at `tdrg-v2.13` §6.3: at `S=0`, `2E≡0 mod N` the path is a balanced tie), and the consumer re-annotation of the Census-1 witness universe under it is recorded (§6.6 P2 block; `records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md`). The research target remains a certified non-degenerate composable three-stream witness: all 158 Census-1 TDR-G records (including the 40 quarantined ones) carry the stream pair `(SWAP, P3)`, so this TDR-G sub-universe contributes no candidate chain at either interface level (§6.6, Census-1 result). The P2 rule change alone does not remove that schema obstruction; the two continuous-dyad records are separate. M-4 stays HOLD pending approval of a design and preregistration capable of addressing the missing chain, with typed middle-interface witnesses, outer-pair admissibility and WD-DOM stated before outcome-sensitive computation. Finding the witness is the research objective, not a prerequisite to searching for it. A new evidence universe requires its own preregistration (Census-2). The abstract WD-DOM design continues; this release authorizes no campaign.")

# ---- §6.2 q* disambiguation (P03, F3) ------------------------------------------------------------------------------
e("Z1", "F3 q-star", "§6.2 N-1C witness",
  "This is **uniqueness at the stated scan resolution**, not a global uniqueness theorem. Exact existence/location remains `[NUM]` until the accepted interval/Arb certificate is run.",
  "This is **uniqueness at the stated scan resolution**, not a global uniqueness theorem. Exact existence/location remains `[NUM]` until the accepted interval/Arb certificate is run. `q_*` is not Dyadic's branch-split value `q_{3/4} ≈ 1.2602142`, a zero of `rho_4` with `eta_6(q_{3/4})-q_{3/4} ≈ -0.5537` (`DYAD-THM-OPEN18-STEP-MONOTONE`, `dyad-v6.4.24` §6.8): different objects.")

# ---- §6.6 P2 audit lines (F1/F2, S1) -------------------------------------------------------------------------------
e("P1", "F1/F2 P2", "§6.6 DISC-2 summary line",
  "Discrete-owner policy action is pending; DISC-1 requires the same audit.",
  "Discrete-owner policy: `TDRG-DEF-ORIENT` (`tdrg-v2.13` §6.3); under it 20/136 records change verdict or class and the ten labels are unchanged; DISC-1: 0/22 exposed (§6.6 P2 re-annotation).")
e("P2", "F1/F2 P2", "§6.6 DISC-1 evidence",
  "label projection `{2:1, 3:1}` unchanged under the tested reverse and inert alternative policies.",
  "label projection `{2:1, 3:1}` unchanged under the tested reverse and inert alternative policies. Execution artifact and the result under `TDRG-DEF-ORIENT` (0/22 exposed, 0/22 changed): §6.6 P2 re-annotation (" + S1 + ").")
e("P3", "F1/F2 P2", "§6.6 DISC-2 evidence",
  "every admitted label with at least one unexposed witness; label set unchanged under the tested reverse and inert alternative policies.",
  "every admitted label with at least one unexposed witness; label set unchanged under the tested reverse and inert alternative policies and under `TDRG-DEF-ORIENT` (§6.6 P2 re-annotation).")
e("P4", "F1/F2 P2", "§6.6 P2 guard + S1 block",
  "A Discrete-Genesis owner ruling on the antipodal endpoint policy (or a presentation-independent path-selection theorem) is required before future campaigns. DISC-1 requires the same audit separately.",
  "The Discrete-Genesis owner ruling is `TDRG-DEF-ORIENT` (`tdrg-v2.13` §6.3); future campaigns use it or a presentation-independent path-selection theorem. The re-annotation below changes no frozen record and no Census-1 decision.\n\n`[NUM]` `[scope: Census-1 TDR-G witness universe, DISC-1 22 + DISC-2 136; N=24, three nodes, k in {0,1,2,3}, bound_symmetric]` `[conv: pinned v18 engine with orient_path replaced by the TDR-G reference implementation of TDRG-DEF-ORIENT]` **P2 re-annotation under TDRG-DEF-ORIENT (v1.22 S1).** Positive control 158/158: unmodified v18 matches the frozen DISC-1 transport tuples (k=0..3, PASS_INT) and DISC-2 verdicts/base classes, both in tick-by-tick lockstep with their own frozen enumerators. DISC-2: 40 exposed; 20 change verdict or class — 8 change class with PASS kept (1:1→4:3 ×4, 1:1→3:2 ×4), 6 lose PASS with the base dual kept, 6 lose the base dual (5:2→NO_BASE_DUAL); 124/136 remain PASS; the ten admitted labels are unchanged. DISC-1: 0/22 exposed, 0/22 changed; `{2:1, 3:1}` unchanged. DISC-2 comparison: 136/136 verdicts/classes and v18 exposure indicators agree with the held v1.19 audit's `inert` comparison. The DISC-1 result is from S1's direct execution, not from that audit. Evidence: `records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md`; `evidence/numgen/v1.22/s1/` (annotation `1819015a…3524`). Not a certificate replacement; Census-1 F6 decisions and its verdict are unchanged; no record is admitted retroactively.")
e("P5", "F1 hold", "§6.6 M-4 HOLD",
  "`[HOLD]` **M-4 realization search** — pending the Discrete-owner P2 antipodal-endpoint policy ruling.",
  "`[HOLD]` **M-4 realization search** — the P2 policy is answered (`TDRG-DEF-ORIENT`; §6.6 P2 re-annotation); the hold awaits an approved design/preregistration addressing the missing composable-chain evidence object (§2 item 1).")

# ---- §8 DZT provenance (P10, P11, F5) ------------------------------------------------------------------------------
e("D1", "F5 DZT", "§8 PROVENANCE",
  "No DZT document of that number is in the repository; the governing DZT edition is `dzt-v0.8` (`RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md`).",
  "Two files labelled v0.17 are in the repository as received history without adoption record or tag (`upload/dzt-recovery-20261116/received/originals/downloads/`; DZT notice of 19 Nov 2026); they are not part of the DZT lineage. The governing DZT edition is `dzt-v0.19` (`RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md`). The audit-reported odd-support and denominator statements are covered there by `DZT-THM-CASCADE-NORM-LAW` (§6.3, a theorem assuming `DYAD-THM-Q403-PHASELAW`, for `p=4s≥12`, absolute real-subfield norm, sign outside the theorem), cited here as a locator only.")

# ---- §9.1 import ledger, received items, consumers and pins (P01–P11) ---------------------------------------------
e("L1", "P06 pins", "§9.1 Programme import row",
  "read at `programme-v1.3` (SG-PROG-1–4 restated there as clarifications; this use unchanged); no status promotion |",
  "read at `programme-v1.3` (SG-PROG-1–4 restated there as clarifications; this use unchanged); SG-PROG-1–4 byte-identical at `programme-v1.4`; no status promotion |")
e("L2", "P01 RIDs", "§9.1 TDR-G import row",
  "| TDR-G `Z_N`, finite recurrence, cross-branch firewall | `RTG_DISCRETE_GENESIS_DSN_v2.12.13 §6.1–§6.2`, SG-10 |",
  "| TDR-G `Z_N`, finite recurrence, cross-branch firewall | `RTG_DISCRETE_GENESIS_DSN_v2.13 §6.1–§6.2` (TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE, TDRG-THM-RECURRENCE; statements identical to v2.12.13), SG-10 (retained pin `tdrg-v2.12.13`, unchanged at v2.13) |")
e("L3", "receiving", "§9.1 dispositions heading",
  "**Notice and request dispositions (v1.20.8).** Owner-side records only; no import follows from a receipt.",
  "**Notice and request dispositions.** Owner-side records only; no import follows from a receipt.")
e("L4", "receiving", "§9.1 dispositions rows (v1.22)",
  "| statement accepted as independent agreement (acceptance matrix below); not imported; custody of GAP-LOCK 1–3 and INF-1 unchanged |\n",
  "| statement accepted as independent agreement (acceptance matrix below); not imported; custody of GAP-LOCK 1–3 and INF-1 unchanged |\n| TDRG-DEF-ORIENT and eight producer RIDs; star / multistar domain | TDR-G (v2.12.14, v2.12.15) | accept with change: §1.1 cites three matched producer RIDs at `tdrg-v2.13`; the others are available, not newly consumed. The reference orientation is used for consumer re-annotation (§6.6). No affected NUMGEN claim relies on the earlier K1,3-only restriction: RF-06 uses fixed-centre token inversion; the DISC panels are birth-free |\n| `q_{3/4}` answer; N15 receipt; v6.4.24 unchanged imports | Dyadic (v6.4.23, v6.4.24) | accept: §6.2 disambiguation; NC-17 closed; no import changed |\n| REQ-O09-03 fulfilled; N-1A2 vocabulary use | OFN (v0.11, v0.12) | accept: consumer rows below; N-1A2 vocabulary only (no import of its closure); the L-BACKBONE and NG-7A reference scopes remain separate |\n| interface rows IF12–IF14, IF24, IF27, IF37, IF38 | Programme (v1.4) | accept: checked against this ledger; pin used stays v1.3 (guards unchanged) |\n| A1c explicit-`U` rows; GAP-LOCK Lemma 3 two-grade use | RECOG (v0.3.26, v0.3.27) | accept with change: consumer row below; A1c compared only, not imported |\n| v0.17 files and `DZT-THM-CASCADE-NORM-LAW` | DZT (v0.18, v0.19) | accept: §8 provenance; nothing imported |\n")
e("C1", "P08 pins", "§9.1 consumers Dyadic map row",
  "| v6.4.18 (statements unchanged at v6.4.22) | `dyad-v6.4.22` | IF12 |",
  "| v6.4.18 (statements unchanged at v6.4.24) | `dyad-v6.4.24` | IF12 |")
e("C2", "P08 pins", "§9.1 consumers Dyadic row A",
  "| v6.4.22 (producer v6.4.19) | `dyad-v6.4.22` | IF12 |",
  "| v6.4.22 (producer v6.4.19; unchanged at v6.4.24) | `dyad-v6.4.24` | IF12 |")
e("C3", "P01 RIDs", "§9.1 consumers TDR-G row",
  "| import | TDR-G | `Z_N`, finite recurrence, SG-10 firewall, DISC harness input | v2.12.13 | `tdrg-v2.12.13` | IF13 |",
  "| import | TDR-G | `Z_N` (TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE), finite recurrence (TDRG-THM-RECURRENCE), SG-10 firewall | v2.13 (state/recurrence); v2.12.13 (retained SG-10 firewall pin) | `tdrg-v2.13` | IF13 |\n| evidence input | TDR-G | DISC harness input (frozen v18 conventions); TDRG-DEF-ORIENT for the bounded consumer re-annotation only (§6.6), not a new general theorem import | v2.12.13 (frozen evidence); v2.13 §6.3 | `tdrg-v2.13` | IF13 |")
e("C4", "P05 pins", "§9.1 consumers OFN import row",
  "| import | OFN | §1.1 definitions, holonomy-rank diagnostic | v0.10 | `ofn-v0.10` | — |",
  "| import | OFN | §1.1 definitions, holonomy-rank diagnostic | v0.10 | `ofn-v0.12` | — |")
e("C5", "P06 pins", "§9.1 consumers Programme row",
  "| import | Programme | SG-PROG-1, SG-PROG-2 (`RTG-OPEN-GENERATOR-SELECTION`) | v1.3 | `programme-v1.3` | — |",
  "| import | Programme | SG-PROG-1, SG-PROG-2 (`RTG-OPEN-GENERATOR-SELECTION`) | v1.3 (byte-identical at v1.4) | `programme-v1.4` | — |")
e("C6", "P06 pins", "§9.1 consumers Genesis import row",
  "| import | Genesis | §6.6 GEN-ART-SATURATION (NG-10 only) | v2.9 | `gen-v2.9` | — |",
  "| import | Genesis | §6.6 GEN-ART-SATURATION (NG-10 only) | v2.9 | `gen-v2.10` | IF37 |")
e("C7", "P07 consumers", "§9.1 consumers RECOG export row",
  "GAP-LOCK Lemma 3 as cited in RECOG §7 | v1.20.8 (RECOG keeps v1.15 producer pins where load-bearing) | `recog-v0.3.24` | IF14 |",
  "NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO at two grades (exact identity at ALG inside RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE, RECOG §6.16e; locking statement as HEUR cross-reference) | v1.21 (RECOG keeps v1.15 producer pins where load-bearing) | `recog-v0.3.27` | IF14 |")
e("C8", "P07 consumers", "§9.1 consumers RECOG received row",
  "| received | RECOG | A1a/A1b explicit-domain theorems: consumer-side confirmations (acceptance matrix above) | v0.3.24 | `recog-v0.3.24` | IF27 |",
  "| received | RECOG | A1a/A1b explicit-domain theorems: consumer-side confirmations (acceptance matrix above); A1c rows of v0.3.27 compared only, not imported | v0.3.24 (matrix baseline) | `recog-v0.3.27` | IF27 |")
e("C9", "P04/P05 consumers", "§9.1 consumers OFN export row",
  "| export | OFN | NG-7A additive operator and representation results (OFN §11 inspected NUMGEN v1.20.7 §6.8) | as declared in OFN §11 | `ofn-v0.10` | IF24 |",
  "| export | OFN | NG-7A additive operator and representation results (reference-only feedback); `NUMGEN-RESULT-N5AS1-L-BACKBONE` (REQ-O09-03); N-1A2 definitions as vocabulary only (OFN §5.5.4; closure not imported) | v1.21 (OFN §1.1, §6.8, §9.1, §12.3–§12.4) | `ofn-v0.12` | IF24 |\n"
  "| export | Genesis | `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE` (§6.4): independent route to `G_2(Z)=0`; `GEN-ART-G2-CHRONO` stays custody-A at Genesis | v1.21 (Genesis §6.4, §7) | `gen-v2.10` | IF38 |")

# ---- carried forward from v1.21 release record §14 (atlas note on E42) ----------------------------------------------
e("X1", "hash form", "RECOG v0.3.24 hash abbreviation", "`8c64bea2…69e7c1`", "`8c64bea2…e7c1`")

# ---- §9.2 artifact registry ----------------------------------------------------------------------------------------
e("R1", "S1 evidence", "§9.2 NG_C7C_M_DESIGN row",
  "physical carrier closure/global WD-DOM not yet certified; M-4 search held pending P2 policy |",
  "physical carrier closure/global WD-DOM not yet certified; M-4 search held (§2 item 1) |")
e("R2", "S1 evidence", "§9.2 S1 artifact row",
  "| `disc2_p2_antipodal_exposure_audit_v1.py` + `.log` |",
  "| `records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md` + `evidence/numgen/v1.22/s1/` (script `4c5c2f17…8ae9`, annotation `1819015a…3524`) | P2 re-annotation of the 158 Census-1 TDR-G witnesses under TDRG-DEF-ORIENT; the frozen-record positive control; DISC-1 execution artifact | `[NUM]` — not a certificate replacement |\n"
  "| `disc2_p2_antipodal_exposure_audit_v1.py` + `.log` |")

# ---- Appendix A, footer --------------------------------------------------------------------------------------------
e("A1", "history", "Appendix A v1.22 entry",
  "### v1.21 — 26 October 2026 — Adopted\n",
  "### v1.22 — 24 November 2026 — DRAFT (not adopted)\n\n- **Basis:** Atlas sync advisory of 23 Nov 2026 (rev. 2, `records/numgen/ATLAS_ADVISORY_NUMGEN_SYNC_20261123.md`); owner disposition (`records/numgen/NUMGEN_OWNER_DISPOSITION_SYNC_20261123_CLAUDE_20261124.md`); co-owner GO for S1 and for S2–S3 (24 Nov 2026).\n- **Evidence [NUM] (S1):** P2 re-annotation of the 158 Census-1 TDR-G witnesses under TDRG-DEF-ORIENT (§6.6; `records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md`); DISC-1 0/22 now has an execution artifact.\n- **Receiving (S2):** eleven inbox notices dispositioned (`records/numgen/NUMGEN_v1_22_RECEIVING_LEDGER.md`); no new import.\n- **Synchronization (S3):** §1.1 TDR-G imports cite TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE and TDRG-THM-RECURRENCE at `tdrg-v2.13`; §2 item 1 and §6.6: C7C-M4 hold reason (P2 answered; approved design/preregistration for the missing composable chain still needed); §6.2 `q_*` vs Dyadic `q_{3/4}`; §8 DZT provenance (`dzt-v0.19`); §9.1 consumers and pins (Dyadic v6.4.24, TDR-G v2.13, OFN v0.12, Programme v1.4, Genesis v2.10 with the IF38 export, RECOG v0.3.27 two-grade GAP-LOCK 3 use); §9.2 S1 artifact row.\n- **Unchanged:** every claim grade and OPEN status; Census-1 INCONCLUSIVE / INCONCLUSIVE; C7C-M4 HOLD; DISC-3 deferred; the C7C algebra; the φ* comparison.\n- **Records:** release record `records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md` (DRAFT); predecessor tag `numgen-v1.21` (`4805760d…5701`).\n\n### v1.21 — 26 October 2026 — Adopted\n")
e("F1", "history", "footer",
  "*END OF DOCUMENT — RTG_NUMBER_GENESIS_DSN_v1.21 (ADOPTED, 26 October 2026).*",
  "*END OF DOCUMENT — RTG_NUMBER_GENESIS_DSN_v1.22 (DRAFT; not adopted).*")

# ---- Round 2: review 6041922508 (R1–R4); round-1 candidate retained in Git ----
e("RV1A", "review R1", "§6.6 C7C-M summary",
  "C7C-A not opened; M-4 HOLD (P2).",
  "C7C-A not opened; M-4 HOLD (approved design/preregistration for the missing composable chain pending; P2 answered).")
e("RV1B", "review R1", "§8 research queue",
  "full-interface typed WD-DOM OPEN; M-4 HOLD (P2). Then `C7C-A` only if the composition carrier survives.",
  "full-interface typed WD-DOM OPEN; M-4 HOLD (approved design/preregistration for the missing composable chain pending; P2 answered). Then `C7C-A` only if the composition carrier survives.")
e("RV4A", "review R4", "§9.1 TDR-G evidence availability",
  "verified against live source; per-cycle `N=24,k=1` enumerator/export still pending in accessible corpus |",
  "verified against the owner statements; NUMGEN's held enumerators and S1 inputs are accessible (`upload/numgen-records/`, `evidence/numgen/v1.22/s1/`). The original owner-side BIND3-CYCLE-N24K1 enumeration/export (`TDRG-ART-BIND3-N24K1`, `tdrg-v2.13` §8) is still owner-reported missing (EV-SRC-REPORTED); the available NUMGEN reproductions are not that original artifact. |")
e("RV4B", "review R1/R4", "§9.2 governance row",
  "`[GOVERNANCE]` — v2 pending; **v3 owner-policy update required before future SWAP/P3 campaigns** |",
  "`[GOVERNANCE]` — historical reproduction-gap note; P2 producer policy answered and S1 witness-panel re-annotation recorded. Original owner enumeration remains missing as reported at `tdrg-v2.13` §8; any future SWAP/P3 campaign needs its own approved design and current-policy reproduction scope. |")

def sha(s): return hashlib.sha256(s.encode("utf-8") if isinstance(s, str) else s).hexdigest()

def build(base):
    s, log = base, []
    for key, group, row, old, new in E:
        n = s.count(old)
        assert n == 1, f"{key}: old text occurs {n} times"
        s = s.replace(old, new)
        assert s.count(new) == 1, f"{key}: new text not unique after the edit"
        log.append({"key": key, "group": group, "row": row, "old": old, "new": new,
                    "old_sha256": sha(old), "new_sha256": sha(new)})
    return s, log

if __name__ == "__main__":
    base_p, out_p, log_p = sys.argv[1:4]
    raw = open(base_p, "rb").read()
    assert sha(raw) == BASE_SHA, "base is not numgen-v1.21"
    out, log = build(raw.decode("utf-8"))
    open(out_p, "wb").write(out.encode("utf-8"))
    json.dump({"base_sha256": BASE_SHA, "candidate_sha256": sha(out), "round": 2, "round1_candidate_sha256": ROUND1_SHA, "edits": log}, open(log_p, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"{len(log)} edits; candidate {sha(out)}")
