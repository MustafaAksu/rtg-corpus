# Programme work list — what each stream still needs (Atlas advisory)

**Date:** 20 November 2026. **By:** Claude, Atlas owner. **Status:** [SESSION] advisory, NONCANONICAL. The Atlas owner advises and does not decide; nothing here is adopted, and no stream is told what to do.
**Asked by the PI** (project conversation, 20 Nov 2026, 10:30 +03:00): a general list of the work still to be done — the move to GitHub, adaptation to the new Methodology, record-keeping for operational continuity, working with LIT, and so on.
**Basis:** `main` `d422b89`, read on 20 Nov 2026:
- `BASELINE.md` and the newest tag of every study;
- the release records and entry notes in `records/`;
- the pipe states (`tools/pipes_index.py`: 142 items, check OK);
- the open PRs;
- `atlas-v0.14` and its manifest;
- the LIT rules in `CONVENTIONS.md` §8 and in `rtg-lit/CONVENTIONS.md` (adopted 11 Nov 2026).

Owner texts were not reread beyond their headers and the strings counted. Counts are mechanical and are to be confirmed by each owner.
**Builds on:** `records/atlas/ATLAS_ADVISORY_STREAM_ONBOARDING_20261116.md` (§6: DZT first; the rest deferred).

## 1. Where each stream stands

The columns:
- **Repo** — the governing edition has an OWNER release record in `records/`, as opposed to a PI- or XREF-verified baseline import;
- **Meth.** — the Methodology version the file declares;
- **Entry** — an entry note or orientation note for co-owner sessions exists, with the date it was last changed;
- **Open in** — open or acknowledged items in the stream's own inbox;
- **Compound** — backticked `[X/Y]` grade tokens still in the file. Some may sit in history or retraction blocks, which are allowed; the owner checks.

