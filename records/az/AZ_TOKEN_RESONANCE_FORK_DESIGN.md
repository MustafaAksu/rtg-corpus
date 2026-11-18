# AZ token resonance — §6.3 common-prefix fork design (review draft)

**[SESSION] NONCANONICAL · DESIGN ONLY · NOT PREREGISTERED · NO EXECUTION AUTHORISED.** Prepared by ChatGPT for the Claude AZ co-owner's independent review, 18 November 2026. The PI delegated drafting of §6.3; Claude's source-focused review `5954291073` of r1 is addressed in this r2 text. **No operator, landmark, target population, horizon, endpoint, cell, test or run has been scientifically selected or adopted** by that delegation. This record makes the alternatives operationally explicit so that the PI can choose them before any experiment. No DSN or source evidence is changed.

## 0. Authority, source scope and inference boundary

- **Governing AZ science:** `az-v0.10`, `dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` §§4.2.1–4.2.2, 8, release record `records/az/AZ_v0_10_RELEASE_RECORD.md` (targeted source reading). AZ remains Level A; S1/S2 are AZ-owned `NUM diagnostic` results, not growth-mechanism proofs. Its §8 TDR-G consumer pin remains `tdrg-v2.12.15`, even though TDR-G `tdrg-v2.13` is subsequently adopted.
- **AZ-pinned TDR-G owner source for rules and limits:** `tdrg-v2.12.15`, `dsn/RTG_DISCRETE_GENESIS_DSN.md` §§6.3, 6.13, especially `TDRG-ALG-EVENT-INVENTORY`, `TDRG-ALG-TOKEN-CENSUS-LAW`, `TDRG-ALG-PARENT-CHILD-PHASE`; targeted statements, not a full-owner rereview. The accepted AZ source-check `evidence/az/owner_sync/tdrg_v2_13_check.py` compares 24 cited TDR-G blocks at `tdrg-v2.12.15` and the later adopted `tdrg-v2.13`: these three §6.13 blocks are byte-identical. This draft **uses `tdrg-v2.12.15` as its cited owner pin**; any future AZ repin is a separate PI-governed edition decision.
- **Existing AZ design:** `records/az/AZ_TOKEN_RESONANCE_MECHANISM_DESIGN.md` §§4.1–4.2, 5, 6.1–6.3 (merged PR #281); exploratory S1-C1 readout `records/az/AZ_TOKEN_RESONANCE_MECHANISM_S1C1_TABLES.md` §§1–4 (merged PR #290), known outcomes, no causal timing identification.
- **Instrument at review scope:** `evidence/az/mechanism/az_tokres_provenance.py` / `PROVENANCE_NOTES.md` (PR #313, reviewed `5951975805`, merge `8de175c`). Source inspected: `Provenance`, `RunState`, `tick`, `checkpoint`, `fingerprint`, `OracleLedger`. Its synthetic validation does **not** establish an intervention operator or a prospective experimental pipeline.
- **Pinned computational profile for a candidate prototype, not a selected campaign:** engine `upload/tdrg-records/genesis_mode_b_mc.py` SHA-256 `4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608`, orientation `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` `ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c`, runner `evidence/az/scripts/az_tokres_run.py` `75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992`; P1, `bound_symmetric`, `CONV-TICK`. Original S1/S2 archive/profile pins remain untouched.

**Question:** Does an intervention made at a specified **boundary of the same unmodified BASE reference prefix** change the remaining trajectory? Boundary options include just before or just after the tagged copy's first BASE graph contact. A positive answer would show a **boundary-specific intervention effect in a specified reference-prefix population**. It would not identify the fraction of the original tick-zero S1/S2 effect mediated by births, or establish that early contact was irrelevant. The original S1 mechanism data informed these candidate hypotheses: any later inferential study needs new prespecified seeds, outcomes and analysis, not retrospective confirmation from S1.

## 1. Common BASE prefix and reference state

For each prospective unit, draw an independent seed bundle \`z\` from a *to-be-registered* law \`P_ref\`. At enrollment, before running the engine, fix four BASE phases and tokens, one initial slot-node index \`j=j(z)\`, and the paired intervention values/offsets in §4. Do not select \`j\` or parameter values by observing prefix growth. The reference prefix uses **only BASE tokens**, never R or D, with the same engine, orientation, policy and observation rules for all future forks.

Let \`S_t^0\` denote the full \`RunState\` at the **end of complete BASE tick** \`t\`, after all snapshot components and runner bookkeeping, with \`S_0^0\` the initialized pre-tick state. The initial copy at slot node \`j\` is \`c_j=j\` for the four-node initialisation; its current carrier \`carrier_t(c_j)\` is identity-tracked, not value-matched.

**Distinguish the BASE reference event time \`tau_ell\` from the physical fork boundary \`s_ell\`:**

- First-birth option B: \`s_B=tau_B\`.
- Pre-contact option C-: \`s_C-=tau_C-1\` (including \`s_C-=0\` when \`tau_C=1\`).
- Post-contact option C+: \`s_C+=tau_C\`.

The event \`tau_C\` is determined **only from the unmodified BASE trajectory**; for C- it is a one-tick *reference* look-ahead, known by pure graph prediction from \`S^0_{tau_C-1}\` before R/D assignment. C- does **not** require executing the contact tick or selecting a unit from either R/D outcome.

For a candidate \`ell\`, if its BASE event is defined by the fixed observation limit \`L\` and the boundary state \`S^0_{s_ell}\` is eligible, valid and **nonterminal**, set \`S=S^0_{s_ell}\`. "Nonterminal" means explicitly \`done=False\`, \`iters<T_ref\` for the reference runner's stopping budget and, for a positive cap, \`M_{s_ell}<C\`; do not treat a nominally false \`done\` at \`iters=T_ref\` as sufficient. Configure a reference runner with \`T_ref>=L+1\` when observing possible boundaries through tick \`L\`, or handle continuation limits with an independently validated equivalent. Clone the complete \`S\` once for each arm; fingerprints, historical clocks and target identity are equal **before** the boundary intervention. Never fork an R or D prefix or select eligibility using its future.

Undefined landmarks and stopped/invalid prefixes are enumerated in a preregistered eligibility inventory. A late or missing contact is never silently replaced with \`tau_slot^free\`.

## 2. Dynamic landmark definitions — B, C- and C+ are distinct candidates

### 2.1 Candidate B: end of first complete BASE birth tick

\`tau_B=min{t>=1:births(S_t^0)>births(S_{t-1}^0)}\`, with \`min(empty)=undefined\`; \`s_B=tau_B\`. Read the engine's **actual** BASE birth increment and fork after every component and the entire birth tick have completed. Multiple same-tick births require no order-dependent selection when the target is the original slot copy, but a first-newborn alternative needs its own predeclared tie rule. A first-birth-eligible population is conditional on a BASE event, **not** the original unconditional S1 population.

### 2.2 Common BASE actual-contact clock for C- and C+

At the **end of BASE tick \`t-1\`**, let \`v_j(t^-)=carrier_{t-1}(c_j)\` and compute the pure *would-be BASE pre-interaction graph* for tick \`t\`:

\`theta_i^{pre}(t)=(theta_i^0(t-1)+delta_i^0(t-1)) mod N\`;

\`E_t^0=graph_edges_for(nodes_{t-1}^0,theta^{pre}(t),N,k)\`.

Then define \`tau_C=min{t>=1:deg_{E_t^0}(v_j(t^-))>0}\`. The graph is that used by the unmodified BASE engine at the next tick **if BASE is continued**. It includes simultaneous edges, bound cycles, paths and multistars; it is a **contact** clock, not the first successful token exchange or counted event. Since \`step_universe\` first advances all phases and then constructs \`graph_edges_for\`, no *new mutating hook* is required. The §6.1 instrument's oracle uses the same pure graph construction. **Gate I** still needs one test against a read-only observed engine graph, including bound cases and no extra orientation calls, to certify this equality in the new code.

The contact clock is dynamically recomputed from each actual previous **BASE** boundary; it is **not** \`tau_slot^free\` (which assumes initial free flight and can fail once other nodes have interacted). For C- the BASE one-tick prediction is made **before** arm assignment; for C+ the BASE contact tick itself is executed before cloning. No event in an R/D branch is used to decide \`tau_C\`.

### 2.3 C- (pre-contact): \`s_C-=tau_C-1\`

Fork at \`S^0_{tau_C-1}\`, **before** the anticipated BASE contact's phase advance. Applying \`I_R\` or \`I_D\` changes the target's advance and may alter the defect graph at tick \`tau_C\`, including whether contact occurs at all. \`tau_C\` is therefore a **reference BASE potential contact time**, not a promise of contact in either treated continuation. An arm-specific actual first-contact time must be observed independently if reported.

For \`tau_C=1\`, \`s_C-=0\`; the absolute one-carrier intervention of §4 then writes the slot token at tick zero **exactly as the frozen S1 \`arm_state\` function does** for the same \`th0,d0,j,r_f,epsilon_f\`. This is an operator-level/metamorphic identity, **not** an equality of the C- eligible population, horizon, or estimated effect with S1.

### 2.4 C+ (post-contact): \`s_C+=tau_C\`

Continue BASE through the first tagged-copy graph-contact tick and fork at its **complete end**. The first contact therefore occurs with the BASE token in both copies of the prefix. The current carrier \`carrier_{tau_C}(c_j)\` may differ from \`v_j(t^-)\` because that tick can swap/rotate provenance identities. C+ asks about the effect **after** the contact and cannot directly change that first contact. C- and C+ answer different intervention questions; their eligible state laws generally differ.

## 3. Target identity, birth-provenance convention and centre/newborn choice

**Birth convention from the merged §6.1 instrument (bookkeeping, not physical identity):** swaps transport copy identities; path rotations transport identities in the engine's frozen successor permutation. At a star birth the **newborn receives a fresh child copy** descended from the centre's *pre-event* copy with the same sign; the **centre retains its old copy** and flips sign. Parent, root, birth tick, sign history, current carrier and copied sign are recorded. Equal-valued roots never fuse, including \`x=0\` and \`x=N/2\`.

**First candidate target (not PI-selected):** the single physical carrier \`v_s=carrier_{s_ell}(c_j)\` of the *original slot copy* at the chosen fork boundary. Its token alone is replaced. This is a target **defined by declared identity**, not a fixed node ID and not value matching. Existing descendants are not automatically modified; targeting original node ID \`j\`, one newborn, a particular descendant, all existing descendants or all future descendants are separate physical operators.

**The birth-centre versus newborn ambiguity is material.** If the slot copy \`c_j\` is carried by a star centre at a BASE birth before or on the fork boundary, the declared convention keeps \`c_j\` on the **centre**, which has the post-birth token \`-x\`; its newborn receives a new child-copy ID and has token \`x\` at the antipodal position. A different birth-provenance convention could instead assign the tracked copy to the **newborn**; the intervention would then modify a different **physical node**. List explicitly as a PI sub-choice: **current carrier of original copy / post-birth centre** versus **the corresponding newborn copy/carrier**. For repeated births from the same tracked copy, an "associated newborn" requires a further predeclared tie rule (e.g. first or most recent corresponding birth) and an exact rule for following that newborn's current carrier. Do not change the §6.1 convention merely to pick a favourable result; a child-target operator is a new selection rule, not a relabeling of the centre-target result.

Before any future analysis, report from BASE only: numerator and denominator of eligible seeds where \`c_j\` was a star-birth centre in one or more completed ticks through \`s_ell\`; the subset where the triggering B tick itself has such a birth; and, separately, whether a candidate child-copy target exists at the boundary. This is **pre-assignment provenance** reporting, not a post-R/D subgroup. For C- do not count a future birth at \`tau_C\`, because it has **not** occurred at boundary \`tau_C-1\`.

**Intervention != birth.** Current \`Provenance.check_ledger()\` expects a birth-only forest and constant root value along its birth edges. Simply mutating \`u.delta[v_s]\`, recycling the old copy's root value, or silencing the guard would be invalid. A future implementation needs a distinct audited **intervention event/value-origin epoch** (e.g. retiring the replaced current segment, making a new active segment at the same carrier with a non-birth link). The *historical* birth ancestry remains immutable; existing descendants retain their own provenance and values. Later star births inherit the active segment's value/sign under the same **birth** convention. Extend the oracle, copy/carrier ledger and active-identity bijection for this new boundary before any applied-fork tests. The epoch scheme is **unimplemented**, not a property of PR #313.

## 4. Matched R/D operator — absolute replacement candidate; sign-covariant alternative

For a chosen family \`f\`, prespecify an independent \`r_f\` and symmetric \`epsilon_f in {-1,+1}\` **before any BASE prefix**, together with slot \`j\` and seed \`z\`:

- **O1** (even \`N\`): \`r_1 in {0,N/2}\`, \`d_1=(r_1+epsilon_1) mod N\`.
- **O2** (only \`4|N\`): \`r_2 in {N/4,3N/4}\`, \`d_2=(r_2+epsilon_2) mod N\`.

For matching the Stage 1 *assignment law* in a later comparison, use the same **uniform** O1/O2 choices and independent fair \`epsilon\` as the pinned \`az_tokres_run.py:arm_choices\`; this is not permission to reuse S1 seeds or outcomes. The family and exact draw law remain PI_PENDING.

**Proposed physical candidate, not yet selected: an absolute one-carrier write**

\`I_a^abs(S): delta[v_s] <- x_a mod N\`, with \`x_R=r_f\`, \`x_D=d_f\`, \`a in {R,D}\`.

The same carrier node \`v_s\` is selected from the common BASE state, and the same preassigned \`r_f,epsilon_f\` determine both arm values. There is **no dependency on the bookkeeping sign**. At \`s=0\` this is exactly the S1 tick-zero token assignment \`arm_state\` for the same draw, phases and slot (operator identity only; no assertion about S1 population/horizon). The pre-existing value and any no-op arm are reported without post-hoc exclusion.

**Unselected alternative: sign-covariant write**, \`I_a^sign(S):delta[v_s] <- sigma_s*x_a mod N\`, where \`sigma_s\` is the §6.1 provenance sign. This alternative changes the per-seed physical assignment when \`sigma_s=-1\` and hence depends on an explicitly *nonphysical* birth-copy bookkeeping convention. Under independent symmetric Stage 1 value draws, its **marginal assignment law** coincides with the absolute rule: in O1, \`sigma_s*r_1=r_1\` because \`2r_1=0 mod N\`, and \`sigma_s*epsilon_1\` remains a fair sign; in O2, uniform \`r_2 in {N/4,3N/4}\` is invariant under \`r_2->-r_2\`, with the independent fair neighbour sign transformed accordingly. **No per-seed potential outcomes or conditional effects are thereby equated.** The sign-covariant variant is a separate PI choice and not the default comparator proposal.

No virtual tick, phase advance, birth, swap, population change or engine event counter increment is injected by either operator. Each R/D starts from an independent deep copy of the *same complete* BASE boundary fingerprint.

**Boundary accounting:** record a separate \`intervention\` event, create a physically consistent active provenance segment as specified in §3, and set the arm's census to \`Counter(delta_after)\`. Preserve absolute \`fe,fb,t100\`, all Universe histories, cap/termination status, observer windows and accumulated law-violation count. An external replacement may introduce a new signed token family. A candidate **common** post-boundary admissible alphabet for both arms is

\`S_*=S_BASE union {+r_f,-r_f,+d_f,-d_f} mod N\`.

This expands the TDR-G signed-token alphabet *only at an explicitly logged non-native intervention boundary*, not through an engine birth. After the boundary, verify the ordinary TDR-G token/census laws against the new declared baseline, including every subsequent actual birth. The reference BASE prefix is preserved byte-identically. Neither \`I_a\` nor intervention-epoch/graph-boundary support exists in the merged §6 instrument; all require a separate reviewed implementation.

## 5. Population Q, observation limits and endpoints — independent choices

### 5.1 Eligible target populations

For \`ell in {B,C-,C+}\`, let \`tau_ell\` denote the corresponding **BASE event time** (\`tau_B\` or \`tau_C\`), and \`s_ell\` its actual fork boundary from §1. A candidate eligibility event is

\`A_ell(z;L,C,q)={tau_ell defined and <=L, S^0_{s_ell} valid with done=False and iters<T_ref, M_{s_ell}<C if C>0, and optionally M_{s_ell}<q}\`.

Here the chosen prefix limit \`L\`, cap \`C\` (\`C=0\` means no cap), endpoint threshold \`q\` and optional common pre-assignment threshold restriction are **separate unselected parameters**. A cap reached on the BASE boundary is terminal and invalid for fork eligibility. For C-, the one-tick **BASE potential** graph at \`tau_C\` is computed from \`S^0_{tau_C-1}\`, *before* either arm is intervened on; neither R nor D's subsequent contact is used for eligibility. Selecting on this potential BASE event is **not** selecting on any realized post-assignment R/D event, but it does define a reference-event-conditioned target population.

Define \`Q_ell\` as the law of the tuple \`(S^0_{s_ell},j,r_f,epsilon_f,tau_ell)\` from independent reference seeds conditional on \`A_ell\`. The pairs \`Q_B\`, \`Q_C-\`, \`Q_C+\` differ in boundary time, histories and eligibility, even when C-/C+ refer to the same BASE contact event; contrasts across these distributions do **not** constitute a mechanism decomposition.

Report the *full* number of reference seeds, missing/no-contact/no-birth cases by \`L\`, pre-boundary termination, cap hits, validation failures and already-positive \`M_{s_ell}>=q\` counts. Count and report pre-boundary slot-copy-centred births as in §3. Missing/terminated seeds are never quietly omitted from denominators. Extending an eligible-only contrast to an all-seed policy effect would be a **different estimand**, requiring a predeclared identical treatment for ineligible seeds.

### 5.2 Additional post-boundary horizon H

A fixed integer \`H>=1\` means **H additional engine ticks after boundary \`s_ell\`**, not H ticks after the reference contact when \`ell=C-\`, and not automatically S1's absolute tick \`T=800\`. Both arms have the same H and cap C. Since the merged \`RunState.tick()\` stops when \`iters>=T\`, a future fork implementation must capture an identical *pre-intervention* fingerprint then explicitly set \`T_fork=iters_at_boundary+H\` on both clones as a **configuration boundary** (not a physical engine event). Keep \`iters\`, \`u.steps\`, historic \`fe,fb,t100\` and counters unchanged; verify \`T_fork-iters_at_boundary=H\`. The post-fork clock is \`h=u.steps-s_ell\`. End-of-step cap stopping is observed and recorded, not imputed; no fake clock reset is permitted.

### 5.3 Endpoint, monotonicity and cap boundary

The primary **candidate** binary threshold is

\`Y_{H,q}^a = 1{M^a_{s_ell+min(H,h_stop^a)} >= q}\`,

because the pinned TDR-G engine **only adds nodes at births and does not delete them**, so \`M_t\` is nondecreasing on each uninterrupted continuation. This is identical to \`1{max_{0<=h<=min(H,h_stop)} M_{s_ell+h}^a>=q}\`. A preregistered \`q=100\` is a **candidate only**, not fixed by this draft. If positive cap \`C\` is used, require \`C>=q\`; then hitting the cap before H entails \`Y=1\`, avoiding a false negative from a stopped run. If \`M_{s_ell}>=q\` already, the threshold is positive in **both** arms; retain/flag it or exclude with a preregistered *common BASE-boundary* rule, never based on R/D futures.

An optional secondary endpoint is \`G_H^a=M_{s_ell+min(H,h_stop^a)}^a-M_{s_ell}^0\`: observed cap-limited growth, **not** an uncensored full-H counterfactual where an early cap stops. Optional BASE-no-intervention continuation from the exact same fork boundary can be recorded as a **secondary reference arm**, not an extra multiplicity-unaccounted R/D test family. Any post-fork event clock has its own name (\`fb_post\`, \`t100_post\`) and does not overwrite original \`fb\`, \`t100\` or TDR-26 windows.

## 6. Estimand, null and inference limits

For a **single** fully chosen combination `(ell,f,target,Q_ell,H,C,q,I)`, where `ell in {B,C-,C+}` and H is counted from **s_ell**, denote the pinned engine continuation by `Phi_H` and the candidate endpoint by `g_H`. The paired reference-prefix estimand is

`Delta_post(ell,f;Q_ell,H)= E_{S~Q_ell}[g_H(Phi_H(I_R(S)))-g_H(Phi_H(I_D(S)))] `.

The sample unit is the independent BASE prefix seed `z`, not a post-birth node or all its descendant copies. One seed produces a matched R/D pair. A prospective analysis may estimate the mean of per-seed differences `Y_R-Y_D` on eligible seeds, with paired uncertainty and an explicitly predeclared family/multiplicity policy. No test, p-value, margin or sample-size calculation is specified in this **design-only** record.

**Interpretation:** an estimated nonzero `Delta_post` supports only an intervention effect *at the designated BASE-derived fork boundary* in `Q_ell`, under the proposed counterfactual alteration. It is neither the S1 tick-zero contrast nor a mediation proportion. A zero or inconclusive result does not prove an early-only mechanism. The choice of post-birth eligibility can select a distinctive growth-prone BASE population; the two landmark populations are not interchangeable. An apparent contrast in a selected subgroup is not evidence of a universal growth law or a bridge to Dyadic OPEN-P1.

## 7. Acceptance gates before any later preregistration or campaign

**Gate D — design review (this PR):** Claude checks the AZ/TDR-G adopted **source pin**, the three BASE reference landmark options and exact distinction \`tau_ell\` versus \`s_ell\`; the identity-based target and **centre-vs-newborn** sub-choice; the absolute and sign-covariant physical operators as different interventions; the independent choices of \`Q,L,H,C,q\`; and the fact that an external intervention must not be disguised as a native TDR-G birth. A textual PASS is not scientific adoption or consent to run a fork experiment.

**Gate I — synthetic-only implementation/review (separate PR, not started):**
1. A single pinned BASE prefix. Determine \`tau_C\` by *pure recomputation* from each complete preceding end-of-tick state (\`theta+delta\` then \`graph_edges_for\`); check against the actual frozen engine graph in a bounded fixture using a read-only observation wrapper employed only for equality verification. Cover all component types, tied graph contacts, previously moved slot-copy carriers, undefined contacts, bound cycles/multistars and no extra mutating orientation call. Negative control: substitution of \`tau_slot^free\` after other-node interactions must fail.
2. Explicit C- and C+ boundary construction. In C- retain the untouched state at \`tau_C-1\` and do **not** run the BASE contact tick on the fork clones; C+ waits until the complete \`tau_C\` BASE tick. Observe whether R/D actually make contact at the reference tick; it need not happen under C-. Require \`done=False\`, \`iters<T_ref\`, and (if capped) \`M<C\` on the selected boundary. Compare full common fingerprints before intervention and audit the subsequent \`T_fork=iters+H\` configuration change.
3. One-carrier absolute operator with the original \`j,r_f,epsilon_f\` and unchanged other phases/tokens/node IDs. For \`tau_C=1\`, C- at tick zero must agree **exactly per seed** with frozen runner \`arm_state\` for the same O1/O2 assignment (not simply in distribution); use an explicit fixture. For equal-arm operator values, no-op replacements and an optional sign-covariant alternative, test each exact physical assignment and noninfluence of bookkeeping signs in the absolute case.
4. Extend the provenance ledger for an explicit **intervention** (not birth) identity/value-origin epoch, with active vs retired copy segments and preserved prior ancestry; distinguish centre target from newborn/child-copy target when a tagged copy has triggered a birth. Report eligible BASE seeds with any such birth (including the landmark tick for B, but **not** a not-yet-executed C- contact tick). Independently check value history, sign events, carriers, birth counts, duplicate token values and pre-existing descendants.
5. Validate the post-boundary signed alphabet/census via a separate updater and every later TDR-G engine tick's unchanged natural event/census laws. Preserve absolute runner clocks, full observer state and stopping/cap semantics; no silent reset. Compare instrumented/plain trajectories, uninterrupted/full-checkpoint restarts (including provenance), both R/D potential continuations, and optional BASE reference arm when requested.
6. Negative/metamorphic controls: \`I_R=I_D\` gives bit-identical continuations; a no-op write reproduces the unaltered BASE reference; swapping R/D labels swaps paired outputs without changing values; deliberately wrong birth target, lost ancestry, mutated \`alphabet\`, omitted nonattainers, bad target, bad pin, duplicate active copy IDs, skipped cap, truncated sign history, double orientation and incorrect C- timing all fail closed. Run single-threaded unless observer architecture is separately certified.

**Gate P — later registration and explicit PI compute decision:** freeze, **before any new run**, exact choice of operator form, one of B/C-/C+, centre/newborn target sub-choice, reference seed law and \`j,r,epsilon\` generation, cell/profile, target population and missingness, \`L,H,C,q\`, primary/secondary outcomes, analysis family/multiplicity, sample size/power, seed independence, stopping and costs, code hashes, validation gates and immutable output custody. Existing registered S1/S2 input/results cannot be reused as confirmatory fork outcomes. A completed design or synthetic Gate I does **not** itself authorize a campaign.

## 8. Decision register — all open at this draft

| Decision | Candidate(s) | Status |
|---|---|---|
| BASE event and fork boundary | B: end of first BASE birth tick; C-: end of tick before the first actual BASE tagged-copy contact; C+: end of that contact tick | **PI_PENDING** |
| Operator form | **Absolute value write** \`delta[v_s]<-x_a\` (candidate); sign-covariant write \`delta[v_s]<-sigma_s*x_a\` (alternative) | **PI_PENDING** |
| Physical target | Current carrier of original slot copy (candidate) versus original node ID / descendants / an associated newborn | **PI_PENDING** |
| After slot-copy-centred birth | Retain/copy on centre under §6.1 convention versus target newborn child copy/carrier; choose associated newborn when multiple | **PI_PENDING** |
| Value family | O1, O2 or separately registered families; uniform \`r\` and fair \`epsilon\` draw if matching S1 assignment law | **PI_PENDING** |
| Reference ensemble | New independent BASE seeds and prespecified slot/value draw law | **PI_PENDING** |
| Cell and representation | P1 / \`bound_symmetric\` only in current instrument; \`N,k\` not selected | **PI_PENDING** |
| Eligibility and missingness | Event cutoff \`L\`, nonterminal state, optional \`M_s<q\`, BASE-event-conditioned population \`Q\`, no-landmark policy, birth-centre incidence report | **PI_PENDING** |
| Horizon and endpoint | \`H\` **after the fork boundary**, \`C\`, \`q=100\` candidate, threshold vs growth endpoint; optional BASE reference arm | **PI_PENDING** |
| Analysis and budget | Pairing, inferential family, multiplicity, power, independent seed set, output and cost | **PI_PENDING** |
| Implementation / computation | Separate synthetic operator/graph tests, any prospective preregistration and subsequent campaign | **NOT AUTHORISED BY THIS DRAFT** |

**Status:** r2 text incorporates Claude review `5954291073` (R1–R4 required; R5–R8 recommendations) and is submitted for changed-content readback by the Claude AZ co-owner. The settled **§6.1 birth provenance convention** is retained for ordinary births, but the new *intervention boundary* is only proposed and needs independent implementation/validation. No data opened, no numerical fork run, no preregistration, no mechanism claim, no AZ DSN change, no tag or merge.
