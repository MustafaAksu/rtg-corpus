# Number Genesis → Dyadic — Receipts, N3 answer, and a request on the GAP-LOCK angular enclosure

**Date:** 20 October 2026 · **From:** Number Genesis owner side (Claude, DSN editor/auditor; the PI keeps the final decision) · **To:** Dyadic DSN owner
**Status:** `[SESSION]` memo. **Prepared for PI dispatch; not sent.** No owner file is modified. Nothing is adopted on either side.
**Basis:**
- NUMGEN: `RTG_NUMBER_GENESIS_DSN_v1.20.7`, `c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28`. This is the current NUMGEN edition; there is no newer one.
- Dyadic: adopted `RTG_DYADIC_OSCILLATOR_DSN_v6.4.18`, `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d`.
- DYAD reply to RECOG G3 v0.1.2, §3.

---

## 1. Receipts N10–N14

| Notice | NUMGEN status | Use |
|---|---|---|
| N10 (OPEN 3 spiral residual; v6.4.14) | **RECEIVED** | none at present. See §3: a possible future use as a *bound* input. That would not be a coefficient transfer. |
| N11 (OPEN 3b asymptotic phase; v6.4.15) | **RECEIVED** | none. See §2 for a possible bearing on N3. |
| N12 (OPEN 3 lifecycle, OPEN 21 opened; v6.4.16) | **RECEIVED** | none (informational) |
| N13 (OPEN 21; v6.4.17, conditional on R9) | **RECEIVED** | none. NUMGEN takes no R9-conditional input. |
| N14 (smooth embedding; v6.4.18) | not addressed to NUMGEN; seen only | none |

- NUMGEN accepts the SG-19 condition in N10–N13 as stated: no transfer of L1 or ISP-angle coefficients.
- These receipts are given here at session level. They enter the NUMGEN owner record at the next NUMGEN edition, a planned consumer-sync release v1.20.8.
- NUMGEN's import `DYAD-THM-PRIM-CTR` was checked against v6.4.18:
  - the §6.14 statement is unchanged, per your passage hash `a611ab681837`;
  - the import stays valid;
  - only the version pin will move.

## 2. N3 answer — the `DYAD-CAND-PHISTAR-ENTRY-PHASE` pin

**Where it occurs.** The pin occurs in one live place in NUMGEN v1.20.7: §6.1 NG-0R, the `[DEF]` pre-registration pin of the parallel, non-blocking audit `HYP-NG-0R-COV`. The audit is `[OPEN]`. The pin reads:

> "`Q_0 -> lambda Q_0` acting on gauge-reduced entry data only through the entry-phase shift `tau ln lambda` of the `[CAND]` phi* law (`DYAD-CAND-PHISTAR-ENTRY-PHASE`) … Any conclusion inheriting the phi* leg is capped at `[CAND]`."

The pin was added in the v1.4-series audit-hygiene patch (August 2026). No artifact, certificate or owner source for the "phi* law" is registered in NUMGEN. **NUMGEN cannot identify the historical source**, and accepts that the RID does not exist in Dyadic.

**NUMGEN action (next edition).**
- The RID is removed from the pin.
- The pin will read `[RID unavailable — historical phi* entry-phase law; source not identified (Dyadic N3)]`.
- The `[CAND]` cap is retained.
- No result depends on this pin. `HYP-NG-0R-COV` remains an unexecuted parallel audit.

**Question to Dyadic (optional, no RID requested).** The leading-order content of the pin is a flow-translation statement:
- Along the backbone, `ΔΘ ≈ −τq` and `Δlog q ≈ −q`.
- So `Θ − τ log q` is invariant at leading order.
- A rescaling `Q_0 → λQ_0` along the flow shifts the entry phase by `τ ln λ`.

This looks like the leading-order content of the asymptotic phases `Ψ_z`, `Ψ_W` in `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` (v6.4.15). Those objects are conditional on RECOG R9.

Does Dyadic regard those objects as the right current home for the content, so that NUMGEN could cite them when the audit is executed? This is offered as a candidate identification only. NUMGEN does not assert it. NUMGEN will not cite those objects without Dyadic's view.

## 3. Request — explicit enclosure of the NUMGEN L-PHASE angular remainder

**Background.**
- NUMGEN L-PHASE (v1.20.7 §6.6) reads
  `φ̂_{6(m+1)} − φ̂_{6m} = 2π − τ q_m + r_m`, with `|r_m| ≤ C q_m^{3/2}`.
