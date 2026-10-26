# NG-8A / NG-8B Independent Re-Certification v1

**Date:** 2026-08-28
**Auditor:** Claude (RTG mathematical auditor / DSN editor)
**Applies to:** RTG Number Genesis DSN v1.4 (§1.3, §2 NG-8A/NG-8B, §6.9)
**Companion artifacts:** `ng8ab_independent_recert_v1.py`, `ng8ab_independent_recert_v1.log` (all assertions pass, exit 0)

---

## 1. Purpose

NG v1.4 closes NG-8A and NG-8B citing `NG_NG8A_ORBIT_CARDINAL_CERT_v1.md` and `NG_NG8B_REBLOCK_MULT_CERT_v1.md`. Those files were produced in the external reviewer's sandbox and are **not present in the project corpus**. Under the exit-code-gated-certificate rule, a CLOSED status must rest on certificates in our possession. This document, together with its executable companion, supplies an independent in-corpus certification so that the CLOSED status of both results is supported regardless of whether the external files are later relayed.

## 2. Imported premises (stated, not re-proved)

**PREMISE-1 — free monogenic tube.** `[source: NG_N1_UNIFIED_T_ALIGNMENT_CERT_v1.md; NG changelog v0.8/v0.9]` On the certified local primitive-dyad tube `U_T`: (i) `U_T` is forward invariant under `T` (hence under every `T^m`); (ii) the primitive orbit has no finite collision — `T^r x = T^s x ⟹ r = s` for all integers `r,s ≥ 0` and admissible `x`. Consequently the history monoid is free monogenic and is faithfully modelled by words in one primitive token with concatenation as composition.

**PREMISE-2 — physical distinguishability of tube states.** Distinct states on `U_T` are distinct points of the gauge-reduced chart and therefore differ in certified relational observables (`Q_true` and/or relational phase). Set-distinctness of tube states equals physical distinguishability at this scope. This premise anchors the word "physically" in NG-8A against SG-NG-11 (strict vs counting equivalence) and is recorded in v1.4.1 as the explicit NG-8A state-counting predicate.

## 3. NG-8A — ordinal-to-cardinal orbit-state compatibility

**Statement (post-event convention).** For admissible `x ∈ U_T` and finite `m ≥ 0`, with `S_m^+(x) = {T^k x : 1 ≤ k ≤ m}` and `S_0^+(x) = ∅`: the `m` primitive event occurrences are physically equinumerous with the `m` newly visited post-event states; in mathematical representation `|S_m^+(x)| = m`.

**Proof audited.** The orbit-evaluation map `k ↦ T^k x` on `{1,…,m}` is injective by PREMISE-1 and surjective onto `S_m^+(x)` by construction; a bijection between an `m`-element index set and the visited-state collection is exactly equinumerosity, and PREMISE-2 upgrades set-distinctness of the states to physical distinguishability. The `m = 0` edge is the empty collection. **Valid.**

**Convention guard verified.** The position-set `{x, Tx, …, T^{m−1}x}` has `m` positions but only `m−1` internal transitions; it equals `S_{m−1}^+(x) ∪ {x}`. The executable certificate verifies both the post-event count and the exact relation between the two conventions, so the off-by-one guard in the DSN is correct and non-vacuous.

## 4. NG-8B — multiplication by physical re-blocking

**Statement.** For every block size `m ≥ 1`, `B_m = T^m` generates a free submonoid `⟨T^m⟩`, and for every `k ≥ 0`, `(T^m)^k = T^{mk}` as identity of the same ordered primitive history under two groupings; re-blocking introduces no second independent event type.

**Proof audited.** Freeness: `(B_m)^j = (B_m)^k` gives words of lengths `mj` and `mk`; ambient freeness (PREMISE-1) forces `mj = mk`, and integer cancellation with `m ≥ 1` gives `j = k`. Grouping identity: concatenating `k` copies of the `m`-block flattens to exactly the `mk`-token primitive word — literal word equality, not merely endpoint equality — while the grouping metadata (`k` parts vs `mk` tokens) differs whenever `m ≥ 2, k ≥ 1`. Alphabet check: every `⟨B_m⟩` word, and every mixed `(T^m, T^n)` composite, uses only the single primitive token, so no second generator appears (SG-NG-20 alignment). Edges `(T^m)^0 = id` and `m = 1` verified. **Valid.**

## 5. Executable verification summary

15 assertion families, all PASS, exit 0: word-model sanity (S0.1–S0.3); NG-8A counts, injectivity/surjectivity, convention relation (A1–A5); NG-8B grouping identity exhaustively for `m,k ≤ 20` plus large spot checks including `(137,89)`, `(2,250)`, freeness for `m ≤ 12, j,k ≤ 30`, length-homomorphism cancellation, flatten/grouping distinction, single-alphabet checks, edge cases (B1–B6); SG-NG-20 mixed-blocking alphabet check (C1).

## 6. Verdict

**NG-8A: RE-CERTIFIED.** **NG-8B: RE-CERTIFIED.** Both at `[RESULT][from: ALG]`, scope `local primitive-dyad tube U_T`, conditional on PREMISE-1 (already certified in-corpus) with PREMISE-2 recorded as the declared counting predicate. The v1.4 CLOSED statuses are sound; with this document in the registry they no longer depend on artifacts outside the corpus. The two external certificate files should still be relayed when convenient and cross-checked against this one; any discrepancy would be ledgered, not silently merged.
