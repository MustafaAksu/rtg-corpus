# Atlas advisory — Number Genesis v1.20.8 → next edition (pass 1 of 2)

**Date:** 25 October 2026. **From:** Claude (atlas owner). **To:** the PI and the Number Genesis owner session(s). **Status:** advisory; the NUMGEN owner and the PI decide every row. Nothing here changes a document. A second, independent pass (ChatGPT, blind) follows; the two are reconciled before any edit.
**Object:** `dsn/RTG_NUMBER_GENESIS_DSN.md` v1.20.8, tag `numgen-v1.20.8`, SHA-256 `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e` (= file at `main` `36c9122`), adopted 21 Oct 2026 under Methodology v1.3; 3,412 lines. Line numbers are at that hash.
**Basis:** atlas v0.5 (`atlas-v0.5`) H4, H5, H8 and the D2/D5 rows NUMGEN.N-S1, N-A, N-B, N-D, N-E, N-L1–L7, N-SC1, N-R1, N-R2, N-C, N-F, N-C1, N-D1, N-G1, N-T1–T3, N-Q*; RECOG v0.3.24, DYAD v6.4.22, GEN v2.9, Programme v1.3 §7.2 (IF12, IF13, IF14, IF24, IF27), OFN v0.10 §11 at their tags; Methodology v1.4 §§1.1, 3.4, 12, 13.6–13.9. Every atlas row below was re-read at `numgen-v1.20.8`; one is partly withdrawn (NC-16). No certificate was rerun.

## 0. Why now

NUMGEN v1.20.8 was a maintenance release (consumer synchronization, RID allocation for RECOG's A1a request, interface definition; no theorem-level change). Since then RECOG adopted v0.3.23 and v0.3.24: the explicit-U existence theorem `RECOG-THM-A1A-PHASE-EXISTENCE-U` (C_D^ext without R9/INF-1) and the slip-schedule theorem `RECOG-THM-A1B-SLIP-SCHEDULE-U` (gap alphabet {6,7}, s(M)=(3τ/π)log M+O(1), M_{k+1}/M_k → e^{π/(3τ)}, digamma schedule) — results that NUMGEN holds in existential or RESULT-grade form on its own tube, now proved by a consumer on an explicit Dyadic tube, with GAP-LOCK/INF-1 custody explicitly left with NUMGEN ("NUMGEN is informed", RECOG §6.13b line 740). Dyadic adopted the row-A theorem NUMGEN said it would import "in a NUMGEN edition after v1.20.8" (§6.6 line 2196; §9.1 N15 line 2750). Programme v1.3 records IF27 ("RECOG's explicit-domain A1a theorems are not listed by NUMGEN as inputs"). This is that edition's agenda.

## 1. Proposed outcome and release contract

One NUMGEN edition (v1.21 if the owner migrates to Methodology v1.4 with stage-2 compaction — recommended, since the Changelog and three Result/Change Notes are 518 lines and the header carries a long pointer-validation narrative; v1.20.9 if corrections only), built as RECOG v0.3.24 and Genesis v2.9 were: stage 1 (exact-once corrections, assertion-gated script, checker with negative controls, frozen intermediate hash), stage 2 (layout-only compaction, `tools/check_compaction.py`, movement map), publication transform (status lines only), release record, PI adoption, merge commit, annotated tag. Two independent advisories reconciled in `records/numgen/`; owner dispositions per row.

Labels: **I** inconsistency inside the live text · **S** stale against an adopted source · **Y** RID/identifier · **E** editorial/clarity · **G** governance/methodology.

## 2. Findings register

### 2.1 Tier A — interfaces and live-text state

**NA-01 | S | RECOG v0.3.23/v0.3.24 results on NUMGEN's own objects are not recorded (atlas N-L5, N-SC1, N-B; Programme IF27).** NUMGEN's latest RECOG pin is v0.3.22 (§9.1 line 2753 A1a RID request; §9.2 line 2824 consumer row at v0.3.5). Since then: (i) `RECOG-THM-A1A-PHASE-EXISTENCE-U` proves C_D^ext on the explicit Dyadic tube U={0<Q₀≤1/625} without R9 or INF-1, using `DYAD-THM-LPHASE-ROWA-REMAINDER`; (ii) `RECOG-THM-A1B-SLIP-SCHEDULE-U` proves on U that every gap is 6 or 7, s(M)=(3τ/π)log M+O(1), and M_{k+1}/M_k → e^{π/(3τ)} — the quantity NUMGEN states as `[RESULT] [from: ALG]` on its existential tube (§6.6 lines 2269–2307: (1/k)log M_k^(phys) → π/(3τ); M_{k+1}/M_k → exp(π/(3τ)) = exp(√3π/6)); (iii) RECOG states that GAP-LOCK 1–3 and INF-1 remain NUMGEN's and that no custody changes. Owner: add §9.1 rows recording the two RECOG theorems as **available explicit-U inputs / consumer-side confirmations** (received, scope U, no custody change), and at §6.6 one sentence per affected statement: "explicit-U version: RECOG-THM-… (consumer theorem on DYAD-THM-PRIM-CTR's tube); NUMGEN's existential statement unchanged". No regrading is asked; the owner may choose to import by RID or only to record.

