# DYAD OPEN 20 / O20-∞ — P1-b literature follow-up and P2 (orbit bounds and inverse-iteration domain)

**Version:** v0.1 · **Date:** 19 October 2026 · **Author:** Dyadic DSN owner (Claude)
**Status:** `[SESSION]` record.
- §1 is a literature status.
- §2–§3 give a **proof proposal** for P2-a and P2-b, for review. It is not yet a reviewed proof.
- No existence result is claimed. DYAD v6.4.17 is unchanged.

**Basis:** review of the scope note v0.1 (`3a06222a…c0be`): `SCOPE REVIEW ACCEPTED — PROOF NOT YET ESTABLISHED`. It approves P1-b and asks for P2 orbit bounds **together with** inverse-iteration domain control (new P2-b) before P3-a.

**Statuses unchanged** (v6.4.17): OPEN 20 PARTIAL; B-an, B-6 and B-∞ existence OPEN; no physical, G2 or network-exchange claim.

## 1. P1-b — literature follow-up

| Lead | What could be inspected | Status |
|---|---|---|
| Chaperon 1986, *Géométrie différentielle et singularités de systèmes dynamiques*, Astérisque 138–139 | Bibliographic record and reference list only. The list includes Sternberg 1957, Chaperon 1979/1980 (C^∞ linearization of actions), Dumortier–Roussarie 1980 and Takens 1971 (*Partially hyperbolic fixed points*). | **Contents not accessible here.** The reference list points to hyperbolic and partially hyperbolic theory. No statement for germs tangent to the identity was seen. |
| Roussarie 1975, Astérisque 30 | Bibliographic record only | **Not accessible here.** Concerns vector fields. |
| Belitskii (smooth equivalence of germs) | No item matching the needed statement was located | **Not located.** |
| Thilliez 2004 (arXiv math/0406259) | Abstract and theorem: infinite determinacy of *functions* on closed sets under Łojasiewicz-type conditions | **Not applicable** (functions, not maps). |

**P1 status after P1-b.**
- No theorem that applies directly to F has been located **in the sources accessible here**.
- Per the reviewer, this is recorded as "not found", **not** as "does not exist".
- The Chaperon and Roussarie volumes remain open for anyone with library access (PI, reviewer).
- O20-∞ continues on the self-contained route.

## 2. P2-a — two-sided orbit decay (proposal)

**Setting** (raw frame W, |·| Euclidean, Q = |W|²):
- F = id + G₃ + R_F with G₃ = μ|W|²W; G = exp(X_∞), Borel, with the same ∞-jet, so G = id + G₃ + R_G.
- On a ball B_ρ: |R_F(W)|, |R_G(W)| ≤ C₄|W|⁴, and |F − G|(W) ≤ c_N|W|^N for every N (flatness).
- Constants for G are **qualitative**: X_∞ is any Borel realization. ρ is taken small enough for all the statements below. B-∞ existence is a qualitative claim, so no explicit radius is needed.

**Claim P2-a.** There are ρ > 0 and constants 0 < a < b such that, for H ∈ {F, G} and 0 < Q₀ = |W₀|² ≤ ρ²:

  1/Q₀ + a·m ≤ 1/Q(H^m W₀) ≤ 1/Q₀ + b·m,  for all m ≥ 0,

and B_ρ is forward-invariant under H.

**Sketch.** Q(H(W)) = Q − Q² + O(Q^{5/2}); the half-power term is P₅ for F and identical for G. So Q − (3/2)Q² ≤ Q(HW) ≤ Q − ½Q² for small Q. For F this is exactly DYAD-THM-PRIM-CTR (Q ≤ 1/400); for G it is the same majorant argument on a smaller ball. Then 1/Q′ ≥ 1/Q + ½ and 1/Q′ ≤ 1/Q + 3/2 + O(Q). Sum over the orbit.

**Consequence.** Σ_{j<m} Q(H^jW₀) ≤ (1/a)·log(1 + a·m·Q₀) + const.

## 3. P2-b — inverse-iteration domain (the reviewer's obligation)

**Claim P2-b.** There is ρ₁ ≤ ρ such that, for every x ∈ B_{ρ₁} and every n ≥ 0:
- (i) F^n(x) ∈ G^n(B_ρ), so Φ_n(x) := G^{−n}(F^n(x)) is defined;
- (ii) the segment [F(F^n x), G(F^n x)] lies in G^{n+1}(B_ρ), so G^{−(n+1)} is defined along it;
- (iii) |Φ_n(x) − x| ≤ Σ_{k<n} |Φ_{k+1}(x) − Φ_k(x)|, and this sum converges, with |Φ_∞(x) − x| = O(|x|^M) for every M.

### Ingredients

**(D1) Polynomial expansion of inverse iterates.** On B_ρ:
- ‖DG(W)⁻¹‖ ≤ 1 + c|W|², because DG = I + DG₃ + O(|W|³) and ‖DG₃(W)‖ ≤ 3|μ||W|².
- For p with forward G-orbit in B_ρ, the chain rule and P2-a give ‖(DG^m(p))⁻¹‖ ≤ Π_{j<m}(1 + c·Q(G^jp)) ≤ C·(1 + m·Q(p))^{c/a}.
- This is polynomial in m: the crude Euclidean bound is enough, and no adapted norm is needed.

