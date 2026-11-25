# Triadic / RER C09 — receiving review of formal age-family result

**Date:** 2026-10-09  
**Status:** NONCANONICAL; conditional Genesis analytic modal map, one-time birth contract A. No adopted DSN/RRF or physical-model state modified.

## Received artifacts and provenance

- Contributor note: `RER_C09_INDEPENDENT_VERIFICATION_20261009 (3).md` (SHA-256 `94b48b732e99af8ed980187d21acaa2b68f416626b9cb41bb60c965698480137`). §8 is the new proposed result; §6's earlier tau-update statement is explicitly withdrawn in §7.
- Checker: `triad_formal_age_family_check.py` (SHA-256 `5bc3494dae0d4cb390dbe4946382d8d3bbe1167d0613dafc0a34dde48d4f98e1`).
- Source implementation: `c09_independent_series_check_rev2.py` extracted *without editing* from archived `TRIAD_C09_TAU_RECEIVING_20261009.zip` (SHA-256 `67b2e0e785dd30a1bd637c79db2a7210d93516b79f5a00d5fb8233da04f6799b`).

## Receiving disposition

**[ALG, formal — accepted with scope corrections].** Let `F` be the **named** six-step, reproject-after-each-step Genesis analytic modal map, in its formal germ about zero, and let `C_κ(s)=κ Q(s) J_Q s` be the trial birth graph. The only model properties used by the general construction are

1. `F(0)=0` and `F(X)=X+O(||X||^3)`;
2. `F_c(s,0)=0` (the child-free graph is invariant);
3. `C_κ(s)=O(||s||^3)`.

The age-`n` graph `c_n(s)` is the graph of `F^n(graph C_κ)` over current parent `s`, defined as a formal germ. At every homogeneous `s`-degree `d`, its coefficient is polynomial in `n`. A sharper admissible bound is

`deg_n [c_n]_d <= floor((d-3)/2)` for `d>=3`, with `[c_n]_3=C_κ`, independent of age.

This corrects the contributor's unqualified `<=d-4`, which is not meaningful at `d=3`; the latter is a valid weaker bound for `d>=5`.

**Independent structural proof (no coefficient interpolation assumption).** In the completed local algebra `A=R[[s_1,s_2,c_1,c_2]]`, write `U=F^*` for substitution and `N=U-I`. Because `F-Id=O(3)`, `N` raises total filtration degree by at least two. Therefore

`U^τ := sum_{k>=0} binom(τ,k) N^k`

is a valid formal operation, with coefficients polynomial in `τ` at every fixed state degree. On nonnegative integers it is exactly `(F^*)^n`. Each coefficient of `U^τ(fg)-U^τ(f)U^τ(g)` is polynomial in `τ` and vanishes at every nonnegative integer, so it vanishes identically. Thus `U^τ` is a formal algebra automorphism. By the binomial identity `U^τ U^σ=U^{τ+σ}`. These operations define formal fractional iterates `F^τ` without claiming a convergent flow.

Define `(S_τ(s_0),Z_τ(s_0)):=F^τ(s_0,C_κ(s_0))`. Since `D_{s_0}S_τ(0)=I`, it has a formal inverse `s_0=S_τ^{-1}(s)`. Set

`C(s,τ):=Z_τ(S_τ^{-1}(s))`.

Then `C(s,n)=c_n(s)` for every nonnegative integer `n` and

`F(s,C(s,τ))=(s^+,C(s^+,τ+1))`, `s^+=F_s(s,C(s,τ))`,

**as a formal power-series identity**. `C(s,τ)` is unique among series whose coefficients in `s` are polynomials in `τ` and which agree on all integer ages. This does **not** make it unique in larger smooth/nonpolynomial interpolation classes.

The filtration bound follows because `F_c(s,0)=0` keeps the child-coordinate ideal invariant. Each application of `N` raises degree by at least two, and substituting the cubic birth graph raises the order of terms carrying a child factor. Formal inversion of `S_τ` preserves the bound. Consequently the age-degree at `s`-degree `d` is at most `floor((d-3)/2)`.

## What the result does *not* show

- It is not a proven convergent, analytic, or actual smooth three-dimensional invariant manifold for the full six-step map.
- It does not contradict the earlier no-regular-`C^1`-three-fold-through-the-origin theorem: `∂_τ C(0,τ)=0`, so the parametrization is singular there.
- `τ+=τ+1` is a **formal interpolation coordinate**, not a measured event clock, physical memory, or autonomous age recovery from physical observables.
- It is a formal invariant *parameterization/semiconjugacy* of the reachable age sheets, not an observable-preserving two-dimensional factor.
- The `w_13` curvature obstruction persists against **affine-in-τ child fibres at fixed parent**; it is compatible with a curved formal `C(s,τ)`.
- “Every other τ is a reparameterization” is too broad absent the requirement that both charts parameterize the same family with invertible changes. Nonpolynomial interpolants can agree at all integers yet differ between them.
- The exact source remains the conditional analytic modal map, **not** a physically selected standalone-K3 law. Uniform-in-age control, radius of convergence, domain away from zero, and physical birth/event acceptance remain OPEN.

## Receiving execution

The attached checker uses the actual full sin/exp map as exact rational **truncated series**, not the G3/G4 jet alone. It tests polynomial age interpolation on three ray/κ combinations, and noninteger τ=1/2, -1/3, 5/2 up to t^12. These are *finite-order sampled tests*, not a general all-orders theorem; the structural proof above supplies the latter at formal-series scope.

See `positive.log` and `negative.log` for the exact rerun receipts. Hash and provenance above apply to the untouched original script/source bytes; no source scientific owner document was edited.

## Suggested RER handling

Preserve C09. Add §8 as a **noncanonical, model-specific formal-series supplement** rather than silently promoting it to an exact analytic factor theorem. Keep any new scientific RID and physical interpretation unselected. The next meaningful problem is convergence/admissible-domain control of the formal suspension, or an explicitly defined observable-preserving factor on the actual reachable union, not another arbitrary clock parametrization.
