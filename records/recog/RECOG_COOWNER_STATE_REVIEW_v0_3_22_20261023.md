# RECOG co-owner review of the current state (v0.3.22) — reply to the atlas-owner note of 23 Oct 2026

**Date:** 23 October 2026 · **From:** RECOG co-owner (Claude) · **To:** the PI and the atlas owner · **Status:** `[SESSION]` review. It changes no file, RID, grade or OPEN status.

**Sources read.** `rtg-corpus` was read as a shallow clone of `main` at `23a05f4` with tags.
- RECOG `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`: SHA-256 `0dcce9e4…bcd9`, identical to tag `recog-v0.3.22` and to the adoption hash.
- Dyadic v6.4.22: `2363ca40…8c29`; v6.4.19–v6.4.21 were read at their tags.
- NUMGEN v1.20.8: `835a56f8…817e`.
- Methodology v1.4, `CONVENTIONS.md`, `BASELINE.md`, `records/dyad/DYAD_NOTICES_N16_N21.md`.
- Atlas v0.2, domain D3 (L1–L5).

**Not read, on purpose:** the atlas advisory for RECOG, as the note asked. Disclosure: one repository-wide `grep` for `FC-DYAD-32` printed three lines from `records/recog/ATLAS_ADVISORY_*`. Those lines name the same R9-free route as atlas R-L1. The verification of that route in §3.1 below was done before that grep and does not rest on it.

## 1. Census (question 1)

The OPEN registry is as the atlas reads it.

| OPEN | Status line in v0.3.22 |
|---|---|
| R1 RECOG-OPEN-RHO-PARITY | PARTIAL |
| R2 RECOG-OPEN-KRET-P | CLOSED (v0.3) |
| R3 RECOG-OPEN-P2-BAND | PARTIAL (only global $W^s(P_2)$ open) |
| R4 RECOG-OPEN-TYPE-CHANGE | ACTIVE |
| R5 RECOG-OPEN-ONESIDED-SHEAR | ACTIVE |
| R6 RECOG-OPEN-EVENT-RULE | ACTIVE |
| R7 RECOG-OPEN-TWIN-ACCESS | CLOSED (v0.3.16) |
| R8 RECOG-OPEN-P2-HET-ENTRY | CLOSED (v0.3.3) |
| R9 RECOG-OPEN-LATTICE-MEMORY-NF | CLOSED (v0.3.4) |
| R10 RECOG-OPEN-RETURN-ENCLOSURE | status line "DELIVERED and ACCEPTED (v0.3.2)" (counted as closed) |
| R11 RECOG-OPEN-QUINTIC-FRAME | CLOSED (v0.3.2) |

One wording point: R10's status line is not literally "CLOSED". It should read "CLOSED (v0.3.2) — delivered and accepted" at the next release. This is wording only.

**Next work on R6.** The F3/F4 endpoint stands. The registered single-dyad package has no mechanism by which a token is retained in independent memory ($R_{\rm ind}$). The network route waits on RRF OPEN-B → OPEN-E1 → OPEN-E2, plus the bridge `RRF-DYAD-W → RRF-NET-W-RAW` and W1–W5. Neither of those is RECOG's to move.

The one RECOG-internal step I see is a scoping cell, provisionally **F5: admissible event-gated carriers**. It would do three things:
- define the class of single-dyad carrier enlargements that do not reduce to token logs, counters or the Track-A clock (criterion 5, $R_{\rm ind}$);
- turn F3's C2 definition into a necessary condition. The target is a proved statement that write-through requires a non-smooth or event-gated update on a registered carrier;
- test the one natural candidate, a branch carrier at the $C_0$ Whitney fold (E-type there, no registered R), against W-type conditions.

This is research for the PI to rank. Nothing in it is ready for a release.

## 2. Atlas D3 reading (question 2)

Most of D3 is a faithful and careful reading. I checked R-S2, R-G1, R-P3 and R-T2 against the DSN text, and all four are correct. Where D3 goes wrong or overreaches:

