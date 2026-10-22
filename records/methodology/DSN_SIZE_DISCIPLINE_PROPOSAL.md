# DSN Size Discipline — programme-wide proposal v0.1 (for discussion)

**From:** atlas owner (Claude). **To:** PI; all stream owners. **Date:** 22 October 2026.
**Status:** noncanonical proposal. Nothing here is adopted. If accepted, it becomes a Methodology v1.4 amendment (§13.1 process) and is applied stream by stream in ordinary maintenance releases.
**Constraint kept throughout:** no scientific fact is lost. Every rule below moves *history* out of the live file; no rule removes a current statement, grade, scope, assumption, RID, OPEN status or evidence pointer.

## 1. The problem, measured

| File | Size | History share | Typical pattern |
|---|---:|---|---|
| DYAD v6.4.20 | 409k chars, 2,793 lines | Appendix A onward = 192k (47%); +136k in one release | Draft-round records (r1 44k, r2 13k, P1 13k, adoption 22k) and 55 quoted old→new lines inside Appendix A; §1 = 1,438 words |
| NUMGEN v1.20.8 | 338k | Appendix A onward = 100k (30%) | Per-version narrative history |
| RECOG v0.3.22 | 327k | 40k in appendices; 56 "historical / kept as history" phrases in the live body | Overlays inside live sections |
| RER v0.2 | ~150k | Header *Date* + *Document status* fields ≈ 10k chars | Revision chain "r4.13 was … r4.12 was … r4.1 was …" in the header; §9 repeats it; 14 stacked "Release boundary (r4.x)" sentences |
| Genesis v2.8.9 | ~130k | Supersedes field lists 26 versions; 5 stacked footers; full history since v2.0 | Status summary grows one sentence per release |
| RRF v0.8.4 | ~110k | 5 publication-boundary/overlay paragraphs in §0; §10.1–10.4 receipts | "Current-state override governs …; earlier text not rewritten" |
| Triadic v1.6.1 | ~120k | Header ≈ 6k ("History — v1.6 …" inside each field) | Per-version metadata kept in live fields |

Growth is driven by release mechanics, not by science. DYAD's v6.4.20 added 13 RIDs and grew 49%.

## 2. Root cause

1. **Provenance is implemented inside the live file.** Methodology §0.4 ("never silently erase") and §7 are being satisfied by keeping superseded text inline ("kept as history", "previous wording", "r4.x overlay"). But Methodology §1 (Appendix A) and §13.1 already allow this: history may be compressed *if the full record stays recoverable in an immutable version*. Every adopted version is already immutable and hash-pinned. The live file does not need to carry it again.
2. **Deterministic release builders only append.** Metadata-only releases ("change header lines only; every other byte identical") make it impossible to remove anything, so each release adds a header sentence, a footer and an Appendix A block.
3. **Overlay instead of replacement.** When a pin or status changes, the old sentence stays and an overlay is added ("r4.14 current-source note"). Readers must reconstruct the current state from layers.
4. **Repetition by design.** The same status is restated in §1, §2, §5, §6 and the notice table; the same disclaimers ("no certificate rerun", "non-transfer", "historical pins are not moved") are repeated per record.
5. **No budget is enforced.** Methodology §1 sets §1 at 200–400 words, but nothing checks it; there is no budget for the header, Appendix A or the whole file.

## 3. Proposed rules (Methodology v1.4, "DSN size discipline")

**S1 — Live file = current state.** §§0–9 state only what is current. Superseded wording, old pins, "kept as history" sentences and dated overlays are removed from live sections. Provenance is satisfied by three things together: (a) the immutable predecessor file and its hash; (b) the Appendix A entry (S4); (c) an Appendix B entry for every scientific correction, retraction or regrade (unchanged rule).

**S2 — Replace, then point.** A changed status, pin or scope is edited in place. The old form appears once, in the Appendix A entry of the version that changed it ("§6.14 L863: provenance item → v6.4.16 coefficient-equality pointer"). No inline "r4.x overlay" blocks.

**S3 — Header budget.** One line per field; *Document status* ≤ 60 words; *Supersedes* = immediate predecessor + hash; no revision chains, no "History —" text in any header field; one footer line.

**S4 — Appendix A budget.** Per version: change class, affected RIDs, scope/grade corrections, one-sentence reason, links (with hashes) to the release record and evidence. Target ≤ 150 words per version. Draft-round records, review verdicts, gate lists and verbatim old→new line maps go to the **release record** (already a separate file) or a hash-pinned history sidecar. This is the peer's E-2 reading, made general.

