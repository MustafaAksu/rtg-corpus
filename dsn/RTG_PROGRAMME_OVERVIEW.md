# RTG_PROGRAMME_OVERVIEW_v1.3

**Title:** Relational Time Geometry — Programme Overview and Study Hierarchy
**Date:** 23 October 2026
**Scope:** Inventory, ownership, branch/layer architecture, programme OPENs and scope guards, synchronized to the governing editions of the corpus; pass-two revision of the adopted v1.2 architecture.
**Document class:** Programme overview, under DSN Methodology v1.4 §0.5.
**Document status:** ADOPTED — PI, 24 October 2026 (pass-two synchronization of the v1.2 architecture under Methodology v1.4; adoption record `records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md`). Supersedes `programme-v1.2`.
**Supersedes:** `RTG_PROGRAMME_OVERVIEW_v1.2` (tag `programme-v1.2`, SHA-256 `4207da05dca24256e7bc528cb9814f848838bcd98e3d01222fb2a633ec9fd359`, adopted 20 September 2026).
**Repository:** `MustafaAksu/rtg-corpus`, `main`. A study's governing edition is its latest adopted tag with its release record (Methodology v1.4 §13.9); `BASELINE.md` lists the governing editions with their SHA-256; `CONVENTIONS.md` gives the working rules. Project copies mirror `main`.
**Companion documents:** the governing editions in §6.1 (by tag). The list is not a substitute for claim-level imports; each consumer's own pins are in its Import Ledger (§7.2 records them where they differ).
**DSN Methodology:** v1.4 (tag `methodology-v1.4`); v1.2 was adopted under v1.3.
**Status summary:** Two physical research branches, continuous and discrete, with shared foundational, historical and diagnostic documents whose contents remain branch-typed. The inventory (§6.1) records fifteen canonical document homes in `dsn/`, including the RRF representation registry adopted as a working standard, three noncanonical registries and studies in `noncanonical/`, and one derived map (the State Atlas) that is never a source. All five programme-level scientific OPEN records (P0, P1, P2A, P2B, P3) remain ACTIVE; no maturity grade, scope guard or scientific status is changed by this edition. No physical bridge is certified.
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok — inherited authorship; separate approval by other inherited authors is not inferred.
**Revision editor (v1.3):** Claude (atlas owner), by PI decision of 23 October 2026; change-focused review by ChatGPT.
**Release record:** `records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md`. The v1.2 release and change records are not in the repository (recorded as missing there); v1.2's header records the PI's adoption of 20 September 2026.
**Archive reference:** rtgtheory.org · Zenodo DOI 10.5281/zenodo.17568897 — inherited programme locator, not a claim that this release has been deposited there.
---

<a id="prog-purpose"></a>
## 0. What This Document Is

`[DEF]` This Tier 0 document owns programme navigation: the study inventory, programme-level OPEN coordination, maturity definitions and programme scope guards. Scientific definitions, proofs, numerical campaigns and claim corrections remain in their designated owner DSNs. No physical theorem is established by appearing in this overview.

### 0.1 Present orientation and revision boundary

The governing Methodology is v1.4 (tag `methodology-v1.4`). Programme v1.3 is the pass-two synchronization of the adopted v1.2 architecture: the inventory, the interface register, the owner pointers and the maintenance record are brought to the governing editions of 23 October 2026; the two-branch architecture, maturity semantics, OPEN-P criteria and scope guards of v1.2 are unchanged. The source of every edition is the repository: a study's governing edition is its latest adopted tag with its release record; `BASELINE.md` is the machine-readable list.

The inventory (§6.1) recognizes fifteen canonical document homes in `dsn/` — Methodology, Programme Overview, Ontological Foundations, the RRF representation registry (adopted working standard), the two historical ledgers, Number Genesis as the foundational/technical common home, six continuous technical studies (Dyadic, Triadic, Genesis, OPEN M, RECOG, DZT), one discrete owner (TDR-G) and AZ as shared diagnostic infrastructure — plus three noncanonical documents (RER, FMS, ER-2B) and one derived map (the State Atlas). These are document homes and classes, not physical branches. Number Genesis keeps its continuous and discrete realization sectors distinct; AZ keeps its continuous references and discrete graph diagnostics distinct. Their shared location supplies no physical identification between substrates. A noncanonical document is a working record that no owner has adopted as science: it may be cited for what it records, never as the source of a claim. The derived map is read, not cited; on any conflict the owner DSN wins.

Owner closures that postdate v1.2 are indexed in §6 by edition and pointer; this overview does not re-certify them and does not restate them. The local continuous generator remains selected rather than physically derived; discrete rule/policy selection, the physical cross-branch bridge, primitive-object selection and metric/Regge/coupling completion remain research questions (§5).

**For an AI reader.** Start with `BASELINE.md` (editions and hashes), `CONVENTIONS.md` and Methodology v1.4 (rules), then the owner DSN of the question at its tag. `atlas/RTG_STATE_ATLAS.md` is a noncanonical map of the current state with its own method and limits; it points into the owners and is never the source of a claim.

### 0.2 Profile map

