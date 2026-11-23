# RER Phase B-03: source and scope reading note for RER-GEN-C04 to C09

**Date:** 20 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase B input for independent receiving review. This is not a record disposition.
- No RER record, grade, contract table or OPEN status is changed.
- Nothing is adopted, frozen or published.

**Inputs:**
- RER v0.2 DRAFT r4.6 (`2fa878ff…4772`), records at lines 279–500.
- Phase A r7 (`2a13e279…a4d3`), `sources_available/` and the source-currency matrix.

## 0. Sources

| Key | Cited by | Bytes | Use here |
|---|---|---|---|
| `ANGLE` (`4f57e538…56e8`) | C04 (§2 lines 37–103, §3 lines 104–144) | **BYTE_VERIFIED_HERE** | Read in full |
| `RANK` (`a1315d4f…fef6`) | C05 (§3 lines 51–103, §4 lines 104–110) | BYTE_VERIFIED_HERE | Read in full |
| `F3` (`a4e95caa…d633`) | C06 (F3-a 19–34, F3-b 35–51), C07 (F3-c 52–66) | BYTE_VERIFIED_HERE | Read in full |
| `REACH` (`9e11a9f3…772c`) | C08 (R1 26–41, R2 42–64, domain 65–72) | BYTE_VERIFIED_HERE | Read in full |
| `AGE` (`fe0da2b3…1392`) | C09 (§1–§4, lines 6–73) | BYTE_VERIFIED_HERE | Read in full |
| `GENMODEL` (`721d9059…3304`) | C07 (§2) | BYTE_VERIFIED_HERE | Read (Phase B-02) |
| `JET` (`15a7d056…2824`) | C09 | BYTE_VERIFIED_HERE | Not used: all jets were re-derived from the model definition |
| `HARM` §3 (lines 56–109) (`7a888515…acd`) | C04 | **MISSING** | Not read |
| `ANGLE_DATA`, `COMMON_ANGLE_JET.json` (`8b558388…3483`) | C04 | **MISSING** | Not read. It holds the general quintic polynomials P₁, P₃; this note checks only their values on the witness orbit |
| `RANKDATA`, `EXACT_RANK_CERTIFICATE.json` (`3daa611c…ac33`) | C05 | **MISSING** | Not read. Its content (the degree-17 coefficient) is reproduced here by two independent routes |

**Source coverage.** Complete for C06, C07, C08 and C09. Incomplete for C04 (HARM, ANGLE_DATA) and C05 (RANKDATA), as the receiver's r6 review stated. The missing files are machine artifacts or a secondary review note; none is the defining model or the only statement of the mathematics.

**Receipt files (not imports).** C07, C08 and C09 carry a "Review receipt" line citing `TRIAD_RER_v0_2_r2_RECORD_REVIEW_20261014.md` (`d388d7eb…1ab`). That file is in the preparer's workspace and its SHA-256 matches. It is not tracked by the Phase A matrix, which covers import lines only; recorded here as an aside.

## 1. Preparer re-derivation (SESSION; exact unless marked [NUM])

All four scripts rebuild the RER §3 model from its definition alone — E, P = (EᵀE)⁻¹Eᵀ, the raw T_e, reprojection after each primitive step, F = N⁶ — with exact rational truncated-polynomial arithmetic (`b03_model.py`, `24570ef0…d21d`). No jet file, source script or source coefficient is read. Each script lists its checks in its docstring and exits 0 only if all pass. Runtimes are given so the receiver can plan a replay; `b03b` and `b03c` have a `--fast` mode.

| Script | SHA-256 | Checks | Runtime |
|---|---|---|---|
| `b03a_c04_check.py` | `6c4b6f5c…581c` | 20/20 | 1.5 s |
| `b03b_c05_check.py` | `9e9aa0d0…b36f` | 9/9 (7/7 with `--fast`) | 37 s (2 s) |
| `b03c_c06_c07_check.py` | `108d1293…8e48` | 15/15 | 26 s (15 s) |
| `b03d_c08_c09_check.py` | `41e7474b…1734` | 8/8 | 4 s |

Outputs: `*_output.txt`; hashes in `b03/SHA256SUMS.txt`. The results are preparer SESSION evidence, not owner certificates and not scientific acceptance.

**Sanity values reproduced on the way:** the linear part of F is the identity, F has no quadratic part, and G₄(1,0,0,0) = (−5/64, −15/64, 0, 0) as GENMODEL §4 states.

## 2. Record-by-record reading

### RER-GEN-C04 — Common-angle jet and fixed-orbit successor separation

