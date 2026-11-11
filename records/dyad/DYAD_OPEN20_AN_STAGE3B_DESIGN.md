# DYAD OPEN 20 (analytic branch) — stage 3b: design of a certificate for one nonzero sectorial jump

**Date:** 11 November 2026. **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION). A written design with `[NUM]` feasibility sampling. Nothing is certified, no result is claimed, and no certification run was made. **Accepted by the PI on 11 November 2026 as the basis for the stage-3c certificate design, scoped (§12).** Stage 3c itself is not authorized.
**Revision:** r2, after the co-owner's review of r1 (PR #218, review `5858511915`, verdict REVISE). The five review items R1–R5 are applied; §11 lists what changed.
**Authority:** item 2 of the order of work in `records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md` §9 (the "pilot design" below). Target agreed by the co-owner and the owner on 11 November 2026: one jump, first at \|ξ*\| = 0.40. Stage 3c (certification) is not authorized. Scouting of the second overlap class is not authorized.
**Governing edition:** DYAD v6.4.24 (`dyad-v6.4.24`). OPEN 20 B-an and B-6 are ACTIVE.
**Reviews and decision:** r1 review `5858511915` (REVISE), r2 read-back `5858796744` (ACCEPT, scoped), PI decision of 11 November 2026 (§12).

## 0. Outcome in one paragraph

The design replaces the operator route (pilot design §4, E3–E6) by a **tube route**. Each sectorial curve is shown to lie in an explicit thin tube around a truncated series, over a bounded local domain that reaches from 0 to the common point ξ*. The proof needs a guard property of the domain, two pointwise inequalities for one step of the map, (A) and (B) in §4, and the published existence of the curves near 0. The dynamics then shrinks the set of admissible values at ξ* step by step, so two enclosures at ξ* can be separated. Sampling at 877 and 763 points finds the inequalities satisfied, with margins equal to what the leading normal form predicts, on domains that contain ξ*. The estimated width of the final enclosure is about 3·10⁻⁷ of the jump measured in stage 2b. The sampling is `[NUM]` and bounds nothing between its points. What remains is listed as proof obligations in §6; the main ones are the analytic estimate near 0 and the interval verification of the guard property, (A) and (B).

## 1. What a certificate would state

Notation as in the pilot design: pilot branch Γ̂₊ of F = T⁶ with formal series w = Σ a_k z^k, ξ = c₊z, lifted coordinate w = z²(a₊ + y), Y = y − b₁x, common point ξ* = 0.40·e^{iπ/6}. G is the local inverse of F at 0.

**Claim C (target of stage 3c; not claimed here).**
- **C1.** There are bounded open sets D₀, D₁ (§3) and analytic functions φ₀ on D₀ and φ₁ on D₁ such that:
  - the graph of φ₀ is invariant under F, and the graph of φ₁ under G;
  - near 0, φ₀ is the invariant curve that López-Hernanz 2012 attaches to the attracting petal of F around arg ξ = 0, and φ₁ the one attached to the attracting petal of G around arg ξ = π/3.
- **C2.** There is an arc γ in D₀ ∩ D₁ from ξ* to 0, and γ has a connected open neighbourhood U in D₀ ∩ D₁.
- **C3.** φ₁(ξ*) − φ₀(ξ*) ≠ 0: two complex discs that contain the two values are disjoint.

**What follows (§5, step 6).** Γ̂₊ diverges. Then Γ̂₋ diverges, because T exchanges the branches, and log F diverges by Lemma 5b-1 of P1-c-5 (SESSION). This is the decision rule of the pilot design §5.

**What does not follow.** B-an and B-6 are not decided. Nothing is said about the second T²-class of overlaps, about a Stokes constant, or about real orbits.

**Relation to D9.** If φ₀ and φ₁ are identified with the 3-sums of Γ̂₊ (López-Hernanz 2012, Corollary 5.2), then C3 says Δ₊,₀(z*) ≠ 0 in the sense of D9. The divergence conclusion does not use this identification.

## 2. Choice of route

| Route | State | Verdict |
|---|---|---|
| Hakim operator with a-priori constants (pilot design §4; LIT INF-009/010) | stage 3a: admits only \|ξ\| < 1.76·10⁻⁶ in the m = 2 chart. LIT's subpetal reply: the orbit criterion alone stops at \|ξ\| < 0.074 | set aside |
| Validated Borel–Laplace resummation of Γ̂₊ | LIT found no validated method for a map of this type; validated Borel summation exists for linear ODEs only | not pursued |
| **Tube route (this note)** | uses only one-step inequalities and forward or backward iteration; sampled in §7 | **proposed** |

Why the tube route fits this map:
- Along the attracting direction of F the curve is transversally expanding (Re α = −102/19 < 0). A normally expanding invariant curve is the set of points whose forward orbits stay near it. That gives existence on a larger domain and a sharp shooting condition from the same inequality.
- The jump is large where the map is still close to its normal form in the right coordinates. At \|ξ*\| = 0.40 it is about 2·10⁻⁸ in the lifted unit, so no high precision is needed.
- The local theory is used only qualitatively: existence, uniqueness and asymptotics near 0. No constant of the published proofs enters.

