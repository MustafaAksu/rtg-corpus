#!/usr/bin/env python3
"""Atlas v0.3 -> v0.4 candidate: internal-consistency refresh after the two independent audits
(records/atlas/ATLAS_V0_4_AUDIT_CLAUDE.md C04-01..10; records/atlas/ATLAS_V0_4_INDEPENDENT_CHATGPT_AUDIT.md A04-01..06;
reconciled in records/atlas/ATLAS_V0_4_RECONCILIATION.md; receiving review V04-01/V04-02 in
records/atlas/ATLAS_V0_4_RECEIVING_REVIEW.md applied in the same deterministic build).

Scope. One source moved: Programme v1.2 -> v1.3 (`programme-v1.3`). Edits: SOURCES row and manifest; H6/H7/H8/H10/H11;
cross-domain index (class C, K3 identity); D1 PROG nodes; D1.L5 PROG.* and RRF.F5; D4a kappa line, F1, F2; D4b FACE-LIFT,
GEN.D5; D5.L5 AZ.A3. Convention introduced: every HEADLINE line cites L5 row ids only (evidence/atlas/v0.4/h_l5_map.json);
"kappa_f" is marked as an atlas label wherever it occurs (GEN writes kappa in §6.8/§6.9). No other domain re-extracted.
No owner DSN, source tag or shared checker is modified. Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_4.py
"""
from __future__ import annotations
import hashlib, importlib.util, json, re, subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.4'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = '21edfb8d019f6f3130217035f387855cde87ce87'   # origin/main after PR #26/#27 (programme-v1.3 merged)
BASE_SHA = '71310e8c5e1b29979a854ee2ee932efa4765f038bbe0c10299e14f424ad1dc5b'   # atlas-v0.3
PROG_SHA = '1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06'   # programme-v1.3 file
PROG_COMMIT = '02848538b81637828826eeef8e3b73b09c7cc221'

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
        self.log.append(dict(id=f'AR04-{len(self.log)+1:03d}', finding=finding, where=where,
                             old_sha256=sha(old), new_sha256=sha(new), old=old, new=new))
    def _one(self, prefix, finding, where):
        ls = [l for l in self.text.split('\n') if l.startswith(prefix)]
        assert len(ls) == 1, (finding, where, prefix, len(ls)); return ls[0]
    def line(self, prefix, new, finding, where): self.rep(self._one(prefix, finding, where), new, finding, where)
    def drop_line(self, prefix, finding, where): self.rep(self._one(prefix, finding, where) + '\n', '', finding, where)

