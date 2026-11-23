# N-5A-S1 Long-Horizon Correction — Finite-Horizon Alias and Nonlinear Phase Slip

**Memo ID:** `NG_N5AS1_LONG_HORIZON_CORRECTION_v1`  
**Date:** 2026-08-28  
**Corrects:** `NG_N5AS1_SECTION_SEARCH_v1` / `RTG_NUMBER_GENESIS_DSN_v1.7`  
**Status:** `[COR]` to the v1.7 gate-5 verdict; N-5A-S1 returns to ACTIVE candidate status.  
**Artifacts:** `ng_n5a_s1_long_horizon_recheck_v1.py` / `.log`

## 1. What survives from the original run

The original 240-step exact-map run is reproducible: for the small seed `(rho,eta)=(0.01,0.004)` and the section `Theta=0`, the observed return-gap set is `{6}`. The original short-horizon output is therefore not a coding error.

## 2. Decisive long-horizon recheck

The same exact primitive map was re-run at 60 decimal digits through the first rare slip. For section `Theta=0`, the first non-6 return occurs at primitive step

`33229`

with a **7-step gap**. Immediately before that crossing,

`Q_true = 5.34427576108541615961463636929e-5`,

which is **smaller** than the starting value

`Q_0 = 7.6e-5`.

Thus the non-constant return word occurs deeper in the contracting small-amplitude regime, not in the large-amplitude exploratory regime.

A separate 200,000-step 12-section sweep `Theta_0=2 pi k/12` on the same exact map gives the gap set `{6,7}` for all twelve tested sections. The first 7-step slips occur between primitive steps 33,229 and 97,791 depending on section.

Therefore:

- the pre-registered prediction `HYP-N5AS1-GAP` (“the return-gap word becomes the constant word 6 on the contracting tube”) is **FALSIFIED**;
- gate 5 is **not failed** by the section-crossing candidate;
- the numerical evidence instead falsifies the fixed-block identity `B=T^m` on the audited orbit, because one and the same event stream realizes both 6- and 7-step primitive return gaps;
- gates 1–4 remain to be certified before N-5A can close.

## 3. Why the short run aliased the dynamics

The Dyadic owner already contains the six-step Birkhoff/ISP phase shear

`Theta_(m+1) = Theta_m - tau Q_m + O(Q_m^2)`,  
`tau = 2 sqrt(3)/3 > 0`,

together with the asymptotic radial backbone `Q_m ~ 1/(m+kappa)`.

Hence the leading phase defect accumulated over six-step blocks behaves schematically as

`sum_m tau Q_m ~ tau log(m+kappa)`,

whereas `sum Q_m^2` is summable. The nonlinear angular defect is therefore not expected to freeze merely because the instantaneous rotation tends to the rational linear value `1/6`. It can accumulate slowly and produce rare phase slips at ever longer horizons.

This is the correct mechanism candidate for the observed 7-step returns. Turning that mechanism into a theorem about infinitely many slips or every transverse section still requires a dedicated bridge proof from the six-step phase law to the primitive crossing word.

## 4. Correction to the “rational-rotation obstruction”

The v1.7 statement

> “exactly rational limiting rotation number p/q gives every transverse section a constant return gap q”

is not an admissible theorem. A rational **limiting** rotation does not make the nonlinear map an exact rigid rational rotation at finite amplitude. The exact-map counterexample above already refutes the asserted consequence in the present RTG realization.

Accordingly, `NUMGEN-ART-ROTNUM-OBSTRUCTION` is **retracted in its v1.7 form**.

Replacement candidate:

**`NUMGEN-CAND-N5AS1-LOGSLIP` — nonlinear logarithmic phase-slip mechanism.**

The order-6 linearization fixes the limiting rational angle, but the nonzero nonlinear phase shear combined with slow `Q_m ~ 1/m` contraction can accumulate without bound and generate sparse non-6 section returns. Current status: `[CAND]` with strong `[NUM]` support and an owner-source `[ALG]` mechanism; not yet a theorem.

## 5. Programme consequence

The N-4/N-5A coupling is **not** established by this candidate. A non-fixed section-crossing return word already occurs numerically inside the contracting local regime. N-4 may still be needed for globality or stronger recurrence classes, but it is no longer a prerequisite merely to escape `T^6` re-blocking.

The next N-5A-S1 work is therefore gates 1–4:

1. certify the section event predicate as relational/gauge-admissible;
2. prove repeatability (ideally infinitely many crossings, not a finite numerical horizon);
3. certify co-realization with Track-A on one declared domain;
4. use N-2-ORD reachability as the common event order;
5. retain the long-horizon result as gate-5 numerical non-relabeling evidence while seeking an ALG proof.

## 6. Epistemic verdict

`[COR]` **v1.7 gate-5 negative closure retracted.**  
`[NUM]` **Fixed-block relabeling is falsified on the audited exact-map orbit.**  
`[CAND]` **Nonlinear logarithmic phase-slip mechanism registered.**  
`[OPEN]` **N-5A-S1 remains active; N-5A remains open.**
