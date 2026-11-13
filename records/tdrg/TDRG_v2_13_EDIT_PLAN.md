# TDR-G v2.13 — edit plan (scope and decisions before the candidate)

**[SESSION] NONCANONICAL. This is a plan, not an edition: it changes no DSN text, grade, pin or RID.**

- **Prepared by:** the TDR-G co-owner (Claude, session `claude01SKePJ`), 13 November 2026.
- **Mandate:** the PI started the v2.13 maintenance cycle on 13 Nov 2026 at 12:07 +03:00, in the project conversation ("onaylıyorum"). It answered this lane's proposal:
  - one candidate that changes no scientific content: the Methodology v1.4 migration plus the AZ v0.8 pin;
  - separate decision notes on XFER-O08-01 and on `largest_center` / TDR-19.
- **Co-owner agreement:** the ChatGPT co-owner's plan evaluation, relayed in the same conversation at 12:06, agrees and adds:
  - Stage 1 carries source pins, structural fit and scope corrections;
  - Stage 2 is compaction only, with a movement map and a content-equivalence check;
  - scientific results, RIDs, grades and OPEN states are preserved;
  - the TDR-6 relational question is not a closing condition.
- **Precedent:** this plan follows AZ v0.8 (`records/az/AZ_v0_8_EDIT_PLAN.md`): edit rows, then the PI's decisions, then the two stages.

**Governing sources:**
- TDR-G `tdrg-v2.12.15`: `dsn/RTG_DISCRETE_GENESIS_DSN.md`, SHA-256 `1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64`.
- Methodology `methodology-v1.4`: `cdacab5f…f2df`.
- AZ `az-v0.8`.
- `CONVENTIONS.md` and `tools/` on `main` `93f1986`.

## 1. What was read for this plan, and what was not

**Read:**
- Methodology v1.4: §§0–2, §3.2, §8, §13 and Appendix A v1.4.
- AZ v0.8 edit plan; the AZ v0.8 notice to TDRG.
- The usage text of `tools/check_compaction.py`.

**Read in the TDR-G DSN at `tdrg-v2.12.15`:**
- the header and Local Tag Aliases;
- §1; the §2 priority block, OPEN list and TDR-6;
- §7 pins and consumers; §9; Appendix B; §A.sim; the footer.

**Read by outline and line size only:** the remaining §2 bodies (TDR-24A/B/F, TDR-25, TDR-26, OPEN-POLICY-GEOMETRY, TDRG-RESPONSE-TENSOR), §6, §8 and Appendix C. They will be read in full before Stage 1 freezes.

**Run (informational, no gate):** `tools/dsn_lint.py` (§2 below).

## 2. Measured state at `tdrg-v2.12.15`

**Size and lint.** 196,268 bytes, 1,432 lines. The lint reports:
- header 4,121 characters, of which the *Status summary* is 2,874 (Methodology §1: 2–4 sentences);
- §1: 726 words (target 200–400; above 500 it needs a header exception or reduction);
- Appendix A: 41,084 characters in 36 entries, the largest entry 440 words;
- one footer line, but it lists the whole lineage of predecessors;
- history phrases in live sections: `superseded` 11, `historical` 8, `former` 4, `no longer` 1;
- 90 RIDs.

**Version-scoped markers in live sections.** There are 47, for example "*(v2.12.14 …)*", "(v2.12)" and "*(new in v2.12)*".

**Bytes by section:**

| Section | Bytes |
|---|---|
| §1 | 6,061 |
| §2 | 52,849 |
| §3 | 6,960 |
| §4 | 1,162 |
| §5 | 2,767 |
| §6 | 55,665 |
| §7 | 8,329 |
| §8 | 6,806 |
| §9 | 1,036 |
| Appendix A | 41,596 |
| Appendix B | 3,803 |
| Appendix C | 3,984 |

**Structure against Methodology §1.** The file already has the standard order: §§1–9, Appendices A and B, and a further scientific Appendix C (the TDR-T requirements ledger). It also has the `AI_CONTEXT_CORE_END` marker. No renumbering is needed.

