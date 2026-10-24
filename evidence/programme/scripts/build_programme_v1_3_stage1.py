#!/usr/bin/env python3
"""Programme Overview v1.3, stage 1: corrected intermediate (a build stage, not an edition).

Applies the accepted rows of the atlas advisory records/programme/ATLAS_ADVISORY_PROGRAMME_v1_2.md
(PA-01..06, PB-07, PB-09, PB-10, PC-12, PC-13; PI decisions of 23 Oct 2026 in its §5) to the adopted
Programme v1.2 file. Stage 2 (layout-only compaction: Appendices A-C, header history) is a separate build.

Rules
- every edit is a section replacement or an exact-once string replacement; the old text is taken from
  the base at run time by its boundaries and hashed into the log, so the log reconstructs the base;
- no OPEN-P status, maturity grade or scope-guard text changes (checked by check_programme_v1_3_stage1.py);
- the Programme restates no owner science: §6 rows carry edition, tag, custody and interfaces, and point to
  the owner's own status summary.

usage (repository root): python -I evidence/programme/scripts/build_programme_v1_3_stage1.py BASE OUT EDITLOG_JSON
  BASE = `git show programme-v1.2:dsn/RTG_PROGRAMME_OVERVIEW.md`
"""
import hashlib, json, sys

BASE_SHA = "4207da05dca24256e7bc528cb9814f848838bcd98e3d01222fb2a633ec9fd359"

def sha(s): return hashlib.sha256(s.encode("utf-8") if isinstance(s, str) else s).hexdigest()

# ----------------------------------------------------------------------------------------------
# New texts
# ----------------------------------------------------------------------------------------------

HEADER = """# RTG_PROGRAMME_OVERVIEW_v1.3

**Title:** Relational Time Geometry — Programme Overview and Study Hierarchy
**Date:** 23 October 2026
**Scope:** Inventory, ownership, branch/layer architecture, programme OPENs and scope guards, synchronized to the governing editions of the corpus; pass-two revision of the adopted v1.2 architecture.
**Document class:** Programme overview, under DSN Methodology v1.4 §0.5.
**Document status:** DRAFT — v1.3 candidate (stage 1: corrections; stage 2: compaction); not adopted. `programme-v1.2` governs until adoption.
**Supersedes:** `RTG_PROGRAMME_OVERVIEW_v1.2` (tag `programme-v1.2`, SHA-256 `4207da05dca24256e7bc528cb9814f848838bcd98e3d01222fb2a633ec9fd359`, adopted 20 September 2026).
**Repository:** `MustafaAksu/rtg-corpus`, `main`. A study's governing edition is its latest adopted tag with its release record (Methodology v1.4 §13.9); `BASELINE.md` lists the governing editions with their SHA-256; `CONVENTIONS.md` gives the working rules. Project copies mirror `main`.
**Companion documents:** the governing editions in §6.1 (by tag). The list is not a substitute for claim-level imports; each consumer's own pins are in its Import Ledger (§7.2 records them where they differ).
**DSN Methodology:** v1.4 (tag `methodology-v1.4`); v1.2 was adopted under v1.3.
**Status summary:** Two physical research branches, continuous and discrete, with shared foundational, historical and diagnostic documents whose contents remain branch-typed. The inventory (§6.1) records fifteen canonical document homes in `dsn/`, including the RRF representation registry adopted as a working standard, three noncanonical registries and studies in `noncanonical/`, and one derived map (the State Atlas) that is never a source. All five programme-level scientific OPEN records (P0, P1, P2A, P2B, P3) remain ACTIVE; no maturity grade, scope guard or scientific status is changed by this edition. No physical bridge is certified.
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok — inherited authorship; separate approval by other inherited authors is not inferred.
**Revision editor (v1.3):** Claude (atlas owner), by PI decision of 23 October 2026; change-focused review by ChatGPT.
**Release record:** `records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md`. The v1.2 release and change records are not in the repository (recorded as missing there); v1.2's header records the PI's adoption of 20 September 2026.
**Archive reference:** rtgtheory.org · Zenodo DOI 10.5281/zenodo.17568897 — inherited programme locator, not a claim that this release has been deposited there.
"""

S0_1 = """### 0.1 Present orientation and revision boundary

The governing Methodology is v1.4 (tag `methodology-v1.4`). Programme v1.3 is the pass-two synchronization of the adopted v1.2 architecture: the inventory, the interface register, the owner pointers and the maintenance record are brought to the governing editions of 23 October 2026; the two-branch architecture, maturity semantics, OPEN-P criteria and scope guards of v1.2 are unchanged. The source of every edition is the repository: a study's governing edition is its latest adopted tag with its release record; `BASELINE.md` is the machine-readable list.

The inventory (§6.1) recognizes fifteen canonical document homes in `dsn/` — Methodology, Programme Overview, Ontological Foundations, the RRF representation registry (adopted working standard), the two historical ledgers, Number Genesis as the foundational/technical common home, six continuous technical studies (Dyadic, Triadic, Genesis, OPEN M, RECOG, DZT), one discrete owner (TDR-G) and AZ as shared diagnostic infrastructure — plus three noncanonical documents (RER, FMS, ER-2B) and one derived map (the State Atlas). These are document homes and classes, not physical branches. Number Genesis keeps its continuous and discrete realization sectors distinct; AZ keeps its continuous references and discrete graph diagnostics distinct. Their shared location supplies no physical identification between substrates. A noncanonical document is a working record that no owner has adopted as science: it may be cited for what it records, never as the source of a claim. The derived map is read, not cited; on any conflict the owner DSN wins.

Owner closures that postdate v1.2 are indexed in §6 by edition and pointer; this overview does not re-certify them and does not restate them. The local continuous generator remains selected rather than physically derived; discrete rule/policy selection, the physical cross-branch bridge, primitive-object selection and metric/Regge/coupling completion remain research questions (§5).

**For an AI reader.** Start with `BASELINE.md` (editions and hashes), `CONVENTIONS.md` and Methodology v1.4 (rules), then the owner DSN of the question at its tag. `atlas/RTG_STATE_ATLAS.md` is a noncanonical map of the current state with its own method and limits; it points into the owners and is never the source of a claim.
"""

