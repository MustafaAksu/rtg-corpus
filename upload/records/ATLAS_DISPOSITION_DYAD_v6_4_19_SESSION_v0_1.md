# ATLAS Disposition — DYAD v6.4.19 — SESSION v0.1

**Date:** 21 October 2026 · **Owner:** Dyadic DSN (Claude) · **Status:** `[SESSION]` owner disposition record. **Not an adoption.** No owner file is modified.
**Authority:** reviewer decision `ADVISORY ACCEPTED FOR OWNER DISPOSITION — SCIENTIFIC CLAIMS REQUIRE INDIVIDUAL REVIEW` (21 Oct 2026). That decision authorizes *preparation* of this record only.
**Boundaries:**
- The ATLAS advisory stays a noncanonical advisory.
- Adopted DYAD v6.4.19 (`40c9e63f…6ec9`) is unchanged by this record. The checker (§9) verifies this.
- No text edit for v6.4.20 starts here. This record fixes the decisions that the later passes implement.
- `ACCEPT` means "the correction is needed and the owner will make it". It does not certify any ATLAS derivation. Owner checks are listed per row with their own tags.

---

## 0. Inspected sources

| Object | Version | SHA-256 | How inspected |
|---|---|---|---|
| DYAD owner file (unchanged) | v6.4.19 adopted | `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9` | Full text; every ATLAS line reference in Tier A re-located |
| ATLAS advisory | FINAL v1.0 | `de371b71960861b92ee0267fb669a427f7febd46115619185cdbca391fba5fb3` | Full text (398 lines) |
| Reviewer assessment | 21 Oct 2026 | `0a5f13f8b8a9aaeb45425cf05d18b9ef41cb68e62230f549d9038a3977686fb5` | Full text |
| RECOG | v0.3.22 adopted | `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` (project copy) | §6.13b A1a cell, §6.14 chart laws, §7 |
| NUMGEN | v1.20.8 | `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e` (project copy) | N3, N10–N15 receipts, L-PHASE sub-item |
| Genesis | v2.8.9 adopted | not hashed here (OFN records `d143673e…c6fc`) | §6.2 OPEN 9 imports, §6.3c, §7, §8 |
| Triadic | v1.6.1 adopted | not hashed here | §7.1 (N2 repin, BRIDGE-LEMMA import) |
| OFN | v0.10 adopted | not hashed here | §5.5.4, IMP-O10-03/04, OPEN-OFN-TRIAD-CLASS |
| RRF | v0.8.4 adopted | not hashed here | §0.2, §2.4b, §6.2a, §6.3 |

"Not hashed here" means the text was read through the project interface and no byte hash was taken in this session. It is not a claim about those files' identities.

---

## 1. Evidence levels used in this record

- `[ALG — owner-run]` / `[NUM — owner-run]`: computed by the owner in this session by `atlas_disposition_math_checks.py` (§9). **Not reviewer-replayed.**
- `[ALG — SESSION, owner draft]`: an owner proof sketch written here. Not a registered result. It needs review before any RID is created.
- `ATLAS-reported`: taken from the advisory and not rechecked by the owner.

---

## 2. Tier A — owner decisions (FA-DYAD-01–08)

**FA-DYAD-01** — Decision: `ACCEPT`
- **Owner basis:** v6.4.19 §7 (L1014) states that the local core "has no upstream scientific DSN imports" and lists RECOG v0.3.20 as context. But T1/T2 (`DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`) and `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` are `[THM — conditional on RECOG-THM-R9-MEMORY]`. R9 is load-bearing. RECOG v0.3.22 §6.13b confirms the chain: Dyadic NF6, PRIM-CTR and NF-REM feed R9; R9 feeds Dyadic T1/T2/OPEN 21; those feed `RECOG-THM-A1A-CD-IDENTIFICATION` and `RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION`. RECOG states that no A1a claim is used to establish R9. The chain is acyclic.
- **Action (P1):**
  - Split §7 into a self-contained foundation (NF6, NF6-OBS, NF-INV, NF-REM, PRIM-CTR, OPEN3 per-block results, L-PHASE row A) and an R9-dependent layer (T1, T2, OPEN 21).
  - Add a claim-level import row for `RECOG-THM-R9-MEMORY`: edition v0.3.22, track C_z, rows (517, 1/400) and (163, 1/1600), not mixed.
  - Name RECOG v0.3.22 §7.3 as the channel for any change to R9.
  - Custody does not move.
- **Validation:** text check. No load-bearing import may be labelled "context".
- **Consumers:** RECOG, NUMGEN.

**FA-DYAD-02** — Decision: `ACCEPT`
- **Owner basis:** confirmed: L259 keeps `(B-∞ existence) [OPEN]` under its CLOSED replacement, and the `---` after L261 renders the paragraph as a heading. The §2 queue still lists closed items. §6.9 still says "until RECOG R11 completes" (R11 is closed). Appendix B L1577 says the universal proof "remains open".
- **Action (P1):**
  - Live entries carry only current status: OPEN 3 CLOSED at its scope; OPEN 19 CLOSED (formal); OPEN 20 PARTIAL (B-∞ existence and flat uniqueness CLOSED; B-an, B-6 OPEN); OPEN 21 CLOSED with the R9 premise; OPEN 9 PARTIAL.
  - Superseded text moves to Appendix A, verbatim.
  - The R11 sentence becomes a permanent transfer guard (SG-19 language).
  - Rebuild the §2 queue from live OPENs only.
