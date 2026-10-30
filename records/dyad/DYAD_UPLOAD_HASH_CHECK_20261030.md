# DYAD upload hash check — `upload/dyad-sources` (rtg-engine C++ certificates)

**Date:** 30 October 2026. **By:** Claude, Atlas owner.
**Object:** branch `upload/dyad-sources`, commit `59b3f87`. The PI pushed it from the lab server `ailab:/root/rtg-engine` with the commands of the inbox advisory thread. The folder is `upload/dyad-sources/rtg-engine/`: 16 sources, `bulk_cert_results.txt`, `MANIFEST_rtg-engine.txt` and `SHA256SUMS.txt`.

**Evidence:**
- `EV-HASH` for the files.
- `EV-RUN` for the short certificates, rerun here (§3).
- No file was changed, renamed or moved. The originals stay under `upload/dyad-sources/` (intake placement, as for `upload/ofn-records/`).

## 1. Hash check

- `sha256sum -c SHA256SUMS.txt`: 18/18 OK (16 sources, the results file and the manifest).
- Every source hash also equals the hash in the server-side manifest.
- The manifest lists the server folder with timestamps, the SHA-256 of every regular file (the compiled binaries included, which were not uploaded) and the toolchain (g++ 13.3.0). `pkg-config` reported no FLINT/Arb version.
- The DSN records no hash for any of these files (§8, L1154–1162: "not recorded"). Under the recovery-list rule they are accepted as **PI-supplied**, and identified by content.

## 2. Identification against the Dyadic §8 registry (`dyad-v6.4.22`)

| Uploaded file (SHA-256 prefix) | Registry artifact | Identification |
|---|---|---|
| `open18_arb_cert3.cpp` (`a9acb69f…6ae4`), 4 May 2026 13:12 | DYAD-ART-OPEN18 `open18_arb_cert_final.cpp` | **identified by its own first line**, `// open18_arb_cert_final.cpp`. The server copy carries the name `…cert3`. `open18_arb_cert.cpp` (`30f2a5e6…ebf1`) and `open18_arb_cert2.cpp` (`4bee1309…13ed7`) are earlier versions from the same day: fixed-box and then adaptive sweeps, without the Θ-denominator check |
| `certify_transition_strip2.cpp` (`f1baf422…e275`) | DYAD-ART-STRIP2 | name equal |
| `certify_transition_strip.cpp` (`69fe019d…a32c`) | DYAD-ART-STRIP1 | name equal |
| `rtg_ia_bulk_cert.cpp` (`acbff177…e81f`) + `bulk_cert_results.txt` (`3ea62fdb…c095`) | DYAD-ART-IA-BULK | name equal; the results file is a run record of the sub-branches (4,11), (5,11), (5,12) |
| `certify_q_max.cpp` (`af2f5cc5…99a9`) | DYAD-ART-QMAX | name equal |
| `certify_branch_4_10.cpp` (`41b5aa13…6970`) | DYAD-ART-IA-CERT-FIXED `rtg_ia_cert_fixed.cpp` ("Arb ball certification on (4,10) branch") | **candidate only**. The content matches the description (the IA-BULK header calls it "the validated (4,10) engine"), but the name differs and no hash is recorded. Not identified |
| `rtg_core.hpp` (`5336f207…de93`) | — (header used by five sources) | needed to build |
| `certify_g_monotonic.cpp`, `certify_s_max.cpp`, `test_arb/jet/map/state.cpp` | not cited in the DSN | engine checks and tests; `test_map.cpp` and `test_state.cpp` are byte-identical |
| `triad_t3a_arb_enclosure_v4g.cpp` (`430015bb…fd32`) | not Dyadic: a Triadic T-3a Arb enclosure | for the Triadic migration (separate) |

The recovery list is updated accordingly:
- five files are placed (OPEN18, STRIP2, STRIP1, IA-BULK, QMAX);
- `rtg_ia_cert_fixed.cpp` stays missing, with the candidate noted.

## 3. Reruns in the Atlas sandbox

