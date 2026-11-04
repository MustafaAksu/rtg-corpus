#!/usr/bin/env python3
"""Programme Overview v1.4 candidate: maintenance synchronization of the adopted v1.3 (one content stage).

Basis: PI decision of 4 November 2026 in the atlas session ("programme i yapıp geçelim": do the Programme sync and
move on), with Claude (atlas owner) as revision editor as for v1.3. Inputs: the four receiver items in pipes/PROG/
(GEN kappa-table finding with E-P13-1; OFN v0.11 and v0.12 notices; Triadic v1.7 notice with CN-05), the v1.3
post-release note (E-P13-1), and the governing editions of 4 November 2026 (BASELINE.md and the tags).

Rules
- every edit is exact-once: `rep` (a string occurring once in the current text) or `line` (the unique line starting with
  a given prefix, replaced whole); the old text is taken from the text at run time and logged with its hash, so the log
  reconstructs the base (gate C2 of check_programme_v1_4.py);
- no OPEN-P status, maturity grade, criterion or scope-guard text changes; no scientific tag is introduced;
- the Programme restates no owner science: §6 rows carry edition, tag, custody and interfaces only.

usage (repository root):
  git show programme-v1.3:dsn/RTG_PROGRAMME_OVERVIEW.md > base.md
  python -I evidence/programme/scripts/build_programme_v1_4.py base.md OUT.md EDITLOG.json
"""
import hashlib, json, sys

BASE_SHA = "1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06"

def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()

class Builder:
    def __init__(self, t): self.t = t; self.log = []
    def rep(self, key, old, new):
        n = self.t.count(old)
        assert n == 1, f"{key}: old text occurs {n}x"
        assert old != new, f"{key}: no change"
        self.t = self.t.replace(old, new)
        assert self.t.count(new) == 1, f"{key}: new text not unique"
        self.log.append(dict(key=key, op="rep", old=old, new=new, old_sha256=sha(old), new_sha256=sha(new)))
    def line(self, key, prefix, new):
        L = self.t.split("\n")
        hits = [i for i, l in enumerate(L) if l.startswith(prefix)]
        assert len(hits) == 1, f"{key}: prefix matches {len(hits)} lines"
        old = L[hits[0]]
        self.rep(key, old, new)
        self.log[-1]["op"] = "line"; self.log[-1]["prefix"] = prefix

# ---------------------------------------------------------------------------------------------------------------
H_TITLE = "# RTG_PROGRAMME_OVERVIEW_v1.4"
H_DATE = "**Date:** 4 November 2026"
H_SCOPE = ("**Scope:** Inventory, ownership, branch/layer architecture, programme OPENs and scope guards, synchronized to the "
           "governing editions of the corpus; maintenance synchronization of the adopted v1.3 (inventory, interface register, "
           "pointers, κ table, receiver items).")
H_STATUS = ("**Document status:** DRAFT — v1.4 candidate (one content stage; no compaction); not adopted. `programme-v1.3` "
            "governs until adoption.")
H_SUPERSEDES = ("**Supersedes:** `RTG_PROGRAMME_OVERVIEW_v1.3` (tag `programme-v1.3`, SHA-256 "
                "`1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06`, adopted 24 October 2026).")
H_METH = "**DSN Methodology:** v1.4 (tag `methodology-v1.4`); v1.2 was adopted under v1.3; v1.3 and v1.4 under v1.4."
H_EDITOR = ("**Revision editor (v1.4):** Claude (atlas owner), by PI decision of 4 November 2026; change-focused review by "
            "ChatGPT. v1.3: the same editor, by PI decision of 23 October 2026.")
H_RELEASE = ("**Release record:** `records/programme/RTG_PROGRAMME_OVERVIEW_v1_4_RELEASE_RECORD.md`; v1.3: "
             "`records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md`. The v1.2 release and change records are not "
             "in the repository (recorded as missing there); v1.2's header records the PI's adoption of 20 September 2026.")

