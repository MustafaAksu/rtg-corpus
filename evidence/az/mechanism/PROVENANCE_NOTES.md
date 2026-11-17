# Provenance sidecar and checkpoint/restart — synthetic stage (for review)

**[SESSION] NONCANONICAL.** Implementation of design §6.1–6.2 (`records/az/AZ_TOKEN_RESONANCE_MECHANISM_DESIGN.md`, r2) by the Claude AZ lane, 17 November 2026; **r2 (18 November 2026)** closes R1 and R2 of review `5945968886` and its non-blocking points. **PI, 17 Nov 2026, 22:50 +03:00, verbatim:** "aracı sen yaz ChatGPT denetlesin" ("you write the tool, ChatGPT reviews it"). The scope of the first delivery is the one proposed in review `5936050012`: synthetic cases only. Covered: provenance and sign tracking, identity separation when −x = x, no second call of the orientation routine, and exact checkpoint/restart equality. **No registered record is read, no campaign is run, no fork operator, landmark, population or cell is chosen.**

| File | Role |
|---|---|
| `az_tokres_provenance.py` | library: pinned loading of separate engine instances, provenance sidecar, the held runner loop with `checkpoint`, `--selftest` |
| `provenance_selftest_output.txt` | `SELFTEST PASS`, 5,556 checks (r1: 4,825) |
| `provenance_negcontrols.py`, `provenance_negcontrols_output.txt` | sixteen injected faults, each run with the runtime guard on and off; each must make the self-test fail; `NEGCONTROLS PASS` |

Pins checked before anything is loaded: engine `4c94d874…a608`, orientation `ca59e9b9…d59c` (profile P1), frozen runner `az_tokres_run.py` `75c5f139…8992`. The engine and runner files are not modified. Policy `bound_symmetric` only. **Single-threaded use only:** the observer is attached to the engine instance through a module-level holder, which is set for the duration of one tick and cleared in a `finally` block.

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
  
  and the **ledger check** (r2, R1): every lineage record is checked against the event log. Root copies are exactly the initial nodes, with no parent or birth record. Each non-root copy has exactly one birth event whose parent, tick, centre and newborn equal its record. It has the same root and root value as its parent, and parent id < child id. Each sign history equals what the birth events imply: the copy's first entry, then one alternating flip at every birth in which it was the centre's copy, in order. The number of birth events equals the number of non-root copies.

  None of these checks is used to assign provenance.
- **Runtime guard (r2):** with `strict=True` (the default) every tick ends with the full check, and any error raises `ProvenanceError`, so a run fails closed. The self-test's randomized part runs with `strict=False`, so that failures are counted rather than raised; the guard itself is tested by D7.
- **Queries for later operators:** `lineage(copy)` and `descendants(copy)`.

## 2. Checkpoint and restart (§6.2)

- `RunState` holds every mutable quantity of the frozen `run_state` loop, plus the provenance and the loop count:
  - the `Universe`, `alphabet`, `census` and law counter;
  - `fe`, `fb`, `t100` and `M_at`;
  - the TDR-26 window accumulators and the cap flag.
  
  It holds no module reference.
- `tick()` repeats the `run_state` loop body line for line, including the cap test before and after the step.
- **Full snapshot (r2, R2):** `fingerprint()` is a canonical, order-preserving image of the **whole** `RunState`. It includes every `Universe` field, every runner field including the configuration (`N`, `k`, `T`, `cap`, `tdr26`, `check_law`, `window`, `checkpoints`, `strict`) and the whole provenance object: copies with parent, root and birth records, labels, carriers, full sign histories, the event log and the per-tick scratch fields. Only `landmark_tick` is excluded: it is an annotation set on a checkpoint copy and never continued from, and it is compared separately.
- `checkpoint()` is `copy.deepcopy` taken at the end of a complete tick. The absolute tick (`u.steps`) and the historical clocks (`fe`, `fb`, `t100`) are never reset. The checkpoint tick is stored as `landmark_tick`, so post-landmark tick = `u.steps − landmark_tick`. No post-landmark reset fields are defined.
- Serialization to disk is not used (deep copy only), so it is not tested.

## 3. Self-test (synthetic; `python3 -I evidence/az/mechanism/az_tokres_provenance.py --selftest`, about 6 min)

- **A — explicit fixtures** (N = 24, k = 2; with the runtime guard on):
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
  - B1 (r2): after every tick, the values, labels, carriers, the **whole copy table** (root, root value, parent, birth record) and the **full sign histories** equal an independent **oracle ledger**. The ledger is kept in its own representation (separate field maps). It is advanced only from the engine's pre-tick physical state, using the engine's pure graph helpers and its own counter-free copy of the v2.12.14 orientation rule, and it never reads the sidecar after initialisation.
  - B2: the consistency and ledger checks hold at every tick.
  - B3: the instrumented and plain instances give the identical full snapshot (provenance excluded) at every tick.
  - B4: the global random state is untouched.
  - B5: the final result equals the frozen runner's `run_state` output.
  - B6–B8: at up to three restart ticks per trajectory, on both instances, with **full snapshots**:
    - B6: the checkpoint equals the live state at the boundary, `landmark_tick` apart (set to the checkpoint tick on the copy, absent on the live run), and it is unaffected by continuing the original run;
    - B7: the restarted trajectory equals the uninterrupted one in full snapshot at every tick, and the absolute tick is kept;
    - B8: the final full snapshot equals that of the uninterrupted run from the start.
