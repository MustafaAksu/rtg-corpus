# DYAD–RRF–OFN G2 Consolidated Note v0.1

**Date:** 16 October 2026 · **Status:** NONCANONICAL working note; no owner file, RID, OPEN status or custody changed.
**Contributors:** Mustafa (PI; G1 formal proof, κ-family argument), ChatGPT (reviews, formal group-closure proof via T⁶ ≠ I, interacting group-closure construction), Claude (uniqueness lemma, edge-slot symmetry result, D_Ŝ/Standard-B synthesis, symmetric transported-carrier construction).
**Intended receivers:** DYAD (technical owner of §§1–4), RRF (carrier/representation evaluation, §§5–6), OFN v0.10 (decision structure and OPENs only, §§7–8).
**Scope:** formal category throughout unless stated. Analytic/C^∞ realization is Problem B (OPEN).

## 0. Setting

- T(ρ,η) = (ρ − sin η, η + e^ρ − 1 − sin η); A = DT(0), A⁶ = I; T⁶ ≠ I (non-zero resonant six-step cubic term).
- f = 𝓛T𝓛⁻¹ in the W-frame. h is any formal Poincaré–Dulac normalizer, N = h⁻¹fh.
- N is odd: N(−z) = −N(z), formally. Reason: resonant monomials z^p z̄^q satisfy p − q ≡ 1 (mod 6), so p + q is odd.
- Triangle: edges r_AB, r_BC, r_CA stored cyclically. Raw additive closure is Σr_e = 0.

## 1. G1 — the formal involution `[THM — formal]` (DYAD)

**Definition.** Ŝ := f³∘(f⁶)^{−1/2}. Here (f⁶)^{−1/2} is the unique formal tangent-to-identity root of the tangent-to-identity germ f⁶. Equivalently, Ŝ is the cube of the semisimple (Jordan–Chevalley) part of f.

**Result.** For every formal PD normalizer h, Ŝ = h∘(−I)∘h⁻¹. Hence Ŝ² = I and Ŝf = fŜ hold formally and exactly.

**Proof.** N = R_λ∘U with U unipotent and commuting with R_λ. Then N³(N⁶)^{−1/2} = R_λ³ = −I. Powers and tangent-to-identity roots are natural under conjugation.

**Consequence.** RRF v0.8's S_h is the degree-6 truncation of Ŝ.

**Evidence.**
- `formal_involution_jet_check.py` (SHA-256 `609dda42…e5f5e406`): exact Q(i√3) arithmetic, 15/15 PASS at orders 7/9/11/13, executed on the PI machine.
- The F^{−1/3} negative-control FAIL is a transferred execution record. That check is not in the uploaded script.
- Degree-2 jet (−W + s₂, s₂ = 2h₂) and [f⁶]₂ = 0 re-derived independently (Claude).

**Analytic realization.** If the normal form converges, Ŝ is analytic. The converse and C^∞ realization are OPEN (Problem B).

## 2. Uniqueness lemma `[ALG — formal]` (DYAD; independent check requested)

Every formal involution commuting with T is either I or Ŝ.

**Proof.**
1. DR(0) commutes with A. The commutant of A consists of complex scalars, so DR(0) = ±I.
2. Ŝ is a formal function of T, so any R commuting with T also commutes with Ŝ.
3. If DR(0) = −I, then RŜ is tangent to the identity and (RŜ)² = I.
4. A unipotent involution is the identity, so R = Ŝ.

## 3. κ-family classification `[THM — conditional, raw encoding]` (DYAD/RRF)

F_κ(r)_e = T(r_e) − (κ/3)·Σ_j T(r_j), with E_e(r) = r_e.

- E_eF_κ − TE_e = −(κ/3)ΣT. ΣF_κ = (1 − κ)ΣT.
- Witness (x, 0, −x), x = (ρ, 0): ΣT = (0, 2(cosh ρ − 1)) ≠ 0. Only the even part of T is used, not μ.
- Over any neighbourhood of 0: primitive autonomous-edge factorization holds ⟺ κ = 0. Raw additive closure is preserved on every closed state ⟺ κ = 1.
- For any F (not only κ-family) on the raw carrier, exact additive closure together with all edges autonomous is impossible, by the same witness.

## 4. Formal group-closure obstruction `[ALG — formal]` (DYAD)

**Premises.**
- ⋆ is a real two-dimensional formal (Lie) group law in characteristic 0.
- Its identity is e = 0 = P₁, the fixed point of T.
- Edges are cyclically oriented, and closure is x⋆y⋆z = e.
- The same autonomous T acts on every edge.
- Closure is preserved on all local closed triples.

**Proof.**
1. The triple (u, u⁻¹, e) gives T(u⁻¹) = T(u)⁻¹.
2. Choosing z = (x⋆y)⁻¹ gives T(x⋆y) = T(x)⋆T(y), so T is a formal automorphism.
3. A formal automorphism is linear in canonical (log) coordinates; this holds in the non-commutative case too, via BCH.
4. So T would be formally conjugate to A, and T⁶ = I. This contradicts T⁶ ≠ I.

**Conclusion.** Standard A (§7) is excluded under group-type closure.

**Scope.** The obstruction concerns **only** T being an automorphism of the closure group. It does **not** exclude group laws whose inversion is Ŝ (§5).

**Correction recorded.** Claude's earlier claim (16 Oct) that group-type closure also excludes the coincidence realization of Standard B, and that a group inversion cannot be Ŝ, was wrong. §5 is the counterexample.

