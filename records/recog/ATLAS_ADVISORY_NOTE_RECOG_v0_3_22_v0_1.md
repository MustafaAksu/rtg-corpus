# Atlas Advisory Note — Relational Recognition DSN v0.3.22 — v0.1 (Claude pass)

**To:** the RECOG stream owners and reviewers. **From:** the atlas owner (Claude). **Date:** 23 October 2026.
**Source under review:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22` at tag `recog-v0.3.22`, `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`, 1,581 lines, 329,148 bytes, SHA-256 `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` (= `BASELINE.md`). Read in full for this note. Line numbers below are for that file.
**Atlas basis:** atlas v0.2 (tag `atlas-v0.2` on merge `6c52666`; SHA-256 `9963aead…31c5`), D3 and the cross-stream items that name RECOG.
**Owner editions used for the checks:** DYAD v6.4.22 (`dyad-v6.4.22`), NUMGEN v1.20.8 (`numgen-v1.20.8`), RRF v0.8.4 (`rrf-v0.8.4`), RER v0.2 (`rer-v0.2`), Methodology v1.4 (`methodology-v1.4`); DYAD's prepared notices `records/dyad/DYAD_NOTICES_N16_N21.md` (N19, N21 to RECOG; not yet sent).
**Status:** noncanonical advisory, one of two planned independent passes (the second by ChatGPT); the two are reconciled into one final proposal, as for DYAD. It amends, adopts, regrades or notifies nothing. The RECOG owners decide every row.

## 0. Conventions

- **Tiers.** **A** = resolve in the next owner release. **B** = same release unless a named dependency blocks it. **C** = scientific opportunity; may be deferred with its missing premise or next test.
- **Types.** S scientific · I interface / identifier · Y synchronization · E editorial · F formatting.
- **Keys.** `FA-/FB-/FC-RECOG-nn` are tracking keys only, not proposed RIDs.
- `~` marks a link the atlas derived itself; verify before use.
- Every row was re-checked against the tagged RECOG text and the current owner text; the atlas is only the pointer.

## 1. Requested outcome

1. **One owner release** (the team picks the number), through draft → change-focused review → PI adoption, under Methodology v1.4.
2. **Two stages, as in the DYAD v6.4.21 pilot.** Stage 1 applies the corrections (Tier A/B content rows); stage 2 is the layout-only compaction of FA-RECOG-01, checked by `tools/check_compaction.py` against a movement map. Every removed passage stays recoverable at `recog-v0.3.22`.
3. **Per-row disposition** (accept / reject / defer) with reason, the edited section or RID, and how it was validated; a deferral names its missing premise or next test.
4. **Release record** under `records/recog/` before adoption; notices only after the release hash is fixed, keeping *received*, *statement accepted* and *adopted use* separate.
5. The atlas is refreshed from the adopted successor, not from this note.

## 2. Findings

### 2.1 Tier A

**FA-RECOG-01 | E | Live-file rule and compaction (Methodology v1.4 §1.1, Appendix A rule, §13.6)**
- **Location:** header: 21 stacked status summaries v0.2.1–v0.3.22 (L12–L60), a freeze chronicle of about 25 "*Earlier freeze history*" sentences (L52), a 25-edition Supersedes list (L6); §2 closed OPEN entries that keep their historical specifications — R8 (L159–L166), R9 (L237–L249), R10 (L284–L291, status "DELIVERED and ACCEPTED" where the census says CLOSED), R11 ("Former OPEN R11 text (v0.3.1), retained for the record" with `[OPEN]` sub-items, L268–L280), R7 (closed items under "Active sub-items", L301–L304); §6.16 F1 "CELL-F2 targets" and "Order: F2(b) before F2(c0)" (L907–L913) and the F1 ledger cell "the subject of F2(b)" (L880), all completed later; dated inline history (L644 "(Historical, v0.3–v0.3.2 …)", L656 "(v0.3.3–v0.3.4 recorded this as mixed grade; retired in v0.3.5.)"); §9 "Archive. none yet", "critique round pending" (L1267–L1268); Appendix A, 22 full entries (L1317–L1528).
- **Problem:** these sections must hold current state only; the history is preserved by the tag.
- **Action:** stage 2 compaction: one current status paragraph; closed OPEN entries reduced to question, closure, closing RIDs and residuals (v1.4 §1.1 item 3 keeps the question and obligations); F2 target list replaced by the current R6 residual; Appendix A compact (one entry per version, release-record locator); SG order R1…R14 (R13, R14 currently precede R12, L347–L355). No RID, grade, scope or OPEN obligation may change in stage 2.
- **Atlas:** RECOG.R-T1; process residue under Method v0.2.

**FA-RECOG-02 | Y/I | NUMGEN imports still "RID unavailable"**
- **Location:** §6.13b L728, L730; §7 L1148–L1149; header L7; Appendix A L1320 ("canonical repin … after NUMGEN v1.20.8").
- **Owner state:** NUMGEN v1.20.8 registers `NUMGEN-DEF-N5AS1-DEFECT` ($D_M:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)$, the same formula, restated verbatim in INF-1), `NUMGEN-RESULT-N5AS1-INF1` (`[RESULT] [from: ALG]`), and also `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`, `-RESULT-N5AS1-L-BACKBONE`, `-L-MONO`, `-L-PHASE`.
- **Action:** claim-level check, then repin both imports to `numgen-v1.20.8` by RID; remove tracking keys `A1A-NG-D-DEF`/`A1A-NG-INF1` and the governance text from the live rows (they belong in the release record). Consider importing the lift definition by RID too (§6.13b (i), L746).
- **Atlas:** RECOG.R-P2.

**FA-RECOG-03 | S/E | Statements that contradict RECOG's own current theorems**
- **Location / problem:**
  - SG-R10 (L341): "the quoted leading amplitude … is not a finite-$Q_0$ bound (R9/R10/R11)" — R9 is a THM with explicit $C_2$ rows (§6.13a).
  - §6.13 (L691): "Leading amplitude $|\Lambda|\le0.007652Q_0$ — leading order only, for the truncated model (R9, R10, R11)" — same.
  - §6.14 "R9 budget" (L797): pre-R9 dominance-threshold planning presented as live.
  - §4 routing (L369): the "$p$-family / normal form" layer lists $c_\theta^{(6)}$ and "backbone" as canonical objects although SG-R13 and the §6.14 refusal line exclude them from the chart.
  - SG-R14 quantified note (L353): the T1/T2 import is called a "reference import … no RECOG claim changes", while §6.13b (L740, L762) uses T1/T2 at theorem grade.
- **Action:** restate each at current state; SG-R14 points to §6.13b as the adopted use. This also answers DYAD notice N19/N21 ("N11 correction").
- **Atlas:** RECOG.R-T2.

**FA-RECOG-04 | Y | Fixed-point flag to Dyadic is answered**
- **Location:** §6.3 L473: "(Dyadic §6.1 lists only $P_1,P_2$; flagged to Dyadic in the memo.)"
- **Owner state:** DYAD v6.4.22 §1 fixed-point table lists the wrapped-cylinder winding fixed points $(\log(1+2\pi k),0)$, $(\log(1+2\pi k),\pi)$, $k\ge1$, and states agreement with RECOG §6.3 (owner check M9).
- **Action:** replace the sentence by a pointer to the Dyadic table.

**FA-RECOG-05 | Y | Notice mirror and dependents register**
- **Location:** §7.2 receipts (L1192–L1199), §7.3 register (L1203–L1219), §7 synchronization note (L1114: "current owner edition (Dyadic v6.4.17 … RRF v0.8.3)").
- **Owner state:**
  - DYAD records N11 as adopted use by RECOG-THM-A1A-CD-IDENTIFICATION; N13 used at the v6.4.18 pin.
  - DYAD N19/N21 (prepared): R9 claim-level import row; $S_h=j^6R_0$; the N11 correction; FC-DYAD-32 offered for RECOG's H-NG decision (FC-RECOG-18); frame rule via DYAD-ALG-KP-FRAME-SCALE (FB-RECOG-13); $h_4$ field $\mathbb Q(i\sqrt3)$ for the archival object; "RECOG R11" naming.
  - Consumers: DYAD v6.4.22 keeps T1/T2/OPEN 21 conditional on R9; RER is adopted v0.2 (not r4.6); RRF v0.8.4 imports RECOG v0.3.21 W3 verbatim with RID (§6.3, L452 of RRF).
- **Action:** update §7.2 (N11 adopted use) and §7.3 (current consumer editions); the §7 synchronization note states only current pins.

**FA-RECOG-06 | I | Methodology edition**
- **Location:** header L7–L8 ("DSN_METHODOLOGY_v1.3 (current adopted edition)"), §6.13b L724 ("Methodology v1.3 §3.4 (M13-C04)"), §6.13b L728 ("Methodology §3.3 temporary `RID unavailable`").
- **Owner state:** v1.4 governs (`methodology-v1.4`); §3.4 keeps the same conditional-proof rule and the key M13-C04; §4.2 namespace registry still lists RECOG.
- **Action:** repin to v1.4; the release is built under v1.4 (§13.7 records, §13.9 governing edition).

**FA-RECOG-07 | Y | Release records are not in the repository**
- **Location:** header L6, L52 and §8 cite `RECOG_v0_3_22_RELEASE_RECORD.md`, `RECOG_v0_3_21_RELEASE_RECORD.md`, `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` and the G2/A1a session records; `records/recog/` held none of them before this note.
- **Problem:** the governing edition is the tag with its release record (v1.4 §13.9); a reader of the repository cannot see the record that adopted v0.3.22.
- **Action:** the PI uploads the existing RECOG release and governance records unchanged on an `upload/recog-records` branch (hash-checked against the hashes RECOG prints), before the next release.

### 2.2 Tier B

**FB-RECOG-08 | I | Import rows without RID now have Dyadic RIDs**
- **Location:** §7 L1127 (§6.1 block), L1128 (§6.4 block), L1129 (§6.7/§6.8 block), L1137 (§6.5, 47/54), L1154 ("requesting assignment there is part of the critique round"); §6.15c L859 ("Dyadic v6.4.10 §4" for $Q_c$).
- **Owner state (DYAD v6.4.22):** `DYAD-DEF-PRIMITIVE-MAP` (map), `DYAD-DEF-CRITICAL-CURVE` ($C_0$, with kernel field $k=(\cos\eta,1)$; its record cites RECOG-ALG-P2-C0-WHITNEY-FOLD), `DYAD-ALG-QC-CRITICAL-AMPLITUDE` ($Q_c=(\arcsin\ln2)^2$, §6.4), `DYAD-ALG-ISP-MAPS` (ISP $\Theta$, winding invisibility), `DYAD-ALG-SIXSTEP-CUBIC-JET` ($M+M^\top=-I$), `DYAD-ALG-RAW-ANGULAR-MEAN` (47/54 as $\mathcal A_{\rm raw}$). Non-symplecticity still has no Dyadic RID.
- **Action:** claim-level check, then cite by RID; remove the process sentence at L1154.

**FB-RECOG-09 | Y | Dyadic pins and line-number locators**
- **Location:** §7 rows pinned to v6.4.10; §6.13b imports at v6.4.16 and v6.4.18 with "lines 806–809", "lines 843–850" (L736, L742, L766, L1151–L1152); SG-R14 at v6.4.15 (L353).
- **Problem:** a deliberate, still-valid pin is not a defect (atlas D-PIN). But only `dyad-v6.4.19` and later are tagged in the repository, so these pins cannot be resolved from the repository, and line numbers do not survive the v6.4.21 compaction (anchors do).
- **Action:** one claim-level audit v6.4.18 → v6.4.22 for the imported RIDs (DYAD states the consumed statements unchanged; its §7.0 lists RECOG v0.3.22 as consumer of §6.14); repin to `dyad-v6.4.22` with section anchors; keep a historical pin only where it is the load-bearing source, labelled as such (v1.4 §1.1 item 4). Same for NUMGEN pins at v1.15 / v1.20.7 (L463, L506, L1132–L1133, L1140) against `numgen-v1.20.8`.

**FB-RECOG-10 | I | Identifier hygiene**
- RECOG-OPEN-INTERSECTION carries `[OPEN]` in §1 (L84) and `[HYP]` in §6.5 (L508) and R6 (L220): one claim, two grades.
- RECOG-ALG-LEADING-RETURN-EQUIVARIANCE heads two entries (§6.10 L622 consequence, §6.12 L666 theorem); keep one home, point from the other.
- `E2C-ENG-SPLIT-REFINEMENT` (L817) lacks the RECOG namespace (v1.4 §4.2).
- Not a finding: THM-word RIDs graded `[ALG via IA]` (RECOG-THM-TWIN-P9-SADDLE, -P9-STABLE-LOCAL) and the RESULT-word RID graded `[ALG]` (RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE). Under v1.4 the category word is immutable identity text, not live status; no rename is requested.
- **Atlas:** RECOG.R-G1, R-R3 (narrowed here).

**FB-RECOG-11 | I | Load-bearing results without RID**
- **Location / items (atlas RECOG.R-R2):** the exact-map comparator-incompleteness corollary `[THM]` (§6.13a L709; exported in §6.9 L609 and used by R6 and F1); the P2-HET corollary and the P2-C0-FIRST corollaries; the swap-odd $\rho$ lemma (§6.4 L483); the radial-fate law (§6.7 L572); the exact radial identity $\Re(\bar\lambda\nu_3)=-\sin^2(\theta/2)$ (§6.10 L632; Dyadic folds it into its import of NU3-CLOSED-FORM); the fixed-point inventory (§6.3); the finite ledger $\mu_5,\mu_7,\nu_3^{(1,5)},\nu_3^{(1,7)}$; the uncoupled-pair law (§6.12 L671); the A1a finite-block identity (L754, "no RID").
- **Action:** the owner decides which to register; priority to the three that other owners consume (incompleteness corollary, radial identity, fixed-point inventory).

**FB-RECOG-12 | S | Unlabelled frame in a lattice ratio**
- **Location:** §6.13 L685: "the 'leading-crossing' value $|\mu|/|c_{05}|\approx41.3$".
- **Check (atlas-checked):** with $|\mu|^2=19/12$, $\mathcal I_{\rm lat}=|c_{05}|/|\mu|^2$: post-$H_2$ $|\mu|/|c_{05}^{\rm NF}|\approx59.12$; raw $|\mu|/|c_{05}^{\rm raw}|\approx41.27$. The quoted 41.3 is the raw-frame value in a paragraph about NF quantities.
- **Action:** label the frame (SG-R10 requires it) or give both values.
- **Atlas:** RECOG.R-S2.

**FB-RECOG-13 | I | Frame scale across $p$ is now a Dyadic RID**
- **Location:** §6.10 L620 ("The $p=6$ member in this $Z$-frame relates to the $W$-frame by the exact scale $6\bar\lambda\nu_3(\zeta_6)=3\mu_6^W$"), R2 residual L134.
- **Owner state:** `DYAD-ALG-KP-FRAME-SCALE`: $W_p=i\cot(\pi/p)\,Z$, $\nu_3^Z=\cot^2(\pi/p)\,\nu_3^{W_p}$ ($=3$ at $p=6$); exported $\mu_p$/$\nu_3$ name their frame (DYAD N19 frame rule).
- **Action:** cite the Dyadic RID at the $p=6$ scale statement; tag RECOG-ALG-NU3-CLOSED-FORM and the $\Re\mu_p$ law as $Z$-frame exports.

**FB-RECOG-14 | Y | $S_h$ and the exact smooth involution**
- **Location:** §6.4 L483 (covariance premise, $S_h$), §6.14 L795 (relabeling action), R1 (L103–L120).
- **Owner state:** DYAD §6.15–§6.17: $S_h$ equals $R_0$ through degree 6 and is not an exact commuting involution ($S_h=j^6R_0$, N19); DYAD-THM-SMOOTH-EMBEDDING gives a $C^\infty$ involution $R=T^3\circ K_2^{-1}$, $DR(0)=-I$, commuting exactly with $T$ near $P_1$.
- **Action:** record the relation at §6.14; in R1 note that an exact nonlinear swap commuting with $T$ exists for the isolated-dyad germ in $C^\infty$. This does not settle physical relabeling (RRF OPEN-A, OPEN-OFN-OPA) and does not close R1.
- **Atlas:** H12, RECOG.R-L5.

**FB-RECOG-15 | Y | Notice and audit state inside the live file**
- **Location:** §7.1 "Notices to the OFN owner (i) OFN pins RECOG v0.3.1 — current is v0.3.20" (L1177); §7.2 "Outbound notices (G3)" (L1201); Appendix A "G3 notices to OFN, RRF and RER unsent" (L1320); the §7.1/§7.2 audit tables (claim-level synchronization of earlier editions).
- **Owner state elsewhere:** RER v0.2 records the RECOG G3 notice (W1/W3 quoted from §6.16g); RRF v0.8.4 imports W3 verbatim from RECOG v0.3.21 with RID and labels inter-space transport as a separate OPEN extension (RF-1 answered).
- **Action:** keep in §7 the current import rows and a current notice table only; move audit and notice history to `records/recog/` (with FA-RECOG-01).
- **Atlas:** RECOG.R-P3.

**FB-RECOG-16 | E | Bridge-lemma custody wording**
- **Location:** §6.10 L622 ("Ownership of this general theorem is recommended for Dyadic"), R2 L127, §7 L1135.
- **Owner state:** DYAD keeps DYAD-ALG-BRIDGE-LEMMA (frame-named) with RECOG-ALG-LEADING-RETURN-EQUIVARIANCE as general-$p$ proof provenance; the §7 mutual-citation guard already says so.
- **Action:** state the settled custody once (RID Dyadic, proof RECOG) and drop the open recommendation, or re-raise it as an explicit request in a record.
- **Atlas:** RECOG.R-L4, DYAD.X6.

**FB-RECOG-17 | E | Symbol load in §6.13b**
- **Location:** §6.13b L746–L767: $M$ is both the block count in $D_M^U$, $\lim_M$ and $MQ_M$, and the retained memory $M(z_0)$, $M_W$ — in the same formula $C_D^{\rm ext}=\lim_M(D_M^U-\tau\log M)=\ldots-M(z_0)$.
- **Action:** rename the block count locally (e.g. $N$), keeping NUMGEN's $D_M$ name at the import.
- **Atlas:** RECOG.R-Y1/Y2.

**FB-RECOG-18 | Y | Evidence held outside the repository**
- **Location:** §8 (L1221–L1261): about 40 scripts, certificates and records (R8, B3, E2C chunk files, E3A, R9, A1a), several run by the PI; Arb runs executed once (atlas RECOG.R-D1: D-PROOF (c)); RECOG-ALG-CHART-SHADOW has a numerical script only (D-PROOF (b)).
- **Problem:** corpus goal — every claim testable from the repository. None of these files is in `evidence/`.
- **Action:** a source-recovery list as for DYAD (`records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`); collection can be deferred, the list cannot. No certificate rerun is requested.

### 2.3 Tier C

**FC-RECOG-19 | S | `~` R9-free existence on all of $U$ (H-NG discharge)**
- **Premises (owner results):** $D_M^U=\tau\sum_{m<M}Q_m-\sum_{m<M}r_m$ with $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$ (DYAD-THM-LPHASE-ROWA-REMAINDER, row A, base points in $U$); $Q_M^{-1}=Q_0^{-1}+M+O(\sqrt M)$ (RECOG-THM-A1A-RECIPROCAL-AMPLITUDE), so $Q_m=1/(m+Q_0^{-1})+O(m^{-3/2})$ and $Q_m^{3/2}=O(m^{-3/2})$.
- **Consequence:** $D_M^U-\tau\log M$ converges for every $x_0\in U$, without R9 and without INF-1. With RECOG-THM-A1A-PHASE-EXISTENCE-ALT (H-NG ⇒ conclusion) this would extend RECOG-RESULT-A1A-PHASE-EXISTENCE-NG from $U\cap U_{\rm NUMGEN}$ (no radius) to the explicit $U$.
- **Not supplied:** R9 coefficients, $C_2$, an R9-free OPEN 21.
- **Check:** lift and indexing conventions (DYAD §7.0a I1–I5 vs §6.13b (i)–(iii)), the start-domain restriction, no circular import. Offered by DYAD as FC-DYAD-32 (N19); RECOG owns the decision.
- **Atlas:** RECOG.R-L1, H5.

**FC-RECOG-20 | S | `~` Lattice-clock rate from RECOG's own theorems**
- RECOG-ALG-LATTICE-CLOCK imports its rate from NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO (L687). R9 gives $\Theta_m=\Psi_\infty+\tau\log q_m+o(1)$ and $1/q_m=m+O(\log m)$ (§6.13a corollary), hence $\Theta_m=\Psi_\infty-\tau\log m+o(1)$ and threshold ratios $\to e^{\pi/(3\tau)}$ on the $C_z$ track, without the import.
- **Check:** owner verification; keep the NUMGEN cross-reference with the differing scope reading (RECOG SG-R10 vs NUMGEN SG-NG-23).
- **Atlas:** RECOG.R-L3, NUMGEN.N-L7.

**FC-RECOG-21 | S | `~` Proof route for Genesis chrono-protection**
- RECOG-ALG-LEADING-RETURN-EQUIVARIANCE with $L=\operatorname{diag}(A,A,A)$ and the charge rule gives six-step quadratic vanishing $G_2=0$ (degree-2 charges $\in\{2,0,-2\}$, none $\equiv1\bmod6$), i.e. Genesis *GEN:chrono-protection, whose proof source GEN-ART-G2-CHRONO is missing.
- **Action:** a RECOG corollary line is optional; the main beneficiary is GEN (routed in the GEN advisory).
- **Atlas:** RECOG.R-L2, NUMGEN.N-L6.

**FC-RECOG-22 | S | `~` Section-shadow law for the exact involution**
- If $j^2R=j^2S_h$ (follows from FB-RECOG-14), RECOG-ALG-SH-SECTION-SHADOW's $\pm\tfrac3{8\sqrt Q}$ displacement holds for $R(\Sigma_B)$ as well.
- **Check:** owner verification of the jet agreement.

### 2.4 Items routed to other owners (no RECOG edit)

| item | owner | content |
|---|---|---|
| GAP-LOCK Lemma 3 grade of use | NUMGEN | NUMGEN §9.2 says RECOG uses Lemma 3 "at HEUR"; RECOG uses it inside `[ALG]` RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE (L1011) and as a `[HEUR cross-reference]` in R6 (L218). Lemma 3 has no RID (atlas NUMGEN.N-G1). |
| explicit-domain inputs | NUMGEN | RECOG-THM-A1A-LIFT-ALIGNMENT and -RECIPROCAL-AMPLITUDE are explicit forms of NUMGEN L-MONO / L-BACKBONE on $U_T$ / $U$ (atlas NUMGEN.N-B, N-L5). |
| phase-moment retest | GEN | GEN OPEN 1A #2 should use RECOG-ALG-CHART-LAWS / R9, not the archival $c_\theta^{(6)}$ (opposite sign to the chart coefficient $+\tfrac{89\sqrt3}{324}$) (atlas RECOG.R-L6, H6). |
| VF-1 citation | RECOG/RRF | RECOG F3(b) cites VF-1 through the RRF label; the Dyadic RID is DYAD-ALG-NF6-DEG10 (atlas RECOG.R-L8). Optional RECOG edit. |

## 3. Summary

| tier | rows |
|---|---|
| A | FA-RECOG-01 … 07 (7) |
| B | FB-RECOG-08 … 18 (11) |
| C | FC-RECOG-19 … 22 (4) |
| routed | 4 |


Atlas D3 L5 items not carried into a row: RECOG.R-L7 (answered by FA-RECOG-03/05), R-T3 (deleted in atlas v0.2 as process state; covered by FB-RECOG-15).

## 4. Requests to the reviewer (second pass)

1. Check the Tier A/B rows independently against `recog-v0.3.22`; add what this pass missed.
2. Rule on FB-RECOG-10's narrowing (category word is identity, not status) for RECOG as it was ruled for DYAD.X4.
3. Check the arithmetic of FC-RECOG-19 (convergence of $\tau\sum Q_m-\tau\log M$ from the reciprocal-amplitude bound).