## 3. Objects

All objects are explicit elementary functions of ξ. Numbers are `[NUM]` values from the sampling run.

- **Truncated series.** φ_N(z) = Σ_{k=2..N} a_k z^k with N = 40. Normal deviation in the lifted unit: d = (w − φ_N(z))/z².
- **Chart sectors and branches.**
  - Ω₀ = {0 < \|ξ\| < 0.60, −0.20π < arg ξ < 0.30π} and Ω₁ = {0 < \|ξ\| < 0.60, 0.03π < arg ξ < 0.50π}.
  - On both, log ξ and log z (z = ξ/c₊) are the principal branches. This is one continuous sheet: arg z = arg ξ − arg c₊ stays between −0.512π and 0.188π.
- **Fatou coordinate, four terms.** τ(ξ) = A₃z⁻³ + A₂z⁻² + A₁z⁻¹ + κ log z. It is the truncation of the formal Fatou coordinate of the restricted map on the series curve (stage 2b): A₃ = −1/(3ℓ₊) ≈ −3.328 − 0.682i, A₂ ≈ 0.537 + 1.611i, A₁ ≈ −0.135 + 0.154i, κ ≈ 1.812 + 0.090i. One step of F changes τ by about +1, one step of G by about −1. τ* = τ(ξ*) ≈ −1.693 − 4.082i.
- **Wedge functionals.** h₀(τ) = Re(e^{iθ₀}τ) and h₁(τ) = Re(−e^{−iθ₀}τ), with θ₀ = π/2 − η₀ and η₀ = π/8.
- **Local domains.** With s₀ = Re τ* − 0.25, s₁ = Re τ* + 0.25, c₀ = h₀(τ*) − 0.15, c₁ = h₁(τ*) − 0.15:
  - D₀ = {ξ ∈ Ω₀ : Re τ(ξ) > s₀, h₀(τ(ξ)) > c₀}, for F;
  - D₁ = {ξ ∈ Ω₁ : Re τ(ξ) < s₁, h₁(τ(ξ)) > c₁}, for G.
- **Why the chart sector is part of the definition (review R1).** Without it the two wedge conditions hold again far from 0, because Re κ > 0: on arg ξ = π/12 both functionals grow like log\|ξ\|. In an exploratory scan (not part of the package) they hold again from \|ξ\| ≈ 0.7 on. So "the wedge" is not a local set by itself.
- **Guard property (G).** D₀ lies in the core Ω₀⁻ = {\|ξ\| ≤ 0.47, −0.08π ≤ arg ξ ≤ 0.20π}, and D₁ in Ω₁⁻ = {\|ξ\| ≤ 0.42, 0.09π ≤ arg ξ ≤ 0.43π}. Equivalently: no point of the guard zone Ω_j ∖ Ω_j⁻ satisfies both wedge conditions. Then the closure of D_j does not meet the artificial boundary of Ω_j except at 0; its boundary consists of the two natural walls and the point 0.
- **Nested families.** D_j(c) = {ξ ∈ D_j : h_j(τ(ξ)) > c} for c ≥ c_j. Only one wall moves.
  - *Locality.* D_j is bounded and τ is continuous on Ω_j away from 0. So for every r > 0 there is c with D_j(c) ⊂ {\|ξ\| < r}.
  - *The common arc stays in the family.* On the half-line τ = Re τ* − it the functionals h_j grow like t·cos η₀. So its points with large t lie in D₀(c) ∩ D₁(c) for every c.
- **Tube radius.** With q₁ = q₂ = 9 and ε fixed by R(ξ*) = 2·10⁻³:
  - R₀(ξ) = ε\|ξ^α\|·(Re τ − s₀ + 1)^{−q₁/3}·h₀(τ)^{−q₂/3} on D₀;
  - R₁(ξ) = ε\|ξ^α\|·(s₁ − Re τ + 1)^{−q₁/3}·h₁(τ)^{−q₂/3} on D₁.
  - \|ξ^α\| is the leading normal multiplier accumulated along an orbit. The two other factors make the tube shrink along orbits faster than the normal dynamics. To first order the relative gain per step is (q₁/3)/(first functional) + (q₂/3)·sin η₀/(second functional). Call this the model gain.
- **Tubes.** V₀ = {ξ ∈ D₀, \|d\| ≤ R₀(ξ)}, and V₁ likewise.

## 4. The tube lemma

Stated for F on D₀; the statement for G on D₁ is the same with G, D₁(c), R₁. Points are written in the coordinates (ξ, d), so the truncated series is d = 0 and a curve is a function d = δ(ξ). Write (ξ′, d′) for the image of (ξ, d) under the map, E(ξ) = d′(ξ, 0), μ₀(ξ) for the derivative of d′ in d at d = 0, and nl(ξ) = sup over \|d\| = R(ξ) of \|d′ − E − μ₀d\| / (\|μ₀\|R(ξ)).

**Hypotheses.**
- **(G) Guard:** D₀ ⊂ Ω₀⁻ (§3).
- **(A) Inward base motion.** For every point (ξ, d) of the tube over D₀:
  - (A1) Re τ(ξ′) > s₀ and h₀(τ(ξ′)) ≥ h₀(τ(ξ)) + σ, with a fixed σ > 0;
  - (A2) \|ξ′/ξ − 1\| ≤ κ, with κ = 0.15.
