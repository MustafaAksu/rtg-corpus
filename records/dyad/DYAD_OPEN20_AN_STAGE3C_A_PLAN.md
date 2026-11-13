# DYAD OPEN 20 (analytic branch) — stage 3c-a: work plan and certificate architecture

**Date:** 11 November 2026. **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION). A plan and its progress log. It claims no result.
**Authority:** PI decision of 11 November 2026, 15:59 (UTC+3), in the owner session: "3c-a ile başlayalıp neticelendirelim sonrasını daha sonra değerlendiririz." Stage 3c-a is the proof record and the certificate script, with no certification claim. Stage 3c-b (the certification run and its receiving review) is **not** authorized.
**Basis:** `records/dyad/DYAD_OPEN20_AN_STAGE3B_DESIGN.md` r2 (accepted by the PI as scoped basis, §12 there). Obligation numbers P1–P11, L1–L3 are those of its §6.
**Governing edition:** DYAD v6.4.24. OPEN 20 B-an and B-6 are ACTIVE.

## 1. What 3c-a delivers, and what it does not

- **Delivers:** (a) a proof record for the analytic obligations P1, P3, P4 and the analytic parts of P9; (b) a certificate script for P5–P11, with its negative controls, developed and tested.
- **Does not deliver:** a certificate. Test runs made while the script is developed are development runs. They are recorded as such, and no statement about the jump, about divergence, or about B-an and B-6 is drawn from them. A certificate exists only after 3c-b: fixed command, recorded outputs with hashes, independent replay, review, PI decision.
- **Stop rule.** If an obligation cannot be met with the accepted design (for example an inequality that fails on a box and cannot be repaired by subdividing or by a parameter change within §3 of the design), the work stops there and reports it.

## 2. Architecture of the certificate

### 2.1 The cancellation problem

F = T⁶ is the identity plus terms of order four on the curve. A ball evaluation of F on a box loses these terms: the box radius is much larger than \|x\|⁴. So nothing may be computed as "F on a box minus the identity".

### 2.2 Power series along the curve

The tube lemma needs the map only on the tube, at points (z, w) = (x, φ_N(x) + x²d) with small d. Along d = 0 every one-step quantity is a function of the single complex variable x, and F is entire. The certificate therefore represents these functions by their power series in x at x = 0:

- ball coefficients, computed by acting with the six steps of T on series (the routine of stage 2);
- a truncation degree D and a rigorous tail bound from a Cauchy estimate on a larger circle;
- the dependence on d as a jet in d: first and second order exactly, the rest by a remainder constant (a Taylor model in d on a torus, and the maximum principle; §5, W2b).

The cancellation is then exact: the low coefficients vanish identically. For example Z(x) = F_z(x, φ_N(x)) = x + ℓx⁴ + …, so g(x) = Z(x)/x − 1 is a series that starts at x³.

In the lifted chart of the pilot design D2 (x′ = x(1 + g), u = w/x², d = u − û(x) with û = φ_N/x²), the quantities of the lemma are cancellation-free expressions in such series:

| Quantity | Expression |
|---|---|
| relative step, (A2) | x′/x − 1 = g |
| increment of the Fatou coordinate, (A1) | τ(x′) − τ(x) = (g/x³)·[−A₃(3 + 3g + g²)/(1 + g)³ − A₂x(2 + g)/(1 + g)² − A₁x²/(1 + g) + κx³·log(1 + g)/g] |
| normal multiplier μ₀ | the first-order d-jet of d′ |
| ratio of tube radii | R(x′)/R(x) = \|(1 + g)^α\|·(first′/first)^{−q₁/3}·(second′/second)^{−q₂/3}, with the increments of the functionals from the line above |
| truncation defect E | its own series: the raw defect W − φ_N(Z), divided by x′² |

On a box, a series is evaluated by a Taylor shift to the box centre; this is accurate also where the terms of the series cancel.

### 2.3 The truncation defect

a₂ … a_N are the exact formal coefficients; the certificate knows them as balls. So the raw defect W(x) − φ_N(Z(x)) vanishes at 0 to order N + 4 = 44, and the lifted defect to order N + 2 = 42. In the series the lower coefficients come out as tiny balls around 0; by this structural fact they are exactly 0 and are set to 0.

### 2.4 Zones

- **Zone II** (ρ₀ ≤ \|ξ\| ≤ 0.60, the whole chart sector): rectangles in (log\|ξ\|, arg ξ), each covered by one disc in x (a *piece*). A piece is *out* (a wedge condition fails on all of it) or *pass* (it lies in the guard core, and (A1), (A2), (B) hold for every point of it that satisfies the wedge conditions). The walls are not located: the functionals enter only through first ≥ 1, second ≥ c_j and their upper bounds on the piece. A piece that is neither is cut into four; the first piece that is neither at the largest depth ends the run with a failure. If all pieces are out or pass, (G) holds on the covered part and (A1), (A2), (B) hold on D_j there (§5, W3).
- **Zone I** (0 < \|ξ\| ≤ ξ₀ = 0.05): no cover. The hypotheses are reduced to inequalities between constants: sup bounds of the series on one disc at 0, elementary bounds of τ, of the functionals and of the tube radius, each inequality divided by the power of \|x\| it scales with (`zone1_check`, with the derivation in its header; §5, W4). The seam with zone II is the circle \|ξ\| = 0.05, which both zones contain.

### 2.5 The inverse map, the legs and the arc

- **Inverse map (for D₁): a local inverse from the forward series.** The first plan, the series of F⁻¹ along the curve by formal inversion, was computed and set aside (2.6). The inverse step is now taken from the forward series by a local inverse lemma (`inverse_conditions` in the library, with its proof in the docstring):
  - for a target set B′ × {\|d′\| ≤ R′} it gives a disc B and a fibre radius ρ such that every target point has exactly one preimage in B × {\|d\| < ρ} (Rouché in d, then Rouché in x);
  - the quantities of the inverse step on B′ are the forward quantities on B × {\|d\| ≤ ρ}: x/x′ − 1 = −g̃/(1 + g̃) and τ(x) − τ(x′) = −Δτ, both free of cancellation;
  - the tube lemma of the design is not changed. This is the way obligation P8 ("validated inverse on each box") is met.
  - *For the proof record (W7):* that the local inverses over the pieces of D₁ are one branch of F⁻¹; and the form in which (B) for G is checked on B (W3 fixes it).
- **Legs (P10):** the nested fibre discs of the design §5 step 3, with one-step enclosures from the same series and the interval Jacobian in (x, d).
- **Arc (P9):** validated continuation of τ(γ(t)) = Re τ* − it on the compact part; the tail by the analytic estimate of the proof record.

### 2.6 Tried and set aside

**Second-order Taylor forms on boxes in (x, u).** The first engine carried value, gradient and Hessian through the six steps on each box and used f(c + h) ∈ f(c) + ∇f(c)h + ½hᵀ Hess f(B) h. Its enclosures were sound in every test (sampled points inside), but far too wide:
- with the steps carried in the coordinates (ρ, η), the Hessian balls grow by about 2.7 per step;
- with the steps carried in the diagonal coordinates (z, w), the growth is smaller, but at a relative box size of 0.5% the enclosure of G still has a relative radius of 1.4% to 7%, and that of H_u exceeds 100%, at every \|x\| ≤ 0.5;
- the cause is structural: the quotients are of order \|x\|⁴ and \|x\|⁵ against steps of order 1, so a form of order two cannot be uniform in scale. Order four or more would be needed, in two variables.
The series of 2.2 replace it. The code of the first engine is not kept.

