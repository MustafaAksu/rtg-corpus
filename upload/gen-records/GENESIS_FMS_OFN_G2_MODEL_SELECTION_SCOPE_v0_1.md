# GENESIS — FMS/OFN G2 Model-Selection Scope Note v0.1

**Date:** 19 October 2026
**Status:** `[SESSION]` noncanonical. This is a Genesis-side dependency analysis.
- No owner file is modified.
- No new GEN RID, claim tag or theorem is introduced.
- No OFN or FMS decision is made or reconstructed here.

**In force (Genesis):** adopted `RTG_GENESIS_GEOMETRY_DSN_v2.8.8` (`9abd36169a4bf6056318605c0399ff1f91c53f157b9181bdbfdb9faed3000f37`).

**Purpose.** This note keeps three layers apart:
1. **Mathematical exclusion.** What a theorem rules out, under its own hypotheses.
2. **Physical admissibility.** Which requirements OFN counts as necessary.
3. **Model selection.** Which class survives once the requirements are applied.

It then answers one question:

> **Central question.** Do the physical requirements that OFN counts as necessary actually entail the mathematical factor class that Genesis excludes?

---

## 0. Sources (actual texts read)

| Source | Version / location | Grade | Note |
|---|---|---|---|
| OFN reply | `claude/OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_7_2.md` (project copy) | `[SESSION]` joint OFN co-owner decision; PI adoption pending (OFN v0.10) | Read in full in this session. SHA not pinned: byte identity of the project copy to the OFN owners' file was not verified. **The owner should confirm that this copy is authoritative.** |
| FMS ledger | `claude/FMS_MODEL_SELECTION_LEDGER_v0_5_1_SESSION.md` (17 Oct) | `[SESSION]` | Read in full. It predates OFN v0.7.x and the Genesis v2.8.7 adoption. |
| Genesis | adopted v2.8.8 (hash above) | `[OWNER]` | `GEN-THM-K3-PLANAR-FACTOR-NOGO`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`, `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO`, `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA`, `GEN-DEF-MEANFEEDBACK-FAMILY`; SG-15, SG-16 |

Every OFN statement below is cited by its section in v0.7.2. Anything not found in that text is marked **"not stated in text"**.

**Notation.** OFN and FMS write κ; Genesis SG-16 writes γ for the same parameter of the mean-feedback family. Here γ ≡ κ.

---

## 1. The three layers

| Layer | Question | Owner | Typical object |
|---|---|---|---|
| L1 — mathematical exclusion | Under the stated hypotheses, does an object (factor, invariant manifold, conjugacy) exist? | Genesis, DYAD, FMS (SESSION) | `[THM]` / `[ALG]` with scope |
| L2 — physical admissibility | Which properties must a physical triad model have? | OFN (RRF for representation) | Q1–Q6, Standard C `[DEF]` |
| L3 — model selection | Which of A1/A2/B/C survives the L2 requirements? | FMS proposes; OFN decides | disposition table (OFN §4) |

**Transfer rule.** An L1 result affects L3 only through a **bridge premise**. The bridge says that a requirement in L2 *is* (or implies) the hypothesis or conclusion of the L1 result. Bridge premises are L2 statements: OFN or RRF must state them. Genesis does not supply them.

---

## 2. Status table

| Item | Stream | Status | Text basis |
|---|---|---|---|
| F₁ and 6S-core factor obstructions | Genesis | **Adopted** | v2.8.8 `GEN-THM-K3-PLANAR-FACTOR-NOGO`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` |
| F_γ spectral-conditional obstruction | Genesis | **Adopted** | v2.8.8 `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO`, γ∉{0,2}, (H_spec). Primitive-clock statement under (H_prim) |
| γ = 2 resonance | Genesis | OPEN | v2.8.8; FMS §3, κ=2 row `UNRESOLVED` |
| d = 2 C¹/C² factors | Genesis | OPEN | v2.8.8 scope; FMS §4 regularity gates |
| Spectral contact with the closure mode (factors onto 𝒟 / failure of (H_spec)) | Genesis | OPEN | v2.8.8 SG-16; FMS §9; OFN §3.1 "Still open", §4 "Open" |
| Physical closure / edge-autonomy requirements | OFN | decision area: SESSION decision v0.7.2, PI adoption pending | OFN §1 Q1–Q6, Standard C `[DEF]` |
| FMS C-a…C-e alternatives | FMS | model research | FMS §5.3 |
| Physical G2 / node-exchange realization | OFN/RRF and owners | OPEN | OFN §1 Q5 (OPEN-OPA); §3.5(f); DYAD OPEN 20; RRF OPEN-A |
| *(added)* Transfer of the factor no-go chain to the transported family | Genesis (candidate) | not opened | OFN §3.4 "apply verbatim"; see §6 D-4 |

