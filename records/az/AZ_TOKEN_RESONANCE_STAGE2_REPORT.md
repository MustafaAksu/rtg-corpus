# AZ Action 1 — Stage 2: report

**[SESSION] NONCANONICAL. Report of the registered confirmatory campaign `AZ-TOKRES-S2`; nothing here is adopted.** Prepared by the AZ co-owner (Claude), 16 November 2026. Registration: `records/az/AZ_TOKEN_RESONANCE_STAGE2_PREREGISTRATION.md` r2 at commit `74ad6946e9710a2272b9d7792d6d8f0c45cda168` (cited as *P §n*). Decisions and start: `records/az/AZ_TOKEN_RESONANCE_STAGE2_AUTHORISATION.md`. Data: `upload/az-token-resonance-stage2/` (custody PR from the upload branch). Every number below is copied from the registered output `analysis_stage2.txt`, which a rerun in this session reproduced byte for byte (§3).

## 1. Result in one paragraph

All ten confirmatory contrasts read **SUPPORTED**, every one **unqualified**. At `N = 240`, `242` and `480` (`k = N/15`, profile P1, policy `bound_symmetric`), setting one initial token to a value with `2x ≡ 0` rather than to its neighbour `x ± 1` raises the probability of the endpoint by +0.21 to +0.28; setting it to a value with `2x ≡ N/2` (`N = 240`, `480`) by +0.13 to +0.16; on both endpoints — `M ≥ θ(N)` at the horizon fixed by the pilot, and the Stage 1 endpoint `M ≥ 100` at tick 800. Every simultaneous 99.5 % lower limit is above `δ* = 0.05` (smallest +0.108). At `N = 242`, the four values nearest `N/4` are **equivalent to the native state** within ±0.05 on both endpoints. Node-label permutation, sham perturbation and the detuned comparators read PASS / EQUIVALENT in every cell and endpoint. The integrity layers and both gates passed; the token-law counter is 0 over 26,300 campaign runs and the three pilot files. Within its registered scope, the Stage 1 contrast persists at the three larger `N`.

## 2. Run record

| Item | Fact | Source |
|---|---|---|
| Machine | the PI's Ubuntu server, one process (`--jobs 1`), Python 3.12.3, `Linux-6.8.0-147-generic-x86_64-with-glibc2.39` | `CAMPAIGN_COMPLETE.json` |
| Code | worktree at the authorised commit `74ad694`; `stage2/SHA256SUMS` = `25b796b3…eb4b` checked by the block before the run; the nine script and pin hashes recorded in the marker equal the registered package (§3) | marker; PI's terminal output of 14 Nov |
| Time | started 2026-11-14 20:14:02Z, finished 2026-11-15 15:51:22Z; 70,640 s (19.6 h); not resumed | marker |
| Steps | self-test exit 0; pilot files as registered; fixtures exit 0; three cells, one shard each, all exit codes 0, record counts as expected; analysis exit 0 | marker `steps` |
| Records | S2-C240 9,400; S2-C242 7,500; S2-C480 9,400 (26,300) | marker; files |
| Upload | branch `upload/az-token-resonance-stage2`, commit `7aafe37d51ba58665bce91c0cc2b3fb46271ffda` by the PI (2026-11-15 15:51:24Z), one commit on `main` `2676e6f`; 15 files incl. logs; `HASHES.txt` SHA-256 `3e211e6a7bab27b9e13af0dd5c0a93128b79c464d64470ea4d6b86775314a7e7` | GitHub; PI's terminal output of 16 Nov, 08:41 +03:00 |
| Exclusions | none (`excluded=[]` in every cell) | output |

**No interim look.** The record files were first opened in this lane after the marker and the upload existed. That nobody opened them on the server before the marker is source-reported (the PI relayed only `tail` lines and record counts were the only permitted look).

## 3. Custody and verification (`EV-BYTES`, `EV-HASH`, `EV-RUN`)

