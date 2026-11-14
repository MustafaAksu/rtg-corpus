# Atlas check report

atlas: `atlas/RTG_STATE_ATLAS.md` sha256 `47384c0c6959392e786829e4435a62b52d76aa38c19d655fe9f7890ac86160a1`; manifest `evidence/atlas/v0.13/source_manifest.json`

| check | PASS | FAIL | UNVERIFIED | other |
|---|---|---|---|---|
| sources | 72 | 0 | 0 | — |
| coverage | 137 | 0 | 0 | — |
| qualifiers | 4 | 0 | 0 | — |
| links | 525 | 0 | 2 | DOCUMENTED-UNRESOLVED 10 |
| artifacts | 120 | 0 | 2 | — |
| keys | 154 | 0 | 0 | — |
| process | 0 | 0 | 0 | — |
| wording | 0 | 0 | 0 | WARN 13 |

Unparsed or unchecked items are not PASS. Scope notes: the qualifier check covers DYAD declarations carrying `[assuming: …]` only; script checks establish naming in the owner file, not file availability or execution; content fidelity is a matter for the change-focused review. Separate limitation (not a checker row): byte equality of 13 sources with the atlas v0.1 extraction input is UNVERIFIED (manifest `v0_1_input_equality`).

## UNVERIFIED (4)

- links · NUMGEN-ART-ROTNUM-OBSTRUCTION — present in NUMGEN but not in a recognized declaration form
- links · NUMGEN-CAND-N5AS1-LOGSLIP — present in NUMGEN but not in a recognized declaration form
- artifacts · cm.py — line 937: named in a source other than the line owner (GEN)
- artifacts · fit.py — line 937: named in a source other than the line owner (GEN)

## DOCUMENTED-UNRESOLVED (10)

- links · DYAD-ALG-CASCADE-P12 — DYAD consumer_string: unmatched; p=12 micro-certification value has no RID (App F); cited only in L5 or marked unresolved
- links · DYAD-ALG-PHASELAW — DYAD historical_label: historical note label; superseded finite-horizon law, part of DYAD-THM-Q403-PHASELAW (App F); cited only in L5 or marked unresolved
- links · DYAD-ART-CASCADE-Q4-03 — DYAD consumer_string: artifact string; content matches DYAD-ART-Q403-EXTRACT, no byte identity (App F); cited only in L5 or marked unresolved
- links · DYAD-CAND-PHISTAR-ENTRY-PHASE — DYAD denied: never a Dyadic identifier (DYAD current-grade lookup); cited only in L5 or marked unresolved
- links · DYAD-CF-Q403 — DYAD consumer_string: component of PHASELAW (App F); cited only in L5 or marked unresolved
- links · DYAD-THM-LEAD — DYAD consumer_string: component of PHASELAW (App F); cited only in L5 or marked unresolved
- links · DYAD-THM-P1 — DYAD consumer_string: component of DYAD-THM-Q403-PHASELAW, no separate RID (App F); cited only in L5 or marked unresolved
- links · DYAD-THM-Q403-PHASE-ALLP — DYAD historical_label: historical note label; theorem DYAD-THM-Q403-PHASELAW (App F); cited only in L5 or marked unresolved
- links · DYAD-THM-R — DYAD consumer_string: component of PHASELAW (App F); cited only in L5 or marked unresolved
- links · DYAD-THM-REALITY — DYAD consumer_string: component of PHASELAW (App F); cited only in L5 or marked unresolved

## WARN (13)

- wording · line 223 — "pending": …GIIL) · RER Stage-2 global certificate (pending, uninspected)…
- wording · line 549 — "now": …or · reblocking "vanishes identically" (now 0≤Δ<m)…
- wording · line 729 — "was": …er (DYAD: DYAD-CAND-PHISTAR-ENTRY-PHASE was never a Dyadic identifier) | @§1,§6.13b…
- wording · line 818 — "resolved": …onditional; RECOG side of sign question resolved negatively by RECOG-ALG-SHEAR-ORIENTATI…
- wording · line 1104 — "pending": … record-level "Registry/owner adoption: pending" lines and frozen r3.1 contract cells m…
- wording · line 1147 — "resolved": …le-node exact; projection nontriviality resolved; exact scalar susceptibility derived; p…
- wording · line 1147 — "was": …ent governing the critical lift: ALG·s (was THM); resonance-assisted saddle-node: H…
- wording · line 1147 — "was": …t THM); projection nontriviality: OPEN (was RES) | RET (no RID): soft mode governs …
- wording · line 1256 — "pending": …TALE: the UVM §6 header says R1–R6 are "pending PI audit before any export to Genesis";…
- wording · line 1286 — "RESOLVED": …NV-AZ-GRAPH-EXPORT (AZ-OPEN-EDGE-EXPORT RESOLVED) DEF | symmetric defect pair {a,b} expo…
- wording · line 1320 — "RESOLVED": …G-OPEN-STRUCT-SLOT-PROJECTION (TDR-24F) RESOLVED mechanism NUM strong | ψ_slot~N^{+0.01}…
- wording · line 1329 — "resolved": …TOPO-FILTER (TDR-24A) ACTIVE, mechanism-resolved, BLOCKS TDR-T | C_component=(occ_in_cs/…
- wording · line 1375 — "resolved": …census and pairwise-difference multiset resolved as a predictable-change law (TDRG-ALG-T…
