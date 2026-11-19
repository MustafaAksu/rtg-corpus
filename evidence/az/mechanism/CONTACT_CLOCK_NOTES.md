# BASE contact clock τ_C and C⁻/C⁺ boundary states — synthetic stage (for review)

**[SESSION] NONCANONICAL.** r2 (19 Nov 2026) closes the two non-blocking points F1 and F2 of review `5980963543`. This is the first Gate I deliverable of the §6.3 fork design (`records/az/AZ_TOKEN_RESONANCE_FORK_DESIGN.md` r2, PR #322, head `08ef706`, Gate D PASS `5960841961`). Its scope is the one set in PR #322 comment `7008416095`, which records the PI decision of 19 November 2026 (source-reported there). The PI's own words in this session, 18 Nov 2026, 20:35 +03:00: "Uygulama şamasını başlatalım" ("let us start the implementation stage"). Written by the Claude AZ lane; independent review by ChatGPT.

**Synthetic only.** No registered record is read. No fork operator, intervention epoch, R/D arm or BASE pilot is implemented or run.

| File | Role |
|---|---|
| `az_tokres_contact_clock.py` | `predicted_graph`, `contact_clock`, `eligible`, `tau_free` (counterfactual, never a substitute); `--selftest` |
| `contact_clock_selftest_output.txt` | `SELFTEST PASS`, 2,374 checks |
| `contact_clock_negcontrols.py`, `contact_clock_negcontrols_output.txt` | nine injected faults, each must make the self-test fail; `NEGCONTROLS PASS` |

Pins are checked before anything is loaded:

- engine `4c94d874…a608`;
- orientation `ca59e9b9…d59c`;
- runner `75c5f139…8992`;
- provenance library `az_tokres_provenance.py` `5d5ca8ac…3f68`, as merged at `8de175c`.

All four files are unchanged. Profile: P1, `bound_symmetric`.

## 1. Definitions as implemented (design §2.2–2.4)

- **Slot copy.** `c_j = j`, the root copy of slot node j in the §6.1 sidecar.
- **The clock.** From the complete end-of-tick BASE state `S_{t−1}`:
  - `θ_pre(t) = (θ + δ) mod N` for every node;
  - `E_t = graph_edges_for(nodes, θ_pre(t), N, k)`, the pinned pure function, called on the **plain** engine instance;
  - `v = carrier_{t−1}(c_j)`, taken from the sidecar.
  
  `τ_C` is the first t ≥ 1 with an edge of `E_t` incident to `v`. Bound, tied and event-free contacts count.
- **Read-only.** The prediction works on copies of the phases. It never steps the engine, never calls `orient_path` and needs no engine hook.
- **Boundary states.** `C⁻ = S_{τ_C − 1}`, taken before any BASE tick past it. `C⁺ = S_{τ_C}`, taken after the BASE contact tick. Both are deep checkpoints, and absolute ticks are kept.
- **Eligibility of a boundary state:** `done = False`, `iters < T_ref` and, with a positive cap, `M < cap`. The reference runner uses `T_ref = L + 1`.
- **Status per seed:** `contact`, `no_contact_by_L` or `terminated_before_contact`. No time is substituted for a missing contact. The clock fails closed: if a BASE tick makes no progress, the status is `terminated_before_contact`. This guard was added after the first run of NC05, in which faulty eligibility made the search loop forever.
- **Also recorded:**
  - the incident edge set at `τ_C`;
  - the pre-tick carrier;
  - the C⁺ carrier, using the §6.1 convention, so the centre after a slot-copy birth;
  - whether the slot copy is a birth centre at the contact tick;
  - flags for an already-reached threshold (`M ≥ q`) at each boundary;
  - two checks at C⁻: the carrier is node j, and its token is the original one.

## 2. Self-test (`python3 -I evidence/az/mechanism/az_tokres_contact_clock.py --selftest`, about 4.5 min)

- **A — explicit fixtures** (N = 24, k = 2). Each asserts the contact time, the complete incident edge set and the carrier:
  - A1: tick-1 contact through a swap: C⁻ = S₀, and the carrier moves at C⁺.
  - A2: delayed contact at tick 16, equal to `τ_free`.
  - A3: contact inside a bound 4-cycle with no event; it is counted, and both slot edges are listed.
  - A4: the slot is the centre of a birth at its contact, with cap 5. The C⁺ carrier is the centre; C⁺ is ineligible (the cap is reached on the contact tick) while C⁻ is eligible.
  - A5: never in contact, so the status is `no_contact_by_L`.
  - A6: equal, sign-invisible tokens (x = N/2); the carrier is still tracked.
  - A7: two components in the contact tick; only the slot's edges are counted.
  - A8: the cap is reached by another component first, so the status is `terminated_before_contact`.
- **B — 400 synthetic trajectories** (51,461 observed ticks). 100 are native draws in the chosen cell, N = 120, k = 8, L = 400, cap ∈ {0, 100, 300}, from seeds derived from the tag `AZ-FORK-CLOCK-SYNTH`, never a registered tag. The other 300 are small random states with N ∈ {24, 60, 120}, small caps and L ∈ {3, 20, 60, 150}. The independent reference is the pinned engine's **own** graph: a separate instance with a read-only wrapper on `graph_edges_for`, used only in the test, which calls the original once per call and records it. Checks:
  - B1: at every tick there is exactly one graph call, and pure prediction = engine graph (nodes, phases, edges) = `graph_edges_bruteforce`.
  - B2: `τ_C`, its incident edges and the pre-tick carrier equal the engine-observed ones.
  - B3: the C⁻ and C⁺ states equal the independent run at ticks `τ_C − 1` and `τ_C`, in full snapshot including provenance; their `landmark_tick` annotations are `τ_C − 1` and `τ_C` (r2, F2; also in A1).
  - B4: before `τ_C` the slot copy took part in no event, so at C⁻ its carrier is j and its token is the original one. This is the design's claim, checked on every contact trajectory.
  - B5: the C⁺ carrier and C⁺ eligibility agree with the independent run.
  - B6: the clock run (continued to the end) = the observed run, in full state including provenance and orientation counters. Both equal a plain run in physical trajectory at every tick. The global random state is untouched.
- **C — coverage** (counts in the output):
  - contact 381, `no_contact_by_L` 15, `terminated_before_contact` 4; τ_C = 1: 196;
  - non-slot events before τ_C: 113 (births among them: 9);
  - **`τ_free ≠ τ_C`: 66** (free-flight earlier 40, later or never 26);
  - contact without a slot event: 66; carrier moved at contact: 306; slot-copy birth at contact: 9;
  - C⁺ ineligible: 6; other components in the contact tick: 226;
  - equal tokens: 87; sign-invisible slot token: 96; already at threshold at C⁻: 65 (q ∈ {5, 8, 100} in the small states).
- **D1.** An audit hook, installed at the top of the module before any project module is imported (r2, F1 of review `5980963543`); it covers the helper import, the pinned files and the tests, shows that the only repository files opened are the four pinned files and this script, or their attempted bytecode-cache entries. Nothing under `upload/az-token-resonance-*` is opened.

## 3. Negative controls (`contact_clock_negcontrols.py`; 60 trajectories each, fixtures included; the coverage assertions, which need the full 400, are skipped)

NC00 is the unmodified clock and passes. Each of NC01–NC09 injects one fault, and each must be detected:

- NC01: graph one tick late (tick shift).
- NC02: post-interaction graph (no advance).
- NC03: stale pre-tick carrier used as the C⁺ target.
- NC04: `τ_slot^free` substituted for τ_C.
- NC05: eligibility ignores the cap.
- NC06: C⁻ taken after the contact tick.
- NC07: the prediction mutates the live phases.
- NC08 (r2): wrong `landmark_tick` annotation on the boundary checkpoint.
- NC09: an attempt to open a path under the registered uploads. It stays last, because the audit list is process-wide.

The checks that fail for each control are listed in the output.

## 4. Limits

- Only the synthetic stage is covered: P1 with `bound_symmetric`, the four-node native initialisation in the chosen cell, and small random states otherwise.
- The clock is defined for an original root copy (`c_j = j`).
- The engine-graph reference shares the engine's own `graph_edges_for`. The brute-force graph is an independent check of that function.
- `τ_free` is implemented only to show that it differs from `τ_C`. It is never used as a clock.
- Not implemented, and each needing its own PI decision and review: the R/D operator, the intervention epoch in the ledger, the `T_fork = iters + H` continuation, the post-fork alphabet and census, and the BASE-only pilot for the final L.