- **(B) Strong exit inequality.** For every ξ ∈ D₀: \|μ₀\|(1 − nl)·R(ξ) − \|E(ξ)\| > sup of R(ξ′) over the fibre \|d\| ≤ R(ξ).
- **(Q) Seed.** For some c₁, there is an analytic function δ on D₀(c₁) whose graph is F-invariant and lies in the tube (\|δ\| ≤ R₀).

**(G), (A1) and (A2) give the inward property on the whole fibre and at every wall.** Let (ξ, d) be in the tube over D₀(c).
- By (G), \|ξ\| ≤ 0.47 and −0.08π ≤ arg ξ ≤ 0.20π. By (A2), \|ξ′\| ≤ 0.47·1.15 < 0.60 and arg ξ′ differs from arg ξ by at most arcsin 0.15 < 0.048π. So ξ′ ∈ Ω₀: a step cannot cross the outer arc or a side of the chart sector. (For D₁: 0.42·1.15 < 0.60, and the angular margins are 0.06π and 0.07π.)
- By (A1), ξ′ satisfies both wedge conditions. So ξ′ ∈ D₀, and h₀(τ(ξ′)) > c + σ. Hence ξ′ ∈ D₀(c + σ).

**Conclusion.** There is exactly one analytic δ₀ on D₀ that extends the seed of (Q), has an F-invariant graph and satisfies \|δ₀\| < R₀. In the raw chart it is φ₀(z) = φ_N(z) + z²δ₀(c₊z). For every ξ ∈ D₀, δ₀(ξ) is the only point of the closed tube fibre whose image lies on the graph of δ₀.

The lemma gives the unique extension **of the chosen seed**. It does not say that every invariant graph in the tube equals δ₀. The design no longer needs such a statement (§5, step 6).

**Proof sketch** (to be written out in the proof record of 3c).
1. *One step outward.* Let δ be analytic on D₀(c) with invariant graph in the tube, and let ξ ∈ D₀(c − s) with 0 < s ≤ σ. By the inward property, every point of the fibre over ξ is mapped over D₀(c). So Ψ(d) = d′(ξ, d) − δ(ξ′(ξ, d)) is analytic on the closed fibre disc \|d\| ≤ R(ξ). Its zeros are the points of the fibre that are mapped onto the graph of δ.
2. Put Ψ₀(d) = d′(ξ, d). On the fibre circle, \|Ψ₀\| ≥ \|μ₀\|(1 − nl)R − \|E\|, and \|Ψ − Ψ₀\| = \|δ(ξ′)\| ≤ R(ξ′). By (B) and Rouché's theorem, Ψ and Ψ₀ have the same number of zeros in the disc. By the same inequality Ψ₀ differs from the linear function μ₀d by less than \|μ₀\|R on the circle, so Ψ₀ has one zero. Hence Ψ has exactly one zero δ̃(ξ).
3. δ̃ is analytic in ξ (a simple zero of an analytic family). It equals δ on D₀(c), since δ(ξ) is a zero and cannot lie on the circle. Its graph is invariant by construction.
4. *Induction.* Start from (Q) at c₁ and go down to c₀ in finitely many steps.

**The seed (Q), made precise.** Let u_j be the invariant curve of López-Hernanz 2012, Theorem 4.2, on the petal domain Δ_j of the pilot design D8 (for F if j = 0, for G in the rotated chart of D5 if j = 1). The seed is u_j, written as a deviation from φ_N, restricted to D_j(c₁). Three things are needed for large c₁:
- **(Q1) Domain.** D_j(c₁) ⊂ S_j ⊂ Δ_j, where S_j is the straight sector of D7 (\|arg ξ − jπ/3\| ≤ 5π/24).
  - By locality (§3), D_j(c₁) lies in an arbitrarily small disc.
  - For small ξ, τ = (1/(3ξ³))(1 + O(ξ)), so the wedge conditions confine arg ξ to (−η₀/3, π/6) for j = 0 and to (π/6, π/3 + η₀/3) for j = 1, up to o(1). The distance to the bisector is at most π/6, which is less than 5π/24.
  - This has to be proved with an explicit bound for the O(ξ) term (P9).
- **(Q2) Tube.** On closed subsectors of the petal, u_j has Γ̂₊ as asymptotic expansion (López-Hernanz 2012, Theorem 5.1). So u_j differs from φ_N by O(\|ξ\|^{N−1}) = O(\|ξ\|³⁹) in the lifted unit, while R_j ≥ const·\|ξ\|^{Re α + q₁ + q₂} = const·\|ξ\|^{12.6}. Hence the graph of u_j over D_j(c₁) is in the tube for c₁ large.
- **(Q3) Invariance in the sense of the lemma.** The image of a graph point over ξ ∈ D_j(c₁) is a graph point of u_j, and its base lies in D_j(c₁) by the inward property.
- LIT checked the deductions of the literature chain (owner assessment §5; INF-005 to INF-008). It is at SESSION scope in the Dyadic records and is not a theorem-grade import.