Toolchain: g++ 13.3.0, FLINT 3.0.1 (Ubuntu `libflint-dev`). Every source compiled unchanged with `g++ -O2 -std=c++17 <file> -lflint`. Outputs, with their hashes, and the rerun script `run.sh` are in `evidence/atlas/dyad_inbox_20261030/cert_runs/`.

| Certificate | Run here | Result |
|---|---|---|
| `open18_arb_cert3.cpp` (OPEN 18 "final") | 0.13 s | Micro strip q ∈ (0, 0.001]: d²Q₃/dq² ∈ [2.0 ± 0.0473], d²N_Θ,3/dq² ∈ [−1.0 ± 0.0242]. Γ₃ (n = 3) on [0.001, 1.26021320256]: 11 701 boxes. Γ₄ (n = 4) on [1.26021520256, 2.0]: 81 boxes. All SUCCESS ("THM-READY") |
| `certify_transition_strip2.cpp` (OPEN 11 T1) | < 0.01 s | On [0.9004911, 0.9004916]: F changes sign (3.495e−7 / −4.786e−9) and F′ ∈ [−0.709 ± 7.0e−4] excludes 0, so the IFT applies |
| `certify_q_max.cpp` | < 0.01 s | Q_max = Q⁽²⁾(2.0) ∈ [0.2644325152160405178595027 ± 3.5e−26] |
| `open18_arb_cert2.cpp` (earlier version) | 0.17 s | same boxes and SUCCESS as the final version; no Θ-denominator check |
| `open18_arb_cert.cpp` (first version) | 0.02 s | fixed 2000-box sweep: Γ₃ **FAIL**, Γ₄ SUCCESS. This shows why the adaptive versions followed; the final version supersedes it |
| `certify_g_monotonic.cpp`, `certify_s_max.cpp` (not cited in the DSN) | < 0.01 s | g′(ρ) > 0 certified on its domain; s_max^{F1} ∈ [0.5237212707001281468486508 ± 1.2e−26] |
| `certify_branch_4_10.cpp` (IA-CERT-FIXED candidate) | stopped at the 300 s limit | zones 1–2 of 5 (10⁷ slices each) certified before the stop, with no failure printed; not a completed run |
| `certify_transition_strip.cpp`, `rtg_ia_bulk_cert.cpp` | not run here | 1.5·10⁷-slice and 3·10⁶-per-zone sweeps, for the lab server. `bulk_cert_results.txt` is the PI-supplied record of an earlier IA-BULK run: all three sub-branches CERTIFIED, 0 structure and 0 positivity failures |

## 4. What the OPEN 18 certificate settles for the NUMGEN q* question (pipe item D1)

The certificate source defines the branches by the footprint step: Γ₃ ↔ n = 3, Γ₄ ↔ n = 4. It sweeps them on either side of a gap of half-width 10⁻⁶ centred at 1.26021420256. Branch legality and the root isolation of q* are "supplied by independent footprint audits", which are not recovered.

**Atlas reading (`EV-RUN`, `evidence/atlas/dyad_inbox_20261030/qstar_dyad_split.py`).** The script tests ρ_k, η_k, Θ_k + π/3 and Θ_k + 2π/3 for k ≤ 6 inside that gap. Only ρ₄ changes sign there, and equivalently Θ₄ + π/3 (on ρ = 0, Arg W = −π/3 for η < 0). The root is

  q_*^DYAD = 1.26021420256347711487243856095650439…

which lies 3.5 × 10⁻¹² from the gap centre. At q_* the fourth iterate meets the ISP-funnel edge Θ = −π/3 (§6.8):
- just below q_*, Θ₄ = −1.0471965 > −π/3 (outside the funnel);
- just above q_*, Θ₄ = −1.0471986 < −π/3 (inside).

The OPEN 11 bulk record shows the same split between the (4,11) and (5,11) sub-branches (1.260 | 1.261).