- **Validation:** a checker gate in the v6.4.20 draft: no `[OPEN]` tag on a CLOSED item; the set of closures is unchanged (no widening).
- **Consumers:** all.

**FA-DYAD-03** — Decision: `ACCEPT`
- **Owner basis:** confirmed at L408: the §5 row writes the centralizer without the restriction. The owner theorem (§6.16) is Cent_{formal, DG(0)=I}(F) = {exp(s log F) : s ∈ ℝ}. Without DG(0)=I the equality fails: the formal involution R₀ (DR₀(0) = −I) and T itself also commute with F. SG-16 (L358) can be read as forbidding the owner's own certified b=3,4 statements.
- **Action (P1):**
  - Restore DG(0)=I in the §5 row.
  - Rewrite rows that forbid later-established results as "not implied by this result alone; see [RID]". This covers C^∞ commutation and existence (v6.4.13 F1–F3, v6.4.18 E1–E4) and the primitive-variable remainder.
  - Keep the real restrictions: finite S_h ≠ R₀ beyond the 6-jet; analyticity (B-an, B-6); physical exchange; larger domains; E2 only with DX′(0)=0.
  - Rewrite the SG-16 violation clause to forbid exactly two things: ALG use without the registered proof, and use outside p ≥ b+2.
- **Validation:** each §5 row is matched to its theorem's hypotheses in a gate table.
- **Consumers:** RRF, OFN.

**FA-DYAD-04** — Decision: `ACCEPT` (proof audit)
- **Owner basis:** `[ALG — owner-run]` E1: (x+x²)∘(x+x²) = x + 2x² + 2x³ + x⁴. Quadratic–quadratic composition already contributes at degree 3. The general bound is a+b−1. The L638 sentence ("product of ≥2 nonlinear factors, hence degree ≥4") is wrong.
- **Conclusion stands.** VANISH-B2 concerns a fixed degree slot. Its proof needs only that every composition term contributing to that slot is accounted for; the owner's Q403 argument already uses the degree-3 Dq₂·q₂ term.
- **Action (P1):** replace the explanation by the a+b−1 bound. Audit `degree_b_vanishing_cert_v2.py` for the bound it actually enumerates. If the certificate enumerates only terms of degree ≥4, the theorem is re-checked before its tag is kept.
- **Validation:** certificate source inspection and rerun (owner), then reviewer.
- **Consumers:** AZ, DZT.

**FA-DYAD-05** — Decision: `ACCEPT`
- **Owner basis:** confirmed at L457–458 and L601–602: complex values labelled ℚ(√3). L629: the p=5 value is nonreal but labelled ℚ(√5, √(10+2√5)), a real field.
- **Action (P1):** write ℚ(i√3) (or "real and imaginary parts in ℚ(√3)"). For p=5 write ℚ(ζ₅) with the stated embedding ζ₅ = e^{2πi/5}. No value changes.
- **Validation:** a checker gate that every displayed value is unchanged byte-for-byte except the field label.
- **Consumers:** GEN (`DYAD-ALG-NU5-P5` import), RECOG.

**FA-DYAD-06** — Decision: `REVISE`
- **Owner basis:**
  - "p=6 uniqueness" (L525) only states λʲ ≠ 1 for 0<j<6. That holds for every primitive root of unity. Its content is `[ALG]`, not `[THM]`.
  - The three-tier hierarchy (L527–530) has no clock, cutoff or proof.
  - `[NUM — owner-run]` E4: Re μ_p^Z = −p sin²(π/p) for p = 4…50 (max deviation 2·10⁻⁴⁹ at 50 digits). The p=7 value is −1.317786, **not** 1.316 as printed in the advisory.
  - The RECOG ν₃ closed form has a pole at p=3 (denominator λ²+λ+1 = 0). p=3 and p=4 are outside RECOG's all-p cubic scope (p ≥ 5).
  - The comparison of decay across p is frame-dependent (FA-07): in the W_p frame the moduli scale by tan²(π/p).
- **Action (P1):**
  - Retag "uniqueness" as `[ALG]` with its exact content.
  - Split the hierarchy into a `[DEF]` classification and precise statements.
  - A decay statement may cite RECOG's law only for p ≥ 5, in the Z frame, at cubic order, in the declared K_p family, with the frame scale stated. p=3 and p=4 values are not presented as the RECOG import.
  - Harmonic counts are given with a fixed degree cutoff.
  - Record the narrowing as a `[COR]`.
- **Validation:** owner recheck of the RECOG source scope; E4 values in the record.
- **Consumers:** GEN, TRIAD.

