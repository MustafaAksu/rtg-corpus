# RTG State Atlas v0.2 — acceptance record

**Status:** DRAFT — PI decision pending. Nothing below is accepted until the PI fills in §3.
**Object:** derived, NONCANONICAL product (Method v0.2 §2). Acceptance identifies this atlas edition; it adopts no owner science, changes no DSN and gives the atlas no authority over any stream.

## 1. Identities

| object | path | SHA-256 |
|---|---|---|
| Atlas v0.2 | `atlas/RTG_STATE_ATLAS.md` | `9963aead02fad686a9a5bd4d1824882a890ef6279d50899c4090e0e5092331c5` |
| Method v0.2 | `atlas/RTG_STATE_ATLAS_METHOD.md` | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| Source manifest (18 sources at their tags) | `evidence/atlas/source_manifest_v0_2.json` | `35013c11eea7b6854287e0ab69db04b81ccbc15de63b23850fcf0eacc75e5a98` |
| Checker | `tools/atlas_check.py` | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| Checker data | `evidence/atlas/coverage_map_v0_2.json`, `owner_identifier_map_v0_2.json`, `retired_l5_keys_v0_2.json` | `31a5fcbe…45e2`, `dde03f8c…5ccb`, `85ee8e08…7ba77` |

Values are those after the AV02 corrections (review packet §1); if review edits change a file, the final values replace them here before the PI decision.

## 2. Basis

- Plan `records/atlas/ATLAS_REFRESH_PLAN.md` and its review `records/atlas/ATLAS_REFRESH_PLAN_REVIEW.md` (ACCEPT WITH SCOPED EDITS, ARP-01–05).
- Review packet `records/atlas/ATLAS_V0_2_REVIEW_PACKET.md`; L5 dispositions `records/atlas/ATLAS_V0_2_L5_DISPOSITIONS.md`.
- Check report `evidence/atlas/atlas_check_report_v0_2.md` (no FAIL; 4 link and 3 artifact UNVERIFIED, 11 DOCUMENTED-UNRESOLVED listed separately) and controls `evidence/atlas/atlas_check_selftest_v0_2.txt` (18/18 as expected, including the receiving-review fixtures).
- Separate limitation: byte equality with the v0.1 extraction input is UNVERIFIED for 13 sources.
- Receiving review 1: `records/atlas/ATLAS_V0_2_RECEIVING_REVIEW.md` (ChatGPT, 23 Oct 2026, REVISE: AV02-01–04), applied (review packet §12).
- Receiving review 2 (focused on the AV02 corrections): _(reviewer, date, verdict — to be added)_.

## 3. Decision

- PI decision: _(accept / accept with edits / reject)_ — date: _( )_
- Tag after merge: annotated `atlas-v0.2` on the merge commit, message naming the atlas SHA-256 of §1.
- Next stream (plan Q4, accepted in the plan review): RECOG advisory from this snapshot, recorded under `records/recog/`.
