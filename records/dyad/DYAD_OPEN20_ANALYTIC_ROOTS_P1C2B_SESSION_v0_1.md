# DYAD OPEN 20 / O20-an — P1-c-2b: Gevrey class of the formal curves φ± (Baldomá–Fontich–Martín), and status of the López-Hernanz (2012) questions (SESSION v0.1)

**Version:** v0.1 · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Basis.** P1-c-2 SESSION v0.1 (`7e7aa09f…8788`), reviewed as `SCIENTIFIC REVIEW ACCEPTED — WITH TWO SCOPE QUALIFICATIONS`, which authorized P1-c-2b. P1-c-2b was scoped as a reading of López-Hernanz (2012) against four questions. That paper turned out to be closed-access (§4). While searching for it, the PI and the owner found Baldomá–Fontich–Martín (2017). The PI approved checking it here ("Önerini uygulayalım", 20 Oct 2026).

**Status.**
- `[SESSION]` record. Nothing is adopted.
- DYAD v6.4.18 is unchanged; OPEN 20 PARTIAL; B-an and B-6 OPEN.
- Convergence and divergence of φ± are both OPEN.
- P1-c-5d and P1-c-6 have not been run.

**Check script.** `dyad_open20_an_p1c2b_check.py`, with helpers `qw.py`, `fzw.py` and `ext.py` (unchanged copies). It writes `p1c2b_check.json` (byte-deterministic; verified by rerun) and `p1c2b_perf.json` (timings only).
- 4 gates (B1–B4) and 3 negative controls (M1–M3).
- Runs in under 1 s.
- Arithmetic is exact in E = ℚ(ω)[a]/(Aa² + Ba + C), with ω = i√3 and a = a₂ either root. Every statement therefore holds for Γ₊ and Γ₋ at once.

**Scope qualifications carried over from the P1-c-2 review.**
- "Exactly three" parabolic curves refers only to the orbit classes asymptotic to a given Γ±. It is not a count of all parabolic curves at 0.
- The formal distinctness of Γ₊ and Γ₋ says nothing about separate carriers in the real DYAD dynamics.

## 1. Source

[BFM] I. Baldomá, E. Fontich, P. Martín, "Gevrey estimates for one dimensional parabolic invariant manifolds of non-hyperbolic fixed points", Discrete Contin. Dyn. Syst. 37(8) (2017) 4159–4190, DOI 10.3934/dcds.2017177.
- Read as arXiv:1702.05961v1; PDF SHA-256 `94913000dd8983037f7c4805b748b2ec96ca2d02d80bbbc2f93892b635516a09`.
- Found through reference [1] of S. A. Carrillo, A. Lastra, Math. Ann. 386 (2023) 85–112 (supplied by the PI, two copies). That paper's own results concern finite-order singular PDEs. They do not apply to the invariance equation of φ, which is a functional equation of infinite order whose shift depends on the unknown.

