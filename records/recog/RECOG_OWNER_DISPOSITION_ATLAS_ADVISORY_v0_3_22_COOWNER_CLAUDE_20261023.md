# RECOG — owner disposition of the atlas advisory for v0.3.22 (co-owner Claude)

**Date:** 23 October 2026 · **From:** RECOG co-owner (Claude) · **For:** the PI and the second RECOG co-owner
**Status:** `[SESSION]` disposition proposal. The PI decides every row; nothing is adopted here. The other co-owner's disposition is reconciled by the PI.

**Answers:** `records/recog/ATLAS_ADVISORY_RECOG_v0_3_22.md` (FINAL PROPOSAL v1.0) §3, and the PI's five questions of 23 Oct 2026.

**Read:** `main` at `92fc09f`, including:
- `records/recog/RECOG_SOURCE_RECOVERY_LIST.md`;
- `records/recog/RECOG_OWNER_SELF_REVIEW_20261023.md`;
- RER v0.2 §G9 (r4.11 note);
- Dyadic v6.4.22;
- NUMGEN v1.20.8.

## 1. Answers to the five questions

**Q1 — FC-RECOG-21.** It joins the successor, but as a **separately gated science block inside stage 1**, not as a maintenance edit.
- It gets its own proposed RID, `RECOG-THM-A1A-PHASE-EXISTENCE-U`.
- It gets its own proof cell. [G] §5 already supplies a written proof; it needs a check against v6.4.22 of the lift convention (§7.0a I1–I2), the domain (base points in $U$; $F(U)\subset U$), the sum indexing and the amplitude inversion.
- It gets its own review verdict.
- The release record lists it under "new science".
- Existing RECOG-RESULT-A1A-PHASE-EXISTENCE-NG and RECOG-RESULT-A1A-CD-AGREEMENT stay unchanged as the NUMGEN-route records.
- **Decoupling rule:** if its review is not complete when the maintenance rows are ready, the successor is released without it, and FC-21 follows in a release of its own. Holding a small verified result back adds no evidence. Mixing it into maintenance without its own verdict would hide new science. The gate avoids both.

**Q2 — FB-RECOG-14.** Both.
- **In place:** "$|\mu|/|c_{05}^{\rm raw}|\approx41.27$ (raw six-step frame); post-$H_2$ $|\mu|/|a_{05}|\approx59.12$".
- **Correction record:** a one-line Appendix A entry pointing to the release record, which keeps the original sentence and why it was ambiguous.
- **Rounding:** $|G|=\sqrt{481897}/90720$, displayed as $\approx0.0076520$. The windows stay $|G|/517$ and $|G|/163$ with $\approx$ displays.

**Q3 — notice states.** RECOG records only confirmed states.
- **G3-RER: received.** RER v0.2 §G9 (r4.11) records `RECOG_G3_NOTICE_TO_RER_20261020.md`, SHA-256 `53341b9a…b4b5` (matches the file in `records/recog/g3/`), "received by the RER preparer via the PI on 21 Oct 2026". It records RECOG v0.3.21 as current authority and keeps its v0.3.20 pins.
  - received = 21 Oct 2026 (RER record);
  - sent = via the PI, on or before 21 Oct (implied by the receipt; no dispatch time recorded);
  - statement accepted = recorded by RER (G9 note);
  - adopted use = none new (pins unchanged).
- **G3-OFN and G3-RRF:** unconfirmed. They stay "prepared" until the PI confirms.
- **v0.3.22 notices:** N-D, N-NG and N-O/R/E are prepared and unsent.
- **Dyadic N19/N21 to RECOG:** prepared by Dyadic and not sent. Their content is used as input only, not as a receipt.

**Q4 — the five review items.** All five go into stage 1:
- R10 status wording (under FA-01, stage 1 part);
- Dyadic tag-form change (under FB-11);
- line-number pins (FB-11);
- E-0322-1 (header);
- RF-1 row closure (FB-17).

The R10 wording is a status edit, not layout. It belongs in stage 1 so that stage 2 sets no status.

**Q5 — research order.** I agree with the proposed order:
1. FC-21;
2. R6. Between the two R6 options I prefer **F5 first**, because it is RECOG-internal and needs no upstream interface. The W1–W5 network feasibility depends on RRF OPEN-B/E1 and runs when RRF moves;
3. R4 or R3, whichever upstream interface opens first.

FC-22 and FC-24 are short follow-ons; they are deferred in the table below. The PI ranks.

**v0.3.5 mismatch.** The session file `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_5.md` (`9dd73601…6ab1`) has the header "Freeze status: v0.3.5 freeze candidate, 28 Sep 2026 … The final freeze hash is recorded by the external release record after the consistency pass". It is the pre-freeze candidate text, not the frozen `3ba74002…abd6`, which this session never held. The frozen bytes are not recovered; record them as missing.

## 2. Disposition table (§3 of the advisory)

