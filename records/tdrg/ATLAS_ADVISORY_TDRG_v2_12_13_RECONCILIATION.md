# Discrete Genesis (TDR-G) v2.12.13 — reconciliation of the two independent atlas advisories

**Date:** 27 October 2026. **By:** Claude, atlas owner (advises; does not decide). **To:** the PI; the TDR-G co-owner sessions.
**Inputs.** Pass 1: `records/tdrg/ATLAS_ADVISORY_TDRG_v2_12_13.md` (PR #82, atlas owner; TA-01…08, TB-09…13, TC-14…18; atlas check `evidence/atlas/tdrg/atlas_tdrg_orientation_covariance_check.py`). Pass 2: `records/tdrg/ATLAS_ADVISORY_TDRG_v2_12_13_INDEPENDENT_CHATGPT.md` (PR #84, branch `chatgpt/tdrg-independent-pass`, commit `c3064ac`, file SHA-256 `861f4196…`; TG13-I01…I12), written blind — PR #82 not read. Both against `tdrg-v2.12.13` (`aa232643…053f`).
**Status:** record. The merged list (§3) is what the TDR-G co-owners disposition; nothing here grades a TDR-G claim.

## 1. Verdict

**No disagreement.** The two passes find the same P0 (the path-orientation selector is not node-relabelling covariant on S=0 ∧ δ_{v_n}−δ_{v_1}≡N/2), the same two mathematical wording errors (LEM-RETRIG at d=0; LEM-SPECCONS "equivalently"), the same scaling/grade, RID, pin, custody and interface items. The passes are complementary on the P0: pass 2 states the obstruction and its acceptance criteria (exact covariance group; a no-go for a selector built on (S,E) alone; a declared policy); pass 1 supplies the no-go and the existence result — on the degenerate stratum the pair (S,E) is reversal-invariant (C1, exhaustive at N=24), while the centre-relative advances never are (C2), so for P_3 a covariant selector exists on the whole stratum and never ties — together with the witness and census counts (C3, C4). Pass 2 adds four points pass 1 lacks (§2, items marked ChatGPT-only); pass 1 adds six (atlas-only). Two statements are sharpened by the reconciliation (§2.3).

## 2. Correspondence

### 2.1 Items in both passes

| Pass 1 | Pass 2 | Agreement |
|---|---|---|
| TA-01 (P0) | TG13-I01 (P0) | Same obstruction, same cause (`sc_N(N/2) = sc_N(−N/2)`; order-two element has no intrinsic sign), same reading of Appendix B's "[FAIL] arbitrary path label fallback" and of the v18 ID-sorted listing as a presentation convention. Pass 2's criteria (i)–(iii) are met by pass 1 §2: (ii) C1 is the no-go for any selector using only (S,E); (iii) options (a) covariant G-rule / (b) extend the balanced tie to E≡N/2 are the covariant policies; (c) node identity as physical is rejected by both. Pass 2's caution "the obstruction does not prove that no covariant completion exists" is confirmed constructively by C2. |
| TA-08, TA-01 | TG13-I02 | The §6.12 "relabeling-covariance check: PASS" tests the ±d mirror on the inspected families, not node permutation of the selector; qualify it and add the failing fixture. Both keep BIND3-CYCLE-N24K1 numbers unchanged pending a scoped sensitivity audit; pass 1's census bounds the exposure (4.9 % of k=1 states, 77 of 9,800 eventual cycles). |
| TC-14 (P0) | TG13-I03 | Same evidential separation (per-event failure / exposed witness records / existential label projection robust / other panels unreviewed); same HOLD on C7C-M4 until the owner rules; DISC-1 not covered by the DISC-2 audit. Pass 2's "verify that the 96 unexposed witnesses are unchanged under the corrected rule" holds by construction for any rule that differs from v18 only on the degenerate stratum (an unexposed orbit never enters it), and pass 1's C3 confirms it numerically for the inert, reverse and G rules (changes 20 / 10 / 12, all among the 40 exposed). |
| TA-05 | TG13-I04 | d=0 is a fixed point (least period 1), not an exact period-2 orbit; "period divides two / retrigger on every tick" with least period 2 only for (ε−d,−d) ≠ (ε,d). Pass 2 adds the d ≡ N/2 aliasing (d = −d); note that \|N/2\|_c = N/2 > 2k ≥ \|d\|_c for k < N/6, so it lies outside the threshold and is a wording point only. |
| TA-06 | TG13-I05 | "equivalently" → "therefore, in particular" (the \|d\|_c multiset determines the gcd multiset, not conversely; N=24 magnitudes 1 and 5 share gcd 1). |
| TA-04 | TG13-I06 | Range-tag α (full-range composite −0.869 vs 480–1440 ≈ −0.730); drop or archive the superseded χ exponent 0.836 from the live consistency sentence; crystallization HEUR only; no refit unless the owner picks a new headline. |
| TB-09, TB-11 | TG13-I08 | Core definitions/theorems/lemmas/BIND3 results lack claim RIDs; the 34 `[RID: …]` strings are OPEN/ART/EXPORT keys only (pass 1 census; pass 2 declined to count); evidence custody states held / placed / replayed / missing with hashes; no certificate invention. |
| TB-10, TB-13 | TG13-I09 | Methodology v1.2 → v1.4 two-stage successor (stage 1 corrections under an assertion-gated log; stage 2 history relocation with a movement map); companions Programme v1.1 / OFN v0.6 stale as "governing" while claim-specific pins may stay; one predecessor, one footer. |
| TB-10, TC-15, TC-18 | TG13-I10 | §7 Imports / Exports / Consumers / Pins with received / statement accepted / adopted-use states; OFN Finding A stays OFN-owned until TDR-G accepts custody; NUMGEN C7C-M4 HOLD; AZ owns its graph algebra; Programme IF rows route, they do not transfer results. |

### 2.2 Items in one pass only (all accepted into the merged list)

**ChatGPT-only.**
- **TG13-I07** — front-of-DSN closure alignment: §1 status summary says the TDR-24 chain must close without acknowledging D/F closed and A/B/C open; §5 calls the analytic ψ-intensiveness explanation "TDR-24F, OPEN" while §1 calls F "resolved `[NUM strong]`" (numerical mechanism vs analytic constants). One current-state rewrite of §1/§2/§5.
- **TG13-I11** — OFN Finding A (common token shift, fixed component map, residual 2c=0) and the P2 endpoint relabelling are two different covariance questions; disposition them separately (XFER-O08-01; REQ-O09-05).
- **TG13-I12** — AZ's static-ℤ_N 4\|q Hashimoto signal is substrate geometry, disqualified as a TDR-G dynamical bridge candidate; it must not be re-read as support for the policy N-scaling; `bound_symmetric` stays OPEN TDR-19 as a selected law.
- The d ≡ N/2 aliasing remark under I04.

**Atlas-only.**
- **TA-02** — `signed_centered` and `signed_defect_error` are undefined in the DSN; the (−N/2, N/2] convention that creates the degeneracy is nowhere stated.
- **TA-03** — no relabelling-covariance guard among SG-1…13; Appendix B calls label fallback a "background-independence violation" without a guard naming the requirement; the global token shift's status is likewise undeclared (ties to I11).
- **TA-07** — cross-branch residues quoted in stale form (K₃ 96:1 as settled vs TRIAD v1.6.1 bookkeeping; App. C TDR-T3 safe wedge and R0 x*, −32r⁴ from the withdrawn T-6 chain).
- **TB-12** — compound grades `[ALG/NUM]`, `[ALG / NUM strong]`, `[NUM / mixed]`, `[ALG structure]` to unpack (Methodology v1.4 §8.4); the legacy-alias table is dead.
- **TC-16** — `AZ-ALG-ANTIPODAL-LOWORDER` is the same arithmetic as narrow-band exclusion and strictly extends it; cross-cite once the exclusion theorem has a RID (also resolves AZ's phantom `TDRG-ZN-STATE`).
- **TC-17** — Programme v1.2 §6 listed "state/gauge conventions, the antipodal path tie, counting observables, statistical/rank interpretation" as TDR-G owner-review tasks; v1.3 §6.4 dropped the sentence; the tasks belong in TDR-G §2 (atlas D5.X1 cites "PROG §6.4" — stale; atlas-side fix in v0.7).
- The atlas check itself (C1–C4): numbers for the owner's "targeted witness-effect table" and the census bound for the rerun question.

### 2.3 Sharpened by the reconciliation

- Pass 1 TC-15 said OFN's REQ-O09-05 and the P2 endpoint policy "are the same question"; pass 2 I11 is right that they are distinct covariance questions (token shift vs node relabelling). The merged list keeps them as two disposition entries (TA-03 names both guards).
- Pass 1 §2 option (a) proposes the G-rule for P_3 and a palindromic-tie fallback for P_n; pass 2's criterion (i) "exact intended covariance group" applies to whichever option the owner chooses: the guard (TA-03) must name the group (node permutations; optionally joint phase/token transformations) before the selector is amended.

## 3. Merged list for the TDR-G co-owners (disposition one row each)

| Key | Prio | Item | Source |
|---|---|---|---|
| TA-01 / I01 | P0 | Orientation selector not covariant on S=0 ∧ δ_{v_n}−δ_{v_1}≡N/2; declare the stratum; choose (a) covariant G-rule (P_3; palindromic tie for even n) or (b) extend the balanced tie to E≡N/2; name the covariance group; add the failing permutation fixture and a covariant-rule control; state which v2.12 certificates are touched | both |
| TA-02 | P1 | Define `signed_centered` ((−N/2, N/2]) and `signed_defect_error` in the DSN | atlas |
| TA-03 / I11 | P1 | SG-14 relabelling-covariance guard (ties only on invariant data); separate entry on the global token shift (OFN Finding A, XFER-O08-01, REQ-O09-05) | both |
| TA-08 / I02 | P1 | Qualify §6.12 "relabeling-covariance check: PASS" (±d mirror on inspected families); add the antipodal fixture; BIND3 numbers unchanged pending a scoped sensitivity audit (census bound available) | both |
| TC-14 / I03 | P0 | Disposition of `pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md` with the witness-effect table (40 exposed; 10/20/12 changes under reverse/inert/G; label set unchanged; 96 unexposed unchanged by construction); DISC-1 audit is NUMGEN's; C7C-M4 HOLD until the ruling; acknowledge `…-NUMGEN-v1-21-adopted.md` | both |
| TA-05 / I04 | P1 | LEM-RETRIG least-period wording at d=0 (and the d≡N/2 aliasing note) in §1, §6.5 and the regime table | both |
| TA-06 / I05 | P1 | LEM-SPECCONS "equivalently" → "therefore, in particular" | both |
| TA-04 / I06 | P1 | Headline exponent range/conditioning tags; retire the χ=0.836 consistency sentence; crystallization HEUR | both |
| I07 | P1 | §1/§2/§5 current-state alignment on TDR-24 D/F closed vs analytic residuals vs A/B/C | ChatGPT |
| TA-07 | P2 | Cross-branch residues (K₃ 96:1; T-6 wedge) marked historical | atlas |
| TB-09 / I08 | P1 | Claim RIDs: definitions consumed by OFN/NUMGEN first, then the §6.2 theorems, the four lemmas, the BIND3 results; no OPEN-module RID renamed | both |
| TB-11 / I08 | P1 | Evidence custody: session-held certificates and motif logs to an `upload/tdrg-records` branch (unchanged, hash-checked), cite by hash; classify the rest held / placed / replayed / missing | both |
| TB-10 / I09 / I10 | P1 | Methodology v1.4 two-stage successor; current pins (Programme v1.3, OFN v0.10, Methodology v1.4) with claim-specific historical pins retained; §7 Imports / Exports / Consumers / Pins with states | both |
| TB-12 | P2 | Unpack compound grades; drop the legacy-alias table | atlas |
| TB-13 | P2 | Internal stale: header date, footer chain, Appendix A order, TDR-24B overlays, Appendix C gate vs §2 | atlas (I09 touches it) |
| TC-16 | P2 | Cross-cite AZ-ALG-ANTIPODAL-LOWORDER; resolve AZ's phantom TDRG-ZN-STATE via the state RID | atlas |
| TC-17 | P2 | Record the dropped Programme v1.2 owner-review tasks in TDR-G §2 | atlas |
| I12 | P2 | Scope any AZ citation (4\|q signal is substrate geometry; no bridge; TDR-19 stays OPEN) | ChatGPT |

## 4. Questions for the PI

Unchanged from pass 1 §5 and consistent with pass 2 §2: **Q1** edition — v2.13 with the Methodology v1.4 migration in two stages, or v2.12.14 corrections-only first; **Q2** the TDR-G co-owner sessions build (disposition records, then stage 1/2), atlas owner row-checks, ChatGPT reviews change-focused; **Q3** scope of reruns — BIND3-CYCLE-N24K1 sensitivity and DISC annotations inside this edition under the amended rule, or `EV-NOT-RERUN` with the census bound and a later campaign; **Q4** whether the TDR-G sessions hold the session-certified scripts and motif logs for an `upload/tdrg-records` branch. The orientation choice (a)/(b) is the owner's scientific decision, not a PI question.

## 5. PI decisions (27 October 2026)

- **Q1 — staged.** TDR-G has gone unmaintained for long; it is updated in stages: a corrections-only edition first (**v2.12.14**: the merged list §3 — orientation ruling, definitions, guard, wording, grades, RIDs, pins, consumers — under Methodology v1.2 as declared, with the v1.4 rule that an edition keeps its declared methodology until migrated), then the Methodology v1.4 migration with stage-2 compaction as **v2.13** in a later cycle.
- **Q2 — roles as proposed.** The TDR-G co-owner sessions write the disposition records and build; the atlas owner row-checks and reruns; ChatGPT reviews change-focused; the PI adopts, merges and tags.
- **Q3 — reruns deferred.** No BIND3 sensitivity rerun or DISC re-annotation inside v2.12.14; the touched certificates are recorded `EV-NOT-RERUN` with the census bound (4.9 % of k=1 states, 77 of 9,800 eventual cycles) and the rerun is a later campaign.
- **Q4 — held files.** The PI holds the motif logs (and the session scripts, if present) on his machine; they go to an `upload/tdrg-records` branch unchanged, assembled with the atlas owner, and are hash-checked there.

## 6. Hand-over

`records/tdrg/TDRG_COOWNER_ENTRY_NOTE.md` (same branch) brings the TDR-G co-owners to the current state and lists what is asked of them.
