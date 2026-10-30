# Triadic custody intake — hash check (stage 0)

**Date:** 30 October 2026. **By:** Claude, Atlas owner.
**Evidence:** `EV-HASH` and `EV-SRC-READ`. No owner decision is made and no canonical file is changed.

## 1. `upload/triad-records`, commit `2a1a4a8`

Uploaded by the PI and ChatGPT from the user-supplied `TRIAD_v1_6_1_RELEASE_PACKAGE_20261019.zip` (ZIP SHA-256 `8ab2a3c6…ca5f`, per the intake manifest). The branch is based on current `main` (`c6724e9`); its diff against `main` is exactly four added files.

| File | SHA-256 (recomputed here) | Check |
|---|---|---|
| `upload/triad-records/release/records/OWNER_ADOPTION_v1_6_1.json` | `33bcd3cea83b467d0bc4d8cc4a37c10771cd81151831caec87c55873937cd5dd` | equals the package's `release/SHA256SUMS` entry; names the DSN `95340abe…451f` (= `triad-v1.6.1`), DRAFT r1 `31b87c3e…30ea` and DRAFT r2 `dd67907f…b3e7`, the same hashes the DSN header prints (L7, L12) |
| `upload/triad-records/release/records/RELEASE_RECORD_v1_6_1.md` | `aa3d8d773a2083908f2e576bc59f9c6d3c110c1caadbc70782c72b07e95eb45d` | equals the `SHA256SUMS` entry; same three identities; dated 19 October 2026; "release verification by the receiving co-owner is pending" and "Programme v1.2 pass two" are preserved literally, as historical content |
| `upload/triad-records/release/SHA256SUMS` | `eda9af16…bb9c` | lists 11 package files. The 2 records are present and OK. The other 9 (the DSN and its two drafts, the release and check scripts, the edits JSON, the diff) are **not on the branch**. The listed DSN hash equals the tagged `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md`. The two draft hashes equal the ones the DSN prints (L12), but the draft files are not in the repository. The 7 script, output, edits and diff files cannot be checked here |
| `upload/triad-records/INTAKE_MANIFEST.md` | `f52103ff…170b` | the uploader's intake note, not an original |

The DSN cites these records at L14 but prints no hash for them, so the identification rests on the package checksum list and on the three DSN and draft hashes they contain.

Per the intake manifest, the branch is not merged automatically. Placement under `records/triad/` is the owners' decision; until then the files are cited where they are.

## 2. Two producer scripts recovered from git history

The PI uploaded both scripts in commit `9df0319` ("TDRG files", 27 Oct 2026, `upload/tdrg-records/`). `07df334` removed them from that branch as "unrelated" before the TDR-G custody merge. They are copied byte-for-byte from `9df0319` to `evidence/triad/scripts/`:

| File | SHA-256 | DSN |
|---|---|---|
| `tetrahedral_six_step_cross_phase_t6c2_patched.py` | `afb4525ccc2f459964fc3e9acade004f2aa61c03be2366f125cef63fc466d80e` | **equal** to TRIAD-ART-T6C-CROSSPHASE (L903) |
| `triad_analytic_phase_steering_t6l_patched.py` | `2e0317bf90332d1fe0ab7489710a3c8c67b772e3031dd7ef95b3163f7d7a11cd` | **equal** to TRIAD-ART-T6L-TORSION (L915) |

They have not been run. The DSN cites them as recovered producer bytes and historical algebra; nothing is regraded.

## 3. Still missing

These items are not needed to begin the owners' dispositions. The custody rows (24–28 of the reconciliation) stay open for them.

- **The v1.6 release evidence (DSN L15):** `evidence/accepted_r4_2/`. It holds the manifests (`EXECUTION_MANIFEST*.json`, `FILE_IDENTITIES.json`), `t6u_certificate.json`, and `triad_t6_producers.zip` (`8ad574ff…de69`, L918). It also holds the T-6u scripts: `triad_t6u_apex_source_v1_6.py`, with its 47 assertions (L621), and the point-of-use and scope checks. Further contents are `scripts/triad_torsion_object_check_r4_2.py` (`bd9ae5d5…773e`, L918), the T-6b/d/e/f/h/j producers and the release build scripts (TC-02).
- **The v1.6 records (DSN L14):** `records/OWNER_ADOPTION.json`, `records/RELEASE_RECORD.md` and `records/METADATA_EDITS.json`. The v1.5 and v1.6 DSN files are also missing (TC-01).
- **The remaining 9 files of the v1.6.1 release package.** The original ZIP is with the PI.
- **The T-6j2 session script and log.** The DSN states they are unrecoverable (L766, L917). TRIAD-ART-T6M-BIRTH (L916) is likewise session-only.
- **Placeholders.** "proof-source reference required" at L899–902 and L905. `apex_ratio_setup.py` and `genesis_k4_route_census.py` are stated as unavailable (TC-04).
- **The T-3a scaffold** (`upload/dyad-sources/rtg-engine/triad_t3a_arb_enclosure_v4g.cpp`). It is present, but it is not a certificate and no Triadic claim cites it.
