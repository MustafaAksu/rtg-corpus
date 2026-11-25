# DYAD OPEN 20 — scale of the real forward leg, for the C++ adapter

**By:** Claude, Dyadic DSN owner. **Date:** 17 November 2026. **Status:** [NUM] working note (SESSION). Floating midpoint orbit estimates, not enclosures; nothing here is a bound or a certificate.
**Why:** the co-owner's first real-input step (relayed by the PI, 17 November) enclosed one block over the whole fibre \|d\| ≤ 0.002 with tangent width 10.74. The co-owner proposes subdivision and a horizon of 2 → 5 → 10 → 20. This note gives the true sizes along the real orbit, so that the adapter's targets can be set from them.

**Method.** `evidence/dyad/open20-an/cpp-review/realleg-scale/dyad_open20_realleg_scale_estimate.py`:
- the pilot coefficients a₀…a₄₀ (stage-1 constants, the library's `coefficients`, 400 digits);
- the raw map T with its variational equation, 80 digits, midpoints kept after every block;
- the start ξ* = 0.40 e^{iπ/6} in the lifted chart of F;
- the tube radius R₀ of the library (`R_upper`).

**The reference orbit d₀ = 0 is not the curve** (co-owner's comment `6943957865`). The true value d* is about 2·10⁻⁸ away, so d_k(0) ≈ −b_k d* grows: at k = 20, \|d₂₀(0)\| = 2.6·10⁻⁷ is already above R₀(ξ₂₀) = 9.4·10⁻⁸. The table is therefore a scale estimate for shooting, not a statement about the orbit of the curve. To first order it carries over, because b_k and ξ_k change little between d₀ = 0 and d₀ = d* (§2: across the whole fibre of radius 0.002 they change by a few per cent).

Here b_k = ∂d_k/∂d₀ at d₀ = 0, and the ratio R_k/(\|b_k\| R*) is the radius the necessary condition at step k would give, relative to the initial radius R* = 0.002, if the derivative were known exactly.

## 1. Along the orbit from d₀ = 0

| k | \|ξ_k\| | arg ξ_k / π | \|b_k\| | R₀(ξ_k) | R_k / (\|b_k\| R*) |
|---|---|---|---|---|---|
| 1 | 0.408 | 0.142 | 0.81 | 2.0·10⁻⁴ | 0.125 |
| 2 | 0.408 | 0.113 | 0.75 | 4.5·10⁻⁵ | 3.0·10⁻² |
| 5 | 0.358 | 0.047 | 1.31 | 4.6·10⁻⁶ | 1.7·10⁻³ |
| 10 | 0.289 | 0.019 | 3.92 | 8.0·10⁻⁷ | 1.0·10⁻⁴ |
| 20 | 0.232 | 0.008 | 12.8 | 9.4·10⁻⁸ | 3.7·10⁻⁶ |
| 100 | 0.141 | 0.001 | 206 | 2.1·10⁻¹⁰ | 5.0·10⁻¹⁰ |
| 334 | 0.096 | −0.000 | 1711 | 1.4·10⁻¹² | 4.1·10⁻¹³ |

**Two consistency checks with the Python legs:**
- 0.002 × 4.1·10⁻¹³ = 8.1·10⁻¹⁶, which is the radius of the F-leg disc of W6/W8 (8.0967·10⁻¹⁶).
- d₃₃₄ / b₃₃₄ at d₀ = 0 has modulus 2.04·10⁻⁸, which is the modulus of the F-leg centre (−4.32·10⁻⁹ + 1.99·10⁻⁸ i).

## 2. How much the derivative and the base really vary over the whole fibre

From 12 points on \|d₀\| = 0.002:

| k | \|b_k(0)\| | max \|b_k(d₀) − b_k(0)\| | max \|ξ_k(d₀) − ξ_k(0)\| |
|---|---|---|---|
| 1 | 0.81 | 0.012 | 8.8·10⁻⁴ |
| 2 | 0.75 | 0.020 | 1.7·10⁻³ |
| 5 | 1.31 | 0.040 | 1.9·10⁻³ |
| 10 | 3.92 | 0.031 | 2.6·10⁻³ |
| 20 | 12.8 | 1.19 | 7.7·10⁻³ |

## 3. What follows for the adapter

1. **The contraction comes from the shrinking tube radius, not from fibre expansion.** For the first three steps \|b_k\| < 1. The necessary condition still gives a factor 8 after one step and about 30 after two, because R₀ falls by a factor 5–10 per step at the start. A horizon of 1–2 is enough for the first acceptance criterion (the radius 0.002 really shrinks). Horizon 20 would give about 7·10⁻⁹, already below the jump size \|c₁ − c₀\| ≈ 2·10⁻⁸.
2. **The obstacle at k = 1 is overestimation of the derivative, not the dynamics.** The true variation of b₁ over the whole fibre is 0.012. The enclosure width was 10.74, about 900 times larger. With the true D, even the whole fibre would contract in one step: (2.0·10⁻⁴ + 0.012 × 0.002)/0.81 ≈ 2.8·10⁻⁴, a factor 7.
3. **Two ways to close the gap:**
   - *Subdivision.* If the enclosed D scales linearly with the tile radius, tiles of radius about 3·10⁻⁴ suffice at k = 1, that is roughly 50 tiles.
   - *A finer evaluator.* Mean-value updates per T instead of per six-step block. At \|x\| ≈ 0.87 the map is far from the identity, and one block of interval jets wraps strongly.

   Which is cheaper is for the co-owner to measure.
4. **The base enclosure matters for M.** R₀ varies like \|ξ\|^{12.6} and depends strongly on the angle. A base enclosure about 8 times wider than the true spread (as in the first step) makes M = sup R₀ larger, but not by orders of magnitude. The F2 rule (supremum over X_k ∩ D₀) applies.
5. **A simple form of M on X ∩ D₀.** On D₀, first > 1 and second > c₀. So, with R₀ = ε\|ξ^α\| first⁻³ second⁻³, an upper bound on X ∩ D₀ is
   ε · sup_X \|ξ^α\| · max(1, inf_X first)⁻³ · max(c₀, inf_X second)⁻³.
   The supremum of \|ξ^α\| = exp(Re α log ξ) is taken with the principal logarithm restricted to the chart sector of D₀ (−0.20π < arg ξ < 0.30π); D₀ lies in that sector. This needs no proof that X ⊂ D₀, which is the refinement of §7 of the C++ review.
6. **Scope.** These are floating estimates of one orbit and of 12 sample points. They are targets for the adapter, not premises. The adapter's acceptance must rest on its own enclosures, as the design says.
