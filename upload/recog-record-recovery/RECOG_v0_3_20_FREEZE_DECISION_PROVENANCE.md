# RECOG v0.3.20 — Freeze Decision Provenance

**Status:** `[SESSION]` governance record (G1 of `RECOG_STUDY_PLAN_2026-10-19_r1`). It documents an existing decision. It is not a new scientific review and not a new adoption decision. No DSN text is changed.

| Field | Value |
|---|---|
| Edition | `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20` |
| SHA-256 | `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df` |
| Decision date | 19 October 2026 (exact clock time not recorded) |
| Decision source | RTG Dyadic project, RECOG co-owner conversation |
| PI decision | Explicit confirmation that the corrected edition (after the one-line §7.1 correction) is the frozen canonical v0.3.20 |
| Co-owner verification | Uploaded-file hash independently recomputed and matched in the same conversation; frozen canonical status confirmed. Re-hashed again on 19 Oct 2026 (local copy, 285,585 bytes, 1,430 lines): match. |
| Predecessor candidate | `8b00cd38…9c8d` — never frozen |
| Previous frozen edition | RECOG v0.3.19 (`2b006b9f…2b36`) |
| External release record | Not previously issued. This record documents the existing decision. |

## Evidence qualification

- **The decision and the hash check are separate acts.** The decision was stated in the co-owner conversation and confirmed by the PI. The file identity was verified by recomputing the hash in that same conversation.
- **Not everything here is traceable within this session.**
  - The verbatim exchange lies before the retained context of the current session.
  - It is consistent with the session record that the stale §7.1 "current is" line was corrected earlier in the same conversation.
  - The predecessor hash `8b00cd38…9c8d` is taken from the PI's provenance statement and was not re-verified here.
- **The DSN header still reads "freeze candidate".** That is by design: the header defers the final hash to an external record, and this is that record.

## Consumers that may now cite v0.3.20 as frozen

| Consumer | Citation |
|---|---|
| OFN v0.10 | IMP-O09-01/02/03, RF-O09-01/02. Fulfils REQ-O09-02. |
| RER v0.2 r4.6 | G9: RECOG §6.6a and §6.16g. |
| Dyadic v6.4.15–17 | §7 source row; T1, T2, the memory law and OPEN 21 are conditional on RECOG-THM-R9-MEMORY. |
| RRF v0.8.3 | §4.1a should repin from v0.3.14 (content unchanged); the §6.6a, §6.16b and §6.16g citations stand. |