**Power series of the inverse map along the curve.** Computed by formal inversion (Newton iteration on series for each inverse step of T; in a test at degree 120, F applied to the result gave back the curve to 10⁻¹⁶⁹). Its coefficients grow (`[NUM]`, §5 W2b): the ratio of successive coefficients is 1.13 at degree 240, which points to a radius of convergence of about 0.88 in x (\|ξ\| ≈ 0.41). D₁ needs \|x\| up to 0.91 (\|ξ\| = 0.42), and a Cauchy tail needs a larger circle still.
- A growing coefficient sequence is an observation, not a proof of the radius. It is enough to drop the route: no tail bound is available where it is needed.
- A likely reason: T⁻¹ is not entire (the inverse step solves a transcendental equation for η), so the inverse series has singularities at finite distance. F itself is entire, and its series converge on every circle.
- `inverse_curve` stays in the library only so that the check reproduces the observation. The second-order jets of the inverse were also built and are removed.

## 3. Work packages

| # | Package | Obligations | State |
|---|---|---|---|
| W1 | Engine, first part: constants, coefficient balls, series of the map and of the defect along the curve | P5 | **done as a development check** (§5) |
| W2a | Jets in d (first order), order-zero series, Cauchy constants and tails, Taylor-shift evaluation on discs, the one-step quantities of 2.2 for F | P6 | **done as a development check** (§5) |
| W2b | Second-order jets in d; remainder in d beyond second order; one step on a tube piece; local inverse from the forward series | P6, method for P8 | **done as a development check** (§5) |
| W3 | Zone II verification with adaptive pieces, for F on Ω₀ and G on Ω₁ (through the local inverse), including the guard property | P7, P8 | **done as a development check** for 0.05 ≤ \|ξ\| ≤ 0.60 (§5); gluing of the local inverses open (§4) |
| W4 | Zone I: reduction of (G), (A1), (A2), (B) and of the local inverse lemma to constant inequalities; seam with zone II | P7, P8 | **done as a development check** (§5) |
| W5 | The common arc: validated continuation on the compact part, one constant inequality for the tail, the link, both inside the guard cores | P9 | **done as a development check** (§5) |
| W6 | Legs and the two-disc test; controls (zero-jump model, perturbed α, wrong log branch; wrong branch not built) | P10, P11 | **script done and tested in a development run** (§5); method differs from the design's step 3 (§4) |
| W7 | Proof record `DYAD_OPEN20_AN_STAGE3C_A_PROOF_RECORD.md`: structural facts (exact), remainder in d, local inverse and one inverse branch, the Rouché step with the zero count, zone II and zone I, the arc, the legs, rounding | analytic parts of P3, P9; soundness of P6–P10 | **written, not yet reviewed** (§5); the seed (Q), P1, P4 and the divergence step are not rewritten: they wait for L1–L3 |
| W8 | Hand-over `DYAD_OPEN20_AN_STAGE3C_A_HANDOVER.md`: package, fixed parameters and commands, state of the obligations; the legs in the form the proof covers; strict SND; machine checks of the float bounds; control "wrong branch" | P10, P11; hand-over | **done as a working record with development runs** (§5); 3c-b is the PI's decision |

LIT's answer on Theorem 4.2(3) (L3; `pipes/LIT/20261111-DYAD-lh2012-thm42-uniqueness-use.md`) is awaited. It does not block W1–W6.

## 4. Progress log

- **11 Nov 2026.** Plan written. A first engine (Taylor forms on boxes) was built, tested and set aside (2.6). The series engine was started; W1 is done as a development check (§5). PR #220, co-owner review `5859686051` (ACCEPT as a development record), merged as `d730738`.
- **11 Nov 2026, W2a.** Jets in d, order-zero series, tails, disc evaluation and the one-step quantities for F (§5). Two points of the W1 review are built in:
  - *Tails are proved, not read off the coefficients.* The observed coefficient roots (about 0.77) are not used. Each series has a Cauchy constant from a rigorous sup bound on the circle \|x\| = 1.10, and the tail on \|x\| ≤ r is at most M(r/X)^{D+1}/(1 − r/X).
  - *Zeros by structure, not by balls.* A coefficient ball that contains 0 proves nothing. The coefficients that vanish are set to 0 on the strength of four structural facts S1–S4 (module docstring); the containment is reported as a consistency check only. The proofs of S1–S4 belong to the proof record (W7). S4 is the recursion argument: the order-(k+3) coefficient of the defect is affine in a_k with slope ℓ(k* − k) and independent of a_j for j > k.

- **11 Nov 2026, W2a reviewed.** PR #223, co-owner check `6798107781` (ACCEPT as a merged development check), merged as `07fdbd6`. Two obligations for W7 were named there: the full algebraic proofs of S1–S4, and the justification of the circle cover and of the outward rounding of the floating-point upper bounds.
- **11 Nov 2026, W2b.** Second-order jets, the remainder in d, tube pieces and the inverse (§5). Three points:
  - *The inverse series is dropped* (2.6) and replaced by the local inverse of 2.5. The 3b design is not changed by this; plan section 2.5 is.
  - *One more structural fact, S5* (library, W2b header): with weights (1, 2) for (z, w), F_w − w has only monomials of weighted order at least 5 (and F_z − z of order at least 4, which is S1). It makes (Φ − d)/x³ analytic and is what the maximum principle for the remainder rests on. Its proof joins S1–S4 in W7.
  - *The coupling between fibre and base is not negligible near the outer edge.* ∂x′/∂d = x⁴Q4 with \|Q4(0)\| = \|μ\| ≈ 1.26, against a base step x⁴G0 with \|G0(0)\| = \|ℓ\| ≈ 0.098. At \|x\| = 0.87 a fibre radius of 2·10⁻³ changes the relative step by 2.4% and Δτ by 2.6%; a radius of 5·10⁻³ by 6% and 7% (§5). W3 has to carry this in (A1) and (A2). It is a property of the map: the bounds are attained to within a few per cent.

- **11 Nov 2026, W2b reviewed.** PR #224, co-owner review `5861181371` (ACCEPT for the development archive; the local inverse is an acceptable *conditional* method for P8, not yet a verified inverse on a cover of D₁), merged as `dce1cc5`. The co-owner checked S5 independently at low order with exact rational arithmetic. Conditions taken over from the review:
  - *W3:* the two conditions of the lemma on every active target piece of D₁; source discs and fibres inside the chart; one inverse branch on overlaps; μ₀ ≠ 0; positive Rouché margins; the coupling in (A1) and (A2); every tube piece inside a recorded remainder profile; a stop on any uncovered piece.
  - *W7:* a reproducible exact derivation of S1–S5 with the chart and the weighted-order cutoff; the arc enclosure, the Taylor-in-d bound and the maximum-principle step; outward conversion of the float constants (an argument, or Arb-only constants).
  - *W8:* in control outputs, distinguish the printed nominal constants from the mutated ones.
