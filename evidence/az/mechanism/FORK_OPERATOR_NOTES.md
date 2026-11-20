# Matched R/D operator, intervention epoch and H continuation — synthetic stage (for review)

**[SESSION] NONCANONICAL.** r2 (20 Nov 2026) closes R1–R3 of review `5983692458`. This is the second Gate I deliverable of the §6.3 fork design (`records/az/AZ_TOKEN_RESONANCE_FORK_DESIGN.md` r2, PR #322, head `08ef706`, Gate D PASS `5960841961`).

- **Authority.** PI, 19 Nov 2026, 23:28 +03:00, verbatim: "sıradaki adım önerin uygun . uygulayalım." The proposal it accepts: the R/D operator (absolute write, O1 only), the intervention epoch in the ledger, the H-tick continuation, and the post-fork alphabet and census, with synthetic tests only.
- **Parameters** are those recorded in PR #322 comment `7008416095` (PI decision, source-reported there).
- **Built on** the merged §6 instrument (#313) and the contact clock (PR #328, r2 `c73dc6a`). Written by the Claude AZ lane; reviewed by ChatGPT.
- **Not in scope:** no registered record is read, no campaign is run, and the BASE pilot for the final L is not included.

| File | Role |
|---|---|
| `az_tokres_fork.py` | `ForkProvenance` (intervention epochs), `o1_values`, `fork`, `continue_fork`, `endpoint`; `--selftest` |
| `fork_selftest_output.txt` | `SELFTEST PASS`, 13,448 checks (r1: 12,174) |
| `fork_negcontrols.py`, `fork_negcontrols_output.txt` | seventeen injected faults (r1: twelve), each run with the fail-closed guard on and off; all detected in both modes; `NEGCONTROLS PASS` |

Pins are checked first:

- engine `4c94d874`, orientation `ca59e9b9` and runner `75c5f139`;
- provenance library `5d5ca8ac`;
- contact clock `4cdd9a7d` (PR #328 r2).

Profile: P1, `bound_symmetric`.

## 1. As implemented (design §3–§5)

- **Boundary.** The C⁻ or C⁺ state from `contact_clock`. It must be eligible (`done = False`, `iters < T_ref`, `M < cap`); otherwise the fork is refused.
- **Arms.** Each arm (R, D, and the BASE reference) is a separate deep copy of the **same** boundary. The boundary itself is never modified.
- **Target.** `v_s = carrier_s(c_j)`, the current carrier of the original slot copy. At C⁻ this is node j (proved in PR #328, B4). At C⁺ after a slot-copy birth it is the **centre**, by the §6.1 convention, whose token is −x.
- **Operator.** An absolute write `δ[v_s] ← x_a`, O1 only:
  - `x_R = r1`, `x_D = (r1 + s1) mod N`, with `r1 ∈ {0, N/2}` and `s1 = ±1`;
  - the draw law is the one of `az_tokres_run.arm_choices`, under the synthetic tag `AZ-FORK-OPERATOR-SYNTH`, which is refused if it collides with the registered prefix `AZ-TOKRES`.
  
  No tick, advance, birth, swap or counter change is injected. A write that leaves the value unchanged (`old = x`) is logged as `noop` and not excluded.
- **Intervention epoch** (in the ledger):
  - The replaced copy is **retired**. It is kept with its birth ancestry, and its descendants are untouched; the newborn of an earlier slot-copy birth keeps its value and its parent link to the retired copy.
  - A **new value-origin copy** is created at the same carrier: no parent, its root is itself, root value x, sign +1. It carries an explicit `intervention` record {tick, carrier, replaces, old_value, new_value, arm}, and an `intervention` event is added to the log.
  - Later births from that carrier descend from the new copy under the unchanged birth convention.
  - `ForkProvenance.check_ledger` checks:
    - initial roots, birth children and intervention origins, each against its own events;
    - every retired copy against a matching intervention;
    - that no birth comes from a copy after its retirement;
    - full sign histories;
    - that the active copies are exactly the labels and the carrier map.
- **Accounting.** On R and D, the census is reset to `Counter(δ after)` and the common alphabet becomes `S_* = S_BASE ∪ {±r, ±d}`. The BASE reference arm keeps `S_BASE`. The configuration boundary `T_fork = iters + H` is set on all arms. `u.steps`, `iters`, `fe`, `fb`, `t100`, `M_at`, the TDR-26 window, the law-violation count and every `Universe` history are kept.
- **Endpoint** (r2, R1: fail closed). `endpoint(st, q)` is refused unless all of the following hold:
  - q is a positive integer;
  - the run is a finished fork;
  - `0 ≤ h_stop ≤ H`, and the configuration boundary is consistent;
  - the stop is either the horizon (`h_stop = H` and `iters = T`) or a cap stop with `M ≥ cap`;
  - no positive cap is below q, since a cap-stopped run would then be censored.
  
  It returns `Y = 1{M at stop ≥ q}` (M is non-decreasing, and this is checked), `G = M_stop − M_s`, `h_stop`, `hit_cap` and the stop reason.
- **Validation** (r2, R2: fail closed). `o1_values` and `fork` accept only the PI-selected scope. Everything else raises `ValueError`. The accepted scope:
  - N even;
  - `r1 ∈ {0, N/2}` and `s1 ∈ {−1, +1}`, both integers and not bool;
  - a value pair `{R, D}` with `R ∈ {0, N/2}` and `D = R ± 1 (mod N)`, and no other keys;
  - `H` a positive integer;
  - landmark `C-` or `C+`, with `tau_C` a positive integer;
  - a BASE boundary that carries provenance (not an already forked state, no intervention event), whose `landmark_tick` equals both `u.steps` and the C⁻/C⁺ fork tick (`τ_C − 1` or `τ_C`);
  - j an active initial root copy;
  - an eligible state.
  
  This validation is not a PI selection of any further parameter.
  - Maintenance (20 Nov, review `5989076562`, non-blocking): `o1_values` also refuses a draw that is not a mapping (E5).

## 2. Self-test (`python3 -I evidence/az/mechanism/az_tokres_fork.py --selftest`, about 2.5 min)

- **A — explicit fixtures** (N = 24, k = 2):
  - A1: at s = 0 (contact at tick 1, C⁻), the absolute write equals `arm_state('O1R')` per seed.
  - A2: the continuation over H = 30 equals `run_state` on those initial values.
  - A3: C⁺ after a slot-centred birth: the target is the centre (token −x), the newborn keeps x and its parent link to the retired copy, new origin copy 5, and the ledger check passes.
  - A4: no-op arm.
  - A5: cap reached at h = 1 < H with cap ≥ q, so Y = 1.
  - A6 (r2): a slot-centred birth at contact that reaches cap 5 makes the C⁺ fork refused and the C⁻ fork accepted.
  - A7 (r2): C⁺ after a slot-centred birth with a no-op write (−x = x_R = N/2): the continuation and endpoint equal the BASE reference arm.
- **E — fail-closed contracts** (r2):
  - E1, E2: the endpoint of an unadvanced and of a partial continuation is refused.
  - E3: a completed run gives stop = horizon; a q that is not a positive integer is refused.
  - E4: a cap stop is refused when 0 < cap < q and accepted with stop = cap when cap ≥ q.
  - E5, E6: off-family r, an invalid ε, non-integers, missing or extra keys and an odd N are refused.
  - E7: other landmarks are refused.
  - E8: a wrong or missing `landmark_tick` annotation, the wrong landmark for the boundary and a wrong `tau_C` are refused.
  - E9: an invalid H is refused.
  - E10: a non-root slot, an unknown arm and an already forked state are refused.
- **B — 300 synthetic seeds, 594 forked boundaries.** 100 seeds are native in N = 120, k = 8, L = 400, cap ∈ {0, 300}, q = 100, H ∈ {40, 120}; ten of them use **H = 800**. The rest are small states (N ∈ {24, 60}, small caps, H ∈ {20, 60}). For each eligible C⁻ and C⁺ boundary, and for each arm:
  - B0: an oracle ledger replayed from tick 0 reproduces the boundary.
  - B1: only the target token changes; histories, clocks, `u.steps` and `iters` are kept; `T − iters = H`.
  - B2: the written value is x; the target is the carrier of `c_j`; the ledger check passes; the census is reset; the alphabet is `S_*`.
  - B3: the boundary is unchanged by forking.
  - B4: the intervention epoch equals the extended **independent oracle ledger**.
  - B5: every continuation tick equals the oracle (values, labels, carriers, copy table, sign histories), and the ledger check holds.
  - B6: M is non-decreasing; no new law violation under `S_*`; the run stops at H or at the cap; cap ≥ q implies Y = 1.
  - B7: a restart inside the continuation equals the uninterrupted run.
  - B8: rerunning R after D and BASE gives the identical result.
  - B9: the BASE reference arm equals BASE `run_state` to tick `s + H`.
  - B10: at s = 0, each of R and D equals `run_state(arm_state(O1R/O1D))` over H.
  - **Metamorphic relations** (r2, R3), on every forked boundary:
    - M1: `I_R = I_D` (both arms write `x_R`) gives identical physical and runner continuations and endpoints.
    - M2: a physical no-op write reproduces the BASE continuation and endpoint (73 cases: 36 at C⁻, 37 at C⁺).
    - M3: swapping the R/D assignments only swaps the paired outcomes.
- **C — coverage** (counts in the output):
  - forks at C⁻ and C⁺: 297 each; s = 0 identity cases: 137;
  - no-op arms: 73; target ≠ j: 494 (C⁺ after the carrier moved); slot birth before C⁺: 8;
  - births from an intervention origin: 401; retired copies with descendants: 16;
  - the write removes the BASE contact at τ_C (C⁻): 276 **arm-level** cases out of 594 C⁻ arm forks (two arms × 297 boundaries). These are not independent seeds and not mechanism evidence;
  - cap hits: 18; Y differs between R and D: 40.
- **D1.** Only the pinned files, the clock, the provenance library and this script are opened inside the repository; nothing under `upload/az-token-resonance-*`. The audit hook is installed by the clock module before any project import.

## 3. Negative controls (40 seeds each, guard on and off)

NC00 passes in both modes. Each of NC01–NC12 is detected in **both** modes:

- NC01: sign-covariant write.
- NC02: write without an epoch.
- NC03: recycled old copy.
- NC04: `T_fork` not set.
- NC05: `fb` reset.
- NC06: an arm shares the boundary's `Universe`.
- NC07: alphabet not expanded.
- NC08: census not reset.
- NC09: target fixed to node j.
- NC10: a virtual tick injected.
- NC11: the retired copy left in the carrier map.
- NC12: the new segment linked as a birth child.
- r2:
  - NC13: endpoint without its completion, stop-reason and cap ≥ q checks.
  - NC14: value and boundary validation removed.
  - NC15: a hidden D-arm side effect on runner state (M1, M3).
  - NC16: a no-op write that alters runner state (M2). A first version cleared `M_at` and was missed, because the runner's grid starts at tick 100, after these synthetic boundaries. It now clears `fe`.
  - NC17: D writes −x (M3).

With the guard on, the faults that break the ledger are caught by the fail-closed `ProvenanceError` and counted as `A*` and `B*` failures. With the guard off, they are caught by the oracle and ledger comparisons (B2, B4, B5) and the fixtures.

## 4. Limits

- Only the synthetic stage is covered: P1 with `bound_symmetric`, the O1 family, absolute write, centre convention, and boundaries C⁻ and C⁺ only. Landmark B and O2 are not implemented.
- H = 800 is exercised on ten native seeds. Most randomized continuations are shorter.
- The oracle ledger states the same declared conventions (birth and intervention epoch) in an independent representation. It tests the implementation, not the choice of convention.
- Not included: the BASE-only pilot for the final L, power and sample size, the analysis code and the preregistration. Each needs its own PI decision.