**NA-02 | S | The deferred L-PHASE import (atlas N-A, DYAD.X10).** §6.6 line 2196 `[OPEN] [target: THM]` "L-PHASE explicit constant — Dyadic row-A theorem adopted upstream; NUMGEN import deferred"; §9.1 N15 (line 2750): "RECEIVED … import by RID deferred to a NUMGEN edition after v1.20.8". The I1–I5 interface (W ≡ 𝓛, lift ≡ PRIMITIVE-LIFT, q_m ≡ Q_m, lag sign, base points in U) is already stated. Owner: execute the import of `DYAD-THM-LPHASE-ROWA-REMAINDER` at its THM grade on U (block base points), close or rescope the §6.6 OPEN item, and record the resulting explicit constant C on U beside the existential one. Dyadic's governing edition is v6.4.22 (NUMGEN pins v6.4.18; v6.4.19 added the row-A theorem; v6.4.20–22 added the smooth embedding/chart theorems, not NUMGEN inputs) — a claim-level repin for this row only.

**NA-03 | I/E | "U", "U_T" denote two tubes in one document (atlas N-S1; H8 advice).** §6.2–§6.9 use U/U_T for the existential L1 tube (line 1055: U_T := U ∪ T(U) ∪ … ∪ T⁵(U), with U the existential radius of the N-1 closure, line 1125 "local and existential in the L1 radius"); §6.6 L-PHASE and the RECOG rows use U={0<Q_true≤1/625}, the explicit Dyadic tube; "U" is also the L1 coordinate √3ρ/2. RECOG had to write "U_NUMGEN" to disambiguate. Owner: one notation decision — e.g. U_NG / U_NG,T for the existential tube and U, U_T for the explicit Dyadic tube (matching DYAD/RECOG) — applied at every theorem scope that says "U_T" without a section.

