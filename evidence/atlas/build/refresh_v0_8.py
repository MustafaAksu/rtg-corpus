#!/usr/bin/env python3
"""Atlas v0.7 -> v0.8 candidate: impact refresh for two moved sources — Ontological Foundations v0.11 (`ofn-v0.11`,
adopted 30 Oct 2026) and RECOG v0.3.26 (`recog-v0.3.26`, adopted 28 Oct 2026). Change-focused; no general compaction,
no Methodology migration of the atlas itself.

OFN (D1, H1, H4, H8, D-WRONG, D2 DYAD.X1/DYAD-THM-SMOOTH-EQUIVARIANT-CHART, D3 comparator edge, D4a F2/F5/F8, OPENM.U7):
source row and D1 header (17 DEF RIDs, 21 OPEN = 20 ACTIVE + 1 PARTIAL); six atlas labels renamed to the RIDs registered
in v0.11 (zero-origin, DIST-ZN, discrete reduction boundary, continuous representation); discrete imports carry the
TDR-G v2.12.14 owner RIDs; the class-C node carries the five-row regularity table (formal / polynomial C1 / transported
C^∞ C2 used / analytic OPEN / physical OPEN) with SG-19 and the qualitative radius; Standard C carries the corrected
local C³ manifold-germ test (OFN11-C01); the triad contract carries the C^∞ test class (OFN11-C02, RID retained);
narrow-Q6 carries [from: ALG] (OFN11-C03) and the C^∞ C2 instance; the single κ table; χ, N_ch notation; FMS disposition
"primary realized smooth mathematical candidate family"; lock imports with SG-19; OPA / 3B / TRIAD-CLASS / P2B inputs;
the admin queue and the token-sum row as stated in v0.11. Retired: OFN.O1, O3, O4, O5, O7, O8 (+ RRF.F6), O12, O13;
reworded: OFN.O6, O9, O11, RRF.F5, DYAD.X1, F2, F5, F8, METH.M2, OPENM.U7, NUMGEN.N-I1; new: OFN.O14.
RECOG (D3, H5): source row and D3 header; the A1b node carries the v0.3.26 [COR] (order sentences hold for the corrected
closed forms; the v0.3.25 sentences retracted in Appendix B; inequalities and E'≤0.31 unchanged); new nodes
RECOG-ALG-A1C-RECIPROCAL-DRIFT and RECOG-ALG-A1C-LOGFREE-ENVELOPE [assuming: (D5)]; the FAIL line lists the two
retracted-statement identifiers; R-D1 names the two new artifacts; R-A1 records the filed registration requests.
Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_8.py
"""
from __future__ import annotations
import hashlib, importlib.util, json, re, subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.8'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = 'f8f3b5b'   # origin/main after PR #117 (OFN v0.11 post-tag records and notices); resolved in main()
BASE_TAG = 'atlas-v0.7'
BASE_SHA = '8ebfbd1008ce96e167ec90931468d166c568294a66453824667fba88e3f49c6c'   # atlas-v0.7
MOVED = {'OFN': dict(edition='v0.11', tag='ofn-v0.11', authority='OWNER: records/ofn/OFN_v0_11_RELEASE_RECORD.md at ofn-v0.11 (+ post-tag records, PR #117)'),
         'RECOG': dict(edition='v0.3.26', tag='recog-v0.3.26', authority='OWNER: records/recog/RECOG_v0_3_26_RELEASE_RECORD.md at recog-v0.3.26')}
OFN_SHA = '38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4'
RECOG_SHA = '45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34'
NEW_RIDS = {'OFN': ['RTG-OFN-DEF-ZERO-ORIGIN', 'RTG-OFN-DEF-DIST-ZN', 'RTG-OFN-DEF-DISCRETE-REDUCTION-BOUNDARY', 'RTG-OFN-DEF-CONTINUOUS-REPRESENTATION',
                    'RTG-OFN-DEF-FINITE-DESCRIPTION', 'RTG-OFN-DEF-REDUCTION-TARGET'],
            'RECOG': ['RECOG-ALG-A1C-RECIPROCAL-DRIFT', 'RECOG-ALG-A1C-LOGFREE-ENVELOPE', 'RECOG-ART-A1C-DRIFT-CENTERING', 'RECOG-ART-A1C-CORRECTED-GRID',
                      'RECOG-ALG-A1C-TAIL-HARMONICS-LIMITS-V0325', 'RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325'],
            'TDRG': ['TDRG-DEF-ZN-STATE', 'TDRG-DEF-PHYSICAL-STATE', 'TDRG-DEF-REL-ADVANCE', 'TDRG-DEF-BAND', 'TDRG-DEF-STAR', 'TDRG-DEF-CONV-TICK', 'TDRG-DEF-CONV-P3CYC',
                     'TDRG-THM-HOLONOMY', 'TDRG-THM-NARROW-BAND-EXCLUSION', 'TDRG-THM-RECURRENCE', 'TDRG-ALG-LEM-REACH', 'TDRG-ALG-LEM-NOANNIHIL', 'TDRG-ALG-LEM-RETRIG',
                     'TDRG-ALG-LEM-SPECCONS'],
            'NUMGEN': ['NUMGEN-RESULT-N5AS1-L-BACKBONE']}
OFN_RID_COUNT = 43   # 17 DEF + 1 HYP + 4 RESULT + 21 OPEN
PIPE_COUNTS = {'closed': 6, 'dispositioned': 3, 'open': 24}
PATHS = ['records/ofn/OFN_v0_11_RELEASE_RECORD.md', 'records/recog/RECOG_v0_3_26_RELEASE_RECORD.md', 'records/recog/RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md',
         'pipes/ATLAS/20261029-RECOG-v0-3-26-adopted.md', 'pipes/TDRG/20261029-OFN-token-sum-gauge-label.md',
         'pipes/DYAD/20261029-RECOG-c7-ceilings-registration.md', 'pipes/DYAD/20261029-RECOG-d5-bridge-constants-registration.md',
         'pipes/DYAD/20261030-OFN-v0-11-adopted.md', 'pipes/FMS/20261030-OFN-v0-11-adopted.md', 'pipes/ER2B/20261030-OFN-v0-11-adopted.md']

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
        self.log.append(dict(id=f'AR08-{len(self.log)+1:03d}', finding=finding, where=where, old_sha256=sha(old), new_sha256=sha(new), old=old, new=new))
    def _one(self, prefix, finding, where):
        ls = [l for l in self.text.split('\n') if l.startswith(prefix)]
        assert len(ls) == 1, (finding, where, prefix, len(ls)); return ls[0]
    def line(self, prefix, new, finding, where): self.rep(self._one(prefix, finding, where), new, finding, where)
    def drop_line(self, prefix, finding, where): self.rep(self._one(prefix, finding, where) + '\n', '', finding, where)
    def after_line(self, prefix, new_lines, finding, where):
        l = self._one(prefix, finding, where); self.rep(l + '\n', l + '\n' + '\n'.join(new_lines) + '\n', finding, where)
    def sub_in_line(self, prefix, old, new, finding, where):
        l = self._one(prefix, finding, where); assert l.count(old) == 1, (finding, where, old[:60]); self.rep(l, l.replace(old, new), finding, where)
    def head(self, old_prefix, new_prefix, finding, where):
        """Rename a node head (line start) keeping the rest of the line."""
        l = self._one(old_prefix, finding, where); self.rep(l, new_prefix + l[len(old_prefix):], finding, where)

