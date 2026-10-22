# DYAD OPEN 20 / O20-an — P1-b: Lemma S proof record, degenerate characteristic directions, embedding and root-divergence criteria (SESSION v0.1.1)

**Version:** v0.1.1 (supersedes v0.1 `a9edbf53…27c0`; Lemma S correction only, §6) · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Basis.**
- Scope note `DYAD_OPEN20_ANALYTIC_ROOTS_SCOPE_SESSION_v0_1.md` (`5154ca52…a8b0`).
- Its review: `O20-an SCOPE ACCEPTED — P1-b GO`. The review asked for three outputs:
  1. a separate proof record for Lemma S, compared with Baker 1964;
  2. classification of the two degenerate characteristic directions under the original Abate–Tovena definitions;
  3. a hypothesis-level assessment of whether Ribón's work and the later literature give a concrete embedding or root-divergence criterion for DYAD.

**Status.**
- `[SESSION]` record. No new adopted result.
- DYAD v6.4.18 is unchanged; OPEN 20 PARTIAL; B-an and B-6 OPEN.
- No campaign code was written (P2/P3 are separate decisions). N14 is PENDING.

**Check script.** `dyad_open20_an_p1b_check.py` writes `p1b_check.json`.
- 4 gates (D1–D4) and 2 negative controls (K1–K2).
- Exact sympy, under 2 s, run locally.

## 1. Lemma S — proof record

`[THM — SESSION]`. The review accepted the argument. Recorded here as a standalone statement.

### 1.1 Setting

- X̂ = log F is the formal generator of §6.16. It is real and has j²X̂ = 0.
- For s ∈ ℂ, exp(sX̂) is the formal Lie series. Its degree-d coefficients are polynomials in s of degree at most ⌊(d − 1)/2⌋, because L_{X̂} raises the order by at least 2.
- The formal flow identity exp(sX̂)∘exp(tX̂) = exp((s + t)X̂) holds coefficientwise. Both sides are polynomial in (s, t) in each coefficient and agree for all s, t: this is the group law of formal flows.
- Define S_ℂ := {s ∈ ℂ : exp(sX̂) has positive radius of convergence} and S := S_ℂ ∩ ℝ.

### 1.2 Statement

- **(i)** S_ℂ is an additive subgroup of ℂ containing ℤ, and S is an additive subgroup of ℝ containing ℤ.
- **(ii)** B-an ⟺ ½ ∈ S; B-3 ⟺ ⅓ ∈ S; B-6 ⟺ ⅙ ∈ S. Hence B-6 ⟺ B-an ∧ B-3.
- **(iii)** Either S = (1/q)ℤ for a unique integer q ≥ 1, or S is dense in ℝ. If S contains an irrational number, S is dense. The converse is false: S = ℚ is a dense additive subgroup containing ℤ and no irrational number.
  - In the discrete case, B-an ⟺ 2 | q and B-6 ⟺ 6 | q.
- **(iv)** If X̂ converges, then S_ℂ = ℂ.

### 1.3 Proof

- **Convergent maps form a group.** Convergent tangent-to-identity germs of (ℂ², 0) are closed under composition. The inverse of such a germ converges, by the inverse function theorem.
- **Group property of S_ℂ.** If s, t ∈ S_ℂ, then exp(sX̂)∘exp(tX̂) converges and equals exp((s + t)X̂) formally. exp(−sX̂) is the formal inverse of exp(sX̂), so it converges.
- **ℤ ⊂ S.** exp(nX̂) = Fⁿ formally (§6.16) and Fⁿ is analytic.
- **Real part.** S = S_ℂ ∩ ℝ is the intersection of two subgroups of ℂ, hence a subgroup of ℝ.
- **(ii)** follows from the definitions and the group property, using ⅙ = ½ − ⅓, ½ = 3·⅙ and ⅓ = 2·⅙.
- **(iii)** Every additive subgroup of ℝ is either cyclic or dense. If it is cyclic and contains 1, it equals (1/q)ℤ. A subgroup containing 1 and an irrational number is not cyclic, hence dense; a dense subgroup need not contain an irrational (e.g. ℚ).
- **(iv)** The time-s map of a convergent field is analytic for every s ∈ ℂ, on a small enough ball. ∎

### 1.4 Comparison with Baker 1964

The comparison follows the summary of the paper. Baker's internal proof was not reproduced here.