| Required function | Location in this programme profile |
|---|---|
| Current orientation and scope | Header and §0.1 |
| Mission and historical provenance | §§1–2 |
| Branch/layer routing and maturity semantics | §§3–4 |
| Programme OPEN registry | §5 |
| Existing and proposed study inventory | §6 |
| Declared dependencies and ownership interfaces | §7 |
| Scope guards / high-risk programme inferences | §8 |
| Naming, adoption and synchronization | §9 |
| Version history / replaced programme statements | Appendices A/B |
| Versioned reference ledger and evidence boundaries | §6.1 (governing editions by tag), `BASELINE.md`; build and check evidence under `evidence/programme/` |
| Technical derivations | Not applicable: owned in the scientific source ledgers |
| Computational physics artifacts | Not executed here; this package contains administrative validation only |
| Collaboration and revision provenance | Header, Appendix A, preserved change record and adoption/release record |

The programme orientation core is noncontiguous: header, §0.1, §§3–5, §6.1, §7.2 and §8. The standard technical-ledger `AI_CONTEXT_CORE_END` marker is not used for this programme-specific layout. All new section links use explicit HTML anchors. Local tag aliases: none.

---

<a id="prog-mission"></a>
## 1. Programme Mission

`[DEF]` **RTG (Relational Time Geometry)** investigates whether spacetime geometry, including metric structure, dimensional count and gravitational coupling, can arise from pre-geometric relational structure rather than pre-given physical spacetime coordinates.

The central research question is retained: can a universe with no pre-given physical metric, no external physical time and no absolute position generate the appearance of smooth 3+1-dimensional geometry through internal relational dynamics?

`[HYP]` Continuous effective dynamics and discrete constructive dynamics are two candidate strategies for that question. Pursuing both does not establish that either is physically selected, that one is more primitive, or that a limiting bridge exists. Formal mathematical state spaces and update indices used to formulate a model are not thereby claimed to be primitive physical space or time.

---

<a id="prog-history"></a>
## 2. Historical Arc

### 2.1 ESM studies and Pre-Legacy provenance

Reference-only history: the Pre-Legacy ledger (v0.8, `prelegacy-v0.8`) records the sequence from node-resonance models through cubic and spherical substrates to tetrahedral ESM. It preserves kernel constructions, campaigns, rejected assumptions and proposed current-study connections. These are historical records with source-specific evidence and limitations, not current-branch certifications merely because they appear in this timeline. See Appendix C of v1.2 (tag `programme-v1.2`), PREL.

### 2.2 L0 / L1 / L2 studies

Reference-only history: the L0/L1/L2 Bridge Legacy ledger (v0.7, `legacy-v0.7`) already provides the dedicated provenance ledger that v1.1 described as absent. It distinguishes L0 configurations, L0→L1 dynamical diagnostics, L1 micro-band work, L2 effective geometry and hypothesis-level emergence notes. Its §§0.2–0.5 explicitly withhold derivation/selection of the current continuous generator and impose revalidation/export gates.

`[COR]` Programme v1.1 §2.2 attributed the present $T$, $Q$ and zero-origin package to L0/L1/L2 without a recoverable handoff in that owner ledger. This overview records the attribution as a provenance question, not as established derivation and not as disproved history. The current technical definitions are located in the selected Dyadic/Genesis sources; origin evidence must be recovered separately. See PROG12-C02 in Appendix B and REQ-P12-02 in the change record.

### 2.3 Current programme

The current inventory is §6. Historical provenance, a selected working model, a proved result within that model and physical selection are separate records. Earlier node-based notation is not silently substituted for OFN's current relational commitments. Current-branch use of a historical result needs its declared revalidation/identification, not a chronological arrow alone.

---

<a id="prog-branches"></a>
## 3. Two-Branch Architecture

### 3.1 Distinct model strategies

`[DEF]` The physical branch labels remain **continuous** and **discrete**. “Branch” in the OPEN M title denotes a sub-study of the continuous programme, not a third substrate. The comparison below describes model roles; it is not a table of established physical endpoints.

| Property | Continuous programme | Discrete programme |
|---|---|---|
| Starting model | Selected dyadic map and explicitly defined extensions/families | Cyclic-state dynamics on $\mathbb Z_N$ with declared event rules/policies |
| State typing | Relational coordinates such as $(\rho,\eta)$; primitive, lifted/wrapped and normalized charts must be distinguished | Phases and advance tokens with branch-local relational/gauge definitions; variable node count where births occur |
| Interaction question | What follows from the chosen map, and what could select or extend it? | What motivates/selects the defect criterion, local event law and multistar policy? |
| Structures studied | Dyad, $K_3/K_4$ motifs, coupled networks, metric and UV constructions | Defect components, no-birth sectors, event-driven growth and policy-dependent networks |
| Intended downstream question | Conditions for metric emergence, cascade and a Regge/coupling dictionary | Native organization, growth/suppression limits, and any well-defined continuum description |
| Governing selection gaps | OPEN-P0 and owner-specific construction assumptions | TDR-G interaction/policy OPENs; OPEN-P1 for physical continuous comparison |

`[COR]` The former “momentum: inertial primitive / gauge artifact” row and unqualified “terminus” row are replaced by typed model questions. This overview does not resolve the owner-level momentum/gauge dispute or promote bulk-conditioned suppression to a policy-independent final state. See PROG12-C03.

### 3.2 Firewall and allowable reference use

> **[Local guard SG-PROG-1]** A physical use across the discrete/continuous boundary needs a named proved bridge with explicit assumptions; a reference, analogy or abstract isomorphism is not that bridge.

