# AZ Thread C (`az_v5`) recovery — hash check and replay

**Date:** 11 November 2026. **By:** Claude, AZ co-owner. **[SESSION]** custody record.
**Evidence keys:** `EV-BYTES`, `EV-HASH`, `EV-CODE`, `EV-RUN` as stated per item. No owner decision is made, no DSN is edited, no grade changes. What AZ v0.7 §9 says about availability stays as adopted until a later AZ edition.

## 1. What arrived

The PI attached files to this session in three deliveries on 11 Nov 2026, found after the AZ v0.7 release record (§14) listed the Thread C evidence as absent: eleven files at 16:53 +03:00, four at 17:07 +03:00 and one at 17:25 +03:00. On the PI's instruction ("bu dosyalardan lazımlı olanları repoya yükleyelim. sana bu konuda tam yetki", 16:41 +03:00) thirteen of them were pushed unchanged to `upload/az-v5-partial-recovery-20261111` (commits `10426f7`, `f6be0b3`, `b3aa0ba`), directory `upload/az-records/`; two were byte-identical duplicates; one is held. The branch had been created by the ChatGPT co-owner session and carried no commit of its own before. Intake manifest: `upload/az-records/INTAKE_MANIFEST.md`.

## 2. Hash check (`EV-BYTES`, `EV-HASH`)

All hashes recomputed here from the bytes on the branch; the staged Git blobs were compared with the attached files before each commit (`.gitattributes` is `* -text`).

| File under `upload/az-records/` | SHA-256 | Against the registry |
|---|---|---|
| `az_v5/benchmarks/AZ_ARTIFACT_REGISTRY.json` | `6686706490c0f4d1d90629aaf6594176faff333096d4b0e3834128ff75ba875a` | the registry: ten entries, `version: az_v5`, `phase: AZ-1A + AZ-1B` |
| `az_v5/lib/hashimoto.py` | `9cc2137936bd43b2dcf02c4ffd4c5c039527076a9891edecea33d13abd5f1b70` | equal |
| `az_v5/lib/graphgen.py` | `6bd34a917ec32ef3091ed0a70ad4c81ac176932efc29b4cb478d9d7b3058d4b8` | equal |
| `az_v5/lib/graphio.py` | `4dcb913118fb2b7f3d7619c7c35ee992cfb07728a9af83004717bc049f76f6d8` | equal |
| `az_v5/lib/manifest.py` | `ea845088f74992c34a8c673693daa41f1d22b5df7b354e42e9fd0571a72d0ec5` | equal |
| `az_v5/benchmark_ladder.py` | `d771dfa2cbdefe23b780dc21c42df60d6cdf951e2ed59bd3f831f947ff2a4352` | equal |
| `az_v5/validate_solver.py` | `50ff52e10f32cb553671a0c2d14fdba7daf2f1be18168112692b8cd7a69879ec` | equal |
| `az_v5/az1b_certify.py` | `7a0f8aa5b9aa5e6debd3510c3c6e330b68bb15632ab1cbe8d0dfacddb1bcc02b` | equal |
| `az_v5/benchmarks/bouquet_2_4_hashimoto_matrix.json` | `4c377fa704e8b08e648caf3baff516f97bb5551cafc17506d7a560501347ca01` | equal |
| `az_v5/benchmarks/bouquet_2_4_charpoly.txt` | `6a6979b0d25b8a314f524a35a8f7114848701d4486f70b0a029b1c3313db788f` | equal |
| `CONVENTIONS_FROZEN.md` | `1c4b715aea0785c22c2f194d9cf8ba6a1b3c76dc2608366dedd58160ed478f2d` | not a registry entry |
| `export/conv_az_graph_export.py` | `fab14ae1d2b151f405bda105103ec3fcca32841542369304d1d1a5b35517fe1e` | not a registry entry |
| `phase2/AZ_PHASE2_N120_NULL1_smoke.json` | `561c66ac8e5d359d5806d9aa058e988b682412ddb4a84e71371e754e89e22284` | not a registry entry |