def refresh(a: Edit):
    O = 'OFN v0.11'
    R = 'RECOG v0.3.26'
    # ---- identity ----
    a.rep('# RTG STATE ATLAS v0.7\n', '# RTG STATE ATLAS v0.8\n', 'identity', 'title')
    a.rep('full identities in evidence/atlas/v0.7/source_manifest.json', 'full identities in evidence/atlas/v0.8/source_manifest.json', 'identity', 'SOURCES header')
    a.rep('| OFN | RTG_ONTOLOGICAL_FOUNDATIONS | v0.10 | `ofn-v0.10` | canonical Tier 2 |', '| OFN | RTG_ONTOLOGICAL_FOUNDATIONS | v0.11 | `ofn-v0.11` | canonical Tier 2 |', O, 'SOURCES OFN row')
    a.rep('| RECOG | RTG_RELATIONAL_RECOGNITION_DSN | v0.3.25 | `recog-v0.3.25` | canonical Tier 3 |', '| RECOG | RTG_RELATIONAL_RECOGNITION_DSN | v0.3.26 | `recog-v0.3.26` | canonical Tier 3 |', R, 'SOURCES RECOG row')
    a.rep('*END — RTG STATE ATLAS v0.7. Noncanonical; owner DSNs govern.*', '*END — RTG STATE ATLAS v0.8. Noncanonical; owner DSNs govern.*', 'identity', 'footer')
    a.rep('(owner RECOG = RTG_RELATIONAL_RECOGNITION_DSN v0.3.25;', '(owner RECOG = RTG_RELATIONAL_RECOGNITION_DSN v0.3.26;', R, 'D3 header')
    # ---- HEADLINE ----
    a.line('H1 D-STALE high — class C is real in C^∞:',
           'H1 D-STALE high — class C is real in C^∞: DYAD-THM-SMOOTH-EMBEDDING (B-∞ existence closed) gives a C^∞ J_ℤ6 commuting with T, and DYAD-THM-SMOOTH-EQUIVARIANT-CHART gives the C^∞ chart Φ with ΦTΦ⁻¹ commuting with A, so class C / GEN §6.3c instance C2 is non-vacuous in C^∞; only the analytic case (B-an, B-6) and physical realization are open. OFN v0.11 consumes both theorems (IMP-O10-06/07) with a five-row regularity table (formal family · real polynomial C1 · exactly transported C^∞ C2, used · analytic OPEN · physical OPEN), SG-19 (Φ inherits no finite-chart bounds) and a qualitative radius; GEN v2.9 §6.3c G-20 records the imported existence. The wording "formal / real only once J realized / existence not asserted" persists at FMS and ER-2B (F5, DYAD.X1). Fix in FMS, ER-2B.', O, 'H1')
    a.sub_in_line('H4 D-RID high —', 'with a §7 owner RID map for the consumer names — OFN\'s "RID unavailable" imports from TDR-G resolve once OFN repins (OFN.O5 ≡ METH.M2);',
                  'with a §7 owner RID map for the consumer names, and OFN v0.11 repinned its twelve TDR-G imports to them (METH.M2);', O, 'H4')
    a.sub_in_line('H5 D-LINK high —', 'the (D5) constants and the C₇ ceilings remain [assuming:] until Dyadic registers them (RECOG.R-A1).',
                  'the (D5) constants and the C₇ ceilings remain [assuming:] until Dyadic registers them (RECOG.R-A1). RECOG v0.3.26 corrects the v0.3.25 asymptotic-order sentences about the closed-form majorants ([COR]; two Appendix B retractions — they hold for the corrected forms Lg_corr with the M-dependent bracket; every inequality, E\'≤0.31, grade, RID and OPEN status unchanged) and adds the chart reciprocal drift RECOG-ALG-A1C-RECIPROCAL-DRIFT (adopted Dyadic rows only; log-free K_ε) and the log-free envelope RECOG-ALG-A1C-LOGFREE-ENVELOPE [assuming: (D5)] (E^(5)≤C(a,r)/(a+M) term by term).', R, 'H5')
    a.sub_in_line('H5 D-LINK high —', 'NUMGEN v1.21 records these theorems statement by statement as consumer-side confirmations in its §9.1 acceptance matrix (nothing imported, custody of GAP-LOCK 1–3 and INF-1 unchanged; 15/2',
                  'NUMGEN v1.21 §9.1 records the RECOG v0.3.24 A1a/A1b comparisons (RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, RECOG-THM-A1A-LIFT-ALIGNMENT, RECOG-THM-A1A-PHASE-EXISTENCE-U with RECOG-RESULT-A1A-CD-AGREEMENT, RECOG-THM-A1B-SLIP-SCHEDULE-U) statement by statement as consumer-side confirmations in its acceptance matrix — independent agreement, nothing imported, custody of GAP-LOCK 1–3 and INF-1 unchanged; for GAP-LOCK 3 the agreement covers the ratio limit and the digamma schedule is not adopted; the matrix carries no consumer acceptance of the v0.3.25/v0.3.26 additions (sharpened R9 rows, decoder and fiber results, DRIFT, ENV) (15/2', 'AV08-R1', 'H5 NUMGEN acceptance scope')
    a.sub_in_line('H8 D-SYM high —', '≡GEN γ by the OFN §11.4 / RRF §6.2a parameter convention', '≡GEN γ by the OFN §5.5.4 / §11.4 and RRF §6.2a parameter convention', O, 'H8 convention')
    a.sub_in_line('H8 D-SYM high —', 'and κ=1 vs κ=2 treated differently across the sites listed at OFN.O8 + RRF.F6 and F1.',
                  'and κ=1 vs κ=2 treatment: OFN v0.11 states one κ table (§5.5.4; κ=0 decoupled reference, κ=1 flat, κ=2 not a proved Q6 failure, 0<κ<2 κ≠1 closure-mode attraction, κ∉{0,1,2} the formal contract) to which its other sites point; the cross-family collision is F1, the convention attribution OFN.O14.', O, 'H8 κ table')
    # ---- D-WRONG ----
    a.drop_line('OFN.O7 | TDR-G LEM-RETRIG prose', O, 'D-WRONG OFN.O7 (both sides corrected)')
    # ---- D1 header and objects ----
    a.sub_in_line('(owners: OFN v0.10 adopted 2026-10-19 canonical,', 'OFN v0.10 adopted 2026-10-19 canonical', 'OFN v0.11 adopted 2026-10-30 canonical', O, 'D1 header edition')
    a.sub_in_line('(owners: OFN v0.11 adopted 2026-10-30 canonical,', 'owner counts 11 DEF RIDs, 1 HYP RID, 4 local RESULT RIDs, 21 OPEN (19 ACTIVE + 1 PARTIAL + TRIAD-CLASS)',
                  'owner counts 17 DEF RIDs, 1 HYP RID, 4 local RESULT RIDs, 21 OPEN (20 ACTIVE + 1 PARTIAL), 43 OFN RIDs; Methodology v1.4 qualifier spellings', O, 'D1 header counts')
    a.line('O-ZERO DEF(no RID) |', 'RTG-OFN-DEF-ZERO-ORIGIN DEF (atlas label O-ZERO; RID registered v0.11) | 𝒪₀=0; first dyad 0→(A,B), A+B=0 | <GEN zero-origin condition (IMP-O08-01, gen-v2.9 §6.1 cited by section; the Genesis [DEF] carries no RID, METH.M2) | ¬ creation mechanism, binary-event inevitability, exact conservation @OFN§1.3', O, 'zero-origin node')
    a.head('O-DIST-ZN DEF(no RID) |', 'RTG-OFN-DEF-DIST-ZN DEF (atlas label O-DIST-ZN; RID registered v0.11) |', O, 'DIST-ZN node')
    a.line('O-DISC-STATE DEF(import, D5 owner) |', 'O-DISC-STATE DEF(import, D5 owner) | X=(θ₁..θ_M, δ₁..δ_M)∈ℤ_N, θ_i↦θ_i+c gauge, d_ij=δ_i−δ_j (IMP-O08-02 <TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE, TDRG-DEF-REL-ADVANCE; OFN keeps its caveat on the owner phrase "only Δ_ij are physical": no token deletion); band 𝒟_k={Δ: dist_{C_N}(Δ,N/2)≤k}, even N (IMP-O08-03 <TDRG-DEF-BAND); star rule: new node at centre\'s antipodal shadow, copied token, centre token inverted (IMP-O08-09 <TDRG-DEF-STAR); advance → snapshot/classify → synchronous events (IMP-O08-14 <TDRG-DEF-CONV-TICK); successor-token path shift (IMP-O08-15 <TDRG-DEF-CONV-P3CYC); pinned tdrg-v2.12.14 with the owner §7 RID map, legacy names (CONV-*, LEM-*) as aliases; [conv: v18] and EV-NOT-RERUN kept @OFN<TDRG', O, 'discrete state node')
    a.head('O-DISC-REDUCTION DEF(no RID) |', 'RTG-OFN-DEF-DISCRETE-REDUCTION-BOUNDARY DEF (atlas label O-DISC-REDUCTION; RID registered v0.11) |', O, 'reduction-boundary node')
    a.head('O-CONT-REP DEF(no RID) |', 'RTG-OFN-DEF-CONTINUOUS-REPRESENTATION DEF (atlas label O-CONT-REP; RID registered v0.11) |', O, 'continuous-representation node')
    a.sub_in_line('O-B-Q DEF(import) |', '(pinned v2.8.5)', '(gen-v2.9 §6.1)', O, 'B-Q pin')
    a.after_line('RTG-OFN-DEF-CONTINUOUS-REPRESENTATION DEF (atlas label O-CONT-REP;', ['RTG-OFN-DEF-FINITE-DESCRIPTION DEF (RID registered v0.11) | finite current node list ≠ finite alphabet per node ≠ uniform node-count cap ≠ finite global state set; exact finite arithmetic is the adopted discrete-model practice; a continuous approximation is not substituted into its primitive update without changing that model and passing the programme firewall | >*OFN:finite-recurrence, SG-OFN-INFORMATION @OFN§4.1'], O, 'finite-description node new')
    a.sub_in_line('O-T ≡ PROG-P0-MAP DEF', '(≡ GEN-DEF-PRIMITIVE-MAP alias; OFN still cites "RID unavailable", IMP-O08-12, see L5 OFN.O3)',
                  '(≡ GEN-DEF-PRIMITIVE-MAP alias; OFN IMP-O08-12 at dyad-v6.4.22 §6.1; CUST-O09-01 answered, REQ-O09-04 fulfilled)', O, 'primitive-map node')
    a.sub_in_line('O-COMP DEF(import) |', '(pinned v0.3.20)', '(recog-v0.3.26, IMP-O08-17)', O, 'comparator pin')
    a.line('O-LOCK DEF/ALG(formal, SESSION) |', 'O-LOCK DEF/ALG (formal family; real C^∞ for 𝓕_{κ,Φ}; SESSION provenance, recorded, not registered) | 𝒮₀={(z,−z,0)}, 𝒮_±={(z,ω^{±1}z,ω^{±2}z)}, ω=λ²; invariant with I≡0; edge dynamics N≅T; cyclic relabel preserves 𝒮_±, transposition+edge reversal swaps them (= chirality datum); raw generators J=T∘F^{−1/6}, R₀=J³, G=J² (formal uniqueness IMP-O10-03; real C^∞ germ IMP-O10-06); C^∞ member: [N_Φ,A]=0 with A³=−I, A²=ω makes N_Φ odd and ω-equivariant ⇒ its lock surfaces are real C^∞ invariant submanifolds with exact isolated-dyad evolution (OFN-local ALG on IMP-O10-06/07, not a new Dyadic existence proof) @OFN§5.5.4', O, 'lock node')
    a.sub_in_line('O-CHIRAL-CONV DEF |', 'N=|u|²+|v|², S=Im(w₁w̄₂)=(|u|²−|v|²)/√12, ρ=S/N;', 'N_ch=|u|²+|v|², S=Im(w₁w̄₂)=(|u|²−|v|²)/√12, χ=S/N_ch (v0.11 symbols; v0.10 wrote ρ, N; formulas unchanged);', O, 'chiral convention')
    # ---- class C ----
    a.sub_in_line('CLASS-C DEF (RTG-OFN-DEF-TRIAD-MODEL-CONTRACT part)',
                  'contract fields: regularity formal + real C³ polynomial reps; C^∞: DYAD E4 smooth J + F3 exactly λ-equivariant smooth chart ⇒ conditional RRF reading (not adopted by OFN/GEN; OFN still writes "analytic/C^∞ conditional on DYAD OPEN 20", L5 OFN.O1); analytic conditional on DYAD B-6;',
                  'contract fields — regularity, one table used at every §5.5 site: all-order formal family (formal algebra and lock geometry; a formal series is not a real germ or a basin theorem) · real polynomial instance C1 (exists independently of smooth J; "C1" is the Genesis instance label, not differentiability) · exactly transported C^∞ instance C2, 𝓕_{κ,Φ}=(Φ⁻¹)^{×3}∘P_κ∘N_Φ^{×3}∘Φ^{×3}, exists and is used (IMP-O10-06/07 <DYAD-THM-SMOOTH-EMBEDDING, DYAD-THM-SMOOTH-EQUIVARIANT-CHART; local C^∞ hence C³; qualitative radius; no finite-chart bounds, SG-19; chart-family freedom remains) · exactly transported analytic realization OPEN (DYAD OPEN 20 B-an/B-6) · physical realization or selection OPEN (TRIAD-CLASS);', O, 'class-C regularity')
    a.sub_in_line('CLASS-C DEF (RTG-OFN-DEF-TRIAD-MODEL-CONTRACT part)',
                  'κ∉{0,1,2} formal, stability only 0<κ<2, κ≠1; κ=2 closure multiplier on unit circle, excluded from centre reduction (not a Q6 failure);',
                  'κ values, one OFN table (§5.5.4): κ=0 decoupled reference (raw B), excluded by Q6 · κ=1 flat (raw A1 fails Q4; class C flat; narrow-Q6 (i) via GEN-THM-K3-SIXSTEP-FACTOR-NOGO) · κ=2 closure multiplier −λ on the unit circle, hyperbolic centre reduction does not apply, not a proved Q6 failure (Genesis γ∈{0,2} OPEN) · 0<κ<2, κ≠1 linear closure-mode attraction |1−κ|, the range of the stability statements, not a basin theorem · κ∉{0,1,2} the formal contract;', O, 'class-C κ table')
    a.sub_in_line('CLASS-C DEF (RTG-OFN-DEF-TRIAD-MODEL-CONTRACT part)', 'registration request to RRF as model-contract row',
                  'registered by RRF as a reference-only model-contract row with a representation-level ψ-readout entry (rrf-v0.8.4 §6.2a, recorded by OFN v0.11; OPEN-B/E1 stays locked)', O, 'class-C registration')
    a.sub_in_line('⊥ ρ: dyad radial ≠ chiral ratio S/N', '⊥ ρ: dyad radial ≠ chiral ratio S/N · ⊥ N: chiral norm ≠ normal-form map',
                  '⊥ ρ: dyad radial ≠ chiral ratio S/N (OFN v0.11 writes χ=S/N_ch) · ⊥ N: chiral norm (OFN v0.11 N_ch; D4a chiral coords still N) ≠ normal-form map', O, '⊥ ρ/N')
    # ---- discrete facts used by OFN ----
    a.sub_in_line('*OFN:A8-noannihil ALG |', '<LEM-NOANNIHIL (TDRG v2.12.13 §6.5)', '<TDRG-ALG-LEM-NOANNIHIL (IMP-O08-06, tdrg-v2.12.14 §6.5)', O, 'A8-noannihil')
    a.sub_in_line('*OFN:reach ALG |', '<LEM-REACH @OFN§4.6', '<TDRG-ALG-LEM-REACH (IMP-O08-05) @OFN§4.6', O, 'reach')
    a.sub_in_line('*OFN:retrig ALG |', 'd=0 is a fixed state (OFN correction; TDRG summary "period two even at d=0" — L5 OFN.O7) <LEM-RETRIG',
                  'd=0 is a fixed state (OFN08-C12 fulfilled: TDR-G v2.12.14 states the same) <TDRG-ALG-LEM-RETRIG (IMP-O08-07)', O, 'retrig')
    a.sub_in_line('*OFN:narrow-band THM |', '<IMP-O08-04B (RID unavailable)', '<TDRG-THM-NARROW-BAND-EXCLUSION (IMP-O08-04B)', O, 'narrow-band')
    a.sub_in_line('*OFN:flat-closure THM |', '<IMP-O08-04 @OFN§2.2', '<TDRG-THM-HOLONOMY (IMP-O08-04) @OFN§2.2', O, 'flat-closure')
    a.sub_in_line('*OFN:finite-recurrence THM |', '<IMP-O08-08 |', '<TDRG-THM-RECURRENCE (IMP-O08-08) |', O, 'finite-recurrence')
    a.sub_in_line('*OFN:specs ALG |', '<LEM-SPECCONS |', '<TDRG-ALG-LEM-SPECCONS (IMP-O08-16) |', O, 'specs')
    a.sub_in_line('RTG-OFN-ALG-STAR-TOKEN-SHIFT RES(from ALG) |', 'XFER-O08-01 → TDRG proposed, not accepted;',
                  'statement accepted by TDR-G and used in SG-14 (tdrg-v2.12.14 §7); custody transfer XFER-O08-01 deferred by TDR-G to v2.13, the RID stays OFN\'s;', O, 'Finding A')
    # ---- links line ----
    a.sub_in_line('links (edges only):', '>OPEN-OFN-7; OFN pins v6.4.10 §6.14)', '>OPEN-OFN-7; OFN pins dyad-v6.4.22 §6.14, IMP-O08-20)', O, 'links PRIM-CTR pin')
    a.sub_in_line('links (edges only):', 'NUMGEN L-BACKBONE (q_M=1/M+O(M^{−3/2}), Σ_{m<M}q_m=log M+C_Q+o(1); no dedicated RID, REQ-O09-03; primitive-orbit reading OFN\'s)',
                  '<NUMGEN-RESULT-N5AS1-L-BACKBONE (RES[from ALG]; q_M=1/M+O(M^{−3/2}), Σ_{m<M}q_m=log M+C_Q+o(1); owner types q_m:=Q_true(T^{6m}x), the block-sampled primitive; REQ-O09-03 fulfilled; no domain inclusion inferred)', O, 'links L-BACKBONE')
    # ---- triad contract ----
    a.sub_in_line('RTG-OFN-DEF-TRIAD-MODEL-CONTRACT DEF |', 'Q3a full primitive edge autonomy not required; minimum = Standard C;',
                  'Q3a full primitive edge autonomy not required; minimum = Standard C in its corrected local form, with an explicitly defined, physically admissible, dynamically consistent isolation regime;', O, 'Q3a')
    a.sub_in_line('RTG-OFN-DEF-TRIAD-MODEL-CONTRACT DEF |', 'unless designation is declared state data (route C-a);',
                  'unless designation is declared state data (route C-a; necessary, not sufficient for full-state covariance; representation gate RRF-CND-01 Identity/Action, rrf-v0.8.4 §6.2, slot symmetry not identified with node exchange);', O, 'Q3b ↔ RRF-CND-01')
    a.sub_in_line('RTG-OFN-DEF-TRIAD-MODEL-CONTRACT DEF |', 'regularity real-analytic admitted test class',
                  'regularity: real C^∞ update germs admitted, real-analytic laws a distinguished subclass, each candidate states its realized regularity, formal series stay formal candidates; C³ remains Q6-REG and the Standard C manifold minimum (contract amendment OFN11-C02, v0.11; RID retained as the same versioned contract — consumers assess the amendment, METH v1.4 §4.4)', O, 'test-class regularity')
    a.line('RTG-OFN-DEF-STANDARD-C DEF |', 'RTG-OFN-DEF-STANDARD-C DEF [COR v0.11, OFN11-C01] | F_e(r)=T(r_e)+I_e(r); Standard C at cubic order ⟺ a positive-dimensional embedded C³ manifold germ M through the null state, invariant under the declared update as a germ, carrying nonzero edge states arbitrarily near 0, with one common punctured domain on which ‖I_e(r)‖≤C‖r‖⁴ for all edges and 0<‖r‖<ε; carrier, edge readout, norm (complete local network-state norm) and primitive clock declared; a singleton, a finite null-state record or an isolated trajectory does not qualify; not all edges need be nonzero (coincidence embedding admitted); recovers the isolated dyad through the μ-carrying order and the six-step return, linear order alone insufficient; quantifiers match RTG-OFN-ALG-RAW-STANDARD-C-NOGO; order fixed by PI 2026-10-18 | physical-isolation scope: I_e≡0 meets the order-four bound only on a regime satisfying the manifold, nontriviality, domain and clock requirements; algebraic cancellation establishes neither those requirements nor physical isolation; physical-isolation reading OPEN (TRIAD-CLASS) | RID retained: correction of the same proposition (old text at ofn-v0.10, Appendix B OFN11-C01) @OFN§5.5.2', O, 'Standard C')
    a.sub_in_line('COVARIANCE-DISCIPLINE node', '~ OFN Q3b C-a and Q5 express the same complete-state covariance requirement (L5 OFN.O12)',
                  'OFN v0.11 Q3b route C-a names RRF-CND-01 Identity/Action as its representation gate (necessary, not sufficient); Q5 states the complete-state covariance requirement', O, 'covariance node')
    a.sub_in_line('RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT RES(from THM+ALG) |', 'RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT RES(from THM+ALG) |',
                  'RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT RES(from ALG) (single conclusion status since v0.11, OFN11-C03, METH v1.4 §3.4; Genesis THM premises in Depends on, no promotion) |', O, 'narrow-Q6 status')
    a.sub_in_line('RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT RES(from ALG)', '(C1 real polynomial reps; C2 𝓕_{κ,Φ} conditional on C³ Φ with ΦTΦ⁻¹ commuting with A)',
                  '(C1 real polynomial reps; C2 the exactly transported 𝓕_{κ,Φ} in the real C^∞, hence C³, chart Φ of DYAD-THM-SMOOTH-EQUIVARIANT-CHART, IMP-O10-07)', O, 'narrow-Q6 C2')
    a.sub_in_line('RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT RES(from ALG)', '¬ realizes J;', '¬ analytic or physical realization;', O, 'narrow-Q6 non-claim')
    a.head('*OFN:class-C-defect ALG(formal, SESSION, unregistered) |', '*OFN:class-C-defect ALG (formal family; real C^∞ for 𝓕_{κ,Φ}; SESSION provenance, unregistered) |', O, 'defect node')
    a.sub_in_line('*OFN:class-C-realization ALG |', '| <DYAD OPEN 20 (OFN import IMP-O10-04); owner state: C^∞ existence by DYAD-THM-SMOOTH-EMBEDDING and DYAD-THM-SMOOTH-EQUIVARIANT-CHART, analytic B-6 OPEN (L5 OFN.O1) @OFN§5.5.4',
                  '| in C^∞ the object exists (<DYAD-THM-SMOOTH-EMBEDDING, IMP-O10-06) and Φ is the owner\'s chart (<DYAD-THM-SMOOTH-EQUIVARIANT-CHART, IMP-O10-07); uniqueness of J, K_m, R in the DYAD F2/F3 sense, E2 only among generators with DX′(0)=0; analytic existence DYAD OPEN 20 B-an/B-6 (IMP-O10-04) @OFN§5.5.4', O, 'realization node')
    a.sub_in_line('*OFN:FMS-disposition DEF(model policy) |', '· A2 raw 0<κ<2, κ≠1 excluded under Standard C cubic (NOGO); Q6+Q4 hold; loopholes non-manifold / finite amplitude / other carriers (OPEN-C19-L) · C transported κ-family = primary formal candidate class, "real only once J realized" (stale, OFN.O1), family with in-class modulus; other C routes open',
                  '· A2 raw 0<κ<2, κ≠1 excluded under Standard C cubic (NOGO; narrow-Q6 (i)); Q6 and Q4 capacity hold; non-manifold invariant sets and finite-amplitude regimes lie outside this test and the no-go (a proposal using them supplies its own recovery contract); other carriers OPEN-C19-L · C transported κ-family = primary realized smooth mathematical candidate family (Standard C exactly on 𝒮₀, 𝒮_±, real C^∞ for the C^∞ member; Q4 capacity; Q5 with active covariance; Q6 by IMP-O10-02 and narrow-Q6 (ii), C2 included); analytic exact realization and physical selection open; a family with an in-class modulus, not one model; other C routes open', O, 'FMS disposition')
    a.sub_in_line('*OFN:chiral-attraction ALG(leading order, SESSION) |', 'Δρ=S(1/6−2ρ²)+O(5) ⇒ |ρ|→1/√12 while |S| decays with N;', 'Δχ=S(1/6−2χ²)+O(5) ⇒ |χ|→1/√12 while |S| decays with N_ch;', O, 'chiral attraction')
    a.sub_in_line('*OFN:lock-imports DEF |', 'conditional on real surfaces (J); nothing off-surface, no separator/basin',
                  'the surfaces exist as real C^∞ submanifolds for the C^∞ member; constants hold edgewise in the dyad chart and domain where proved, qualitatively in the Φ chart unless an explicit estimate is supplied (SG-19); R9-conditional statements keep their assumption; nothing off-surface, no separator/basin', O, 'lock imports')
    # ---- frontier ----
    a.sub_in_line('  ← RTG-OFN-OPEN-OPA', 'DYAD Lemma F/F3 (removes flat ambiguity among smooth commuting realizations),',
                  'DYAD Lemma F/F3 (removes flat ambiguity among smooth commuting realizations; a real C^∞ realization exists, IMP-O10-06/07, analytic open; identifying any realization with pole exchange needs a separate ontological and representation contract),', O, 'OPA inputs')
    a.sub_in_line('  ← RTG-OFN-OPEN-BANDWIDTH (5A)', '<LEM-REACH, LEM-RETRIG, FSP, SECTOR', '<TDRG-ALG-LEM-REACH, TDRG-ALG-LEM-RETRIG, FSP, SECTOR', O, 'BANDWIDTH deps')
    a.sub_in_line('  ← RTG-OFN-OPEN-SECTOR', '<LEM-REACH, LEM-SPECCONS, TDRG OPEN-SPECCONS-STAR', '<TDRG-ALG-LEM-REACH, TDRG-ALG-LEM-SPECCONS, TDRG OPEN-SPECCONS-STAR', O, 'SECTOR deps')
    a.sub_in_line('RTG-OFN-OPEN-TIME-INDEX (7) |', '<PRIM-CTR, NUMGEN history/order/slip, L-BACKBONE, RECOG event rule', '<DYAD-THM-PRIM-CTR (IMP-O08-20), NUMGEN history/order/slip, NUMGEN-RESULT-N5AS1-L-BACKBONE, RECOG event rule', O, 'TIME-INDEX deps')
    a.sub_in_line('P2B-CRITERION node', 'v0.10 inputs: class-C lock surfaces = formal J-conditional invariant-subsystem witness (built from T in transported chart ⇒ "independently specified"? undecided);',
                  'OFN v0.11 inputs: class-C lock surfaces = a real C^∞ invariant-subsystem witness for a specified coupled triad law (IMP-O10-06/07), not closure (built from T in a transported chart ⇒ "independently specified admissible T₃"? undecided);', O, 'P2B inputs')
    a.sub_in_line('P2B-CRITERION node', '· RTG-OFN-OPEN-PRIMACY-3B · O-REDUCTION-TARGET)', '· RTG-OFN-OPEN-PRIMACY-3B · RTG-OFN-DEF-REDUCTION-TARGET (atlas label O-REDUCTION-TARGET; RID registered v0.11))', O, 'P2B citers')
    a.line('RTG-OFN-OPEN-TRIAD-CLASS (new v0.10) |', 'RTG-OFN-OPEN-TRIAD-CLASS (registered at the v0.10 adoption) | physical criterion selecting class-C member (ψ-modulus) + physical-isolation reading of Standard C + chirality dictionary <DYAD OPEN 20 B-an/B-6 (only if an analytic model is wanted), RF-O10-02, RRF §6.2a model-contract row and representation-level readout entry, FMS basin work, sub-C³ (Q6-REG), OPEN-C19-L, OPA | ¬ closed by formal invariant, "Im c=0", basin preference | next: the physical selection, isolation and chirality obligations; rrf-v0.8.4 §6.2a supplies the representation-level readout contract (primitive clock and transported chart declared; |c| reads m only up to reflection; "Im c=0" no selection principle); no sign-reading scalar for m−m* mandatory', O, 'TRIAD-CLASS')
    a.head('*OFN:continuous-closure OPEN(no RID) |', '*OFN:continuous-closure OPEN (no own RID; registry home OPEN-OFN-FRUSTRATION and OPEN-OFN-HOLONOMY-RANK since v0.11) |', O, 'continuous closure')
    a.line('admin queue (OFN) |', 'admin queue (OFN, v0.11 §12.3–§12.4) | XFER-O08-01 Finding A: statement accepted by TDR-G, custody deferred to TDR-G v2.13, RID stays OFN\'s · CUST-O09-01 answered, REQ-O09-04 fulfilled (DYAD-DEF-PRIMITIVE-MAP, Genesis alias) · REQ-O09-02 fulfilled (records/recog/RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md, 5c00f66d…9b55, with its evidence qualification) · REQ-O09-03 fulfilled (NUMGEN-RESULT-N5AS1-L-BACKBONE) · REQ-O09-05 endpoint component fulfilled (TDRG-DEF-ORIENT, SG-14 on the canonical branch, largest_center exception), custody component deferred, six-constraint list not recovered (OPEN-OFN-2) · REQ-O09-06 primary FMS closeout record (open) · REQ-O08-01 OPA definition/proof task (open) · IMP-O08-01 zero-origin cited by Genesis section (no Genesis RID) · custody: v0.10 release record and builders placed unchanged under upload/ofn-records/ (20/20 hash-checked); transported_chiral_pq.py, the FMS ψ scripts, ER-2B v0.3.1 and the v0.9 records missing', O, 'admin queue')
    # ---- constraints ----
    a.sub_in_line('*OFN:rejections (live, scoped) |', '· total additive token sum as conserved — rejection withheld pending TDRG',
                  '· total additive token sum as a physical conserved quantity — exact conservation fails on the birth-capable model: Σδ changes by −δ_A (mod N) at a star event (TDRG-DEF-STAR) and is preserved by swap, path shift and ties; the common token shift is not a full-model gauge (TDR-G SG-14); nonconservation ≠ gauge dependence; TDR-G\'s "gauge-like"/"gauge artifact" labels referred to TDR-G (pipes/TDRG/20261029-OFN-token-sum-gauge-label.md, open)', O, 'token-sum row')
    a.sub_in_line('*OFN:retired |', 'trap axiom deleted (= LEM-NOANNIHIL scope)', 'trap axiom deleted (= TDRG-ALG-LEM-NOANNIHIL scope)', O, 'retired trap axiom')
    # ---- D1.L5 ----
    for k in ('OFN.O1 (≡ DYAD.X1, GEN.D15) D-STALE high:', 'OFN.O3 D-STALE:', 'OFN.O4 D-STALE:', 'OFN.O5 D-RID (to TDRG, owner side done):', 'OFN.O7 D-WRONG/D-SCOPE (to TDRG):',
              'OFN.O8 + RRF.F6 D-SCOPE:', 'OFN.O12 ~ D-LINK:', 'OFN.O13 + D1 ⊥ D-CONV/D-SYM:'):
        a.drop_line(k, O, k.split()[0] + ' retired')
    a.line('OFN.O6 D-RID (OFN-internal):', 'OFN.O6 D-RID (OFN-internal, residual after v0.11): v0.11 registered six DEF RIDs for unchanged bodies (RTG-OFN-DEF-ZERO-ORIGIN, -DIST-ZN, -DISCRETE-REDUCTION-BOUNDARY, -CONTINUOUS-REPRESENTATION, -FINITE-DESCRIPTION, -REDUCTION-TARGET) and gave the continuous-closure block (§4.1) the registry home OPEN-OFN-FRUSTRATION / -HOLONOMY-RANK and the null-ledger block (§4.5) OPEN-OFN-IQP; still without identity: the orientation vocabulary (O-ORIENT-VOCAB), the §7.3 joint-selection item (≈ OPEN-OFN-5A); OPEN-C19-L stays a session label by owner decision.', O, 'OFN.O6 reworded')
    a.line('OFN.O9 D-STALE:', 'OFN.O9 D-STALE (low; owner-kept exception): IMP-O10-05 (§11.4) keeps "not re-verified line by line for this draft" as the evidence-access qualification of the reviewed candidate, deliberately retained at the release (v0.11 release record §3b item 2) for a later source-maintenance pass; the other v0.10 draft-tense residues (header companion line, §0.1 boundary, §0.3 "until then", RF-O10-04 "for this draft") are absent from v0.11.', O, 'OFN.O9 reworded')
    a.sub_in_line('OFN.O11 ~ D-LINK |', 'OFN IMP-O10-05 uses the DYAD OPEN 3 phase package at its recorded R9-conditional scope.',
                  'OFN v0.11 IMP-O10-05 uses the DYAD OPEN 3 phase package at its recorded R9-conditional scope, edgewise on the lock surfaces only (constants in the dyad chart; qualitative in Φ, SG-19).', O, 'OFN.O11 reworded')
    a.after_line('OFN.O11 ~ D-LINK |', ['OFN.O14 D-LINK (low; wording, new): the v0.11 κ table (§5.5.4) calls γ≡κ "the declared parameter convention of Genesis §6.3c and RRF §6.2a"; GEN v2.9 §6.3b–c writes γ only and states no κ identification (atlas-checked: gen-v2.9 §6.3b–c, L814–906, carry no κ symbol apart from the script name kappa_pq_symbolic.py; §6.8 keeps κ_f distinct from that γ and makes no parameter identification). The declaration is OFN\'s and RRF\'s, applied to the Genesis family parameter; for the next OFN edition, no scientific effect (RRF.F5).'], O, 'OFN.O14 new')
    a.sub_in_line('RRF.F5 D-LINK (owner-stated convention):', '— OFN v0.10 §11.4 (claim-level import of GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO: γ ≡ κ ∈ ℝ∖{0,2}, under (H_spec)) and RRF v0.8.4 §6.2a (γ≡κ in the OFN class-C parameter convention);',
                  '— OFN v0.11 §11.4 (claim-level import of GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO: γ ≡ κ ∈ ℝ∖{0,2}, under (H_spec)) and its §5.5.4 κ table ("not a raw/transported model identity"; attribution wording OFN.O14) and RRF v0.8.4 §6.2a (γ≡κ in the OFN class-C parameter convention);', O, 'RRF.F5 reworded')
    a.sub_in_line('METH.M2 D-RID (programme pattern):', 'AZ, Legacy imports;', 'AZ, Legacy imports, the Genesis zero-origin [DEF] (gen-v2.9 §6.1, cited by OFN IMP-O08-01 by section);', O, 'METH.M2 zero-origin')
    a.sub_in_line('METH.M2 D-RID (programme pattern):', 'TDR-G registered its claim RIDs in v2.12.14 and NUMGEN its tier 1 in v1.21;',
                  'TDR-G registered its claim RIDs in v2.12.14 (OFN v0.11 repinned to them), NUMGEN its tier 1 in v1.21 and OFN six DEF RIDs in v0.11;', O, 'METH.M2 OFN')
    # ---- D2 (Dyadic) ----
    a.sub_in_line('DYAD-THM-SMOOTH-EQUIVARIANT-CHART THM |', 'whether OFN class C uses it is OFN\'s decision;', 'OFN v0.11 class C uses it (IMP-O10-07: C2 exists and is used; narrow-Q6 (ii));', O, 'chart node consumer')
    a.sub_in_line('DYAD.X1 D-LINK |', 'OFN v0.10 §5.5.4 does not;', 'OFN v0.11 §5.5.4 consumes it (IMP-O10-06/07; C2 in the regularity table and in narrow-Q6 (ii));', O, 'DYAD.X1 OFN')
    a.sub_in_line('DYAD.X1 D-LINK |', '(≡ OFN.O1/FMS.M1/ER2B.Z2 class-C staleness, D1/D4a)', '(residual class-C staleness at FMS.M1/ER2B.Z2, F5)', O, 'DYAD.X1 residual')
    # ---- D3 (RECOG) ----
    a.sub_in_line('RECOG-DEF-POLE-COMPARATOR, RECOG-DEF-STATE-COMPARATOR DEF |', '>OFN v0.10 §6.4 (IMP-O08-17)', '>OFN v0.11 §6.4 (IMP-O08-17, recog-v0.3.26)', O, 'comparator consumer')
    a.sub_in_line('RECOG-THM-A1B-SLIP-SCHEDULE-U THM |', 'and an error E\'\'\'=O_a((1+log(a+M_k))/(a+M_k)) computable from (a, M_k, r_k) — not from the record alone; harmonic tails with the universal ceiling E\'≤0.31 (RECOG-ALG-A1C-TAIL-HARMONICS, -INBLOCK-ANGLE),',
                  'and an error bound E\'\'\' (|ε\'\'\'_k|≤E\'\'\') computable from (a, M_k, r_k) — not from the record alone; [COR v0.3.26] the order E\'\'\'=O_a((1+log(a+M_k))/(a+M_k))=o((a+M_k)^{−1/2}) holds for the corrected closed forms (Lg_corr, M-dependent bracket for q_M⁻¹; a pure O((a+M_k)⁻¹) not claimed); the v0.3.25 sentence for the majorants as then defined is retracted (Appendix B RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325: constant floor of Lg, uniform κ slack), the inequality remains valid and the reported grid values at M≤10⁵ change by less than 0.5 %; harmonic tails with the universal ceiling E\'≤0.31 (RECOG-ALG-A1C-TAIL-HARMONICS, -INBLOCK-ANGLE; limit sentences restated for the corrected forms, the v0.3.25 ones retracted as RECOG-ALG-A1C-TAIL-HARMONICS-LIMITS-V0325; cert RECOG-ART-A1C-CORRECTED-GRID),', R, 'A1b node COR')
    a.after_line('RECOG-THM-A1B-SLIP-SCHEDULE-U THM |', [
        'RECOG-ALG-A1C-RECIPROCAL-DRIFT ALG (v0.3.26) | sc: x₀∈U, chart row A, block base points; adopted rows only (DYAD-ALG-NF6 μ, a₃₂, a₀₅; DYAD-THM-NF-REM C₇=100, one-orbit contraction; part-1b closed forms), no Dyadic proof constant | (i) exact first order δ_m:=q_{m+1}⁻¹−q_m⁻¹−1=−(29/216)q_m−2Re(a₀₅e^{−6iΘ_m})q_m+R_m, |R_m|≤γ₂q_m², γ₂=212.6 (2C₇=200 of it); the isotropic coefficient 1−|μ|²−2Re a₃₂=−29/216 is exact, the sixth harmonic has zero mean · (ii) centred drift sup_m|q_m⁻¹−b̃_m|≤K_ε(a), log-free, K_ε=0.7203/0.4513/0.1860 at a=625/1000/2500 (98 % from the C₇ term), for every m≥0 and every admissible b (proof table D1–D8) · (iii) exact centring identity A₁=Λ^log_M(b)+A₁′, |A₁′|≤K_εP₂′ | NUM jet-model illustration separate (NC1–NC2) | ¬ a sharper exact-map drift (needs a Dyadic bound on Re(ρ₇/z) along an orbit, or the B1-L2 ceiling C₇≤85.1); ¬ event, carrier or Q1′ statement | cert RECOG-ART-A1C-DRIFT-CENTERING | >RECOG-ALG-A1C-LOGFREE-ENVELOPE | @§6.13b',
        'RECOG-ALG-A1C-LOGFREE-ENVELOPE ALG·c (v0.3.26) | if: [assuming: Dyadic row-A bridge proof constants c_Q=0.79246, c′_Q=0.36915 and the remainder decomposition of the DYAD-THM-LPHASE-ROWA-REMAINDER proof — proof constants, not theorem rows; registration requested] | sc: as RECOG-THM-A1C-SHARPENED-SCHEDULE with the start offset enclosed (RECOG-ALG-A1C-START-OFFSET); a known | centred envelope E^(5)_k with the log-free bracket q_M⁻¹∈[b̃_M(b⁻)−K_ε, b̃_M(b⁺)+K_ε], |ε^(5)_k|≤E^(5)_k; E^(5) is the sum of ten non-negative terms, each ≤c_i(a,r)/(a+M) for every M≥1 by its closed form ⇒ E^(5)(a,M,r)≤C(a,r)/(a+M), no floor, no logarithm (C=58.0/61.0/75.1 at r=5, a=625/1000/2500) | <RECOG-ALG-A1C-RECIPROCAL-DRIFT, RECOG-THM-A1C-SHARPENED-SCHEDULE (corrected forms), RECOG-ALG-A1C-START-OFFSET | the grid limit E^(5)(a+M)→19.15 and the 73/73 slip containment (tolerance-dominated at the latest slips) are observations, not the proof | cert RECOG-ART-A1C-DRIFT-CENTERING (G3c, G5, PT2–PT4) | @§6.13b'], R, 'DRIFT, ENV nodes new')
    a.sub_in_line('FAIL | RECOG-FAIL-K-FROM-SADDLE ·', '· termwise lattice/7-gap identity', '· termwise lattice/7-gap identity · RET v0.3.26 (Appendix B, retracted-statement identifiers, not live RIDs): RECOG-ALG-A1C-TAIL-HARMONICS-LIMITS-V0325 (limits of S̄′, R̄′, E′ scaled by √(a+M) for the majorants as then defined) and RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325 (the E\'\'\' order sentence as then defined); inequalities unaffected', R, 'RECOG FAIL line')
    a.sub_in_line('RECOG.R-D1 D-PROOF (c)/(b) |', 'RECOG-ART-A1C-DECODER, RECOG-ART-A1C-Q1PRIME-FIBER are in evidence/recog/ with hashes (naming checked, not rerun here; the v0.3.25 certificates were not rerun for the owner build either, release record §3).',
                  'RECOG-ART-A1C-DECODER, RECOG-ART-A1C-Q1PRIME-FIBER and the v0.3.26 artifacts RECOG-ART-A1C-DRIFT-CENTERING, RECOG-ART-A1C-CORRECTED-GRID are in evidence/recog/ with hashes (naming checked, not rerun here; the v0.3.25 certificates were not rerun for the owner build; the v0.3.26 drift certificate and proof-table certificate were run by the owner, release record §3).', R, 'RECOG.R-D1')
    a.line('RECOG.R-A1 D-LINK (cross-owner dependency) |', 'RECOG.R-A1 D-LINK (cross-owner dependency) | RECOG v0.3.25/v0.3.26 prove RECOG-THM-A1C-SHARPENED-SCHEDULE, the A1c decoder blocks and RECOG-ALG-A1C-LOGFREE-ENVELOPE [assuming: the Dyadic (D5) row-A bridge proof constants 0.79246, 0.36915 of the LPHASE row-A proof] and RECOG-THM-R9-SHARPENED-ROWS-C7 [assuming: C₇≤85.1 / 27.7, Dyadic\'s published NF-REM certificate values rounded up]; neither is a Dyadic theorem statement, so nothing in them is unconditional on these constants. RECOG-ALG-A1C-RECIPROCAL-DRIFT uses adopted Dyadic rows only (DYAD-ALG-NF6, DYAD-THM-NF-REM); its K_ε is 98 % the C₇=100 ceiling, so a Dyadic orbit bound on Re(ρ₇/z) would lower it (informational, pipes/DYAD/20261029-RECOG-v0-3-26-adopted.md). RECOG\'s two registration requests are filed as pipe items (pipes/DYAD/20261029-RECOG-d5-bridge-constants-registration.md, …-c7-ceilings-registration.md; open, the receiver decides). The claim audits of the builds found the constants present in dyad-v6.4.22 at statement level. RECOG still pins NUMGEN v1.20.8 (repin to v1.21 is RECOG\'s separate maintenance).', R, 'RECOG.R-A1 reworded')
    # ---- D2 pipe states ----
    a.line('NUMGEN.N-I1 D-LINK (receiver side) |', 'NUMGEN.N-I1 D-LINK (pipe states, receiver side) | at the snapshot pipes_index --check passes with 33 items in 19 inboxes — 6 closed, 3 dispositioned, 24 open. closed: NUMGEN\'s request and notice to TDR-G (after v2.12.14), RECOG\'s A1b notice to NUMGEN, OFN\'s three inbox items (NUMGEN v1.21, TDR-G v2.12.14, RECOG v0.3.26 notices; closed after ofn-v0.11, PR #117) · dispositioned: NUMGEN\'s finding and notice to RECOG; RECOG\'s v0.3.26 notice to ATLAS (accept; carried by this edition, closed by the atlas owner after its tag) · open: NUMGEN v1.21 notices to DYAD and GEN, the q* question to DYAD, the cyclic-average offer to GEN; TDR-G v2.12.14 notices to NUMGEN and AZ; RECOG v0.3.26 notices to DYAD, NUMGEN, RER and RRF and its two registration requests to DYAD ((D5) bridge constants, C₇ ceilings); OFN v0.11 notices to DYAD, ER2B, FMS, GEN, NUMGEN, PROG, RECOG, RRF, TDRG (OFN11-C01/C02 named to the consumers of §5.5) and OFN\'s token-sum label finding to TDR-G; GEN\'s κ_f items to PROG and UVM. A filed item is not adopted use; each receiver decides at its own checkpoint (CONVENTIONS §7).', 'pipes', 'NUMGEN.N-I1')
    # ---- D4a ----
    a.sub_in_line('chiral coords |', '(OFN chiral convention)', '(OFN chiral convention; OFN v0.11 writes N_ch and χ=S/N_ch)', O, 'D4a chiral coords')
    a.sub_in_line('F2 ~ D-LINK (RER.E1; high):', 'excluded by OFN v0.10 §5.5.5 (RTG-OFN-ALG-RAW-STANDARD-C-NOGO)', 'excluded by OFN §5.5.5 (RTG-OFN-ALG-RAW-STANDARD-C-NOGO; v0.11 wording unchanged in substance)', O, 'F2 pin')
    a.sub_in_line('F2 ~ D-LINK (RER.E1; high):', 'Fix: one scope sentence in RER citing OFN v0.10.', 'Fix: one scope sentence in RER citing OFN §5.5.5.', O, 'F2 fix')
    a.sub_in_line('F5 D-STALE (ER2B.Z2, FMS.M1; ≡ OFN.O1, DYAD.X1; high):', '(ER2B.Z2, FMS.M1; ≡ OFN.O1, DYAD.X1; high)', '(ER2B.Z2, FMS.M1; ≡ DYAD.X1; high; the OFN side is fixed in v0.11, IMP-O10-06/07)', O, 'F5 head')
    a.sub_in_line('F8 D-PIN/D-STALE (RER.E3, ER2B.Z5, FMS.M3):', '(i) FMS and OFN RF-O10-03 cite "ER-2B v0.3.1 §A.4" (hash 711e427a…81b4) but the corpus file is v0.3 — version identity unresolved;',
                  '(i) FMS cites "ER-2B v0.3.1 §A.4" (hash 711e427a…81b4) but the corpus file is v0.3 — version identity unresolved; OFN v0.11 RF-O10-03 cites er2b-v0.3 for its three checked uses and keeps v0.3.1 source-reported, authentication deferred;', O, 'F8 (i)')
    # ---- OPEN M ----
    a.sub_in_line('OPENM.U7 D-STALE:', 'but OFN v0.10 RF-O08-08/RF-O08-11 consume OPEN-M v0.7.1', 'but OFN v0.11 RF-O08-08/RF-O08-11 consume OPEN-M v0.7.1', O, 'OPENM.U7 pin')

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

