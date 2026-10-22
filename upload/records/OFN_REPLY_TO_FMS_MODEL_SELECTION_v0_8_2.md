# OFN → FMS: Scoped Model-Selection Decision — v0.8.2 (consolidated)

**Status:** `[SESSION]` consolidated co-owner handoff. It is the single input for OFN v0.10. **OFN owner adoption is a separate PI decision**, and no owner file is modified by this text.

**v0.8.2 (19 Oct 2026): readout correction (FMS reflection note v0.1.1 §4; co-owner finding).** Q1–Q6, the ψ decision and the theorem itself are unchanged.
- **§4, Canonical:** v0.8.1 said "|c| reads it given κ". That is wrong. Given κ, |c| fixes m only up to the reflection m ↦ 2m* − m, because |c|² is symmetric about m*. OFN rechecked this symmetry symbolically.
- **§3.5(a′):** the finite-a item now says that |c| alone does not separate m from its reflection, and states the reduced-map scope. The Readout item is narrowed to match. The grade of the universal claim is aligned with the co-owner's tag.
- **Open list:** a torus-invariant scalar that reads the sign of m − m* is added. It is needed only if RRF wants a physical readout.

**v0.8.1 (19 Oct 2026): second co-owner review of v0.8 applied, plus new results.** Q1–Q6 are unchanged.
- **§3.3 and §3.5(c):** the canonicity wording is corrected (co-owner text). The ambient law is a family, and a formal conjugacy obstruction has been **found**, which is different from "not proved".
- **§3.5(a′):**
  - **Finite a.** The ℤ₂ reflection is now excluded. Through degree 5, m(a) is a **complete** invariant of the chart family: f_{κ,a} ≅ f_{κ,b} ⟺ m(a) = m(b). This uses the FMS reflection test (κ symbolic) and an independent OFN audit at κ ∈ {1, 1/2, 3}.
  - The evidence level of each sub-result is stated separately: read, executed, or reported.
- **§3.5(a′) and §4:** the basin statement is narrowed. Quintic dynamics depend on the member, but dependence of the actual basin boundary is not proved, and existence of the boundary is open.
- **Genesis v2.8.9 notice erratum applied:**
  - §3.1 is routed through the six-step theorem, not the primitive-clock `[ALG]` statement;
  - the κ = 1 wording in §3.4 is fixed.
- **§0:** DYAD pin moved to v6.4.16 (lifecycle release). FMS ledger v0.6.4 is reported, not read.
- **§5:** evidence rows added.

**v0.8 (19 Oct 2026): consolidation.** This version merges the accepted v0.7.2 handoff with the following, all accepted by both OFN co-owners on 19 Oct 2026:
- the source review `OFN_SOURCE_REVIEW_ER2B_GEN288_OPEN3_v0_1_1.md` (`8d18640f…0944`);
- its addendum `OFN_SOURCE_REVIEW_ADDENDUM_FMS062_DYAD6414_RRF083_v0_1.md` (`f86cd483…c5b8`);
- the later co-owner rounds on Genesis v2.8.9, the FMS ψ invariants and DYAD v6.4.15.

**Q1–Q6 verdicts are unchanged.** The changes are to evidence grade, scope and wording only:
- **§0 (new):** source manifest with live pins. §0a fixes one chiral convention.
- **§1 Q6:** the regularity class (local C³) and the narrow planar-product contract are fixed (D1).
- **§2:** class C is declared as a re-imposed conditional model (RRF v0.8.3 §0.3), with regularity, clock, domain and readout chart stated (D6).
- **§3.1:** "conditional on 6S" is replaced by the adopted Genesis RIDs, for the raw family only.
- **§3.2:** the "other carriers" loophole is sharpened (OPEN-C19-L).
- **§3.4:** class-C Q6 rests on adopted Genesis v2.8.9 `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO`, plus an OFN corollary for the narrow contract.
  - The κ range is split into a formal range and a stability range (D2).
  - Chirality statements are relative (D5).
  - A raw-readout guard is added.
  - Single-dyad on-surface imports (DYAD v6.4.15) are added.
- **§3.5(a):** "remaining class members are not conjugate — withdrawn as unproved" is replaced by the established modulus (D3): every κ ∉ {0, 2}, and finite a up to a ℤ₂ reflection. |c| is the conjugacy invariant, and Im c = 0 is not a normalization principle.
- **§4, §5:** dispositions, tests and evidence updated.
- **§6 (new):** non-claims.

**v0.7.2 (19 Oct 2026):** owner-source synchronization only, no scientific change. Agreed by both OFN co-owners on 19 Oct.
- §3.5(b): uniqueness of J now cites the adopted `DYAD-THM-FORMAL-Z6-GENERATOR` (DYAD v6.4.13 §6.16). FMS R3 is demoted to SESSION corroboration.
- §3.5(e): DYAD statements carry their adopted grades.
  - Lemma F: `[THM]`.
  - F1–F3: `[THM — conditional]`, on the existence of the smooth object.
  - OPEN 20: PARTIAL.
  - Grades are cited directly, not inferred from the RID strings (DSN v1.3).
- §3.5(f): new scoped ontological reading. It is narrowed per the second co-owner: flat ambiguity is removed, but existence and physical pole-exchange identification stay separate.
- §5: DYAD v6.4.13 source row added.
- This answers DYAD notice N9 for OFN at session level. Owner level waits for OFN v0.10, after RRF v0.8.3.

**v0.7.1 (19 Oct 2026):** synchronized with adopted DYAD v6.4.13.
- §3.5(e) C^∞ paragraph corrected:
  - commutation and uniqueness of an existing C^∞ root are THM via F3;
  - the Borel-and-iterate route is a proposal only;
  - the reliance on L-SHADOW-POLY is withdrawn.
- The DYAD target and §4 test 1 are replaced by OPEN 20 B-6 / B-∞ existence.

**Date:** 18 October 2026 · **Status:** `[SESSION]` joint OFN co-owner decision for the FMS receiving interface. Pending PI adoption into OFN v0.10. No canonical owner document is modified.
**Replies to:** `OFN_MODEL_SELECTION_DECISION_REQUEST_v0_2.md`, which adds the Q3a/Q3b split.
**Supersedes:** v0.7.1 of 19 Oct (v0.7.1 superseded v0.7, which superseded v0.6).
**Changes in v0.7 (from v0.6):** the FMS canonicity and realization reviews of 18 Oct are incorporated:
- new §3.5: normalizer dependence, the canonical ℤ₆ generator J, and the Bochner construction of a real transported carrier;
- §3.3 *Conditions* rewritten: the realization target is one object, an identity-tangent sixth root of F = T⁶ (equivalently J), not two separate roots and not a convergent normalizer; the superseded "Q6 not yet shown" sentence is marked historical;
- §4 and the required tests updated;
- two withdrawn claims recorded: "normalizer changes affect only fifth and higher order" and "the remaining class members are not conjugate".

