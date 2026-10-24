# Genesis v2.8.9 DRAFT (D-4 scientific) — Occurrence Disposition v0.1

**Date:** 19 October 2026 · **State:** draft companion. Nothing is adopted; adopted Genesis v2.8.8 stays the owner file.

**Identities**
- **Baseline:** adopted v2.8.8 `9abd36169a4bf6056318605c0399ff1f91c53f157b9181bdbfdb9faed3000f37` (1581 lines). Line numbers below refer to this file.
- **Draft:** `RTG_GENESIS_GEOMETRY_DSN_v2_8_9_DRAFT.md`, `b2cc5c5cb637459b3e2aded30b1c48ad859f2591a93684f463f89fbab503f62a` (1645 lines).
- **Control:**
  - occurrence disposition plan v0.1 (`aee218c0…1ee3`);
  - owner-pass manifest v0.1 (`53782f85…0570`);
  - D-4 SESSION v0.1.1 (`1a5f7f56…cee3`);
  - owner decisions of 19 Oct 2026: D1–D5, R-1–R-5, and the primitive proof dependency clarification.

**Build.** `build_v2_8_9_draft.py` (`21388c8b…ac2e`) applies 11 exact-once edits. Reversing them recovers v2.8.8 byte-exactly (gate M1c). The diff has 76 changed lines (`GENESIS_v2_8_8_to_v2_8_9_DRAFT.diff`, `38859e10…c0e7`).

## 1. Edit-by-edit disposition

| ID | v2.8.8 site | Package | Change | S3 rule |
|---|---|---|---|---|
| H1 | line 1 | G9-03 | title → v2.8.9_DRAFT | exact title |
| H2 | lines 4–5 | G9-03 | date 19 Oct (draft); DRAFT owner successor, scientific (D-4, §6.3c); **Not adopted**; adopted owner v2.8.8 | prefix; "Not adopted"; no claim tag |
| H3 | line 7 | G9-03 | "Supersedes (on adoption)" adds v2.8.8 | exact prefix insertion |
| P11 | line 11 (end) | G9-03 | appended sentence "v2.8.9 draft addition", which names the new RID once; it states no selection and no existence | append only; no claim tag; GEN set = {new RID} |
| C1 | after line 55 | G9-02 | §1 `[THM]` summary of the new RID only (R-4) | one tag; required phrases; ends "see §6.3c, SG-15 and SG-16." |
| R5 | after line 624 | G9-02 | §5 row "Transported chiral factor" (certified / forbidden / pointer) | one appended row ending "\| §6.3c, SG-15, SG-16 \|" |
| S6 | before line 850 (`### §6.4`) | G9-01 | **new §6.3c** | block starts with the §6.3c heading; exactly one `[RID:`; GEN set = {new RID, Lemma S, GEN-DEF-PRIMITIVE-MAP} |
| X7 | after line 1145 | G9-02 | §7 `[DEF]` export of the new RID; the primitive companion is **not** exported as a theorem | one tag; GEN set = {new RID} |
| R8 | after line 1186 | G9-02 | §8 RID line, with proof source, certificate hash and the Lemma S dependency | one line; certificate hash prefix; Lemma S RID |
| APPA | before line 1201 | G9-03 | Appendix A v2.8.9 DRAFT record | append only; no claim tag; GEN set = {new RID} |
| FOOT | lines 1577–1578 | G9-03 | draft footer followed by the inherited v2.8.8 footer | prefix plus inherited tail |

**Content of §6.3c**
- `[DEF]` model class 𝒩₃, G^N_γ, G^{(n)}_γ. No RID (R-2).
- `[THM]` `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` (D1), the main statement C3:
  - hypotheses: (H-JET) written out as (i)–(iii), (H-μ), γ ∉ {0,2} and (H_spec);
  - closure under C³ conjugacy;
  - proof (a)–(d), with Lemma S as the explicit algebraic dependency: c = p − q, β = iq, adopted branch.
- `[ALG]` primitive-clock companion. No RID and the same grade as §6.3b (D2). It uses the **direct primitive argument**; the six-step theorem is explicitly not invoked, and the text records that (H_prim) does not imply (H_spec) (owner correction §3).
- `[ALG]` instances:
  - C1: n_T and μ₆, both printed (R-5);
  - C2: through a C³ chart Φ with ΦTΦ⁻¹ commuting with A (R-3). This is a hypothesis; existence is not asserted, and nothing Dyadic is imported;
  - C3: the theorem itself.
- Guards G-JET, G-20, G-SEL and G-OFN at the point of use. They are not a new scope guard.
- `[OPEN]` list. It also states which part of the §6.3b item "other network dynamics" is now covered.
- `[DEF]` evidence, with the full hashes of the D-4 record, the certificate and the manifest.