S4_TABLE_TAIL = """| Study | Previous or owner-declared maturity record | v1.3 |
|---|---|---|
| Dyadic | B in Programme v1.1 | Record retained; no owner header at `dyad-v6.4.22` declares an A–D grade; scientific reconciliation of the grade not performed by the Programme |
| Triadic | B/C locally in Programme v1.1 | Record retained; scope of B versus local bridge support unresolved |
| Genesis | A/B in Programme v1.1 | Record retained; scope of the mixed assignment unresolved |
| TDR-G | B in Programme v1.1 | Record retained; policy/limit scope remains visible |
| DZT | A in owner header (v0.8) | Owner record; no promotion |
| RECOG | A requested in the v0.3 header and stream memo (September 2026) | Record retained; no grade requested or declared in the v0.3.23 header; no grade issued here |
| OPEN M | B conditionality in the v0.6 summary | Record retained; v0.7.1 declares no A–D grade |
| AZ | A retained in owner header (v0.6) | Owner record; its own diagnostic gate is not a universal programme maturity rule |
| Number Genesis | No A–D assignment in the owner | No grade assigned |
| RRF, RER, FMS, ER-2B, Atlas | standard / registry / ledger / study / map | No technical-model grade; not candidates for one |
| Methodology, Programme, OFN, historical ledgers | Governance/foundational/historical roles | No automatic technical-model grade |
"""

S5_P0_OWNER = """**Owner study:** Programme Overview for coordination; OFN (admissibility and model-selection criteria, OFN v0.10 §§5, 9) and RRF (representation and interface contracts, RRF v0.8.4) supply the criteria; technical owners supply results.  """
S5_P2B_NEXT = """**Next required decision:** the criterion home is OFN v0.10, OPEN-OFN-3B (`RTG-OFN-OPEN-PRIMACY-3B`: admissible triad-to-dyad invariant reduction; row agreement on $c=0$ explicitly insufficient). No technical construction owner is assigned; the Programme assigns none."""
S5_P3_DEPS = """**Dependencies:** the source-specific UV, metric and gluing requirements. OPEN M v0.7.1 (tag `uvm-v0.7.1`) supplies no physical UV blocks and records no certified calibration deficit (its R15/R16 reinterpretation; see OPEN M §6 and Appendix B); OPEN M completion is not by itself Regge closure. Preparatory Regge definitions and consistency studies need not wait for every UV computation; their final physical coupling use does."""

S6_1 = """### 6.1 Navigation tiers and source inventory

`[DEF]` Tier numbers are navigation groups, not proof arrows or physical rankings. The labels 0–5 are retained: 0 programme; 1 methodology; 2 foundational/historical/common-home ledgers; 3 continuous technical studies; 4 discrete technical studies; 5 shared infrastructure, standards and separately proposed bridge programmes. Class says what kind of document it is: canonical (adopted owner science or governance), adopted working standard, noncanonical (working record, not owner-adopted science), derived (a map built from the others). The placement additions and clarifications of v1.2 are retained; v1.3 adds the RRF, RER, FMS, ER-2B and Atlas rows and the class column.

**Governing edition, adoption state and ownership are distinct.** The table lists the governing edition of each document by its tag; `BASELINE.md` carries the SHA-256 values and is the authority if this table and it ever disagree. Consumers keep their own import pins; §7.2 records them where they differ from the governing edition. Filenames in `dsn/`, `noncanonical/` and `atlas/` are fixed (CONVENTIONS); versions live in tags, not in names.

| Key | Document (fixed path) | Governing edition | Tag | Class | Tier | Role / physical scope |
|---|---|---|---|---|---:|---|
| METH | `dsn/DSN_METHODOLOGY.md` | v1.4 | `methodology-v1.4` | canonical governance | 1 | Adopted grammar, profiles, evidence and revision rules |
| PROG | `dsn/RTG_PROGRAMME_OVERVIEW.md` | v1.3 (this edition; v1.2 governs until adoption) | programme-v1.3, created on adoption | canonical governance | 0 | Inventory, architecture, programme OPENs, guards |
| OFN | `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` | v0.10 | `ofn-v0.10` | canonical foundational | 2 | O0–O3 commitments; model selection; class-C model contract; foundational OPENs |
| RRF | `dsn/RTG_RRF_REPRESENTATION_REGISTRY.md` | v0.8.4 | `rrf-v0.8.4` | adopted working standard | 5 | Representation conventions, interface contracts and identifiers (`RRF` namespace, Methodology v1.4 §4.2); not an owner of physics |
| LEGACY | `dsn/RTG_L0_L1_L2_BRIDGE_LEGACY_DSN.md` | v0.7 | `legacy-v0.7` | canonical historical | 2 | L0/L1/L2 revalidation ledger; not a current branch |
| PREL | `dsn/RTG_PRE_LEGACY_DSN.md` | v0.8 | `prelegacy-v0.8` | canonical historical | 2 | ESM / node-resonance provenance; not a current branch |
| NUMGEN | `dsn/RTG_NUMBER_GENESIS_DSN.md` | v1.20.8 | `numgen-v1.20.8` | canonical common home | 2 | Relational composition, representation and realization; continuous and discrete sectors separately typed |
| DYAD | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` | v6.4.22 | `dyad-v6.4.22` | canonical | 3 | Selected primitive map, local return and normalization, $p$-resonance programme |
| TRIAD | `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` | v1.6.1 | `triad-v1.6.1` | canonical | 3 | Birth kinematics and diagnostic lifts |
| GEN | `dsn/RTG_GENESIS_GEOMETRY_DSN.md` | v2.8.9 | `gen-v2.8.9` | canonical | 3 | Integrating study: $K_3/K_4$ algebra, metric, constrained lift, network, Regge machinery |
| UVM | `dsn/RTG_OPEN_M_DSN.md` | v0.7.1 | `uvm-v0.7.1` | canonical | 3 | UV-generator model classes and source/restoring blocks; Genesis keeps test and verdict custody |
| RECOG | `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` | v0.3.23 | `recog-v0.3.23` | canonical | 3 | Comparators, return content, event strata, lattice memory on the dyadic substrate |
| DZT | `dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md` | v0.8 | `dzt-v0.8` | canonical | 3 | Arithmetic diagnostics of Dyadic-owned coefficients |
| TDRG | `dsn/RTG_DISCRETE_GENESIS_DSN.md` | v2.12.13 | `tdrg-v2.12.13` | canonical | 4 | Native discrete model, policies, growth/suppression programme |
| AZ | `dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md` | v0.6 | `az-v0.6` | canonical infrastructure | 5 | Diagnostic engine and graph mathematics with typed threads |
| RER | `noncanonical/RTG_RELATIONAL_EMERGENCE_REGISTRY.md` | v0.2 ADOPTED (noncanonical) | `rer-v0.2` | noncanonical registry | — | Emergence records and supplementary contracts with receiver-scoped acceptance |
| FMS | `noncanonical/FMS_MODEL_SELECTION_LEDGER.md` | v0.6.4 SESSION | `fms-v0.6.4` | noncanonical ledger | — | Model-selection audit; input to OFN's class-C contract |
| ER2B | `noncanonical/RTG_ER2B_CONSOLIDATED_STUDY.md` | v0.3 | `er2b-v0.3` | noncanonical study | — | Consolidated research source and provenance record; not a handoff |
| ATLAS | `atlas/RTG_STATE_ATLAS.md` | v0.3 | `atlas-v0.3` | derived map (noncanonical) | — | AI-oriented current-state map with `atlas/RTG_STATE_ATLAS_METHOD.md`; never a source; owner DSN wins |

Genesis's own header tier statement is the owner's; this overview locates the integrating study in Tier 3 and records discrete inputs as blocked interfaces, not dual branch membership. Number Genesis and the historical ledgers receive navigation placement only. No scientific maturity follows from a placement or a class.
"""

