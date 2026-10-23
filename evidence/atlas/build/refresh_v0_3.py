#!/usr/bin/env python3
"""Reproducible, source-pinned Atlas v0.2 -> v0.3 refresh.
No owner DSN, source tag, adoption decision, or shared checker is modified.
Run from any directory inside a full-history checkout: python3 -I <this file>.
"""
from __future__ import annotations
import copy, hashlib, importlib.util, json, re, subprocess, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.3'
RECORDS = ROOT / 'records/atlas'
ATLAS_PATH = 'atlas/RTG_STATE_ATLAS.md'
RECOG_PATH = 'dsn/RTG_RELATIONAL_RECOGNITION_DSN.md'
SNAPSHOT = '9453e35cec6d5a4da076652527c13176db27f6f8'
BASE_HASH = '9963aead02fad686a9a5bd4d1824882a890ef6279d50899c4090e0e5092331c5'
RECOG_HASH = '0d5834003ce8f6819a760ac02ec4e1b65c4d34a0eb13381d0fe4e175af9ca31a'
RECOG_COMMIT = '4edaa88c6bcbbca82663e84a4c7949e188d0d9ad'
NEW_RESULT = 'RECOG-THM-A1A-PHASE-EXISTENCE-U'

def git(*args: str) -> bytes:
    return subprocess.check_output(['git', '-C', str(ROOT), *args])
def sha(data: bytes | str) -> str:
    return hashlib.sha256(data.encode() if isinstance(data, str) else data).hexdigest()
def at(ref: str, path: str) -> bytes:
    return git('show', f'{ref}:{path}')
def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

class Edit:
    def __init__(self, text):
        self.text, self.log = text, []
    def replace(self, old, new, reason, count=1):
        n = self.text.count(old)
        assert n == count, (reason, old[:90], n, count)
        self.text = self.text.replace(old, new)
        self.log.append(dict(id=f'AR03-{len(self.log)+1:03d}', operation='replace',
            locator=old.split('\n')[0][:180], old_sha256=sha(old), new_sha256=sha(new),
            occurrences=n, reason=reason))
    def line(self, prefix, new, reason):
        found = [l for l in self.text.splitlines() if l.startswith(prefix)]
        assert len(found)==1, (prefix, len(found))
        old=found[0]
        self.replace(old+'\n', '' if new is None else new+'\n', reason)
    def editline(self, prefix, old, new, reason):
        found = [l for l in self.text.splitlines() if l.startswith(prefix)]
        assert len(found)==1, (prefix, len(found))
        assert old in found[0], (prefix,old)
        self.line(prefix,found[0].replace(old,new),reason)
    def after(self,prefix,new,reason):
        found=[l for l in self.text.splitlines() if l.startswith(prefix)]
        assert len(found)==1,(prefix,len(found))
        self.line(prefix,found[0]+'\n'+new,reason)