- **11 Nov 2026, W3.** Zone II for both sides, 0.05 ≤ \|ξ\| ≤ 0.60 (§5). How the review conditions are met, and what is not:
  - *Met in the run.* Every pass piece of D₁ carries the two verified conditions of the lemma (they include inf\|μ₀\| > 0 and both Rouché margins). Every pass piece lies in the guard core. Tube pieces use `gt_dev` and `dtau_dev` in (A1) and (A2). A piece outside the remainder profiles or the range of the series is a failure, not an exception. The run stops at the first unresolved piece.
  - *Chart.* For G the source disc B is an enclosure; functions are evaluated on it only through the entire series and through log(1 + g̃) with \|g̃\| ≤ 1/4. That the true preimage stays in the chart sector follows from the core and (A2), as in the design (§4 there).
  - *Form of (B) for G.* Checked on the source disc in forward form: \|d\| ≤ R₁(x) implies \|d′\| < R₁(x′). On the fibre circle \|d′\| = R₁(x′) this gives \|d\| > R₁(x) at the same point, which is the pointwise inequality Rouché's theorem needs. The design states (B) with a supremum over the fibre; the pointwise form is weaker and sufficient. For F the run checks the supremum form. **To be confirmed in review; the proof belongs to W7.**
  - *Not done: one inverse branch on overlaps.* Planned method: verify the lemma also on an enlarged source set that contains the source sets of the neighbouring pieces; uniqueness in the larger set then identifies the local inverses on common targets. Open.
  - *Below ρ₀ = 0.05:* zone I (W4), including the guard property there.
- **11 Nov 2026, a distinction to keep** (`[SESSION]`, from the co-owner's comparison with LIT's notes; the owner checked the DYAD side against the stage-2b record). The target here is the jump at one point of the overlap S₀ ∩ S₁ (Im t → −∞). LIT's harmonic target s₁ is worked out on the other overlap class (S₅ ∩ S₀, Im t → +∞) and is a first Fourier coefficient, not a point value. A certified jump gives the divergence of the branch under the recorded conditional steps; it does not give s₁ ≠ 0, and no derivation between the two is recorded. Nothing from LIT is used here.

- **12 Nov 2026, W3 reviewed.** PR #226, co-owner review `5869443092` (ACCEPT as a development record), merged as `3bc5202`. On the form of (B) for G: the pointwise form can be enough, the supremum form of the design is not required; but three things must be proved in W7 for it: one analytic inverse branch on the whole target fibre, a unique solution of the base equation, and that its normal image stays inside the target fibre (the zero count). Also for W7: the exact covering argument for the pieces with the float bounds, given the thin (A2) margin (0.0011).
- **12 Nov 2026, W4.** Zone I for both sides (§5). With W3 the hypotheses (G), (A1), (A2), (B) are now checked, as development runs, on all of D₀ and D₁ inside the chart sectors. Open as before: one inverse branch on overlaps; the proofs (W7).

- **12 Nov 2026, W4 reviewed.** PR #231, co-owner review `5870411450` (ACCEPT as a development record; the product bound, the binomial majorant, the scaling and the directions of the reduced (B) inequalities were read back independently and found consistent), merged as `3d3e4d3`. Kept for W7: S1–S5, outward rounding, the cover of the whole domain, the full scaling proof of zone I, one analytic inverse branch for G.
- **12 Nov 2026, W5.** The common arc (§5). The two obligations named in the review are both addressed: existence of the analytic inverse of τ for large Fatou time (one inequality between constants), and a validated continuation on the compact part; a link gate joins them.

- **12 Nov 2026, W5 reviewed.** PR #233, co-owner review `5871277385` (ACCEPT as a development record; the Rouché justification of the inverse function step was confirmed; two recorded points of the arc were reproduced with a separate `mpmath` computation), merged as `4138aa4`. Four points for W7: the exact start t* inside the first disc; the tail estimates for every t ≥ t_M with the right branch of the logarithm and of the cube root; CHAIN and TAIL as one analytic inverse branch; outward rounding and reproducibility of the 173 disc inequalities. Noted separately: the continuation of τ⁻¹ in W5 does not settle the gluing of the branches of F⁻¹ in W3 and W4.
- **12 Nov 2026, W6.** The script for the legs and the two-disc test, with controls (§5). **Its run is a development run. No statement about the jump, about divergence, or about B-an and B-6 is drawn from it; a certificate needs stage 3c-b, which is not authorized.** Points for the review:
  - *The method differs from the design (§5 step 3 there).* The design builds nested fibre discs with interval Jacobians and an exclusion step. The script encloses the one true orbit instead: discs X_k for the base points and D_k for the deviations, updated by the exact relations of the lifted map in centred form and by the a-priori bound \|d_k\| ≤ R_j(x_k) of the tube lemma, in repeated forward and backward sweeps (library header of the W6 block). It uses the same facts and carries the moving base point in the discs X_k. A first version with interval boxes carried from step to step was dropped: the boxes doubled at every step (wrapping) and left the range of the engine after 7 steps. **This change of method needs the co-owner's judgment; it is not covered by the acceptance of the design.**
  - *What the enclosure assumes.* The conclusion of the tube lemma for the orbit of (ξ*, d_j*); the remainder constants of W2b (S5); for G, the local inverse lemma at each step of the first round, and that these local inverses are the branch G of the lemma (the open gluing point).
  - *Controls of P11.* The zero-jump model is built (`ModelEngine`: base x(1 + 3x³)^{−1/3}, fibre multiplier (x′/x)^α, an invariant analytic curve at d = 2x¹⁴) and the script must and does return overlapping discs for it. *Perturbed α* and *wrong log branch* act on the hypotheses of the lemma, not on the legs; they are run through the W4 and W5 scripts. A small change of α is absorbed by the gain of the functionals (the tube lemma does not need the exact α), so the control uses α + 10. A constant shift of τ applied consistently changes nothing, because the walls are defined relative to τ*; the control shifts τ of D₁ by 2πiκ against the walls of the principal branch. *Wrong branch* (the other root of the quadratic for a₂) is **not built**: it needs the coefficient recursion for the other branch. Open for W8.

- **12 Nov 2026, W6 reviewed.** PR #237, co-owner review `5872115882` (ACCEPT SCOPED: the forward–backward disc enclosure is acceptable as the development approach of 3c-a; it does not widen the scope of the 3b design and is not a certificate), merged as `8c89820`. Named for W7: the coverage preconditions of every update, one analytic inverse branch for G, outward rounding. New finding of the review: the SND tolerance 10⁻¹¹ of the W6 script is larger than the discs (10⁻¹⁵), so that gate does not test membership in the discs; to be tightened in W8. The control "wrong branch" is to be decided in W8.
- **12 Nov 2026, W7.** The proof record is written (`records/dyad/DYAD_OPEN20_AN_STAGE3C_A_PROOF_RECORD.md`), with two supporting computations (§5). Points for the review:
  - *One inverse branch for G* (proof record §4). The gluing is reduced to a one-dimensional fact: the base map b₀ of the reference curve is injective on a convex sector S₁ that contains every source disc. Two local inverses of a target fibre then agree at the image of the reference-curve point, and agreement spreads along the connected fibre. The enlarged-disc method proposed in the W3 entry above is not needed and is withdrawn.
  - *The zero count for G* (proof record §5): existence from the reference-curve point, uniqueness from the injectivity of b₀, simplicity from b₀′ ≠ 0.
  - *A correction for W8 found while writing §4.3:* the leg G must call the local inverse lemma for the whole a-priori fibre over X_k (`full_fibre=True`, added to the library with the old behaviour as default). The W6 development run used the current disc D_k, for which the identification with the branch G is not covered by the proof.
  - *S5 is now derived exactly* (script, rational arithmetic). A by-product: S5 survives any change of the quadratic part of T; it depends on the linear part having order 6.
  - *Not in the proof record:* the seed (Q), P1, P4 and the divergence step (they need L1–L3); the triangular form of the recursion behind S4 (taken from the earlier records).

