# RTG State Atlas v0.9 — acceptance record

**Status:** PI ACCEPTED, 3 November 2026. The merge of PR #147 and the annotated tag `atlas-v0.9` are pending (§4). `atlas-v0.8` stays the tagged Atlas until both exist and are verified.
**Object:** a derived, NONCANONICAL Atlas. Acceptance adopts no owner science.
**Recorded by:** Claude, Atlas owner, on branch `claude/atlas-v0.9`. Under CONVENTIONS §4 this record comes before the merge and the tag. The tag verification is added after them.

## 1. Accepted object

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` — candidate rev. 2, PR #147 commit `e18cfb21d8eab260ab2ee43acd7c232cd2d1e7af`; the rev.-2 receiving review read these bytes | `b48343f5a4d4c066eb37a325ff87d1dadf686fc6c616b67e7a0ad418dcec3b70` (517,999 bytes, 1,547 lines) |
| `atlas/RTG_STATE_ATLAS.md` — candidate rev. 1, PR #147 commit `e2543cb159431d07be6869c5d69b0f6f464e36d7`; the first receiving review read these bytes | `c7f678edb5f2ea6c0ab58651ce3f6f97f5e2f816bcc3b07c6411d43f4429ae3a` (517,717 bytes) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.9/source_manifest.json` (unchanged rev. 1 → rev. 2) | `d9e84879deb2f34b63f6f4812b770e5e263aa110238397231bf8ec6d2f6009c3` |
| `evidence/atlas/v0.9/edit_log.json` (rev. 2, 49 operations) | `c9bfab2ef43a523d307c1633c419c78411ef3a03184a90b5f0015cdb343effb6` |
| `evidence/atlas/v0.9/dispositions.json` (rev. 2) | `128120c9cc95791d4983fefb3a0bca763947456944f11afd6b24599c8c77cc65` |
| `evidence/atlas/build/refresh_v0_9.py` (rev. 2) | `e3f86aa990f97ccdaa2aa6e1f43d281c84e985321484f9b8d0a9c23a410034b2` |
| `tools/atlas_check.py` (self-test NC7 made edition-independent) | `2141e0b991f21acfa2c4f2e0575e88d3ae5d1f43bffd00dafc4ef80d66f66373` (was `0db3a23b…004d`) |

**Rev. 1 → rev. 2:**
- Three builder operations changed: F32, PROG.G9 and NUMGEN.N-I1. These follow receiving-review notes A09-N1 and A09-N2, plus the snapshot wording.
- Five operations were added from the final-review sweep: the `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` consumer edge, the two AZ.A2 rows and the two Legacy-row pointers.

Review packet §6 has the details. The publication bytes equal the accepted bytes, because the Atlas carries no status line that publication would change.

## 2. Basis and limits

**Basis:**
- Method v0.2.
- `records/atlas/ATLAS_V0_9_REVIEW_PACKET.md` (rev. 2) and the verification files under `evidence/atlas/v0.9/`.
- Base `atlas-v0.8` (`47320ca5…71b7`).
- Source snapshot `f20f080`.

**The three moved sources:**

| Source | Tag | Tag object | Commit | File |
|---|---|---|---|---|
| Dyadic v6.4.23 | `dyad-v6.4.23` | `e32abf02…` | `ab8749b2…` | `9f874ccc…25cb` |
| OFN v0.12 | `ofn-v0.12` | `b313064f…` | `2b2573f5…` | `55ff8ba8…76aa` |
| Triadic v1.7 | `triad-v1.7` | `ed7da56f…` | `7568941d…` | `506f3403…e64a` |

The builder asserts each file hash at the tag and at the snapshot. The other 15 sources are byte-equal to their v0.8 inputs: 15 EQUAL and 3 CHANGED, asserted.

**Limits:**
- The checks are structural, and no owner certificate was rerun for this edition.
- New RIDs were checked for presence in the tagged sources, not re-proved.
- The TRIAD row-1 algebra and the owner row-1–3 scripts were checked in the Atlas row check of 2 November 2026 (`records/atlas/ATLAS_TRIAD_v1_7_29_ROW_CHECK_OWNER.md`).
- The receiving reviewer reapplied the edit log independently, byte for byte, in both rounds. The builder run, the checker and the 18 + 14 controls remain the producer's execution.

## 3. Decision

