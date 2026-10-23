# Number Genesis → RECOG: reply to the A1a RID request (INF-1, D_M)

**Date:** 20 October 2026 · **From:** Number Genesis owner side (Claude, DSN editor/auditor). The PI keeps the final decision. · **To:** RECOG owner
**Status:** `[SESSION]` reply, **DRAFT pending the co-owner ruling on the RID strings (§3)**. It becomes final once the strings are ruled; the PI then dispatches it. No NUMGEN owner file is edited here.
**In reply to:** `RECOG_TO_NUMGEN_A1A_RID_REQUEST_20261020.md`, received through the PI (SHA-256 recorded in the dispatch log).
**Basis:** NUMGEN v1.20.7 (`c4637e7a…ab28`), §6.6 N-5A-S1-INF.

---

## 1. Decision: option 1 — dedicated RIDs will be assigned

NUMGEN takes option 1. The RIDs are assigned in the planned maintenance release **v1.20.8**, which the co-owner has already scoped. v1.20.8 changes no statements: INF-1, its proof, its domain and its grade stay exactly as in v1.20.7.

**Why option 1.**
- The co-owner has already authorized a dedicated RID for **L-BACKBONE** (OFN REQ-O09-03, 20 Oct 2026).
- The co-owner has already authorized an explicit **[DEF] of the primitive lift φ̂** (the I1 interface item with Dyadic, 20 Oct 2026).
- INF-1 and the D_M definition belong to the same chain. Assigning their RIDs together closes RECOG's exception without leaving a second governance item open.

## 2. Your two observations

- **Your reading is correct.** `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` is the consecutive-ratio theorem. It is not INF-1, and it must not be reused for INF-1.
- **The module RID is not an INF-1 RID.** v1.20.7 does carry `NUMGEN-OPEN-N5AS1-INF` (§6.6, module header "CLOSED at v1.11"). That is the lifecycle RID of the closed OPEN item, not a statement RID. Your entry "none in the inspected source" is therefore correct for the statement. Please do not repin to the module RID.

## 3. Proposed RID strings (subject to the co-owner ruling)

| Item | Proposed RID | Grade, unchanged from v1.20.7 |
|---|---|---|
| Primitive lift φ̂: the sum of the principal one-step angles under L-MONO | `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT` | `[DEF]` (new explicit block; v1.20.7 implicit) |
| D_M := 2πM − (φ̂_{6M} − φ̂_0) | `NUMGEN-DEF-N5AS1-DEFECT` | `[DEF]` |
| L-BACKBONE | `NUMGEN-RESULT-N5AS1-L-BACKBONE` | `[RESULT] [from: ALG]` |
| L-MONO | `NUMGEN-RESULT-N5AS1-L-MONO` | `[RESULT] [from: ALG]` |
| L-PHASE | `NUMGEN-RESULT-N5AS1-L-PHASE` | `[RESULT] [from: ALG]` (existential constant; v1.20.8 adds an `[OPEN]` sub-item for the Dyadic row-A certificate, with no C_* value) |
| INF-1: D_M = τ log M + C_D + o(1) | `NUMGEN-RESULT-N5AS1-INF1` | `[RESULT] [from: ALG]` |

The pattern follows the existing `NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION`, with the `N5AS1` module tag that `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` already uses. Under Methodology v1.3 a RID is a fixed identifier once assigned. The strings are therefore final only when v1.20.8 is adopted.

## 4. Timing and RECOG's gate A1a-G1

- The RIDs become owner identifiers when NUMGEN v1.20.8 is adopted.
- **If RECOG v0.3.22 is signed off before that date,** RECOG can record the following line and keep its tracking keys `A1A-NG-D-DEF` and `A1A-NG-INF1` until it repins:

  > "Owner RID: dedicated RID decided by the NUMGEN owner (reply of 20 Oct 2026); string to be fixed in NUMGEN v1.20.8; responsible owner NUMGEN."

  This is a recorded governance disposition (option 1, pending edition), not a deferral.
- No other NUMGEN change follows from this request, and NUMGEN takes no import from RECOG.

## 5. Unchanged

- INF-1 is independent of RECOG R9, and D_M is defined for any start (C4 reply, Q1/Q2).
- The INF-1 domain is NUMGEN's existential tube. An explicit-tube INF-1 would additionally need:
  - the Dyadic row-A certificate after Dyadic owner adoption;
  - an explicit L-BACKBONE constant (NUMGEN-side work, not started).

  Both are recorded as not yet available.
