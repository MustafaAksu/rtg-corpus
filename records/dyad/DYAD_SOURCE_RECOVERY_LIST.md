# DYAD — missing source files (recovery list)

**Date:** 22 October 2026. **Prepared by:** Claude (atlas owner). **Status:** working record at a fixed path; updated as files arrive. **Collection deferred by the PI (22 Oct 2026):** most files are on the PI's machine; they will be gathered later. Until then the DSN's availability notes stand.
**Source of the list:** every file name cited in `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` v6.4.21 (tag `dyad-v6.4.21`), mostly from the §8 artifact registry, checked against the repository tree and the members of the ZIP packages in it.
**Result:** 155 distinct files cited; 15 present (`normalize_p6_liegauge_exact.py`, `dyad_h4_archival_exact_check.py`, `qw.py` inside the OPEN 20 packages, three records, and the nine files of the placed table below); **140 missing** (plus one closeout record not cited in the DSN): Tier 1 60, Tier 2 43, Tier 3 28, Tier 4 10.
**Correction (30 October 2026, atlas owner):** the first extraction missed the six C++ (FLINT/Arb) certificate sources cited in the §8 registry (`DYAD-ART-OPEN18`, `-STRIP2`, `-STRIP1`, `-IA-BULK`, `-QMAX`, `-IA-CERT-FIXED`); they are added below (Tier 1: the two cited by closed theorems; Tier 2: the four `[ENG]` entries). A full re-check of every backticked file name of `dyad-v6.4.21` and `dyad-v6.4.22` against this list and the repository finds no other omission. Found while preparing `records/dyad/ATLAS_ADVISORY_DYAD_INBOX_20261030.md`.

**Goal.** Anyone using the repository can test every DYAD claim from the repository alone. A missing file here does not mean the work was not done; it means its evidence is not independently inspectable from the repository.

**How to deliver.** Upload the files as you find them, unchanged, to a branch `upload/dyad-sources` (any folder layout). Claude then:
1. checks each file's SHA-256 against the value below, where one is recorded; a file with no recorded hash is accepted as PI-supplied and marked so;
2. places scripts under `evidence/dyad/scripts/` and records under `records/dyad/`, with their original names, and evidence ZIPs under `evidence/dyad/`, kept as received;
3. updates this list, `BASELINE.md` and, at the next DYAD release, the §8 entries (pins and availability).
A file whose content differs from its recorded hash is still useful; it is recorded as a different version, not as the cited one.

**Search hints.** Your local tree `C:\GIT\rtg-resonance-2025\rtg-ns-bifurcations\src\rtg-toolkit\scripts\dyadic` is the likely home of most scripts; session records and evidence ZIPs were project uploads (Claude/ChatGPT downloads). Tier 1 first: the return-enclosure evidence (`DYAD_RETURN_ENCLOSURE_P0_P1_evidence.zip`, `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` with `certificate.json`) underlies §6.14, on which the OPEN 3, OPEN 21 and L-PHASE theorems rest.

Closeout C-2 items are included in Tier 3 (`OPEN9_arithmetic_horizon_definitions.md`, `DYAD_RESPONSE_TO_DZT_REQ-002.md`, `OPEN9_full_onestep_normalization_table_v2.md`, the P1/P2 session records) plus `DYAD_v6_4_17_v6_4_18_RELEASE_RECORD_ADDENDA_v0_1_1.md`, which the closeout names but the DSN does not cite. Hashes shown with an ellipsis are recorded only in short form in the DSN.

## Placed (30 October 2026)

