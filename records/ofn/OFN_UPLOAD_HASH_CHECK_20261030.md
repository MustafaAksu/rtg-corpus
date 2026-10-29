# OFN custody intake — hash check of `upload/ofn-records` (commit `c6fd574`)

**Date:** 30 October 2026. **By:** Claude, atlas owner. **Object:** branch `upload/ofn-records`, commit `c6fd5743dea3e5e2b6162d1242d03cad2bba1078` (29 Oct 2026, "OFN v0.10 originals held by co-owner session claude012ZC8x (unchanged)"), one commit on `main` `b0dc6db`, 21 files, all under `upload/ofn-records/`. **Status:** record (`EV-HASH`, `EV-RUN`); the PI merges the upload PR.

## 1. Manifest

`upload/ofn-records/SHA256SUMS.txt` lists 20 files; `sha256sum -c` from the extracted tree: **20/20 OK** (`evidence/atlas/rowcheck/ofn_v0_11/upload_sha256sum_check.txt`). No file outside the manifest except the manifest itself.

## 2. Against the hashes OFN already prints

`ofn-v0.10` (`acb70a8c…5dfa`) prints abbreviated or full SHA-256 values for 13 of the 20 files; each **matches** the manifest: `build_ofn_v0_10_draft1.py` (`6a4fe7af…58ff`), `build_ofn_v0_10_draft2.py` (`930b0aef…5c82`), Draft 1 (`d94e1e39…8c36`), Draft 2 (`58e2dec5…3610`, full), `iso_check.py` (`b92f6659…0d75e`), `iso_quadratic_nogo.py` (`91fd63f4…5308`), `transported_pq.py` (`2dcd4331…20bf6`), `OFN_PSI_KAPPA_EXTENSION_v0_1.py` (`6566009c…5f88`), `OFN_PSI_KAPPA_ALL_MINOR_CHECK_v0_1.py` (`c56a01ac…a9e3`), `OFN_PSI_INVARIANT_C_CHECK_v0_1.py` (`18f10aa4…b114`), `OFN_PSI_INVARIANT_C_GAUGE_CHECK_v0_1.py` (`d3e5cedf…9781`), `OFN_PSI_REFLECTION_AUDIT_v0_1.py` (`e6d9b089…235a`), `OFN_STAB_F3_CHECK_v0_1.py` (`8b415461…e5ea9`). Not printed in OFN v0.10 (identity from the manifest and, for the first two, from the v0.10 release record): `RTG_ONTOLOGICAL_FOUNDATIONS_v0_10_RELEASE_RECORD.md` (`10a1ec6b…0844`), `release_ofn_v0_10.py` (`2aca119f…4f5f`, named in that record), `transported_sim.py`, `basin_test.py` (named in OFN §12.1 without hash), `k3_six_step_factor_check.py`, and the two v0.8 input reviews (`8d18640f…0944`, `f86cd483…c5b8`).

## 3. Replay of the v0.10 chain (`EV-RUN`)

- `build_ofn_v0_10_draft2.py` on the uploaded Draft 1 → `58e2dec54ad600dec189119adc16c8ca89872e74419f78ae317f33558a913610` = the uploaded Draft 2 and the approved object of the v0.10 release record.
- `release_ofn_v0_10.py` on the uploaded Draft 2 → `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa` = the `ofn-v0.10` file. The script then runs a post-check that reads `RTG_ONTOLOGICAL_FOUNDATIONS_v0_9.md`, which is not held; it stops there after writing the output.
- Draft 1 from v0.9 (`build_ofn_v0_10_draft1.py`) is not replayed: the v0.9 bytes (`5ae8fdab…9795`) are not in the repository.

So the v0.10 edition is now reproducible from placed originals from Draft 1 on, and its release record is placed. Once merged, BASELINE's OFN authority can name `upload/ofn-records/RTG_ONTOLOGICAL_FOUNDATIONS_v0_10_RELEASE_RECORD.md` instead of the RECOG cross-reference (or the v0.11 release record after that tag).

## 4. Still not held

As the OFN v0.11 DRAFT release record §4 states: `transported_chiral_pq.py` (`09129ffc…73ac`) — held by neither OFN session; the FMS ψ scripts (`ad44f66a…`, `5af23da9…`); ER-2B v0.3.1 (`711e427a…81b4`, source-reported); `REVIEW_FINDINGS.md`, `OFN_TDRG_FINDING_A_HANDOFF.md`, `OFN_v0_9_PROGRAMME_AND_OWNER_SYNC_REQUEST.md`; the v0.9 release record and validation files and the v0.9 bytes; the v0.8 release record (`0015347c…0848`, held by the ChatGPT session, not uploaded). Missing evidence is "not supplied", not refutation (Methodology v1.4 §7).
