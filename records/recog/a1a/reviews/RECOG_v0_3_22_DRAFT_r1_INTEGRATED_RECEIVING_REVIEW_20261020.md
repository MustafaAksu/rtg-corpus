# RECOG v0.3.22 DRAFT r1 — Independent integrated receiving review

**Date:** 20 October 2026  
**Review level:** `[SESSION]` scientific/integration/release-readiness review; not an owner adoption, RID registration, freeze or dispatch.  
**Disposition:** **ACCEPT SCIENTIFIC INTEGRATION WITH TWO LIMITED RECORD CORRECTIONS; ADOPTION HELD ON A1a-G1 AND THE SEPARATE PI DECISION.**

## 1. Verified source manifest and review scope

| Item | Version / identity verified | Inspection |
|---|---|---|
| Methodology | `DSN_METHODOLOGY_v1.3.md`, SHA-256 `3e23ba94606706b3c8d50aecfb2184df52042cf8e65cdd3c3e0cd3159254ec7e` | §§3.3–3.4, missing-RID and conditional-proof rules |
| RECOG adopted base | v0.3.21, SHA-256 `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3`, 301,292 bytes | All bytes hashed and reconstructed by exact reverse-delta; scientifically relevant §6.13a and §7 reviewed |
| RECOG proposed draft | v0.3.22 DRAFT r1, SHA-256 `2acf910da1ebb75a75a96031061cb2241fed2bf5906ba70d6bc7c4c83fc10762`, 324,169 bytes, 1,577 lines | All bytes hashed; new §6.13b, changed source and governance paragraphs, §7, §7.2, §8, §9, Appendix A examined |
| Package | `RECOG_v0_3_22_DRAFT_r1_package.zip`, SHA-256 `9fa7380e25be58bb00c571dd21f7deec33700cec6baaff37338754476a904fff` | 25 nondirectory members; 24 payload members individually hash- and size-verified against MANIFEST.json (manifest itself excluded, conventionally) |
| NUMGEN owner | v1.20.7, SHA-256 `c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28` | §6.6 L-BACKBONE, L-MONO, L-PHASE, INF-1 directly compared |
| Dyadic owner | v6.4.18, SHA-256 `f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d` | §6.14 primitive-variable second-order qualifier and OPEN 21 theorem, bounds and row domains directly compared; v6.4.17 bytes not inspected |
| NUMGEN proposed RID request | `RECOG_TO_NUMGEN_A1A_RID_REQUEST_20261020.md`, SHA-256 `a89b69243f24d63f74fed29c9af809f8616017ecdbbd8ef07446ed646e0246a0` | Complete request read; explicitly prepared, not sent |

This is an integrated claim-and-provenance review, **not** an independent re-execution of the Dyadic 28-gate P5 certificate, RECOG's Arb R9 certificate, or the older 1,493-line adopted RECOG scientific portfolio. For the older portfolio, the exact reconstruction/reverse check establishes no change outside the specified 17 edit replacements.

## 2. Independent package and rebuild audit `[ENG — SESSION]`

- Base inside package and separately mounted adopted v0.3.21: byte-identical.
- Draft inside package and independently uploaded Markdown: byte-identical.
- Request inside package and separately uploaded Markdown: byte-identical.
- Unpacked package into fresh directory, ran builder with `python -I`, independently reproduced both draft and edit JSON byte for byte.
- Ran checker independently with `python -I --controls`: C0–C11 **12/12 PASS**, NC1–NC12 **12/12 caught**, and output byte-identical to the archived checker output.
- Exact-once builder operations: 17 edits H1–H7, A1, R1, S1, I1–I2, N1, F1, P1, V1–V2, with original adoption base preserved.
- Byte-exact C1/C3 protections establish the scoped delta. **Qualification:** all negative-control mutations also fail the exact-draft C1 gate; therefore 12 caught mutations do not independently demonstrate that each semantic guard would detect an arbitrary unrelated change without C1. They are valid regressions for the frozen build, not 12 separate mathematical proof certificates.
- Eight proposed new scientific RECOG identifiers and four new artifact identifiers; all distinct and not already present in base. They are **not registered** merely by appearing in this draft.

## 3. Scientific integration review `[SESSION]`

**Accepted claims and grades, within the postulated generator T:** 

