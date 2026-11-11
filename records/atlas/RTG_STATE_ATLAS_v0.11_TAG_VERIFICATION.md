# RTG State Atlas v0.11 — post-tag verification

**Date:** 10 November 2026.
**Status:** [SESSION] **VERIFIED SCOPED.** A post-publication provenance record, NONCANONICAL. Not a second adoption, not a scientific claim, not an authorization to edit the adopted Atlas.
**Recorded by:** Claude, Atlas owner.
**Governance:** `CONVENTIONS.md` §§2, 4, 6–7; `records/atlas/RTG_STATE_ATLAS_v0.11_RELEASE_RECORD.md` §§1–4.

## 1. Publication identities

| Check | Observation | Evidence |
|---|---|---|
| PI decision | Atlas v0.11 accepted on 10 November 2026 at 15:25 +03:00, object `8d7a43f0…f358`. A derived NONCANONICAL map; no owner science adopted. | Release record §3 |
| PR #204 | MERGED as a merge commit, not squash: `65ca82fddf46227fe2457d7d8f696f099390679c`, parents `7d6eb4c4ccb021964d9221fe879b5515eed4f81b` (`main`) and `38b01a436ec053541c3a2fdd444de5ce83a936b6` (PR head, which carries the acceptance record and the BASELINE row). The tree of the merge equals the tree of the PR head. | PI server output; `git log`, `git diff --quiet` in a fresh fetch |
| Tag object | `atlas-v0.11` is an annotated tag: object `95723f2a34c2011a042858b3ba629ce50ea7d7dc`, type `tag`. Tagger Mustafa Aksu, 2026-11-10 12:29:01 UTC. The message names the accepted SHA-256. | `git cat-file -p atlas-v0.11`; the PI's `git cat-file -t` and `git ls-remote` |
| Tag target | `atlas-v0.11^{commit}` = `65ca82fddf46227fe2457d7d8f696f099390679c`, the PR #204 merge commit; `origin/main` was at the same commit when checked. | `git rev-parse`; `git ls-remote` |
| File SHA-256 at tag and at `main` | **`8d7a43f05a42c6a69b50eb97b98dd96ddda7eea327333ae5cc73e03dee46f358`**, equal to the accepted candidate | `sha256sum` here and on the PI's server |
| Manifest and Method at `main` | `evidence/atlas/v0.11/source_manifest.json` `2773f774…2b90`; `atlas/RTG_STATE_ATLAS_METHOD.md` `fbd2efb3…2c04` (v0.2, unchanged) | `sha256sum` |
| Order | PI acceptance → release record on the branch → merge commit → annotated tag | Commit `38b01a4` precedes the merge; tag time follows the merge |
| Reporter | `tools/orient.py ATLAS` at 12:29:36 UTC: COMPLETE; newest tag `atlas-v0.11`; `main` equals tag; release record found and names the hash; 0 commits after the tag on Atlas paths; 0 matched open PRs; inbox 7 closed | native run in this workspace |

**Result.** The accepted bytes are identical at the annotated tag, the merge commit, `main` and the reviewed candidate commit `8cd20d1a`. Publication needed no content transform.

## 2. Scope and limits

- The source snapshot of this edition is that of v0.10, `fa3db80`; no source moved and no pipe census was taken for v0.11.
- This check verifies publication identity and bytes. No owner certificate was rerun; nothing here is physical validation or scientific adoption.
- The release record's status line still reads "merge and tag pending": it is the frozen acceptance record and is not edited; this record supplies the post-publication facts.

## 3. After publication

- `BASELINE.md`: the ATLAS row's tag cell is set to `atlas-v0.11` and names this record (this PR).
- `pipes/ATLAS/`: no item was opened or dispositioned by v0.11; the inbox stays at 7 closed.
- Orientation note: owner lane and PI_PENDING brought to the published state (this PR).
