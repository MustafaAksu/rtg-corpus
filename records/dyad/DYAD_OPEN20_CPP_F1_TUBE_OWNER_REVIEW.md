# DYAD OPEN 20 — owner review of the C++ first-block tube bound and contractor (F1)

**By:** Claude, Dyadic DSN owner and math auditor. **Date:** 17 November 2026. **Status:** [SESSION] owner review of a co-owner development package. Not an adoption, not a certificate, not stage 3c-b. B-an and B-6 stay ACTIVE.
**Reviewed:** `DYAD_CPP_F1_TUBE_CONTRACTOR.zip`, SHA-256 `f8e66093fa2980ef48d96cd7d975aceca4532c9ca47dcdb05138c19961a5a567` (relayed by the PI on 17 November; 8 files; its `SHA256SUMS.txt` checks). It is **not yet on GitHub**; it should arrive unchanged on an `upload/...` branch.
**Dependencies used (from branch `dyad-cpp-centered-20261116`, `upload/dyad-cpp-centered-20261116/received/`):** `DYAD_CPP_FORWARD_METHOD_BENCHMARK.zip` `6079c11b…176d` (bench.cpp: `tiles`, `direct6`, `Tcentered`, `read_data`, `xstar`), `DYAD_CPP_PHI40_B_EVALUATOR_DIAGNOSTIC_V2.zip` `98390698…6ecc` (`import_phi40.py`, `centered_evaluator.hpp`, `independent_core.cpp`: `necessary_disk`, `intersection`, `outside_disk`). Both packages' `SHA256SUMS.txt` check.
**Request:** the co-owner's `OWNER_REVIEW_REQUEST.md`, items R1–R5, against proof record §§1, 4–5, 9 and the real-leg scale note §3.5 (PR #301).

## Verdict

**ACCEPT as a development checkpoint, at SESSION scope.** R1–R4 pass by reading; R4 also by a ball-arithmetic check; the package reproduces bit-for-bit in its summary lines on a second machine. One small owner-side finding (O-1) concerns the existing Python library, not this package. Nothing here proves that a curve exists, that it lies in the tube, or anything about the point jump.

## R1 — M(X) is an upper bound of R₀ on X ∩ D₀

`ForwardTube::upper` (real_f1_tube.cpp l. 116–152) against the library `Tube` (stage3c lib l. 756–790) and proof record §1:

| item | code | check |
|---|---|---|
| normalisation | M = (1/500)·\|ξ^α\|/\|ξ*^α\|·(1.25/first)³·(second*/second)³ | equals ε\|ξ^α\|first⁻³second⁻³ with ε fixed by R(ξ*) = 0.002, first(ξ*) = 1.25, second(ξ*) = second* (library `eps`, q = 9). ✓ |
| α, signs | exponent −(51/19)·log(\|ξ\|²/0.16) + (16√3/19)(θ − π/6) | Re(α log ξ) = −(102/19)ln\|ξ\| + (16√3/19) arg ξ; −51/19 = Re α/2 on \|ξ\|²; \|ξ*\|² = 0.16 = 4/25; Im α < 0 so only the upper end of θ is needed. ✓ |
| angle | θ_hi = min(0.3π upper, atan(Im ξ/Re ξ) upper) | principal arg (Re ξ > 0 required, else only the chart cap). On D₀ the principal arg lies in (−0.20π, 0.30π), the library's chart and the definition of \|ξ^α\| (`xi_alpha`: principal log of ξ = cx). ✓ |
| τ | fixed decimals A₃, A₂, A₁, κ; principal log of x | identical to `TAU_DECIMALS` (lib l. 433) and to `Tube.tau` (x = ξ/c, principal log). Re x ≤ 0 on the box → τ not evaluated, global floors used. ✓ |
| first | Re τ − Re τ* + 5/4 | = Re τ − s₀ + 1 with s₀ = Re τ* − 0.25. ✓ |
| second | Re(e^{i3π/8} τ), e^{i3π/8} = (√(2−√2)/2, √(2+√2)/2) | θ₀ = π/2 − π/8. ✓ |
| floors | max(1, first.lower), max(c_wall.lower, second.lower) | valid for every x ∈ X ∩ D₀ (first > 1, second > c₀); no claim X ⊂ D₀ is made. ✓ |
| ξ = 0 | refused (domain error → tile retained) | ✓ |

