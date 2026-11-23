# FMS MODEL SELECTION LEDGER v0.5 — SESSION

**Date:** 2026-10-17
**Profile:** Foundations & Model Selection (FMS) working ledger — noncanonical
**Owner:** FMS (proposed). Scientific theorems remain with their owners (DYAD, Genesis, RRF, OFN, NUMGEN).
**Lifecycle:** `[SESSION]` — NOT owner adopted. No adopted DSN is modified by this file.
**Supersedes:** FMS Ledger v0.4 SESSION (not overwritten; v0.5 is a new file).
**Vocabulary:** `SUFFICIENT`, `NECESSARY`, `EXCLUDED UNDER ASSUMPTIONS`, `UNRESOLVED` are model-assessment verdicts under explicitly stated premises. They are not adoption or task statuses.

> **Reading rule.** Every row says *which source grade* supports it. An owner-adopted theorem is marked `[OWNER]` with its RID. A result proved in session but not adopted is marked `[SESSION]`. A SESSION result is never cited as an owner result.

---

## 0. Source manifest

| Source | Version used | Grade | Used for |
|---|---|---|---|
| `RTG_GENESIS_GEOMETRY_DSN` | v2.8.6 (adopted 16 Oct 2026) | `[OWNER]` | `GEN-THM-K3-PLANAR-FACTOR-NOGO` (§6.3a) |
| `RTG_DYADIC_OSCILLATOR_DSN` | v6.4.12 (adopted 16 Oct 2026); v6.4.12.1 metadata release present | `[OWNER]` | `DYAD-ALG-CENT-KERNEL`, `DYAD-THM-FORMAL-CENTRALIZER`, `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`, `DYAD-THM-ANALYTIC-CLOCK-BRIDGE`, `DYAD-THM-LOCAL-INVOLUTION-GERM`; OPEN 20 `DYAD-OPEN-INVOLUTION-REALIZATION` |
| `RTG_RRF_REPRESENTATION_REGISTRY` | v0.8.2 (adopted working standard, 17 Oct 2026) | `[OWNER — RRF working standard]` | G2 contract, clock/regularity declarations |
| `RTG_ONTOLOGICAL_FOUNDATIONS` | v0.9 | `[OWNER]` | identity/exchange framing; physical decisions remain OFN's |
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
| R3 | Full formal centralizer of T: Cent_formal(T) = {T^k exp(sX) : k ∈ ℤ₆, s ∈ ℝ}; linear multipliers restricted to μ₆ because a₀₅ ≠ 0 | `[SESSION — ALG]` | formal (§5.2) |
| R4 | Tangent classification of invariant closures for independent edges | `[SESSION — ALG]` | §5 |
| R5 | General-κ centre manifold ψ₂ and exact reduced chiral coefficients p(κ), q(κ) | `[SESSION — ALG]` | §6 |
| R6 | Lemma S′: real-linear cubic factor obstruction for p ≠ 0, q ≠ 0 | `[SESSION — ALG]` | §7.2 |
| R7 | Theorem 6S: no neutral low-dimensional factor, primitive or six-step clock, for κ ∈ ℝ∖{0,2} | `[THM — SESSION]`; Genesis owner adoption pending | §7 |
| R8 | κ=0 relative holonomy limit `|h_m|/√N_m → L ≥ 0`, with `|h_m| → 0` | conditional local theorem (NUMGEN/DYAD provenance) | isolated-edge tube initializations |

---

## 3. Base model assessment

Primitive law; columns refer to §1. "Excluded" always means `EXCLUDED UNDER ASSUMPTIONS` for the named condition.

| Model class | C | C′ | A (primitive) | A6 (six-step, neutral target) | H | Support |
|---|---|---|---|---|---|---|
| **κ = 0** — independent edges | no (generic) | **no**: no invariant C³ closure tangent to any three-edge plane (§5) | **yes** (raw `E_e = r_e`) | yes | `|h|→0`, `|h|/√N → L ≥ 0`; L may vanish | R4, R8 |
| **κ = 1** — projected K3 | **yes** in raw additive carrier | trivially (ψ ≡ 0) | **no**: C³, d=2; C¹, d=1,3 | **no** (SESSION) | h = 0 by construction | R1 `[OWNER]`; six-step extension R7 `[SESSION]` |
| **0 < κ < 2, κ ≠ 1** | no | **yes**: attracting C^r centre manifold `h = ψ(u) = O(|u|²)`, attraction transverse only | **no** for neutral targets (SESSION) | **no** (SESSION) | h slaved to u; not free | R5, R7 |
| **κ < 0 or κ > 2** | no | invariant manifold exists but is normally repelling | **no** for neutral targets (SESSION) | **no** (SESSION) | not certified | R5, R7 |
| **κ = 2** | no | quadratic resonance: ψ₂ has a pole | `UNRESOLVED` | `UNRESOLVED` | — | OPEN |
| **Outside the κ family** | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | — |

**Scope of the no-factor rows.** They exclude local C³ submersive factors whose target linearization has spectrum disjoint from the closure-mode spectrum (unit-circle target spectrum suffices). They do not exclude C¹/C² rank-2 factors, factors onto the closure mode itself (e.g. `E_h = Σ r_e` at κ = 1, target = zero map), non-submersive encodings, or other network dynamics.

