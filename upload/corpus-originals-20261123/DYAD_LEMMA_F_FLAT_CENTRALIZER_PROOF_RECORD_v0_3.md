# DYAD Lemma F — flat centralizer triviality for the six-step return: proof record v0.3

**Date:** 18 October 2026 · **Author:** Claude (Dyadic DSN owner/editor) · **Status:** `[SESSION]` proof record. External review of v0.2 (18 Oct 2026; v0.2 SHA-256 `0a2ae5e266a9d9dd175503df4ea9629c10978637bdaadadc38e75a94fb104dfb`): Lemma F with D1–D3 ACCEPT; F1–F3 ACCEPT (conditional on Lemma F); one scope correction R1 applied here (§3.4). Nothing here is owner-adopted. Adopted DYAD v6.4.12.1 is unchanged.

**v0.3 change:** §3.4 only — the C⁰-convergence sentence for the construction plan is withdrawn as unproved (review R1). The lemma, its proof and F1–F3 are unchanged.

**Supersedes:** v0.2 (kept unchanged); and §4 of `DYAD_OCT18_CORPUS_REVIEW_AND_OPEN20_SESSION_v0_1.md` (SHA-256 `aedd8e69…702f`).

**Changes from v0.1, per the PI/reviewer work decision of 18 Oct:**
- **Domain conditions:** fixed explicitly in §1 (D1–D3).
- **Regularity:** stated separately for the lemma and for each corollary (§3). The lemma needs no regularity of C at all, only value-level flat contact. The corollaries need C^∞ only to *derive* that contact from jets (§3.0).
- **K:** a numerical illustration of K is added (§4). It is not used in the proof.

**Inputs (all adopted):**
- `DYAD-THM-PRIM-CTR`: for 0 < Q ≤ 1/400, Q(F x) ≤ Q − ½Q², where Q = |W|² in the raw frame W = 𝓛(ρ,η).
- `DYAD-THM-C21` and `DYAD-ALG-CUBIC-PARABOLIC`: F = T⁶ = id + μ|W|²W + O(|W|⁴), analytic, with no quadratic term.
- `DYAD-THM-FORMAL-CENTRALIZER` and `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`, used only in the corollaries.

---

## 1. Setting and domain conditions

Write B_s := {W : Q(W) ≤ s}. Q is a positive-definite quadratic form, so B_s is a compact convex disk.

**(D1) Constants.**
- F is analytic near 0, F(0) = 0, and DF(W) − I = O(|W|²).
- Fix s₀ ∈ (0, 1/400] such that F is defined on a neighbourhood of B_{s₀}.
- Then there is K > 0 with ‖DF(W) − I‖ ≤ K·Q(W) on B_{s₀} (operator norm for the Euclidean norm on ℂ ≅ ℝ²).

**(D2) Radii.** Choose r > 0 with 4r ≤ s₀ and 4rK ≤ ½. Put B := B_{4r}.

**(D3) Forward invariance.**
- B_r and B are F-forward-invariant, because Q(Fx) ≤ Q(x) on B_{1/400}.
- Every orbit in B obeys Q(F^k z) ≤ Q(z)/(1 + ½Q(z)k) ≤ min(4r, 2/k) for k ≥ 1.
- Proof: q ↦ q − ½q² is increasing on [0, 1], so the one-step bound iterates. The second inequality is 1/(1/q + k/2) ≤ 2/k.

## 2. Lemma F `[THM — SESSION candidate]`

**Statement.** Let C: B_r → B be **any map** (no continuity assumed) such that:
- (i) C∘F = F∘C on B_r. Both sides are defined there by (D3).
- (ii) For every N there is c_N with |C(W) − W| ≤ c_N |W|^N on B_r.

Then C = id on B_r.

*Proof.* Fix x ∈ B_r and put a := C(x) ∈ B, b := x ∈ B_r ⊂ B.

