# OFN source review — addendum: FMS ledger v0.6.2, DYAD v6.4.14, RRF v0.8.3 (v0.1)

**Date:** 19 October 2026 · **Author:** Claude (OFN co-owner) · **Status:** `[SESSION]`. Addendum to `OFN_SOURCE_REVIEW_ER2B_GEN288_OPEN3_v0_1_1.md` (SHA-256 `8d18640f…0944`; accepted by both co-owners as OFN v0.10 input). No owner file is modified. No OFN decision is changed. Q1–Q6 verdicts stay as they are.

## 0. Sources

| Source | State | Read |
|---|---|---|
| `FMS_MODEL_SELECTION_LEDGER_v0_6_2_SESSION.md` | FMS `[SESSION]`; the file header reads "v0.6.1" while the filename and the §12B change note say v0.6.2 | full |
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_14.md` | `[OWNER]` adopted 19 Oct 2026 | full |
| `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_3.md` | RRF working standard, adopted 19 Oct 2026 | full |
| Genesis D-4 session record v0.1 / v0.1.1, `d4_transported_cubic_cert.py`; FMS `FMS_PSI_QUINTIC_KAPPA_ALL_v0_1.py` and its modulus note | earlier listed in the project, **no longer present** | not read |

## 1. D3 — the ψ modulus for every κ

**FMS (§12B, SESSION).**
- The κ-all script eliminates the κ-independent Φ₃ block.
- With symbolic t = (1 − κ)/κ, it reports a 9×9 minor equal to a nonzero constant, independent of t.
- Conclusion: the first-order obstruction in the direction a ∈ iℝμ holds for every real κ ∉ {0, 2}.
- The completeness lemma covers the earlier audit guard: even generators vanish, and non-equivariant degree-5 generators drop out under the ℤ₆ projection.

**OFN independent check.** Script `OFN_PSI_KAPPA_ALL_MINOR_CHECK_v0_1.py` (SHA-256 `c56a01ac…a9e3`, exit 0, ~15 s). It uses a different method from FMS and does not share its code.
- The entries of [A | d₅] are affine in t; this was verified at κ = 3. Only 8 of the 32 columns depend on t, so every 32×32 minor is a polynomial of degree ≤ 8 in t.
- rank A = 31 at 21 distinct t. Hence every 32×32 minor of A vanishes identically, and rank A ≤ 31 for every t.
- One fixed 32×32 minor of [A | d₅] takes the same nonzero value at all 21 points: −16416686845683351829 / 1855672460829295245297723250394879490524310405120. It is therefore a nonzero constant.
- Consequence: rank [A | d₅] = 32 > rank A for every t. The obstruction holds for every real κ ≠ 0. κ = 2 is excluded by the scope of the centre-manifold reduction, because the closure mode is not hyperbolic there.

**Revised D3 wording for OFN v0.10** `[ALG — SESSION; two independent computations]`:

> In the transported class, the λ-equivariant cubic chart change g_a(z) = z + a z²z̄ gives formally non-conjugate models for every real κ ∉ {0, 2}, in the direction a ∈ iℝμ, at degree five. For a ∈ ℝμ the models coincide through degree five, because g_a agrees with an element of Cent(N).

- **What changed.** v0.1.1 said "all but finitely many κ". The exceptional set is now **empty**.
- **Limits, unchanged.**
  - The result is first order in a.
  - It covers only the connected linear stabilizer. Discrete stabilizer components and finite a are OPEN.
  - It is formal conjugacy through degree 5.
  - No observable readout of the modulus and no physical model selection follows.

## 2. DYAD v6.4.14 — OPEN 3 is now owner-adopted

**Owner facts.**
- `DYAD-ALG-OPEN3-LEADING` `[ALG]` and `DYAD-THM-OPEN3-SPIRAL-REM` `[THM]` are adopted, with per-row constants. The constants are suprema of majorants, not of the true errors.
- OPEN 3 is PARTIAL:
  - 3a, the per-block chart residual: CLOSED;
  - 3b, asymptotic-phase transfer P4: OPEN;
  - 3c, the historical fit P0: BLOCKED.
- N9 is RECEIVED by RRF (v0.8.3). On the OFN side it is received at session level only, with owner level pending OFN v0.10.

**Effect on the v0.10 table.** Row R-5 ("reference until v6.4.14") becomes direct import **I-3**. The transfer scope of v0.1.1 §4 stays exactly as written:
- the static leading offsets D₃ and D_{Θ,1} transfer edgewise, and class-wide at leading order;
- the per-block bounds K_Θ and K_Q transfer **only on the exact lock surfaces**, edgewise, conditional on the real surfaces (J);
- nothing transfers off the surfaces;
- nothing transfers as a separator or basin statement.

**§4.1 readout guard.** Its single-edge ingredient (D₃, D_{Θ,1}) is now owner-grade. The network-mode statement u_W = O(|v|²) on 𝒮₊ stays OFN SESSION, and its coefficient depends on the convention.

**N9.** OFN v0.10 should record N9 as answered at owner level once v0.10 is adopted. Until then, keep the session-level receipt.

## 3. RRF v0.8.3 — representation contract for class C

**Relevant RRF rules.**
- **§0.3.** Re-imposing linear addition or projection in new coordinates creates a *different conditional model*, not a passive rechart.
- **Representation safety lock (provisional until OPEN-E).** Network equations live in `RRF-NET-W-RAW`. z_NF may appear in network work only inside transported single-dyad subexpressions.
- **§6.2.** Every realization contract must declare `regularity` and `clock`.
- **§2.4b–c.**
  - In the C∞ and analytic categories, an odd chart exists if and only if a tangent-to-identity square root of F exists. RRF registers this as an algebraic consequence of the DYAD owner results; it is not an existence proof.
  - B-6 ⇔ B-an ∧ B-3, hence B-6 ⇒ B-an.
  - Both agree with OFN v0.7.2 §3.5(e).

**Consequence for v0.10 (new item D6, wording/contract only).**
- Class C, F_κ = P_κ ∘ N^{×3} in the N- or Φ-chart, is a **different conditional model** in the sense of RRF §0.3. It is not a passive transport of the raw κ-family and not an `RRF-NET-W-RAW` equation set.
- v0.10 should state this explicitly and declare, for class C:
  - regularity: formal now; analytic or C∞ conditional on B-6 / B-∞ existence;
  - clock: primitive T, with T⁶ as derived sampling;
  - the domain;
  - its readout chart: transported or raw, see §4.1.
- OFN should also send RRF an interface request to register class C as a **model contract row**, not as a new native profile, while OPEN-B/E1 stays locked. The registration decision belongs to RRF.

## 4. D-4

The Genesis D-4 session record and its certificate are no longer in the project, so this review cannot assess them. D-4 stays `[OPEN]`; both co-owners agree on this. If the PI provides the record again, it should be reviewed before the v0.10 Q6 section is finalized.

The reduced-map computations here, for κ = 1/2 and κ = 3, confirm one link of the chain at formal level: the reduced cubic is κ-independent. That is corroboration, not the D-4 argument.

## 5. Delta to the v0.10 table (v0.1.1 §5)

| # | Change |
|---|---|
| I-3 (was R-5) | DYAD v6.4.14 `DYAD-ALG-OPEN3-LEADING`, `DYAD-THM-OPEN3-SPIRAL-REM`: direct import, with the v0.1.1 §4 transfer scope |
| D3 | "all but finitely many κ" → **every real κ ∉ {0, 2}**. Other limits unchanged |
| D6 (new) | Class C declared a re-imposed conditional model (RRF §0.3), with regularity, clock, domain and readout chart stated. Interface request to RRF for a model-contract row |
| Pins | DYAD v6.4.14, Genesis v2.8.8, RRF v0.8.3; FMS ledger v0.6.2 (SESSION) |
| Housekeeping to FMS | Header/filename mismatch (v0.6.1 vs v0.6.2). §0 manifest still pins Genesis v2.8.7, DYAD v6.4.13 and RRF v0.8.2. The OFN v0.7.2 working-copy SHA `6044f43e…5b4c`, verified by both co-owners, can replace "user-reported" |
| Unchanged | Q1–Q6; Standard C at cubic order; A1/A2/B dispositions; class C the primary formal candidate; D-4 OPEN; OPEN-C19-L OPEN; J realization (OPEN 20) OPEN |

## 6. Non-claims

- No physical model is selected by D3.
- No network basin statement is drawn from OPEN 3.
- The RRF registration of class C is requested, not assumed.
- Files absent from the project were not reviewed.
