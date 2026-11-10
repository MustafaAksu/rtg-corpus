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
