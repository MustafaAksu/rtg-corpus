# Provenance sidecar and checkpoint/restart — synthetic stage (for review)

**[SESSION] NONCANONICAL.** Implementation of design §6.1–6.2 (`records/az/AZ_TOKEN_RESONANCE_MECHANISM_DESIGN.md`, r2) by the Claude AZ lane, 17 November 2026. **PI, 17 Nov 2026, 22:50 +03:00, verbatim:** "aracı sen yaz ChatGPT denetlesin" ("you write the tool, ChatGPT reviews it"). The scope of the first delivery is the one proposed in review `5936050012`: synthetic cases only. Covered: provenance and sign tracking, identity separation when −x = x, no second call of the orientation routine, and exact checkpoint/restart equality. **No registered record is read, no campaign is run, no fork operator, landmark, population or cell is chosen.**

| File | Role |
|---|---|
| `az_tokres_provenance.py` | library: pinned loading of separate engine instances, provenance sidecar, the held runner loop with `checkpoint`, `--selftest` |
| `provenance_selftest_output.txt` | `SELFTEST PASS`, 4,825 checks |
| `provenance_negcontrols.py`, `provenance_negcontrols_output.txt` | ten injected faults, each must make the self-test fail; `NEGCONTROLS PASS` |

Pins checked before anything is loaded: engine `4c94d874…a608`, orientation `ca59e9b9…d59c` (profile P1), frozen runner `az_tokres_run.py` `75c5f139…8992`. The engine and runner files are not modified. Policy `bound_symmetric` only.

## 1. Provenance (§6.1)

- **Read-only sidecar on a separate engine instance.** The pinned engine is loaded twice under different module names. The plain instance is never touched. In the instrumented instance, four module functions are wrapped: `orient_path` (the P1 rule), `apply_single_edge_swap`, `apply_path_cycle` and `blow_up_star_with_snapshot`. Each wrapper calls the original exactly once with the same arguments and then observes. A second `orient_path` call within one path event raises an error.
- **Labels.** Every node carries `(copy id, sign)`. Every copy records:
  - its root (initial node) and root value;
  - its parent copy and birth event (tick, centre, newborn);
  - its sign history;
  - its current carrier.
- **Events.**
  - A swap exchanges the two labels.
  - A path rotation moves labels along the oriented path that the engine's own `orient_path` call returned: `v_i ← v_{i+1}`, wrapping around.
  - A balanced path tie bound under `bound_symmetric` is logged; no label moves.
- **Birth convention (declared bookkeeping, not a physical identity claim).** The newborn receives a **new** copy, which is a child of the centre's pre-event copy and keeps its sign. The centre keeps its copy, and that copy's sign flips. Both are read from the pre-tick labels, as the engine reads `delta_pre`. With x = 0 or x = N/2 the flip is invisible in the value but is recorded in the sign history.
- **No value matching.** Labels are moved only by the observed events. The value identity `delta[v] = sign · root_value (mod N)` is checked after every tick, together with three more checks:
  - the labels form a bijection onto the copies;
  - each copy's carrier field points to the node that holds it;
  - each sign agrees with its sign history.
  
  None of these checks is used to assign provenance.
- **Queries for later operators:** `lineage(copy)` and `descendants(copy)`.

## 2. Checkpoint and restart (§6.2)

- `RunState` holds every mutable quantity of the frozen `run_state` loop, plus the provenance and the loop count:
  - the `Universe`, `alphabet`, `census` and law counter;
  - `fe`, `fb`, `t100` and `M_at`;
  - the TDR-26 window accumulators and the cap flag.
  
  It holds no module reference.
- `tick()` repeats the `run_state` loop body line for line, including the cap test before and after the step.
- `checkpoint()` is `copy.deepcopy` taken at the end of a complete tick. The absolute tick (`u.steps`) and the historical clocks (`fe`, `fb`, `t100`) are never reset. The checkpoint tick is stored as `landmark_tick`, so post-landmark tick = `u.steps − landmark_tick`. No post-landmark reset fields are defined.
- Serialization to disk is not used (deep copy only), so it is not tested.

## 3. Self-test (synthetic; `python3 -I evidence/az/mechanism/az_tokres_provenance.py --selftest`, about 3 min)

