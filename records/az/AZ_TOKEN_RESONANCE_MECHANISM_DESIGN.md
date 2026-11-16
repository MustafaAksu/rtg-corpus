# AZ token resonance — mechanism design

**[SESSION] NONCANONICAL — design proposal, not a preregistration, adopted result, or campaign authorization.** Prepared by ChatGPT, 16 November 2026; revised after co-owner review `5920669916` on PR #281. No canonical file, frozen evidence, or registered campaign parameter is changed.

## 1. Decision and question

The PI wrote in this project conversation: “brinci öneri ile devam edebiliriz” (proceed with the first proposal). The first proposal was the mechanism question: does the seed-token effect arise during early contact/first birth, during subsequent growth, or both? Receipt: PR #279 review `5920431601`. This selects the direction, not an operator, sample size, endpoint, or new campaign. Orders 3/4 and TDR-26 Stage 3 are not selected. The Claude lane correctly records this decision as source-reported to that lane; it was directly received in this ChatGPT conversation.

AZ v0.10 is adopted: tag `az-v0.10`, merge `062a1728d8b98aa026c751ecc77d45026538a8ca`, DSN SHA-256 `0cc84c9a587bab270624a824d5e004a327f20f41f0c03307e01a6725afe80e6e`. Release record §8 excludes a mechanism claim and any new campaign. S1 and S2 keep their separate scopes and grades; Level A and AZ-OPEN-PROMO are unchanged. No separate TDRG numerical-result item is to be filed.

PR #279 was merged as `2d898fdafedee7f5b3d4628fe0c08ef2871a8b0c`; outgoing notices are queue events, not consumer adoption. PR #284 contains the responsible lane's entry-note correction and links this fixed-path design. This document does not replace that entry note or rewrite frozen adoption records.

## 2. Sources, review disposition, and evidence extent

| Source | Identity and reading extent |
|---|---|
| AZ owner | `az-v0.10`, §§4.2.1–4.2.2 and guards read in the release reviews; release record §§6–8 previously checked. Current BASELINE re-read in this revision. Not a new full-DSN review. |
| TDR-G context | AZ's existing pin `tdrg-v2.12.15`, also listed in current BASELINE. Owner candidate #265 and Atlas row-check #277 are not substituted for the tagged owner. No automatic repin. |
| Runner | `evidence/az/scripts/az_tokres_run.py` at `74ad6946e9710a2272b9d7792d6d8f0c45cda168`; `run_state`, observer-local variables, clocks and output fields re-read. Recorded SHA-256 `75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992`; not rehashed here. Seed/arm construction was read in r1. |
| Engine and orientation | At the same commit: `upload/tdrg-records/genesis_mode_b_mc.py`, swap/path/birth rules and `step_universe` re-read (lines 590–840); geometry, initialization and `Universe` read in r1. Recorded engine SHA-256 `4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608`. Complete `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` read in r2; recorded SHA-256 `ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c`. Neither executed or rehashed here. |
| Registered analysis | Stage 2 r2 at the same commit, §§6.1–6.7 previously inspected. Its endpoint and control contracts are unchanged. |
| Co-owner review | `5920669916` on original design `a7ffd0ac771a02649aa60f2eabee9352adf19566`, read in full. A1–A4 accepted with the inference and implementation boundaries below. |
| Co-owner instrument | PR #284 at `b93f152175a790e66b8c84fa39661c2eca93bfce`: complete `contact_instrument_check.py`, saved output, and entry-note diff read. The saved 35 targeted / 31,800 synthetic scan comparisons and 10,329 engine agreements are source-reported executions, not a rerun by this reviewer. |
| Current independent checks | `evidence/az/mechanism/contact_scope_checks.py` and `contact_scope_checks_output.json`, executed by ChatGPT in r2; standard-library Python, exact integer arithmetic. No engine import, registered input, growth endpoint or campaign run. Details in §4.4. |
| Governance | Current CONVENTIONS §§1–7 read. Methodology v1.4 §§12–13.5 were read in the preceding review. |