**FA-DYAD-07** — Decision: `ACCEPT` (owner verification)
- **Owner basis:**
  - `[ALG — owner-run]` E3 at p=6: 6λ̄n₂₁ = μ; ν₃(ζ₆) = 3n₂₁; 6λ̄ν₃ = 3μ. So μ₆^Z = 3μ₆^W.
  - `[NUM — owner-run]` E5, general p: μ_p^Z / μ_p^{W_p} = cot²(π/p) for p = 5…50 (max deviation 5·10⁻¹³). Examples: 1.894427 (p=5), 3 (p=6), 4.311941 (p=7), 5.828427 = (1+√2)² (p=8), 13.928203 = (2+√3)² (p=12). The ratio is real, consistent with a linear frame change of modulus cot(π/p). **This general rule is `[NUM]` until a proof from the two frame definitions is written.**
  - Confirmed at L671: "pμ_p real parts match −p sin²(π/p)" should read Re μ_p^Z.
- **Action (P1):**
  - Add a frame qualifier to `DYAD-ALG-BRIDGE-LEMMA`: μ_p = pλ̄ν₃^{(1,p)} holds in each frame for that frame's ν₃; the frames differ by the stated factor.
  - Add the interface rule μ^Z = 3μ^W at p=6 (certified).
  - Publish the general-p rule only after a written proof and a check of the normalizer conventions (resonant h = 0 in both).
  - Fix L671.
- **Validation:** written proof of the cot² rule (owner), then reviewer.
- **Consumers:** TRIAD (imports BRIDGE-LEMMA for κ_shear = −2√3/3), RECOG.

**FA-DYAD-08** — Decision: `INVESTIGATE`
- **Owner basis:** `DYAD-THM-RAW-CUBIC` occurs only at L183, as a ticked list item with no statement. A project search found no statement in the owner corpus. The only external mention is AZ v0.6 ("the raw cubic coefficient of the p-step map is exact").
- **Candidate content found by the owner** (`[ALG — SESSION, owner draft]`, with `[NUM — owner-run]` E6):
  - Setting: declared K_p family in the W_p frame; one-step normal form N = h⁻¹fh with resonant h coefficients zero.
  - Claim: for p ≥ 4 the raw p-step map has no quadratic part, and F_raw^p = id + pλ̄ Σ n_{ab} z^a z̄^b + O(4), the sum over resonant cubic slots (a−b−1 ≡ 0 mod p). For p ≥ 5 the only slot is (2,1), so the raw cubic is pλ̄n₂₁ z²z̄. For p = 4 the slot (0,3) is also resonant.
  - Proof sketch: resonant quadratic slots need a−b−1 ∈ {1,−1,−3} ≡ 0 mod p, impossible for p ≥ 4, so N has no quadratic part. N^p = id + pλ̄(resonant cubic) + O(4), because λ^{j(a−b−1)} = 1 on resonant slots and λ^{p−1} = λ̄. Conjugating a tangent-to-identity map with zero quadratic part by h = id + h₂ + h₃ leaves its cubic part unchanged. Hence F^p = hN^ph⁻¹ has the stated cubic.
  - E6 confirms it numerically for p = 4, 5, 6, 7, 8, 12, 24, including the p = 4 (0,3) slot.
- **Missing premise:** the historical proposition (statement, p-range, frame, proof source) that the RID was meant to carry. It is not in the owner corpus.
- **Next test:** (1) the PI is asked for the historical source (v5.x / early v6 sessions); (2) if none is found, the owner proposes the candidate content above as a new statement under the existing RID, with an explicit `[COR]` saying it is a reconstruction, after review; (3) AZ is told the outcome.
- **Do not:** identify it with RECOG's all-p cubic theorem by name.
- **Consumers:** AZ.

---

## 3. Tier B — implementation, external dependency or deferral (FB-DYAD-09–30)

Work families follow the reviewer: science/RID (09–12, 15, 25, 30), interface (13, 14, 18–21, 26), source/evidence (16, 17, 29), readability (22–24, 27, 28). Pass P1 = scientific correction pass; P2 = interface and editorial pass with an old→new section map; P3 = notices after the successor release.

**FB-DYAD-09** — Decision: `ACCEPT`
- **Owner basis:** checked in v6.4.19: none of `DYAD-THM-Q403-PHASE-ALLP`, `-P1`, `-REALITY`, `-LEAD`, `-R`, `DYAD-CF-Q403`, `DYAD-ALG-CASCADE-P12`, `DYAD-ALG-PHASELAW`, `DYAD-ART-CASCADE-Q4-03`, `DYAD-ALG-Q3-CANCEL` occurs (0 matches each). `DYAD-THM-Q403-PHASELAW` occurs 11 times.
- **Action (P2):** a crosswalk table. Each string is classified as exact alias, component of PHASELAW, historical note label, artifact, or unmatched. No automatic alias is created.
- **Consumers:** DZT, AZ (notice N17).

**FB-DYAD-10** — Decision: `ACCEPT`
- **Action (P1/P2):** register result-level RIDs for statements that consumers use: the b=5 all-p theorem (keeping `DYAD-OPEN-B5-ALLP` as the closed lifecycle RID); 𝒜_raw = 47/54 and the 37/40 burst; P₅; the six-step cubic jet and M+Mᵀ = −I; the q=3 cancellation; C₀, Q_c and the ISP maps. No RID is renamed. New RIDs exist only from the successor adoption.
- **Validation:** RID count rises by exactly the new set; the old 136 RIDs are all present.
- **Consumers:** NUMGEN, AZ, DZT.

