# DYAD OPEN 20 / O20-∞ — Smooth embedding: P1 literature audit and scope note

**Version:** v0.1 · **Date:** 19 October 2026 · **Author:** Dyadic DSN owner (Claude)
**Status:** `[SESSION]` literature audit and scope note. **Scope preparation only.** No existence or non-existence result is claimed. DYAD v6.4.17 is unchanged.
**Authorization:** PI decision of 19 Oct 2026 — O20-∞ opened with the P1 literature audit and a SESSION scope note only. This is not a scientific acceptance of C^∞ root existence or of analytic convergence. O20-an stays deferred. No heavy formal-log coefficient campaign at this stage.
**Statuses unchanged** (DYAD v6.4.17): OPEN 20 PARTIAL; B-an, B-6 and B-∞ existence OPEN. No physical, G2 or network-exchange claim (SG-14/15).

## 1. The question (C^∞ category)

**Setting.** F = T⁶ near P₁ in the lifted (ρ,η)-plane, in the raw linear frame W = 𝓛(ρ,η):
- F = id + G₃ + O(|W|⁴), with G₃(W) = μ|W|²W and μ = −½ − 2i√3/3;
- X̂ = log F is the formal logarithm, with X̂₃ = μ|W|²W.

**Question Q∞.** Is there a C^∞ vector field X near 0 with F = exp(X) **exactly** on a neighbourhood of 0?

**Consequence if Q∞ holds.** K := exp(X/6) is a C^∞ tangent-to-identity sixth root of F. By F3 (§6.17) it is unique and commutes with T. Hence J := T∘K⁻¹ satisfies J⁶ = id, DJ(0) = A and JT = TJ. Likewise F^{1/2} = exp(X/2) and R := T³∘F^{−1/2}. This settles B-∞ existence for F^{1/6}, J and F^{1/2}.

**Precision 1: Borel realization is not enough** (reviewer note). A C^∞ field X_∞ with j^∞X_∞ = X̂ exists by Borel's lemma. G := exp(X_∞) then satisfies j^∞G = j^∞F, but **G = F does not follow**.
- The whole difficulty is removing the flat difference F − G.
- Lemma F gives **uniqueness** of a flat-close commuting map. It does **not** give the existence of the correcting map.

**Precision 2: J versus the sixth root** (reviewer note).
- **K ⇒ J (holds).** If K is C^∞ with DK(0) = I and K⁶ = F, then F3 gives KT = TK. So J = TK⁻¹ satisfies J⁶ = T⁶K⁻⁶ = id, DJ(0) = A and JT = TJ.
- **J ⇒ K (needs an explicit hypothesis).** Suppose J is C^∞ with J⁶ = id and DJ(0) = A. Setting K := J⁻¹T gives K⁶ = F **only if J commutes with T**. The condition J⁶ = id with DJ(0) = A is not sufficient by itself.
- **Equivalence used in O20-∞:** B-∞(F^{1/6}) ⟺ there is a C^∞ J with J⁶ = id, DJ(0) = A **and** JT = TJ.

## 2. P1 — literature audit (first pass)