The full operative wording is in §8. Mere co-location, standard-mathematics reuse and reference-only indexing are permitted when their limited role is explicit. Importing a dynamical coefficient, identifying physical observables, or strengthening the other branch's physical conclusion requires the corresponding proved identification. A conditional bridge establishes only its stated implication; its physical assumptions remain visible.

### 3.3 Shared homes and typed sectors

Number Genesis owns composition/representation questions and scoped realization results. Its continuous local-history modules and its discrete DISC modules remain separately typed. Its foundational/technical profile is not evidence for OPEN-P1.

AZ owns its diagnostic engine and graph mathematics while retaining other studies' results as references. Its Thread A and Thread C are not a route for transferring Dyadic coefficients to discrete graphs. Historical ledgers preserve evidence and hypotheses but are not automatically active model branches. OFN supplies commitments and receives scoped technical feedback; it does not acquire the proofs it cites.

<a id="prog-maturity"></a>
## 4. Maturity Classification

`[DEF]` Maturity describes a **specified study/model and scope**, not every claim in a document. The A–D labels and their original intent are retained, with the following explicit reading adopted in v1.2:

| Level | Name | Required interpretation |
|---|---|---|
| **A** | Defined model | The named object/rule and its exploration scope are specified; an assignment must not conceal a known unresolved definition conflict. |
| **B** | Certified dynamics | Scoped mathematical and/or numerical behavior is established within the named model, with the actual evidence grades stated. Physical selection is not implied. |
| **C** | Bridge-supported | A named proved bridge supports the specified model/interface and permitted use. This can be local and conditional; it does not certify every other layer or physical inevitability. |
| **D** | Physical-universality candidate | A model-selection, limit or universality argument has been established for a stated class, observable set and domain; extrapolation beyond them is not licensed. |

`[DEF]` Document profile, navigation tier, physical branch, maturity, claim status, evidence access, task closure and adoption are independent fields. A document can contain multiple models or interfaces with different maturity records. A planned document that has not been opened receives **no model-maturity assignment** merely from its filename.

`[COR]` The v1.1 blanket “all continuous-branch results are Level B until P0 closes” is replaced by the physical-selection restriction in SG-PROG-2. A complete conditional theorem or a local bridge is not invalidated by open generator selection. Conversely, closing P0 by an administrative disposition or one restricted route cannot certify every coefficient as physically inevitable. See PROG12-C04/C05.

**First-pass assignment boundary.** No existing scientific study is promoted or demoted here. The records below preserve the prior Programme labels or owner-declared/requested labels as provenance. Slashed grades are not newly certified combined levels; their scope needs reassessment during the owner updates and pass two.

| Study | Previous or owner-declared maturity record | v1.3 |
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

---

<a id="prog-open-registry"></a>
## 5. Programme-Level Open Problems

`[DEF]` Four clusters are retained: P0, P1, P2 and P3. P2A and P2B are separate sub-problems of P2. All five existing module RIDs are preserved. They coordinate research across owners; a required theorem remains owned where it is proved. The revised closure semantics below are **adopted programme criteria**, not scientific closures. Their approval is recorded as P12-P2 in the release record; the Draft 1 change record preserves the proposal history.

<a id="prog-open-p0"></a>
### OPEN-P0 — Generator selection / universality

**RID:** `RTG-OPEN-GENERATOR-SELECTION`  
**Status:** ACTIVE  
**Owner study:** Programme Overview for coordination; OFN (admissibility and model-selection criteria, OFN v0.10 §§5, 9) and RRF (representation and interface contracts, RRF v0.8.4) supply the criteria; technical owners supply results.  
**Question:** What, if anything, selects the canonical continuous generator rather than adopting it as an effective model?

`[DEF]` [scope: selected model already stated in Programme v1.1 §5; owner definition `DYAD-DEF-PRIMITIVE-MAP`, Dyadic §6.1 at `dyad-v6.4.22`] The reference map is
$$T(\rho,\eta)=\bigl(\rho-\sin\eta,\;\eta+e^\rho-1-\sin\eta\bigr).$$
This is a model identification, not a derivation or proof import. Local chart and parameter-family conventions belong to Dyadic. Results conditional on this choice need not assume that nature selects it.

**Scientific closure routes:** a proved relational variational/selection principle; a proved effective limit of specified discrete dynamics; or a proved universality statement for a defined generator class and set of geometric observables. Each route must state assumptions, uniqueness/equivalence actually obtained, domain, owner results and physical-identification limits.

**Separate effective-model disposition:** the programme may explicitly retain $T$ as a useful scoped effective model without achieving selection. Such adoption closes a bookkeeping/model-policy task, not the scientific selection claim. Record it separately rather than marking scientific P0 closed by relabeling the existing model.

**Dependencies:** OPEN-P1 is required for the **discrete-limit route only**. It is not an unconditional prerequisite of a variational or other independent route. OFN admissibility criteria and appropriate owner definitions are common inputs; specific proof dependencies must be named by the chosen route.

**Known consumers:** continuous studies and continuous realization modules in Number Genesis.  
**Next required decision:** sharpen route-specific criteria at the OFN/Dyadic updates.  
**Governance follow-up:** no owner result is transferred by this entry; general-return transfer requests remain separate (§7).

<a id="prog-open-p1"></a>
### OPEN-P1 — Discrete–continuous bridge

**RID:** `RTG-OPEN-DISCRETE-BRIDGE`  
**Status:** ACTIVE  
**Owner study:** Programme Overview for coordination; a dedicated physical bridge study has not been opened (§6.6).  
**Question:** Does a specified discrete family admit a controlled continuous description, and what relation does that description have to the selected continuous programme?

