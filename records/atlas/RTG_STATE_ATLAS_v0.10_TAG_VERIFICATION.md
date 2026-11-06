# RTG State Atlas v0.10 — post-tag verification

**Date:** 6 November 2026.
**Status:** [SESSION] **VERIFIED SCOPED.** This is a post-publication provenance record and is NONCANONICAL. It is not a second adoption, not a new scientific claim, and not an authorization to edit the adopted Atlas.
**Recorded by:** Claude, Atlas owner.
**Governance:** `CONVENTIONS.md` §§2, 4, 6–7, and `records/atlas/RTG_STATE_ATLAS_v0.10_RELEASE_RECORD.md` §§1–4, the frozen PI acceptance record.

## 1. Publication identities

| Check | Observation | Evidence |
|---|---|---|
| PI decision | Atlas v0.10 rev. 2 accepted on 6 November 2026 at 14:17 +03:00. The acceptance adopts a derived NONCANONICAL map and no owner science. | Release record §3 |
| PR #186 (receiving review) | MERGED. Merge commit `ba0ae9ec83d0a064d7809b677d4b19792cceda6b`; parents `1908e15f…` (`main`) and `0a70b556…` (PR head). | GitHub PR metadata; `git log` (`EV-SRC-READ`) |
| PR #185 (Atlas v0.10) | MERGED. Merge commit `28516ddf10cf7ba67634cdecf17bec0e6e6b4404`; parents `ba0ae9ec…` (the PR #186 merge) and `06ef0025…` (PR head, i.e. the candidate `f90d74e` plus the acceptance record). | GitHub PR metadata; `git log` (`EV-SRC-READ`) |
| Merge order | PR #186, then PR #185, both as merge commits, not squash. The tag target contains both. | Commit parents above |
| Tag object | `atlas-v0.10` is an annotated tag: object `9afaddfe8ccb16f28f0ea034f3b6eb40123bc9aa`, type `tag`. Tagger Mustafa Aksu, 2026-11-06 11:22:23 UTC. The message names the accepted SHA-256. | `git cat-file -p atlas-v0.10` in a fresh fetch; also the PI's `git cat-file -t` and `git ls-remote` output (`EV-SRC-READ`, `EV-SRC-REPORTED`) |
| Tag target | `atlas-v0.10^{commit}` = `28516ddf10cf7ba67634cdecf17bec0e6e6b4404`, the PR #185 merge commit. `origin/main` was at the same commit when checked. | `git rev-parse`; `git ls-remote` (`EV-SRC-READ`) |
| Git blob | `ccff5ed52b175f1faa3a602608531fd1c7b38d61` at the tag and at the candidate commit `f90d74e`. The Atlas files, `evidence/atlas/` and the release record do not differ between the PR head `06ef002` and the merge commit. | `git rev-parse <ref>:atlas/RTG_STATE_ATLAS.md`; `git diff --quiet` |
| File SHA-256 at tag and `main` | **`443b5990e6082599d1f43fca7d4d24e512e7a632ec395aa56f05bed16f53dbf7`**, an exact match with accepted rev. 2 | `sha256sum` in this workspace and on the PI's server (`EV-HASH`) |
| Pipes at `main` | `tools/pipes_index.py --check`: 88 items in 20 inboxes | PI output; rerun here |

**Result.** The accepted bytes are identical at four places: the annotated tag, the PR #185 merge commit, `main`, and the reviewed candidate commit. The governance chain was PI acceptance, then the release record, then the merge commits, then the tag. Publication needed no content transform, because the Atlas carries no status line (release record §1).

## 2. Scope and evidence limits

- **Source snapshot.** The source snapshot of this edition stays `fa3db80`. Its pipe census of 87 items is recorded at that snapshot. `main` holds 88 items after the LIT reply item of PR #184. That difference is expected history, not drift, and the next refresh counts at its own snapshot.
- **Scientific checks.** Neither this check nor the receiving review reruns the owner certificate campaigns. The independent work here verifies publication identity and bytes. It is not physical validation or scientific adoption.

## 3. Atlas inbox after publication

The three `pipes/ATLAS/` items dispositioned in v0.10 are closed in this post-release PR. Their accept verdicts are unchanged, and closing them creates no consumer adoption.

| Inbox file | Before | After |
|---|---|---|
| `pipes/ATLAS/20261103-TRIAD-atlas-readings-y6-f18.md` | dispositioned | closed |
| `pipes/ATLAS/20261104-PROG-v1-4-adopted.md` | dispositioned | closed |
| `pipes/ATLAS/20261104-RECOG-v0-3-27-adopted.md` | dispositioned | closed |

`pipes/ATLAS/INDEX.md` is regenerated with `tools/pipes_index.py`, and `--check` passes: 88 items in 20 inboxes. With this PR the ATLAS inbox has no open or dispositioned item.
