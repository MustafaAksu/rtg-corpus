# DSN_METHODOLOGY_v1.3

**Title:** Dense Semantic Notation — Methodology, Grammar, and Canonical Tag Registry  
**Date:** September 20, 2026  
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok  
**Revision editor:** ChatGPT; finalized from PI-approved Draft 1. The inherited author list is not a record of separate approval by the other contributors.  
**Document class:** Methodology / governance reference  
**Status:** ADOPTED — active canonical methodology for the RTG corpus update. Supersedes DSN_METHODOLOGY_v1.2 as the governing reference; existing study files retain their declared methodology version until individually migrated.  
**Revision base:** `DSN_METHODOLOGY_v1_2.md` (`DSN_METHODOLOGY_v1.2`), read in full.  
**Approved draft:** `DSN_METHODOLOGY_v1_3_DRAFT.md` — Draft 1, September 19, 2026.  
**Adoption:** Mustafa (PI) approved all proposed updates, including P1–P5, in this update branch on September 20, 2026.  
**Release record:** `DSN_METHODOLOGY_v1_3_RELEASE_RECORD.md`.  
**Supersedes:** `DSN_METHODOLOGY_v1.2`; the earlier file and approved draft are preserved unchanged as historical records.  
**Scope:** Rules for scientific records, evidence, ownership, imports, document profiles, and controlled corpus maintenance. This document contains no RTG physics result and does not decide any study's scientific OPEN.  
**Status summary:** This adopted revision preserves the DSN claim-block model, established tag spellings, and the standard technical-ledger section order. It separates proof status from assumptions, physical interpretation, evidence availability, and workflow completion; makes ownership and source-version handling explicit; and adds document profiles and a two-pass migration protocol. The PI has accepted all rule revisions and policy proposals P1–P5; the release record preserves that decision and the remaining nonblocking archive/tooling follow-ups. Adoption changes the methodology, not any scientific claim, study split, proof ownership, or programme maturity; corpus migration proceeds document by document.

---

<a id="dsn-section-0"></a>

## 0. Purpose and Design Philosophy

### 0.1 What DSN Is

Dense Semantic Notation is a structured Markdown format for scientific records in which every scientific claim-block carries its epistemic status, imported claims declare their source and inherited scope, and OPEN problems have explicit closure criteria. Current state, detailed evidence, and permanent history have distinct locations.

DSN serves as a working scientific record, an AI context pack, and a provenance log. A concise summary makes a study navigable; it does not replace the definitions, proof, or evidence needed to perform a calculation.

### 0.2 What DSN Is Not

DSN is not a free-form lab notebook or scratch-work file. Exploratory calculations and review findings remain in working records until their scope and status can be assigned. An audit finding is not automatically an adopted correction; a proposed exact formula is not automatically an `[ALG]` result.

Methodology governs records, not scientific truth. Administrative approval cannot repair a proof gap. A missing archive file does not by itself refute a theorem whose proof is otherwise available.

### 0.3 The Single-File Principle — One Canonical Home per Study

There is one adopted methodology and one designated canonical DSN per **study**, not one file per entire continuous or discrete branch. Each claim has one designated owner. Other studies import it rather than maintaining competing authoritative copies.

A study may have versioned technical appendices, certificate bundles, datasets, and historical snapshots. The canonical DSN must identify them and retain the claim statements, scope, current status, dependencies, and evidence locations. A supplement must not acquire an independent competing current-state ledger. Splits, mergers, and ownership transfers follow §13; this permission does not authorize a particular restructuring.

### 0.4 Design Priorities, in Order

1. **Epistemic honesty:** separate what was defined, proved, observed, inferred, or merely proposed.
2. **Current-state legibility:** locate the current position without reading a version history.
3. **Provenance preservation:** never silently erase a scientific correction, rejection, or source dependency.
4. **AI-context efficiency:** a bounded orientation core points to the complete record; it is not a self-contained substitute for every technical dependency.
5. **Human maintainability:** stable grammar and ownership allow focused updates without reinterpreting the entire corpus.

### 0.5 Document Profiles and Authority

Every document declares a profile. Claim grammar, evidence discipline, ownership, and import rules apply across all profiles; only layout and authority differ.

| Profile | Architecture | Authority and limits |
|---|---|---|
| Technical scientific ledger | Standard §0–§9 and Appendices A/B in §1 | Owns scoped definitions, derivations, experiments, and OPENs. |
| Foundational/technical bridge ledger | Standard layout by default; declared section map for a justified hybrid | Distinguishes mathematical construction, representation, physical realization, and ontology. The word “bridge” in its title is not a bridge theorem. |
| Foundational ontology / model-selection ledger | Declared section map | Owns commitments, model-selection questions, and interpretations; technical results are imported from their owners unless an explicit technical module is authorized. |
| Infrastructure / diagnostic ledger | Standard layout or declared section map | May own engineering results and mathematics of its own diagnostic objects. It does not acquire ownership of input physics. |
| Historical / legacy provenance ledger | Declared section map and archival scope | Preserves historical findings and revalidation gates. A new layout or filename does not promote historical evidence. |
| Programme overview | Programme-specific layout | Owns the study inventory, programme-level dependencies, maturity definitions, and programme guards; it does not substitute for source derivations. |
| Methodology / governance reference | This document's layout | Owns grammar and maintenance rules, not scientific results or programme maturity decisions. |
| Working note, review, or handoff memo | Explicitly noncanonical layout | Records proposals, checks, and requests. Adoption into an owner DSN is a separate recorded action. |

A nonstandard profile supplies a short map to current state, OPENs, guards, routing, technical content, imports, artifacts, and history. Missing functions are stated as not applicable with a reason. Profile selection must not be used to evade evidence or scope requirements.

### 0.6 Independent Status Axes

Record these separately: **claim status**, **model assumptions and conventions**, **physical interpretation**, **evidence availability/review**, **task closure**, and **document adoption**. Programme tier and maturity are assigned in Programme Overview, not inferred from a theorem tag or from the name of a branch.

A complete proof under an adopted model can be `[THM]` while the model's physical selection remains `[HYP]` or `[OPEN]`. A script can pass all of its tests while a larger scientific claim remains unproved. A scientific task can close while an identifier-assignment task remains open. No axis silently upgrades another.

### 0.7 Corpus Language

New canonical prose, change records, templates, and metadata are written in English. Mathematical notation and exact identifiers are preserved. A non-English historical quotation or identifier may be retained verbatim when necessary for provenance, with its source and an English explanation; it is not silently translated or renamed.

---

<a id="dsn-section-1"></a>

## 1. Canonical Document Architecture

The standard technical profile retains the following section order. Titles may be adapted; positions and functions are fixed. Other profiles follow §0.5 and declare their section map.

```text
§0   Header Block
§1   Current Canonical State              ← AI Context Core begins
§2   Active Frontier / OPEN Registry
§3   Scope Guards
§4   Layer Routing                        ← AI Context Core ends
§5   High-Risk Claims Ledger
§6   Main Scientific Ledger
§7   Import Ledger
§8   Artifact and Script Registry
§9   Collaboration and Provenance
     Appendix A — Version History
     Appendix B — Retired and Rejected Claims
     Optional further appendices / versioned technical supplements
```

### §0 — Header Block

Required fields, in this order; additional metadata follows them:

```md
# [STUDY_ID]_DSN_v[VERSION]

**Title:** [full title]
**Date:** [date of this revision; exact date preferred]
**Scope:** [one-sentence scientific scope]
**Document class:** [profile from Methodology §0.5]
**Document status:** [DRAFT | REVIEW-READY | ADOPTED | SUPERSEDED]
**Supersedes:** [immediately previous adopted version; or “none”; qualify a draft]
**Companion documents:** [directly relevant, versioned references; not proof imports]
**DSN Methodology:** [adopted version; explicitly identify use of a draft]
**Status summary:** [2–4 sentences: settled, active, blocked; at their stated grades]
```