| Item | Reading |
|---|---|
| Θ₂ (FINITE_ORDER claim) | Θ₂ = (√3/2Q_s)(s_ρ G₃,s,η − s_η G₃,s,ρ) equals the printed Φ-form and the (a,h,k)-form exactly (A1). On the witness Θ₂ = −√3/3 (A2). |
| Θ₃ harmonics | N₄ on the orbit has only harmonics ±1, ±3: no constant term and no ±5 term. The four printed witness coefficients (65√3/1728, −19/192, −199√3/3456, −863/3456) are reproduced exactly (A2). |
| Readout structure | Φ is invariant under the common proper B-isometry R_θ = L⁻¹Rot(θ)L, and the t⁴ readout term DΦ·G₃ is θ-independent on the orbit, as ANGLE §4's table says (A3). J_Q is L⁻¹Rot(π/2)L and LᵀL = B. |
| Ψ₅ and the embedding (EXACT_LOCAL claim) | Ψ₅(θ) = DΦ·G₄ on the orbit has only harmonics ±1, ±3; the 4×4 matrix M equals the printed one entry by entry; rank M = 3; the kernel direction is the printed v; Im(r q̄³) = 31867336191987863672583168√3 ≠ 0 (A4). The two trigonometric identities of the injectivity proof hold (A5). |
| Steps read, not re-derived | (i) The C¹-stability step: a smooth embedding of a compact circle stays an embedding under C¹-small perturbations, and the O_{C¹}(t⁶) remainder is uniform on the orbit because the expansion is analytic in (t, θ). Standard. (ii) The general polynomials P₁, P₃ of ANGLE_DATA, which this note does not reconstruct. |
| Scope | Correct. The record says this is a reparameterization, not a lower-dimensional factor; the result blocks phase lumping on this orbit and for this observation task only; no physical gauge statement. Matches ANGLE §3 "Precise implication" and §4. |
| Record wording | "five displayed quantities but four independent coordinates" and "Angle O(t⁴); fixed-orbit successor O_C1(t⁶)" match the source. |
| Gaps | HARM §3 and ANGLE_DATA not checked |
| Suggested disposition | `SCOPE_CONSISTENT_WITH_ANGLE; WITNESS_VALUES_INDEPENDENTLY_REDERIVED (preparer); SOURCE_COVERAGE_INCOMPLETE (HARM, ANGLE_DATA)` |

### RER-GEN-C05 — No smaller smooth Q_s-preserving factor near ambient rank-four witnesses

| Item | Reading |
|---|---|
| Degree-17 certificate | Two independent routes agree with the printed value. Route 1 follows RANK §3: the degree-16 determinant vanishes at (1,0,0,1) and the three one-row replacements give 1724491/248832, −337264345/5971968 and 201466337/3981312, summing to 12645889/11943936 (R1). Route 2 composes the exact map through 18 primitive steps, forms the Jacobian of H₃ directly and expands its determinant on the ray: t¹⁶ coefficient 0, t¹⁷ coefficient 12645889/11943936 (R2). The second witness (1,1,1,0) gives −57718145/11943936 (R2). |
| Factor obstruction | The chain-rule argument of RANK §3 is read and is standard: H₃ = H̃₃∘π forces rank DH₃ ≤ dim Y_eff. A nonzero leading coefficient of an analytic function gives rank 4 for all sufficiently small t > 0. |
| F1 witnesses (RANK §2, not in the record) | ½t⁴ for Q_s and −√3/2 t⁴ for Ω_G reproduced with equal inputs (R3). Context only. |
| Grade `[THM]`, `EXACT_LOCAL` | Supported at the declared scope: the conditional model, local near the witness and its three forward iterates, no radius. The rank certificate rests on the exact model jets, now reproduced twice. |
| Scope | Correct. The record keeps the two boundaries of RANK §3 and §5: no exclusion on an invariant restricted manifold, and no physical K₃ statement. The "Joint passive transport" transformation-law line matches RANK §6. |
| Gap | RANKDATA not read; its content is reproduced |
| Suggested disposition | `SCOPE_CONSISTENT_WITH_RANK; CERTIFICATE_INDEPENDENTLY_REDERIVED_TWO_ROUTES (preparer); SOURCE_COVERAGE_INCOMPLETE (RANKDATA)` |

### RER-GEN-C06 — Child-free exact invariant stratum

