# NG-8A / NG-8B Certificate Cross-Check v1

**Date:** 2026-08-28
**Auditor:** Claude (RTG mathematical auditor / DSN editor)
**Objects compared:** (1) external certificates `NG_NG8A_ORBIT_CARDINAL_CERT_v1.md`, `NG_NG8B_REBLOCK_MULT_CERT_v1.md` (relayed 2026-08-28; written 2026-08-27 against NG v1.3); (2) independent in-corpus re-certification `NG_NG8AB_INDEPENDENT_RECERT_v1.md` + `ng8ab_independent_recert_v1.py` (exit 0); (3) DSN text `RTG_NUMBER_GENESIS_DSN_v1_4/v1_4_1` (§1.3, §2 NG-8A/NG-8B, §6.9).

**Verdict: CONSISTENT — zero material discrepancies.** The three lines certify the same two theorems from the same four N-1 inputs, with mutually compatible conventions and guards. NG-8A/NG-8B CLOSED status now rests on two independent certificate lines plus the executable word-algebra verification.

---

## 1. Claim-by-claim comparison

| Item | External certificate | Independent re-certification | DSN text | Match |
|---|---|---|---|---|
| N-1 inputs (invariance, non-collision, freeness, counting token) | §1, four inputs, pointwise non-collision over ℕ₀ | PREMISE-1, identical content | §1.1/N-1 CLOSED block | ✓ |
| NG-8A convention | post-event `S_m^+ = {T^k x : 1≤k≤m}`, `S_0^+=∅` | same, A1 | same + off-by-one `[GUARD]` | ✓ |
| NG-8A injectivity | from non-collision (§4) | word-level A2 | stated | ✓ |
| NG-8A surjectivity | by construction (§5) | A3 | stated | ✓ |
| `|S_m^+| = m`, incl. `m=0` | §6 | A1 (`m` up to 499 incl. spot values) | stated | ✓ |
| Position-set formulation | §7: `|S_m^pos| = m`, `m−1` internal transitions | A4/A5 (`S_m^pos = S_{m−1}^+ ∪ {id}` verified) | `[GUARD]` off-by-one | ✓ |
| NG-8B inherited freeness | §3: pointwise `B_m^r x = B_m^s x ⟹ r=s` | B2 (map-level) + B3 (length homomorphism) | stated | ✓ (see note L2) |
| Re-blocking identity `(T^m)^k = T^{mk}` | §4, incl. `k=0` | B1 exhaustive `m,k≤20` + spot `(137,89)`, `(2,250)`; B6 edges | stated | ✓ |
| "Same ordered history, different grouping" | §5: tokens/order/intermediate states/final state preserved | B4 flatten-of-`k` blocks = primitive word; grouping metadata differs | stated | ✓ |
| No second event type / N-5A firewall | §9 guards 3–4 | B5, C1 single-alphabet checks incl. mixed `(T^m,T^n)` | `[GUARD]` ×2 + SG-NG-20 | ✓ |
| Scope: local tube, OPEN-P0 ceiling | §9 guards 1–2 | scope line in premises | `[scope: U_T]` + SG-PROG-2 import | ✓ |
| No Track-B/network, no Track-C identification, no completed infinity | NG-8A §9 guards 3–6, NG-8B §9 guard 5 | out of scope by construction, noted | final `[GUARD]` in NG-8A/B block | ✓ |

## 2. Counting-convention table (for future reference; all three are consistent, they count different things)

| Convention | Set | Cardinality | Transitions represented |
|---|---|---|---|
| Post-event (NG-8A's) | `{Tx, …, T^m x}` | `m` | `m` (one per event) |
| Position-set | `{x, Tx, …, T^{m−1} x}` | `m` | `m−1` internal |
| Full trajectory incl. initial, `m` events | `{x, Tx, …, T^m x}` | `m+1` | `m` |

## 3. Ledger notes (differences worth recording; none material)

**L1 — implicit vs declared counting predicate.** The external NG-8A certificate asserts the `m` post-event states are "pairwise physically distinguishable by the present reduced relational state itself" (§4) but does not declare this as a premise. The v1.4.1 `[DEF]` state-counting predicate (SG-NG-11 discharge) makes it explicit; the re-certification records it as PREMISE-2. Compatible; the `[DEF]` stays.

**L2 — pointwise-stronger freeness proof.** The external NG-8B certificate proves block-orbit non-collision pointwise (`B_m^r x = B_m^s x` at a single `x` forces `r=s`), which is strictly stronger than, and implies, the map-level freeness stated in the DSN. Recorded as a strengthening, not a discrepancy.

**L3 — two guards richer in the certificate than in the DSN.** (i) Positive block-size guard (`m=0` excluded as generator since `⟨id⟩` is not a free monogenic event stream; `k=0` valid) — already implicit in the DSN's "for every positive block size m"; no edit needed. (ii) No-commutativity-from-grouping guard (§9.7) — imported into v1.4.1 with the deflationary clarification that within Track A `(T^m)^k` and `(T^k)^m` flatten to the same primitive history, inheriting metalanguage integer commutativity; only cross-track commutativity is future NG-8 work.

**L4 — provenance chain.** Certificates target v1.3 (2026-08-27); imported by v1.4; relayed and cross-checked at v1.4.1 candidacy (2026-08-28). Registry rows updated accordingly. D8's NG-8 half is discharged; the DZT v0.17 owner file remains the outstanding relay item.