The summary is present-state information, not a chain of version addenda. Authorship, revision editor, owner, programme pointer, and archive locator may follow. Do not invent an approval, date, archive DOI, or source version. Ancillary notes are not additional competing summaries.

### §1 — Current Canonical State

A compact, tagged account of accepted definitions and results, with their limitations and references to the detailed ledger. This is the navigation entry point; exact claim statements, evidence, and owner records govern technical use.

Target: 200–400 words. Above 500 words, move derivations, campaign tables, and history to their proper locations or record a justified profile exception. An inconsistency between the summary and detailed record must be reported and resolved, not settled by whichever location sounds stronger.

### §2 — Active Frontier / OPEN Registry

Unresolved tasks use Methodology §5. Closed modules have one-line references here; their proofs and closure records belong in §6 and Appendix A. A partial module may list completed sub-items without duplicating their proofs. Proposed experiments and requested artifacts must be distinguishable from executed ones.

### §3 — Scope Guards

Numbered, stable boundaries, with the consequence of violation:

```md
**[SG-N]** [Prohibition and applicable domain.]
Violation: [what the prohibited inference would get wrong or fail to establish]
```

A guard forbidding an inference does not prove that its proposed conclusion is false. Guard IDs are not reassigned to unrelated prohibitions; changed scope is recorded as a correction.

### §4 — Layer Routing

Map layers to typed objects, owners, and allowed transformations. Relevant entries name the model, state space, coordinate/gauge convention, tensor type, observable, and required identification or bridge. Mathematical reuse and physical identification are separate uses. A shared symbol, norm name, graph motif, or numerical value is not an identification.

End the actual section with exactly one machine marker outside a code fence:

```md
<!-- AI_CONTEXT_CORE_END -->
```

### §5 — High-Risk Claims Ledger

```md
| Claim | Valid form and scope | Forbidden overclaim | Owner RID / section |
|---|---|---|---|
```

This is a scope index, not a second proof ledger. It may flag a pending audit, but must not label a disputed statement established merely because it appears in the table.

### §6 — Main Scientific Ledger

Definitions, complete result statements, derivations, numerical protocols, and closure records. Each result states its assumptions and evidence location. Subsection headings have persistent anchors; mixed sections use §3.5. Large proof details may be linked to a versioned technical appendix without removing the operative statement and scope from this section.

### §7 — Import Ledger

One entry per load-bearing imported claim, using §4.3. A companion-document list or a reference-only bibliography is not a substitute. Include bridge requirements, source verification state, and pending synchronization actions where relevant.

### §8 — Artifact and Script Registry

One entry per artifact, using §§10.2 and 12. State whether it is planned, available, inspected, executed, or unavailable. Filename registration alone does not certify implementation or output.

### §9 — Collaboration and Provenance

Contributors and actual roles, revision authorship, adoption record, canonical archive locator if one exists, and custody of contributed proofs or computations. “PI-approved,” “independent rederivation,” and “rerun” require a corresponding record. Authorship inherited from an earlier version is not approval of a new one.

### Appendix A — Version History

```md
### vX.Y — [date and document status]
- **§X.Y [change class]:** [specific change and reason; affected RID(s) where applicable]
```

Recent versions retain detailed entries. Older entries may be summarized only if the full record remains recoverable in an immutable version or linked history. Compression never removes a correction's original statement or provenance. Version numbers in filenames and headers remain; the prohibition on top-of-file history concerns the narrative, not necessary metadata.

### Appendix B — Retired and Rejected Claims

Permanent records of corrected, rejected, withdrawn, and superseded statements:

```md
`[SUPERSEDED]` [RID: ORIGINAL-ID] Original: [statement or exact versioned locator].
Reason: [reason]. Replacement: [RID/location or none]. Recorded in: vX.Y.

`[RETRACTED]` [RID: ORIGINAL-ID] Original: [statement or exact versioned locator].
Reason: [reason]. Replacement: [RID/location or none]. Recorded in: vX.Y.

`[FAIL]` [RID: ORIGINAL-ID] [Precisely scoped claim or route rejected.]
Basis: [counterexample, contradiction, or limited route-failure evidence].
Replacement: [RID/location or none]. Recorded in: vX.Y.
```

An original statement's identifier is a historical reference here, not a second active claim. A correction to an unnumbered rule uses an administrative correction key and exact old section, not a fabricated historical RID. Erroneous rejection records are corrected under §7, never erased.

---

<a id="dsn-section-2"></a>

## 2. Inline Scope Guard Callouts

### 2.1 Full Callout — First Governed Section

The first section governed by a scope guard carries the full callout immediately after its heading:

```md
> **[Local guard SG-N]** [One-sentence restatement of the prohibition.]
```

### 2.2 Pointer Callout — Subsequent Governed Sections

Later sections governed by the same guard carry only a compressed pointer:

```md
> **[Guard SG-N applies]**
```

This preserves steering at the point of use without repeating full warning text.

---

<a id="dsn-section-3"></a>

## 3. Claim Format

### 3.1 Claim-Blocks

A claim-block is the smallest unit asserting a scientific definition, result, hypothesis, or interpretation: a sentence, an equation with its caption, a theorem with one proof status, a table row, or a short paragraph. Pure navigation, metadata, and routine derivation steps need no independent truth-status tag. A step making a new substantive claim does.

Each scientific block opens with its primary status, or with the paired `[RESULT]` form in §3.4. Split blocks when their conclusions have different proof grades, domains, or evidential bases. A section heading does not tag every assertion beneath it.

```md
`[ALG]` [family: MODEL-A] [conv: FRAME-A] [RID: STUDY-ALG-COEFFICIENT]
The coefficient equals the exact expression given below.
Depends on: [definitions and derivation].

`[HEUR]` [scope: physical interpretation of that coefficient]
The coefficient may provide a mechanism for [specified phenomenon].
```

Examples in this methodology are grammar templates, not registered RTG claims or scientific approvals.

### 3.2 Scope and Evidence Qualifiers

Truth-status tags are in backticks. Metadata qualifiers follow in plain brackets. A qualifier narrows or identifies a claim; it does not upgrade its truth status.

| Key | Meaning |
|---|---|
| `[conv: NAME]` | Named coordinate, normalization, orientation, gauge, or tensor convention |
| `[family: DESC]` | Defined model/parameter family |
| `[scope: DESC]` | Domain, interpretation, approximation order, or other validity limit |
| `[horizon: PARAMS]` | Explicit finite parameter set, time interval, degree, or campaign range |
| `[assuming: IDs]` | Assumptions not discharged by the statement; list fully in `Depends on:` |
| `[bridge-required]` | The specified use awaits a named identification/bridge; not export permission |
| `[obs-fit]` | Observable-fit evidence, not primitive/normalized-layer certification |
| `[import: SOURCE LOCATION \| RID]` | Exact source version and stable claim identity; §3.3 exceptions are explicit |
| `[proof: METHOD]` | E.g. written derivation, exact computation, rigorous interval certificate; evidence in §8 |
| `[provenance: STATE]` | E.g. source-read, source-reported, artifact-inspected, independently-checked; see §12 |
| `[RID: ID]` | Claim identity; not its present proof status |

Use readable continuation fields rather than packing every detail into one tag line. Only relevant qualifiers are required. A result's statement must nevertheless contain the complete applicable assumptions, quantifiers, units, and limitations.

### 3.3 Imported Claims

An import declares the **actual source version used**, the source claim's identity, inherited scope, and a `Depends on:` line. It also appears in the Import Ledger. A hypothetical transformation from the source object to a local one is a separate claim, not part of an unqualified imported theorem.

```md
`[ALG]` [import: SOURCE_DSN_vX.Y §6.2 #source-anchor | SOURCE-ALG-ITEM]
[Source statement restricted to the domain actually used.]
Depends on: [source definitions, conventions and prerequisites]. See §7.
```

Do not replace `[import:]` with `[source:]` for a newly written load-bearing import. Existing `[source:]` records are migration inputs, not a parallel canonical grammar. A simple bibliographic or historical reference may use ordinary prose without asserting proof import.

