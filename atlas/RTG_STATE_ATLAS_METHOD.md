# RTG State Atlas — Method v0.2

**Status:** working method of a derived, NONCANONICAL product. Owner of the method and of the atlas: Claude (atlas owner), under PI (Mustafa) authority. Not a DSN. The method changes by a new version of this file. Versions and their acceptance records are in git (tag `atlas-v<version>`, `records/atlas/`).

## 1. Purpose

The RTG State Atlas is one file that lets an AI session grasp the entire current RTG scope in a single read:
- what exists;
- what is established, at which grade and scope;
- what depends on what;
- what is open and what blocks it;
- where the corpus is inconsistent or has unnoticed links.

The reader is an AI; human readability is secondary.

Priority order of optimization:
1. relational expression (objects, claims and the edges between them);
2. token economy, only after (1) is satisfied.

## 2. Status and authority

- The atlas is **derived and noncanonical**. It is never the source of a claim. Every node cites its owner document and RID. On any conflict the owner DSN wins.
- The atlas owner has **no authority** over any stream. It reports and advises; stream owners decide; the PI holds the final decision.
- An updated owner node in the atlas does not mean that a consumer has adopted that owner edition (§4, rule 10).
- An atlas computation (PASS) does not confer owner adoption.

## 3. Inputs and source snapshot

- **Inputs.** The files in `dsn/` and `noncanonical/` of `rtg-corpus`, each at its governing tag as listed in `BASELINE.md`. For a canonical source this is the latest adopted tag. A noncanonical source is used at the tagged snapshot the PI selected, and its class and status (NONCANONICAL, SESSION, adopted scope) are kept as node metadata; a tag alone does not establish adoption. The DSN Methodology contributes grade and identifier semantics to L0 only.
- **Frozen snapshot.** A build starts by freezing a source manifest (`evidence/atlas/source_manifest_v<version>.json`). For each source it records: owner key, path, edition, class, tag, resolved commit, full SHA-256, and the authority record.
- **Header.** The atlas header carries a compact source table (key, document, edition, tag, class).
- **Changes during a build.** A source that changes after the freeze is a declared divergence, handled in the next refresh. Inputs are never switched halfway through a build.
- **"Unchanged" means equal bytes.** A source is unchanged only if the bytes of the previous build's input equal the bytes of the new tagged input. Where the previous input hash was not retained, the equality is recorded as unverified.

## 4. Content rules

1. **Current scientific state only.** The atlas describes the current scientific state at its frozen source snapshot:
   - definitions;
   - established and conditional claims;
   - operative negative constraints;
   - unresolved scientific interfaces;
   - current evidence limitations.

   It excludes the chronology of edits, reviews, advisory dispositions and notice handling. Obsolete diagnostics are absent from the live atlas; their removal and justification stay in the versioned review record under `records/atlas/`. Source identity, source class and scoped acceptance are kept as metadata, not narrated as release history.
2. **Evidence boundaries are current state.** Statements such as "source-reported", "not rerun", "certificate unavailable" and "conditional use" stay. A retracted assertion is not a theorem of its falsity.
3. **Rejected claims are current state.** FAIL and RETRACTED entries are kept compactly, at their scope, as live constraints ("this route is closed").
4. **One node per object and per claim.** An imported claim is not restated; the consumer gets an edge to the owner's node. A module that is no longer open leaves L3, but the results that closed it stay in L2.
5. **No stream partitioning.** Stream labels (DYAD, GEN, …) mark provenance only, never structure.
6. **No fact is dropped for size.** The size target (≈60–90k tokens) yields to completeness. Wording compression is a separate pass.
7. **Proofs are not summarized.** A claim carries at most a one-line method pointer; full proofs stay in the owner DSN.
8. **Clearly wrong facts.** A fact clearly wrong against the rest of the established corpus is not used as a node. It is recorded as one L5 D-WRONG line (claim, location, conflicting evidence), never silently dropped. Unproved or uncertain facts are included at their stated grade.
9. **Atlas-derived links** (identities, dependencies or equivalences the atlas notices but no owner records) are marked `~` and must be verified before use.
10. **Owner state and consumer pins are separate.** An edge from a consumer to an owner node carries the edition the consumer actually imports. It is joined to the current owner node only through a documented same-claim, same-scope relation. An edge whose target is no longer in the latest owner file is kept, as a typed reference or diagnostic, until owner, claim identity, imported edition and scope have been checked. Absence from the latest file is not by itself grounds for deletion or for repinning.
11. **Identifier types.** These are different kinds of identifier and are never counted as each other:
    - scientific RIDs;
    - artifact RIDs (`-ART-`), cited in `cert` fields, normally not as nodes, but always link-checked;
    - local registry keys (`RER-*`, ER2B-Cxx, FMS session labels);
    - Methodology section keys;
    - representation-profile identifiers.
12. **Language:** English. Words such as "history", "resolved" or "return" keep their mathematical meanings. Wording checks only raise review warnings; they never delete anything automatically.

## 5. Output structure

```
L0 KEY        grades, qualifiers, record syntax, edge operators, global scope rules
L1 OBJECTS    every mathematical object defined once; aliases (≡); symbol collisions (⊥)
L2 CLAIMS     one record per claim, grouped by topic (not by stream)
L3 FRONTIER   OPEN items in dependency order: what each blocks and is blocked by
L4 CONSTRAINTS scope guards and firewalls as rules; exportability; required bridges
L5 DIAGNOSTICS current inconsistencies, gaps, collisions, pin mismatches, unnoticed links
```