S6_2_5 = """### 6.2 Governance, foundations, standards and history

Each entry gives custody and the programme-relevant interfaces. The owner's current state is in its own header status summary and OPEN registry at the tag; this overview does not restate it.

**METH — Methodology** (v1.4, `methodology-v1.4`). Owns the grammar, profiles, evidence and revision rules, the namespace registry (§4.2; `RRF` added in v1.4) and the release discipline (two-stage releases, release records, governing edition = tag + release record, §13). Programme v1.3 is built under it. Existing owner files keep their declared Methodology edition until individually migrated.

**PROG — Programme Overview** (v1.3 candidate). Owns navigation: inventory, programme OPEN coordination, maturity semantics, programme guards. All five programme OPEN records remain ACTIVE (§5).

**OFN — Ontological Foundations** (v0.10, `ofn-v0.10`). Owns commitments, competing primitive hypotheses, model-selection questions, the class-C model contract and the foundational OPENs (OPEN-OFN-3B, -FRUSTRATION, -OPA among them). Receives scoped technical feedback from DYAD, RECOG, GEN, TRIAD, OPEN M, NUMGEN and TDR-G as imports (OFN §11); it does not acquire the proofs it cites.

**RRF — Representation Registry** (v0.8.4, `rrf-v0.8.4`; adopted working standard). Records representation conventions (CN-xx), interface contracts (RRF-CND-01 and the class-C model contract with OFN), its own OPEN interface items (OPEN-A pole relabeling, OPEN-B/E1/E2 network inheritance) and verbatim owner imports (DYAD, RECOG, OFN, GEN, TRIAD). It owns no physics and adopts no owner claim; consumers cite it for conventions and interface identifiers.

**LEGACY — L0/L1/L2 Bridge Legacy** (v0.7, `legacy-v0.7`). Owns preservation and recovery of its historical diagnostic records and toolkit. Explicitly not a current active scientific branch; its artifact/definition gates, low-$\\mu$ restrictions and non-export rule remain operative within the source.

**PREL — Pre-Legacy** (v0.8, `prelegacy-v0.8`). Owns the historical node-resonance/ESM synthesis and article provenance. Historical claim grades are not current-branch calibrations. Its owner pass in the v1.2 maintenance sequence has not been executed; its pointers into OFN and Genesis content predate the current editions of those owners (§9.2).

**NUMGEN — Number Genesis** (v1.20.8, `numgen-v1.20.8`). Owns relational composition, representation and realization modules; its continuous local-history modules and its discrete DISC modules remain separately typed. Imports OFN, DYAD, GEN and TDR-G (DISC) at the editions in its §9.1; exports to RECOG by RID (N5AS1 definitions and results) and records RECOG as a consumer (its §9.1 row). Its foundational/technical profile is not evidence for OPEN-P1.

### 6.3 Continuous technical studies

**DYAD — Dyadic Oscillator** (v6.4.22, `dyad-v6.4.22`). Owns the selected primitive map, local return enclosure and normalization, ISP geometry and the explicitly defined $p$-resonance coefficient programme. Direct consumers: Genesis, Triadic, RECOG, DZT, OPEN M, continuous Number Genesis modules, RRF, OFN; AZ cross-indexes its arithmetic. Imports RECOG results (its §7: RECOG-THM-R9-MEMORY as the stated assumption of its OPEN 3/21 asymptotic-phase theorems; RECOG-THM-A1A-RECIPROCAL-AMPLITUDE), NUMGEN, RRF conventions and OFN commitments.

**TRIAD — Triadic Birth–Lift** (v1.6.1, `triad-v1.6.1`). Owns its birth/lift and diagnostic-model ledger and the T-6 export protocol. Imports Genesis (primitive seed, metric conventions), Dyadic, RRF (CN-05 planar metric convention), OFN and Programme; exports scoped diagnostics to Genesis and OPEN M.

**GEN — Genesis Geometry** (v2.8.9, `gen-v2.8.9`). One canonical owner file combining primitive $K_3/K_4$ algebra with quaternionic metric, constrained-lift, network and Regge machinery; retains the test framework and geometry verdict custody for OPEN M. Imports Dyadic, Triadic, OFN; TDR-G input remains a blocked cross-branch interface (IF25). The proposed split of primitive algebra from the geometry framework is still a proposal (§6.7).

**UVM — OPEN M** (v0.7.1, `uvm-v0.7.1`). Owns UV-generator model classes and the derivation of source/restoring blocks and their physical parameters; Genesis keeps the harness and the cascade/metric verdict. Imports Genesis, Dyadic, Triadic, OFN, Programme and Pre-Legacy priors. No physical UV deliverable to Genesis is complete (IF09).

**RECOG — Relational Recognition** (v0.3.23, `recog-v0.3.23`). Owns comparators, return-content results, candidate event strata and the lattice-memory theorems on the dyadic substrate. Imports Dyadic, Number Genesis (by RID at v1.20.8), Genesis, OFN and RRF conventions; its results are consumed by Dyadic, OFN, RRF and RER (RECOG §7.3). The general-$p$ return-equivariance proof is RECOG's; the bridge-lemma statement RID is Dyadic's — a settled custody split, not a pending transfer. Its OPEN registry and the live-file exception of its release record are the owner's; see RECOG §2 and `records/recog/RECOG_v0_3_23_RELEASE_RECORD.md` §11.

**DZT — Dyadic Arithmetic-Resonance Transform** (v0.8, `dzt-v0.8`). Owns channel-state, resultant/norm and transform diagnostics of Dyadic-owned coefficients; imports Dyadic (its §7 pin v6.4.8.1). Not a Riemann-Hypothesis claim or an OPEN-M source calibration. Its owner pass has not been executed since v1.2 (§9.2).

### 6.4 Discrete technical study and its launch gate

**TDRG — Discrete Genesis** (v2.12.13, `tdrg-v2.12.13`). Owns native cyclic-state/event definitions, policy branches, kinematic/BIND3 modules and the growth/suppression programme; imports OFN and Programme (its §7 pins v0.6 and v1.1). Exports to Number Genesis (DISC) and AZ (Threads B/C). Its owner pass has not been executed since v1.2.

**Launch-gate source record** (unchanged since v1.2; the owner edition is unchanged). The owner's canonical §§1–2 give
```text
TDR-24D / TDR-24F: reported closed at the declared scope
TDR-24A -> TDR-24B -> TDR-24C -> TDR-T: pending launch chain
```
Its Appendix C still carries an older D/A/B gate and reserves R3–R10 for work after TDR-T0 opens. This overview records that unresolved source discrepancy; it does not repair the owner appendix or authorize a launch. BIND3 and already-scoped three-node/no-birth diagnostics are not equated with launch of the full birth programme.

### 6.5 Shared infrastructure, noncanonical documents and the derived map

**AZ — Arithmetic Resonance and Zeta** (v0.6, `az-v0.6`). Tier 5 infrastructure serving both branches; owns Thread C engineering and graph-theoretic facts about its diagnostic objects; Dyadic and TDR-G physics remain in their own sources (its §8 pins Dyadic v6.4.8.1 and TDR-G v2.12). DZT and AZ remain separate studies. Its owner pass has not been executed since v1.2.

**RER — Relational Emergence Registry** (v0.2 ADOPTED, noncanonical, `rer-v0.2`). A working registry of emergence records with receiver-scoped acceptance; adoption covers the registry scope, not the science it records. Imports RRF, Dyadic, Genesis, Triadic, RECOG, OFN and ER-2B at the editions in its §7; keeps frozen historical pins where it says so.

**FMS — Model Selection Ledger** (v0.6.4 SESSION, noncanonical, `fms-v0.6.4`). Session-grade audit of model selection; its results enter OFN's class-C contract only through OFN's own imports.

**ER2B — ER-2B Consolidated Study** (v0.3, noncanonical, `er2b-v0.3`). Consolidated research source and provenance record; kept as a reference, not a handoff request.

**ATLAS — RTG State Atlas** (v0.3, `atlas-v0.3`; derived, noncanonical). An AI-oriented map of the current state across all owners, built by its own method (`atlas/RTG_STATE_ATLAS_METHOD.md`) from the tagged editions, with typed diagnostics and declared evidence limits. It advises owners through advisories recorded under `records/`; owners decide. It is never the source of a claim; on any conflict the owner DSN wins.
"""