**Nine of the ten registry entries are deposited as original bytes and are equal.** The tenth, `benchmarks/az_v5_synthetic_benchmark_report.json`, was not received as a file; its content is recovered by regeneration (§3). `export/conv_az_graph_export.py` (third delivery) has no registry entry to be checked against; its hash is recorded here and in the intake manifest.

**Limits of the identification.**
1. No adopted document records the registry's own hash. §3 shows that the deposited `az1b_certify.py`, run over the deposited files, writes a registry byte-identical to the found one: the set is self-consistent and self-generating. That it is the June 2026 state rests on the PI's account of where the files come from.
2. AZ §9 describes `AZ-ART-AZV5-REGISTRY` as covering also `phase2_harness`. The registry does not list it, and `az1b_certify.py` itself fixes the list at these ten files and the phase at "AZ-1A + AZ-1B". The package as found is the state at the AZ-1B gate; a later registry, if one existed, was not received.
3. `CONVENTIONS_FROZEN.md` contains `CONV-AZ-GRAPH-EXPORT`, `DEF-AZ-CORE`, `CONV-AZ-SPECTRUM-MODE`, `CONV-AZ-STATS-MULTITEST`, `CONV-AZ-STATS-DEFS`, `CONV-AZ-NULLS`, `SG-PLAN-5/6/7` and the no-signal template. It does **not** contain `CONV-AZ-ANGLE-ZERO`, which AZ §9 lists for `AZ-ART-CONVENTIONS-FROZEN` and AZ §4.3 attributes to AZ-1C; nor `CONV-AZ-MANIFEST`, which `lib/manifest.py` enforces. The found file is not the frozen state the adopted DSN describes; most simply, it is an earlier one.

## 3. Replay (`EV-CODE`, `EV-RUN`)

`bash evidence/az/az_v5_replay/replay.sh`, from the repository root; output `evidence/az/az_v5_replay/replay_output.txt`. The package is copied to temporary directories first, because `benchmark_ladder.py` writes into `benchmarks/` next to itself and `az1b_certify.py` rewrites the registry there. Environment: Python 3.13.18, numpy 2.5.3, scipy 1.18.1 (the June 2026 environment is not recorded in the received files).

| Script | Result |
|---|---|
| `benchmark_ladder.py` | exit code 0, "AZ-1 GATE: PASS": S1 directed cycles `L = 4, 6, 8`, S2 bidirected cycles `L = 4, 6`, S3 disjoint cycles `(k, L) = (2,4), (3,6)`, S4 bouquet `k = 2, L = 4` by construction, spectral radius `1.189207` (`= 2^{1/4}`, the value AZ §4.3 names for AZ-1A) |
| `validate_solver.py` | exit code 0, "Result: PASS": sparse leading-10 against dense on a 200-edge graph, difference of order `1e-15`; trace moments `m = 1…8` consistent |
| `export/conv_az_graph_export.py` | self-test exit code 0 (6 directed edges in `G_T`, non-empty core, one birth snapshot); `write_export` writes four object files and a manifest whose checksums verify |
| `az1b_certify.py` | exit code 0, "AZ-1B GATE: PASS": independent S2 assertion `L = 4, 6, 8`; JSON loader round-trips, empty graph, six malformed inputs rejected, flagged self-loop and multiedge accepted; non-empty Hashimoto on a both-orientations export and detection of the acyclic case; sparse against dense leading-12 angular error of order `1e-15`; manifest validator (valid passes; odd `N`, non-canonical `B1`, no-null rejected); registry written |

Regenerated files against the deposited originals and the registry:

