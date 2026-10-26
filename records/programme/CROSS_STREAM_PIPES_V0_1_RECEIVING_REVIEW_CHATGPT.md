# Cross-stream pipes v0.1 — independent change-focused receiving review

**Date:** 26 October 2026  
**Status:** [SESSION] / receiving review; not a Methodology or scientific owner adoption  
**Object:** PR #66 `claude/pipes-v0.1`, head `a6285b6728130015355781b2b74e792b7e0c8ffa`  
**Reading extent:** `CONVENTIONS.md` §7, `pipes/README.md` entire, `tools/pipes_index.py` entire, pilot methodology clause entire, three representative pipe items (TDRG, UVM, NUMGEN) fully, 30-file PR paths; not an independent execution of the script or a byte-level validation of all seven initial items.  
**Verdict: REVISE (bounded, one batch).** Architecture and autonomous recipient checkpoints supported; no owner-science change is requested.

## Findings

### PIPES-R1 — four notice statuses are not derived from the one four-value queue status (BLOCKING)

**Locations:** `CONVENTIONS.md` §7, amended paragraph; `pipes/README.md` 'States' and 'What an item is'; proposed Methodology clause.

CONVENTIONS retains `sent / received / statement accepted / adopted use`. The proposed item has only `open / acknowledged / dispositioned / closed` and says filing is **not** sending. This is correct, but then the sentence 'the four states above are read off the item's state and the receiver's ledgers' is not a defined mapping. In particular an `open` filed item does **not** establish sent, nor does `dispositioned` with a rejection establish statement accepted. `closed` by explicit no-action/rejection is not adopted use. Keep owner autonomy and no PI routing; do not add a mandatory extra status if unnecessary. Instead define `state` as the *queue lifecycle only*, explicitly distinguish the four notice events as optional evidence citations and restrict 'adopted use' to the receiving Import Ledger or release record. Say **not all four notice states can be inferred from queue state**. Where no distinct formal notice was sent, record `notice not sent / not applicable` without pretending otherwise. All seven day-one items remain `open`, with no recipient action implied.

**Acceptance:** no assertion that state mechanically implies sent/statement accepted/adopted use; specify whether `kind: notice` merely means a candidate notice in the inbox until receipt, and where a genuine sender/recipient event is documented.

### PIPES-R2 — checker has non-failing bypasses (BLOCKING for claimed validation)

**Location:** `tools/pipes_index.py` `validate_item`, `run`, `selftest`.

1. `if tags and t not in tags` skips tag validation entirely when no tags are visible (e.g. shallow/missing tags or incorrect repo root), producing false PASS. Require a nonempty verifiable tag set when validating real items and always reject an unknown item tag. A standalone selftest may pass a controlled fixture tag set.
2. `date` checks format only; does not check that its `YYYYMMDD` equals filename date or that the ISO date is valid. Enforce both.
3. `tags: []` is accepted even though all items must declare object tags; `object` and tags require nonempty values. `dispositioned/closed` needs a dated verdict **and receiver record/ledger pointer**, not any arbitrary nonempty `disposition` string.
4. `selftest` has **nine cases total: one positive and eight negative**, not '9/9 negative controls'. The comment about hand-edited indexes says a control exists, but `selftest` never tests the index comparison; test the real `--check` path against a tampered index, or describe the existing code path as a non-replayed feature. Add a check that a file path outside a recognized stream inbox cannot bypass process validation.

**Acceptance:** updated script/tests reject missing git tags, invalid/mismatched date, empty tags, malformed disposition, hand-tampered INDEX, and unknown inbox; honest positive/negative counts. Producer supplies stdout and exit statuses. No new scientific campaign is needed.

### PIPES-R3 — proposed pilot not yet adopted (NONBLOCKING editorial, fix with same patch)

**Location:** `pipes/README.md` title `(pilot v0.1, adopted by the PI 26 Oct 2026)`, and `CONVENTIONS.md` `(pilot v0.1, PI decision 26 Oct 2026)`.

PI approved the **concept** of pilot installation in the conversation; PR #66 is still open. Distinguish authorization to prepare/implement a pilot from merged and operative repository convention. Use 'PI-authorized pilot candidate, pending merge' before merge, or cite the precise PI authorization and keep 'adopted' for after PI merges this exact implementation. No need to block pilot on Methodology v1.5: the pilot clause remains a proposal.

### PIPES-R4 — attribution and notice provenance for proxy filings (NONBLOCKING but consequential)

**Location:** seven initial files, particularly `pipes/NUMGEN/20261026-RECOG-a1b-slip-schedule-informed.md` and `pipes/UVM/20261026-GEN-kappa-f-b-star-sourced-junction.md`.

`from: RECOG` and `from: GEN` currently express **scientific source identity**, while Atlas physically files the item on behalf of that stream. The record body discloses this. Make the rule explicit in README: `from` denotes provenance of the originating owner claim, **not a claim that the owner personally sent/approved this exact pipe text**; proxy filing must cite the source record and show a proxy-by-Atlas note. Recipients retain independent choice; `kind: notice` + `state: open` is not evidence of an official delivered notice.

### PIPES-R5 — operating boundary (ACCEPT)

One inbox per stream, no duplicate out-folder, owner-controlled dispositions, check-point reading, generated INDEX, and keeping scientific content in authoritative DSNs/consumer Import Ledgers are sensible and low-maintenance. The pilot may operate with zero new scientific adoption or notifications; the deferred Methodology proposal is appropriately noncanonical.

## Requested action

One batch for R1–R3 and the one-sentence proxy convention R4. Rerun script `--check`, `--selftest` and tampered-index negative fixture. Return changed lines and results for a short readback. No need to reopen the seven scientific issues or modify adopted scientific owner DSNs. PR #66 remains unmerged pending receiving acceptance.