**The departures from v1.4 are of four kinds:**
- the header is not in current-only form: the date narrative, a lineage note in *Supersedes*, a historical-pin sentence among the companions, a version-by-version status summary, and Methodology v1.2 declared;
- version overlays in live sections;
- research narrative and superseded-hypothesis text inside §2;
- a long Appendix A, with a live block inside it (§A.sim, below).

**Tag spellings.** All live truth tags are canonical v1.4 §8.1 spellings: `[NUM strong]`, `[HEUR strong]`, `[ALG candidate]` and `[ALG structure]` are canonical. The local aliases (`[INTERP]`, `[REVISED]`, `[REJ]`, `[REPLACED]`, `[ENG audit: PASS]`, the prose labels) are declared in the alias table. So no grade question arises from spelling. Stage 1's checker lists any non-canonical live tag it finds.

## 3. Edit rows

### S. Stage 1 — content-bearing corrections (reviewed change by change)

| # | Item | Proposed edit |
|---|---|---|
| S1 | AZ pin | §6.2 citation of `AZ-ALG-ANTIPODAL-LOWORDER`: `az-v0.7` → `az-v0.8`. The entry is byte-identical at `az-v0.6`, `az-v0.7` and `az-v0.8`, and the checker re-verifies this from the tags. The §7 AZ consumer row is restated from AZ's own v0.8 text: AZ cites the TDR-G state, LEM-REACH, LEM-RETRIG, LEM-SPECCONS, BIND3, N-scaling, TDR-26 and TDR-24 items in its §8 only, at `tdrg-v2.12.14`. `TDRG-AZ-STATIC-ZN-4Q` and `TDRG-AZ-EXPORT-BASELINE` are AZ identifiers, not TDRG RIDs. |
| S2 | Methodology | *DSN Methodology* becomes v1.4 (`methodology-v1.4`). The alias sentence "declared v1.2; the spellings are unchanged in v1.4" becomes the v1.4 statement. |
| S3 | Historical pins | v1.4 §1.1 rule 4: each claim-specific pin to Programme v1.1 or OFN v0.6/v0.7 (TDR-1, TDR-19, LEM-NOANNIHIL) is read in place. It is kept, labelled as the load-bearing source, when that edition is what the statement relies on. Otherwise it is repinned where the cited statement is byte-identical at the current edition. A pin whose cited text changed is reported, not repinned silently. |
| S4 | §2 owner-review tasks | The paragraph says the tasks were "recorded for TDR-G by Programme v1.2 §6, not carried by Programme v1.3". It is restated as TDR-G's own current open items with their present status (state/gauge conventions; antipodal path tie discharged). The provenance narrative leaves the live text in Stage 2. |
| S5 | §A.sim | The simulation-artifact table sits inside Appendix A but carries live records: the `[FAIL]` `[scope: implementation bug]` row that invalidates the v1–v2 results, and a `[RESULT]`. Under **D3** the table is placed verbatim in §8 as an "Engine lineage" block. Stage 2 can then remove the Appendix A copy as an exact duplicate. |
| S6 | §1 homes | Under **D1 (a)**: each §1 statement is matched to its full statement elsewhere (§6, the §2 record, or §3). A §1 statement without such a home is first placed at its owner location in Stage 1, verbatim with its qualifiers. Stage 2 then reduces §1 to readouts and pointers. |
| S7 | Readouts and consumer table | Every new navigation text is written in Stage 1 and reviewed against its owner record, because the compaction checker does not certify paraphrase (Methodology §13.6.2). This covers the 2–4-sentence status summary, the §1 readouts, and the §7 consumer rows stated as current use rather than queue history. |
| S8 | Superseded hypotheses in §2 | Each `[REVISED]` or "historical; superseded" passage (for example the v2.8 failed-relock hypothesis under TDR-26, and the $q_{\rm proj}\sim N^{1.371}$ artifact under TDR-24F) is matched to a scientific correction record. If Appendix B lacks a record that §7 requires, Stage 1 adds one entry with the original statement and reason. Stage 2 can then remove the live narrative. A current correction statement stays live ("$q_{\rm proj}\sim N^{1.06}$, the earlier value was a ratio-convention artifact"). |

### C. Stage 2 — compaction (`tools/check_compaction.py` against the Stage 1 intermediate)

