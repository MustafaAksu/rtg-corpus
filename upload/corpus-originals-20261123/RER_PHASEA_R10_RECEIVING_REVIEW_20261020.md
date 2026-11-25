# RER Phase A r10 — independent receiver review

Date: 20 October 2026. Status: RECEIVING REVIEW, NONCANONICAL. No adoption, freeze or publication.

## Source identity and replay
- Uploaded `RER_phaseA_r10.zip`: SHA-256 `bb27548fa05a90e0e7234de1228fcb9fc263654164bbaeea75d5417374de270f` — VERIFIED HERE.
- Extracted `SHA256SUMS.txt`: 70/70 entries match extracted files.
- Draft source `RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_2_DRAFT_r4_7.md`: SHA-256 `110729e54a2c960e93150a8d38fc75cbd6794c62ec00d2375dae80d20382cd1d` — checked in package.
- Fresh `python -I build_phaseA.py` then `python -I check_phaseA.py --tamper`: 24/24 positive gates PASS; 39/39 controls rejected as expected; entire check output byte-identical to packaged `check_phaseA_output.txt`.
- `python -I check_phaseA.py` without `--tamper` yields only the 24 positive gates and therefore, correctly, does not equal the packaged combined output.

## Phase A scope
- 90 matrix rows: 77 `RECORD_IMPORT`, 13 `GAP_REFERENCE`. A24 compares with pinned r9 outputs and enforces only RRF083 addition.
- Newly recognized RRF083 row for RER-DYAD-FORMAL-INVOLUTION: v0.8.3, `RECEIVER_BYTE_VERIFIED`, `OWNER_REPORTED` currency status. Receiver verification means the preparer did not hold the source bytes; it is not new owner proof certification.
- Registry source is r4.7, not r4.6. No grade, OPEN status, Dyadic v6.4.13 pin, physical selection or adoption changed. ER-2B blocks and G2 §5b source gap persist.

## Finding R10-F1: primary grade parser
- Exact observed value: `primary_grade` is the entire appended paragraph starting `[THM] (owner grade). Owner grades per imported RID (r4.7): ...`; `grade_tags=['ALG','THM']`.
- Those tags correctly enumerate grades appearing in the line, but do NOT mean the record's primary grade was changed to a compound `[ALG,THM]`. The record primary grade remains THM; the imported CENT-KERNEL RID is ALG and the analytic bridge is a distinct THM.
- Receiver choice: **(b)**, narrow r4.8 editorial fix placing the per-RID grade sentence on a separate line, while keeping scientific text and proof distinctions unchanged. This restores a machine-readable primary-grade field of `[THM] (owner grade)` under the current parser. It must preserve the per-RID grade sentence as a separately visible claim/source annotation and must not discard the ALG grade. Fresh Phase A on r4.8 will be needed; do not silently edit the r10 JSON.
- Until that version is reviewed, r10 is mechanically accepted with R10-F1 documented as a nonblocking schema/typing issue. The parsed grade_tags are a historical fact of r4.7, not a scientific grade promotion.

## Decision
**ACCEPT SCOPED — Phase A r10**, as a faithful mechanically verified extraction of the existing r4.7 DRAFT. **R10-F1 remains OPEN for prospective editorial fix**, not an obstacle to using the remaining correctly scoped Phase B scientific evidence. No owner/registry adoption, release, freeze, or whole-registry scientific acceptance.
