# AZ Action 1 — Stage 2 pilot: intake and calibration evaluation

**[SESSION] NONCANONICAL, EXPLORATORY. Not a registration, not a confirmatory result, no claim about token resonance at any `N`.** Prepared by the AZ co-owner (Claude), 13 November 2026. Plan and review record: `records/az/AZ_TOKEN_RESONANCE_STAGE2_PILOT_PLAN.md` (PR #251). Nothing here is adopted; the confirmatory Stage 2 campaign is not authorised.

## 1. What arrived

| Item | Fact | Source |
|---|---|---|
| Run | the PI's Ubuntu server, pilot script at commit `a6d50adb852b30e1dc520d2a54e680ea95d98c6a` (SHA-256 `ccc9e776…9a95`), plan `pilot`, tag `S2-CALIB-PILOT-20261112`; finished 12 Nov 2026 17:07:26Z; 10,977 s in the invocation that completed it; Python 3.12.3 | `PILOT_COMPLETE.json` |
| Upload | branch `upload/az-token-resonance-s2-pilot`, commit `5fb65fb6e15a44f973c9314bc004171809a02976` by the PI (12 Nov 2026 17:07:27Z), one commit on `main` `2de679b`; 11 files, 17,134,921 bytes, under `upload/az-token-resonance-s2-pilot/` | GitHub; PI's terminal output in the project conversation (13 Nov 10:38 +03:00) |
| Files | seven record files of 3,000 records each (21,000 native runs), `MANIFEST.jsonl`, `PILOT_COMPLETE.json`, `summary.txt`, `HASHES.txt` (SHA-256 `a463a197327888c11b46a121217fff51beff634b5c16271ec16f2f1af16cc1cd`) | upload commit |

## 2. Custody checks (`EV-BYTES`, `EV-HASH`, `EV-RUN`)

`evidence/az/token_resonance/stage2_pilot/intake_check.py` (SHA-256 `29d37f24934ff48def91ef765e68aec158c2fbb899d01173fe4799db3957f50c`), run on a clean checkout of the upload commit; output `intake_output.txt` (SHA-256 `04dfb890771551147c899aae6d297fc931922d3249c1569deaae772f55b499a2`), exit code 0, `RESULT: PASS`:

- `HASHES.txt` lists ten files and every one has its listed hash; the manifest, the completion marker and the files agree on the seven record-file hashes; the marker carries the manifest's hash;
- every one of the 21,000 records carries its cell's identity (`N`, `k`, `T`, cap 300, profile P1, policy `bound_symmetric`, arm `BASE`, tag) and the four pinned hashes of `stage2_pilot/SHA256SUMS` (engine `4c94d874…a608`, orientation reference `ca59e9b9…d59c`, runner `75c5f139…8992`, pilot script `ccc9e776…9a95`); records are complete and in the order of the draw index; the law-violation counter is 0 in every record;
- the stored `summary.txt` equals, byte for byte, a rerun of the pilot script's `summary` on the uploaded files.

**What was read, and what was not.** Review `5875885484` item 9 limits this lane's intake to the hash check, the stored summary and its rerun. The intake script reads, in addition and for every record, the identity fields, the draw index, the law-violation counter and the run time; it reads the outcome fields (`M`, `hit_cap`) **only** for native draws without a resonant seed token (`native_class == "NR"`), and `t100`, `births` and `M_at` for no record. No outcome of a draw that carries a resonant token was read, tabulated or printed in this intake, by the script or otherwise. Two aggregate facts about all draws were already in the stored summary and are repeated: total run time and the longest run per cell.

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

**Consequences proposed for the registration** (proposals of this lane; review and the PI decide):

1. The thresholds enter as **registered constants** (106, 84, 114 at horizons 1,460, 1,460, 2,670). Each paired contrast at one `N` compares two arms at the same threshold and is a valid test of a difference between them **for any fixed threshold**; calibration error does not bias it. What the calibration carries is only the comparability of the endpoint *across* `N`.
2. A **registered out-of-sample calibration check**: the confirmatory campaign's own native (`BASE`) draws without a resonant token give, per cell, a fresh realised rate at the registered `θ` with its exact interval. It is reported whatever it is. Any statement that compares effect sizes across `N` is conditional on it; the within-`N` readings are not.
3. A **registered sensitivity band**: each contrast is also reported at the two thresholds of the middle column above, without a decision rule, next to the Stage 1 endpoint (`M ≥ 100`, `T = 800`) and the threshold-free paired comparison already planned.
4. The alternative — enlarging the pilot before registering (four times the draws would halve the uncertainty of `θ`; about ten hours on the server) — is not recommended by this lane: item 2 obtains the same information from runs the campaign needs anyway, and item 1 makes the primary readings independent of it.

## 6. Other observations (non-resonant native draws only; exploratory)

- **The bulk moves with the horizon, as the plan expected.** Fraction with `M ≥ 100`: at `N = 240`, 8 of 2,796 at `T = 800` and 18 of 2,796 at `T = 1460`; at `N = 480`, 2 of 2,906 at `T = 800` and 30 of 2,906 at `T = 2670`. A fixed threshold of 100 would have given a baseline of 0.07 % at (480, 800) and 1.0 % at (480, 2670), against 0.53 % at the reference.
- **`N = 240` and `N = 242` differ in the non-resonant tail at the same `k` and `T`.** `M ≥ 100`: 8 of 2,796 against 1 of 2,913 at `T = 800` (Fisher exact two-sided `p = 0.019`); 18 of 2,796 against 8 of 2,913 at `T = 1460` (`p = 0.048`); the matched thresholds differ accordingly (106 against 84). Post hoc, two overlapping comparisons, unadjusted: **not established**, and no cause is proposed. If real, it would mean that the class "no token with `4x ≡ 0`" is not equally inert at the two `N`; the matched threshold absorbs such a difference by construction, which is a reason to keep the fixed-threshold endpoint in parallel (review item 3). It is noted so that the registration can decide in advance whether to describe the non-resonant class further (for instance by `8x ≡ 0`), not to motivate a claim.
- **Share of native draws with a resonant seed token** (identity field): 380, 204, 87 and 94 of 3,000 at `N = 120, 240, 242, 480`. The native-only decomposition of plan §4 will rest on few exposed draws at the larger `N` unless the campaign's `BASE` arm is large; its resolution has to be stated in the registration.

## 7. Run time and a cost estimate for Stage 2

Native runs on the PI's server (one core, one process): mean 0.68 s at (240, 1460), 0.50 s at (242, 1460), 1.33 s at (480, 2670); 0.23–0.39 s at `T = 800`. Among non-resonant draws a run ending below 100 nodes costs 0.5 s / 0.5 s / 1.1 s in these three cells, one ending at 100–299 about 2–4 s, a run reaching the cap 15–19 s (one such run at `N = 240` and one at `N = 480`).

In Stage 1 (already analysed) the mean run time over all arms was 1.65 times the native mean in cell C1 and 1.18 times in C2. **If** the arms behave at the larger `N` as they did at `N = 120` — which is what Stage 2 asks, so this is a planning assumption and not a prediction — a campaign with the Stage 1 arms and 1,000 base draws per cell (6,400 + 5,000 + 6,400 runs) costs about 7 core-hours, and with 1,500 base draws about 10; with no effect at all, about 4 and 6. Tail runs at the scaled horizons may cost more than the Stage 1 ratio assumes; twice these figures is a prudent upper planning value. The server has one core, so core-hours are wall-clock hours.

## 8. State and next steps

- The upload is offered for custody unchanged (its own PR from `upload/az-token-resonance-s2-pilot`); merge is the PI's decision.
- Next in this lane: the Stage 2 registration (`records/az/`, with its package), carrying the nine obligations of plan §8 and the proposals of §5 above; then review by the second co-owner; then the PI's decision on compute. No confirmatory run before that.
- Until the registration is fixed, the outcomes of draws with a resonant token in these files stay unread by this lane.
