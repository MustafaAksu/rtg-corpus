# DYAD OPEN 20 (analytic branch) — stage 3c-a: proof record (W7)

**Date:** 12 November 2026. **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION). It writes out the arguments on which the certificate script of stage 3c-a relies. It claims no result about the jump, about divergence, or about B-an and B-6. Nothing here has been reviewed yet.
**Authority and basis:** as in `records/dyad/DYAD_OPEN20_AN_STAGE3C_A_PLAN.md` (PI decision of 11 November 2026; design `DYAD_OPEN20_AN_STAGE3B_DESIGN.md` r2). Stage 3c-b is not authorized.
**Governing edition:** DYAD v6.4.24. OPEN 20 B-an and B-6 are ACTIVE.

## 0. What this record contains

| § | Content | Kind | State |
|---|---|---|---|
| 1 | Notation | — | — |
| 2 | Structural facts S1–S5 | exact algebra (script) and one argument (S4) | written |
| 3 | Remainder in d: Taylor model on arcs, maximum principle | proof | written |
| 4 | Local inverse lemma; one analytic inverse branch G | proof, with three computed facts | written |
| 5 | Tube lemma: the Rouché step for F and for G, with the zero count | proof | written; the seed (Q) is not treated here |
| 6 | Zone II: from the piece statuses to the hypotheses | proof | written |
| 7 | Zone I: the reduction | proof | written |
| 8 | The common arc | proof | written |
| 9 | The legs: validity of the forward–backward updates | proof | written |
| 10 | Rounding | argument | written |
| 11 | What is not proved here | list | — |

Every statement of §§3–9 is conditional on the computed facts it names. Those facts come from development runs. A proof in this record does not turn a development run into a certificate.

## 1. Notation

- T(ρ, η) = (ρ − sin η, η + e^ρ − 1 − sin η), F = T⁶; z = ρ + ωη, w = ρ + ω̄η, ω = e^{2πi/3}.
- φ_N(x) = Σ_{k=2}^{N} a_k x^k, N = 40: the truncation of the pilot branch; a₂ the pilot root, a_k from the exact recursion.
- Input point (z, w) = (x, φ_N(x) + x²d). Image (Z, W) = F(z, w). Lifted map F̂(x, d) = (x′, d′) with x′ = Z and d′ = Φ(x, d) = (W − φ_N(Z))/Z². ξ = cx.
- d-jets at d = 0: Z = Z₀ + Z₁d + Z₂d² + …, W likewise. Order-zero series G0, Q4, P4, M3, S2, ET44 as in the library (`order_zero_from_jets`). g = x³G0, b₀(x) = x(1 + g(x)) = Z₀.
- One-step quantities: Φ(x, d) = E + μ₀d + c₂d² + r(x, d); Z(x, d) = b₀(x) + x⁴Q4·d + x⁴P4·d² + r_Z(x, d).
- τ, the functionals first and second, the walls s_j, c_j, the domains D_j, the chart sectors Ω_j, the guard cores Ω_j⁻ and the tube radius R_j: design §3. Side j = 0 is F on D₀; side j = 1 is the inverse branch G on D₁.

## 2. Structural facts

**S5 (which contains S1, S2, S3).** With weights (1, 2) for (z, w):
- F_z − z has only monomials z^p w^q with p + 2q ≥ 4;
- F_w − w has only monomials z^p w^q with p + 2q ≥ 5.

*Derivation.* `evidence/dyad/scripts/dyad_open20_an_stage3c_w7_structure.py`, exact arithmetic only. The Taylor polynomial of T⁶ at 0 is computed through total degree 5 with rational coefficients (the series of sin and exp are truncated at degree 5; a term of degree above 5 cannot contribute to a coefficient of degree at most 5, because T has no constant term). The linear change to (z, w) preserves total degree, and every monomial with p + 2q ≤ 5 has total degree at most 5. The result, over Q(√3, i):

- F_z = z + μz²w + c₄₀z⁴ + (terms z³w, z⁵ and higher weighted order), μ = −1/2 − (2√3/3)i, c₄₀ = −1/16 + (7√3/144)i;
- F_w = w + μ̄zw² + d₃₁z³w + cc·z⁵ + (higher weighted order), d₃₁ = 1/3 − (√3/9)i, cc = −61/2160 + (43√3/6480)i.

These are the stage-1 constants used by the library. F has no terms of degree 2. F_z has no monomial w².
- A control shows what the statement depends on: if the linear part of T is changed so that it no longer has order 6, S5 fails. If only the quadratic part of T is changed, S5 still holds and the constants change.

