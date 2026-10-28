# Discrete Genesis v2.12.14 — atlas tag verification

**Date:** 28 October 2026. **By:** Claude, atlas owner. **Status:** record.

- Tag `tdrg-v2.12.14`: type `tag` (annotated), object `da941f3b2f02f9f242e1c0f517120bfbaead7996` → commit `05c7e78acf63dd1dc5bcbc7bb8364e152e9f0659` = the PR #92 merge commit (parents `3f40c2e` main after PR #95, `fd1b83e` the candidate branch head with the PI adoption §13); message names the DSN SHA-256. Verified from `origin`.
- `dsn/RTG_DISCRETE_GENESIS_DSN.md` at the tag and at `main` both recompute to SHA-256 `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392` (the reviewed candidate; no publication transform — the adopted bytes are the candidate bytes, as the release record §2 planned).
- `BASELINE.md` row TDRG: v2.12.14, same hash, tag `tdrg-v2.12.14`, predecessor v2.12.13 `aa232643…053f` — correct.
- Commits the DSN and its checker cite are reachable from `main`: `c359e21` (PR #91, merged `0a25c06`), `386e9d4` (session scripts, PR #97 merged `6c0365f`), `e3f55c7` (candidate), `f055784` (PR #94). Merge order as asked: #87, #91, #97, #94, #95, #92 — all merge commits.
- `tools/pipes_index.py --check` on `main`: OK (12 items). `pipes/TDRG/`: both items `dispositioned` (request: `2026-10-28 · accept · records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md`; notice: `no action`); to be closed by the owner after the notices.
- Supersedes `tdrg-v2.12.13` as the governing TDR-G edition. The atlas D5 rows that cite v2.12.13 are refreshed in Atlas v0.7.

**Open on the owner side (release record §12 / hand-over step 5):** the tagged release record still describes adoption, merge and tag as pending in §1 — a post-tag section (as NUMGEN's §15) belongs with the closeout commit that files the three `kind: notice` items (`pipes/NUMGEN/`, `pipes/OFN/`, `pipes/AZ/`) and closes the two `pipes/TDRG/` items. None of this changes the adopted DSN or the tag.
