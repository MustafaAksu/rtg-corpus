# AZ Action 1 — Stage 2: preregistration and test package

**[SESSION] NONCANONICAL. Draft r1, for review; nothing here is adopted and no campaign is authorised by a review.** Prepared by the AZ co-owner (Claude) on 13 November 2026. Branch `claude/az-tokres-stage2-prereg`. It edits no DSN, closes no pipe item, claims no TDR-G result and authorises no campaign: the PI decides on the confirmatory run after the independent review.

**Authority and what is still the PI's.** PI, 12 Nov 2026, 16:54 +03:00, project conversation, verbatim: "Stage 1 sonucunun `[NUM diagnostic]` olarak bir sonraki sürüme girmesini ve Stage2 çalışmasının başlamasını kabul ediyorum." — Stage 2 starts. The design below follows the joint recommendation of the two co-owners on the three choices of the pilot intake (§7 there): **A3** (both endpoints confirmatory), **B1** (the order hierarchy as a descriptive output only), **C1** (the pilot's thresholds as registered constants). The PI relayed the second co-owner's review `5888182978` on 13 Nov 2026 without a decision text of his own; **no PI decision on A, B, C is recorded.** They are decided when the PI authorises compute for a named commit of this file, or changes them before that. If the PI chooses A1 instead of A3, the analysis script is amended before any run (§12).

Governing sources: AZ `az-v0.8` (file SHA-256 `146fcc28…ee76`); TDR-G `tdrg-v2.12.14` for the engine, the orientation rule and the event definitions the Stage 1 preregistration pinned (a later TDR-G edition does not change the pinned bytes). Stage 1: `records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` (cited as *S1 §n*) and `…_STAGE1_REPORT.md`. Pilot: `…_STAGE2_PILOT_PLAN.md` (*plan §n*) and `…_STAGE2_PILOT_INTAKE.md` (*intake §n*). Every statement about TDR-G dynamics is a proposal to the TDR-G owner; `TDRG-OPEN-SPECCONS-STAR` and TDR-26 stay open and stay TDR-G's (SG-AZ-6).

## 0. What is registered, in one paragraph

On the pinned TDR-G engine with the adopted orientation rule (profile P1), policy `bound_symmetric`, at `N = 240` (`k = 16`), `N = 242` (`k = 16`) and `N = 480` (`k = 32`), runs whose initial state differs in **one token only** — a resonant value (`2x ≡ 0`, or `2x ≡ N/2`) against its neighbour `x ± 1`, same initial phases, same other three tokens — are compared on **two endpoints taken from the same run**: `E_θ = 1{M ≥ θ(N)}` at the horizon `T(N)` fixed by the pilot (`θ, T` = 106, 1460; 84, 1460; 114, 2670), and `E_100 = 1{M ≥ 100 at tick 800}`, the Stage 1 endpoint unchanged. Five contrasts (two orders at `N = 240` and `480`, order 1 at `N = 242`) on two endpoints form **one confirmatory family of ten**. Tests of `RD = 0`: exact McNemar with Holm over the ten. The minimum-effect requirement `RD > 0.05` rests on simultaneous 99.5 % intervals (Bonferroni over the ten). 1,500 base draws per cell, fixed in advance, no interim look; 26,300 runs. Node-label permutation, sham perturbation, detuned comparator and the near-quarter control at `N = 242` are controls with declared margins, separate from the family. The analysis is fail-closed. A supported contrast would establish the causal effect of the token replacement at that `N`, engine, profile, endpoint and horizon — not a mechanism, and not a scaling law.

## 1. Sources and pins

