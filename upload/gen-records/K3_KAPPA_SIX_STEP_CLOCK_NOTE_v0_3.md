# K3 / κ-family: six-step-clock factor obstruction — proof record v0.3

**Date:** 17 October 2026 · **Status:** `[SESSION]` noncanonical proof record. No owner file, RID or OPEN status is changed. Ownership of any adopted result would be Genesis (K3 theorem lineage, §6.3a).
**Supersedes:** note v0.2 (`13f8c679…605f`).
**Answers:** Genesis-side disposition of 17 Oct (`8e3f465e…19bc`). That disposition asked for the following before any v2.8.7 owner draft:
- (i) the spectral hypothesis, written precisely;
- (ii) a parameter-general proof of Lemma S;
- (iii) a source manifest.

**Changes from v0.2:**
1. **p(κ), q(κ).** These are now verified as identities in ℚ(κ)(i√3), with κ an indeterminate (`kappa_pq_symbolic.py`). The all-κ statement no longer rests on point evaluations or interpolation (§1.3).
2. **Lemma S.** It now has a hand proof for every p ≠ 0, covering all ranks (§2.2). The Gröbner script is needed only for the p = 0 branch, which the κ-family never reaches.
3. **Theorem 6S is split into two layers (§3).**
   - **6S-core** (κ = 1, on the carrier 𝒞): needs **no** hypothesis on T′ beyond C³. The v0.2 sentence "no hypothesis is made on T′" is correct for this layer, and only for it.
   - **6S-κ** (on ℝ⁶): the closure-mode kernel condition is no longer an assumption. It is derived from a spectral-separation hypothesis (H_spec). Some hypothesis is necessary on ℝ⁶ (§3.3).
4. **Regularity is stated per layer and per clock (§4).**
5. **The source manifest is in §6.**

---

## 1. Model and exact source data

### 1.1 `[DEF]` κ-family

Let T be the primitive dyad map (`GEN-DEF-PRIMITIVE-MAP` ≡ `DYAD-DEF-PRIMITIVE-MAP`), written in the complex chart w ∈ ℂ, with DT(0) = λ = e^{iπ/3}. For κ ∈ ℝ define F_κ on ℝ⁶ ≅ ℂ³ by

  w_e′ = T(w_e) − κ · (1/3) Σ_{e′} T(w_{e′}),  e = 1, 2, 3.

- **Closure coordinate.** s = Σ_e w_e. Then s′ = (1−κ) Σ_e T(w_e).
- **Closure plane.** Σ = {w₁ = w₂ = w₃} (real dimension 2) is the closure mode. DF_κ(0) acts on Σ by multiplication by (1−κ)λ (real pair (1−κ)λ, (1−κ)λ̄), and on 𝒞 by λ.
- **Carrier.** 𝒞 = {s = 0} carries the dynamics P_𝒞 T^{×3}, which is independent of κ.
- **κ = 1.** F₁ maps ℝ⁶ into 𝒞. Its restriction to 𝒞 is exactly the Genesis v2.8.6 §6.3a model F₁ = P_𝒞 T^{×3}.

### 1.2 `[ALG]` Centre manifold

For κ ∈ ℝ ∖ {0, 2}, the closure eigenvalues satisfy |(1−κ)λ| = |1−κ| ≠ 1. So there is a local C³ centre manifold W^c_κ = {s = ψ_κ(u)}, tangent to 𝒞, where u = (w₁, w₂) are the carrier coordinates.

- **ψ is solved term by term** from ψ(Λu + …) = (1−κ) Σ_e T(w_e). The degree-k coefficient of the monomial with chiral weight m has the denominator λ^m − (1−κ)λ.
- **Where the denominators vanish.** Over real κ, these denominators vanish only at:
  - κ = 2 (degree 2, m = 4: λ⁴ = −λ);
  - κ = 0 (degree 3, m = 1).
- **Script confirmation.** `kappa_pq_symbolic.py` prints the denominators. Their real-κ zeros are exactly {0, 2}; the other factors are κ² − κ + 1 > 0 and κ⁴ − 4κ³ + 7κ² − 6κ + 3 = (κ² − 2κ)² + 3(κ − 1)² > 0.
- **The reduced map is P∘T^{×3}(u + ψ/3).**
  - κ enters only through ψ.
  - ψ₃ enters the cubic only through the linear part DT(0)ψ₃/3, which is the same on every edge, so P kills it.
  - So the cubic depends on ψ₂ only.