`evidence/az/token_resonance/stage2_result/verify.sh`, run in this session on this branch with the upload commit merged into a scratch worktree; output `verify_output.txt`, `VERIFY PASS`:

- the registered package passes `sha256sum -c` and its `SHA256SUMS` equals the authorised hash;
- `HASHES.txt` passes for all 13 listed files;
- the marker: plan `stage2`, confirmatory, not resumed, fixtures not skipped, pilot supplied; the nine SHA-256 values it records (engine, orientation reference, runner, fixtures, Stage 1 analysis, Stage 2 analysis, driver, golden file, `HASHES.txt`) equal the bytes in the repository;
- 26,300 records in three files;
- the registered Stage 2 analysis, rerun from the authorised scripts on the uploaded records with the pilot files from `main`, exits 0 and its output is **byte-identical** to `analysis_stage2.txt` from the campaign machine (rerun stored as `analysis_stage2.rerun.txt`).

Inside that analysis (fail-closed; P §6.4): `INTEGRITY: PASS (26300 records in 3 file(s) of 3 cells; identity, custody, states, records, set, tick-800 checkpoint, pilot files checked)`; `G1 fixtures on the campaign machine: PASS`; `G2 … summed violation counter (campaign and pilot files): 0 -> PASS`.

## 4. Controls (verbatim readings; 95 % Agresti–Min, margin ±0.025)

| Cell | Endpoint | G3 permutation | G4 sham vs BASE | G5 `O1D` vs BASE | G5 `O2D` vs BASE |
|---|---|---|---|---|---|
| S2-C240 | `E_θ` | PASS (0 of 400 differ) | EQUIVALENT, +0.0076 [−0.0018, +0.0169] | EQUIVALENT, +0.0034 [−0.0048, +0.0115] | EQUIVALENT, −0.0027 [−0.0105, +0.0051] |
| S2-C240 | `E_100` | PASS | EQUIVALENT, +0.0083 [+0.0008, +0.0157] | EQUIVALENT, +0.0061 [−0.0007, +0.0128] | EQUIVALENT, +0.0027 [−0.0039, +0.0093] |
| S2-C242 | `E_θ` | — | EQUIVALENT, −0.0020 [−0.0082, +0.0042] | EQUIVALENT, +0.0067 [−0.0011, +0.0145] | — |
| S2-C242 | `E_100` | — | EQUIVALENT, −0.0007 [−0.0053, +0.0039] | EQUIVALENT, +0.0007 [−0.0043, +0.0056] | — |
| S2-C480 | `E_θ` | PASS (0 of 400 differ) | EQUIVALENT, +0.0020 [−0.0057, +0.0097] | EQUIVALENT, +0.0034 [−0.0052, +0.0119] | EQUIVALENT, +0.0027 [−0.0051, +0.0105] |
| S2-C480 | `E_100` | PASS | EQUIVALENT, +0.0040 [−0.0017, +0.0098] | EQUIVALENT, +0.0034 [−0.0028, +0.0095] | EQUIVALENT, +0.0020 [−0.0032, +0.0073] |

One control interval excludes zero: G4 sham at S2-C240 on `E_100`, +0.0083 [+0.0008, +0.0157] (discordant 21/9, unadjusted McNemar `p = 0.043`). It lies inside ±0.025 and reads EQUIVALENT by the registered rule (P §6.4: an interval inside the margin is equivalence; one of the sixteen nominal 95 % control intervals excluding zero is within what chance gives). It is stated, not read.

## 5. Registered readings (verbatim)

Paired on the base draw, `n = 1500` each; Holm over the ten; simultaneous 99.5 % Agresti–Min intervals.