## R2 — directed rounding of the elementary functions

- **atan** on [0, 1]: alternating Leibniz series, N = 320 terms in interval arithmetic; the first omitted term u^{2N+1}/(2N+1) bounds the error with the right sign for even N (enclosure [S.l, S.h + err.h]). Terms decrease on [0, 1]. u > 1 by π/2 − atan(1/u); u < 0 by oddness; intervals by monotonicity of the endpoints. ✓ (At u near 1 the bound is wide, 1/641, but still valid; here Im ξ/Re ξ ≈ 0.5.)
- **π** = 16 atan(1/5) − 4 atan(1/239) (Machin), both arguments exact points. ✓
- **log** on u > 0: 2 atanh q, q = (u−1)/(u+1); remainder 2\|q\|^{2N+1}/((2N+1)(1−q²)) with the upper magnitude of q^{2N+1} and 1 − q² from its interval; endpoints by monotonicity. ✓
- **e^{i3π/8}** algebraic, sqrt enclosures of the engine. ✓
- **exp_c**: the engine routine of `independent_core.cpp` (Taylor sum with tail M^{N+1}/(N+1)!/(1 − M/(N+2)), large arguments refused), reviewed in the C++ independent review (#288). ✓
- Unit gates (π, atan(1/2), log(1/2), R(ξ*) ∈ (1.99, 2.01)·10⁻³) pass, also under ASan/UBSan, empty sanitizer stderr.

## R3 — contractor, derivative, coverage, no false discard

- **Coverage.** `tiles(N)`: the square [−r, r]² with r = 1/500 rounded up, N×N boxes with outward-rounded edges; a box is skipped only if `outside_disk` proves it disjoint from \|d\| ≤ r; each kept box becomes `ball(box)` ⊇ box. 60 (N = 8) and 96 (N = 10) tiles. ✓
- **Whole-tile derivative.** `from_lift(x*, tile, φ)` enters the fibre as `tile.box()` with tangent 1, so `r.b.d` encloses ∂d₁/∂d₀ on a set containing the tile disc. ✓
- **Centre and radius.** f(a) is the enclosure of d₁ at the tile centre (separate point orbit), b = mid of its tangent (exact dyadic). `necessary_disk`: centre B.c − f(a)/b moved to its midpoint with the error added; radius (M + D·r)/\|b\|_lower with D = sup\|r.b.d − b\|, outward. This is C1–C2: \|f(d)\| ≤ M and f(d) = f(a) + b(d − a) + E, \|E\| ≤ D\|d − a\|. ✓
- **Discard** only when the tile box and the box of the necessary disc are disjoint. Domain errors (pole, log, slope, ξ = 0) → UNRESOLVED, tile retained in the hull; other exceptions abort the run with exit 3 (never a discard). ✓
- **Negative controls:** no arguments → exit 64; the JSON passed as transfer → exit 3 (`wrong transfer header`). ✓
- **Consistency with the estimated true point** ([NUM], PR #301 §1): d* ≈ −4.32·10⁻⁹ + 1.99·10⁻⁸ i lies in tiles 26, 34 (N = 8) and 43, 53 (N = 10); all four are KEPT.

## R4 — input dependence

`import_phi40.py` pads the 80-digit midpoint strings `info.coefficients[k]` (k = 2..40) by 10⁻⁶⁵ and the 40-digit `info.c_pil` by 10⁻³². The strings are `mid().str(80, radius=False)` of the stage-2 balls (scout l. 105, 192). Owner check (`evidence/dyad/open20-an/cpp-review/f1-tube/dyad_open20_cpp_f1_transfer_check.py`, ball arithmetic, 400 digits, against the library recursion `coefficients(K, 40)` and `Consts().c`):
- max over k of \|string − library ball\| ≤ **2.81·10⁻⁸¹** (pad 10⁻⁶⁵);
- \|c string − c\| ≤ **3.86·10⁻⁴¹** (pad 10⁻³²).

**PASS.** The transfer boxes contain the coefficient balls of the library, with margins of 16 and 8 orders. This replaces the display assumption by a check, but only relative to the library recursion of stage 2 (the source the proof record already uses); it is not an independent regeneration in C++.

## R5 — scope

Three levels, kept apart:
1. **Theorem-type content of the code (if R1–R4 hold):** for every tile and every d in it, *if* the image base x₁(d) lies in D₀ and \|d₁(d)\| ≤ R₀(x₁(d)), then d lies in the necessary disc; tiles whose box misses it contain no such d.
2. **Hypothesis not proved here:** that the curve through ξ* exists, is a graph over the fibre, and its first image lies in D₀ inside the tube (seed and tube lemmas; the point jump is not certified).
3. **Numerical campaign:** the 8×8 and 10×10 results below and the mpmath spot-checks (352/352 and 562/562 samples inside D₀, max R/M = 0.712 and 0.765) are [NUM]/SESSION.

## Reproduction (REVIEWER-REPLAYED, SESSION)

Owner container, g++ 13.3.0, Boost.Multiprecision headers, the co-owner's `run_ubuntu_f1.sh` unchanged; outputs in `evidence/dyad/open20-an/cpp-review/f1-tube/run-local/` (transfer SHA-256 `3fea1c3d194d691a7bfd4d0a853f0acbd16c6f11f6ee873fa48603092719fae8`):

| grid | tiles | unresolved | discarded | kept | M_min | M_max | hull radius |
|---|---|---|---|---|---|---|---|
| 8 | 60 | 0 | 44 | 16 | 2.708876·10⁻⁴ | 2.987379·10⁻⁴ | 1.526194·10⁻³ |
| 10 | 96 | 0 | 80 | 16 | 2.516209·10⁻⁴ | 2.783942·10⁻⁴ | 1.198129·10⁻³ |

These equal the co-owner's local figures. The hull shrinks from 0.002 to 1.2·10⁻³ in one block; the [NUM] target of #301 §3.2 is a factor 7. The PI server run is not needed for this review; it can be added later as a third machine.

## Minor remarks (no change required)

- m1. `check_m_samples.py`: the sample directions ±1/2 appear twice.
- m2. The usage line advertises grid 16; the run script uses 8 and 10 only.
- m3. When Re ξ ≤ 0 on a box, M falls back to the chart cap 0.3π; the fallback is correct. The details files do not record which tiles used it; a column for the flags `used_tau` / `used_local_angle` would make that visible.

## O-1 (owner finding, Python library, outside this package)

The library floors `second` with **`TB.cw.upper()`** (`R_upper` l. 1193, `_piece_check` l. 837, l. 956), while D_j is defined by second > c_j with c_j = second(ξ*) − 0.15, a real number of which `TB.cw` is a ball. Taken literally, second ≥ cw.upper does not follow from second > c_j; the gap is the ball radius (3·10⁻⁴⁶ at 160 bits, 4·10⁻³⁹⁸ at 400 digits), so it is a formal gap, not a numerical one. The C++ code uses `cwall.l` and is not affected.
**Proposed resolution (needs a PI decision):** fix the wall constant as the dyadic upper end of the computed ball (c_j := cw.upper()), and say so in proof record §1. Then every use is consistent: the out-test (second ≤ cw in ball arithmetic) implies second ≤ c_j, the floors become exact, and ξ* stays inside with margin 0.15. Changing the code to `cw.lower()` would also close it but changes adopted evidence. This touches the 3c-a record and should be settled before any 3c-b production.

## Next

- PI: put `DYAD_CPP_F1_TUBE_CONTRACTOR.zip` unchanged on an `upload/...` branch (hash above).
- Co-owner: proceed to horizon 2 and finer tiles per #301 §3; the review conditions of R3 carry over unchanged.
- PI decision on O-1.
