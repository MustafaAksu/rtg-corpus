# DYAD OPEN 20 — owner review of the independent C++ checkpoint

**By:** Claude, Dyadic DSN owner and math auditor. **Date:** 16 November 2026. **Status:** working record (SESSION). Not an adoption, not a certificate; no point jump computed.
**Reviewed (as relayed by the PI; not yet in the repository):** the co-owner's checkpoint of 16 November 2026 — `independent_core.cpp` (SHA-256 `f5b574b0…7783`, 323 lines) and `DYAD_OPEN20_CPP_INDEPENDENT_DESIGN.md` (SHA-256 `44466127…6f3d`). Read whole. The package zip was not available to the owner.
**Governing edition:** `dyad-v6.4.24`, unchanged. B-an and B-6 ACTIVE; stage 3c-b production run and replay not authorized.

## 1. Verdict

**The kernel is sound as far as checked: no line accepts a false enclosure, and the contractor theorem is correct.** One finding is decisive for the plan: **the design is not feasible at the horizon of the legs** in its present evaluation scheme (F1). The independence disclosure is accurate.

| Item of the design §9 | Owner |
|---|---|
| C1–C2 proof and code | correct (§2) |
| E1 and interval arithmetic | correct; enclosures confirmed against a 320-digit oracle (§3) |
| Initial fibre and budget | sound; one efficiency point (F3) |
| Raw map and lift | correct for the owner's definitions (§2) |
| Independence | accurately disclosed |
| Implementation extent | accurately stated; no point-jump claim |

## 2. Checked by reading

- **C1.** f(d*) = f(a) + b(d* − a) + E with \|E\| ≤ D\|d* − a\| ≤ Dr on the segment in the convex disk. Hence \|d* − (a − f(a)/b)\| ≤ (M + Dr)/\|b\|. No convergence, existence or uniqueness is needed. Correct.
- **C2 in `necessary_disk`.** The true centre a − f(a)/b lies in `new_c_box`; the recentring error is bounded by the L1 norm (≥ Euclidean); D by the L1 norm of `derivative − b`; the products are rounded up; the denominator is max(\|Re b\|, \|Im b\|) ≤ \|b\|. Correct.
- **Interval core.** Products and quotients take all endpoint combinations with signed floor/ceiling; the square root uses a floor integer square root for the lower end and rounds the upper end up; a zero in a denominator is an unresolved evaluation. Correct.
- **E1.** The omitted majorant terms have ratio at most M/(N + 2), so the geometric bound holds for M < N + 2 (M ≤ 8, N = 160). The bound is added to both coordinates. Correct.
- **Map, chart, lift.** T(ρ, η) = (ρ − sin η, η + e^ρ − 1 − sin η) with sin from e^{±iz}. z = ρ + ωη, w = ρ + ω̄η, η = (z − w)/(i√3), ρ = (z + w + η)/2. The lift is w = φ(x) + x²d in, d′ = (w′ − φ(z′))/z′² out, with derivatives carried in d. This matches the owner's definitions (proof record §1).
- **Cover.** A tile is discarded only if it is proved outside the initial disk, if the contractor returns "empty", or if its intersection with the contracted box is empty. Unresolved tiles and the pending queue are retained; an empty cover is refused. Sound.
- **Separation.** Exact centres, strict integer comparison; tangency is not separation. Correct.

## 3. Checked by running

**Build and tests.** GCC 13.3, Boost.Multiprecision and Boost.Config 1.83 headers (standalone mode). The 20 unit tests pass, also under AddressSanitizer and UndefinedBehaviorSanitizer; a call without `--unit-tests` exits with 64.

**Own probes** (`evidence/dyad/open20-an/cpp-review/`):

1. **Oracle.** F, F¹⁰ and F²⁰ at one complex point (ρ, η) = (0.03 + 0.01i, −0.02 + 0.005i), and ∂F/∂ρ: every C++ interval contains the 320-digit mpmath value (`check_oracle.py`: PASS).
2. **exp(8)** at the edge of the range budget: contains e⁸; width 2·10⁻⁷⁵.
3. **Contractor on a nonlinear function.** f(d) = 7(d − r) + (d − r)² on B(0, 1/4), with the derivative enclosed over the whole disk: all 27,549 points of a dyadic grid (step 2⁻¹⁶) with \|f\| ≤ M = 0.01 lie in the returned disk (radius 0.044).
4. **Width growth along an orbit** (the measurement behind F1). Starting from an exact point, the width of the enclosure is 7·10⁻⁷³ after one F, 1·10⁻⁴⁹ after 10, 5·10⁻²⁴ after 20. That is a factor of about 330 per F, or about 2.6 per T. After about 28 steps the range check refuses the evaluation. The true derivative of F at these points is close to the identity; the growth is overestimation, not dynamics.
5. **Speed.** One F with jets takes about 0.05 s at 256 bits.

