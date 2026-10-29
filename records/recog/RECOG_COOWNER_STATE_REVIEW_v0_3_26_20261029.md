# RECOG co-owner review of the current state (v0.3.26) — against the review of 23 October 2026

**Date:** 29 October 2026 · **From:** RECOG co-owner (Claude) · **To:** the PI · **Status:** `[SESSION]` review. It changes no file, RID, grade or OPEN status. Predecessor: `records/recog/RECOG_COOWNER_STATE_REVIEW_v0_3_22_20261023.md` (23 Oct 2026, at `recog-v0.3.22`); the plan it was measured against: `records/recog/RECOG_STUDY_PLAN_2026-10-19.md`.

**Sources read.** `main` at `2c076a7` (the `recog-v0.3.26` merge commit) with tags: RECOG `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` SHA-256 `45e307f8…dd34` (identical to the tag and to `BASELINE.md`); the editions v0.3.22–v0.3.26 at their tags for the census; the release records v0.3.23–v0.3.26; `BASELINE.md` companion rows (Dyadic v6.4.22, NUMGEN v1.21, OFN v0.10, RRF v0.8.4, RER v0.2, TDRG v2.12.14, Atlas v0.7); the open pull requests. Not re-read: the owner DSNs beyond their `BASELINE.md` rows (no claim-level audit of companions is made here; the v0.3.25 and v0.3.26 claim audits stand for the statements RECOG uses).

## 0. Bottom line

