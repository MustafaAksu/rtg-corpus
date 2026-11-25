# DYAD OPEN 3 — P3 review disposition and provenance addendum (v0.1)

**Date:** 19 October 2026 · **Author:** Claude (Dyadic DSN owner/editor) · **Status:** `[SESSION]` owner disposition of the external review "P3 SCIENTIFIC REVIEW ACCEPTED — OWNER ADOPTION PENDING".

No owner file is modified. DYAD v6.4.13 is unchanged. Adoption is a PI decision on a successor text.

## 1. Review receipt

The reviewer replayed the certificate independently. All of the following passed or matched:

| Item | Result |
|---|---|
| P3 proof record `af4a6123…2a54` | PASS |
| `dyad_open3_p3_remainder_cert.py` `b7df79b0…d258d` | PASS |
| `dyad_return_qchi_exact.py` `e45286fa…50f6` | PASS |
| main run | exit 0 |
| output JSON `bd533725…ddfcde` | byte-identical |
| `neg_K` / `neg_h2` / `neg_mu` | exit 1 each |

The reviewer found no mathematical error in:
- Lemma 2 (the A₁/A₂/B/C split, the 1/|w| second-derivative behaviour, the Log branch);
- Lemma 3 (D_Q of degrees 3–12, with Q_prim ≠ q kept separate);
- the monotonicity argument, together with its scope note: it places the supremum *of the majorant* at s = r, not the supremum of the true error.

Recorded caveat: the replay re-executes the same code. It is not an independent second certificate.

## 2. Owner position on the reviewer's recommendations

| Recommendation | Owner position |
|---|---|
| T-OPEN3 → `[THM]`, P2 identities → `[ALG]` in the next DYAD revision | **Agree**; propose for v6.4.14 |
| Per-block chart-remainder subproblem → CLOSED | **Agree** |
| General OPEN 3 → **PARTIAL** rather than CLOSED, so that P4 and P0 stay visible | **Agree.** This replaces the proposal in P3 record §5 ("OPEN 3 CLOSED at per-block chart scope") |
| Next priority P4 (asymptotic-phase transfer) | **Agree** |

Proposed OPEN 3 line for a successor, as wording only (not applied):

> OPEN 3 — PARTIAL. Per-block chart-level spiral residual CLOSED: exact leading terms (`DYAD-ALG-OPEN3-LEADING`) and certified remainders |S_Θ − L_Θ| ≤ K_Θq², |S_Q − [S_Q]₅| ≤ K_Qq³ on the NF-REM rows 1/20 and 1/40 (`DYAD-THM-OPEN3-SPIRAL-REM`). OPEN: asymptotic-phase transfer to primitive variables (P4). BLOCKED: comparison with the historical `spiral_phase_fit.py` (P0; artifact unavailable). The fit is not a definition of the residual.

The RIDs above are proposals.

## 3. Provenance addendum: comparison of h with an archived reconstruction

The adopted `certificate.json` (P2B v2, `jets.h_degree6`) is still unavailable. One earlier artifact *was* found in the uploaded files: `DYAD_RETURN_ENCLOSURE_P0_P1_evidence.zip` (SHA-256 `433805bf…8d81`, dated 19 Sep 2026). It contains `outputs/coordinate_h_deg6_reconstructed.json` (SHA-256 `bb09bace…99f6`). That file's meta record marks it as an "independent exact reconstruction in this audit", **not** the historical owner artifact.

| Comparison | Result |
|---|---|
| keys (monomials) | 23 = 23 |
| exact coefficient equality over ℚ(i√3) | **23/23 equal, 0 mismatches** |

**Reading:**
- The h regenerated in P3 agrees exactly with an independent reconstruction made a month earlier by a different audit. That reconstruction is consistent with the conventions of the P0 convention contract (W the primitive linear eigenframe).
- This strengthens the provenance of the P3 inputs. It does **not** replace the byte-level comparison with the adopted P2B v2 `certificate.json`, which stays an open provenance item.
- J was checked through μ, the two chart-law identities and its monomial support (P3 record §2). The archive's `jet1_deg6_reconstructed.json` is a one-step jet in a different (archival) object, so it is not compared (SG-19).

## 4. Status after this disposition

- P1, P2 and P3 are externally accepted. Owner adoption is pending a PI decision on a v6.4.14 successor.
- OPEN 3: OPEN in v6.4.13. The proposed successor status is PARTIAL (§2).
- P4 is the next scientific item. P0 is BLOCKED.
- Provenance item: compare h and J with the adopted P2B v2 `certificate.json` when it becomes available.
- OPEN 20: PARTIAL, unchanged.