def refresh(a: Edit):
    a.replace('# RTG STATE ATLAS v0.2', '# RTG STATE ATLAS v0.3', 'candidate edition')
    a.replace('*END — RTG STATE ATLAS v0.2.', '*END — RTG STATE ATLAS v0.3.', 'matching footer edition')
    a.replace('evidence/atlas/source_manifest_v0_2.json','evidence/atlas/v0.3/source_manifest.json','frozen source manifest')
    a.replace('| RECOG | RTG_RELATIONAL_RECOGNITION_DSN | v0.3.22 | `recog-v0.3.22` | canonical Tier 3 |',
              '| RECOG | RTG_RELATIONAL_RECOGNITION_DSN | v0.3.23 | `recog-v0.3.23` | canonical Tier 3 |','adopted owner edition')
    a.replace('(owner RECOG = RTG_RELATIONAL_RECOGNITION_DSN v0.3.22, adopted 2026-10-20;',
              '(owner RECOG = RTG_RELATIONAL_RECOGNITION_DSN v0.3.23;','D3 owner snapshot; no release narrative')
    a.line('H5 D-LINK',
      'H5 D-LINK high — explicit-domain phase existence is owner science: RECOG-THM-A1A-PHASE-EXISTENCE-U proves C_D^ext on U without R9 or INF-1 (D3). Remaining interfaces: NUMGEN has not imported this explicit-domain result; 15/2 bounds reciprocal-amplitude increments and is an ingredient, not a complete L-BACKBONE error constant (NUMGEN.N-B). C_D^ext is a candidate comparison source for φ*, not its owner or an established identification (NUMGEN.N-D, RECOG.R-L1b). GEN chrono-protection G₂=0 has candidate proof routes through the NUMGEN cyclic average and RECOG-ALG-LEADING-RETURN-EQUIVARIANCE (RECOG.R-L2); explicit GAP-LOCK inequality is NUMGEN.N-E. These remaining cross-owner identifications are ~ and require their own scope checks.',
      'A2/A3: separate adopted existence from remaining Atlas-derived interfaces')
    a.line('H12 ',
      'H12 D-SCOPE / ~ D-LINK med — j⁶S_h=j⁶R₀, with S_h=h₆∘(−I)∘h₆⁻¹ an exact involution and only degree-6 commutation certified; the C^∞ involution R=T³∘K₂⁻¹ commutes with T locally (DYAD-THM-SMOOTH-EMBEDDING). RECOG §6.14 records this distinction. Exact dynamical commutation neither discharges R1\'s physical/linear pole-swap premise nor gives raw C_W covariance; RRF OPEN-A and OPEN-OFN-OPA remain open. Transfer of the section-shadow asymptotics to R is a separate ~ question (RECOG.R-L5, RRF.F7).',
      'A1: involution, dynamical commutation, comparator covariance and physical exchange separated')
    a.editline('memory and return ·','A1A chain (D3) > DYAD bridge lemma, OPEN 9/12/21, NUMGEN L-BACKBONE/φ*',
      'A1A chain and RECOG-THM-A1A-PHASE-EXISTENCE-U (D3) > DYAD bridge lemma, OPEN 9/12/21; ~ NUMGEN explicit-domain and φ* comparison interfaces (not automatic repins)', 'cross-domain index: actual uses versus proposed interfaces')
    a.line('RRF.F7 ',
      'RRF.F7 D-SCOPE / ~ D-LINK | DYAD-THM-SMOOTH-EMBEDDING supplies a local smooth involution commuting with T; RECOG §6.14 records j⁶S_h=j⁶R₀ and the separate exact-involution / finite-commutation scopes. Neither supplies a physical action or an unchanged-raw-comparator covariance contract. RRF OPEN-A remains open; any transport of RECOG section-shadow statements to the smooth action needs its own scoped argument.',
      'A1 propagated to representation interface')
    a.line('NUMGEN.N-B ',
      'NUMGEN.N-B D-LINK | RECOG-THM-A1A-RECIPROCAL-AMPLITUDE bounds |Q_{m+1}^{−1}−Q_m^{−1}−1|<(15/2)√Q_m on U; 15/2 is an increment-bound ingredient, not the whole L-BACKBONE error constant. RECOG-THM-A1A-PHASE-EXISTENCE-U supplies R9/INF-1-independent C_D^ext existence on explicit U using DYAD-THM-LPHASE-ROWA-REMAINDER. NUMGEN v1.20.8 retains its existential domain and explicit-constant import obligation. A NUMGEN adoption requires its own same-lift/clock/domain comparison and error-budget statement; no automatic domain extension.',
      'A2: explicit upstream theorem and outstanding consumer contract')
    a.line('NUMGEN.N-D ',
      'NUMGEN.N-D D-LINK | NUMGEN\'s φ* comparison remains open. DYAD-CAND-PHISTAR-ENTRY-PHASE is not an owner RID (DYAD classification); C_D^ext, provided by RECOG-THM-A1A-CD-IDENTIFICATION and RECOG-THM-A1A-PHASE-EXISTENCE-U at their distinct scopes, is a candidate comparison source only. A separate NUMGEN proof must identify the observable, gauge, starting-state dependence and overlap domain; no φ* ownership transfer or identity is asserted.',
      'A3: candidate source not owner identity')
    # Correct only the live NUMGEN backbone readout, not archived checks or consumer pins.
    for line in list(a.text.splitlines()):
        if line.startswith('NUMGEN-RESULT-N5AS1-L-BACKBONE'):
            a.line(line.split(' | ')[0],line.replace('constant 15/2','reciprocal-increment bound 15/2 (an ingredient, not the complete backbone error constant)'), 'A2 typed backbone input')
    a.editline('DYAD-THM-LPHASE-ROWA-REMAINDER ', '| @DYAD§6.14,§7.0a',
      ' | >RECOG-THM-A1A-PHASE-EXISTENCE-U [RECOG v0.3.23 imports DYAD v6.4.22, row A] | @DYAD§6.14,§7.0a', 'record actual new RECOG use; leave NUMGEN state unchanged')
    a.editline('imports (edges only):', 'NG objects (literal, NUMGEN v1.20.7+GAP-LOCK v2):',
      'NG objects (current counterpart NUMGEN v1.20.8; valid v1.15 producer pins retained where stated; GAP-LOCK v2):', 'D3 current imports with producer pins distinguished')
    a.editline('imports (edges only):', 'C₀, P₁, P₂, Q_c=(arcsin ln2)² <DYAD-DEF-PRIMITIVE-MAP',
      'P₁, P₂ <DYAD-DEF-PRIMITIVE-MAP; C₀ <DYAD-DEF-CRITICAL-CURVE; Q_c=(arcsin ln2)² <DYAD-ALG-QC-CRITICAL-AMPLITUDE; ISP <DYAD-ALG-ISP-MAPS (DYAD v6.4.22 §7 import counterparts; statement-level audit, not certificate replay)', 'claim-level Dyadic identifiers')
    a.editline('R9 observable (', '|G|=0.0076520', '|G|=√481897/90720≈0.0076520', 'exact R9 magnitude and rounded display')
    a.editline('*RECOG:remainder-by-frame ', 'leading coefficient, k_ret, local strict contraction frame-independent',
      'leading coefficient preserved by tangent-to-identity conjugacy; linear rescaling changes its magnitude (DYAD-ALG-KP-FRAME-SCALE); k_ret and local strict contraction retain their stated invariant scope', 'qualified frame invariance')
    a.editline('*RECOG:swap-odd-rho ', '*RECOG:swap-odd-rho ALG·c', 'RECOG-ALG-SWAP-ODD-RHO ALG·c', 'owner registers existing conditional lemma')
    a.editline('RECOG-OPEN-INTERSECTION ', ' | ! RECOG.R-G1', '', 'HYP aligned at point of use; immutable OPEN prefix not grade')
    a.editline('RECOG-ALG-LEADING-RETURN-EQUIVARIANCE ', ' | ownership recommended for Dyadic (DYAD N5 acknowledged, not executed)',
      ' | custody: general-p proof RECOG-ALG-LEADING-RETURN-EQUIVARIANCE; Dyadic export identity DYAD-ALG-BRIDGE-LEMMA', 'settled custody, no advisory chronology')
    a.editline('RECOG-ALG-LEADING-RETURN-EQUIVARIANCE ', ' | ~ RECOG.R-L2, R-L4', ' | ~ RECOG.R-L2', 'remove retired custody diagnostic reference')
    a.editline('RECOG-ALG-LATTICE-STRENGTH ', '"leading-crossing" |μ|/|c₀₅|≈41.3 outside local regime | ! RECOG.R-S2 (41.3 is raw-frame)',
      '"leading-crossing" ratios |μ|/|c₀₅^raw|≈41.2694355 and |μ|/|a₀₅|≈59.1194304 (post-H₂), both outside local regime', 'frame-labelled ratios; no stale diagnostic')
    a.editline('RECOG-ALG-LATTICE-CLOCK ', ' | ~ RECOG.R-L3;',
      ' | alternative direct R9/first-passage proof is not installed (D3.L3);', 'deferred alternative proof stays open, not a grade promotion')
    a.editline('*RECOG:R9-corollary ', '*RECOG:R9-corollary THM', 'RECOG-THM-R9-COMPARATOR-INCOMPLETENESS THM', 'owner RID for existing exact-map corollary')
    a.editline('RECOG-THM-R9-COMPARATOR-INCOMPLETENESS ', ' | ! RECOG.R-R2 (no RID)', '', 'registered corollary no longer RID gap')
    a.editline('RECOG-THM-R9-COMPARATOR-INCOMPLETENESS ', ': 1.48×10⁻⁵ (row |z|≤1/20), 4.69×10⁻⁵', ': ≈1.4800743×10⁻⁵ (row |z|≤1/20), ≈4.6944689×10⁻⁵', 'witness-window rounded values')
    a.line('*RECOG:R9-budget ',
      '*RECOG:R9-budget ALG | degree≥7 partial contribution ≤2C₇q₀² (200q₀² on |z|≤1/20, 60q₀² on |z|≤1/40); max_Θ|Λ₁|=|G|=√481897/90720; associated partial-budget thresholds q₀<|G|/(2C₇)≈3.83×10⁻⁵ / 1.28×10⁻⁴ | full R9 bound per row: |M−c_iso q₀|≤|G|q₀+C₂q₀², |M|≤(|c_iso|+|G|)q₀+C₂q₀²; C_z, normalized q₀; leading amplitude alone is not a bound for the whole exact memory; witness windows |G|/C₂ are distinct | one-return sign bound |χ₁(−z)−χ₁(z)|≤2C₇|z|⁶ (RRF) same order, not an input | cert recog_r11_chart_ledger_cert.py (8) | @RECOG§3 SG-R10,§6.13a,§6.14',
      'partial degree-seven budget versus complete R9 remainder')
    a.editline('RECOG-DEF-A1A-PHASE-INTERFACE DEF', '<NUMGEN-DEF-N5AS1-DEFECT (cited "RID unavailable", v1.20.7; ! RECOG.R-P2)',
      '<NUMGEN-DEF-N5AS1-DEFECT, NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT [NUMGEN v1.20.8 §6.6]', 'owner current imports')
    a.line('RECOG-THM-A1A-LIFT-ALIGNMENT ',
      'RECOG-THM-A1A-LIFT-ALIGNMENT THM | sc: U_T of DYAD-THM-PRIM-CTR | π/6<δ_T(x)<π/2 for every x∈U_T; x₀∈U, integer M≥1 ⇒ D_M^U=Θ_W(0)−Θ_W(M) | proof: exact W(Tx)/(λW) identity, 4R+(4/3)R²=143209/750000<1/2 at R=47/1000; six-step increments lie in (π,3π), so no branch ambiguity | <DYAD-THM-PRIM-CTR [DYAD v6.4.22]; >RECOG-THM-A1A-PHASE-EXISTENCE-U | ~ explicit counterpart of NUMGEN L-MONO requires consumer scope comparison (NUMGEN.N-L5) | cert RECOG-ART-A1A-C1-CHECK | @RECOG§6.13b',
      'lift alignment home and current dependency without retired R-L1')
    a.editline('RECOG-THM-A1A-RECIPROCAL-AMPLITUDE ', ' | @',
      ' | 15/2 is the reciprocal-increment bound, not a complete L-BACKBONE error constant; estimates are orbitwise unless additional uniform bounds are supplied | @', 'A2 point-of-use scope')
    a.editline('RECOG-THM-A1A-RECIPROCAL-AMPLITUDE ', 'constant 15/2 is the explicit L-BACKBONE constant NUMGEN lacks; RECOG.R-L1, D2 N-B', 'increment bound 15/2 is one input to a consumer backbone estimate; NUMGEN.N-B', 'retired existence diagnostic replaced with consumer interface')
    a.editline('RECOG-THM-A1A-PHASE-EXISTENCE-ALT ', 'if: H-NG (lim_M(D_M^U−τlog M) exists for the orbit)',
      'if: H-NG (orbitwise limit hypothesis on U; INF-1 discharges it only on U∩U_NUMGEN; ~ denotes any broader Atlas comparison, not an identity of theorems)', 'A4 do not identify domains of H-NG and INF-1')
    a.editline('RECOG-RESULT-A1A-PHASE-EXISTENCE-NG ', ' | ~ upgradable to THM on explicit U (RECOG.R-L1)',
      ' | separate explicit-U theorem: RECOG-THM-A1A-PHASE-EXISTENCE-U; this NUMGEN-route statement retains its overlap domain', 'preserve existing route, no silent regrade')
    a.editline('RECOG-THM-A1A-CD-IDENTIFICATION ', 'v1.3', 'v1.4', 'conditional-proof grammar current edition')
    a.editline('RECOG-THM-A1A-CD-IDENTIFICATION ', 'candidate owner', 'candidate comparison source', 'A3 no phi ownership identification')
    a.after('RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION ',
      'RECOG-THM-A1A-PHASE-EXISTENCE-U THM | sc: postulated T; every x₀∈U={0<Q₀≤1/625}; x_m=T^{6m}x₀, Q_m=Q(x_m), a=Q₀⁻¹; N block count | C_D^ext=lim_N(D_N^U−τlog N)=τH(a)+τΣ_{m≥0}(Q_m−1/(a+m))−Σ_{m≥0}r_m; H(a)=−log a+Σ_{m≥0}[1/(a+m)−log(1+1/(a+m))]=−ψ(a), ψ digamma; all three series absolutely convergent | D_N^U=Σ_{m<N}(τQ_m−r_m), |r_m|≤(403/250)Q_m^{3/2}; Q_m⁻¹=a+m+O_{x₀}(√m) | Ψ_{z,∞}=Ψ_{W,∞}=Θ_W(0)−C_D^ext and C_D^ext=τlog Q₀−M_W | <DYAD-THM-LPHASE-ROWA-REMAINDER [DYAD v6.4.22 §6.14, row A, primitive Q, base U / intermediate U_T], DYAD-THM-PRIM-CTR, RECOG-THM-A1A-LIFT-ALIGNMENT, RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, RECOG-THM-A1A-PHASE-EXISTENCE-ALT | R9 and NUMGEN INF-1 not used | ¬ R9-free c_iso/Λ₁/C₂ or quantitative OPEN21; ¬ chart-variable memory formula without R9; ¬ comparator incompleteness; ¬ starts in U_T∖U; ¬ NUMGEN domain/grade extension; ¬ physical memory or event mechanism; no new uniform numerical error budget | cert RECOG-ART-A1A-EXISTENCE-U (written proof cell plus NUM illustration, not a numerical proof); @RECOG v0.3.23 §6.13b',
      'adopted explicit-U theorem; independent proof route, not research suggestion')
    a.editline('*RECOG:A1a-scope ', '(a) is the only R9-free claim, only on the existential intersection',
      '(a) R9-free on the overlap; RECOG-THM-A1A-PHASE-EXISTENCE-U R9/INF-1-free on explicit U', 'two distinct R9-free routes')
    a.line('*RECOG:relabeling-Sh ',
      '*RECOG:relabeling-Sh ALG (convention / typed owner import) | S_h=h₆∘(−I)∘h₆⁻¹ is an exact involution on h₆(D); 𝒥_{≤6}(f∘S_h−S_h∘f)=0, only degree-6 commutation certified; j⁶S_h=j⁶R₀ | C_W(S_ht,S_ht)−C_W(t,t)=3t³/2+O(t⁴); raw C_W is not exactly S_h-covariant | DYAD-THM-SMOOTH-EMBEDDING supplies a distinct C^∞ local dynamical involution R commuting with T, DR(0)=−I | ¬ identify S_h with R as full maps; ¬ transfer finite-chart radius/constants; ¬ discharge R1 physical/linear pole-swap premise; ¬ infer raw-comparator covariance from RT=TR; ¬ close RRF OPEN-A or OPEN-OFN-OPA | <DYAD v6.4.22 §§6.15–6.17; RRF convention reference | cert recog_r11_chart_ledger_cert.py (9) | @RECOG§6.14',
      'A1 exact involution versus finite jet commutation; full refusal list')
    # RESULT labels follow actual v0.3.23 owner block decisions; these are not new grades.
    for prefix, grade in [('*RECOG:prerequisite-ladder','ALG'),('*RECOG:radial-fate-law','ALG'),('*RECOG:order-rigid','ALG'),('*RECOG:unification','ALG'),('*RECOG:comparator-incompleteness-truncated','ALG'),('*RECOG:R5-restated','ALG'),('*RECOG:radial≠rank-entry','THM'),
       ('*RECOG:R7-independence','THM'),('RECOG-RESULT-TWIN-QC-DEGENERACY','ALG'),
       ('RECOG-RESULT-EVENT-UNDERDETERMINATION','THM'),('*RECOG:F2a-table','ALG'),
       ('RECOG-RESULT-P2-FOLD-NO-REGISTERED-RETENTION','ALG'),('*RECOG:Btoken-Rlog','ALG'),
       ('*RECOG:criterion-table','ALG'),('RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH','ALG'),
       ('*RECOG:F3-outcome','ALG'),('RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS','DEF'),
       ('*RECOG:F4-alignment','DEF')]:
        matches=[l for l in a.text.splitlines() if l.startswith(prefix+' ')]
        assert len(matches)==1, prefix
        line=matches[0]; assert ' RES' in line,prefix
        new=line.replace(' RES',f' RES[from {grade}]',1)
        a.line(prefix+' ',new,'owner RESULT pairing; statement/scope retained')
    a.line('*RECOG:tokenisation-consequence ',
      '*RECOG:tokenisation-consequence RES[from NUM strong] | sc: F2(b) campaign 12 orbits / 87 slips; leading law RECOG-ALG-CHART-SHADOW | primitive B-event is the NUMGEN-named physical return-section token (not a physical-event verdict); 7-gap determined by raw window 0≤o_j<Δ_j=O(Q); chart lag crossings have the same asymptotic clock but no termwise identity; shadow displacement ±3/(16√Q) blocks, unbounded absolute count and O(√Q) relative time | @RECOG§6.16a\n*RECOG:tokenisation-schema RES[from ALG] | lattice thresholds fail representation safety (O(√Q) shadow versus O(Q) deciding window) and return-word transition; NG 7-gap changes word 6→7 and transported-section safety is RECOG-ALG-BTOKEN-TRANSPORT | ¬ selection of the recognition event | @RECOG§6.16a–b',
      'owner separates numerical token and algebraic schema conclusions')
    a.line('*RECOG:R-E-separation ',
      '*RECOG:R-E-retention RES[from THM] | registered package has independent retention without transition: RECOG-THM-R9-MEMORY in rank-safe tube | @RECOG§6.16d\n*RECOG:R-E-transition RES[from ALG] | sc: registry-relative | fold supplies transition/noninjectivity without registered retention; B/7-gap is a representation-safe dynamically distinguished token under transported section | ¬ selection of the recognition event; R6 requires selection and independent write-through | @RECOG§6.16a–d',
      'owner split retention and transition/token statuses')
    a.editline('*RECOG:F3-common-driver ', ' | VF-1 ≡ DYAD-ALG-NF6-DEG10 (RECOG.R-L8)', '', 'V1 remove retired diagnostic field without composing a self-equivalence')
    a.editline('*RECOG:F3-common-driver ', 'VF-1', 'DYAD-ALG-NF6-DEG10 (VF-1)', 'V1 retain the explicit owner citation in the statement')
    a.editline('RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS ', '>RRF v0.8.3 §6.3 (RF-1: RRF restates W3 across spaces), RER v0.2 G9',
      '>RRF v0.8.4 §6.3 (W3 quoted verbatim with RID at RECOG v0.3.21; inter-space transport is a separate RRF OPEN extension; RF-1 fulfilled as a content state, not a notice receipt), RER v0.2 G9', 'V2 current RRF consumer edge with its actual RECOG pin and separate extension')
    a.line('closed (constraints only) |', None, 'closed lifecycle modules not open frontier')
    a.after('*RECOG:F4-alignment ',
      '*RECOG:closed-modules DEF | closed lifecycle: R2 RECOG-OPEN-KRET-P (NU3-NONVANISHING); R7 RECOG-OPEN-TWIN-ACCESS (scoped twin theorems); R8 RECOG-OPEN-P2-HET-ENTRY (P2-HET); R9 RECOG-OPEN-LATTICE-MEMORY-NF (R9-MEMORY); R10 RECOG-OPEN-RETURN-ENCLOSURE (delivered/accepted owner package); R11 RECOG-OPEN-QUINTIC-FRAME (CHART-LAWS). These keys do not replace result RIDs. Physical relabeling remains RRF OPEN-A; historical specifications do not reopen these modules | @RECOG§2',
      'explicit shared lifecycle home without changing census')
    a.editline('non-blocking |', 'explicit radius for R9-free A1a route (RECOG says none; available per RECOG.R-L1)',
      'alternative internal R9-to-lattice-clock proof (first-passage thresholds and vanishing overshoot; current ALG import route unchanged); section-shadow transfer to the exact smooth involution (jet premise and domain to be checked)', 'deferred scientific alternatives stay OPEN, no advisory keys')
    a.editline('RECOG-OPEN-EVENT-RULE (R6)', 'ACTIVE (priority)', 'ACTIVE', 'no process-priority assertion in Atlas')
    a.after('RECOG-OPEN-EVENT-RULE (R6)',
      '*RECOG:event-carrier-interface OPEN | proposed local carrier study: declare event predicate, state/carrier, update and background/channel decomposition; test fold branch information after the common image rather than assign a token log retrospectively. A non-smooth boundary signature or independently registered event-gated channel can supply a sufficient C2 witness, not a necessary classification of all admissible carriers. No F5 theorem or new carrier is registered in this owner edition; network inheritance still needs OPEN-B→E1→E2 and W1–W5 | <RECOG-ALG-CONTINUOUS-CARRIER-NOWRITE | provenance: PI decision 23 Oct 2026, records/recog/ATLAS_ADVISORY_RECOG_v0_3_22_DISPOSITION_RECONCILIATION.md §5 at snapshot 9453e35cec6d5a4da076652527c13176db27f6f8; proposal not in RECOG v0.3.23',
      'F5 scope as prospective task, not installed science or necessary nonsmoothness')
    a.editline('SG-R10 lattice scopes:', 'Λ leading order; thresholds mathematical, "event" HYP',
      'Λ leading order; whole-memory bound |M−c_iso q₀|≤|G|q₀+C₂q₀² per row on C_z; partial 2C₇ budget is distinct; thresholds mathematical, "event" HYP', 'valid SG-R10 guard with complete R9 bound')
    a.editline('forbidden overclaims ', 'A1a: universal C_D, explicit radius for the R9-free route, R9-free coefficients/C₂',
      'A1a: universal C_D, extension of the R9-free theorem to U_T∖U, R9-free coefficients/C₂', 'remove obsolete explicit-U prohibition; preserve new boundary')
    a.editline('export protocol (§6.9;', 'R9-MEMORY with C_z track and window q₀<|G|/C₂ only',
      'R9-MEMORY on its certified C_z row domains; RECOG-THM-R9-COMPARATOR-INCOMPLETENESS on smaller witness windows q₀<|G|/C₂; RECOG-THM-A1A-PHASE-EXISTENCE-U at explicit U with its nonclaims', 'do not conflate full R9 and witness domains')
    a.editline('export protocol (§6.9;', 'RRF v0.8.3', 'RRF v0.8.4', 'current consumer edition; its actual historical RECOG pin preserved')
    # Diagnostic dispositions: no resolved rows left in live Atlas.
    retired = {
      'RECOG.R-L1':'Explicit-U R9/INF-1-free existence is registered by the owner; residual NUMGEN interface is NUMGEN.N-B.',
      'RECOG.R-L3':'Alternative clock proof is an open scientific task in D3.L3, not an adopted proof or regrade.',
      'RECOG.R-L4':'Proof/export custody stated by both owners; no unsettled ownership recommendation.',
      'RECOG.R-L7':'Owner import table and adopted A1a use record the R9 dependency; conditional theorem grades unchanged.',
      'RECOG.R-L8':'VF-1 cited by DYAD-ALG-NF6-DEG10 in the owner.',
      'RECOG.R-S2':'Raw and post-H2 ratios explicitly frame-labelled.',
      'RECOG.R-G1':'Hypothesis grade aligned; OPEN in immutable RID is not live status.',
      'RECOG.R-R3':'Immutable-prefix nonissues removed; canonical home and E2C custody supplied.',
      'RECOG.R-P2':'NUMGEN definition and INF-1 imported at v1.20.8 by their owner RIDs.',
      'RECOG.R-T2':'Current guard, routing and adopted T1/T2 use reconciled; leading-only warning remains valid.'}
    for key, reason in retired.items():
        a.line(key+' ',None,reason)
    a.line('RECOG.R-L1b ',
      'RECOG.R-L1b ~ D-LINK | C_D^ext is a candidate comparison source for NUMGEN φ*, not its owner node. RECOG-THM-A1A-CD-IDENTIFICATION supplies the R9 chart formula; RECOG-THM-A1A-PHASE-EXISTENCE-U supplies the explicit-U R9-free existence route. Identifying φ* needs a separate NUMGEN proof with its gauge, readout and starting-state conventions; DYAD-CAND-PHISTAR-ENTRY-PHASE remains an owner-denied name.', 'A3 scoped candidate comparison')
    a.line('RECOG.R-L5 ',
      'RECOG.R-L5 ~ D-LINK | RECOG §6.14 records exact S_h involution, degree-6 commutation, j⁶S_h=j⁶R₀ and the distinct smooth R of DYAD-THM-SMOOTH-EMBEDDING. The prospective transfer of RECOG-ALG-SH-SECTION-SHADOW to R(Σ_B) requires a scoped jet/domain comparison; no new section-shadow theorem is installed. Physical exchange and raw-comparator covariance do not follow from RT=TR; R1, RRF OPEN-A and OPEN-OFN-OPA stay open.', 'A1 remove false premise-discharge claim, retain genuine candidate link')
    a.line('RECOG.R-R2 ',
      'RECOG.R-R2 D-RID | separately exported subclaims without dedicated owner RID include P2-HET/C0-FIRST corollaries, radial-fate law, discriminant, χ₆ and fixed-point inventory, finite p=5/7 coefficients, Re(λ̄ν₃)=−sin²(θ/2), chart comparator tracks, S_h action, partial R9 budget and A1a finite-block identity. Named sub-statements must be cited under their actual owner homes and scope; no automatic RID invention. The comparator-incompleteness and swap-odd-rho claims have their own RIDs.', 'registered versus named sub-statements; owner not forced to invent identifiers')
    a.line('RECOG.R-P3 ',
      'RECOG.R-P3 D-SCOPE | §7.1/§7.2 audit tables retain historical pins and receipt wording under the owner live-file exception. These are not current adoption/notice assertions; current §7 claim imports and §7.3 consumer records govern their stated use. A reader must not silently upgrade RRF/RER/OFN historical pins to RECOG v0.3.23.', 'recorded history exception, not false current-state conflict')
    a.line('RECOG.R-T1 ',
      'RECOG.R-T1 D-SCOPE | retained R8/R9 specifications, former R11 [OPEN] sub-items and R7 closed Active sub-items are historical under the explicit owner exception. Current census: R1/R3 PARTIAL; R4/R5/R6 ACTIVE; R2/R7–R11 CLOSED. Residual presentation risk is mistaking the retained specifications for live research obligations; no scientific closure is reversed.', 'partial live-file exception accurately scoped')
    a.editline('RECOG.R-Y1 ', '— M(z₀) and block count M appear in the same formula C_D^ext=lim_M(D_M^U−τlog M)=…−M(z₀)',
      '— §6.13b defines M as a block count and M(z₀), M_W as functions, with N used in the new theorem; existing cross-context overload remains a typing concern, not an undefined quantity', 'notation line resolves undefined-use reading')
    a.line('RECOG.R-D1 ',
      'RECOG.R-D1 D-PROOF (c)/(b) | evidence custody and execution are separate: repository inventory recovers the named RECOG §8 scripts/packages except the Dyadic-side dyad_referee_p2b_v2.py; 24 hash-cited historical or unavailable items remain listed by the owner recovery inventory, not claimed here to have been executed. Arb/R9/B3/E2C proof runs retain their original execution provenance; no fresh scientific certificate replay is supplied by this Atlas. CHART-SHADOW has its written derivation and numerical script; absence of an additional symbolic certificate is not refutation. The reciprocal-amplitude and explicit-U existence theorems have in-ledger written proofs.', 'artifact recovery updates availability, not proof grade or replay state')
    # Remaining short references to removed diagnostics must resolve at content homes.
    for old,new in [('RECOG.R-L1)', 'RECOG-THM-A1A-PHASE-EXISTENCE-U)'),
                    ('RECOG.R-L1,', 'RECOG-THM-A1A-PHASE-EXISTENCE-U,'),
                    ('RECOG.R-L8)', 'DYAD-ALG-NF6-DEG10)')]:
        if old in a.text:
            a.replace(old,new,'content target replaces retired diagnostic',count=a.text.count(old))
    # Accepted, non-scientific presentation correction from the v0.2 receiving review.
    line=next(l for l in a.text.splitlines() if l.startswith('*ATLAS:checked-D2 '))
    start=line.index('DZT N_+(M_p)=')
    end=line.index('; p=12 reduced norm',start)
    item=line[start:end]
    assert '80-digit evaluation' in item
    line=line[:start]+line[end+2:]
    line=line.replace('| numerical:', '| numerical: '+item+'; ',1)
    a.line('*ATLAS:checked-D2 ',line,'move 80-digit norm evaluations into numerical evidence; exact p12 remains exact')
    return retired