| | Baker (one variable, f(z) = z + …) | DYAD (Lemma S, F a germ of ℂ² after complexification) |
|---|---|---|
| Polynomial dependence of coefficients on s | yes | yes (§1.1) |
| Group property of the convergence set | yes | yes, (i) |
| Trichotomy: ℂ, rank-1 lattice, or rank-2 lattice | **proved**, using one-variable theory | **not available**: S_ℂ could a priori be dense and not all of ℂ |
| Whole plane only for special global forms (Szekeres for entire/rational f, Baker for meromorphic f) | proved for meromorphic f | no analogue found for entire maps of ℂ² (F = T⁶ is entire) |

**Consequence.** Lemma S gives exactly the group-theoretic part of Baker's picture. The closedness and discreteness part, which in one variable forces S_ℂ to be a lattice unless the log converges, is `[OPEN]` for F.

**Recorded obligation P1-c-1:** read Baker's proof (and Szekeres 1958 and Baker 1958, cited through Baker 1964) to see which step is genuinely one-dimensional.

## 2. Degenerate characteristic directions of the complexified F

### 2.1 Definitions used

The definitions are those of Vivas (arXiv:1106.1471, §2), who attributes them to Abate–Tovena, arXiv:0903.3485.

- Write F(z, w) = (z, w) + P_k + …, with P_k = (p_k, q_k).
- [v] is **characteristic** if P_k(v) = λv. It is **degenerate** if λ = 0.
- At [1:0], set u = w/z, p(u) := p_k(1, u) and r(u) := q_k(1, u) − u·p_k(1, u). Let m := ord₀ p and n := ord₀ r.
- The direction is **Fuchsian** if 1 + m = n, **irregular** if 1 + m < n, and **apparent** if 1 + m > n or m = ∞.
- **Index:** Ind = Res_{u=0} p(u)/r(u).

**Provenance limit.** The original Abate–Tovena text, Sections 7–8 (apparent, Fuchsian and irregular singularities; Proposition 8.4, Corollary 8.5), could not be retrieved in full through the tools available here; the text extraction stopped before those sections. The introduction confirms:
- the three types "apparent, Fuchsian (the generic case), irregular";
- the Fuchsian local form z^μ(a₀ + …)·v ∂/∂z − … with a₀, b₀ ≠ 0;
- the residue ρ = b₀/a₀ = Res_{p₀}(∇);
- that degenerate directions are those along which Q vanishes identically.

The classification below therefore uses Vivas's statement of the Abate–Tovena definitions. A line-by-line check against Abate–Tovena §7–8 is obligation **P1-c-2**. The PI could supply the PDF, or the check can be made in a later session.

### 2.2 Computation

`[ALG]`, gates D1–D4.

- **Cubic part.** Complexify W → z and W̄ → w. The cubic part μ|W|²W (pilot gate A5) gives P₃ = (μz²w, μ̄zw²), with μ = −½ − (2√3/3)i.
- **D1.** The characteristic directions are exactly [1:0] and [0:1].
  - For zw ≠ 0 the condition P₃(v) = λv forces μ = μ̄, which is impossible.
  - Both directions are degenerate, since P₃ vanishes on both axes.
- **D2.** At [1:0]:
  - p(u) = μu, so m = 1;
  - r(u) = (μ̄ − μ)u², so n = 2;
  - 1 + m = n, so **[1:0] is Fuchsian** in the sense of §2.1.
- **D3.** By the swap symmetry, **[0:1] is also Fuchsian** (m = 1, n = 2).
- **D4.** Indices:
  - Ind[1:0] = μ/(μ̄ − μ) = −½ + i√3/8;
  - Ind[0:1] = −½ − i√3/8;
  - the sum is −1.
  - The sum agrees with what Abate's index theorem requires (as I recall it, the indices over the exceptional divisor sum to −1). This is a consistency check only, `[HEUR]`.
- **Negative controls.**
  - K1: with real μ, r ≡ 0 and the germ is dicritical. The classification gate fails, as required.
  - K2: exchanging p and r in the residue makes the index gate fail, as required.

### 2.3 Reading

`[HEUR]`; nothing here is used as a premise.

- **Hakim's non-degenerate theory** does not apply: there is no non-degenerate direction.
- **Vivas's basin results for Fuchsian directions** require the index to lie in an explicit region. Whether −½ ± i√3/8 lies in that region has not been checked; this is obligation P1-c-2.
- **Abate's parabolic-curve theorem** requires 0 to be an **isolated** fixed point of the complexified F.
  - At cubic order, P₃ vanishes on both axes. Isolatedness therefore depends on higher-order terms.
  - A resultant computation of the intersection multiplicity was attempted here and abandoned as too slow in sympy.
  - Isolatedness is **not established**; this is obligation P1-c-3.
