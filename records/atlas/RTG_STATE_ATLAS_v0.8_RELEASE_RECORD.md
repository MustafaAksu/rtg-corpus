# RTG State Atlas v0.8 — acceptance record

**Status:** PI ACCEPTED, 30 October 2026. The merge of PR #119 and the annotated tag `atlas-v0.8` are pending (§4). `atlas-v0.7` remains the tagged Atlas until both exist and are verified.
**Object:** a derived, NONCANONICAL Atlas. Acceptance adopts no owner science.
**Recorded by:** Claude, Atlas owner, on branch `claude/atlas-v0.8`. Under CONVENTIONS §4 this record comes before the merge and the tag; the tag verification is added after them.

## 1. Accepted object

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` — candidate rev. 2, PR #119 commit `fe0d4b9385192aad2360cb85dc1da4c234d6d6f3`; the receiving readback read these bytes | `47320ca55f25955ff0d5e73be690465c7f9e6ebad9fa6bbc09692d4cf86371b7` (502,700 bytes, 1,540 lines) |
| `atlas/RTG_STATE_ATLAS.md` — candidate rev. 1, PR #119 commit `f656c2010b59b6505406b346d313d7006170c663`; the first receiving review read these bytes | `450d8e7127beef06d07f4b2315b23233085b5766ffd2cb4894418780bd198e46` (502,219 bytes) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.8/source_manifest.json` (unchanged rev. 1 → rev. 2) | `1e698a08bf47a3648caa27c29c4e1329b71a44c26dde0987ca158fe420c83c6e` |
| `evidence/atlas/v0.8/dispositions.json` (unchanged rev. 1 → rev. 2) | `cb04c326dddadeba522693b82618ca57deb68ad81567c44efd77f66177d12e6a` |
| `evidence/atlas/v0.8/edit_log.json` (rev. 2, 95 operations) | `debc21e6b5a9dc585799154030047e4aee49fbc7cfc885edc1da6112267d8307` |
| `evidence/atlas/build/refresh_v0_8.py` (rev. 2) | `944c94c34c26acafc98ef8e08310b90afd75cc9ed5ad0e9bc3c4c043fd790683` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |

**Rev. 1 → rev. 2:** two lines of the Atlas changed, H5 (AV08-R1) and the A1b node (AV08-N1). Packet §6 has the change table and the read-back. The publication bytes equal the accepted bytes: the Atlas carries no status line that publication would change.

## 2. Basis and limits

**Basis:**
- Method v0.2.
- `records/atlas/ATLAS_V0_8_REVIEW_PACKET.md` (rev. 2) and the verification files under `evidence/atlas/v0.8/`.
- Base `atlas-v0.7` (`8ebfbd10…9c6c`).
- Source snapshot `f8f3b5b172649c69236e327af1f12f93e2307b1d`.

**The two moved sources:**
- OFN v0.11: `ofn-v0.11`, tag object `2018dfd0…`, commit `886afc64…`, file `38a2f444…e9e4`. The tag verification record is in PR #118, still open.
- RECOG v0.3.26: `recog-v0.3.26`, tag object `1ad76914…`, commit `2c076a75…`, file `45e307f8…dd34`.

For both, the builder asserts the file hash at the tag and at the snapshot. The other 16 sources are byte-equal to their v0.7 inputs (16 EQUAL, 2 CHANGED, asserted).

**Limits.** The checks are structural, and no owner certificate was rerun. New RIDs were checked for presence in the tagged sources, not re-proved. The receiving reviewer did not rerun the builder, the checker or the 18+8 controls; those stay the producer's execution (receiving review §1, §5).

## 3. Decision

**Receiving review.** ChatGPT, Atlas co-owner, 30 October 2026, `records/atlas/ATLAS_V0_8_RECEIVING_REVIEW.md` (PR #121, branch `chatgpt/atlas-v0.8-review`, head `cfbf1905ad576e6ba8a655dfbb81f1e2d8826275`, file SHA-256 `d35053234ccffb3f0b2a4d56486f3d5b575c3cc166bd095c61748adaceb0a0a6`):
- **Round 1, on rev. 1** (commit `ea959e41`; PR #119 comment `6517704790`): REVISE, narrow.
  - AV08-R1 (required): the H5 NUMGEN consumer-acceptance scope.
  - AV08-N1 (recommended): the grid-value wording.
  - Packet questions Q1–Q5 accepted: class C, OFN11-C01/C02, the nine L5 retirements, OFN.O14, and the RECOG correction with the DRIFT/ENV nodes.
- **Round 2, on rev. 2** (§5, commit `cfbf1905`; PR #119 review `5709824879` on `fe0d4b9`): **ACCEPT SCOPED / READY FOR PI ACCEPTANCE**. AV08-R1 and AV08-N1 are CLOSED, and no open finding remains.

**PI acceptance:** **ACCEPTED** in the project conversation, 30 October 2026, 11:35 +03:00. Verbatim: "Atlasın mevcut halini kabul ediyorum" — "I accept the current state of the Atlas". The current state at that moment is rev. 2, `47320ca5…71b7`, the object the round-2 readback names. Acceptance adopts a NONCANONICAL derived map, not owner science. It changes no owner DSN, grade, source tag, Method edition, pipe state or consumer adoption.

## 4. Publication (pending; the PI executes)

1. **Merge PR #119** into `main` with a merge commit (not squash). PR #121 (the receiving review record) can be merged before or with it. PR #118 (OFN tag verification) and PR #113 (tool) are independent.
2. **Create and push the annotated tag** on the PR #119 merge commit:
   ```powershell
   git fetch origin
   git checkout main; git pull --ff-only
   git log -1 --format="%H %P"          # the PR #119 merge commit
   (Get-FileHash atlas/RTG_STATE_ATLAS.md -Algorithm SHA256).Hash   # must be 47320CA5…71B7
   git tag -a atlas-v0.8 -m "RTG State Atlas v0.8 — NONCANONICAL; PI accepted 30 October 2026; SHA-256 47320ca55f25955ff0d5e73be690465c7f9e6ebad9fa6bbc09692d4cf86371b7"
   git push origin atlas-v0.8
   ```
3. **After the tag**, the Atlas owner:
   - verifies the tag (type, target, file hash at the tag and at `main`) and adds the result to this record;
   - closes `pipes/ATLAS/20261029-RECOG-v0-3-26-adopted.md` (state `closed`, disposition pointing here);
   - regenerates the inbox index (`tools/pipes_index.py`).

A merge, a tag or a passing check is not an adoption; the decision is the one in §3.

## 5. Carried forward

Each item belongs to its owner; nothing here is an obligation set by the Atlas:
- **OFN next edition:** OFN.O14 (γ≡κ attribution wording), OFN.O9 (the IMP-O10-05 "for this draft" exception) and the OFN.O6 residue (orientation vocabulary, §7.3 joint selection).
- **FMS / ER-2B:** class-C wording (H1, F5, DYAD.X1).
- **Receiver dispositions** of the 24 open pipe items, including the two RECOG registration requests to DYAD and OFN's token-sum label finding to TDR-G.
- **RECOG:** repin to NUMGEN v1.21.
- **Tool:** PR #113 (`tools/check_compaction.py` `history_appendix` profile), on its own review track.