## 5. From the lemma to the certificate

1. **Curves.** The lemma for (F, D₀, R₀) and for (G, D₁, R₁) gives δ₀ and δ₁, hence φ₀ and φ₁. This is C1.

2. **Common arc.** γ(t), t ≥ t* = −Im τ*, is the continuous solution of τ(γ(t)) = Re τ* − it with γ(t*) = ξ*. Its τ-values satisfy the wedge conditions of both domains by construction. To be proved (review R3):
   - *for all large t, analytically:* on a region {\|ξ\| < ρ, \|arg ξ − π/6\| < β} the function τ is injective, and its image contains the half-line for t ≥ t_M. One way: in the variable ζ = ξ⁻³, τ = ζ/3 + g(ζ) with \|g′\| ≤ k < 1/3 on a half-plane {Im ζ < −M}, which is convex. A map of this form is injective on a convex set, and a perturbation argument with explicit bounds for g shows that its image contains the half-line for large t. This gives γ(t) → 0 and arg γ(t) → π/6. The bounds are not yet written;
   - *for t* ≤ t ≤ t_M:* a validated continuation (interval Newton on consecutive segments), which also shows that γ stays in Ω₀⁻ ∩ Ω₁⁻.
   - U is the union of small discs around the points of γ inside the open set D₀ ∩ D₁. It is open and connected. This is C2.
   - For large t, γ(t) ∈ D₀(c₁) ∩ D₁(c₁), by §3.

3. **Value of φ₀ at ξ* (review R4).** Let 𝔽* = {\|d\| ≤ R₀(ξ*)} be the closed fibre over ξ*. For d ∈ 𝔽* write (ξ_k(d), d_k(d)) = F^k(ξ*, d). Both components depend on d: the base point moves with the normal deviation. By the lemma, d* = δ₀(ξ*) lies in 𝔽* and \|d_k(d*)\| ≤ R₀(ξ_k(d*)) for every k. The certificate constructs discs 𝔽* = B⁽⁰⁾ ⊃ B⁽¹⁾ ⊃ … ⊃ B⁽ⁿ⁾ = B₀ with the property

   *every d ∈ B⁽ᵏ⁻¹⁾ with \|d_k(d)\| ≤ R₀(ξ_k(d)) lies in B⁽ᵏ⁾.*

   Then d* ∈ B₀. One step of the construction, all in ball arithmetic:
   - **Inclusion.** An enclosure of the full two-component image F^k(ξ*, B⁽ᵏ⁻¹⁾), obtained from the enclosure at step k − 1 by one validated evaluation of F. It covers every d in the disc, not one orbit.
   - **Derivative.** An interval enclosure A_k of ∂d_k/∂d on B⁽ᵏ⁻¹⁾, as the lower-right entry of the product of the interval Jacobians of F in (ξ, d) along the enclosures. The product carries the effect of the moving base point.
   - **Exclusion.** For d, c in the disc, \|d_k(d) − d_k(c)\| ≥ m_k\|d − c\| with m_k = \|mid A_k\| − rad A_k. This holds because the disc is convex and the derivative stays in the one complex interval disc A_k along the segment from c to d (integrate the derivative). The certificate must show m_k > 0. With c the centre: every d with \|d_k(d)\| ≤ R₀(ξ_k(d)) satisfies \|d − c\| ≤ (sup R₀ + \|d_k(c)\|)/m_k, where the supremum is over the enclosure of ξ_k. This disc is B⁽ᵏ⁾.
   - **Error sources covered:** the coefficient balls of φ_N, the evaluation of the map, of τ and of R₀, the branch of the logarithms on the enclosures (inside Ω₀ by the inward property), and rounding. The image, and for the second leg the inverse, must be validated on the whole enclosure, not only along the centre orbit.
   - By (B) each step shrinks the disc by about the factor 1 + (margin of (B)). This is the lemma's own mechanism, carried out along one fibre with validated numbers.

4. **Value of φ₁ at ξ*.** The same with G in place of F and R₁ in place of R₀, with a validated inverse at each step. It gives B₁.

5. **Separation.** B₀ = disc(c₀ᴮ, r₀) and B₁ = disc(c₁ᴮ, r₁) are discs in the same coordinate, the deviation d at ξ* from the same φ_N. C3 holds if \|c₁ᴮ − c₀ᴮ\| > r₀ + r₁, evaluated in ball arithmetic.

6. **Divergence.** Suppose Γ̂₊ converges, with sum S on \|ξ\| < r.
   - In the normalized chart the graph of S is Y = O(ξ²), because m = 2, and it is invariant under F and G. On a sufficiently small petal domain Δ_j it therefore belongs to the class 𝓗_Δ of D8 (\|Y\| ≤ \|ξ\|, \|Y′\| ≤ 1).
   - By the uniqueness statement of López-Hernanz 2012, Theorem 4.2(3), S = u₀ on Δ₀ and S = u₁ on Δ₁ (for G in the rotated chart).
   - For large t the point γ(t) lies in D₀(c₁) ∩ D₁(c₁) and in \|ξ\| < r. Near it, φ₀ = u₀ = S = u₁ = φ₁.
   - φ₀ − φ₁ is analytic on the connected set U and vanishes on an open subset. So it vanishes on U, in particular at ξ*. This contradicts C3.
   - This step uses the published uniqueness and no uniqueness statement of our own. It does not use the identification with 3-sums.

