# RTG State Atlas v0.9 — post-tag verification

**Date:** 3 November 2026.  
**Status:** [SESSION] **VERIFIED SCOPED** — a post-publication provenance record; NONCANONICAL. This is not a second adoption, a new scientific claim, or authorization to edit the adopted Atlas.  
**Governance:** `CONVENTIONS.md` §§2, 4, 6–7; `records/atlas/RTG_STATE_ATLAS_v0.9_RELEASE_RECORD.md` §§1–4 (frozen PI acceptance record).

## 1. Publication identities

| Check | Verified observation | Evidence |
|---|---|---|
| PI decision | Atlas v0.9 rev. 2 accepted on 3 November 2026; acceptance adopts a derived NONCANONICAL knowledge map, no owner science | Release record §3; OWNER decision previously recorded |
| PR #149 | MERGED; merge commit `64ab2be41157fc3eed20a0a790c58f8887b172c8` | GitHub PR metadata (`EV-SRC-READ`) |
| PR #147 | MERGED; merge commit `04cd5e0eda4be80002574b49b58139863c7b3e77`, head `3c6259e72daf70d843ad05428059dc0690f75313` | GitHub PR metadata and commit record (`EV-SRC-READ`) |
| Tag | `atlas-v0.9` resolves to the accepted Atlas file and the file at PR #147's merge commit | GitHub `fetch_file` at tag and merge commit (`EV-BYTES`) |
| Annotated tag metadata | The PI's `git show --no-patch atlas-v0.9` reports an annotated tag with message naming the expected SHA-256 and target commit `04cd5e0e...` | PI-provided Git command/output, `EV-SRC-REPORTED`; tag-object type not independently fetched through an API |
| Git blob at tag | `5ee7e1683d0e8a8f548afec82053c02bb5ca2513` | GitHub `fetch_file` |
| Git blob at merge, head and main | Same `5ee7e1683d0e8a8f548afec82053c02bb5ca2513` (content equality checked) | GitHub `fetch_file` at merge, candidate head and `main` |
| File SHA-256 at tag and main | **`b48343f5a4d4c066eb37a325ff87d1dadf686fc6c616b67e7a0ad418dcec3b70`**, exact match with accepted rev. 2 | Independent UTF-8 SHA-256 computation (`EV-INDEP`, `EV-HASH`); `abc` known-answer self-check PASS |
| File size and lines | 517,999 UTF-8 bytes; 1,547 lines | Fetched bytes and review manifest |

**Result:** The accepted v0.9 bytes are identical at the annotated tag's resolved file, PR #147 merge commit, and inspected `main`. The governance chain is PI acceptance → merge commits → tag. The published Atlas requires no metadata-only content transform (release record §1).

## 2. Scope and evidence limits

- The source snapshot of this Atlas edition is still `f20f080`; later pipe/owner events are not imported by the tag's creation.
- The current source set includes DYAD v6.4.23, OFN v0.12 and TRIAD v1.7. Consumer pin distinctions remain as recorded in the Atlas.
- Neither this check nor the previous Atlas receiving review reruns the owner scientific certificate campaigns. The independent work here is publication identity/byte verification, not physical validation or scientific adoption.
- The annotated tag type and tag-object message are verified from the PI-supplied local `git show` output (`EV-SRC-REPORTED`); repository-connected file retrieval confirms the tag resolves to the accepted bytes, not the tag object's own object type.

## 3. Atlas inbox disposition after publication

The receiving Atlas team can close its two previously dispositioned notices without changing their accept verdict or creating consumer adoption:

| Inbox file | Previous queue state | Post-tag state | Disposition basis |
|---|---|---|---|
| `pipes/ATLAS/20261030-DYAD-v6-4-23-adopted.md` | dispositioned | closed (proposed in this PR) | DYAD v6.4.23 changes included in the tagged Atlas v0.9; review packet §2 |
| `pipes/ATLAS/20261103-TRIAD-v1-7-adopted.md` | dispositioned | closed (proposed in this PR) | TRIAD v1.7 changes included in the tagged Atlas v0.9; review packet §§2, 6 |

The earlier TRIAD row-check request is already `closed` and remains unchanged. The `pipes/ATLAS/INDEX.md` view is regenerated from the resulting item front matter using the exact rendering rules of `tools/pipes_index.py`.

**Open outside this queue:** RECOG's 0.36916 owner-side reassessment; Genesis's two TRIAD questions; Programme IF07/IF11; and any post-snapshot notices are not closed by this record. A `closed` pipe item is not evidence of a receiver Import Ledger adoption.

## 4. Process boundary

This record and the proposed two pipe-state changes are prepared on `chatgpt/atlas-v0.9-post-tag-closeout` for review. They do not modify `atlas/RTG_STATE_ATLAS.md`, the frozen release record, a tagged revision, or a scientific owner DSN. Only the PI may merge this PR. The Atlas v0.9 tag and its scientific source snapshot remain unchanged.
