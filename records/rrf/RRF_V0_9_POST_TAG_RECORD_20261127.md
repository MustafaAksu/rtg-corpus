# RRF v0.9 — post-tag publication record

**Date:** 27 November 2026.
**Status:** [SESSION] post-tag readback (Claude, RRF second co-owner). This is a dated publication receipt. It does not amend the frozen release record `records/rrf/RRF_v0_9_RELEASE_RECORD.md`.
**Publication:** run by the PI on the Ubuntu server from the reviewed block. The PI delegated publication authority to this co-owner lane for the post-tag steps ("yayın yetkisi senin", 27 Nov 2026).

## Verified publication identities

| Object | Value |
|---|---|
| Merge of #417 | `d010e2f`, parents `136d1c59` and `638a1a8b`. Merge commit, not squash. |
| Merge of #418 | `3f6dea9`, parents `d010e2f` and `829d9e6f`. Merge commit. |
| BASELINE commit | `0d79defef39d8fa87ba3c84bf5d13b6d55739615` (`main`) |
| Tag `rrf-v0.9` | annotated. Tag object `92c4762540b6d46b882dbd5a1091b546e61dd716`, target `0d79defe…5615`. The message names the PI adoption (comment 7213581950), the DSN SHA-256 and the release record. |
| Tagged DSN | `dsn/RTG_RRF_REPRESENTATION_REGISTRY.md`: 121,216 bytes, SHA-256 `28c9c101c715b402b5ed60eeab8bfa2c7e5e637fef3cd2b00961dfa60553075d`, equal to `main` |
| G1 ancestry | `98da97c3` (S2a freeze), `8de7a8cd` (adopted candidate), `638a1a8b` (publication head) and `829d9e6f` (#418) are all ancestors of `rrf-v0.9`, which is on `main`. |
| BASELINE row at the tag | RRF v0.9 `28c9c101…075d`, OWNER release record, tag `rrf-v0.9`. Matches release record §6 byte for byte. |
| Checks on `main` | `publish_rrf_v0_9.py` gives `RRF_V0_9_PUBLICATION_PASS`; pipes 199/20. #404, #417 and #418 are shown as merged on GitHub. |

**Governing edition:** `rrf-v0.9`, superseding `rrf-v0.8.4`.

The scope is the RRF working representation standard only:
- OPEN-A/B/E1/E2 remain ACTIVE;
- no owner science, physical gauge or carrier, or BR-Q2 result is adopted;
- PRR v0.3 and GIIL decisions remain separate.

The adapter `check_rrf_s2b.py` certifies the S2b candidate only. Replay it at `8de7a8cd`. On `main` it fails on candidate identity by design.

## Post-tag follow-ups

- **Done here:** the PROG and RER notices gain `rrf-v0.9` in their tag lists and a receipt line at the end of the body. No original text is changed.
- **Open:**
  - **Notice dispositions:** the receivers (PROG for IF30/31/33; RER for IF33/G7–G10) decide.
  - **Inbox closeout:** the nine S1 RRF inbox items are a separate receiving action of the RRF co-owners. BR-Q2 stays open, and its #414 review is pending.
  - **Orientation note:** the shared block's "publication pending" line should be updated by the preparer.
