# DYAD OPEN 20 / O20-an — P1-c-2: original statements of the parabolic-curve literature, checked against the complexified DYAD germ (SESSION v0.1)

**Version:** v0.1 · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Basis.** P1-c-5 SESSION v0.1 (`11917ba2…e36b`), reviewed as `SCIENTIFIC REVIEW ACCEPTED — CONDITIONAL RESULTS ONLY`. The review approved P1-c-2 ahead of the P1-c-5d high-order campaign: first establish what the existing theorems already deliver about sectorial curves and Stokes data, then point any expensive computation at the right object.

**Status.**
- `[SESSION]` record. Nothing is adopted.
- DYAD v6.4.18 is unchanged; OPEN 20 PARTIAL; B-an and B-6 OPEN.
- Convergence and divergence of φ± are both OPEN.
- P1-c-5d has not been run.

**Check script.** `dyad_open20_an_p1c2_check.py`, with helpers `qw.py`, `fzw.py`, `ext.py` and `logzw.py` (unchanged copies from P1-c-5). It writes `p1c2_check.json` (byte-deterministic; verified by rerun) and `p1c2_perf.json` (timings only).
- 7 gates (K1–K7) and 4 negative controls (N1–N4).
- Runs in about 1 s.

**Exact fields.** K = ℚ(ω) with ω = i√3. E = K[a]/(Aa² + Ba + C), where a = a₂ stands for either root of the P1-c-5 quadratic; an identity proved in E holds for Γ₊ and Γ₋ at once.

## 0. Dispositions from the P1-c-5 review

The P1-c-5 record is not modified. These points are recorded here.

| Item | Disposition |
|---|---|
| Résidu itératif convention | The reviewer checked it against the literature: résit(g) = mult(g)/2 − ι, so résit = 2 − ι for multiplicity 4. This supersedes "as I recall" in P1-c-5 §2. The owner has not re-read that source. `[LIT — reviewer-checked]` |
| "Best bound" (P1-c-5 §3.2) | To be read as the growth scale the crude majorant predicts, not as an optimality statement. Accepted. |
| **Citation erratum** | arXiv:1411.2945 is **L. López-Hernanz and F. Sanz Sánchez**, "Parabolic curves of diffeomorphisms asymptotic to formal invariant curves" (DOI 10.1515/crelle-2015-0064). The four-author paper (López-Hernanz, Raissy, Ribón, Sanz-Sánchez) is **arXiv:1710.03728**, "Stable manifolds of two-dimensional biholomorphisms asymptotic to formal curves". P1-b v0.1/v0.1.1, P1-c and P1-c-5 attribute 1411.2945 to the four authors; this record corrects the attribution. |

## 1. Sources read

All were read in full text, except where marked. The hashes are SHA-256 of the PDFs as downloaded on 20 Oct 2026. Preprint versions were read; published versions were not compared.

| Key | Source | Version read | PDF SHA-256 |
|---|---|---|---|
| [A01] | M. Abate, "The residual index and the dynamics of holomorphic maps tangent to the identity", Duke Math. J. 107 (2001) 173–207 | author's preprint (Sept 1999), pagine.dm.unipi.it | `631add628dc280a339f97f6eb22d6663ac5dfb5da71b7ab381691609eee34248` |
| [AT] | M. Abate, F. Tovena, "Poincaré–Bendixson theorems for meromorphic connections and holomorphic homogeneous vector fields" | arXiv:0903.3485v3 | `b55b8e42e25048edd58fc9e1804d3cd97c5d1a9eaea2e0da3833ab88ca730cc1` |
| [V] | L. Vivas, "Degenerate characteristic directions for maps tangent to the identity" | arXiv:1106.1471v2 | `f2a44382ee8255578c92fbdd6065afa2d310ea7544e349cd9262a1eb12adfbf5` |
| [LS] | L. López-Hernanz, F. Sanz Sánchez, "Parabolic curves of diffeomorphisms asymptotic to formal invariant curves", J. reine angew. Math. (DOI above) | arXiv:1411.2945v1 | `842c157049ace0569e560e6c8cc9ce1b1fdd4f7bb8f69bd57ed099df20561f1f` |
| [LRRS] | L. López-Hernanz, J. Raissy, J. Ribón, F. Sanz-Sánchez, "Stable manifolds of two-dimensional biholomorphisms asymptotic to formal curves" | arXiv:1710.03728v1 | `77347e41915904c42ddc4fc3f5db78f221849118509309b29229fa0bdacb8c71` |
| [BL] | F. E. Brochero Martínez, L. López-Hernanz, "Gevrey class of the infinitesimal generator of a diffeomorphism", Astérisque 323 (2009) 33–40 | arXiv:math/0701355v1 | `33fea26f9159e300317ac91df840d37c271a779169fde9efcaf537613d681d75` |
| [L12] | L. López-Hernanz, "Summable formal invariant curves of diffeomorphisms", Ergodic Theory Dynam. Systems 32 (2012) 211–221, DOI 10.1017/S0143385710000805 | **abstract only**; full text not retrieved (no arXiv version found) | — |

