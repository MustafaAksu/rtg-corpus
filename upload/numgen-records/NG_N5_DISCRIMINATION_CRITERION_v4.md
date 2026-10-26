# N-5 Discrimination v4 — D1 Relocated, Same-Realization Guard, Frozen DISC-1D

**Memo ID:** `NG_N5_DISCRIMINATION_CRITERION_v4` · supersedes `_v3`
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.15` (sha256 `d56440c6…3375`, verified)
**Date:** 2026-08-31 · **Auditor:** Claude
**Artifact:** `ng_n5_discrimination_identity_cert_v4.py` / `.log` — identity certificate; exit code covers **T1a, T1b, T2, T3, T4, P1a and nothing else**.

---

## 1. `[COR]` — D1 removed from the certificate

Accepted without reservation. The v3 test was `sp.simplify(sp.diff(D4,m)) != 0`, which verifies only that `b a' − a b'` is not identically the zero polynomial, while the PASS line asserted a design theorem covering a same-realization quantifier, the need for two distinct deformation points, admissibility of three `k` values, dual activity at them, and the experimental structure. None of that is checkable symbolically. This is the A3/A6 category error in milder form — in the package meant to have fixed it — and the pattern is worth naming: **when a PASS string is longer than what its expression can decide, the expression is not the claim.** I will apply that test to every future assertion line.

D1 now lives here, as: **T3 + T4 + same-realization definition ⟹ D1.** The certificate header states explicitly what the exit code does not cover.

## 2. Same-realization quantifier — accepted as the definition

The correction is right and the reason is the important part. Without it, one move `k₀ → k₁` could supply stability from seed `x` and contingency from seed `y`, so `Q^dyn` would mix robustness from one orbit with sensitivity from an unrelated one. That is not a claim about the dynamics; it is a claim about the *panel*. Adopted:

> **DISC-1D same-realization guard.** Admission of `r` to `Q^dyn` requires one certified base realization `x` carrying `r` such that the continuation of that same frozen relational initial state under the declared deformation family supplies both (i) a persistence witness and (ii) a distinct contingency witness. Stability and contingency may not be assembled from different base realizations.

**D1 (memo-level, follows).** For a single tracked realization, T4 makes persistence and class-change exhaustive and exclusive at a qualifying comparison point. One move therefore yields exactly one verdict and forecloses the other, so DISC-1D needs **two distinct comparison points**, i.e. at least three `k` values counting the base.

## 3. Deformation set and pass rule — accepted, and my prescription withdrawn

`k = 3` admissible-but-unaudited, and `k = 0` retained as the legitimate zero-width boundary case rather than discarded, both accepted. The frozen set is `𝒦_DISC = {0,1,2,3}` at fixed `N = 24`, base `k = 1`.

I withdraw my v3 suggestion that `k=1→2` be designated stable and `k=1→3` contingent. Your point is decisive: that ordering is an unnecessary prediction, and an existential test over an already-frozen set is not post-hoc selection. Freezing the *comparison set and pass rule* is strictly better than freezing which member must produce which outcome.

Correspondingly, my v3 warning about needing a fallback axis is withdrawn: a seed ceasing to be dual-active at `k = 3` is that seed failing the comparison fence, not `k = 3` being inadmissible. No second axis is needed as an admissibility fallback.

## 4. Two pre-data reporting requirements I would add

Neither changes the pass rule; both protect its interpretation.

**(a) Report per-seed dual-activity counts.** A seed needs **two** qualifying comparison points to be eligible at all. If `k = 0` produces no dual-active cycles (plausible at zero band width), the effective comparison set collapses to `{2,3}` — still exactly sufficient, with zero margin. That collapse must be reported explicitly rather than silently absorbed, since it changes the test's power without changing its verdict.

**(b) Pre-register the failure-mode taxonomy.** Report the full transport map `x ↦ (r_{x,0}, r_{x,1}, r_{x,2}, r_{x,3})` over the frozen panel, because a null result has three very different readings that the pass/fail bit alone cannot distinguish:

- **No contingency anywhere** — every seed keeps its class under every admissible `k`. The label behaves like predicate multiplicity; SG-NG-26 territory, and `Q^dyn` is plausibly empty on this axis for structural reasons.
- **No stability anywhere** — every seed changes class at every comparison. This is a finding about the *deformation family*, not about `Q^dyn`: it would indicate `k`-steps are not elementary moves in the required sense, so the declared deformation structure is misdeclared and the stability half of the criterion was never testable on this axis.
- **Both present, never on the same seed** — the same-realization guard is biting. This is the genuine null result and the only one that is evidence about `Q^dyn` itself.

Fixing that taxonomy now prevents the post-hoc temptation to reinterpret the second case as the third.

## 5. Frozen state

- **DISC-1B:** original `N=24, k=1` SWAP/P3 non-`1` census; original FAIL rule unchanged.
- **DISC-1D deformation family:** fixed `N = 24`, three-node no-birth sector, canonical CONV-TICK and CONV-P3CYC, same SWAP/P3 predicates, frozen raw seed states, `k ∈ {0,1,2,3}`.
- **Base:** `k = 1`. **Same-realization guard** in force.
- A comparison point qualifies only if the cycle is dual-active there.
- **Pass:** for the same seed, `∃ k_s ∈ {0,2,3}` with `r_{x,k_s} = r`, and `∃ k_c ∈ {0,2,3}`, `k_c ≠ k_s`, with `r_{x,k_c} ≠ r` — equivalently, by T4, `|Δ_r^{(k_c)}| ∼ |b a_{x,k_c} − a b_{x,k_c}|·m → ∞`.
- If no seed meets both, **DISC-1D fails on the `k` axis.** No further axis is introduced after seeing the data.
- **Reporting:** per-seed dual-activity counts and the full transport map, per §4.

## 6. Ledger

C1–C4 CLOSED; C5-SYN-13 mathematical periodic control; T2 periodicity triviality; T3 corrected (closed finite invariant sector); T4 class-change ⟺ loss of boundedness; C6 unchanged and discriminating; N5-PHYS-1 first physical positive control, `1 ∈ Q^bd`; C7A unchanged; `Q^dyn` empty; DISC-1B falsifiable non-`1` census; DISC-1D dynamic gate as frozen above; C7C downstream of `Q^dyn`.
