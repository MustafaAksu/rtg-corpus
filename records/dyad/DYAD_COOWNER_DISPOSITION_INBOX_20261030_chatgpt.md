# DYAD inbox D1–D6 — independent co-owner disposition (ChatGPT)

**Date:** 30 October 2026
**Author:** ChatGPT, Dyadic co-owner
**Status:** SESSION / independent co-owner decision proposal, **not** a joint owner disposition, not an adopted DSN or permission to release.
**Baseline:** DYAD v6.4.22, annotated tag `dyad-v6.4.22` (tag object `2c50b7a2946b48a4f4ca21f3f051366c312a077f`, commit `7130978f43b417d335622d2072abe9e571b4e142`, SHA-256 recorded in the release/tag: `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29`); Methodology v1.4; Programme v1.3.
**Advisory snapshot:** PR #125, `claude/atlas-advisory-dyad-inbox`, commit `80f1c7e678cc275ab7de0d1639889d7489f4c315`, **unmerged** at the time of this review.
**Scope:** Six open items in `pipes/DYAD/` (D1–D6). OPEN 20, any scientific upgrade outside these six items, canonical edits, releases, tags and pipe state changes are excluded.

## 1. Independent dispositions

| Item | Verdict | Required outcome and acceptance test |
|---|---|---|
| **D1** NUMGEN q-star | **ACCEPT WITH CHANGE** | Answer **NO** to numerical identity; distinguish `q_star^DYAD` and `q_star^NUMGEN`. Do not define the former as a *first safe-funnel entry* on current evidence. Before revising `DYAD-THM-OPEN18`, owner must define precisely which step wins (first/last; angular-only versus angular+Q), domain and tie convention, and separately substantiate branch legality/root isolation. |
| **D2** RECOG C7 registration | **ACCEPT** (scoped registration) | Register independent, RID-addressable row-specific ceilings `C7 <= 85.1` on `|z|<=1/20`, `C7 <= 27.7` on `|z|<=1/40` for the *same adopted NF chart and vector norm*. Retain `100/30` as existing theorem constants and proof inputs; do not silently sharpen derivative constants or consumers. |
| **D3** RECOG (D5) bridge | **ACCEPT WITH CHANGE** | State the exact row-A remainder decomposition and the two chart bounds under a new RID or explicitly labelled sub-RID, with `c_Q <= 0.79246` and **`c'_Q <= 0.36916`**, not 0.36915. Add point-of-use `[COR]` to the proof outline. Keep `403/250` unchanged (see independent conservative check below); require RECOG's receiver-side recheck before it drops `[assuming:]`. |
| **D4** NUMGEN v1.21 notice | **ACCEPT** | Register NUMGEN's adopted use of `DYAD-THM-LPHASE-ROWA-REMAINDER` at pin `dyad-v6.4.22`; record the `DYAD-ALG-P5-RADIAL` owner-name equality, preserve the NUMGEN scope and pre-existing pin semantics. |
| **D5** RECOG v0.3.26 notice | **ACCEPT** | Bring current consumer inventory to `recog-v0.3.26`; retain each actual claim-level historical pin and `[assuming:]` boundary. Optional OPEN 21 numerical-constant replacement is a **DEFERRED separate scientific revision**, not automatic receipt bookkeeping. |
| **D6** OFN v0.11 notice | **ACCEPT** | Register OFN's adopted use of two smooth owner theorems and its map custody import at `dyad-v6.4.22`; distinguish N4 used, N6 received without an OFN import, N14 used. Include Genesis v2.9's scoped smooth-theorem import without bulk repinning its older v6.4.13 imports. |

These are independent co-owner positions. The Dyadic owner must separately disposition all six items; the joint list reconciles disagreements and only then defines the v6.4.23 candidate scope. No pipe status was edited by this review.

## 2. D1 — what the recovered source does and does not decide

**[OWNER: DYAD v6.4.22 §§6.4, 6.8 / DYAD-THM-OPEN18, DYAD-ALG-QC-CRITICAL-AMPLITUDE]**
The adopted record states monotonicity of `Q` and `Theta` on `Gamma_3` and `Gamma_4`, with a split at `q_*`, and the safe funnel
`S_ISP = {Q < Q_c, Theta in [-2*pi/3, -pi/3]}`,
`Q_c=(asin(log 2))^2≈0.58652039411886457`.
It does **not** define the first-footprint selection operator, the branch membership predicate or the root-isolation proof.