def final_interfaces(a):
    a.line('OFN.O11 ',
      'OFN.O11 ~ D-LINK | OFN IMP-O10-05 uses the DYAD OPEN 3 phase package at its recorded R9-conditional scope. RECOG-THM-A1A-PHASE-EXISTENCE-U supplies a separate R9-free existence route on U, not an automatic removal of the R9 premise from T1/T2 or OPEN21. Any OFN lock-surface import change requires a claim/domain/observable comparison and an owner decision; no physical consequence follows from phase existence alone.',
      'explicit existence does not discharge every R9-dependent consumer claim')
    a.editline('NUMGEN-RESULT-N5AS1-INF1 ', 'explicit-U existence of C_D via RECOG R-L1 (RECOG-owned; L5 NUMGEN.N-B)',
      'separate explicit-U existence of C_D^ext by RECOG-THM-A1A-PHASE-EXISTENCE-U (not an extension of NUMGEN INF-1; NUMGEN.N-B)', 'owner theorem replaces derived link without consumer regrade')
    a.editline('E2C-ENG-SPLIT-REFINEMENT ', ' | ! RECOG.R-R3', ' | custody: RECOG local engineering identifier, unchanged historical spelling', 'E2C local custody is declared')
    a.replace(' | ! RECOG.R-R3', '', 'immutable RID category is not live grade', count=3)
    a.editline('PROG.G4 ', 'RECOG v0.3.22', 'RECOG v0.3.23', 'current owner comparison; Programme source not repinned')
    a.editline('NUMGEN.N-G1 ', 'RECOG v0.3.22', 'RECOG v0.3.23', 'downstream grade-of-use mismatch remains')
    a.editline('RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION ',
       '(ALG formal second order, remainder not certified there)',
       '(ALG; formal second order, remainder certified separately by OPEN21)', 'current imported qualifier spelling; dependency unchanged')
    a.editline('RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION ',
       'source check A1a-E2 PASS on DYAD v6.4.18 (not a recertification)',
       'current import DYAD v6.4.22; A1a-E2 is a source check on v6.4.18; current quoted-statement audit is not a historical byte comparison or recertification', 'pin and evidence edition kept distinct')
    a.editline('RECOG-THM-A1A-CD-IDENTIFICATION ',
       'candidate comparison source node for NUMGEN\'s unowned φ*',
       'candidate comparison source for NUMGEN φ*; no identification or ownership transfer', 'A3 tightened point of use')
    # The direct theorem node keeps all original exact algebra and proof-input values.
    a.editline('RECOG-THM-A1A-LIFT-ALIGNMENT ',
       'proof: exact W(Tx)/(λW) identity, 4R+(4/3)R²=143209/750000<1/2 at R=47/1000;',
       'proof: W(Tx)=λW+λ(η−sinη)+ω(e^ρ−1−ρ), ω²=−1−ω; |ρ|,|η|≤(2/√3)|W|<2R, R=47/1000, 2R<ln2; |η−sinη|<(8/6)|W|³, |e^ρ−1−ρ|<4|W|²; relative error <4R+(4/3)R²=143209/750000<1/2;', 'retain exact local proof-input facts')
    # Preserve the prospective block displacement fact separately rather than drop it.
    a.editline('RECOG.R-L5 ', 'requires a scoped jet/domain comparison;',
       'has candidate leading displacement ±3/(8√Q) from j²R=j²S_h, but requires a scoped jet/domain comparison;', 'prospective shadow value remains unadopted')


