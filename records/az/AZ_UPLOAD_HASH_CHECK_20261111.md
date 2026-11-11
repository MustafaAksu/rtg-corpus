# AZ Thread C (`az_v5`) partial recovery — hash check and replay

**Date:** 11 November 2026. **By:** Claude, AZ co-owner. **[SESSION]** custody record.
**Evidence keys:** `EV-BYTES`, `EV-HASH`, `EV-CODE`, `EV-RUN` as stated per item. No owner decision is made, no DSN is edited, no grade changes. What AZ v0.7 §9 says about availability stays as adopted until a later AZ edition.

## 1. What arrived

The PI attached eleven files to this session (11 Nov 2026, 16:53 +03:00), found after the AZ v0.7 release record (§14) listed the Thread C evidence as absent. On the PI's instruction ("bu dosyalardan lazımlı olanları repoya yükleyelim. sana bu konuda tam yetki", 16:41 +03:00) eight of them were pushed unchanged to `upload/az-v5-partial-recovery-20261111`, commit `10426f7`, directory `upload/az-records/`; two were byte-identical duplicates; one is held. The branch had been created by the ChatGPT co-owner session and carried no commit of its own before. Intake manifest: `upload/az-records/INTAKE_MANIFEST.md`.

## 2. Hash check (`EV-BYTES`, `EV-HASH`)

All hashes recomputed here from the bytes on the branch; the staged Git blobs were compared with the attached files before the commit (`.gitattributes` is `* -text`).

| File under `upload/az-records/` | SHA-256 | Against `az_v5/AZ_ARTIFACT_REGISTRY.json` |
|---|---|---|
| `az_v5/AZ_ARTIFACT_REGISTRY.json` | `6686706490c0f4d1d90629aaf6594176faff333096d4b0e3834128ff75ba875a` | the registry: ten entries, `version: az_v5`, `phase: AZ-1A + AZ-1B` |
| `az_v5/lib/hashimoto.py` | `9cc2137936bd43b2dcf02c4ffd4c5c039527076a9891edecea33d13abd5f1b70` | equal |
| `az_v5/lib/graphgen.py` | `6bd34a917ec32ef3091ed0a70ad4c81ac176932efc29b4cb478d9d7b3058d4b8` | equal |
| `az_v5/benchmark_ladder.py` | `d771dfa2cbdefe23b780dc21c42df60d6cdf951e2ed59bd3f831f947ff2a4352` | equal |
| `az_v5/validate_solver.py` | `50ff52e10f32cb553671a0c2d14fdba7daf2f1be18168112692b8cd7a69879ec` | equal |
| `az_v5/benchmarks/bouquet_2_4_hashimoto_matrix.json` | `4c377fa704e8b08e648caf3baff516f97bb5551cafc17506d7a560501347ca01` | equal |
| `az_v5/benchmarks/bouquet_2_4_charpoly.txt` | `6a6979b0d25b8a314f524a35a8f7114848701d4486f70b0a029b1c3313db788f` | equal |
| `CONVENTIONS_FROZEN.md` | `1c4b715aea0785c22c2f194d9cf8ba6a1b3c76dc2608366dedd58160ed478f2d` | not a registry entry |

Six of the ten registry entries are present and equal. Not received by this session: `lib/graphio.py`, `lib/manifest.py`, `az1b_certify.py`, `benchmarks/az_v5_synthetic_benchmark_report.json`. The ChatGPT session reported seven matches, the seventh being `az1b_certify.py`, and a further file `conv_az_graph_export.py` outside the registry; neither reached this session, so both are unverified here.

**Limits of the identification.**
1. No adopted document records the registry's own hash. The check shows that the found set agrees with the found registry; it does not show, by itself, that the registry is the June 2026 original.
2. AZ §9 describes `AZ-ART-AZV5-REGISTRY` as covering also `phase2_harness`; the found registry does not list it and declares the phase "AZ-1A + AZ-1B". It is an earlier state of the registry than the one §9 describes, or §9's description is wider than the registry was.
3. `CONVENTIONS_FROZEN.md` contains `CONV-AZ-GRAPH-EXPORT`, `DEF-AZ-CORE`, `CONV-AZ-SPECTRUM-MODE`, `CONV-AZ-STATS-MULTITEST`, `CONV-AZ-STATS-DEFS`, `CONV-AZ-NULLS`, `SG-PLAN-5/6/7` and the no-signal template. It does **not** contain `CONV-AZ-ANGLE-ZERO`, which AZ §9 lists for `AZ-ART-CONVENTIONS-FROZEN` and AZ §4.3 attributes to AZ-1C. The found file is therefore not the frozen state the adopted DSN describes; most simply, it is the state before AZ-1C.

## 3. Replay (`EV-CODE`, `EV-RUN`)

`bash evidence/az/az_v5_replay/replay.sh`, from the repository root; output `evidence/az/az_v5_replay/replay_output.txt`. The package is copied to a temporary directory first, because `benchmark_ladder.py` writes into `benchmarks/` next to itself. Environment: Python 3.13.18, numpy 2.5.3, scipy 1.18.1 (the June 2026 environment is not recorded in the received files).

