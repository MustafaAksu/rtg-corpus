# RTG State Atlas v0.12 — post-tag verification

**Date:** 12 November 2026.
**Status:** [SESSION] **VERIFIED SCOPED.** A post-publication provenance record, NONCANONICAL. Not a second adoption, not a scientific claim, not an authorization to edit the adopted Atlas.
**Recorded by:** Claude, Atlas owner.
**Governance:** `CONVENTIONS.md` §§2, 4, 6–7; `records/atlas/RTG_STATE_ATLAS_v0.12_RELEASE_RECORD.md` §§1–5.

## 1. Publication identities

| Check | Observation | Evidence |
|---|---|---|
| PI decision | Atlas v0.12 accepted on 12 November 2026 at 09:51 +03:00, object `cf9d8647…ef55`. A derived NONCANONICAL map; no owner science adopted. | Release record §4 |
| PR #229 | MERGED as a merge commit, not squash: `661b29503918d475a350fc2c28df92b3709b8c0b`, parents `082f702b63d631491866241164ddc19031773854` (`main`) and `705d0bc967e175bea2ab554ae86a838d39ff975e` (PR head, which carries the acceptance record and the BASELINE row). On the Atlas paths (`atlas/`, `evidence/atlas/`, `records/atlas/`, `BASELINE.md`) the merge equals the PR head. | PI server output; `git log`, `git diff --quiet` in a fresh fetch |
| Tag object | `atlas-v0.12` is an annotated tag: object `c4417a36d9cbfc1e39a8407ffc020107db267ff1`, type `tag`. Tagger Mustafa Aksu, 2026-11-12 07:06:22 UTC. The message names the accepted SHA-256. | `git cat-file -p atlas-v0.12`; the PI's `git cat-file -t` and `git ls-remote` |
| Tag target | `atlas-v0.12^{commit}` = `661b29503918d475a350fc2c28df92b3709b8c0b`, the PR #229 merge commit; `origin/main` was at the same commit when checked. | `git rev-parse`; `git ls-remote` |
| File SHA-256 at tag and at `main` | **`cf9d8647b4c33206537e46ca37c7879d4fc33b1a936e0a50330a469f054def55`**, equal to the accepted and reviewed candidate (review 5869585886 on `24f231be`) | `sha256sum` here and on the PI's server |
| Manifest at `main` | `evidence/atlas/v0.12/source_manifest.json` `c798d272…8e6d` | `sha256sum` |
| Order | receiving review → PI acceptance → release record on the branch → merge commit → annotated tag | commit `705d0bc` precedes the merge; tag time follows the merge |
| Reporter | `tools/orient.py ATLAS` at 07:07:08 UTC: COMPLETE; newest tag `atlas-v0.12`; `main` equals tag; release record found and names the hash; 0 commits after the tag on Atlas paths; one matched open PR (#225, the reviewer's preparation record, not merged); inbox 7 closed, 2 dispositioned | native run in this workspace |

**Result.** The accepted bytes are identical at the annotated tag, the merge commit, `main` and the reviewed candidate. Publication needed no content transform.

## 2. Scope and limits

- The source snapshot of the edition is `c8e7198`. Between it and the merge, `main` received evidence and record commits of other streams (AZ Action 1 and Thread C custody, Dyadic OPEN 20 working evidence); no DSN, no source tag and no `BASELINE.md` source row moved, so the manifest is still current at the tag.
- This check verifies publication identity and bytes. No owner certificate was rerun; nothing here is physical validation or scientific adoption.
- The release record's status line still reads "merge and tag pending": it is the frozen acceptance record and is not edited; this record supplies the post-publication facts.

## 3. After publication

- `pipes/ATLAS/20261111-AZ-v0-7-adopted.md` and `pipes/ATLAS/20261111-DYAD-v6-4-24-adopted.md`: closed (this PR); index regenerated.
- `BASELINE.md`: the ATLAS row's tag cell is set to `atlas-v0.12` and names this record (this PR).
- Orientation note: owner lane and PI_PENDING brought to the published state (this PR).
