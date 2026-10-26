# Relay Note to Dyadic Owner — Invariant Form, τ, and Parabolic Class

**Note ID:** `NG_TO_DYAD_RELAY_RIEMANN_LENS_v1` · **Date:** 2026-08-28
**From:** Number Genesis (auditor) · **To:** `RTG_DYADIC_OSCILLATOR_DSN` owner
**Certificate:** `ng_riemann_lens_cert_v1.py` / `.log` (8 assertion families, exit 0)
**Status:** findings offered for Dyadic adoption; **not** claimed in the Number Genesis ledger, since `Q_true`, `J`, `τ` and the phase law are Dyadic-owned objects.

---

## 1. Findings

**D-1. `Q_true` is the unique invariant quadratic form of the order-6 linearization.** For `J = J(P₁) = [[1,−1],[1,0]]` (order 6, eigenvalues `exp(±iπ/3)`), the form `Q = ρ² − ρη + η²` satisfies `Q ∘ J = Q` exactly, and the space of `J`-invariant quadratic forms is one-dimensional. `Q` is therefore the Eisenstein/hexagonal norm form attached to `λ = exp(±iπ/3)`.

**D-2. This makes SG-1 forced rather than conventional.** `Q_euclid = ρ² + η²` is *not* `J`-invariant; its defect is exactly `ρ(ρ − 2η)`. The existing policy that `Q_true` is the sole primary radial observable and `Q_euclid` is comparison-only currently reads as a modelling convention. It is a theorem: only `Q_true` is preserved by the certified linearization. Suggest recording this as the *reason* for SG-1.

**D-3. `τ` has a closed form.** With Gram matrix `g = [[1, −½], [−½, 1]]`, `det g = 3/4`, and

```
τ = 2√3/3 = 1/√(det g).
```

The ISP phase-shear constant is the volume normalisation of the invariant form — not an independent empirical constant.

**D-4. Consequent closed form for the observed slip ratio.** `π/(3τ) = √3π/6`, so the geometric spacing constant observed in the Number Genesis section-return study is

```
exp(√3π/6) = 2.476632271…
```

against measured successive ratios 2.4710, 2.4746, 2.4760 (converging). Offered as a Dyadic-side prediction; the Number Genesis usage of it remains guarded under SG-NG-23 as a representation-level diagnostic.

**D-5. `F = T⁶` is tangent to the identity, with `F − id` of leading total degree 3.** Verified symbolically. This places the six-step map in the classical **cubic parabolic germ** class, for which orbits satisfy `|z_n| ~ n^{-1/2}` — exactly matching the certified `Q_m ~ 1/(m+κ)` backbone. The practical consequence: Fatou-coordinate / Takens normal-form theory applies to `F`, and the logarithmic term in a parabolic Fatou coordinate is the natural home for the observed logarithmic phase drift. This may give the ISP phase law a route to theorem status beyond the current cubic-vector truncation label.

**D-6. Conjecture offered, not claimed.** That `√3π/6` is the iterative-residue / logarithmic coefficient of the Fatou coordinate of `F`. If confirmed, the slip-spacing law and the exact-map remainder bound plausibly follow from one computation.

## 2. Cross-checks and caveats

- The measured phase-law remainder is `O(Q^{3/2})`, **not** `O(Q²)`: `sup|r|/Q²` diverges as `Q → 0` while `sup|r|/Q^{3/2}` is stable at ≈ 1.35 across a 256-fold range. Half-powers of `Q` are odd powers of `|z|`, the signature of real/anti-holomorphic resonant terms — consistent with the existing N-3C result that the primitive pullback mixes anti-holomorphic sectors and with the pure anti-holomorphic `(0, p−1)` resonant slot. A purely holomorphic normal-form treatment would miss this.
- D-1 through D-5 are exact symbolic statements about the linearization and the truncated six-step jet. They make no claim about the exact map beyond the stated degree computation.
- No Number Genesis claim depends on these findings; they are offered upstream. If the Dyadic owner adopts them, Number Genesis will import by reference only, with tags inherited.