`[HYP]` A limit or effective description of suitably scaled TDR-G dynamics may be related to a continuous RTG model. The limit and effective-description readings can overlap; they are not assumed mutually exclusive. Successful representation alone would not decide ontological primacy.

**Closure criterion:** specify the discrete policy and state/gauge data, limiting parameters, any simultaneous time/node-count scaling, source/target observables, maps between them, convergence notion and error/domain control. Prove the resulting relation at the claimed scope and register its permitted physical uses. Numerical agreement is evidence for the candidate, not the completed bridge theorem.

**Dependencies:** branch-local owner definitions and results required by the selected limit. TDR-G TDR-22/TDR-24 and Dyadic transport/backbone results are relevant possible inputs, not universal prerequisites of every conceivable bridge route.

**Negative outcome:** a failed specified scaling/policy/observable comparison rejects or constrains that regime; it does not automatically reject every bridge hypothesis.  
**Known consumers:** P0's discrete-limit route and currently blocked cross-branch uses in Genesis and shared ledgers.  
**Next required artifact:** a bridge charter and typed source/target/scaling specification, not a new imported coefficient table.

<a id="prog-open-p2a"></a>
### OPEN-P2A — Ontological primacy of the triad

**RID:** `RTG-OPEN-TRIAD-PRIMACY-ONTO`  
**Status:** ACTIVE  
**Owner study:** Programme Overview coordination; OFN owns the ontological question.  
**Question:** Under what explicit criterion, if any, is the triad physically more primitive or more complete than a dyad or minimal network?

`[HYP]` A triad may be the minimal physically complete relational object. “Closure” must specify the graph, directedness, dynamical and holonomy meanings at issue; a count or a shared name does not decide primacy.

**Closure criterion:** an explicit OFN criterion with a justified relation to the admissible dynamical models and the relevant alternatives. Technical results can constrain or provide witnesses; P2B alone is not an ontological verdict.  
**Dependencies:** OFN's competing primitive-object hypotheses and any specifically invoked owner results.  
**Next required decision:** define the criterion before declaring one construction to select ontology.

<a id="prog-open-p2b"></a>
### OPEN-P2B — Dynamical reduction of triad to dyad

**RID:** `RTG-OPEN-TRIAD-REDUCTION`  
**Status:** ACTIVE  
**Owner study:** Programme Overview coordination; construction and proof remain with a designated continuous technical owner.  
**Question:** Does an independently specified admissible triadic dynamics contain the dyadic map as a genuine invariant reduction?

`[DEF]` [scope: adopted closure specification, not an established construction] State the source/target spaces, admissible triadic model class, embedding $\iota$, gauges and equivalence relation. The target includes invariance and an intertwining relation
$$T_3\circ\iota=\iota\circ T,$$
with coordinate/gauge equivalence expressed explicitly where used. A longitudinal match on $c=0$ without transverse invariance is insufficient. The criterion must also exclude a trivial extension obtained only by inserting the already-chosen $T$ as a factor, unless that limited embedding is precisely the stated target.

**Closure criterion:** exhibit the admissible construction and prove the reduction, or prove nonexistence in an explicitly named class.  
**Interpretation boundary:** a positive reduction proves that subsystem relation; a negative result excludes its stated class. Neither automatically establishes triad-first or dyad-first ontology.  
**Dependencies:** the declared continuous state/model conventions; P0 remains a physical-selection condition, not an automatic blocker of a conditional reduction theorem.  
**Next required decision:** the criterion home is OFN v0.10, OPEN-OFN-3B (`RTG-OFN-OPEN-PRIMACY-3B`: admissible triad-to-dyad invariant reduction; row agreement on $c=0$ explicitly insufficient). No technical construction owner is assigned; the Programme assigns none.

<a id="prog-open-p3"></a>
### OPEN-P3 — RTG-to-Regge / smooth-geometry bridge

**RID:** `RTG-OPEN-REGGE-BRIDGE`  
**Status:** ACTIVE  
**Owner study:** Programme Overview coordination; Genesis retains geometry/test/verdict custody, OPEN M owns UV derivation, and a future Regge study would require a separate charter.

> **[Local guard SG-PROG-3]** No derived physical smooth gravitational coupling is established before the required metric branch and curvature/coupling dictionary are proved. A formal target is not that result.

**Question and closure stages:** derive the required physical UV inputs with their complete source/norm conventions; establish the claimed nondegenerate metric branch and necessary network compatibility; supply a typed RTG-to-Regge curvature dictionary; and derive the coupling with units, normalization and domain controlled.

`[HYP]` [scope: intended future matching, not a defined physical coupling] The v1.1 expression $\kappa_{\rm RTG}=\mathcal G_e/J_e$ is retained only as a **formal intended matching target**, not as a presently defined physical coupling. Its terms and applicability require the owner dictionary.

**Dependencies:** the source-specific UV, metric and gluing requirements. OPEN M v0.7.1 (tag `uvm-v0.7.1`) supplies no physical UV blocks and records no certified calibration deficit (its R15/R16 reinterpretation; see OPEN M §6 and Appendix B); OPEN M completion is not by itself Regge closure. Preparatory Regge definitions and consistency studies need not wait for every UV computation; their final physical coupling use does.

