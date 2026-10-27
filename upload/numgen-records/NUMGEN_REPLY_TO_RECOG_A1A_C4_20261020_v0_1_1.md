# Number Genesis → RECOG — Review response to the A1a C4 question (v0.1.1)

**Date:** 20 October 2026 · **From:** Number Genesis owner side (Claude, DSN editor/auditor; PI keeps final decision) · **To:** RECOG owner
**Re:** `RECOG_A1A_C4_QUESTION_TO_NUMGEN_20261020_r2.md`
**Status:** `[SESSION]` review response. Nothing is adopted on either side. No NUMGEN file is changed. **v0.1.1** supersedes the undispatched v0.1 (`8a887ef31206334d78ced4cb0bc91d6a8cad5c010f7d0960e1ecb64810ffbc4d`). It changes Q3 only: the source pointer is corrected, the session grade of the branch bound is stated, and the ongoing Dyadic certificate work is noted. Q1, Q2 and Q4 are unchanged. Co-owner GO: 20 Oct 2026.
**Basis:** Number Genesis v1.20.7 (`c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28`, project copy verified), §6.6 N-5A-S1-INF (L2126–L2311), §6.2 L1 (L943–L1153).

---

## Preliminary checks

- **Same objects.** NUMGEN's section angle `Θ = atan2(√3·η_wrap, 2ρ − η_wrap)` (L2104) is exactly `arg W` for `W = ρ + ω·η_wrap`, `ω = e^{2πi/3}`: `Re W = ρ − η/2`, `Im W = (√3/2)η`. Also `|W|² = ρ² − ρη + η² = Q_true` (L898). So RECOG's `W`, `Q` and the lift `φ̂` of `arg W` are NUMGEN's objects. Checked symbolically.
- **The finite-block identity is an exact rearrangement of NUMGEN's definition.** With `D_M := 2πM − (φ̂_{6M} − φ̂_0)` (L2186) and `Θ_W(M) − Θ_W(0) = φ̂_{6M} − φ̂_0 − 2πM`, the identity
  `D_M − τ log M = τ log Q_0 − (Ψ_W(M) − Ψ_W(0)) − τ log(M·Q_M)`
  holds identically. Checked symbolically. Its only content beyond algebra is the branch statement that the block-sampled `Θ_W` is the continuous lift with exactly 2π removed per block. That is what RECOG's explicit `π/6 < δ_T < π/2` secures.

## Q1 — Does INF-1 depend on R9, or on anything that depends on R9?

**No.** The proof chain is:

| step | basis in NUMGEN v1.20.7 | external input |
|---|---|---|
| L1 radial law `ΔQ_true = −Q_true² + O(Q_true^{5/2})` | exact symbolic composition of the primitive map (L947, L1010) | none |
| L-BACKBONE `q_m = 1/m + O(m^{-3/2})`, `Σ_{m<M} q_m = log M + C_Q + o(1)` | from L1 (L2133–L2149) | none |
| L-MONO `δ_T = π/3 + O(Q^{1/2})` | exact one-step map, `W(Tx) = e^{iπ/3}W + O(|W|²)` (L2152–L2164) | none |
| L-PHASE `φ̂_{6(m+1)} − φ̂_{6m} = 2π − τq_m + r_m`, `|r_m| ≤ C q_m^{3/2}` | exact six-step Taylor composition; "not an import from the continuous cubic-vector truncation" (L2166–L2182) | none |
| INF-1 `D_M = τ log M + C_D + o(1)` | L-BACKBONE + L-PHASE (L2184–L2190) | none |

No live NUMGEN line imports RECOG; a scan of the pre-changelog text finds no R9 or RECOG import. The only Dyadic import in the neighbourhood is `DYAD-THM-PRIM-CTR` (v1.20 explicit-domain block, L2124). It discharges tube membership of the named seed only. INF-1 does not use it, and the owner's own guard says the GAP-LOCK angular hypotheses "remain Number Genesis obligations discharged by L-MONO / L-PHASE".

**Existence of `C_D`.** It is part of the INF-1 statement, and the proof makes it explicit:
`D_M = Σ_{m<M}(τ q_m − r_m)`, so `C_D = τ·C_Q − Σ_{m≥0} r_m`.
Both pieces converge: `Σq_m − log M → C_Q` by L-BACKBONE, and `Σ|r_m| ≤ C Σ q_m^{3/2} < ∞`. `C_D` depends on the starting point, as RECOG assumes.

## Q2 — Is `D_M` defined for an arbitrary start, with no B-event anchor?

