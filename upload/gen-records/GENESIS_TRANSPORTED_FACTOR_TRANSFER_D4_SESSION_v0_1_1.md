# GENESIS — Transported Factor Transfer (D-4) — SESSION v0.1.1

**Date:** 19 October 2026
**v0.1.1 (19 Oct 2026):** record-level correction only, per the Genesis receiving review and owner review of 19 Oct (D4 certificate 6/6 PASS independently rerun; L-JET accepted with the C³ remainder correction; T-D4 accepted for owner-scope review).
- Real C³ remainders are written as o(|z|³), or as third-jet identities, instead of O(4) (§1, §5 C2).
- No coefficient, gate, hypothesis or conclusion changes. Supersedes v0.1 (`182f4756…bacf`), which is kept unchanged.
**Work ID:** `GENESIS-WORK-TRANSPORTED-FACTOR-TRANSFER`. This is a work identifier, **not** a GEN scientific RID.
**Status:** `[SESSION]`, noncanonical.
- Opened by the Genesis owner decision of 19 Oct 2026: "D-4: OPEN FOR SCOPED INVESTIGATION".
- Adopted Genesis v2.8.8 (`9abd3616…0f37`) is unchanged.
- No v2.8.9 draft is started. No claim is offered for adoption here.

**Parent:** `GENESIS_FMS_OFN_G2_MODEL_SELECTION_SCOPE_v0_1.md` (`05255113…b3fd`), §6 D-4.

**Central question (owner wording).**

> Under which additional assumptions can the submersive-factor obstruction proved for the raw mean-feedback family be transferred to the transported dyad family?

**Short answer** (`[ALG — SESSION]`; independent review pending).

The transfer needs no assumption about the existence of J. It needs only:
- a real C³ edge map N, with DN(0) = A;
- a λ-equivariant 3-jet of N (no quadratic part);
- μ(N) ≠ 0.

The obstruction is a property of the 3-jet. DYAD OPEN 20 decides whether the exactly transported class **exists** as a real map. It does not decide its factor obstruction. One consequence: the obstruction (and so the narrow Q6) does **not** distinguish the exactly transported class from its 3-jet equivalents.

**Notation.** γ ≡ κ (SG-16). λ = e^{iπ/3}. A is multiplication by λ in the W eigenframe. 𝒞 = {Σw_e = 0}, 𝒟 = {w₁ = w₂ = w₃}. Chiral coordinates are u = w₁ + λw₂ and v = w₁ + λ̄w₂.

On the Lemma S convention: the adopted text writes the cubic as (c u|u|² − iβNu, …). The sources (and OFN) write it as (p u|u|² + q|v|²u, …). These are related by p = c − iβ and q = −iβ, so the adopted hypotheses c − iβ ≠ 0 and β ≠ 0 read **p ≠ 0 and q ≠ 0**.

---

## 1. Objects (D4-A)

| Symbol | Definition | Kind | Source / status |
|---|---|---|---|
| 𝒩₃ | real C³ germs N: (ℂ,0) → (ℂ,0) with DN(0) = A and j³N(0) commuting with A. Equivalently j³N = λz + n z²z̄. | class of real maps | defined here |
| μ(N) | the leading coefficient of N⁶ − id; for N ∈ 𝒩₃, N⁶(z) = z + μ(N) z²z̄ + o(\|z\|³), i.e. j³(N⁶)(z) = z + μ(N) z²z̄, with **μ(N) = 6λ̄n**. (C³ regularity alone does not give an O(\|z\|⁴) remainder; the polynomial and formal computations of §4 are exact at the jet level.) | invariant | §4, G3 |
| G^N_γ | (G^N_γ w)_e = N(w_e) − (γ/3) Σ_j N(w_j) on ℝ⁶ ≅ ℂ³ | real C³ network map | same shape as `GEN-DEF-MEANFEEDBACK-FAMILY`, with T replaced by N |
| F^N_κ | the same formula with N the formal λ-equivariant normal form | **formal** series | OFN v0.7.2 §3.3 `[ALG — formal]` |
| 𝓕_{γ,Φ} | (Φ⁻¹)^{×3} ∘ G^{N_Φ}_γ ∘ Φ^{×3}, with Φ = (1/6) Σ_k A^{−k}J^k and N_Φ = ΦTΦ⁻¹ | real map, **conditional on J** | OFN v0.7.2 §3.5(d) `[THM — conditional on J]` (OFN SESSION) |
| G^{N₃}_γ | G^N_γ with N₃(z) = λz + n_T z²z̄, where n_T is the Birkhoff cubic of T | real polynomial map, **unconditional** | jet surrogate (§5, C1) |

