# OFN v0.11 — tag verification

**Date:** 30 October 2026. **By:** Claude, atlas owner. **Object:** annotated tag `ofn-v0.11`. **Status:** record (`EV-HASH`, `EV-RUN`, from `origin`).

| Check | Result |
|---|---|
| Tag type | annotated (`tag`); tag object `2018dfd078dd90287632a8c942f35ec1f20aaded`; tagger Mustafa Aksu |
| Target | `886afc64573579165170bff682de21d5acf60978` = "Merge pull request #112 from MustafaAksu/claude/ofn-v0.11" (parents `520abad` main, `e022183` branch head) — a merge commit, not squash |
| Message | "OFN v0.11 — RTG_ONTOLOGICAL_FOUNDATIONS.md SHA-256 38a2f444…e9e4" (full hash in the message) |
| File at the tag and on `main` (`f8f3b5b`) | `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` SHA-256 `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4` at both (1,581 lines, 192,052 bytes) |
| Accepted candidate → published | the accepted candidate `df3c465fb79f049f686f07635d889613e8ab112895cdbcd5af7af029e97400eb` (atlas row check, PR #115) is the file at `ba61f51` and `8ec6338`; `release_ofn_v0_11.py` replayed on it with "30 October 2026" writes `38a2f444…e9e4` byte-exact; its gates P1–P6 PASS and controls X1–X5 caught, output identical to `evidence/ofn/v0.11/release_check_output.txt` (`evidence/atlas/rowcheck/ofn_v0_11/release_check_replay.txt`) |
| What differs | 8 lines, each declared: Date, Document status, Supersedes ("on adoption" dropped), the §0.3 v0.11 label, the §12.3 six-DEF row, the Appendix B and Appendix C v0.11 headings, the footer — the release record §8 list plus the Date line; no claim tag, RID or math changes (P6) |
| Prerequisites reachable from the tag | PR #108 (`2861b16`), #109 (`d2fecb7`), #110 (`c82c606`), #111 (`e1e8851`), #116 upload (`d906cd2`), #115 row check (`520abad`) — the publication condition of the row check §4.1 is met |
| Non-blocking remarks of the row check | §4.2: RID-retention reason for OFN11-C02 now in the release record §3b; the RRF, Genesis and FMS/ER-2B notices name OFN11-C01/C02 · §4.3: the IMP-O10-05 phrase is kept as a declared live-file exception (release record §3b) · §4.4: no `history_appendix` in the map (optional; PR #113 still open) · §4.5: BASELINE row OFN = v0.11, `38a2f444…`, tag `ofn-v0.11`, authority the v0.11 release record |
| Post-tag (PR #117, `f8f3b5b`) | the three `pipes/OFN/` items `closed` with their 29 Oct dispositions; nine `kind: notice` items filed (DYAD, ER2B, FMS, GEN, NUMGEN, PROG, RECOG, RRF, TDRG; `state: open`); `tools/pipes_index.py --check` on `main`: OK, 33 items in 19 inboxes |

**Verdict:** `ofn-v0.11` is a correct publication of the accepted candidate. OFN v0.11 governs from 30 October 2026; `ofn-v0.10` is the predecessor. The filed notices are not receiver acceptance (CONVENTIONS §7). Atlas side next: the H1 / OFN.O1–O13 / DYAD.X1 / GEN.D15 refresh at the next atlas edition, together with RECOG v0.3.26.
