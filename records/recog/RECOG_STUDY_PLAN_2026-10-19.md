# RECOG Study Plan — review of v0.3.20 and next work

**Date:** 19 October 2026
**Status:** `[SESSION]` planning record. No DSN is edited. Every grade below is a *target*, not a claim. The PI makes the final decisions.
**Base:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20`
- SHA-256 `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df` (re-hashed locally today; matches the project root copy).
- 1,430 lines; freeze candidate in its own header. **No external freeze record exists yet.**

**Corpus read for this plan:**
- Dyadic v6.4.16, plus v6.4.17 (adopted today; reviewer release verification pending) and notices N11–N13;
- OFN v0.10 and its release record;
- RRF v0.8.3; RER v0.2 r4.6; Genesis v2.8.9; FMS ledger v0.6.4;
- targeted searches of Triadic v1.6.1, OPEN-M v0.7.1 and ER-2B v0.3.

---

## 0. Bottom line

1. **RECOG's mathematics is in good shape; its interfaces are not.**
   - 6 of 11 OPENs are closed, with 6 theorem-grade results.
   - Four other streams now *depend* on RECOG: Dyadic (3 conditional theorems rest on R9), OFN, RRF and RER.
   - Yet v0.3.20 has no freeze record, still pins Dyadic v6.4.10 and OFN v0.8, and has four unanswered Dyadic notices (N10–N13).
   - Fixing this is cheap and unblocks other owners. It comes first (Phase 0).
2. **The new upstream results open three inexpensive, algebra-only RECOG cells.**
   - **A1 (R6).** Dyadic's T1/T2/P5 suggest an exact identity: Number Genesis' slip-locking constant equals the retained memory, `C_D = τ log Q_{W,0} − M_W(x₀)`. The canonical B/7-gap token stream would then be a *read-out* of R9's independent memory. This is the most valuable next cell.
   - **A2 (R1/R5).** Dyadic's formal involution `R₀ = T³F^{-1/2}` makes *formal* pole-swap covariance automatic for every p = 6 germ. This sharpens R1's `[HYP]`, and it retypes the "swap-breaking" language of §6.6–6.7 as breaking of the linear swap S_o only.
   - **A3 (R4).** The parabolic locus cos η = 0 is exactly the pole-comparator quadrature Ĉ_pole = ±i. Sub-item 1 of R4 can close.
3. **One compute cell has a downstream payoff: R9's C₂ (B1).**
   - Today's certified incompleteness window is 13–170× smaller than the memory theorem's domain.
   - C₂ enters Dyadic's new OPEN 21 constant directly.
4. **R3 and the R4 periodic-orbit inventory are worthwhile but optional** compute campaigns for the PI machine.
5. **R5-P1, the network side of R6, and R6's selection principle stay routed or blocked upstream.** These are RRF OPEN-B/E1, multiplicative edges, OFN-OPA and NG-7B. RECOG's job there is to keep its requests precise, not to invent carriers.

---

## 1. Review: where RECOG stands

### 1.1 Certified inventory (v0.3.20)

| Layer | Theorem-grade `[THM]` | Key `[ALG]` / `[RESULT]` |
|---|---|---|
| Return defect | — | shear-jet law μ₆(a,b); cubic-return rigidity \|μ₆\| ≥ ½; ν₃(λ) closed form, so k_ret(p) = 3 for all p ≥ 5; leading-return equivariance; comparator closure through degree p−2 |
| Lattice / memory | **RECOG-THM-R9-MEMORY** with its C_z incompleteness corollary | lattice strength, clock λ_DSI^{1/6}, leading Λ₁; chart laws and the R11 ledger |
| P₂ manifolds | **P2-HET** (W^u₋ → P₁, avoids C₀); **P2-C0-FIRST** (unique first transverse C₀ hit) | — |
| Twin T_s (diagnostic only, SG-R4) | **TWIN-RADIAL-ACCESS**; **TWIN-STAGE2-NONUNIVERSAL**; **TWIN-C0-ACCESS** | P9 saddle and local stable graph `[ALG via IA]`; crossing-step rank safety; Q_c degeneracy |
| Shear origin (R5) | — | cocycle classification g_k; inversion projection; **orientation conjugacy** S∘T_k∘S = T_{−k}; weight identification \|k\| = 1 |
| Event rule (R6) | — | F1 underdetermination; F2(a) B-token transport; F2(b) chart shadow; F2(c0) Whitney fold; F2(c1) no registered fold retention; F2(d) B-token ≡ R_log; F3 continuous-carrier no-write and R9 no write-through; F4 network well-posedness with W1–W5 |

### 1.2 OPEN census and what is actually left

| OPEN | Status | Residual content | Assessment |
|---|---|---|---|
| R1 radial swap parity | PARTIAL | adopting oriented ρ as an OFN primitive (held by OPEN-OFN-OPA); status of pole-swap covariance `[HYP]` | **Movable now on the RECOG side** (A2). The covariance premise can be typed by *which* involution. Closure stays with OFN. |
| R2, R7, R8, R9, R10, R11 | CLOSED | — | R9 is closed, but its constant C₂ is now a downstream bottleneck (B1). |
| R3 P₂ band geometry | PARTIAL | global geometry of W^s(P₂) | Well defined, compute-heavy. Needs a working definition first, because T is not globally invertible (B2). |
| R4 type-change locus | ACTIVE | (1) coordinate-free counterpart of cos η = 0; (2) global periodic-orbit inventory | (1) closable cheaply (A3); (2) compute census (B3). |
| R5 one-sided shear | ACTIVE | P1 composition (routed); P2 weight magnitude (identified, not derived); saturation reading | P3 is already resolved on the RECOG side. P1 is blocked on unregistered multiplicative edges. P2 can only gain a `[HEUR]` principle. |
| R6 event rule | ACTIVE | selection principle; token → R_ind coupling; network successor (W1–W5) | Single-dyad channel: closed negatively for write-through. The **read-out** direction is unexamined (A1). Network side: blocked on OPEN-B, but OFN's class C allows a conditional audit (A4). |

### 1.3 Who now depends on RECOG

| Consumer | What it uses | Pin | RECOG action |
|---|---|---|---|
| Dyadic v6.4.15–17 | `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` (T1, T2, memory law) and `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER`, all **conditional on RECOG-THM-R9-MEMORY** at statement level (Λ₁, c_iso, C₂ = 517/163, q_max, C_z) | v0.3.20 | receipts N10–N13; register the dependency; flag any R9 change |
| OFN v0.10 | IMP-O08-17/18/19, IMP-O09-01/02/03 ("freeze candidate"), RF-O09-01/02; **REQ-O09-02 asks for the RECOG freeze record** | v0.3.20 | freeze record; consumer audit |
| RRF v0.8.3 | §4.1a R9 import, §2 R11 conventions, §6.6a/§6.16b/§6.16g citations | R9 rows still cite **v0.3.14** | notice to repin (the content is unchanged since v0.3.4) |
| RER v0.2 r4.6 | G9 cites RECOG first as owner (§6.6a; §6.16g, lines 1002–1042, verified correct) | fdb8c9a7, "freeze candidate in header" | freeze record |
| ER-2B v0.3 | optional C11–C12 request lane (A.5) | — | answer only if invoked |

### 1.4 Upstream changes since RECOG's pins

| Owner | RECOG pins | Current | Relevance |
|---|---|---|---|
| Dyadic | v6.4.10 | **v6.4.17** (adopted 19 Oct; release verification pending) | imports NF6, NF-INV, NF-REM, PRIM-CTR, C21 and the bridge lemma need a claim-level audit; new formal involution / ℤ₆ generator (v6.4.12–13) bears on R1; OPEN 3 / OPEN 21 results enable A1 |
| Genesis | v2.8.4 | v2.8.9 | §6.1/§6.6 comparator and J_Q imports need a claim-level audit |
| OFN | v0.8 | v0.10 | §5.5 class C bears on R6/W1–W5 (A4); OPA unchanged |
| RRF | v0.6 (convention), v0.4 (R11) | v0.8.3 | OPEN-B → E1 → E2 still locked; class C registration request pending at RRF |
| Number Genesis | v1.20.7 | v1.20.7 | current |
| Triadic / OPEN-M | none | v1.6.1 / v0.7.1 | no RECOG import |

### 1.5 Health issues found

1. **No external freeze record for v0.3.20.** Four consumers cite it as a "freeze candidate".
2. **Stale companion pins** in the header: Dyadic v6.4.10, Genesis v2.8.4, OFN v0.8. The Programme Overview still selects RECOG v0.3.
3. **Four Dyadic notices unanswered** (N10–N13).
4. **R9 export interface lacks a consumer register.** §6.9 lists R9 as exportable, but nowhere records that three adopted Dyadic theorems are conditional on it. A silent R9 change would break them.
5. **SG-R14's raw-track clause is qualitative** ("generically O(√q₀)"). Dyadic T2 now quantifies it exactly: `M_W − M = −Δ₀(z₀)`, `|Δ₀| ≤ K₀√q`.
6. **Header bloat.** All status summaries back to v0.1 and a 15-level nested freeze chain sit above §1 (lines 12–56). Consumers have to read through history to reach the current state.
7. **The R6 addendum memo** (`RECOG_MEMO_TO_STREAMS_2026-09-30_R6_ADDENDUM.md`) is not registered in §8.

---

## 2. Plan overview

| Phase | Item | Type | Target grade | Compute | Depends on | Release |
|---|---|---|---|---|---|---|
| **0** | G1 v0.3.20 freeze record | governance | — | none | PI decision D1 | record file |
| **0** | G2 sync micro-release | governance, no new mathematics | — | sandbox (hashes, claim diffs) | G1 | **v0.3.21** |
| **0** | G3 outbound notices | governance | — | none | G2 | memo |
| **1** | A1 CELL-F5 token read-out of R9 (R6) | algebra + light numerics | `[ALG consequence]` / `[THM — conditional]`; check `[NUM]` | sandbox or PI (numpy, minutes) | G2 (N11/N13 receipts) | v0.3.22 |
| **1** | A2 typed involution ledger (R1, R5-P3, §6.6) | algebra | `[ALG]` (formal) + `[DEF]` | sandbox (sympy sanity) | G2 (Dyadic v6.4.12–13 pins) | v0.3.23 |
| **1** | A3 R4(1) via pole-comparator quadrature | algebra | `[ALG]` | none | — | with A2 |
| **1** | A4 CELL-F6 class-C well-posedness audit (R6) | registry audit | `[RESULT]`, conditional | none | OFN v0.10; RRF class-C decision optional | v0.3.24 |
| **2** | B1 R9 C₂ sharpening | proof engineering | `[THM]` (new row) | stage A sandbox; stage B Arb on PI machine | Dyadic NF-REM machinery | v0.3.25 + notice |
| **2** | B2 R3 W^s(P₂) global geometry | scouting, then certificate | `[NUM strong]` → `[THM]` | PI machine (mpmath / Arb) | definition fixed first | later |
| **2** | B3 R4(2) periodic-orbit census | census + certificates | `[NUM strong]` + `[ALG via IA]` | PI machine | E3A-3a Krawczyk engine | later |
| **3** | routed and parked items (§6) | — | — | — | upstream owners | — |

Workflow per cell, as in the corpus:
1. Claude drafts the cell, plus a script where needed.
2. Mustafa runs any heavy computation on the RTG machine.
3. The contributor critiques; Claude verifies and integrates.
4. Freeze check, then a micro-release.

---

## 3. Phase 0 — governance

### G1. v0.3.20 freeze record (REQ-O09-02)

**Proposed file:** `RECOG_v0_3_20_FREEZE_RECORD.md`, containing:
- the full hash;
- a consistency-pass checklist: RID set; OPEN statuses; §5 rows against §6; the §6.6a scope sentence; §7.1 OFN notice;
- the PI freeze decision;
- the list of consumers that may now drop "candidate".

No DSN text changes.

### G2. v0.3.21 synchronization micro-release (no new mathematics; the v0.3.18 pattern)

1. **Claim-level consumer audit** (§7.1 classes: identical, strengthened, restructured, semantically changed, new):
   - Dyadic v6.4.10 → v6.4.17, for every DYAD import in §7: C21, NF6, NF6-OBS, PRIM-CTR, NF-INV, NF-REM, BRIDGE-LEMMA, ALIAS-PHASE, and the §6.1/§6.2/§6.3/§6.4/§6.7–6.8 blocks.
   - Genesis v2.8.4 → v2.8.9 (§6.1, §6.6, J_Q).
   - OFN v0.8 → v0.10 (§6.2a, §7.3, the OPA wording).
   - RRF v0.6 → v0.8.3 (convention rows only).
   - Check whether Dyadic OPEN 12 (an R3 dependency) is still open.
2. **Receipts.**
   - N10 (OPEN 3a per-block residual).
   - N11 (OPEN 3b: T1, T2, memory law).
   - N12 (lifecycle).
   - N13 (OPEN 21 / P5), only after the reviewer's release verification of v6.4.17, as its notice requires.
3. **New §7.2 "Downstream dependents of RECOG RIDs"** (the R9 export-consumer register; see §1.3).
   - Standing rule: any change to R9's statement, rows, C₂ or track goes out as a notice before release.
   - Adding a *new* row (B1) is additive and does not break existing dependents.
4. **SG-R14 quantitative note.** Cite `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` T2:
   - on the primitive asymptotic-phase track, `M_W − M = −Δ₀(z₀)`;
   - `|M_W − M| ≤ K₀√q₀`, with K₀ = 1101/1000 for |z| ≤ 1/20 and 533/500 for |z| ≤ 1/40.
   - This replaces "generically O(√q₀)" with an owner-certified statement. It is still not a C_W^{(h)} statement.
5. **Header and hygiene.**
   - Update the companion pins.
   - Register the R6 addendum memo in §8.
   - *Optional (PI decision D2):* move the pre-v0.3.18 status summaries and the nested freeze chain to Appendix A, so that the header carries only the current state plus a one-line freeze table.

### G3. Outbound notices (memo `RECOG_MEMO_TO_STREAMS_2026-10-xx.md`)

- **→ RRF:** repin the §4.1a R9 import from v0.3.14 to v0.3.21. The content is unchanged.
- **→ OFN, RER:** the freeze record exists; the v0.3.21 hash.
- **→ Dyadic:** receipt lines (in the DSN), and the §7.2 dependency register.

---

## 4. Phase 1 — algebraic cells (no heavy compute)

### A1. CELL-F5 — the B/7-gap token stream as a read-out of R9 memory (R6)

**Why now.**
- F2(d) classified the owner's slip-locking law as "predictability, not retention".
- F3 noted that token descriptors and R9 memory are functions of one hidden phase.
- Dyadic T1/T2/P5 now give the raw-track asymptotic phase as a theorem (conditional on R9). That should make the link exact.

**Candidate identity** (derivation sketch in Appendix A.1; this cell must verify the conventions):

$$C_D(x_0)=\tau\log Q_{W,0}-M_W(x_0)=\tau\log Q_{W,0}-M(z_0)+\Delta_0(z_0),$$

where:
- D_M = 2πM − (φ̂_{6M} − φ̂₀) = τ log M + C_D + o(1) is the Number Genesis law (`NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`);
- M_W = Ψ_{W,∞} − Ψ_W(x₀).

With Dyadic P5 this becomes explicit in primitive variables:

$$C_D=\tau\log Q_{W,0}-\mathcal P_2(W_0)+E,\qquad |E|\le K'_jQ_0^{3/2}+C_{2,j}(256/225)^2Q_0^2.$$

Combined with the owner slip law D_{M_k} = C + (k−1)π/3 + o(1), where C is the bookkeeping constant of F2(d), the log-offset of the slip schedule is fixed by the retained memory:

$$\tau\log M_k-(k-1)\tfrac{\pi}{3}\ \to\ C-\tau\log Q_{W,0}+M_W(x_0).$$

**What it would establish (and not establish).**
- *Would establish:* the canonical token stream *reads out* R_ind. The coupling R_ind → token is exact, which makes F3's C0 "common driver" an identity rather than a correlation.
- *Would not establish:* token → R_ind write-through. C2 remains absent; RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH stands.
- *R6 profile change:* "B/7-gap: token + transition + R_log; schedule offset reads R_ind". This makes theorem-grade the "samples Λ" half of the existing R6 `[HYP]` on readability emergence, without promoting any event (SG-R6).

**Steps.**
1. Fix conventions: sign of arg W versus Θ; block alignment; lift; Q_W = Q_prim = |W|².
2. Prove the limit identity, using 1/Q_{W,m} = m + O(√m), so that τ log(M Q_{W,M}) → 0.
3. Intersect the domains: the NG local tube versus Dyadic rows A/B (|W₀| ≤ 3/64, 3/128) versus R9 rows.
4. `[NUM]` check: extend `recog_cell_f2b_token_bridge.py` rev. 2.
   - On its 12 orbits, compute C_D from the D_M tail.
   - Compute M_W from the Ψ_W tail.
   - Compare both with τ log Q₀ − 𝒫₂(W₀).
   - numpy only; minutes on the PI machine, feasible in the sandbox.
5. Notices: NUMGEN (an explicit certified formula for its C_D); OFN (an RF-O09-02 inventory update).

**Grade target:** `[ALG consequence]` for the identity; `[THM — conditional on R9 + DYAD T1/T2/P5 + NG N-5A-S1]` for the explicit form.
**Guards:** SG-R6 (no event adoption); SG-R14 (raw track only through Dyadic's theorems); SG-19 (no NUMGEN coefficient transfer beyond what the identity states).

### A2. Typed involution ledger (R1; R5-P3; §6.6–6.7 wording)

**Why now.** Dyadic v6.4.12–13 registered `DYAD-THM-FORMAL-INVOLUTION-UNIQUE` (R₀ = T³F^{-1/2}) and `DYAD-THM-FORMAL-Z6-GENERATOR` (J = T∘F^{-1/6}, R₀ = J³). RECOG still uses one undifferentiated "pole swap".

**Content** (derivations in Appendix A.2):
1. **Ledger `[DEF]`** of the five registered involution objects:
   - S_o = −I on the lift (exact, linear);
   - R₀ (formal, commutes with T);
   - S_h (finite chart; equals R₀ through degree 6);
   - J³ (formal ℤ₆);
   - wrapped ζ ↦ ζ^{-1}.
   For each RECOG statement, record which one it uses: §6.4 selection lemma, §6.6 swap split, §6.6a conjugacy, §6.14, F2(a) S_h.
2. **`[ALG]` Formal covariance is automatic.** For *any* germ with DT(0) = A, A³ = −I, the map R₀ = T³F^{-1/2} is a formal involution with linear part −I that commutes with T. This uses only the uniqueness of the formal log; uniqueness of R₀ uses Re μ·Im μ ≠ 0.
   - So formal pole-swap covariance has **no selective power**.
   - The R1 premise is selective only for a *declared* involution, and choosing it is OPEN-A / OPA.
   - This sharpens R1's `[HYP]` sub-item into the question "which involution?".
3. **`[ALG]` T_b measures R₀ ≠ S_o.** R₀ = −I exactly iff T is odd. For T_s, R₀^{(s)} = S_o.
   - The degree-2 part of R₀ for T is the homological image of 2T_b.
   - Consequence for §6.6–6.7 and §5 ("healing from symmetry breaking"): "breaking" means S_o-breaking. T is formally R₀-symmetric. Healing versus expansion is decided by μ, not by the presence of a −I-linear symmetry.
   - This is a wording and scope change; no claim changes.
4. **`[ALG]` Tangent-to-identity orientation equivalence.** Φ_k = S_o∘R₀^{(k)} satisfies Φ_k T_k Φ_k^{-1} = T_{−k} and DΦ_k(0) = I.
   - So the germs of T_{±k} at P₁ are formally equivalent even with the linear swap forbidden. This strengthens consequence (i) of the orientation-conjugacy result.
   - The analytic version follows if Dyadic B-an holds; the converse is open.
   - Orientation can therefore only be global or analytic structure. This is a notice for OPA and RRF OPEN-A.

**Compute:** sympy sanity checks in the sandbox (degree ≤ 6):
- R₀^{(s)} = −I;
- the R₀ degree-2 term from T_b;
- Φ conjugacy.

**Grade target:** `[ALG]` (formal), conditional on the Dyadic formal RIDs where uniqueness is used. R1 does not close: OFN owns adoption.

### A3. R4 sub-item 1 via comparator geometry

**`[ALG]` (primitive chart, pole-comparator track).** From §6.5, Δ_J = c(c − 4e^ρ) with c = cos η = Re Ĉ_pole. Hence:
- the parabolic locus cos η = 0 is exactly the pole-comparator quadrature {Ĉ_pole = ±i};
- for ρ > −ln 4, primitive transport type is rotation where Re Ĉ_pole > 0 and stretching where Re Ĉ_pole < 0.

**Disposition.** The question asks for a coordinate-free counterpart "via periodic-orbit multipliers or comparator geometry".
- *Comparator geometry:* yes. The locus is a typed pole-comparator locus (SG-R2).
- *Conjugacy-intrinsic:* no. Pointwise type is chart-dependent (SG-R3); an explicit near-identity chart moving the locus can be added as a witness.

Sub-item 1 → CLOSED. R4 then reduces to the inventory (B3).
**Aside:** the P2-C0-FIRST itinerary (−1 → −i → +1 → +i → C₀) crosses the parabolic locus twice before rank loss.

### A4. CELL-F6 — conditional W1–W5 audit against OFN class C (R6 network successor)

**Object:** OFN v0.10 §5.5.4 class C, F^N_κ(z)_e = N(z_e) − (κ/3)Σ_j N(z_j), on a triangle, in the transported chart, with lock surfaces 𝒮₀ and 𝒮_±.
**Status:** a declared conditional model, *not* an RRF-registered identification. So the audit is "registry-conditional".

**Preliminary reading, to be verified.**
- **W1 (graph, coefficients, cochain): conditionally supplied.** A triangle; ℂ coefficients; a transported edge cochain; cycle sum Σz_e, so H¹ = ℂ.
- **W3 (same cohomology space): supplied.**
- **W2 (dyad → edge attachment preserving the token): not supplied.** OPEN-B is locked. Also, on 𝒮_± the edges are related by G = J², and transporting the B-section by G is a *different token rule* (F2(a)).
- **On the lock surfaces [a] ≡ 0 identically,** so Δ[a] ≡ 0 for any event there.
- **Off the surfaces,** the defect evolves by the smooth law (1−κ)ΣN with no event-gated channel. RECOG-ALG-CONTINUOUS-CARRIER-NOWRITE should therefore transfer, and C2 is absent.

**Expected endpoint `[RESULT]`:** class C, as contracted, does not instantiate the NG-7B "birth/history data" candidate. It supplies W1 and W3 but neither W2 nor an event-gated channel. This is a registry-relative result, with no dynamics asserted.
**Timing:** can be done now as a conditional audit, or after RRF decides on class-C registration (PI decision D3).

---

## 5. Phase 2 — compute cells (PI machine)

### B1. R9 C₂ sharpening

**Need.** The certified incompleteness window (q₀ < |G|/C₂) is much smaller than the memory-theorem domain:

| Row | Window | Theorem domain | Ratio |
|---|---|---|---|
| \|z\| ≤ 1/20 | q₀ < 1.48×10⁻⁵ | q₀ ≤ 1/400 | 169× smaller |
| \|z\| ≤ 1/40 | q₀ < 4.69×10⁻⁵ | q₀ ≤ 1/1600 | 13× smaller |

- RECOG's own `[NUM]` estimate shows C₂ conservative by about 170–550 (|M − q₀g|/q₀² ≈ 0.934).
- In Dyadic's new OPEN 21 theorem, the R9 term C₂(256/225)²Q₀² (669.3 / 211.0) dominates the single constant. N13 explicitly invites a sharper C₂.

**Targets.**
- C₂ ≤ |G|·1600 ≈ 12.2 makes incompleteness hold on the *entire* small row.
- C₂ ≤ |G|·400 ≈ 3.06 does so for the large row. This is likely reachable only via stage C.

**Stages.**
- **A — budget breakdown (sandbox, hours).** Decompose K_Φ (258.49 / 81.44) from `recog_cell_r9_memory_cert.py`. The C₇ term is only about 37–39% of K_Φ, so the elementary remainder inequalities may be the cheaper lever. Decide between the RECOG-side and the Dyadic-side route.
- **B — new row (Arb, PI machine).** Either tighten RECOG's remainder inequalities, or add a Dyadic NF-REM row with a sharper C₇ on a smaller disk (Dyadic is also Claude-owned). This gives an additional (C₂, q_max) row; existing rows stay in force, so the change is additive (G2 item 3). Notices go to Dyadic, OFN and RRF.
- **C — optional, large: second-order memory.** Compute M to O(q₀²) exactly with an O(q₀³) remainder. This needs the degree-7 jet of F̂ in the NF6 chart plus a C₈ remainder (a Dyadic deliverable). The payoff is incompleteness on (nearly) the whole row and a sharp Q₀² term for Dyadic P5. PI decision D4.

**Grade target:** `[THM]` (new row).

### B2. R3 — global geometry of W^s(P₂)

**Definition first.** T is not globally invertible (it folds at C₀), so W^s(P₂) = ∪T^{-n}W^s_loc is a branching set. Proposed working object:
- the *principal branches* W^s_±(P₂), continued by the local inverse branch at P₂ until their first encounter with the critical-value curve T(C₀);
- plus the basin question: is W^s(P₂) part of ∂𝓑(P₁)?

**R3-0 `[NUM]` scouting (mpmath; PI machine or sandbox).**
1. The fate of W^u₊(P₂) *after* its certified first C₀ hit: back to 𝓑(P₁), escape, or accumulation. This decides whether P₂'s stable set is a basin boundary.
2. Backward continuation of W^s_±(P₂), recording fold branchings.
3. A coarse 𝓑(P₁) membership grid.

**R3-1 `[THM]`.** One statement chosen from the scouting, for example "the first T(C₀) encounter of the backward principal branch W^s₊(P₂)" in B3 style. Reuse the B3 Lohner+tangent engine on the local inverse branch; Arb on the PI machine.
**Dependency:** Dyadic OPEN 12 status (G2 audit).

### B3. R4 sub-item 2 — periodic-orbit census of the primitive T

1. **`[NUM strong]` census.** Solve T^n x = x + (0, 2πL) for n ≤ 12, small |L|, in a box. Use Newton from grid seeds; deduplicate orbits; classify them in the (t_n, d_n)-plane.
2. **`[ALG via IA]`.** Krawczyk certificates for a selected subset, adapting `recog_cell_e3a3a_p9_saddle_cert.py` (rev. 1.2, safe-box serialization) from T_s to T.
3. **Closure criterion:** a certified inventory up to period N in a declared box, with `[NUM]` completeness evidence. A global inventory is not claimable.

**Value:** it populates §6.5's spectral stratum beyond P₁/P₂ and the known winding fixed points. This is the lowest scientific priority of the compute cells.

---

## 6. Routed and parked items (no RECOG action beyond keeping requests precise)

| Item | Blocking owner / reason | RECOG posture |
|---|---|---|
| R5-P1 composition (twisted cocycle along r_AC = r_AB r_BC) | RRF: multiplicative edges / H_× not registered; OPEN-B → E1 | Send one precise request in G3: what a multiplicative network realization must supply for P1 to be posable. |
| R5-P2 weight \|k\| = 1 | not derivable inside the dyad: all linear data at P₁ and P₂ are k-independent; k first appears at quadratic order | Optional `[HEUR]` for OFN/OPEN-P0: k = 1 is the identity character. g(r) = r − 1 is the displacement of the unit under the relation acting on itself. Recorded only as motivation. |
| R5 "saturation" reading | needs a nonlocal test design | Park. Retire at the next release unless a test is specified. |
| R1 adoption / P3 physical orientation | OFN OPEN-OFN-OPA; RRF OPEN-A | A2 supplies the sharpened dichotomy and the formal tangent-identity equivalence. |
| R6 route 1 (new event-gated single-dyad carrier) | would require RECOG to invent physics | Park. Act only if OFN/NUMGEN propose a carrier; audit it with F3(c). |
| R6 selection principle | genuinely open | A1 and A4 narrow it; no adoption (SG-R6). |
| R6 network successor | RRF OPEN-B/E1/E2; NG-7B | A4 (conditional); otherwise wait. |
| R7 genericity / full-measure entry for T_s | deliberately not an R7 claim; SG-R4 diagnostic | Park. |
| ER-2B C11–C12 lane | optional, ER-2B-initiated | Respond if invoked. |
| Dyadic OPEN 20 (B-an / B-6 / B-∞) | Dyadic | Its outcome upgrades A2(4) to analytic and decides class-C realization (A4). |

---

## 7. Decision points for the PI

| # | Decision | Recommendation |
|---|---|---|
| D1 | Record v0.3.20 as FROZEN at `fdb8c9a7…b8df` | Yes. Unblocks OFN REQ-O09-02, RER, Dyadic and RRF. |
| D2 | v0.3.21 scope | Sync only (G2 items 1–5); include the header compaction. |
| D3 | Order of the Phase 1 cells | A1 → A2 + A3 → A4. A4 now as conditional, or after RRF decides on class C. |
| D4 | Depth of R9 sharpening | Stage A now; stage B if A shows ≥10× gain is plausible; stage C only with a Dyadic degree-7 jet + C₈ deliverable. |
| D5 | PI-machine time for R3/R4 campaigns | R3-0 scouting yes, as one modest numpy/mpmath run; R4 census later. |
| D6 | Project housekeeping | See below. |

**Housekeeping note (D6).**
- Project knowledge is at **1,913,391 / 2,000,000 bytes (95.7%)**.
- The root still holds Dyadic v6.4.16, while v6.4.17 is adopted. Installing it at the root is pending the reviewer's release verification.
- Deletion candidates (PI's call): superseded `claude/` drafts — OFN v0.10 DRAFT1/DRAFT2, Dyadic v6.4.16/6.4.17 DRAFT r1, Genesis v2.8.9 DRAFT, P5 proof records v0.1/v0.1.1 and their scripts, and duplicated adopted copies once the root holds them.
- This plan is delivered as a file only; it is not written to the project.

---

## 8. Proposed release map

| Release | Content | New mathematics |
|---|---|---|
| v0.3.20 freeze record | G1 | none |
| v0.3.21 | G2 sync: receipts N10–N13, pins, §7.2 dependents, SG-R14 note, header compaction, §8 memo row | none |
| v0.3.22 | A1 CELL-F5 token read-out | yes (R6) |
| v0.3.23 | A2 involution ledger + A3 R4(1) closure | yes (R1/R4/R5 wording) |
| v0.3.24 | A4 CELL-F6 class-C audit | registry-relative result |
| v0.3.25+ | B1 new R9 row; later R3 / R4 cells | yes |

Each release follows the usual pattern: draft → contributor critique → freeze check → external hash record.

---

## Appendix A — candidate derivations (to be verified inside the cells)

### A.1 Slip-locking constant = raw-track retained memory

**Setup.**
- Lifted section angle: φ̂ = arg W.
- Per primitive step the linear rotation is +π/3, and the per-block phase lag is ΔΘ_W = −τQ_W + ….
- Define the block phase Θ_{W,M} := φ̂_{6M} − 2πM. Then D_M = 2πM − (φ̂_{6M} − φ̂₀) = Θ_{W,0} − Θ_{W,M}.

**Limit.**
- Ψ_W := Θ_W − τ log Q_W converges to Ψ_{W,∞}. This is Dyadic T1, conditional on R9.
- Raw-track Q_W obeys Q' = Q − Q² + O(Q^{5/2}). Hence 1/Q_{W,M} = M + O(√M), so τ log Q_{W,M} = −τ log M + o(1).
- Therefore Θ_{W,M} = Ψ_{W,∞} − τ log M + o(1), and
  D_M = τ log M + [Θ_{W,0} − Ψ_{W,∞}] + o(1).

**Identification.**
- C_D = Θ_{W,0} − Ψ_{W,∞} = Ψ_W(x₀) + τ log Q_{W,0} − Ψ_{W,∞} = τ log Q_{W,0} − M_W(x₀).
- Then T2 (M_W = M − Δ₀), R9 and P5 give the stated forms.

**Points to check in the cell:**
- block alignment of x₀;
- the orientation convention (SG-R9);
- that NG's φ̂ and Dyadic's lifted W-phase are the same lift (owner lift φ̂ = θ + 2πc_n);
- the domain intersection.

### A.2 Involutions

**(i) R₀ exists for every such germ.** Let DT(0) = A with A³ = −I and F = T⁶ tangent to identity. The formal log X = log F is unique, and T*X = X because TF = FT. So F^{−1/2} = exp(−X/2) commutes with T, and R₀ := T³F^{−1/2} satisfies:
- R₀² = T⁶F^{−1} = id;
- DR₀(0) = −I;
- R₀T = TR₀.

Uniqueness among −I-linear commuting involutions is Dyadic's theorem; it needs Re μ ≠ 0 and Im μ ≠ 0.

**(ii) R₀ = −I iff T is odd.** If T is odd, then (−T³)² = T⁶ and −T³ is tangent to identity. By uniqueness of the formal square root, F^{1/2} = −T³, and so R₀ = T³(−T³)^{-1} = −I. Conversely, R₀ = −I commuting with T means T is odd. For T_s: R₀^{(s)} = S_o.

**(iii) Degree 2.** From R₀T = TR₀, the quadratic part r₂ of R₀ satisfies r₂(Ax) − A r₂(x) = 2T₂(x), where T₂ = (0, ρ²/2) is the quadratic part of T_b. There is no degree-2 resonance at p = 6.

**(iv) Orientation equivalence.** With S := S_o, S T_k S = T_{−k} exactly (RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY). Put Φ_k := S R₀^{(k)}. Then:
- Φ_k T_k Φ_k^{-1} = S R₀ T_k R₀ S = S T_k S = T_{−k};
- DΦ_k(0) = (−I)(−I) = I.

Equivalently, the λ-equivariant formal normal forms of T_{±k} coincide, because N is odd.
