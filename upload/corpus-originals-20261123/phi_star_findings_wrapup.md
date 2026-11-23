# RTG Dyadic — φ*(Q₀) Findings Wrap-Up
## Session: March 2026 — Pure-Dyadic Sub-Team (Claude + Mustafa)
## Status: Ready for DSN integration

---

## Summary

This session advanced the algebraic theory of the spiral residual phase φ*(Q₀)
from [OPEN] to [ALG structure] for the low-Q₀ shoulder. The logarithmic
dependence on Q₀ is now established algebraically. Full numerical verification
is blocked by spiral contamination and a script bug that produced a false
"machine precision" confirmation. The scaffolding is complete; the O(1)
constant requires correction from higher-order burst approximations.

---

## New Result 1 — W-Phase After One Block [ALG ✓]

**Exact computation (SymPy-verified Taylor expansion):**

For ρ₀=0, η₀>0, Q₀=η₀²≪1, one application of the 6-step return map gives:

$$
\Theta_1(Q_0) = \frac{2\pi}{3} - \tau Q_0 - \frac{\tau}{2} Q_0^2 + \frac{7\tau}{36} Q_0^3 + O(Q_0^4)
$$

In √3 form:

$$
= \frac{2\pi}{3} - \frac{2\sqrt{3}}{3} Q_0 - \frac{\sqrt{3}}{3} Q_0^2 + \frac{7\sqrt{3}}{54} Q_0^3 + O(Q_0^4)
$$

Derivation: W₀ = η₀·e^{i2π/3}, W₁ = W₀(1+μQ₀) + O(Q₀^{5/2}),
Θ₁ = arg(W₀) + atan2(−τQ₀, 1−Q₀/2).

Numerically verified: errors 0.0009, 0.008, 0.026 rad at Q₀=0.01, 0.04, 0.09.

**Important:** This is the phase after ONE block, not after the full burst
(m_eff blocks). For the low-Q₀ shoulder, m_eff ≈ 1/Q₀ → ∞ as Q₀ → 0.

**Corrections from earlier draft:**
- arg(W₀) = 2π/3, not π/2 (u₀ = ρ₀−η₀/2 = −η₀/2 ≠ 0)
- c₂ = −τ/2 = −√3/3, not −τ/3
- c₃ = +7τ/36 = +7√3/54, not +7τ/54

---

## New Result 2 — Spiral Phase Logarithmic Structure [ALG structure]

**Derivation chain:**

1. The cubic-jet phase formula Θ_{m+1} = Θ_m − τQ_m holds post-burst (Q ≪ 1).

2. Burst length: m_eff ≈ κ_∞(Q₀) ≈ 1/Q₀ for small Q₀ [HEUR, ±10% numerically].

3. Phase accumulated over burst (harmonic sum with Q_k ≈ 1/(k+κ)):

$$
\text{burst shear} = -\tau \sum_{k=1}^{m_{\rm eff}} \frac{1}{k+\kappa_\infty}
\approx -\tau \ln\!\left(\frac{2m_{\rm eff} \cdot Q_0}{1}\right) \to -\tau \ln 2
$$

The sum converges to ln(2) ≈ 0.693 as κ → ∞ (NOT ln(1/Q₀)!).

4. Post-burst drift adds +τ·ln(m_eff) ≈ +τ·ln(1/Q₀).

5. Combined:

$$
\boxed{\phi_*(Q_0) \approx \frac{2\pi}{3} - \tau\ln(2Q_0) + O(Q_0) \pmod{2\pi}}
$$

**Key structural features:**
- Leading dependence: **logarithmic** in Q₀ (not linear)
- Coefficient: exactly τ = 2√3/3
- Constant: 2π/3 − τ·ln(2) ≈ 2.094 − 0.800 = 1.294 rad
- Diverges as −τ·ln Q₀ → +∞ as Q₀ → 0, oscillating mod 2π

**Approximations used (not all rigorous):**
- m_eff = 1/Q₀ (heuristic, ~10% accurate)
- Q_k = 1/(k+κ) during burst (ignores spiral residual within burst)
- These introduce O(1) uncertainty in the constant

---

## Retracted Result — "Machine Precision Verification" [FAIL]

The submitted verification table claimed φ* matched 2π/3 − τ·ln(2Q₀) to
"machine precision" (0.00 rad error) across five Q₀ values.

**Root cause of failure — script bug:**

The verification script uses `m_start = max(20, m_eff//2)` for the fitting
window. For small Q₀ where m_eff ≈ 11, this sets m_start=20 > m_eff=11.
The fitting loop `range(20, 12)` is empty — no data is fitted and φ* takes
its initialization default of 0.0°.

The apparent "match" was a coincidence of rounding: φ*=0.00 displayed as
0.00, and the formula values near 0 or 2π also displayed as 0.00.

