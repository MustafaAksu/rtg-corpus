# DYAD OPEN 20 / B-∞ existence — final owner integration audit (SESSION v0.1.1)

**Version:** v0.1.1 (supersedes v0.1 `4e598848…7b57`; E2/L7 scope correction only, §8) · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Purpose.** This record does what the review of P3-b/P3-c v0.1 requested (`P3-b/P3-c SCIENTIFIC REVIEW ACCEPTED — FINAL OWNER INTEGRATION AUDIT REQUIRED`, item 6):
- merge the chain P2-b → P3-a → P3-b/c → Q∞ → F3 into one statement;
- check its hypotheses, the order in which radii and constants are chosen, and the §6.15 domain convention;
- propose the content of a DYAD v6.4.18 draft.

**Status.**
- `[SESSION]` audit. Nothing here is adopted.
- DYAD v6.4.17 is unchanged; OPEN 20 PARTIAL; B-∞ existence formally OPEN until owner/PI adoption.

**Check script.** `dyad_open20_binf_integration_check.py`, run with the directory of the five pinned inputs. It writes `binf_integration_check.json`:
- 6 gates (I0–I5);
- 3 negative controls (M1–M3);
- exit 0. Exact sympy, under 5 s, run locally.

## 1. Inputs (pinned; gate I0)

| Record | SHA-256 | Review |
|---|---|---|
| P2-b `DYAD_OPEN20_P2B_DOMAIN_PROOF_SESSION_v0_2_1.md` | `6f275e735897a3f29308de132a416d184b01c2e420fafb83cc012d360033fcf4` | PROOF REVIEW ACCEPTED (Props B, C) |
| P3-a `DYAD_OPEN20_P3A_ITERATE_DERIVATIVE_BOUNDS_SESSION_v0_1.md` | `b044a41d88c57bfc258469e741d01bd458e9256e2fe4e4ebda92e32b07e9a846` | SCIENTIFIC REVIEW ACCEPTED |
| P3-a script `dyad_open20_p3a_check.py` | `56d8178109b34a8858dca6d3d5470524916ae850390bf2a81b86d9ddf2e67140` | re-run by reviewer |
| P3-b/c `DYAD_OPEN20_P3BC_FLAT_DERIVATIVES_AND_CK_CONVERGENCE_SESSION_v0_1_1.md` | `3ceca25ee64d0b0263da10972ab8e64231545e74e8ad8fc977cd25caeb9e487f` | v0.1 accepted; v0.1.1 applies P3C-01/02 |
| DSN `RTG_DYADIC_OSCILLATOR_DSN_v6_4_17.md` | `e07cf2b93b532554d9e1d05d2bfef3be34829b7cb892627c0bb03d1d182d4bfc` | adopted |

Also used from the adopted DSN:
- DYAD-THM-PRIM-CTR;
- §6.15 (domain convention; cubic term μ|W|²W, DYAD-THM-C21);
- §6.16 (formal X = log F; formal centralizer);
- §6.17 (Lemma F; F1–F3).

## 2. Integrated statement

`[THM — SESSION]`, proposed for v6.4.18.

**Theorem E (smooth flow embedding of the six-step return).** Let F = T⁶ and X̂ = log F, the formal generator of §6.16. Then:
- **(E1)** There are a ball U* = B(0, r″) in the raw frame and a C^∞ vector field X near 0 with j^∞_0X = X̂ and F = φ¹_X on U*.
- **(E2) Uniqueness among generators with zero linear part.** Let X′ be another C^∞ field with φ¹_{X′} = F near 0 **and DX′(0) = 0**. Then X′ = X as local germs. (X itself has DX(0) = 0, since j¹X = j¹X̂ = 0.) In particular, X does not depend on the Borel realization X_∞ used to build it, because every such realization yields a field with zero linear part.
  - **Not claimed:** uniqueness among all C^∞ generators of F. The relation exp(DX′(0)) = DF(0) = I does not force DX′(0) = 0; for example, a planar rotation field with angular speed 2π has linear time-one map I.
- **(E3) Roots.** For every m ≥ 1, K_m := φ^{1/m}_X is a C^∞ tangent-to-identity germ with K_m^m = F. It commutes with T and is the unique such root (adopted F3).
- **(E4) B-∞ existence.**
  - J := T∘K_6⁻¹ is a C^∞ local germ with J⁶ = id, DJ(0) = A and JT = TJ.
  - R := T³∘K_2⁻¹ is a C^∞ local involution with DR(0) = −I and RT = TR. It is the unique such involution (F2).
  - Hence OPEN 20 B-∞ existence holds at the C^∞ scope, for F^{1/2}, R₀, F^{1/6} and J.