**Not edited, by design**
- §6.3a, §6.3a.1 and §6.3b (lines 734–848), SG-15 and SG-16.
- The 24 lines carrying the five existing K3/6S RIDs.
- §2 OPEN registry and §7 import ledger.
- The Dyadic v6.4.13 pins (R-1: v6.4.14 repin deferred).
- Every other line of v2.8.8 (M1c).

## 2. Declared deltas (frozen draft)

| Quantity | Delta |
|---|---|
| GEN RID set | + `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` |
| DYAD RID set | none (13 unchanged) |
| OFN / FMS identifiers | none |
| Claim tags | **`[THM]` +4**: §1 summary, §5 row, §6.3c theorem, §8 line. **`[ALG]` +3**: §5 row (primitive companion), §6.3c primitive block, §6.3c instances. **`[DEF]` +4**: §6.3c heading tag, model, evidence, §7 export. **`[OPEN]` +1**: §6.3c. |

The plan v0.1 §3 estimate (THM +2, DEF +4, ALG +3, OPEN +1) did not count the backticked `[THM]` in the §5 row or the §8 line. Following the owner instruction, the exact delta is fixed on the frozen draft and enforced by S1.

## 3. Gates (`check_v2_8_9_draft.py`, `1ac4dd5c…463c`)

| Gate | Plan ID | Content | Result (`--final --cert`) |
|---|---|---|---|
| M1a–c | DM1 | baseline hash; fresh build equals the draft; anchors unique; reverse recovery | PASS |
| M2 | DM2 | §6.3a–§6.3b block (15 480 chars), SG-15, SG-16 and the 24 RID lines byte-identical | PASS |
| M3 | DM3 | Lemma S with c = p − q, β = iq and the branch; (H-μ) explicit; n_T and μ₆ printed | PASS |
| M4 | DM4 | primitive `[ALG]`, no RID, direct argument; (H_prim) not equated with (H_spec); the new RID appears only on the three six-step `[THM]` lines; the export excludes the primitive companion | PASS |
| M5 | DM5 | all four guards present; forbidden selection or existence phrases absent from the added text | PASS |
| M6 | DM6 | certificate hash and a rerun of 6/6 PASS with empty stderr. **SKIP counts as FAIL in `--final`.** | PASS |
| M7 | DM7 | DYAD RID set unchanged; no generator, centralizer or realization RID; no OFN/FMS identifier added | PASS |
| S1 | — | GEN delta = {new RID}; tag delta equals the declared values | PASS |
| S3 | — | 11 edits, each authorized by an independent rule and used once | PASS |

**Results**
- `checker_output_final.txt` (`898a2c6e…9e22`): **11/11 PASS**, exit 0.
- `--final` without `--cert` (`checker_output_final_nocert.txt`, `9067baac…171f`): exit 1, as required, because the M6 SKIP counts as FAIL.

**Negative controls** (`negative_controls_v2_8_9.py` `956383f4…b113`; output `negative_controls_output.txt` `0116d7e8…fc92`). All controls exit 1 with the expected gates failing:

| Control | Caught by |
|---|---|
| NC1 widen `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` (§1 line) | M2, S3 |
| NC2 primitive companion tagged `[THM]` | M4, S1 |
| NC3 (H-μ) hypothesis dropped | M3 |
| NC4 `DYAD-THM-FORMAL-Z6-GENERATOR` imported | M7 |
| NC5 "unique physical model" wording | M5 |
| NC6 one byte changed in §6.3b (draft only) | M1b, M1c, M2 |
| **NC7 (H_prim) equated with (H_spec)** (owner-requested additional control) | M4 |
| NC8 certificate bytes altered | M6 |

## 4. Certificate execution record

- **Script:** `d4_transported_cubic_cert.py`, `f4c382855b130249ce290d3ca939b283aadd27d6ea9a1af551599f4cd9533f6d`, unchanged since D-4 v0.1.
- **Run:** in this workspace, Python 3.13.16 with sympy 1.14.0, invoked as `python -I d4_transported_cubic_cert.py`.
  - Exit 0, empty stderr, 6/6 PASS.
  - Output `cert_execution_output.txt` `0e8053ae21f93844304605716bd58a79c1d210f94b60b8fe7274209622a70df7`, byte-identical to the D-4 recorded output.
  - The same run is executed inside gate M6.

## 5. After review

1. **Independent receiving review** of the draft bytes, this disposition, the build, the checker and the negative controls, run with `--final --cert`. Expected result: 11/11, exit 0.
2. **Owner adoption decision.**
3. **Metadata-only release transform and release checker**, on the v2.8.8 pattern:
   - DRAFT → adopted header, status and footer;
   - the Appendix A DRAFT record kept as history.
4. **Notices citing the adopted hash:**
   - OFN: an informational update to the SESSION notification. The coverage of Q6 stays conditional on OFN's Q6-REG.
   - RRF and FMS: informational.

Until adoption, OFN receives D-4 only as SESSION (D5).
