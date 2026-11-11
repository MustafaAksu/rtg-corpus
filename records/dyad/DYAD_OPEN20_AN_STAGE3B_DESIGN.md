# DYAD OPEN 20 (analytic branch) — stage 3b: design of a certificate for one nonzero sectorial jump

**Date:** 11 November 2026. **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION). A written design with `[NUM]` feasibility sampling. Nothing is certified, no result is claimed, and no certification run was made.
**Authority:** item 2 of the order of work in `records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md` §9 (the "pilot design" below). Target agreed by the co-owner and the owner on 11 November 2026: one jump, first at \|ξ*\| = 0.40. Stage 3c (certification) is not authorized. Scouting of the second overlap class is not authorized.
**Governing edition:** DYAD v6.4.24 (`dyad-v6.4.24`). OPEN 20 B-an and B-6 are ACTIVE.
**For:** co-owner review, then a PI decision (§10).

## 0. Outcome in one paragraph

The design replaces the operator route (pilot design §4, E3–E6) by a **tube route**. Each sectorial curve is shown to lie in an explicit thin tube around a truncated series, over an explicit wedge that reaches from 0 to the common point ξ*. The proof needs two pointwise inequalities for one step of the map, (A) and (B) in §4, and the published existence of the curves near 0. The dynamics then sharpens the tube at ξ* by three to four orders of magnitude per leg, so two enclosures at ξ* can be separated. Sampling at 770 and 760 points finds both inequalities satisfied, with margins equal to what the leading normal form predicts, on wedges that reach \|ξ*\| = 0.40. The sampled width of the final enclosure is about 10⁻⁷ of the jump measured in stage 2b. The sampling is `[NUM]` and bounds nothing between its points. What remains is listed as proof obligations in §6; the main ones are the analytic estimate near 0 and the interval verification of (A) and (B).

## 1. What a certificate would state

Notation as in the pilot design: pilot branch Γ̂₊ of F = T⁶ with formal series w = Σ a_k z^k, ξ = c₊z, lifted coordinate w = z²(a₊ + y), Y = y − b₁x, common point ξ* = 0.40·e^{iπ/6}. G is the local inverse of F at 0.

**Claim C (target of stage 3c; not claimed here).**
- **C1.** There are open sets D₀, D₁ and analytic functions φ₀ on D₀ and φ₁ on D₁ such that:
  - the graph of φ₀ is invariant under F, and the graph of φ₁ under G;
  - near 0, φ₀ is the invariant curve that López-Hernanz 2012 attaches to the attracting petal of F around arg ξ = 0, and φ₁ the one attached to the attracting petal of G around arg ξ = π/3. Both have Γ̂₊ as asymptotic expansion.
- **C2.** D₀ ∩ D₁ contains a connected open set U with ξ* ∈ U and 0 in its closure.
- **C3.** φ₁(ξ*) − φ₀(ξ*) ≠ 0, with an interval enclosure that excludes 0.

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
- Along the attracting direction of F the curve is transversally expanding (Re α = −102/19 < 0). A normally expanding invariant curve is the set of points whose forward orbits stay near it. That gives existence on a larger domain, uniqueness in a tube, and a sharp shooting condition, all from the same inequality.
- The jump is large where the map is still close to its normal form in the right coordinates. At \|ξ*\| = 0.40 it is about 2·10⁻⁸ in the lifted unit, so no high precision is needed.
- The local theory is used only qualitatively: existence and asymptotics near 0. No constant of the published proofs enters.

## 3. Objects

All objects are explicit elementary functions of ξ. Numbers below are `[NUM]` values from the sampling run.