---

## 4. Carrier / clock / regularity overlay

| Item | Primitive clock T | Six-step clock T⁶ | Grade |
|---|---|---|---|
| Formal exchange jet | unique, = Ŝ (G1 square-root argument; covered by `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`) | unique, = Ŝ (`DYAD-THM-FORMAL-CENTRALIZER`) | `[OWNER]` formal |
| Analytic involution commuting with T⁶, DR(0) = −I | — | commutes exactly with T | `[OWNER]` `DYAD-THM-ANALYTIC-CLOCK-BRIDGE` |
| C^∞ involution commuting with T⁶ | — | only j^∞(RT−TR) = 0; exact commutation needs flat uniqueness | `[OPEN]` (OPEN 20) |
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
| C^∞ | formal j^∞R = Ŝ if a true involution exists | realization; flat uniqueness |
| analytic | formal j^∞R = Ŝ; exact T-commutation from T⁶-commutation | existence |

---

## 5. Invariant closures for independent edges (κ = 0) `[SESSION — ALG]`

### 5.1 Three-edge tangency obstruction (C³)

On three independent edges, `D⁶(w) = w + μ(w_e|w_e|²)_e + O(|w|⁴)`. This cubic is unchanged by tangent-to-identity coordinate changes, because D⁶ has no quadratic part.

Let M be a local C³ invariant manifold through 0 of real codimension 2. Its tangent P is invariant under A⊕A⊕A. Every such real subspace is complex for J = (A − cos(π/3) I)/sin(π/3). Hence P = {Σ a_e w_e = 0} is a complex hyperplane. No separate complex-linearity hypothesis is needed. Odd real codimensions cannot occur.

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

**Result.** The tangent of every C⁵ invariant codimension-2 manifold is w_k = 0 or w_i = λ^m w_j (m ∈ ℤ₆). Two-edge formal locks are exactly the graphs w_i = T^k exp(sX)(w_j). The special cases are coincidence (k = 0, s = 0) and the Ŝ-lock (k = 3, s = −1/2).

**OPEN.** Whether a lock-tangent manifold that depends on the third edge at higher order must itself be a centralizer graph.

**Remark on a₀₅.** DYAD v6.4.12 states that a₀₅ plays no role in OPEN 19. That is correct for the tangent-to-identity centralizer. For the full centralizer of T, a₀₅ is what restricts the linear multipliers to μ₆. The two statements are consistent.

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
   - (ii) N_α = Df(e^{iα}, 0) − Df(1, 0) acts as (δu, δv) ↦ (p(e^{2iα}−1) δū, 0). The real span of {e^{2iα}−1} is ℂ. Using p ≠ 0, K ∈ {0, ℂ_u, ℂ_v, ℂ²}, which excludes d = 1, 3.
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
| **A1** — exact closure | κ = 1 | C holds; no neutral low-dimensional primitive factor | `[OWNER]` R1; six-step extension `[SESSION]` R7 |
| **A2** — dynamically selected closure | 0 < κ < 2, κ ≠ 1 | C′ holds (transversally attracting curved closure); no neutral low-dimensional factor under either clock; chiral intensities coupled (Re q ≠ 0) | `[SESSION]` R5, R7 |
| **B** — primitive autonomy | κ = 0 | A holds; C fails; no invariant C³ curved three-edge closure; relative holonomy L ≥ 0 | `[SESSION]` R4; R8 conditional |
| **C** — alternative realization | outside the tested class | outside every no-go above; candidate routes include closure through extra (connection/holonomy) variables, closures below C³, a changed meaning of autonomy or encoding, or other couplings. Not an exhaustive list. | `UNRESOLVED` |

**Elimination statement, scoped.** Within the κ family, raw edge encoding and declared regularity:

- no model satisfies both closure (C or C′) and neutral edge autonomy (A or A6);
- changing the clock from primitive to six-step does not recover autonomy.

This excludes these scoped models only. It is not a theorem about all RTG realizations.

**No verdict here.** FMS does not pre-assign `SUFFICIENT`/`NECESSARY` to A1, A2, B or C. These verdicts follow only after OFN states which physical requirements it counts as `NECESSARY` (see the companion OFN decision request).

---

## 9. Open items

| Item | Owner | State |
|---|---|---|
| Theorem 6S, Lemma S′, exact p(κ), q(κ), ψ₂ | Genesis | owner review pending |
| RRF import | RRF | `GEN-THM-K3-PLANAR-FACTOR-NOGO` importable now (v0.8.3); Theorem 6S only after Genesis adoption |
| Analytic / C^∞ odd carrier | DYAD | OPEN 20 |
| C¹/C² rank-2 factors | Genesis | OPEN |
| Factors onto the closure mode (target spectrum meeting it) | Genesis | OPEN; not G2-relevant |
| κ = 2 resonance | Genesis | OPEN |
| Third-edge-dependent lock manifolds | FMS / Genesis | OPEN (tangent classified) |
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
| `k3_six_step_factor_check.py` | not recorded here | Lemma S Gröbner confirmation (reported ALL PASS) |

---

## 11. Change log

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