| Item | Reading |
|---|---|
| Exact invariance | With the untruncated T_e, the child row of N vanishes identically on c = 0 and the parent row is N_s(s) = ⅔(T_e(s) − T_e(−s/2)); F3-a's explicit formula agrees (S1). This is exact, not jet-order. |
| Q increment and determinant | Q(F_s(s)) − Q = Q²/4 + P₅ + O(6) with the printed P₅ (S2); det D(Q, Q∘F_s) = −(Q/64)(r³ + 74er² − 11e²r − 33e³) + O(6), equal to −t⁵/64 at (t,0) (S3). |
| Q not autonomous on M₀ | 5t⁵/32 difference between (t,0) and (−t,0) (S4). |
| Lower bound 2 | Chain rule as in C05 with H₁ = (Q, Q∘F_s): rank 2 near (t,0) forces dimension ≥ 2; the identity chart attains 2. Read; standard. |
| Grade `[THM]`, `EXACT_LOCAL` | Supported at the declared scope |
| Scope | Correct. "Invariant stratum is child-free, not a nonzero-child birth manifold" and the Next-test line keep C07 separate, as F3 does. |
| Gaps | None: both cited sections are byte-verified |
| Suggested disposition | `SCOPE_CONSISTENT_WITH_F3; INDEPENDENTLY_REDERIVED (preparer); SOURCE_COVERAGE_COMPLETE` |

### RER-GEN-C07 — Leading nonzero-child birth graph is not invariant

| Item | Reading |
|---|---|
| Defect | 𝒟_κ(s) = F_c(s,C) − C(F_s(s,C)) has degree-5 part −(√3κ/6)Q²s, obtained both from the jet formula D_cG₃,c(s,0)·C − DC·G₃,s(s,0) and by direct substitution into the degree-7 jet (D2). The degree-6 part is printed in the output for information; the record does not claim it. |
| Structural facts used | G₃,c(s,0) = G₄,c(s,0) = 0 (consistent with C06); parent jets even in c and child jets odd in c through degree 7, from the exchange of the two equal edge roles (D1). |
| Correction stability | Adding any homogeneous degree-5 correction to C leaves the degree-5 and degree-6 parts of the defect unchanged. The degree ≤ 6 defect is linear in the correction, so the 12 monomial directions suffice (D3). This supports the record's "analytic O(|s|⁵) graph corrections do not cancel the stated degree-five defect". |
| Grade `[ALG]`, `EXACT_LOCAL` | Supported |
| Scope | Correct. The record says this does not refute event-time initialization and selects no reset; F3-c says the same, and that Genesis's birth theorem is an admissibility claim, not a post-birth invariance claim. The r4 cross-reference separating this degree-5 F-defect from the degree-4 Ŝ-defect of RER-TRIAD-BIRTH-GRAPH-INVOLUTION is consistent (that record is not reviewed here). |
| Gaps | None |
| Suggested disposition | `SCOPE_CONSISTENT_WITH_F3; INDEPENDENTLY_REDERIVED (preparer); SOURCE_COVERAGE_COMPLETE` |

### RER-GEN-C08 — Natural reachable-state factors fail at birth and across ages 0–1

| Item | Reading |
|---|---|
| R1, age-zero signed Gram | Q_s(F B_κ(t,0)) − Q_s(F B_κ(−t,0)) = 5t⁵/32 + O(t⁶); the t⁵ coefficient is κ-independent, as REACH says (E1). The t⁶ coefficient is 0 and the t⁷ coefficient is 11/60. The delay-map determinant on the birth surface is −t⁵/64 + O(t⁶) at (t,0) (E2). |
| R2, cross-age parent difference | At jet level: 2B(C_κ, R_κ), with B the bilinear form of the c-quadratic part of the cubic parent field, equals κ²Q⁴/18·(−r−2e, 2r−3e) (E3); at (t,0) this is κ²t⁹(−1/18, 1/9), the record's value. The other contributions are O(10) because the parent jets are even in c and the child difference is O(5). [NUM] The full analytic map, with the age-1 state built by Newton inversion so that the current parent is exactly s, reproduces the vector with relative error 0.8–1.1 % at t = 0.005, halving with t, for both reference κ and two directions; a control coefficient 1/17 does not converge (N2, N3). |
| Grade `[ALG]`, `EXACT_LOCAL` | Supported |
| Scope | Correct. "No exclusion of all two-dimensional reachable factors follows" and the memory line match REACH. The age-labelled chart of REACH is described there as a logical upper bound, not a physical proposal; the record does not import it. |
| Gaps | None |
| Suggested disposition | `SCOPE_CONSISTENT_WITH_REACH; INDEPENDENTLY_REDERIVED (preparer, exact + [NUM]); SOURCE_COVERAGE_COMPLETE` |

### RER-GEN-C09 — Fixed finite age sheets separate; parent-only factors fail pairwise

