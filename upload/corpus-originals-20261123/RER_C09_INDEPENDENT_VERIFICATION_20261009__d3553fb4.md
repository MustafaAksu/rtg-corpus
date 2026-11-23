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

## 10. Finite-jet compatibility defect, N = 7 and N = 8 (10 Oct) — first pass at the Triadic error contract

Files: `triad_finite_jet_defect_N7_N8.py` (SHA `de3675953013d3a1e83227a46565708b16068314974bf81ad142a3f42034d9a3`; 4 PASS, exit 0; `--negative` drops 𝒞₇ and exits 1), its log, and `age_family_polynomials_kt1.json` (SHA `03042f84…d83c`). κ̃ = 1 only.

**A. Exact all-direction 𝒞_d, d = 3…9.** Reconstructed from exact ray series of the full map (d+1 rational rays per degree, ages 0…⌊(d−3)/2⌋), checked against an unused ray and against the closed forms of D₅ and B₇. This supplies D₇, D₈, D₉ and all n²/n³ terms without a quintic jet. τ-degrees are exactly ⌊(d−3)/2⌋ at every d.

**B. [COR to my own draft of this study] Leading defect.** Because ∂_cF_c = I + O(‖X‖²), the omitted order enters at both ends of the step, and

\[
\mathcal E_N(s,\tau)=\Delta_\tau\mathcal C_{N+1}(s,\tau)+\Delta_\tau\mathcal C_{N+2}(s,\tau)+O(\|s\|^{N+3}),\qquad \Delta_\tau f(\tau)=f(\tau+1)-f(\tau),
\]

not −𝒞_{N+1}(s,τ+1) as I first wrote. Confirmed against the real map at 50 digits: N=8 deviates 0.28 % from Δ_τ𝒞₉ at |s| = 0.003; N=7 deviates 0.055 % from the two-term prediction. In the binomial basis Δ_τ removes the age-independent part, so Δ_τ𝒞₈ = D₈ + τB₈ and Δ_τ𝒞₉ = D₉ + τB₉⁽²⁾ + C(τ,2)B₉⁽³⁾.

**C. Empirical constants (grid: 24 directions × τ ∈ {0, ½, 1, 3/2, 2} × 8 radii; not certified bounds).**

| |s| | Q_s range | sup|𝓔₇|/|s|⁸ | sup|𝓔₈|/|s|⁹ | sup|𝓔₇|/|D₅| | sup|𝓔₈|/|D₅| |
|---|---|---|---|---|---|
| 0.003 | 7–9 ·10⁻⁶ | 2.51 | 58.4 | 1.4·10⁻⁷ | 7·10⁻⁹ |
| 0.03 | 0.0007–0.0009 | 4.05 | 59.6 | 2.2·10⁻⁴ | 1.0·10⁻⁵ |
| 0.12 | 0.011–0.014 | 8.90 | 64.0 | 0.031 | 0.019 |
| 0.25 | 0.047–0.063 | 15.6 | 72.7 | 0.49 | 0.57 |

Three readings. (i) The N=8 jet is **not** better than N=7 at |s| ≳ 0.2: the degree-9 coefficient (sup ≈ 58) is ≈ 25× the degree-8 one (≈ 2.3), so at |s| ≈ 0.04 successive orders are already comparable; the asymptotic regime for the N=7 contract is |s| ≲ 0.01. (ii) Measured against the inter-age separation |D₅| = ½Q²|s| (the quantity that decides whether the family resolves age at all), the one-step defect is ≈ 1 % at |s| = 0.12 and ≈ 50 % at |s| = 0.25 for both N. So for τ ≤ 2 the finite-jet family is age-resolving only for Q_s ≲ 0.01–0.02 — this is the quantitative content of the "no uniform-in-age control" caveat. (iii) The 25× growth between d = 8 and d = 9 is the first hint on the convergence question; if it persists the formal series has radius ≲ 0.04 in |s|, but two orders are far too few to claim that. More orders (d = 10, 11) with the same reconstruction would settle whether the ratio is stable.

Observables: Q_s error is identically zero by construction (same s⁺ on both sides); I_sc and Ω_G errors are 2–6·10⁻⁵ at |s| = 0.25 and 10⁻¹⁴ at |s| = 0.03.

**D. [CAND] Closed form of the top-age-degree coefficients.** At s-degree 2k+3 the τ-degree-k coefficient is, for k = 1, 2, 3,

