# Atlas row check — Genesis v2.10 candidate (round 2)

**Date:** 3 November 2026. **By:** Claude, Atlas owner. The Atlas advises and does not decide.
**Status:** NONCANONICAL record. It is not adoption, a merge, a tag, a pipe-state change or a candidate edit.

**Result: PASS SCOPED — no Atlas-row blocker.** Every item of the fixed co-owner list (G1–G8, the pins, R1) is implemented as fixed, at the scope fixed. Two nonblocking typing notes follow (N1, N2).

## 1. Object

| Object | Identity | Check |
|---|---|---|
| Candidate | PR #162 head `262fe58`, `dsn/RTG_GENESIS_GEOMETRY_DSN.md`, SHA-256 `b1666ef03aa150f19771189a42ec362b7332316bc25fb3f26f0df0e39e878c1f` (1,420 lines) | recomputed |
| Base | `gen-v2.9`, `9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac` | recomputed |
| Fixed list | `records/gen/GEN_OWNER_RECONCILIATION_INBOX_20261103.md` (PR #161; ChatGPT acceptance, comment `6602196670`); PI decision of 3 Nov 2026, 14:14 (release record §1) | read |
| Advisory | `records/gen/ATLAS_ADVISORY_GEN_INBOX_20261103.md` (as revised, PR #152) | — |

## 2. Atlas runs

These are `EV-RUN` by the Atlas, in a clean worktree at `262fe58` with `python3 -I`:

| Run | Result |
|---|---|
| `build_gen_v2_10.py` on the `gen-v2.9` bytes | 38 edits → `b1666ef0…8c1f`, **byte-identical**; edit log byte-identical |
| `check_gen_v2_10.py` | C0–C15 **16/16 PASS**; live grade drops only `[THM]` −1 (G8) and `[CAND]` −1 (G6/R1) |
| `check_gen_v2_10.py --controls` | NC1–NC11 **11/11 caught**. Each control also fails its content gate (C3, C6, C7, C8, C9, C10, C11 or C13), not only the rebuild gates C1/C2 |
| `gen_inbox_checks.py` (`4b9f0a3c…5415`) on the candidate and on `gen-v2.9` | 6/6 PASS on both; output byte-identical to `evidence/gen/inbox/gen_inbox_checks_output.txt` |

**Independent Atlas check (`EV-INDEP`, own sympy script, not the owner's).** Take the printed §6.5 ΔQ_d⁽⁴⁾ with GEN's conventions: B=[[1,−½],[−½,1]] and ω_ab=a₂b₁−a₁b₂. Then V=½B⁻¹∇_d𝒫₄|_{d=0} gives:
- Q(V_s)=7/1024·Q_s³;
- I(V_s,s)=ω(V_s,s)=−Q_s²/16;
- Q(V_c)=61/34992·Q_c³.

These are the printed seed and birth-symmetry values. So `GEN-ALG-P4-DRIFT-IDENTITY`, applied to the printed polynomial, is consistent with `GEN-ART-G3D-SEED` and `GEN-ALG-BIRTH-SYMMETRY-SEED`.

## 3. Rows

| Row | Fixed content | Candidate | Verdict |
|---|---|---|---|
| G1 | NUMGEN route at its own grade, plus a Genesis `[ALG]` application; source stays `[custody-A]` | §6.4 `[ALG]` application line ("every quadratic F₂ on ℝ⁶, cross-component terms included"; "a new proof … not a recovery"). §7 row `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE` `[RESULT][from: ALG]` matches `numgen-v1.21` L1501. §8 `GEN-ART-G2-CHRONO` stays `[THM]`, `[custody-A]`. §6.4 `[THM]` unchanged | PASS |
| G2 | receipt | NUMGEN pin line added | PASS |
| G3, G4 | companion pin at v0.12; no claim import | §7 companion and IF32 rows at `ofn-v0.12`; OFN11-C01/C02 named as fields Genesis does not use | PASS |
| G5 | ν₅⁽⁵⁾ label, that row repinned | "exact in ℚ(ζ₅) … real and imaginary parts in ℚ(√5, √(10+2√5))", claim pin `dyad-v6.4.23` §6.11 (RID present there); value and `[conv:]` unchanged; the other v6.4.13 rows unchanged | PASS |
| G6 | claim-level repin to v1.7; (a) T-6s/T-6t, (b) T-6u | T-6s and T-6t are `[ALG]` imports at v1.7 §6.15/§6.16. T-6u: an `[ALG]` import line, then the Genesis `[CAND]` reading `GEN-CAND-APEX-T6U` (RID kept); §8 row repinned. CN-01–05 stay "as received at v1.6". The three RIDs are present at `triad-v1.7` | PASS |
| R1 | separate the source mathematics from the proposed use | T-6s: "The imported coherent-family identity is `[ALG]`; its proposed use as an OPEN-M interface remains `[CAND]` and is not a source realization" (NC11) | PASS |
| G7 | answer yes; `[ALG]`; own RID; general cubic term shown; not under `GEN-THM-DELTA-QC` | §6.5 `GEN-ALG-P4-DRIFT-IDENTITY` `[ALG]`. Q_d(d′)−Q_d(d)=2dᵀBG₂,d+[2dᵀBG₃,d+Q_d(G₂,d)]+O(5), then L⁶=I and G₂=0; G₃,d(s,c,0)=½B⁻¹∇_d𝒫₄\|_{d=0}. "Distinct from" `GEN-THM-DELTA-QC`; census custody stated (`GEN-ART-P4-PRIMITIVE`, `[custody-A]`). §8 row added | PASS |
| G8 | `[ALG]` at §6.6, §1, §2; own RID; §8 row keeps its typing | §6.6 `[ALG]` `GEN-ALG-BIRTH-SYMMETRY-SEED` ("exact evaluation"), values unchanged. §1 L80 and §2 cite the RID. §8 `GEN-ART-JQ-PHASEDRIFT` "artifact typing; supports …". Appendix B entry; §8 result row | PASS (N1) |
| Pins | per the fixed list | Dyadic v6.4.22 rows and the other v6.4.13 pins kept. Triadic at v1.7. TDR-G blocked interface at `tdrg-v2.12.14`. OFN v0.12. TRIAD consumer row at its declared state (claim by claim at `gen-v2.9`, radial polynomial held at v2.8.7 pending G7) | PASS (N2) |
| Stage | one content stage; §6.3a–c protected; no OPEN status change | C3 protects §6.3a–c and the K3/6S/D-4 rows; RID set adds exactly the two PI-assigned RIDs; Appendix A v2.10 entry; candidate status, header and footer | PASS |

## 4. Nonblocking notes (no patch requested)

- **N1 (Appendix B typing).** The grade correction is written `**[RETRACTED | RID: GEN-ALG-BIRTH-SYMMETRY-SEED]**`.
  - That RID is the live `[ALG]` claim, assigned in this edition. The retracted object is the earlier unnumbered `[THM]` grade at `gen-v2.9` §6.6 L987.
  - The Methodology v1.4 Appendix B template names the *original* identifier, and asks that a correction to an unnumbered statement use "an administrative correction key and exact old section, not a fabricated historical RID".
  - Genesis has a precedent of the same form: `[RETRACTED | RID: GEN-THM-SOURCED-JUNCTION]`, a clause of a live RID, at `gen-v2.9` L1344. The Atlas checker is not misled: the first `[RID:]` declaration is the live §6.6 line.
  - A tighter form for a later edition: `[RETRACTED]` grade `[THM]` of `gen-v2.9` §6.6 L987 (no RID at the time); replacement `GEN-ALG-BIRTH-SYMMETRY-SEED` `[ALG]`.
- **N2 (two v1.6 labels).** The OPEN 1T record keeps "Source: adopted `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6`" (candidate L260), and SG-12 is headed "Triadic v1.6 current-use guard" (candidate L565).
  - Both describe the CN-05 protocol that v1.6 issued, so they are provenance, consistent with the CN rows "as received at v1.6".
  - The OPEN 1T title and §1 summary are already edition-free. A later edition may align the two labels.

## 5. After adoption

These are for the owners and the Atlas, not conditions of adoption.
- **Publication transform.** The status line, Appendix A heading and footer go from candidate to adopted, so the adopted file hash will differ from `b1666ef0…8c1f`. The release record should name both hashes.
- **Owner follow-ups.**
  - Close the eight `pipes/GEN/` items as receiver.
  - Answer Triadic on G7 and G8 through `pipes/TRIAD/`; the Triadic repin of the radial-polynomial import is Triadic's.
  - Notify TRIAD, OFN, RRF and UVM where their rows changed.
- **Atlas, next refresh.**
  - F30 can be retired once Triadic repins.
  - F31 narrows to the separate T-6u `[CAND]` reading.
  - F13 and GEN.D7 lose the birth-symmetry and 𝒫₄ items (both now carry RIDs).
  - F14 records the independent route to G₂=0 next to the missing `GEN-ART-G2-CHRONO`.
