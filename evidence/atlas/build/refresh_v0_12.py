#!/usr/bin/env python3
"""Atlas v0.11 -> v0.12 candidate: impact refresh for two moved sources — Arithmetic Resonance and Zeta v0.7
(`az-v0.7`, adopted 11 Nov 2026; corrections only) and Dyadic Oscillator v6.4.24 (`dyad-v6.4.24`, adopted 11 Nov 2026) —
and the two items of pipes/ATLAS/ that announce them. Change-focused; the other 16 sources are not re-extracted.

AZ (D5, D2 edges, D4b edges, H2, H3): the v0.6 "legal ×2" sentence is withdrawn in the owner text (AZ.A1 retired; the
D-WRONG list is empty); DYAD-THM-Q403-PHASELAW is an import-ref and the Genesis pointers are current (AZ.A2 retired);
the Programme request is closed (AZ.A3 retired); consumer strings are owner RIDs (AZ.A7 retired; DZT.Q1 keeps the DZT
half); the raw-cubic import carries the owner caveat (DYAD.X11 retired). AZ.A5 stays. Thread C nodes keep statements and
grades; AZ §9's availability statement becomes an evidence qualifier.
DYAD (D2): three results get owner RIDs (pseudo-IDs replaced; not-area-preserving THM -> ALG as the owner retagged it);
DYAD.X4 narrowed to the one statement still without a Dyadic RID; new node DYAD-THM-OPEN21-SHARP-ROWS (conditional);
the OPEN 20 frontier line carries the owner's [SESSION] state-of-work paragraph, no result claimed.
Pipes: NUMGEN.N-I1 restated at the new snapshot.
Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_12.py
"""
from __future__ import annotations
import hashlib, importlib.util, json, re, subprocess, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.12'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = 'c8e71980d053545edcc2f4d1fc5ccf92460de48f'   # main after PR #219
BASE_TAG = 'atlas-v0.11'
BASE_SHA = '8d7a43f05a42c6a69b50eb97b98dd96ddda7eea327333ae5cc73e03dee46f358'
MOVED = {'AZ': dict(edition='v0.7', tag='az-v0.7', authority='OWNER: release record `records/az/AZ_v0_7_RELEASE_RECORD.md` (PI adopted 11 Nov 2026)'),
         'DYAD': dict(edition='v6.4.24', tag='dyad-v6.4.24', authority='OWNER: release record `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md` (+ `records/dyad/DYAD_v6_4_24_POST_TAG.md`)')}
SHAS = {'AZ': '2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94',
        'DYAD': '10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16'}
NEW_RIDS = {'DYAD': ['DYAD-ALG-NOT-AREA-PRESERVING', 'DYAD-ALG-P6-LINEAR-ORDER', 'DYAD-ALG-HOMOLOGICAL-RESONANCE', 'DYAD-THM-OPEN21-SHARP-ROWS',
                     'DYAD-ART-OPEN21-SHARP-ROWS', 'DYAD-ART-BRIDGE-NOTE-CHECK', 'DYAD-ART-OPEN20-AN-PILOT']}
PIPE_SNAPSHOT = {'closed': 52, 'dispositioned': 4, 'open': 51}
ATLAS_ITEMS = ['pipes/ATLAS/20261111-AZ-v0-7-adopted.md', 'pipes/ATLAS/20261111-DYAD-v6-4-24-adopted.md']
PATHS = ['records/az/AZ_v0_7_RELEASE_RECORD.md', 'records/az/AZ_REACTIVATION_TRIAGE.md', 'records/az/AZ_UPLOAD_HASH_CHECK_20261111.md',
         'records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md', 'records/dyad/DYAD_v6_4_24_POST_TAG.md',
         'evidence/dyad/scripts/dyad_s1_open21_sharp_rows_cert.py', 'evidence/dyad/scripts/dyad_bridge_note_v1_1_check.py'] + ATLAS_ITEMS

