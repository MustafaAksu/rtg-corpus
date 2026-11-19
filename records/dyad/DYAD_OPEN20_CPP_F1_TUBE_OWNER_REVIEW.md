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

---

# Addendum — F2: two-block successor (17 November 2026, evening)

**Reviewed:** `DYAD_CPP_F2_TUBE_CONTRACTOR.zip`, SHA-256 `b30dda66278ee6e21fde8b040f80abebb9ad534c906e3cb9613112b5e30d378e`, on branch `upload/dyad-cpp-f2-20261117` (head `596c2319f8edd27fc4ed136f7757cf43abc7d326`, pushed by the PI from the server together with his run outputs, `pi-run/`). Inner `SHA256SUMS.txt` 7/7 OK. Main source `real_f2_tube.cpp` (140 lines), read in full; it includes the unchanged F1 source and the reviewed engine.
**Request:** the package's `OWNER_REVIEW_REQUEST.md`, F2-R1 to F2-R5.

## Verdict

**ACCEPT as a development checkpoint, at SESSION scope.** F2-R1 to F2-R4 pass by reading. The owner rerun of the unchanged runner gives outputs **byte-identical** to the PI's server run (§F2-R5). The status of everything is the same as for F1: conditional on the graph/tube hypotheses, not a certificate, no point jump.

## F2-R1 — the two-step induction

Hypothesis (as in R5 above, now for two blocks): the candidate d* satisfies, for k = 1, 2, x_k(d*) ∈ D₀ and \|d_k(d*)\| ≤ R₀(x_k(d*)).
1. Step 1 is the F1 step unchanged in substance (same calls: whole-tile flow, centre point flow, mid slope, `necessary_disk`, box intersection). So d* ∈ tile implies d* ∈ after1 = tile box ∩ box of the first necessary disc.
2. `split_box(after1, 4)`: the 16 rectangles cover after1 (below). So d* lies in some part P.
3. `ball(P)` ⊇ P ∋ d*. Extra points in the disc only weaken the bound; they cannot remove d*.
4. `iter(x*, ball(P), φ, 2)`: `from_lift` once, two `direct6` blocks, `lifted_readout` once at the end. `Tcentered` composes the tangent as Σ J_ij · tangent_j with J the Jacobian enclosure over the whole state box: the chain rule with an enclosure of DT on a set that contains every intermediate state. The tangent is never reset. So `R2.b.d` encloses ∂d₂/∂d₀ on all of ball(P), and `R2.a.v` encloses x₂ there.
5. \|d₂(d*)\| ≤ R₀(x₂(d*)) ≤ M₂ := `upper(R2.a.v)` (F1-R1 applies unchanged, on X₂ ∩ D₀). C1–C2 then gives d* ∈ necessary disc 2, so d* ∈ P ∩ box(disc 2).
Step 2 uses only the k = 2 condition on P ⊂ after1; it does not need to repeat k = 1. ✓

## F2-R2 — the bound at both bases; exceptions; wall

- M₁ = `upper(X₁)`, M₂ = `upper(X₂)`, each the F1-reviewed bound on X_k ∩ D₀; no claim X_k ⊂ D₀; no sampled or Python value enters. ✓
- A `domain_error` at step 1 keeps the whole tile in the final hull; at step 2 it keeps P (the box the candidate is known to be in at that point). Other exceptions end the run with exit 3, never a discard. ✓
- **Wall.** The C++ floor `cwall.l` is the lower end of a 256-bit enclosure of second(ξ*) − 0.15. It is ≤ c₀ for the current definition. It is also ≤ c₀ under the O-1 proposal (c_j := upper end of the library ball, which is ≥ the real value). So the C++ code is valid under both. ✓
- **O-1 status.** The co-owner's request calls the proposal "PI-approved". This review has no record of a PI decision on O-1. Until the PI decides, O-1 is open. The co-owner's point is right: if adopted, c_j must be fixed as one exact dyadic number with its provenance (precision, routine), not as whatever `cw.upper()` gives at the working precision of a run.

## F2-R3 — tiling, coverage, hull