## 5. Group-type closure realizing Standard B `[ALG — formal construction]`

**Transported group law.** u⋆v := h(h⁻¹u + h⁻¹v). Its inversion is h(−h⁻¹u) = Ŝu. Closure in normal-form coordinates is z₁ + z₂ + z₃ = 0.

**(a) ChatGPT's construction.** 𝓕(z) = (N z₁, N z₂, −N z₁ − N z₂).
- Closure is preserved.
- (z, −z, 0) ↦ (Nz, −Nz, 0), so the coincidence embedding recovers T.
- Node-permutation equivariance is not established: the third slot is slaved.

**(b) Symmetric version: κ = 1 in the transported carrier.** 𝓕_sym(z)_e := N(z_e) − ⅓Σ_j N(z_j), i.e. 𝓕_sym = P∘N^{×3} with P the sum-zero projection.
- **Closure:** transported closure is preserved exactly.
- **Slot symmetry:** equivariant under all edge-slot permutations, because P and N^{×3} both commute with them.
- **Reversal symmetry:** equivariant under the reversal −I^{×3}, i.e. Ŝ^{×3} in original coordinates. N is odd and P is linear.
- **Node symmetry:** node transposition = slot transposition ∘ reversal, so the model is node-permutation equivariant. (Formal; Claude's argument, not yet independently checked.)
- **Standard B:** on (z, −z, 0) we have ΣN = 0, so 𝓕_sym restricts to N. The coincidence stratum is the fixed set of a node transposition and is invariant (equivariance lemma). Standard B is realized by the coincidence embedding ι(u) = (u, Ŝu, 0) in original coordinates.
- **Standard A:** fails, because N is not additive.

**Contrast with raw-carrier κ = 1 (projected K₃).** That model is symmetric only under edge-slot permutations; node transposition is broken by T's even part (verified numerically 14 Oct). Its coincidence stratum is not invariant. The difference between the two κ = 1 models is **only the carrier in which closure and projection are written**. This is RRF's §0 lock rationale made explicit.

**Caveats.**
- (i) Everything is formal. The finite h₆ gives oddness only to degree 6; RRF VF-1 records an even degree-10 term for the delivered F̂.
- (ii) **Non-canonical carrier.** The transported group law depends on h. Normalizers differ by elements of the formal centralizer of N, which are generally non-additive. So, unlike Ŝ, the transported closure is not intrinsic. The DYAD-ALG-NF6 convention fixes it only through degree 6. Selecting it physically is OPEN.
- (iii) No physical network model is selected.

## 6. Coincidence embedding and Standard B

- ι(u) = (u, Ŝu, 0) and D_Ŝ = im ι, with dim 2 and codim 4 in R⁶. ι intertwines T^{×3} with T formally.
- For any network update F_net, closure-compatibility (D_Ŝ ⊂ C, F_net(C) ⊂ C) is not sufficient. F_net∘ι = ι∘T must be shown separately.
- The condition D_Ŝ ⊂ C encodes "coincident nodes are admissible closed configurations under the dynamically compatible reversal". It is mandatory only if G2-A admits coincidence as a physical closed configuration (class G2-A1).

## 7. Decision structure for G2-A `[HEUR]` (OFN)

Two independent choices: closure type × dyad-recovery standard.
- **A — global factor:** E_eF = TE_e everywhere.
- **B — invariant embedding:** F∘ι = ι∘T.
- **C — boundary-conditioned recovery:** I_e = 0 under a declared admissible isolation condition.

| Closure type | A | B via coincidence | B other / C |
|---|---|---|---|
| Group-type, raw additive | Excluded (§3, §4) | Not available (D_Ŝ ⊄ raw C) | Open |
| Group-type, h-transported | Excluded (§4) | **Formal realization exists, symmetric** (§5b) | Open |
| Non-group invariant relation | Open | Open (non-group germ) | Open |
| Exact closure not required | κ = 0 (formal) | κ = 0 + Ŝ (formal) | Open |

Coincidence classes: G2-A1, coincidence-admitting (D_Ŝ requirement applies when exchange is represented by Ŝ); G2-A2, general relational network (requirement not imposed).

**OFN's question** is no longer "group-type or not". It is: **which carrier carries physical closure (raw vs h-transported vs non-group), and which recovery standard is required?** Formal realizability does not settle identity/action/encoding admissibility.

## 8. OPEN list

1. **Problem B:** analytic or C^∞ realization of Ŝ, and of the transported carrier.
2. **Canonicity:** physical selection of the closure carrier, given that the transported group law depends on h (§5 caveat ii).
3. **Non-group germ:** T^{×3}-invariant codim-2 closure germs at 0 that are not of formal-group type, kept separate across formal, analytic and sectorial classes. Fatou-type coordinates are a `[HEUR]` direction only.
4. **Other recovery routes:** edge-mixing full-triad factors onto T; factors onto other clocks (e.g. T⁶).
5. **Physical selection:** exchange action, coincidence admissibility (A1/A2) and clock — G2-A / OPEN-OPA / OPEN-3B.

## 9. Ownership and next steps

- **DYAD:** one written proof note covering §1 (G1), §2 (uniqueness), §3 (κ), §4 (group obstruction), and §5 as formal constructions.
- **RRF:** evaluate §5b as an h-transported carrier profile candidate, given the §0 lock and canonicity caveat (ii). No registration implied.
- **OFN v0.10:** receive §7 and §8 as decision structure and OPENs; no theorem ownership.
- No new campaign is needed. Independent checks are requested for §2 and the node-equivariance claim in §5b.