The enclosure of step 3 is far below the jump because the tube is thin where the orbit ends, not because the tube is thin at ξ*. At ξ* the tube has radius 2·10⁻³, which is 10⁵ times the jump.

## 6. Proof obligations

| # | Obligation | Kind | State |
|---|---|---|---|
| P1 | Tube lemma, full proof, with the guard property and the inward property at every wall (§4) | analytic | sketched here |
| P2 | *Withdrawn.* A uniqueness theorem for all invariant graphs in the tube is not needed; L3 replaces it | — | — |
| P3 | **Zone I:** (G), (A1), (A2) and (B) for \|ξ\| ≤ ρ₀, from explicit bounds of the lifted map on a polydisc | analytic, with constants from P6 | **open; the main analytic work** |
| P4 | Divergence argument (§5, step 6) | analytic | sketched here |
| P5 | Enclosures of a₂ … a₄₀ | computer-checked (ball arithmetic, exact recursion) | stage 2 has `[NUM]` values |
| P6 | Bounds of the lifted map and of its inverse branch on a polydisc; lower bound for \|1 + x³G\| (pilot design E1, E2) | computer-checked | tooling exists (bounds preflight); constants to be recomputed on the right polydisc |
| P7 | **Zone II for F:** a box cover of the whole chart sector Ω₀ ∩ {\|ξ\| ≥ ρ₀}. On the guard zone: (G). On D₀, including boxes that meet its two walls: (A1), (A2), (B) | computer-checked (interval arithmetic) | **open; the main computation** |
| P8 | The same on Ω₁ for G, with a validated inverse on each box | computer-checked | open |
| P9 | Domain and arc: (Q1) with an explicit bound; the arc γ for large t analytically and on the compact part by validated continuation; γ ⊂ D₀ ∩ D₁ | analytic and computer-checked | open; small |
| P10 | Fibre enclosures B₀, B₁ as in §5 steps 3 and 4: inclusion of the whole fibre image, derivative with moving base, exclusion, all error sources; then the two-disc test of step 5 | computer-checked | estimated only (§7, SEP) |
| P11 | Negative controls of the certificate: the zero-jump vector-field model must give overlapping discs; wrong branch; wrong log branch; perturbed α (pilot design §5) | computer-checked | the zero-jump harness exists (stage 2b) |
| L1 | Existence of u_j on Δ_j and asymptotics on closed subsectors (López-Hernanz 2012, Theorems 4.2 and 5.1), for F and for G | literature | SESSION scope; LIT-checked chain |
| L3 | Uniqueness in the class 𝓗_Δ (Theorem 4.2(3)) applied to a convergent invariant graph, for F and for G in the rotated chart of D5. To be shown: the graph is a parabolic curve in the theorem's sense (the base dynamics is forward stable on the petal) and the hypotheses hold in the rotated chart | literature | the co-owner read the theorem and proposed this use; LIT is asked to validate it (`pipes/LIT/20261111-DYAD-lh2012-thm42-uniqueness-use.md`) |
| L2 | Lemma 5b-1 (P1-c-5), for the step to log F | existing SESSION lemma | unchanged |

The owner has not read the text of López-Hernanz 2012 in this session; it is not in the repository. L1 and L3 rest on LIT's records and on the co-owner's reading.

The tube lemma holds on any family of sets for which its hypotheses hold. The chart sectors, the cores, the exponents and R(ξ*) are design choices; a certification run may change them if an interval check fails somewhere.

## 7. Feasibility sampling (`[NUM]`, OWNER-RUN)

**Package.** Script `evidence/dyad/scripts/dyad_open20_an_stage3b_tube_sampling.py` (SHA-256 `e6dbffad48b22f98823e007de4711ec5b323b476bed43b26b1fc8a2f6c8ae34a`); run `evidence/dyad/open20-an/stage3b-design/run.sh`; outputs and `SHA256SUMS.txt` in the same folder (`tube_sampling.json` `6dc2e2de…e247`). Inputs: the stage-2 coefficients (`6ca8c663…477e`) and the stage-2b output (`610433e5…a268`).

**What it does.** It evaluates the full map F, and a numerical inverse G, at 100 digits on a polar grid over each chart sector: 59 radii from 0.01 to 0.595, arguments in steps of π/96. At each grid point of a domain it computes E, μ₀, nl on eight points of the fibre circle and the quantities of (A) and (B). It computes no sectorial value and no jump.

**Limits.** Sampling is not a bound. Nothing is known between the points. No interval arithmetic is used. The numbers show that the hypotheses are plausible and how large the margins are; they prove nothing.

**Result** (16 gates PASS; the controls SWAP and SHIFTCOEF each exit 1 at the named gates):

