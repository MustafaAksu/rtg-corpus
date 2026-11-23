# DYAD–RRF–OFN G2 Consolidated Note v0.3

**Date:** 16 October 2026 · **Status:** REVIEW-READY / NONCANONICAL. No owner file, RID, OPEN status or custody is changed by this note.
**Changes from v0.2:**
- §2a: OPEN 19 closure candidate (formal centralizer of T⁶), with an independent recheck. Regularity boundary added: j^∞ statements need R ∈ C^∞ or analytic.
- §3a: the factor dimension split is recorded. d = 1 and d = 3 are excluded at C¹; d = 2 needs C³ in the present proof.
- §5 caveat (ii): normalizer freedom is the centralizer only for a fixed normal form; across normal-form representatives it is a general normal-form conjugacy.
- §7: absence of a planar factor is not absence of an invariant embedding.

**Changes from v0.1:**
- §5b: the two κ = 1 models are not related by a passive recharting. This follows ChatGPT's independent review.
- §2: ChatGPT's independent check is recorded. New §2a relates the lemma to DYAD v6.4.11 §6.15 and OPEN 19.
- §3a: the Genesis K3 cubic-factor obstruction is added, with an independent re-check of its source identities.
- §7 table and §8 OPEN list are updated to match.
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

## 2. Uniqueness lemma `[ALG — formal]` (DYAD; independently checked by ChatGPT, 16 Oct)

Every formal involution commuting with T is either I or Ŝ.

**Proof.**
1. DR(0) commutes with A. The commutant of A consists of complex scalars, so DR(0) = ±I.
2. R commutes with Ŝ. Indeed, R commutes with g := T⁶, so R g^{1/2} R⁻¹ is a tangent-to-identity square root of R g R⁻¹ = g. Tangent-to-identity roots are unique: log is a bijection from tangent-to-identity formal maps onto formal vector fields of order ≥ 2 (characteristic 0), and a² = exp(2 log a). Hence R commutes with g^{−1/2}, and so with Ŝ = T³g^{−1/2}.
3. If DR(0) = −I, then RŜ is tangent to the identity. Since R and Ŝ are commuting involutions, (RŜ)² = R²Ŝ² = I.
4. A tangent-to-identity involution is the identity: if C = I + c_k + …, then C² = I + 2c_k + …, so c_k = 0, and by induction C = I. Hence R = Ŝ.

All steps hold over ℝ. No normal form, no centralizer description and no assumption on the lattice term a₀₅z̄⁵ is used.

## 2a. Relation to DYAD v6.4.11 §6.15 and OPEN 19 (for DYAD owner review)

DYAD v6.4.11 registers DYAD-THM-LOCAL-INVOLUTION-GERM (§6.15). A non-identity local involution R commuting with the return has DR(0) = −I. The two cases are:
- (a) R is C¹ and commutes with T;
- (b) R is C³ and commutes with T⁶, in the tube U_T.

DYAD records "j^∞R = Ŝ" as conditional on OPEN 19 (DYAD-OPEN-FORMAL-CENTRALIZER, "is the tangent-to-identity centralizer {exp(sX̂)}?").

- **Branch (a), primitive clock.** §2 above proves j^∞R = Ŝ directly whenever R is C^∞ or analytic, so that its jet is a formal involution commuting with ĵT. Step 2 uses only uniqueness of unipotent roots. So OPEN 19 is **not needed** for branch (a). Proposed DYAD action: record j^∞R = Ŝ for branch (a) as `[ALG — formal]` via §2. The §5 risk-table entry "j^∞R = Ŝ without OPEN 19" then applies only to branch (b).
- **Branch (b), six-step clock.** Here R commutes only with T⁶, and step 2 fails: commuting with g does not give commuting with T³. Reduction:
  1. R commutes with g = exp(X̂). So exp(R_*X̂) = exp(X̂), and R_*X̂ = X̂ by uniqueness of log.
  2. Ŝ also preserves X̂.
  3. Therefore C = RŜ is a tangent-to-identity symmetry of X̂.
  4. If that centralizer is {exp(sX̂)} (OPEN 19), then C commutes with Ŝ, and R = Ŝ follows as DYAD states.
  
  OPEN 19 therefore remains the genuine gate for branch (b) only. Its question can be stated without f: it asks for the tangent-to-identity symmetries of the formal vector field X̂ = log T⁶.