- **12 Nov 2026, W7 reviewed.** PR #241, co-owner review `5874133624` (ACCEPT SCOPED as a working and proof record), merged as `2679f37`. One dependency was made explicit there: \|E(x₀)\| < R₁(x′) does not follow from the SRC check alone (it compares with an upper bound of the tube radius); it needs the strict forward (B) inequality. Four items were set for W8: the G leg with `full_fibre=True` and a new SEP; a strict membership test in SND; machine-checkable rounding for W3–W7; the control "wrong branch" or a PI disposition.
- **12 Nov 2026, W8.** The hand-over record is written and the four items are done (§5; hand-over record §7). Points for the review:
  - *The dependency above* is now written out in proof record §4.3 (the claim follows from the numbers of the passed (B) inequality on the source disc) and checked directly by a new option of the branch script (`--strict-e`: sup\|E\| on the source disc below the *lower* bound of the tube radius on the piece).
  - *Machine checks instead of an argument.* Every float that stores a rigorous upper bound is now compared with its ball when it is made, and every piece disc is checked to contain its rectangle. The values are unchanged; the earlier outputs are reproduced byte for byte. What stays unchecked by machine: two elementary lemmas and the control flow.
  - *"Wrong branch" turned out differently than expected.* The other root of the quadratic for a₂ is not rejected by the engine: it gives a second valid formal curve. It is rejected by the tube of the pilot branch, in zone I, because its orbits move the other way in the pilot's Fatou coordinate.
  - *Stage 3c-a is complete as far as it can be completed without the literature inputs.* The seed (Q1–Q3), P4 and L1–L3 are open; the hand-over record (§5, §6) says what a certification run could and could not claim without them. **Whether and when to authorize 3c-b is the PI's decision.**
- **12 Nov 2026, W8 reviewed, r2.** PR #244, co-owner review `5875142356` (REVISE BEFORE MERGE; reviewed commit `e948de2`), two findings:
  - *R1.* `_leg_data` handed the fibre radius of the enclosures to the engine as a float rounded to nearest. Corrected (`_fup` in both calls). The finding was taken as a class: every conversion of a ball to a float in the library and in the scripts of W3–W7 was read again, and the same defect was corrected in `piece_check`, in zone I, in the arc tail, in INJ, and in the source discs of SRC and SRC1; the zone-I part of SRC1 now decides in ball arithmetic. What was left, and why, is listed in the hand-over record §7 item 6; how the gates decide is stated in the proof record §10.
  - *R2.* `run_w8.sh` did not test the exit code of each positive process. It now records every exit code under a name, accepts only ten names with code 0 and byte-identical replays, and carries a control of this rule (a replay that writes the right file and exits 1).
  - *Source state.* LIT's reply on López-Hernanz 2012 arrived in the inbox (`pipes/DYAD/20261112-LIT-lh2012-thm42-use-check.md`, as on rtg-corpus `main` at `e3fafc8`; report at rtg-lit `a3628d4`). The hand-over record §5 and the proof record §11 now state it: reply received, favourable under conditions C1 and C2, not yet dispositioned by the owner, and by its own statement no proof of the seed. Nothing of it is used in this stage.
  - *Scope unchanged:* development record; no certificate; 3c-b not authorized.
- **12 Nov 2026, W8 r2 read back and merged.** Co-owner review `5877317450` (ACCEPT as a working and development hand-over; R1 and R2 closed at that scope; the co-owner tested the acceptance rule of `run_w8.sh` independently with one positive and four negative ledgers and did not rerun the computations). PR #244 merged as `fdc4fc4`. One point is filed with the prerequisites of a certification run (hand-over record §8): the threshold t_M of the arc tail must use the upper bound of \|A₃\|. **The work packages W1–W8 of stage 3c-a are complete; nothing in them is a certificate.**
- **12 Nov 2026, inbox.** The three open items are dispositioned (`DYAD_INBOX_20261112_OWNER_DISPOSITION.md`): LIT's reply on López-Hernanz 2012 accepted as a check of use, so condition 1 of the design is met at SESSION scope; LIT's INF-016 deferred; AZ's notice accepted. Open for the analytic branch: the seed (Q1–Q3) and P4. Stage 3c-b is not authorized.

## 5. Development runs (not certificates)

Recorded here as the packages are completed. None of them is a certificate.

**W1** (`evidence/dyad/scripts/dyad_open20_an_stage3c_lib.py`, `…_w1_check.py`; run `evidence/dyad/open20-an/stage3c-a/run_w1.sh`; 400 digits, D = 200; about 7 seconds). All gates PASS; the control SHIFTCOEF exits 1 at W1c.
- **Coefficient balls.** a₂ … a₄₀ from the exact recursion agree with the values recorded by stage 2 to 2.4·10⁻⁸⁰ relative (the printing accuracy of that record); the largest ball radius is 4·10⁻²⁷⁶.
- **Structure.** Z(x) = x + ℓx⁴ + … with the coefficients of x⁰, x², x³ equal to 0 up to balls of radius below 10⁻¹⁵⁰.
- **Defect.** The raw defect has coefficients 0 (balls of radius at most 1.3·10⁻²⁷²) through x⁴³ and a nonzero coefficient 3.5·10⁻⁶ at x⁴⁴.
- **Decay.** The k-th roots of \|Z_k\| and \|W_k\| are 0.771 to 0.776 for k from 100 to 200. So the series converge well beyond \|x\| = 1.02, the outer edge of D₀ (\|ξ\| = 0.47).
- **Why boxes are still needed for the defect.** The sum of \|defect_k\|X^k is 1.3·10⁻⁶ at X = 0.9 and 1.3·10⁻³ at X = 1.02, orders of magnitude above the defect itself. The terms cancel, so the defect is evaluated by a Taylor shift on boxes near the outer edge.