**Carrier.** Everything sits in the raw W eigenframe of Genesis §6.3a. G^N_γ is written in the chart where the edge map is N. 𝓕_{γ,Φ} is the same law pulled back to raw coordinates by Φ^{×3}.

**Formal vs real (owner boundary, §4 of the decision).**
- No statement in this record derives the absence of real C³ factors from a formal conjugacy.
- The only formal ingredient used is the uniqueness of Taylor coefficients of a centre manifold up to order 3. That is a property of every *real* C³ centre manifold.
- The formal series F^N_κ is not a real map. §5 makes no real statement about it.

---

## 2. Source / assumption matrix — the six links of the owner decision

| # | Link | Raw F_γ (Genesis adopted) | Transported G^N_γ (this record) | Status here |
|---|---|---|---|---|
| 1 | Exact map and carrier | `GEN-DEF-MEANFEEDBACK-FAMILY`, W frame | §1: G^N_γ, N ∈ 𝒩₃; 𝓕_{γ,Φ} by C³ conjugacy | **closed** (definition) |
| 2 | Linear spectrum; centre/normal split | λ on 𝒞, (1−γ)λ on 𝒟 | identical: DN(0) = A and P_γ linear. Checked in G3 (DG⁶ = I on 𝒞). | **closed** |
| 3 | Centre manifold: existence, tangency, regularity | §6.3b `[ALG]`: C³, tangent to 𝒞 for γ∉{0,2} | identical theorem input (G is C³, \|1−γ\| ≠ 1). Jets: ψ₂ ≡ 0, ψ₃ computed, invariance through degree 3 (G3). | **closed** for real C³ G |
| 4 | Six-step chiral cubic | §6.3b, `kappa_pq_symbolic.py` | **p = 2λ̄n = μ/3 and q = 4λ̄n = 2μ/3, identically in γ and n.** Both chiral components; no other monomials. | **closed** (D4-B, own computation from the full ℝ⁶ map) |
| 5 | Reduction of the factor to the centre via the target-spectrum condition | §6.3b proof (a)–(b), (H_spec); primitive (i)–(iii), (H_prim) | uses only link 2 and link 3 | **closed** by the audit in §3 |
| 6 | Lemma S | `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` | p ≠ 0 and q ≠ 0 ⟺ μ(N) ≠ 0. For the DYAD value, μ₆ = −1/2 − (2/3)i√3 ≠ 0. | **closed** |

---

## 3. Jet-dependence audit of the adopted proof `[ALG — SESSION]`

This section audits the adopted proofs of §6.3a.1 and §6.3b of v2.8.8, step by step. The question for each step: **which data of the map does it use?**

| Proof step (v2.8.8) | Data of the map used |
|---|---|
| §6.3b (a): 𝒟 ⊆ ker ℓ under (H_spec) | DF(0) and its 𝒞/𝒟 eigenspaces |
| §6.3b (b): reduction to M^c | existence of a C³ centre manifold tangent to 𝒞 (needs the map C³ and \|1−γ\| ≠ 1) |
| §6.3a.1 (a): DT′ = I | DF⁶(0)\|_𝒞 = I |
| §6.3a.1 (b): no quadratic term | leading-term lemma §6.3a(b): needs only D(F\|M^c)(0) = rotation of order 6 |
| §6.3a.1 (c): ℓ∘f₃ = t₃∘ℓ | the cubic of F⁶\|M^c, i.e. **j³ of F and of M^c** |
| §6.3a.1 (d): Lemma S | the coefficients (p, q) of that cubic |
| Primitive (i)–(iii) | DF(0) spectra, then the same chain |
| Coefficients of M^c up to order 3 | unique, because the homological denominators λ^m − (1−γ)λ, degrees 2 and 3, are nonzero for γ ∉ {0,2}. Every C³ centre manifold has the same 3-jet. |

