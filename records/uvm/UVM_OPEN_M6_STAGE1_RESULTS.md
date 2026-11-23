# OPEN M (UVM) — OPEN-M-6 Stage 1: Jet-Covariance Results

**Status:** [SESSION] / NONCANONICAL. Results of the bounded jet algebra the PI authorized on 23 November 2026. They are finite-jet identities with a filed script and output. Nothing here is adopted UVM science, edits the DSN, registers an RRF profile, or selects a carrier, lowering or normalization. **Revision 3** (23 November 2026) makes the two documentation corrections of the second co-owner's readback `6020412456` (JP6 and §4–§5; §9), after which that review gives Stage 1 ACCEPT SCOPED at `[SESSION]` grade. **Revision 2** answered the second co-owner's review `6019523031` (ACCEPT WITH SCOPED CHANGES): its independent reproduction is recorded in §2, its three required changes in §4–§6, the revision in §9. The numerical results are unchanged and the certificate was not rerun.
**By:** Claude, UVM co-owner (preparer and triage owner).
**Date:** 23 November 2026. Branch base `main` `98a4a80643007c2421dc4cee09260ba12d4ed9b4`.
**Scope:** `records/uvm/UVM_OPEN_M6_SCOPE_DRAFT.md` (PR #365), contracts C0, C1 (A1–A3), C2 (A1′).

---

## 1. PI decisions of 23 November 2026 (12:32 +03:00, project conversation with this session)

Recorded by the preparer from the PI's numbered reply to the three numbered questions of the scope draft §10; preparer-reported until the PI confirms on the PR.

| # | Question | PI's reply | What it settles |
|---|---|---|---|
| 1 | Is the scope accepted as the definition of OPEN-M-6's first stage? | "Kabul" | the scope draft governs this stage |
| 2 | Is the bounded algebra C0, C1 (A1–A3), C2 (A1′) authorized as a certificate-bearing step? | "Yetkilendiriliyor." | this record and its evidence |
| 3 | Who proposes `J_⊥` and the bundle typing? | "OPEN-M(UVM) önerir Genesis inceler." | UVM proposes (§6 below), Genesis reviews |

---

## 2. Evidence

| Item | Value |
|---|---|
| Script | `evidence/uvm/scripts/uvm_open_m6_stage1_jet_cert.py`, SHA-256 `db080cdc33081aa902257d5be7da22c0c5c763f0405ccdc91bd69322da3db42d` |
| Output | `evidence/uvm/open-m6-stage1/stdout.txt`, SHA-256 `60bdac3156661ba1d91ec1c79a8b12dfc949aa82f9855fe7ceab4f9b3fa8e544` |
| Coefficient tables | `evidence/uvm/open-m6-stage1/results.json`, SHA-256 `507479c8a0492b6ff339bb733fd5e853df7133c637d29e31c37cab030b771087` |
| Hash list | `evidence/uvm/open-m6-stage1/SHA256SUMS.txt` |
| Command | `python3 -I evidence/uvm/scripts/uvm_open_m6_stage1_jet_cert.py --json evidence/uvm/open-m6-stage1/results.json > evidence/uvm/open-m6-stage1/stdout.txt` |
| Environment | Python 3.13.18, standard library only; about two seconds; exit code 0 |
| Result | 39 checks, 39 passed, 0 failed; a second run is byte-identical |
| Method | exact arithmetic in `ℚ(i√3)` on jets of total degree ≤ 6 in a complex variable and its conjugate; no floating point |
| Independent reproduction | second co-owner (ChatGPT UVM session), review `6019523031`: a separate SymPy 1.14 polynomial-ring implementation over `ℚ(i√3)[z, z̄]`, written without importing or running this script. Checks reproduced: E0–E6, G0–G6, P2, A2, A1′ (degree 2 and degrees 2–6), P3, C2a-1, plus the GL₂(ℝ) source-matching identity of §4 through degree 6. All pass. `EV-INDEP` for those checks |
| Its files | `evidence/uvm/scripts/uvm_open_m6_independent_sympy_check.py`, SHA-256 `2f1089d16c981677a676258cbc9878ab18bc1a763cea0837a10a4ec4a3370405`; `evidence/uvm/open-m6-stage1/independent_sympy_output.txt`, SHA-256 `c371a8ede8f3176aa7bb3e088789da1e1ecdd0907ea2a9a880603f16faa02eb3`. Arrived unchanged on branch `upload/uvm-open-m6-independent-check` (commit `1b42a1a2cf14`); placed here by copy. Hashes equal those stated in the review |
| Its re-run here | in an empty directory with `python3 -I` (SymPy 1.14.0): exit 0, output byte-identical. This confirms the run; the independence is of the reviewer's implementation |
| Not independently reproduced | A1 as a separate check (it follows from P2), A3, Q1–Q3, CONTROL-Q4, C0-0 to C0-4 and the four controls, C2a-2, C2a-3. Single-session `EV-RUN` |

Four of the 39 are expected-failure controls (`CONTROL-*`): each passes when a deliberately wrong variant is detected as wrong.

**Engine validation.** Starting only from the generator `T(ρ, η) = (ρ − sin η, η + e^ρ − 1 − sin η)` and the frame `W = ρ + ωη`, the script recomputes the Dyadic normalizer and normal forms and matches the owner values of `DYAD-ALG-NF6` exactly: `h_2`; `h_3` nonzero in the channels (3,0), (1,2), (0,3) only; 23 nonzero coefficients of `h_6`; `n_21`, `n_32`, `n_05`; `μ`, `a_32`, `a_05` (checks E1–E6). That is an independent recomputation of those owner numbers with new code, not a rerun of the Dyadic certificate.

---

## 3. Results

| Check | Statement | Result |
|---|---|---|
| E0–E6 | engine reproduces `DYAD-ALG-NF6` (see above) | pass |
| G0–G5 | the intrinsic generator built from first principles in the raw frame — `J_W := f∘K⁻¹`, with `K` the tangent-to-identity sixth root of `F = f⁶` solved degree by degree — has linear part `λ`, satisfies `J_W⁶ = id` and commutes with `f`, all through degree 6 | pass |
| P2 | `𝒥_{≤6}(h_6⁻¹ J_W h_6) = A`: the generator is linear in the NF chart through degree 6 | pass. The scope draft derived this from the owner's uniqueness clause; here it is computed directly |
| P4 | quadratic part of `J_W` equals `δ_2 = (1+i√3)/12 · W² − (1−i√3)/6 · W W̄ − (1/6) W̄²` | pass |
| **C0-0 … C0-4** | passive transport, both directions (NF → W and W → NF), with the fibre trivialization fixed and with a nonconstant fibre re-trivialization `g(x)`: the transported model reproduces the fibre observable after 1, 2 and 3 steps | pass |
| CONTROL-C0-5 | the *section-form* rule `s̃ = g(x)·s(x)` is detected as wrong for nonconstant `g` | pass (detected). The rule that works is the update form `s̃ = g(b(x))·s(x)`, `g` taken at the image point |
| CONTROL-C0-6 | re-imposing `Λ W̄` in the raw frame differs from the transported NF-native source at degree 2 | pass (detected) |
| **A1** | C1, `s(z) = Λ z̄` in the NF chart, is covariant under the generator through degree 6 with the constant fibre action `λ̄` | pass |
| **A2**, A2b | covariant source monomials through degree 6 are exactly `z̄`, `z z̄²`, `z² z̄³` and `z⁵`; covariant degrees are 1, 3, 5; `z̄` is the only degree-1 member | pass. R1's weight statement is recovered without its missing certificate |
| **A3** | two tangent-to-identity maps commuting with `A` (`ψ = z + c_21 z²z̄ + …`): the source stays in the weight class, its degree-1 coefficient is unchanged, its cubic member becomes `−conj(c_21) ≠ 0` | pass |
| Q1–Q3 | with `q = z + j y`, `j a = ā j` and ℤ₆ acting by left multiplication by `λ`: the `j`-component has weight −1; `H = jΛz̄` on `Π_∥` satisfies `H(λz) = λ H(z)`; the word `q jΛ q̄ q` is equivariant for general `q` and gives `jΛ z z̄²` on `Π_∥` | pass |
| CONTROL-Q4 | the full-space linear word `jΛq̄` is not equivariant off `Π_∥` | pass (detected): the minimal coupling is a statement on `Π_∥` |
| **A1′**, A1′b | C2, `s(W) = Λ W̄` in the raw frame, with the same constant fibre action: the covariance defect is `Λ·conj(δ_2)` at degree 2 and is nonzero at every degree 2 to 6 (3, 4, 5, 6, 7 nonzero coefficients) | pass: **C2 is not covariant** under that action |
| P3 | `s_C1` written in the raw frame minus `s_C2` equals `−Λ·conj(h_2(W, W̄))` at degree 2 | pass |
| C2a-1 | the `W²` coefficient of the degree-2 defect is `−1/6 ≠ 0`, so defect / `W̄` is not differentiable at 0: no `C¹` complex-scalar fibre action absorbs it | pass |
| C2a-2 | a real-linear state-dependent repair `s ↦ α(W)s + β(W)s̄` removes the covariance defect through degree 2 | pass (explicit `α`, `β` in the output). **Requalified (revision 2):** a pointwise repair of covariance, with the action taken at the source point. It does not check the ℤ₆ composition law, the update form or the restoring block, so it is not a ℤ₆ action. Exploratory `[SESSION]` algebra |
| C2a-3 | a real-linear state-dependent re-trivialization carries C1, written in the raw frame, onto C2 through degree 2 | pass (explicit map in the output). **Requalified (revision 2):** this is a *source-section match* with the gauge evaluated at the source point, not an update conjugacy. Superseded in strength by the all-order construction in §4 S4(a). Exploratory `[SESSION]` algebra |
| CONTROL-P2 | a perturbed `h_2` coefficient makes the generator nonlinear in that chart | pass (detected) |

C2a-1 to C2a-3 go one step beyond A1′. They were added because the scope's deliverable (c), the separation of C1, C2a and C2b, cannot be stated without them; they are degree-2 algebra of the same kind and are offered for review as such.

---

## 4. What the results say

`[SESSION: ALG]`, finite jets through degree 6 (degree 2 where stated), conditional on the stipulations of §5.

**S1.** In the NF chart, with a constant complex fibre action, the NF-native source is covariant under the dyad's intrinsic ℤ₆ generator through degree 6. The covariant class through that degree is spanned by `z̄`, `z z̄²`, `z² z̄³`, `z⁵`.

**S2.** Within that class only the degree-1 coefficient is fixed. A normalizer change that respects the symmetry moves the cubic member. "Minimal coupling with no cubic member" is a convention, not a model property.

**S3.** The W-native source with the same constant action is not covariant, at any degree from 2 to 6. Read as C2b, it is a source that does not respect the dyad's ℤ₆ symmetry; in one trivialization it differs from C1 by `−Λ·conj(h_2)` at degree 2.

**S4 — three levels, kept apart** (revision 2, after the second co-owner's review).

(a) *Source-section match.* Let `V(W) = Λ·conj(h_6⁻¹(W))` (C1 written in the raw frame) and `U(W) = Λ W̄` (C2), with `Λ ≠ 0`, both read as real maps of `ℝ²` on the disk where `DYAD-THM-NF-INV` gives an analytic inverse. Both vanish at 0 and have the same invertible real derivative `A`. With `B(W) = ∫₀¹ DV(tW) dt` and `Γ(W) = A B(W)⁻¹`, one has `V(W) = B(W)W` and hence `Γ(W)V(W) = U(W)` exactly, on a neighbourhood where `B(W)` is invertible. `[SESSION: THM, conditional on that domain and Λ ≠ 0]` — the second co-owner's construction, checked by its implementation through degree 6; the argument checked by hand here. The same argument relates **any** two source germs `V`, `U` that vanish at 0 and share an invertible real derivative: with `B_V(W) = ∫₀¹ DV(tW) dt` and `C(W) = ∫₀¹ DU(tW) dt` one has `V = B_V W`, `U = C W`, and `Γ = C B_V⁻¹` gives `ΓV = U`, with `Γ(0) = I` (the general form is the second co-owner's; the display above is the case `C = A`). This is a local analytic-germ statement, not a jet identity; its domain is qualitative and it carries no new radius and no physical-fibre evidence. So under unrestricted local `GL₂(ℝ)` gauges, section-level comparison carries no information, at any order. C2a-3 is the degree-2 instance. No `C¹` complex-scalar gauge does this: the `W²` coefficient of `V − U` is `−Λ(1+i√3)/24 ≠ 0` (P3; asserted independently in the reviewer's script), so `U/V` is not `C¹` at 0.

(b) *Update conjugacy.* A re-trivialization of the update acts with the fibre factor at the image point (S6), so the gauge that matches the sources is `g(Y) = Γ(f⁻¹(Y))`, giving `g(f(W))V(W) = U(W)`. The same `g` then transforms the restoring block, `M̃(W) = g(f(W)) M(W) g(W)⁻¹`, and the symmetry action, `P̃_W = g(J_W W) P_W g(W)⁻¹`. An action obtained by such a transport satisfies the ℤ₆ composition law `P_{J⁵x}⋯P_{Jx}P_x = I` to the order tested, by telescoping (with `J_W⁶ = id`). C2a-3 as computed is (a), not (b); C2a-2 is a repair, not an action of this form.

(c) *Model equivalence.* Two models are equivalent only if one admissible gauge relates source, restoring block, action and observable together. That is not established. It needs the admissible gauge group, the dual action on `Π_⊥*`, `M_spin2`, the observable and the UV dynamics.

**S5 — the conditional separation, restated.** In the model class tested:
- if admissible re-trivializations are complex-linear (structure group `GL₁(ℂ)`), C1 is ℤ₆-covariant under a constant action, C2 is not, and no admissible gauge carries one source onto the other: within that class they are different models. This is a conditional statement about the named class, not a proof of physical inequivalence;
- if `GL₂(ℝ)` gauges are admissible, the two sources are section-equivalent at all orders (S4(a)), and any distinction moves to (b)–(c): whether, under the same gauge, the restoring blocks and the actions correspond.

The structure group of the transverse bundle is therefore a necessary input. It is not sufficient to select the physical model.

**S6 — transport rule.** For `U(x, y) = (f(x), s(x) + M(x)y + O(y²))` and a re-trivialization `Ψ(x, y) = (φ(x), g(x)y)`, direct composition gives `s̃(φx) = g(fx)s(x)` and `M̃(φx) = g(fx)M(x)g(x)⁻¹`, for an arbitrary real-linear `M` (the second co-owner's general statement; checked by hand). The certificate tested this rule in a one-complex-dimensional fibre with scalar `M` (C0-1 to C0-4) and showed the source-point rule to be wrong (CONTROL-C0-5). A symmetry lift `𝒥(x, y) = (Jx, P_x y)` commutes with the update iff `fJ = Jf`, `s(Jx) = P_{fx}s(x)` and `M(Jx)P_x = P_{fx}M(x)`. Stage 1 tested the first two with constant `P`; the condition on `M` is untested, because `M_spin2` has not been typed.

**A side observation from A2.** The degree-5 members are two: `z² z̄³` and `z⁵`. The second is covariant under ℤ₆ but would not be under a continuous phase symmetry. v0.7.1 R1 names the degrees and the degree-1 and degree-3 members only.

---

## 5. Limits

- **Finite jets.** The 39 certificate checks are identities of polynomials truncated at degree 6: for them there is no convergence, no domain, no radius and no remainder bound. The exception is S4(a), a local analytic-germ statement conditional on the analytic inverse of `DYAD-THM-NF-INV`; it has a qualitative local domain and no numerical radius.
- **Stipulations, not owner facts:** the constant fibre action `λ̄`; the quaternion convention `q = z + j y`, `j a = ā j` with ℤ₆ acting by left multiplication. The convention is reconstructed from three relations in the v0.7.1 text (`j`-component weight −1; `ja = āj`; `yk = kȳ`); it cannot be compared with `single_sandwich_dichotomy_certificate.py` or `uvjet_equivariant_classification.py`, which are missing.
- **Scope acceptance, A1/A2.** The scope asked for these "with the quaternionic ordering and the covector typing written out". The ordering is written out (Q1–Q3). The **covector typing is not exercised**: the certificate works in the update form, where the transverse block is a vector in `Π_⊥`. Hypothesis H7 of the scope draft stays open.
- **A3** verifies two explicit instances and one formula; it is not a classification of the centralizer.
- **C2a** is degree-2 algebra only.
- **C0** uses a one-complex-dimensional fibre with complex-scalar `m` and `g`. It is an implementation control of the transport rule in that class.
- `Λ = 1` in A1, A1′, P3: those statements are linear in `Λ`.
- **C2a-2 and C2a-3** exceed the authorized C0 / C1 / A1′ task; they are kept as exploratory `[SESSION]` algebra, as the second co-owner recommends, pending any PI decision on scientific use.
- **S4(a)** is a local statement on the analytic-inverse disk; it says nothing about the update, the restoring block or physics.
- Not touched: `M_spin2`, the anisotropy `w`, any norm, `0.024`, `4/125`, R15, any physical observable, the historical `1.006×10⁻²` envelope.

---

## 6. UVM proposal for `J_⊥` and the bundle typing — for Genesis review

Under PI decision 3. **A proposal, not adopted**; identifier for discussion only: `UVM-PROP-JPERP-01`.

| # | Proposed | Basis | Open for Genesis |
|---|---|---|---|
| JP1 | UV space `ℍ ∋ q = z + j y` with `j a = ā j`; `Π_∥ = {y = 0}`; `Π_⊥` is the `j`-component | reconstruction from v0.7.1 R1, R3, R10; checks Q1–Q3 show it is a *consistent stipulated model* | is this the embedding the harness `T_ℍ^UV` uses? Genesis has not adopted it |
| JP2 | the base coordinate `z` is a ℤ₆-equivariant dyad chart, **named at each claim**: the NF chart `W = h_6(z)` (linearizes the generator through degree 6 only; P2) or the smooth chart `Φ` of `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (exact, `C^∞` only, qualitative radius) | P2; Dyadic §6.17 | the two charts need not coincide; to the order where both linearize the generator they differ by an `A`-equivariant centralizer change, which moves the higher tower members (A3). `h_6` is not an all-order symmetry statement |
| JP3 | the symmetry lifts as left multiplication by `λ` in that chart. On the **vector** fibre `Π_⊥` this gives the constant complex-linear action `P = λ̄`, which satisfies the composition law `P⁶ = I` | Q1; A1 | does the harness commute with this lift, or with another one? |
| JP4 | covariance in the update form, all three conditions of S6: `fJ = Jf`, `s(Jx) = P_{fx}s(x)`, `M(Jx)P_x = P_{fx}M(x)`; any state-dependent `P` must satisfy `P_{J⁵x}⋯P_x = I` | S6, S4(b) | — |
| JP5 | structure group `GL₁(ℂ)`: admissible re-trivializations are complex-linear | S4, S5: without a restriction the NF/W distinction is empty at section level | **a physical hypothesis**, not a consequence of the jet calculation. What justifies a rigid complex structure on `Π_⊥`? Genesis / PI |
| JP6 | the covector side, `[SESSION: ALG]`, not certified. The source takes values in `Π_⊥*`, on which the stipulated vector-fibre representation `P` induces the contragredient `P^∨ = (P⁻¹)ᵀ`. Given a separately chosen symmetric positive-definite lowering `B: Π_⊥ → Π_⊥*`, lowering is ℤ₆-equivariant iff `BP = P^∨B`, i.e. `PᵀBP = B`, **with `P` and `B` written in corresponding bases**. Sanity check in the primitive frame, re-verified exactly here: with `B = [[1, −1/2], [−1/2, 1]]` (`GEN-DEF-PRIMITIVE-METRIC`), `A = [[1, −1], [1, 0]]` (linear part of `T` in `(ρ, η)`) and `P = A⁻¹ = [[0, 1], [−1, 1]]`, one has `PᵀBP = B`; in the complex `W` chart the metric is `I` and `P` is multiplication by `λ̄`. Mixing `P_W` with the primitive array `B_{ρη}` would fail spuriously. This checks consistency in a **stipulated** shared metric; the primitive metric is not automatically a metric on the transverse fibre. With the input representation and the contragredient output representation fixed, the degree-1 intertwiners form **one complex monomial with a free complex coefficient**, a two-real-dimensional space, not a unique map; changing the complex orientation of the target changes the words "antilinear / linear", not that space. Without the physical lift, "order-six rotation" does not establish R1's physical source type | scope H7; `GEN-OPEN-SOURCE-PAIRING`; `GEN-DEF-PRIMITIVE-METRIC` | which `B` acts on `Π_⊥`, and in which basis; is the lifted action `B`-orthogonal there; vector or contragredient action on the source? |
| JP7 | clock: primitive `T` | RRF §6.2 | — |

Consequence if JP1–JP5 were accepted: C1 would be the covariant model, C2 would be C2b (a source breaking ℤ₆), and the question "which is physical" would become "does the UV source respect the dyad's ℤ₆ symmetry". That is a hypothesis to be stated, not a result.

No item has been placed in `pipes/GEN/`. The request to Genesis is prepared only after the second co-owner has checked this record.

---

## 7. Reproduction

```bash
# from a checkout of branch claude/uvm-open-m6-stage1
python3 -I evidence/uvm/scripts/uvm_open_m6_stage1_jet_cert.py --json /tmp/m6_results.json > /tmp/m6_stdout.txt; echo "exit=$?"
sha256sum /tmp/m6_stdout.txt /tmp/m6_results.json
# expected: exit=0
#   60bdac3156661ba1d91ec1c79a8b12dfc949aa82f9855fe7ceab4f9b3fa8e544  stdout
#   507479c8a0492b6ff339bb733fd5e853df7133c637d29e31c37cab030b771087  results.json
```

Byte-identical output on another machine confirms the run, not the mathematics. An independent check means a second implementation, or a hand derivation, of at least P2, A1′ (the degree-2 defect) and C2a-1.

---

## 8. Second co-owner's review and what it settled

Review `6019523031` (23 November 2026 09:55 UTC, on `06f4545`), verdict ACCEPT WITH SCOPED CHANGES:

| Question put in revision 1 | Answer |
|---|---|
| reproduce E1–E6, P2, A1′ at degree 2, P3, C2a-1 | done with a separate implementation; all pass; also A2, G0–G6 and A1′ at degrees 2–6 (§2) |
| is S5 stated correctly | partly: section match, update conjugacy and model equivalence had to be separated, and the structure group is necessary but not sufficient (S4, S5 now) |
| does C2a survive beyond degree 2 | as a section match, yes, at all orders, under unrestricted `GL₂(ℝ)` gauge (S4(a)); as an update conjugacy only with the image-point gauge, and as a model equivalence not shown |
| does the update form need a real two-dimensional fibre | not for the algebra: S6 holds for arbitrary real-linear `M`; the physical `Π_⊥*` interface still needs real matrix notation |
| review the `J_⊥` proposal before Genesis | guards added: stipulated model (JP1), chart named per claim (JP2), vector-fibre action and composition law (JP3, JP4), structure group as a physical hypothesis (JP5), dual action and lowering (JP6) |

## 9. Revision record

| Review item | Change | Where |
|---|---|---|
| R1 | C2a-2 and C2a-3 requalified (repair; source-section match at the source point); S4 split into section match, update conjugacy, model equivalence; S5 restated as conditional on the model class | §3, §4 |
| R2 | the reviewer's local `GL₂(ℝ)` construction recorded as a conditional finding with its domain; consequence stated: section-level comparison carries no information under that gauge class | §4 S4(a) |
| R3 | composition law, dual action on `Π_⊥*`, chart named per claim, structure group as physical hypothesis | §6 JP1–JP6 |
| other | S6 stated for real-linear `M`, with the update-form condition on `M` marked untested; independent reproduction and its files recorded | §2, §4 S6 |
| readback R1 (`6020412456`) | JP6: contragredient `P^∨`, `BP = P^∨B ⟺ PᵀBP = B` in corresponding bases, the primitive-frame sanity check (re-verified), the two-real-dimensional degree-1 intertwiner space, the missing physical lift | §6 JP6 |
| readback R2 | §5 "finite jets" limited to the 39 checks; S4(a) given its general form `Γ = C B_V⁻¹` and stated as a local analytic-germ result with qualitative domain | §4 S4(a), §5 |

Not changed: the certificate, its output and hashes, every numerical result. No new certificate run.

The second co-owner's readback `6020412456` (23 November 2026 10:56 UTC, on `a25244e`) found R1–R3 resolved and asked for the two documentation corrections above; with them it gives Stage 1 ACCEPT SCOPED at `[SESSION]` grade and clears `UVM-PROP-JPERP-01` to go to Genesis as a proposal and review request. The `pipes/GEN/` item is filed separately (its own PR); it adopts nothing.

*End of record. No UVM statement, pin, grade or pipe state is changed by it.*