| # | Endpoint | Cell | Contrast | `p1` | `p0` | RD [99.5 % simultaneous] | discordant | Holm `p` | Reading | Qualifiers |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `E_θ` | S2-C240 (`θ = 106`, `T = 1460`) | order 1, `O1R` vs `O1D` | 0.2527 | 0.0173 | +0.2353 [+0.2035, +0.2666] | 360/7 | 9.1e−96 | SUPPORTED | UNQUALIFIED |
| 2 | `E_θ` | S2-C240 | order 2, `O2R` vs `O2D` | 0.1620 | 0.0113 | +0.1507 [+0.1233, +0.1776] | 235/9 | 1.9e−57 | SUPPORTED | UNQUALIFIED |
| 3 | `E_θ` | S2-C242 (`θ = 84`, `T = 1460`) | order 1 | 0.2953 | 0.0173 | +0.2780 [+0.2435, +0.3118] | 433/16 | 1.4e−105 | SUPPORTED | UNQUALIFIED |
| 4 | `E_θ` | S2-C480 (`θ = 114`, `T = 2670`) | order 1 | 0.2553 | 0.0160 | +0.2393 [+0.2065, +0.2715] | 373/14 | 7.1e−91 | SUPPORTED | UNQUALIFIED |
| 5 | `E_θ` | S2-C480 | order 2 | 0.1733 | 0.0153 | +0.1580 [+0.1297, +0.1859] | 250/13 | 1.9e−57 | SUPPORTED | UNQUALIFIED |
| 6 | `E_100` | S2-C240 | order 1 | 0.2200 | 0.0140 | +0.2060 [+0.1755, +0.2360] | 317/8 | 4.2e−82 | SUPPORTED | UNQUALIFIED |
| 7 | `E_100` | S2-C240 | order 2 | 0.1453 | 0.0107 | +0.1347 [+0.1083, +0.1606] | 212/10 | 2.0e−50 | SUPPORTED | UNQUALIFIED |
| 8 | `E_100` | S2-C242 | order 1 | 0.2273 | 0.0053 | +0.2220 [+0.1913, +0.2521] | 335/2 | 3.7e−96 | SUPPORTED | UNQUALIFIED |
| 9 | `E_100` | S2-C480 | order 1 | 0.2180 | 0.0087 | +0.2093 [+0.1787, +0.2394] | 321/7 | 1.7e−84 | SUPPORTED | UNQUALIFIED |
| 10 | `E_100` | S2-C480 | order 2 | 0.1500 | 0.0073 | +0.1427 [+0.1163, +0.1687] | 220/6 | 6.6e−57 | SUPPORTED | UNQUALIFIED |

**Side by side** (P §6.2): every contrast is SUPPORTED on both endpoints — "the contrast is present at this `N` on both endpoints".

**Near-quarter control, `N = 242`** (separate from the family; 99.5 %, margin ±0.05): `E_θ` `Q2R` vs `BASE` −0.0040 [−0.0144, +0.0064] — EQUIVALENT TO BASE; `E_100` −0.0020 [−0.0095, +0.0055] — EQUIVALENT TO BASE; both unqualified. Per value (D7) the four near-quarter values give `E_θ` 0.005–0.014.

The simultaneous coverage of the minimum-effect intervals is nominal under the normal approximation (P §6.2, R1). Every lower limit exceeds `δ*` by at least 0.058, so no reading sits near the boundary where that approximation would matter.

## 6. Descriptive outputs (no reading attached)

