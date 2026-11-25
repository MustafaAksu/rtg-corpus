# F3-FINITE-JET-CONTROL — stage 2 driver, coverage certificate and K = 8 pilot

**13 October 2026 · NONCANONICAL · Triadic contributor deliverable.** Not a region certificate. The full sweep has not been run; the four pilot boxes are the only computed boxes. κ̃ = 1.

## 1. Deliverables and governing hashes

| File | SHA-256 | Role |
|---|---|---|
| `triad_tm_engine_v3.py` | `78a5e434073165b37e9e5457766b6d21edb63e51d076172f4ac92052c63bfd18` | v2 engine + recording hooks; **no arithmetic change** (diff vs v2: `configure(K)`, per-step records in `Fmap`, `certify_box` returns post-map radius, τ+1 interval, six step records, transverse defect; `R_eff`; main block removed) |
| `triad_stage2_driver.py` | `5268d037ba15ec7f7787e8cb2b67e6918479283ee12cae8635b33290e1f78e63` | resumable sweep driver |
| `triad_stage2_coverage.py` | `2b5a9ff81f97af068d29f0293f459b58ba3defbc78bd2533a055caacd122555b` | coverage certificate + aggregator |
| `stage2_config.json` | `73389a2b83bac9fd2c55db779c9509c4865edada2d830568f97782a5ec455549` | region/tiling/K/dps contract (default: K = 8) |
| `age_family_polynomials_kt1.json` | `03042f84…d83c` | coefficient table (unchanged) |

