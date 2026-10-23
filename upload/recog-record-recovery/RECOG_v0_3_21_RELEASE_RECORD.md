# RECOG v0.3.21 — Release Record

**Date:** 20 October 2026
**Status:** `[SESSION]` release record (governance). Not a scientific review and not an owner theorem.
**Edition adopted:** `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21.md`, SHA-256 `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3` (1,493 lines, 301,292 bytes)
**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_20.md` (frozen 19 Oct 2026), SHA-256 `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df`. v0.3.20 stays frozen and unchanged.

## 1. Decision

The PI (Mustafa) authorized adoption of v0.3.21 on 20 October 2026, in the RECOG co-owner conversation. The authorization followed the independent receiving review of DRAFT r2, which found it ready for adoption. This record does not give a clock time.

The release is synchronization-only. No existing scientific RID, result grade or OPEN status changed. The OPEN statuses are those of v0.3.20: R1 and R3 PARTIAL; R4, R5 and R6 ACTIVE; R2 and R7–R11 CLOSED. Three artifact IDs are new: RECOG-ART-MEMO-R6-ADDENDUM, RECOG-ART-FREEZE-0320 and RECOG-ART-G2-AUDIT. v0.3.21 is the current authoritative edition. It is not frozen; a freeze is a separate decision.

## 2. Identity chain

| Step | Artifact | SHA-256 |
|---|---|---|
| Base | `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_20.md` (frozen) | `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df` |
| DRAFT r1 | `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21_DRAFT_r1.md` | `a59436eec6049ecdb8da03ebe628edb9499afcad178279efd540c46948795980` |
| r1 builder | `build_recog_v0_3_21_draft.py` | `21b5e1e09f7d5ba1e97aea8edde0ce1b4904beb94586ee05f55ed5a54c8395f9` |
| r1 review | receiving review of 20 Oct 2026: accepted with corrections R1–R5 | (not hashed here) |
| DRAFT r2 | `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21_DRAFT_r2.md` | `be164a9f7dba3943e06d76e8a9448cb9b02d395f9ab18947498bdf3a8fef58c2` |
| r2 builder | `build_recog_v0_3_21_draft_r2.py` | `507a03ae7e9c5a7edcd00d986cf3685760934fe81b8ae53419595afc04111798` |
| r2 edit list (22 edits) | `recog_v0_3_21_edits_r2.json` | `2c071b53a58e2f3ff0b4d00c7fd986bf9f845627ef287f55ec8e646543d92125` |
| draft checker (unchanged since r1) | `check_recog_v0_3_21_draft.py` | `2f4459731d43e83911a22d614a843f6d66938424f18ca4d48033800a4db7d79e` |
| r2 checker transcript | `check_recog_v0_3_21_draft_r2_output.txt` | `89e1efbcd790c6544ce3335e501010864c911fbd75132045d4336b05a63306ad` |
| r2 review | `RECOG_v0_3_21_DRAFT_r2_RECEIVING_REVIEW_20261020.md`: accepted for adoption | `9a7ae8aa2f0f8db34436da48702ef84bc1927a870d22ef64d9c98f2048d31c45` |
| Adoption builder | `release_recog_v0_3_21.py` | `200c1e9fe6c7ebd3245fde4378956ac73bd0c4d3973e5b86a39ba5f3def37634` |
| Adoption edit list (7 edits) | `recog_v0_3_21_release_edits.json` | `dd0fdaca32ea0e718c198c19ef66757bb6750a71a9393e46730eacdd7edde0a3` |
| Adoption checker | `check_recog_v0_3_21_release.py` | `dff14b506cc0496c71f038da929d4cc4360a6846102333307dd0c2aff3670e0f` |
| Adoption checker transcript | `check_recog_v0_3_21_release_output.txt` | `dea0f32c62bd175e2af83480df762501b0823ebe6a92e2851355e180157950da` |
| **Adopted** | `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21.md` | `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3` |

The adopted hash is different from the DRAFT r2 hash, as the r2 review asked. The adoption pass starts from DRAFT r2 and refuses any other input bytes.

## 3. Adoption pass

The pass makes seven exact-once replacements, P1–P7. It changes only the edition markers:

- the title, date and supersedes line;
- the label of the v0.3.21 status summary;
- the freeze status;
- the Appendix A heading, plus one new adoption line under it;
- the footer.

`check_recog_v0_3_21_release.py --controls` passed all ten gates, P0–P9:

- P0: the input is the accepted DRAFT r2.
- P1–P3: building and reversing are byte-exact.
- P4: the grade-tag sequence is identical to r2.
- P5: the RID sequence is identical to r2.
- P6: the OPEN "Status:" lines are identical to r2.
- P7: no READ/WRITE/DECODE vocabulary was added.
- P8: the N13 row is unchanged and still conditional.
- P9: the edition-marker lines are in adopted form.

It caught all seven negative controls, RC1–RC7:

- an omitted release edit;
- a grade change in the body;
- a changed OPEN status;
- N13 reworded as acceptance;
- a renamed RID;
- a change to body text outside the markers;
- a draft marker left in the title.

Running the pass a second time produced a byte-identical file. The checker reverses only the adoption pass, recovering DRAFT r2 byte for byte. The draft checker separately reverses the r2 edits, recovering the frozen base. Together they cover the whole base → adopted chain.

## 4. Provenance qualifications carried forward

- **R6 addendum memo:** `RECOG_MEMO_TO_STREAMS_2026-09-30_R6_ADDENDUM.md` (`24a9fd85…c9f3`) was rehashed in the co-owner session. The receiving reviewer did not have the file, so it is not independently rehashed. This does not block adoption.
- **Dyadic source-fidelity record:**
  - `RECOG_G2_DYADIC_SOURCE_FIDELITY_RUN_v0_1.md` (`8cb01193…15ecb`) is the reviewed record.
  - `RECOG_G2_DYADIC_SOURCE_FIDELITY_RUN_v0_1_1.md` (`97a24f12…1d30`) adds the receiving disposition.
  - An interim state, hash `b8c151bd…aab2`, had appended that disposition to the v0.1 file itself. That state is withdrawn and not cited.
- **N13:** a conditional receipt only. Dyadic's release verification of v6.4.17 and any RECOG decision to use the N13 theorem are still pending.

## 5. Outbound obligations (G3, not yet sent)

Every notice cites the adopted file and its hash `a3459522…0ae3`, not a draft hash.

- **To RRF:** repin the RECOG v0.3.14 citations (§0.2, §4.1, §4.1a, §4.2, §4.3) to v0.3.21. Also RF-1: quote W3 verbatim, or label RRF's version an extension that carries an explicit map between the pre- and post-birth spaces as an additional obligation.
- **To OFN and RER:** the G1 freeze record and the adopted hash.
- **To Dyadic:** receipts N10–N13, with N13 conditional, and the §7.3 downstream-dependents register.

## 6. Unchanged authority statements

v0.3.21 introduces no new RECOG theorem, closes no OPEN, adopts nothing from any owner, and adds no token read-out vocabulary. Phase 1 science cells, starting with A1a, may now cite v0.3.21 as their base edition.
