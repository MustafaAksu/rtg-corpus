# ATLAS — Co-owner Session Orientation

**Status:** [SESSION] LIVING WORKING NOTE — pilot, noncanonical. Not an owner DSN, a scientific authority, a release/adoption record, or an Atlas L5 diagnostic.  
**Checked:** 6 November 2026, against GitHub `main` through PR #187 (`e4f3dbf1ba97cf115c3615c335e613f9d0d62953`). Revalidate all mutable fields on entry.  
**Working roles:** Claude is the Atlas owner/editor; ChatGPT is the independent Atlas co-owner/reviewer; the PI (Mustafa Aksu) has the sole final decision on adoption and publication. The Atlas advises scientific owners, but never changes their claims.  
**Author of this checkpoint:** ChatGPT [SESSION]. Owner updates and independent review inputs can amend this **same fixed-path file** through separate, reviewable PRs.  
**Handover target:** a replacement session that has no access to earlier conversation text. No memory, private scratchpad or uncommitted work is assumed to survive.

## 1. Start here — verified sources before new analysis

Read in this order; do not treat this note as a shortcut for the sources:

1. `CONVENTIONS.md` on `main`; adopted `methodology-v1.4` (`dsn/DSN_METHODOLOGY.md`) §§6.1–6.3, 12–13. **Until a successor is adopted, v1.4 governs.**
2. This orientation file (at the branch/commit in which it is actually available), then `atlas/RTG_STATE_ATLAS_METHOD.md` at `atlas-v0.10` (Method v0.2).
3. `atlas/RTG_STATE_ATLAS.md` at **annotated** `atlas-v0.10`; `records/atlas/RTG_STATE_ATLAS_v0.10_RELEASE_RECORD.md` (frozen PI decision) and `records/atlas/RTG_STATE_ATLAS_v0.10_TAG_VERIFICATION.md` (post-tag identity). The frozen release record still narrates pending publication; the later tag-verification record governs that *subsequent event*, not the science.
4. `BASELINE.md` and `pipes/ATLAS/INDEX.md` on current `main`; list open PRs and branches affecting `atlas/`, `records/atlas/`, `pipes/ATLAS/` and its source manifest. Read any open pipe item itself, not just its index.
5. For a consequential scientific statement, open its **owner DSN at its governing adopted tag**, targeted section, RID and evidence restrictions. The Atlas is a navigation map, never an owner substitute.

**Entry verification:** report observed tags/commits, the exact read extent, whether this checkpoint is stale, active branch/PR and pipe states, and the next eligible action. If a tag, owner edition or required record cannot be checked, mark the dependency `[UNVERIFIED]` and stop only the affected conclusion. A PR, a release record's draft wording, a tool PASS or an orientation sentence alone never proves adoption.

## 2. Last VERIFIED checkpoint (historical, not an instruction to repin)