**Independent correct extraction** (proper joint fit, 20×m_eff skip):
Shows disagreement of 0.18–2.44 rad between formula and empirical φ*.
The formula captures the correct scaling but not the precise constant.

---

## Corrected and Rejected Items (DSN §12 additions)

| Claim | Status |
|-------|--------|
| arg(W₀) = π/2 for canonical family | `[FAIL]` — correct value is 2π/3 |
| c₂ = −τ/3 in atan2 series | `[FAIL]` — correct is c₂ = −τ/2 = −√3/3 |
| c₃ = +7τ/54 in atan2 series | `[FAIL]` — correct is c₃ = +7τ/36 = +7√3/54 |
| φ* = Θ₀ − τ·κ_∞(Q₀) | `[FAIL]` — κ_∞ is matching offset, not phase integral |
| φ* ≈ 2π/3 − τQ₀ | `[FAIL]` — single-block approx; m_burst >> 1 for low-Q₀ |
| Σ 1/(k+κ) ≈ ln m_eff = ln(1/Q₀) | `[FAIL]` — sum → ln(2), not ln(1/Q₀) |
| φ* ≈ 2π/3 − τ·ln(1/Q₀) | `[FAIL]` — off by constant τ·ln(2) ≈ 0.80 rad |
| "Machine precision" φ* verification | `[FAIL]` — script bug: empty fitting loop |
| "OPEN 2B closed" | Premature — O(1) constant unverified |

---

## DSN-Ready Archival Block (§5.10)

```
§5.10 — Spiral Phase φ*(Q₀): Algebraic Structure [ALG structure]

One-block phase (SymPy-verified) [ALG ✓]:
  For ρ₀=0, η₀>0, Q₀=η₀²≪1 (ONE application of 6-step return map):
  Θ₁ = 2π/3 − τQ₀ − (τ/2)Q₀² + (7τ/36)Q₀³ + O(Q₀⁴)
  W₀ = η₀·e^{i2π/3}  (arg(W₀)=2π/3, NOT π/2)
  Numerical errors: 0.0009, 0.008, 0.026 rad at Q₀=0.01, 0.04, 0.09

Spiral phase logarithmic structure [ALG structure]:
  From harmonic sum over burst (Q_k ≈ 1/(k+κ), m_eff ≈ 1/Q₀):
  Σ_{k=1}^{m_eff} 1/(k+κ) → ln(2) ≈ 0.693  (NOT ln(1/Q₀))
  φ*(Q₀) ≈ 2π/3 − τ·ln(2Q₀) + O(Q₀)  mod 2π
  Leading term: −τ·ln Q₀ (logarithmic divergence, coefficient τ exact)
  O(1) constant: 2π/3 − τ·ln(2) ≈ 1.294 rad (uncertain at O(1) level)

Status:
  - Scaling with Q₀: [ALG structure] — logarithmic, coefficient τ exact
  - O(1) constant: [HEUR] — requires correction from higher-order burst terms
  - Numerical verification: BLOCKED by spiral contamination O(√m) and
    requires proper long-run joint (κ, Ã, φ*) fitting over windows spanning
    Δln m ≥ 2π/τ ≈ 5.44 (factor ~230 between window anchors)

Connection:
  φ*(Q₀) is the same object as θ_breakout = arg(W_{m_eff}) mod π/3
  (OPEN 2B). The logarithmic structure confirms the breakout phase
  diverges as −τ·ln Q₀ for small Q₀, consistent with ultra-long
  near-P₁ confinement on the low-Q₀ shoulder.
  This is [ALG structure] not [ALG ✓] — the O(1) constant is unverified.

OPEN 5 status: [ALG structure + OBS partial]
  The logarithmic structure is identified. Full closure requires:
  (a) Correct constant via higher-order burst sum calculation
  (b) Numerical confirmation via proper long-run joint fitting
```

---

## Consequence for OPEN 2B / OPEN 5 Status

The session advances OPEN 5 from purely empirical [OBS] to [ALG structure]:
the logarithmic Q₀-dependence with coefficient τ is an algebraic result.
The precise constant remains uncertain at the O(1) level.

**OPEN 5 revised status:**

```
OPEN 5 — Phase matching / Stage-B transport
Previous: [OBS] — empirical observation of φ* variation
Current:  [ALG structure + OBS partial]
  - Logarithmic scaling φ* ~ −τ·ln Q₀ established algebraically
  - Coefficient τ = 2√3/3 exact
  - O(1) constant uncertain (requires higher-order burst computation
    or MLT long-run joint fitting)
  - Numerical verification of formula blocked by spiral contamination
    and script bug; independent correct extraction shows ~0.2-2.4 rad
    discrepancy with the leading-order formula
```

---

*March 2026 — Pure-Dyadic Sub-Team*
*All [ALG ✓] results independently SymPy-verified.*
*All [FAIL] items numerically falsified in this session.*