**[SESSION: EV-SRC-READ / EV-CODE]** The PI-supplied source `upload/dyad-sources/rtg-engine/open18_arb_cert3.cpp` (identified by its internal first line as `open18_arb_cert_final.cpp`), available on PR #125, checks `dQ_n/dq>0`, the sign of the angular derivative numerator and positivity of its denominator. Its macro runs are `Gamma_3, n=3, q in [0.001,1.26021320256]` and `Gamma_4, n=4, q in [1.26021520256,2]`. It explicitly delegates **branch legality and q-star root isolation to independent footprint audits**, not recovered. Its printed `[THM-READY]` and process exit cannot by themselves discharge those delegated obligations; the program returns 0 unconditionally at the end. Atlas reported successful reruns; this co-owner **did not rerun the C++ source**.

**[SESSION: independent high-precision map evaluation]** For the canonical lifted family `(rho_0,eta_0)=(0,q)`, solving `rho_4(q)=0` inside the certificate gap gives
`q_star^DYAD = 1.2602142025634771148724385609565043943923…`.
At that root `Theta_4=-pi/3` on the relevant negative-eta branch. NUMGEN's adopted v1.21 §6.6 uses `q_star^NUMGEN = 0.315625883659561602974267621967906111219946754…` as a high-precision **NUM** candidate for `eta_6(q)-q=0`, not as a Dyadic branch split. Thus the values and defining equations differ; **NO** is the correct answer to D1. The Dyadic number computed here is an unvalidated high-precision root within the supplied gap, **not** a newly certified global uniqueness or branch-legality theorem.

**Counterexample to a tempting definition.** At `q=1.30` the primitive map gives:
- step 3: `Q_3≈0.5507847507<Q_c`, `Theta_3≈-2.042783025` (inside `[-2pi/3,-pi/3]`);
- step 4: `Q_4≈0.3264859505<Q_c`, `Theta_4≈-1.089300939` (also inside).
Both qualify as *safe-funnel* steps. If "first footprint" means **earliest** qualifying iterate, it is step 3 at `q=1.30`, although that `q` is assigned to the certificate's `Gamma_4` region. Further, `Q_3=Q_c` occurs numerically at `q≈1.34159703`, `Theta_3=-2pi/3` at `q≈1.36713045`, and `Q_4=Q_c` at `q≈1.97865695`. In particular `Gamma_4` sweeps to `q=2` and cannot be a branch claiming `Q_4<Q_c` throughout. An **angular-window-only last eligible step** could explain the observed switch, but is **only a proposed new explicit definition until the owner confirms it**. Do not claim it is the lost audit's definition.

**D1 acceptance criteria for v6.4.23:** explicitly define `Gamma_n`, step priority and clock, angular/wrapped convention, `Q_c` requirement if any, endpoint convention, and `q_star^DYAD` as the certified root of a stated equation (or downgrade the precision/grade). Record any replaced "first footprint" reading as a scoped correction rather than retroactively rewriting certificate scope. Leave numerical root uniqueness / interval coverage unclaimed unless verified. Send NUMGEN the negative identity answer; its NC-17 may close as a disambiguation, not a common-root theorem.

## 3. D2 — row-specific NF remainder ceilings

**[OWNER: DYAD v6.4.22 §6.14 / DYAD-THM-NF-REM]** The live theorem retains `C7=100` on `|z|<=1/20` and `C7=30` on `|z|<=1/40`, with `|Fhat-J|<=C7|z|^7`. Neither chart nor derivative constants are free to change.

**[SESSION: inspected Atlas rerun receipt and logs, not independently rerun]** PR #125's P2-B v2 package is identified by SHA-256 `e4e2bab004d4e39b76920e486607acc34749037ae2638809a9c2117d548fdbe4`; Atlas reports a 7/7 replay with byte-identical certificate. The captured `certify.log` displays `85.07319334710797` and `27.602220983621145`; the printed 85.07 / 27.60 are not outward bounds. Values 85.1 and 27.7 are outward ceilings at the identical rows. The source package and `certificate.json` were not independently extracted/re-executed here. The owner's v6.4.23 certificate check should confirm the rational inequalities and quote the exact source path, gate and execution pin.

