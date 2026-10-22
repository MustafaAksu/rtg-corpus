# DYAD OPEN 20 / O20-an — P1-c-5b/5c: convergence analysis of the formal invariant curves φ±, and the fixed-point index of F|Γ± (SESSION v0.1)

**Version:** v0.1 · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Basis.** P1-c SESSION v0.1 (`9f6f09d8…0902`), reviewed as `SCIENTIFIC REVIEW ACCEPTED — WITH SCOPE RESTRICTIONS`.

The review set the priorities:
- **P1-c-5b:** a convergence analysis of φ±. Numerator and denominator growth are to be kept separate. A failed majorant attempt is **not** a divergence proof.
- **P1-c-5c** (in parallel): the résidu itératif, as a small algebraic task.

**Status.**
- `[SESSION]` record. Nothing is adopted.
- DYAD v6.4.18 is unchanged; OPEN 20 PARTIAL; B-an and B-6 OPEN.
- The P2/P3 campaign has not been run.

**Check script.** `dyad_open20_an_p1c5_check.py`, with helpers `qw.py`, `fzw.py`, `ext.py` and `logzw.py`. It writes `p1c5_check.json` (byte-deterministic; verified by rerun) and `p1c5_perf.json` (timings only).
- 4 gates (H1–H4) and 3 negative controls (M1–M3).
- Runs in about 5 s.

**Exact field.** All exact work is done in E = ℚ(i√3)[a]/(Aa² + Ba + C), where a = a₂ stands for **either** root. An identity proved in E therefore holds for both curves φ₊ and φ₋ at once.

## 1. Exact low-order data

`[ALG]`, gate H1.

Through order z¹⁴ the recursion was run exactly in E:
- L_k = ℓ(k* − k) for every k ≤ 11;
- the invariance residual vanishes identically.

**Curve coefficients** (written as p + q·a with p, q ∈ ℚ(i√3)):
- a₃ = (1/108 − i√3/108) + (−1/6 + i√3/6)a;
- a₄ = (199/19845 + 2603i√3/476280) + (−23/216 + i√3/216)a.

a₅, …, a₇ are listed in the JSON.

**Restricted map** g := F_z(z, φ(z)):

g = z + ℓz⁴ + g₅z⁵ + g₆z⁶ + g₇z⁷ + …, with
- ℓ = (−1/16 + 7i√3/144) + (−½ − 2i√3/3)a;
- g₅ = (−5/144 − i√3/432) + (¼ − 7i√3/36)a;
- g₆ and g₇ are in the JSON.

## 2. P1-c-5c — the fixed-point index of F|Γ±

`[ALG]` / `[THM — SESSION]`, gate H2.

**Definition.** For the formal germ g(z) = z + ℓz⁴ + …, the holomorphic fixed-point index is

ι := Res_{z=0} dz/(z − g(z)) = −[z³](ℓ + g₅z + g₆z² + g₇z³ + …)⁻¹.

It depends only on g₄, …, g₇. These in turn depend only on a₂, …, a₅ and on the degree-≤ 7 part of F, so ι is a finite computation.

**Result.**

ι = 49658905924/263611634013 − (40940212120/790834902039)·i√3 ≈ 0.188379037632 − 0.089665399544i.

- **ι lies in ℚ(i√3).** Its a-component vanishes identically, so the two formal curves φ₊ and φ₋ have the **same** index, even though ℓ₊ = −ℓ₋.
- **Stable under truncation:** the same value is obtained from the order-10 and order-14 recursions.
- **Negative controls:**
  - M1, the wrong orientation Res 1/(g − z), gives a different value, as required;
  - M3, truncating g before z⁷, gives a different value, as required.
- **Résidu itératif.** For multiplicity p + 1 = 4 (p = 3), and using Milnor's convention as I recall it (résit = (p + 1)/2 − ι), the value is 2 − ι ≈ 1.811621 + 0.089665i. The convention is to be checked against the source before the value is quoted anywhere else.
- **Invariance.** ι is a formal-conjugacy invariant of g. It is therefore well defined for the formal germ F|Γ±, whether or not φ± converges.

**Reading** (`[HEUR]`). ι is only the formal datum. It does not decide whether ½ ∈ 𝔅(F|Γ), because a formal half-iterate always exists. The analytic question needs the Écalle–Voronin moduli: three pairs of horn maps for p = 3.

