#!/usr/bin/env python3
"""Atlas v0.5 -> v0.6 candidate: impact refresh for one moved source — Number Genesis v1.21 (`numgen-v1.21`, adopted
26 Oct 2026; release record records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md; atlas row checks PR #77). No other source moved.

NUMGEN (D2, D5, H4, H5, H8, H9, cross-domain index): source row; Methodology v1.4 declared (every [RESULT] paired, no
bounded migration); DYAD-THM-LPHASE-ROWA-REMAINDER imported at §6.6 (pin dyad-v6.4.22, producer v6.4.19; the OPEN
explicit-constant sub-item closed; L-PHASE itself keeps its existential form); RECOG v0.3.24 explicit-domain theorems
recorded as consumer-side confirmations in the §9.1 acceptance matrix (nothing imported, custody unchanged); §6.2 domain
alias table U_NG, U_NG,tube, U_D,base, U_D,tube, U_R,base (U_NG ≡ RECOG's U_NUMGEN); five result RIDs
(NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET, -GAPLOCK-COUNT, -GAPLOCK-SLIP-RATIO, NUMGEN-RESULT-N5AS1-INF2,
NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE); pins Programme v1.3, Genesis v2.9, Q403 v6.4.18; evidence-state clause (§9.2);
DYAD-ALG-P5-RADIAL owner alias of ΔQ₅; φ* vs C_D^ext comparison conventions pinned, identity OPEN; C7C-M4 HOLD with the
TDR-G request in pipes/TDRG/; sampled L-PHASE range live as [NUM].
Retired: NUMGEN.N-S1, N-L3, N-L5, N-L7, N-G1, N-T2, N-T3. New: NUMGEN.N-I1 (five v1.21 notices awaiting receiver dispositions).
Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_6.py
"""
from __future__ import annotations
import hashlib, importlib.util, json, re, subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.6'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = '38ed5bb'   # origin/main after PR #78 (NUMGEN v1.21 post-tag notices); resolved to the full id in main()
BASE_SHA = 'cf250c9140e6ee26c65b2497a2a61dc1e326a69574d590132f0cea9646a2b0e5'   # atlas-v0.5
MOVED = {'NUMGEN': dict(edition='v1.21', tag='numgen-v1.21', authority='OWNER: records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md at numgen-v1.21')}
NEW_RIDS = ['NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET', 'NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT', 'NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO',
            'NUMGEN-RESULT-N5AS1-INF2', 'NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE']
PIPE_TDRG = 'pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md'
PIPE_DYAD = 'pipes/DYAD/20261026-NUMGEN-q-star-branch-split.md'
PIPE_GEN = 'pipes/GEN/20261026-NUMGEN-cyclic-average-route-to-g2-zero.md'

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
        self.log.append(dict(id=f'AR06-{len(self.log)+1:03d}', finding=finding, where=where, old_sha256=sha(old), new_sha256=sha(new), old=old, new=new))
    def _one(self, prefix, finding, where):
        ls = [l for l in self.text.split('\n') if l.startswith(prefix)]
        assert len(ls) == 1, (finding, where, prefix, len(ls)); return ls[0]
    def line(self, prefix, new, finding, where): self.rep(self._one(prefix, finding, where), new, finding, where)
    def drop_line(self, prefix, finding, where): self.rep(self._one(prefix, finding, where) + '\n', '', finding, where)
    def after_line(self, prefix, new_lines, finding, where):
        l = self._one(prefix, finding, where); self.rep(l + '\n', l + '\n' + '\n'.join(new_lines) + '\n', finding, where)
    def sub_in_line(self, prefix, old, new, finding, where):
        l = self._one(prefix, finding, where); assert l.count(old) == 1, (finding, where, old[:60]); self.rep(l, l.replace(old, new), finding, where)