1. **Six days, four adopted editions, no OPEN moved.** v0.3.23 (23 Oct), v0.3.24 (24 Oct), v0.3.25 (27 Oct), v0.3.26 (28 Oct). RIDs 106 → 136; `[THM]` blocks 65 → 69; `[ALG]` 161 → 172; `[NUM]` 17 → 38; artifact RIDs 36 → 45. The OPEN census is exactly the one of 23 October: R2, R7–R11 CLOSED; R1, R3 PARTIAL; R4, R5, R6 ACTIVE. The growth is depth under R6 (the A1a–A1c chain) and under R9/R4, not closure.
2. **The mathematics moved where the 19 Oct plan said it would, by a different route.** The plan's Phase-1 cells were A1 (token read-out of R9 memory), A2 (involution ledger), A3 (R4 sub-item 1), A4 (class-C audit) and the compute cell B1. Done: A3 (v0.3.24), B1 at Stage A and the L1/L2 rows (v0.3.25). Replaced: A1's "C_D = τ log Q − M_W read-out" became the A1a–A1c chain — R9-free existence of $C_D^{\rm ext}$ on all of $U$ (v0.3.23), the explicit-$U$ slip schedule and the infinite-record phase readout (v0.3.24), the known-$a$ sharpened schedule, the record-only outer decoder and the record-fiber structure (v0.3.25), the drift centring and the log-free envelope (v0.3.26). Not done: A2 (typed involution ledger; only RECOG-ALG-SWAP-ODD-RHO was named), A4 (CELL-F6), B2 (R3), B3 (R4 census), F5.
3. **The interfaces improved less than the mathematics.** Pins are current (Dyadic v6.4.22 by RID, NUMGEN v1.20.8 by RID, RRF v0.8.4, OFN v0.10) and the Methodology v1.4 grammar is in force (`[assuming:]` 0 → 25 occurrences). But **no outbound notice has been sent since the previous review** — the v0.3.22 notices (N-D, N-NG, N-O/R/E), the v0.3.25 notices N1–N6 (PR #90, review-accepted, unmerged) and the v0.3.26 notices M1–M4 (PR #104) are all "prepared". Two of them are requests that gate RECOG's own grades: the (D5) proof constants and the $C_7$ ceilings as Dyadic owner statements. NUMGEN moved to v1.21 (BASELINE) while RECOG pins v1.20.8; the repin waits on its own claim audit.
4. **One scientific correction was needed and made.** v0.3.26 retracts, in Appendix B under Methodology §3.6, two asymptotic-order sentences of v0.3.25 about closed-form majorants (`Lg`'s $M$-independent slack; the uniform $\kappa$ in the reference term). No inequality, grade or RID was affected; the statements are restated for corrected closed forms. The finding came from inside the programme (the drift-centering cell checking the order of its own remaining terms), two days after the sentences were adopted. §5 draws the lesson: order sentences about majorants need an all-$M$ statement with explicit constants, or the label "grid observation".
5. **What the next cell should be is now a quantitative question, not a conceptual one.** On the known-$a$ side the log-free envelope $E^{(5)}$ is dominated by the in-block residual $c_P(r)Q^\dagger$ ($14.4/(a+M)$ at $r=5$ of $19.15$) and the start-offset slack; the drift constant $K_\epsilon$ is $98$ % Dyadic's $C_7$ ceiling. On the R6 side the open question is Q1′ (injectivity of the record map); the decoder gives windows, not identification. Nothing on the carrier/write-through side has changed since F3/F4.

## 1. Census

### 1.1 OPEN registry (unchanged since 23 Oct)

| OPEN | 23 Oct (v0.3.22) | 29 Oct (v0.3.26) | What moved underneath |
|---|---|---|---|
| R1 RHO-PARITY | PARTIAL | PARTIAL | RECOG-ALG-SWAP-ODD-RHO named (v0.3.23); the A2 involution ledger not done |
| R2 KRET-P | CLOSED (v0.3) | CLOSED | — |
| R3 P2-BAND | PARTIAL | PARTIAL | B2 not started |
| R4 TYPE-CHANGE | ACTIVE | ACTIVE | sub-item 1 answered in reframed form (RECOG-ALG-QUADRATURE-TYPING, v0.3.24); sub-item 2 (periodic census) open; the odd-$m$ period-2 family inventoried |
| R5 ONESIDED-SHEAR | ACTIVE | ACTIVE | — |
| R6 EVENT-RULE | ACTIVE | ACTIVE | three new sub-items: A1c readout `[RESULT]` ✓ (v0.3.24); A1c-decoder answered in bounded form ✓ (v0.3.25); A1c-Q1′ `[OPEN]` |
| R7 TWIN-ACCESS | CLOSED (v0.3.16) | CLOSED | — |
| R8 P2-HET-ENTRY | CLOSED (v0.3.3) | CLOSED | — |
| R9 LATTICE-MEMORY-NF | CLOSED (v0.3.4) | CLOSED | rows sharpened: $(259.2,\tfrac1{400})$, $(81.49,\tfrac1{1600})$ unconditional; $(221.4,\tfrac1{400})$, $(75.69,\tfrac1{1600})$ under the $C_7$ ceilings (v0.3.25) |
| R10 RETURN-ENCLOSURE | "DELIVERED and ACCEPTED" | CLOSED (v0.3.2) — delivered and accepted | wording fixed (v0.3.23), as the previous review asked |
| R11 QUINTIC-FRAME | CLOSED (v0.3.2) | CLOSED | — |

### 1.2 Grade census by edition (live text)

| Edition | bytes | RIDs | `[THM]` | `[ALG]` | `[RESULT]` | `[NUM]` | `[assuming:]` | artifact RIDs |
|---|---|---|---|---|---|---|---|---|
| v0.3.22 | 329,148 | 106 | 65 | 161 | 49 | 17 | 0 | 36 |
| v0.3.23 | 281,915 | 110 | 60 | 150 | 47 | 15 | 12 | 37 |
| v0.3.24 | 295,325 | 116 | 63 | 153 | 49 | 25 | 12 | 39 |
| v0.3.25 | 331,038 | 132 | 69 | 168 | 49 | 34 | 23 | 43 |
| v0.3.26 | 349,982 | 136 | 69 | 172 | 49 | 38 | 25 | 45 |

The v0.3.23 drop is the header/Appendix-A compaction (history moved to the tag); every later growth is new science and registry rows, no compaction since. The `[assuming:]` column is the Methodology v1.4 grammar replacing the old "conditional on" tag forms, plus the genuinely conditional new blocks: every (D5)-dependent statement and the $C_7$-ceiling rows carry it; nothing became unconditional in the period.

### 1.3 What the four editions added (by group, as adopted)

- **v0.3.23** — RECOG-THM-A1A-PHASE-EXISTENCE-U: R9-free existence of $C_D^{\rm ext}$ on all of $U$ (the route the previous review verified in its §3.1(a)); NUMGEN and Dyadic imports repinned by RID (S1, S2 of the previous review); the atlas-advisory dispositions; compaction.
- **v0.3.24** — A1b: RECOG-THM-A1B-SLIP-SCHEDULE-U (B-events as lift crossings; alphabet $\{6,7\}$; digamma slip schedule with explicit error ceiling); A1c: RECOG-RESULT-A1C-RECORD-PHASE-READOUT (the complete record determines $\Psi_\infty$ mod $2\pi$, conditional on A1b; no carrier downgrade); A3: RECOG-ALG-QUADRATURE-TYPING, RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY; structural maintenance.
- **v0.3.25** — B1: RECOG-ALG-R9-SUM-LEMMA, RECOG-THM-R9-SHARPENED-ROWS(-C7); A1c-E: harmonic tails, in-block angle law, exact combined-tail identity, RECOG-THM-A1C-SHARPENED-SCHEDULE `[assuming: (D5)]` (known-$a$ envelope $E'''$); A1c-D: admissible region, start offset, joint contractor — the record-only outer decoder (windows on $U$ with $\ge2$ usable slips; no uniqueness); A1c-Q: threshold coding and the $C^1$ record fibers (Q1′ reduced, not closed).
- **v0.3.26** — CORR (Appendix B, §3.6): the two retractions and the `[COR]` restatements; DRIFT: RECOG-ALG-A1C-RECIPROCAL-DRIFT (exact first order $-\tfrac{29}{216}$, log-free $K_\epsilon$ for every $m$ and admissible $b$, exact centring identity); ENV: RECOG-ALG-A1C-LOGFREE-ENVELOPE `[assuming: (D5)]` — $E^{(5)}\le C(a,r)/(a+M)$ for every $M\ge1$ with explicit constants.

## 2. The previous review's items — where they stand

| Item (23 Oct) | Then | Now |
|---|---|---|
| §1 R10 wording | "should read CLOSED (v0.3.2) — delivered and accepted" | done, v0.3.23 |
| §1 F5 (admissible event-gated carriers) | proposed as the one RECOG-internal R6 step | not started; the A1b/A1c chain took the R6 slot and produced the readout `[RESULT]`, the decoder and Q1′ instead — a different, sharper question about the *record* rather than the carrier. F5 remains the carrier-side question and is unchanged |
| §2 A1–A6 (atlas D3 reading) | six corrections to the atlas reading | disposed with the PI's reconciliation record (v0.3.23 basis); A6 (lattice-clock regrade as RECOG's own route) — the ratio $e^{\pi/(3\tau)}$ appears in the DSN; whether it carries the proposed `[RESULT] [from: THM]` grade as a RECOG route was not re-verified here |
| §3.1(a) R9-free existence on $U$ | proposed as a new `[THM]` | adopted as RECOG-THM-A1A-PHASE-EXISTENCE-U (v0.3.23) |
| §3.1(b) Dyadic tag forms | RECOG quoted v6.4.18 forms | repinned to v6.4.22 forms (v0.3.23) |
| §3.1(c) OPEN 21 constants | unchanged | unchanged; RECOG's own rows sharpened (v0.3.25) and offered to Dyadic (N3, unsent) |
| S1 NUMGEN `RID unavailable` | pending repin | done (v0.3.23); NUMGEN has since moved to v1.21 — repin pending its own claim audit |
| S2 line-number pins | 5 occurrences | 0 |
| S3 Methodology v1.3 | header and §6.13b | 0 occurrences; v1.4 grammar throughout |
| S4 companion pins | v6.4.10/16/18, v1.20.7, RRF v0.8.3 | v6.4.22, v1.20.8, v0.8.4, OFN v0.10 (NUMGEN v1.21 pending) |
| S5 §7 "(none — …)" rows | Dyadic RIDs of v6.4.20 missing | the v6.4.20 RIDs added (v0.3.23); 9 "(none — …)" rows remain, legitimately (owner has no RID, e.g. RRF Registry noncanonical rows) |
| S6 N11/N13 | reconcile §7.2 | §7.2 current state rewritten (v0.3.23); notice states unchanged (nothing sent) |
| S7 freeze-status line | erratum E-0322-1 | gone with the compaction |
| S8 live notice history in the DSN | belongs in records | moved: §7.2 points to `records/recog/g3/` and the notice records |
| S9 stale wordings (OFN pin v0.3.1, RRF v0.4 "PI adoption pending", …) | confirmed | OFN wording gone; the two RRF Registry rows still read "noncanonical, PI adoption pending" — correct as a description of RRF's registry status, not stale |
| S10 Dyadic consumer pin of R9 "v0.3.20" | Dyadic-side | unchanged on Dyadic's side as far as RECOG records; a consumer record only |
| §4 unreleased work | none | none: everything produced since is adopted or in records; the stacked cell PRs #59–#75 are in `main` and should be closed (housekeeping) |
| §5 hand-over bundle | packed for `upload/recog-records` | the records and evidence of the four editions are in the repository tree (`records/recog/`, `evidence/recog/`); the 23 Oct bundle's "not held" list (contributor scripts, PI production outputs) is unchanged |

## 3. Interfaces

**Dyadic.** RECOG now rests on Dyadic in three distinct ways and the tags say which: (i) adopted rows (NF6, NF-REM, LPHASE row A and branch (B), PRIM-CTR, NF-INV) — unconditional use; (ii) the $C_7$ certificate values $85.07/27.60$ as ceilings — `[assuming:]`, one `[THM]` row pair; (iii) the (D5) row-A bridge proof constants $c_Q$, $c'_Q$ and the remainder decomposition — `[assuming:]`, the whole known-$a$ envelope chain (sharpened schedule, decoder, log-free envelope). Both registration requests (N1, N2) are written and unsent. Until Dyadic registers them, RECOG-THM-A1C-SHARPENED-SCHEDULE and RECOG-ALG-A1C-LOGFREE-ENVELOPE stay conditional theorems however many times they are reviewed. The reverse direction: RECOG's sum lemma sharpens Dyadic's $\sum q_m^3$ bound and its OPEN 21 constant (N3), and $K_\epsilon$ names the one Dyadic bound that would lower it (M1). Dyadic's own notices N19, N21 to RECOG are still "prepared by Dyadic, not sent".

**NUMGEN.** The A1a/A1b chain gives NUMGEN what the plan called the explicit L-BACKBONE ingredient and the R9-free $C_D^{\rm ext}$; custody of GAP-LOCK and INF-1 is unchanged. BASELINE says NUMGEN v1.21; RECOG imports v1.20.8 by RID. Action: claim audit at `numgen-v1.21`, then a repin micro-edit (recorded as pending since v0.3.25).

**Consumers (OFN, RRF, RER).** RRF v0.8.4 imports W3 verbatim (RF-1 fulfilled); RER v0.2 pins v0.3.20 and records later editions; OFN v0.10 unchanged. The v0.3.26 correction changes no consumed inequality (M2). None has been told of v0.3.23–v0.3.26.

**Atlas.** Atlas v0.7 (tag `atlas-v0.7`, 28 Oct) carries RECOG v0.3.25 — the receiving review accepted the RECOG transfer (R9, A1c, RECOG.R-A1). v0.3.26 is the row update M4 for the next Atlas edition.

## 4. Governance: what the period established

- **The package pattern.** Each edition was built as a stage-1 intermediate by an assertion-gated builder, checked by a deterministic checker with negative controls (v0.3.25: C0–C24, 27 controls; v0.3.26: C0–C25, 33 controls), decoupled into per-group variants so that the PI could adopt a subset, reviewed by the co-owner (ChatGPT) in one or two rounds, adopted group by group with the PI's words recorded verbatim, and published by a metadata-only transform whose diff is the eight declared lines. Four editions went through it without a publication defect. It is now the RECOG release method in practice; it is not yet written down as such outside the release records.
- **Separate acceptances worked.** The PI's "dördünü de benimsiyorum" (v0.3.25) and "üçünü de benimsiyorum" (v0.3.26) were decisions over independently reviewable groups with independent variant hashes. The one time the reviewer split (v0.3.26 round 1: CORR ACCEPT, DRIFT CONDITIONAL, ENV HOLD), the split mapped onto the variants and one batched revision resolved it.
- **The correction worked as §3.6 intends.** A false order sentence was found by the programme itself, disposed by the PI with an explicit choice (option (b)), retracted in Appendix B with reason and replacement, and the cell records that carried it were left unchanged (their hashes are cited). The cost was one maintenance round.
- **Reviews are on GitHub**, as the PI asked on 27 Oct: every PR of the period carries its review number in the release record; the PI's adoption entries name them.

## 5. Health issues

1. **Order sentences without an all-$M$ statement (the CORR lesson).** v0.3.25 adopted "$E'''=o((a+M)^{-1/2})$" and three limit sentences on the strength of grids to $M=10^7$ and an $O$-argument that did not look inside the closed forms. The v0.3.26 round-2 revision then found a second, smaller instance of the same pattern in its own enclosure ($O(\kappa_2\log n/n)$ from a uniform factor, $10^{-5}$ of the term). Proposed rule for RECOG (to be written into CONVENTIONS or the cell template): **an asymptotic-order claim about a computed majorant is adoptable only with a term-by-term bound carrying explicit constants, valid for every $M$ in the stated range (the §3a pattern of the drift record); otherwise it is tagged `[NUM]` as a grid observation.** The v0.3.26 checker already has the shape for this (C19 reads the proof-table JSON); future checkers should require the proof-table gate for any new order sentence.
2. **Late-slip tests dominated by the reference tolerance.** The 73-slip containment tests of the start-offset and drift cells compare $|\varepsilon_k|$ with $E_k+L_{\rm tol}$; at the latest slips $E_k<L_{\rm tol}$, so the test is a consistency check only (recorded with the caveat both times). A sharper reference $L$ (longer orbits, or an independent estimate) is needed before any further envelope claim is "tested" at $M>10^5$.
3. **Notices.** Zero dispatched in six days while two of them gate grades. The v0.3.25 post-release PR #90 is review-accepted and unmerged since 27 Oct.
4. **Dependence on one Dyadic ceiling.** $K_\epsilon$ (98 %), $\gamma_2$ ($2C_7$ of $212.6$) and the B1-L2 rows all hang on $C_7$. Any Dyadic sharpening propagates; any Dyadic correction would too.
5. **The in-block residual.** $c_P(r)Q^\dagger$ at $r\ge3$ is $75$ % of the log-free envelope's constant at $r=5$ and was flagged as the next lever already in v0.3.25's records. It is the first thing to sharpen if the known-$a$ window is to improve by more than the $1.02$–$1.87$ gains of v0.3.26.
6. **GitHub hygiene.** Six stacked cell PRs whose heads are in `main` remain open; PR #90 unmerged; PR #103 (OFN advisory) and #104 (v0.3.26 post-release) open. Harmless, but the PR list no longer reflects the work queue.
7. **The release method is undocumented as a method.** See §4; a one-page `records/recog/RECOG_RELEASE_METHOD.md` (builder, checker with controls, variants, separate acceptances, transform, verification) would let another stream reuse it and would make the next release cheaper to review.

## 6. Research frontier after v0.3.26

| Lever | Where it bites | Kind | Dependency |
|---|---|---|---|
| In-block residual $c_P(r)Q^\dagger$ ($r\ge3$) and the start-offset slack $\tau\,{\rm half}(\omega S)$ | the dominant terms of $E^{(5)}$; the decoder windows | algebra + interval certificate; no long orbit | none external |
| A1c-Q1′ injectivity of the record map | OPEN R6 sub-item; the only open question on the record side | analysis on the $C^1$ fibers; margin criterion is `[SESSION/HEUR]` | none external |
| $K_\epsilon$ | $\gamma_2$'s $2C_7$ share | Dyadic bound on $\operatorname{Re}(\rho_7/z)$ along an orbit, or $C_7\le85.1$ registered | Dyadic (M1, N2) |
| B1 Stage C | R9 comparator-incompleteness windows | PI-machine computation (Arb) | Dyadic NF-REM machinery |
| R4 sub-item 2 (B3 census), R3 (B2) | the two remaining ACTIVE/PARTIAL geometric OPENs | PI-machine campaigns | E3A-3a engine |
| F5 / F6 (carrier side of R6) | the write-through question | scoping and registry audit | OFN v0.10 class C; RRF OPEN-B/E1/E2 |
| A2 typed involution ledger (R1, R5) | wording of §6.6–6.7; R1's `[HYP]` | algebra | Dyadic $R_0$ |

Ranking is the PI's. My reading: the first row is the cheapest certified gain and feeds everything downstream (decoder windows, readout precision); the second is the scientifically decisive one for R6 and may well end negative; the third is a notice, not a cell.

## 7. Recommended next governance actions (cheap, in order)

1. Merge PR #90 and PR #104; close the stacked cell PRs #59, #61, #63, #64, #71, #75 (content in `main`).
2. Dispatch the Dyadic requests N1, N2 (with N3, M1 attached) and the consumer notices N4–N6, M2–M4 in one batch, recording states on dispatch.
3. NUMGEN v1.21 claim audit and repin (micro-edit, structural maintenance).
4. Write the release method down (§5.7) and the order-sentence rule (§5.1) into CONVENTIONS or the cell template.
5. Then the next scientific cell per §6.
