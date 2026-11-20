# AZ token-resonance fork — BASE-only observation-bound pilot report

**[SESSION] NONCANONICAL · REVIEW CANDIDATE · NOT AN AZ DSN ADOPTION · NO R/D CAMPAIGN.** Prepared by ChatGPT, 20 November 2026, for the Claude AZ co-owner's independent review. This record reports the outcome of the PI-authorised, once-only BASE pilot; it makes no new physical or growth-mechanism claim.

## 0. Decision and scientific boundary

**[NUM][SESSION]** Applying the pilot protocol's previously fixed selection rule to the 500 stored BASE seed records selects **L* = 100** from the permitted grid {100, 200, 400, 800}. All 500 seeds have their first actual tagged-copy BASE graph contact by tick 22, so F(100) = 500/500 = 1. The two BASE-defined C- and C+ fork boundaries are both eligible in all 500 cases under cap C = 300; no boundary has yet attained q = 100.

**[SESSION]** This is an observation-limit calibration, **not** an estimate of any R/D intervention effect. L* = 100 is the **smallest allowed grid point**, not a claim that tick 100 is a dynamically distinguished threshold or that smaller L values were tested as candidates. These pilot seeds must not be reused in a confirmatory R/D campaign. The subsequent campaign's seed law, n/power, analysis, preregistration, and compute remain separate PI decisions.

## 1. Authority, exact source identities and reading extent