**Earlier changes (v0.6 and before):** see the v0.6 header. In brief:
- v0.6: the second co-owner's acceptance review (off-plane terminology, conditional basin-boundary role of the coincidence surfaces, rate target, truncated-model scope);
- v0.5: narrowings of §3.4;
- v0.4: proof repair in §3.2 and a new §3.4;
- v0.3: PI decision fixing Standard C at cubic order.

## 0. Source manifest (v0.8)

| Source | Version / identity | Grade | Verification by the OFN co-owners |
|---|---|---|---|
| DYAD | **v6.4.16** (adopted 19 Oct, lifecycle release; `33c14c5cc27625c17a2b78be74e070ae61b5c7399ded49a1538098735ab559e0` per its release record, not re-hashed by OFN) | `[OWNER]` | Release record read. OPEN 3 is CLOSED within its scope; new OPEN 21 (primitive-variable phase remainder); OPEN 20 unchanged; no graded RID changed. v6.4.15 (`be270dde…c947c4`, OPEN 3b) is the source of the cited OPEN 3 RIDs, and its release record and N11 were read. v6.4.14 (`7fb85105…6bdd`) is retained as the historical source of OPEN 3a, and v6.4.13 (`5958f7fe…8542`) as the source of §6.16–§6.17 |
| Genesis | **v2.8.9** (adopted 19 Oct; `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc`, 1649 lines) | `[OWNER]` | SHA computed directly from the file; §6.3c read in full. Byte identity of §6.3a–§6.3c with the draft is release-checker reported |
| RRF | **v0.8.3** (adopted working standard, 19 Oct) | `[OWNER — RRF working standard]` | Read in full; file SHA not measured by OFN (DYAD reports `b393657e…a187`) |
| FMS ledger | v0.6.2 (SESSION; header reads v0.6.1) read. v0.6.4 with its §12E record is **reported, not read** | `[SESSION]` | v0.6.2 read |
| FMS ψ notes | phase-invariant, finite-invariant and reflection notes | `[SESSION]` | All three notes read. Scripts **not** rerun by OFN. Their main claims were recomputed independently with OFN's own code, at the scope stated in §3.5(a′); this does not cover every step of the FMS proofs |
| ER-2B | v0.3.1, noncanonical reference record | noncanonical | Read; A.4 cubic identity reproduced |
| OFN | v0.9 (adopted baseline). This text supersedes the v0.7.2 working copy (`6044f43e…5b4c`, SHA confirmed by both co-owners) | `[OWNER]` / `[SESSION]` | — |

### 0a. Chiral-coordinate convention

This document uses the Genesis §6.3a convention: u = w₁ + λw₂, v = w₁ + λ̄w₂, N = Σ|w_e|² = |u|² + |v|², S = Im(w₁w̄₂) = (|u|² − |v|²)/√12, and ρ = S/N ∈ [−1/√12, 1/√12].

The Fourier convention w_e = uω^e + vω^{−e} gives N = 3(|u|² + |v|²) and S = −(√3/2)(|u|² − |v|²). The limit |ρ| = 1/√12 is the same, but the sign attached to each axis differs. Any statement about the sign of chirality must name its convention.

**Accepted from earlier revisions:**
1. Coincidence is not postulated to be a merge. r_BC = 0, B = C and the reduction 𝒳₃ → 𝒳₂ remain distinct.
2. Raw W is the FMS test carrier only; it is not a physical or canonical choice.
3. Identity encoding holds only on the fixed incidence/chirality edge-value sector.
4. Q4 and Q6 are model-class requirements, not universal axioms.
5. The holonomy capacity, a nonzero value, dynamical independence and a curvature reading are kept as separate properties.

---

## 1. Verdicts

**Q1 — Exact closure.** Not a universal requirement. Exact additive closure is admissible as a flat, node-mediated sector. It is not imposed on independent relational-edge models.

**Q2 — Asymptotic closure.** Admissible, not required. Any asymptotic closure must follow from the selected dynamics.

**Q3a — Full primitive edge autonomy.** Not required. Boundary-conditioned isolated-dyad recovery (Standard C) is the minimum target for a genuine relational triad. The isolation regime must be explicitly defined, physically admissible, nonempty and dynamically consistent. Standard B remains an alternative.

**Standard C, order fixed (PI decision, 18 Oct 2026).** `[DEF]` Write the update as F_e(X) = T(r_e) + I_e(X). Standard C holds if there is a nonempty, F-invariant regime 𝓡 on which **I_e = O(|r|⁴) for every edge e**. That is, the isolated dyad is recovered through cubic order, the order that carries μ and the six-step return. Recovery at linear order alone does not count, because every κ-model has it.

**Q3b — Partial autonomy.** Not required, and **not acceptable as the law of a genuine triad** in its asymmetric form.
- The reason is covariance (Q5): designating which edge is slaved breaks covariance under complete-state relabeling, unless that designation is itself physical state data.
- If it were, it would be an additional state variable, i.e. route C-a, and must be declared as such.
- The known formal construction (two exact factor edges, one slaved edge, transported closure) is retained as a mathematical witness only.

**Q4 — Cycle content.** The genuine relational-triad model class must permit nonintegrable cycle content. The raw additive defect is a candidate observable, not an established curvature variable. Flat sectors remain admissible.

**Q5 — Exchange and coincidence.**
- Covariance of the complete oriented state under relabeling is required: F_{π·m}(πX) = πF_m(X), where m carries orientation, role and model data.
- Active dynamical reversal on a fixed raw-edge model is not required, so DYAD OPEN 20 is not a precondition **for Q5**. (It is a precondition for the real transported carrier, §3.5.)
- Vanishing relation, node identity and merge are distinct; any merge needs its own reduction contract.
- OPEN-OPA is only partly addressed: whether physical pole-role exchange is the same operation as bookkeeping relabeling stays open.
- Clock: primitive T.

**Q6 — Genuine coupling.** Required within the genuine interacting-triad class. Coupling means interaction that cannot be removed by a passive transformation into a decoupled product, under the declared state, encoding and clock.
- **Regularity (Q6-REG, D1; fixed in v0.8).** Passive transformations are **local C³ diffeomorphisms** fixing the base point. This is the regularity of every theorem used (§3.1, §3.4; Lemma S; carrier independence). Decouplings below C³ are `[OPEN]`: unproved, not refuted.
- **Governing contract.** The **narrow** reading governs: no local C³ conjugacy to a product of three planar edge maps, and no neutral planar C³ factor under the declared clock. Wider product decompositions (non-planar, d ≥ 4) are not covered and need separate proof (Genesis v2.8.9 §6.3c guard G-OFN).