| Review proposal | Disposition |
|---|---|
| A1: first-contact configuration as well as time | Accepted (§4.1, §5). The additional one-arm absence inference is not accepted; a counterexample and a paired sufficient condition replace it (§4.2). |
| A2: short free orbits | Accepted as arithmetic descriptors, not a mechanism (§4.3); relative advances and a common-advance-shift invariance guard added. |
| A3: reviewed table script before data access | Accepted (§5). The outcomes are already known; freezing the script does not make the analysis confirmatory. |
| A4: provenance tracking before carrier/lineage forks | Accepted (§6.1). Full observer state, not only `Universe`, belongs in the restart contract (§6.2). No operator is selected from exploratory output. |

## 3. Separate the clocks

[SESSION] Define:

- `tau_contact`: first processed tick with any edge in the **post-advance, pre-interaction** defect graph. Tick zero is not processed contact.
- `tau_event`: runner `fe`, the first nonzero cumulative counter among single-edge swaps, path interactions, births, multistars seen, or path ties seen. The bound-cycle counter is absent.
- `tau_birth`: runner `fb`, recorded after the first positive birth increment. The engine writes `birth_steps_list` before incrementing `u.steps`; conversion to the runner clock must be explicit.

The PR #284 synthetic sample reports `fe = tau_contact` in 10,241 cases and a lag of 1–7 in 88 cases; it also reports 88 bound-four-cycle first-contact configurations. These are finite-sample descriptions, not a universal lag bound, and its PASS gate tests contact-time agreement, not a general assertion about `fe`.

**Exact limitation.** At `(N,k)=(120,8)`, `theta=(0,0,60,60)` and `delta=(0,0,0,0)` give a stationary `K2,2`. Contact occurs at tick 1; the inspected bound-cycle branch changes neither phases nor tokens, and none of the counters defining `fe` ever fires. Thus `fe` can remain absent forever despite finite `tau_contact`. The geometry is checked by §4.4; the all-time statement follows from the source rule, not an executed engine replay.

The summary records `t100` and `M_at` but no full first-birth checkpoint. `keep_final` returns only final phase/token dictionaries. Do not invent an intermediate state from summaries.

## 4. Exact early-contact instrument

[SESSION][ALG] Bounded derivation from the inspected update order; no novelty or adopted owner grade claimed. For even `N`, integer `0 <= k < N/6`, and four initial nodes, all components before first contact are isolated, so tokens are unchanged. Through the first pre-interaction snapshot,

    theta_i(t) = theta_i(0) + t delta_i(0)  (mod N).
    a_ij = theta_i(0) - theta_j(0) - N/2,
    b_ij = delta_i(0) - delta_j(0).
    tau_contact = min { t >= 1 : a_ij + t b_ij = e (mod N)
                                  for some i<j and integer e in [-k,k] }.

Set `min(empty)=infinity`. The isolated-component branch proves free flight at every earlier tick; at the first nonempty tick the predicate is exactly the engine's defect predicate.

With `g=gcd(N,b_ij)`, a congruence is solvable iff `g` divides `e-a_ij`. For `L=N/g > 1`,

    t = ((e-a_ij)/g) * inverse(b_ij/g modulo L)  (mod L),

replacing zero by `L` to obtain the first positive time. For `b_ij=0 mod N`, the pair is either always in band (first processed time 1) or never in band. Minimize over six pairs and all band residues. The free-flight graph repeats after `N` ticks; no contact in `1..N` means no contact ever and hence no birth for this initial state. A free-flight pair time after the first global contact need not be its actual later time.

### 4.1 First-contact configuration (A1)

For finite `tau_contact`, compute all phases at that tick by the displayed formula, then the **whole** defect edge set `E_contact`. Preserve simultaneous edges and every connected component, including isolated nodes. Record the edge list, component partition/type multiset, the slot node's degree and component role, and whether the first graph contains a unique-centre star. Do not select an arbitrary first pair and discard ties. For the inspected four-node, narrow-band, `bound_symmetric` setting, a first-contact `star_k1c_c3` triggers a birth at that tick; this does not say that the slot was the centre or that the later endpoint is determined.

These are pre-interaction descriptors but **post-intervention** variables: being computable from initial data does not make them pretreatment covariates. Existing `th0`, `d0` and slot metadata suffice; no trajectory stepping is needed. Classification must be checked against the pinned component classifier on synthetic first-contact snapshots before application. PR #284 checks first-contact times; do not describe it as an independent exhaustive graph-classifier validation.

