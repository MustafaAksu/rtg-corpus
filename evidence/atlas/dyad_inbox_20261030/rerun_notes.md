# Reruns of the two recovered Dyadic certificates (30 October 2026, Atlas sandbox)

Inputs are the members of the zips on `upload/dyad-sources` (commit `3e62f1a`, branch `missing-files`), extracted to a scratch copy; nothing in `upload/` was changed.

1. **P2-B v2** (`DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip`, `e4e2bab0…dbe4` = the DSN's recorded hash).
   - Command: `python3 -I DYAD_RETURN_ENCLOSURE_P2B_v2/scripts/run_all.py` on a copy of the extracted package (Python 3.13.16, sympy 1.14.0, mpmath 1.3.0).
   - Result: 7/7 jobs as expected (`run_status.json`): certify, independent, numerical_sanity PASS; negative_tail10, negative_C7, negative_derivative, negative_raw_lattice exit 1 as required.
   - `outputs/certificate.json` is byte-identical to the packaged one.
   - Exact rational upper bounds: C₇ ≤ 85.07319334710797… on |z| ≤ 1/20 and ≤ 27.60222098362114… on |z| ≤ 1/40; C_D ≤ 812.89362494832… and ≤ 216.76641142802….
2. **L-PHASE row A** (`replay_inputs_dyad/` inside `NUMGEN_v1_20_8_DRAFT_r3_REVIEW.zip`).
   - The four files match the DSN's recorded hashes: `dyad_numgen_lphase_rowA_cert.py` `117484ae…9cdb`, `qw.py` `3a913062…cce8`, `tzw.py` `f007d42c…5609`, `lphase_rowA_certificate.json` `8697c697…d4fa`.
   - Command: `python3 dyad_numgen_lphase_rowA_cert.py` in a scratch folder holding the three code files.
   - Result: RESULT: PASS; 10 gates true, N1–N6 false; the regenerated JSON is byte-identical (`8697c697…d4fa`).
   - The certified constants are exact rationals, shown as floats in the JSON: c_Q = 0.79245761523303… and c′_Q = 0.36915230466066…, with c_Q ≤ 0.79246 but **c′_Q > 0.36915** (checked in exact arithmetic; c′_Q ≤ 0.36916).
