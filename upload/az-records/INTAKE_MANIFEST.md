# AZ Thread C (`az_v5`) — partial recovery, intake manifest

**Intake date:** 11 November 2026. **Written by:** Claude (AZ co-owner session); this manifest and `SHA256SUMS` are the session's, everything else in this directory is an unchanged outside file.
**Source:** eleven files the PI attached to the AZ co-owner session on 11 Nov 2026, 16:53 +03:00, found on his side after the AZ v0.7 release record (§14) listed the Thread C evidence as absent. The same files had first been given to the ChatGPT co-owner session, whose upload to this branch did not arrive (the branch existed without any commit of its own).
**Authority for the push:** PI, 11 Nov 2026, 16:41 +03:00: "bu dosyalardan lazımlı olanları repoya yükleyelim. sana bu konuda tam yetki." CONVENTIONS §6 otherwise restricts Claude sessions to `claude/*` branches; this push to an `upload/*` branch is made under that instruction and is declared here.

## Deposited unchanged (exact bytes as attached)

The files arrived with flat names. The paths under `az_v5/` are **reconstructed from the keys of `AZ_ARTIFACT_REGISTRY.json`**, which is also the layout the scripts expect (`lib/` and `benchmarks/` next to them); the bytes are untouched.

| Path in this directory | SHA-256 | Registry entry |
|---|---|---|
| `az_v5/AZ_ARTIFACT_REGISTRY.json` | `6686706490c0f4d1d90629aaf6594176faff333096d4b0e3834128ff75ba875a` | the registry itself (`version: az_v5`, `phase: AZ-1A + AZ-1B`); its own hash is recorded nowhere in the repository; its place inside the package is not known |
| `az_v5/lib/hashimoto.py` | `9cc2137936bd43b2dcf02c4ffd4c5c039527076a9891edecea33d13abd5f1b70` | equal |
| `az_v5/lib/graphgen.py` | `6bd34a917ec32ef3091ed0a70ad4c81ac176932efc29b4cb478d9d7b3058d4b8` | equal |
| `az_v5/benchmark_ladder.py` | `d771dfa2cbdefe23b780dc21c42df60d6cdf951e2ed59bd3f831f947ff2a4352` | equal |
| `az_v5/validate_solver.py` | `50ff52e10f32cb553671a0c2d14fdba7daf2f1be18168112692b8cd7a69879ec` | equal |
| `az_v5/benchmarks/bouquet_2_4_hashimoto_matrix.json` | `4c377fa704e8b08e648caf3baff516f97bb5551cafc17506d7a560501347ca01` | equal |
| `az_v5/benchmarks/bouquet_2_4_charpoly.txt` | `6a6979b0d25b8a314f524a35a8f7114848701d4486f70b0a029b1c3313db788f` | equal |
| `CONVENTIONS_FROZEN.md` | `1c4b715aea0785c22c2f194d9cf8ba6a1b3c76dc2608366dedd58160ed478f2d` | not a registry entry (AZ §9 names it as `AZ-ART-CONVENTIONS-FROZEN`, without a hash) |

Duplicates received and not deposited twice: a second copy of `hashimoto.py` and a second copy of `CONVENTIONS_FROZEN.md`, each byte-identical to the deposited one (same SHA-256).

## Not deposited

| File | State |
|---|---|
| `lib/graphio.py` (`4dcb9131…f6d8`), `lib/manifest.py` (`ea845088…0ec5`) | registry entries; **not received**; missing |
| `az1b_certify.py` (`7a0f8aa5…c02b`) | registry entry; **not received by this session** (the ChatGPT session reported having a copy that matches the registry: unverified here) |
| `benchmarks/az_v5_synthetic_benchmark_report.json` (`e6fd6968…a4e`) | registry entry; **not received**. See `records/az/AZ_UPLOAD_HASH_CHECK_20261111.md`: running the deposited `benchmark_ladder.py` regenerates a file with exactly this hash; a regenerated file is not the original |
| `conv_az_graph_export.py` | named by the ChatGPT session as present on its side and absent from the registry; **not received by this session** |
| `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0_5.md` | received (SHA-256 `fe9be4031baed86769ec7289e1bcddaa93bfd0136fd6727f3d247405b18802bb`, 66,428 bytes); **held, not deposited**: a superseded DSN edition without authority, which predates the `az_v5` work and names no registry or hash; the tagged v0.6 names it as its predecessor but records no hash of it. It can be deposited later if the PI wants the pre-Git history kept |

Everything else AZ §9 names (`phase2_harness`, `spectral_radius_patch.py`, `prove_core_equiv.py` and its certificates, `THM_AZ_ANTIPODAL_4Q.md`, the Phase-2 runner and the three Null1 reports, `AZ_THETA_CORE_MATCHED.json`, `rtg_graph_zeta_proto_v3.py`) was not received.

## Custody limits

- The hashes are checked against a registry that was found together with the files. The match shows that this set is internally consistent with that registry; it does not, by itself, show that the registry is the June 2026 original, since no adopted document records the registry's hash.
- The registry covers the phase "AZ-1A + AZ-1B" and has ten entries. AZ §9 describes `AZ-ART-AZV5-REGISTRY` as also covering `phase2_harness`, which this registry does not list: this file is either an earlier state of the registry or the description in §9 is wider than the registry was.
- **Do not run the scripts in place.** `benchmark_ladder.py` writes into `benchmarks/` next to itself and would overwrite the two deposited originals. Replay from a copy (`evidence/az/az_v5_replay/replay.sh` does that).

**Governance:** untouched intake evidence. Nothing here edits `dsn/`, raises a grade or changes what AZ v0.7 states about availability; that is for a later AZ edition and the PI.