| # | Atlas site | Issue | Correct reading |
|---|---|---|---|
| A1 | R-L5 (i) | It says R1's covariance premise "is satisfied exactly in $C^\infty$" by Dyadic's $R=T^3\circ K_2^{-1}$. | R1's premise is about physical pole exchange, acting at linear order as $S_o=-I$. $R$ shows that a $C^\infty$ germ involution with $DR(0)=-I$ commuting exactly with $T$ exists. So the swap-odd conclusion is *consistent with* an exact commuting involution. It does not show that the physical pole exchange acts as $R$ (Dyadic: "not a physical exchange"; RRF OPEN-A; OPEN-OFN-OPA). RECOG §6.4 also stays true: $T$ breaks $S_o$-equivariance at quadratic order. Item (ii), the $3/(8\sqrt Q)$ shadow for $R(\Sigma_B)$ from $j^2R=j^2S_h$, is correct. |
| A2 | L2 A1a, RECIPROCAL-AMPLITUDE row; R-L1 | It says the constant $15/2$ "is exactly the explicit L-BACKBONE constant NUMGEN lacks". | $15/2$ bounds the per-block reciprocal increment on the explicit $U$. An explicit L-BACKBONE error constant ($q_M=1/M+O(M^{-3/2})$) still needs a summation with a $Q_0$-dependent constant, and it holds on $U$, not on NUMGEN's tube. It supplies the ingredient; it is not the constant itself. |
| A3 | L2 A1a, CD-IDENTIFICATION row; R-L1b | It calls RECOG-THM-A1A-CD-IDENTIFICATION the "candidate owner node" for NUMGEN's $\phi^*$. | NUMGEN v1.20.8 (§3, pre-registration pin) says Dyadic's asymptotic-phase objects "are not a substitute without a separate comparison proof". The same holds for $C_D^{\rm ext}=\tau\log Q_0-M_W$. It reproduces the $\tau\ln\lambda$ entry-phase shift only up to the change of $M_W$, which is $O(\sqrt{Q_0})$. It is a *candidate source*, pending a comparison proof that NUMGEN would own. |
| A4 | L1/L2 A1a rows | They write "H-NG discharged by NUMGEN-RESULT-N5AS1-INF1" and similar. | RECOG v0.3.22 cites these items as `RID unavailable` with a pending repin. The RIDs are now canonical (NUMGEN v1.20.8), so the edge is right as of today. It should still be marked as the atlas's identification, not RECOG text. |
| A5 | R-L7 | It says Dyadic "does not record that the premise is an adopted RECOG THM". | Partly stale. Dyadic v6.4.20+ records N11 as RECOG's adopted use (§7 notices; N19 asks RECOG to reconcile §7.2). Still open on the Dyadic side: OPEN 21's "Recorded distinctions" still cite R9 "at statement level only (RECOG v0.3.20 …)". |
| A6 | R-L3 | Lattice-clock regrade, "owner to verify". | **Verified, with a scope note.** From R9 ($\Psi_z\to\Psi_\infty$) and $1/q_m=m+O(\log m)$ (§6.13a corollary), $\Theta_m=\Psi_\infty-\tau\log m+o(1)$ on the $C_z$ track for the exact $\widehat F$. Hence the threshold ratio is $e^{\pi/(3\tau)}$ with no NUMGEN import. The frame change from post-$H_2$ to the chart moves $\Theta$ by $O(\sqrt q)\to0$, so the ratio limit carries over. Candidate grade: `[RESULT] [from: THM]`, recorded as RECOG's own route next to the NUMGEN import. |

**Missed by D3.** Everything in §3 marked "not in atlas".

## 3. Upstream changes (question 3)

### 3.1 Changes that touch a RECOG claim at statement level

**(a) DYAD-THM-LPHASE-ROWA-REMAINDER (v6.4.19) makes the R9-free existence route a theorem on the explicit $U$.** This is atlas R-L1, verified here.

**Source** (v6.4.22 §6.14): for $x\in U$ and every $m\ge0$,
- **(B)** $|W(Ty)/(\lambda W(y))-1|\le0.04654$ on $U_T$;
- **(R)** $\hat\varphi_{6(m+1)}-\hat\varphi_{6m}=2\pi-\tau Q_m+r_m$, with $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$.

The lift is the increasing lift (§7.0a I1). The frames agree on $U_T$ (I2). $Q_m$ is primitive (I3).

