# DSN_METHODOLOGY_v1.2

**Title:** Dense Semantic Notation — Methodology, Grammar, and Canonical Tag Registry  
**Date:** June 2026  
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok  
**Status:** Active canonical reference. All scientific DSN documents in this project derive their formatting rules, tag vocabulary, document architecture, and claim grammar from this file.  
**Supersedes:** `DSN_METHODOLOGY_v1.1`  
**Scope:** This document defines the DSN format completely. It contains no physics results, no simulation data, and no open problems from the research program. It exists solely to specify how scientific DSN documents must be written, structured, and maintained — by humans and by AI systems alike.

---

## 0. Purpose and Design Philosophy

### 0.1 What DSN Is

Dense Semantic Notation is a structured Markdown format for scientific records in which:

- every claim-block carries an explicit proof-status tag,
- every imported claim declares its source, version, and scope,
- every open problem is tracked as a structured ledger entry with sub-item resolution,
- version history is preserved permanently but demoted to an appendix,
- the document architecture is fixed so that any reader — human or AI — can locate the current canonical state, open frontier, and scope guards in a predictable position without reading the full document.

DSN is designed to serve simultaneously as a working scientific record, an AI context pack, and a provenance log. It achieves this by giving each purpose a dedicated section in a fixed architecture — not by making one section serve all three purposes.

### 0.2 What DSN Is Not

DSN is not a free-form lab notebook, a narrative report, or a scratch-work file. Exploratory sessions and draft derivations belong in working notes. Results graduate into the DSN ledger only when they carry an assignable proof-status tag.

### 0.3 The Single-File Principle

This project uses one methodology file (this document) and one dedicated scientific DSN per study branch. All tag registries, grammar rules, OPEN entry formats, and structural templates are consolidated here. Scientific DSN documents reference this file; they do not redefine its contents.

### 0.4 Design Priorities, In Order

1. **Epistemic honesty.** Every claim carries its actual proof status. Overclaiming is a structural error.
2. **Current-state legibility.** The canonical present state of a study is reachable in the first screenful.
3. **Provenance preservation.** No result, correction, or retraction is silently overwritten.
4. **AI-context efficiency.** The AI Context Core (§6) is extractable and sufficient for a computational session without loading the full document.
5. **Human maintainability.** The fixed architecture and tag vocabulary are consistent enough that a collaborator can update a document without reading this entire methodology first.

---

## 1. Canonical Document Architecture

Every scientific DSN document follows this section order. Section titles may be adapted to the study; section positions may not be changed.

```
§0   Header Block
§1   Current Canonical State              ← AI Context Core begins
§2   Active Frontier / OPEN Registry      ← AI Context Core
§3   Scope Guards                         ← AI Context Core
§4   Layer Routing                        ← AI Context Core ends
§5   High-Risk Claims Ledger
§6   Main Scientific Ledger
§7   Import Ledger
§8   Artifact and Script Registry
§9   Collaboration and Provenance
     Appendix A — Version History
     Appendix B — Retired and Rejected Claims
```

### §0 — Header Block

Required fields, in this order:

```md
# [STUDY_ID]_DSN_v[VERSION]

**Title:** [full title]
**Date:** [Month YYYY]
**Scope:** [one-sentence scope declaration]
**Supersedes:** [previous version filename]
**Companion documents:** [directly linked DSN files, if any]
**DSN Methodology:** DSN_METHODOLOGY_v1.2
**Status summary:** [2–4 sentences: what is settled, what is active, what remains open]
```

The status summary is the first thing any reader encounters. It must reflect actual current state — not a changelog entry, not aspirational claims.

### §1 — Current Canonical State

A compressed, fully-tagged account of everything settled in the study. Written in dense prose or structured bullet form. Every claim-block carries its tag. Cross-references to §6 are permitted; narrative derivation is not.

Target length: 200–400 words. If it exceeds 500 words, it is absorbing material that belongs in §6.

### §2 — Active Frontier / OPEN Registry

All unresolved problems as structured ledger entries (§5 of this document). Closed problems appear only as one-line closed references.

### §3 — Scope Guards

A numbered list of hard epistemic boundaries. Each guard states what is forbidden.

```md
**[SG-N]** [Prohibition.]  
Violation: [consequence]
```

