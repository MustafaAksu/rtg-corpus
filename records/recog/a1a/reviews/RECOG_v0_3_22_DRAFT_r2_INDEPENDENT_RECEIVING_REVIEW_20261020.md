# RECOG v0.3.22 DRAFT r2 — Independent integrated receiving review

**Date:** 20 October 2026  
**Review grade:** `[SESSION]`; review of a candidate DSN and its package, **not** scientific owner adoption, RID registration, freeze, release, or cross-stream dispatch.  
**Disposition:** **INTEGRATED REVIEW ACCEPTED — L1/L2 CLOSED; A1a-G1 OPEN; ADOPTION NOT AUTHORIZED BY THIS REVIEW.**

## 1. Verified source manifest and scope

| Source | Independently verified identity | Scope actually examined |
|---|---|---|
| Adopted RECOG base | `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21.md`; SHA-256 `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3`; 301,292 bytes | Entire byte sequence rehashed, exact delta/reversal against r2; previous §6.13a/R9 owner chain taken at adopted grade; existing portfolio **not** independently recertified |
| Candidate RECOG r2 | `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22_DRAFT_r2.md`; SHA-256 `8f7f6f861e419afa2e43c11e32b0d5e1647f37a81f63baafdc41a15905c1624e`; 325,687 bytes; 1,578 lines | Rehashed in ZIP and uploaded copy; all changed spans, §6.13b, §7/§7.2/§8, status summaries and release metadata reviewed |
| r2 package | `RECOG_v0_3_22_DRAFT_r2_package.zip`; SHA-256 `ca486fa6c06a9f8e8be1a6f23780cab33760e766d054ef46f2eb9f70ecfc0ba4` | All 31 manifest-listed payload files hash/size checked; 32 files including self-excluded manifest |
| Methodology | `DSN_METHODOLOGY_v1_3.md`; SHA-256 `3e23ba94606706b3c8d50aecfb2184df52042cf8e65cdd3c3e0cd3159254ec7e` | §§3.3–3.4, 4.5: missing-RID grammar, grade distinction and exported-claim custody |
| NUMGEN owner | `RTG_NUMBER_GENESIS_DSN_v1_20_7.md`; SHA-256 `c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28` | §6.6 INF-1 / L-BACKBONE / L-PHASE checked at point of use; NUMGEN C4 response is cited in draft, not packaged here |
| Dyadic owner | `RTG_DYADIC_OSCILLATOR_DSN_v6_4_18.md`; SHA-256 `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d` | §6.14 primitive-variable form, OPEN 21 theorem, R9 condition and row constants; no new P5 recertification |
| r1 independent review | `RECOG_v0_3_22_DRAFT_r1_INTEGRATED_RECEIVING_REVIEW_20261020.md`; SHA-256 `c1d4901381305a101d11b88a5f553619eceb562829c40580fcf6734b34d88d17` | Read completely from the r2 package; L1/L2 acceptance requirements compared directly |
| A1a E2 source record | `RECOG_A1A_E2_OPEN21_SOURCE_CHECK_v6_4_18_20261020.md`; SHA-256 `941f42d6273f707bb161c24bd7e753c12acacda991dd29ff4050cbdcbfa6126e` | Source-statement fidelity only; not a proof-certificate replay |

Verified from files in this review environment, not a claim of global current-version discovery.

## 2. Independent reproduction `[ENG — SESSION]`

- Unpacked r2 in a fresh directory and checked **31/31** entries against the package manifest (SHA-256 and byte size). The manifest is not self-listed.
- Package copy of the adopted v0.3.21 source has the required full SHA and is unchanged; package draft and separately uploaded draft are byte-identical.
- Re-executed `python -I build_recog_v0_3_22_draft_r2.py BASE reproduced/`. Rebuilt DRAFT r2 and the 17-edit JSON are both byte-identical to the archived outputs.
- Re-executed `python -I check_recog_v0_3_22_draft_r2.py BASE DRAFT EDITS --controls`: **C0–C12 13/13 PASS**, **NC1–NC13 13/13 caught**, exit 0; checker output byte-identical to the archived output.
- Executed the unchanged historical `r1/check_recog_v0_3_22_draft.py` on the archived r1 base, draft, and edits, with controls: PASS and output byte-identical to archived r1 output.
- Independently compared r1 → r2 via unified diff: **13 added and 12 removed lines (25 changed)**, across header/status text, §6.13b request metadata, §7 RID-pending entries, §8 archive provenance, Appendix A and footer. No A1a mathematical formula, theorem grade, domain, proof dependency or proposed RID changed. Reverse exact-edit verification proves no unlisted base changes.
- **Negative-control interpretation:** the checker contains a global exact-build gate C1, so catching 13 mutations does not imply that each independent semantic subgate would detect arbitrary mutations if C1 were disabled. The controls are valid frozen-build regression tests, not 13 independent scientific proofs.

Additional independent checks: the A1a C1 script ran with G1–G6 PASS and 3/3 negative controls caught; exact rational arithmetic confirms `4R+(4/3)R²=143209/750000<1/2`, `16/375<1/20`, `16/15 · 3/128=1/40`. The script's dense numerical G6 check is **not** itself the analytic proof of the Taylor bounds.

## 3. L1/L2 disposition