| row | decision | reason | location / RID | validation | consumers |
|---|---|---|---|---|---|
| FA-RECOG-01 | **accept** (stage 2); R10 wording and other status edits in stage 1 | v1.4 §1.1; no live obligation lost | header; R7–R11 blocks; §6.16 F2 pointers; §9; App. A; SG order | `check_compaction.py` with a RECOG-profile calibration and the negative controls of advisory §1.2; must-stay-live list checked by the review | — |
| FA-RECOG-02 | **accept** | NUMGEN v1.20.8 registers both items with unchanged statements and grade | §6.13b imports; §7 A1a rows; header → `NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-INF1` at `numgen-v1.20.8`; INF-1 `Depends on:` cites `-PRIMITIVE-LIFT`, `-L-BACKBONE`, `-L-MONO`, `-L-PHASE`; $U$ vs $U\cap U_{\rm NUMGEN}$ kept; tracking keys and A1a-G1 text go to the release record | source read at the tag (`EV-SRC-READ`); gate: no `RID unavailable` left in A1a imports, NUMGEN strings occur only at the import sites | NUMGEN (A1a-G1 closed) |
| FA-RECOG-03 | **accept** as revised by [G] | the guard stays true; routing and use wording are stale | SG-R10, §6.13 (keep guard; add $\lvert M-c_{\rm iso}q_0\rvert\le\lvert G\rvert q_0+C_2q_0^2$ per row, $C_z$, normalized $q$ — follows from R9 since $\lvert\Lambda_1\rvert\le\lvert G\rvert$); §6.14 "R9 budget" named the degree-≥7 partial budget $2C_7q_0^2$; §4 p-family row; SG-R14 note (T1/T2 in adopted use) | one-line derivation in the release record; review | DYAD |
| FA-RECOG-04 | **accept** | DYAD v6.4.22 §1 lists the winding fixed points and states agreement | §6.3 | source read | DYAD |
| FA-RECOG-05 | **accept** | N11 adopted use recorded by DYAD; current consumer editions | §7.2 current table (N11 adopted use; N13 at its pin); §7.3 editions (DYAD v6.4.22, RRF v0.8.4, RER v0.2, OFN v0.10); history moves to records | review against the Dyadic notices file and consumer DSNs; five states kept separate (Q3) | DYAD, RER, RRF, OFN |
| FA-RECOG-06 | **accept** | successor built under v1.4; v0.3.22 correctly under v1.3 | header; §6.13b grade-principle pointer → v1.4 §3.4 (M13-C04) | — | — |
| FA-RECOG-07 | **accept; largely met** | hand-over placed 174/174 OK | §8 paths into `records/recog/`, `evidence/recog/`; missing items recorded by PI decision; frozen v0.3.5 bytes recorded missing | `RECOG_SOURCE_RECOVERY_LIST.md` | PI |
| FA-RECOG-08 | **accept**, owner review per block in stage 1 | v1.4 §3.4 pairing rule | the 19 listed blocks: pair each `[RESULT]` with exactly one `[from: TAG]` (the canonical tag of its load-bearing input); split heterogeneous ones (L927 NUM+ALG, L1003 THM/ALG/RESULT); L487 `[from: ALG conditional]` → `[from: ALG] [assuming: …]`; registry-relative and nonclaim wording kept | per-block table in the release record; lint scan for line-leading `[RESULT]` without `[from:` | — |
| FA-RECOG-09 | **accept** | §6.7 governs | §5 radial-neutrality row: $6\gamma t^6+O(t^8)$ | — | — |
| FB-RECOG-10 | **accept** | identifiers only; content checked claim by claim | §7 rows → `DYAD-DEF-PRIMITIVE-MAP`, `DYAD-DEF-CRITICAL-CURVE`, `DYAD-ALG-QC-CRITICAL-AMPLITUDE`, `DYAD-ALG-ISP-MAPS`, `DYAD-ALG-SIXSTEP-CUBIC-JET`, `DYAD-ALG-RAW-ANGULAR-MEAN`; §6.15c $Q_c$ citation; non-symplecticity stays without RID; L1154 process sentence removed | source read at `dyad-v6.4.22` | DYAD |
| FB-RECOG-11 | **accept**, with three additions | claim-level audit, not a blind repin | (i) audit against `dyad-v6.4.22`/`numgen-v1.20.8`, historical producer pins labelled where load-bearing; (ii) the five line pins "§6.14 lines 806–809 / 843–850" → RID + section anchor, with the v6.4.18 A1a-E2 check kept as historical evidence; (iii) quote current owner tag forms (`[THM] [assuming: RECOG-THM-R9-MEMORY]`; `[ALG] [scope: formal second order; remainder certified separately, OPEN 21]`) and state equivalence to the v6.4.18 forms; (iv) OPEN 21 constants re-read: unchanged | audit table in the release record | DYAD, NUMGEN |
| FB-RECOG-12 | **accept** | clarity; RIDs immutable | §1 L84 `[OPEN]` → `[HYP]` (registered under R6); LEADING-RETURN-EQUIVARIANCE authoritative at §6.12, pointers elsewhere; `E2C-ENG-SPLIT-REFINEMENT` keeps its identifier text with a custody note "RECOG artifact" (no rename) | — | — |
| FB-RECOG-13 | **accept in part** | priority to externally consumed claims | new proposed RIDs: `RECOG-THM-R9-COMPARATOR-INCOMPLETENESS` (§6.13a corollary; exported §6.9, used by R6), `RECOG-ALG-SWAP-ODD-RHO` (§6.4 lemma; OFN-facing R1 sub-item); the radial identity $\Re(\bar\lambda\nu_3)=-\sin^2(\theta/2)$ named as a sub-statement of `RECOG-ALG-NU3-CLOSED-FORM` (matches DYAD's attribution); P2 corollaries as named sub-statements of their RIDs; **defer** the rest (radial-fate law, fixed-point inventory, finite ledger, uncoupled pair, finite-block identity stays internal) — next step: assign when a consumer cites them | RID-set gate in the stage-1 checker | OFN, DYAD, RRF |
| FB-RECOG-14 | **accept: both** (Q2) | frame label in place plus correction record | §6.13 L685; $\lvert G\rvert$ displays L703 ff.; windows L713–L714 | exact values $41.2694355\ldots$, $59.1194304\ldots$, $\sqrt{481897}/90720$ rechecked | — |
| FB-RECOG-15 | **accept** | frame rule | §6.10 L620, R2 L134 cite `DYAD-ALG-KP-FRAME-SCALE`; NU3 and $\Re\mu_p$ tagged $Z$-frame; §6.2 L457 restricted to the tangent-to-identity comparison | $\cot^2(\pi/6)=3$ check | DYAD |
| FB-RECOG-16 | **accept**, with the "must not" list verbatim | the atlas R-L5(i) overstatement is excluded | §6.14 L795: $j^6S_h=j^6R_0$; reference DYAD-THM-SMOOTH-EMBEDDING at germ scope; R1, RRF OPEN-A, OPEN-OFN-OPA stay open | review | DYAD, RRF, OFN |
| FB-RECOG-17 | **accept** | live file current-only; RF-1 answered by RRF v0.8.4 | §7.1/§7.2 notices → current notice table; history to `records/recog/`; RF-1 row closed (RRF imports W3 verbatim with RID); G3 states per Q3 | — | RRF, RER, OFN |
| FB-RECOG-18 | **accept** | custody already settled | §6.10 L622, R2 L127, §7 L1135: one sentence; "recommended for Dyadic" removed | — | DYAD |
| FB-RECOG-19 | **accept, minimal**: notation line only | a rename risks errors in exact formulas | §6.13b: one line stating that $M$ (block count) and $M(\cdot)$, $M_W$ (memory) are distinct; the new FC-21 block uses $N$ for the block count | — | — |
| FB-RECOG-20 | **accept; met** | inventory exists | §8 rows get repository path and access state; superseded revisions marked superseded | recovery list | PI |
| FC-RECOG-21 | **accept**, gated science block (Q1) | verified independently by both co-owners; [G] written proof | new proposed `RECOG-THM-A1A-PHASE-EXISTENCE-U` in §6.13b; premises DYAD-THM-LPHASE-ROWA-REMAINDER (row A), RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, RECOG-THM-A1A-LIFT-ALIGNMENT, finite-block identity; existing (a), (b′) unchanged; "not supplied" list of the advisory copied as scope | proof cell plus its own review; exact-rational sanity script for the tail constants (optional) | NUMGEN, DYAD (FC-DYAD-32) |
| FC-RECOG-22 | **defer** | missing: the first-passage index definition, eventual monotonicity of $\Theta_m$, and the vanishing-overshoot step | — | next test: a lemma with a fixed first-passage definition on the $C_z$ track | NUMGEN |
| FC-RECOG-23 | **route to GEN**; no RECOG edit | GEN owns the conclusion | — | GEN checks its map, block action and domain | GEN |
| FC-RECOG-24 | **defer** | missing: frame match between $S_h$ (chart) and $R$ (raw lifted chart) at second order | — | next test: compute $j^2R$ in the B-section frame and compare with $c=-(3+i\sqrt3)/8$ | RRF |

**Routed items (§2.4):**
- GAP-LOCK Lemma 3 use and the explicit-domain inputs → NUMGEN, through the PI, informational;
- the phase-moment retest → GEN;
- VF-1: accept as an identifier-only edit in stage 1 (cite `DYAD-ALG-NF6-DEG10`).

## 3. Build plan (for the PI's go/no-go)

- **Stage 1** is built on `claude/recog-v0.3.23-stage1`. It contains:
  - the accepted rows above;
  - the five Q4 items;
  - E-0322-1;
  - FC-21 as a separately marked block.

  It is built by an assertion-gated script against `recog-v0.3.22`. The intermediate hash is recorded.
- **Stage 2** is built on the same branch. It is layout only, with a movement map, checked with `tools/check_compaction.py` calibrated on the RECOG profile.
- **Release record:** `records/recog/RECOG_v0_3_23_RELEASE_RECORD.md`.
- **Version number:** v0.3.23 is a placeholder; the PI fixes it.
- **Branch push:** this session currently has read-only repository access. To push the `claude/*` branch it needs push access, or the PI uploads the built files.
