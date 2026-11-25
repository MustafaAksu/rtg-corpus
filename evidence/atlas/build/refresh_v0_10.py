#!/usr/bin/env python3
"""Atlas v0.9 -> v0.10 candidate: impact refresh for three moved sources — Genesis Geometry v2.10 (`gen-v2.10`, adopted
3 Nov 2026), Relational Recognition v0.3.27 (`recog-v0.3.27`, adopted 4 Nov 2026) and Programme Overview v1.4
(`programme-v1.4`, adopted 4 Nov 2026) — plus the three items of pipes/ATLAS/ (TRIAD readings Y6/F18; the PROG v1.4 and
RECOG v0.3.27 notices). Change-focused; no compaction, no Methodology migration of the atlas itself.

GEN (D4a, D4b, D2/D3 edges, H5): new nodes GEN-ALG-P4-DRIFT-IDENTITY (d-mode identity, general cubic term first) and
GEN-ALG-BIRTH-SYMMETRY-SEED (one home node in D4a, grade [ALG], values unchanged; the D4b record becomes a cross-reference — review R1a);
chrono-protection with the independent [ALG] route (a new proof, not a recovery; GEN-ART-G2-CHRONO stays [custody-A]);
T-6s/t/u imported at [ALG] (T-6u with the separate Genesis [CAND] reading); section pointers repinned to v2.10 only where
the cited section is byte-identical at v2.10 or the quoted words are present there. L5: F13, F14, F30, GEN.D7, GEN.D17
reworded; F31 (+ TRIAD.T12) and NUMGEN.N-L6 retired (owner-resolved).
RECOG (D3, D2 edges, H5): the (D5) [assuming:] discharged at the A1c sites (registered Dyadic rows imported; c_J, c_7
bounded by the new RECOG-ALG-A1C-JET-REMAINDER-BOUNDS); C7 rows import DYAD-THM-NF-REM-C7-SHARP; K_eps displays outward;
RECOG.R-A1 retired.
PROG (D1, H10): IF register at v1.4 (IF37, IF38; OFN import/reference typing); TDR-G launch-gate record; maintenance
state; PROG.G8 and PROG.G9 retired (answered in v1.4).
TRIAD finding (pipes/ATLAS/20261103-TRIAD-atlas-readings-y6-f18.md): LEGACY.Y6 retyped D-STALE -> D-SCOPE (review R1b) and reworded to the owner readings (Phi_{2->3} is
Triadic [DEF] notation; Genesis states the leading transverse birth [THM] under that name, without a RID); F18 (+ TRIAD.T10)
retired (the RER citation is reference-only; the p=4 remainder bounds are stated conditionally in Triadic).
Pipes: NUMGEN.N-I1 states the census at the snapshot and after this edition's three ATLAS state changes.
Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_10.py
"""
from __future__ import annotations
import hashlib, importlib.util, json, re, subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.10'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = 'fa3db80'   # origin/main after PR #181 (Programme v1.4 post-release); resolved in main()
BASE_TAG = 'atlas-v0.9'
BASE_SHA = 'b48343f5a4d4c066eb37a325ff87d1dadf686fc6c616b67e7a0ad418dcec3b70'   # atlas-v0.9
MOVED = {'PROG': dict(edition='v1.4', tag='programme-v1.4', authority='OWNER: records/programme/RTG_PROGRAMME_OVERVIEW_v1_4_RELEASE_RECORD.md (§7 tag verification)'),
         'GEN': dict(edition='v2.10', tag='gen-v2.10', authority='OWNER: records/gen/GEN_v2_10_RELEASE_RECORD.md at gen-v2.10 (+ Atlas row check records/gen/ATLAS_ROW_CHECK_GEN_v2_10.md)'),
         'RECOG': dict(edition='v0.3.27', tag='recog-v0.3.27', authority='OWNER: records/recog/RECOG_v0_3_27_RELEASE_RECORD.md (§8 publication and verification)')}
SHAS = {'PROG': '37d857d08bb47771ed50fc5829584be74aab120a23e922eba7c84bae097f28c0',
        'GEN': '63c3b020d9c63a43a2e5e9a43c411fad2d07dfcab33995bd928683435bb13d62',
        'RECOG': '19556f913f51b98599faa6ad88c363dda0a278345677f3bd69f3b892d810e1f1'}
NEW_RIDS = {'GEN': ['GEN-ALG-P4-DRIFT-IDENTITY', 'GEN-ALG-BIRTH-SYMMETRY-SEED'],
            'RECOG': ['RECOG-ALG-A1C-JET-REMAINDER-BOUNDS', 'RECOG-ART-A1C-JET-REMAINDER-BOUNDS']}
PIPE_SNAPSHOT = {'closed': 38, 'dispositioned': 1, 'open': 48}
PIPE_BRANCH = {'closed': 38, 'dispositioned': 4, 'open': 45}
ATLAS_ITEMS = ['pipes/ATLAS/20261103-TRIAD-atlas-readings-y6-f18.md', 'pipes/ATLAS/20261104-PROG-v1-4-adopted.md', 'pipes/ATLAS/20261104-RECOG-v0-3-27-adopted.md']
PATHS = ['records/gen/GEN_v2_10_RELEASE_RECORD.md', 'records/gen/ATLAS_ROW_CHECK_GEN_v2_10.md', 'records/recog/RECOG_v0_3_27_RELEASE_RECORD.md',
         'records/programme/RTG_PROGRAMME_OVERVIEW_v1_4_RELEASE_RECORD.md', 'records/triad/TRIAD_v1_8_FIRST_PASS_ADVISORY.md',
         'pipes/TRIAD/20261103-GEN-p4-identity-answer.md', 'pipes/TRIAD/20261103-GEN-birth-symmetry-grade-answer.md',
         'pipes/GEN/20261026-NUMGEN-cyclic-average-route-to-g2-zero.md', 'evidence/gen/scripts/gen_inbox_checks.py',
         'evidence/recog/scripts/recog_a1c_jet_remainder_bounds_cert.py', 'evidence/recog/atlas_review/ra1/ra1_recheck_summary.json'] + ATLAS_ITEMS

