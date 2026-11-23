# FMS — Quintic ψ-Modulus of the Transported κ-Family: Completeness Lemma and All-κ Result v0.1

**Date:** 19 October 2026 · **Status:** `[SESSION]`, noncanonical. Not owner-adopted; no DSN is modified.
**Answers:** FMS review of 19 Oct (`ACCEPT SCOPED — EXACT COMPUTATION VERIFIED`), requests (i) a completeness lemma for the allowed generators, (ii) "for which κ is the quintic obstruction ≠ 0?".
**Builds on:**
- `FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py` (`550adcb8…e7eb`), the κ = 1 test;
- `OFN_PSI_KAPPA_EXTENSION_v0_1.py` (OFN co-owner), which supplies the centre-manifold reduction ψ₃ and the sampled-κ result.

## 1. Setting

**Transported family.**
- N is the λ-equivariant one-step DYAD normal-form jet through degree 5 (`DYAD-ALG-NF6`: n₂₁, n₃₂, n₀₅).
- g_a(z) = z + a z²z̄ is the only λ-equivariant cubic chart change. An equivariant quintic g₅ drops out at degree 5.
- N_a = g_a⁻¹ N g_a, and the model is F_{κ,a} = P_κ ∘ N_a^{×3} on ℂ³.

**Reduced map.**
- For |1 − κ| ≠ 1, i.e. κ ∉ {0, 2}, the closure mode is hyperbolic and has no resonance with the centre characters. The formal centre manifold h = ψ(u) is therefore unique.
- Since N has no even terms, ψ₂ = 0. The cubic term is ψ₃ = t · (n₂₁/3) λ̄ Σ_e c_e² c̄_e, with t = (1 − κ)/κ. This was verified by direct three-edge construction at κ = 1/2, 7/5, 3.
- The reduced map is f_{κ,a} = λ-equivariant, with linear part λI. Through degree 5 it is f_{1,a} + t·E, where E is a-independent (OFN script).

## 2. Lemma (completeness of the generator set through degree 5) `[SESSION — ALG]`

Let f and f′ be formal real maps of (ℂ², 0), both commuting with multiplication by λ = e^{iπ/3}, with linear part λI, the same cubic f₃, and no even-degree terms. Suppose φ is a formal real diffeomorphism with φ∘f = f′∘φ. Then:

(a) **Linear part.** B = Dφ(0) commutes with λI, so B is complex-linear. Comparing cubic terms gives B∘f₃∘B⁻¹ = f₃, so B ∈ Stab(f₃).

(b) **Reduce to tangent-to-identity.** Write φ = B∘ψ with ψ tangent to the identity. Then ψ conjugates f to f″ = B⁻¹f′B. The map f″ has the same cubic and is still λ-equivariant and odd.

(c) **Degrees 2 and 4.** The homological operator is ℒψ_k = λψ_k − ψ_k∘λ. On a monomial w^α w̄^β with |α| − |β| = m it acts by the factor λ − λ^m.
- At degree 2 the right-hand side is 0. Since m ∈ {2, 0, −2} and m ≢ 1 (mod 6), every factor is nonzero, so ψ₂ = 0.
- At degree 4, with ψ₂ = 0 and no even terms in f, the right-hand side is again 0. Every quartic character is even, so ψ₄ = 0.

(d) **Degree 3.** ℒψ₃ = f″₃ − f₃ = 0, so ψ₃ is λ-equivariant.

(e) **Degree 5.** The equation is ℒψ₅ + [Df₃·ψ₃ − Dψ₃(λw)·f₃] = f″₅ − f₅.
- The ℤ₆-averaging projector Π commutes with ℒ.
- ℒ vanishes on equivariant ψ₅ and maps non-equivariant terms to non-equivariant terms.
- f, f″ and ψ₃ are all equivariant.

Applying Π therefore gives exactly the tested equation
  **f″₅ − f₅ = Df₃·ψ₃ − Dψ₃(λw)·f₃, with ψ₃ equivariant,**
and ψ₅ plays no role.

