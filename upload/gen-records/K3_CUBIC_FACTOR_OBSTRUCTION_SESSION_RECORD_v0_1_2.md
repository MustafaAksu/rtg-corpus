# K3-CUBIC-FACTOR-OBSTRUCTION — SESSION proof record v0.1.2

**Date:** 16 October 2026
**Lifecycle:** `[SESSION]` noncanonical proof record. Mathematical ownership: Genesis Geometry (accepted). No owner integration; adopted Genesis v2.8.5, RRF v0.8, OFN v0.9 and Dyadic v6.4.11 are unchanged.
**Status:** `[THM — exact, conditional on the named model]`. Physical realization / admissibility: `[OPEN]`. Accepted for Genesis owner review (Stage A), 16 Oct 2026.
**v0.1.1:** source pin to adopted Dyadic v6.4.11 (SHA-256 `6fccd429758adb729032a68c2a99e24a7bab6f5226aae5df1453b09b189ccb2e`); primitive cited as `DYAD-DEF-PRIMITIVE-MAP` (Genesis alias `GEN-DEF-PRIMITIVE-MAP`, recognition pending N1); relation to `DYAD-THM-LOCAL-INVOLUTION-GERM` recorded (§5a). No mathematical change.
**v0.1.2:** lifecycle line repinned to Dyadic v6.4.11; §5a reworded as an analogy (no derivation); §4 adds the other target dimensions (d = 1, 3 already at C¹).

---

## 1. Statement

**Model.** Let T be the selected primitive [RID: DYAD-DEF-PRIMITIVE-MAP, Dyadic v6.4.11 §1; Genesis alias GEN-DEF-PRIMITIVE-MAP], T(ρ,η) = (ρ − sin η, η + e^ρ − 1 − sin η), written in the eigenframe W = ρ − η/2 + i(√3/2)η. Let 𝒞 = {(w₁,w₂,w₃) : w₁+w₂+w₃ = 0} ≅ ℂ², and let

  F₁ = P_𝒞 ∘ T^{×3}

be the projected K3 primitive map: apply T to each edge, then subtract the mean. Then DF₁(0) = A⊕A, where A acts as multiplication by λ = e^{iπ/3}.

