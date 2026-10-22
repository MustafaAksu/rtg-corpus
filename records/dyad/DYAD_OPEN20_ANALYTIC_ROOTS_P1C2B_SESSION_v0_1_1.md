# DYAD OPEN 20 / O20-an — P1-c-2b: Gevrey class of the formal curves φ± (Baldomá–Fontich–Martín), complex-extension audit, and status of the López-Hernanz (2012) questions (SESSION v0.1.1)

**Version:** v0.1.1 · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Supersedes:** v0.1 (`9e15d23a…699f14`). v0.1 is not modified.

**Review of v0.1:** `P1-c-2b PARTIAL REVIEW ACCEPT — COMPLEX EXTENSION AUDIT REQUIRED`. The exact algebra (B1–B4) was accepted. Three changes were asked for:
- R1: complete the complex-coefficient audit of BFM Lemma 6.1 and Lemma 6.5;
- R2: record Theorem 3.1 → Remark 3.7 → φ± as one short proof chain;
- R3: narrow the finite-jet reading of BFM Proposition 3.8.

**What changed from v0.1:** §2.2 (new gates L1–L3 and control M4), §3 (audit and proof chain, replacing the v0.1 provenance limit), §4.2 (narrowed wording), and the status lines. §1, §2.1 and §5 are unchanged in substance.

**Status.**
- `[SESSION]` record. Nothing is adopted.
- DYAD v6.4.18 is unchanged; OPEN 20 PARTIAL; B-an and B-6 OPEN.
- Convergence and divergence of φ± are both OPEN.
- P1-c-5d and P1-c-6 have not been run.

**Check script.** `dyad_open20_an_p1c2b_check_v0_1_1.py`, with helpers `qw.py`, `fzw.py` and `ext.py` (unchanged). It writes `p1c2b_check_v0_1_1.json` (byte-deterministic; verified by rerun) and `p1c2b_perf_v0_1_1.json` (timings only).
- 7 gates (B1–B4, L1–L3) and 4 negative controls (M1–M4).
- Runs in about 2 s.
- Arithmetic is exact in E = ℚ(ω)[a]/(Aa² + Ba + C), with ω = i√3 and a = a₂ either root; statements hold for Γ₊ and Γ₋ at once. L3 is a 50-digit numerical sanity check.

**Scope qualifications carried over from the P1-c-2 review.**
- "Exactly three" parabolic curves refers only to the orbit classes asymptotic to a given Γ±.
- The formal distinctness of Γ₊ and Γ₋ implies nothing about separate real carriers.

## 1. Source

[BFM] I. Baldomá, E. Fontich, P. Martín, *Discrete Contin. Dyn. Syst.* 37(8) (2017) 4159–4190, DOI 10.3934/dcds.2017177.
- Read as arXiv:1702.05961v1; PDF SHA-256 `94913000dd8983037f7c4805b748b2ec96ca2d02d80bbbc2f93892b635516a09`.
- Found through reference [1] of Carrillo–Lastra, *Math. Ann.* 386 (2023) 85–112. Two downloads of that paper were supplied by the PI; their text is identical apart from page headers. Carrillo–Lastra's own results, on finite-order singular PDEs, do not apply to the invariance equation of φ.

**Statements used:** form (3) (here d = 1, d′ = 0), Theorem 3.1, Proposition 5.1, Lemmas 6.1–6.5, Proposition 6.6, Remark 3.7, Proposition 3.8 and Claim 4.2, as summarized in v0.1 §1.

## 2. Exact hypothesis check

### 2.1 Form (3)

Gates B1–B4, unchanged from v0.1.

**Chart.**
- Blow up once: w = x·w₁.
- Set y = w₁ − J₆(φ/x).

