# RTG State Atlas v0.4 — acceptance record

**Status:** DRAFT — candidate under receiving review; not accepted. `atlas-v0.3` governs until the PI decision in §3.
**Object:** derived NONCANONICAL Atlas; acceptance adopts no owner science.

## 1. Candidate identities

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` | `b63eaf8b85dbb1f4a8fbee61cb82f2af089276797c387e6a8a0b13922805c35b` |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.4/source_manifest.json` | `dc8a840694f6da4cb42b5829efac02c4021c36a7ba52ac801b4e1d29409ca037` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_4.py` | `c2e405c33c8c2ca5d929d280c3570141f6f6eca8d44869087e1dac67515eeca9` |

## 2. Basis and limits

Method v0.2; `records/atlas/ATLAS_V0_4_RECONCILIATION.md` (two independent audits, reconciled); `records/atlas/ATLAS_V0_4_REVIEW_PACKET.md`; verification files under `evidence/atlas/v0.4/`. Source snapshot `21edfb8d019f6f3130217035f387855cde87ce87`; the only moved source is Programme v1.3 (`programme-v1.3`). Internal-consistency refresh only: no scientific domain re-extracted; A04-06 (Genesis sign conventions) deferred to the Genesis advisory. Carried checker results unchanged by text from v0.3: 7 UNVERIFIED, 11 DOCUMENTED-UNRESOLVED, 16 wording warnings; v0.1 input-equality unknowns for 13 sources; no certificate replay.

## 3. Decision

- Receiving review: ChatGPT, 24 Oct 2026, `records/atlas/ATLAS_V0_4_RECEIVING_REVIEW.md` (commit `aaddc51a…0362e`, PR #34): REVISE (V04-01, V04-02) on the first candidate `988d0fa9…6b3c4`; corrections applied by the atlas owner (packet §6); readback of the second candidate `b63eaf8b…5c35b`: _pending_.
- PI acceptance: _pending_ — to be filled with date, merge commit of `claude/atlas-v0.4` into `main` (merge commit, not squash) and the accepted bytes `b63eaf8b…5c35b`.
- Tag: _pending_ — annotated `atlas-v0.4` on the merge commit, message naming the hash; verified by the atlas owner after creation.
- Next: Genesis advisory (two independent passes), then NUMGEN; Programme next edition carries E-P13-1.