- **Truncated series.** φ_N(z) = Σ_{k=2..N} a_k z^k with N = 40. Normal deviation in the lifted unit: d = (w − φ_N(z))/z².
- **Fatou coordinate, four terms.** τ(ξ) = A₃z⁻³ + A₂z⁻² + A₁z⁻¹ + κ log z with z = ξ/c₊. It is the truncation of the formal Fatou coordinate of the restricted map on the series curve (stage 2b): A₃ = −1/(3ℓ₊) ≈ −3.328 − 0.682i, A₂ ≈ 0.537 + 1.611i, A₁ ≈ −0.135 + 0.154i, κ ≈ 1.812 + 0.090i. One step of F changes τ by about +1, one step of G by about −1. τ* = τ(ξ*) ≈ −1.693 − 4.082i.
- **Wedge functionals.** h₀(τ) = Re(e^{iθ₀}τ) and h₁(τ) = Re(−e^{−iθ₀}τ), with θ₀ = π/2 − η₀ and η₀ = π/8. Under τ ↦ τ + 1, h₀ grows by sin η₀; under τ ↦ τ − 1, h₁ grows by sin η₀.
- **Wedges.** With s₀ = Re τ* − 0.25, s₁ = Re τ* + 0.25, c₀ = h₀(τ*) − 0.15, c₁ = h₁(τ*) − 0.15:
  - D₀ = {Re τ > s₀, h₀(τ) > c₀}, for F;
  - D₁ = {Re τ < s₁, h₁(τ) > c₁}, for G.
  - Both contain the half-line τ = Re τ* − it, t ≥ −Im τ*, which starts at τ* and runs to ξ → 0.
  - Nested families for the induction: D₀(c) = {Re τ > s₀ + (c − c₀), h₀ > c} for c ≥ c₀, and the mirror family D₁(c).
- **Tube radius.** With q₁ = q₂ = 9 and ε fixed by R(ξ*) = 10⁻³:
  - R₀(ξ) = ε\|ξ^α\|·(Re τ − s₀ + 1)^{−q₁/3}·h₀(τ)^{−q₂/3} on D₀;
  - R₁(ξ) = ε\|ξ^α\|·(s₁ − Re τ + 1)^{−q₁/3}·h₁(τ)^{−q₂/3} on D₁.
  - \|ξ^α\| is the leading normal multiplier accumulated along an orbit. The two other factors make the tube shrink along orbits faster than the normal dynamics, with a relative gain of (q₁/3)/(first functional) + (q₂/3)·sin η₀/(second functional) per step. Call this the model gain.
- **Tubes.** V₀ = {ξ ∈ D₀, \|d\| ≤ R₀(ξ)}, and V₁ likewise.

## 4. The tube lemma

Stated for F on D₀; the statement for G on D₁ is the same with G, D₁(c), R₁. Points are written in the coordinates (ξ, d), so the truncated series is d = 0 and a curve is a function d = δ(ξ). Write (ξ′, d′) for the image of (ξ, d) under the map, E(ξ) = d′(ξ, 0), μ₀(ξ) for the derivative of d′ in d at d = 0, and nl(ξ) = sup over \|d\| = R(ξ) of \|d′ − E − μ₀d\| / (\|μ₀\|R(ξ)).

**Hypotheses.**
- **(A) Inward base motion.** There is σ > 0 such that, for every c ≥ c₀ and every point of the tube over D₀(c), the base point of the image lies in D₀(c + σ).
- **(B) Strong exit inequality.** For every ξ ∈ D₀: \|μ₀\|(1 − nl)·R(ξ) − \|E(ξ)\| > sup of R(ξ′) over the fibre \|d\| ≤ R(ξ).
- **(Q) Start.** For some c₁, there is an analytic function δ on D₀(c₁) whose graph is F-invariant and lies in the tube (\|δ\| ≤ R₀).

**Conclusion.** There is exactly one analytic δ₀ on D₀ that extends the function of (Q), has an F-invariant graph and satisfies \|δ₀\| < R₀. In the raw chart it is φ₀(z) = φ_N(z) + z²δ₀(c₊z). For every ξ ∈ D₀, δ₀(ξ) is the only point of the closed tube fibre whose image lies on the graph of δ₀.

**Proof sketch** (to be written out in the proof record of 3c).
1. *One step outward.* Let δ be analytic on D₀(c) with invariant graph in the tube, and let ξ ∈ D₀(c − s) with 0 < s ≤ σ. By (A), every point of the fibre over ξ is mapped over D₀(c). So Ψ(d) = d′(ξ, d) − δ(ξ′(ξ, d)) is analytic on the closed fibre disc \|d\| ≤ R(ξ). Its zeros are the points of the fibre that are mapped onto the graph of δ.
2. Put Ψ₀(d) = d′(ξ, d). On the fibre circle, \|Ψ₀\| ≥ \|μ₀\|(1 − nl)R − \|E\|, and \|Ψ − Ψ₀\| = \|δ(ξ′)\| ≤ R(ξ′). By (B) and Rouché's theorem, Ψ and Ψ₀ have the same number of zeros in the disc. By the same inequality Ψ₀ differs from the linear function μ₀d by less than \|μ₀\|R on the circle, so Ψ₀ has one zero. Hence Ψ has exactly one zero δ̃(ξ).
3. δ̃ is analytic in ξ (a simple zero of an analytic family). It equals δ on D₀(c), since δ(ξ) is a zero and cannot lie on the circle. Its graph is invariant by construction.
4. *Induction.* Start from (Q) at c₁ and go down to c₀ in finitely many steps.