**Results.**
- **N = M = 4** and a = −ℓ.
- f₄ = μx³y.
- g₄ = (μ̄ − μ)x²y², with zero x⁴ coefficient.
- B₁ = ℓ(k* − 1).
- −B₁/a = k* − 1 = −83/19 − (16/19)ω is non-real, so B₁ + la ≠ 0 for every l ≥ 2. Hence γ = 1/3.
- The strict transform of Γ is y = O(x⁷) (B4).

**Controls.**
- M1: form (3) fails in (z, w).
- M2: without the jet, the x⁴ coefficient of y∘F is c̄₀₅ ≠ 0.
- M3: a planted resonance is detected.

### 2.2 BFM Lemma 6.1 for this F, proved directly (R1)

`[ALG]`, gates L1 and L2.

BFM state Lemma 6.1 without proof ("cumbersome but straightforward computations"). It is replaced here by a proof for our F.

**Step 1: the change of variables reduces to a change of x only.** In our chart, K^y_l = 0 for l ≤ 6 (B4). So the Lemma 6.1 change Φ(x̄, ȳ) = K_{≤3}(x̄) + (0, ȳ) is Φ(x̄, ȳ) = (h(x̄), ȳ) with

h(t) = t + k₂t² + k₃t³.

Here k₂ and k₃ are the unique solutions of g∘h = h∘R through order t⁶, where g(x) = x∘F(x, 0) and R = t − at⁴ + bt⁷. They are exactly the Proposition 5.1 values K^x_2 and K^x_3, since those are forced (l ≠ N).
- Exactly: k₂ = −(1 + ω)/12 and k₃ = (1 + ω)/54 − a/3.
- Gate L2: the residual g(h(t)) − h(R(t)) vanishes through t⁶.

**Step 2: Lemma 6.1(1).** F̄ = Φ⁻¹∘F∘Φ is computed exactly through total degree 6, with h⁻¹ the formal inverse.
- Gate L1: F̄ is in form (3) with the same N = M = 4, a, v (= μ) and B₁, the same g₄, and zero y-free part through degree 6.
- Form (3) constrains only the jet of degree ≤ max(N, M) = 4, so this finite check proves (1) completely.
- Control M4: with the wrong change (h(x̄), ȳ + x̄), the predicate fails.

**Step 3: Lemma 6.1(2).** Let K̂ be the Proposition 5.1 solution for F. Then K̄ := Φ⁻¹∘K̂ = (h⁻¹(K̂^x(t)), K̂^y(t)) solves F̄∘K̄ = K̄∘R with the same R. Since K̂^x = h + O(t⁴) and K̂^y = O(t⁷), K̄ = (t, 0) + O(t⁴). By Proposition 5.1 uniqueness (for the given c = K̄^x_4), it is the solution that §6 estimates.

**Step 4: Lemma 6.1(3).** K̂ = Φ∘K̄ with Φ polynomial. The Gevrey-s classes are closed under sums and products, by the elementary inequality

Σ_{i+j=n} (i!)^s (j!)^s ≤ (n + 1)(n!)^s,

and the factor (n + 1) is absorbed into the geometric constant. So K̄ γ-Gevrey implies K̂ γ-Gevrey.

### 2.3 The rest of BFM §6 read for complex coefficients (R1)

`[LIT]`, owner audit.