| File | Finding |
|---|---|
| `benchmarks/az_v5_synthetic_benchmark_report.json` (original **not received**) | the file regenerated by `benchmark_ladder.py` has SHA-256 `e6fd69680b80bb906a84bdb1a82cff806a033af996d51bafdf0e5088fc371a4e`, **equal to the registry entry**. Its content (`S1`–`S4` all `true`) is therefore byte-identical to the missing original. Kept as `evidence/az/az_v5_replay/az_v5_synthetic_benchmark_report.regenerated.json`: a file regenerated on 11 Nov 2026, not the June file |
| `benchmarks/AZ_ARTIFACT_REGISTRY.json` | the registry written by `az1b_certify.py` over the nine deposited originals and the regenerated report is **byte-identical to the deposited registry** (`66867064…875a`) |
| `benchmarks/bouquet_2_4_hashimoto_matrix.json` | `k`, `L`, `edges`, `matrix_size` and `matrix` identical to the deposited original; the eigenvalue lists differ in floating-point noise only (multiset distance below `1e-6`; the matrix has a defective zero eigenvalue of multiplicity four) |
| `benchmarks/bouquet_2_4_charpoly.txt` | nine coefficients, equal within `1e-12`; rounded: `λ⁸ − 2λ⁴` |

The replay output is not byte-reproducible (it prints floating-point residuals); the exit codes, the PASS lines, the report hash and the registry identity are.

**Scope of the AZ-1B replay, and how the exporter meets the package.** AZ §4.3 describes AZ-1B as certifying that "real TDR-G defect-graph exports … ingest, validate, and round-trip with checksums". The deposited `az1b_certify.py` exercises the loader, the export convention and the manifest validator on synthetic graphs and on one example manifest; it reads no TDR-G export. The deposited exporter runs, but as received the two sides do not meet without an adapter: `lib/graphio.load_graph_json` rejects the exporter's object files (they carry `directed_edges`, the loader requires `directed` and `edges`; after that mapping the edges load), and the exporter's manifest is a checksum manifest of schema `tdrg_az_graph_export_v1`, not the run manifest that `lib/manifest.validate_manifest` checks (seven required keys are absent). The piece that joined them — presumably the Phase-2 harness — and any real export were not received. That part of the AZ-1B description is therefore not replayed.

**An inconsistency between two deposited files, recorded and not resolved.** `CONVENTIONS_FROZEN.md` defines `G_birth(w)` as the birth-*window* graph over `[t_first_birth, t_first_birth + w]`, default `w = 200` (and `lib/manifest.py` has an export type `birth_window` with `window_w`); `conv_az_graph_export.py` defines `G_birth(w)` as the snapshot at the tick of the `w`-th birth. Which of the two the Phase-2 work used cannot be read from the received files; the registered Phase-2 results and the smoke report use `Core(G_T)` only. This matters for AZ §4.3.6, which names "the `G_birth(w)` sequence" among the candidate dynamical observables: the object is not uniquely defined by the recovered material.

## 4. The Phase-2 smoke report (`EV-BYTES` only)

`phase2/AZ_PHASE2_N120_NULL1_smoke.json`: one run, `N = 120`, `k = 8`, `bound_symmetric`, `T = 1000`, seed 2, object `Core_G_T` (248 directed edges, full spectrum), 100 reciprocal-pair-preserving nulls, per-`q` table, self-labelled `[NUM diagnostic]`. It is **not** one of the three registered Null1 reports of `AZ-ART-PHASE2-N120-CORE` (1000 nulls, five seeds), carries no hash anchor, and cannot be rerun (the harness is absent).

