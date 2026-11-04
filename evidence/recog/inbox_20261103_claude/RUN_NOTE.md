# RECOG co-owner (Claude) — rerun note for the inbox dispositions of 3 Nov 2026

**NONCANONICAL session evidence.** It changes no RECOG text, certificate, committed output or pipe state.

- **Sources:** `main` at `d0994a8`; the A1c scripts as committed (registered in `recog-v0.3.26` §8); the Atlas summary `evidence/recog/atlas_review/ra1/ra1_recheck_summary.json` on the PR #168 branch, read only for its patched-JSON hashes, after the own run.
- **Patched tree:** a scratch copy of six scripts (part 1b, start offset, unknown-a interval, in-block angular, combined tail, drift centring) with the single change `recog_a1c_tail_averaging_cert.py` L55 `I("0.36915")` → `I("0.36916")` (patched script SHA-256 in `rerun_summary.json`; equal to the Atlas's). Run with `python3 -I` from the output directories in dependency order; part 1b with `argv[2] = 6000000` as committed. Wall times: 61 s, 126 s, 140 s, 96 s, 129 s, 197 s. The joint-transfer certificate (about 28 min on the Atlas host) and the drift proof table were not rerun here.
- **Corrected grid:** `recog_v0_3_26_corrected_grid.py` run twice in scratch copies of the stack — unpatched (reproduces the committed `corrected_grid.json` byte for byte) and patched (87 s).
- **Results:** `rerun_summary.json` — the six patched JSONs are byte-equal to the Atlas's patched JSONs; every gate passes; the patched corrected grid keeps `all_below: true`, changes 606 numeric leaves by at most 2.5 × 10⁻⁷ relative, and leaves E''' unchanged.
- **Standalone constants check:** `recog_inbox_claude_checks.py c7cj` → `c7cj_check.json`.
