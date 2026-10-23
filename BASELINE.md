# Baseline manifest

Baseline completed 22 October 2026. Every file is stored byte-exact; the SHA-256 below is the hash of the file in this repository.

**Verification column:**
- **OWNER** — matches the full hash in the owner's own release/adoption record.
- **XREF** — matches a hash recorded by another stream (full, or short form `xxxxxxxx…yyyy`), as named.
- **PI** — supplied by the PI; no independent recorded hash was found. This hash is now the reference for the file.

## Canonical DSNs and standards (`dsn/`)

| Study | File | Version | SHA-256 | Verification | Tag |
|---|---|---|---|---|---|
| Methodology | `DSN_METHODOLOGY.md` | v1.4 | `cdacab5feb79161cd86313086065ca67313ef354e30ceaf205386cf2f3a0f2df` | OWNER: release record `records/methodology/DSN_METHODOLOGY_v1.4_RELEASE_RECORD.md` | `methodology-v1.4` |
| Programme | `RTG_PROGRAMME_OVERVIEW.md` | v1.2 | `4207da05dca24256e7bc528cb9814f848838bcd98e3d01222fb2a633ec9fd359` | XREF: RRF v0.7 §10 | `programme-v1.2` |
| DYAD | `RTG_DYADIC_OSCILLATOR_DSN.md` | v6.4.22 | `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29` | OWNER: release record `records/dyad/RTG_DYADIC_v6_4_22_RELEASE_RECORD.md`; change-focused review (PR #9) | `dyad-v6.4.22` (v6.4.21: `a412f34d…dc7d`, `dyad-v6.4.21`; v6.4.20: `0b2d5a44…4852`, `dyad-v6.4.20`; v6.4.19: `dyad-v6.4.19`) |
| TRIAD | `RTG_TRIADIC_BIRTH_LIFT_DSN.md` | v1.6.1 | `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f` | XREF: RER v0.2 §7 (`TRIAD161`, byte-verified there) | `triad-v1.6.1` |
| GEN | `RTG_GENESIS_GEOMETRY_DSN.md` | v2.8.9 | `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` | XREF: OFN v0.10 IMP-O10-01 (`d143673e…c6fc`) | `gen-v2.8.9` |
| TDRG | `RTG_DISCRETE_GENESIS_DSN.md` | v2.12.13 | `aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f` | XREF: RER v0.2 §7 | `tdrg-v2.12.13` |
| RECOG | `RTG_RELATIONAL_RECOGNITION_DSN.md` | v0.3.22 | `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` | XREF: RER v0.2 G9 (`0dcce9e4…bcd9`) | `recog-v0.3.22` |
| NUMGEN | `RTG_NUMBER_GENESIS_DSN.md` | v1.20.8 | `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e` | XREF: DYAD v6.4.20 §7 (project copy hashed by DYAD) | `numgen-v1.20.8` |
| OFN | `RTG_ONTOLOGICAL_FOUNDATIONS.md` | v0.10 | `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa` | XREF: RECOG v0.3.22 header (`acb70a8c…5dfa`) | `ofn-v0.10` |
| UVM (OPEN-M) | `RTG_OPEN_M_DSN.md` | v0.7.1 | `0a51644de0a15035797ab03945207cf319fd6d7514a04b8cae441d9d6e93f53e` | XREF: RER v0.2 §7 | `uvm-v0.7.1` |
| RRF | `RTG_RRF_REPRESENTATION_REGISTRY.md` | v0.8.4 | `2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce` | XREF: RER v0.2 §7 (byte-verified, Phase A r19) | `rrf-v0.8.4` |
| DZT | `RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md` | v0.8 | `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2` | PI | `dzt-v0.8` |
| AZ | `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` | v0.6 | `dec78a4721d2f34711218d9b79ba0ce6438523060098f770cad5dd3f5eb70b8a` | PI | `az-v0.6` |
| Legacy | `RTG_L0_L1_L2_BRIDGE_LEGACY_DSN.md` | v0.7 | `3b707c90eb5e048717513c6ba161b738d0d1d4cd341eb0a125fb15779afd7e13` | PI | `legacy-v0.7` |
| Pre-Legacy | `RTG_PRE_LEGACY_DSN.md` | v0.8 | `22ecf37869cd1192b7fc3a13efe364d6cc2644928f4ecf5afe38e0ad8b95a446` | PI | `prelegacy-v0.8` |

The table lists the **governing adopted editions**. Predecessor: Methodology v1.3, `3e23ba94…ec7e`, tag `methodology-v1.3`.

## Noncanonical registries and studies (`noncanonical/`)

| Study | File | Version | SHA-256 | Verification | Tag |
|---|---|---|---|---|---|
| RER | `RTG_RELATIONAL_EMERGENCE_REGISTRY.md` | v0.2 ADOPTED (noncanonical) | `58feee5ff1f16a37fc4ee029f24499928ea7439731de0a090d8794c1cbe57ad0` | PI | `rer-v0.2` |
| ER-2B | `RTG_ER2B_CONSOLIDATED_STUDY.md` | v0.3 | `80669c69ada042230c36883f5f1de7a0738e637793a4d1cf4b590990da57a134` | PI | `er2b-v0.3` |
| FMS | `FMS_MODEL_SELECTION_LEDGER.md` | v0.6.4 (session) | `d6313b707464da7ae016662e32fc366981cae9cc5335033129acfcce515d3984` | PI | `fms-v0.6.4` |

## Not yet in the repository

Release/adoption records of the streams other than DYAD v6.4.20 (to `records/<study>/` when supplied), and the DYAD v6.4.19 disposition record.

## Records recovered after the project cleanup (22 October 2026)

Received documents keep their original filenames, because other documents cite them by name or hash. SHA-256 is of the committed file; "Cited in" means a hash for this file appears there and matches.

| File | Location | SHA-256 | Cited in |
|---|---|---|---|
| `ATLAS_DISPOSITION_DYAD_v6_4_19_SESSION_v0_1.md` | `records/dyad/` | `7b2d1573…465c` | DYAD v6.4.20 |
| `DYAD_OPEN20_ANALYTIC_ROOTS_SCOPE_SESSION_v0_1.md` | `records/dyad/` | `5154ca52…a8b0` | — |
| `DYAD_REPLY_TO_FMS_OPEN20_PRIORITY_v0_1.md` | `records/dyad/` | `208ec09a…dda3` | DYAD v6.4.20 |
| `DYAD_REPLY_TO_NUMGEN_LPHASE_ROWA_v0_1.md` | `records/dyad/` | `45cdd704…51cf` | DYAD v6.4.20 |
| `DYAD_REPLY_TO_RECOG_G3_v0_1_2.md` | `records/dyad/` | `836853b0…7104` | — |
| `DYAD_v6_4_19_OUTBOUND_NOTICES_N15.md` | `records/dyad/` | `e221e633…617a` | — |
| `FMS_PILOT_CLOSEOUT_RECORD_v0_1_SESSION.md` | `records/fms/` | `dc65ca48…3349` | — |
| `FMS_TO_DYAD_OPEN20_PRIORITY_REQUEST_v0_1.md` | `records/fms/` | `03da0e34…45ac` | — |
| `GENESIS_V2_8_9_NOTICE_ERRATUM_OFN_Q6_v0_1.md` | `records/gen/` | `81d97f25…94e1` | — |
| `OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_8_2.md` | `records/ofn/` | `6e4fc3c3…4b1d` | OFN v0.10 (governing input) |
| `RRF_EDITOR_QUESTION_PACKET_RER_PHASEA_v0_2_20261019.md` | `records/rer/` | `b1a67b6e…2ccf` | — |

| `DYAD_OPEN20_ANALYTIC_ROOTS_P1B_SESSION_v0_1_1.md` | `records/dyad/` | `6c202d51…` | — |
| `DYAD_OPEN20_ANALYTIC_ROOTS_P1C_SESSION_v0_1.md` | `records/dyad/` | `9f6f09d8…` | — |
| `DYAD_OPEN20_ANALYTIC_ROOTS_P1C2_SESSION_v0_1.md` | `records/dyad/` | `7e7aa09f…` | — |
| `DYAD_OPEN20_ANALYTIC_ROOTS_P1C2B_SESSION_v0_1_1.md` | `records/dyad/` | `578c8f02…` | — |
| `DYAD_OPEN20_ANALYTIC_ROOTS_P1C5_SESSION_v0_1.md` | `records/dyad/` | `11917ba2…` | — |
| `DYAD_OPEN20_AN_P1C_PACKAGE_v0_1.zip` | `evidence/dyad/open20-an/` | `d0b5f929…` | internal SHA256SUMS 8/8 OK |
| `DYAD_OPEN20_AN_P1C2_PACKAGE_v0_1.zip` | `evidence/dyad/open20-an/` | `e7b53ff0…` | internal SHA256SUMS 7/7 OK |
| `DYAD_OPEN20_AN_P1C2B_PACKAGE_v0_1_1.zip` | `evidence/dyad/open20-an/` | `a8de6c31…` | internal SHA256SUMS 6/6 OK |
| `DYAD_OPEN20_AN_P1C5_PACKAGE_v0_1.zip` | `evidence/dyad/open20-an/` | `f5724f9c…` | internal SHA256SUMS 11/11 OK |

The session note inside each package is byte-identical to the standalone note in `records/dyad/`. Packages are kept as received (Methodology v1.4 §13.7, frozen packages).

**Superseded rounds, kept in history only** (commit `19124ac`): `DYAD_OPEN20_ANALYTIC_ROOTS_P1B_SESSION_v0_1.md` (`a9edbf53…`), `DYAD_OPEN20_ANALYTIC_ROOTS_P1C2B_SESSION_v0_1.md` (`9e15d23a…`), `DYAD_OPEN20_AN_P1C2B_PACKAGE_v0_1.zip` (`1864492c…`, internal SHA256SUMS 6/6 OK). Retrieve with `git show 19124ac:<path>`.

**Still missing:** `RECOG_v0_3_22_POST_RELEASE_MAINTENANCE_NOTE.md`.