**Known consumers:** Genesis downstream physics and programme-level geometry claims.  
**Next required artifacts:** reconciled Genesis/OPEN M interface and a Regge dictionary specification. Exact coefficients and finite-$g$ cascade judgments are outside this inventory pass.

---

<a id="prog-inventory"></a>
## 6. Study Hierarchy and Status

### 6.1 Navigation tiers and source inventory

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

### 6.2 Governance, foundations, standards and history

Each entry gives custody and the programme-relevant interfaces. The owner's current state is in its own header status summary and OPEN registry at the tag; this overview does not restate it.

**METH — Methodology** (v1.4, `methodology-v1.4`). Owns the grammar, profiles, evidence and revision rules, the namespace registry (§4.2; `RRF` added in v1.4) and the release discipline (two-stage releases, release records, governing edition = tag + release record, §13). Programme v1.3 is built under it. Existing owner files keep their declared Methodology edition until individually migrated.

**PROG — Programme Overview** (v1.3 candidate). Owns navigation: inventory, programme OPEN coordination, maturity semantics, programme guards. All five programme OPEN records remain ACTIVE (§5).

**OFN — Ontological Foundations** (v0.10, `ofn-v0.10`). Owns commitments, competing primitive hypotheses, model-selection questions, the class-C model contract and the foundational OPENs (OPEN-OFN-3B, -FRUSTRATION, -OPA among them). Receives scoped technical feedback from DYAD, RECOG, GEN, TRIAD, OPEN M, NUMGEN and TDR-G as imports (OFN §11); it does not acquire the proofs it cites.

**RRF — Representation Registry** (v0.8.4, `rrf-v0.8.4`; adopted working standard). Records representation conventions (CN-xx), interface contracts (RRF-CND-01 and the class-C model contract with OFN), its own OPEN interface items (OPEN-A pole relabeling, OPEN-B/E1/E2 network inheritance) and verbatim owner imports (DYAD, RECOG, OFN, GEN, TRIAD). It owns no physics and adopts no owner claim; consumers cite it for conventions and interface identifiers.

**LEGACY — L0/L1/L2 Bridge Legacy** (v0.7, `legacy-v0.7`). Owns preservation and recovery of its historical diagnostic records and toolkit. Explicitly not a current active scientific branch; its artifact/definition gates, low-$\mu$ restrictions and non-export rule remain operative within the source.

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
Its Appendix C (`tdrg-v2.12.13`) still carries an older D/A/B gate and reserves R3–R10 for work after TDR-T0 opens. This overview records that unresolved source discrepancy; it does not repair the owner appendix or authorize a launch. BIND3 and already-scoped three-node/no-birth diagnostics are not equated with launch of the full birth programme.

### 6.5 Shared infrastructure, noncanonical documents and the derived map

**AZ — Arithmetic Resonance and Zeta** (v0.6, `az-v0.6`). Tier 5 infrastructure serving both branches; owns Thread C engineering and graph-theoretic facts about its diagnostic objects; Dyadic and TDR-G physics remain in their own sources (its §8 pins Dyadic v6.4.8.1 and TDR-G v2.12). DZT and AZ remain separate studies. Its owner pass has not been executed since v1.2.

**RER — Relational Emergence Registry** (v0.2 ADOPTED, noncanonical, `rer-v0.2`). A working registry of emergence records with receiver-scoped acceptance; adoption covers the registry scope, not the science it records. Imports RRF, Dyadic, Genesis, Triadic, RECOG, OFN and ER-2B at the editions in its §7; keeps frozen historical pins where it says so.

**FMS — Model Selection Ledger** (v0.6.4 SESSION, noncanonical, `fms-v0.6.4`). Session-grade audit of model selection; its results enter OFN's class-C contract only through OFN's own imports.

**ER2B — ER-2B Consolidated Study** (v0.3, noncanonical, `er2b-v0.3`). Consolidated research source and provenance record; kept as a reference, not a handoff request.

**ATLAS — RTG State Atlas** (v0.3, `atlas-v0.3`; derived, noncanonical). An AI-oriented map of the current state across all owners, built by its own method (`atlas/RTG_STATE_ATLAS_METHOD.md`) from the tagged editions, with typed diagnostics and declared evidence limits. It advises owners through advisories recorded under `records/`; owners decide. It is never the source of a claim; on any conflict the owner DSN wins.

### 6.6 Proposed documents and historical placeholders

These are **not existing document homes** of the §6.1 inventory. None receives maturity A merely because it has a proposed name. Since v1.2 two documents that v1.2 did not list came into existence as homes and are now in §6.1 (RRF as an adopted working standard, RER as a noncanonical registry); neither is a replacement for any proposal below.

| Proposed name or concept | Current disposition | Opening / replacement requirement |
|---|---|---|
| `RTG_DISCRETE_BIRTH_DSN` / TDR-T | Planned and launch-gated | Reconciled TDR-G launch contract, native definitions and a charter |
| `RTG_DISCRETE_CONTINUOUS_BRIDGE` | Proposed for P1 | Typed source/target, scaling and proof programme; no bridge yet |
| `RTG_GENERATOR_SELECTION` | Proposed for P0 | Owner/charter decision; existing OFN/Dyadic work need not wait for a new file |
| `RTG_REGGE_BRIDGE` | Proposed for P3 | Genesis/Regge custody and dictionary specification; no coupling closure |
| `RTG_PRIMITIVE_ONTOLOGY` | V1.1 placeholder retained as a deferred concept | Existing OFN and technical definition owners are the working homes; a new document needs a nonduplicating mandate |
| `RTG_PROVENANCE_L0_L1_L2` | V1.1 proposed remit is now served by the existing Legacy ledger | This is a scope-routing note, not an invented filename alias or automatic rename |