S6_6_INTRO = """These are **not existing document homes** of the §6.1 inventory. None receives maturity A merely because it has a proposed name. Since v1.2 two documents that v1.2 did not list came into existence as homes and are now in §6.1 (RRF as an adopted working standard, RER as a noncanonical registry); neither is a replacement for any proposal below."""

S6_7_TAIL = """**Historical and governance documents:** retain the separate Pre-Legacy, Legacy, Methodology, Programme and OFN roles. No merger is enacted. Methodology v1.4 §13.3 governs any later decision. The queue is retained from v1.2 (P12-P4); none of its items has been executed, and its retention does not authorize a split, merger, rename or claim transfer."""

S7 = """## 7. Cross-Study Dependency Graph and Ownership Interfaces

### 7.1 Typed overview

`[DEF]` An arrow is meaningful only with its type. **Declared import** means a consumer records using an owner source in its own Import Ledger, not that this pass certified the import. **Standard reference** means a consumer cites a convention or interface identifier from RRF. **Requested deliverable** is incomplete. **Historical reference** provides no current-physics proof. **Noncanonical record** means a noncanonical document records an owner's result or request; it transfers nothing. **Blocked cross-branch** is not an available path. Arrows are read from the consumer's ledger at its governing edition (§7.2 gives the sections).

```text
Methodology v1.4 -- normative rules --> every document built or migrated under it
Programme / OFN -- coordination and commitments --> scoped technical owners
RRF -- conventions and interface contracts (standard reference) --> DYAD, TRIAD, RECOG, OFN, RER, FMS

Continuous declared imports:
  DYAD --> TRIAD; DYAD --> GEN; GEN --> TRIAD; TRIAD --> GEN
  GEN --> UVM; DYAD --> UVM; TRIAD --> UVM
  DYAD --> NUMGEN[continuous]; NUMGEN[continuous] --> RECOG (RECOG recorded by NUMGEN as consumer)
  DYAD --> RECOG; RECOG --> DYAD (R9 memory as stated assumption of OPEN 3/21; reciprocal amplitude)
  GEN --> RECOG; DYAD --> DZT
  OFN <-- DYAD, RECOG, GEN, TRIAD, UVM, NUMGEN, TDRG   (scoped technical feedback, OFN §11)

Requests, NOT completed supply:
  UVM -?-> GEN                         physical UV inputs (open)
  DZT -?-> DYAD                        arithmetic diagnostic feedback (open)
  NUMGEN -?-> OFN                      technical feedback synchronization (recorded by OFN as import; open items remain)

Discrete declared uses:
  TDRG --> NUMGEN[discrete/DISC]
  TDRG --> AZ[Thread B/C]

Noncanonical records (transfer nothing):
  RER  records RRF, DYAD, GEN, TRIAD, RECOG, OFN, ER-2B
  FMS  records OFN, RRF, GEN, DYAD, ER-2B
  ER2B records OFN, RRF, TRIAD, GEN, LEGACY, PREL, RECOG, DYAD

Shared reference-only indexing:
  DYAD -- reference --> AZ[Thread A]
  LEGACY -- historical scope --> PREL
  PREL -- hypothesis/provenance only --> UVM

Physical cross-branch route:
  TDRG -X-> continuous uses            blocked until a named P1 bridge
  continuous coefficients -X-> TDRG   same firewall in reverse

P0 discrete-limit route needs P1; other P0 routes have their own prerequisites.
P2B invariant reduction does not itself settle P2A ontology (criterion home: OFN OPEN-OFN-3B).
P3 coupling conclusion needs metric + curvature dictionary, not UV input alone.
```

Closed since v1.2: the v1.2 request "RECOG -?-> DYAD general-return adoption/ownership" is settled as a custody split (statement RID Dyadic's, general-$p$ proof RECOG's; IF17). No path through NUMGEN, AZ, RRF or a noncanonical document converts a reference-only or branch-local result into a proved cross-branch physical transfer. This graph is a study-level navigation map, not a claim-RID dependency DAG.

### 7.2 Interface register

Each row names the consumer section that declares the interface and the consumer's own pin where it is not the source's governing edition. A pin older than the governing edition is the consumer's declared state, not a defect; repinning is the consumer's decision. Rows IF01–IF25 keep their v1.2 identifiers; IF26–IF36 are new in v1.3; a retired row says so.

| IF | From → To | Type | Content | Declared at (consumer) | Consumer pin |
|---|---|---|---|---|---|
| IF01 | METH → PROG | normative | grammar, profiles, evidence and revision rules | this document, header | v1.4 |
| IF02 | OFN → DYAD | constraint | model-selection commitments, not a derivation of $T$ | DYAD §7 | v0.10 |
| IF03 | OFN → TDRG | constraint | relational commitments; discrete interaction-selection questions | TDRG §7 | v0.6 (historical pin) |
| IF04 | DYAD → TRIAD | declared-import | fracture state, local return, frame data | TRIAD §7 | v6.4.13 (and v6.4.8.1 historical) |
| IF05 | DYAD → GEN | declared-import | direct dyadic input | GEN §7 | v6.4.13 |
| IF06 | GEN → TRIAD | declared-import | primitive tetrahedral seed and metric conventions | TRIAD §7 | v2.8.7 |
| IF07 | TRIAD → GEN | declared-import | scoped diagnostic exports under the T-6 protocol | GEN §7 | v1.6 |
| IF08 | GEN → UVM | declared-import | secular frame, norms, cascade test and geometry requirements; Genesis keeps verdict custody | UVM §0.3, §7 | v2.8.5 |
| IF09 | UVM → GEN | requested-deliverable | UV blocks and physical source/stiffness data | UVM §0.2–§0.3 | open; no cascade implied |
| IF10 | DYAD → UVM | declared-import | normalization and local inputs, not a UV generator | UVM §7 | v6.4.10 |
| IF11 | TRIAD → UVM | declared-import | chirality and seed-comparison imports | UVM §7 | v1.6 |
| IF12 | DYAD → NUMGEN | declared-import | selected-map support for continuous history constructions | NUMGEN §9.1 | v6.4.18 |
| IF13 | TDRG → NUMGEN | declared-import | discrete event rules and harness input for DISC | NUMGEN §9.1 | v2.12.13 |
| IF14 | NUMGEN → RECOG | declared-import | contraction, defect and INF-1 results by RID (`NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-INF1`, L1, N1C, GAP-LOCK) | RECOG §6.13b, §7 | v1.20.8 (v1.15 producer pins retained where load-bearing) |
| IF15 | GEN → RECOG | declared-import | $B$, $J_Q$, pairings and phase-memory context | RECOG §7 | as declared in RECOG §7 |
| IF16 | DYAD → RECOG | declared-import | map, return coefficients, resonance and normal-form inputs; chart laws | RECOG §7 | v6.4.22 by RID and section (producer editions named per row) |
| IF17 | RECOG ↔ DYAD | mutual citation (retired as transfer-proposal) | `DYAD-ALG-BRIDGE-LEMMA` statement RID is Dyadic's; the general-$p$ proof is `RECOG-ALG-LEADING-RETURN-EQUIVARIANCE` | RECOG §6.10, §7; DYAD §6.9 | settled; nothing pending |
| IF18 | DYAD → DZT | declared-import | channel coefficients and cascade formula | DZT §7 | v6.4.8.1 |
| IF19 | DZT → DYAD | feedback-proposal | arithmetic diagnostic feedback | DZT §§1–2 | open |
| IF20 | DYAD → AZ | reference-only | Thread A arithmetic cross-index | AZ §8 | v6.4.8.1 |
| IF21 | TDRG → AZ | declared-import | Thread B context and Thread C graph exports | AZ §8 | v2.12 |
| IF22 | LEGACY → PREL | historical-reference | L2 scope underlying condensed summaries | PREL §7 | as declared |
| IF23 | PREL → UVM | historical-hypothesis | harmonic/log-frustration and dimensional-ladder priors | UVM §7 | v0.8 |
| IF24 | NUMGEN → OFN | feedback (recorded import) | holonomy operator and representation results | OFN §11 | as declared in OFN §11 |
| IF25 | TDRG → GEN | blocked-cross-branch | possible native phase moments or selector evidence | GEN §2 OPEN 1, §7 | v2.12.13; blocked pending a named P1 bridge |
| IF26 | RECOG → DYAD | declared-import | `RECOG-THM-R9-MEMORY` as the stated assumption of Dyadic's OPEN 3/21 asymptotic-phase theorems (`[THM] [assuming: RECOG-THM-R9-MEMORY]`); `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE` | DYAD §6.14, §7 | v0.3.22 |
| IF27 | NUMGEN ← RECOG | consumer record | NUMGEN records RECOG as a consumer of its N5AS1 RIDs; RECOG's explicit-domain A1a theorems are not listed by NUMGEN as inputs | NUMGEN §9.1 | v0.3.22 |
| IF28 | RECOG → OFN | declared-import | comparator definitions and recognition feedback (IMP rows) | OFN §11 | as declared in OFN §11 |
| IF29 | RRF → DYAD, TRIAD, RECOG, OFN | standard reference | conventions (CN-05 planar metric among them), interface contracts, identifiers | DYAD §7; TRIAD §7; RECOG §7; OFN §11 | DYAD v0.8.4; TRIAD v0.8.2; RECOG v0.8.4 (v0.8.3 rows historical); OFN v0.8.3 |
| IF30 | DYAD, RECOG, OFN, GEN, TRIAD, TDRG → RRF | verbatim owner import | registry imports with RID (e.g. RECOG W3, DYAD N14, OFN class-C request) | RRF §2 table | DYAD v6.4.18; RECOG v0.3.21; OFN v0.10; GEN v2.8.9 |
| IF31 | OFN ↔ RRF | interface contract | class-C model contract (OFN N-O10-3 / RRF §6.2a) | OFN §5.5, §11; RRF §6.2a | v0.10 / v0.8.4 |
| IF32 | DYAD, GEN, TRIAD, UVM, TDRG → OFN | declared-import (scoped feedback) | technical feedback rows IMP-O10-* | OFN §11 | as declared in OFN §11 |
| IF33 | RRF, DYAD, GEN, TRIAD, RECOG, OFN, ER2B → RER | noncanonical record | emergence records and contracts with receiver-scoped acceptance | RER §7, source manifest | RRF v0.8.4; TRIAD v1.6.1; RECOG v0.3.20 frozen pin (v0.3.21/22 recorded) |
| IF34 | OFN, RRF, GEN, DYAD, ER2B → FMS | noncanonical record | model-selection audit inputs | FMS §0 source manifest | as declared |
| IF35 | OFN, RRF, TRIAD, GEN, LEGACY, PREL, RECOG, DYAD → ER2B | noncanonical record | consolidated study inputs | ER2B Part A | as declared |
| IF36 | all owners → ATLAS | derived map | typed current-state extraction with declared evidence limits | atlas SOURCES table | the governing tags at the atlas snapshot |

### 7.3 Read-only reports, normative imports and pending uses

The entries of §6 are **custody and interface records**. No theorem coefficient is imported here for a new derivation, and no owner closure is re-certified or restated; the owner's header status summary at its tag is the current state. The load-bearing governance source is **DSN_METHODOLOGY v1.4** (`methodology-v1.4`), §§0.5–0.7, 1.1, 3.3–3.4, 4.2–4.5, 5.2–5.4 and 13; its rules have section identities, not theorem RIDs. The GEN/UVM custody split is transcribed from **OPEN M v0.7.1 §0.3**; the TDR-T gate report from **Discrete Genesis v2.12.13 §§1–2 and Appendix C** (`tdrg-v2.12.13`), with the discrepancy preserved. Neither report substitutes a module RID for an unnamed theorem.
"""