## 3. P1-c-5b — convergence analysis of φ±

### 3.1 Conditional convergence lemma (Briot–Bouquet)

`[THM — SESSION]`; gate H3; uses Lemma (a) of P1-b §3.4, which the review accepted as logically sound.

**Lemma 5b-1.** If X̂ = log F converges, then φ₊ and φ₋ converge.

*Proof.*
1. **Tangency.** Γ± is a formal F-invariant curve, so X̂ is tangent to it (P1-b §3.4(a)): X̂_w(z, φ) = φ′(z)·X̂_z(z, φ).
2. **Substitution.** Put w = z²u. Then:
   - X̂_z(z, z²u) = z⁴·g(z, u), because every monomial z^i w^j of X̂_z has i + 2j ≥ 4;
   - X̂_w(z, z²u) = z⁵·h(z, u), because every monomial of X̂_w has i + 2j ≥ 5 (F_w has no z⁴ term).

   If X̂ converges, g and h are analytic near (0, a₂). The tangency equation becomes z·u′ = f(z, u) := (h − 2ug)/g, with g(0, a₂) = ℓ ≠ 0.
3. **Briot–Bouquet data, exact (H3).** The data are computed from the exact log X̂ (Mercator series, degree ≤ 6):
   - f(0, a₂) = 0. This is the same quadratic as for F, since X̂ and F agree on the monomials involved: X̂₅ − F₅ affects only the (3,2) and (2,3) slots.
   - λ := ∂_u f(0, a₂) = k* − 2 = −102/19 − (16/19)i√3. This is non-real, hence not in {1, 2, …}.
4. **Briot–Bouquet theorem.** The equation z·u′ = f(z, u), with f analytic, f(0, a₂) = 0 and ∂_u f(0, a₂) ∉ ℕ_{≥1}, has a unique formal solution with u(0) = a₂, and that solution converges.
5. **Conclusion.** By uniqueness it equals φ±/z². ∎

**Control.** M2 (λ computed with conj(c₄₀)) fails, as required.

**Corollary (contrapositive).** If φ₊ or φ₋ diverges, then X̂ = log F diverges, i.e. F is not the time-one map of an analytic vector field with zero linear part.
- This would **not** decide B-an. By Lemma S, X̂ diverging does not exclude ½ ∈ S.

### 3.2 Why the majorant method does not give convergence for the map equation

`[HEUR]`; recorded as a failed route, **not** as a divergence statement.

**Expansion.** Write δ(z) := F_z(z, φ) − z = ℓz⁴ + O(z⁵). Then

φ(z + δ) − φ(z) = Σ_{j≥1} φ^{(j)}(z)·δ(z)^j / j!.

The order-(m + 3) equation reads ℓ(k* − m)·a_m = R_m, and R_m has two kinds of terms.

**Denominator.** |ℓ(k* − m)| grows **linearly** in m (exact; §1).

**Numerator, j = 1 part** (the "Briot–Bouquet part"). Its contributions to R_m are bounded by sums of the form Σ k·|a_k|·|δ|_{m+4−k}. By §3.1, this is exactly the structure that converges when F is replaced by the time-one map of an analytic field.

**Numerator, j ≥ 2 parts** (the genuinely discrete part).
- Since δ^j has order 4j, the term φ^{(j)}δ^j/j! contributes, at order m + 3, the coefficient a_k with k ≤ m + 3 − 3j.
- The weight is the falling factorial k(k − 1)⋯(k − j + 1)/j!·ℓ^j, of size about m^j/j!.
- For j = 2 the leading term is about ½(m − 3)(m − 4)ℓ²·a_{m−3}. Divided by the linear denominator, this gives a factor of about (m/2)·|ℓ| per index shift of 3.

**Consequence.**
- A majorant series built on |R_m| inherits a factor growing like m per 3 steps. The best bound this method can give is of Gevrey type, |a_m| ≲ C·K^m·Γ(m/3), not convergence.
- Convergence would need cancellations between the j ≥ 2 terms and the rest, and the majorant method cannot detect them.
- Such cancellations **do** occur when F embeds in an analytic flow (§3.1). So the method fails exactly because it ignores structure, not because divergence has been shown.
- As the review stipulated, this failure is not a divergence proof.

