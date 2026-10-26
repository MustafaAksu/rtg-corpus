# N-5A-S1-INF — Reduction to Three Lemmas, with a Corrected Hypothesis

**Memo ID:** `NG_N5AS1_INF_REDUCTION_v1` · **RID:** `NUMGEN-OPEN-N5AS1-INF`
**Canonical base:** `RTG_NUMBER_GENESIS_DSN_v1.9.1` (sha256 `7b8545fb…54d42`, verified)
**Date:** 2026-08-28 · **Author/auditor:** Claude
**Artifacts:** `ng_n5as1_inf_reduction_cert_v1.py` / `.log` (8 assertion families, exit 0)
**Status:** N-5A-S1-INF reduced to three named lemmas; the two combination theorems are proved; **one proposed hypothesis is falsified and corrected**.

---

## 1. Sign convention, measured not assumed

With the lifted section angle `φ` built from `Θ = atan2(√3 η_wrap, 2ρ − η_wrap)`, `φ` is **increasing**, and the six-step block law reads

```
φ_{m+1} − φ_m = 2π − τ Q_m + r_m,      τ = 2√3/3.
```

The defect is a **lag**: each block advances slightly less than `2π`, so section returns are occasionally delayed by one primitive step — which is why the slips are 7s and never 5s. Worth recording, since the memo's schematic `Θ_{m+1} = Θ_m − τQ_m` sits in the opposite-orientation ISP convention and the sign must be pinned before any counting argument is written.

## 2. Material correction: INF-1's proposed remainder bound is false

The proposed hypothesis was `|r_m| ≤ C Q_m²`. **This is false for the exact map.** Measured across a 256-fold range of `Q₀`:

| `Q₀` | `sup |r|/Q²` | `sup |r|/Q^{3/2}` |
|---|---|---|
| 3.04e-4 | 77.80 | 1.3565 |
| 7.6e-5 | 154.90 | 1.3503 |
| 1.9e-5 | 309.08 | 1.3473 |
| 4.75e-6 | 617.45 | 1.3457 |
| 1.1875e-6 | 1234.18 | 1.3449 |

`sup|r|/Q²` doubles for every fourfold decrease in `Q` — it diverges as `Q → 0`. The stable exponent is **3/2**, with `C ≈ 1.35`. In hindsight this should have been expected: the certified L1 law is `ΔQ = −Q² + O(Q^{5/2})`, a relative half-power correction, and `O(Q^{3/2}) = τQ · O(Q^{1/2})` is the same half-power scale on the phase side.

**The theorem survives the correction.** INF-1 needs only `Σ|r_m| < ∞`, and with `Q_m ~ 1/m` we have `Σ Q_m^{3/2} ~ Σ m^{-3/2} < ∞`. So the corrected hypothesis is *both true and sufficient*. Had the O(Q²) form been pursued, effort would have gone into proving something false.

**Corrected INF-1 hypothesis:** `|r_m| ≤ C Q_m^{3/2}` on the declared certified domain.

## 3. The reduction — three lemmas

**L-MONO.** The per-primitive-step lifted increment lies strictly in `(0, 2π)` (measured range `[1.0371, 1.0571]` about `π/3`). *This is the same lemma already flagged as the gate-1 orientation caveat* — one lemma discharges both, which is worth knowing before scheduling. Route: fixed rotation sense from the `exp(±iπ/3)` linearization plus smallness on the declared domain.

**L-PHASE.** The exact-map block law `φ_{m+1} − φ_m = 2π − τQ_m + r_m` with `|r_m| ≤ C Q_m^{3/2}`, established for the **exact six-step iterate**, not the cubic-vector truncation. This is the substantive analytic task and the one the Dyadic owner's "cubic-vector truncation only" label makes mandatory.

**L-BACKBONE.** `Q_m ≥ c/(m+κ)`, hence `Σ Q_m = ∞` and `Σ Q_m² < ∞`. Route (essentially available from the certified L1 law): from `|ΔQ + Q²| ≤ K Q^{5/2}` one gets `1/Q_{m+1} − 1/Q_m = 1 + O(Q_m^{1/2})`, so `1/Q_M = 1/Q_0 + M + O(Σ Q^{1/2}) = M(1+o(1))` since `Σ m^{-1/2} = o(M)`. Observed: `1/Q_m − m` drifts only from 13157.89 to 13171.03 over 4000 blocks. This lemma looks closest to a full proof.

## 4. The combination theorems (proved, given the lemmas)

**INF-1.** Define the accumulated defect `D_M := 2πM − (φ_{6M} − φ_0) = τ Σ_{m<M} Q_m − Σ_{m<M} r_m`. By L-BACKBONE the first sum diverges; by L-PHASE the second converges absolutely. Hence `D_M → ∞`. Verified in-window: `D_M` = 0.0088, 0.0854, 0.1649, 0.3090 at M = 100, 1000, 2000, 4000, with `Σ|r_m| = 0.00261` bounded against `τΣQ_m = 0.3064` growing logarithmically.

**INF-2 (counting bridge).** Given L-MONO, the crossing count equals the lap count, so the number of B-events in the first `6M` primitive steps satisfies

```
N(M) = M − D_M/(2π) + O(1).
```

Verified to within one event at every checkpoint. Now suppose all return gaps were eventually a fixed `m₀`. Then `N(M) = 6M/m₀ + O(1)`; matching the leading order forces `m₀ = 6`, and then `D_M = O(1)` — contradicting INF-1. **Therefore infinitely many non-6 gaps**, and since `N(M) → ∞`, infinitely many B-events. Gate 2 and the ALG form of Gate 5 close **together**, exactly as the PI anticipated.

Note this bridge is formulated at block level against the primitive return count, so it does not require a per-primitive-step phase law — only the block law the owner supplies plus monotonicity. That removes what looked like the awkward part of the six-step-to-primitive bridge.

## 5. What remains, and a scheduling observation

Only L-MONO, L-PHASE, L-BACKBONE. The combination arguments are done and need no revisiting. Ordering suggestion, cheapest first: **L-BACKBONE** (nearly derivable from certified L1 material), then **L-MONO** (small, and it also retires the gate-1 orientation caveat), then **L-PHASE** (the real work, requiring the exact six-step jet rather than the cubic truncation).

`[GUARD]` Everything numerical here is `[NUM]` seed-orbit evidence on an orbit not proved to lie in the theorem-certified `U_T` (the explicit-radius gap recorded in the v1.9.1 scope audit). The reduction and the two combination theorems are structural and independent of that seed. Nothing here touches SG-NG-23: closing INF would give a second stream, not a nontrivial commensurability class, and the limiting ratio would remain 6.
