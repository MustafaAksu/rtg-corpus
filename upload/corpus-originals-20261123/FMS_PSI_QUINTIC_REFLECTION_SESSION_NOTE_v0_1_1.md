# FMS — ℤ₂ Reflection Test: m(a) Is a Complete Degree-5 Invariant of the Chart Family v0.1.1

**v0.1.1 (19 Oct 2026):** §4 corrected per the FMS review. |c| determines m only up to the reflection; the full classification also needs the reflection obstruction. The theorem and the evidence are unchanged.

**Date:** 19 October 2026 · **Status:** `[SESSION]`, noncanonical. Not owner-adopted; no DSN is modified.
**Answers:** FMS §12E follow-up ("is the reflected pair conjugate?") and OFN v0.8 §4, test 4.
**Builds on:**
- `FMS_PSI_QUINTIC_FINITE_INVARIANT_SESSION_NOTE_v0_1.md` (|c|² invariant, Stab(f₃) = T² ⋊ swap, exact degree-5 linearity);
- `FMS_PSI_QUINTIC_PHASE_INVARIANT_SESSION_NOTE_v0_1.md`.

## 1. Method

Any formal conjugacy has the form φ = B∘ψ, with B ∈ Stab(f₃) = T² ⋊ ⟨swap⟩ and ψ tangent to the identity. At degree 5 the effect of ψ is exactly linear: f″₅ = f₅ + L₃(ψ₃). So f_b ≅ f_a through degree 5 **iff** some B satisfies

  (B⁻¹ f_b B)₅ − f_{a,5} ∈ Im L₃.

**Reduction to a polynomial system.**
- B is a torus element diag(e^{iα}, e^{iβ}) in chiral coordinates, possibly composed with the swap.
- It acts on λ-equivariant quintic monomials only through the characters w^k and w^k z, where w = e^{i(α−β)} and z = e^{−6iβ}.
- The left null space of L₃ has dimension 49. Imposing it turns the condition into a system of Laurent polynomials in (w, z) with coefficients in ℚ(√3, i). This is solved exactly by Gröbner bases with the domain pinned to ℚ(√3, i).

## 2. Results `[SESSION — ALG, exact]`

| Test | Result |
|---|---|
| (P1) κ = 1, a = 0, b = (17√3/513)·iμ, the exact reflected pair (\|c_a\| = \|c_b\|, c_b = c̄_a) | Gröbner basis **[1]** with and without the swap ⇒ **not conjugate** |
| (P2) Control: identical pair | basis (w³ − 1, z − 1): solvable, and recovers the cyclic S₃ symmetries |
| (P2) Control: f_b = diag(λ, 1)·f_a·diag(λ, 1)⁻¹ | basis (w³ + 1, z − 1): solvable, and recovers the conjugating element |
| (P3) Symbolic family a = r·iμ with its reflected partner b, at t ∈ {0, 1, −1/2} | the elimination ideal in r is linear, with single root **r\* = the reflection fixed point** (a = b) |
| (P4) r **and** t symbolic | elimination ideal in (r, t) = ⟨1026r − 17√3 − 72√3·t⟩, which is **exactly the fixed-point line m(a) = m\*(t)**. An elimination-ideal element is a necessary condition for any solution, so there are no specialization gaps |

A numerical torus scan (361² grid plus refinement) found a minimum residual of 2.2·10⁻³ for the reflected pair. A positive control at a known conjugating B gave 6·10⁻¹⁶. This scan is confirmatory only and is not part of the certificate.

## 3. Consequence

**Structure of f₅.**
- The degree-5 part of the chart family is real-affine in a. This follows from the same exact-linearity argument, with g₃ = a z²z̄ in place of ψ₃, and was checked as bilinear in (r, t).
- It vanishes along ℝμ.
- So f_{κ,a} at degree 5 depends on a **only through m(a) = Im(aμ̄)**.

Combining |c|² (finite-invariant note) with P4:

> **Theorem (SESSION).** For every κ ∉ {0, 2}, and for κ = 2 in the odd category, the reduced maps f_{κ,a} and f_{κ,b} are formally conjugate through degree 5 **if and only if m(a) = m(b)**. Within the transported chart family, the real number m(a) is a complete degree-5 formal invariant.

- **"If":** the reduced 5-jets are identical.
- **"Only if":** for m(b) ≠ m(a), either |c| differs, or b is the reflection of a and P4 excludes it.
- **Full transported models:** by step (g) of the completeness lemma, the "only if" direction carries over for κ ∉ {0, 2}.

This closes the ℤ₂ item. The finite-a classification of the chart family at degree 5 is now complete.

## 4. Limits

- **Degree 5 only.** Higher jets may add further obstructions, but they cannot remove this one. Conjugacy at degree 5 for m(a) = m(b) is trivial, since the jets are identical.
- **Only the chart family g_a is classified.** The 7 other first-order moduli of the general S₃ quintic class are not reached by charts, and their classification is not attempted.
- **Excluded parameters:** κ = 0, and κ = 2 for general (non-odd) conjugacies.
- **Physics.** m(a) is a mathematical modulus. Its physical reading and selection remain `[OPEN — OFN/RRF]`.
- **Correction (v0.1.1, per FMS review).** |c| does **not** determine m completely. Given κ, |c| fixes m only up to the reflection m ↦ 2m* − m. The complete degree-5 classification uses |c| **together with** the reflection obstruction (P4), which comes from the remaining quintic data, not from c. |c| therefore remains a conjugacy-invariant **candidate** readout, but it is not a full numerical readout of m. The sign of m − m* is not readable from |c|. A torus-invariant scalar that reads it has not yet been constructed `[OPEN]`.

## 5. Evidence

| File | SHA-256 | Result |
|---|---|---|
| `FMS_PSI_QUINTIC_REFLECTION_TEST_v0_1.py` | `5af23da97e0d39bf9160c8263575fd9eed00b857d01fcab613e403b3254bf409` | P1–P4 ALL PASS, exit 0, ~35 s. Needs `FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py` and `FMS_PSI_QUINTIC_KAPPA_ALL_v0_1.py` in the same directory; uses sympy |