**Not included:**
- analyticity (B-an, B-6), since a C^∞ root need not be analytic;
- a quantitative radius;
- finite-C^k versions with explicit constants;
- any physical or G2 realization, or identification of EF = TE with EF = T⁶E (SG-14/15).

## 3. Proof as a chain, with each link's source

**L0 — Formal generator** (§6.16, adopted).
- X̂ = log F exists and is unique as a formal tangent-to-identity generator.
- Its jets satisfy j²X̂ = 0 and X̂₃ = μ|W|²W, with μ = −½ − (2√3/3)i.
- Gate I1 recomputes the cubic part of T⁶ from T and confirms it is μ|W|²W in W = ρ − η/2 + i(√3/2)η. This links P3-a Claim 1 to §6.15/DYAD-THM-C21.
- Gate I5 confirms that the quadratic part vanishes.

**L1 — Borel realization and G.**
- X_∞ is a C^∞ field with j^∞_0X_∞ = X̂ (Borel's lemma, componentwise).
- G := φ¹_{X_∞} is defined near 0 by the Grönwall argument of P3-b/c §3.1, step 2.
- **Jet identity j^∞_0G = exp(X̂) = j^∞_0F** (short proof):
  - for each k, t ↦ j^k_0φ^t satisfies the polynomial ODE d/dt j^kφ^t = [j^kX_∞ ∘ j^kφ^t]_k on the finite-dimensional space of k-jets fixing 0;
  - the truncated formal flow [exp(tX̂)]_k satisfies the same ODE with the same initial value;
  - ODE uniqueness gives equality, and t = 1 gives the identity.
- **Notation clash.** The DSN already uses G = J² (§6.16). In the v6.4.18 text the time-one map will be written **G_∞**.

**L2 — Hypotheses (H1)–(H3)** (P2-b §0), for F and for G:
- **(H1)** For F: analytic, j¹F = I (gate I4: A⁶ = I), no quadratic term (I5). For G: the same 2-jet by L1. Hence ‖DH − I‖ ≤ c₁|w|² on a small ball.
- **(H2)** Q(Hw) = Q − Q² + O(|w|⁵), from Re μ = −½ (gate I2) and the common 4-jet. Hence Q(Hw) ≤ Q − ½Q² on a small ball, so a = ½.
  - For F this agrees with DYAD-THM-PRIM-CTR (Q ≤ 1/400).
  - For G it is proved only from the jet, not imported.
- **(H3)** Equal ∞-jets by L1. At value level this is (H3); at derivative level it is Lemma D (P3-b).

**L3 — C⁰ flat conjugacy** (P2-b, accepted).
- Proposition B: p_n = Γ_n∘F^n → Φ_∞, with Φ_∞F = G_∞Φ_∞.
- Proposition C: Φ_∞ is a local homeomorphism. Lemma F is used twice:
  - for C_F (adopted Lemma F);
  - for C_G (re-proved for G_∞ from its own (H1)–(H2); not imported).

**L4 — Derivative bounds** (P3-a, accepted). Lemmas A, B, B′, C, uniform in the base point. The §1 observation of P3-a shows that the uniform (1 + nQ)^A form is impossible.

**L5 — C^∞ upgrade** (P3-b/c, accepted; v0.1.1 corrections).
- Lemma D: derivative flatness with the same N in every term.
- Lemma P3-c.1: E_ℓ = (8α + 1)ℓ + 2α, independent of N.
- Integer N_k = ⌈2E_k + 3⌉.
- Conclusion: Φ_∞ ∈ C^∞(U), and Φ_∞ − id is flat at 0.

**L6 — Q∞** (P3-b/c v0.1.1 §3.1). Explicit domains r′ → r_G → r″. Result: F = φ¹_X on U*, X = Φ_∞*G_∞-field, j^∞X = X̂. This is (E1).

**L7 — Uniqueness of X** (E2). New in this audit; owner proof. It uses adopted Lemma F with a ball that does not depend on t.

Let X and X′ be C^∞ fields with φ¹_X = φ¹_{X′} = F near 0 and DX(0) = DX′(0) = 0 (scope of E2).

1. **Jets.**
   - By the jet ODE of L1, j^∞_0φ¹_{X′} = exp(j^∞X′) formally, so exp(j^∞X′) = j^∞F.
   - Since DX′(0) = 0, j^∞X′ lies in the class of formal vector fields with zero linear part. On that class the formal exponential is a bijection onto tangent-to-identity formal maps, with inverse the formal logarithm (§6.16).
   - Hence j^∞X′ = log F = X̂ = j^∞X.
   - **This is the only place where DX′(0) = 0 is used** (review of v0.1, E2). Without it the step fails, as the rotation-field example in E2 shows.
2. **Flows.** Both fields vanish to third order at 0. By Grönwall there is a ball B° on which both flows exist for t ∈ [−1, 2] and stay in their domains.
3. **The family C_t.** For t ∈ [0, 1] put C_t := φ^{−t}_X∘φ^t_{X′}. Then:
   - C_t is C^∞;
   - C_t has ∞-jet id at 0 (step 1, jet ODE as in L1), so |C_t(W) − W| ≤ c_N(t)|W|^N for every N;
   - C_t commutes with F, because φ^t_{X′} commutes with φ¹_{X′} = F, and φ^{−t}_X commutes with φ¹_X = F, on B°.
4. **A t-independent ball.** (t, w) ↦ C_t(w) is C² on [0, 1] × B̄°, and C_t(0) = 0, DC_t(0) = I. So there is M with |C_t(w) − w| ≤ M|w|² for all t.
   - Fix the Lemma F data s₀ and K once.
   - Choose r with 4r ≤ s₀, 4rK ≤ ½, B_{4r} ⊂ B° and M√(4r) ≤ 1, where B_s = {Q ≤ s}.
   - Then Q(C_tw) ≤ (1 + M|w|)²Q(w) ≤ 4r for w ∈ B_r. So C_t : B_r → B_{4r} for **every** t, and F(B_r) ⊂ B_r.
5. **Conclusion.** Lemma F gives C_t = id on B_r for all t ∈ [0, 1], i.e. φ^t_{X′} = φ^t_X on B_r. Differentiating at t = 0 gives X′ = X on B_r. ∎

Independence of X_∞ follows: two Borel realizations give two fields X, X′ with exp = F, and both have zero linear part. (F3 is not needed for E2; it is used in L8. E2 is not a premise of E3–E4.)

**L8 — Roots, J and R** (E3–E4).
- K_m := φ^{1/m}_X has K_m^m = φ¹_X = F, by the flow property along flow lines inside U*.
- DK_m(0) = exp(DX(0)/m) = I, since j¹X = j¹X̂ = 0. So K_m is tangent to the identity.
- F3 (adopted, `[THM — conditional]` on the existence of the smooth root) applies. Its existence condition is **discharged** by (E1). It gives TK_m = K_mT and uniqueness.
- **J := T∘K_6⁻¹.**
  - J⁶ = T⁶K_6⁻⁶ = F∘F⁻¹ = id, using TK_6 = K_6T.
  - DJ(0) = A.
  - JT = T·K_6⁻¹·T = T·T·K_6⁻¹ = TJ.
- **R := T³∘K_2⁻¹.**
  - R² = T⁶K_2⁻² = id.
  - DR(0) = A³ = −I (gate I4).
  - RT = TR and RF = FR follow.
- F2 gives uniqueness of R. ∎

## 4. Order of choices (no circularity)

1. **ρ.** (H1)–(H3) hold on B̄(0, 3ρ) for F and G_∞. In addition:
   - 9ρ² ≤ 1/400 (PRIM-CTR);
   - B̄(0, 3ρ) lies in the lifted chart {|η| < π} and in U_T ∪ {0};
   - B̄(0, 3ρ) lies inside the domains of X_∞ and G_∞.

   This fixes c₁, a = ½, α = c₁/a and γ = 2α.
2. **N₀ > 2γ + 4**, then C₃(N₀) and ρ₁ = min(ρ, (16C₃)^{−1/(N₀−3)}), with U = B(0, ρ₁). Propositions B and C and Lemmas A–C hold here.
3. **For each k:** N_k = ⌈2E_k + 3⌉. This enters only the constants C_{N_k,j} of Lemma D on B̄₃. It never changes ρ or ρ₁.
4. **r′, V′** (inverse function theorem for Φ_∞ ∈ C^∞(U)), then **r*, r_G** (Grönwall for X_∞), then **r″** (continuity of Φ_∞), with U* = B(0, r″) forward-invariant under F.
5. **F2/F3 and Lemma F shrinkings** (their balls B_r with 4r ≤ s₀, 4rK ≤ ½) are taken inside U*. These are germ statements, so shrinking is harmless.

Each later choice depends only on earlier ones; no earlier radius is revised.

## 5. §6.15 domain convention (G2-DOM) — check for R and for commutation

The convention needs:
- an open V ∋ 0 in the lifted plane;
- R : V → V with R∘R = id_V;
- for Φ ∈ {T, F}, commutation on D_Φ = V_Φ ∩ R⁻¹(V_Φ), with 0 ∈ int D_Φ.

**Construction.**
1. Take a ball B ⊂ U* ∩ {|η| < π} on which R is defined and R∘R = id holds as a germ identity.
2. Put V := B ∩ R⁻¹(B). It is open and contains 0, since R(0) = 0.
3. R(V) ⊂ V: for x ∈ V, R(x) ∈ B, and R(R(x)) = x ∈ B, so R(x) ∈ R⁻¹(B).
4. R∘R = id on V.
5. RΦ = ΦR holds as a germ identity, both sides being defined near 0. So D_Φ contains a neighbourhood of 0.

**Consequences.**
- §6.15(a)/(b) apply, consistently: R(0) = 0 and DR(0) = −I.
- F1 then gives RT = TR again, consistent with L8.
- For J and K_m, which are not involutions, the G2-DOM convention is not required. F3 is a germ statement.

**Verdict:** the domain convention is satisfied; no new hypothesis is needed.

## 6. Proposed v6.4.18 content

Owner proposal; PI decision.

1. **New RID `DYAD-THM-SMOOTH-EMBEDDING`**, `[THM]` at the C^∞ germ scope: Theorem E (E1)–(E4).
   - Proof records: P2-b v0.2.1, P3-a v0.1, P3-b/c v0.1.1 and this audit, all pinned.
   - Supporting lemmas are cited, not given separate RIDs; owner's choice.
2. **OPEN 20, B-∞ existence:** `[OPEN]` → **CLOSED (C^∞ scope)**.
   - Together with B-∞ flat uniqueness (closed in v6.4.13), B-∞ is fully closed.
   - **OPEN 20 overall stays PARTIAL**: B-an and B-6 stay OPEN.
3. **§6.17:**
   - The `[OPEN] Not established: existence…` paragraph is replaced by a pointer to Theorem E.
   - F1–F3 keep their grade; their existence condition is recorded as discharged at the C^∞ scope.
   - The old construction route (F^{−n}R_∞F^n) stays recorded as **unproved**. The route actually used is G_∞^{−n}F^n, which is a different sequence.
4. **Notation:** G_∞ for the Borel time-one map, to avoid the clash with G = J² in §6.16.
5. **Unchanged:** all other RIDs and grades; G2 and SG-14/15; OPEN 3 and OPEN 21 closures.
6. **Outbound notice N14** (sent by the PI), with the exact addressee list to be fixed in the draft:
   - FMS: the original requester of the OPEN 20 priority;
   - RRF: G2 and L-SHADOW-POLY remain unused;
   - OFN: reply v0.7 §3.5(b),(e), C^∞ branch.
7. **Process:** v6.4.18 DRAFT r1 with builder, checker, negative controls, SHA-256 and manifest, then review, then owner/PI adoption, then release verification, as usual.

## 7. Audit findings

| # | Finding | Effect |
|---|---|---|
| A1 | All links L0–L8 have an accepted or adopted source; L1 (jet identity) and L7 (uniqueness of X) are proved here | none — recorded |
| A2 | The cubic term of T⁶ in the W frame equals the DSN's μ\|W\|²W (I1); a = ½ is consistent (I2) | consistency confirmed |
| A3 | Notation clash G (P2/P3) vs G = J² (§6.16) | rename to G_∞ in v6.4.18 |
| A4 | §6.17's construction route differs from the route used | v6.4.18 text must not say the old route converged |
| A5 | E2 (uniqueness of X; t-uniform Lemma F ball) and independence of X_∞ are new owner content. v0.1.1 restricts E2 to generators with zero linear part | reviewed; scope corrected |
| A6 | No circularity in radii and constants (§4); G2-DOM satisfied (§5) | none |

Request to the reviewer: please check §3 L1 and L7, §4 and §5. These are the parts that are new in this audit.

## 8. Changes v0.1 → v0.1.1 (review of 20 Oct 2026: `SMOOTH EMBEDDING CHAIN ACCEPTED — E2 SCOPE CORRECTION REQUIRED`)

1. **E2 narrowed.** v0.1 claimed that every C^∞ field with time-one map F equals X. That claim is **stronger than proved**: L7 step 1 inferred j^∞X′ = log F from φ¹_{X′} = F alone, which needs DX′(0) = 0. E2 now assumes DX′(0) = 0, and the general claim is explicitly not made. Counterexample to the inference (not to the DYAD case): a planar rotation field with angular speed 2π.
2. **L7 step 1** rewritten. It now uses the L1 jet ODE, then injectivity of the formal exponential on fields with zero linear part (§6.16). Steps 2–5 are unchanged and were accepted (common t-domain, flat closeness of C_t, Lemma F).
3. **Borel independence** is unchanged in substance; the reason (zero linear part) is now stated.
4. **Unchanged:** E1, E3, E4, L0–L6, L8, §4, §5, and the check script and its results. The reviewer accepted these, and E3–E4 do not depend on E2.
