# Number Genesis held records — unchanged upload

**Date:** 26 October 2026. **Uploaded by:** Claude, NUMGEN co-owner session (the session that built and released v1.20.8). **Basis:** PI hand-over for v1.21 (26 Oct 2026) and `records/numgen/NUMGEN_COOWNER_ENTRY_NOTE.md` §2: "place them unchanged on an `upload/numgen-records` branch; the atlas owner hash-checks them. Nothing is reconstructed."

## What this is

These are all the files held in this session's output folder, copied byte for byte with no renaming or editing:
- 276 top-level files;
- the 2 files of `census1_tdrg_replay/`, kept in their folder.

Python bytecode caches (`__pycache__/`) are left out. `SHA256SUMS.txt` lists every uploaded file except itself and this README.

Nothing here is a new record. The PI and the atlas owner decide placement.

## Provenance, as far as this session can state it

- **Built in this session (20–21 Oct 2026):** the v1.20.8 drafts r1–r3, builders, checkers, edit lists, diffs, the r2 and r3 review packages, the release transform, its checker and output, `NUMGEN_v1_20_8_RELEASE_RECORD.md`, `RTG_NUMBER_GENESIS_v1_20_8_INSTALL_MANIFEST.json`, the r3 delta note, and the `NUMGEN_*_20261020*` memos and records.
  - Main identities:
    - adopted v1.20.8 `835a56f8…817e`, byte-equal to `main` `dsn/RTG_NUMBER_GENESIS_DSN.md`;
    - release record `fb699967…1f97`;
    - r3 review package `a7fc9ed6…ee84`;
    - r2 review package `4722809b…be602`.
- **Present in the session folder before this session's recorded work (dated 20 Oct in the folder):** the earlier editions `RTG_NUMBER_GENESIS_DSN_v1_4_1.md` … `v1_20_7.md`; their fingerprints and diffs; the `NG_*` campaign, preregistration, freeze and review records; and the certificate, harness and replay scripts with their logs (`ng_*`, `disc1_*`, `disc2_*`, `bind3_*`, `genesis_mode_b_mc_v18.py`, …). This session did not create them. Their earlier history (which session or upload produced each one) is not recorded here. They are uploaded as held.
- `RTG_NUMBER_GENESIS_DSN_v1_20_7.md` hashes to `c4637e7a…ab28`, the hash v1.20.8 names as its predecessor.

## Files that carry a banner on purpose

These files were bannered SUPERSEDED in the session folder after their successors were verified:
- `RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r1.md`, `_r2.md`, `_r3.md`;
- `NUMGEN_REPLY_TO_RECOG_A1A_C4_20261020_v0_1.md`;
- `NUMGEN_REPLY_TO_RECOG_A1A_RID_REQUEST_20261020_v0_1.md`.

Each banner states the hash of the content without the banner. The payload is everything after the first blank line. For example, r3 without its banner hashes to `9d59cfa1…e7b3`, the reviewed draft that the PI adopted.

## Not claimed

- No file was rerun for this upload.
- No hash beyond those printed by `sha256sum` here is asserted.
- Files cited in `numgen-v1.20.8` that are absent from this upload are for the atlas hash check to list as missing; nothing is reconstructed.