---

## 3. Scope correction: the bridge premise

The Genesis theorems have the form (L1):

> no local C³ submersive factor E with E∘F = T′∘E (or E∘F⁶ = T′∘E) of the stated rank, under the stated spectral hypothesis.

FMS R4′ (§5.3, `[SESSION — ALG]`) adds one step. If the state is exactly three edges, then three-edge closure (C or C′) and **A** (primitive autonomy of all three edges) cannot both hold.

From these alone, "physical closure and physical edge autonomy are logically incompatible" follows **only if** this premise holds:

> **(P-bridge)** Physical edge autonomy is represented by the submersive-factor contract A (or A6): E_e∘F = T∘E_e on a neighbourhood of 0, with E_e submersive and of the stated regularity.

**What the texts say about P-bridge**
- **FMS §1** defines A as a mathematical condition. FMS does not claim A is the physical meaning of autonomy, and §8 explicitly leaves the verdicts to OFN.
- **OFN v0.7.2 §1, Q3a:** *"Full primitive edge autonomy. Not required."* OFN's minimum target is **Standard C** `[DEF]`: a nonempty, F-invariant regime 𝓡 on which I_e = O(|r|⁴) for every edge.
- **OFN §1, Q3b:** partial autonomy is *"not acceptable as the law of a genuine triad"* in asymmetric form.

**Conclusion (L2 reading of the texts, not a theorem).** OFN v0.7.2 does not assert P-bridge. The incompatibility chain therefore does not enter OFN's selection as a premise. The Genesis theorems and FMS R4′ remain true at L1, but neither is a physical incompatibility result.

---

## 4. Central question, requirement by requirement

The question for each OFN item: does it entail the factor class that Genesis excludes?

| OFN item (v0.7.2) | Text status | Entails the excluded factor class? | Role of Genesis results |
|---|---|---|---|
| Q1 exact closure | not universal; admissible as a flat sector | no | none |
| Q2 asymptotic closure | admissible, not required | no | none |
| Q3a full primitive autonomy | **not required** | It *would* have been the entry point: A is exactly the factor contract. Not required, so no. | none at L3 |
| Standard C `[DEF]` | required minimum target | **no** (see below) | none |
| Q3b partial autonomy | not acceptable in asymmetric form | no requirement | none |
| Q4 cycle content | genuine class must permit nonintegrable cycle content | no factor statement | possible link to the closure-mode OPEN (§6 D-3); not stated in text |
| Q5 covariance | required | no | none |
| Q6 genuine coupling | required | no. The direction is **reversed**: *absence* of a neutral planar factor implies Q6 | **positive certificate** (OFN §3.1, §3.4) |

**Why Standard C does not entail a factor.** A factor is a relation E∘F = T∘E on an open neighbourhood, with E submersive. Standard C constrains F only on the invariant regime 𝓡, which may be lower-dimensional, and only through cubic order (I_e = O(|r|⁴)). On 𝓡 it gives at most an approximate edge relation r_e∘F = T∘r_e + O(|r|⁴) for F|𝓡. That is not a submersive factor of F, so the Genesis no-go hypotheses are not met. Conversely, the Genesis theorems say nothing about Standard C. OFN's exclusion of A2 under Standard C comes from its own §3.2, not from Genesis.

