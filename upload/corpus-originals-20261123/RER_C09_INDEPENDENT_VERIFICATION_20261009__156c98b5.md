# RER-GEN-C09 — independent receiving verification

**9 October 2026 · NONCANONICAL receiving check.**

This record does not adopt C09, register it in RER, or change any owner DSN or physical target. The target remains `NO_TARGET_VECTOR_LAW_SELECTED`. The model is the conditional Genesis→RER analytic modal contract (E, P, T_e, reprojection after every primitive step, F = N⁶) with one-time birth contract A, B_κ(s) = (s, κQ(s)J_Qs).

## 1. Method (independent of the C08/C09 code)

The checker is `c09_independent_series_check.py`. Revision 2 (SHA-256 `67b2e0e785dd30a1bd637c79db2a7210d93516b79f5a00d5fb8233da04f6799b`) adds a `--quick` mode; its full-grid run is byte-for-byte the same calculation as revision 1 (`758d38c7…aa613`). It uses the Python standard library only. Runtimes here: full grid ≈18 s, `--quick` ≈1.3 s (43 PASS; negative exits 1).

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

## 6. Addendum (9 Oct, later) — receiving of the co-owner's age-geometry note

Inputs: `C09_AGE_GEOMETRY_RECEIVING_REVIEW.md` and `check_second_difference.py` (SHA-256 `fb8907f07ca285d6031135397b084c0d00fc80b320604f6a2742d696937150be`), run here against the pinned jet `15a7d056…2824`: **13/13 PASS, exit 0; `--negative` exits 1.**

**B₇ derivation (§B) — accepted.** The one-step propagation of a current-parent child perturbation δ is δ⁺ = δ + D₅ + A_c δ − Dδ·g_s + O(8), where the bracket D₅ = G₃,c(s,C) − DC·g_s is exactly the C07 drift. The neglected pieces are all O(8) or higher: the child-induced parent shift is O(7) and enters C(s′) at O(9); the G₄ child contributions carrying n are O(8). So B₇ = A_c D₅ − DD₅·g_s is the complete degree-7 n² coefficient. The symbolic result (κ̃/4)Q³s coincides with my untruncated full-map ray values on all five rays, so the two routes agree: symbolic-in-direction on the jet, exact-in-map on rays.

**[THM] no C¹ embedded 3-fold through the origin containing two age sheets (§D) — accepted, with one hypothesis discharged.** The proof needs both sheets to be graphs over a full s-neighbourhood of 0. That is not an extra assumption: DF(0)=I and DB_κ(0)=(I,0) make g_κ(s)=F_s(B_κ(s)) a local diffeomorphism, so every M_{κ,n} is a graph c=c_n(s) near 0 for fixed n. The argument then only uses C07's drift and C¹ continuity of D_cH at the origin; it is independent of the rest of the dynamics. The decisive feature is that the drift R_κ(s) ∝ s sweeps every direction of the child plane as s turns, which kills every candidate normal a. A drift along a fixed direction would not have this consequence. The same argument covers any pair n≠m.

**Fingerprint singular at 0 (§E) — accepted.** Trivially: distinct per-sheet limits at one accumulation point.

**New: the τ coordinate has a formal autonomous update at the retained order.** Define τ on the state by projecting c − C(s) onto D(s) = D₅+D₆+D₇ (equivalently, c₁(s) − c₀(s) through degree 7). Reading τ from the actual states X_n and F(X_n) on the untruncated map gives, on rays (1,0), (1,1), (2,−1) and κ̃ ∈ {1, −2/3}, ages 0–2:

\[
\tau^+ = 1 + \Big(1-\tfrac{Q_s}{2}\Big)\tau + O(Q_s^2\tau^2),
\]

with the residual starting exactly at order Q_s² (coefficient −Q_s²/4 at age 2) and no odd-order terms. Consistent with τ_n = n − (Q_s/4)n(n−1): τ_{n+1}−τ_n = 1 − nQ_s/2 = 1 − τQ_s/2 + O(Q_s²). So at this order the pair (s, τ) carries a reduced update (s, τ) ↦ (s + g_s(s) + …, 1 + (1 − Q_s/2)τ). Boundaries: formal, fixed-n remainders only; DF(0)=I makes all multipliers 1, so there is no standard convergence theorem for continuing this order by order; the chart degenerates at s=0 (∂_τ c(0,τ)=0), which is the singular 3-fold the THM says is unavoidable — a cone over the sheets with vertex at the origin.