**L-JET (`[ALG — SESSION]`, proposed; not adopted).** The adopted proofs of `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` and of the primitive-clock statement use only three things:
1. that the map is a real C³ germ on ℝ⁶;
2. the linear data (multiplication by λ on 𝒞, by (1−γ)λ on 𝒟, with γ ∈ ℝ∖{0,2});
3. the six-step centre cubic, which is determined by the 3-jet of the map.

They therefore hold for every real C³ germ with these linear data whose six-step centre cubic has the Lemma S form with p ≠ 0 and q ≠ 0. The family theorem keeps (H_spec); the primitive statement keeps (H_prim).

**Conjugacy step.** Suppose G′ = Ψ⁻¹GΨ with Ψ a C³ diffeomorphism fixing 0. Then E is a factor of G′ if and only if E∘Ψ⁻¹ is a factor of G, with the same T′. Hence (H_spec) and (H_prim) are unchanged.

**Review flag.** L-JET restates which inputs the adopted proof uses. It does not change that proof. It is still a new SESSION statement and needs the independent review requested in §8.

---

## 4. D4-B: cubic-transfer certificate

**Script:** `d4_transported_cubic_cert.py` (`f4c382855b130249ce290d3ca939b283aadd27d6ea9a1af551599f4cd9533f6d`).
**Output:** `d4_transported_cubic_cert_output.txt` (`0e8053ae21f93844304605716bd58a79c1d210f94b60b8fe7274209622a70df7`). **6/6 PASS**, exit 0, about 30 s.
**Arithmetic:** exact, in the field ℚ(γ, a, b)(i√3), with n = a + i√3·b generic.

**Pipeline.** The certificate does not use OFN's coefficient transfer. It builds everything from the full six-dimensional map:
1. the ℝ⁶ network map;
2. its own invariant graph s = ψ(x) through degree 3;
3. the reduced map on 𝒞;
4. the six-fold composition;
5. both chiral components.

The pipeline code matches the adopted load-bearing script `kappa_pq_symbolic.py`, generalized to an arbitrary edge map.

| Gate | Content | Result |
|---|---|---|
| G1 | j³(T⁶) of the primitive itself has no quadratic part; its only cubic monomial is z²z̄, with **μ₆ = −1/2 − (2/3)i√3** | PASS |
| G2 | Own Birkhoff chart (degree-2 removal) gives n_T = 1/8 − (7/72)i√3, and **6λ̄n_T = μ₆** | PASS |
| G3 | N₃ = λz + n z²z̄ with γ and n indeterminate: ψ₂ ≡ 0; invariance through degree 3; six-step linear part I; no quadratic part; u-form and v-form exact; **p = 2λ̄n, q = 4λ̄n identically in γ** | PASS |
| G4 | Calibration: the same pipeline with N := T (raw, with quadratic part) reproduces the adopted Genesis p(γ), q(γ) of §6.3b identically | PASS |
| G5 | At the DYAD value: p = μ₆/3 = −1/6 − (2/9)i√3, q = 2μ₆/3 = −1/3 − (4/9)i√3. Hence c − iβ = p ≠ 0 and β = iq ≠ 0. | PASS |
| G6 | n = 0 gives p = q = 0 (Lemma S branch excluded; sharpness); a wrong claim p = μ/6 is rejected | PASS |

**Agreement with OFN.** The certificate agrees with OFN v0.7.2 §3.4 (p = μ/3, q = 2μ/3, independent of κ). The agreement is now established from the full network map, not from the reduced-cubic transfer.

**Additional negative controls** (scratch runs; the gate script itself is unchanged):
- Adding a z z̄ quadratic term to N: G3 fails (ψ₂ ≠ 0, and p, q change).
- Adding a z² term: G3 fails on ψ₂ ≠ 0. In this particular case p and q happen to be unchanged.