**Missing owner RID:** do not invent one, borrow an OPEN-module RID as a theorem ID, or register a proposed owner ID from a consumer. Use a temporary, explicit record:

```md
`[ALG]` [import: SOURCE_DSN_vX.Y §6.2 #source-anchor | RID unavailable]
[Exactly identified source statement.]
Owner RID: none in the inspected source; dedicated RID requested.
Depends on: [source assumptions]. Governance request: [local tracking key]. See §7.
```

This is a declared exception with unresolved identifier governance, not a scientific gap by itself. It requires enough versioned location and statement detail to identify one result. If the source itself has not been inspected, say `source-reported`, identify the intermediate memo/report, and do not describe the owner proof as verified. A missing load-bearing source is not replaced by recollection.

A newer source version does not automatically invalidate an older pinned import. Inspect changes to the specific claim. Retain intentional historical citations; update scientific uses and synchronization records deliberately.

### 3.4 The `[RESULT]` Tag — Mandatory Pairing and Conditional Proofs

`[RESULT]` is a synthesis marker, not a new proof grade. It must be paired with exactly one canonical status for the conclusion being asserted:

```md
`[RESULT]` `[from: HEUR]` [scope: model-to-physics interpretation]
[Interpretive consequence.]
Depends on: [exact source facts and the unproved identification actually used].
```

The weakest-undischarged-premise rule applies to an **unconditional conclusion that uses those premises as true**. Definitions are not “weak evidence,” and an unproved hypothesis does not lower the proof grade of a completely proved implication in which that hypothesis is explicitly assumed:

```md
`[THM]` [family: MODEL-A] [assuming: H1] [RID: STUDY-THM-CONDITIONAL]
If H1 holds, then P holds.
Depends on: [definitions and H1]. The proof establishes H1 => P, not H1.
Proof: [complete derivation or evidence location].

`[RESULT]` `[from: HYP]` [scope: proposed physical application]
P is proposed for the physical system, conditional on identifying it with H1.
Depends on: STUDY-THM-CONDITIONAL and [unproved physical identification].
```

There is no total strength ordering across definitions, algebra, engineering, and observations. Select the tag for the actual assertion. Split an exact identity, its numerical test, and its physical interpretation when they have different status. Bare `[RESULT]` and a combined `[from: ALG/NUM/HYP]` label are not canonical.

### 3.5 Section Heading Tags and Persistent Anchors

Technical subsections use a primary status and a stable anchor. A mixed-content suffix is prose, not a new compound truth tag:

```md
### §6.3 Normalization `[ALG]` — mixed content {#sec-normalization}
```

The heading is navigation; claim-block tags remain authoritative. A section devoted to a rejected route may use `[FAIL]`; a correction discussion may use `[COR]`. Neither proves anything beyond its tagged blocks. Do not invent positive content merely to give a rejection section a “positive” heading.

New anchors should describe content without requiring the current section number, e.g. `sec-normalization`. Preserve existing anchors such as `sec-6-3-radial` verbatim after moves or renumbering. Never reuse a retired anchor for unrelated content. Record redirects where a split changes the file.

The `{#...}` notation is a Markdown heading-attribute convention, not a universally supported HTML feature. Validate the chosen renderer; an explicit `<a id="sec-normalization"></a>` is an alternative. Imports identify the owner version and RID even when rendered-anchor support differs.

### 3.6 Corrections and Retractions

A scientific correction records the old statement/status, reason, new statement/status, evidence, and affected consumers. The new scientific assertion carries its own tag:

```md
`[COR]` Prior summary of [RID/version] omitted assumption H1 already present in the owner theorem. See Appendix B.
`[ALG]` [assuming: H1] [RID: ORIGINAL-ID]
[Corrected version of the same claim.]
```

Keep the RID when refining the same claim with an explicit versioned correction. A materially different proposition, domain, or replacement hypothesis receives a new RID with `Replaces:`. Do not quietly use a retained RID to mean a different theorem. Editorial spelling/link corrections belong in the change record; they do not require duplicating every typo in Appendix B.

---

<a id="dsn-section-4"></a>

## 4. Stable Identifiers and Ownership

### 4.1 Purpose

RIDs identify claims, definitions, OPEN modules, and artifacts independently of section numbers. Every externally used scientific result needs its own identity; closing an OPEN module does not turn that module's RID into the RID of each theorem it contains.

### 4.2 Format and Namespace Registry

```text
[STUDY_PREFIX]-[CATEGORY]-[SHORT_DESCRIPTION]
```

| Namespace | Custodian / routing |
|---|---|
| `DYAD` | RTG Dyadic Oscillator |
| `TRIAD` | RTG Triadic Birth–Lift |
| `GEN` | RTG Genesis Geometry; reassignment only through §13 |
| `TDRG` | RTG Discrete Genesis |
| `RECOG` | RTG Relational Recognition |
| `DZT` | RTG Dyadic Arithmetic-Resonance Transform |
| `AZ` | RTG Arithmetic Resonance and Zeta infrastructure/diagnostics |
| `UVM` | RTG UV Completion / OPEN M |
| `NUMGEN` | RTG Number Genesis |
| `RTG` | Programme-level entries |
| `RTG-OFN` | Existing Ontological Foundations namespace; match before the broader `RTG` prefix |
| `PL` | Pre-Legacy provenance records |
| `L0L1`, `L2` | Legacy-ledger namespaces; historical spellings retained and owner-qualified |

The additions beyond v1.2 are adopted registry synchronization in v1.3. They recognize custodians and existing usage; they neither assign programme maturity nor create/close a study. Shortnames such as OFN are not automatic RID aliases. Preserve existing nonstandard IDs (for example, legacy OPEN/LEM/PROP spellings) with an explicit owner map rather than silently rewriting them.

| Category | Meaning |
|---|---|
| `THM`, `ALG` | Theorem / algebraic-result identity |
| `DEF` | Definition or adopted axiom |
| `NUM`, `OBS` | Numerical or observational result identity |
| `HYP`, `CAND` | Hypothesis or candidate identity |
| `RESULT` | Synthesis-result identity |
| `OPEN` | Research or governance module |
| `ART`, `ENG` | Artifact or engineering-result identity |
| `FAIL` | Historical rejected-claim identity |

Category text is part of an immutable identifier, not a live truth-status tag. A RID containing `THM` does not remain theorem-grade if its proof is later corrected; conversely a proved candidate need not be renamed solely to change its category word.

### 4.3 Import Ledger Entry Format

Retain the compact v1.2 five-field format and add short continuation fields where required:

```md
- [RID: SOURCE-RID] :: [claim] :: SOURCE_DSN_vX.Y §6.2 #source-anchor :: [local use] :: [inherited scope]
  Source status: [tag in the inspected source, or explicitly source-reported].
  Depends on: [source assumptions; local identification/bridge RID, or not required with reason].
  Verification: [source text inspected; artifact inspected/rerun; or unavailable].
  Synchronization: [checked against named version; pending request/correction key if any].
```

An exact version is required; “current,” “latest,” and an unversioned shortname alone are insufficient. A stable RID is primary; section and anchor provide navigation. Preserve the missing-RID exception in §3.3 until owner assignment is complete.

**Three uses must stay distinct:** a reference-only summary; a load-bearing import of an owner result; and a locally proved consequence of imported premises. The last may receive a local RID for its genuinely new inference, but must not re-own the original theorem. A mirror statement cites its source rather than creating duplicate authority.

For cross-branch physical use, retain the applicable programme firewall: cite a named bridge with a proved `[ALG]` or `[THM]` statement (including an appropriate rigorous-IA form), its source/target objects, assumptions, and permitted use. A proposed bridge, a diagnostic correlation, or reuse of standard mathematics does not certify a physical identification. A bridge may itself be conditional; its unproved physical premises remain visible under §3.4. Programme tier numbers do not replace branch and layer typing.

### 4.4 RID Lifecycle