**Yes; C2 is correct.** `D_M` uses only the start `x_0`, the block counter `M` counted from `x_0`, and the increasing lift of `arg W` along the orbit, which exists because the punctured tube is forward invariant with `W ≠ 0`. B-event anchors `n_j` enter only GAP-LOCK Lemma 3 (L2263–L2285), through `G_n` with `G_{6M} = D_M`, and not the definition of `D_M` or INF-1.

## Q3 — Would an explicit radius for INF-1 need a uniform enclosure of `r_m`? Does NUMGEN hold one?

**Yes, it would need one, and NUMGEN does not hold it.**
- **Angular side, missing.** NUMGEN holds `|r_m| ≤ C q_m^{3/2}` with `C` and the radius existential. The certificate is an exact symbolic jet certificate, not an interval enclosure, and the owner guards say so: "local/existential in radius" (L2305) and "local existence, not optimized radius" (L1127). For INF-1 on a named radius, existence needs only some finite `C` valid on that whole tube, not a sharp one.
- **Radial side, already explicit upstream, not in NUMGEN.** Dyadic `DYAD-THM-PRIM-CTR` gives phase-uniform ceilings, `|P_5| ≤ (16931/10000)·Q^{5/2}` and `|R^{prim}_{≥6,rad}| ≤ 108·Q³` on `Q ≤ 1/400`, plus `Q_m ≤ Q_0/(1 + ½Q_0 m)`. These give an explicit reciprocal-increment bound `1/q_{m+1} − 1/q_m = 1 + O(√q_m)` and hence explicit `Σ q_m^{3/2} < ∞`. That covers L-BACKBONE's role. Custody stays with Dyadic.
- **Branch control:** RECOG's explicit `π/6 < δ_T < π/2` (error constant `143209/750000 < 1/2`) covers L-MONO's role on the explicit tube. Its source is the A1a session record (`RECOG_A1A_CD_IDENTIFICATION_SESSION_v0_2.md`, `b4906ddf…c428`). It is not in RECOG v0.3.21, so it carries session grade until RECOG adopts it.

So the only missing piece for a fully explicit NUMGEN INF-1 is a uniform enclosure of the six-step **angular** remainder `r_m` on the named tube. NUMGEN does not hold it.

**Where it can come from.** The relevant adopted inputs are the Dyadic per-block results:
- `DYAD-THM-OPEN3-SPIRAL-REM`, which is unconditional;
- `DYAD-THM-NF-REM`;
- `DYAD-THM-NF-INV`.

Dyadic OPEN 21 is not the relevant input. It concerns the asymptotic memory `M_W` and is conditional on R9.

**Status of that work.**
- Dyadic and NUMGEN have agreed a session-level scope: `DYAD_NUMGEN_LPHASE_ANGULAR_ENCLOSURE_SCOPE_v0_1.md`, `1eae1d1a…1f74`, reviewer outcome *row A certification authorized*.
- It covers an explicit `C_*` with `|r_m| ≤ C_* Q_m^{3/2}` on row A, without R9.
- No constant has been certified yet, and Dyadic §6.14 still lists quantitative GAP-LOCK angular inequalities as not established.
- If the certificate is adopted, INF-1 on the explicit tube would follow without R9. That would bear on RECOG's existence route, which is currently limited to `U ∩ U_NUMGEN`.

## Q4 — Should NUMGEN record the identification `C_D = τ log Q_0 − M_W` (conditional on R9)?

**Recommendation: keep it a RECOG session result for now; the PI decides.**
1. NUMGEN needs only the **existence** of `C_D`. Its value enters no live theorem, and the owner calls the Fatou/`C_D` question "optional refinement, not a GAP-LOCK blocker" (L2296).
2. Recording it would give NUMGEN its first dependency on RECOG, conditional on R9 via Dyadic T1. Meanwhile RECOG's R9-independent existence route consumes NUMGEN's INF-1. Neither is circular as a proof, but a two-way provenance link should not be created for an optional remark.
3. If RECOG later adopts A1a at owner grade, NUMGEN can add a **one-line provenance pointer**, not an import, under the optional question. Proposed wording: *"An external identification `C_D = τ log Q_0 − M_W`, conditional on RECOG R9 via Dyadic T1, is recorded in RECOG vX; it is not imported, and no NUMGEN theorem depends on it."*

## On the R9-independent existence route

No objection from the NUMGEN side; the claim is RECOG's. Two qualifiers should travel with any use of INF-1:
- **Domain.** INF-1's domain is NUMGEN's existential tube. The route therefore gives existence on `U ∩ U_NUMGEN`, as RECOG states. On that domain `MQ_M → 1` already follows from L-BACKBONE alone (`q_M = 1/M + O(M^{-3/2})`), without Dyadic.
- **Generator.** INF-1 is "conditional on the selected continuous generator `T` under OPEN-P0" (guard L2305). That qualifier should be carried.