| Field | At 6 Nov 2026 |
|---|---|
| Governing Atlas | `atlas-v0.10`, **NONCANONICAL derived map**, PI accepted 6 Nov 2026 |
| Tag target | `28516ddf10cf7ba67634cdecf17bec0e6e6b4404` (merge PR #185) |
| Exact Atlas SHA-256 | `443b5990e6082599d1f43fca7d4d24e512e7a632ec395aa56f05bed16f53dbf7` |
| Source snapshot *inside* v0.10 | `fa3db80a935a20b1eff64b0e14c6d0436f861852` (3 moved tagged sources: GEN v2.10, RECOG v0.3.27, Programme v1.4; 15 unchanged) |
| Most recent post-release `main` checked | `e4f3dbf1ba97cf115c3615c335e613f9d0d62953` (PR #187 merge) |
| Atlas inbox | **7/7 closed** at that post-release `main`; `tools/pipes_index.py --check` passed, 88 items / 20 inboxes (producer/PI-reported and GitHub index checked) |
| Publication evidence | PR #186 independent receiving review → PR #185 Atlas merge → annotated `atlas-v0.10` → PR #187 post-tag verification/inbox closeout; no tag rewrite |
| Atlas next-edition draft | None confirmed at this checkpoint. The session-orientation pilot is a **working-record PR**, not an Atlas scientific refresh. |
| Methodology | `methodology-v1.4` adopted; any v1.5 session-orientation proposal is **DRAFT until separately accepted and tagged** |

**Identity caveat.** The Atlas v0.10 frozen source snapshot records **87** pipe items; the post-tag `main` records **88** after LIT traffic. The two counts refer to different commits, not a mismatch requiring an Atlas rewrite. Recheck at the next snapshot; do not silently update v0.10.

## 3. Scientific navigation — owner decisions still pending elsewhere

These are *navigation pointers to owner-held obligations*, not work items assigned by Atlas or grounds to edit an owner DSN:

| Atlas pointer | Responsible owner / next event |
|---|---|
| `F30` | **TRIAD** may decide whether to repin GEN's P4 identity and use the source's birth-symmetry `[ALG]` instead of its historical `[THM]` import. GEN's two answers are filed in `pipes/TRIAD/`; producer answer is not consumer adoption. |
| `F14` | **GEN** original `GEN-ART-G2-CHRONO` / `GEN-ART-P4-PRIMITIVE` proof-source custody remains missing. Independent G2 algebra and P4 identity are not recovery of the original coefficients' certificate. |
| `c_J`, `c_7` | **DYAD** decides whether to register its own bounds. RECOG's `RECOG-ALG-A1C-JET-REMAINDER-BOUNDS` proves RECOG-scoped ceilings; it is not a DYAD claim. |
| TDR-G export gate | **TDR-G** `TDRG-EXPORT-DISCRETE-TRIAD` still carries historical D/A/B wording in one §7 export row; the current owner launch gate is A→B→C, not completed. |
| `BASELINE.md` RECOG metadata | **RECOG** owns the obsolete “tag to be created” note, even though `recog-v0.3.27` has been tagged. |
| LIT notices after Atlas snapshot | Check `pipes/LIT/`, affected receiving inboxes and release records. Literature/queue changes do **not** become adopted owner science or automatically trigger an Atlas re-extraction. |

**Atlas refresh trigger:** a new governing source tag, a change in representation/schema or diagnostic semantics, or a source/consumer change that actually affects Atlas nodes. Freeze a new manifest; re-extract changed sources and affected dependency edges, then issue dispositions and verify. Do not repin an owner consumer by implication. Read the Atlas method §7.

## 4. Co-owner lanes and immediate safe actions

**Atlas owner/editor (Claude):** Maintains the Atlas-derived map and method, source manifest, impact-builder, diagnostics, review packet and Atlas receiving queue. When a new owner tag or material finding appears: freeze input identities, prepare one scoped refresh, request independent review, and seek PI adoption. Close queue items only after their receiver disposition and appropriate post-tag step.

**Independent Atlas co-owner/reviewer (ChatGPT):** First verify current owner/tag/queue evidence and the precise requested delta. Independently challenge scientific scope, imports, source identity and selected computational claims as appropriate. Record a change-focused English review under `records/atlas/` on a `chatgpt/*` branch and PR. Never change an Atlas owner candidate or owner scientific DSN merely because an independent review recommends correction. Mark independent runs separately from producer-reported runs.

**Current immediate action:** No active Atlas release decision was outstanding at this checkpoint. If no new source tag, valid inbox item, material inconsistency or PI task is present, there is **no forced Atlas action**. A new session should confirm that fact, rather than creating administrative work to fill the gap.

**If new work exists:** (1) identify the governing tag and exact changed claims; (2) inspect the owner and consumer pins, evidence limitations and new pipe messages; (3) make a scoped plan with acceptance criteria and an explicit PI decision boundary. Keep independent owner dispositions separate until reconciliation.

## 5. Keep this record usable after abrupt session loss

Update this **single working file** at meaningful, natural checkpoints, without waiting for the conversation to end: a new PR/branch or review verdict, a completed reconciliation, a PI adoption plus tag, a material blocker or its removal, and a significant change in the next action. Update it before entering an unusually long calculation/review when the continuation state is otherwise only in chat. A minor message, a completed read with no changed state or unchanged owner science does not need an edit.

For each update: specify who checked it, when, **what sources and portions were actually reverified**, exact branch/PR/commit of ongoing work, pending decision and the next concrete action. Remove stale operational text rather than stacking session diaries; Git preserves the past working-note commits. Keep this file compact (target ~1,000–1,500 words, not a hard gate); link to detailed reviews and release records rather than copying science, proofs, open-issue matrices or full PR transcripts. Co-owners update on separate branches and PRs; avoid concurrent silent overwrites.

**Fail-safe:** Work not committed to the repository (private reasoning, local scripts, an unsubmitted draft) may be lost when a session ends. Mark it `not committed / not verified`; do not claim it was preserved. This file is a continuation aid, not durable storage for evidence, source uploads or unpublished approvals.

### Replacement-session bootstrap message

> Take the Atlas co-owner/reviewer role. Read `records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION.md` and `CONVENTIONS.md` on the current repository; verify `methodology-v1.4` or its latest adopted successor, the latest *adopted* Atlas tag and its release/tag-verification records, `BASELINE.md`, `pipes/ATLAS/INDEX.md`, and open Atlas PRs. Report exact versions, checked sections, stale orientation details and the next eligible action. Treat this orientation as [SESSION], not owner science, and do not merge/tag/adopt.
