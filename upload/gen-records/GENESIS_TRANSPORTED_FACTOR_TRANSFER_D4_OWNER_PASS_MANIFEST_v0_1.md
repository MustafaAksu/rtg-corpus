# GENESIS — D-4 Owner-Pass Manifest v0.1

**Date:** 19 October 2026
**Work ID:** `GENESIS-WORK-TRANSPORTED-FACTOR-TRANSFER`. This is not a GEN RID.
**Status:** `[SESSION]` owner-pass manifest, authorized by the Genesis owner decision of 19 Oct 2026 ("Owner-pass manifest: AUTHORIZED").
- Adopted Genesis v2.8.8 (`9abd36169a4bf6056318605c0399ff1f91c53f157b9181bdbfdb9faed3000f37`) is unchanged.
- **No v2.8.9 draft is authorized or started.**
- No new GEN RID, claim tag or grade is introduced here.

**Purpose.** Before any decision on whether D-4 becomes a Genesis owner theorem, fix two things:
- **D4-O1:** the exact OFN Q6 contract that D-4 is meant to serve;
- **D4-O2:** the exact adopted Lemma S dependency, with its point of application.

The manifest also states three guards (§4) and lists the owner decisions that remain (§5).

---

## 0. Inputs

| Input | Identity | Grade | Used for |
|---|---|---|---|
| D-4 SESSION v0.1.1 | `1a5f7f56690b1496d9972dc294053334e2eeca40a1d1d9e9f41185d84da3cee3` | `[SESSION]`, receiving review ACCEPT (19 Oct) | T-D4, L-JET, C1–C4 |
| `d4_transported_cubic_cert.py` / output | `f4c38285…3f6d` / `0e8053ae…0df7` | 6/6 PASS, independently rerun | D4-B gates G1–G6 |
| Genesis v2.8.8 | `9abd3616…0f37` | `[OWNER]` | §6.3a, §6.3a.1, §6.3b, SG-15, SG-16 |
| OFN reply v0.7.2 | project copy `claude/OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_7_2.md`. The OFN co-owner's working-copy SHA is `6044f43e…5b4c` as reported in the OFN source review; Genesis has **not** verified the project copy's bytes. | `[SESSION]` OFN co-owner decision; PI adoption pending (OFN v0.10) | Q6 text, §3.1, §3.4, §2 declarations |
| OFN source review v0.1 (`claude/OFN_SOURCE_REVIEW_ER2B_GEN288_OPEN3_v0_1.md`) | not pinned | `[SESSION]`, single OFN co-owner; its §3 answers are **proposals** for joint OFN agreement | proposed Q6 regularity (local C³), κ=2 reason |
| RRF v0.8.3 (adopted working standard, 19 Oct) | not pinned here | RRF working standard | §0.3 passive vs model-changing rule; "EF=TE and EF=T⁶E are different contracts" |
| RRF G2 interface review v0.4 | not pinned here | noncanonical, ACCEPT SCOPED | §3: factor ≠ exchange locality |

Genesis took the hash pins in the first three rows directly. Every OFN and RRF statement below is quoted or paraphrased from the project copies listed and is cited by section.

---

## 1. D4-O1 — The OFN Q6 contract

### 1.1 Source text

**OFN v0.7.2 §1, Q6 (verbatim):**

> "Required within the genuine interacting-triad class. Coupling means interaction that cannot be removed by a passive transformation into a decoupled product, under the declared state, encoding and clock."

**Operational forms that OFN itself uses:**
- **§3.1:** "Suppose F_κ … were locally C³-conjugate to a product G₁ × G₂ × G₃ of planar maps … A2 (and κ = 1) cannot be passively decoupled into three planar maps, nor into a neutral planar map times anything. That is exactly Q6 in the form OFN requires."
- **§3.1, still open:** "Splitting off the closure mode alone … is not a decoupling into edge relations and does not affect Q6 as worded."
- **§3.4, scope:** "the narrow Q6 definition (no passive decoupling into planar edge maps), not every conceivable product decomposition."

**Declarations (§2):**
- clock: "The primitive update. T⁶ is derived sampling" (also Q5: "Clock: primitive T");
- encoding: raw W is the test carrier;
- regularity: "Real-analytic laws are the admitted continuous FMS test class."

### 1.2 Fixed contract elements