- `split_box`: with Δ = h − l ≥ 0, the pieces are [l + ⌊Δi/n⌋, l + ⌈Δ(i+1)/n⌉]. The first starts at l, the last ends at l + Δ = h, and each piece ends at or after the start of the next (⌈·⌉ ≥ ⌊·⌋). So the union is the whole box, for any signed l (only Δi ≥ 0 is divided). ✓ The unit test samples 17 × 17 points; the argument above covers all points.
- Discard only on empty intersection; F1-excluded tiles leave no row in the final hull; unresolved tiles keep their whole box. ✓
- **Hull radius.** `enclosing_disk` uses `norm_upper`, the \|Re\| + \|Im\| bound about the box centre. The printed radii are therefore L¹ radii, an upper bound on the Euclidean radius (at most √2 times it). The F1 radii above use the same convention, so the F1 → F2 comparison is like for like. ✓
- Negative controls: no arguments → 64; JSON as transfer → 3; subdivision 7 → 3. ✓
- Detail TSV: the package's integer checker passes on both grids. **Independent check against #301:** the estimated d* lies in subtiles (25,15), (26,12), (33,3), (34,0) for 8×8 and (42,15), (43,12), (52,3), (53,0) for 10×10. All are RETAINED at both steps.

## F2-R4 — sources and dependencies

- F2 zip hash matches on the PI server and here. Runner gates: the F2, F1, benchmark and V2 package sums and the pinned stage-2 JSON. ✓
- The F1 source is included under a renamed `main`, unchanged; bench.cpp, `centered_evaluator.hpp` and `independent_core.cpp` come from the reviewed packages, unchanged. ✓
- The coefficient transfer is the one checked in R4 above (against the library recursion; not a C++ regeneration). Output `phi40_outer_256.txt` is identical on both machines.
- The PI's `unzip` prompt (an older SHA256SUMS not replaced): the PI-side `f2_package_checks.txt` equals the owner's, and every result file is byte-identical to the owner's run from the hash-verified zip. That rules out a stale source in effect.

## F2-R5 — scope and the runs

| run | status | grid / subdiv | step 1: excluded / kept | step 2: subtiles / excluded / kept | unresolved | M₂ range | L¹ radius F1 → F2 |
|---|---|---|---|---|---|---|---|
| PI server, 17 Nov 14:01 UTC | PI-RUN | 8 / 4 | 44 / 16 | 256 / 96 / 160 | 0 | 6.016285·10⁻⁵ – 8.930092·10⁻⁵ | 1.526194·10⁻³ → 1.296767·10⁻³ |
| PI server | PI-RUN | 10 / 4 | 80 / 16 | 256 / 128 / 128 | 0 | 5.585222·10⁻⁵ – 7.644073·10⁻⁵ | 1.198129·10⁻³ → 9.656854·10⁻⁴ |
| owner container | REVIEWER-REPLAYED | both | identical | identical | 0 | identical | identical |

`compare_pi_vs_owner.txt` (evidence `cpp-review/f2-tube/`): 21 of 23 files identical; the two that differ are `environment.txt` (time, repo head, Python version) and `RUN_SHA256SUMS.txt`, which hashes `environment.txt`.
The co-owner's local proxy figures (18-digit coefficients) are a third level ([NUM]); they agree to the printed digits but are not evidence for the source-backed run.

**Reading of the numbers ([NUM]).** M₂ is about 1.3–2× the true R₀(ξ₂) ≈ 4.5·10⁻⁵ of #301, as a bound should be. The radius falls only about 15–20 % from F1 to F2, against the factor of about 30 that an exact derivative would give (#301 §3). The D·r term still dominates. Finer parts at step 2 (or per-T mean-value updates) will gain more than further blocks; adding blocks on the present parts mainly increases D.

## Next

- Co-owner: before a five-block run, measure on the step-2 parts how D·r and M₂ compare (one column each in the TSV is enough), and use that to choose subdivision against horizon.
- PI: decide O-1. If accepted, the owner fixes c₀ and c₁ as exact dyadic numbers with provenance in proof record §1, on a separate branch.
- No 3c-b, no certificate, no point jump. B-an and B-6 ACTIVE.

---

# Addendum 2 — selective second-stage refinement (18 November 2026)