- **D1 band thresholds.** At the lower and upper band threshold of each cell the ten contrasts range from +0.128 to +0.297; all sign tests and McNemar values far below any conventional level. The readings do not depend on where in its band `θ` lies.
- **D2 ladder.** The resonant arms separate from all others at every threshold from 60 to 300 and at both read-outs. At `c = 300` the order-2 arms reach the cap mostly after tick 800 (S2-C240 `O2R`: 0.0060 at tick 800, 0.0933 at the end; S2-C480: 0.0060 / 0.1100), the order-1 arms mostly before it (S2-C240 `O1R` 0.1140 / 0.1360).
- **D3 threshold-free.** Resonant `M` exceeds detuned `M` in 971–1,094 of 1,500 pairs (smaller in 360–483); sign tests 5e−38 to 4e−86; median paired difference 5–14 nodes.
- **D4 out-of-sample calibration** (report only; thresholds unchanged): non-resonant `BASE` draws with `M ≥ θ`: 10/1409 = 0.0071 [0.0034, 0.0130] (240), 6/1454 = 0.0041 [0.0015, 0.0090] (242), 11/1454 = 0.0076 [0.0038, 0.0135] (480), against the pilot's `α` = 0.0053 [0.0029, 0.0090]: each point estimate inside the pilot's interval. `M ≥ 100` at tick 800 in the same draws: 1, 1, 2.
- **D5 native decomposition** (`BASE` only). Native draws with a token of `4x ≡ 0`: 91, 46, 46 of 1,500 (law: 0.065, 0.033, 0.033 of draws). Their `E_θ` risk `p1` = 0.13 [0.08, 0.22], 0.33 [0.21, 0.47], 0.30 [0.19, 0.45], against `p0` = 0.0071, 0.0041, 0.0076. The pilot's exposed draws, tabulated here for the first time: `p1` = 0.20, 0.28, 0.23 (204, 87, 94 draws); pooled 0.18, 0.29, 0.26. In the native state the few draws that carry a resonant token account for about half of all endpoint events (e.g. S2-C240: 12 of 22 on `E_θ`).
- **D6 order breakdown** (exploratory; cut post hoc on the pilot). `E_θ` among non-resonant `BASE` draws: smallest order ≤ 6 — 8/408 (240), 3/230 (480); every order > 6 — 2/1001, 8/1224; at 242 the low-order class is empty by arithmetic (6/1454). Same direction as in the pilot at `N = 240`, weaker at `N = 480`; untested, no mechanism (B1).
- **D7 by value.** The two resonant values of each order give similar risks (e.g. S2-C240 `O1R` value 0: 0.264, value 120: 0.241; S2-C480 `O2R` 120: 0.174, 360: 0.173).
- **D8 clean pairs** (other three tokens non-resonant): RD +0.129 to +0.272; the detuned risk falls to 0.000–0.012.
- **D9 cap.** `O1R` reaches the cap in 204, 224, 222 runs, mostly before tick 800 (170, 189, 180); `O2R` in 140, 165 runs, almost all after tick 800 (9, 9 before). Other arms: 2–16.
- **D10 run time.** Mean seconds per run, e.g. S2-C480: BASE 2.49, `O1R` 5.00, `O2R` 9.89.

## 7. Across `N` — tabulated, not tested

No trend across `N` is registered or tested (P §6.7); the intervals below are at different levels (Stage 1: 97.5 % Agresti–Min; Stage 2: 99.5 % simultaneous) and the endpoints are those named.

| `N` | `k` | order 1, `M ≥ 100` at tick 800 | order 2, same endpoint | Source |
|---|---|---|---|---|
| 120 | 8 | +0.2427 [+0.2166, +0.2681] | +0.1613 [+0.1381, +0.1841] | Stage 1 PC1, PC2 |
| 122 | 8 | +0.2193 [+0.1944, +0.2436] | — (no order-2 value) | Stage 1 PC3 |
| 240 | 16 | +0.2060 [+0.1755, +0.2360] | +0.1347 [+0.1083, +0.1606] | Stage 2 #6, #7 |
| 242 | 16 | +0.2220 [+0.1913, +0.2521] | — | Stage 2 #8 |
| 480 | 32 | +0.2093 [+0.1787, +0.2394] | +0.1427 [+0.1163, +0.1687] | Stage 2 #9, #10 |

Read as a table only: order 1 is about +0.21 to +0.24 and order 2 about +0.13 to +0.16 at every `N` tested, and the order-1 effect exceeds the order-2 effect wherever both exist. That is a description of five cells, not a scaling law, not an `N`-independence claim, and not a statement that `M ≥ 100` at tick 800 is the same event at every `N`.

## 8. What this establishes and what it does not

