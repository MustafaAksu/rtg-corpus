# TRIAD — source recovery list

**Date:** 30 October 2026. **Prepared by:** Claude (Triadic co-owner). **Status:** working record at a fixed path; updated as files arrive.
**Source of the list:** every file name cited in `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` at `triad-v1.6.1` (64 backticked names, mostly from §8 and the header), checked against the repository tree on 30 October 2026, plus the intake check `records/triad/TRIAD_UPLOAD_HASH_CHECK_20261030.md`.
**States** (reconciliation rows 25–28, ChatGPT's five states): **P** placed and hash-verified · **H** held by the PI, not in the repository · **K** hash recorded, bytes missing · **S** session-only or unrecoverable · **F** scaffold or placeholder.

**Goal.** Anyone using the repository can test every Triadic claim from the repository alone. A missing file here does not mean the work was not done; it means its evidence is not independently inspectable from the repository. Missing files are cited as missing and are **not reconstructed**. They do not block v1.7 content decisions and are no reason to regrade an existing claim.

**How to deliver.** Upload files unchanged to an `upload/triad-…` branch (CONVENTIONS §6). A co-owner checks each SHA-256 against the value below where one is recorded, places scripts under `evidence/triad/scripts/`, records under `records/triad/`, packages under `evidence/triad/` as received, and updates this list and, at the next release, the §8 entries.

## P — placed and hash-verified

| File | Where | SHA-256 | DSN |
|---|---|---|---|
| `OWNER_ADOPTION_v1_6_1.json` | `records/triad/` (from `upload/triad-records`, `2a1a4a8`) | `33bcd3cea83b467d0bc4d8cc4a37c10771cd81151831caec87c55873937cd5dd` | header (adoption records) |
| `RELEASE_RECORD_v1_6_1.md` | `records/triad/` (same) | `aa3d8d773a2083908f2e576bc59f9c6d3c110c1caadbc70782c72b07e95eb45d` | header |
| `tetrahedral_six_step_cross_phase_t6c2_patched.py` | `evidence/triad/scripts/` (from commit `9df0319`) | `afb4525ccc2f459964fc3e9acade004f2aa61c03be2366f125cef63fc466d80e` | TRIAD-ART-T6C-CROSSPHASE |
| `triad_analytic_phase_steering_t6l_patched.py` | `evidence/triad/scripts/` (same) | `2e0317bf90332d1fe0ab7489710a3c8c67b772e3031dd7ef95b3163f7d7a11cd` | TRIAD-ART-T6L-TORSION (rerun 30 Oct 2026; output in `evidence/triad/v1.7/`) |

## H — held by the PI, not in the repository

The v1.6 accepted evidence package `evidence/accepted_r4_2/` (DSN header, "Evidence location"). Cited members, with the hash where the DSN prints one:

| File | DSN locator | Recorded SHA-256 |
|---|---|---|
| `triad_t6_producers.zip` (25 producer scripts; `SHA256_MANIFEST.csv` inside) | TRIAD-ART-T6-ORIENTATION-NORMALIZATION-V16 | `8ad574ff97938b3dac8f79f68bca0458bc0e768b3fdf5a12c46a28fafd98de69` |
| `t6c2_out.json` (fresh T-6c2 output, UTF-16LE) | same | `82451781d45e2af2bff311656b2046b02fad767ed1c2e2f5901766bd507aa414` |
| `t6e_out.json` (fresh T-6e output, UTF-16LE) | same | `288cd77da617a12022350f7902c01a1f4d02565298b84e101becb108f6e241db` |
| `triad_orientation_normalization_audit.py` (15 checks) | same | `d5c0f698232cca6c2fe5d8321249e5d93f9bfe2c5288c7f918c3ef55d89a0e29` |
| `scripts/triad_torsion_object_check_r4_2.py` | same | `bd9ae5d5bf8ecc598b99a12f1a061d04715e5abe7a971e7ff96aa0b6930b773e` |
| `tetrahedral_six_step_omega_t6e.py` (holds the T-6e polynomials $H_0,H_1,H_2$) | TRIAD-ART-T6E-OMEGA | `98e4b0b033c2592b6a084006ab51283092238f291f5b455f1aa2e23b7af82d59` |
| `triad_safe_arc_basin_search_t6j.py` | TRIAD-ART-T6J-BASIN | `5b75db2d7c4663402a7bd068d141e49ae49aac705e1c3d29024f75af29bbf697` |
| `t6b_orthogonal_ode.py`, `t6d_generalized_ode.py`, `triad_direct_orientation_ode_t6f_v2.py`, `triad_free_qc_dimensionless_ode_t6h_v2.py`; the T-6i/i2 and T-6k/k2 producers | TRIAD-ART-T6B/T6D/T6F/T6H-ODE, T6I-MAP, T6K-STEER | not recorded |
| `inputs/historical/triad_t6s_chirality.py` | TRIAD-ART-T6S-CHIRALITY | `0eb2fd1bf5ff3d44612b42428ee3285637ed09fbedc0585621daa55b69f325dc` |
| `inputs/historical/triad_thread4_chirality_count.py` | TRIAD-ART-T6T-CHIRALITY | `e0718a25fa8d18338cb55d8fd84b13b17d72ecf6d1f5bd06a79b4b36a7afc909` |
| `inputs/historical/triad_t6u_apex_source.py` | TRIAD-ART-T6U-APEX-SOURCE | `435cf09964850626b08c6d7c59f6f93401cced554eff0cb023ce8f27cc96762f` |
| `triad_t6u_apex_source_v1_6.py` (47 assertions), `triad_v1_6_r2_point_use_checks.py`, `triad_v1_6_r3_scope_checks.py`, `validate_r3.py`, `scripts/run_all.py`, `T6U_PROOF_AND_SCOPE.md`, `t6u_certificate.json`, `environment.json` | TRIAD-ART-T6U-APEX-SEED-DIAGNOSTIC-V16 | in `evidence/FILE_IDENTITIES.json` (not in the repository) |
| `evidence/EXECUTION_MANIFEST.json`, `evidence/EXECUTION_MANIFEST_R4_2.json`, `evidence/FILE_IDENTITIES.json`, `RECOVERED_HISTORICAL_RUNS.json` | §8 | not recorded in the DSN |

Also with the PI:
- **The remaining 9 files of the v1.6.1 release package** (the DSN and its two drafts, `release_v1_6_1.py`, `check_release_v1_6_1.py`, the draft build and check scripts, the edits JSON, the diff). The ZIP `TRIAD_v1_6_1_RELEASE_PACKAGE_20261019.zip` is with the PI (intake manifest). The listed DSN hash equals `triad-v1.6.1`; the draft hashes are DRAFT r1 `31b87c3e…30ea` and DRAFT r2 `dd67907f…b3e7` (DSN header).
- **The v1.6 records:** `records/OWNER_ADOPTION.json`, `records/RELEASE_RECORD.md`, `records/METADATA_EDITS.json`. These are history only and are not needed to adopt v1.7.

## K — hash recorded, bytes missing (location not stated)

| File | Recorded SHA-256 |
|---|---|
| `RTG_TRIADIC_BIRTH_LIFT_DSN_v1_6.md` | `c768687cec6d52ffd358dc362cee4348f076160943564adaa461e6c7c4595b36` |
| `RTG_TRIADIC_BIRTH_LIFT_DSN_v1_5.md` | `07e9f00b818950c70d3e51e8f3b65fd1e79922074211d0f0b20d400f8c45b735` |
| v1.6 accepted r4.2 candidate | `420eaf3e0b98ee150d4a44de805480ae05764f6bdcac753a9c73e14e0e5a9bf0` |

Without the v1.5 and v1.6 files the v1.6 phrase "all 49 RIDs" cannot be checked; v1.6.1 declares 46 (§9 of v1.7).

## S — session-only or unrecoverable

- **T-6j2 session script and event log** (TRIAD-ART-T6J2-PROXY): never archived; the terminal event cannot be reconstructed (DSN §6.13).
- **T-6m session computation** (TRIAD-ART-T6M-BIRTH): no standalone script; canonical computation in a session log.
- **`apex_ratio_setup.py`** (consumer-side verification) and **`genesis_k4_route_census.py`** (Genesis-owned): stated unavailable in the package.
- **`dyad_triad_antisymmetric_bridge_v1_1.md`** (Dyadic intermediary bridge note): stated not in the package.
- **Review records named in Appendix A** (`TRIAD_D3_RECEIVING_REVIEW_20261019.md`, `TRIAD_RER_R2_R41_RECEIVING_REVIEW_20261019.md`): not in the repository; location not stated.

## F — scaffold or placeholder

- **`triad_t3a_arb_enclosure_v4g.cpp`** (`upload/dyad-sources/rtg-engine/`): PI-supplied scaffold, **not a certificate** (forcing placeholder 0, dummy $Q_c$ step, yet prints CERTIFIED). No Triadic claim cites it.
- **"Proof-source reference required"** placeholders: TRIAD-ART-T1-K3-PUMP, TRIAD-ART-T2B-DIAG-BIRTH, TRIAD-ART-T4H-ESCAPE, TRIAD-ART-T6A-RETURN, TRIAD-ART-T6G-SQUARES.

## Companion editions cited as historical pins

Available by tag: Programme v1.2 (`programme-v1.2`), TDR-G v2.12.13 (`tdrg-v2.12.13`), Methodology v1.3 (`methodology-v1.3`), OPEN-M v0.7.1 (`uvm-v0.7.1`). Not tagged in the repository: Genesis v2.8.7, Dyadic v6.4.13, OFN v0.9, RRF v0.8.2. The proof imports that v1.7 repins were re-read at the governing tags (DSN §7.1–§7.2); the two held pins say why.
