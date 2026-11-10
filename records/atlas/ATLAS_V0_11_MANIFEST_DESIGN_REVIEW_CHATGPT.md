# Atlas v0.11 preservation manifest — ChatGPT design review

**Date:** 10 November 2026. **Status:** [SESSION], NONCANONICAL design/tooling review; no scientific adoption or release approval.
**Object:** PR #202, `claude/atlas-v0.11-manifest-design`, head `1075cc730cc065addcf29efd4e7fce8e933d252e` (design draft 0).
**Verdict:** **REVISE DESIGN CONTRACT — three bounded groups below.** The two-tier direction is accepted for continued development; it is not yet a preservation gate. Integrate these groups in the next extractor/comparator implementation pass, then perform one bounded D3 pilot review. The intentionally absent comparator and disclosed incomplete parsing are not themselves defects in a design draft.

## 1. Sources, reading extent and execution

Read the complete design §§1–6, complete 83-line extractor, complete `full_run_summary.json`, targeted entries across the eight-record `sample_manifest.json`, and Atlas v0.10 lines 736–740 as an original D3 sample. Governance: current CONVENTIONS (complete), current Atlas orientation (complete), Atlas Method v0.2 at `atlas-v0.10` (complete; especially §§3–7), and Methodology v1.4 §§13.5–13.7 at `methodology-v1.4` (targeted). This is not a full scientific rereading of the 18 owners or the 1,543-line Atlas.

Independently verified #113 merged at `447eb99750bd3ad807e78840e9259ac8c40f35d4` and #114 at `752bb6a4e136c9eccb5424b5c83ce421462f4e28`. That review is closed; this design review does not reopen it. A DSN checker acceptance is not certification of an Atlas comparator.

[EV-BYTES / EV-HASH / EV-RUN] The extractor was obtained through the GitHub connector, materialized locally, and matched to its Git blob before execution, without altering it:

- Path: `evidence/atlas/v0.11_design/atlas_manifest_draft.py`.
- SHA-256: `5809873f739e144e042b51330ce8511d2eaee7f581090cf3db4f078a27b3b9b2`.
- Git blob: `f98ceec30f6c46e6daa9dffc78d461f2f81344a3`; 5,785 bytes.
- Python 3.13.5. `check_draft0_contract.py` executes ten small design observations against the unchanged extractor, including a real CLI invocation for newline handling. All ten reported observations reproduced. **This is not ten passing preservation gates or ten failures of a comparator: no comparator exists yet.**

[EV-SRC-REPORTED / EV-NOT-RERUN] Whole-file counts (687 parsed node occurrences, 117 combined diagnostic occurrences, 488 UNPARSED lines, 545 UNVERIFIED fields, 15 duplicate identifier strings) are the preparer's report; the full Atlas extraction was not independently rerun. No owner scientific certificate was rerun. The reviewed schema contains no Atlas byte edit.

## 2. Accepted design choices

Keep raw-text binding, distinct typed/opaque coverage, the frozen source snapshot, per-field comparison rather than identifier-set equivalence, transparent UNVERIFIED coverage, size as an aim rather than a gate, and Method v0.3 as a separately reviewed delta. Keeping unsupported syntax unchanged is a valid option; no complete mathematical parser is required. Check logs may move out while the current result, scope and evidence limitation remain at the Atlas home.

## 3. Required contract changes — one implementation batch

### R1 — real byte identity and complete source accounting

**Locations:** design §2 and §4.1–2; extractor `fields`, `parse`, `main`.

**Executed facts.** `span` is documented as bytes but computed with Python Unicode string indices. For `TEST-ALG-X ALG | α=1 | sc: q>0 | ¬global`, all three field hashes match character slices and none matches the advertised UTF-8 byte slices. Separately, `open(..., encoding='utf-8').read()` normalizes CRLF: the reported source SHA-256 equals normalized LF text, not the input bytes. These are source-identity defects, not numerical issues.

**Required:** hash `read_bytes()`; define half-open UTF-8 byte ranges explicitly (or label character ranges and also provide a verified byte mapping). Assert `sha256(source_bytes[a:b]) == recorded_hash` for every source and destination span. Bind schema/extractor identity, document identity, occurrence, field position and raw content. Newline transformations, if desired, must be declared rather than hidden in reading.

