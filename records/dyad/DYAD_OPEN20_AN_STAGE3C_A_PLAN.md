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
- the dependence on d as a jet in d (first and second order exactly, the rest by a Cauchy bound in d).

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

- **Zone II** (ρ₀ ≤ \|x\|): adaptive boxes in x over each chart sector. A box is *guard* (shown to violate a wedge condition everywhere), or *active*. On an active box the inequalities (A1), (A2), (B) are verified for every point of the box that satisfies the wedge conditions, without locating the walls: the functionals enter only through first ≥ 1, second ≥ c_j and their upper bounds on the box. A box that fails is split; a minimal size ends the run with a failure report.
- **Zone I** (\|x\| ≤ ρ₀): the same inequalities in scale-free form. Each series is enclosed on the whole disc by its leading term and the sum of the absolute values of the rest; every term of (B) is then \|x\|³ times a quantity bounded on the zone. The reduction is part of the proof record.

### 2.5 The inverse map, the legs and the arc

- **Inverse map (for D₁):** the series of F⁻¹ along the curve by formal inversion, with a validated inverse on a circle for the tail bound.
- **Legs (P10):** the nested fibre discs of the design §5 step 3, with one-step enclosures from the same series and the interval Jacobian in (x, d).
- **Arc (P9):** validated continuation of τ(γ(t)) = Re τ* − it on the compact part; the tail by the analytic estimate of the proof record.

### 2.6 Tried and set aside

**Second-order Taylor forms on boxes in (x, u).** The first engine carried value, gradient and Hessian through the six steps on each box and used f(c + h) ∈ f(c) + ∇f(c)h + ½hᵀ Hess f(B) h. Its enclosures were sound in every test (sampled points inside), but far too wide:
- with the steps carried in the coordinates (ρ, η), the Hessian balls grow by about 2.7 per step;
- with the steps carried in the diagonal coordinates (z, w), the growth is smaller, but at a relative box size of 0.5% the enclosure of G still has a relative radius of 1.4% to 7%, and that of H_u exceeds 100%, at every \|x\| ≤ 0.5;
- the cause is structural: the quotients are of order \|x\|⁴ and \|x\|⁵ against steps of order 1, so a form of order two cannot be uniform in scale. Order four or more would be needed, in two variables.
The series of 2.2 replace it. The code of the first engine is not kept.

## 3. Work packages

| # | Package | Obligations | State |
|---|---|---|---|
| W1 | Engine, first part: constants, coefficient balls, series of the map and of the defect along the curve | P5 | **done as a development check** (§5) |
| W2a | Jets in d (first order), order-zero series, Cauchy constants and tails, Taylor-shift evaluation on discs, the one-step quantities of 2.2 for F | P6 | **done as a development check** (§5) |
| W2b | Remainder in d beyond first order (Cauchy bound on a torus); the inverse map along the curve with a validated inverse | P6 | open |
| W3 | Zone II verification with adaptive boxes, for F on Ω₀ and G on Ω₁, including the guard property | P7, P8 | open |
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