**Where (Q) comes from.** López-Hernanz 2012, Theorem 4.2 and Corollary 5.2, applied to F and to G: the invariant curve of each petal exists on a petal domain and has Γ̂₊ as Gevrey asymptotic expansion on closed subsectors. For large c, D₀(c) lies in such a subsector. There R₀ ≥ const·\|ξ\|^{Re α + q₁ + q₂} = const·\|ξ\|^{12.6}, and the curve differs from φ_N by O(\|ξ\|^{N−1}) = O(\|ξ\|³⁹) in the lifted unit. So the curve is in the tube near 0.
- LIT checked the deductions of this chain (owner assessment §5; INF-005 to INF-008). It is at SESSION scope in the Dyadic records and is not a theorem-grade import.

**Uniqueness in the tube** (needed in §5, step 6). Two F-invariant analytic graphs in the tube over D₀(c) coincide. Reason: along an orbit the ratio of their difference to R₀ grows at least by the factor 1 + (model gain) per step. The product of these factors diverges, because the gains decay like 1/n, while the ratio is at most 2. So the difference is 0. This needs (B) in a slightly larger tube and a Cauchy estimate. It is a proof obligation (§6, P2).

## 5. From the lemma to the certificate

1. **Curves.** The lemma for (F, D₀, R₀) and for (G, D₁, R₁) gives φ₀ and φ₁. This is C1.
2. **Common domain.** The preimage under τ of the half-line of §3 is an arc from ξ* to 0 inside D₀ ∩ D₁. U is the component of D₀ ∩ D₁ that contains it. This is C2.
3. **Value of φ₀ at ξ*.** The orbit of (ξ*, φ₀(ξ*)) under F stays on the graph, so after n steps its deviation is at most R₀(ξ_n). Along the orbit the normal direction expands. So the points of the fibre over ξ* that are still in the tube after n steps lie in a disc B₀ of radius about 2R₀(ξ_n)/(amplification). A validated computation encloses B₀: an interval Newton step for the shooting function near a numerical value, and a lower bound for the derivative on the rest of the fibre.
4. **Value of φ₁ at ξ*.** The same with G in place of F gives B₁.
5. **Separation.** If B₀ and B₁ are disjoint, C3 holds.
6. **Divergence.** Suppose Γ̂₊ converges, with sum S on \|ξ\| < r.
   - The graph of S is invariant under F and G near 0, and S − φ_N = O(\|ξ\|³⁹). So for large c the graph of S over D₀(c) lies in the tube, and S = φ₀ there by uniqueness in the tube.
   - By the identity theorem S = φ₀ on D₀ ∩ {\|ξ\| < r}, and in the same way S = φ₁ on D₁ ∩ {\|ξ\| < r}.
   - So φ₀ = φ₁ on U near 0, hence on U, hence at ξ*. This contradicts C3.

The enclosure of step 3 is far below the jump because the tube is thin where the orbit ends, not because the tube is thin at ξ*. At ξ* the tube has radius 10⁻³, which is 5·10⁴ times the jump.

## 6. Proof obligations

