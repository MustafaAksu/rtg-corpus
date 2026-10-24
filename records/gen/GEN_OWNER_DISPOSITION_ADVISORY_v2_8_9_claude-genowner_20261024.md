# Genesis owner disposition of the v2.8.9 advisory — Claude co-owner session

**Date:** 24 October 2026
**From:** Genesis co-owner session (Claude), "claude-genowner"
**To:** the PI; the atlas owner (reconciler); the other Genesis co-owner session
**Status:** working record. These are owner proposals, not decisions. The PI decides. Nothing in `dsn/` is changed by this record.

## 0. Basis

| Item | Value |
|---|---|
| Governing edition | `gen-v2.8.9`, `dsn/RTG_GENESIS_GEOMETRY_DSN.md`, SHA-256 `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc`. The file on `main` @ `4b1364b` was hash-checked against this value. |
| Working list | `records/gen/ATLAS_ADVISORY_GEN_v2_8_9_RECONCILIATION.md` §3 and §4 |
| Read in full | `GEN_COOWNER_ENTRY_NOTE.md`, `ATLAS_ADVISORY_GEN_v2_8_9.md`, `ATLAS_ADVISORY_GEN_v2_8_9_RECONCILIATION.md` (branch `claude/gen-advisory` @ `386a807`); `CONVENTIONS.md`; Methodology v1.4 §12.3 and §13.6 |
| **Not read directly** | `ATLAS_ADVISORY_GEN_v2_8_9_INDEPENDENT_CHATGPT.md` (PR #38). Its items enter this record only through the reconciliation's G29-Ixx cross-keys. |
| Line numbers | refer to the governing edition at `d143673e…c6fc` |

All line citations in the reconciliation that this record relies on were re-read at the governing edition. These are lines 61, 94, 138, 171, 206, 256, 275, 437, 439, 450, 563, 682, 965, 1004, 1048, 1054, 1060–1074, 1142, 1185 and 1223–1231 (EV-SRC-READ).

## 1. Evidence produced by this session

`[SESSION]` evidence. It was newly written by this session. Per Methodology §12.3 it is an **independent contribution, not a rerun** of any archived Genesis script. None of the archived face-lift, secular or sourced-junction scripts is held (§5).

| File | SHA-256 |
|---|---|
| `evidence/gen/scripts/gen_owner_advisory_checks.py` | `0ba256be3999606e936a0b14f92311600fd5bd3ff041dd3a828d7688dab6bf99` |
| `evidence/gen/advisory/gen_owner_advisory_checks_output.txt` | `ccec23130ab91ebeee1adfc12d20c184da6151a3fb55a062276175108a6c95c3` |
| `evidence/gen/advisory/gen_owner_advisory_checks_negative_controls.txt` | `c263fac5a121ea47cb3f60d2f927f0f1f6e3795c4775c49ff8cadfd7749d0ff0` |

**Command:** `python -I evidence/gen/scripts/gen_owner_advisory_checks.py`
- Python 3.13, sympy 1.14.0.
- Result: **8/8 PASS**, exit 0, about 10 s.

**Negative controls** (each must exit 1):
- NC1, flipped secular cross-term sign → S3 FAIL.
- NC2, minimiser test reversed to τ ≥ κ → S4 FAIL.
- NC3, Π₊ pole placed at −sgn(m)κ → K3 FAIL.
- All three caught.

**Object conventions.**
- Objects are taken verbatim from §6.8: ΔM_f(w) = m·N(w), with N(w) = [[Im w, −Re w], [−Re w, −Im w]].
- They are also taken verbatim from §6.9 9A: L_sc = (τ−g)I − ΔM_f.
- m is a free real parameter of either sign, because B_* is undefined (GA-03).

| Gate | Grade | Content |
|---|---|---|
| K1 | exact | N² = \|w\|²I; (ΔM_f)² = m²\|w\|²I |
| K2 | exact | With signed κ_s = m\|w\|, Π± = ½(I ± N/\|w\|) do not depend on m. ΔM_f Π± = ±κ_s Π±. The 9A inverse holds for both signs of m. v₊ = (μ₁, μ₂ − \|w\|) is the +1 eigenvector of N/\|w\|. |
| K3 | exact | Under the §6.8 κ := \|m\|\|w\|, the Π₊ pole sits at τ − g = sgn(m)·κ. So for m < 0 the 9A "soft branch τ − g − κ → 0" attaches to Π₋. |
| K4 | exact | R^(E)₊ = H₀ᵀΠ₊H₀ and R^(B)₊ = H₀ᵀBΠ₊H₀ do not change under m → −m. |
| S1 | exact | w = 0 ⇒ ΔM_f = 0 ⇒ K₊ = K₋ = τI |
| S2 | exact | Take w = 0, \|d\|² = Δ₃, S ≠ 0. τd + S = 0 has exactly two solutions, d = ∓√Δ₃·S/\|S\|, with τ = ±\|S\|/√Δ₃, when Δ₃ > 0. It has none when Δ₃ = 0. |
| S3 | exact | For E_s(d) = (s/2)dᵀΔM_f d + Sᵀd with multiplier τ: stationarity is (τI − sΔM_f)d = S, and \|d\|²(τ²−κ²)² = σ²(τ² + 2saτ + κ²) with a = rᵀΔM_f r. s = +1 reproduces the §6.8 K₋ numerator (+2aτ); s = −1 gives the K₊ one. The equation is even in S, so it is the same for the DSN's sign convention K∓d + S_f = 0. |
| S4 | **NUM**, not a proof | 3,999 seeded cases (seed 20261024), both s. The global minimiser of E_s on the circle exists, solves the s-branch secular equation, and has τ ≤ −κ (second-order condition sΔM_f − τI ⪰ 0, in the script's convention ∇E = τd). 0 failures. |

Evidence keys: K1–K4, S1–S3 are EV-CODE + EV-RUN (exact). S4 is EV-CODE + EV-RUN (numerical).

## 2. Owner disposition table (reconciliation §3)

| Key | Prio | Disposition | Short reason (details in §3) |
|---|---|---|---|
| GA-01 / I01 | P0 | **accept with change** | Rescope to the algebraic statement on its true domain (w = 0, Δ₃ > 0). "Valid minimizer" becomes "two antipodal stationary points; the physical minimizer is OPEN pending a declared energy". This applies at §1 line 70, §6.9 line 1048 and the §7 export line 1185. |
| GA-02 / I02 | P0 | **accept with change** | One κ. Keep κ := \|m\|\|w\| ≥ 0 (§6.8). Rewrite 9A as λ± = (τ−g) ∓ sgn(m)κ, with Π± = ½(I ± N̂) and N̂ := N/\|w\|. Domain m ≠ 0, w ≠ 0. The negative-m test is done (K2–K4). |
| GA-03 | P0 | **accept with change** | B_* is not defined in any held edition. Declare it undefined and its sign unknown at line 1004, and mark every statement that depends on sgn m. Do not identify it with RECOG's B_*. |
| GA-04 / I03 | P1 | **accept with change** | The ✓ at line 439 holds only under the scalar-M ansatz at H₀ = J_Q s_*. Define "generic" as outside the residue zero set. Lines 563 and 1054 stay OPEN beyond scalar-M; add the scope words there. |
| GA-05 / I04 | P1 | **accept** | Add the qualifier "under the additional raw-array premise KᵀB = BK (GEN-OPEN-MSPIN2-ANISO); not required by 9B typing" at line 450. |
| GB-10 / I06 | P1 | **accept with change** | Assign RIDs, exported theorems first. Assign them only after the statement is final (the sourced-junction RID waits for GA-01). Merge the §1/§6 duplicate statements to one home each. Proposed names are in §3 and are not yet assigned. |
| GB-11 / I06 | P1 | **accept** | Per-artifact custody state recorded in §5. No reconstruction is presented as recovery. |
| GB-12 / I05 | P1 | **accept (archival reference-only)** | Line 682 keeps the value only as an archival reference under DYAD-ALG-LIEGAUGE-NORM `[conv: Lie strict-kernel gauge]`, not imported (consistent with line 1142). It is never a chart or phase-moment input. Add a pointer to the Dyadic chart value +89√3/324. |
| GC-17 | P1 | **accept** | Tag check done (§9): `dyad-v6.4.22` exists, the Dyadic file on `main` equals it, both RIDs are present. One import row for DYAD v6.4.22, `DYAD-THM-SMOOTH-EMBEDDING` + `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`, scope C^∞ local germs. One sentence after G-20. The analytic case stays OPEN (Dyadic OPEN 20 B-an/B-6). |
| GA-06 / I10 | P2 | **accept** | One `GEN-OPEN-WPHASE` record (§2, line 171). Line 275 becomes a pointer, or moves to history in stage 2. |
| GA-07 / I10 | P2 | **accept** | OPEN 1T leaves the frontier list at line 94 (CLOSED at line 256). Completed OPEN 2 items leave the active lists. |
| GA-08 / I07 | P2 | **accept with change** | A scoped non-identity sentence, with no rank or map claim. The 6-moment set (line 965) is an `[ALG structure]` closure ansatz, not a basis of the exact 13-moment space (line 138). A map or rank result would be new science and is out of stage-1 scope. |
| GA-09 / I13 | P2 | **accept** | Line 61: "different objects in different declared constructions; not a verified passive conjugacy". The current text already disclaims the passive explanation. The change is wording only. |
| GB-13 / I08 | P2 | **accept with change** | One specialization line with the convention caveat. It is inserted only if the stage-1 script verifies the specialization symbolically; otherwise it is not added. |
| GB-14 / I09 | P2 | **accept** | Label √21/64 as the reference-policy / reference-reading case. Cite the Triadic §6.17 table for the four-case maximum √14/16 (TRIAD v1.6.1 line 88). The citation edition follows the GC-18/19 pin decision. |
| GB-15 / I12 | P2 | **accept** | Edition recommendation in §6 (Q1). |
| GC-18, GC-19 / I11 | P2 | **accept** | Four-part §7 (imports / exports / consumers / pins). Remove stale "current" words. Add a Consumers block from Programme v1.3 §7.2. Record the RRF v0.8.4 consumer pin (v2.8.9). |
| GB-16 | opt. | **accept** | Tier wording only. |
| GC-20 | opt. | **accept with change** | Notation note only: "γ of §6.3c is not the κ of §6.8". No physical identification or selection of κ or γ (entry note §5). |
| GC-21 | opt. | **accept** | Cite the OFN Q6 erratum (`records/gen/GENESIS_V2_8_9_NOTICE_ERRATUM_OFN_Q6_v0_1.md`) in the v2.8.9 Appendix A entry and in the next release record. Describe it as a `[SESSION]` erratum record that the owner accepted on 19 Oct 2026; that acceptance corrects the notice wording only and does not make the erratum an adopted theorem. *(Revised, §9.)* |

No row is rejected or deferred. Where these dispositions might differ from the other co-owner's, the atlas owner reconciles.

## 3. Notes on the scientific rows

### GA-01 — local sourced-junction theorem

The live statement is at line 70 (§1) and line 1048 (§6.9). The proposed scope is exported at line 1185, and OPEN M-foam depends on it at line 109.

1. **The K₊/K₋ question does not arise on the theorem's domain.**
   - The hypothesis is w = 0. Then ΔM_f(0) = 0, so K₊ = K₋ = τI (S1).
   - The GCL-02 sign issue (line 1012 ff.) applies to w ≠ 0. That is §6.8's domain, not this theorem's.
   - The display should read τd_⊥ + S_f = 0, or keep the ΔM_f term with an explicit "(ΔM_f = 0 at w = 0)".
2. **A hypothesis is missing: Δ₃ > 0.** At Δ₃ = 0 the constraint forces d_⊥ = 0, and there is no solution for σ_f ≠ 0 (S2).
3. **"Has a valid minimizer" is not supported as stated.**
   - On {|d_⊥|² = Δ₃} there are exactly two stationary points, d_⊥ = ∓√Δ₃·Ŝ_f (S2).
   - That a minimizer of any continuous functional exists on the circle is trivial by compactness.
   - Which stationary point is *the* constrained birth depends on an energy whose sign and normalization the owner text does not declare.
   - Proposed text: **"the constrained birth equation has exactly the two antipodal solutions d_⊥ = ∓√Δ₃ S_f/|S_f|; selection of the physical branch requires the birth energy, which is OPEN (GCL-02)."**
   - Grade: `[THM]`, restricted to the algebraic content. The vacuum-gluing failure (S_f = 0 impossible for σ_f ≠ 0) is unaffected.
4. **§7 export (line 1185) and OPEN M-foam (line 109)** carry the same scope. That is: the algebraic sourced-junction statement at w = 0, with the branch selection OPEN.
5. **For w ≠ 0 (outside this theorem; §6.8 scope), recorded for the GCL-02 owner record.**
   - With the trial energy E_s = (s/2)dᵀΔM_f d + Sᵀd, both branches K₋ (s = +1) and K₊ (s = −1) have a global constrained minimiser. In the script's convention its multiplier satisfies τ ≤ −κ (S3 exact; S4 numerical).
   - So the trial energy does not exclude either sign. The sign must come from the physical birth energy, which is not in the archive (§4).
   - This is `[SESSION]`. It does not change GCL-02, and no physical branch is selected (entry note §5).

### GA-02 / GA-03 — κ and B_*

1. **The text uses two κ's.**
   - §6.8 (line 1004): κ = |m||w|.
   - §6.9 9A (line 1060) and OPEN-GEN-II-9 item 1 (line 437): κ = m|w|.
   - 9A is internally consistent with the signed κ (K2). Its projectors equal ½(I ± N̂) and do not depend on m.
   - Under the §6.8 κ, the labels swap for m < 0 (K3).
2. **Proposed single convention.**
   - Keep κ := |m||w| ≥ 0, so that (ΔM_f)² = κ²I is unchanged.
   - In 9A write N̂ := N(w)/|w| and Π± := ½(I ± N̂).
   - Then λ± = (τ−g) ∓ sgn(m)κ, and L_sc⁻¹ = Π₊/(τ−g−sgn(m)κ) + Π₋/(τ−g+sgn(m)κ).
   - The soft eigenvector v₊ = (μ₁, μ₂ − |w|) is the +1 eigenvector of N̂ for either sign of m (K2).
   - The pole–projector assignment is written explicitly with sgn(m): the pole at τ − g = +κ carries Π₊ if m > 0 and Π₋ if m < 0. *(Revised after reconciliation, §9.)* No definition of the *physical* soft branch is given; its limiting-path definition stays OPEN, and the 9A "soft branch" wording is not relabelled beyond this explicit sgn(m) map.
   - Domain: m ≠ 0, w ≠ 0. At κ = 0, L_sc = (τ−g)I and there is no split.
3. **Residues.** R^(E)₊ and R^(B)₊, with Π₊ defined via N̂, do not depend on m (K4). The 9A residue statements (PSD / sign-indefinite) therefore survive the convention change unchanged. Only the pole each one attaches to depends on sgn m. **Audit range for the build:** lines 437, 1004, 1060–1074. The script's gates become the stage-1 checks.
4. **B_*.**
   - In every held edition (v2.8.6–v2.8.9) the symbol B_* occurs exactly once, at its first use in m = 2Q_sB_*. It is never defined (EV-SRC-READ).
   - Its source in ≤ v2.8.5 is not held.
   - Proposed text at line 1004: "B_* is not defined in the current owner text; its sign is unknown, and every statement that depends on sgn m carries that dependence explicitly."
   - It must not be identified with any B_* of RECOG without a mapping record.

### GB-10 — RID proposals (names proposed, **not assigned**; the PI or owner assigns)

The exported theorems of line 1185 come first:
- block-diagonal quaternionic no-go (lines 65 and 991) → *`GEN-THM-QH-NOGO`* (proposed);
- smooth single-face metric criterion (lines 67 and 1045) → *`GEN-THM-SINGLE-FACE-METRIC`* (proposed);
- local sourced-junction theorem (lines 70 and 1048) → *`GEN-THM-SOURCED-JUNCTION`* (proposed). Assign only after the GA-01 restatement.
- "tetrahedral quartic drift" (lines 44 and §6.5): the owner first confirms whether this is the P4 primitive closure (GEN-ART-P4-PRIMITIVE) before a THM RID is assigned. Its proof source is missing (§5).

Second: pure chiral protection (lines 34 and 692) and tetrahedral chronological protection (lines 42 and 908).

In each pair, §6 becomes the single home and §1 a one-line pointer (§1.1 one home per statement). The ART RIDs of §8 stay as the artifact keys.

## 4. Q3 — energy functional / second variation for the constrained birth

**Answer: not in the archive held by this session.**

Held Genesis material:
- editions v2.8.6–v2.8.9 with their drafts, previews, kits, manifests, dispositions and release records (now on `upload/gen-records`);
- the K3/6S and D-4 session records.

None of these contains a birth energy functional, or a second-variation argument for the constrained birth with ΔM_f ≠ 0 (EV-SRC-READ).

In the held editions, §6.8 states the stationarity equation only. GCL-02 records that the physical sign, energy branch and minimizer are OPEN.

The v2.8.4 "stable branch" calculations named in the reconciliation are in **v2.8.4, which is not held by this session**. Neither are the scripts `secular_numerator_trace.py` and `tau_coupling_trace.py`. Whether v2.8.4 contains an energy functional can only be answered from that edition or from the session that wrote it.

What this session can add, labelled as an independent contribution (§12.3), not a recovered source:
- **w = 0:** the elementary algebra in §3 (S1, S2). It needs no energy, because both K's coincide.
- **w ≠ 0:** for the trial energy E_s, existence of a global constrained minimiser on both branches and its second-order condition (S3, S4). The physical energy is not determined. So GA-01 is resolved by scoping, as both advisory passes recommend.

## 5. Q4 — proof-source recovery (GB-11 custody)

Custody states (entry note §3):
- (a) missing — nobody holds it;
- (b) held but not placed in the repository;
- (c) placed but not rerun.

From this session, none of the nine proof sources of lines 1223–1231 is held. The scripts inside the held v2.8.6 and v2.8.9 packages are release-pipeline scripts and the D-4 certificate only (`build_/check_/release_v2_8_x*.py`, `negative_controls_v2_8_9*.py`, `d4_transported_cubic_cert.py`).

The state below is therefore "(a) unless another session holds it, then (b)". This session cannot establish (b) or (c) for anyone else.

| Artifact | Held here? | Session state | Remark |
|---|---|---|---|
| PURE-CHIRAL | no | (a)/(b)? | A short exact algebraic check is possible as an independent contribution. |
| PHI-2TO3 | no | (a)/(b)? | — |
| **G2-CHRONO** | no | (a)/(b)? | An alternative route exists, as an **independent contribution, not recovery**: the RECOG general-p lemma `RECOG-ALG-LEADING-RETURN-EQUIVARIANCE` (§6.12; LG_k = G_k∘L) plus the charge rule, specialised to the tetrahedral block L = diag(A,A,A). This is conditional on checking that the Genesis action is of that form. It is `[ALG]` in RECOG, so the grade carried into Genesis must not exceed that unless re-proved. |
| **P4-PRIMITIVE** | no | (a)/(b)? | Certified by `genesis_k4_route_census.py` (line 946), which is not held. Not recoverable from this session. |
| PHASE-AVG | no | (a)/(b)? | Depends on P4. |
| PHASE-CLOSURE | no | (a)/(b)? | — |
| QH-NOGO | no | (a)/(b)? | — |
| **FACE-LIFT** | no | (a)/(b)? | The algebra of ΔM_f, (ΔM_f)² = κ²I and both secular equations is re-derived here (K1, S3) as an independent contribution, not a rerun. Its derivation from the UV data is not re-derived, because B_* is undefined (GA-03). |
| **SOURCED-JUNCTION** | no | (a)/(b)? | The rescoped w = 0 statement of GA-01 is proved here (S1, S2) as an independent contribution. The original proof is not recovered. |

**Recommendation.**
- Declare the evidence state at each claim now.
- Ask the PI whether any older session or account holds the v2.8.4/≤v2.8.5 editions and the scripts above. Anything recovered enters as recovered evidence pending inspection (§12.3).
- The three independent contributions above can be placed in stage 1 as `[SESSION]` evidence only if the owner decides so. They do not by themselves upgrade a grade.

## 6. Q1 — edition (recommendation) and Q2

**Recommendation: v2.9 as one release, built in the two recorded stages of Methodology §13.6.**

1. **Stage 1, corrections.** Applied to the adopted v2.8.9 file and gated by an assertion script. It gives a corrected intermediate baseline with its hash recorded; this is a build stage, not an adopted version. It contains:
   - the dispositions of §2;
   - the import row (GC-17);
   - the RID assignments the PI approves (GB-10).

   The stage gets the change-focused scientific review its P0 content requires.
2. **Stage 2, compaction and v1.4 migration.** Movement map; `tools/check_compaction.py` against the stage-1 baseline; negative fixtures.

**Reasons.**
- Two P0 rows touch a theorem that is exported at line 1185. Their correction must be reviewable as a small diff, not inside a 1,649-line layout move. §13.6 already ensures this.
- Stale statuses fixed in stage 1 need not survive stage 2.
- One adoption avoids a short-lived v2.8.10 that consumers would have to pin and then repin.

**Fallback.** If stage 2 is not ready when stage 1 has passed review, the PI may adopt the stage-1 baseline as **v2.8.10 (corrections-only, Methodology v1.3 kept)**. The migration then follows as v2.9. This is the only case where I would recommend v2.8.10.

**Q2.** Already decided: the co-owners build. This session is ready to build stage 1 once the PI has fixed the dispositions. It would then be reviewed by the other co-owner and the atlas owner. The PI may assign it the other way round.

## 7. Held records placed unchanged

Branch **`upload/gen-records`** (commit `2425539`), folder `upload/gen-records/`:
- 36 files byte-for-byte as held by this session, with `SHA256SUMS.txt` and `README_UPLOAD.md`;
- the v2.8.9 release record `GENESIS_V2_8_9_RELEASE_RECORD.md` (`f6df5d11…4181`, as cited by the erratum);
- the v2.8.6–v2.8.9 manifests, dispositions, release records, kit notes and draft/kit/release packages;
- the K3/6S and D-4 session records.

All internal zip manifests verified. The README lists what is **not held**:
- review texts and owner decisions, which arrived as chat messages;
- editions ≤ v2.8.5;
- scripts earlier than v2.8.6.

The atlas owner hash-checks and places these files. Nothing was reconstructed.

## 8. Scope kept (entry note §5)

- No rerun of the K₃ certificates or the Dyadic campaigns.
- `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` and its hypotheses are untouched.
- No physical selection of κ, γ or the sourced-junction branch: GA-01 and GA-02 are scoping and notation only.
- No notices sent.
- No hash, RID or approval is asserted beyond those quoted from the repository or computed here.

## 9. Reconciliation with the other co-owner (PR #41), 24 October 2026

The other Genesis co-owner's record is `records/gen/GEN_OWNER_DISPOSITION_ADVISORY_v2_8_9_chatgpt_20261024.md` (branch `chatgpt/gen-owner-disposition-20261024`, commit `fa8561c`). It was read in full.

**No scientific disagreement.** Both records accept all 21 rows; neither rejects or defers any. The two label counts (13 + 8 here, 10 + 11 there) differ only in labelling, so neither record is rewritten to match the other.

**Five points settled between the co-owners.** The ChatGPT co-owner agreed to the five points below in a message relayed by the PI on 24 Oct 2026.

| Row | Agreed text for stage 1 |
|---|---|
| GC-17 | The other record's condition is met. `dyad-v6.4.22` exists; `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` on `main` equals it; both RIDs are present (EV-SRC-READ). A C^∞ chart does not close the analytic OPEN 20 / B-6 case and proves no network-level node exchange. |
| GC-18 | Four-part §7: Imports / Exports / Consumers / Pins. The other record's distinctions sit inside these parts: navigation, scoped scientific imports versus representation-standard citations, blocked requests, and companion references versus historical proof pins. Consumers are not repinned in bulk. |
| GA-02 | The pole–projector map is written explicitly with sgn(m). The limiting-path definition of the physical soft branch stays OPEN. §3 is revised accordingly. |
| GB-13 | If the stage-1 script cannot verify the specialization symbolically, the line does not enter the live owner text. It stays in the working record only. |
| GC-21 | The erratum is cited both as a `[SESSION]` record and as a correction the owner accepted on 19 Oct 2026. That acceptance does not make it an adopted scientific theorem. §2 is revised accordingly. |

**PI remark, 24 Oct 2026, verbatim:** "bence benimsenmeye hazır kısımlar benimsenebilir."

This record does not itself fix the dispositions or the edition.
- The PI decides which PRs to merge.
- The PI decides Q1 (v2.9 two-stage, or v2.8.10 fallback).
- The atlas owner may keep the final reconciliation in its own record.

Stage 1 is the same under either Q1 answer. GA-01 and GA-02/03 come first.

**Repository maintenance:** PR #42 untracks the bytecode cache `tools/__pycache__/check_compaction.cpython-313.pyc`. `.gitignore` already excludes it; history is not rewritten.