def manifest_and_sources():
    old=json.loads(at('atlas-v0.2','evidence/atlas/source_manifest_v0_2.json'))
    m=copy.deepcopy(old)
    m.update(atlas='v0.3',frozen_at='2026-10-23',repository_snapshot=SNAPSHOT,
       previous_atlas_tag='atlas-v0.2',method_tag='atlas-v0.2',method_edition='v0.2')
    observations=[]
    for s in m['sources']:
        previous=next(x for x in old['sources'] if x['key']==s['key'])
        s['v0_2_edition']=previous['edition'];s['v0_2_input_sha256']=previous['sha256']
        oldbytes=at(previous['tag'],previous['path'])
        assert sha(oldbytes)==previous['sha256'],s['key']
        if s['key']=='RECOG':
            s.update(edition='v0.3.23',tag='recog-v0.3.23',commit=RECOG_COMMIT,
              sha256=RECOG_HASH,authority='OWNER: records/recog/RECOG_v0_3_23_RELEASE_RECORD.md at recog-v0.3.23, §11')
        data=at(s['tag'],s['path']); resolved=git('rev-parse',s['tag']+'^{commit}').decode().strip()
        assert sha(data)==s['sha256'] and resolved==s['commit'],s['key']
        assert data==at(SNAPSHOT,s['path']),('snapshot/tag divergence',s['key'])
        s['v0_2_input_equality']='EQUAL' if data==oldbytes else 'CHANGED'
        observations.append(dict(source=s['key'],bytes=len(data),sha256=sha(data),commit=resolved,
          previous_equal=data==oldbytes,snapshot_equals_tag=True))
    assert Counter(x['v0_2_input_equality'] for x in m['sources'])=={'EQUAL':17,'CHANGED':1}
    return m,observations