Account for the complete document in a raw-span ledger, not just parsed content rows. Headings currently become a `section` string and have no independent span/hash. Header/source-table/L0/L4 material, inherited scope, index entries, syntax separators and blank lines need explicit semantic/context/structural classification; structural bytes may change under a declared layout rule. Do not let an ignored heading erase a guard or detach it from its descendants. Coverage is bidirectional: no unexplained source loss and no unexplained candidate insertion. This does not require every raw region to become a scientific node.

### R2 — DECLARED is not PRESERVED; signatures are alarms, not proofs

**Locations:** design §2 tier rule and §4.4–8.

The draft already requires review of every DECLARED edit (§4.8); keep that safeguard and remove any implication elsewhere that equal extracted features prove preservation. The unchanged extractor gives equal RID/pin/marker/number signatures for `q<1` versus `q>1`; numeral multisets also agree for `x=1,y=2` versus `x=2,y=1`. Raw hashes correctly differ. A declaration plus such equality must remain pending review, not become a mechanical PASS.

Use distinct outcomes, for example EXACT, MAPPED_EXACT, DECLARED_PENDING_REVIEW, REVIEWED_CHANGE, UNVERIFIED and FAIL. Parsing status and preservation status are separate: opaque text can be proved byte-preserved without being semantically typed. A reviewed change must cite the particular base/candidate spans and review disposition; it is not an automated proof of free paraphrase.

Tier B's phrase "found verbatim in the candidate" must require the correct mapped home and context, not global substring membership. Executed example: an untyped `only on q>0` segment retains its hash when moved from synthetic node X to unrelated Y, although X has lost its condition. Require an occurrence-specific source-to-destination map. Permitted many-to-one duplicate collapse must be explicit and keep all distinct qualified payload and consumer relations. Disallow unexplained field relocation, weakening, insertion or disappearance.

A grade/qualifier change or substantive diagnostic retirement is not made compaction-only by adding a disposition. Put an independently reviewed correction into a separately hashed stage-1 baseline, then compact against that baseline. Pure presentation/alias deduplication can remain compaction when its preservation map proves the unchanged content and reference roles.

### R3 — preserve occurrences, typed identities and edge associations

**Locations:** schema key definitions, extractor `fields`/`L5`/`HEAD`, criteria §4.3–4.

Keep `scientific_id` separate from an occurrence key such as document identity + source byte span. Two lines with one ID can contain distinct qualified payloads; equal ID sets do not account for both. The prototype retains both rows, which is good, but the proposed set-only acceptance criterion is insufficient.

The implementation uses `sorted(set(...))` for RIDs, pins and markers despite the design's multiset wording. An executed two-mention/one-mention pair produces the same list. Preserve occurrence counts/positions where required, and keep the full field hash authoritative.

A list of RID names and a separate list of pins loses their association. Swapping the two pins between `<DYAD-ALG-X [dyad-v1.0]; GEN-ALG-Y [gen-v2.0]` leaves both extracted lists unchanged. Preserve ordered raw edge fragments or explicit bound tuples containing source/target, edge type, role, actual consumer pin and qualifier context. Unresolved syntax may stay opaque and unchanged; it need not be guessed into tuples.

Distinguish claim RIDs, artifact RIDs, local/RID-less keys, index/cross-reference occurrences, stable L5 keys and HEADLINE display numbers. Atlas Method §4(11)/§5 expressly distinguishes these. The reported duplicate list includes `GEN-ART-*`; fifteen repeated strings are not automatically fifteen duplicated scientific claims. Preserve each origin and classify it before coalescing anything. A syntax flag `conditional:false` must mean only "no recognized explicit marker", not "unconditional": the current extractor returns false for a statement that says "If H holds, P follows." Keep raw grade/qualifier payloads such as `RES[from THM]` bound even where normalized typing is incomplete.

## 4. Answers to the four owner questions