### 1.3 `[ALG]` Six-step cubic

In chiral coordinates u = w₁ + λw₂ and v = w₁ + λ̄w₂ (a real-linear isomorphism ℂ² → ℂ²), the six-step map F_κ⁶|W^c has:
- linear part I;
- no quadratic part;
- cubic part

  f_κ(u, v) = ( u(p|u|² + q|v|²), v(p|v|² + q|u|²) ),

with

  p(κ) = −(κ² − 3κ + 1) / (6(κ² − κ + 1)) − i (√3/9)(2κ² − 3κ + 2) / (κ² − κ + 1),
  q(κ) = −(2/3)(κ − 1)³ / ((κ − 2)(κ² − κ + 1)) − i (2√3/9)(2κ² − 3κ + 2) / (κ² − κ + 1).

**Sources (three independent routes):**

| Route | What it establishes |
|---|---|
| `exact_q.py` (ChatGPT; rerun by the PI, identical output) | q at 7 κ-points, plus the degree bound deg(q·D) ≤ 3, D = (κ−2)(κ²−κ+1) |
| `kappa_pq_independent.py` (Claude) | own ψ₂ **and** ψ₃ from the 6-dim map; both chiral components; p and q exact at κ ∈ {1/2, −1, 7, 3/2, 1} |
| `kappa_pq_symbolic.py` (Claude, new) | same construction with κ an indeterminate. Invariance through degree 3, the u-form, the v-form, and both closed forms hold **as identities in ℚ(κ)(i√3)**. Specializing to any real κ ∉ {0, 2} is legitimate because no denominator vanishes there (§1.2) |

**Checks at κ = 1:**
- p(1) = 1/6 − i√3/9 = c₀ − iβ*;
- q(1) = −i·2√3/9 = −iβ*.

These agree with Genesis v2.8.6 §6.3a.

**`[ALG]` Non-vanishing.** For every real κ ≠ 2:
- Im p ≠ 0 and Im q ≠ 0, since 2κ² − 3κ + 2 has discriminant −7 and κ² − κ + 1 > 0;
- hence p(κ) ≠ 0 and q(κ) ≠ 0.

---

## 2. Lemma S

**Lemma S.** Let f(u, v) = (u(p|u|² + q|v|²), v(p|v|² + q|u|²)) on ℂ² ≅ ℝ⁴, with p, q ∈ ℂ. Suppose ℓ: ℝ⁴ → ℝ^d is a real-linear surjection with 1 ≤ d ≤ 3, and ℓ∘f = t∘ℓ for some C¹ map t. Then:
- d = 2 ⇒ q = 0;
- d ∈ {1, 3} ⇒ p = q = 0.

### 2.1 Reduction to invariant subspaces

Differentiate ℓ∘f = t∘ℓ to get ℓ·Df(x) = Dt(ℓx)·ℓ for every x. Hence **K = ker ℓ is invariant under Df(x) for every x ∈ ℝ⁴**. K is proper and nonzero, of real dimension 4 − d.

### 2.2 `[THM]` Hand proof for p ≠ 0

Write P_α for the orthogonal projection of ℂ ≅ ℝ² onto ℝe^{iα}, and A(α) = P_α − P₀. Let ℂ_u = ℂ ⊕ 0 and ℂ_v = 0 ⊕ ℂ.

**(a) Jacobian on the u-axis.**

  Df(e^{iα}, 0) = diag( p(I + 2P_α), q ).

So D_α − D₀ := Df(e^{iα}, 0) − Df(1, 0) = diag( 2p·A(α), 0 ).

**(b) K ∩ ℂ_u = 0 ⇒ K ⊆ ℂ_v.**
- D_α − D₀ maps K into K ∩ ℂ_u, through k ↦ 2p A(α) π_u(k).
- For α ∉ πℤ, A(α) is invertible (det A(α) = −sin²α). Multiplication by p ≠ 0 is also invertible.
- So K ∩ ℂ_u = 0 forces π_u(K) = 0, i.e. K ⊆ ℂ_v.
- By the u ↔ v symmetry of f, K ∩ ℂ_v = 0 ⇒ K ⊆ ℂ_u.