## 2. Model declarations

1. **State.** Oriented edge relations, incidence and chirality data. Taking nodes as endpoint classes is a model choice. Whether further state fields are needed stays open.
2. **Encoding.** Raw W edge values are the test carrier. Identity encoding holds on the fixed incidence/chirality edge-value sector.
3. **Closure.** No exact closure is imposed. h = Σ_e r_e is tracked as the raw additive cycle defect, a dynamical observable.
4. **Clock.** The primitive update. T⁶ is derived sampling. No final ontological definition of time is drawn from this.
5. **Regularity.** Real-analytic laws are the admitted continuous FMS test class. This is not a universal requirement.
6. **Class C model contract (D6; new in v0.8).** The transported family F^N_κ = P_κ ∘ N^{×3}, written in the N- or Φ-chart, **re-imposes** additive mean-feedback in new coordinates. By RRF v0.8.3 §0.3 it is therefore a *different conditional model*. It is not a passive transport of the raw κ-family, and not an `RRF-NET-W-RAW` equation set (RRF representation safety lock). For class C, OFN declares:
   - **regularity:** formal, or real C³ for the polynomial representatives. Analytic or C^∞ realization is conditional on DYAD OPEN 20 (B-6 / B-∞ existence).
   - **clock:** primitive T; T⁶ is derived sampling.
   - **domain:** a local neighbourhood of 0.
   - **readout chart:** transported (z or Φ). Raw-W readouts carry the static chart offsets of §3.4.
   - **RRF request:** register class C as a *model-contract row*, not a new native profile, while OPEN-B/E1 stays locked. The decision is RRF's.

---

## 3. Co-owner addenda: the A2 checks and the transported-carrier candidate `[SESSION]`

### 3.1 Genuine coupling of A2 follows from Theorem 6S (strong form) `[THM — imported; raw family only]` (v0.8; previously `[ALG — conditional on 6S]`)

**v0.8 source.** For the raw family the condition is discharged at owner level by these Genesis RIDs, unchanged since v2.8.7:
- `GEN-THM-K3-PLANAR-FACTOR-NOGO` and `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` (κ = 1);
- `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO`, for γ ≡ κ ∈ ℝ∖{0,2}, under (H_spec); the primitive-clock family statement is for the same range under (H_prim).

They are cited with exactly this scope. (H_prim) is a hypothesis inside the range; it does not extend anything to κ = 2. This import does **not** cover class C, which is treated in §3.4.

Suppose F_κ (κ ∉ {0, 2}) were locally C³-conjugate to a product G₁ × G₂ × G₃ of planar maps.
- DF_κ(0) has spectrum {λ, λ̄} with multiplicity 2, and {(1−κ)λ, (1−κ)λ̄}.
- So at least two factors have unit-circle spectrum.
- Each such factor Gᵢ has spec DGᵢ(0) = {λ, λ̄}, so spec D(Gᵢ⁶)(0) = {1}. The induced six-step factor Eᵢ∘F⁶ = Gᵢ⁶∘Eᵢ therefore satisfies (H_spec), because (1−κ)⁶ ≠ 1. The six-step theorems `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` (κ ≠ 1) and `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` (κ = 1) exclude it. *(v0.8.1: routed through the six-step `[THM]`, per the Genesis notice erratum. The primitive-clock family statement is `[ALG]` and is not used.)*

**Conclusion.** A2 (and κ = 1) cannot be passively decoupled into three planar maps, nor into a neutral planar map times anything. That is exactly Q6 in the form OFN requires.

**Still open.** Splitting off the closure mode alone, i.e. a factor whose target is the closure mode (ker = 𝒞). This is not a decoupling into edge relations and does not affect Q6 as worded.

### 3.2 Standard C at cubic order fails in the raw carrier for every κ ≠ 0 `[ALG — SESSION]`

**Theorem.** Let κ ≠ 0. In the raw carrier there is no F_κ-invariant C³ submanifold M ∋ 0 of positive dimension on which I = O(|r|³), and a fortiori none with I = O(|r|⁴). So Standard C, in its smooth local form, already fails at quadratic order. This covers A1 and A2.

*Proof.*
- **Tangent.** The tangent of M is invariant under A^{×3}. So it is complex, of complex dimension 1, 2 or 3.
- **M lies in the closure plane to second order** (repaired per second co-owner review).
  1. I = O(|r|³) gives Σ T(r) = A·h + O(2) = O(|r|³). Hence h = O(|r|²) on M, and T₀M ⊂ 𝒞.
  2. On T₀M, DF_κ(0) = A^{×3} is invertible. So F_κ|M is a local diffeomorphism near 0, and every y ∈ M near 0 equals F(x) for some x ∈ M with |x| ~ |y|.
  3. Then h(y) = (1−κ) Σ T(x) = O(|x|³) = O(|y|³). Hence h = O(|r|³) on M.
- **Complex dimension 2** (T₀M = 𝒞). On M, Σ_e T(r_e) = Σ_e T₂(u_e) + O(3), and Σ_e T₂(u_e) = (0, ½Σ_e ρ_e²) ≢ 0. So I is not O(|r|³). Contradiction.
- **Complex dimension 1.** M is a graph w_e = G_e(w) with linear parts c_e ∈ ℂ, c₁ = 1 and Σ_e c_e = 0.
  - F = T^{×3} + O(3) on M, so each G_e commutes with T to order 2.
  - Degree 2 has no resonance, so g_{e,2} is unique: g_{e,2}(w) = h₂(c_e w) − c_e h₂(w) in the DYAD h₂ chart.
  - Then h = O(3) on M requires the degree-2 part of Σ_e G_e to vanish. Its z z̄ coefficient is c₁₁ · Σ_e |c_e|² with c₁₁ = −1/3 (DYAD §6.2), which is ≠ 0.

  Contradiction. `iso_quadratic_nogo.py` checks the identity exactly for general c₂ ∈ ℂ, and `iso_check.py` checks the two lock lines. The tangent classification itself rests on the analytic argument, not on the scripts. ∎

**Scope.**
- The result is local at 0 and concerns smooth invariant regimes.
- Not covered: non-manifold invariant sets (isolated orbits), finite-amplitude regimes away from 0, and other carriers.
- **OPEN-C19-L (v0.8)** `[ALG — SESSION; hand derivation]`. Take the ER-2B C19 quadratic-carrier family, with residual quadratic q̃ = ũw² + ṽww̄ + t̃w̄² and linear closure re-imposed.
  - The dimension-2 step forces q̃ = 0.
  - On equilateral lock lines (Σc_e² = 0), the dimension-1 step only forces ṽ = 0, since c̃₁₁ = −ṽ/(λ − 1).
  - Along the ER-2B σ-slice the no-go therefore extends to every σ < 1.
  - The codimension-2 subfamily ṽ = 0 is not excluded at quadratic order; its cubic-order and invariance conditions are unchecked.
  - This is a gap in an exclusion, not a candidate model.
