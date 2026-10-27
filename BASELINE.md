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
| Programme | `RTG_PROGRAMME_OVERVIEW.md` | v1.3 | `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06` | OWNER: release record `records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md`; predecessor v1.2 `4207da05…9359` (`programme-v1.2`) | `programme-v1.3` |
| DYAD | `RTG_DYADIC_OSCILLATOR_DSN.md` | v6.4.22 | `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29` | OWNER: release record `records/dyad/RTG_DYADIC_v6_4_22_RELEASE_RECORD.md`; change-focused review (PR #9) | `dyad-v6.4.22` (v6.4.21: `a412f34d…dc7d`, `dyad-v6.4.21`; v6.4.20: `0b2d5a44…4852`, `dyad-v6.4.20`; v6.4.19: `dyad-v6.4.19`) |
| TRIAD | `RTG_TRIADIC_BIRTH_LIFT_DSN.md` | v1.6.1 | `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f` | XREF: RER v0.2 §7 (`TRIAD161`, byte-verified there) | `triad-v1.6.1` |
| GEN | `RTG_GENESIS_GEOMETRY_DSN.md` | v2.9 | `9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac` | OWNER: release record `records/gen/GEN_v2_9_RELEASE_RECORD.md`; predecessor v2.8.9 `d143673e…c6fc` (`gen-v2.8.9`) | `gen-v2.9` |
| TDRG | `RTG_DISCRETE_GENESIS_DSN.md` | v2.12.14 | `b8317a75e5fb335075828f706f42f14708538fc15ff958b6acd4ef5402295a61` | OWNER: release record `records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md`; predecessor v2.12.13 `aa232643…053f` (`tdrg-v2.12.13`) | `tdrg-v2.12.14` |
| RECOG | `RTG_RELATIONAL_RECOGNITION_DSN.md` | v0.3.25 | `86cae8ff094d63d077ec5c0887451775ec3a26485cfad95833d8390bda4bd7db` | OWNER: release record `records/recog/RECOG_v0_3_25_RELEASE_RECORD.md`; per-group reviews (PR #83; cells PR #48, #49, #51, #53, #54, #59, #61, #63, #64, #71, #75) | `recog-v0.3.25` (tag to be created by the PI; v0.3.24: `8c64bea2…e7c1`, `recog-v0.3.24`; v0.3.23: `0d583400…a31a`; v0.3.22: `0dcce9e4…bcd9`; XREF RER v0.2 G9) |
| NUMGEN | `RTG_NUMBER_GENESIS_DSN.md` | v1.21 | `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701` | OWNER: release record `records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md`; atlas row checks (PR #77); predecessor v1.20.8 `835a56f8…817e` (`numgen-v1.20.8`) | `numgen-v1.21` |
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

Release/adoption records of the streams other than DYAD v6.4.20–v6.4.22, RECOG v0.3.21–v0.3.24 and NUMGEN v1.21 (to `records/<study>/` when supplied), and the DYAD v6.4.19 disposition record.

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

## RECOG records and evidence recovered (23 October 2026)

Received from the RECOG co-owner sessions via the PI on `upload/recog-record-recovery` (commits `d2ace94`, `f177eee`, `5c4dfc9`, `95725a4`) and placed unchanged. Hand-over bundle `RECOG_HANDOVER_RECORDS_AND_EVIDENCE_20261023.zip` `c20e1aa56dd341288c1cc65cce10340d605bdc8586a42115e99ebb6eba3bbd79`, internal SHA256SUMS 174/174 OK; kept in history only (its `editions/` are not placed).

| File | Location | SHA-256 | Cited in |
|---|---|---|---|
| `RECOG_v0_3_22_RELEASE_RECORD.md` | `records/recog/` | `d9636a8d…0820` | — |
| `RECOG_v0_3_21_RELEASE_RECORD.md` | `records/recog/` | `4b7aefee…ef72` | — |
| `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` | `records/recog/` | `5c00f66d…9b55` | RER v0.2 |
| `RECOG_v0_3_22_POST_RELEASE_MAINTENANCE_NOTE.md` | `records/recog/` | `b5b9131c…eab0` | — |
| `RECOG_A1A_G1_DISPOSITION_RECORD_20261020.md` | `records/recog/a1a/g1/` | `0e5f91c0…71a7` | RECOG v0.3.22 |
| `RECOG_G3_NOTICE_TO_RER_20261020.md` | `records/recog/g3/` | `53341b9a…b4b5` | RER v0.2 |
| `RECOG_COOWNER_STATE_REVIEW_v0_3_22_20261023.md` | `records/recog/` | `5ae79687…93a7` | — |
| `RECOG_OWNER_SELF_REVIEW_20261023.md` (received as `attachment.txt`) | `records/recog/` | `33a491d0…c845` | — |
| `e2c_prod.zip` (PI production run) | `evidence/recog/packages/` | `4f171da6…b22d` | 29/29 chunk hashes of `e2c_production_certificate_v2.json` |

Full per-hash inventory, placement map and the items still missing: `records/recog/RECOG_SOURCE_RECOVERY_LIST.md`.

## Genesis records recovered (24–25 October 2026)

Held Genesis records for editions v2.8.6–v2.8.9 were received from the Genesis co-owner session on `upload/gen-records` and merged unchanged (PR #40). Their **permanent home is `upload/gen-records/`** by PI decision V2 of 25 October 2026; they are not moved, renamed or re-encoded.

| Item | Location | SHA-256 |
|---|---|---|
| 36 held files (release records, manifests, dispositions, kit notes, session records, 7 zip packages) | `upload/gen-records/` | per `upload/gen-records/SHA256SUMS.txt` (`beb32a22…f8ca`; 36/36 OK) |
| Upload README (what was not held) | `upload/gen-records/README_UPLOAD.md` | `ecab0818…34e5` |
| Atlas hash check and placement record | `records/gen/GEN_UPLOAD_HASH_CHECK_20261024.md` | — |
| Inventory (files, zip members, cited identities present or missing) | `evidence/gen/inventory/gen_upload_inventory_20261024.json` | `5b97dfa0…10be` |

Among them: the Genesis release records of v2.8.6 (`b6137587…3fec`), v2.8.7 (`d3fcc38e…9223`), v2.8.8 (`03deb7cb…c049`) and v2.8.9 (`f6df5d11…4181`). The 11 cited identities not held are listed in the hash-check record and stay missing; nothing was reconstructed.