def checker_module():
    spec=importlib.util.spec_from_file_location('atlas_checker', ROOT/'tools/atlas_check.py')
    c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
    return c


def recog_inventory(c, source, text):
    # Historical Appendix A/B entries are not new governing declarations.
    live=source.split('## Appendix A')[0]
    rows=c.tag_declarations(live)
    own={rid:line for rid,line in rows.items() if rid.startswith('RECOG-')}
    atlas=c.Atlas(text)
    report=[]
    for rid,line in sorted(own.items()):
        if '-ART-' in rid:
            # Artifact inventory records declaration, source line and scope separately.
            # A registry/index ID need not be a second scientific node in the Atlas.
            occurrences=atlas.occurrences(rid)
            report.append(dict(id=rid,type='artifact',status='DECLARATION_INVENTORIED',
              owner_line=live[:live.index(line)].count('\n')+1,source_line_sha256=sha(line),
              atlas_occurrences=[n for n,k in occurrences],
              note='Evidence identity, not a scientific-result coverage PASS; availability/execution not inferred.'))
            continue
        direct=atlas.node_lines(rid)
        shared=[]
        if not direct and rid.startswith('RECOG-OPEN-'):
            shared=[i for i,l in enumerate(atlas.lines) if l.startswith('*RECOG:closed-modules ') and c.tokpat(rid).search(l)]
        if not direct and not shared:
            report.append(dict(id=rid,type='scientific',status='FAIL',reason='No explicit scientific or reviewed lifecycle home'))
            continue
        i=(direct or shared)[0]
        report.append(dict(id=rid,type='scientific',status='PASS',
          home_kind='direct' if direct else 'closed-lifecycle',home_line=i+1,
          home_id=atlas.node_id(atlas.lines[i]),home_sha256=sha(atlas.lines[i]),
          owner_line=live[:live.index(line)].count('\n')+1,source_line_sha256=sha(line)))
    return report


