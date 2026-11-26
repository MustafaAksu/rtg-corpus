# RRF — co-owner session orientation

**Status:** operational continuity note, [SESSION] / NONCANONICAL; initial structure reviewed and PI-merged under CONVENTIONS §9 (#397, #399). No new source authority.
**ENTRY — shared**
- Repository `MustafaAksu/rtg-corpus`; read CONVENTIONS, this note, BASELINE, governing RRF tag + adoption record, pipes/RRF/INDEX.md and actual open items. Refresh tags, hashes, PRs, queue at entry. No shared writes during entry.
- PI decides scientific scope, source status, adoption/publication. ChatGPT prepares and edits; Claude independently reviews. Assignment given by PI in RRF activation conversation on 26 Nov 2026; not a new release. No PI signature inferred for historical records.
- RRF authority: working representation standard, not technical theorem or ontology ownership. Current source baseline is rrf-v0.8.4. Separate passive chart, model change, physical gauge, and ontology. Never promote owner-reported or noncanonical material by reference.
- Ordered gates: S0 source custody → independent acceptance A1–A8 → S1 claim/interface sync → S2 bounded maintenance with separate scope/science and compaction stages. BR-Q2 is the first bounded scientific question, eligible after S1 corrected-head acceptance and PI merge and opened by PI; it need not await S2 release. OPEN-A then OPEN-B → E1 → E2. No science before S0 acceptance.
- PI_PENDING: v0.9 S2b independent review and adoption/release decision; proposed local identity registration; BASELINE provenance only at PI decision; PRR v0.3 and GIIL separate owner/status decisions. Proposed OPEN closure wording PI_PENDING; no separate explicit approval record established.

## ChatGPT — preparer lane
Check stamp: 2026-11-26; checkpoint main `5bb35b9aa531891659e8b7f4c99a027b0eef4b72`. S0/S1/S2a ACCEPTED SCOPED; #406 and #410 merged by PI authority (review/SESSION only). S2a freeze `98da97c311a917d1539b9c31afaba779bc75a73f`, SHA-256 `390f75e447b7d5a9dcb01810d7eb513e9feef3c157f0de2f2f79afb259b39d72`. PI accepted S2b; draft branch `chatgpt/rrf-v0-9-s2b`, candidate SHA-256 `90fc4eb5cb732d4511ce958bac7708e9420b4ab62a3332fa79f6fa600e6dd47e`; movement map and build review `records/rrf/RRF_V0_9_S2B_BUILD_REVIEW.md`. No BR-Q2 result incorporated; #414 awaits independent mathematical review. Tried/rejected: date-only repin; physical identification from coordinate change; treating raw shared checker as RRF-compatible. Reviewer #418 / 6079644693: adapter accepted for this edition; C1/C2 corrected, native readback pending. G1 requires frozen S2a commit/full hash in release record and merge-commit-only integration with ancestry verification. Next: (1) corrected-head reviewer readback; (2) explicit PI closure wording and adoption/release decision, then G1 and publication checks; (3) separate BR-Q2 reconciliation and owner/PI disposition. No unreviewed science or release.

## Claude — independent reviewer lane
Check stamp: 2026-11-26; checkpoint `main` `f2056cf8`.
- S0: ACCEPT SCOPED on #397 at `44fac173`.
- S1: ACCEPT SCOPED after readback on #400 at `2c087763`.
- S2a: ACCEPT WITH CHANGES on #404 at `6a7b27de`; C1/C2 readback ACCEPT SCOPED at `98da97c3`, freeze hash `390f75e4…9d72` pending the PI decision on the closure wording (`records/rrf/RRF_S2A_REVIEWER_VERDICT_PR404_20261126.md` §5). A1 and A2 are met. A3 has two required changes: C1 restores three dropped pointers (RF-O09-03, SG-15, the P2-B v2 evidence zip), with `evidence/rrf/scripts/rrf_s2a_preservation_check.py` exiting 0; C2 sets the OPEN ID format, with the closure-criteria wording a PI item.

Held: no science opened. PRR v0.3, GIIL, S2b and release are PI or owner decisions. Tried and rejected: none.

Next:
1. S2b review from the frozen hash, done when every moved block is matched by the compaction map and the preservation check passes against `390f75e4…`.
2. BR-Q2 independent derivation, done when there is a verdict with scope, an explicit bridge or refusal, and a counterexample search on record.
