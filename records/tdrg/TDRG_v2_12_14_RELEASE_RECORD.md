# Discrete Genesis (TDR-G) v2.12.14 — Release Record

**Status:** DRAFT — candidate built and checked; awaiting the ChatGPT co-owner's change-focused review, the atlas owner's row check and the PI's adoption.
**Date:** 28 October 2026
**Prepared by:** Claude, TDR-G co-owner session `claude01SKePJ` (branch `claude/tdrg-v2-12-14-stage1`).
**Edition:** v2.12.14, corrections only, one stage, under DSN Methodology v1.2 as declared (PI decision of 27 Oct 2026; the Methodology v1.4 migration and any layout compaction are v2.13).
**Predecessor:** `RTG_DISCRETE_GENESIS_DSN_v2.12.13`, tag `tdrg-v2.12.13`, SHA-256 `aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f`.

Fields marked *(to be filled)* depend on steps that have not happened yet. This record invents no hash, approval or review identifier; every hash below was computed on the branch files by the fill step named in §2.

## 1. Authorization and reviews

| Step | Source | State |
|---|---|---|
| Advisories | `records/tdrg/ATLAS_ADVISORY_TDRG_v2_12_13.md` (pass 1), `…_INDEPENDENT_CHATGPT.md` (pass 2), `…_RECONCILIATION.md` (§3 merged list, §5 PI decisions) | merged (#82, #84) |
| Owner dispositions | `records/tdrg/TDRG_OWNER_DISPOSITION_ADVISORY_v2_12_13_claude01SKePJ_20261027.md` (PR #89), `…_chatgpt_20261027.md` (PR #88, with its post-peer addendum) | merged (`78c2fef`, `ed5f85b`) |
| Disposition reconciliation | `records/tdrg/TDRG_OWNER_DISPOSITION_RECONCILIATION_v2_12_13.md` (atlas owner; PR #91) | open PR; read at `c359e21` |
| PI fixation | "başla" on the fixed dispositions of the reconciliation §3 (relayed in the session, 27 Oct 2026, 23:46) | given |
| Change-focused review | ChatGPT co-owner session: `records/tdrg/TDRG_v2_12_14_CHATGPT_CHANGE_FOCUSED_REVIEW_20261028.md` (PR #94, commit `728f959`); acceptance criteria in PR #92 comment 6454252077 | **CONDITIONAL PASS** — two bounded changes, applied in round 2 (§3a) |
| Row check and rerun | atlas owner (`records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_12_14.md`) | *(to be filled)* |
| Adoption, merge commit, tag `tdrg-v2.12.14` | PI | *(to be filled)* |

## 2. Identities

| Object | Path | SHA-256 |
|---|---|---|
| Base (adopted v2.12.13) | `git show tdrg-v2.12.13:dsn/RTG_DISCRETE_GENESIS_DSN.md` | `aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f` |
| **Candidate v2.12.14** | `dsn/RTG_DISCRETE_GENESIS_DSN.md` | `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392` |
| Builder | `evidence/tdrg/scripts/build_tdrg_v2_12_14.py` | `71d990b3579adaa2cecaa4308064af0a5e5c8ff127636609c757c4f0921f286e` |
| Checker | `evidence/tdrg/scripts/check_tdrg_v2_12_14.py` | `d27b946bd1e0ed2a40edf26da2c83d35401dae7f7e887eb4cdd9f53c762af847` |
| Reference implementation of TDRG-DEF-ORIENT | `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` | `ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c` |
| Edit log (105 edits, old/new text and hashes) | `evidence/tdrg/v2.12.14/edit_log.json` | `c94ff966ffe1f707c0e25cba3df83d6daad38c16074ab1ee7348224541c2edcb` |
| Checker output (gates) | `evidence/tdrg/v2.12.14/check_output.txt` | `df8579ac057132a08d346c37d76909770f46f9afc72f2b7dc2392cc7157874d9` |
| Checker output (negative controls) | `evidence/tdrg/v2.12.14/controls_output.txt` | `61473bc3e07c4ed9f7632bd0354b17a4cb4ce43e714dd4fc7aade4c1e151910f` |
| Checker output (C8 with the branch refs deleted locally) | `evidence/tdrg/v2.12.14/check_output_no_branch_refs.txt` | `0346ada7fab3bff9c9c8545ebc8aa2c77aefa5d177e9d30b558ebc5f798d6470` |
| Checker output (`--exhaustive`) | `evidence/tdrg/v2.12.14/check_exhaustive_output.txt` | `cd612a5e131fbe13e65d93702e39a6d3a9f9390611d80dd15552483e96b24c0f` |
| Pinned engine (v18) used by the checker | `upload/tdrg-records/genesis_mode_b_mc_v18.py` | `9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e` |
| Disposition evidence | `evidence/tdrg/disposition/SHA256SUMS.txt` | `dc0661ea922cefad1cd66c6f5ab73528613831332be2f07849ff90fcc774d385` |
| Session-held scripts (TB-11) | branch `upload/tdrg-session-scripts`, commit `386e9d44f1f819d89b5b0e0ce4f6cb18c6e08c8b`, `upload/tdrg-session-scripts/SHA256SUMS.txt` | `00ce64d9b9fc8039e81eb5cc2489248f3b71f5e0de33740f85bb0cb3696ac6e3` |

**Reproduce.** `git show tdrg-v2.12.13:dsn/RTG_DISCRETE_GENESIS_DSN.md > base.md`; `python3 -I evidence/tdrg/scripts/build_tdrg_v2_12_14.py base.md OUT.md LOG.json` writes the candidate (`3be72923…2392`) and the log; `python3 -I evidence/tdrg/scripts/check_tdrg_v2_12_14.py base.md dsn/RTG_DISCRETE_GENESIS_DSN.md evidence/tdrg/v2.12.14/edit_log.json` runs the gates (add `--controls` for the negative controls, `--exhaustive` for the full three-node census). The checker reads tags and two commit objects, `386e9d44…` (session scripts) and `c359e21…` (PR #91), until their content is merged; no branch name is needed. No publication transform is planned: the candidate carries no DRAFT marker, so the adopted file can be the candidate byte for byte.

## 3. Edits by disposition

All 105 edits are exact-once (`str`, `line` or one `block`), logged with old and new text and their SHA-256 in the edit log; every new text occurs once in the candidate, so the log can be undone in reverse (gate C2).

| Row (reconciliation §3) | Fixed disposition | Edits | What changed |
|---|---|---|---|
| TA-01 / I01 | accept — option (b) | E53, E57, E97 | TDRG-DEF-ORIENT: tie on $S=0\wedge2E\equiv0$ for all $n$; TDRG-ALG-ORIENT-NOGO; the superseded node-ID completion named and scoped; the G-rule recorded as unadopted alternative; policy-table column; Appendix B row |
| TA-02 | accept | E53 | `[DEF]` TDRG-DEF-SIGNED-CENTERED ((−N/2, N/2], named as the source of the stratum), TDRG-DEF-SIGNED-DEFECT-ERROR |
| TA-03 / I11 | accept with change | E32, E91 | SG-14 ($\mathrm{Sym}(V)\times\mathbb{Z}_N^{\rm phase}$; token shift and mirror outside; `largest_center` exception); two separate OFN entries (§7 import; REQ-O09-05) |
| TA-08 / I02 | accept | E79, E84, E90 | mirror-inventory wording; v18-orientation scope on §6.12; orientation-covariance block with the antipodal fixture |
| TC-14 / I03 | accept | E90, E91 | DISC-2 witness effect (40 exposed; **20 of 136** under (b); 10 / 12 for comparison; ten labels unchanged; 96 unexposed unchanged); NUMGEN consumer row |
| TA-05 / I04 | accept | E10, E38, E65, E67 | LEM-RETRIG: period dividing 2, least period 2 for $d\neq0$, fixed point at $d=0$; no aliasing caveat (the band never reaches $N/2$) |
| TA-06 / I05 | accept | E81 | "therefore, in particular", with the $N=24$ counterexample; LEM-SPECCONS unaffected by the extended tie |
| TA-04 / I06 | accept | E06, E13, E14, E15, E20, E21, E33, E34, E72, E73 | headline `[NUM]` with full-range scope; window dependence citing the owner's own Exp-0 line ($N^{-0.730}$ on 480–1440, §2 OPEN-POLICY-GEOMETRY); the $\chi=0.836$ check withdrawn; crystallization `[HEUR]`; no refit |
| I07 | accept | E06, E17, E23, E36, E99, E100, E103 | TDR-24 D/F closed at mechanism level with analytic constants OPEN; A → B → C the gate; TDR-24B current-status line; Appendix C aligned |
| TA-07 | accept | E37, E98, E101, E102 | K₃ 96:1 and the T-6 wedge / $x_*$ marked historical continuous references (TRIAD v1.6.1, CN-05) |
| TB-09 / I08 | accept with change | E39–E47, E49–E52, E54–E56, E58, E61–E64, E80, E82, E85–E89, plus declarations inside E53, E69, E90, E92 | 39 RIDs in `TDRG-<CAT>-<DESC>` form (Methodology v1.4 §4.2); the consumer names `TDRG-ORIENT`, `TDRG-ZN-STATE`, `CONV-TICK`, `CONV-P3CYC`, `LEM-*` and the atlas names `TDRG-SWAP`, `TDRG-CYCLE`, `TDRG-MULTISTAR` are mapped as aliases in the §7 owner RID map (see §6, form note); no OPEN-module RID renamed |
| TB-11 / I08 | accept | E92 | §8 custody register: placed / replayed / held / missing with hashes; engine identity of the v17 corpus per file; the four certificate suites and the v6 per-run outputs missing; session-held scripts uploaded (TDRG-ART-SESSION-SCRIPTS) |
| TB-10 / I09 / I10 | accept with change | E04, E05, E91, E93 | governing editions named, historical pins kept; §7 imports / consumers / pins / RID map; v1.4 migration deferred to v2.13 |
| TB-12 | accept | E07, E09, E11, E12, E16, E18, E22, E24–E31, E35, E59, E60, E66, E70, E74–E78, E83, E94, E95 | compound tags unpacked; alias table replaced by the live non-canonical spellings with expansions; bare `[RESULT]` paired |
| TB-13 | accept with change | E01–E03, E08, E96, E104, E105 | title, date, supersedes, status-summary sentence, Appendix A entry, footer title and first supersedes item; footer chain and Appendix A order left for v2.13 |
| TC-16 | accept | E48, E91 | narrow-band exclusion cites `AZ-ALG-ANTIPODAL-LOWORDER`; `TDRG-ZN-STATE` resolves through the map |
| TC-17 | accept | E19 | the four Programme v1.2 owner-review tasks with their status |
| I12 | accept | E48 | AZ scope sentence: static $\mathbb{Z}_N$ graph statement, no bridge, TDR-19 OPEN, no confirmation of N-scaling |
| N1 (owner finding) | accept (both records) | E68, E69 | TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK; v18-orientation guard on §§6.6–6.10 |
| N2 (owner finding) | accept (both records) | E84, E90 | TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY |
| XFER-O08-01 / REQ-O09-05 | statement accepted; custody deferred; answered | E91 | §7 import of `RTG-OFN-ALG-STAR-TOKEN-SHIFT`; custody to v2.13 |

## 3a. Round 2 (review changes, 28 Oct 2026)

The round-1 candidate `b8317a75e5fb335075828f706f42f14708538fc15ff958b6acd4ef5402295a61` is superseded by the round-2 candidate in §2. Only the two requested changes were made, and no other edit text changed:

- **R1 — SG-14 scope (edit E32).** The first sentence now binds SG-14 to the canonical branch `bound_symmetric`; any other policy branch is covered only once its covariance is separately established. Equality is stated **modulo a relabelling of freshly born nodes** (one-to-one matching of newborn nodes, as the checks compare them). The branch-scope sentence says the finite checks support SG-14 on their tested scope and are not a theorem for all $N$ or all policies. `largest_center` is stated as not satisfying SG-14. A Violation clause is added for citing SG-14 on a branch whose covariance is not established. Gate C6 now asserts these three phrases.
- **R2 — checker C8 without branch dependence.** The session-held scripts are verified through the manifest `SHA256SUMS.txt`, whose own SHA-256 (`00ce64d9…`) is pinned in the checker. The manifest and members are read from the placed tree `upload/tdrg-session-scripts/` if present, else from the immutable upload commit `386e9d44…`. The pending-path fallback likewise uses commit SHAs (`c359e21` for PR #91, `386e9d44`), not branch names. New control K8 (altered manifest hash) must fail C8. A run with the remote-tracking refs `origin/upload/tdrg-session-scripts` and `origin/claude/tdrg-disposition-reconciliation` deleted locally passes C8 (`check_output_no_branch_refs.txt`).

## 4. Checks

**Gates** (`check_output.txt`, EV-RUN): RESULT: PASS (11/11 gates) — C0 BASE; C1 BUILD; C2 REVERSE; C3 HISTORY; C4 RIDS; C5 TAGS; C6 ORIENT; C7 NUMBERS; C8 EVIDENCE; C9 SOURCES; C10 DYNAMICS.

**Negative controls** (`controls_output.txt`): every control is caught, including K8 (round 2).

```
[CAUGHT] K1 old orientation text restored: failing gates ['C1 BUILD', 'C2 REVERSE', 'C4 RIDS', 'C6 ORIENT']
[CAUGHT] K2 one RID declaration dropped: failing gates ['C1 BUILD', 'C2 REVERSE', 'C4 RIDS']
[CAUGHT] K3 unlogged change: failing gates ['C1 BUILD', 'C2 REVERSE']
[CAUGHT] K4 wrong engine hash in §8: failing gates ['C8 EVIDENCE']
[CAUGHT] K5 compound tag reintroduced: failing gates ['C1 BUILD', 'C2 REVERSE', 'C5 TAGS']
[CAUGHT] K6 edited Appendix A history: failing gates ['C1 BUILD', 'C2 REVERSE', 'C3 HISTORY']
[CAUGHT] K7 v18 rule substituted for the reference rule: C10 FAIL
[CAUGHT] K8 session manifest hash altered: failing gates ['C8 EVIDENCE']
CONTROLS: PASS (all caught)
```

**Exhaustive** (`check_exhaustive_output.txt`): the dynamics gate with the full three-node $k=1$ census on the pinned engine.

```
  exhaustive k=1: v18 [72, 72] (expect [72, 72]); v2.12.14 [0, 0] (expect [0, 0])
RESULT: PASS (11/11 gates)
```

**Owner checks reused** (independent contributions, `evidence/tdrg/disposition/`, merged with PR #89): exhaustive equivariance at $k=1,3$ and the four-node sample; antipodal and $K_{2,3}$ fixtures; mirror probe; engine replays; the atlas check rerun byte-identically.

## 5. What the change touches (`EV-NOT-RERUN`)

PI decision Q3: no rerun inside v2.12.14. Results computed with the superseded completion carry `[conv: v18 path orientation]`: BIND3-CYCLE-N24K1 and its d-resolved anatomy, BIND3-PARITY / -SPECTRAL-GATE / -MEMORY-PARITY / -XFER / -REGEN, the NKSCAN suite, and every motif-log result of §§1, 2, 6.6–6.10 (the v17 and v18 engines share one `orient_path`). Bound: three-node census at $N=24$, $k=1$ — 77 of 9,800 eventual cycles, 16,322 of 331,776 states (4.9 %). The many-node exposure rate is not measured. Untouched: CONV-TICK, the swap, CONV-P3CYC, star blow-up, cycle bound states, the §6.2 theorems, LEM-REACH, LEM-NOANNIHIL, LEM-RETRIG and LEM-SPECCONS (ties act as identity).

## 6. Live-file exceptions kept on purpose

- **Appendix A order and the footer supersession chain** — layout (v2.13). Only the v2.12.14 entry is added on top, and the footer gains its title and first item.
- **Dated overlays in §2 TDR-24B** (v2.12.1–v2.12.9) — kept as the supporting record under the new current-status line; moving them is layout (v2.13).
- **Historical claim pins** — "Connection: OPEN-OFN-2 in `RTG_ONTOLOGICAL_FOUNDATIONS_v0.6`" at TDR-1 and TDR-19; "exported to `RTG_ONTOLOGICAL_FOUNDATIONS` v0.7" at LEM-NOANNIHIL; CONV-TICK's "imported by OFN v0.7". They record what each claim was stated against.
- **Engine not patched.** `genesis_mode_b_mc_v18.py` keeps the superseded completion; the amended rule exists as the reference implementation. A patched engine belongs to the sensitivity campaign.
- **§6.11 path-tie counters** (`pt_seen`, `pt_bound`, `pt_fail`) keep their engine meaning: in the v17/v18 logs they count $S=E=0$ ties only.
- **`[NUM exhaustive: …]` qualifiers** on the lemmas stay; the alias table now expands them.
- **§1 "No plateau through $N = 1080$"** and similar owner statements of the June scans are unchanged (no rerun, no new reading).
- **Form note (TB-09).** The reconciliation says the consumer names `TDRG-ORIENT` and `TDRG-ZN-STATE` are "adopted after collision checking". Methodology v1.4 §4.2 requires `PREFIX-CATEGORY-DESCRIPTION` and §4.2's last paragraph asks for an explicit owner map for nonstandard names. The edition therefore declares `TDRG-DEF-ORIENT` and `TDRG-DEF-ZN-STATE` and maps the consumer names to them in §7. Consumers resolve without repointing. If the reviewers prefer the bare names as the declared RIDs, this is a two-edit change.

## 7. Removals and name changes

- Local Tag Aliases: the rows `[ALG/NUM]`, `[ENG/ALG]`, `[NUM-strong]`, `[HEUR-strong]` and the sentence "Legacy aliases are accepted only during migration" are removed. New rows expand the non-canonical spellings still in live use.
- §6.12 "relabeling-covariance check: PASS" → "mirror-inventory check: PASS", with the qualification.
- §6.3 policy table column "Path double-tie" → "Path tie ($S=0$, $2E\equiv0$)".
- §1 "Exponent consistency: 1.593 ≈ 0.757 + 0.836; 0.869 ≈ 1.593 − 0.723" removed from §1. §6.8 keeps 0.869 ≈ 1.593 − 0.723 as a reading of the exact factorization and withdraws the 0.836 sum (`[COR]`).
- Grades: §1 N-scaling `[NUM strong]` → `[NUM]` with scope; TDR-22b/TDR-23 and §5 `[HEUR strong]` → `[NUM]` (fit) plus `[HEUR]` (limit); crystallization `[HEUR strong]` → `[HEUR]`; §6.8 fits `[HEUR strong]` → `[NUM]` with scope.

## 8. Pipe items (`pipes/`)

Inbox checkpoint: 28 Oct 2026 on `origin/main` (`ed5f85b`) and the open PRs. `pipes/TDRG/` holds two items.

| Item | Direction | State on this branch | Disposition |
|---|---|---|---|
| `pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md` (request; blocks NUMGEN C7C-M4) | inbound | dispositioned | `2026-10-28 · accept · records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md` — the ruling is TDRG-DEF-ORIENT option (b); witness effect §3 row TC-14. Closed after the tag. |
| `pipes/TDRG/20261026-NUMGEN-v1-21-adopted.md` (notice) | inbound | dispositioned (PR #89) | `no action`. Closed after the tag. |

No outbound item is filed before the tag.

## 9. Affected consumers and notices (after the tag)

One `kind: notice` item per consumer, filed by the TDR-G co-owner after `tdrg-v2.12.14` exists. Filing is a queue event and does not show receipt.

| Consumer | Inbox | What changes for them |
|---|---|---|
| NUMGEN | `pipes/NUMGEN/` | The ruling is TDRG-DEF-ORIENT option (b): tie on $S=0\wedge2E\equiv0$. Reference implementation `tdrg_orient_v2_12_14.py`. DISC-2 effect: **20 of 136** records; ten labels unchanged; 96 unexposed unchanged; DISC-1 is NUMGEN's to audit. RIDs replace "RID unavailable": TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE, TDRG-THM-RECURRENCE, TDRG-DEF-CONV-TICK, TDRG-DEF-SWAP, TDRG-DEF-CONV-P3CYC, TDRG-DEF-ORIENT. Re-annotation and the C7C-M4 release are NUMGEN's. |
| OFN | `pipes/OFN/` | Finding A (`RTG-OFN-ALG-STAR-TOKEN-SHIFT`): statement accepted; custody transfer XFER-O08-01 deferred to v2.13. REQ-O09-05 answered (TDRG-DEF-ORIENT and this entry). Owner RIDs for IMP-O08-02…16 per the §7 map. SG-14: the token shift is not a gauge. |
| AZ | `pipes/AZ/` | `TDRG-ZN-STATE` resolves to TDRG-DEF-ZN-STATE. `LEM-REACH`, `LEM-RETRIG` and `LEM-SPECCONS` map to TDRG-ALG-LEM-*. TDR-G §6.2 cites `AZ-ALG-ANTIPODAL-LOWORDER` with the I12 scope. Note that AZ declares a `TDRG-`-prefixed RID of its own (`TDRG-AZ-STATIC-ZN-4Q`); TDR-G leaves it to AZ and does not declare it. |

## 10. Size

| File | Bytes | Lines |
|---|---|---|
| v2.12.13 (adopted) | 148,073 | 1,288 |
| v2.12.14 candidate | 178,909 | 1,387 |

Net change: +30,836 bytes (+20.8 %). Corrections only: the orientation definitions and no-go remark, SG-14, the §6.12 orientation-covariance block, the §7 register and RID map, the §8 custody register and the Appendix A entry account for the growth; compaction is v2.13.

## 11. Not done (by instruction)

- No rerun of BIND3-CYCLE-N24K1, NKSCAN or the N-scaling scans (`EV-NOT-RERUN`, census bound).
- No engine patch; no new campaign.
- No layout compaction; no Methodology v1.4 migration (v2.13).
- No custody transfer of OFN Finding A (v2.13).
- No choice of the G-rule; it is recorded only.
- No merge and no tag by this session.

## 12. Steps after adoption, in order

| # | Step | Who | State |
|---|---|---|---|
| 1 | Change-focused review of this branch | ChatGPT co-owner | CONDITIONAL PASS (PR #94); round-2 changes applied (§3a) — confirmation *(to be filled)* |
| 2 | Row check, builder/checker rerun, `ATLAS_ROW_CHECK_TDRG_v2_12_14.md` | atlas owner | *(to be filled)* |
| 3 | Adoption decision entered here (§13) | PI | *(to be filled)* |
| 4 | Merge commits (not squash), in order: #87, #91, this PR; the `upload/tdrg-session-scripts` branch after its atlas hash check | PI | *(to be filled)* |
| 5 | Annotated tag `tdrg-v2.12.14` on the merge commit that carries the candidate hash, with the hash in the tag message | PI | *(to be filled)* |
| 6 | `BASELINE.md` TDRG row (entered on this branch: v2.12.14, candidate hash, tag `tdrg-v2.12.14`) | row: this session; tag: PI | row entered |
| 7 | Notices to NUMGEN, OFN and AZ (§9); close both `pipes/TDRG/` items | TDR-G co-owner, after the tag | *(to be filled)* |
| 8 | Tag verification; atlas refresh (D5 TDRG rows, D5.X1, H4, H9, the N1 row, the TC-17 fix) | atlas owner | *(to be filled)* |

## 13. Adoption decision

*(to be filled by the PI)*

## 14. Open items carried forward

- Sensitivity campaign: rerun BIND3-CYCLE-N24K1, NKSCAN and the N-scaling subset with TDRG-DEF-ORIENT. Compare it with the G-alternative on the same universes, and measure the many-node exposure rate. This needs a patched engine.
- NUMGEN: DISC-1 audit and DISC-2 re-annotation under TDRG-DEF-ORIENT; C7C-M4 release.
- v2.13: Methodology v1.4 migration and stage-2 compaction (Appendix A, footer, TDR-24B overlays); XFER-O08-01 custody; the policy-selection question for `largest_center`'s ID tie-break, with TDR-19.
- Custody: zip upload of the ten held motif logs; placement of `upload/tdrg-session-scripts` after the atlas hash check; the four certificate suites stay missing unless found.
- Owner-review tasks (3) counting observables and (4) statistical/rank interpretation stay open (§2).