**FB-DYAD-11** — Decision: `DEFER`
- **Missing premise:** the owner definitions of Q(p), K_extra, Π_extra, the strobe, the reachable basis, Z^miss and the multiplicities, and the statement and proof locator of the "eigenframe linear-part lemma". They are not in v6.4.19 and were not found in the project corpus.
- **Next test:** search the archived OPEN 9 session scripts and v6.2–v6.4.8 records (PI archive). If found, add a versioned appendix. If not, mark the inventory as "symbols without recovered definitions" and do not rebuild them from the atlas.
- **Consumers:** NUMGEN.

**FB-DYAD-12** — Decision: `ACCEPT`
- **Owner basis:** RECOG-THM-A1A-RECIPROCAL-AMPLITUDE (RECOG v0.3.22): |Q_{m+1}⁻¹ − Q_m⁻¹ − 1| < (15/2)√Q_m on U, proved from DYAD-THM-PRIM-CTR alone. Hence 1/Q_m = Q₀⁻¹ + m + O(√m) and Q_m = 1/(m+Q₀⁻¹) + O(m^{−3/2}). A fitted offset κ is subleading and not canonical.
- **Not taken over:** the advisory's reading of the O(√m) term as the P₅ log-spiral with harmonics k = ±1, ±3. It is ATLAS-reported and not checked here.
- **Action (P1):** state m·Q_m → 1 with domain U and its attributed input. Define κ_bb and C as fit parameters of a historical ansatz (SG-7); the 7/54 log fit is "not validated". Keep 47/54, 37/40, 245/216 and the long-orbit behaviour as separate objects.
- **Consumers:** NUMGEN, RECOG.

**FB-DYAD-13** — Decision: `ACCEPT` (scoped corollary)
- **Owner basis** (`[ALG — SESSION, owner draft]`; E10 checks the linear part):
  - By v6.4.18 E3–E4 there is a C^∞ J = T∘K₆⁻¹ with J⁶ = id and DJ(0) = A, and T commutes with K₆, hence with J.
  - Put Φ = ⅙ Σ_{k=0}^{5} A^{−k} J^k. Then DΦ(0) = I. Using J⁶ = id and A⁶ = I, Φ∘J = A∘Φ.
  - So N_Φ = ΦTΦ⁻¹ satisfies A N_Φ A⁻¹ = ΦJTJ⁻¹Φ⁻¹ = N_Φ: it commutes with A.
  - This is the hypothesis of Genesis v2.8.9 §6.3c instance C2 (a real C³ diffeomorphism with Φ(0)=0, DΦ(0)=I and ΦTΦ⁻¹ commuting with A). Instance C2 is therefore not vacuous.
- **Scope kept:** the radius is qualitative; B-an and B-6 stay OPEN; E2 needs DX′(0)=0; this is a mathematical realization, not a physical selection of model, carrier or γ.
- **Action (P1):** register the corollary with a RID after review. **External dependency:** whether Genesis C2 and OFN class C use it is their owners' decision.
- **Consumers:** GEN (N16), OFN (N16), RRF (already records it in v0.8.4 §6.2a), RER/ER-2B through the PI.

**FB-DYAD-14** — Decision: `ACCEPT`
- **Action (P2):** restate I1–I5 as an export table mapped to the NUMGEN v1.20.8 records. Label 403/250 an upper bound. State the domain asymmetry: branch bound on U_T, remainder statement for starts in U. Replace the "still not established anywhere: GAP-LOCK angular inequalities" sentence by a scoped pointer. Whether GAP-LOCK is discharged is NUMGEN's decision.
- **Consumers:** NUMGEN (N18).

**FB-DYAD-15** — Decision: `ACCEPT` (sign); the asymptotic part goes to FC-DYAD-31
- **Owner basis:** `[ALG — owner-run]` E2: −13 + 15√3/2 = −0.0096189…; L214 writes "≈ 0.0096" without the sign.
- **Action (P1):** write the sign; cite DZT-ALG-P12-NORM (norm ¼) as DZT's partial answer, with its finite p ≤ 1000 scope. Keep the DZT/AZ firewalls.
- **Consumers:** DZT (N17).

**FB-DYAD-16** — Decision: `ACCEPT`
- **Action (P2):** one current-edition table (edition, hash, inspection date) replacing the dated "editions inspected" lists. Keep intentional historical pins with their check date. Fix the §7 Genesis row (Genesis pins v6.4.13 since v2.8.8, not v6.4.11).
- **Current editions at this record:** OFN v0.10; RECOG v0.3.22; TRIAD v1.6.1; GEN v2.8.9; NUMGEN v1.20.8; RRF v0.8.4.