- The cause is structural: the even part of T. It is the same h₂ term (c₁₁ = −1/3) that breaks raw coincidence invariance (RRF §6.2).

### 3.3 Transported carrier: exact Standard C on two node-covariant surfaces `[ALG — formal]`

In the h-transported carrier, take normal-form coordinates z, with N the λ-equivariant formal normal form. N is odd and satisfies N(ωz) = ωN(z) for ω = λ². The transported κ-family is

  F^N_κ(z)_e = N(z_e) − (κ/3) Σ_j N(z_j).

**Coincidence surface** 𝒮₀ = {(z, −z, 0)}.
- N is odd, so Σ N = 0 and I ≡ 0 **exactly**.
- 𝒮₀ is invariant, and each edge evolves by N ≅ T.

**Equilateral surfaces** 𝒮_± = {(z, ω^{±1} z, ω^{±2} z)}.
- Σ_k ω^{±k} N(z) = 0, so I ≡ 0 **exactly**.
- 𝒮_± is invariant, all three edges evolve by N simultaneously, and the transported closure Σ z_e = 0 holds on it.

**Node covariance.** Cyclic relabeling maps 𝒮_± to itself. A transposition with edge reversal maps 𝒮_+ ↔ 𝒮_−; edge reversal is −I, an exact symmetry because N is odd. So the pair carries exactly the **chirality datum** of the OFN state, and the full model is actively node-covariant.

**Cycle-defect capacity.** For κ ≠ 1, the transported defect Σ z_e evolves by (1−κ) Σ N off the surfaces. So Q4 capacity is present. At κ = 1 the model is transported A1 and flat.

**Back in raw coordinates.**
- 𝒮_± = {(u, G u, G² u)} with G = T²∘F^{−1/3}, an order-3 element of the formal centralizer of T.
- 𝒮₀ = {(u, R₀u, 0)} with R₀ = T³F^{−1/2}.
- Both are powers of the canonical generator J = T∘F^{−1/6}: R₀ = J³, G = J² (§3.5).

**Conditions** (revised in v0.7).
- *Existence.* The construction above is formal. A real carrier for the **whole** transported class, not only for the lock surfaces, follows from a single object: an identity-tangent sixth root of F = T⁶ in the required regularity, equivalently a real J (§3.5). A convergent normalizer h is **not** needed.
- *Canonicity* (v0.8.1 wording). The canonical formal lock geometry, the isolated edge dynamics on the lock surfaces, and the leading reduced chiral cubic coefficients are normalizer-independent. The ambient network law is a family, not a uniquely determined model. Its higher-order conjugacy structure is addressed in §3.5(a′).
- *Q6.* Settled in §3.4. (Historical: v0.3 recorded Q6 here as "not yet shown"; superseded.)

**Reading (`[HEUR]`).** Standard C at cubic order separates the carriers sharply.
- The raw carrier fails it locally for every coupling (§3.2).
- The transported carrier satisfies it exactly on the coincidence surface and on a node-covariant equilateral, chiral pair.

This is the first concrete class-C candidate meeting the OFN requirements Q3-C, Q4 (κ ≠ 1), Q5a and Q6. It is formal until J is realized (§3.5).

### 3.4 Transported model: Q6 and closure-internal stability `[ALG — formal; leading order]`

**Six-step cubic.** N has no quadratic term, so the centre manifold of F^N_κ (κ ∉ {0, 2}) is ψ = O(3). ψ₃ enters the cubic only through the linear part, which P kills. The reduced one-step cubic n₂₁(w_e|w_e|² − ⅓Σ_j w_j|w_j|²) is λ-equivariant. So the six-step cubic is

  f_e = μ(w_e|w_e|² − ⅓Σ_j w_j|w_j|²),

which is **independent of κ**. It is the raw-K3 cubic with ν → μ and χ → 0.

**Chiral form.** Both components have exactly the chiral form, with

  p = μ/3 = −1/6 − i·2√3/9,  q = 2μ/3 = −1/3 − i·4√3/9.

`transported_pq.py` checks this exactly, including the v-component and the absence of other monomials.

**Q6 for class C (v0.8).**
- `[THM — conditional; imported]` Genesis v2.8.9 §6.3c, `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO`.
  - **Statement:** no local C³ submersive six-step factor of real dimension d ∈ {1, 2, 3} exists.
  - **Hypotheses:**
    - (H-JET): the third jet equals that of the mean-feedback form over N₃(z) = λz + nz²z̄;
    - (H-μ): μ = 6λ̄n ≠ 0;
    - κ ∈ ℝ∖{0, 2};
    - (H_spec).
  - The theorem is closed under C³ conjugacy, and its algebraic dependency is Lemma S, adopted branch.
  - **Class C satisfies (H-JET) with n = n₂₁ and μ = μ₆ ≠ 0.** This holds for the real polynomial representatives (instance C1). It also holds for 𝓕_{κ,Φ}, conditionally on a real C³ chart Φ with ΦTΦ⁻¹ commuting with A (instance C2, whose existence is not asserted).
- `[SESSION — OFN corollary of the owner theorem; OFN adoption pending]` **Narrow Q6.** These real C³ network germs cannot be locally C³-conjugated to a product of three planar maps. *Proof.*
  1. Suppose F = Ψ⁻¹(G₁ × G₂ × G₃)Ψ. Then spec DF(0) = {λ, λ̄}^{×2} ∪ {(1 − κ)λ, (1 − κ)λ̄}.
  2. Each DGᵢ(0) is a real 2×2 matrix, so its spectrum is closed under conjugation. For κ ∉ {0, 2} the closure eigenvalues (1 − κ)λ and (1 − κ)λ̄ are off the unit circle, and λ, λ̄ must pair inside real blocks. At κ = 1 the closure eigenvalue is 0, which is real; the pairing argument still holds there, and κ = 1 is in any case outside the class-C formal range. Hence the closure pair lies in one factor. The two other factors are **exactly** neutral, with spectrum {λ, λ̄}.
  3. For a neutral factor, Eᵢ = πᵢ∘Ψ satisfies Eᵢ∘F⁶ = Gᵢ⁶∘Eᵢ. Here spec D(Gᵢ⁶) = {1} and (1 − κ)⁶ ≠ 1, so (H_spec) holds. This contradicts the Genesis theorem. ∎
