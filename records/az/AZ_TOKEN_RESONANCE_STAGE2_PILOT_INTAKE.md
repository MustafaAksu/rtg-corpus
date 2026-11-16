# AZ Action 1 — Stage 2 pilot: intake and calibration evaluation

**[SESSION] NONCANONICAL, EXPLORATORY. Not a registration, not a confirmatory result, no claim about token resonance at any `N`.** Prepared by the AZ co-owner (Claude), 13 November 2026. Plan and review record: `records/az/AZ_TOKEN_RESONANCE_STAGE2_PILOT_PLAN.md` (PR #251). Nothing here is adopted; the confirmatory Stage 2 campaign is not authorised.

## 1. What arrived

| Item | Fact | Source |
|---|---|---|
| Run | the PI's Ubuntu server, pilot script at commit `a6d50adb852b30e1dc520d2a54e680ea95d98c6a` (SHA-256 `ccc9e776…9a95`), plan `pilot`, tag `S2-CALIB-PILOT-20261112`; finished 12 Nov 2026 17:07:26Z; 10,977 s in the invocation that completed it; Python 3.12.3 | `PILOT_COMPLETE.json` |
| Upload | branch `upload/az-token-resonance-s2-pilot`, commit `5fb65fb6e15a44f973c9314bc004171809a02976` by the PI (12 Nov 2026 17:07:27Z), one commit on `main` `2de679b`; 11 files, 17,134,921 bytes, under `upload/az-token-resonance-s2-pilot/` | GitHub; PI's terminal output in the project conversation (13 Nov 10:38 +03:00) |
| Files | seven record files of 3,000 records each (21,000 native runs), `MANIFEST.jsonl`, `PILOT_COMPLETE.json`, `summary.txt`, `HASHES.txt` (SHA-256 `a463a197327888c11b46a121217fff51beff634b5c16271ec16f2f1af16cc1cd`) | upload commit |

## 2. Custody checks (`EV-BYTES`, `EV-HASH`, `EV-RUN`)

`evidence/az/token_resonance/stage2_pilot/intake_check.py` (SHA-256 `cc94d9bbefae94cb1b92f63080cb964089d1d9c6f07e0e5a19b399cfefa23a98`), run on a clean checkout of the upload commit; output `intake_output.txt` (SHA-256 `04c750d38352a9496ecdb120e93875dcee08e9aa2e7e0ac3f82fd5cc3be2bbb4`), exit code 0, `RESULT: PASS`:

- `HASHES.txt` lists ten files and every one has its listed hash; the manifest, the completion marker and the files agree on the seven record-file hashes; the marker carries the manifest's hash;
- every one of the 21,000 records carries its cell's identity (`N`, `k`, `T`, cap 300, profile P1, policy `bound_symmetric`, arm `BASE`, tag) and the four pinned hashes of `stage2_pilot/SHA256SUMS` (engine `4c94d874…a608`, orientation reference `ca59e9b9…d59c`, runner `75c5f139…8992`, pilot script `ccc9e776…9a95`); records are complete and in the order of the draw index; the law-violation counter is 0 in every record;
- the stored `summary.txt` equals, byte for byte, a rerun of the pilot script's `summary` on the uploaded files.

**What was read, and what was not.** Review `5875885484` item 9 limits this lane's intake to the hash check, the stored summary and its rerun. The intake script reads, in addition and for every record, the identity fields, the draw index, the law-violation counter and the run time; it reads the outcome fields (`M`, `hit_cap`) and the seed tokens **only** for native draws without a resonant seed token (`native_class == "NR"`), and `t100`, `births` and `M_at` for no record. No outcome value and no token value of a draw that carries a resonant token was read, tabulated or printed in this intake, by the script or otherwise. **This is a restriction on what was tabulated, not perfect blinding:** the run time of a run is a proxy for its outcome (a run that grows large takes longer), and two aggregates over all draws — total run time and the longest run per cell — were already in the stored summary and are repeated in §8 (review `5888182978`, safeguard ii).

## 3. Calibration table (non-resonant native draws only)

Reference cell `N = 120, k = 8, T = 800`: 14 of 2,620 non-resonant draws have `M ≥ 100`. **`α = 0.00534`, exact 95 % interval `[0.00292, 0.00895]`.** (The plan expected `α` near 1 %; it is about half that.) No non-resonant draw of the reference cell ends between 91 and 99, so "smallest `m`" gives 91 there; the reference endpoint is `M ≥ 100` by definition and the two coincide on this sample.

| Cell | `n_NR` | `θ` | exceed `θ` | realised rate | exact 95 % of realised | realised − `α` | inside interval of `α` | `θ ≤ 200` |
|---|---|---|---|---|---|---|---|---|
| N120 k8 T800 | 2,620 | 91 (≡ 100) | 14 | 0.00534 | [0.00292, 0.00895] | 0 | yes | yes |
| N240 k16 T800 | 2,796 | 80 | 13 | 0.00465 | [0.00248, 0.00794] | −0.00069 | yes | yes |
| N240 k16 T1460 | 2,796 | 106 | 14 | 0.00501 | [0.00274, 0.00839] | −0.00034 | yes | yes |
| N242 k16 T800 | 2,913 | 64 | 15 | 0.00515 | [0.00288, 0.00848] | −0.00019 | yes | yes |
| N242 k16 T1460 | 2,913 | 84 | 15 | 0.00515 | [0.00288, 0.00848] | −0.00019 | yes | yes |
| N480 k32 T800 | 2,906 | 70 | 14 | 0.00482 | [0.00264, 0.00807] | −0.00053 | yes | yes |
| N480 k32 T2670 | 2,906 | 114 | 15 | 0.00516 | [0.00289, 0.00850] | −0.00018 | yes | yes |

In every cell the largest non-resonant value below `θ` is `θ − 1`: the integer step at the threshold is one unit, and no cell has an atom there.

## 4. Evaluation against the rules fixed before the pilot

Plan §4 (horizon rule) and §8 item 2 (stop rule), applied without change:

| `N` | horizon | `θ` | stop rule | result |
|---|---|---|---|---|
| 240 | scaled, `T = 1460` | **106** | `θ ≤ 200`; realised rate inside the interval of `α` | valid |
| 242 | `T = 1460` (the documented exception of plan §2) | **84** | as above | valid |
| 480 | scaled, `T = 2670` | **114** | as above | valid |

No cell falls back to `T = 800`; no calibration failed. By the rules as written, the calibration is valid and these are the values a registration would carry.

## 5. What that validity does and does not show

**The check of §4 is an in-sample check.** `θ` is chosen on the same draws on which its realised rate is then compared with `α`; the rate can only fall short of `α` by the size of an integer step. The rule therefore tests what review item 1 asked for — that discreteness does not spoil the match — and that is all it tests. It says nothing about how firmly 2,600–2,900 draws fix a quantile that about 14 of them exceed. Two checks that are not automatic:

| Cell | `θ` | `θ` if `α` were at the upper / lower end of its interval | split by parity of the draw index: `θ` from one half → exceedances in the other half |
|---|---|---|---|
| N120 k8 T800 | 91 | 78 / 129 | 86 → 9 of 1,291 (0.0070); 110 → 5 of 1,329 (0.0038) |
| N240 k16 T1460 | 106 | 92 / 127 | 119 → 3 of 1,411 (0.0021); 103 → 10 of 1,385 (0.0072) |
| N242 k16 T1460 | 84 | 78 / 98 | 83 → 9 of 1,459 (0.0062); 92 → 5 of 1,454 (0.0034) |
| N480 k32 T2670 | 114 | 104 / 131 | 122 → 4 of 1,455 (0.0027); 114 → 8 of 1,451 (0.0055) |

(`T = 800` cells in `intake_output.txt`.) Reading: within the uncertainty of `α` alone the selected thresholds move by 6–14 nodes downwards and 14–21 upwards. A threshold fixed on one half of the draws gives, in the other half, rates between 0.0021 and 0.0072 in the three selected cells (0.0014 to 0.0076 over all seven cells): of the fourteen half-sample rates four lie below the lower end of the interval of `α` (two of them in selected cells: 3 of 1,411 at `N = 240`, 4 of 1,455 at `N = 480`) and none above its upper end. The half-sample exercise uses half the draws and so overstates the uncertainty of the full-sample thresholds, by a factor of roughly √2. This lane's reading: the registered thresholds should be expected to give an out-of-sample baseline within roughly a factor of two of 0.5 %, not equal to it. Nothing here indicates a failed calibration; it is the precision of the calibration, and the registration has to carry it.

## 6. Two findings in the non-resonant draws that bear on the design (exploratory, post hoc)

Both were looked for after the calibration table was seen, because the thresholds of `N = 240` and `N = 242` differ (106 against 84) at the same `k` and `T`. They use non-resonant native draws only. The classification below and its cut were chosen after the fact; the `p`-values are descriptions, not tests.

### 6.1 The baseline the threshold is matched to is not a homogeneous background

For a seed token `x`, let `ord(2x)` be the additive order of `2x` in `ℤ_N` — the number of ticks after which the free parent–child separation of preregistration Proposition 2 returns to `N/2`. Orders 1 and 2 are the two resonant classes of Stage 1; a non-resonant draw has every order ≥ 3. Draws are classified by the **smallest** order among their four seed tokens.

| Cell (threshold) | smallest order ≤ 6 | every order > 6 | Fisher exact, two-sided |
|---|---|---|---|
| N120 k8 T800 (`M ≥ 100`) | 14 of 1,419 | **0 of 1,201** | 2.0·10⁻⁴ |
| N240 k16 T1460 (`θ = 106`) | 11 of 828 | 3 of 1,968 | 2.1·10⁻⁴ |
| N242 k16 T1460 (`θ = 84`) | no such token exists (`ord(2x) ∈ {1, 11, 121}`) | 15 of 2,913 | — |
| N480 k32 T2670 (`θ = 114`) | 6 of 466 | 9 of 2,440 | 0.023 |

In the reference cell all 14 baseline events are draws that contain a token of order 3 (8 of 343), 4 (4 of 329), 5 (1 of 537) or 6 (1 of 210); none of the 1,201 draws without such a token reaches 100 (largest `M`: 85). Full tables by order in `intake_output.txt`.

Reading, with its limits. (i) The reference rate `α` is not the rate of a featureless background: on this sample it is carried entirely by draws with a low-order token. This looks like a graded continuation of the Stage 1 pattern (order 1: 0.258, order 2: 0.185 in the intervention arms; orders 3 and 4: about 0.02 and 0.01 in native draws here) — **a hypothesis formed on these data, not a result.** (ii) The share of non-resonant draws that contain a token of order ≤ 6 depends on the arithmetic of `N`: 54 % at `N = 120`, 30 % at 240, none at 242, 16 % at 480. A threshold matched to `α` therefore equates rates of populations of different composition. This is review item 3 ("equal baseline exceedance is not the same dynamical event") in concrete form. (iii) The `N = 240` / `N = 242` difference is consistent with such a composition effect — which is not a shown cause and not a tested mechanism: `M ≥ 100` at `T = 1460` in 18 of 2,796 against 8 of 2,913 (Fisher `p = 0.048`), and at `T = 800` in 8 against 1 (`p = 0.019`) — two overlapping post hoc comparisons, unadjusted; among draws with every order > 6 the counts at `N = 240` are 4 of 1,968 and 1 of 1,968, against 8 and 1 of 2,913 at `N = 242`. (iv) None of this touches the Stage 1 contrasts: the detuned neighbours `r ± 1` have large order, and the three other tokens are native in both arms of a pair.

### 6.2 At `T = 800` the centre of the non-resonant distribution does not move with `N` in this range

| | N = 120 | N = 240 | N = 242 | N = 480 |
|---|---|---|---|---|
| all non-resonant draws, `T = 800`: median / 90 % / 99 % of `M` | 40 / 51 / 76 | 39 / 48 / 70 | 39 / 46 / 59 | 39 / 46 / 64 |
| draws with every order > 6, `T = 800`: median / 90 % / 99 % / 99.5 % / max | 39 / 50 / 62 / 71 / 85 | 39 / 47 / 61 / 68 / 101 | 39 / 46 / 59 / 65 / 104 | 39 / 46 / 63 / 68 / 105 |
| the same draws with `M ≥ 100` at `T = 800` | 0 of 1,201 | 1 of 1,968 | 1 of 2,913 | 1 of 2,440 |

The pilot plan expected the bulk at fixed `T` to fall with `N` (the owner's bulk birth-rate scaling, which review item 8 had already limited to its own profile and horizon). In this profile, at `k/N = 1/15` and `T = 800`, the median is 39–40 at all four `N` and the listed upper quantiles are close. That is what these samples show; it is not a proof that the whole distribution, or its tail, is independent of `N` (review `5888182978`, safeguard i). On these samples the Stage 1 endpoint `M ≥ 100` at `T = 800` meets an almost empty background at every `N` of Stage 2 — three draws of 8,522 among draws without a low-order token. It is the scaled horizons that lift the bulk towards 100 (99.5 % of `M` among those draws: 89, 85 and 107 at the three scaled horizons). Whether *tails* need the longer horizon at larger `N` is not answered by non-resonant draws; one weak indication that they may: draws with a token of order ≤ 6 reach 100 by `T = 800` in 14 of 1,419 at `N = 120` and 1 of 466 at `N = 480`, and in 10 of 466 at `N = 480` by `T = 2670`.

## 7. What this means for the registration — choices for review and the PI

**Unaffected by any of the choices.** The campaign runs each cell once, to its scaled horizon, with the checkpoint at tick 800: both endpoints come from the same runs at the same cost. Thresholds are registered constants. A paired contrast at one `N` compares two arms at one fixed threshold and is a valid test of a difference between them whatever the threshold; calibration error and the composition effect of §6.1 do not bias it. They affect only how an endpoint compares *across* `N`.

**Choice A — which endpoint carries the confirmatory readings.** The plan (§4) fixed in advance: primary `M ≥ θ(N)` at the scaled horizon, the Stage 1 endpoint as a secondary. That rule was applied in §4 above and stands unless the PI changes it. §6 weakens its rationale (the matched baseline is not one population) and strengthens the Stage 1 endpoint's (identical definition; background almost empty on these samples at every `N`).

| | Confirmatory | Secondary | For | Against |
|---|---|---|---|---|
| A1 | `M ≥ θ(N)`, scaled horizon (five contrasts) | `M ≥ 100`, `T = 800` | the rule fixed before the pilot, unchanged | its comparability across `N` rests on a baseline of changing composition, and on thresholds known to ±10–20 nodes |
| A2 | `M ≥ 100`, `T = 800` (five contrasts) | `M ≥ θ(N)`, scaled horizon | the Stage 1 endpoint itself; no calibrated constant in a confirmatory reading | departs from the rule fixed in advance; if tails are slower at large `N`, the confirmatory reading could miss an effect that the secondary shows |
| A3 | both (ten contrasts, one family, Holm) | — | keeps the pre-committed endpoint confirmatory and adds the Stage 1 endpoint on equal terms; every pattern (both, only one) has a registered reading | simultaneous intervals for ten contrasts are wider than for five: by Bonferroni and the normal approximation the ratio of quantiles is 2.807 / 2.576 ≈ 1.09. This is a statement about Bonferroni intervals, not about Holm: Holm on the McNemar `p`-values controls the tests of `RD = 0` and gives no bound for `RD > δ*` (review `5888182978`) |

This lane recommends **A3**. It is a **post-pilot amendment of plan §4**, motivated by an exploratory look at non-resonant pilot draws — not a rule fixed before the pilot — and has to be recorded as such in the registration. It is an addition, made before any outcome of an exposed draw has been read by anyone; it is the reviewer's and the PI's to accept or refuse; A1 remains available without any new work, and is the fallback if the multiplicity rule for ten contrasts cannot be set up validly.

**Choice B — the order hierarchy of §6.1.** B1: no new arm; the registration adds one descriptive output — the native (`BASE`) arm by smallest order — and names the hypothesis as untested. B2: test it, with intervention arms for order 3 and order 4 (resonant value against its `±1` neighbour, as for orders 1 and 2). B2 needs a new version of the pinned runner (it has no such arms), a larger family and more compute, and `N = 242` cannot carry it. This lane recommends **B1 now**, and B2, if the PI wants it, as its own registered step after Stage 2 — at `N = 120`, where Stage 1 gives the reference.

**Choice C — precision of the thresholds (§5).** C1: register the pilot's thresholds; add an out-of-sample calibration check from the campaign's own non-resonant `BASE` draws (reported whatever it is; with 1,500 base draws it rests on about seven expected exceedances and detects only a miscalibration by a factor of roughly two to three or more); report every contrast also at the two band thresholds of §5 and on a ladder of fixed thresholds, without decision rules. C2: enlarge the pilot first (four times the draws halve the uncertainty; about ten hours). This lane recommends **C1**; under A3 the Stage 1 endpoint does not depend on the thresholds at all.

**Also for the registration.** The share of native draws with a resonant seed token is 380, 204, 87 and 94 of 3,000 at `N = 120, 240, 242, 480` (identity field). The native-only decomposition of plan §4 will rest on few exposed draws; this lane proposes to register, as a descriptive supplement, the pilot's own exposed draws at the selected horizons (unread so far; the thresholds were chosen without them), read for the first time by the registered analysis after the campaign. The decomposition is descriptive and uses the conditional risks of native (`BASE`) draws only; the risks of the intervention arms are never substituted into it (safeguard iii).

## 8. Run time and a cost estimate for Stage 2

Native runs on the PI's server (one core, one process): mean 0.68 s at (240, 1460), 0.50 s at (242, 1460), 1.33 s at (480, 2670); 0.23–0.39 s at `T = 800`. Among non-resonant draws a run ending below 100 nodes costs 0.5 s / 0.5 s / 1.1 s in these three cells, one ending at 100–299 about 2–4 s, a run reaching the cap 15–19 s (one such run at `N = 240` and one at `N = 480`).

In Stage 1 (already analysed) the mean run time over all arms was 1.65 times the native mean in cell C1 and 1.18 times in C2. **If** the arms behave at the larger `N` as they did at `N = 120` — which is what Stage 2 asks, so this is a planning assumption and not a prediction — a campaign with the Stage 1 arms and 1,000 base draws per cell (6,400 + 5,000 + 6,400 runs) costs about 7 core-hours, and with 1,500 base draws about 10; with no effect at all, about 4 and 6. Tail runs at the scaled horizons may cost more than the Stage 1 ratio assumes; twice these figures is a planning heuristic for an upper value, not a guaranteed cap. The server has one core, so core-hours are wall-clock hours.

## 9. Review record

**Review `5888182978`** (second co-owner, ChatGPT; 13 Nov 2026, 08:32:09Z; PR #260 at commit `4af11ed`): *accept, scoped, for the exploratory calibration; revisions required before the preregistration; no confirmatory compute authorised.* The reviewer did not open the record files and did not rerun the pilot; it recomputed the exact interval of `α` and the Fisher values from the published counts. Its points and what was done:

| Point | Disposition |
|---|---|
| Calibration: the three `(N, T, θ)` satisfy the pre-pilot rule as written; this is a check of discrete feasibility, not of calibration accuracy; out-of-sample checks are report-only and never retune `θ` | agreed (§4, §5); carried into the registration as a prohibition |
| A: A3, conditional on a precise prospective test contract — five order/cell contrasts per endpoint, one family of ten superiority tests, Holm, three readings; the near-quarter equivalence and the sham / detuned gates kept separate; **a valid multiplicity-adjusted bound for the minimum-effect requirement**, since Holm on `RD = 0` gives none; the "9 %" is a Bonferroni normal-quantile ratio; A3 to be recorded as a post-pilot amendment; fall back to A1 if not implemented | §7 corrected (table row A3 and the paragraph under it); the contract is an obligation of the registration |
| B: B1; the order association is descriptive and hypothesis-generating; "sufficient description" must not read as a shown cause; effect-size transport across `N` can be affected by the native-token mixture; no order-3/4 arms in Stage 2 | §6.1 (iii) reworded; B1 carried into the registration |
| C: C1; freeze `θ = 106 / 84 / 114` and the horizons; register the pilot's uncertainty bands and the campaign's out-of-sample `BASE` exceedances with exact intervals, unconditionally; band-limit outcomes without decisions; cap before tick 800 counts as positive, with counts | carried into the registration |
| (i) a median of 39–40 is not an `N`-invariant distribution or tail | §6.2 retitled and reworded |
| (ii) run-time fields of all draws are an outcome proxy; "no resonant-seed outcome or token values tabulated", not perfect blinding | §2 reworded |
| (iii) the native mixture identity is descriptive and uses `BASE` conditional risks only | §7, last paragraph |
| (iv) sample size, new independent seed tag, full hashes, five contrasts, baseline-composition reports and all gate rules fixed before execution | obligation of the registration |
| (v) the twofold run-time reserve is a planning heuristic | §8 reworded |

**PI.** The PI relayed this review in the project conversation on 13 Nov 2026 (11:51 and 11:59 +03:00) without a decision text of his own. No PI decision on A, B or C is recorded here. Both co-owners recommend A3 (conditional), B1, C1.

## 10. State and next steps

- The upload is offered for custody unchanged (PR #259); merge is the PI's decision.
- The Stage 2 registration (`records/az/`, with its package) is drafted on the joint recommendation A3 (conditional), B1, C1 and carries the nine obligations of plan §8 and the conditions of review `5888182978`. It is a draft for review: the choices A–C are the PI's, to be confirmed or changed before any confirmatory run, together with or before the decision on compute. No confirmatory run before that.
- Until the registration is fixed, the outcome and token values of draws with a resonant token in these files stay untabulated by this lane.
