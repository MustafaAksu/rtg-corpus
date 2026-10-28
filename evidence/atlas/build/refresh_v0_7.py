#!/usr/bin/env python3
"""Atlas v0.6 -> v0.7 candidate: impact refresh for two moved sources — Discrete Genesis v2.12.14 (`tdrg-v2.12.14`,
adopted 28 Oct 2026, corrections only, Methodology v1.2 declared) and RECOG v0.3.25 (`recog-v0.3.25`, adopted 27 Oct 2026).

TDRG (D5, H4, H9, D1 METH.M2/OFN.O5/OFN.O7, D2 N-I1): source row and D5 header; node heads renamed from atlas labels to the
owner RIDs registered in v2.12.14 (TDRG-DEF-*, TDRG-THM-*, TDRG-ALG-LEM-*, TDRG-ALG/NUM-BIND3-*), old labels kept as aliases;
TDRG-DEF-ORIENT rewritten (option (b): balanced tie on S=0 ∧ 2E≡0; superseded node-ID completion; G-rule recorded, not
adopted); new nodes TDRG-ALG-ORIENT-NOGO, TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE, TDRG-NUM-ORIENT-EQUIVARIANCE-N24,
TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK, TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY; SG-14 in D5.L4; LEM-RETRIG/SPECCONS wording;
N-scaling grades (NUM/HEUR, χ=0.836 check withdrawn); BIND3 results marked [conv: v18 path orientation] EV-NOT-RERUN with the
three-node census bound; NUMGEN DISC/P2 nodes point to the ruling. Retired: TDRG.G1, G2, G3, G4, G5, G6, G7 (reasons in
dispositions.json); reworded: TDRG.G8, D5.X1, AZ.A7, OFN.O5, OFN.O7, METH.M2, NUMGEN.N-I1; new: TDRG.G10 (largest_center
ID tie-break, N1), TDRG.G11 (evidence custody).
RECOG (D3, H5): source row and D3 header; R9-MEMORY node gains the v0.3.25 sharpened rows (RECOG-ALG-R9-SUM-LEMMA,
RECOG-THM-R9-SHARPENED-ROWS, -C7 [assuming Dyadic C7 ceilings]); A1b node gains RECOG-THM-A1C-SHARPENED-SCHEDULE [assuming
(D5)]; A1c readout node gains the record-only outer enclosure (RECOG-ALG-A1C-ADMISSIBLE-REGION, -START-OFFSET,
-JOINT-CONTRACTOR; windows, not identification) and the record-fiber result (RECOG-ALG-A1C-THRESHOLD-CODING,
-PHASE-C1-FIBER; A1c-Q1′ stays OPEN); R6 sub-items updated; R-D1 names the four new artifacts; new row RECOG.R-A1
((D5) constants and C7 ceilings as [assuming:] until Dyadic registers them).
Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_7.py
"""
from __future__ import annotations
import hashlib, importlib.util, json, re, subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.7'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = '53b56e4'   # origin/main after PR #99 (TDR-G v2.12.14 post-tag closeout); resolved in main()
BASE_SHA = '35ebee6d61f4db93211f2ed6f2de2bb973aa2fc6f2ea3cdf670656b1e961bd8a'   # atlas-v0.6
MOVED = {'TDRG': dict(edition='v2.12.14', tag='tdrg-v2.12.14', authority='OWNER: records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md at tdrg-v2.12.14 (+ TDRG_v2_12_14_POST_TAG_ADDENDUM_20261028.md)'),
         'RECOG': dict(edition='v0.3.25', tag='recog-v0.3.25', authority='OWNER: records/recog/RECOG_v0_3_25_RELEASE_RECORD.md at recog-v0.3.25')}
TDRG_SHA = '3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392'
RECOG_SHA = '86cae8ff094d63d077ec5c0887451775ec3a26485cfad95833d8390bda4bd7db'
NEW_RIDS_TDRG = ['TDRG-DEF-ZN-STATE', 'TDRG-DEF-BAND', 'TDRG-DEF-CONV-TICK', 'TDRG-DEF-SWAP', 'TDRG-DEF-CONV-P3CYC', 'TDRG-DEF-ORIENT', 'TDRG-DEF-CYCLE-BOUND',
                 'TDRG-DEF-STAR', 'TDRG-DEF-MULTISTAR', 'TDRG-THM-HOLONOMY', 'TDRG-THM-NARROW-BAND-EXCLUSION', 'TDRG-THM-RECURRENCE', 'TDRG-THM-REACHABILITY-K0',
                 'TDRG-ALG-LEM-REACH', 'TDRG-ALG-LEM-NOANNIHIL', 'TDRG-ALG-LEM-RETRIG', 'TDRG-ALG-LEM-SPECCONS', 'TDRG-ALG-BIND3-CYCLE-N24K1', 'TDRG-NUM-BIND3-PARITY',
                 'TDRG-NUM-BIND3-SPECTRAL-GATE', 'TDRG-NUM-BIND3-MEMORY-PARITY', 'TDRG-NUM-BIND3-XFER', 'TDRG-NUM-BIND3-REGEN', 'TDRG-ALG-ORIENT-NOGO',
                 'TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE', 'TDRG-NUM-ORIENT-EQUIVARIANCE-N24', 'TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK', 'TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY',
                 'TDRG-DEF-SIGNED-CENTERED', 'TDRG-DEF-SIGNED-DEFECT-ERROR']
NEW_RIDS_RECOG = ['RECOG-ALG-R9-SUM-LEMMA', 'RECOG-THM-R9-SHARPENED-ROWS', 'RECOG-THM-R9-SHARPENED-ROWS-C7', 'RECOG-THM-A1C-SHARPENED-SCHEDULE', 'RECOG-ALG-A1C-COMBINED-TAIL',
                  'RECOG-ALG-A1C-ADMISSIBLE-REGION', 'RECOG-ALG-A1C-START-OFFSET', 'RECOG-ALG-A1C-JOINT-CONTRACTOR', 'RECOG-ALG-A1C-THRESHOLD-CODING', 'RECOG-ALG-A1C-PHASE-C1-FIBER',
                  'RECOG-ART-R9-SHARPENED-ROWS', 'RECOG-ART-A1C-SHARPENED-SCHEDULE', 'RECOG-ART-A1C-DECODER', 'RECOG-ART-A1C-Q1PRIME-FIBER']