| Quantity | D₀ with F | D₁ with G |
|---|---|---|
| sample points in the domain | 877 | 763 |
| extent of the sampled domain | \|ξ\| ≤ 0.46, arg ξ from −0.031π to 0.167π | \|ξ\| ≤ 0.40, arg ξ from 0.156π to 0.365π |
| (G): grid points in the guard zone, of which in the wedge | 1376, 0 | 1139, 0 |
| (A1): smallest gain of the first, second functional | 0.935, 0.292 | 0.948, 0.335 |
| (A2): largest relative step | 0.137 | 0.073 |
| sampled images outside the domain | 0 | 0 |
| (B): smallest margin | 1.48·10⁻⁵ at \|ξ\| = 0.01 | 1.47·10⁻⁵ at \|ξ\| = 0.01 |
| (B): smallest margin / model gain | 0.9999 | 1.0000 |
| largest \|E\|/R | 0.082 | 1.5·10⁻⁵ |
| largest nl | 7.3·10⁻³ | 7.2·10⁻³ |

Margin of (B) by radius (smallest value in each band, with the model gain at the same point):

| \|ξ\| | D₀: margin | D₀: model | D₁: margin | D₁: model |
|---|---|---|---|---|
| 0.01–0.03 | 1.48·10⁻⁵ | 1.48·10⁻⁵ | 1.47·10⁻⁵ | 1.47·10⁻⁵ |
| 0.03–0.06 | 4.17·10⁻⁴ | 4.16·10⁻⁴ | 4.12·10⁻⁴ | 4.10·10⁻⁴ |
| 0.06–0.10 | 3.97·10⁻³ | 3.94·10⁻³ | 3.83·10⁻³ | 3.80·10⁻³ |
| 0.10–0.15 | 0.0166 | 0.0164 | 0.0156 | 0.0154 |
| 0.15–0.20 | 0.072 | 0.069 | 0.065 | 0.063 |
| 0.20–0.25 | 0.179 | 0.164 | 0.159 | 0.146 |
| 0.25–0.30 | 0.329 | 0.286 | 0.296 | 0.257 |
| 0.30–0.35 | 0.599 | 0.479 | 0.577 | 0.455 |
| 0.35–0.41 | 1.04 | 0.74 | 1.25 | 0.83 |
| 0.41–0.48 | 1.38 | 0.93 | no points | — |

**The common point itself** (gate XISTAR; 64 fibre directions; review R5). ξ* lies in D₀ and in D₁.

| At ξ* | D₀ with F | D₁ with G |
|---|---|---|
| margin of (B) | 6.60 | 6.03 |
| gains of the two functionals | 0.949, 0.355 | 0.948, 0.333 |
| \|E\|/R | 8.0·10⁻⁶ | 3.7·10⁻⁶ |
| nl | 7.2·10⁻³ | 7.2·10⁻³ |

- *Agreement with the co-owner's independent point check.* That check used R(ξ*) = 10⁻³ and gave margins 6.81 and 6.22, \|E\|/R 1.59·10⁻⁵ and 7.38·10⁻⁶, nl 0.00357 and 0.00359. This script with `--rstar 1e-3` gives 6.80 and 6.22, 1.591·10⁻⁵ and 7.383·10⁻⁶, 0.00357 and 0.00359. The two computations are separate codes.
- The margin at ξ* is far above the model gain because the first functional is close to 1 there, so one step changes it by a large factor. The model gain is a first-order expression.

**Reading.**
- The margin follows the model gain down to \|ξ\| = 0.01 and exceeds it at larger radii. It decays like \|ξ\|³, as the gain per step should. This is what an analytic proof near 0 has to reproduce (P3).
- The wedge functionals gain nearly their model values (1 and sin η₀ = 0.383) everywhere. So the four-term Fatou coordinate is good enough on these domains. The leading term 1/(3ξ³) alone is not: in an exploratory run, which is not part of the package, its step error was 0.5 to 0.7 at \|ξ\| = 0.40.
- The truncated series is inside its tube: \|E\|/R ≤ 0.082, reached at the outer edge of D₀ (\|ξ\| between 0.44 and 0.46).
- The guard zones are clear on the grid, and a step is shorter than their width.

**Common arc** (gate PATH; 29 points). The arc Re τ = Re τ* was followed from ξ* to −Im τ = 3000. \|ξ\| decreases from 0.40 to 0.047 and arg ξ moves from π/6 to 0.1634π. This is a finite sample; the proof is P9.

**Last step** (gate SEP; n = 334 steps, as in stage 2b). An **estimate**, not an enclosure: it uses the derivative along one sampled orbit per leg.

| Leg | Tube radius at the far end | Factor along the leg | Contribution to the width at ξ* |
|---|---|---|---|
| φ₀: F from ξ* to \|ξ\| = 0.0961 | 1.4·10⁻¹² | amplification 1711 | 1.6·10⁻¹⁵ |
| φ₁: from \|ξ\| = 0.0986 on the S₁ side to ξ* | 1.5·10⁻¹¹ | contraction 1.18·10⁻⁴ | 3.5·10⁻¹⁵ |

Estimated total width 5.1·10⁻¹⁵, against \|Δ_Y\| = 1.95·10⁻⁸ from stage 2b: a ratio of 2.6·10⁻⁷. So the validated construction of §5 step 3 has six orders of magnitude to spare.