Scope guards also appear as inline callouts in governed sections; see §2.1 of this document.

### §4 — Layer Routing

The explicit map from scientific layer to canonical objects and tools for the study. Names the bridge theorem required for each cross-layer claim.

<!-- AI_CONTEXT_CORE_END -->

### §5 — High-Risk Claims Ledger

Compact table of results correct within scope but prone to over-generalization.

```md
| Claim | Valid form | Forbidden overclaim | Scope section |
|---|---|---|---|
```

### §6 — Main Scientific Ledger

Full technical content: definitions, theorems, derivations, numerical results, simulation invariants, policy characterizations. Numbered subsections with status-tagged headings (§3.5).

### §7 — Import Ledger

All claims imported from other DSN documents, in structured list format (§4.3). One entry per imported claim, collected here for dependency tracking and demotion propagation.

### §8 — Artifact and Script Registry

All computational artifacts with role descriptions and status tags, in structured list format (§10.2).

### §9 — Collaboration and Provenance

Named contributors, roles, canonical archive reference (Zenodo DOI or equivalent), and a table of contributed insights with provenance notes and tags.

### Appendix A — Version History

One subsection per version using the micro-format:

```md
### vX.Y — [Month YYYY]
- **§X.Y [tag]:** [what changed and why]
```

Only the two most recent versions need full bullet lists. Earlier versions collapse to one sentence.

### Appendix B — Retired and Rejected Claims

Permanent record; entries are never deleted.

```md
**[RETRACTED | RID: ID]** [Original claim.] Reason: [reason.] Replaced by: [pointer.] Version: vX.Y.
**[SUPERSEDED | RID: ID]** [Original claim.] Replaced by: [pointer.] Version: vX.Y.
**[FAIL | RID: ID]** [Hypothesis or route.] Reason: [why it fails.] Closed: vX.Y.
```

---

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

## 3. Claim Format

### 3.1 Claim-Blocks

A **claim-block** is the smallest unit of text that asserts a scientific result. It may be a single sentence, a theorem statement with closely related supporting sentences that share the same proof status, an equation with its caption, a table row, or a bullet point. Connective prose, mathematical setup, and derivation steps that do not assert a result do not require tags.

**Every claim-block must open with its proof-status tag.** If a paragraph contains sentences at different proof-status levels, split it into separate claim-blocks.

**Example — correct:**
```md
`[ALG]` In the p=6 primitive frame, the six-step cubic coefficient is
$$\mu_6 = -\tfrac{1}{2} - i\tfrac{2\sqrt{3}}{3}.$$
This coefficient controls the leading radial sink and nonlinear phase shear.
```

**Example — incorrect (second claim untagged):**
```md
`[ALG]` The cubic coefficient is $\mu_6 = -\tfrac{1}{2} - i\tfrac{2\sqrt{3}}{3}$.
The asymptotic backbone coefficient is $47/54$.
```
The second sentence is a separate claim at a potentially different status and must be independently tagged.

### 3.2 Scope Qualifiers

Scope qualifiers narrow the domain of validity of a truth-status tag. They follow the truth-status tag on the same line, written in plain brackets (not backticks) to visually distinguish them from truth-status tags. Use the canonical shorthand keys below.

**Canonical shorthand keys:**

| Key | Full meaning |
|---|---|
| `[conv: NAME]` | result depends on the named normalization or gauge convention |
| `[family: DESC]` | result is exact within the stated parameter family |
| `[scope: DESC]` | result holds within stated boundaries; generalization not claimed |
| `[horizon: PARAMS]` | result applies only at named parameter values |
| `[bridge-required]` | ready for export but needs a bridge theorem before use in another layer |
| `[obs-fit]` | from observable fitting; does not certify primitive or normalized-layer claims |
| `[import: SOURCE §X \| RID]` | derived in another DSN document; source and RID required |

**Example:**
```md
`[ALG]` [conv: Lie strict-kernel] [horizon: p=6]
$$c_\theta^{(6)} = -\tfrac{119\sqrt{3}}{648}.$$
```

```md
`[ALG]` [family: p=5,6,7]
The finite one-step ledger is sealed.
```