**Consequence.** NUMGEN's q* = 0.315625883659561602974267621967906111219946754… (root of η₆(q) − q, `numgen-v1.21` L909, reproduced in `qstar_repro.py`) is **a different number**. The two documents use one symbol, q*, for two objects on the same canonical family.

This is an Atlas reading of a recovered PI-supplied certificate, not a Dyadic owner statement. The Dyadic owner confirms or corrects it and states the footprint definition, which lives in the unrecovered audits.

## 4a. Second upload — branch `missing-files`, commit `3e62f1a`

The PI pushed two zips to `upload/dyad-sources/` on a branch named `missing-files`. Its base `07df334` is an older `main` commit, an ancestor of the current `main`, so a merge adds exactly these two files; it was merged unchanged into the advisory branch.

| File | SHA-256 | Identification |
|---|---|---|
| `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` | `e4e2bab004d4e39b76920e486607acc34749037ae2638809a9c2117d548fdbe4` | **equal to the hash recorded** for DYAD-ART-RE-P2B2 (L1177; recovery list Tier 1) |
| `NUMGEN_v1_20_8_DRAFT_r3_REVIEW.zip` | `a7fc9ed63113e7f6f48296b9593b92467b94314d71f5117e106cf9dcdbe1ee84` | a NUMGEN review package. Its folder `replay_inputs_dyad/` holds four DYAD-ART-LPHASE-ROWA files, each **equal to its recorded hash**: `dyad_numgen_lphase_rowA_cert.py` `117484ae…9cdb`, `qw.py` `3a913062…cce8`, `tzw.py` `f007d42c…5609` and `lphase_rowA_certificate.json` `8697c697…d4fa`. It also holds `lphase_rowA_perf.json`, a timing file, not cited |

**Reruns** (`EV-RUN`; `evidence/atlas/dyad_inbox_20261030/rerun_notes.md`, logs and hashes alongside):
- **P2-B v2.** `run_all.py` on an extracted copy runs 7/7 jobs as expected: three positive and four negative controls. The regenerated `certificate.json` is byte-identical.
  - The certificate's exact rational upper bounds are C₇ ≤ 85.0731933471… (|z| ≤ 1/20) and C₇ ≤ 27.6022209836… (|z| ≤ 1/40).
  - The DSN's "certificate values 85.07 / 27.60" are therefore nearest-rounded, not ceilings. RECOG's outward values 85.1 / 27.7 are valid ceilings of the certified bounds.
- **L-PHASE row A.** The certificate runs PASS (10 gates; N1–N6 false), and the regenerated JSON is byte-identical.
  - The certified constants are exact rationals: c_Q = 0.79245761523303… and c′_Q = 0.36915230466066….
  - The published c_Q = 0.79246 is an outward ceiling. The published **c′_Q = 0.36915 is not**: it lies 2.3 × 10⁻⁶ below the certified value (exact-arithmetic check: c′_Q > 0.36915, c′_Q ≤ 0.36916).
  - The theorem's published constant 403/250 is unaffected, because the certificate uses the exact c′_Q internally (FIN: 1.61112… ≤ 1.612).
  - The decimal "c′_Q = 0.36915" in the DSN proof outline (L902), and RECOG's `[assuming:]` copy of it, are not certified ceilings.

Still missing for DYAD-ART-LPHASE-ROWA:
- the illustration and scope files (`lphase_rowA_numeric.*`, `lphase_scope_checks.*`);
- the provenance gate (`dyad_lphase_p2b_provenance_gate*.py`, its two JSONs);
- the three Dyadic session records.

None is needed for items D2 and D3.

## 5. Not claimed

- No Dyadic grade, statement or registry entry is changed.
- The reruns confirm that the recovered sources reproduce their printed success lines on this toolchain. They do not re-audit the arguments: for example, the micro strip's use of the second derivative, or branch legality.
- `certify_branch_4_10.cpp` is not identified as `rtg_ia_cert_fixed.cpp`.
- The second upload supplies the evidence for D2 and D3 (§4a). Whether to register the constants, and with which outward values, is the Dyadic owners' decision.
