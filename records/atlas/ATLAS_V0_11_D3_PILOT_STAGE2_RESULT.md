# Atlas v0.11 — D3 pilot, stage 2a: deletion-only compaction, measured yield, and the decision it leaves open

**Date:** 10 November 2026. **By:** Claude, Atlas owner. **Status:** [SESSION] pilot result for review. Not an Atlas edition; `atlas-v0.10` governs; the live `atlas/RTG_STATE_ATLAS.md` is unchanged.
**Frozen base:** stage-1 output, SHA-256 `0f8ba5c0e34dcbbaaa11858e2d568a9f5d5ced63aeca8ee69a44c973d7a1a6c2` (accepted as intermediate base, PR #204 review 5840025491).
**Tool:** `tools/atlas_preservation.py` rev. 3. **Files:** `evidence/atlas/v0.11_pilot/stage2a/`.

## 1. What was done

D3 (stage-1 lines 608–857, 97,852 bytes) was read in full. Stage 2a applies only removals that the adopted Method v0.2 already prescribes, and only by deleting declared byte spans: nothing is reworded, moved or added, so the text that remains is byte-identical to the base.

| Class | Rule | Spans | What is removed |
|---|---|---|---|
| K1 | Method §4.1: chronology of edits is not atlas content | 12 | owner-edition labels such as "; v0.3.24", "v0.3.25: ", "[COR v0.3.26] ", "in place of the earlier [assuming:]" |
| K2 | Method §4.7: at most a one-line method pointer | 9 | proof and certificate-run detail inside `method:`/`proof:` text of seven theorems; the method name, `cert` and `@owner§` stay |

All 21 spans are listed verbatim in `stage2a_deleted_spans.md`. The builder asserts the base hash, that each span occurs exactly once in its line, and that no edit falls outside D3.

## 2. Mechanical result

| Item | Result |
|---|---|
| Candidate | SHA-256 `ace0b408def88c78291e7f26eaa8e358ade87205b738a9dcf8f7952a9818a5d6`, 519,983 bytes (base 521,832) |
| Comparator | **MECHANICAL PASS**: 1,486 EXACT, 15 DECLARED_PENDING_REVIEW, 0 MAPPED_EXACT, 0 FAIL, 0 context reviews |
| Two builds | byte-identical (output and map) |
| `tools/atlas_check.py --manifest evidence/atlas/v0.10/source_manifest.json` | 0 FAIL; counts equal to the live v0.10 file (sources 72, coverage 132, links 499/5/11, artifacts 110/3) |

The 15 pending items are 12 record lines (14 fields; two whole-field deletions) and one raw line (L740). None is certified preserved by the tool.

## 3. Yield

**−1,849 bytes: 1.9 % of D3, 0.35 % of the file.**

## 4. Why the yield is small: where the bytes of D3 are

Census of the stage-1 text by the extractor (bytes):

| Part | Bytes | Share of D3 |
|---|---|---|
| L1 objects | 6,538 | 6.7 % |
| L2 claims | 75,460 | 77.1 % |
| — of which the Atlas's own check record `*ATLAS:checked-D3` | 3,343 | 3.4 % |
| L3 frontier | 4,205 | 4.3 % |
| L4 constraints | 5,840 | 6.0 % |
| L5 diagnostics | 5,320 | 5.4 % |

Inside the typed L2 records: statement text 24,748; untyped segments (mostly further statement text) 9,015; raw-form record lines 26,537; negatives 2,469; dependencies 2,258; scope 1,501; `cert` 1,364; consumers 1,044; locators 831; premises 565.

Reading: there is no layer of overhead to strip. Pointers, locators and certificates together are about 5.5 kB. The mass is statement content: exact constants, domains, rows, negative limits. D3 is already written in telegraphic form.

## 5. Finding

Under Method v0.2 as adopted ("no fact is dropped for size", §4.6), compaction cannot bring the Atlas towards the size aim. The aim (≈60–90k tokens) asks for a reduction by a factor of two to three; the rules that authorize removal reach about two per cent in the pilot domain. A wording pass over the remaining text was **not** attempted and is not measured: every reworded field is a pending item with semantic risk, and the text leaves little to shorten. I do not expect it to change the order of magnitude, but that expectation is unverified.

So v0.11 as a "compaction edition" has no route to its goal by compaction. What remains is a choice about the Method, which is the PI's:

| Option | What changes | Loss | Cost |
|---|---|---|---|
| A. Accept the size | Method v0.3 states that completeness governs and replaces the token aim by a structural aim (critical items first, one node per claim) | none | none; the file stays ≈520 kB and grows with the owners |
| B. Lossless split | one core file (identifier, grade, scope, short statement, edges, negatives, L3–L5) plus one detail annex per domain holding constants, rows and evidence text; a reader loads the core and the annex it needs | none overall; the core alone is no longer self-contained | new structure, comparator extended to several files, a full review of the split |
| C. Lossy core | constants and evidence detail are dropped in favour of `@owner§` pointers | the Atlas stops carrying exact values | smallest file; contradicts §4.6 and needs an explicit Method change |

Advice (Atlas owner; advisory only): A or B. C gives up what the Atlas is used for, namely checking a statement without opening the owner. B is the only route that reaches the size aim without loss, and it is a new design, not a compaction; it should be decided as such, not slipped in under v0.11.

Independently of the choice, the stage-2a deletions can be kept or dropped as a small cleanliness item; they do not matter for size.

## 6. A v0.10 defect found while reading (not a compaction item; not changed here)

Two places in D3 still carry a conditional tag that the owner removed in the edition the Atlas pins:

| Atlas v0.10 / stage-1 line | Text | Owner, `recog-v0.3.27` |
|---|---|---|
| L736, in `RECOG-THM-A1B-SLIP-SCHEDULE-U` | "RECOG-THM-A1C-SHARPENED-SCHEDULE [assuming: Dyadic (D5) row-A bridge proof constants]" | DSN line 764: `[import: … DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM]`, "the former (D5) qualifier is discharged, v0.3.27" |
| L740, in `RECOG-RESULT-A1C-RECORD-PHASE-READOUT` | "RECOG-ALG-A1C-JOINT-CONTRACTOR; [assuming: (D5)]" | DSN line 1056: `[import: …]`, discharged |

The Atlas itself says so two lines away (L738: "the (D5) [assuming:] removed"; L739: "discharged"). The stale tags make the Atlas more cautious than the owner, not less, so no claim is overstated; but they are a qualifier error against the pinned source. `RECOG-ALG-A1C-START-OFFSET` part (ii) was not checked here: UNVERIFIED. This is a correction, not a compaction: it needs its own reviewed delta (a stage-1-type change, or the next refresh), and the reviewer should confirm the reading against the owner text.

## 7. Requested

1. Review of the 15 pending items of stage 2a (`stage2a_deleted_spans.md`), by class: is an owner-edition label chronology in the sense of §4.1, and is the K2 text method detail in the sense of §4.7?
2. Review of the finding in §5 and of the defect in §6.
3. PI: the choice among A, B and C, or another route. Until then no further compaction work is done on other domains.

## 8. PI decision (10 November 2026, 14:02 +03:00, project conversation)

**Route A.** The PI's words, translated: "We continue with A. We do want it smaller and we make it as small as we can, but we do not break the structure in order to shrink it."

Consequences recorded by the owner (operational reading, not an extension of the decision):
- No split of the Atlas (B) and no lossy core (C). The L0–L5 / D1–D6 structure and the rule "no fact is dropped for size" stay.
- Size reduction continues only by removals the Method already prescribes (the K1 and K2 classes of this pilot, and one node per claim as in stage 1), domain by domain, under the same comparator contract. It starts on other domains only after the reviewer's verdict on the stage-2a classes.
- The token figure in Method §4.6 no longer describes a reachable state. Restating it as an aim subordinate to completeness and structure is a Method v0.3 delta, to be drafted and reviewed separately; nothing in the Method is changed by this record.

## 9. Stage 2a accepted (10 November 2026)

PR #204 review 5841129271 (new reviewer session, entered through the orientation note): ACCEPT SCOPED. K1 accepted; K2 accepted scoped (statements, scopes, negative limits, method names and source pointers kept; no proof is re-verified by this); the two whole `proof:`/`method:` field deletions accepted. The stale `(D5)` tags are confirmed as a source mismatch that must be corrected by a separate stage-1-type change, not inside a compaction. Producer evidence (two builds, `atlas_check`) was not rerun by the reviewer.

## 10. Stage 2b — source correction of the `(D5)` tags (not a compaction)

**Base:** the accepted stage-2a output `ace0b408…a5d6`. **Files:** `evidence/atlas/v0.11_pilot/stage2b/`.

A scan of the whole candidate for `(D5)` found three stale D3 sites, one more than §6 listed (L823, the A1c-decoder sub-item in D3.L3). L560 is NUMGEN's own "(D5)" label and L738 already says "removed"; neither is touched.

| Line | Record | Replaced | By | Owner, `recog-v0.3.27` |
|---|---|---|---|---|
| L736 | `RECOG-THM-A1B-SLIP-SCHEDULE-U` (text on SHARPENED-SCHEDULE) | `[assuming: Dyadic (D5) row-A bridge proof constants]` | `[import: DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM (dyad-v6.4.23) and RECOG-ALG-A1C-JET-REMAINDER-BOUNDS]` | DSN lines 43, 764 |
| L740 | `RECOG-RESULT-A1C-RECORD-PHASE-READOUT` (text on JOINT-CONTRACTOR) | `[assuming: (D5)]` | the same `[import: …]` | DSN line 1056 |
| L823 | `RECOG-OPEN-EVENT-RULE` (A1c-decoder) | "under the (D5) [assuming:]" | "with the row-A remainder constants of" the same three RIDs | DSN line 180 |

Owner basis for all three: Appendix A v0.3.27, "Source conditions changed (only these): the (D5) `[assuming:]` of six A1c sites replaced by imported owner theorem rows and RECOG-ALG-A1C-JET-REMAINDER-BOUNDS"; results and grades unchanged. `RECOG-ALG-A1C-START-OFFSET` (ii): owner line 1054 also says discharged, and the Atlas carries no `(D5)` tag on it, so there is nothing to correct there.

| Item | Result |
|---|---|
| Candidate | SHA-256 `66f0b2ebdad84a578a7159d727c2d51d3831ebea15f18c07d9b17744173c20da`, 520,271 bytes (+288) |
| Comparator | MECHANICAL PASS: 1,431 EXACT, 3 DECLARED_PENDING_REVIEW, 0 FAIL, 0 context reviews |
| Two builds | byte-identical |
| `atlas_check.py` (v0.10 manifest) | 0 FAIL, counts unchanged |

Old and new spans verbatim: `stage2b_changes.md`. **Requested:** review of the three pending items.

## 11. K1/K2 on the other domains: what a scan shows

Pattern scan of the stage-2b text (labelled `method:`/`proof:` fields; edition-label forms as in K1):

| Domain | Bytes | Labelled method/proof fields (bytes) | Edition-label pattern hits |
|---|---|---|---|
| D1 | 68,930 | 0 | 10 |
| D2 | 111,381 | 2 (261) | 10 |
| D3 (after 2a) | 96,291 | 5 (374, already reduced to pointers) | 6 |
| D4a | 96,073 | 1 (100) | 5 |
| D4b | 38,656 | 2 (202) | 4 |
| D5 | 50,587 | 0 | 17 |
| D6 | 36,786 | 0 | 1 |

The hits are an upper bound: many are import pins (`[DYAD v6.4.22]`), which are scope, not chronology, and stay. Outside D3 the labelled material is about 0.6 kB of method text and a few hundred bytes of labels, well under 0.5 % of the file. D3 was the richest domain for this because RECOG's recent editions were absorbed line by line. Method detail that is not labelled can only be found by reading each domain in full, as was done for D3.

**Advice (advisory only).** Under route A the remaining yield does not justify a separate campaign over 400 kB with a review per domain. Proposal: close the pilot as the content of v0.11 (stage 1 + 2a + 2b), and make K1/K2 a standing rule applied whenever a domain is opened for a refresh, with the same span-deletion form. If the PI prefers the full pass now, it is done domain by domain as in §1.
