# DYAD OPEN 20 / O20-∞ — P3-b: derivative flatness of F − G; P3-c: C^k convergence of p_n on one fixed ball (SESSION v0.1.1)

**Version:** v0.1.1 (supersedes v0.1 `f299f50f…a136`; changes in §5) · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Basis.**
- `DYAD_OPEN20_P2B_DOMAIN_PROOF_SESSION_v0_2_1.md` (`6f275e73…fcf4`): Propositions B and C, Corollary-level domain facts. Review: `PROOF REVIEW ACCEPTED`.
- `DYAD_OPEN20_P3A_ITERATE_DERIVATIVE_BOUNDS_SESSION_v0_1.md` (`b044a41d…a846`): Lemmas A, B, B′, C. Review: `SCIENTIFIC REVIEW ACCEPTED — P3-b AUTHORIZED`.
- Notation is taken from those records: (H1)–(H3), B̄₃, O, Γ_m, α = c₁/a, s = 2α + 1, b = 7α + 1, A_m, B_m, C_m, C̄_m.

**Scope of this record.**
- Review of v0.1: `P3-b/P3-c SCIENTIFIC REVIEW ACCEPTED — FINAL OWNER INTEGRATION AUDIT REQUIRED`; corrections P3C-01, P3C-02 applied here.
- §1 is P3-b, as the review asked.
- §2 is P3-c. P3-b is short, and P3-c follows from it with the P3-a lemmas, so both are submitted together. The reviewer may accept P3-b alone.
- §3 states what P3-c would give (Q∞) and a candidate consequence for B-∞ existence. Both are **conditional on review** and change no status.

**Status.**
- `[SESSION]` proof record for review.
- DYAD v6.4.17 is unchanged; OPEN 20 PARTIAL; B-∞ existence OPEN.
- No owner theorem is adopted.

**Check script.** `dyad_open20_p3bc_check_v0_1_1.py` writes `p3bc_check_v0_1_1.json`. It checks exponent bookkeeping only (exact Fractions, < 1 s, run locally):
- 3 gates (E4–E6; E6 now uses the integer N_k of P3C-01);
- 3 negative controls (N5–N7; N7 = floor instead of ceiling);
- exit 0.

## 1. P3-b — derivative flatness of R := F − G

`[THM — SESSION]`

**Lemma D (flat derivatives).** For all integers N ≥ 0 and j ≥ 0 and all w ∈ B̄₃:

  ‖D^jR(w)‖ ≤ C_{N,j}·|w|^N,  C_{N,j} := (1/N!)·sup_{B̄₃}‖D^{N+j}R‖.

*Proof.*
1. **Regularity.** By (H1), F and G are C^∞ on an open set containing the compact convex ball B̄₃. So every sup_{B̄₃}‖D^mR‖ is finite.
2. **Vanishing jet.** j^∞_0F = j^∞_0G, so D^mR(0) = 0 for every m. Fix j and put S := D^jR, a C^∞ map into the symmetric j-linear maps. Then D^iS(0) = D^{i+j}R(0) = 0 for every i.
3. **Taylor.** Use Taylor's formula with integral remainder at 0 and order N, in the Banach-space form. For w ∈ B̄₃ the segment {tw} lies in B̄₃ by convexity, and

  S(w) = Σ_{i<N} D^iS(0)[w^{⊗i}]/i! + ∫₀¹ ((1 − t)^{N−1}/(N − 1)!)·D^NS(tw)[w^{⊗N}] dt.

   The polynomial part vanishes.
4. **Bound.** Hence ‖S(w)‖ ≤ sup_{B̄₃}‖D^{N+j}R‖·|w|^N·∫₀¹(1 − t)^{N−1}/(N − 1)! dt = C_{N,j}|w|^N.
5. For N = 0 the statement is the definition of the sup. ∎

**Remarks.**
- The value-level constant of (H3) is c_N = C_{N,0}.
- The constants depend on the domain only through sup_{B̄₃}‖D^{N+j}R‖. They are fixed once ρ is fixed, and they do **not** depend on ρ₁ or on N₀.
- In P3-a §5 the outlook used |w|^{N−j}. Lemma D gives the full power |w|^N for **every** j, with a j-dependent constant. So no flat order is lost per derivative, and in §2 the same N appears in every term. This addresses the reviewer's "track which j is used".

## 2. P3-c — Σ_n ‖p_{n+1} − p_n‖_{C^k} < ∞ on one fixed ball

### 2.0 Fixed data