The PDFs are not redistributed; only their hashes are recorded.

## 2. Exact data of the germ

`[ALG]`, gates K1–K5. Here F is the complexified F = T⁶ in the coordinates (z, w) = (W, W̄); it is a holomorphic germ at 0 ∈ ℂ².

- **K1. Order.** DF(0) = I, and F has no quadratic terms. The cubic part is exactly P₃ = (μz²w, μ̄zw²) with μ = −½ − 2ω/3. So F is tangent to the identity, and its order in the sense of [A01] is ν(F) = 3.
- **K2. Singular cone.** F is not dicritical, because wP₃ − zQ₃ = (μ − μ̄)z²w² = −(4ω/3)z²w² ≢ 0.
  - Since 0 is an isolated fixed point (P1-c-3), the gcd ℓ of the components of F − id is a unit. So the pure-order parts are P₃ and Q₃.
  - The singular cone vP₃(u,v) − uQ₃(u,v) = −(4ω/3)u²v² has the singular directions [1:0] and [0:1], each of multiplicity 2. The total is ν_o + 1 = 4, as [A01] §2 requires.
- **K3. Residual indices** ([A01] (1.10) and its mirror chart; the same formula is (6.5) in [AT] and §2 in [V]):
  - ι[1:0] = Res_{u=0} P₃(1,u)/(Q₃(1,u) − uP₃(1,u)) = μ/(μ̄ − μ) = −½ + ω/8;
  - ι[0:1] = −½ − ω/8;
  - their sum is −1, which matches the Residual Index Theorem ([A01] Thm 0.5/1.2, c₁ of the exceptional divisor = −1);
  - both indices are non-real, hence **not in ℚ⁺**.
- **K4. Type of the directions.** Both are degenerate and **Fuchsian**. This is checked both ways:
  - [V] §2: m = 1 and n = 2 at both directions;
  - [AT] Def. 6.1/7.1: μ_X = 2 = ord(∂g¹/∂z¹) + 1.

  This confirms P1-b §2 against the original [AT] text and closes the P1-b provenance limit. The [AT] data are:
  - ν_AT = 2 (Q has degree ν_AT + 1 = 3);
  - residue ρ = −ν_AT·ι = 1 − ω/4 at [1:0], and its conjugate at [0:1];
  - μ_Y = 1 and μ_Y − ρ = ω/4 ∉ ℕ*, so the direction is non-resonant;
  - **Re ρ = μ_Y with ρ ≠ μ_Y.**
- **K5. Identity.** k* = 2/ι[1:0] exactly, where k* = −64/19 − 16ω/19 is the P1-c-5 resonance root. The Briot–Bouquet ratio of P1-c-5 is therefore λ = k* − 2 = 2/ι[1:0] − 2.

## 3. Abate (2001)

**Statements read** ([A01]):
- **Theorem 0.4 = 3.2.** Let f be a germ of holomorphic self-map of ℂ² tangent to the identity, with the origin an isolated fixed point. Then there exist at least ν(f) − 1 parabolic curves for f at the origin.
- **Corollary 3.3.** Under the same hypotheses, let [v] be a singular direction of f whose residual index satisfies ι[v](f̃, ℙ¹) ∉ ℚ⁺. Then there are ν(f) − 1 parabolic curves tangent to [v] at the origin.

| Hypothesis | DYAD | Source |
|---|---|---|
| Holomorphic germ of ℂ², df_O = id | yes | K1 |
| O is an isolated fixed point | yes | P1-c-3 (accepted; Nakayama certificate, multiplicity 13) |
| [v] is a singular direction (in C_f) | [1:0] and [0:1] | K2 |
| ι[v] ∉ ℚ⁺ | −½ ± ω/8 are non-real | K3 |

**Consequence C1** `[THM — imported, hypotheses checked]`. F has at least ν − 1 = 2 parabolic curves tangent to [1:0] and at least 2 tangent to [0:1].

P1-c §1 had used Theorem 0.4 only through Vivas's summary. That use is now checked against the original. Corollary 3.3 gives the stronger, direction-wise statement.