### 6.7 Restructuring queue — proposals only

**Genesis:** consider separating primitive Genesis algebra from metric/UV/Regge framework. Before any split, enumerate claims, preserve RIDs and evidence, name the two custodians and redirect consumers. No new Genesis file is created by this release.

**Number Genesis:** keep one study home; move chronological material and long proofs/campaign detail to the appropriate sections or versioned subordinate appendices before considering a scientific split.

**AZ:** reduce duplicated owner-science summaries and focus its owned diagnostic content. Do not merge it with DZT solely because both use arithmetic/zeta vocabulary.

**Triadic:** distinguish model identities and internal layers before deciding a split. Do not merge incompatible primitive and diagnostic systems into one claim set.

**Historical and governance documents:** retain the separate Pre-Legacy, Legacy, Methodology, Programme and OFN roles. No merger is enacted. Methodology v1.4 §13.3 governs any later decision. The queue is retained from v1.2 (P12-P4); none of its items has been executed, and its retention does not authorize a split, merger, rename or claim transfer.

---

<a id="prog-dependencies"></a>
## 7. Cross-Study Dependency Graph and Ownership Interfaces

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

---

<a id="prog-guards"></a>
## 8. Programme-Level Scope Guards

These are the adopted clarifications of the existing SG-PROG-1–4 under P12-P3, not new physics. Their old wording and replacement reasons are preserved in Appendix B. Existing consumers remain pinned to their stated Programme version until individually synchronized.

**[SG-PROG-1] — Cross-branch physical use.** No physical dynamical law, coefficient, observable identification or evidential strengthening may pass between discrete and continuous branches without a named bridge proved at the required `[ALG]` or `[THM]` scope, including a suitable rigorous-IA form where applicable. The importing owner must state the bridge's source/target objects, assumptions, permitted use and exact version/RID in its Import Ledger. Reference-only discussion and standard-mathematics reuse do not discharge this requirement.  
Violation: the cross-branch physical inference is unsupported; the guard alone does not prove its conclusion false or authorize an automatic `[FAIL]` verdict.

**[SG-PROG-2] — Model selection is not local proof status.** No result conditional on the selected continuous generator may be described as physically primitive, inevitable or universal beyond the support of an explicit selection/universality result. An OPEN-P0 disposition must name the route and domain; effective-model adoption is not physical selection. Exact local mathematics and properly scoped bridges may remain established while physical selection is open.  
Violation: upgrading conditional mathematics or a programme status label into an unsupported claim about nature.

**[SG-PROG-3] — Smooth coupling requires its physical dictionary.** No derived physical smooth gravitational coupling $\kappa_{\rm RTG}$ may be claimed before the required smooth metric branch and curvature/coupling dictionary are established with their assumptions, units and normalizations. Formal symbols, toy-model parameters and hypothesis-grade targets must be labeled as such.  
Violation: presenting an unestablished matching expression or historical calibration as the derived smooth coupling. UV closure alone does not discharge the Regge/dictionary stage.

**[SG-PROG-4] — Document location does not create transfer authority.** A tier label, shared infrastructure home, representation theorem or legacy provenance link may not be used to bypass the branch/layer restrictions of SG-PROG-1–3 or an owner's scope guards. Physical promotion requires the actual proved object-level identification, wherever the documents are filed.  
Violation: treating a Tier 2 or Tier 5 hub as an implicit bridge, or a Tier 3 label as a guarantee of physical compatibility.

### 8.1 High-risk programme readings

| Indexed statement | Valid use | Prohibited enlargement |
|---|---|---|
| A source is in the inventory | Its available edition, scope and custodian are recorded | Its claims have all been recertified or its methodology migrated |
| A source reports a closure | Report the outcome, grade, model and remaining dependencies | Close a broader programme question by summary |
| A local bridge exists | Use the named theorem within its assumptions | Infer physical universality or ontological priority |
| Number Genesis realizes labels/structures | Preserve its sector and representation/realization distinction | Identify different physical substrates or claim completed field arithmetic |
| A diagnostic null explains a pattern | Report the tested statistic and ensemble | Exclude all dynamic information or every alternative observable |
| A seed or representation ratio is known | Use its defined variables and normalization | Substitute it for a physical UV operator amplitude |
| A historical result is preserved | Recover or cite its historical scope | Treat it as an active-model calibration without revalidation |
| A source-RID assignment is open | Keep an exact temporary locator and request owner assignment | Reopen an intact theorem or borrow the containing module ID |
| A split is recommended | Prepare the custody and redirect plan | Create two competing authoritative copies or merge incompatible models |

### 8.2 Cross-stream symbol table — κ

Navigation only. The same letter names different objects in different owners; each owner keeps its symbol and its definition. A reader meeting κ checks this table and then the owner section. No identification between rows is implied unless an owner states it. Rows are at the governing editions of §6.1.