| Item | Content | Complex validity |
|---|---|---|
| Prop. 5.1 | Recursion for K_l, R_l. Uses field operations, a(l − N) ≠ 0 and invertibility of B₁ + la | valid over ℂ |
| Lemma 6.2 | Rescaling by real λ ≥ 1. Cauchy bounds ‖G̃_k‖ ≤ κ̃δ̃^{−k} on a complex ball (BFM already complexify). "ã ≤ ε" is the modulus bound \|λ^{−1/γ}a\| ≤ ε | valid; moduli only |
| Lemma 6.3 | ‖(B̃₁ + ãl)⁻¹‖ ≤ 2λ^{N−1}(l\|a\|)⁻¹ for l\|a\| ≥ 2‖B₁‖, a Neumann series | valid over ℂ |
| Lemma 6.4 | Coefficients of R̃^k, bounded by the triangle inequality with \|ã\| and \|b̃\| | valid. **Notation:** the text defines σ = ãb̃², but the proof uses \|b̃\|/\|ã\|² and states σ is independent of λ. Both fit only σ = b̃/ã² = b/a². This is a typo with no effect on the argument. |
| **Lemma 6.5** | i) M_{k,ν} ≤ (ν − k + 1)!^β N_β^{k−1}; ii) J²_{k,ν} ≤ ((N_β + 1)^k − 1)/N_β · (ν − k + 1)!^β. Read line by line: **purely combinatorial**, depending only on N, β, k, ν. It uses (a + b)! c! ≤ b! (a + c)! for b ≤ c, N!^β ≤ N^{β(N−1)}, and β(N − 1) ≥ 1 (equality here: β = 1/3, N = 4). | independent of the field. L3 (50 digits) confirms both bounds exhaustively for N = 4, β = 1/3, k ≤ 8, ν ≤ 36 |
| Prop. 6.6 | Induction bounds for H¹–H⁸ through Lemmas 6.2–6.5. Read line by line for N = M (L = N, γ = 1/(N − 1), µ₀ = 1, no z-component). Only norms and moduli appear; no sign of a and no ordering is used | valid over ℂ |

The paper's real setting is used only in §7 (Theorem 3.3: a > 0, real-analytic sectorial solution), which is not imported.

## 3. Result and proof chain (R2)

**Consequence C4** `[THM — imported; hypotheses checked; complex-extension audit completed by the owner; SESSION, pending review]`. For both formal curves, with constants c₁, c₂:

|a_m^±| ≤ c₁ c₂^m (m!)^{1/3}  for all m.

**Proof chain.**
1. **Form (3).** In the chart (x, y), F has form (3) with N = M = 4, a = −ℓ, B₁ = ℓ(k* − 1), and B₁ + la ≠ 0 for every l ≥ 2. (B1–B3, exact.)
2. **Lemma 6.1, case-specific.** Φ = (h, id) puts F̄ in form (3) with the same data. The Proposition 5.1 solution satisfies K̄ = (t, 0) + O(t⁴). Gevrey class is the same for K̂ and K̄. (§2.2, L1 and L2, exact, plus the product inequality.)
3. **Proposition 6.6** (Lemmas 6.2–6.5, valid over ℂ by §2.3). K̄ is γ-Gevrey with γ = 1/(N − 1) = 1/3. Hence K̂ = Φ∘K̄ is 1/3-Gevrey.
4. **Remark 3.7, formal level.** The invariant graph is Φ̂ = K̂^y∘(K̂^x)⁻¹, and it is 1/3-Gevrey. This step uses that a Gevrey-s series t + O(t²) has a Gevrey-s formal inverse and that Gevrey-s classes are closed under composition. BFM use this fact in Remark 3.7 ("its inverse is Gevrey"). It is a standard property of formal Gevrey classes and is **not re-proved here**; this is the one remaining imported auxiliary fact.
5. **Identification.** Φ̂ = O(x²) gives the smooth formal curve w = x(J₆ + Φ̂) = a₂x² + …, tangent to [1:0] with the same a₂. All coefficients a_k (k ≥ 3) are forced (P1-c-5: L_k = ℓ(k* − k) ≠ 0). So x(J₆ + Φ̂) = φ±.
6. **Conclusion.** φ± = x·(J₆ + Φ̂). Multiplying by polynomials preserves the class, so φ± is 1/3-Gevrey. ∎

**Reading.** This is an **upper bound** only. BFM give no lower bounds ("remains open"), and C4 is compatible with φ± being convergent. The P1-c-5 numerics (m ≤ 37) do not contradict it.

## 4. What C4 does not decide

### 4.1 BFM Theorem 3.3 (not imported)