## 2. Region, tiling and coverage proof
Region: 0.03 ≤ |s|₂ ≤ 0.08, τ ∈ [0, 2], all as exact decimals in the config. Tiling: origin-anchored Cartesian squares of side 2h — inner ring h = 0.0025 for |s| ∈ [0.03, 0.05], outer ring h = 0.005 for [0.05, 0.08]; τ-layers [0, 1], [1, 2]. A square is selected iff it meets its sub-annulus (exact rational min/max-distance test). Plan: 272 inner + 180 outer squares per τ-layer = **904 box-runs per N** (Triadic's estimate of 896 confirmed up to tiling detail).
Coverage certificate (structural): the squares tile the plane, so each point s of a sub-annulus lies in some square Q with dist(Q, 0) ≤ |s| ≤ R_hi and maxdist(Q, 0) ≥ |s| ≥ R_lo, hence Q is selected; τ-layers are checked contiguous and spanning. `triad_stage2_coverage.py` re-derives the plan from the config, states this argument, runs a 20 000-point sampled membership sanity check (0 misses), and counts PASS records with matching engine/poly/config hashes; it exits 0 only when every planned (box, N) has such a record and then prints K_N = max K_up (upward). Boxes straddling the inner circle are certified for s in box ∩ {|s| ≥ R_lo} via R_eff = max(R_min, R_lo) (exact).

## 3. Record contract (one JSON line per box and N)
Box id, ring, exact rational endpoints r, e, τ; engine/poly/config SHA-256; K, dps, κ̃; status; R_min, R_max, R_eff (outward); bound_B_up, centre_abs_up, K_up, K_perp_up (upward-rounded to 4 significant digits) plus K_raw; ρ_s, ρ_c, λ_last, L_C, post-map radius Rm, τ+1 interval; six per-step records (enlarged-region component bounds, edge bound a, λ, fresh and transported remainders); seconds. Transverse channel: |𝓔_⊥|_B = |B(𝓔, J_Q s)|/|s|_B with |J_Q s|_B = |s|_B, i.e. the B-orthogonal component relative to D₅ ∥ s, bounded as (√3/2)·bound(s_e𝓔_r − s_r𝓔_e)·√2/R_eff + ρ_c + L_C ρ_s; reported separately from the total and never identified with w₁₃. Resume: a (box, N) is skipped only if a PASS record with all three hashes matching exists; FAIL records carry the exception and are never counted.

## 4. Pilot (four corner boxes; `stage2_pilot_K6.jsonl`, `stage2_pilot_K8.jsonl`)

| box (ring, r-range, e-range, τ) | N | K = 6: K_up / K_perp / ρ_c / s | K = 8: K_up / K_perp / ρ_c / s |
|---|---|---|---|
| inner [0.025, 0.03]×[−0.005, 0], τ∈[0,1] (angle 0, R_eff 0.03) | 7 | 1.467 / 1.456 / 1.1e-14 / 63 s | 1.445 / 1.434 / 2.2e-18 / 324 s |
| | 8 | 23.56 / 23.56 / 1.1e-14 / 77 s | 22.82 / 22.83 / 2.6e-18 / 366 s |
| inner [−0.025, −0.02]×[0.02, 0.025], τ∈[0,1] (≈135°) | 7 | 3.734 / 3.808 / 1.3e-14 / 63 s | (running) |
| | 8 | 323.1 / 374.0 / 1.3e-14 / 76 s | (running) |
| outer [−0.06, −0.05]×[0.05, 0.06], τ∈[0,1] (≈135°, R ∈ [0.0707, 0.0849]) | 7 | 18.59 / 22.13 / 2.9e-12 / 62 s | (running) |
| | 8 | 394.1 / 465.3 / 3.2e-12 / 74 s | (running) |
| inner [−0.025, −0.02]×[0.02, 0.025], τ∈[1,2] | 7 | 8.463 / 8.893 / 1.3e-14 / 69 s | (running) |
| | 8 | 291.5 / 336.9 / 1.4e-14 / 76 s | (running) |

Findings. (i) **Degree:** K = 8 tightens K₇ by 1.5 % and K₈ by 3 % over K = 6 at ≈5× the cost; the transported remainders are 10⁻¹⁴ (K = 6) vs 10⁻¹⁸ (K = 8) against polynomial parts of 10⁻¹², so the slack is the box's R-spread (up to (R_max/R_min)^{N+1}) and the triangle-inequality range bound, not the remainder. K = 6 is adequate for the sweep; a K = 5 trial could be considered for the inner ring. (ii) **Wide τ-boxes (h_τ = 0.5) cost nothing** at K = 6: remainders unchanged from the h_τ = 0.05 stage-1 runs. (iii) **Outer ring:** λ rises to 0.22 and remainders to 3·10⁻¹², still four orders below the polynomial part (10⁻⁸); the engine is comfortable at R = 0.085 with h = 0.005. (iv) **τ-dependence is real for N = 7 at the Q_s-maximal angle:** K₇ = 3.73 on τ ∈ [0, 1] vs 8.46 on [1, 2], consistent with Δ_τ𝒞₈ = D₈ + τB₈. (v) **Transverse channel** is of the same order as the total everywhere sampled (K_perp/K between 0.98 and 1.19): the defect is not predominantly along D₅.

Timing for the sweep at K = 6: 904 boxes × (63 + 76) s ≈ 35 core-hours; on an 8-core RTG machine ≈ 4.5 h wall. At K = 8 ≈ 5× that.

## 5. Recommended stage-2 run (RTG machine)
`stage2_config.json` with K = 6 (edit the one field; the config hash then governs), `python triad_stage2_driver.py --config stage2_config.json --only inner` and `--only outer` in parallel processes writing to separate result files (set `results` per config copy), then concatenate and run `triad_stage2_coverage.py`. Expect the global K_N to be set by the outer ring at the Q_s-maximal angle and, for N = 7, by the τ ∈ [1, 2] layer. A refinement pass with h halved on the worst boxes is a one-line config change and reuses the resume mechanism.

## 6. Non-claims
No K_{7,2}, K_{8,2} over the region yet; no multi-step control; no observable contract; the Taylor-model lemmas (product truncation, Lagrange remainders, remainder transport through A⊕A, post-map Lipschitz radius) are implemented as documented in the stage-1 note §2 and §6 but have not had an independent line-by-line proof review of the engine, which Triadic listed as a prerequisite before any RER `CONTROLLED_APPROXIMATE_CLOSURE` record.