**NA-04 | S | Stale pointers in the live text (atlas N-F; companions).** §7 N-3 item 7 (line 2650) pins the q=4,(0,3) cascade closure to "Dyadic v6.4.10" while the body uses v6.4.18 (the v1.20.7 changelog, line 2978, says STOP-03 fixed exactly this to v6.4.9 → the live line still reads v6.4.10 — check which is meant); §9.1 header (line 2729) "Validation state carried into v1.19"; the header pointer-validation note (line 11) still narrates v1.3/v1.17 checks and reports "DZT v0.17" as the frozen DZT state (line 2721 `[PROVENANCE]`) while the governing DZT edition is `dzt-v0.8` (different numbering — the owner should say which document "DZT v0.17" names); companion list (line 9) names Programme v1.2 (→ v1.3), Genesis v2.8.9 (→ v2.9; NUMGEN's Genesis use is companion-level), Dyadic v6.4.18 (consumer pin, fine); Methodology line "Programme v1.2 SG-PROG-4" (line 12) → Programme v1.3 (SG-PROG-4 exists there with the same meaning, §8 line 474). Under v1.4 §1.1 item 4 each use carries the pin actually used; narrative validation history goes to the release record.

**NA-05 | I/E | N-1 tree vs N-1A0/N-1A1 status (atlas N-T2).** §6.2 tree (line 437) "N-1C … [CLOSED local dyad by L1]" while N-1A0 is ACTIVE and N-1A1 PARTIAL — consistent only as "closed on the existential tube, open abstractly"; the scope word is missing at the N-1A0/N-1A1 headers. One clause each.

**NA-06 | G/E | Superseded formulations retained in live §6.6 (atlas N-T1; v1.4 §1.1).** Line 2081 `[COR] [historical formulation — superseded by v1.11/v1.16 closures]` `NUMGEN-CAND-N5AS1-LOGSLIP` block and the "predicted asymptotic slip law" passages; N-5A-S1 header "[COR: v1.7 verdict]"; §9.2 NG_C7C_M_DESIGN_v1 historical statements ("typed by B suffices", "associativity free"). Under v1.4 the live section states the current law once (lines 2269–2307) and the history lives at the tag; the retained blocks move to Appendix B/changelog or are cut, with the compact Appendix entry pointing at `numgen-v1.20.8`.

### 2.2 Tier B — RIDs, grades, evidence, methodology

**NB-07 | Y | RID vacuum (atlas N-R1, H4).** Only 6 `[RID: NUMGEN-…]` declarations exist (N5AS1 DEFECT, PRIMITIVE-LIFT, INF1, L-BACKBONE, L-MONO, L-PHASE) plus module keys (`NUMGEN-OPEN-N5`, `-N5-COMM-BD`, …; 42 distinct `NUMGEN-*` strings in all). Without RIDs: the N-3C+ module (projector, first-nonlinear cyclic average, support, reachable charge, OPEN-9 boundary, Bessel), **GAP-LOCK Lemmas 1–3** (RECOG cites them as "no RID"; RECOG §7 line 167), INF-2, gates 1/3/4, the section identity, N5-C1–C6, N5-PHYS-1, C7A, C7B-T1–T4, DISC-1/2, the ten-label bound, C7C-0, M-1A, M-1B, M2-1, Census-1, P3 injectivity, ORD-1–4, T4, the explicit-domain corollaries. Owner: register RIDs first for what consumers cite (GAP-LOCK 1–3, L1, N1C, the cyclic-average theorem — GEN and RECOG both route G₂=0 through it, atlas N-L6/R-L2), then the rest; Methodology v1.4 §4 namespace `NUMGEN`.

**NB-08 | Y/G | RID type ≠ status (atlas N-R2).** CLOSED results sit under OPEN-type RIDs (N1, N2, N2-ORDER, N1A2, N5A, N5AS1-SECTION, N5AS1-INF, REC-HOL-OPERATOR, TWO-FIVES-ORBIT-CARDINAL, TWO-FIVES-REBLOCK); `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` is THM-typed but graded `[RESULT] [from: ALG]`; N1A2 heads an ALG closure; `N1C-DYAD-RADIAL` and `OPEN-N1C` both head the N-1C closure. Methodology v1.4 §5 keeps OPEN records with question/criterion/status; a closed result gets its own result RID and the OPEN record points to it. Owner's naming decision; no regrading implied.

**NB-09 | G | Evidence state at the claim (atlas N-D1).** In-ledger proofs without separate certificate: N5-C1–C4, C5, N5-PHYS-1, C7A (§9.2 "no separate external certificate yet"), P3 injectivity, NG-7A abelian, explicit-domain corollaries, N-1A2. Under v1.4 §12 declare the evidence state (written proof in ledger / certificate / replayed) at each claim; nothing is downgraded by the declaration.

**NB-10 | G | Methodology v1.4 migration.** Header "DSN Methodology: v1.3"; 3,412 lines; Changelog 518 lines (v0.1–v1.20.8 with detailed entries) plus three legacy notes ("v0.3 Change Note", "v1.0 Result Note", "v0.9 Result Note") after it; header carries a status summary, pointer-validation narrative and methodology notes that v1.4 moves to the release record. Strength to keep: `[RESULT]` pairing is already v1.4-conformant (193 of 194 occurrences carry `[from:]`). Owner/PI: v1.21 with stage-2 compaction (Appendix A one entry per edition; legacy notes to the tag) or v1.20.9 corrections-only.

**NB-11 | E | Changelog-only facts (atlas N-T3).** sup|r|/Q^{3/2}∈[1.3449,1.3565] (v1.10), first-slip pre-transition amplitude 5.3443×10⁻⁵, Δη_future digits appear only in the changelog. Either live (at their §6.6 statements, with evidence pointer) or dropped from the compact Appendix A.

### 2.3 Tier C — cross-owner identifications (atlas `~` rows, for the owner to confirm or deny)

**NC-12 | E | Clock ratio e^{π/(3τ)} = λ_DSI^{1/6} (atlas N-L7).** NUMGEN types it a representation-level diagnostic (SG-NG-23, lines 262/2104; value 2.476632… at lines 2090, 2277, 3110); RECOG exports it as a universal clock ratio under SG-R10; RECOG v0.3.24 now has it as the THM consequence M_{k+1}/M_k → e^{π/(3τ)} on U. Same number, three scope readings, no cross-citation. One sentence at SG-NG-23 naming the RECOG result and the scope difference.

**NC-13 | E | Dyadic identities used but unrecorded (atlas N-L1, N-L2, N-L3).** L1 is the existential form of `DYAD-THM-PRIM-CTR`; the atlas checked ΔQ₅ ≡ P₅ exactly (sympy) and the DYAD ceiling 1.6931 vs NUMGEN C5=2.14998; (U,V)=(√3ρ/2, η−ρ/2) is the ISP U+iV with φ=Θ−π/6; the relay identities are `DYAD-ALG-Q-INVARIANT-FORM`, `-TAU-DETB`, `-CUBIC-PARABOLIC` (NUMGEN §9.2 "not claimed in NG" without RIDs). Owner: cite the RIDs; decide whether to state the degree-5 identity and the explicit ε_L1 (Q≤1/400) as imported facts.

**NC-14 | E | φ* comparison with RECOG's C_D^ext (atlas N-D, N-L4; H5).** `DYAD-CAND-PHISTAR-ENTRY-PHASE` is not an owner RID; `RECOG-THM-A1A-CD-IDENTIFICATION` gives C_D^ext(x₀)=τlog Q₀−M_W(x₀) on U, so Q₀→λQ₀ at fixed Θ₀ shifts C_D by τln λ+O(√Q₀) — the NG-0R-COV target (§6.1a line 394 pre-registration pin). NUMGEN's §8 says a "separate comparison proof" is needed. Owner: either run it (observable, gauge, start dependence, overlap domain) or state that φ* and C_D^ext are distinct objects until then.

**NC-15 | E | Cyclic-average theorem → Genesis chrono-protection (atlas N-L6; GEN custody).** NUMGEN's first-nonlinear cyclic-average theorem with vector charge a−b−1 mod 6 gives G₂=0 for L=diag(A,A,A) — Genesis's `GEN-ART-G2-CHRONO`, whose proof source Genesis v2.9 records as custody (a) missing ([custody-A]); RECOG's `RECOG-ALG-LEADING-RETURN-EQUIVARIANCE` gives the same route (Genesis owner disposition, G2-CHRONO row). Owner (with GEN): register the theorem's RID (NB-07) so Genesis can cite an independent route — an independent contribution, not a recovery of Genesis's original source.

**NC-16 | — | Atlas row partly withdrawn: N-G1.** The atlas said NUMGEN §9.2 (line 2824, "RECOG … cross-references GAP-LOCK Lemma 3 at heuristic grade") is stale because RECOG uses Lemma 3 at ALG. Re-read: RECOG §7 (line 167) tags its GAP-LOCK Lemma 3 import "[HEUR cross-reference …]" while `RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE` (line 977) uses it in an ALG identity. NUMGEN's sentence is therefore correct about RECOG's §7 row; the grade tension is RECOG-internal and goes to the RECOG owner, not to NUMGEN. The atlas row will be reworded at the next refresh.

**NC-17 | E | q* branch split (atlas N-Q*).** `DYAD-THM-OPEN18` (DYAD §6, line 600): "q=q_* is the branch split" on Γ₃, Γ₄; NUMGEN q* = 0.3156258836… (line 912) on the canonical family (0,q). Plausibly the same q*; neither document cites the other. Owner: confirm or deny with one line.

**NC-18 | E | Minor (atlas N-C, N-C1).** Tube bound 0.0665 valid but loose (sharp 0.05427, atlas-checked); NUMGEN's PRIM-CTR and Q403 import values agree with DYAD; q_m (NUMGEN) ≡ Q_m (DYAD) while q is also |z|² in DYAD/RECOG — a notation guard sentence.

**NC-19 | E | Consumers and interface register (Programme v1.3 §7.2).** IF12 (DYAD → NUMGEN, pin v6.4.18), IF13 (TDRG → NUMGEN, v2.12.13), IF14 (NUMGEN → RECOG by RID at v1.20.8), IF24 (NUMGEN → OFN feedback, recorded import in OFN §11), IF27 (NUMGEN records RECOG as consumer). A short "Consumers" block in §9 (RECOG with its pins; OFN §11 rows that import NUMGEN) would let the Programme register and the future notice structure read from the owner.

### 2.4 Routed, no NUMGEN edit

- RECOG: the HEUR/ALG grade tension of the GAP-LOCK Lemma 3 import (NC-16) → RECOG owner.
- Dyadic: `DYAD-CAND-PHISTAR-ENTRY-PHASE` classification stands; DYAD-THM-OPEN18 ↔ q* (NC-17) needs only a cross-citation on whichever side the owners choose.
- Genesis: G2-CHRONO custody stays (a) missing until an original source is placed; an independent NUMGEN/RECOG route is a new proof, not recovery.
- Atlas: after the next NUMGEN edition, refresh D2/D5 NUMGEN nodes, retire the dispositioned N-rows, reword N-G1, rename the tube node if NA-03 is adopted, update H4/H5/H8.

## 3. Owner disposition table (to be filled by the NUMGEN owner; PI decides)

| Key | Tier | Proposed | Owner disposition | Note |
|---|---|---|---|---|
| NA-01 | A | record RECOG A1a/A1b explicit-U theorems as inputs/confirmations; no custody change | | IF27 |
| NA-02 | A | execute the L-PHASE row-A import; close/rescope §6.6 OPEN | | pin v6.4.19+ for this row |
| NA-03 | A | one tube notation (existential vs explicit) | | H8 advice |
| NA-04 | A | stale pointers (v6.4.10/v6.4.9, v1.19, DZT v0.17, Programme v1.2, Genesis v2.8.9) | | |
| NA-05 | A | scope words at N-1A0/N-1A1 | | |
| NA-06 | A | superseded §6.6 blocks → history | | v1.4 §1.1 |
| NB-07 | B | RIDs, consumer-cited first (GAP-LOCK 1–3, cyclic average) | | H4 |
| NB-08 | B | result RIDs for CLOSED items under OPEN keys | | |
| NB-09 | B | evidence state at each claim | | |
| NB-10 | B | v1.21 with v1.4 migration, or v1.20.9 | | PI Q1 |
| NB-11 | B | changelog-only facts live or dropped | | |
| NC-12 | C | SG-NG-23 cross-citation to RECOG clock ratio | | |
| NC-13 | C | Dyadic identity RIDs cited | | |
| NC-14 | C | φ* vs C_D^ext: run the comparison or declare distinct | | |
| NC-15 | C | cyclic-average RID for Genesis's independent route | | with GEN |
| NC-16 | — | atlas row N-G1 partly withdrawn; RECOG-side item | | no NUMGEN edit |
| NC-17 | C | q* cross-citation | | with DYAD |
| NC-18 | C | notation guard q_m ≡ Q_m; tube bound note | | optional |
| NC-19 | C | Consumers block in §9 | | notice structure |

## 4. Open questions for the PI

1. **Edition type:** v1.21 (Methodology v1.4 migration, stage 2 compaction of the 518-line changelog and legacy notes) or v1.20.9 (corrections only)?
2. **Who builds:** the NUMGEN owner session builds stage 1 (atlas and the other co-owner review), as with Genesis?
3. **NA-01 depth:** record RECOG's explicit-U theorems as consumer confirmations only, or import them by RID into §6.6 (which would make NUMGEN a consumer of RECOG for those statements — a custody question the owners should answer explicitly)?
4. **NA-03:** is the tube renaming acceptable to the owner (it touches many theorem scopes but no content)?

## 5. PI decisions

_(to be filled)_
