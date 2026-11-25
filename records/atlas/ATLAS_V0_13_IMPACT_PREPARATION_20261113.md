# Atlas v0.13 — impact preparation (no build, no frozen manifest)

**Date:** 13 November 2026, checked 11:30–12:10 +03:00 on `main` `2de679b`. **By:** Claude, Atlas owner. **Status:** [SESSION] working record. Nothing here is atlas content; `atlas-v0.12` governs; no atlas byte is changed on this branch.
**Method:** v0.3 (`atlas-method-v0.3`).

## 1. Timing

Two source tags have moved since the v0.12 snapshot `c8e7198`: `az-v0.7` → `az-v0.8` and `tdrg-v2.12.14` → `tdrg-v2.12.15`. The other sixteen are unchanged (checked against `evidence/atlas/v0.12/source_manifest.json`). A third movement is in sight: the AZ v0.9 candidate (PR #253, head `e51fa3e62a`, not adopted, final readback pending).

**Sequence followed.** In the project conversation of 13 November 2026, 11:23 +03:00, the PI relayed a [SESSION] text that settles the question the owner had put on 12 November (refresh now with two sources, or wait): wait for AZ v0.9 and make one refresh; prepare the impact map now; do not freeze the manifest before AZ v0.9 is adopted; if the AZ review drags or meets a blocking scientific problem, reconsider an early refresh with two sources. The owner follows that sequence. The text's third point is taken as a constraint on the build: `AZ-NUM-TOKRES-S1` enters as AZ's `[NUM diagnostic]`, the new TDR-G `[ALG]` results enter under TDR-G's RIDs, and no claim gets two scientific owners.

**Consequence:** §§2–3 below are final in their source (adopted tags). §4 is provisional and is redone against the adopted `az-v0.9` bytes, whatever they are.

## 2. TDR-G v2.12.15 (`tdrg-v2.12.15`, adopted 12 Nov; file `1e35be54…2e64`)

Read for this map: the DSN diff through its 32-edit log and §6.13 in full (atlas row check, `records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_12_15.md`). Nine RIDs are new, none is removed.

| Atlas v0.12 item (line) | Change needed | Owner basis |
|---|---|---|
| SOURCES row TDRG; D5 header | `tdrg-v2.12.15`; scientific scope edition; Methodology v1.2 still declared (v1.4 migration is v2.13) | header |
| `TDRG-DEF-STAR` (L1279) | event domain: a valid centre has at least three pairwise non-adjacent defect neighbours; a single-star component has exactly one valid centre, any shape; only centre and newborn change. The K₁,₃-only wording is superseded; no result changes (`EV-CODE`); the share of non-pure single-star events in the canonical scans is unmeasured | §6.3, E16 |
| `TDRG-DEF-MULTISTAR` (L1280) | two or more valid centres, any shape | E17 |
| `TDRG-DEF-CONV-TICK` (L1269) | step 4: the precedence isolated, single edge, single-star, multistar, path, cycle; ties are outcomes of the path rule, not a class | E15 |
| O-DISC-STATE (L97, D1, OFN's import of the star rule) | no change to OFN's text; check whether an edge note is needed that the owner's DEF is now wider than the K₁,₃ picture | OFN v0.12 is unchanged |
| `TDRG-ALG-LEM-SPECCONS` (L1303); `*OFN:specs` (L149) | the n-node birth-free statement is proved (`TDRG-ALG-SPECCONS-N`), replacing "conjectured"; across births the update is exact but not determined by the spectrum | E18 |
| D5.L3 "invariants" line (L1366); L206 | TDR-6 is ACTIVE — PARTIAL. Sub-items: P FAIL as a birth invariant with ΔP ≡ −x, **not** "gauge"; pairwise multiset resolved as a predictable-change law; signed-class set exactly invariant, its "purely relational" status undecided. `TDRG-OPEN-SPECCONS-STAR` stays ACTIVE: open is a spectrum-level invariant or a law closed on the spectrum, and which centres fire | E07–E10 |
| **TDRG.G9** (L1386, "one question, two RIDs") | re-evaluate: the owner now separates the TDR-6 sub-item (resolved in predictable-change form) from the still-open spectrum-level question. Candidate for retirement or rewording | E09, E10 |
| D5.L4 guard list: SG-3 (L1377) | "total P not physical" → not adopted as a physical observable; not conserved at births; invariant under the declared gauge and under relabelling; not a gauge quantity. SG-12 gets the new status | E11–E13 |
| retired/FAIL lists mentioning P (L234 area, D1; D5) | "gauge artifact" → the owner's corrected reason | E08, E30 |
| exports line (L1371); `*PROG:TDRG-launch-gate` (L188) | the export row now names 24A → 24B → 24C and TDR-T0. Programme v1.4 §6.4 still says "recorded, not repaired": that sentence is Programme's and becomes stale against the owner — a D-STALE note on the PROG node, or a rewording of the Atlas line with both facts | E27; `programme-v1.4` unchanged |
| new L2 nodes (D5) | `TDRG-ALG-EVENT-INVENTORY`, `-NARROW-BAND-CLASSES`, `-TOKEN-CENSUS-LAW` (i–iii), `-BIRTH-SPECTRUM-INJECTION`, `-SPECCONS-N`, `-BIRTH-SPECTRUM-NOT-CLOSED`, `-PARENT-CHILD-PHASE` (`[scope:]` free two-body kinematics; not a bond or growth mechanism), `TDRG-NUM-TOKEN-LAW-CHECK` (finite check, not a proof). `TDRG-ART-TOKEN-LAW-CHECKS` as `cert`. Each credited to AZ as proposer, owned by TDR-G | §6.13 |
| TDRG pins in D5 (Programme, OFN, AZ) | Programme v1.4, OFN v0.12, AZ v0.7 (the owner's pin; the cited AZ entry is byte-identical at `az-v0.8`) | E04, E20–E24 |
| TDRG.G8, G10, G11 | G8 (layout, v2.13) stands; G10 (`largest_center`) stands, unaffected by the token laws; G11 custody: add the new artifact RID | release record §6 |
| `*AZ:B-ledger` (D5) | AZ's re-quotation is checked at the AZ edition of the build, not here | — |

## 3. AZ v0.8 (`az-v0.8`, adopted 12 Nov; file `146fcc28…ee76`)

Read for this map: the notice `pipes/ATLAS/20261112-AZ-v0-8-adopted.md`, the v0.8 version-history entry, the section list, the RID sets at `az-v0.7` and `az-v0.8`, and the entries named below. **Not yet read in full:** the v0.8 body and its release record; that reading belongs to the build.

Mechanical facts: no RID of v0.7 is missing at v0.8; five identifiers gain RID declarations (`AZ-OPEN-PROMO`, `AZ-OPEN-SCOPE-ARITH`, `AZ-OPEN-SCOPE-ZETA`, `TDRG-OPEN-TOPO-FILTER`, and the new `AZ-ART-CORE-EQUIV-CHECK`); the section numbering is unchanged (47 headings, declared section map §0.3).

| Atlas v0.12 item | Change needed | Owner basis |
|---|---|---|
| SOURCES row AZ; D2 and D5 headers | `az-v0.8`; Methodology v1.4 declared; Level A retained; no new scientific result | header, notice |
| `PROP-AZ-CORE-EQUIV` (L1354) | **grade THM-ALG → THM** on a written proof (§4.3.2); the 2,141,014-graph enumeration becomes source-reported corroboration; `cert AZ-ART-CORE-EQUIV-CHECK` (2,131,019 labelled graphs with at most 7 vertices, 0 mismatches). A grade change: its own reviewed item with owner evidence (Method §7) | v0.8 line 310, §9 |
| Thread C evidence qualifier (on `AZ-1A/1B/1C`) | rewrite from AZ §9's per-artifact availability: the ten-file AZ-1A/AZ-1B registry state deposited and replayed; AZ-1C, the Phase-2 reports and the certificates source-reported; two definitions of G_birth(w) recorded. The v0.12 sentence "none of the files is in the repository" no longer describes the owner text, and the "[SESSION] custody record" clause goes | §9, notice |
| `TDRG-AZ-STATIC-ZN-4Q`; AZ.A5 (two rows) | AZ side narrowed: the static-geometry reading is stated for the tested null protocol only (SG-AZ-7, §4.3.5). Both guards stand; AZ.A5 is kept and its AZ clause reworded | §4.3.5, notice |
| `*AZ:A-ledger`, `*AZ:B-ledger`, `*AZ:A-heur` | owner statements are now cited once, in AZ §8: locators `@AZ§4.1`, `@AZ§4.2` → `@AZ§8`; Dyadic pin `dyad-v6.4.24`; TDR-G context pin as AZ states it; the HEUR reading (§4.1.3) unchanged | §8 headings |
| PROG.G6 (L250) | AZ has now done the Methodology v1.4 migration and the §6.7 reduction: the v0.12 parenthesis ("not the §9.2 pass") is replaced | release record |
| METH.M1 (L251) | AZ's compound grades: three occurrences of the patterns remain in the v0.8 text; check whether they are current grades or history before removing AZ from the row | to verify at build |
| H2, OPENM.U11, the UVM audit node | AZ §6 keeps the verdict sentence; only the edition label "v0.7" in those lines moves | notice |
| D5.L3 AZ frontier line | `AZ-OPEN-*` now have RID declarations; no content change expected | RID diff |

## 4. AZ v0.9 candidate — provisional (PR #253, `e51fa3e62a`; not adopted)

| Candidate content | Planned Atlas treatment, if adopted as it stands |
|---|---|
| `AZ-NUM-TOKRES-S1`, `[NUM diagnostic]`, §4.2.1, owned by AZ; scope: pinned TDR-G engine with `TDRG-DEF-ORIENT`, policy `bound_symmetric`, N ∈ {120, 122}, k = 8, four initial nodes, 800 ticks, node cap 300, endpoint M ≥ 100; `[conv:]` orientation reference of TDR-G v2.12.14 | **one node, in the AZ block of D5**, grade as the owner prints it, the full scope and convention carried; negatives from the owner text ("not a TDR-G result, not a bridge, no bridge-candidate promoted"); `cert AZ-ART-TOKRES-S1` |
| relation to TDR-G | edges only: `<TDRG-ALG-PARENT-CHILD-PHASE`, `<TDRG-ALG-TOKEN-CENSUS-LAW`, `<TDRG-DEF-ORIENT`. The `[ALG]` laws are **not** restated in the AZ block and the diagnostic is **not** repeated in the TDR-G block. TDR-G v2.12.15 says the Stage 1 numbers are not part of its results; the Atlas keeps that negative on the TDR-G nodes |
| AZ-OPEN-PROMO, AZ-OPEN-SCOPE-ARITH | whatever the adopted text says about them; no inference by the Atlas from the diagnostic to a promotion |
| Stage 2 (PR #251) | [SESSION]; not atlas content |

## 5. Checks the build will have to pass (beyond the shared checker)

- A provisional run of the shared checker on the v0.12 text against a manifest with the two moved tags fails only in the two SOURCES rows. The checker's coverage check extracts Dyadic RIDs only, so **it does not see the nine new TDR-G RIDs or the AZ changes**. The builder therefore asserts, for TDR-G and AZ: every RID that is new at the tag has exactly one home (node or `cert`), and no RID present at the old tag is absent at the new one.
- Focused negative controls planned: K₁,₃-only star restored; "gauge" restored as the reason for P; TDR-6 shown closed; the signed-class invariant shown as closing TDR-6; `SPECCONS-N` shown as holding across births; the phase law shown as a bond or growth mechanism; `PROP-AZ-CORE-EQUIV` left at THM-ALG; the enumeration shown as the proof; the `4|q` verdict shown beyond the tested protocol; the diagnostic placed under a TDR-G RID or the `[ALG]` laws under an AZ RID; a Stage 1 number on a TDR-G node.
- Method §4.1 and §4.7 are applied as span deletions in D5 only (the domain that is opened), each logged with its rule.

## 6. Freeze rule

The source manifest is frozen only when `az-v0.9` exists as an annotated tag with its release record, or when the PI decides to refresh without it. Until then the open `pipes/ATLAS/` item (AZ v0.8) stays open; it is dispositioned with the build.