**Argument:**
1. $D_M^U=\sum_{m<M}(\tau Q_m-r_m)$.
2. By RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, $Q_m^{-1}=Q_0^{-1}+m+E_m$ with $|E_m|\le\tfrac{15}2\sum_{j<m}\sqrt{\min(Q_0,2/j)}=O(\sqrt m)$.
3. So $Q_m-(m+Q_0^{-1})^{-1}=O(m^{-3/2})$ and $Q_m^{3/2}=O(m^{-3/2})$. Both are summable.
4. Hence $D_M^U-\tau\log M$ converges for every $x_0\in U$, with neither R9 nor INF-1. This is H-NG on all of $U$.

**Consequences:**
- RECOG-THM-A1A-PHASE-EXISTENCE-ALT discharges unconditionally. $\Psi_{W,\infty}$ and $\Psi_{z,\infty}$ exist for every start in $U$ without R9, which is an R9-free T1-type existence on $U$.
- RECOG-RESULT-A1A-PHASE-EXISTENCE-NG (domain $U\cap U_{\rm NUMGEN}$) is no longer the strongest form.

**Proposed release action:**
- Register a new RECOG `[THM]` on explicit $U$, citing DYAD-THM-LPHASE-ROWA-REMAINDER (row A) and RECIPROCAL-AMPLITUDE.
- Keep (a) and (b′) unchanged as the NUMGEN-route records. Changing (a)'s domain in place would hide a scientific change.
- Tell Dyadic. This bears on its "R9-independent version" target: existence only, starts in $U$; OPEN 21 keeps R9. Dyadic's FC-DYAD-32, a SESSION result, offers the same route, and Dyadic leaves the H-NG decision to RECOG.

**(b) The Dyadic tag form changed at v6.4.21.** RECOG §6.13b and §7 quote:
- `[ALG — formal second order; remainder not certified]` for the primitive-variable form;
- `[THM — conditional on RECOG-THM-R9-MEMORY]` for T1/T2 and OPEN 21.

Dyadic v6.4.21/v6.4.22 now write:
- `[ALG]` `[scope: formal second order; remainder certified separately, OPEN 21]`;
- `[THM]` `[assuming: RECOG-THM-R9-MEMORY]` (Methodology v1.4 grammar).

The content and grade are unchanged. The old strings occur 0 times in v6.4.21/22 and 1–3 times in v6.4.19/20. RECOG's "carried verbatim" claim is now verbatim only to v6.4.18. Not in atlas.

**(c) OPEN 21 constants and rows, K₀, T1/T2: unchanged.** In v6.4.22:
- K′ = 3951/1000, 971/250;
- C₂ = 517, 163;
- (256/225)²;
- w_j = 3/64, 3/128;
- K₀ = 1101/1000.

The certified content RECOG uses is intact.

### 3.2 Stale RECOG passages (no statement change)

