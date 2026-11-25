# OPEN M (UVM) — OPEN-M-6 Scope Draft

## Typed model contract for the source-coupling audit

**Status:** [SESSION] / NONCANONICAL. Preparer's draft for the second co-owner's review and the PI's decision. It defines a scope. It authorizes no campaign and no certificate run, changes no DSN, registers no RRF profile, and selects no carrier, clock, lowering map or source normalization.
**By:** Claude, UVM co-owner (preparer and triage owner, PI assignment of 21 November 2026).
**Date:** 23 November 2026. `main` `98a4a80643007c2421dc4cee09260ba12d4ed9b4`.
**Basis:** PI decision 5 of 22 November 2026 (OPEN-M-6 selected as the first bounded science question; recorded in `records/uvm/UVM_REACTIVATION_TRIAGE.md` §1, PR #361, preparer-reported); triage row U1; the second co-owner's review `6013448844` and its reply of 23 November to the framing proposed after the RRF reading (relayed by the PI). The contract table C0–C3 in §6 is the second co-owner's; §5 states its three limits and what I checked of them.

---

## 1. The question, and why it has to be restated

The owner text (`uvm-v0.7.1`) asks, in §9 item 1, to replace the archival-chart `h_3 = 0` inference by transporting the source coupling through the adopted one-step conjugacy and to decide whether the leading coupling is "invariant, renormalized, or mixed"; R9 (line 304) records that "full-map + observable source-coupling invariance is OPEN".

Read literally, that question has no content, for three reasons found in the sources:

1. **A passive change of chart cannot test anything.** If dynamics and observable are transported together, `F̃ = ΦFΦ⁻¹`, `Õ = OΦ⁻¹`, then `Õ(F̃ⁿ(Φx)) = O(Fⁿx)` identically (second co-owner, review `6013448844`). RRF v0.8.4 §0.3 and §6.2 state the same rule: a passive recharting keeps the model; re-imposing an ansatz in the new coordinates makes a different conditional model unless an intertwining equivalence is proved.
2. **The three "charts" are not peers.** The archival object is `Φ_archive = id + h_4 + h_{5,nr}` (Dyadic SG-19 (i); line 81): a six-step Lie-gauge coordinate change that leaves every raw coefficient through degree 5 untouched. Through degree 3 it is the identity on the raw frame, so "`h_3 = 0`" there carries no information about the one-step conjugacy, whose `h_2` and `h_3` are nonzero. RRF §7 does not register `Φ_archive` as a profile.
3. **The source has no typed home.** RRF registers four dyad profiles and one provisional network profile, and no profile or transport arrow for the UV source bundle; UVM v0.7.1 cites RRF nowhere. By RRF §3 a quantity written in a profile without a registered arrow is untransported.

The restated question: **in which typed model is the source defined, under which symmetry action is it covariant, and which rival definitions are admissible — before any of them is compared physically.**

---

## 2. Sources and evidence state

| Source | Ref / SHA-256 | Read for this draft | Evidence |
|---|---|---|---|
| OPEN M DSN | `uvm-v0.7.1`, `0a51644d…f53e` | in full on 22 November; re-read here: §1.1–§1.2 (lines 54–66), R1 (237), R4 (269), R5 (297), R9 (304), OPEN-M-6 (138–139), §9 | `EV-SRC-READ`, `EV-HASH` |
| Dyadic DSN | `dyad-v6.4.24`, `10fbdacc…bc16` | targeted: line 81; SG-14 (360); SG-19 (369); §6.14 lines 768–800; §6.16 lines 1017–1022; §6.17 lines 1048–1060 | `EV-SRC-READ`, `EV-HASH` |
| RRF Representation Registry | `rrf-v0.8.4`, `2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce` (= BASELINE) | **in full**, 604 lines | `EV-SRC-READ`, `EV-HASH` |
| Genesis DSN | `gen-v2.10`, `63c3b020…3d62` | §6.7 lines 1006, 1008; 9B/9C lines read on 22 November | `EV-SRC-READ`, `EV-HASH` |

Not read: Dyadic §6.9, the body of §6.15, Theorem C of §6.16, and the O20 session records. Not available: `uvjet_equivariant_classification.py`, the certificate of R1–R6 (triage S0-3), so R1 is `EV-SRC-REPORTED`; `open1_liegauge_candidate.py`, so what the historical `1.006×10⁻²` envelope computed cannot be reconstructed. RRF v0.8.4 pins Dyadic v6.4.18; the smooth equivariant chart was registered at v6.4.20 and is not yet in RRF.

---

## 3. Objects and their typing

| Object | Owner statement | RRF status | Regularity and domain | Remark |
|---|---|---|---|---|
| One-step map `T`; return `F = T⁶` | Dyadic §6.14 `[DEF]` | native dynamics of `RRF-DYAD-LIFT` / `-W` | exact | every statement is conditional on the selected generator (SG-14) |
| Raw frame `W = 𝓛(ρ, η)` | Dyadic §6.14 | `RRF-DYAD-W` | lifted local | — |
| Polynomial conjugacy `W = h_6(z, z̄)` | `DYAD-ALG-NF6`, `DYAD-THM-NF-INV` | `RRF-DYAD-NF` | degree-6 identities; `h_6` injective on the disk of radius 1/10 in `z`, inverse on radius 9/100 in `W` | `h_2 ≠ 0`, `h_3 ≠ 0`; resonant coefficients set to zero |
| Formal normalizer and formal normal form | Dyadic §6.14, §6.16; RRF §2.4 | formal object | formal only | commutes with the linear action `A` at all orders |
| Archival change `Φ_archive` | Dyadic SG-19 (i), line 81 | **not registered** (RRF §7) | six-step, Lie strict-kernel convention | identity through degree 3 |
| Intrinsic generator `J_ℤ6 := T∘F^{−1/6}` | `DYAD-THM-FORMAL-Z6-GENERATOR` (formal, unique); `DYAD-THM-SMOOTH-EMBEDDING` E4 (`C^∞` germ) | imported in RRF §2.4b–c | formal; `C^∞` local with qualitative radius; analytic existence OPEN (B-6) | `J_ℤ6⁶ = id`, `J_ℤ6 T = T J_ℤ6`, linear part `A`. Chart-free, but defined from `T` |
| Smooth equivariant chart `Φ` | `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` | not yet in RRF | `C^∞`, qualitative radius | `Φ∘J_ℤ6 = A∘Φ` |
| UV update and its blocks | Genesis §6.7 `[DEF]` (no RID): `P_⊥ T_ℍ^UV(x+y) = H(x) + M_spin2(x)y + O(y²)` | none | not stated | `H` is covector-valued (`GEN-OPEN-SOURCE-PAIRING`); lowering conditional |
| Transverse bundle over the dyad domain, fibre `Π_⊥*`, and its trivialization | **no owner statement** | **no profile, no arrow** | — | missing object 1 |
| Action of the symmetry on that bundle, `J_⊥` | **no owner statement**; R1 gives only a linear weight ("`j`-component weight −1") in an unnamed chart | none | — | missing object 2 |
| Observable to be compared | none chosen | — | — | missing object 3 |
| Clock | not declared in UVM; R1 is a one-step statement, the archival object a six-step one | RRF requires `clock:` in every contract (§6.2) | — | missing declaration |

---

## 4. Notation fixed for this draft

Several letters mean different things across the streams (triage U5). Here:

- `J_ℤ6` is the intrinsic order-six generator of Dyadic §6.16; `J_NF(z) = z + μ_D z²z̄ + …` is the six-step normal-form jet of §6.14. They are different objects.
- `λ = e^{iπ/3}` only; `A` is multiplication by `λ`. The modulus of `Λ` in R5 is not called `λ` here.
- `μ_D` is the Dyadic cubic coefficient `c_21`; UVM's uses of `μ` are not needed below.
- `h`, `h_n`, `h_6` are the Dyadic normalizer; the UVM source amplitude (`m = C_m h`) does not occur below.
- `s(x)` is the complex coefficient function of the source in a fixed trivialization, so that the R1 minimal coupling `jΛz̄` has `s_NF(z) = Λ z̄`. The constant fibre action that makes its linear term covariant is multiplication by `λ̄`: `s(λz) = λ̄ s(z)`.

---

## 5. Three limits set by the second co-owner, and what I checked

**L1 — `J_ℤ6` is intrinsic to the chart but not to the model, and the bundle action is missing.** Agreed, and verified against Dyadic lines 1019–1021 and 1050: the generator is defined from `T`, so it inherits SG-14. What Dyadic does not supply is `J_⊥`. Without it, R1's weight classification has no chart-natural meaning.

Two typing points the scope has to settle, which I add:
- *Section form or update form.* If `H` is treated as a section, covariance reads `H(J_ℤ6 x) = J_⊥(x) H(x)`. If `H` is the transverse zeroth-order block of an update `T_ℍ^UV` that commutes with a lifted symmetry `J_ℍ(x+y) = J_ℤ6(x) + J_⊥(x)y + O(y²)`, then comparing the `Π_⊥` parts of `T_ℍ^UV∘J_ℍ` and `J_ℍ∘T_ℍ^UV` at `y = 0` gives `H(J_ℤ6 x) = J_⊥(Tx) H(x)` to first order in `H`. The two agree when `J_⊥` is constant. Genesis defines `H` through the update, which points to the second form. `[SESSION: ALG, conditional on the stated form of the lift]`
- *Covector type.* The fibre is `Π_⊥*`, so the action on it is the dual one. Reading it as the same "weight −1" representation as on `Π_⊥` presupposes an invariant pairing; with the `B`-form that is the conditional lowering Genesis leaves open. To be stated as a hypothesis, not assumed.

**L2 — the tower class is natural at jet order six; individual tower coefficients are not canonical.** Verified by hand:
- In the formal normal-form chart the one-step map commutes with `A` (only resonant monomials; RRF §2.4), hence so does its sixth iterate. `A` then commutes with `F`, has linear part `A` and order six, so by the uniqueness clause of `DYAD-THM-FORMAL-Z6-GENERATOR` the generator **is** `A` in that chart.
- `h_6` is the degree-6 truncation of the formal normalizer under the shared convention (RRF §2.4), so `𝒥_{≤6}(h_6⁻¹ J_ℤ6 h_6) = A`. R1's weight conditions are therefore usable through degree 6 in the `RRF-DYAD-NF` chart, which covers the tower degrees 1, 3, 5.
- The centralizer of `A` contains tangent-to-identity maps such as `ψ(z) = z + k z²z̄` (checked: `ψ(λz) = λψ(z)`). Under `ψ` the source `Λz̄` acquires a cubic term proportional to `Λ k̄ z z̄²` (sign by the direction of transport): same weight class, different cubic member. So "the minimal coupling has no cubic member" is a statement about a normalizer convention, not about the model. What survives every tangent-to-identity equivariant change is the degree-1 coefficient.

This bears on R4 (single-jet naturalness, `[INTERP]`) and on triage I-1: "one antilinear tower" fixes a class, not its higher members.

**L3 — the NF-native and W-native writings differ at degree two, and that difference is not yet physical.** Verified; formulas in §7. Both of its limits stand: without `J_⊥` the difference is not a certified physical difference, and neither candidate may be assumed covariant before it is tested.

---

## 6. The contract

The table is the second co-owner's. Tasks, acceptance criteria and the reading of a failure are the preparer's proposal.

| Contract | Mathematical task | Status | Acceptance criterion | What a failure means |
|---|---|---|---|---|
| **C0 — passive transport** | write the transport rule for dynamics, source, restoring block and observable under a base chart change together with a fibre re-trivialization; verify the identity of §1 item 1 on jets through a stated order | `[ALG]` control | the identity holds to that order in both directions (NF → W and W → NF) | an error in the transport or a truncation effect. Never physics |
| **C1 — NF-native candidate** | `s_C1(z) = Λ z̄` in the `h_6` chart, fixed trivialization, constant fibre action `λ̄`. Tests: **A1** covariance under `J_ℤ6` through jet order 6; **A2** the weight statement of R1 (degrees 1, 3, 5) re-derived without the missing certificate; **A3** the list of centralizer changes and of the data invariant under them | `[CAND]` | A1 and A2 hold as finite-jet identities with the quaternionic ordering and the covector typing written out; A3 names what is canonical | if A1 fails with the ordering written out, R1's premise is not what v0.7.1 states and R1 itself becomes a triage row |
| **C2 — W-native candidate** | `s_C2(W) = Λ W̄` in the raw frame, fixed trivialization, the same constant fibre action. Test **A1′**: covariance under `J_ℤ6` expressed in `W` | `[CAND]` | A1′ decided at each degree through 6 | see below: the preflight says A1′ fails at degree 2 under a constant fibre action |
| **C3 — physical discrimination** | for C1 and C2 on a common domain: one chosen representation-covariant observable and one source normalization | `[OPEN]` | not attempted in this scope | — |

C0 is not a model selection. C1 and C2 are not assumed to lie in one admissible class.

**What the preflight implies for C2** (conditional on §7). In the raw frame the generator is `J_W(W) = λW + δ_2(W) + O(3)` with `δ_2 ≠ 0`, so `s_C2(J_W W) − λ̄ s_C2(W) = Λ·conj(δ_2(W)) + O(3) ≠ 0`. C2 is then left with exactly two readings, and the work must say which is meant:
- **C2a:** keep `Λ W̄` and let the fibre action depend on the state so as to absorb the defect. It must then be shown whether (C2a, that action) is C1 in another trivialization — in which case it is not a rival — or a different model.
- **C2b:** keep the constant fibre action and accept covariance only under the *linear* map `W ↦ λW`. That map commutes with `T` at linear order only, so C2b is a source that does not respect the dyad's ℤ₆ symmetry. It is a legitimate hypothesis, and a different one from R1.

**C3 is out of scope here.** It needs, in this order: `J_⊥` or a principle that selects the trivialization; the clock; the common domain; the observable; the lowering and normalization of the covector. A candidate observable, not chosen: the quadratic part of the transverse source in raw coordinates, which C1 predicts to be `−Λ·conj(h_2(W, W̄))` and C2b predicts to be zero, in the same trivialization. RRF §4.1 applies: covariance belongs to the pair (observable, action), so the observable cannot be chosen before the action.

---

## 7. Preflight algebra

`[SESSION: ALG]`, conditional on a fixed fibre trivialization and a constant fibre action. Derived by hand and re-checked with a short symbolic script in this session; the script is not filed and this is not a certificate. P3 was derived independently by the second co-owner in its reply. With `h_2` of `DYAD-ALG-NF6`:

`h_2(z, z̄) = −(1+i√3)/12 · z² − (1/3) z z̄ + (1−i√3)/24 · z̄²`

- **P1.** In the formal normal-form chart `J_ℤ6 = A` (§5, L2).
- **P2.** `𝒥_{≤6}(h_6⁻¹ J_ℤ6 h_6) = A`.
- **P3.** From `z = W − h_2(W, W̄) + O(3)`: `s_C1` written in the raw frame is `Λ[W̄ − conj(h_2(W, W̄))] + O(3)`, so

  `s_C1^W − s_C2 = −Λ·conj(h_2(W, W̄)) + O(3)`, with `conj(h_2(W, W̄)) = (1+i√3)/24 · W² − (1/3) W W̄ − (1−i√3)/12 · W̄²`.

  Nonzero for `Λ ≠ 0`.
- **P4.** `J_W = h_6 A h_6⁻¹ + O(7) = λW + δ_2(W) + O(3)` with `δ_2(W) = h_2(λW, λ̄W̄) − λ h_2(W, W̄) = (1+i√3)/12 · W² − (1−i√3)/6 · W W̄ − (1/6) W̄²`. All three coefficients are nonzero because no quadratic monomial is resonant.
- **P5.** `ψ(z) = z + k z²z̄` commutes with `A`; it changes the cubic member of `Λz̄` by a term proportional to `Λ k̄ z z̄²`.

Not computed: anything at degree 3 or above; anything with the quaternionic ordering written out; any norm, amplitude or number.

---

## 8. Hypotheses the work would carry

| # | Hypothesis | Source of the obligation |
|---|---|---|
| H1 | the generator `T` (every dyad statement is conditional on it) | Dyadic SG-14 |
| H2 | regularity: formal, or `C^∞` local with qualitative radius; analytic not available | Dyadic OPEN 20 (B-an, B-6) |
| H3 | clock: primitive `T`; `T⁶` is derived sampling and not interchangeable with it | RRF §6.2, §6.2a |
| H4 | the UV update has the Genesis block form with `Π_∥`, `Π_⊥` as stated | Genesis §6.7 `[DEF]` |
| H5 | the symmetry lifts to the UV space, the lift preserves `Π_∥`, and the `Π_∥` part of the update at `y = 0` is `T` | not stated by any owner; needed for L1 |
| H6 | the fibre action is constant in the chosen trivialization (tests A1, A1′) | stipulation of this draft, made explicit |
| H7 | an invariant pairing identifies the action on `Π_⊥*` with the one on `Π_⊥` | conditional lowering, `GEN-OPEN-SOURCE-PAIRING` |
| H8 | the quaternionic ordering and the embedding of `Π_∥`, `Π_⊥` used by R1 | R1; its certificate is missing |

---

## 9. What the work delivers, and what it does not

**Delivers:** (a) a typed model contract for the source, in the form of RRF §6.2a (carrier and operation, `regularity:`, `clock:`, domain and chart, parameters, native-profile impact: none); (b) the results of A1, A2, A3 and A1′ as finite-jet identities; (c) a conditional separation statement for C1, C2a, C2b; (d) the ordered list of physical inputs C3 needs.

**Does not deliver:** a verdict "invariant / not invariant"; any number; a statement about `0.024`, `4/125` or R15; a physical falsifier; a selected carrier, profile, trivialization, lowering or normalization; a reading of the historical `1.006×10⁻²` envelope beyond "its chart does not move degrees 2 and 3".

**Size.** Everything in (b) is jet algebra through degree 6 in two real variables with a two-dimensional fibre. It fits a session; no server run is needed. If authorized, scripts and outputs would go to `evidence/uvm/` on a `claude/*` branch and the second co-owner would reproduce them independently.

---

## 10. Decisions asked

**Of the PI**
1. Is this scope accepted as the definition of OPEN-M-6's first stage?
2. If so, is the bounded algebra C0, C1 (A1–A3) and C2 (A1′) authorized as a certificate-bearing step? Decision 5 selected the question only.
3. Who proposes `J_⊥` and the bundle typing (H5–H7)? Suggested: UVM proposes, Genesis reviews as owner of the harness and of the covector typing.
4. Should UVM later ask RRF for a reference-only model-contract entry in the style of §6.2a? Not before (b) exists.

**Of the second co-owner**
1. Check P1–P5 and the derivation of P1 from the owner's uniqueness clause.
2. The section-form / update-form remark in §5 L1: is `J_⊥(Tx)` the right argument for the update form?
3. Is the split of C2 into C2a and C2b complete, or is there a third reading?
4. Anything in §3 that mis-types an owner object.

*End of scope draft. No UVM statement, pin, grade, pipe state or evidence file is changed by it.*