**Consequences used.** At the input point every monomial z^p w^q becomes x^{p+2q}(û(x) + d)^q with û = φ_N/x² a polynomial. Hence:
- (Z − x)/x⁴ and (W − φ_N(x) − x²d)/x⁵ are entire functions of (x, d); in particular Z₀ − x = O(x⁴) (S1), Z₁ = O(x⁴) (S2), and all d-jets of Z − x are O(x⁴);
- where Z/x ≠ 0: Φ − d = [x⁵B − (φ_N(x + x⁴A) − φ_N(x)) − d·x²(2x³A + x⁶A²)]/(x²(1 + x³A)²) with A = (Z − x)/x⁴, B = (W − φ_N(x) − x²d)/x⁵. The numerator is x⁵ times an entire function. So (Φ − d)/x³ is analytic in (x, d) where 1 + x³A ≠ 0. This gives S3 and the regularity of P4 and of the series S2.

**S4 (the defect is O(x⁴⁴)).** E(x) = Φ(x, 0) = (W₀ − φ_N(Z₀))/Z₀². For the exact coefficients a_k the numerator W₀ − φ_N(Z₀) has no terms below x⁴⁴:
- its coefficient of order k + 3 is affine in a_k and does not involve a_j with j > k (design P1-c; it is the statement that the linear part of the homological equation at order k is ℓ(k* − k)a_k);
- a_k is defined as the solution of "coefficient of order k + 3 equals 0", for k = 3, …, 40, and a₂ as the pilot root of the quadratic at order 5;
- the orders 2, 3, 4 vanish by S5.
- The series engine works with balls that contain the exact a_k. The coefficients of orders below 44 come out as balls that contain 0. They are *set* to 0 on the strength of the argument above; the containment is a consistency check.
- *Not re-derived in this record:* the triangular form of the recursion (P1-c). It is the content of the stage-1 and stage-2 records; W1 checks it numerically (defect zero through x⁴³ with radii below 10⁻²⁷⁰, and a control that breaks it).

**Not assumed.** The identity M3(0) = (2 + α)G0(0) is used in zone I only through a ball of radius below 10⁻⁴⁰ (§7).

## 3. The remainder in d

**Lemma 3.1 (one step of T on a Taylor model).** Let e = e₀ + δ. Then sin e = sin e₀ + cos e₀·δ − ½ sin e₀·δ² + R with |R| ≤ cosh(|Im e₀| + |δ|)|δ|³/6, and e^{r₀+δ} = e^{r₀}(1 + δ + δ²/2 + R′) with |R′| ≤ e^{|δ|}|δ|³/6.
*Proof.* Taylor's formula with integral remainder for t ↦ sin(e₀ + tδ) on [0, 1]; the third derivative is −cos(e₀ + tδ)δ³ and |cos ζ| ≤ cosh(Im ζ). For the exponential, Σ_{k≥3}|δ|^k/k! ≤ e^{|δ|}|δ|³/6. ∎

With δ = e₁d + e₂d² + (remainder of modulus ≤ B) and |d| ≤ ρ: δ² − e₁²d² is bounded term by term by 2|e₁||e₂|ρ³ + |e₂|²ρ⁴ + 2(|e₁|ρ + |e₂|ρ²)B + B². This is `_tm_step_bound`. Six steps give bounds B_Z, B_W for the remainders of Z and W beyond d². The same bookkeeping carries them through φ_N (third derivative bounded on the ball of Z by a Taylor shift), through 1/Z² = Z₀⁻²(1 − 2q + 3q² + …) with the tail Σ_{k≥3}(k+1)θ^k = θ³(4 − 3θ)/(1 − θ)², and through one product. Result: a bound B_Φ of |Φ − E − μ₀d − c₂d²| for x on a ball and |d| ≤ ρ.

**Lemma 3.2 (cover of a circle).** The balls of `_arcs` cover the circle |x| = X: the centre of ball i is the midpoint of arc i rounded to working precision, and the radius 1.0001·Xπ/n exceeds the half-length Xπ/n of the arc (which bounds the chord) by 10⁻⁴Xπ/n, far above the rounding of the centre. ∎

**Lemma 3.3 (maximum principle on a polydisc).** If f is continuous on P = {|x| ≤ X, |d| ≤ ρ} and analytic inside, then sup_P |f| is attained on the torus |x| = X, |d| = ρ. *Proof.* The one-variable principle in x for fixed d, then in d for fixed x on the circle. ∎

**Proposition 3.4.** Suppose (i) S5; (ii) θ := sup over the torus of |Z/x − 1| < 1; (iii) B_Φ and B_Z are bounds as above on every ball of the cover, with suprema B̄_Φ, B̄_Z. Put M₃ = B̄_Φ/(X³ρ³), M_Z = B̄_Z/(X⁴ρ³). Then for |x| ≤ X, |d| ≤ ρ:
|Φ(x, d) − E − μ₀d − c₂d²| ≤ M₃|x|³|d|³ and |Z(x, d) − Z₀ − Z₁d − Z₂d²| ≤ M_Z|x|⁴|d|³.
*Proof.* (Z − x)/x is entire and bounded by θ < 1 on the torus, hence on P; so Z/x ≠ 0 on P and Φ is analytic near P away from x = 0. By S5, Φ − d = x³A₃(x, d) with A₃ analytic on a neighbourhood of P. E, μ₀ − 1, c₂ are the d-jets of x³A₃, so (Φ − E − μ₀d − c₂d²)/(x³d³) is analytic on a neighbourhood of P. On the torus its modulus is at most B̄_Φ/(X³ρ³). Lemma 3.3 gives the first inequality. The second is the same with (Z − Z₀ − Z₁d − Z₂d²)/(x⁴d³), entire by S5. ∎

