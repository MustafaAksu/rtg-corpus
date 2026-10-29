# RTG State Atlas v0.7 — acceptance record

**Status:** PI ACCEPTED — 28 October 2026; PR #100 merged by merge commit `8ece2a59a0962e6433d19f3c8203345ab22d4c1b`; annotated tag `atlas-v0.7` on that merge commit, verified by the atlas owner (§3). Supersedes `atlas-v0.6`.
**Object:** derived NONCANONICAL Atlas; acceptance adopts no owner science.

## 1. Candidate identities

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` (candidate rev. 2, PR #100 head `ae4d505c4f22835525a72feb89023ddc21af31af`) | `8ebfbd1008ce96e167ec90931468d166c568294a66453824667fba88e3f49c6c` (492,059 bytes, 1,545 lines) |
| `atlas/RTG_STATE_ATLAS.md` (candidate rev. 1, PR #100 commit `15793e747178aef7ec30974493bdeab4ab83d311`, the bytes the receiving review read) | `3655d4043e5eee046e93811d37b1fbe7bc863146dceed8b95c4e9d031ca53078` (492,007 bytes) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.7/source_manifest.json` | `e88e5b15037261eb0c694d908e0330b951e0b006c095cdd0a1e445419d43865d` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_7.py` (rev. 2) | `519c57e580c8cd22fcb42ecbdf3d00592cd2fe06334da7eb84f2005987ed70ed` |

Rev. 1 → rev. 2: one line of the Atlas changed — the tail of the D3 `RECOG-THM-A1B-SLIP-SCHEDULE-U` node, "`supplied in place ( change)`" → "`supplied in place (known-a only; the unknown-a windows are at the readout node)`" — the builder slip the receiving review reported as its editorial note; checker counts, controls and the manifest unchanged (packet rev. 2 header).

## 2. Basis and limits

Method v0.2; `records/atlas/ATLAS_V0_7_REVIEW_PACKET.md`; verification files under `evidence/atlas/v0.7/`. Source snapshot `53b56e4445a8c2869e41198e30bc66aa0fb93073` (after PR #99); the two moved sources are Discrete Genesis v2.12.14 (`tdrg-v2.12.14` → `05c7e78a…`, file `3be72923…2392`, tag verified 28 Oct, PR #98) and RECOG v0.3.25 (`recog-v0.3.25` → `bdb37123…`, file `86cae8ff…db7b`; file hash equal at the tag and at the snapshot by builder assertion; no separate atlas tag-verification record for this tag). Impact refresh of two domains; no other domain re-extracted; no certificate replay; the 44 cited new RIDs checked for presence in the tagged sources only; the ten `[conv: v18 path orientation]` TDR-G results carried EV-NOT-RERUN with the three-node census bound. Carried checker results unchanged by text from v0.6: 5 link + 3 artifact UNVERIFIED, 11 DOCUMENTED-UNRESOLVED, 16 wording warnings (same sites).

## 3. Decision

- Receiving review: ChatGPT, 28 Oct 2026, `records/atlas/ATLAS_V0_7_RECEIVING_REVIEW.md` (PR #101, branch `chatgpt/atlas-v0.7-review`, head `a1d994b`, file SHA-256 `dc81d533e1e67ef265317f6f377974842a2a4be593f79e69f5a81dfd9f4a2ca9`): **ACCEPT** on the rev. 1 bytes `3655d404…3078` (PR #100 comment `6479571563`), scoped to the two moved sources; all five packet questions ACCEPT; one non-blocking editorial note (the "( change)" tail), resolved by rev. 2, which changes nothing else. The receiving review did not independently rerun the build or owner certificates.
- PI acceptance: **ACCEPTED** in the project conversation, 28 October 2026 ("bende kabul ediyorum"), and by the tag message, which names the rev. 2 bytes `8ebfbd1008ce96e167ec90931468d166c568294a66453824667fba88e3f49c6c`. Acceptance adopts a NONCANONICAL derived map, not owner science.
- Merge: PR #100 head `ae4d505c4f22835525a72feb89023ddc21af31af` merged into `main` by merge commit `8ece2a59a0962e6433d19f3c8203345ab22d4c1b` (parents `a63d5161…` main, `ae4d505c…`), not squash; PR #101 (receiving review record) merged separately at `0ad2cd301fe07790d4926f266de9ffd18b911e21`; the pending tag records PR #81 (`atlas-v0.6`, merge `6acdd25`) and PR #98 (`tdrg-v2.12.14`, merge `a63d516`) merged in the same round.
- Tag: annotated `atlas-v0.7` created by the PI, 28 October 2026; tag object `643120ce08fba201dfa48e3f76874c3df89dedb8` → merge commit `8ece2a59a0962e6433d19f3c8203345ab22d4c1b` (the PR #100 merge); message "RTG State Atlas v0.7 — NONCANONICAL; PI accepted 28 October 2026; SHA-256 8ebfbd10…9c6c". Verified by the atlas owner from `origin`: tag type `tag`; `atlas/RTG_STATE_ATLAS.md` at the tag and at `main` both recomputed to SHA-256 `8ebfbd1008ce96e167ec90931468d166c568294a66453824667fba88e3f49c6c` (492,059 bytes); the builder rerun on `main` after the merge reproduces the same bytes; candidate, record and review commits (`15793e7`, `ae4d505`, `a1d994b`, `0ad2cd3`) reachable from `main`.
- Next: RECOG v0.3.26 (stage 1 open, PR #96; atlas refresh when adopted); NUMGEN's re-annotation of DISC-1/DISC-2 under `TDRG-DEF-ORIENT` and its C7C-M4 release decision (D5.X1); TDR-G v2.13 (Methodology v1.4 migration, footer/Appendix A layout, TDRG.G8) and the later sensitivity campaign ((a) vs (b)); the held motif corpora and the four missing certificate suites (TDRG.G11); Programme next edition (E-P13-1/E-P13-2, κ_f, the owner-review tasks); OFN/FMS/ER-2B class-C wording (H1); receiver dispositions of the open pipe items (RECOG, DYAD, GEN, OFN, AZ; NUMGEN.N-I1).