**Recommendation:** use a **new RID** for the strengthened C7 ceilings rather than a silent replacement inside `DYAD-THM-NF-REM`; cross-reference it adjacent to the existing theorem. `100/30`, `1000/250`, L-PHASE's `c_7=157.58`, OPEN 3 and existing RECOG unconditional results remain unchanged. RECOG alone decides any successor statement making `RECOG-THM-R9-SHARPENED-ROWS-C7` unconditional.

## 4. D3 — row-A bridge, corrected majorant, unchanged main theorem

**[OWNER: DYAD v6.4.22 §6.14 / DYAD-THM-LPHASE-ROWA-REMAINDER, DYAD-ALG-OPEN3-LEADING]**
Use chart `W=h(z,bar z)`, `q=|z|^2`, row A `|z|<=1/20`; the theorem is applied to block base points in `U={0<Q<=1/625}`, whereas branch control holds on `U_T`. The exact identity under the branch hypothesis is
`r=Lambda_3(z)+(S_Theta-L_Theta)+tau(D_Q-D_3)+(Arg(J/z)+tau*q)+Arg(Fhat/J)`,
with `Lambda_3=L_Theta+tau*D_3`. It is not a universal identity for arbitrary observables/charts.

**[SESSION: EV-SRC-READ / EV-SRC-REPORTED]** The hash-checked L-PHASE package supplied through the NUMGEN review ZIP is reported by Atlas to regenerate the byte-identical certificate (10 gates, 6 negative controls). Its accessible output has `c_Q=0.7924576152330335...` and `c'_Q=0.3691523046606689...`. Therefore `0.79246` is an outward ceiling and `0.36915` **is not an outward ceiling of the certificate's majorant**. This does *not* prove the underlying true supremum exceeds 0.36915. Register `c'_Q<=0.36916` and add a `[COR]` at DYAD §6.14's existing `c'_Q=0.36915` proof line, preserving the originally adopted text in the previous tag.

**[SESSION: EV-INDEP / exact rational safety check]** The correction **does not require changing** `403/250=1.612`. Using only published rounded-up quantities, a conservative independent majorant is
```text
cQ = 79246/100000;  cQprime = 36916/100000;  tau <= 7/6
R = 1401/1000 + (123/125 + (7/6)*cQprime + 50220/100000)/20 + (15758/100)/8000
  = 9099251/6000000 = 1.5165418333...
B = 106253/100000 = 1.06253
B^2 * (1-cQ/20)^3 > 1   [exact rational comparison]
R * B < 403/250          [margin = 377283497/600000000000 > 0]
```
Thus, provided the component estimates and chart/domain hypotheses of the adopted proof are retained, the public ceiling `403/250` follows even with `c'_Q=0.36916`, independently of using the original FIN gate's exact majorant. No optimality or improved theorem constant is claimed.

**D3 acceptance criteria:** register the exact decomposition as an `ALG` statement and the two row-A inequalities as certified `THM` under explicit domain/representation and a new RID; identify proof gates and raw inputs; correct the decimal; keep the old `403/250` and branch contract. RECOG must **rerun/review** dependent uses of `c'_Q=0.36915` (including its `recog_a1c_tail_averaging_cert.py` input) before removing `[assuming: (D5)]`; the numeric difference is small but not an automatic receiver acceptance.

## 5. D4–D6 — owner-consumer synchronization, not theorem re-proof

