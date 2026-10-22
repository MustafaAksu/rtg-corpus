# Atlas Advisory — Dyadic Oscillator DSN v6.4.19 — FINAL PROPOSAL v1.0

**To:** the Dyadic stream owners and reviewers.
**From:** the atlas owner (Claude), consolidating two independent advisory passes over the same source and the same atlas basis:
- **[C]** `ATLAS_ADVISORY_NOTE_DYAD_v6_4_19_v0_1.md` (Claude, 33 rows);
- **[G]** `RTG_ATLAS_ADVISORY_DYADIC_v0_1.md` (ChatGPT, 28 rows, with an 11-check algebra script and a disposition CSV).

**Date:** 21 October 2026.
**Source under review:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.19` (adopted 20 Oct 2026). Both passes read it in full: 1,592 lines, 275,935 bytes, SHA-256 `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9` per [G].
**Atlas basis:** `RTG_STATE_ATLAS_v0_1.md`, SHA-256 `88353763…78cc6` per [G].
**Status:** noncanonical advisory. It is not an amendment, adoption, regrade or notice. The Dyadic DSN is unchanged. The owner decides every row.

This document supersedes both v0.1 notes as the version to act on. Neither earlier note is edited; both stay in the project as working records.

---

## 0. How the two passes were reconciled

- **Overlap.** Both passes found 17 issues independently. Each appears below once, with both source IDs listed.
- **Unique findings.** [C] contributed 12 findings and [G] 11. The atlas owner re-checked every unique [G] finding against the DSN text (line numbers below are for v6.4.19), and all of them hold. Where [G] corrects an atlas reading, the correction is adopted (§5).
- **Disagreements.** There were two, both now settled:
  - On the deferral standard, [G]'s stricter rule is adopted. A deferral must name a missing premise or a next test; "noted for a future release" on its own is not enough.
  - The S12/H12 link ($S_h$ as the 6-jet of $R_0$) is recorded as already present in DYAD, not as a new link (§5).
- **Priority tiers.** **A** = resolve in this owner pass. **B** = implement in the same release unless a named external dependency blocks it. **C** = scientific opportunity, which may be deferred with a target and its missing premise.
  - These are not Programme OPEN-P0/P1/P2.
  - Types: S = scientific, I = interface or identifier, Y = synchronization, E = editorial, F = formatting.
- **Row IDs.** `FA-DYAD-nn` IDs are tracking keys only; they are not proposed RIDs.
- **Atlas-derived links.** Rows marked `~` rest on links the atlas derived itself. Verify before use.

---

## 1. Requested outcome and release contract

1. **One substantive successor release.** The Dyadic team produces one owner-adopted successor through its normal draft → review → adoption cycle. The team chooses the version number; v6.4.20 is used here only as an example.
   - Every Tier A row is implemented or carries an explicit owner disposition.
   - Tier B rows are implemented unless a named dependency blocks them.
   - Tier C rows may be deferred.
2. **Disposition per row.** For every row, record: accept / reject / defer, a reason, the edited section or RID (or the evidence locator), and the consumers affected.
   - A **reject** needs a reason.
   - An **accept** needs the location of the edit and how it was validated.
   - A **defer** needs the missing premise or the next concrete test.
3. **Successor diff.** Provide the diff from v6.4.19, together with separated validation:
   - Structural checks: rendering, anchors, a single context marker, RID preservation, imports that resolve.
   - Scientific checks: changed hypotheses, frames, domains and dependency direction.
   - Editorial moves must preserve every formula and stay recoverable through an old-to-new map.
4. **Notices after release.** Send consumer notices only after the release identity (its hash) is fixed. In every notice, keep three fields separate: received, statement accepted, and adopted in use.
5. **Atlas refresh.** The atlas is refreshed from the adopted successor, never from this note. A later pass checks the actual diff against this table.

---

## 2. Findings register

### 2.1 Tier A — resolve in this owner pass

**FA-DYAD-01 | S | §7 dependency description is wrong [G AD-05]**
- **Location:** §7 L1014–1019, where the core is described as having "no upstream scientific DSN imports" and the RECOG imports are said to "feed OPEN 9/OPEN 12 status and cross-references only". Also §6.14 T1/T2 and DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER.
- **Problem:** T1 and the chart-variable memory law are `[THM — conditional on RECOG-THM-R9-MEMORY]`, and OPEN 21 rests on them. So R9 is a load-bearing import, not context.
- **Action:**
  - Separate the self-contained foundation (NF6, NF6-OBS, PRIM-CTR, NF-INV, NF-REM, OPEN3 per-block, L-PHASE row A) from the R9-dependent results.
  - Add claim-level import rows with edition, RID, track, rows and domain.
  - Record the dependency chain DYAD bounds → RECOG R9 → DYAD T1/T2/OPEN 21 → RECOG A1a (RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION, v0.3.22). The chain has no cycle.
  - Acknowledge RECOG v0.3.22 §7.3 (the pre-release notification register) as the channel for any change to R9.
  - Ownership does not move.
- **Accept when:** no load-bearing import is labelled as context.

**FA-DYAD-02 | E/S | One status per module across §§1–3, §5 and the result bodies [C E2, E3; G AD-02]**
- **Problems:**
  - "Retained as history" text sits inside live entries:
    - OPEN 3, L139–144;
    - OPEN 20 B-∞ existence: L259 still reads `[OPEN]` directly under its CLOSED replacement;
    - the §6.14 "Not established" blocks at L805, L832 and L844;
    - §6.17 L996;
    - §6.15 L927;
    - the DYAD-ART-SPIRAL-FIT note.
  - The §2 priority queue still lists items 0, 1, 4 and 4b, which are closed or completed.
  - §6.9 L614 still says "until RECOG R11 completes", although R11 is closed.
  - Appendix B L1577 says the "universal proof remains open", although VANISH-B4 is `[ALG]`.
- **Action:**
  - Keep current status only in live entries: OPEN 3 CLOSED at its scope; OPEN 19 CLOSED (formal); OPEN 20 PARTIAL, with B-∞ existence and flat uniqueness CLOSED and B-an/B-6 OPEN; OPEN 21 CLOSED with the R9 premise; OPEN 9 PARTIAL without Q403 or b=5.
  - Move superseded text to Appendix A.
  - Turn the old R11 sentence into a permanent transfer guard.
  - Rebuild the queue from live OPENs: OPEN 20 B-an/B-6, the L-PHASE row-B constant, the rest of OPEN 9, and OPEN 2A, 2B, 4, 5, 6, 16.
- **Accept when:** no live `[OPEN]` tag sits on a closed item, and no closure is widened.

**FA-DYAD-03 | S | High-risk table summaries must mirror their theorem hypotheses [G AD-04, AD-03]**
- **Problems:**
  - §5 L408 writes Cent(T⁶)={exp(sX)} without the DG=I restriction.
  - Several rows forbid things that later results establish (C^∞ exact commutation and existence; the primitive-variable remainder).
  - SG-16's violation clause, L358, can be read as forbidding the owner's own certified b=3,4 statements.
- **Action:**
  - Restore Cent_{formal, DG=I}(F).
  - Rewrite those warnings as "not implied by this result alone; see [later RID]".
  - Keep the genuine restrictions: the finite $S_h$, analyticity, physical exchange, larger domains, and E2's DX′(0)=0.
  - Rewrite SG-16 to forbid exactly two things: ALG without the registered proof, and use outside p≥b+2.

**FA-DYAD-04 | S | Repair the explanation of VANISH-B2 [G AD-09]**
- **Problem:** L638 says a cross-term is "a product of ≥2 nonlinear factors…, hence degree ≥4". Under composition, quadratic–quadratic terms already appear at degree 3: (x+x²)∘(x+x²)=x+2x²+2x³+x⁴ (checked as [G] A01). The Q403 proof itself uses this degree-3 Dq₂·q₂ term.
- **Action:** Use the composition bound a+b−1≥3. The conclusion stands, so the theorem is not withdrawn. Check whether the certificate already uses the correct bound.

**FA-DYAD-05 | S | Coefficient-field labels [G AD-08]**
- **Problem:** h₂ (L457–458) and the complex raw coefficients (L601–602) are labelled "in ℚ(√3)", a real field, but the values are complex and lie in ℚ(i√3). The p=5 value at L629 is labelled ℚ(√5, √(10+2√5)), which is real, yet the value is nonreal.
- **Action:** Write ℚ(i√3) (or "components in ℚ(√3)"). For p=5 write ℚ(ζ₅) with the stated embedding. No value changes.

**FA-DYAD-06 | S | The resonance summaries in §6.6 are tagged [THM] [C S4; G AD-10]**
- **Problem:** "p=6 uniqueness" (L525) only states λ^j≠1, which holds for every primitive root. The three-tier hierarchy (L527–530) asserts "faster decay" and "more harmonics" with no clock, no cutoff and no proof.
- **Action:**
  - Retag "uniqueness" as [ALG] with its exact content.
  - Split the hierarchy into a [DEF] classification plus precise statements.
  - `~` [C] offers one precise form of "faster decay" from the imported RECOG law Re μ_p^Z=−p sin²(π/p). Its modulus is 2.25, 2, 1.727, 1.5, 1.316 for p=3…7, decreasing toward π²/p. This holds in the declared K_p family, Z-frame, at cubic order, and the frame scale must be stated.
  - Harmonic counts need a fixed degree cutoff.
  - Record any narrowing explicitly (as a COR).

**FA-DYAD-07 | S/I | Frame typing of the bridge lemma [C S6; G AD-07]**
- **Problem:** μ_p=pλ̄ν₃^(1,p) is used in both the W_p and the Z frame. Only §6.11 records the factor 3. [G] verified W=i√3 Z, μ₆^Z=3μ₆^W and ν₃^Z=3n₂₁ at p=6 (checks A02–A04). TRIAD imports BRIDGE-LEMMA for κ_shear. In addition, L671 reads "pμ_p real parts match −p sin²(π/p)", which looks like a typo for μ_p^Z.
- **Action:** Add a frame qualifier to the RID statement and a conversion rule at the interface. Publish a general-p rule only after checking the normalizer conventions. Fix L671.

**FA-DYAD-08 | I | DYAD-THM-RAW-CUBIC has no statement [C S2; G AD-11]**
- **Problem:** The RID appears once in the file, as a ticked item in the OPEN 9 list. AZ imports it.
- **Action:**
  - Recover the proposition, range, frame and proof source.
  - If it is an alias, record the owner-approved mapping.
  - If neither is possible, disclose the gap.
  - Do not identify it with RECOG's all-p theorem on the strength of its name.

### 2.2 Tier B — implement in the same release

**FB-DYAD-09 | I | Crosswalk of identifiers used by DZT and AZ [C S2; G AD-13]**
- **Problem:** Consumers cite strings that do not resolve in v6.4.19:
  - DZT: DYAD-THM-Q403-PHASE-ALLP, -P1, -REALITY, -LEAD, -R, DYAD-CF-Q403, DYAD-ALG-CASCADE-P12, DYAD-ALG-PHASELAW, DYAD-ART-CASCADE-Q4-03.
  - AZ: DYAD-ALG-Q3-CANCEL.
- **Action:** Classify each string as one of: exact alias, component of PHASELAW (the four supporting links λ^{−s}=−i, reality, S₋₄=0, relation (R) are given only in prose), historical external-note label, artifact, or unmatched. Send the result to DZT and AZ. No automatic aliases.

**FB-DYAD-10 | I | Result-level RIDs for statements consumers use [C S2, E9; G AD-14]**
- **Problem:** The b=5 all-p theorem is cited only through the OPEN-type DYAD-OPEN-B5-ALLP. Several statements have no RID at all:
  - 𝒜_raw 47/54 and the 37/40 burst;
  - P₅ (NUMGEN's L1 degree-5 term equals P₅ exactly; atlas sympy PASS);
  - the six-step cubic jet and M+Mᵀ=−I;
  - the q=3 cancellation;
  - the critical curve C₀, Q_c, and the ISP maps.
- **Action:** Register RIDs for the consumed statements first. Keep DYAD-OPEN-B5-ALLP as the closed lifecycle RID. Do not rename anything.

**FB-DYAD-11 | I | Definitions behind the OPEN 9 projector inventory [G AD-12]**
- **Problem:** L648–650 is a list of symbols, and the "eigenframe linear-part lemma" has a role but no statement.
- **Action:** Recover the owner definitions (Q(p), K_extra, Π_extra, the strobe, the reachable basis, Z^miss, the multiplicities) and the lemma's statement and proof locator. A versioned appendix is acceptable. Do not rebuild them from the atlas.

**FB-DYAD-12 | S | Separate the certified leading decay from the fitted backbone offset [C S3; G AD-17]**
- **Problem:** §6.5 tags "Q_m∼1/(m+κ), Q_n∼6/(n+C)" as `[ALG]`, while §1 calls the same law a historical fitted surrogate.
- **Reading shared by both passes:** 1/Q_m = Q₀⁻¹+m+O(√m), using RECOG-THM-A1A-RECIPROCAL-AMPLITUDE together with PRIM-CTR. The O(√m) term is the log-spiral of P₅, with harmonics k=±1, ±3, and agrees with the adopted m^{−3/2} spiral amplitude of §6.14. Hence Q_m = 1/(m+Q₀⁻¹)+O(m^{−3/2}), so an O(1/m²) offset κ is subleading and not canonical.
- **Action:**
  - State m·Q_m→1 (or the sharper form above) with its domain and its attributed input.
  - Define κ and C as fit parameters (historical ansatz, SG-7), with the 7/54 log fit marked as not validated.
  - Keep 47/54, 37/40, 245/216 and the long-orbit behaviour as distinct objects.
  - Rename κ to κ_bb.

**FB-DYAD-13 | S/I | Export the smooth equivariant chart to the class-C consumers [C S8; G AD-20]**
- **Content:** SMOOTH-EMBEDDING E4 with F3 gives a C^∞ J. Then Φ=⅙Σ_{k=0}^{5}A^{−k}J^k satisfies DΦ(0)=I, ΦJ=AΦ, and [ΦTΦ⁻¹, A]=0. This is exactly the hypothesis of GEN §6.3c instance C2. RRF v0.8.4 §6.2a already records it. GEN v2.8.9 and OFN v0.10 §5.5.4 predate it. N14 did not go to Genesis.
- **Action:**
  - Issue an owner-endorsed corollary or interface statement; a RID for it is recommended.
  - Notify Genesis, and RER/ER-2B through the PI.
  - Keep open: B-an/B-6, the qualitative radius, E2's DX′(0)=0, and the line between mathematical realization and physical selection.

**FB-DYAD-14 | I | L-PHASE export contract and the GAP-LOCK pointer [C S5; G AD-22, AD-24 part]**
- **Problem:** The L860–891 sentence "Still not established anywhere: quantitative GAP-LOCK angular inequalities" is out of date in substance. NUMGEN v1.20.8 has now allocated its lift, defect and N5AS1 RIDs.
- **Action:**
  - Restate I1–I5 as an export table mapped to the NUMGEN records.
  - Label 403/250 as an upper bound.
  - State the domain asymmetry explicitly: the branch bound holds on U_T, the remainder statement only for starts in U.
  - Replace the stale sentence with a scoped pointer to what is supplied: explicit L-MONO/L-PHASE (this RID) and explicit L-BACKBONE (RECOG A1a). Whether GAP-LOCK is discharged remains NUMGEN's decision.

**FB-DYAD-15 | S/I | The near-cancellation item: sign, DZT feedback and a re-scope [C S1; G AD-25]**
- **Problem:** L214 writes "≈ 0.0096". The value is Q₁₂=−0.0096189…; its modulus is 0.0096.
- **Partial answer already held by DZT:** DZT-ALG-P12-NORM gives N(−13+15√3/2)=¼, with conjugate ≈−25.99. DZT's p≤1000 anomaly audit has finite scope.
- `~` **Atlas observation [C]:** the PHASELAW closed form gives |Q_p| = 0.00962, 0.01284, 0.01453, 0.01560, 0.01768 for p=12, 16, 20, 24, 40. Its L→1 limit is i/48. Numerically |Q_p| ≈ 1/48 − 0.1309/p at p=10², 10³, 10⁴, which matches π/24. So p=12 is the first member of a smooth family, not an isolated cancellation.
- **Action:**
  - Write the sign and cite DZT.
  - Then either close the item through an exact expansion of the closed form in 2π/p (Tier C, task FC-DYAD-31), or restate it as "arithmetic of M_p" and route that part to DZT.
  - Keep the DZT/AZ firewalls.

**FB-DYAD-16 | Y | Edition pins and the consumer table [C P1; G AD-18 part]**
- **Problem:** The named editions trail the current ones:

  | Document | Named in DYAD | Current |
  |---|---|---|
  | OFN | v0.9 | v0.10 |
  | RECOG | v0.3.20 ("freeze candidate") | v0.3.20 frozen; v0.3.21 and v0.3.22 adopted |
  | TRIAD | v1.6 | v1.6.1 |
  | GEN | v2.8.7/8 | v2.8.9 |
  | NUMGEN | v1.20.7 | v1.20.8 |
  | RRF | v0.8/0.8.3 | v0.8.4 |

  The §7 Genesis row also says "pins v6.4.11", while N8 and GEN v2.8.9 show v6.4.13.
- **Action:**
  - Replace the dated "editions inspected" lists with one current table (edition, hash, inspection date).
  - Keep intentional historical pins, with the date of the check ([G] caution: an old pin is not automatically an error).
  - Fix the Genesis row.

**FB-DYAD-17 | Y | Carry out the promised RECOG corrections [C P2]**
- **Problem:** `DYAD_REPLY_TO_RECOG_G3_v0_1_2.md` §4 promised, for the next revision:
  - distinguishing frozen v0.3.20 (`fdb8c9a7…bdf`, G1 `5c00f66d…9b55`) from adopted v0.3.21;
  - adding the receipt states;
  - annotating the v6.4.17 and v6.4.18 release records.

  v6.4.19 did not do this.
- **Action:** Do it in this release.

**FB-DYAD-18 | Y | Notice states, one recipient per cell [C P3; G AD-18, AD-28]**
- **N2 Triadic:** ANSWERED (TRIAD v1.6.1 §7.1).
- **N3:** ANSWERED as a citation repair (NUMGEN v1.20.8 §9.1). The φ* statement stays an orphan, source unresolved.
  - No Dyadic RID is created.
  - `~` RECOG-THM-A1A-CD-IDENTIFICATION is a candidate for NUMGEN/RECOG to evaluate; it needs a separate comparison proof.
  - Either define φ* in §4 or remove it from the observable table.
- **N7, N9 OFN:** OFN v0.10 IMP-O10-03 imports DYAD-THM-FORMAL-Z6-GENERATOR (resting on Theorem C). Record N9 as received at owner level, and check N7 against the same import.
- **N10–N13 RECOG:** RECEIVED.
  - N11: reference use only (SG-R14).
  - N13: adopted use in RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION. Inspect that use before closing the row.
  - NUMGEN: received, no use of the R9-dependent results.
- **N14:** RRF recorded. FMS and OFN to be checked.
- **N15:** NUMGEN received, not imported.
- **Rule:** receipt ≠ statement acceptance ≠ adopted use.

**FB-DYAD-19 | Y | New outbound notices, sent after release (proposed N16–N19) [C P5]**
- **To Genesis:** FB-13 (C2) and FB-25 (c_θ chart value).
- **To DZT and AZ:** FB-09 and FB-15.
- **To NUMGEN:** FB-14 and FB-18 (φ*).
- **To RECOG and RRF:** FB-21 (informational).

**FB-DYAD-20 | S/I | Citations for the UV threshold chain [C S11; G AD-26]**
- **Already correct:** SG-15 states that there is no certified deficit.
- **Action:**
  - Cite GEN-OPEN-UVJET-SCOPE for the 0.024 target, with OPEN-GEN-II-7B (= GEN-OPEN-UVJET-ALPHAF) as an alias.
  - Cite OPEN-M v0.7.1 R16 / UVM-RESULT-AUDIT1 for the current status of the ×2/×4 question.
  - Keep Pre-Legacy §1.8 as historical provenance only.
  - At the 0.024×4/3=4/125 conversion, name the inherited conditions: reduced wrapper, 9C, large g, state matching, source normalization.
  - Keep energy ratio, source amplitude and restoring norm separate.

**FB-DYAD-21 | I | Route the existing S_h = j⁶R₀ statement [C S12; G AD-21]**
- **Status:** already in DYAD (§6.15 L918; §6.16 L978).
- **Action:** Send it, with its evidence locator, to RECOG and RRF. With E4, the smooth involution R has the same 6-jet in the matched W frame.
- **Do not claim:** $S_h$ = R as maps, or that R1's coordinate-action premise is met, or pole exchange.

**FB-DYAD-22 | E | Current orientation in the header and §1 [C E1; G AD-01]**
- **Problem:** L1–30 carry about 20k characters of review verdicts, evidence tables, hashes and per-version summaries. §6.4 L481 says "ontological ground truth".
- **Action:**
  - Header: current status, adoption, base hash, and pointers to the release record and manifest.
  - §1: current state only, aiming at the Methodology's orientation size or with a declared exception.
  - Move the history to Appendix A.
  - In §6.4, use "reference mathematical model".
  - Keep only the current footer (seven are stacked now) [C E7].

**FB-DYAD-23 | E/F | Notation dictionary and symbol collisions [C E11; G AD-06]**
- **J:** DT (Jacobian), J_NF (the jet; Arg(J/z) in L-PHASE resolves to J_NF), J_ℤ6.
- **U:** U_ISP=(√3/2)ρ (§6.4); U_DYAD, U_T,DYAD (tube) versus NUMGEN's existential tube.
- **h:** h₆, ĥ (formal) and Φ (smooth chart), versus h_src (OPEN-M amplitude, SG-15).
- **Other overloads:** q_NF versus Q_prim; r_rem versus polar r; κ_bb; and G, M overloads.
- **W:** state lifted or wrapped.
- **Action:** Add a short notation table. Map archived scripts explicitly rather than renaming them.

**FB-DYAD-24 | F | Grammar, rendering and anchors [C E8, F1–F4, E10; G AD-15]**
- **F2 (rendering bug):** L261 is followed directly by `---`, which turns the paragraph into a setext H2. Insert a blank line.
- **F1:** double-escaped LaTeX (`\\rm`, `\\ge`, …) in §8 L1130–1131 and in Appendix A v6.2–v6.4.8.
- **Grades:** unpack mixed grades such as `[ALG / ENG]`, `[ALG structure / NUM strong]`, `[THM/ALG]`, `[CAND/conditional]`, `[THM — analytic]`, `[ALG, exact]`, `[ALG finite sweep]` into canonical tags plus qualifiers. Keep OBS, ALG via IA and THM-ALG via IA, which are canonical.
- **RIDs:** CAND-prefixed RIDs stay immutable. Add a lookup of current grades.
- **Tagging:** use one `[RID: X]` per RID (this is a precondition for the atlas Pass 3 gate).
- **Wording:** "breaker primes" should read "exceptional orders", because the lists contain 4.
- **Structure:** one context marker. Recheck the orientation core after FB-22.

**FB-DYAD-25 | S/E | The c_θ^(6) high-risk cell [C S7]**
- **Action:** Add the chart value +89√3/324 (RECOG-ALG-CHART-LAWS) and "not a phase-moment or chart input" to the §5 forbidden-overclaim cell. Notify Genesis, which still uses the archival −119√3/648.

**FB-DYAD-26 | S/E | SG-14 and the export protocol in SG-PROG-2 terms [C S10]**
- **Problem:** "Until OPEN-P0 is resolved" predates Programme v1.2 (PROG12-C04/C05).
- **Action:** Rewrite as "conditional on the selected T; not physically primitive, inevitable or universal beyond an explicit selection/universality result (RTG-OPEN-GENERATOR-SELECTION)".

**FB-DYAD-27 | E | OPEN registry hygiene [C E5, E6]**
- OPEN 2B is "equivalent to OPEN 5". Make it an alias or merge the two.
- OPEN 4b's "historical label OPEN 13" collides with the archived OPEN 13. Qualify or drop the label.
- Add one line: "SG-17, SG-18 not assigned".

**FB-DYAD-28 | E | Fixed-point scope at first use [G AD-16]**
- **Action:** At §1 L51 and §6.1, add a short scope table: lifted chart, the zero-winding representatives P₁/P₂, and the wrapped cylinder with its additional fixed points (log(1+2πk), 0/π), k≥0, which are already in §6.15. Point to the §6.15 proof and to the RECOG inventory.

**FB-DYAD-29 | Y | Claim-to-evidence matrix [G AD-19]**
- **Action:** One table covering, for each claim: scope, written proof, certificate or script, input identity, backend, coverage, owner run, reviewer run, independent-engine status and remaining gaps. Bound the meaning of "reviewer full replay pending". An absent attachment is not a refutation.

**FB-DYAD-30 | E | Constant identities [C E12]**
- `~` R* = e^{π/τ} = λ_DSI^{1/2}.
- The NUMGEN and RECOG clock ratio e^{π/(3τ)} = λ_DSI^{1/6}; NUMGEN SG-NG-23 and RECOG SG-R10 give it different scope readings.
- **Action:** Add both to §6.3 with pointers to the consumers.

### 2.3 Tier C — scientific opportunities (deferral allowed with target and missing premise)

**FC-DYAD-31 | S | Exact large-p behaviour of the q=4,(0,3) cascade [C S1]**
- `~` **Target:** an [ALG] expansion of Q(L,I), I=i, at L=e^{2πi/p}, giving |Q_p| → 1/48 and the 1/p coefficient (the numerical value suggests π/24). Monotonicity in p is optional.
- **Premise:** only DYAD-THM-Q403-PHASELAW.

**FC-DYAD-32 | S | Existence on the explicit domain without R9 [G AD-23; C S5 part]**
- **Owner premises:** D_M^U = τΣQ_m − Σr_m with |r_m| ≤ (403/250)Q_m^{3/2} (DYAD L-PHASE row A); 1/Q_m = Q₀⁻¹+m+O(√m) (RECOG reciprocal amplitude).
- **Consequence:** lim(D_M^U − τ log M) exists for every x₀∈U, without R9 or INF-1.
- **Not supplied:** the R9 coefficients, C₂, or an R9-free OPEN 21.
- **Custody:** RECOG owns the A1a join; NUMGEN owns its own application.
- **Check:** shared lift, indexing, the start-domain restriction, no circular import.

**FC-DYAD-33 | S | Lag-sign corollary for GAP-LOCK [C S5; G AD-24]**
- `~` **Statement:** on U, √Q≤1/25<250τ/403≈0.716, so τQ_m−r_m>0 with explicit two-sided bounds. The six-step lifted sum is below 2π at base points in U.
- **Action:** Offer it to NUMGEN as a corollary scoped to base points. NUMGEN checks anchor indexing, the seven-step crossing and coverage. No tube-wide claim is made.

**FC-DYAD-34 | S | Shear/recoil relation [G AD-27; atlas DYAD.X9]**
- **Statement:** (4√3/3)² = 16/3 equals the ratio of GEN's declared leading seed coefficients.
- **Action:** Optional cross-reference only. It is bookkeeping and selects no birth policy.

---

## 3. Protected scientific boundaries (from [G] §6, endorsed)

The successor must not change these unless a separately reviewed scientific change addresses them:
- **Selected T ≠ physical selection.** OPEN-P0, pole exchange and UV dynamics are untouched.
- **Normalization objects stay distinct.** Raw, archival, projected and finite-conjugacy objects are different. The smooth chart Φ is a fifth object and does not inherit the finite-chart bounds.
- **Maps ≠ jets.** NF6-DEG10 is a statement about the delivered chart. $S_h$ is not the smooth involution.
- **Domains.** Q_prim ≠ q_NF. Rows A and B are not mixed. U and U_T are kept explicit. The smooth radius is qualitative.
- **Existence ≠ analyticity.** B-an and B-6 are OPEN. E2 holds only with DX′(0)=0. The route used is G_∞^{−n}F^n.
- **Arithmetic and UV scope.**
  - b=5 does not settle b≥6.
  - Q403 is the p=4s family.
  - DZT's anomaly result is finite-horizon.
  - No OPEN-M deficit and no ×2/×4 repair is certified.

## 4. Verification behind this proposal

- **[C], atlas-run:**
  - Q₁₂ = −0.0096189… matches the closed form; M₁₂ = +0.0096….
  - N(−13+15√3/2) = ¼.
  - 47/54, 245/216, 89√3/324 and 4√3/3 re-derived.
  - τQ − (403/250)Q^{3/2} > 0 on U.
  - R* = λ_DSI^{1/2}.
  - The modulus of p sin²(π/p) decreases for p≥3.
  - GEN v2.8.9 §7 and TRIAD v1.6.1 §7.1 values match v6.4.19.
- **[G], advisory script `review_checks.py`, 11 checks:**
  - A01: the composition counterexample.
  - A02–A04: the W/Z map at p=6, with μ^Z = 3μ^W and ν₃^Z = 3n₂₁.
  - Others as listed in [G]'s package.
- **Re-checked by the atlas owner against the DSN text:** [G]'s L408, L614, L638, L671, L1577, L481, L358, and the field labels at L457/L601/L629. All confirmed.
- **Not performed by either pass:** replay of owner certificates (NF, IA, smooth embedding, L-PHASE, provenance).

## 5. Atlas corrections adopted from [G]

| Atlas reading | Corrected disposition |
|---|---|
| H12 / RECOG.R-L5: S_h = j⁶R₀ "needs verification" | Already in DYAD §§6.15–6.16. Route it (FB-21); no new link. |
| H1: all class-C consumers stale | RRF v0.8.4 §6.2a already has it. GEN and OFN remain (FB-13). |
| DYAD.X4: CAND-prefixed RIDs misleading | Keep them immutable; add a lookup of current grades (FB-24). |
| DYAD.X6: bridge proof custody differs | Documented by the owner. Clarify the agreement (N5); no invalidity. |
| Old pin ⇒ error | No. Check the claim; keep intentional historical pins (FB-16). |
| In-text proof without a certificate = gap | Not necessarily. Distinguish written proof, unavailable artifact and missing argument (FB-29). |
| Grammar cleanup | Do not remove OBS, ALG via IA or THM-ALG via IA (FB-24). |
| R-L9: cylinder fixed points missing | Present in §6.15. Fix navigation at first use (FB-28). |

These corrections will be applied to the atlas when it is regenerated from the adopted DYAD successor.

## 6. Disposition table (to be filled by the Dyadic team)

| Row | Tier | Origin | Disposition | Reason / missing premise | Edited section / RID / evidence | Consumers |
|---|---|---|---|---|---|---|
| FA-DYAD-01 | A | G05 | | | | RECOG, NUMGEN |
| FA-DYAD-02 | A | C-E2/E3, G02 | | | | all |
| FA-DYAD-03 | A | G03, G04 | | | | RRF, OFN |
| FA-DYAD-04 | A | G09 | | | | AZ, DZT |
| FA-DYAD-05 | A | G08 | | | | GEN, RECOG |
| FA-DYAD-06 | A | C-S4, G10 | | | | GEN, TRIAD |
| FA-DYAD-07 | A | C-S6, G07 | | | | TRIAD, RECOG |
| FA-DYAD-08 | A | C-S2, G11 | | | | AZ |
| FB-DYAD-09 | B | C-S2, G13 | | | | DZT, AZ |
| FB-DYAD-10 | B | C-S2/E9, G14 | | | | NUMGEN, AZ, DZT |
| FB-DYAD-11 | B | G12 | | | | NUMGEN |
| FB-DYAD-12 | B | C-S3, G17 | | | | NUMGEN, RECOG |
| FB-DYAD-13 | B | C-S8, G20 | | | | GEN, OFN, RRF, RER, ER-2B |
| FB-DYAD-14 | B | C-S5, G22, G24 | | | | NUMGEN |
| FB-DYAD-15 | B | C-S1, G25 | | | | DZT |
| FB-DYAD-16 | B | C-P1, G18 | | | | all |
| FB-DYAD-17 | B | C-P2 | | | | RECOG |
| FB-DYAD-18 | B | C-P3, G18, G28 | | | | TRIAD, NUMGEN, OFN, RECOG, RRF, FMS |
| FB-DYAD-19 | B | C-P5 | | | | GEN, DZT, AZ, NUMGEN, RECOG, RRF |
| FB-DYAD-20 | B | C-S11, G26 | | | | GEN, OPEN-M |
| FB-DYAD-21 | B | C-S12, G21 | | | | RECOG, RRF |
| FB-DYAD-22 | B | C-E1/E7, G01 | | | | — |
| FB-DYAD-23 | B | C-E11, G06 | | | | NUMGEN, RECOG |
| FB-DYAD-24 | B | C-E8/E10/F1–F4, G15 | | | | — |
| FB-DYAD-25 | B | C-S7 | | | | GEN |
| FB-DYAD-26 | B | C-S10 | | | | PROG |
| FB-DYAD-27 | B | C-E5/E6 | | | | — |
| FB-DYAD-28 | B | G16 | | | | RECOG |
| FB-DYAD-29 | B | G19 | | | | — |
| FB-DYAD-30 | B | C-E12 | | | | NUMGEN, RECOG |
| FC-DYAD-31 | C | C-S1 | | | | DZT |
| FC-DYAD-32 | C | G23 | | | | RECOG, NUMGEN |
| FC-DYAD-33 | C | C-S5, G24 | | | | NUMGEN |
| FC-DYAD-34 | C | G27 | | | | GEN, TRIAD |

*End of the consolidated Atlas Advisory for DYAD v6.4.19 (FINAL v1.0). Noncanonical; the Dyadic owner decides. No DSN was edited and no notice was sent.*
