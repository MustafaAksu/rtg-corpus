# AZ Thread C (`az_v5`) — recovery, intake manifest

**Intake dates:** 11 November 2026, two deliveries. **Written by:** Claude (AZ co-owner session); this manifest and `SHA256SUMS` are the session's, everything else in this directory is an unchanged outside file.
**Source:** files the PI attached to the AZ co-owner session, found on his side after the AZ v0.7 release record (§14) listed the Thread C evidence as absent: eleven files at 16:53 +03:00 (first commit, `10426f7`) and four at 17:07 +03:00 (second commit). The first files had earlier been given to the ChatGPT co-owner session, whose upload to this branch did not arrive (the branch existed without any commit of its own).
**Authority for the push:** PI, 11 Nov 2026, 16:41 +03:00: "bu dosyalardan lazımlı olanları repoya yükleyelim. sana bu konuda tam yetki." CONVENTIONS §6 otherwise restricts Claude sessions to `claude/*` branches; the pushes to this `upload/*` branch are made under that instruction and are declared here.

## Deposited unchanged (exact bytes as attached)

The files arrived with flat names. The paths under `az_v5/` are those of the registry keys, which is the layout the scripts expect (`lib/` and `benchmarks/` next to them). The registry itself is placed at `az_v5/benchmarks/AZ_ARTIFACT_REGISTRY.json`, the path to which `az1b_certify.py` writes it (the first commit had it one level higher, before that script was received; same bytes). Bytes are untouched.

| Path in this directory | SHA-256 | Registry entry |
|---|---|---|
| `az_v5/benchmarks/AZ_ARTIFACT_REGISTRY.json` | `6686706490c0f4d1d90629aaf6594176faff333096d4b0e3834128ff75ba875a` | the registry itself (`version: az_v5`, `phase: AZ-1A + AZ-1B`, ten entries); its own hash is recorded in no adopted document |
| `az_v5/lib/hashimoto.py` | `9cc2137936bd43b2dcf02c4ffd4c5c039527076a9891edecea33d13abd5f1b70` | equal |
| `az_v5/lib/graphgen.py` | `6bd34a917ec32ef3091ed0a70ad4c81ac176932efc29b4cb478d9d7b3058d4b8` | equal |
| `az_v5/lib/graphio.py` | `4dcb913118fb2b7f3d7619c7c35ee992cfb07728a9af83004717bc049f76f6d8` | equal (second delivery) |
| `az_v5/lib/manifest.py` | `ea845088f74992c34a8c673693daa41f1d22b5df7b354e42e9fd0571a72d0ec5` | equal (second delivery) |
| `az_v5/benchmark_ladder.py` | `d771dfa2cbdefe23b780dc21c42df60d6cdf951e2ed59bd3f831f947ff2a4352` | equal |
| `az_v5/validate_solver.py` | `50ff52e10f32cb553671a0c2d14fdba7daf2f1be18168112692b8cd7a69879ec` | equal |
| `az_v5/az1b_certify.py` | `7a0f8aa5b9aa5e6debd3510c3c6e330b68bb15632ab1cbe8d0dfacddb1bcc02b` | equal (second delivery) |
| `az_v5/benchmarks/bouquet_2_4_hashimoto_matrix.json` | `4c377fa704e8b08e648caf3baff516f97bb5551cafc17506d7a560501347ca01` | equal |
| `az_v5/benchmarks/bouquet_2_4_charpoly.txt` | `6a6979b0d25b8a314f524a35a8f7114848701d4486f70b0a029b1c3313db788f` | equal |
| `CONVENTIONS_FROZEN.md` | `1c4b715aea0785c22c2f194d9cf8ba6a1b3c76dc2608366dedd58160ed478f2d` | not a registry entry (AZ §9 names it as `AZ-ART-CONVENTIONS-FROZEN`, without a hash) |
| `phase2/AZ_PHASE2_N120_NULL1_smoke.json` | `561c66ac8e5d359d5806d9aa058e988b682412ddb4a84e71371e754e89e22284` | not a registry entry and not one of the registered Phase-2 reports: a **smoke** output (one seed, `T = 1000`, 100 nulls, self-labelled `[NUM diagnostic]`); second delivery |

Nine of the ten registry entries are deposited as original bytes. Duplicates received and not deposited twice: a second copy of `hashimoto.py` and a second copy of `CONVENTIONS_FROZEN.md`, each byte-identical to the deposited one.

## Not deposited

| File | State |
|---|---|
| `benchmarks/az_v5_synthetic_benchmark_report.json` (`e6fd6968…a4e`) | the tenth registry entry; **original not received**. Running the deposited `benchmark_ladder.py` regenerates a file with exactly this hash (`records/az/AZ_UPLOAD_HASH_CHECK_20261111.md`); the regenerated file is kept under `evidence/az/az_v5_replay/` and is not the original |
| `conv_az_graph_export.py` | named by the ChatGPT session as present on its side and absent from the registry; **not received by this session** |
| `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0_5.md` | received (SHA-256 `fe9be4031baed86769ec7289e1bcddaa93bfd0136fd6727f3d247405b18802bb`, 66,428 bytes); **held, not deposited**: a superseded DSN edition without authority, which predates the `az_v5` work and names no registry or hash; the tagged v0.6 names it as its predecessor but records no hash of it. It can be deposited later if the PI wants the pre-Git history kept |

Everything else AZ §9 names (`phase2_harness`, `spectral_radius_patch.py`, `prove_core_equiv.py` and its certificates, `THM_AZ_ANTIPODAL_4Q.md`, the Phase-2 runner and the three registered Null1 reports, `AZ_THETA_CORE_MATCHED.json`, `rtg_graph_zeta_proto_v3.py`) was not received.

## Custody limits

- The hashes are checked against a registry that was found together with the files, and no adopted document records the registry's hash. The replay shows more than agreement: the deposited `az1b_certify.py`, run over the deposited files, writes a registry that is byte-identical to the found one. The set is therefore self-consistent and self-generating; that it is the June 2026 state rests on the PI's account of where the files come from.
- The registry covers the phase "AZ-1A + AZ-1B". AZ §9 describes `AZ-ART-AZV5-REGISTRY` as also covering `phase2_harness`, which this registry does not list: it is an earlier state than the one §9 describes, or §9's description is wider than the registry was.
- **Do not run the scripts in place.** `benchmark_ladder.py` writes into `benchmarks/` next to itself and would overwrite deposited originals; `az1b_certify.py` rewrites the registry there. Replay from a copy (`evidence/az/az_v5_replay/replay.sh` does that).

**Governance:** untouched intake evidence. Nothing here edits `dsn/`, raises a grade or changes what AZ v0.7 states about availability; that is for a later AZ edition and the PI.
