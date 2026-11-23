# RER Phase B-05: source reading note for RER-DYAD-FORMAL-INVOLUTION

**Date:** 20 Oct 2026.
**From:** Claude, RER co-owner (preparer).
**Status:** NONCANONICAL Phase B input for the receiving review. The final verdict on this record is the receiver's (B-04 routing).
- No RER record, grade, contract table or OPEN status is changed.
- Nothing is adopted, frozen or published.

## 0. Conflict disclosure for this note

The mathematics is the Dyadic owner's (v6.4.12–v6.4.13). So the receiver allowed a preparer reading. Three parts of the record are mine, however, and this note does not assess them:

| Part | Author | Treatment here |
|---|---|---|
| Owner theorems (§§6.15–6.17 of DYAD) | Dyadic owner | read and compared with the record (§2) |
| Record text, written as an owner import (r4, 17 Oct) and its erratum E1 (r4.1) | RER editor (me) | compared line by line with the owner source (§2); observations only |
| Review receipt "RER editor ACCEPT SCOPED (17 Oct)" | RER editor (me) | an editor receipt, not an independent review |
| r4.6 carrier cell | RER editor (me), implementing RRF editor Q5 | **history only (§1); no assessment**. The Q5 question and its proposed answer in the question packet were also drafted by me; the RRF editor's answer is not mine |

## 1. Editorial history of the carrier cell (r4 → r4.6)

Extracted mechanically by `b05_carrier_history.py` from the seven RER drafts held here. The span is the record heading to the next anchor. The output is in `b05_carrier_history_output.txt` and `b05_carrier_history.json`.

| RER draft | File SHA-256 | Record lines | Record span SHA-256 | Carrier cell SHA-256 | Carrier change |
|---|---|---|---|---|---|
| r4 | `93a63c49…8eff` | 849–886 | `785567cf…` | `465b1a5b…` | — (first version) |
| r4.1 | `19f16436…be42` | 849–888 | `a94d5c18…` | `465b1a5b…` | none (record changed: E1 repin to v6.4.13, OPEN 20 split) |
| r4.2 | `a443cc82…7079` | 850–889 | `a94d5c18…` | `465b1a5b…` | none; record unchanged |
| r4.3 | `0dadf6e8…b159` | 850–889 | `a94d5c18…` | `465b1a5b…` | none; record unchanged |
| r4.4 | `5df47386…a9d8` | 851–890 | `a94d5c18…` | `465b1a5b…` | none; record unchanged |
| r4.5 | `5691e20a…8c19` | 851–890 | `a94d5c18…` | `465b1a5b…` | none; record unchanged |
| r4.6 | `2fa878ff…4772` | 860–899 | `6cf39a38…` | `4dde49ed…` | **replaced** (only change in the record) |

**r4–r4.5 carrier text (verbatim):**

> Formal germs of the isolated dyad at P1 in the raw linear frame W=L(rho,eta); profile RRF-DYAD-W (RRF v0.8.2 §2.3, §2.4b). Not the triad carrier.

**Trigger.** RRF editor response v0.2 (19 Oct 2026, `413a869b…3084`, NONCANONICAL written interface response, byte-verified here), Q5 (verbatim):

> **Q5 — CONFIRM WITH CARRIER CORRECTION.** Formal `R_0=T^3 F^{-1/2}` is registered in RRF `RRF-DYAD-NF` row and §2.4b (DYAD §6.16 is its scientific owner; the formula is independent of choosing a normalizer). `RRF-DYAD-W` relabeling candidate is the finite-chart exact involution `S_h=h_6(-I)h_6^{-1}`; matching through degree-six jet is not full equality. Correct RER-DYAD-FORMAL-INVOLUTION's carrier label accordingly. Network profile `RRF-NET-W-RAW` remains provisional and separate; `RRF-DYAD-W → RRF-NET-W-RAW` bridge is OPEN. Do not create a physical network profile by that relabeling.

**r4.6 carrier text (verbatim):**

> Formal germs of the isolated dyad at P1, written in the raw linear frame W=L(rho,eta) (frame of RRF-DYAD-W, RRF v0.8.3 §2.3); R_0 is defined there without a normalizer (DYAD v6.4.13 §6.16). RRF registers the formal involution at RRF-DYAD-NF + §2.4b (formal only); the RRF-DYAD-W relabeling candidate is the finite S_h, equal to R_0 only through jet degree 6. The isolated-dyad W is not the network raw W (RRF-NET-W-RAW provisional; bridge OPEN). r4.6 carrier per RRF editor Q5; r4–r4.5 label was profile RRF-DYAD-W (RRF v0.8.2 §2.3, §2.4b). Not the triad carrier.

