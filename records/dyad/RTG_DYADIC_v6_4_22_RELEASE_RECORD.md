# RTG Dyadic Oscillator DSN v6.4.22 — release record

**Status:** DRAFT — prepared for the change-focused review; **not adopted**. This record becomes frozen at adoption; the adoption section (§6) is filled in only after an explicit PI decision.
**Prepared by:** Claude (Dyadic DSN owner), 23 October 2026, branch `claude/dyad-v6.4.22`.
**Authority:** co-owner review of 23 Oct 2026 on `records/dyad/DYAD_OWNER_REVIEW_v6_4_21.md` (PR #8): `OWNER REVIEW ACCEPTED — v6.4.22 ERRATA DRAFT AUTHORIZED`. That decision accepted F1–F5, the three wordings and the h₄ evidence reference. It extended F4 to every live R11 use, classified by source rather than by blind replacement, and excluded the §1 reduction from this release.
**Governing methodology:** DSN Methodology v1.4 (tag `methodology-v1.4`).
**Predecessor:** v6.4.21, tag `dyad-v6.4.21`, SHA-256 `a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d`.
**Official state unchanged:**
- v6.4.21 is the governing edition.
- OPEN 20 is PARTIAL; B-an and B-6 are OPEN.
- N16–N21 are prepared and not sent.

## 1. Build

| Stage | File SHA-256 | Tool | Check |
|---|---|---|---|
| Adopted v6.4.21 | `a412f34d…dc7d` | `git show dyad-v6.4.21:dsn/RTG_DYADIC_OSCILLATOR_DSN.md` | — |
| v6.4.22 candidate | `c6cb222f6f6f58a5d3c1fe269f8b2b86c62131657f464a2e55d09e362cada95a` (258,927 bytes, 1,570 lines) | `evidence/dyad/scripts/build_dyad_v6_4_22.py` (37 assertion-gated edits, one stage, no compaction) | `evidence/dyad/scripts/check_dyad_v6_4_22.py`: C0–C8 ALL PASS |

**Reproduce:**
```
git show dyad-v6.4.21:dsn/RTG_DYADIC_OSCILLATOR_DSN.md > v6421.md
python -I -B evidence/dyad/scripts/build_dyad_v6_4_22.py v6421.md cand.md log.json   # -> c6cb222f…a95a
python -B evidence/dyad/scripts/check_dyad_v6_4_22.py --base v6421.md --cand dsn/RTG_DYADIC_OSCILLATOR_DSN.md
python -B evidence/dyad/scripts/check_dyad_v6_4_22_controls.py --base v6421.md --cand dsn/RTG_DYADIC_OSCILLATOR_DSN.md
```

Diff: `git diff dyad-v6.4.21 -- dsn/RTG_DYADIC_OSCILLATOR_DSN.md` (38 insertions, 29 deletions). Every edit, with old and new text and their hashes, is in `evidence/dyad/v6.4.22/build_log.json`.

## 2. Changes

| Key | Location | Change |
|---|---|---|
| F1 | §7.0 Dyadic row | v6.4.22 as this edition; predecessor v6.4.21 with hash and tag; earlier editions by tag. Before: v6.4.20 was called "this edition" |
| F2 | §7 notice-table intro | N16–N21 prepared and not sent (`records/dyad/DYAD_NOTICES_N16_N21.md`); the four states per recipient are kept there. "Where recorded" now refers to the last update of each row |
| F3 | Appendix F intro | repins requested by N17 (prepared, not sent) |
| F4-01…16 | §1 (2), SG-15, SG-19, §5, §6.2, §6.11 (3), §6.12 (3), §6.14 (2), §7, Appendix E | each bare "R11" names its owner, classified one by one from the source text: **OPEN-M R11** (OPEN-M v0.7.1 "R11 — OPEN-M-2B assembly formulas": cascade-gate conversion, $\theta_f=2\pi/3$, source formula $\vert H\vert_B=hr^2$, factor $3/4$) — 12 edits; **RECOG R11** (RECOG v0.3.22 OPEN R11, `RECOG-OPEN-QUINTIC-FRAME`, final-chart ledger, CLOSED v0.3.2) — 4 edits (SG-19 violation clause, §6.14 boundaries ×2, §7 consumer line). The four places that already said "RECOG R11" (§1 ×2, §6.5, §6.9) are unchanged |
| F4-17 | Appendix C | new row R11: (i) RECOG OPEN R11; (ii) OPEN-M R11; guard "always written with its owner" |
| F5 | §6.14 L-PHASE (iv); §8 `DYAD-ART-LPHASE-P2B-PROV` | "reviewer full replay pending" → G14 and the G15 main gate each reviewer-replayed separately (v6.4.19 release verification, 21 Oct 2026); the combined G14–G15 run and the separate-process M1–M4 exit codes not completed |
| W1, W2 | §1 one-block burst; §6.5 half-power `[COR]` | the "earlier … superseded" sentences removed; the statements themselves are unchanged |
| W3 | tag tables | §6.13 "keeps its former heading tag" → "keeps its `[ENG]` heading tag" |
| H4a–d | §1 OPEN 13; §8 `DYAD-ART-NORM-P6`; Appendix E.1/E.2 `DYAD-ALG-LIEGAUGE-NORM` | second-route exact check `evidence/dyad/scripts/dyad_h4_real_route_check.py` (SHA-256 `dd06a1a2…1e6d`) cited beside `dyad_h4_archival_exact_check.py` |
| ED-1…8 | header (title, date, status, supersedes, release record), Appendix A entry, Appendix G note, footer | edition lines of a DRAFT candidate |

**Not changed:**
- no RID, grade, statement, scope or OPEN status;
- §1 length (profile exception kept; the reduction is a separate future simplification);
- Appendix A history (one entry inserted);
- Appendices B and D.

The new Appendix C row cites `RECOG-OPEN-QUINTIC-FRAME`. That is a RECOG identifier, which is why `dsn_lint.py` reports one new RID string; it is not a Dyadic RID.

## 3. Checks (OWNER-RUN, 23 Oct 2026)

| Gate | Content | Result |
|---|---|---|
| C0 | base = v6.4.21; candidate = fresh build | PASS |
| C1 | two clean builds byte-identical (file and log) | PASS |
| C2 | base Appendix A kept byte-for-byte plus one inserted entry; outside it, +1 line (Appendix C row) and every changed line carries a logged edit's new text | PASS |
| C3 | RID-tag set and sequence equal; Dyadic RID strings equal; no grade tag or math span removed; added ones belong to logged edits | PASS |
| C4 | every live R11 has its owner; context check (OPEN-M: cascade / $h$ / $\theta_f$ / factor / source formula / gate; RECOG: final-chart / chart ledger / CLOSED / reconciliation); counts OPEN-M 13, RECOG 9 | PASS |
| C5 | stale wordings (F1–F3, F5, W1–W3) absent from live text | PASS |
| C6 | title, DRAFT status, Supersedes v6.4.21 + hash, release-record path, Appendix A heading, one footer, one `AI_CONTEXT_CORE_END` | PASS |
| C7 | §2 "Status:" lines identical to v6.4.21; OPEN 20 sentence present | PASS |
| C8 | cited h₄ script present with the cited hash; it exits 0 and its `--control K` exits 1 | PASS |

- **Negative controls** (`check_dyad_v6_4_22_controls.py`): P0 passes, and all 11 controls are caught on their intended gate.
  - N0: one byte, rebuild → C0.
  - Q1: bare R11 → C4.
  - Q2: OPEN-M occurrence relabelled RECOG → C4.
  - Q3: stale replay wording → C5.
  - Q4: constant → C3.
  - Q5: grade tag → C3.
  - Q6: RID tag → C3.
  - Q7: older Appendix A entry → C2.
  - Q8: §2 Status line → C7.
  - Q9: header ADOPTED → C6.
  - Q10: cited script hash → C8.
- **Reports:** `evidence/dyad/v6.4.22/check_report.json`, `negative_controls_report.json`, `size_report.txt`.
- **Limits:** C2 checks that each changed line carries logged text. It does not prove the edits are correct; the review does that. The C4 context words are a heuristic aid to the one-by-one classification, which is documented in §2. A passing check authorizes nothing.

## 4. Size (`tools/dsn_lint.py`; informational)

| Metric | v6.4.21 | v6.4.22 candidate |
|---|---:|---:|
| Bytes | 256,508 | 258,927 (+0.9%) |
| Lines | 1,561 | 1,570 |
| §1 words | about 1,500 | 1,507 (profile exception kept) |
| Appendix A characters | 3,899 | 4,804 |
| Footer lines | 1 | 1 |

## 5. Evidence levels

| Level | Content |
|---|---|
| `OWNER-RUN` | build, C0–C8, the 11 negative controls; `dyad_h4_real_route_check.py` (exit 0, `--control K` exit 1) |
| `REVIEWER-REPLAYED` | none yet for v6.4.22. The co-owner review compared the h₄ script and recommended running it separately |
| `REVIEWER FULL REPLAY NOT COMPLETED` | everything new in v6.4.22. Carried: the combined G14–G15 run (v6.4.19) |

## 6. Adoption

Not adopted. After the change-focused review, an explicit PI decision is needed. Only then would the following be done, in this order:
1. this section is filled in;
2. a status-lines-only publication commit gives the final hash (header status, Appendix A heading, footer);
3. the PI merges with a merge commit and creates the tag `dyad-v6.4.22` with the hash;
4. `BASELINE.md` is updated;
5. a notice delta is added to `records/dyad/DYAD_NOTICES_N16_N21.md` if consumers need one. F4 and F1–F3 concern wording only; the owner sees no consumer action.