**Two controls that were tried and dropped.**
- A tube with \|ξ^{−α}\| in place of \|ξ^α\| still passes on these domains. So it is not a negative control: here the decay factors carry the inequality, and the factor \|ξ^α\| only makes the margin equal to the model gain.
- q₁ = q₂ = 0 gives a tube whose radius grows without bound as ξ → 0. The run did not finish and was stopped.

**Parameter history.** The script has exploration options (`--q`, `--rstar`, `--eta-div`, `--dc`, `--ds`); the recorded run uses the defaults.
- q₁ = q₂ = 12 with R(ξ*) = 10⁻⁴: \|E\|/R = 1.2 at the outer edge of D₀, so the gate failed.
- η₀ = π/6: the domain reaches \|ξ\| = 0.48, where N = 40 is no longer adequate. η₀ = π/8 was chosen for that reason.
- r1 used q = 9 with R(ξ*) = 10⁻³ on a grid whose largest radius was 0.437. The grid missed the outer edge of D₀ (0.44 to 0.46) and stopped below \|ξ*\| on D₁ (review R5). With the edge radii added, \|E\|/R reached 0.143 there, above the gate of 0.1. R(ξ*) = 2·10⁻³ brings it to 0.082. The inequality (B) held in both cases.

## 8. What stage 3c would consist of (not authorized; for the decision)

1. **Proof record:** P1, P3, P4 and the analytic parts of P9 written out, with the constants that P6 supplies.
2. **Certificate script** with fixed command, JSON output with hashes, and the controls of P11:
   - P5 and P6: coefficient enclosures and map bounds;
   - P7 and P8: zone II. A box cover of the two chart sectors for ρ₀ ≤ \|ξ\| < 0.60, with boxes of a few per cent relative size, is of the order of 10⁴ to 10⁵ boxes per sector. Each box needs one interval evaluation of the map with its first derivatives. At small radius the margin is of order \|ξ\|³, so the evaluation has to use a centred form;
   - P9: the compact part of the arc;
   - P10: two legs of 334 steps, each step with an interval Jacobian.
3. **Receiving review** with an independent replay.

**Cost (owner estimate, not measured).** Minutes to about an hour of `python-flint` computation, no special hardware, precision of 100 to 200 digits. It can run in the repository workspace or on the PI's machine.

**Choice of ρ₀.** The sampled margin equals the model gain already at \|ξ\| = 0.1. A zone I up to ρ₀ between 0.05 and 0.1 is the working assumption. It depends on the constants of P6 and is not verified.

## 9. Open points and risks

1. **Zone I is not sampled as a proof.** The analytic estimate needs bounds of the lifted map on a polydisc of radius about 0.1. The earlier preflight used a Cauchy radius of 0.002 and gave constants too large to use. If good constants cannot be obtained, zone II has to go down to smaller radii with boxes of geometric size, which costs more but changes nothing else.
2. **The literature inputs L1 and L3 are at SESSION scope.** A certificate built on them is a SESSION result for review, as the decision rule says. A theorem-grade statement in the DSN would need them as claim-level imports with LIT's validation. That is a later decision. If LIT finds that Theorem 4.2(3) does not cover a convergent invariant graph as used in §5 step 6, a uniqueness proof of our own (the withdrawn P2, with moving-base estimates) would be needed.
3. **Sampling can miss a narrow violation,** most likely near the outer edge of D₀, where \|E\|/R is largest. The remedy is a smaller target radius. At \|ξ*\| = 0.35 or 0.30 the jump is 10⁻¹³ or 10⁻²³ and still far above the attainable width, because the orbit can be followed to smaller radius, where the tube is thinner.
4. **The guard property is sampled on a grid only.** A thin tongue of the wedge set inside the guard zone would break the locality argument. The interval cover of P7 and P8 has to exclude it.
5. **Inverse branch.** G is evaluated here by Newton iteration. A certificate needs a validated inverse on each box and at each step of the second leg (pilot design E1). The map is close to the identity there, so this is routine but not written.
6. **One overlap, one branch.** The design certifies S₀ ∩ S₁ of Γ₊ only. It gives no information on the second T²-class.
7. **The tube centre must be the exact truncation.** The control SHIFTCOEF shows it: a relative change of 10⁻⁶ in a₅ breaks (B) near 0. So P5 has to give enclosures from the exact recursion, and zone I has to use the exact vanishing order of the truncation defect.

## 10. What is asked

- **Co-owner:** a read-back of the changed parts only: §3 (local domains, guard, families), §4 (hypotheses, inward property, seed), §5 steps 2, 3, 5 and 6, §6. The sampling campaign need not be replayed for the proof plan; the new gates are GUARD0, GUARD1, STEP and XISTAR.
- **PI, after the read-back:** whether this design is accepted as the basis for stage 3c. A separate decision is whether to authorize stage 3c itself.

Nothing in this record changes the DSN, a RID, a grade or an OPEN status.

## 11. Review of r1 and the changes in r2

Co-owner review `5858511915` on PR #218 (head `3014b93`): REVISE. The conditional Rouché step was found sound; the domain, the seed, the uniqueness argument, the arc and the transport step were not yet a proof plan.

