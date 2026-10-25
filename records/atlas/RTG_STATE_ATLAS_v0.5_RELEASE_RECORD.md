# RTG State Atlas v0.5 — acceptance record

**Status:** DRAFT — candidate under receiving review; not accepted. `atlas-v0.4` governs until the PI decision in §3.
**Object:** derived NONCANONICAL Atlas; acceptance adopts no owner science.

## 1. Candidate identities

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` | `3479e046bffeb2e521237a7ee4a537a5b269f5d590f05f9653974e647d3a7cec` |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.5/source_manifest.json` | `923e87cc59c803359ed44dc87f333cf10911b3bf887c59d7f9f0fa8c38cc9ce3` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_5.py` | `6c5912b4edf6df861b222486f64040353e625e8e8390ceb24f4c0b71e22cc1f1` |

## 2. Basis and limits

Method v0.2; `records/atlas/ATLAS_V0_5_REVIEW_PACKET.md`; verification files under `evidence/atlas/v0.5/`. Source snapshot `75f8dc95520aaceac6a36614016902b408a8b52e`; moved sources Genesis v2.9 (`gen-v2.9`) and RECOG v0.3.24 (`recog-v0.3.24`); Dyadic unchanged (v6.4.22). Impact refresh of two domains; no other domain re-extracted; no certificate replay; new-node RIDs checked for presence in the tagged sources only. Carried checker results unchanged by text from v0.4: 7 UNVERIFIED, 11 DOCUMENTED-UNRESOLVED, 16 wording warnings; v0.1 input-equality unknowns for 13 sources.

## 3. Decision

- Receiving review: _pending_ (ChatGPT, Atlas co-owner).
- PI acceptance: _pending_ — merge commit of `claude/atlas-v0.5` into `main` (not squash); accepted bytes `3479e046…7cec`.
- Tag: _pending_ — annotated `atlas-v0.5` on the merge commit, message naming the hash; verified by the atlas owner after creation.
- Next: NUMGEN advisory (two independent passes); Programme next edition carries E-P13-1/E-P13-2 (PROG.G8); OFN/FMS/ER-2B class-C wording (H1).
