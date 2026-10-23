# G3-DYAD — RECOG adoption, N10–N13 receipts and downstream dependency notification

**Status:** [SESSION] OUTBOUND NOTICE — FINAL FOR DISPATCH, NOT SENT. Drafted by the contributor; owner corrections by the RECOG co-owner (Claude), listed at the end. The PI sends it; dispatch and acknowledgment are recorded in `RECOG_G3_DISPATCH_RECORD_20261020.md`. **Date:** 20 October 2026.
**Recipient:** Dyadic Oscillator owner. Editions known to RECOG: v6.4.16 (`33c14c5c…59e0`, release-verified); v6.4.17 (`e07cf2b9…4bfc`, adopted 19 Oct 2026) and v6.4.18 (`f70308f19f5955c0597c03a27b572abfd4c8746aef6922c959675eb0d56e458d`, adopted 20 Oct 2026), both with reviewer release verification pending according to Dyadic's own release records.

RECOG v0.3.21 was **adopted** 20 October 2026 (**not frozen**). Adopted source: `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21.md`, SHA-256 `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3`. Predecessor v0.3.20 remains frozen, SHA-256 `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df`; G1 record `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` (SHA-256 `5c00f66dae7d4de6ccd4a04d642a23edfc861bbd6bd55e432513747fbd679b55`). Release record SHA-256 `4b7aefeeaf5803d85e904dee246924f8f48f106a677078c167c2189a9573ef72`.

[OWNER: RECOG v0.3.21 §§7.2–7.3] The G2 consumer audit of Dyadic's pinned v6.4.10 against the reported v6.4.17 source checked 18 load-bearing RECOG uses: no changed imported theorem statement, hypothesis, certified row, chart, constant or grade. NF6 gained supporting evidence, §6.1 map received an identifier, and Dyadic OPEN 12 was reported as PARTIAL; RECOG R3 still owns only global `W^s(P_2)` geometry, not later positive-branch re-intersections or large-amplitude dynamics. The bridge-lemma mutual-citation guard remains: Dyadic owns the statement, RECOG §6.12 the general-p proof provenance; neither citation strengthens the other.

## Three-state receipts: received / source verification / RECOG use

| Notice | Received | Source verification / lifecycle | RECOG use |
|---|---|---|---|
| N10 (Dyadic v6.4.14) | `DYAD-ALG-OPEN3-LEADING`, `DYAD-THM-OPEN3-SPIRAL-REM` | Content carried unchanged in the verified adopted v6.4.16 | None; no new RECOG claim |
| N11 (v6.4.15) | `DYAD-ALG-OPEN3-PHASE-OFFSET`, `DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS`, `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` (T1/T2) | Content carried unchanged in verified adopted v6.4.16 | **Reference-only** quantitative SG-R14 note, with T2 conditional on T1 and T1 conditional on `RECOG-THM-R9-MEMORY` |
| N12 (v6.4.16) | OPEN 3 CLOSED at its defined scope; OPEN 21 opened | Verified adopted edition | None |
| N13 (reported v6.4.17; SHA-256 `e07cf2b93b532554d9e1d05d2bfef3be34829b7cb892627c0bb03d1d182d4bfc`) | `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER`, conditional on R9 | **Owner release verification pending** in RECOG's receiving record; G2 passage comparison is not that release verification | **None decided; conditional receipt only**; no N13 theorem used by RECOG |

The only N11 quantitative note [OWNER: RECOG v0.3.21 SG-R14; Dyadic §6.14, N11 reference] is `M_W-M=-Δ_0(z_0)`, `|M_W-M|≤K_0 sqrt(q_0)`. Keep the certified rows separate: `K_0=1101/1000` on `|z|≤1/20`, and `K_0=533/500` on `|z|≤1/40`. `M_W` denotes primitive-phase memory through Dyadic's transported asymptotic-phase observable, **not** an exact-map theorem for raw comparator `C_W^(h)`; no R9 coefficient or comparator-incompleteness theorem is moved between tracks.

**v6.4.18.** RECOG's claim-level audit was run against v6.4.17. v6.4.18 is not claim-audited by RECOG. Its release record states that the changes are confined to OPEN 20 B-∞ existence (§6.17, `DYAD-THM-SMOOTH-EMBEDDING`) and that no adopted RID is renamed or regraded. RECOG records this as owner-reported and asks the owner to confirm that the RECOG-consumed passages (§1 import lines, §6.9 bridge-lemma provenance, §6.11 ν₃ import, OPEN 12, §6.14 and its consumer cross-references) are unchanged from v6.4.17. N14 (v6.4.18) is addressed to FMS, RRF and OFN, not to RECOG; RECOG records it as seen only.

## Reverse dependency and source-status request

RECOG v0.3.21 §7.3 now registers Dyadic's uses of `RECOG-THM-R9-MEMORY`, chart laws, the ν3 closed form/non-vanishing results, leading-return equivariance, and the two P2 theorems. Any proposed change to a listed RECOG statement, hypotheses, domain/rows, constants, track or grade will be notified to each registered consumer **before** RECOG releases it. New rows/windows are additive but still notified on release. This is a notification discipline, not a Dyadic theorem adoption.

N13 asked RECOG to flag any change of the R9 statement, rows or $C_2$; the §7.3 notification rule is RECOG's answer, and no such change is made by v0.3.21.

Please update the stale Dyadic “freeze candidate” lines for RECOG. In v6.4.18 they are: the header list of editions inspected in the v6.4.11 pass (“RECOG v0.3.20 (live header: freeze candidate)”); the §7 programme-context row (“`RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20` (freeze candidate)”); and the §7 consumer row (“live header: freeze candidate; final freeze record not inspected”). Please distinguish frozen v0.3.20 from adopted v0.3.21, without changing theorem custody. Import tags of the form `[import: RECOG v0.3.20 §…]` may stay as they are or be repinned: the cited RECOG passages are identical in v0.3.21. Please return the independent owner-release identity/verification for v6.4.17 if available, so RECOG can separately revisit N13's **verification**, and only then separately decide whether to use its theorem. No Dyadic OPEN status or scientific grade is changed by this notice.

## Owner corrections to the contributor draft

- Recipient line: added the adopted v6.4.18 edition and its hash. Both v6.4.17 and v6.4.18 have reviewer release verification pending, according to Dyadic's own release records.
- New v6.4.18 paragraph. RECOG audited v6.4.17, not v6.4.18. The v6.4.18 change summary is recorded as owner-reported, and Dyadic is asked to confirm that the RECOG-consumed passages are unchanged. N14 is recorded as seen, not received.
- N13's request to flag R9 changes is answered by the §7.3 notification rule.
- The stale "freeze candidate" lines are now named by location in v6.4.18. The import tags may stay pinned to v0.3.20, because the cited text is identical in v0.3.21.
- The G1 record is cited with its hash.