A short HEADLINE list of the most consequential L5 items comes directly after L0, so a reader sees critical problems first; the full L5 stays in each domain. The body is grouped in seven subject domains: D1 foundations, governance and representation · D2 dyad core and resonance arithmetic · D3 recognition, return and memory · D4a triad, primitive K₃/K₄ and model families · D4b geometry, metric, network and UV · D5 discrete branch and graph diagnostics · D6 historical provenance.

Record syntax:

```
ID GRADE | statement | sc: scope | if: premises | <dep | >used-by | ¬ not-claimed | cert | @owner§
```

- `ID` = owner RID; `*STREAM:slug` when the owner gives no RID (itself an L5 D-RID item; the atlas never invents an owner RID).
- grades: THM ALG DEF CAND HYP RES NUM HEUR INTERP OPEN FAIL RET CONV; qualifiers `·c` conditional, `·s` structural, `·dx` diagnostic only, `nc` node from a noncanonical source.
- edges: `<` depends on · `>` consumed by · `≡` same object · `⊥` symbol collision · `!` tension/conflict · `~` atlas-derived link.
- `@owner§` may carry the consumer's actual import pin (`@GEN§7 [DYAD v6.4.13]`) when it differs from the source table.
- formulas in LaTeX-like plain text; exact values kept exactly.

L5 IDs are stable keys (`STREAM.<id>`). A deleted diagnostic's key is never reused. HEADLINE numbering is a display order only.

## 6. Diagnostic classes (L5)

| Class | Meaning |
|---|---|
| D-RID | claim without RID; duplicate RID; RID heading two entries; cited RID that does not resolve at its owner (phantom) |
| D-PROOF | one of three distinct states, always named: (a) the proof argument is missing; (b) the certificate or artifact is not available; (c) the check was not rerun in the cited review. (b) and (c) do not by themselves withdraw an adopted result. |
| D-GRADE | an omitted premise; an unjustified unconditional application of a conditional result; or the same claim at different grades. A complete proof of $H\Rightarrow P$ under an explicit hypothesis $H$ is a valid THM even if $H$ is HYP or OPEN. RESULT keeps its explicit `from` status. Grades are not propagated by RID prefix or by a total order of tags. |
| D-CONV | sign, normalization or convention conflict between sites |
| D-SYM | symbol collision or undefined symbol |
| D-PIN | a demonstrated content or scope mismatch between a consumer's pin and its use; an unresolved identity; an incorrect representation of a present use. An older, intentional pin that is still valid is not a defect; age alone only prompts inspection. |
| D-STALE | an entry whose stated status contradicts its own body or the owner's current statement |
| D-SCOPE | scope label missing where two sites differ only by scope |
| D-LINK | an unrecorded identity, equivalence or dependency between claims (often cross-stream) |
| D-WRONG | a fact excluded as clearly wrong (rule 4.8) |

Exact facts the atlas recomputed are placed at their content layer with a scoped evidence pointer (`atlas-checked: …`), not kept as a list of passed checks.

## 7. Process

**Build.** Each source is read and transcribed into the record format. Its slice is merged into the master atlas: objects are unified and imports collapse to owner nodes.

**Refresh (impact-based).**
- **Triggers:** a new governing tag of a source, a schema change or a change of diagnostic semantics.
- **Changed sources:** a changed source is re-extracted in full.
- **Affected records:** every edge into a changed source, and every diagnostic whose truth or meaning depends on changed inputs or changed semantics, is validated against the new snapshot. Unchanged owners are not reread unless affected.
- **L5 dispositions:** each L5 item receives a current-snapshot disposition (retained, reworded, deleted, new). Text about unchanged sources is carried forward only when its dependencies and governing semantics are also unchanged. Dispositions and their reasons are recorded under `records/atlas/`.
- **Certificates:** scientific certificates are not rerun for an atlas refresh.

**Checks** (`tools/atlas_check.py`; report-only, with PASS, FAIL and UNVERIFIED kept separate):
- **sources:** the source table matches the frozen manifest and `BASELINE.md`;
- **typed coverage:** each live owner item of a re-extracted source maps to a node, an owner-approved alias or shared node, a `cert` reference, or a justified out-of-scope disposition. A RID that appears only in L5, in the source table or in an unrelated `cert` field does not cover its claim;
- **owner-resolved links:** each cited RID resolves to a declaration in its owner's file at the snapshot. Known phantom RIDs documented in L5 are reported separately as documented unresolved references, never as resolved;
- **wording:** history and process phrases are listed as review warnings.

Unparsed or unchecked items are not counted as PASS. Content fidelity remains a matter for the change-focused review.

**Advisories (Pass 2).** For each stream, the atlas owner issues one batched advisory to its owners from the accepted atlas snapshot and the checked owner sources:
- one row per finding (class, location, observation, suggested fix, editorial or scientific);
- the stream owner records a disposition for each row;
- accepted fixes go through the stream's own release cycle; the atlas never edits a DSN and is refreshed from the adopted result.

Advisories and dispositions live under `records/<study>/` and are never mentioned in the atlas.

**Acceptance.** An atlas version is accepted by the PI after a change-focused review. A short acceptance record (`records/atlas/`) pins the atlas, method and source-manifest identities. The PI creates the annotated tag `atlas-v<version>`. The tag identifies a noncanonical derived artifact; it adopts no owner science.
