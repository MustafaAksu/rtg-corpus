# RTG State Atlas v0.5 — acceptance record

**Status:** PI ACCEPTED — 25 October 2026; PR #57 merged by merge commit `b77c8c7a488bbb2ec7e72fda6ec5f55c1fc80c22`; annotated tag `atlas-v0.5` on that merge commit, verified by the atlas owner (§3). Supersedes `atlas-v0.4`.
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

- Receiving review: ChatGPT, 25 Oct 2026, `records/atlas/ATLAS_V0_5_RECEIVING_REVIEW.md` (PR #58, merged `398b52d082f0da4f4efcdb4211ac91742e4c566a`): REVISE (AV05-R1/R2) on first candidate `3479e046…7cec`; the three-line correction at PR #57 head `34fc66beb0c7dea54fdb96b71e0d2fcb8e094779` was independently source-read and **ACCEPTED** for candidate `cf250c91…b0e5` (review readback commit `470a6ae136eb442f2a43eccb46f1272dabf89875`). This receiving review did not independently rerun the build or owner certificates.
- PI acceptance: **ACCEPTED** in the project conversation, 25 October 2026 (conditional on focused receiving check, fulfilled above; PI authorized merge and necessary repository steps). Accepted derived Atlas file SHA-256 `cf250c9140e6ee26c65b2497a2a61dc1e326a69574d590132f0cea9646a2b0e5` (producer-reported 477,266 bytes). PR #57 merged by merge commit `b77c8c7a488bbb2ec7e72fda6ec5f55c1fc80c22`, not squash; PR #58 receiving review merged independently at `398b52d082f0da4f4efcdb4211ac91742e4c566a`. Acceptance adopts a NONCANONICAL derived map, not owner science.
- Tag: annotated `atlas-v0.5` created by the PI, 25 October 2026; tag object `eca72165ff30986d97ed166f3c101b89c8ec1962` → merge commit `b77c8c7a488bbb2ec7e72fda6ec5f55c1fc80c22` (parents `75f8dc9` main, `34fc66b` second candidate); message names the Atlas SHA-256. Verified by the atlas owner from `origin`: tag type `tag`; `atlas/RTG_STATE_ATLAS.md` at the tag and at `main` both recomputed to SHA-256 `cf250c9140e6ee26c65b2497a2a61dc1e326a69574d590132f0cea9646a2b0e5` (477,266 bytes); candidate and review commits (`34fc66b`, `9a419073`) reachable from `main`. The co-owner's blob-equality check (PR #57 thread) is confirmed by this full-hash recomputation.
- Next: NUMGEN advisory (two independent passes); Programme next edition carries E-P13-1/E-P13-2 (PROG.G8); OFN/FMS/ER-2B class-C wording (H1).