- **Scope.**
  - The result covers real C³ germs: the polynomial representatives, and 𝓕_{κ,Φ} conditionally on Φ.
  - Formal power-series maps "as such" are not covered (Genesis guard G-JET).
  - It asserts no realization of the all-order formal model, no existence of J, no sub-C³ statement and no physical selection.
  - The obstruction does not distinguish class C from its third-jet equivalents (Genesis guard G-SEL).
  - General primitive-clock factor statements keep the Genesis `[ALG]` grade (primitive companion, no RID), which is not cited as a theorem.

**Geometry in chiral coordinates.** On the transported closure plane:
- the equilateral surfaces are the chiral axes, 𝒮₊ = {u = 0} and 𝒮₋ = {v = 0};
- the coincidence surface 𝒮₀ lies on the diagonal |u| = |v|, since u = λ̄z and v = λz there.

**Stability at leading order.** On the closure subspace, per six-step block,

  Δ log(|u|²/|v|²) = ⅓(|u|² − |v|²) + O(|(u,v)|⁴).

Consequences:
- **Relative attraction of the chiral axes.** For |u| < |v| the ratio tends to shrink, and for |u| > |v| it tends to grow. So 𝒮₊ and 𝒮₋ are relatively attracting at cubic order.
- **Cubic-order separator.** The equal-amplitude set |u| = |v| separates the two tendencies **at cubic order only**. It has **not** been shown to be invariant under the complete map. Higher orders, including the U(1)×U(1)-breaking n₀₅ z̄⁵ term, can move the basin boundary.
- **The coincidence surface.** 𝒮₀ is exactly invariant and lies on |u| = |v|. In the transverse closure-internal cubic direction it is repelling.
- **Coincidence surfaces and the basin boundary (conditional).** By the exact S₃ × reversal symmetry (N is odd), the three coincidence surfaces, one per node pair, are exactly invariant and lie on |u| = |v|. That alone does **not** prove they lie on a basin boundary.
  - They would, *if* two disjoint chiral basins are shown to exist *and* the corresponding transposition-with-reversal is shown to exchange them. An exchange-fixed surface could not then lie in the interior of either basin.
  - Until both are shown, this stays conditional.
- **Rate target (cubic truncation) `[ALG]`.** On the branch u → 0 (convergence to 𝒮₊):
  - |v_m|² ≈ 3/m and Δ log(|u|²/|v|²) ≈ −1/m;
  - hence |u_m|/|v_m| ≍ m^{−1/2}, |u_m| ≍ m^{−1} and |v_m| ≍ m^{−1/2}.

  Whether the quintic and higher terms preserve this is part of the FMS parabolic estimate. The late-stage simulation ratios approach it: for κ = 0.5, trial 1, the ratio changes by a factor 0.73 between m = 10⁴ and 2·10⁴, against the predicted 2^{−1/2} ≈ 0.707.
- **Closure mode.** Linearly attracting for 0 < κ < 2, with modulus |1−κ|.
- **κ range (D2; v0.8).**
  - The formal class-C properties (Standard C on the lock surfaces, p, q, Q6) hold for κ ∉ {0, 1, 2}.
  - Stability statements apply only for 0 < κ < 2, κ ≠ 1. For κ < 0 or κ > 2 the closure mode is **repelling**.
  - κ = 2 is excluded because the closure multiplier (1 − κ)λ = −λ lies on the unit circle. There the closure direction is non-hyperbolic and the centre-manifold reduction does not apply. This is not a Q6 failure.
- **Relative versus absolute chirality (D5; v0.8).** The attraction above is **relative**. With ρ = S/N (§0a), Δρ = S(1/6 − 2ρ²) + O(5) on the closure plane, so |ρ| → 1/√12. The absolute |S| decays together with N. ER-2B's "chirality attenuating" (C11/C20) refers to the absolute |S| and does not conflict.
- **Raw-readout guard (v0.8)** `[ALG structure — SESSION]`. If chiral modes are read in raw coordinates W_e = h(z_e), the raw mode does not vanish on the exact surface u = 0: u_W = O(|v|²), so |u_W|/|v_W| = O(|v|) ∝ m^{−1/2}. This has the same exponent as the predicted approach rate.
  - Rate tests must therefore use transported-chart modes, or subtract the static offset.
  - The coefficient depends on the convention.
  - The single-edge ingredients are owner-grade: `DYAD-ALG-OPEN3-LEADING` (v6.4.14) and, asymptotically, `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` T2, M_W − M = −Δ₀(z₀) (v6.4.15, conditional on RECOG R9).
- **Single-dyad imports on the lock surfaces (v0.8)** `[OWNER: DYAD v6.4.14–v6.4.15; conditional on the real surfaces (J)]`. On 𝒮₀ and 𝒮_± each edge evolves as an isolated dyad. Edgewise, and only there, the following apply:
  - the chart laws and PRIM-CTR;
  - `DYAD-THM-OPEN3-SPIRAL-REM` (per-block bounds);
  - `DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS`.

  The static leading offsets D₃ and D_{Θ,1} transfer edgewise and class-wide at leading order. **Nothing transfers off the surfaces, and nothing transfers as a separator or basin statement.**

**Status levels (FMS review accepted).**
- Formal invariance of the chiral surfaces: `[ALG — formal]`.
- Cubic-model normal shape attraction: `[ALG — leading order]`.
- Convergence of an open set of initial states to the chiral surfaces under the full local dynamics: `[OPEN]`, numerically supported only.

**Numerics `[NUM]`.**
- **Withdrawn v0.4 claim.** v0.4 said "|u|/|v| drifts monotonically away from 1 in every run". That is withdrawn. In `transported_sim.py` the initial states lie off the closure plane (|Σz| ≈ 0.1). There the linear projections u, v are not a complete chiral coordinate system, and trials 1 and 2 at κ = 0.5 cross 1 during that transient.
- **After relaxation.** From n = 600 onward, all six runs keep the side they then have, and their ratios drift away from 1.
- **Closure-plane test.** `basin_test.py` places initial states on the transported closure plane with |u|/|v| = 1 ± d, for d ∈ {0.3, 0.1, 0.03}, random phases and κ ∈ {0.5, 1.5}. The long-time side agrees with the cubic separator in **48 of 48** runs.
- **Scope.** This supports the cubic separator near the diagonal, at these amplitudes, phases and iteration lengths. It does **not** show that |u| = |v| is invariant under the complete map, or that it decides the basin side for every sufficiently small initial state.
- **Model scope.** The simulations run the **degree-5 truncated** λ-equivariant polynomial N, not the all-order formal map or a convergent normal-form map.

**Reading (`[HEUR]`; physical interpretation `[OPEN]`).** At cubic order, the transported model drives closure-internal ratios toward one of two invariant chiral equilateral surfaces, with the coincidence surfaces on the separating set. Which branch is selected is decided by the true basin boundary, which is open. This is mathematical chiral separation, not physical chirality selection.

