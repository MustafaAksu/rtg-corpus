# v1.20.6 Grade Normalization — Review Group 2 (N-3 internal, C1–C7A, NG-7A)

**Memo ID:** `NG_V1206_REVIEW_G2_v1` · **Date:** 2026-09-29 · **Base:** frozen v1.20.5 (`351384dc…d3f34c`)
**Criterion:** K1–K6 **as amended by the co-owner** (recorded in `NG_V1206_RULING_LEDGER.json`). Group 1 CLOSED at ruling level.
**Status:** REVIEW — proposals only. Nothing applied.

Rows: **2, 3, 7, 8, 12, 13, 14, 15, 16, 19** (line numbers in v1.20.5).

---

## 0. What the owner bodies actually carry

Before grading, the bodies these rows restate or depend on were read. **Every one is single-grade `[ALG]`:** N5-C1 (L1620), C2 (L1655), C3 (L1669), C4 (L1681), C6 (L1743, L1768), N5-PHYS-1's four results (L1786 gauge audit, L1788 strict alternation, L1797 prefix-cofinal repeatability, L1804 physical bounded class; its predicates are a `[DEF]` at L1780), and N-3C (module status L1377, core non-translation result L1388). The combined `MATH/ALG` / `ALG/MATH` tags in this group are, in every case examined, shorthand over `[ALG]` evidence plus standard mathematics used in the proof — which K3 moves to `Depends on:` / provenance, not into the grade.

## 1. Owner rows

### Row 8 — L1405 · N-3C consequence — **`[RESULT] [from: ALG]`**
*"Primitive `T` therefore mixes phase-character sectors with ρ-dependent amplitudes rather than translating the harmonic index by a fixed history unit."*
Type: a consequence ("therefore") drawn from the exact non-translation result at L1388 `[RESULT][from: ALG]`. Evidence: exact computation; character theory is proof input (K3). Scope: the module's open dyadic domain, unchanged. `[RESULT]` is legitimate here — a genuine local consequence (K4). Matches the module status L1377.

### Row 14 — L1705 · C5-SYN-13 — **SPLIT: `[DEF]` + `[RESULT] [from: ALG]`**
Defines `W_(13:2) := A^6 B A^7 B` **and the admissible prefix set** `P_(13:2)` (finite prefixes of `W^m`), then proves `Δ_(13:2)(W)=0`, complete-period cancellation for every `H = W^m R`, the one-period defect sequence, `|Δ_(13:2)(H)| ≤ 13` for every admissible prefix, and — with C3/C4 — that `13:2` is the unique reduced class.
- The control language and its admissibility set are a **substantive definition** (amended K1): the bound is a statement *about that admissible set*.
- The bound holds for **all** `m` by the cancellation argument, so it is not merely a finite check; `[ALG]` at full scope.
- **Proposal:** **14a** `[DEF]` synthetic control language `W_(13:2)` and admissible prefix set `P_(13:2)`; **14b** `[RESULT] [from: ALG]` bounded synthetic `13:2` class with `|Δ| ≤ 13`, `Depends on: 14a, C3, C4`.

### Row 15 — L1729 · nearby negative control — **SINGLE `[RESULT] [from: ALG]`**
`W_fail := A^6 B A^8 B` has 14 A- and 2 B-events per period, so `Δ_(13:2)(W_fail^m) = 2m → ∞`.
- `W_fail` is a **name for one explicit word**, i.e. notation, not a substantive definition (amended K1) — the contrast with row 14 is deliberate: row 14 defines an admissible prefix *set* that the theorem quantifies over; row 15 names a single word.
- **Proposal:** single `[RESULT] [from: ALG]`. The closing sentence ("discriminating rather than automatic") is the conclusion of the same claim, not a separate guard.

