# OPEN M (UVM) — OPEN-M-6 Stage 1: Jet-Covariance Results

**Status:** [SESSION] / NONCANONICAL. Results of the bounded jet algebra the PI authorized on 23 November 2026. They are finite-jet identities with a filed script and output. Nothing here is adopted UVM science, edits the DSN, registers an RRF profile, or selects a carrier, lowering or normalization. **Independent reproduction by the second co-owner is pending**; until then every result below is `EV-CODE`, `EV-RUN` of one session.
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
| C2a-2 | a real-linear state-dependent action `s ↦ α(W)s + β(W)s̄` absorbs the defect through degree 2 | pass (explicit `α`, `β` in the output) |
| C2a-3 | a real-linear state-dependent re-trivialization carries C1, written in the raw frame, onto C2 through degree 2 | pass (explicit map in the output) |
| CONTROL-P2 | a perturbed `h_2` coefficient makes the generator nonlinear in that chart | pass (detected) |

C2a-1 to C2a-3 go one step beyond A1′. They were added because the scope's deliverable (c), the separation of C1, C2a and C2b, cannot be stated without them; they are degree-2 algebra of the same kind and are offered for review as such.

---

## 4. What the results say

`[SESSION: ALG]`, finite jets through degree 6 (degree 2 where stated), conditional on the stipulations of §5.

**S1.** In the NF chart, with a constant complex fibre action, the NF-native source is covariant under the dyad's intrinsic ℤ₆ generator through degree 6. The covariant class through that degree is spanned by `z̄`, `z z̄²`, `z² z̄³`, `z⁵`.

**S2.** Within that class only the degree-1 coefficient is fixed. A normalizer change that respects the symmetry moves the cubic member. "Minimal coupling with no cubic member" is a convention, not a model property.

**S3.** The W-native source with the same constant action is not covariant, at any degree from 2 to 6. Read as C2b, it is a source that does not respect the dyad's ℤ₆ symmetry; in one trivialization it differs from C1 by `−Λ·conj(h_2)` at degree 2.

**S4.** No differentiable complex-scalar fibre action repairs that. A real-linear, state-dependent one does — and then, at degree 2, C2a is C1 in another trivialization.

**S5 — the conditional separation.** Whether C1 and C2 are two models or one is therefore not a property of the source. It is exactly as strong as the restriction placed on fibre trivializations:
- if the transverse fibre carries a rigid complex structure, so that only complex-linear re-trivializations are admissible, C1 and C2 are different models and only C1 is ℤ₆-covariant;
- if arbitrary real-linear, state-dependent re-trivializations are admissible, the two cannot be told apart at the order tested.

The first physical input C3 needs is thus identified: **the structure group of the transverse bundle**. This is what the `J_⊥` proposal in §6 has to fix.

**S6.** In the model class tested (an update whose transverse part is `s(x) + m(x)y`), the transport rule that reproduces the observable takes the fibre factor at the image point. By the same algebra the covariance equation is the update form `H(J_ℤ6 x) = J_⊥(Tx)H(x)`, not the section form; they coincide for a constant action. The certificate tests the re-trivialization rule; the covariance form is the hand derivation of the scope draft §5.

**A side observation from A2.** The degree-5 members are two: `z² z̄³` and `z⁵`. The second is covariant under ℤ₆ but would not be under a continuous phase symmetry. v0.7.1 R1 names the degrees and the degree-1 and degree-3 members only.

---

## 5. Limits

- **Finite jets.** Everything is an identity of polynomials truncated at degree 6. No convergence, no domain, no radius, no remainder bound.
- **Stipulations, not owner facts:** the constant fibre action `λ̄`; the quaternion convention `q = z + j y`, `j a = ā j` with ℤ₆ acting by left multiplication. The convention is reconstructed from three relations in the v0.7.1 text (`j`-component weight −1; `ja = āj`; `yk = kȳ`); it cannot be compared with `single_sandwich_dichotomy_certificate.py` or `uvjet_equivariant_classification.py`, which are missing.
- **Scope acceptance, A1/A2.** The scope asked for these "with the quaternionic ordering and the covector typing written out". The ordering is written out (Q1–Q3). The **covector typing is not exercised**: the certificate works in the update form, where the transverse block is a vector in `Π_⊥`. Hypothesis H7 of the scope draft stays open.
- **A3** verifies two explicit instances and one formula; it is not a classification of the centralizer.
- **C2a** is degree-2 algebra only.
- **C0** uses a one-complex-dimensional fibre with complex-scalar `m` and `g`. It is an implementation control of the transport rule in that class.
- `Λ = 1` in A1, A1′, P3: those statements are linear in `Λ`.
- Not touched: `M_spin2`, the anisotropy `w`, any norm, `0.024`, `4/125`, R15, any physical observable, the historical `1.006×10⁻²` envelope.

---

## 6. UVM proposal for `J_⊥` and the bundle typing — for Genesis review

Under PI decision 3. **A proposal, not adopted**; identifier for discussion only: `UVM-PROP-JPERP-01`.

| # | Proposed | Basis | Open for Genesis |
|---|---|---|---|
| JP1 | UV space `ℍ ∋ q = z + j y` with `j a = ā j`; `Π_∥ = {y = 0}`; `Π_⊥` is the `j`-component | reconstruction from v0.7.1 R1, R3, R10; checks Q1–Q3 | is this the embedding the harness `T_ℍ^UV` uses? |
| JP2 | the base coordinate `z` is a ℤ₆-equivariant dyad chart: the NF chart through degree 6, or the smooth chart `Φ` of `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` exactly (`C^∞` only) | P2; Dyadic §6.17 | — |
| JP3 | the symmetry lifts as left multiplication by `λ` in that chart, so `J_⊥` is multiplication by `λ̄` on `y`: constant and complex-linear | Q1; A1 | does the harness commute with this lift, or with another one? |
| JP4 | covariance is imposed in the update form: `T_ℍ^UV∘J_ℍ = J_ℍ∘T_ℍ^UV` | S6 | — |
| JP5 | admissible fibre re-trivializations are complex-linear; real-linear state-dependent ones are not gauge | S4, S5: without this the NF/W distinction is empty | is a rigid complex structure on `Π_⊥` physically justified, and by what? |
| JP6 | the covector side: left open | scope hypothesis H7 | which pairing identifies the action on `Π_⊥*`; is the left action `B`-orthogonal; does the conditional lowering `S_f = Bc_f` commute with it? |
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

## 8. Asked of the second co-owner

1. Reproduce independently: E1–E6 against Dyadic, P2, A1′ at degree 2, P3, C2a-1.
2. Is S5 stated correctly — in particular, is "structure group of the transverse bundle" the right name for what is missing?
3. C2a-3 shows equivalence at degree 2 only. Is there an obstruction at higher degree that would make C2a a genuine rival after all?
4. Is the update form (S6) established widely enough by a one-dimensional complex fibre, or does it need the real two-dimensional fibre with a real-linear `m`?
5. Check `UVM-PROP-JPERP-01` before it goes to Genesis: anything mis-stated, anything missing.

*End of record. No UVM statement, pin, grade or pipe state is changed by it.*