### 4.2 Paired invariance, not a one-arm mechanism exclusion

For a one-slot replacement at node `j`, the three non-slot pair candidates are common:

    tau_contact^a = min(tau_common, tau_slot^a),  a in {R,D}.

**Rejected inference from review 5920669916:** absence of `j` from the resonant arm's first contact, even among endpoint-positive runs, does not establish that the intervention could not affect first contact. The other arm can have an incident edge absent in R. Also, endpoint positivity in R alone is not a paired causal contrast.

**Synthetic counterexample to the implied first-contact invariance:**

    N=120, k=8, j=0,
    theta=(109,97,80,2),
    delta_R=(0,41,21,96), delta_D=(1,41,21,96).
    tau_R=tau_D=2,
    E_R={(1,2)}, E_D={(0,1),(1,2)}.

No earlier processed edge exists. The slot is absent in R but changes the first graph relative to D. §4.4 checks this exactly; no growth outcome is evaluated and no mechanism is demonstrated by this fixture.

A valid **sufficient condition for first-event invariance** is finite `tau_common` with both `tau_slot^R > tau_common` and `tau_slot^D > tau_common` (infinity allowed). Then neither arm has a slot edge before or at the common contact, the non-slot phase/token states agree, and the first graph and the non-slot interaction updates are identical under the inspected rules. This does not imply equal full states, later paths, or outcomes. Equality cases are ties, not strict invariance certificates. Report the paired event/configuration comparison; do not infer a mediated fraction or an early-only/late-only mechanism from it.

### 4.3 Orbit arithmetic (A2)

[SESSION][ALG] Under unchanged token `x`, the single-node free orbit has period

    P(x)=N/gcd(N,x), including P(0)=1.

For the registered even cells, `2x=0 mod N` gives `P=1` or `2`; `2x=N/2 mod N` exists only if `4|N` and gives `P=4`. The neighbour's period is exactly `N/gcd(N,x±1)`; use the exact value, not a universal “long” label.

First-contact geometry depends on phase offsets and **relative** periods `P_ij=N/gcd(N,delta_i-delta_j)`. Adding a common `c` to all advances adds `tc` to every free phase and leaves every free-flight graph unchanged although individual orbit periods may change. This is a first-contact/free-flight invariance, not a claim about the full birth dynamics. Store both individual and relative descriptors; short orbit alone is not an explanation. §4.4 checks 240 common-shift comparisons on the paired fixture.

### 4.4 Acceptance evidence and remaining tool gates

The co-owner's `contact_instrument_check.py` at PR #284 reports scan agreement on 35 targeted and 31,800 synthetic states, plus 10,329 pinned-engine time agreements. Its output is inspected, not rerun here. These counts do not establish general correctness by themselves; the derivation above supplies the all-state statement within its hypotheses.

**Coverage correction:** independently scanning the exact 35 targeted inputs shows that none has `tau_contact=N`. Their per-cell times are in `contact_scope_checks_output.json`; the “N-ish” comment does not test the residue-zero boundary. The extra fixture `(N,k)=(12,0)`, `theta=(0,6,0,0)`, `delta=(1,0,1,1)` has `tau_contact=12` and explicitly exercises it. A separate nonzero-relative-advance, unreachable fixture is included. Keep the original #284 evidence unchanged; qualify its coverage and include these explicit acceptance fixtures in the production table instrument.

Executed here: `python3 -I evidence/az/mechanism/contact_scope_checks.py`. Independent solver versus direct scan agrees on all **62,804** tuples `(N,k,a,b)` with even `2<=N<=40`, integer `0<=k<N/6`, and all residues `a,b`; the 35 coverage inputs, two boundary fixtures, one-arm-absence fixture, 240 common-shift comparisons, and stationary-cycle geometry also pass. Finite exact checks, not an engine replay or an empirical mechanism result.

