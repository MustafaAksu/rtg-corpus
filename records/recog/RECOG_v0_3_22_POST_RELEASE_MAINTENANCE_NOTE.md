# RECOG v0.3.22 — post-release maintenance note (erratum record and active-edition pointer)

**Date:** 21 October 2026 · **Owner:** RECOG (PI Mustafa; Claude, co-owner)
**Status:** `[SESSION]` maintenance record. The adopted file is **not** edited by this note.

**Adopted edition:** `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22.md`, SHA-256 `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9`. Release record `RECOG_v0_3_22_RELEASE_RECORD.md`, `d9636a8d56e519e633d22f2e3705ebd29a0b84d3cf2abea50c8eb60361ba0820`.

**Trigger:** the post-release documentary review of 21 Oct 2026, disposition `ADOPTED — DOCUMENTARY REVIEW ACCEPTED; BYTE-LEVEL VERIFICATION PENDING`, notes 1–2.

## E-0322-1 — stale qualifier in the historical freeze text

- **Location:** the header line `**Freeze status:**`, in its *Earlier:* clause about v0.3.21.
- **Current text:** "v0.3.21 adopted 20 Oct 2026 (…); current authoritative edition, not frozen (a freeze is a separate decision)."
- **Problem:** the clause was carried verbatim from v0.3.21. In v0.3.22 the qualifier "current authoritative edition" is stale. The same line correctly opens with "v0.3.22 adopted 20 Oct 2026 … current authoritative edition".
- **Correct reading:** v0.3.21 is the *prior adopted edition* (historical). v0.3.22 is the current authoritative edition.
- **Disposition:** editorial erratum only. There is no scientific consequence and no change to any RID, grade or OPEN status. The phrase is to be corrected at the next RECOG revision, which is expected to be the NUMGEN v1.20.8 repin. Until then, this note governs the reading.

## E-0322-2 — active owner edition and project location

| Edition | Project path | Role |
|---|---|---|
| v0.3.22 | `claude/RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22.md` (project readback hash verified equal to the adopted hash) | **active owner edition** |
| v0.3.21 | `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21.md` (project root) | prior adopted edition; historical |

- **Different directories:** the two editions sit in different project directories. Directory placement carries no authority. The active edition is fixed by the adoption record and the hash above.
- **Consumers are not automatically switched:** a file being present in the project does not repin any consumer. Each consumer moves to v0.3.22 only by its own synchronization. The consumers are Dyadic, NUMGEN, OFN, RRF, RER and the Programme Overview's selected-edition entry.
- **Notices:** the v0.3.22 notices (`RECOG_v0_3_22_OUTBOUND_NOTICES.md`) carry the hash, so receivers can pin it. They are unsent.
- **Programme Overview:** updating the Programme Overview's RECOG entry is ordinary programme synchronization. It is outside RECOG custody and is not done here.

## Still open (unchanged)

- **Byte-level verification:** independent verification of `0dcce9e4…bcd9` and of the 12-edit release delta is pending. The artifacts are the release transform, edit list, checker and r3 package listed in the release record.
- **Notices:** Dyadic (N-D), NUMGEN (N-NG) and informational OFN/RRF/RER notices for v0.3.22, and the v0.3.21 G3 notices to OFN, RRF and RER. None has been sent. Only real dispatch events are to be recorded.
- **NUMGEN repin:** the canonical NUMGEN RID repin follows after NUMGEN v1.20.8 adoption.
- **OPEN status:** R6 ACTIVE.
