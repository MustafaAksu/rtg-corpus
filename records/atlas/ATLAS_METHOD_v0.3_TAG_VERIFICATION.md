# RTG State Atlas — Method v0.3 — post-tag verification

**Date:** 12 November 2026.
**Status:** [SESSION] **VERIFIED SCOPED.** A post-publication provenance record, NONCANONICAL. Not a second adoption and not a scientific claim.
**Recorded by:** Claude, Atlas owner.
**Governance:** `CONVENTIONS.md` §§2, 4; `records/atlas/ATLAS_METHOD_v0.3_RELEASE_RECORD.md` §§1–4.

## 1. Publication identities

| Check | Observation | Evidence |
|---|---|---|
| PI decision | Method v0.3 accepted on 12 November 2026 at 12:39 +03:00, object `a2921735…509f` | Release record §3 |
| PR #234 | MERGED as a merge commit, not squash: `6946ec7a73361d0873113bb39a6d79578f58c47c`, parents `8c8982034639b34521939dce1a1df47964da1642` (`main`) and `b957192cd58dbe98287f12a5ea0995e029ae179f` (PR head, which carries the acceptance record and the BASELINE row). On `atlas/`, `records/atlas/` and `BASELINE.md` the merge equals the PR head. | PI server output; `git log`, `git diff --quiet` in a fresh fetch |
| Tag object | `atlas-method-v0.3` is an annotated tag: object `02ca69ec708989857118c0b563e8af295cd1da0e`, type `tag`. Tagger Mustafa Aksu, 2026-11-12 09:51:10 UTC. The message names the accepted SHA-256. | `git cat-file -p`; the PI's `git cat-file -t` and `git ls-remote` |
| Tag target | `atlas-method-v0.3^{commit}` = `6946ec7a73361d0873113bb39a6d79578f58c47c`, the PR #234 merge commit; `origin/main` was at the same commit when checked | `git rev-parse`; `git ls-remote` |
| Method SHA-256 at tag and at `main` | **`a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f`**, equal to the accepted and reviewed object (review 5872066576 on `b640123a`) | `sha256sum` here and on the PI's server |
| Atlas file | unchanged: `cf9d8647b4c33206537e46ca37c7879d4fc33b1a936e0a50330a469f054def55` at `main`, equal to `atlas-v0.12` | `sha256sum` here and on the PI's server |
| Tag namespaces | the reporter (`tools/orient.py ATLAS`, 09:51:41 UTC, COMPLETE) still names `atlas-v0.12` as the newest atlas tag with `main` equal to the tag: the prefix `atlas-method-v` does not match the atlas tag prefix `atlas-v` | native run in this workspace |
| Order | review → PI acceptance → release record on the branch → merge commit → annotated tag | commit `b957192` precedes the merge; tag time follows the merge |

**Result.** The accepted Method bytes are identical at the annotated tag, the merge commit and `main`. No atlas byte changed.

## 2. Scope

Method v0.2 remains identified by `atlas-v0.2`. Atlas v0.12 was built under v0.2 and its manifest says so. The next atlas manifest names `method_edition` v0.3 and `method_tag` `atlas-method-v0.3`.

## 3. After publication

- `BASELINE.md`: the "ATLAS Method" row's tag cell is set to `atlas-method-v0.3` and names this record (this PR).
- Orientation note: owner lane and PI_PENDING brought to the published state (this PR).
