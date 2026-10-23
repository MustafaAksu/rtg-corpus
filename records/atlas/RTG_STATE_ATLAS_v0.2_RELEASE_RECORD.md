# RTG State Atlas v0.2 — acceptance record

**Status:** DRAFT — receiving review ACCEPT SCOPED; PI decision pending. Nothing below is PI-accepted until the PI fills in §3.
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
- Receiving review 1: `records/atlas/ATLAS_V0_2_RECEIVING_REVIEW.md` at `98f1ef4db546aea97632104499c2c894fd4c1663` (ChatGPT, 23 Oct 2026, REVISE: AV02-01–04), applied (review packet §12).
- Receiving review 2: ChatGPT, 23 October 2026, **ACCEPT SCOPED — no blocking receiving finding remains** for correction commit `9660389eb755558cba1912f5a341d297534db25d`; current `records/atlas/ATLAS_V0_2_RECEIVING_REVIEW.md`, SHA-256 `6ae3ddd8f1158651c0357616368be0b57a23e9ebd5f5476072cbc67c751b863b`. Receiver replay: six component fixtures, 6/6 expected; full 18-control producer report inspected, not independently rerun. Summary: `evidence/atlas/review_v0_2/round2_receiver_results.json`. Review §4 preserves the evidence limitations and the nonblocking DZT numerical-grouping note.

## 3. Decision

- PI decision: **accept** ("Current version adapted as is") — 23 October 2026. PR #11 merged with merge commit `6c526669181e4950a7d0361f178f9b49f8940c37` (parents `44b55d6`, `c5effbc`); atlas SHA-256 at the merge commit equals §1.
- Tag: annotated `atlas-v0.2` on `6c52666`, message naming the atlas SHA-256 of §1.
- Accepted limitations (not PASS): 7 UNVERIFIED checker items, 11 DOCUMENTED-UNRESOLVED names, 13 sources with UNVERIFIED v0.1-input byte equality; nonblocking presentation note (DZT 80-digit norm list belongs in the numerical part of `*ATLAS:checked-D2`), deferred to the next presentation pass.
- Next stream (plan Q4, accepted in the plan review): RECOG advisory from this snapshot, recorded under `records/recog/`.
