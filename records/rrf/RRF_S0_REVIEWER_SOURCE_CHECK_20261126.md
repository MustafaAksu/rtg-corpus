# RRF S0 — independent reviewer source check

**Date:** 26 November 2026.
**Status:** [SESSION] / NONCANONICAL. Reviewer lane of the RRF maintenance pass (Claude, independent mathematical reviewer and second co-owner; ChatGPT prepares; the PI decides). Source custody only: no scientific review, owner disposition, placement, adoption, BASELINE edit, pipe closure or new RRF edition.
**Checkpoint:** `main` `43dabc5818b2dccba31030116e4ecd80570e7e35`. PR #395 read at head `73dd0cf88d3e89063f1eff1de911255c26313489` (two commits; `ff008c47` + B1/O1 correction).
**Lane separation:** this record is not the Atlas-owner readback of #395. That readback (of `7187371035`, B1/O1) belongs to the Atlas lane and is not given here.

## 1. Governing state (recomputed)

| Object | Result |
|---|---|
| `rrf-v0.8.4` | annotated tag `cb8f7caf6ac4…` → commit `d7d661c0b89c…`; blob `6882fd517e54…`; 108,615 bytes; SHA-256 `2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce` = `main` = BASELINE = v0.8.4 adoption record. No later RRF tag; RRF unchanged on `main` since the baseline commit `6a6a347`. |
| v0.8.4 adoption record | upload copy 3,198 bytes, `621ee53c…1611`. Scope: RRF working representation standard only. Authorization is stated as reviewer approval; no separate PI signature is asserted in it (v0.7's record says so explicitly). Kept as stated. |
| Methodology | `methodology-v1.4`, `cdacab5f…f2df` = `main`. RRF itself still declares v1.3. |
| Programme | `programme-v1.5`, `9c53159f…f611` = `main`. |
| `records/rrf/`, `evidence/rrf/` | absent at checkpoint (created by this branch only for this record and its scripts). No RRF co-owner orientation note exists yet. |
| RRF inbox | nine open items (`pipes/RRF/INDEX.md`), none with `blocks`; BR-Q2 (4 Nov, OFN) is the only question. PR #394 head `39c42a33` would add a tenth (Programme v1.5 notice); not merged. |

## 2. Method

`python -I evidence/rrf/scripts/rrf_s0_object_scan.py <repo> <out.json>` hashes every working-tree file and every archive member, nested zips to depth 4, reading bytes only: 13,013 objects, 9,234 of them archive members, 0 read errors. SHA-256 self-test (`abc`) passed. Located objects: `evidence/rrf/s0/rrf_s0_object_locations.csv`. Native extraction covers what the advisory (#395 §1) and the intake left to archive inspection.

## 3. Findings

**F1 — v0.8.2 record and G2 v0.3 final: read natively.** Both are members of `RTG_RRF_v0_8_2_ADOPTED_G2_v0_3_RELEASE_PACKAGE.zip` and nowhere else: record 4,089 bytes `17dd1293…13f1`; G2 v0.3 final 16,164 bytes `d3203739…c9c3`, the digest printed in the v0.8.2 and v0.8.3 records. The v0.8.2 record states "ADOPT — RRF v0.8.2 WORKING STANDARD ONLY", reviewer authorization subject to four provenance corrections, and no science adoption beyond DYAD v6.4.12.

**F2 — the two "missing" v0.8.4 publication diffs are recoverable byte-exactly.** No file with either digest exists anywhere in the repository, nested archives included. They are regenerated deterministically by `evidence/rrf/scripts/rrf_s0_regenerate_v084_diffs.py` (Python `difflib.unified_diff`, n=3, bare file names; output `evidence/rrf/s0/rrf_s0_regenerate_v084_diffs.txt`, exit 0):
- control: the same generator reproduces the archived Review diff A (36,647 bytes, `e4b666fa…3385`) byte-exactly;
- `RTG_RRF_v0_8_4_REVISED_CANDIDATE_to_ADOPTED.diff`: 7,893 bytes, `e8eb5193a71fc573f4003cad1052c6b0b2cbe15290c584b06ac0a14c973403ce`;
- `RTG_RRF_v0_8_3_ADOPTED_to_v0_8_4_ADOPTED.diff`: 37,612 bytes, `bcb8c9b5721ea4fbeb22f1be88d9578f193e1555f56ef8f7f7e414817321a967`;
- both equal digest and byte count in the v0.8.4 adoption record and in `RTG_RRF_v0_8_4_ADOPTION_QA.json`; a perturbed input fails (negative control).

The full SHA-256 match establishes the bytes (EV-HASH). Custody is regeneration on 26 Nov 2026, not the original files; any placement must say so. With F2 the six adoption records' digest chain is 37/37 (intake §2.4: 35/37). This corrects #395 §2 ("reconstruct a new comparison only as a new check, not recovered historical diff bytes").

**F3 — RER editor response: agrees with B1 as corrected.** One digest, `413a869b…3084`, 5,586 bytes: one loose copy (`build_r4_7_draft.py`, wrong stored name) and 31 archive members (my count; the Atlas review said "more than thirty").

**F4 — SH-R0 note: custody link stronger than title.** `87a67a90…87bf` is also a member of `RTG_RRF_v0_8_3_G2_v0_4_ADOPTED_RELEASE_PACKAGE.zip`, beside adopted v0.8.3 (`b393657e…`), its adoption record (`c2ef6489…`), G2 v0.4 final and the release diffs. The v0.8.3 record does not cite the note by digest. Release-package co-membership only; still a SESSION deduction, not owner-adopted proof.

**F5 — PRR Wrap-up v0.2 has a source-printed digest, and all six RRF locators agree with v0.2 by content.**
- Wrap-up v0.3 Appendix B, row S00, prints `88274f70449027d0a27231e950819e7b3d2c3432de4471451486288cffd9e2f2` for v0.2, which equals the recovered bytes. This corrects intake §3 row 6.1 ("no source prints a digest"). The printer is a noncanonical draft, so this is a digest cross-reference, not an adoption.
- Topic check against RRF v0.8.4: header `parent: … v0_2 §20, §26` (v0.2 §20 "Representation profiles and equation annotations", §26 "Recommended next work programme"); line 301 §11 comparator transport; line 131/469 §14.1 Ledger; line 344 "typed-covariance criterion (§10.2)", where v0.2 §10.2 contains the boxed $O(Sx)=\tau_O(O(x))$; line 53 "(Wrap-up §19)", cited for $\sum_e\epsilon_{\gamma e}h(z_e)=0$ rather than $\sum_e\epsilon_{\gamma e}z_e=0$, where v0.2 §19 contains $h(z_{AB})+h(z_{BC})+h(z_{CA})=0$. So O1 settles positively: the §19 citation is the cycle-constraint chart statement, not a "safety lock".
- v0.3 renumbers. Its §10.2 is "Typed covariance is an operational obligation, not a label" and its §19 is "Network representations: the provisional lock and the joint problem". v0.3 is therefore not a drop-in parent: if substituted, the RRF locators would point at different text. v0.3 (25 Sep) is a noncanonical sync draft on base v0.2, referencing RRF v0.6 as a non-adopted candidate. RRF v0.8.4 never adopted or cited it (lines 521, 550). Its one identified consumer is GIIL v0.19.

**F6 — GIIL identity: the mismatch is on the RER side.**
- RER v0.2 line 1124 cites GIIL v0.19 "as pinned by Genesis queue v0.4" with short form `f6320914…0be8`.
- The pin source itself, `upload/gen-records/GENESIS_V2_8_5_OWNER_PASS_QUEUE_v0_4.md` (`f5fa239c…344f`, also in two Genesis packages), prints the full `f6320914190b434332058b69fe0974ce584d1a8167ae40e2650091be5bdbe2f8` in §0. So does RER's own 17 Oct candidate record (`RER_v0_2_r4_TRIAD_RECORD_CANDIDATES_20261017.md`, line 46).
- That digest equals the uploaded GIIL v0.19 draft (198,306 bytes). No object anywhere has prefix `f6320914` and suffix `0be8`.

[INTERP] The "…0be8" suffix is most likely a transcription error in RER's short form. Correcting it is for the RER owners. RRF records only the identity evidence.

Dependency: GIIL v0.19 is a working draft on owner baseline GEN v2.8.4 and cites PRR v0.3 and RRF v0.6. GEN v2.10 does not reference it. It is therefore usable only as historical noncanonical proposal input, and its inheritance fields stay unregistered.

**F7 — still missing (unchanged).**
- `RTG_RRF_v0_8_ADOPTION_QA_MANIFEST.json`: absent; the v0.8 record prints no digest for it, so `RTG_RRF_v0_8_ADOPTION_QA.md` cannot be identified with it.
- `PRR_RRF_REVIEW_v1.zip`: absent, nested archives included.

These limit only claims that depend on them: the "23/23" QA identity, and the third-reviewer artifact identity in RRF §2.4a. They are source gaps, not scientific errors.

## 4. S0 acceptance criteria for the preparer's inventory/placement PR

1. **A1 Governing identity.** Tag, commit, blob, SHA-256 and byte count of v0.8.4 restated as in §1. The v0.8.4 record placed byte-identical under `records/rrf/` with its original name and upload provenance. BASELINE provenance is edited only by PI decision. The DSN and tag are untouched.
2. **A2 Historical records.** The six records are placed byte-identical (the v0.8.2 one as extracted, with package provenance), or listed with location if left in place. Each record's authorization is quoted as written. No PI approval is added where a record does not state one.
3. **A3 Digest chain.** 37/37, with F2's two diffs marked "regenerated, digest-verified" and their regeneration script cited. If the bytes are placed, they are labelled as regenerated, not as original files.
4. **A4 Misnamed files.** Every RRF-relevant §4.1 wrong pairing (at least `build_r4_7_draft.py` and the `v0_8_4_CANDIDATE` label) is mapped to its true identity by full digest. Placement uses the true name. Uploads stay unchanged.
5. **A5 PRR.** v0.2 is recorded as the cited historical NONCANONICAL parent, with F5's digest cross-reference and locator check. v0.3 gets its own row (noncanonical draft, not cited by RRF, not a drop-in parent, consumer GIIL). Its status is a PI decision.
6. **A6 GIIL.** Identity is recorded by full digest with F6's owner-side pin evidence. The RER short-form discrepancy is routed to RER as a finding (pipe item, not an edit), and the GEN v2.8.4 baseline dependency is stated.
7. **A7 Missing list.** A separate list, with no gap converted into an approval or a reconstruction: F7 items, plus any other missing item the preparer finds. Each entry names the claims it limits.
8. **A8 Byte custody check.** A script or command recomputes every placed file's SHA-256 against its upload/archive source, and the PR shows the output.

S0 is ACCEPTED when A1–A8 hold at an exact PR head. S1 and the scientific items (BR-Q2, OPEN-A, OPEN-B → E1 → E2) are not opened before then.

## 5. Verdict on the RRF-relevant content of #395 (reviewer lane)

ACCEPT SCOPED as source/readiness input, subject to these three updates. They go in the preparer's S0 inventory; #395 itself need not be re-edited unless the Atlas lane wants them.
- F2: the v0.8.4 diffs are recovered by digest.
- F5: the §19 topic is confirmed as the cycle constraint, and v0.3 renumbers.
- F6: the GIIL identity is resolved on the owner-pin side; the discrepancy is RER's.

Not checked here: the S1 owner-source rows and the S2 profile counts. These come in S1/S2.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