- Script SHA-256: `e52a75969cb35440e0d7cbc6d2d3978d637b0f5e0495bb09f8ddcc1f6279cfac`.
- Output `contact_scope_checks_output.json` SHA-256: `2020e01df3c9dd0da1e47660f0c9486c352c8b94f61f429544cf20f386eafae1`.
- Independence: new standard-library implementation and direct scan; the formula and the 35 input fixtures are shared. No engine import, registered tag/data, or growth endpoint. The co-owner's engine tests remain source-reported.

Production acceptance still requires complete first-contact graph/classifier checks, label/phase covariance, simultaneous components and slot ties, invalid-input refusal, and reproducible input/output identity. A PASS of these tools is not scientific adoption.

## 5. Existing-record table contract (A3; exploratory only)

No Stage 1/2 records are opened by the new table analysis before its script and input manifest are reviewed and frozen. Specify script SHA-256, exact input commits/manifests, stage/profile/cells/arms, pairing keys, missing-data rules and every output table. The initially proposed cell `(120,8)` remains a proposal; no cell or extension is selected by inspecting a mechanism table. Known outcomes make the exercise secondary exploratory even after the script is fixed.

The proposed schema, to be implemented and reviewed before execution:

| Output | Contract |
|---|---|
| Identity and population | Verify pins, manifests, record identities, unique `(stage,cell,base,arm)` and complete paired sets. Permutation controls are not extra independent base draws. Preserve all eligible base draws; no endpoint/survivor-based exclusion. |
| Contact descriptors | Per arm: `tau_contact`, whole edge set, component-type multiset, slot membership/degree/role, individual slot period and three relative periods. For R/D: both configurations, joint membership categories, equality/difference and strict common-contact condition of §4.2. |
| Times | Per arm and paired R/D: empirical distributions of `tau_contact`, `fe`, `fb`, `t100`; attainment counts at a grid explicitly fixed in the script, with stage/cell observation limits. Never relabel `fe` as contact. |
| Missingness | Distinguish analytically proved no-contact-ever from no recorded event by the horizon, malformed/missing fields, and cap stopping. Do not assign infinity an arbitrary finite value or subtract missing times. Finite-pair differences, if printed, are labelled conditional descriptions with the full-population counts alongside. |
| Joint tables | Only the prelisted cross-tabs: paired endpoint status `(Y_R,Y_D)` against paired contact membership/configuration; endpoint against first-contact star indicator; endpoint against birth attainment by a fixed time. No adaptive bins, outcome-selected subsets, new threshold scans or automatic mechanism verdicts. |
| Controls and output | Existing G4/G5 subset definitions and endpoint/cap rules retained when their quantities are printed. Deterministic output and synthetic negative tests for wrong pins, missing/duplicate records, dropped nonattainers, clock conversion, and swapped pairing keys. Input records remain read-only. |

Each proposed cross-tab is descriptive; distributions conditional on a post-intervention descriptor are not causal mediation estimates. No new multiplicity-controlled discovery family is created. A code or output-specification change after the first look is recorded as an exploratory amendment, not silently backdated.

When an endpoint implies a birth, `P(Y_a)=P(B_a)P(Y_a|B_a)` is an identity but not an identified mediation decomposition. Born runs under R and D generally form different populations. A joint principal-stratum description is possible in a paired simulator but still selects a population and does not isolate late growth. Methodological background retained from r1: P. R. Rosenbaum (1984), “The Consequences of Adjustment for a Concomitant Variable that Has Been Affected by the Treatment,” JRSS A 147(5), 656–666, DOI 10.2307/2981697; publisher abstract previously checked, full proof not read here, not a LIT-validated import.

## 6. Provenance and restart instrument before a fork operator (A4)

### 6.1 Read-only token provenance

Node identity is not token identity after swaps/path rotations. Equal token values are not interchangeable provenance labels. A birth preserves the centre's old token on the newborn and negates it on the centre; the existing census cannot identify a unique carrier or a copied lineage.

First deliverable: a sidecar that observes the **actual** event permutation/copy map without influencing engine execution. Record immutable initial-root identity, distinct copy identity, parent-copy/birth-event link, sign history, and current carrier. Swap transports identities; a path rotation uses the same frozen permutation as the engine; a birth uses the pre-event centre provenance for both branches, preserving their distinction. Handle equal-valued roots, `x=0` and `x=N/2` (where a sign flip is invisible numerically), simultaneous events and stable new-node IDs. Do not reconstruct provenance by value matching alone.