S01_P1 = ("The governing Methodology is v1.4 (tag `methodology-v1.4`). Programme v1.3 was the pass-two synchronization of "
          "the adopted v1.2 architecture. Programme v1.4 is a maintenance synchronization of v1.3: the inventory, the "
          "interface register, the owner pointers, the κ table and the maintenance record are brought to the governing "
          "editions of 4 November 2026, and the receiver items of `pipes/PROG/` are answered; the two-branch architecture, "
          "maturity semantics, OPEN-P criteria and scope guards are unchanged since v1.2. The source of every edition is the "
          "repository: a study's governing edition is its latest adopted tag with its release record; `BASELINE.md` is the "
          "machine-readable list.")

S4_HEAD = "| Study | Previous or owner-declared maturity record | v1.4 |"
S4_DYAD = ("| Dyadic | B in Programme v1.1 | Record retained; no owner header at `dyad-v6.4.23` declares an A–D grade; "
           "scientific reconciliation of the grade not performed by the Programme |")
S4_RECOG = ("| RECOG | A requested in the v0.3 header and stream memo (September 2026) | Record retained; no grade requested or "
            "declared in the v0.3.27 header; no grade issued here |")

S5_P0 = ("**Owner study:** Programme Overview for coordination; OFN (admissibility and model-selection criteria, OFN v0.12 "
         "§§5, 9) and RRF (representation and interface contracts, RRF v0.8.4) supply the criteria; technical owners supply "
         "results.  ")
S5_P2B = ("**Next required decision:** the criterion home is OFN v0.12, OPEN-OFN-3B (`RTG-OFN-OPEN-PRIMACY-3B`: admissible "
          "triad-to-dyad invariant reduction; row agreement on $c=0$ explicitly insufficient). No technical construction "
          "owner is assigned; the Programme assigns none.")

INV = {
 "PROG": "| PROG | `dsn/RTG_PROGRAMME_OVERVIEW.md` | v1.4 (this document) | `programme-v1.4` on adoption (predecessor `programme-v1.3`) | canonical governance | 0 | Inventory, architecture, programme OPENs, guards |",
 "OFN": "| OFN | `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` | v0.12 | `ofn-v0.12` | canonical foundational | 2 | O0–O3 commitments; model selection; class-C model contract; foundational OPENs |",
 "NUMGEN": "| NUMGEN | `dsn/RTG_NUMBER_GENESIS_DSN.md` | v1.21 | `numgen-v1.21` | canonical common home | 2 | Relational composition, representation and realization; continuous and discrete sectors separately typed |",
 "DYAD": "| DYAD | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` | v6.4.23 | `dyad-v6.4.23` | canonical | 3 | Selected primitive map, local return and normalization, $p$-resonance programme |",
 "TRIAD": "| TRIAD | `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` | v1.7 | `triad-v1.7` | canonical | 3 | Birth kinematics and diagnostic lifts |",
 "GEN": "| GEN | `dsn/RTG_GENESIS_GEOMETRY_DSN.md` | v2.10 | `gen-v2.10` | canonical | 3 | Integrating study: $K_3/K_4$ algebra, metric, constrained lift, network, Regge machinery |",
 "RECOG": "| RECOG | `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` | v0.3.27 | `recog-v0.3.27` | canonical | 3 | Comparators, return content, event strata, lattice memory on the dyadic substrate |",
 "TDRG": "| TDRG | `dsn/RTG_DISCRETE_GENESIS_DSN.md` | v2.12.14 | `tdrg-v2.12.14` | canonical | 4 | Native discrete model, policies, growth/suppression programme |",
 "ATLAS": "| ATLAS | `atlas/RTG_STATE_ATLAS.md` | v0.9 | `atlas-v0.9` | derived map (noncanonical) | — | AI-oriented current-state map with `atlas/RTG_STATE_ATLAS_METHOD.md`; never a source; owner DSN wins |",
}

S61_INTRO_OLD = "The placement additions and clarifications of v1.2 are retained; v1.3 adds the RRF, RER, FMS, ER-2B and Atlas rows and the class column."
S61_INTRO_NEW = ("The placement additions and clarifications of v1.2 are retained; v1.3 added the RRF, RER, FMS, ER-2B and Atlas "
                 "rows and the class column; v1.4 moves eight rows to their governing editions and adds no home.")