| Symbol as written | Owner | Where defined | What it names |
|---|---|---|---|
| κ (class-C coupling) | OFN, RRF, FMS | OFN §5.5.4; RRF §6.2a; FMS (throughout, §10A) | class-C model coupling of the OFN/RRF model contract; its relation to Genesis's γ is an atlas reading, not an owner statement |
| κ (birth coefficient), child ratio $i\kappa Q_s$ | GEN; TRIAD; UVM | GEN §2 priority ordering, §3, §6.3; TRIAD §6.1; UVM §1.3 | Genesis birth coefficient in the leading child W-ratio; its selection is OPEN in Genesis |
| CN-05 (planar metric convention) | RRF; TRIAD; UVM; OFN | RRF §3.1; TRIAD header and §3; UVM §0.3 | a convention identifier, not a coupling; often appears beside κ |
| κ_recoil | GEN | GEN §6.3 (recoil reference policy) | recoil reference value $-\tfrac12$ |
| κ_phys | GEN; UVM | GEN §1; UVM §3 | physical-branch coupling target as Genesis defines it; see GEN §1 for its current status |
| κ_RTG = 𝒢_e/J_e | PROG; GEN; LEGACY | this document §5 P3; GEN §2 priority ordering; LEGACY §7 | formal intended matching target for the smooth coupling, hypothesis-grade (§5 P3); not a defined physical coupling (SG-PROG-3) |
| κ_bb, κ_fit | DYAD | DYAD §6.5, §4 | backbone ansatz and DSI-fit parameters (historical fit quantities, not canonical constants) |
| κ (shear family $g_\kappa$), κ (cusp order 2), κ (fold scalar) | RECOG | RECOG §6.6a; §6.11; §6.16c | three distinct local uses inside RECOG, each defined at its site |
| κ₃ | LEGACY; PREL; UVM | LEGACY §5 (L2 Type-I), PREL §1.8; UVM §6 | historical L2 curvature coupling; UVM cites it as a historical quantity |
| κ = 2πc, κ_grav, κ_top, κ′, κ_B | PREL | PREL §1.5, §1.7, quick-retrieval table | historical ESM constants; not current-branch calibrations |
| κ (3-field basis ρ·σ·κ) | TDRG | TDRG §6 (TDR-24 dependency chain) | a proposed and rejected factorization basis, recorded as such |

---

<a id="prog-naming"></a>
## 9. Naming, Maintenance and Release Discipline

### 9.1 Document and identifier names

Preserve established study identities and exact historical filenames. A displayed version such as `v2.12.13` may be represented in a filename as `v2_12_13`; the number of version components is not restricted to two. The `_DSN` suffix is retained where it belongs to the existing study identity, not added retrospectively to Methodology, Programme or OFN.

The namespace registry is **Methodology v1.4 §4.2** (`RRF` registered there in v1.4). This overview does not maintain a competing RID grammar. `UVM` is the OPEN M namespace; `OFN` is a shortname, not an automatic replacement for `RTG-OFN`. Existing nonstandard identifiers remain owner-qualified until an exact alias is authorized. A theorem offered for transfer keeps its current identity until the explicit owner decision and movement record.

### 9.2 Two-pass completion and maintenance record

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

### 9.3 Evidence and adoption

This revision has no physics computation and no scientific certificate. Its evidence is administrative: the build scripts, edit logs, checker outputs and movement map under `evidence/programme/`, and the release record under `records/programme/`. Hashes establish file identity only; the checks establish that the inventory and interface pins agree with `BASELINE.md` and the tags, that the five programme OPEN RIDs, the four scope-guard identifiers and the section anchors are retained, and that no scientific tag is introduced. They do not re-prove owner mathematics or certify the completeness of the corpus dependency graph.

Adoption is the PI's decision, recorded in the release record; publication is a merge commit on `main` and the annotated tag programme-v1.3 naming the adopted file's SHA-256. The v1.2 release record, change record and the three administrative registers of the v1.2 package were searched for and not found (PI, 23 October 2026); they are recorded as missing, not reconstructed. Scientific OPENs remain; unresolved contradictions are not described as reconciled.

---

<a id="prog-history-appendix"></a>
## Appendix A — Version History

One compact entry per edition (Methodology v1.4 §1.1). Full entries of v1.0–v1.2, the Draft 1 history of v1.2 and the adopted replacement ledger's provenance are in Appendix A of v1.2 (tag `programme-v1.2`); the full stage-1 draft entry of v1.3 is at the stage-1 commit named in the release record.

### v1.3 — 24 October 2026 — Adopted

- **Basis:** atlas advisory `records/programme/ATLAS_ADVISORY_PROGRAMME_v1_2.md` as disposed by the PI on 23 October 2026 (its §5); Methodology v1.4.
- **Inventory and interfaces:** governing editions by tag for every home; class column; new rows for RRF (adopted working standard), RER, FMS, ER-2B (noncanonical) and the State Atlas (derived map); §6.2–6.5 reduced to custody and interface records pointing to the owners' status summaries; §7 pins at governing tags or labelled consumer pins; IF17 retired as a transfer proposal; IF26–IF36 added.
- **Pointers:** OFN v0.10 and RRF v0.8.4 as criterion homes for P0 and P2B; OPEN M v0.7.1 for P3; §8.2 cross-stream κ table; §9.2 maintenance record with the remaining queue (Pre-Legacy, TDR-G, DZT, AZ); §9.3 repository-based evidence and adoption.
- **Compaction [layout]:** compact Appendix A; Appendix C of v1.2 left at tag `programme-v1.2`; Appendix B retained (see release record).
- **Unchanged:** architecture, maturity semantics and the v1.1 maturity records, the five programme OPEN RIDs (all ACTIVE), SG-PROG-1–4, the restructuring queue, the TDR-T launch-gate record.
- **Records:** `records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md`; v1.2 release and change records recorded as missing.