| Item | Reading |
|---|---|
| c_n = C_κ + nR_κ + O_n(6) | [NUM] For n = 1, 2, 3 the current-parent child offset divided by n approaches R_κ(s), relative error 0.4 % at t = 0.005 and halving with t (N1). The jet-level propagation argument of AGE §2 is read, not re-derived. |
| Sheet separation | c_n − c_m has degree-5 part −(n−m)(√3κ/6)Q²s, nonzero for every s ≠ 0 because Q = (r − e/2)² + 3e²/4 is positive definite. Read; immediate from the above. |
| Scalar witness | ΔQ_s = −(n−m)(2κ²/9)Q⁵ + O(11): exact at jet level via (−r−2e, 2r−3e)·∇Q = −4Q (E3); [NUM] confirmed for pairs (1,0), (2,0), (2,1), (3,1), relative error ≤ 1 % at t = 0.005 (N2). |
| Grade `[ALG]`, `EXACT_LOCAL` | Supported |
| Scope | Correct. The record keeps all AGE boundaries: age-pair-dependent neighbourhoods, no uniform radius, countable union not a manifold, no age label or memory inferred, general reachable-only factor NOT_PROPOSED. |
| Gaps | None |
| Suggested disposition | `SCOPE_CONSISTENT_WITH_AGE; INDEPENDENTLY_REDERIVED (preparer, exact + [NUM]); SOURCE_COVERAGE_COMPLETE` |

## 3. Cross-record observations

- **B03-O1, one consistent chain of coefficients.** The same handful of exact numbers recur across the six records and were obtained here from the model alone: 5/32 (pure-parent and birth-surface Q_s asymmetry, C06, C08, and GENMODEL §4), −1/64 (delay-map determinant on M₀ and on the birth surface, C06, C08), −√3κ/6 (graph defect, C07, C08, C09), κ²/18 and −2κ²/9 (cross-age differences, C08, C09). No inconsistency between records was found.
- **B03-O2, grades.** C05 and C06 carry `[THM]`; C04, C07, C08, C09 carry `[ALG]`. The sources label the C05 and C06 results "[THM — conditional exact local result]" and "[ALG/conditional theorem]" respectively. Whether `[THM]` is the right RER grade for results that are theorems about a conditional, noncanonical model is a receiver decision; the mathematics behind both is reproduced here.
- **B03-O3, Evidence lines.** As in B-02, all six records' Evidence lines say no historical certificate was rerun. The present re-derivations are preparer SESSION evidence outside the records; any update of those lines is a later RER edit decision and is not proposed here.
- **B03-O4, the receiver's replay limit.** The B-02 script took 46 s and timed out on the receiving side. The B-03 scripts are 1.5–37 s; `--fast` modes bring the two longer ones to 2 s and 15 s.

## 4. Summary of suggested dispositions (for the receiver)

| Record | Math (preparer SESSION) | Source coverage | Suggested |
|---|---|---|---|
| C04 | witness values and structure reproduced exactly; general P₁, P₃ not reconstructed | incomplete (HARM, ANGLE_DATA) | `SCOPE_CONSISTENT; SOURCE_COVERAGE_INCOMPLETE` |
| C05 | degree-17 certificate reproduced by two routes; second witness too | incomplete (RANKDATA, content reproduced) | `SCOPE_CONSISTENT; SOURCE_COVERAGE_INCOMPLETE` |
| C06 | exact invariance and all coefficients reproduced | complete | `SCOPE_CONSISTENT; SOURCE_COVERAGE_COMPLETE` |
| C07 | defect reproduced two ways; correction stability proved for degree 5 | complete | `SCOPE_CONSISTENT; SOURCE_COVERAGE_COMPLETE` |
| C08 | R1 exact; R2 exact at jet level and [NUM] on the full map | complete | `SCOPE_CONSISTENT; SOURCE_COVERAGE_COMPLETE` |
| C09 | scalar witness exact at jet level; propagation and separation [NUM] + read | complete | `SCOPE_CONSISTENT; SOURCE_COVERAGE_COMPLETE` |

## 5. Not in this note

- No reading of HARM, ANGLE_DATA or RANKDATA.
- No disposition is made; the receiver decides.
- The remaining Phase B records: TRIAD-FORMAL-AGE, TRIAD-AGE-CURVATURE, TRIAD-REGULAR-3FOLD, RRF-CND01 (deep review); F3-N7N8, GEN-K3-MODAL, DYAD-FORMAL-INVOLUTION (claim level); the two Triadic involution records, which stay with the receiver; the two blocked ER-2B records.
- G2 §5b carrier identification stays pending.