**Answer to the central question (under OFN v0.7.2 as written).** No requirement that OFN counts as necessary entails the submersive-factor class Genesis excludes. The Genesis factor obstructions enter model selection in one place only, and **positively**: as sufficient certificates for Q6 in its narrow form (no passive decoupling into planar edge maps).

---

## 5. Attribution of the OFN §4 dispositions

This table shows where each exclusion actually comes from.

| Class | OFN §4 disposition | Source of the exclusion | Uses a Genesis no-go? |
|---|---|---|---|
| A1, κ = 1 (raw) | excluded | Q4 fails (flat); Standard C fails (§3.2) | no |
| B, κ = 0 (raw) | excluded from the coupled class | Q6: the model is a product by construction | no |
| A2, 0<κ<2, κ≠1 (raw) | excluded under Standard C at cubic order | §3.2 `[ALG — SESSION]` (OFN), local, smooth invariant regimes only | no. Genesis certifies A2's Q6 (§3.1), which is the property A2 *satisfies* |
| C, transported, κ∉{0,1,2} | **primary candidate**, formal until J is realized | n/a | Q6 entry via Lemma S plus "§3.1 argument verbatim" (§3.4); see D-4 |

**Consequences**
1. Genesis is **not** on the critical exclusion path of OFN §4. Every exclusion rests on OFN's Standard C definition (PI decision), OFN §3.2 (OFN SESSION), Q4, or the trivial product structure at κ=0.
2. The L1 support for "C is selected" is therefore OFN §3.2 together with its stated loopholes: non-manifold invariant sets, finite-amplitude regimes, other carriers. That support is a SESSION result of OFN, not an owner result of Genesis.
3. **C is not shown to be the only possible model.** OFN calls it the "primary candidate class", not the unique one. It is formal until DYAD OPEN 20 (B-6 / B-∞ existence) is answered. OFN §4 also lists "C — other routes" as open, and models outside the κ family are not tested at all (FMS §3, last row).

---

## 6. Dependency map: which Genesis OPEN actually affects selection?

| ID | Genesis OPEN | Effect on L3 under OFN v0.7.2 | Condition under which it would matter |
|---|---|---|---|
| D-1 | γ = 2 resonance | **None.** Raw κ=2 is covered by §3.2, which is stated for every κ≠0. The transported C range excludes κ=2 explicitly (§4). | If OFN admits a κ=2 member. Its Q6 would then need the γ=2 analysis, which (H_spec)/(H_prim) do not cover. The reason for excluding κ=2 from class C is **not stated in text**. |
| D-2 | d = 2 C¹/C² factors | **Conditional.** Q6 says "under the declared state, encoding and clock". The regularity of the *passive transformation* is **not stated in text**. §3.1 and §3.4 argue at C³. | If OFN fixes Q6 at C³ or above, there is no effect. If Q6 is meant below C³, the Q6 entry of class C (and of A2) becomes **unproved, not refuted**. Also bears on FMS route C-c. |
| D-3 | Closure-mode factors (spectral contact) | **None for Q6:** OFN §3.1 says it "does not affect Q6 as worded". | Possible relevance to Q4. A factor onto the closure mode would make the cycle defect dynamically autonomous. OFN keeps "dynamical independence" as a separate property (accepted item 5) but states no requirement on it. |
| D-4 | *(not in the original table)* Factor no-go for the **transported** family F^N_κ (formal) and 𝓕_{κ,Φ} (real, conditional on J) | **The only selection-relevant Genesis item.** The Q6 entry of the primary candidate (OFN §3.4) rests on it. | See below. |

**D-4 in detail**