| # | Obligation | Kind | State |
|---|---|---|---|
| P1 | Tube lemma, full proof (§4) | analytic | sketched here |
| P2 | Uniqueness of invariant graphs in the tube | analytic | idea only |
| P3 | **Zone I:** (A) and (B) for \|ξ\| ≤ ρ₀, from explicit bounds of the lifted map on a polydisc | analytic, with constants from P6 | **open; the main analytic work** |
| P4 | Divergence argument (§5, step 6), including connectedness of D_j ∩ {\|ξ\| < r} | analytic | sketched here |
| P5 | Enclosures of a₂ … a₄₀ | computer-checked (ball arithmetic, exact recursion) | stage 2 has `[NUM]` values |
| P6 | Bounds of the lifted map and of its inverse branch on a polydisc; lower bound for \|1 + x³G\| (pilot design E1, E2) | computer-checked | tooling exists (bounds preflight); constants to be recomputed on the right polydisc |
| P7 | **Zone II:** (A) and (B) on a box cover of D₀ ∩ {\|ξ\| ≥ ρ₀}, for F | computer-checked (interval arithmetic) | **open; the main computation** |
| P8 | The same on D₁ for G, with a validated inverse on each box | computer-checked | open |
| P9 | Branch and domain bookkeeping: the sector on which τ and ξ^α are defined, the arc of §5 step 2, injectivity of τ near 0 | computer-checked and analytic | open; small |
| P10 | Shooting enclosures B₀, B₁ and their separation | computer-checked | sampled (§7, SEP) |
| P11 | Negative controls of the certificate: the zero-jump vector-field model must give an enclosure containing 0; wrong branch; wrong log branch; perturbed α (pilot design §5) | computer-checked | the zero-jump harness exists (stage 2b) |
| L1 | (Q): existence and asymptotics near 0, for F and for G | literature | SESSION scope; LIT-checked chain |
| L2 | Lemma 5b-1 (P1-c-5), for the step to log F | existing SESSION lemma | unchanged |

The tube lemma holds on any family of sets for which (A) and (B) hold. The wedges, the exponents and R(ξ*) are design choices; a certification run may change them if an interval check fails somewhere.

## 7. Feasibility sampling (`[NUM]`, OWNER-RUN)

**Package.** Script `evidence/dyad/scripts/dyad_open20_an_stage3b_tube_sampling.py` (SHA-256 `a4ca55b6927538989e5da0efec5c9b6b8064b43f7eb545e9162b1c0cb97fd037`); run `evidence/dyad/open20-an/stage3b-design/run.sh`; outputs and `SHA256SUMS.txt` in the same folder (`tube_sampling.json` `53374a14…5493`). Inputs: the stage-2 coefficients (`6ca8c663…477e`) and the stage-2b output (`610433e5…a268`).

**What it does.** It evaluates the full map F, and a numerical inverse G, at 100 digits on a polar grid: 42 radii from 0.01 to 0.44 and 65 arguments. At each grid point inside a wedge it computes E, μ₀, nl on eight points of the fibre circle, and the two sides of (A) and (B). It computes no sectorial value and no jump.

**Limits.** Sampling is not a bound. Nothing is known between the points. No interval arithmetic is used. The numbers show that the inequalities are plausible and how large the margins are; they prove nothing.

**Result** (all gates PASS; the controls SWAP and SHIFTCOEF each exit 1 at the named gates):

| Quantity | D₀ with F | D₁ with G |
|---|---|---|
| sample points | 770 | 760 |
| largest \|ξ\| in the wedge | 0.437 | 0.398 |
| (A): smallest gain of the first, second functional | 0.948, 0.312 | 0.966, 0.352 |
| (B): smallest margin | 1.48·10⁻⁵ at \|ξ\| = 0.01 | 1.47·10⁻⁵ at \|ξ\| = 0.01 |
| (B): smallest margin / model gain | 0.9999 | 1.0000 |
| largest \|E\|/R | 0.034 | 2.9·10⁻⁵ |
| largest nl | 3.6·10⁻³ | 3.3·10⁻³ |

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

**Reading.**
- The margin follows the model gain down to \|ξ\| = 0.01 and exceeds it at larger radii. It decays like \|ξ\|³, as the gain per step should. This is what an analytic proof near 0 has to reproduce (P3).
- The wedge functionals gain nearly their model values (1 and sin η₀ = 0.383) everywhere. So the four-term Fatou coordinate is good enough up to \|ξ\| = 0.44. The leading term 1/(3ξ³) alone is not: in an exploratory run, which is not part of the package, its step error was 0.5 to 0.7 at \|ξ\| = 0.40.
- The truncated series is well inside its tube: \|E\|/R ≤ 0.034, reached at the outer edge of D₀.

**Common arc** (gate PATH). The arc Re τ = Re τ* was followed from ξ* to −Im τ = 3000. \|ξ\| decreases from 0.40 to 0.047 and arg ξ moves from π/6 to 0.1634π.

**Last step** (gate SEP; n = 334 steps, as in stage 2b).

| Leg | Tube radius at the far end | Factor along the leg | Contribution to the width at ξ* |
|---|---|---|---|
| φ₀: F from ξ* to \|ξ\| = 0.0961 | 6.9·10⁻¹³ | amplification 1711 | 8·10⁻¹⁶ |
| φ₁: from \|ξ\| = 0.0986 on the S₁ side to ξ* | 7.3·10⁻¹² | contraction 1.18·10⁻⁴ | 1.7·10⁻¹⁵ |

