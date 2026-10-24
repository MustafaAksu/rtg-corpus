# RTG State Atlas v0.4 — acceptance record

**Status:** PI ACCEPTED — 24 October 2026; PR #33 merged by merge commit `96d9670fb3f07daa635cadfd3544fce20efea308`; annotated tag `atlas-v0.4` on that merge commit, verified by the atlas owner (§3). Supersedes `atlas-v0.3`.
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

- Receiving review: ChatGPT, 24 Oct 2026, `records/atlas/ATLAS_V0_4_RECEIVING_REVIEW.md` (PR #34, merged `8fff65f65ed2b322ed223d8396f2a738c5e4a978`): initial REVISE V04-01/V04-02 on candidate `988d0fa9…6b3c4`; corrected candidate `b63eaf8b…5c35b` ACCEPT on focused source readback (review commit `2ebfb86752003b2131ec2de283c7119f1ce69118`). Producer structural checks and inherited scientific certificates were not independently rerun by the receiving reviewer.
- PI acceptance: ACCEPTED explicitly in the project conversation, 24 October 2026 ("Ben de benimsiyorum. lütfen yapabildiğin repo işlemlerini yap..."). Accepted derived Atlas bytes: SHA-256 `b63eaf8b85dbb1f4a8fbee61cb82f2af089276797c387e6a8a0b13922805c35b`, 469,991 bytes. PR #33 head `1039075b86d0a1572b25da277b8b7d499a04de2e` merged into `main` with merge method `merge`, commit `96d9670fb3f07daa635cadfd3544fce20efea308`. PR #34 (review record only) merged separately at `8fff65f65ed2b322ed223d8396f2a738c5e4a978`. No owner science adopted.
- Tag: annotated `atlas-v0.4` created by the PI, 24 October 2026; tag object `467246533db8b471a910af18e32a9c0cec7016a7` → merge commit `96d9670fb3f07daa635cadfd3544fce20efea308`; message names the Atlas SHA-256. Verified by the atlas owner from `origin`: tag type `tag`, target is the PR #33 merge commit (not a later records-only commit); `atlas/RTG_STATE_ATLAS.md` at the tag and at `main` both hash to `b63eaf8b85dbb1f4a8fbee61cb82f2af089276797c387e6a8a0b13922805c35b`; the candidate, audit, review and readback commits (`1039075`, `1ad2f6c`, `c0cbbc5`, `aaddc51`, `2ebfb86`) are reachable from `main` after the branch deletions. Independent ChatGPT audit PR #31 (`chatgpt/atlas-v0.4-independent-audit`, commit `284e49d`, file SHA-256 `882eac50…b04c10`) is now merged into `main` by merge commit `8aae02368806bbbf50ecf80dc162b7c81b0cf908`, preserving the independent audit cited by the reconciliation.
- Next: Genesis advisory (two independent passes), then NUMGEN; Programme next edition carries E-P13-1.