**Reviewed:** `DYAD_CPP_F2_SELECTIVE_REFINE.zip`, SHA-256 `a900d31a88725dc0a0870b84ab5ee0658971d62399b7da9583263fe98b35f3ae`, on `upload/dyad-cpp-f2-selective-20261118` (head `0a658b85fbc41659f4e72b2b7f0e550a730763e3`). The branch also carries the PI's 4×4 and 8×8 term runs (`pi-run/sub4`, `pi-run/sub8`). The PI's selective run is on `upload/dyad-cpp-f2-selective-results-20261118` (head `fc84ab66a7f49e21b2726d79147686a47a44f6c6`). Dependency used for the 8×8 source run: `DYAD_CPP_F2_TERM_AUDIT_SUB8.zip` `1677b05a…ea16` (on `main`, `upload/dyad-cpp-centered-20261116/received/`). Its diagnostic differs from the 4×4 term audit (`b2a0f428…d6c0`) only in admitting subdivision 8 and a limit up to 1024 (diff checked).
**Request:** the package's `OWNER_REVIEW_REQUEST.md`, S1 to S5.

## Verdict

**ACCEPT as a development checkpoint, at SESSION scope.** S1 to S4 pass by reading. The owner replay of both the 8×8 source run and the selective run is byte-identical to the PI's runs in every result file. The status is unchanged: conditional on the graph/tube hypotheses; no certificate, no point jump.

## S1 — the frozen source selection

- `read_prior` rejects a wrong header, extra or missing fields, any row that is not VALID, any action other than RETAINED/EXCLUDED, indices out of range, duplicates, rows that break the integer identities Dr = ⌈D·r⌉ and radius = err + ⌈(M + Dr)/|b|⌉, and any run that does not have exactly 1024 rows, 100 RETAINED and 16 first-stage tiles with 64 rows each.
- The 924 EXCLUDED parents are not replayed. Their exclusion rests on the 8×8 run of `f2_term_diagnostic_sub8.cpp`. That code is the reviewed F2 step (same `iter`, `upper`, `necessary_disk`, `intersection`; exclusion only on an empty intersection; `domain_error` → UNRESOLVED and kept). The log does not store the box endpoints, so an exclusion cannot be rechecked from the log alone. It is rechecked here by the **owner replay of the whole 8×8 run** (§S5), whose `terms.tsv` is byte-identical to the PI's.
- The 100 RETAINED parents are recomputed by the original F2 calculation, and the run stops unless all seven recorded integers (M₂, Dr, D, r, |b|_lower, recentring error, radius) are equal. This also fixes the index correspondence between the log and `split_box(after1, 8)`. ✓

## S2 — the retained set

The parent rectangle is `intersection(part, N2.box())`, the same expression as `after2` in F2, recomputed from the same disc. `split_box(·, 2)` covers it (Addendum 1, F2-R3). A candidate in the parent lies in some child. Children are cut from the post-F2 rectangle, not from the wider part. ✓

## S3 — the child bound

For each child: `ball(child)`; two unreset `direct6` blocks from the lift; whole-disc tangent; M₂ from the child's own X₂ ∩ D₀ (`upper`, F1-R1); the C1–C2 disc, with its radius identity checked; exclusion only on an empty intersection with the child. A `domain_error` keeps the child box. At the parent level a `domain_error` ends the run with exit 2 and no narrower claim. Other exceptions → exit 3. The final hull is required to lie inside the prior hull. ✓

## S4 — the output

The package checker, re-run here, passes: every child is `split_four(parent)[k]`, lies in its parent, and the four children of each parent are all present; every VALID row satisfies the integer identities; RETAINED ⇔ non-empty intersection, and the stored final box equals that intersection; 400 rows, 100 parents. The prior hull is recomputed from the 100 parent rectangles and equals the 8×8 run's `final_L1_hull` (5.723708·10⁻⁴). The counts 100 + 400 involve no repetition of the 924. ✓

## S5 — evidence and replay

| run | status | result |
|---|---|---|
| 8×8 source (grid 8, sub 8) | PI-RUN 17 Nov; REVIEWER-REPLAYED 18 Nov | 1024 rows: 924 excluded, 100 retained, 0 unresolved; L¹ hull 5.723708·10⁻⁴; `terms.tsv` SHA-256 `1f5fa762…6e72` |
| selective (100 parents × 2×2) | PI-RUN 18 Nov; REVIEWER-REPLAYED 18 Nov | 400 children: 256 excluded, 144 retained, 0 unresolved; L¹ hull 2.501176·10⁻⁴; `selective_children.tsv` SHA-256 `3566a7c7…6579` |