- **D4 [ACCEPT].** [OWNER: NUMGEN v1.21 §6.6, §9.1] `DYAD-THM-LPHASE-ROWA-REMAINDER` is now an adopted consumer import, sourced from DYAD v6.4.22 at the I1–I5 matching scope. `DYAD-ALG-P5-RADIAL` names the producer's `P_5`; NUMGEN's statement of identity `Delta Q_5=P_5` is NUMGEN-owned. Update DYAD §7.0 and §7 consumer list; do not silently assert an inclusion between different tube domains.
- **D5 [ACCEPT].** [OWNER: RECOG v0.3.26 §§6.13a–b, §6.16e, §7] New R9 sharpened rows, A1c outputs and Appendix B retractions are RECOG-owned; Dyadic may list their receipt and actual imports, without adopting their proofs. Its conditional C7 and (D5) uses remain conditional until D2/D3 are **adopted by DYAD and accepted by RECOG**. The optional OPEN 21 C2/K improvement is deferred to a separate scoped scientific recomputation and review, rather than silently included in a maintenance synchronization.
- **D6 [ACCEPT].** [OWNER: OFN v0.11 §5.5.4, §11] OFN uses `DYAD-THM-SMOOTH-EMBEDDING` and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` at `dyad-v6.4.22` and imports `DYAD-DEF-PRIMITIVE-MAP`. Preserve E2 uniqueness only for zero-linear-part generators, qualitative radius, no analyticity and SG-19. Separate N4 **adopted use**, N6 **received / not imported** and N14 **adopted use**. [OWNER: Genesis v2.9 §7] Also synchronize Genesis's separate v6.4.22 smooth-theorem import for §6.3c C2; its other citations remain intentionally pinned to v6.4.13. Programme v1.3 and Methodology v1.4 are current reference editions.

For all three, **prepared / sent / received / statement accepted / adopted use are separate states**. Updating a consumer table does not send a notice or change the receiver's adopted text. No old pin is marked wrong merely because a newer owner edition exists.

## 6. Source-reading extent, provenance and boundaries

- **FULL:** `CONVENTIONS.md` on `main`; `records/dyad/DYAD_OWNER_ENTRY_NOTE_INBOX_20261030.md` at PR #125 commit; the six `pipes/DYAD/` items and index; `open18_arb_cert3.cpp` from the PR #125 upload; `evidence/atlas/dyad_inbox_20261030/qstar_dyad_split.py` and its output.
- **TARGETED:** `records/dyad/ATLAS_ADVISORY_DYAD_INBOX_20261030.md` §§0–5; `DYAD_UPLOAD_HASH_CHECK_20261030.md` §§1–5; DYAD v6.4.22 §§6.4,6.8,6.14,7–8; NUMGEN v1.21 §6.6/§9; RECOG v0.3.26 §§6.13a–b,6.16e,7; OFN v0.11 §§5.5.4,11; Genesis v2.9 §7; Programme v1.3 header; Methodology v1.4 §§12–13.
- **ARTIFACT LOGS inspected:** PR #125 `cert_runs/open18_arb_cert3.out.txt`, `p2b_v2_rerun/certify.log`, `lphase_rowA_rerun/run_output.txt`; their prior computations are **Atlas-reported EV-RUN**, not this co-owner's EV-RUN.
- **THIS REVIEW'S INDEPENDENT COMPUTATIONS:** mpmath primitive-map iteration/root finding (D1), exact `fractions.Fraction` upper-bound inequalities (D3). These are not new all-order Arb certificates or independent proof of lost branch-legality audits.
- **Not inspected/executed:** original unrecovered footprint audits; direct binary ZIP extraction/hash measurement of the P2-B v2 package or original L-PHASE source files; independent full computational reruns; original arbitrary-precision C++ certification; validation of the downstream RECOG A1c certificate with corrected D5 data.

## 7. Proposed reconciliation and release gate

1. Owner writes a **separate** D1–D6 disposition on `claude/*`; keep this co-owner record independent. Do not overwrite either record while reconciling.
2. Produce one joint item-by-item list. Resolve D1's definition, branch legality, certificate gap, and numerical precision before draft wording; D2/D3 registration RIDs and exact certificate gates before proof-grade promotion; carry D3's point-of-use correction; update §7 consumer rows including Genesis v2.9.
3. v6.4.23 is a **candidate** only after these scoped obligations and change-focused review. Optional OPEN 21 sharpening should be separated unless a bounded exact recomputation/review is accepted. The PI alone decides adoption; only then release record, `main` merge and annotated tag `dyad-v6.4.23`.
4. After adoption and tag, update each `pipes/DYAD/` disposition/state, generate/check `pipes/DYAD/INDEX.md`, and send or record consumer-specific replies at the proper level. Do not send notices before the owner statement exists. OPEN 20 and other owner science are unchanged.

**This co-owner record itself changes no canonical file, RID, pipe state, notice, adoption or tag.**