**Physical-isolation scope note.** On 𝒮_± the interaction vanishes algebraically while all three relations stay active. This satisfies the mathematical Standard C contract. It does **not** by itself show that the triad's surroundings have been physically removed. The physical-isolation reading of Standard C stays `[OPEN]` in OFN.

### 3.5 Canonicity and realization of the transported class `[SESSION]` (new in v0.7)

**(a) Normalizer freedom `[ALG — formal]`.** Two λ-equivariant normal-form charts with identity linear part differ by h′ = h∘g. Here g is λ-equivariant and tangent to the identity, with first nonlinear term of degree ≥ 3. The raw-space law is

  M_g = H·(G P_κ G⁻¹)·N^{×3}·H⁻¹,  H = h^{×3}, G = g^{×3},

with P_κ linear. Two special subclasses:
- **Linear g:** only z ↦ λ^k z is possible, and it commutes with P_κ, so the model is unchanged. (The multipliers are restricted to μ₆ because a₀₅ ≠ 0.)
- **g ∈ Cent(N),** i.e. g = exp(sX_N): then M_g = Φ_s M Φ_s⁻¹ with Φ_s = (exp(sX_T))^{×3}. This is an edge-local shift of each isolated dyad's clock phase, so these models are formally conjugate.

**Withdrawn (FMS review accepted).**
- "Normalizer changes affect only fifth and higher order" is withdrawn. In common raw coordinates the ambient laws differ **from cubic order**: g₃^{×3}(P_κ y) − P_κ g₃^{×3}(y) ≠ 0 in general. Only the resonant six-step cubic of the reduced dynamics coincides.
- "The remaining class members are not conjugate" was withdrawn in v0.7 as unproved. **v0.8 replaces it with the result below.**

**(a′) The class carries a genuine in-class modulus (D3)** `[ALG — SESSION]`. The evidence level is given for each item. Take the λ-equivariant cubic chart change g_a(z) = z + a z²z̄.
- **a ∈ ℝμ.** g_a agrees with an element of Cent(N) through degree 5, so N_a = N identically through degree 5. The models coincide, not merely conjugate.
- **a ∈ iℝμ, first order in a.** Formal conjugacy, within the connected linear stabilizer, is obstructed at degree 5 for **every** real κ ∉ {0, 2}. The exceptional set is empty: a fixed 32×32 minor is a nonzero constant in t = (1 − κ)/κ (FMS 9×9 minor; OFN independent 32×32 minor). *Evidence: two independent exact computations, executed by both co-owners.*
- **Explicit invariant.** Let c(κ, a) be the u³v̄³ coefficient of A∘F₆ − A, with A = |u|². Then
  c = −1/486 + 7t/648 + i·[17√3/2916 + 2√3·t/81 − (2/9)·Im(aμ̄)].
  - The closed form was checked exactly by OFN at 12 points, including finite a.
  - c is unchanged by all 24 equivariant cubic generators (S₃ and non-S₃).
  - The relative-phase torus rotates c by a phase. |c| is invariant under **every formal conjugacy**.
  - *Evidence for these three items:*
    - The FMS proposition rests on exact degree-5 linearity and Stab(f₃) = T² ⋊ swap. It was read by OFN.
    - OFN independently checked: the closed form at 12 points; invariance under the 24 generators at κ = 1/2 and κ = 3; the torus action c → −c under diag(λ, 1).
    - OFN independently re-derived the degree-5 linearity step by hand, and computed Stab(f₃) = T² ⋊ swap exactly. The Gröbner basis of f₃∘B = B∘f₃, with reality and invertibility imposed, has two branches: B diagonal with unit-modulus entries, or B antidiagonal with unit-modulus entries.
- **Finite a: complete degree-5 invariant (v0.8.1).** Through degree 5, **f_{κ,a} ≅ f_{κ,b} ⟺ m(a) = m(b)**. Here m = Im(aμ̄), and m* = 17√3/648 + √3·t/9 is the reflection point.
  - *If.* The degree-5 part is real-affine in a and vanishes along ℝμ, so equal m gives identical 5-jets.
  - *Only if.* Unequal |c| excludes the generic case. The reflected case m(b) = 2m* − m(a) is excluded by the condition (B⁻¹f_bB)₅ − f_{a,5} ∈ Im L₃, solved exactly over the torus (with and without the swap) by a Gröbner basis.
  - *Evidence:*
    - FMS reflection test (P1–P4; κ symbolic in P4). The note was read; the script was not rerun by OFN.
    - **Independent OFN audit** with its own linear algebra and exact kernel over ℚ(√3), at κ ∈ {1, 1/2, 3}. Two reflected pairs per κ give GB = [1]. Two controls per κ (identical pair; pair conjugated by diag(λ, 1)) are solvable; the identical pair recovers w³ = 1, z = 1.
  - **Readout limit (v0.8.2).** |c| alone does not separate m from its reflection. The reflection is separated by the remaining quintic data, through P4, and not by c.
  - **Scope.** The statement holds within the stated reduced-map scope (the chart family on the centre manifold). For the full transported models only the "not conjugate" direction carries over (FMS completeness lemma, step (g), κ ∉ {0, 2}).
  - **Grade:** `[ALG — SESSION; FMS symbolic P4 reported, OFN sampled verification]`. The universal κ statement rests on FMS P4, whose proof text OFN has not audited independently. Both co-owners have executed the OFN confirmation at three κ values.
- **Readout.** |c| is the amplitude of the 3θ relative-phase harmonic in Δ(A ± B) over one six-step return. It is the conjugacy-invariant **candidate** observable. It reads m only up to the reflection m ↦ 2m* − m, so it is not a full numerical readout of the modulus. The phase of c depends on the representation, so the chart "Im c = 0" is **not** a normalization or selection principle.
- **Open:**
  - the other seven first-order moduli of the S₃ class, which the chart family does not reach;
  - a torus-invariant scalar that reads the sign of m − m*. It is needed only if RRF requires a physical readout;
  - κ ∈ {0, 2};
  - jets beyond degree 5;
  - the physical readout in a declared carrier and encoding (RRF contract).
- **Consequence for FMS** (v0.8.1 wording). Leading-order results (separator, rate target) are class-invariant. The full nonlinear basin boundary remains OPEN. Quintic dynamics depend on the model member, so basin boundaries and asymptotic corrections must be investigated per member, or uniformly across the admitted modulus family. Actual dependence of the basin boundary on the member has not been proved.

**(b) Canonical objects `[THM — formal]`.** Let X = log(T⁶) and

  **J = T∘exp(−X/6) = T∘F^{−1/6}.**

Then J⁶ = I, JT = TJ, DJ(0) = A, and R₀ = J³, G = J².