Only the designated owner registers or reassigns its claim IDs, with the adoption decision recorded. A consumer or reviewer may propose a name, not present it as an existing owner record.

Retain identity for an editorial repair or a correction to the same proposition. If a supposed universal theorem is replaced by a materially narrower theorem, or a revised model changes the proposition, create a successor RID and retain the original verdict. A corrected summary of an already-qualified owner theorem may retain that theorem's RID.

Promotions, demotions, transfers, and corrected rejection decisions leave an audit trail. Never delete/recycle a retired ID. During a move, record old owner, new owner, old/new location, unchanged statement or explicit scientific change, and the approval/version. The original prefix may remain even after custody changes.

### 4.5 Exports, Dependency Records, and Alias Resolution

The owner's result entry or a short export index lists known consumers and their local uses. The corpus update record is the reverse-dependency checklist; it is not a second scientific ledger.

An alias is valid only when its owner records an exact mapping. Similar names do not establish equivalence. Conflicting ownership or two claims under one RID create a resolution task; do not settle them by choosing the newer-looking filename.

RIDs are optional for strictly internal minor claims, but mandatory for exported claims, externally used definitions, OPEN modules, and claimed computational certificates, subject to the explicit temporary exception in §3.3.

---

<a id="dsn-section-5"></a>

## 5. OPEN Problem Entry Format

### 5.1 Full Entry

```md
**OPEN [N] — [title]** [RID: STUDY-OPEN-TARGET]

Status: ACTIVE | PARTIAL | CLOSED
Owner study: [one canonical DSN]
Scheduling: [READY | BLOCKED | DEFERRED; optional and independent of proof status]
Question: [precise target and domain]
Closure criterion: [required statement, result grade, evidence, and scope]
Dependencies: [result/module RIDs; mark genuine prerequisites versus alternative routes]
Known consumers: [documents/local claims already using partial results]
Proposed consumers: [future uses, not established imports]

Closed sub-items:
- [statement] :: `[TAG]` :: [RID: theorem/result ID] :: [proof/artifact location]

Active sub-items:
- [unresolved target] :: `[OPEN]` :: [required evidence or next action]

Retracted/superseded sub-items:
- [old target] :: [workflow status] :: [reason; Appendix B pointer]

Next required artifact or decision: [exact request, or none]
Closure record: [if applicable: date, outcome, grade, scope, evidence, adoption]
Governance follow-up: [missing RID, archive item, or consumer synchronization; or none]
```

Omit inapplicable sub-lists. Owner, question, criterion, and current status remain explicit. Historical `Imports to` / `Exports to` fields must be interpreted and migrated to the unambiguous consumer fields, not mechanically swapped.

A module ID and a result ID serve different roles. If a module closes several results, each independently imported result needs its own RID.

### 5.2 Closure Protocol

First verify the declared criterion. Record the **outcome and grade**: proved, disproved at stated scope, numerical diagnostic completed, model/protocol adopted, or administrative recovery completed. Completing a finite numerical task does not prove its universal analogue. Choosing an effective model does not prove that nature selects it.

After adoption, set the scoped status, move full proof/closure detail to §6, keep a one-line closed reference at the end of §2, update §1 where needed, record the version change, and process all known consumers. Example:

```md
**OPEN [N] — [title]** [RID: STUDY-OPEN-TARGET] :: CLOSED :: `[ALG]` :: [scope] :: Results: STUDY-ALG-ITEM :: [closure location]
```

A completed scientific criterion and an unfinished owner-RID assignment can be recorded separately. A theorem must not be reopened merely because its identifier is missing. Conversely, closing an archive inventory by recording an artifact as lost is not scientific revalidation.

### 5.3 Partial Closure and Residual Work

Use `PARTIAL` while part of the original criterion remains unresolved. Keep `ACTIVE` when no part has yet closed. A blocked task is still scientifically open.

A module may close at its original finite, conditional, or diagnostic scope with a separately registered extension. It may not quietly narrow an originally universal criterion just to mark it closed. Record that change, its rationale, and any successor OPEN. Distinguish optional robustness checks from unresolved premises of the claimed result.

### 5.4 Dependency Logic

An alternative proof route has that route's prerequisites; it does not automatically impose them on every route. An exact conditional result may be usable while a model-selection question remains open, but only as the stated conditional result. A circular chain of summaries is not a proof or an ownership resolution.

---

<a id="dsn-section-6"></a>

## 6. AI Context Core

### 6.1 Definition and Boundary

For a standard technical ledger, the core spans exactly §1–§4. It gives orientation, accepted scope, dependencies, and active work; it is **not guaranteed sufficient to reconstruct a proof or run an experiment**. The final line of actual §4 content is the single `AI_CONTEXT_CORE_END` comment shown in §1, before §5.

Examples and quoted markers inside code fences are not extraction boundaries. For a nonstandard profile, declare the corresponding core sections explicitly. Methodology itself is exempt from the scientific-ledger marker requirement.

The core should not exceed 800 lines. If it does, move historical addenda, complete proofs, closed-module detail, and raw tables out of the core; document any temporary migration exception. Do not achieve the limit by deleting assumptions.

### 6.2 Instructions for AI Systems Reading a DSN

1. Identify the exact file/version and its adoption state. Read current state, OPEN registry, scope guards, and layer routing before drawing conclusions.
2. Treat `[ALG]` and `[THM]` as established **within their stated assumptions and scope**, subject to explicit correction or verification flags. Inspect the detailed statement when using it; do not infer proof from the tag alone.
3. Keep owner statements, source-reported history, independently inspected evidence, and new review deductions distinct. Do not silently resolve a contradiction between summary, proof, script, and memo.
4. Inspect the relevant technical section and artifacts before a computation or certification claim. A parsed excerpt, filename, or script's final PASS line is not full inspection.
5. Follow the Import Ledger. Use actual versioned sources, not memory of an earlier session. Report absent sources and ask for the precise missing item when it is needed.
6. Apply guards at the actual use point. An analogy or abstract mathematical isomorphism is not a physical bridge; a convention-fixed number is not automatically invariant.
7. Report a newly found error or possible correction as a review finding until adopted. Preserve counterexamples, assumptions, and uncertainty. Do not promote a proof because several AIs repeat it.
8. Use current records for current status and history for provenance. If those disagree, flag the inconsistency rather than letting either silently overwrite the other.

### 6.3 Instructions for AI Systems Writing or Updating a DSN

1. Write new technical results in §6; update §1 only for changed canonical content. Keep closed proofs out of the active registry.
2. Follow the claim, OPEN, import, artifact, and correction formats. Assign owner RIDs only with recorded authority; retain explicit missing-ID requests otherwise.
3. Distinguish exact symbolic computation, rigorous interval verification, ordinary numerical tests, and physical interpretation. State which checks were actually executed.
4. Preserve frozen inputs and exact source history. Use assertion-gated edits, a versioned output, a readable diff, and a change record; verify that promised result bodies survived the edit.
5. Follow §13 for splits, merges, transfer, and the two-pass corpus update. A recommendation in a review or memo does not itself authorize a scientific reclassification.
6. Keep prose and metadata in English under §0.7. Preserve exact historical identifiers and notation.
7. Ask focused questions for missing definitions, versions, conventions, scripts, datasets, or owner decisions. Record unresolved requests explicitly; do not invent archive paths, hashes, approvals, or previous-session content.
8. Finish with the actual output version, checks performed, unresolved limitations, and affected consumers. Never claim that inaccessible project files or remote archives were updated.

---

<a id="dsn-section-7"></a>

## 7. Correction, Demotion, and Retraction Protocol

A review finding may be editorial, scope/typing-related, scientific, or evidential. Its adoption and effect must be explicit.

For a scientific correction or demotion: identify the original version/RID and statement; preserve it in Appendix B or an immutable referenced record; give the corrected statement/status and reason in §6; update §1 and the relevant OPEN entry; record the change in Appendix A; and propagate it to known consumers. Where a shared premise changes, assess each dependent conclusion rather than mechanically changing every tag.