**Regularity boundary (ChatGPT, accepted).** j^∞R is defined only for C^∞ (or analytic) R. The formal results therefore strengthen §6.15 only in that sub-case. The C¹ statement (a) and the C³ statement (b) stand as registered, and nothing formal is transferred to them.

**OPEN 19 closure candidate (PI/ChatGPT session, 16 Oct) `[THM — formal; SESSION, owner adoption pending]`.** For F = T⁶ and X = log F, the real identity-tangent formal centralizer of F is {exp(sX) : s ∈ ℝ}.

*Proof sketch.*
1. If G = exp(Y) commutes with F, then G_*X = X, so e^{ad Y}X = X.
2. ad Y raises degree, so the factor (e^{ad Y} − 1)/ad Y is invertible, and [Y, X] = 0.
3. The lowest-degree part gives [Y_k, X₃] = 0, with X₃ = μ|W|²W.
4. ker ad_{X₃} = ℝX₃, which lives in degree 3 only. Hence Y₃ = sX₃, and the same argument applied to Y − sX gives Y = sX.

*Independent check (Claude, `centk.py`, exact sympy rational ranks; not the session's `cent.py`).* The real kernel dimension of ad_{X₃} on degree-k fields, for k = 2,…,13, is:

| μ | Kernel dimension, k = 2…13 |
|---|---|
| selected μ = −1/2 − 2i√3/3 | 0, 1, 0, 0, …, 0 — **confirmed** |
| real μ (Im μ = 0, control) | 0, 3, 0, … — rotations survive |
| imaginary μ (Re μ = 0, control) | 1 in every odd degree — the \|W\|^{2m}W family survives |

So both Re μ ≠ 0 and Im μ ≠ 0 are needed, as the proposed text states. The lattice term enters only at degree ≥ 5, above the lowest-degree comparison, and plays no role.

*Consequences.*
- Branch (b): C = R̂Ŝ lies in Cent(F) = {exp(sX)} and commutes with Ŝ, so R̂² = exp(2sX) = id, hence s = 0 and R̂ = Ŝ.
- Branch (a) has the simpler direct proof: T³R̂ is identity-tangent with (T³R̂)² = F, so R̂ = T³F^{−1/2} = Ŝ.
- A formal involution commuting only with T⁶ therefore commutes with T. This holds formally only; the factor contracts EF = TE and EF = T⁶E remain distinct.

This is a proposed owner reading, not a registration. DYAD decides.

**DSN bookkeeping proposal.**
- Keep DYAD-OPEN-FORMAL-CENTRALIZER as a CLOSED pointer.
- Register the result under a THM RID (for example DYAD-THM-FORMAL-CENTRALIZER) with `cent.py` and its output as evidence.
- Until adoption, the RRF v0.8.1 §6.2 guard ("do not transfer T-uniqueness to a T⁶-only hypothesis") stays in force.

## 3. κ-family classification `[THM — conditional, raw encoding]` (DYAD/RRF)

F_κ(r)_e = T(r_e) − (κ/3)·Σ_j T(r_j), with E_e(r) = r_e.

- E_eF_κ − TE_e = −(κ/3)ΣT. ΣF_κ = (1 − κ)ΣT.
- Witness (x, 0, −x), x = (ρ, 0): ΣT = (0, 2(cosh ρ − 1)) ≠ 0. Only the even part of T is used, not μ.
- Over any neighbourhood of 0: primitive autonomous-edge factorization holds ⟺ κ = 0. Raw additive closure is preserved on every closed state ⟺ κ = 1.
- For any F (not only κ-family) on the raw carrier, exact additive closure together with all edges autonomous is impossible, by the same witness.

## 3a. K3 cubic-factor obstruction `[THM — exact, conditional on the model]` (Genesis; [SESSION] record v0.1, 16 Oct)

**Statement.** The raw κ = 1 model F₁ = P_C T^{×3} has no C³ planar factor. That is, there is no C³ submersion E and planar C³ map T' with E∘F₁ = T'∘E near 0. The fixed point, linear part and cubic coefficient of T' are all left free.

**Mechanism.** In the chiral modes u = w₁ + λw₂ and v = w₁ + λ̄w₂, the six-step cubic is
- u(f₃) = c₀u|u|² − iβ*Nu,
- v(f₃) = c₀v|v|² − iβ*Nv,

where N = |u|² + |v|² and β* = 2√3/9 ≠ 0. The phase coupling through N cannot be pushed down to any plane.

**Independent re-check (Claude, own code, mpmath 50 dps; not the record's scripts).**
- Built F₁ from T directly.
- The numerical cubic of F₁⁶ matches the record's f₃ (ν = 1/6 − i√3/3, χ = 1/3). The residual is 6.9·10⁻⁵ at ε = 10⁻³ and 6.9·10⁻⁶ at ε = 10⁻⁴, scaling as O(ε) as expected for the quartic remainder.
- N = |u|² + |v|² holds to 10⁻⁵¹.
- Both chiral identities hold to 10⁻⁵¹.
- The §2(e) monomial elimination was read and is correct.

**Placement in G2.**
- Strengthens the raw-additive row of §7: on the raw carrier, κ = 1 fails autonomous-edge factorization (§3) and also admits no planar C³ factor of any kind.
- Dimension split: d = 1 and d = 3 are already excluded at C¹, since a real λ-invariant subspace must have even dimension. Only d = 2 needs C³ in the present proof, so the C¹/C² OPEN concerns d = 2 only.
- Does **not** cover the h-transported carrier (§5b), C¹/C² factors, factors of dimension ≥ 3, or the physical exchange action. The record states these limits itself.

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
- **Node symmetry:** node transposition = slot transposition ∘ reversal, so the model is node-permutation equivariant. (Formal; independently checked by ChatGPT, 16 Oct.)
- **Standard B:** on (z, −z, 0) we have ΣN = 0, so 𝓕_sym restricts to N. The coincidence stratum is the fixed set of a node transposition and is invariant (equivariance lemma). Standard B is realized by the coincidence embedding ι(u) = (u, Ŝu, 0) in original coordinates.
- **Standard A:** fails, because N is not additive.

**Contrast with raw-carrier κ = 1 (projected K₃).** That model is symmetric only under edge-slot permutations; node transposition is broken by T's even part (verified numerically 14 Oct). Its coincidence stratum is not invariant, and it has no C³ planar factor (§3a).

`[ALG — formal]` The symmetric model is obtained by imposing additive closure and projection in normal-form coordinates. It is a distinct conditional network construction, not merely a passive recharting of the raw projected K₃ model: the true transport of the raw model is H⁻¹P_C T^{×3}H with H = h^{×3}, which in general differs from P_C N^{×3}. Its node-equivariance and coincidence invariance are exact formal properties of that construction. This agrees with RRF's §0 representation lock.

**Caveats.**
- (i) Everything is formal. The finite h₆ gives oddness only to degree 6; RRF VF-1 records an even degree-10 term for the delivered F̂.
- (ii) **Non-canonical carrier.** The transported group law depends on h. Normalizers leading to the same normal form N differ by elements of the formal centralizer of N, which are generally non-additive. Normalizers leading to different admissible normal-form representatives are related by a more general normal-form conjugacy (ChatGPT). So, unlike Ŝ, the transported closure is not intrinsic. The DYAD-ALG-NF6 convention fixes it only through degree 6. Selecting it physically is OPEN.
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
| Group-type, raw additive | Excluded (§3, §4); κ = 1 has no C³ planar factor at all (§3a) | Not available (D_Ŝ ⊄ raw C) | Open. §3a restricts the extended factor class for κ = 1; it does not exclude 2D invariant embeddings or other B routes |
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
6. **DYAD OPEN 19:** a closure candidate exists (§2a). Owner adoption is pending. The C¹/C³ (non-C^∞) uniqueness question stays separate.
7. **K3 record provenance:** manifest and execution receipt for `fac.py`. This is confirmatory only.

## 9. Ownership and next steps

- **DYAD:** one written proof note covering §1 (G1), §2 (uniqueness), §3 (κ), §4 (group obstruction), and §5 as formal constructions. Also the §2a reading of §6.15 and OPEN 19, for the next DYAD revision.
- **Genesis:** owns §3a. G2 consumers cite it as `[import: Genesis K3-CUBIC-FACTOR-OBSTRUCTION | RID unavailable — SESSION record]` until Genesis registers it.
- **RRF:** evaluate §5b as an h-transported carrier profile candidate, given the §0 lock and canonicity caveat (ii). No registration implied.
- **OFN v0.10:** receive §7 and §8 as decision structure and OPENs; no theorem ownership.
- No new campaign is needed. §2 and §5b have been independently checked. §2a has not yet been independently checked; it is requested from DYAD review.
- Technical theorems are not recorded as OFN results before DYAD/Genesis acceptance.