**(c) K ∩ ℂ_u is 0 or ℂ_u.**
- Suppose L = K ∩ ℂ_u is a real line. Each 2pA(α) (α ∉ πℤ) maps L into K ∩ ℂ_u = L and is invertible, so it fixes L.
- Then L is also invariant under (2pA(π/2))⁻¹(2pA(π/6)) = A(π/2)⁻¹A(π/6). Here p cancels, because the complex scalar commutes with itself.
- But A(π/2)⁻¹A(π/6) = ½·Rot(π/3), which has no real eigenline. Contradiction.
- The same holds for ℂ_v.

**(d) Case analysis.** By (b) and (c):

| (K∩ℂ_u, K∩ℂ_v) | K | Outcome |
|---|---|---|
| (0, 0) | ⊆ ℂ_u ∩ ℂ_v = 0 | excluded (K ≠ 0) |
| (ℂ_u, ℂ_v) | ℝ⁴ | excluded (K proper) |
| (ℂ_u, 0) | ℂ_u ⊕ 0 (by (b)) | v-block of Df(1,1)·(h, 0) is 2q·Re(h); invariance forces q = 0 |
| (0, ℂ_v) | 0 ⊕ ℂ_v | u-block of Df(1,1)·(0, h) is 2q·Re(h); invariance forces q = 0 |

**Hence, for p ≠ 0:**
- d ∈ {1, 3} is impossible, since dim K would be 3 or 1, but the only candidate kernels have dimension 2;
- d = 2 requires q = 0.

This is Lemma S on the branch p ≠ 0. The bound is sharp: if q = 0 then ℓ = π_u is a factor, with t(u) = pu|u|². ∎

**Audit.** `lemmaS_hand_identities.py` checks every matrix identity used above (I1–I5) symbolically in p = a + ib and q = c + id: 5/5 PASS. It audits the computations; the proof is the text above.

### 2.3 Branch p = 0

This branch is covered only by the Gröbner chart elimination `k3_six_step_factor_check.py` (`7d761090…d4ff`; ChatGPT executed it independently: 14/14 charts, exit 0). It is **not used** by Theorem 6S, because p(κ) ≠ 0 for all real κ ≠ 2.

### 2.4 Corroboration at sample points (not a proof)

`lemmaS_burnside_check.py` computes, exactly over ℚ(√3), the real algebra generated by {Df(x)} at five rational points:
- for p(κ), q(κ) with κ ∈ {1, 1/2, −1, 3/2, 7}: dim = 16, i.e. M₄(ℝ), so there is no common invariant subspace;
- for the q = 0 control: dim = 8.

---

## 3. Theorem 6S

**Notation.**
- E is a local C³ submersion near 0 onto a d-manifold, d ∈ {1, 2, 3}, and ℓ = DE(0).
- T′ is a local C³ map near E(0).
- The six-step contract is E∘F⁶ = T′∘E.

### 3.1 `[THM]` 6S-core: κ = 1 on the carrier 𝒞

On 𝒞 with F₁ = P_𝒞T^{×3} (Genesis v2.8.6 §6.3a model), there is no pair (E, T′) as above with E∘F₁⁶ = T′∘E near 0. **No hypothesis is placed on T′ beyond C³** — not on its linear part, and not that T′ = T⁶.

*Proof.*
1. ℓ·DF₁⁶(0) = DT′(E0)·ℓ, and DF₁⁶(0) = I on 𝒞. Since ℓ is onto, DT′(E0) = I.
2. F₁⁶ = id + g with g = O(|x|²). Its leading homogeneous term commutes with Λ = DF₁(0). A quadratic Λ-equivariant term would need λ^{a−b} = λ with a + b = 2, which is impossible. So F₁⁶ has no quadratic term.
   - Comparing degree 2 in E∘F₁⁶ = T′∘E gives t₂∘ℓ = 0, so t₂ = 0.