- Here `C` and the radius are existential.
- INF-1, `D_M = τ log M + C_D + o(1)`, inherits that existential radius.
- Your §6.14 correctly states that "quantitative GAP-LOCK angular inequalities" are not established anywhere.
- RECOG R10 states that the §6.14 enclosure "lifts the existential-radius guard on NUMGEN long-orbit results". That is RECOG's rationale sentence; the work has not been done.

**Notation.** NUMGEN's `q_m` is the block-sampled **primitive** `Q_true = |W|²` (your `Q_prim`). It is not your chart variable `q = |z|²`. Below, `Q` is primitive and `q = |z|²`.

**Candidate route (not executed, not checked).** With `z = h^{-1}(W)`, `D_Q = Q − q`, and principal angle increments:

```text
r_m = [Arg(J(z)/z) + τq]          explicit polynomial J; expected O(q²)
    + [Arg(F̂(z)/z) − Arg(J(z)/z)]  from DYAD-THM-NF-REM, |F̂ − J| ≤ C_7|z|^7
    + S_Θ(z)                       DYAD-THM-OPEN3-SPIRAL-REM (unconditional): |S_Θ| ≤ 0.705 q^{3/2} on |z| ≤ 1/20
    + τ·D_Q(z)
```

Then `q ≤ (256/225) Q` (DYAD-THM-NF-INV) converts the bound to primitive `Q`. The tube compatibility is already adopted: `Û_T ⊂ {|z| < 1/20}`, and the disk is forward-invariant. No R9 input enters.

**Two pieces are not written anywhere:**
- (P-a) a certified ceiling `|D_Q| ≤ c_Q q^{3/2}` on each NF-REM row. `D_3` is explicit; the degree 4–12 part needs a majorant from the P3 coefficient data.
- (P-b) a certified bound on `Arg(J(z)/z) + τq`, i.e. on `ΔΘ_z` beyond RECOG-ALG-CHART-LAWS. Your v6.4.14 §6.14 lists this item as not established.

**Requests.**
1. **Custody of P-a and P-b.** Both are chart-native objects of DYAD-ALG-NF6. Would Dyadic prefer to certify them in its own ledger? NUMGEN would then import them. The alternative is for NUMGEN to derive them from your adopted data, citing it. NUMGEN prefers the first option but does not require it.
2. **SG-19 reading.** Please confirm, or correct, the following reading. Composing your adopted *bounds* (NF-REM, NF-INV, OPEN3-SPIRAL-REM, P-a, P-b) into a bound on NUMGEN's primitive `r_m` is not a coefficient transfer under SG-19. No chart coefficient would be read as an L1 or ISP-angle coefficient.
3. **Branch.** NUMGEN's lift adds exactly `2π` per block, and L-MONO gives `π/6 < δ_T < π/2` per step. The route needs the principal value `ΔΘ_W = Arg(W_{m+1}/W_m)` to equal `φ̂_{6(m+1)} − φ̂_{6m} − 2π` on the whole row disk. Is `|ΔΘ_W| < π` there already certified on your side, or should NUMGEN prove it?
4. **Rows.** Unless you advise otherwise, NUMGEN would use row A (`|z| ≤ 1/20`, `C_7 = 100`), because the PRIM-CTR tube maps into it. Rows will not be mixed.

**What NUMGEN would claim if the route closes.** A `[THM]` or `[RESULT] [from: ALG]` enclosure `|r_m| ≤ C_* Q_m^{3/2}`, with explicit `C_*` on the PRIM-CTR tube, and hence INF-1 on that explicit tube. The claim is not: an optimal constant; any statement about `C_D`'s value; or any physical event reading. The conditional generator scope (SG-14 / OPEN-P0) stays.

## 4. Information only

- NUMGEN has not been re-released since v1.20.7. Your §7 consumer row and header ("not re-inspected since v6.4.11") remain accurate for NUMGEN. A NUMGEN consumer-sync release (v1.20.8) is planned: pins, these receipts, and the N3 edit. It changes no scientific result.
- FMS v0.6.4 R8 attributes a κ = 0 relative holonomy limit to "NUMGEN/DYAD provenance". NUMGEN v1.20.7 contains no such statement. If Dyadic is also cited there, you may wish to check it. NUMGEN will raise it with FMS separately.

## 5. Replies requested

- §2: optional view on the candidate home of the phi* content.
- §3: items 1–4.
- No reply is needed on §1 or §4.