**W2a** (`…_stage3c_lib.py`, `…_stage3c_w2_check.py`; run `evidence/dyad/open20-an/stage3c-a/run_w2.sh`; series at 400 digits with D = 360, disc work at 160 bits; about 55 seconds with the control). All gates PASS; the control TAMPER exits 1 at SND.
- **Order-zero series.** With the input point (x, φ_N(x) + x²d): G0 = (Z₀ − x)/x⁴, Q4 = (∂Z/∂d)/x⁴, M3 from the d-derivative of the lifted deviation, ET44 = (raw defect)/x⁴⁴. Leading coefficients: G0(0) = ℓ, Q4(0) = μ, and M3(0) = (2 + α)G0(0), the identity behind the cancellation in the normal multiplier.
- **Cauchy constants on \|x\| = 1.10** (16 000 arcs; mean-value forms with second derivatives on each arc): 1.63 (G0), 2.11 (Q4), 1235 (M3), 0.705 (ET44). The pieces of each series are bounded separately, so no cancellation is needed on the circle. Tails at \|x\| = 1.02: 3·10⁻¹¹, 4·10⁻¹¹, 2.5·10⁻⁸, 1.4·10⁻¹¹.
- **Soundness.** On 21 discs (\|x\| from 0.01 to 1.0; relative radius 2%, 0.5% and 10⁻⁶) and 5 random points each, the values of g, Δτ, μ₀ and ∂x′/∂d computed independently (mpmath, 60 digits, the full map of the stage-3b sampling module) lie in the enclosures. For E the test is made for \|x\| ≥ 0.2, where the independent value is resolved. The discs of relative radius 10⁻⁶ have enclosures of relative radius about 10⁻⁵, which makes the test sharp: a change of 10⁻³ in one coefficient of G0 is detected (control).
- **Accuracy at relative radius 0.5%.** For \|x\| ≤ 0.87 the enclosures of g, Δτ, μ₀ − 1 and ∂x′/∂d have relative radius 4% to 7%. At \|x\| = 1.0, near the outer edge of D₀, Δτ has 13%; smaller discs are needed there.
- **Cost.** One evaluation of the one-step quantities on a disc takes about 40 ms.
- **Changes made while testing, recorded here.** The first version of the control passed, because the enclosures at 0.5% were wider than the tampering; the discs of relative radius 10⁻⁶ were added. The first circle bounds were not finite (first-order mean-value forms on arcs); second derivatives are now carried on the arcs. The gate on tails was set to 10⁻⁷ after the M3 constant came out at 1235; D was raised from 320 to 360.

**W2b** (`…_stage3c_lib.py`, `…_stage3c_w2b_check.py`; run `evidence/dyad/open20-an/stage3c-a/run_w2b.sh`; series at 400 digits with D = 360, disc work at 160 bits; about 2.5 minutes per run, 7.5 minutes with the two controls). All gates PASS; the controls SHRINKREM and SHIFTINV exit 1 at REM and INV. A second positive run gave an identical output file. The W1 and W2a runs were repeated with the extended library: outputs identical to the committed ones.
- **Second-order series.** P4 = Z₂/x⁴ and S2 = (W₂ − φ′(Z₀)Z₂ − ½φ″(Z₀)Z₁²)/x⁵, with Z₂, W₂ the d² coefficients. Leading coefficients: P4(0) = 0, S2(0) = μ̄. The d² coefficient of d′ is c₂ = x³[S2/(1+g)² − 2Q4(1 + x³M3)/(1+g)³] + (terms with the defect). The four series shared with W2a, computed there by another routine, overlap coefficient by coefficient. Cauchy constants on \|x\| = 1.10: 3.84 (P4), 2.86·10⁴ (S2); tails at \|x\| = 1.02: 8·10⁻¹¹ and 5.7·10⁻⁷.
- **Remainder in d beyond second order.** On the polydisc \|x\| ≤ X, \|d\| ≤ 0.02:
  \|d′ − E − μ₀d − c₂d²\| ≤ M₃\|x\|³\|d\|³ and \|x′ − (its d-jet of order two)\| ≤ M_Z\|x\|⁴\|d\|³.

  | X | arcs | M₃ | M_Z | sup \|Z/x − 1\| on the torus |
  |---|---|---|---|---|
  | 0.90 | 8 000 | 109.4 | 65.4 | 0.130 |
  | 1.03 | 32 000 | 680.9 | 117.4 | 0.218 |

  Method: a Taylor model in d of order two is carried through the six steps on each arc of the circle (remainder bounds for sin and exp), then through φ_N, 1/Z² and the product; the maximum principle on the polydisc turns the torus bound into the two inequalities. It needs S5 and Z/x ≠ 0 on the polydisc (last column below 1).
  - The bounds are conservative: at sampled points the true remainder is at most 12% of the bound for d′ (at \|x\| = 0.87) and at most 3% for x′.
  - Size against the second-order term at \|x\| = 0.87: with \|d\| = 2·10⁻³, M₃\|x\|³\|d\|² = 2.9·10⁻⁴, and \|c₂\|\|d\| ≈ 7·10⁻³.
- **One step on a tube piece** {\|x − x_c\| ≤ r} × {\|d\| ≤ ρ} (`tube_step`): enclosures of x′/x − 1 and of Δτ for every d of the piece, bounds dev_lo ≤ \|d′\| ≤ dev_hi on \|d\| = ρ, and modulus bounds for the dependence on d (`gt_dev`, `dtau_dev`: the differences from the values at d = 0). Sound on 12 pieces (\|x\| from 0.05 to 1.0, ρ from 10⁻¹² to 5·10⁻³), 6 random points each. The d-dependence of Δτ is separated from the value at d = 0.
  - Dependence on d at \|x\| = 0.87, relative to the values at d = 0: 2.4% (step) and 2.6% (Δτ) for ρ = 2·10⁻³; 6% and 7% for ρ = 5·10⁻³. At \|x\| = 1.0 and ρ = 5·10⁻³: 6% and 7 to 8%. The true differences reach 80% to 100% of the bounds, so the bounds are sharp. This is the coupling noted in §4.
  - Cost: about 50 ms per piece.
- **Local inverse** (`inverse_conditions`, `inverse_step`), targets at arg ξ = 0.26π, \|x′\| from 0.03 to 0.87, R′ from 10⁻¹⁴ to 5·10⁻³, relative radius 0.5% and 10⁻⁶: both conditions verified on all 12 targets; the independent preimages (numerical inverse of the full map, 6 random points each) lie in B × {\|d\| < ρ}, and x/x′ − 1, τ(x) − τ(x′) lie in the enclosures.
  - At \|x′\| = 0.87 with R′ = 5·10⁻³: ρ/R′ = 1.8 (the inverse step expands the fibre there) and r/r′ = 4.4 for a 0.5% target. The preimage disc is set by the coupling term, not by the size of the target.
  - Cost: 0.1 to 0.3 s per target.
- **`[NUM]` inverse series** (reported, not gated; degree 240, 400 digits): k-th roots of the coefficients 1.00, 1.06, 1.08 at k = 60, 120, 180; ratio of successive coefficients 1.130 to 1.132 for k from 198 to 238.
- **Changes made while testing, recorded here.**
  - *Remainder.* A first form, one Cauchy estimate in d for Φ − d on the torus \|x\| = 1.10, \|d\| = 0.05, was dropped after sampling: sup \|Φ − d\| ≈ 1.6 there, which gives a constant near 10⁴. The remainder is now bounded directly, on the circles 0.90 and 1.03 with \|d\| ≤ 0.02.
  - *Δτ on a tube piece.* The first version used x′/x − 1 as one ball in every term (relative radius 62% at \|x\| = 0.87, ρ = 5·10⁻³). The second separated the d-dependence but kept it as a complex box (20%, against a true variation of 6%). The committed version gives modulus bounds.
  - *`inverse_step`.* The first search did not enlarge the disc enough when the coupling term exceeds the target radius; it now solves condition (ii) for r.
  - *Precision.* Early scratch samples used coefficients built at 60 digits. The recursion loses its precision there and the sizes were wrong (\|a₄₀\| came out 12 times too large). Everything recorded here uses coefficients built at 400 digits, as the checks do.