def _load(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
R10 = _load('refresh_v0_10')   # reused helpers only: Edit, h_l5_map, checker, pipe_states, git, sha, at, wjson
git, sha, at, wjson, h_l5_map, checker, pipe_states = R10.git, R10.sha, R10.at, R10.wjson, R10.h_l5_map, R10.checker, R10.pipe_states

class Edit(R10.Edit):
    def rep(self, old, new, finding, where):
        super().rep(old, new, finding, where); self.log[-1]['id'] = f'AR12-{len(self.log):03d}'

IMPORT_SHARP = 'pin recog-v0.3.26 §6.13a; the entry is byte-identical at recog-v0.3.27'

def refresh(a: Edit):
    I, Z, D, P = 'identity', 'AZ v0.7', 'DYAD v6.4.24', 'pipes'
    # ---- identity ----
    a.rep('# RTG STATE ATLAS v0.11\n', '# RTG STATE ATLAS v0.12\n', I, 'title')
    a.rep('evidence/atlas/v0.11/source_manifest.json', 'evidence/atlas/v0.12/source_manifest.json', I, 'SOURCES header')
    a.rep('*END — RTG STATE ATLAS v0.11.', '*END — RTG STATE ATLAS v0.12.', I, 'end line')
    a.line('| DYAD | RTG_DYADIC_OSCILLATOR_DSN | v6.4.23 |', '| DYAD | RTG_DYADIC_OSCILLATOR_DSN | v6.4.24 | `dyad-v6.4.24` | canonical Tier 3 |', I, 'SOURCES row DYAD')
    a.line('| AZ | RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN | v0.6 |', '| AZ | RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN | v0.7 | `az-v0.7` | canonical Tier 5 |', I, 'SOURCES row AZ')
    a.rep('(sources: DYAD v6.4.23 · NUMGEN v1.21', '(sources: DYAD v6.4.24 · NUMGEN v1.21', I, 'D2 header, DYAD')
    a.rep('· DZT v0.8 · AZ v0.6 Thread A.', '· DZT v0.8 · AZ v0.7 Thread A.', I, 'D2 header, AZ')
    a.rep('AZ = RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN v0.6 (June 2026, Tier 5, Level A retained)',
          'AZ = RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN v0.7 (11 Nov 2026 corrections edition of the June 2026 v0.6 text: pins, identifiers and owner corrections, Thread C byte-identical; Methodology v1.2 declared, the v1.4 migration is a separate edition; Tier 5, Level A retained)', I, 'D5 header, AZ')

    # ---- AZ.A1: the ×2 sentence is withdrawn in the owner text ----
    a.line('H2 D-WRONG/D-LINK high —', 'H2 D-LINK high — no certified OPEN-M deficit: the chain 0.024 target → 4/125 → ρ≥16/5 → R15 0.007–0.008 is one node *UVM:deficit-chain (D4b) with verdict "no certified deficit"; PROG does not adopt the "2× short" headline; AZ v0.7 §6 states the same verdict (OPENM.U2, U11; DYAD.X8).', Z, 'H2 without the AZ conflict')
    a.line('AZ.A1 | AZ §6 "To OPEN M": legal deficit correction ×2 (not ×4)', '(none at this edition)', Z, 'D-WRONG list: AZ.A1 leaves; the list is empty')
    a.sub_in_line('UVM-RESULT-AUDIT1 (R16) COR |', '| ! AZ "legal ×2 correction" (D5, D-WRONG AZ.A1) |', '| >AZ §6 (v0.7 cites R15/R16 as stated; its v0.6 "legal ×2" sentence is withdrawn, AZ App. B) |', Z, 'UVM deficit node: AZ edge')
    a.sub_in_line('OPENM.U11 ~ D-LINK:', 'AZ\'s "legal ×2 correction" (D-WRONG AZ.A1) contradicts R16\'s SUPERSEDED verdict.', 'AZ v0.7 §6 cites R15/R16 as stated; its v0.6 "legal ×2" sentence is withdrawn (AZ App. B).', Z, 'OPENM.U11: AZ clause')
    a.drop_line('AZ.A1 D-WRONG (high; ≡ OPEN-M U2 chain):', Z, 'AZ.A1 retired (D5.L5)')

    # ---- AZ.A2: Q403 phase law imported as closed; Genesis pointers current ----
    a.sub_in_line('DYAD-THM-Q403-PHASELAW THM', 'AZ (lists as open: stale, L5 AZ.A2)', 'AZ (import-ref at az-v0.7 §4.1.1, §8)', Z, 'Q403 node: AZ consumer')
    a.drop_line('AZ.A2 D-STALE (Thread A) |', Z, 'AZ.A2 retired (D2.L5 row)')
    a.drop_line('AZ.A2 D-STALE: §4.1.2', Z, 'AZ.A2 retired (D5.L5 row)')

    # ---- AZ.A3: Programme request closed ----
    a.sub_in_line('AZ: AZ-OPEN-SCOPE-ZETA', ' · *AZ:programme-patch-request (register AZ as Tier 5; DONE in PROG v1.2)', '', Z, 'D5.L3: closed request leaves the frontier line')
    a.drop_line('AZ.A3 D-STALE:', Z, 'AZ.A3 retired')
    a.sub_in_line('PROG.G6 D-STALE (owner-recorded):', 'and not executed for Pre-Legacy, DZT, AZ;', 'and not executed for Pre-Legacy, DZT, AZ (since then AZ v0.7, 11 Nov 2026: a corrections edition, by its release record not the §9.2 pass — no Methodology migration, no restructuring);', Z, 'PROG.G6: AZ state after the Programme snapshot')

    # ---- AZ.A7: consumer strings are owner RIDs ----
    a.line('H3 D-RID high —', 'H3 D-RID high — consumer strings that are not owner RIDs: DZT cites DYAD-THM-Q403-PHASE-ALLP and DYAD-ALG-PHASELAW (historical note labels; owner theorem DYAD-THM-Q403-PHASELAW), DYAD-THM-P1, -REALITY, -LEAD, -R, DYAD-CF-Q403 (components of PHASELAW, no separate RID), DYAD-ALG-CASCADE-P12 (unmatched) and DYAD-ART-CASCADE-Q4-03 (content = DYAD-ART-Q403-EXTRACT, no byte identity). The owner classifies each string (DYAD App F) and creates no aliases; DZT cites them unchanged (DZT.Q1). AZ repinned to the owner RIDs in v0.7. PROG cites the correct PHASELAW.', Z, 'H3: DZT half only')
    a.sub_in_line('DZT.Q1 D-RID |', ' AZ cites DYAD-ALG-Q3-CANCEL (statement = DYAD-ALG-Q3-DEG2-CANCEL). DYAD App F classifies all strings and creates no aliases. Fix: DZT and AZ repin.', ' DYAD App F classifies all strings and creates no aliases. Fix: DZT repins. (AZ repinned in v0.7.)', Z, 'DZT.Q1: AZ half done')
    a.sub_in_line('DYAD-ALG-Q3-DEG2-CANCEL ALG', '| AZ prints DYAD-ALG-Q3-CANCEL (not a DYAD RID; DYAD App F maps it here, no alias) |', '| >AZ (import-ref under this RID since az-v0.7; the eigenframe linear-part lemma\'s statement is not recovered at the owner, DYAD App D) |', Z, 'Q3 node: AZ consumer')
    a.sub_in_line('TDRG-DEF-ZN-STATE DEF (alias TDRG-ZN-STATE; v2.12.14) |', 'AZ\'s "TDRG-ZN-STATE" resolves through the v2.12.14 §7 alias map', 'AZ cites TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE and TDRG-DEF-BAND since az-v0.7 (the consumer name "TDRG-ZN-STATE" resolves through the v2.12.14 §7 map)', Z, 'TDRG state node: AZ citation')
    a.line('*AZ:B-ledger (restatement; edges only) |', '*AZ:B-ledger (restatement; edges only; owner RIDs since az-v0.7) | AZ Thread B re-quotes TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE, TDRG-DEF-BAND, TDRG-THM-REACHABILITY-K0, TDRG-ALG-LEM-REACH, TDRG-ALG-LEM-RETRIG (bound state of period dividing 2; least period 2 for d≠0), TDRG-ALG-LEM-SPECCONS (gcd multiset a consequence only; converse fails), BIND3 (TDRG-ALG-BIND3-CYCLE-N24K1, TDRG-NUM-BIND3-PARITY, TDRG-NUM-BIND3-SPECTRAL-GATE, TDRG-NUM-BIND3-MEMORY-PARITY, TDRG-NUM-BIND3-XFER, TDRG-NUM-BIND3-REGEN: isolated period-2 not persistent, multi-pair scattering, even-parity survival, KNIFE FAIL, odd-memory COR; conv v18 path orientation, not rerun by the owner), k/N growth control, *TDRG:bulk-fits (full-range 0.869; window-dependent, N^{−0.730} on N=480–1440; not a structural constant), TDR-26 rule (TDRG-OPEN-LOCKING-FAIL), TDR-24 frontier (24A → 24B → 24C); all as bridge-candidate @AZ§4.2', Z, 'AZ Thread B ledger at v0.7')
    a.drop_line('AZ.A7 D-RID:', Z, 'AZ.A7 retired')

    # ---- Thread A ledger; DYAD.X11 ----
    a.line('*AZ:A-ledger (→ D2 reference-only edges) |', '*AZ:A-ledger (→ D2 reference-only edges; pin dyad-v6.4.23 since az-v0.7) | DYAD raw cubic (raw one-step map, p≥3; carried with the owner caveat on the historical proposition), P567 ledger, GLATTICE5, VANISH-B2/B3/B4, B5-ALLP-NONVANISHING (DYAD-OPEN-B5-ALLP named as the closed lifecycle identifier), DIRECT-WEIGHT, CROSS-IDENTITY, Q3-DEG2-CANCEL, Q403-PHASELAW (closed; import-ref), subgroup-charge 𝒬(p) (named sub-items of DYAD-OPEN-P-RESONANCE; eight projector objects not recovered at the owner), P6-FACEFLUX; *AZ:A-heur "operative arithmetic = divisor structure, subgroup charge, cyclotomic cancellation, not primality" @AZ§4.1', Z, 'AZ Thread A ledger at v0.7')
    a.sub_in_line('*AZ:A-heur HEUR |', '(pin v6.4.8.1)', '(pin dyad-v6.4.23 since az-v0.7)', Z, 'A-heur: pin')
    a.sub_in_line('DYAD-ALG-B5-ALLP-NONVANISHING ALG', '| >DZT, AZ (both cite the lifecycle RID) |', '| >DZT (cites the lifecycle RID), AZ (cites this RID since az-v0.7) |', Z, 'B5 node: consumers')
    a.sub_in_line('DYAD-THM-RAW-CUBIC', 'identity with the historical OPEN-9 proposition not established (L5 DYAD.X11) | >AZ Thread A |', 'identity with the historical OPEN-9 proposition not established | >AZ Thread A (az-v0.7 imports it at this scope, with the caveat) |', Z, 'raw cubic node: AZ import at owner scope')
    a.drop_line('DYAD.X11 D-LINK |', Z, 'DYAD.X11 retired')

    # ---- Thread C evidence qualifier (AZ §9 at v0.7) ----
    a.sub_in_line('AZ-1A/1B/1C ENG PASS |', ' → AZ-ART-SPECTRAL-RADIUS-PATCH @AZ', ' → AZ-ART-SPECTRAL-RADIUS-PATCH | evidence (AZ v0.7 §9): none of the Thread C files, the hash registry AZ-ART-AZV5-REGISTRY included, is in the repository at this edition and none is described as recreated (EV-SRC-REPORTED, EV-NOT-RERUN); the owner keeps the grades with that limit, which holds for every AZ-owned node of this block; a later [SESSION] custody record (records/az/AZ_UPLOAD_HASH_CHECK_20261111.md) is not owner text and changes nothing here @AZ', Z, 'Thread C: availability qualifier')
    a.rep('not supported by AZ v0.6;', 'not supported by AZ v0.7;', Z, 'PREL/Legacy routing row: AZ edition (AZ v0.7 does not mention CHSH)')

    # ---- DYAD: three registrations ----
    a.line('*DYAD:not-area-preserving THM |', 'DYAD-ALG-NOT-AREA-PRESERVING ALG | det DT=1+(e^ρ−1)cosη; =1 only on ρ=0 or cosη=0, not globally; non-symplecticity lets Q_true decay | owner tag ALG (a direct Jacobian computation); THM in editions before v6.4.24, content unchanged | cert DYAD-ART-BRIDGE-NOTE-CHECK (gate B2; exact replay of DYAD-ART-BRIDGE-NOTE) | @DYAD§1,§6.1', D, 'RID registered; THM -> ALG')
    a.line('*DYAD:p6-linear-order ALG |', 'DYAD-ALG-P6-LINEAR-ORDER ALG | λ=e^{iπ/3} has order exactly 6 (λ^j≠1, j=1..5; λ⁶=1); linear part only; holds for every primitive root of unity, not a uniqueness property of p=6 | cert DYAD-ART-BRIDGE-NOTE-CHECK (gate B3) | @DYAD§6.6', D, 'RID registered')
    a.sub_in_line('*DYAD:homological-resonance ALG |', '*DYAD:homological-resonance ALG |', 'DYAD-ALG-HOMOLOGICAL-RESONANCE ALG |', D, 'RID registered')
    a.line('DYAD.X4 D-RID |', 'DYAD.X4 D-RID | one statement is used downstream without a Dyadic RID: the cubic radial rate across p (*DYAD:cubic-rate-across-p), which the owner keeps as a statement-level import of RECOG-ALG-NU3-CLOSED-FORM (owner decision, dyad-v6.4.24). The other three statements of this row have owner RIDs since v6.4.24: DYAD-ALG-NOT-AREA-PRESERVING, DYAD-ALG-P6-LINEAR-ORDER, DYAD-ALG-HOMOLOGICAL-RESONANCE.', D, 'DYAD.X4 narrowed')
    # ---- DYAD: new conditional theorem ----
    a.after_line('DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER THM·c |', [
        'DYAD-THM-OPEN21-SHARP-ROWS THM·c | sc: as DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER — rows A, B of NF-REM, not mixed; primitive start W₀, 0<|W₀|≤w_j; 𝒫₂, M_W, w_j as there | if RECOG-THM-R9-SHARPENED-ROWS: |M_W−𝒫₂(W₀)|≤K′_jQ₀^{3/2}+C′_{2,j}(256/225)²Q₀² (primary) and ≤S_jQ₀^{3/2} (secondary); row A w=3/64: K′=3951/1000 (unchanged), C′₂=259.2, S=492/25 (adopted single K=8831/250); row B w=3/128: K′=971/250, C′₂=81.49, S=6357/1000 (adopted 883/100); S_j = three-decimal ceiling of K′_j+C′_{2,j}(256/225)²w_j (exact 19.67964, 6.356466963…) | ¬ unconditional; rows not mixed; RECOG\'s −C7 rows are not imported; DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER and its rows are unchanged | cert DYAD-ART-OPEN21-SHARP-ROWS (exact rationals, gates G0–G5, five negative controls; OWNER-RUN; RECOG\'s certificate not rerun) | <RECOG-THM-R9-SHARPENED-ROWS (' + IMPORT_SHARP + ') | @DYAD§6.14'], D, 'new node: sharpened R9 rows')
    # ---- DYAD: OPEN 20 state of work ----
    a.sub_in_line('**smooth/analytic realization** DYAD-OPEN-INVOLUTION-REALIZATION (OPEN 20) PARTIAL:', ' Quantitative: finite-C^k / quantitative-radius smooth embedding.',
                  ' Quantitative: finite-C^k / quantitative-radius smooth embedding. State of work on B-an at v6.4.24 (owner [SESSION] paragraph; no result claimed): sectorial pilot in the complexified raw frame — F=T⁶ has two formal invariant curves Γ_± (w=a_±z²+…), exchanged by T; stage 1 exact (OWNER-RUN): k=3, m=2, α=−102/19−16√3i/19 on both branches; literature basis at SESSION scope (3-summability of Γ_±; not a theorem-grade import; the statements concern the complexified germ only, no real-orbit statement follows); stage 2 [NUM]: coefficients a₂..a₂₁₆ of Γ_+, Borel scale INCONCLUSIVE; stage 3a: the a-priori operator route is negative (it admits only |ξ|<1.76·10⁻⁶); stage 2b [NUM] scouting on one branch, one overlap, one direction, no certified truncation bound: the two sectorial values differ numerically, slopes consistent with e^{−2πT}, no asymptotic exponent certified. By the pilot\'s decision rule a certified nonzero sectorial jump would give divergence of Γ_± and of log F and would not decide B-an or B-6; both stay ACTIVE; no certification run is authorized (evidence DYAD-ART-OPEN20-AN-PILOT, SESSION working evidence; no theorem rests on it).', D, 'OPEN 20: owner state-of-work paragraph')

    # ---- pipes census at the new snapshot ----
    a.line('NUMGEN.N-I1 D-LINK (pipe states, receiver side) |', 'NUMGEN.N-I1 D-LINK (pipe states, receiver side) | at the source snapshot c8e7198, pipes_index --check passes with 107 items in 20 inboxes — 52 closed, 4 dispositioned (among them the two ATLAS notices this edition answers: AZ v0.7, DYAD v6.4.24; closed by the atlas owner after the tag), 51 open. Open at the snapshot, by receiver: DZT (DYAD N16–N21, AZ v0.7) · ER2B (OFN v0.11, DYAD N16–N21) · FMS (OFN v0.11, v0.12) · GEN (LIT Regge interface inputs, PROG v1.4, DYAD v6.4.24) · LIT (two DYAD items: LH2012 Thm 4.2 uniqueness use, v6.4.24 use report) · NUMGEN (TDR-G v2.12.14, RECOG v0.3.26 and v0.3.27, DYAD v6.4.23 and v6.4.24, OFN v0.11 and v0.12, PROG v1.4) · OFN (DYAD v6.4.23 and v6.4.24, GEN v2.10, TRIAD v1.7, PROG v1.4, RECOG v0.3.27) · PREL (SAT finding on K₃ degeneracy and lift) · PROG (SAT satellite interface, AZ v0.7) · RECOG (DYAD v6.4.24) · RER (RECOG v0.3.26, DYAD N16–N21) · RRF (RECOG v0.3.26, OFN v0.11 and v0.12, DYAD N16–N21, GEN v2.10, TRIAD v1.7) · TDRG (OFN token-sum label finding, OFN v0.11, PROG v1.4, AZ v0.7) · TRIAD (DYAD bridge-note recovery, GEN 𝒫₄-identity and birth-symmetry answers, GEN v2.10, PROG v1.4, DYAD v6.4.24; F30) · UVM (GEN κ_f/B_*/sourced-junction items, DYAD N16–N21, GEN v2.10, TRIAD v1.7). AZ and DYAD have no open inbox item. A filed item is not adopted use; each receiver decides at its own checkpoint (CONVENTIONS §7).', P, 'pipe census at c8e7198')

STALE = [r'`dyad-v6\.4\.23` \|', r'\| v6\.4\.23 \| `dyad', r'`az-v0\.6` \|', r'\| v0\.6 \| `az', r'sources: DYAD v6\.4\.23', r'AZ v0\.6 Thread A', r'ZETA_DSN v0\.6 \(June',
         r'\*DYAD:not-area-preserving', r'\*DYAD:p6-linear-order', r'\*DYAD:homological-resonance', r'no RID, L5 DYAD\.X4', r'legal ×2 correction"? \(D', r'D-WRONG AZ\.A1',
         r'lists as open: stale', r'AZ prints DYAD-ALG-Q3-CANCEL', r'\*AZ:programme-patch-request', r'pin v6\.4\.8\.1', r'AZ v0\.6 §8', r'snapshot fa3db80', r'Fix: DZT and AZ repin']
def stale_editions(text):
    return [l[:90] for l in text.split('\n') if not l.startswith('*ATLAS:checked-') and any(re.search(p, l) for p in STALE)]

def node(text, prefix):
    ls = [l for l in text.split('\n') if l.startswith(prefix)]
    return ls[0] if len(ls) == 1 else ''

def scope_guards(text):
    """Owner scope that must survive in the refreshed nodes (focused, statement-level)."""
    bad = []
    s = node(text, 'DYAD-THM-OPEN21-SHARP-ROWS THM·c |')
    if 'if RECOG-THM-R9-SHARPENED-ROWS' not in s or '¬ unconditional' not in s or 'rows not mixed' not in s: bad.append('sharp rows: conditional, rows not mixed')
    if 'C′₂=259.2, S=492/25' not in s or 'C′₂=81.49, S=6357/1000' not in s: bad.append('sharp rows: constants per row')
    if '−C7 rows are not imported' not in s or 'recog-v0.3.26 §6.13a' not in s: bad.append('sharp rows: import pin and C7 exclusion')
    if 'C₂=517' not in node(text, 'DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER THM·c |'): bad.append('adopted OPEN21 node changed')
    n = node(text, 'DYAD-ALG-NOT-AREA-PRESERVING ALG |')
    if 'not globally' not in n or 'THM in editions before v6.4.24' not in n: bad.append('not-area-preserving: grade record')
    if len([l for l in text.split('\n') if l.startswith('DYAD-ALG-NOT-AREA-PRESERVING')]) != 1: bad.append('not-area-preserving: one home')
    p6 = node(text, 'DYAD-ALG-P6-LINEAR-ORDER ALG |')
    if 'linear part only' not in p6 or 'not a uniqueness property of p=6' not in p6: bad.append('p6 order: scope')
    hr = node(text, 'DYAD-ALG-HOMOLOGICAL-RESONANCE ALG |')
    if '¬ order of λ ≡ homological resonance' not in hr: bad.append('homological resonance: not the order of λ')
    x4 = node(text, 'DYAD.X4 D-RID |')
    if '*DYAD:cubic-rate-across-p' not in x4 or 'owner decision' not in x4: bad.append('X4: narrowed, not closed')
    if not node(text, '*DYAD:cubic-rate-across-p ALG (import RECOG-ALG-NU3-CLOSED-FORM'): bad.append('cubic rate keeps its pseudo-ID')
    o20 = node(text, '**smooth/analytic realization** DYAD-OPEN-INVOLUTION-REALIZATION (OPEN 20) PARTIAL:')
    if 'no result claimed' not in o20 or 'both stay ACTIVE' not in o20 or 'no asymptotic exponent certified' not in o20 or 'B-an (R₀ / F^{1/2} analytic) OPEN' not in o20: bad.append('OPEN 20: session state, nothing closed')
    c = node(text, 'AZ-1A/1B/1C ENG PASS |')
    if 'EV-SRC-REPORTED' not in c or 'is not owner text' not in c or 'the owner keeps the grades' not in c: bad.append('Thread C: availability qualifier')
    z = node(text, 'TDRG-AZ-STATIC-ZN-4Q NUM·dx / HEUR strong · bridge-disqualified |')
    if 'static ℤ_N antipodal-band geometry, not dynamics' not in z: bad.append('4|q: static geometry verdict')
    if not node(text, 'AZ.A5 ~ D-LINK / SG trap:') or not node(text, 'AZ.A5 ~ D-LINK / SG trap |'): bad.append('AZ.A5 kept (both rows)')
    u = node(text, 'UVM-RESULT-AUDIT1 (R16) COR |')
    if 'v0.6 "legal 2×" SUPERSEDED' not in u or 'AZ App. B' not in u: bad.append('UVM node: verdict kept, AZ edge at v0.7')
    q = node(text, 'DZT.Q1 D-RID |')
    if 'Fix: DZT repins.' not in q or 'DYAD-THM-Q403-PHASE-ALLP' not in q: bad.append('DZT.Q1: DZT half kept')
    al = node(text, '*AZ:A-ledger (→ D2 reference-only edges; pin dyad-v6.4.23 since az-v0.7) |')
    if 'with the owner caveat' not in al or 'not recovered at the owner' not in al: bad.append('AZ A-ledger: owner caveats')
    dw = text.split('## D-WRONG (excluded as clearly wrong; not used as nodes)\n', 1)[1].split('\n', 1)[0]
    if dw != '(none at this edition)': bad.append('D-WRONG list')
    return bad

def main():
    snap = git('rev-parse', SNAPSHOT + '^{commit}').decode().strip(); assert snap == SNAPSHOT
    base = at(BASE_TAG, ATLAS).decode(); assert sha(base) == BASE_SHA
    a = Edit(base); refresh(a); text = a.text
    assert not stale_editions(text), stale_editions(text)
    assert not scope_guards(text), scope_guards(text)
    # ---- manifest ----
    old = json.loads(at(BASE_TAG, 'evidence/atlas/v0.11/source_manifest.json'))
    m = json.loads(json.dumps(old)); m.pop('note', None)
    for s in m['sources']:
        for k in [k for k in s if k.startswith('v0_9_')]: del s[k]
    m.update(atlas='v0.12', frozen_at='2026-11-12', repository_snapshot=SNAPSHOT, previous_atlas_tag=BASE_TAG, method_tag='atlas-v0.2', method_edition='v0.2')
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_11_edition'] = prev['edition']; s['v0_11_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] in MOVED:
            mv = MOVED[s['key']]; data = at(mv['tag'], s['path'])
            s.update(edition=mv['edition'], tag=mv['tag'], commit=git('rev-parse', mv['tag'] + '^{commit}').decode().strip(), sha256=sha(data), authority=mv['authority'])
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(SNAPSHOT, s['path']), ('snapshot/tag divergence', s['key'])
        newest = git('tag', '--list', s['tag'].rsplit('-v', 1)[0] + '-v*', '--sort=v:refname').decode().split()[-1]
        assert newest == s['tag'], ('a newer source tag exists', s['key'], newest)
        s['v0_11_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_11_input_equality'] for x in m['sources']) == {'EQUAL': 16, 'CHANGED': 2}
    assert {x['key'] for x in m['sources'] if x['v0_11_input_equality'] == 'CHANGED'} == set(MOVED)
    for k, h in SHAS.items(): assert next(s for s in m['sources'] if s['key'] == k)['sha256'] == h, k
    wjson(OUT / 'source_manifest.json', m)
    # ---- H -> L5 ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys (the cumulative list of v0.10 is the base: v0.11 retired none) ----
    oldret = json.loads(at(BASE_TAG, 'evidence/atlas/v0.10/retired_l5_keys.json'))
    R = 'AZ v0.7 (az-v0.7; release record records/az/AZ_v0_7_RELEASE_RECORD.md §3'
    newret = {'AZ.A1': R + ', triage row 1, edits E41, E57): §6 "To OPEN M" now carries the OPEN-M v0.7.1 verdict (R16 UVM-RESULT-AUDIT1 withdraws the 2× reading; no certified deficit factor; R15 a calibration-conditional diagnostic); the v0.6 sentence is recorded as withdrawn in AZ Appendix B. The owner text no longer asserts what its source withdrew.',
              'AZ.A2': R + ', rows 11, 13, 29): DYAD-THM-Q403-PHASELAW is an [import-ref] [THM] row (§4.1.1, §8) and the "exact cubic cascade formula" bullet is removed from §4.1.2; Genesis is cited at v2.10 with OPEN 1C and the reduced-model 𝒫₄ statement as two entries (§6).',
              'AZ.A3': R + ', row 28): §0.1, §6 and §7 record the registration in Programme v1.4; the patch request and the proposed entry text are removed.',
              'AZ.A7': R + ', rows 14, 19–26): DYAD-ALG-Q3-DEG2-CANCEL; TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE, TDRG-DEF-BAND, the TDR-G lemma, BIND3 and OPEN RIDs are cited; "TDRG-ZN-STATE" survives once as a named consumer string. Dyadic v6.4.24 Appendix F re-read at az-v0.7: each of AZ\'s 16 Dyadic-pattern strings is an owner RID except the closed lifecycle item DYAD-OPEN-B5-ALLP and the historical mention DYAD-ALG-Q3-CANCEL. DZT.Q1 keeps the DZT half.',
              'DYAD.X11': R + ', row 9, edits E16, E46): AZ §4.1.1 and §8 import DYAD-THM-RAW-CUBIC as the raw one-step statement for p≥3 and carry the owner caveat that the identity with the historical proposition is not established (Dyadic Appendix E). The consumer no longer cites more than the owner states; the caveat itself stays on the DYAD-THM-RAW-CUBIC node.'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    assert not set(newret) & set(oldret['retired'])
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret if '.' in k]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.12 reasons in dispositions.json. Atlas v0.11 retired no key.'))
    # ---- shared checker ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at('atlas-v0.2', 'evidence/atlas/coverage_map_v0_2.json')); cmap0 = json.loads(json.dumps(cmap))
    # Dyadic v6.4.24 §7 declares an import row for RECOG-THM-R9-SHARPENED-ROWS. Its one home in the atlas is RECOG's own record,
    # where the sharpened rows are stated inside the R9 node (D3); the Dyadic consumer node carries the edge. One reviewed shared home, no second node.
    assert 'RECOG-THM-R9-SHARPENED-ROWS' not in cmap['homes']
    cmap['homes']['RECOG-THM-R9-SHARPENED-ROWS'] = dict(home='RECOG-THM-R9-MEMORY THM |', kind='RECOG result stated inside its parent node (D3); imported by DYAD-THM-OPEN21-SHARP-ROWS')
    cmap['_note_v0_12'] = 'coverage_map_v0_2.json at atlas-v0.2 plus one shared home for the RECOG import row that dyad-v6.4.24 §7 declares.'
    wjson(OUT / 'coverage_map.json', cmap)
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.12/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    # ---- the same checker, with the same auxiliary files, on the adopted v0.11 bytes (the v0.11 record ran it with the default retired list) ----
    m11 = json.loads(at(BASE_TAG, 'evidence/atlas/v0.11/source_manifest.json')); src11 = c.load_sources(m11)
    rep11 = c.run(base, m11, src11, cmap0, idmap, oldret['retired'], with_sources=False)   # BASELINE has moved on since v0.11; identities are in the v0.11 records
    v011 = dict(atlas_sha256=sha(base), fails=len(rep11.fails()), counts={ch: dict(rep11.count(ch)) for ch in c.CHECKS}); assert not rep11.fails(), rep11.fails()
    # ---- RID presence in the tagged sources (naming check, not certificate replay) ----
    presence = {r: (('RID: ' + r) in src['DYAD']) for r in NEW_RIDS['DYAD']}; assert all(presence.values()), presence
    for r in NEW_RIDS['DYAD']: assert r in text, r
    d_old = set(re.findall(r'RID: (DYAD-[A-Z0-9-]+)', at('dyad-v6.4.23', 'dsn/RTG_DYADIC_OSCILLATOR_DSN.md').decode())); d_new = set(re.findall(r'RID: (DYAD-[A-Z0-9-]+)', src['DYAD']))
    assert d_new - d_old == set(NEW_RIDS['DYAD']) and d_old <= d_new, (d_new - d_old, d_old - d_new)
    az6 = at('az-v0.6', 'dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md').decode(); az7 = src['AZ']
    az_owned = lambda t: set(re.findall(r'(?<![A-Z0-9-])((?:AZ|PROP-AZ|DEF-AZ|CONV-AZ|TDRG-AZ|SG-AZ)-[A-Z0-9.-]*[A-Z0-9])', t))
    owner_facts = dict(az_x2_sentence_only_in_appendix_b=az7.count('the legal correction is') == 1 and 'Withdrawn as a current statement' in az7,
                       az_cites_deg2_cancel='RID: DYAD-ALG-Q3-DEG2-CANCEL' in az7, az_cites_zn_state='RID: TDRG-DEF-ZN-STATE' in az7, az_imports_q403='RID: DYAD-THM-Q403-PHASELAW' in az7,
                       az_raw_cubic_caveat='its identity with the historical proposition is not yet established' in az7, az_thread_c_availability='EV-SRC-REPORTED' in az7,
                       az_no_chsh='CHSH' not in az7, az_owned_identifiers_kept=az_owned(az6) <= az_owned(az7),
                       dyad_tag_alg='`[ALG]` [RID: DYAD-ALG-NOT-AREA-PRESERVING]' in src['DYAD'], dyad_sharp_conditional='`[THM]` `[assuming: RECOG-THM-R9-SHARPENED-ROWS]` [RID: DYAD-THM-OPEN21-SHARP-ROWS]' in src['DYAD'],
                       dyad_open20_no_result='**Sectorial pilot; no result is claimed.**' in src['DYAD'], dyad_cubic_rate_no_rid='stays a statement-level import of `RECOG-ALG-NU3-CLOSED-FORM` without a Dyadic RID' in src['DYAD'],
                       recog_sharp_rows_at_pin='RID: RECOG-THM-R9-SHARPENED-ROWS' in at('recog-v0.3.26', 'dsn/RTG_RELATIONAL_RECOGNITION_DSN.md').decode())
    assert all(owner_facts.values()), [k for k, v in owner_facts.items() if not v]
    for p in PATHS: assert at(SNAPSHOT, p), p
    n_snap, st_snap = pipe_states(SNAPSHOT); assert n_snap == 107 and st_snap == PIPE_SNAPSHOT, (n_snap, st_snap)
    # ---- dispositions ----
    def row(t, key):
        ls = [l for l in t.split('\n') if l.startswith(key + ' ')]; return '\n'.join(ls) if ls else None
    touched = ['AZ.A1', 'AZ.A2', 'AZ.A3', 'AZ.A7', 'DYAD.X11', 'AZ.A5', 'DYAD.X4', 'DZT.Q1', 'OPENM.U11', 'PROG.G6', 'NUMGEN.N-I1', 'OPENM.U2', 'DYAD.X8', 'D5.X3', 'METH.M1', 'METH.M2']
    disp = []
    for key in touched:
        o = row(base, key); n = row(text, key); assert o, key
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded'); assert (n is None) == (key in newret), key
        disp.append(dict(key=key, disposition=state, reason=newret.get(key, 'unchanged: the owner state it records is unchanged at the v0.12 sources' if state == 'retained' else 'reworded; see edit_log.json'),
                         previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    run = lambda t, with_sources=True: bool(c.run(t, m, src, cmap, idmap, retired, with_sources=with_sources).fails())
    t = text.replace('AZ v0.7 §6 states the same verdict (OPENM.U2, U11; DYAD.X8).', 'AZ v0.7 §6 states the same verdict (AZ.A1; OPENM.U2, U11; DYAD.X8).', 1); ctl('V1', 'H2 cites the retired AZ.A1', 'H2:AZ.A1' in h_l5_map(t)['dangling'] and run(t, False))
    t = text + 'AZ.A7 D-RID: reused\n'; ctl('V2', 'retired key reused', run(t, False))
    t = text.replace('| v6.4.24 | `dyad-v6.4.24` |', '| v6.4.23 | `dyad-v6.4.23` |', 1); ctl('V3', 'SOURCES row older than the manifest', run(t) or bool(stale_editions(t)))
    t = text.replace('| v0.7 | `az-v0.7` |', '| v0.6 | `az-v0.6` |', 1); ctl('V4', 'stale AZ SOURCES row', run(t) or bool(stale_editions(t)))
    t = text.replace('DYAD-THM-OPEN21-SHARP-ROWS THM·c |', 'DYAD-THM-OPEN21-SHARP-ROW THM·c |', 1); ctl('V5', 'new Dyadic RID misspelled against the source', run(t))
    t = text.replace('DYAD-THM-OPEN21-SHARP-ROWS THM·c |', 'DYAD-THM-OPEN21-SHARP-ROWS THM |', 1).replace(' | if RECOG-THM-R9-SHARPENED-ROWS: ', ' | ', 1); ctl('V6', 'sharp rows shown as unconditional', bool(scope_guards(t)))
    t = text.replace('C′₂=259.2, S=492/25', 'C′₂=81.49, S=492/25', 1); ctl('V7', 'row constants mixed', bool(scope_guards(t)))
    t = text.replace('DYAD-ALG-NOT-AREA-PRESERVING ALG |', 'DYAD-ALG-NOT-AREA-PRESERVING THM |', 1); ctl('V8', 'not-area-preserving kept at THM against the owner tag', bool(scope_guards(t)) or run(t))
    t = text.replace('DYAD-ALG-P6-LINEAR-ORDER ALG |', '*DYAD:p6-linear-order ALG |', 1); ctl('V9', 'registered RID shown as a pseudo-ID again (coverage)', run(t) or bool(stale_editions(t)))
    t = text.replace('DYAD.X4 D-RID | one statement is used downstream without a Dyadic RID: the cubic radial rate across p (*DYAD:cubic-rate-across-p), which the owner keeps', 'DYAD.X4 D-RID | closed: the owner keeps', 1); ctl('V10', 'DYAD.X4 shown as closed', bool(scope_guards(t)))
    t = text.replace('both stay ACTIVE; no certification run is authorized', 'B-an is decided', 1); ctl('V11', 'OPEN 20 pilot read as a result', bool(scope_guards(t)))
    t = text.replace('(EV-SRC-REPORTED, EV-NOT-RERUN); the owner keeps the grades with that limit', '(recovered and hash-checked); the grades are confirmed', 1); ctl('V12', 'SESSION recovery read as owner evidence', bool(scope_guards(t)))
    t = text.replace('⇒ static ℤ_N antipodal-band geometry, not dynamics', '⇒ a dynamical law', 1); ctl('V13', '4|q rule read as dynamics', bool(scope_guards(t)))
    t = '\n'.join(l for l in text.split('\n') if not l.startswith('AZ.A5 ~ D-LINK / SG trap:')); ctl('V14', 'AZ.A5 dropped with the retired rows', bool(scope_guards(t)))
    t = text.replace('(none at this edition)', 'AZ.A1 | AZ §6 "To OPEN M": legal deficit correction ×2 (not ×4) | contradicts OPEN-M v0.7.1 R16', 1); ctl('V15', 'withdrawn sentence listed as a current D-WRONG', bool(scope_guards(t)) and run(t, False))
    t = text.replace(' Fix: DZT repins. (AZ repinned in v0.7.)', ' Fix: none.', 1); ctl('V16', 'DZT half of the identifier finding dropped', bool(scope_guards(t)))
    t = text.replace('<RECOG-THM-R9-SHARPENED-ROWS (pin recog-v0.3.26 §6.13a;', '<RECOG-THM-R9-SHARPENED-ROWS (pin recog-v0.3.27;', 1); ctl('V17', 'consumer pin of the new theorem moved to the newest RECOG edition', bool(scope_guards(t)))
    t = text.replace('carried with the owner caveat on the historical proposition', 'historical proposition confirmed', 1); ctl('V18', 'raw cubic import without the owner caveat', bool(scope_guards(t)))
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), [x for x in controls if not x['detected']]
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    bl, tl = base.split('\n'), text.split('\n')
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas=BASE_TAG, base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()), atlas_lines=text.count('\n'),
                   base_bytes=len(base.encode()), base_lines=base.count('\n'), source_snapshot=SNAPSHOT, changed_sources=list(MOVED), edit_operations=len(a.log),
                   retired_keys=list(newret), new_keys=[], new_rids_at_tag=NEW_RIDS, new_node_rids=[r for r in NEW_RIDS['DYAD'] if '-ART-' not in r], new_artifact_rids=[r for r in NEW_RIDS['DYAD'] if '-ART-' in r],
                   dyad_rids_at_tag=len(d_new), owner_facts=owner_facts, pipes=dict(items=n_snap, snapshot=st_snap), dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_controls=len(shared), focused_controls=len(controls),
                   v0_11_recheck_with_cumulative_retired_list=v011,
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_12.py': sha(Path(__file__).read_bytes()),
                                'evidence/atlas/build/refresh_v0_10.py': sha(Path(__file__).with_name('refresh_v0_10.py').read_bytes())},
                   limitations=['Structural checks only; no owner certificate was rerun for this edition; new RIDs are checked for presence in the tagged sources, not re-proved.',
                                'Impact refresh of two moved sources (AZ v0.7, DYAD v6.4.24) and the two ATLAS inbox items; the other 16 sources were not re-extracted. AZ v0.7 was read at statement level in its header, §§2, 4.1, 4.2, 6–9 and Appendix B, and through its release record §§3–7; the 59 edits were not re-compared one by one with their owner texts. DYAD v6.4.24 was read in the diff against v6.4.23 (§§1, 2 OPEN 20, 6.1, 6.6, 6.14, 7, 8, Appendix A, F).',
                                'Edition labels on Dyadic and RECOG results ("(v6.4.23)", pins of other consumers) are not source currency and stay; a consumer pin is moved only where the consumer moved it.'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