**FB-DYAD-17** — Decision: `ACCEPT`
- **Action (P2):** carry out the promises of `DYAD_REPLY_TO_RECOG_G3_v0_1_2.md` §4: separate frozen RECOG v0.3.20 from adopted v0.3.21/v0.3.22; add receipt states; annotate the v6.4.17 and v6.4.18 release records with successor addenda (the records themselves are not edited).
- **Consumers:** RECOG.

**FB-DYAD-18** — Decision: `ACCEPT`
- **Rule:** receipt ≠ statement acceptance ≠ adopted use. One recipient per cell.
- **States verified by the owner in this session:**

| Notice | Recipient | State | Source |
|---|---|---|---|
| N2 | Triadic | ANSWERED (repin to v6.4.13, BRIDGE-EXPORT-CONTRACT, PROTECTION-MATRIX) | TRIAD v1.6.1 §7.1 |
| N3 | NUMGEN | ANSWERED as a citation repair; φ* source still unresolved | NUMGEN v1.20.8 |
| N7 | OFN | to be checked against IMP-O10-03 | OFN v0.10 |
| N9 | OFN | RECEIVED at owner level (IMP-O10-03 imports DYAD-THM-FORMAL-Z6-GENERATOR) | OFN v0.10 §11.4, release notice N-O10-1 |
| N10–N12 | RECOG | RECEIVED; N11 reference only (SG-R14) | RECOG v0.3.22 |
| N13 | RECOG | ADOPTED IN USE (RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION, v6.4.18 pin, source-statement check PASS) | RECOG v0.3.22 §6.13b |
| N10–N13 | NUMGEN | RECEIVED, no use of R9-dependent results | NUMGEN v1.20.8 |
| N14 | RRF | RECEIVED and recorded (B-∞ existence CLOSED) | RRF v0.8.4 §0.2, §2.4b |
| N14 | OFN, FMS | not yet visible (OFN v0.10 predates v6.4.18) | — |
| N15 | NUMGEN | RECEIVED, owner theorem noted, import deferred past v1.20.8 | NUMGEN v1.20.8 |

- **φ\*:** either define it in §4 or remove it from the observable table (P2). `RECOG-THM-A1A-CD-IDENTIFICATION` is only a candidate for NUMGEN/RECOG to compare; no Dyadic RID is created.

**FB-DYAD-19** — Decision: `ACCEPT` (planned, P3)
- See §6. Notices are sent only after the successor release, with its verified hash.

**FB-DYAD-20** — Decision: `ACCEPT`
- **Owner basis:** `GEN-OPEN-UVJET-SCOPE` is present in Genesis v2.8.9 §8; OPEN-GEN-II-7B = `GEN-OPEN-UVJET-ALPHAF`.
- **External dependency:** OPEN-M v0.7.1 R16 / UVM-RESULT-AUDIT1 was not inspected in this session; it is checked before citation.
- **Action (P2):** cite as listed; at 0.024 × 4/3 = 4/125 name the inherited conditions (reduced wrapper, 9C premise, large g, state matching, source normalization). Keep energy ratio, source amplitude and restoring norm separate. Pre-Legacy §1.8 stays historical provenance.
- **Consumers:** GEN, OPEN-M.

**FB-DYAD-21** — Decision: `ACCEPT` (routing only)
- **Action (P3):** send the existing statement S_h = j⁶R₀ (v6.4.19 §§6.15–6.16) with its evidence locator to RECOG and RRF. With v6.4.18 E4 the smooth involution R has the same 6-jet in the matched W frame.
- **Not claimed:** S_h = R as maps; R1's coordinate-action premise met; pole exchange.

**FB-DYAD-22** — Decision: `ACCEPT`
- **Action (P2):** header = current status, adoption, base hash, pointers to release record and manifest. §1 = current state only. History to Appendix A. §6.4 "ontological ground truth" → "reference mathematical model". One footer.