- It requires real a > 0, and its adaptation to our complex setting has not been checked.
- Its sectors have opening < π/3. For Gevrey-1/3 asymptotics, Watson-type uniqueness needs opening > π/3. So it would not give summability or uniqueness of sectorial curves in any case.
- The existence of the parabolic curves asymptotic to Γ± is already covered by C2 (P1-c-2, [LRRS]).

### 4.2 BFM Proposition 3.8: narrowed reading (R3)

`[LIT]`. The two statements must be kept apart.

- **What is proved.** For every p there is an analytic map G that agrees with F to order p and has an invariant graph with the same p-jet as φ which is convergent (a polynomial). Hence **no general criterion based only on a finite Taylor jet of F can force divergence of the invariant curve.**
- **What is not claimed.** That no finite computation can be useful for DYAD's particular F. Finite computations can still be decisive when combined with structural identities proved for the whole map. The v0.1 sentence "No finite computation decides divergence" is withdrawn and replaced by the first bullet.
- **Consequence for P1-c-5d.** Coefficient or Stokes-gap numerics can serve as `[NUM]` indicators. A proof would have to combine them with a statement about the full map.

## 5. The four questions of the P1-c-2 review

[L12], *ETDS* 32 (2012) 211–221, DOI 10.1017/S0143385710000805, is closed-access:
- no open-access copy is listed by Semantic Scholar or OpenAlex;
- no arXiv version was found.

The PI has been asked to supply the PDF.

| Question | Status |
|---|---|
| 1. Γ± and the hypotheses of [L12] | **Partly.** [L12]'s notion of a Briot–Bouquet (strong) separatrix is quoted with attribution in Cano–Corral–Mol (arXiv:1508.06882, §2): the trace point after reduction is complex-hyperbolic or a badly oriented saddle-node. Γ± is complex-hyperbolic (P1-c-2 K7). [L12]'s technical hypotheses and the formal case need the full text. |
| 2. Summability level vs Gevrey-1/3 | Gevrey part: upper bound 1/3 (C4, §3). Summability and its level: OPEN. |
| 3. Comparable attracting/repelling sectorial sums | OPEN. |
| 4. Exact conditions under which a zero difference implies convergence | OPEN. |

The P1-c-5d Stokes-gap campaign remains **not approved**.

**Bibliographic completion** for P1-c-2: [LS] = L. López-Hernanz, F. Sanz Sánchez, *J. reine angew. Math.* 739 (2018) 277–296.

## 6. Status

| Item | Status |
|---|---|
| φ± Gevrey-1/3 upper bound (C4) | imported; owner complex-extension audit complete (§2.2–2.3); one standard auxiliary fact (Gevrey inversion and composition) cited, not re-proved; pending review |
| Lower bounds / divergence of φ± | OPEN; no finite-jet criterion can force divergence (§4.2) |
| [L12] questions 1–4 | Q1 partly; Q2 Gevrey part answered; the rest OPEN (full text needed) |
| B-an, B-6 | OPEN |

**Unchanged:** DYAD v6.4.18 adopted; OPEN 20 PARTIAL. No owner adoption; everything above is SESSION material.

## 7. Reproduction

- **Files:** `dyad_open20_an_p1c2b_check_v0_1_1.py`, `qw.py`, `fzw.py`, `ext.py`, `p1c2b_check_v0_1_1.json`, `p1c2b_perf_v0_1_1.json`, `SHA256SUMS.txt`.
- **Command:** `python3 dyad_open20_an_p1c2b_check_v0_1_1.py`. Expected output: `RESULT: PASS`, with B1–B4 and L1–L3 true and M1–M4 false.
- **Checker SHA-256:** `1aa66da0ea36b48f23461b79a9625a691ed21f8d0b5d1105ec67c3886f26e57f`.
- **`p1c2b_check_v0_1_1.json` SHA-256:** `cf5c219c278aec4d468a931d7c78cffcb917be35c0da429eb182a4d3aee3acdf`.
- The v0.1 checker and JSON (`451024…badb5e`, `a068da…0f45e2`) remain valid for gates B1–B4.