Estimated total width 2.5·10⁻¹⁵, against \|Δ_Y\| = 1.95·10⁻⁸ from stage 2b: a ratio of 1.3·10⁻⁷. The validated transport therefore needs only crude derivative bounds.

**Two controls that were tried and dropped.**
- A tube with \|ξ^{−α}\| in place of \|ξ^α\| still passes on these wedges. So it is not a negative control: on these wedges the decay factors carry the inequality, and the factor \|ξ^α\| only makes the margin equal to the model gain.
- q₁ = q₂ = 0 gives a tube whose radius grows without bound as ξ → 0. The run did not finish and was stopped.

**Parameter choice.** The script has exploration options (`--q`, `--rstar`, `--eta-div`, `--dc`, `--ds`); the recorded run uses the defaults.
- With q₁ = q₂ = 12 and R(ξ*) = 10⁻⁴ the full grid gave \|E\|/R = 1.2 at the outer edge of D₀. The tube was thinner than the truncation defect there, so the gate failed.
- The recorded parameters q = 9, R(ξ*) = 10⁻³ are the first set that passed on the full grid.
- With η₀ = π/6 the wedge reaches \|ξ\| = 0.48, where N = 40 is no longer adequate. η₀ = π/8 was chosen for that reason.

## 8. What stage 3c would consist of (not authorized; for the decision)

1. **Proof record:** P1 to P4 written out, with the constants that P6 supplies.
2. **Certificate script** with fixed command, JSON output with hashes, and the controls of P11:
   - P5 and P6: coefficient enclosures and map bounds;
   - P7 and P8: zone II. A box cover of the two wedges for ρ₀ ≤ \|ξ\| ≤ 0.44, with boxes of a few per cent relative size, is of the order of 10⁴ to 10⁵ boxes per wedge. Each box needs one interval evaluation of the map with its first derivatives. At small radius the margin is of order \|ξ\|³, so the evaluation has to use a centred form;
   - P10: two legs of 334 steps.
3. **Receiving review** with an independent replay.

**Cost (owner estimate, not measured).** Minutes to about an hour of `python-flint` computation, no special hardware, precision of 100 to 200 digits. It can run in the repository workspace or on the PI's machine.

**Choice of ρ₀.** The sampled margin equals the model gain already at \|ξ\| = 0.1. A zone I up to ρ₀ between 0.05 and 0.1 is the working assumption. It depends on the constants of P6 and is not verified.

## 9. Open points and risks

1. **Zone I is not sampled as a proof.** The analytic estimate needs bounds of the lifted map on a polydisc of radius about 0.1. The earlier preflight used a Cauchy radius of 0.002 and gave constants too large to use. If good constants cannot be obtained, zone II has to go down to smaller radii with boxes of geometric size, which costs more but changes nothing else.
2. **The literature input (Q) is at SESSION scope.** A certificate built on it is a SESSION result for review, as the decision rule says. A theorem-grade statement in the DSN would need (Q) as a claim-level import with LIT's validation. That is a later decision.
3. **Sampling can miss a narrow violation,** most likely near the outer edge of D₀. The remedy is a smaller target radius. At \|ξ*\| = 0.35 or 0.30 the jump is 10⁻¹³ or 10⁻²³ and still far above the attainable width, because the orbit can be followed to smaller radius, where the tube is thinner.
4. **Inverse branch.** G is evaluated here by Newton iteration. A certificate needs a validated inverse on each box (pilot design E1). The map is close to the identity there, so this is routine but not written.
5. **One overlap, one branch.** The design certifies S₀ ∩ S₁ of Γ₊ only. It gives no information on the second T²-class.
6. **The tube centre must be the exact truncation.** The control SHIFTCOEF shows it: a relative change of 10⁻⁶ in a₅ breaks (B) near 0. So P5 has to give enclosures from the exact recursion, and zone I has to use the exact vanishing order of the truncation defect.

## 10. What is asked

- **Co-owner:** review of the lemma and of the divergence argument (§4, §5), of the list of obligations (§6), and a replay of the sampling package (§7).
- **PI, after the review:** whether this design is accepted as the basis for stage 3c. A separate decision is whether to authorize stage 3c itself.

Nothing in this record changes the DSN, a RID, a grade or an OPEN status.
