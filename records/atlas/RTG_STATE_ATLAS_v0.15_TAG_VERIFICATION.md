# RTG State Atlas v0.15 — post-tag verification

**Date:** 21 November 2026.
**Status:** [SESSION] **VERIFIED SCOPED.** A post-publication provenance record, NONCANONICAL. Not a second adoption, not a scientific claim, not an authorization to edit the adopted Atlas.
**Recorded by:** Claude, Atlas owner.
**Governance:** `CONVENTIONS.md` §§2, 4, 6–7; `records/atlas/RTG_STATE_ATLAS_v0.15_RELEASE_RECORD.md` §§1–5.

## 1. Publication identities

| Check | Observation | Evidence |
|---|---|---|
| PI decision | Atlas v0.15 accepted on 21 November 2026 at 14:51 +03:00, object `483e6003…02df`. A derived NONCANONICAL map; no owner science adopted. | Release record §4 |
| PR #349 | MERGED as a merge commit, not squash: `a2b3bbeb8d8dd0f41eb9dabf5af4c8527cee95ea`. Parents: `e34b3230b424ebca57e529334e4b56b2a67a49db` (`main` before the merge) and `c2c6d687586fecedc0a85203f723afb7bce1f877` (PR head with the publication commit). | `git show -s --format='%H %P'`; GitHub PR state |
| Tag object | `atlas-v0.15` is an annotated tag: object `defa3e3f4f3144c14c5523d8dfba9cfebce244d4`, type `tag`, tagger Mustafa Aksu, 2026-11-21 11:53:07 UTC. Its message names the accepted SHA-256, the moved source, the review and the record. | `git cat-file -t`; `git for-each-ref`; GitHub ref |
| Tag target | `atlas-v0.15^{commit}` = `a2b3bbeb…`, the PR #349 merge commit. The CLI block asserted the PR head and the file hash on it before merging, and the absence of the tag. | `git rev-parse`; PI's server output |
| File SHA-256 at the tag and at `main` | **`483e60034ff3bb644216c5123d28b8bca253d3ba1b72cdf68bfb0056518d02df`**; blob `76755bc1f9f29d38277dd8bcc8d0ceb48b7b96cb` at both. Equal to the candidate of review `6004985736` on `46a4105`; the two later commits on the branch (review recorded; decision and BASELINE row) changed no Atlas byte. | `sha256sum`; `git rev-parse <rev>:atlas/RTG_STATE_ATLAS.md` |
| Manifest at `main` | `evidence/atlas/v0.15/source_manifest.json`, `5fadeb23…46cd` | `sha256sum` |
| BASELINE | ATLAS row v0.15 with the accepted hash and tag `atlas-v0.15` | `BASELINE.md` |
| Sources | For all 18 manifest sources the manifest tag is the newest tag of its study at the time of this check. Nothing changed under `dsn/` or `pipes/` between the snapshot `357b963` and the merge commit. | `git tag --list`; `git diff --stat` |
| Pipes | `pipes_index.py --check` passes on the merge commit: 147 items in 20 inboxes | PI's server output |
| Reporter | `tools/orient.py ATLAS` at 11:53:45 UTC: COMPLETE; newest tag `atlas-v0.15`; `main` equals the tag; the release record names the tag hash; inbox 12 closed; one open PR on Atlas paths (#337, the work list) | native run in this workspace |

**Result.** The accepted bytes are identical at the annotated tag, the merge commit, `main` and the reviewed candidate.

## 2. Scope and limits

This check verifies publication identity and bytes. No owner certificate was rerun; nothing here is physical validation or scientific adoption. The reviewer's evidence boundary stands (release record §4): the builder, the shared checker and the 22 focused controls are producer records. The four Atlas-side compound heads in D5 stay carried forward.

The builder `evidence/atlas/build/refresh_v0_15.py` asserts that no source tag is newer than its manifest. It stops by design once any source moves; the publication does not depend on rebuilding.

## 3. After publication

- No `pipes/ATLAS/` item belonged to this edition; the inbox has no open item.
- Orientation note: the owner lane and PI_PENDING are brought to the published state (this PR). `BASELINE.md`: the ATLAS row names this record (this PR).
- Next refresh: any owner tag after `357b963`. DZT B1 (PR #347) is not part of v0.15; a later DZT edition enters through the next refresh.