### 3.3 Numerical growth (`[NUM]`, illustration only, no inference)

See §5. These are 80-digit floating-point numbers, not certified intervals.

### 3.4 Routes to a decision on φ±

All `[HEUR]`.

- **Divergence route.** The expected scenario is that φ± is Gevrey of order 1/3 and 1/3-summable (in the variable z³). Its sectorial sums would then be invariant curves on sectors, which should be the parabolic curves of P1-c §1 (cf. López-Hernanz–Raissy–Ribón–Sanz, arXiv:1411.2945, not yet read). φ± converges iff the Stokes constants vanish.
  - A proof of divergence would require a nonzero Stokes constant.
  - A numerical estimate of the Stokes constant from large-order asymptotics would be a strong `[NUM]` indicator, not a proof.
- **Convergence route.** No sufficient criterion was found. The only one known here is Lemma 5b-1, which requires X̂ to converge, itself an open question.

## 4. Consequences for B-an

| Outcome for φ± | Consequence |
|---|---|
| φ± converges | Criterion P1-b §3.4(c) becomes applicable. One must then show ½ ∉ 𝔅(F\|Γ) for the one-variable germ g (multiplicity 4, index ι of §2), via its Écalle–Voronin data. B-an is decided negatively only if that obstruction is proved. |
| φ± diverges | By Lemma 5b-1, X̂ diverges: F does not embed in an analytic flow with zero linear part. B-an is still **not** decided (Lemma S). The invariant-curve route is then closed, and B-an would need a sectorial (parabolic-curve) analysis in ℂ². |

Neither outcome is established.

## 5. Numerical appendix

`[NUM]`, illustration only.

**Run.** `curve_num.py` with 80 digits and truncation N = 40, giving coefficients a_m for m ≤ 37. Output `curve_num_N40.json`; fits `gevrey_N40.json` from `gevrey_fit.py`. Run time 551 s.

**Accuracy.**
- The curve residual is below 10⁻⁸² for both roots.
- L_k agrees with ℓ(k* − k) to below 10⁻⁷⁹.

| | φ₊ | φ₋ |
|---|---|---|
| Root test \|a_m\|^{1/m} at m = 12 / 24 / 36 | 0.488 / 0.540 / 0.660 | 0.557 / 0.652 / 0.694 |
| Ratio \|a_m/a_{m−3}\|, m = 20 … 37 | erratic, 0.07 – 3.2 (phase oscillation) | 0.42 – 0.58, no monotone growth |
| Fit log\|a_m\| ≈ α·m log m + βm + γ | α = 0.49 (m ≥ 10), 0.52 (m ≥ 16), 0.26 (m ≥ 22): unstable | α = 0.06, −0.05, −0.30: unstable |
| Baseline: F itself, max\|F_{ij}\|^{1/d} | about 0.92 – 0.98 | (same) |

**Observations** (no inference drawn):
- Up to m = 37 there is no clear Gevrey-1/3 signature.
- §3.2 predicts, for the j = 2 terms alone, a factor of about (m/2)|ℓ| ≈ 0.049m per 3 steps. That factor exceeds 1 for m ≳ 20. For φ₋ the observed 3-step ratios stay at 0.4–0.6 up to m = 37; for φ₊ the ratios are dominated by phase oscillation.
- The root tests are still rising slowly and remain below the baseline of the convergent F.
- These data neither establish convergence nor rule out divergence. If the asymptotic regime exists, it may set in only beyond m ≈ 40. Any further numerical step belongs to the P2 decision (P1-c-5d).

## 6. Proposed next steps

Each needs its own decision.

| Step | Content |
|---|---|
| P1-c-5d | Large-order asymptotics of a_m, to about m ≈ 100, with interval arithmetic: test the Gevrey-1/3 hypothesis and estimate a Stokes constant. Recommended on the PI machine; this is part of the P2 campaign decision |
| P1-c-2 | Abate 2001, Abate–Tovena and López-Hernanz–Raissy–Ribón–Sanz: original statements and hypotheses |
| P1-c-6 | If useful: the Écalle–Voronin data of the one-variable model z + ℓz⁴ + … with index ι, as a calibration for the ½ ∈ 𝔅 question |

**Status:** DYAD v6.4.18 adopted; OPEN 20 PARTIAL; B-an and B-6 OPEN. Everything above is SESSION material.