S62_METH_OLD = "Programme v1.3 is built under it."
S62_METH_NEW = "Programme v1.3 and v1.4 are built under it."
S62_PROG = ("**PROG — Programme Overview** (v1.4, this document; edition and tag in §6.1). Owns "
            "navigation: inventory, programme OPEN coordination, maturity semantics, programme guards. All five programme "
            "OPEN records remain ACTIVE (§5).")
S62_OFN_OLD = "**OFN — Ontological Foundations** (v0.10, `ofn-v0.10`)."
S62_OFN_NEW = "**OFN — Ontological Foundations** (v0.12, `ofn-v0.12`)."
S62_NUMGEN = ("**NUMGEN — Number Genesis** (v1.21, `numgen-v1.21`). Owns relational composition, representation and "
              "realization modules; its continuous local-history modules and its discrete DISC modules remain separately "
              "typed. Imports OFN, DYAD, GEN and TDR-G (DISC) at the editions in its §9.1; exports to RECOG by RID (N5AS1 "
              "definitions and results) and one route row to Genesis (IF38); records RECOG's explicit-domain theorems as "
              "independent agreement, not imports (its §9.1 acceptance matrix). Its foundational/technical profile is not "
              "evidence for OPEN-P1.")

S63_DYAD = ("**DYAD — Dyadic Oscillator** (v6.4.23, `dyad-v6.4.23`). Owns the selected primitive map, local return enclosure "
            "and normalization, ISP geometry and the explicitly defined $p$-resonance coefficient programme. Direct "
            "consumers: Genesis, Triadic, RECOG, DZT, OPEN M, continuous Number Genesis modules, RRF, OFN; AZ cross-indexes "
            "its arithmetic. Its scientific imports are RECOG results (its §7: RECOG-THM-R9-MEMORY as the stated "
            "assumption of its OPEN 3/21 asymptotic-phase theorems; RECOG-THM-A1A-RECIPROCAL-AMPLITUDE); RRF conventions "
            "are standard references (IF29), OFN commitments programme context (IF02), and Number Genesis appears as a "
            "consumer and in the L-PHASE interface (its §7.0, §7.0a).")
S63_TRIAD = ("**TRIAD — Triadic Birth–Lift** (v1.7, `triad-v1.7`). Owns its birth/lift and diagnostic-model ledger and the "
             "T-6 export protocol. Imports Genesis (primitive seed, metric conventions) and Dyadic claim by claim; RRF "
             "(CN-05 planar metric convention), OFN, the Programme and TDR-G are reference-only pointers (its §7.1); "
             "exports scoped diagnostics to Genesis and OPEN M, with per-recipient consumer state in its §7.4.")
S63_GEN = ("**GEN — Genesis Geometry** (v2.10, `gen-v2.10`). One canonical owner file combining primitive $K_3/K_4$ algebra "
           "with quaternionic metric, constrained-lift, network and Regge machinery; retains the test framework and geometry "
           "verdict custody for OPEN M. Imports Dyadic, Triadic and one Number Genesis route row (IF38); the Programme and "
           "OFN are companion references, not scientific imports (its §7); TDR-G input remains a blocked cross-branch "
           "interface (IF25). The proposed split of primitive algebra from the geometry framework is still a proposal (§6.7).")
S63_RECOG = ("**RECOG — Relational Recognition** (v0.3.27, `recog-v0.3.27`). Owns comparators, return-content results, "
             "candidate event strata and the lattice-memory theorems on the dyadic substrate. Imports Dyadic and Number "
             "Genesis by RID (at `dyad-v6.4.23` and `numgen-v1.21`), Genesis, OFN and RRF conventions; its results are "
             "consumed by Dyadic, OFN, RRF and RER (RECOG §7.3). The general-$p$ return-equivariance proof is RECOG's; the "
             "bridge-lemma statement RID is Dyadic's — a settled custody split, not a pending transfer. Its OPEN registry "
             "and release record are the owner's; see RECOG §2 and `records/recog/RECOG_v0_3_27_RELEASE_RECORD.md`.")