Computed values (W2b): X = 0.90: M₃ = 109.4, M_Z = 65.4, θ = 0.130; X = 1.03: M₃ = 680.9, M_Z = 117.4, θ = 0.218; ρ = 0.02.

**Cauchy tails of the series.** A series f = Σf_kx^k with sup_{|x|=X_c}|x^p f| ≤ S has |f_k| ≤ S/X_c^{k+p}. The pieces of each order-zero series are entire (S5), are bounded separately on the cover of the circle, and their bounds are added; this needs no cancellation. The tail beyond degree D on |x| ≤ r is then at most M t^{D+1}/(1 − t), t = r/X_c.

## 4. The inverse branch G

### 4.1 Local inverse lemma

Let B = {|x − c| ≤ r}, ρ ≤ 0.02, and a target set B′ × {|d′| ≤ R′}, B′ = {|x′ − c′| ≤ r′}. On B × {|d| ≤ ρ} write x′ = b₀(x) + β(x, d), d′ = E + μ₀d + ν(x, d), with |β| ≤ |x|⁴(|Q4|ρ + |P4|ρ² + M_Zρ³) and |ν| ≤ |c₂|ρ² + M₃|x|³ρ³ (Proposition 3.4).
- (i) inf_B|μ₀|·ρ > R′ + sup_B|E| + sup|ν|;
- (ii) r(1 − L) > |b₀(c) − c′| + r′ + sup|β|, L = sup_B|b₀′ − 1|.

**Lemma 4.1.** If (i) and (ii) hold, every (x′, d′) of the target set has exactly one preimage under F̂ in S = {|x − c| < r} × {|d| < ρ}.
*Proof.* Fix the target. For x ∈ B, by (i) |μ₀(x)d| > |d′ − E(x) − ν(x, d)| on |d| = ρ, so Rouché (against μ₀d) gives exactly one d = δ(x) with |δ(x)| < ρ and Φ(x, δ(x)) = d′; it is simple, so δ is analytic on a neighbourhood of B. A point (x, d) of B × {|d| < ρ} is a preimage if and only if d = δ(x) and h(x) := b₀(x) + β(x, δ(x)) − x′ = 0. On |x − c| = r: |h(x) − (x − c)| ≤ |b₀(x) − x − (b₀(c) − c)| + |b₀(c) − c′| + |c′ − x′| + |β| ≤ Lr + |b₀(c) − c′| + r′ + sup|β| < r by (ii); the first term uses that b₀ − id has Lipschitz constant L on the convex set B. By Rouché h has exactly one zero in the open disc. ∎

Remarks. (a) The inequalities are strict, so they hold for slightly larger r′ and R′: the unique preimage exists for targets in an open set U ⊃ B′ × {|d′| ≤ R′}. (b) The map p′ ↦ (its preimage in S) is continuous on U: a limit of preimages is a preimage in the closure of S, and none lies on the boundary of S (the Rouché inequalities are strict there). (c) F̂ is injective on the open set S ∩ F̂⁻¹(U), so it is biholomorphic onto its image (an injective holomorphic map between domains of the same dimension is open with holomorphic inverse). Hence the local inverse is holomorphic on U. (d) Dropping β: every x′ ∈ B′ has exactly one preimage under b₀ in the open disc of B.

### 4.2 Three computed facts

`evidence/dyad/scripts/dyad_open20_an_stage3c_w7_branch.py` (development run; the numbers are in the plan record, §5, W7).

- **INJ.** On the sector S₁ = {|ξ| ≤ 0.47, 0.03π ≤ arg ξ ≤ 0.50π} (as a set of x = ξ/c): sup|b₀′ − 1| < 1. S₁ is a circular sector of opening 0.47π < π, so it is convex. Hence |b₀(u) − b₀(v)| ≥ (1 − sup|b₀′ − 1|)|u − v| on S₁: **b₀ is injective on S₁**.
- **SRC.** For every pass piece i of the zone-II cover of Ω₁ (the cover of W3): the source disc B_i of the lemma lies in S₁, and sup_{B_i}|E| is below the fibre radius R′_i of the piece's target set.
- **SRC1.** For every target x′ of D₁ with |ξ′| ≤ 0.05: the source disc D(x′, 2|x′|⁴ sup|G0|) of the zone-I lemma (§7) lies in S₁, and |E| on it is below R₁(x′).

### 4.3 One branch