Plain brackets are chosen over backtick-code format for qualifiers because: (1) they are visually subordinate to the primary backtick truth-status tag, making the tag hierarchy immediately legible; (2) they are shorter; (3) they remain trivially parseable by regex.

### 3.3 Imported Claims

An imported claim must declare its source using the `[import:]` qualifier, and the `Depends on:` line is mandatory. The claim must also appear in the Import Ledger (§7 of the scientific DSN).

```md
`[ALG]` [import: RTG_DYADIC_DSN_v5.4.16 §9.11b | DYAD-ALG-LIE-GAUGE-CANONICAL]
$$\tau = 2\sqrt{3}/3.$$
Depends on: Lie strict-kernel gauge convention fixed in source document. See §7.
```

### 3.4 The `[RESULT]` Tag — Mandatory Pairing

`[RESULT]` must always be paired with a truth-status tag reflecting the weakest premise in the derivation chain.

```md
`[RESULT]` `[from: HEUR]`
The multistar axiom controls the macroscopic fate of the simulation.
Depends on: §6.15 [HEUR], §6.18 [NUM strong].
```

A bare `[RESULT]` without a paired truth-status tag is malformed.

### 3.5 Section Heading Tags and Persistent Anchors

Each subsection heading in §6 carries a primary status tag as a suffix, plus a **persistent HTML anchor** that never changes regardless of tag promotion or demotion.

```md
### §6.3 Primary Radial Observable `[ALG]` {#sec-6-3-radial}
```

The anchor `{#sec-6-3-radial}` is the stable navigational identity of the section. External links and cross-references use the anchor ID, not the section number or tag text, so that promoting `[HYP]` to `[ALG]` does not break any existing references.

**Anchor naming convention:** `{#sec-[MAJOR]-[MINOR]-[SLUG]}` where SLUG is a short, lowercase, hyphenated description of the content — not the tag. Tags change; slugs do not.

When a subsection contains claim-blocks at multiple proof-status levels, the heading carries the **primary positive status** of the section's main result, followed by `/ mixed`:

```md
### §6.12 OPEN 9 Lattice Channels `[ALG candidate / mixed]` {#sec-6-12-open9-lattice}
```

The heading tag is a navigation aid. Internal claim-block tags are authoritative.

**Prohibited:** `[FAIL]` or `[COR]` as the sole heading tag. These appear inside the section as claim-block tags; the heading reflects positive content.

### 3.6 Corrections and Retractions

When a prior claim is corrected or retracted, the correction is made in-place using `[COR]`, and the original is moved to Appendix B.

```md
`[COR]` Prior wording stated X. Correct statement: Y. See Appendix B, RID: [original-RID].
```

Do not silently overwrite. The audit trail is permanent.

---

## 4. Stable Identifiers

### 4.1 Purpose

Section numbers are human-readable but shift under reorganization. Stable result IDs (RIDs) provide machine-stable identity for cross-document imports, major theorems, OPEN problems, and artifacts.

### 4.2 Format

```
[STUDY_PREFIX]-[CATEGORY]-[SHORT_DESCRIPTION]
```

Study prefixes:

| Prefix | Study |
|---|---|
| `DYAD` | RTG Dyadic |
| `TRIAD` | RTG Triadic |
| `GEN` | RTG Genesis |
| `TDRG` | TDR-G Discrete Relational Genesis |

Category codes:

| Code | Category |
|---|---|
| `THM` | Theorem or exact identity |
| `ALG` | Algebraic result or exact constant |
| `OPEN` | Open problem |
| `ART` | Artifact or script |
| `DEF` | Definition or axiom |
| `FAIL` | Rejected hypothesis |

Example RIDs:
```
DYAD-ALG-C21-6STEP-CUBIC
DYAD-OPEN-P-RESONANCE
TDRG-OPEN-MULTISTAR-AXIOM
GEN-THM-BLOCK-DIAGONAL-NOGO
TRIAD-ALG-K3-QUARTIC-PUMP
TDRG-ART-MOTIF-V5-SLOT
```

### 4.3 Import Ledger Entry Format

The Import Ledger (§7 of scientific DSN documents) uses structured list entries, one per imported claim:

```md
- [RID: SOURCE-RID] :: [brief claim description] :: [source doc + §] :: [local use] :: [scope inherited]
```

