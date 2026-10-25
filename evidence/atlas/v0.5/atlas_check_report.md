# Atlas check report

atlas: `atlas/RTG_STATE_ATLAS.md` sha256 `cf250c9140e6ee26c65b2497a2a61dc1e326a69574d590132f0cea9646a2b0e5`; manifest `evidence/atlas/v0.5/source_manifest.json`

| check | PASS | FAIL | UNVERIFIED | other |
|---|---|---|---|---|
| sources | 72 | 0 | 0 | — |
| coverage | 128 | 0 | 0 | — |
| qualifiers | 3 | 0 | 0 | — |
| links | 419 | 0 | 4 | DOCUMENTED-UNRESOLVED 11 |
| artifacts | 99 | 0 | 3 | — |
| keys | 77 | 0 | 0 | — |
| process | 0 | 0 | 0 | — |
| wording | 0 | 0 | 0 | WARN 16 |

Unparsed or unchecked items are not PASS. Scope notes: the qualifier check covers DYAD declarations carrying `[assuming: …]` only; script checks establish naming in the owner file, not file availability or execution; content fidelity is a matter for the change-focused review. Separate limitation (not a checker row): byte equality of 13 sources with the atlas v0.1 extraction input is UNVERIFIED (manifest `v0_1_input_equality`).

## UNVERIFIED (7)

- links · AZ-OPEN-PROMO — present in AZ but not in a recognized declaration form
- links · AZ-OPEN-SCOPE-ARITH — present in AZ but not in a recognized declaration form
- links · AZ-OPEN-SCOPE-ZETA — present in AZ but not in a recognized declaration form
- links · NUMGEN-ART-ROTNUM-OBSTRUCTION — present in NUMGEN but not in a recognized declaration form
- artifacts · cm.py — line 946: named in a source other than the line owner (GEN)
- artifacts · fit.py — line 946: named in a source other than the line owner (GEN)
- artifacts · prove_core_equiv.py — line 1357: named in a source other than the line owner (None)

## DOCUMENTED-UNRESOLVED (11)

- links · DYAD-ALG-CASCADE-P12 — DYAD consumer_string: unmatched; p=12 micro-certification value has no RID (App F); cited only in L5 or marked unresolved
- links · DYAD-ALG-PHASELAW — DYAD historical_label: historical note label; superseded finite-horizon law, part of DYAD-THM-Q403-PHASELAW (App F); cited only in L5 or marked unresolved
- links · DYAD-ALG-Q3-CANCEL — DYAD consumer_string: unmatched; statement = DYAD-ALG-Q3-DEG2-CANCEL (App F); cited only in L5 or marked unresolved
- links · DYAD-ART-CASCADE-Q4-03 — DYAD consumer_string: artifact string; content matches DYAD-ART-Q403-EXTRACT, no byte identity (App F); cited only in L5 or marked unresolved
- links · DYAD-CAND-PHISTAR-ENTRY-PHASE — DYAD denied: never a Dyadic identifier (DYAD current-grade lookup); cited only in L5 or marked unresolved
- links · DYAD-CF-Q403 — DYAD consumer_string: component of PHASELAW (App F); cited only in L5 or marked unresolved
- links · DYAD-THM-LEAD — DYAD consumer_string: component of PHASELAW (App F); cited only in L5 or marked unresolved
- links · DYAD-THM-P1 — DYAD consumer_string: component of DYAD-THM-Q403-PHASELAW, no separate RID (App F); cited only in L5 or marked unresolved
- links · DYAD-THM-Q403-PHASE-ALLP — DYAD historical_label: historical note label; theorem DYAD-THM-Q403-PHASELAW (App F); cited only in L5 or marked unresolved
- links · DYAD-THM-R — DYAD consumer_string: component of PHASELAW (App F); cited only in L5 or marked unresolved
- links · DYAD-THM-REALITY — DYAD consumer_string: component of PHASELAW (App F); cited only in L5 or marked unresolved

## WARN (16)

- wording · line 186 — "pending": …ed at declared scope; 24A→24B→24C→TDR-T pending; owner App. C still older D/A/B gate, R…
- wording · line 221 — "pending": …GIIL) · RER Stage-2 global certificate (pending, uninspected)…
- wording · line 232 — "pending": …n sum as conserved — rejection withheld pending TDRG…
- wording · line 244 — "was": ….4.16 (lifecycle-only)", RF-O10-04 "N12 was not read for this draft", §0.1 "v0.10 D…
- wording · line 551 — "now": …or · reblocking "vanishes identically" (now 0≤Δ<m)…
- wording · line 741 — "was": …er (DYAD: DYAD-CAND-PHISTAR-ENTRY-PHASE was never a Dyadic identifier) | @§1,§6.13b…
- wording · line 827 — "resolved": …onditional; RECOG side of sign question resolved negatively by RECOG-ALG-SHEAR-ORIENTATI…
- wording · line 1108 — "pending": …1 says CN-01–CN-05 "consumer acceptance pending" while §7.4 records dispositions.…
- wording · line 1114 — "pending": … record-level "Registry/owner adoption: pending" lines and frozen r3.1 contract cells m…
- wording · line 1155 — "resolved": …le-node exact; projection nontriviality resolved; exact scalar susceptibility derived; p…
- wording · line 1155 — "was": …ent governing the critical lift: ALG·s (was THM); resonance-assisted saddle-node: H…
- wording · line 1155 — "was": …t THM); projection nontriviality: OPEN (was RES) | RET (no RID): soft mode governs …
- wording · line 1264 — "pending": …TALE: the UVM §6 header says R1–R6 are "pending PI audit before any export to Genesis";…
- wording · line 1289 — "RESOLVED": …NV-AZ-GRAPH-EXPORT (AZ-OPEN-EDGE-EXPORT RESOLVED) DEF | symmetric defect pair {a,b} expo…
- wording · line 1315 — "RESOLVED": …G-OPEN-STRUCT-SLOT-PROJECTION (TDR-24F) RESOLVED mechanism NUM strong | ψ_slot~N^{+0.01}…
- wording · line 1324 — "resolved": …TOPO-FILTER (TDR-24A) ACTIVE, mechanism-resolved, BLOCKS TDR-T | C_component=(occ_in_cs/…
