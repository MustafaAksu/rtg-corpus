# DYAD owner review of v6.4.21 (reply to the co-owner note)

**Date:** 22 October 2026. **From:** Dyadic DSN owner (Claude). **To:** the PI and the atlas owner. **Status:** working record. It is not an amendment, a release or a notice.

**Reviewed:**
- `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` at tag `dyad-v6.4.21` (SHA-256 `a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d`);
- the stage-1 diff `dyad-v6.4.20..6622dcd`;
- `records/dyad/DYAD_COOWNER_NOTE_v6_4_21.md` §2;
- `records/dyad/RTG_DYADIC_v6_4_21_RELEASE_RECORD.md`.

Governing methodology: v1.4 (tag `methodology-v1.4`).

## 1. Answers to the co-owner note §2

| # | Item | Owner answer |
|---|---|---|
| 1 | Stage-1 diff (30 edits) | **Confirmed.** Every edit matches the current owner state: OPEN 3 CLOSED within scope; P4 = `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` with the R9 premise; OPEN 21 certifies the primitive remainder; the P2B v2 check is stated as coefficient equality, not byte identity; N11 is RECOG's adopted use; the OPEN 19 scope is $DG(0)=I$; the RAW-CUBIC caveat and the range $p\ge3$ hold. The §7 dependency split is correct: the static-offset identity and $\Delta_1,\Delta_2$ are self-contained, and the primitive-memory expansion uses R9, $c_{\rm iso}$ and $\Lambda_1$. The E-1 record correction (three grade changes in the P1 pass) is accurate. |
| 2 | $h_4$ field label | **Confirmed by a second route.** The atlas check `dyad_h4_archival_exact_check.py` was rerun here (EV-RUN; 5/5 exact; about 48 s). The new script `evidence/dyad/scripts/dyad_h4_real_route_check.py` composes $T^6$ in exact rationals in the real chart $(\rho,\eta)$ and maps the degree-4 part to the script's $(Z,\bar Z)$ frame (see below). It gives the same five coefficients, which are non-real, so the field is $\mathbb Q(i\sqrt3)$. Relative to the first route this is EV-INDEP: same definitions, different engine and chart. It does not re-derive the archival gauge convention. |
| 3 | R11 wording (§1 backbone entry, §6.5) | **Confirmed for RECOG R11.** RECOG v0.3.22 records OPEN R11 (`RECOG-OPEN-QUINTIC-FRAME`) as CLOSED (v0.3.2) at the final-chart ledger scope. What stays `[OPEN]` here is the identification of the historical fitted backbone. It reads as intended. A separate label clash was found in the process (finding F4 below). |
| 4 | §1 profile exception (§1 is about 1,510 words) | **Keep it for v6.4.21.** In the next owner release I intend to shorten §1 by stating each certified result once with its load-bearing qualifier and moving the proof-level detail to §6. The exception would then be dropped if §1 fits 200–400 words without losing a qualifier; otherwise it stays, with the reason in the header. No change now. |
| 5 | History phrases in live text | **Reviewed one by one** (84 matches of historical / superseded / former / previously / withdrawn outside Appendix A). Most need no change, and three wordings should be replaced in place; see the breakdown below. |

**Item 2 — `dyad_h4_real_route_check.py` details.**
- Script SHA-256: `dd06a1a20466dbe16da9c9b2e5bfe01a209decbedeed5a2c4a3ba33c783c1e6d`.
- Command: `python -B evidence/dyad/scripts/dyad_h4_real_route_check.py`, exit 0. The stdout SHA-256 is `5dbc63ba…8c09`.
- Negative control: `--control K` exits 1.
- The script also confirms that the linear part of $T^6$ is the identity and that its degree-2 part is zero.

**Item 5 — breakdown of the 84 history phrases.**
- **No change needed (about 75).** These fall into four groups:
  - names of historical *objects*, current statements about them (historical fit, historical backbone ansatz, historical RECOG pins, historical source);
  - `[COR]`/`[FAIL]`/`[RETRACTED]` lines that warn at the point of use against a wording consumers may still hold. Examples: the "iff $b\le4$" shorthand, the unqualified backbone map, the withdrawn P2 record. These stay;
  - Appendix E cells "historical (v6.4.x)", meaning evidence older than this ledger's records;
  - Appendix F classes.