PIPE_NOTICE = '20261028-TDRG-v2-12-14-adopted.md'

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
        self.log.append(dict(id=f'AR07-{len(self.log)+1:03d}', finding=finding, where=where, old_sha256=sha(old), new_sha256=sha(new), old=old, new=new))
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
    # ---- identity ----
    a.rep('# RTG STATE ATLAS v0.6\n', '# RTG STATE ATLAS v0.7\n', 'identity', 'title')
    a.rep('full identities in evidence/atlas/v0.6/source_manifest.json', 'full identities in evidence/atlas/v0.7/source_manifest.json', 'identity', 'SOURCES header')
    a.rep('| RECOG | RTG_RELATIONAL_RECOGNITION_DSN | v0.3.24 | `recog-v0.3.24` | canonical Tier 3 |', '| RECOG | RTG_RELATIONAL_RECOGNITION_DSN | v0.3.25 | `recog-v0.3.25` | canonical Tier 3 |', 'RECOG move', 'SOURCES RECOG row')
    a.rep('| TDRG | RTG_DISCRETE_GENESIS_DSN | v2.12.13 | `tdrg-v2.12.13` |', '| TDRG | RTG_DISCRETE_GENESIS_DSN | v2.12.14 | `tdrg-v2.12.14` |', 'TDRG move', 'SOURCES TDRG row')
    a.rep('*END — RTG STATE ATLAS v0.6. Noncanonical; owner DSNs govern.*', '*END — RTG STATE ATLAS v0.7. Noncanonical; owner DSNs govern.*', 'identity', 'footer')
    a.rep('(owner RECOG = RTG_RELATIONAL_RECOGNITION_DSN v0.3.24;', '(owner RECOG = RTG_RELATIONAL_RECOGNITION_DSN v0.3.25;', 'RECOG move', 'D3 header')
    a.rep('(sources: TDRG = RTG_DISCRETE_GENESIS_DSN v2.12.13 (June 2026, Tier 4, maturity record B); AZ = RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN v0.6 (June 2026, Tier 5, Level A retained); NUMGEN v1.20.8 DISC/C7B modules.',
          '(sources: TDRG = RTG_DISCRETE_GENESIS_DSN v2.12.14 (October 2026 corrections edition of the June 2026 v2.12 line; Methodology v1.2 declared by PI decision, the v1.4 migration is v2.13; Tier 4, maturity record B); AZ = RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN v0.6 (June 2026, Tier 5, Level A retained); NUMGEN v1.21 DISC/C7B modules.', 'TDRG move', 'D5 header')
    a.rep('Local aliases: TDRG [ALG/NUM] = ALG co-certified by NUM, [ENG/ALG], legacy [NUM-strong]/[HEUR-strong]; AZ [ENG PASS]',
          'Local aliases: TDRG compound tags unpacked in v2.12.14 (one grade per claim; node heads below carry the v2.12.14 owner RIDs, former atlas labels in parentheses); AZ [ENG PASS]', 'TDRG TB-12', 'D5 header aliases')
    # ---- HEADLINE ----
    a.rep('H4 D-RID high — discrete and historical RID vacuum: TDR-G core theorems/definitions carry no RIDs; seven OFN imports are "RID unavailable" (TDRG.G2 ≡ OFN.O5 ≡ METH.M2); PREL has one RID in total (PREL.P5);',
          'H4 D-RID high — historical RID vacuum, narrowed: TDR-G v2.12.14 registered 36 claim RIDs (the consumed definitions, the three §6.2 theorems, the four lemmas, the BIND3 results) with a §7 owner RID map for the consumer names — OFN\'s "RID unavailable" imports from TDR-G resolve once OFN repins (OFN.O5 ≡ METH.M2); PREL has one RID in total (PREL.P5);', 'TDRG TB-09', 'H4')
    a.line('H9 D-SCOPE/D-LINK high (discrete) —',
           'H9 D-CONV/D-LINK med (discrete) — the path-orientation degeneracy at S=0, |E|=N/2 is ruled in TDR-G v2.12.14: TDRG-DEF-ORIENT declares the balanced tie on S=0 ∧ 2E≡0 (no orientation from the declared invariants, TDRG-ALG-ORIENT-NOGO), SG-14 names the covariance group, and every v18-computed result is kept with [conv: v18 path orientation] EV-NOT-RERUN under the three-node census bound (4.9 % of k=1 states); 20 of 136 DISC-2 records change under the rule, the ten labels do not; NUMGEN re-annotates and decides its C7C-M4 release itself (D5.X1). Residual non-covariance in a non-canonical branch: largest_center chooses between equal-degree centres by node ID (TDRG.G10; TDR-19 open). The headline exponent is range-tagged by the owner ([NUM] full range −0.869; 480–1440 ≈ −0.730 from its own Exp-0 line); the superseded χ=0.836 check is withdrawn.', 'TDRG TA-01/TA-04', 'H9')
    a.rep('and the infinite-record readout RECOG-RESULT-A1C-RECORD-PHASE-READOUT (D3; NUMGEN informed, no custody change).',
          'and the infinite-record readout RECOG-RESULT-A1C-RECORD-PHASE-READOUT (D3; NUMGEN informed, no custody change); RECOG v0.3.25 adds the known-a sharpened schedule RECOG-THM-A1C-SHARPENED-SCHEDULE [assuming: Dyadic (D5) row-A proof constants], a record-only outer enclosure of (a, L, a−b, Θ₀) by an interval contractor (RECOG-ALG-A1C-JOINT-CONTRACTOR; windows, not identification, no uniqueness) and the record-fiber result (fibers on one C¹ level curve of Ψ_∞; A1c-Q1′ stays OPEN), plus the sharpened R9 rows (259.2, 1/400), (81.49, 1/1600) — the (D5) constants and the C₇ ceilings remain [assuming:] until Dyadic registers them (RECOG.R-A1).', 'RECOG v0.3.25', 'H5')
    # ---- D1 ----
    a.line('METH.M2 D-RID (programme pattern):', 'METH.M2 D-RID (programme pattern): "RID unavailable" imports / unnumbered theorems recur in PREL (one RID total), NUMGEN tier 2 (C7C, DISC, ten-label results under module RIDs), AZ, Legacy imports; TDR-G registered its claim RIDs in v2.12.14 and NUMGEN its tier 1 in v1.21; only owners register RIDs (METH v1.4 §4.4).', 'TDRG TB-09', 'METH.M2')
    a.line('OFN.O5 D-RID (to TDRG):', 'OFN.O5 D-RID (to TDRG, owner side done): the load-bearing imports IMP-O08-02 state, -03 band, -04 holonomy, -04B narrow-band, -08 finite recurrence, -09 star rule and the legacy LEM-*/CONV-* labels are "RID unavailable" in OFN v0.10; TDR-G v2.12.14 registered TDRG-DEF-ZN-STATE, -BAND, -CONV-TICK, -CONV-P3CYC, -STAR, TDRG-THM-HOLONOMY, -NARROW-BAND-EXCLUSION, -RECURRENCE and the four lemma RIDs TDRG-ALG-LEM-REACH, -NOANNIHIL, -RETRIG, -SPECCONS with a §7 alias map; the repin is OFN\'s (notice filed in pipes/OFN/). GEN zero-origin (IMP-O08-01) still without RID.', 'TDRG TB-09', 'OFN.O5')
    a.line('OFN.O7 ≡ TDRG.G4 |', 'OFN.O7 | TDR-G LEM-RETRIG prose "exact period-2 bound state even at d=0" | corrected in TDR-G v2.12.14 (period dividing 2; least period 2 for d≠0; d=0 a fixed point); OFN08-C12 correction on the OFN side still to be recorded', 'TDRG TA-05', 'OFN.O7 (D-WRONG list)')
    # ---- D2 N-I1 ----
    a.line('NUMGEN.N-I1 D-LINK (receiver side) |', 'NUMGEN.N-I1 D-LINK (receiver side) | five v1.21 `kind: notice` items filed by NUMGEN after its tag (pipes/RECOG, pipes/DYAD, pipes/TDRG, pipes/GEN, pipes/OFN): acceptance matrix and GAP-LOCK/INF-2 RIDs (RECOG), row-A import and DYAD-ALG-P5-RADIAL alias (Dyadic), C7C-M4 HOLD (TDR-G), Genesis v2.9 pin and the cyclic-average RID (Genesis), §6.8 OFN v0.10 pointer (OFN). TDR-G closed its two inbox items after v2.12.14 (request: accept · release record; notice: no action) and filed three notices of its own (pipes/NUMGEN, pipes/OFN, pipes/AZ, `' + PIPE_NOTICE + '`: TDRG-DEF-ORIENT ruling with the witness-effect table and RIDs; owner RIDs replacing "RID unavailable"; TDRG-ZN-STATE alias and the AZ cross-citation). The other receivers (RECOG, DYAD, GEN, OFN, AZ) have not dispositioned their items. A filed item is not adopted use; each receiver decides at its own checkpoint (CONVENTIONS §7).', 'pipes', 'NUMGEN.N-I1')
    # ---- D3 RECOG ----
    a.sub_in_line('RECOG-THM-R9-MEMORY THM | sc: postulated T;', '| cert recog_cell_r9_memory_cert.py (200-bit, 7 checks) | @§1,§6.13a',
                  '| cert recog_cell_r9_memory_cert.py (200-bit, 7 checks) | v0.3.25 sharpened rows (adopted rows stay in force): RECOG-ALG-R9-SUM-LEMMA Σq_m³≤(1+q₀)q₀² (within the one-orbit bound essentially sharp) ⇒ RECOG-THM-R9-SHARPENED-ROWS (C₂,q_max)=(259.2,1/400), (81.49,1/1600), incompleteness windows ×2 (K_Φ re-enclosed 258.4848 / 81.4328); RECOG-THM-R9-SHARPENED-ROWS-C7 [assuming: C₇≤85.1 / 27.7 — Dyadic\'s published NF-REM certificate values 85.07 / 27.60, not Dyadic theorem statements, registration requested] (221.4, 1/400), (75.69, 1/1600); cert RECOG-ART-R9-SHARPENED-ROWS | @§1,§6.13a', 'RECOG B1', 'R9-MEMORY node')
    a.sub_in_line('RECOG-THM-A1B-SLIP-SCHEDULE-U THM |', 'GAP-LOCK/INF-1 remain NUMGEN\'s (NUMGEN informed, no custody',
                  'GAP-LOCK/INF-1 remain NUMGEN\'s (NUMGEN informed, no custody change; recorded by NUMGEN v1.21 as independent agreement) | v0.3.25: RECOG-THM-A1C-SHARPENED-SCHEDULE [assuming: Dyadic (D5) row-A bridge proof constants] — same schedule with the known-a / declared-data centre c\'\'\'_k(a)=τψ(a+M_k)−(k−1)π/3+(√3/8)(a+M_k)^{−1/2}+(τ/2)(a+M_k)^{−1} and an error E\'\'\'=O_a((1+log(a+M_k))/(a+M_k)) computable from (a, M_k, r_k) — not from the record alone; harmonic tails with the universal ceiling E\'≤0.31 (RECOG-ALG-A1C-TAIL-HARMONICS, -INBLOCK-ANGLE), the two tails combine exactly into one boundary term (RECOG-ALG-A1C-COMBINED-TAIL); cert RECOG-ART-A1C-SHARPENED-SCHEDULE; the A1b "Not supplied" status for a computable envelope is supplied in place (', 'RECOG A1c-E', 'A1b node')
    a.sub_in_line('RECOG-RESULT-A1C-RECORD-PHASE-READOUT RES[from THM] |', 'with a unknown no window (NUM least-squares (â,L̂) ≤3.5% on illustration runs, no guarantee);',
                  'with a unknown: v0.3.25 supplies a certified outer enclosure from a finite record alone — admissible region ℛ_K={(a,L): a≥625, |c_k(a)−L|≤E_k(a) ∀k≤K} and its first finite interval from two slips (RECOG-ALG-A1C-ADMISSIBLE-REGION), start sector n₀≤7 and signed start offset (RECOG-ALG-A1C-START-OFFSET), interval contractor on (a, L, a−b, Θ₀) with the true a never an input (RECOG-ALG-A1C-JOINT-CONTRACTOR; [assuming: (D5)]; ≥2 usable slips; windows, not identification; no uniqueness, no write mechanism, no Q1′ conclusion; cert RECOG-ART-A1C-DECODER; NUM least-squares (â,L̂) ≤3.5 % on illustration runs stays an illustration);', 'RECOG A1c-D', 'A1c readout node')
    a.sub_in_line('RECOG-RESULT-A1C-RECORD-PHASE-READOUT RES[from THM] |', '| >R6 sub-items A1c-Q1′ (injectivity of x₀↦ℛ(x₀) on U, open), A1c-decoder | @§6.16e',
                  '| v0.3.25 record fibers: the record is the threshold coding g_{j+1}=7 ⟺ o_j<Δ_j of the overshoot sawtooth (RECOG-ALG-A1C-THRESHOLD-CODING); Ψ_∞ is C¹ in (log q₀, Θ₀) on the punctured row disk with |∂_{Θ₀}Ψ_∞−1|≤11.13 q₀ and ∂_{log q₀}Ψ_∞=−τ+O(q₀), so record fibers lie on one C¹ level curve — empty interior; connectedness and injectivity open (RECOG-ALG-A1C-PHASE-C1-FIBER; conditional on DYAD NF-REM/NF-INV/NF6 only; cert RECOG-ART-A1C-Q1PRIME-FIBER) | >R6 sub-items A1c-Q1′ (injectivity of x₀↦ℛ(x₀) on U, open; reworded v0.3.25), A1c-decoder (answered in bounded form, v0.3.25) | @§6.16e', 'RECOG A1c-Q', 'A1c readout node sub-items')
    a.sub_in_line('RECOG-OPEN-EVENT-RULE (R6) ACTIVE |', 'OPEN sub-items (v0.3.24): A1c-Q1′ — is x₀↦ℛ(x₀) (start state → complete token record) injective on U? neither answer established (the cell\'s local-nonconstancy argument is SESSION, conjectural); A1c-decoder — finite-prefix window for (a,L) with a unknown, and a record-only majorant for the known-a window via Q_m≤Q₀/(1+½Q₀m) and the A1a tail estimates',
                  'OPEN sub-items (v0.3.25): A1c-Q1′ — is x₀↦ℛ(x₀) (start state → complete token record) injective on U? neither answer established; known: record fibers lie on one C¹ level curve of Ψ_∞ in the chart row, hence have empty interior (RECOG-ALG-A1C-PHASE-C1-FIBER; the former SESSION conjecture proved, conditional on the Dyadic normal-form rows); connectedness open; record equality on the curve is equality of threshold codings; A1c-decoder — answered in bounded form ✓: certified outer admissibility windows on U for records with ≥2 usable slips under the (D5) [assuming:] (RECOG-ALG-A1C-JOINT-CONTRACTOR) — no identification, no uniqueness, no write mechanism, no Q1′ conclusion', 'RECOG R6', 'R6 node')
    a.sub_in_line('RECOG.R-D1 D-PROOF (c)/(b) |', 'the v0.3.24 artifacts RECOG-ART-A1B-SIXSTEP-DEFICIT and RECOG-ART-A3-QUADRATURE-TYPING are in evidence/recog/ with hashes (naming checked, not rerun here).',
                  'the v0.3.24 artifacts RECOG-ART-A1B-SIXSTEP-DEFICIT and RECOG-ART-A3-QUADRATURE-TYPING and the v0.3.25 artifacts RECOG-ART-R9-SHARPENED-ROWS, RECOG-ART-A1C-SHARPENED-SCHEDULE, RECOG-ART-A1C-DECODER, RECOG-ART-A1C-Q1PRIME-FIBER are in evidence/recog/ with hashes (naming checked, not rerun here; the v0.3.25 certificates were not rerun for the owner build either, release record §3).', 'RECOG v0.3.25', 'RECOG.R-D1')
    a.after_line('RECOG.R-D1 D-PROOF (c)/(b) |', ['RECOG.R-A1 D-LINK (cross-owner dependency) | RECOG v0.3.25 proves RECOG-THM-A1C-SHARPENED-SCHEDULE and the A1c decoder blocks [assuming: the Dyadic (D5) row-A bridge proof constants 0.79246, 0.36915 of the LPHASE row-A proof] and RECOG-THM-R9-SHARPENED-ROWS-C7 [assuming: C₇≤85.1 / 27.7, Dyadic\'s published NF-REM certificate values rounded up]; neither is a Dyadic theorem statement, so nothing in v0.3.25 is unconditional on them; RECOG\'s two requests to Dyadic (register (D5) and the C₇ ceilings as owner statements) are prepared in its release record §4, not filed as pipe items. The claim audit of the build found the constants present in dyad-v6.4.22 at statement level. RECOG still pins NUMGEN v1.20.8 (repin to v1.21 is RECOG\'s separate maintenance).'], 'RECOG v0.3.25', 'RECOG.R-A1 new')
    # ---- D5 L2 node heads -> owner RIDs (old labels kept as aliases) ----
    a.line('*TDRG:state DEF |', 'TDRG-DEF-ZN-STATE DEF (alias TDRG-ZN-STATE; v2.12.14) | ℤ_N, N even (SG-4, unique antipode); X_n=(θ₁..θ_M, δ₁..δ_M)∈⊔_{M≥2}ℤ_N^{2M}; M grows at star blow-up; physical state = quotient by global phase θ_i↦θ_i+c; relabelling covariance declared (SG-14, v2.12.14); Δ_ij=(θ_i−θ_j) mod N; relative advance d_ij=δ_i−δ_j; kinematics Δ_{ij,n+1}=Δ_{ij,n}+d_{ij,n} (TDRG-DEF-PHYSICAL-STATE, -REL-ADVANCE, -KINEMATICS) | ≡ OFN IMP-O08-02 | ! OFN Finding A: common token shift NOT a full-model gauge — statement accepted by TDR-G v2.12.14 §7, outside SG-14\'s group | AZ\'s "TDRG-ZN-STATE" resolves through the v2.12.14 §7 alias map | >NUMGEN imp-DISC (RID available since v2.12.14; NUMGEN repin is NUMGEN\'s) @TDRG§6.1', 'TDRG TB-09', 'state node')
    a.head('*TDRG:band DEF |', 'TDRG-DEF-BAND DEF (with TDRG-DEF-EDGE-SET, -NARROW-BAND; v2.12.14) |', 'TDRG TB-09', 'band node')
    a.head('CONV-TICK DEF·ENG PASS v18 |', 'TDRG-DEF-CONV-TICK DEF·ENG PASS v18 (alias CONV-TICK) |', 'TDRG TB-09', 'CONV-TICK node')
    a.head('TDRG-SWAP DEF |', 'TDRG-DEF-SWAP DEF |', 'TDRG TB-09', 'swap node')
    a.head('CONV-P3CYC DEF·script-certified v18 |', 'TDRG-DEF-CONV-P3CYC DEF·script-certified v18 (alias CONV-P3CYC) |', 'TDRG TB-09', 'P3CYC node')
    a.line('TDRG-ORIENT DEF |', 'TDRG-DEF-ORIENT DEF [COR v2.12.14] (alias TDRG-ORIENT) | P_n listed [v₁..v_n]: S=Σ signed_defect_error(θ_{v_i},θ_{v_{i+1}},N) (TDRG-DEF-SIGNED-DEFECT-ERROR; reversal-odd on defect edges since |·|≤k<N/6); S>0 forward, S<0 reversed; S=0 ⇒ E=signed_centered(δ_{v_n}−δ_{v_1},N) (TDRG-DEF-SIGNED-CENTERED, representative in (−N/2,N/2] — the half-open choice makes signed_centered(±N/2)=+N/2): 0<E<N/2 forward, −N/2<E<0 reversed; S=0 ∧ 2E≡0 (E∈{0,N/2}) ⇒ balanced path-tie (no orientation from the declared invariants; policies treat it as before: bound_path_tie/bound_symmetric inert, trap/bound_multistar ambiguous) | superseded completion: v2.12.13 declared the tie only at S=E=0, and at S=0 ∧ E≡N/2 the v17/v18 engine oriented "forward" relative to the node-ID listing (raw_ordered_path) — the arbitrary-label fallback Appendix B rejects; every motif-log and BIND3 result stems from it and is kept [conv: v18 path orientation] EV-NOT-RERUN | reference implementation evidence/tdrg/scripts/tdrg_orient_v2_12_14.py (TDRG-ART-ORIENT-V2-12-14) | >NUMGEN DISC-1/DISC-2 (re-annotation NUMGEN\'s), OFN REQ-O09-05 (answered) @TDRG§6.3', 'TDRG TA-01', 'orient node')
    a.after_line('TDRG-DEF-ORIENT DEF [COR v2.12.14]', [
        'TDRG-ALG-ORIENT-NOGO ALG (v2.12.14) | reversal maps S↦−S always and E↦−E except when δ_{v_n}−δ_{v_1}≡N/2, where signed_centered gives +N/2 for both listings ⇒ on S=0 ∧ E≡N/2 the pair (S,E) is reversal-invariant: any selector that is a function of (S,E) alone is the tie or depends on the listing; the extended tie is the declared rule\'s covariant completion and adds no input | recorded alternative, not adopted: for P₃ with centre c, G=sc(δ_{v₁}−δ_c)−sc(δ_{v₃}−δ_c) is reversal-odd and never 0 on the stratum (δ_{v₃}−δ_{v₁}≡N/2≠0; atlas check C2, exhaustive N=24) — admitting the centre token would give a covariant non-tie rule for P₃ (palindromic ties for longer paths), a law choice of the TDR-19 kind kept for the later sensitivity campaign (make_orient_g_alternative) @TDRG§6.3',
        'TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE ALG | sc: one explicit state; pinned v18 engine | N=24, k=1, θ_pre=(0,11,12), δ=(0,1,12) → θ=(0,12,0), defect path 0–1–2, S=0, E=+12=N/2 under both listings; exchanging the endpoint labels changes the v18 outcome (δ′=(1,12,0), not the relabelled image); under TDRG-DEF-ORIENT the event is a tie and the step equivariant (G-alternative δ′=(12,0,1), also equivariant) | negative control of the v2.12.14 checker (gate C10) | ev evidence/tdrg/disposition/antipodal_fixture.txt @TDRG§6.12',
        'TDRG-NUM-ORIENT-EQUIVARIANCE-N24 NUM | sc: N=24; three nodes exhaustive over the 331,776 gauge-reduced states at k=1 and k=3, generators (01),(12) of S₃; four nodes 100,000 random (state, k∈{1,2,3}, π∈S₄) samples; bound_symmetric (and largest_center at four nodes); the pinned engine\'s own step_universe with only orient_path exchanged | failures per generator: v18 72/72 (k=1), 168/168 (k=3); TDRG-DEF-ORIENT 0; G-alternative 0; four nodes v18 112, both covariant rules 0; global phase shift 0 everywhere | a finite check, not a theorem for all N or all policies | ev evidence/tdrg/disposition/owner_relabel_equivariance_check.py (2f54e0fc…) | atlas census (independent, three nodes, k=1): under v18 77 of 9,800 eventual cycles contain a listing-dependent event, 16,322 of 331,776 states (4.9 %) flow into one; under the extended tie 9,789 cycles, 66 with a tie on the stratum; whether any of the 3,456 retrigger-entry or 10,368 one-pass BIND3 ICs reaches the stratum is undetermined (IC script missing) | ev evidence/atlas/tdrg/atlas_tdrg_orientation_covariance_check.py (5684da96…) @TDRG§6.12',
        'TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY ALG (v2.12.14) | the mirror (θ,δ)↦(−θ,−δ) is not a step symmetry at P₃ events: the mirrored state orients reversed, so the successor shift becomes a predecessor shift ((δ₁,δ₂,δ₃)↦(δ₂,δ₃,δ₁) vs (−δ₃,−δ₁,−δ₂)≠−(δ₂,δ₃,δ₁) unless the three tokens are equal); 60,000 random three-node states, N=24, k=1: 2,661 equivariance failures, all among the 2,703 states with a P₃ event; the §6.12 "±d mirror symmetry" is an identity of class inventories (mirror-inventory check), not equivariance | ev evidence/tdrg/disposition/mirror_probe.py @TDRG§6.12',
        'TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK ALG (v2.12.14; owner finding N1) | sc: non-canonical branch largest_center | choose_largest_center sorts centres by (−degree, node id): between equal-degree multistar centres the one with the smaller ID fires — not relabelling-covariant (K_{2,3} fixture, N=24, k=1, two centres of equal degree 3 with tokens 1 and 2: exchanging the centre labels changes which fires); bound_symmetric (binds) and all_centers (all fire, modulo newborn labels) are equivariant | recorded exception to SG-14; the largest_center policy-fate results carry it as a scope note EV-NOT-RERUN; resolution belongs with TDR-19 (TDRG.G10) | ev evidence/tdrg/disposition/multistar_fixture.py @TDRG§6.6'],
        'TDRG TA-01/TA-08/N1/N2', 'new orientation nodes')
    a.head('TDRG-CYCLE DEF |', 'TDRG-DEF-CYCLE-BOUND DEF |', 'TDRG TB-09', 'cycle node')
    a.head('*TDRG:star DEF |', 'TDRG-DEF-STAR DEF |', 'TDRG TB-09', 'star node')
    a.sub_in_line('TDRG-DEF-STAR DEF |', '| < RTG-OFN-ALG-STAR-TOKEN-SHIFT (equivariant under common token shift c iff 2c=0) @TDRG', '| < RTG-OFN-ALG-STAR-TOKEN-SHIFT (equivariant under common token shift c iff 2c≡0; statement accepted by TDR-G v2.12.14 §7, custody transfer XFER-O08-01 deferred to v2.13) @TDRG', 'TDRG TC-15', 'star node OFN edge')
    a.head('TDRG-MULTISTAR DEF |', 'TDRG-DEF-MULTISTAR DEF (with TDRG-DEF-CANONICAL-BRANCH) |', 'TDRG TB-09', 'multistar node')
    a.sub_in_line('TDRG-DEF-MULTISTAR DEF', 'bound_symmetric (canonical clean branch = multistar + balanced path-tie bound)', 'bound_symmetric (canonical clean branch = multistar + balanced path-tie bound; the tie includes S=0 ∧ E≡N/2 since v2.12.14)', 'TDRG TA-01', 'multistar node tie')
    a.head('*TDRG:holonomy THM |', 'TDRG-THM-HOLONOMY THM |', 'TDRG TB-09', 'holonomy node')
    a.line('*TDRG:narrow-band THM |', 'TDRG-THM-NARROW-BAND-EXCLUSION THM | k<N/6 ⇒ |E_def∩K₃|≤2 (no fully defective K₃) | ≡ OFN IMP-O08-04B | v2.12.14 cites AZ-ALG-ANTIPODAL-LOWORDER as AZ\'s strict generalisation (odd L impossible for Lk<N/2); the same arithmetic in two homes, cross-cited since v2.12.14 @TDRG', 'TDRG TC-16', 'narrow-band node')
    a.head('*TDRG:recurrence THM |', 'TDRG-THM-RECURRENCE THM |', 'TDRG TB-09', 'recurrence node')
    a.head('*TDRG:reach-k0 THM |', 'TDRG-THM-REACHABILITY-K0 THM |', 'TDRG TB-09', 'reach node')
    a.head('LEM-REACH ALG (NUM exhaustive even N≤40, 77,552 band cases) |', 'TDRG-ALG-LEM-REACH ALG (alias LEM-REACH; NUM exhaustive even N≤40, 77,552 band cases) |', 'TDRG TB-09', 'LEM-REACH node')
    a.head('LEM-NOANNIHIL ALG (NUM N=2–40 all states) |', 'TDRG-ALG-LEM-NOANNIHIL ALG (alias LEM-NOANNIHIL; NUM N=2–40 all states) |', 'TDRG TB-09', 'LEM-NOANNIHIL node')
    a.line('LEM-RETRIG ALG (NUM even N≤40, k≤N/6) |', 'TDRG-ALG-LEM-RETRIG ALG (alias LEM-RETRIG; NUM even N≤40, k≤N/6) | sc: isolated dyad, CONV-TICK | ε=Δ−N/2∈B_k=[−k,k]; swap d↦−d, ε′=ε−d; retrigger iff ε∈B_k∩(B_k+d); exists iff |d|_c≤2k; all offsets retrigger iff d=0; realized overlap: retrigger on every tick, map period dividing 2 — least period 2 for d≠0, (ε,0) a fixed point at d=0 (v2.12.14 wording; the band |d|_c≤2k<N/3 never reaches N/2, so d=0 is the only degenerate case) | >OFN IMP-O08-07, AZ-B @TDRG', 'TDRG TA-05', 'LEM-RETRIG node')
    a.line('LEM-SPECCONS ALG (NUM 3000 ICs × 500 steps, 0 violations) |', 'TDRG-ALG-LEM-SPECCONS ALG (alias LEM-SPECCONS; NUM 3000 ICs × 500 steps, 0 violations) | sc: 3 nodes, no star | free advance fixes δ; swap = signed transposition of (d_AB,d_BC,d_CA) (Σ≡0); P₃ shift = cyclic permutation; ties = identity ⇒ multiset {|d_AB|_c,|d_BC|_c,|d_CA|_c} exactly conserved; therefore, in particular, the gcd-spacing multiset is conserved (v2.12.14 wording; converse fails: N=24, |d|_c=1 and 5 share gcd 1); the extended balanced tie of TDRG-DEF-ORIENT is identity too, so the lemma is unchanged by the ruling | n-node signed-permutation invariance CAND for swap/path sectors; across star OPEN (SG-12) | >OFN IMP-O08-16, AZ-B, NUMGEN DISC @TDRG', 'TDRG TA-06', 'LEM-SPECCONS node')
    a.line('*TDRG:bulk-fits NUM strong (fits) / HEUR strong (exponent reading) |', '*TDRG:bulk-fits NUM (fits; one grade since v2.12.14) / HEUR (exponent reading beyond the scan) | range-tagged by the owner (v2.12.14 §1, §5, §6.8). FULL range N=120–1440, t≥4001, M≤500, k/N=1/15, T=5000, bound_symmetric: C_birth 9.514N^{−1.593} (R² 0.993); C_component 0.7366N^{−0.757} (0.939); χ composite (cs/row ~N^{−0.73}); B_bulk/step 1.041N^{−0.869} (0.973) [headline α=0.869 = full-range composite, window-dependent]; O_bulk/step 0.1094N^{+0.723} (0.972); M_bulk 419.5N^{−0.295} (0.881); O_slot/step 53.69N^{+0.709} (0.976); ψ_slot 0.00204N^{+0.014} (0.015, intensive); consistency 0.709+0.014=0.723, 0.869≈1.593−0.723. HIGH-N window 480–1440 (owner §2 OPEN-POLICY-GEOMETRY Exp-0 line): C_component N^{−0.936}, χ N^{+0.697}, C_birth N^{−1.633} (R² 0.976), O/step N^{+0.903}, B/step N^{−0.730}. The former §1 check "1.593≈0.757+0.836" (superseded χ exponent) is withdrawn as [COR] in v2.12.14 | >AZ-B (quotes 0.869) @TDRG§1,§5', 'TDRG TA-04', 'bulk-fits node')
    a.head('*TDRG:crystallization HEUR strong |', '*TDRG:crystallization HEUR (v2.12.14: extrapolation grade) |', 'TDRG TA-04', 'crystallization node')
    a.head('BIND3-CYCLE-N24K1 ALG/NUM strong |', 'TDRG-ALG-BIND3-CYCLE-N24K1 ALG + NUM strong (alias BIND3-CYCLE-N24K1; [conv: v18 path orientation], EV-NOT-RERUN, census bound in TDRG-NUM-ORIENT-EQUIVARIANCE-N24) |', 'TDRG TB-09/TA-08', 'BIND3-CYCLE node')
    a.sub_in_line('TDRG-ALG-BIND3-CYCLE-N24K1', 'exact cycle enumeration, both P₃ conventions (3332/124 each):', 'exact cycle enumeration, both P₃ rotation conventions (3332/124 each — an inventory statement, not trajectory covariance; the "relabeling-covariance check" of v2.12.13 is the ±d mirror-inventory check, v2.12.14):', 'TDRG TA-08', 'BIND3-CYCLE wording')
    a.head('BIND3-PARITY NUM strong (+ALG necessity at N=24) |', 'TDRG-NUM-BIND3-PARITY NUM strong (alias BIND3-PARITY; +ALG necessity at N=24; [conv: v18 path orientation]) |', 'TDRG TB-09', 'BIND3-PARITY node')
    a.head('BIND3-SPECTRAL-GATE NUM strong |', 'TDRG-NUM-BIND3-SPECTRAL-GATE NUM strong (alias BIND3-SPECTRAL-GATE; [conv: v18 path orientation]) |', 'TDRG TB-09', 'SPECTRAL-GATE node')
    a.head('BIND3-MEMORY-PARITY NUM strong (+COR) |', 'TDRG-NUM-BIND3-MEMORY-PARITY NUM strong (alias BIND3-MEMORY-PARITY; +COR; [conv: v18 path orientation]) |', 'TDRG TB-09', 'MEMORY-PARITY node')
    a.head('BIND3-XFER NUM strong |', 'TDRG-NUM-BIND3-XFER NUM strong (alias BIND3-XFER; [conv: v18 path orientation]) |', 'TDRG TB-09', 'XFER node')
    a.head('BIND3-REGEN NUM strong |', 'TDRG-NUM-BIND3-REGEN NUM strong (alias BIND3-REGEN; [conv: v18 path orientation]) |', 'TDRG TB-09', 'REGEN node')
    # NUMGEN DISC nodes: the ruling
    a.sub_in_line('*NUMGEN:DISC-1 ALG |', '| NUM·dx: P2 exposure 0/22; projection {2:1,3:1} unchanged under reverse/inert policies @NUMGEN§6.6', '| NUM·dx: P2 exposure 0/22; projection {2:1,3:1} unchanged under reverse/inert policies; TDR-G ruled the stratum a tie (TDRG-DEF-ORIENT, v2.12.14), NUMGEN\'s DISC-1 re-annotation is its own @NUMGEN§6.6', 'TDRG TC-14', 'DISC-1 node')
    a.sub_in_line('*NUMGEN:P2-exposure NUM·dx |', 'Discrete-owner ruling required before future campaigns | ! TDRG-ORIENT (X1) @NUMGEN§6.6', 'TDR-G ruling given in v2.12.14 (TDRG-DEF-ORIENT: balanced tie on the stratum; under it 20 of 136 records change, ten labels unchanged, 96 unexposed unchanged by construction; notice filed in pipes/NUMGEN/); NUMGEN\'s re-annotation and its C7C-M4 release decision are NUMGEN\'s (D5.X1) @NUMGEN§6.6', 'TDRG TC-14', 'P2-exposure node')
    # ---- D5.L4 SG-14 ----
    a.sub_in_line('TDRG SG-1 no continuous space/time ·', 'TDRG SG-1 no continuous space/time ·', 'TDRG SG-14 (v2.12.14) relabelling covariance: on bound_symmetric (and on other branches only once separately established) the step commutes with Sym(V)×ℤ_N^phase, equality modulo relabelling of newborn nodes; ties declared on invariant data only; the common token shift and the mirror are outside the group; largest_center\'s ID tie-break is a recorded exception · SG-1 no continuous space/time ·', 'TDRG TA-03', 'D5.L4 SG line')
    a.sub_in_line('TDR-T ladder (App C, gated):', '"safe-wedge reachability" (stale referent, TDRG.G6)', '"safe-wedge reachability" (historical continuous reference since v2.12.14: TRIAD v1.6.1 wedge / x*, CN-05)', 'TDRG TA-07', 'TDR-T ladder line')
    a.sub_in_line('*TDRG:retired FAIL |', '"K₃ globally explosive (96:1 healing/pump)" (stale referent, TDRG.G6)', '"K₃ globally explosive (96:1 healing/pump)" (marked a historical continuous reference in v2.12.14)', 'TDRG TA-07', 'retired FAIL line 96:1')
    a.sub_in_line('*TDRG:retired FAIL |', 'arbitrary path label tie-break;', 'arbitrary path label tie-break; the node-ID completion of the orientation rule at S=0 ∧ E≡N/2 (v2.12.14, an instance of it);', 'TDRG TA-01', 'retired FAIL line')
    # ---- D5.L5 ----
    a.drop_line('TDRG.G1 D-SCOPE/D-CONV (high):', 'TDRG TA-04', 'TDRG.G1 retired')
    a.drop_line('TDRG.G2 D-RID (≡ OFN.O5, AZ.A7, METH.M2):', 'TDRG TB-09', 'TDRG.G2 retired')
    a.drop_line('TDRG.G3 D-LINK:', 'TDRG TC-15', 'TDRG.G3 retired')
    a.drop_line('TDRG.G4 D-WRONG (minor; ≡ OFN.O7, OFN08-C12):', 'TDRG TA-05', 'TDRG.G4 retired')
    a.drop_line('TDRG.G5 ≡ AZ.A6 D-SCOPE:', 'TDRG TA-06', 'TDRG.G5 retired')
    a.drop_line('TDRG.G6 D-STALE (cross-stream):', 'TDRG TA-07', 'TDRG.G6 retired')
    a.drop_line('TDRG.G7 ≡ AZ.A4 D-LINK (atlas-checked):', 'TDRG TC-16', 'TDRG.G7 retired')
    a.line('TDRG.G8 D-STALE (internal):', 'TDRG.G8 D-STALE (internal, residual after v2.12.14): the footer supersession chain of fourteen point releases and the Appendix A ordering (v2.12 before v2.12.14…v2.12.1) are layout items deferred to v2.13 together with the Methodology v1.4 migration (PI decision 27 Oct 2026); the header date, the companion editions, the TDR-24B live status and the Appendix C gate were corrected in v2.12.14. The edition still declares Methodology v1.2.', 'TDRG TB-13', 'TDRG.G8 reworded')
    a.after_line('TDRG.G9 ~ D-LINK (D-RID duplicate):', [
        'TDRG.G10 D-CONV (non-canonical branch; owner finding N1, v2.12.14): largest_center chooses between equal-degree multistar centres by node ID (TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK), outside SG-14; the branch\'s policy-fate results (§§6.6–6.7, OPEN-POLICY-GEOMETRY slice) carry a scope note, EV-NOT-RERUN; canonical results unaffected (bound_symmetric binds multistars). Resolution belongs with TDR-19 (policy selection), v2.13 or later.',
        'TDRG.G11 D-PROOF (b)/(a) (evidence custody, v2.12.14 §8): placed — genesis_mode_b_mc.py 4c94d874… (engine label "v15.3"; "v17" is the data-campaign label; replay-verified producer for two v17 files, schema-consistent for the other placed ones), genesis_mode_b_mc_v18.py 9d787b43… (byte-equal to NUMGEN\'s copy; same orient_path), tdr_motif_bootstrap v1–v6, analysis scripts, the TDR-24/25/26 session scripts (upload/tdrg-session-scripts, 17 files); partly placed / held with hashes — the v17 and v16 motif corpora (ten files >100 MB on the PI\'s machine, SHA-256 in SHA256SUMS_tdrg_held.txt); missing — the four session-certified suites TDRG-ART-KINEMATIC-CERTS, -SPECCONS, -BIND3-N24K1, -BIND3-SUITE and the v6 per-run CSV / DSN-patch outputs (custody (a); a re-derivation would be an independent contribution). Hash check records/tdrg/TDRG_UPLOAD_HASH_CHECK_20261027.md.'],
        'TDRG N1/TB-11', 'TDRG.G10, G11 new')
    a.line('AZ.A7 D-RID:', 'AZ.A7 D-RID: AZ\'s "TDRG-ZN-STATE" is an alias of TDRG-DEF-ZN-STATE in the TDR-G v2.12.14 §7 map (notice filed in pipes/AZ/); the AZ-side labels BIND3-*, TDR-24/N-SCALING, TDR-26-BIRTH-ANCHOR remain AZ\'s to repin (actual owner IDs: TDRG-ALG/NUM-BIND3-*; TDR-24/26 exist only as OPEN module RIDs).', 'TDRG TC-16', 'AZ.A7 reworded')
    a.line('D5.X1 ~ D-LINK / D-CONV:', 'D5.X1 D-LINK (ruled on the TDR-G side, v2.12.14): the second degenerate case S=0 ∧ |E|=N/2 of the path orientation rule — endpoint reversal invisible under signed_centered (−N/2,N/2], v18 resolving it by sorted node IDs — is declared a balanced path-tie (TDRG-DEF-ORIENT; TDRG-ALG-ORIENT-NOGO; SG-14); the v2.12.13 text and the v18 engine stand as the superseded completion; TDR-G\'s request disposition and notice to NUMGEN carry the witness-effect table (40 of 136 exposed; 20 change under the rule; ten labels unchanged; 96 unexposed unchanged; DISC-1 not covered). Residual, on the NUMGEN side: re-annotation of DISC-1/DISC-2 under TDRG-DEF-ORIENT at tdrg-v2.12.14 and the C7C-M4 release decision (NUMGEN v1.21 §2 item 1 HOLD). The owner-review tasks Programme v1.2 §6 listed for TDR-G (state/gauge conventions, antipodal path tie, counting observables, rank interpretation) are recorded in TDR-G §2 since v2.12.14 (the antipodal tie discharged); Programme v1.3 §6.4 does not list them (v1.2 §6 did).', 'TDRG TA-01/TC-17', 'D5.X1 reworded')

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