S64_TDRG = ("**TDRG — Discrete Genesis** (v2.12.14, `tdrg-v2.12.14`). Owns native cyclic-state/event definitions, policy "
            "branches, kinematic/BIND3 modules and the growth/suppression programme; imports OFN (its §7 claim pin v0.10; "
            "historical v0.6/v0.7 pins at its §2) and cites the Programme as context (v1.3). Exports to Number Genesis "
            "(DISC) and AZ (Threads B/C). Its owner pass since v1.2 is executed in part: v2.12.14 is a corrections edition "
            "under its declared Methodology v1.2, and records the state of the four owner-review tasks of Programme v1.2 "
            "§6 in its §2; the Methodology v1.4 migration is planned for its v2.13.")
S64_GATE_OLD_HEAD = "**Launch-gate source record** (unchanged since v1.2; the owner edition is unchanged). The owner's canonical §§1–2 give"
S64_GATE_NEW_HEAD = ("**Launch-gate source record** (owner edition `tdrg-v2.12.14`). The owner's canonical §§1–2 and its "
                     "Appendix C gate condition give")
S64_GATE_OLD_TAIL = ("Its Appendix C (`tdrg-v2.12.13`) still carries an older D/A/B gate and reserves R3–R10 for work after TDR-T0 "
                     "opens. This overview records that unresolved source discrepancy; it does not repair the owner appendix or "
                     "authorize a launch. BIND3 and already-scoped three-node/no-birth diagnostics are not equated with launch "
                     "of the full birth programme.")
S64_GATE_NEW_TAIL = ("The owner aligned its Appendix C with §§1–2 in v2.12.14 (a correction line); Appendix C still reserves R3–R10 for "
                     "work after TDR-T0 opens, and one export row of its §7 (`TDRG-EXPORT-DISCRETE-TRIAD`) still names the "
                     "earlier D/A/B gate. This overview records the source state; it does not repair the owner text or "
                     "authorize a launch. BIND3 and already-scoped three-node/no-birth diagnostics are not equated with launch "
                     "of the full birth programme.")
S65_ATLAS_OLD = "**ATLAS — RTG State Atlas** (v0.3, `atlas-v0.3`; derived, noncanonical)."
S65_ATLAS_NEW = "**ATLAS — RTG State Atlas** (v0.9, `atlas-v0.9`; derived, noncanonical)."

G71_OLD = "  GEN --> RECOG; DYAD --> DZT"
G71_NEW = "  GEN --> RECOG; DYAD --> DZT\n  GEN --> NUMGEN[continuous] (NG-10 only); NUMGEN --> GEN (one route row)"

R72_INTRO_OLD = "Rows IF01–IF25 keep their v1.2 identifiers; IF26–IF36 are new in v1.3; a retired row says so."
R72_INTRO_NEW = ("Rows IF01–IF25 keep their v1.2 identifiers; IF26–IF36 are new in v1.3; IF37–IF38 are new in v1.4 (IF37 "
                 "records an import that predates v1.3 and was not listed there); a retired row says so.")