So the λ-equivariance of the 3-jet is checked directly, not inferred from the values of p and q.

**Not cross-checked here:** the value n_T against the printed DYAD normal-form table. Only the invariant μ₆ is compared. It agrees with the Genesis §6.3a "dyad cross-check μ_num = μ₆" record and with the ER-2B study value.

---

## 5. D4-C: conditional statement and corollaries

**T-D4** (`[ALG — SESSION]`; a proposed theorem, **not adopted, not offered for adoption in this record**).

Let N ∈ 𝒩₃ with μ(N) ≠ 0, and let γ ∈ ℝ∖{0,2}. Let E be a C³ submersion from a neighbourhood of 0 ∈ ℝ⁶ onto a manifold of dimension d ∈ {1,2,3}, and let T′ be C³.
- **(i) Six-step clock.** E∘(G^N_γ)⁶ = T′∘E is impossible under (H_spec): (1−γ)⁶ ∉ spec DT′(E(0)).
- **(ii) Primitive clock.** E∘G^N_γ = T′∘E is impossible under (H_prim): (1−γ)λ ∉ spec DT′(E(0)).
- **(iii) Conjugates.** (i) and (ii) hold for every germ that is C³-conjugate to G^N_γ by a diffeomorphism fixing 0.

*Proof.* By L-JET (§3), it suffices to check links 2–4 of §2 for G^N_γ.
- Link 2 holds by DN(0) = A.
- Link 3 holds because G^N_γ is C³ and |1−γ| ≠ 1.
- Link 4 is G3: p = μ(N)/3 and q = 2μ(N)/3, both nonzero.
- (iii) is the conjugacy step of §3. ∎

**C1 — jet surrogate (unconditional).** Take N₃ = λz + n_T z²z̄. Then G^{N₃}_γ is a real polynomial map, and T-D4 applies to it. This needs no DYAD OPEN 20 input.

**C2 — real transported class (conditional on J).** Suppose J is realized with JT = TJ, J⁶ = I, DJ(0) = A, and of class at least C³. Then:
- the Bochner chart Φ is C³ with DΦ(0) = I (OFN §3.5(d));
- N_Φ = ΦTΦ⁻¹ commutes with A exactly, so N_Φ ∈ 𝒩₃;
- μ(N_Φ) = μ₆. Here N_Φ⁶ = ΦT⁶Φ⁻¹ with T⁶(z) = z + f₃(z) + o(|z|³), f₃ = μ₆ z²z̄. For a local C³ diffeomorphism Φ with Φ(0) = 0 and DΦ(0) = I, Φ∘T⁶∘Φ⁻¹(z) = z + f₃(z) + o(|z|³), so the leading cubic is unchanged (G2 confirms the value). This does not prove that J exists; it only shows the coefficient is preserved when a suitable real J and Bochner chart exist.

Hence 𝓕_{γ,Φ} satisfies T-D4(i)–(iii) for every admissible Φ and every γ ∉ {0,2}. In particular, the Q6 argument of OFN §3.1 (product decomposition, primitive clock, (H_prim) with unit-circle targets) goes through for the transported class.

**C3 — scope of the Q6 certificate** (`[ALG]`, with a `[HEUR]` reading).
- T-D4 depends only on j³N. So every real C³ model sharing the 3-jet of the transported law has the same obstruction. This includes models that are **not** exactly transported, such as the surrogate in C1.
- *Reading:* narrow Q6 is satisfied by the class C candidate but does not single it out. What separates class C from its jet-equivalents is OFN's exact Standard C on the lock surfaces. That is an all-order property, not a 3-jet property. This reading concerns model selection, which is not a Genesis decision.

**C4 — OPEN 20 dependence.** If no real J exists, the exactly transported class is empty and C2 is vacuous. C1 and C3 do not change. **The Q6 entry is therefore not what depends on OPEN 20; the existence of the class is.**

---

## 6. D4-D: realization interface

