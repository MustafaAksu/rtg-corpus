# RTG State Atlas v0.10 — acceptance record

**Status:** PI ACCEPTED, 6 November 2026. The merges of PR #186 and PR #185 and the annotated tag `atlas-v0.10` are pending (§4). `atlas-v0.9` stays the tagged Atlas until all three exist and are verified.
**Object:** a derived, NONCANONICAL Atlas. Acceptance adopts no owner science.
**Recorded by:** Claude, Atlas owner, on branch `claude/atlas-v0.10`. Under CONVENTIONS §4 this record comes before the merge and the tag. The tag verification is added after them.

## 1. Accepted object

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md`: candidate rev. 2, PR #185 commit `f90d74e19c5d5b7ddaee8f2c50ec80efbbdc62b6`. The rev.-2 receiving review read these bytes. | `443b5990e6082599d1f43fca7d4d24e512e7a632ec395aa56f05bed16f53dbf7` (521,243 bytes, 1,543 lines) |
| `atlas/RTG_STATE_ATLAS.md`: candidate rev. 1, PR #185 commit `20878fbd41a17ac00e2ce0e17c0521ff252581ba`. The first receiving review read these bytes. | `ea7faa79d16228985f2b8e52e40db66b5dbb04a1f679f8d39360cecd7ab9d1bc` (520,786 bytes) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.10/source_manifest.json` (unchanged rev. 1 → rev. 2) | `32849944091e931bfb9461eb4b7c542772fbb2d7122c8e90867a574ba28c8c46` |
| `evidence/atlas/v0.10/edit_log.json` (rev. 2, 83 operations) | `9c5b191897c0440bfdf89929925dfab1f16f6ee06bdb2046de16276fb26ee5c5` |
| `evidence/atlas/v0.10/dispositions.json` (rev. 2) | `5e257f9f9fc620c11754142375b56bc0ccf86d4814643d50bedf5fd603fae025` |
| `evidence/atlas/build/refresh_v0_10.py` (rev. 2) | `9405436c738f9c3dd079975ce21d5a4a73d45181a2831634b43c6c7512f2e01c` |
| `tools/atlas_check.py` (unchanged since v0.9) | `2141e0b991f21acfa2c4f2e0575e88d3ae5d1f43bffd00dafc4ef80d66f66373` |
| `records/atlas/ATLAS_V0_10_REVIEW_PACKET.md` (rev. 2) | `8ca97ef232e7cde182776fc9fb71a741ba1d41f6f822802d8f58085e84cc3427` |

**Rev. 1 → rev. 2.** Three builder operations changed: `AR10-057`, `AR10-075` and `AR10-083`. The count stays at 83. As a result, three Atlas lines changed:
- D4a L1051: the one home node `GEN-ALG-BIRTH-SYMMETRY-SEED` (R1a);
- D4b L1204: the typed cross-reference (R1a);
- L1537: `LEGACY.Y6` changed from D-STALE to D-SCOPE (R1b).

The rev.-2 commit also corrected two metadata fields (`gen_repin_evidence`, and the split between RID kinds) and added four focused controls (V16–V19). Review packet §8 has the details.

**Publication bytes.** The publication bytes equal the accepted bytes, because the Atlas carries no status line that publication would change. On 6 November 2026 the builder was rerun on the branch in a fresh workspace. It reproduced every committed output byte for byte (`git status` clean).

## 2. Basis and limits

**Basis:**
- Method v0.2.
- `records/atlas/ATLAS_V0_10_REVIEW_PACKET.md` (rev. 2) and the verification files under `evidence/atlas/v0.10/`.
- Base `atlas-v0.9` (`b48343f5…3b70`).
- Source snapshot `main` `fa3db80a935a20b1eff64b0e14c6d0436f861852`.

**The three moved sources:**

| Source | Tag | Commit | File |
|---|---|---|---|
| Programme Overview v1.4 | `programme-v1.4` | `514e17f3…` | `37d857d0…f28c0` |
| Genesis Geometry v2.10 | `gen-v2.10` | `12bb2b39…` | `63c3b020…13d62` |
| Relational Recognition v0.3.27 | `recog-v0.3.27` | `7bad433b…` | `19556f91…0e1f1` |

The builder asserts each file hash at the tag and at the snapshot. The other 15 sources are byte-equal to their v0.9 inputs; the builder asserts 15 EQUAL and 3 CHANGED.

**Pipe census.** The census of 87 items is recorded at the frozen snapshot. Later pipe items do not change this edition; `main` held 88 after PR #182 and PR #184. The next refresh counts them at its own snapshot.