**L1 CLOSED — PASS.** The new v0.3.22 status summary says expressly that the object aligned with Dyadic block phase throughout the explicit `U={0<Q_0<=1/625}` is RECOG's local extension `D_M^U`. Only on `U ∩ U_NUMGEN` does `D_M^U=D_M` hold. Section §6.13b, the finite-block identity, and the (a)/(b)/(b′) scope distinctions match this summary. No NUMGEN theorem has been enlarged.

**L2 CLOSED — PASS.** Current companion header, §6.13b and the two new NUMGEN entries of §7 consistently say **request prepared, not yet dispatched; A1a-G1 OPEN**. The request file itself is unchanged and its SHA-256 is `a89b69243f24d63f74fed29c9af809f8616017ecdbbd8ef07446ed646e0246a0`. Older Appendix A historical wording need not be retroactively changed. No imaginary owner reply, dispatch or RID is registered.

**Other fixes PASS.** The Dyadic v6.4.17 verification-pending phrase is explicitly typed as historical v0.3.21 metadata and points to N13; §8 now clarifies the independently held evidence that is hash-cited but not included in the ZIP, and records the r1 receiving review.

## 4. Integrated scientific and source-consumer disposition

`[SESSION]` No new scientific objection arises from r2. The r1 scientific acceptance carries forward unmodified. The mathematical results retain separate scopes and grades:

| Block | Proposed grade | Dependency and permissible scope | Review |
|---|---|---|---|
| C1 lift alignment and reciprocal amplitude | `[THM]`, `[THM]` | Postulated `T`, explicit Dyadic tube `U` | PASS at inherited r1 proof and current algebra/check level |
| Finite-block identity | `[ALG]`, internal | RECOG's `D_M^U` | PASS |
| H-NG implication | `[THM] [assuming: H-NG]` | Only implication; no presumed INF-1 on the entire `U` | PASS |
| (a) | `[RESULT] [from: ALG]` | `U ∩ U_NUMGEN`, selected `T`; NUMGEN INF-1; **without R9** | PASS |
| (b) | `[THM]` | `U`; RECOG's adopted R9 discharges Dyadic T1/T2 premises | PASS |
| (b′) | `[RESULT] [from: ALG]` | `U ∩ U_NUMGEN`, equality with NUMGEN's start-dependent `C_D` | PASS |
| (c) | `[THM]` | Separate rows A/B; Dyadic v6.4.18 OPEN 21, with its R9 premise discharged by RECOG R9 | PASS, **source-statement fidelity**, no certificate rerun |

The second-order primitive form remains owner-tagged `[ALG — formal second order; remainder not certified]`; only OPEN 21 gives the certified per-row bound with `K'_A=3951/1000`, `K'_B=971/250`, `C_{2,A}=517`, `C_{2,B}=163`, and `(256/225)^2`. Neither comparator-track transfer nor OPEN-P0 physical generator selection is supplied by A1a. R6 remains ACTIVE.

Eight distinct scientific RID proposals and four artifact RID proposals are present, absent from the authoritative base; they remain **proposed, not registered**.

## 5. Nonblocking documentation notes

- **N1 — N13 historical candidate label.** The §7.2 N13 RECOG-use cell still says `v0.3.22 DRAFT r1: proposed use ...`. As an accurate *historical* statement it is not false, but for a final candidate/update this could be revised to `v0.3.22 DRAFT r2 (superseding r1): proposed use ...` or to a revision-neutral `v0.3.22 draft` reference. No proof or source change is needed. It does not block accepting the r2 integrated review.
- **N2 — checker docstring.** The header of `check_recog_v0_3_22_draft_r2.py` still shows the old `dedicated RID requested` condition under its human-readable C10 description, and the usage comment retains an r1 checker filename. The executable C10/C12 implementation **does enforce the correct r2 conditions**, and tests pass; update the help/docstring if creating a final publication tool bundle. This is documentation hygiene, not a checker failure.

No r3 is required solely to implement N1/N2 before addressing A1a-G1, unless the owner wants fully synchronized candidate metadata before sign-off.

## 6. Remaining hard release gate and recommendation

**A1a-G1 OPEN — release-blocking.** Methodology v1.3 §3.3 permits a declared temporary `RID unavailable` exception but does not convert a prepared request into a resolution. Recommended default: transmit the already prepared `RECOG_TO_NUMGEN_A1A_RID_REQUEST_20261020.md` to NUMGEN and record a real owner reply assigning a RID or explicitly deferring/declining. Alternatively, the PI acting as Methodology steward may issue a specific recorded authorization to continue the temporary exception for v0.3.22 naming NUMGEN as responsible owner. Neither decision is documented as having occurred here.

Following A1a-G1 closure, retain the r2 acceptance and obtain a **separate PI adoption decision**. Only then register the eight scientific/four artifact RIDs, produce a released DSN with version metadata, verify release files, and update dispatch/receipt history. Neither G3 OFN/RRF/RER notices nor any other cross-chat dispatch was performed by this review.

**Final:** `DRAFT r2 INTEGRATED REVIEW ACCEPTED — L1/L2 CLOSED; A1a-G1 OPEN; NO ADOPTION, RID REGISTRATION, FREEZE OR DISPATCH`.