- **Radius.** Fix N₀ > 2γ + 4 once and let ρ₁ = ρ₁(N₀) be the radius of Proposition B. Put U := B(0, ρ₁), an open ball.
- **One ball for all k.** ρ₁ and U are fixed for the whole section.
  - Larger flat orders N enter **only** through Lemma D, which holds on all of B̄₃.
  - So the radius is never shrunk (the reviewer's second point).
- **Norm.** ‖f‖_{C^k(U)} := max_{ℓ≤k} sup_U ‖D^ℓf‖.

### 2.1 Integral representation

`[THM — SESSION]` **Lemma P3-c.0.** For x ∈ B̄(0, ρ₁), n ≥ 0, y_n := F^n x and z_t(x) := G(y_n) + t·R(y_n), t ∈ [0, 1]:
- (a) z_t(x) ∈ G^{n+1}(O) = dom Γ_{n+1} for all t;
- (b) p_n(x) = Γ_{n+1}(G(y_n)) and p_{n+1}(x) = Γ_{n+1}(F(y_n));
- (c) d_n := p_{n+1} − p_n satisfies, on U,

  d_n(x) = ∫₀¹ DΓ_{n+1}(z_t(x))[R(F^n x)] dt.

*Proof.*
- (a) For 0 < |x| ≤ ρ₁ this is Corollary B′ (P3-a). For x = 0, z_t(0) = 0 = G^{n+1}(0) ∈ G^{n+1}(O).
- (b) G(y_n) = G(G^n p_n) = G^{n+1}p_n with p_n ∈ O, and Γ_{n+1} is the inverse of G^{n+1}|_O. The F case is the definition of p_{n+1}.
- (c) By (a), the path t ↦ z_t(x) lies in the open set dom Γ_{n+1}, so the fundamental theorem of calculus applies along it. ∎

**Smoothness.**
- By (a), for every x ∈ U the whole path lies in dom Γ_{n+1}, and (t, x) ↦ z_t(x) is C^∞ on [0, 1] × U.
- So the integrand is C^∞ in x with all x-derivatives jointly continuous on [0, 1] × U.
- Differentiation under the integral is therefore allowed on U. No perturbation argument is needed.

### 2.2 One flat factor in every term

**Leibniz split.**
- Write the integrand as ℰ(Ψ_t(x), V(x)), where:
  - Ψ_t := DΓ_{n+1}∘z_t (operator-valued);
  - V := R∘F^n (vector-valued);
  - ℰ(L, v) = Lv is the bounded bilinear evaluation.
- By the Leibniz rule for bounded bilinear maps:

  ‖D^ℓ[ℰ(Ψ_t, V)](x)‖ ≤ Σ_{i=0}^{ℓ} binom(ℓ, i)·‖D^iΨ_t(x)‖·‖D^{ℓ−i}V(x)‖.  (L)

- **Every term of (L) contains exactly one factor D^{ℓ−i}V, a derivative of R∘F^n**, of order 0 to ℓ (the reviewer's first point).
- The factor D^iΨ_t also depends on R through z_t. There R is used only as a **bounded** quantity, and its decay is not used.

**Bounds**, for x ∈ U, n ≥ 0 and t ∈ [0, 1]:

(V) **The flat factor.**
- Apply (FdB) to R∘F^n: ‖D^mV(x)‖ ≤ Σ_π ‖D^{|π|}R(y_n)‖·Π_B ‖D^{|B|}F^n(x)‖.
- Use Lemma D with the **same N** for every |π| = j, and Lemma A.
- This gives ‖D^mV(x)‖ ≤ K_{N,m}·|y_n|^N·(1 + n)^{A_m}, with A_0 := 0.
- The exponent bound uses max_π Σ_B A_{|B|} = A_m, attained at |π| = 1.

(Z) **The path.**
- For q ≥ 1, ‖D^q z_t(x)‖ ≤ ‖D^q(G∘F^n)(x)‖ + ‖D^qV(x)‖ ≤ Z_q(1 + n)^{A_q}.
- This uses (FdB) for G∘F^n with sup_{B̄₃}‖D^jG‖ < ∞ and Lemma A, and (V) with |y_n| ≤ 3ρ.

(Ψ) **The inverse factor.**
- D^rΨ_t = (D^{r+1}Γ_{n+1})∘z_t composed with derivatives of z_t.
- Lemma B at the points z_t(x) ∈ G^{n+1}(O) gives ‖D^{r+1}Γ_{n+1}‖ ≤ C̄_{r+1}(2 + n)^{B_{r+1}} ≤ 2^{B_{r+1}}C̄_{r+1}(1 + n)^{B_{r+1}}.
- With (FdB) and (Z): ‖D^iΨ_t(x)‖ ≤ Y_i(1 + n)^{X_i}, where:
  - X_0 = B_1;
  - X_i = max over partitions of i into j ≥ 1 blocks of (B_{j+1} + Σ_B A_{|B|}).

**Lemma P3-c.1** `[THM — SESSION]`. For every ℓ ≥ 0 and N ≥ 0 there is M_{N,ℓ} such that, for x ∈ U and n ≥ 0:

  ‖D^ℓd_n(x)‖ ≤ M_{N,ℓ}·(1 + n)^{E_ℓ}·|F^n x|^N,  E_ℓ := (8α + 1)ℓ + 2α.

- The exponent E_ℓ does not depend on N; only the constant does.
- *Proof.* Combine (L), (V) and (Ψ) and integrate in t. The exponent is max_{0≤i≤ℓ}(X_i + A_{ℓ−i}). Since b > s, this maximum is attained at i = ℓ with ℓ blocks: B_{ℓ+1} + ℓα = (7α + 1)ℓ + 2α + ℓα = E_ℓ. ∎
- Gate E4 checks the inequality and gate E5 checks that it is attained (ℓ ≤ 12, 35 values of α). Controls N5 (constant α) and N6 (slope 8α) fail.

### 2.3 Summation

`[THM — SESSION]` **Proposition P3-c.**

**Uniform decay.** By (H2), Q(F^n x) ≤ 1/(1/Q(x) + an) ≤ 1/(an) for n ≥ 1, uniformly in x ∈ U. So |F^n x|^N ≤ (an)^{−N/2}.

**Choice of N.**
- Fix k and take the **integer** N_k := ⌈2E_k + 3⌉ (P3C-01; Lemma D needs an integer Taylor order). Then E_k − N_k/2 ≤ −3/2. E_ℓ is nondecreasing in ℓ (gate E6), so for every ℓ ≤ k, using (1 + n)^{E_ℓ} ≤ 2^{E_ℓ}n^{E_ℓ}:

  sup_U ‖D^ℓd_n‖ ≤ M_{N_k,ℓ}·a^{−N_k/2}·2^{E_ℓ}·n^{E_ℓ−N_k/2} ≤ M′_{k}·n^{−3/2}  (n ≥ 1).

- Hence Σ_n ‖d_n‖_{C^k(U)} < ∞ for every k, on the **same** ball U = B(0, ρ₁(N₀)).

**Consequences.**
- (i) p_n → Φ_∞ in C^k(U) for every k. Φ_∞ is the C⁰ limit of Proposition B, so Φ_∞ ∈ C^∞(U).
- (ii) **Flatness.**
  - j^∞_0F^n = j^∞_0G^n, so j^∞_0p_n = j^∞_0(Γ_n∘G^n) = id for every n.
  - C^k convergence then gives D^ℓΦ_∞(0) = D^ℓid(0) for every ℓ.
  - So Φ_∞ − id is C^∞-flat at 0, and in particular DΦ_∞(0) = I. ∎

## 3. Consequences, conditional on acceptance of §2

### 3.1 Q∞

`[THM — SESSION, conditional on review of §2]`

**Corollary Q∞.** F = exp(X) near 0 for a C^∞ vector field X whose ∞-jet at 0 equals X̂ = log F.

*Proof* (domains written out, P3C-02). All balls are Euclidean balls in the raw frame W, centred at 0.

1. **Inverse of Φ_∞.** Φ_∞ ∈ C^∞(U) and DΦ_∞(0) = I. By the inverse function theorem there are r′ ∈ (0, ρ₁) and an open V′ ∋ 0 such that Φ_∞ : B(0, r′) → V′ is a C^∞ diffeomorphism. Write Ψ := (Φ_∞|_{B(0,r′)})⁻¹ ∈ C^∞(V′). By Proposition C, Ψ agrees with the C⁰ inverse there.
2. **Flow domain of X_∞.** X_∞ is C^∞ near 0 with X_∞(0) = 0 and DX_∞(0) = 0 (j¹X̂ = 0, because j¹F = id).
   - Choose r* > 0 with B̄(0, r*) ⊂ V′, B̄(0, r*) inside the domain of X_∞, and |X_∞(v)| ≤ |v| on B̄(0, r*).
   - Put r_G := r*/e. For |v| < r_G, Grönwall gives |φ^t_{X_∞}(v)| ≤ |v|e^t < r* while the solution exists. So the solution exists for t ∈ [0, 1] and stays in B(0, r*) ⊂ V′.
   - G = exp(X_∞) is the time-one map, so G(v) = φ¹_{X_∞}(v) for v ∈ B(0, r_G).
3. **Common domain.** By continuity and Φ_∞(0) = 0, choose r″ ∈ (0, r′] with Φ_∞(B(0, r″)) ⊂ B(0, r_G). Put U* := B(0, r″).
4. **Pull-back field and its flow.** X(u) := DΦ_∞(u)⁻¹X_∞(Φ_∞u) is C^∞ on B(0, r′) ∩ Φ_∞⁻¹(B(0, r*)).
   - For w ∈ U* and t ∈ [0, 1], the curve γ(t) := Ψ(φ^t_{X_∞}(Φ_∞w)) is defined and C^∞ in (t, w).
   - It satisfies γ′ = DΨ(·)X_∞(·) = X(γ), since DΨ(Φ_∞u) = DΦ_∞(u)⁻¹. So γ(t) = φ^t_X(w), and the flow of X exists on U* for t ∈ [0, 1].
5. **Time-one map.**
   - U* is a ball with r″ ≤ 3ρ, so F(U*) ⊂ U* by (H2). In particular Fw ∈ B(0, r′), and Ψ(Φ_∞(Fw)) = Fw.
   - Proposition B gives Φ_∞(Fw) = G(Φ_∞w), with Φ_∞w ∈ B(0, r_G).
   - Hence Fw = Ψ(G(Φ_∞w)) = Ψ(φ¹_{X_∞}(Φ_∞w)) = φ¹_X(w) for all w ∈ U*. That is, F = exp(X) on U*.
6. **Jet.** Φ_∞ − id is flat, so j^∞_0X = j^∞_0X_∞ = X̂. ∎

**Scope.** This is a germ-level statement on the explicit but non-quantified ball U* = B(0, r″). Here r″ depends on Φ_∞ and X_∞ through steps 1–3. No numerical radius is claimed.

**Uniqueness.** By adopted F3 (§6.17), applied to roots, together with Lemma F, the flat-close C^∞ objects built this way are unique. The choice of Borel realization X_∞ therefore does not affect the germ of exp(X/m). This is to be confirmed in the audit below.

### 3.2 Candidate for B-∞ existence

`[CAND — SESSION]`; owner and PI decision, not claimed here.

**Chain.**
- If Q∞ holds, then K := exp(X/6) is a C^∞ tangent-to-identity germ with K⁶ = F.
- Adopted F3 (§6.17, `[THM — conditional]` on the existence of the smooth object) then gives:
  - K commutes with T and is unique;
  - J := T∘K⁻¹ exists with J⁶ = id, DJ(0) = A and JT = TJ.
- Likewise F^{1/2} = exp(X/2) gives R₀ via F3.
- This would settle **B-∞ existence** for both F^{1/2} and F^{1/6} at the C^∞ scope.

**Not settled by this chain.** B-an and B-6 (analyticity), finite-C^k versions with explicit constants, and any physical realization.

**Audit needed before any status change:**
- the §6.15 domain convention for F3 against the ball U* used here;
- the "tangent to identity" hypothesis of F3 for exp(X/6). This holds formally because j¹X = 0;
- the existence of X_∞ for X̂ = log F. This is Borel's lemma: X̂ is a formal vector field, and Borel realizes every formal series by a C^∞ germ. It is already the standing input of P2.

## 4. Status

| Item | Status |
|---|---|
| P2-a, P2-b (Props B, C), P3-a | Review accepted (SESSION) |
| §1 Lemma D (P3-b) | `[THM — SESSION]` — submitted |
| §2 Lemmas P3-c.0/1, Proposition P3-c | `[THM — SESSION]` — submitted |
| §3.1 Corollary Q∞ | conditional on §2 review |
| §3.2 B-∞ existence via F3 | `[CAND — SESSION]`; owner audit plus PI decision; no status change |
| O20-an (B-an, B-6) | OPEN, untouched |

Adopted DYAD version: v6.4.17; OPEN 20 PARTIAL; B-∞ existence OPEN. If §2–§3 are accepted, the owner route is a DYAD successor draft (v6.4.18 DRAFT r1) with its own builder, checker, negative controls and review, as usual.

## 5. Changes v0.1 → v0.1.1 (review of 20 Oct 2026)

1. **P3C-01.** N_k := ⌈2E_k + 3⌉ (integer Taylor order), giving E_k − N_k/2 ≤ −3/2. The check script v0.1.1 tests the integer choice in gate E6. New negative control N7 (floor) fails as required.
2. **P3C-02.** §3.1 proof rewritten with explicit domains:
   - IFT ball B(0, r′) and inverse Ψ on V′;
   - Grönwall flow ball B(0, r_G) of X_∞ for t ∈ [0, 1];
   - common ball U* = B(0, r″), forward-invariant under F;
   - the flow of X = Φ_∞*X_∞ on U*, and F = φ¹_X on U*.
3. **Unchanged:** §1, §2.0–§2.2, all exponents and the statuses in §4.