**Receiving review.** ChatGPT, Atlas co-owner. Record: `records/atlas/ATLAS_V0_9_CHATGPT_RECEIVING_REVIEW.md` (PR #149, branch `chatgpt/atlas-v0.9-receiving-review`, head `6b56fb1c32f6beea3299494a0030a1f9e602f3ad`, file SHA-256 `e27dc438fd52da5949b3c00dbc47552aa520efa81444fa99bf068fc8b78cf6d6`).
- **Round 1, on rev. 1** (PR #147 comment `6597141019`): **ACCEPT SCOPED, no blocking finding.**
  - Packet questions 1–3 ACCEPT: NUMGEN.N-Q\* retirement, the RECOG parentheticals and the causal-interface node.
  - Question 4 KEEP: F30 and F31 stay in D4a.
  - Question 5 ADVISORY.
  - Nonblocking notes: A09-N1 (F32) and A09-N2 (PROG.G9).
- **Round 2, on rev. 2** (record §6; PR #147 comment `6598068801`): **ACCEPT SCOPED, no blocker.**
  - The three changed operations: 3/3 PASS.
  - The five added operations: 5/5 PASS.
  - 49/49 exact-once matches; the independent reapplication equals the candidate.
  - The candidate hash `b48343f5…3b70` was recomputed independently.
  - One process note: the PR #147 description still showed the rev.-1 figures. It is updated with this record.

**PI acceptance: ACCEPTED** in the project conversation, 3 November 2026, 10:38 +03:00. Verbatim: "Bende Atlas v0.9 u bu haliyle benimsiyorum" ("I too adopt Atlas v0.9 as it stands"). The object at that moment is rev. 2, `b48343f5…3b70`, which the round-2 review names.

Acceptance adopts a NONCANONICAL derived map, not owner science. It changes no owner DSN, grade, source tag, Method edition or consumer adoption. Its only pipe-state changes are the Atlas owner's three items in `pipes/ATLAS/` (row-check request closed; DYAD and TRIAD notices dispositioned).

## 4. Publication (pending; the PI executes)

1. **Merge the PRs** into `main` with merge commits, not squash:
   - PR #149 (the receiving review record) may go before or with #147;
   - PR #147 itself.
2. **Create and push the annotated tag** on the PR #147 merge commit:
   ```powershell
   git fetch origin
   git checkout main; git pull --ff-only
   git log -1 --format="%H %P"          # the PR #147 merge commit
   (Get-FileHash atlas/RTG_STATE_ATLAS.md -Algorithm SHA256).Hash   # must be B48343F5…3B70
   git tag -a atlas-v0.9 -m "RTG State Atlas v0.9 — NONCANONICAL; PI accepted 3 November 2026; SHA-256 b48343f5a4d4c066eb37a325ff87d1dadf686fc6c616b67e7a0ad418dcec3b70"
   git push origin atlas-v0.9
   ```
3. **After the tag**, the Atlas owner:
   - verifies the tag (type, target, file hash at the tag and at `main`) and adds the result to a tag-verification record;
   - closes `pipes/ATLAS/20261030-DYAD-v6-4-23-adopted.md` and `pipes/ATLAS/20261103-TRIAD-v1-7-adopted.md` (state `closed`, disposition pointing here);
   - regenerates the inbox index (`tools/pipes_index.py`).

A merge, a tag or a passing check is not an adoption. The decision is the one in §3.

## 5. Carried forward

Each item belongs to its owner; nothing here is an obligation set by the Atlas.
- **RECOG:** re-check the A1c blocks against the registered `DYAD-THM-LPHASE-ROWA-BRIDGE` (c′_Q = 0.36916) and `DYAD-THM-NF-REM-C7-SHARP` before dropping `[assuming:]` (RECOG.R-A1). Repin to NUMGEN v1.21.
- **GEN:**
  - the two TRIAD questions, on the 𝒫₄ identity and the birth-symmetry grade (F30);
  - the `[CAND]` imports of T-6s, T-6t and T-6u at the Triadic v1.6 pins (F31);
  - the open OFN, NUMGEN and TRIAD notices.
- **Programme:** the consumer refresh of IF07/IF11 and the CN-05 record (PROG.G9), together with its other open notices.
- **TRIAD:** A-1 wording (F32). F-1, F-2 and row 29 stay in the TRIAD release record.
- **NUMGEN:** the q\* cross-citation (v1.21 NC-17) and the DYAD v6.4.23 notice.
- **Next Atlas refresh:** the pipe items filed after the snapshot (PR #148: DYAD notices N16–N21 to seven inboxes, the LIT finding and report), and any source tagged after `f20f080`.
- **Tool:** PR #113 (`tools/check_compaction.py` `history_appendix` profile) stays on its own review track.
