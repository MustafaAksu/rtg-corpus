# v1.20.6 Grade Normalization — Review Group 1 (imported / standard-mathematics rows)

**Memo ID:** `NG_V1206_REVIEW_G1_v1` · **Date:** 2026-09-29 · **Base:** frozen v1.20.5 (`351384dc…d3f34c`)
**Status:** REVIEW — proposals only. Nothing applied. Each row needs a ruling.
**Working rule (PI, 2026-09-29):** the draft table is a review queue only; every row is decided on its full claim block along four axes — claim type, evidence, scope/assumptions, single grade vs split. §9.2 mirrors are synchronized after the owner row is ruled. DISC-1/DISC-2 last, by separate ruling.

**Group 1** = rows where imported or standard mathematics dominates: **1, 4, 5, 6, 9, 10, 11** (line numbers in v1.20.5). Group 2 = N-3 internal computations (7, 8), C1–C7A (2, 3, 12–16), NG-7A (19). Group 3 = DISC-1/DISC-2 (17, 18).

---

## 1. Proposed split criterion (to be fixed by ruling on this group)

Grounded in Methodology v1.3: `[DEF]` L553, `[THM]` L554, `[ALG]` L556, the `[MATH]` alias L600 = `[THM] [scope: standard mathematical input]`, imports §3.3, splitting L318.

- **K1 — Decompose.** Break the block into truth claims. Definitions, notation, usage guards and pointers to other claims are not truth claims.
- **K2 — Split only on differing evidence kind.** A block is split iff it contains two or more truth claims whose evidence differs in kind (definition, proof, exact computation, import, numerics). A guard, definition or pointer sitting beside a single truth claim is re-typed (`[DEF]`, `[GUARD]`, or plain text), not graded.
- **K3 — Standard mathematics is a scope qualifier, not a second grade.** Standard mathematics used to prove an RTG claim is disclosed as `[scope: standard mathematical input]`. RTG premises proved elsewhere in this ledger enter as dependencies (`Depends on:` / `[assuming:]`), not as grade components.
- **K4 — Imports keep the source grade.** An imported claim carries its source's own grade through `[import: SOURCE_vX.Y §… | RID]` and is never combined with a local grade.
- **K5 — Summaries are mirrors.** A §6 summary line (the pre-migration §6 layer) or a §1/§5 summary that restates a body claim is decided once, at the body, then synchronized — like the §9.2 mirrors.
- **K6 — `[THM]` vs `[ALG]`.** `[THM]` for a complete proof of a proposition, including a standard theorem instantiated on an RTG object. `[ALG]` for an exact symbolic identity or derivation with domain, coefficient field and conventions stated.

## 2. Rows

### Row 1 — L68 `[from: DEF/THM]` · §1.1 imported foundation — **SPLIT**
*"Finite phase support. The discrete branch is defined on `Z_N` (N even), physical states are quotiented by global phase shift, relational phase differences are primary, and capped deterministic dynamics are eventually periodic."*
- **Type:** three definitional clauses + one theorem.
- **Evidence:** import. Source checked: Discrete Genesis v2.12.13 §6.1 gives the first three as `[DEF]` (L521, L523: *only Δ_ij are physical*); §6.2 gives *finite-state recurrence* as `[THM]` under a fixed node-count cap (L547). No RIDs.
- **Scope:** "capped" matches the source's node-count cap — preserved.
- **Proposal:** split into **1a** `[DEF] [import: RTG_DISCRETE_GENESIS_DSN_v2.12.13 §6.1 | RID unavailable]` (Z_N with N even; global-phase quotient; relational differences physical) and **1b** `[RESULT] [from: THM] [import: RTG_DISCRETE_GENESIS_DSN_v2.12.13 §6.2 | RID unavailable]` (capped deterministic dynamics eventually periodic). Legacy `[source:]` → `[import:]` in the touched block.

### Row 6 — L1349 `[from: MATH/ALG]` · N-3B body — **SINGLE `[THM]`**  *(owner row for row 4)*
Status + construction: `ρ_char(g^k) = χ_k` from the N-2 generator into `Ŝ¹ = {χ_k}`.
- **Type:** one proposition — the infinite cyclic `G_T` is isomorphic to `Ŝ¹` by generator-to-generator map.
- **Evidence:** standard (`Ŝ¹ ≅ Z`; infinite cyclic groups are isomorphic via generators) applied to the RTG premise *`G_T` infinite cyclic*, which is N-2's result.
- **Scope:** "abstract representation of the local Track-A group" — keep.
- **Proposal:** `[RESULT] [from: THM] [scope: standard mathematical input; abstract representation of the local Track-A group]`, `Depends on: N-2`. The "ALG" half is a dependency, not a second grade (K3).

