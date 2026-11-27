# RRF — co-owner session orientation

**Status:** operational continuity note, [SESSION] / NONCANONICAL; initial structure reviewed and PI-merged under CONVENTIONS §9 (#397, #399). No new source authority.
**ENTRY — shared**
- Repository `MustafaAksu/rtg-corpus`; read CONVENTIONS, this note, BASELINE, governing RRF tag + adoption record, pipes/RRF/INDEX.md and actual open items. Refresh tags, hashes, PRs, queue at entry. No shared writes during entry.
- PI decides scientific scope, source status, adoption/publication. ChatGPT prepares and edits; Claude independently reviews. Assignment given by PI in RRF activation conversation on 26 Nov 2026; not a new release. No PI signature inferred for historical records.
- RRF authority: working representation standard, not technical theorem or ontology ownership. Governing edition is rrf-v0.9 (annotated tag and release record; verified post-tag record records/rrf/RRF_V0_9_POST_TAG_RECORD_20261127.md). Separate passive chart, model change, physical gauge, and ontology. Never promote owner-reported or noncanonical material by reference.
- Ordered gates: S0 source custody → independent acceptance A1–A8 → S1 claim/interface sync → S2 bounded maintenance with separate scope/science and compaction stages. BR-Q2 is the first bounded scientific question, eligible after S1 corrected-head acceptance and PI merge and opened by PI; it need not await S2 release. OPEN-A then OPEN-B → E1 → E2. No science before S0 acceptance.
- PI_PENDING: PRR v0.3 source/status decision; BR-Q2 disposition/adoption after independent reconciliation. GIIL dispositions remain with GEN/RER owners; no source-status promotion. v0.9 publication verified; all four approved OPEN closure criteria and ACTIVE states retained. Outgoing PROG/RER dispositions belong to their receivers.

## ChatGPT — preparer lane
Check stamp: 2026-11-27; checkpoint main `41f14723bd7dab301a1e2f541476e76eadadfa99`. S0–S2 ACCEPTED SCOPED and v0.9 published. PI decision 7213581950; final DSN SHA-256 `28c9c101c715b402b5ed60eeab8bfa2c7e5e637fef3cd2b00961dfa60553075d`; tag object `92c4762540b6d46b882dbd5a1091b546e61dd716` → `0d79defef39d8fa87ba3c84bf5d13b6d55739615`; tag/main blob and G1 ancestry verified. Post-tag #426 merged; native checks source-reported in the post-tag record. Nine notice closeout proposed in `records/rrf/RRF_V0_9_INBOX_CLOSEOUT_20261127.md`, branch `chatgpt/rrf-v0-9-post-tag-closeout-20261127`; BR-Q2 question unchanged. No new science or DSN amendment. Tried/rejected: bulk date repin, physical gauge from chart, treating custody or notice closure as adopted scientific use. Next: (1) independent scoped closeout readback/native pipes check then PI merge; (2) BR-Q2 #414 independent result reconciliation with #410, complete on explicit per-result verdict and counterexample scope, then PI disposition and scoped OFN response; (3) after BR-Q2, OPEN-A then OPEN-B→E1→E2 at approved closure criteria. PROG/RER receiver dispositions separate.

## Claude — independent reviewer lane
Check stamp: 2026-11-27; checkpoint `main` `0d79defe` (`rrf-v0.9` published and verified; `records/rrf/RRF_V0_9_POST_TAG_RECORD_20261127.md`).
- S0: ACCEPT SCOPED on #397 at `44fac173`.
- S1: ACCEPT SCOPED after readback on #400 at `2c087763`.
- S2a: ACCEPT WITH CHANGES on #404 at `6a7b27de`; C1/C2 readback ACCEPT SCOPED at `98da97c3`, freeze hash `390f75e4…9d72` pending the PI decision on the closure wording (`records/rrf/RRF_S2A_REVIEWER_VERDICT_PR404_20261126.md` §5). A1 and A2 are met. A3 has two required changes: C1 restores three dropped pointers (RF-O09-03, SG-15, the P2-B v2 evidence zip), with `evidence/rrf/scripts/rrf_s2a_preservation_check.py` exiting 0; C2 sets the OPEN ID format, with the closure-criteria wording a PI item.
- S2b: ACCEPT WITH CHANGES on #417 at `917f76ef`; C1/C2 readback ACCEPT SCOPED at `8de7a8cd`, candidate `2950dbc0…942d` (`records/rrf/RRF_S2B_REVIEWER_VERDICT_PR417_20261126.md` §6). C1 restores the predecessor adoption-record pointer; C2 cites the PI decision record for the closure wording or restores PI_PENDING. G1 release gate: intermediate `98da97c3` is named in the release record and kept reachable by merge commit. The adapter is accepted for this edition with stated limits.
- v0.9 release readback: ACCEPT SCOPED at #417 `638a1a8b`, final DSN `28c9c101…075d`, ready for publication (`records/rrf/RRF_V0_9_RELEASE_READBACK_20261127.md`).
- BR-Q2: independent derivation merged (#410); the preparer's #414 awaits review.

Held: no science opened. PRR v0.3, GIIL, S2b and release are PI or owner decisions. Tried and rejected: none.

Next:
1. Done: post-tag readback.
2. Review of #414 against #410, done when there is a reconciliation verdict per result (agree / differ / scope) with counterexample checks.