| Object | Path | SHA-256 | State |
|---|---|---|---|
| TDR-G engine | `upload/tdrg-records/genesis_mode_b_mc.py` | `4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608` | as S1 §1; not modified |
| Reference `orient_path` (`TDRG-DEF-ORIENT`, v2.12.14) | `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` | `ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c` | as S1 §1; not modified |
| Runner | `evidence/az/scripts/az_tokres_run.py` | `75c5f139a453a4b2595eba76760e34cddc32c990370259ae6e84ec5379408992` | the Stage 1 runner, **unchanged**; cells and horizon are command-line arguments it already had |
| Fixtures and golden file | `evidence/az/scripts/az_tokres_fixtures.py`, `evidence/az/token_resonance/fixtures/golden.json` | `da9256dc…cb86`, `40eba430…c134` | Stage 1, unchanged; rerun on the campaign machine (gate G1) |
| Stage 1 analysis, used as a library | `evidence/az/scripts/az_tokres_analyse.py` | `490b3d4f06ef52d6d39b217d0821bd8361d0a8ed37941f32f9c154113c91dc80` | unchanged; hash asserted by the Stage 2 analysis before anything else |
| **Stage 2 analysis** (new) | `evidence/az/scripts/az_tokres_s2_analyse.py` | in `stage2/SHA256SUMS` | the registered cells, horizons, thresholds, family and outputs are constants of this file |
| **Stage 2 driver** (new) | `evidence/az/scripts/az_tokres_s2_campaign.py` | in `stage2/SHA256SUMS` | adds no parameter |
| Pilot record files (three) | `upload/az-token-resonance-s2-pilot/N240k16T1460.jsonl`, `N242k16T1460.jsonl`, `N480k32T2670.jsonl` | `f4ab8c57733ee0ed8d60ba62de6672785c954353ab5092f8ab27fd7d56fd86cf`, `baeb4640d7f30f8491f76b2a3309c3e3b44e58374869573b650ade256ae482ec`, `18233c683617d81bfb3f81e7f1b9c7e3d176c2f41a6cdffd9943ada23304c877` | by the PI, commit `5fb65fb` (custody PR #259); read by the registered analysis for one descriptive supplement (§6.6 D5) |

`evidence/az/token_resonance/stage2/SHA256SUMS` lists the package (scripts, pins, validation outputs); its own SHA-256 is given in the PR that carries the registered commit and, at authorisation, in the server block. Profile P1 only: Stage 2 has no cell under the superseded orientation rule (P2); Stage 1 covered that sensitivity at `N = 120` and it is not repeated.

## 2. What is taken from Stage 1 without change

The event inventory, Propositions 1–3 and their limits (S1 §2); the native law, the base draw and the arms `BASE, O1R, O1D, O2R, O2D, SHAM` (`4 | N`) or `BASE, O1R, O1D, Q2R, SHAM` (`N ≡ 2 mod 4`), with `BASE_P`, `O1R_P` on the first 200 base draws (S1 §5); the per-tick law check and what it does and does not cover (S1 §2); the minimal effect `δ* = 0.05` and the neutrality margin `δ_neutral = 0.025`; the paired design, the exact McNemar test, the Agresti–Min interval; the integrity layers and the gates G1, G2 (S1 §6.5); the outcome rule confirmed by the PI on 12 Nov 2026 (Stage 1 report §11 item 3). `k/N = 1/15` as in Stage 1.

**Stage 1 result, for reference only** (not re-tested, not pooled): PC1 `+0.2427 [+0.2166, +0.2681]`, PC2 `+0.1613 [+0.1381, +0.1841]` at `N = 120`; PC3 `+0.2193 [+0.1944, +0.2436]` at `N = 122`; near-quarter control equivalent within ±0.05; 0 law violations in 19,900 runs.

## 3. The pilot, and one amendment made after it

**What the pilot fixed (intake §3–§4).** Native draws only, 3,000 per cell, tag `S2-CALIB-PILOT-20261112`. Reference rate `α = 14/2620 = 0.00534` (exact 95 % `[0.00292, 0.00895]`). By the horizon rule of plan §4 and the stop rule of plan §8 item 2, applied without change:

| Cell | `N` | `k` | `T` | `θ` | band (intake §5) |
|---|---|---|---|---|---|
| S2-C240 | 240 | 16 | 1460 | 106 | 92, 127 |
| S2-C242 | 242 | 16 | 1460 (documented exception: the rule gives 1470) | 84 | 78, 98 |
| S2-C480 | 480 | 32 | 2670 | 114 | 104, 131 |

**These are registered constants. They are frozen.** No output of the campaign changes them (§6.6 D4). The acceptance rule they passed is a check of discrete feasibility on the sample they were chosen on; it is not evidence that they reproduce the rate `α` out of sample (intake §5). The exponent used to pick the scaled horizons is the owner's fit for another profile and horizon; it served to choose a second horizon to calibrate and no scaling law is claimed (plan §8 item 8).

**Post-pilot amendment of plan §4 — recorded as such.** Plan §4 fixed, before the pilot, one primary endpoint (`E_θ`) and the Stage 1 endpoint as a secondary without a decision rule. This registration makes **both** confirmatory. The reason is an exploratory, post hoc look at the pilot's **non-resonant** draws (intake §6): the baseline to which `θ` is matched is carried by draws with a seed token of low additive order of `2x`, whose share depends on the arithmetic of `N` (none exists at `N = 242`), so that equal baseline rates do not make the endpoint comparable across `N`; and at `T = 800` the median of the non-resonant distribution is 39–40 at all four `N`, with `M ≥ 100` in 3 of 8,522 draws without a low-order token. The amendment is an addition (the pre-committed endpoint stays confirmatory), it was made before any outcome of an exposed draw at these `N` was tabulated by either co-owner from the pilot files (§7 states what the test configuration showed), and it was accepted conditionally by review `5888182978`, the condition being the multiplicity contract of §6.2. It is not a rule that was fixed before the pilot, and the report will say so.

## 4. Hypotheses

For a cell, an order and an endpoint `e`, let `RD_e` be the risk of `e` when one uniformly chosen node's token is set to a resonant value of that order, minus the risk when it is set to that value's neighbour `±1` (sign random), everything else native (S1 §4).

- **H(240, 1), H(240, 2), H(242, 1), H(480, 1), H(480, 2)**, each on `E_θ` and on `E_100`: `RD_e ≥ δ* = 0.05`.
- **Near-quarter control (`N = 242`).** Setting a token to one of the four values nearest `N/4`, `3N/4` (60, 61, 181, 182; none has order 2) leaves the risk within `±δ*` of the native risk, on each endpoint.

Not separated by this design, as in Stage 1: whether the resonant token acts during growth or through the time and manner of the first contact and first birth. Not tested: any dependence of the effect on `N` (§6.7).

## 5. Design

**Cells and sizes (all fixed before any run).**

| Cell | `N` | `k` | `T` | Base draws | Arms | Runs |
|---|---|---|---|---|---|---|
| S2-C240 | 240 | 16 | 1460 | 0–1499 | BASE, O1R, O1D, O2R, O2D, SHAM; BASE_P and O1R_P for base draws 0–199 | 9,400 |
| S2-C242 | 242 | 16 | 1460 | 0–1499 | BASE, O1R, O1D, Q2R, SHAM | 7,500 |
| S2-C480 | 480 | 32 | 2670 | 0–1499 | BASE, O1R, O1D, O2R, O2D, SHAM; BASE_P and O1R_P for base draws 0–199 | 9,400 |

26,300 runs. Common: profile P1; policy `bound_symmetric`; stop at `M ≥ 300`; four initial nodes; the runner's checkpoints at ticks 100, …, 800 (so that `E_100` is read from the same run); the per-tick law check on; the birth-anchored collection on, as in Stage 1 (it is not analysed at Stage 2).

**Seeds.** Tag `AZ-TOKRES-S2`; base draw `b` from `sha256("AZ-TOKRES-S2|N<N>|k<k>|base|<b>")`, the arm stream from `…|arm|<b>` (S1 §5). No draw is shared with Stage 1 (`AZ-TOKRES-S1`), the pilot (`S2-CALIB-PILOT-20261112`), the timing probe of 12 Nov (`S2-TIMING-PROBE`) or the test configuration (`S2SMOKE`); those tags are spent. The tag `AZ-TOKRES-S2` has not been run: the runner refuses registered tags without `--confirmatory`.

**Sample size and power.** 1,500 pairs per contrast, as in Stage 1, so that intervals at the different `N` have comparable width. Operating characteristics of the reading rule of §6.2 at this size, for one contrast of the family (`stage2/power_table_output.txt`; arms taken as independent within a pair; Holm replaced by its Bonferroni bound, so the *supported* rates are lower bounds):

| Assumed risks (resonant, detuned) | true RD | supported | not supported | inconclusive |
|---|---|---|---|---|
| Stage 1 values (0.258, 0.015), (0.185, 0.024), (0.231, 0.011) | 0.243, 0.161, 0.220 | 1.000 | 0 | 0 |
| (0.12, 0.02) | 0.10 | 0.997 | 0 | 0.003 |
| (0.10, 0.02); half of the Stage 1 order-2 effect (0.105, 0.024) | 0.08 | 0.76 | 0 | 0.24 |
| (0.09, 0.02) | 0.07 | 0.34 | 0 | 0.66 |
| (0.08, 0.02) | 0.06 | 0.05 | 0 | 0.95 |
| (0.05, 0.02) | 0.03 | 0 | 0.57 | 0.43 |
| (0.04, 0.02) | 0.02 | 0 | 0.97 | 0.03 |
| equal risks (0.02 or 0.005) | 0 | 0 | 1.000 | 0 |

An effect as large as in Stage 1 is supported with near certainty; half of it is supported in about three runs of four; a true difference between about 0.03 and 0.08 will most probably read *inconclusive*, and will be reported so.

**Stopping, censoring, exclusions.** The campaign stops when every registered `(base, arm)` record exists. There is no interim analysis: the driver runs the analysis once, after the last cell, and the record files are not opened before `CAMPAIGN_COMPLETE.json` exists (record counts may be looked at). Both endpoints are defined for every run (§6.1); nothing is censored. No run is excluded on its outcome. A run that raises an error is rerun from the same seed; if the error is deterministic the base draw is removed from all arms of its cell with `--exclude-base CELL:b`, which the analysis prints as a deviation and attaches as a qualifier to every reading of that cell.

**Amendments.** Any change to §§3–6 before data exist is made in this file by a commit and listed in §12. A change after confirmatory data exist is a deviation and is labelled as such in the report.

## 6. Analysis plan

Implemented by `evidence/az/scripts/az_tokres_s2_analyse.py`, one invocation over the three cells; its output is reported verbatim. The registered parameters are constants of that script (`REGISTRY`, `CONTRASTS`), not command-line arguments.

### 6.1 Endpoints

`M_t` never decreases (S1 Proposition 1), so both are well defined for every run.

- **`E_θ`**: `Y = 1{M ≥ θ(N)}` with `M` the node count when the run stops — at tick `T(N)`, or at the cap of 300 (then `Y = 1`).
- **`E_100`**: `Y = 1{M ≥ 100 at tick 800}`, read from the runner's checkpoint at tick 800. A run that reached the cap **before** tick 800 has no such checkpoint; it had at least 300 nodes before tick 800 and is **positive**. Such runs are not excluded; their number is reported per arm (D9). The analysis refuses (integrity) a record without the checkpoint that did not reach the cap before tick 800.

On one run the two can differ in two ways: `E_100 = 0, E_θ = 1` when the run passes `θ` only after tick 800; `E_100 = 1, E_θ = 0` when it has at least 100 nodes at tick 800 and ends below `θ` (possible only where `θ > 100`, i.e. at `N = 240` and `480`).

### 6.2 The confirmatory family, and the multiplicity contract

**The family** is exactly these ten, in this order; nothing else is confirmatory:

| | S2-C240 `O1R` vs `O1D` | S2-C240 `O2R` vs `O2D` | S2-C242 `O1R` vs `O1D` | S2-C480 `O1R` vs `O1D` | S2-C480 `O2R` vs `O2D` |
|---|---|---|---|---|---|
| `E_θ` | 1 | 2 | 3 | 4 | 5 |
| `E_100` | 6 | 7 | 8 | 9 | 10 |

Each is paired on the base draw; estimate `RD = (b − c)/n` from the discordant counts.

**Two requirements, two procedures** (review `5888182978`: Holm on the tests of `RD = 0` gives no bound for `RD > δ*`):

1. *Existence of a difference.* Exact two-sided McNemar test on the discordant pairs; **Holm** adjustment over the ten at family level 0.05. This procedure involves no approximation.
2. *Minimum effect.* **Simultaneous** two-sided intervals for `RD`: Agresti–Min adjusted Wald interval for matched proportions at level `1 − 0.05/10 = 99.5 %` each (normal quantile 2.8070). By Bonferroni the ten intervals cover their ten true values jointly with probability at least 95 %, **to the accuracy of the interval's normal approximation** — this part is approximate, unlike the McNemar test. At the registered size, in two boundary scenarios with `RD = δ*` exactly, the simulated probability that the lower limit exceeds `δ*` is 0.0016 and 0.0012 (400,000 repetitions each; nominal 0.0025), so the rule is not anti-conservative there; the probability that the upper limit falls below `δ*` is 0.0035 and 0.0048, above the nominal 0.0025 — the interval is shifted slightly towards zero, which bears on the *not supported* reading and not on a claim of effect (`power_table_output.txt`). The simultaneous intervals are wider than five-contrast intervals by the ratio of normal quantiles 2.807/2.576 ≈ 1.09; that is a property of the Bonferroni intervals, not of Holm.

**Registered reading, per contrast and endpoint.** *Supported*: Holm `p < 0.05` **and** simultaneous lower limit `> δ*`. *Not supported at the registered size*: simultaneous upper limit `< δ*`. Otherwise *inconclusive* — not a refutation; reported as insufficient resolution. The familywise guarantee attached to "at least `δ*`" is that of procedure 2; procedure 1 is an additional condition and never a substitute.

**Reading the two endpoints of one contrast together** (a description of the pattern, not a further test):

| `E_θ` | `E_100` | Stated as |
|---|---|---|
| supported | supported | the contrast is present at this `N` on both endpoints |
| supported | not supported or inconclusive | present at the scaled horizon with the calibrated threshold; not shown on the Stage 1 endpoint at tick 800 |
| not supported or inconclusive | supported | present on the Stage 1 endpoint; not shown at the scaled horizon with the calibrated threshold |
| neither supported | | not shown at this `N` at the registered size, with the two readings as printed |

Every reading is printed with its qualifiers (§6.4).

### 6.3 Near-quarter control at `N = 242` — separate from the family

`Q2R` against `BASE`, on each endpoint: Agresti–Min interval at 99.5 % two-sided; *equivalent* if the interval lies inside `(−δ*, +δ*)`, *different* if it lies entirely beyond `±δ*`, otherwise *inconclusive*. It is an equivalence statement and is not one of the ten superiority tests; its two intervals at 99.5 % are more conservative than a Bonferroni split over its two statements (97.5 %) would require. If the family is supported at `N = 242` and this control reads *different*, the report says that the order-1 effect at `N = 242` is not specific to resonant values.

### 6.4 Gates and qualifiers

**Integrity (any failure: errors listed, no estimate, no reading, exit code 2).** The Stage 1 library hashes to its pin; engine, orientation reference and runner hash to their pins; per cell, the five Stage 1 layers — identity, custody, states (independent re-derivation of every initial state), records, set — with the Stage 2 cell parameters; the tick-800 checkpoint rule of §6.1; the three pilot files hash to the registered values and every pilot record has the pilot's identity, pins and a class label equal to a re-derivation from its seed tokens.

**Gates (a failed gate: no estimate, no reading, exit code 3).** G1: the fixtures log produced on the campaign machine shows the pinned bytes, no failed test, and ends with `FIXTURES PASS`. G2: the law-violation counter summed over all campaign runs and the three pilot files is zero; a non-zero value contradicts S1 Proposition 1 for this engine and is reported to TDR-G.

**Qualifiers (per cell and per endpoint; attached to the readings of that cell and endpoint).** As in S1 §6.5: Agresti–Min intervals at 95 % two-sided, neutrality margin `±0.025`, readings *equivalent* / *different* / *inconclusive*; an interval that contains zero is never by itself read as neutrality.
- **G3 node labels** (S2-C240, S2-C480): *pass* iff no permuted run differs from its unpermuted run in `(M, births, steps, fb, M_at)`.
- **G4 sham**: `SHAM` against `BASE` on base draws whose native and perturbed slot token are both non-resonant.
- **G5 detuned comparator, per contrast**: `O1D` (resp. `O2D`) against `BASE` on base draws whose native slot token is non-resonant.
- A reading is **unqualified** only if G3 passes (where it exists) and G4 and its G5 read *equivalent*; otherwise it is *qualified by* the failing or inconclusive control and may be stated only as "resonant value against its `±1` neighbour". Qualifiers do not turn one registered reading into another.
- **Multiplicity of the controls.** The control intervals are nominal 95 % each and are not adjusted. They are not claims of the campaign; each one qualifies the readings of its own cell and endpoint only, and its error rate is to be read per control. Expected resolution if the controls are neutral: about 1,450–1,480 eligible pairs, half-width below about 0.011.

### 6.5 What is fixed and may not be re-chosen

The thresholds `θ`, the horizons, the band thresholds, the tick of `E_100` and its threshold of 100, the sample size, the family and its order, the margins, the quantile 2.8070. In particular **the out-of-sample check D4 is report-only**: whatever it shows, no threshold is re-selected, no cell is dropped and no reading is changed on Stage 2 data.

### 6.6 Descriptive outputs (nominal 95 %; no reading, no decision)

- **D1** the five contrasts at the two band thresholds of each cell (intake §5).
- **D2** threshold ladder: rate of `M ≥ c`, `c ∈ {60, 80, 100, 150, 200, 300}`, by arm, at the end of the run and at tick 800.
- **D3** threshold-free paired comparison of `M` between the resonant and the detuned arm, at the end of the run and at tick 800: counts greater / smaller / equal, exact sign test, median difference (`M` is capped at 300).
- **D4** out-of-sample check of the calibration: among `BASE` draws without a resonant seed token, the count and rate of `M ≥ θ` with the exact 95 % interval, next to the pilot's `α` and its interval; and the same for `M ≥ 100` at tick 800. With about 1,400 such draws per cell it rests on about seven expected exceedances and can show only a miscalibration by a factor of roughly two to three or more.
- **D5** native decomposition `P(Y) = p0 + P(R)·(p1 − p0)`, per cell and endpoint, **from native (`BASE`) draws only** — `R`: at least one seed token with `4x ≡ 0`; `p0`, `p1` the conditional risks of native draws without and with such a token. The risks of the intervention arms are never substituted into it. With about 100, 50 and 50 exposed `BASE` draws it is coarse; as a supplement the analysis reads the pilot's native draws at the same `N`, horizon and threshold (204, 87 and 94 exposed draws; other seeds) and prints the pilot's `p1` and the pooled `p1`. `θ` was chosen on the pilot's non-resonant draws, so the pilot's `p0` is in-sample and is labelled so; the choice did not use the exposed draws. **This is the first tabulation of the outcomes of the pilot's exposed draws**; it happens inside the registered analysis, after the campaign.
- **D6** `BASE` draws without a resonant seed token, by the smallest additive order of `2x` among the four seed tokens (orders up to 12 separately; the cut "≤ 6 / > 6"), positives on both endpoints. Exploratory: the classification and the cut were chosen post hoc on the pilot (intake §6.1). At `N = 242` `ord(2x) ∈ {1, 11, 121}`, so the low-order class is empty by arithmetic. No mechanism is claimed and no arm tests it (choice B1).
- **D7** resonant arms by value (`0` / `N/2`; `N/4` / `3N/4`; the four near-quarter values). **D8** the contrasts on pairs whose three other seed tokens are non-resonant. **D9** runs that reached the cap, by arm: all, and before tick 800. **D10** mean run time by arm.
- Not produced at Stage 2: the largest-class share, the TDR-26 birth-anchored cross-tabulation and the first-birth medians of Stage 1 (S7, S8, S10). The runner still collects their inputs.

### 6.7 What a result would and would not mean

Each contrast estimates the **total causal effect, on the stated endpoint, of replacing one initial token by a resonant value rather than by its `±1` neighbour**, under the native law of all other coordinates, for this engine, profile, `N`, `k`, horizon and threshold. A supported contrast is a `[NUM]`-type statement of exactly that, at that `N`.

It is **not**: a mechanism (the first-contact mechanism stays open, S1 §6.6); a scaling law or an `N`-dependence of the effect — no trend across `N` is tested, and the report tabulates the estimates at `N = 120, 122, 240, 242, 480` without a reading; a statement that `E_θ` is "the same event" at different `N` (equal baseline rates of populations whose native-token mixture differs with `N` do not make it so; effect sizes do not transport across `N` for that reason either); a statement about the TDR-26 basin, other policies or `k/N`; a bridge observable (OPEN-P1 untouched); or anything related to AZ's Hashimoto `4 | q` rule or to Dyadic/DZT `q = 4` beyond the numeral (SG-AZ-7, SG-DZT-1). Under the PI's outcome rule a validated, supported contrast is *eligible* for a PI-approved `[NUM diagnostic]` entry in AZ Level A with its exact scope, is offered to TDR-G for owner disposition, and by itself closes no `AZ-OPEN-PROMO`, promotes no maturity and is no TDR-G claim.

## 7. Instrument validation — what was executed, and what was not

Executed in the session of 13 Nov 2026 (Python 3.13.18; outputs under `evidence/az/token_resonance/stage2/`, hashes in `SHA256SUMS`):

| Check | Result | Output |
|---|---|---|
| Stage 2 analysis self-test: pins and margins equal Stage 1's; the quantile; registry against the intake's values; seed independence of the four tags; both endpoints on synthetic runs, including a run capped before tick 800 and one capped at tick 800; record checks; exact interval of `14/2620` equal to the reviewer's independent value `[0.0029243, 0.0089493]`; orders of `2x`; the three readings; Holm over ten; the pilot loader (accept, wrong hash, missing pins, contradicting label, missing file) | 35 checks, PASS | `selftest_output.txt` |
| Test campaign, plan `s2test` (tag `S2SMOKE`; `N = 240, 242, 480`; `T = 900`; 10, 8, 6 base draws; 144 runs; stand-in threshold 45): driver end to end — self-test, Stage 1 fixtures, runner, shard checks, analysis, hashes, marker | `CAMPAIGN COMPLETE`; integrity PASS, G1 PASS, G2 0 violations | `test_campaign/`, `test_campaign_driver_output.txt` |
| Negative controls on copies of the test campaign: changed `M`; file changed after the run; a cell missing; records of another cell or another horizon; tick-800 checkpoint removed; a law violation; fixtures log not passing; a record missing; Stage 1 library changed; registered plan without pilot directory; stand-in pilot files read and reported, then a contradicting label and a missing file; four driver refusals, the last showing that the registered plan stops before any run when the pilot files are not the registered ones | 20 controls, each refused (or accepted) as stated; nothing estimated in a refused case | `negcontrols_output.txt` |
| The three real pilot files: hashes and record structure | as registered; 204 / 87 / 94 records with a resonant seed token | `pilot_check_output.txt` |
| Operating characteristics of the reading rule | §5, §6.2 | `power_table_output.txt` |

**Not executed, and why.** The registered analysis has not been run on the real pilot files: that would tabulate the outcomes of exposed pilot draws before the campaign. Their path through the analysis was exercised with stand-in files made from the test campaign's own `BASE` records (negative controls NC12–NC14), and the real files were checked for hashes and structure only — a check that evaluates no outcome and prints only counts by class label. The tag `AZ-TOKRES-S2` has not been run.

**What the test configuration showed, disclosed.** The test campaign ran all arms at the Stage 2 `N` on 10, 8 and 6 base draws of a separate tag, and its analysis output — rates by arm on those few draws — is in the package and was seen by this lane. It has no evidential value, is not pooled with anything, and every registered constant was fixed in the script before it was run. The timing probe of 12 Nov (tag `S2-TIMING-PROBE`; all arms on 3–6 base draws per cell; plan §6) was read for wall time and the native arm's `M` only. As in the pilot intake, the restriction this lane can state is that **no outcome or token value of an exposed draw of the pilot or of the registered tag has been tabulated**; it is not perfect blinding (run times are an outcome proxy; intake §2).

## 8. Exact commands

From the repository root.

**Verification of this package (reviewer; about two minutes):**
```bash
S=evidence/az/scripts; P=evidence/az/token_resonance/stage2
sha256sum -c --quiet $P/SHA256SUMS && echo "package bytes OK"
python3 -I $S/az_tokres_s2_analyse.py --selftest --analysis-s1 $S/az_tokres_analyse.py              # must end: SELFTEST PASS
python3 -I $S/az_tokres_s2_campaign.py --plan s2test --jobs 2 --out /tmp/az_s2_test                 # must end: CAMPAIGN COMPLETE
python3 -I $S/az_tokres_s2_negcontrols.py --campaign /tmp/az_s2_test --work /tmp/az_s2_negcontrols  # must end: NEGCONTROLS PASS
diff <(grep -v -e SHA-256 /tmp/az_s2_test/analysis_s2test.txt | grep -v '^D10\|^      T2-.*  BASE [0-9.]* ') \
     <(grep -v -e SHA-256 $P/test_campaign/analysis_s2test.txt | grep -v '^D10\|^      T2-.*  BASE [0-9.]* ')
```
The test-campaign records are reproducible in every field except `secs`; the analysis output is reproducible except for the SHA-256 lines of the record files and the run-time lines of D10. The pilot check (`--check-pilot upload/az-token-resonance-s2-pilot`) can be repeated once PR #259 is merged or from the upload branch; it prints counts by class label only.

**Stage 2 campaign (only after the PI's authorisation, for the commit the PI names).** One command; the driver checks the self-test and the pilot files first, then runs the fixtures, the three cells and the analysis, checks every exit code and every shard, and writes `CAMPAIGN_COMPLETE.json` only if all of it succeeded. Venue: the PI's Ubuntu server (one core: `--jobs 1`). The block below is the form; the block issued at authorisation carries the commit and the SHA-256 of `SHA256SUMS`.
```bash
cat > ~/az_tokres_stage2.sh <<'AZ_STAGE2'
set -euo pipefail
REPO="$HOME/rtg-corpus"; WT="$HOME/az_tokres_s2_wt"; OUT="$HOME/az_tokres_stage2"; PILOT="$HOME/az_tokres_s2_pilot"
COMMIT="<the commit named in the PI's authorisation>"; SUMS="<SHA-256 of stage2/SHA256SUMS at that commit>"
git -C "$REPO" fetch -q origin
test -d "$WT" || git -C "$REPO" worktree add -q --detach "$WT" "$COMMIT"
cd "$WT"
git checkout -q --detach "$COMMIT"
test -z "$(git status --porcelain)" || { echo "STOP: worktree not clean"; exit 1; }
git log --oneline -1; python3 --version; nproc
test "$(sha256sum evidence/az/token_resonance/stage2/SHA256SUMS | cut -d' ' -f1)" = "$SUMS" || { echo "STOP: not the registered package"; exit 1; }
sha256sum -c --quiet evidence/az/token_resonance/stage2/SHA256SUMS
echo "package bytes OK"
if ! test -f "$PILOT/N480k32T2670.jsonl"; then          # the pilot output as uploaded, if the original directory is gone
  PILOT="$HOME/az_tokres_s2_pilot_from_git"; mkdir -p "$PILOT"
  ( git archive origin/main upload/az-token-resonance-s2-pilot 2>/dev/null || git archive origin/upload/az-token-resonance-s2-pilot upload/az-token-resonance-s2-pilot ) | tar -x -C "$PILOT" --strip-components=2
fi
python3 -I evidence/az/scripts/az_tokres_s2_campaign.py --plan stage2 --jobs 1 --out "$OUT" --pilot-dir "$PILOT" --confirmatory ${AZ_RESUME:+--resume}
test -f "$OUT/CAMPAIGN_COMPLETE.json"
( cd "$OUT" && sha256sum -c --quiet HASHES.txt )
echo "campaign hashes OK"
cat "$OUT/CAMPAIGN_COMPLETE.json"
git checkout -q -b upload/az-token-resonance-stage2 origin/main
mkdir -p upload/az-token-resonance-stage2
cp -r "$OUT"/. upload/az-token-resonance-stage2/
git add upload/az-token-resonance-stage2
git commit -q -m "upload: AZ token-resonance Stage 2 campaign output, unchanged"
git push -q -u origin upload/az-token-resonance-stage2
echo "UPLOADED: upload/az-token-resonance-stage2 at $(git rev-parse --short HEAD)"
AZ_STAGE2
setsid nohup bash ~/az_tokres_stage2.sh >> ~/az_tokres_stage2.out 2>&1 < /dev/null &
```
Progress: `tail -n 5 ~/az_tokres_stage2.out`; record counts with `wc -l ~/az_tokres_stage2/*.jsonl` (expected 9,400 / 7,500 / 9,400). If the run is interrupted: the same last line with `AZ_RESUME=1 ` in front of `setsid`. If the driver ends with `CAMPAIGN FAILED`, nothing is uploaded and `~/az_tokres_stage2/CAMPAIGN_FAILED.txt` names the step.

**Cost.** From the pilot's native run times on that server (0.68, 0.50, 1.33 s) and the Stage 1 ratio of all arms to the native arm (1.65; 1.18 at `N ≡ 2 mod 4`): about 10 hours if the arms behave as at `N = 120`, about 6 with no effect. Twice that is a planning heuristic for an upper value, not a guaranteed cap (intake §8).

## 9. Evidence manifest

`evidence/az/token_resonance/stage2/SHA256SUMS` (repository-relative paths; `sha256sum -c` from the root): the three new scripts; the six pinned Stage 1 files; `selftest_output.txt`; `test_campaign/` (records, manifests, logs, fixtures log, analysis, `HASHES.txt`, marker); `test_campaign_driver_output.txt`; `negcontrols_output.txt`; `pilot_check_output.txt`; `power_table.py` and `power_table_output.txt`. The pilot's evidence is under `evidence/az/token_resonance/stage2_pilot/` and `upload/az-token-resonance-s2-pilot/` (PR #259).

## 10. Obligations carried, and where they are met

| Source | Obligation | Here |
|---|---|---|
| plan §8, 1 | target `α`, realised rate at `θ`, difference, exact intervals | intake §3; D4 for the campaign's own draws |
| plan §8, 2 | `θ ≤ 200` and realised rate inside the interval of `α`, else fallback, else not registered | intake §4: all three cells valid at the scaled horizon |
| plan §8, 3 | equal baseline exceedance is not the same event; Stage 1 endpoint kept in parallel | §3, §6.7; `E_100` is confirmatory |
| plan §8, 4 | decomposition from the native arm only | D5 |
| plan §8, 5 | one family, multiplicity, power, three readings | §6.2, §5 |
| plan §8, 6 | cap before tick 800: positive, counted | §6.1, D9 |
| plan §8, 7 | horizon of `N = 242` documented | §3 |
| plan §8, 8 | the exponent claims no scaling law | §3, §6.7 |
| plan §8, 9 | exposed pilot outcomes unread before the design is fixed | §7; first tabulation in D5, after the campaign |
| review `5888182978`, A | five contrasts per endpoint, family of ten, Holm, three readings; near-quarter and gates separate, their multiplicity stated; a valid simultaneous bound for the minimum effect, its approximation status distinguished from the exact test; A3 recorded as a post-pilot amendment | §6.2, §6.3, §6.4, §3 |
| review `5888182978`, B | order association descriptive; no order-3/4 arms | D6, §6.7 |
| review `5888182978`, C | `θ` and horizons frozen; bands and out-of-sample estimates reported unconditionally, no adaptation; band-limit outcomes without decisions; cap-before-800 rule | §3, §6.5, D1, D4, §6.1 |
| review `5888182978`, (iv) | sample size, independent seed tag, full hashes, five contrasts, baseline-composition reports, all gate rules fixed before execution | §5, §1, §6.2, D5–D6, §6.4 |

## 11. Dependencies and firewalls

The engine and the orientation reference are TDR-G's; whether P1 is the profile TDR-G wants for new campaigns remains a TDR-G decision (S1 §11); the offer `pipes/TDRG/20261112-AZ-token-alphabet-law-offer.md` is acknowledged without disposition. Stage 3 (TDR-26 in its own scope) waits for TDR-G. This registration needs nothing from another stream. OPEN-P1 firewall, SG-PROG-1/2/4, SG-AZ-1…7 and SG-DZT-1 apply unchanged. AZ v0.9 (PR #253) is independent of Stage 2 and is not changed by it.

## 12. Review record and amendment log

| Date | Event |
|---|---|
| 13 Nov 2026 | Draft r1. Package validated as in §7. Submitted for independent review. |

**If the PI chooses A1 instead of A3:** the family becomes the five `E_θ` contrasts (rows 1–5 of §6.2), the simultaneous level becomes `1 − 0.05/5 = 99 %` (quantile 2.5758), `E_100` becomes a descriptive output without a reading; the change is two constants and one loop in the analysis script, made and re-validated before any run and listed here. **If the multiplicity contract of §6.2 is found wanting in review**, the same fallback applies (review `5888182978`).
