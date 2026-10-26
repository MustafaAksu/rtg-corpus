# NUMGEN v1.20.8 DRAFT r3 — delta note for the co-owner

**Date:** 21 October 2026 · **From:** Number Genesis owner side (Claude, DSN editor/auditor; the PI keeps the final decision) · **To:** NUMGEN co-owner
**Status:** `[SESSION]` delta note. Nothing is adopted. v1.20.7 (`c4637e7a…ab28`) remains canonical.

## 1. Why r3

Three owner editions were adopted after your r2 acceptance:
- Dyadic v6.4.19 (`40c9e63f…6ec9`), which includes `DYAD-THM-LPHASE-ROWA-REMAINDER` and notice N15;
- RECOG v0.3.22 (`0dcce9e4…bcd9`);
- RRF v0.8.4 (`2fb0a0fe…afce`).

As a result, three statements in r2 became stale: the L-PHASE sub-item text "owner adoption pending", the RECOG v0.3.21 row and the RRF v0.8.3 row. The PI chose a narrow fact sync. C_* is not imported.

## 2. Identities

| Object | SHA-256 |
|---|---|
| Base v1.20.7 | `c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28` |
| Accepted r2 (stripped of its banner) | `423cd7198c75ab7f39d3e1608c5e3bb85c0230dee795d13e03915dc0d4857b78` |
| **r3** | **`9d59cfa1edf15c4e263494c9fbc615dc915ed3b84e556df8ade61fd1fa7de7b3`** |
| Review package `NUMGEN_v1_20_8_DRAFT_r3_REVIEW.zip` | `a7fc9ed63113e7f6f48296b9593b92467b94314d71f5117e106cf9dcdbe1ee84` |

The project copies of the three upstream editions were each hashed, and each matches its owner release record. The Dyadic v6.4.18 text was taken from the project and hashes to `f70308f1…e58d`, the predecessor that v6.4.19 pins.

## 3. Delta (r2 → r3; 27 changed lines)

Only edits E01–E05, E16 and E27–E30 change. All others are byte-identical to r2, and G12 checks this.

| Edit | Change |
|---|---|
| E01–E03 | Edition markers: r3, dated 21 Oct. |
| E04 | Companion line: v6.4.19 is recorded as the current Dyadic edition. **The pins stay at v6.4.18.** A section-level diff shows that §§2–3, §6.1, §6.4, §6.11 and the PRIM-CTR / NF-INV / NF6 passages are byte-identical. The only §6.14 change is the inserted L-PHASE block. Consumer references move to RECOG v0.3.22 and RRF v0.8.4. |
| E05 | Status summary: the Dyadic theorem is adopted, the import is deferred, and no constant is entered. |
| E16 | L-PHASE sub-item, still `[OPEN] [target: THM]`. The title changes to "Dyadic row-A theorem adopted upstream; NUMGEN import deferred". The text names the RID and v6.4.19 §6.14, links the theorem to I1–I5 and the receipt replay, and states that C stays existential in this edition. |
| E27 | New N15 receipt row: RECEIVED; import deferred to a NUMGEN edition after v1.20.8; no constant entered. |
| E28 | RECOG row → v0.3.22. Its imports of INF-1 and D_M quote v1.20.7 §6.6 verbatim, with `RID unavailable`; the repin is RECOG's. |
| E29 | RRF row → v0.8.4. Its NUMGEN citations (§6.6 M2-1/Census-1, §6.4 N-3A, §6.8 NG-7A) are correct. |
| E30 | Changelog items 1, 5 and 6, and a draft-history entry for r2 → r3. |

## 4. Checks

`check_v1_20_8_r3.py --neg` returns exit 0.
- **Gates G1–G13 all PASS.** G1–G11 are the r2 gates, unchanged. G12 confines the delta: outside the declared edits the edit list is identical to r2, the anchors are the same, every changed line lies inside a declared span, and the r2 hash is pinned. G13 checks the fact-sync content and that no import pin names v6.4.19.
- **Negative controls N1–N10 all FAIL, as required.** N8 changes an undeclared edit, N9 restores the stale sub-item, and N10 removes the N15 row. I confirmed that every control actually alters the text.
- **Other runs:** INV-LIVE reports 0 live hits. `build_v1_20_8_r2.py` still reproduces r2 byte-exactly. The receipt replay still passes, with the JSON unchanged at `8697c697…a4fa`. The package was verified again in a clean folder.

The tag census is unchanged from r2, and G6 still holds: neither "403/250" nor "1.612" appears.

## 5. Requested

- A short delta review of r3.
- Then the PI adoption decision. The release pass will change metadata only. It will record the final SHA, the v1.20.7 SHA and the r3 SHA separately, as you set for r2.