**Uniqueness of J.** J is the unique formal map commuting with F, with J⁶ = id and DJ(0) = A.
- Source: `[THM — formal]` `[import: DYAD v6.4.13 §6.16; RID: DYAD-THM-FORMAL-Z6-GENERATOR]`. The owner proof uses only Theorem C (`DYAD-THM-FORMAL-CENTRALIZER`).
- The SESSION classification Cent_formal(T) = {T^k exp(sX)} (FMS R3), cited in v0.7.1, is now corroboration only, not a premise.

Hence the lock surfaces 𝒮₀, 𝒮_± are normalizer-independent in raw coordinates, as is the isolated T dynamics on them.

**(c) Class-invariant observables `[ALG — formal]`.**
- Exactness of Standard C on the lock surfaces holds for every member: g is λ-equivariant, hence odd and ω-equivariant, so N′ = g⁻¹Ng is too.
- p = μ/3 and q = 2μ/3, hence Q6 and the leading-order shape law, each in that member's own closure chart.
- Q5 covariance.

*(v0.8.1, co-owner text.)* The full ambient network law is not uniquely determined by the canonical generator and the lock geometry. The fifth-order ψ-modulus in §3.5(a′) establishes a nontrivial formal conjugacy obstruction within the stated class. This does not classify every member, every higher-order jet, or every invariant manifold.

The existence and geometry of the full nonlinear chiral basins, and their dependence on the class modulus, remain OPEN. No physical selection observable is established by the formal modulus alone.

**(d) Bochner construction of a real carrier `[THM — conditional on J]`.** Assume J is realized near 0 (analytic or C^∞) with J⁶ = I, DJ(0) = A and JT = TJ exactly. Put

  Φ = (1/6) Σ_{k=0}^{5} A^{−k} J^k.

Then:
- DΦ(0) = I and Φ∘J = A∘Φ;
- Φ is a local diffeomorphism of the same regularity;
- N_Φ = Φ T Φ⁻¹ commutes with A **exactly**.

The law

  𝓕_{κ,Φ} = (Φ⁻¹)^{×3} ∘ P_κ ∘ N_Φ^{×3} ∘ Φ^{×3}

is a real local transported κ-family with exact Standard C on 𝒮₀ and 𝒮_±. The admissible charts are {ψ∘Φ : ψ λ-equivariant}, the real counterpart of the g-family in (a). No normal form and no normalizer convergence is required.

**(e) The realization target.** Write T = J∘K with K = F^{1/6} identity-tangent and JK = KJ. This is the multiplicative Jordan–Chevalley split of T into a finite-order (semisimple) part J and a unipotent part K.
- **Analytic category `[THM — analytic, local]`:** the following are equivalent:
  - an analytic identity-tangent sixth root K of F exists;
  - an analytic T-commuting J exists;
  - an analytic chart exists in which T is exactly λ-equivariant.

  (A real K has formal jet exp(X/6), which commutes with T formally, hence exactly by the identity theorem.)
- **C^∞ category (corrected in v0.7.1, grades pinned in v0.7.2):** take an *existing* C^∞ identity-tangent root of F. Its exact commutation with T and its uniqueness are owner results:
  - F3: `[THM — conditional]` on the existence of the smooth object, `[import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]`;
  - resting on Lemma F: `[THM]`, `[RID: DYAD-CAND-FLAT-CENTRALIZER]`, on its D1–D3 domain with value-level flat contact.
  - The `CAND` in these RID strings is an identity, not a status (DSN v1.3).

  So KT = TK need **not** be added as a separate hypothesis, and the C^∞ uniqueness question is closed. What stays open is **existence**: OPEN 20, B-∞ existence, which is also stated there for F^{1/6}/J.

  The Borel-and-iterate sequence J = lim T^{−n} J_∞ T^n is only a proposed construction route. Its convergence and the limit's properties are **not** claimed (DYAD §6.17 R1). RRF L-SHADOW-POLY is not imported. *(v0.7 said this route "builds commutation in" and "rests on L-SHADOW-POLY"; withdrawn.)*
- **Expectation `[HEUR]`.** Analytic existence is a genuine question, not a formality. In the one-dimensional holomorphic analogue (multiplier a root of unity), such splittings are governed by Écalle–Voronin-type moduli and fail generically. The C^∞ route is the more promising one.

**(f) Scoped ontological reading `[HEUR]`** (narrowed per the second co-owner, 19 Oct).

> Radial contraction eliminates flat ambiguity among admissible smooth commuting realizations. Existence remains open, and physical identification of any realization with pole exchange requires a separate ontological and representation contract (OFN OPEN-OPA; RRF OPEN-A).

This does **not** say that the choice of exchange reduces to an existence question.

**DYAD target (registered by the owner in DYAD v6.4.13 OPEN 20).** OPEN 20 is PARTIAL: B-∞ flat uniqueness is CLOSED for existing C^∞ objects; B-an, B-6 and B-∞ existence are open.

> **B-6:** does F^{1/6} = exp(⅙ log F) converge? Equivalently: does J converge; does an analytic, exactly λ-equivariant chart exist? Since B-6 ⟺ B-an ∧ B-3, a negative answer to B-an also answers B-6 negatively.
>
> **B-∞ existence:** does a C^∞ identity-tangent sixth root exist? (Commutation and uniqueness of an existing one are already THM via F3.) A positive answer gives J = T∘K⁻¹ and, via Bochner averaging, the real transported class.

## 4. FMS disposition (scoped; Standard C at cubic order)

- **A1, κ = 1 (raw):** excluded. Q4 fails (flat), and Standard C fails (§3.2). Retained as a flat-sector model.
- **B, κ = 0 (raw):** excluded from the coupled class (Q6). Retained as the decoupled reference.
- **A2, 0 < κ < 2, κ ≠ 1 (raw):** **excluded under Standard C at cubic order**, because it has no smooth invariant isolation regime through 0 (§3.2). Q6 (§3.1, now on owner RIDs) and Q4 capacity hold. Remaining loopholes: non-manifold or finite-amplitude regimes; other carriers, sharpened by OPEN-C19-L.
- **C — transported κ-family:** **primary candidate class; real once J is realized.** It is a family with a genuine in-class modulus (§3.5(a′)), not a single model.
  - **Ranges (D2):** formal properties for κ ∉ {0, 1, 2}; stability statements for 0 < κ < 2, κ ≠ 1.
  - **Satisfies:**
    - Standard C exactly on 𝒮₀ and 𝒮_±;
    - Q4 capacity;
    - Q5a with active covariance;
    - Q6: `[THM]` Genesis v2.8.9 import, plus the narrow-contract OFN corollary (§3.4), for real C³ germs.
  - **Canonical:** J, R₀, G, the lock surfaces, p, q, and the leading-order shape law (§3.5). The ψ-modulus m(a) is complete through degree 5. |c| reads m only up to the reflection m ↦ 2m* − m. The complete classification additionally uses the reflection obstruction (FMS P4). No explicit torus-invariant scalar resolving the sign of m − m* has been constructed `[OPEN]`.
  - **Dynamics:** the equilateral chiral surfaces are relatively attracting at cubic order (relative chirality, §0a). The coincidence surfaces lie on the cubic separator and are transversally repelling there. The full basin boundary is OPEN: its existence is open, and its dependence on the member is not proved (§3.4, §3.5(a′)).
  - **Open:**
    - realization of J (DYAD OPEN 20, B-6 / B-∞ existence);
    - choice of the chart ψ inside the class. This is now a genuine modulus, so a physical criterion is needed (OFN/RRF);
    - physical isolation and the chirality reading;
    - RRF registration of the model contract (§2 item 6).
