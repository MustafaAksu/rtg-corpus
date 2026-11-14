# AZ Action 1 — Stage 2: timing and calibration pilot (plan)

**[SESSION] NONCANONICAL, EXPLORATORY. Not a registration, not a confirmatory run, no claim.** Prepared by the AZ co-owner (Claude), 12 November 2026.

**Authority.** PI, 12 Nov 2026, 16:54 +03:00, project conversation, verbatim: "Stage 1 sonucunun `[NUM diagnostic]` olarak bir sonraki sürüme girmesini ve Stage2 çalışmasının başlamasını kabul ediyorum." Two decisions: (1) the Stage 1 result enters the next AZ edition as a `[NUM diagnostic]` (under the outcome rule; `records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md` §11 item 3) — a separate piece of work, not in this note; (2) Stage 2 starts. This note is the first step of (2). Large runs go to the PI's Ubuntu server (PI, 11 Nov 2026).

## 1. Why a pilot comes first

Stage 2 asks whether the Stage 1 contrast persists at `N = 240, 242, 480` (preregistration §10). Two quantities of the Stage 1 endpoint `Y = 1{M ≥ 100 at T = 800}` are not known at the new `N`, and the Stage 1 data show that they matter:

- **The endpoint is a threshold on a continuum, not a gap.** In the Stage 1 records at `N = 120`, 1,119 runs have `M ≥ 100`; 402 of them reached the cap of 300 and 717 were still between 100 and 299 at `T = 800`; among the runs below the threshold the 99th percentile of `M` is 90 and the maximum 99. A fixed threshold therefore cuts a distribution whose bulk moves with `N` and with `T`.
- **Tails take time.** Among the Stage 1 runs with `M ≥ 100`, the median time to reach 100 nodes is 335 ticks and the 90th percentile 616, of 800. The owner reports a bulk birth rate falling as `N^{-0.869}` at fixed `k/N` (TDR-G v2.12.14 §1; window-dependent exponent). With `T = 800` fixed, a tail at `N = 480` may not have developed; with `T` scaled, the bulk itself grows towards 100.

A registration that fixed `T` and the threshold blindly could manufacture or hide the effect. The pilot measures what is needed to fix them **without looking at any exposure contrast**.

## 2. What is run

`evidence/az/scripts/az_tokres_s2_pilot.py`, plan `pilot`: the **native arm only** — the engine's own initial draw, no token replaced — under the Stage 1 primary profile P1 (engine `4c94d874…a608`, orientation reference `ca59e9b9…d59c`), policy `bound_symmetric`, cap 300. It uses the registered runner as a library (SHA-256 `75c5f139…8992` asserted; unchanged): `load_engine`, `base_draw`, `run_state`, with the exact per-tick law check on.

| Cell | `N` | `k` | `T` | native draws |
|---|---|---|---|---|
| reference | 120 | 8 | 800 | 3,000 |
| | 240 | 16 | 800 and 1,460 | 3,000 each |
| | 242 | 16 | 800 and 1,460 | 3,000 each |
| | 480 | 32 | 800 and 2,670 | 3,000 each |

`k/N = 1/15` as in Stage 1 (`N = 242` with `k = 16`, as `N = 122` had `k = 8`). The second horizon is `800·(N/120)^{0.87}`, rounded to 10, for `N = 240` (1,462 → 1,460) and `N = 480` (2,672 → 2,670). **For `N = 242` the rule gives 1,473 → 1,470; the pilot runs 1,460, the horizon of its neighbour `N = 240`.** This was an oversight in the table, found in review `5875885484` after the pilot had started; it is kept as a fixed value — `N = 240` and `N = 242` share one horizon — and is not changed after the fact (§8). 21,000 runs in all. Seeds derive from the tag `S2-CALIB-PILOT-20261112`; no base draw is shared with Stage 1 (`AZ-TOKRES-S1`) or with a later registered Stage 2 tag.

## 3. What is read from it, and what is not

The summary prints, per cell: run time (sum, median, maximum); and, **for native draws without a resonant seed token only** (`4x ≢ 0 mod N` for all four tokens), the distribution of the final `M` (quantiles, maximum, the fraction with `M ≥ 100`) and the matched threshold defined below. It prints nothing about draws that carry a resonant token. Those records are in the files — about 13 % of the draws at `N = 120`, 6 % at 240, 3 % at 242 and 480 — and are not analysed in the pilot; any use of them belongs to a registered analysis.

**Matched threshold (the quantity the pilot is for).** Let `α` be the fraction of non-resonant native draws with `M ≥ 100` in the reference cell (`N = 120, k = 8, T = 800`, this pilot). For each other cell, `θ(N,T)` is the smallest integer `m` whose exceedance fraction `P(M ≥ m)` among that cell's non-resonant native draws is at most `α`. By construction the unexposed baseline rate is the same in every cell, and at the reference cell `θ ≤ 100`. With about 2,600–2,900 non-resonant draws per cell and `α` near 1 %, `α` is known to about ±0.4 percentage points (95 %).

## 4. How the result will be used

It goes, with the timing, into a **Stage 2 registration** (a new `records/az/` file, its own package hashes, review by the second co-owner, compute authorisation by the PI, as in Stage 1). The design this lane intends to propose there, stated now so that it cannot be shaped by the pilot's outcome beyond the two calibrated quantities:

- contrasts as in Stage 1 (resonant replacement against its detuned neighbour, same base draw; exact McNemar; Holm over the confirmatory family); cells `N = 240, 480` for both resonance orders and `N = 242` for order 1 with the near-quarter control;
- **primary endpoint** `Y = 1{M ≥ θ(N,T)}` with `θ` from §3, at one horizon per `N`, chosen by a rule fixed here: the scaled horizon, unless at the scaled horizon `θ(N,T) > 200` (the bulk too close to the cap of 300 to leave room for a tail), in which case `T = 800`;
- **secondary, reported without a decision rule:** the Stage 1 endpoint `M ≥ 100` at `T = 800` from the same runs (checkpoint `M_at[800]`), and a threshold-free paired comparison of `M` between the resonant and the detuned arm;
- the decomposition `P(Y_N) = p0(N) + P(R_N)·[p1(N) − p0(N)]` estimated from the arms, so that a change of the native tail rate with `N` is not read as a change of the effect.

These are proposals for the registration and its review; the PI decides.

## 5. Limits

Exploratory. The pilot fixes two design quantities and gives run times; it supports no statement about token resonance at any `N`. The matched threshold makes baselines comparable; it does not make cells equivalent in any other respect. The scaling exponent is the owner's full-range fit and is used only to choose a second horizon. No relation to the Hashimoto `4|q` rule or to DZT `q = 4` is implied (SG-DZT-1, SG-AZ-7); nothing here concerns TDR-26.

## 6. Checks made before the run (this session)

- `selftest` (`evidence/az/token_resonance/stage2_pilot/selftest_output.txt`): for eight base draws the pilot's native run equals the registered runner's own BASE arm in `M`, births, steps, checkpoints, cap flag and law counter; the pilot seed differs from the Stage 1 seed of the same index. PASS.
- Plan `test` (three small cells): run, completion marker, `--resume` on a complete directory (cells skipped), summary; a record file altered after completion is refused by `run --resume` and reported by `summary`.
- Timing probe in the session (registered runner, exploratory tag, all arms, 3–6 base draws per cell; only wall time and the native arm's `M` were read): 0.2–0.7 s per run at `N = 120–242`, 1.7 s at `N = 480, T = 2670`, one run of 29 s. The pilot's native runs are cheaper; the whole plan is expected to take one to three hours on one core. This is an estimate.

## 7. Commands (PI's server)

In the project conversation of 12 Nov 2026, as one block: a worktree at the commit of this note, package hash check, `selftest`, `run --plan pilot` (resumable; started detached so that a console timeout does not stop it), `summary`, and upload of the output directory, unchanged, to `upload/az-token-resonance-s2-pilot`.

## 8. Review record and what it fixes for the Stage 2 registration

**Review `5875885484`** (second co-owner, ChatGPT; 12 Nov 2026, 17:12 +03:00; PR #251 at commit `a6d50ad`): *pilot accepted as an exploratory calibration; no stop or restart needed; the confirmatory Stage 2 campaign is not authorised.* The reviewer had not seen the pilot's result files. Its points, all accepted, are obligations of the registration, not changes to the running pilot (the run is pinned to commit `a6d50ad`):

| # | Point | What the registration will do |
|---|---|---|
| 1 | The matched threshold does not guarantee equality: `M` is an integer, so the realised baseline rate can be below `α`, and the step between neighbouring thresholds can be large | Report, per cell, the target `α`, the realised exceedance rate at `θ`, their difference and the uncertainty of both (exact binomial intervals) |
| 2 | A threshold above the cap (`θ = 301`) makes the event impossible | Such a cell is not a valid calibration. Stop rule, fixed here: a cell is used only if `θ ≤ 200` at the chosen horizon (plan §4) **and** the realised rate lies within the 95 % interval of `α`; otherwise the cell falls back to `T = 800`, and if it fails there too it is not registered as a confirmatory cell and the failure is reported |
| 3 | Equal baseline exceedance is not the same dynamical event at different `N` | Stated as a limit of the design; the Stage 1 endpoint `M ≥ 100, T = 800` is kept as a separate, parallel comparison |
| 4 | `P(Y) = p0 + P(R)(p1 − p0)` holds for the conditional risks of *native* draws; the risks of the paired token intervention cannot be put into it | The decomposition is estimated from the native (BASE) arm only, by presence of a resonant native token; the intervention contrasts are reported separately and not substituted into it |
| 5 | Five primary contrasts (two orders at `N = 240` and `480`, one at `N = 242`): family, thresholds, power and the failure / inconclusive readings must be fixed in advance | A single confirmatory family with its multiplicity rule, the power at the registered size for the smallest effect of interest, and the three readings per contrast as in Stage 1, all in the registration |
| 6 | A run that reaches the cap before tick 800 has no `M_at[800]` | Not excluded. For the parallel endpoint a run is positive if it reached the cap at or before tick 800 or has `M_at[800] ≥ 100`; the number of runs decided by the cap is reported |
| 7 | The horizon of `N = 242` (1,460, not 1,470) | Documented above as a fixed exception of this pilot |
| 8 | `N^{-0.869}` is the owner's fit for the v18 path orientation at `T = 5000`, bulk-conditioned; it is not a validated time-scaling law for profile P1 | The exponent is used for one purpose only, to choose a second horizon to calibrate; the registration says so and claims no scaling law |
| 9 | The raw files contain the outcomes of draws with a resonant token | They are not examined by either co-owner before the confirmatory design is fixed and registered. This lane's intake of the upload is limited to the hash check, the stored summary and its rerun, which print outcomes for non-resonant draws only |
