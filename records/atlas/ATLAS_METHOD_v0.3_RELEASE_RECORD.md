# RTG State Atlas — Method v0.3 — acceptance record

**Status:** PI ACCEPTED, 12 November 2026. The merge of PR #234 and the annotated tag `atlas-method-v0.3` are pending (§4). Method v0.2 (identified by `atlas-v0.2`) stays the tagged method until both exist and are verified.
**Object:** the working method of a derived, NONCANONICAL product. Not a DSN; acceptance adopts no owner science and changes no atlas byte.
**Recorded by:** Claude, Atlas owner, on branch `claude/atlas-method-v0.3` (PR #234). Under CONVENTIONS §4 this record comes before the merge and the tag.

## 1. Object

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS_METHOD.md`, v0.3 | `a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f` (16,239 bytes, 139 lines) |
| predecessor v0.2, at `atlas-v0.2` | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` (12,985 bytes) |
| `atlas/RTG_STATE_ATLAS.md` (unchanged, v0.12 at `atlas-v0.12`) | `cf9d8647b4c33206537e46ca37c7879d4fc33b1a936e0a50330a469f054def55` |

Against v0.2: twelve anchored replacements (15 lines added, 10 removed in the line diff); everything else byte-identical. The changes, the source of each rule and what is deliberately left unchanged: `records/atlas/ATLAS_METHOD_V0_3_DELTA.md` §§2–3, 6.

## 2. Basis and limits

- The delta writes down practice already decided by the PI and applied and reviewed in Atlas v0.10–v0.12; it introduces no rule that had not been applied.
- No tool is changed. `tools/atlas_check.py` names the Method in a comment only; the builders are unchanged.
- Atlas v0.12 was built under v0.2 and its manifest says so; that record is not edited. The next atlas manifest names `method_edition` v0.3 and `method_tag` `atlas-method-v0.3`.
- Rule 4.6 withdraws the former quantitative size target. The measured figures are in `records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md` and the v0.11 and v0.12 records, not in the Method.

## 3. Decision

**PI decisions on the four open points,** 12 November 2026, 11:36 +03:00 (delta §6, verbatim there): the tag name `atlas-method-v0.3` is suitable; numbers only in the records; the boundary test of rule 4.1 is clear enough; "editions are built, not hand-edited" is correct.

**Receiving review.** ChatGPT, Atlas co-owner.
- PR #234 review 5871391538 on `c3be81b1`: ACCEPT WITH CHANGE — the twelve declared changes and nothing else verified against `atlas-v0.2`; one required change, rule 4.6 without figures, with its text.
- PR #234 review 5872066576 on `b640123a551eb5752f5167c00f4765ca7920dd5d`: **ACCEPT SCOPED** — only line 49 (rule 4.6) differs from the first candidate; the other 138 lines byte-identical; the rule carries the reviewer's text; hash recomputed independently; the delta's §6 checked.

**PI acceptance: ACCEPTED** in the project conversation, 12 November 2026, 12:39 +03:00, in the message that relayed the final review. Verbatim: "Method v0.3 'ü benimsiyorum." ("I adopt Method v0.3.") The object is that of §1, `a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f`, the one the review names by hash.

## 4. Publication (pending; the PI executes)

1. `BASELINE.md`: "ATLAS Method" row set to v0.3 with the hash of §1 and this record (done on the branch with this record).
2. Merge PR #234 into `main` with a merge commit, not squash.
3. Annotated tag `atlas-method-v0.3` on that merge commit, after checking the file hash on `main`.
4. The Atlas owner writes the tag verification.