**Missing evidence:** distinguish `not supplied for this review` from `lost`, `never existed`, or `failed validation`. Lack of an attachment alone is not refutation. Keep the source's reported grade distinguishable from the local verification state. New promotion or artifact-dependent certification may remain blocked until the required evidence is inspected.

**Conflicting proof or computation:** preserve both records and the exact mismatch. Identify whether it concerns model, coordinate, coefficient, domain, numerical implementation, or interpretation. An unresolved load-bearing contradiction must not be described as reconciled merely because one source is later or carries a stronger tag.

**Rejected statements:** `[FAIL]` records a precisely scoped rejection. A valid refutation cannot be promoted away without changing the proposition or correcting the refutation itself. A materially revised hypothesis gets a new RID. If the rejection was erroneous, an explicit `[COR]` records the error and the new assessment of the original proposition; the historical rejection is never deleted. A failed derivation route is not a refutation of every route or of the overarching hypothesis.

Cosmetic edits and resolved navigation defects do not require scientific demotion. Revised physics or mathematical scope does require a substantive record even when the changed text is short. Neither an automated formatter nor an administrative editor silently performs that decision.

---

<a id="dsn-section-8"></a>

## 8. Tag Registry — Canonical Definitions

### 8.1 Claim-Status Tags

These retain the v1.2 spellings. They describe different kinds of assertions; they are not one universal ladder of strength.

| Tag | Definition |
|---|---|
| `[DEF]` | A definition or explicitly adopted axiom, with its role and domain stated. An axiom's adoption is not evidence of physical necessity. |
| `[THM]` | A complete mathematical proof of the stated proposition under explicit assumptions and conventions. Convention independence and physical universality are additional properties, not requirements hidden in this tag. |
| `[THM-ALG via IA]` | A theorem established with a rigorous interval-arithmetic certificate that covers the claimed domain and whose proof procedure, rounding control, and artifacts are archived and reproducible. |
| `[ALG]` | An exact algebraic derivation or symbolic identity/value with its domain, coefficient field, and conventions specified. Finite exact checks support only their declared finite scope unless accompanied by a general argument. |
| `[ALG via IA]` | An algebraic assertion established by a complete rigorous interval certificate for the stated domain. It does not certify a broader theorem not covered by that certificate. |
| `[ALG candidate]` | An exact-form conjecture supported by structural or numerical evidence, not yet proved. Exact-looking notation is not exact proof. |
| `[ALG structure]` | A partially derived algebraic mechanism; the proved part and remaining coefficients, assumptions, or completion are explicitly separated. Not interchangeable with a fully established `[ALG]` result. |
| `[ENG]` | Validated engineering infrastructure within named tests and intended use. Not a proof of the physics processed by it; not a tag for merely planned code. |
| `[NUM]` | A numerical result with a stated protocol and finite scope. Artifact availability, independent repeatability, and robustness are recorded separately. |
| `[NUM strong]` | A numerical result with documented relevant robustness or independent checks (such as seeds, methods, precision, or runs). The exact checks are named; high precision alone is insufficient. |
| `[OBS]` | An observation not yet systematically characterized by a defined campaign. |
| `[HEUR]` | An interpretation or heuristic argument; not a complete proof. |
| `[HEUR strong]` | A heuristic interpretation supported by multiple stated checks; still not theorem-grade. |
| `[HYP]` | An unproved working hypothesis. It may have supporting evidence; its defining assertion remains unestablished. |
| `[OPEN]` | An unresolved task/question; workflow information, not a scientific conclusion. |
| `[FAIL]` | A rejected claim or route, with the exact rejected scope and basis. Permanence applies to the record, not infallibility of the rejection decision; see §7. |

Evidence and adoption qualifiers never turn a numerical or heuristic statement into an exact one. Conversely, proving a conditional mathematical proposition does not require proving the physical truth of its hypotheses.

### 8.2 Scope-Status Qualifiers

The single canonical qualifier registry is §3.2. Do not maintain a second, potentially divergent table here. A qualifier may restrict the claim or disclose evidence status; it may not broaden the claimed domain beyond the statement or erase an assumption inherited from a source.

The literal `[from: TAG]` occurs in backticks only as the companion to `[RESULT]`. It refers to a tag in §8.1, including a canonical compound spelling when appropriate, not a new slash-combination.

### 8.3 Workflow-Status Tags

| Tag | Meaning |
|---|---|
| `[RESULT]` | Synthesis/consequence marker; must be paired with `[from: TAG]` under §3.4. |
| `[COR]` | Correction notice with old/new statements, reason, and traceable history. The corrected scientific assertion receives its own status. |
| `[RETRACTED]` | Formal withdrawal; reason and replacement, if any, recorded permanently. Withdrawal need not mean a proof of falsity. |
| `[SUPERSEDED]` | Replacement by a revised record; replacement pointer required. Supersession alone does not refute the old scoped proposition. |
| `[ARCHIVE-READY]` | A specific version is ready for immutable archival at its declared completeness and limitations. It does not imply that the research programme has no future work. |

Document adoption states, task scheduling, artifact availability, and review checks are metadata fields, not additional scientific truth tags. Normative rules and administrative change records in this Methodology do not masquerade as `[ALG]` results.

### 8.4 Local Alias Protocol