def refresh(a: Edit):
    # ---- identity and sources (C04-01 / A04-01) ----
    a.rep('# RTG STATE ATLAS v0.3\n', '# RTG STATE ATLAS v0.4\n', 'identity', 'title')
    a.rep('full identities in evidence/atlas/v0.3/source_manifest.json', 'full identities in evidence/atlas/v0.4/source_manifest.json', 'C04-01', 'SOURCES header')
    a.rep('| PROG | RTG_PROGRAMME_OVERVIEW | v1.2 | `programme-v1.2` | canonical Tier 0 |',
          '| PROG | RTG_PROGRAMME_OVERVIEW | v1.3 | `programme-v1.3` | canonical Tier 0 |', 'C04-01 / A04-01', 'SOURCES PROG row')
    a.rep('*END — RTG STATE ATLAS v0.3. Noncanonical; owner DSNs govern.*', '*END — RTG STATE ATLAS v0.4. Noncanonical; owner DSNs govern.*', 'identity', 'footer')
    # ---- HEADLINE ----
    a.rep('persists at OFN (O1), GEN §6.3c C2 and G-20, FMS (M1) and ER-2B (Z2) (D4a F5, DYAD.X1).',
          'persists at OFN, GEN §6.3c C2 and G-20, FMS and ER-2B (OFN.O1, F5, DYAD.X1).', 'C04-04 / A04-05', 'H1 keys')
    a.rep('face-lift κ_f=|m||w| vs m|w| flips the soft-branch label for m<0 (GEN.D2)',
          'face-lift κ=|m||w| (GEN §6.8) vs κ=m|w| (GEN §6.9) flips the soft-branch label for m<0 (GEN.D2; the atlas labels this face-lift κ as κ_f, GEN writes κ)', 'C04-10', 'H6')
    a.rep('and the RER modal map ≡ GEN F₁ ≡ OFN raw κ=1, i.e. every RER Triadic record sits in the flat A1 sector OFN excludes, unstated in RER (RER.E1, D4a F2/F3, FMS.M5, ER2B.Z1).',
          'and the RER modal map 𝒩 ≡ GEN F₁ ≡ OFN raw κ=1 (RER-E-CONJ), so ~ the RER Triadic records built on 𝒩 (the F2 list) read as flat-sector reference results in the A1 sector OFN excludes — a per-record scope reading, unstated in RER and not verified against each record\'s hypotheses (F2, F3).', 'A04-04 / C04-04', 'H7')
    a.rep('κ collision programme-wide (class-C coupling κ≡GEN γ ·', 'κ collision programme-wide (class-C coupling κ, ≡GEN γ by the OFN §11.4 / RRF §6.2a parameter convention ·', 'C04-05 / A04-03', 'H8 convention')
    a.rep('· DYAD backbone κ · face-lift κ_f · RRF-CN05 κ ·', '· DYAD backbone κ · GEN face-lift κ (atlas label κ_f) · RRF-CN05 κ ·', 'C04-10', 'H8 kappa_f')
    a.rep("treated differently at four sites (OFN.O8, RRF.F6, RER.E5, PROG.G7); U/U_T denote both NUMGEN's existential tube and DYAD's explicit PRIM-CTR tube (NUMGEN.N-S1). Advice: one cross-stream κ table; rename NUMGEN tube.",
          "treated differently across the sites listed at OFN.O8 + RRF.F6 and F1; U/U_T denote both NUMGEN's existential tube and DYAD's explicit PRIM-CTR tube (NUMGEN.N-S1). The owner corpus carries a cross-stream κ table (Programme v1.3 §8.2, navigation only; the collisions themselves remain). Advice: rename NUMGEN tube.", 'C04-02 / C04-04 / A04-02', 'H8 keys and advice')
    a.rep("H10 D-SCOPE/D-STALE med — corpus map out of date: Programme v1.2 inventory and owner-status reports describe superseded owner states and omit RRF, RER, FMS, ER-2B (no interface edges) (PROG.G1/G2); OPEN-M's chart-dependent OPEN-M-6 audit does not consider DYAD's smooth λ-equivariant chart (OPENM.U1); Pre-Legacy pointers to OFN 3B/OPEN-OFN-6 point to changed content (PREL.P1, PROG.G6).",
          "H10 D-STALE med — owner passes outstanding: OPEN-M's chart-dependent OPEN-M-6 audit does not consider DYAD's smooth λ-equivariant chart (OPENM.U1); the Pre-Legacy owner pass of the Programme maintenance sequence is recorded as not executed (Programme v1.3 §9.2) and Pre-Legacy's pointers to OFN 3B/OPEN-OFN-6 point to changed content (PREL.P1, PROG.G6). The corpus map itself is current at this snapshot: Programme v1.3 (`programme-v1.3`) inventories every home, RRF, the noncanonical records and the atlas at their governing tags.", 'C04-02 / A04-01', 'H10')
    a.rep('(LEGACY.Y2 ≡ PREL.P2 ≡ OPENM.U9)', '(LEGACY.Y2 ≡ OPENM.U9; PREL side in LEGACY.Y2)', 'C04-04', 'H11 key 1')
    a.rep('(LEGACY.Y3, PREL.P3)', '(LEGACY.Y3)', 'C04-04', 'H11 key 2')
    # ---- cross-domain index ----
    a.rep('class C · CLASS-C node (D1) ≡ GEN F_γ (γ≡κ) ≡ FMS model C ≡ RRF class-C contract;',
          'class C · CLASS-C node (D1) = OFN F^N_κ, the same declared operation as GEN G^N_γ (§6.3c) under the OFN §11.4 / RRF §6.2a γ≡κ parameter convention (κ∈ℝ∖{0,2}, (H_spec); GEN itself writes γ); ≠ GEN raw F_γ (§6.3b): a different conditional model, not passive transport of the raw family (OFN §5.5.4, RRF §0.3), no owner conjugacy; ≡ FMS model C ≡ RRF class-C contract;', 'C04-05 / A04-03 / V04-02', 'index class C')
    a.rep('K₃ model identity · RER-E-CONJ node (D4a) ≡ GEN F₁ ≡ ER-2B 𝒩 ≡ RER 𝒩 ≡ OFN raw κ=1 (A1, excluded flat sector)',
          'K₃ model identity · RER-E-CONJ node (D4a) ≡ GEN F₁ ≡ ER-2B 𝒩 ≡ RER 𝒩 ≡ OFN raw κ=1 (A1, excluded flat sector); the extension to the RER records built on 𝒩 is an atlas reading per record (~, F2), not an identity', 'A04-04', 'index K3 identity')
    # ---- receiving review V04-01 / V04-02 ----
    a.rep('· Programme Overview v1.2 adopted 2026-09-20, Tier 0 navigation, no physical theorem by appearance ·',
          '· Programme Overview v1.3 adopted 2026-10-24, Tier 0 navigation, no physical theorem by appearance ·', 'V04-01', 'D1 introduction')
    a.rep('CLASS-C DEF (RTG-OFN-DEF-TRIAD-MODEL-CONTRACT part) ≡ GEN F_γ/G^N_γ (γ≡κ) ≡ FMS "model C" ≡ *RRF:class-C-contract |',
          'CLASS-C DEF (RTG-OFN-DEF-TRIAD-MODEL-CONTRACT part) ≡ GEN G^N_γ (§6.3c; same declared operation, γ≡κ parameter convention) ≡ FMS "model C" ≡ *RRF:class-C-contract; ≠ GEN raw F_γ (§6.3b; GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO covers the raw family only, OFN IMP-O10-01 "does not cover class C") |', 'V04-02', 'D1 CLASS-C node')
    # ---- D1 nodes (C04-03 / A04-02) ----
    a.line('PROG-TIERS DEF |',
           'PROG-TIERS DEF | navigation only: 0 programme · 1 methodology · 2 foundational/historical/common-home (OFN, LEGACY, PREL, NUMGEN) · 3 continuous (DYAD, TRIAD, GEN, UVM, RECOG, DZT) · 4 discrete (TDRG) · 5 shared infrastructure and standards (AZ, RRF); classes distinct from tiers: 14 canonical homes + RRF adopted working standard (15 files in dsn/) · RER, FMS, ER2B noncanonical (no tier) · ATLAS derived map (no tier; never a source); homes ≠ branches; GEN header tier statement is the owner\'s, placed Tier 3; discrete inputs = blocked interfaces; BASELINE.md is the hash authority @PROG§6.1', 'C04-03 / A04-02', 'D1 PROG-TIERS')
    a.line('PROG-INTERFACE-TYPES DEF |',
           'PROG-INTERFACE-TYPES DEF | declared-import · standard reference (RRF conventions/contracts/identifiers) · requested-deliverable (incomplete) · feedback-proposal/request · mutual citation (settled custody split) · consumer record · verbatim owner import · interface contract · reference-only · historical-reference/hypothesis · noncanonical record (transfers nothing) · derived map · blocked-cross-branch · normative · constraint; transfer-proposal has no live instance (IF17 retired as such) @PROG§7.1', 'C04-03 / A04-02', 'D1 PROG-INTERFACE-TYPES')
    a.line('*PROG:IF-register |',
           '*PROG:IF-register | IF01 METH→PROG normative · IF02 OFN→DYAD constraint (commitments, not derivation of T) · IF03 OFN→TDRG constraint (v0.6 historical pin) · IF04 DYAD→TRIAD (fracture state, local return, frame) · IF05 DYAD→GEN direct · IF06 GEN→TRIAD (tetrahedral seed, metric conventions) · IF07 TRIAD→GEN (T-6 scoped diagnostic exports) · IF08 GEN→UVM (secular frame, norms, cascade test; GEN keeps verdict custody) · IF09 UVM→GEN requested UV blocks (open; no cascade implied) · IF10 DYAD→UVM · IF11 TRIAD→UVM (chirality, seed comparison) · IF12 DYAD→NUMGEN continuous · IF13 TDRG→NUMGEN DISC · IF14 NUMGEN→RECOG by RID at v1.20.8 (N5AS1 DEFECT/INF1, L1, N1C, GAP-LOCK; v1.15 producer pins retained where load-bearing) · IF15 GEN→RECOG (B, J_Q, pairings, phase memory) · IF16 DYAD→RECOG (map, return coefficients, normal form, chart laws; v6.4.22 by RID and section) · IF17 RECOG↔DYAD mutual citation (bridge-lemma statement RID Dyadic\'s, general-p proof RECOG\'s; retired as transfer-proposal; settled) · IF18 DYAD→DZT · IF19 DZT→DYAD feedback-proposal (open) · IF20 DYAD→AZ-A reference-only · IF21 TDRG→AZ-B/C · IF22 LEGACY→PREL historical · IF23 PREL→UVM historical-hypothesis (harmonic/log-frustration, ladder priors) · IF24 NUMGEN→OFN feedback (recorded import; holonomy operator) · IF25 TDRG→GEN blocked-cross-branch · IF26 RECOG→DYAD (R9 memory as `[assuming:]` of OPEN 3/21; reciprocal amplitude; v0.3.22) · IF27 NUMGEN records RECOG as consumer (explicit-domain A1a theorems not listed as inputs) · IF28 RECOG→OFN comparator DEFs (IMP rows) · IF29 RRF→DYAD/TRIAD/RECOG/OFN standard reference (DYAD v0.8.4, TRIAD v0.8.2, RECOG v0.8.4) · IF30 owners→RRF verbatim import with RID · IF31 OFN↔RRF class-C contract (OFN N-O10-3 / RRF §6.2a) · IF32 DYAD/GEN/TRIAD/UVM/TDRG→OFN scoped feedback IMP-O10-* · IF33 RER, IF34 FMS, IF35 ER2B noncanonical records (RER RECOG pin v0.3.20 frozen) · IF36 owners→ATLAS derived map; consumer pins per row @PROG§7.2', 'C04-03 / A04-02', 'D1 *PROG:IF-register')
    a.line('⊥ κ: class-C coupling κ(≡GEN γ) ·',
           '⊥ κ: class-C coupling κ (≡GEN γ by the OFN §11.4 / RRF §6.2a parameter convention) · GEN birth κ · DYAD backbone κ · GEN face-lift κ (atlas label κ_f) · RRF-CN05 κ (units) · PROG κ_RTG=𝒢_e/J_e · (D6: κ=2πc, κ_grav, κ_top, κ₃, κ′, κ_B) — programme-wide node in header; owner-side navigation table: Programme v1.3 §8.2 (11 rows)', 'C04-05 / C04-10 / A04-02', 'D1 kappa line')
    # ---- D1.L5 ----
    a.line('RRF.F5 ~ D-LINK:', 'RRF.F5 D-LINK (owner-stated convention): class-C κ ≡ GEN γ is OFN\'s and RRF\'s parameter convention — OFN v0.10 §11.4 (claim-level import of GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO: γ ≡ κ ∈ ℝ∖{0,2}, under (H_spec)) and RRF v0.8.4 §6.2a (γ≡κ in the OFN class-C parameter convention); the §11.4 row is the raw-family dictionary and says it does not cover class C; GEN writes γ and states no identification of its own; no owner asserts a model identity raw F_γ ↔ class-C F^N_κ (different conditional model, OFN §5.5.4); FMS model C ≡ class C (CLASS-C node). κ still collides with GEN birth κ, GEN face-lift κ (atlas label κ_f), DYAD backbone κ (F1).', 'C04-05 / A04-03', 'RRF.F5')
    a.drop_line('PROG.G1 D-STALE:', 'C04-02 / A04-01', 'PROG.G1 retired')
    a.drop_line('PROG.G2 D-SCOPE:', 'C04-02 / A04-01', 'PROG.G2 retired')
    a.drop_line('PROG.G4 ~ D-LINK:', 'C04-02 / A04-01', 'PROG.G4 retired')
    a.line('PROG.G5 ~ D-LINK:', 'PROG.G5 ~ D-LINK: P2B criterion = OPEN-OFN-3B criterion; Programme v1.3 §7.1 names OFN OPEN-OFN-3B as the criterion home (Programme side consistent with the node); PREL still quotes the old row-agreement form (PREL.P1); the P2B-CRITERION node (D1) carries the one text.', 'C04-02', 'PROG.G5')
    a.line('PROG.G6 D-STALE:', 'PROG.G6 D-STALE (owner-recorded): Programme v1.3 §9.2 records the maintenance sequence as executed for OFN, Legacy, Dyadic, Number Genesis, Genesis, Triadic, OPEN M, RECOG and not executed for Pre-Legacy, TDR-G, DZT, AZ; Pre-Legacy (v0.8, June) still carries v0.5/v0.3/v1.1/v1.2 pins (bears on PREL.P1).', 'C04-02 / A04-02', 'PROG.G6')
    a.drop_line('PROG.G7 D-SYM:', 'C04-02 / A04-02', 'PROG.G7 retired')
    a.line('AZ.A3 D-STALE:', 'AZ.A3 D-STALE: AZ\'s programme-patch request is satisfied by Programme v1.2 and v1.3 but still listed as open in AZ v0.6.', 'C04-02', 'AZ.A3')
    # ---- D4a / D4b kappa labels (C04-10) and F2 scope (A04-04) ----
    a.rep('vs GEN face-lift κ=|m||w| (D4b) vs κ_RTG (D4b) vs κ_f. Atlas convention in this domain:',
          'vs GEN face-lift κ=|m||w| (D4b; atlas label κ_f) vs κ_RTG (D4b). Atlas convention in this domain:', 'C04-10', 'D4a kappa line')
    a.rep('Plus face-lift κ, κ_RTG, κ_f. Fix: one programme-wide rename (γ for family).',
          'Plus face-lift κ (atlas label κ_f), κ_RTG. Owner-side navigation: Programme v1.3 §8.2 κ table; the owners\' symbols are unchanged.', 'C04-10 / A04-02', 'F1')
    a.rep('all RER Triadic records (C01–C09, age family, 3-fold, N7/N8, triad involution, birth graph) are flat-sector reference results in OFN terms.',
          'the RER Triadic records built on 𝒩 (atlas list: C01–C09, age family, 3-fold, N7/N8, triad involution, birth graph) read as flat-sector reference results in OFN terms — a per-record scope reading; the transfer to each record\'s own hypotheses (conditional age sheets, transported contracts, blocked ER-2B interfaces) is not verified.', 'A04-04', 'F2 scope')
    a.rep('(ΔM_f)²=κ_f²I, κ_f=|m||w|; a(φ)=r_φᵀΔM_f r_φ=m(Im w cos2φ−Re w sin2φ), |a|≤κ_f |',
          '(ΔM_f)²=κ²I, κ=|m||w| (GEN writes κ; the atlas labels this face-lift κ as κ_f elsewhere); a(φ)=r_φᵀΔM_f r_φ=m(Im w cos2φ−Re w sin2φ), |a|≤κ |', 'C04-10', 'D4b FACE-LIFT node')
    a.rep('κ (birth vs κ_f vs scalar-M κ vs κ_RTG)', 'κ (birth vs face-lift κ, atlas label κ_f, vs scalar-M κ vs κ_RTG)', 'C04-10', 'GEN.D5')
    a.rep('κ (birth coefficient vs κ_f=|m||w| vs scalar-M κ=m|w| (sign: GEN.D2) vs κ_RTG=𝒢_e/J_e',
          'κ (birth coefficient vs face-lift κ=|m||w| (GEN §6.8; atlas label κ_f) vs scalar-M κ=m|w| (GEN §6.9; sign: GEN.D2) vs κ_RTG=𝒢_e/J_e', 'C04-10', 'D4b kappa line')
    a.rep('| ! GEN.D2 (κ=m|w| here vs κ_f=|m||w| in §6.8) |', '| ! GEN.D2 (κ=m|w| here vs κ=|m||w| in §6.8, atlas label κ_f) |', 'C04-10', 'D4b SCALARM node')
    a.rep('Δ₃(τ²−κ_f²)²=σ_f²(τ²+2a(φ)τ+κ_f²) exactly;', 'Δ₃(τ²−κ_f²)²=σ_f²(τ²+2a(φ)τ+κ_f²) exactly (κ_f: atlas label for the face-lift κ=|m||w|, GEN writes κ);', 'C04-10', 'D4b secular-K− node')

