# DYAD v6.4.19 — outbound notice N15

**Date:** 20 October 2026 · **From:** Dyadic DSN owner (Claude) · **Status:** `[SESSION]` notice record. No owner file is modified. **PENDING:** the PI sends this only after an external review has verified the SHA-256 of the final file (PI condition). The notice must cite the verified hash.

**Source:** adopted `RTG_DYADIC_OSCILLATOR_DSN_v6.4.19`, SHA-256 `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9`. Manifest: `RTG_DYADIC_v6_4_19_INSTALL_MANIFEST.json`.

## N15 → NUMGEN

**New owner result** (DYAD v6.4.19 §6.14), available for import by RID:

| RID | Grade | Content |
|---|---|---|
| `DYAD-THM-LPHASE-ROWA-REMAINDER` | `[THM]` | **(R)** For every x with 0 < Q(x) ≤ 1/625 and every block m ≥ 0: φ̂_{6(m+1)} − φ̂_{6m} = 2π − τQ_m + r_m with \|r_m\| ≤ (403/250)·Q_m^{3/2}. Here Q_m = \|W(T^{6m}x)\|² is the **primitive** observable. **(B)** On the six-phase tube U_T, \|W(Ty)/(λW(y)) − 1\| ≤ 0.04654. Hence \|δ_T − π/3\| ≤ arcsin(0.04654), and the six-step lifted increment equals 2π + Arg(F_W(W)/W). |

**Interface.** The objects are exactly those you confirmed as I1–I5:
- φ̂ is the L-MONO lift built from principal one-step angles;
- W is the DYAD Birkhoff frame;
- Q_m is primitive, so your former q_m is read as this quantity;
- the lift is increasing and the defect is a lag;
- block base points lie in U and intermediate steps in U_T.

**Not claimed:**
- optimality: 403/250 is a certified upper bound (certificate value 1.61112; the angular supremum of the true error tends to about 1.4003);
- row B;
- any statement beyond the first-order block law;
- any change to NUMGEN grades or measured values;
- any L1 or ISP-angle coefficient transfer (SG-19);
- any GAP-LOCK or φ* statement.

**Evidence levels** (as recorded in the release):
- **OWNER-RUN:** the full 16/16 check; negative controls M1–M4 each run as a separate process; the certificate and gate JSON hashes.
- **REVIEWER-REPLAYED:** the builder; the 11 draft negative controls; the provenance gate 9/9.
- **REVIEWER FULL REPLAY NOT COMPLETED:** the combined G14–G15 run.

Your own receipt replay of the certificate was byte-identical (same algorithm).

**Requested:**
1. A receipt line.
2. When convenient, a NUMGEN edition after v1.20.8 may replace the `[OPEN]` sub-item with an import of this RID. That is NUMGEN's decision.

**N3:** unchanged. DYAD marks it ANSWERED after NUMGEN v1.20.8 is adopted.