S8_2 = """### 8.2 Cross-stream symbol table — κ

Navigation only. The same letter names different objects in different owners; each owner keeps its symbol and its definition. A reader meeting κ checks this table and then the owner section. No identification between rows is implied unless an owner states it. Rows are at the governing editions of §6.1.

| Symbol as written | Owner | Where defined | What it names |
|---|---|---|---|
| κ (class-C coupling) | OFN, RRF, FMS | OFN §5.5.4; RRF §6.2a; FMS (throughout, §10A) | class-C model coupling of the OFN/RRF model contract; its relation to Genesis's γ is an atlas reading, not an owner statement |
| κ (birth coefficient), child ratio $i\\kappa Q_s$ | GEN; TRIAD; UVM | GEN §2 priority ordering, §3, §6.3; TRIAD §6.1; UVM §1.3 | Genesis birth coefficient in the leading child W-ratio; its selection is OPEN in Genesis |
| CN-05 (planar metric convention) | RRF; TRIAD; UVM; OFN | RRF §3.1; TRIAD header and §3; UVM §0.3 | a convention identifier, not a coupling; often appears beside κ |
| κ_recoil | GEN | GEN §6.3 (recoil reference policy) | recoil reference value $-\\tfrac12$ |
| κ_phys | GEN; UVM | GEN §1; UVM §3 | physical-branch coupling target as Genesis defines it; see GEN §1 for its current status |
| κ_RTG = 𝒢_e/J_e | PROG; GEN; LEGACY | this document §5 P3; GEN §2 priority ordering; LEGACY §7 | formal intended matching target for the smooth coupling, hypothesis-grade (§5 P3); not a defined physical coupling (SG-PROG-3) |
| κ_bb, κ_fit | DYAD | DYAD §6.5, §4 | backbone ansatz and DSI-fit parameters (historical fit quantities, not canonical constants) |
| κ (shear family $g_\\kappa$), κ (cusp order 2), κ (fold scalar) | RECOG | RECOG §6.6a; §6.11; §6.16c | three distinct local uses inside RECOG, each defined at its site |
| κ₃ | LEGACY; PREL; UVM | LEGACY §5 (L2 Type-I), PREL §1.8; UVM §6 | historical L2 curvature coupling; UVM cites it as a historical quantity |
| κ = 2πc, κ_grav, κ_top, κ′, κ_B | PREL | PREL §1.5, §1.7, quick-retrieval table | historical ESM constants; not current-branch calibrations |
| κ (3-field basis ρ·σ·κ) | TDRG | TDRG §6 (TDR-24 dependency chain) | a proposed and rejected factorization basis, recorded as such |
"""

