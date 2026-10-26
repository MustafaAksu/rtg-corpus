# Response to the External Review of RTG_NUMBER_GENESIS_DSN v1.18

**Memo ID:** `NG_EXTERNAL_REVIEW_v118_RESPONSE_v1` · **Date:** 2026-09-19 · **Auditor:** Claude
**Reviewed artifact:** the reviewer audited a **3,058-line** file — the pre-patch draft (`0e9f330d…`), not the frozen 3,062-line `908786bb…`. One finding (I4) is therefore already repaired in the frozen owner. Everything else applies.
**Verdict:** the review is accurate throughout. No ratified label changes. One finding (P2) is **verdict-relevant at the witness level** and is now quantified; it does not disturb the label-level admission. A v1.19 documentation pass and a Discrete-Genesis policy ruling are required.

---

## 1. Findings independently verified

| # | reviewer claim | my check | status |
|---|---|---|---|
| **I1** | NG-8A's "Q and/or relational phase" does not separate `(a,0)` from `(−a,0)` | `Q` and `η` equal, `ρ` differs; `(Q,Θ)` separates | **correct** — observable-identification gap, not a refutation |
| **I2** | N-3C+ projector needs `ord(λ)=p`, not `λ^p=1` | `λ=1` makes the conjugation trivial | **correct** — hypothesis strengthening; certified `p=6` support unaffected |
| **I3** | C2 origin invariance needs a fixed/cofinal comparison domain on branching prefix posets | `(AB)^n` vs `(AAB)^n` branches | **correct** — deterministic-orbit use unaffected; general statement needs the qualifier |
| **I4** | "WD-DOM trivial for unary maps" is a false generalization | already replaced by totality on `R_bd` in the frozen file | **already fixed** (reviewer saw the earlier draft) |
| **I5** | NG-7A unit-defect control must specify a cycle-sensitive edge | pendant edge gives `C·(0,0,0,1)ᵀ = 0`, exact node-potential data | **correct** — follows from completeness; control statement needs the premise |
| **I6a** | C5: `Δ_{m:1}` is bounded in `[0,m)`, not identically zero | line 1345 says "vanishes identically" | **correct** — my own harness C5.1 already asserted `[0,m)`; owner text is wrong |
| **I6b** | primitive slip steps are `6M_k + O(1)`, not `M_k + O(1)` | line 2004 right, line 2013 drops the factor 6 | **correct** — ratio limit unaffected |
| **I6c** | `5.344275761085416e-5` is `Q_33228` (pre-step), endpoint is `Q_33229 = 5.363929537269259e-5` | recomputed at 60 dps: **both values reproduce to all printed digits** | **correct** — needs explicit pre/post reporting |
| **I7** | historical LOGSLIP "remains open" wording survives in the live registry | present | **correct** — must be marked superseded |
| **P1** | SG-NG-18 mislabels the `37/40` ray result as normal-form; a `−5/24·Q^{5/2}` term intervenes | 60-dps ray numerics: coefficient → `−0.2083 = −5/24`, residual `/Q³` → `0.925 = 37/40` | **correct** — Dyadic-owner label defect; NG's use of the primitive law is right |
| **P2** | TDR-G path orientation is listing-dependent at `S=0`, `\|E\|=N/2` | reproduced exactly: `(S, E_listed, E_reversed) = (0, 12, 12)` | **correct and load-bearing** — see §2 |
| **P3** | defect-threshold ratio theorem has no dedicated RID | confirmed | **correct** — assignment needed |
| **5.1** | `T` is injective on the box `\|ρ\|,\|η\| ≤ 1/10` by a derivative bound | `‖DT−A‖_F² ≤ 0.0124 < 1/4`, `σ_min(A) = (√5−1)/2 > 1/2` | **correct** — promotes the N-2-ORD P3 premise from `[NUM]` to `[ALG]` on a shrunken tube; valuable |
| **5.2** | `ℤ_N` completeness holds with a fundamental integral cycle basis | standard spanning-forest argument | **correct** — clean extension of NG-7A's zero-control; no physical-source claim |

## 2. P2 — quantified, and the answer the reviewer could not reach

The reviewer correctly declined to say whether P2 affects the 136 ratified DISC-2 witnesses, lacking the artifacts. With them, the answer is now certified (`disc2_p2_antipodal_exposure_audit_v1.py`, exit 0):

- **40 of 136 ratified witnesses** touch the antipodal-endpoint condition somewhere in `k ∈ {0,1,2,3}`; 216 such events occur inside eventual cycles.
- **Witness records are policy-sensitive:** under a "reverse-at-antipodal" policy 10 witnesses change class; under "inert-at-antipodal" 20 change, some losing PASS.
- **The label set is not:** the ten-label set is identical under v18, reverse, and inert policies.
- **Decisive:** every ratified label has at least one witness that **never** touches the condition (96 such witnesses). Thinnest: `4:3` with 2 unexposed witnesses; `2:1, 3:1, 4:1, 5:1, 7:2, 9:4` have zero exposed witnesses.

**Therefore `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} ⊆ Q_RTG^dyn` is robust to the P2 defect.** The existential admission survives because it never depended on any particular witness. What does *not* survive unqualified is the witness-level provenance: 40 records rest on a node-listing convention rather than a relabeling-covariant rule, and must be annotated `CONVENTION-EXPOSED` in the witness table. This is exactly the situation the witness-relation architecture (`Q^dyn = π_r(W_dyn)`) was designed for — the defect is visible at the fibre level and invisible at the projection.

Two consequences beyond DISC-2. First, the same audit must be run on the 22 DISC-1 witnesses (enumeration is mounted; queued). Second, the defect belongs to the **Discrete Genesis owner**: the printed rule is reproducible but not presentation-covariant at antipodal endpoint difference, and an owner-level policy ruling (or a proved presentation-independent selection) is required before any future campaign. This goes into the governance note as a **v3 item**, alongside the reproduction-contract gap already filed.

## 3. Actions

**v1.19 (documentation, no theorem changes):** I1 fix the NG-8A observable to `(Q, Θ)` with fixed eigenframe; I2 add `ord(λ)=p`; I3 add the cofinal-domain qualifier to C2; I5 add the cycle-sensitive-edge premise to the NG-7A control; I6a/b/c correct the three index statements; I7 mark superseded LOGSLIP wording; P3 assign `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`; 5.1 register the injectivity deduction and promote P3 to `[ALG]` on the shrunken tube; 5.2 register the `ℤ_N` completeness extension; P2 annotate the 40 exposed witnesses and register the exposure audit.

**Governance (Discrete Genesis owner), note v3:** P2 antipodal-endpoint policy; P1 SG-NG-18 relabeling.

**Not changed:** no ratified label, no closed theorem, no DISC verdict at the label level.

## 4. On the review itself

It is the most useful external audit this programme has received: it found a real specification defect (P2) that our own exhaustive owner-equivalence test could not see — because equivalence to v18 certifies implementation agreement, not presentation covariance. That is precisely the distinction the reviewer drew, and it is the right one.
