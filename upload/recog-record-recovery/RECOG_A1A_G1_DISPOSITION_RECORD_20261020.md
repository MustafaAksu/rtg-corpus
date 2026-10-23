# RECOG — disposition of release gate A1a-G1 (NUMGEN `RID unavailable` governance)

**Date:** 20 October 2026 · **Recorded by:** RECOG owner (Claude, co-owner; PI Mustafa)
**Status:** `[SESSION]` governance record. This record registers no RID, adopts nothing, and edits no owner file.

## 1. Evidence chain

| Step | Record | Identity |
|---|---|---|
| Request | `RECOG_TO_NUMGEN_A1A_RID_REQUEST_20261020.md` | `a89b69243f24d63f74fed29c9af809f8616017ecdbbd8ef07446ed646e0246a0` |
| NUMGEN reply (draft; option 1) | `NUMGEN_REPLY_TO_RECOG_A1A_RID_REQUEST_20261020_v0_1.md` | `184a74fcede666c9427d0f959ed94b15c4206435b371b7d69b438a7254265227` |
| RECOG receipt | `RECOG_A1A_G1_RECEIPT_OF_NUMGEN_REPLY_20261020.md` | `87a0d9ce72f717be4a1cd256a12ff98b399578047d1d6da7b81fd447ac40722b` |
| NUMGEN co-owner ruling | given by the PI in the RECOG conversation, 20 Oct 2026, 19:03 local time (text in §2) | conversation record; no file hash |
| Final NUMGEN reply copy | the same body with an updated header (approval date and status), to be dispatched by the PI | **not yet received**; its hash is to be added when it arrives |

## 2. The ruling (PI as NUMGEN co-owner, summarized)

- **All six proposed strings are approved as allocations:**
  - `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`
  - `NUMGEN-DEF-N5AS1-DEFECT`
  - `NUMGEN-RESULT-N5AS1-L-BACKBONE`
  - `NUMGEN-RESULT-N5AS1-L-MONO`
  - `NUMGEN-RESULT-N5AS1-L-PHASE`
  - `NUMGEN-RESULT-N5AS1-INF1`
- **Scope of the approval:** it is an identifier allocation, not a regrade. Statements, proofs, domains and `[RESULT] [from: ALG]` grades are unchanged. The lift gets an explicit `[DEF]` block.
- **Two constraints:**
  1. `NUMGEN-OPEN-N5AS1-INF` stays the closed module's RID, and `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` stays with its own theorem.
  2. The six strings become canonical owner RIDs only when NUMGEN v1.20.8 is adopted. Until then they are approved allocation decisions, and **RECOG must not use them as if they already exist in an owner record.**
- **A1a-G1:** the interim governance line proposed in the reply is appropriate. The gate is **not** to be read as "citation complete". The allocation decision is resolved; the canonical source repin depends on v1.20.8 adoption.
- **Other items:** NUMGEN v1.20.8 DRAFT r1 is GO, with its scope limited as stated. The Dyadic $C_*=403/250$ certificate is not imported into NUMGEN as an owner result.

## 3. Disposition

**A1a-G1: allocation resolved; canonical repin pending NUMGEN v1.20.8.**

- **What closes:** the release-blocking governance question, namely whether the `RID unavailable` exception has a recorded owner disposition. It now has one: option 1, with the strings ruled by the co-owner, and NUMGEN as responsible owner.
- **What stays open:** the repin of RECOG's two imports (`A1A-NG-D-DEF`, `A1A-NG-INF1`) to canonical NUMGEN RIDs. This is a follow-up item for the first RECOG revision after NUMGEN v1.20.8 is adopted. It does not block a v0.3.22 release.
- **RECOG text:** the imports keep `RID unavailable` with the interim line. No approved string is written into a RECOG `[RID: …]` field before v1.20.8. The approved strings appear only in this record.
- **Missing evidence:** the final dispatched NUMGEN reply copy and its hash are not yet received. When it arrives, it is appended to §1 and to the release record. It does not change the disposition above, which rests on the co-owner ruling.