KEY = re.compile(r'(?<![A-Za-z0-9_.-])((?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?)|F\d+)(?![A-Za-z0-9_-])')
ROW = re.compile(r'^((?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?)|F\d+)(?: \+ ((?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?)))?(?![A-Za-z0-9_-])')

def l5_rows(lines):
    rows, sec = {}, None
    for i, l in enumerate(lines, 1):
        if l.startswith('## ') or l.startswith('### '): sec = l
        if sec and 'L5' in sec and not l.startswith('#'):
            m = ROW.match(l)
            if m:
                rows[m.group(1)] = i
                if m.group(2): rows[m.group(2)] = i
    return rows

def h_l5_map(text):
    lines = text.split('\n'); rows = l5_rows(lines)
    out, dangling = [], []
    for h in [l for l in lines if re.match(r'^H\d+ ', l)]:
        hid = h.split()[0]
        keys = sorted(set(KEY.findall(h)))
        miss = [k for k in keys if k not in rows]
        dangling += [f'{hid}:{k}' for k in miss]
        out.append(dict(h=hid, l5_keys=keys, missing=miss))
    cited = {k for r in out for k in r['l5_keys']}
    high = [k for k, i in rows.items() if re.search(r'\bhigh\b', lines[i-1][:120]) and k not in cited]
    return dict(rows=out, dangling=dangling, high_l5_without_h=high, l5_rows=len(rows))