- **C — other routes** (extra state variables, other couplings): open, same requirements.

**Required next tests:**
1. **DYAD (priority):** OPEN 20 B-6 (analytic F^{1/6}) and B-∞ existence for F^{1/6}/J (§3.5e). No commutation hypothesis is needed at C^∞ (DYAD F3).
2. **OFN/RRF:** the physical principle that selects ψ inside the class. A candidate readout is |c| in a declared carrier and encoding. It reads m only up to reflection. "Im c = 0" is excluded as a principle (§3.5(a′)).
3. **FMS:** the true chiral basin boundary and the rigorous parabolic rate, per member or uniformly in the modulus. Rate tests use transported-chart modes (§3.4 readout guard).
4. **FMS (optional):** ℤ₂-reflected pair: **CLOSED** (not conjugate; §3.5(a′)). Remaining: the seven first-order moduli the chart family does not reach; jets beyond degree 5; κ ∈ {0, 2}.
5. **RRF:** decision on the class-C model-contract row (§2 item 6).

**Open:** carrier realization (J / K); the in-class chart choice; identity versus merge; physical exchange beyond passive relabeling; holonomy-to-curvature interpretation; non-manifold isolation sets; the closure-mode factor; sub-C³ decouplings (Q6-REG); OPEN-C19-L.

## 5. Evidence

| File | Role |
|---|---|
| `iso_check.py` (`b92f6659…0d75e`) | §3.2 degree-2 obstruction, both lock lines |
| `iso_quadratic_nogo.py` (`91fd63f4…5308`) | §3.2 general tangent: z z̄ coefficient = −(1/3)Σ\|c_e\|², exit-gated |
| `transported_pq.py` (`2dcd4331…20bf6`) | §3.4 p = μ/3, q = 2μ/3, exact |
| `transported_chiral_pq.py` (`09129ffc251a6f9d045ca9184a613a54d2025a77d7b1e41cf951603e6b3c73ac`) | §3.4 independent check of the ν-part chiral split (ν/3, 2ν/3) |
| `transported_sim.py` (`95a86e45…81db`) | §3.4 `[NUM]`; off-plane start, transient explained |
| `basin_test.py` (`569f1430…`) | §3.4 `[NUM]`; closure-plane starts near the diagonal, 48/48 |
| `k3_six_step_factor_check.py` (`7d761090…d4ff`) | Lemma S, Gröbner (historical / confirmatory) |
| `d4_transported_cubic_cert.py` (`f4c38285…3f6d`) | Genesis §6.3c third-jet certificate, 6/6; independently run by the second co-owner |
| `OFN_PSI_KAPPA_EXTENSION_v0_1.py` (`6566009c…5f88`) | §3.5(a′) centre-manifold reduction; ψ-obstruction at sampled κ; 28/28 |
| `OFN_PSI_KAPPA_ALL_MINOR_CHECK_v0_1.py` (`c56a01ac…a9e3`) | §3.5(a′) all-κ obstruction via a constant 32×32 minor; run by both co-owners |
| `OFN_PSI_INVARIANT_C_CHECK_v0_1.py` (`18f10aa4…b114`) | §3.5(a′) closed form of c(κ, a), 12/12 |
| `OFN_PSI_INVARIANT_C_GAUGE_CHECK_v0_1.py` (`d3e5cedf…9781`) | §3.5(a′) c unchanged by 24 cubic generators; torus phase action. *v0.8.1:* sent to the second co-owner with the two scripts below; not attached to the project, to save capacity |
| FMS `FMS_PSI_QUINTIC_*` scripts and notes | κ = 1 test, all-κ minor, phase invariant (FMS SESSION) |
| `FMS_PSI_QUINTIC_FINITE_INVARIANT_v0_1.py` (`ad44f66a…445f4c`) | |c|² invariance under formal conjugacy; FMS-run with a PI run reported; not rerun by OFN |
| `FMS_PSI_QUINTIC_REFLECTION_TEST_v0_1.py` (`5af23da9…f409`) and note v0.1.1 | ℤ₂ reflection excluded, P1–P4 (P4 κ symbolic); not rerun by OFN. Note v0.1.1 §4 (|c| reads m up to reflection) has been read |
| `OFN_PSI_REFLECTION_AUDIT_v0_1.py` (`e6d9b089…235a`; needs `OFN_PSI_KAPPA_EXTENSION_v0_1.py`) | independent OFN reflection audit at κ ∈ {1, 1/2, 3}: 6 controls solvable, 6 reflected pairs GB = [1]. Also executed by the second co-owner, ALL PASS |
| `OFN_STAB_F3_CHECK_v0_1.py` (`8b415461…e5ea9`) | exact Gröbner computation of Stab(f₃) = T² ⋊ swap |
| Genesis v2.8.9 (adopted; `d143673e…c6fc`) | §3.1 raw-family RIDs; §3.4 `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` |
| DYAD v6.4.12–v6.4.15 (adopted) | formal centralizer / Corollary U (v6.4.12); J, Lemma F, F1–F3, OPEN 20 B-6 (v6.4.13); OPEN 3a (v6.4.14); OPEN 3b (v6.4.15) |
| RRF v0.8.3 (adopted working standard) | §0.3 re-imposed model rule; safety lock; §2.4b–c existence equivalence, B-6 ⟺ B-an ∧ B-3 |
| ER-2B v0.3.1 (noncanonical) | A.4 cubic cross-derivation (reproduced); C09, C19 context |
| Source review v0.1.1 + addendum v0.1 | dispositions consolidated here |

## 6. Non-claims

- No physical carrier, chirality, isolation regime or exchange operation is selected.
- Class C is not claimed to be the unique model, and the ψ-modulus is not given a physical value.
- No single-dyad result is used as a network separator or basin theorem.
- The narrow-Q6 corollary is OFN-derived. It is not a Genesis statement, and it is recorded as OFN SESSION until OFN v0.10 is adopted.
- No sub-C³, non-planar or formal-series decoupling statement is made.
- OFN v0.10 owner adoption is a separate PI decision.