Annotations must not enter interaction decisions, change iteration order, advance random streams, or invoke mutating orientation routines a second time on the live state; the orientation reference increments tie counters. Instrumentation-on/off tests compare full trajectories and state, not merely final `M`. Synthetic acceptance cases cover isolated nodes, swaps, both path orientations, balanced path ties, bound cycles, births/sign copies, repeated equal values and simultaneous components. Birth provenance is a declared bookkeeping convention, not an adopted physical identity claim.

### 6.2 Full checkpoint and deterministic restart

The inspected P1 `bound_symmetric` step/orientation functions use no random draw after initialization. This makes exact no-intervention replay feasible; it does **not** make `deepcopy(Universe)` alone a complete runner checkpoint. `run_state` also holds `alphabet`, `census`, `fe`, `fb`, `t100`, `M_at`, law counters, window accumulators, cap/termination state and the configured clocks outside `Universe`.

Copy all mutable `Universe` fields (including counters and histories), provenance and observer state, and pin engine/orientation/runner/environment. Preserve dictionary/order conventions and the precise boundary: end of the complete tick, not halfway through its frozen event set. Distinguish absolute tick from post-landmark tick; continuation must not silently reset `fb` or historical flags. If post-landmark diagnostics are deliberately reset, define them as new fields and test both raw-state replay and their reset semantics. Check equality of uninterrupted versus clone/restart trajectories and deterministic diagnostics; wall-clock runtime is excluded from equality. Check serialization/restore separately if used.

Acceptance is on bounded synthetic fixtures before campaign use, with no unchanged expensive campaign rerun. The fixture plan and implementation need review; no production lineage replay is authorized here.

### 6.3 Prospective intervention target (operator unresolved)

Generate a reference prefix under a fixed prespecified policy independent of the later R/D assignment. A possible landmark is the end of the first complete birth tick of a BASE prefix, subject to a fixed eligibility horizon. This is a candidate, not a selected landmark. Clone the full checkpoint and apply matched operators `I_R`, `I_D`; continue for fixed post-landmark horizon `H` under identical pinned settings:

    Delta_post = E_{S ~ Q}[g_H(I_R(S)) - g_H(I_D(S))].

Fix `Q`, eligibility/non-birth treatment, landmark, carrier/lineage rule, intervention values, endpoint, cap and horizon before execution. Prefixes without an eligible landmark are counted and reported. Eligibility is before the later assignment, but restricts the target population.

Changing the original node, a current carrier, one newborn, or every descendant are different interventions. Provenance validation is an instrument gate, not permission to select whichever intervention produces the largest effect. Any deliberate boundary change of alphabet/census and any provenance reset must be defined; subsequent engine-law checks use the updated reference and still reject genuine violations.

A nonzero `Delta_post` supports a post-landmark intervention effect in `Q`, not the fraction of S1/S2 mediated by growth; a null/inconclusive result does not prove an early-only mechanism. No borrowing of TDR-26 thresholds, new owner claim or binary exhaustive early-versus-late conclusion.

## 7. Next deliverables and authorization boundary

The four additions are incorporated. Next: co-owner readback of this revision; implement and review the fixed exploratory table script **before** it accesses records; in parallel design/review the read-only provenance and clone/restart instrument on synthetic fixtures. The PI then selects operator, landmark, population and cell. A subsequent preregistration freezes margins, multiplicity, sample size/power assumptions, independent seeds, hashes, gates and cost policy before a separate campaign authorization.

PR #284's entry-note cleanup is accepted as operational continuity. Its contact tests are finite development evidence with the §4.4 coverage qualification; no original evidence is rewritten here. This revision does not itself merge #281/#284.

**Performed in r2:** source/code readback, bounded independent integer checks and explicit synthetic geometric counterexamples, with script and output stored. **Not performed:** new campaign, registered-data aggregation, mechanism table, engine replay, provenance tool execution, canonical-file edit, release tag, adoption, or TDRG numerical-result item. The first-contact arithmetic is a SESSION deduction; the mechanism remains open.