## 4. Findings

**F1 — not feasible at horizon 334 (decisive; not a soundness fault).** The growth of probe 4 has a plain cause. In raw coordinates T adds widths: η′ = η + (e^ρ − 1) − sin η adds the widths of η and sin η, which are correlated, and the linear part [[1, −1], [1, 0]] has \|·\|-spectral radius 1.618 even though it is a rotation of order 6. So:
- a point evaluation at 256 bits fails near step 28, and would need roughly 3000 bits for 334 steps;
- the derivative enclosure over a tile, which C2 needs, grows by the same factor times the tile width, so already the first tiles cannot contract.

The design anticipated this ("feasibility at horizon 334 untested"; "if dependency inflation prevents useful bounds, record the negative result"). This record is that result, for the present scheme.

**Remedy (for the co-owner's choice; owner does not prescribe the route):**
- evaluate in the eigen-coordinates (z, w), where the linear part is diagonal;
- use disc (midpoint–radius) arithmetic, which is invariant under the rotation, instead of rectangles;
- propagate a centre plus a mean-value or Lohner-type remainder per step, instead of the whole box.

Any of these changes the evaluator, not the contractor. The owner's Python legs met the same wall in W6 and passed it with centred discs; adopting that idea is not translating code, but it should be disclosed.

**F2 — one hypothesis must be checked by the adapter.** The necessary condition \|f_{j,k}(d*)\| ≤ R_j(ξ_k) needs the base points ξ_k of the true orbit to lie in D_j, where R_j is defined and the tube lemma applies. The adapter must prove that the base enclosure lies in D_j (including the log cut and the sector) before it uses R_j as M. Where it cannot, the condition is not available and the tile must be retained.

**F3 — unresolved tiles are not subdivided (efficiency only).** `outer_cover` retains a tile on a `domain_error` without bisecting it. The design (§3 step 5) allows subdivision. With a large initial tile this turns a range refusal straight into INCONCLUSIVE. Suggest bisecting while the tile is wider than `width`.

**F4 — minor.**
- Only `domain_error` is caught; other exceptions end the whole cover. This is fail-loud and acceptable, but the design should say it.
- The inverse adapter of §6 can be a complex 2×2 Krawczyk test on C², since F is holomorphic; K ⊂ int X is sufficient by itself.
- `exp_c` divides by `C(k)` (complex) where a real divisor would do; speed only.

## 5. What this means for the plan

- The kernel and the contractor are a sound base. Accepting them as a checkpoint is reasonable.
- The next step is **not** the coefficient and tube adapters. It is a short-horizon feasibility test with a changed evaluator (F1). A useful acceptance criterion: a point evaluation over 334 lifted steps at fixed precision, with a final width small against the tube radius; then a tile-derivative enclosure over a small tile.
- No comparison with the Python disks should be made before that, as the design says (§10).
- Nothing here is a run of stage 3c-b, and nothing bears on B-an or B-6.

## 6. Evidence

`evidence/dyad/open20-an/cpp-review/`: `probe_kernel.cpp` (probes 2–5; includes the reviewed source unchanged), `probe_kernel_output_n20.txt` (20 steps; all probes), `probe_kernel_output.txt` (30 steps; shows the range refusal), `probe_oracle.cpp`, `probe_oracle_endpoints.txt`, `check_oracle.py`, `check_oracle_output.txt`, `SHA256SUMS.txt`. The probes include `independent_core.cpp` by name; it is not in the repository yet, so the probes are reproducible once the package arrives on an `upload/…` branch. OWNER-RUN, SESSION.

## 7. Second checkpoint: the centred evaluator (16 November 2026)

**Reviewed (as relayed by the PI; not yet in the repository):** `centered_evaluator.hpp` (SHA-256 `b868f945…a04a894`, matching the co-owner's comment `6919482912`) and `DYAD_OPEN20_CPP_CENTERED_FEASIBILITY.md` (SHA-256 `c0acf8a3…1567`), read whole. The package zip (`5dfb8b1f…068a`), the 15 new unit tests, the probes and the patched `independent_core.cpp` (F3) were **not** available to the owner; F3 is therefore not checked.

**Verdict: the evaluator is correct as far as checked, and F1 is answered on the tested trajectories.** Accepted as a development checkpoint. The actual legs remain open.

**Checked by reading.**
- *Eigen-map.* With E = e^ρ − 1 − ρ and S = sin η − η: ρ′ = ρ − η − S and η′ = ρ + E − S. Since 1 + ω + ω² = 0, λz = (1 + ω)ρ − η, so z′ = λz + ωE − λS; w′ likewise with the conjugated constants only. The code implements exactly this.
- *Residual series.* `exp_residual` sums degrees ≥ 2 for E and ≥ 1 for E′ = e^ρ − 1. `sin_residual` takes odd degrees ≥ 3 with sign + at k ≡ 1 (mod 4) for S, and even degrees ≥ 2 with sign + at k ≡ 0 (mod 4) for S′ = cos η − 1. Every omitted term has degree ≥ 161 and is bounded by the exponential majorant E1. Correct.
- *MV1.* F is entire, the polydisc P is convex, and the 2×2 Jacobian is enclosed on the rectangle containing all of P (`block(boxes)`). The centre error is the radius of the ball around the interval value of F(c). r′_i = e_i + Σ_j sup\|J_ij\| r_j, rounded up. Correct.
- *AD1.* The tangent at the true point is DF(p)·v with DF(p) in the whole-P Jacobian and v in the tangent disc. Disc products use \|a\|s + \|b\|r + rs plus the centre-rounding error; sums add radii. Correct.
- *Lift and readout.* The input is z = x, w = φ(x) + x²d with the whole d-disk, and tangent (0, x²). The readout d = (w − φ(z))/z² is taken once, at the end, with the pole excluded. Because the raw map is iterated, intermediate lifts are not needed for holomorphy in d. The readout treats w and z as independent boxes: sound, and loose by \|φ′\|·width(z)/\|z\|².

**Checked by running** (`evidence/dyad/open20-an/cpp-review/centered/`; the evaluator built against the reviewed kernel):
- *334 blocks at the owner's raw point,* 13 s. Final widths 7.743·10⁻⁷¹ (values) and 1.414·10⁻⁶⁶ (tangents), equal to the co-owner's. All 16 enclosures at blocks 1, 10, 100 and 334 contain the 360-digit mpmath values of T⁶ᵏ and of its variational equation.
- *The broad synthetic disk* (φ = x²/2, x = 1/64 + i/128, \|d\| ≤ ⌈2²⁵⁶/500⌉/2²⁵⁶). The enclosure of d₃₃₄ has width 1.12·10⁻²; that of its derivative has width 5.99·10⁻², equal to the co-owner's 5.99178729·10⁻². Independent mpmath iterations at 36 initial points (on the boundary, at half radius, at the centre) are all inside both enclosures.

**Points for the next steps** (none blocks this checkpoint):
- *F2, refined.* The true point after n steps lies on the graph over a base point in D_j: (G) and the tube lemma keep the true orbit there. So M may be the supremum of R_j over the base enclosure **intersected with** D_j, provided R_j is bounded there rigorously. Full containment of the enclosure in D_j is not needed. If no bound on that intersection can be proved, the tile is retained.
- *Readout.* For the real leg, where \|d\| is small against \|z\|, the independent-box readout may dominate the final width. Reading out d through the lifted tangent, or with a mean-value step for w − φ(z), would tighten it.
- *Real-leg feasibility.* The tested trajectories are a raw point and a synthetic lift. On the real legs the fibre expands along the orbit. Whether the full initial fibre \|d\| ≤ R_j(ξ*) contracts with a manageable number of tiles is the open question. A short-horizon test with the real φ₄₀ and ξ* answers it.
- *The inverse leg G* is unimplemented, as the checkpoint states.

**Not done by the owner:** the package as a whole, the 15 unit tests, the sanitizer runs, the F3 change, and the shooting probe with its contractor step. The checkpoint's statements about these are the co-owner's.