### v1.2 — 20 September 2026 — Adopted

- Inventory/architecture release under Methodology v1.3: 14-home inventory, typed interfaces IF01–IF25, maturity semantics, OPEN-P closure criteria, scope guards SG-PROG-1–4 clarified (P12-P1–P12-P4 accepted by the PI). No scientific claim promoted, demoted or closed. Full entry and Draft 1 history: tag `programme-v1.2`.

### v1.1 — June 2026

- Four OPEN clusters; $T$ as postulated effective generator until OPEN-P0 closes; discrete wording corrected; filenames updated to the June editions. Full entry: tag `programme-v1.2`.

### v1.0 — June 2026

- Initial release from the RTG hierarchy analysis and the multi-AI design review: OPEN-P0–P3, maturity ladder, SG-PROG-1–4, five-tier hierarchy, dependency graph. Full entry: tag `programme-v1.2`.


---

<a id="prog-corrections"></a>
## Appendix B — Adopted Replacements of v1.1 Programme Statements

These administrative keys are not fabricated historical theorem RIDs. Each entry points to the immutable `RTG_PROGRAMME_OVERVIEW_v1_1.md` included in the package. The Programme replacements are adopted under the PI approval recorded for v1.2. They are not corrections enacted in scientific owner documents; those sources and their pending review tasks remain unchanged.

**PROG12-C01 — Authority and default tag.** Original §0 assigns untagged claims a default `[HEUR strong]` or `[HYP]`. Replacement: §0/§7.3 distinguishes navigation metadata, normative programme rules, versioned reference reports and genuinely scientific assertions. A default cannot supply evidence strength.

**PROG12-C02 — Historical handoff.** Original §2.2 says the L0/L1/L2 studies introduced the current $T,Q,\mathcal O_0$ package and that standalone provenance is absent. Replacement: §2 identifies the existing historical ledgers and leaves the specific handoff unverified. The attribution is not declared false; evidence is requested.

**PROG12-C03 — Branch comparison.** Original §3.1 uses “continuous phases,” a momentum dichotomy and unconditional termini. Replacement: §3.1 names typed state/model questions and prospective targets. This does not resolve the owners' state/gauge or limit claims.

**PROG12-C04 — Maturity scope.** Original §4 calls all continuous results Level B while §6 uses A/B and B/C locally. Replacement: §4 treats model/interface scope explicitly and preserves old/source labels without issuing new scientific grades. Selection openness is governed separately by SG-PROG-2.

**PROG12-C05 — P0 outcomes and dependency.** Original P0 counts scoped effective-model adoption as selection closure and unconditionally depends on P1. Replacement: §5 P0 distinguishes adoption disposition from selection and makes P1 conditional on the discrete-limit route. This is an adopted programme criterion clarification, not a newly proved route.

**PROG12-C06 — P1 test specificity.** Original P1 presents overlapping limit/effective readings as alternatives and treats failed convergence as evidence against an unspecified hypothesis. Replacement: §5 P1 requests a precise policy, scaling, correspondence and convergence claim; failures remain regime-scoped.

**PROG12-C07 — P2 reduction and ontology.** Original P2B makes reduction imply a more primitive triadic ontology and failure favor dyad primacy. Replacement: P2A/P2B separates invariant reduction, admissible model class and ontological selection; the intertwining expression is the adopted target specification, not a construction.

**PROG12-C08 — P3 custody and coupling.** Original P3 omits the dedicated OPEN M owner and treats the coupling expression as a closure item without a typed dictionary. Replacement: P3/§7 preserves GEN/UVM custody and the formal target, requires metric/dictionary/units, and permits preparatory work without premature physical coupling.

**PROG12-C09 — Inventory and planned entries.** Original §6 lists old DYAD/TRIAD/GEN/TDRG versions, omits or only partially registers several now-existing homes, and assigns A to unopened proposed studies. Replacement: §6 inventories the available owners (including OFN and the two historical ledgers), preserves editions and distinguishes unopened proposals from defined active models. No alias or merger is inferred from similar titles.

**PROG12-C10 — Discrete launch.** Original §6 requires all R0–R11 before launch and names 24D as the immediate blocker. Replacement: §6.4 records the current source's D/F closure and pending A/B/C chain, retains its Appendix C (TDR-G's, `tdrg-v2.12.13`) discrepancy and post-launch reserved requirements, and withholds launch authorization pending owner reconciliation.

**PROG12-C11 — Dependency graph and tier firewall.** Original §7 omits direct and reverse interfaces; SG-PROG-4 uses document tier as a physical-transfer test. Replacement: §§7–8 types each interface, preserves physical firewalls independent of placement, and distinguishes requests/proposals from completed results. Existing consumers remain unchanged.

**PROG12-C12 — Naming and current-state maintenance.** Original §9 limits the example to two version components and supplies only four study prefixes. Replacement: §9 preserves real filenames and uses the adopted Methodology namespace registry. Reference-only status refreshes, review findings and adopted scientific changes are separate actions.

---

---

*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.3 (ADOPTED, 24 October 2026; pass-two synchronization of the adopted v1.2 architecture under DSN Methodology v1.4).*