Example:
```md
- [RID: DYAD-ALG-LIE-GAUGE-CANONICAL] :: τ = 2√3/3 :: RTG_DYADIC_DSN_v5.4.16 §9.11b :: Genesis birth scaling :: p=6, K=1, Lie strict-kernel gauge
```

### 4.4 Where RIDs Appear

RIDs appear:
- on the claim-block opening line: `[RID: DYAD-ALG-C21-6STEP-CUBIC]`
- in Appendix B retired-claim entries
- in Import Ledger entries (§4.3)
- in OPEN entry headers and sub-items (§5)
- in Artifact Registry entries

RIDs are optional for internal claims not referenced elsewhere. They are **mandatory** for any claim that appears in another document's Import Ledger.

---

## 5. OPEN Problem Entry Format

### 5.1 Full Entry

```md
---
**OPEN [N] — [short title]** [RID: STUDY-OPEN-SHORTNAME]

Status: ACTIVE | PARTIAL | CLOSED  
Owner branch: [DSN document name]  
Imports to: [downstream DSN documents that use results from this problem]  
Exports to: [documents that have already imported partial results]

Closed sub-items:
- [description] :: `[TAG]` ✓ [RID: ...]

Active sub-items:
- [description] :: `[OPEN]`

Retracted sub-items:
- [description] :: `[RETRACTED]` — [reason]. See Appendix B, RID: [...]

Next required artifact:
- [description]

Dependencies:
- [other OPENs or settled results, with RIDs]
---
```

Fields that do not apply may be omitted. A simple closed problem collapses to:

```md
**OPEN [N] — [title]** [RID: ...] :: `[TAG]` ✓ CLOSED — [one-sentence closure].
```

### 5.2 Closure Protocol

1. Set `Status: CLOSED`.
2. Move to a "Closed" subsection at the end of §2.
3. Record in Appendix A under the closing version.
4. Update §1 to reflect the new settled result.
5. Update all documents in `Exports to`.

### 5.3 Partial Closure

Set `Status: PARTIAL` when a subset of sub-items is closed. Do not mark `CLOSED` until all active sub-items are resolved.

---

## 6. AI Context Core

### 6.1 Definition and Boundary

The AI Context Core is the minimum block of a scientific DSN document sufficient for a productive computational session. It spans exactly:

- §1 Current Canonical State
- §2 Active Frontier / OPEN Registry
- §3 Scope Guards
- §4 Layer Routing

The end of §4 is marked by the HTML comment `<!-- AI_CONTEXT_CORE_END -->` inserted as the last line of §4 content, before §5 begins. This marker is invisible in rendered Markdown and allows automated extraction scripts to slice the context core without parsing section headings.

These four sections should not collectively exceed 800 lines in a mature document. If they do, §1 or §2 has absorbed material that belongs in §6.

### 6.2 Instructions for AI Systems Reading a Scientific DSN

**1. Read §1 first.** This is the canonical present state. `[ALG]` and `[THM]` results are established. `[HYP]` and `[HEUR]` results are working assumptions. `[OPEN]` items are the active frontier. Appendix A is provenance — do not use it to determine current status.

**2. Check §3 (Scope Guards) before generating any claim.** Scope guards are hard boundaries. Common violations: importing across layers without a bridge theorem; treating `[conv: ...]` results as gauge-universal; treating `[horizon: ...]` results as universal.

**3. Read §4 (Layer Routing) before reasoning across layers.** An observable-layer result does not certify a primitive-layer claim. The routing table defines which objects belong to which layer and which bridges exist.

**4. Use §2 (OPEN Registry) to understand what is not settled.** "Active sub-items" and "Next required artifact" define the current work target. Do not treat active sub-items as settled.

**5. Assign a tag before stating a new result.** The tag is not annotation — it is part of the claim. A result without a tag is epistemically untagged and must not be registered in the ledger.

**6. Do not promote a result without stating the promotion criterion** from §9.1. State the met condition explicitly.

**7. Check §5 (High-Risk Claims Ledger) before registering a result of a structurally familiar type.** Explicitly state which valid form you are asserting and which overclaim you are avoiding.

**8. Do not silently overwrite.** Use `[COR]`; originals go to Appendix B.

**9. For imported claims, verify the Import Ledger (§7).** Confirm scope and that the source version has not been superseded.

