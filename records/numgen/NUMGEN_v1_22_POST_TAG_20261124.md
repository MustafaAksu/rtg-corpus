# Number Genesis v1.22 — Post-tag publication and queue closeout

**Date:** 24 November 2026.
**Status:** [SESSION] publication verification and administrative closeout; not a new scientific release or adoption decision.
**Session:** ChatGPT NUMGEN co-owner, following the PI's adoption and server tag push.
**Governing edition:** `numgen-v1.22`. This dated addendum supplements the frozen `records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md` (§§1, 2, 5, 6, 9–10). The release record is retained byte-identically; its publication-pending wording describes the checkpoint at which it was frozen.

## 1. Publication identity and verification

| Object | Identity |
|---|---|
| Adopted round-2 candidate commit | `dafd8c7c274eb4a0ea25b9e7929fa90593ebf2ba` |
| Candidate SHA-256 | `fa28c0abe8bca5e9e7bb307e27ecb8f13c75399a7d804487a7a48b7a8b5c78b9` |
| Publication transform commit | `391d42f3a35a69a91147022ffe7becd802cd091e` |
| PR #374 merge | `64e99e61e03b16249fbda685ec4ca9a8f905a6ac` |
| PR #375 merge | `e89d84237dce37eb2b8fa1dd32820ff165257f80` |
| PR #377 merge and tagged target | `c5acda99de18598108e9b5e368ad15fa74f5488d` |
| Annotated tag object | `a81ae6d512e40a2f3e8de308e4035136d260613a` |
| Tagger timestamp (UTC) | 2026-11-24T16:13:26Z |
| Published DSN SHA-256 | `36b31755c1bd73f1d5f69117c63b1556afacc18c2505e1b865b7a3adf512d40b` |
| Published DSN Git blob | `0972ffd8af574cc436f639640b5a371a3fca8dfa` |
| Frozen release record Git blob | `630a11680b088c9129aa4437cea322677adf6f00` |

- PI server output: the exact tagged-target DSN passed the expected SHA-256 comparison before the annotated tag was created and pushed. The two remote tag refs match the object and peeled commit above.
- Connector readback: the GitHub tag object is annotated, points to the stated merge commit, and its message contains the full published hash. All three PRs are merged. The DSN blob on the later checked main commit `085e567be4c522f4b7e62044e2755e3af9d7a9b0` is identical to the tag blob. BASELINE at the tag records the published identity.
- Connector transform readback: reversing all five exact-once publication replacements in `evidence/numgen/v1.22/publication_transform.json` on the tagged UTF-8 text recovers the reviewed candidate text exactly. No scientific body change.
- Round-2 native C0–C10, NC1–NC15 and Atlas row-check evidence remain as recorded in the adopted release record; no scientific campaign, native builder/checker or native publication script was rerun in this post-tag session. The distinct Atlas-owner acceptance is not inferred from the recorded Atlas co-owner concurrence.

## 2. Receiver queue closeout

The eleven dispositions in the adopted receiving ledger `records/numgen/NUMGEN_v1_22_RECEIVING_LEDGER.md` (P01–P11) are closed in the proposed closeout branch now that the tag is verified. The disposition text, sender body, tags and source references are retained. Only the receiver-owned queue state changes. Queue closure is not additional scientific adoption.

| Key | Item under `pipes/NUMGEN/` | Verdict retained |
|---|---|---|
| P01 | `20261028-TDRG-v2-12-14-adopted.md` | accept with change |
| P02 | `20261029-RECOG-v0-3-26-adopted.md` | accept |
| P03 | `20261030-DYAD-v6-4-23-adopted.md` | accept |
| P04 | `20261030-OFN-v0-11-adopted.md` | accept |
| P05 | `20261030-OFN-v0-12-adopted.md` | accept |
| P06 | `20261104-PROG-v1-4-adopted.md` | accept |
| P07 | `20261104-RECOG-v0-3-27-adopted.md` | accept with change |
| P08 | `20261111-DYAD-v6-4-24-adopted.md` | no action |
| P09 | `20261112-TDRG-v2-12-15-adopted.md` | accept |
| P10 | `20261119-DZT-v0-18-adopted.md` | accept |
| P11 | `20261120-DZT-v0-19-adopted.md` | accept |

## 3. Outbound notices

The seven notices below implement release record §6, scoped to the adopted edition and actual companion pins. They are proposed in the same closeout PR, not yet a merged queue event. Each receiver owns its own disposition, pin and adopted-use decision.

| Receiver | Proposed item |
|---|---|
| TDRG | `pipes/TDRG/20261124-NUMGEN-v1-22-adopted.md` |
| GEN | `pipes/GEN/20261124-NUMGEN-v1-22-adopted.md` |
| RECOG | `pipes/RECOG/20261124-NUMGEN-v1-22-adopted.md` |
| DYAD | `pipes/DYAD/20261124-NUMGEN-v1-22-adopted.md` |
| OFN | `pipes/OFN/20261124-NUMGEN-v1-22-adopted.md` |
| DZT | `pipes/DZT/20261124-NUMGEN-v1-22-adopted.md` |
| PROG | `pipes/PROG/20261124-NUMGEN-v1-22-adopted.md` |

## 4. Mechanical scope and remaining gate

The eight affected inbox indexes were rebuilt connector-side from the item front matter using the ordering and row-rendering contract of `tools/pipes_index.py` (the DYAD original rows were verified in two batches). The corresponding pre-edit indexes matched; all seven named companion tags exist. Eleven NUMGEN items change state; seven notices are added; eight indexes change. At the fixed tag base the item census is 149; the proposed tree has 156. The NUMGEN inbox has twelve items, all closed after the proposed merge. The pre-existing closed RECOG item stays unchanged.

Native `python3 -I tools/pipes_index.py --check` is still a pre-merge check for the proposed PR; connector rendering is not a claimed native run. No adopted DSN, frozen release record, evidence file or existing tag is changed. The working entry note is refreshed separately. Review and PI-authorized merge of the closeout PR remain pending.

## 5. Scientific status unchanged

[OWNER: NUMGEN v1.22 §§2, 6.6, 9.1] P2 sensitivity is addressed for the bounded witness panel. Census-1 remains INCONCLUSIVE / INCONCLUSIVE, full-interface typed WD-DOM OPEN, M4 HOLD pending an approved design/preregistration, DISC-3 DEFER, and the phi-star comparison OPEN. This closeout neither approves a campaign nor refreshes Atlas.

*END OF RECORD.*
