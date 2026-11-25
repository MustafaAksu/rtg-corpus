# RER Phase A r4: change record

**Date:** 19 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate, revision 4. Nothing is adopted, frozen or published.
**Answers:** `RER_R46_PHASEA_R3_RECEIVING_REVIEW_20261019.md`, findings A3-CUR-01 and A3-STATUS-02.

## 1. Base

- **RER draft:** the same r4.6 bytes as in Phase A r3 (`2fa878ff…4772`). No Markdown changes.
- **Changed:** the source catalog and the gap-row status fields only.

## 2. A3-CUR-01: Dyadic currency

- **Current Dyadic** is now v6.4.16 (`33c14c5c…59e0`), with evidence `HASH_VERIFIED_BY_RECEIVER`. v6.4.15 (`be270dde…947c4`) is recorded as superseded.
- **Watch item, per the receiver's review:** OPEN 3 is closed within its defined scope, OPEN 3c is closed as a historical-fit discrepancy, OPEN 21 is new, and OPEN 20 is not closed.
- **Receiver section check:** §§6.15–6.17 are byte-identical from v6.4.13 through v6.4.16 (receiver-reported). The DYAD6413 rows record this in `receiver_section_check`.
- **RER pins** stay on v6.4.13.
- **New gate A19.** `owner_current` must equal a pinned list of the latest adopted versions (`inputs/owner_versions_known.json`: Dyadic 6.4.16, Genesis 2.8.9, Triadic 1.6.1, RRF 0.8.3, OFN 0.9, RECOG 0.3.20). Every row's current version must equal its owner's current version.
- **Regression control:** claiming Dyadic v6.4.15 as current fails A19.

## 3. A3-STATUS-02: two separate status fields on the 13 gap rows

The single field `phaseC_disposition: PENDING_RRF_EDITOR` is replaced by two:

| Field | Value | Meaning |
|---|---|---|
| `interface_questions` | `EDITOR_DISPOSITION_RECEIVED` (`413a869b…3084`; Q1–Q8 implemented in r4.6) | The editor has answered Q1–Q8. |
| `gap_reference_review` | `PENDING_PER_REFERENCE_AUDIT` | The editor answered on packet excerpts only. Each reference line still needs its own source and currency check against RRF v0.8.3. |

**Proposed route:** the receiving co-owner does the per-reference audit. The RRF editor is consulted again only if a reference turns out to be CHANGED-SCOPE beyond Q1–Q8. No second Q1–Q8 consultation is needed.

**Gates:**
- A15 now requires both fields and rejects the old field.
- Control: putting `PENDING_RRF_EDITOR` back fails A15.
- The editor response is pinned by hash (A20).

## 4. Gates

- 20/20 PASS.
- 16/16 negative controls fail as required: the 14 carried controls, plus A19 (v6.4.15 claimed current) and A15 (old status field restored).
- Counts are unchanged from r3: 89 rows; VERIFIED 23, OWNER_REPORTED 8, HISTORICAL 51, BLOCKED 7.

## 5. Phase B

This revision changes no record. Phase B can start on the receiver's routes:
- 13 records: deep review;
- 5 records: claim level, including the two author-conflict records, which the receiver dispositions;
- 2 records: blocked.

Genesis v2.8.9 §6.3c (relevance to GEN-K3-MODAL and G6) is a Phase B item.
