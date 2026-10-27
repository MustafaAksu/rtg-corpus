# Number Genesis — Receipt replay of the DYAD L-PHASE row-A certificate

**Date:** 20 October 2026 · **From:** Number Genesis owner side (Claude, DSN editor/auditor; the PI keeps the final decision) · **To:** Dyadic DSN owner; PI
**Status:** `[SESSION]` receipt record. It is an addendum to `NUMGEN_INTERFACE_CONFIRMATION_LPHASE_ROWA_20261020_v0_1.md` (`7a91c223691b3705c2560fca452e671442939452e11cf98820512b182f46f78f`, co-owner GO). That file is unchanged. No owner file is modified and nothing is adopted.

**Purpose.** The interface confirmation (§3.1) asked for the helper files. Dyadic has placed them in the project (`claude/lphase_rowA/`). This record discharges that request.

## 1. Identity

Every file below was taken from the project, written into a clean folder, and hashed. Each hash matches `claude/lphase_rowA/SHA256SUMS.txt`.

| File | SHA-256 | Match |
|---|---|---|
| `dyad_numgen_lphase_rowA_cert.py` | `117484ae1a2509b6f6065d395840bfdfe2b0c977af0505f9fe6de68c13959cdb` | ✓ |
| `qw.py` | `3a913062c1cdc6d151a2fb5b2f76d5354a367d1fa55df43f1f31d06e1b94cce8` | ✓ |
| `tzw.py` | `f007d42cde36d2a70115b9db25f47b107c446735fa31c66664f620c3247a5609` | ✓ |

## 2. Replay

`python3 dyad_numgen_lphase_rowA_cert.py` was run in that folder.

- Exit code 0, `RESULT: PASS`, run time about 1.7 s.
- Positive gates G-H, G-L, G-D, P-c, P-L, P-a, P-b, P-7, S-T and FIN: 10/10 true.
- Negative controls N1–N6: all false, as required.
- The regenerated `lphase_rowA_certificate.json` has SHA-256 `8697c6970bd908327c66ef2ce3b2d38386947899033ef7f720bc096c4c3ad4fa`. This is **byte-identical** to the packaged JSON.

**Reproduced values:**

| Quantity | Value |
|---|---|
| Combined constant before bridge | 1.5163199720 |
| Bridge factor | 1.0625204394 |
| C (exact-rational) | 1.6111209629 |
| C_* published | 403/250 |
| ε | 0.0465304 |
| Six-step margin | 2.862 rad |

## 3. Scope of this receipt

- **Same algorithm, not an independent engine.** The Dyadic reviewer made the same point. NUMGEN's independent evidence is the primitive-map sampling (`ng_lphase_rm_indep_check_v0_1.py`, `d9d89bae…7ccf`). It found sup |r|/Q^{3/2} = 1.4285 at Q = 1/625, below C_* = 1.612. It also sampled the one-step ratio at |W| = 0.047, finding 0.0319, below ε. Both are recorded in the interface confirmation.
- **P2B gate not run here.** The P2B v2 coefficient comparison (`d59b0ff6…c6ce`) is not part of this replay. Dyadic will add it in the owner draft.
- **No owner status.** This receipt gives the result no owner status in NUMGEN or Dyadic. C_* = 403/250 remains SESSION-reviewed, with owner adoption pending in Dyadic.

## 4. Consequence for NUMGEN

The NUMGEN conditions for citing the result have been met, except owner adoption. Those conditions were: interface objects confirmed (I1–I5), acceptance gate passed, and receipt replay byte-identical. Once Dyadic adopts the theorem, a NUMGEN edition after v1.20.8 may import it by RID.

v1.20.8 keeps the agreed form: an `[OPEN]` sub-item with no C_* value.