PI-supplied on `upload/dyad-sources` — the C++ sources from `ailab:/root/rtg-engine` (commit `59b3f87`, kept under `upload/dyad-sources/rtg-engine/`; the DSN records no hash for them, so identification is by name or content) and two zips (branch `missing-files`, commit `3e62f1a`; the DSN's recorded hashes match). Hash-checked in `records/dyad/DYAD_UPLOAD_HASH_CHECK_20261030.md`; files kept unchanged.

| Cited file | §8 RID | Placed as | SHA-256 |
|---|---|---|---|
| `open18_arb_cert_final.cpp` | DYAD-ART-OPEN18 | `open18_arb_cert3.cpp` (first line names itself `open18_arb_cert_final.cpp`) | `a9acb69f532a8535c6e18a1da3658a33587737874436ff7020734fba01d36ae4` |
| `certify_transition_strip2.cpp` | DYAD-ART-STRIP2 | same name | `f1baf4221481c52fec1875560c80896c381c074017374ee24e7eb47a3722e275` |
| `certify_transition_strip.cpp` | DYAD-ART-STRIP1 | same name | `69fe019d5b27653a973f3725ce6aaf4962cb2447b32e3fb78269d96de0d3a32c` |
| `rtg_ia_bulk_cert.cpp` | DYAD-ART-IA-BULK | same name (+ run record `bulk_cert_results.txt`) | `acbff177b0a799fd779bd17478db474e2dc3479621383b7cb239a6476130e81f` |
| `certify_q_max.cpp` | DYAD-ART-QMAX | same name | `af2f5cc57300230d683616e9e19c3243a1ba7c6667be9a4094f3f24b9b1299a9` |
| `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` | DYAD-ART-RE-P2B2 | same name, `upload/dyad-sources/` (branch `missing-files`, `3e62f1a`); recorded hash matches | `e4e2bab004d4e39b76920e486607acc34749037ae2638809a9c2117d548fdbe4` |
| `dyad_numgen_lphase_rowA_cert.py` | DYAD-ART-LPHASE-ROWA | member `replay_inputs_dyad/` of `upload/dyad-sources/NUMGEN_v1_20_8_DRAFT_r3_REVIEW.zip` (`3e62f1a`); recorded hash matches | `117484ae1a2509b6f6065d395840bfdfe2b0c977af0505f9fe6de68c13959cdb` |
| `lphase_rowA_certificate.json` | DYAD-ART-LPHASE-ROWA | same zip member folder; recorded hash matches | `8697c6970bd908327c66ef2ce3b2d38386947899033ef7f720bc096c4c3ad4fa` |
| `tzw.py` | DYAD-ART-LPHASE-ROWA | same zip member folder; recorded hash matches | `f007d42cde36d2a70115b9db25f47b107c446735fa31c66664f620c3247a5609` |

## Tier 1 — certificates and exact/theorem evidence (scripts, their outputs, evidence packages) — 60 files

| File | §8 RID | Grade of the registry entry | Recorded SHA-256 |
|---|---|---|---|
| `rtg_b5_Seff_limit_cert.py` | DYAD-ART-B5-ALLP-CERT | ALG | not recorded |
| `rtg_b5_secular_decomposition.py` | DYAD-ART-B5-DECOMP | ALG/NUM | not recorded |
| `rtg_extract_b5_secular_coeff.py` | DYAD-ART-B5-SECULAR | ALG | not recorded |
| `rtg_b5_step3_reduction.py` | DYAD-ART-B5-STEP3 | ALG | not recorded |
| `exact_Fraw_b5_sweep.py` | DYAD-ART-FRAW-B5-SWEEP | ALG | not recorded |
| `exact_Fraw7_certificate.py` | DYAD-ART-FRAW7-B5 | ALG | not recorded |
| `gauge_bridge_p6.py` | DYAD-ART-GAUGE-BRIDGE | ENG/ALG | not recorded |
| `jet1_deg5.json` | DYAD-ART-JET1 | ALG | not recorded |
| `jet6_deg5.json` | DYAD-ART-JET6 | ALG | not recorded |
| `dyad_lphase_p2b_provenance_gate.py` | DYAD-ART-LPHASE-P2B-PROV | ALG | `5cff2b46eee14d157678320d173c2ca6fe8fa4dcb248018d5ab3d8646e0bf59f` |
| `dyad_lphase_p2b_provenance_gate_v0_1_1.py` | DYAD-ART-LPHASE-P2B-PROV | ALG | `343a3631f41e41741f3c0b6e99b6431fe2e0635b7821f9f71674b5f1878a27a5` |
| `lphase_p2b_provenance_control_exits.json` | DYAD-ART-LPHASE-P2B-PROV | ALG | `e2ffa46bced46fff76044a1a651281557b93a70fa7ab96dc13cb1e8f859c1a1e` |
| `lphase_p2b_provenance_gate.json` | DYAD-ART-LPHASE-P2B-PROV | ALG | `58cfafd359da64ef8b20f12b656fe3e8ab8b69e559cd46574767c8629692fc89` |
| `lphase_rowA_numeric.json` | DYAD-ART-LPHASE-ROWA | NUM/THM | `2291db4e1404654427b567bdba338ea1ce0ddd0b7f4e8bad1bd8b03b16d1b9c4` |
| `lphase_rowA_numeric.py` | DYAD-ART-LPHASE-ROWA | NUM/THM | `95b891f8f62b42342c0307e77b0f8c13e68cc7f5a3b9d368b18a1a3e4c3a4647` |
| `lphase_scope_checks.json` | DYAD-ART-LPHASE-ROWA | NUM/THM | `9b31c7107a9d1e44cb19b213e1060f5aead30dddc7b79a49b6ca42372d1c3f25` |
| `lphase_scope_checks.py` | DYAD-ART-LPHASE-ROWA | NUM/THM | `570078dbfc2c8a881c47c4a468370452e0a5d76e8c73055857196e99e49cd8b6` |
| `dyad_m2c_nu5_p5_exact.py` | DYAD-ART-NU5-P5 | ALG | `5fcccb9d38a7dcafe317044ca341cbead38047e24041da92e6fe891faa5cd464`, `5fcccb9d…d464` |
| `open16_alias_phase.py` | DYAD-ART-OPEN16 | ALG | not recorded |
| `open17_a2.py` | DYAD-ART-OPEN17 | ALG | not recorded |
| `dyad_open19_a0_boundary_check.py` | DYAD-ART-OPEN19-KERNEL | ALG | `a2aedc51acef70738e5b6006c601c036d5ee182a5d2eb899beb92c5dc4303a45` |
| `dyad_open19_kernel_check.py` | DYAD-ART-OPEN19-KERNEL | ALG | `1cb40446c0289424fcb8539c77aec6d43f4e6a0873434645b8cc3dc4397a291e`, `1cb40446…291e` |
| `dyad_open19_R0_identity_cert.py` | DYAD-ART-OPEN19-R0CERT | ALG | `c8c144426b2c9e795df19a997b181209fce6ab7edeaa1b9c04e731ad0d059cf8` |
| `binf_integration_check.json` | DYAD-ART-OPEN20-BINF-CHECKS | ALG | `26ef2748045cb0ceac138beb2f211f4dc5ff2aa17d7d47c81e2e387bca078f5f` |
| `dyad_open20_binf_integration_check.py` | DYAD-ART-OPEN20-BINF-CHECKS | ALG | `0d5a1dfdc13a7bfe7d3ebbe63d5dc1d8f88baff44f663fddaff4b765c2fb0264` |
| `dyad_open20_p3a_check.py` | DYAD-ART-OPEN20-BINF-CHECKS | ALG | `56d8178109b34a8858dca6d3d5470524916ae850390bf2a81b86d9ddf2e67140` |
| `dyad_open20_p3bc_check_v0_1_1.py` | DYAD-ART-OPEN20-BINF-CHECKS | ALG | `6cde7ca66cb86101a4ae7b8a41877d49a31ec449563c41bb0d6fc136b6c76d48` |
| `p3a_check.json` | DYAD-ART-OPEN20-BINF-CHECKS | ALG | `1665994e5460a377192a29d3ef7b6efd55491856b7aa5bcd291be7d8fa12ebd1` |
| `p3bc_check_v0_1_1.json` | DYAD-ART-OPEN20-BINF-CHECKS | ALG | `4204cd4f05d889df153744b161709d38db261a9ed14ff112c5bf026f7dfe14e9` |
| `dyad_open21_p5_lambda1_check.py` | DYAD-ART-OPEN21-P5 | NUM/THM | `aca13bf62a6034a11e30190178e3e7a7fad932f26b4114cceb941e530e06e8ae` |
| `dyad_open21_p5_orbit_num.py` | DYAD-ART-OPEN21-P5 | NUM/THM | `e9af1ee1a66287044484aeffe90fb1b2bed1ddf614cefc9dda0c8f049cecc7f5` |
| `dyad_open21_p5_remainder_cert.py` | DYAD-ART-OPEN21-P5 | NUM/THM | `80452d8af9c58bd32f1ffeb587e2b5102cf2c651b05770fc002b58a81837787c`, `80452d8a…787c` |
| `p5_certificate.json` | DYAD-ART-OPEN21-P5 | NUM/THM | `2902ba44f443fbd911f3c6457e769170795384436140cec0bb5709778942bc10` |
| `p5_orbit_num.json` | DYAD-ART-OPEN21-P5 | NUM/THM | `94c0933cfb57e16e96d6b10cdb2ab80e8fe4d2fce3c51aadf3fe40993d5f8297` |
| `dyad_open3_p2_exact_gate.py` | DYAD-ART-OPEN3-P2 | ALG | `89939581d553483de0793b17c6e4b65748291e158e6db218bf1a0c2883b10c50`, `89939581…0c50` |
| `dyad_open3_p5_sq_identity_sanity.py` | DYAD-ART-OPEN3-P2 | ALG | `9ded29aa0484d695abc1d09e0e57312924a456bb52d3381214300b9fda5614d7` |
| `p2_coefficients.json` | DYAD-ART-OPEN3-P2 | ALG | `c24389c94f5d77a674374aabc8cef75f7f5781e821a81d65700e1c2f8151f3dc` |
| `dyad_open3_p3_numeric_check.py` | DYAD-ART-OPEN3-P3 | NUM/THM | `7e91c6b5648b9756cd83de7f4a1222890537c33b273203f4bb679e4b8d8737e3` |
| `dyad_open3_p3_remainder_cert.py` | DYAD-ART-OPEN3-P3 | NUM/THM | `b7df79b0f820f8431e6c2af54a03ef8fd93f869fb06470ed037cdca1126d258d`, `b7df79b0…258d` |
| `p3_certificate.json` | DYAD-ART-OPEN3-P3 | NUM/THM | `bd533725b8c562fae708becdfa6b58ab3601ac5698b1ab00da6afd6493ddfcde` |
| `p3_numeric.json` | DYAD-ART-OPEN3-P3 | NUM/THM | `2e7ee33640c894e3371e26aabc833b2ffd01df2be5072e494a41faead9f414cd` |
| `dyad_open3_p4_exact.py` | DYAD-ART-OPEN3-P4 | NUM/ALG/THM | `199a15bae67db1f30cfce66221822315f44d40f27cbfd74249dceebf96f0b703`, `199a15ba…0703` |
| `dyad_open3_p4_numeric_check.py` | DYAD-ART-OPEN3-P4 | NUM/ALG/THM | `df8badbf128c97930776666e4646c271d55482d6af959288051a8c6204081005` |
| `dyad_open3_p4_offset_cert.py` | DYAD-ART-OPEN3-P4 | NUM/ALG/THM | `4058dfc92d587db75e2a7d68d3c15cddb9d62c6aaaa72b124ab5795f7a8f6b7a`, `4058dfc9…7a8f` |
| `p4_exact.json` | DYAD-ART-OPEN3-P4 | NUM/ALG/THM | `945db486fa87e61b9412b47c5b591d88c7e01e607c4aec4998c898882d6b38d8` |
| `p4_numeric.json` | DYAD-ART-OPEN3-P4 | NUM/ALG/THM | `3c19292da85eefa181924f6c26aec0e04b9d7b8a42278013b5832097ee893a34` |
| `p4_offset_certificate.json` | DYAD-ART-OPEN3-P4 | NUM/ALG/THM | `9b0e0c80f3a7f5f9ddf052ca8bc203e30f79e7d1ad8619555875f3df3e8557b4` |
| `prove_p5_lattice_anomaly_exact.py` | DYAD-ART-P5-LATTICE | ALG | not recorded |
| `normalize_p7_c06_full_cyclotomic_optimized.py` | DYAD-ART-P7-C06 | ALG | not recorded |
| `q4_03_R_identity_certificate.py` | DYAD-ART-Q403-CERT | ALG | not recorded |
| `q4_03_cascade_extract.py` | DYAD-ART-Q403-EXTRACT | ALG | not recorded |
| `DYAD_RETURN_ENCLOSURE_P0_P1_evidence.zip` | DYAD-ART-RE-P0P1 | ALG | not recorded |
| `P2A_v1_certificate_preserved.json` | DYAD-ART-RE-P2B2 | THM | not recorded |
| `rtg_betagraded_vanishing.py` | DYAD-ART-VANISH-BGRADED | ENG/ALG | `dec08174…d774` |
| `degree_b_vanishing_cert_v2.py` | DYAD-ART-VANISH-CERT | ALG | not recorded |
| `certificate.json` | — | — | `d59b0ff68b4341debf5e8a7542bf3865b63dd63e36546952db95298c2bd5c6ce` |
| `coordinate_h_deg6_reconstructed.json` | — | — | `bb09bace…99f6` |
| `normalized_onestep_deg6.json` | — | — | not recorded |
| `normalized_sixstep_deg6.json` | — | — | not recorded |
| `recog_cell_a2_nu3_closed_form_cert.py` | — | — | not recorded |

## Tier 2 — engineering and numerical tools and outputs — 43 files

| File | §8 RID | Grade of the registry entry | Recorded SHA-256 |
|---|---|---|---|
| `step_accumulation_p_general_cli.py` | DYAD-ART-ACCUM-GEN | ENG | not recorded |
| `step_accumulation_p5_p6_cli.py` | DYAD-ART-ACCUM-P56 | ENG | not recorded |
| `build_dyad_p1.py` | DYAD-ART-ATLAS-P1 | ENG | not recorded |
| `check_dyad_p1.py` | DYAD-ART-ATLAS-P1 | ENG | not recorded |
| `dyad_p1_math_checks.py` | DYAD-ART-ATLAS-P1 | ENG | not recorded |
| `build_dyad_v6_4_20_r1.py` | DYAD-ART-ATLAS-P2 | ENG | not recorded |
| `build_dyad_v6_4_20_r2.py` | DYAD-ART-ATLAS-P2 | ENG | not recorded |
| `check_dyad_v6_4_20_r1.py` | DYAD-ART-ATLAS-P2 | ENG | not recorded |
| `check_dyad_v6_4_20_r2.py` | DYAD-ART-ATLAS-P2 | ENG | not recorded |
| `dyad_p2_math_checks.py` | DYAD-ART-ATLAS-P2 | ENG | not recorded |
| `p2_content.py` | DYAD-ART-ATLAS-P2 | ENG | not recorded |
| `p2_source_checks.py` | DYAD-ART-ATLAS-P2 | ENG | not recorded |
| `rtg_b5_step3_Seff.py` | DYAD-ART-B5-SEFF | NUM | not recorded |
| `generate_block_csv.py` | DYAD-ART-BLOCK-CSV | ENG | not recorded |
| `channel_classification_scan.py` | DYAD-ART-CHANNEL-CLASS | ENG/NUM | not recorded |
| `normalize_p_full_onestep_cyclotomic.py` | DYAD-ART-CYCLOTOMIC-P567 | ENG | not recorded |
| `homological_solver_p_general_numeric.py` | DYAD-ART-HOM-GEN | ENG | not recorded |
| `homological_solver_p6_numeric.py` | DYAD-ART-HOM-P6 | ENG | not recorded |
| `phi1_p6_deg5.json` | DYAD-ART-HOM-P6 | ENG | not recorded |
| `normalize_pstep_lie.py` | DYAD-ART-NORM-PSTEP | ENG | not recorded |
| `compare_h_J_with_p2b_v2.py` | DYAD-ART-OPEN3-P0 | NUM/SESSION/ENG | `6e8c7fa75094fe5bd8caa6218c524efb29aa564ea95026392f885829a2f80579` |
| `p0_fit_comparison.json` | DYAD-ART-OPEN3-P0 | NUM/SESSION/ENG | `60687aceba1dee73259c055a79412168eb0f809c2bffd9d53af752a42fa3c73f` |
| `p0_fit_comparison.py` | DYAD-ART-OPEN3-P0 | NUM/SESSION/ENG | `2d5bedaa84a2a98af90f4657e57a45b527b5b5933842e437ca00172e7c422d48` |
| `rtg_p_horizon_audit.py` | DYAD-ART-P-AUDIT | ENG | not recorded |
| `rtg_p_certs.py` | DYAD-ART-P-CERTS | ENG | not recorded |
| `rtg_p_core.py` | DYAD-ART-P-CORE | ENG | not recorded |
| `rtg_p_normalform.py` | DYAD-ART-P-NORMALFORM | NUM/ENG | not recorded |
| `rtg_p_subgroup.py` | DYAD-ART-P-SUBGROUP | ENG | not recorded |
| `dyad_referee_p2b_v2.py` | DYAD-ART-RE-REFEREE | ENG | not recorded |
| `dyad_return_qchi_exact.py` | DYAD-ART-RE-REFEREE | ENG | `e45286fa100b2b31c4d547e8513e23f926b2bda36d31938577fa9f312ca350f6`, `e45286fa…50f6` |
| `DYAD_OWNER_ADOPTION_REVIEW_v1.zip` | DYAD-ART-RE-SUPPL | ENG | `c04096e1cd9ab559d5997c92ad8a442fbf79d350e801e9ed01e6e6a9e19800fe` |
| `check_owner_adoption.py` | DYAD-ART-RE-SUPPL | ENG | `c04096e1cd9ab559d5997c92ad8a442fbf79d350e801e9ed01e6e6a9e19800fe` |
| `spiral_phase_fit.py` | DYAD-ART-SPIRAL-FIT | ENG | not recorded |
| `rtg_invariant_algebraic_engine_surgical.py` | DYAD-ART-SURGICAL | ENG | not recorded |
| `f1_T1_sign_proof.py` | DYAD-ART-T1-SIGN | ENG | not recorded |
| `t1_near_zero_taylor.py` | DYAD-ART-T1-TAYLOR | ENG | not recorded |
| `f1_T2_theta_bound.py` | DYAD-ART-T2-BOUND | ENG | not recorded |
| `degree_b_vanishing_scan.py` | DYAD-ART-VANISH-B234 | NUM/ENG | not recorded |
| `RTG_DYADIC_v6_4_10_INSTALL_MANIFEST.json` | — | — | not recorded |
| `cent.py` | — | — | not recorded |
| `degree_b_vanishing_cert.py` | — | — | `c9a369e6…0dc6`, `dec08174…d774` |
| `rtg_dyad_audit.py` | — | — | not recorded |
| `rtg_ia_cert_fixed.cpp` | DYAD-ART-IA-CERT-FIXED | ENG | not recorded (candidate by content: `upload/dyad-sources/rtg-engine/certify_branch_4_10.cpp`, not identified) |

## Tier 3 — proof, session and source records — 28 files

| File | §8 RID | Grade of the registry entry | Recorded SHA-256 |
|---|---|---|---|
| `DYAD_v6_4_17_v6_4_18_RELEASE_RECORD_ADDENDA_v0_1_1.md` | — (closeout C-2) | — | not recorded |
| `DYAD_ATLAS_P1_SCIENTIFIC_CORRECTION_SESSION_v0_1.md` | DYAD-ART-ATLAS-P1 | ENG | not recorded |
| `DYAD_FC32_HNG_R9FREE_SESSION_v0_1.md` | DYAD-ART-ATLAS-P1 | ENG | not recorded |
| `DYAD_ATLAS_P2_EDITORIAL_INTERFACE_SESSION_v0_1.md` | DYAD-ART-ATLAS-P2 | ENG | not recorded |
| `dyad_triad_antisymmetric_bridge_v1_1.md` | DYAD-ART-BRIDGE-NOTE | ALG | not recorded |
| `DYAD_LEMMA_F_FLAT_CENTRALIZER_PROOF_RECORD_v0_3.md` | DYAD-ART-LEMMA-F-RECORD | SESSION/THM | `2e6c5c59a1fdfe6baa1702df8873b0d89664796d4f317313f239969b406a8ece`, `2e6c5c59…8ece` |
| `DYAD_LPHASE_ROWA_P2B_PROVENANCE_GATE_SESSION_v0_1_1.md` | DYAD-ART-LPHASE-ROWA-RECORDS | SESSION | `5e9f324e444a8c48bc226cd159af0195c84f4f10c3a103d49035c971480a8a7f` |
| `DYAD_NUMGEN_LPHASE_ANGULAR_ENCLOSURE_SCOPE_v0_1.md` | DYAD-ART-LPHASE-ROWA-RECORDS | SESSION | `1eae1d1a204673969ea0a69f0ecd32624a734e9e96a7f855985c360882c01f74` |
| `DYAD_NUMGEN_LPHASE_ROWA_CERTIFICATE_SESSION_v0_1.md` | DYAD-ART-LPHASE-ROWA-RECORDS | SESSION | `775c6715e1a5ba3c020927c1990c1843120cecd3e3b2855be17c959947cf233d` |
| `DYAD_CHECK_degree10_even_term_hatF.md` | DYAD-ART-NF6-DEG10 | ALG | `dcfd808c0270202768b4422acb474cda08f693a1cf69e8ec368e7faac414f4d4`, `dcfd808c…f4d4` |
| `DYAD_OPEN19_FORMAL_CENTRALIZER_PROOF_SESSION.md` | DYAD-ART-OPEN19-SESSION | SESSION | `6749df1126b36453f1f860dd797a872f291fcc7926412225f839acfb2e60e1c6` |
| `DYAD_OPEN20_BINF_EXISTENCE_INTEGRATION_AUDIT_SESSION_v0_1_1.md` | DYAD-ART-OPEN20-BINF-RECORDS | SESSION | `57327922a56aabc409023a780618d9ff46070daa785e4c6355a086cabbe66f4e` |
| `DYAD_OPEN20_P1B_P2_DOMAIN_SESSION_v0_1.md` | DYAD-ART-OPEN20-BINF-RECORDS | SESSION | `0ab4fab0e30c02a8874e6d08d91dff00abe389e528b492435dc0e3409a55820c` |
| `DYAD_OPEN20_P2B_DOMAIN_PROOF_SESSION_v0_2_1.md` | DYAD-ART-OPEN20-BINF-RECORDS | SESSION | `6f275e735897a3f29308de132a416d184b01c2e420fafb83cc012d360033fcf4` |
| `DYAD_OPEN20_P3A_ITERATE_DERIVATIVE_BOUNDS_SESSION_v0_1.md` | DYAD-ART-OPEN20-BINF-RECORDS | SESSION | `b044a41d88c57bfc258469e741d01bd458e9256e2fe4e4ebda92e32b07e9a846` |
| `DYAD_OPEN20_P3BC_FLAT_DERIVATIVES_AND_CK_CONVERGENCE_SESSION_v0_1_1.md` | DYAD-ART-OPEN20-BINF-RECORDS | SESSION | `3ceca25ee64d0b0263da10972ab8e64231545e74e8ad8fc977cd25caeb9e487f` |
| `DYAD_OPEN20_SMOOTH_EMBEDDING_LITERATURE_SCOPE_SESSION_v0_1.md` | DYAD-ART-OPEN20-BINF-RECORDS | SESSION | `3a06222a67d7b895cbcd911db7928a94fc8dc1599d1aa69da1e83e0a2a78c0be` |
| `DYAD_OPEN21_P5_PRIMITIVE_PHASE_PROOF_RECORD_v0_1_2.md` | DYAD-ART-OPEN21-P5-RECORDS | SESSION | `ed7b5f25cc927193351245b05f6175a8511ab3f2da53e5d3cd7a1d98ee10463a` |
| `DYAD_OPEN21_P5_PRIMITIVE_PHASE_SCOPE_SESSION_v0_1.md` | DYAD-ART-OPEN21-P5-RECORDS | SESSION | `a75994fdbc51ff662b9db3937a74d3e0c34773182a61b9431942f6a6ba35cf07` |
| `DYAD_RECOVERED_ARTIFACTS_PROVENANCE_AND_P0_SESSION_v0_1_1.md` | DYAD-ART-OPEN3-P0 | NUM/SESSION/ENG | `233947368e7b865eb401f2aa9f5f9e37b059a7c9df3b8fb315615f5fb85801fe` |
| `DYAD_OPEN3_P4_ASYMPTOTIC_PHASE_PROOF_RECORD_v0_1.md` | DYAD-ART-OPEN3-P4-RECORD | SESSION | `9d781afcc395683379929a93496bcb069f9b1aa14a1de03ff1147bc21fc8cd16` |
| `DYAD_OPEN3_OBSERVABLE_TRANSPORT_SCOPE_SESSION_v0_1_1.md` | DYAD-ART-OPEN3-RECORDS | SESSION | `4526546ad6a99835a9fe2cddd8a6b63d2134ce89d0e9a405e2b601ccf8e6c1ab` |
| `DYAD_OPEN3_P1_P2_SESSION_RECORD_v0_1.md` | DYAD-ART-OPEN3-RECORDS | SESSION | `83248235367c0b38eac670121d209da7bef9d22fd6d5daba8af288a017d91b53` |
| `DYAD_OPEN3_P3_REMAINDER_PROOF_RECORD_v0_1.md` | DYAD-ART-OPEN3-RECORDS | SESSION | `af4a61237a56152101026c70ce461b0ec7bc9fd33e681c215133209e273c2a54` |
| `P2A_v1_PROOF_PRESERVED.md` | DYAD-ART-RE-P2B2 | THM | not recorded |
| `DYAD_RESPONSE_TO_DZT_REQ-002.md` | — | — | `0f8c4b1566e62f0cb97513bc9b9e2b57d9fd712a314f24f66ba8ad7b0a7f7dd3` |
| `OPEN9_arithmetic_horizon_definitions.md` | — | — | `d944ad8ccdbdaaeb79344cf312f6bcff9694159f60c7c8b483f3decd23867c29` |
| `OPEN9_full_onestep_normalization_table_v2.md` | — | — | `af90dc13…700e` |

## Tier 4 — reviews, notices, manifests, relays — 10 files

| File | §8 RID | Grade of the registry entry | Recorded SHA-256 |
|---|---|---|---|
| `NUMGEN_INTERFACE_CONFIRMATION_LPHASE_ROWA_20261020_v0_1.md` | DYAD-ART-LPHASE-ROWA-RECORDS | SESSION | `7a91c223691b3705c2560fca452e671442939452e11cf98820512b182f46f78f` |
| `NUMGEN_RECEIPT_REPLAY_LPHASE_ROWA_20261020_v0_1.md` | DYAD-ART-LPHASE-ROWA-RECORDS | SESSION | `71bfc4c597b4be502129a6d0da0b1c987723979eec1701b9c1b4187140c4b66f` |
| `RTG_RRF_OPEN19_G2_POSTADOPTION_SYNC_REVIEW_v0_2.md` | DYAD-ART-OPEN19-SESSION | SESSION | not recorded |
| `DYAD_v6_4_14_OUTBOUND_NOTICES_N10.md` | DYAD-ART-OPEN3-P4-RECORD | SESSION | `ea120a2658dc28dd85661c71740efb8696457c77827417ec6ee6ae683f91b4c0` |
| `DYAD_OPEN3_P3_REVIEW_DISPOSITION_v0_1.md` | DYAD-ART-OPEN3-RECORDS | SESSION | `6ab21ca55da0127ccd25fc49ae629b21bcb3f1d4a91e0941d80578db5b69db0b` |
| `DYAD_P2A_V2_P2B_V1_REVIEW.md` | DYAD-ART-RE-REVIEWS | — | not recorded |
| `DYAD_P2B_V2_REVIEW.md` | DYAD-ART-RE-REVIEWS | — | not recorded |
| `DYAD_RETURN_ENCLOSURE_P0_P1_REVIEW.md` | DYAD-ART-RE-REVIEWS | — | not recorded |
| `OWNER_ADOPTION_REVIEW_v1.md` | DYAD-ART-RE-REVIEWS | — | not recorded |
| `NG_TO_DYAD_RELAY_RIEMANN_LENS_v1.md` | — | — | not recorded |
