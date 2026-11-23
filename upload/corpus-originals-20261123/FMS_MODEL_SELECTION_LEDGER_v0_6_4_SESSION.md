# FMS MODEL SELECTION LEDGER v0.6.4 — SESSION

**Date:** 2026-10-19
**Profile:** Foundations & Model Selection (FMS) working ledger — noncanonical
**Owner:** FMS (proposed). Scientific theorems remain with their owners (DYAD, Genesis, RRF, OFN, NUMGEN).
**Lifecycle:** `[SESSION]` — NOT owner adopted. No adopted DSN is modified by this file.
**Supersedes:** FMS Ledger v0.6.3 SESSION. Earlier versions remain historical records; the present ledger consolidates v0.6–v0.6.2 and the κ=2 parity-restricted result.
**Vocabulary:** `SUFFICIENT`, `NECESSARY`, `EXCLUDED UNDER ASSUMPTIONS`, `UNRESOLVED` are model-assessment verdicts under explicitly stated premises. They are not adoption or task statuses.

> **Reading rule.** Every row says *which source grade* supports it. An owner-adopted theorem is marked `[OWNER]` with its RID. A result proved in session but not adopted is marked `[SESSION]`. A SESSION result is never cited as an owner result.

---

## 0. Source manifest

| Source | Version used | Grade | Used for |
|---|---|---|---|
| `RTG_GENESIS_GEOMETRY_DSN` | v2.8.7 (file available; adopted status reported in project record) | `[OWNER]` | `GEN-THM-K3-PLANAR-FACTOR-NOGO`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`; mean-feedback theorem distinct |
| `RTG_DYADIC_OSCILLATOR_DSN` | v6.4.13 (adopted 18 Oct 2026; file inspected) | `[OWNER]` | §6.16 formal canonical Z6 generator, §6.17 Lemma F and F1–F3 conditional smooth uniqueness/commutation; OPEN 20 B-an, B-6, B-infinity existence remain open |
| `RTG_RRF_REPRESENTATION_REGISTRY` | v0.8.2 (adopted working standard, 17 Oct 2026) | `[OWNER — RRF working standard]` | G2 contract, clock/regularity declarations |
| `RTG_ONTOLOGICAL_FOUNDATIONS` | v0.9 (available owner baseline); v0.7.1 OFN response reported as SESSION and not adopted into OFN v0.10 | `[OWNER baseline / SESSION response]` | identity/exchange baseline; model-selection decisions are co-owner SESSION input, PI adoption outstanding |
| `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD` | v0.1.2 | source of the Genesis owner theorem | proof record |
| Session computations 14–17 Oct 2026 | §10 | `[SESSION]` | general-κ coefficients, Theorem 6S, Lemma S′, tangent classification |

FMS Ledger v0.3 and v0.4 texts were not available to the author of this file. v0.5 is rebuilt from v0.2 plus the deltas reported for v0.3/v0.4 and the session results of 16–17 October.

---

## 1. Selection conditions (kept separate)

- **C — Exact additive closure** in the declared carrier: `h = Σ_e r_e = 0` at every primitive step.
- **C′ — Dynamically selected closure:** an invariant, locally attracting manifold `h = ψ(u)` tangent to the closure plane. Closure is approached, not imposed.
- **A — Primitive edge autonomy:** a local submersive factor `E∘F = T∘E` onto the isolated DYAD map. This is distinct from a factor for `T⁶`.
- **A6 — Six-step edge autonomy:** a factor `E∘F⁶ = T′∘E` onto a neutral (unit-circle spectrum) planar return.
- **I — Exact node-coincidence preservation**, after the full-state encoding and the clock are fixed. The raw condition `r_BC = 0` is not enough.
- **X — An actual local exchange involution:** well defined on encoding fibres and commuting with the declared evolution. Formal uniqueness does not give existence.
- **H — Holonomy behaviour:** absolute or normalized. Additive holonomy depends on the carrier and is not automatically curvature.
- **R — Regularity:** C¹, C³, C⁵, C^∞ or real-analytic, declared explicitly.

---

## 2. Results register

| ID | Result | Grade | Scope |
|---|---|---|---|
| R1 | Projected K3 (κ=1) primitive update: no local C³ submersive planar factor; d=1,3 excluded at C¹ | `[OWNER]` `GEN-THM-K3-PLANAR-FACTOR-NOGO` | 4-real-dim closure state space |
| R2 | Formal centralizer of `F=T⁶` tangent to identity = {exp(sX)}; unique formal involution with linear part −I, equal to Ŝ = T³F^{−1/2}; analytic six-step involution commutes exactly with T | `[OWNER]` DYAD v6.4.12 RIDs above | formal / analytic; realization is OPEN 20 |
| R3 | Full formal centralizer of T: Cent_formal(T) = {T^k exp(sX) : k ∈ {0,…,5}, s ∈ ℝ} (bijective parametrization; T⁶ = exp X ≠ id); linear multipliers restricted to μ₆ because a₀₅ ≠ 0 | `[SESSION — ALG]` | formal (§5.2) |
| R4 | Tangent classification of invariant closures for independent edges | `[SESSION — ALG]` | §5 |
| R4′ | Carrier independence: with the state exactly three edges and full primitive autonomy, no carrier or encoding admits a C³ invariant closure genuinely involving all three edges | `[SESSION — ALG]` | §5.3 |
| R5 | General-κ centre manifold ψ₂ and exact reduced chiral coefficients p(κ), q(κ) | `[SESSION — ALG]` | §6 |
| R6 | Lemma S′: real-linear cubic factor obstruction for p ≠ 0, q ≠ 0 | `[OWNER]` Genesis v2.8.7 `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` | §7.2 |
| R7 | Theorem 6S: no neutral low-dimensional factor, primitive or six-step clock, for κ ∈ ℝ∖{0,2} | `[OWNER]` Genesis v2.8.7: `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` (core); `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` (spectrally restricted) | §7 |
| R8 | κ=0 relative holonomy limit `|h_m|/√N_m → L ≥ 0`, with `|h_m| → 0` | conditional local theorem (NUMGEN/DYAD provenance) | isolated-edge tube initializations |

---

## 3. Base model assessment

Primitive law; columns refer to §1. "Excluded" always means `EXCLUDED UNDER ASSUMPTIONS` for the named condition.

| Model class | C | C′ | A (primitive) | A6 (six-step, neutral target) | H | Support |
|---|---|---|---|---|---|---|
| **κ = 0** — independent edges | no (generic) | **no**: no invariant C³ closure tangent to any three-edge plane (§5) | **yes** (raw `E_e = r_e`) | yes | `|h|→0`, `|h|/√N → L ≥ 0`; L may vanish | R4, R8 |
| **κ = 1** — projected K3 | **yes** in raw additive carrier | trivially (ψ ≡ 0) | **no**: C³, d=2; C¹, d=1,3 | **no** (OWNER, six-step core) | h = 0 by construction | R1 `[OWNER]`; six-step extension R7 `[OWNER]` |
| **0 < κ < 2, κ ≠ 1** | no | **yes**: attracting C^r centre manifold `h = ψ(u) = O(|u|²)`, attraction transverse only | **no** for neutral targets (OWNER, spectral hypothesis) | **no** (OWNER, spectral hypothesis) | h slaved to u; not free | R5, R7 |
| **κ < 0 or κ > 2** | no | invariant manifold exists but is normally repelling | **no** for neutral targets (OWNER, spectral hypothesis) | **no** (OWNER, spectral hypothesis) | not certified | R5, R7 |
| **κ = 2** | no | **raw family:** quadratic resonance in ψ₂; **transported odd family:** ψ₂=0, odd centre-graph unique but even-degree resonances persist | `UNRESOLVED` | `UNRESOLVED` | — | OPEN (general formal conjugacy); see §12C |
| **Outside the κ family** | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | — |

**Scope of the no-factor rows.** They exclude local C³ submersive factors whose target linearization has spectrum disjoint from the closure-mode spectrum (unit-circle target spectrum suffices). They do not exclude C¹/C² rank-2 factors, factors onto the closure mode itself (e.g. `E_h = Σ r_e` at κ = 1, target = zero map), non-submersive encodings, or other network dynamics.

---

## 4. Carrier / clock / regularity overlay

| Item | Primitive clock T | Six-step clock T⁶ | Grade |
|---|---|---|---|
| Formal exchange jet | unique, = Ŝ (G1 square-root argument; covered by `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`) | unique, = Ŝ (`DYAD-THM-FORMAL-CENTRALIZER`) | `[OWNER]` formal |
| Analytic involution commuting with T⁶, DR(0) = −I | — | commutes exactly with T | `[OWNER]` `DYAD-THM-ANALYTIC-CLOCK-BRIDGE` |
| C^∞ involution commuting with T⁶ | — | exact commutation conditional on existence (DYAD v6.4.13 Lemma F/F3) | `[OWNER]`; existence OPEN 20 |
| Existence of an analytic or C^∞ odd carrier | — | — | `[OPEN]` OPEN 20 (Problem B) |
| Raw carrier, R = −I | not a symmetry (T is not odd) | not automatically a six-step symmetry | `[ALG]` |
| Finite charts B₂, B₆ | finite-order only | finite-order only | not an exact coincidence theorem |

**Separation rule.** Formal uniqueness of the exchange jet (R2, R3) is a statement about *which* object would have to be realized. It is not evidence that a real carrier exists, and not a physical selection. Every realization contract must declare `regularity`, `clock`, domain, encoding E and fibre compatibility (RRF v0.8.2 §6.2).

**Regularity gates.**

| R | Supported | Still open |
|---|---|---|
| C¹ | involution-germ dichotomy (`DYAD-THM-LOCAL-INVOLUTION-GERM`); d=1,3 factor exclusion | rank-2 factors |
| C³ | rank-2 neutral factor exclusion (R1, R7); three-edge closure tangency (§5.1) | odd-carrier existence |
| C⁵ | lock tangents restricted to μ₆ (§5.2) | full lock-manifold classification |
| C^∞ | formal j^∞R = Ŝ if a true involution exists | realization only; conditional flat uniqueness/commutation owner-closed |
| analytic | formal j^∞R = Ŝ; exact T-commutation from T⁶-commutation | existence |

---

## 5. Invariant closures for independent edges (κ = 0) `[SESSION — ALG]`

### 5.1 Three-edge tangency obstruction (C³)

On three independent edges, `D⁶(w) = w + μ(w_e|w_e|²)_e + O(|w|⁴)`. This cubic is unchanged by tangent-to-identity coordinate changes, because D⁶ has no quadratic part.

Let M be a local C³ manifold through 0 of real codimension 2, **invariant under the primitive map D = T^{×3}** (not only under D⁶). Primitive invariance is what makes the tangent P invariant under DD(0) = A⊕A⊕A. Every such real subspace is complex for J = (A − cos(π/3) I)/sin(π/3). Hence P = {Σ a_e w_e = 0} is a complex hyperplane. No separate complex-linearity hypothesis is needed. Odd real codimensions cannot occur.

Cubic tangency requires `Σ a_e w_e|w_e|² = 0` on P. This forces:

- **one nonzero coefficient:** P = {w_k = 0};
- **two:** P = {w_i = c w_j} with |c| = 1;
- **three:** impossible. Setting w₂ = 0 and then w₁ = 0 gives |a₁/a₃| = |a₂/a₃| = 1. The point w = (a₃/a₁, a₃/a₂, −2) then gives the cubic value −6a₃ ≠ 0.

**Conclusion.** No C³ invariant closure manifold of independent edges is tangent to a genuine three-edge relation. This covers every curved version of triangle closure with such a tangent.

### 5.2 Fifth-order lock restriction (C⁵)

For a lock tangent w_i = c w_j, write the manifold as w_i = G(w_j, w_k). The argument works in the six-step normal-form jet J = z + μ z²z̄ + a₃₂ z³z̄² + a₀₅ z̄⁵, with a₀₅ = 6λ̄ n₀₅ ≠ 0 (DYAD).

1. **Degree 3:** |c| = 1.
2. **Degree 4:** the operator on quadratic maps G₂(w_j, w_k) has zero kernel for every |c| = 1. The 20×20 minor equals const·(1+t²)⁴⁰ under c = (1−t²+2it)/(1+t²); c = −1 is checked separately. Hence G₂ = 0.
3. **Degree 5:** without step 2, the z̄⁵ coefficient contains an h₀₂² contamination. With G₂ = 0 it is ∝ (c − c̄⁵). Monomials containing w_k cannot reach pure w̄_j⁵. Hence **c⁶ = 1**.

**Result.** The tangent of every C⁵ invariant codimension-2 manifold is w_k = 0 or w_i = λ^m w_j (m ∈ ℤ₆). Two-edge formal locks are exactly the graphs w_i = T^k exp(sX)(w_j), k ∈ {0,…,5}, s ∈ ℝ. The special cases are coincidence (k = 0, s = 0) and the Ŝ-lock (k = 3, s = −1/2).

**OPEN.** Whether a lock-tangent manifold that depends on the third edge at higher order must itself be a centralizer graph.

**Remark on a₀₅.** DYAD v6.4.12 states that a₀₅ plays no role in OPEN 19. That is correct for the tangent-to-identity centralizer. For the full centralizer of T, a₀₅ is what restricts the linear multipliers to μ₆. The two statements are consistent.

### 5.3 Carrier independence `[SESSION — ALG]` (corollary of §5.1)

**Hypotheses.**
1. The physical state is exactly the three edges: the joint encoding E = (E₁, E₂, E₃) is a local C³ diffeomorphism ℝ⁶ → ℝ⁶ with E(0) = 0.
2. Every edge is primitively autonomous: E_e∘F = T∘E_e. Hence F = E⁻¹∘T^{×3}∘E.
3. Closure is a C³ codimension-2 submanifold through 0 preserved by F, either exactly (Q1) or as an invariant attracting manifold (Q2).

**Conclusion.** E maps the closure to a C³ invariant manifold of T^{×3}. By §5.1 its tangent is w_k = 0 or a two-edge lock w_i = c·w_j, with |c| = 1 at C³ and c⁶ = 1 at C⁵. **A closure that genuinely involves all three edges is impossible in any carrier and any encoding**, group-type or not, curved or flat.

**Special cases.** The κ = 0 raw-carrier row (§3) and the formal group-closure no-go of the G2 note §4 (which needs T⁶ ≠ I) are both special cases.

**Consequence for class C.** While the state is three edges and E is a joint diffeomorphism, changing the carrier or the encoding is **not** an escape. The genuine routes are:

| Route | Content |
|---|---|
| C-a | extra state variables, so that the state dimension exceeds six (connection, holonomy, node data) |
| C-b | partial or asymmetric autonomy (Q3b in the OFN request) |
| C-c | regularity below C³ |
| C-d | non-submersive or singular encodings at 0 |
| C-e | closure that is not a codimension-2 manifold through 0 |

No new computation: the proposition follows from §5.1 by conjugation. Ownership goes with §5.1 (FMS/Genesis). Source: review `FMS_v0_5_AND_OFN_REQUEST_REVIEW_v0_1.md` §2.

---

## 6. General κ family `[SESSION — ALG]`

`r_e⁺ = T(r_e) − (κ/3) Σ_j T(r_j)`. Split `r_e = u_e + h/3` with u ∈ 𝒞:

- `u⁺ = P T^{×3}(r)`
- `h⁺ = (1−κ) Σ T(r)`

**Linear part.** λ on 𝒞; (1−κ)λ on the closure mode.

**Centre manifold.** `h = ψ(u)`. ψ₂ is solved exactly. Denominator (κ−2)(κ²−κ+1); ψ₂ ≡ 0 at κ = 1. The only real singularity is κ = 2, a quadratic resonance where (1−κ)λ = λ̄². The formal manifold exists to all orders for κ ∉ {0, 2}. It is attracting in the normal direction for 0 < κ < 2. At κ = 0 it fails at cubic order, consistent with §5.1.

**Reduced six-step cubic.** By S₃ equivariance it has the chiral form `u(f) = p u|u|² + q |v|² u`, with u = w₁ + λw₂ and v = w₁ + λ̄w₂. The v-component follows from the 1↔2 transposition, which maps u ↦ λv.

```
q(κ) = −(2/3)(κ−1)³ / ((κ−2)(κ²−κ+1))  −  i (2√3/9)(2κ²−3κ+2)/(κ²−κ+1)
p(κ) = −(κ²−3κ+1) / (6(κ²−κ+1))         −  i (√3/9)(2κ²−3κ+2)/(κ²−κ+1)
```

**Proof of exactness.** G₂ is κ-free and G₃ is affine in ψ₂, so q·D is a polynomial of degree ≤ 3. Exact rational arithmetic at seven κ values determines it from four points and verifies three. The other monomials vanish by the same bound.

**Structural facts.**

- Im q = 2 Im p, and 2κ²−3κ+2 = 2(κ−3/4)² + 7/8 > 0. Hence p ≠ 0 and q ≠ 0 for every real κ.
- **Re q = 0 ⟺ κ = 1.** The chiral intensities |u|², |v|² decouple at cubic order only under exact projection. ER-2B shape-sphere integrals must not be transported to κ ≠ 1 unchanged.
- Re p changes sign at κ = (3∓√5)/2 = φ^{∓2}. Mathematical observation only; no physical reading.
- Check at κ = 1: q = −i·2√3/9 = −iβ*, p = c₀ − iβ*. This agrees with R1.

---

## 7. Theorem 6S and Lemma S′ `[THM — SESSION]`

### 7.1 Statement

> For every real κ ∉ {0, 2}, the six-real-dimensional κ-family update admits no local C³ submersive dynamical factor of real dimension 1, 2 or 3, under either `E∘F_κ = T′∘E` or `E∘F_κ⁶ = T′∘E`, **provided** spec(DT′(p)), p = E(0), is disjoint from the corresponding closure-mode spectrum. The closure-mode spectrum is {(1−κ)λ, (1−κ)λ̄} for the primitive clock and {(1−κ)⁶} for the six-step clock. Unit-circle target spectrum is a sufficient condition.

**Spectral disjointness is a sufficient hypothesis, not a necessary one.** It makes the Sylvester operator invertible. A particular factor may still have L_H = 0 when the spectra meet.

### 7.2 Proof structure

1. **Sylvester step.** H and 𝒞 are invariant under DF. `L M = B L` restricts to `L_H M_H = B L_H`, and disjointness gives L_H = 0. At κ = 1, M_H = 0 and the hypothesis reads 0 ∉ spec(B), which excludes `E_h`.
2. **Reduction.** L|_𝒞 is surjective. E restricted to the C^r centre manifold is a submersive factor of the reduced dynamics.
3. **Primitive clock, d = 2.** `L_C λ = B L_C` with L_C surjective gives spec(B) ⊆ {λ, λ̄}, so B ~ A is derived. The induced six-step factor satisfies disjointness automatically, since (1−κ)⁶ ≠ 1.
4. **Primitive clock, d = 1.** B is a real scalar b. Disjointness is automatic for κ ≠ 1 and means b ≠ 0 at κ = 1. Then L_H = 0 and L_C = 0, contradicting surjectivity.
5. **Six-step clock.** The reduced return is tangent to the identity, so B = I on the image and t₂ = 0. At degree 3, ℓ∘f is constant on the fibres of ℓ.
6. **Lemma S′** (p ≠ 0, q ≠ 0 ⇒ no real-linear factor of rank 1, 2, 3):
   - (i) The factor condition is equivalent to Df(x)K ⊆ K for all x, with K = ker ℓ (f is cubic).
   - (ii) N_α = Df(e^{iα}, 0) − Df(1, 0) acts as (δu, δv) ↦ (p(e^{2iα}−1) δū, 0), and symmetrically N′_α = Df(0, e^{iα}) − Df(0, 1) acts as (δu, δv) ↦ (0, p(e^{2iα}−1) δv̄). The real span of {e^{2iα}−1} is ℂ. Using p ≠ 0: if π_u(K) ≠ 0 then ℂ_u ⊆ K (from N_α), and if π_v(K) ≠ 0 then ℂ_v ⊆ K (from N′_α). Hence K ∈ {0, ℂ_u, ℂ_v, ℂ²}, which excludes d = 1, 3.
   - (iii) For K = ℂ_u, the v-component of Df(x)(δu, 0) is q v(ū δu + u δū), which forces q = 0. Likewise for ℂ_v. Hence d = 2 is excluded for q ≠ 0.
   - Sharpness: at q = 0, ℓ = u is a factor.
   - The Gröbner elimination (`k3_six_step_factor_check.py`, 14/14 charts, ALL PASS, as reported) is now independent confirmation, not a required input.
7. p(κ), q(κ) ≠ 0 (§6).

**Relation to R1.** Within the same model and admissible factor class, every primitive-clock factor induces a six-step-clock factor. Theorem 6S therefore also excludes primitive factors within its regularity and spectral hypotheses. It does not absorb the owner theorem's C¹ scope or its state-space convention.

**Not covered.** Factors whose target spectrum meets the closure-mode spectrum; C¹/C² rank-2 factors; κ ∈ {0, 2}; transported-carrier network models; other network dynamics; physical realization.

---

## 8. Model classes for the OFN decision

| Class | Model | What the mathematics establishes | Grade of support |
|---|---|---|---|
| **A1** — exact closure | κ = 1 | C holds; no neutral low-dimensional primitive or six-step factor | `[OWNER]` R1 and R7 |
| **A2** — dynamically selected closure | 0 < κ < 2, κ ≠ 1 | C′ holds (transversally attracting curved closure); no neutral low-dimensional factor under either clock under the spectral hypothesis; chiral intensities coupled (Re q ≠ 0) | `[SESSION]` R5; `[OWNER]` R7 |
| **B** — primitive autonomy | κ = 0 | A holds; C fails; no invariant C³ curved three-edge closure; relative holonomy L ≥ 0 | `[SESSION]` R4; R8 conditional |
| **C** — alternative realization | outside the tested class | if the state is exactly three edges, carrier or encoding changes do not help (§5.3); the genuine routes are C-a extra state variables, C-b partial/asymmetric autonomy, C-c sub-C³ regularity, C-d singular encodings, C-e non-manifold closure | `UNRESOLVED` |

**Elimination statement, scoped.**

- **Closure + full primitive autonomy:** if the physical state is exactly three edges, no carrier and no C³ encoding satisfies both a three-edge closure (C or C′) and autonomy of all three edges (§5.3). This does not depend on raw edge encoding. Raw additivity enters only the *definition* of C at κ = 1.
- **Within the κ family:** the autonomy failures (R1, R7) hold for every C³ submersive E, not only the raw one. Changing the clock from primitive to six-step does not recover autonomy.
- **Partial autonomy (Q3b) in the κ family:** A1 and A2 admit no neutral planar factor at all, so they fail partial autonomy too. Partial autonomy is realized only outside the κ family, and only formally so far (§9).

These are statements about the stated classes. They are not theorems about all RTG realizations.

**No verdict here.** FMS does not pre-assign `SUFFICIENT`/`NECESSARY` to A1, A2, B or C. These verdicts follow only after OFN states which physical requirements it counts as `NECESSARY` (see the companion OFN decision request).

---

## 9. Open items

| Item | Owner | State |
|---|---|---|
| Theorem 6S, Lemma S′, exact p(κ), q(κ), ψ₂ | Genesis | v2.8.7 owner theorems adopted as reported; verify current source manifest before use |
| RRF import | RRF | `GEN-THM-K3-PLANAR-FACTOR-NOGO` importable now (v0.8.3); Theorem 6S import now eligible, subject to RRF release/lifecycle review |
| Analytic / C^∞ odd carrier | DYAD | OPEN 20 |
| C¹/C² rank-2 factors | Genesis | OPEN |
| Factors onto the closure mode (target spectrum meeting it) | Genesis | OPEN; not G2-relevant |
| κ = 2 resonance | Genesis / FMS | OPEN for general formal conjugacy; transported odd-conjugacy quintic obstruction is SESSION established (§12C) |
| Third-edge-dependent lock manifolds | FMS / Genesis | OPEN (tangent classified) |
| Partial-autonomy construction (G2 note §5a: F(z) = (Nz₁, Nz₂, −Nz₁−Nz₂); exact transported closure; edges 1, 2 exact factors onto T via E_e = h∘z_e) | DYAD / RRF | formal only: depends on the normalizer h, needs OPEN 20 for a real carrier, breaks node symmetry |
| Independent reruns requested by K3 note v0.3 §6: `kappa_pq_symbolic.py`, `lemmaS_hand_identities.py` | Genesis | files not in this author's workspace; `exact_q.py` (§10) is an independent derivation of p(κ), q(κ) |
| Physical requirements; choice among A1/A2/B/C | OFN | **decision requested** |
| G2 physical realization | OFN / RRF | CONTRACT READY; realization OPEN |

---

## 10. Session evidence

| Artifact | SHA-256 | Role |
|---|---|---|
| `cent.py` / `cent_output.txt` | `c61890682c7e07a6eb3e7c19e28698e5556a963cec706a174669cfedc1cb4624` / `eacf66b872e1a22046a1da6ccfa69201ec24c84a04d5d03326db3d21b908ee03` | ker ad_{X₃} for k = 2..13 (cross-check of `DYAD-ALG-CENT-KERNEL`) |
| `lock5.py` / `lock5_output.txt` | `0f24df601a35b648991bd51e334188c063b291b28e4a78025fdc03a6a723bf23` / `4aaf73d82a2481f07df775af77384a1d38f8df177b78bce9df7f2a8bc8388d31` | §5.2: G₂ = 0, c⁶ = 1 |
| `cm.py`, `fit.py` / `fit_output.txt` | `4c74e53d936338dcb10a914f3e14de6cba124b3a6db5c46b338be0cad9bb5eb8`, `9271943368dce208146990ed85e3546b3d84f3c715c9362d9efc8d812266705e` / `33ae187df6f5244466a95599145252fc3d6f6acef964c69266ca6bbbc6e828cc` | §6: ψ₂ exact, numerical p, q at 15 κ |
| `exact_q.py` / `exact_q_output.txt` | `44105683b5da2b57fa9dfbd2f9e05488107c560f7b7fae7ab88b6ae24d4a6001` / `951a6f24e021b7e9cac3b88f2cb6a8369ed4ae6d4bbec80f898d678fcde1dddc` | §6: exact p(κ), q(κ) |
| `K3_factor_obstruction.zip` + `MANIFEST.sha256` | zip `046ac458e9a2a3e82a9fed14d52350f875ddb69bdf94fd4b5767a113bae585cc` | R1 confirmatory package; manifest and execution receipt now supplied |
| `k3_six_step_factor_check.py` | `7d761090378781c5c74ec64abc1f215cc951cec21f139a231ee1bd8ed18ad4ff` | Lemma S Gröbner confirmation (14/14 charts, ALL PASS); answers K3 note v0.3 §6, request 2 |

---

## 10A. Transported κ-family — Standard C, Q6 and shape `[SESSION]`

**Model-definition guard.** Let `N` be a formal primitive chart in which the isolated DYAD map commutes with the order-six linear rotation `A` and has no even-degree terms. Define the *new* network model `M_{κ,N}=P_κ ∘ N^{×3}` by imposing additive mean-feedback **again in this chart**. This is not the passive re-expression of the raw κ model. `P_κ(y)_e=y_e-(κ/3)Σ_j y_j`; it is an idempotent projection only for κ=0 or κ=1 (for κ=0 the identity).

- **Exact formal Standard C:** `S0={(z,-z,0)}` and `S±={(z,ω^{±1}z,ω^{∓1}z)}`, `ω=λ²`, satisfy `ΣN(z_e)=0`, hence the mean-feedback interaction vanishes exactly and `M_{κ,N}|_{S}=N^{×3}|_S`. These are formal invariant surfaces, not yet a physical isolation regime. `[SESSION — ALG, formal]`
- **Kiral six-step coefficients:** with `μ=-1/2-2i√3/3`, `p=μ/3`, `q=2μ/3`. In the four-dimensional centre dynamics for κ outside the singular/neutral cases, `q≠0`; Lemma S′ excludes the relevant neutral planar C³ factors under its spectral/rank premises. This supports **Q6's defined narrow sense**: no passive decoupling into edge-level planar maps; not an exclusion of all conceivable products. `[SESSION — ALG, formal, conditional]`
- **Leading shape law:** for chiral intensities `A_c=|u|²`, `B_c=|v|²`, `ΔA_c=-(1/3)A_c²-(2/3)A_cB_c+O(6)` and symmetrically for `B_c`; `Δ ln(A_c/B_c)=(A_c-B_c)/3+O((A_c+B_c)²)` away from vanishing intensities. Pure chiral surfaces are shape-attracting in this cubic approximation; `A_c=B_c` is **only a cubic-order separator**, not a proved full nonlinear invariant hypersurface. Truncated numerics are confirmatory, not a rigorous basin theorem. `[SESSION — ALG leading order / NUM]`
- **Regularity guard:** formal invariance does not establish analytic or smooth realization of `N`/its chart. `[OWNER: DYAD v6.4.13, OPEN 20]` existence remains OPEN.

## 10B. Normalizer dependence and canonical lock geometry

**Layer 1 — canonical formal geometry.** `[OWNER: DYAD v6.4.13 §6.16, DYAD-THM-FORMAL-Z6-GENERATOR]` Write `F=T⁶`, `X=log F`, `J=T exp(-X/6)`, `R0=J³`, `G=J²=T² F^{-1/3}`. These formal finite-order symmetries, and the raw-edge lock graphs defined using `R0` and `G`, do not depend on which tangent-to-identity normalizer is used. No real existence is inferred.

**Layer 2 — class-invariant cubic data.** `[SESSION — ALG, formal]` Two linear-part-normalized A-equivariant charts differ by an A-equivariant tangent-to-identity map `g`. The model is reprojected after the chart change. All such transported variants have the *same intrinsic centre six-step cubic* `p=μ/3`, `q=2μ/3`, hence the same leading chiral shape law and narrowly specified Q6 obstruction. This does **not** make the complete ambient maps identical or prove they are conjugate.

**Ambient difference at cubic order.** For `g=id+g3+O(5)` acting edgewise, `g^{×3} Pκ (g^{×3})^{-1} = Pκ + g3^{×3}Pκ - Pκ g3^{×3} + O(5)`. The difference may start in degree 3. The earlier mixed closure-mode cubic diagnostic was superseded by the κ=1 quintic test in §12A. Full ambient classification remains OPEN. `[SESSION]`

**Layer 3 — conditional realization.** `[OWNER: DYAD v6.4.13 §6.16–6.17, OPEN 20]` If an analytic identity-tangent sixth root `K` of `F` exists, then `J=TK^{-1}` is an analytic order-six symmetry commuting with `T`; Bochner averaging `Φ=(1/6)Σ_{k=0}^5 A^{-k}J^k` gives `DΦ(0)=I` and exact `ΦJ=AΦ`, so `ΦTΦ^{-1}` commutes with `A`. Reapplying `Pκ` in this chart gives a *real local transported network model*. The smooth analogue for an existing C∞ root has exact commutation and uniqueness by adopted DYAD Lemma F/F3; an extra smooth-commutation hypothesis is **not** needed. Neither analytic nor C∞ existence is established. Charts remain `ψ∘Φ` with `ψA=Aψ`; the physically admissible ψ/additive law is OPEN with OFN/RRF. Bochner constructs a model class, **not** a unique physical carrier.

**ER-2B interface.** `[SESSION: ER-2B consolidated v0.3.1 §A.4, reported SHA 711e427a…81b4]` The σ=1 endpoint of carrier interpolation shares `ν=μ, χ=0` and the quartic observable responses `Δ₄N=-N²/2+2S²`, `Δ₄S=-NS/3` with this transported model **at cubic return order only**. No full nonlinear equivalence follows. The v0.3.1 hash is reported rather than independently revalidated from a newly supplied v0.3.1 file.

## 10C. Model-selection disposition, 19 October 2026

| Option | Standard C at cubic order | Coupling / shape | Decision status |
|---|---|---|---|
| A1 raw κ=1 | EXCLUDED UNDER ASSUMPTIONS: positive-dimensional C³ invariant isolation near zero in the raw carrier | K3 owner factor obstructions; not a failure of all physically possible closure models | Excluded as **raw realization** under the OFN SESSION Standard-C requirement |
| A2 raw 0<κ<2, κ≠1 | EXCLUDED UNDER SAME ASSUMPTIONS | attracting curved closure is not isolation | Excluded as **raw realization** |
| B raw κ=0 | isolated dyad exact, no genuine edge coupling | independent edges, relative holonomy can remain nonzero | Reference model, not genuine coupled-triad candidate under OFN SESSION criteria |
| C transported κ-family | formal exact Standard C on locked surfaces | formal `p=μ/3`, `q=2μ/3`, Q6; leading-order chiral shape attraction | **Primary formal research candidate, UNRESOLVED as real physical model** |
| C alternatives (C-a…C-e) | undecided | undecided | UNRESOLVED; fallback if sixth-root existence or admissibility fails |

**Governance.** OFN response v0.7.1 is reported by the receiving stream as a non-adopted co-owner decision; admission into OFN v0.10 remains a PI decision. Do not silently treat these as v0.9 owner axioms. DYAD v6.4.13 §6.17 resolves *flat uniqueness/commutation conditional on existence*, not OPEN 20 B-an/B-6/B-infinity existence. FMS should next test the class' formal conjugacy invariants, then route physical ψ-selection to OFN/RRF; the existence theorem belongs to DYAD.


## 11. Change log

- **v0.6 (19 Oct 2026):** adds §10A–10C transported κ class, canonical J/Bochner hierarchy, OFN-reported scoped model selection, ER-2B C20 interface, and separate formal-conjugacy diagnostic. Existing v0.5.1 text remains as historical prior-state; new sections override stale OPEN/SESSION statements where owner results advanced.


- **v0.5.1 (17 Oct 2026):** review `FMS_v0_5_AND_OFN_REQUEST_REVIEW_v0_1.md` applied:
  - Lemma S′ step (ii) completed with the symmetric operator N′_α.
  - §5.1 states primitive invariance of M explicitly.
  - R3 parametrization fixed: k ∈ {0,…,5}, s ∈ ℝ.
  - `k3_six_step_factor_check.py` hash recorded.
  - New §5.3 carrier-independence proposition (R4′), with the class-C route menu C-a…C-e.
  - §8 elimination statement no longer restricted to raw edge encoding; partial autonomy addressed.
  - §9 records the formal partial-autonomy construction and the pending independent reruns.
- **v0.5 (17 Oct 2026):**
  - Theorem 6S and Lemma S′ recorded as `[THM — SESSION]`, with the invariant-kernel proof as primary and Gröbner as confirmation.
  - Spectral disjointness stated as a sufficient hypothesis.
  - Primitive d = 2: B ~ A derived. Primitive d = 1: linear exclusion recorded.
  - A1 and A2 both under the six-step obstruction; A1's six-step extension kept SESSION.
  - General-κ rows rebuilt from the exact centre-manifold computation; κ = 2 isolated.
  - Owner statuses refreshed against Genesis v2.8.6, DYAD v6.4.12 and RRF v0.8.2, and separated from SESSION results.
  - Formal exchange results separated from carrier realization.
- **v0.4 / v0.3 (16 Oct 2026, as reported):** source manifest refresh; c ∈ μ₆ lock theorem; third-edge tangent constraint; general-κ research route opened.
- **v0.2 (16 Oct 2026):** automatic complex-linearity of invariant tangents; three-edge tangency obstruction; A/B/C fork.

## 12. Preliminary formal ψ-conjugacy calculation `[SESSION — ALG, partial]`

**A nontrivial negative diagnostic for the proposed first invariant.** For the allowed radial cubic chart perturbation `g(z)=z+a z² bar(z)+O(5)`, write `z_e=u_e+h/3` with `Σu_e=0` and compare `g^{×3}Pκ(g^{×3})^{-1}` against `Pκ` at cubic order. In the mean/closure component the coefficients of both `h Σ|u_e|²` and `bar(h) Σu_e²` **cancel identically**. In fact, after the linear `A` step the mean cubic difference is pure closure:

`δh₃ = -(a λ² barλ /9) κ(κ-1)(κ-2) h² bar(h)`.

This was checked symbolically on the independent centre-line `u=(w,0,-w)`; the displayed pure-closure expression is the algebraic result for the general zero-sum centre input as well, because all mixed terms cancel in the sum. At κ outside `{0,2}`, `h²bar(h)` is nonresonant relative to the closure eigenvalue `(1-κ)λ`, so this particular cubic difference does **not** prove a formal obstruction. The κ=1 first-order-in-a *quintic* diagnostic is in §12A; its all-κ extension and κ=2 odd-category refinement are in §§12B–12C. Finite-a/nonlinear dependence remains OPEN. Evidence: `FMS_FORMAL_PSI_CUBIC_TEST_v0_1.py` (local SESSION script, run 19 Oct 2026). This note supersedes any suggestion that the mixed resonant cubic `h|u|²` coefficient necessarily varies with g.


## 12A. κ=1 quintic ψ-conjugacy test (19 October 2026)

**[SESSION — exact computational check; scope-limited]** Source: `FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py`; SHA-256 `550adcb8865246ec54f5094dd9e0f586f54bb638347164faff62309d9059e7eb`. Independently executed 19 Oct 2026: six PASS checks; exit code 0. The calculation uses exact Q(√3)(i) arithmetic.

For the reprojected **κ=1 closure-plane model** `f_a = P∘(g_a^{-1} n g_a)^{×3}`, with `g_a(z)=z+a z² z̄`, common cubic and the script's prescribed formal-conjugacy ansatz through degree five, the displayed linear system has 32 unknowns and coefficient rank 31. The augmented rank remains 31 for `a=μ` and `a=μ/6` (clock-gauge direction), but increases to 32 for `a=iμ` (obstruction). Positive/negative controls pass. The tested quintic variation is **linearized in a**, not a global classification of all ψ or finite a.

**Implication.** At this order, one real clock-flow direction is gauge and a transverse real direction is formally distinguishable under the tested conjugacy class. This provides a nontrivial mathematical selection parameter; it does **not** establish different physical models or observational distinguishability.

**Audit guard.** The script asserts/implements the allowed lower-order conjugacy ansatz (including the linear stabilizer). Before owner-grade adoption, document why excluded non-equivariant and even-degree generators cannot affect the resonant order-five quotient, and check finite-a/nonlinear effects. The all-κ infinitesimal extension is now addressed in §12B; κ=2 is parity-scoped in §12C. Finite-a effects, physical carrier existence (DYAD OPEN 20), and OFN/RRF ψ-selection remain OPEN.

**Provenance refresh.** Genesis v2.8.7 is reported adopted, including `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`, `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO`, and `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA`; DYAD v6.4.13 conditional smooth flat uniqueness/commutation is owner-closed, existence OPEN. OFN response v0.7.2 is user-reported and must be checked against its source before source-specific claims are promoted. ER-2B v0.3.1 hash `711e427a…81b4` is user-reported here, not independently recalculated from v0.3.1 bytes.

## 12B. All-κ first-order quintic ψ-obstruction — verified SESSION result (19 Oct 2026)

**[SESSION — ALG, exact; noncanonical]** The independent run of `FMS_PSI_QUINTIC_KAPPA_ALL_v0_1.py` (SHA-256 `2849e32f172243833794f754b7df37486f6ace826104777574024448b370013e`) exited `0` and reported PASS. The script imports the locally available `FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py` (κ=1). It checked the formal centre-manifold reduction at κ = 1/2, 3, 7/5, and then computed exactly, with symbolic `t=(1-κ)/κ`, a 9×9 minor after elimination of the κ-independent Φ₃ block:

`8115129463*sqrt(3)/373805638912038666240` (nonzero, independent of t).

Consequently the tested **first-order-in-a** degree-five conjugacy obstruction in the direction `a ∈ i ℝμ` persists for every real `κ ∉ {0,2}`. `κ=0` is excluded from this centre-manifold reduction; `κ=2` admits the odd-category result in §12C, while unrestricted formal conjugacy remains OPEN. The direction `a ∈ ℝμ` is the edge-local clock-centralizer/gauge direction; the result does not classify arbitrary finite `a`, disconnected stabilizer components, higher jets or physical equivalence.

**Completeness lemma (SESSION, source: `FMS_PSI_QUINTIC_MODULUS_SESSION_NOTE_v0_1.md`).** For λ-equivariant odd source and target maps with the same cubic, a tangent-to-identity formal conjugacy has zero even components at degrees two and four, an equivariant cubic generator, and degree-five non-equivariant generators that disappear under the ℤ₆ projection. The infinitesimal connected linear stabilizer is included in the tested columns. Its scope is first order in `a` and the connected stabilizer; the discrete components and finite-`a` classification remain unresolved.

**Status update:** The previous §12A and §10B statements that extension of the *infinitesimal quintic obstruction* to general κ remains OPEN are superseded **only for** `κ ∉ {0,2}` and **only at first order in a**. The search for an explicit invariant/physical readout of the modulus and the OFN/RRF choice of additive chart remain OPEN. This SECTION does not amend any adopted owner DSN.

**Provenance / release guard.** Genesis v2.8.8, DYAD v6.4.14, RRF v0.8.3 and OFN v0.7.2 were reported by a contributor but were not independently read for this update; the older owner source pins should not be silently presented as globally current. `ER-2B v0.3.1` SHA-256 `711e427a4f16069d3d3df8bf18aa582a408b1ca54c2bcb8dbd38cb0fe6ff81b4` remains contributor-reported in this session, not recalculated from the v0.3.1 bytes. Genesis reruns of `kappa_pq_symbolic.py` and `lemmaS_hand_identities.py` are reported PASS, not rerun by this script.

**19 Oct v0.6.2 change note:** Adds all-κ first-order quintic modulus verification and explicit limitation to infinitesimal formal conjugacy; does not modify historical evidence or adopted owners.

## 12C. κ = 2: parity-restricted quintic obstruction `[SESSION — ALG, partial]`

Source: `FMS_PSI_QUINTIC_MODULUS_SESSION_NOTE_v0_1_1.md`, 19 October 2026 (contributor derivation; this ledger update did not independently execute its `direct()` routine).

For the **transported odd** κ=2 model, the closure eigenvalue is `−λ = λ⁴`. Every monomial of odd total degree has an odd character, hence cannot resonate with the even character `4 mod 6`. Therefore the formal *odd* invariant closure graph is uniquely determined degree by degree. Its cubic term uses `t=(1−κ)/κ=−1/2`, and the contributor reports that the reduction satisfies the same quintic expression `f₅(1)+tE`. The previously verified nonzero 9×9 minor is independent of `t`; thus the first-order quintic obstruction for `a∈iℝμ` extends to κ=2 **among odd formal conjugacies**.

In contrast, even-degree closure-graph monomials can resonate at κ=2 (already in degree 2 and 4). No all-order uniqueness of the unrestricted invariant manifold has been shown, and an unrestricted formal conjugacy need not preserve the particular odd graph. Thus **general formal conjugacy at κ=2 remains `[OPEN]`**. The raw κ-family has a different quadratic resonance issue: its ψ₂ has a pole at κ=2, whereas the transported family has ψ₂=0. These cases must not be conflated.

**Precise grade:** `[SESSION — ALG, conditional on the reported κ=2 odd reduction]`; not an owner theorem, not a finite-a classification, and not a physical selection.

## 12D. Relative-phase harmonic readout of the quintic ψ direction `[SESSION — exact checks; limited conjugacy scope]`

**Evidence:** `FMS_PSI_QUINTIC_PHASE_INVARIANT_SESSION_NOTE_v0_1.md` and `FMS_PSI_QUINTIC_PHASE_INVARIANT_v0_1.py` (SHA-256 `1c4ab0d0d4e255d474f87b804451f6d92d128471f6268898513d6cd3fe17212f`), independently executed 19 Oct 2026 with the two prerequisite scripts present; exit 0, `ALL PASS`. The script uses exact symbolic arithmetic. Its finite parameter checks are examples, not a universal finite-conjugacy proof.

Let `u=w₁+λw₂`, `v=w₁+bar(λ)w₂`, `A=|u|²`, `B=|v|²`. Define `c(κ,a)` as the coefficient of `u³ bar(v)³` in the homogeneous degree-six part of `A∘f_a⁶−A`, where `a` is the cubic normalizer parameter and `t=(1−κ)/κ`. The candidate explicit phase-harmonic functional is

`c(κ,a) = −1/486 + 7t/648 + i[17√3/2916 + 2√3 t/81 − (2/9) Im(a bar(μ))]`.

**Exact computational results within specified scope:** (i) the real vector space of S₃- and λ-equivariant quintic perturbations has dimension 12; its intersection with the image of the tested infinitesimal conjugacy operator has dimension four, so the corresponding first-order quotient has dimension eight; (ii) the chart direction occupies one real quotient direction; (iii) the stated coefficient vanishes on all tested first-order gauge directions, including changes that alter the same-order mixed intensity coefficients; (iv) formula checks pass at `t∈{0,1,−2/3,−1/2,3/7}` for six finite `a` values, and finite S₃ cubic-conjugacy checks pass at the same `t` values. The `t=−1/2` check is **only** in the κ=2 odd-category reduction.

**Phase readout in the declared chiral representation.** With `θ=arg(u)−arg(v)`, S₃-related coefficients in `ΔB` yield

`Δ(A+B) ⊃ 4 Re(c) (AB)^(3/2) cos(3θ)`;

`Δ(A−B) ⊃ −4 Im(c) (AB)^(3/2) sin(3θ)`.

For the tested family `Re(c)` depends on κ but not `a`, while `Im(c)` is affine in `Im(a bar(μ))`. In particular `a∈ℝμ` changes neither `c` nor the canonical isolated-edge normal form; the transverse `iℝμ` direction changes the coefficient. This is a **mathematical readout** rather than a physical observable until carrier, chiral orientation and encoding are specified under RRF.

**Scope guard:** The coefficient is an infinitesimal formal-conjugacy functional in the tested S₃ class. Exact invariance under **all finite formal conjugacies**, non-S₃ transformations, arbitrary degree-five generators, and discrete stabilizer components is not established by the finite random checks. Neither finite-`a` pairwise inequivalence nor physical distinctness follows merely from those checks. κ=0 and unrestricted κ=2 remain outside the asserted full-class scope. The eight-dimensional quotient is a **first-order perturbation-space count**, not a claim that the nonlinear moduli space has dimension eight or that `c` is the unique canonical cokernel functional.

**Disposition:** This supplies the explicit algebraic candidate requested in §12B; **physical gauge-invariant readout**, finite full-conjugacy classification and owner adoption remain `[OPEN]`. Supersedes only the older statements that no candidate explicit quintic readout was available.

## 13. Revision note

- **v0.6.4 (19 Oct 2026):** corrects prior attachment ambiguity and adds §12D phase-harmonic functional, 8-dimensional first-order quotient count and exact computational checks, preserving finite-conjugacy and physical-readout limitations. No adopted DSN changed.

- **v0.6.1 (19 Oct 2026):** updates stale owner/SESSION labels, smooth-commutation status, and source notes; registers the independently rerun κ=1 quintic test with explicit limits. Historical v0.6 text is preserved where not explicitly amended.

- **v0.6.3 (19 Oct 2026):** corrects header/supersession and section order; records parity-restricted κ=2 result and separates raw versus transported κ=2 resonances. No adopted owner file changed.
- **v0.6.2 (19 Oct 2026):** exact all-κ first-order quintic obstruction for κ∉{0,2}, independently executed, with finite-a caveat.
