# Atlas Advisory — Relational Recognition DSN v0.3.22 — FINAL PROPOSAL v1.0

**To:** the RECOG stream owners and reviewers. **From:** the atlas owner (Claude), consolidating two passes over the same source and the same atlas basis:
- **[C]** `records/recog/ATLAS_ADVISORY_NOTE_RECOG_v0_3_22_v0_1.md` (Claude, 22 rows + 4 routed);
- **[G]** `records/recog/ATLAS_ADVISORY_RECOG_INDEPENDENT_REVIEW.md` (ChatGPT, independent full-source assessment after reading [C]; 22 row assessments, four additional findings IRR-01–04, a written proof for FC-19, 12/12 bounded checks in `evidence/recog/atlas_review/recog_advisory_checks.py`).

**Date:** 23 October 2026.
**Source under review:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22`, tag `recog-v0.3.22`, 1,581 lines, 329,148 bytes, SHA-256 `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9`; both passes read it in full. Line numbers refer to that file.
**Atlas basis:** atlas v0.2 (tag `atlas-v0.2`, merge `6c52666`, SHA-256 `9963aead…31c5`).
**Status:** noncanonical advisory. It is not an amendment, adoption, regrade or notice. RECOG v0.3.22 is unchanged. The owners decide every row. Both earlier notes stay as working records and are not edited.

---

## 0. How the two passes were reconciled

- **Overlap.** [G] supports 18 of the 22 [C] rows as scoped, revises two (FA-03, FB-14) and narrows two (FB-09 claim-level audit, FB-16 custody wording). Each appears once below with both sources.
- **Additions from [G].** IRR-01 (RESULT tag grammar), IRR-02 (missing remainder in a §5 summary), IRR-03 (further stale F2 follow-ons), IRR-04 (frame wording and rounded equalities). The atlas owner re-checked all four against the tagged text; all hold (the 19 RESULT blocks were recounted: 16 without `[from: …]` at L548, 837, 853, 865, 873, 905, 956, 995, 999, 1019, 1021, 1030, 1052, 1054, 1108, 1110; three combined or alias forms at L487, 927, 1003).
- **Corrections to [C] adopted.**
  - FA-03: the SG-R10 warning that the leading amplitude is not a finite-$q_0$ bound for the whole exact memory is **valid** and stays; only the stale routing and the T1/T2 "reference import" wording change.
  - FB-14: $S_h=h_6\circ(-I)\circ h_6^{-1}$ is an **exact involution** on its domain; what holds only through degree 6 is its commutation with the map. The correct relation is $j^6S_h=j^6R_0$, not an identity of full maps.
  - FA-05: prepared Dyadic notices (N19, N21) are not receipts.
  - FA-06: v0.3.22 was adopted under Methodology v1.3; migration to v1.4 is a successor action, not retroactive noncompliance.
  - Cross-reference fix: the H-NG item is FC-RECOG-21 below ([C] FC-19; [C] FA-05 wrongly said FC-18).
- **Agreed narrowing.** A category word inside an RID (`THM`, `RESULT`, `CAND`, `OPEN`) is immutable identity text, not live status; no RID is renamed for that reason ([C] FB-10, [G] §2.3; as ruled for DYAD.X4).
- **Tiers.** **A** = resolve in this owner pass. **B** = same release unless a named dependency blocks it. **C** = scientific opportunity, optional for the maintenance release; a deferral names its missing premise or next test.
- **Types.** S scientific · I interface/identifier · Y synchronization · E editorial · F formatting.
- **Keys.** `FA-/FB-/FC-RECOG-nn` are tracking keys only; numbering is new in this proposal (map to [C] and [G] in §4).
- `~` marks a link the atlas derived itself; verify before use.

---

## 1. Requested outcome and release contract

1. **One owner successor** (the team picks the number) through draft → change-focused review → PI adoption, built under Methodology v1.4.
2. **Two stages, correction before compaction.**
   - Stage 1: every substantive status, grade, scope and wording correction (all Tier A/B content rows, including the RESULT-grammar decisions of FA-RECOG-08). Record the intermediate hash.
   - Stage 2: layout-only compaction (FA-RECOG-01), with a per-block movement map, checked by `tools/check_compaction.py`. Stage 2 must not set a grade, change a hypothesis or delete a live obligation because it sits inside old text.
   - The checker must be calibrated on the RECOG profile (header, anchors, alias grammar, artifact and OPEN forms), with negative controls for scope deletion, wrong RID attachment, missing evidence pointer and stale-state preservation. Passing the DYAD pilot does not validate a new profile.
3. **Disposition per row**: accept / reject / defer, reason, edited section or RID, validation. A reject needs a reason; a defer names the missing premise or next test. "Noted for a future release" alone is not implementation of an accepted current-state correction.
4. **Release record** under `records/recog/` with the intermediate and final identities, the correction and compaction deltas, the checker results, the current import and consumer tables, and the recovery and notice limitations stated as they are.
5. **Notices** after the release hash is fixed. Keep *prepared*, *sent*, *received*, *statement accepted* and *adopted use* separate. Material changes to exported claims follow RECOG §7.3's pre-release notification rule.
6. The atlas is refreshed from the adopted successor, never from this note.

---

## 2. Findings register

### 2.1 Tier A — resolve in this owner pass

**FA-RECOG-01 | E | Live-file rule and compaction [C FA-01; G IRR-03, §2.4]**
- **Location:**
  - header: 21 stacked status summaries v0.2.1–v0.3.22 (L12–L60); about 25 "*Earlier freeze history*" sentences (L52); a 25-edition Supersedes list (L6);
  - closed OPEN entries keeping old specifications: R8 (L159–L166), R9 (L237–L249), R10 (L284–L291, status "DELIVERED and ACCEPTED" where the census says CLOSED), R11 ("Former OPEN R11 text (v0.3.1), retained for the record", with `[OPEN]` sub-items, L268–L280), R7 (closed items under "Active sub-items", L301–L304);
  - stale F2 follow-ons: F1 ledger cell "the subject of F2(b)" (L880), "CELL-F2 targets" and "Order: F2(b) before F2(c0)" (L907–L913), "remaining F2(a) question" (L927), "Next: F2(c0)" (L956), F2(c1) posed as the open follow-on (L972–L974);
  - dated inline history (L644, L656); §9 "Archive. none yet", "critique round pending" (L1267–L1268); Appendix A, 22 full entries (L1317–L1528); SG order R13, R14 before R12 (L347–L355).
- **Action:** stage 2 (after stage 1): one current status paragraph; closed OPEN entries keep question, closure, closing RIDs and residuals (v1.4 §1.1 item 3); stale F2 pointers become current result pointers plus the actual R6 residual; Appendix A compact with release-record locators; SG order R1…R14. History stays at `recog-v0.3.22`.
- **Must stay live:** F2(a3)'s selection question; registry-relative limits; the absence of independent write-through; W1–W5; R6 ACTIVE.
- **Atlas:** RECOG.R-T1.

**FA-RECOG-02 | Y/I | NUMGEN imports "RID unavailable" [C FA-02; G support]**
- **Location:** §6.13b L728, L730; §7 L1148–L1149; header L7; Appendix A L1320.
- **Owner state:** NUMGEN v1.20.8 registers `NUMGEN-DEF-N5AS1-DEFECT` (same $D_M$ formula, restated verbatim in INF-1) and `NUMGEN-RESULT-N5AS1-INF1` (`[RESULT] [from: ALG]`); also `-DEF-N5AS1-PRIMITIVE-LIFT`, `-RESULT-N5AS1-L-BACKBONE`, `-L-MONO`, `-L-PHASE`.
- **Action:** claim-by-claim repin to `numgen-v1.20.8`; drop tracking keys and governance text from live rows; keep the overlap-domain distinction ($U$ vs $U\cap U_{\rm NUMGEN}$).
- **Atlas:** RECOG.R-P2.

**FA-RECOG-03 | S/E | Stale routing and stale use wording; keep the valid guard [C FA-03 revised by G §2.1]**
- **Keep:** SG-R10 (L341) and §6.13 (L691): the leading amplitude is not a finite-$q_0$ bound for the full exact memory. That stays true after R9.
- **Update:**
  - Replace the routing "(R9/R10/R11)" by a pointer to the certified rows: from RECOG-THM-R9-MEMORY, $|M-c_{\rm iso}q_0|\le|G|q_0+C_2q_0^2$ and $|M|\le(|c_{\rm iso}|+|G|)q_0+C_2q_0^2$ (elementary consequence, [G]), per row, $C_z$ track, normalized $q$; comparator incompleteness only for $q_0<|G|/C_2$.
  - §6.14 "R9 budget" (L797): name $2C_7q_0^2$ as the degree-≥7 partial budget, distinct from the full remainder $C_2q_0^2$; its thresholds use the amplitude $|G|$, not the phase-dependent $\Lambda_1(\Theta)$.
  - §4 routing (L369): $c_\theta^{(6)}$ and "backbone" are not canonical chart objects (SG-R13, refusal line).
  - SG-R14 quantified note (L353): T1/T2 are in adopted use in §6.13b (L740, L762), not a reference import only.
- **Atlas:** RECOG.R-T2.

**FA-RECOG-04 | Y | Fixed-point flag answered [C FA-04; G support]**
- **Location:** §6.3 L473 "(Dyadic §6.1 lists only $P_1,P_2$; flagged to Dyadic in the memo.)"
- **Owner state:** DYAD v6.4.22 §1 table lists the lifted-chart fixed points and the wrapped-cylinder winding fixed points $(\log(1+2\pi k),0)$, $(\log(1+2\pi k),\pi)$, $k\ge1$, and states agreement with RECOG §6.3.
- **Action:** pointer to the Dyadic table; keep the lifted/wrapped distinction and the winding index.

**FA-RECOG-05 | Y | Consumer register and notice mirror [C FA-05; G receipt boundary]**
- **Location:** §7 synchronization note (L1114), §7.2 receipts (L1192–L1199), §7.3 register (L1203–L1219).
- **Owner state:** DYAD records N11 as adopted use by RECOG-THM-A1A-CD-IDENTIFICATION, N13 in use at the v6.4.18 pin; DYAD v6.4.22 keeps T1/T2/OPEN 21 conditional on R9; RER is adopted v0.2; RRF v0.8.4 imports RECOG v0.3.21 W3 verbatim with RID. DYAD N19 and N21 to RECOG are **prepared, not sent** (`records/dyad/DYAD_NOTICES_N16_N21.md`); their content is input for FA-03, FB-15, FB-16 and FC-21, not a receipt.
- **Action:** update §7.2 (N11 adopted use) and §7.3 (current consumer editions); keep actual input pins; keep the five notice states separate.

**FA-RECOG-06 | I | Methodology edition for the successor [C FA-06; G scope]**
- **Location:** header L7–L8; §6.13b L724 ("Methodology v1.3 §3.4 (M13-C04)"), L728.
- **Owner state:** v1.4 governs; §3.4 keeps the conditional-proof rule and the key M13-C04.
- **Action:** the successor is built and pinned under v1.4. v0.3.22 itself was correctly adopted under v1.3.

**FA-RECOG-07 | Y | Release records outside the repository [C FA-07; G §6]**
- **Location:** header L6, L52, §8: `RECOG_v0_3_22_RELEASE_RECORD.md`, `RECOG_v0_3_21_RELEASE_RECORD.md`, `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md`, G2/A1a records.
- **State:** none is in the repository; [G] found none in its accessible files (bounded search, not exhaustive).
- **Action:** the PI uploads the **original** records unchanged on an `upload/recog-records` branch, hash-checked against the hashes RECOG prints. Nothing is recreated. If an original cannot be found, its absence is recorded as a release limitation by explicit PI decision; it is not a mathematical defect. The successor gets its own release record in any case.

**FA-RECOG-08 | I | RESULT tag grammar [G IRR-01]**
- **Location:** §§1–6: 16 line-leading `[RESULT]` blocks without `[from: TAG]` (L548, 837, 853, 865, 873, 905, 956, 995, 999, 1019, 1021, 1030, 1052, 1054, 1108, 1110) and three combined or alias forms (L487 `[from: ALG conditional]`, L927 `[from: NUM strong, ALG]`, L1003 `[from: THM, ALG, RESULT]`). Bounded scan; §9 credits, history, table cells and headings excluded.
- **Rule:** Methodology v1.4 §3.4: RESULT is a synthesis marker paired with exactly one canonical tag; heterogeneous conclusions are split.
- **Action:** owner decision per block in stage 1. Not an automatic relabel; registry-relative conclusions, conditional assertions and physical nonclaims keep their wording.

**FA-RECOG-09 | S | Missing remainder in a high-risk summary [G IRR-02]**
- **Location:** §5 radial-neutrality row (L416) prints $Q(T^6(t,0))-t^2=6\gamma t^6$; the governing §6.7 text (L572) has $+O(t^8)$.
- **Action:** restore the remainder or say "degree-six term". The cubic-neutrality conclusion is unchanged.

### 2.2 Tier B — same release unless blocked

**FB-RECOG-10 | I | Import rows without RID now have Dyadic RIDs [C FB-08; G support]**
- **Location:** §7 L1127, L1128, L1129, L1137, L1154; §6.15c L859 ("Dyadic v6.4.10 §4" for $Q_c$).
- **Owner RIDs (v6.4.22):** `DYAD-DEF-PRIMITIVE-MAP`; `DYAD-DEF-CRITICAL-CURVE` ($C_0$, kernel field $k$; its record cites RECOG-ALG-P2-C0-WHITNEY-FOLD — this creates no dependency loop); `DYAD-ALG-QC-CRITICAL-AMPLITUDE`; `DYAD-ALG-ISP-MAPS`; `DYAD-ALG-SIXSTEP-CUBIC-JET` ($M+M^\top=-I$); `DYAD-ALG-RAW-ANGULAR-MEAN` (47/54). Non-symplecticity has no Dyadic RID.
- **Action:** claim-level mapping, then cite by RID; keep missing-RID exceptions where genuinely unassigned; remove the process sentence at L1154.

**FB-RECOG-11 | Y | Pins: claim-level audit, not blind repin [C FB-09 narrowed by G]**
- **Location:** §7 rows at Dyadic v6.4.10; §6.13b imports at v6.4.16/v6.4.18 with "lines 806–809", "843–850" (L736, L742, L766, L1151–L1152); SG-R14 at v6.4.15 (L353); NUMGEN pins at v1.15/v1.20.7 (L463, L506, L1132–L1133, L1140).
- **Point:** a deliberate valid pin is not a defect, and old line references stay true at their own pins. But only `dyad-v6.4.19` and later and `numgen-v1.20.8` are in the repository.
- **Action:** claim-level audit against `dyad-v6.4.22` / `numgen-v1.20.8`; distinguish the current counterpart from the historical producer input; keep proof-source editions where they are load-bearing, labelled; use section anchors for new references.

**FB-RECOG-12 | I | Identifier clarity [C FB-10 narrowed; G §2.3]**
- RECOG-OPEN-INTERSECTION: separate the HYP scientific assertion (§6.5 L508, R6 L220) from the OPEN task status (§1 L84). A clarity repair, not a mathematical contradiction.
- RECOG-ALG-LEADING-RETURN-EQUIVARIANCE: authoritative statement §6.12 (L666); other sites (§1 L86, §6.10 L622) point to it.
- `E2C-ENG-SPLIT-REFINEMENT` (L817): owner-approved custody/identifier mapping into the RECOG namespace; no silent rewrite.
- Not requested: renaming THM/RESULT-word RIDs whose grade differs.

**FB-RECOG-13 | I | Load-bearing results without RID [C FB-11; G owner decision]**
- Candidates (atlas RECOG.R-R2): the exact-map comparator-incompleteness corollary `[THM]` (§6.13a L709; exported §6.9 L609); P2-HET and P2-C0-FIRST corollaries; swap-odd $\rho$ lemma (L483); radial-fate law (L572); radial identity $\Re(\bar\lambda\nu_3)=-\sin^2(\theta/2)$ (L632); fixed-point inventory (§6.3); finite ledger $\mu_5,\mu_7$; uncoupled-pair law (L671); A1a finite-block identity (L754).
- **Action:** owner decides; priority to externally consumed claims. An explicitly identified sub-statement under an existing RID may suffice. No RID is assigned by this advisory.

**FB-RECOG-14 | S/F | Frame labels and rounded equalities [C FB-12; G IRR-04]**
- §6.13 L685 "$|\mu|/|c_{05}|\approx41.3$": raw-frame value; post-$H_2$ value $\approx59.12$ (verified by both passes: $41.2694355\ldots$, $59.1194304\ldots$). Label the frame; do not silently replace the raw calculation.
- $|G|=\sqrt{481897}/90720\approx0.007651984290981194$; replace "$|G|=0.0076520$" (L703 and siblings) by $\approx$ or a certified upper bound; keep $|G|/517$, $|G|/163$ exact with displays $\approx1.4800743309\times10^{-5}$, $\approx4.6944688902\times10^{-5}$ (L713–L714). Keep the partial-budget thresholds $|G|/(2C_7)$ distinct from the incompleteness windows.

**FB-RECOG-15 | I | Frame scale and frame-independence wording [C FB-13; G IRR-04]**
- §6.10 L620 and R2 L134: cite `DYAD-ALG-KP-FRAME-SCALE` ($W_p=i\cot(\pi/p)Z$, $\nu_3^Z=\cot^2(\pi/p)\nu_3^{W_p}$, factor 3 at $p=6$); tag RECOG-ALG-NU3-CLOSED-FORM and the $\Re\mu_p$ law as $Z$-frame exports.
- §6.2 L457 "Leading coefficient, return order and local strict contraction are frame-independent": restrict to the stated tangent-to-identity comparison (L451 already says magnitudes change under linear rescaling); refer complex linear scaling to the frame rule.

**FB-RECOG-16 | Y | $S_h$, $R_0$ and the smooth involution [C FB-14 revised by G §2.2]**
- **Owner state:** $S_h=h_6\circ(-I)\circ h_6^{-1}$ is an exact involution on its domain; its commutation with $f$ is certified through degree 6 only; $j^6S_h=j^6R_0$ (DYAD §§6.14–6.16). DYAD-THM-SMOOTH-EMBEDDING gives a $C^\infty$ involution $R=T^3\circ K_2^{-1}$, $DR(0)=-I$, commuting exactly with $T$ at germ scope.
- **Action:** record $j^6S_h=j^6R_0$ at §6.14 (L795). Reference the smooth commuting involution at its owner-stated germ scope.
- **Must not:** identify $R$ with the delivered finite-chart action, transfer finite-chart radii to it, read it as physical pole/node exchange, or use it to discharge the §6.4 linear-swap covariance premise. R1, RRF OPEN-A and OPEN-OFN-OPA stay open.

**FB-RECOG-17 | Y | Notice and audit state inside the live file [C FB-15; G support]**
- **Location:** §7.1 notices (L1177); §7.2 "Outbound notices (G3)" (L1201); Appendix A "G3 notices to OFN, RRF and RER unsent" (L1320); §7.1/§7.2 audit tables.
- **Recorded use elsewhere:** RRF v0.8.4 quotes same-space W3 with RID and labels inter-space transport as a separate OPEN extension; RER v0.2 records the G3 input to G9.
- **Action:** §7 keeps current import rows and a current notice table; audit and notice history move to `records/recog/` (with FA-01). Do not record a receipt RECOG has not received.

**FB-RECOG-18 | E | Bridge-lemma custody wording [C FB-16 narrowed by G]**
- **Location:** §6.10 L622, R2 L127, §7 L1135.
- **Action:** state the existing split once: DYAD-ALG-BRIDGE-LEMMA is Dyadic's RID; RECOG-ALG-LEADING-RETURN-EQUIVARIANCE supplies the general-$p$ proof. Remove the open "recommended for Dyadic" sentence; no ownership transfer.

**FB-RECOG-19 | E | Symbol load in §6.13b — optional [C FB-17; G optional]**
- $M$ is the block count ($D_M^U$, $\lim_M$, $MQ_M$) and the retained memory ($M(z_0)$, $M_W$) in one formula (L746–L767). A local block-index rename with a reversible symbol map, or a notation line; keep NUMGEN's $D_M$ at the import.

**FB-RECOG-20 | Y | Evidence and source inventory [C FB-18; G §6]**
- **Location:** §8 (L1221–L1261): about 40 scripts, certificates and records; none in `evidence/`.
- **Action:** a recovery inventory as for DYAD: original name, printed hash (full vs short), RID/use, location, access state, next action. [G]'s package holds a 71-file-name starting list (not in the repository; a starting list, not a recovery). Collection may be deferred; the inventory may not.
- **Not a defect by itself:** file absence or a single Arb run (D-PROOF (b)/(c)) does not refute a result.

### 2.3 Tier C — optional; not a maintenance gate

**FC-RECOG-21 | S | R9-free existence of $C_D^{\rm ext}$ on all of $U$ [C FC-19; G §5 written proof]**
- **Premises:** DYAD-THM-LPHASE-ROWA-REMAINDER (row A, base points in $U$, not conditional on R9): block increment $2\pi-\tau Q_m+r_m$, $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$; RECOG-THM-A1A-RECIPROCAL-AMPLITUDE: $Q_m^{-1}=a+m+O(\sqrt m)$, $a=Q_0^{-1}$ (no R9); the A1a interface's common lift and block clock.
- **Result ([G] §5, written proof; atlas owner agrees):** $Q_m-1/(a+m)=O(m^{-3/2})$ and $\sum Q_m^{3/2}<\infty$, so
  $C_D^{\rm ext}=\lim_N(D_N^U-\tau\log N)=\tau H(a)+\tau\sum_m\big(Q_m-\tfrac1{a+m}\big)-\sum_m r_m$, with $H(a)=-\log a+\sum_m\big[\tfrac1{a+m}-\log(1+\tfrac1{a+m})\big]$, exists for every $x_0\in U$, without R9 and without NUMGEN INF-1. With the finite-block identity this gives convergence of $\Psi_W$ and $\Psi_z$ (H-NG discharged for RECOG-THM-A1A-PHASE-EXISTENCE-ALT).
- **Not supplied:** $c_{\rm iso}$, $\Lambda_1$, $C_2$, R9 incompleteness, an R9-free quantitative OPEN 21; starts in $U_T\setminus U$; any extension of NUMGEN's adopted domain; any physical memory or token mechanism.
- **Action if adopted:** register under its own RECOG identity; keep the existing NUMGEN-based route and result unchanged (editing the restricted result's domain would hide a scientific change). DYAD offered the same route as FC-DYAD-32 (N19, prepared).
- **Atlas:** RECOG.R-L1, H5.

**FC-RECOG-22 | S | `~` Lattice-clock rate from R9 [C FC-20; G conditional]**
- RECOG-ALG-LATTICE-CLOCK imports its rate from NUMGEN (L687). From R9, $\Theta_m=\Psi_\infty-\tau\log m+o(1)$ on the $C_z$ track. **Before deriving the ratio:** fix the first-passage index definition, eventual direction/monotonicity and vanishing overshoot. Equal rates do not identify two event streams; the scope readings differ (RECOG SG-R10 vs NUMGEN SG-NG-23).

**FC-RECOG-23 | S | `~` Proof route for Genesis chrono-protection [C FC-21; G conditional]**
- RECOG-ALG-LEADING-RETURN-EQUIVARIANCE with $L=\operatorname{diag}(A,A,A)$ and the charge rule gives $G_2=0$. Applies only after checking GEN's actual map, block linear action and domain/closure restriction. GEN owns the conclusion; this does not recover the missing `GEN-ART-G2-CHRONO` bytes.

**FC-RECOG-24 | S | Leading section-shadow coefficient for $R(\Sigma_B)$ [C FC-22; G scoped]**
- With $j^2R=j^2S_h$ (from FB-16, after matching frames), RECOG-ALG-SH-SECTION-SHADOW's leading coefficient $\pm\tfrac3{8\sqrt Q}$ carries over, with the same $O(1)$ limits; no finite-$Q$ offset, global domain, physical exchange or token identity.

### 2.4 Routed to other owners (no RECOG edit required)

| item | owner | content |
|---|---|---|
| GAP-LOCK Lemma 3 use | NUMGEN | RECOG uses Lemma 3 at ALG inside the exact log-equivalence proof (L1011) and as a separate HEUR cross-reference in R6 (L218); NUMGEN §9.2 records only "at HEUR". Lemma 3 has no RID (atlas NUMGEN.N-G1). |
| explicit-domain inputs | NUMGEN | RECOG-THM-A1A-LIFT-ALIGNMENT and -RECIPROCAL-AMPLITUDE are explicit forms of NUMGEN L-MONO / L-BACKBONE on $U_T$ / $U$ (atlas NUMGEN.N-B, N-L5). |
| phase-moment retest | GEN | GEN OPEN 1A #2 should use RECOG-ALG-CHART-LAWS / R9, not archival $c_\theta^{(6)}$ (opposite sign to the chart coefficient $+\tfrac{89\sqrt3}{324}$) (atlas RECOG.R-L6, H6). |
| VF-1 | RECOG (optional) | cite `DYAD-ALG-NF6-DEG10` directly instead of the RRF label (atlas RECOG.R-L8); identifier routing only. |

---

## 3. Owner disposition table (to be filled by the RECOG owners)

| row | tier/type | decision | reason | location / RID | validation | consumers |
|---|---|---|---|---|---|---|
| FA-RECOG-01 | A/E | | | | | |
| FA-RECOG-02 | A/Y,I | | | | | NUMGEN |
| FA-RECOG-03 | A/S,E | | | | | DYAD (T1/T2 use) |
| FA-RECOG-04 | A/Y | | | | | DYAD |
| FA-RECOG-05 | A/Y | | | | | DYAD, RER, RRF, OFN |
| FA-RECOG-06 | A/I | | | | | — |
| FA-RECOG-07 | A/Y | | | | | PI |
| FA-RECOG-08 | A/I | | | | | — |
| FA-RECOG-09 | A/S | | | | | — |
| FB-RECOG-10 | B/I | | | | | DYAD |
| FB-RECOG-11 | B/Y | | | | | DYAD, NUMGEN |
| FB-RECOG-12 | B/I | | | | | — |
| FB-RECOG-13 | B/I | | | | | OFN, DYAD, RRF |
| FB-RECOG-14 | B/S,F | | | | | — |
| FB-RECOG-15 | B/I | | | | | DYAD |
| FB-RECOG-16 | B/Y | | | | | DYAD, RRF, OFN |
| FB-RECOG-17 | B/Y | | | | | RRF, RER, OFN |
| FB-RECOG-18 | B/E | | | | | DYAD |
| FB-RECOG-19 | B/E (optional) | | | | | — |
| FB-RECOG-20 | B/Y | | | | | PI |
| FC-RECOG-21 | C/S | | | | | NUMGEN, DYAD |
| FC-RECOG-22 | C/S | | | | | NUMGEN |
| FC-RECOG-23 | C/S | | | | | GEN |
| FC-RECOG-24 | C/S | | | | | RRF |

---

## 4. Key map

| final | [C] | [G] |
|---|---|---|
| FA-RECOG-01 | FA-01 | FA-01 support with staging; IRR-03 |
| FA-RECOG-02 | FA-02 | support |
| FA-RECOG-03 | FA-03 | revised (§2.1) |
| FA-RECOG-04 | FA-04 | support |
| FA-RECOG-05 | FA-05 | receipt boundary |
| FA-RECOG-06 | FA-06 | successor scope |
| FA-RECOG-07 | FA-07 | access limit |
| FA-RECOG-08 | — | IRR-01 |
| FA-RECOG-09 | — | IRR-02 |
| FB-RECOG-10 | FB-08 | support |
| FB-RECOG-11 | FB-09 | claim-level audit |
| FB-RECOG-12 | FB-10 | narrowing accepted (§2.3) |
| FB-RECOG-13 | FB-11 | owner decision |
| FB-RECOG-14 | FB-12 | verified; IRR-04 rounding |
| FB-RECOG-15 | FB-13 | IRR-04 L457 |
| FB-RECOG-16 | FB-14 | revised (§2.2) |
| FB-RECOG-17 | FB-15 | support |
| FB-RECOG-18 | FB-16 | narrow |
| FB-RECOG-19 | FB-17 | optional |
| FB-RECOG-20 | FB-18 | inventory |
| FC-RECOG-21 | FC-19 | written proof (§5) |
| FC-RECOG-22 | FC-20 | conditional |
| FC-RECOG-23 | FC-21 | conditional |
| FC-RECOG-24 | FC-22 | scoped |

Totals: Tier A 9, Tier B 11, Tier C 4; 4 routed items.
