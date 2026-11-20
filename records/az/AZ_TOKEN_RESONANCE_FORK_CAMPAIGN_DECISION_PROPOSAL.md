# AZ token-resonance fork campaign — decision proposal for L, new seeds and common eligible population

**[SESSION] NONCANONICAL · DRAFT FOR CLAUDE REVIEW · PI_PENDING · NOT PREREGISTERED · NO COMPUTE AUTHORISATION.** ChatGPT scientific proposal, 21 November 2026. This is a **decision precursor**, not a registration, a frozen study plan or an AZ owner-science statement. Claude AZ co-owner reviews; PI retains authority for choices and scientific adoption.

## 0. Source identity, scope, and reading

- **[OWNER: AZ v0.10 §4.2.1–4.2.2 and §8]** Governing adopted AZ scientific source: Git tag az-v0.10, dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md; AZ remains Level A; the two earlier registered diagnostics are not a verified mechanism, scaling statement or DYAD bridge. Its TDR-G consumer pin remains tdrg-v2.12.15. Only the relevant owner sections were inspected for this proposal, not the full owner DSN or its computational campaigns.
- **[SESSION / operational design]** records/az/AZ_TOKEN_RESONANCE_FORK_DESIGN.md r2, §§1–7 (merged PR #322, design Gate D PASS 5960841961); the Gate I.1 contact clock and Gate I.2 operator are synthetic engineering tools, not a confirmatory experiment.
- **[SESSION / pilot]** records/az/AZ_TOKEN_RESONANCE_FORK_BASE_PILOT_PROTOCOL.md §§1–7; records/az/AZ_TOKEN_RESONANCE_FORK_BASE_PILOT_AUTHORISATION.md §§1–3; records/az/AZ_TOKEN_RESONANCE_FORK_BASE_PILOT_REPORT.md §§0–7 (ChatGPT report PR #346, Claude review 5999283212 PASS SCOPED on head 7680af2). Uploaded pilot evidence: upload/az-fork-base-pilot/ at upload commit e52a635, merged PR #344. All 500 stored BASE records and checksums were independently reduced by ChatGPT for the report; the full pinned-engine replay was reported by Claude, not rerun by ChatGPT.
- **[SESSION / seed-law interface]** Frozen runner evidence/az/scripts/az_tokres_run.py at az-v0.10, targeted functions derive_int, base_draw, arm_choices, arm_state. The native draw and arm/slot draw use distinct SHA-256-derived streams.

Only the first **three** preparation decisions below are proposed. Sample size/power, test code, a final analysis family, preregistration, custody and any new campaign compute authorisation are explicitly **not** settled here.

## 1. Decision P1 — observation bound L = 100 (proposed)

**[NUM][SESSION]** The once-only 500-seed **BASE-only** pilot selected L* = 100 by its PI-approved fixed rule over {100, 200, 400, 800}: 500/500 actual first slot-copy BASE graph contacts occurred by tick 22; the lower 95% Wilson bound for F(100)=1 is ~0.99238, but the selection used the empirical F, not this bound. Both C- and C+ were eligible in 500/500 pilot seeds.

**[HEUR][SESSION] Recommendation:** carry **L = 100** into the later campaign's preregistration **as an observation cutoff**, not as a dynamic constant. The campaign will use its own independent seed sample; the fraction making contact by L can be below 100%. Under the pinned four-node engine assumptions of §3, C-/C+ eligibility conditional on contact by L is structurally guaranteed; do not extrapolate the pilot's 500/500 contact frequency. Do **not** reuse pilot seeds, alter L on observing new R/D outcomes, or silently choose a larger L if the future sample has nonattainers. If no contact by L or the BASE prefix terminates first, record that outcome and the distinct reason.

**[OPEN]** PI must separately approve carrying L = 100 forward. The report's Claude PASS and this proposal do not themselves constitute that approval.

## 2. Decision P2 — campaign seed generation (proposed; no seed draw run)

**[HEUR][SESSION] Candidate tag:** AZ-FORK-CONFIRM-C1-P1 (not yet reserved, registered or approved; validate uniqueness against old S1/S2 registered tags, the BASE pilot tag AZ-FORK-BASEPILOT-P1 and all synthetic tags before freezing).

Use the unmodified, frozen P1 runner's exact laws for each preassigned integer index b in **0..n_total-1** (n_total **PI_PENDING** until power analysis):

- base_seed_b = derive_int(tag, "N120", "k8", "base", b)
- arm_seed_b = derive_int(tag, "N120", "k8", "arm", b)
- theta0_b, delta0_b = base_draw(engine, tag, 120, 8, b); initial node count 4.
- choices_b = arm_choices(tag, 120, 8, b); (j_b, r_b, epsilon_b) = (choices_b["slot"], choices_b["r1"], choices_b["s1"]). Here j is uniform among four root nodes, r in {0,60}, epsilon in {-1,+1}.
- R writes x_R=r_b and D writes x_D=(r_b+epsilon_b) mod 120 **absolutely** to the current physical carrier of original slot copy c_j, only at their selected BASE fork boundary. The R/D alternatives use identical pre-fork phases, other tokens, identity and reference event time.

**[SESSION]** The hash-derived streams are reproducible *pseudorandom* draws under a declared computational generator, not a theorem asserting probabilistic independence of deterministic outputs. The same b may be used for R/D/C-/C+ within this **one campaign** (that is the paired design); the initial seed streams must be disjoint from prior pilot and registered experiment streams.

**Freeze-time acceptance gates (not yet implemented):**
1. The exact tag, n_total, index range, random derivation, code hashes, profile, cell and seed/arm stream separation are fixed **before** any new campaign outputs.
2. Compare the derived base/arm seed identifiers against all known registered and pilot identifiers at the same cell (and within the new sample); reject any exact collisions rather than relying only on different tag strings. Record the comparison scope and explicit noncovered external uses. A repeated physical state by chance is different from reuse of an identical seed identifier.
3. Persist a deterministic manifest of every b, seed-derivation identity and intended cell/profile; verify b=0..n_total-1 exactly, with no silent replacement of missing/ineligible seeds. Never use Stage 1/Stage 2 or BASE pilot outcomes as new confirmatory R/D units.
4. Avoid registering, producing or reading any new R/D outcome before the PI separately approves the preregistration and campaign compute.

**[OPEN]** The PI must approve a new final tag and sampling rule, after the source-focused Claude review and before freeze. The sample size cannot be inferred from 500 pilot seeds, which contain **no R/D binary outcome pairs**.

## 3. Decision P3 — a single, common BASE-defined eligibility population (proposed)

For a new campaign seed z_b, run a **single unmodified BASE prefix** and determine the first actual tagged-copy graph-contact time tau_C,b with the verified contact clock. Define s_-(b)=tau_C,b−1, s_+(b)=tau_C,b. At either boundary use the same originally chosen slot j_b, O1 draw (r_b,epsilon_b), and the same BASE event tau_C,b. Do not let realised R/D contacts define the sample.

Let:
A_-(b) = {tau_C,b exists, tau_C,b <= L, C- boundary exists and is eligible: done=False, iters<T_ref, M<C}.
A_+(b) = {tau_C,b exists, tau_C,b <= L, C+ boundary exists and is eligible: done=False, iters<T_ref, M<C}.
A_both(b)=A_-(b) ∩ A_+(b).

**[HEUR][SESSION] Primary proposed population:** Q_both = the induced law of (BASE prefix, original j, O1 draw, tau_C), **conditional on A_both**. Use this exact same pre-intervention cohort for both paired contrasts. Do not retain extra C--only seeds in one confirmatory contrast, because doing so would change the estimand population between C- and C+.

At each eligible seed define paired binary outcomes from H=800 **additional** ticks at the respective boundary and node cap C=300, q=100:
D_-(b) = Y_R^-(b) − Y_D^-(b),  D_+(b) = Y_R^+(b) − Y_D^+(b).
Proposed estimands, for the same Q_both:
Delta_- = E[D_- | A_both],  Delta_+ = E[D_+ | A_both].

**[SESSION]** A common seed population does not make the physical fork states identical: C- occurs before the BASE contact, and the C- assignment can change whether contact takes place; C+ follows the completed BASE contact. Because each H is measured from its own fork boundary, absolute endpoint times also differ by one tick. A contrast between Delta_- and Delta_+ does **not** isolate a mediator or validate a growth mechanism.

**[ALG][SESSION] Conditional structural lemma for this specific pinned cell (Claude S1; independently source-checked).** Assume native four-node initialisation M0=4, an original tagged root slot, the pinned P1 / `bound_symmetric` engine with graph-contact clock, a positive cap C>=6, q>=6 and T_ref=L+1; all engine/sidecar operations are valid. Then, as **events on the original BASE seed space**,

`A_-(b) = A_+(b) = A_both(b) = {tau_C,b is defined and tau_C,b <= L}`.

Further, `M_C-=4`, `M_C+ in {4,5}` and `M_C-/M_C+ < q`. **Proof:** before the tagged root's first incident graph edge it has not taken part in an event. With only four original nodes, the other three cannot contain a star centre (the pinned `star_centers` requires at least three mutually nonadjacent neighbours). Thus no pre-contact birth can occur, although swaps and paths among those three nodes can change their phase/token history. At the contact tick the graph still has four pre-tick nodes: at most one valid four-node star component can give one birth; no node is deleted. Hence M at the two boundaries is 4 and at most 5. Both boundary clock values are strictly below T_ref for tau_C<=L; neither can reach cap C>=6, and neither already meets q>=6. Therefore both are eligible exactly for the same reference-contact seeds. In a bounded exact combinatorial cross-check, all 64 labelled simple graphs on four nodes were enumerated: no graph with the tagged slot isolated has a valid star centre, and no graph has more than one valid star centre. This is a **conditional engine-model deduction**, not physical validation or an adopted owner theorem.

**Critical interpretation:** equality of the *conditioning events/seed cohorts* does **not** imply `Q_-=Q_+` as **state-valued distributions**: `S^0_{tau_C-1}` and `S^0_{tau_C}` differ in their BASE histories, tokens and absolute ticks. The proposed common seed measure ensures comparable paired estimands without identifying a mediation decomposition. The equality would need re-derivation for a different initial node count, engine, profile, clock or cap.

**Predeclared missingness and audit obligations:**
- Retain every b in the total-source ledger. Report the number with no actual BASE contact by L and the number with both boundaries eligible. Retain pre-contact termination, C- ineligible, C+ ineligible, exactly-one-eligible and M_s>=q as **zero-required structural invariant checks** for the pinned cell, *not* categories for discretionary exclusion. A nonzero such invariant is an instrument/source mismatch and stops the run for Gate I review, rather than changing the estimand denominator.
- **R1 — fail-closed integrity:** any provenance, checkpoint, graph/replay, seed-identity, source-pin or ledger validation failure indicates a malfunctioning instrument and **MUST immediately stop the entire campaign**. Quarantine any incomplete output and return to Gate I review; do **not** resume that campaign, count the fault as a seed outcome/missingness category, replace a seed or selectively drop it. Log the engineering incident separately from the outcome/eligibility ledger; future runs require a new explicit approval after correction.
- **No post-treatment exclusions** or rerandomization/replacement for realised R/D contact, birth, growth, cap stop, no-op assignment, or failed attainment. A no-op remains a legitimate assigned intervention epoch.
- Keep already-positive M_s>=q seeds **included and flagged** (as selected in the earlier design). Since q=100 and C=300, a valid cap stop cannot be a censored negative endpoint. Report BASE reference as secondary only.
- Under the pinned four-node lemma the jointly eligible count equals the contact-by-L count. If that count is below the preregistered power requirement, report the shortfall and invoke a **predeclared** decision rule; do not add seeds adaptively or silently change to separate cohorts.

**[OPEN]** PI must approve the target estimands and the choice to use the same contact-by-L BASE seed cohort at both landmarks. For the pinned cell the three eligibility events coincide by the conditional lemma, so there is no substantive separate-versus-common *seed-selection* choice; however the C- and C+ **boundary-state laws and their effect estimands remain distinct**. The pilot's 500/500 contact-by-L frequency is not a guarantee for future independent seeds.

## 4. Next independent obligations (not decisions of this proposal)

**[OPEN]** Obtain the PI's dispositions for P1–P3; fix whether the **two tests** for Delta_-, Delta_+ use the previously suggested Holm family and their null/alternative, effect threshold, confidence intervals and stopping criteria. A descriptive on-common-cohort Gamma=E[D_-−D_+] may be reported, but a confirmatory test of Gamma would need its own prospective family specification and error control.

**[OPEN]** Sample size/power must be derived for the **paired** R/D binary outcomes, explicitly accounting for within-seed discordance and the possible common-eligibility fraction. S1/S2 effect sizes are at different timing estimands and cannot silently be reused as power estimates; the BASE pilot has no intervention effect or discordance information. Power analysis may present a sensitivity grid and predeclared conservative bound, not a retrospective choice based on campaign outcomes.

**[OPEN]** A separate code-and-analysis PR, exact-hash freeze, campaign preregistration, PI approval and compute authorisation are required before any new campaign run. Do not merge this proposal as a scientific adoption or treat a PASS as an authorisation to compute.

## 5. Claude review request

Review status: Claude co-owner review `5999451703` gave PASS / ACCEPT SCOPED subject to R1. This successor corrects R1 as a **stop-and-return-to-Gate-I** integrity gate and incorporates Claude's suggested S1 with the seed-event versus state-distribution distinction. Check (a) the exact fail-closed wording, (b) conditional four-node structural proof and its limitations, (c) source/pin and seed-law accuracy, and (d) that P1–P3 remain PI_PENDING and no campaign permission is implied. Return a **change-focused** review with concrete counterexamples or a scoped PASS. No registered data need be opened and no large computations should be run to review this decision proposal.