**10. Use anchor IDs for cross-references, not section numbers.** Section numbers shift; `{#sec-6-3-radial}`-style anchors do not.

### 6.3 Instructions for AI Systems Writing or Updating a Scientific DSN

**1. New results go in §6.** Update §1 only if the result changes the canonical state summary.

**2. Resolved OPEN problems follow the closure protocol (§5.2).** Update the entry, §1, Appendix A, and exporting documents.

**3. Corrections use `[COR]` in-place; originals go to Appendix B.**

**4. Version metadata goes to Appendix A only.** The header status summary may be updated; details go in the appendix.

**5. Do not introduce unregistered tags.** Use the local alias protocol (§8.4) for compound shorthands.

**6. Assign a RID when registering a result that may be imported by another document.**

**7. Update the Import Ledger (§7) when using a result from another document.**

**8. Use the `{#sec-...}` anchor format on all new §6 subsection headings.**

---

## 7. Demotion Protocol

When a claim is demoted:

1. Mark the current claim `[COR]` in §6 and state the new (lower) status.
2. Move the original to Appendix B.
3. Update §1 if canonical state changes.
4. For every document in the claim's `Exports to` field, communicate the demotion and update their Import Ledgers.
5. Record in Appendix A under the demotion version.

Demotion to `[FAIL]` follows the same protocol. `[FAIL]` is terminal: not promotable. A corrected hypothesis may be registered as a new `[HYP]` with a new RID and corrected scope.

---

## 8. Tag Registry — Canonical Definitions

All tags used in scientific DSN documents are defined here. No tag may be used that does not appear in this registry or in the document's Local Alias table.

### 8.1 Truth-Status Tags

| Tag | Definition |
|---|---|
| `[DEF]` | Definition or axiom. Not subject to proof; subject to revision or supersession. |
| `[THM]` | Proven theorem or exact identity. Proof is complete and convention-independent. |
| `[THM-ALG via IA]` | Theorem-grade closure carried by an interval arithmetic certificate. Certificate must be archived and reproducible. |
| `[ALG]` | Exact algebraic derivation or exact symbolic constant. Carry `[conv: ...]` if convention-dependent. |
| `[ALG via IA]` | Exact algebraic statement proven by interval arithmetic. Certificate archived and reproducible. |
| `[ALG candidate]` | Exact-form candidate supported by strong structural or numerical evidence; not yet proven. |
| `[ALG structure]` | Mechanism identified algebraically, but coefficients open or theorem-grade closure incomplete. |
| `[ENG]` | Validated engineering infrastructure: pipeline, audit script, certification scaffold. Not on the theorem-promotion axis. |
| `[NUM]` | Numerical result from a limited campaign. Reproducibility not yet established. |
| `[NUM strong]` | High-precision numerical result with cross-seed, cross-method, or multi-run agreement. |
| `[OBS]` | Empirical observation from a limited campaign; not yet systematically characterized. |
| `[HEUR]` | Plausible interpretation or heuristic argument. Not theorem-grade. |
| `[HEUR strong]` | Strongly supported interpretation across multiple independent checks; not closed. |
| `[HYP]` | Working hypothesis under active investigation. No confirmation yet. |
| `[OPEN]` | Unresolved problem. Used in OPEN Registry entries. |
| `[FAIL]` | Rejected hypothesis, route, or claim. Permanent. Not promotable. |

### 8.2 Scope-Status Qualifiers

Qualifiers follow the truth-status tag in plain brackets. See §3.2 for the canonical shorthand keys and their full meanings.

The shorthand keys and their expansions:

| Shorthand | Full meaning |
|---|---|
| `[conv: NAME]` | Result depends on the named normalization or gauge convention |
| `[family: DESC]` | Result is exact within the stated parameter family |
| `[scope: DESC]` | Result holds within stated boundaries; generalization not claimed |
| `[horizon: PARAMS]` | Result applies only at named parameter values |
| `[bridge-required]` | Needs a bridge theorem before use in another layer or branch |
| `[obs-fit]` | From observable fitting; does not certify primitive or normalized-layer claims |
| `[import: SOURCE §X \| RID]` | Derived in another DSN document; source and RID required |

### 8.3 Workflow-Status Tags