\[
P_{2k+3,k}(s) = -\tfrac12\binom{-1/2}{\,k-1\,}\,Q_s^{\,k+1}\,s \qquad(-\tfrac12 Q^2 s,\ \tfrac14 Q^3 s,\ -\tfrac{3}{16} Q^4 s),
\]

all along s, with κ̃ = 1. Three data points only; if it continues, the radial part of the age dependence resums to Σ_k C(τ,k) C(−½,k−1) Q^{k−1}, a hypergeometric-type function of (τ, Q) — which is exactly the regime τQ ~ 1 where fixed-age asymptotics fail. Worth one more order before anyone leans on it.

Scope unchanged: conditional model, formal family, empirical grid; no certified K_{N,T}, no multi-step accumulation, no physical clock or memory.

## 11. [COR] Corrections to §10 on Triadic receiving review (10 Oct, evening)

Receiving review `N7_N8_RECEIVING_REVIEW.md` and `check_pointwise_metrics.py` (SHA `61a54f0a29a786941ee283bc52a7a2274de0d8a4f7101eea03c6f2ef37eadf0b`) reproduced here against the unchanged polynomial table; all five rows agree. Three corrections accepted:

1. **Q_s range.** On the grid s = R(cos θ, sin θ), Q_s = R²(1 − ½ sin 2θ), so **½R² ≤ Q_s ≤ 3/2 R²**, both extremes attained at the sampled angles. The "[0.75R², R²]" label in §10 and in the script was wrong. At R = 0.12 the sampled range is [0.0072, 0.0216]; at R = 0.25 it is [0.031, 0.094]. The Q_s-threshold phrasing in §10 C(ii) is withdrawn with it.
2. **Age-resolution normalisation.** |D₅(s)| = ½Q_s²R varies with direction; §10's "sup|𝓔|/|D₅|" column divided a grid supremum by the fixed ½R⁵ and overstated the ratio. The pointwise statistic max_grid |𝓔_N(s,τ)|/|D₅(s)| is:

   | R | 0.03 | 0.08 | 0.12 | 0.18 | 0.25 |
   |---|---|---|---|---|---|
   | N=7 | 9.7·10⁻⁵ | 3.1·10⁻³ | 1.4 % | 6.2 % | 21.6 % |
   | N=8 | 4.3·10⁻⁵ | 2.3·10⁻³ | 1.2 % | 6.3 % | 25.2 % |

   The script now prints this statistic (rev. SHA `5c63c363d25f30f610e3339363b5fcb261c1e9a31e6a99086767993d0e837c82`; JSON unchanged, log replaced). Consequently §10 C(i) is also narrowed: **N=8 does improve on N=7 for R ≲ 0.12**, loses the advantage near R ≈ 0.18, and is worse at 0.25. The grid maxima all occur at τ = 0 and at the Q_s-maximal angles; at τ = 0 the state is exactly the birth graph, so 𝓔_N(s,0) is simply the age-1 sheet's truncation tail Σ_{d>N} D_d(s⁺).
3. **ΔQ_s = 0** is by construction (identical s⁺ on both sides), as §10 said; it is not a parent-accuracy statement for a multi-step comparison. One-step observable errors are exactly ΔI = B(s⁺, 𝓔), ΔΩ_G = (√3/2)(s⁺_η𝓔_ρ − s⁺_ρ𝓔_η), hence |ΔI| ≤ (3/2)|s⁺||𝓔| and |ΔΩ_G| ≤ (√3/2)|s⁺||𝓔|.

Also withdrawn as over-reaching: the §10 C(iii) remark that a persistent 25× coefficient growth "would mean radius ≲ 0.04" — two degrees determine no radius. Everything in §10 remains sampled-grid evidence at κ̃ = 1; no certified K_{N,T}, no multi-step accumulation, no physical interpretation.

**On the proposed next gate (certified K₇, K₈ on a compact region).** Agreed that this precedes d = 10, 11. The ingredients are: exact majorants for Δ_τ𝒞₈, Δ_τ𝒞₉ on the region (they are explicit polynomials, so this is routine), and a rigorous remainder for the 36 primitive sin/expm1 steps with reprojection — most directly by interval arithmetic (mpmath `iv` or Arb) over the region with τ ∈ [0,T] including τ+1 and all intermediate states, together with an invariance check that the region's image stays inside the domain where the majorants hold. That is a substantial compute piece and belongs on the RTG machine; I can draft the interval-arithmetic checker and the region contract next.