1. **Iterating (i).** Since F(B_r) ⊂ B_r, induction gives F^n(C(x)) = C(F^n(x)) for every n.
2. **Lower Lipschitz bound.** Let a_k = F^k a and b_k = F^k b. Both lie in B by (D3), and so does the segment between them (B is convex). On that segment Q ≤ q_k := max(Q(a_k), Q(b_k)), because Q is convex. By (D1) and the mean-value inequality,
   |a_{k+1} − b_{k+1}| ≥ |a_k − b_k| − |(F − id)(a_k) − (F − id)(b_k)| ≥ (1 − K q_k)|a_k − b_k|.
3. **Polynomial loss.**
   - By (D3), q_k ≤ min(4r, 2/k), and K q_k ≤ ½ by (D2).
   - Using ln(1 − u) ≥ −2u for u ∈ [0, ½]:
     Σ_{k<n} ln(1 − K q_k) ≥ −2K(4r + Σ_{1≤k<n} 2/k) ≥ −2K(4r + 2 + 2 ln n).
   - Hence |a_n − b_n| ≥ c₀ n^{−4K} |a − b|, with c₀ = e^{−2K(4r+2)}.
4. **Superpolynomial gain.** By step 1 and (ii), |a_n − b_n| = |C(F^n x) − F^n x| ≤ c_N |F^n x|^N = c_N Q_n^{N/2} ≤ c_N (2/n)^{N/2}.
5. **Conclusion.** |C(x) − x| ≤ c₀⁻¹ c_N 2^{N/2} n^{4K − N/2} for every n. Take N > 8K and let n → ∞. Then C(x) = x. ∎

**Remarks on scope.**
- No derivative or continuity of C is used. All analytic estimates are on F alone, so the lemma is a value-level statement.
- Only the radial contraction (Re μ < 0, through `DYAD-THM-PRIM-CTR`) is used. The chirality Im μ ≠ 0, the formal centralizer and the lattice term are not.
- The lemma is local and fixes B_r once r is chosen. For germs, any smaller r also works.
- The exponent bookkeeping is generous. The point is that the loss is polynomial in n while the gain is faster than any polynomial.

## 3. Corollaries `[THM — conditional on Lemma F; SESSION]`

### 3.0 From jets to value-level flatness (regularity)

Let C be a composition of finitely many maps, each C^∞ near 0 and fixing 0. Then C is C^∞, and its Taylor series j^∞C is the formal composition of the factors' Taylor series (chain rule / Faà di Bruno).

If j^∞C = id, Taylor's theorem with remainder gives (ii) on a small ball: for each N, C(W) − W = O(|W|^N).

This is the **only** place where C^∞ is used. Finite C^k gives (ii) only for N ≤ k. That is not enough for step 5 unless k > 8K, and no finite-regularity statement is made here.

### 3.1 F1 — C^∞ clock bridge

**Hypotheses.**
- R is a C^∞ local involution satisfying the §6.15 domain convention for Φ = F, with R(0) = 0.
- RF = FR on D_F, and DR(0) = −I.

**Conclusion.** RT = TR on a neighbourhood of 0.

*Proof.*
1. Choose r so small that the following hold on B_r:
   - C := T∘R∘T⁻¹∘R is defined, with T⁻¹ the local analytic inverse;
   - every intermediate point lies in int D_F ∩ (domain of T⁻¹);
   - C(B_r) ⊂ B.
   This is possible because C is C^∞ with C(0) = 0 and DC(0) = A(−I)A⁻¹(−I) = I.
2. **Commutation.** T commutes with F, so T⁻¹ does too near 0, and R commutes with F on D_F. So C∘F = F∘C on B_r.
3. **Jet.** By §3.0, j^∞C = T∘R₀∘T⁻¹∘R₀. Here j^∞R = R₀ by `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`. Since R₀ commutes with T and R₀² = id, this jet is id. So (ii) holds.
4. Lemma F gives C = id, i.e. TRT⁻¹ = R⁻¹ = R. ∎