| Element | Fixed value | Source | Status |
|---|---|---|---|
| Q6-STATE | the complete three-edge state on ℝ⁶ (closure mode included) | OFN §2.1–2.3 | fixed by text |
| Q6-CLOCK | **primitive** update; a six-step statement is supplementary | OFN §2.4, Q5 | fixed by text |
| Q6-TARGET | planar factors: (a) three planar maps; (b) one neutral planar map × arbitrary complement | OFN §3.1 | fixed by text |
| Q6-PASSIVE | local conjugacy by a diffeomorphism fixing 0. This transports the same model (RRF v0.8.3 §0.3). Reimposing closure or linear structure in new coordinates is a **different model**, not a passive transformation. | OFN §3.1 ("locally C³-conjugate"); RRF §0.3 | fixed by text |
| Q6-REG | regularity of the passive transformation | **not stated in Q6.** §3.1 and §3.4 argue at C³; the OFN source review proposes "local C³; below C³ OPEN" (proposal D1) | **OPEN at OFN**, pending joint OFN agreement or v0.10 |
| Q6-SCOPE | "narrow Q6" = no passive decoupling into planar (edge) maps; not every product decomposition | OFN §3.4 | fixed by text |

### 1.3 Coverage by T-D4 (transported family, γ ∈ ℝ∖{0,2})

| Q6 form | Reduction to a factor statement | Hypothesis check | Covered by |
|---|---|---|---|
| **(a)** F ≅ G₁×G₂×G₃ by C³ conjugacy Ψ, primitive clock | E_i = π_i∘Ψ is a C³ submersion onto ℝ² with E_i∘F = G_i∘E_i | The spectrum of DF(0) is {λ, λ, λ̄, λ̄, (1−γ)λ, (1−γ)λ̄}. A real 2×2 block takes a conjugate pair or two reals, so λ and λ̄ must pair: at least two G_i have spectrum {λ, λ̄}. **(H_prim):** (1−γ)λ ∉ {λ, λ̄} for real γ ≠ 0 (at γ = 1 the 𝒟 eigenvalues are 0). | T-D4(ii) |
| **(b)** F ≅ G₁ × G′ with G₁ planar and neutral, primitive clock | E = π₁∘Ψ | The unit-circle eigenvalues of DF(0) are λ and λ̄ only, since \|1−γ\| ≠ 1. So spec DG₁(0) = {λ, λ̄} and (H_prim) holds. | T-D4(ii) |
| (a)/(b) at the six-step clock | E∘F⁶ = G′∘E with a unit-circle target | (H_spec): \|1−γ\|⁶ ≠ 1 | T-D4(i), supplementary |
| Encoding change (raw W ↔ Φ-chart) | C³ conjugacy | same T′ | T-D4(iii) |

**Result (`[ALG — SESSION]`).** With Q6-REG = C³, the narrow Q6 forms (a) and (b), at the declared primitive clock, are covered by T-D4. This holds for every real C³ germ in the class of T-D4: the jet surrogate, 𝓕_{γ,Φ} whenever it exists, and any real C³ model with the same 3-jet. The class-C range κ ∉ {0,1,2} lies inside γ ∈ ℝ∖{0,2}.

### 1.4 Not covered — Q6 readings outside the Genesis hypotheses

The owner's rule applies here: OFN's physical meaning for Q6 cannot widen the Genesis hypotheses. Any wider exclusion needs its own proof.

| Reading | Why it is not covered | Reference |
|---|---|---|
| Passive transformations below C³ | d=2 C¹/C² factors are OPEN | SG-16; scope note D-2 |
| Products that are not planar, e.g. a 4+2 split into a centre part times the closure mode | Genesis covers target dimension d ≤ 3 only, and factors onto the 𝒟 mode are OPEN. Whether such a split exists is **not examined**. OFN §3.1 already places it outside "Q6 as worded". | SG-16; scope note D-3 |
| γ ∈ {0, 2} | outside the hypotheses; the neutral 𝒟 mode at γ = 2 | D-4 §7(2) |
| Non-submersive, non-local or topological decouplings | not in any Genesis statement | SG-15, SG-16 |
| The formal series F^N_κ as such | Genesis makes no statement about formal maps (guard G-JET) | D-4 §1, §7(4) |