IF = {
 "IF02": "| IF02 | OFN → DYAD | constraint | model-selection commitments, not a derivation of $T$ | DYAD §7 | v0.12 (programme context, §7.0) |",
 "IF03": "| IF03 | OFN → TDRG | constraint | relational commitments; discrete interaction-selection questions | TDRG §7 | v0.10 (claim pin; v0.6/v0.7 historical at its §2) |",
 "IF04": "| IF04 | DYAD → TRIAD | declared-import | fracture state, local return, frame data | TRIAD §7.1 | v6.4.23 claim by claim (v6.4.8.1 and v6.4.13 historical) |",
 "IF05": "| IF05 | DYAD → GEN | declared-import | direct dyadic input | GEN §7 | v6.4.13 (historical proof pins); v6.4.22 for the §6.3c (C2) rows; v6.4.23 for `DYAD-ALG-NU5-P5` |",
 "IF06": "| IF06 | GEN → TRIAD | declared-import | primitive tetrahedral seed and metric conventions | TRIAD §7.2 | v2.9 claim by claim (the radial-polynomial import held at v2.8.7) |",
 "IF07": "| IF07 | TRIAD → GEN | declared-import | scoped diagnostic exports under the T-6 protocol | GEN §7 | v1.7 claim by claim (CN-01–CN-05 received at v1.6) |",
 "IF12": "| IF12 | DYAD → NUMGEN | declared-import | selected-map support for continuous history constructions; the L-PHASE row-A remainder | NUMGEN §9.1 | v6.4.18 (map, PRIM-CTR, Q403); v6.4.22 (`DYAD-THM-LPHASE-ROWA-REMAINDER`) |",
 "IF14": "| IF14 | NUMGEN → RECOG | declared-import | contraction, defect and INF-1 results by RID (`NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-INF1`, L1, N1C, GAP-LOCK Lemma 3 by `NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO`) | RECOG §6.13b, §7 | v1.21 (v1.15 producer pins retained where load-bearing) |",
 "IF16": "| IF16 | DYAD → RECOG | declared-import | map, return coefficients, resonance and normal-form inputs; chart laws; row-A bridge and $C_7$ rows | RECOG §7 | v6.4.23 by RID and section (producer editions named per row) |",
 "IF25": "| IF25 | TDRG → GEN | blocked-cross-branch | possible native phase moments or selector evidence | GEN §2 OPEN 1, §7 | v2.12.14; blocked pending a named P1 bridge |",
 "IF26": "| IF26 | RECOG → DYAD | declared-import | `RECOG-THM-R9-MEMORY` as the stated assumption of Dyadic's OPEN 3/21 asymptotic-phase theorems (`[THM] [assuming: RECOG-THM-R9-MEMORY]`); `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE` | DYAD §6.14, §7 | v0.3.22 (claim-level; its §7.0 names v0.3.26 as current companion) |",
 "IF27": "| IF27 | NUMGEN ← RECOG | consumer record | NUMGEN records RECOG as a consumer of its N5AS1 RIDs and records RECOG's explicit-domain A1a/A1b theorems as independent agreement, not as inputs (its acceptance matrix) | NUMGEN §9.1 | v0.3.24 |",
 "IF29": "| IF29 | RRF → DYAD, TRIAD, RECOG, OFN | standard reference | conventions (CN-05 planar metric among them), interface contracts, identifiers | DYAD §7; TRIAD §7.1; RECOG §7; OFN §11 | DYAD v0.8.4; TRIAD v0.8.4; RECOG v0.8.4; OFN v0.8.4 |",
 "IF31": "| IF31 | OFN ↔ RRF | interface contract | class-C model contract (OFN N-O10-3 / RRF §6.2a) | OFN §5.5, §11; RRF §6.2a | RRF pins OFN v0.10; OFN pins RRF v0.8.4 |",
}
IF_NEW_AFTER_IF36 = (
 "| IF37 | GEN → NUMGEN | declared-import | reduced-sector saturation ceiling (`GEN-ART-SATURATION`), NG-10 only | NUMGEN §9.1 | v2.9 |\n"
 "| IF38 | NUMGEN → GEN | declared-import | cyclic-average theorem (`NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE`) as an independent route in Genesis §6.4 | GEN §7 | v1.21 |")

S73_OLD = ("the TDR-T gate report from **Discrete Genesis v2.12.13 §§1–2 and Appendix C** (`tdrg-v2.12.13`), with the "
           "discrepancy preserved. Neither report substitutes a module RID for an unnamed theorem.")
