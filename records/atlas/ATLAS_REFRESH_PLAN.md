# RTG State Atlas — refresh plan (v0.1 → v0.2)

**Date:** 23 October 2026. **From:** Claude (atlas owner). **To:** PI; ChatGPT (reviewer). **Status:** working plan; nothing built yet.

## 1. Principle

The atlas holds the **latest knowledge and the currently open issues**, nothing else.
- It does not say what was done, fixed, corrected, resolved or changed, or in which edition. No "now", "previously", "was", "resolved in vX", and no advisory or review status.
- A diagnostic (L5) that no longer holds is deleted, not marked resolved. A diagnostic that still holds is restated against the current sources.
- Process state (advisories, dispositions, notices, release records) lives in `records/`, never in the atlas.
- Unchanged from Method v0.1: derived and noncanonical; the owner DSN wins on any conflict; no fact is dropped for size.

## 2. What changed in the sources

Atlas v0.1 was built on 21 Oct 2026. Its source table, compared with the governing tags in `BASELINE.md`:

| Source | Atlas v0.1 read | Governing now | Action |
|---|---|---|---|
| Methodology | v1.3 | v1.4 (`methodology-v1.4`) | rewrite L0.M (grade semantics, EV keys, governing-edition rule, live-file rule) |
| DYAD | v6.4.19 | v6.4.22 (`dyad-v6.4.22`) | **full re-extraction of the DYAD slice** (three releases; 13 RIDs registered since; atlas cites 72 DYAD identifiers, v6.4.22 has 164 including artifact IDs) |
| RER | v0.2 DRAFT r4.6 | v0.2 ADOPTED, noncanonical (`rer-v0.2`) | re-extraction of the RER nodes (D4a and edges) |
| the other 15 sources | same editions | same tags | no re-extraction; edges and L5 items that touch the three changed sources are re-checked |

Before building, every unchanged source is hash-checked against its tag, so "same edition" is verified rather than assumed.

## 3. Steps

1. **Method v0.2** (`atlas/RTG_STATE_ATLAS_METHOD.md`, fixed name). Changes:
   - write the principle of §1 as content rule 4.1;
   - the source table gives edition and repository tag, and the atlas is built only from tagged files;
   - inputs are the files in `dsn/` and `noncanonical/` at their governing tags, replacing "the project root";
   - L5 IDs are stable keys only, with no link to advisory rows;
   - regeneration is by changed tag.
2. **Source table and L0.** New table: edition, tag, date, class. L0.M is rewritten from Methodology v1.4. Header pointers go to `atlas/RTG_STATE_ATLAS_METHOD.md`.
3. **DYAD slice (D2 and DYAD nodes elsewhere).** Re-extracted from v6.4.22 in full, in the v0.1 record syntax. Every live DYAD result RID gets a node. Imports collapse to owner nodes. Edges from D1, D3, D4a, D4b and D5 into DYAD are re-pointed or removed if their target no longer exists.
4. **RER nodes.** Re-extracted from the adopted v0.2: the 18 accepted records at their adopted scope, and the exception for the two blocked ER-2B records.
5. **L5 re-evaluation.**
   - Every L5 item, including the HEADLINE list (H1–H12) and D-WRONG, is checked against the current sources.
   - An item that touches a changed source is kept (restated in current terms) or deleted.
   - Items about unchanged sources stay as they are, with any process wording removed.
   - New findings from the re-extraction are added.
   - The HEADLINE list is recomputed.
6. **Wording pass for history.** Remove history and process wording atlas-wide: "advisory", "resolved", "previously", "vX adds", "now". Facts are kept.
7. **Checks** (`tools/atlas_check.py`, new; reports only):
   - **sources:** every source-table row equals the governing tag in `BASELINE.md`, and its hash matches;
   - **coverage:** every live result RID of the three changed sources appears in the atlas. Artifact (`-ART-`) RIDs are excluded unless the PI wants them; see §5, Q2;
   - **link integrity:** every RID the atlas cites exists in some current source, or is listed in L5 as a phantom RID;
   - **history wording:** a list of history and process phrases, reported for review.
8. **Review and release.**
   - Branch `claude/atlas-v0.2`.
   - ChatGPT gets a change-focused review: the method diff, the DYAD and RER slices, the L5 deletions with a one-line reason each in the review packet (not in the atlas), and the check report.
   - PI acceptance, merge, tag `atlas-v0.2`, then "Sync now".
   - The atlas is not a DSN, so there is no adoption cycle beyond this.

## 4. Deliverables

`atlas/RTG_STATE_ATLAS.md` (v0.2), `atlas/RTG_STATE_ATLAS_METHOD.md` (v0.2), `tools/atlas_check.py` and its report. The review packet with the L5 deletion list goes under `records/atlas/`.

## 5. Questions for the PI and the reviewer

1. **Size.** v0.1 is about 424k characters (≈110k tokens), above the 60–90k target. Should this refresh include a wording-compression pass (no fact removed), or keep size as it is and do compression separately later?
   - Proposal: separately later.
2. **Artifact RIDs.** Should certificate/script RIDs (`DYAD-ART-…`) be atlas nodes, or only cited as `cert` on the claims they support?
   - Proposal: cite as `cert`; no separate nodes.
3. **Atlas tags.** Tag atlas releases (`atlas-v0.2`) for traceability, even though the atlas is noncanonical?
   - Proposal: yes.
4. **Stream rollout after the refresh.** Proposal: Pass 2 advisories go to the remaining streams in the method's reading order, starting with RECOG. Each advisory is one record under `records/<study>/` and is never mentioned in the atlas.