**Theorem.** There is no pair (T', E) with all of the following:
- T' is a C³ map of a two-dimensional manifold;
- E is a C³ submersion from a neighbourhood of 0 ∈ 𝒞 onto it;
- E ∘ F₁ = T' ∘ E holds near 0.

No hypothesis is placed on the fixed point, the linearization or the cubic coefficient of T'.

## 2. Proof

**(a) Fixed point and linear part are derived.** Set p = E(0). Then T'(p) = E(F₁(0)) = p. Let ℓ = DE(0); it is surjective because E is a submersion. Differentiating gives ℓ(A⊕A) = DT'(p)ℓ.

ker ℓ is a real 2-plane invariant under λ-multiplication. Because λ ∉ ℝ, that plane is a complex line. DT'(p) is the map induced on the quotient by that line, so it is multiplication by λ in a suitable real coordinate centred at p. That makes DT'(p) conjugate to A, and ℓ complex-linear in that coordinate. (If the coordinate reverses orientation, conjugate it; the equations below keep their form, with C replaced by C̄.)

**(b) Leading-term lemma.** Let G be C³ with DG(0) = R, where R⁶ = I, and let P = G⁶ = id + p_k + o(|x|^k), commuting with G. At degree k, p_k(Rx) = R p_k(x), because Dg₂(x)·p_k(x) has degree k+1.

For λ = e^{iπ/3}:
- no quadratic map is equivariant (its characters are λ^{±2} and λ⁰), so p₂ = 0;
- the only equivariant cubics are y ↦ C y|y|² on the plane, and maps of the form Σ c z_i z_j z̄_k on ℂ².

This applies both to F₁⁶ = id + f₃ + O(4) and to T'⁶ = id + C y|y|² + o(|y|³), in every C³ chart. No normalizer is used.

**(c) Cubic factor identity.** From E ∘ F₁⁶ = T'⁶ ∘ E, with E = ℓ + E₂ + E₃ + o(3): the E₂ and E₃ terms cancel at degree 3, because E₂(x + f₃) − E₂(x) = O(4). What remains is

  ℓ(f₃(x)) = C ℓ(x)|ℓ(x)|²,  with C ∈ ℂ unrestricted.

**(d) Source cubic.** The exact six-step cubic is

  f₃,e = ν(w_e|w_e|² − ⅓Σ_j w_j|w_j|²) + (2iχ/3)(w_{e+1} − w_{e−1}) Im(w₁w̄₂),  ν = 1/6 − i√3/3, χ = 1/3.

Take the chiral modes u = w₁ + λw₂ and v = w₁ + λ̄w₂, and set N = Σ|w_e|². Then:
- N = |u|² + |v|²;
- u(f₃) = c₀ u|u|² − iβ* N u;
- v(f₃) = c₀ v|v|² − iβ* N v;
- c₀ = 1/6 + i√3/9 and β* = 2√3/9.

**(e) Elimination.** Write ℓ = αu + βv and compare monomials in (c).
- u²v̄: the left side has none; the right side has Cα²β̄. Symmetrically for v²ū, Cβ²ᾱ = 0.
- If C ≠ 0, then αβ = 0. Take β = 0, α ≠ 0. The u|v|² coefficient is −iβ*α on the left and 0 on the right, so β* = 0, a contradiction.
- If C = 0, the left side must vanish. Its u|v|² and v|u|² coefficients are −iβ*α and −iβ*β, so α = β = 0.

Hence ℓ = 0, which contradicts surjectivity. ∎

**Structural reading.** The obstruction is the nonzero chiral phase coupling β*, through the term N = |u|²+|v|², which couples the two chiral modes. It is not a radial-sign mismatch and not a normalizer artefact. Each |u|² and |v|² is autonomous at cubic order, so the radial data factor; the phases do not.

## 3. Evidence

| Component | Role | Identity |
|---|---|---|
| `k3_obstruction_exact_check.py` | Exact f₃ derived from the primitive (no imported jet): six-step return tangent to identity, quadratic term zero, closure, ER-2B (ν,χ) match on every edge, N = \|u\|²+\|v\|², both chiral identities, β* ≠ 0. 8/8 PASS; χ=1/4 negative control fails (exit 1). Run independently by co-owner, unchanged. | SHA-256 `384aaa5f17ecd0786960b3a97fc08a5d332c9e12809a2c92796616f2615a01ee` |
| §2(e) monomial comparison | Proof of the planar no-go for every C³ target | this record |
| `fac.py` (Gröbner, real elimination a=x+iy, c free) | Separate algebraic confirmation: basis [x₁,y₁,x₂,y₂] | SHA-256 `91608cb7b92bda2f3678f0fc022a6ebc8398de5ea198ef208338066be7587f2b`; package `K3_factor_obstruction.zip` `046ac458e9a2a3e82a9fed14d52350f875ddb69bdf94fd4b5767a113bae585cc` (no internal manifest; not rerun here, sympy unavailable) |
| `exact_chiral.py` | Original chiral identity (sympy) | SHA-256 `e5e268a6b9d53f6c692e4f6d25dd0bae044597ea1ccc938802f5798a1459af7d` |
| `k3.py` | `[NUM]` cubic of the untruncated map; fit s=1, γ=0 (rel. resid 5·10⁻⁹); dyad cross-check μ_num = −1/2 − 2i√3/3 = μ₆. Its rotation-averaging is harmless by lemma (b). | SHA-256 `dcb08a273ebc3a6a46c1314eaf42337f1f74825de7732eeab435a3a3e1ef1038` |
| ER-2B Observable Response v1 | Historical first source of (ν,χ); companion local-outflow result ΔN = ⅙N² + 2S² | `ER2B_OBSERVABLE_RESPONSE_v1.zip` `06d5e0c90d864ee8f5ab5ecfa7cadac5e76272a0b4754955bf43ecdcbc4b82b1` |

## 4. Scope and OPEN

- **Other target dimensions.** No nontrivial local submersive factor of strictly lower real dimension d exists. For d = 1, 3 this already holds at C¹: ker DE(0) would be a real λ-invariant subspace of odd dimension, and since λ ∉ ℝ every such subspace is complex, hence even-dimensional. For d = 2 the present proof needs C³ (§2). The C¹/C² OPEN below therefore concerns d = 2 only.
- **Covered:** every local C³ planar target. The fixed point, linearization and the cubic coefficient C are free; no value of C removes the obstruction.
- **Not covered:** C¹/C² factors with d = 2; targets of dimension ≥ 3; other network or incidence dynamics; other carriers (including the formal odd carrier, aday B); the physical node-exchange action.
- **Not to be confused with:** RER observable-preserving minimum-dimension theorems. This result excludes a dynamical factor of the primitive projected map, which is a different statement.

## 5. Consumers

- **RRF / G2-CLOCK:** in any admissibility class that requires a planar primitive factor, the raw projected K3 is excluded. This does not select a node-exchange action, does not exclude every network–dyad bridge, and does not accept aday B physically.
- **Genesis:** candidate for the next scientific successor, after owner review. Companion reading for the Interpretation field: the isolated dyad contracts (Re μ₆ < 0), the projected triad has local radial outflow, and no C³ planar factor connects them.

## 5a. Relation to DYAD-THM-LOCAL-INVOLUTION-GERM (Dyadic v6.4.11 §6.15)

Independent results; neither proves the other, and this theorem is **not** derived from §6.15. The comparison below is an analogy only. §6.15 classifies local involutions of the 2D dyad commuting with T or T⁶. This record excludes 2D factors of the 4D projected network map. They show a parallel mechanism: at the six-step clock DF⁶(0)=I removes linear selectivity, and the cubic chiral term restores it (Im μ ≠ 0 in §6.15(b); β* ≠ 0 here). The cubic-comparison step of §2(b–c) was written independently. It happens to use the same o(|·|³) remainder discipline as §6.15(b) after its r3 correction R2-02.

## 6. Remaining provenance item

`K3_factor_obstruction.zip` has no internal manifest. Its producer should add file hashes and an execution receipt for `fac.py`. That item is confirmatory only and does not gate the theorem: the proof is §2, and its source data are certified by the hashed exact script.
