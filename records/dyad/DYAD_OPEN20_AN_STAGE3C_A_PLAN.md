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
- **Zone I** (\|x\| ≤ ρ₀): the same inequalities in scale-free form. Each series is enclosed on the whole disc by its leading term and the sum of the absolute values of the rest; every term of (B) is then \|x\|³ times a quantity bounded on the zone. The reduction is part of the proof record.

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
| W4 | Zone I: scale-free verification and its reduction | P3 | open |
| W5 | Arc: compact continuation; analytic tail | P9 | open |
| W6 | Legs and the two-disc test; controls (zero-jump model, wrong branch, wrong log branch, perturbed α) | P10, P11 | open |
| W7 | Proof record: tube lemma, inward property, seed, divergence argument, soundness of every computer-checked step | P1, P4, and the analytic parts of P3, P9 | open |
| W8 | Hand-over: fixed commands, package layout, what 3c-b would run | — | open |

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