S73_NEW = ("the TDR-T gate report from **Discrete Genesis v2.12.14 §§1–2 and Appendix C** (`tdrg-v2.12.14`), with the "
           "remaining export-row wording recorded (§6.4). Neither report substitutes a module RID for an unnamed theorem.\n\n"
           "**Consumer notices received.** Triadic CN-05 (Programme/OFN note; Triadic v1.7 §7.4): received and accepted, no "
           "action. No statement of this overview uses the withdrawn T-6 sector, wedge, basin, phase-steering or "
           "route-obstruction exports, and the overview issues no cascade verdict, source deficit or ontology selection "
           "(§§5, 8). The IF07 pin is now Genesis's v1.7 pin; IF11 is OPEN M's own pin (v1.6) and moves only when OPEN M "
           "repins. OFN v0.11 and v0.12: received; OFN remains the criterion home of OPEN-P0 and OPEN-P2B (§5).")

K_CLASSC_OLD = "| κ (class-C coupling) | OFN, RRF, FMS | OFN §5.5.4; RRF §6.2a; FMS (throughout, §10A) | class-C model coupling of the OFN/RRF model contract; its relation to Genesis's γ is an atlas reading, not an owner statement |"
K_CLASSC_NEW = "| κ (class-C coupling) | OFN, RRF, FMS | OFN §5.5.4, §11.4; RRF §6.2a; FMS (throughout, §10A) | class-C model coupling of the OFN/RRF model contract; OFN §11.4 and RRF §6.2a record γ ≡ κ as the class-C parameter convention (Genesis writes γ) |"
K_CN05_OLD = "| CN-05 (planar metric convention) | RRF; TRIAD; UVM; OFN | RRF §3.1; TRIAD header and §3; UVM §0.3 | a convention identifier, not a coupling; often appears beside κ |"
K_CN05_NEW = "| CN-05 (planar metric convention) | RRF; TRIAD; UVM; OFN | RRF §3.1; TRIAD §6.18, §7.4; UVM §0.3 | a convention identifier, not a coupling; often appears beside κ |"
K_RECOIL_OLD = "| κ_recoil | GEN | GEN §6.3 (recoil reference policy) | recoil reference value $-\\tfrac12$ |"
K_RECOIL_NEW = (K_RECOIL_OLD + "\n| κ_f | GEN | GEN §6.8 (definition of the face-lift magnitude) | face-lift magnitude $\\kappa_f=\\lvert m\\rvert\\,\\lvert w\\rvert$ of the "
                "canonical face lift; Genesis states it distinct from the birth coefficient, κ_phys, κ_RTG and γ |")
K_TDRG_OLD = "| κ (3-field basis ρ·σ·κ) | TDRG | TDRG §6 (TDR-24 dependency chain) | a proposed and rejected factorization basis, recorded as such |"
K_TDRG_NEW = "| κ (3-field basis ρ·σ·κ) | TDRG | TDRG §2 (TDR-24B) | a proposed and rejected factorization basis, recorded as such |"

S92_P1_OLD = ("v1.2 was the pass-one architecture release; v1.3 is the pass-two synchronization of its inventory and "
              "interfaces.")
S92_P1_NEW = ("v1.2 was the pass-one architecture release; v1.3 was the pass-two synchronization of its inventory and "
              "interfaces; v1.4 is a maintenance synchronization of the same kind.")
S92_SEQ_OLD = "(OFN → Legacy → Pre-Legacy → Dyadic → TDR-G → Number Genesis → DZT → Genesis primitive → Triadic → Genesis geometry → OPEN M → RECOG → AZ) **— state at 23 October 2026:**"
S92_SEQ_NEW = "(OFN → Legacy → Pre-Legacy → Dyadic → TDR-G → Number Genesis → DZT → Genesis primitive → Triadic → Genesis geometry → OPEN M → RECOG → AZ) **— state at 4 November 2026:**"
ROW92 = {
 "| OFN | v0.7 |": "| OFN | v0.7 | v0.12 | executed (v0.8–v0.12) |",
 "| Dyadic | v6.4.9 |": "| Dyadic | v6.4.9 | v6.4.23 | executed (v6.4.10–v6.4.23; two-stage release pilot at v6.4.21) |",
 "| TDR-G | v2.12.13 |": "| TDR-G | v2.12.13 | v2.12.14 | executed in part (v2.12.14, corrections edition; Methodology v1.4 migration planned for v2.13) |",
 "| Number Genesis | v1.18 |": "| Number Genesis | v1.18 | v1.21 | executed |",
 "| Genesis | v2.8.4 |": "| Genesis | v2.8.4 | v2.10 | executed (one file; the primitive/geometry split remains a proposal, §6.7) |",
 "| Triadic | v1.5 |": "| Triadic | v1.5 | v1.7 | executed |",
 "| RECOG | v0.3 |": "| RECOG | v0.3 | v0.3.27 | executed (v0.3.1–v0.3.27) |",
}
S92_QUEUE_OLD = "Remaining queue, in the v1.2 order: Pre-Legacy, TDR-G, DZT, AZ."
S92_QUEUE_NEW = "Remaining queue, in the v1.2 order: Pre-Legacy, TDR-G (Methodology migration), DZT, AZ."