def refresh(a: Edit):
    # ---- identity ----
    a.rep('# RTG STATE ATLAS v0.5\n', '# RTG STATE ATLAS v0.6\n', 'identity', 'title')
    a.rep('full identities in evidence/atlas/v0.5/source_manifest.json', 'full identities in evidence/atlas/v0.6/source_manifest.json', 'identity', 'SOURCES header')
    a.rep('| NUMGEN | RTG_NUMBER_GENESIS_DSN | v1.20.8 | `numgen-v1.20.8` | canonical Tier 2 common home |', '| NUMGEN | RTG_NUMBER_GENESIS_DSN | v1.21 | `numgen-v1.21` | canonical Tier 2 common home |', 'NUMGEN move', 'SOURCES NUMGEN row')
    a.rep('*END — RTG STATE ATLAS v0.5. Noncanonical; owner DSNs govern.*', '*END — RTG STATE ATLAS v0.6. Noncanonical; owner DSNs govern.*', 'identity', 'footer')
    a.rep('(sources: DYAD v6.4.22 · NUMGEN v1.20.8 (continuous + abstract modules; DISC realizations → D5) ·',
          '(sources: DYAD v6.4.22 · NUMGEN v1.21 (Methodology v1.4 declared, every [RESULT] paired; continuous + abstract modules; DISC realizations → D5) ·', 'NUMGEN move', 'D2 header')
    # ---- HEADLINE ----
    a.rep('PREL has one RID in total (PREL.P5); NUMGEN GAP-LOCK lemmas unnumbered; FMS R4′',
          'PREL has one RID in total (PREL.P5); NUMGEN v1.21 registered GAP-LOCK 1–3, INF-2 and the cyclic-average theorem, its C7C/DISC/ten-label results stay under module RIDs (NUMGEN.N-R1); FMS R4′', 'NUMGEN NB-07', 'H4')
    a.rep('Remaining interfaces: NUMGEN has not imported this explicit-domain result; 15/2 bounds reciprocal-amplitude increments and is an ingredient, not a complete L-BACKBONE error constant (NUMGEN.N-B).',
          'NUMGEN v1.21 records these theorems statement by statement as consumer-side confirmations in its §9.1 acceptance matrix (nothing imported, custody of GAP-LOCK 1–3 and INF-1 unchanged; 15/2 typed as the per-block increment, not an L-BACKBONE constant — NUMGEN.N-B) and imports the explicit L-PHASE constant from DYAD-THM-LPHASE-ROWA-REMAINDER at §6.6 while its own L-PHASE keeps the existential tube (NUMGEN.N-A).', 'NUMGEN NA-01/NA-02', 'H5')
    a.rep('GEN chrono-protection G₂=0 has candidate proof routes through the NUMGEN cyclic average and RECOG-ALG-LEADING-RETURN-EQUIVARIANCE (RECOG.R-L2);',
          'GEN chrono-protection G₂=0 has candidate proof routes through NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE (offered to Genesis in pipes/GEN/, undecided by the receiver) and RECOG-ALG-LEADING-RETURN-EQUIVARIANCE (RECOG.R-L2);', 'NUMGEN NC-15', 'H5')
    a.rep('and κ=1 vs κ=2 treated differently across the sites listed at OFN.O8 + RRF.F6 and F1; U/U_T denote both NUMGEN\'s existential tube and DYAD\'s explicit PRIM-CTR tube (NUMGEN.N-S1). The owner corpus carries a cross-stream κ table (Programme v1.3 §8.2, navigation only; the collisions themselves remain). Advice: rename NUMGEN tube.',
          'and κ=1 vs κ=2 treated differently across the sites listed at OFN.O8 + RRF.F6 and F1. The owner corpus carries a cross-stream κ table (Programme v1.3 §8.2, navigation only; the collisions themselves remain). The U/U_T collision is settled on the NUMGEN side: v1.21 §6.2 labels U_NG, U_NG,tube, U_D,base, U_D,tube, U_R,base (U_NG ≡ RECOG\'s U_NUMGEN) and asserts no inclusion between U_NG and U_D,base.', 'NUMGEN NA-03', 'H8')
    a.rep('and blocks NUMGEN C7C M-4 — needs a TDR-G scientific ruling (D5.X1).',
          'and blocks NUMGEN C7C M-4 (v1.21 §2 item 1: HOLD; request filed as ' + PIPE_TDRG + ') — needs a TDR-G scientific ruling (D5.X1).', 'NUMGEN I06', 'H9')
    # ---- cross-domain index ----
    a.rep('⊥ NUMGEN existential U/U_T (cited as §6.12 by ER2B.Z4)', '⊥ NUMGEN existential U_NG/U_NG,tube (v1.21 §6.2 alias table; cited as §6.12 by ER2B.Z4)', 'NUMGEN NA-03', 'index PRIM-CTR line')
    a.rep('~ NUMGEN explicit-domain and φ* comparison interfaces (not automatic repins)', '~ NUMGEN explicit-domain confirmations (v1.21 §9.1 matrix) and φ* comparison interfaces (not automatic repins)', 'NUMGEN NA-01', 'index memory line')
    # ---- D2 L2 nodes ----
    a.rep('| explicit row-A C = DYAD-THM-LPHASE-ROWA-REMAINDER (NUMGEN OPEN [target THM], import deferred; L5 NUMGEN.N-A) | ≡ *DYAD:six-step-cubic-jet | @NUMGEN§6.6',
          '| explicit row-A C = DYAD-THM-LPHASE-ROWA-REMAINDER, imported by NUMGEN v1.21 at §6.6 as a distinct [THM] block (pin dyad-v6.4.22 §6.14, producer v6.4.19; base points in U_D,base, branch on U_D,tube; the explicit-constant OPEN sub-item closed by the import; L5 NUMGEN.N-A) | ≡ *DYAD:six-step-cubic-jet | @NUMGEN§6.6', 'NUMGEN NA-02', 'L-PHASE node')
    a.rep('orbit sampling (below DYAD angular sup 1.42849, no conflict); lives only in NUMGEN Changelog v1.10 (L5 NUMGEN.N-T3) | @NUMGEN changelog',
          'orbit sampling (below DYAD angular sup 1.42849 and the imported ceiling 403/250, no conflict); live at v1.21 §6.6 as [NUM] with evidence pointers (seed-family sampling on U_NG; not a proof input) | @NUMGEN§6.6', 'NUMGEN NB-11', 'LPHASE-exponent-NUM node')
    a.sub_in_line('NUMGEN-RESULT-N5AS1-INF1 RES[ALG] |', '(not an extension of NUMGEN INF-1; NUMGEN.N-B) | ¬ explicit radius |',
                  '(not an extension of NUMGEN INF-1; recorded by NUMGEN v1.21 §9.1 as independent agreement, not imported; NUMGEN.N-B) | ¬ explicit radius |', 'NUMGEN NA-01', 'INF1 node')
    a.sub_in_line('*NUMGEN:INF-2 RES[ALG] |', '*NUMGEN:INF-2 RES[ALG] |', 'NUMGEN-RESULT-N5AS1-INF2 RES[ALG] |', 'NUMGEN NB-07', 'INF-2 node RID')
    a.sub_in_line('*NUMGEN:GAPLOCK-1 RES[ALG] |', '*NUMGEN:GAPLOCK-1 RES[ALG] |', 'NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET RES[ALG] |', 'NUMGEN NB-07', 'GAPLOCK-1 node RID')
    a.sub_in_line('*NUMGEN:GAPLOCK-2 RES[ALG] |', '*NUMGEN:GAPLOCK-2 RES[ALG] |', 'NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT RES[ALG] |', 'NUMGEN NB-07', 'GAPLOCK-2 node RID')
    a.sub_in_line('*NUMGEN:GAPLOCK-3 RES[ALG] |', '*NUMGEN:GAPLOCK-3 RES[ALG] |', 'NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO RES[ALG] |', 'NUMGEN NB-07', 'GAPLOCK-3 node RID')
    a.sub_in_line('*NUMGEN:first-nonlinear-average RES[ALG] |', '*NUMGEN:first-nonlinear-average RES[ALG] |', 'NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE RES[ALG] |', 'NUMGEN NB-07', 'cyclic-average node RID')
    a.sub_in_line('DYAD-ALG-CUBIC-PARABOLIC ALG |', '≡ NUMGEN first-nonlinear-average consequence', '≡ NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE consequence', 'NUMGEN NB-07', 'CUBIC-PARABOLIC node alias')
    a.sub_in_line('NUMGEN-OPEN-NG0R-COV OPEN→ALG/NUM |', '| ~ replacement candidate RECOG-THM-A1A-CD-IDENTIFICATION (L5 NUMGEN.N-L4) | @NUMGEN§6.1a',
                  '| ~ replacement candidate RECOG-THM-A1A-CD-IDENTIFICATION; v1.21 pins the comparison conventions (chart, lift, readout, clock, start state, overlap U_R,base ∩ U_NG) and keeps φ* ≟ C_D^ext OPEN (L5 NUMGEN.N-L4) | @NUMGEN§6.1a', 'NUMGEN NC-14', 'NG0R-COV node')
    a.rep('GAP-LOCK Lemma 3 (no RID) → RECOG; relay identities (Q-INVARIANT-FORM, TAU-DETB, CUBIC-PARABOLIC) → DYAD (NG_TO_DYAD_RELAY_RIEMANN_LENS_v1, registered DYAD v6.4.11 as definition-ledger identities).',
          'GAP-LOCK Lemma 3 (NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO since v1.21) → RECOG; relay identities → DYAD (NG_TO_DYAD_RELAY_RIEMANN_LENS_v1; registered DYAD v6.4.11 as DYAD-ALG-Q-INVARIANT-FORM, -TAU-DETB, -CUBIC-PARABOLIC, cited by RID in NUMGEN v1.21 §9.2).', 'NUMGEN NC-13', 'D2 exports line')
    a.sub_in_line('DYAD-THM-LPHASE-ROWA-REMAINDER THM |', '>NUMGEN L-PHASE (offered; NUMGEN v1.20.8 records receipt, interface I1–I5 confirmed, import deferred: NUMGEN OPEN sub-item)',
                  '>NUMGEN L-PHASE (imported by NUMGEN v1.21 §6.6 at pin dyad-v6.4.22, producer v6.4.19; interface I1–I5 confirmed at receipt; states received / statement accepted / adopted use recorded in NUMGEN §9.1)', 'NUMGEN NA-02', 'DYAD row-A node consumer edge')
    a.rep('· NUMGEN L-PHASE explicit constant (OPEN [target THM]): row A available upstream (DYAD-THM-LPHASE-ROWA-REMAINDER), not imported by NUMGEN v1.20.8; explicit-tube INF-1 also needs an explicit L-BACKBONE, which NUMGEN does not state (available via RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, L5 NUMGEN.N-B);',
          '· NUMGEN L-PHASE explicit constant: row A imported by NUMGEN v1.21 (DYAD-THM-LPHASE-ROWA-REMAINDER at §6.6; the OPEN sub-item closed); an explicit-tube INF-1 of NUMGEN\'s own would also need an explicit L-BACKBONE, which NUMGEN does not state and does not import (RECOG-THM-A1A-RECIPROCAL-AMPLITUDE recorded as independent agreement, L5 NUMGEN.N-B);', 'NUMGEN NA-02', 'D2.L3 phase constants')
    a.rep('NG objects (current counterpart NUMGEN v1.20.8; valid v1.15 producer pins retained where stated; GAP-LOCK v2)', 'NG objects (RECOG pins NUMGEN v1.20.8; governing counterpart v1.21, whose GAP-LOCK/INF-2 RIDs RECOG may cite at its next edition; valid v1.15 producer pins retained where stated; GAP-LOCK v2)', 'NUMGEN move', 'D3 imports line')
    a.rep('**domains** (⊥ D2.L5 NUMGEN.N-S1)', '**domains** (labels per NUMGEN v1.21 §6.2: U_NG, U_NG,tube, U_D,base, U_D,tube, U_R,base; no inclusion asserted between U_NG and U_D,base)', 'NUMGEN NA-03', 'D2.L1 domains heading')
    a.rep('| >NUMGEN relay (L5 NUMGEN.N-L3) | @DYAD§6.3', '| >NUMGEN relay (cited by RID in NUMGEN v1.21 §9.2) | @DYAD§6.3', 'NUMGEN NC-13', 'Q-INVARIANT-FORM node')
    a.rep('| ~ explicit counterpart of NUMGEN L-MONO requires consumer scope comparison (NUMGEN.N-L5) | cert RECOG-ART-A1A-C1-CHECK |', '| ~ explicit counterpart of NUMGEN L-MONO; NUMGEN v1.21 §9.1 records it as independent agreement on U_D,tube vs U_NG,tube (comparison only, no inclusion) | cert RECOG-ART-A1A-C1-CHECK |', 'NUMGEN NA-01', 'LIFT-ALIGNMENT node')
    # ---- D2.L5 ----
    a.drop_line('NUMGEN.N-S1 ⊥ D-SYM |', 'NUMGEN NA-03', 'NUMGEN.N-S1 retired')
    a.line('NUMGEN.N-A + DYAD.X10 D-LINK |',
           'NUMGEN.N-A + DYAD.X10 ~ D-LINK | L-PHASE ↔ DYAD row A: NUMGEN v1.21 imports DYAD-THM-LPHASE-ROWA-REMAINDER at §6.6 as a distinct [THM] block (pin dyad-v6.4.22 §6.14, producer v6.4.19; typed interface I1–I5: W ≡ 𝓛, lift ≡ PRIMITIVE-LIFT, q_m ≡ Q_m, lag sign, base points in U_D,base) and keeps NUMGEN-RESULT-N5AS1-L-PHASE existential on U_NG; 403/250 appears only in the import block and the matrix row. Scope gap stated by both owners: (R) needs x∈U_D,base, so U_D,tube∖U_D,base is covered only once the orbit enters the base. atlas-checked: 403/250=1.612≥1.61112.', 'NUMGEN NA-02', 'NUMGEN.N-A reworded')
    a.line('NUMGEN.N-D D-LINK |',
           'NUMGEN.N-D D-LINK | NUMGEN\'s φ* comparison stays open by owner decision: v1.21 enters RECOG-THM-A1A-CD-IDENTIFICATION / -PHASE-EXISTENCE-U as available comparisons under NUMGEN-OPEN-NG0R-COV with the conventions pinned (chart, lift, readout, clock, start state, overlap U_R,base ∩ U_NG) and asserts no identity φ* ≡ C_D^ext; A1c recovers neither a nor an R_ind downgrade. DYAD-CAND-PHISTAR-ENTRY-PHASE is not an owner RID.', 'NUMGEN NC-14', 'NUMGEN.N-D reworded')
    a.line('NUMGEN.N-B D-LINK |',
           'NUMGEN.N-B D-LINK | explicit-domain counterparts recorded by the producer: NUMGEN v1.21 §9.1 acceptance matrix (8 rows; columns event predicate/anchor, lift, base/tube, clock, estimate scope, grade, relationship, receiving status) types RECOG-THM-A1A-RECIPROCAL-AMPLITUDE\'s 15/2 as the per-block increment (type 1), the series tails as type 2 and the slip-schedule ε_k as type 3, and records each RECOG theorem as independent agreement, not imported (custody of GAP-LOCK 1–3 and INF-1 unchanged, as RECOG states). NUMGEN\'s statements keep their existential domain; no inclusion U_NG vs U_D,base is asserted.', 'NUMGEN NA-01', 'NUMGEN.N-B reworded')
    a.line('NUMGEN.N-E ~ D-LINK |',
           'NUMGEN.N-E ~ D-LINK | GAP-LOCK upstream coverage, per statement in NUMGEN v1.21 §9.1: DYAD (B) explicit L-MONO on U_D,tube; DYAD (R) explicit L-PHASE at base points in U_D,base (imported); RECOG LIFT-ALIGNMENT π/6<δ_T<π/2 on U_D,tube; RECOG RECIPROCAL-AMPLITUDE on U_R,base; RECOG (B),(C′) deficit 0.927τQ<Δ<τQ+1.82Q^{3/2} on U_D,tube — all independent agreement, none consumed. Atlas reading (not adopted by either owner): on U_D,base τQ−(403/250)Q^{3/2}>0 ⇒ Λ_6<2π and Λ_7>2π explicitly ⇒ Lemma 1 explicit for B-event points in U_D,base; U_D,tube∖U_D,base not covered.', 'NUMGEN NA-01', 'NUMGEN.N-E reworded')
    a.line('NUMGEN.N-L6 ~ D-LINK (→ GEN D3) |',
           'NUMGEN.N-L6 ~ D-LINK (→ GEN D3) | NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE (RID since v1.21; stated for f=R+h_d, applied to the primitive dyad) with vector charge a−b−1 mod 6 gives six-step quadratic vanishing for L=diag(A,A,A): degree-2 vector monomial charges ∈{1,−1,−3}≢0 mod 6 ⇒ G₂=0 = GEN chrono-protection whose proof source GEN-ART-G2-CHRONO is custody (a) missing; RECOG R-L2 gives the same route via leading-return equivariance; the diag(A,A,A) application is atlas-derived (charge rule per output component), offered to Genesis as an independent route in ' + PIPE_GEN + ' (receiver undecided).', 'NUMGEN NC-15', 'NUMGEN.N-L6 reworded')
    a.line('NUMGEN.N-L1 ~ D-LINK |',
           'NUMGEN.N-L1 ~ D-LINK | L1 is the existential form of PRIM-CTR; ΔQ₅≡P₅ exactly — NUMGEN v1.21 names DYAD-ALG-P5-RADIAL as the Dyadic owner name at L1 (exact sympy gate A1, evidence/numgen/scripts/numgen_v1_21_stage1_checks.py); DYAD ceiling 1.6931 tighter than C5=2.14998; true sup|A|=1.63878; explicit ε_L1 (Q≤1/400) still not stated on the NUMGEN side.', 'NUMGEN NC-13', 'NUMGEN.N-L1 reworded')
    a.drop_line('NUMGEN.N-L3 D-LINK |', 'NUMGEN NC-13', 'NUMGEN.N-L3 retired')
    a.line('NUMGEN.N-L4 ~ D-LINK |',
           'NUMGEN.N-L4 ~ D-LINK | φ* replacement candidate: RECOG-THM-A1A-CD-IDENTIFICATION C_D^ext(x₀)=τ log Q₀−M_W(x₀) on U, M_W=O(√Q₀) (DYAD OPEN3-PHASE-OFFSET-BOUNDS/OPEN21) ⇒ Q₀→λQ₀ at fixed Θ₀ shifts C_D by τ ln λ+O(√Q₀) = NG-0R-COV target; NUMGEN v1.21 pins the comparison conventions and still requires its own comparison proof; atlas reading of C_D as gauge-reduced entry datum unverified.', 'NUMGEN NC-14', 'NUMGEN.N-L4 reworded')
    a.drop_line('NUMGEN.N-L5 D-LINK |', 'NUMGEN NA-01', 'NUMGEN.N-L5 retired')
    a.drop_line('NUMGEN.N-L7 D-LINK |', 'NUMGEN NC-12', 'NUMGEN.N-L7 retired')
    a.line('NUMGEN.N-SC1 D-SCOPE |',
           'NUMGEN.N-SC1 ~ D-SCOPE | explicit upstream versions exist for N-1, N-2-ORD, N-3A, NG-8A/B, gates 1/3/4 (DYAD explicit U_D,tube: PRIM-CTR Q≤1/400⊃U_D,tube, P3 box ⊃U_D,tube, |η|<0.0665<π/2 one-chart) and for L-BACKBONE, L-MONO, INF-1, GAP-LOCK (RECOG, §9.1 matrix); NUMGEN v1.21 keeps every statement on U_NG by owner decision and adds explicit-domain pointers at the points of use (comparison only, no inclusion). Not a staleness; an owner-declared scope.', 'NUMGEN NA-01', 'NUMGEN.N-SC1 reworded')
    a.line('NUMGEN.N-R1 D-RID |',
           'NUMGEN.N-R1 D-RID | registered in v1.21: NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET, -GAPLOCK-COUNT, -GAPLOCK-SLIP-RATIO, NUMGEN-RESULT-N5AS1-INF2, NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE (RECOG can cite GAP-LOCK 3 by RID). Still no RID (owner tier 2, next edition): N-3C+ projector/support/reachable-charge/OPEN-9 boundary/Bessel; gates 1/3/4, section identity; N5-C1–C6, N5-PHYS-1, C7A, C7B-T1..T4, DISC-1/2, ten-label bound, C7C-0, M-1A, M-1B, M2-1, C7C-M FAILs, Census-1 (module RIDs only); P3 injectivity; ORD-1..4, T4; explicit-domain corollaries; q* witness; NG-7A abelian extension.', 'NUMGEN NB-07', 'NUMGEN.N-R1 reworded')
    a.line('NUMGEN.N-R2 D-RID |',
           'NUMGEN.N-R2 D-RID | RID type ≠ status: CLOSED results under OPEN RIDs (N1, N2, N2-ORDER, N1A2, N5A, N5AS1-SECTION, N5AS1-INF, REC-HOL-OPERATOR, TWO-FIVES-ORBIT-CARDINAL, TWO-FIVES-REBLOCK); v1.21 §6.6 guard: the module record points to its result RIDs and the category word is not a grade (DEFECT-THRESHOLD-RATIO graded RES[ALG] as tagged). Residual: N1A2 heads an ALG closure; N1C-DYAD-RADIAL and OPEN-N1C both head the N-1C closure (owner tier 2).', 'NUMGEN NB-08', 'NUMGEN.N-R2 reworded')
    a.line('NUMGEN.N-F D-STALE |',
           'NUMGEN.N-F D-STALE (low residue) | v1.21 fixes §7 N-3 item 7 (Q403 at v6.4.18), the Programme v1.3 and Genesis v2.9 pins, the DZT provenance and the §9.1 header; remaining dated wording is in historical COR/guard notes (Dyadic v6.4.10 provenance at the coefficient-conflation guard; §6.1a pre-registration pin "v6.4.15") and in ten `[v1.20.x]` markers of untouched rows, all declared in the release record §6.', 'NUMGEN NA-04', 'NUMGEN.N-F reworded')
    a.line('NUMGEN.N-C1 D-CONV |', 'NUMGEN.N-C1 D-CONV | q_m (NUMGEN) ≡ Q_m (DYAD) with q also |z|² in DYAD/RECOG; owner-stated in NUMGEN v1.21 §6.2 ("q_m is the primitive Q_true at block base points, not the chart variable q=|z|²").', 'NUMGEN NC-18', 'NUMGEN.N-C1 reworded')
    a.line('NUMGEN.N-D1 D-PROOF (b) |', 'NUMGEN.N-D1 D-PROOF (b, declared) | in-ledger proofs without separate certificate: N5-C1–C4, C5, N5-PHYS-1, C7A, P3 injectivity, NG-7A abelian, explicit-domain corollaries, N-1A2 — NUMGEN v1.21 §9.2 declares the evidence state at each ("written proof in ledger; no separate certificate", v1.4 §12 keys) and the availability of the held records on upload/numgen-records.', 'NUMGEN NB-09', 'NUMGEN.N-D1 reworded')
    a.drop_line('NUMGEN.N-G1 D-GRADE/D-STALE |', 'NUMGEN NC-16', 'NUMGEN.N-G1 retired')
    a.line('NUMGEN.N-T1 D-STALE |', 'NUMGEN.N-T1 D-STALE (declared exception) | §6.6 keeps the superseded LOGSLIP block (NUMGEN-CAND-N5AS1-LOGSLIP, [COR] historical) in place by owner decision (release record §6: moving it would move claim blocks; a reviewed later edit); that RID carries no `[RID:]` declaration in the live text — its registration line sits in the changelog at tag numgen-v1.20.8 (checker: link UNVERIFIED, documented here); §9.2 NG_C7C_M_DESIGN_v1 statements ("typed by B suffices", "associativity free") historical; N-5A-S1 header "[COR: v1.7 verdict]" (flagged history in source; excluded).', 'NUMGEN NA-06', 'NUMGEN.N-T1 reworded')
    a.drop_line('NUMGEN.N-T2 D-STALE/D-SCOPE |', 'NUMGEN NA-05', 'NUMGEN.N-T2 retired')
    a.drop_line('NUMGEN.N-T3 D-STALE |', 'NUMGEN NB-11', 'NUMGEN.N-T3 retired')
    a.line('NUMGEN.N-Q* ~ D-LINK |', 'NUMGEN.N-Q* ~ D-LINK | DYAD-THM-OPEN18 "q=q_* branch split" and NUMGEN q*≈0.3156258836 on the same canonical family (0,q): plausibly the same q*; NUMGEN\'s q* is a [NUM] root candidate of η₆(q)−q=0 (same wrapped phase after one block), not stated as a branch split; question filed as ' + PIPE_DYAD + ' (receiver undecided); NUMGEN defers the cross-citation (v1.21 NC-17).', 'NUMGEN NC-17', 'NUMGEN.N-Q* reworded')
    a.after_line('NUMGEN.N-Q* ~ D-LINK |', ['NUMGEN.N-I1 D-LINK (receiver side) | five v1.21 `kind: notice` items filed by NUMGEN after the tag (pipes/RECOG, pipes/DYAD, pipes/TDRG, pipes/GEN, pipes/OFN; each `state: open`): acceptance matrix and GAP-LOCK/INF-2 RIDs (RECOG), row-A import and DYAD-ALG-P5-RADIAL alias (Dyadic), C7C-M4 HOLD (TDR-G), Genesis v2.9 pin and the cyclic-average RID (Genesis), §6.8 OFN v0.10 pointer (OFN). A filed item is not adopted use; each receiver decides at its own checkpoint (CONVENTIONS §7).'], 'NUMGEN notices', 'NUMGEN.N-I1 new')
    # ---- D5 ----
    a.rep('PROG §6.4 lists "antipodal path tie" as an owner-review task; NUMGEN blocks C7C M-4 on it. Fix (TDR-G, scientific): rule on endpoint antipode (affects any policy using path orientation).',
          'PROG §6.4 lists "antipodal path tie" as an owner-review task; NUMGEN v1.21 §2 item 1 holds C7C M-4 on it (HOLD, with a sensitivity audit of affected witnesses before any status change) and the request is filed as ' + PIPE_TDRG + ' (blocks C7C-M4; receiver undecided). The 216 antipodal events lie inside the audited eventual cycles; every admitted label keeps at least one unexposed witness, so the ten-label lower bound is unaffected (NUMGEN §6.6). Fix (TDR-G, scientific): rule on endpoint antipode (affects any policy using path orientation).', 'NUMGEN I06', 'D5.X1')
    a.line('NUMGEN.N-R1 (DISC part) D-RID:', 'NUMGEN.N-R1 (DISC part) D-RID: DISC-1/DISC-2 results, ten-label bound, C7B-ALG-T1..T4, Census-1 sit under module RIDs NUMGEN-OPEN-N5 / -N5-COMM-BD only (owner tier 2 after v1.21).', 'NUMGEN NB-07', 'D5 NUMGEN.N-R1')