**W3** (`…_stage3c_lib.py`: `Tube`, `piece_check`, `build_engine`; `…_stage3c_w3_zone2.py`; run `evidence/dyad/open20-an/stage3c-a/run_w3.sh`; both sides in parallel, about 24 minutes on two cores with the three controls). Both positive runs exit 0 with all gates PASS (G0, ENG, Z2, SND); the controls CORE, SIGMA, QZERO exit 1 at Z2. A second full run gave identical output files.
- **Parameters.** σ = 0.05, κ = 0.15, q₁ = q₂ = 9, R(ξ*) = 2·10⁻³ (design values; σ is fixed here). Cover of ρ₀ ≤ \|ξ\| ≤ 0.60 with ρ₀ = 0.05 over the whole chart sector; rectangles of side 0.02 in (log\|ξ\|, arg ξ), cut into four up to depth 5. Design objects are built as balls from the exact definitions (s_j, c_j, ε from τ(ξ*)).
- **Result.**

  | Side | pieces out | pieces pass | cut | deepest piece used | smallest margin of (B) | largest relative step |
  |---|---|---|---|---|---|---|
  | F on Ω₀ | 6 427 | 4 312 | 288 | depth 3 | 1.5·10⁻³ at \|ξ\| = 0.0505 | 0.1489 |
  | G on Ω₁ | 5 884 | 3 663 | 99 | depth 2 | 1.6·10⁻³ at \|ξ\| = 0.0505 | 0.1114 |

  No piece is unresolved. So on 0.05 ≤ \|ξ\| ≤ 0.60: the guard property holds (every piece that meets D_j lies in the core), and (A1), (A2), (B) hold on D_j, for both sides.
- **Margins.**
  - (B): the margin shrinks like \|ξ\|³ toward 0, as the model gain does; its smallest value is at the inner edge of the cover. At the outer edge of D₀ it stays above 5·10⁻⁴ after cutting (exploratory scan).
  - (A2): 0.1489 against κ = 0.15 for F, at the outer edge of D₀. The margin is thin. κ is a design value; the sampling of 3b had 0.137.
  - (A1): smallest enclosed gains of the second functional 0.064 (F) and 0.051 (G) against σ = 0.05. These are lower ends of enclosures: the true gains near those pieces are 0.32 and 0.37. The first functional gains at least 0.70.
  - For G the preimage disc is up to 5.4 times the target piece (the coupling term).
- **Semantics check (SND).** At 60 random points of D_j in pass pieces, with \|d\| = R, an independent evaluation (mpmath, the full map and its numerical inverse, its own formulas for τ, the functionals and R) confirms (A1), (A2) and the exit inequality. Smallest exit ratio \|d_new\|/R(ξ_new): 1.0022 (F), 1.0023 (G), at small \|ξ\|.
- **Controls.** CORE (core shrunk to \|ξ\| ≤ 0.44): an undecided guard piece at \|ξ\| = 0.458. SIGMA (σ = 0.5): (A1) fails on the first active piece. QZERO (q₁ = q₂ = 0): (B) fails at \|ξ\| = 0.424, arg ξ = 0.019π; 3 015 pieces of the outer part pass before that, so without the two functional factors the inequality holds on part of the domain only.
- **Not covered by this run.** \|ξ\| < 0.05 (zone I). The identification of the local inverses on overlaps (§4). The proof that the piece statuses imply the hypotheses of the lemma (W7), including the pointwise form of (B) for G, the cover by discs of rectangles, and the rounding of the float piece radii.
- **Changes made while testing, recorded here.** The first scan used σ = 0.1 and depth 2 and left 19 guard pieces undecided at \|ξ\| = 0.469; D₀ ends between 0.460 and 0.465 there (second functional 2.88 against c₀ = 2.97 at \|ξ\| = 0.47), so more depth resolves them. A control with R(ξ*) = 10⁻³ was planned for (B) and replaced by QZERO before it was run: the gain at the outer edge is large, so it was not expected to fail. The stop at the first unresolved piece was added so that a failing run ends quickly.

**W4** (`…_stage3c_lib.py`: `zone1_check`; `…_stage3c_w4_zone1.py`; run `evidence/dyad/open20-an/stage3c-a/run_w4.sh`; about 1.5 minutes on two cores with the three controls). The positive run exits 0 with all gates PASS (G0, ENG, Z1F, Z1G, SEAM, SND); the controls BIGZONE, SIGMA, CORE exit 1 at the zone-I gates. A second run gave identical output files.
- **Setting.** ξ₀ = 0.05, σ = 0.05, κ = 0.15. Targets \|x′\| ≤ X′ = (ξ₀/\|c\|)(1 + 10⁻⁹); sources and lemma discs \|x\| ≤ X = 1.001 X′ = 0.10851. All sup bounds are over the disc \|x\| ≤ X (sum of the moduli of the coefficients, plus the Cauchy tail).
- **How the reduction goes** (derivation in the library header of W4; to be written out in W7).
  - τ = A₃x⁻³(1 + η), \|η\| ≤ 0.0586. So \|τ\| ≥ t_lo\|x\|⁻³ and both functionals are at most T_c\|x\|⁻³, T_c = 3.60.
  - *Guard.* On each guard arc of the chart sector the argument of τ lies in a half-plane where one wedge condition fails. Margins: 0.30 and 631 (F), 0.62 and 0.44 (G).
  - *Tube radius.* On D_j the product of the two functionals is at least \|τ\|/K − \|s_j\| (K = 1 + cot θ₀), because they are two independent real-linear functionals of τ with lower bounds 1 and c_j. This gives R ≤ 2.8·10⁻⁶ (F) and 2.0·10⁻⁵ (G) in zone I. Without it the factor \|ξ^α\| alone is unbounded.
  - *(A1), (A2).* Δτ ∈ 1 ± 0.11 on the whole disc and fibre: Re Δτ ≥ 0.89; the second functional gains at least 0.24 against σ = 0.05; relative step at most 9·10⁻⁴.
  - *(B).* μ₀(1 + g)^{−α} − 1 = x³(M3 − (2 + α)G0) + higher order, and M3 − (2 + α)G0 vanishes at 0, so the left side is at most λ\|x\|³ with λ = 0.0088. The value at 0 enters as a ball of radius below 10⁻⁴⁰; it is not assumed to be 0. The gain of the first functional alone is 3 Re Δτ/first ≥ 0.74\|x\|³. Margin of (B) divided by \|x\|³: 0.734 on both sides. The terms with the defect, with c₂ and with the remainder are below 4·10⁻⁴.
  - *Local inverse for G.* With centre x′, radius 2\|x′\|⁴ sup\|G0\| and fibre radius 2R(x′), both conditions of the lemma hold for every target of zone I (margins 0.9985 and 0.102 in the normalised forms); the disc stays inside \|x\| ≤ X.
- **Seam.** The gate SEAM reads the two zone-II outputs of W3 (by hash): they pass Z2 and start at ρ₀ = 0.05 = ξ₀. Zone II covers 0.05 ≤ \|ξ\| ≤ 0.60 and zone I covers 0 < \|ξ\| ≤ 0.05(1 + 10⁻⁹), so the circle \|ξ\| = 0.05 lies in both.
- **Semantics check (SND).** Grid of \|ξ\| ∈ {0.05, 0.03, 0.01, 0.003} × 41 arguments across each chart sector, independent evaluation at 110 digits: 68 (F) and 72 (G) grid points lie in D_j; all of them lie in the guard core and satisfy (A1), (A2) and the exit inequality at \|d\| = R. Smallest exit ratio minus 1: 4·10⁻⁷, the size the \|ξ\|³ scaling gives at \|ξ\| = 0.003.
- **Controls.** BIGZONE (ξ₀ = 0.10): (A1) for the second functional fails on both sides (enclosed gain 0.03 and 0.02 against σ = 0.05). SIGMA (σ = 0.5): fails on both sides, and in the independent check. CORE (core of Ω₀ cut to arg ξ ≤ 0.10π): the guard arc fails for F, and the independent check finds points of D₀ outside the cut core.
- **Not covered.** The proofs of the elementary steps (W7). One inverse branch on overlaps. Zone I gives no piece list; its statement is uniform.
- **A correction made while testing.** The first version of the guard margin for F had the sign of s₀ wrong in one term (the margin came out 634.5 instead of 630.6; the verdict was the same). Found on re-reading the derivation, before the committed run.