(f) **Stabilizer.** B enters through f″ = B⁻¹f′B. To first order in the chart parameter a, the connected component of Stab(f₃) contributes the commutator directions [Φ₁, f] with Φ₁ ∈ Lie Stab(f₃). These are exactly the scripts' Φ₁ columns, including the degree-3 constraint.

(g) **Full maps.** A formal conjugacy of the full six-real-dimensional maps sends the unique formal centre manifold to itself. An obstruction for the reduced maps is therefore an obstruction for the full transported models.

**Consequence.** Within "first order in a, connected component of the linear stabilizer", the linear system of the scripts is the complete degree-5 formal conjugacy condition. The excluded generators cannot change the obstruction space:
- Φ₂ and Φ₄ vanish;
- Φ₅ drops out;
- non-equivariant parts drop out.

**Not covered:**
- finite a (nonlinear dependence on a);
- discrete stabilizer components: the S₃ permutations and the u ↔ v swap. These are isolated and cannot absorb a continuous one-parameter family near a = 0, but they are not treated as a classification;
- orders beyond 5;
- analytic or C^∞ conjugacy.

## 3. All-κ result `[SESSION — ALG, exact]`

**Where κ enters.** κ enters only through t, and only in the stabilizer columns.
- The Φ₃ block depends on f₃ alone, which is κ-free.
- The obstruction vector b = δ₅(a = iμ) is κ-free, because E is a-independent.

**Computation.**
1. Project out the Φ₃ block: rank 23, with a left null space of dimension 73.
2. The projected stabilizer block Q·Φ₁(t) has 8 columns. Together with Q·b, a 9 × 9 minor is
   **det = 8115129463·√3 / 373805638912038666240**,
   a **nonzero constant in t**.
3. So rank[QΦ₁(t) | Qb] = 9 > 8 ≥ rank QΦ₁(t) for every t.

**Result.** For **every κ ∈ ℝ ∖ {0, 2}**, the direction a ∈ iℝμ is a genuine quintic formal modulus of the transported class. There is no exceptional κ.

Together with the OFN check that N_a = N **identically** through degree 5 for a ∈ ℝμ, the cubic chart freedom a ∈ ℂ = ℝμ ⊕ iℝμ splits as:

| Direction | Status through degree 5 |
|---|---|
| a ∈ ℝμ | **trivial**: the same single-dyad map at this order. This is the Cent(N) clock-gauge, and the models coincide, not merely conjugate. |
| a ∈ iℝμ | **modulus**: not formally conjugate, for all κ ∉ {0, 2} |

**Excluded values.**
- κ = 0: ψ₃ has a pole, so the centre manifold fails (consistent with Ledger §5.1).
- κ = 2: |1 − κ| = 1, the closure mode is neutral and the reduction to ℂ² does not apply. This case stays `[OPEN]`.

## 4. Reading and limits

**The class carries a modulus.** The transported class is a one-real-parameter family of formally inequivalent models at quintic order, not a single model up to formal conjugacy. Choosing the chart ψ inside the class is therefore a choice with dynamical content. It is not pure gauge, except along the ℝμ clock direction.

**What this does not establish:**
- physical distinguishability;
- an observable that reads the modulus;
- realization: J and its existence are DYAD OPEN 20;
- which value OFN/RRF should select.

**Next step.** If useful: identify the modulus as an explicit invariant, for example a cokernel functional evaluated on δ₅, and express it through a readout already in the corpus, for instance a correction to the shape law at order (A + B)². That would turn "a modulus exists" into a readout OFN/RRF can name.

## 5. Evidence

| File | SHA-256 | Result |
|---|---|---|
| `FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py` | `550adcb8865246ec54f5094dd9e0f586f54bb638347164faff62309d9059e7eb` | κ = 1; 6/6 PASS; independently rerun by FMS |
| `OFN_PSI_KAPPA_EXTENSION_v0_1.py` | project file (OFN co-owner) | ψ₃ reduction; N_a = N for a ∈ ℝμ; obstruction at sampled κ |
| `FMS_PSI_QUINTIC_KAPPA_ALL_v0_1.py` | `2849e32f172243833794f754b7df37486f6ace826104777574024448b370013e` | constant nonzero 9 × 9 minor in t ⇒ all κ ∉ {0, 2}; exit 0. Needs the first script in the same directory |