- **[OWNER: AZ v0.10 §§4.2, 8]** Governing adopted AZ edition: tag az-v0.10; its TDR-G consumer pin remains tdrg-v2.12.15. The pilot is an AZ-session mechanism-study instrument, not an adopted AZ theorem or NUM diagnostic. No consumer repin is implied.
- **[SESSION / operational authorisation]** Protocol: records/az/AZ_TOKEN_RESONANCE_FORK_BASE_PILOT_PROTOCOL.md §§1–7, and records/az/AZ_TOKEN_RESONANCE_FORK_BASE_PILOT_AUTHORISATION.md §§1–3. PI decision and single-run conditions are recorded there, with a frozen manifest at commit 56cbda76c26099d3a46740695c154f5a2300bf78 and ChatGPT freeze readback 5998649703.
- **[SESSION / source custody]** Uploaded evidence is at upload/az-fork-base-pilot/ from upload commit e52a63502d23aa9e6069fffae41fd1a48a6f885a (PR #344). The protocol/driver was merged through PR #342 (merge commit 379edcfc8169645e7d8e769c0393149e4b0a4d04), and the upload through PR #344 (merge commit a194f42b65d8da981f4876eef66d3e7447fba87d). Each is a two-parent merge commit. The adopted AZ tag is unchanged.
- **[SESSION / reading extent]** Read the complete uploaded manifest, SHA256SUMS, HASHES.txt, summary.json, summary.txt, timing.txt and all 500 JSONL seed records. Read the governing pilot protocol and authorization record in full; used targeted parts of the previously reviewed frozen driver and fork design. Recomputed hashes, tabulations, quantiles, rule selection, summary rows and timing aggregates independently from the stored files. **Did not independently execute the pinned engine or its post-hoc --audit;** the replay and audit results below are source-reported.

**Frozen configuration (manifest SHA-256 H):**

- H = c218cad90e9bfd7d3911a630168aa356e8ff6aad1b448383b4ed27f8a7e44203
- Driver SHA-256 = a91ada53dd6f629cade2b8a2b6addc9b7ad2f5818ae06e023f084c6feb17d0a1
- Tag = AZ-FORK-BASEPILOT-P1, N = 120, k = 8, P1 / bound_symmetric
- Seed indices b = 0,...,499, native four-node BASE draws and independently derived initial-slot choice
- C = 300, q = 100; candidate L grid = {100, 200, 400, 800}
- Threshold = 0.95; wilson_in_rule = false. Wilson intervals are diagnostics, not inputs to L selection.
- Prefix observation maximum Lmax = 800; reference runner Tref = 801, without any R/D arm.

## 2. Prespecified rule and empirical selection

**[SESSION / protocol §4]** For each candidate L, let k(L) be the number of the **500 original seeds** with a recorded BASE first contact tau_C at or before L. The denominator includes every seed, even one with no contact or prior termination:

F(L) = k(L)/500, and L* = min { L in {100,200,400,800} : F(L) >= 0.95 }.

If no L qualifies, the prescribed result is "no qualifying L". Under the frozen manifest the Wilson lower bound **does not alter** this decision.

**[NUM][SESSION]** Independent recomputation from seeds.jsonl reproduces every stored summary row:

| L | k(L)/500 | F(L) | Two-sided 95% Wilson interval | C- eligible | C+ eligible | Both eligible |
|---:|---:|---:|---:|---:|---:|---:|
| 100 | 500/500 | 1.0000 | [0.9924, 1.0000] | 500 | 500 | 500 |
| 200 | 500/500 | 1.0000 | [0.9924, 1.0000] | 500 | 500 | 500 |
| 400 | 500/500 | 1.0000 | [0.9924, 1.0000] | 500 | 500 | 500 |
| 800 | 500/500 | 1.0000 | [0.9924, 1.0000] | 500 | 500 | 500 |

Therefore the rule selects **L* = 100**. Its selection is not affected by C-/C+ eligibility, birth-centre cases, prior threshold attainment or elapsed runtime; these are separately reported diagnostics.

## 3. Contact distribution and additional diagnostics

**[NUM][SESSION]** Exact empirical BASE first-contact distribution (cumulative counts from the 500 rows):

| Tick bound t | Seeds with tau_C <= t | Fraction |
|---:|---:|---:|
| 1 | 173 | 34.6% |
| 2 | 294 | 58.8% |
| 3 | 375 | 75.0% |
| 5 | 458 | 91.6% |
| 7 | 483 | 96.6% |
| 10 | 496 | 99.2% |
| 22 | 500 | 100.0% |

- **[NUM]** Contact statuses: 500 contact, 0 no_contact_by_L, 0 terminated_before_contact. Empirical min = 1, nearest-rank median = 2, p90 = 5, p95 = 7, maximum = 22.
- **[NUM]** For every contact: carrier before the first contact equals the initial slot node j, and M_C- = 4. The tracked-copy carrier at C+ differs from the pre-contact carrier in **473/500** cases; this is identity transport under BASE, not an R/D observation.
- **[NUM]** Both boundaries are eligible for **500/500** seeds; no already-positive boundary M >= 100 was observed. At C+ the node count is 4 in 485 cases and 5 in 15 cases: one birth occurred on the first-contact tick for 15 seeds. Of those 15, **4** are cases where the *tracked slot copy itself* was the birth centre (seed indices 67, 96, 105, 479). This centre-case rate is 4/500 = **0.8%**, with a descriptive two-sided Wilson 95% interval approximately [0.31%, 2.04%].
- **[NUM]** The counterfactual initial free-flight candidate differs from actual dynamic BASE first contact in **125/500 = 25.0%** cases (63 free predictions earlier, 61 later, one undefined). A descriptive two-sided Wilson 95% interval for the 25% fraction is approximately [21.40%, 28.98%]. The free-flight clock must not substitute for tau_C. This is evidence about the contact-clock *representation*, not about a token-resonance growth mechanism.
- **[NUM]** All stored contact-boundary IDs have a 64-hex-character format and all 500 seed indices and initial four-node draws have the required shape. Their **meaning as full engine-state fingerprints** relies on the separately reported replay/audit, not on the present data-only reduction.

**[SESSION]** The 95% Wilson intervals describe model-based binomial sampling uncertainty under the chosen seed-draw law, not a guaranteed physical distribution across other cells or profiles. Zero missing/terminated cases in these 500 draws is not a proof that they never occur.

## 4. Runtime accounting

**[NUM][SESSION]** The 500 rows of timing.txt are in seed order. Their **recorded per-seed times** sum to approximately 2.408 s; mean 4.816 ms, median 4.3 ms, p95 8.3 ms, range 2.7–20.8 ms. Times are rounded to 0.1 ms per seed. This is a sum of instrument-reported per-seed intervals, **not a measured full-process wall clock** including startup, hashing, reporting and upload.

**[SESSION]** These short BASE prefixes (all tau_C <= 22) cannot be used as the computational budget for a future four-arm, H = 800 fork campaign. Such a campaign's cost and power require distinct, authorised planning.

## 5. Custody, verification and independent calculations

**[SESSION / EV-HASH]** Recomputed SHA-256 directly from each UTF-8 file's retrieved contents using an independently implemented SHA-256 routine cross-checked on the standard empty-string and "abc" vectors. Both checksum lists match their referenced files; HASHES.txt also verifies the inner SHA256SUMS file:

| Evidence file | Independently recomputed SHA-256 |
|---|---|
| manifest.json | c218cad90e9bfd7d3911a630168aa356e8ff6aad1b448383b4ed27f8a7e44203 |
| seeds.jsonl | 2417e7c518085943e717216dff0c5b2bd0eb08d92d3da431d2a20485edcd98ed |
| summary.json | 5316e5d6480e1bf6242f925bc263c3b428bcc6ed20702a4fca70329887b034bd |
| summary.txt | f3aed6be4251f67a0480dc1071bc219a177bbb552974b193bd0520b1165c6d9c |
| timing.txt | 4331c29c551a58eff355ab3bfdb537ab15c7da8105fc52934076fd5971996830 |
| SHA256SUMS | e18cdf4ff42311c96c7e825138a596fba190c28491f9146d6a32472a29f95885 |

**[SESSION / EV-INDEP, data reduction only]** Parsed all 500 seed records directly (b = 0,...,499 once each); independently reconstructed all four k(L), F(L), Wilson intervals and eligibility/centre/positive rows from the per-seed values. Recomputed min/median/p90/p95/max tau_C, first-tick and other contact counts, tau_free discrepancy categories, node counts and timing summaries. The recomputed fields match the stored summary.json and summary.txt at their stated precision.

**[SOURCE-REPORTED / EV-RUN]** The PI/Claude handoff reports the PI's server run from freeze commit 56cbda7, then an independent replay on files downloaded back from GitHub with **AUDIT PASS: 0 problem(s)**. Claude also reports that modifying seed 499's M_minus and rewriting SHA256SUMS consistently yielded **AUDIT FAIL** with that seed identified. These demonstrate the source-reported audit's operation but are **not independently rerun by ChatGPT**. The uploaded files are unchanged relative to their hash inventories; the present independent data reduction is narrower than a full engine/oracle replay.

## 6. Scientific interpretation, limitations and negative findings

**[SESSION]** The pilot supplies the intended BASE contact-clock and eligibility distribution for this **specified** N=120, k=8, P1/bound_symmetric reference ensemble. At the selected observation limit 100, **all 500 pilot prefixes are jointly C-/C+ eligible**, and the pre-boundary threshold restriction M < 100 would remove none of these pilot seeds. These are observations, not a universal eligibility statement and not estimates on a future independent campaign's realised cohort.

**[SESSION]** The C-/C+ matched design remains a candidate **prospective experiment**, not yet executed here. An intervention at C- may itself change whether the predicted BASE contact occurs; an intervention at C+ occurs after that BASE contact. C-/C+ effects, if later measured, cannot automatically be interpreted as a mediation share or a proof that the first contact is the unique growth channel. Their horizons are measured from different absolute fork boundaries. Any confirmatory inference, including the two-contrast Holm family and a possible difference-of-differences contrast, requires preregistration.

**[SESSION]** This pilot does **not** identify causal resonance mechanisms, measure R/D effects, validate TDR-G physical dynamics, close AZ-OPEN-PROMO, upgrade AZ Level A or supply a DYAD bridge. The failure of free-flight contact timing in 125 cases supports the previously motivated need to use the actual dynamic graph clock and does not establish a growth law.

## 7. Disposition requested from Claude and subsequent PI decisions

**[SESSION] Recommended review disposition:** accept the **BASE-only pilot report and the rule-based result L* = 100 as a noncanonical session finding**, subject to Claude's independent check of source identities, numerical reductions and the limitations above. This review neither changes an adopted DSN nor authorises a new scientific release.

**[OPEN]** The PI separately determines whether to carry L = 100 into the future fork-campaign preregistration. The next preparatory items remain: (i) a new independent R/D campaign seed derivation and strict separation from the 500 pilot seeds; (ii) common BASE eligibility and the target population for C-/C+ paired comparisons; (iii) sample size and power under a predeclared inferential family; (iv) analysis code; (v) prospective registration, code/custody freeze and explicit campaign compute authorisation. Do not reuse this exploratory pilot as a confirmatory contrast.

**No merge, tag, new run, or adoption is requested by this report draft.**
