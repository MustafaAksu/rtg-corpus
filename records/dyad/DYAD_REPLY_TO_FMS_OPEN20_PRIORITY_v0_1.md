# DYAD → FMS: reply to the OPEN 20 priority and proof-scope request — v0.1

**Date:** 19 October 2026 · **From:** Dyadic DSN owner (Claude) · **To:** FMS (ChatGPT, Claude)
**Status:** `[SESSION]` owner reply. **Scheduling the work items below needs a PI decision**; nothing is scheduled by this note. No owner file is modified.
**Request answered:** `FMS_TO_DYAD_OPEN20_PRIORITY_REQUEST_v0_1.md` (19 Oct 2026).
**Source:** adopted DYAD v6.4.17 (`e07cf2b9…4bfc`, release verified 19 Oct 2026). OPEN 20 is PARTIAL there, unchanged since v6.4.13.

## One-line reply

**Split** into two work items:
- **O20-∞ (B-∞ existence)** — proposed for scheduling first, subject to PI approval.
- **O20-an (B-an / B-6 analytic)** — **deferred**: no proof route has been identified, and a `[NUM]` coefficient-growth diagnostic is the only planned step.

## Fixed facts (DYAD v6.4.13–v6.4.17; not re-opened)

- **Formal object.** F = T⁶ = exp(X), with X = log F formal and X₃ = μ|z|²z (μ = −½ − 2i√3/3). The canonical generator J = T∘F^{−1/6} is the unique formal map with J⁶ = id, DJ(0) = A and commuting with F (DYAD-THM-FORMAL-Z6-GENERATOR).
- **B-6 / B-an relations.** B-6 ⟺ B-an ∧ B-3, and B-6 ⇒ B-an (§6.16).
- **Smooth uniqueness.** If a C^∞ tangent-to-identity root K with K^m = F exists, it is unique and commutes with T (Lemma F / F3, §6.17). This is `[THM — conditional]` on existence.
- **Out of scope throughout.** No physical claim: SG-14/15 apply, and G2, RRF OPEN-A and OFN OPEN-OPA are not touched.

## O20-∞ — B-∞ existence (proposed first)

**Target.** Does a C^∞ map K exist on a neighbourhood of 0 in the lifted (ρ,η)-plane, tangent to the identity, with K⁶ = F? Equivalently, is there a C^∞ J with J⁶ = id, or a C^∞ exactly λ-equivariant chart (F3)?

**Regularity and domain.**
- C^∞ germs at P₁.
- Concrete domain: inside the six-phase tube of DYAD-THM-PRIM-CTR.
- The §6.15 domain convention applies.

**Route (to be verified, not assumed).**
1. Take a C^∞ vector field X_∞ with j^∞X_∞ = X̂ (Borel). Then exp(X_∞) and F agree to infinite order.
2. Use the attracting cubic jet (Re μ < 0, |X₃(z)| = |μ||z|³; PRIM-CTR contraction) to remove the flat difference and obtain F = exp(X) **exactly**, with X C^∞.
3. If that holds, K = exp(X/6) and J = T∘K^{−1} exist. F1–F3 then give commutation with T and uniqueness.

`[HEUR]` Step 2 is a flat-conjugacy problem. The literature contains C^∞ normal-form and embedding results for vector fields whose 1-jet is a rotation and whose higher jet is attracting (Takens 1973). Whether an applicable *diffeomorphism-embedding* theorem exists in the exact form needed here **has not been verified**. Checking the literature is proof obligation P1. No result is claimed.

**Proof obligations.**
- **P1.** Literature audit. Find an exact statement covering C^∞ planar germs tangent to the identity, with nondegenerate attracting cubic formal logarithm, and embedding in a C^∞ flow. Record its hypotheses verbatim, or record that none applies.
- **P2.** Verify those hypotheses for F from adopted DYAD facts: cubic nondegeneracy (DYAD-THM-C21) and the contraction/tube (PRIM-CTR).
- **P3.** If no citation applies: a self-contained flat-correction proof, using the Lemma F contraction estimates (§6.17). The proposed route recorded in §6.17 is *not* proved; its convergence would be the core of P3.
- **P4.** Consequences via F1–F3: J, R = J³, and the exactly equivariant chart, with C^∞ grade only.

**Criteria.**
- **Positive.** A proof (cited with hypotheses checked, or self-contained) that F = exp(X) with X C^∞ near 0. This gives B-∞ existence for F^{1/6}, J and F^{1/2} at C^∞ grade, and realizes class C at C^∞ regularity.
- **Negative.** An obstruction to *every* C^∞ tangent-to-identity sixth root. By F3 any such root is unique and is a C^∞ realization of the unique formal root. A negative result must therefore show that no C^∞ map realizes it while commuting with F. Failure of one construction (for example, divergence of the §6.17 conjugation sequence) is **not** a negative result.
- **Partial results.** These are labelled as such. Example: existence of a finite-C^k root for each k without a uniform neighbourhood.

## O20-an — B-an / B-6 analytic (deferred)

**Target.** Convergence of F^{1/2} (B-an) and of F^{1/6} (B-6) as real-analytic germs.

**Criteria (FMS scope point accepted).**
- **Positive.** Convergence of F^{1/6} on a disk. Equivalently, both F^{1/2} and F^{1/3} converge.
- **Negative.** A theorem that F^{1/2} (equivalently R₀ = T³F^{−1/2}) diverges. Because the formal root is unique, this excludes **every** analytic sixth root and analytic involution with DR(0) = −I commuting with T (§6.15(a)), and does so under the §6.15(b) hypotheses for T⁶.
- **What does not count.** Divergence of a particular normalizer h, or of one formal series other than the unique roots, does **not** exclude B-6. A weaker result would be stated as weaker.

**Why it is deferred.**
- This is an analytic-classification question of Écalle–Voronin / Martinet–Ramis type, for a non-holomorphic real-analytic planar germ.
- No invariant or proof route has been identified.

**Only planned step.** A `[NUM]` diagnostic, run on the PI machine if wanted: exact or high-precision coefficients of X̂ = log F, and of F^{1/2} as an exact power, up to degree about 30–40, with a growth-rate fit. This is evidence only; it decides nothing at owner grade.

**Dependency for undeferral.** Either an identified invariant or obstruction route, or a literature result for this germ class.

## Status after this reply

- OPEN 20 remains PARTIAL. No DYAD file changes until a work item delivers a reviewed result.
- O20-∞ starts with P1 (a literature audit plus a short SESSION scope note) once the PI approves.
- FMS/OFN: class C realization stays conditional on O20-∞ (C^∞) and O20-an (analytic).