KEY = re.compile(r'(?<![A-Za-z0-9_.-])((?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?|NUMGEN\.N-Q\*|NUMGEN\.N-[A-Z]+\d*)|F\d+)(?![A-Za-z0-9_-])')
ROW = re.compile(r'^((?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?|NUMGEN\.N-Q\*|NUMGEN\.N-[A-Z]+\d*)|F\d+)(?: \+ ((?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?)))?(?![A-Za-z0-9_-])')

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

def stale_editions(text):
    # consumer pins on v1.20.8 (RECOG §6.13b, Programme IF14) are owner text and stay; only atlas-side staleness phrases are refused
    return [l[:80] for l in text.split('\n') if re.search(r'`numgen-v1\.20\.8`|\| v1\.20\.8 \| `numgen|import deferred|GAP-LOCK lemmas unnumbered|U/U_T denote both|not imported by NUMGEN v1\.20\.8|current counterpart NUMGEN v1\.20\.8|NUMGEN v1\.20\.8 records receipt', l)]

def checker():
    spec = importlib.util.spec_from_file_location('atlas_checker', ROOT / 'tools/atlas_check.py')
    c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c); return c

def main():
    global SNAPSHOT
    SNAPSHOT = git('rev-parse', SNAPSHOT + '^{commit}').decode().strip()
    base = at('atlas-v0.5', ATLAS).decode(); assert sha(base) == BASE_SHA
    a = Edit(base); refresh(a); text = a.text
    assert not stale_editions(text), stale_editions(text)
    # ---- manifest ----
    old = json.loads(at('atlas-v0.5', 'evidence/atlas/v0.5/source_manifest.json'))
    m = json.loads(json.dumps(old))
    m.update(atlas='v0.6', frozen_at='2026-10-26', repository_snapshot=SNAPSHOT, previous_atlas_tag='atlas-v0.5', method_tag='atlas-v0.2', method_edition='v0.2')
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_5_edition'] = prev['edition']; s['v0_5_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] in MOVED:
            mv = MOVED[s['key']]; data = at(mv['tag'], s['path'])
            s.update(edition=mv['edition'], tag=mv['tag'], commit=git('rev-parse', mv['tag'] + '^{commit}').decode().strip(), sha256=sha(data), authority=mv['authority'])
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(SNAPSHOT, s['path']), ('snapshot/tag divergence', s['key'])
        s['v0_5_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_5_input_equality'] for x in m['sources']) == {'EQUAL': 17, 'CHANGED': 1}
    assert next(s for s in m['sources'] if s['key'] == 'NUMGEN')['sha256'] == '4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701'
    wjson(OUT / 'source_manifest.json', m)
    # ---- H -> L5 ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys ----
    oldret = json.loads(at('atlas-v0.5', 'evidence/atlas/v0.5/retired_l5_keys.json'))
    newret = {'NUMGEN.N-S1': 'NUMGEN v1.21 §6.2 [DEF] domain labels U_NG, U_NG,tube, U_D,base, U_D,tube, U_R,base; unlabelled U/U_T means U_NG; L1 coordinate U named as a coordinate (NA-03/I08).',
              'NUMGEN.N-L3': 'NUMGEN v1.21 §9.2 relay row cites DYAD-ALG-Q-INVARIANT-FORM, -TAU-DETB, -CUBIC-PARABOLIC by RID (NC-13).',
              'NUMGEN.N-L5': 'NUMGEN v1.21 §9.1 acceptance matrix lists every RECOG explicit-domain theorem as an available comparison, recorded as independent agreement (NA-01).',
              'NUMGEN.N-L7': 'NUMGEN v1.21 SG-NG-23 cross-reading names RECOG (S) and the scope difference for e^{π/(3τ)} (NC-12).',
              'NUMGEN.N-G1': 'NUMGEN v1.21 §9.2 RECOG row (v0.3.24) names the §7 HEUR cross-reference tag, the ALG use in RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE and the A1b route; no grade asserted (NC-16). The atlas row itself overstated: RECOG §7 does tag HEUR.',
              'NUMGEN.N-T2': 'NUMGEN v1.21: scope words at the N-1 tree and the N-1A0/N-1A1 status lines ("closed on U_NG by L1; abstract question open") (NA-05).',
              'NUMGEN.N-T3': 'NUMGEN v1.21: the sampled L-PHASE range is live at §6.6 as [NUM] with evidence pointers; the other changelog-only facts are at tag numgen-v1.20.8 (NB-11).'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.6 reasons in dispositions.json.'))
    # ---- shared checker ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at('atlas-v0.2', 'evidence/atlas/coverage_map_v0_2.json'))
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.6/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    # ---- new-node RID presence in the moved source (naming check, not certificate replay) ----
    presence = {r: (('RID: ' + r) in src['NUMGEN']) for r in NEW_RIDS}; assert all(presence.values()), presence
    assert 'DYAD-THM-LPHASE-ROWA-REMAINDER]' in src['NUMGEN'] and 'DYAD-ALG-P5-RADIAL' in src['NUMGEN']
    for p in (PIPE_TDRG, PIPE_DYAD, PIPE_GEN): assert (ROOT / p).exists() and at(SNAPSHOT, p), p
    # ---- dispositions ----
    def row(t, key): return next((l for l in t.split('\n') if l.startswith(key + ' ')), None)
    touched = ['NUMGEN.N-S1', 'NUMGEN.N-A', 'NUMGEN.N-D', 'NUMGEN.N-B', 'NUMGEN.N-E', 'NUMGEN.N-L6', 'NUMGEN.N-L1', 'NUMGEN.N-L3', 'NUMGEN.N-L4', 'NUMGEN.N-L5',
               'NUMGEN.N-L7', 'NUMGEN.N-SC1', 'NUMGEN.N-R1', 'NUMGEN.N-R2', 'NUMGEN.N-F', 'NUMGEN.N-C1', 'NUMGEN.N-D1', 'NUMGEN.N-G1', 'NUMGEN.N-T1', 'NUMGEN.N-T2', 'NUMGEN.N-T3', 'NUMGEN.N-Q*', 'D5.X1']
    disp = []
    for key in touched:
        o, n = row(base, key), row(text, key)
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded')
        disp.append(dict(key=key, disposition=state, reason=newret.get(key, 'reworded; see edit_log.json'), previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    disp.append(dict(key='NUMGEN.N-I1', disposition='new', reason='five v1.21 notices await receiver dispositions (pipes)', previous_sha256=None, current_sha256=sha(row(text, 'NUMGEN.N-I1'))))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    t = text.replace('not an L-BACKBONE constant — NUMGEN.N-B)', 'not an L-BACKBONE constant — NUMGEN.N-L5)', 1); ctl('U1', 'H cites a retired L5 row', 'H5:NUMGEN.N-L5' in h_l5_map(t)['dangling'])
    t = text + 'NUMGEN.N-G1 D-GRADE: reused\n'; ctl('U2', 'retired key reused', bool(c.run(t, m, src, cmap, idmap, retired, with_sources=False).fails()))
    t = text.replace('| v1.21 | `numgen-v1.21` |', '| v1.20.8 | `numgen-v1.20.8` |', 1); ctl('U3', 'SOURCES row older than manifest', bool(c.run(t, m, src, cmap, idmap, retired).fails()) or bool(stale_editions(t)))
    t = text.replace('NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT RES[ALG] |', 'NUMGEN-RESULT-N5AS1-GAPLOCK-COUNTS RES[ALG] |', 1); ctl('U4', 'new node RID misspelled against the source', bool(c.run(t, m, src, cmap, idmap, retired, with_sources=False).fails()) or ('RID: NUMGEN-RESULT-N5AS1-GAPLOCK-COUNTS' not in src['NUMGEN']))
    t = text.replace('imported by NUMGEN v1.21 at §6.6 as a distinct [THM] block', 'NUMGEN OPEN [target THM], import deferred', 1); ctl('U5', 'stale "import deferred" wording reintroduced', bool(stale_editions(t)))
    t = text.replace(PIPE_TDRG, 'pipes/TDRG/20261026-NUMGEN-orientation-policy.md'); ctl('U6', 'pipe path cited that does not exist in the snapshot', not all((ROOT / p).exists() for p in re.findall(r'pipes/[A-Z]+/\d{8}-[A-Z]+-[a-z0-9-]+\.md', t)))
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), controls
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas='atlas-v0.5', base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()), atlas_lines=text.count('\n') + 1,
                   source_snapshot=SNAPSHOT, changed_sources=list(MOVED), edit_operations=len(a.log), retired_keys=list(newret), new_keys=['NUMGEN.N-I1'],
                   new_node_rids=NEW_RIDS, dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_controls=len(shared), focused_controls=len(controls),
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_6.py': sha(Path(__file__).read_bytes())},
                   limitations=['Structural checks only; no owner certificate rerun; new RIDs checked for presence in the tagged source, not re-proved.',
                                'Impact refresh of one moved source (NUMGEN v1.21); the other 17 domains were not re-extracted; pipe items are cited as filed, their receiver dispositions are not atlas sources.',
                                'NUMGEN v1.21 §6.2/§6.6/§9.1/§9.2 extracted at statement level from the tagged file; proofs live in the owner cells.'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
