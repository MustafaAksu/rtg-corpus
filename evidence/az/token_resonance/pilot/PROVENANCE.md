# Exploratory pilot of 11 November 2026 — frozen copy and provenance

**[SESSION] EXPLORATORY. Not evidence for any registered claim, not adopted, not confirmatory.** This directory freezes the scratch work on which the BOOTSTRAP 4 advisory of the AZ co-owner (Claude) rested. It is kept apart from the fixtures (`../fixtures/`) and from any later confirmatory data. Preregistration: `records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` §3.

## What is here

| File | State | What it is |
|---|---|---|
| `alphabet_check.py`, `pilot.py`, `analyse.py`, `analyse2.py`, `analyse3.py`, `hub_micro.py`, `hub_trace.py` | original bytes | the scratch scripts as they were run in the session (copied from the session scratch directory; SHA-256 compared before and after the copy) |
| `pilot_time.jsonl` (252 runs), `pilot_N120.jsonl` (2,123 runs) | original bytes | per-run records written by `pilot.py` |
| `stdout_alphabet_check.txt`, `stdout_pilot_N120.txt` | original bytes | the captured standard output of the two background runs |
| `regenerated/*.txt` | **regenerated** on 11 Nov 2026 from the frozen data with the frozen scripts | the analysis outputs. The original analysis outputs were printed in the session and not saved as files; the regenerated numbers were compared with the session transcript by the author and agree. They are not the original output bytes. |
| `regenerated/neighbour_control_reconstructed.py` | **reconstructed** | the post hoc detuned-neighbour table was an inline command, not a file; this file repeats it from the transcript |

Not available: the standard output of the first timing run of `pilot.py` (a line `runs 252 time 40.1`, seen in the session only); the scratch output of `hub_micro.py` and `hub_trace.py` (the hub table is reproduced, under the test runner, by fixture T7).

## Bytes used

Engine `upload/tdrg-records/genesis_mode_b_mc.py`, SHA-256 `4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608`, unchanged. Orientation: `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py`, SHA-256 `ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c`, bound as `eng.orient_path = make_orient(eng)` (`alphabet_check.py` ran both this and the engine's built-in `orient_path`). Python 3.13.18, Linux container of the session. All commands were run as `python3 -I SCRIPT ENGINE ORIENT …` from the repository root.

## Chronology (UTC, 11 Nov 2026; file times are the scratch files' modification times)

1. **06:24** `alphabet_check.py` started in the background: 3,000 runs (5 policies × 2 orientation bindings × 5 cells `(N,k)` = (24,1), (24,3), (60,4), (120,8), (240,16) × 60 runs, 300 ticks, cap 400), checking at every tick that all tokens lie in ±A₀, that no token count decreases and that the count grows by the number of births. Finished 06:39: `runs=3000 runs_with_violation=0 total_births=463193 max_distinct_tokens=8`.
2. **06:27–06:28** `pilot.py … pilot_time.jsonl 120 8 800 300 40 5551`: a timing sample, master seed 5551, stopped by a 40 s wall-clock budget: 252 runs. The first 40 records (births, final M, steps, first-birth step) were printed.
3. **06:28** `pilot.py … pilot_N120.jsonl 120 8 800 300 420 20261111` started in the background: master seed 20261111, stopped by a 420 s wall-clock budget, independent of any outcome. Until it finished, only its line count was read (433, 558, 754, 1,143 lines).
4. **06:28–06:30, while it ran** — hypothesis generation on `pilot_time.jsonl` only:
   - `analyse.py`: five covariates chosen before any data were seen (two seeds equal or opposite; number of seeds with |2x|_c ≤ k; minimal first-return time τ; numbers of seed pairs with |a−b|_c ≤ 2k and with |a+b|_c ≤ 2k). None was significant (permutation p from 0.08 to 0.94). The same output showed that the eight tail runs end with one signed token class holding 98–99 % of the nodes.
   - `analyse2.py`: the dominant class of the eight tail runs is 0 (four runs) or 30 = N/4 (four runs). **The hypothesis "tails need a seed token with 4x ≡ 0 (mod N)" was formed here.**
   - `analyse3.py` was written (06:30:32) and dry-run on `pilot_time.jsonl`.
5. **06:31** `hub_micro.py`, `hub_trace.py`: an isolated hub whose four nodes share one token gives births for every token (N = 120: 60 births in 60 ticks for x ∈ {0, 60}; the scratch output listed the top classes only, 44 down to 30; the full table, reproduced under the test runner by fixture T7, runs from 3 to 44 for the other tokens) — the resonance is therefore not explained by hub maintenance alone.
6. **06:35:28** the background run ended: 2,123 runs. `analyse3.py` was then run **once** on `pilot_N120.jsonl` (output: `regenerated/analyse3_on_pilot_N120.txt`).
7. **After that result was seen (post hoc):** the detuned-neighbour table and the threshold table (`regenerated/neighbour_control_on_pilot_N120.txt`).

## What the pilot does and does not show

Settings: N = 120, k = 8, policy `bound_symmetric`, four initial nodes drawn by the engine's `init_universe`, T = 800 ticks, stop at 300 nodes, tail := final M ≥ 100.

On the independent sample (`pilot_N120.jsonl`): tails 72 of 2,123; with a seed token satisfying 4x ≡ 0: 61 of 258 (23.6 %, Wilson 95 % 18.9–29.2); without: 11 of 1,865 (0.59 %, 0.33–1.05); risk ratio 40.1; one-sided Fisher p = 1.6·10⁻⁴⁷. By value: x = 0: 22/74; x = N/2: 16/62; x = ±N/4: 32/134. Post hoc: no resonant seed but one at distance 1 from a resonant value: 1 of 462.

Limits: one cell; the tail definition is not the TDR-26 birth-anchored rule; 11 of 72 tails have no resonant seed; the number of runs was fixed by a time budget; the hypothesis was formed on 8 tail runs of the first sample; the detuned-neighbour and threshold tables are post hoc; no mechanism is established. Master seeds 5551 and 20261111 are spent and must not be reused in a confirmatory run.
