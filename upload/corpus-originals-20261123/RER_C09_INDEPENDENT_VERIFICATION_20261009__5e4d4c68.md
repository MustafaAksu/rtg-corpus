# RER-GEN-C09 — independent receiving verification

**9 October 2026 · NONCANONICAL receiving check.**

This record does not adopt C09, register it in RER, or change any owner DSN or physical target. The target remains `NO_TARGET_VECTOR_LAW_SELECTED`. The model is the conditional Genesis→RER analytic modal contract (E, P, T_e, reprojection after every primitive step, F = N⁶) with one-time birth contract A, B_κ(s) = (s, κQ(s)J_Qs).

## 1. Method (independent of the C08/C09 code)

The checker is `c09_independent_series_check.py`, SHA-256 `758d38c79074333f98e289ddf0e66da1572014aab4d60ca19f00a48814aaa613`. It uses the Python standard library only.

- It imports nothing from the RER, C08 or C09 packages and does not read `jet_coefficients.json`.
- It composes the full sin/exp map exactly, without truncating to G₃/G₄. Each state is a power series in a scale parameter t along a ray s = t·u, kept through t¹², with exact rational coefficients.
- States at a matched current parent come from t-adic series inversion of s₀ ↦ s_n. This tests the stated current-parent claims directly, rather than only through the initial chart.
- √3 bookkeeping: writing κ = √3κ̃ makes every claimed identity rational, so equality is exact rather than numerical.
- The parameter grid is κ̃ ∈ {1, −2/3, 3/5}, rays u ∈ {(1,0), (0,1), (1,1), (2,−1), (1,3)}, ages n = 0–3, and all age pairs.

**Result: 511 PASS, 0 FAIL, exit 0.** These are six identity families checked over the parameter grid. The count is not 511 independent theorems.

The negative control (`--negative`) changes the C09 coefficient √3κ/6 to √3κ/9. It produces 180 named FAILs and exits 1.

## 2. Claims reproduced

| Claim (C07–C09 notes) | Order checked | Result |
|---|---|---|
| c_n(s) = C_κ(s) + nR_κ(s) + O_n(‖s‖⁶), with R_κ = −(√3κ/6)Q²s | residual is O(t⁶) | ✓ |
| c_n − c_m = −(n−m)(√3κ/6)Q²s + O(‖s‖⁶) | O(t⁶) | ✓ |
| s(FX_n) − s(FX_m) = (n−m)(κ²Q⁴/18)(−r−2e, 2r−3e) + O(‖s‖¹⁰) | O(t¹⁰) | ✓ |
| Q_s(FX_n) − Q_s(FX_m) = −(n−m)(2κ²/9)Q⁵ + O(‖s‖¹¹) | leading order exactly 10, remainder O(t¹¹) | ✓ |
| I_sc,n = −n(√3κ/6)Q³ + O(‖s‖⁷) | O(t⁷) | ✓ |
| Ω_G,n = −κQ² + O(‖s‖⁷) | O(t⁷) | ✓ |
| 2√3·I_sc/(Ω_G·Q_s) = n + O(‖s‖) | leading value equals n | ✓ |
| DF(0) = I, no quadratic part | — | ✓ |

## 3. Receiving rerun of the package's own suite

In a disposable copy, `RUN_CHECKS.py --negatives` was run under Python 3.13.16 with SymPy installed for this run.

- All three jet copies have SHA-256 `15a7d056…2824`.
- `make_jet.py` regenerates the jet byte-identically.
- The C08 checker reports 16 PASS lines and the C09 checker 25.
- Both intended negative controls fail as designed.

The notes state 15 and 24 checks. The runner counts every line containing `PASS`, which probably includes a summary line. This is cosmetic.

## 4. New observations: how the error terms depend on age

These are exact on the stated rays and κ values. They are a computed pattern, not a theorem.

1. **The O(‖s‖⁶) graph remainder is sharp and still affine in n.** On (t,0) with κ̃ = 1, the age-1 t⁶ term is (−13/32, 13/64)t⁶. The t⁶ coefficient is exactly proportional to κ·n.
2. **The first nonlinear age dependence appears at t⁷.** Its second difference in n is exactly (κ̃/4)Q³s. The coefficient of n² is therefore (√3κ/24)Q³s, along the parent direction. This holds on all five rays for κ̃ ∈ {1, −2/3}.
3. **Consequence for the age fingerprint:**
   - Its first-order error is multiplicative and κ-independent: R_age = n·(1 + a_u·t + …) along s = t·u, with a_(1,0) = 65/64 and a_(1,1) = 47/64. This was checked for n = 1–4.
   - Age-nonuniform terms enter only at the next relative order.
   - So the fingerprint resolves age while n‖s‖ is small. Point 2 is a concrete form of the "no uniform-in-age guarantee" caveat.
4. **Input to F3:** through order 6 the reachable sheets are c = C_κ(s) + n·D(s), with one age-independent drift field D. So up to t⁶ the union of sheets lies on a single smooth 3-fold parametrized by (s, τ), with τ continuous and τ⁺ = τ + 1. The n² term at t⁷ is the first obstruction to τ being exactly affine. A τ-reparametrization might absorb it, but that is untested.

## 5. Boundaries

- These are formal series in t along rays, with exact coefficients through t¹². Analyticity of F gives the stated asymptotic claims for sufficiently small t on each ray.
- No explicit radius is given, and no age-uniform domain is claimed.
- The checks are restricted to the five sampled rays. Five rays do not determine homogeneous polynomials of degree 5 or higher in two variables, which would need d+1 rays. So this is an exact sampled check of the C09 identities, not a symbolic-direction proof. The package's own SymPy checkers supply the symbolic version from the jet. The two routes agree.
- This does not independently authenticate historical Genesis producer bytes. It reproduces the declared formula.
- No physical birth contract, event law, RECOG recognition claim or factor selection follows.
