# RECOG Study Plan — r1 (after scientific review)

**Date:** 19 October 2026
**Status:** `[SESSION]` planning record. No DSN is edited. All grades are targets; no closure or release number is fixed before its test succeeds. The PI makes the final decisions.
**Supersedes:** `RECOG_STUDY_PLAN_2026-10-19.md` (r0, kept unchanged).
**Input:** the contributor's review, "ACCEPT WITH SCIENTIFIC REVISIONS" (19 Oct 2026).
**Base:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20`, SHA-256 `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df`.

---

## 0. Disposition of the review

Every point of the review was checked against the owner texts. All are accepted. Six refinements of my own are added, marked **[r1 add]**.

| Review point | Disposition | Where |
|---|---|---|
| G1: record the existing freeze decision; do not manufacture a new date | **Accepted.** I could not find that decision in the project or in the past chats available to me, so the record needs its provenance from the PI (D1). | §2 G1 |
| G2: N13 stays a conditional receipt until Dyadic v6.4.17's release verification reaches the receiving review | Accepted | §2 G2 |
| G2: header compaction as a separate mechanical change with a content-preservation check | Accepted | §2 G2 |
| A1: split into constant identity, slip schedule and recoverability; A1a ⇏ A1c; finite prefixes may be non-injective | Accepted | §3 A1 |
| §9: WRITE / READ / DECODE | Accepted as a proposed `[DEF]`. **[r1 add]** READ needs an *identity*, not mere dependence; otherwise it is Markov-trivial. | §3 A0 |
| — | **[r1 add]** Chart-free primary form of A1a, `C_D = φ̂₀ − Ψ_∞`. Given Dyadic T1 it is close to definitional; its content is the certified evaluation and the convention lock. | §3 A1a |
| — | **[r1 add]** Candidate decoder layering: the infinite token record → Ψ_∞; M_W and M need the full initial state; on a C_z fiber the O(√q₀) chart term dominates the O(q₀) R9 memory. | §3 A1c |
| A2: object/action/regularity ledger, not "five involutions"; J³ = R₀ is an alias | Accepted | §3 A2 |
| A2: check S_h = R₀ through degree 6 with the correct transport | Accepted. An owner statement exists (Dyadic v6.4.12 §6.16, as received in RRF v0.8.3 §4.2) and will be cited with its LIFT transport, then re-checked. | §3 A2 |
| A2: no "orientation can only be global/analytic"; allow an externally specified oriented carrier; no family-wide reuse of Dyadic's analytic conditions | Accepted | §3 A2 |
| A3: the quadrature identity is right but does not close R4; register it as typing | Accepted. R4(1) stays OPEN, with its target reworded. | §3 A3 |
| A4: per-gate W1–W5 table; vanishing holonomy on lock surfaces is a negative control; no automatic transfer of the continuous-carrier no-write lemma; keep F2(a)'s transport/substitution distinction | Accepted. **[r1 add]** The token predicate itself is only conditionally defined on class-C edges (it needs h_form, i.e. DYAD OPEN 20). r0's "G-transport = different token rule" sentence is corrected. | §3 A4 |
| B1: decompose the actual proof constant first; correlated errors; a direct \|M_W − 𝒫₂\| benchmark; Stage C only if Stage A shows a real bottleneck | Accepted. The direct benchmark is Dyadic-owned with RECOG input. | §4 B1 |
| R3: separate backward branches, forward fate and basin-boundary classification; the fate of one branch decides nothing about ∂𝓑(P₁) | Accepted. r0's "this decides…" sentence is withdrawn. | §4 B2 |
| R4 census: discovery evidence, not completeness; bounded completeness needs validated exclusion; park behind R3 | Accepted | §4 B3 |
| D6 storage: keep immutable adopted files, records and certificates; remove verified duplicates first | Accepted. r0's deletion list is withdrawn. | §6 |
| Revised execution order | Adopted | §1 |

---

## 1. Revised execution order

| Step | Item | Compute | Gate to the next step |
|---|---|---|---|
| 0 | G1 freeze record; G2 source synchronization (v0.3.21, no new mathematics); G3 notices | none / sandbox | source RIDs and notices validated before any new import |
| 1 | **A1a** defect-constant identity | sandbox algebra + light numpy (sandbox or PI) | lifts, block alignment and domains matched |
| 2 | **A1b / A1c** slip schedule and decoder audit | numpy (PI machine for long orbits) | decoder specified before any recoverability claim |
| 3 | **A2** formal involution and orientation ledger | sandbox sympy | — |
| 4 | **B1 Stage A** R9 bound decomposition | sandbox | decides whether Stage B is worth running |
| 5 | **A3 + A4** comparator typing; conditional class-C audit | none | narrowly scoped results; no forced R4/R6 closure |
| 6 | **B1 Stage B**, then **R3-0** sub-campaigns | Arb / mpmath on the PI machine | per budget findings |
| park | B3 R4 census; B1 Stage C; R5/R6 routed items (§5) | — | upstream or PI decision |

A1a and A2 are independent, sandbox-only cells and could run in parallel if wanted. No new RECOG scientific release before the A1 proof/decoder split and the A3 non-closure correction are in the cell texts (review recommendation).

---

## 2. Phase 0 — governance

### G1. External freeze record for v0.3.20 (REQ-O09-02)

- **Records an existing decision; does not make one.**
- **Provenance gap.** The review states the freeze was "already authorized and hash-confirmed in our earlier owner-state exchange". I could not locate that exchange:
  - the project holds no RECOG freeze record;
  - the DSN header says "freeze candidate";
  - the past-chat search returned only consumer citations of the candidate status (OFN, RRF, RER receiving reviews).
- **Needed from the PI:** the date and channel of that authorization. If none exists, the PI decides now and the record says so.
- **Record content:**
  - full hash, re-hashed today;
  - consistency-pass checklist (RID set; OPEN statuses; §5 versus §6; §6.6a scope; §7.1 notice);
  - decision provenance;
  - the consumers that may drop "candidate": OFN IMP-O09-01/02/03, RER G9, Dyadic §7, RRF §4.1a.

### G2. v0.3.21 synchronization (no new mathematics; the v0.3.18 pattern)

1. **Claim-level audit**, using the §7.1 classes:
   - Dyadic v6.4.10 → v6.4.17 for every DYAD import (C21, NF6, NF6-OBS, PRIM-CTR, NF-INV, NF-REM, BRIDGE-LEMMA, ALIAS-PHASE, and the §6.1/6.2/6.3/6.4/6.7–6.8 blocks);
   - Genesis v2.8.4 → v2.8.9 (§6.1, §6.6, J_Q);
   - OFN v0.8 → v0.10;
   - RRF v0.6 → v0.8.3 (convention rows);
   - status of Dyadic OPEN 12 (an R3 dependency).
2. **Receipts:**
   - N10, N11, N12;
   - **N13 conditional:** "received against adopted v6.4.17 (`e07cf2b9…4bfc`); release verification not yet available to this review". The receipt does not claim independent verification.
3. **New §7.2, downstream dependents of RECOG RIDs** (the R9 consumer register):
   - Dyadic T1, T2 and the memory law (v6.4.15);
   - Dyadic OPEN 21 / P5 (v6.4.17);
   - OFN IMP/RF rows;
   - RRF §4.1a;
   - RER G9.

   Standing rule: any change to R9's statement, rows, C₂ or track is noticed before release. A *new* row is additive.
4. **SG-R14 note.** Cite Dyadic T2:
   - M_W − M = −Δ₀(z₀), with |M_W − M| ≤ K₀√q₀;
   - K₀ = 1101/1000 on |z| ≤ 1/20 and 533/500 on |z| ≤ 1/40.

   This quantifies the raw-track clause. It is still no C_W^{(h)} statement.
5. **Hygiene:** companion pins; register the R6 addendum memo in §8.
6. **Header compaction, as a separate mechanical change.** Move the pre-v0.3.18 status summaries and the nested freeze chain into Appendix A. Run a preservation check: every moved line appears byte-identically in its new location, and anchors stay intact. The PI decides whether to do this at all (D2).

### G3. Notices

- **→ RRF:** repin the §4.1a R9 import from v0.3.14 to the current RECOG version (the content is unchanged since v0.3.4).
- **→ OFN, RER:** the freeze-record and v0.3.21 hashes.
- **→ Dyadic:** the §7.2 register and the receipts.

---

## 3. Phase 1 — algebraic cells

### A0. Proposed R6 vocabulary `[DEF]` (from review §9, refined)

| Relation | Meaning | Existing status |
|---|---|---|
| **WRITE** E → K_retained | event-gated update of a retained carrier | = F3(c) C2; absent from the registered single-dyad carriers (RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH) |
| **READ** K_retained → 𝒯 | **[r1 add]** an *exact registered identity* expressing a token-schedule statistic through a named retained observable, with declared side data | new |
| **DECODE** 𝒯 → K̂ | a specified decoder 𝒟 (finite prefix, infinite stream, or limiting schedule) plus declared side data, with uniqueness and stability | new |

- **Guards:** READ ⇏ WRITE; READ ⇏ DECODE.
- **[r1 add] Anti-tautology for READ.** In a deterministic autonomous system every token statistic is a function of x₀. "Depends on the retained state" is therefore Markov-trivial, the same reason F3(a) excludes full-state conditioning. READ requires an identity, not dependence.

### A1. R6 information interface — split cell

**A1a (review A1-P1): defect-constant identity.**
Candidate, with three equivalent forms:

$$\lim_{M\to\infty}\bigl[D_M-\tau\log M\bigr]=\widehat\phi_0-\Psi_\infty(x_0)=\tau\log Q_{W,0}-M_W(x_0)=\tau\log q_0+D_\Theta(z_0)-M(z_0).$$

- D_M = 2πM − (φ̂_{6M} − φ̂₀) and D_M = τ log M + C_D + o(1) are the NG owner law (`NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`).
- Ψ_∞ = Ψ_{W,∞}, by Dyadic T1, conditional on R9.
- D_Θ = arg(W/z) is the static chart phase offset.
- The last form uses T2, M_W = M − Δ₀, with Δ₀ = D_Θ − τ log(1 + D_Q/q), and Q_W = q + D_Q.

**[r1 add] Honest weight.** Given T1, the first equality is close to definitional:

D_M − τ log M = φ̂₀ − Ψ_W(6M) − τ log(M·Q_{W,6M}),

and the last term → 0 because 1/Q_{W,M} = M + O(√M). Its content is:

1. cross-owner consistency of NG's C_D with RECOG/Dyadic's Ψ_∞;
2. a **certified explicit evaluation**, via Dyadic P5:
   C_D = τ log Q_{W,0} − 𝒫₂(W₀) + E, with |E| ≤ K′_j Q₀^{3/2} + C_{2,j}(256/225)² Q₀² (rows A/B);
3. locking the conventions.

**Tasks:**
- lift identity (owner φ̂_n = θ_n + 2πc_n versus Dyadic's lifted W-phase);
- block alignment of x₀;
- orientation (SG-R9);
- domain intersection: NG local tube ∩ Dyadic rows A/B (|W₀| ≤ 3/64, 3/128) ∩ R9 rows;
- `[NUM]` check on the 12 F2(b) orbits: C_D from the D_M tail versus Ψ_∞ from the Ψ_W tail versus the P5 closed form.

**Target:** `[ALG consequence]` (conditional on T1/R9) for the limit identity; `[THM — conditional on R9 + DYAD T1/T2/P5 + NG N-5A-S1]` for the explicit form.

**A1b: asymptotic slip schedule.**

The F2(d) identities give the bookkeeping constant
C = G_{n_j} + o_j − (π/3)s_j = (π/3)n₀ − 2πℓ₀ + φ̂₀,
which uses only first-anchor index, lap and initial phase. Combined with the owner law D_{M_k} = C + (k−1)π/3 + o(1), this gives the candidate

$$\lim_{k\to\infty}\Bigl[\tau\log M_k-(k-1)\tfrac\pi3\Bigr]=\tfrac\pi3 n_0-2\pi\ell_0+\Psi_\infty(x_0).$$

This states READ for Ψ_∞. It still has to be checked against the owner definitions:
- the k-labelling;
- slip_start versus slip_end;
- n_{j_k} = 6M_k + r_k;
- the lap convention ℓ₀.

**A1c (review A1-P2): decoder audit.**

Candidate layering, to be tested and not asserted:

| Target | Decoder and side data | Expected status |
|---|---|---|
| Ψ_∞ (chart-free asymptotic phase, T⁶-invariant along the orbit) | 𝒟_∞: infinite slip record + first-anchor bookkeeping (n₀, ℓ₀); no state data | candidate DECODE, if A1b holds |
| Ψ_∞ from a finite prefix (up to slip k) | same, truncated | localizes only to width ≈ τ/M_k + (the o(1) rate); **non-injective**. Test on comparator fibers, as the review asks. |
| M_W = Ψ_∞ − Ψ_W(x₀) | needs θ_{W,0} *and* Q_{W,0}, i.e. the full initial state W₀ | **not** an independent read-out |
| M (R9, C_z track) | needs z₀ = h^{-1}(W₀) | not independent |

**[r1 add] Fiber caution.** On a comparator fiber 𝓕_{q,δ}, the pairwise difference of C_D is
D_Θ(z_b) − D_Θ(z_a) − ΔM.
The first term is the O(√q₀) static chart offset; R9's comparator-invisible lattice memory ΔM is O(q₀). The token schedule therefore reads the asymptotic phase, of which R9's lattice memory is a *subleading* component, separable only with state data.

**Consequence to check, if 𝒟_∞ exists:**
- Ψ_∞ is token-recoverable *in the limit*;
- R9's R_ind status (it concerns M, which needs the state) and F2(d)'s R_log verdict (finite marks H_j) should be unaffected;
- the anti-tautology guard then needs an explicit finite-versus-limit qualifier.

**Grade:** A1c stays `[OPEN]` until a decoder with uniqueness and stability is shown.

**What A1 cannot do:** establish WRITE (C2 stays absent), or adopt any event (SG-R6).

### A2. Formal involution and orientation ledger (R1; R5-P3; §6.6–6.7 wording)

**Object / action / regularity ledger `[DEF]`** (aliases marked):

| Object | Action type | Regularity, status | Relations |
|---|---|---|---|
| S_o = −I on the lift | linear point reflection of the lift chart | exact, global | S_o T_k S_o = T_{−k} (RECOG §6.6a); a symmetry of T_k iff T_k is odd |
| R₀^{(k)} = T_k³ F_k^{−1/2} | dynamical: commutes with T_k | **formal existence for every germ with A³ = −I**; uniqueness under Re μ·Im μ ≠ 0 (Dyadic formal centralizer); analytic only under its own B-an^{(k)}, a per-k hypothesis not inherited from k = 1 | for k = 1: R₀ = J³ (alias, not a separate object) |
| S_h = h∘(−I)∘h^{−1}; LIFT form 𝓛^{−1}S_h𝓛 | representation-level finite-chart involution | exact involution; commutes with the dynamics to degree 6 | equals R₀ through the degree-6 jet under the shared normalization (owner: Dyadic v6.4.12 §6.16, as received in RRF v0.8.3 §4.2); **re-check in the cell** with the 𝓛 transport and truncation |
| J = T∘F^{−1/6} | formal ℤ₆ generator | formal; B-6 OPEN | J³ = R₀ |
| wrapped ζ ↦ ζ^{−1} | representation action on the wrapped pole ratio | exact relabeling candidate | agrees with the LIFT action at linear order only (RRF OPEN-A) |

**Results to establish** (derivations in Appendix A.2):

- **(a) `[ALG]` formal existence.** It needs only uniqueness of the formal log; uniqueness of R₀ needs Re μ·Im μ ≠ 0.
- **(b) `[ALG]` R₀ = S_o ⟺ T odd (formal).**
  - R₀ = S_o for T_s, T_log = T₀ and T_tanh.
  - For T_k with k ≠ 0, R₀ ≠ S_o, and its degree-2 part is the homological image of 2T_b. At k = 0, R₀ = S_o exists, but Dyadic's uniqueness hypothesis fails (Re μ₆(0) = 0), so no uniqueness is asserted there.
- **(c) `[ALG]` tangent-to-identity orientation equivalence.** Φ_k = S_o R₀^{(k)}, DΦ_k(0) = I, and Φ_k T_k Φ_k^{−1} = T_{−k} for formal germs at P₁, k ≠ 0.
  - `[RESULT] [from: ALG]` (review wording): formal local conjugacy cannot distinguish the two orientations. Analytic realization, global extension, physically admissible pole exchange, complete-state encoding, *and an externally specified oriented physical carrier* remain separate questions; the last is exactly OPA's.
- **(d) Wording and scope (no claim change).**
  - In §6.6–6.7 and the §5 row "healing from symmetry breaking", "swap breaking" means S_o-breaking.
  - T is formally R₀-symmetric. Healing versus expansion is decided by μ, not by the presence of a −I-linear symmetry.
- **(e) R1 `[HYP]` sharpened.** Formal −I-linear covariance is automatic, so the §6.4 covariance premise is selective only for a *declared* involution. Which involution is physical is OPEN-A / OPA.

**Compute:** sandbox sympy, degree ≤ 6:
- (b) for T_s;
- the degree-2 term of R₀ for T;
- Φ conjugacy for k = ±1;
- the S_h / R₀ jet agreement.

R1 does not close.

### A3. Pole-quadrature typing (R4)

- **`[ALG]` RECOG-ALG-POLE-QUADRATURE-TYPING** (primitive chart, pole-comparator track):
  - cos η = 0 ⟺ Ĉ_pole = ±i;
  - for ρ > −ln 4, primitive one-step transport is rotational where Re Ĉ_pole > 0 and stretching where Re Ĉ_pole < 0 (Δ_J = c(c − 4e^ρ), with c = Re Ĉ_pole).
- **R4(1) stays OPEN.** Under F′ = hFh^{−1}, DF′_{h(x)} = Dh_{F(x)} DF_x Dh_x^{−1}, which is not a similarity when F(x) ≠ x. A comparator level set is typing, not an intrinsic dynamical counterpart.
- **Proposed rewording of the target:** "a conjugacy-invariant or covariantly defined structure — periodic-orbit multipliers, return invariants — capturing the one-step type transition".

### A4. Conditional W1–W5 audit against OFN class C (R6 network successor)

**Object:** OFN v0.10 §5.5.4, F^N_κ(z)_e = N(z_e) − (κ/3)Σ_j N(z_j), on a triangle; transported chart; lock surfaces 𝒮₀ and 𝒮_±. It is a declared conditional model, **not** an RRF-registered carrier. Model-defined cochains are not promoted to physical carriers.

| Gate | Preliminary disposition | Qualification |
|---|---|---|
| W1 graph / cochain | conditional mathematical PASS | triangle, ℂ-valued cochain; no physical dyad → edge realization |
| W2 token-preserving attachment | OPEN | **[r1 add]** the canonical B-predicate is defined on primitive variables; on a class-C edge it needs z_e ↦ primitive via h_form, whose realization is conditional on DYAD OPEN 20 (B-6 / B-∞). The token is therefore itself only conditionally defined there. On 𝒮_± the edge states are related by G = J²; that relates *different edges' streams* and is not a change of token rule on any edge (F2(a) intact). |
| W3 same cohomology space | conditional PASS | fixed graph, H¹(G;ℂ) ≅ ℂ, common edge typing, comparable pre/post cochains |
| W4 independent retention | not established | Ca⁻ = Ca⁺ = 0 ⇒ Δ[a] = 0 on lock surfaces: a **negative control**, not evidence of general absence |
| W5 common-driver quotient | OPEN | needs a specified quotient and an identifiable event-conditioned update |

- **Before any no-write statement, verify:**
  - the class-C defect update (1−κ)ΣN is smooth on the declared domain;
  - the token predicate is well-defined there (see W2);
  - no independently specified event channel exists.
- **Target conclusion (narrow):** "Under the specified smooth class-C update and without an additional event-gated channel, the current model supplies no identifiable C2 write-through mechanism for its registered cochain carrier."
- This is not a general theorem about networks. Timing is decision D3.

---

## 4. Phase 2 — compute cells

### B1. R9 constant

**Stage A (sandbox, first).** Decompose the owner proof's constant from `recog_cell_r9_memory_cert.py`, term by term as the proof defines them. Do not assume an additive split.
- For each term: its inequality, its radius dependence, and its correlation with the others (r0's "C₇ ≈ 37–39% of K_Φ" is only a first observation).
- Test low-cost improvements first: phase-aware bounds, and not bounding correlated errors independently.
- Output: a budget table and a go/no-go for Stage B.

**Second benchmark (Dyadic-owned, RECOG input).** A separately certified direct bound on |M_W − 𝒫₂(W₀)| for Dyadic OPEN 21. No numerical cancellation is transferred.

**Stage B (Arb, PI machine), after A.**
- A new (C₂, q_max) row, either from tightened RECOG inequalities or from a sharper Dyadic C₇ row.
- Additive to the existing rows; noticed under §7.2.
- Reference targets, not predictions: C₂ ≤ |G|·1600 ≈ 12.2 makes the incompleteness window cover the small row (q₀ ≤ 1/1600); C₂ ≤ |G|·400 ≈ 3.06 does so for the large row.

**Stage C (parked).** Degree-7 jet plus a C₈ remainder, only if Stage A identifies a bottleneck that needs higher-order terms.

### B2. R3 — W^s(P₂): three independent sub-campaigns

T is not globally invertible, so W^s(P₂) = ∪T^{−n}W^s_loc. Its principal branches are not the whole stable set.

| Sub-campaign | Question | Grade path |
|---|---|---|
| R3-0a | backward continuation of W^s_±(P₂) by the local inverse branch; first encounters with the critical-value curve T(C₀) and the resulting branchings | `[NUM]` → B3-style `[THM]` for a first-encounter statement |
| R3-0b | forward fate of W^u₊(P₂) beyond its certified first C₀ hit | `[NUM]` |
| R3-0c | basin-boundary classification (W^s(P₂) ⊆ ∂𝓑(P₁)?) | needs its own topological or dynamical argument; **not** decided by R3-0b |

Dependency: the status of Dyadic OPEN 12 (G2 audit).

### B3. R4(2) periodic-orbit census (parked behind R3)

- A Newton census with deduplication is `[NUM]` discovery evidence only.
- A bounded completeness statement (all orbits of period ≤ N in box B) needs validated domain coverage, i.e. interval Newton or Krawczyk *exclusion* certificates for every unresolved box.
- Krawczyk *existence* certificates for selected orbits can reuse the E3A-3a engine.

---

## 5. Routed and parked items (unchanged from r0)

| Item | Blocking owner / reason | RECOG posture |
|---|---|---|
| R5-P1 composition | RRF: multiplicative edges / H_× not registered; OPEN-B → E1 | one precise request in G3 |
| R5-P2 weight \|k\| = 1 | not derivable inside the dyad (k first enters at quadratic order) | optional `[HEUR]` for OFN: the identity character |
| R5 saturation reading | needs a nonlocal test design | park; retire unless a test is specified |
| R1 adoption / P3 physical orientation | OFN OPEN-OFN-OPA; RRF OPEN-A | A2 supplies the typed ledger and formal equivalence |
| R6 route 1 (new single-dyad carrier) | would require inventing physics | park; audit with F3(c) if one is proposed |
| R6 selection principle; network successor | genuinely open; RRF OPEN-B/E1/E2; NG-7B | A1 and A4 narrow it; no adoption (SG-R6) |
| R7 genericity / full measure | deliberately not claimed; SG-R4 | park |
| ER-2B C11–C12 lane | ER-2B-initiated | respond if invoked |
| Dyadic OPEN 20 | Dyadic | conditions A2(c)'s analytic upgrade (per k) and A4's W2 |

---

## 6. Decision points for the PI

| # | Decision | Recommendation |
|---|---|---|
| D1 | Provenance of the v0.3.20 freeze authorization (date and channel), or the decision now if none exists | Supply the provenance; G1 records it. |
| D2 | v0.3.21 sync scope; whether to do the header compaction | Sync only; compaction as a separate checked mechanical change. |
| D3 | A4 now (conditional) or after RRF decides on class-C registration | Now, as conditional; it is short. |
| D4 | B1 depth | Stage A now; Stage B on the A verdict; Stage C parked. |
| D5 | PI-machine time | A1b/A1c long orbits, then R3-0a/0b; R4 census parked. |
| D6 | Storage (project at 95.7%) | Remove only *verified byte-identical duplicates* first (e.g. `claude/` copies of files also at the root, after a hash match). Keep adopted files, release records, certificates and load-bearing proof records. |

---

## 7. Release map (conditional)

| If… | then |
|---|---|
| G1 provenance supplied | the freeze record is written |
| G2 audit complete | v0.3.21 (sync, no new mathematics) |
| A1a passes its convention, domain and `[NUM]` checks | one R6 micro-release (A1a; A1b/A1c registered as OPEN sub-items or results, as earned) |
| A2 (+ A3 typing) checks pass | one R1/R4 micro-release |
| A4 verified | one registry-relative R6 result |
| B1 Stage B certifies a row | an R9 row addition with a §7.2 notice |

Numbers are assigned only at release.

---

## Appendix A — derivations (to be verified inside the cells)

### A.1 Defect constant and slip schedule

**Defect constant.**
- With Θ_{W,M} := φ̂_{6M} − 2πM: D_M = Θ_{W,0} − Θ_{W,M}, and Ψ_W := Θ_W − τ log Q_W → Ψ_∞ (T1).
- Raw Q_W obeys Q′ = Q − Q² + O(Q^{5/2}). Hence 1/Q_{W,M} = M + O(√M), so τ log Q_{W,M} = −τ log M + o(1).
- Therefore D_M − τ log M → Θ_{W,0} − Ψ_∞ = φ̂₀ − Ψ_∞.
- Rewritings:
  - Ψ_W(x₀) = θ_{W,0} − τ log Q_{W,0} gives τ log Q_{W,0} − M_W;
  - T2 together with Q_W = q + D_Q gives τ log q₀ + D_Θ − M.

**Bookkeeping constant.** With n_j = n₀ + 6j + s_j, φ̂_{n_j} = 2πℓ_j + o_j and ℓ_j = ℓ₀ + j:

G_{n_j} + o_j − (π/3)s_j = (π/3)n₀ − 2πℓ₀ + φ̂₀ = C.

**Slip schedule.** Then τ log M_k = C − C_D + (k−1)π/3 + o(1) gives the A1b formula.

**Check list:**
- s₀ convention;
- the definition of M_k_phys;
- whether the owner law's o(1) is uniform enough for the decoder's stability claim.

### A.2 Involutions

**(a) Formal existence.** Let DT(0) = A with A³ = −I. X = log F is unique, and T*X = X because TF = FT. Hence F^{−1/2} = exp(−X/2) commutes with T, and R₀ := T³F^{−1/2} satisfies:
- R₀² = T⁶F^{−1} = id;
- DR₀(0) = −I;
- R₀T = TR₀.

**(b) R₀ = S_o ⟺ T odd.**
- If T is odd, U := −T³ satisfies U² = T⁶ and DU(0) = I. Uniqueness of the tangent-identity formal square root gives F^{1/2} = −T³, hence R₀ = −I.
- Conversely, R₀ = −I commuting with T means T is odd.

**Degree 2.** r₂(Ax) − A r₂(x) = 2T₂(x), where T₂ = (0, ρ²/2) is the quadratic part of T_b. There is no degree-2 resonance at p = 6.

**(c) Orientation equivalence.**
- Φ_k T_k Φ_k^{−1} = S_o R₀ T_k R₀ S_o = S_o T_k S_o = T_{−k};
- DΦ_k(0) = (−I)(−I) = I;
- equivalently, the λ-equivariant formal normal forms of T_{±k} coincide because N is odd.
