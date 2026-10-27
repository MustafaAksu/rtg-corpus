# Number Genesis → Dyadic — Interface confirmation I1–I5 for the L-PHASE row-A certificate

**Date:** 20 October 2026 · **From:** Number Genesis owner side (Claude, DSN editor/auditor; the PI keeps the final decision) · **To:** Dyadic DSN owner
**Status:** `[SESSION]` interface confirmation. Prepared for PI dispatch. No owner file is modified. Nothing is adopted.
**In reply to:** `DYAD_REPLY_TO_NUMGEN_LPHASE_ROWA_v0_1.md` §2. Received via the PI; the received copy has SHA-256 `45cdd7043ee69f0b0dccf23ce47d3c165216d6c8eb381680f8dff581d27851cf` and its content is the same as the project copy that was read. Record: `DYAD_NUMGEN_LPHASE_ROWA_CERTIFICATE_SESSION_v0_1.md` (`775c6715…f233d`). External review: `L-PHASE ROW A SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION PENDING`.
**NUMGEN basis:** v1.20.7, `c4637e7a…ab28`.

---

## 1. Confirmations

All five readings are **CONFIRMED**. The notes beside them mark where v1.20.7 is implicit rather than wrong.

| # | DYAD reading | NUMGEN v1.20.7 source | Verdict |
|---|---|---|---|
| I1 | Lift φ̂ = sum of principal one-step angles δ_T(y) = Arg(W(Ty)/W(y)); φ̂_{6m} at T^{6m}x | L-MONO (L2152–L2164): "the primitive angular lift is strictly increasing", with δ_T = π/3 + O(Q^{1/2}) and corollary π/6 < δ_T < π/2. Step-indexed φ̂_n is used in G_n (L2265) and D_M (L2186). | **CONFIRMED.** v1.20.7 never writes φ̂ explicitly as a sum of principal angles; it is implicit through L-MONO. Your P-c gives \|δ_T − π/3\| ≤ arcsin(0.04654) on U_T, so on the explicit tube the principal-sum lift *is* the L-MONO lift. NUMGEN will add an explicit `[DEF]` of φ̂ in v1.20.8 (interface hygiene, no scientific change). |
| I2 | W = u + iv, u = ρ − η/2, v = (√3/2)η | Θ = atan2(√3 η_wrap, 2ρ − η_wrap) (L2104) is exactly arg(ρ + ωη_wrap). Q_true = \|W\|² (L898). | **CONFIRMED.** On U_T, \|η\| ≤ (2/√3)·0.047 < π, so η_wrap = η and the wrapped and lifted frames coincide. |
| I3 | Q_m = \|W(T^{6m}x)\|² primitive; v1.20.7 "q_m" read as this, not as the chart q = \|z\|² | L-BACKBONE derives q_m from L1, `q_{m+1} = q_m − q_m² + O(q_m^{5/2})`, which is the primitive Q_true law | **CONFIRMED.** v1.20.8 will retype the symbol as block-sampled primitive Q_true, per OFN REQ-O09-03 and the co-owner GO. |
| I4 | Increasing lift; block law 2π − τQ_m + r_m; defect read as a lag | Sign convention pinned in v1.11.x (changelog L3074); D_M = 2πM − (φ̂_{6M} − φ̂_0) | **CONFIRMED** |
| I5 | Block base points in U = {0 < Q ≤ 1/625}; intermediate steps in U_T | v1.20 explicit-domain block (L2124) imports exactly U and U_T from DYAD-THM-PRIM-CTR, and the canonical seed lies in U | **CONFIRMED.** U is the explicit tube NUMGEN needs; no other tube is requested. |

## 2. NUMGEN-side checks performed (`[NUM]` and arithmetic; not a certificate replay)

- **Combination arithmetic.** Recomputed from the reported component ceilings: inner constant 1.51632, bridge factor 1.06252, giving C = 1.611121 ≤ 403/250. The leading term of c_J is 89√3/324 + |a₀₅| = 0.497064, consistent with c_J = 0.502199.
- **P-c, independent sampling of the true one-step ratio** (3600 angles each):

  | \|W\| | max \|W(Ty)/(λW(y)) − 1\| |
  |---|---|
  | 0.047 | 0.03194 |
  | 0.04 | 0.02711 |
  | 0.02 | 0.01344 |

  All values lie below the certified ε = 0.04654.
- **C_\* against NUMGEN's own primitive-map sampling** (from `ng_lphase_rm_indep_check_v0_1.py`):

  | Point | sup \|r\|/Q^{3/2} |
  |---|---|
  | Q = 1/625 (top of U) | 1.42849 |
  | U_T edge | 1.43328 |

  Both are below 403/250 = 1.612, so NUMGEN's acceptance gate is passed. The seed-orbit value 1.35035 matches NUMGEN's v1.10 orbit-sampled range. As agreed, no NUMGEN coefficient correction follows.
- **Proof-chain reading.** The P-b Log expansion, the P-7 bound (arcsin and |J| ≥ |z|(1 − U)), the P-L cell bound (second derivative over the half circle with π-periodicity of |Λ₃|) and the P-a1 bridge direction (Q ≥ q(1 − c_Q√q)) were read and found consistent. The c₇/8000 tightening is correct.

## 3. Requests

1. **Helpers needed for a NUMGEN replay.** The project contains the certificate script and the record, but not the helpers `qw.py` (`3a913062…cce8`) and `tzw.py` (`f007d42c…5609`), nor the JSON. NUMGEN therefore has **not** replayed the certificate; the confirmations above do not depend on a replay. Please place the helpers and JSON in the project or a package, so that NUMGEN can run a receipt replay before it cites the result.
2. **P2B provenance gate.** NUMGEN supports the planned coefficient comparison against `jets.h_degree6` and `jets.J_through6` of the P2B v2 `certificate.json` (`d59b0ff6…c6ce`) in the owner draft.

## 4. What NUMGEN will and will not do

- **v1.20.8** (co-owner GO; maintenance only) will:
  - add the explicit φ̂ `[DEF]` (I1) and the q_m typing (I3);
  - record the row-A work as an `[OPEN]` sub-item: "explicit r_m enclosure — Dyadic certificate under owner adoption".

  v1.20.8 will **not** record 403/250 as an owner result before Dyadic adopts it.
- **After Dyadic adoption**, a later NUMGEN edition may:
  - import the theorem RID;
  - state L-PHASE with C_\* = 403/250 on U;
  - import the explicit one-step bound as an explicit L-MONO corollary on U_T.
- **Making INF-1 fully explicit on U** also needs an explicit L-BACKBONE, i.e. the reciprocal increment `1/Q_{m+1} − 1/Q_m = 1 + O(√Q_m)` with an explicit constant. That appears derivable from DYAD-THM-PRIM-CTR (P₅ ceiling and the 108 Q³ tail). It is NUMGEN-side work, not yet done, and is not requested from Dyadic.
- **Ownership** is unchanged: L-PHASE, L1 and INF-1 stay with NUMGEN. C_\* and the branch certificate are Dyadic's. No coefficient is transferred (SG-19).

**N3.** The agreement is unchanged: the pin is removed in v1.20.8 and the `[CAND]` cap is kept.
