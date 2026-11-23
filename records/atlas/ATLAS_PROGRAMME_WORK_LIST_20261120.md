# Programme work list — what each stream still needs (Atlas advisory)

**Date:** 20 November 2026. **By:** Claude, Atlas owner. **Status:** [SESSION] advisory, NONCANONICAL. The Atlas owner advises and does not decide; nothing here is adopted, and no stream is told what to do.
**Asked by the PI** (project conversation, 20 Nov 2026, 10:30 +03:00): a general list of the work still to be done — the move to GitHub, adaptation to the new Methodology, record-keeping for operational continuity, working with LIT, and so on.
**Basis:** `main` `d422b89`, read on 20 Nov 2026:
- `BASELINE.md` and the newest tag of every study;
- the release records and entry notes in `records/`;
- the pipe states (`tools/pipes_index.py`: 142 items, check OK);
- the open PRs;
- `atlas-v0.14` and its manifest;
- the LIT rules in `CONVENTIONS.md` §8 and in `rtg-lit/CONVENTIONS.md` (adopted 11 Nov 2026).

Owner texts were not reread beyond their headers and the strings counted. Counts are mechanical and are to be confirmed by each owner.
**Builds on:** `records/atlas/ATLAS_ADVISORY_STREAM_ONBOARDING_20261116.md` (§6: DZT first; the rest deferred).
**B-stage review scope and authorship (21 November 2026):** §1 was prepared by the Atlas reviewer **ChatGPT** on PR #353 from the source-checked `main` `bf101d9` snapshot, under Atlas Method v0.3 and CONVENTIONS §9. The Atlas owner **Claude** independently checked it in PR #353 comment `7062936161` (**ACCEPT WITH CHANGES**); all five requested editorial/classification changes are incorporated here, pending the owner's final readback. The file's original "By: Claude, Atlas owner" line refers to the 20 November advisory (§§2–§4), not to the authorship of this §1 replacement. Sections §2–§4 retain their original 20 November advisory content and may mention then-pending decisions that have since been resolved. Nothing here is an owner scientific disposition, PI decision, release, tag or instruction to other streams.
**Correction of 23 November 2026 (Atlas owner):** rows A2, A6 and A7 of §2 were corrected, and the inventory under table A was added, after `rrf-v0.8.4` was read in full for the first time (`records/atlas/ATLAS_MAINTENANCE_LEDGER_20261123.md` §5). The 20 Nov inventory had been made from the header and from name counts. Each corrected row says what the 20 Nov text said where it was wrong; nothing is re-dated. The rest of §§2–4 is unchanged.
**Availability update of 23 November 2026 (Atlas owner):** a table was added under the inventory. It says, row by row, whether an object is now in `upload/corpus-originals-20261123/` and on what basis, from the intake check (`records/atlas/CORPUS_ORIGINALS_INTAKE_20261123.md`; `main` `bc5bd11`). The inventory itself is not changed and stays the record of the tree at `98a4a80`. Rows A2, A6 and A7 each get one dated paragraph. No class of §1 is changed.

## 1. Where each stream stands — verified B-stage checkpoint (21 November 2026)

**[SESSION] Source/reading extent.** GitHub `main` `bf101d9be34e5b7e23c5bfe80576ac7521066321`; governing tag refs and `BASELINE.md`; tagged-document headers and a targeted literal-grade-token scan of all eighteen Atlas inputs; `CONVENTIONS.md` §§2, 6, 7, 9; repository tree for the existence of owner release records and working entry notes; all 20 public `pipes/<KEY>/INDEX.md` files; and the open `rtg-corpus` PR list. Atlas `atlas-v0.15` and `main` share the same Atlas Git blob. The PI's server `pipes_index.py --check` reported PASS at 147 items, 20 inboxes; this check was **not rerun** by the reviewer. LIT's own `rtg-lit/CONVENTIONS.md` was read; its private scientific records and complete private queue were **not** audited or copied here. The working list's earlier 20 November findings remain historical observations in §§2–4; their owner-dependent conclusions have not all been independently re-reviewed.

**[SESSION] Classification is an advisory triage, not an owner verdict.** `CURRENT` = tagged identity/known release basis and working entry/queue show no identified *operational synchronization blocker* at this snapshot; it does not mean scientific completion, absence of OPENs or accepted consumer repins. `NEEDS_REVIEW` = owner confirmation of inbox, pin, grade or entry-currentness still needed. `BLOCKED` = required source/record or PI onboarding/status decision missing. `UNVERIFIED` = the necessary scope of source/queue verification was not completed. `INTENTIONAL_PIN` may be attached **only to an individual consumer pin after that stream's owner records the decision**, never inferred by Atlas from an older tag; no such label is assigned in this checkpoint. Multiple issues may coexist; the last column selects the immediate operational gate, not a rank or grade.

The **Authority** column distinguishes an owner release record visible at the named repo path (`OWNER`) from a `PI`-supplied baseline, cross-stream hash `XREF`, or explicitly non-adopted session source. Tag presence alone does not turn `ER2B` or `FMS` into adopted science. **Entry** reports the presence/currentness of the existing entry note, not whether a human session is presently online. **Compound** is a lexical count of backticked `[X/Y]`-shaped tokens at the tagged source (not a count of scientific grade defects); examples, retractions, provenance notation and historical text need owner classification. In particular RECOG has nine such occurrences under this documented lexical test, versus four in the earlier advisory's unspecified count: that is **not** evidence of an edition change or nine active errors.