**Statements used** (d = 1, d′ = 0; quoted in substance, with the paper's numbering).

**Form (3):**
- x∘F = x − ax^N + f_N(x, y) + f_{≥N+1}, with a ≠ 0 and f_N homogeneous of degree N with f_N(x, 0) = 0.
- y∘F = y + x^{M−1}B₁y + g_M(x, y) + g_{≥M+1}, with g_M homogeneous of degree M, g_M(x, 0) = 0 and ∂_y g_M(x, 0) = 0.
- N, M ≥ 2; the remainders have the stated orders.

**Theorem 3.1.** Assume form (3), and for M = N assume that B₁ + la is invertible for every l ≥ 2. Then F∘K̂ = K̂∘R̂ has a formal solution, with R(t) = t − at^N + bt^{2N−1} and K̂(t) = (t, 0) + O(t²). This K̂ is γ-Gevrey, ‖K_n‖ ≤ c₁c₂ⁿ(n!)^γ, where γ = 1/(N − 1) for N ≤ M.

**Remark 3.7.** "The same happens at a formal level": the graph invariance equation F^y(x, Φ(x)) = Φ(F^x(x, Φ(x))) with Φ(0) = 0, DΦ(0) = 0 has a γ-Gevrey formal solution iff K̂ is γ-Gevrey. This uses that the formal inverse of K̂^x(t) = t + O(t²) is Gevrey of the same order.

**Proposition 3.8.** For any p there is an analytic G with G − F = O(‖·‖^{p+1}) for which the polynomial truncation φ_{≤p} is an invariant manifold. Hence lower bounds (divergence) "cannot depend on a finite number of coefficients of the Taylor expansion of F".

**Claim 4.2.** For the time-1 map of an analytic vector field of this form, the invariant graph is analytic. This is the same content as Lemma 5b-1 of P1-c-5, a third independent literature counterpart after [LS] §1.

**Theorem 3.3** (true manifold). Requires a > 0 in the paper's real setting. It gives analytic solutions on sectors S(β, ρ) of opening β < απ = π/3, which are γ-Gevrey asymptotic to K̂. It is not imported here (§3.3).

## 2. Hypothesis check

`[ALG]`, gates B1–B4.

**Chart.**
- Blow up once: w = x·w₁.
- Set y = w₁ − J₆(φ/x), with φ the P1-c-5 formal curve.
- Expand x∘F and y∘F exactly in (x, y) through total degree 6.

| Gate | Result |
|---|---|
| B1 | x∘F − x has no terms of degree 2 or 3. Its degree-4 part is ℓx⁴ + μx³y. So **N = 4**, **a = −ℓ**, f₄ = μx³y and f₄(x, 0) = 0. |
| B2 | y∘F − y has no terms of degree 2 or 3, and no linear term other than y. Its degree-4 part is B₁x³y + (μ̄ − μ)x²y², with a **zero x⁴ coefficient**. So **M = 4**, g₄ = (μ̄ − μ)x²y² satisfies g₄(x, 0) = ∂_y g₄(x, 0) = 0, and **B₁ = ℓ(k* − 1)** exactly. |
| B3 | N = M condition: −B₁/a = k* − 1 = −83/19 − (16/19)ω is non-real, so it is not an integer ≥ 2, and B₁ + la ≠ 0 for every l ≥ 2. Also ℓ ≠ 0. Hence **γ = 1/(N − 1) = 1/3**. |
| B4 | The y-free part of y∘F vanishes through degree 6: the strict transform of Γ is the graph y = O(x⁷). |
| M1 (control) | Form (3) fails in the original (z, w) coordinates, because of the degree-3 term μz²w. The test detects this. |
| M2 (control) | Without the jet subtraction, the x⁴ coefficient of y∘F equals c̄₀₅ = −61/2160 + 43ω/6480 ≠ 0, so form (3) fails. The test detects this. |
| M3 (control) | A planted resonance B₁ = 3ℓ (so B₁ + 3a = 0) is detected. |

B₁/ℓ = k* − 1 coincides with c₃/ℓ in P1-c-2 K6 (same chart). One blow-up later it becomes the Briot–Bouquet ratio λ = k* − 2 of P1-c-5.

**Identification of the BFM solution with Γ±.**
- Theorem 3.1 and Remark 3.7 (formal level) give a γ-Gevrey graph y = Φ̂(x), with Φ̂ = O(x²), invariant in this chart.
- Blowing down, it is the smooth formal curve w = x(J₆(x) + Φ̂(x)) = a₂x² + …, tangent to [1:0] with the same leading coefficient a₂.
- By P1-c-5, all coefficients a_k for k ≥ 3 are forced once a₂ is fixed (L_k = ℓ(k* − k) ≠ 0). So x(J₆ + Φ̂) = φ±.

## 3. Results

### 3.1 Consequence C4

`[THM — imported, hypotheses checked; SESSION]`. The formal invariant curves φ± are **Gevrey of order 1/3**. There are constants c₁, c₂ with

|a_m| ≤ c₁ c₂^m (m!)^{1/3}  for all m,

for both roots of the P1-c-5 quadratic. This holds because φ = x(J₆ + Φ̂), and multiplication by a polynomial preserves the class.

**Provenance limit.** [BFM] is written for real-analytic maps. Here the transformed map has complex coefficients. I read the proofs with that in mind:
- **Proposition 5.1 (formal construction).** It uses only field operations, a(l − N) ≠ 0 for l ≠ N, and invertibility of B₁ + la. It is valid over ℂ.
- **§6, Lemmas 6.2–6.4 and the induction of Proposition 6.6.** These use Cauchy bounds on a complex ball, and estimates in |a|, ‖B₁‖ and |σ|. Lemma 6.3 is a Neumann-series bound for (B₁ + al)⁻¹ when l|a| ≥ 2‖B₁‖. Lemma 6.2's "ã ≤ ε" is a consequence of |λ^{−1/γ}a| ≤ ε, i.e. a modulus bound.
- **Rest of §6.** Scanned for any use of the sign of a or of reality; none found.
- **Lemma 6.1.** This is the polynomial change of variables making K̄ = (t, 0) + O(t^N). Its proof is omitted in the paper ("cumbersome but straightforward computations"), so its complex validity is accepted on the algebraic nature of the step, without a line check.
- **Lemma 6.5.** Not read line by line.

These are the remaining owner-side limits of the import.

### 3.2 What C4 changes

- P1-c-5 §3.2 recorded Gevrey-1/3 as the growth scale of a crude majorant (`[HEUR]`; the reviewer asked that it not be read as optimal). It is now an **upper bound with a theorem behind it**. It is still only an upper bound:
  - [BFM] gives no lower bounds and states that obtaining them "remains open";
  - C4 is fully consistent with φ± being convergent.
- The P1-c-5 numerics (m ≤ 37: root tests 0.66–0.69, no Gevrey-1/3 signature) do not contradict C4.
- **No finite computation decides divergence** (Proposition 3.8, `[LIT]`, applicable by the same reading, not separately line-checked). For any p, some analytic G agrees with F to order p and has a convergent (polynomial) invariant curve with the same p-jet as φ. So convergence or divergence of φ± is not determined by any finite Taylor jet of F. This supports the reviewer's caution about numerical "zero gaps" and coefficient asymptotics: such data can only ever be indicators. A divergence proof must use the full map (for example, a Stokes constant expressed through the transcendental structure of T).

### 3.3 Not imported

- **[BFM] Theorem 3.3.**
  - Its sectors have opening < π/3. For Gevrey-1/3 asymptotics, Watson-type uniqueness needs opening > π/3. So even an adapted Theorem 3.3 would not give summability or uniqueness of the sectorial curves.
  - It is also stated for real a > 0, and the adaptation to our complex setting has not been checked.
  - The existence of the parabolic curves asymptotic to Γ± is already covered by C2 (P1-c-2, [LRRS]).

## 4. The four questions of the P1-c-2 review

**López-Hernanz (2012) full text.** [L12], ETDS 32 (2012) 211–221, DOI 10.1017/S0143385710000805, is closed-access:
- Semantic Scholar and OpenAlex report no open-access copy.
- No arXiv version was found.
- One institutional repository blocks automated access; the other holds only a different paper.

The PI has been asked to supply the PDF. Until then:

| Question | Status |
|---|---|
| 1. Does Γ± meet the hypotheses of [L12]? | **Partly.** The definition [L12] uses ("Briot–Bouquet type" or "strong" separatrix: the trace point after reduction is complex-hyperbolic or a badly oriented saddle-node) is quoted with attribution to [L12] in Cano–Corral–Mol (arXiv:1508.06882, §2, supplied by the PI). Γ± matches the complex-hyperbolic case (P1-c-2 K7: eigenvalues ℓ and λℓ, ratio non-real). That survey states the definition for convergent foliations; the formal case and [L12]'s technical hypotheses need the full text. |
| 2. Summability level, and relation to Gevrey-1/3 | **Gevrey part answered:** upper bound 1/3 (C4). Summability and its level: OPEN, needs [L12]. |
| 3. Which attracting and repelling sectorial sums are comparable on a common region | OPEN, needs [L12]. |
| 4. Under which exact conditions a zero difference implies convergence | OPEN, needs [L12]. By §3.2, any such criterion is about the transcendental map, not a finite jet. |

The P1-c-5d Stokes-gap campaign remains **not approved**, per the P1-c-2 review.

## 5. Bibliographic completion

[LS] (P1-c-2): L. López-Hernanz, F. Sanz Sánchez, *J. reine angew. Math.* 739 (2018) 277–296 (from the UVaDOC record).

## 6. Status

| Item | Status |
|---|---|
| φ± Gevrey-1/3 upper bound | imported (C4), with the provenance limits of §3.1 |
| Lower bounds / divergence of φ± | OPEN; not decidable from any finite jet of F ([BFM] Prop. 3.8) |
| [L12] questions 1–4 | Q1 partly; Q2 Gevrey part answered; Q2 summability, Q3, Q4 OPEN (full text needed) |
| B-an, B-6 | OPEN |

**Unchanged:** DYAD v6.4.18 adopted; OPEN 20 PARTIAL. No owner adoption; everything above is SESSION material.

## 7. Reproduction

- **Files:** `dyad_open20_an_p1c2b_check.py`, `qw.py`, `fzw.py`, `ext.py`, `p1c2b_check.json`, `p1c2b_perf.json`, `SHA256SUMS.txt`.
- **Command:** `python3 dyad_open20_an_p1c2b_check.py`. Expected output: `RESULT: PASS`, with B1–B4 true and M1–M3 false.
- **Checker SHA-256:** `451024649a09b5246d99afe91b765754869f697e969ef3b33331de2e01badb5e`.
- **`p1c2b_check.json` SHA-256:** `a068dabc4b643c18990f43d021e2f2d74daa8f8c238866a213e2bf71b70f45e2`.
- **Source PDFs** (not redistributed): [BFM] `94913000…6a09`; Carrillo–Lastra `e499915c…376e` and `8ac28ea5…cda6` (two downloads of the same article); Cano–Corral–Mol `724555f4…decd5`.
