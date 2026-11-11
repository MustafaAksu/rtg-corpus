# Arithmetic Resonance and Zeta (AZ) v0.7 — Release Record

**Status:** CANDIDATE — not adopted. Review and the PI's adoption decision are pending (§12, §13). Until an annotated tag `az-v0.7` exists, `az-v0.6` remains the governing edition.
**Date:** 10 November 2026; revised 11 November 2026 after the change-focused review (§1).
**Prepared by:** Claude, AZ co-owner session (branch `claude/az-v0.7`).
**Edition:** v0.7, corrections only, one stage, under DSN Methodology v1.2 as declared (PI decision of 10 Nov 2026; the Methodology v1.4 migration and any layout work are a separate edition).
**Predecessor:** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.6`, tag `az-v0.6`, SHA-256 `dec78a4721d2f34711218d9b79ba0ce6438523060098f770cad5dd3f5eb70b8a`. It has no release record (`BASELINE.md`: verification "PI").
**LIT dependencies:** none.

Fields marked *(to be filled)* depend on steps that have not happened yet. This record invents no hash, approval or review identifier; every hash below was computed on the branch files.

## 1. Authorization and reviews

| Step | Source | State |
|---|---|---|
| Reactivation | PI, 10 Nov 2026: AZ is reactivated; advisory row 1 first (`records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md` §4) | given |
| Triage | `records/az/AZ_REACTIVATION_TRIAGE.md` (PR #207, head `23e6d4d`): 34 rows, two inbox items, five Atlas findings; list (i) / list (ii) | merged by the PI, 11 Nov 2026, merge commit `f5e548e` |
| Co-owner review of the triage | ChatGPT co-owner session, PR #207 reviews `5848171706` (accept with minor corrections) and `5848352191` (accepted) | done |
| PI decisions on the six triage questions | PI, 10 Nov 2026, 22:52 +03:00, project conversation: "6 konuda da co-owner tavsiyelerini kabul ediyorum" (triage §7) | given: list (i) is the scope; Methodology v1.2 stays declared; corrected Thread A list with a pointer; SG-PROG by pointer; the §9 provenance claim is replaced; Claude drafts, ChatGPT reviews |
| Change-focused review of this edition | ChatGPT co-owner session, PR #208 review `5854287756` on `fcd1c3d` (candidate `c1cb4140…a39f`): accepted with two minor corrections. It reconstructed the 59 edits against the tagged v0.6 text and recomputed five hashes; gate and control outputs were inspected, not rerun. R1 (size figures of this record) and R2 (three TDR-G definitions cited under one RID) are applied in this revision. | done; readback of the changed lines *(to be filled)* |
| Adoption | PI | *(to be filled)* |
| Merge commit, tag `az-v0.7` | PI | *(to be filled)* |

## 2. Identities

| Object | Path | SHA-256 |
|---|---|---|
| Base (adopted v0.6) | `git show az-v0.6:dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` | `dec78a4721d2f34711218d9b79ba0ce6438523060098f770cad5dd3f5eb70b8a` |
| **Candidate v0.7** | `dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` | `2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94` |
| Builder and checker | `evidence/az/scripts/build_az_v0_7.py` | `753c273d2b50f8063e0d5a6c329af598ff80e7532d4870f9e6dc73ca510b0f50` |
| Edit log (59 edits, old and new text with hashes, triage rows) | `evidence/az/v0.7/edit_log.json` | `341dd6dd54ea4e5e84575a7a1290923d07f4a601c32684fae8bcef3d654b1357` |
| Check output (gates) | `evidence/az/v0.7/check_output.txt` | `13640f0b1fb0ec97bb7aa8267d25ce104aa0e140d6598b53af693b35164c7f00` |
| Check output (negative controls) | `evidence/az/v0.7/controls_output.txt` | `13e30f32bf4df37f5829e5aa06813d87a5c2a9a6b76ec61fa06741363ed166ff` |

**Reproduce.** `git show az-v0.6:dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md > base.md`; `python3 -I evidence/az/scripts/build_az_v0_7.py base.md OUT.md LOG.json` writes the candidate and the log; `python3 -I evidence/az/scripts/build_az_v0_7.py base.md dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md evidence/az/v0.7/edit_log.json --check` runs the gates (`--controls` for the negative controls).

Owner editions the candidate is synchronized with (read at the tag, hash equal to `BASELINE.md`; scope of reading in triage §1): `dyad-v6.4.23` `9f874ccc…25cb`; `tdrg-v2.12.14` `3be72923…2392`; `gen-v2.10` `63c3b020…3d62`; `programme-v1.4` `37d857d0…28c0`; `uvm-v0.7.1` `0a51644d…f53e`; `methodology-v1.4` `cdacab5f…f2df`.

## 3. Edits by triage row

All 59 edits address base lines by number and are asserted against the base text (a line prefix, or an exact-once substring inside the line); the log holds the old and new text of each. Kinds: 27 substring, 22 line, 3 block, 5 insertion, 2 deletion.

| Triage row | Decided disposition | Edits | What changed |
|---|---|---|---|
| 1 | first correction | E41, E57 | §6 "To OPEN M": the "legal ×2 … certified dimensional type error" sentence is replaced by the OPEN-M v0.7.1 verdict (R16 `UVM-RESULT-AUDIT1`: the 2× reading withdrawn, conditional on two bridges; 4× not directly admissible; no certified deficit factor; R15 `UVM-NUM-2F-RHO` a calibration-conditional diagnostic). Appendix B correction entry. |
| 2–6 | repin | E05, E07, E08, E10, E11, E13, E14, E15, E19, E24, E27, E28, E34, E36, E38, E39, E40, E43, E44, E45, E52 | Programme v1.1 → v1.4; Dyadic v6.4.8.1 → v6.4.23; TDR-G v2.12 → v2.12.14; Genesis v2.8.4 → v2.10; OPEN-M v0.6 → v0.7.1, in the header, §0.1, §1.2, §3, §4.1, §4.2, §5, §6, §7 and §8. The two "v0.6 carries Thread A / Thread B forward unchanged" sentences now say what v0.7 does. |
| 7 | header | E04 | *Supersedes* = v0.6 with tag and hash. |
| 8 | keep v1.2 declared | E03, E05 | Methodology line: v1.2 declared, v1.4 named as governing, migration separate. Nothing else of row 8 is done. |
| 9 | restate at owner scope | E16, E46 | Raw cubic theorem: raw one-step map, $p\ge3$, "not a statement about the raw $p$-step map", owner caveat on the historical proposition. |
| 10 | owner wording | E12, E19, E20, E48 | "iff $b\le4$" removed in §1.2 and §8; `DYAD-ALG-B5-ALLP-NONVANISHING` cited for the $b=5$ result; `DYAD-OPEN-B5-ALLP` named as the closed lifecycle identifier. |
| 11 | register as closed | E18, E25, E39, E51 | New `[import-ref]` `[THM]` row for `DYAD-THM-Q403-PHASELAW` (§4.1.1, §8); the "exact cubic cascade formula" bullet is removed from §4.1.2 and from the §6 frontier sentence. |
| 12 | sign | E26 | §4.1.2: $\approx-0.0096$ (modulus $0.0096$). |
| 13 | (a) corrected list with pointer | E24, E26, E39 | §4.1.2 and §6 point to Dyadic §2 OPEN 9 as the owner's current list; the near-cancellation item carries the owner's current form. The four owner items AZ never listed are not added. |
| 14 | repin | E22, E49 | `DYAD-ALG-Q3-CANCEL` → `DYAD-ALG-Q3-DEG2-CANCEL`; source pointer §6.11. |
| 15 | owner qualification | E22, E23 | The eigenframe linear-part lemma's statement and eight projector objects are marked as not recovered at the owner (Dyadic Appendix D); owner grades untouched. |
| 16 | sub-labels are not identifiers | E47, E48, E50 | §8: one `DYAD-OPEN-P-RESONANCE` row naming its sub-items, including the cardinality lemma; the separate "subgroup cardinality" row is merged into it. |
| 17 | section pointer | E20, E21 | DIRECT-WEIGHT and CROSS-IDENTITY: source §2 OPEN 9. |
| 18 | label | E17 | $\nu_5^{(5)}$: exact in $\mathbb{Q}(\zeta_5)$; the radical field is that of its real and imaginary parts. |
| 19–20 | repin | E29, E30, E53 | The three owner definitions of TDR-G §6.1, each under its own RID: `TDRG-DEF-ZN-STATE` (phase universe, state), `TDRG-DEF-PHYSICAL-STATE` (quotient by global phase), `TDRG-DEF-BAND` (defect band) — in §4.2 and as three §8 rows (review R2). `TDRG-ALG-LEM-REACH`, `TDRG-THM-REACHABILITY-K0`. |
| 21 | owner wording | E31, E53 | LEM-RETRIG: bound state of period dividing 2; least period 2 for $d\ne0$; fixed point at $d=0$. |
| 22 | owner wording | E32, E53 | LEM-SPECCONS: gcd multiset "in particular", a consequence only, with the owner's $N=24$ counterexample to the converse. |
| 23 | repin + convention | E33, E53 | BIND3 owner RIDs; `[conv: v18 path orientation]`; not rerun by the owner. |
| 24 | qualification | E35, E53 | N-scaling: full-range fit, window-dependent exponent ($N^{-0.730}$ on 480–1440), not a structural constant; crystallization `[HEUR]`; owner tags and convention. |
| 25 | current chain | E37, E53 | TDR-24D/F closed at the mechanism level; gate TDR-24A → 24B → 24C with the owner OPEN RIDs. |
| 26 | repin | E36, E53 | OPEN TDR-26, `TDRG-OPEN-LOCKING-FAIL`. |
| 27 | pointers | E13 | §3: SG-PROG-1/2/4 by pointer to Programme v1.4 §8, each with this study's application; no v1.1 wording quoted. |
| 28 | request met | E09, E42, E43 | §0.1, §6 and §7 record the registration in Programme v1.4 (§6.1, §6.5, §7.1, §7.2 IF20/IF21); the patch request and the proposed entry text are removed. |
| 29 | two owner entries | E40 | §6: OPEN 1C (`GEN-OPEN-CHIRAL-ADMISS`, closed `[THM]`) and the reduced-model $\mathcal{P}_4$ `[RESULT]` inside OPEN 1 (`GEN-OPEN-PHASE-DIST`) cited separately; routing through `GEN-OPEN-UVJET-ALPHAF` and OPEN M. |
| 31(i) | replace the provenance claim | E54 | §9: files not in the repository and not recreated; `EV-SRC-REPORTED`; `EV-NOT-RERUN`; provenance by pointer to a manifest that cannot be inspected from the repository; grades kept with that limit, which also applies where §4.3.1 and §5 call an artifact hashed or certified. |
| — (edition lines) | — | E01, E02, E06, E55, E56, E58, E59 | Title, date, status-summary sentence, §10 entry, Appendix A entry, footer. |

Rows 30, 33 and 34 need no edit. Row 32 is a release step (§9).

## 4. Checks

**Gates** (`check_output.txt`, `EV-RUN`): RESULT: PASS (7/7 gates).

- G1 BUILD — the candidate equals the build from the tagged v0.6 bytes.
- G2 LOG — the stored edit log equals the build's log.
- G3 PROTECTED — four AZ-owned regions are byte-identical to v0.6: §2 (base lines 119–148), the SG-AZ guards (159–196), §4.3 Thread C (297–401), the Appendix B entries registered through v0.6 (582–596).
- G4 STALE — no superseded pin, identifier or withdrawn sentence survives outside three dated history lines of v0.6 (§1.3 milestone AZ-0, the §10 and Appendix A entries for v0.3) and the v0.7 Appendix A / Appendix B entries that name what was replaced.
- G5 OWNED-IDS — no edit drops an AZ-owned identifier, except E43, which removes the proposed Programme entry text (mentions of `AZ-1`, `SG-AZ-3`, `SG-AZ-0.4`; no declaration).
- G6 TAGS — no edit drops a grade or status tag, except the three declared owner-tag changes of §7.
- G7 ROWS — every edit names its triage row.

**Negative controls** (`controls_output.txt`): every control is caught.

```
[CAUGHT] K1 withdrawn ×2 sentence restored: failing gates ['G1', 'G4']
[CAUGHT] K2 old Dyadic pin restored in one place: failing gates ['G1', 'G4']
[CAUGHT] K3 unlogged change inside Thread C: failing gates ['G1', 'G3']
[CAUGHT] K4 unlogged removal of an AZ grade tag (header): failing gates ['G1']
CONTROLS: PASS (all caught)
```

**Lint** (`tools/dsn_lint.py`, informational, no gate; rerun on the final bytes): 83,281 bytes, 600 lines; growth +9,648 bytes (+13.1 %) over v0.6.

**Pipes:** `tools/pipes_index.py --check` passes on the branch.

A passing check authorizes nothing. The gates test that the file is the logged transformation of v0.6 and that AZ-owned content is intact; they do not test that each new sentence matches its owner text. That was read by this session at the owner tags (triage §1) and is the subject of the change-focused review.

## 5. What the change touches (`EV-NOT-RERUN`)

No computation was run or rerun. Every imported statement keeps its owner's grade. No AZ-owned result is changed or regraded: PROP-AZ-CORE-EQUIV, the antipodal-band low-order obstruction, the Phase-2 `4|q` diagnostic with its static-geometry reclassification, the retraction block, Level A and the `[bridge-disqualified]` status are byte-identical (G3).

The Thread C evidence named in §9 is not in the repository (triage §1). PI, 10 Nov 2026: the files may exist locally and were not located that day. v0.7 states this and changes no grade because of it.

## 6. Live-file exceptions kept on purpose

- **Methodology v1.2 structure.** Version-scoped headings and notes ("§0.1 v0.6 Distributed-Ownership Map", "Major update (v0.6 at a glance)", "v0.6 note", "REVISED v0.6"), the stacked Appendix A and the `[COR]` overlay in §4.1.2 stay. Removing them is the v1.4 migration.
- **Dated history lines** that record what earlier editions did keep their old pins: §1.3 milestone AZ-0, and the §10 and Appendix A entries for v0.3.
- **Bare `[THM-ALG]`** stays under the declared v1.2 (triage row 34).
- **`TDRG-AZ-STATIC-ZN-4Q` and `PROP-AZ-CORE-EQUIV`** keep their names (triage row 33).
- **`[CAND/conditional]`** on the $p=6$ face-flux transfer (§4.1.1, §8) is AZ's v0.6 spelling of the owner's `[CAND]` `[scope: conditional]` (`DYAD-CAND-P0-DYADIC`); triage classed that row "none", so it is not touched.
- **The two-component description of the degree-2 $q=3$ cancellation** (reachability; cancellation) is carried from v0.6. The current Dyadic edition prints that result as a one-line entry with its RID; the longer description was not found there and is unverified against the owner's current text. Review `5854287756` checked the degree-2 mechanism independently for the declared $K_p$ family (`[SESSION]`, not owner-adopted): the one-step $\bar z^2$ coefficient is nonzero and its $s$-step sum vanishes for $s=p/3\ge2$. That check does not recover or authenticate the owner's eigenframe linear-part lemma, is not adopted by this edition, and changes no text.
- **"Thread B (§4)"** in the SG-PROG-1 entry is v0.6's own cross-reference and is kept.

## 7. Removals and tag changes

- **Removed text.** §7's proposed Programme entry and dependency-graph request (base lines 449–471; request met). The §4.1.2 bullet "Exact cubic cascade formula …" (closed at the owner). The §8 row "DYAD-OPEN-P-RESONANCE — subgroup cardinality" (merged into the sub-item row).
- **Withdrawn sentence.** §6 "the legal correction is ×2, not ×4 …" — recorded in Appendix B.
- **Owner tags of imported statements** (none is an AZ grade; all follow TDR-G v2.12.14): N-scaling "`[NUM strong / HEUR strong in source]`" → "`[NUM]` (fit) / `[HEUR]` (limit) in source"; "remains `[HEUR strong]`" → "`[HEUR]` extrapolation in the source"; §8 "crystallization `[HEUR strong]`" → "`[HEUR]`".
- **Identifier strings no longer printed as RIDs:** `DYAD-ALG-Q3-CANCEL`, `TDRG-ZN-STATE` (kept once as the consumer name that resolves to `TDRG-DEF-ZN-STATE`), `[RID: LEM-…]`, `BIND3-*`, `TDR-24 / N-SCALING`, `TDR-26-BIRTH-ANCHOR`, the `DYAD-OPEN-P-RESONANCE — …` sub-labels.

## 8. Pipe items (`pipes/`)

Inbox checkpoint: 11 Nov 2026 on `origin/main` (`f5e548e`). `pipes/AZ/` holds two items; both are notices that ask for nothing.

| Item | State on this branch | Disposition |
|---|---|---|
| `pipes/AZ/20261028-TDRG-v2-12-14-adopted.md` | dispositioned | `2026-11-10 · accept · records/az/AZ_v0_7_RELEASE_RECORD.md` — rows 19–22, 32, 33. Closed after the tag. |
| `pipes/AZ/20261103-DYAD-notices-n16-n21.md` | dispositioned | `2026-11-10 · accept · records/az/AZ_v0_7_RELEASE_RECORD.md` — rows 9, 12, 14, 16; the VANISH-B2 range was already right. Closed after the tag. |

"Accept" is the statement-accepted state. Adopted use is AZ §8 at the producer editions, and exists only once `az-v0.7` is tagged. No outbound item is filed before the tag.

## 9. Affected consumers and notices (after the tag)

One `kind: notice` item per consumer, filed by the AZ co-owner after `az-v0.7` exists. Filing is a queue event and does not show receipt.

| Consumer | Inbox | What changes for them |
|---|---|---|
| TDR-G | `pipes/TDRG/` | TDR-G §6.2 cites `AZ-ALG-ANTIPODAL-LOWORDER` at `az-v0.6`: the entry is unchanged at `az-v0.7`. AZ now cites the owner RIDs and the two corrected lemma statements. Reply to the TDR-G notice. |
| Dyadic | `pipes/DYAD/` | Reply to the notice carrying N17/N21: the four points are taken up; AZ's §8 pins `dyad-v6.4.23`. |
| Programme | `pipes/PROG/` | Inventory and §6.5 name AZ v0.6 and say its §8 pins Dyadic v6.4.8.1 and TDR-G v2.12; IF20 and IF21 carry those pins. All are superseded by v0.7. The request to register AZ is closed. The §9.2 owner pass is done in part: corrections only, no migration, no restructuring. |
| Atlas | `pipes/ATLAS/` | Findings AZ.A1, AZ.A2, AZ.A3 and AZ.A7 and advisory rows 1 and 3 are addressed by v0.7; AZ.A5 needs no action. The absence of the Thread C evidence is now stated in AZ §9. |
| DZT | `pipes/DZT/` | DZT names AZ v0.6 as a companion and SG-DZT-1 names the $4\mid q$ rule in its no-transfer guard. Thread C is unchanged; nothing changes for DZT beyond the edition number. |

## 10. Size

| File | Bytes | Lines |
|---|---|---|
| v0.6 (adopted) | 73,633 | 601 |
| v0.7 candidate | 83,281 | 600 |

Net change: +9,648 bytes (+13.1 %), measured on the candidate bytes of §2. The growth is the owner RIDs and qualifications in Thread A, Thread B and §8, the §9 availability statement and the Appendix A/B entries; §7 shrinks by 22 lines. (The first issue of this record printed 82,889 bytes, taken from a lint run that preceded the final build; the candidate reviewed at `fcd1c3d` was 82,896 bytes — review finding R1.)

## 11. Not done (by decision)

- No Methodology v1.4 migration, no compaction, no restructuring (triage list (ii); Programme v1.4 §6.7).
- No recovery of the Thread C evidence; no rerun; no new certificate.
- No rename of AZ-owned identifiers.
- No work on AZ's own frontier (AZ-2; the analytic completion of the `4|q` mechanism; transfer-zeta poles).
- The four Dyadic OPEN 9 items that AZ never listed are not added to §4.1.2.
- No merge and no tag by this session. `BASELINE.md` is not edited before adoption.

## 12. Steps, in order

| # | Step | Who | State |
|---|---|---|---|
| 1 | Change-focused review of this branch: every edit against its triage row and the owner text | ChatGPT co-owner | review `5854287756` done; R1 and R2 applied; readback of the changed lines *(to be filled)* |
| 2 | Adoption decision entered here (§13) | PI | *(to be filled)* |
| 3 | Adoption commit on this branch: status line of this record, §13, and the `BASELINE.md` AZ row (v0.7, the adopted hash, this record, tag `az-v0.7`) | AZ co-owner | *(to be filled)* |
| 4 | Merge commits (not squash): the triage PR #207 first, then this PR | PI | #207 merged (`f5e548e`); this PR *(to be filled)* |
| 5 | Annotated tag `az-v0.7` on the merge commit of this PR, with the adopted hash in the tag message | PI | *(to be filled)* |
| 6 | Notices of §9; close both `pipes/AZ/` items; lane update in the orientation note | AZ co-owner, after the tag | *(to be filled)* |
| 7 | Tag verification and Atlas refresh | atlas owner | *(to be filled)* |

## 13. Adoption decision

*(to be filled — PI.)* No publication transform is planned: the candidate carries no DRAFT marker, so the adopted object would be the candidate bytes of §2 as they stand after review.

## 14. Open items carried forward

- Thread C evidence: locate the `az_v5` package, registry and certificates; bring them in unchanged on an `upload/…` branch; hash-check against `AZ-ART-AZV5-REGISTRY`; place under `evidence/az/`.
- Methodology v1.4 migration of the file, with the owner map for the two nonstandard identifiers and the `[THM-ALG]` tag.
- Restructuring proposed by Programme v1.4 §6.7: reduce duplicated owner-science summaries and focus the study's owned diagnostic content (no merge with DZT).
- AZ-2: a dynamical, non-substrate observable; the analytic completion of the `4|q` mechanism; transfer-zeta poles (BOOTSTRAP 4 of the orientation note).
- The pinned editions of v0.6 (Dyadic v6.4.8.1, TDR-G v2.12, Genesis v2.8.4, Programme v1.1, OPEN-M v0.6) are not in the repository; whether v0.6 reproduced them faithfully stays unverified and is no longer load-bearing once v0.7 is adopted.