S9_2 = """### 9.2 Two-pass completion and maintenance record

Pass one (owner updates) and pass two (consumer and Programme synchronization) are the Methodology's release passes (v1.4 §13). v1.2 was the pass-one architecture release; v1.3 is the pass-two synchronization of its inventory and interfaces. Under Methodology v1.4 §1.1 and §13.1 a material change to this file is a new tagged edition; history lives in tags and release records, not in the live file.

**Maintenance sequence recorded in v1.2** (OFN → Legacy → Pre-Legacy → Dyadic → TDR-G → Number Genesis → DZT → Genesis primitive → Triadic → Genesis geometry → OPEN M → RECOG → AZ) **— state at 23 October 2026:**

| Owner | v1.2 edition | Governing edition | Owner pass since v1.2 |
|---|---|---|---|
| OFN | v0.7 | v0.10 | executed (v0.8, v0.9, v0.10) |
| Legacy | v0.6 | v0.7 | executed |
| Pre-Legacy | v0.8 | v0.8 | **not executed**; the oldest outstanding item; its pointers into OFN and Genesis content predate those owners' current editions |
| Dyadic | v6.4.9 | v6.4.22 | executed (v6.4.10–v6.4.22; two-stage release pilot at v6.4.21) |
| TDR-G | v2.12.13 | v2.12.13 | **not executed** |
| Number Genesis | v1.18 | v1.20.8 | executed |
| DZT | v0.8 | v0.8 | **not executed** |
| Genesis | v2.8.4 | v2.8.9 | executed (one file; the primitive/geometry split remains a proposal, §6.7) |
| Triadic | v1.5 | v1.6.1 | executed |
| OPEN M | v0.6 | v0.7.1 | executed |
| RECOG | v0.3 | v0.3.23 | executed (v0.3.1–v0.3.23) |
| AZ | v0.6 | v0.6 | **not executed** |
| Methodology | v1.3 | v1.4 | moved (v1.4 adopted 22 October 2026) |

Remaining queue, in the v1.2 order: Pre-Legacy, TDR-G, DZT, AZ. The sequence is administrative, not a mathematical dependency. A corrected source does not update its consumers by implication; intentional historical pins remain pinned (§7.2).
"""

