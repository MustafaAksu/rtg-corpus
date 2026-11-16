# Atlas advisory to the PI — are the active streams stable, and which streams are not yet in the working pattern

**Date:** 16 November 2026. **By:** Claude, Atlas owner. **Status:** [SESSION] advisory. The Atlas owner advises and does not decide; nothing here is adopted.
**Asked by the PI** (project conversation, 16 Nov 2026, 16:06 +03:00): if the current streams have reached stable levels, take the streams not yet brought to the current state, to the GitHub working pattern and into Atlas-era work.
**Basis:** `main` `2d898fd`; `BASELINE.md`; `atlas-v0.13`; pipe states from `tools/pipes_index.py`; tag dates; the files' own headers. Owner texts were not reread for this note beyond their headers.
**Earlier advice this builds on:** `records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md` (rows 2, 4, 5 are still open and ride with the reworks proposed here).

## 1. What "in the working pattern" means here

A stream is in the working pattern when all of the following hold:
- its governing edition has a release record in `records/<study>/`, and `BASELINE.md` verifies it as OWNER;
- it declares DSN Methodology v1.4;
- it has an entry note for co-owner sessions;
- its inbox is answered at its own checkpoints;
- its editions reach the Atlas through impact refreshes.

## 2. Are the active streams stable?

| Stream | Edition (tag date) | Methodology | State |
|---|---|---|---|
| Methodology, Programme | v1.4 (22 Oct, 4 Nov) | — / v1.4 | stable; Programme inbox 6 open (one request: the SAT interface, since 9 Nov) |
| DYAD | v6.4.24 (11 Nov) | v1.4 | stable edition; OPEN 20 stage 3c-b in progress (research, not instability) |
| TDR-G | v2.13 adopted 16 Nov, **not yet merged or tagged** (PR #265) | v1.4 in v2.13 | stable once published |
| AZ | v0.10 (16 Nov) | v1.4 | reactivated, stable; Level A |
| TRIAD, GEN, RECOG, NUMGEN, OFN | v1.7, v2.10, v0.3.27, v1.21, v0.12 (26 Oct – 4 Nov) | v1.4 | stable editions; **notice backlogs**: NUMGEN 9, OFN 7, TRIAD 6, GEN 3 (one request: LIT Regge inputs, since 4 Nov) |

Verdict: **stable enough to start.** No active stream has an edition in flux except TDR-G, whose publication is a server step. Two costs remain open:
- **Notice backlogs.** 26 open items in the five maintained streams, all notices except one request. None blocks, but each consumer pin they report stays stale until answered.
- **Two old PRs open since 3–4 Nov:** #160 (GEN inbox disposition) and #183 (OFN Binary Recognition wrap-up).

A light inbox pass per stream would clear the backlogs. That pass is separate from onboarding new streams and can run between them.

## 3. Streams not yet in the working pattern

Eight streams have not been opened since the baseline import of 22 Oct 2026. All are tagged, but none has a records folder of its own except RER and FMS (the folders hold no release record), and none has an entry note.

| Stream | File (bytes) | Methodology declared | BASELINE verification | Programme §9.2 pass | Open inbox | Atlas L5 rows | Known debts |
|---|---|---|---|---|---|---|---|
| **DZT** v0.8 | 50,547 | v1.2 | PI | not executed | 4 (DYAD n16–n21, AZ v0.7, AZ v0.8, LIT norm-law proof offer) | 3 | DZT.Q1 non-owner Dyadic RIDs (advisory row 2); AZ pin v0.6 |
| **OPEN-M (UVM)** v0.7.1 | 92,170 | v1.3 | XREF (RER v0.2) | executed (before the repository) | 4 (GEN κ_f/B_*, DYAD n16–n21, GEN v2.10, TRIAD v1.7) | 11 | R12 attribution (advisory row 4); Genesis pin v2.8.5 |
| **RRF** v0.8.4 | 108,615 | not stated | XREF (RER v0.2) | not in the sequence | 6 (RECOG, OFN v0.11, v0.12, DYAD, GEN, TRIAD) | 5 | Genesis row pinned at v2.8.9; class-C reading |
| **Pre-Legacy** v0.8 | 70,805 | not stated | PI | not executed | 1 (SAT finding on K₃ degeneracy) | 6 | old pins v0.5/v0.3/v1.1/v1.2 (PROG.G6); advisory row 5 |
| **Legacy** v0.7 | 138,141 | v1.3 | PI | executed (before the repository) | 0 | 4 | advisory row 5 (with Pre-Legacy) |
| **RER** v0.2 (noncanonical) | 222,178 | — | PI | — | 2 | 0 | — |
| **ER-2B** v0.3 (noncanonical) | 60,351 | — | PI | — | 2 | 0 | — |
| **FMS** v0.6.4 (session) | 43,516 | — | PI | — | 2 | 0 | — |

## 4. Advice

**One stream at a time.** At most two can run in parallel, because each needs two co-owner sessions and the PI's review. Use the same pattern as AZ:
1. an entry note with staged first messages (read the updates, then put the stream's own work in order);
2. a triage record of what is stale, wrong or missing;
3. a corrections edition (identifiers, pins, attribution) with no new science;
4. the Methodology v1.4 migration;
5. the inbox answered;
6. the Atlas row check, then an Atlas impact refresh.

The AZ cycle (10–16 Nov) took four editions. A smaller stream can take one or two.

**Order:**
1. **DZT** — the closest to live science: it consumes Dyadic and AZ, and its arithmetic is cited by both. Its debts are identifiers and pins, and it has the oldest Methodology (v1.2). LIT has offered a proof candidate for its open norm law. Its Q1 row also produces about 11 documented-unresolved links in every Atlas check.
2. **OPEN-M** — 11 Atlas diagnostics, the H2/H11 rows, four notices. Its first pass was executed before the repository existed, so only the repository side and v1.4 are missing.
3. **RRF** — six notices from the streams it registers, and an interface registry whose rows go stale as those streams move.
4. **Pre-Legacy, then Legacy** — historical sources. The work is source maintenance (pins, conventions, the "0.5" convention trap of advisory row 5), not new science. Legacy has nothing open.
5. **RER, ER-2B, FMS** — noncanonical. Before any rework, the PI decides their status: keep each as a live registry or study (then onboard it), or record it as frozen at its tag (then its inbox items are answered "recorded, no further editions" and the Atlas marks it historical).

**Atlas:** each reworked edition enters through the next impact refresh. The next refresh is v0.14 (`tdrg-v2.13` and `az-v0.10`); DZT would follow in v0.15.

## 5. Asked of the PI

1. Start with DZT, or another stream?
2. One stream at a time, or two in parallel?
3. RER, ER-2B and FMS: onboard, or record as frozen?
4. Whether the maintained streams run a light inbox pass now, and what happens to PRs #160 and #183.

After the PI chooses, the Atlas owner drafts the first stream's entry note, as for AZ (`records/az/AZ_COOWNER_SESSION_ORIENTATION.md`). The stream's owners then maintain it.