**What Genesis needs from OFN (no Genesis action).** Confirmation that Q6 means the narrow form at local C³ and at the primitive clock, i.e. adoption of proposal D1 or an equivalent v0.10 wording. Until that is confirmed, the coverage in §1.3 is conditional on Q6-REG = C³.

---

## 2. D4-O2 — Dependence on the adopted Lemma S

### 2.1 The adopted statement

`GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA`, v2.8.8 §6.3a.1, scope "real-linear factors of a homogeneous chiral cubic; branch c − iβ ≠ 0, β ≠ 0":
- On ℂ² ≅ ℝ⁴, f(u,v) = (c u|u|² − iβNu, c v|v|² − iβNv), with N = |u|² + |v|².
- Assume c − iβ ≠ 0 and β ≠ 0.
- Then no real-linear surjection ℓ: ℝ⁴ → ℝ^d (d ∈ {1,2,3}) satisfies ℓ∘f = t∘ℓ for a C¹ map t.

### 2.2 Point of application in D-4

| Item | D-4 value | Check |
|---|---|---|
| Space | 𝒞 = T₀M^c, coordinates (w₁, w₂) with w₃ = −w₁ − w₂ | same as §6.3a; certificate `ue = [u1, u2, −u1−u2]` |
| Chiral coordinates | u = w₁ + λw₂, v = w₁ + λ̄w₂ | identical to §6.3a(d) |
| Cubic | the degree-3 part of F⁶ restricted to M^c: u(f) = p u\|u\|² + q\|v\|²u, and v(f) symmetric; no other monomials | G3 (both components, exact) |
| Coefficient map | c = p − q and β = iq, hence c − iβ = p and −iβ = q | algebraic identity; the same convention note appears in v2.8.8 §6.3a.1 Evidence ("p = c − iβ, q = −iβ") |
| Values | p = μ(N)/3 and q = 2μ(N)/3; at the DYAD value p = −1/6 − (2/9)i√3, q = −1/3 − (4/9)i√3 | G3, G5 |
| Branch | c − iβ = p ≠ 0 and β = iq ≠ 0 ⟺ μ(N) ≠ 0 | G5, G6 (n = 0 control) |
| ℓ | ℓ\|_𝒞 for ℓ = DE(0), onto by the reduction step | §6.3b (b) / primitive (ii) |
| t | the cubic t₃ of the target return; a polynomial, so C¹ | §6.3a.1 (c) |

**Result.** D-4 uses Lemma S **exactly in its adopted branch and scope**. It needs no extension of the lemma, no other branch (c − iβ = 0) and no Gröbner input.

### 2.3 Other adopted inputs D-4 depends on

| Dependency | Location in v2.8.8 | Grade there | Note for the owner |
|---|---|---|---|
| Leading-term lemma (no quadratic part of the six-step return) | §6.3a(b), inside the proof of `GEN-THM-K3-PLANAR-FACTOR-NOGO` | proof step of a `[THM]` | general; used verbatim |
| Linear part, no quadratic term, cubic identity ℓ∘f₃ = t₃∘ℓ | §6.3a.1 (a)–(c), proof of `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` | proof steps of a `[THM]` | used verbatim on M^c |
| Six-step reduction under (H_spec) | §6.3b proof (a)–(b) of `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` | proof steps of a `[THM]` | used verbatim |
| **Primitive-clock reduction under (H_prim)** | §6.3b "Primitive clock (C³ only)" | **`[ALG]`, no RID** | **Q6 is a primitive-clock contract (§1.2).** The primitive transfer therefore rests on an adopted `[ALG]` block, not on a `[THM]` RID. The owner must decide the grade of any primitive-clock D-4 statement (§5, decision 2). |
| Existence of a C³ centre manifold, and uniqueness of its 3-jet | §6.3b "Centre manifold and exact six-step cubic" | `[ALG]`; external centre-manifold theorem for C^r maps (not cited by name) | used with the same standing as in v2.8.8 |
| L-JET (the proofs use only C³ regularity, the linear data and the 3-jet) | D-4 §3 | `[SESSION]`, receiving review ACCEPT | not an owner statement |

---

## 3. Coverage matrix: D-4 objects × statements