S9_3 = """### 9.3 Evidence and adoption

This revision has no physics computation and no scientific certificate. Its evidence is administrative: the build scripts, edit logs, checker outputs and movement map under `evidence/programme/`, and the release record under `records/programme/`. Hashes establish file identity only; the checks establish that the inventory and interface pins agree with `BASELINE.md` and the tags, that the five programme OPEN RIDs, the four scope-guard identifiers and the section anchors are retained, and that no scientific tag is introduced. They do not re-prove owner mathematics or certify the completeness of the corpus dependency graph.

Adoption is the PI's decision, recorded in the release record; publication is a merge commit on `main` and the annotated tag programme-v1.3 naming the adopted file's SHA-256. The v1.2 release record, change record and the three administrative registers of the v1.2 package were searched for and not found (PI, 23 October 2026); they are recorded as missing, not reconstructed. Scientific OPENs remain; unresolved contradictions are not described as reconciled.
"""

APPA_ENTRY = """### v1.3 — 23 October 2026 — DRAFT, stage 1 (corrected intermediate; not adopted)

- **Basis [governance]:** atlas advisory `records/programme/ATLAS_ADVISORY_PROGRAMME_v1_2.md` (atlas v0.3 H10, PROG.G1–G7) as disposed by the PI on 23 October 2026 (its §5); Methodology v1.4.
- **§§0/6 [inventory]:** governing editions by tag for all homes (nine rows moved: METH v1.4, OFN v0.10, LEGACY v0.7, NUMGEN v1.20.8, DYAD v6.4.22, TRIAD v1.6.1, GEN v2.8.9, UVM v0.7.1, RECOG v0.3.23); class column; new rows RRF (adopted working standard), RER, FMS, ER-2B (noncanonical) and the State Atlas (derived map); §6.2–6.5 reduced to custody and interface records that point to the owners' status summaries.
- **§7 [interfaces]:** pins to governing tags or labelled consumer pins; IF17 retired as a transfer proposal (settled custody split); IF26–IF36 added (RECOG → DYAD/OFN, NUMGEN's consumer record of RECOG, RRF as standard, OFN feedback imports, noncanonical records, atlas).
- **§§5/8/9 [pointers]:** OFN v0.10 and RRF v0.8.4 named as criterion homes for P0 and P2B (OPEN-OFN-3B); OPEN M v0.7.1 for P3; §8.2 cross-stream κ table; §9.2 maintenance record with the remaining queue (Pre-Legacy, TDR-G, DZT, AZ); §9.3 repository-based evidence and adoption.
- **Unchanged:** two-branch architecture, maturity semantics and the v1.1 maturity records, all five programme OPEN RIDs and their ACTIVE status, SG-PROG-1–4, the restructuring queue, the TDR-T launch-gate record, Appendix B replacement ledger.
- **Records:** release record `records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md`; v1.2 release and change records recorded as missing.
"""

FOOTER = """*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.3 (DRAFT candidate, 23 October 2026; pass-two synchronization of the adopted v1.2 architecture under DSN Methodology v1.4; `programme-v1.2` governs until adoption).*
"""

# ----------------------------------------------------------------------------------------------

def section(text, start, end):
    """Exact-once block from the line starting with `start` up to (not including) the line starting with `end`."""
    i = text.find(start)
    assert i >= 0 and text.find(start, i + 1) < 0, ("start not unique/found", start)
    j = text.find(end, i + len(start))
    assert j >= 0, ("end not found", end)
    return text[i:j]