Place `## Local Tag Aliases` after the header (or the profile's declared equivalent). Each alias maps to canonical status and qualifiers without changing their meaning. It does not propagate automatically into another document.

```md
| Local alias | Canonical expansion | Use |
|---|---|---|
| `[ALG conditional]` | `[ALG]` [assuming: stated hypotheses] | Proved algebraic implication, not proof of the hypotheses |
| `[ALG diagnostic]` | `[ALG]` [scope: named diagnostic model] | Exact result in that diagnostic model |
| `[NUM diagnostic]` | `[NUM]` [scope: named diagnostic campaign] | Finite numerical evidence |
| `[MATH]` | `[THM]` [scope: standard mathematical input] | Established background theorem with source or sufficient derivation, not a novel RTG result |
| `[INTERP]` | `[HEUR]` [scope: interpretation] | Interpretive inference; use `[HYP]` directly for a distinct proposed hypothesis |
```

An alias cannot override a canonical tag, including `[ALG structure]`. Existing `[ALG/NUM]` or `[ENG/ALG]` mixtures must be unpacked into the exact assertion and its numerical/engineering corroboration. They are not permission to attach an exact grade to the union of unrelated evidence. Planned engineering work uses an artifact status or `[OPEN]`, not an alias expanding to validated `[ENG]`.

Migration preserves old spellings in historical quotations; new live claims use canonical forms or explicitly declared valid aliases.

---

<a id="dsn-section-9"></a>

## 9. Promotion and Demotion Criteria

### 9.1 Promotion and Scope-Extension Table

Transitions are available when their evidence conditions are met; a result need not pass through every row. Scope expansion, proof completion, numerical robustness, and physical interpretation are separate actions.

| From | To | Required |
|---|---|---|
| `[OBS]` | `[NUM]` | Defined measurement/computational protocol, campaign scope, and recorded outputs; disclose reproducibility state. |
| `[NUM]` | `[NUM strong]` | Documented relevant independent or robustness checks, with their actual extent. |
| `[NUM strong]` or `[HEUR strong]` | `[ALG candidate]` | An explicit exact-form conjecture and a proposed route; no claim that the conjecture is proved. |
| `[ALG candidate]` | `[ALG]` | Exact derivation in a declared field/ring or a complete exact computation establishing the stated domain. Floating precision and integer-relation guessing alone do not qualify. |
| `[ALG structure]` | `[ALG]` | All missing steps necessary for the full stated assertion completed; retained assumptions explicitly listed. |
| `[ALG]` | `[THM]` | Complete proof at the claimed quantifiers and scope, including any rigorous computational component. No need to erase legitimate conventions. |
| `[ALG via IA]` | `[THM-ALG via IA]` | Complete theorem argument and rigorous certificate covering the entire asserted domain; archived/reproducible proof procedure. |
| Convention-fixed result | Explicit invariant/generalized result | A transformation or invariance proof for the specified objects and admissible transformations. Choosing a canonical convention alone is insufficient. |
| Finite-horizon exact result | All-parameter result | A valid general argument; a larger finite sweep alone does not qualify. |
| `[HEUR]` | `[ALG structure]` | A proved algebraic component of the mechanism, with unproved interpretation kept separate. |
| `[HYP]` | `[HEUR]` or `[HEUR strong]` | Supporting evidence and an articulated interpretive argument; retain any separate unproved proposition as such. |
| Any scientific claim | `[FAIL]` | A valid refutation at the exact stated scope, or rejection of a precisely delimited route. |

Every proposed promotion identifies the condition met, proof/evidence location, owner decision, and consumers. Unsupported promotion is an unadopted request, not a new scientific grade. No Methodology update automatically promotes existing `[ALG]` entries to `[THM]`.

### 9.2 Demotion and Correction Table

| Original assertion | Finding | Appropriate action |
|---|---|---|
| Complete exact result | Essential gap in proof | Record the gap; retain only established components and use `[ALG candidate]`, `[ALG structure]`, or `[OPEN]` for the unresolved remainder. |
| Universal result | Proof covers a smaller domain | Correct the overclaim; distinguish the valid restricted result and the unresolved generalization, with IDs under §4.4. |
| `[NUM strong]` | Relevant independent agreement fails | Reassess the specific robustness claim and affected result; use `[NUM]` when justified, with the failed check retained. |
| Interpretive conclusion | Counterevidence or missing identification | Narrow or weaken the interpretation without automatically demoting intact underlying algebra. |
| Any reported result | Required artifact absent from this review | Record verification/provenance limitation; do not equate absence with refutation. |
| Rejected proposition | Rejection itself shown erroneous | Correct the decision under §7; retain the historical record and new evidence. |

All substantive changes use §7 and the dependency propagation in §13. Reformatting alone supplies no scientific justification for retagging.

---

<a id="dsn-section-10"></a>

## 10. Grammar and Formatting Rules

### 10.1 Section Numbering and Cross-References

Scientific sections use `§1`, `§6.3`, and `§6.3.1`; appendices use `Appendix A`. Persistent anchors and RIDs survive renumbering under §3.5. A source citation must identify the version and claim, not just a mutable section number.

Use one live definition for each symbol or metadata field. State alternate meanings explicitly. In particular, distinguish primitive and normalized coordinates, exact and approximate relations, phase orientations, pre/post-event counters, matrices and their tensor types, signed values and magnitudes, and time horizons. These are requirements to state the study's conventions, not Methodology's selection of those conventions.

### 10.2 Ledger and Registry Format

Use tables for genuinely tabular comparisons with short fixed-column entries: tag definitions, high-risk claims, promotion criteria, and concise contributor records. Use `::` structured lists for long growing Import and Artifact Registries and for OPEN sub-items.

```md
- [RID: SOURCE-RID] :: [claim] :: SOURCE_DSN_vX.Y §6.2 #anchor :: [local use] :: [scope]
  Depends on: [required inputs]. Verification: [actual check state].

- [RID: STUDY-ART-CHECK] :: `check.py` :: [specific role] :: AVAILABLE; NOT EXECUTED IN THIS REVIEW
  Version/hash: [exact value if known; otherwise “not supplied”].
  Evidence specification: [inline §12 fields or a versioned manifest].
```

An artifact may also have a separate `[ENG]` claim if its engineering behavior was validated. Registry presence is not that claim. Avoid delimiter ambiguity by putting long metadata on continuation lines. Do not replace evidence with a table cell saying only “certified.”

### 10.3 LaTeX Formatting

Use `$...$` inline and `$$...$$` for display equations. When plain-text mathematics is retained for compatibility with a technical tool, state that convention and keep expressions unambiguous. Named equations are referenced through stable anchors or RIDs, not through their current line number alone.

### 10.4 Code and Artifact References

Use backticks for filenames and exact symbols. Pin the file version/hash or repository commit in §8. A relative path is resolved against a named archive/package root. A filename mentioned in a transcript is not evidence that the corresponding file is present.

### 10.5 Blockquotes

Reserve blockquotes for local scope-guard callouts and high-priority editorial warnings. Keep ordinary derivations and version history outside them. Exact source quotations for audit purposes must be clearly labeled and located; a quoted historical claim is not a live assertion.

### 10.6 Boxed Results

Use boxes sparingly, ordinarily no more than two or three central results in the canonical summary. A box does not replace the tag, scope, or source. Additional boxes in a long technical appendix should serve navigation rather than apparent emphasis-based promotion.

### 10.7 Change-Record Format

```md
- **§X.Y [editorial | scope/typing | scientific | evidence | governance]:**
  [Old issue, new treatment, reason, affected IDs, and pending consumer updates.]
```

These are administrative change classes, not scientific truth tags. Exact class names may be recorded as fields in a machine-readable manifest. “Updated” or “fixed” alone is insufficient for a scientific change.

### 10.8 Literal Preservation

Preserve source equations, filenames, identifiers, and meaning when moving content. Do not normalize a historical mistake out of a quotation. Any correction, alternative derivation, or model change is identified as such. UTF-8 English prose may retain standard mathematical symbols and contributor names.

---

<a id="dsn-section-11"></a>

## 11. Anti-Patterns Catalogue

| Anti-pattern | Why it fails | Correct practice |
|---|---|---|
| Scientific assertion without a claim tag | Evidence level becomes implicit | Tag the block; split mixed assertions. |
| Using a theorem tag to imply physical selection | Confuses proof and interpretation | State assumptions and the independent physical bridge. |
| Treating convention-fixed proof as necessarily incomplete | Confuses scope with rigor | Allow complete conditional proofs; prove invariance separately. |
| Calling a chosen canonical gauge “gauge-independent” | Canonical choice is still a choice | Keep its convention until the specified invariance theorem exists. |
| Promoting high precision, guessed relations, or a finite sweep to exact general proof | Computation has not covered the claim's quantifiers | Separate numerical evidence, finite exact verification, and all-parameter derivation. |
| Using an observable fit as a primitive-map identity | Silently changes the mathematical object | Supply the coordinate/observable map and approximation scope. |
| Reusing a number in two differently normalized models | Numerical agreement is not an identification | Trace variables, dimensions, normalization, and transfer assumptions. |
| Loading a long changelog before current state | Conceals the present position | One current summary; history in Appendix A. |
| Keeping closed proofs in the active OPEN registry | Obscures residual obligations | Full proof in §6; short closed reference in §2. |
| A bare `[RESULT]` or a slash-combined truth label | Hides the actual grade of the conclusion | One paired status for each assertion, with conditional logic under §3.4. |
| Local alias overriding a canonical tag | Changes meaning without a methodology decision | Correct the alias or request a central revision. |
| Choosing the newest-looking source to resolve a contradiction | Version order is not proof | Inspect the owner statement and evidence; record the discrepancy. |
| Cross-branch physical import without a named bridge | Transfers meaning not established by the formulas | Keep reference-only analogies separate; require the applicable bridge. |
| Assigning a module RID to an unnamed theorem | Gives false claim-level identity | Request the theorem's own RID; retain a precise temporary locator. |
| Silently renaming IDs after promotion or moving sections | Breaks provenance and consumers | Preserve IDs/anchors or record explicit successor/transfer mappings. |
| Treating `PASS`, a hash, or a manifest as mathematical sufficiency | Identity and execution do not prove test adequacy | Inspect the checks and match them to the claim. |
| Saying an unavailable certificate failed | Confuses evidence access with evidence content | Record unavailable/not rerun; assess separately. |
| Copying a reviewer deduction into an owner as already approved | Erases adoption and authorship | Record the contribution, verification, and owner decision. |
| Treating file split/merger as scientific reconciliation | Layout does not establish model equivalence | Keep incompatible objects and disputed claims explicit. |
| Claiming the entire corpus was synchronized after editing one file | Consumers and pinned imports may remain unchanged | Maintain per-consumer completion records in the two-pass update. |

---

<a id="dsn-section-12"></a>

## 12. Evidence and Computational Certification

### 12.1 Evidence Contract

For a load-bearing computational artifact, record these fields inline or in an immutable, versioned manifest referenced from §8:

| Field | Required content |
|---|---|
| Identity | Artifact RID, exact filename, version or commit, and hash when available |
| Custody | Owner and retrievable archive/package location; explicitly unknown if absent |
| Target | Exact claim/RID and the part actually checked |
| Inputs | Model, coordinates, conventions, parameters, seeds/data identities, inclusion/exclusion rules |
| Arithmetic | Exact field/ring or numerical precision; interval method and rounding guarantees if used |
| Execution | Command, dependencies/environment, and any resource-sensitive assumptions |
| Acceptance | Assertions, domains, coverage, thresholds, expected success/failure outcome |
| Outputs | Logs, machine-readable results, exit status, run date and executor when known |
| Independence | What code, formulas, inputs, or implementations were shared between alleged independent checks |
| Limitations | Untested domains, analytic premises, finite-horizon limits, and unresolved source issues |

Not every artifact needs an executable script: a complete written proof can be its own evidence. Every computational certification claim does need enough information to reconstruct the relevant computation and its relation to the theorem. Missing values are disclosed rather than fabricated.

### 12.2 Separate Identity, Execution, and Adequacy

Use explicit review states, not a single overloaded “verified” flag: **source statement inspected**, **artifact bytes available**, **hash checked**, **code inspected**, **executed in this review**, **independent mathematical check**, and **claim coverage assessed**. Record only the actions actually performed. A reported prior run remains reported until locally checked.

A successful exit code establishes only that the implemented acceptance conditions passed. A falsifier can deliberately return nonzero on a valid counterexample; preserve its documented semantics. Distinguish execution errors, failed assertions, inconclusive resource limits, and a scientifically successful negative result.

Exact tests with rational or algebraic arithmetic establish their specified finite assertions. They establish an all-parameter theorem only with a general derivation or a justified exhaustive reduction. Ordinary floating-point residuals, regardless of precision, are not exact equality proofs. Rigorous interval certificates require verified enclosure, coverage, and rounding controls, not merely an interval-like output format.

### 12.3 Provenance Requests and Review Deductions

When an archive item is needed, request its exact owner/version, claim, and reason: e.g. the map definition and orientation rule, the normalizer used for a coefficient, the raw data/selection protocol behind a fit, or the proof/checker underlying a closure. Distinguish blocking and nonblocking requests.

Information recovered from another account, AI session, or transcript enters as **recovered evidence pending inspection**. It may resolve a provenance gap; it does not automatically override an owner DSN. A newly reconstructed proof or script is labeled as an independent contribution, not a rerun of missing original code.

A maintenance review can discover a genuine new proof. Its proposed owner, statement, assumptions, artifact, and adoption decision must be recorded before the scientific ledger changes. Do not classify a scientific promotion as mere reference cleanup.

### 12.4 Validation Boundaries

A syntax linter checks only documented machine-verifiable rules. It cannot certify truth, physical admissibility, model equivalence, or completeness of a proof. A parser-specific limitation is reported, not silently interpreted as a scientific failure. Validation reports state which checks ran, which were manual, and which were not implemented.

---

<a id="dsn-section-13"></a>

## 13. Controlled Revision, Restructuring, and Corpus Synchronization

### 13.1 Working Revision and Adoption

Preserve the adopted source version. Create one explicit target version as a draft; record its base, editor, date, and change record. New drafts are not described as adopted merely because their text was generated. Record the PI/authorized owner acceptance before changing the adopted pointer.

Use one target version through the coordinated revision cycle; identify intermediate drafts separately. Do not invent minor-version successors for every cross-reference adjustment. If an already adopted target changes materially, issue a new immutable version. A release manifest identifies the actual adopted versions, profiles, and hashes; it does not replace their claims.

### 13.2 Issue Record

The maintenance register is administrative, not a scientific DSN. Each issue records: tracking key; source/version/location; class (editorial, scope/typing, scientific, evidence, governance); proposed action; owner; proof/artifact or reason; decision state; affected consumers; and pass-two completion.

Decision states distinguish **proposed**, **accepted**, **deferred**, **rejected**, and **needs evidence**. They are not claim-status tags. No row is closed merely because a file was edited; the specified evidence and propagation must also be checked.

### 13.3 Split, Merge, and Ownership-Transfer Protocol

Before restructuring, record the purpose and boundaries, proposed canonical owners, and a claim-by-claim movement map. Do not merge different generators, coordinate conventions, or diagnostic models solely because they share symbols or topics.

For each moved claim preserve its statement, assumptions, proof grade, RID, evidence, and history. If any of those scientific contents changes, record a separate scientific correction. Keep original frozen files; add source/destination pointers and update importers. A new filename is not a new proof.

A split has one designated owner for each claim and no competing current summaries. A merger retains all source histories and marks retired files explicitly. Technical appendices remain subordinate to a canonical DSN and are versioned or hash-pinned. They may carry full derivations without becoming a parallel research ledger.

This Methodology authorizes a process, not a specific Genesis, Triadic, Number Genesis, AZ, or legacy restructuring. Those are separate owner decisions.

### 13.4 Two-Pass Corpus Update

**Pass 1 — owner-first revision:** establish baseline versions and profile maps; resolve owner statements and typing; separate accepted corrections from unresolved review findings; assign or request missing IDs; record evidence limitations; and produce a versioned draft plus diff for each study. Handle genuine cross-study cycles by claim-level coordination, not by letting one summary settle the other.

**Pass 2 — consumer and registry synchronization:** traverse all affected imports, summary statements, OPEN states, guards, and artifact pointers against the accepted owner versions. Update foundational feedback and programme status summaries after their technical inputs are reconciled. Check current-state agreement without erasing intentionally pinned historical citations.

A methodology change alone does not apply itself to all source files, retag their claims, reassign theorem ownership, or satisfy programme bridge gates. Existing v1.2 documents remain identified as such until individually migrated.

### 13.5 Release Checks

Before calling a draft review-ready, verify that edits actually applied, required sections/result bodies are present, code fences and anchors are valid, IDs are not silently reused, the diff matches the change record, and preserved inputs remain unchanged. Check examples as well as normative rules.

Before calling the corpus synchronized, verify the owner-to-consumer records and the adopted manifest. Remaining scientific OPENs are expected; unresolved load-bearing contradictions cannot be described as resolved. Explicitly accepted evidence limitations, pending archive recovery, and deferred governance actions are listed rather than concealed.

Formatting/structure checks and scientific checks are separate. A snapshot may be archived with declared limitations; do not call it fully certified or fully synchronized beyond the completed checks.

---

<a id="dsn-appendix-a"></a>

## Appendix A — Version History

### v1.3 — September 20, 2026 — Adopted

- **Adoption [governance]:** Mustafa (PI) approved all proposed updates in Draft 1, including policy proposals P1–P5 and the rule repairs recorded under M13-C01–M13-C12. V1.3 is the active canonical methodology, superseding v1.2.
- **Finalization [editorial/governance]:** Updated release metadata, namespace-adoption wording, the Appendix B introduction, and the footer; added the adoption record. No new substantive rule was introduced beyond the approved draft.
- **Preservation [provenance]:** The September 19 Draft 1 entry below remains the historical pre-adoption record. V1.2, Draft 1, and its change record are retained unchanged in the release package.
- **Scope [governance]:** No scientific result was promoted, demoted, transferred, or closed; no study split or merger was enacted. Other DSNs migrate individually under §13.
- **Follow-up [evidence/governance]:** Archive-amendment recovery and compatibility with any existing owner linter/renderer remain nonblocking, unverified items in `DSN_METHODOLOGY_v1_3_RELEASE_RECORD.md`. The next document-level step is Programme Overview's inventory/architecture pass.

### v1.3 — September 19, 2026 — Draft 1 (not yet adopted)

- **§0 [governance]:** Recast the single-file rule as one canonical owner per study; add document profiles, independent status axes, and English-language maintenance.
- **§1 [scope/typing]:** Preserve the technical §0–§9 template; formalize nonstandard profile maps, one current summary, and versioned technical appendices.
- **§§3/8/9 [scientific-method correction]:** Separate complete conditional proofs from unproved physical premises; remove convention independence as a prerequisite for `[THM]`; distinguish exact computation from high precision and resolve the `[NUM]` reproducibility inconsistency.
- **§§3/4 [governance]:** Preserve canonical import syntax; add exact source-version, missing-RID, namespace, and owner-transfer rules. Registry additions are proposed synchronization, not programme promotion.
- **§§5/7 [governance]:** Separate scoped scientific closure from identifier/archive tasks; disambiguate consumers; preserve but permit explicit correction of mistaken rejection decisions.
- **§§3/10 [editorial]:** Preserve old anchors after moves; use semantic anchors for new sections; correct the heading-attribute description and avoid undeclared mixed tags.
- **§12 [evidence]:** Add artifact/check-coverage requirements and explicit distinctions between reported, inspected, rerun, and independently reconstructed evidence.
- **§13 [governance]:** Add assertion-gated editing, draft/adoption states, issue records, split/merge custody, and owner-first/consumer-second migration.
- **Appendix B [provenance]:** Record substantive replacements of v1.2 rules. Earlier version histories remain verbatim below.
- No RTG scientific result is promoted, demoted, transferred, or closed by this draft. No companion document is edited.

### v1.2 — June 2026

- **§3.2 [format]:** Replaced backtick scope qualifiers with plain-bracket format; introduced canonical shorthand keys (`[conv:]`, `[family:]`, `[scope:]`, `[horizon:]`, `[obs-fit]`, `[import:]`). Eliminates the visual ambiguity between truth-status tags (backtick) and scope qualifiers (plain bracket).
- **§3.5 [format]:** Added persistent HTML anchor requirement `{#sec-N-M-slug}` to all §6 subsection headings. Anchor slug is content-based, not tag-based, so promotion/demotion does not break links.
- **§1 architecture [format]:** Added `<!-- AI_CONTEXT_CORE_END -->` HTML comment as a machine-parseable boundary marker at the end of §4 in the scientific DSN template.
- **§10.2 [format]:** Introduced the table vs. structured-list split: tables for fixed-column comparisons; `::` structured lists for Import Ledger, Artifact Registry, and OPEN sub-items. Reduces token overhead in long-running registries.
- **§4.3 [format]:** Import Ledger entry format updated to `::` structured list.
- **§11 [format]:** Added anti-pattern entry for Markdown tables in long registries.
- **§8.2 [format]:** Scope qualifier shorthand table added as canonical reference, mirroring §3.2.
- No changes to tag definitions, promotion criteria, OPEN format logic, or demotion protocol.

### v1.1 — June 2026

- Claim-block model introduced (§3.1); replaced per-sentence tagging.
- `[RESULT]` mandatory truth-status pairing added (§3.4).
- Section heading rule changed to primary-positive-status + `/ mixed` (§3.5).
- Stable Identifier (RID) system added (§4).
- OPEN entries gained RIDs, `Exports to` field, and sub-item RIDs (§5.1).
- Import Ledger added as mandatory §7 (§1 architecture).
- Formal Demotion Table added symmetric to Promotion Table (§9.2).
- Anti-patterns catalogue extended with four new entries.

### v1.0 — June 2026

Initial release. Consolidated tag definitions, fixed document architecture, AI reading/writing instructions, OPEN entry format, promotion criteria, and anti-patterns from the DSN critique process.

---

<a id="dsn-appendix-b"></a>

## Appendix B — Retired and Replaced Methodology Rules

These administrative correction keys are not historical scientific RIDs. They identify the rule replacements adopted in v1.3 on September 20, 2026. Exact old locations refer to the preserved `DSN_METHODOLOGY_v1_2.md`; the original Draft 1 proposal and its change record remain historical records.

**M13-C01 — Single-file scope.** Original §0.3: “one dedicated scientific DSN per study branch.” Replacement: §0.3, one canonical DSN per study with versioned supplements and explicit custody. Reason: a scientific branch already contains multiple studies; file structure must not imply duplicate claim authority.

**M13-C02 — Universal fixed architecture.** Original §1 applies the technical section order to every scientific DSN without a profile exception. Replacement: §§0.5/1, retain the standard technical template and require functional maps for explicitly different document classes. This does not exempt any profile from evidence or import rules.

**M13-C03 — Convention-independent theorem requirement.** Original §8.1 defines `[THM]` as a complete “convention-independent” proof; §9.1 links promotion to removing convention ambiguity. Replacement: §§3.4/8.1/9.1, allow complete proofs under explicit conventions and assumptions; invariance remains a distinct theorem. No automatic retagging of existing claims follows.

**M13-C04 — Unqualified weakest-premise rule.** Original §3.4 assigns every `[RESULT]` the weakest premise without distinguishing a proved implication from an asserted physical application. Replacement: §3.4, assumptions in a conditional theorem are not claimed proved; unproved physical identifications still constrain the application's grade.

**M13-C05 — Numerical reproducibility conflict.** Original §8.1 defines `[NUM]` with reproducibility “not yet established,” while §9.1 requires reproducibility for `[OBS]` to `[NUM]`. Replacement: §§8.1/9.1/12, protocol and numerical scope determine the claim kind; availability and actual repeatability checks are explicit independent fields.

**M13-C06 — Exactness at declared precision.** Original §9.1 permits “exact symbolic engine at declared precision” without distinguishing arithmetic modes. Replacement: §§9.1/12.2, exact algebra and rigorous interval proof are distinguished from ordinary numerical precision, conjecture recognition, and finite testing.

**M13-C07 — Anchor and heading grammar.** Original §3.5 calls `{#...}` a persistent HTML anchor, ties its form to section numbers, and requires a positive heading even for rejected content. Replacement: §3.5, renderer-aware anchors preserved after moves; semantic new anchors; legitimate negative/correction headings; mixed content is not a new truth tag.

**M13-C08 — Consumer fields and closure.** Original §5.1 uses both `Imports to` and `Exports to` for downstream documents. Replacement: §5.1, dependencies, known consumers, and proposed consumers are separate. A module closure has its actual outcome/grade and does not impersonate a theorem-specific RID or settle all administrative follow-ups.

**M13-C09 — Irreversible rejection interpretation.** Original §§7/8/9 treat `[FAIL]` as terminal without a procedure for an erroneous rejection. Replacement: §7, valid refutations remain binding at their scope, revised propositions get successor records, and mistaken rejection decisions can be explicitly corrected without erasing history.

**M13-C10 — Competing qualifier tables and alias mixtures.** Original §§3.2/8.2 duplicate the qualifier registry; §8.4 allows mixed exact/numerical shorthand without a unique claim-grade rule. Replacement: §§3.2/8.2/8.4, one qualifier registry and separate assertions for different evidence types.

**M13-C11 — Automatic freshness and context sufficiency.** Original §6 treats the orientation core as computationally sufficient and requires source versions not to be superseded. Replacement: §§3.3/6, inspect needed technical dependencies and actual claim revisions; deliberately pinned historical versions remain valid citations.

**M13-C12 — Archival finality and historical compression.** Original §8.3 says no further updates are expected for `[ARCHIVE-READY]`; §1 compresses older histories without specifying preserved source access. Replacement: §§1/8.3/13, archival readiness applies to an immutable snapshot, not to future research; full correction history stays recoverable.

---

*END OF DOCUMENT — DSN_METHODOLOGY_v1.3*  
*Active canonical methodology, adopted September 20, 2026. Supersedes v1.2 as the governing reference; scientific claims and existing study files are not automatically changed by methodology adoption.*
