# AZ token resonance — §6.3 common-prefix fork design (review draft)

**[SESSION] NONCANONICAL · DESIGN ONLY · NOT PREREGISTERED · NO EXECUTION AUTHORISED.** Prepared by ChatGPT for the Claude AZ co-owner's independent review, 18 November 2026. The PI delegated drafting of §6.3; **no operator, landmark, target population, horizon, endpoint, cell, test or run has been scientifically selected or adopted** by that delegation. This record makes the alternatives operationally explicit so that the PI can choose them before any experiment. No DSN or source evidence is changed.

## 0. Authority, source scope and inference boundary

- **Governing AZ science:** `az-v0.10`, `dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` §§4.2.1–4.2.2, 8, release record `records/az/AZ_v0_10_RELEASE_RECORD.md` (targeted source reading). AZ remains Level A; S1/S2 are AZ-owned `NUM diagnostic` results, not growth-mechanism proofs. Its §8 TDR-G consumer pin remains `tdrg-v2.12.15`, even though TDR-G `tdrg-v2.13` is subsequently adopted.
- **Governing TDR-G source for rules and limits:** `tdrg-v2.13`, `dsn/RTG_DISCRETE_GENESIS_DSN.md` §§6.3, 6.13, especially `TDRG-ALG-EVENT-INVENTORY`, `TDRG-ALG-TOKEN-CENSUS-LAW`, `TDRG-ALG-PARENT-CHILD-PHASE`; targeted statements, not a full-owner rereview. Referencing the newer owner edition here does **not** repin AZ.
- **Existing AZ design:** `records/az/AZ_TOKEN_RESONANCE_MECHANISM_DESIGN.md` §§4.1–4.2, 5, 6.1–6.3 (merged PR #281); exploratory S1-C1 readout `records/az/AZ_TOKEN_RESONANCE_MECHANISM_S1C1_TABLES.md` §§1–4 (merged PR #290), known outcomes, no causal timing identification.
- **Instrument at review scope:** `evidence/az/mechanism/az_tokres_provenance.py` / `PROVENANCE_NOTES.md` (PR #313, reviewed `5951975805`, merge `8de175c`). Source inspected: `Provenance`, `RunState`, `tick`, `checkpoint`, `fingerprint`, `OracleLedger`. Its synthetic validation does **not** establish an intervention operator or a prospective experimental pipeline.
- **Pinned computational profile for a candidate prototype, not a selected campaign:** engine `upload/tdrg-records/genesis_mode_b_mc.py` SHA-256 `4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608`, orientation `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` `ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c`, runner `evidence/az/scripts/az_tokres_run.py` `75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992`; P1, `bound_symmetric`, `CONV-TICK`. Original S1/S2 archive/profile pins remain untouched.

**Question:** Does an intervention made *after the same unmodified BASE prefix* change the remaining trajectory? A positive answer would show a **post-landmark intervention effect in a specified reference-prefix population**. It would not identify the fraction of the original tick-zero S1/S2 effect mediated by births, or establish that early contact was irrelevant. The original S1 mechanism data informed these candidate hypotheses: any later inferential study needs new prespecified seeds, outcomes and analysis, not retrospective confirmation from S1.

## 1. Common BASE prefix and reference state

For each prospective unit, draw an independent seed bundle `z` from a *to-be-registered* law `P_ref`. At enrollment, before running the engine, fix four BASE phases and tokens, one initial slot-node index `j=j(z)`, and the paired intervention values/offsets in §4. Do not select `j` or parameter values by observing prefix growth. The reference prefix uses **only BASE tokens**, never R or D, with the same engine, orientation, policy and observation rules for all future forks.

Let `S_t^0` denote the full `RunState` (Universe, observer-local clocks/windows/census and provenance) at the **end of complete tick** `t`, after the snapshot's entire event set and all bookkeeping. The initial copy carried by slot node `j` is `c_j=j` for the four-node initialisation. This copy identity persists through swaps, rotations and births, though its carrier need not remain node `j`. With the birth convention of §3, `carrier_t(c_j)` is unique in the unmodified prefix.

For a candidate landmark `ell`, define `tau_ell(z)` on the **BASE prefix only** (§2). If it is observed by a fixed prefix observation limit `L`, and the complete end-of-tick prefix is still **nonterminal** (the node cap has not ended the run on that same tick), valid and eligible, set `S=S^0_{tau_ell}`. Snapshot and clone it *once per arm* before injecting any arm-specific change. The two pre-intervention fingerprints and all historical clocks must be exactly equal. No reforking from an R or D prefix, and no population selection from potential R/D post-fork outcomes.

Both candidate landmarks may be undefined on some seeds. A seed with no landmark by `L`, a terminating prefix or invalid reference state receives a **registered eligibility/stop category**, not a fabricated time or a substituted time from the other arm. Denominators and every exclusion criterion are declared before any new results.

## 2. Dynamic landmark definitions — two alternatives, not one selected rule

### 2.1 Candidate B: first complete birth tick

`tau_B = min{t >= 1 : births(S_t^0) > births(S_{t-1}^0)}`, with `min(empty)=undefined`. Detect from actual BASE engine birth increments, not an analytic first-contact predictor. Clone the full state at the **end of that tick**, after all simultaneously processed events and births. If several births occur that tick, no one is silently selected by event order for the proposed **slot-copy carrier** target (§3). An optional *first newborn* target is a **different** operator/target-population choice and would require a preregistered tie rule and its node-label covariance audit.

The fact that eligibility here depends on an observed BASE birth is explicit. It is a pre-assignment selection for the later R/D fork, but is *not* the unconditional population of the original tick-zero S1 study.

### 2.2 Candidate C: actual contact of the tagged initial slot copy

At the start of BASE tick `t`, let `v_j(t^-)` be the carrier of initial copy `c_j` **before** token motion and before any interaction in that tick. Let `E_t^0` be the **actual** defect graph computed from the BASE engine's post-advance, pre-interaction snapshot at that tick. Define

`tau_C = min{t >= 1 : deg_{E_t^0}(v_j(t^-)) > 0}`.

This is a **graph-contact clock**: a bound path/cycle/multistar still counts as contact if its defect graph has an incident edge, whether or not an exchange or birth results. If the scientific target is instead the first *successful interaction*, define a different clock and preregister it; do not call the two equivalent.

The current §6.1 provenance sidecar logs token-changing events, but does not itself guarantee observation of **all** pre-interaction defect graphs, including bound configurations. Therefore `tau_C` requires a newly reviewed *read-only graph-snapshot hook*. The hook must observe the graph and tagged carrier actually used for this tick without calling mutating `orient_path` again or influencing event decisions. After tick `tau_C` finishes, the intervention target in §3 is the **then-current** carrier of `c_j`; it may differ from `v_j(t^-)` because the contact tick can swap/rotate copies.

`tau_slot^free` in the existing table is only a **counterfactual initial free-flight pair-time candidate**. Once other components interact, even a tag that has not itself interacted may encounter partners whose motions have changed. **It must never replace `tau_C`.** Candidate C may occur before, at or after `tau_B`; it is not automatically a "post-birth" comparison.

## 3. Target identity and fixed birth-provenance convention

**Declared convention carried from §6.1 (not physical identity):** each initial token copy has a distinct immutable origin; swaps transport copy identities; oriented path successor rotations transport the identities in the exact frozen engine permutation. At a star birth, the **newborn receives a fresh child-copy ID** descended from the centre's *pre-event* copy with the same sign; the centre retains its prior copy and its sign flips. Record parent, event tick, centre, newborn, current carrier, root and complete sign history. Equal numerical values never fuse identities, including `x=0` and `x=N/2`, for which sign flips can be invisible in the token value.

**Proposed target for a first comparator design (NOT PI-selected):** the single carrier `v_tau=carrier_tau(c_j)` of the **original slot copy** in `S_tau^0`. A carrier is identified by the provenance ledger, not by equal-value matching and not necessarily by original node ID `j`. Only the token at `v_tau` changes; descendants already present at the fork are **not** automatically modified. This defines a one-carrier intervention, not a lineage-wide replacement. The alternative targets—original node ID, first newborn, one specific descendant, all existing descendants and all future descendants—are distinct estimands and need separate approval.

A replacement is **not a birth** under TDR-G. The current `Provenance.check_ledger()` assumes a birth-only forest with all copies active and the same root value along parent/child birth edges. Mutating `u.delta[v_tau`] alone, reusing the old copy's root value, or silently disabling that guard is **invalid**. An implementation must add a separate `intervention` event/epoch to the provenance model (for example: retire the replaced carrier-copy, create a new active value-origin segment at the same carrier, and retain an explicit non-birth link to the replaced copy). Historical birth ancestry remains immutable; existing descendant copies keep their pre-fork value origins. Subsequent star births inherit the **new active segment's** value/sign under the fixed birth convention. The independent oracle and bijection/ledger checks must be extended to distinguish **birth** from **intervention** identities and retired versus active copies before any fork test is accepted. This implementation scheme is a **proposal**, not a completed or tested extension of PR #313.

## 4. Matched R/D operator — concrete candidate, not yet implemented

For a predeclared family `f` and every seed `z`, choose `r_f(z)` and `epsilon_f(z) in {-1,+1}` **before the BASE prefix**, identically for both potential arms:

- **O1** (if `N` even): `r_1 in {0,N/2}`, `d_1=(r_1+epsilon_1) mod N`.
- **O2** (only if `4|N`): `r_2 in {N/4,3N/4}`, `d_2=(r_2+epsilon_2) mod N`.

These match the *arithmetic classes* of the original Stage 1 arm definitions; the proposal neither reuses registered S1 seeds nor claims the later intervention reproduces S1 effects. Whether O1, O2 or both are included is a separate PI choice with multiplicity consequences.

At the common end-of-tick checkpoint, read the target copy's **pre-intervention** sign `sigma_tau in {+1,-1}`. Define the candidate one-carrier operator by

`I_a(S): delta[v_tau] <- (sigma_tau * x_a) mod N`, where `x_R=r_f`, `x_D=d_f`, `a in {R,D}`.

The same `v_tau`, `sigma_tau`, prefix and prechosen values are used for both arms. Each arm starts from its own deep clone. All other physical phases, node identities and tokens remain equal *at the intervention boundary*. No virtual tick, phase advance, birth, swap, population change or event counter increment is injected by the operator. The sign-covariant convention `sigma_tau*x_a` (rather than an absolute replacement `x_a`) is itself a design decision for PI approval; it agrees with a tick-zero replacement when `sigma_0=+1`. Record arm-specific no-op replacements without excluding their seeds.

**Accounting at the boundary:** label the alteration as a **separate intervention event**, then set the arm's physically consistent current census from `Counter(delta_after)`. Preserve prior absolute `fe,fb,t100`, history, cap/termination status, window accumulators and accumulated law-violation count; do **not** reset clocks to zero or misclassify the intervention as a normal birth. A proposed common post-fork allowed token alphabet for both arms is

`S_*=S_BASE union {+r_f,-r_f,+d_f,-d_f} (mod N)`.

This is **not** the unmodified TDR-G signed-alphabet invariance from tick zero: it is a new externally introduced-token boundary convention that must be explicitly logged and audited. The post-boundary engine must still obey the ordinary token/birth/census laws relative to its new declared baseline. Changing `alphabet` and `census` without extending the intervention ledger or without an independent boundary check would invalidate the test. The reference-prefix state remains unmodified.

The existing `az_tokres_provenance.py` implements **none** of `I_a`, the post-fork ledger extension or the dynamic contact hook. They are **development requirements**, not capabilities already supplied by PR #313.

## 5. Population Q, observation limits and endpoints — independent choices

### 5.1 Eligible target populations

For landmark `ell in {B,C}`, eligibility may be defined prospectively as

`A_ell(z;L,C,q) = {tau_ell(z) defined and <=L, prefix not terminated before fork, lineage/graph checks pass, M_{tau_ell}<q if that baseline restriction is chosen}`.

Here `L` (prefix limit), `C` (node cap), `q` (threshold) and the optional `M_tau<q` restriction are **unselected parameters**. The restriction is evaluated on the *common BASE prefix*, never on post-assignment R or D. For each separately chosen landmark, `Q_ell` is the law of `S_{tau_ell}^0` (including its preselected target and paired parameter bundle), conditional on the final preregistered `A_ell`. `Q_B` and `Q_C` need not be equal; comparing their numerical effect sizes does **not** isolate a birth-vs-contact mediation channel.

Report the full input seed count, fractions with no birth/contact by `L`, pre-landmark cap termination, other failure categories and baseline `M_tau>=q` separately, even if a restriction makes some observations ineligible. An unconditional *policy effect* that assigns identical no-intervention handling to all ineligible seeds is a **different estimand** and must not be silently substituted for `Q_ell`.

### 5.2 Post-landmark horizon H

Choose a fixed integer `H>=1` *before* generating new outcomes. It means **additional processed engine ticks after the completed landmark tick**, not absolute tick `H`, and not automatically the original S1 absolute `T=800`. Both arms share the same `H` and cap `C`. The current `RunState.tick()` stops when `iters >= T`; a fork implementation must therefore explicitly set the **continuation limit** `T_fork = iters_at_landmark + H` (for an ordinary complete-tick prefix, `iters_at_landmark = u.steps = tau_ell`) on both clones, after capturing their identical pre-intervention fingerprint. This is a recorded **configuration-boundary update**, not a tick reset, a new physical interaction, or permission to discard the prefix's clock history. Verify `T_fork-iters_at_landmark=H` and keep `iters`, `u.steps`, `fe`, `fb`, `t100` and historical counters untouched. Preserve absolute `u.steps` throughout; define post-fork tick `h=u.steps-tau_ell` only as a derived observation clock. Early cap termination is a genuine observed stopping event; no unexecuted events are imputed or fabricated.

### 5.3 Endpoint and censoring rule

A primary **candidate** is the binary threshold

`Y^a_{H,q}=1{max_{0<=h<=min(H,h_stop^a)} M^a_{tau_ell+h} >= q}`.

`q=100` is a comparability candidate (not an approved fork endpoint). Require `C>=q` if a node cap is used; then a cap reached before `H` entails `Y=1`, so binary threshold attainment is observed without a censored/negative misclassification. If `M_tau>=q`, the endpoint is already attained in *both* arms; either retain and flag such seeds or preregister their **common pre-assignment** exclusion—never drop based on R/D futures. `H`, `C`, `q`, and the status of already-positive prefixes are distinct PI decisions.

Secondary candidate: `G_H^a = M_{tau_ell+min(H,h_stop^a)}^a - M_{tau_ell}^0`, an observed node-count increment, explicitly cap-limited and not an uncensored fixed-H counterfactual. Do not treat post-fork first-birth clocks as the original runner's historic `fb`; define separate `fb_post` or `t100_post` fields if used, without resetting original historical fields or copying the TDR-26 diagnosis.

## 6. Estimand, null and inference limits

For a **single** fully chosen combination `(ell,f,target,Q_ell,H,C,q,I)`, denote the pinned engine continuation by `Phi_H` and the candidate endpoint by `g_H`. The paired reference-prefix estimand is

`Delta_post(ell,f;Q_ell,H)= E_{S~Q_ell}[g_H(Phi_H(I_R(S)))-g_H(Phi_H(I_D(S)))] `.

The sample unit is the independent BASE prefix seed `z`, not a post-birth node or all its descendant copies. One seed produces a matched R/D pair. A prospective analysis may estimate the mean of per-seed differences `Y_R-Y_D` on eligible seeds, with paired uncertainty and an explicitly predeclared family/multiplicity policy. No test, p-value, margin or sample-size calculation is specified in this **design-only** record.

**Interpretation:** an estimated nonzero `Delta_post` supports only an intervention effect *after the particular BASE landmark* in `Q_ell`, under the proposed counterfactual alteration. It is neither the S1 tick-zero contrast nor a mediation proportion. A zero or inconclusive result does not prove an early-only mechanism. The choice of post-birth eligibility can select a distinctive growth-prone BASE population; the two landmark populations are not interchangeable. An apparent contrast in a selected subgroup is not evidence of a universal growth law or a bridge to Dyadic OPEN-P1.

## 7. Acceptance gates before any later preregistration or campaign

**Gate D — design review (this PR):** Claude independently checks that first birth and slot-copy contact are genuine *BASE-prefix* clocks; that the target is identity-based; that operator, landmark, `Q`, `L`, `H`, cap, endpoint and value-family choices are separate; and that the token alphabet/lineage boundary is not silently treated as a native TDR-G birth. PI records each eventual choice separately. A PASS here only accepts a proposed design text.

**Gate I — implementation and synthetic tests (separate PR, not started):**
1. One pinned BASE prefix with zero sidecar influence; independent graph-snapshot clock for `tau_C` including bound cases, ties, carrier movement on the trigger tick and no graph-orientation double call. Negative control: substitute `tau_slot^free` for an actual later contact after earlier other-node interactions; detect incorrect use.
2. Fork each state with the same full pre-fork `fingerprint` (including provenance), identical preselected slot copy/arm values, exactly one carrier's physical token modified per arm, zero hidden changes to phases, nodes or inherited engine/runner counters. Detect ineligible/preterminal/threshold-already-met cases.
3. Extend provenance bookkeeping for explicit intervention/retirement (not birth), preserve historical genealogy, allow distinct current value roots, maintain a bijection on **active** copies and recheck sign/carrier/lineage histories independently. Include `x=0`, `x=N/2`, descendants present at fork, a previously swapped carrier, simultaneous prior births and token-value collisions. Detect a forged intervention counted as a birth, and a changed ancestor/descendant without registration.
4. Verify post-fork signed alphabet and census against a separate reference updater. Check the true TDR-G event/census law on **every later engine tick** and verify that only the explicit intervention boundary alters the baseline ledger. Keep ordinary historic clocks and observer-local TDR-26 windows intact.
5. Negative and metamorphic controls: `I_R=I_D` produces bit-identical continued trajectories (where deliberately set in a fixture); a no-op intervention reproduces uninterrupted BASE; instrumented/plain engine equality after applying the *same* physical change; uninterrupted versus checkpoint/restart equality on both arms including complete provenance and observer state; a swapped family-order label only relabels paired outputs. Confirm seed/order reproducibility and complete output hashes. No comparison can use value matching as provenance.
6. Explicit failure cases: wrong pin, missing target, invalid new lineage root, unsupported policies, orientation called twice, truncated history, mutant `alphabet` or `census`, duplicate token-copy carriers, skipped cap check and omitted nonattainers. Any failure stops without a scientific reading. Single-thread use only unless the observer architecture is independently redesigned.

**Gate P — prospective registration (future PI action):** freeze the exact operator/lineage extension, landmark and hook, `P_ref` and independent seed derivation, cell/profile, eligibility/`Q` including nonattainers, `L,H,C,q`, outcome/secondary outputs, analysis family/multiplicity, sample size/power assumptions, stopping rules, hardware/run costs, code hashes, gate logs and immutable custody **before** any new campaign. Reuse neither S1/S2 outcome records as confirmatory fork units nor post-outcome-selected parameter settings. Require independent implementation review and explicit PI compute authorization.

## 8. Decision register — all open at this draft

| Decision | Candidate(s) | Status |
|---|---|---|
| Landmark | B: first completed BASE birth tick; C: actual graph contact of original slot copy | **PI_PENDING** |
| Intervention target | Current carrier of original slot copy (proposed); newborn/descendant/whole lineage are distinct operators | **PI_PENDING** |
| Physical operator | One-carrier sign-covariant R/D replacement defined in §4; absolute-value replacement is a different operator | **PI_PENDING** |
| Value family | O1, O2 or separately registered families | **PI_PENDING** |
| Reference ensemble | New independent BASE seeds and preregistered slot/value draw law | **PI_PENDING** |
| Cell and representation | Prototype P1 / `bound_symmetric`; `N,k` to be chosen | **PI_PENDING** |
| Eligibility and missingness | `L`, pre-landmark cap, optional `M_tau<q`, no-landmark policy, population `Q` | **PI_PENDING** |
| Horizon and endpoint | `H`, `C`, `q=100` candidate, binary threshold vs separate count endpoint | **PI_PENDING** |
| Analysis and budget | Pairing, primary/secondary family, multiplicity, power, independent seed set, outputs and cost | **PI_PENDING** |
| Computation | Synthetic operator development and any new campaign | **NOT AUTHORISED BY THIS DRAFT** |

**Status:** design submitted for Claude co-owner criticism. The settled **§6.1 birth provenance convention** is retained for ordinary births, but the new *intervention boundary* is only proposed and needs independent implementation/validation. No data opened, no numerical fork run, no preregistration, no mechanism claim, no AZ DSN change, no tag or merge.
