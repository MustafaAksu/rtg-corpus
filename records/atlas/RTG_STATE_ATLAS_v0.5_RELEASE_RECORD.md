# RTG State Atlas v0.5 — acceptance record

**Status:** DRAFT — candidate under receiving review; not accepted. `atlas-v0.4` governs until the PI decision in §3.
**Object:** derived NONCANONICAL Atlas; acceptance adopts no owner science.

## 1. Candidate identities

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` | `cf250c9140e6ee26c65b2497a2a61dc1e326a69574d590132f0cea9646a2b0e5` |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.5/source_manifest.json` | `923e87cc59c803359ed44dc87f333cf10911b3bf887c59d7f9f0fa8c38cc9ce3` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_5.py` | `b08fafa347a0a316dae21749b801482338949e9ad70a1696eae70201d1fa212e` |

## 2. Basis and limits

Method v0.2; `records/atlas/ATLAS_V0_5_REVIEW_PACKET.md`; verification files under `evidence/atlas/v0.5/`. Source snapshot `75f8dc95520aaceac6a36614016902b408a8b52e`; moved sources Genesis v2.9 (`gen-v2.9`) and RECOG v0.3.24 (`recog-v0.3.24`); Dyadic unchanged (v6.4.22). Impact refresh of two domains; no other domain re-extracted; no certificate replay; new-node RIDs checked for presence in the tagged sources only. Carried checker results unchanged by text from v0.4: 7 UNVERIFIED, 11 DOCUMENTED-UNRESOLVED, 16 wording warnings; v0.1 input-equality unknowns for 13 sources.

## 3. Decision

- Receiving review: ChatGPT, 25 Oct 2026, `records/atlas/ATLAS_V0_5_RECEIVING_REVIEW.md` (PR #58, `9a419073`): REVISE (AV05-R1, AV05-R2) on the first candidate `3479e046…7cec`; corrections applied (packet §6); readback of the second candidate `cf250c91…b0e5`: _pending_.
- PI acceptance: _pending_ — merge commit of `claude/atlas-v0.5` into `main` (not squash); accepted bytes `cf250c91…b0e5`.
- Tag: _pending_ — annotated `atlas-v0.5` on the merge commit, message naming the hash; verified by the atlas owner after creation.
- Next: NUMGEN advisory (two independent passes); Programme next edition carries E-P13-1/E-P13-2 (PROG.G8); OFN/FMS/ER-2B class-C wording (H1).