1. `[THM]` Primitive lift alignment on Dyadic's six-phase invariant tube, via the exact one-step map and the strict rational angle enclosure `143209/750000 < 1/2`.
2. `[THM]` Reciprocal radial increment bound `|1/Q_{m+1}-1/Q_m-1| < (15/2) sqrt(Q_m)` and `MQ_M -> 1` on `U = {0<Q_0<=1/625}`. The stated summation follows from Dyadic's adopted radial decay.
3. `[ALG]` Exact finite-block identity using A1a's **local** defect `D_M^U` (not an unqualified enlargement of NUMGEN's `D_M`).
4. `[THM] [assuming: H-NG]` Conditional implication: existence of the defect limit on U implies existence and equality of primitive/normalized asymptotic phase limits, using the unconditional P4 offset bound; no R9 use.
5. `(a) [RESULT] [from: ALG]` On `U intersect U_NUMGEN`, NUMGEN INF-1 discharges H-NG, yielding existence without R9. `U_NUMGEN` remains existential and has no explicit radius.
6. `(b) [THM]` On U, RECOG's already adopted R9 discharges the conditional hypothesis of Dyadic T1/T2 and yields the extended `C_D^ext` identity. No cyclic proof dependence on A1a is found.
7. `(b') [RESULT] [from: ALG]` Equality of `C_D^ext` and the original NUMGEN `C_D` only on the intersection, because `D_M^U = D_M` there.
8. `(c) [THM]` On the separately restricted A and B disks, primitive-variable OPEN 21 quantitative bound; source and grade verified directly against adopted Dyadic v6.4.18 §6.14. Source-statement E2 is PASS, **not** a certification replay. The owner formal-second-order form remains `[ALG — formal second order; remainder not certified]`.

**Unchanged:** adopted R9 theorem and row profiles, historical RIDs/grades, OPEN R6 ACTIVE, comparator-track restrictions, OPEN-P0 model selection, A1b/A1c not implied. No physical recognition-event rule is established.

## 4. Limited corrections before a release candidate r2

**L1 — Header claim typing.** The new v0.3.22 status-summary paragraph says, in substance, that "Number Genesis's primitive phase defect `D_M` and Dyadic's block phase align exactly" on the entire U. The proof there establishes alignment of **A1a's extension** `D_M^U` on U, with `D_M^U=D_M` only on `U intersect U_NUMGEN`. Restate the header as: *"A1a's local extension `D_M^U` of the Number Genesis defect formula aligns exactly with Dyadic's block phase on U; on the intersection with NUMGEN's existential tube it equals NUMGEN's `D_M`."* This avoids silently enlarging upstream claim custody. No scientific theorem or grade change.

**L2 — RID-request dispatch semantics.** The dedicated request is explicitly **prepared and not sent**. The draft nevertheless uses `dedicated RID requested` in the companion note, §6.13b and §7. Preserve the Methodology §3.3 temporary exception but mark *"dedicated RID request prepared, not yet dispatched; A1a-G1 OPEN"* until there is real evidence of delivery. The request itself should remain untouched until dispatched. This corrects metadata, not a source assertion.

**Optional provenance completeness:** The ZIP manifest is internally complete for its 24 listed payloads, but not every externally referenced C4/review item in §8 is packaged. In particular the actual NUMGEN C4 reply `8a887ef3…bc4d` and its separate receiving review are referenced by identity, not included in the ZIP. Both can be read from separately mounted project evidence in this review; a strictly self-contained release archive would need those copies or explicit external archive locators. This is not a false manifest entry and not a mathematical blocker.

**Optional precision:** Header's old Dyadic-v6.4.17 `release verification pending` language belongs to the historical v0.3.21 comparison. Label it explicitly as such or refer readers to the updated three-column §7.2 N13 receipt; the new N13 row is correctly separated into receipt, verification, conditional RECOG use.

## 5. Unresolved release gate and lifecycle

**A1a-G1 remains OPEN.** Methodology v1.3 §3.3 allows `RID unavailable` as a declared temporary exception but requires the missing-identifier governance to be made explicit. Its example says *"dedicated RID requested"*. Here the actual request file has not been sent; even a sent request is not an owner response. For final sign-off obtain one of:

- **NUMGEN owner response** assigning a RID or recording deferral/decline, with its identity and receipt; or
- **A recorded PI/Methodology-steward decision** authorizing the continuing exception for this release, naming its owner (NUMGEN) and unresolved state.

Do not invent a NUMGEN RID, use the defect-threshold ratio RID as INF-1's identity, or mark a prepared request as dispatched. Any adoption and release verification remain separate decisions following the corrected integrated draft.

**G3 status:** OFN, RRF and RER notices remain unsent; no send or acknowledgment records inferred here.

## 6. Final disposition

**`SCIENTIFIC/ENGINEERING INTEGRATION REVIEW ACCEPTED — LIMITED METADATA PATCH (L1/L2) REQUIRED; A1a-G1 OPEN; NO ADOPTION AUTHORIZED`.**

Prepare DRAFT r2 from the same adopted v0.3.21 hash, with only L1/L2 and optionally the historical header clarification. Rebuild, hash, rerun all controls and record the r1→r2 delta. Independent receiving review then checks the exact correction; PI adoption, if chosen, follows a separate release decision and only then registers the eight scientific and four artifact identifiers.