**Establishes** (P §6.7, within scope): on the pinned TDR-G engine `TDRG-ART-GENESIS-MC` with `TDRG-DEF-ORIENT` (profile P1), policy `bound_symmetric`, four initial nodes, `k = N/15`, cap 300, at `N ∈ {240, 242, 480}` with horizons 1460 / 1460 / 2670 and thresholds 106 / 84 / 114, and on `M ≥ 100` at tick 800 at the same `N`: the total causal effect of replacing one initial token by a value with `2x ≡ 0` rather than by its `±1` neighbour is at least 0.05 (and estimated at +0.21 to +0.28); for `2x ≡ N/2` likewise (+0.13 to +0.16); the near-quarter values at `N = 242` have no effect beyond ±0.05. Together with Stage 1 the contrast is observed at five `N` from 120 to 480.

**Does not establish:** a mechanism (whether the token acts during growth or through the first contact and first birth — open, as at Stage 1); that the arithmetic condition acts through the free parent–child phase law (`TDRG-ALG-PARENT-CHILD-PHASE` names the condition; its role is untested); any `N`-dependence or independence; anything at other `k/N`, policies, profiles, horizons or thresholds; anything about TDR-26, `TDRG-OPEN-LOCKING-FAIL` or any open module of TDR-G; a bridge observable (OPEN-P1 untouched); the order hierarchy below order 2 (D6, untested); any relation to AZ's Hashimoto `4 | q` rule or to Dyadic/DZT `q = 4` beyond the numeral (SG-AZ-7, SG-DZT-1).

## 9. Deviations and process notes

- **No deviation from the registration.** No exclusion, no resume, no change of any registered constant; the block differed from the form of P §8 only as recorded in the authorisation record §3.
- **Run time** 19.6 h against the planning figure of about 10 h; inside the twofold planning value (≈ 20 h), which the registration called a heuristic. The cause is visible in D9–D10: order-2 resonant runs grow slowly to the cap after tick 800 and run to the full horizon (mean 6.4 s at `N = 240`, 9.9 s at `N = 480`, against 1.1 and 2.5 s for `BASE`). Planning information only.
- **One control interval excluding zero** (G4 sham, S2-C240, `E_100`): §4.
- **Out-of-sample calibration** (D4): consistent with the pilot's `α` in all three cells; it changes nothing by registration.
- **Blinding statement.** The pilot's exposed draws were tabulated for the first time by the registered analysis (D5), after the campaign. Run-time aggregates of all draws had been seen earlier (intake §2).

## 10. Outcome rule and decisions for the PI

**The rule** (PI, 12 Nov 2026; Stage 1 report §11 item 3): *a validated, supported Action 1 contrast is eligible for a PI-approved `[NUM diagnostic]` entry within AZ Level A, with its exact simulation scope and provenance. It is offered to TDR-G for owner disposition. It does not by itself close `AZ-OPEN-PROMO`, promote AZ maturity, or become an adopted TDR-G claim.* All ten Stage 2 contrasts are supported and, after review of this report, validated in the sense of that rule.

Proposals of this lane, for the second co-owner's review and the PI's decision:

1. **Accept this report** after independent review.
2. **Whether Stage 2 enters AZ**, and how. This lane's proposal: one new `[NUM diagnostic]`, `AZ-NUM-TOKRES-S2`, beside `AZ-NUM-TOKRES-S1` (not a widening of S1's scope, so that each carries its own registration, endpoints and provenance), with the artifact `AZ-ART-TOKRES-S2`, in an AZ v0.10 built as one content stage. It would change neither Level A nor `AZ-OPEN-PROMO`.
3. **TDR-G.** By the PI's decision of 12 Nov 2026 ("gerek yok") no separate TDR-G item is filed for the numerical result; TDR-G would receive the usual notice of the AZ edition that carries it. This lane proposes to keep that.
4. **What next** (no proposal to run anything now): the open questions are the mechanism (first contact vs growth — a design using the birth-anchored collection the runner already records), the order hierarchy below 2 (choice B2 of the intake, as its own registered step at `N = 120`), and Stage 3 (TDR-26 in TDR-G's scope, which needs TDR-G). Each would be a new registration.
