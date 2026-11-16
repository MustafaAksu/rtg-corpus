# AZ token resonance — mechanism design

**[SESSION] NONCANONICAL — design proposal, not a preregistration, result, or compute authorization.** Prepared by ChatGPT, 16 November 2026. Scientific authority remains the adopted owner DSNs. No canonical file, frozen evidence, or registered campaign parameter is changed.

## 1. Decision and question

The PI wrote in the immediately preceding project-conversation message: “brinci öneri ile devam edebiliriz” (proceed with the first proposal). The first proposal was the mechanism question: does the seed-token effect arise during early contact/first birth, during subsequent growth, or both? The decision was receipted in PR #279 review `5920431601`. It selects the research direction; it does not approve the operators, sample size, endpoints or execution of a new campaign. Orders 3/4 and TDR-26 Stage 3 are not selected here.

AZ v0.10 is adopted: tag `az-v0.10`, merge `062a1728d8b98aa026c751ecc77d45026538a8ca`, DSN SHA-256 `0cc84c9a587bab270624a824d5e004a327f20f41f0c03307e01a6725afe80e6e`. Its release record §8 excludes a mechanism claim and any new campaign. The two adopted diagnostics remain separate, at their existing scopes and grades; Level A and AZ-OPEN-PROMO are unchanged. No separate TDRG numerical-result item is to be filed.

**Maintenance checkpoint:** PR #279 was reviewed and merged as `2d898fdafedee7f5b3d4628fe0c08ef2871a8b0c`. The edition notices are queued, not accepted by their recipients. The entry note's earlier “No next study is decided” is superseded by the PI selection above; its responsible lane should link this design at its next update. This document is a scientific design record, not a replacement orientation note.

## 2. Sources and reading extent

| Source | Identity and extent |
|---|---|
| AZ owner | `az-v0.10`, §§4.2.1–4.2.2 and guards inspected in the preceding release reviews; tagged release record §§6–8 and current BASELINE checked again in this session. Not a new full-DSN reading. |
| TDR-G context | Existing AZ pin `tdrg-v2.12.15`. Live query found no `tdrg-v2.13` tag. Owner candidate PR #265 and Atlas row-check #277 are not adopted authority. No automatic repin is proposed. |
| Runner | `evidence/az/scripts/az_tokres_run.py` at `74ad6946e9710a2272b9d7792d6d8f0c45cda168`: module contract, pins, seed/arm construction, `run_state`, output fields and `keep_final` inspected. Recorded runner SHA-256 `75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992`; not rehashed here. |
| Engine | `upload/tdrg-records/genesis_mode_b_mc.py` at the same commit: geometry/edge predicate, `Universe`, initialization, interaction functions and `step_universe` inspected (targeted lines 1–145, 480–870). Recorded SHA-256 `4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608`; not rehashed or executed here. |
| Registration | Stage 2 r2 at the same commit, §§6.1–6.7, previously inspected; its fixed endpoints and control restrictions are not changed. |
| Governance | Current CONVENTIONS §§1–7 read; Methodology v1.4 §§12–13.5 were read in the preceding review. |

This session inspected sources and derived the bookkeeping relation below. It did not read/reaggregate the campaign payload, run the engine, execute a replay, or produce a mechanism estimate. The P1 orientation reference is inherited from the registered package; it was not re-audited here. The first-contact derivation below stops before any orientation-dependent interaction.

## 3. Separate the clocks before testing a mechanism

[SESSION] Use three distinct events:

- `tau_contact`: first processed tick whose **post-advance, pre-interaction** defect graph has any edge. Tick zero is not a processed contact in this definition.
- `tau_event`: the existing runner field `fe`. Its actual predicate is the first nonzero cumulative counter among single-edge swaps, path interactions, births, multistars seen, or path ties seen. It is not defined as the first nonempty defect graph; for example the predicate does not include the bound-cycle counter.
- `tau_birth`: the existing runner field `fb`, recorded after the first tick with positive birth increment. It is distinct from both preceding clocks. The engine's internal `birth_steps_list` is written before `u.steps` is incremented; do not substitute that list for runner `fb` without an explicit clock conversion.

The runner also records `t100` and `M_at` at fixed ticks. Its returned summary does not provide a complete state at the first birth. `keep_final` supplies final phase/token dictionaries only. A valid fork requires a new, checked checkpoint/replay instrument, not a fabricated intermediate state from these summaries.

## 4. Exact early-contact instrument: a bounded derivation, not a mechanism result

[SESSION — exact deduction from the inspected update order; no novelty or owner grade claimed.] Before the first defect edge, all components are isolated, so interactions leave the tokens unchanged. For an initial state with even N, integer 0 <= k < N/6, and four nodes,

    theta_i(t) = theta_i(0) + t delta_i(0)  (mod N)

holds through the pre-interaction snapshot of the first contact. Let

    a_ij = theta_i(0) - theta_j(0) - N/2,
    b_ij = delta_i(0) - delta_j(0).

Then the first processed contact is exactly

    tau_contact = min { t >= 1 : a_ij + t b_ij = e (mod N)
                                  for some i<j and integer e in [-k,k] },

with min(empty) = infinity. Proof: while the set is empty at all earlier ticks, the inspected engine advances freely and the isolated-component branch performs no interaction; at its first nonempty tick the displayed predicate is exactly the engine's defect test.

