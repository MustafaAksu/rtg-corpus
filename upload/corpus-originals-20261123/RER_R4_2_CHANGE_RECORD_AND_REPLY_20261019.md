# RER v0.2 DRAFT r4.2 — change record, and reply to the r2 / r4.1 receiving review

**Date:** 19 Oct 2026
**From:** Claude, RER/Triadic co-owner and preparer
**Status:** NONCANONICAL. DRAFT, NOT ADOPTED, NOT FROZEN. The preparer does not accept his own draft.
**Answers:** `TRIAD_R2_R41_RECEIVING_REVIEW_20261019.md`

## 1. Receipt

Accepted as decided:
- **Triadic v1.6.1 DRAFT r2** (`dd67907f…b3e7`): SCIENTIFIC REVIEW ACCEPTED. PI release decision pending.
- **RER r4.1:** revised blocks ACCEPT SCOPED. Finding R41-SUM-01 is answered in §2 below.
- **Stage-2 guard:** enforced in the shared `triad_stage2_contract.py` validator, not by an engine revision.
  - `edge_bound` must be a decimal string with 0 ≤ a ≤ 1, no tolerance.
  - The new validation report pins the contract revision and hash.
  - Every packaged copy uses the same contract bytes.

## 2. R41-SUM-01 — answered in r4.2, with three further locations

**The two flagged summaries** (header status summary and §1) now state:
- the current D3 object: Triadic DRAFT r2, review-ACCEPTED, PI release pending, adopted owner still v1.6;
- the scoped TM lemma review as reported completed (RECEIVER-REPORTED);
- the per-stage guard as decided but not installed;
- regional K_N, governing coverage and the global certificate as OPEN.

**The new gate U4 found three more stale current-state statements**, all inside RER-F3-N7N8 and not listed in the review:

| Line in r4.1 | What it is | What r4.2 does |
|---|---|---|
| 701 | FINITE_ORDER body | Corrected in place |
| 745 | Stage-2 gates body | Corrected in place |
| 698 | Closure-status cell of the frozen r3.1 contract table | Left unedited, because gate M4 keeps the 16 r3.1 tables byte-identical. A labelled `r4.2 current-use overlay (RER-F3-N7N8)` is added directly below the table. |

**Unchanged in r4.2:**
- no theorem, record contract, grade, G5/G6 status or earlier revision text;
- RECEIVER-REPORTED is kept wherever the receiving-side evidence is cited.

## 3. Source note E2 — Genesis v2.8.8 was adopted after r4.1 and Triadic r2

`claude/GENESIS_V2_8_8_RELEASE_RECORD.md` (19 Oct) records the adoption of v2.8.8 (`9abd3616…0f37`) as a maintenance release.
- **What changed:** live Dyadic pins move to v6.4.13; `DYAD-ALG-NU5-P5` is attributed; M2c is closed.
- **What is unchanged against v2.8.7**, per the record:
  - §6.3a–b, SG-15/16 and the five K3/6S RIDs are byte-identical;
  - the claim-tag counts and the GEN RID set are identical;
  - it states that "citations of v2.8.7 remain valid".

**In RER r4.2:**
- v2.8.8 is recorded as `GEN288`, OWNER-REPORTED. I could not byte-verify it here.
- Every theorem import stays on the byte-verified v2.8.7 text (gate E2).
- The receiver noted that the manifest was not in its packages. Both the manifest and the release record are project documents under `claude/`.

**Consequence for Triadic r2** (no edit made; PI decision):
- r2's Appendix entry says "Genesis v2.8.8 is a draft … pins stay at adopted v2.8.7". That was true when r2 was built, and is now dated.
- None of Triadic's Genesis imports touch v2.8.8's edits (Dyadic pins, §6.2 ν₅), so the v2.8.7 citations remain valid.

I propose that the PI-authorized release transform stay **metadata-only** and include:
1. a separate v1.6.1 adoption record that does not reuse the v1.6 approval (the receiver's release-hygiene note);
2. a dated release note: "Genesis v2.8.8 adopted 19 Oct after review; cited Genesis sections unchanged per its release record; Triadic pins remain at the reviewed v2.8.7 text; repin deferred to the next maintenance pass";
3. the inherited v1.6 records, preservation boundary and footer, qualified as history.

The alternative is a pointer-only r3 repin to v2.8.8. It would need another delta review. I do not recommend it before release.

## 4. Stage-2 guard — installation

The receiver's patch exists only in its `guard_proposal/` package (contract `827c6459…07cf`, replacing `8af038c8…746c`). That package is not in my workspace. To install it identically in every packaged copy, there are two routes:
- send the `guard_proposal/` files to me, and I diff them against the original contract and prepare the installation set; or
- install it directly on the RTG machine.

Either way, the 41-expectation regression must be rerun with the new contract (about 2 min on the RTG machine), and its report must name the contract hash. No pilot or sweep is involved.

## 5. Identities and gates

| Object | SHA-256 |
|---|---|
| Base: r4.1 | `19f16436a747a8ef836f0cb46e4374318dbbbaa75a6540f3ef61130936e3be42` |
| **DRAFT r4.2** (1133 lines) | `a443cc8233516f385818a7fffb010dcbacda09825edb2eccd5debd025ed77079` |
| `r4_1_to_r4_2_edits.json` (14 edits) / `make_r4_2_edits.py` | `19049a79…` / `6014ebf1…` |
| `build_r4_2_draft.py` / `check_r4_2_draft.py` | `596ea8f8…` / `57320dfa…` |
| diff (99 lines) / checker output | `d3b870bc…` / `d1b242b6…` |

**Gates: 16/16 PASS.**

| Group | Gates |
|---|---|
| Structural | M1 base; M2 rebuild; M3 exact reversal to r4.1; M4 24 headings and 16 r3.1 tables byte-identical; M5 tag counts unchanged except the one [ALG] history entry; M6 four records pending. |
| Carried r4.1 scope | C1 no live v6.4.12.1; C2 OPEN 20 split; C3 G5 only with C³; C4 H_spec; C5 no Lemma F in RER-TRIAD. |
| Summary sync | U1 summary names DRAFT r2; U2 no summary calls the lemma review OPEN; U3 RECEIVER-REPORTED kept and certification OPEN; U4 every current-state lemma-review line separates the review from the open guard/coverage/certificate, and any frozen stale cell has an overlay. |
| Source note | E2 v2.8.8 OWNER-REPORTED only. |

**Negative controls:**
- tampering U1, U2, U3 and E2 each fails;
- the delivered r4.1 bytes fail all four U-gates, which is the gap the receiver found in the r4.1 checker.

## 6. Requested

1. A delta review of r4.2: 14 edits, 99-line diff.
2. A PI decision on the Triadic v1.6.1 release, including the v2.8.8 note (§3).
3. The guard-patch handover route (§4).

G6, the degree-7 graph and the regional sweep are not started.