| Object | T-D4(i), six-step | T-D4(ii), primitive | Q6 narrow (a)/(b) | Exists as a real map? |
|---|---|---|---|---|
| Jet surrogate G^{N₃}_γ (C1) | yes | yes | yes, at Q6-REG = C³ | yes, a polynomial |
| 𝓕_{γ,Φ}, the exact transported class (C2) | yes, if Φ is C³ | yes, if Φ is C³ | yes, if it exists | **OPEN 20** |
| Any real C³ model with the same 3-jet (C3) | yes | yes | yes | — |
| Formal F^N_κ | no statement | no statement | no statement | not a real map |
| Raw F_γ | existing RID | existing [ALG] | existing (OFN §3.1) | yes |

---

## 4. Guards (binding on any successor text)

- **G-JET (jet vs real map).** No real C³ no-go is derived from formal computations alone. Real statements concern real C³ germs. Formal and polynomial computations enter only as exact third-jet data (D-4 v0.1.1 §1: o(|z|³) and j³ identities).
- **G-20 (OPEN 20).** The existence of the exact transported class (J, Φ; DYAD OPEN 20 B-an / B-6 / B-∞) is kept separate from the factor obstruction of existing real C³ models. T-D4 neither needs nor supplies existence. C2 is vacuous if no real J exists.
- **G-SEL (model selection).** No statement that C is the only physical option follows from the Q6 coverage: **Q6 obstruction ⇏ unique physical model C.** By C3, narrow Q6 does not even distinguish class C from its 3-jet equivalents. Selection stays with OFN/FMS.
- **G-OFN (no widening by meaning).** OFN's physical reading of "decoupled product" does not extend the Genesis hypotheses (C³, d ≤ 3, planar or low-rank targets, (H_spec)/(H_prim), γ ∉ {0,2}). Exclusion of any wider class (§1.4) needs a separate proof.
- **G-SG (scope guards).** SG-15 and SG-16 stay byte-identical. The existing RIDs `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` and `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` are **not widened or regraded** to cover the transported family.

---

## 5. Owner decisions remaining (none taken here)

1. **Form.** If D-4 becomes owner text, would it be a new GEN RID for the transported-class statement, with its own proof citing the adopted steps, or a non-RID `[ALG]` block? Widening existing RIDs is excluded by G-SG.
2. **Primitive-clock grade.** The six-step part can be stated as `[THM]` alongside the existing six-step RID. The primitive part, which is the one Q6 actually uses, sits beside an adopted `[ALG]` block. Possible routes: keep it `[ALG]`, or promote the primitive family statement and its transported counterpart together. Either way that is a separate owner decision.
3. **Content of the statement.** Which of these to include: the jet surrogate (C1), the conditional class statement (C2), the 3-jet class (C3) or the encoding clause T-D4(iii).
4. **Dependency on OFN.** Whether owner-level treatment waits for OFN's confirmation of Q6-REG = C³ (§1.4), or states the result at C³ regardless and leaves the Q6 reading to OFN.
5. **Notice.** Until a decision is made, OFN may receive D-4 v0.1.1 only with its SESSION status. No notice may describe it as an adopted Genesis theorem.

## 6. Gates for a later draft (if authorized; not run now)

| Gate | Content |
|---|---|
| DM1 | v2.8.8 baseline hash; deterministic build; reverse-edit recovery |
| DM2 | §6.3a, §6.3a.1, §6.3b, SG-15 and SG-16 byte-identical; existing GEN RID lines unchanged |
| DM3 | the new text cites `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` with branch and convention exactly as in §2.2 |
| DM4 | the primitive-clock part carries the grade chosen in decision 2, never higher than the adopted primitive block unless that block is regraded in the same draft |
| DM5 | guard phrases G-JET, G-20, G-SEL and G-OFN are present; no "unique model" or "physical selection" wording |
| DM6 | `d4_transported_cubic_cert.py` reruns 6/6 at its pinned hash |
| DM7 | no import of J, Lemma F, F1–F3 or OFN verdicts as Genesis claims |

## 7. Disposition requested

- **D4-O1:** closed on the text level for the narrow Q6 contract. Q6-REG stays conditional at OFN (C³ proposed, not yet adopted).
- **D4-O2:** closed. Lemma S is used in its adopted branch without extension. The primitive-clock dependency on an `[ALG]` block is flagged for owner decision 2.
- **Genesis v2.8.8:** ADOPTED, UNCHANGED. **v2.8.9 draft:** NOT AUTHORIZED.