| Question | Recommended decision |
|---|---|
| Normalize syntax first or keep large Tier B? | First improve the lossless observational extractor on unchanged v0.10. Recognize only unambiguous secondary segments; preserve unsupported ones opaquely. For D3, optionally add an assertion-gated resegmentation/rendering step with an exact origin map. Do not normalize all 18-source content merely to raise a coverage percentage. |
| Is the marker list sufficient; freeze `·s`, `·dx`, `nc`? | The list is a useful diagnostic aid, never sufficient semantic evidence. Preserve grade, `·c/·s/·dx/nc`, `from`, all premises, quantifiers, conventions/clocks, polarity and custody at their mapped homes. Forbid semantic qualifier changes in the pure compaction stage; authorized corrections are stage 1. No exhaustive lexicon is required when exact raw binding is retained. |
| Fix all fifteen duplicate identifiers? | Inventory/classify all fifteen reported cases once; resolve the pilot/touched cases and any ambiguity that blocks a mapping. Exact duplicate-to-pointer replacement is editorial when qualified payloads and edge roles are identical. Conflicting/different-scope cases need scoped review; untouched cases can remain explicitly deferred. Never overwrite one occurrence merely because its ID equals another. |
| Comparator in `tools/`? | Yes, a separate Atlas-aware tool, e.g. `tools/atlas_preservation.py`, after this draft matures. Keep independent receiving controls under Atlas evidence and reuse source/link checks from `atlas_check.py`; do not weaken or retrofit the DSN checker to claim Atlas semantics. Pin schema/extractor/comparator hashes in the report. |

## 5. Bounded acceptance for the next implementation and D3 pilot

Retain the draft's six proposed mutation controls. Add the demonstrated UTF-8/raw-newline binding cases and controls for wrong-home opaque text, duplicate-occurrence loss, relation/pin association swap, unchanged-number polarity/assignment changes, inherited-context loss and unaccounted candidate insertion. Positive cases must include exact retention, same-context movement, declared byte-preserving resegmentation and qualified duplicate-to-pointer mapping. Require no false preservation verdict; unsupported parsing can remain UNVERIFIED with mapped exact bytes.

Freeze base and candidate byte identities and source-manifest identity; compare raw coverage first and typed payloads second. Review only changed or ambiguous blocks; do not rerun owner certificates. Extractor extensions and the compare stage can be developed together now under these criteria; a separate paperwork-only iteration is not needed before coding.

The design's "about half" coverage is a denominator-specific observation: 314 fully typed nodes / 687 parsed node occurrences is about 45.7%, but 314 / 1,292 reported content lines is about 24.3%. Neither is semantic coverage of all facts. Report typed/opaque bytes and occurrence counts separately. The 117 count combines H/L5 parses; do not compare it directly with a count of stable L5 keys. The 25 conditional-node figure is syntax coverage only.

**Next eligible action:** owner incorporates R1–R3 in one design/implementation batch, extends representative examples (including an explicit conditional qualifier, an opaque field and a context-bound occurrence), and runs the bounded D3 pilot before whole-file compaction. Method v0.3 remains separate. PI priority 1 → 2 → 3 is unchanged; stage 1 tool debt is closed.

## 6. Reproduction and durable checkpoint

Evidence: `evidence/atlas/v0.11_design_receiving/check_draft0_contract.py` and `probe_results.json`. Obtain the extractor at the reviewed commit, then run:

```sh
python3 -I evidence/atlas/v0.11_design_receiving/check_draft0_contract.py \
  /path/to/unchanged/atlas_manifest_draft.py /tmp/pr202-draft0-probes.json
```

The harness pins the extractor SHA/blob and uses synthetic TEST IDs, not proposed owner science. It demonstrates design limits; it does not implement the compare stage or score whole-Atlas preservation.

Reviewer continuation: reviewed PR #202 draft 0 at `1075cc73`; keep the ten observations and the three correction groups together. Resume with the revised contract/extractor and comparator controls, not with #113/#114 or the completed orientation pilot. Own work branch: `chatgpt/atlas-v0.11-manifest-design-review`; its actual pushed head and review PR locate this checkpoint. Owner/shared orientation sections remain the owner's; this record does not overwrite another lane.

No Atlas/Method/owner bytes, producer draft files, source tags, pipe state or main branch were modified by this review. No full-corpus or scientific correctness assertion is made.
