# Genesis next edition — stage-1 implementation matrix (preparation)

**Date:** 24 October 2026
**From:** Genesis co-owner session (Claude)
**Status:** working note, kept at one fixed path and changed by commit (CONVENTIONS).

This note is **preparation only.** It is neither a build nor an adoption. It does not authorize anything:
- Nothing in `dsn/` is changed.
- No edit below is applied, and no RID is assigned.
- Preparing a stage-1 candidate does not authorize a merge, a tag or scientific adoption.

**Still open for the PI:**
1. Authorize the 21 reconciled dispositions as the stage-1 scope.
2. Q1, the edition: v2.9 in two stages, or v2.8.10 as the fallback.

**Basis:**
- `records/gen/GEN_OWNER_DISPOSITION_ADVISORY_v2_8_9_claude-genowner_20261024.md` (PR #39, including §9 reconciliation);
- `records/gen/GEN_OWNER_DISPOSITION_ADVISORY_v2_8_9_chatgpt_20261024.md` (PR #41);
- the reconciliation §3 (PR #37).

## 1. Frozen source manifest

Hashes computed on `main` @ `091baaf` (24 Oct 2026).

| Source | Edition | SHA-256 | Tag check |
|---|---|---|---|
| `dsn/RTG_GENESIS_GEOMETRY_DSN.md` (**stage-1 input**) | v2.8.9 | `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` | equals `gen-v2.8.9` |
| `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` | v6.4.22 | `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29` | equals `dyad-v6.4.22` |
| `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` | v1.6.1 | `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f` | tag `triad-v1.6.1` exists |
| `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` | v0.3.24 | `8c64bea231b3691b737f4143f6f4105030ee183fcc90d7f604ec83a4c869e7c1` | **no `recog-v0.3.24` tag yet** (latest is `recog-v0.3.23`). Adopted per the `main` commit `6a26a83`; use only after the tag exists. |
| `dsn/RTG_PROGRAMME_OVERVIEW.md` | v1.3 | `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06` | tag `programme-v1.3` exists |
| `dsn/RTG_RRF_REPRESENTATION_REGISTRY.md` | v0.8.4 | `2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce` | tag `rrf-v0.8.4` exists |
| `dsn/DSN_METHODOLOGY.md` | v1.4 | `cdacab5feb79161cd86313086065ca67313ef354e30ceaf205386cf2f3a0f2df` | tag `methodology-v1.4` exists |

**Notes on the manifest.**
- "Tag exists" for the Triadic, Programme, RRF and Methodology rows means the tag is present. Equality of the file with the tag is checked by the build script before use; it was checked here only for GEN and DYAD.
- The material on `upload/gen-records` (PR #40) is **not** a stage-1 source until the atlas owner's hash and provenance check passes.
- **Change since PR #39:** RECOG is now v0.3.24 on `main`. The G2-CHRONO route in PR #39 §5 cited v0.3.23. `RECOG-ALG-LEADING-RETURN-EQUIVARIANCE` is still present at v0.3.24 (line 39).

## 2. Build rules for stage 1 (from CONVENTIONS and Methodology §13.6)

**Script.** `evidence/gen/scripts/build_gen_stage1.py` (to be written after authorization). It:
- refuses an input other than `d143673e…c6fc`;
- applies each edit below exactly once, with a unique anchor and an assertion;
- logs old and new line hashes;
- writes the intermediate baseline and records its hash. This is a build stage, not an adopted version.

**Checker.** `evidence/gen/scripts/check_gen_stage1.py`. It verifies:
- the changed lines equal the edit list;
- every other byte is unchanged;
- claim-tag counts per block;
- the RID set changes only by approved assignments;
- the protected blocks are unchanged.

**Protected (byte-identical):**
- §6.3a–§6.3c, except the one GC-17 sentence after G-20;
- the K3/6S RIDs and `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` with its hypotheses (entry note §5);
- Appendix A history entries other than the new edition entry.

**Negative controls.** At least one per gate family:
- a tampered anchor;
- a double application;
- an edit inside a protected block;
- a missing GA-01 hypothesis;
- a wrong sgn(m) map.

**Evidence gates carried over.** `gen_owner_advisory_checks.py` (`0ba256be…bf99`, PR #39) K1–K4 and S1–S3 are the algebraic checks behind GA-01 and GA-02. S4 is numerical and supports no live text.

## 3. Edit matrix

Line numbers refer to `d143673e…c6fc`. The proposed text is a draft for owner review; the final wording is fixed in the build review.

### 3.1 P0 rows

| ID | Row | Site (line) | Current text (anchor) | Proposed edit |
|---|---|---|---|---|
| E01 | GA-01 | §1, 70 | "If $w=0$ and $\sigma_f\neq0$: vacuum gluing fails ($S_f = 0$ is impossible), but the constrained birth $(\Delta M_f + \tau I)d_\perp + S_f = 0$ has a valid minimizer." | "If $w=0$, $\sigma_f\neq0$ and $\Delta_3>0$: vacuum gluing fails ($S_f=0$ is impossible), and the constrained birth equation (where $\Delta M_f(0)=0$, so $K_\pm=\tau I$) $\tau d_\perp+S_f=0$, $\lvert d_\perp\rvert^2=\Delta_3$, has exactly the two antipodal solutions $d_\perp=\mp\sqrt{\Delta_3}\,S_f/\lvert S_f\rvert$. Selecting the physical branch requires the birth energy and its constrained second variation, which are OPEN (GCL-02)." The last sentence ("foam branch is sourced-birth") is kept. |
| E02 | GA-01 | §6.9, 1048 | the same theorem in its §6 form | The same statement, with §6 as its single home (GB-10). §1 line 70 becomes a one-line summary with a pointer (§1.1). |
| E03 | GA-01 | §7 export, 1185 | "…and the local sourced-junction theorem with their stated scopes." | Append "(the algebraic statement at $w=0$, $\Delta_3>0$; physical branch selection OPEN)". |
| E04 | GA-01 | §2 item 7, 109 | "OPEN M-foam … Downstream of local sourced-junction structure." | Add "(algebraic statement only; branch selection OPEN, GCL-02)". |
| E05 | GA-02 | §6.8, 1004 | "…$(\Delta M_f)^2 = \kappa^2 I, \quad \kappa = \lvert m\rvert\lvert w\rvert$." | Unchanged. This becomes the single definition. Add after the display: "We write $\hat N:=N(w)/\lvert w\rvert$ for $w\neq0$, so $\Delta M_f=\operatorname{sgn}(m)\,\kappa\,\hat N$." |
| E06 | GA-02 | §6.9 9A, 1060–1062 | "eigenvalues are $\lambda_\pm=(\tau-g)\mp\kappa$, $\kappa=m\lvert w\rvert$"; "$\Pi_\pm=\tfrac12(I\pm\Delta M_f/\kappa)$"; "The soft branch is $\tau-g-\kappa\to0$ with soft eigenvector $v_+$…" | Replace with: $\lambda_\pm=(\tau-g)\mp\operatorname{sgn}(m)\kappa$; $\Pi_\pm=\tfrac12(I\pm\hat N)$; $L_{\rm sc}^{-1}=\Pi_+/(\tau-g-\operatorname{sgn}(m)\kappa)+\Pi_-/(\tau-g+\operatorname{sgn}(m)\kappa)$; domain $m\neq0$, $w\neq0$. Then "$v_+=(\mu_1,\mu_2-\lvert w\rvert)$ spans the range of $\Pi_+$ for either sign of $m$. The pole at $\tau-g=+\kappa$ carries $\Pi_+$ if $m>0$ and $\Pi_-$ if $m<0$. The limiting-path definition of the physical soft branch remains OPEN (OPEN-GEN-II-9)." The RID `GEN-THM-SCALARM-EIGEN` and its grade are kept. |
| E07 | GA-02 | §2 OPEN-GEN-II-9, 437–438 | "$\kappa=m\lvert w\rvert$"; "Soft-mode identification (branch $\tau-g-\kappa\to0$, …): `[ALG]` ✓" | Replace with $\kappa=\lvert m\rvert\lvert w\rvert$ and the sgn(m) form. Item 2 becomes "Pole–projector map with explicit sgn(m): `[ALG]` ✓; physical soft-branch limiting path: `[OPEN]`." |
| E08 | GA-02 | 9A residues, 1066–1068 | the $R^{(E)}_+$ and $R^{(B)}_+$ definitions | Text unchanged. Add one clause: "with $\Pi_+=\tfrac12(I+\hat N)$, both numerators are independent of the sign of $m$". |
| E09 | GA-02 | 81–82, 1057–1058 (`GEN-ALG-SCALARM-RESOLVENT`) | "Algebraic poles occur at $\tau-g=\pm\kappa$…" | **No change needed.** These lines are valid for κ ≥ 0 and already route branch selection to OPEN-GEN-II-9. Listed so that the checker confirms they stay unchanged. |
| E10 | GA-03 | §6.8, 1004 | "$m = 2Q_s B_*$" | Add: "$B_*$ is not defined in the current owner text; its sign is unknown, so every statement that depends on $\operatorname{sgn}(m)$ carries that dependence explicitly. $B_*$ is not identified with any quantity of another stream." |

### 3.2 P1 rows

| ID | Row | Site | Edit |
|---|---|---|---|
| E11 | GA-04 | 439 | "✓" → "✓ `[scope: scalar-M ansatz, $H_0=J_Qs_*$]`". "generically" is defined as "off the residue zero set (one line for $R^{(E)}_+$, two lines for $R^{(B)}_+$ in $s_*$-space)". |
| E12 | GA-04 | 563 (SG-13), 1054 | Add "beyond the scalar-M ansatz" after "Projection nontriviality is `[OPEN]`". |
| E13 | GA-05 | 450 | Add "under the additional raw-array premise $K^\top B=BK$ (`GEN-OPEN-MSPIN2-ANISO`); not required by the 9B type contract". |
| E14 | GB-10 | 34/692, 42/908, 44, 65/991, 67/1045, 70/1048 | §6 becomes the single home and §1 a pointer. **RID assignment needs a PI/owner decision.** The proposed names in PR #39 §3 are not assigned and need a collision check. The sourced-junction RID comes after E01. |
| E15 | GB-11 | §8, 1223–1231 | Each ART line gets its custody state: (a) missing, (b) held but not placed, or (c) placed but not rerun, as known at build time. The independent contributions are cited as such, never as recovery. |
| E16 | GB-12 | 682 | Add "archival reference only (`DYAD-ALG-LIEGAUGE-NORM`, not imported; see §7 note at 1142); not a chart or phase-moment input; the Dyadic chart quintic phase coefficient is $+89\sqrt3/324$ (DYAD v6.4.22)". |
| E17 | GC-17 | §7 Dyadic block (1133 ff.); after G-20 (892) | One import row: `DYAD-THM-SMOOTH-EMBEDDING`, `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` from v6.4.22, scope C^∞ local germs, plus an $(\rho,\eta)\to W$ frame note. After G-20, one sentence: "By DYAD v6.4.22 a $C^\infty$ (hence $C^3$) $\Phi$ with $\Phi(0)=0$, $D\Phi(0)=I$ and $\Phi T\Phi^{-1}$ commuting with $A$ exists, so (C2) is non-vacuous at $C^\infty$; the analytic case remains Dyadic OPEN 20 B-an/B-6, and no network-level node exchange follows." The §6.3c body stays byte-identical. Whether the rest of the Dyadic block is repinned from v6.4.13 is part of E21. |

### 3.3 P2 and optional rows

| ID | Row | Site | Edit |
|---|---|---|---|
| E18 | GA-06 | 171, 275 | Line 171 stays the single `GEN-OPEN-WPHASE` record. Line 275 becomes a pointer that keeps its obligations and links. |
| E19 | GA-07 | 94 (frontier 1b); OPEN 2 at 264 ff. | OPEN 1T leaves the active list (CLOSED at 256). Completed OPEN 2 items leave the active lists and point to their closure record. |
| E20 | GA-08 | 965 | Add: "a coarse closure ansatz; not a basis of the 13-moment space of OPEN 1A (line 138); no rank or map is asserted". |
| E21 | GC-18/19 | §7 (1131–1200) | Four parts: **Imports** (scoped scientific imports; representation-standard citations; blocked requests such as the Discrete Genesis block at line 1167, Programme IF25), **Exports**, **Consumers** (from Programme v1.3 §7.2: TRIAD, UVM, RECOG, RRF, OFN, RER/FMS/ER-2B, each at the pin they declare), **Pins** (producer pins, separating current companion references from historical proof pins). No bulk repin. Stale "current" words are removed. |
| E22 | GA-09 | 61 | Wording: "different objects in different declared constructions; not a verified passive conjugacy". |
| E23 | GB-13 | 206 / 1214 and 1204 | Insert the GSPLIT ↔ DELTA-QC specialization line **only if** the build script verifies it symbolically under the declared inner product. Otherwise there is no live-text change, and the result goes to the working record. |
| E24 | GB-14 | 1215 (and 1335 history, unchanged) | Label √21/64 as the reference-policy / reference-reading case. Cite TRIAD v1.6.1 §6.17 for the four-case maximum √14/16. |
| E25 | GB-16 | 10 | Tier wording only; Programme maturity grades unchanged. |
| E26 | GC-20 | §6.3c guard area, outside the protected body | Notation note: "γ of §6.3c is not the κ of §6.8 or the birth coefficient κ of §6.1; no parameter identification". |
| E27 | GC-21 | Appendix A, v2.8.9 entry | Cite `records/gen/GENESIS_V2_8_9_NOTICE_ERRATUM_OFN_Q6_v0_1.md` as a `[SESSION]` erratum that the owner accepted on 19 Oct 2026. That acceptance does not make it an adopted theorem. |
| E28 | GB-15 | header, Appendix A, footer | New-edition metadata only. The v1.4 migration itself belongs to stage 2. |

## 4. New finding for the owners (not in the advisory)

**F-1. κ denotes two different objects.**
- κ is the triadic birth coefficient: $c_0^{[3]}=\kappa Q_sJ_Qs_*$; $\kappa_{\rm shear}=-2\sqrt3/3$, $\kappa_{\rm recoil}=-1/2$; $Q_c=\kappa^2Q_s^3$. It appears at lines 38, 140, 183–198, 303–307, 536, 614 and 721–733. It is signed and negative in both reference policies.
- κ is also the face-lift magnitude $\kappa=\lvert m\rvert\lvert w\rvert\ge0$, at lines 81–82, 434–438, 1004–1083.
- Programme §8.2 keeps its own κ table.

GA-02 fixes the sign of the second κ, but the shared symbol remains.

**Proposal for owner decision.** Rename the face-lift κ to $\kappa_f$ in §6.8/§6.9 and at their §2 mentions. This is a notation-only edit with no scientific change. Otherwise add an explicit notation guard at line 1004.

It is not applied without a decision. If adopted, E05–E09 use $\kappa_f$.

## 5. Next steps

**After PI authorization:**
- write `build_gen_stage1.py` and `check_gen_stage1.py` with the negative controls;
- produce the intermediate baseline and its hash;
- the ChatGPT co-owner and the atlas owner give change-focused review.

**Stage 2 (if v2.9):** movement map; `tools/check_compaction.py` against the stage-1 baseline.

**Release record:** `records/gen/RTG_GENESIS_GEOMETRY_v<version>_RELEASE_RECORD.md` (DRAFT).