**(D2) Inner radius of iterated balls.** Suppose the forward orbit of B(p, s) stays in B_ρ (P2-a) and G is injective on B_ρ. Then

  G^m(B(p, s)) ⊇ B(G^m(p), s/Λ_m(p)),  with Λ_m(p) = sup_{B(p,s)} ‖(DG^m)⁻¹‖.

This is the standard inverse-function inner-radius estimate, applied to the injective local diffeomorphism G^m. The precise version to be written out: invariance of domain plus a Lipschitz bound of G^{−m} on G^m(B(p,s)).

**(D3) Flat step.** |F(y) − G(y)| ≤ c_N|y|^N, with |y| = |F^nx| ≤ (1/Q₀ + a·n)^{−1/2} by P2-a.

### Induction (proposal)

Set p_n := Φ_n(x). Then F^n x = G^n(p_n) and p_n ∈ B(x, s₀), with s₀ = |x|/4 held fixed.

1. **Base.** p₀ = x.
2. **Step.**
   - F^{n+1}x = F(y_n), with y_n = G^n(p_n).
   - G(y_n) = G^{n+1}(p_n), and |F(y_n) − G(y_n)| ≤ c_N|y_n|^N =: δ_n.
   - By (D2), G^{n+1}(B(p_n, s₀)) contains B(G^{n+1}p_n, s₀/Λ_{n+1}). Here Λ_{n+1} ≤ C(1 + n·Q₀)^{c/a} is polynomial, while δ_n ~ (Q₀⁻¹ + a·n)^{−N/2} decays faster than any polynomial.
   - So F(y_n) and the whole segment [G(y_n), F(y_n)] lie in G^{n+1}(B(p_n, s₀)). This gives (ii).
   - Then p_{n+1} = G^{−(n+1)}(F(y_n)) satisfies |p_{n+1} − p_n| ≤ Λ_{n+1}·δ_n.
3. **Summation.** Σ_n Λ_{n+1}δ_n ≤ C_N Σ_n (1 + nQ₀)^{c/a}(Q₀⁻¹ + a·n)^{−N/2} = O(Q₀^{(N−2)/2 − c/a}) for N large. For |x| small this is below s₀/2, so the induction never leaves B(x, s₀) ⊂ B_ρ. This gives (i) and (iii).

**What the induction shows.** The reviewer's condition holds with U = B(x, s₀), whose forward G-orbit stays in B_ρ, and U′ = B_ρ: F^n(x) ∈ G^n(U) and G^{−n}(F^n x) ∈ U. The early-time flat differences need no relative-error control, because each telescoping step is pulled back by G^{−(n+1)} from the **current** point, not transported forward.

### Still to be written before P2-b counts as proved

- (D2) with full detail: injectivity of G^m on the ball, which follows from injectivity of G on B_ρ, and the Lipschitz constant of G^{−m} on the image.
- Uniformity in x for |x| ≤ ρ₁. The exponent c/a and the constants must not depend on x.
- The pointwise bound (iii) for every M.

## 4. What P3 then needs (unchanged order)

| Step | Obligation |
|---|---|
| P3-a | C^k version of (D1): ‖D^k(G^{−m})‖ ≤ C_k(1 + mQ₀)^{e_k} on the controlled domain (Faà di Bruno with the D1 product), together with ‖D^k(F^n)‖ polynomial |
| P3-b | ‖F − G‖_{C^k(B_r)} ≤ c_{N,k}r^N |
| P3-c | C^k convergence of Φ_n on a fixed neighbourhood for every k, flat contact of Φ_∞ with the identity, and Φ_∞∘F = G∘Φ_∞. Pointwise convergence (§3) is **not** sufficient (reviewer) |
| P4 | K = Φ⁻¹exp(X_∞/6)Φ, J = TK⁻¹ with JT = TJ by F3, F^{1/2}, R |

**Note for P3-c.** Φ_∞ is a local diffeomorphism because DΦ_∞(0) = I and the C¹ convergence is uniform.

## 5. Criteria (unchanged from v0.1)

- **Positive:** L-FC proved, giving Q∞ (F = exp(X), X C^∞).
- **Negative:** an obstruction to every C^∞ root. Failure of this construction is not a negative result.
- **Partial:** labelled as such.

## Sources

- M. Chaperon, [Géométrie différentielle et singularités de systèmes dynamiques](https://numdam.org/item/AST_1986__138-139__1_0/), Astérisque 138–139 (1986); bibliographic record and references only.
- R. Roussarie, [Modèles locaux de champs et de formes](https://www.numdam.org/item/AST_1975__30__1_0), Astérisque 30 (1975); not accessible here.
- V. Thilliez, [Infinite determinacy on a closed set for smooth germs with non-isolated singularities](https://www.arxiv.org/pdf/math/0406259) (2004).
- F. Takens, [Normal forms for certain singularities of vectorfields](https://www.numdam.org/item/AIF_1973__23_2_163_0) (1973); used in v0.1.