## 4. Abate–Tovena and Vivas: no basin statement applies

### 4.1 [AT], Corollary 8.5

This result concerns **only the homogeneous vector field Q = P₃** and its time-1 map. It is not a statement about F.

At [1:0], the residue lies exactly on the borderline Re ρ = μ_Y, which is case (iii) of Corollary 8.5. For the model Q, no integral curve outside the characteristic leaf converges to the origin tangent to [1:0]. The convergent ones spiral, without a tangent direction.

**Reading** (`[HEUR]`).
- The cubic model of DYAD sits on a borderline.
- Q vanishes identically on both axes (Q(z, 0) = Q(0, w) = 0), so the model has non-isolated zeros.
- The dynamics of F along [1:0] is therefore decided by terms of degree ≥ 4. This matches P1-c-5, where ℓ = c₄₀ + μa₂ involves the quartic coefficient c₄₀.
- No [AT] conclusion is transferred to F.

### 4.2 [V], Theorem 1 / Theorem 7

These results give an open basin along a Fuchsian degenerate direction when a region condition holds. The paper states the condition in three non-equivalent ways:
- Theorem 1: "the real part of the inverse of the index belongs to R";
- Theorem 7: "Ind ∈ R";
- Proposition 2 uses a different circle centre.

It is proved through the sufficient Lemma 4. Gate K4 evaluates all of these readings for both directions, with k = 3 and m = 1. **Every one is false.**
- In the Theorem 7 reading, ι[1:0] lies **exactly on the boundary line** Re ζ = −m/(k − 1) = −½.
- Positive control N4: the point moved by 1/100 to the right is accepted.

This boundary is the same borderline as Re ρ = μ_Y in §4.1, since ρ = −2ι.

**Consequence** (`[LIT]`). Vivas's sufficient condition does not hold, so no open basin along [1:0] or [0:1] can be imported. This is not a non-existence statement.

## 5. López-Hernanz–Sanz and López-Hernanz–Raissy–Ribón–Sanz: parabolic curves asymptotic to Γ±

### 5.1 Statements read

- **[LS] Theorem 1.** For F ∈ Diff₁(ℂ², 0) and a formal invariant curve Γ not contained in Fix(F), there is at least one attracting or repelling parabolic curve asymptotic to Γ.
- **[LRRS] Theorem 1** (with Remark 1, m = 1). Let F ∈ Diff(ℂ², 0) and let Γ be an irreducible formal invariant curve with F|Γ rationally neutral and non-periodic. Then, in a small neighbourhood, there is a finite family of pairwise disjoint stable manifolds of positive dimension.
  - Every orbit in them is asymptotic to Γ.
  - Every orbit asymptotic to Γ is eventually contained in their union.
- **[LRRS] §4, Def. 4.1–4.3, Theorem 5.1, §7.**
  - After blow-ups along Γ, the pair (F, Γ) is reduced, with integers k, p: k + 1 is the order of the transformed F, and k + p + 1 the order of F|Γ.
  - There are k + p attracting directions.
  - If spec DF(0) = {1} and p = 0 (the Briot–Bouquet case), every attracting direction is a **saddle** direction.
  - Each saddle direction carries a parabolic curve S = {(x, ϕ(x)) : x ∈ R} asymptotic to Γ, which eventually contains every orbit asymptotic to Γ with that tangent direction (Thm 5.1).
  - §7: "if |µ| > 1 or |µ| = 1 and p = 0 … every S_j has dimension one".
  - Introduction: "In the case spec(DF(0)) = {1} and p = 0 (Briot-Bouquet case) … there exist k parabolic curves of F whose union is a base of convergent orbits asymptotic to Γ", as in Écalle and Hakim.

### 5.2 Hypothesis check

`[ALG]`, gates K6 and K7, exact in E (so for Γ₊ and Γ₋ at once).

**K6. The [LRRS] §4 reduction, run on Γ.**
- Blow up once (w = x·w₁). Γ becomes w₁ = φ(x)/x, which is smooth and transversal to the divisor {x = 0}.
- Change coordinates to y = w₁ − J₄(φ/x), as [LRRS] §4 prescribes with r + 1 = 4.
- Exactly:
  - x∘F|_{y=0} = x + ℓx⁴ + O(x⁵), with ℓ ≠ 0, so r = 3;
  - y∘F|_{y=0} = O(x⁵);
  - ∂_y(y∘F)|_{y=0} = 1 + c₃x³ + O(x⁴), so c₁ = c₂ = 0 and t ≥ 3 = r.