Byte comparison (`evidence/dyad/open20-an/cpp-review/f2-selective/compare_pi_vs_owner.txt`): every result file is identical. The only files that differ are `environment.txt` (time, repo head, Python), the `RUN_SHA256SUMS.txt` that hashes it, and `stage2_source_check.txt` (it prints the local path). The executables were not compared.
This is a replay of the same code on a second machine, not an independent implementation. The co-owner's integer check of the outputs (#305 comment `6974990978`) is a third, independent reading of the same rows.

**Matched scaling (co-owner's `matched_scaling.py`, re-run here on the PI 4×4 log and the owner's 8×8 log):** median child/parent ratios r 0.5, D 0.443, D·r 0.221, M₂ 0.759, D·r/M₂ 0.292. These are the figures of comment `6971328504`, now from deposited files.

## Reading ([NUM])

- On the selected children, D·r/M₂ has median 0.549 and max 0.555 (min 0.081). The derivative term is now below the tube term on every child. Further subdivision gains less than before. The radius M₂/|b| becomes the main limit.
- The L¹ hull is 2.5·10⁻⁴, about 8 times smaller than 0.002. The W8 distance between the two centres (about 1.95·10⁻⁸, co-owner's figure) is still about 10⁴ times smaller. Two blocks cannot close this gap: M₂ itself is of order 10⁻⁵ to 10⁻⁴. The next lever is the horizon (more blocks shrink M_k, #301 §1), now on the small retained set rather than on the whole fibre.

## Next

- Co-owner: a horizon step (k = 3 to 5) on the 144 retained children, with the same rules (own M_k, whole-disc derivative, unresolved kept), and the D·r/M_k column. Compare its cost with one more 2×2 split.
- The 924 + 256 exclusions stay valid only together with the logs they come from; any later stage must cite both run hashes above.
- No 3c-b, no certificate, no point jump. B-an and B-6 ACTIVE.

---

# Addendum 3 — horizon 3 against a further 2×2 split (18 November 2026, evening)

**Reviewed:** `DYAD_CPP_F3_HORIZON_DIAGNOSTIC.zip`, SHA-256 `0bee93e58d7df73525a5817e7340a9258d8e13bb63065ddbbdc535accceec379`, on `upload/dyad-cpp-f3-horizon-20261118` (head `c500a6dc1b1598fce9c08c766bf89668c609b335`); inner `SHA256SUMS.txt` 10/10 OK. PI run on `upload/dyad-cpp-f3-horizon-results-20261118` (head `1c980e945a870d4d14db77cf19dca0831e8b457c`). New source `horizon.cpp` (193 lines), read in full; it includes the reviewed selective, F2, F1 and engine sources unchanged.
**Request:** H1 to H5 of the package's `OWNER_REVIEW_REQUEST.md`.

## Verdict

**ACCEPT as a development experiment, at SESSION scope.** H1 to H4 pass by reading; the owner replay of `compare` gives the same `details.tsv` for both modes and the same counts, M ranges, ratios and radii; only wall-clock times differ. Scope as before; for `h3` the hypothesis now also covers k = 3 (x₃ ∈ D₀, \|d₃\| ≤ R₀(x₃)).

## H1 — frozen source

`load_checked_source` rejects a wrong header, missing or extra fields, inverted boxes, IDs out of range, duplicates, non-VALID rows, broken integer identities (Dr, radius, and necessary-box width = 2·radius), a child that is not `split_box(parent, 2)[k]`, a RETAINED row whose final box is not the intersection, an EXCLUDED row whose intersection is not empty, and any count other than 400 / 144 / 256 / 100 parents with four children each. Each of the 144 retained rows is then recomputed by the unchanged F2 code, and the run stops unless all seven integers, the necessary box and the final box agree. The 256 excluded rows are not recomputed; they rest on the selective run, which was replayed (Addendum 2). ✓

## H2 — the horizon step

`h3`: on each retained final box b, `ball(b)`, three `direct6` blocks from the original lift (`f2::iter(…, 3)`, tangent never reset), M₃ = `upper(X₃)` from the box's own base, C1–C2 at k = 3. `refine2`: `split_box(b, 2)` and the k = 2 step on each child. Both are necessary conditions on the same candidate set; their results could also be intersected. `h5` exists and was not run. ✓

## H3 — retention and arithmetic

Exclusion only on an empty intersection with the probe box; `domain_error` keeps the probe box (a subset of b); other exceptions → exit 3; counts are checked (144 replays; 144 or 576 evaluations) and the final hull must lie in the source hull. The package checker (`check_horizon.py`) passes on both modes here. ✓

## H4, H5 — comparison and provenance

| mode | evaluations | excluded / retained / unresolved | M range | Dr/M median | L¹ hull 2.501176·10⁻⁴ → | owner time |
|---|---|---|---|---|---|---|
| h3 | 144 | 4 / 140 / 0 | 1.79–4.46·10⁻⁵ | 8.39 | 2.499532·10⁻⁴ | 74 s |
| refine2 | 576 | 252 / 324 / 0 | 4.49–4.82·10⁻⁵ | 0.144 | 1.707123·10⁻⁴ | 137 s |

PI-RUN and REVIEWER-REPLAYED agree in every result file (`evidence/dyad/open20-an/cpp-review/f3-horizon/compare_pi_vs_owner.txt`; 25 files identical, the rest differ only in times, local paths or the hash lists of those). Same code on two machines, not an independent implementation. Coefficient transfer as in R4. ✓

## Reading ([NUM]) — where the two-block route stops

From the `details.tsv` files (owner computation):
- `refine2`: box radius r ≈ 1.6·10⁻⁵ (median), but the necessary-disc radius is ≈ 8.5·10⁻⁵, with the tube-only part M₂/\|b₂\| ≥ 6.95·10⁻⁵ (median 7.4·10⁻⁵, \|b₂\| ≈ 0.65). The discs are already about five times larger than the boxes. Further 2×2 splits at k = 2 can only cut the candidate set down to roughly the intersection of these discs, a set of radius of order M₂/\|b₂\| ≈ 7·10⁻⁵. **The two-block route saturates near an L¹ hull of about 10⁻⁴**, a factor below 2 from the present 1.7·10⁻⁴.
- `h3`: the tube-only part is smaller, M₃/\|b₃\| from 2.2·10⁻⁵ (median 5.5·10⁻⁵), but D₃·r is about 8 M₃ on the present boxes (r ≈ 3.1·10⁻⁵). With D ∝ r^{1.17} (Addendum 2), halving r divides D·r by about 4.5, so on the 324 `refine2` boxes (r ≈ 1.6·10⁻⁵) one expects D₃·r ≈ 2 M₃, and on their 2×2 children ≈ 0.4 M₃.
- So the next gain needs both: smaller boxes **and** k = 3. A horizon step pays only once r is below about M_k/D_k (per unit of r).

## Next

- Co-owner proposal (a k = 3 pilot on the 324 `refine2` boxes): agreed. A subset is not needed: from the times above, all 324 at k = 3 cost about 3 minutes. In the same run, k = 3 on their 2×2 children (1296 evaluations, about 11 minutes) gives the combined split + horizon point, which the estimate above says is the one that should work.
- The 252 new `refine2` exclusions depend on the selective run and on the 8×8 run; cite all three log hashes.
- No 3c-b, no certificate, no point jump. B-an and B-6 ACTIVE.

---

# Addendum 4 — k = 3 on the 324 refined survivors (19 November 2026)

**Reviewed:** `DYAD_CPP_F3_ON_REFINED_324.zip`, SHA-256 `499db143cb952a2d663c967e64866c136064487a84d00ecc7ac4ee857c8b5c74`, on `upload/dyad-cpp-h3-refined-20261118` (head `f873c643299ef99a79d9985673dbc997de4fafe7`); inner sums OK. PI run on `upload/dyad-cpp-h3-refined-results-20261118` (head `c7699269162b4debf42815d2d5b56d35b5c687de`). New source `h3_refined.cpp` (197 lines), read in full; it includes `horizon.cpp` and everything below it unchanged.
**Request:** K1 to K5 of the package's `OWNER_REVIEW_REQUEST.md`.

## Verdict

**ACCEPT as a development experiment, at SESSION scope.** K1 to K3 pass by reading. The owner replay of `compare` gives byte-identical `details.tsv` for both modes (SHA-256 `b285d0dc…dd0d` for `h3_324`, `3f3ac0df…7325` for `h3_split2`); summaries differ only in times. The hypothesis now covers k = 1, 2, 3.

## K1 — the cumulative cover

`load_frozen` reads the `refine2` log of the horizon run (SHA-256 `bf9d4507…7a1a`, identical to the owner's replay in Addendum 3) on top of the checked selective log. It rejects wrong headers or fields, inverted boxes, IDs out of range or not among the 144 selective survivors, duplicates, non-VALID rows, a parent rectangle different from the selective final box, a child that is not `split_box(parent, 2)[k]`, broken integer identities, RETAINED/EXCLUDED rows inconsistent with the stored intersection, and any count other than 576 / 144 parents × 4 / 324 kept / 252 excluded. Then the 144 selective survivors (`horizon::replay`) and the 324 `refine2` survivors (`replay_frozen`, unchanged F2) are recomputed, and the run stops on any difference in the seven integers, the necessary box or the final box. The earlier exclusions (924 + 256 + 252) are not re-evaluated or counted again. ✓

## K2 — the two k = 3 modes

`h3_324`: each of the 324 final rectangles; `h3_split2`: `split_box(·, 2)` of each (1296). Both use `f2::iter(…, 3)` from the original lift over the current disc, M₃ = `upper(X₃)` of that disc, the C1–C2 disc, exclusion only on an empty intersection, `domain_error` → the current rectangle kept, other exceptions → exit 3; counts and hull inclusion are checked. ✓

## K3, K4 — output and replay

The package checker passes here on both modes. Results (identical PI-RUN and REVIEWER-REPLAYED):

| mode | evaluations | excluded / retained / unresolved | M₃ range | Dr/M₃ median | L¹ hull 1.707123·10⁻⁴ → | owner time |
|---|---|---|---|---|---|---|
| h3_324 | 324 | 72 / 252 / 0 | 1.68–2.50·10⁻⁵ | 2.88 | 1.659646·10⁻⁴ | 160 s |
| h3_split2 | 1296 | 972 / 324 / 0 | 1.63–1.97·10⁻⁵ | 0.818 | 8.790759·10⁻⁵ | 396 s |

Owner recomputation from the TSV files confirms the co-owner's figures (#305 comment `7018240286`): the 324 retained children come from 100 of the 324 parents (0 / 1 / 2 / 4 children kept for 224 / 4 / 32 / 64 parents); on them, median r = 7.81·10⁻⁶, M₃/\|b₃\| = 2.42·10⁻⁵ (minimum 2.41·10⁻⁵), necessary radius 4.39·10⁻⁵, \|b₃\| ≈ 0.81.

## K5 — scope

Same-engine conditional numerical development; not an independent implementation, not a proof of the graph or tube, not a jump. O-1 is PR #312, not merged at the time of writing.

## Reading ([NUM], [HEUR])

- The pattern of Addendum 3 repeats one block later. At k = 2 the cover stalled at a disc floor M₂/\|b₂\| ≈ 7·10⁻⁵; at k = 3 the floor is M₃/\|b₃\| ≈ 2.4·10⁻⁵, a factor of about 3 per block, and the retained boxes (r ≈ 8·10⁻⁶) are again about 5 times smaller than the discs. Further splitting at k = 3 cannot go much below an L¹ hull of a few 10⁻⁵.
- So the working rule is: **at each horizon, split until D_k·r is below M_k, then add a block.** The number of live boxes then stays roughly constant (here 100 to 300), and each evaluation costs k blocks.
- Scale to the target, from the #301 table (true R₀ along the orbit, not enclosures): the tube-only floor is about 0.002 × 1.7·10⁻³ ≈ 3·10⁻⁶ at k = 5, 2·10⁻⁷ at k = 10 and 7·10⁻⁹ at k = 20, against the W8 centre distance ≈ 2·10⁻⁸. The present enclosed floors are within a factor of about 2 of the true ones at k = 2, 3. A horizon of about 15 to 20 blocks is therefore the order needed, not 4 or 5. This is an estimate for planning, not a claim.

## Next

- The co-owner's 4-block comparison (direct and with 2×2) is a reasonable next measurement. Expected [HEUR]: direct k = 4 on the 324 boxes behaves like `h3_324` (Dr/M₄ of a few); k = 4 with 2×2 works.
- More useful than one more pairwise comparison would be a small **adaptive driver** that applies the rule above: for k = 4, 5, …, split the retained boxes until the median Dr/M_k < 0.5, evaluate, keep the log, and stop at a fixed budget. Same rules as before (own M_k, whole-disc tangent from the original lift, unresolved kept, hashes of all source logs). Its output would show directly how the floor and the cost grow with k.
- No 3c-b, no certificate, no point jump. B-an and B-6 ACTIVE.