| Tag | Meaning |
|---|---|
| `[RESULT]` | Derived synthesis or program-level consequence. **Must be paired with a truth-status tag:** `[RESULT]` `[from: TAG]`. |
| `[COR]` | Correction to prior wording, status, or logic. Original goes to Appendix B. |
| `[RETRACTED]` | Claim formally withdrawn. Reason and replacement stated. Permanent. |
| `[SUPERSEDED]` | Claim replaced by stronger or corrected result. Pointer required. |
| `[ARCHIVE-READY]` | Settled and ready for external archival. No further updates expected. |

### 8.4 Local Alias Protocol

A scientific DSN may define local aliases under `## Local Tag Aliases` immediately after the header block.

Rules:
1. Each alias maps to canonical tags plus qualifiers from this registry.
2. A local alias may not redefine or override a canonical tag.
3. Local aliases do not propagate to other DSN documents.

Example:
```md
## Local Tag Aliases

| Local alias | Expands to | Used for |
|---|---|---|
| `[ALG/NUM]` | `[ALG]` co-certified with `[NUM]` | exact derivation cross-verified numerically |
| `[ENG/ALG]` | `[ENG]` with `[ALG]`-grade audit | implementation verified against exact reference |
```

---

## 9. Promotion and Demotion Criteria

### 9.1 Promotion Table

| From | To | Required |
|---|---|---|
| `[OBS]` | `[NUM]` | Systematic measurement protocol; reproducibility established. |
| `[NUM]` | `[NUM strong]` | Cross-seed / cross-method / multi-run agreement. |
| `[NUM strong]` | `[ALG candidate]` | Exact-form conjecture formed; PSLQ, invariant pattern, or symbolic route identified. |
| `[ALG candidate]` | `[ALG]` | Exact derivation over declared algebraic field, or exact symbolic engine at declared precision. |
| `[ALG]` `[conv: ...]` | `[ALG]` (unconditional) | Convention shown canonical or gauge-invariant by theorem. |
| `[ALG]` | `[THM]` | Full proof independent of implementation and convention ambiguity. |
| `[ALG via IA]` | `[THM-ALG via IA]` | IA certificate complete, archived, reproducible. |
| `[HEUR]` | `[ALG structure]` | Structural derivation of mechanism found, even if coefficients remain open. |
| `[HEUR strong]` | `[ALG candidate]` | Exact-form conjecture formed and structurally supported. |
| `[HYP]` | `[HEUR]` | First supporting evidence obtained. |
| `[HYP]` | `[FAIL]` | Definitive refutation; reason stated. |

When proposing a promotion, state which condition is met. A promotion claim without a stated condition is itself `[HYP]`.

### 9.2 Demotion Table

| From | To | Trigger |
|---|---|---|
| `[ALG]` | `[ALG candidate]` | A gap is found in the derivation. |
| `[ALG]` | `[ALG structure]` | Derivation found to be structurally incomplete. |
| `[NUM strong]` | `[NUM]` | Cross-method agreement breaks down. |
| `[HEUR strong]` | `[HEUR]` | A contradicting case is found. |
| Any | `[FAIL]` | Definitive refutation. Terminal. |

All demotions follow the Demotion Protocol in §7.

---

## 10. Grammar and Formatting Rules

### 10.1 Section Numbering

Scientific DSN sections: `§1`, `§6`. Subsections: `§6.3`, `§6.3.1`. Appendices: `Appendix A`. These conventions are fixed.

### 10.2 Ledger and Registry Format

DSN uses two distinct formats depending on use case.

**Tables** are used for: tag registry (§8), promotion/demotion criteria (§9), high-risk claims ledger (§5), collaboration/provenance (§9 of scientific DSN), and local alias declarations. These are genuinely tabular: fixed columns, short rows, horizontal comparison is meaningful.

**Structured lists** with `::` delimiters are used for: the Import Ledger (§7), the Artifact and Script Registry (§8 of scientific DSN), and OPEN sub-item lists. These grow long with the research archive and are better served by the compact list format.

Structured list format:
```md
- [RID: ID] :: [brief description] :: [key attribute] :: [key attribute]
```