STALE = [r'`ofn-v0\.10` \|', r'\| v0\.10 \| `ofn', r'`recog-v0\.3\.25` \|', r'\| v0\.3\.25 \| `recog', r'OFN still cites', r'OFN still writes', r'real only once J realized" \(stale',
         r'all RID unavailable', r'XFER-O08-01 → TDRG proposed', r'formal J-conditional', r'rejection withheld pending TDRG', r'exists\? OFN\.O4', r'TDRG v2\.12\.13 §6\.5',
         r'Δρ=S\(1/6', r'ρ=S/N;', r'regularity real-analytic admitted', r'RES\(from THM\+ALG\)', r'OFN v0\.10 §5\.5\.4 does not', r'conditional on real surfaces \(J\)',
         r'∃ nonempty F-invariant 𝓡']

def stale_editions(text):
    # *ATLAS:checked-* lines are dated evidence records ("sources as then read", EV-NOT-RERUN) and are left as recorded
    return [l[:90] for l in text.split('\n') if not l.startswith('*ATLAS:checked-') and any(re.search(p, l) for p in STALE)]

def retracted_unqualified(text):
    """The two v0.3.26-retracted order/limit sentences may appear only next to the corrected-form qualification or as retracted identifiers."""
    bad = []
    for l in text.split('\n'):
        if "E'''=O_a(" in l and 'corrected closed forms' not in l: bad.append(l[:90])
        if re.search(r'√\(a\+M\)\s*→\s*(0\.74850|1\.0753|5\.4646)|\\sqrt\{a\+M\}\\to(0\.74850|1\.0753|5\.4646)', l): bad.append(l[:90])
    return bad

