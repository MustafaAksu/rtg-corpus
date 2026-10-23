# RTG State Atlas v0.2 — acceptance record

**Status:** DRAFT — PI decision pending. Nothing below is accepted until the PI fills in §3.
**Object:** derived, NONCANONICAL product (Method v0.2 §2). Acceptance identifies this atlas edition; it adopts no owner science, changes no DSN and gives the atlas no authority over any stream.

## 1. Identities

| object | path | SHA-256 |
|---|---|---|
| Atlas v0.2 | `atlas/RTG_STATE_ATLAS.md` | `8a5b51d2356fbb460d90d5fe37c5f13aa72b9035759ca60934980f7368bbf167` |
| Method v0.2 | `atlas/RTG_STATE_ATLAS_METHOD.md` | `afa4127f0f12b30da689ef94a5d2eae905df82c168dc342fb646765c12f29d7f` |
| Source manifest (18 sources at their tags) | `evidence/atlas/source_manifest_v0_2.json` | `35013c11eea7b6854287e0ab69db04b81ccbc15de63b23850fcf0eacc75e5a98` |
| Checker | `tools/atlas_check.py` | `4377a389f34871bd15d3b827fcac6272dcead5018557a21478b34ed4ab471d1d` |

Values are those of the review packet; if review edits change a file, the final values replace them here before the PI decision.

## 2. Basis

- Plan `records/atlas/ATLAS_REFRESH_PLAN.md` and its review `records/atlas/ATLAS_REFRESH_PLAN_REVIEW.md` (ACCEPT WITH SCOPED EDITS, ARP-01–05).
- Review packet `records/atlas/ATLAS_V0_2_REVIEW_PACKET.md`; L5 dispositions `records/atlas/ATLAS_V0_2_L5_DISPOSITIONS.md`.
- Check report `evidence/atlas/atlas_check_report_v0_2.md` (no FAIL; UNVERIFIED items listed separately) and negative controls `evidence/atlas/atlas_check_selftest_v0_2.txt` (all detected).
- Change-focused review: _(reviewer, date, verdict, file and hash — to be added)_.

## 3. Decision

- PI decision: _(accept / accept with edits / reject)_ — date: _( )_
- Tag after merge: annotated `atlas-v0.2` on the merge commit, message naming the atlas SHA-256 of §1.
- Next stream (plan Q4, accepted in the plan review): RECOG advisory from this snapshot, recorded under `records/recog/`.
