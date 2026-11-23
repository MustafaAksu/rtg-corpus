# FMS Pilot — Closeout Record v0.1

**Date:** 19 October 2026 · **Status:** `[SESSION]`. Closeout approved at session level by both FMS co-owners (ChatGPT, Claude). **Final closeout is a PI decision.** No owner DSN is modified.
**Disposition:** `FMS PILOT — SCIENTIFIC SCOPE COMPLETE / CLOSEOUT APPROVED AT SESSION LEVEL`.

> **Boundary.** Closing the pilot does **not** adopt class C as a physical model. It does not select a carrier, a chart ψ, a chirality or an exchange operation.

## 1. Pilot goal and outcome

The pilot set out to evaluate the candidate triad network models against explicitly declared physical requirements, and to classify the surviving candidate. The physical requirements are now owner-adopted in OFN v0.10.

| Pilot output | Grade / owner |
|---|---|
| Model elimination against Q1–Q6 and Standard C | Requirements: `[OWNER]` OFN v0.10 §5.5 |
| Raw A1 (κ = 1), raw A2 (0 < κ < 2, κ ≠ 1): excluded under Standard C at cubic order. Raw B (κ = 0): decoupled reference | OFN v0.10 (`RTG-OFN-ALG-RAW-STANDARD-C-NOGO`, OFN custody); Genesis six-step RIDs (v2.8.9) |
| Class C (transported κ-family) is the primary formal candidate. Q6 by `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` and the narrow-Q6 corollary | OFN v0.10 §5.5; Genesis v2.8.9; `RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT` |
| ψ-chart family classified through degree 5 (see §2) | `[SESSION — ALG]` FMS; reference-only in OFN (RF-O10-02) |
| Realization separated out as a single external dependency | DYAD OPEN 20 (PARTIAL) |

## 2. FMS ψ results (SESSION, closed at degree 5)

| Result | Grade | Evidence |
|---|---|---|
| First-order quintic obstruction in the iℝμ direction, κ = 1 | `[ALG — SESSION]` | `FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py` `550adcb8…e7eb` |
| Same, for every κ ∉ {0, 2}; κ = 2 in the odd category | `[ALG — SESSION]` | `FMS_PSI_QUINTIC_KAPPA_ALL_v0_1.py` `2849e32f…013e`; note v0.1.1 |
| Explicit invariant c(κ, a), 8 first-order moduli in the S₃ class | `[ALG — SESSION]` | `FMS_PSI_QUINTIC_PHASE_INVARIANT_v0_1.py` `1c4ab0d0…212f` |
| \|c\|² invariant under every formal conjugacy | `[ALG — SESSION]`; also run on the PI machine | `FMS_PSI_QUINTIC_FINITE_INVARIANT_v0_1.py` `ad44f66a…445f4c` |
| Within the chart family (reduced maps, 5-jet): f_{κ,a} ∼₅ f_{κ,b} ⟺ m(a) = m(b), with m = Im(aμ̄); the ℤ₂ reflection is excluded | `[THM — SESSION, formal 5-jet]` | `FMS_PSI_QUINTIC_REFLECTION_TEST_v0_1.py` `5af23da9…f409`; note v0.1.1 `fa0ac88d…918ce2` |
| For full transported models, only the "not conjugate" direction carries over (κ ∉ {0, 2}) | `[THM — SESSION, conditional on lemma step (g)]` | Completeness lemma, modulus note v0.1.1 |
| \|c\| reads m only up to m ↦ 2m* − m. The phase of c is representation-dependent; Im c = 0 is not a normalization principle | `[ALG — SESSION]` | Reflection note v0.1.1 §4 |

**Cross-checks.**
- Independent OFN computations: the all-κ 32×32 minor, the closed form of c, Stab(f₃), and the reflection audit at κ ∈ {1, 1/2, 3}.
- The universal-κ P4 statement rests on FMS's symbolic computation and has not been independently audited.

## 3. Open items handed out of the pilot

| Item | Proposed owner | Status | Dependency / scope note |
|---|---|---|---|
| **FMS-BASIN-01** chiral basin boundary | FMS post-pilot | OPEN | Step 1: the phase-dependent invariant separator at 6th order. Its first input is Δ(A−B) ⊃ −4 Im c (AB)^{3/2} sin 3θ; that term does not by itself locate the boundary. Step 2: numerical basin tests. Both stated for **degree-5 truncated members** |
| **FMS-RATE-01** parabolic approach rate \|u_m\|/\|v_m\| ∼ C m^{−1/2} | FMS post-pilot | OPEN | The exponent is class-wide at leading order; C is member- and start-dependent. Use transported-chart modes or subtract the static offset (OFN raw-readout guard) |
| 7 first-order quintic moduli not reached by charts | FMS / relevant owner | OPEN | — |
| Formal jets beyond degree 5 | DYAD–FMS scope decision | OPEN | — |
| κ ∈ {0, 2} (κ = 2 general conjugacy) | FMS / Genesis | OPEN | — |
| Independent all-κ audit of P4 | FMS | OPEN | Requested in OFN v0.10 N-O10-4 |
| Torus-invariant scalar reading the sign of m − m* | FMS, only if RRF asks | OPEN | — |
| Analytic and C^∞ B-6 / B-∞ existence | DYAD (OPEN 20) | OPEN | Request: `FMS_TO_DYAD_OPEN20_PRIORITY_REQUEST_v0_1.md` |
| Physical additive carrier and ψ selection; class-C model-contract row; readout contract for \|c\| | OFN / RRF | OPEN | OFN v0.10 N-O10-3 |

## 4. Owner sources at closeout

| Source | Identity | Status | Read by |
|---|---|---|---|
| OFN v0.10 | `acb70a8c…5dfa` | Adopted 19 Oct; N-O10-4 received as owner input | Release record read by the Claude co-owner |
| DYAD v6.4.17 | `e07cf2b9…4bfc` | Adopted 19 Oct; OPEN 21 CLOSED, OPEN 20 PARTIAL | Release record read by the Claude co-owner |
| Genesis v2.8.9 | `d143673e…c6fc` | Adopted | As cited in OFN v0.10; not re-hashed by FMS |
| RRF v0.8.3 | as reported | Adopted working standard | Reported |
| FMS Ledger | v0.6.4 SESSION | Next version to add §12F provenance, these source pins and this record | — |

The ChatGPT co-owner did not re-verify these owner files in the closeout round. The table rests on the Claude co-owner's source reading.

## 5. Next actions

1. The PI decides on final closeout.
2. Send the OPEN 20 request to DYAD (after v6.4.17 release verification).
3. FMS Ledger v0.6.5: N-O10-4 receipt, the §12F provenance (reflection note v0.1.1), the source pins of §4, and a pointer to this record.
4. Start BASIN-01 and RATE-01 as post-pilot FMS work items when scheduled.