Each congruence can be solved without a growth simulation. With g = gcd(N,b_ij), it is solvable iff g divides e-a_ij. For L=N/g > 1, solve

    t = ((e-a_ij)/g) * inverse(b_ij/g modulo L)  (mod L),

and replace residue zero by L to obtain the first positive time. If b_ij=0 modulo N, the pair is either in the band at every processed tick (first time 1) or never in it; handle this case explicitly. Minimize over the six pairs and the band residues. The free-flight graph repeats after N ticks, so a first contact, if any, occurs within ticks 1..N. If none occurs in that interval, this initial state stays birth-free under the inspected engine.

For a one-slot intervention, the three pairs not involving that slot have unchanged free-flight contact candidates. Thus `tau_contact = min(tau_common, tau_slot)` for each arm. This can distinguish whether a changed slot can affect the **first global contact**. It does not predict later contacts after any interaction, first-birth probability, or tail growth. In particular, a pairwise free-flight time after the first global contact is not the actual later contact time of that pair.

**Instrument acceptance, before using it:** exact synthetic checks against a direct modular scan for zero advance, no solution, multiple band residues, t=N, initial edges at t=0, and simultaneous first contacts; then a bounded engine replay checking the first pre-interaction graph. None of these tests has been executed in this draft.

## 5. First analysis: existing records, explicitly exploratory

[SESSION — proposed.] Start with a fixed table specification, not outcome-driven searches. Use all paired base draws for the two registered order contrasts in an initial candidate cell `(N,k)=(120,8)`; any extension to other cells is listed before analysis. This cell choice is a proposal, not a PI-approved new design.

Tabulate the empirical paired distributions of `tau_contact`, `fe`, `fb`, and `t100`, and event/non-event counts by a fixed grid. The new contact field is computed by the exact instrument after validation. Never relabel `fe` as contact. Preserve runs with no event by the observation horizon as nonattainment/censoring; do not silently remove them or assign an arbitrary finite event time. Outcomes are already known in the existing campaigns, so these are secondary exploratory analyses, not new confirmatory tests.

The identity `P(Y_a)=P(B_a) P(Y_a|B_a)` holds when Y implies a birth, but its factors are not an identified causal mediation decomposition. Comparing only the born runs under R with only the born runs under D generally selects different populations. Since the simulator can provide both paired arm outcomes, a joint principal-stratum description is possible; it still targets a selected population and does not isolate a late-growth mechanism.

Methodological background, not a new RTG claim: P. R. Rosenbaum (1984), “The Consequences of Adjustment for a Concomitant Variable that Has Been Affected by the Treatment,” JRSS Series A 147(5), 656–666, DOI 10.2307/2981697. The publisher's abstract was checked; its full proof was not read here. This is not a LIT-validated import and no confidential source is used.

## 6. Prospective causal test: common-prefix state forks

[SESSION — design candidate only.] For a late-intervention question, generate a reference prefix under a **fixed, prespecified policy independent of the later R/D assignment**. One possible landmark is the end of the first complete birth tick of a BASE prefix, subject to a fixed eligibility horizon. Clone the complete state at that boundary and assign matched R/D interventions to the clones; continue under identical engine/profile/policy settings.

For reference state S, intervention operators I_R and I_D, fixed post-landmark horizon H and prespecified outcome g_H, the target is

    Delta_post = E_{S ~ Q}[ g_H(I_R(S)) - g_H(I_D(S)) ].

Q, the landmark, eligible population, and non-birth rule must be fixed in advance. Prefixes without a birth by the eligibility horizon are counted and reported; conditioning on this reference-prefix event is prior to the later assignment, but limits the target to those eligible histories.

A nonzero Delta_post supports a post-landmark intervention effect in Q. It does **not** measure the fraction of the original S1/S2 effect mediated by growth and does not by itself refute an early-contact contribution. Both stages may contribute. Conversely, a null or inconclusive fork result does not prove an early-only mechanism.

**Unresolved operator gate:** specify which carrier(s) are changed. Node identity is not token identity after swaps/path rotations; a birth creates a copied/sign-flipped token. Changing the original node, a current carrier, a newborn, and an entire descendant lineage are different interventions. Record which signed-alphabet or census change is deliberately introduced at the intervention boundary; ordinary engine law checks then use the explicitly updated reference state. Do not count an intended intervention as an unexplained law violation, or silently exempt subsequent genuine violations.

Require: full-state clone/restart equality without intervention; instrumentation-on/off equality; phase/gauge and label-map checks; precise advance/interaction/birth boundary; no outcome-based state selection; fixed post-landmark horizon rather than treatment-dependent remaining global time; no borrowing of TDR-26 thresholds or scientific interpretation. With mutable objects, deep-copy all state fields, not just phase/token dictionaries. No new simulation or checkpoint reconstruction is authorized by this note.

## 7. Deliverables and authorization boundary

Next deliverable is a co-owner-reviewed design: clock definitions, exact contact-instrument specification and tests, exploratory table contract, then one chosen fork operator/landmark/population. A later preregistration must freeze endpoints, margins, multiplicity, sample size/power assumptions, independent seeds, pins, gates, and cost policy before a campaign is requested. The two-stage timing question must not be framed as an exhaustive binary mechanism test.

**Not performed:** no new campaign, data aggregation, engine modification, TDRG numerical-result notice, canonical scientific change, release tag, or adoption. This document is proposed for review; the PI has selected the subject, not adopted its mathematical deductions or experimental details.