**W5** (`…_stage3c_lib.py`: `arc_chain`, `arc_tail`; `…_stage3c_w5_arc.py`; run `evidence/dyad/open20-an/stage3c-a/run_w5.sh`; a few seconds; it needs only τ and c, not the series engine). The positive run exits 0 with all gates PASS (WEDGE, CHAIN, TAIL, LINK, SND); the controls BIGSTEP, CORE, BRANCH exit 1. A second run gave identical output files.
- **The arc.** γ solves τ(γ(t)) = Re τ* − it for t ≥ t* = −Im τ* = 4.0819, with γ(t*) = ξ*.
- **Inverse function step** (used for both parts; statement in the library header of W5): if m = \|f′(c)\| − r sup_B\|f″\| > 0 on a disc B of radius r, then f is injective on B with \|f(a) − f(b)\| ≥ m\|a − b\|, and every w with \|w − f(c)\| < rm has exactly one preimage in B.
- **Compact part (CHAIN).** 173 discs of relative radius 2% from t* to t = 5377. For each segment: the step applies to every t of the segment; the next centre lies in the disc, and the two consecutive solutions agree at the common t; the disc lies in both guard cores (\|ξ\| ≤ 0.42, 0.09π ≤ arg ξ ≤ 0.20π). Along the centres \|ξ\| falls from 0.40 to 0.0396 and arg ξ stays in [0.1493π, 0.1667π].
- **Tail (TAIL).** For \|ξ₀\| ≤ 0.04, i.e. t ≥ t_M = 5208: around the leading approximation x₀(w) = (A₃/w)^{1/3} (the cube root with arg ξ near π/6) the step applies on the disc of relative radius 3%, by one inequality between constants (margin 0.027). So for every t ≥ t_M there is exactly one solution in that disc, within 1.9% of x₀; \|γ(t)\| ≤ 1.03 (\|A₃\|/\|w\|)^{1/3} → 0, and arg ξ ∈ [0.1571π, 0.1763π]: inside both cores.
- **Link (LINK).** The chain ends at t_K = 5377 ≥ t_M, and its solution there lies in the tail disc (relative distance to the tail centre 1.45% < 3%). So the chain and the tail are one arc.
- **Wedge conditions (WEDGE).** At τ*: first − 1 = 0.25 on both sides, second − c_j = 0.15 on both sides (the design margins). Along the half-line Re τ is constant and both second functionals grow with slope sin θ₀ = 0.924. So γ ⊂ D₀ ∩ D₁, which is C2 of the design: the open neighbourhood U exists because D₀ and D₁ are open. For t > 5.33 the arc lies in D₀(c₁) ∩ D₁(c₁) (used in the divergence step).
- **Independent continuation (SND).** 175 points (mpmath, Newton steps in t with ratio 1.05) from t* to 4 t_M: each lies in the chain disc that covers its t, or in the tail disc. At t = 3109: \|ξ\| = 0.0468, arg ξ = 0.1634π, as in the sampling of the design (0.047 and 0.1634π at t = 3000).
- **Controls.** BIGSTEP: the first segment is not covered. CORE (core of Ω₀ cut to arg ξ ≤ 0.16π): the first disc is not in the core, and the tail is not either. BRANCH (another cube root in the tail): the tail leaves the cores and the chain does not meet it.
- **For W7.** The proof of the inverse function step (a Rouché argument); that the continuation is analytic in t and that consecutive discs give one curve (stated in the docstring of `arc_chain`); the float values t_k (the step covers a disc in w, so the rounding of t* is inside it); the monotonicity of the three sup bounds of the tail.

**W6** (`…_stage3c_lib.py`: `leg_F`, `leg_G`, `MapEngine`, `ModelEngine`; `…_stage3c_w6_legs.py`; run `evidence/dyad/open20-an/stage3c-a/run_w6.sh`; about 12 minutes on two cores with four controls). **Development run; not a certificate; no statement about the jump is drawn from it.** The positive run exits 0 with all gates PASS (G0, ENG, LEGF, LEGG, SEP, SND); the controls SHORT, ZEROJUMP, ALPHA, LOGBRANCH exit 1. A second full run gave identical output files.
- **Setting.** 334 steps on each leg (the number of the design), 5 rounds of sweeps, engine as in W3. X_0 is the ball of x* = ξ*/c.
- **Output of the development run** (the deviation d at ξ* from φ₄₀, one coordinate for both legs):

  | Leg | centre | radius | radius after each round | end of the orbit |
  |---|---|---|---|---|
  | F (D₀) | −4.3167·10⁻⁹ + 1.99338·10⁻⁸ i | 8.1·10⁻¹⁶ | 1.5·10⁻⁵, 1.1·10⁻⁹, 2.0·10⁻¹⁴, 8.1·10⁻¹⁶, 8.1·10⁻¹⁶ | \|ξ\| = 0.0961, a-priori radius 1.4·10⁻¹² |
  | G (D₁) | 4.0447·10⁻⁹ + 2.2869·10⁻⁹ i | 2.1·10⁻¹⁵ | 2.5·10⁻⁸, 2.2·10⁻⁹, 3.2·10⁻¹², 3.3·10⁻¹⁵, 2.1·10⁻¹⁵ | \|ξ\| = 0.0986, a-priori radius 1.5·10⁻¹¹ |

  Two-disc test: \|c₁ − c₀\| = 1.9528·10⁻⁸ against r₀ + r₁ = 2.9·10⁻¹⁵. Every disc X_k lies in the guard core of its domain.
- **Consistency with earlier numerics.** The independent computation (SND: mpmath, 80 digits, the full map and its numerical inverse; a point of the reference curve 150 steps along the orbit is carried back and its start adjusted until the base point is ξ*) gives values at distance about 10⁻²² and 10⁻²⁶ from the two centres, and \|difference\| = 1.952756045·10⁻⁸. Stage 2b recorded \|Δ_Y\| = 1.95·10⁻⁸ at this point, and the estimate SEP of the design a width of 5·10⁻¹⁵.
- **Controls.**
  - ZEROJUMP: for the model the two discs have radius 5.0·10⁻¹⁵ each and centres 2.3·10⁻¹⁷ apart; both contain the known common value 2x*¹⁴; the model curve stays inside the a-priori tube (at most 17% of its radius). The two-disc test fails, as it must.
  - SHORT (10 steps): radii 2.0·10⁻⁷ and 3.2·10⁻⁷; the test fails.
  - ALPHA (α + 10, W4 script): λ = 1.03, (B) fails on both sides. LOGBRANCH (W5 script): the second functional of D₁ at ξ* is 10.15 below its wall; WEDGE fails.