### Row 16 — L1836 · C7A body — **SPLIT: two `[RESULT] [from: ALG]` + `[GUARD]`**
The block holds three different things:
- **16a** — *"C2 … C3 … C4 … Therefore `ρ_Q` is a well-defined unique positive-rational invariant of every certified bounded physical pair."* A genuine local synthesis of C2, C3, C4, all `[ALG]`. → `[RESULT] [from: ALG]`, `Depends on: C2, C3, C4`.
- **16b** — *"From N5-PHYS-1, `ρ_Q(B_+, B_-) = 1`, `1 ∈ Q_RTG^bd`."* Different evidential basis: a specific certified witness, not the general theorem (K2). → `[RESULT] [from: ALG]`, `Depends on: 16a, N5-PHYS-1`.
- **16c** — *"This witness is bounded and is a positive control; it is not itself a dynamic realization. `1 ∈ Q_RTG^dyn` is established separately by C7B-DISC-2 …"* A usage boundary. → separate `[GUARD]` block (precedent: row 5).
- **Ruling needed on 16a:** `[RESULT] [from: ALG]` vs `[THM]`. Well-definedness of `ρ_Q` is a proposition with a complete proof (K6 would allow `[THM]`). I propose `[RESULT] [from: ALG]` because it is a synthesis *whose entire basis is C2–C4 at `[ALG]`*; grading the synthesis above its basis would be inconsistent within the module.

### Row 19 — L2376 · NG-7A `Z_N` zero-control — **SINGLE `[ALG]` core; finite checks to provenance**
*"Integer cycle vectors annihilate node-difference `Z_N` phase data mod N (rings N = 6, 8, 12; random graphs)."* followed by a `[COR v1.19]` detection note.
- The claim is the integer identity `C·Dᵀ = 0` reduced mod `N`: exact and general in `N` → `[ALG]`.
- The parenthesis records finite exact checks (three ring sizes, sampled random graphs). They add no scope beyond the general identity, so under K2 they are an **evidential record**, not a second graded claim.
- **Proposal:** `[RESULT] [from: ALG]` for the general identity; move "(rings N = 6, 8, 12; random graphs)" into a provenance phrase ("finite exact checks: …"). The `[COR v1.19]` note is unchanged.
- *Alternative for ruling:* keep the checks as a separate `[ALG] [scope: rings N=6,8,12; sampled random graphs]` claim. I do not recommend it: Methodology L556 allows it, but it would duplicate a claim the general identity already covers.

## 2. Mirrors (K5)

| row | location | synchronizes to | note |
|---|---|---|---|
| **7** | L1364 N-3B conclusion | **row 6** (`[THM]`) | same proposition as the N-3B owner row: the unique homomorphism `g ↦ χ_1`, surjective, trivial kernel |
| **12** | L1553 §6.6 C5 summary | **rows 14b, 15** | last sentence "without constituting a physical RTG witness" → separate `[GUARD]` (row 5 precedent) |
| **13** | L1563 §6.6 C7A summary | **rows 16a, 16b** | "Bounded realization and dynamic admission are distinct" → separate `[GUARD]` |
| **3** | L330 §5 high-risk table | **rows 16a, 16b** | table row; the "must not claim" column already carries the guard, so no split |
| **2** | L143 §1.3 N-5 spine summary | **DEFERRED** | bundles C1–C4, C5, C6, N5-PHYS-1, C7A (all `[ALG]`) **and** the DISC-1/DISC-2 label sets. If group 3 grades DISC as `[ALG]`, row 2 can be a single `[RESULT] [from: ALG]` summary mirror; otherwise K2 requires the DISC sentence to be split out. Decide after group 3. |

## 3. Running count (for the eventual `[COR v1.20.6]`, not yet final)

Group 1: 4 owner decisions (1, 6, 10, 11) + 3 syncs (4, 5, 9).
Group 2: 5 owner decisions (8, 14, 15, 16, 19) + 4 syncs (7, 12, 13, 3) + 1 deferred (2).
Group 3 remains. Per the ruling, no corpus-wide number is written until the last ruling.

## 4. Decisions requested

1. Owner rows **8, 14 (split), 15, 16 (split + guard), 19**.
2. **16a:** `[RESULT] [from: ALG]` (proposed) vs `[THM]`.
3. **19:** finite checks as provenance (proposed) vs a separate finite-scope `[ALG]` claim.
4. Mirror treatment of **7, 12, 13, 3**, including the two `[GUARD]` separations (12, 13).
5. **Row 2 deferred** until the DISC rulings.