- **C — coverage.** Each listed case occurs at least once. Counts in the output: swaps 5,123 (847 with equal values); forward rotations 1,364; reversed 1,514; ties bound 133; path events on four or more nodes 335; bound cycles 386; bound multistars 18,861; births 3,717 (x = 0: 561, x = N/2: 907, other: 2,249); ticks with two or more events 1,616. Lineage cases (r2):
  - births from an already descended copy: 1,553;
  - births where the centre carries a copy other than its own initial one: 2,138;
  - births where the centre's value is shared with another node: 2,982;
  - births giving a lineage of depth ≥ 4: 452.
- **D — the checks do bite:**
  - D1: a wrong permutation of distinct values is detected.
  - D2: an unflipped centre sign at x = 0 is detected.
  - D2b: the centre's early sign-history entries are dropped, with the last kept; detected.
  - D3: provenance on the plain instance is refused.
  
  r2 adds D4a–D9, on a synthetic trajectory with several generations of births (the test copy has depth 5):
  - D4: the parent is redirected to another copy with the **same root and value**, with labels and engine untouched; detected, and `descendants()` of the true parent changes.
  - D5: a birth record with a wrong tick is detected.
  - D6: early sign-history entries are dropped, with the last kept; detected.
  - D7: the strict runtime guard raises at the next tick on a corrupted ledger.
  - D8: a changed continuation field (the checkpoint grid) leaves the outputs unchanged, but the full snapshot differs.
  - D9: `landmark_tick` alone does not change the snapshot.

## 4. Negative controls (`provenance_negcontrols.py`; 40 trajectories each, runtime guard on and off)

NC00 is the unmodified instrument and passes in both modes. Each of NC01–NC16 injects one fault and must be detected **in both modes**. With the guard off, detection has to come from the self-test's own comparisons (oracle ledger, full snapshots, ledger check); the D7 guard line is then not counted. Controls:

- NC01: rotation along the raw path.
- NC02: rotation in the opposite direction.
- NC03: the centre's sign is not flipped.
- NC04: newborn and centre share one copy.
- NC05: swap by value matching.
- NC06: a second `orient_path` call.
- NC07: shallow checkpoint.
- NC08: the checkpoint resets `fb`.
- NC09: the TDR-26 window is not collected.
- NC10: the cap test before the step is omitted (reachable only from the start, so detected by A9).
- r2:
  - NC11: the child is linked to the **grandparent** copy, with the event log made consistent, so that only the independent ledger can see it.
  - NC12: the birth record stores the previous tick.
  - NC13: the sign history keeps only the latest entry at a flip.
  - NC14: the checkpoint truncates the sign histories.
  - NC15: the checkpoint changes a configuration field, with outputs unchanged.
  - NC16: the checkpoint drops the event log.

The detection counts are in the output file.

## 5. Limits

- The tests use small synthetic populations and short horizons: at most 220 ticks, a node cap of at most 150, and N up to 120.
- They cover P1 with `bound_symmetric` only. Other policies are not supported (`tick` passes `bound_symmetric`).
- Omitting the law-check census update in the held loop cannot be told apart by the `run_state` outputs while the engine obeys the law. A control for it was tried in r1 and removed. The census is part of the full snapshot, but such an omission would affect the uninterrupted and the restarted run alike.
- The oracle ledger states the same declared birth convention in an independent representation. It checks the implementation of the convention, not the choice of convention. It shares the engine's graph helpers. It does not test the defect graph itself; that was tested in `contact_instrument_check.py`.
- The birth convention is a choice. Alternatives would give the centre the new copy, or new copies to both branches. These would change only labels, not dynamics, but a fork operator defined on "the newborn" or "the centre's copy" depends on the convention. It must be fixed with the operator.

## 6. What this enables, and what it does not

It allows a later fork operator to clone a run at a tick boundary, with complete runner state and token provenance, and to target the original node, a current carrier, one newborn or all descendants of a copy. The design (§6.3) treats these as **different interventions**. Their choice, the landmark, the population `Q`, the horizon `H`, the endpoint and the cell are the PI's, after this instrument is reviewed. Nothing here is mechanism evidence.

**What is tested and what is guaranteed at run time.** Tested (synthetic, as above): agreement with the oracle ledger, full-snapshot restart equality, on/off identity and equality with `run_state`. At run time, the strict guard enforces only the internal checks (value identity, bijection, carriers, ledger against the event log). It cannot catch a fault that is consistent with itself but wrong, such as NC11. That class is covered only by the oracle ledger in the self-test.