**r4.6 change record** (RER r4.6 line 1133, verbatim excerpt): "the carrier cell of RER-DYAD-FORMAL-INVOLUTION separates the raw-W formal germ from the RRF-DYAD-NF registration and the finite S_h (Q5)".

**Source facts the receiver may wish to set against the cell** (no assessment):
- RRF v0.8.3 (project copy, not byte-verified here), `RRF-DYAD-NF` table row "Formal involution — owner-adopted, formal only": `R_0=T^3F^{-1/2}=\widehat h(-I)\widehat h^{-1}` … `[import: DYAD v6.4.12 §6.16; RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE]`; finite `S_h` "equals `R_0` only through jet degree six under the shared normalizer convention".
- RRF v0.8.3 §8.1: "`RRF-NET-W-RAW` remains provisional, the `RRF-DYAD-W→RRF-NET-W-RAW` bridge is OPEN".
- DYAD v6.4.17 §6.16, Corollary U: "No normalizer is used."
- **Pin gap (neutral):** the r4.6 cell cites RRF v0.8.3 §2.3. The record's import lines pin only `RRF082` (v0.8.2 §2.4b, §4.2; Phase A r7: OWNER_REPORTED, RECEIVER_BYTE_VERIFIED, currency UNCHANGED_OWNER_REPORTED). No RRF v0.8.3 key appears in this record.

## 2. Owner-import fidelity (record text vs. DYAD source)

