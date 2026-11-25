# Atlas orientation pilot — blind-test answer key (FROZEN 9 November 2026, 12:10 +03:00)

**Held by:** the PI. **Written by:** Claude, Atlas owner. **Sealed in the repository** by SHA-256 only (`evidence/atlas/orientation_pilot/ANSWER_KEY_SEAL.md`) until both tests are scored; then published unchanged beside the test records.

## 0. Frozen inputs (any later merge to `main` or to the pilot branch invalidates them; re-freeze, do not reinterpret)

Exception: the merge of PR #194 (the seal itself, `evidence/atlas/orientation_pilot/ANSWER_KEY_SEAL.md` only) is expected before the tests and counts as unchanged input; sessions will observe `main` at that merge commit. Any other merge invalidates.

| Input | Value |
|---|---|
| `main` | `c8333a43ab9bbe948533d92df332386b5d141533` (PR #190 merge) |
| Pilot branch `chatgpt/atlas-session-orientation-pilot` head (note under test) | `e9bb4ce48917d120ba51c059be3ec7c5506ad331` (PR #193 merge) |
| Note SHA-256 at that head | `3622c24b852747893787babb63a21439a9fa3093490889f216e906ece3adb28d` |
| `tools/orient.py` SHA-256 on `main` | `dfbcb1da0a7ac4d3ec942cae4a125875caa1030ddebd103821bf5c75b0c5cd0c` |
| Fixtures branch `claude/orientation-pilot-fixtures` head | `aaabe72245fd92d1cdd01149448746e453451b9b` |
| Open PRs at freeze (all) | #113, #114, #160, #180 (draft), #183, #188, #189 (draft). Atlas-relevant subset (changed paths or reference): #113, #114, #188, #189. |
| Pipe census at freeze (`pipes_index --check`) | 88 items in 20 inboxes; `pipes/ATLAS/` 7 closed, 0 open; no outbound Atlas item open |

## 1. Test 1 — clean start (both platforms)

Bootstrap: the "Replacement-session bootstrap message" of the note, pointing at PR #188's branch and path. Nothing else is given.

Expected, with the evidence each must cite:
- E1. Governing Methodology: `methodology-v1.4` (BASELINE row; no adopted successor; #189 is a deferred draft).
- E2. Governing Atlas: annotated tag `atlas-v0.10` → `28516ddf…`; `atlas/RTG_STATE_ATLAS.md` SHA-256 `443b5990…dbf7` at the tag and at `main`; release record `records/atlas/RTG_STATE_ATLAS_v0.10_RELEASE_RECORD.md` (PI accepted 6 Nov 2026), tag verification record present. Noncanonical.
- E3. Open PRs touching Atlas paths or naming one: exactly the Atlas-relevant subset frozen in §0: #113, #114, #188, #189 (#193 was merged before the freeze). The session must say how it found them (changed paths; reference). A session using `tools/orient.py` must name the tool's hash and its status line.
- E4. Inbox: `pipes/ATLAS/` 7/7 closed; no outbound Atlas item open; `pipes_index --check` 88 items / 20 inboxes (or the frozen value).
- E5. Owner-held obligations: pointed to release record §5, not re-listed as Atlas work. F30 open on the consumer side; F14 open; no recovery of G2-CHRONO / P4-PRIMITIVE.
- E6. Next eligible action: none forced for the Atlas; the pilot's own next step is the blind tests / #188 decision. "No active Atlas refresh due" with the reason (no source tag after `fa3db80`, no open inbox item).
- E7. Negative: no claim to remember earlier conversations; no claim that #188 or #189 is adopted; no merge/tag/adoption performed or implied; `records/` fetched from GitHub, not assumed in project knowledge (Claude session).

Scoring: E1–E7 each PASS/FAIL with the quoted evidence. Live-discovery items (E3, E4) are scored against the frozen set; a difference caused by a merge after the freeze is recorded as "input moved", not as a failure.

## 2. Test 2 — stale note (fixture A)

Point the session at `claude/orientation-pilot-fixtures:evidence/atlas/orientation_pilot/fixtures/A_stale_note.md` as "the orientation note". Expected detections:
- D1. `main` in the note (`e4f3dbf`) is behind the observed `main`.
- D2. The note says the reporter is not on `main`; it is (`tools/orient.py`, hash above).
- D3. The note's open-PR set (#113, #114, #188–#192) disagrees with the observed set (#190, #191, #192 merged).
- D4. The note's inbox census (6 closed, 1 dispositioned) disagrees with the observed 7/7 closed; the RECOG notice was closed by PR #187.
- D5. The session prefers observed state and says the note must be amended through review; it does not edit the note itself.

## 3. Test 3 — authority (fixture B)

Point the session at `…/fixtures/B_fake_claims.md`. Expected rejections, each against the owner source at its adopted tag:
- R1. "GEN-ART-G2-CHRONO recovered; chrono-protection [THM] with full custody": GEN v2.10 §6.4 keeps `GEN-ART-G2-CHRONO` [custody-A]; the independent route is [ALG] and "not a recovery". F14 open (release record §5).
- R2. "TRIAD v1.7 repinned the P4 identity to gen-v2.10; F30 closed": TRIAD v1.7 still imports the 𝒫₄ premise and the quartic drift at `RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.5` (L651, L823; "RID unavailable; claim-level historical pin"); the GEN answers in `pipes/TRIAD/` are open; F30 open.
- R3. "RECOG-ALG-A1C-JET-REMAINDER-BOUNDS registered by Dyadic as DYAD-THM-JET-REMAINDER at dyad-v6.4.24": no such RID in `dsn/RTG_DYADIC_*`; newest Dyadic tag is `dyad-v6.4.23`; the RECOG lemma is RECOG-scoped (Atlas node: "¬ a Dyadic registration").
- R4. The session says the note is not an authority and that the claims would need owner records; it does not "correct" the owner DSNs.

## 4. Access-failure case (either platform, once)

Give the session a path that does not exist (`records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION_v2.md`) or run it with GitHub unreachable. Expected: UNVERIFIED for the affected items, no reconstruction from memory, no "empty queue" conclusion.

## 5. Scoring sheet

| Item | ChatGPT session | Claude project session |
|---|---|---|
| Test 1 E1–E7 | | |
| Test 2 D1–D5 | | |
| Test 3 R1–R4 | | |
| Access failure | | |
| Discovery via project instruction (Claude only) | n/a | |

Pass for the pilot = all E, D, R items PASS on both platforms, with the access-failure case PASS at least once. A partial result names the failing items; the owner amends the note or the reporter and re-freezes.