The analytic case (`DYAD-THM-ANALYTIC-CLOCK-BRIDGE`) is a special case.

### 3.2 F2 — C^∞ uniqueness

**Statement.** Two such involutions R, R′, each commuting with F with linear part −I, coincide on a neighbourhood of 0.

*Proof.* Apply Lemma F to C := R′∘R. Its jet is R₀R₀ = id, and it commutes with F. ∎

### 3.3 F3 — smooth roots commute with T and are unique

**Statement.** Let K be C^∞ near 0, tangent to the identity, with K^m = F for some m ≥ 1 (m = 2, 3, 6 are the cases of interest). Then:
- K commutes with T;
- K is the unique such C^∞ germ.

*Proof.*
1. **Commutation with F.** K commutes with F, since KF = K^{m+1} = FK.
2. **Jet.** The formal m-th root tangent to the identity is unique: exp(X/m), by the exp/log bijection on the pro-unipotent group. So j^∞K = exp(X/m).
3. **Commutation with T.** TKT⁻¹ is also a C^∞ m-th root of F tangent to the identity, because T commutes with F. Its jet is T exp(X/m) T⁻¹ = exp(X/m). Then C := TKT⁻¹K⁻¹ commutes with F and has jet id. Lemma F gives TK = KT.
4. **Uniqueness.** For two such roots K, K′, C := K′K⁻¹ commutes with F and has jet id. ∎

**Consequence.** In the C^∞ category the following are equivalent:
- F^{1/6} exists;
- the ℤ₆ generator J = T∘F^{−1/6} exists, with J⁶ = id and J commuting with T;
- a C^∞ chart exists in which T is exactly λ-equivariant (Bochner averaging).

No separate commutation hypothesis is needed. The same holds for F^{1/2} ↔ R₀ (odd chart) and F^{1/3} ↔ G.

### 3.4 What is not proved

- **Existence (OPEN 20 B-∞).** The existence of any C^∞ root, involution or J is **not** proved. A **proposed** construction route is the conjugation sequence F^{−n}∘R_∞∘F^n, with R_∞ a Borel realization of R₀. `[COR v0.3, review R1]` C⁰ convergence of this sequence, convergence of higher derivatives, and the commutation properties of a limit are **not proved**. Lemma F proves uniqueness of an already existing F-commuting flat-close map; it does not by itself show that approximately commuting conjugates converge. (v0.2 stated that C⁰ convergence follows from the estimates of steps 2–5; that sentence is withdrawn. The same withdrawal applies to §4 (F4) of the SESSION note v0.1.)
- **Analytic questions (B-an, B-6).** Untouched.
- **Physical realization.** No physical exchange or G2 realization; the factor contracts EF = TE and EF = T⁶E are not identified (SG-14/15).

## 4. Numerical illustration (not a proof input) `[NUM]`

Central differences of the exact F = T⁶ in the W-frame, sampled on 72 directions, give:

| Radius |W| | 0.005 | 0.01 | 0.02 | 0.05 |
|---|---|---|---|---|
| max ‖DF − I‖/Q | 3.80 | 3.83 | 3.89 | 4.07 |

This is consistent with ‖DG₃(W)‖ ≤ 3|μ| Q, where 3|μ| ≈ 3.77. With K ≈ 4, step 5 needs N ≳ 32 under the generous bookkeeping above. Any finite N suffices, because C − id is flat.

## 5. Review requests

1. **(D1)–(D3)** and step 2: the mean-value inequality on a convex sublevel set of Q, with Q-convexity bounding Q along the segment.
2. **Step 3:** the polynomial lower bound, which uses only q_k ≤ 2/k.
3. **§3.0 and the domain choices in F1:** that C maps B_r into B and commutes with F there.
4. **F3's use of unique formal roots:** exp/log on the pro-unipotent group.
