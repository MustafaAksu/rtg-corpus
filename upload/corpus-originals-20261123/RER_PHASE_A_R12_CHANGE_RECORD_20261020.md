# RER Phase A r12: change record (owner-currency catalog update)

**Date:** 20 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate, revision 12. Nothing is adopted, frozen or published.
**Answers:** the receiving decision of 20 Oct 2026 ("Phase A r12 ve RER r4.9 ayrı yürütülmeli"), part 1. That decision authorized a catalog update to Dyadic v6.4.18 and RECOG v0.3.21 at `OWNER_REPORTED`, with five conditions, which are listed in §5.

## 1. Base

- **Source Markdown:** unchanged, RER r4.8 (`2dfebebf…0e3e`).
- **Base package:** Phase A r11 (`eb3ba748…0bc7`, accepted), extracted fresh.
- **Patch:** `patch_r12.py`, included at the package root.
- **r11 history:** the five r11 outputs and the r11 checker output are kept byte-unchanged under `inputs/phaseA_r11_outputs/` and pinned in `PINS.json`.

## 2. Evidence basis

The two releases are taken from the owner release records in the project:
- `claude/RTG_DYADIC_v6_4_18_RELEASE_RECORD.md`;
- `claude/RECOG_v0_3_21_RELEASE_RECORD.md`.

I read both records. Their hashes are the ones stated there; I did not compute any hash for v6.4.18 or v0.3.21, because their bytes are not held here. Nothing in r12 is an independent source verification.

## 3. Catalog changes

| Owner | Current (r12) | Evidence | Superseded, kept | History kept |
|---|---|---|---|---|
| Dyadic | v6.4.18 `f70308f1…458d` | OWNER_REPORTED; release verification pending | v6.4.17 `e07cf2b9…4bfc`, BYTE_VERIFIED. The file, custody r9 and section check stay in the package. | `phaseA_r8` (OWNER_REPORTED), `phaseA_r9_r11` (BYTE_VERIFIED) |
| RECOG | v0.3.21 `a3459522…0ae3` | OWNER_REPORTED; synchronization-only release per its record | v0.3.20 `fdb8c9a7…bdf`, BYTE_VERIFIED (file in `sources_available`). Its frozen status is recorded as `FROZEN 19 Oct 2026 — OWNER_REPORTED`, because the v0.3.21 release record states it. | `phaseA_r6_r11` (BYTE_VERIFIED) |

**Key rules:**

| Key | r11 rule | r12 rule | Why |
|---|---|---|---|
| `RECOG` | CURRENT | UNCHANGED_OWNER_REPORTED | The cited version is now superseded; the release record reports no scientific change. |
| `DYAD6413` | UNCHANGED_OWNER_REPORTED | RECHECK_IN_PHASE_B, plus `sync_warning` | The cited §2 OPEN 20 changed at the owner. |

## 4. Scientific synchronization warning SYNC-DYAD-OPEN20-BINF

The warning is carried in the matrix JSON and in a new section of the matrix Markdown:
- **Record and key:** RER-DYAD-FORMAL-INVOLUTION, `DYAD6413`.
- **Owner change (OWNER_REPORTED, v6.4.18):** OPEN 20 B-∞ existence is CLOSED by `DYAD-THM-SMOOTH-EMBEDDING` `[THM]` at C^∞ germ scope. The F1–F3 existence condition is discharged for K_m, J and R. B-an and B-6 stay OPEN, and no analytic convergence is claimed.
- **RER lines, quoted verbatim from r4.8:**
  1. `[OPEN] OPEN 20 B-∞ existence: …` — contradicts the reported owner status.
  2. The §6.17 import line (F1–F3 conditional on existence; "No existence is asserted") — its scope needs re-checking against v6.4.18 §6.17.
- **Status:** the builder recomputes it from the source. It is `OPEN — record correction required` while both lines are present.
- **Closes only when:** the lines are corrected in an RER revision and that revision is receiver-accepted. A catalog change alone does not close it.
- **Required action:** read v6.4.18 §2 OPEN 20, §6.17 and the new theorem from the original bytes, then prepare a narrow RER r4.9 for receiving review. B-an, B-6 and physical exchange are unchanged, and nothing transfers to the Triadic records.