def git(*a): return subprocess.check_output(['git', '-C', str(ROOT), *a])
def sha(b): return hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()
def at(ref, path): return git('show', f'{ref}:{path}')
def wjson(p, v):
    p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(v, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

class Edit:
    def __init__(self, text): self.text, self.log = text, []
    def rep(self, old, new, finding, where):
        n = self.text.count(old); assert n == 1, (finding, where, n, old[:90])
        self.text = self.text.replace(old, new)
        self.log.append(dict(id=f'AR10-{len(self.log)+1:03d}', finding=finding, where=where, old_sha256=sha(old), new_sha256=sha(new), old=old, new=new))
    def _one(self, prefix, finding, where):
        ls = [l for l in self.text.split('\n') if l.startswith(prefix)]
        assert len(ls) == 1, (finding, where, prefix, len(ls)); return ls[0]
    def line(self, prefix, new, finding, where): self.rep(self._one(prefix, finding, where), new, finding, where)
    def drop_line(self, prefix, finding, where): self.rep(self._one(prefix, finding, where) + '\n', '', finding, where)
    def after_line(self, prefix, new_lines, finding, where):
        l = self._one(prefix, finding, where); self.rep(l + '\n', l + '\n' + '\n'.join(new_lines) + '\n', finding, where)
    def sub_in_line(self, prefix, old, new, finding, where):
        l = self._one(prefix, finding, where); assert l.count(old) == 1, (finding, where, old[:60]); self.rep(l, l.replace(old, new), finding, where)

# ---- GEN section evidence for pointer repins ----
def gen_sections(tag):
    out, cur = {}, None
    for l in at(tag, 'dsn/RTG_GENESIS_GEOMETRY_DSN.md').decode().split('\n'):
        m = re.match(r'^#{2,4} §?(\d+(?:\.\d+[a-z]?)?)[ .]', l)
        if m: cur = m.group(1); out.setdefault(cur, [])
        if cur: out[cur].append(l)
    return {k: '\n'.join(v) for k, v in out.items()}
G9, G10 = gen_sections('gen-v2.9'), gen_sections('gen-v2.10')
REPIN_EVIDENCE = []
def gen_same(sec):
    ok = G9.get(sec) == G10.get(sec) and G10.get(sec); assert ok, ('GEN section changed', sec)
    REPIN_EVIDENCE.append(dict(section=sec, basis='section byte-identical gen-v2.9 -> gen-v2.10'))
def gen_has(sec, quote):
    ok = quote in (G10.get(sec) or ''); assert ok, ('quote not at gen-v2.10', sec, quote)
    REPIN_EVIDENCE.append(dict(section=sec, basis=f'quote present at gen-v2.10: {quote}'))

def refresh(a: Edit):
    REPIN_EVIDENCE.clear()   # one record per pointer per build (the reproducibility rebuild reruns refresh)
    G, R, P, T = 'GEN v2.10', 'RECOG v0.3.27', 'PROG v1.4', 'TRIAD finding'
    # ---- identity ----
    a.rep('# RTG STATE ATLAS v0.9\n', '# RTG STATE ATLAS v0.10\n', 'identity', 'title')
    a.rep('full identities in evidence/atlas/v0.9/source_manifest.json', 'full identities in evidence/atlas/v0.10/source_manifest.json', 'identity', 'SOURCES header')
    a.rep('| PROG | RTG_PROGRAMME_OVERVIEW | v1.3 | `programme-v1.3` | canonical Tier 0 |', '| PROG | RTG_PROGRAMME_OVERVIEW | v1.4 | `programme-v1.4` | canonical Tier 0 |', P, 'SOURCES PROG row')
    a.rep('| RECOG | RTG_RELATIONAL_RECOGNITION_DSN | v0.3.26 | `recog-v0.3.26` | canonical Tier 3 |', '| RECOG | RTG_RELATIONAL_RECOGNITION_DSN | v0.3.27 | `recog-v0.3.27` | canonical Tier 3 |', R, 'SOURCES RECOG row')
    a.rep('| GEN | RTG_GENESIS_GEOMETRY_DSN | v2.9 | `gen-v2.9` | canonical Tier 3 |', '| GEN | RTG_GENESIS_GEOMETRY_DSN | v2.10 | `gen-v2.10` | canonical Tier 3 |', G, 'SOURCES GEN row')
    a.rep('*END — RTG STATE ATLAS v0.9. Noncanonical; owner DSNs govern.*', '*END — RTG STATE ATLAS v0.10. Noncanonical; owner DSNs govern.*', 'identity', 'footer')
    # ---- HEADLINE ----
    a.sub_in_line('H5 D-LINK high —', 'RECOG-THM-A1C-SHARPENED-SCHEDULE [assuming: Dyadic (D5) row-A proof constants],', 'RECOG-THM-A1C-SHARPENED-SCHEDULE,', R, 'H5 sharpened schedule')
    a.sub_in_line('H5 D-LINK high —', " — Dyadic v6.4.23 registers both: DYAD-THM-LPHASE-ROWA-BRIDGE (c_Q=0.79246, c′_Q=0.36916 outward; the certified majorant is 0.3691523…, so the 0.36915 RECOG assumes lies below it) and DYAD-THM-NF-REM-C7-SHARP (C₇=85.1 / 27.7); RECOG's blocks keep [assuming:] until RECOG re-checks them against the registered rows (RECOG.R-A1).",
                  '; since v0.3.27 the known-a chain (sharpened schedule, start offset, decoder blocks, log-free envelope) rests on imported Dyadic theorem rows — DYAD-THM-LPHASE-ROWA-BRIDGE (c′_Q=0.36916, with the owner rerun of the eight A1c certificates) and DYAD-THM-OPEN3-SPIRAL-REM — and on RECOG-ALG-A1C-JET-REMAINDER-BOUNDS (c_J, c₇ bounded from DYAD-ALG-NF6 and DYAD-THM-NF-REM alone), with no [assuming:] on Dyadic proof constants; the C₇ rows import DYAD-THM-NF-REM-C7-SHARP; grades unchanged.', R, 'H5 (D5) discharged')
    a.sub_in_line('H5 D-LINK high —', 'RECOG-ALG-A1C-LOGFREE-ENVELOPE [assuming: (D5)] (E^(5)', 'RECOG-ALG-A1C-LOGFREE-ENVELOPE (E^(5)', R, 'H5 envelope')
    a.sub_in_line('H5 D-LINK high —', 'GEN chrono-protection G₂=0 has candidate proof routes through NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE (offered to Genesis in pipes/GEN/, undecided by the receiver) and RECOG-ALG-LEADING-RETURN-EQUIVARIANCE (RECOG.R-L2);',
                  'GEN chrono-protection G₂=0 has an independent [ALG] route in GEN v2.10 §6.4 through NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE (a new proof, not a recovery of GEN-ART-G2-CHRONO, which stays [custody-A]) and a second route through RECOG-ALG-LEADING-RETURN-EQUIVARIANCE, noted only (RECOG.R-L2);', G, 'H5 chrono route')
    a.sub_in_line('H10 D-STALE med —', 'recorded as not executed (Programme v1.3 §9.2)', 'recorded as not executed (Programme v1.4 §9.2; TDR-G recorded as executed in part)', P, 'H10 maintenance pointer')
    a.sub_in_line('H10 D-STALE med —', 'Programme v1.3 (`programme-v1.3`) inventories', 'Programme v1.4 (`programme-v1.4`) inventories', P, 'H10 corpus map')
    gen_same('6.3c'); a.sub_in_line('H1 D-STALE high —', 'GEN v2.9 §6.3c G-20 records', 'GEN v2.10 §6.3c G-20 records', G, 'H1 pointer')
    gen_same('6.8'); a.sub_in_line('H8 D-SYM high —', '(owner notation, GEN v2.9 §6.8)', '(owner notation since GEN v2.9, §6.8; Programme v1.4 §8.2 row)', G, 'H8 κ_f pointer')
    gen_has('6.6', 'This six-member set is a coarse closure ansatz'); a.sub_in_line('phase moments · GEN-OPEN-PHASE-MOMENT', '(D4a; GEN v2.9 §6.6: the six', '(D4a; GEN v2.10 §6.6: the six', G, 'index pointer §6.6')
    # ---- D1 (PROG) ----
    a.sub_in_line('(owners: OFN v0.12 adopted 2026-10-30 canonical,', 'Programme Overview v1.3 adopted 2026-10-24', 'Programme Overview v1.4 adopted 2026-11-04', P, 'D1 header Programme edition')
    a.sub_in_line('⊥ κ: class-C coupling κ', '(owner notation, GEN v2.9 §6.8)', '(owner notation since GEN v2.9, §6.8; Programme v1.4 §8.2 row)', G, 'D1 κ collision pointer')
    a.sub_in_line('⊥ κ: class-C coupling κ', 'Programme v1.3 §8.2 (11 rows; no κ_f row yet, PROG.G8)', 'Programme v1.4 §8.2 (12 rows; κ_f row added, class-C row records γ ≡ κ as the OFN/RRF parameter convention)', P, 'D1 κ table at v1.4')
    a.sub_in_line('H8 D-SYM high —', '(Programme v1.3 §8.2, navigation only;', '(Programme v1.4 §8.2, navigation only;', P, 'H8 κ table pointer')
    a.sub_in_line('RRF.F5 D-LINK (owner-stated convention):', '(owner notation, GEN v2.9 §6.8)', '(owner notation since GEN v2.9, §6.8)', G, 'RRF.F5 κ_f pointer')
    a.sub_in_line('F1 D-SYM (GEN.D5, ER2B.Z7, FMS.M7; high):', 'Programme v1.3 §8.2 κ table', 'Programme v1.4 §8.2 κ table (κ_f row included)', P, 'F1 κ table pointer')
    a.sub_in_line('F5 D-STALE (ER2B.Z2, FMS.M1;', 'recorded by GEN v2.9 §6.3c', 'recorded by GEN v2.10 §6.3c', G, 'F5 pointer')
    a.sub_in_line('D5.X1 D-LINK (ruled on the TDR-G side', 'Programme v1.3 §6.4 does not list them', 'Programme v1.4 §6.4 does not list them', P, 'D5.X1 pointer')
    a.line('*PROG:IF-register |', '*PROG:IF-register | IF01 METH→PROG normative · IF02 OFN→DYAD constraint (commitments, not derivation of T; DYAD pin v0.12, programme context) · IF03 OFN→TDRG constraint and declared import (RTG-OFN-ALG-STAR-TOKEN-SHIFT for SG-14; claim pin v0.10, v0.6/v0.7 historical) · IF04 DYAD→TRIAD (fracture state, local return, frame; v6.4.23 claim by claim) · IF05 DYAD→GEN (v6.4.13 historical proof pins; v6.4.22 §6.3c (C2); v6.4.23 DYAD-ALG-NU5-P5) · IF06 GEN→TRIAD (tetrahedral seed, metric conventions; v2.9 claim by claim, radial polynomial held at v2.8.7) · IF07 TRIAD→GEN (T-6 scoped exports; v1.7 claim by claim) · IF08 GEN→UVM (secular frame, norms, cascade test; GEN keeps verdict custody; v2.8.5) · IF09 UVM→GEN requested UV blocks (open; no cascade implied) · IF10 DYAD→UVM · IF11 TRIAD→UVM (chirality, seed comparison; OPEN M\'s own pin v1.6) · IF12 DYAD→NUMGEN continuous (v6.4.18; v6.4.22 for the L-PHASE row-A remainder) · IF13 TDRG→NUMGEN DISC · IF14 NUMGEN→RECOG by RID at v1.21 (N5AS1 DEFECT/INF1, L1, N1C, GAP-LOCK Lemma 3 by NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO; v1.15 producer pins retained where load-bearing) · IF15 GEN→RECOG (B, J_Q, pairings, phase memory) · IF16 DYAD→RECOG (map, return coefficients, normal form, chart laws, row-A bridge and C₇ rows; v6.4.23 by RID and section) · IF17 RECOG↔DYAD mutual citation (bridge-lemma statement RID Dyadic\'s, general-p proof RECOG\'s; retired as transfer-proposal; settled) · IF18 DYAD→DZT · IF19 DZT→DYAD feedback-proposal (open) · IF20 DYAD→AZ-A reference-only · IF21 TDRG→AZ-B/C · IF22 LEGACY→PREL historical · IF23 PREL→UVM historical-hypothesis (harmonic/log-frustration, ladder priors) · IF24 NUMGEN→OFN reference-only feedback (OFN §11.3: RF-O08-09, -10, RF-O09-04) · IF25 TDRG→GEN blocked-cross-branch (consumer pin v2.12.14; blocked until a named P1 bridge) · IF26 RECOG→DYAD (R9 memory as `[assuming:]` of OPEN 3/21; reciprocal amplitude; v0.3.22 claim-level) · IF27 NUMGEN records RECOG as consumer and RECOG\'s explicit-domain A1a/A1b theorems as independent agreement, not inputs (v0.3.24) · IF28 RECOG→OFN claim-level IMP-O08-17–19, IMP-O09-01–03 (further RECOG feedback reference-only) · IF29 RRF→DYAD/TRIAD/RECOG/OFN standard reference (all v0.8.4) · IF30 owners→RRF verbatim import with RID · IF31 OFN↔RRF class-C contract (OFN N-O10-3 / RRF §6.2a; RRF pins OFN v0.10, OFN pins RRF v0.8.4) · IF32 DYAD/GEN/TDRG→OFN claim-level imports (IMP-O08-01–16, -20; IMP-O10-01–07), TRIAD/UVM→OFN reference-only · IF33 RER, IF34 FMS, IF35 ER2B noncanonical records (RER RECOG pin v0.3.20 frozen) · IF36 owners→ATLAS derived map · IF37 GEN→NUMGEN (GEN-ART-SATURATION, NG-10 only; v2.9) · IF38 NUMGEN→GEN (NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE route row; v1.21); consumer pins per row @PROG§7.2', P, 'IF register at v1.4')
    a.line('*PROG:TDRG-launch-gate |', '*PROG:TDRG-launch-gate | owner §§1–2 and App. C gate condition (aligned by the owner in v2.12.14): TDR-24D/F closed at the mechanism level (analytic constants OPEN); 24A→24B→24C before TDR-T; App. C reserves R3–R10 post-TDR-T0; one §7 export row (TDRG-EXPORT-DISCRETE-TRIAD) still names the earlier D/A/B gate — recorded, not repaired, no launch authorized; v1.1 "all R0–R11 before launch" withdrawn @PROG§6.4', P, 'TDR-G launch gate at v1.4')
    a.sub_in_line('*PROG:maintenance-sequence |', '(consumers, OFN feedback, Programme synthesis; material change ⇒ new immutable version) @PROG§9.2',
                  '(consumers, OFN feedback, Programme synthesis; material change ⇒ new immutable version); state at 4 Nov 2026 (v1.4): executed OFN, Legacy, Dyadic, NUMGEN, Genesis, Triadic, OPEN M, RECOG; TDR-G in part (v2.12.14 corrections edition, Methodology migration planned for v2.13); not executed Pre-Legacy, DZT, AZ @PROG§9.2', P, 'maintenance state')
    a.sub_in_line('PROG.G5 ~ D-LINK:', 'Programme v1.3 §7.1 names OFN OPEN-OFN-3B as the criterion home', 'Programme v1.4 §5 names OFN v0.12 OPEN-OFN-3B as the criterion home', P, 'PROG.G5 pointer')
    a.line('PROG.G6 D-STALE (owner-recorded):', 'PROG.G6 D-STALE (owner-recorded): Programme v1.4 §9.2 records the maintenance sequence as executed for OFN, Legacy, Dyadic, Number Genesis, Genesis, Triadic, OPEN M, RECOG, executed in part for TDR-G (v2.12.14 corrections edition; Methodology v1.4 migration planned for v2.13) and not executed for Pre-Legacy, DZT, AZ; Pre-Legacy (v0.8, June) still carries v0.5/v0.3/v1.1/v1.2 pins (bears on PREL.P1).', P, 'PROG.G6 at v1.4')
    a.drop_line('PROG.G8 D-SCOPE', P, 'PROG.G8 answered (retired)')
    a.drop_line('PROG.G9 D-LINK', P, 'PROG.G9 answered (retired)')
    gen_same('6.3b'); a.sub_in_line('OFN.O14 D-LINK (low; wording, new):', 'GEN v2.9 §6.3b–c writes γ only', 'GEN v2.10 §6.3b–c writes γ only', G, 'OFN.O14 pointer')
    # ---- D2 (DYAD edges, NUMGEN) ----
    a.sub_in_line('DYAD-THM-SMOOTH-EQUIVARIANT-CHART THM |', 'GEN v2.9 imports it for the G-20 existence note', 'GEN v2.10 imports it for the G-20 existence note (dyad-v6.4.22 pin)', G, 'smooth chart consumer')
    a.sub_in_line('DYAD.X1 D-LINK |', 'GEN v2.9 §6.3c records it', 'GEN v2.10 §6.3c records it', G, 'DYAD.X1 pointer')
    gen_has('7', 'v6.4.13 for the historical rows above'); a.sub_in_line('DYAD-DEF-BRIDGE-EXPORT-CONTRACT DEF |', 'GEN v2.9 §7 (item 1, historical pin DYAD v6.4.13)', 'GEN v2.10 §7 (item 1, historical pin DYAD v6.4.13)', G, 'export-contract consumer')
    a.sub_in_line('DYAD-THM-NF-REM-C7-SHARP THM (v6.4.23) |', '>RECOG-THM-R9-SHARPENED-ROWS-C7 (RECOG keeps its [assuming:] until its own re-check; RECOG.R-A1)', '>RECOG-THM-R9-SHARPENED-ROWS-C7 (imported at recog-v0.3.27 in place of the [assuming:]; same ceilings, rows not mixed)', R, 'C7-SHARP consumer')
    a.sub_in_line('DYAD-THM-LPHASE-ROWA-BRIDGE THM (v6.4.23) |', '>RECOG-THM-A1C-SHARPENED-SCHEDULE, RECOG-ALG-A1C-LOGFREE-ENVELOPE (RECOG keeps [assuming:] with 0.36915 until its own re-check; RECOG.R-A1)',
                  '>RECOG-THM-A1C-SHARPENED-SCHEDULE, RECOG-ALG-A1C-START-OFFSET, RECOG-ALG-A1C-LOGFREE-ENVELOPE and the decoder blocks (imported at recog-v0.3.27 with c′_Q=0.36916; owner rerun of the eight A1c certificates, all gates pass)', R, 'bridge consumer')
    a.sub_in_line('NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE RES[ALG] |', '~ GEN chrono-protection G₂=0 route (L5 NUMGEN.N-L6)', '>GEN §6.4 independent route to G₂=0 (GEN v2.10 [ALG] application for L=diag(A,A,A); Programme IF38)', G, 'N3CP consumer')
    a.drop_line('NUMGEN.N-L6 ~ D-LINK (→ GEN D3)', G, 'NUMGEN.N-L6 adopted by the owner (retired)')
    a.sub_in_line('AZ.A2 D-STALE (Thread A) |', '(current GEN v2.9)', '(current GEN v2.10)', 'currency', 'AZ.A2 (D2) pointer')
    gen_same('6.2'); a.sub_in_line('GEN OPEN-9 imports (no GEN claim; owner D2):', 'GEN v2.9 §6.2: archival reference only', 'GEN v2.10 §6.2: archival reference only', G, 'GEN OPEN-9 pointer')
    a.sub_in_line('GEN OPEN-9 imports (no GEN claim; owner D2):', '-NU5-P5 [ν₅^(5)=', '-NU5-P5 [GEN v2.10 §7 label: exact in ℚ(ζ₅), real and imaginary parts in ℚ(√5, √(10+2√5)), pin dyad-v6.4.23 §6.11; ν₅^(5)=', G, 'NU5-P5 label')
    # ---- pipes ----
    a.line('NUMGEN.N-I1 D-LINK (pipe states, receiver side) |', 'NUMGEN.N-I1 D-LINK (pipe states, receiver side) | at the source snapshot fa3db80, pipes_index --check passes with 87 items in 20 inboxes — 38 closed, 1 dispositioned, 48 open; with this edition\'s three ATLAS state changes (TRIAD finding on Legacy Y6 and the RER citation, PROG v1.4 and RECOG v0.3.27 notices: dispositioned, closed by the atlas owner after the tag) 38 closed, 4 dispositioned, 45 open. Open at the snapshot, by receiver: AZ (TDR-G v2.12.14, DYAD N16–N21) · DYAD (PROG v1.4, RECOG v0.3.27) · DZT, ER2B, RER, RRF, UVM (DYAD N16–N21 each) · ER2B, FMS, NUMGEN, RRF, TDRG (OFN v0.11; FMS, NUMGEN, RRF also OFN v0.12) · GEN (PROG v1.4) · LIT (three DYAD requests: INF009/INF010 use validation, sub-petal orbit constant, validated Stokes numerics) · NUMGEN (TDR-G v2.12.14, RECOG v0.3.26 and v0.3.27, DYAD v6.4.23, PROG v1.4) · OFN (DYAD v6.4.23, GEN v2.10, TRIAD v1.7, PROG v1.4, RECOG v0.3.27) · RER, RRF (RECOG v0.3.26) · RRF (GEN v2.10, TRIAD v1.7) · TDRG (OFN token-sum label finding, PROG v1.4) · TRIAD (DYAD bridge-note recovery, GEN 𝒫₄-identity and birth-symmetry answers, GEN v2.10, PROG v1.4; F30) · UVM (GEN κ_f/B_*/sourced-junction items, GEN v2.10, TRIAD v1.7); dispositioned: OFN v0.12 notice to TRIAD (no action). A filed item is not adopted use; each receiver decides at its own checkpoint (CONVENTIONS §7).', 'pipes', 'NUMGEN.N-I1')
    # ---- D3 (RECOG) ----
    a.sub_in_line('(owner RECOG = RTG_RELATIONAL_RECOGNITION_DSN v0.3.26;', 'RTG_RELATIONAL_RECOGNITION_DSN v0.3.26;', 'RTG_RELATIONAL_RECOGNITION_DSN v0.3.27;', R, 'D3 header edition')
    a.sub_in_line('RECOG-THM-R9-MEMORY THM |', 'RECOG-THM-R9-SHARPENED-ROWS-C7 [assuming: C₇≤85.1 / 27.7 — Dyadic\'s published NF-REM certificate values 85.07 / 27.60, not Dyadic theorem statements, registration requested] (Dyadic v6.4.23 registers C₇=85.1 / 27.7 as DYAD-THM-NF-REM-C7-SHARP; RECOG.R-A1)',
                  'RECOG-THM-R9-SHARPENED-ROWS-C7 [import: DYAD-THM-NF-REM-C7-SHARP, dyad-v6.4.23; C₇≤85.1 / 27.7, chart and norm of NF-REM, rows not mixed; v0.3.27, in place of the earlier [assuming:]]', R, 'R9 C7 rows import')
    a.sub_in_line('RECOG-ALG-A1C-RECIPROCAL-DRIFT ALG (v0.3.26) |', 'K_ε=0.7203/0.4513/0.1860 at a=625/1000/2500', 'K_ε=0.7204/0.4514/0.1861 at a=625/1000/2500 (outward displays, v0.3.27 [COR]; certified 0.72030407…, 0.45131291…, 0.18603976…)', R, 'K_eps outward')
    a.sub_in_line('RECOG-ALG-A1C-RECIPROCAL-DRIFT ALG (v0.3.26) |', '(needs a Dyadic bound on Re(ρ₇/z) along an orbit, or the B1-L2 ceiling C₇≤85.1)', '(needs a Dyadic bound on Re(ρ₇/z) along an orbit, or the registered ceiling C₇≤85.1 of DYAD-THM-NF-REM-C7-SHARP — not applied in v0.3.27)', R, 'drift not-supplied')
    a.after_line('RECOG-ALG-A1C-RECIPROCAL-DRIFT ALG (v0.3.26) |', ['RECOG-ALG-A1C-JET-REMAINDER-BOUNDS ALG (v0.3.27) | sc: chart of DYAD-ALG-NF6 and DYAD-THM-NF-REM, 0<q=|z|²≤q*=256/140625 (<1/400: row A); adopted rows only, no RECOG A1c result | J(z)/z=1+u, u=μq+(a₃₂+a₀₅e^{−6iΘ})q², ū=|μ|q+A₅q², A₅=|a₃₂|+|a₀₅|: |Arg(J/z)+τq|≤c_J(q)q², c_J(q)=89√3/324+|a₀₅|+|μ|A₅q+½A₅²q²+ū³/(3(1−ū)q²) (89√3/324=Im a₃₂−½Im μ²); |Arg(F̂/J)|≤c₇(q)q³, c₇(q)=C₇/((1−ū)(1−w)), w=C₇q³/(1−ū), C₇=100; both increase with q ⇒ on q≤q*: c_J≤0.500819, c₇≤100.231, so the proof-outline constants c_J=0.50220, c₇=157.58 of DYAD-THM-LPHASE-ROWA-REMAINDER that RECOG\'s closed forms use are valid ceilings on RECOG\'s domain | <DYAD-ALG-NF6, DYAD-THM-NF-REM | >the six A1c sites TAIL-HARMONICS, SHARPENED-SCHEDULE, LOGFREE-ENVELOPE, START-OFFSET (ii), ADMISSIBLE-REGION, JOINT-CONTRACTOR (with DYAD-THM-LPHASE-ROWA-BRIDGE and DYAD-THM-OPEN3-SPIRAL-REM imported, the (D5) [assuming:] removed; release record R2); RECOG-ALG-A1C-COMBINED-TAIL states c_J^R, c₇^R from it (the majorants were first computed for COMBINED-TAIL, v0.3.25, and are stated source-independently here) | ¬ a Dyadic registration of c_J, c₇ (Dyadic\'s decision) | cert RECOG-ART-A1C-JET-REMAINDER-BOUNDS (exact rationals, interval check; atlas rerun byte-identical, 4 Nov 2026) | @§6.13b'], R, 'new JET-REMAINDER-BOUNDS node')
    a.sub_in_line('RECOG-ALG-A1C-LOGFREE-ENVELOPE ALG·c (v0.3.26) |', 'RECOG-ALG-A1C-LOGFREE-ENVELOPE ALG·c (v0.3.26) | if: [assuming: Dyadic row-A bridge proof constants c_Q=0.79246, c′_Q=0.36915 and the remainder decomposition of the DYAD-THM-LPHASE-ROWA-REMAINDER proof — proof constants, not theorem rows; registration requested] (Dyadic v6.4.23 registers c_Q=0.79246, c′_Q=0.36916 in DYAD-THM-LPHASE-ROWA-BRIDGE; 0.36915 lies below the certified majorant 0.3691523…; RECOG.R-A1) |',
                  'RECOG-ALG-A1C-LOGFREE-ENVELOPE ALG (v0.3.26; source condition v0.3.27) | import: DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM (dyad-v6.4.23; c_Q=0.79246, c′_Q=0.36916, K_Θ=123/125) and RECOG-ALG-A1C-JET-REMAINDER-BOUNDS (c_J, c₇); the (D5) [assuming:] of v0.3.26 is discharged (v0.3.27), grade unchanged |', R, 'LOGFREE envelope source condition')
    a.drop_line('RECOG.R-A1 D-LINK (cross-owner dependency)', R, 'RECOG.R-A1 resolved by the owner (retired)')
    a.sub_in_line('RECOG.R-L2 ~ D-LINK (GEN D3 proof route) |', 'Also bears on D2\'s note that the NUMGEN cyclic-average theorem gives a route to G₂=0.',
                  'GEN v2.10 §8 names it as a second route to G₂=0, noted only; the NUMGEN cyclic-average route is the one Genesis applies as its own [ALG] line (§6.4; IF38).', G, 'RECOG.R-L2 state')
    # ---- D4a (GEN primitive, TRIAD) ----
    a.sub_in_line('(sources: GEN v2.9 primitive/triad/K3/K4/phase parts ·', 'GEN v2.9 primitive', 'GEN v2.10 primitive', G, 'D4a header edition')
    a.sub_in_line('⊥ κ (central collision; see D4a.L5 F1):', '(D4b; GEN v2.9 §6.8)', '(D4b; GEN v2.10 §6.8)', G, 'D4a κ pointer')
    gen_has('2', 'Specialization of `GEN-THM-DELTA-QC`'); a.sub_in_line('GEN-OPEN-WPHASE-GSPLIT ALG·dx |', '(GEN v2.9 §2 specialization line', '(GEN v2.10 §2 specialization line', G, 'GSPLIT pointer')
    a.sub_in_line('GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO THM·c |', 'GEN v2.9 §6.3c G-20 note', 'GEN v2.10 §6.3c G-20 note', G, 'factor no-go pointer')
    a.line('*GEN:chrono-protection THM |', '*GEN:chrono-protection THM | L=diag(A,A,A): G₂(Z)=Σ_{j=0}^5L^{5−j}F₂(L^jZ)=0; ΔQ_u=O(‖Z‖⁴), u∈{s,c,d}; G₃ survives parity filter (ALG; magnitude needs hexagonal-orbit evaluation) | art GEN-ART-G2-CHRONO [custody-A] | independent route (GEN v2.10 §6.4, ALG): application of NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE — first nonlinear degree quadratic, degree-2 vector charges a−b−1∈{1,−1,−3}≢0 mod 6 ⇒ resonant projection of F₂ vanishes ⇒ G₂=0, for every quadratic F₂:ℝ⁶→ℝ⁶, cross-component terms included; exact check [indep-INB] gate G1; a new proof, not a recovery of the original source; RECOG-ALG-LEADING-RETURN-EQUIVARIANCE a second route, noted only (RECOG.R-L2) | >TRIAD (T-6u premise G₂=0), GEN-ALG-P4-DRIFT-IDENTITY | @§6.4', G, 'chrono-protection independent route')
    a.after_line('GEN-THM-DELTA-QC THM |', ['GEN-ALG-P4-DRIFT-IDENTITY ALG (v2.10) | sc: six-step block map Z↦L⁶Z+G₂(Z)+G₃(Z)+O(‖Z‖⁴) of §6.4, Q_d=dᵀBd, d′ the d-component of the image | Q_d(d′)−Q_d(d)=2dᵀBG_{2,d}(Z)+[2dᵀBG_{3,d}(Z)+Q_d(G_{2,d}(Z))]+O(‖Z‖⁵) (cubic term first, quartic bracket second); with L⁶=I (GEN-THM-LIN-ORDER6) and G₂=0 (§6.4) ⇒ 𝒫₄=ΔQ_d^(4)=2dᵀBG_{3,d}, and G_{3,d}(s,c,0)=½B⁻¹∇_d𝒫₄|_{d=0}; the printed ΔQ_d^(4) reproduces the printed seeds Q_{d,1}^[s³]=7/1024Q_s³, Q_{d,1}^[c³]=61/34992Q_c³ ([indep-INB] gates G7a, G7b) | d-mode analogue of GEN-THM-DELTA-QC, distinct from it | ¬ an independent certificate of the ΔQ_d^(4) coefficients (GEN-ART-P4-PRIMITIVE [custody-A]); G₂=0 rests on §6.4 (original source [custody-A], independent route there) | >TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC premise (TRIAD v1.7 still holds the import at gen-v2.8.7; F30) | atlas-checked (3 Nov 2026, by hand; records/gen/ATLAS_ADVISORY_GEN_INBOX_20261103.md §6) | @§6.5'], G, 'new P4 drift identity node')
    a.line('*GEN:birth-symmetry THM | s³-seeded apex, d₀=0: I_ds^(1)=ω_ds^(1)=−Q_s²/16 ⇒ φ_ds^(1)=π+arctan(√3/2)≈3.8553 (3rd', 'GEN-ALG-BIRTH-SYMMETRY-SEED ALG | s³-seeded apex, d₀=0: I_ds^(1)=ω_ds^(1)=−Q_s²/16 ⇒ φ_ds^(1)=π+arctan(√3/2)≈3.8553 (3rd quadrant); D_birth^[s³]=7/512Q_s³=2Q(V_s), the selected seeded-vector radial channel — distinct from the seeded-state amplitude Q(V_s)=Q_{d,1}^[s³]=7/1024Q_s³ and not by itself a demonstrated complete next-block increment | old ω=−I and second-quadrant branch FAIL (GEN-FAIL-OLD-BIRTH-SIGN-PHASEDRIFT) | the former §6.6 [THM] grade is a corrected claim (GEN App. B), values unchanged | ≡ TRIAD T6U I_{V_s,s} (TRIAD v1.7 imports it as [THM]; F30) | exact evaluation at seed GEN-ART-G3D-SEED; also from the printed 𝒫₄ through GEN-ALG-P4-DRIFT-IDENTITY ([indep-INB] gate G8) | >D4b phase-bridge harness (cross-reference there) | @§6.6', G, 'birth symmetry RID (D4a home node)')
    gen_has('6.6', 'This six-member set is a coarse closure ansatz'); a.sub_in_line('*GEN:moment-closure ALG·s |', '| GEN v2.9: coarse closure ansatz', '| GEN v2.10 §6.6: coarse closure ansatz', G, 'moment closure pointer')
    a.sub_in_line('TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC ALG |', '(from V_d=½B⁻¹∇_d𝒫₄, premises G₂=0, 𝒫₄=2dᵀBG_{3,d}; the 𝒫₄ identity keeps its gen-v2.8.7 claim-level pin in TRIAD v1.7 §7.2, not printed at gen-v2.9, F30)',
                  '(from V_d=½B⁻¹∇_d𝒫₄, premises G₂=0, 𝒫₄=2dᵀBG_{3,d}; GEN v2.10 prints the identity as GEN-ALG-P4-DRIFT-IDENTITY; TRIAD v1.7 §7.2 still holds its gen-v2.8.7 claim-level pin — the consumer\'s decision, F30)', G, 'T-6u premise')
    gen_has('8', 'the four-case maximum over the two reference policies and two typed readings'); a.sub_in_line('TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC ALG |', 'GEN v2.9 §8 labels the case and cites the four-case maximum √14/16)', 'GEN v2.10 §8 labels the case and cites the four-case maximum √14/16; GEN imports the diagnostic at [ALG], triad-v1.7 §6.17)', G, 'T-6u consumer')
    a.sub_in_line('TRIAD-EXPORT-PROTOCOL-2 DEF |', 'Programme CN-05 not recorded (PROG.G9); RRF convention-only; OFN reference-only; GEN imports T-6s/t/u at [CAND] (F31)',
                  'Programme v1.4 §7.3 records CN-05 received and accepted, no action; RRF convention-only; OFN reference-only; GEN v2.10 imports T-6s/t/u at [ALG] (triad-v1.7 §§6.15–6.17; T-6u with the separate Genesis [CAND] reading GEN-CAND-APEX-T6U; the proposed OPEN-M interface use of T-6s stays [CAND])', G, 'export consumer state')
    a.sub_in_line('RER-TRIAD-BIRTH-GRAPH-INVOLUTION ALG·FORMAL_ONLY nc', '>TRIAD §7.2 citation (L5 F18)', '>TRIAD §7.2 citation (reference only, noncanonical; owner reading: not load-bearing, TRIAD v1.7 §6.15, §7.4 CN-02 state the p=4 remainder bounds conditionally)', T, 'RER citation typed')
    # ---- D4a L5 ----
    a.sub_in_line('F13 D-RID/D-LINK (ER2B.Z8, RER.E8, GEN.D7, TRIAD.T3):', 'GEN unnumbered THMs (pure-chiral, antisym-channel, master parity, birth-leading, chrono-protection, P4, rank obstruction, birth symmetry, NF sign split, meanfeedback cubic) uncitable by RID;',
                  'GEN unnumbered THMs (pure-chiral, antisym-channel, master parity, birth-leading, chrono-protection, P4 polynomial, rank obstruction, NF sign split, meanfeedback cubic) uncitable by RID (GEN v2.10 adds GEN-ALG-P4-DRIFT-IDENTITY for the d-mode identity and GEN-ALG-BIRTH-SYMMETRY-SEED, graded [ALG], for birth symmetry);', G, 'F13 GEN RIDs')
    a.sub_in_line('F13 D-RID/D-LINK (ER2B.Z8, RER.E8, GEN.D7, TRIAD.T3):', 'TRIAD imports birth-leading, chrono-protection, P4, birth-symmetry by locator (TRIAD v1.7 §7.2: re-read at gen-v2.9, the nine "RID unavailable" imports still have no result RID there, and Genesis records no response to the REQ-T16 requests).',
                  'TRIAD imports birth-leading, chrono-protection, P4, birth-symmetry by locator (TRIAD v1.7 §7.2, re-read at gen-v2.9; at gen-v2.10 two of them have result RIDs, the others still none, and Genesis records no response to the REQ-T16 requests).', G, 'F13 TRIAD locators')
    a.sub_in_line('F14 D-PROOF (TRIAD.T5, GEN.D3 primitive part):', '(GEN v2.9 §8 custody state (a) missing,', '(GEN v2.10 §8 custody state (a) missing,', G, 'F14 pointer')
    a.sub_in_line('F14 D-PROOF (TRIAD.T5, GEN.D3 primitive part):', 'load-bearing: P4 feeds the cascade chain;',
                  'load-bearing: P4 feeds the cascade chain; GEN v2.10 adds an independent [ALG] route for G₂=0 ([indep-INB] gate G1, a new proof, not a recovery) and the d-mode identity (GEN-ALG-P4-DRIFT-IDENTITY), but no independent certificate of the ΔQ_d^(4) coefficients — G2-CHRONO and P4-PRIMITIVE stay [custody-A];', G, 'F14 GEN v2.10')
    a.drop_line('F18 ~ D-LINK (TRIAD.T10):', T, 'F18 owner reading: citation not load-bearing (retired)')
    a.line('F30 D-PIN/D-GRADE (TRIAD.T11;', 'F30 D-PIN/D-GRADE (TRIAD.T11; consumer side after the Genesis answers): GEN v2.10 answers both Triadic questions — it prints the identity 𝒫₄=2dᵀBG_{3,d} as GEN-ALG-P4-DRIFT-IDENTITY (§6.5, under L⁶=I and G₂=0) and states birth symmetry as [ALG] at all sites with GEN-ALG-BIRTH-SYMMETRY-SEED (the §6.6 [THM] corrected; Appendix B entry); the answers are filed (pipes/TRIAD/20261103-GEN-p4-identity-answer.md, pipes/TRIAD/20261103-GEN-birth-symmetry-grade-answer.md; open). TRIAD v1.7 §7.2 still holds the radial-polynomial import at gen-v2.8.7 and imports birth symmetry as [THM]: the repin and the import grade are the consumer\'s decision at its next edition; no Triadic grade changes.', G, 'F30 consumer side')
    a.drop_line('F31 D-GRADE (consumer side; TRIAD.T12):', G, 'F31 resolved by the owner (retired)')
    # ---- D4b (GEN geometry) ----
    a.sub_in_line('(owners: GEN = RTG_GENESIS_GEOMETRY_DSN v2.9', 'RTG_GENESIS_GEOMETRY_DSN v2.9', 'RTG_GENESIS_GEOMETRY_DSN v2.10', G, 'D4b header edition')
    a.sub_in_line('FACE-LIFT GEN-ART-FACE-LIFT ALG |', '(GEN v2.9 §6.8 DEF: face-lift magnitude', '(GEN v2.10 §6.8 DEF: face-lift magnitude', G, 'face-lift pointer')
    a.sub_in_line('⊥ (domain-local): c₀', '(GEN v2.9 §6.8; 9A uses sgn(m)κ_f)', '(GEN v2.10 §6.8; 9A uses sgn(m)κ_f)', G, 'D4b κ pointer')
    a.sub_in_line('*GEN:secular-K− ALG·c |', 'GEN v2.9 §6.8)', 'GEN v2.10 §6.8)', G, 'secular pointer')
    a.line('GEN-CAND-APEX-T6U CAND |', 'GEN-CAND-APEX-T6U CAND | V_s=G_{3,d}^[s³](s,0,0), Q(V_s)=7/1024Q_s³; versus Q_c^seed=4/3Q_s³: R_apex=√21/64≈0.0716 (a primitive seed diagnostic; Genesis\'s own [CAND] reading, beneath the [ALG] import of TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC at triad-v1.7 §6.17, GEN v2.10) | ¬ HINDEX/UV source ratio; [d³], [s³] and the UV apex source are distinct | <TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC, GEN-ART-G3D-SEED (D4a) | @GEN§2', G, 'T6U CAND reading')
    a.line('*GEN:birth-symmetry THM | s³-seeded apex, d₀=0: I_ds^(1)=ω_ds^(1)=−Q_s²/16 ⇒ φ_ds^(1)=π+arctan(√3/2)≈3.8553 (third', '→ GEN-ALG-BIRTH-SYMMETRY-SEED (cross-domain reference, not a node; the one node is in D4a) | the birth phase φ_ds^(1)≈3.8553 of the s³-seeded apex, stated in GEN §6.6 beside this harness; values, scope, the FAIL branch and the not-a-complete-increment caution at the D4a node | <GEN-ALG-BIRTH-SYMMETRY-SEED (D4a) | @GEN§6.6', G, 'birth symmetry (D4b cross-reference)')
    a.sub_in_line('exports: allowed from this domain —', 'GEN v2.9 §7 lists its consumers', 'GEN v2.10 §7 lists its consumers', G, 'exports pointer')
    a.sub_in_line('GEN.D6 D-SYM (owner-declared):', 'in GEN v2.9 §6.8', 'in GEN v2.10 §6.8', G, 'GEN.D6 pointer')
    a.sub_in_line('GEN.D7 D-RID (D4b part, narrowed v2.9):', 'still RID-less: birth symmetry here, pure chiral protection and tetrahedral chronological protection in D4a',
                  'birth symmetry has GEN-ALG-BIRTH-SYMMETRY-SEED since v2.10 (with the d-mode identity GEN-ALG-P4-DRIFT-IDENTITY); still RID-less: pure chiral protection and tetrahedral chronological protection in D4a', G, 'GEN.D7 birth symmetry')
    a.sub_in_line('GEN.D17 D-GRADE (owner-declared):', 'GEN v2.9 declares Methodology v1.4 with a bounded migration — 29 inherited [RESULT] blocks', 'GEN v2.10 (as v2.9) declares Methodology v1.4 with a bounded migration — 29 inherited [RESULT] blocks counted in the v2.9 release record', G, 'GEN.D17')
    # ---- D5, Legacy, PREL ----
    a.sub_in_line('AZ.A2 D-STALE: §4.1.2', '(current GEN v2.9)', '(current GEN v2.10)', 'currency', 'AZ.A2 (D5) pointer')
    a.rep('— verify against GEN v2.9; routing', '— verify against GEN v2.10; routing', 'currency', 'PREL/Legacy row (verify)')
    a.rep('recheck REQ-L07-06 against GEN v2.9.', 'recheck REQ-L07-06 against GEN v2.10.', 'currency', 'Legacy row (recheck)')
    a.line('LEGACY.Y6 D-STALE (minor):', 'LEGACY.Y6 D-SCOPE (minor; owner readings, GEN v2.10 and TRIAD v1.7): SG-L0L1-10 calls Φ_{2→3} "the current certified birth theorem in the continuous branch". At current owner scope the certified part is the leading one: Genesis states the leading one-dimensional transverse birth, c₀^[3]=κQ_sJ_Qs_*, as `[THM]` under that name (§1; proof source GEN-ART-PHI-2TO3 [custody-A]; no result RID); the fifth-order remainder c₀=κQ_sJ_Qs_*+O(|s_*|⁵) holds only if the selected complete child functional preserves the cubic term and inherits it, and the physical residual/child functional is OPEN (GCL-06). Triadic §6.1 uses Φ_{2→3} as `[DEF]` notation for the declared continuous birth family, the complete physical event OPEN. The Legacy phrase matches the leading Genesis theorem; it overstates only if read as a certified complete birth or event law, which no owner states (pipes/ATLAS/20261103-TRIAD-atlas-readings-y6-f18.md).', T, 'LEGACY.Y6 owner reading (D-SCOPE)')

KEY = re.compile(r'(?<![A-Za-z0-9_.-])((?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?|NUMGEN\.N-Q\*|NUMGEN\.N-[A-Z]+\d*|RECOG\.R-[A-Z]+\d+[a-z]?)|F\d+)(?![A-Za-z0-9_-])')
ROW = re.compile(r'^((?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?|NUMGEN\.N-Q\*|NUMGEN\.N-[A-Z]+\d*|RECOG\.R-[A-Z]+\d+[a-z]?)|F\d+)(?: \+ ((?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?)))?(?![A-Za-z0-9_-])')

def l5_rows(lines):
    rows, sec = {}, None
    for i, l in enumerate(lines, 1):
        if l.startswith('## ') or l.startswith('### '): sec = l
        if sec and 'L5' in sec and not l.startswith('#'):
            m = ROW.match(l)
            if m:
                rows.setdefault(m.group(1), i)
                if m.group(2): rows.setdefault(m.group(2), i)
    return rows

def h_l5_map(text):
    lines = text.split('\n'); rows = l5_rows(lines); out, dangling = [], []
    for h in [l for l in lines if re.match(r'^H\d+ ', l)]:
        hid = h.split()[0]; keys = sorted(set(KEY.findall(h))); miss = [k for k in keys if k not in rows]
        dangling += [f'{hid}:{k}' for k in miss]; out.append(dict(h=hid, l5_keys=keys, missing=miss))
    cited = {k for r in out for k in r['l5_keys']}
    high = [k for k, i in rows.items() if re.search(r'\bhigh\b', lines[i-1][:120]) and k not in cited]
    return dict(rows=out, dangling=dangling, high_l5_without_h=high, l5_rows=len(rows))

STALE = [r'`programme-v1\.3` \|', r'\| v1\.3 \| `programme', r'`gen-v2\.9` \|', r'\| v2\.9 \| `gen', r'`recog-v0\.3\.26` \|', r'\| v0\.3\.26 \| `recog',
         r'RECOGNITION_DSN v0\.3\.26;', r'GENESIS_GEOMETRY_DSN v2\.9 ', r'sources: GEN v2\.9 primitive', r'Programme Overview v1\.3 adopted', r'Programme v1\.3 §',
         r'GEN v2\.9 §6\.[2368]', r'GEN v2\.9 §[278]', r'GEN v2\.9: coarse', r'current GEN v2\.9', r'against GEN v2\.9',
         r'keeps? (its )?\[assuming:\]', r'until its own re-check', r'K_ε=0\.7203', r'B1-L2 ceiling C₇≤85\.1\)', r'undecided by the receiver', r'\*GEN:birth-symmetry',
         r'at \[CAND\] \(F31\)', r'PROG\.G9\)', r'\(L5 F18\)', r'no Φ_\{2→3\} RID in current GEN/TRIAD']

def stale_editions(text):
    # *ATLAS:checked-* lines are dated evidence records ("sources as then read", EV-NOT-RERUN) and are left as recorded
    return [l[:90] for l in text.split('\n') if not l.startswith('*ATLAS:checked-') and any(re.search(p, l) for p in STALE)]

def node(text, prefix):
    ls = [l for l in text.split('\n') if l.startswith(prefix)]
    return ls[0] if len(ls) == 1 else ''

def scope_guards(text):
    """Owner scope that must survive in the refreshed nodes (focused, statement-level)."""
    bad = []
    p4 = node(text, 'GEN-ALG-P4-DRIFT-IDENTITY ALG')
    if '2dᵀBG_{2,d}(Z)' not in p4 or 'with L⁶=I' not in p4 or 'G₂=0' not in p4: bad.append('P4 identity: general cubic term and premises')
    if '¬ an independent certificate of the ΔQ_d^(4) coefficients' not in p4: bad.append('P4 identity: coefficient custody')
    ch = node(text, '*GEN:chrono-protection THM')
    if 'a new proof, not a recovery' not in ch or '[custody-A]' not in ch: bad.append('chrono route not a recovery')
    homes = [l for l in text.split('\n') if l.startswith('GEN-ALG-BIRTH-SYMMETRY-SEED')]
    if len(homes) != 1: bad.append(f'birth symmetry: {len(homes)} node lines (one home required)')
    bs = node(text, 'GEN-ALG-BIRTH-SYMMETRY-SEED ALG |')
    if 'values unchanged' not in bs or 'not by itself a demonstrated complete next-block increment' not in bs: bad.append('birth symmetry: grade record / increment caution')
    if '<GEN-ALG-BIRTH-SYMMETRY-SEED (D4a)' not in node(text, '→ GEN-ALG-BIRTH-SYMMETRY-SEED (cross-domain reference'): bad.append('birth symmetry: D4b cross-reference')
    j = node(text, 'RECOG-ALG-A1C-JET-REMAINDER-BOUNDS ALG')
    if 'adopted rows only, no RECOG A1c result' not in j or '¬ a Dyadic registration of c_J, c₇' not in j: bad.append('jet bounds: scope / not a Dyadic registration')
    if 'c_J≤0.500819, c₇≤100.231' not in j: bad.append('jet bounds: certified ceilings')
    e = node(text, 'RECOG-ALG-A1C-LOGFREE-ENVELOPE ALG')
    if 'grade unchanged' not in e or 'c′_Q=0.36916' not in e or '0.36915' in e: bad.append('envelope: source condition')
    f30 = node(text, 'F30 D-PIN/D-GRADE')
    if "consumer's decision" not in f30 or 'no Triadic grade changes' not in f30: bad.append('F30: consumer decision')
    y6 = node(text, 'LEGACY.Y6 D-SCOPE')
    if '`[DEF]`' not in y6 or 'leading one-dimensional transverse birth' not in y6 or 'which no owner states' not in y6 or 'OPEN (GCL-06)' not in y6: bad.append('Y6: owner reading at scope')
    rer = node(text, 'RER-TRIAD-BIRTH-GRAPH-INVOLUTION')
    if 'not load-bearing' not in rer: bad.append('RER citation typing')
    ifr = node(text, '*PROG:IF-register')
    if 'IF24 NUMGEN→OFN reference-only' not in ifr or 'TRIAD/UVM→OFN reference-only' not in ifr or 'IF38 NUMGEN→GEN' not in ifr: bad.append('IF register typing')
    return bad

def checker():
    spec = importlib.util.spec_from_file_location('atlas_checker', ROOT / 'tools/atlas_check.py')
    c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c); return c