| Stream | Tagged source | Authority | Method | Entry | Open in | Compound* | Atlas v0.15 input | B-stage class — next gate |
|---|---|---|---|---|---:|---:|---|---|
| Methodology | `methodology-v1.4` | OWNER | governance | none (draft in PR #189, deferred) | 0 | 2 examples | current | `CURRENT` — no identified release sync blocker; PR #189 deferred |
| Programme | `programme-v1.4` | OWNER | v1.4 | none | 9 | 0 | current | `NEEDS_REVIEW` — owner entry, receiver dispositions and dated inventory |
| DYAD | `dyad-v6.4.24` | OWNER | v1.4 | present; 20 Nov checkpoint | 3 | 2 aliases | current | `NEEDS_REVIEW` — AZ, LIT and DZT receiving items; owner decides; OPEN 20 remains separate |
| TDR-G | `tdrg-v2.13` | OWNER | v1.4 | present; predates v2.13 | 0 | 0 | current | `NEEDS_REVIEW` — entry resumption, crystallization grade (`[HEUR strong]` vs `[HEUR]`) and OFN XFER-O08-01 custody |
| AZ | `az-v0.10` | OWNER | v1.4 | present; v0.10 scope | 0 | 2 historical | current | `CURRENT` — separate fork work is not an adopted AZ edition or a pin discrepancy |
| DZT | `dzt-v0.19` | OWNER | v1.4 | present; v0.19 checkpoint | 0 | 0 | current | `CURRENT` — B1 PR #347 remains an unadopted research branch |
| TRIAD | `triad-v1.7` | OWNER | v1.4 | present; pre-v1.7 resumption text | 6 | 3 | current | `NEEDS_REVIEW` — receiver queue, older consumer pins, mixed-token scopes |
| GEN | `gen-v2.10` | OWNER | v1.4 | present; pre-v2.10 resumption text | 3 | 2 | current | `NEEDS_REVIEW` — includes LIT Regge request, producer notice and older pins; PR #160 open |
| RECOG | `recog-v0.3.27` | OWNER | v1.4 | present; pre-v0.3.27 resumption text | 1 | 9 lexical | current | `NEEDS_REVIEW` — DYAD notice, pinned uses and token provenance; nine ≠ nine defects |
| NUMGEN | `numgen-v1.21` | OWNER | v1.4 | present; pre-v1.21 resumption text | 11 | 17 | current | `NEEDS_REVIEW` — highest receiver backlog, dated imports and mixed evidence tags |
| OFN | `ofn-v0.12` | OWNER | v1.4 | present; pre-v0.12 resumption text | 9 | 0 | current | `NEEDS_REVIEW` — receiver queue, owner/consumer pins, TDR-G custody; PR #183 open |
| OPEN-M / UVM | `uvm-v0.7.1` | XREF; no owner record here | v1.3 | none | 4 | 10 | current | `BLOCKED` — PI/owner reactivation and release provenance before a recipient pass |
| RRF | `rrf-v0.8.4` | XREF; cited adoption record absent | v1.3 | none | 6 | 0 | current | `BLOCKED` — locate owner adoption/review records and PRR parent source; then activate owner |
| Pre-Legacy | `prelegacy-v0.8` | PI baseline | not declared (companion: `DSN_METHODOLOGY_v1.2`) | none | 1 | 0 | current | `BLOCKED` — PI activation/owner entry first; PI baseline source exists; then review older pins and SAT finding |
| Legacy | `legacy-v0.7` | PI baseline | v1.3 | none | 0 | 0 | current | `BLOCKED` — PI activation/owner entry first; PI baseline source exists; then historical scope and v1.4 migration decision |
| RER (noncanonical) | `rer-v0.2` | PI; scoped NONCANONICAL adoption | — | none | 2 | 0 | current | `BLOCKED` — PI decides frozen versus live working-registry continuation |
| ER-2B (noncanonical) | `er2b-v0.3` | PI baseline; owner text: WORKING / NOT OWNER-ADOPTED | — | none | 2 | 0 | current | `BLOCKED` — PI scope/status decision; source and model conditions retained |
| FMS (session) | `fms-v0.6.4` | PI baseline; owner text: SESSION / NOT OWNER-ADOPTED | — | none | 2 | 0 | current | `BLOCKED` — PI scope/status decision; no science promoted from tag |
| PRR Wrap-up (noncanonical) | v0.2 cited; bytes absent | missing source | — | none | no inbox | — | not an input | `BLOCKED` — locate v0.2/v0.3 bytes, establish hash/provenance and PI status |
| Atlas | `atlas-v0.15` | OWNER acceptance + tag verification | Atlas Method v0.3 | present; 21 Nov | 0 | 4 inherited D5 heads | derived (not an input) | `CURRENT` — the four heads remain explicitly nonblocking review debt |
| LIT (`rtg-lit`) | per-source records, not DSN tags | private independent workflow | own adopted CONVENTIONS | own repo (not counted here) | 3 public; private not audited | — | not an input | `UNVERIFIED` — public receiving queue is known; full private-source/queue state belongs to LIT co-owners |

**[SESSION] Queue cross-check:** 147 public items / 20 indexes = 80 `closed` + 5 `dispositioned` + 62 `open` (0 acknowledged). The largest currently open inboxes are NUMGEN 11, OFN 9, Programme 9, TRIAD 6 and RRF 6. Neither an inbox `closed` nor a document tag implies accepted imported use; see CONVENTIONS §7. No pipe was modified.

**[SESSION] Owner check:** Atlas owner independently inspected the §1 source and queue inventory, PR #353 comment `7062936161`, verdict **ACCEPT WITH CHANGES**. Five requested changes have been applied to this draft; final owner readback is pending. Classification total: **4 `CURRENT`, 8 `NEEDS_REVIEW`, 8 `BLOCKED`, 1 `UNVERIFIED`** (21 rows including Atlas/LIT/PRR). Individual scientific owners still must validate their own pins and dispositions; record `INTENTIONAL_PIN` only for a specific pin with a named owner decision. For unstaffed streams, begin with a fixed entry note and PI activation decision; for active streams, one batched receiver notice or review request per owner after inspecting its DSN. Do not repin, close an OPEN, revise a grade, elevate a SESSION result, or declare an adoption from this matrix.

## 2. The work, by kind

### A. Streams never brought into the working pattern

This means the move to GitHub, Methodology v1.4 and an entry note. Seven streams have not been opened since the baseline of 22 Oct. The AZ and DZT cycles show the shape of the work:
1. an entry note with staged first messages;
2. a reading report;
3. a triage with PI decisions;
4. a corrections edition with Methodology v1.4 as a second stage;
5. notices;
6. an Atlas refresh.

AZ took four editions and DZT two, both under a week.

| # | Stream | What is known to be needed | Suggested order |
|---|---|---|---|
| A1 | **OPEN-M (UVM)** | Methodology v1.3 → v1.4; 10 compound tokens; 11 Atlas diagnostics (OPENM.*), including the R12 attribution (advisory row 4); Genesis pin v2.8.5; 4 notices (GEN κ_f/B_*, DYAD N16–N21, GEN v2.10, TRIAD v1.7) | 1 — the most Atlas findings and live consumers |
| A2 | **RRF** | **As corrected on 23 Nov 2026.** It declares DSN Methodology v1.3 (header: `governing methodology`). Its pins are DYAD v6.4.18, RECOG v0.3.21, OFN v0.10, Genesis v2.8.9, NUMGEN v1.20.7, Triadic v1.6. The listed pins are older than the corresponding current owner editions and require a claim/scope impact check, statement by statement. A newer producer edition does not by itself invalidate a consumer pin or authorize repinning (§1, §5); whether a pin stays, moves or is declared intentional is the RRF owner's decision. The five RRF diagnostics of `atlas-v0.15` (RRF.F2, F3, F4, F5, F7) are each scoped to a named passage and are not changed by this row. 6 notices (RECOG, OFN ×2, DYAD, GEN, TRIAD). **What is verified and what is not:** the bytes of the v0.8.4 file are verified (annotated tag `rrf-v0.8.4`, BASELINE hash `2fb0a0fe…afce`, the same hash in RER). That verifies the text. It does not verify the adoption: the adoption is stated by the file's own header and by RER's cross-reference, and none of the adoption records the file names is in the repository. There is no `records/rrf/`. **Absent RRF records and predecessors** (inventory below, groups 1 and 2): six adoption records (v0.7, v0.8, v0.8.1, v0.8.2, v0.8.3, v0.8.4), a v0.8 QA manifest, and every edition before v0.8.4. **RER pointer:** RRF §§0.2, 6.4, 8.1 and 10.1 call RER v0.2 a communicated plan, not read and not mounted. That was the state on 14–20 Oct, when those paragraphs were written. RER v0.2 was adopted on 21 Oct and is at `rer-v0.2`; the RRF text has not been resynchronised since. Whether any RRF edition after v0.8.4 (20 Oct) exists is not known to the Atlas owner. First step: the PI locates the RRF working files; they arrive unchanged on an `upload/rrf-records` branch and are hash-checked against the hashes of the inventory. *20 Nov text, superseded where it differs:* "It declares no Methodology" (wrong: v1.3 is declared); "the adoption records of v0.7, v0.8.3 and v0.8.4" (three of six); "Its interface registry rows are stale as their streams have moved" and, in the order cell, "its rows go stale with every edition elsewhere" (stronger than the sources support: the age of a pin is not a defect; reworded on review `6022833998`); `RTG_RRF_OPEN19_G2_POSTADOPTION_SYNC_REVIEW_v0_2` listed as an RRF review (it is cited by DYAD, not by RRF v0.8.4; inventory group 4). **After the upload of 23 Nov 2026:** the first step happened in another form: the files came in `upload/corpus-originals-20261123/` (PR #367) and were checked (PR #369). In the folder are the six adoption-record files and every earlier edition; v0.6, v0.7, v0.8, v0.8.1, v0.8.2 and v0.8.3 agree with the hashes of this inventory (availability table below). That establishes byte identity. It does not establish what the five earlier records approve, which were not read, and no file named as an edition after v0.8.4 is in the folder, which does not show that none exists. The next step belongs to an RRF owner: placing the records under `records/rrf/` by its own PR. RRF has no active owner session; opening one is the PI's decision and stands after NUMGEN and OFN in the PI's order of 23 Nov | 2 — each later owner edition elsewhere adds to the impact check that its six pins need; this is a reason of workload, not a finding that any row is wrong |
| A3 | **Pre-Legacy** | Old pins (PROG.G6); the "0.5" convention trap (advisory row 5); one SAT finding (K₃ degeneracy and lift) | 3 — historical source; maintenance only |
| A4 | **Legacy** | Methodology v1.3 → v1.4; advisory row 5 together with Pre-Legacy; nothing open | 4 — with A3 or right after |
| A5 | **RER, ER-2B, FMS** | **The PI decides their status first:** onboard each as a live registry or study, or record it as frozen at its tag. In the second case its notices are answered "recorded, no further editions" and the Atlas marks it historical. 2 open items each | after the PI's decision (question 3 of the 16 Nov advisory, deferred) |
| A6 | **PRR Wrap-up** (`RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP`, noncanonical; added 20 Nov 2026 after the PI noted that a fourth noncanonical element never reached GitHub) | Never imported. It is the declared parent of RRF (`dsn/RTG_RRF_REPRESENTATION_REGISTRY.md` header: "parent: …WRAPUP_v0_2 §20, §26") and is cited by RECOG (§ source ledger: "PRR Wrap-up v0.2, noncanonical … interpretive only"). Its v0.3 synchronisation was delegated to its editor in Sep–Oct 2026 and is not known to have been produced. Steps: (1) the PI locates the bytes (v0.2, and v0.3 if it exists); (2) they arrive unchanged on an `upload/...` branch and are hash-checked; (3) `noncanonical/` gets the governing version under a fixed filename, with a release record and a BASELINE row; (4) the PI decides its status together with A5. No hash is known to the Atlas owner. **Added 23 Nov 2026:** RRF v0.8.4 leans on the Wrap-up in four more places than the parent line: §10.2 (the typed-covariance criterion for gauge status, RRF §4.2), §11 (the comparator discussion, RRF §4.1), §14.1 (the Genesis Identification & Inheritance Ledger, RRF §2.1 and §7) and §19 (the rationale of the representation safety lock, RRF §0). These are pointers to check when the bytes arrive; what the Wrap-up says there is not reconstructed here. **After the upload of 23 Nov 2026:** steps (1) and (2) are done for three files: v0.1, v0.2 and v0.3 are in the folder (availability table, row 6.1). They are identified by name only, since no source prints a hash for any version. A file named v0.3 therefore exists; whether it is the delegated synchronisation was not read here, and it is not thereby the version RRF and RECOG cite (they cite v0.2) or the governing one. Step (3) needs a recorded PI decision on source and status first. Step (4) is unchanged. The five pointers were not checked | with A5; the import (1)–(3) can come first, since RRF's five pointers into it cannot be checked until then |
| A7 | **Other cited, absent sources** | **As restructured on 23 Nov 2026:** see the inventory below, groups 3–6. Every file of the 20 Nov row is in it with the hash recorded then; none is removed. Added from the full reading of RRF: the G2 reviews, the RRF-side review and response records, ER-2B v0.2 and the Inheritance Ledger. **After the upload of 23 Nov 2026:** the search was run once for the whole corpus (440 names; intake record §2.3). For groups 3–6 see the availability table below. Not found: `PRR_RRF_REVIEW_v1` (3.4) and Legacy's `supplement_register.json` (6.4); no object is named `RTG_MASTER_DSN_v1.3` (6.5) | a targeted search together with A6; each found file goes through the same `upload/...` hash check against the recorded hash, where one exists |

#### Inventory for A2 and A7 — cited, absent sources by kind (23 November 2026)

Read from `rrf-v0.8.4` in full, and from RER v0.2 and `dyad-v6.4.24` at the lines that cite the same files. "Absent" means not in the `rtg-corpus` tree at `main` `98a4a80`. A missing file is not missing evidence in every case, so each row says which it is:
- **record** — a record of a decision or a review. Its absence leaves provenance unchecked; it changes no statement.
- **text** — a document that a statement points into. Its absence leaves that pointer unchecked.
- **evidence** — a derivation, certificate or verification record. Its absence means the result is source-reported, not inspectable here.
- **edition** — the bytes of an earlier edition. Its absence means a recorded hash cannot be compared with a file.

No hash below is new: each is copied from the source named. "none recorded" means no source in the repository prints one. **Checked on review (23 Nov, review `6022833998`):** rows 5.1 and 6.4 said "none recorded" although RER, ER-2B v0.3 and Legacy print a hash; both are corrected, and 6.4 is split into 6.4 and 6.5 (33 rows). The remaining "none recorded" cells were then swept by file name over the text files of the tree at `98a4a80`, outside `upload/`: each SHA-256 on a line naming the file, or within two lines of one, was read and belongs to another object. The sweep is lexical and is not a full reading of the sources; rows that give no file name (1.2–1.4, 2.1, 3.1, 3.5, 3.6, 6.3) cannot be swept this way.

| # | File, as cited | Cited in | Kind | SHA-256 known | Left unchecked while absent |
|---|---|---|---|---|---|
| **1** | **RRF adoption records** | | | | |
| 1.1 | `RTG_RRF_REPRESENTATION_REGISTRY_v0_7_ADOPTION_RECORD.md` | RRF header, §10, §10.1 | record | none recorded | scope of the v0.7 working-standard adoption; its "twelve finalization sites" |
| 1.2 | the "separate v0.8 adoption record" and its "QA manifest" (no file names given) | RRF §10.1 | record | none recorded | the source hashes that §10.1 says are recorded there |
| 1.3 | the "separate v0.8.1 adoption record" (no file name given) | RRF §0.2, §9 | record | none recorded | scope of the v0.8.1 release |
| 1.4 | the "separate v0.8.2 adoption record" (no file name given) | RRF §9, §10.2 | record | none recorded | reviewed-candidate and predecessor identities |
| 1.5 | `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_3_ADOPTION_RECORD.md` | RRF §0, §10.3; RER (as a project file, the source of its v0.8.2 and v0.8.3 hashes) | record | none recorded for the record itself | final bytes, candidate identities, the separate G2 v0.4 acceptance |
| 1.6 | `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_ADOPTION_RECORD.md` | RRF header (`adoption:`), §10.4 | record | none recorded | the adoption that the header states; the two review diffs |
| **2** | **RRF earlier editions** | | | | |
| 2.1 | v0.1–v0.5 | RRF §9 | edition | none recorded | — |
| 2.2 | `…_v0_6.md` | RRF §10 | edition | `7a31357729e1561c600673cf673c785b645666ae65d8280ebbaf9b57722d6b89` (RRF §10) | — |
| 2.3 | `…_v0_7_DRAFT.md` | RRF header, §10.1 | edition | none recorded | — |
| 2.4 | `…_v0_7.md` (adopted, 57,524 bytes) | RRF §9, §10.1; RER | edition | `2a2b4102ba12e53bc56c746ffe30c553d24ecffa90afddeb4027cd72307717a5` (RRF §9; RER) | — |
| 2.5 | `…_v0_8.md` | RRF §9; RER | edition | `c4ec1f10da0cdf3b95a84b3013909e04db49212e0119b858c170e5fd8f42b44a` (RER) | RER records that these bytes were not recovered in its archive search of 21 Oct |
| 2.6 | `…_v0_8_1.md` (80,889 bytes) | RRF §10.2 | edition | `1ba4713855a59b51cad8d79f88007380dfe2364f1b638478a927eea68f642c4c` (RRF §10.2) | — |
| 2.7 | `…_v0_8_2.md` | RRF §10.3; RER | edition | `f09dbb12f4b65b13c3f08ec049dcd701b04ca24c4b55876b565868f288555461` (RRF §10.3; RER, as reported by the v0.8.3 adoption record) | — |
| 2.8 | `…_v0_8_3.md` | RRF header, §10.4; RER | edition | `b393657e75e78ce46aea8920f4e5c25480e523caaa105589920a34ee55d4a187` (RRF header; RER) | — |
| 2.9 | the reviewed v0.8.4 candidate (107,629 bytes) | RRF §10.4 | edition | `fc53acff20c17e152884bc1835d4de2d4354a406f4d63262cdb04c200e2cab9e` (RRF §10.4) | — |
| **3** | **RRF-side reviews, notes and responses** | | | | |
| 3.1 | "G2 v0.3" (§4: the averaging chart) | RRF §2.4b, §9 | text and evidence | none recorded | the chart used by RRF's `[ALG]` existence equivalence (odd chart ⇔ square root) |
| 3.2 | `RTG_RRF_G2_PRIMITIVE_EXCHANGE_INTERFACE_REVIEW_v0_4_REVIEW_CANDIDATE.md` ("G2 v0.4 review") | RRF §2.4c, §10.3 | text | none recorded | the "full gate contract" that §2.4c leaves to it. RER names a `DYAD_RRF_OFN_G2_CONSOLIDATED_NOTE_v0_4.md` (`G2NOTE04`, no hash printed, bytes not held); whether that is the same document is not established here |
| 3.3 | `RTG_RRF_DEGREE10_REVIEW_INTEGRATION_v1` | RRF §2.4a | record (inspection only, no re-execution, by its own description) | none recorded | — |
| 3.4 | `PRR_RRF_REVIEW_v1` (also as `.zip`) | RRF §2.4a; DYAD §6.14 | evidence (the third-party report that VF-1 confirms) | none recorded | artifact-level identity, which RRF says was not re-done |
| 3.5 | the "separate editor response" to RER's Phase A G9 request (no file name given) | RRF §9 | record | none recorded | — |
| 3.6 | the "separate SESSION review" locating the first non-matching jet of S_h and R₀ (no file name given) | RRF §10.3 | evidence (RRF says it is not promoted to owner grade and not used) | none recorded | — |
| 3.7 | `RTG_RRF_RER_DYNAMICAL_CLOSURE_PROPOSAL_v0_1.md` | RRF §6.4, §9; RER | text (non-normative proposal) | `65186f393985ed502512c875601891cec999830abc2cc7db2fe01dd94f554e86` (RER, as recorded by the RRF editor) | the closure taxonomy that §6.4 moved there |
| 3.8 | `RTG_RRF_RESPONSE_TO_OFN_COINCIDENCE_v0_2.md` | RRF §6.2, §10.1; RER | text and evidence (noncanonical audit) | `897bfad065aa20c995b471c09cab564d4c1b6ac610769ae5b3f0fa1eb401126d` (RER, as reported by the RRF editor) | the coincidence calculation that §6.2 says it does not reproduce |
| 3.9 | `RTG_RRF_COINCIDENCE_ADMISSIBILITY_REVIEW_v0_1.md` | RRF §6.2, §10.1; RER | text and evidence (noncanonical audit) | `ef89db5c9aa6544c286cdc62b3841f4c7787ac90bf6512594865af122d472a53` (RER, as reported by the RRF editor) | as 3.8 |
| **4** | **Files owned by DYAD that RRF or the 20 Nov row named** (already on `records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`; listed here only so that they are not searched twice) | | | | |
| 4.1 | `DYAD_CHECK_degree10_even_term_hatF.md` (`DYAD-ART-NF6-DEG10`) | DYAD §6.14, §8; RRF §2.4a | evidence | `dcfd808c0270202768b4422acb474cda08f693a1cf69e8ec368e7faac414f4d4` (DYAD §8) | DYAD's degree-ten verification record |
| 4.2 | `RTG_RRF_OPEN19_G2_POSTADOPTION_SYNC_REVIEW_v0_2.md` (`DYAD-ART-OPEN19-SESSION`) | DYAD; not cited by RRF v0.8.4 | record (SESSION) | none recorded | — |
| **5** | **ER-2B and RER side** | | | | |
| 5.1 | `RTG_ER2B_CONSOLIDATED_STUDY_v0_2.md` | RRF §0.2, §6.2, §10.1; RER §7 (`ER02` row); ER-2B v0.3 (header `Supersedes`; §A.6) | edition (the repository holds ER-2B v0.3 at `er2b-v0.3`) | `ea26d3d1a4853ac88d1938dcb66c76eda4d55980ebf6f4d61091b97d67b2bb5e` (RER §7, `ER02`: byte-hashed by the RRF editor, `RRF_EDITOR_VERIFIED`, Q7; RER states that the bytes were not available to it, so this is RER's source report and not a receiving verification by RER. ER-2B v0.3 prints the same hash in its header and in §A.6, "re-hashed 19 Oct 2026, from the v0.2 package", together with the hash of that package, `RTG_ER2B_CONSOLIDATED_v0_2.zip`, `8c6352906143653a1736848e289da9765876927e3d2f089389c3a29326a048ee`; the package is not a separate row here) | whether RRF's C15A–C20 pointers still hold at v0.3 |
| 5.2 | `ER2B_COINCIDENCE_SIXSTEP_AUDIT_v0_1.zip` | RER | evidence | none recorded | — |
| **6** | **Ontology and historical side** | | | | |
| 6.1 | PRR Wrap-up v0.2 | RRF (five places), RECOG | text | none recorded | row A6 |
| 6.2 | Genesis Identification & Inheritance Ledger (RER: v0.19 DRAFT, `GIIL019`) | RRF §2.1, §7, §10 (as pending); RER | text | `f6320914…0be8` (RER prints this short form only; owner-reported; RER says the bytes are unavailable and an older v0.16 was accessible to it) | the "Genesis inheritance" fields RRF leaves open |
| 6.3 | the "Initial Ontological Premises and Questions" note (Oct 2026) | not cited in the repository | text | none recorded | — |
| 6.4 | `RTG_L0_L1_L2_BRIDGE_LEGACY_HISTORY_ARCHIVE_v0_7.md` | Legacy §10 (`ART-L07-HISTORY`), §13.1 | text (archival supplement: the v0.6–v0.1 history body, registered by Legacy as adopted with its parent v0.7 release and not as an independent current-state ledger) | `e46e17cc09a6b9b91bcf53251b252d8a7a5ccdbc65b9a630064f5eab633b3e47` (Legacy §10, repeated in §13.1; registered by the owner. Legacy says the same registration is in `supplement_register.json`, which is not in the tree either) | the registered hash cannot be compared with a file |
| 6.5 | `RTG_MASTER_DSN` (Legacy names `RTG_MASTER_DSN_v1.0.txt` as still unreceived, §3.1, and `RTG_MASTER_DSN_v1.3` as an integrated legacy source, §10) | Legacy | text | not found, and Legacy was not read in full for it: a string sweep on 23 Nov of the text files of the tree at `98a4a80`, outside `upload/`, found no SHA-256 on any line naming `RTG_MASTER_DSN`, or within two lines of one. This is not the "none recorded" of the other rows | — |

#### Availability after the upload of 23 November 2026

Source: the intake check of `upload/corpus-originals-20261123/` (529 files; 103 archives read, 8,484 members hashed), `records/atlas/CORPUS_ORIGINALS_INTAKE_20261123.md` §§2.4, 3 and 4, reviewed in PR #369. The rows below were re-queried against the same object index on `main` `bc5bd11`.

How to read it:
- **In the folder** means an object is there. It does not mean that an old approval is authenticated, that an edition is chosen as governing, that a dependency is accepted, or that an owner has received the file. The folder is an upload area; each owner places its own files by its own PR.
- **Basis** uses the intake record's terms. *Full digest*: an object has exactly the SHA-256 recorded in the inventory above. *Name only*: an object has the cited name and there is no recorded hash to compare. *Candidate*: the source gives no file name, and a file fits by its name; nobody has identified it. *Not found*: no such object in the 529 files or in the archives read; this says nothing about files elsewhere.
- The inventory above is not edited. Its "absent" statements stay true of `98a4a80` and are not current absence findings. RER's statements that it did not hold certain bytes stay true of RER's own dates.

| # | In the folder | Basis | Not settled by this |
|---|---|---|---|
| 1.1 | yes | name only. The digests the record prints resolve to objects in the folder (intake §2.4) | what the record approves: not read |
| 1.2 | the v0.8 adoption record: yes. The QA manifest: `RTG_RRF_v0_8_ADOPTION_QA.md`, `RTG_RRF_v0_8_CANDIDATE_REVIEW_MANIFEST.json`, `RTG_RRF_v0_8_ADOPTED_BASE_QA.md`, `RTG_RRF_v0_8_REVIEW_CANDIDATE_QA.md` | the record by name only; the manifest files are candidates | which file RRF §10.1 means; what the record approves |
| 1.3 | yes | name only | what the record approves |
| 1.4 | yes, only inside `RTG_RRF_v0_8_2_ADOPTED_G2_v0_3_RELEASE_PACKAGE.zip` | name only | what the record approves |
| 1.5 | yes | name only | what the record approves |
| 1.6 | yes | name; and one complete link: the record names the published file as 108,615 bytes with `2fb0a0fe…afce`, which is the tagged `dsn/RTG_RRF_REPRESENTATION_REGISTRY.md` at `rrf-v0.8.4` (record read in full; intake §2.4) | the two publication diffs the record names are not in the folder |
| 2.1 | v0.1 DRAFT, v0.2 DRAFT, v0.3, v0.4, v0.5 | name only | — |
| 2.2 | yes | full digest | — |
| 2.3 | yes | name; an object of this name has a digest printed in the v0.7 adoption record | — |
| 2.4 | yes | full digest | — |
| 2.5 | yes | full digest. This is the edition RER recorded as not recovered in its search of 21 Oct | — |
| 2.6 | yes | full digest | — |
| 2.7 | yes | full digest | — |
| 2.8 | yes | full digest | — |
| 2.9 | yes; its own name is `…_v0_8_4_REVISED_REVIEW_CANDIDATE.md`, and the folder stores it under another name (intake §4) | full digest | — |
| 3.1 | G2 v0.3 as a review candidate, and as a final file inside the v0.8.2 release package | both by digests printed in the v0.8.2 adoption record | which of the two RRF §2.4b means |
| 3.2 | the cited `…_v0_4_REVIEW_CANDIDATE.md`, and a `…_v0_4.md`; also `DYAD_RRF_OFN_G2_CONSOLIDATED_NOTE` v0.1–v0.4 | both G2 v0.4 files by digests printed in the v0.8.3 adoption record; the consolidated notes by name only | the review and the consolidated note are different documents (intake §3); RER's `G2NOTE04` has no recorded hash |
| 3.3 | yes | name only | — |
| 3.4 | **no** | not found (searched as `PRR_RRF_REVIEW_v1.zip`) | everything of this row |
| 3.5 | `RRF_EDITOR_RESPONSE_TO_RER_PHASEA_v0_2_20261019.md`, `RER_RRF_EDITOR_RESPONSE_RECEIVER_HANDOFF_20261019.md`, `RER_TO_RRF_EDITOR_W3_RF1_AND_G9_3_REQUEST_v0_1_20261020.md` | candidates | which file RRF §9 means |
| 3.6 | `RTG_RRF_SH_R0_FIRST_DIFFERENCE_SESSION_NOTE_v0_1.md` | candidate, by its title | whether it is the review RRF §10.3 means |
| 3.7 | yes | full digest | — |
| 3.8 | yes | full digest | — |
| 3.9 | yes | full digest | — |
| 4.1 | the bytes, under a browser-renamed file name (intake §4.1) | full digest | — |
| 4.2 | v0.1, v0.2, v0.3, v0.4 | name only | — |
| 5.1 | yes: the document, loose and inside the package; and the package `RTG_ER2B_CONSOLIDATED_v0_2.zip` | full digest for both (`ea26d3d1…bb5e`; `8c635290…48ee`) | whether RRF's C15A–C20 pointers still hold at v0.3: not checked |
| 5.2 | yes | name only | — |
| 6.1 | v0.1, v0.2, v0.3 (40,136 / 49,059 / 101,038 bytes; SHA-256 `7ff7d154…0a9d`, `88274f70…e2f2`, `68d45d37…a40c`, computed from the files) | name only | which version governs (row A6); RRF's five pointers |
| 6.2 | twelve drafts between v0.1 and v0.19 | name only. The v0.19 draft has `f6320914190b…e2f8`; RER prints `f6320914…0be8`. The first eight digits agree and the last four do not | unresolved; neither source is corrected here |
| 6.3 | `RTG_INITIAL_ONTOLOGICAL_PREMISES_v0_2.md` | candidate; the note is not cited in the repository | — |
| 6.4 | yes | full digest | `supplement_register.json`: not found |
| 6.5 | `RTG_MASTER_DSN_v1.0.txt` | name only | no object is named `RTG_MASTER_DSN_v1.3`; the search list named v1.0 only |

Counts over the 33 rows: 13 by full digest (2.2, 2.4–2.9, 3.7–3.9, 4.1, 5.1, 6.4); 3 by digests printed in an adoption record (2.3, 3.1, 3.2); 13 by name (1.1–1.6, 2.1, 3.3, 4.2, 5.2, 6.1, 6.2, 6.5), with no recorded hash to compare; 3 with candidates only (3.5, 3.6, 6.3); 1 not found (3.4). The counts are of rows, not of files.


### B. Streams in the pattern that the later changes have overtaken

These streams have notices waiting and pins one or more editions behind. The work is, at each stream's own checkpoint:
- an inbox pass that disposes of the notices;
- if pins or citations changed, a small synchronization edition;
- the stream's own open questions.

| # | Stream | What waits |
|---|---|---|
| B1 | **NUMGEN** (v1.21, 26 Oct; the oldest maintained edition) | 10 open notices: TDR-G v2.12.14, v2.12.15, v2.13; RECOG v0.3.26, v0.3.27; DYAD v6.4.23, v6.4.24; OFN v0.11, v0.12; PROG v1.4; DZT v0.18. Pins `dzt-v0.8`, `dyad-v6.4.22`, `gen-v2.9`, `ofn-v0.10`, `programme-v1.3`. **17 compound audit labels** (`[ENG/ALG audit]` and others) under a v1.4 declaration, to be unpacked or justified (Methodology §8.4) |
| B2 | **OFN** (v0.12, 30 Oct) | 9 open notices (DYAD ×2, GEN v2.10, TRIAD v1.7, PROG v1.4, RECOG v0.3.27, TDR-G v2.12.15 and v2.13, DZT v0.18); older pins; PR #183 (Binary Recognition wrap-up) open since early November; XFER-O08-01 custody, open with TDR-G |
| B3 | **TRIAD** (v1.7, 3 Nov) | 6 open items, among them the GEN 𝒫₄-identity and birth-symmetry answers and the DYAD bridge-note recovery; pins `gen-v2.9`, `dyad-v6.4.23`, `programme-v1.3`, `tdrg-v2.12.14`; 3 compound tokens |
| B4 | **GEN** (v2.10, 3 Nov) | 3 open items, among them the **LIT Regge interface inputs, open since 4 Nov**; PR #160 (inbox disposition) open since 3 Nov; older pins; 2 compound tokens |
| B5 | **RECOG** (v0.3.27, 4 Nov) | 1 notice (DYAD v6.4.24); 4 compound tokens; older pins |
| B6 | **Programme** (v1.4, 4 Nov) | 8 open items: the **SAT satellite-interface request (9 Nov)**; AZ v0.7–v0.10; TDR-G v2.12.15 and v2.13; DZT v0.18. Its §9.2 maintenance record and §6.4 gate sentence describe states that AZ, TDR-G and DZT have since passed (Atlas PROG.G6). A Programme maintenance edition (v1.5) would record the new state |
| B7 | **DYAD** (v6.4.24, 11 Nov) | 2 open items: the AZ v0.10 notice and the LIT reply on the scope of LH2012 Prop. 5.3. OPEN 20 has five open PRs (#296, #301, #305, #312; #287 parked) |
| B8 | **TDR-G** (v2.13) | Inbox clear. Open questions from its release record: the TDR-19 policy choice, XFER-O08-01 custody (with OFN), and the crystallization grade (`[HEUR]` against `[HEUR strong]`) |
| B9 | **AZ** (v0.10) | Inbox clear. Fork work in progress (PR #331); `AZ-OPEN-PROMO` and Level B conditions open |
| B10 | **DZT** (v0.18) | **v0.19 waits for the PI's adoption** (PR #334, readback `5988755813`, ACCEPT SCOPED). After it come B1 re-examination, channel universality and the targeted search for missing sources (DYAD `q4_03` certificate, `qb_extract.py`, v0.6, the v0.17 session record). The v0.18 notices are open at PROG, NUMGEN and OFN |

### C. Methodology and the shared rules

| # | Item | State |
|---|---|---|
| C1 | **Compound grade tokens under a v1.4 declaration** (NUMGEN 17, OPEN-M 10, RECOG 4, TRIAD 3, GEN 2, DYAD 2) | Each owner checks whether a token is in an allowed history or retraction block, or needs unpacking (§8.4). The Atlas carries METH.M1 for the pattern |
| C2 | **The PI's 19 Nov practice**: next to every equality, state the coordinate system and the categorical class it holds in, so that equalities from different conceptual systems are not mixed without normalization | Wanted in LIT as well. It is not yet a Methodology rule. Whether it becomes one (a Methodology amendment) is a PI decision |
| C3 | PR #189 — Methodology session-continuity proposal (DEFERRED) | CONVENTIONS §9 now carries the working-memory rule. The PI decides whether #189 is closed, folded into a later Methodology edition, or kept |
| C4 | Methodology §13.7/§13.8 (no stored diffs; size report) | Applied in the AZ, TDR-G and DZT cycles. The streams of A and B meet it at their next edition |

### D. Record-keeping for operational continuity

| # | Item | State |
|---|---|---|
| D1 | **Entry notes missing**: Methodology, Programme, OPEN-M, RRF, Pre-Legacy, Legacy, RER, ER-2B, FMS, PRR Wrap-up | Each is written when the stream is opened (A), or now for Programme, which has open items |
| D2 | **Entry notes not refreshed since 11 Nov**: GEN, NUMGEN, OFN, RECOG, TDR-G, TRIAD, and the two DYAD/GEN/RECOG inbox notes of 30 Oct–3 Nov | Each lane gets a checkpoint at the stream's next session (CONVENTIONS §9). TDR-G's lane predates v2.13's tag |
| D3 | `tools/orient.py` has no built-in profile for AZ and DZT. Their release records are not found without `--tag-prefix`, `--file` and `--record-glob` | Tool debt. A profile table for every study would make LIVE_STATE one command everywhere |
| D4 | Notices sent but not closed: DYAD 14, OFN 8, GEN 7, TDR-G 6, AZ 6, RECOG 5, PROG 4, TRIAD 3, DZT 3 | No action by the sender. Each closes when its receiver decides |
| D5 | The PRs listed above, open since early November (#160, #183, #189, #287) | A PI decision each: merge, close, or keep parked with a reason |

### E. LIT

| # | Item | State |
|---|---|---|
| E1 | GEN: the LIT Regge interface inputs (since 4 Nov) | waiting at GEN (B4) |
| E2 | DYAD: the LIT reply on the scope of LH2012 Prop. 5.3 (17 Nov) | waiting at DYAD |
| E3 | LIT inbox: DYAD's LH2012 use report (12 Nov) and the SAT use reports (HCG Abdulali, HHO Witt) | waiting at LIT |
| E4 | DZT: the LIT proof offer (acknowledged). It closes with v0.19. After the tag, the LIT notice asks LIT to correct two things: its record header ("not reviewed / not offered") and the phrase "right on the anomaly set" | after v0.19 |
| E5 | LIT is consolidating the literature it already holds (PI, 18 Nov). New searches are set aside | LIT's own work |
| E6 | The equality annotation of C2, in LIT's index | LIT's own work, when the PI confirms the form |
| E7 | Prior-art checks (CONVENTIONS §8) | No stream has asked for one for its new results: the DZT norm law, the TDR-G token laws, the AZ diagnostics. Asking is the stream's choice. The PI's rule is that RTG claims no novelty for what LIT finds in the literature |

### F. Atlas

| # | Item | State |
|---|---|---|
| F1 | DZT moved from v0.8 to v0.18; v0.19 is near | One refresh (v0.15) after v0.19, as was done for AZ v0.9. The PI has not yet answered whether to wait |
| F2 | Four Atlas-side compound heads in D5 | At the next D5 opening |
| F3 | Tool debts: the coverage check for non-Dyadic sources (now done by builder assertions); seven multi-line identifiers; a comparator mode for heading renames; F4 | Open |
| F4 | Every stream opened under A enters through an impact refresh after its first edition | Follows A |
| F5 | Size | Reported, not targeted. The PI looks at it again after the streams are reworked (10 Nov decision) |

## 3. Suggested sequence

1. **Now:** the PI decides DZT v0.19. Then the Atlas v0.15 refresh (DZT v0.8 → v0.19) and the DZT notices.
2. **OPEN-M**, on the AZ/DZT pattern. In parallel, if the PI wants: an inbox pass for **NUMGEN** and **OFN**, the two largest backlogs, and the oldest maintained editions.
3. **RRF**, then a **Programme** maintenance edition that records the state after A1–A2 and answers its 8 items.
4. **Pre-Legacy and Legacy** together (maintenance only).
5. **RER, ER-2B, FMS** according to the PI's status decision; the **PRR Wrap-up** import (A6) and the search for the other absent sources (A7) can start now, independent of that decision.
6. Throughout: GEN answers LIT (E1); the decisions on the old PRs (D5); the C2 rule if the PI wants it in Methodology.

## 4. Asked of the PI

1. Whether to start OPEN-M next. Whether inbox passes in NUMGEN and OFN run in parallel.
2. The status of RER, ER-2B, FMS and the PRR Wrap-up: onboard them, or record them as frozen. Where the PRR Wrap-up bytes (v0.2, any v0.3) are, and whether the ontological premises note belongs in the repository.
3. Whether the equality annotation (C2) becomes a Methodology rule, and in what form.
4. What happens to PRs #160, #183, #189 and #287.
5. Whether the Atlas waits for DZT v0.19 before refreshing (F1).

## 5. Since the snapshot (added 21 November 2026)

Sections §2–§4 retain the original 20 Nov advisory snapshot; §1 is the 21 Nov B-stage current-state **proposal**, independently checked by the Atlas owner with five corrections requested (PR #353 comment `7062936161`) and applied; final readback is pending. The dated historical changes below are provenance, not additional live status tables:
- **DZT v0.19** was adopted and tagged on 20 Nov (`dzt-v0.19`, file `2b959f46…f6ce`). Row B10's first clause, sequence step 1 and item E4's condition are met. DZT's B1 work continues in PR #347.
- **Atlas v0.15** was accepted and tagged on 21 Nov (`atlas-v0.15`, file `483e6003…02df`; DZT `dzt-v0.8` → `dzt-v0.19`). F1 is closed and question 5 of §4 no longer needs an answer. In §1 the DZT pin is current and the Atlas edition is v0.15.
- **A2, A6, A7** were added on 20–21 Nov after the PI noted that RRF's records and the PRR Wrap-up never reached GitHub.
- B-stage review of 21 Nov **proposes** the single updated §1 status matrix (4 `CURRENT`, 8 `NEEDS_REVIEW`, 8 `BLOCKED`, 1 `UNVERIFIED`), reviewed by the Atlas owner in PR #353 comment `7062936161` with five changes now applied; **owner readback pending**. `INTENTIONAL_PIN` remains owner-only per specific consumer pin, not a class that Atlas assigns by tag age. §§2–§4 and the original 20 Nov counts remain archival.

- **23 Nov 2026:** rows A2, A6 and A7 corrected and the A2/A7 inventory added, after `rrf-v0.8.4` was read in full at the PI's request. What the 20 Nov rows had wrong is stated in row A2. On review (`6022833998`, ChatGPT, Atlas reviewer) two further corrections were made in the same change: inventory rows 5.1 and 6.4 now carry the hashes that RER, ER-2B v0.3 and Legacy already print (6.4 split into 6.4 and 6.5), and row A2 no longer calls an old pin stale. The inventory describes the tree at `98a4a80`, before the upload of 23 Nov; what that upload makes available is recorded in `records/atlas/CORPUS_ORIGINALS_INTAKE_20261123.md` and is not folded into these rows. The Atlas, the RRF DSN, the pipes and every adopted result are unchanged; no RRF review is opened.
- **23 Nov 2026, availability update:** after the upload of that day (PR #367; intake record, PR #369) an availability table was added under the A2/A7 inventory, and rows A2, A6 and A7 each got one dated paragraph. Of the 33 inventory rows, 29 now have an object in the folder under the cited name or with the recorded hash, 3 have only an unidentified candidate, and one (`PRR_RRF_REVIEW_v1`) has none. In §1 the next gates of RRF ("locate owner adoption/review records and PRR parent source") and of the PRR Wrap-up ("locate v0.2/v0.3 bytes") are met as far as locating goes. Hash and provenance of the Wrap-up, its PI status, the placement of any file and the activation of an owner are not. Both rows stay `BLOCKED`; no class is changed here. The inventory and RER's dated statements are left as written.

Questions 1–4 of §4 are still open with the PI.