def scope_checks(text, retired, source):
    checks=[]
    def check(name, ok):checks.append(dict(id=name,result='PASS' if ok else 'FAIL'))
    def line(prefix):
        hits=[l for l in text.splitlines() if l.startswith(prefix)]
        return hits[0] if len(hits)==1 else ''
    check('edition-presentation', text.startswith('# RTG STATE ATLAS v0.3\n') and text.rstrip().endswith('*END — RTG STATE ATLAS v0.3. Noncanonical; owner DSNs govern.*'))
    n=line(NEW_RESULT+' ')
    check('new-result-home',n.startswith(NEW_RESULT+' THM |'))
    check('explicit-U-and-series',all(s in n for s in ['0<Q₀≤1/625','τH(a)','−ψ(a)','absolutely convergent']))
    check('no-R9-or-INF1-proof-dependency','R9 and NUMGEN INF-1 not used' in n and '<RECOG-THM-R9-MEMORY' not in n)
    check('unchanged-domain-and-quantitative-nonclaims',all(s in n for s in ['¬ starts in U_T∖U','¬ R9-free c_iso/Λ₁/C₂ or quantitative OPEN21','¬ NUMGEN domain/grade extension']))
    check('preserve-R9-chart-route','<RECOG-THM-R9-MEMORY' in line('RECOG-THM-A1A-CD-IDENTIFICATION '))
    check('preserve-NUMGEN-overlap-route','sc: x₀∈U∩U_NUMGEN' in line('RECOG-RESULT-A1A-PHASE-EXISTENCE-NG '))
    check('swap-odd-premise','if: pole-swap covariance HYP' in line('RECOG-ALG-SWAP-ODD-RHO '))
    check('no-physical-swap-discharge','¬ discharge R1 physical/linear pole-swap premise' in line('*RECOG:relabeling-Sh '))
    check('backbone-input-not-full-constant','not the whole L-BACKBONE error constant' in line('NUMGEN.N-B '))
    check('phi-comparison-not-ownership','not its owner node' in line('RECOG.R-L1b '))
    check('F5-sufficient-not-necessary','not a necessary classification' in line('*RECOG:event-carrier-interface '))
    check('clock-alternative-remains-open','alternative internal R9-to-lattice-clock proof' in line('non-blocking |'))
    check('R6-active-and-closed-census','ACTIVE' in line('RECOG-OPEN-EVENT-RULE ') and 'R10 RECOG-OPEN-RETURN-ENCLOSURE' in line('*RECOG:closed-modules '))
    check('new-artifact-support','cert RECOG-ART-A1A-EXISTENCE-U' in n)
    check('no-retired-diagnostics',not any(re.search(r'(?<![A-Za-z0-9_.-])'+re.escape(k)+r'(?![A-Za-z0-9_-])',text) for k in retired))
    check('full-R9-vs-partial-budget',all(s in line('*RECOG:R9-budget ') for s in ['partial contribution','full R9 bound','|G|/C₂']))
    check('DZT-numeric-not-exact', 'DZT N_+(M_p)=' in line('*ATLAS:checked-D2 ').split('| numerical:')[1])
    f3=line('*RECOG:F3-common-driver ')
    check('V1-direct-owner-citation', f3.count('DYAD-ALG-NF6-DEG10')==1 and f3.endswith('| <RECOG-THM-R9-MEMORY | @§6.16f'))
    f4=line('RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS ')
    check('V2-current-RRF-consumer', all(s in f4 for s in ['>RRF v0.8.4 §6.3', 'RECOG v0.3.21', 'inter-space transport is a separate RRF OPEN extension']) and '>RRF v0.8.3' not in f4)
    f5=line('*RECOG:event-carrier-interface ')
    check('V3-record-sourced-proposal', all(s in f5 for s in ['<RECOG-ALG-CONTINUOUS-CARRIER-NOWRITE', 'PI decision 23 Oct 2026', 'records/recog/ATLAS_ADVISORY_RECOG_v0_3_22_DISPOSITION_RECONCILIATION.md §5', 'proposal not in RECOG v0.3.23']) and '@RECOG§6.16f–g' not in f5)
    check('postulated-generator-wording', 'sc: postulated T;' in n)
    # This is a scoped structural guard list, not a proof checker.
    return checks


def focused_controls(c, text, src, retired):
    controls=[]
    def mutate(cid, old, new, expected):
        assert text.count(old)>=1,cid
        altered=text.replace(old,new,1)
        failed=[r['id'] for r in scope_checks(altered,retired,src) if r['result']=='FAIL']
        controls.append(dict(id=cid,expected_failure=expected,failures=failed,detected=expected in failed))
    mutate('U01 remove new result home',NEW_RESULT+' THM |','*TEST:missing OPEN |','new-result-home')
    mutate('U02 widen start domain','every x₀∈U={0<Q₀≤1/625}','every x₀∈U_T','explicit-U-and-series')
    mutate('U03 remove R9-free scope','R9 and NUMGEN INF-1 not used','no dependency declaration','no-R9-or-INF1-proof-dependency')
    bound=next(l for l in text.splitlines() if l.startswith(NEW_RESULT+' '))
    mutate('U04 remove domain boundary',bound,bound.replace('¬ starts in U_T∖U','starts unrestricted'),'unchanged-domain-and-quantitative-nonclaims')
    n=next(l for l in text.splitlines() if l.startswith('RECOG-RESULT-A1A-PHASE-EXISTENCE-NG '))
    mutate('U05 widen old NUMGEN route',n,n.replace('sc: x₀∈U∩U_NUMGEN','sc: x₀∈U'),'preserve-NUMGEN-overlap-route')
    mutate('U06 physical covariance inference','¬ discharge R1 physical/linear pole-swap premise','discharges R1','no-physical-swap-discharge')
    mutate('U07 remove swap lemma assumption','if: pole-swap covariance HYP','without covariance premise','swap-odd-premise')
    mutate('U08 false full backbone constant','not the whole L-BACKBONE error constant','the whole L-BACKBONE error constant','backbone-input-not-full-constant')
    mutate('U09 necessity overclaim','not a necessary classification','a necessary classification','F5-sufficient-not-necessary')
    mutate('U10 phi ownership','not its owner node','its owner node','phi-comparison-not-ownership')
    mutate('U11 evidence pointer removed','cert RECOG-ART-A1A-EXISTENCE-U','cert unidentified','new-artifact-support')
    altered=text+'\nRECOG.R-L1 ~ D-LINK | obsolete fixture\n'
    failed=[r['id'] for r in scope_checks(altered,retired,src) if r['result']=='FAIL']
    controls.append(dict(id='U12 retired diagnostic',expected_failure='no-retired-diagnostics',failures=failed,detected='no-retired-diagnostics' in failed))
    # Coverage must not count a bare dependency after deleting the new theorem home.
    lines=[l for l in text.splitlines() if not l.startswith(NEW_RESULT+' ')]
    inv=recog_inventory(c,src,'\n'.join(lines))
    controls.append(dict(id='U13 RID left in dependencies is not coverage',detected=any(r['id']==NEW_RESULT and r['status']=='FAIL' for r in inv)))
    mutate('U14 mismatched footer', '*END — RTG STATE ATLAS v0.3.', '*END — RTG STATE ATLAS v0.2.', 'edition-presentation')
    f3=next(l for l in text.splitlines() if l.startswith('*RECOG:F3-common-driver '))
    mutate('V1 duplicate self-equivalence', f3, f3.replace(' | @§6.16f', ' | DYAD-ALG-NF6-DEG10 ≡ DYAD-ALG-NF6-DEG10 | @§6.16f'), 'V1-direct-owner-citation')
    f4=next(l for l in text.splitlines() if l.startswith('RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS '))
    mutate('V2 stale RRF edge', f4, f4.replace('>RRF v0.8.4 §6.3', '>RRF v0.8.3 §6.3'), 'V2-current-RRF-consumer')
    f5=next(l for l in text.splitlines() if l.startswith('*RECOG:event-carrier-interface '))
    mutate('V3 proposal wrongly sourced to DSN', f5, f5.split(' | provenance:')[0]+' | @RECOG§6.16f–g', 'V3-record-sourced-proposal')
    mutate('V4 generator wording regression', bound, bound.replace('sc: postulated T;', 'sc: selected T;'), 'postulated-generator-wording')
    return controls