def pipe_states(ref=None):
    """ref=None reads the working tree (the branch's own pipe-state changes); otherwise a git ref."""
    if ref is None:
        files = sorted(str(p.relative_to(ROOT)) for p in ROOT.glob('pipes/*/2*.md')); read = lambda p: (ROOT / p).read_text(encoding='utf-8')
    else:
        files = [p for p in git('ls-tree', '-r', '--name-only', ref, 'pipes/').decode().split('\n') if re.match(r'pipes/[A-Z0-9]+/2\d+.*\.md$', p)]
        read = lambda p: at(ref, p).decode()
    st = Counter()
    for p in files:
        m = re.search(r'^state:\s*(\S+)', read(p), re.M); st[m.group(1)] += 1
    return len(files), dict(st)

def main():
    global SNAPSHOT
    SNAPSHOT = git('rev-parse', SNAPSHOT + '^{commit}').decode().strip()
    base = at(BASE_TAG, ATLAS).decode(); assert sha(base) == BASE_SHA
    a = Edit(base); refresh(a); text = a.text
    assert not stale_editions(text), stale_editions(text)
    assert not scope_guards(text), scope_guards(text)
    # ---- manifest ----
    old = json.loads(at(BASE_TAG, 'evidence/atlas/v0.9/source_manifest.json'))
    m = json.loads(json.dumps(old))
    for s in m['sources']:
        for k in [k for k in s if k.startswith('v0_8_')]: del s[k]
    m.update(atlas='v0.10', frozen_at='2026-11-04', repository_snapshot=SNAPSHOT, previous_atlas_tag=BASE_TAG, method_tag='atlas-v0.2', method_edition='v0.2')
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_9_edition'] = prev['edition']; s['v0_9_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] in MOVED:
            mv = MOVED[s['key']]; data = at(mv['tag'], s['path'])
            s.update(edition=mv['edition'], tag=mv['tag'], commit=git('rev-parse', mv['tag'] + '^{commit}').decode().strip(), sha256=sha(data), authority=mv['authority'])
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(SNAPSHOT, s['path']), ('snapshot/tag divergence', s['key'])
        s['v0_9_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_9_input_equality'] for x in m['sources']) == {'EQUAL': 15, 'CHANGED': 3}
    assert {x['key'] for x in m['sources'] if x['v0_9_input_equality'] == 'CHANGED'} == set(MOVED)
    for k, h in SHAS.items(): assert next(s for s in m['sources'] if s['key'] == k)['sha256'] == h, k
    wjson(OUT / 'source_manifest.json', m)
    wjson(OUT / 'gen_repin_evidence.json', REPIN_EVIDENCE)
    # ---- H -> L5 ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys ----
    oldret = json.loads(at(BASE_TAG, 'evidence/atlas/v0.9/retired_l5_keys.json'))
    newret = {'RECOG.R-A1': 'RECOG v0.3.27 (D5B, R1, C7; release record records/recog/RECOG_v0_3_27_RELEASE_RECORD.md): the (D5) [assuming:] is discharged at the six A1c sites by DYAD-THM-LPHASE-ROWA-BRIDGE and DYAD-THM-OPEN3-SPIRAL-REM (imported at dyad-v6.4.23, c′_Q=0.36916, owner rerun of the eight A1c certificates) and RECOG-ALG-A1C-JET-REMAINDER-BOUNDS; RECOG-THM-R9-SHARPENED-ROWS-C7 imports DYAD-THM-NF-REM-C7-SHARP; grades unchanged. Pipe items closed by the receiver (pipes/RECOG/20261030-DYAD-v6-4-23-adopted.md).',
              'PROG.G8': 'Programme v1.4 §8.2 (programme-v1.4): κ_f row added (GEN §6.8) and the class-C row corrected per E-P13-1 (OFN §11.4 and RRF §6.2a record γ ≡ κ as the class-C parameter convention); pipes/PROG/20261026-GEN-kappa-table-kappa-f-row-and-e-p13-1.md closed.',
              'PROG.G9': 'Programme v1.4 §7.2–§7.3: IF07 carries Genesis\'s pin v1.7, IF11 stays OPEN M\'s own pin v1.6 (recorded, not set by the Programme), and CN-05 is received and accepted with no action; pipes/PROG/20261103-TRIAD-v1-7-adopted.md closed.',
              'F31': 'GEN v2.10 (G6): T-6s and T-6t imported at [ALG] at triad-v1.7 §§6.15–6.16; T-6u imported at [ALG] at §6.17 with the separate Genesis [CAND] reading GEN-CAND-APEX-T6U; the proposed OPEN-M interface use of T-6s stays [CAND] (round-2 R1). The receiver graded its own use; nothing below the owner grade remains.',
              'TRIAD.T12': 'Co-key of F31; retired with it.',
              'F18': 'Owner reading, both Triadic co-owners (pipes/ATLAS/20261103-TRIAD-atlas-readings-y6-f18.md; records/triad/TRIAD_v1_8_FIRST_PASS_ADVISORY.md §3): TRIAD v1.7 §7.2 cites RER-TRIAD-BIRTH-GRAPH-INVOLUTION as a reference-only noncanonical formal instance; the p=4 remainder bounds (§6.15; §7.4 CN-02) are stated conditionally in Triadic and not derived from RER — the citation is not load-bearing. The RER node keeps the typed edge.',
              'TRIAD.T10': 'Co-key of F18; retired with it.',
              'NUMGEN.N-L6': 'GEN v2.10 (G1): §6.4 states the L=diag(A,A,A) application of NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE as its own [ALG] line (every quadratic F₂, cross-component terms included; [indep-INB] gate G1; a new proof, not a recovery of GEN-ART-G2-CHRONO, which stays [custody-A]); §7 imports the RID at numgen-v1.21; the offer pipes/GEN/20261026-NUMGEN-cyclic-average-route-to-g2-zero.md is closed. The atlas-derived link became owner text.'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    assert not set(newret) & set(oldret['retired'])
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret if '.' in k]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.10 reasons in dispositions.json.'))
    # ---- shared checker ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at('atlas-v0.2', 'evidence/atlas/coverage_map_v0_2.json'))
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.10/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    # ---- RID presence in the tagged sources (naming check, not certificate replay) ----
    presence = {f'{k}:{r}': (('RID: ' + r) in src[k]) for k, rs in NEW_RIDS.items() for r in rs}
    assert all(presence.values()), [k for k, v in presence.items() if not v]
    for r in NEW_RIDS['GEN'] + NEW_RIDS['RECOG']: assert r in text, r
    gen_old = set(re.findall(r'RID: (GEN-[A-Z0-9-]+)', at('gen-v2.9', 'dsn/RTG_GENESIS_GEOMETRY_DSN.md').decode())); gen_new = set(re.findall(r'RID: (GEN-[A-Z0-9-]+)', src['GEN']))
    assert gen_new - gen_old == set(NEW_RIDS['GEN']) and gen_old <= gen_new, (gen_new - gen_old, gen_old - gen_new)
    rec_old = set(re.findall(r'RID: (RECOG-[A-Z0-9-]+)', at('recog-v0.3.26', 'dsn/RTG_RELATIONAL_RECOGNITION_DSN.md').decode())); rec_new = set(re.findall(r'RID: (RECOG-[A-Z0-9-]+)', src['RECOG']))
    assert rec_new - rec_old == set(NEW_RIDS['RECOG']) and rec_old <= rec_new, (rec_new - rec_old, rec_old - rec_new)
    for p in PATHS: assert at(SNAPSHOT, p), p
    n_snap, st_snap = pipe_states(SNAPSHOT); assert n_snap == 87 and st_snap == PIPE_SNAPSHOT, (n_snap, st_snap)
    n_items, states = pipe_states(None); assert n_items == 87 and states == PIPE_BRANCH, (n_items, states)
    # ---- dispositions ----
    def row(t, key):   # all rows of a key, joined (AZ.A2 has a D2 and a D5 row)
        ls = [l for l in t.split('\n') if l.startswith(key + ' ')]; return '\n'.join(ls) if ls else None
    co = {'TRIAD.T12': 'F31', 'TRIAD.T10': 'F18'}
    touched = ['RECOG.R-A1', 'PROG.G8', 'PROG.G9', 'F31', 'TRIAD.T12', 'F18', 'TRIAD.T10', 'NUMGEN.N-L6', 'NUMGEN.N-I1', 'F13', 'F14', 'F30', 'GEN.D3', 'GEN.D6', 'GEN.D7', 'GEN.D17',
               'PROG.G5', 'PROG.G6', 'OFN.O14', 'DYAD.X1', 'RECOG.R-L2', 'AZ.A2', 'LEGACY.Y6', 'PREL.P1', 'F1', 'F11']
    disp = []
    for key in touched:
        o = row(base, co.get(key, key)); n = row(text, key) if key not in co else None
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded')
        disp.append(dict(key=key, disposition=state, reason=newret.get(key, 'unchanged: the owner state it records is unchanged at the v0.10 sources' if state == 'retained' else 'reworded; see edit_log.json'),
                         previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    t = text.replace('noted only (RECOG.R-L2);', 'noted only (RECOG.R-L2, RECOG.R-A1);', 1); ctl('V1', 'H cites a retired L5 row', 'H5:RECOG.R-A1' in h_l5_map(t)['dangling'])
    t = text + 'F31 D-GRADE: reused\n'; ctl('V2', 'retired key reused', bool(c.run(t, m, src, cmap, idmap, retired, with_sources=False).fails()))
    t = text.replace('| v2.10 | `gen-v2.10` |', '| v2.9 | `gen-v2.9` |', 1); ctl('V3', 'SOURCES row older than manifest', bool(c.run(t, m, src, cmap, idmap, retired).fails()) or bool(stale_editions(t)))
    t = text.replace('GEN-ALG-P4-DRIFT-IDENTITY ALG (v2.10)', 'GEN-ALG-P4-DRIFT-IDENTITIES ALG (v2.10)', 1); ctl('V4', 'new GEN RID misspelled against the source (shared checker links FAIL)', bool(c.run(t, m, src, cmap, idmap, retired).fails()))
    t = text.replace('RECOG-ALG-A1C-JET-REMAINDER-BOUNDS ALG (v0.3.27)', 'RECOG-ALG-A1C-JET-REMAINDER-BOUND ALG (v0.3.27)', 1); ctl('V5', 'new RECOG RID misspelled against the source (shared checker links FAIL)', bool(c.run(t, m, src, cmap, idmap, retired).fails()))
    t = text.replace('Q_d(d′)−Q_d(d)=2dᵀBG_{2,d}(Z)+[', 'Q_d(d′)−Q_d(d)=[', 1); ctl('V6', 'P4 identity without the general cubic term', bool(scope_guards(t)))
    t = text.replace('a new proof, not a recovery of the original source', 'a recovery of the original source', 1); ctl('V7', 'independent route shown as a recovery of the missing source', bool(scope_guards(t)))
    t = text.replace(' | ¬ a Dyadic registration of c_J, c₇ (Dyadic\'s decision)', '', 1); ctl('V8', 'RECOG lemma shown as a Dyadic registration', bool(scope_guards(t)))
    t = text.replace('c′_Q=0.36916, K_Θ=123/125', 'c′_Q=0.36915, K_Θ=123/125', 1); ctl('V9', 'below-majorant c′_Q in the envelope source condition', bool(scope_guards(t)))
    t = text.replace('the repin and the import grade are the consumer\'s decision at its next edition', 'the repin follows automatically', 1); ctl('V10', 'consumer repin implied by the producer answer', bool(scope_guards(t)))
    t = text.replace('uses Φ_{2→3} as `[DEF]` notation', 'states Φ_{2→3} as a certified theorem', 1); ctl('V11', 'Triadic Φ₂→₃ notation read as a certified theorem', bool(scope_guards(t)))
    t = text.replace('IF24 NUMGEN→OFN reference-only feedback', 'IF24 NUMGEN→OFN feedback (recorded import)', 1); ctl('V12', 'NUMGEN→OFN typed as an import again', bool(scope_guards(t)))
    t = text.replace('K_ε=0.7204/0.4514/0.1861', 'K_ε=0.7203/0.4513/0.1860', 1); ctl('V13', 'unsafe-direction K_ε display reintroduced', bool(stale_editions(t)))
    t = text.replace('GEN-ALG-BIRTH-SYMMETRY-SEED ALG |', '*GEN:birth-symmetry THM |', 1); ctl('V14', 'birth symmetry back as an unnumbered THM', bool(stale_editions(t)) or bool(scope_guards(t)))
    t = text.replace('| v1.4 | `programme-v1.4` |', '| v1.3 | `programme-v1.3` |', 1); ctl('V15', 'stale Programme SOURCES row', bool(stale_editions(t)))
    t = text.replace('→ GEN-ALG-BIRTH-SYMMETRY-SEED (cross-domain reference, not a node; the one node is in D4a)', 'GEN-ALG-BIRTH-SYMMETRY-SEED ALG (D4b copy)', 1); ctl('V16', 'second full node for one owner claim (Method §4(4))', bool(scope_guards(t)))
    t = text.replace(' and not by itself a demonstrated complete next-block increment', '', 1); ctl('V17', 'D_birth read as a complete next-block increment', bool(scope_guards(t)))
    t = text.replace('LEGACY.Y6 D-SCOPE (minor;', 'LEGACY.Y6 D-STALE (minor;', 1); ctl('V18', 'Y6 typed as stale against the leading GEN theorem', bool(scope_guards(t)))
    t = text.replace(', which no owner states (pipes/', ' (pipes/', 1); ctl('V19', 'Y6 without the full-birth-law restriction', bool(scope_guards(t)))
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), controls
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas=BASE_TAG, base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()), atlas_lines=text.count('\n') + 1,
                   source_snapshot=SNAPSHOT, changed_sources=list(MOVED), edit_operations=len(a.log), retired_keys=list(newret), new_keys=[],
                   new_rids_at_tag=NEW_RIDS, new_node_rids=[r for rs in NEW_RIDS.values() for r in rs if '-ART-' not in r], new_artifact_rids=[r for rs in NEW_RIDS.values() for r in rs if '-ART-' in r], gen_rids_at_tag=len(gen_new), recog_rids_at_tag=len(rec_new), gen_repin_evidence=len(REPIN_EVIDENCE),
                   pipes=dict(items=n_items, snapshot=st_snap, branch=states), dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_controls=len(shared), focused_controls=len(controls),
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_10.py': sha(Path(__file__).read_bytes())},
                   limitations=['Structural checks only; no owner certificate rerun for this edition except the RECOG jet-remainder certificate (byte-identical, 4 Nov 2026) and the A1c chain rerun of the RA1 advisory (evidence/recog/atlas_review/ra1/); new RIDs checked for presence in the tagged sources, not re-proved. The GEN-ALG-P4-DRIFT-IDENTITY algebra was checked by hand in the GEN inbox advisory (records/gen/ATLAS_ADVISORY_GEN_INBOX_20261103.md §6) and the GEN v2.10 Atlas row check (records/gen/ATLAS_ROW_CHECK_GEN_v2_10.md).',
                                'Impact refresh of three moved sources (GEN v2.10, RECOG v0.3.27, Programme v1.4) and the three ATLAS inbox items; the other 15 domains were not re-extracted; GEN section pointers were repinned only where the section is byte-identical at gen-v2.10 or the quoted words are present (gen_repin_evidence.json); pipe items cited as filed, receiver dispositions are not atlas sources.',
                                'GEN v2.10 §§1, 2, 6.4–6.6, 7, 8 and App. B; RECOG v0.3.27 §§1, 6.13a–b, 6.16e, 7, 8; Programme v1.4 §§5, 6, 7, 8.2, 9.2 and the release records extracted at statement level from the tagged files; proofs live in the owner cells.'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