- The PI's instruction stands: no Écalle–Voronin-type statement is transferred.

## 3. Embedding and root-divergence criteria

`[HEUR]` assessment.

### 3.1 Ribón (2009, Ann. Inst. Fourier 59)

- Ribón shows that formal classes which do not embed exist in (ℂ², 0), and are generic in his affine families.
- **His notion is weaker than ours.** "Formal class embeddable" means that log φ is *formally conjugate* to a convergent field. B-an and B-6 ask whether exp(½X̂) and exp(⅙X̂) themselves converge.
- **Consequences for DYAD:**
  - If F's formal class were *not* embeddable, X̂ could not converge, and Lemma S(iv) would not apply. B-an itself would still not be decided.
  - If F's formal class *is* embeddable, Ribón's obstruction is silent. The question then becomes whether the formal conjugacy, or X̂ itself, diverges.
- **Concrete sub-question, obligation P1-c-4:** is the formal normal form of X̂ (the formal-conjugacy class of a field with cubic part μ|z|²z, μ ∉ ℝ, together with the λ-equivariant lattice term a₀₅z̄⁵) convergent, for example a finite-parameter polynomial or rational field?
- **No direct criterion for DYAD** is given by this paper.

### 3.2 Ribón (2012, J. Differential Equations 253)

Embedding of smooth and formal *hyperbolic* diffeomorphisms through the Jordan–Chevalley decomposition. It does not apply: F is unipotent.

### 3.3 Klimeš–Stolovitch (arXiv:2204.09449)

Reversible parabolic diffeomorphisms of (ℂ², 0) with a holomorphic **Morse first integral**. Restricted to the components of the zero level of the first integral, the classification recovers the one-variable Birkhoff–Écalle–Voronin modulus.

It does not apply directly. F has a strict radial contraction (Re μ < 0, DYAD-THM-PRIM-CTR), so it has no first integral at all:
- every real orbit tends to 0, so a first integral continuous at 0 is constant on the real plane;
- a holomorphic function constant on the totally real plane ℝ² ⊂ ℂ² is constant.

The *mechanism* (restriction to an invariant curve recovers one-variable moduli) is however the template for §3.4.

### 3.4 Candidate negative criterion through invariant curves

`[THM — SESSION candidate]` for (a) and (b); `[OPEN]` for (c).

- **(a) Formal tangency.** Let Γ be a formal curve at 0, with ideal I ⊂ ℂ[[z, w]], that is F-invariant: F*(I) = I. Then X̂ is tangent to Γ: X̂(I) ⊂ I.
  - *Sketch.* F* is a unipotent automorphism of ℂ[[z, w]]. Its logarithm Σ_{k≥1} (−1)^{k+1}(F* − I)^k/k converges in the Krull topology and is the derivation X̂. Each term maps I into I, and I is closed.
- **(b) Restriction.** If Γ is moreover *convergent* and smooth, with parameter t, then F|_Γ is a one-variable germ t ↦ t + … and exp(sX̂)|_Γ = exp(s·X̂|_Γ) formally.
  - If F^{1/2} converges, its restriction is a convergent half-iterate of F|_Γ, so ½ ∈ 𝔅(F|_Γ) in Baker's notation.
  - Likewise B-6 ⇒ ⅙ ∈ 𝔅(F|_Γ).
- **(c) Criterion.** Suppose F has a convergent smooth invariant curve Γ through 0 on which F|_Γ is parabolic and non-trivial, and suppose ½ ∉ 𝔅(F|_Γ) (decidable in one variable through Écalle–Voronin moduli or Baker-type arguments). Then **B-an is negative**. The same holds for B-6 with ⅙.
  - Nothing here transfers one-variable theory to F itself. It is applied only to the one-variable germ F|_Γ.

**Obstacles, all `[OPEN]`:**
- **No real invariant curve.** F has no *real*-analytic invariant curve through 0. Real orbits spiral, because the angle per block is −τQ + …, so the angle diverges logarithmically while Q → 0. Γ must therefore be a genuinely complex curve.
- **Existence and convergence of Γ.** Formal invariant curves tangent to the Fuchsian directions [1:0] and [0:1] are natural candidates. Their existence and convergence is obligation P1-c-5. For formal invariant curves and parabolic curves asymptotic to them, see López-Hernanz–Raissy–Ribón–Sanz, arXiv:1411.2945 (not yet read).
- **Restricted dynamics.** Even if Γ converges, F|_Γ may be the identity or of high parabolic order. Its one-variable modulus would then have to be computed.