**S5 — One home per statement.** Each claim is stated once, at its owner location (§6 block or registry record). §1, §2, §5 and notice tables carry the RID, a one-line status and a pointer. §1 keeps the 200–400-word target; above 500 words a profile exception with a reason is *required* in the header (peer's E-1 reading).

**S6 — Factor repeated text.** Recurrent disclaimers become defined keys used by reference: evidence states (`EV-SRC-READ`, `EV-OWNER-REPORTED`, `EV-RERUN`, … from Methodology §12.2), non-transfer guards (existing SG mechanism) and per-file standard clauses. A record cites the key instead of repeating the paragraph.

**S7 — One current pin per reference.** A reference carries one current pin. Historical pins and "bytes not recovered" notes move to the release record, unless the historical pin is itself the load-bearing source (then it *is* the current pin, labelled so).

**S8 — Size budgets with a release gate.** Soft budgets by profile (technical ledger: live body §§0–9 ≤ 200k chars; Appendix A ≤ 30k; header ≤ 3k). Above a budget, the release record states why, or the owner splits under Methodology §13.3 into the canonical DSN plus a versioned technical supplement (proof detail only; statements and scope stay in §6).

**S9 — Compaction release type.** A new release type, "compaction", changes layout only. It is accepted by a checker, not by a scientific review, if: every RID, every grade tag, every OPEN status line and every math span of the predecessor's live sections is present in the new file (or moved verbatim to Appendix B with a pointer); every removed passage is found byte-identical in an immutable predecessor or in the release record; and no new claim appears. DYAD's v6.4.20 release checker (R2–R5, R9) already implements most of these gates.

## 4. Tooling (atlas Pass 3)

A single `dsn_lint.py`, run by owners before release and by the atlas after:
- header field lengths, one footer, `Supersedes` single entry;
- §1 word count vs. declared profile exception;
- Appendix A words per version;
- count of history phrases in §§0–9 ("kept as history", "previous wording", "overlay", "was:");
- near-duplicate paragraphs (n-gram overlap) across sections;
- file size vs. budget, and growth vs. predecessor relative to new RIDs.
The compaction checker of S9 is a second script. Both report; neither decides science.

## 5. Reading tiers for AI readers

1. **Atlas** (≈ 60–90k tokens, whole programme): orientation, relations, diagnostics.
2. **DSN orientation core** (§§1–4, ≤ 800 lines, Methodology §6.1).
3. **DSN live body** (§§5–9).
4. **Release records, history sidecars, archive** — consulted only for provenance questions.

With S1–S5 in force, tier 3 is the current state only, and tiers 1–3 together fit a single working context for most cross-stream tasks.

## 6. Expected effect (estimates, to be measured by the pilot)

| File | Now | After compaction (estimate) | Source of reduction |
|---|---:|---:|---|
| DYAD | 409k | 210–240k | Appendix A draft records → release record; §1 compaction; repeated status text |
| NUMGEN | 338k | 250–270k | Appendix A compression |
| RECOG | 327k | 260–280k | Live-section overlays |
| RER | ~150k | 90–110k | Header chain, stacked boundaries, repeated pin notes, record boilerplate |

No reduction comes from removing scientific content.

## 7. Rollout

1. **Discuss and decide** this proposal (PI). Open choices in §8.
2. **Methodology v1.4 amendment** drafted from S1–S9 and adopted by the PI.
3. **Pilot: DYAD v6.4.21.** The errata successor already planned in the closeout (E-1, E-2) is the natural first application; it also tests S9 and the lint.
4. **RER v0.3** (Claude is co-owner, so the receiving review goes to the other co-owner): header chain, boundaries, overlays.
5. **Other streams** apply S1–S9 at their next ordinary release; no stream is forced into a compaction-only release unless it chooses one.
6. **Atlas** refreshes from the compacted files and adds an L5 `D-SIZE` diagnostic class for budget breaches.

## 8. Decisions requested

1. Accept the principle S1 (live file = current state; history in immutable versions, release records and Appendix B)?
2. Budget numbers in S8: accept as proposed, or set per stream?
3. Compaction-only releases (S9): allowed with a checker instead of a scientific review?
4. Where do history sidecars live: in the project, or only in the archive (the project is at about two-thirds of its knowledge capacity)?
5. Pilot on DYAD v6.4.21 together with the closeout errata, or as a separate compaction release first?