def stale_editions(text):
    return [l[:80] for l in text.split('\n') if re.search(r'`tdrg-v2\.12\.13`|\| v2\.12\.13 \| `tdrg|`recog-v0\.3\.24`|\| v0\.3\.24 \| `recog|needs a TDR-G scientific ruling|Discrete-owner ruling required|carry no RIDs; seven OFN imports|with a unknown no window', l)]

def checker():
    spec = importlib.util.spec_from_file_location('atlas_checker', ROOT / 'tools/atlas_check.py')
    c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c); return c

def main():
    global SNAPSHOT
    SNAPSHOT = git('rev-parse', SNAPSHOT + '^{commit}').decode().strip()
    base = at('atlas-v0.6', ATLAS).decode(); assert sha(base) == BASE_SHA
    a = Edit(base); refresh(a); text = a.text
    assert not stale_editions(text), stale_editions(text)
    # ---- manifest ----
    old = json.loads(at('atlas-v0.6', 'evidence/atlas/v0.6/source_manifest.json'))
    m = json.loads(json.dumps(old))
    m.update(atlas='v0.7', frozen_at='2026-10-28', repository_snapshot=SNAPSHOT, previous_atlas_tag='atlas-v0.6', method_tag='atlas-v0.2', method_edition='v0.2')
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_6_edition'] = prev['edition']; s['v0_6_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] in MOVED:
            mv = MOVED[s['key']]; data = at(mv['tag'], s['path'])
            s.update(edition=mv['edition'], tag=mv['tag'], commit=git('rev-parse', mv['tag'] + '^{commit}').decode().strip(), sha256=sha(data), authority=mv['authority'])
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(SNAPSHOT, s['path']), ('snapshot/tag divergence', s['key'])
        s['v0_6_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_6_input_equality'] for x in m['sources']) == {'EQUAL': 16, 'CHANGED': 2}
    assert next(s for s in m['sources'] if s['key'] == 'TDRG')['sha256'] == TDRG_SHA
    assert next(s for s in m['sources'] if s['key'] == 'RECOG')['sha256'] == RECOG_SHA
    wjson(OUT / 'source_manifest.json', m)
    # ---- H -> L5 ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys ----
    oldret = json.loads(at('atlas-v0.6', 'evidence/atlas/v0.6/retired_l5_keys.json'))
    newret = {'TDRG.G1': 'TDR-G v2.12.14 (TA-04/I06): headline exponent range-tagged [NUM] with window dependence citing its own Exp-0 line; the χ=0.836 consistency sentence withdrawn as [COR]; crystallization [HEUR].',
              'TDRG.G2': 'TDR-G v2.12.14 (TB-09/I08): 36 claim RIDs registered with a §7 owner RID map; OFN/AZ repins are theirs (OFN.O5, AZ.A7 reworded).',
              'TDRG.G3': 'TDR-G v2.12.14 §7 (TC-15/I11): OFN Finding A statement accepted (one-line algebra, EV-CODE), custody transfer XFER-O08-01 deferred to v2.13; REQ-O09-05 answered by TDRG-DEF-ORIENT and that entry.',
              'TDRG.G4': 'TDR-G v2.12.14 (TA-05/I04): LEM-RETRIG least-period wording at d=0 corrected in §1, §6.5 and the regime table.',
              'TDRG.G5': 'TDR-G v2.12.14 (TA-06/I05): "equivalently" → "therefore, in particular" with the N=24 counterexample; AZ.A6 stays as AZ\'s own wording item.',
              'TDRG.G6': 'TDR-G v2.12.14 (TA-07): K₃ 96:1 and the T-6 wedge / x* references marked historical continuous references (TRIAD v1.6.1, CN-05).',
              'TDRG.G7': 'TDR-G v2.12.14 (TC-16): narrow-band exclusion cites AZ-ALG-ANTIPODAL-LOWORDER as AZ\'s strict generalisation; AZ.A4 stays as AZ\'s side.'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.7 reasons in dispositions.json.'))
    # ---- shared checker ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at('atlas-v0.2', 'evidence/atlas/coverage_map_v0_2.json'))
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.7/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    # ---- new-node RID presence in the moved sources (naming check, not certificate replay) ----
    presence = {r: (('RID: ' + r) in src['TDRG']) for r in NEW_RIDS_TDRG}; presence.update({r: (('RID: ' + r) in src['RECOG']) for r in NEW_RIDS_RECOG})
    assert all(presence.values()), [k for k, v in presence.items() if not v]
    for p in ('pipes/NUMGEN/' + PIPE_NOTICE, 'pipes/OFN/' + PIPE_NOTICE, 'pipes/AZ/' + PIPE_NOTICE, 'records/tdrg/TDRG_UPLOAD_HASH_CHECK_20261027.md', 'evidence/tdrg/scripts/tdrg_orient_v2_12_14.py'):
        assert at(SNAPSHOT, p), p
    # ---- dispositions ----
    def row(t, key): return next((l for l in t.split('\n') if l.startswith(key + ' ')), None)
    touched = ['TDRG.G1', 'TDRG.G2', 'TDRG.G3', 'TDRG.G4', 'TDRG.G5', 'TDRG.G6', 'TDRG.G7', 'TDRG.G8', 'D5.X1', 'AZ.A7', 'OFN.O5', 'OFN.O7', 'METH.M2', 'NUMGEN.N-I1', 'RECOG.R-D1']
    disp = []
    for key in touched:
        o, n = row(base, key), row(text, key)
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded')
        disp.append(dict(key=key, disposition=state, reason=newret.get(key, 'reworded; see edit_log.json'), previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    for key in ['TDRG.G10', 'TDRG.G11', 'RECOG.R-A1']:
        disp.append(dict(key=key, disposition='new', reason='see edit_log.json', previous_sha256=None, current_sha256=sha(row(text, key))))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    t = text.replace('(TDRG.G10; TDR-19 open)', '(TDRG.G2; TDR-19 open)', 1); ctl('U1', 'H cites a retired L5 row', 'H9:TDRG.G2' in h_l5_map(t)['dangling'])
    t = text + 'TDRG.G1 D-SCOPE: reused\n'; ctl('U2', 'retired key reused', bool(c.run(t, m, src, cmap, idmap, retired, with_sources=False).fails()))
    t = text.replace('| v2.12.14 | `tdrg-v2.12.14` |', '| v2.12.13 | `tdrg-v2.12.13` |', 1); ctl('U3', 'SOURCES row older than manifest', bool(c.run(t, m, src, cmap, idmap, retired).fails()) or bool(stale_editions(t)))
    t = text.replace('TDRG-DEF-ORIENT DEF [COR v2.12.14]', 'TDRG-DEF-ORIENTATION DEF [COR v2.12.14]', 1); ctl('U4', 'new node RID misspelled against the source', bool(c.run(t, m, src, cmap, idmap, retired, with_sources=False).fails()) or ('RID: TDRG-DEF-ORIENTATION' not in src['TDRG']))
    t = text.replace('NUMGEN re-annotates and decides its C7C-M4 release itself (D5.X1)', 'needs a TDR-G scientific ruling (D5.X1)', 1); ctl('U5', 'stale "needs a ruling" wording reintroduced', bool(stale_editions(t)))
    t = text.replace('RECOG-ALG-A1C-JOINT-CONTRACTOR; windows, not identification, no uniqueness', 'RECOG-ALG-A1C-JOINT-CONTRACTORS; windows, not identification, no uniqueness', 1); ctl('U6', 'RECOG RID misspelled against the source', 'RID: RECOG-ALG-A1C-JOINT-CONTRACTORS' not in src['RECOG'])
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), controls
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas='atlas-v0.6', base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()), atlas_lines=text.count('\n') + 1,
                   source_snapshot=SNAPSHOT, changed_sources=list(MOVED), edit_operations=len(a.log), retired_keys=list(newret), new_keys=['TDRG.G10', 'TDRG.G11', 'RECOG.R-A1'],
                   new_node_rids=NEW_RIDS_TDRG + NEW_RIDS_RECOG, dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_controls=len(shared), focused_controls=len(controls),
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_7.py': sha(Path(__file__).read_bytes())},
                   limitations=['Structural checks only; no owner certificate rerun; new RIDs checked for presence in the tagged sources, not re-proved.',
                                'Impact refresh of two moved sources (TDRG v2.12.14, RECOG v0.3.25); the other 16 domains were not re-extracted; pipe items cited as filed, receiver dispositions are not atlas sources.',
                                'RECOG v0.3.25 §6.13a/§6.13b/§6.16e and TDRG v2.12.14 §6.3/§6.12/§7/§8 extracted at statement level from the tagged files; proofs live in the owner cells.'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