| # | Item | Operation |
|---|---|---|
| C1 | Header | Current-only v1.4 header: exact date; *Supersedes* = `tdrg-v2.12.15` and its hash only; current companions; the S7 status summary. *Programme tier* is kept as additional metadata. |
| C2 | Version overlays | Remove the 47 markers such as "*(v2.12.14 …)*" and "*(new in v2.12)*" from live sections (history-removal edits, each mapped). Where an overlay carries a current qualifier, the qualifier stays in the claim and only the version label goes. |
| C3 | §2 history | Remove the superseded narratives of S8 and the struck-through closed items of the priority list. They are replaced by one-line references to the closed records, which remain where they are (see D2). |
| C4 | Local aliases | Remove the v2.12.14 history sentence under the alias table. |
| C5 | Appendix A | One compact entry each for v2.13, v2.12.15 and v2.12.14. One line per earlier edition (v1.1–v2.12.13), each giving the date, change classes, affected RIDs and the locator: the full text stays at the tagged editions and in the release records. Once S5 is in place, the §A.sim copy goes. Appendix B is not touched. |
| C6 | Footer | One line, current edition only. |

**Expected size after C1–C6:** about 150–160 KB, from 196 KB. Most of the reduction comes from Appendix A and the header. This is an estimate, not a target.

## 4. Decisions for the PI

- **D1 — §1 length.**
  - (a) Reduce §1 to 200–400 words of readouts with pointers, with S6 first.
  - (b) Keep §1 and declare a profile exception in the header.
  - **Recommended: (a).** §1 now restates numbers and mechanisms that §6 and §2 hold in full. Drifts corrected in v2.12.15 sat in restated places: the $P$ label in §2 and Appendix B, and the gate named in the §7 export row.
- **D2 — depth of the §2 work.**
  - (a) *History only, in v2.13.* §2 keeps its records, including the closed TDR-24D/F modules and the TDR-24A/B/25/26 result bodies; only the history leaves (S8, C2, C3).
  - (b) *OPEN-registry restructuring.* §2 keeps only OPEN records (question, residual obligations, closure criterion, sub-items with pointers); the result bodies, about 30 KB of numerical record, move to new §6 subsections. (b) is the shape Methodology §1 describes for §2. But `tools/check_compaction.py` verifies a move only within one section, so a cross-section move of that size is a restructuring under §13.3. It would need its own claim-by-claim movement map and checking.
  - **Recommended: (a) now, and (b) as a separately planned edition.** This keeps v2.13 a pure migration that the existing checker can verify.
- **D3 — §A.sim.**
  - (a) Move it verbatim to §8 (S5).
  - (b) Leave it in Appendix A, where Stage 2 compaction would have to keep it whole.
  - **Recommended: (a).** It records which engine versions produced valid results, which is current artifact information.

## 5. Procedure

**Stage 1** covers rows S1–S8 and the Stage 1 parts of D1 and D3.
- Build: an assertion-gated builder with exact-once edits and an edit log, as in v2.12.15.
- Checker: a base gate; a reverse gate; preservation of every RID, truth tag and `OPEN` record outside the declared edits; the pin checks from the tags; and negative controls.
- Records: the intermediate hash is recorded.
- Review: a change-focused review by the ChatGPT co-owner.

**Stage 2** covers rows C1–C6.
- Movement map against the intermediate, checked by `tools/check_compaction.py` with its negative controls.
- Size report by `tools/dsn_lint.py --prev`.

**Then:**
1. PR, the atlas owner's row check, and the PI's decision.
2. Release record, status-lines commit.
3. The PI merges and tags `tdrg-v2.13`.
4. Notices are filed as pipe items to OFN, AZ, PROG and NUMGEN and listed in the release record. `pipes/TDRG/` is read again before Stage 1 freezes.

**No result is recomputed.** No engine is run, and no evidence state changes.

## 6. Not in v2.13

The following get separate decision notes:
- XFER-O08-01 (custody of Finding A);
- `largest_center` / TDR-19.

The following are also outside v2.13:
- the TDR-6 relational question for $\mathcal I(X)$;
- the N4 log reading;
- the §2 restructuring, if D2 (a) is chosen;
- any change of grade, RID, OPEN state, scope guard or evidence state.

## 7. PI decision

*(to be recorded)*
