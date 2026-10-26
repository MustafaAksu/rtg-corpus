# Number Genesis v1.21 — Release Record

**Status:** ADOPTED by the PI, 26 October 2026 (§13). Publication pending: the merge commit and the annotated tag `numgen-v1.21` are the PI's steps and have not happened yet. Until the tag exists, `numgen-v1.20.8` remains the tagged governing edition on GitHub.
**Date:** 26 October 2026
**Prepared by:** Claude, Number Genesis co-owner session (branch `claude/numgen-v1.21-stage2`, stacked on PR #74).
**Edition:** v1.21, built in two stages under DSN Methodology v1.4 §13.6. Stage 1 makes the corrections. Stage 2 is layout-only compaction.
**Predecessor:** `RTG_NUMBER_GENESIS_DSN_v1.20.8`, tag `numgen-v1.20.8`, SHA-256 `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e`.

Fields marked *(to be filled)* depend on steps that have not happened yet: the merge, the tag and the notices. This record invents no hash, approval or review identifier. Every hash below was computed on the branch files.

## 1. Authorization and reviews

| Item | Source | State |
|---|---|---|
| v1.21 hand-over: disposition, stage 1, stage 2, release record, notices, held-record upload | PI and atlas owner, 26 Oct 2026 (hand-over attachment in the co-owner session) | received |
| Start of stage 1 | PI, 26 Oct 2026, verbatim: "başla" | given |
| Owner dispositions of the v1.20.8 advisory | `records/numgen/NUMGEN_OWNER_DISPOSITION_ADVISORY_v1_20_8_CLAUDE_20261026.md` (PR #70); `records/numgen/NUMGEN_OWNER_DISPOSITION_ADVISORY_v1_20_8_chatgpt_20261026.md` (PR #72) | filed; not merged |
| Reconciliation of the two disposition records | `records/numgen/NUMGEN_OWNER_DISPOSITION_RECONCILIATION_v1_20_8.md` (PR #73, atlas owner): no substantive difference; five form differences settled in favour of the ChatGPT labels and columns; `U_NG ≡ U_NUMGEN` | filed; not merged |
| Hash check of the held records | `records/numgen/NUMGEN_UPLOAD_HASH_CHECK_20261026.md` (PR #73): `upload/numgen-records/SHA256SUMS.txt` 278/278 OK (PR #69) | filed; not merged |
| Stage-1 review, round 1 (`702e3917…3880`) | ChatGPT co-owner on PR #74: ACCEPT WITH CHANGE. R1: no domain arrows in the acceptance matrix. R2: `upload/numgen-records` is a branch, so say what the release commit can reach | applied as round 2 |
| Stage-1 review, round 2 (`ab25c162…99d2`) | ChatGPT co-owner, 26 Oct 2026: round 2 ACCEPTED, **Stage 2 GO**. Limits: base `ab25c162…99d2` only; Methodology v1.4 layout and compaction only; no new claim, RID, grade or OPEN change; movement map, `tools/check_compaction.py` and negative controls required; this record DRAFT until PI adoption; atlas row check before final stage-2 acceptance; PR #74 not to be merged yet | given |
| Stage-2 review | ChatGPT co-owner on PR #76 (comment `6417476658`): SCIENTIFIC/COMPACTION SCOPE ACCEPTED; final acceptance conditioned on the atlas row check and the shared-tool review; G2/G3 byte guards are load-bearing and must stay | accepted (conditions met by PR #77) |
| Atlas row check (stage 1 rows and stage 2) | PR #77 (head `fff3e2f`): `records/numgen/ATLAS_ROW_CHECK_NUMGEN_v1_21_STAGE1.md` — stage 1 rebuilt byte-identical, C0–C13, NC1–NC12, A1 rerun, 45 edits checked at the owner tags: **CONCUR**; `…_STAGE2.md` — candidate and map rebuilt byte-identical, checker output identical, G0–G6, F1–F11: **ACCEPT FOR ADOPTION (atlas side)**. Non-blocking: E42 writes the RECOG v0.3.24 hash with a six-character suffix (`…69e7c1`); left for the next edition (§14) | done |
| Review of the `tools/check_compaction.py` extension (§5.3) | PR #77: diff read in full; DYAD v6.4.21, RECOG v0.3.23, RECOG v0.3.24, GEN v2.9 (+ fixtures) and Programme v1.3 rerun with the branch and the `main` checker, outputs byte-identical in all five; five extra atlas fixtures on the key FAIL as required (`evidence/atlas/rowcheck/numgen_v1_21/`): **ACCEPT** for `main`, two non-blocking notes for the next tool edition | done |
| PI adoption | PI, 26 Oct 2026, 22:46 +03:00, in the co-owner session: scope fixed by stage 1 `ab25c162…99d2` and stage 2 `05b3315f…4258`; no further scientific review or r4 needed for publication (§13) | given |

## 2. Identities

| Object | SHA-256 |
|---|---|
| Base: adopted v1.20.8 (`numgen-v1.20.8`), 339,003 bytes | `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e` |
| Stage-1 intermediate, round 1 (reviewed on PR #74; superseded by round 2) | `702e3917126edfeeda41e43b6a8ad820695b5feec19a61e724b12849dfb83880` |
| **Stage-1 intermediate, round 2 (accepted; the stage-2 base)**, 354,024 bytes, 3,471 lines; archived at `evidence/numgen/v1.21/stage1_intermediate.md`. A build stage, not an edition | **`ab25c162a727b0826adfb0b8fd5f3898969ed78260fc00e8bbcaa9e1e3b899d2`** |
| **Stage-2 candidate** `dsn/RTG_NUMBER_GENESIS_DSN.md`, 274,236 bytes, 2,970 lines | **`05b3315fe74ec006b5610b1823522f843f55d677c01f1ec39b42144dd4be4258`** |
| **Published file** `dsn/RTG_NUMBER_GENESIS_DSN.md` after the publication transform (§13.2), 274,246 bytes, 2,970 lines | **`4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701`** |
| Tag `numgen-v1.21` | *(to be filled by the PI)* |

| Build or check file | SHA-256 |
|---|---|
| `evidence/numgen/scripts/build_numgen_v1_21_stage1.py` | `1fc6ae0bcec76c4514acc9221938145db76ef506292103ab5d15fde4373267cd` |
| `evidence/numgen/scripts/check_numgen_v1_21_stage1.py` | `c3b7b9193dd256526874b2f9d9df2e997fd25342c4e4eabc6fa30191ccbc27e6` |
| `evidence/numgen/scripts/numgen_v1_21_stage1_checks.py` (gate A1) | `d4aa89dfd4e718a69215a5fccf895fdac6c1287e4529d9a5de7db12fc2d70567` |
| `evidence/numgen/v1.21/stage1_edit_log.json` (45 logged edits) | `d31eaee0e75ad7b256039fd4dbcd5e3590cd617767dfc55947abfdba9956813d` |
| `evidence/numgen/v1.21/stage1_check_output.txt` (C0–C13 PASS) | `83342647b8ee4f28be78b6f44e6dc19b933eca30539109ecbc3ad1a33ea58a42` |
| `evidence/numgen/v1.21/stage1_negative_controls_output.txt` (NC1–NC12 caught) | `eeecaa7d255ffd6b4ef96699467b297c675072f3c24728b694c407feaf76476e` |
| `evidence/numgen/v1.21/stage1_gateA1_output.txt` (A1 PASS; `--neg` fails as required) | `6344d5f574ec84c97d2687475dfd50eae93aa7e79d887a649230a1ad258c2a8e` |
| `evidence/numgen/v1.21/dsn_lint_stage1.txt` (informational) | `4da72526e7ca03dc6c4fcaba4411347aaea08f350637c267f808d8814c64e1fa` |
| `evidence/numgen/scripts/build_numgen_v1_21_stage2.py` | `495d9ac59934903fe90c6d00befc786453189b161deed22dac6f04bfa56f5caf` |
| `evidence/numgen/scripts/check_numgen_v1_21_stage2.py` | `9f1c3b8357119c5bd5fef8e4c3770621e065fc18c9bb7dd14cf4155a9c3433c2` |
| `evidence/numgen/v1.21/movement_map.json` (2 operations) | `fb93b2a95ba561516c736462c2b396db5991212300acbbaa3b59ba6cb31dbfa9` |
| `evidence/numgen/v1.21/check_compaction_output.txt` (PASS) | `9e8d2a7b334e8334428c60813e4d0700d6d52d1488ed3d51fb05973d82e7e977` |
| `evidence/numgen/v1.21/check_compaction_report.json` | `926bed3826e6a196f22911828fbbedd61c70db72d5d5c9798974cd105c566d6e` |
| `evidence/numgen/v1.21/stage2_guard_output.txt` (G0–G6 PASS) | `dcf82ef2a00d25aebfa90feae5b66a61f922a2b0c88a25ffa5bbb61ff4e65c7e` |
| `evidence/numgen/v1.21/stage2_negative_controls_output.txt` (F1–F11 caught) | `84f1f3980b639d15fa538bf7931f63b9a7e7cfb31cc8a5086336fdc3420c6d38` |
| `evidence/numgen/v1.21/dsn_lint_stage2.txt` (informational) | `b2c4415bfb88f9c7543cf006714c6e77630a42c01aa0fc909dd5b4b37a0114a1` |
| `tools/check_compaction.py` (branch; extended, §5.3) | `2ba2a4093391d069b38325783823ea48217a3a4637c252a2c9a517d89f087306` |
| `tools/check_compaction.py` on `main` before the extension | `6ed877986d47b485ca3dfcacbfb1493e93270af73a70bdb80533f58e5453b603` |
| `evidence/numgen/v1.21/tool_regression_summary.txt` | `b1e7ddcd58643d3ab09ffe5152c4dc603c23a9f961498d9ce718c69434b9566d` |
| `evidence/numgen/scripts/release_numgen_v1_21.py` (publication transform) | `19ff1869dfe2fdd75e1229d4c582abcd729685de6b43d47ca5e1fd54618b95f1` |
| `evidence/numgen/v1.21/release_check_output.txt` (P1–P6 PASS) | `5529724e9616b81c359e771eb0a3a1d899396a313202efbba1ce5d743bfb6709` |
| `evidence/numgen/v1.21/release_negative_controls_output.txt` (N1–N5 rejected) | `650747eb5f0228ff862b474b4148d7cfe9c17182af32ed90823f50006c967297` |

**Reproduce.** `git show numgen-v1.20.8:dsn/RTG_NUMBER_GENESIS_DSN.md > v.md`. Run the stage-1 builder on `v.md` to get `ab25c162…99d2`. Then run `build_numgen_v1_21_stage2.py ab25c162-file OUT MAP`. That gives `05b3315f…4258` and the map `fb93b2a9…dbfa9`. The stage-2 build was rerun from scratch on 26 Oct 2026 and both hashes reproduced. Then `release_numgen_v1_21.py CANDIDATE OUT "26 October 2026"` gives `4805760d…5701`; the candidate is also at commit `19432b9` (`git show 19432b9:dsn/RTG_NUMBER_GENESIS_DSN.md`).

## 3. Stage 1 — edits by disposition (round 2, accepted)

The edit log has 45 entries. Each has a key, group, row, mode, old and new text, and their hashes. Each is applied exactly once, is reversible (gate C2), and only touches the rows listed here. These are the dispositions of PRs #70 and #72 as reconciled in PR #73.

| Group | Change |
|---|---|
| Dyadic row-A import (NB-11) | §6.6 L-PHASE explicit-constant OPEN sub-item closed by the import of `DYAD-THM-LPHASE-ROWA-REMAINDER` (pin `dyad-v6.4.22` §6.14; producer edition v6.4.19). Import row in §9.1. 403/250 appears only in the import block and the matrix row (gate C9). The sampled L-PHASE range stays live as `[NUM]`. `NUMGEN-RESULT-N5AS1-L-PHASE` is unchanged. |
| RECOG explicit-domain results | Recorded as consumer-side confirmations: the §9.1 acceptance matrix (8 rows) and the RECOG v0.3.24 notice row. Nothing is imported. Domain column per R1: "NUMGEN: `U_NG`; RECOG: `U_R,base` (comparison only; no inclusion claimed)". |
| Domain labels | §6.2 alias table: `U_NG` (≡ RECOG's `U_NUMGEN`), `U_NG,tube`, `U_D,base`, `U_D,tube`, `U_R,base`. Explicit-domain pointers at L-BACKBONE, L-MONO, INF-1 and GAP-LOCK/INF-2. PRIM-CTR seed-domain label. Gate C12 checks that every label used is defined. |
| RIDs | Five result RIDs at their statements: `NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET`, `-GAPLOCK-COUNT`, `-GAPLOCK-SLIP-RATIO`, `NUMGEN-RESULT-N5AS1-INF2`, `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE`. Identifier-scope guard (§6.6): result RIDs sit under the module RID, and the RID category word is not a grade (Methodology §4.2). No collisions (gate C5). |
| Pins | Programme v1.3 (SG-PROG-1 firewall, SG-PROG-2 generator-selection guard, §9.1 row); Genesis v2.9 (§6.9a NG-10 source, §9.1 row); §7 N-3 item 7 Q403 pin aligned with the live imports at v6.4.18; §8 DZT provenance restated (the repository has `dzt-v0.8`; there is no DZT v0.17). |
| Evidence keys (§9.2) | Evidence-state and availability clause (R2: the held records are on the branch `upload/numgen-records` and are reachable at the release commit only if that branch is merged first). In-ledger keys for N5-C1–C4, C5, N5-PHYS-1, C7A, P3 and the NG-7A extension. The abbreviated hash is written as prefix…last four. |
| Owner alias | L1: `DYAD-ALG-P5-RADIAL` as the Dyadic owner name of ΔQ₅ (ΔQ₅ ≡ P₅, exact gate A1: sympy six-fold Taylor composition, ΔQ₄ = −Q², ΔQ₅ = P₅). §9.2 relay row for the Dyadic owner RIDs. |
| Scope words | N-1 tree, N-1A0 and N-1A1 status lines. SG-NG-23 cross-reading of exp(π/(3τ)). NG-0R-COV pin of the comparison conventions for φ* vs `C_D^ext`. No identity φ* ≡ `C_D^ext` is claimed. |
| Consumers | §9.2 RECOG rows (v0.3.5; v0.3.22) merged into one current row (RECOG v0.3.24) carrying both facts. §6.8 Foundations export: OFN v0.10 consumer pointer and additive-rank scope. |
| C7C-M4 | §2 item 1: HOLD, with the TDR-G request pointer and the sensitivity audit. C7C algebra and Census-1 INCONCLUSIVE / INCONCLUSIVE are unchanged. |
| Inbox | `pipes/NUMGEN/20261026-RECOG-a1b-slip-schedule-informed.md` dispositioned: `2026-10-26 · accept with change · dsn/RTG_NUMBER_GENESIS_DSN.md §9.1`. |
| Changelog | One stage-1 entry. Stage 2 replaced it with the Appendix A entry (§5). |

Tag-count delta over the whole file (gate C6): `[OPEN] −1`, `[THM] +1`, `[DEF] +1`, `[RESULT] +1`, `[from: NUM] +1`, `[PROVENANCE] −1` (E42 merges two rows). Gate C7 finds no grade change. Gate C8 finds exactly one OPEN removed: the L-PHASE explicit-constant sub-item, closed by the import.

## 4. Stage 1 — checks

| Check | Evidence key | Result |
|---|---|---|
| `check_numgen_v1_21_stage1.py` C0–C13 (base, build, reversibility, changelog, header, RIDs, tags, grades, OPEN, imports, sources, evidence paths, labels, R1/R2) | EV-RUN | PASS |
| Negative controls NC1–NC12 | EV-RUN | all caught |
| Gate A1 (`numgen_v1_21_stage1_checks.py`) | EV-RUN | PASS; `--neg` exits 1 as required |
| `tools/dsn_lint.py` | EV-RUN | informational |
| Campaign evidence of v1.20.8 (N-5, C7A, DISC, Census-1) | EV-NOT-RERUN | not rerun, as the hand-over requires. Cited at the hashes in the held records (PR #69) |

## 5. Stage 2 — layout-only compaction

### 5.1 Operations (movement map)

| Id | Operation | What |
|---|---|---|
| S2-H | `replace-header` | Current-only header, one field per line: Title, Date, Scope, Document class (with the §1 profile exception and "not itself an OPEN-P1 physical bridge (Programme v1.3 SG-PROG-4)"), Document status, Supersedes (one predecessor, full hash, tag), Companion documents (pointer to §9.1), DSN Methodology v1.4, Status summary (the first three sentences of the base summary, verbatim), Release record. Removed from the header: the Methodology note and the Pointer-validation note, both history. They are kept in the stage-1 archive and at the tag. |
| S2-T | `replace-section` (`history-appendix`) | From `## Appendix A. Working Thesis` to the end of the file. New Appendix A — Version History has one entry per edition (v1.21 DRAFT, v1.20.8, v1.20.7) and points to tag `numgen-v1.20.8` for the full changelog and the three legacy notes (v0.3 Change Note, v1.0 Result Note, v0.9 Result Note). Appendix B is byte-identical. The Working Thesis moves to Appendix C, changing only the heading letter, with a byte-identical body. One footer. |

The live body from `## §0.` to the first appendix heading is byte-identical to stage 1. `check_compaction.py` finds 253/253 claim blocks byte-identical, 0 changed, 0 unexplained.

### 5.2 Checks

| Check | Evidence key | Result |
|---|---|---|
| `tools/check_compaction.py` on (stage 1, candidate, map) | EV-RUN | PASS: mechanical scope, operations, base history region (79,981 chars relocated and archived), 253/253 claim blocks, RID set, anchors, hashes, qualifiers, references, presentation |
| `check_numgen_v1_21_stage2.py` owner guards G0–G6 (base; live body byte-identical; Appendix B byte-identical; Working Thesis body byte-identical; header; history archived with the tag pointer; checker PASS) | EV-RUN | PASS |
| Negative fixtures F1–F9 (through the checker), F4, F10 and F11 (through the guards) | EV-RUN | all caught (list below) |
| `tools/dsn_lint.py` | EV-RUN | informational |

Fixtures:
- F1: live §6.6 sentence changed without declaration.
- F2: `base_history_from` pointed at a live section (§9).
- F3: `base_history_from` names a heading absent from the base.
- F4: an Appendix B record deleted inside the declared tail.
- F5: Appendix A names an identifier absent from the live text.
- F6: two footer lines.
- F7: status summary gains a sentence not in the base summary.
- F8: archive replaced by unrelated bytes.
- F9: Supersedes lists two predecessors.
- F10: Appendix B records reordered.
- F11: a Working Thesis sentence changed inside the declared tail.

**Known checker limit, covered by owner guards.** S2-T replaces the whole tail. The checker therefore accepts any byte inside that tail as declared, including Appendix B and the Working Thesis, which this stage must not change. Guards G2 and G3 cover that region. Fixtures F4, F10 and F11 show the guards catch what the checker accepts.

### 5.3 Checker extension: `base_history_from` (needs atlas review)

NUMGEN keeps its history after the appendices: `## Changelog` and three legacy notes, about 80 kB. Before this extension, the checker counted that region as base live text. Every RID, hash and qualifier found only in the changelog was then reported as "lost" (for example `NUMGEN-FAIL-N5AS1-SECTION`, `RECOG-ALG-LATTICE-CLOCK`, `TDRG-ART-BIND3-N24K1`, and the hashes `423cd719…`, `9d59cfa1…`, `eef001d1…`).

The new optional profile key `base_history_from` names one `## ` heading of the base. The base live text ends at that heading. The new check "base history region" requires all of the following:
- the heading occurs exactly once;
- no `## §` or `## Appendix` heading follows it;
- the heading is absent from the candidate;
- the region is removed by a `replace-section`;
- the region is found in a named archive.

The key does nothing when absent. No existing check was removed or relaxed.

Regression (`evidence/numgen/v1.21/tool_regression_summary.txt`):

| Triple | Harness | Result |
|---|---|---|
| DYAD v6.4.21 | `tools/test_check_compaction.py` | 16/16. Output byte-identical to the run with the `main` checker, and to the file recorded for RECOG v0.3.23 (`0ab7f5f7…ccd0`) |
| RECOG v0.3.23 | `test_check_compaction_recog.py` | 17/17 |
| RECOG v0.3.24 | `test_check_compaction_move.py` | 12/12 |
| GEN v2.9 | `check_compaction.py` | PASS, output byte-identical to `main` |
| GEN v2.9 | GEN stage-2 fixtures | all caught |

The new key's own controls are fixtures F2, F3 and F8. The tool is shared by every stream, so the atlas owner must accept the extension before this edition is adopted.

## 6. Live-file exceptions kept on purpose

| Exception | Where | Why kept |
|---|---|---|
| LOGSLIP block (`NUMGEN-CAND-N5AS1-LOGSLIP`, `[COR] [historical formulation — superseded by v1.11/v1.16 closures]`, and the `[RESULT] [from: NUM]` numerical-test paragraph after it) | §6.6 | Disposition NA-06. Moving it out of §6 would move claim blocks. Stage 2 must not do that, and the checker operations cannot do it without a re-derivation. It stays in place and is marked historical. Relocating it is a separate, reviewed edit for a later edition. |
| Dated `[v1.20.x]` markers in rows that stage 1 did not touch (10 in the candidate) | §2, §6, §9 | Only rows the dispositions named were edited. Removing markers elsewhere would be undeclared editing. |
| §1 length beyond the v1.4 profile | §1 | Stated in the header (Document class: "§1 profile exception"). Shortening §1 is content work, not layout. |
| Informational lint counts: history words in live text (historical 11, superseded 6, former 6, retained as 4, no longer 5) | whole file | Reported by `dsn_lint.py` with no gate. They sit in guards and scope sentences the dispositions did not touch. |

## 7. Removals and name changes to note

- `RECOG-ALG-LATTICE-CLOCK`: stage 1 (the E42 merge of the two RECOG consumer rows into one current row) dropped this name from the §9.2 consumer row. The RID belongs to RECOG and stays in RECOG's own §7. NUMGEN does not cite it as an import. After stage 2 the name is in the NUMGEN tag history only.
- `NUMGEN-FAIL-N5AS1-SECTION` appeared only in the changelog. After stage 2 it is at tag `numgen-v1.20.8` (and in the stage-1 archive) only. It was never a live statement.
- Header Methodology note and Pointer-validation note: see §5.1.
- Working Thesis: Appendix A → Appendix C (heading letter only). No live text referred to "Appendix A" as the Working Thesis. The checker's reference check passes.

## 8. Pipe items (`pipes/`)

Inbox checkpoint: 26 Oct 2026 on `origin/main` (`252e803`) and on the open PRs. `pipes/NUMGEN/` holds one item only.

| Item | Direction | State | Disposition or note |
|---|---|---|---|
| `pipes/NUMGEN/20261026-RECOG-a1b-slip-schedule-informed.md` | inbound | dispositioned (stage 1, PR #74) | accept with change · §9.1. To be closed by the receiver after the tag. |
| `pipes/RECOG/20261026-NUMGEN-gap-lock-3-grade-of-import.md` (finding) | outbound | open | RECOG decides. NUMGEN v1.21 now names the GAP-LOCK lemmas by RID (`NUMGEN-RESULT-N5AS1-GAPLOCK-*`), so RECOG can cite the RID. The text is not corrected here; the notice (§9) carries it. |
| `pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md` (request) | outbound | open | C7C-M4 stays HOLD until TDR-G answers (§2 item 1). |
| `pipes/GEN/20261026-NUMGEN-cyclic-average-route-to-g2-zero.md` (offer) | outbound | open | The item says "(no RID yet)". v1.21 allocates `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE`. After the tag the sender adds a dated line with the RID, as a text correction only. |
| `pipes/DYAD/20261026-NUMGEN-q-star-branch-split.md` (question) | outbound | open | No answer from Dyadic. NC-17 deferred. |

## 9. Affected consumers and notices (after the tag)

One `kind: notice` item per consumer, filed by NUMGEN after `numgen-v1.21` exists. *(to be filled: paths and commits)*

| Consumer | What changes for them |
|---|---|
| RECOG | Acceptance matrix §9.1 (consumer-side confirmation; nothing imported); domain alias `U_NG ≡ U_NUMGEN`; GAP-LOCK and INF-2 RIDs; one current RECOG row in §9.2; inbox item dispositioned. |
| Dyadic | `DYAD-THM-LPHASE-ROWA-REMAINDER` imported at §6.6 (pin `dyad-v6.4.22`); owner alias `DYAD-ALG-P5-RADIAL`; Q403 pin at v6.4.18; q* question still open. |
| TDR-G | C7C-M4 HOLD pending the orientation-policy request; no change to C7C algebra. |
| Genesis | Pin Genesis v2.9 (§6.9a, §9.1); RID for the cyclic-average theorem named in the open offer. |
| OFN | §6.8 Foundations export: OFN v0.10 consumer pointer and additive-rank scope; the OFN §1.1 imports narrowed in v1.20.8 are unchanged. |

## 10. Size

| File | Bytes | Lines |
|---|---|---|
| v1.20.8 (adopted) | 339,003 | 3,412 |
| Stage-1 intermediate (round 2) | 354,024 | 3,471 |
| Stage-2 candidate | 274,236 | 2,970 |

Net change against v1.20.8: −64,767 bytes (−19.1 %). The history region (79,981 characters) moves to the tag. Stage 1 adds 15,021 bytes: the acceptance matrix, the domain table, the RIDs and the evidence keys.

## 11. Not done (by instruction)

- No rerun of the N-5, C7A or DISC campaigns.
- No change to the C7C algebra or to Census-1 INCONCLUSIVE.
- No ALG→THM promotion.
- No φ* ≡ `C_D^ext`.
- No action on outbound pipe items beyond text correction.
- No merge and no tag by this session: both are the PI's steps (§12).

## 12. Steps after adoption, in order

| # | Step | Who | State |
|---|---|---|---|
| 1 | Publication transform from the accepted candidate (§13.2); final SHA-256 | NUMGEN co-owner session | done: `4805760d…5701` |
| 2 | Adoption decision and final hash entered in this record | NUMGEN co-owner session | done (§13) |
| 3 | Reverse transform recovers the candidate byte-exactly (gate P4) | NUMGEN co-owner session | done |
| 4 | Merge commits (not squash), in dependency order: #69, #70, #72, #73, #74, #76, #77 | PI (CONVENTIONS: the PI merges into `main`) | *(to be filled: merge commits)* |
| 5 | Annotated tag `numgen-v1.21` on the merged commit carrying `4805760d…5701`, with the hash in the tag message | PI | *(to be filled)* |
| 6 | `BASELINE.md` NUMGEN row: entered on this branch (v1.21, `4805760d…5701`, tag `numgen-v1.21`); registration of the tag after it exists | row: NUMGEN co-owner session; tag registration: PI | row done; tag *(to be filled)* |
| 7 | Five `kind: notice` items (§9) and closure of the dispositioned inbox item; GEN offer text correction (RID named) | NUMGEN co-owner session, after the tag | *(to be filled: paths and commits)* |
| 8 | "Sync now" in the Claude project | PI | *(to be filled)* |

## 13. Adoption decision (PI, 26 October 2026)

### 13.1 Decision

Given by the PI on 26 October 2026 at 22:46 +03:00 in the NUMGEN co-owner session. Recorded verbatim in the parts that fix the scope:

> [SESSION — governance] Benimseme kapsamı şu iki nesneyle sabittir:
> Stage 1 — frozen intermediate `ab25c162a727b0826adfb0b8fd5f3898969ed78260fc00e8bbcaa9e1e3b899d2`;
> Stage 2 — accepted candidate `05b3315fe74ec006b5610b1823522f843f55d677c01f1ec39b42144dd4be4258`.
> Bilimsel içerik ve Methodology v1.4 sıkıştırması benimsendi. C7C-M4 HOLD, Census-1 INCONCLUSIVE ve diğer açık yükümlülükler mevcut statülerini koruyor.
> Yayın işlemi için ayrıca bir bilimsel inceleme veya r4 gerekmiyor.
> … PI bilimsel benimsemesi verilmiştir; yayın commit'i, merge ve tag henüz gerçekleştirilmiş değildir.

Summary in English: the scientific content (stage 1) and the Methodology v1.4 compaction (stage 2) are adopted, scoped by exactly the two hashes above. C7C-M4 HOLD, Census-1 INCONCLUSIVE / INCONCLUSIVE and every other open obligation keep their status. No further scientific review or round 4 is required for publication. Adoption is not publication: the merge and the tag follow (§12).

### 13.2 Publication transform

`evidence/numgen/scripts/release_numgen_v1_21.py`, applied to the accepted candidate `05b3315f…4258` with decision date "26 October 2026". Three lines change, each exactly once:

| Line | Candidate | Published |
|---|---|---|
| Document status | DRAFT — v1.21 stage-2 candidate, not adopted; v1.20.8 governs until PI adoption. Release record (DRAFT): … | ADOPTED — PI, 26 October 2026 (corrections of the reconciled v1.20.8 advisory and Methodology v1.4 compaction; stage 1 and stage 2 reviewed). Release record: … |
| Appendix A v1.21 heading | `### v1.21 — 26 October 2026 — DRAFT (stage-2 candidate; not adopted)` | `### v1.21 — 26 October 2026 — Adopted` |
| Footer | `*END OF DOCUMENT — RTG_NUMBER_GENESIS_DSN_v1.21 (DRAFT stage-2 candidate; not adopted).*` | `*END OF DOCUMENT — RTG_NUMBER_GENESIS_DSN_v1.21 (ADOPTED, 26 October 2026).*` |

The Date line already reads 26 October 2026 and is asserted, not changed. Nothing else changes: no live text, no other header field, no claim, grade, RID or OPEN status.

### 13.3 Checks (EV-RUN)

| Gate | Result |
|---|---|
| P1 input is the accepted candidate `05b3315f…4258` | PASS |
| P2 output equals the transform of the candidate | PASS |
| P3 exactly the declared lines differ (3: status, Appendix A heading, footer); Date line = decision date | PASS |
| P4 reverse transform recovers the candidate byte-exactly | PASS |
| P5 no DRAFT / candidate / not-adopted marker in the header fields, the Appendix A v1.21 heading or the footer | PASS |
| P6 every other line byte-identical; claim-tag census identical | PASS |
| Negative controls N1 (live-text change), N2 (footer not transformed), N3 (wrong decision date), N4 (one `[OPEN]` regraded), N5 (another header field edited) | all rejected |

Published: `dsn/RTG_NUMBER_GENESIS_DSN.md`, 274,246 bytes, SHA-256 **`4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701`**. The candidate hash `05b3315f…4258` identifies the reviewed candidate only.

## 14. Open items carried forward

- Census-1 INCONCLUSIVE / INCONCLUSIVE; C7C-M4 HOLD pending the TDR-G orientation-policy request; C7B global breadth, C7C-A, N-4, N-6, NG-7B and full NG-8 OPEN — unchanged.
- LOGSLIP relocation (NA-06) and the dated `[v1.20.x]` markers in untouched rows (§6): content work for a later edition.
- E42 hash form: the RECOG v0.3.24 hash is written `8c64bea2…69e7c1` (six-character suffix) instead of prefix…last four (`…e7c1`). Atlas note, non-blocking; next edition.
- Two non-blocking notes of the atlas owner on `tools/check_compaction.py` (PR #77): for the next tool edition.
- NC-17 (Dyadic q* question) deferred until Dyadic answers.
