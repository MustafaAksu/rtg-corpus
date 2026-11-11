# DYAD v6.4.24 — backlog (preparation record)

**Date:** 3 November 2026. **From:** Dyadic DSN owner (Claude). **Status:** working record. It changes no DSN text, grade or RID, and it decides nothing. It lists what a later maintenance edition may carry. Scope boundary, agreed with the co-owner (3 Nov 2026):
- v6.4.24 carries the accepted interface changes and the S1 result, if S1 is accepted;
- the §1 compaction is deferred to v6.4.25 or later, as an independent editorial edition;
- S2 (L-PHASE row B) and S3 (OPEN 20 stage 3) are separate scientific work. S3 stays not authorized.

Governing edition: `dyad-v6.4.23` (`9f874ccc…25cb`). Line numbers refer to it.

## A. Consumer register (§7.0, §7) — stale rows

| Row | Now | Current state | Source |
|---|---|---|---|
| Triadic Birth-Lift (§7.0 L≈1081; §7 export line) | v1.6.1, "§7.1 repins to Dyadic v6.4.13 (N2 answered)" | Triadic v1.7 (`triad-v1.7`) repins its five Dyadic imports to v6.4.23 (`DYAD-THM-C21`, `DYAD-ALG-BRIDGE-LEMMA`, `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` item 1, `DYAD-ALG-PROTECTION-MATRIX`, `DYAD-DEF-PRIMITIVE-MAP`); Triadic filed no notice to DYAD | `triad-v1.7` §7 (import records) |
| RECOG, NUMGEN, OFN, ATLAS | as in v6.4.23 | update only when the receivers answer the v6.4.23 notices (RECOG re-check with $c'_Q=0.36916$; NUMGEN disambiguation of $q_*$) | `pipes/*/20261030-DYAD-v6-4-23-adopted.md` |
| GEN, DZT, AZ, RRF, RER, ER-2B, OPEN-M | as in v6.4.23 | update when the receivers record the 3 Nov notices | `pipes/*/20261103-DYAD-notices-n16-n21.md` |

## B. RID candidates (Atlas DYAD.X4: results used downstream without an owner RID)

| Statement | Location (v6.4.23) | Grade | Note |
|---|---|---|---|
| The map is not globally area-preserving ($\det DT=1+(e^\rho-1)\cos\eta$) | §1 L63, §6.1 L447 | `[THM]` | cited by OFN (non-symplecticity). **Grade question (3 Nov 2026):** the recovered bridge note grades the same statement `[ALG]` (§1, §8 ledger). It is a direct Jacobian computation, replayed in gate B2 of the bridge-note check. Owner proposal: register the RID as `[ALG]`, with the bridge note and the replay as its sources. This is a regrade of the displayed tag only, with no change of content, and is recorded as such in the v6.4.24 change matrix |
| $p=6$ linear order ($\lambda=e^{i\pi/3}$ has order exactly six) | §6.6 L543 | `[ALG]` | regraded from THM at v6.4.20 |
| Homological resonance condition ($a-b-1\equiv0\pmod6$) | §6.6 L545 | `[ALG]` | |
| Cubic radial rate across $p$ ($\Re\mu^Z_p=-p\sin^2(\pi/p)$) | §6.6 L549 | `[ALG]` `[import: RECOG-ALG-NU3-CLOSED-FORM]` | custody question: a Dyadic RID for an evaluation of a RECOG result, or a pointer to RECOG's RID only |

Owner decision needed per row: register (name, scope) or record "no RID; cite the section". A new RID is a registration only; it changes no statement.

**Tentative decisions (3 Nov 2026; co-owner proposal, owner agrees; final at the v6.4.24 candidate review):** DYAD RIDs for the first three rows (names to be proposed with the candidate). For the cubic radial rate across $p$: no new DYAD RID. The entry stays a statement-level import of `RECOG-ALG-NU3-CLOSED-FORM`, evaluated in the declared $K_p$ family, unless an independent Dyadic proposition and proof are separated out.

## B2. Items from the Triadic v1.7 reading (3 Nov 2026)

- **`DYAD-DEF-PRIMITIVE-MAP` "provisional" label (§1 L47).** Triadic v1.7 §7.1 records that the definition "is still provisional" at `dyad-v6.4.23`. Map custody is settled: OFN CUST-O09-01 is answered, the Genesis alias is recorded, and the Programme adopts $T$ as the effective model (PROG-P0-MAP; selection is OPEN-P0). Owner question for v6.4.24: replace the bare "provisional" with what it means, e.g. `[scope: adopted effective model; selection open (OPEN-P0)]`. The definition itself, the RID and all consumer imports are unchanged. If the wording changes, Triadic, Genesis and OFN get one informational notice.
- **Shared source, recovered 3 Nov 2026.** `dyad_triad_antisymmetric_bridge_v1_1.md` (DYAD-ART-BRIDGE-NOTE) is cited by Dyadic §2 (downstream handoff) and by Triadic §7.1 (historical pin route).
  - The PI uploaded it unchanged: `upload/dyad-bridge-note/`, branch `miss1`, commit `47f807c`, SHA-256 `5ddebfe46b5572761a5154a05712fbcfe4e675f912430ee7d6bfcf0d93f4e875`.
  - Hash check, identification and exact replay are in `records/dyad/DYAD_UPLOAD_HASH_CHECK_20261103_BRIDGE_NOTE.md` (branch `claude/dyad-bridge-note-intake`). Both recovery lists are updated there.
  - For v6.4.24:
    - §8 `DYAD-ART-BRIDGE-NOTE`: add the path and hash, with the availability note "PI-supplied 3 Nov 2026, identified by content" (finding F3).
    - Any DSN text that quotes the component formula Δ_cT_η uses the general-K form, 2cb + 2K e^ρ sinh(ca) − 2K cos η sin(cb). The note prints the K = 1 form (finding F1). The odd-channel statement is unaffected.
- **Triadic v1.7 import scope** (for the §7 consumer row): five RIDs repinned to v6.4.23 after a claim-level re-read; `DYAD-ALG-KP-FRAME-SCALE` and the isolated-dyad results (Z₆ generator, Lemma F, OPEN 20) are explicitly not imported. This is consistent with the N20 closure.

## C. Science feeding v6.4.24

- **S1 — OPEN 21 with the unconditional sharpened R9 rows** (selected; work item).
  - The co-owner's rational pre-check (3 Nov) uses the existing $K'_j$, $w_j$ and RECOG-THM-R9-SHARPENED-ROWS $(259.2,\tfrac1{400})$, $(81.49,\tfrac1{1600})$. It gives $K_A\approx19.679640\to19.68$ and $K_B\approx6.356467\to6.36$, against $35.32$ and $8.83$ now.
  - Form: a **new, separate result** (new RID). `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` keeps its rows and its `[assuming: RECOG-THM-R9-MEMORY]`.
  - The new result keeps the R9 dependency on the sharpened rows, the chart/primitive separation and every hypothesis. It never uses the -C7 rows.
  - Plan: design note → exact-rational certificate with negative controls → co-owner review → candidate for v6.4.24.
  - **Status (3 Nov 2026):** done through review. `records/dyad/DYAD_S1_OPEN21_SHARP_ROWS_DESIGN.md`; RID `DYAD-THM-OPEN21-SHARP-ROWS` accepted by the co-owner (PR #150 reviews `5748327144`, `5748500129`); $S_A=19.680$, $S_B=6.357$.

- **S3 — OPEN 20 analytic branch: record the sectorial pilot's current state in the DSN** (PI instruction, 3 Nov 2026: Dyadic work on the pilot is done in rtg-corpus and its outputs are recorded in the Dyadic DSN; LIT is used only through `pipes/LIT/` requests).
  - The DSN at `dyad-v6.4.23` does not mention the pilot. Its stages so far live only in records:
    - stage 1, exact preparation (OWNER-RUN);
    - stage 2, `[NUM]` scouting, Borel scale INCONCLUSIVE;
    - the LH2012 literature basis at SESSION scope (LIT INF-005 to INF-008; assessment §5);
    - the stage-3 a-priori route check of 3 Nov 2026 (design record §8).
  - Proposal for v6.4.24:
    - one `[SESSION]` progress paragraph under OPEN 20 B-an, stating what each stage established and what it did not;
    - §8 artifact entries for the stage scripts and outputs, with hashes.
  - B-an and B-6 stay ACTIVE. No statement is regraded. No LIT result is imported as an RTG result; LIT sources are cited by LIT-ID@version:label where they are used.
  - **Added 4 Nov 2026:** one `[SESSION]` sentence on the local orbit structure along Γ_σ (LIT INF-014, INF-015; owner check `records/dyad/DYAD_OPEN20_AN_LH2012_OWNER_ASSESSMENT.md` §6), with its qualifications. It is not a B-an statement.
    - The sentence keeps four limits: complexified germ only (on the real slice \|w/z²\| = 1/\|z\| → ∞); FL-Q1 and IMRN-Q1; IMRN read from arXiv v1, not the journal version; and the 3-sum identification as a separate LIT step. With these open, it is not a `[THM]`.
    - Candidate `[ALG]` line: P′(u) = α(c₄₀ + μu) identically (2A = αμ, B = αc₄₀), with §8 entries for `dyad_open20_lit_inf014_inf015_hypothesis_check.py` and the LIT-ID@version:label citations (co-owner proposal, PR #174 comment `6626218705`).
  - **Status (3 Nov 2026):** route check done (`evidence/dyad/open20-an/stage3-route/`). The a-priori route of INF-009/010 cannot reach the radius the jump needs. Stage 3 itself stays not authorized; a revised stage-3 design comes first.

## C2. Schedule

Checkpoint **10 November 2026** (co-owner proposal, 3 Nov); held on 11 November, see §C3. If RECOG and NUMGEN have answered the v6.4.23 notices by then, their answers are included. Otherwise they are recorded as open dependencies and the v6.4.24 candidate is prepared. Until then: the X4 decisions and the v6.4.24 change matrix. This is a maintenance schedule, not a scientific requirement.

## C3. State at the checkpoint of 11 November 2026

Held one day after the planned date. Sources: `records/dyad/DYAD_INBOX_20261111_OWNER_DISPOSITION.md`; live state from `tools/orient.py` at `main` `fe73d56`.

**Answers to the v6.4.23 notices and the 3 Nov notices:**

| Receiver | State | For the v6.4.24 register (§7.0, §7) |
|---|---|---|
| RECOG | answered: `recog-v0.3.27` imports BRIDGE, SPIRAL-REM and C7-SHARP; c′_Q = 0.36916 used throughout | row at `recog-v0.3.27` |
| GEN | answered: `gen-v2.10`; `DYAD-ALG-NU5-P5` label corrected, claim-level pin `dyad-v6.4.23` §6.11 | row at `gen-v2.10` |
| AZ | answered: `az-v0.7` pins `dyad-v6.4.23`; owner RIDs used | row at `az-v0.7`; Appendix F re-read |
| Programme | `programme-v1.4` adopted | companion pin |
| NUMGEN, OFN | **open** | recorded as open dependencies; rows unchanged |
| Triadic | bridge-note notice open; v1.7 row as in §A | row at `triad-v1.7` |
| DZT, ER-2B, RER, RRF, UVM | open | rows unchanged |

**Additions to the candidate scope since 3 November:**
- S3 paragraph: the stage-3a verdict with its chart-relative scope and LIT's grid-free bound (design record §8); the INF-014/015 sentence with its four limits; the `[ALG]` line P′(u) = α(c₄₀ + μu).
- §8 artifacts: the stage-3 route check, the INF-014/015 hypothesis check and the bridge-note check, with hashes.
- No DYAD RID for RECOG's c_J and c_7 (disposition record, item 3).

**Not in v6.4.24, recorded for later:**
- a sharper row-A constant built on `RECOG-ALG-A1C-JET-REMAINDER-BOUNDS` (optional; needs its own certificate);
- the owner check of AZ §4.1.1 (answer to AZ by pipe; a DSN change only if the owner text is found unclear);
- OPEN 20 stage 2b and the 3b design (design record §9).

**Schedule proposed by the owner** (maintenance schedule, not a scientific requirement):
1. change matrix and X4 RID names: with the candidate;
2. candidate build (assertion-gated script, checks, negative controls) and draft release record on `claude/dyad-v6.4.24`;
3. co-owner review; corrections; read-back;
4. PI adoption, merge and tag.

NUMGEN and OFN answers are included if they arrive before step 3; otherwise they stay open dependencies in the release record.

## D. Not in v6.4.24

- §1 compaction (two-stage editorial edition, v6.4.25 or later).
- S2 L-PHASE row B; S3 OPEN 20 stage 3 (not authorized); N=432.
- OPEN 18 footprint `[DEF]`; RAW-CUBIC historical identity (DYAD.X11); source recovery (`DYAD_SOURCE_RECOVERY_LIST.md`).