*What is already covered.*
- `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` is algebraic and applies to any cubic of chiral form.
- With c = p − q and β = iq, the conditions c − iβ ≠ 0 and β ≠ 0 read p ≠ 0 and q ≠ 0.
- OFN's p = μ/3 and q = 2μ/3 satisfy both.

*What is not covered.*
- The owner scope of `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` and of the primitive-clock statement is the raw family F_γ built from the DYAD map T.
- The reduction chain (Sylvester step, centre-manifold reduction, six-step cubic) for F^N_κ or 𝓕_{κ,Φ} is not an owner statement.
- OFN grades its own transfer `[ALG — formal; leading order]` at SESSION level.

*What would settle it.* A scoped Genesis statement for the class "mean-feedback family over a dyad map N with DN(0) = A and six-step cubic of chiral form with p, q ≠ 0".
- For 𝓕_{κ,Φ} it would be conditional on the realization of J (DYAD OPEN 20).
- **No such statement is made here.** Opening this work needs an owner decision.

**Consistency with v2.8.8 SG-16 / consumer record §4.** The edgewise maps J^{×3} and R₀^{×3} do not preserve 𝒞 in the raw carrier. The OFN transported class is a *differently constructed* network: P_κ acts in the Φ-chart. It is therefore not excluded by that result, as the consumer record's scope guard already says.

---

## 7. FMS ↔ OFN synchronization observations (informational, no decision)

1. **FMS v0.5.1 is behind its sources.**
   - R7 reads "Genesis owner adoption pending". The results are now owner-adopted: v2.8.7 (18 Oct), carried unchanged into v2.8.8.
   - FMS's κ corresponds to SG-16's γ.
2. **The FMS §8 elimination statement** (closure + full autonomy, R4′) is a correct SESSION statement at L1. Under OFN Q3a it is **not a selection premise**, because A is not required.
3. **The FMS route menu is incomplete relative to OFN.**
   - C-a…C-e negate R4′ hypotheses while keeping hypothesis 2 (full primitive autonomy).
   - The OFN transported class instead **replaces hypothesis 2 by Standard C**: autonomy only on an invariant regime, to cubic order. It is not one of C-a…C-e. C-b (partial/asymmetric autonomy) is a different thing.
   - Any label for this route is left to FMS.
4. **OFN §3.1 is graded "`[ALG — conditional on 6S]`"** and OFN §5 cites "K3 note v0.3".
   - For the raw family the condition is now discharged at owner level by the adopted Genesis RIDs.
   - The (H_prim) check: for a unit-circle target, (1−κ)λ ∉ {λ, λ̄} for every real κ ≠ 0.
   - OFN may repin at its convenience. This is informational and does not change any OFN verdict.

---

## 8. Explicit non-claims

- It is **not** claimed that physical closure and physical edge autonomy are incompatible (§3).
- It is **not** claimed that class C is the only mathematically possible physical model (§5).
- It is **not** claimed that A2 or A1 is physically excluded by Genesis. Their exclusions are OFN's, at SESSION level.
- No OFN decision is reconstructed from summaries. Every OFN item is quoted from the v0.7.2 project copy, or marked "not stated in text".
- D-4 is a dependency, not a theorem. Genesis owner RIDs keep their adopted scope (SG-15, SG-16).

## 9. Questions this note raises (for the owners; no action taken)

**To OFN**
- (i) What is the regularity class of the passive transformation in Q6? (D-2)
- (ii) Why is κ=2 excluded from the transported C range? (D-1)
- (iii) Is dynamical independence of the cycle defect a requirement, a prohibition, or neither? (D-3)
- (iv) Confirm that the project copy of v0.7.2 is the authoritative text.

**To FMS**
- Register the OFN Standard C route next to C-a…C-e.
- Refresh R7 to the adopted Genesis RIDs.

**To the Genesis owner**
- Decide whether D-4 should be opened as a scoped work item. It is the only Genesis OPEN found here with a direct effect on model selection.