**FB-DYAD-23** — Decision: `ACCEPT`
- **Action (P2):** notation table for J (DT, J_NF, J_ℤ6), U (U_ISP, U, U_T, NUMGEN's tube), h/ĥ/Φ versus h_src, q_NF versus Q_prim, r_rem versus polar r, κ_bb, and lifted versus wrapped W. Archived scripts are mapped, not renamed.

**FB-DYAD-24** — Decision: `ACCEPT`
- **Owner basis:** confirmed: L261 followed by `---` (setext heading).
- **Action (P2):** blank line fix; remove double-escaped LaTeX; unpack mixed grades into canonical tags plus qualifiers (keeping OBS, ALG via IA and THM-ALG via IA); one `[RID: X]` per RID; a lookup of current grades for CAND-prefixed RIDs (RIDs immutable); "breaker primes" → "exceptional orders"; one context marker.

**FB-DYAD-25** — Decision: `ACCEPT`
- **Owner basis:** RECOG-ALG-CHART-LAWS (v0.3.22 §6.14): chart quintic phase coefficient +89√3/324, opposite in sign to the archival c_θ^(6) = −119√3/648. Genesis v2.8.9 §6.2 still quotes −119√3/648 `[conv: Lie strict-kernel gauge]`.
- **Action (P1):** add the chart value and "not a phase-moment or chart input" to the §5 cell. Notify Genesis (N16).

**FB-DYAD-26** — Decision: `ACCEPT`
- **Action (P2):** SG-14 and the export protocol in SG-PROG-2 terms: "conditional on the selected T; not physically primitive, inevitable or universal beyond an explicit selection/universality result (RTG-OPEN-GENERATOR-SELECTION)".

**FB-DYAD-27** — Decision: `ACCEPT`
- **Action (P2):** OPEN 2B as an alias of OPEN 5; qualify or drop OPEN 4b's "historical label OPEN 13"; add "SG-17, SG-18 not assigned".

**FB-DYAD-28** — Decision: `ACCEPT`
- **Action (P2):** fixed-point scope table at first use (§1, §6.1): lifted chart, zero-winding P₁/P₂, wrapped cylinder with (log(1+2πk), 0/π), k ≥ 0; pointers to §6.15 and RECOG.

**FB-DYAD-29** — Decision: `ACCEPT`
- **Action (P2):** claim-to-evidence matrix with columns: scope, written proof, certificate/script, input identity, backend, coverage, OWNER-RUN, REVIEWER-REPLAYED, REVIEWER FULL REPLAY NOT COMPLETED, independent-engine status, remaining gaps. An absent attachment is recorded as absent, not as a refutation.

**FB-DYAD-30** — Decision: `ACCEPT`
- **Owner basis:** `[ALG — owner-run]` E9: R* = e^{π/τ} = λ_DSI^{1/2} and e^{π/(3τ)} = λ_DSI^{1/6}, with λ_DSI = e^{π√3}.
- **Action (P2):** add both to §6.3 with pointers to NUMGEN SG-NG-23 and RECOG SG-R10, keeping their different scope readings.

---

## 4. Tier C — scientific target and missing hypothesis (FC-DYAD-31–34)

**FC-DYAD-31** — Decision: `DEFER`
- **Target:** an `[ALG]` expansion of the PHASELAW closed form Q(L, i) at L = e^{2πi/p}: the limit of |Q_p| (advisory: 1/48) and the 1/p coefficient (advisory numerics suggest π/24).
- **Missing premise:** none beyond DYAD-THM-Q403-PHASELAW. What is missing is the computation.
- **Next test:** exact series of the closed form in 2π/p; compare with DZT's finite p ≤ 1000 audit. Coordinate with DZT before the item is closed; the arithmetic of M_p stays DZT's.
- **Consumers:** DZT.

**FC-DYAD-32** — Decision: `ACCEPT` as first scientific priority (`[ALG — SESSION, owner draft]`; no RID)
- **Target:** H-NG — lim_M (D_M^U − τ log M) exists for every x₀ ∈ U — without R9 and without NUMGEN INF-1.
- **Owner argument:**
  1. *Indexing.* RECOG defines D_M^U = 2πM − (φ̂_{6M} − φ̂_0). DYAD row A gives φ̂_{6(m+1)} − φ̂_{6m} = 2π − τQ_m + r_m for every block m ≥ 0 with base point in U. Hence D_M^U = Σ_{m<M} (τQ_m − r_m) exactly.
  2. *Remainder.* |r_m| ≤ (403/250) Q_m^{3/2}, and Q_m ≤ min(Q₀, 2/m) by PRIM-CTR. So Σ|r_m| < ∞. This part uses DYAD results only.
  3. *Main term.* By RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, 1/Q_m = m + a + E_m with a = 1/Q₀ and |E_m| ≤ (15/2) Σ_{k<m} √Q_k = O(√m). From Q_m ≤ min(Q₀, 2/m), 1/Q_m ≥ (m+a)/3. So Q_m − 1/(m+a) = −E_m Q_m/(m+a) = O(m^{−3/2}), which is summable. Σ_{m<M} 1/(m+a) − log M converges.
  4. Hence D_M^U − τ log M converges. H-NG holds on U.
- **Checks asked for by the reviewer, done here:**
  - *Shared lift:* both use the increasing lift built from principal one-step angles (NUMGEN I1–I5). RECOG's lift alignment (δ_T ∈ (π/6, π/2) on U_T) and DYAD's branch certificate (|δ_T − π/3| ≤ arcsin 0.04654 on U_T) fix the same branch.
  - *Indexing:* block m runs from step 6m to 6(m+1); Q_m = Q(T^{6m}x₀); the sum runs over m = 0…M−1. Both sides match.
  - *Start domain:* both statements use base points in U = {0 < Q ≤ 1/625}.
  - *Acyclicity:* row A depends on NF6, NF-REM row A, PRIM-CTR and OPEN3-SPIRAL-REM. None of these uses R9 or any RECOG A1a result. The reciprocal-amplitude lemma uses PRIM-CTR only.
- **Consequence (not registered here):** with RECOG-THM-A1A-PHASE-EXISTENCE-ALT, Ψ_{W,∞} = Ψ_{z,∞} exists for every x₀ ∈ U, R9-free. This widens RECOG's R9-free existence statement from the existential domain U ∩ U_NUMGEN to all of U.
- **Not supplied:** R9 coefficients, C₂, the value identification C_D^ext, or an R9-free OPEN 21.
- **Missing for registration:** review of steps 1–4; RECOG's decision to register the H-NG discharge (RECOG owns the A1a join); NUMGEN's decision on its own application. DYAD may register only the DYAD-side lemma "Σ|r_m| < ∞ on U" as a corollary of row A.
- **Consumers:** RECOG (N19), NUMGEN (N18).

**FC-DYAD-33** — Decision: `ACCEPT` (candidate corollary, base points only)
- **Owner basis:** `[ALG — owner-run]` E7: on U, √Q_m ≤ 1/25, so |r_m| ≤ (403/6250) Q_m and (τ − 403/6250) Q_m ≤ τQ_m − r_m ≤ (τ + 403/6250) Q_m, with τ − 403/6250 ≈ 1.0902 > 0. The six-step lifted increment is below 2π at every base point in U.
- **Action:** offer to NUMGEN as a corollary scoped to base points (N18). NUMGEN checks anchor indexing, the seven-step crossing and coverage. No tube-wide claim.
- **Consumers:** NUMGEN.

**FC-DYAD-34** — Decision: `ACCEPT` (reference note only)
- **Owner basis:** `[ALG — owner-run]` E8: (κ_shear/κ_recoil)² = (4√3/3)² = 16/3, equal to Genesis's leading ratio (4/3)/(1/4).
- **Action (P2):** optional cross-reference. Bookkeeping only; selects no birth policy.
- **Consumers:** GEN, TRIAD.

---

## 5. Protected set

The successor must keep the following unchanged unless a separately reviewed scientific change addresses them.

**Theorem/RID/status set:**
- All 136 RIDs of v6.4.19, with spelling and grade. CAND-prefixed RIDs stay immutable.
- Grades in force: `DYAD-THM-LPHASE-ROWA-REMAINDER` [THM] at its reviewed scope; `DYAD-THM-SMOOTH-EMBEDDING` E1–E4 [THM]; `DYAD-THM-FORMAL-Z6-GENERATOR`, `DYAD-THM-FORMAL-CENTRALIZER`, `DYAD-THM-FORMAL-INVOLUTION-UNIQUE` [THM, formal]; `DYAD-CAND-FLAT-CENTRALIZER` [THM]; `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` [THM — conditional]; `DYAD-THM-PRIM-CTR`, `DYAD-THM-NF-INV`, `DYAD-THM-NF-REM`, `DYAD-ALG-NF6`, `DYAD-ALG-NF6-OBS`, `DYAD-ALG-NF6-DEG10`; OPEN3 results; `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` [THM — conditional on R9]; `DYAD-THM-Q403-PHASELAW`; `DYAD-THM-C21`.
- OPEN statuses: OPEN 20 PARTIAL (B-an, B-6 OPEN); OPEN 9 PARTIAL; OPEN 19 CLOSED (formal); OPEN 3 CLOSED at its scope; OPEN 21 CLOSED with the R9 premise.
- All scientific constants (403/250, 1/625, 0.04654, C₇ rows, μ, n₂₁, a₃₂, a₀₅, 47/54, 245/216, 89√3/324).

**Scientific boundaries (advisory §3, endorsed):**
- Selected T ≠ physical selection.
- Raw, archival, projected, finite-chart and smooth-chart objects are distinct. Φ does not inherit finite-chart bounds.
- Maps ≠ jets. S_h ≠ R as maps.
- Q_prim ≠ q_NF; rows A and B not mixed; U and U_T explicit; the smooth radius is qualitative.
- Existence ≠ analyticity; E2 only with DX′(0)=0; the route is G_∞^{−n}F^n.
- b=5 does not settle b ≥ 6; Q403 is the p=4s family; DZT's anomaly result is finite-horizon; no OPEN-M deficit is certified.

**Evidence levels:** the three levels of the v6.4.19 release and verification records stay separate. `REVIEWER FULL REPLAY NOT COMPLETED` (combined G14–G15 run; separate-process M1–M4) changes only after new independent runs.

---

## 6. Planned owner notices (P3 — after the successor release only)

Status of every row: **Prepared for PI dispatch after release; not drafted for sending yet.** Each will cite the successor's verified hash.

| Key | Recipient | Content |
|---|---|---|
| N16 | Genesis; OFN | FB-13 smooth chart corollary (C2 hypothesis met at C^∞); FB-25 chart value +89√3/324; FA-05 field label for ν₅^(5) |
| N17 | DZT; AZ | FB-09 crosswalk; FB-15 sign; FA-04 VANISH-B2 explanation; FA-08 outcome |
| N18 | NUMGEN | FB-14 export table; FB-18 φ*; FC-33 lag-sign corollary; FC-32 H-NG argument (for information) |
| N19 | RECOG; RRF | FA-01 R9 import row; FB-21 S_h jet routing; FC-32 H-NG discharge offered for RECOG's decision; FA-07 frame rule |
| N20 | Triadic | FA-07 frame qualifier on DYAD-ALG-BRIDGE-LEMMA (informational; κ_shear unchanged) |

N15 is separate and unchanged: cleared for dispatch, PENDING until NUMGEN's receipt is recorded in a DYAD edition.

---

## 7. Release path

1. This record (v0.1) → reviewer.
2. P1 scientific correction pass: Tier A plus FB-10, 12, 13, 15, 25. New claims marked apart from existing theorem scope.
3. P2 interface and editorial pass on the same base, with an old→new section map.
4. One owner release: draft v6.4.20 → external review → explicit PI adoption → release checker.
5. P3 notices N16–N20.

---

## 8. Summary table (advisory §6, filled)

| Row | Tier | Decision | Pass | Validation | Consumers |
|---|---|---|---|---|---|
| FA-DYAD-01 | A | ACCEPT | P1 | text gate | RECOG, NUMGEN |
| FA-DYAD-02 | A | ACCEPT | P1 | status gate | all |
| FA-DYAD-03 | A | ACCEPT | P1 | hypothesis-mirror gate | RRF, OFN |
| FA-DYAD-04 | A | ACCEPT | P1 | E1; certificate audit | AZ, DZT |
| FA-DYAD-05 | A | ACCEPT | P1 | value-unchanged gate | GEN, RECOG |
| FA-DYAD-06 | A | REVISE | P1 | E4; RECOG scope | GEN, TRIAD |
| FA-DYAD-07 | A | ACCEPT | P1 | E3, E5; written proof | TRIAD, RECOG |
| FA-DYAD-08 | A | INVESTIGATE | P1 | E6; PI source | AZ |
| FB-DYAD-09 | B | ACCEPT | P2 | string census | DZT, AZ |
| FB-DYAD-10 | B | ACCEPT | P1/P2 | RID-count gate | NUMGEN, AZ, DZT |
| FB-DYAD-11 | B | DEFER | — | archive search | NUMGEN |
| FB-DYAD-12 | B | ACCEPT | P1 | source check | NUMGEN, RECOG |
| FB-DYAD-13 | B | ACCEPT | P1 | E10; review | GEN, OFN, RRF, RER, ER-2B |
| FB-DYAD-14 | B | ACCEPT | P2 | table vs NUMGEN | NUMGEN |
| FB-DYAD-15 | B | ACCEPT | P1 | E2 | DZT |
| FB-DYAD-16 | B | ACCEPT | P2 | edition table | all |
| FB-DYAD-17 | B | ACCEPT | P2 | text check | RECOG |
| FB-DYAD-18 | B | ACCEPT | P2 | verified states (§3) | TRIAD, NUMGEN, OFN, RECOG, RRF, FMS |
| FB-DYAD-19 | B | ACCEPT | P3 | after release | GEN, DZT, AZ, NUMGEN, RECOG, RRF |
| FB-DYAD-20 | B | ACCEPT | P2 | OPEN-M source check | GEN, OPEN-M |
| FB-DYAD-21 | B | ACCEPT | P3 | routing | RECOG, RRF |
| FB-DYAD-22 | B | ACCEPT | P2 | editorial | — |
| FB-DYAD-23 | B | ACCEPT | P2 | editorial | NUMGEN, RECOG |
| FB-DYAD-24 | B | ACCEPT | P2 | render/grammar gate | — |
| FB-DYAD-25 | B | ACCEPT | P1 | RECOG source | GEN |
| FB-DYAD-26 | B | ACCEPT | P2 | text | PROG |
| FB-DYAD-27 | B | ACCEPT | P2 | registry gate | — |
| FB-DYAD-28 | B | ACCEPT | P2 | text | RECOG |
| FB-DYAD-29 | B | ACCEPT | P2 | matrix | — |
| FB-DYAD-30 | B | ACCEPT | P2 | E9 | NUMGEN, RECOG |
| FC-DYAD-31 | C | DEFER | — | exact series | DZT |
| FC-DYAD-32 | C | ACCEPT | research | review of steps 1–4 | RECOG, NUMGEN |
| FC-DYAD-33 | C | ACCEPT | research | E7 | NUMGEN |
| FC-DYAD-34 | C | ACCEPT | P2 | E8 | GEN, TRIAD |

Counts: ACCEPT 30, REVISE 1, INVESTIGATE 1, DEFER 2.

---

## 9. Artifacts

| File | SHA-256 | Role |
|---|---|---|
| `atlas_disposition_math_checks.py` | `cccc9e3980a3e5c6daed82db66f30a38c27054d723937fce570f93fbb77a0cb0` | Owner checks E1–E10; controls C1–C3 (each exits 1) |
| `atlas_disposition_math_checks.json` | `77cebd42163fa5fe4abe81645cc5455fb5c065a23e25be45daf8841db1606459` | Output, byte-deterministic (two runs compared) |
| `check_atlas_disposition_v0_1.py` | `ac90b4a81677f14d8b10b36db8f564facc717bc466e2ba040f999f712cbf37cb` | Structural gate D1–D9 for this record; controls K1–K4 (each exits 1) |
| `check_atlas_disposition_v0_1.json`, `controls_exit_codes.json` | in `SHA256SUMS.txt` | Gate output; control exit codes |

The gate reads this record, so its output hash cannot be printed here; it is in `SHA256SUMS.txt`.

`OWNER-RUN` only. Nothing in this package is reviewer-replayed yet.