def main(base_path, out_path, log_path):
    base = open(base_path, encoding="utf-8").read()
    assert sha(base) == BASE_SHA, "base is not programme-v1.2"
    text = base
    log = []

    def rep(key, row, loc, old, new):
        nonlocal text
        assert text.count(old) == 1, (key, "old text not exact-once", old[:80])
        text = text.replace(old, new)
        log.append(dict(key=key, row=row, location=loc, old_sha256=sha(old), new_sha256=sha(new),
                        old_len=len(old), new_len=len(new), old=old, new=new))

    # header: from the title line to the first '---'
    rep("H-1", "PA-01, PA-05, PB-10", "header", section(text, "# RTG_PROGRAMME_OVERVIEW_v1.2\n", "\n---\n") + "\n", HEADER)
    # §0.1
    rep("S0-1", "PA-05, PB-10, PC-13", "§0.1", section(text, "### 0.1 Present orientation and revision boundary\n", "### 0.2 Profile map"), S0_1 + "\n")
    # §4 table
    rep("S4-1", "PB-09", "§4 maturity table", section(text, "| Study | Previous or owner-declared maturity record | This pass |\n", "\n---\n"), S4_TABLE_TAIL)
    # §5 pointers
    rep("S5-1", "PB-07", "§5 P0 owner study",
        "**Owner study:** Programme Overview for coordination; OFN and relevant technical owners supply the selection criteria and results.  ", S5_P0_OWNER)
    rep("S5-2", "PB-07", "§5 P2B next decision",
        "**Next required decision:** assign the technical construction owner and admissibility criterion; no owner is assigned by this release.", S5_P2B_NEXT)
    rep("S5-3", "PB-07", "§5 P3 dependencies",
        "**Dependencies:** the source-specific UV, metric and gluing requirements. OPEN M completion is not by itself Regge closure. Preparatory Regge definitions and consistency studies need not wait for every UV computation; their final physical coupling use does.", S5_P3_DEPS)
    # §6.1 .. §6.5
    rep("S6-1", "PA-01, PA-02", "§6.1", section(text, "### 6.1 Navigation tiers and source inventory\n", "### 6.2 Governance, foundations and history"), S6_1 + "\n")
    rep("S6-2", "PA-02, PA-03", "§6.2–6.5", section(text, "### 6.2 Governance, foundations and history\n", "### 6.6 Proposed documents and historical placeholders"), S6_2_5 + "\n")
    rep("S6-3", "PA-02", "§6.6 intro",
        "These are **not existing scientific homes** in the 14-document inventory. None receives maturity A merely because it has a proposed name.", S6_6_INTRO)
    rep("S6-4", "PA-05", "§6.7 tail",
        "**Historical and governance documents:** retain the separate Pre-Legacy, Legacy, Methodology, Programme and OFN roles. No merger is enacted. Methodology §13.3 governs any later decision. P12-P4 is accepted as retention of this recommendation queue; that acceptance does not authorize a split, merger, rename or claim transfer.", S6_7_TAIL)
    # §7
    rep("S7-1", "PA-04", "§7", section(text, "## 7. Cross-Study Dependency Graph and Ownership Interfaces\n", "\n---\n\n<a id=\"prog-guards\"></a>"), S7)
    # §8.2 κ table appended after §8.1 table (before the --- that precedes §9)
    s81 = section(text, "### 8.1 High-risk programme readings\n", "\n---\n\n<a id=\"prog-naming\"></a>")
    rep("S8-1", "PC-12", "§8.2 new", s81, s81 + "\n" + S8_2)
    # §9.2, §9.3
    rep("S9-1", "PA-05, PA-06", "§9.2", section(text, "### 9.2 Two-pass completion\n", "### 9.3 Evidence and adoption"), S9_2 + "\n")
    rep("S9-2", "PA-05", "§9.3", section(text, "### 9.3 Evidence and adoption\n", "\n---\n\n<a id=\"prog-history-appendix\"></a>"), S9_3)
    # small pointer edits
    rep("S6-5", "PA-05 (reference resolvability)", "§6.4 TDR-G appendix reference",
        "Its Appendix C still carries an older D/A/B gate",
        "Its Appendix C (`tdrg-v2.12.13`) still carries an older D/A/B gate")
    rep("B-1", "PA-05 (reference resolvability; ledger wording otherwise untouched)", "Appendix B PROG12-C10",
        "retains its Appendix C discrepancy and post-launch reserved requirements",
        "retains its Appendix C (TDR-G's, `tdrg-v2.12.13`) discrepancy and post-launch reserved requirements")
    rep("S2-0", "PA-01", "§2.1 Pre-Legacy edition",
        "Reference-only history: `RTG_PRE_LEGACY_DSN_v0.8` records the sequence",
        "Reference-only history: the Pre-Legacy ledger (v0.8, `prelegacy-v0.8`) records the sequence")
    rep("S0-2", "PA-05", "§0.2 profile map row",
        "| Versioned reference ledger and evidence boundaries | Appendix C; release-package manifests and preserved review records |",
        "| Versioned reference ledger and evidence boundaries | §6.1 (governing editions by tag), `BASELINE.md`; build and check evidence under `evidence/programme/` |")
    rep("S0-3", "PA-05", "§0.2 orientation core note",
        "The programme orientation core is noncontiguous: header, §0.1, §§3–5, §6.1 and §8.",
        "The programme orientation core is noncontiguous: header, §0.1, §§3–5, §6.1, §7.2 and §8.")
    rep("S2-1", "PA-01", "§2.2 Legacy edition",
        "Reference-only history: `RTG_L0_L1_L2_BRIDGE_LEGACY_DSN_v0.6` already provides",
        "Reference-only history: the L0/L1/L2 Bridge Legacy ledger (v0.7, `legacy-v0.7`) already provides")
    rep("S5-4", "PA-01", "§5 P0 scope pin",
        "[scope: selected model already stated in Programme v1.1 §5 and Dyadic v6.4.9 §6.1]",
        "[scope: selected model already stated in Programme v1.1 §5; owner definition `DYAD-DEF-PRIMITIVE-MAP`, Dyadic §6.1 at `dyad-v6.4.22`]")
    rep("S5-5", "PA-02", "§5 P1 owner study",
        "a dedicated physical bridge study has not been opened in the supplied inventory.",
        "a dedicated physical bridge study has not been opened (§6.6).")
    rep("S9-0", "PA-05", "§9.1 namespace registry",
        "The namespace registry is **Methodology v1.3 §4.2**.",
        "The namespace registry is **Methodology v1.4 §4.2** (`RRF` registered there in v1.4).")
    # Appendix A entry
    rep("A-1", "release entry", "Appendix A", "## Appendix A — Version History\n\n### v1.2 — September 20, 2026 — Adopted inventory/architecture release",
        "## Appendix A — Version History\n\n" + APPA_ENTRY + "\n### v1.2 — September 20, 2026 — Adopted inventory/architecture release")
    # footer
    rep("F-1", "PA-05", "footer", section(text, "*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.2*", "\n\n\n") if "\n\n\n" in text[text.find("*END OF DOCUMENT"):] else text[text.find("*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.2*"):], FOOTER)

    open(out_path, "w", encoding="utf-8").write(text)
    out = dict(base_sha256=sha(base), intermediate_sha256=sha(text), edit_count=len(log),
               advisory="records/programme/ATLAS_ADVISORY_PROGRAMME_v1_2.md", edits=log)
    json.dump(out, open(log_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(sha(text), len(log), "edits")

if __name__ == "__main__":
    main(*sys.argv[1:4])