### Row 4 — L1295 `[from: MATH/ALG]` · §6.4 summary of N-3B — **MIRROR of row 6**
Restates row 6. Synchronize to row 6's ruling (K5).

### Row 10 — L1429 `[from: MATH/ALG]` · N-3D restriction/kernel — **SINGLE `[THM]`**  *(owner row for rows 5, 9)*
*Restriction `Ŝ¹ → Ĉ_N` is surjective with kernel `{χ_{qN}}`; composed with N-3B, `ker ρ_N = N G_T`, `G_T/(N G_T) ≅ Ĉ_N ≅ Z_N`.* Last sentence fixes `N` for the TDR-G bridge.
- **Type:** one proposition; the final sentence is an application note (`N` = the discrete branch's phase size), not a claim.
- **Evidence:** standard character restriction + dependency on N-3B.
- **Proposal:** `[RESULT] [from: THM] [scope: standard mathematical input]`, `Depends on: N-3B`.

### Row 9 — L1414 `[from: MATH/ALG]` · N-3D module status — **SINGLE `[THM]`, synced to row 10**
*"CLOSED as pure representation theory …; discrete dynamical realization remains OPEN"*, followed by the definitions of `C_N` and `res_N`.
- **Type:** module status; the `C_N`, `res_N` lines are set-up definitions of the row-10 statement.
- **Proposal:** status grade follows row 10: `[RESULT] [from: THM] [scope: standard mathematical input; pure representation theory]`; the OPEN residual stays as written. Set-up definitions stay untagged inside the statement (K1). The status line itself is INV-S-tracked, so its living-state keywords and scope must be preserved exactly.

### Row 5 — L1305 `[from: MATH/ALG]` · §6.4 summary of N-3D — **MIRROR + GUARD re-type**
*"restriction to `C_N` yields `G_T/(N G_T) ≅ Ĉ_N ≅ Z_N`. For TDR-G this is admissible only as a representation bridge; all dynamical transfer remains forbidden."*
- **Proposal:** the mathematical sentence mirrors row 10 (K5). The second sentence is a usage restriction, not a truth claim: re-type it as `[GUARD]` in the same block (K2). This is the one place in group 1 where a sentence changes type.

### Row 11 — L1450 `[from: ALG/MATH]` · N-3C+ — **SPLIT (status line), core `[ALG]`**
Status line bundles: (a) the representation-kinematic projector result; (b) the `q=4,(0,3)` cascade item "CLOSED-by-import from the Dyadic owner"; (c) an OPEN pointer for missing-slot work. Body: `C_R M_ab = λ^{a−b−1} M_ab`, projectors `Π_r`, `Π_r M_ab = δ_{χ_p(a,b),r} M_ab`, with `ord(λ) = p`.
- **Type:** (a) one exact identity; (b) an import; (c) a pointer.
- **Evidence:** (a) exact symbolic computation, general in `p`, using orthogonality of roots of unity; (b) Dyadic v6.4.10 `DYAD-THM-Q403-PHASELAW` `[THM]`, already imported by its own separate `[import:]` line elsewhere in the ledger.
- **Proposal:** status grade → `[RESULT] [from: ALG] [assuming: ord(λ)=p] [scope: standard mathematical input; formal vector-map monomials over C]`. Clause (b) becomes a plain pointer to the existing import line — it must not be graded here as well (K4). Clause (c) stays as plain text.
- **Open question for ruling:** `[ALG]` vs `[THM]`. The identity is proved for all `p` by a complete argument, which also satisfies `[THM]`. I propose `[ALG]` because the claim is an exact symbolic identity with stated conventions, and the existing primary grade was ALG.

## 3. A finding that affects the count

Under K5, rows 4 and 5 are **mirrors** of rows 6 and 10. So "19 independent grade-decision rows" — written into the header at v1.20.4 — overcounts. In group 1, seven rows reduce to **four owner decisions** (rows 1, 6, 10, 11) plus three synchronizations (4, 5, 9). Group 2 is likely similar (rows 12↔14/15, 13↔16, and the §1/§5 summaries 2, 3). The corrected count belongs in v1.20.6 once rulings are in; v1.20.5 stays as frozen.

## 4. Decisions requested

1. Adopt **K1–K6** as the split criterion for v1.20.6.
2. Rulings for **row 1** (split), **row 6** (`[THM]`), **row 10** (`[THM]`), **row 11** (`[ALG]` vs `[THM]`).
3. Confirm the **mirror treatment** of rows 4, 5, 9, and the `[GUARD]` re-type inside row 5.
4. Confirm that the "19 independent" count is to be corrected in v1.20.6.
