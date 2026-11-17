# AZ mechanism study — first-contact tables on S1-C1 (exploratory description)

**[SESSION] NONCANONICAL, EXPLORATORY.** The one run of the frozen table script on the Stage 1 records of cell `S1-C1` (`N = 120`, `k = 8`, 800 ticks, profile P1). Prepared by the AZ co-owner (Claude), 17 November 2026; r2 (17 Nov, 09:35 +03:00) applies the editorial corrections R1–R3 of review `5933968347` (no new run, script, manifest and outputs unchanged). The endpoint outcomes were known before the design (Stage 1 report); this is a pre-specified description, **not mechanism evidence, not a test and not a claim**. Nothing is adopted; no DSN is edited.

## 1. Run record

| Item | Fact |
|---|---|
| Design | `records/az/AZ_TOKEN_RESONANCE_MECHANISM_DESIGN.md` §5 (r2, PR #281) |
| Script | `evidence/az/mechanism/az_tokres_contact_tables.py`, SHA-256 `78822775de7d52540f4700d923ab55a5750df6aa06245c9178a2ed91e952611b` (reviews `5922692022`, `5923426652`, PASS `5933459799` at `19c3b58`) |
| Manifest | `evidence/az/mechanism/contact_tables_manifest.json`, frozen at `e157ffe` (readback PASS `5933699818`), SHA-256 `8c3d1f70145cbe54be7fa4add58aba2e39ffe63f19b2b3ce6a3801748a9e37af`; PI decision on its four settings 17 Nov 2026, 08:54 +03:00 |
| Input | `upload/az-token-resonance-stage1/` bound to its `HASHES.txt` (commit `95db7af`); 1,500 base draws × BASE, O1R, O1D, O2R, O2D, SHAM |
| Run | 17 Nov 2026, 09:00 +03:00, this session (Python 3.13), `--plan registered`, exit 0; `INTEGRITY: PASS` (binding, Stage 1 validator, pairing keys, clocks and endpoint) |
| Output | `evidence/az/mechanism/s1c1_run/s1c1_tables.txt` (`57c3aec1…0af0`), `s1c1_descriptors.jsonl` (9,000 lines, `1aae8cd7…6fd7`), `SHA256SUMS`; committed unchanged at `1211e06` before being read |

Endpoint counts reproduce Stage 1 (Y = 1: O1R 387, O1D 23, O2R 278, O2D 36 of 1,500).

## 2. What the tables show (descriptive; counts as printed)

**(a) The first contact is nearly the same in the two arms.** (`tau_slot` in the tables is the free-flight slot contact time `tau_slot^free`, design §4.) Same first-contact time and edge set in 1,319 of 1,500 order-1 pairs and 1,300 of 1,500 order-2 pairs; `tau_contact` paired R < D / = / > D: 45 / 1,414 / 41 (order 1), 43 / 1,415 / 42 (order 2); the replaced node is in the first-contact graph in 909 resonant vs 900 detuned runs (order 1), 897 vs 892 (order 2). Component types at first contact have nearly equal distributions across all six arms; a unique-centre star (an immediate birth) occurs in 31–40 runs per arm. Separately, `fe = tau_contact` in 1,487–1,495 runs per arm; the remainder have `fe > tau_contact`.

**(b) Early birth: marginally close, not paired-identical.** First birth by tick 100 in 984 (O1R) vs 964 (O1D), 997 (O2R) vs 966 (O2D) runs — close marginal rates. Paired, the first-birth times are mostly **not** equal: `fb` R < D / = / > D: 712 / 99 / 671 (order 1), 696 / 113 / 672 (order 2). The endpoint divergence is already visible by tick 200 (`t100 ≤ 200`, equivalently `M ≥ 100` at tick 200: O1R 87 vs O1D 3 runs, O2R and O2D as printed in T3). `t100` is attained in the resonant arm only in 374 order-1 pairs and in the detuned arm only in 10 (259 / 17 for order 2).

**(c) Pairs in the strict common-contact stratum.** The strict common-contact condition of design §4.2 — finite `tau_common`, both free-flight slot contact times `tau_slot^free,R` and `tau_slot^free,D` later — holds in 555 order-1 and 561 order-2 pairs (counts of pairs). In these pairs, by the design's argument, the first-contact graph and the non-slot updates at the first contact are identical in the two arms. From J2:

| Pair | Stratum | Pairs | Y_R | Y_D | difference |
|---|---|---|---|---|---|
| O1R vs O1D | strict | 555 | 0.267 | 0.014 | +0.252 |
| O1R vs O1D | not strict | 945 | 0.253 | 0.016 | +0.237 |
| O2R vs O2D | strict | 561 | 0.175 | 0.032 | +0.143 |
| O2R vs O2D | not strict | 939 | 0.192 | 0.019 | +0.173 |

The stratum is a **paired stratum**: it is defined by the two potential first-contact configurations of the pair, i.e. by `th0` together with **both** arms' slot tokens. It is not a selection on a post-initial event, but it is also not an intervention-independent baseline subgroup — membership depends on the resonant and the detuned token values, so the strict/not-strict contrast is not a subgroup analysis of a pre-treatment covariate. The 555 and 561 are pair counts; they say nothing about which share of the endpoint difference arises in that stratum.

**(d) Early birth and the endpoint (J4).** endpoint rate among resonant runs with a first birth by tick 100 vs without: 0.264 vs 0.246 (O1R), 0.184 vs 0.189 (O2R); detuned 0.018 vs 0.011, 0.026 vs 0.021. A marginal association only; it does not decide whether early growth contributes.

## 3. Reading, and its limits

A description consistent with these tables: **marginal summaries of the first contact and of early birth show limited differences between the resonant and the detuned arm, while the tick-800 endpoint difference is much larger.** In the paired strict common-contact stratum (555 / 561 pairs), whose first event is identical by construction, the endpoint difference is of similar size to that outside it. **The dynamic stage at which the difference arises is not determined by these tables.**

What this does **not** show:
- It does not locate the effect "in growth" or after the first birth. Paired first-birth times differ in most pairs (712 / 99 / 671), and the endpoint split is visible by tick 200. In the strict stratum the replaced node still differs between arms after the first contact (its orbit, then its own actual contacts and everything after); the difference can arise at any of these stages.
- It is not a mediation share and not a test: no interval, no p-value, outcomes known in advance, one cell, one horizon, one threshold.
- The strict/not-strict difference in (c) is small and of opposite sign for the two orders; it is not read.
- Nothing about other `N`, Stage 2, TDR-26 or any TDR-G module.

## 4. What it suggests for the next design step (for review and the PI)

The tables make the first contact alone an unlikely place for the whole difference, but they do not choose between later stages. Two fork designs of §6 remain **candidates, neither confirmed**: a landmark after the first birth, and a landmark at the replaced node's actual first slot contact. The latter is **not** known from the initial state: `tau_slot^free` (the table field `tau_slot`) is the free-flight contact time, valid only while the replaced node moves freely; after the first global contact, swaps, path cycles and births can change its phase/token history, so its actual first contact is a dynamic variable that the provenance and tracking instrument of §6 would have to record. Both candidates need that instrument first. No run is proposed.