3. At degree 3, E₂ and E₃ cancel on both sides (E₂(x + f) − E₂(x) = O(|x|⁴)). This leaves ℓ∘f₁ = t₃∘ℓ, with f₁ = f_{κ=1}.
4. p(1) ≠ 0 and q(1) ≠ 0 (§1.3). Lemma S (§2.2) excludes every d. ∎

### 3.2 `[THM — conditional]` 6S-κ: κ ∈ ℝ ∖ {0, 2} on ℝ⁶

**(H_spec)** μ_cl := (1−κ)⁶ ∉ spec DT′(E(0)).

Under (H_spec), there is no pair (E, T′) as above with E∘F_κ⁶ = T′∘E near 0.

**Sufficient forms of (H_spec):**
- spec DT′(E0) lies on the unit circle and κ ∉ {0, 2} (since |1−κ| ≠ 1);
- in particular, any dyad target T′ = T⁶ (DT⁶ = I), and any T′ that is a local diffeomorphism when κ = 1 (μ_cl = 0).

*Proof.*
1. **The kernel contains the closure plane.** DF_κ⁶(0) = I on T₀W^c and μ_cl·I on the closure plane Σ. For c ∈ Σ, ℓ·DF⁶·c = DT′·ℓc gives (DT′ − μ_cl)ℓc = 0. By (H_spec), ℓc = 0, so Σ ⊆ ker ℓ.
2. **Restrict to the centre manifold.** W^c is F-invariant and C³. ℓ|T₀W^c is onto, because ℓ is onto and Σ ⊆ ker ℓ. So E|W^c is a C³ submersion and E|W^c ∘ F⁶|W^c = T′∘E|W^c.
3. Steps 1–4 of §3.1 apply verbatim to F⁶|W^c, with cubic f_κ and p(κ), q(κ) ≠ 0. ∎

**Equivalent route.** Replace (H_spec) by the v0.2 assumption "ker DE(0) ⊇ Σ". (H_spec) is preferred because it is a checkable condition on the target, and it covers both dyad clocks.

### 3.3 Why a hypothesis is needed on ℝ⁶

**At κ = 1:** E(w) = Σ_e w_e is a submersion ℝ⁶ → ℝ² and E∘F₁ = 0. So E∘F₁⁶ = T′∘E with T′ ≡ 0.
- This factor violates (H_spec): μ_cl = 0 ∈ spec(0).
- It is exactly the closure-mode target.

**For κ ≠ 1:** the analogous closure-type factor (ker = 𝒞) is not settled. It stays `[OPEN]`, non-gating for G2, because it violates (H_spec) whenever DT′ has unit-circle spectrum.

### 3.4 Primitive clock

Any primitive-clock factor E∘F = T′∘E induces a six-step factor E∘F⁶ = T′⁶∘E, and T′⁶ is C³.

- **On 𝒞 (κ = 1).** 6S-core therefore re-excludes primitive-clock factors at C³ for every d. This adds nothing new over Genesis v2.8.6, whose primitive-clock statement is stronger for d = 1, 3 (C¹). That C¹ statement stays separate and is not absorbed.
- **On ℝ⁶.** The induced six-step target satisfies (H_spec) iff (1−κ)⁶ ∉ (spec DT′)⁶. The primitive-clock analogue of step 1 needs only (1−κ)λ ∉ spec DT′(E0).

---

## 4. Regularity

| Statement | Clock | d = 1, 3 | d = 2 |
|---|---|---|---|
| Genesis v2.8.6 §6.3a (adopted) | primitive | excluded at C¹ | excluded at C³; C¹/C² OPEN |
| 6S-core (κ = 1, 𝒞) | six-step | excluded at C³ | excluded at C³; C¹/C² OPEN |
| 6S-κ (ℝ⁶, H_spec) | six-step | excluded at C³ | excluded at C³; C¹/C² OPEN |

At the six-step clock, d = 1, 3 need C³, not C¹. The C¹ argument at the primitive clock uses DF(0) = λ, which makes ℓ complex-linear. At the six-step clock DF⁶(0) = I carries no such selectivity.

---

## 5. Scope (SG-15 style)