What it shows, as read from the file: `R_q` observed against null mean — `q = 4`: 0.950 / 0.673; `8`: 0.923 / 0.648; `12`: 0.941 / 0.656; `20`: 0.972 / 0.658; `24`: 0.955 / 0.650 (each at the smallest empirical `p` that 100 nulls allow, 0.0099); `q = 3, 5, 15`: observed below `2·10⁻¹⁵`; `q = 2, 6, 10`: observed below the null mean. This is the pattern AZ §4.3.4 Chain 1 describes (elevated on `4 | q`, silent on `q` with an odd prime factor), at smoke level. By the deposited conventions file, 100 nulls allow `[NUM diagnostic]` only. It corroborates the form of the result and nothing about its later reclassification as substrate geometry (Chain 2). The file's `eps_angle = 1e-10` shows that the angle-zero convention was in use when it was produced, which the deposited `CONVENTIONS_FROZEN.md` does not yet contain (§2, limit 3).

## 5. Custody ledger against AZ §9

| AZ §9 identifier | State after this intake |
|---|---|
| `AZ-ART-AZV5-REGISTRY` | **in the repository at the AZ-1B state.** Registry and nine of its ten entries deposited as original bytes, hash-equal; the tenth regenerated with the registry's hash; AZ-1A ladder, solver acceptance and AZ-1B gate replayed with exit code 0; registry regenerated byte-identically. `phase2_harness`: not in the registry, not received |
| `AZ-ART-AZ1B-CERTIFY` | `az1b_certify.py` deposited, hash-equal, replayed (synthetic scope, §3) |
| `AZ-ART-CONVENTIONS-FROZEN` | a file of that name deposited; it lacks `CONV-AZ-ANGLE-ZERO` and `CONV-AZ-MANIFEST` — not shown to be the frozen state the DSN cites |
| (no §9 identifier) `conv_az_graph_export.py` | deposited; it identifies itself as `[RID: TDRG-AZ-EXPORT-BASELINE]`, an identifier AZ v0.7 does not list; self-test replayed; not joined to the loader by the received bytes (§3) |
| `AZ-ART-PHASE2-N120-CORE` | not received. Only an unregistered smoke report of the same family is deposited (§4) |
| `AZ-ART-SPECTRAL-RADIUS-PATCH`, `AZ-ART-PROP-CORE-EQUIV`, `AZ-ART-ANTIPODAL-LOWORDER`, `AZ-ART-THETA-CORE-MATCHED`, `AZ-ART-ZETA-V3` | not received; unchanged: source-reported only (`EV-SRC-REPORTED`, `EV-NOT-RERUN`) |

Held, not deposited: `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0_5.md`, SHA-256 `fe9be4031baed86769ec7289e1bcddaa93bfd0136fd6727f3d247405b18802bb`, 66,428 bytes — a superseded edition without authority; it predates the `az_v5` work and names no registry or hash, and the tagged v0.6 records no hash of it.

## 6. What this changes and what it does not

- It does not change AZ v0.7. §9's sentence that none of the files is in the repository is true of the adopted edition and becomes outdated when the upload is merged; the correction belongs to the next AZ edition, with the PI's decision.
- It supports, by reruns on current libraries, the AZ-1A and (in its synthetic scope) AZ-1B parts of the engineering certification for the deposited bytes. It says nothing about AZ-1C, `PROP-AZ-CORE-EQUIV`, the low-order obstruction, the spectral-radius patch or the Phase-2 diagnostics: their certificates are still absent, and `TDRG-AZ-STATIC-ZN-4Q` stays source-reported.
- Nothing here bears on AZ Action 1 (token resonance), which does not use `az_v5`.

## 7. Open

1. For the next AZ edition, with the PI: the status of `conv_az_graph_export.py` and of its identifier `TDRG-AZ-EXPORT-BASELINE`; the two definitions of `G_birth(w)` (§3).
2. The later states — `CONVENTIONS_FROZEN.md` with `CONV-AZ-ANGLE-ZERO`, a registry with `phase2_harness`, the Phase-2 harness, runner and the three registered Null1 reports, the core-matched null report, the core-equivalence prover and certificates, the spectral-radius patch, `THM_AZ_ANTIPODAL_4Q.md`: missing.
3. Merge order: the upload PR first (custody), then this record with the replay files.