## 7. Correction (9 Oct, 17:xx) — the τ-update claim in §6 is withdrawn; invariant replacement

**[COR] Withdrawn:** "τ⁺ = 1 + (1 − Q_s/2)τ + O(Q_s²τ²), residual starting exactly at order Q_s² (coefficient −Q_s²/4), no odd-order terms." Cause: my probe divided series kept only through t¹² (NT=12), so the quotient had three genuine coefficients and the t³, t⁴ entries were zeros by construction; the "−1/4 at t⁴" was the surviving cross term of a truncated product. Recomputed at NT=15 with a proper series quotient, the convention I used — Euclidean projection of c − C(s) onto d₁(s) truncated at total degree 7 — gives τ₂(t,0) = 2 − t²/2 + (73/3840)t³ + …, and even τ₁ = 1 + (101/960)t³ + …. The co-owner's two conventions give +13/512 (B-metric, full d₁) and −49/256 (Euclidean, full d₁); all three reproduce here. **What survives:** τ⁺ = 1 + (1 − Q_s/2)τ + O(‖s‖³) relative, and nothing beyond that is convention-independent. The co-owner's `check_tau_projection.py` (SHA `fcadd35d…4808`) passes 4/4 against my rev2 series code.

**Invariant replacement — age-fibre curvature as an all-direction polynomial.** Collinearity of the age-0/1/2 child states at a matched parent is measured by w(s) = det[d₁, d₂]. Using d₂ − 2d₁ = B₇ + B₈ + … and B₇ ∥ D₅,

\[
w(s) = D_5\wedge B_8 + D_6\wedge B_7 + O(\|s\|^{14}),
\]

and the degree-8 n² coefficient needs only the pinned G₃/G₄ jet: B₈ = A₃D₆ + A₄D₅ − DD₆·g₃ − DD₅·g₄, with D₆ = [D_cG₄,c(s,0)]C − DC·g₄. Symbolically, for all directions,

\[
\boxed{\,w(s) = -\frac{\tilde\kappa^{2}}{1024}\,Q_s^{5}\,K_3(r,e),\qquad K_3 = 111r^3 - 68r^2e + 177re^2 - 175e^3\,}
\]

(`triad_age_fibre_curvature_check.py`, SHA `e56088b0fa57e97aac590b9c92bd1490c2784cb85b9ee9719a26bc99254817f2`; 13 PASS, negative control exits 1). It reproduces the co-owner's three ray values (−111/1024, −45/1024, 175/1024 at κ̃=1) and three further rays against the untruncated full-map series, including B₈ and D₆ componentwise. Two consequences:

1. The wedge is exactly D₅ ∧ R₈ with R₈ = B₈ + (Q_s/2)D₆ the n² term left after the degree-7 reparametrisation τ = n − (Q_s/4)n(n−1). So no choice of τ(s) can straighten the fibres at degree 8: the transverse part is a coordinate-free obstruction, while any component along D₅ is absorbable. This is the "degree-8 transverse normal defect" the co-owner asked for.
2. K₃ has exactly one real zero direction, e/r ≈ 1.15205 (discriminant −8516860031). On that ray only the t¹³ coefficient of the wedge vanishes; exact collinearity of the three age states in the full analytic model is not shown, and higher orders may separate them [wording narrowed on Triadic review, 9 Oct]. The leading-order bending has opposite senses on either side of that ray. The transverse defect is therefore not a positive multiple of a power of Q_s, unlike D₅ and B₇.

Scope: formal, fixed finite ages 0–2, conditional model; nothing about convergence, uniform domains, physical memory, or a reduced autonomous law. A curved three-parameter description c = C + τD + τ²E + … on the punctured region is not excluded.

## 8. Formal F-invariant age family with trivial clock (9 Oct, evening) — answers the Triadic §5 test at the formal level

**[ALG, formal]** At matched current parent s, the s-degree-d coefficient of c_n(s) is a polynomial in n of degree ≤ d−4. Reason: in the propagation δ_{n+1} = δ_n + D(s) + A·δ_n − Dδ_n·g + (higher), the linear operator raises s-degree by at least 2, so each two s-degrees add at most one power of n (degree 5: n; 7: n²; 9: n³; …). Verified on the untruncated map: age-8 coefficients through t¹¹ are exactly predicted by Lagrange interpolation of ages 0–7 (three rays, two κ).