| Item | Finding | Change in r2 |
|---|---|---|
| R1 (blocking) | D₀ as written is not local: with Re κ > 0 the wedge conditions hold again for large \|ξ\|, e.g. at arg ξ = π/12, \|ξ\| = 1000. (Q) cannot hold on such a set, and (A) did not control an outer boundary | §3: bounded chart sectors with fixed log branches; guard property (G); families with one moving wall; locality. §4: (A) split into (A1) and (A2); the inward property is derived from (G), (A1), (A2) for the whole fibre and every wall; the seed (Q1)–(Q3). The owner confirmed the finding in an exploratory scan: the conditions hold again from \|ξ\| ≈ 0.7 |
| R2 (blocking for the divergence step) | Rouché gives the unique extension of the seed, not uniqueness of all invariant graphs in the tube; the sketched growth argument ignored the moving base | The tube-uniqueness claim is withdrawn (P2). §5 step 6 uses López-Hernanz 2012, Theorem 4.2(3), as the co-owner proposed: a convergent branch gives a graph in 𝓗_Δ, hence S = u_j on each petal. New obligation L3; LIT is asked to validate the use |
| R3 | The common arc was a 29-point sample | §5 step 2 and P9: analytic existence for large t (injectivity of τ on a region convex in ξ⁻³), validated continuation on the compact part, U as a neighbourhood of the arc. With one moving wall, the arc's tail lies in both seed domains, which the divergence step needs |
| R4 | SEP is a pointwise derivative along one orbit, not an enclosure of the unknown values | §5 steps 3 to 5 and P10: nested fibre discs with inclusion of the whole fibre image, interval derivative with moving base, exclusion, listed error sources, and the two-disc test \|c₁ᴮ − c₀ᴮ\| > r₀ + r₁ in one coordinate. SEP is labelled an estimate |
| R5 | The D₁ grid stopped at 0.398 below \|ξ*\|; no gate at ξ* | Gate XISTAR at ξ* with 64 directions; radii added up to 0.595; gates GUARD0, GUARD1, STEP. The added radii exposed the outer edge of D₀, where \|E\|/R exceeded the gate; R(ξ*) was raised to 2·10⁻³ (§7, parameter history). The co-owner's independent values at ξ* are reproduced (§7) |

Unchanged: the target (one branch, one overlap, \|ξ*\| = 0.40), the `[NUM]` status of every number, and the absence of any certification.

## 12. Read-back of r2 and PI decision

**Co-owner read-back** (review `5858796744` on PR #218, head `106161b`; changed parts only; no rerun of the sampling): **ACCEPT as a scoped written design for the PI's decision; not a certificate and not an authorization of stage 3c.**

| Item | Verdict | Remaining obligation |
|---|---|---|
| R1 local domains | fixed at design level | (G), (A1), (A2) are sampled only; their proof for all points is P3, P7, P8. P9 must prove (Q1) and the continuity of the branches |
| R2 uniqueness | correct route, conditional | L3. The co-owner read Theorem 4.2(3) in LIT's verified transcription of the published version: the uniqueness is for any parabolic curve in the class 𝓗_Δ on a sufficiently small petal, not only for fixed points of the operator. Still to be shown: the convergent graph is a parabolic curve in that sense, and the hypotheses for G in the rotated chart. The LIT request stays open |
| R3 common arc | fixed as an obligation | P9: explicit derivative and image estimates; validated compact continuation |
| R4 transport | fixed as a certificate algorithm | P6, P8, P10: m_k > 0; validated image and inverse on all enclosures (added to §5 step 3) |
| R5 sampling | gates included, `[NUM]` only | nothing between samples is certified; P7 and P8 must exclude thin violations |

**Provenance note from the read-back.** The recorded values at ξ* are the committed ones: margins 6.5962 (D₀) and 6.0298 (D₁), with R(ξ*) = 2·10⁻³. The values 6.80 and 6.22 that appeared in a session message belong to the comparison run with `--rstar 1e-3` (§7), which is not a recorded output.

**Conditions before a certification run can claim anything** (co-owner; the owner agrees):
1. LIT's verdict on L3, or an independent proof with the precise parabolicity hypotheses for F and G.
2. A quantified proof of the seed (Q1, Q2) and the full zone-I bounds.
3. A certified guard property and interval cover of (A) and (B) on zone II for both chart sectors, including ξ* and the walls.
4. The certified analytic tail of the common arc and its validated compact continuation.
5. Rigorous complex-interval transport and inverse with m_k > 0, and disjoint enclosures.

**PI decision, 11 November 2026, 15:52 (UTC+3), in the owner session:** "Stage 3b r2 tüp rotasının, \|ξ*\| = 0.40 hedefli Stage 3c sertifika tasarımının temeli olarak scoped kabulü uygundur." (The r2 tube route is accepted, scoped, as the basis of the stage-3c certificate design aimed at \|ξ*\| = 0.40.)

Scope of the acceptance, as the read-back states it:
- it does not authorize a stage-3c run;
- it does not discharge L3 or P1, P3 to P11;
- it proves no nonzero jump and no divergence;
- B-an and B-6 stay ACTIVE; no DSN text changes.
