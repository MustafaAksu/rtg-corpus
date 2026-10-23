# RECOG v0.3.22 DRAFT r3 — Independent delta receiving review

**Date:** 20 October 2026  
**Status:** `[SESSION] REVIEW ACCEPTED — READY FOR SEPARATE PI ADOPTION DECISION`  
**Scope:** r2→r3 exact delta, evidence and governance gate A1a-G1. This is a receiving review, not an adoption, owner RID registration, or new scientific certification.

## 1. Source manifest actually inspected

| Source | Identity / coverage |
|---|---|
| Adopted RECOG v0.3.21 | SHA-256 `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3` — ZIP copy inspected / base identity verified |
| DRAFT r2 (historical) | SHA-256 `8f7f6f861e419afa2e43c11e32b0d5e1647f37a81f63baafdc41a15905c1624e` — exact comparison |
| DRAFT r3 | SHA-256 `8f496d3c1fd0182e058e5fd814c5530e3952d5469b3ea932d3d3f27718fbd959` — entire file available; scope sections and diff read |
| DRAFT r3 package | SHA-256 `b8c4fc60d68b7b0d4f1037121b0294e581812fe62b8b81061fc369c012ea87ba` — complete archive/manifest validation |
| G1 disposition | SHA-256 `0e5f91c0dabbd34bb8261ddd6e0a34361be4dbaaa9b3545b0f98fc14e3e971a7` — read in full |
| G1 reply/receipt/request | SHA-256 `184a74fcede666c9427d0f959ed94b15c4206435b371b7d69b438a7254265227` / `87a0d9ce…40722b` / `a89b6924…246a0` — read in full from archive |
| Methodology | `DSN_METHODOLOGY_v1.3` §3.3 and §4.4, consulted directly |

**Evidence limitation:** the PI's original NUMGEN co-owner ruling (reported at 19:03 local, 20 October 2026) is represented by the G1 disposition record and the current user report, not an independently obtained verbatim conversation transcript. The final dispatched NUMGEN reply is absent, expressly disclosed and awaiting hash entry. The v6.4.18 E2 source check and r2 scientific review were previously accepted; this r3 delta review does not rerun Dyadic P5 or RECOG R9 Arb certificates.

## 2. Engineering / determinism audit

- ZIP payload count: **41**, plus `MANIFEST.json`; 41/41 manifest SHA-256 and byte sizes independently recomputed and matched. ZIP CRC test PASS. Manifest explicitly excludes itself.
- External uploaded draft and governance file are byte-identical to their corresponding ZIP payloads.
- Clean-directory `python -I build_recog_v0_3_22_draft_r3.py` on the adopted v0.3.21 file rebuilt the r3 Markdown and `recog_v0_3_22_edits_r3.json` byte-identically to the package.
- Clean-directory `python -I check_recog_v0_3_22_draft_r3.py BASE DRAFT EDITS --controls`: **14/14 gates PASS** (C0–C13) and **15/15 negative mutants caught**; output byte-identical to packaged checker output. Negative controls share the core exact-rebuild gate: they are fail-closed engineering probes, not 15 independent mathematical proofs.
- Historical r1/r2 checkers rerun against their matching archived drafts: both PASS.
- Independent r2→r3 line comparison: **14 lines added, 13 removed**, 12 replacement regions; no alteration to mathematical statements, grades, numeric rows, domains or proposed RECOG scientific RIDs.
- New RECOG RID-set difference from v0.3.21: **8 distinct scientific RID names and 4 distinct artifact RID names**, no clashes with existing RID names. Multiple mentions of the same RID in synopsis/definition are references, not assignments of a second distinct name.

## 3. Governance A1a-G1

**[SESSION] Verdict: `ALLOCATIONS RESOLVED; CANONICAL REPIN DEFERRED (NONBLOCKING)`** on the terms of the documented NUMGEN co-owner ruling.

1. NUMGEN source v1.20.7 §6.6 lacks dedicated statement IDs for `D_M` and INF-1; Methodology v1.3 §3.3 supports a declared temporary `RID unavailable` with exact source and governance tracking.
2. The NUMGEN owner-side draft response selects option 1 and proposes six identifiers, with no changed theorem, grade, radius or proof. Its own status remains *DRAFT*, so do not characterize that document alone as a final dispatched owner response.
3. The separate disposition records the PI/NUMGEN co-owner ruling approving the allocations and authorizing the interim `RID unavailable` line with NUMGEN responsible for eventual registration. This provides the governance closure described by the request and the receipt's alternate path, **subject to the primary-decision evidence limitation above**.
4. All six approved-but-not-yet-canonical NUMGEN strings occur in the G1 disposition, and **none occurs anywhere in the r3 DSN**. This was independently searched and is enforced by checker C13. They must not be repinned as canonical until adopted NUMGEN v1.20.8 exists and is inspected.
5. The two RECOG tracking keys `A1A-NG-D-DEF` and `A1A-NG-INF1` are retained. The final NUMGEN dispatched reply and its new hash must be appended when received; missing reply is a provenance follow-up, not itself the recorded basis of the G1 closure.

## 4. Scoped delta disposition

| r2→r3 change | Finding |
|---|---|
| Companion header / §6.13b / §7 NUMGEN rows | PASS. Allocation ruling versus pending canonical owner RID consistently separated; `RID unavailable` retained. |
| Status summary / Appendix A | PASS. Integrated r2 review is cited; release gate state names the resolved allocation and pending repin. |
| §7.2 N13 use column | PASS. `v0.3.22 draft` replaces revision-specific `DRAFT r1`; conditional import and adoption timing retained. |
| §8 governance evidence | PASS for document existence and hashes; note that the final owner response and verbatim PI ruling are external/not yet obtained. |
| r3 checker help and C13 | PASS. Current wording and premature-identifier rejection. |
| Scientific claims (a), (b), (b′), (c) | UNCHANGED relative to scientifically accepted r2. No independent new scientific promotion asserted by this delta review. |

## 5. Release recommendation and limitations

**Decision:** `DRAFT r3 INDEPENDENT DELTA REVIEW ACCEPTED — RELEASE CANDIDATE READY FOR EXPLICIT PI ADOPTION DECISION`.

The earlier scientific/integrated r2 acceptance is carried forward because its content is unchanged, not because 14/15 engineering tests recertify those results. A1a-G1's *allocation-governance* blocker is disposed in the stated limited sense; the downstream NUMGEN v1.20.8 canonical RID repin remains explicitly pending. No final NUMGEN reply is silently inferred. No owner DSN, RID, or release artifact is adopted or registered by this review.

For a subsequent **separate release pass**, the PI must explicitly adopt the identified candidate, and the release record should distinguish: draft hash, adoption authorization, publication-metadata delta and resulting release-file hash, the 8 scientific / 4 artifact RIDs registered on adoption, the G1 disposition's evidence class, and outstanding NUMGEN repin plus final reply receipt. Keep RECOG R6 ACTIVE and maintain unsent G3 notices as unsent. Only actual dispatch/receipt events may be recorded as such.