Consequently there is a unique interpolation 𝒞(s,τ), polynomial in τ at each s-degree, with 𝒞(s,n) = c_n(s). Since F(s, c_n(s)) = (s⁺, c_{n+1}(s⁺)) for every integer n ≥ 0 and both sides are polynomial in τ at each s-degree, the identity theorem for polynomials gives order by order

\[
\boxed{\;\mathcal F\big(s,\mathcal C(s,\tau)\big)=\big(s^+,\ \mathcal C(s^+,\tau+1)\big)\quad\text{for every real }\tau\;}
\]

— the invariance test proposed in the Triadic review, with the trivial clock τ⁺ = τ + 1. Checked at τ = 1/2, −1/3, 5/2 on three rays and two κ values: child residual identically zero through t¹² (`triad_formal_age_family_check.py`, SHA `5bc3494dae0d4cb390dbe4946382d8d3bbe1167d0613dafc0a34dde48d4f98e1`; 12 PASS; negative control τ⁺ = τ + 1.1 gives 9 FAIL, exit 1; ≈100 s).

**What this does and does not say.** It shows the age sheets are, formally, the integer slices of one F-invariant one-parameter family of surfaces, and that in the interpolation coordinate the clock is exactly τ⁺ = τ + 1. The earlier τ-convention discussion (§§6–7) therefore had no invariant content beyond this: every other τ(s,c) is a reparametrisation of this coordinate. The curvature w₁₃ ≠ 0 does not obstruct the family; it only says the family is not affine in τ at degree 8. The result is formal: the polynomial degree in τ grows with the s-degree, so for fixed non-integer τ the family is an asymptotic series with no convergence, radius or uniform-in-age statement; all slices still pass through the origin, where the C¹-3-fold obstruction stands; and nothing here is an observable-preserving 2D factor, a physical clock, or a memory variable. The fingerprint 2√3 I_sc/(Ω_G Q_s) restricted to the family equals τ + O(‖s‖), i.e. it is a first-order reading of this same coordinate.

## 9. Scope corrections to §8 on Triadic review (9 Oct, evening)

**[COR] Degree bound.** "Polynomial in n of degree ≤ d−4" is meaningless at d=3 (the cubic C_κ is age-independent) and is only a weak bound for d ≥ 5. The correct statement, from invariance of {c=0} and the two-degree raise per application of N = F* − I, is deg_τ[𝒞]_d ≤ ⌊(d−3)/2⌋ for d ≥ 3. Checked on the full map (κ̃ = 1 on (1,0); κ̃ = −2/3 on (2,−1)): the exact n-degree at s-degrees 3…12 is 0, –, 1, 1, 2, 2, 3, 3, 4, 4 — the bound is attained at every degree ≥ 5, and degree 4 carries no term. So 𝒞 is determined through t¹² by ages 0–4 (five points), not nine; the nine-age interpolation in the §8 certificate is over-determined and therefore also a consistency check.

**[COR] Uniqueness and "reparametrisation".** 𝒞(s,τ) is unique among interpolants whose s-coefficients are polynomial in τ. It is not unique among smooth or analytic interpolants: terms vanishing at all integers (e.g. sin πτ × anything) change nothing on the sheets. The sentence in §8 "every other τ(s,c) is a reparametrisation of this coordinate" is withdrawn as too broad; it holds only for charts of the same polynomial-class family related by invertible changes.

**Accepted as the all-orders proof.** The Triadic structural argument — U^τ := Σ_k C(τ,k) N^k on R[[s,c]] is a formal algebra automorphism with U^τU^σ = U^{τ+σ}, and 𝒞(s,τ) := Z_τ∘S_τ⁻¹ — gives the identity at every formal order; my §8 certificate is the finite-order sampled check of the same statement. The result is a formal fractional iteration of a map tangent to the identity, a general mathematical possibility rather than an RTG-specific mechanism; its status is "formal suspension/semiconjugacy of the reachable age sheets", not an effective state. Convergence, admissible domain away from zero, uniform-in-age control and any observable-preserving 2D factor remain OPEN.