| # | Passage | Why stale | In atlas |
|---|---|---|---|
| S1 | §6.13b and §7: the two NUMGEN imports read `RID unavailable … canonical repin pending NUMGEN v1.20.8`; the companion line has the same | NUMGEN v1.20.8 adopted 21 Oct. Repin to `NUMGEN-DEF-N5AS1-DEFECT` and `NUMGEN-RESULT-N5AS1-INF1`. The INF-1 `Depends on:` line can cite `-PRIMITIVE-LIFT`, `-L-BACKBONE`, `-L-MONO`, `-L-PHASE`. A1a-G1 closes fully. | R-P2 |
| S2 | §6.13b and §7: v6.4.18 pins with **line numbers** "§6.14 lines 806–809, 843–850" (5 occurrences) | Line numbers are not stable across editions. In v6.4.22 OPEN 21 starts at line 876 and the primitive form sits inside line 842. Repin to v6.4.22 by RID and section, and keep the A1a-E2 source check as evidence for v6.4.18 (`EV-SRC-READ`). | no |
| S3 | Header "DSN Methodology: v1.3"; §6.13b "Methodology v1.3 §3.4" | v1.4 in force (§3.4 M13-C04 unchanged in substance) | no |
| S4 | Companion pins: Dyadic v6.4.10/16/18, NUMGEN v1.20.7, OFN v0.10, RRF v0.8.3 | Current: Dyadic v6.4.22, NUMGEN v1.20.8, RRF v0.8.4. Needs a claim-level G2-type check per v1.4 §13.9 before repinning. | partly |
| S5 | §7 rows "(none — §6.1/§6.4/§6.7–6.8 block)", "(none — Dyadic §6.5)" | Dyadic v6.4.20 registered `DYAD-DEF-CRITICAL-CURVE` ($C_0$), `DYAD-ALG-QC-CRITICAL-AMPLITUDE`, `DYAD-ALG-ISP-MAPS`, `DYAD-ALG-SIXSTEP-CUBIC-JET`, `DYAD-ALG-RAW-ANGULAR-MEAN`. Identifiers only. | note §3 |
| S6 | §7.2 N13/N11 rows | N11 is now recorded by Dyadic as RECOG's adopted use, and N19 asks RECOG to reconcile §7.2. N13's verification field can also cite the release-verification report hash; the report itself was not read by RECOG. | R-L7 |
| S7 | Freeze-status line: v0.3.21 "current authoritative edition" | Erratum E-0322-1 (post-release maintenance note) | reviewer note |
| S8 | §7.2 outbound notices; v0.3.22 notices N-D / N-NG / N-O/R/E | Live notice history belongs in `records/recog/` (v1.4 §1.1). All are still unsent. | — |
| S9 | §7.1 "OFN pins RECOG v0.3.1 — current is v0.3.20"; RRF v0.4 row "PI adoption pending"; §4 p-family row lists $c_\theta^{(6)}$ and backbone; SG-R10 "R9/R10/R11" open-wording; closed OPEN blocks keep "Active sub-items" | confirmed against the text | R-P3, R-T1, R-T2 |
| S10 | §6.13a/§7.3: Dyadic consumer pin of R9 "statement level only (RECOG v0.3.20)" | Dyadic-side; to be noted in RECOG's §7.3 only as a consumer record | — |

**Other owners:**
- **RRF v0.8.4:** imports W3 verbatim from v0.3.21. That answers RF-1, so RECOG can close its RF-1 notice row.
- **RER v0.2:** keeps the v0.3.20 pin and records v0.3.21/v0.3.22. No RECOG action.
- **OFN:** unchanged.
- **Dyadic K_p frame scale** (`DYAD-ALG-KP-FRAME-SCALE`, $\nu_3^Z=\cot^2(\pi/p)\nu_3^{W_p}$): agrees with RECOG's $6\bar\lambda\nu_3(\zeta_6)=3\mu_6^W$, since $\cot^2(\pi/6)=3$. A frame cross-reference may be added; no statement changes.

## 4. Unreleased work (question 4)

There is no unreleased scientific work since v0.3.22. The session has only governance and record files from after adoption:
- `RECOG_v0_3_22_POST_RELEASE_MAINTENANCE_NOTE.md` (`b5b9131c…eab0`): E-0322-1/E-0322-2;
- `RECOG_v0_3_22_OUTBOUND_NOTICES.md` (`0de67ec4…5ed5`): prepared, unsent;
- `RECOG_v0_3_22_RELEASE_VERIFICATION_PACKAGE.zip` (`9db286eb…5288`).

All three are in the hand-over bundle.

## 5. Records (question 5)

This session holds the original release and governance records, most §8 certificates and scripts, and all earlier RECOG editions. Hashes confirmed include:
- freeze provenance `5c00f66d…9b55`, matching RER's citation;
- v0.3.21 release record `4b7aefee…`;
- v0.3.22 release record `d9636a8d…0820`;
- v0.3.20 `fdb8c9a7…b8df`.

They are packed unchanged in `RECOG_HANDOVER_RECORDS_AND_EVIDENCE_20261023.zip`, with `MANIFEST.md` and `SHA256SUMS.txt`, for the PI to upload to an `upload/recog-records` branch.
- **Coverage:** of 78 full hashes cited in the DSN, 62 are loose files in the bundle, 4 are members of a bundled frozen zip, and 5 are owner DSNs.
- **Not held here** (manifest list): three contributor scripts (CELL-A p5, CELL-B, CELL-C), four PI production outputs (F2(b) rev. 1 script and rev. 2 results, E3A-1 rev. 3.1 summary and late cells) plus the E2C chunks run on the PI machine, and several reviews and owner reports that were never handed into this session.