| Assumption | Needed for the obstruction (T-D4)? | Needed for the class itself (OFN §3.5)? |
|---|---|---|
| J exists (analytic or C^∞; OPEN 20 B-an / B-6 / B-∞) | **no** (C1); only so that C2 is non-vacuous | yes |
| Regularity of J or Φ | **C³ suffices** | OFN requires analytic or C^∞ |
| Exact JT = TJ, so N_Φ commutes with A at all orders | no; only j³N_Φ λ-equivariant is used | yes (exact Standard C on 𝒮₀, 𝒮_±) |
| Φ tangent to identity | used for μ(N_Φ) = μ₆ | given by Bochner averaging |
| Locality: a common neighbourhood of 0 for J, Φ and the centre manifold | yes, a local germ statement only | yes |

---

## 7. What is not closed

1. **Review.** L-JET and T-D4 are SESSION results. They need independent receiving review (§8). Owner adoption would require a separate decision and a v2.8.9 cycle; neither is started.
2. **γ ∈ {0, 2}.**
   - *Observation for D-1* `[ALG]`: for the transported family the degree-2 homological denominators are never used, because ψ₂ ≡ 0.
   - At γ = 2 the degree-3 denominators λ^m + λ (m ∈ {±1, ±3}) are also nonzero. So the *formal* quadratic resonance of the raw family is absent here.
   - What still blocks γ = 2 is the neutral 𝒟 mode (|1−γ| = 1). Then there is no centre/hyperbolic splitting, and (H_spec) fails for unit-circle targets. γ = 2 stays OPEN.
3. **Inherited OPENs of SG-16.** These are not changed: C¹/C² planar factors; targets meeting the 𝒟 spectrum (D-3); non-submersive or non-local factors; Q6 beyond "no passive decoupling into planar edge maps".
4. **The formal object F^N_κ.** No real statement is made about it. A formal-factor analogue follows by the same steps (the formal invariant graph exists for γ ∉ {0,2}), but it is not recorded as a result.
5. **The DYAD table value of n₂₁** is not text-compared (§4).
6. **Source authority.** OFN v0.7.2 was read from the project copy. The owner's 19 Oct review notes that its authority was not independently verified in the owner session. Nothing here depends on an OFN verdict; only OFN's *definitions* of F^N_κ and 𝓕_{κ,Φ} (§3.3, §3.5(d)) are used.

---

## 8. Requests and notices (no action taken)

**To the independent reviewer (Genesis receiving review)**
1. Check L-JET against the v2.8.8 proof text of §6.3a.1 and §6.3b. In particular: does any step use data beyond C³ regularity, the linear data and j³?
2. Rerun `d4_transported_cubic_cert.py` (expected 6/6, exit 0).
3. Check the conjugacy-invariance argument for μ(N_Φ) = μ₆ in C2.

**To OFN** (informational, after review only)
- The Q6 entry of OFN §3.4 could then cite `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` plus this SESSION transfer, instead of "apply verbatim".
- Per C4, Q6 for the transported class does not wait on OPEN 20.
- Per C3, Q6 does not discriminate class C from its 3-jet equivalents.

**Genesis decisions remaining with the owner**
- Whether, after review, D-4 should go to an owner draft. This record does not request it.

---

## 9. Evidence

| File | SHA-256 | Role |
|---|---|---|
| `d4_transported_cubic_cert.py` | `f4c382855b130249ce290d3ca939b283aadd27d6ea9a1af551599f4cd9533f6d` | D4-B certificate, G1–G6 |
| `d4_transported_cubic_cert_output.txt` | `0e8053ae21f93844304605716bd58a79c1d210f94b60b8fe7274209622a70df7` | 6/6 PASS |
| `kappa_pq_symbolic.py` (adopted evidence) | `091a42105cff7965127c55a4a5adffa281021cd71957ed789409de320c5d42b2` | pipeline template; G4 reproduces its identities |
| Genesis v2.8.8 | `9abd36169a4bf6056318605c0399ff1f91c53f157b9181bdbfdb9faed3000f37` | §6.3a.1, §6.3b proof text audited in §3 |
| Scope note v0.1 | `0525511321599f166f6f6adf5d63c235b8632198f3d765be8bf3a2fcbdd7b3fd` | parent |