| Stream | Edition (tagged) | Repo | Meth. | Entry | Open in | Compound | Atlas v0.14 pin |
|---|---|---|---|---|---|---|---|
| Methodology | v1.4 (22 Oct) | yes | — | none | 0 | 2 (examples?) | source |
| Programme | v1.4 (4 Nov) | yes | v1.4 | none | 8 | 0 | current |
| DYAD | v6.4.24 (11 Nov) | yes | v1.4 | 16 Nov | 2 | 2 | current |
| TDR-G | v2.13 (16 Nov) | yes | v1.4 | 11 Nov | 0 | 0 | current |
| AZ | v0.10 (16 Nov) | yes | v1.4 | 18 Nov | 0 | 2 (retraction block) | current |
| DZT | v0.18 (19 Nov); **v0.19 waiting for the PI** (PR #334) | yes | v1.4 | 19 Nov | 1 acknowledged | 0 | **behind (v0.8)** |
| TRIAD | v1.7 (3 Nov) | yes | v1.4 | 11 Nov | 6 | 3 | current |
| GEN | v2.10 (3 Nov) | yes | v1.4 | 11 Nov | 3 | 2 | current |
| RECOG | v0.3.27 (4 Nov) | yes | v1.4 | 11 Nov | 1 | 4 | current |
| NUMGEN | v1.21 (26 Oct) | yes | v1.4 | 11 Nov | **10** | **17** (audit labels) | current |
| OFN | v0.12 (30 Oct) | yes | v1.4 | 11 Nov | **9** | 0 | current |
| **OPEN-M (UVM)** | v0.7.1 (baseline) | **no** (XREF) | **v1.3** | none | 4 | 10 | current |
| **RRF** | v0.8.4 (baseline) | **no** (XREF) | not stated | none | 6 | 0 | current |
| **Pre-Legacy** | v0.8 (baseline) | **no** (PI) | not stated | none | 1 | 0 | current |
| **Legacy** | v0.7 (baseline) | **no** (PI) | **v1.3** | none | 0 | 0 | current |
| **RER** (noncanonical) | v0.2 (baseline) | **no** (PI) | — | none | 2 | 0 | current |
| **ER-2B** (noncanonical) | v0.3 (baseline) | **no** (PI) | — | none | 2 | 0 | current |
| **FMS** (session) | v0.6.4 (baseline) | **no** (PI) | — | none | 2 | 0 | current |
| **PRR Wrap-up** (noncanonical) | v0.2 cited; **not in the repository** | — | — | none | no inbox | 0 | — |
| Atlas | v0.14 (17 Nov) | yes | Method v0.3 | 17 Nov | 0 | 4 Atlas heads | — |
| LIT (`rtg-lit`) | records, not DSNs | own repo | own CONVENTIONS (adopted 11 Nov) | own entry note | 1 (DYAD's LH2012 use report), and the SAT items | — | not an input |

## 2. The work, by kind

### A. Streams never brought into the working pattern

This means the move to GitHub, Methodology v1.4 and an entry note. Seven streams have not been opened since the baseline of 22 Oct. The AZ and DZT cycles show the shape of the work:
1. an entry note with staged first messages;
2. a reading report;
3. a triage with PI decisions;
4. a corrections edition with Methodology v1.4 as a second stage;
5. notices;
6. an Atlas refresh.

AZ took four editions and DZT two, both under a week.

| # | Stream | What is known to be needed | Suggested order |
|---|---|---|---|
| A1 | **OPEN-M (UVM)** | Methodology v1.3 → v1.4; 10 compound tokens; 11 Atlas diagnostics (OPENM.*), including the R12 attribution (advisory row 4); Genesis pin v2.8.5; 4 notices (GEN κ_f/B_*, DYAD N16–N21, GEN v2.10, TRIAD v1.7) | 1 — the most Atlas findings and live consumers |
| A2 | **RRF** | It declares no Methodology. Its interface registry rows are stale as their streams have moved (Genesis row at v2.8.9). 6 notices (RECOG, OFN ×2, DYAD, GEN, TRIAD). **Its records never came to GitHub:** only the v0.8.4 file itself is in the repository (`dsn/`, `rrf-v0.8.4`, BASELINE verified by XREF through RER, not by an RRF release record). There is no `records/rrf/`. Absent, though cited by name: the adoption records of v0.7, v0.8.3 and v0.8.4 (`RTG_RRF_REPRESENTATION_REGISTRY_v0_*_ADOPTION_RECORD.md`), the earlier editions v0.4–v0.8.3 and the v0.7 DRAFT, and the RRF reviews (`RTG_RRF_OPEN19_G2_POSTADOPTION_SYNC_REVIEW_v0_2`, `RTG_RRF_G2_PRIMITIVE_EXCHANGE_INTERFACE_REVIEW_v0_4_REVIEW_CANDIDATE`, `RTG_RRF_DEGREE10_REVIEW_INTEGRATION_v1`). Whether any RRF edition after v0.8.4 (20 Oct) exists is not known to the Atlas owner. First step: the PI locates the RRF working files; they arrive unchanged on an `upload/rrf-records` branch and are hash-checked against the hashes recorded in the v0.8.4 file and in RER (v0.8.3 `b393657e…4a187`, v0.7 `2a2b4102…`) | 2 — its rows go stale with every edition elsewhere |
| A3 | **Pre-Legacy** | Old pins (PROG.G6); the "0.5" convention trap (advisory row 5); one SAT finding (K₃ degeneracy and lift) | 3 — historical source; maintenance only |
| A4 | **Legacy** | Methodology v1.3 → v1.4; advisory row 5 together with Pre-Legacy; nothing open | 4 — with A3 or right after |
| A5 | **RER, ER-2B, FMS** | **The PI decides their status first:** onboard each as a live registry or study, or record it as frozen at its tag. In the second case its notices are answered "recorded, no further editions" and the Atlas marks it historical. 2 open items each | after the PI's decision (question 3 of the 16 Nov advisory, deferred) |
| A6 | **PRR Wrap-up** (`RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP`, noncanonical; added 20 Nov 2026 after the PI noted that a fourth noncanonical element never reached GitHub) | Never imported. It is the declared parent of RRF (`dsn/RTG_RRF_REPRESENTATION_REGISTRY.md` header: "parent: …WRAPUP_v0_2 §20, §26") and is cited by RECOG (§ source ledger: "PRR Wrap-up v0.2, noncanonical … interpretive only"). Its v0.3 synchronisation was delegated to its editor in Sep–Oct 2026 and is not known to have been produced. Steps: (1) the PI locates the bytes (v0.2, and v0.3 if it exists); (2) they arrive unchanged on an `upload/...` branch and are hash-checked; (3) `noncanonical/` gets the governing version under a fixed filename, with a release record and a BASELINE row; (4) the PI decides its status together with A5. No hash is known to the Atlas owner | with A5; the import (1)–(3) can come first, since RRF's parent pointer cannot be checked until then |
| A7 | **Other cited, absent noncanonical sources** | Cited by RRF and RER with hashes recorded there, but not in the repository: `RTG_RRF_RER_DYNAMICAL_CLOSURE_PROPOSAL_v0_1` (RER records SHA-256 `65186f39…4e86`), `RTG_RRF_RESPONSE_TO_OFN_COINCIDENCE_v0_2` (`897bfad0…126d`), `RTG_RRF_COINCIDENCE_ADMISSIBILITY_REVIEW_v0_1` (hash in RER), `ER2B_COINCIDENCE_SIXSTEP_AUDIT_v0_1.zip` (no hash anywhere). Also the "Initial Ontological Premises and Questions" note (Oct 2026), not cited in the repository. Legacy cites `RTG_MASTER_DSN` and `RTG_L0_L1_L2_BRIDGE_LEGACY_HISTORY_ARCHIVE`, also absent | a targeted search together with A6; each found file goes through the same `upload/...` hash check against the recorded hash |

### B. Streams in the pattern that the later changes have overtaken

These streams have notices waiting and pins one or more editions behind. The work is, at each stream's own checkpoint:
- an inbox pass that disposes of the notices;
- if pins or citations changed, a small synchronization edition;
- the stream's own open questions.

| # | Stream | What waits |
|---|---|---|
| B1 | **NUMGEN** (v1.21, 26 Oct; the oldest maintained edition) | 10 open notices: TDR-G v2.12.14, v2.12.15, v2.13; RECOG v0.3.26, v0.3.27; DYAD v6.4.23, v6.4.24; OFN v0.11, v0.12; PROG v1.4; DZT v0.18. Pins `dzt-v0.8`, `dyad-v6.4.22`, `gen-v2.9`, `ofn-v0.10`, `programme-v1.3`. **17 compound audit labels** (`[ENG/ALG audit]` and others) under a v1.4 declaration, to be unpacked or justified (Methodology §8.4) |
| B2 | **OFN** (v0.12, 30 Oct) | 9 open notices (DYAD ×2, GEN v2.10, TRIAD v1.7, PROG v1.4, RECOG v0.3.27, TDR-G v2.12.15 and v2.13, DZT v0.18); older pins; PR #183 (Binary Recognition wrap-up) open since early November; XFER-O08-01 custody, open with TDR-G |
| B3 | **TRIAD** (v1.7, 3 Nov) | 6 open items, among them the GEN 𝒫₄-identity and birth-symmetry answers and the DYAD bridge-note recovery; pins `gen-v2.9`, `dyad-v6.4.23`, `programme-v1.3`, `tdrg-v2.12.14`; 3 compound tokens |
| B4 | **GEN** (v2.10, 3 Nov) | 3 open items, among them the **LIT Regge interface inputs, open since 4 Nov**; PR #160 (inbox disposition) open since 3 Nov; older pins; 2 compound tokens |
| B5 | **RECOG** (v0.3.27, 4 Nov) | 1 notice (DYAD v6.4.24); 4 compound tokens; older pins |
| B6 | **Programme** (v1.4, 4 Nov) | 8 open items: the **SAT satellite-interface request (9 Nov)**; AZ v0.7–v0.10; TDR-G v2.12.15 and v2.13; DZT v0.18. Its §9.2 maintenance record and §6.4 gate sentence describe states that AZ, TDR-G and DZT have since passed (Atlas PROG.G6). A Programme maintenance edition (v1.5) would record the new state |
| B7 | **DYAD** (v6.4.24, 11 Nov) | 2 open items: the AZ v0.10 notice and the LIT reply on the scope of LH2012 Prop. 5.3. OPEN 20 has five open PRs (#296, #301, #305, #312; #287 parked) |
| B8 | **TDR-G** (v2.13) | Inbox clear. Open questions from its release record: the TDR-19 policy choice, XFER-O08-01 custody (with OFN), and the crystallization grade (`[HEUR]` against `[HEUR strong]`) |
| B9 | **AZ** (v0.10) | Inbox clear. Fork work in progress (PR #331); `AZ-OPEN-PROMO` and Level B conditions open |
| B10 | **DZT** (v0.18) | **v0.19 waits for the PI's adoption** (PR #334, readback `5988755813`, ACCEPT SCOPED). After it come B1 re-examination, channel universality and the targeted search for missing sources (DYAD `q4_03` certificate, `qb_extract.py`, v0.6, the v0.17 session record). The v0.18 notices are open at PROG, NUMGEN and OFN |

### C. Methodology and the shared rules

| # | Item | State |
|---|---|---|
| C1 | **Compound grade tokens under a v1.4 declaration** (NUMGEN 17, OPEN-M 10, RECOG 4, TRIAD 3, GEN 2, DYAD 2) | Each owner checks whether a token is in an allowed history or retraction block, or needs unpacking (§8.4). The Atlas carries METH.M1 for the pattern |
| C2 | **The PI's 19 Nov practice**: next to every equality, state the coordinate system and the categorical class it holds in, so that equalities from different conceptual systems are not mixed without normalization | Wanted in LIT as well. It is not yet a Methodology rule. Whether it becomes one (a Methodology amendment) is a PI decision |
| C3 | PR #189 — Methodology session-continuity proposal (DEFERRED) | CONVENTIONS §9 now carries the working-memory rule. The PI decides whether #189 is closed, folded into a later Methodology edition, or kept |
| C4 | Methodology §13.7/§13.8 (no stored diffs; size report) | Applied in the AZ, TDR-G and DZT cycles. The streams of A and B meet it at their next edition |

### D. Record-keeping for operational continuity

| # | Item | State |
|---|---|---|
| D1 | **Entry notes missing**: Methodology, Programme, OPEN-M, RRF, Pre-Legacy, Legacy, RER, ER-2B, FMS, PRR Wrap-up | Each is written when the stream is opened (A), or now for Programme, which has open items |
| D2 | **Entry notes not refreshed since 11 Nov**: GEN, NUMGEN, OFN, RECOG, TDR-G, TRIAD, and the two DYAD/GEN/RECOG inbox notes of 30 Oct–3 Nov | Each lane gets a checkpoint at the stream's next session (CONVENTIONS §9). TDR-G's lane predates v2.13's tag |
| D3 | `tools/orient.py` has no built-in profile for AZ and DZT. Their release records are not found without `--tag-prefix`, `--file` and `--record-glob` | Tool debt. A profile table for every study would make LIVE_STATE one command everywhere |
| D4 | Notices sent but not closed: DYAD 14, OFN 8, GEN 7, TDR-G 6, AZ 6, RECOG 5, PROG 4, TRIAD 3, DZT 3 | No action by the sender. Each closes when its receiver decides |
| D5 | The PRs listed above, open since early November (#160, #183, #189, #287) | A PI decision each: merge, close, or keep parked with a reason |

### E. LIT

| # | Item | State |
|---|---|---|
| E1 | GEN: the LIT Regge interface inputs (since 4 Nov) | waiting at GEN (B4) |
| E2 | DYAD: the LIT reply on the scope of LH2012 Prop. 5.3 (17 Nov) | waiting at DYAD |
| E3 | LIT inbox: DYAD's LH2012 use report (12 Nov) and the SAT use reports (HCG Abdulali, HHO Witt) | waiting at LIT |
| E4 | DZT: the LIT proof offer (acknowledged). It closes with v0.19. After the tag, the LIT notice asks LIT to correct two things: its record header ("not reviewed / not offered") and the phrase "right on the anomaly set" | after v0.19 |
| E5 | LIT is consolidating the literature it already holds (PI, 18 Nov). New searches are set aside | LIT's own work |
| E6 | The equality annotation of C2, in LIT's index | LIT's own work, when the PI confirms the form |
| E7 | Prior-art checks (CONVENTIONS §8) | No stream has asked for one for its new results: the DZT norm law, the TDR-G token laws, the AZ diagnostics. Asking is the stream's choice. The PI's rule is that RTG claims no novelty for what LIT finds in the literature |

### F. Atlas

| # | Item | State |
|---|---|---|
| F1 | DZT moved from v0.8 to v0.18; v0.19 is near | One refresh (v0.15) after v0.19, as was done for AZ v0.9. The PI has not yet answered whether to wait |
| F2 | Four Atlas-side compound heads in D5 | At the next D5 opening |
| F3 | Tool debts: the coverage check for non-Dyadic sources (now done by builder assertions); seven multi-line identifiers; a comparator mode for heading renames; F4 | Open |
| F4 | Every stream opened under A enters through an impact refresh after its first edition | Follows A |
| F5 | Size | Reported, not targeted. The PI looks at it again after the streams are reworked (10 Nov decision) |

## 3. Suggested sequence

1. **Now:** the PI decides DZT v0.19. Then the Atlas v0.15 refresh (DZT v0.8 → v0.19) and the DZT notices.
2. **OPEN-M**, on the AZ/DZT pattern. In parallel, if the PI wants: an inbox pass for **NUMGEN** and **OFN**, the two largest backlogs, and the oldest maintained editions.
3. **RRF**, then a **Programme** maintenance edition that records the state after A1–A2 and answers its 8 items.
4. **Pre-Legacy and Legacy** together (maintenance only).
5. **RER, ER-2B, FMS** according to the PI's status decision; the **PRR Wrap-up** import (A6) and the search for the other absent sources (A7) can start now, independent of that decision.
6. Throughout: GEN answers LIT (E1); the decisions on the old PRs (D5); the C2 rule if the PI wants it in Methodology.

## 4. Asked of the PI

1. Whether to start OPEN-M next. Whether inbox passes in NUMGEN and OFN run in parallel.
2. The status of RER, ER-2B, FMS and the PRR Wrap-up: onboard them, or record them as frozen. Where the PRR Wrap-up bytes (v0.2, any v0.3) are, and whether the ontological premises note belongs in the repository.
3. Whether the equality annotation (C2) becomes a Methodology rule, and in what form.
4. What happens to PRs #160, #183, #189 and #287.
5. Whether the Atlas waits for DZT v0.19 before refreshing (F1).

## 5. Since the snapshot (added 21 November 2026)

The tables above are the 20 Nov snapshot and are not rewritten. What has changed since:
- **DZT v0.19** was adopted and tagged on 20 Nov (`dzt-v0.19`, file `2b959f46…f6ce`). Row B10's first clause, sequence step 1 and item E4's condition are met. DZT's B1 work continues in PR #347.
- **Atlas v0.15** was accepted and tagged on 21 Nov (`atlas-v0.15`, file `483e6003…02df`; DZT `dzt-v0.8` → `dzt-v0.19`). F1 is closed and question 5 of §4 no longer needs an answer. In §1 the DZT pin is current and the Atlas edition is v0.15.
- **A2, A6, A7** were added on 20–21 Nov after the PI noted that RRF's records and the PRR Wrap-up never reached GitHub.
- The Atlas reviewer proposed (orientation note, reviewer lane, 21 Nov) a verified per-stream state matrix with the categories `CURRENT`, `NEEDS_REVIEW`, `BLOCKED`, `UNVERIFIED`, `INTENTIONAL_PIN`. It starts from the §1 table here, so that one table is maintained and not two.

Questions 1–4 of §4 are still open with the PI.
