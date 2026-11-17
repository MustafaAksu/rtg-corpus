# RTG State Atlas v0.14 — post-tag verification

**Date:** 17 November 2026.
**Status:** [SESSION] **VERIFIED SCOPED.** A post-publication provenance record, NONCANONICAL. Not a second adoption, not a scientific claim, not an authorization to edit the adopted Atlas.
**Recorded by:** Claude, Atlas owner.
**Governance:** `CONVENTIONS.md` §§2, 4, 6–7; `records/atlas/RTG_STATE_ATLAS_v0.14_RELEASE_RECORD.md` §§1–5.

## 1. Publication identities

| Check | Observation | Evidence |
|---|---|---|
| PI decision | Atlas v0.14 accepted on 17 November 2026 at 09:29 +03:00, object `d34e5697…1e85`. A derived NONCANONICAL map; no owner science adopted. | Release record §4 |
| PR #293 | MERGED as a merge commit, not squash: `870afbedfc6fba1d14897da2ea1f6964632e68d3`. Parents: `72087dd8656d788615746d3ded44bf864e4a2496` (`main` before the merge) and `c57ad70673c806351f0c7b34e40299a5aa383fd0` (PR head with the publication commit). | `git log -1 --format=%P` |
| Tag object | `atlas-v0.14` is an annotated tag: object `9b466a1a0d226ff19a8756d9a34dbae96e9018d1`, type `tag`, tagger Mustafa Aksu, 2026-11-17 06:32:31 UTC. Its message names the accepted SHA-256, the sources and the Method tag. | `git cat-file -p atlas-v0.14`; `git ls-remote` |
| Tag target | `atlas-v0.14^{commit}` = `870afbed…`, the PR #293 merge commit. The CLI block asserted the second parent before tagging. | `git rev-parse`; PI's server output |
| File SHA-256 at the tag and at `main` | **`d34e5697ae47201133f513bce5f6b2b8438ed2f4e654fe33a73048a5ca7b1e85`**; blob `13dd2ab6a35d8f7c03cfeac5d19fe1f26c4d8c41` at both. Equal to the candidate of the readback `5933956213` on `6b1f02a`; the publication commit changed no Atlas byte. | `sha256sum`; `git rev-parse <rev>:atlas/RTG_STATE_ATLAS.md` |
| Manifest at `main` | `evidence/atlas/v0.14/source_manifest.json`, `fe2faa91…43c4` | `sha256sum` |
| BASELINE | ATLAS row v0.14 with the accepted hash and tag `atlas-v0.14` | `BASELINE.md` |
| Sources | `tdrg-v2.13` and `az-v0.10` are the newest tags of their studies at the time of the tag; no source moved between the snapshot `a5826ac` and the tag | `git tag --list` |
| Reporter | `tools/orient.py ATLAS` at 06:33:10 UTC: COMPLETE; newest tag `atlas-v0.14`; `main` equals the tag; the release record names the tag hash; inbox 11 closed, 1 dispositioned | native run in this workspace |

**Result.** The accepted bytes are identical at the annotated tag, the merge commit, `main` and the reviewed candidate.

## 2. Scope and limits

This check verifies publication identity and bytes. No owner certificate was rerun; nothing here is physical validation or scientific adoption. The four Atlas-side compound heads in D5 stay carried forward (release record §6).

## 3. After publication

- `pipes/ATLAS/20261116-AZ-v0-10-adopted.md` is closed (this PR) and the index is regenerated. The Atlas inbox has no open item.
- Orientation note: the owner lane and PI_PENDING are brought to the published state (this PR).
- Next refresh: any owner tag after `a5826ac`. The next expected one is DZT's first edition after the onboarding.