- By the rule in [LRRS] §4 ("k = r and p = 0 if t ≥ r"), **k = 3 and p = 0**.
- Also c₃ = ℓ(k* − 1) exactly. One blow-up later this ratio becomes the k* − 2 of P1-c-5. The shift by one per blow-up is the behaviour described in [LRRS] Remark 4.4.
- Negative control N3: with a wrong curve (φ = 0), the y-free part is not O(x⁵).

**K7. Γ± is of Briot–Bouquet type.** After the second blow-up (w = x²u), the reduced singularity of X̂/x³ at (0, a₂) has eigenvalues ℓ and λℓ.
- λ = k* − 2 is non-real, so the singularity is non-degenerate with ratio not in ℚ⁺.
- Γ̃ is tangent to the ℓ-eigendirection, transversal to the divisor.
- This is the Briot–Bouquet type of [LS] §1. It agrees with the P1-c-5 Briot–Bouquet data (H3).

| [LRRS] hypothesis | DYAD | Source |
|---|---|---|
| F ∈ Diff(ℂ², 0) | yes; spec DF(0) = {1} | K1 |
| Γ irreducible formal invariant curve | Γ± are graphs w = φ±(z), so prime ideals; invariant | P1-c-5 H1 |
| F\|Γ rationally neutral, non-periodic | g = z + ℓz⁴ + …, with ℓ ≠ 0 | P1-c-5, K6 |
| Reduced data | k = 3, p = 0, \|µ\| = 1 | K6 |

### 5.3 Consequence C2

`[THM — imported, hypotheses checked]`. For each of the two formal curves Γ₊ and Γ₋ tangent to [1:0]:
- (a) F has exactly k + p = 3 attracting directions along Γ, all of saddle type. There are 3 attracting **parabolic curves** asymptotic to Γ: one-dimensional graphs over sectors in the reduced coordinates. Every orbit of F asymptotic to Γ eventually lies in their union. No open (two-dimensional) stable set consists of orbits asymptotic to Γ.
- (b) The same holds for F⁻¹. Γ is F⁻¹-invariant ([LS] §2), and log F⁻¹ = −log F, so the reduced data k = 3 and p = 0 are unchanged; only the principal part changes sign. This was not separately gated. This gives 3 **repelling** parabolic curves asymptotic to Γ.
- (c) These curves exist **whether or not φ± converges**. They are the sectorial geometric realization of the formal curves.

The curves tangent to [0:1] are the images under the real structure of F. This is stated as `[HEUR]` here; the formal curves tangent to [0:1] were not recomputed in this session.

**Not covered.**
- Orbits converging tangent to [1:0] but not asymptotic to Γ± (for example, along singular Puiseux-type formal curves, whose absence P1-c-5 established only heuristically).
- The relation between the curves of C1 and those of C2. Plausibly the C1 curves are among the C2 curves; not checked.

## 6. Gevrey and summability

- **[BL] Theorem 1.1.** The infinitesimal generator of an analytic diffeomorphism tangent to the identity is (1/ν_BL(F))-Gevrey, where ν_BL(F) = min ord(xᵢ∘F − xᵢ) − 1. Here ν_BL = 2.
  - **Consequence C3** `[THM — imported, hypotheses checked]`: X̂ = log F is ½-Gevrey, i.e. Σ_k X̂_k/(k!)^{1/2} converges, with X̂_k the homogeneous parts.
  - This is a bound only. [BL] stresses that X̂ is in general divergent: in one variable, every entire map tangent to the identity has a divergent generator (Szekeres, Baker).
- **[L12]**, from the abstract only: "Camacho and Sad's formal invariant curves of X give summable formal power series, whose sums correspond to the parabolic curves found by Hakim for F and F⁻¹."
  - [LS] §1 describes the same result: for Γ of Briot–Bouquet type, the parabolic curves are Ramis sums of Γ.
  - By K7, Γ± are of that type. **The precise hypotheses and the summability level have not been checked**, because the full text was not retrieved.
  - Status `[LIT — lead, not imported]`.
  - If it applies, the P1-c-5 §3.2/§3.4 expectation (φ± Gevrey and summable, with the parabolic curves of C2 as its sectorial sums) becomes an imported theorem. The level (1/3 in z, as P1-c-5 guessed, or otherwise) must be read from the paper.
- **Independent confirmation of Lemma 5b-1** (`[LIT]`). [LS] §1 states, without proof in that text: "Invariant curves of Briot-Bouquet type of F are convergent when the infinitesimal generator of F is convergent." This is the content of Lemma 5b-1, which was proved in P1-c-5.

