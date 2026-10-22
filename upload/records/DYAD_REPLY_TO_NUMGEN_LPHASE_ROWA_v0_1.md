# DYAD reply to NUMGEN — L-PHASE angular remainder, row A: result and interface confirmation request (v0.1)

**Date:** 20 October 2026 · **From:** Dyadic DSN owner (Claude) · **To:** NUMGEN owner · **Status:** `[SESSION]` interface note. **Prepared for PI dispatch; delivery not yet confirmed.** No owner file of either stream is modified.

**In reply to:** NUMGEN Requests v0.1 (20 Oct 2026), §3, the request for an explicit certified constant in L-PHASE.

## 1. Result available

DYAD offers the following result as a separate import. It has been reviewed at SESSION level (`L-PHASE ROW A SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION PENDING`) but is not yet adopted by the DYAD owner.

For every x with 0 < Q(x) ≤ 1/625 (the DYAD-THM-PRIM-CTR set U, which contains the canonical seed (1/100, 1/250)) and every block m ≥ 0:

φ̂_{6(m+1)} − φ̂_{6m} = 2π − τQ_m + r_m,  |r_m| ≤ (403/250)·Q_m^{3/2},

where Q_m = Q_true(T^{6m}x) = |W_m|² is the primitive observable.

In addition, on the whole six-phase tube U_T, every one-step increment satisfies |δ_T − π/3| ≤ arcsin(0.04654). Hence the six-step lifted increment equals 2π + Arg(F_W(W)/W) exactly, which is the branch identification L-PHASE uses.

**Sources.**
- Record `DYAD_NUMGEN_LPHASE_ROWA_CERTIFICATE_SESSION_v0_1.md` (SHA-256 `775c6715e1a5ba3c020927c1990c1843120cecd3e3b2855be17c959947cf233d`).
- Certificate `dyad_numgen_lphase_rowA_cert.py` (`117484ae…59cdb`); 10 gates, 6 negative controls; JSON `8697c697…c4ad4fa`.
- Scope note `DYAD_NUMGEN_LPHASE_ANGULAR_ENCLOSURE_SCOPE_v0_1.md` (`1eae1d1a…1f74`).

## 2. Interface confirmations requested before DYAD owner adoption

The certificate fixes the objects below. Please confirm that they are the L-PHASE objects, or name the difference.

| # | Object | DYAD reading used by the certificate |
|---|---|---|
| I1 | Lift φ̂ | Sum of the **principal** one-step angles δ_T(y) = Arg(W(Ty)/W(y)) along the primitive orbit, i.e. the L-MONO lift (δ_T ∈ (π/6, π/2)); φ̂_{6m} taken at the block base point T^{6m}x |
| I2 | Frame W | W = u + iv, u = ρ − η/2, v = (√3/2)η (DYAD §1 Birkhoff frame, lifted local η), with W(Tx) = e^{iπ/3}W + O(\|W\|²) |
| I3 | Observable | Q_m = \|W(T^{6m}x)\|², the primitive Q_true. The "q_m" in the v1.20.7 L-PHASE text is read as this primitive quantity, **not** the DYAD chart variable q = \|z\|² |
| I4 | Sign convention | Increasing lift; block law 2π − τQ_m + r_m (defect read as a lag) |
| I5 | Domain | Block base points in U = {0 < Q ≤ 1/625}; intermediate steps in U_T. If NUMGEN needs a different explicit tube, please name it |

## 3. What does not change

- L-PHASE, L1 and their grades stay NUMGEN-owned. DYAD supplies a constant and a branch certificate; it transfers no coefficient (SG-19).
- No change to NUMGEN's measured values is requested. *Information only:* the sup over all angles of |r|/Q^{3/2} tends to about 1.4003 as Q → 0. The NUMGEN seed orbit gives 1.3503, which lies inside the v1.10 range [1.3449, 1.3565].
- Row B (|z| ≤ 1/40) is not covered. Optimality of 403/250 is not claimed.

## 4. Next steps on the DYAD side

After I1–I5 are confirmed:
1. The result goes into a DYAD owner draft under a new theorem RID, assigned at drafting.
2. The draft carries the exact record, the certificate hash, and an added provenance gate: a coefficient comparison of the regenerated normalizer h and jet J with `jets.h_degree6` and `jets.J_through6` of the adopted P2B v2 `certificate.json` (`d59b0ff68b4341debf5e8a7542bf3865b63dd63e36546952db95298c2bd5c6ce`).
3. Adoption follows review of that draft.

**On N3 (φ\*).** DYAD supports removing the historical pin `DYAD-CAND-PHISTAR-ENTRY-PHASE` in NUMGEN v1.20.8 and keeping the `[CAND]` ceiling. The adopted DYAD asymptotic-phase objects are not a substitute for the historical φ* law. N3 will be marked answered in DYAD after v1.20.8 is adopted.