def checker():
    spec = importlib.util.spec_from_file_location('atlas_checker', ROOT / 'tools/atlas_check.py')
    c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c); return c

def pipe_states(ref):
    files = [p for p in git('ls-tree', '-r', '--name-only', ref, 'pipes/').decode().split('\n') if re.match(r'pipes/[A-Z0-9]+/2\d+.*\.md$', p)]
    st = Counter()
    for p in files:
        m = re.search(r'^state:\s*(\S+)', at(ref, p).decode(), re.M); st[m.group(1)] += 1
    return len(files), dict(st)

def main():
    global SNAPSHOT
    SNAPSHOT = git('rev-parse', SNAPSHOT + '^{commit}').decode().strip()
    base = at(BASE_TAG, ATLAS).decode(); assert sha(base) == BASE_SHA
    a = Edit(base); refresh(a); text = a.text
    assert not stale_editions(text), stale_editions(text)
    assert not retracted_unqualified(text), retracted_unqualified(text)
    # ---- manifest ----
    old = json.loads(at(BASE_TAG, 'evidence/atlas/v0.7/source_manifest.json'))
    m = json.loads(json.dumps(old))
    for s in m['sources']:
        for k in [k for k in s if k.startswith('v0_6_')]: del s[k]
    m.update(atlas='v0.8', frozen_at='2026-10-30', repository_snapshot=SNAPSHOT, previous_atlas_tag=BASE_TAG, method_tag='atlas-v0.2', method_edition='v0.2')
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_7_edition'] = prev['edition']; s['v0_7_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] in MOVED:
            mv = MOVED[s['key']]; data = at(mv['tag'], s['path'])
            s.update(edition=mv['edition'], tag=mv['tag'], commit=git('rev-parse', mv['tag'] + '^{commit}').decode().strip(), sha256=sha(data), authority=mv['authority'])
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(SNAPSHOT, s['path']), ('snapshot/tag divergence', s['key'])
        s['v0_7_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_7_input_equality'] for x in m['sources']) == {'EQUAL': 16, 'CHANGED': 2}
    assert {x['key'] for x in m['sources'] if x['v0_7_input_equality'] == 'CHANGED'} == set(MOVED)
    assert next(s for s in m['sources'] if s['key'] == 'OFN')['sha256'] == OFN_SHA
    assert next(s for s in m['sources'] if s['key'] == 'RECOG')['sha256'] == RECOG_SHA
    wjson(OUT / 'source_manifest.json', m)
    # ---- H -> L5 ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys ----
    oldret = json.loads(at(BASE_TAG, 'evidence/atlas/v0.7/retired_l5_keys.json'))
    newret = {'OFN.O1': 'OFN v0.11 (row 1, IMP-O10-06/07): class C consumes DYAD-THM-SMOOTH-EMBEDDING and DYAD-THM-SMOOTH-EQUIVARIANT-CHART; five-row regularity table; C2 exists and is used; analytic and physical OPEN. FMS/ER-2B residue stays at F5 and DYAD.X1.',
              'OFN.O3': 'OFN v0.11 (row 16): IMP-O08-12 cites DYAD-DEF-PRIMITIVE-MAP (dyad-v6.4.22), GEN-DEF-PRIMITIVE-MAP alias; CUST-O09-01 answered, REQ-O09-04 fulfilled.',
              'OFN.O4': 'OFN v0.11 (row 5): TRIAD-CLASS next artifact and closure criterion point to the RRF v0.8.4 §6.2a readout contract; the model-contract row is recorded.',
              'OFN.O5': 'OFN v0.11 (row 9): the twelve TDR-G imports carry the v2.12.14 owner RIDs; the remaining Genesis zero-origin [DEF] without RID is a Genesis-side item under METH.M2.',
              'OFN.O7': 'OFN v0.11 (row 10): OFN08-C12 fulfilled (owner LEM-RETRIG wording at tdrg-v2.12.14 matches); D-WRONG line dropped, both sides corrected.',
              'OFN.O8': 'OFN v0.11 (row 6): one κ table in §5.5.4 to which the other sites point, with the reconciliation\'s boundaries; the convention attribution is OFN.O14.',
              'RRF.F6': 'Co-key of OFN.O8: the RRF §6.2a κ=2 wording ("excluded from centre reduction") agrees with the single OFN v0.11 κ table; no cross-site conflict remains.',
              'OFN.O12': 'OFN v0.11 (row 18): Q3b route C-a names RRF-CND-01 Identity/Action as its representation gate (necessary, not sufficient).',
              'OFN.O13': 'OFN v0.11 (row 19): χ=S/N_ch and N_ch replace ρ and N in the chiral paragraph; formulas unchanged. The general ⊥ ρ/N line in D1.L1 stays.'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    assert not set(newret) & set(oldret['retired'])
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.8 reasons in dispositions.json.'))
    # ---- shared checker ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at('atlas-v0.2', 'evidence/atlas/coverage_map_v0_2.json'))
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.8/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    # ---- RID presence in the tagged sources (naming check, not certificate replay) ----
    presence = {f'{k}:{r}': (('RID: ' + r) in src[k]) for k, rs in NEW_RIDS.items() for r in rs}
    assert all(presence.values()), [k for k, v in presence.items() if not v]
    for r in NEW_RIDS['OFN'] + NEW_RIDS['RECOG'][:4] + NEW_RIDS['NUMGEN']: assert r in text, r
    ofn_rids = sorted(set(re.findall(r'RID: (RTG-OFN-[A-Z0-9-]+)', src['OFN']))); assert len(ofn_rids) == OFN_RID_COUNT, len(ofn_rids)
    for p in PATHS: assert at(SNAPSHOT, p), p
    n_items, states = pipe_states(SNAPSHOT); assert n_items == 33 and states == PIPE_COUNTS, (n_items, states)
    # ---- dispositions ----
    def row(t, key): return next((l for l in t.split('\n') if l.startswith(key + ' ')), None)
    touched = ['OFN.O1', 'OFN.O3', 'OFN.O4', 'OFN.O5', 'OFN.O6', 'OFN.O7', 'OFN.O8', 'RRF.F6', 'OFN.O9', 'OFN.O10', 'OFN.O11', 'OFN.O12', 'OFN.O13',
               'RRF.F5', 'DYAD.X1', 'F2', 'F5', 'F8', 'METH.M2', 'OPENM.U7', 'NUMGEN.N-I1', 'RECOG.R-D1', 'RECOG.R-A1', 'PROG.G8']
    disp = []
    for key in touched:
        o = row(base, key) or next(l for l in base.split('\n') if l.startswith('OFN.O8 + RRF.F6 '))
        n = row(text, key)
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded')
        disp.append(dict(key=key, disposition=state, reason=newret.get(key, 'unchanged: the owner state it records is unchanged in OFN v0.11' if state == 'retained' else 'reworded; see edit_log.json'),
                         previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    disp.append(dict(key='OFN.O14', disposition='new', reason='see edit_log.json', previous_sha256=None, current_sha256=sha(row(text, 'OFN.O14'))))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    t = text.replace('(F5, DYAD.X1). Fix in FMS, ER-2B.', '(OFN.O1, F5, DYAD.X1). Fix in FMS, ER-2B.', 1); ctl('U1', 'H cites a retired L5 row', 'H1:OFN.O1' in h_l5_map(t)['dangling'])
    t = text + 'OFN.O3 D-STALE: reused\n'; ctl('U2', 'retired key reused', bool(c.run(t, m, src, cmap, idmap, retired, with_sources=False).fails()))
    t = text.replace('| v0.11 | `ofn-v0.11` |', '| v0.10 | `ofn-v0.10` |', 1); ctl('U3', 'SOURCES row older than manifest', bool(c.run(t, m, src, cmap, idmap, retired).fails()) or bool(stale_editions(t)))
    t = text.replace('RTG-OFN-DEF-ZERO-ORIGIN DEF (atlas label', 'RTG-OFN-DEF-ZERO-ORIGINS DEF (atlas label', 1); ctl('U4', 'new OFN RID misspelled against the source (shared checker links FAIL)', bool(c.run(t, m, src, cmap, idmap, retired).fails()))
    t = text.replace('holds for the corrected closed forms (Lg_corr,', 'holds (Lg_corr,', 1); ctl('U5', 'retracted RECOG order sentence left unqualified', bool(retracted_unqualified(t)))
    t = text.replace('primary realized smooth mathematical candidate family (Standard C', 'primary formal candidate class, "real only once J realized" (stale, OFN.O1), (Standard C', 1); ctl('U6', 'stale class-C wording reintroduced', bool(stale_editions(t)))
    t = text.replace('RECOG-ALG-A1C-RECIPROCAL-DRIFT ALG (v0.3.26)', 'RECOG-ALG-A1C-RECIPROCAL-DRIFTS ALG (v0.3.26)', 1); ctl('U7', 'new RECOG RID misspelled against the source (shared checker links FAIL)', bool(c.run(t, m, src, cmap, idmap, retired).fails()))
    t = text.replace('RES(from ALG) (single conclusion status since v0.11', 'RES(from THM+ALG) (single conclusion status since v0.11', 1); ctl('U8', 'compound narrow-Q6 status reintroduced', bool(stale_editions(t)))
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), controls
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas=BASE_TAG, base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()), atlas_lines=text.count('\n') + 1,
                   source_snapshot=SNAPSHOT, changed_sources=list(MOVED), edit_operations=len(a.log), retired_keys=list(newret), new_keys=['OFN.O14'],
                   new_node_rids=NEW_RIDS, ofn_rids_at_tag=len(ofn_rids), pipes=dict(items=n_items, **states), dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_controls=len(shared), focused_controls=len(controls),
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_8.py': sha(Path(__file__).read_bytes())},
                   limitations=['Structural checks only; no owner certificate rerun; new RIDs checked for presence in the tagged sources, not re-proved.',
                                'Impact refresh of two moved sources (OFN v0.11, RECOG v0.3.26); the other 16 domains were not re-extracted; pipe items cited as filed, receiver dispositions are not atlas sources.',
                                'OFN v0.11 §§1.3, 4.1, 4.5, 5.5, 9, 10, 11, 12.3–12.4 and RECOG v0.3.26 §6.13b and Appendix B extracted at statement level from the tagged files; proofs live in the owner cells.'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