## 7. What the literature settles for B-an, and what it does not

**Settled** (C1–C3):
- F has parabolic curves along both Fuchsian directions.
- Along each formal curve Γ±, the orbits asymptotic to Γ± are organized in exactly 3 attracting and 3 repelling one-dimensional parabolic curves, with no open basin asymptotic to Γ±.
- X̂ is ½-Gevrey.

**Not settled.**
- Convergence of φ±, or of X̂.
- Existence of an analytic half-iterate (B-an) or sixth root (B-6).
- Any Stokes or horn-map data.

None of the papers read contains an embeddability or root criterion for this class of germs. Within these sources such a criterion was **not found**.

**Reformulation of the divergence question** (`[HEUR]`; it uses [L12], whose hypotheses are not yet checked).
- If φ± converges, the attracting and repelling parabolic curves of C2 are all pieces of one analytic curve. On every overlap of their sectors they coincide.
- Conversely, if the curves of C2 are the sectorial sums of φ±, they coincide on all overlaps iff φ± converges. The difference of two sectorial sums is then an exponentially small Stokes discrepancy.
- So the divergence question becomes a question about two explicit geometric objects: the gap between an attracting and a repelling parabolic curve on a common sector.

**Consequence for P1-c-5d** (`[HEUR]`; recommendation, needs a decision). A sharper numerical target than coefficient asymptotics to m ≈ 100:
1. Compute the attracting and repelling parabolic curves of C2 for one Γ (Hakim/[LRRS] §5 contraction, or iteration of F and F⁻¹ seeded from the truncated formal curve).
2. Measure their gap on a common sector, as a function of |x|.

A gap behaving like exp(−c/|x|^q) with a stable nonzero prefactor would be a strong `[NUM]` divergence indicator. A gap at working precision would be a strong convergence indicator. Neither would be a proof. The gap is a finite-dimensional, local computation, and is well suited to interval arithmetic.

**Roots and parabolic curves** (`[HEUR]`, not developed).
- An analytic square root K of F tangent to the identity is formally exp(X̂/2). It preserves Γ±, commutes with F, and fixes each attracting direction.
- So K maps each parabolic curve of C2 into itself and acts on it as a half-iterate of F, i.e. a half-translation in a Fatou coordinate.
- B-an therefore forces compatibility conditions between the attracting and repelling curves: a two-dimensional analogue of the horn-map condition. This is the natural setting for P1-c-6.

## 8. Status and next steps

| Item | Status |
|---|---|
| Abate 2001 hypotheses (isolatedness, singular directions, index ∉ ℚ⁺) | checked; C1 imported |
| Abate–Tovena / Vivas Fuchsian classification (P1-b provenance limit) | **closed**: confirmed from the originals |
| Vivas basin region at −½ ± ω/8 | condition false (boundary); no import |
| [LS]/[LRRS] hypotheses for Γ± | checked: k = 3, p = 0, Briot–Bouquet; C2 imported |
| X̂ Gevrey class | ½-Gevrey, imported (C3) |
| Summability of φ± ([L12]) | lead only; full text needed |
| Convergence or divergence of φ± | OPEN |
| B-an, B-6 | OPEN |
| P1-c-5d | not run |

**Proposed next steps** (each needs its own decision):
- **P1-c-2b:** read the [L12] full text (the PI could supply the PDF) to settle its hypotheses and the summability level. This is small.
- **P1-c-5d (redirected):** the parabolic-curve gap computation of §7, on the PI machine, as part of the P2 decision. It would replace or precede the high-order coefficient campaign.
- **P1-c-6:** Écalle–Voronin calibration of the one-variable model, recast through §7 (half-iterates on parabolic curves). Later and bounded.

**Unchanged:** DYAD v6.4.18 adopted; OPEN 20 PARTIAL; B-an and B-6 OPEN. Everything above is SESSION material.

## 9. Reproduction

- **Files:** `dyad_open20_an_p1c2_check.py`, `qw.py`, `fzw.py`, `ext.py`, `logzw.py`, `p1c2_check.json`, `p1c2_perf.json`, `SHA256SUMS.txt`.
- **Command:** `python3 dyad_open20_an_p1c2_check.py`. Expected output: `RESULT: PASS`, with gates K1–K7 true and N1–N4 false.
- **Checker SHA-256:** `63122a81c554b4e25c61231292a422523a4f565260ecb4f14198f912da112d09`.
- **`p1c2_check.json` SHA-256:** `1a89fb9cf4ee4d3facb0554d1ec6f8d80b15e8e24330cc4960d0a09e00bd6966`.
