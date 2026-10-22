# DSN Methodology v1.4 — Size-Discipline Amendment — DRAFT v0.1 (amendment form)

**Base:** `DSN_METHODOLOGY_v1_3.md` (ADOPTED 20 Sep 2026; SHA-256 `3e23ba94606706b3c8d50aecfb2184df52042cf8e65cdd3c3e0cd3159254ec7e`).
**Source proposal:** `claude/atlas/RTG_DSN_SIZE_DISCIPLINE_PROPOSAL_v0_1.md`.
**PI decisions (22 Oct 2026):** D1 rule S1 accepted; D2 no fixed size budgets; D3 compaction is editorial work, a script check is sufficient; D4 history files stay in the project, with no supersede chains; D5 the pilot is DYAD v6.4.21, together with the closeout errata, with no separate release.
**Status:** DRAFT, amendment form. Each item below replaces or inserts text at a named v1.3 location. A whole-file v1.4 is assembled from these items after review. No scientific claim, RID, grade or OPEN status in any DSN is changed by this amendment.
**Prepared by:** Claude (atlas owner). Revision editor and adoption: per v1.3 §13.1.

---

## A1 — §0.4, priority 3 (replace)

> 3. **Provenance preservation:** never silently erase a scientific correction, rejection, or source dependency. Provenance is preserved by immutable adopted versions, the study's history file, release records and Appendix B — not by keeping superseded text in live sections (§1.1).

## A2 — §1 "§0 Header Block" (append after the field list)

Header rules:
- One line per field. *Document status* states the current status only.
- *Supersedes* names the **immediate predecessor and its hash only**. It never lists earlier versions; the chain is recoverable from each predecessor's own header and from the history file.
- No "History —", "previous status", "r-x was" or dated release-boundary text in any header field.
- Exactly one footer line, describing the current version.

## A3 — §1 "§1 — Current Canonical State" (replace the second paragraph)

> Target: 200–400 words. Above 500 words, either move material to its proper location or declare a profile exception **in the header**, with a one-line reason. A declared exception is a required record, not an optional note; "deferred" does not replace it.

## A4 — New §1.1 "Live-file rule" (insert after §1's appendix list)

**§1.1 Live sections state the current state.**
1. **Current only (S1).** §§0–9 contain only current statements, scopes, pins and statuses. Superseded wording, dated overlays ("rX.Y current-use overlay"), "kept as history" sentences and old pins are removed from live sections.
2. **Replace, then record (S2).** A changed status, pin or scope is edited in place. The change is recorded once: one line in Appendix A for the version that made it; an Appendix B entry if it is a scientific correction, retraction or regrade (§7, unchanged).
3. **One home per statement (S5).** Each claim is stated in full once, at its owner location (§6 block or registry record). §1, §2, §5, export tables and notice tables give the RID, a one-line status and a pointer.
4. **One current pin per reference (S7).** A reference carries the pin actually used now. A historical pin stays live only when it is itself the load-bearing source; it is then labelled as the current pin.
5. **Repeated clauses by key (S6).** A disclaimer used in more than two places is defined once (evidence states §12.2; guards §3; per-file standard clauses in a short "Standard clauses" list) and cited by its key.

This rule removes history from live sections; it never removes a current statement, assumption, scope, grade, RID, OPEN status or evidence pointer.

## A5 — §1 "Appendix A — Version History" (replace the rule paragraph)

> Each version has one entry: date and status; change class; affected RIDs; every scope or grade correction; a one-sentence reason; links, with hashes, to the release record and evidence. Draft-round records, review verdicts, gate lists and verbatim old→new line maps belong in the **release record**, not in Appendix A. Older entries move to the study's history file (§13.7) when they are no longer needed for current use; Appendix A keeps a one-line pointer to it.

## A6 — §12.2 (append) Evidence-state keys

The review states of §12.2 may be cited by key:
`EV-SRC-READ` (source statement inspected), `EV-SRC-REPORTED`, `EV-BYTES` (artifact bytes available), `EV-HASH` (hash checked), `EV-CODE` (code inspected), `EV-RUN` (executed in this review), `EV-INDEP` (independent mathematical check), `EV-COVER` (claim coverage assessed), `EV-NOT-RERUN`. A key means exactly its §12.2 definition and nothing more.

## A7 — New §13.6 "Compaction release"

A **compaction release** changes layout only, to bring a file under §1.1 and the header/Appendix A rules. It is editorial work: it needs no scientific review and is accepted when a compaction checker passes (D3). The checker must show:
1. every RID, every claim-status tag sequence, every OPEN status line and every math span in the predecessor's live sections is present in the new file, or moved verbatim to Appendix B with a pointer;
2. every removed passage is found byte-identical in the immutable predecessor, the release record or the history file;
3. no new claim text appears outside the declared metadata lines;
4. the header, single footer and *Supersedes* line follow A2.
A compaction may be combined with an ordinary release (D5); the scientific part then follows the ordinary rules, and the checker covers the layout part.

## A8 — New §13.7 "History file"

Each study keeps **one** history file in the project, `<STUDY>_HISTORY.md`, holding version-history entries and removed historical prose that are not needed for current use. It is cumulative, is updated in place at each release, carries no version number and supersedes nothing, so no supersede chain arises (D4). Its entries are append-only: existing entries are not edited, except by an explicit dated correction note. The DSN's Appendix A points to it. Immutable adopted DSN versions remain in the archive as before.

## A9 — New §13.8 "Size reporting"

There are no fixed size budgets (D2). A lint script reports, for each release: file size and growth against the predecessor; growth per new RID; §1 word count; header field lengths; Appendix A words per version; count of history phrases in §§0–9; near-duplicate paragraphs. The report goes in the release record. It informs the owner; it does not block a release.

## A10 — Anti-patterns (§11, add rows)

| Anti-pattern | Why it fails | Correct practice |
|---|---|---|
| Keeping superseded text in live sections as "history" | Readers must reconstruct the current state from layers; files grow every release | Replace in place; record once in Appendix A / history file (§1.1) |
| Revision chains in header fields | The header grows with every release | Immediate predecessor and hash only (A2) |
| Draft-round records in Appendix A | Appendix A becomes most of the file | Release record (A5) |
| Same status restated in four sections | Inconsistency risk; size | One home, pointers elsewhere (§1.1.3) |

## A11 — Transition

- Applies to each DSN at its next release; no DSN is forced into a separate compaction-only release.
- Pilot: DYAD v6.4.21, combined with the closeout errata (S-1–S-6, E-1, E-2, C-1–C-4).
- Existing files remain valid under v1.3 until their next release.
- Methodology Appendix A gets a v1.4 entry; Appendix B gets correction keys M14-C01 (provenance-location reading of §0.4) and M14-C02 (Appendix A content rule).