| Source | What it proves (as inspected) | Applies to F? |
|---|---|---|
| Takens 1973, *Normal forms for certain singularities of vectorfields*, Ann. Inst. Fourier 23(2):163–195 | Thm 1–2: C^∞ normal forms for non-flat vector fields and diffeomorphisms of **ℝ¹**. **Thm 4: a C^∞ diffeomorphism of ℝ¹ with Y(x) = x + x^kF(x), F(0) ≠ 0, k ≥ 2, is near 0 the time-one map of a C^∞ vector field.** Thm 3: C^∞ normal form for **vector fields** on ℝ² whose 1-jet is a rotation (with a radial term of definite sign, or flat). Method: a functional equation removes the flat terms (Thm 4.1). Prop 5.1: a germ with the ∞-jet of the identity that commutes with Y is the identity. | **Not directly.** Thm 4 is one-dimensional. Thm 3 concerns vector fields, not diffeomorphisms, and has a rotation 1-jet rather than the identity. **The method is the template:** Prop 5.1 is the ℝ¹ analogue of DYAD Lemma F; Thm 4.1 is the flat-removal step that Q∞ needs. |
| Zhang 2010 (*JDE* 248) and 2011 (*JDE* 250); Ribón 2012 (*JDE* 253:3211–3231, arXiv:1107.3601) | Embedding of **hyperbolic** C^∞ diffeomorphisms in C^∞ flows. Weak nonresonance gives embeddability; a sharp non-embeddability criterion is given. | **No.** F is tangent to the identity, not hyperbolic. Not inspected beyond the abstracts. |
| Roussarie 1975, *Modèles locaux de champs et de formes*, Astérisque 30 | Lead only: C^∞ determinacy of vector fields satisfying a Łojasiewicz inequality. | **Not inspected.** It concerns vector fields. Whether a diffeomorphism analogue exists is open in this audit. |
| Belitskii; Chaperon (Astérisque 138–139, 1986) | Leads only: C^∞ conjugacy and flat-perturbation theorems for local maps. | **Not inspected.** |

**P1 conclusion (v0.1).**
- No theorem has been located that applies **directly** to C^∞ planar germs tangent to the identity with a non-degenerate attracting cubic formal logarithm.
- The closest exact results are Takens' one-dimensional Thm 4 and his flat-removal method.
- So O20-∞ proceeds by a **self-contained flat-conjugacy proof (P3)**, unless the remaining leads (Roussarie, Belitskii, Chaperon) turn up an exact statement. Inspecting those is P1-b.

## 3. Reduction: Q∞ ⇐ the flat-conjugacy lemma (L-FC)

**(L-FC)** Let G = exp(X_∞) be the Borel realization. Then there is a C^∞ germ Φ with j^∞Φ = j^∞id and Φ∘F = G∘Φ near 0.

**Why L-FC suffices.** F = Φ⁻¹∘G∘Φ = exp(Φ*X_∞), so X := Φ*X_∞ is C^∞ and F = exp(X). Q∞ holds.

**Uniqueness.** If Φ and Φ′ both satisfy L-FC, then Φ′∘Φ⁻¹ is flat-close to the identity and commutes with G. A Lemma F-type argument for G (same contraction estimates) shows Φ is unique.

**Candidate construction (Sternberg/Takens type).** Φ := lim_{n→∞} G^{−n}∘F^n.
- *Formally:* Φ∘F = lim G^{−n}F^{n+1} = G∘lim G^{−(n+1)}F^{n+1} = G∘Φ.
- *Telescoping:* G^{−(n+1)}F^{n+1} − G^{−n}F^n = G^{−(n+1)}(F(y_n)) − G^{−(n+1)}(G(y_n)), with y_n = F^n(z). This is G^{−(n+1)} evaluated at two points whose difference (F − G)(y_n) is flat in |y_n|.

**Why convergence is plausible** `[HEUR]` (FMS co-owner note):
- the jet attracts in every direction (M + Mᵀ = −I);
- orbits shrink at the rate |y_n| ~ n^{−1/2};
- flat differences are O(|y_n|^N) for every N;
- derivatives of G^{−n} along the orbit grow at most polynomially, as in the n^{4K} estimate of Lemma F.

This is **not** a proof. Making these estimates uniform, including all derivatives, is the content of P3.

## 4. Proof obligations