- **A — explicit fixtures** (N = 24, k = 2):
  - A1: isolated nodes.
  - A2: a swap of **equal** values; the values are unchanged but the labels are exchanged.
  - A3: P3 rotations, forward (E = +3) and reversed (E = −3).
  - A4: balanced ties at E = 0 and E = N/2; bound, no rotation.
  - A5: a bound 4-cycle of equal values.
  - A6: births with x = 0, N/2 and 5, checking the new child copy, the centre's sign flip and both sign histories.
  - A7: a simultaneous birth (x = N/2) and equal-value swap in one tick, newborn id 6.
  - A8: provenance off gives the identical state.
  - A9: cap already reached at the start, giving no tick, as in `run_state`.
- **B — 240 randomized trajectories** (29,353 ticks; N ∈ {24, 60, 120}; initial node count 3–8; values biased towards 0, N/4, N/2, 3N/4; duplicated values in half the draws; T ∈ {40, 120, 220}; cap ∈ {0, 60, 150}):
  - B1: provenance and values after every tick equal an **independent oracle**. The oracle recomputes the tick on copies from the pre-tick state, using the engine's pure graph helpers and its own counter-free copy of the v2.12.14 orientation rule. It shares the graph code with the engine; the label and orientation logic is independent.
  - B2: the consistency checks hold at every tick.
  - B3: the instrumented and plain instances give the identical full state at every tick (every `Universe` field, with dictionary order, plus every runner field).
  - B4: the global random state is untouched.
  - B5: the final result equals the frozen runner's `run_state` output.
  - B6–B8: at up to three restart ticks per trajectory, on both instances:
    - B6: the checkpoint is unaffected by continuing the original run;
    - B7: the restarted trajectory equals the uninterrupted one tick by tick, and the absolute tick is kept;
    - B8: provenance after the restart equals the uninterrupted provenance.
- **C — coverage.** Each listed case occurs at least once. Counts in the output: swaps 5,123 (847 with equal values); forward rotations 1,364; reversed 1,514; ties bound 133; path events on four or more nodes 335; bound cycles 386; bound multistars 18,861; births 3,717 (x = 0: 561, x = N/2: 907, other: 2,249); ticks with two or more events 1,616.
- **D — the checks do bite:**
  - D1: a wrong permutation of distinct values is detected.
  - D2: an unflipped centre sign at x = 0 is detected through the sign history.
  - D3: provenance on the plain instance is refused.

## 4. Negative controls (`provenance_negcontrols.py`; 40 trajectories each)

NC00 is the unmodified instrument and passes. Each of NC01–NC10 injects one fault, and each is detected:

- NC01: rotation along the raw path.
- NC02: rotation in the opposite direction.
- NC03: the centre's sign is not flipped.
- NC04: newborn and centre share one copy.
- NC05: swap by value matching.
- NC06: a second `orient_path` call (the guard raises).
- NC07: shallow checkpoint.
- NC08: the checkpoint resets `fb`.
- NC09: the TDR-26 window is not collected.
- NC10: the cap test before the step is omitted (detected by A9 only; in the randomized trajectories this branch is reachable only from the start).

## 5. Limits

- The tests use small synthetic populations and short horizons: at most 220 ticks, a node cap of at most 150, and N up to 120.
- They cover P1 with `bound_symmetric` only. Other policies are not supported (`tick` passes `bound_symmetric`).
- The law-check census update cannot be told apart from its omission by outputs while the engine obeys the law. A control for that omission was tried and removed for that reason; the law counter itself is compared through `run_state` equality (B5).
- The oracle shares the engine's graph helpers. It does not test the defect graph itself; that was tested in `contact_instrument_check.py`.
- The birth convention is a choice. Alternatives would give the centre the new copy, or new copies to both branches. These would change only labels, not dynamics, but a fork operator defined on "the newborn" or "the centre's copy" depends on the convention. It must be fixed with the operator.

## 6. What this enables, and what it does not

It allows a later fork operator to clone a run at a tick boundary, with complete runner state and token provenance, and to target the original node, a current carrier, one newborn or all descendants of a copy. The design (§6.3) treats these as **different interventions**. Their choice, the landmark, the population `Q`, the horizon `H`, the endpoint and the cell are the PI's, after this instrument is reviewed. Nothing here is mechanism evidence.