**Source read.** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_17.md` (project copy, adopted 19 Oct 2026; release SHA-256 `e07cf2b9…4bfc` as recorded, not byte-verified here). I read §2 OPEN 19/20, §6.15, §6.16, §6.17 and §8 in full.

**Version identity.** The record pins DYAD v6.4.13 (`5958f7fe…8542`). Its bytes are not held here.
- Earlier receiver statement (Phase A): §§6.15–6.17 are byte-identical from v6.4.13 through v6.4.16.
- v6.4.17 release record: only OPEN 21 items changed; no RID was renamed or regraded.
- In v6.4.17, §§6.15–6.17 carry no revision tag later than `[v6.4.13]`. This is a text-level observation; I did not byte-compare v6.4.16 and v6.4.17.

| # | Record element (r4.6) | Owner source (v6.4.17) | Reading |
|---|---|---|---|
| F1 | Closure: R_0 unique formal involution, DR(0) = −I, commuting with F; also commutes with T | §6.16 Corollary U (i)–(ii), `[THM]` | matches |
| F2 | Cent_formal,DG=I(F) = {exp(s log F)} | §6.16 Theorem C, `[THM]` | matches |
| F3 | Constraints: F = id + μ\|W\|²W + O(4); Re μ ≠ 0, Im μ ≠ 0; real formal category | §6.16 Setting; Lemma K "only Re μ ≠ 0 and Im μ ≠ 0 are used" | matches |
| F4 | Transformation law: R_0 = T³∘F^{-1/2} = ĥ(−I)ĥ⁻¹ "for any formal Poincaré–Dulac normalizer ĥ" | §6.16 Identification `[ALG]`: "for any formal Poincaré–Dulac normalizer ĥ **with λ-equivariant normal form**" | **O1**: the qualifier is not carried. RRF v0.8.3 instead writes "under the shared normalizer convention" |
| F5 | Finite S_h = R_0 only through jet degree 6 | §6.15 "Relation to S_h"; §6.16 finite reproductions (N = 6 reproduces S_6) | matches |
| F6 | Analytic bridge: "an analytic involution with R T⁶ = T⁶ R and DR(0) = −I commutes exactly with T"; Domain: "local under the owner's §6.15(b) hypotheses" | §6.15 Corollary A `[THM — analytic]`: hypotheses are R analytic, **R(0) = 0**, the §6.15 domain convention, DR(0) = −I; "(Under the hypotheses of (b), R(0)=0 is automatic …)" | **O2**: the formula line omits R(0) = 0 and the domain convention. The Domain cell names the (b) hypotheses, which imply R(0) = 0 but are narrower than Corollary A's |
| F7 | Map/clock: the same formal involution for T and T⁶; EF = TE and EF = T⁶E stay distinct | §6.15: "Both clocks select the same formal involution"; Reading/Corollary A bullets | matches |
| F8 | Grade line "[THM] (owner grade)" covering three imported RIDs | DYAD-ALG-CENT-KERNEL is `[ALG]`; the other two are `[THM]` | **O3**: the per-RID owner grades are not split in the record |
| F9 | OPEN 20 B-an, B-6 (B-6 ⇒ B-an), B-∞ existence | §2 OPEN 20; §6.16 realization hierarchy | matches |
| F10 | B-∞ flat uniqueness CLOSED: "An existing C^∞ involution with DR(0) = −I commuting with F commutes with T and is unique"; Lemma F `[THM]`, F1–F3 `[THM — conditional]` | §6.17 Lemma F; F1 also requires R(0) = 0 and the §6.15 domain convention; Lemma F is on a stated forward-invariant ball | grades match. **O4**: the R(0) = 0 / domain-convention hypotheses of F1 are not repeated in the record line |
| F11 | Lemma F uses DYAD-THM-PRIM-CTR | §6.17: "uses DYAD-THM-PRIM-CTR only" | matches. The triad non-transfer clause that follows ("G6 is OPEN …") concerns RER-TRIAD-FORMAL-INVOLUTION and is outside this note |
| F12 | "RID word CAND is an identifier, not a status" | §6.17 header (DSN v1.3 RID rule) | matches |
| F13 | Owner certificates `1cb40446…291e`, `c8c14442…cf8`, "not rerun here" | §8 DYAD-ART-OPEN19-KERNEL `1cb40446…a291e`; DYAD-ART-OPEN19-R0CERT `c8c14442…059cf8` | prefixes and suffixes agree. The record prints a three-character suffix for the second hash |
| F14 | Evidence: "independent polar-coordinate proof of the kernel lemma in the G2 consolidated note v0.4 §2a, SOURCE-READ" | DYAD Appendix A v6.4.12: that proof is "a candidate for citation in a later revision, not imported here" | **O5**: the record says SOURCE-READ, but the bytes are not held here. The B-05 inventory row G2NOTE04 is UNAUTHENTICATED_NO_HASH / HISTORICAL, and no copy was found in the workspace. G2 §5b carrier identification is still pending |
| F15 | Registry line: "owner theorems adopted in Dyadic v6.4.12 (released as v6.4.12.1; retained unchanged in adopted v6.4.13)" | v6.4.17 header lineage | matches; the line does not mention later editions |

The record's non-transfer and scope clauses do not conflict with any owner statement I found:
- no physical pole exchange;
- S_h is not upgraded;
- no existence claim.

## 3. Currency finding: Dyadic v6.4.17 (new, reported here first)

Dyadic **v6.4.17 was adopted on 19 Oct 2026** (release `e07cf2b9…4bfc`; project release record). It supersedes v6.4.16. Two consequences:
- The Phase A r7 frozen catalog (`owner_versions_known.json`: Dyadic 6.4.16) and the matrix field `current_owner_version` = 6.4.16 for the DYAD6413 row are now **stale**.
- Other records with Dyadic rows (for example the GEN records that import DYAD §6.14 / §6.3) are affected in the same way. I have not enumerated them here.

What v6.4.17 changes, per its release record:
- It adds `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (`[THM — conditional on RECOG-THM-R9-MEMORY]`).
- It closes OPEN 21 and adds notice N13.
- OPEN 20 is unchanged, and no RID is renamed or regraded.

This record's content is therefore not touched, by the release record and §2 above. RER's exact pin stays v6.4.13.

The v6.4.17 release verification by the receiver is pending. I have not byte-verified the v6.4.17 file.

**Options for the receiver** (no preference stated):
- (a) a narrow Phase A r8 that updates the catalog current version to 6.4.17 with OWNER_REPORTED authentication, using the same pattern as the r5 OFN update;
- (b) record it as a watch item until the release verification is complete.

## 4. Not in this note

- No disposition and no grade suggestion for RER-DYAD-FORMAL-INVOLUTION.
- No assessment of the r4.6 carrier wording.
- Nothing on the seven conflicted items. Their neutral inventory is the separate file `RER_PHASE_B05_NEUTRAL_SOURCE_INVENTORY_20261020.md`.
- G2 `CARRIER_IDENTIFICATION_PENDING`, both ER-2B blockages and the RER r4.6 DRAFT status are unchanged.