**6S does not:**
- give a physical node-exchange verdict or a carrier selection;
- choose a physical κ;
- cover the h-transported carrier (§5b of the G2 note);
- cover the closure-mode target (ker = 𝒞 for κ ≠ 1);
- settle κ = 2;
- settle C¹/C² for d = 2 at either clock;
- import Dyadic OPEN 19 results or create any new network–dyad bridge.

**RRF consumer wording must not exceed:**
- 6S-core: "no local C³ submersive factor of the raw projected K₃ under the six-step contract, for any target dimension 1–3";
- 6S-κ: the same, "for κ ∉ {0, 2}, under (H_spec)".

**Typo flagged in the disposition (§3).** "ℓL = BL" should read ℓL = B_tgt ℓ; the disposition already corrects it in the boxed line.

---

## 6. Source manifest

| File | SHA-256 | Role | Executed | Result |
|---|---|---|---|---|
| `K3_KAPPA_SIX_STEP_CLOCK_NOTE_v0_2.md` | `13f8c67964ff4dc33e731634eb0d18e6bec2c6c9f59ef73e0287c2623a92605f` | predecessor | — | — |
| Genesis-side disposition (17 Oct) | `8e3f465eeceed9e09db5d17af6dbba51be44fb4c2b56c3a878fa41bf3b7419bc` | review input | — | — |
| `exact_q.py` | `44105683b5da2b57fa9dfbd2f9e05488107c560f7b7fae7ab88b6ae24d4a6001` | q(κ) at 7 points + degree bound | ChatGPT; PI rerun (5 min 27 s) | identical output |
| `exact_q_output.txt` | `951a6f24e021b7e9cac3b88f2cb6a8369ed4ae6d4bbec80f898d678fcde1dddc` | recorded output | — | — |
| `kappa_pq_independent.py` | `7056b077e30ff498b17cf96737a32366305995283de3e332d38654bbfe4aef97` | own ψ₂, ψ₃; both components; 5 points | Claude; ChatGPT rerun unmodified | ALL PASS, exit 0 |
| `kappa_pq_symbolic.py` | `091a42105cff7965127c55a4a5adffa281021cd71957ed789409de320c5d42b2` | p, q as identities in ℚ(κ)(i√3) | Claude (≈14 s; needs sympy) | ALL PASS, exit 0 |
| `lemmaS_hand_identities.py` | `af8e79c36f2312c78150c808e5a7a57fc6aeccba9de5355263f5b9c012989674` | audit of §2.2 identities I1–I5 | Claude (<1 s; needs sympy) | 5/5 PASS, exit 0 |
| `lemmaS_burnside_check.py` | `2429212d0c8d38c240a03bac66b8157c687697348c9187f596a0dbc71cb6ea9d` | M₄(ℝ) corroboration at 5 κ + q = 0 control | Claude; ChatGPT rerun unmodified | ALL PASS, exit 0 |
| `k3_six_step_factor_check.py` | `7d761090…d4ff` (**full hash to be pinned from the source file**; not held by Claude) | Lemma S, p = 0 branch (Gröbner) | ChatGPT | 14/14 charts, exit 0 |
| Genesis v2.8.6 (adopted) | `294c6fc26482d7deae42900cb50b3029ac81e96d66e239bfe8b797e95fdaa269` | §6.3a model, c₀, β* | — | — |

**Requested before the owner gate:**
1. An independent rerun of `kappa_pq_symbolic.py` and `lemmaS_hand_identities.py`.
2. The full SHA-256 of `k3_six_step_factor_check.py`.

---

## 7. Routing

| Item | Owner | Action |
|---|---|---|
| §1 data, Lemma S (§2), 6S-core, 6S-κ | Genesis | SESSION record → owner review. Candidate content of a v2.8.7 successor: 6S-core as a clock extension of §6.3a / SG-15; F_κ as a new `[DEF]` with 6S-κ as a separate conditional theorem |
| K3 export citation now; 6S after Genesis adoption | RRF | v0.8.3 consumer line, worded no stronger than §5 |
| Closure-mode factor (κ ≠ 1), κ = 2, d = 2 at C¹/C² | Genesis | `[OPEN]`, non-gating |
| Physical κ, A1/A2/B | OFN | unchanged |
