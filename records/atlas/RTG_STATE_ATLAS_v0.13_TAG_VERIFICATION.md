# RTG State Atlas v0.13 — post-tag verification

**Date:** 16 November 2026.
**Status:** [SESSION] **VERIFIED SCOPED.** A post-publication provenance record, NONCANONICAL. Not a second adoption, not a scientific claim, not an authorization to edit the adopted Atlas.
**Recorded by:** Claude, Atlas owner.
**Governance:** `CONVENTIONS.md` §§2, 4, 6–7; `records/atlas/RTG_STATE_ATLAS_v0.13_RELEASE_RECORD.md` §§1–5.

## 1. Publication identities

| Check | Observation | Evidence |
|---|---|---|
| PI decision | Atlas v0.13 accepted on 16 November 2026 at 15:45 +03:00, object `208ddd96…9045`. A derived NONCANONICAL map; no owner science adopted. | Release record §4 |
| PR #277 | Merged before #272: `52872f9a8f4cababf545a9ffe521bc5329c79451` (atlas row check of TDR-G v2.13; records and evidence only). | `git log --first-parent` |
| PR #272 | MERGED as a merge commit, not squash: `a7a0002327762854d7a51f5fe716cf82955d0c8c`, parents `52872f9a…` (`main` after #277) and `3a496df5d6eb0e988cad4ac242208ce73d30fd6f` (PR head with the publication commit: PI decision, BASELINE row). | `git log -1 --format=%P` |
| Tag object | `atlas-v0.13` is an annotated tag: object `0a87e20056671034fde6deb74a7835b404008403`, type `tag`, tagger Mustafa Aksu, 2026-11-16 12:52:50 UTC. The message names the accepted SHA-256, the sources and the Method tag. | `git cat-file -p atlas-v0.13`; `git ls-remote` |
| Tag target | `atlas-v0.13^{commit}` = `a7a00023…`, the PR #272 merge commit | `git rev-parse` |
| File SHA-256 at tag and at `main` | **`208ddd9622b2ea9d291b40dbc103d6eaa3f357aa0e23b2de6190df2c0f879045`**; blob `b178a63f76277323751e3ce8214d4c4b6ef17f97` at both; equal to the reviewed candidate (readback `5917882889` on `d11f7df`; the publication commit changed no Atlas byte) | `sha256sum`, `git rev-parse <rev>:atlas/RTG_STATE_ATLAS.md` |
| Manifest at `main` | `evidence/atlas/v0.13/source_manifest.json` `460b87ce…1b4e` | `sha256sum` |
| BASELINE | ATLAS row v0.13 with the accepted hash and tag `atlas-v0.13` | `BASELINE.md` |
| Order | review → readback → PI acceptance → publication commit on the branch → merge commit → annotated tag | commit `3a496df` precedes the merge; the tag follows the merge |
| Reporter | `tools/orient.py ATLAS` at 13:07:11 UTC: COMPLETE; newest tag `atlas-v0.13`; `main` equals tag; release record found and names the hash; inbox 9 closed, 2 dispositioned, 1 open | native run in this workspace |
| Second verification | The Atlas co-owner (ChatGPT) checked the same chain independently through Git object identities and the publication records: merges, parents, tag object and target, blob `b178a63f…` | [SESSION] relayed report, 16 Nov 2026 |

**Result.** The accepted bytes are identical at the annotated tag, the merge commit, `main` and the reviewed candidate.

## 2. Scope and limits

- **A source moved before the tag.** `az-v0.10` was merged (`062a172`, PR #276) and tagged (2026-11-16 12:46:18 UTC) six minutes before `atlas-v0.13`. The edition was published with its frozen inputs `tdrg-v2.12.15` and `az-v0.9`, as reviewed and accepted. It is not re-pinned. AZ v0.10 adds one AZ-owned diagnostic, `AZ-NUM-TOKRES-S2`, and enters through the next refresh. Its notice `pipes/ATLAS/20261116-AZ-v0-10-adopted.md` stays open until then. The v0.13 builder's "no newer tag" assertion therefore no longer holds at `main`; publication did not rebuild.
- TDR-G v2.13 has been adopted by the PI (16 Nov 2026) and is not yet merged or tagged (PR #265). It also enters through the next refresh.
- This check verifies publication identity and bytes. No owner certificate was rerun; nothing here is physical validation or scientific adoption.

## 3. After publication

- `pipes/ATLAS/20261112-AZ-v0-8-adopted.md` and `pipes/ATLAS/20261114-AZ-v0-9-adopted.md`: closed (this PR); index regenerated.
- Orientation note: owner lane and PI_PENDING brought to the published state (this PR).
- Next: Atlas v0.14 impact refresh for `tdrg-v2.13` (after its tag) and `az-v0.10`; row list for TDR-G in `records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_13.md` §4.
