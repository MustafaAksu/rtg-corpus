# Number Genesis — Receiving review of `DYAD_NUMGEN_LPHASE_ANGULAR_ENCLOSURE_SCOPE_v0_1`

**Date:** 20 October 2026 · **From:** Number Genesis owner side (Claude, DSN editor/auditor). The PI keeps the final decision. · **To:** Dyadic DSN owner; PI
**Status:** `[SESSION]` receiving review. No owner file is modified; nothing is adopted.
**Verdict:** **SCOPE ACCEPTED FROM THE NUMGEN SIDE.** The certificate step may proceed once the PI approves it. Six notes follow (§3). None of them blocks the certificate.

## 1. Identity of what was reviewed

| File | SHA-256 | Check |
|---|---|---|
| `DYAD_NUMGEN_LPHASE_ANGULAR_ENCLOSURE_SCOPE_v0_1.md` | `1eae1d1a…1f74` | matches the stated hash; the uploaded copy and the package copy are identical |
| `lphase_scope_checks.py` | `570078db…8cb6` | matches |
| `lphase_scope_checks.json` | `9b31c710…3f25` | matches |
| `DYAD_NUMGEN_LPHASE_SCOPE_PACKAGE_v0_1.zip` | `8330b84c…f18c` | matches |

## 2. What was re-executed or re-derived

- **Replay.** `python3 -I lphase_scope_checks.py` was run in a clean folder. Result: `RESULT: PASS`. The regenerated JSON is **byte-identical** to the packaged one (`9b31c710…3f25`). Run time was about 8 s.
- **S1 by hand.** Check of `Λ₃ = L_Θ + τD₃` from the adopted v6.4.14 harmonic forms:
  - cos: `−√3/8 − 5√3/9 = −49√3/72`
  - sin: `−7/24 + 1/3 = 1/24`
  - cos 3Θ: `5√3/48 + √3/18 = 23√3/144`
  - sin 3Θ: `−11/48 − 1/6 = −19/48`

  Hence `Λ₃(0)/r³ = (−98 + 23)√3/144 = −25√3/48`. This is exactly NUMGEN v1.11's quartic-jet coefficient on the positive-u ray (v1.20.7 L2131). All signs and coefficients agree.
- **Identity D.** The exact identity holds under (B1) and (B2), including the `+` sign of `S_Θ`. This agrees with NUMGEN's own derivation in `NUMGEN_REPLY_TO_DYAD_LPHASE_ENCLOSURE_20261020_v0_1.md` §2.
- **Independent `[NUM]` check.** The script `ng_lphase_rm_indep_check_v0_1.py` (`d9d89bae…7ccf`; log `e2a0d15a…f661`) was written from NUMGEN's definitions only. It uses the primitive map, the lifted six-step angle and `r = lift − 2π + τQ`, and no Dyadic code. Settings: 1440 angles per circle, 40 digits.

| Q | sup\|r\|/Q^{3/2} | max\|δ_T − π/3\|/√Q |
|---|---|---|
| 2.209·10⁻³ (U_T edge) | 1.43328 | 0.4516 |
| 1.6·10⁻³ (= 1/625, U edge) | 1.42849 | 0.4516 |
| 4·10⁻⁴ | 1.41456 | 0.4517 |
| 10⁻⁴ | 1.40748 | 0.4517 |
| 2.5·10⁻⁵ | 1.40391 | 0.4517 |
| 6.25·10⁻⁶ | 1.40212 | 0.4517 |

`Λ* = 1.40032256532` is attained at Θ ≈ 0.5671. That point is Dyadic's 3.7087 minus π: `|Λ₃|` is π-periodic, because Λ₃ has only odd harmonics. All S3 and S5 values in the scope note are reproduced to the printed digits.

## 3. Notes

1. **The floor for C_\* on the tube is about 1.43, not 1.40.** `Λ*` is the asymptotic value. The finite-Q supremum rises towards the tube edge: 1.4285 at `Q = 1/625`, and 1.4333 at the `U_T` bound. So a certified C_\* valid on all of `U` must exceed about 1.43. The `[HEUR]` estimate of about 1.7 still leaves a margin of about 0.27. This is not a defect; it sharpens §3 "Finding for NUMGEN".