S93_OLD = "publication is a merge commit on `main` and the annotated tag programme-v1.3 naming the adopted file's SHA-256."
S93_NEW = "publication is a merge commit on `main` and the edition's annotated tag (`programme-v1.4` for this edition) naming the adopted file's SHA-256."

APPA_OLD = "### v1.3 — 24 October 2026 — Adopted"
APPA_NEW = """### v1.4 — 4 November 2026 — DRAFT (candidate; not adopted)

- **Basis:** PI decision of 4 November 2026 (Programme sync by the atlas owner as editor); the four receiver items of `pipes/PROG/` and the v1.3 post-release note (E-P13-1); Methodology v1.4.
- **Inventory and interfaces:** eight §6.1 rows to their governing editions (OFN v0.12, NUMGEN v1.21, DYAD v6.4.23, TRIAD v1.7, GEN v2.10, RECOG v0.3.27, TDR-G v2.12.14, Atlas v0.9); the PROG row and §6.2 entry worded for candidate and adopted state alike; §6.2–6.5 entries re-read against the owners' Import Ledgers; §7.2 consumer pins re-read at the governing tags; IF37 (GEN → NUMGEN, an import that predates v1.3) and IF38 (NUMGEN → GEN) added.
- **Pointers and receipts:** OFN v0.12 as criterion home for P0 and P2B; TDR-G launch-gate record at v2.12.14 (Appendix C aligned by the owner); Triadic CN-05 received and accepted, no action (§7.3); §8.2 class-C row corrected (E-P13-1), κ_f row added, two section pointers corrected; §9.2 state at 4 November 2026.
- **Unchanged:** architecture, maturity semantics and records, the five programme OPEN RIDs (all ACTIVE), SG-PROG-1–4, the restructuring queue, Appendix B.
- **Records:** `records/programme/RTG_PROGRAMME_OVERVIEW_v1_4_RELEASE_RECORD.md`.

### v1.3 — 24 October 2026 — Adopted"""

FOOT_OLD = "*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.3 (ADOPTED, 24 October 2026; pass-two synchronization of the adopted v1.2 architecture under DSN Methodology v1.4).*"
FOOT_NEW = "*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.4 (DRAFT candidate, 4 November 2026; maintenance synchronization of the adopted v1.3 under DSN Methodology v1.4).*"

