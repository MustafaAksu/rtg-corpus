# DYAD — ATLAS P1 Scientific Correction Pass — SESSION v0.1

**Date:** 21 October 2026 · **Owner:** Dyadic DSN (Claude) · **Status:** `[SESSION]` record of the P1 pass. **Not an adoption, not a release, no notice.**
**Authority:** reviewer decision `DISPOSITION ACCEPTED — P1 AUTHORIZED, FA-06 RESONANCE CLARIFICATION REQUIRED` (21 Oct 2026; SHA-256 of the review text `b5ebab75…5796`), on disposition v0.1 (`7b2d1573e6e5f139e2cab23451b7e06ea319f87dcdae2fad4ad3a7a9ef87465c`). The reviewer did not require a new disposition version.
**Base:** adopted DYAD v6.4.19, SHA-256 `40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9`, unchanged. v6.4.19 stays the adopted owner file.
**Output:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_20_P1_WORKING.md` (`6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905`), a noncanonical working file built deterministically from the base. P2 continues on this lineage; the v6.4.20 draft comes after P2.

---

## 1. Evidence-level update for disposition v0.1

The reviewer reran the disposition package. From this record on:

| Item | Level |
|---|---|
| Disposition SHA256SUMS 7/7; math checks E1–E10; record gate D1–D9; controls C1–C3 and K1–K4 (exit 1 each); math JSON byte-identical; v6.4.19 hash | `REVIEWER-REPLAYED` (same scripts, not an independent second implementation) |
| E4–E6 finite-p computations | Finite samples; no all-p theorem |
| v6.4.19 combined G14–G15 run; separate-process M1–M4 | `REVIEWER FULL REPLAY NOT COMPLETED` (unchanged) |

Everything new in this P1 package is `OWNER-RUN` only.

---

## 2. Checkpoints (reviewer's P1 table)

| Checkpoint | Acceptance criterion | P1 result | Where |
|---|---|---|---|
| FA-01–03 | R9 import, live statuses, centralizer hypotheses correct | Done. §7 split into a self-contained foundation and an R9-dependent layer with claim-level import rows (R9 on track C_z, rows not mixed; reciprocal amplitude). 20 superseded passages relocated verbatim to Appendix A (H-1 … H-10); §2 frontier rebuilt from live items; rendering fix after OPEN 20. §5 centralizer row restored to Cent_{formal, DG(0)=I}; five rows rewritten as "not implied by this result alone; see [RID]"; SG-16 violation clause rewritten | E04–E09, E13, E17–E21 |
| FA-04 | VANISH-B2 source certificate inspected | Done (§3.1) | E14a–b |
| FA-05 | Field labels fixed, coefficients kept | Done: ℚ(i√3) twice, ℚ(ζ₅) once; values byte-unchanged (gate G6). §1 L71 (archival h₄ "over ℚ(√3)") not changed: those values were not available for checking | E10a–c |
| FA-06 | Linear order separated from polynomial resonance | Done (§3.2) | E11a–b |
| FA-07 | General-p frame rule proved or kept `[NUM]` | **Proved** (§3.3), `[ALG]`, proposed RID DYAD-ALG-KP-FRAME-SCALE | E09h, E12a–c |
| FA-08 | Historical source found, or reconstruction kept as candidate | **Historical source found** (§3.4) | E02 |
| FB-13 | Smooth chart corollary examined separately | Done; proposed RID DYAD-THM-SMOOTH-EQUIVARIANT-CHART, `[THM]` corollary | E09h, E16 |
| FC-32 | Separate SESSION result; no owner adoption | `DYAD_FC32_HNG_R9FREE_SESSION_v0_1.md`; no DSN text | — |

Also in P1 (scientific Tier B): FB-12 leading decay versus historical ansatz (κ → κ_bb), FB-15 sign, FB-25 chart value in the §5 c_θ row.
Left for P2: FB-10 (result-level RIDs), FB-16/17/18 (pins, receipts, notice states), FB-22–24, 26–30 (editorial).

---

## 3. Scientific findings

### 3.1 FA-04 — VANISH certificates

- **Registry gap.** The registry names `degree_b_vanishing_cert_v2.py` (DYAD-ART-VANISH-CERT). It is not in the project. Available: `degree_b_vanishing_cert.py` (`c9a369e6…0dc6`) and `rtg_betagraded_vanishing.py` (DYAD-ART-VANISH-BGRADED, `dec08174…d774`).
- **Owner reruns, 21 Oct 2026:** both exit 0.
- **Bound used.** Both engines compute the jet of the n-fold map by full composition g_{n+1} = F∘g_n, including all lower-degree parts. Every cross term of degree a+b−1 is therefore enumerated. Neither uses the withdrawn "degree ≥ 4" argument. The DSN explanation was wrong; the certificates were not.
- **β-sets.** The β-graded engine gives {−2}, {−3,−2,0}, {−4,−3,−2,−1,0,2} for b = 2, 3, 4, as printed in the DSN. The denominators of the source coefficients are products of Φ₁, Φ₂, Φ₃, Φ₄ only, so they are nonzero at primitive p-th roots for p ≥ 5.
- **Weakness found in the older certificate.** Route A of `degree_b_vanishing_cert.py` conjugates λ but not the coefficient symbols, i.e. it treats them as real. Under that simplification the β = −2 coefficient of the (0,3) source cancels and the script prints {−3,0}. The vanishing range is the same. The β-graded engine, which conjugates coefficients separately, is the authoritative source for the printed β-sets.
- **Grades unchanged.** Recorded in the §6.11 audit note and SG-16.

### 3.2 FA-06 — order of λ versus homological resonance

As the reviewer noted, λ^j ≠ 1 (1 ≤ j < 6) says nothing about the absence of resonance in the normal form: λ²λ̄ = λ, and z²z̄ is the adopted resonant cubic.

The replacement text in §6.6:
- `[ALG]` linear order exactly six (any primitive root; not a uniqueness property);
- `[ALG]` resonance iff a−b−1 ≡ 0 (mod 6). Resonant monomials occur at every odd degree and no even degree: (2,1); (3,2), (0,5); (4,3), (1,6), (7,0); …
- `[ALG]` non-resonant divisors λ(1 − λ^{a−b−1}) have modulus 1, √3 or 2, so there are no small divisors at any degree (P1-3);
- `[DEF]` sub-/super-resonant classification;
- `[ALG]` cubic radial rate Re μ_p^Z = −p sin²(π/p) for p ≥ 5 only, frame named;
- `[OPEN]` harmonic count needs a cutoff.

The sentence "No intermediate resonance obstruction occurs" is withdrawn as a `[COR]` and relocated (H-7).

### 3.3 FA-07 — the frame rule, proved

- **Frames.**
  - Z: η = Z + Z̄, ρ = uZ + ūZ̄, u = 1/(1−λ). This is the RECOG frame and also the frame of the OPEN 9 engine.
  - W_p = ρ + ((λ−1)/K_p)η, with K_p = |1−λ|².
- **Proof.**
  - Since (λ−1)/K_p = −1/(1−λ̄) = −ū, the frame W_p equals (u − ū)Z.
  - With θ = 2π/p, u = ½ + (i/2)cot(θ/2). Hence W_p = i cot(π/p)·Z.
  - Under w = sz, the coefficient of z^a z̄^b scales by s^{1−a} s̄^{−b}; for z²z̄ the factor is |s|^{−2}. The archived OPEN 9 table v2 §0.4 states the same law.
  - Scaling a normalizer with zero resonant coefficients keeps them zero.
  - Therefore ν₃^Z = cot²(π/p)·ν₃^{W_p} and μ_p^Z = cot²(π/p)·μ_p^{W_p}. Arguments are frame-independent.
- **Evidence:**
  - P1-1, exact symbolic: ū + c = 0; s = i cot(θ/2); the scaling of the cubic coefficient.
  - Disposition E5, `[NUM]` agreement for p = 5…50.
- **DSN.** The rule is registered as `[ALG]` under the proposed RID DYAD-ALG-KP-FRAME-SCALE, next to the bridge lemma. It comes with the interface rule "an exported μ_p or ν₃ names its frame". The L671 typo is fixed.

### 3.4 FA-08 — DYAD-THM-RAW-CUBIC recovered

- **Source.** `OPEN9_full_onestep_normalization_table_v2.md` §4 (companion to DSN v5.4.x; SHA-256 `af90dc13f2d439e74988082dc815264574ed158f9865ddcdeba7509b191a700e`), found in the archived outputs.
- **Statement.** In the raw Z_p eigenframe of the K_p family, the z²z̄ coefficient of the **raw one-step map** (before any normalizer) is

  ν_{3,raw}^{(p)} = K_p/4 + i·(2cos²(2π/p) − 2cos(2π/p) + 1)/(4 sin(2π/p)).

- **Owner re-derivation (P1-2).**
  - A one-step coefficient involves no composition. It is read off the cubic Taylor terms η³/6 (ρ-row) and K_p(ρ³ + η³)/6 (η-row).
  - Agreement with the formula: 10⁻¹⁶¹ at 50 digits for p = 5…60.
  - p = 7 gives 0.18826 + 0.16963i, as in the source.
- **DSN.** The statement is written at the RID's only occurrence (§2 OPEN 9), with source and scope. The grade stays `[THM]` as registered. Whether to retag it `[ALG]` (the proof is an exact identity) is left to the P2 grade lookup (FB-24).
- **Not identified.** The result is not identified with RECOG's normalized ν₃, with μ, or with the raw p-step map.
- **The disposition's p-step candidate.** The raw p-step cubic equals pλ̄ times the resonant one-step normal-form cubic, for p ≥ 4. This is a **different statement**. It is kept as a separate owner observation (P1-5, `[NUM]`; proof sketch in disposition FA-08), with no RID. AZ cited the RID for "the raw cubic coefficient of the p-step map is exact"; that reading does not match the recovered source, so N17 will tell AZ.

### 3.5 FB-13 — smooth equivariant chart

- **Statement.** Φ = ⅙Σ_{k=0}^{5} A^{−k}J^k, with J from E4.
- **Proof.**
  - DΦ(0) = I.
  - ΦJ = AΦ, because J⁶ = id and A⁶ = I.
  - Φ T Φ⁻¹ commutes with A, because JT = TJ.
- **Checks.**
  - The reviewer checked the argument.
  - P1-4 checks the averaging identity on a formal example to degree 3.
- **Registration.** Proposed `[THM]` corollary, RID DYAD-THM-SMOOTH-EQUIVARIANT-CHART, placed in §6.17 after the E1–E4 distinctions.
- **Scope.**
  - The radius is qualitative.
  - Φ inherits no finite-chart bound.
  - No analyticity is claimed.
- **Interface.** Φ meets the Genesis §6.3c C2 hypothesis. Whether Genesis or OFN uses it is their decision.

### 3.6 FB-12, FB-15, FB-25

- **FB-12.** §6.5 now opens with the certified leading decay, imported from RECOG-THM-A1A-RECIPROCAL-AMPLITUDE: Q_m = 1/(m + Q₀⁻¹) + O(m^{−3/2}) on U. The former `[ALG]` "backbone law" becomes a `[DEF]` historical ansatz with fit parameters κ_bb and C_bb.
- **FB-15.** −13 + 15√3/2 ≈ −0.0096, with DZT's norm ¼ cited at DZT's scope.
- **FB-25.** The c_θ row now carries the chart value +89√3/324 and the warning "not a phase-moment or chart input".

---

## 4. What P1 does not change

- **RIDs.** All 136 RIDs of v6.4.19 are present (gate G1). The only new RIDs are the two proposed ones; they are registered only at a future adoption.
- **Constants.** Key constants are never reduced in count (G2). Protected blocks are byte-identical to v6.4.19: §6.1–6.4 (except the FA-05 label line in §6.2), §6.7, §6.8, §6.10, §6.12, §6.13, §6.16 and the L-PHASE theorem (G12).
- **Grades.** No registered grade changes. The only retags are the two §6.6 statements without RIDs: [THM] → [ALG] and [DEF].
- **OPEN statuses.** OPEN 20 PARTIAL (B-an, B-6 OPEN); OPEN 3, 19 and 21 CLOSED at their scopes.
- **Metadata.** The header, adoption metadata, footer, §7 notice table and §8 registry are not updated. They belong to P2 and the draft.

---

## 5. Artifacts (OWNER-RUN)

| File | SHA-256 | Role |
|---|---|---|
| `RTG_DYADIC_OSCILLATOR_DSN_v6_4_20_P1_WORKING.md` | `6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905` | Working file (1765 lines) |
| `build_dyad_p1.py` | `210ac2b34e52f243777d6dbf17e9880f260be17bd3a25591958bef7df3a1e70c` | Deterministic builder: 48 anchored edits, 20 verbatim relocations |
| `p1_edit_log.json` | `3bb82cff6afcf31e3f0eefb9efed965acb9d95fe4d6e08cc395acaa091d3853f` | Edit and relocation log |
| `p1.diff` | `7b91008a0c4fb6562b89fbb4fbb3054dd0ef5c6854098098c23ad340a063c59c` | v6.4.19 → P1 working diff |
| `check_dyad_p1.py` | `c4b37bb8281dc94c6e4cbcfdabd0deb54ecba8ed1b6a37a8fa2b5b8bcb2d7bf1` | Gates G0–G13; controls N1–N8 |
| `check_dyad_p1.json` | `6635aa7beb4231982f56dd569af646ba3cc35f12fdfe3e2bc5116cde173308c7` | 14/14 PASS |
| `dyad_p1_math_checks.py` / `.json` | `cde64935d1caab672eb283a9cdf660bc8b06e99053c97b3a847d4d2184becfed` / `2db893cfa321794fc8eb67bd4537919b4d67da4053b765c075460800c022ff5e` | P1-1…P1-5, 5/5 PASS; controls K1–K3; JSON byte-deterministic |
| `p1_controls_exit_codes.json` | `94670371f2bcbb09455b6d79e24556a2f0fcde613c3ea852a06ff78db3ce999d` | N1–N8 and K1–K3 exit 1 each; main gate exit 0 |
| `vanish/degree_b_vanishing_cert.py`, `vanish/rtg_betagraded_vanishing.py` + run logs | `c9a369e6…0dc6`, `dec08174…d774`; logs `1efdfadc…69c8`, `32843fd0…898a` | Archived certificates, owner rerun (FA-04) |
| `DYAD_FC32_HNG_R9FREE_SESSION_v0_1.md` | `463866188ce769835419663387c8ad0bf4601a43bf6c13cb2a86ba6b52228958` | FC-32 SESSION result |

**Replay.** Run these commands next to the adopted v6.4.19 saved as `base_v6_4_19.md`:
- `python -B build_dyad_p1.py base_v6_4_19.md out.md` (byte-identical output);
- `python -B dyad_p1_math_checks.py` (about 20 s);
- `python -B check_dyad_p1.py --base base_v6_4_19.md --working RTG_DYADIC_OSCILLATOR_DSN_v6_4_20_P1_WORKING.md --build build_dyad_p1.py --math dyad_p1_math_checks.json`;
- add `--control N1` … `N8`; each must exit 1.

---

## 6. Next

1. Review of P1.
2. P2 interface and editorial pass on the P1 working file, with an old→new section map: FB-10, 14, 16–24, 26–30.
3. v6.4.20 DRAFT r1 → external review → explicit PI adoption → release checker.
4. Notices N16–N20 after release.

**Open after P1:**
- the general-p frame rule needs reviewer acceptance before its RID is registered;
- the RAW-CUBIC grade question (P2);
- the missing `degree_b_vanishing_cert_v2.py`;
- FC-31 (deferred);
- FB-11 (deferred).