Example Import Ledger entry:
```md
- [RID: DYAD-ALG-LIE-GAUGE-CANONICAL] :: τ = 2√3/3 :: RTG_DYADIC_DSN_v5.4.16 §9.11b :: Genesis birth scaling :: p=6 Lie strict-kernel gauge
```

Example Artifact Registry entry:
```md
- [RID: TDRG-ART-GENESIS-MC] :: `genesis_mode_b_mc.py` :: Monte Carlo simulation engine, three-policy architecture :: `[ENG]`
```

The `::` delimiter is chosen for token efficiency and trivial parseability.

### 10.3 LaTeX Formatting

Display equations: `$$...$$`. Inline: `$...$`. Named equations are referenced by anchor ID or section pointer, not by equation number, since equation numbers shift with edits.

### 10.4 Code and Artifact References

Script and file names in backtick format: `` `genesis_mode_b_mc.py` ``. Inline references point to §8 (Artifact Registry) rather than repeating role descriptions.

### 10.5 Blockquote Usage

Blockquotes (`>`) are reserved for exactly two purposes:
- Scope guard callouts: `> **[Local guard SG-N]** ...`
- High-priority editorial warnings requiring visual separation.

Blockquotes must not be used for version history, ordinary prose, or derivation steps.

### 10.6 Boxed Key Results

Results central to the canonical state may use `\boxed{}`. Use at most two or three per document. Boxed results still carry their proof-status tag in surrounding prose.

### 10.7 Changelog Micro-Format

```md
- **§X.Y [tag]:** [what changed and why]
```

Always reference the section and tag. Vague entries are not permitted.

---

## 11. Anti-Patterns Catalogue

| Anti-pattern | Why it fails | Correct practice |
|---|---|---|
| Stating a result without a tag | Creates an untagged claim that later gets promoted by default. | Every claim-block opens with its tag. |
| Using `[ALG]` `[conv: ...]` results as unconditional downstream | Convention-dependent scope propagates. | Carry `[conv: ...]` until a gauge-invariance theorem removes it. |
| Importing across the discrete/continuous boundary without a bridge theorem | Discrete and continuous objects are structurally different; a formula valid in one branch may be category-wrong in the other. | Cross-branch imports require a bridge theorem tagged `[ALG]` or stronger, cited in §7. |
| Treating `[obs-fit]` results as primitive-layer certification | Observable fits are downstream of multiple approximations. | Follow Layer Routing; crossing without a bridge is a scope-guard violation. |
| Writing changelog entries at the top of the document | Dead scroll before current state. | Changelogs belong in Appendix A. Header permits only a 2–4 sentence status summary. |
| Compressing a multi-sub-item OPEN problem into a prose paragraph | Makes heterogeneous proof states illegible. | Use the OPEN entry format from §5. |
| Introducing a tag not in the registry and not declared as a local alias | Cross-document inconsistency; AI systems apply the tag incorrectly elsewhere. | Use the local alias protocol (§8.4) or request a methodology update. |
| Silently overwriting a prior claim | Destroys the audit trail. | Use `[COR]` in-place; original to Appendix B; record in Appendix A. |
| Using Appendix A changelog as authoritative for current status | Changelogs record changes, not current state. | §1 is authoritative. |
| Bare `[RESULT]` without a truth-status pair | `[RESULT]` may summarize weak premises; without a tag it becomes an epistemic loophole. | Always pair: `[RESULT]` `[from: TAG]`. |
| Tagging a section heading `[FAIL]` or `[COR]` as sole tag | Misrepresents the section's positive content. | Use primary positive status; append `/ mixed` if heterogeneous. |
| Using blockquotes for version history or prose | Visually conflates with scope guards. | Blockquotes reserved for scope guards and high-priority warnings only. |
| Cross-document citations by section number only | Section numbers shift under reorganization; citations become stale. | Always cite section number (human-readable) and anchor ID or RID (stable). |
| Using Markdown tables for long growing registries | Token-heavy; pipes and alignment tokenize poorly at scale. | Use `::` structured lists for Import Ledger and Artifact Registry. |

---

## Appendix A — Version History

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

*END OF DOCUMENT — DSN_METHODOLOGY_v1.2*  
*This document is the sole authoritative source for DSN tag definitions, document architecture, claim grammar, stable identifier conventions, and formatting rules for this project. All scientific DSN documents defer to it.*
