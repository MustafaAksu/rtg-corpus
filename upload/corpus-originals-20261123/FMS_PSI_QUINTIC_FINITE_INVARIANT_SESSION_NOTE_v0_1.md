# FMS — |c|² as a Formal Conjugacy Invariant: Finite-a Separation up to a ℤ₂ Reflection v0.1

**Date:** 19 October 2026 · **Status:** `[SESSION]`, noncanonical. Not owner-adopted; no DSN is modified.
**Answers:** FMS v0.6.4, research item 1: prove invariance of c under finite and general formal conjugacies, or find a counterexample.
**Builds on:** `FMS_PSI_QUINTIC_PHASE_INVARIANT_SESSION_NOTE_v0_1.md` and the completeness lemma in `FMS_PSI_QUINTIC_MODULUS_SESSION_NOTE_v0_1_1.md`.

## 1. Result

**c itself is not invariant under every formal conjugacy, but |c|² is.** The **phase** of c can be rotated by the relative-phase torus.

### Proposition `[SESSION — ALG; exact checks of finite-dimensional steps]`

**Hypotheses.**
- f and f′ are odd reduced maps, λ-equivariant and S₃-equivariant.
- They have the same cubic f₃ (chiral form p′u|u|² + q′|v|²u with p′ = n₂₁/3 and q′ = 2p′).
- φ is **any** formal conjugacy, φ∘f = f′∘φ. It need not be S₃-equivariant, need not be first order, and need not be tangent to the identity.

**Conclusion.** |c(f′)| = |c(f)|.

### Proof

1. **Split φ.** By the completeness lemma, φ = B∘ψ with B ∈ Stab(f₃) complex-linear and ψ tangent to the identity, ψ₂ = ψ₄ = 0, ψ₃ equivariant.
2. **Exact linearity at degree 5.** ψ conjugates f to f″ = B⁻¹f′B. Since the linear part is the scalar λ, the quadratic ψ₃–ψ₃ terms cancel at degree 5:
   - the λ·(Dψ₃·ψ₃) term from ψ⁻¹ cancels −Dψ₃(λw)·λψ₃ = −λ·Dψ₃·ψ₃;
   - non-equivariant ψ₅ vanishes;
   - equivariant ψ₅ commutes with λ.

   Therefore **f″₅ = f₅ + L₃(ψ₃) exactly**, not only to first order. c_A and c_B (the u³v̄³ coefficients in Δ₆|u|² and Δ₆|v|²) depend only on the 5-jet.
3. **No equivariant cubic generator moves c.** The check covers all 24 real equivariant cubic generators, **including non-S₃ ones**, each at two finite scales, plus a large random non-S₃ finite conjugacy. c_A and c_B are exactly unchanged in every case. Hence c_A(f″) = c_A(f) and c_B(f″) = c_B(f).
4. **The stabilizer acts by a phase.**
   - The Lie algebra of Stab(f₃) is the diagonal phase torus, with real dimension 2 (exact null-space computation).
   - The identity component is normal in Stab(f₃), and its normalizer in GL₂(ℂ) is the monomial group. Because p′, q′ ≠ 0, the entries must have unit modulus. So **Stab(f₃) = T² ⋊ ⟨swap⟩**.
   - For B = diag(e^{iα}, e^{iβ}), c_A ↦ e^{3i(β−α)}c_A. Checked directly: diag(λ, 1) and diag(1, λ) give −c; diag(λ², 1) gives +c.
   - For the swap, c_A ↦ conj(c_B), and conj(c_B) = c_A for S₃ maps.

   In every case c_A(f′) = (unit phase)·c_A(f). ∎

## 2. Consequence for finite a

For f_{κ,a} the real part Re c = −1/486 + 7t/648 is fixed by κ. Therefore:

> **f_{κ,a} and f_{κ,b} are not formally conjugate (by any formal conjugacy) unless Im c(b) = ± Im c(a).**

Equivalently, write m(a) = Im(aμ̄) and m* = 17√3/648 + √3·t/9 for the chart where Im c = 0. Conjugacy is possible only if

  **m(b) = m(a)  or  m(b) = 2m* − m(a).**

**What is now covered.**
- FMS's open item "finite-a pairwise inequivalence" is settled, up to a single ℤ₂ reflection about the distinguished chart m*.
- The scope is no longer first-order or S₃-only. It covers all formal conjugacies of the reduced maps.
- Via lemma step (g), it extends to the full transported models for κ ∉ {0, 2}.

**What remains open.**
- Whether the reflected pair is actually conjugate. That would require a relative-phase element with e^{3iγ} = c̄/c that also matches the other 7 first-order moduli. `[OPEN]`
- The case m(b) = m(a) with b − a ∉ ℝμ: c does not separate it. Whether it is separated is a question for the other moduli, not for c.

## 3. Grade and limits

**Grade.** `[SESSION — ALG]`. The structural steps (1, 2 and the monomial-normalizer argument) are proofs. Step 3 and the torus/swap actions are exact finite-dimensional computations over ℚ(√3)(i).

**Not covered:**
- κ = 0;
- κ = 2 for general conjugacy (the odd category is covered, as in Ledger §12C);
- orders beyond the 5-jet;
- analytic or C^∞ conjugacy (note that formal non-conjugacy implies non-conjugacy in those categories);
- physical observability, which remains `[OPEN — OFN/RRF]`.

**Physical reading.** A consequence of the torus action: in a declared carrier, **only |c|, the sin/cos-3θ harmonic amplitude, is a candidate observable.** The phase of c is representation-dependent, so the "Im c = 0" chart has no special status under general conjugacies. It is distinguished only within the S₃-preserving class. This supports FMS's reservation about using Im c = 0 as a normalization principle.

## 4. Evidence

| File | SHA-256 | Result |
|---|---|---|
| `FMS_PSI_QUINTIC_FINITE_INVARIANT_v0_1.py` | `ad44f66a2fa083bb93d8194f4fdf2ff200eb965d0dfd9e02e773dd72d5445f4c` | 8 checks (E/F/G), ALL PASS, ~35 s. Needs `FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py` in the same directory; uses sympy |
