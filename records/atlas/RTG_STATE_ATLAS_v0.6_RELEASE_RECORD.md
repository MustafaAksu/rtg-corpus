# RTG State Atlas v0.6 — acceptance record

**Status:** PI ACCEPTED — 26 October 2026; PR #79 merged by merge commit `b3de0c52871902bf94a0640dca07d3f4feeb092c`; annotated tag `atlas-v0.6` on that merge commit, verified by the atlas owner (§3). Supersedes `atlas-v0.5`.
**Object:** derived NONCANONICAL Atlas; acceptance adopts no owner science.

## 1. Candidate identities

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` (candidate, PR #79 head `5ebe99ab84a6dda2386e49fdaae4f0fbcf355af6`) | `35ebee6d61f4db93211f2ed6f2de2bb973aa2fc6f2ea3cdf670656b1e961bd8a` (479,995 bytes, 1,544 lines) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.6/source_manifest.json` | `c4ce6967a34802c780139e08df9653883c6635d16cec399e1c62c947fded17eb` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_6.py` | `b8cbe56068e81bbfe31fb5ff4a5969af042faffebc5ca5791159d5a321a1ab48` |

## 2. Basis and limits

Method v0.2; `records/atlas/ATLAS_V0_6_REVIEW_PACKET.md`; verification files under `evidence/atlas/v0.6/`. Source snapshot `38ed5bb1fb7324d939007981f6671d2ac18e8070` (after PR #78); the only moved source is Number Genesis v1.21 (`numgen-v1.21`, file `4805760d…5701`, tag verified 26 Oct). Impact refresh of one domain; no other domain re-extracted; no certificate replay; the five new RIDs checked for presence in the tagged source only. Carried checker results unchanged by text from v0.5: 4 link + 3 artifact UNVERIFIED, 11 DOCUMENTED-UNRESOLVED, 16 wording warnings; one new link UNVERIFIED (`NUMGEN-CAND-N5AS1-LOGSLIP`, registration line at tag `numgen-v1.20.8`; documented at NUMGEN.N-T1, not to be forced to PASS).

## 3. Decision

- Receiving review: ChatGPT, 26 Oct 2026, `records/atlas/ATLAS_V0_6_RECEIVING_REVIEW.md` (PR #80, branch `chatgpt/atlas-v0.6-review`, head `f2cdb02`, file SHA-256 `3bc06b4c…`): **ACCEPT** on the exact candidate `35ebee6d…bd8a` (PR #79 comment `6426506117`): row-A import as a separate THM without upgrading the native L-PHASE; RECOG A1a/A1b as independent agreement only; domain aliases with no inclusion; five exact owner RIDs; seven L5 retirements and `NUMGEN.N-I1` accurate; the LOGSLIP UNVERIFIED declared and non-blocking. The receiving review did not independently rerun the build or owner certificates.
- PI acceptance: **ACCEPTED** in the project conversation, 26 October 2026 (the PI's "tag işi tamam" message confirms the acceptance of the bytes `35ebee6d61f4db93211f2ed6f2de2bb973aa2fc6f2ea3cdf670656b1e961bd8a` on which the merges were made). Acceptance adopts a NONCANONICAL derived map, not owner science.
- Merge: PR #79 head `a515a78c88103d20e8ae492b4cf748c160d0a810` merged into `main` by merge commit `b3de0c52871902bf94a0640dca07d3f4feeb092c` (parents `38ed5bb` main, `a515a78`), not squash; PR #80 (receiving review record) merged separately at `6761ed2a61b7115ad4ae51405c23113c5817f909`.
- Tag: annotated `atlas-v0.6` created by the PI, 26 October 2026; tag object `cd125d0725b826e29694f128cd04e7c9ea1e5d03` → merge commit `b3de0c52871902bf94a0640dca07d3f4feeb092c` (the PR #79 merge, not the later PR #80 review commit); message names the Atlas SHA-256. Verified by the atlas owner from `origin`: tag type `tag`; `atlas/RTG_STATE_ATLAS.md` at the tag and at `main` both recomputed to SHA-256 `35ebee6d61f4db93211f2ed6f2de2bb973aa2fc6f2ea3cdf670656b1e961bd8a` (479,995 bytes); candidate, record and review commits (`5ebe99a`, `a515a78`, `f2cdb02`, `6761ed2`) reachable from `main`. The co-owner's blob-equality check (PI message) is confirmed by this full-hash recomputation.
- Next: TDR-G advisory (two independent passes: atlas owner, then ChatGPT blind; reconciliation; TDR-G co-owner dispositions), centred on the orientation policy at S=0, |E|=N/2 (`pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md`) and the DISC witness scope; Programme next edition carries E-P13-1/E-P13-2 (PROG.G8); OFN/FMS/ER-2B class-C wording (H1).