### 3.5 Positive side

No concrete sufficient criterion for convergence of F^{1/2} or F^{1/6} was found.

The adopted equivalent formulations remain the only handles:
- an analytic involution commuting with T, which must equal R₀;
- an analytic J;
- an exactly λ-equivariant analytic chart.

## 4. Effect on the P2 campaign design

The review asked whether P1-b changes what P2 must track.

1. **Root and log reported separately.** Already required by the review; confirmed. Lemma S shows that fast growth of X̂ says nothing about ½ ∈ S.
2. **Invariant-curve channel.** Add to P2 the computation of formal invariant curves tangent to [1:0] and [0:1] (coefficients of w = φ(z) solving the invariance equation), with growth diagnostics for φ. If φ appears convergent, compute the one-variable germ F|_Γ and its Écalle–Voronin data numerically, as a `[NUM]` lead for criterion §3.4(c).
3. **Formal normal form of X̂** (obligation P1-c-4). Compute the low-degree formal normal form of X̂, to see whether the formal class is plausibly embeddable.
4. **Unchanged from the review:**
   - a separate exact chain and ball chain;
   - norms computed with outward-rounded balls;
   - automatic stop on insufficient precision;
   - C5 must demonstrate the separation of a convergent root from a divergent log;
   - timings written to a separate performance file, so that the result JSON is byte-deterministic.

## 5. Obligations carried

| ID | Item |
|---|---|
| P1-c-1 | Read Baker (1964), Szekeres and Baker (1958): which step of the lattice trichotomy is one-dimensional |
| P1-c-2 | Abate–Tovena §7–8 original definitions; Vivas's Fuchsian basin region at the indices −½ ± i√3/8 |
| P1-c-3 | Isolatedness of 0 in Fix of the complexified F (needed for Abate's parabolic-curve theorem) |
| P1-c-4 | Formal normal form of X̂ / embeddability of the formal class in Ribón's sense |
| P1-c-5 | Formal invariant curves tangent to [1:0], [0:1]: existence and convergence (with López-Hernanz–Raissy–Ribón–Sanz) |
| — | Lemma (a)–(b) of §3.4, to be written out in full before any use |

**Status:** DYAD v6.4.18 adopted; OPEN 20 PARTIAL; B-an and B-6 OPEN. Lemma S, §2 and §3 are SESSION material only. N14 PENDING.

## Sources

- Baker 1964: https://core-cms.cambridgecore.org/core/services/aop-cambridge-core/content/view/B0EE7D3E5945913D19E95C8530106421/S144678870002334Xa.pdf/fractional-iteration-near-a-fixpoint-of-multiplier-1.pdf
- Ribón 2009: https://arxiv.org/pdf/0902.2985
- Ribón 2012 (JDE 253): https://arxiv.org/abs/1107.3601
- Vivas, degenerate characteristic directions: https://arxiv.org/pdf/1106.1471
- Abate–Tovena, Poincaré–Bendixson theorems for meromorphic connections and homogeneous vector fields: https://arxiv.org/abs/0903.3485
- Klimeš–Stolovitch, reversible parabolic diffeomorphisms of (ℂ², 0): https://arxiv.org/abs/2204.09449
- López-Hernanz–Raissy–Ribón–Sanz, parabolic curves asymptotic to formal invariant curves (to read): https://arxiv.org/abs/1411.2945

## 6. Changes v0.1 → v0.1.1 (review of 20 Oct 2026: `P1-b PARTIAL ACCEPT — LEMMA S CORRECTION REQUIRED`)

1. **Lemma S(iii) corrected.** v0.1 stated "S is dense iff it contains an irrational number". This is **false**: ℚ is dense in ℝ, contains ℤ and has no irrational element.
   - The correct dichotomy is: S = (1/q)ℤ for some q ∈ ℕ, or S is dense in ℝ.
   - Only one implication holds: an irrational element in S ⇒ S is dense.
   - The group property (i), statement (ii) (B-6 ⟺ B-an ∧ B-3) and (iv) are unaffected.
2. **Unchanged:**
   - §2 (D1–D4, Fuchsian under Vivas's statement, indices −½ ± i√3/8): accepted.
   - §3.4: accepted as a **conditional** negative criterion. It is usable only once a convergent, smooth, F-invariant complex curve Γ is shown to exist. Fuchsian type alone does not provide one.
   - The check script and its results.
3. **Next priority (review):** P1-c-3 (isolatedness of 0 in Fix of the complexified F) and P1-c-5 (existence and convergence of invariant curves). P2 is a separate decision.