- **Not covered.** The control "wrong branch". The proofs (W7), among them: that the updates of the leg method are valid (each is one exact relation in centred form), the branch of G along the leg, and the points listed for W3–W5. Nothing here is a certificate.
- **Changes made while testing, recorded here.** The first leg code carried interval boxes from step to step; it failed at step 7 (F) and step 4 (G) and was replaced by the centred disc form. In the first model test the model curve (d = 40x¹⁴) left the a-priori tube at intermediate steps; the amplitude was lowered to 2 and the script now checks that the model curve stays inside the tube.

**W7** (`…_stage3c_w7_structure.py`, `…_stage3c_w7_branch.py`; run `evidence/dyad/open20-an/stage3c-a/run_w7.sh`; about 15 minutes on two cores). Both positive runs exit 0; the controls SCALE, SHIFT (structure) and SMALLSECTOR (branch) exit 1. A second full run gave identical output files.
- **Structure (exact).** Taylor polynomial of T⁶ through total degree 5 in rational arithmetic, changed to (z, w) over Q(√3, i). F has no terms of degree 2. F_z − z has the monomials z²w (μ), z⁴ (c₄₀), z³w, z⁵ of weighted order at most 5 and no others; F_w − w has zw² (μ̄), z³w (d₃₁), z⁵ (cc) and no others. The constants equal those of the library. This is S5, with S1–S3 as special cases.
  - Control SCALE (e^ρ − 1 multiplied by 11/10): the linear part no longer has order 6 and S5 fails. Control SHIFT (a term η²/10 added to sin η): S5 still holds; only the constants change, and the gate LEAD fails.
- **Branch.**
  - INJ: sup\|b₀′ − 1\| = 0.704 on the sector S₁ = {\|ξ\| ≤ 0.47, 0.03π ≤ arg ξ ≤ 0.50π} (8 362 discs and the disc \|ξ\| ≤ 0.05, where the sup is 0.0036); the largest value is near \|ξ\| = 0.465, arg ξ = 0.033π.
  - SRC: the cover of W3 for Ω₁ is repeated and gives the same counts (99 cut, 5 884 out, 3 663 pass). Every source disc lies in \|ξ\| ≤ 0.417, 0.128π ≤ arg ξ ≤ 0.386π, well inside S₁; sup\|E\| on it is below the fibre radius of the target set on every piece; the largest fibre radius ρ of the lemma is 0.0084.
  - SRC1 (zone I): the source disc has relative radius 2.6·10⁻⁴; \|E\|/R₁ ≤ 5·10⁻³⁰.
  - Control SMALLSECTOR (S₁ cut to \|ξ\| ≤ 0.30): 534 pieces have their source outside.

**W8** (library: `_assert_up`, `piece_disc`, `build_engine(root=…)`, `leg_G(full_fibre=True)`; options `--full-fibre`, `--strict-snd` of the legs script, `--strict-e` of the branch script, `--control BRANCH` of the zone-I script; run `evidence/dyad/open20-an/stage3c-a/run_w8.sh`; about 30 minutes on two cores). **Development runs; not a certificate; no statement about the jump is drawn.** All exit codes as expected; the two new computations were run a second time with identical output files.
- **Legs in the form the proof covers** (`--full-fibre --strict-snd`): gates G0, ENG, LEGF, LEGG, SEP, SND PASS. Radii 8.10·10⁻¹⁶ (F) and 2.07·10⁻¹⁵ (G); the radii after each round are the same as in the W6 run to the digits printed. Two-disc test: \|c₁ − c₀\| = 1.952756045·10⁻⁸ against r₀ + r₁ = 2.88·10⁻¹⁵. With no tolerance, the independent values lie in the discs (distances 1.1·10⁻²² and 7.7·10⁻²⁷ from the centres).
- **Inverse branch with the strict check** (`--strict-e`): INJ, SRC, SRC1 PASS; the cover of Ω₁ gives the counts of W3 again; on every pass piece sup\|E\| on the source disc is below the lower bound of the tube radius (smallest margin 1.8·10⁻¹⁶, on a piece where the radius itself is of that size).
- **Machine checks.** The run replays six earlier computations with the checks active: zone II for F, the W6 legs, W2a, W2b, zone I and the arc. No check failed, and every output is byte-identical to the committed one (`w8_replay.txt`). The cover of Ω₁ is replayed inside the branch run (same counts).
- **Control BRANCH** (other root of the quadratic for a₂ against the pilot's tube): exit 1. Zone I: Re Δτ ≥ −1.107 only (the first functional decreases), second gain − σ = −0.573, (B) margin −0.93, on both sides. The structural zeros of the other curve are consistent; its series pass every engine check except the tail threshold (5.7·10⁻⁷ becomes 3.6·10⁻⁶ for S2), which is incidental.
- **Not rerun in W8:** W1, the controls of W2–W7, and the structure script (unchanged code paths).

**W8 r2** (after review `5875142356`: library and branch script with the checked float bounds of the hand-over record §7 item 6; `run_w8.sh` rewritten; one run of 42 minutes on two cores, 12 Nov 2026, 17:20–18:03 +03:00). **Development runs; not a certificate; no statement about the jump is drawn.**
- **Why more than the legs was run.** The correction of R1 was applied to the whole class, and the corrected lines lie on the paths of zone II, zone I, the arc and the branch run. Each of these was therefore run again with the corrected library and compared with its committed output.
- **Acceptance rule of the run** (`w8_replay.txt`): ten positive processes, each with exit code 0 — zone II for F and for G, the branch run with `--strict-e`, the W7 branch run, the legs with `--full-fibre --strict-snd`, the W6 legs, W2b, W2a, zone I, the arc — and nine replays byte-identical to the committed outputs (the eight earlier positive outputs and the control ZEROJUMP of W6, exit 1 as before). Control BRANCH: exit 1. All met.
- **Control of the rule:** a replay of W5 that writes a file identical to the committed one and exits 1 is rejected by the rule.
- **Legs with the checked fibre radius** (`w8_legs.json`): the six gates PASS and the file is byte-identical to that of r1. Radii 8.0967·10⁻¹⁶ (F) and 2.07158·10⁻¹⁵ (G); \|c₁ − c₀\| = 1.952756045·10⁻⁸ against r₀ + r₁ = 2.88125·10⁻¹⁵; the independent values lie 1.07·10⁻²² and 7.7·10⁻²⁷ from the centres, with no tolerance. The checked bound exceeds the old float by at most a relative 10⁻¹² and one rounding, which is below the digits printed; so the r1 numbers are also the numbers of the corrected code. How often the old conversion had rounded downward was not measured.
- **Inverse branch with `--strict-e`** (`w8_branch.json`): byte-identical to r1; INJ, SRC, SRC1 PASS with the checked bounds; the smallest R_lo − sup\|E\| is still 1.77·10⁻¹⁶.
- **The W6 output** (default form of the leg, superseded) is reproduced byte for byte; nothing historical had to be set aside.
- **Checksums:** `SHA256SUMS_W8.txt` renewed (`w8_replay.txt`, `run_w8.sh` changed; the six output files unchanged); the files W1–W7 verify unchanged.
- **Not rerun in r2:** W1, the structure script, the controls of W2–W5 and W7, and the controls SHORT, ALPHA, LOGBRANCH of W6. REVIEWER-REPLAYED: none.
