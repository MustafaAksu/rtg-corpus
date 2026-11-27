# RRF — co-owner session orientation

**Status:** operational continuity note, [SESSION] / NONCANONICAL; initial structure reviewed and PI-merged under CONVENTIONS §9 (#397, #399). No new source authority.
**ENTRY — shared**
- Repository `MustafaAksu/rtg-corpus`; read CONVENTIONS, this note, BASELINE, governing RRF tag + adoption record, pipes/RRF/INDEX.md and actual open items. Refresh tags, hashes, PRs, queue at entry. No shared writes during entry.
- PI decides scientific scope, source status, adoption/publication. ChatGPT prepares and edits; Claude independently reviews. Assignment given by PI in RRF activation conversation on 26 Nov 2026; not a new release. No PI signature inferred for historical records.
- RRF authority: working representation standard, not technical theorem or ontology ownership. Current source baseline is rrf-v0.8.4. Separate passive chart, model change, physical gauge, and ontology. Never promote owner-reported or noncanonical material by reference.
- Ordered gates: S0 source custody → independent acceptance A1–A8 → S1 claim/interface sync → S2 bounded maintenance with separate scope/science and compaction stages. BR-Q2 is the first bounded scientific question, eligible after S1 corrected-head acceptance and PI merge and opened by PI; it need not await S2 release. OPEN-A then OPEN-B → E1 → E2. No science before S0 acceptance.
- PI_PENDING: independent v0.9 publication readback, merge/tag/BASELINE authorization; PRR v0.3 and GIIL separate owner/status decisions. PI adopted v0.9 exact reviewed candidate (PR #417 comment 7213581950); all four OPEN criteria approved (7202555052); all remain ACTIVE.

## ChatGPT — preparer lane
Check stamp: 2026-11-27; main checkpoint `c167f80701eb706bca520b4aafcdab1b546a40a9`. S0/S1/S2a/S2b ACCEPTED SCOPED; final S2b readback 6085047516 at `8de7a8cd338f37bce3a73910648eecc9a5628b2c`. PI adopted v0.9 (7213581950); publication record `records/rrf/RRF_v0_9_RELEASE_RECORD.md`, final prepared DSN SHA-256 `28c9c101c715b402b5ed60eeab8bfa2c7e5e637fef3cd2b00961dfa60553075d`. Governing tag remains rrf-v0.8.4 until authorized publication. S2a frozen ancestor `98da97c311a917d1539b9c31afaba779bc75a73f` (390f75e4…9d72) mandatory G1; #417 merge commit only, verify ancestry; #418 separate reviewer record. Two prepared notice items (PROG IF30/31/33, RER IF33), no transmission/receipt/adopted use asserted. Tried/rejected: bulk date repin; physical gauge from chart; generic checker for RRF layout; inferring PI closure approval before explicit record. Next: (1) independent publication metadata/record/pipe check; (2) PI-authorized integration, tag and BASELINE readback; (3) separately reconcile BR-Q2 #414 and post-tag notice closeout. No unreviewed science.

## Claude — independent reviewer lane
Check stamp: 2026-11-27; checkpoint `main` `136d1c59`.
- S0: ACCEPT SCOPED on #397 at `44fac173`.
- S1: ACCEPT SCOPED after readback on #400 at `2c087763`.
- S2a: ACCEPT WITH CHANGES on #404 at `6a7b27de`; C1/C2 readback ACCEPT SCOPED at `98da97c3`, freeze hash `390f75e4…9d72` pending the PI decision on the closure wording (`records/rrf/RRF_S2A_REVIEWER_VERDICT_PR404_20261126.md` §5). A1 and A2 are met. A3 has two required changes: C1 restores three dropped pointers (RF-O09-03, SG-15, the P2-B v2 evidence zip), with `evidence/rrf/scripts/rrf_s2a_preservation_check.py` exiting 0; C2 sets the OPEN ID format, with the closure-criteria wording a PI item.
- S2b: ACCEPT WITH CHANGES on #417 at `917f76ef`; C1/C2 readback ACCEPT SCOPED at `8de7a8cd`, candidate `2950dbc0…942d` (`records/rrf/RRF_S2B_REVIEWER_VERDICT_PR417_20261126.md` §6). C1 restores the predecessor adoption-record pointer; C2 cites the PI decision record for the closure wording or restores PI_PENDING. G1 release gate: intermediate `98da97c3` is named in the release record and kept reachable by merge commit. The adapter is accepted for this edition with stated limits.
- v0.9 release readback: ACCEPT SCOPED at #417 `638a1a8b`, final DSN `28c9c101…075d`, ready for publication (`records/rrf/RRF_V0_9_RELEASE_READBACK_20261127.md`).
- BR-Q2: independent derivation merged (#410); the preparer's #414 awaits review.

Held: no science opened. PRR v0.3, GIIL, S2b and release are PI or owner decisions. Tried and rejected: none.

Next:
1. Post-tag readback, done when the tag target, the tagged DSN hash, both ancestries and the BASELINE row are verified on `main`.
2. Review of #414 against #410, done when there is a reconciliation verdict per result (agree / differ / scope) with counterexample checks.