2. **NUMGEN v1.10 range: accepted.** NUMGEN agrees that `[1.3449, 1.3565]` (v1.20.7 L3073) was orbit-sampled over a 256-fold `Q_0` range and did not reach the maximizing angles. It is a historical changelog figure and is not edited. If the certificate is imported, v1.20.8+ will cite C_\* and add a one-line pointer that the orbit range is not an angular supremum.

3. **Source of the one-step bound (correction on the NUMGEN side).** The bound `π/6 < δ_T < π/2` with error constant `143209/750000`, which the NUMGEN memos called "RECOG's explicit one-step bound", is **not in RECOG v0.3.21**. Its source is the RECOG A1a session record `RECOG_A1A_CD_IDENTIFICATION_SESSION_v0_2.md` (`b4906ddf…c428`), as cited in `RECOG_A1A_C4_QUESTION_TO_NUMGEN_20261020_r2.md`. That record is accepted at session-record level only. The "C1" label came from a summary and is not a RECOG identifier. Dyadic was right not to find it. **NUMGEN supports Dyadic's choice to build P-c on its own one-step majorant.** That keeps owner-grade custody clean. Importing from the RECOG session record would need RECOG owner adoption first. The S5 scale (0.4517·√Q ≤ 0.0213 on `U_T`) is far inside the (π, 3π) window.

4. **Domain: U is accepted; U_T is optional.**
   - The scope note covers orbits started in `U = {Q ≤ 1/625}`. The canonical NUMGEN seed lies there, so this suffices for NUMGEN's named results.
   - NUMGEN's L-MONO/INF-1 statements are phrased on the six-phase tube. v6.4.14 already records `Û_T ⊂ {|z| < 1/20}`, and P-c is designed on `U_T`.
   - If extending the combination to starts in `U_T` costs nothing extra, NUMGEN would welcome it as a second statement.
   - The finite-Q floor at the `U_T` edge is about 1.433, per Note 1.

5. **Combination template: valid, could be tighter.** In §5 the `c₇q³` term is bounded by `(c₇/400)q^{3/2}`. This is valid because `q^{3/2} ≤ q ≤ 1/400`. The sharper `q^{3/2} ≤ (1/20)³ = 1/8000` gives `c₇/8000`. The change is optional; it does not affect correctness.

6. **Provenance (the scope note's request).** The PI should forward these three files to Dyadic so that their hashes can be recorded:
   - `NUMGEN_REQUESTS_TO_DYAD_20261020_v0_1.md` — `a2c49d2eac2f7554c056a595b7211b2b33850c32397b2a79c2fac484e640776a`
   - `NUMGEN_REPLY_TO_DYAD_LPHASE_ENCLOSURE_20261020_v0_1.md` — `1d0b4dce6bfb2476d16ab5f8a6a89dac6ca0a8e65724c72d76a263310f02e5a3`
   - this review and the independent check script with its log (hashes in §2)

## 4. Agreements recorded

- **Ownership.** Dyadic certifies P-a, P-b and P-c and the combined constant, and exports them as a separate import. NUMGEN keeps L-PHASE and L1, and decides whether to cite C_\*. This is the split NUMGEN proposed.
- **SG-19.** The four conditions stated in scope note §7 are accepted as the NUMGEN reading.
- **N3 / φ\*.** Dyadic's reasoning is accepted. NUMGEN removes the pin in v1.20.8 and keeps the `[CAND]` cap. There will be no citation of the asymptotic phase objects without a separate comparison proof.
- **Receipts.** N10–N13 remain RECEIVED at session level until v1.20.8. N14 is not addressed to NUMGEN.

## 5. Gate the certificate should meet, as seen from NUMGEN

The NUMGEN-form statement must be `|r_m| ≤ C_* Q_m^{3/2}` for every block of every orbit from `U` (row A), with:
- C_\* given as an exact rational;
- the Q ↔ q bridge (P-a1) applied explicitly;
- all six negative controls of §6 failing as required.

NUMGEN will check an imported C_\* against the independent primitive-map sampling in §2. Any C_\* below the sampled 1.4285 at `Q = 1/625` would be rejected outright.

**Not claimed:** any certified constant; any change to L-PHASE's grade; any change to NUMGEN or Dyadic owner text.
