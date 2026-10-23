# RTG State Atlas v0.3 — acceptance record

**Status:** DRAFT — receiving corrections V1–V3 implemented; final receiving readback and PI decision pending.
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

- Receiving review: Claude, 23 Oct 2026, `records/atlas/ATLAS_V0_3_RECEIVING_REVIEW.md` at commit `afdef2bf2ae9e40f42cb42fde6facc5756d322e0`: REVISE (V1–V3). Corrections implemented; final receiving readback pending.
- PI acceptance: pending; not supplied by this generator.
- Annotated tag after acceptance and merge: `atlas-v0.3`, naming the final Atlas SHA-256.
- No Atlas merge, tag, or owner-science adoption is performed by this build.