**Limits:**
- The checks are structural. No owner certificate was rerun for this edition, with two exceptions:
  - the RECOG jet-remainder certificate, rerun byte-identical;
  - the A1c chain rerun of the RA1 advisory (`evidence/recog/atlas_review/ra1/`).
- New RIDs were checked for presence in the tagged sources, not re-proved.
- The P4 identity was checked by hand in `records/gen/ATLAS_ADVISORY_GEN_INBOX_20261103.md` §6.
- The receiving reviewer reapplied the edit log independently, byte for byte, in both rounds. The builder run, the checker and the 18 + 19 controls remain the producer's execution.

## 3. Decision

**Receiving review.** ChatGPT, Atlas co-owner.

Record: `records/atlas/ATLAS_V0_10_CHATGPT_RECEIVING_REVIEW_20261104.md`.
- PR #186, branch `chatgpt/atlas-v0.10-receiving-review`, head `0a70b556377af8209e8474a97ea3f4d89a7b609c`.
- File SHA-256 `4a6be7d113420894eb07e4e0b6230a896876ac7eb09101f89ccc00d61216c85e`.

**Round 1, on rev. 1** (PR #185 comment `6634539731`): **CONDITIONAL PASS**.
- 83/83 edits reapplied independently, with full-text equality.
- The source hashes were recomputed.
- The F30, F14, RECOG.R-A1, F31, F18 and NUMGEN.N-L6 dispositions were supported.
- R1a: one home node for birth symmetry.
- R1b: Y6 typed as D-SCOPE.
- Two metadata notes.

**Round 2, on rev. 2** (record §7; PR #185 comment `6635225985`): **ACCEPT SCOPED, no blocker**.
- Exactly three changed lines and three changed log payloads.
- 83/83 exact-once replays reproduced the revised file.
- The 166/166 edit-log hashes and the candidate hash `443b5990…dbf7` were recomputed independently.
- R1a, R1b and the metadata notes: PASS.

**PI acceptance: ACCEPTED** in the project conversation, 6 November 2026, 14:17 +03:00. Verbatim: "Atlas v0.10 u benimsiyorum." ("I adopt Atlas v0.10.") The object at that moment is rev. 2, `443b5990…dbf7`, the candidate the round-2 review names.

Acceptance adopts a NONCANONICAL derived map, not owner science. It changes no owner DSN, grade, source tag, Method edition or consumer adoption. Its only pipe-state changes are the Atlas owner's three items in `pipes/ATLAS/`, all dispositioned:
- the TRIAD Y6/F18 readings;
- the PROG v1.4 notice;
- the RECOG v0.3.27 notice.

Retiring RECOG.R-A1 records that the cross-owner dependency is settled. It is not an unconditional physical validation. F30 and F14 stay open.

## 4. Publication (pending; the PI executes)

1. **Merge the PRs** into `main` with merge commits, not squash:
   - PR #186 (the receiving review record) first;
   - then PR #185.
2. **Create and push the annotated tag** on the PR #185 merge commit, after checking that the file hash at `main` is `443b5990…dbf7`.
3. **After the tag**, the Atlas owner:
   - verifies the tag (type, target, file hash at the tag and at `main`) in a tag-verification record;
   - closes the three `pipes/ATLAS/` items (state `closed`, disposition pointing here);
   - regenerates the inbox index (`tools/pipes_index.py`).

A merge, a tag or a passing check is not an adoption. The decision is the one in §3.

## 5. Carried forward

Each item belongs to its owner; nothing here is an obligation set by the Atlas.
- **TRIAD:** the consumer side of F30: repin the radial-polynomial import from gen-v2.8.7, and set the import grade of birth symmetry. Both GEN answers in `pipes/TRIAD/` are open.
- **GEN:** F14. No recovery of `GEN-ART-G2-CHRONO` or `GEN-ART-P4-PRIMITIVE`, and no independent ΔQ_d^(4) certificate. The bounded Methodology migration (GEN.D17) also stays with GEN.
- **DYAD:** whether to register c_J and c₇. RECOG's `RECOG-ALG-A1C-JET-REMAINDER-BOUNDS` is not a Dyadic registration.
- **TDR-G:** the one §7 export row (TDRG-EXPORT-DISCRETE-TRIAD) that still names the earlier D/A/B gate. It is recorded, not repaired.
- **Programme:** Pre-Legacy, DZT and AZ are not executed in the maintenance sequence (PROG.G6).
- **Next Atlas refresh:** the pipe items filed after `fa3db80` (the LIT acknowledgements in PR #182; the LIT → DYAD reply in PR #184) and any source tagged after the snapshot.
- **Outside Atlas custody:** the `BASELINE.md` RECOG row still says "tag to be created by the PI". That edit belongs to RECOG.