def stale_prog(text):
    """V04-01 guard: no live line names Programme v1.2 as the governing/adopted edition."""
    return [l[:80] for l in text.split('\n') if re.search(r'Programme Overview v1\.2 adopted|`programme-v1\.2`|\| v1\.2 \| `programme', l)]

def raw_classc_identity(text):
    """V04-02 guard: no line identifies the CLASS-C node with GEN's raw F_γ by ≡."""
    return [l[:80] for l in text.split('\n') if 'CLASS-C' in l and re.search(r'≡ GEN F_γ', l)]

def unlabelled_kf(text):
    """Lines using the atlas label κ_f (not κ_fit) must say so on the same line."""
    return [l for l in text.split('\n') if re.search(r'κ_f(?![A-Za-z0-9])', l) and 'atlas label' not in l]

def checker():
    spec = importlib.util.spec_from_file_location('atlas_checker', ROOT / 'tools/atlas_check.py')
    c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c); return c

def main():
    base = at('atlas-v0.3', ATLAS).decode(); assert sha(base) == BASE_SHA
    a = Edit(base); refresh(a); text = a.text
    assert not unlabelled_kf(text), 'unlabelled κ_f remains'
    assert not stale_prog(text), stale_prog(text)
    assert not raw_classc_identity(text), raw_classc_identity(text)
    # ---- manifest ----
    old = json.loads(at('atlas-v0.3', 'evidence/atlas/v0.3/source_manifest.json'))
    m = json.loads(json.dumps(old))
    m.update(atlas='v0.4', frozen_at='2026-10-24', repository_snapshot=SNAPSHOT, previous_atlas_tag='atlas-v0.3', method_tag='atlas-v0.2', method_edition='v0.2')
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_3_edition'] = prev['edition']; s['v0_3_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] == 'PROG':
            s.update(edition='v1.3', tag='programme-v1.3', commit=PROG_COMMIT, sha256=PROG_SHA,
                     authority='OWNER: records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md at programme-v1.3')
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(SNAPSHOT, s['path']), ('snapshot/tag divergence', s['key'])
        s['v0_3_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_3_input_equality'] for x in m['sources']) == {'EQUAL': 17, 'CHANGED': 1}
    wjson(OUT / 'source_manifest.json', m)
    # ---- H -> L5 map ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed; owner keys such as RER.E1 inside D4a rows are not row ids). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys ----
    oldret = json.loads(at('atlas-v0.3', 'evidence/atlas/v0.3/retired_l5_keys.json'))
    newret = {'PROG.G1': 'Programme v1.3 §6.1-6.5 lists every governing edition at its tag and points to owner status summaries; the superseded v1.2 reports are gone.',
              'PROG.G2': 'Programme v1.3 §6.1 inventories RRF, RER, FMS, ER-2B and the atlas; §7.2 IF29-IF36 carry their edges.',
              'PROG.G4': 'Programme v1.3 §7.2: IF14 by RID at v1.20.8; IF16 v6.4.22 by RID and section; IF17 settled custody split, retired as transfer-proposal.',
              'PROG.G7': 'Programme v1.3 §8.2 carries κ_RTG as hypothesis-grade in the cross-stream κ table; no separate diagnostic remains.'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.4 reasons in dispositions.json.'))
    # ---- shared checker ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at('atlas-v0.2', 'evidence/atlas/coverage_map_v0_2.json'))
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.4/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    # ---- dispositions of touched L5 rows ----
    def row(t, key): return next((l for l in t.split('\n') if l.startswith(key + ' ')), None)
    disp = []
    for key in ['RRF.F5', 'PROG.G1', 'PROG.G2', 'PROG.G4', 'PROG.G5', 'PROG.G6', 'PROG.G7', 'AZ.A3', 'F1', 'F2', 'GEN.D5']:
        o, n = row(base, key), row(text, key)
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded')
        disp.append(dict(key=key, disposition=state, reason=newret.get(key, 'reworded; see edit_log.json'), previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    t = text.replace('(OPENM.U1)', '(OPENM.U99)', 1); ctl('U1', 'H cites a nonexistent L5 row', h_l5_map(t)['dangling'] == ['H10:OPENM.U99'])
    t = text.replace('(F2, F3)', '(RER.E1, F2, F3)', 1); ctl('U2', 'H cites an owner key that is not a row id', h_l5_map(t)['dangling'] == ['H7:RER.E1'])
    t = text + 'PROG.G1 D-STALE: reused\n'; ctl('U3', 'retired key reused', bool(c.run(t, m, src, cmap, idmap, retired, with_sources=False).fails()))
    t = text.replace('| v1.3 | `programme-v1.3` |', '| v1.2 | `programme-v1.2` |', 1); ctl('U4', 'SOURCES row older than manifest', bool(c.run(t, m, src, cmap, idmap, retired).fails()))
    t = text.replace('GEN face-lift κ (atlas label κ_f)', 'GEN face-lift κ_f', 1); ctl('U5', 'unlabelled κ_f reintroduced', unlabelled_kf(t))
    t = text.replace('(F2, F3)', '(F3)', 1).replace('(the F2 list)', '(the list)', 1).replace('(~, F2)', '(~)', 1); ctl('U6', 'high row F2 loses its H citation', 'F2' in h_l5_map(t)['high_l5_without_h'] and 'F2' not in hm['high_l5_without_h'])
    t = text.replace('Programme Overview v1.3 adopted 2026-10-24', 'Programme Overview v1.2 adopted 2026-09-20', 1); ctl('U7', 'stale Programme edition in a live domain introduction (V04-01)', bool(stale_prog(t)))
    t = text.replace('class C · CLASS-C node (D1) = OFN F^N_κ,', 'class C · CLASS-C node (D1) ≡ GEN F_γ (raw) = OFN F^N_κ,', 1); ctl('U8', 'raw/transported model equality inserted into the index (V04-02)', bool(raw_classc_identity(t)))
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), controls
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas='atlas-v0.3', base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()),
                   atlas_lines=text.count('\n') + 1, source_snapshot=SNAPSHOT, changed_sources=['PROG'], edit_operations=len(a.log),
                   retired_keys=list(newret), dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_controls=len(shared), focused_controls=len(controls),
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_4.py': sha(Path(__file__).read_bytes())},
                   limitations=['Structural checks only; no owner certificate rerun; semantic cross-reference is for the receiving review.',
                                'Only the Programme source moved; the other 17 domains were not re-extracted.',
                                'High L5 rows without an H of their own are covered by content (H1, H7, H8) and dispositioned in the release record, not forced into new H lines.',
                                'A04-06 (GEN K±/κ sign tensions, H9, F3) is deferred to the Genesis advisory; no GEN re-extraction here.'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
