# RTG State Atlas v0.3 — acceptance record

**Status:** ACCEPTED by the PI, 23 October 2026 (§3); receiving readback ACCEPT. Tag `atlas-v0.3` on merge commit `bfd88cd`.
**Object:** derived NONCANONICAL Atlas; acceptance adopts no owner science.

## 1. Candidate identities

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` | `71310e8c5e1b29979a854ee2ee932efa4765f038bbe0c10299e14f424ad1dc5b` |
| `atlas/RTG_STATE_ATLAS_METHOD.md` | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.3/source_manifest.json` | `db347c8f48da659d1f491fc8f764b6cbc7de2c729c2c1eba1a449f0985b10c96` |
| `tools/atlas_check.py` | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_3.py` | `9ab9c8d6dfed9c87b725244ac63d4b4fcfcbc79269f26e722bb5ed833da6b458` |

## 2. Basis and limits

Method v0.2; `records/atlas/ATLAS_V0_3_REVIEW_PACKET.md`; source and verification manifests under `evidence/atlas/v0.3/`. Source freeze `9453e35cec6d5a4da076652527c13176db27f6f8`; the only changed scientific source is RECOG v0.3.23. Retain checker UNVERIFIED/documented-unresolved results, historical v0.1 input limitations, non-replayed inherited certificates, unchanged consumer pins, and the RECOG historical-block exception. General compression and unadopted research remain outside this acceptance.

## 3. Decision

- Receiving review: Claude, 23 Oct 2026, `records/atlas/ATLAS_V0_3_RECEIVING_REVIEW.md`: REVISE (V1–V3) on the first candidate `dad84402…87c3` (review at `afdef2bf…22e0`); corrections implemented by the co-owner (`d6f3d2d`); readback of the corrected candidate `71310e8c…dc5b`: **ACCEPT** (§5 of the review, commit `72e3ad4`).
- PI acceptance: **ACCEPTED**, PI (Mustafa), 23 October 2026, by merge of PR #25 (`claude/atlas-v0.3-accept`, carrying `chatgpt/atlas-v0.3` through `d6f3d2d` plus the readback) into `main` as merge commit `bfd88cd5c4c8069537dd01f42e9f1b225bdc4518` ("Accepted and aproved."). Accepted bytes: `atlas/RTG_STATE_ATLAS.md` SHA-256 `71310e8c5e1b29979a854ee2ee932efa4765f038bbe0c10299e14f424ad1dc5b`.
- Tag: annotated `atlas-v0.3` on `bfd88cd`, message naming that hash (verified by the atlas owner: tag object → merge commit; file at the tag has the hash; `d6f3d2d` and `72e3ad4` reachable from `main`).
- Accepted limitations (unchanged from the packet): 7 UNVERIFIED links, 11 DOCUMENTED-UNRESOLVED items, 16 wording warnings, v0.1 input-equality unknowns for 13 sources, no certificate replay. No owner DSN, grade, source tag, notice state or consumer adoption is changed by this acceptance. `atlas-v0.2` is the predecessor.
- Next: the next refresh follows the next adopted owner edition; D3 carries the RECOG live-file exception (release record §11) as history, not as live OPEN items.
