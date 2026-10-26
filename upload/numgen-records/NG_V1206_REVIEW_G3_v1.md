# v1.20.6 Grade Normalization — Review Group 3 (DISC-1, DISC-2) and Row 2

**Memo ID:** `NG_V1206_REVIEW_G3_v1` · **Date:** 2026-09-29 · **Base:** frozen v1.20.5 (`351384dc…d3f34c`)
**Criterion:** amended K1–K6 (`NG_V1206_RULING_LEDGER.json`). Groups 1 and 2 CLOSED at ruling level.
**Status:** REVIEW — proposals only. Nothing applied.

---

## 1. What kind of evidence DISC is — Methodology v1.3

- **L716** lists as a forbidden move *"promoting … a finite sweep to exact general proof"* and prescribes: *"Separate numerical evidence, finite exact verification, and all-parameter derivation."*
- **L840** (v1.3 change record): *"distinguish exact computation from high precision."*
- **L556** `[ALG]`: exact derivation or value with domain and conventions specified; *"finite exact checks support only their declared finite scope unless accompanied by a general argument."*
- **L561–562** `[NUM]` / `[NUM strong]`: *numerical* results with protocol and scope.

DISC is deterministic, exact-integer dynamics on a finite state space, evaluated **exhaustively** over a registered finite panel, with exact cycle detection. Nothing is approximated. Under L716 this is **finite exact verification** — the `[ALG]` category with finite scope — and **not** `[NUM]`. Grading it `[NUM strong]` would misclassify exact computation as numerics; grading it `[THM]` would claim an all-parameter argument that does not exist.

L756 requires a computational certification to carry enough to reconstruct the computation and its relation to the claim. DISC has it: pinned owner transition (`genesis_mode_b_mc_v18.py`, `9d787b43…`), the one-step triple-equivalence gateway over all `24^4` reduced states at every `k`, the owner recount (DISC-1: 0 mismatches; DISC-2 A1: 544/544), exact integer `C7B-ALG-T4` certificates (A2: 136/136), domain audit (A3: 136/136), frozen preregistrations by hash.

## 2. New evidence: DISC-1 P2 exposure — the queued audit, now closed

The P2 antipodal-endpoint audit had covered only the 136 DISC-2 witnesses. Run now on DISC-1, with the witness list taken from the **sealed harness** (`57a15421…`, 22 PASS_INT, classes `2:1 ×12`, `3:1 ×10`) and replay agreeing with the enumeration on all 22:

| label | unexposed witnesses | exposed witnesses |
|---|---|---|
| 2:1 | 12 | 0 |
| 3:1 | 10 | 0 |

**0 / 22 DISC-1 witnesses touch the antipodal condition.** Under the reverse and inert alternative policies the witness-level label set is unchanged, `{2:1, 3:1}`. DISC-1 is therefore P2-independent outright; DISC-2 is P2-robust at label level (40/136 exposed, every label with ≥ 1 unexposed witness, label set invariant under both alternatives). Both statements are about the **two tested alternative policies**, not about arbitrary future Discrete-owner policies.

## 3. A structural finding outside the 19-row inventory

The definitions that the DISC membership claims rest on —

```text
Q_RTG^bd  := { p/q : exists a certified physical pair (A,B) with Delta_(p:q)(H) = O(1) }
Q_RTG^dyn := { r in Q_RTG^bd : exists at least one certified realization of r passing the
               frozen same-realization stability+contingency discrimination gate }
rho_Q(A,B) := p/q
```

— sit **inside a `[COR] [scope: v1.15 spectrum notation]` block** (L1816–L1833), a correction note, not a `[DEF]` block. Under amended K1 these are substantive, load-bearing definitions and must be `[DEF]` claim-blocks. The DISC rows below cannot cite `Depends on: Q^dyn DEF` unless that `[DEF]` exists.

**Proposal (K1-derived addition, not one of the 19):** extract the three definitions into a `[DEF]` block in N5-C7A; the `[COR]` note remains as the historical record of the v1.15 → v1.16 notation change. The frozen gate itself is specified by the preregistrations and is referenced from the `[DEF]` by hash.

## 4. Proposal for rows 17 (DISC-1) and 18 (DISC-2) — **SPLIT into three**

Each current block bundles three assertions with different domains and evidential bases (K2):

**(a) Finite exact verification** —
`[ALG] [scope: finite exact verification over the registered panel; frozen protocol; K = {0,1,2,3}] [conv: TDR-G owner transition genesis_mode_b_mc_v18.py @ 9d787b43…]`
The census and discrimination verdicts and the witness list: DISC-1 — 3456 seeds, 3253 dual-active, 64 through the stability fence, 22 PASS-INT, 0 boundary-only; DISC-2 — 10368 registered supplementary seeds, 7468 dual-active, 208 through the fence, 130 PASS_INT + 6 PASS_BDY_ONLY. Provenance: gateway, owner recount, T4 certificates, domain audit, P2 exposure (§2).

**(b) Bounded breadth** —
`[RESULT] [from: ALG]` *non-`1` bounded classes are realized* (DISC-1: the original non-`1` falsifier does not fire; DISC-2: B-check PASS). `Depends on: (a), Q^bd [DEF], C7B-ALG-T2, C7B-ALG-T3`. Basis: the base-`k` census only.

**(c) Dynamic membership** —
`[RESULT] [from: ALG]` DISC-1: `{2,3} ⊆ Q_RTG^dyn`, `Q_RTG^dyn ≠ ∅`; DISC-2: `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} ⊆ Q_RTG^dyn`. `Depends on: (a), Q^dyn [DEF], C7B-ALG-T4`. Basis: the discrimination verdicts.

**Why (c) carries no finite-scope penalty.** `r ∈ Q^dyn` is existential by definition; one exactly verified witness discharges it completely. L556's finite-scope limit bites on *universal* conclusions, and none is drawn: the existing guard (L1921) already states that the ten labels are a lower bound, not `Q^dyn` itself.

**Why (b) and (c) are separate.** Different target sets (`Q^bd` vs `Q^dyn`) and different evidential bases (base census vs same-realization discrimination) — K2. If you judge this split too fine, (b) and (c) could remain one `[RESULT] [from: ALG]` with both consequences; (a) must be separate in either case.

## 5. Row 2 — resolved as a mirror

With (b) and (c) at `[RESULT] [from: ALG]`, every component of the §1.3 spine summary (C1–C4, C5, C6, N5-PHYS-1, C7A, DISC-1, DISC-2) is `[ALG]`-based. **Row 2 → single `[RESULT] [from: ALG]` summary mirror**, synchronized; its closing "remain OPEN" sentence is status text.

## 6. Count (tentative, for the `[COR v1.20.6]`)

**11 owner decisions** (group 1: 1, 6, 10, 11; group 2: 8, 14, 15, 16, 19; group 3: 17, 18) + **8 mirrors** (4, 5, 9, 7, 12, 13, 3, 2) = the 19-row raw inventory; plus the **4 §9.2 provenance mirrors**; plus **1 K1-derived addition** (§3). Final only after this ruling.

## 7. Decisions requested

1. DISC evidence class: **finite exact verification → `[ALG]` with finite scope** (not `[NUM strong]`, not `[THM]`).
2. The **three-way split** (a)/(b)/(c) for rows 17 and 18 — or the two-way alternative (a) + merged (b,c).
3. The **`[conv:]` qualifier** pinning the owner transition, with the P2 robustness record as provenance.
4. The **K1-derived addition**: extract `Q^bd`, `Q^dyn`, `ρ_Q` into a `[DEF]` block.
5. **Row 2** as a single `[RESULT] [from: ALG]` mirror.