Let 𝒯₁ = {(x′, d′): x′ ∈ D₁, |d′| ≤ R₁(x′)} be the closed tube. For p′ ∈ 𝒯₁ call a set *admissible* if it is the source set S_i of a pass piece whose target disc contains x′, or the zone-I source set N(x′) = {|x − x′| < 2|x′|⁴ sup|G0|} × {|d| < 2R₁(x′)} when |ξ′| ≤ 0.05. By W3, W4 and the seam, every p′ ∈ 𝒯₁ has at least one admissible set, and Lemma 4.1 gives exactly one preimage in each (the fibre radius of a piece's target set is an upper bound of R₁ on the piece).

**Proposition 4.2.** For p′ ∈ 𝒯₁ the preimages in all admissible sets coincide. The common value G(p′) defines a map that is holomorphic on a neighbourhood of 𝒯₁, satisfies F̂∘G = id, and for which d′ ↦ G(x′, d′) is injective on each fibre.
*Proof.*
1. *Reference point.* Let x′ ∈ D₁ and let 𝒜, 𝒜′ be admissible for the fibre over x′, with base discs A, A′. By Remark (d) there are x₀ ∈ A, x₀′ ∈ A′ with b₀(x₀) = x′ = b₀(x₀′). Both discs lie in S₁ (SRC, SRC1), and b₀ is injective on S₁ (INJ). So x₀ = x₀′. The point q = (x₀, 0) lies in 𝒜 ∩ 𝒜′, and F̂(q) = (x′, E(x₀)) =: p₀′. *Claim:* |E(x₀)| < R₁(x′).
   - For a piece i: the pass of (B) in forward form is the inequality |μ₀| + |E|/RS_lo + |c₂|RS_hi + M₃|x|³RS_hi² < ratio_lo on all of B_i, between numbers of the piece: R_lo is a lower bound of R₁ at the points of the piece that lie in D₁, RS_lo = R_lo/ratio_hi, and ratio_lo ≤ ratio_hi. Hence sup_{B_i}|E| < RS_lo·ratio_lo ≤ R_lo ≤ R₁(x′). Only x₀ ∈ B_i and x′ ∈ D₁ are used. The option `--strict-e` of the branch script checks sup_{B_i}|E| < R_lo directly (W8).
   - The check SRC alone (sup_{B_i}|E| below the fibre radius R′_i of the target set, an *upper* bound of R₁) does not give the claim (review `5874133624`).
   - For zone I: SRC1.
   So p₀′ lies in the fibre disc, and both local inverses take the value q at p₀′.
2. *Propagation along the fibre.* Let W = {x′} × {|d′| ≤ R₁(x′)}, a disc. Both local inverses are continuous on W (Remark (b)). The set where they agree is closed in W. It is open in W: if they agree at p₁′ with value q₁, then q₁ lies in the open set 𝒜 ∩ 𝒜′; for p″ ∈ W near p₁′ the value of the second inverse is near q₁, hence in 𝒜, and it is a preimage of p″, hence equal to the value of the first. The set contains p₀′ and W is connected. So they agree on W.
3. *Holomorphy.* Near a point of 𝒯₁ with |ξ′| > 0.05, G equals the local inverse of one piece on the open set U of Remark (a). Near a point with |ξ′| ≤ 0.05, G equals the zone-I inverse; it is continuous there (the set N(x′) moves continuously with x′, and the zone-I conditions are strict, so the argument of Remark (b) applies with a slightly larger set), and a continuous right inverse of F̂ maps a small open set injectively and openly, so Remark (c) applies.
4. *Injectivity on a fibre.* G is a right inverse of F̂. ∎

**The branch on the leg.** In the first round of `leg_G` the lemma is called for a target set over the disc X_k. For Proposition 4.2 to identify its preimage with G(p_k), step 1 needs the reference point (x_k, E(x₀)) inside the target set; this holds if the lemma is called for the whole a-priori fibre over X_k (`full_fibre=True`). The W6 development run called it for the current disc D_k. **This is a correction to carry into W8:** the certificate run must use `full_fibre=True`. (The base discs of the leg lie in the guard core of Ω₁, which is inside S₁; that is checked by the gate LEGG.)

## 5. The tube lemma: the Rouché step

The induction over the families D_j(c) and the seed (Q) are as in the design (§4 there). Written here: the step, in the form in which the script checks its hypotheses.

**Side F (j = 0).** Hypotheses on D₀, for every x ∈ D₀ and every |d| ≤ R₀(x), with (x′, d′) = F̂(x, d):
- (G) D₀ ⊂ Ω₀⁻; (A1) first(x′) > 1 and second(x′) ≥ second(x) + σ; (A2) |x′/x − 1| ≤ κ;
- (B) inf|μ₀|·R₀(x) − |E| − |c₂|R₀² − M₃|x|³R₀³ > sup_{|d|≤R₀(x)} R₀(x′).

Let δ be analytic on D₀(c) with |δ| ≤ R₀ there, and x ∈ D₀(c − σ). For |d| ≤ R₀(x) put Ψ₀(d) = Φ(x, d) and Ψ(d) = Φ(x, d) − δ(x′(d)); x′(d) ∈ D₀(c) by (G), (A1), (A2) (design §4: the step stays in the chart sector). On |d| = R₀(x): |Ψ₀| ≥ inf|μ₀|R₀ − |E| − |c₂|R₀² − M₃|x|³R₀³ > sup R₀(x′) ≥ |δ(x′(d))| = |Ψ − Ψ₀|. So Ψ and Ψ₀ have the same number of zeros in the disc. Ψ₀ has exactly one: on the circle |Φ − μ₀d| ≤ |E| + |c₂|R₀² + M₃|x|³R₀³ < |μ₀|R₀ by (B), so Rouché against μ₀d applies. The zero of Ψ is the new value δ(x).

**Side G (j = 1).** G is the branch of Proposition 4.2. Hypotheses, for every p′ = (x′, d′) ∈ 𝒯₁ with (x, d) = G(p′):
- (G) D₁ ⊂ Ω₁⁻; (A1) first(x) > 1 and second(x) ≥ second(x′) + σ; (A2) |x/x′ − 1| ≤ κ;
- (B_fwd) if x ∈ D₁ and |d| ≤ R₁(x), then |d′| < R₁(x′).

(B_fwd) is what the script checks: for x in the source disc and |d| ≤ R₁(x), |d′| ≤ R₁(x)(|μ₀| + |E|/R₁ + |c₂|R₁ + M₃|x|³R₁²) and the bracket is below the lower bound of R₁(x′)/R₁(x).

Let δ be analytic on D₁(c), |δ| ≤ R₁, and x′ ∈ D₁(c − σ). On the fibre disc 𝔽 = {|d′| ≤ R₁(x′)} write G(x′, d′) = (X(d′), Ψ₀(d′)), analytic on a neighbourhood of 𝔽, and Ψ = Ψ₀ − δ∘X; X(d′) ∈ D₁(c) by (A1) and the chart argument.
- *Boundary.* On |d′| = R₁(x′): by (B_fwd) in contrapositive, |Ψ₀(d′)| > R₁(X(d′)) ≥ |δ(X(d′))|. This is the pointwise inequality Rouché needs; the supremum form of the design is not used. So Ψ and Ψ₀ have the same number of zeros in 𝔽°.
- *Existence of a zero of Ψ₀.* Step 1 of Proposition 4.2: G(x′, E(x₀)) = (x₀, 0) with |E(x₀)| < R₁(x′).
- *Uniqueness.* If Ψ₀(d₁′) = Ψ₀(d₂′) = 0 then G(x′, d_i′) = (x_i, 0) with b₀(x_i) = x′ and x_i ∈ S₁; by INJ x₁ = x₂, and d_i′ = E(x_i).
- *Simplicity.* If the zero d₀′ had multiplicity m ≥ 2, then for small ε ≠ 0 the equation Ψ₀(d′) = ε would have m distinct solutions near d₀′. Each gives a point (x, ε) with b(x, ε) = x′ and x near x₀. Since ∂b/∂x(x₀, 0) = b₀′(x₀) ≠ 0 (|b₀′ − 1| < 1), the equation b(x, ε) = x′ has one solution near x₀ for small ε. So the m solutions have the same G-value, hence, G being injective on the fibre, are equal. Contradiction.
- So Ψ has exactly one zero in 𝔽°, simple; it is the new value δ(x′), analytic in x′.

**What this section does not contain.** The seed (Q1–Q3), the start of the induction, and the identification of the resulting graphs with the sectorial curves of the literature (L1–L3). They are as in the design and remain conditional (§11).

## 6. Zone II: from the statuses to the hypotheses

**Cover.** The run tiles [log ρ₀, log 0.60] × [a₁π, a₂π] (the chart sector, |ξ| ≥ ρ₀) by rectangles in (s, t) = (log|ξ|, arg ξ). Cutting a rectangle into four halves both sides. A rectangle with centre (s, t) and half-sides (h_s, h_t) is covered by the disc |x − x_c| ≤ r, x_c ≈ e^{s+it}/c, r = |x_c|(e^h − 1)(1 + 10⁻⁹), h = (h_s² + h_t²)^{1/2}: for a point of the rectangle, x/x_c = e^{δ}(1 + ε) with |δ| ≤ h, and |e^{δ} − 1| ≤ e^{|δ|} − 1. The slack 10⁻⁹ covers ε (§10).

**Statuses.** On a piece P the script encloses first and second on P.
- *out:* first ≤ 1 on P or second ≤ c_j on P. Then P ∩ D_j = ∅.
- *pass:* P lies in the guard core, and (A1), (A2), (B) are verified for every point of P that satisfies the wedge conditions. The verification uses, for such a point: 1 ≤ first ≤ f_hi, c_j ≤ second ≤ s_hi (f_hi, s_hi the upper ends of the enclosures on P); hence R_lo ≤ R_j ≤ R_hi; the one-step quantities on P × {|d| ≤ R_hi}; and for the ratio of tube radii, R_j(x′)/R_j(x) = |(x′/x)^α|(first′/first)^{−3}(second′/second)^{−3} with first′ ≥ first + Re Δτ, second′ ≥ second + Re(e^{iθ₀}Δτ). The logarithm in (x′/x)^α is principal: both points lie in the chart sector, whose opening is below π.
- If every piece is out or pass: a point of D_j in the covered region lies in a pass piece, hence in the guard core, which is (G) there; and (A1), (A2), (B) hold at it.

**Side G.** The piece is a target disc. The lemma (§4.1) gives the source disc B and fibre radius ρ; the forward quantities are enclosed on B × {|d| ≤ ρ}; (A1), (A2) for G are read off as first(x) = first(x′) + Re Δτ and so on; (B_fwd) is checked with R₁(x) ∈ [R_lo/ratio_hi, R_hi/ratio_lo]. The source x of a tube point over D₁ lies in D₁ by (A1), which is what makes the bounds of R₁(x) legitimate.

## 7. Zone I: the reduction

Setting: 0 < |ξ| ≤ ξ₀ = 0.05; X′ = (ξ₀/|c|)(1 + 10⁻⁹), X = 1.001X′, t = X³; sup bounds over |x| ≤ X (moduli of the coefficients plus tail). The derivation is in the header of the W4 block of the library; the elementary facts it uses:

1. **τ.** τ = A₃x⁻³(1 + η), |η| ≤ η̄ = (|A₂|X + |A₁|X² + |κ|X³(|ln X| + π))/|A₃|; the last term uses |log x| ≤ |ln|x|| + π and that r³(|ln r| + π) increases on (0, 1). So |τ| ≥ t_lo|x|⁻³ and first, second ≤ T_c|x|⁻³.
2. **Guard.** arg τ = arg A₃ − 3 arg x + arg(1 + η), |arg(1 + η)| ≤ arcsin η̄. On each guard arc the resulting interval of arg τ lies where one wedge condition fails (Re τ ≤ s₀ needs cos < 0 and |τ| large enough; second ≤ c_j follows from the sign of a cosine).
3. **Product of the functionals.** Let a = Re τ, b = second. Then Im τ = (a cos θ₀ − b)/sin θ₀ for j = 0 and −(a cos θ₀ + b)/sin θ₀ for j = 1, so |τ| ≤ K(|a| + |b|), K = max(1 + cot θ₀, 1/sin θ₀). On D_j: |a| ≤ (first − 1) + |s_j|, so first + second ≥ |τ|/K − |s_j| + 1 =: S. For p ≥ 1, q ≥ c_j ≥ 1, p + q ≥ S ≥ 1 + c_j: pq ≥ min(S − 1, c_j(S − c_j)) = S − 1, because c_j(S − c_j) − (S − 1) = (c_j − 1)(S − c_j − 1) ≥ 0. Hence R_j ≤ ε|ξ^α|(|τ|/K − |s_j|)⁻³, and the bound increases with |x| (Re α + 9 > 0).
4. **Binomial majorant.** |(1 + g)^{−β} − 1 + βg| ≤ (1 − |g|)^{−|β|} − 1 − |β||g|: the coefficients of (1 + g)^{−β} are bounded in modulus by those of (1 − u)^{−|β|}.
5. **Scaling.** If ν is convex on [0, u_m] with ν(0) = 0 then ν(u) ≤ uν(u_m)/u_m. Used to turn bounds at |x| = X into bounds proportional to |x|³.
6. **Gain.** (1 + u)⁻³ ≤ (1 + 3u)⁻¹ ≤ 1 − 3u + 9u² for u ≥ 0.

With these, (B) for F follows from w(1 − wt) − λ − e₁/P_lo − ν₁ > 0 and (B_fwd) for G from w − λ − e₁/P_lo − ν₁(1 + tw) > 0, with the constants of the library header. The lemma of §4.1 is applied with c = x′, r = 2|x′|⁴ sup|G0|, ρ = 2R₁(x′); its two conditions become the constant inequalities inv_i, inv_ii, and inv_disc keeps the disc inside |x| ≤ X.

## 8. The common arc

**Lemma 8.1 (inverse function step).** Let f be analytic on a neighbourhood of B = {|x − c| ≤ r} and m = |f′(c)| − r sup_B|f″| > 0. Then |f(a) − f(b)| ≥ m|a − b| on B, and every w with |w − f(c)| < rm has exactly one preimage in the open disc.
*Proof.* f(a) − f(b) = f′(c)(a − b) + ∫(f′ − f′(c)), and |f′ − f′(c)| ≤ r sup|f″| on B. For the second claim, on |x − c| = r: |f(x) − w − f′(c)(x − c)| ≤ |f(c) − w| + r·r sup|f″| < r|f′(c)|; Rouché against f′(c)(x − c). ∎

The four points of review `5871277385`:
1. *Exact start.* The first disc is centred at the midpoint of the ball of x*; x* lies in it. The check of segment 0 is res + (t₁ − t₀) < rm with t₀ the float nearest to t* and res computed against w(t₀). The step factor 0.8 leaves 0.2rm; |w(t*) − w(t₀)| = |t* − t₀| ≤ 10⁻¹⁵. So w(t*) is in the disc of Lemma 8.1 and its unique preimage in B₀ is x*.
2. *Tail for every t ≥ t_M.* The three sup bounds e₀, e₁, e₂ are sums of terms that increase with |x| on (0, 1). |x₀(w)| = (|A₃|/|w|)^{1/3} ≤ X_M when |w| ≥ |A₃|/X_M³, which holds for t ≥ t_M since |w| ≥ t. Branch: w(t) = Re τ* − it with Re τ* < 0 and t > 0 stays in the open third quadrant, so its principal logarithm is continuous in t; x₀(w(t)) is continuous, with arg ξ₀ → π/6.
3. *One branch.* Within a segment the solution is (τ|B_k)⁻¹(w(t)), analytic in t. At a common endpoint the solutions of B_k and B_{k+1} are the same point (checked). In the tail, for t′ near t the solution lies within ε′|x₀(t′)| of x₀(t′), ε′ < ε, hence in the disc at t, where τ is injective: the tail solution is locally (τ|disc)⁻¹(w), analytic. At t_K the chain solution lies in the tail disc (LINK), so it is the tail solution. The arc is the chain on [t*, t_K] and the tail on [t_K, ∞).
4. *Rounding.* §10. The 173 inequalities are evaluated in ball arithmetic from exact float inputs; a second run reproduces them bit for bit.

**In the domains.** Along the half-line Re τ = Re τ*, so s₀ < Re τ < s₁ (margins 0.25); second_j = second_j(τ*) + (t − t*) sin θ₀ > c_j. Every disc of the chain and the tail lie in both guard cores, hence in both chart sectors, where τ is the function used in the definition of D_j. So γ ⊂ D₀ ∩ D₁ (C2).
*Separate obligation, not settled here:* the continuation of τ⁻¹ along γ says nothing about the branch of F⁻¹; that is §4.

## 9. The legs

**Proposition 9.1.** Let p_k = (x_k, d_k), k = 0, …, n, be points with F̂(a) = b for consecutive points (a, b) = (p_k, p_{k+1}) (leg F) or (p_{k+1}, p_k) (leg G), all with |x_k| below the radius of a remainder profile and |d_k| ≤ 0.02. Let X_k = (x_c, r_x) and D_k = (d_c, r_d) be discs with x_k ∈ X_k, d_k ∈ D_k. Then each of the four updates of the library (base forwards, d forwards, d backwards, base backwards) returns a disc that contains the true value, provided the enclosures q are computed on a square containing X_k, μ₀ ≠ 0 on it (d backwards) and b₀′(x_c) ≠ 0 (base backwards).
*Proof.* Each update starts from an exact relation of §1 between the true values and subtracts the same expression at the centres.
- For a function f of x enclosed on the square Q ⊇ X_k and at the centre: |f(x_a) − f(x_c)| ≤ var f := sup of the modulus of the ball difference. For b₀: |b₀(x_a) − b₀(x_c)| ≤ sup_Q|b₀′|·r_x (segment in the convex disc).
- Products: T(x, d) = x⁴Q4(x)d: T(x_a, d_a) − T(x_c, d_c) = (x_a⁴Q4(x_a) − x_c⁴Q4(x_c))d_a + x_c⁴Q4(x_c)(d_a − d_c). Likewise for x⁴P4·d², μ₀d, c₂d², with |d_a² − d_c²| ≤ r_d(2|d_c| + r_d).
- Remainders: |r_Z| ≤ M_Z|x|⁴|d|³, |r| ≤ M₃|x|³|d|³ (Proposition 3.4), with |d_a| ≤ |d_c| + r_d.
- *d backwards:* d_a = (d_b − E(x_a) − c₂(x_a)d_a² − r)/μ₀(x_a). With cen = (d_{b,c} − E_c − c₂,c d_c²)/μ₀,c: d_a − cen = [(d_b − d_{b,c}) − (E(x_a) − E_c) − (c₂(x_a)d_a² − c₂,c d_c²) − r]/μ₀(x_a) + cen·(μ₀,c − μ₀(x_a))/μ₀(x_a).
- *base backwards:* b₀(x_a) = x_b − (terms in d_a). With u = x_c − (b(x_c, d_c) − x_{b,c})/b₀′(x_c): b₀′(x_c)(x_a − u) = (x_b − x_{b,c}) − [variation of the d-terms] − [b₀(x_a) − b₀(x_c) − b₀′(x_c)(x_a − x_c)], and the last bracket is at most var(b₀′)·r_x.
In each case the stated radius is the sum of the moduli. ∎

**Corollary 9.2.** Start from X₀ ∋ x* and D₀ = {|d| ≤ sup_{X₀}R_j}. Suppose the orbit of (ξ*, d_j*) stays in the tube over D_j (the conclusion of the tube lemma). Then after any sequence of the updates, of the a-priori update D_k ← {|d| ≤ sup_{X_k}R_j}, and of selections of the smaller of two valid discs, every X_k contains x_k and every D_k contains d_k. In particular D₀ contains d_j*.
*Proof.* Induction over the sequence. The a-priori update is valid because x_k ∈ D_j, where first ≥ 1 and second ≥ c_j, which is what `R_upper` assumes. For leg G, X_{k+1} is first obtained from Lemma 4.1 (the branch: §4.3). No update needs the discs to shrink. ∎

The two-disc test compares the two discs D₀ of the legs in ball arithmetic: |c₁ − c₀| > r₀ + r₁ implies d₀* ≠ d₁*.

## 10. Rounding

- **Balls.** All inequalities are evaluated with Arb balls; a comparison is true only if it holds for all points of the balls.
- **Float upper bounds.** `float(v.upper())` rounds a point value to the nearest double: relative error at most 2⁻⁵³. The scripts multiply by 1 + 10⁻¹² afterwards; two float operations add at most 3·2⁻⁵³. So the stored float is an upper bound. Floats enter Arb exactly.
- **Radii as floats.** A disc is *defined* by its centre (an exact Arb midpoint) and its float radius. Statements are about this disc.
- **Pieces.** The centre is computed from floats s, t and float values of |c|, arg c; so x_c = (e^{s+it}/c)(1 + ε) with |ε| ≤ 10⁻¹⁴. The radius carries the factor 1 + 10⁻⁹ on e^h − 1 ≥ 4·10⁻⁴ (smallest piece): a slack of 4·10⁻¹³ relative, above ε and above the rounding of the rectangle edges (10⁻¹⁵ in s and t). Neighbouring rectangles share an edge up to this rounding, so the discs cover a neighbourhood of every edge.
- **Constants M₃, M_Z, Cauchy constants.** Suprema of float upper bounds, with the factor 1 + 10⁻¹².
- **Machine checks (W8).** Each float that stores a rigorous upper bound is compared in ball arithmetic with the ball it bounds when it is made (`_assert_up`): sup bounds and Cauchy constants on circles, remainder constants, the radius of every arc ball (against half the arc length plus the rounding of the centre), the radii of the discs of the legs and the fibre radii handed to the enclosures (legs, pieces, zone I), the radius of the disc of zone I, t_M and the relative bound of the arc tail, the bounds of sup|b₀′ − 1| in INJ and the radius of its inner disc, the source discs recorded for SRC and SRC1, and the disc of every piece of the zone-II cover (`piece_disc`: the disc contains its rectangle enlarged by the relative margin 10⁻¹², so neighbouring rectangles and the four parts of a cut rectangle overlap). The first disc of the arc is checked against t* and x* as balls. A failed check stops the run.
- **How the gates decide (r2).** A gate of W3–W8 that belongs to the argument decides in one of three ways: by a comparison of balls; by comparing a machine-checked float bound with a float that defines a set (a sector edge, a radius, ε); or by the sign of a float made from a lower bound (rounding to nearest keeps the sign). Printed values are rounded for the report and are not bounds. The thresholds on the series tails (10⁻⁶) and on the radii of the vanishing coefficients (10⁻¹⁵⁰) are quality thresholds: no bound of the argument depends on them, since tails and radii enter every enclosure as balls.
- **Not machine-checked.** The two elementary lemmas behind these checks (|e^δ − 1| ≤ e^{|δ|} − 1; chord ≤ arc) and the control flow of the scripts. The sector S₁ and the grids of the covers are given by floats; that the pieces cover them rests on the margin of `piece_disc` (10⁻¹² relative) against the rounding of the grid (10⁻¹⁵). An implementation with Arb-only constants is not built.

## 11. What is not proved here

1. **The seed and the identification with the literature** (Q1–Q3, P1, L1–L3): the start of the induction of the tube lemma and the divergence step (design §5 step 6). They depend on López-Hernanz 2012, Theorems 4.2(3) and 5.1; LIT's reply `pipes/DYAD/20261112-LIT-lh2012-thm42-use-check.md` (rtg-lit `a3628d4`) has arrived and is not yet dispositioned by the owner; by its own statement it does not prove the seed.
2. **The triangular form of the recursion** behind S4 (P1-c) is taken from the earlier records.
3. **The development runs are not certificates.** INJ, SRC, SRC1, the piece statuses, the zone-I constants, the arc and the legs are facts of development runs.
4. **Done in W8** (hand-over record §7): `full_fibre=True` in the leg (§4.3); strict membership in SND; machine checks of the float bounds; the control "wrong branch". *Not done:* separate printing of nominal and mutated constants in the W2b control outputs.
5. **Analyticity of the new δ in the base variable** in §5 is stated, not written out (the zero of a holomorphic family with a simple zero; standard).