# ---------------------------------------------------------------------------------------------------------------
def build(base):
    assert sha(base) == BASE_SHA, "base is not programme-v1.3"
    b = Builder(base)
    b.line("H-1", "# RTG_PROGRAMME_OVERVIEW_v1.3", H_TITLE)
    b.line("H-2", "**Date:** ", H_DATE)
    b.line("H-3", "**Scope:** ", H_SCOPE)
    b.line("H-4", "**Document status:** ", H_STATUS)
    b.line("H-5", "**Supersedes:** ", H_SUPERSEDES)
    b.line("H-6", "**DSN Methodology:** ", H_METH)
    b.line("H-7", "**Revision editor (v1.3):** ", H_EDITOR)
    b.line("H-8", "**Release record:** ", H_RELEASE)
    b.line("S0-1", "The governing Methodology is v1.4 (tag `methodology-v1.4`). Programme v1.3 is", S01_P1)
    b.line("S4-1", "| Study | Previous or owner-declared maturity record | v1.3 |", S4_HEAD)
    b.line("S4-2", "| Dyadic | B in Programme v1.1 |", S4_DYAD)
    b.line("S4-3", "| RECOG | A requested", S4_RECOG)
    b.line("S5-1", "**Owner study:** Programme Overview for coordination; OFN", S5_P0)
    b.line("S5-2", "**Next required decision:** the criterion home is OFN", S5_P2B)
    b.rep("S6-0", S61_INTRO_OLD, S61_INTRO_NEW)
    for k in ("PROG", "OFN", "NUMGEN", "DYAD", "TRIAD", "GEN", "RECOG", "TDRG", "ATLAS"):
        b.line(f"S6-1-{k}", f"| {k} | `", INV[k])
    b.rep("S6-2-METH", S62_METH_OLD, S62_METH_NEW)
    b.line("S6-2-PROG", "**PROG — Programme Overview** ", S62_PROG)
    b.rep("S6-2-OFN", S62_OFN_OLD, S62_OFN_NEW)
    b.line("S6-2-NUMGEN", "**NUMGEN — Number Genesis** ", S62_NUMGEN)
    b.line("S6-3-DYAD", "**DYAD — Dyadic Oscillator** ", S63_DYAD)
    b.line("S6-3-TRIAD", "**TRIAD — Triadic Birth–Lift** ", S63_TRIAD)
    b.line("S6-3-GEN", "**GEN — Genesis Geometry** ", S63_GEN)
    b.line("S6-3-RECOG", "**RECOG — Relational Recognition** ", S63_RECOG)
    b.line("S6-4-TDRG", "**TDRG — Discrete Genesis** ", S64_TDRG)
    b.rep("S6-4-GATE-1", S64_GATE_OLD_HEAD, S64_GATE_NEW_HEAD)
    b.rep("S6-4-GATE-2", S64_GATE_OLD_TAIL, S64_GATE_NEW_TAIL)
    b.rep("S6-5-ATLAS", S65_ATLAS_OLD, S65_ATLAS_NEW)
    b.rep("S7-1", G71_OLD, G71_NEW)
    b.rep("S7-2-0", R72_INTRO_OLD, R72_INTRO_NEW)
    for k, v in IF.items():
        b.line(f"S7-2-{k}", f"| {k} |", v)
    L36 = [l for l in b.t.split("\n") if l.startswith("| IF36 |")]
    assert len(L36) == 1
    b.rep("S7-2-NEW", L36[0], L36[0] + "\n" + IF_NEW_AFTER_IF36)
    b.rep("S7-3", S73_OLD, S73_NEW)
    b.rep("S8-2-1", K_CLASSC_OLD, K_CLASSC_NEW)
    b.rep("S8-2-2", K_CN05_OLD, K_CN05_NEW)
    b.rep("S8-2-3", K_RECOIL_OLD, K_RECOIL_NEW)
    b.rep("S8-2-4", K_TDRG_OLD, K_TDRG_NEW)
    b.rep("S9-2-1", S92_P1_OLD, S92_P1_NEW)
    b.rep("S9-2-2", S92_SEQ_OLD, S92_SEQ_NEW)
    for pre, new in ROW92.items():
        b.line(f"S9-2-{pre.split('|')[1].strip()}", pre, new)
    b.rep("S9-2-Q", S92_QUEUE_OLD, S92_QUEUE_NEW)
    b.rep("S9-3", S93_OLD, S93_NEW)
    b.rep("A-1", APPA_OLD, APPA_NEW)
    b.rep("F-1", FOOT_OLD, FOOT_NEW)
    return b

def main():
    base = open(sys.argv[1], encoding="utf-8").read()
    b = build(base)
    open(sys.argv[2], "w", encoding="utf-8", newline="").write(b.t)
    log = dict(base_sha256=BASE_SHA, candidate_sha256=sha(b.t), n_edits=len(b.log), edits=b.log)
    json.dump(log, open(sys.argv[3], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"{len(b.log)} edits; candidate {sha(b.t)}; {b.t.count(chr(10))} newlines")

if __name__ == "__main__":
    main()