| ID | Obligation | Inputs | Output |
|---|---|---|---|
| **P1-b** | Inspect Roussarie 1975, Belitskii and Chaperon 1986 for an exact diffeomorphism statement. Record its hypotheses verbatim, or record that none applies. | Library access | Either a citation route to Q∞ or confirmation of the self-contained route |
| **P2** | Orbit control for F and G on a common forward-invariant domain: c/(m+κ) ≤ \|y_m\|² ≤ C/(m+κ) uniformly. Also the same for G, and for G⁻¹ on the region the construction uses. | PRIM-CTR (F); the same majorant argument for G (identical jet) | Two-sided decay; domain of G^{−n} along F-orbits |
| **P3-a** | Derivative growth: ‖D^kG^{−n}(w)‖ ≤ C_k·n^{a_k}, for w near the F-orbit at radius ~ n^{−1/2}. Faà di Bruno plus the product bound ∏(1 + K q_m) ~ n^{c}. | P2; the C^k jets of X_∞ | Polynomial exponents a_k |
| **P3-b** | Flat-difference decay in C^k: ‖F − G‖_{C^k(B_ρ)} ≤ c_{N,k}ρ^N for every N. | Borel realization; Taylor | Flat bounds |
| **P3-c** | Convergence of Σ_n ‖G^{−(n+1)}F^{n+1} − G^{−n}F^n‖_{C^k} using P3-a and P3-b with N > 2a_k + 2. Also show that the limit Φ is C^∞, flat to the identity, and a local diffeomorphism. | P2, P3-a, P3-b | L-FC |
| **P4** | Consequences: K = Φ⁻¹exp(X_∞/6)Φ, J = TK⁻¹, F^{1/2}, R = T³F^{−1/2}. Commutation with T follows from F1–F3. | L-FC, §6.17 | B-∞ existence for F^{1/6}, J and F^{1/2} |

**Regularity and domain.**
- C^∞ local germs at P₁ in the lifted plane, with the §6.15 domain convention.
- The working domain is a forward-invariant ball B_{4r} inside the six-phase tube of DYAD-THM-PRIM-CTR (as in Lemma F).
- No analytic claim. No finite-C^k claim unless it is stated separately.

## 5. Result criteria

- **Positive (Q∞ true).** L-FC is proved, either by citation with verified hypotheses or by P2–P3. This gives B-∞ existence for F^{1/6}, J (with JT = TJ) and F^{1/2} at C^∞ grade. It realizes FMS/OFN class C at C^∞ regularity and is a `[THM]` candidate after review. It says nothing about analyticity (O20-an).
- **Negative.** An obstruction to **every** C^∞ tangent-to-identity sixth root of F. By F3 such a root is unique and realizes the unique formal root, so a negative result must show that no C^∞ germ with that jet commutes with F and has sixth power F.
  - Failure of the construction in §3 is **not** a negative result.
  - Divergence of the §6.17 conjugation sequence is not one either.
- **Partial.** Must be labelled as such. Examples:
  - C^k roots for each finite k on k-dependent neighbourhoods;
  - L-FC proved only for a modified G, such as a truncated jet;
  - Q∞ conditional on a cited theorem whose hypotheses are not fully verified.

## 6. Out of scope

- Analytic B-an and B-6 (O20-an, deferred).
- The formal-log coefficient campaign (not started; the deferred `[NUM]` growth diagnostic may be prepared separately, as FMS offered).
- Any change to OPEN 19, to Lemma F / F1–F3 or to their grades.
- Physical exchange, G2, RRF OPEN-A, OFN OPEN-OPA.

## 7. Next step

P1-b (the remaining leads), then P2, and then P3-a as the core estimate. Each step is a SESSION record; DYAD changes only after review and adoption.

## Sources

- F. Takens, [Normal forms for certain singularities of vectorfields](https://www.numdam.org/item/AIF_1973__23_2_163_0), Ann. Inst. Fourier 23 (1973) 163–195; [full text](https://www.numdam.org/item/10.5802/aif.467.pdf) (scanned OCR; statements paraphrased from it).
- J. Ribón, [Embedding smooth and formal diffeomorphisms through the Jordan–Chevalley decomposition](https://www.arxiv.org/abs/1107.3601), J. Differential Equations 253 (2012); abstract only.
- X. Zhang, publication list in [Recent results on embedding diffeomorphisms in flows](https://math.seu.edu.cn/2011/1009/c15556a150941/page.htm) (talk announcement; titles only).
- R. Roussarie, [Modèles locaux de champs et de formes](https://www.numdam.org/item/AST_1975__30__1_0), Astérisque 30 (1975); not inspected.