## 5. Result and conditions

**Matrix.** 90 rows. Exactly three rows change, all in currency fields only:

| Row | Status change |
|---|---|
| RER-DYAD-FORMAL-INVOLUTION / DYAD6413 | OWNER_REPORTED → HISTORICAL (currency RECHECK_IN_PHASE_B; verified hash removed; `sync_warning` added) |
| RER-G9 / RECOG n0 | VERIFIED → OWNER_REPORTED (currency UNCHANGED_OWNER_REPORTED; verified hash removed; bytes still BYTE_VERIFIED_MATCH) |
| RER-G9 / RECOG n1 | VERIFIED → OWNER_REPORTED (same as n0) |

**Counts:**

| Measure | r11 | r12 |
|---|---|---|
| VERIFIED / OWNER_REPORTED / HISTORICAL / BLOCKED | 30 / 5 / 49 / 6 | 28 / 6 / 50 / 6 |
| Authentication | 58 / 7 / 24 / 1 | unchanged |

The registry and the blocked register change only in `schema`.

**The receiver's conditions:**

| Condition | Result |
|---|---|
| RER r4.8 and the 20 records unchanged | Source hash unchanged; the registry differs from r11 only in `schema`. |
| v6.4.17 identity kept; v6.4.18 verified hash empty | Kept as superseded with its file; `verified_current_hash` is None on Dyadic rows (A23). |
| v0.3.20 bytes and identity kept; frozen status OWNER_REPORTED only if the release record states it | It does, so it is recorded as such (A26). |
| Changes to the current-version inventory tested by negative controls | Yes (§6). |
| A visible sync warning for the B-∞ line that Phase A cannot close | A27. |

## 6. Gates: 27/27 PASS; negative controls 57/57 fail as required

| Gate | Requires |
|---|---|
| A19 | also rejects Dyadic v6.4.17 as current; RECOG must be v0.3.21 |
| A23 (re-based) | Dyadic v6.4.18 OWNER_REPORTED with no held file; v6.4.17 BYTE_VERIFIED as superseded, with its file, custody and section check still required; r8 and r9–r11 history; Dyadic rows with no verified hash, currency RECHECK_IN_PHASE_B and the sync link; DYAD6413 pin at v6.4.13 |
| A24, A25 | identity comparisons with r9 and r10, unchanged except that they exclude the owner-currency fields of Dyadic and RECOG rows; A23 and A26 check those fields exactly |
| A26 (new) | the RECOG currency inventory |
| A27 (new) | the sync warning is present and tied to the source; it is OPEN while the lines are present and is never CLOSED by Phase A |

**Controls.** Thirteen output controls are new or re-targeted:
- v6.4.18 promoted without bytes;
- v6.4.18 hash replaced;
- v6.4.18 hash entered as verified;
- DYAD6413 left as UNCHANGED_OWNER_REPORTED;
- r9–r11 history dropped;
- v6.4.17 claimed current;
- v0.3.20 claimed current;
- RECOG v0.3.21 promoted without bytes;
- a RECOG row left CURRENT/VERIFIED;
- a RECOG row given a verified hash;
- the frozen statement dropped;
- the v0.3.20 identity dropped;
- the warning removed, closed, detached from the source or unlinked from its row (four controls).

**File-level control.** Withholding the v6.4.17 file still fails A23.

**Clean extraction.** The package was re-extracted into an empty directory and run with `python -I`: output byte-identical to the stored checker output.

## 7. Not changed

- RER text, grades, OPEN statuses and pins.
- ER-2B stays blocked; G2 §5b stays pending; the 13 gap references stay `PENDING_PER_REFERENCE_AUDIT`.
- RER r4.9 is not started. It needs the original v6.4.18 bytes and the source reading first. The author-conflicted Phase B reviews are with the receiver.