def main():
    OUT.mkdir(parents=True,exist_ok=True);RECORDS.mkdir(parents=True,exist_ok=True)
    base=at('atlas-v0.2',ATLAS_PATH);assert sha(base)==BASE_HASH
    source=at('recog-v0.3.23',RECOG_PATH);assert sha(source)==RECOG_HASH
    assert at('recog-v0.3.23',RECOG_PATH)==at(SNAPSHOT,RECOG_PATH)
    assert git('merge-base','--is-ancestor','97b0425',SNAPSHOT)==b''
    method=at('atlas-v0.2','atlas/RTG_STATE_ATLAS_METHOD.md')
    assert (ROOT/'atlas/RTG_STATE_ATLAS_METHOD.md').read_bytes()==method
    m,sources=manifest_and_sources()
    a=Edit(base.decode());retired_new=refresh(a);final_interfaces(a)
    text=a.text
    # All shared source and scientific owner files remain untouched.
    write_json(OUT/'source_manifest.json',m)
    (ROOT/ATLAS_PATH).write_text(text,encoding='utf-8')
    oldret=json.loads(at('atlas-v0.2','evidence/atlas/retired_l5_keys_v0_2.json'))
    retired=oldret['retired']+list(retired_new)+[x.replace('RECOG.','RECOG ') for x in retired_new]
    write_json(OUT/'retired_l5_keys.json',dict(retired=retired,note='Keys not reused; v0.3 reasons in dispositions.json.'))
    c=checker_module();src=c.load_sources(m)
    cmap=json.loads(at('atlas-v0.2','evidence/atlas/coverage_map_v0_2.json'))
    idmap=json.loads(at('atlas-v0.2','evidence/atlas/owner_identifier_map_v0_2.json'))
    report=c.run(text,m,src,cmap,idmap,retired)
    meta=dict(atlas=ATLAS_PATH,atlas_sha=sha(text),manifest='evidence/atlas/v0.3/source_manifest.json')
    c.write_report(report,str(OUT/'atlas_check_report.md'),meta)
    write_json(OUT/'atlas_check_report.json',dict(meta=meta,rows=report.rows))
    assert not report.fails(),report.fails()
    shared=c.self_test(m,src,cmap,idmap,retired,text)
    write_json(OUT/'shared_controls.json',[dict(name=n,item=i,as_expected=b) for n,i,b in shared])
    assert all(x[2] for x in shared),shared
    coverage=recog_inventory(c,source.decode(),text)
    assert not any(r['status']=='FAIL' for r in coverage),[r for r in coverage if r['status']=='FAIL']
    write_json(OUT/'recog_coverage.json',coverage)
    checks=scope_checks(text,retired,source.decode());assert all(r['result']=='PASS' for r in checks),checks
    controls=focused_controls(c,text,source.decode(),retired);assert all(r['detected'] for r in controls),controls
    write_json(OUT/'scope_checks.json',checks);write_json(OUT/'negative_controls.json',controls)
    write_json(OUT/'source_checks.json',sources);write_json(OUT/'edit_log.json',a.log)
    oldd3=base.decode().split('## D3 ')[1].split('## D4a ')[0]
    diagnostics=[l for l in oldd3.splitlines() if l.startswith('RECOG.R-')]
    dispositions=[]
    for l in diagnostics:
        key=l.split()[0];current=next((n for n in text.splitlines() if n.startswith(key+' ')),None)
        state='retired' if key in retired_new else ('retained' if current==l else 'reworded')
        reasons={'RECOG.R-L1b':'A3: comparison source is not phi-star ownership; both phase existence routes are distinguished.', 'RECOG.R-L5':'A1: physical covariance not discharged; smooth section-shadow transfer stays an unadopted proposal.', 'RECOG.R-R2':'Two new maintenance RIDs no longer missing; residual named sub-statements remain owner-scoped.', 'RECOG.R-P3':'Owner-adopted historical audit exception, not a live repin or receipt claim.', 'RECOG.R-T1':'Owner live-file exception preserves historical specs without reopening closed modules.', 'RECOG.R-Y1':'Notation is expressly typed by the owner; remaining symbol overload is a scoped concern.', 'RECOG.R-D1':'Recovered evidence availability distinguished from execution; missing historical hashes remain listed.'}
        reason=retired_new.get(key,reasons.get(key,'Unchanged owner statement, dependency and diagnostic scope.'))
        dispositions.append(dict(key=key,disposition=state,reason=reason,previous_sha256=sha(l),current_sha256=sha(current) if current else None))
    write_json(OUT/'dispositions.json',dispositions)
    counts=Counter(r['disposition'] for r in dispositions)
    covcounts=Counter((r['type'],r['status']) for r in coverage)
    # Same inputs must generate exactly the same Atlas bytes; no numerical science reruns.
    replay=Edit(base.decode());refresh(replay);final_interfaces(replay);assert replay.text==text
    for s in m['sources']:
        assert (ROOT/s['path']).read_bytes()==at(SNAPSHOT,s['path'])
    identities={ATLAS_PATH:sha(text),'atlas/RTG_STATE_ATLAS_METHOD.md':sha(method),
      'evidence/atlas/v0.3/source_manifest.json':sha((OUT/'source_manifest.json').read_bytes()),
      'tools/atlas_check.py':sha((ROOT/'tools/atlas_check.py').read_bytes()),
      'evidence/atlas/build/refresh_v0_3.py':sha(Path(__file__).read_bytes())}
    summary=dict(status='DRAFT_REVIEW_READY',source_snapshot=SNAPSHOT,source_tag='recog-v0.3.23',
      source_sha256=RECOG_HASH,atlas_sha256=sha(text),atlas_bytes=len(text.encode()),
      method_changed=False,owner_files_changed=False,source_rows=18,unchanged_source_bytes=17,
      changed_source_bytes=1,edit_operations=len(a.log),d3_diagnostic_dispositions=dict(counts),
      recog_scientific_homes=sum(r['type']=='scientific' for r in coverage),
      recog_artifact_declarations=sum(r['type']=='artifact' for r in coverage),
      scope_checks=len(checks),negative_controls=len(controls),shared_controls=len(shared),
      shared_counts={ch:report.count(ch) for ch in c.CHECKS},identities=identities,
      independent_scientific_certificate_replays=0,build_replay_identical=True,
      limitations=['Structural checks do not establish semantic completeness or mathematical truth.',
       'Source manifests authenticate tagged bytes, not historical v0.1 extraction-input equality.',
       'Artifact declarations/names do not establish execution; inherited reports are source-reported.',
       'Consumer pins remain at their actual editions; Atlas refresh is not downstream adoption.',
       'FC-22 clock derivation and smooth section-shadow transfer remain unadopted research tasks.'])
    write_json(OUT/'verification_summary.json',summary)
    header='''# RTG State Atlas v0.3 — change-focused review packet\n\n**Date:** 23 October 2026. **Prepared by:** ChatGPT, Atlas co-owner.\n**Status:** DRAFT / NONCANONICAL — review requested, no PI acceptance or owner-science adoption.\n\n'''
    packet=header+f'''## 1. Inputs and identities\n\nBase `atlas-v0.2`, SHA-256 `{BASE_HASH}`. Freeze `{SNAPSHOT}` after the authorized records-only merge of PR #22. RECOG source `recog-v0.3.23`, commit `{RECOG_COMMIT}`, SHA-256 `{RECOG_HASH}`. All 18 tagged files and resolved commits were checked; 17 are byte-identical to v0.2 inputs and only RECOG differs. Earlier v0.1 equality unknowns are not silently resolved. Method v0.2 and shared checker are unchanged.\n\n'''
    packet+='| Object | SHA-256 |\n|---|---|\n'+''.join(f'| `{p}` | `{h}` |\n' for p,h in identities.items())
    packet+=f'''\n## 2. Review scope\n\nRead the new theorem and owner-corrected passages against the tagged DSN; the complete D3 record set was inventoried, and every RECOG declaration was scanned. This is an impact-based refresh of D3, affected cross-domain edges and diagnostics, not a fresh full-corpus scientific audit. The owner cycle summary routes the work; the adopted source and frozen release record control it. No inherited proof campaign was rerun.\n\n- Add the adopted `RECOG-THM-A1A-PHASE-EXISTENCE-U` and its evidence identity, preserving U, clock, primitive Q, no-R9/INF-1 premise chain, and all nonclaims. Preserve the old NUMGEN and R9 proof routes.\n- Replace two Atlas surrogate labels with the owner comparator-incompleteness and swap-odd-rho RIDs. Carry RESULT pairings and the two owner splits; no Atlas regrading.\n- Apply A1–A5 at H5/H12, D3, OFN/RRF and NUMGEN interfaces: smooth commutation is not physical/comparator covariance; 15/2 is an input; phi-star is not identified; actual INF-1 use is distinguished from Atlas correspondence; obsolete R9-custody diagnostic removed.\n- Update current imports by claim, retain intentional historical consumer pins. Availability reflects recovered records; no receipt/adoption or replay is fabricated.\n- Preserve R1/R3 PARTIAL, R4/R5/R6 ACTIVE, and R2/R7–R11 CLOSED. Owner-authorized historical blocks are not live OPENs. F5 is a prospective interface task, not a theorem in v0.3.23.\n- R-L3 is moved to an open scientific frontier item: the deferred clock proof is not declared adopted. Section-shadow transfer remains open.\n- Move the DZT 80-digit evaluation list to numerical evidence; exact product/p=12 algebra remains distinct. General compression is excluded.\n\n## 3. Dispositions and mechanical checks\n\n{len(dispositions)} existing D3 diagnostic records: {dict(counts)}. Full reasons and hashes: `evidence/atlas/v0.3/dispositions.json`. Retired IDs are not reused or left dangling. `{len(a.log)}` exact-once operations; reproducible by `python3 -I evidence/atlas/build/refresh_v0_3.py`; edit locators and hashes in `edit_log.json`.\n\nRECOG inventory: {summary['recog_scientific_homes']} scientific/definition/lifecycle homes, {summary['recog_artifact_declarations']} artifact declarations inventoried separately. Artifact declarations are not extra scientific-result PASSes. The coverage file pins source and home lines by hash; shared closed-module homes are explicit.\n\nShared checker: zero FAIL; {len(shared)}/{len(shared)} controls as expected. Additional scoped guards: {len(checks)}/{len(checks)} PASS; negative fixtures {len(controls)}/{len(controls)} detected. Reports in `evidence/atlas/v0.3/`. Unverified links, naming-only artifact checks and inherited wording warnings remain separate; see the report rather than interpreting exit 0 as a proof of completeness. Two builds give identical Atlas bytes.\n\n## 4. Questions for receiving review\n\nCheck the new theorem's scoped extraction, preservation of old routes and consumer pins, all A1–A5 sites, the RESULT pairing splits, and the retained/moved/deleted L5 dispositions. Check that the owner live-file exception and unadopted F5/clock/shadow work were not promoted or silently erased. No full certificate replay or size-compression review is requested.\n\n## 5. Publication boundary\n\nThe candidate is not accepted by this build. PI acceptance must identify these bytes, followed by merge commit and an annotated `atlas-v0.3` tag. No owner DSN, scientific grade, source tag, notice state, or consumer adoption is changed. `atlas-v0.2` remains the accepted Atlas until that decision.\n'''
    packet += """
## 6. Receiving-review corrections V1–V3

Basis: Claude's receiving review `records/atlas/ATLAS_V0_3_RECEIVING_REVIEW.md` at immutable commit `afdef2bf2ae9e40f42cb42fde6facc5756d322e0` (separate review branch), verdict REVISE — three corrections, then ACCEPT. This is the producer response; the requested receiving readback of the three sites and new hash remains pending.

- V1: remove the retired R-L8 pointer field before inserting the direct VF-1 owner citation; no self-equivalence remains.
- V2: F4's consumer is RRF v0.8.4; its actual RECOG v0.3.21 pin remains explicit. W3 uses one space; inter-space transport is a separate RRF OPEN extension. Content fulfilment is not notice receipt.
- V3: F5 stays a prospective OPEN task, anchored to CONTINUOUS-CARRIER-NOWRITE, but its proposal is sourced to the PI decision in the reconciliation record §5 at the frozen snapshot, not to a nonexistent DSN F5 cell. This record is supplementary proposal provenance, not a nineteenth scientific owner source.
- Optional wording: the new theorem says postulated T, matching its owner.

Four targeted guards and four negative fixtures cover these edits. No scientific source, Method, shared checker, disposition count or adoption field is changed. The previously accepted scientific scope is not reopened.
"""
    (RECORDS/'ATLAS_V0_3_REVIEW_PACKET.md').write_text(packet,encoding='utf-8')
    release='''# RTG State Atlas v0.3 — acceptance record\n\n**Status:** DRAFT — receiving corrections V1–V3 implemented; final receiving readback and PI decision pending.\n**Object:** derived NONCANONICAL Atlas; acceptance adopts no owner science.\n\n## 1. Candidate identities\n\n'''
    release+='| Object | SHA-256 |\n|---|---|\n'+''.join(f'| `{p}` | `{h}` |\n' for p,h in identities.items())
    release+=f'''\n## 2. Basis and limits\n\nMethod v0.2; `records/atlas/ATLAS_V0_3_REVIEW_PACKET.md`; source and verification manifests under `evidence/atlas/v0.3/`. Source freeze `{SNAPSHOT}`; the only changed scientific source is RECOG v0.3.23. Retain checker UNVERIFIED/documented-unresolved results, historical v0.1 input limitations, non-replayed inherited certificates, unchanged consumer pins, and the RECOG historical-block exception. General compression and unadopted research remain outside this acceptance.\n\n## 3. Decision\n\n- Receiving review: Claude, 23 Oct 2026, `records/atlas/ATLAS_V0_3_RECEIVING_REVIEW.md` at commit `afdef2bf2ae9e40f42cb42fde6facc5756d322e0`: REVISE (V1–V3). Corrections implemented; final receiving readback pending.\n- PI acceptance: pending; not supplied by this generator.\n- Annotated tag after acceptance and merge: `atlas-v0.3`, naming the final Atlas SHA-256.\n- No Atlas merge, tag, or owner-science adoption is performed by this build.\n'''
    (RECORDS/'RTG_STATE_ATLAS_v0.3_RELEASE_RECORD.md').write_text(release,encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