| Script | Result |
|---|---|
| `benchmark_ladder.py` | exit code 0, "AZ-1 GATE: PASS": S1 directed cycles `L = 4, 6, 8`, S2 bidirected cycles `L = 4, 6`, S3 disjoint cycles `(k, L) = (2,4), (3,6)`, S4 bouquet `k = 2, L = 4` by construction, spectral radius `1.189207` (`= 2^{1/4}`, the value AZ §4.3 names for AZ-1A) |
| `validate_solver.py` | exit code 0, "Result: PASS": sparse leading-10 against dense on a 200-edge graph, difference of order `1e-15`; trace moments `m = 1…8` consistent |

Regenerated benchmark files against the deposited originals and the registry:

| File | Finding |
|---|---|
| `benchmarks/az_v5_synthetic_benchmark_report.json` (original **not received**) | the regenerated file has SHA-256 `e6fd69680b80bb906a84bdb1a82cff806a033af996d51bafdf0e5088fc371a4e`, **equal to the registry entry**. Its content (`S1`–`S4` all `true`) is therefore byte-identical to the missing original. Kept as `evidence/az/az_v5_replay/az_v5_synthetic_benchmark_report.regenerated.json`: a file regenerated on 11 Nov 2026, not the June file |
| `benchmarks/bouquet_2_4_hashimoto_matrix.json` | `k`, `L`, `edges`, `matrix_size` and `matrix` identical to the deposited original; the eigenvalue lists differ in floating-point noise only (multiset distance below `1e-6`; the matrix has a defective zero eigenvalue of multiplicity four) |
| `benchmarks/bouquet_2_4_charpoly.txt` | nine coefficients, equal within `1e-12`; rounded: `λ⁸ − 2λ⁴` |

The replay output is not byte-reproducible (it prints floating-point residuals); the exit codes, the PASS lines and the report hash are.

## 4. Custody ledger against AZ §9

| AZ §9 identifier | State after this intake |
|---|---|
| `AZ-ART-AZV5-REGISTRY` | **partly in the repository.** Registry file and six of its ten entries deposited and hash-equal; AZ-1A synthetic ladder and solver acceptance replayed (§3). Benchmark report: content recovered by regeneration with the registry's hash. Missing: `lib/graphio.py`, `lib/manifest.py`; `az1b_certify.py` reported held by the ChatGPT session, not received here. `phase2_harness`: not in the found registry, not received |
| `AZ-ART-CONVENTIONS-FROZEN` | a file of that name deposited; it lacks `CONV-AZ-ANGLE-ZERO` (§2, limit 3) — not shown to be the frozen state the DSN cites |
| `AZ-ART-AZ1B-CERTIFY` | not received here; **AZ-1B** (ingestion, export, provenance) cannot be replayed: it needs `graphio.py`, `manifest.py` and `az1b_certify.py` |
| `AZ-ART-SPECTRAL-RADIUS-PATCH`, `AZ-ART-PROP-CORE-EQUIV`, `AZ-ART-ANTIPODAL-LOWORDER`, `AZ-ART-PHASE2-N120-CORE`, `AZ-ART-THETA-CORE-MATCHED`, `AZ-ART-ZETA-V3` | not received; unchanged: source-reported only (`EV-SRC-REPORTED`, `EV-NOT-RERUN`) |

Held, not deposited: `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0_5.md`, SHA-256 `fe9be4031baed86769ec7289e1bcddaa93bfd0136fd6727f3d247405b18802bb`, 66,428 bytes — a superseded edition without authority; it predates the `az_v5` work and names no registry or hash, and the tagged v0.6 records no hash of it.

## 5. What this changes and what it does not

- It does not change AZ v0.7. §9's sentence that none of the files is in the repository is true of the adopted edition and becomes outdated when the upload is merged; the correction belongs to the next AZ edition, with the PI's decision.
- It supports, by a rerun on current libraries, the AZ-1A part of the engineering certification (`[ENG PASS]`, synthetic engine) for the deposited bytes. It says nothing about AZ-1B, AZ-1C, `PROP-AZ-CORE-EQUIV`, the low-order obstruction or the Phase-2 diagnostics: their certificates are still absent.
- Nothing here bears on AZ Action 1 (token resonance), which does not use `az_v5`.

## 6. Open

1. `az1b_certify.py` and `conv_az_graph_export.py`: the ChatGPT session reports having them. If the PI attaches them, they are hash-checked and added to the same upload directory.
2. `lib/graphio.py`, `lib/manifest.py`: missing. Without them the AZ-1B certification is not reproducible from the repository.
3. The later state of `CONVENTIONS_FROZEN.md` (with `CONV-AZ-ANGLE-ZERO`) and of the registry (with `phase2_harness`), and every Phase-2 artifact: missing.
4. Merge order: the upload PR first (custody), then this record with the replay files.