- **Replace in place in the next owner release (3):**
  - "earlier statements omitting it are superseded" / "the earlier form without it is superseded" (§1 L75, §6.5 L533) → drop the sentence; the current statement suffices.
  - L27 "keeps its former heading tag" → "keeps its `[ENG]` heading tag".
- **Current-state defects** found during this pass: F1–F3 and F5 below.

## 2. New findings (current-state defects in v6.4.21)

These came in with the v6.4.20 release wording (owner responsibility) and were not in the closeout scope. All are wording or status errors. None changes a statement, grade, RID or OPEN status.

| # | Location (v6.4.21 line) | Defect | Proposed replacement |
|---|---|---|---|
| F1 | §7.0 table, Dyadic row (L1059) | Calls v6.4.20 "this edition"; the current edition is v6.4.21 | Row "Dyadic (this ledger) — v6.4.21, ADOPTED 22 Oct 2026 (this edition; SHA-256 in its release record); predecessor v6.4.20 `0b2d5a44…4852`, tag `dyad-v6.4.20`" |
| F2 | §7 notice-table intro (L1109) | "N16–N20 … prepared only after external verification of this edition's SHA-256; none is prepared in this edition" is out of date: v6.4.20's hash is externally verified (closeout §0), and N16–N21 are prepared and unsent (`records/dyad/DYAD_NOTICES_N16_N21.md`) | "N16–N21 are prepared and not yet sent (`records/dyad/DYAD_NOTICES_N16_N21.md`); states per recipient are recorded there and copied here when a receipt exists" |
| F3 | Appendix F intro (L1525) | Same stale clause ("after external verification of this edition's SHA-256") | "requested by notice N17 (prepared, not yet sent)" |
| F4 | §3 SG-15 (L361), §5 R11 row (L413), §6.11 (L465), §6.12 (L672), Appendix E (L1432) | "R11" here is **OPEN-M R11** (the OPEN-M-2B assembly formulas, cascade-gate conversion), not RECOG OPEN R11 (CLOSED). Unqualified, a reader can confuse the two, now that §1 and §6.5 say "RECOG R11 is CLOSED" | Write "OPEN-M R11" at each of these places. Add an Appendix C row: R11 = (i) RECOG OPEN R11, final-chart ledger, CLOSED v0.3.2; (ii) OPEN-M R11, cascade-gate/assembly formulas (OPEN-M v0.7.1) |
| F5 | §6.14 L-PHASE (L908) and §8 `DYAD-ART-LPHASE-P2B-PROV` (L1198) | "reviewer full replay pending" | Current state per the v6.4.19 release verification record (21 Oct 2026; not yet in the repository): G14 and the G15 main gate individually reviewer-replayed; the combined G14–G15 run and the separate-process M1–M4 exit codes NOT COMPLETED |

## 3. Replays done for this review (owner, EV-RUN)

- **v6.4.20 release package, from the repository alone.** `evidence/dyad/v6.4.20/` plus three files retrieved by the README's `git show` paths gives `SHA256SUMS.txt` 12/12 OK. `check_release_v6_4_20.py` R0–R11 ALL PASS, including two clean r2→final transforms with byte-identical results.
- **Tag identities.** The files at the three tags hash to the values in their release records:
  - `dyad-v6.4.19` → `40c9e63f…6ec9`;
  - `dyad-v6.4.20` → `0b2d5a44…4852`;
  - `dyad-v6.4.21` → `a412f34d…dc7d`.
- **v6.4.21 read-back (completion matrix C-4, repository side).** `main` at `7ff45a8` holds `a412f34d…dc7d`, equal to the tag and the release record. As C-4 notes, the project-side copy cannot be byte-read from a session.

## 4. Proposed next owner step

A small errata release v6.4.22 containing F1–F5, the three item-5 wordings, the §6.5/§8 citation of `dyad_h4_real_route_check.py`, and possibly the §1 reduction from item 4. It would be built on a `claude/dyad-v6.4.22` branch as a single stage-1 assertion-gated build with no compaction, followed by a change-focused review, a release record, PI adoption, merge and tag. **Not started.** It waits for the PI's go-ahead.

**Unchanged and carried:**
- the C-2 source files (deferred by the PI);
- N16–N21 (unsent; routed through the PI);
- the RAW-CUBIC historical identity and the eight unrecovered OPEN 9 definitions;
- FC-31 and FC-32;
- B-an and B-6 (OPEN 20);
- the combined G14–G15 replay.
