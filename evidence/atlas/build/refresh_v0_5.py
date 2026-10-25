#!/usr/bin/env python3
"""Atlas v0.4 -> v0.5 candidate: impact refresh for two moved sources — Genesis v2.9 (`gen-v2.9`) and RECOG v0.3.24
(`recog-v0.3.24`). Dyadic is unchanged (v6.4.22); its new records (OPEN 20 LH2012 assessments) change no owner state.

GEN (D1, D4a, D4b, H1, H6, H8): source row; κ_f is owner notation (GEN §6.8 DEF); sourced-junction theorem rescoped
(GEN-THM-SOURCED-JUNCTION, w=0 ⇒ K₊=K₋, two antipodal stationary solutions, minimizer clause retracted to Appendix B);
RIDs GEN-THM-QH-NOGO, GEN-THM-SINGLE-FACE-METRIC; 9A sign-explicit; B_* declared undefined by the owner; custody keys
[custody-A]/[indep-AC]; §6.3c G-20 existence note (C^∞ via DYAD-THM-SMOOTH-EQUIVARIANT-CHART); Methodology v1.4 with
bounded [RESULT] migration. Retired: GEN.D1, D2, D4, D14 (D4b), F9, F10, F15, F16, F17, F19 (D4a); F20 narrowed to TRIAD.
RECOG (D3, H5): source row; new nodes RECOG-THM-A1B-SLIP-SCHEDULE-U, RECOG-RESULT-A1C-RECORD-PHASE-READOUT,
RECOG-ALG-QUADRATURE-TYPING, RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY; R4 sub-item answered in reframed form; R6 gains
two OPEN sub-items; the v0.3.23 live-file exception is resolved (RECOG.R-P3, R-T1 retired).
Programme: new row PROG.G8 (κ table lacks κ_f; E-P13-1). Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_5.py
"""
from __future__ import annotations
import hashlib, importlib.util, json, re, subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.5'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = '75f8dc95520aaceac6a36614016902b408a8b52e'   # origin/main after PR #56 (gen-v2.9 BASELINE sync)
BASE_SHA = 'b63eaf8b85dbb1f4a8fbee61cb82f2af089276797c387e6a8a0b13922805c35b'   # atlas-v0.4
MOVED = {'GEN': dict(edition='v2.9', tag='gen-v2.9', authority='OWNER: records/gen/GEN_v2_9_RELEASE_RECORD.md at gen-v2.9'),
         'RECOG': dict(edition='v0.3.24', tag='recog-v0.3.24', authority='OWNER: records/recog/RECOG_v0_3_24_RELEASE_RECORD.md at recog-v0.3.24')}

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
        self.log.append(dict(id=f'AR05-{len(self.log)+1:03d}', finding=finding, where=where, old_sha256=sha(old), new_sha256=sha(new), old=old, new=new))
    def _one(self, prefix, finding, where):
        ls = [l for l in self.text.split('\n') if l.startswith(prefix)]
        assert len(ls) == 1, (finding, where, prefix, len(ls)); return ls[0]
    def line(self, prefix, new, finding, where): self.rep(self._one(prefix, finding, where), new, finding, where)
    def drop_line(self, prefix, finding, where): self.rep(self._one(prefix, finding, where) + '\n', '', finding, where)
    def after_line(self, prefix, new_lines, finding, where):
        l = self._one(prefix, finding, where); self.rep(l + '\n', l + '\n' + '\n'.join(new_lines) + '\n', finding, where)

def refresh(a: Edit):
    # ---- identity ----
    a.rep('# RTG STATE ATLAS v0.4\n', '# RTG STATE ATLAS v0.5\n', 'identity', 'title')
    a.rep('full identities in evidence/atlas/v0.4/source_manifest.json', 'full identities in evidence/atlas/v0.5/source_manifest.json', 'identity', 'SOURCES header')
    a.rep('| RECOG | RTG_RELATIONAL_RECOGNITION_DSN | v0.3.23 | `recog-v0.3.23` | canonical Tier 3 |', '| RECOG | RTG_RELATIONAL_RECOGNITION_DSN | v0.3.24 | `recog-v0.3.24` | canonical Tier 3 |', 'RECOG move', 'SOURCES RECOG row')
    a.rep('| GEN | RTG_GENESIS_GEOMETRY_DSN | v2.8.9 | `gen-v2.8.9` | canonical Tier 3 |', '| GEN | RTG_GENESIS_GEOMETRY_DSN | v2.9 | `gen-v2.9` | canonical Tier 3 |', 'GEN move', 'SOURCES GEN row')
    a.rep('*END — RTG STATE ATLAS v0.4. Noncanonical; owner DSNs govern.*', '*END — RTG STATE ATLAS v0.5. Noncanonical; owner DSNs govern.*', 'identity', 'footer')
    a.rep('(owner RECOG = RTG_RELATIONAL_RECOGNITION_DSN v0.3.23;', '(owner RECOG = RTG_RELATIONAL_RECOGNITION_DSN v0.3.24;', 'RECOG move', 'D3 header')
    a.rep('(sources: GEN v2.8.9 primitive/triad/K3/K4/phase parts ·', '(sources: GEN v2.9 primitive/triad/K3/K4/phase parts ·', 'GEN move', 'D4a header')
    a.rep('(owners: GEN = RTG_GENESIS_GEOMETRY_DSN v2.8.9; UVM = RTG_OPEN_M_DSN v0.7.1',
          '(owners: GEN = RTG_GENESIS_GEOMETRY_DSN v2.9 (Methodology v1.4 declared with a bounded migration of inherited [RESULT] blocks, GEN.D17); UVM = RTG_OPEN_M_DSN v0.7.1', 'GEN move', 'D4b header')
    # ---- HEADLINE ----
    a.rep('persists at OFN, GEN §6.3c C2 and G-20, FMS and ER-2B (OFN.O1, F5, DYAD.X1). Fix in OFN, GEN, FMS, ER-2B.',
          'persists at OFN, FMS and ER-2B (OFN.O1, F5, DYAD.X1); GEN v2.9 §6.3c G-20 records the imported C^∞ existence (analytic and physical/network realization kept open). Fix in OFN, FMS, ER-2B.', 'GEN GC-17', 'H1')
    a.rep('RECOG-THM-A1A-PHASE-EXISTENCE-U proves C_D^ext on U without R9 or INF-1 (D3). Remaining interfaces:',
          'RECOG-THM-A1A-PHASE-EXISTENCE-U proves C_D^ext on U without R9 or INF-1, and RECOG v0.3.24 adds on the same U the slip-schedule theorem RECOG-THM-A1B-SLIP-SCHEDULE-U (events = lift crossings; gaps {6,7}; digamma schedule) and the infinite-record readout RECOG-RESULT-A1C-RECORD-PHASE-READOUT (D3; NUMGEN informed, no custody change). Remaining interfaces:', 'RECOG A1b/A1c', 'H5')
    a.line('H6 D-CONV high — sign/normalization splits in GEN interfaces:',
           "H6 D-CONV med — GEN v2.9 settled the face-lift convention (κ_f := |m||w| defined once in §6.8; 9A written sign-explicitly with sgn(m)) and rescoped the sourced-junction theorem (GEN-THM-SOURCED-JUNCTION: at w=0 both branches coincide, two antipodal stationary solutions; the \"valid minimizer\" clause is retracted to Appendix B). Still open on the owner side: the physical ±ΔM_f branch, energy functional and minimizer at w≠0 (GCL-02; no energy functional in the held archive) and B_* undefined (GEN.D6); the nine proof sources carry custody state (a) missing (GEN.D3). GEN c_θ^(6)=−119√3/648 is marked archival reference only in v2.9 (not imported); a phase-moment retest should use RECOG CHART-LAWS/R9 (RECOG.R-L6).", 'GEN v2.9', 'H6')
    a.rep('· GEN face-lift κ (atlas label κ_f) · RRF-CN05 κ ·', '· GEN face-lift κ_f (owner notation, GEN v2.9 §6.8) · RRF-CN05 κ ·', 'GEN F-1', 'H8')
    # ---- D1 ----
    a.rep('GEN face-lift κ (atlas label κ_f), DYAD backbone κ (F1).', 'GEN face-lift κ_f (owner notation, GEN v2.9 §6.8), DYAD backbone κ (F1).', 'GEN F-1', 'RRF.F5')
    a.rep('· GEN face-lift κ (atlas label κ_f) · RRF-CN05 κ (units) ·', '· GEN face-lift κ_f (owner notation, GEN v2.9 §6.8) · RRF-CN05 κ (units) ·', 'GEN F-1', 'D1 kappa line')
    a.rep('owner-side navigation table: Programme v1.3 §8.2 (11 rows)', 'owner-side navigation table: Programme v1.3 §8.2 (11 rows; no κ_f row yet, PROG.G8)', 'PROG κ table', 'D1 kappa line pointer')
    a.after_line('PROG.G6 D-STALE', ["PROG.G8 D-SCOPE (atlas reading of Programme v1.3 §8.2 against GEN v2.9 §6.8 and OFN §11.4 / RRF §6.2a): the κ table has no row for GEN's face-lift κ_f (owner symbol since v2.9), and its first row calls γ≡κ \"an atlas reading, not an owner statement\" although OFN and RRF state it — the latter already recorded by the Programme owner as E-P13-1 (records/programme/ post-release note). Both for the next Programme edition."], 'PROG κ table', 'D1.L5 PROG.G8')
    a.rep('GEN v2.8.9 §6.3c C2 ("existence of such Φ not asserted", G-20) and OFN do not. Fix: OFN, GEN.',
          'GEN v2.9 §6.3c G-20 records the imported C^∞ existence (analytic case Dyadic OPEN 20; physical/network realization open); OFN does not. Fix: OFN.', 'GEN GC-17', 'OFN.O1')
    # ---- D2 ----
    a.rep('is exactly GEN §6.3c instance C2\'s hypothesis, recorded there as "existence not asserted"; C2 is non-vacuous in C^∞. GEN v2.8.9 §6.3c and OFN v0.10 §5.5.4 do not record it;',
          'is exactly GEN §6.3c instance C2\'s hypothesis; C2 is non-vacuous in C^∞. GEN v2.9 §6.3c records it (G-20 existence note; scoped DYAD v6.4.22 import of this RID and DYAD-THM-SMOOTH-EMBEDDING); OFN v0.10 §5.5.4 does not;', 'GEN GC-17', 'DYAD.X1')
    # ---- D3 RECOG ----
    a.rep('meeting the hypothesis of GEN v2.8.9 §6.3c instance C2 (Φ(0)=0, DΦ(0)=I, ΦTΦ⁻¹ commuting with A); whether GEN C2 or OFN class C uses it is their owners\' decision;',
          'meeting the hypothesis of GEN §6.3c instance C2 (Φ(0)=0, DΦ(0)=I, ΦTΦ⁻¹ commuting with A); GEN v2.9 imports it for the G-20 existence note (scoped, C^∞ local germs); whether OFN class C uses it is OFN\'s decision;', 'GEN GC-17', 'D2 SMOOTH-EQUIVARIANT-CHART node')
    a.rep('(4√3/3)²=16/3 = GEN v2.8.9 §6.3 leading', '(4√3/3)²=16/3 = GEN §6.3 leading', 'GEN move', 'D2 BRIDGE-EXPORT-CONTRACT node')
    a.rep('@RECOG v0.3.23 §6.13b', '@RECOG §6.13b', 'RECOG move', 'D3 A1a node locator')
    a.after_line('*RECOG:discriminant ALG |', [
        "RECOG-ALG-QUADRATURE-TYPING ALG | sc: postulated T; dyad observables (ρ,η) of the lifted primitive chart; v0.3.24 | 𝒬={Re Ĉ_pole=0}={cosη=0} (swap-invariant as a set; branches η=±π/2 exchanged): (1) primitive-chart typing — on 𝒬 J=[[1,0],[e^ρ,1]], nontrivial unipotent shear with 1-eigenspace ∂_η; (2) comparator-geometric content — ρ(Tx)−ρ(x)=−Im Ĉ_pole(x), so |Δρ|≤1 with equality exactly on 𝒬 (extremal one-step radial transfer); ∂_η[ρ∘T−ρ]=−Re Ĉ_pole, zero exactly on 𝒬; relative to the multiplicative Haar form Ω=dρ∧dη on the RRF wrapped native ratio ζ=e^{ρ+iη} (S*Ω=Ω; derived, model-intrinsic, transported with chart changes, not an RRF-registered observable, no OPEN-A bearing) 𝒬 is the Ω-area-neutral locus | ¬ chart-invariant type (explicit charts change it); ¬ periodic-orbit multiplier signature forced | answers R4 sub-item 1 in reframed form (R4 stays ACTIVE) | cert RECOG-ART-A3-QUADRATURE-TYPING (exact sympy gates Q1–Q5, controls NC1–NC2) | @§6.5",
        "RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY ALG | sc: postulated T; wrapped cylinder; v0.3.24 | on Σ={Ĉ_pole=±1}={sinη=0} (S-invariant as a set) ρ is preserved and η↦η+e^ρ−1, so the wrapped-periodic orbits inside Σ are exactly e^ρ−1=mπ, m∈ℤ_{≥0}: m=0 → P₁,P₂; m=2k → the winding fixed points ((tr,det)=(1,1+2πk) at η=0, (3,1−2πk) at η=π); m odd → period-2 orbits (ln(1+mπ),0)↔(ln(1+mπ),π) alternating Ĉ_pole=+1/−1, M₂=J_{(ρ_m,π)}J_{(ρ_m,0)}, (t₂,d₂)=(1,1−m²π²), hyperbolic (Δ=4m²π²−3>0), orientation-reversing; periodic for the wrapped map only (lift advances 2mπ); none in the zero-winding local sector; Σ∩𝒬=∅ | complete inside Σ; ¬ completeness outside Σ (R4 inventory: NUM sampled list only) | cert RECOG-ART-A3-QUADRATURE-TYPING gate Q6 (symbolic m,k) | @§6.3"], 'RECOG A3', 'D3 A3 nodes')
    a.after_line('*RECOG:A1a-scope DEF |', [
        "RECOG-THM-A1B-SLIP-SCHEDULE-U THM | sc: postulated T; x₀∈U={0<Q₀≤1/625}; lifted primitive chart, frame W=ρ+ωη, increasing lift φ̂ with principal one-step increments δ_T; token conventions §6.16a (F2(b)); block count M, a=Q₀⁻¹; v0.3.24 | (A) events are lift crossings: x_n→x_{n+1} is a canonical B-event iff ⌊φ̂_{n+1}/2π⌋=⌊φ̂_n/2π⌋+1 · (C′) six-step deficit: ∀y∈U_T, Δ(y):=2π−Λ₆(y) satisfies Δ>0.927τQ(y)>0 and |Δ−τQ|<1.82Q^{3/2} · (B) alphabet: every gap is 6 or 7; s(M)=(3τ/π)log M+O(1)→∞ sevens among the first 6M steps · (S) schedule: τψ(a+M_k)−(k−1)π/3=L+ε_k, L(x₀)=(π/3)n₀−2πℓ₀+Ψ_{W,∞}(x₀), |ε_k|≤τQ+1.82Q^{3/2}+5arcsin(0.705√Q+0.257Q)+τ|S^tail_{M_k}|+|R^tail_{M_k}|=O((a+M_k)^{−1/2}), Q the largest primitive amplitude among the points of the k-th slip block, S^tail/R^tail the tails of the A1a series (a-priori quantities, not record data); hence τlog M_k−(k−1)π/3→L and M_{k+1}/M_k→e^{π/(3τ)} (no computable finite-record decoder guarantee follows from this ceiling) | <RECOG-THM-A1A-PHASE-EXISTENCE-U (Ψ_{W,∞}, series tails), RECOG-THM-A1A-PHASE-EXISTENCE-ALT, RECOG-THM-A1A-LIFT-ALIGNMENT, RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, DYAD-THM-C21 (cubic coefficient of the deficit, reproduced exactly), DYAD-THM-PRIM-CTR, DYAD-THM-NF-REM (ingredients only), DYAD-THM-LPHASE-ROWA-REMAINDER | ¬ anything outside U; ¬ ε_k computable from (a,k,M_k) alone (tails and block maximum are a-priori quantities); ¬ decoding of a from a finite record; ¬ statements about M_W, M(z₀) or an event mechanism; ¬ Dyadic domain widened; GAP-LOCK/INF-1 remain NUMGEN's (NUMGEN informed, no custody change) | cert RECOG-ART-A1B-SIXSTEP-DEFICIT (exact six-step jet in ℚ(i√3); NUM illustration separate) | >RECOG-RESULT-A1C-RECORD-PHASE-READOUT | @§6.13b",
        "RECOG-RESULT-A1C-RECORD-PHASE-READOUT RES[from THM] | sc: x₀∈U; the complete infinite token record ℛ(x₀)=(n₀;g₁g₂…) in F2(b) conventions; v0.3.24 | the record determines L(x₀)=lim_k[τlog M_k−(k−1)π/3] and hence Ψ_{W,∞}=Ψ_{z,∞} mod 2π, with no state datum and without the value of a | ¬ reconstruction of a, M_W or M(z₀) from L (statement about the method, not a non-recoverability theorem); finite prefix with a known: window of width 2|ε_k| (a-priori envelope, →0), with a unknown no window (NUM least-squares (â,L̂) ≤3.5% on illustration runs, no guarantee); ¬ R_ind downgrade of R9's carrier M (retrospective reconstruction is not write-through, SG-R6); ¬ carrier downgrade | <RECOG-THM-A1B-SLIP-SCHEDULE-U | >R6 sub-items A1c-Q1′ (injectivity of x₀↦ℛ(x₀) on U, open), A1c-decoder | @§6.16e"], 'RECOG A1b/A1c', 'D3 A1b/A1c nodes')
    a.line('RECOG-OPEN-TYPE-CHANGE (R4) ACTIVE |', 'RECOG-OPEN-TYPE-CHANGE (R4) ACTIVE | sub-item 1 answered in reframed form (v0.3.24): the chart-free content of cosη=0 is comparator-geometric (extremal radial transfer; Ω-area-neutral locus relative to the declared Haar form), the one-step type is not chart-invariant, no periodic-orbit multiplier signature is forced (RECOG-ALG-QUADRATURE-TYPING) · global periodic-orbit inventory beyond P₁,P₂: complete inside the pole stratum Σ={Ĉ_pole=±1} (RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY: e^ρ−1=mπ; new odd-m period-2 family), outside Σ a NUM sampled list only; none in the small punctured P₁ sector', 'RECOG A3', 'D3 R4')
    a.rep('HYPs: memory-version event reading, RECOG-OPEN-INTERSECTION', 'HYPs: memory-version event reading, RECOG-OPEN-INTERSECTION · OPEN sub-items (v0.3.24): A1c-Q1′ — is x₀↦ℛ(x₀) (start state → complete token record) injective on U? neither answer established (the cell\'s local-nonconstancy argument is SESSION, conjectural); A1c-decoder — finite-prefix window for (a,L) with a unknown, and a record-only majorant for the known-a window via Q_m≤Q₀/(1+½Q₀m) and the A1a tail estimates', 'RECOG A1c', 'D3 R6')
    a.rep('RECOG-THM-A1A-PHASE-EXISTENCE-U at explicit U with its nonclaims;', 'RECOG-THM-A1A-PHASE-EXISTENCE-U, RECOG-THM-A1B-SLIP-SCHEDULE-U and RECOG-RESULT-A1C-RECORD-PHASE-READOUT at explicit U with their nonclaims (no decoding of a, no event mechanism, no R_ind downgrade); RECOG-ALG-QUADRATURE-TYPING and RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY at their scopes;', 'RECOG v0.3.24', 'D3 export protocol')
    a.drop_line('RECOG.R-P3 D-SCOPE |', 'RECOG MNT', 'RECOG.R-P3 retired')
    a.drop_line('RECOG.R-T1 D-SCOPE |', 'RECOG MNT', 'RECOG.R-T1 retired')
    a.rep('The reciprocal-amplitude and explicit-U existence theorems have in-ledger written proofs.', 'The reciprocal-amplitude and explicit-U existence theorems have in-ledger written proofs; the v0.3.24 artifacts RECOG-ART-A1B-SIXSTEP-DEFICIT and RECOG-ART-A3-QUADRATURE-TYPING are in evidence/recog/ with hashes (naming checked, not rerun here).', 'RECOG v0.3.24', 'RECOG.R-D1')
    # ---- D4a ----
    a.rep('Plus face-lift κ (atlas label κ_f), κ_RTG.', 'Plus face-lift κ_f (owner notation since GEN v2.9), κ_RTG.', 'GEN F-1', 'F1')
    a.rep('vs GEN face-lift κ=|m||w| (D4b; atlas label κ_f) vs κ_RTG (D4b).', 'vs GEN face-lift κ_f=|m||w| (D4b; GEN v2.9 §6.8) vs κ_RTG (D4b).', 'GEN F-1', 'D4a kappa line')
    a.rep('Also makes GEN transported instance C2 non-vacuous in C^∞ (GEN.D15).', 'Also makes GEN transported instance C2 non-vacuous in C^∞ — recorded by GEN v2.9 §6.3c (G-20 existence note).', 'GEN GC-17', 'F5')
    a.drop_line('F9 D-LINK (GEN.D10', 'GEN GB-13', 'F9 retired')
    a.drop_line('F10 D-SCOPE (TRIAD.T6):', 'GEN GB-14', 'F10 retired')
    a.rep('and GEN PURE-CHIRAL, PHI-2TO3, G2-CHRONO, P4-PRIMITIVE, PHASE-AVG, PHASE-CLOSURE ("proof-source reference required"; load-bearing: P4 feeds the cascade chain; QH-NOGO, FACE-LIFT, SOURCED-JUNCTION → D4b);',
          'and GEN PURE-CHIRAL, PHI-2TO3, G2-CHRONO, P4-PRIMITIVE, PHASE-AVG, PHASE-CLOSURE (GEN v2.9 §8 custody state (a) missing, clause key [custody-A], EV-NOT-RERUN; held by neither Genesis co-owner session and not among the records placed at upload/gen-records/; load-bearing: P4 feeds the cascade chain; QH-NOGO, FACE-LIFT, SOURCED-JUNCTION → D4b);', 'GEN GB-11', 'F14')
    a.drop_line('F15 D-LINK (GEN.D13):', 'GEN GA-08', 'F15 retired')
    a.drop_line('F16 D-PIN (GEN.D9):', 'GEN GB-12', 'F16 retired')
    a.drop_line('F17 ! D-CONV wording (GEN.D16):', 'GEN GA-09', 'F17 retired')
    a.drop_line('F19 D-RID (GEN.D11):', 'GEN GA-06', 'F19 retired')
    a.line('F20 D-STALE (GEN.D12, TRIAD.T9):', 'F20 D-STALE (TRIAD.T9): TRIAD §1 says CN-01–CN-05 "consumer acceptance pending" while §7.4 records dispositions.', 'GEN GA-07', 'F20 narrowed')
    a.rep('¬ physical model/carrier/closure/γ (incl. class C), ¬ existence of exactly transported realization, ¬ formal series,',
          '¬ physical model/carrier/closure/γ (incl. class C), ¬ existence of an analytic exactly transported realization or any physical/network-level realization (the C^∞ mathematical existence is imported: DYAD-THM-SMOOTH-EQUIVARIANT-CHART, GEN v2.9 §6.3c G-20 note, scoped DYAD v6.4.22 import), ¬ formal series,', 'GEN GC-17', 'D4a TRANSPORTED node')
    # ---- D4b ----
    a.rep('≡ GEN-THM-DELTA-QC standalone at I_sc=0 (L5 F9) | @GEN§2', '≡ GEN-THM-DELTA-QC standalone at I_sc=0 (GEN v2.9 §2 specialization line, under the RTG canonical B-metric convention for ω_sc; not a UV energy statement) | @GEN§2', 'GEN GB-13', 'D4a GSPLIT node')
    a.rep('— shear/vec case only, L5 F10) | @§6.17', '— shear policy, vector-seed reading; GEN v2.9 §8 labels the case and cites the four-case maximum √14/16) | @§6.17', 'GEN GB-14', 'D4a T6U node')
    a.rep('cascade ⇔ ⟨𝒫₄⟩>0 | ! L5 F15 | @§6.6', 'cascade ⇔ ⟨𝒫₄⟩>0 | GEN v2.9: coarse closure ansatz, not a basis of the 13-moment space (no map asserted) | @§6.6', 'GEN GA-08', 'D4a moment-closure node')
    a.rep('c_θ^(6)=−119√3/648 [Lie strict-kernel] ! L5 F16', 'c_θ^(6)=−119√3/648 [Lie strict-kernel; GEN v2.9 §6.2: archival reference only, not imported, not a chart or phase-moment input]', 'GEN GB-12', 'D4a c_theta node')
    a.rep('| ¬ passive representation change explains it (Candidate B deferred) | ! L5 F17 | @§1,§6.5', '| ¬ passive representation change explains it (Candidate B deferred); different objects in different declared constructions, no verified passive conjugacy (GEN v2.9 wording) | @§1,§6.5', 'GEN GA-09', 'D4a sign-split node')
    a.rep('*GEN:moment-closure (6 moments) (D4a; no map between them, GEN.D13)', '*GEN:moment-closure (6 moments) (D4a; GEN v2.9 §6.6: the six are a coarse closure ansatz, not a basis of the 13-moment space, no map asserted)', 'GEN GA-08', 'index phase moments')
    a.rep('exact scalar susceptibility derived | >SG-13 | ! GEN.D4 | @GEN§6.9', 'exact scalar susceptibility derived; projection nontriviality: generic under the scalar-M ansatz (off the residue zero set), OPEN beyond it (GEN v2.9 scope words) | >SG-13 | @GEN§6.9', 'GEN GA-04', 'D4b 9-downgrades node')
    a.rep('| ≡ UVM-9C | ! GEN.D14 | @GEN§2,§6.9', '| ≡ UVM-9C | @GEN§2,§6.9', 'GEN GA-05', 'D4b MSPIN2-ANISO node')
    a.rep('sub-step 3 (projection nontriviality) closed only under scalar-M (GEN.D4)', 'sub-step 3 (projection nontriviality) closed only under the scalar-M ansatz, OPEN beyond it (scope words GEN v2.9)', 'GEN GA-04', 'D4b OPEN-GEN-II-9 frontier')
    a.line('FACE-LIFT GEN-ART-FACE-LIFT ALG |', 'FACE-LIFT GEN-ART-FACE-LIFT ALG | ΔM_f(w)=m N(w), N(w)=[[Im w,−Re w],[−Re w,−Im w]], m=2Q_sB_*, (ΔM_f)²=κ_f²I, κ_f:=|m||w|≥0 (GEN v2.9 §6.8 DEF: face-lift magnitude, distinct from the birth κ of §6.1, κ_phys, κ_RTG and the γ of §6.3b–c); for w≠0 N̂=N/|w|, ΔM_f=sgn(m)κ_f N̂; a(φ)=r_φᵀΔM_f r_φ=m(Im w cos2φ−Re w sin2φ), |a|≤κ_f | proof source [custody-A] (GEN.D3); algebra re-derived independently [indep-AC] gates K1, S3 | B_* undefined and its sign unknown — owner declaration (GEN.D6) | ≡ UVM-R2 2θ law | @GEN§6.8', 'GEN F-1/GA-02/GA-03', 'D4b FACE-LIFT')
    a.rep('κ (birth coefficient vs face-lift κ=|m||w| (GEN §6.8; atlas label κ_f) vs scalar-M κ=m|w| (GEN §6.9; sign: GEN.D2) vs κ_RTG=𝒢_e/J_e',
          'κ (birth coefficient vs face-lift κ_f=|m||w| (GEN v2.9 §6.8; 9A uses sgn(m)κ_f) vs κ_RTG=𝒢_e/J_e', 'GEN F-1/GA-02', 'D4b kappa line')
    a.line('*GEN:QH-nogo THM |', 'GEN-THM-QH-NOGO THM | T_ℍ=T⊕T ⇒ w=0: a block-diagonal quaternionic extension gives no smooth 3D metric branch | RID assigned v2.9 (statement unchanged); art GEN-ART-QH-NOGO [custody-A] | ≡ UVM-BLOCK-DIAG (imported at "RID unavailable"; OPEN M has not repinned to the RID, OPENM.U3) | >SG-7 | @GEN§6.7', 'GEN GB-10', 'D4b QH-NOGO')
    a.line('*GEN:metric-criterion THM |', 'GEN-THM-SINGLE-FACE-METRIC THM | Q_s>0, β≠0, Δ₃>0, σ_f≠0, w≠0 ⇒ det Γ_ℍ=β²Δ₃Q_s³>0 | RID assigned v2.9 (statement unchanged); proof source not identified in the owner text | @GEN§1,§6.9', 'GEN GB-10', 'D4b METRIC')
    a.line('*GEN:sourced-junction THM |', 'GEN-THM-SOURCED-JUNCTION THM | w=0, σ_f≠0, Δ₃>0: vacuum gluing fails (S_f=0 is impossible); since ΔM_f(0)=0 the two §6.8 branches coincide, K±=τI, and the constrained birth equation τd⊥+S_f=0 on |d⊥|²=Δ₃ has exactly the two antipodal solutions d⊥=∓√Δ₃ S_f/|S_f|, τ=±|S_f|/√Δ₃ (none at Δ₃=0); which is the physical birth needs the birth energy and its constrained second variation — OPEN (GCL-02); the foam branch is sourced birth | RET (GEN Appendix B, v2.9): "has a valid minimizer" | proof of the algebraic statement [indep-AC] gates S1–S2; original source GEN-ART-SOURCED-JUNCTION [custody-A] | export carries the same scope (GEN §7); OPEN M-foam downstream | @GEN§1,§6.9', 'GEN GA-01', 'D4b SOURCED-JUNCTION')
    a.rep('(κ_f: atlas label for the face-lift κ=|m||w|, GEN writes κ)', '(κ_f=|m||w|, GEN v2.9 §6.8)', 'GEN F-1', 'D4b secular-K−')
    a.line('GEN-ALG-SCALARM-RESOLVENT ALG |', 'GEN-ALG-SCALARM-RESOLVENT ALG | sc: M=gI | ((τ−g)I−ΔM_f)⁻¹=((τ−g)I+ΔM_f)/((τ−g)²−κ_f²); poles at τ−g=±κ_f; physical branch is OPEN-GEN-II-9 | @GEN§1,§6.9', 'GEN F-1', 'D4b SCALARM-RESOLVENT')
    a.line('GEN-THM-SCALARM-EIGEN THM |', 'GEN-THM-SCALARM-EIGEN THM | sc: M=gI; m≠0, w≠0 | λ±=(τ−g)∓sgn(m)κ_f, κ_f=|m||w|; L_sc⁻¹=Π₊/(τ−g−sgn(m)κ_f)+Π₋/(τ−g+sgn(m)κ_f), Π±=½(I±N̂) independent of m; v₊=(μ1,μ2−|w|) spans range Π₊ for either sign of m; the pole at τ−g=+κ_f carries Π₊ if m>0 and Π₋ if m<0 (v2.9 sign-explicit form); limiting-path definition of the physical soft branch OPEN (OPEN-GEN-II-9); v₊·v₋=0 but v₊ᵀBv₋=−μ1μ2≠0; R^(E)₊=(v₊·H₀)²/|v₊|²≥0 and R^(B)₊=H₀ᵀBΠ₊H₀ sign-indefinite (discriminant +1/20), both independent of sgn m; RES: at H₀=J_Qs* both generically ≠0, so the soft pole is excited | both signs checked [indep-AC] gates K2–K4 | @GEN§6.9 (9A)', 'GEN GA-02', 'D4b SCALARM-EIGEN')
    a.rep('exports: allowed from this domain — QH no-go, metric criterion, sourced junction (with hypotheses), the word-sector dichotomy (category-scoped).',
          'exports: allowed from this domain — GEN-THM-QH-NOGO, GEN-THM-SINGLE-FACE-METRIC, GEN-THM-SOURCED-JUNCTION (algebraic statement at w=0, Δ₃>0; physical branch selection OPEN), the word-sector dichotomy (category-scoped); GEN v2.9 §7 lists its consumers (TRIAD IF06, UVM IF08, RECOG IF15, RRF IF30, OFN IF32, nc records IF33–35) with their declared pins, not repinned.', 'GEN GC-18/19', 'D4b exports')
    # D4b.L5
    a.drop_line('GEN.D1 ! D-CONV:', 'GEN GA-01', 'GEN.D1 retired')
    a.drop_line('GEN.D2 ! D-CONV:', 'GEN GA-02', 'GEN.D2 retired')
    a.line('GEN.D3 D-PROOF (b)', 'GEN.D3 D-PROOF (b) (D4b part; the rest is in D4a F14): proof sources of QH-NOGO, FACE-LIFT, SOURCED-JUNCTION, PHASE-AVG (uniform-phase sink), PHASE-CLOSURE (moment closure) carry the owner custody state (a) missing since GEN v2.9 (clause [custody-A], EV-NOT-RERUN; not held by either Genesis co-owner session, not in upload/gen-records/); independent re-derivations ([indep-AC]: face-lift algebra, sourced-junction algebraic statement) are not recoveries. The full list of nine is shared with D4a (PURE-CHIRAL, PHI-2TO3, G2-CHRONO, P4-PRIMITIVE).', 'GEN GB-11', 'GEN.D3')
    a.drop_line('GEN.D4 ! D-SCOPE:', 'GEN GA-04', 'GEN.D4 retired')
    a.line('GEN.D5 D-SYM (D4b part):', 'GEN.D5 D-SYM (D4b part): c₀ vs c₀^UV; κ (birth κ vs κ_f vs κ_RTG — κ_f owner notation since v2.9, one collision fewer); χ; β; μ1, μ2 vs μ, μ6; m; w vs w_e; D vs 𝒟 vs apex D; p. Full GEN list shared with D4a.', 'GEN F-1', 'GEN.D5')
    a.line('GEN.D6 D-SYM:', 'GEN.D6 D-SYM (owner-declared): B_* (in m=2Q_sB_*) is declared undefined with unknown sign in GEN v2.9 §6.8; every sgn(m)-dependent statement carries the dependence explicitly; its source in editions ≤ v2.8.5 is not held. OPEN M reuses m=2Q_sB_* in R2; UVM would be notified (GEN v2.9 release record).', 'GEN GA-03', 'GEN.D6')
    a.line('GEN.D7 D-RID (D4b part):', 'GEN.D7 D-RID (D4b part, narrowed v2.9): the exported theorems carry RIDs since v2.9 (GEN-THM-QH-NOGO, GEN-THM-SINGLE-FACE-METRIC, GEN-THM-SOURCED-JUNCTION); still RID-less: birth symmetry here, pure chiral protection and tetrahedral chronological protection in D4a (second priority, deferred by the owner). OPEN M still imports at "RID unavailable" until its repin (OPENM.U3).', 'GEN GB-10', 'GEN.D7')
    a.drop_line('(GEN.D11, GEN.D12, GEN.D13: see D4a.L5 F19, F20, F15)', 'GEN retirements', 'D4b cross-pointer')
    a.line('GEN.D14 D-SCOPE:', 'GEN.D17 D-GRADE (owner-declared): GEN v2.9 declares Methodology v1.4 with a bounded migration — 29 inherited [RESULT] blocks carry no [from: TAG] companion (v1.4 §3.4), counted in the release record (gate C16); pairing is retagging work for a later edition. Not a defect in any claim; readers should not take the header as full v1.4 retagging.', 'GEN V1', 'GEN.D14 → GEN.D17')

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
    lines = text.split('\n'); rows = l5_rows(lines); out, dangling = [], []
    for h in [l for l in lines if re.match(r'^H\d+ ', l)]:
        hid = h.split()[0]; keys = sorted(set(KEY.findall(h))); miss = [k for k in keys if k not in rows]
        dangling += [f'{hid}:{k}' for k in miss]; out.append(dict(h=hid, l5_keys=keys, missing=miss))
    cited = {k for r in out for k in r['l5_keys']}
    high = [k for k, i in rows.items() if re.search(r'\bhigh\b', lines[i-1][:120]) and k not in cited]
    return dict(rows=out, dangling=dangling, high_l5_without_h=high, l5_rows=len(rows))

def unlabelled_kf_atlas_label(text):
    """v0.5: κ_f is owner notation; the phrase 'atlas label κ_f' must no longer occur."""
    return [l[:80] for l in text.split('\n') if 'atlas label κ_f' in l or 'labels this face-lift κ as κ_f' in l]

def stale_editions(text):
    return [l[:80] for l in text.split('\n') if re.search(r'GEN v2\.8\.9 §|`gen-v2\.8\.9`|RECOG v0\.3\.23 §|`recog-v0\.3\.23`|\| v2\.8\.9 \| `gen|\| v0\.3\.23 \| `recog', l)]

def checker():
    spec = importlib.util.spec_from_file_location('atlas_checker', ROOT / 'tools/atlas_check.py')
    c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c); return c

def main():
    base = at('atlas-v0.4', ATLAS).decode(); assert sha(base) == BASE_SHA
    a = Edit(base); refresh(a); text = a.text
    assert not unlabelled_kf_atlas_label(text), unlabelled_kf_atlas_label(text)
    assert not stale_editions(text), stale_editions(text)
    # ---- manifest ----
    old = json.loads(at('atlas-v0.4', 'evidence/atlas/v0.4/source_manifest.json'))
    m = json.loads(json.dumps(old))
    m.update(atlas='v0.5', frozen_at='2026-10-25', repository_snapshot=SNAPSHOT, previous_atlas_tag='atlas-v0.4', method_tag='atlas-v0.2', method_edition='v0.2')
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_4_edition'] = prev['edition']; s['v0_4_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] in MOVED:
            mv = MOVED[s['key']]; data = at(mv['tag'], s['path'])
            s.update(edition=mv['edition'], tag=mv['tag'], commit=git('rev-parse', mv['tag'] + '^{commit}').decode().strip(), sha256=sha(data), authority=mv['authority'])
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(SNAPSHOT, s['path']), ('snapshot/tag divergence', s['key'])
        s['v0_4_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_4_input_equality'] for x in m['sources']) == {'EQUAL': 16, 'CHANGED': 2}
    wjson(OUT / 'source_manifest.json', m)
    # ---- H -> L5 ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys ----
    oldret = json.loads(at('atlas-v0.4', 'evidence/atlas/v0.4/retired_l5_keys.json'))
    newret = {'GEN.D1': 'GEN v2.9 GEN-THM-SOURCED-JUNCTION: w=0 ⇒ K₊=K₋; minimizer clause retracted (GA-01); physical branch OPEN is the owner\'s GCL-02, not an inconsistency.',
              'GEN.D2': 'GEN v2.9 §6.8/§6.9: κ_f defined once, 9A sign-explicit (GA-02).',
              'GEN.D4': 'GEN v2.9: scope words at OPEN-GEN-II-9 item 3, SG-13, §6.9 (GA-04).',
              'GEN.D14': 'GEN v2.9: raw-array premise named at the dependency line (GA-05); key reused for nothing — GEN.D17 is new.',
              'F9': 'GEN v2.9 §2: specialization line GEN-THM-DELTA-QC → GSPLIT with the convention caveat (GB-13).',
              'F10': 'GEN v2.9 §8 GEN-CAND-APEX-T6U labels the shear/vector-seed case and cites the Triadic §6.17 four-case maximum (GB-14).',
              'F15': 'GEN v2.9 §6.6: six-member set declared a coarse closure ansatz, not a basis of the 13-moment space (GA-08).',
              'F16': 'GEN v2.9 §6.2: c_θ⁽⁶⁾ marked archival reference only, not imported; chart value pointer (GB-12).',
              'F17': 'GEN v2.9 §1/§6.5: "different objects, not a verified passive conjugacy" (GA-09).',
              'F19': 'GEN v2.9 §2: one GEN-OPEN-WPHASE record; second heading is a pointer (GA-06).',
              'RECOG.R-P3': 'RECOG v0.3.24 MNT: §7.1/§7.2 audit tables carry current status at the point of use; history pointed to at recog-v0.3.23.',
              'RECOG.R-T1': 'RECOG v0.3.24 MNT: R8/R9 specifications, former R11 sub-items and the R7 heading resolved to current state; history at recog-v0.3.23.'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret if '.' in k]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.5 reasons in dispositions.json.'))
    # ---- shared checker ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at('atlas-v0.2', 'evidence/atlas/coverage_map_v0_2.json'))
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.5/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    # ---- new-node RID presence in the moved sources (naming check, not certificate replay) ----
    new_rids = ['RECOG-THM-A1B-SLIP-SCHEDULE-U', 'RECOG-RESULT-A1C-RECORD-PHASE-READOUT', 'RECOG-ALG-QUADRATURE-TYPING', 'RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY',
                'RECOG-ART-A1B-SIXSTEP-DEFICIT', 'RECOG-ART-A3-QUADRATURE-TYPING', 'GEN-THM-QH-NOGO', 'GEN-THM-SINGLE-FACE-METRIC', 'GEN-THM-SOURCED-JUNCTION']
    presence = {r: (('RID: ' + r) in (src['RECOG'] if r.startswith('RECOG') else src['GEN'])) for r in new_rids}
    assert all(presence.values()), presence
    # ---- dispositions ----
    def row(t, key): return next((l for l in t.split('\n') if l.startswith(key + ' ')), None)
    touched = ['GEN.D1', 'GEN.D2', 'GEN.D3', 'GEN.D4', 'GEN.D5', 'GEN.D6', 'GEN.D7', 'GEN.D14', 'F1', 'F5', 'F9', 'F10', 'F14', 'F15', 'F16', 'F17', 'F19', 'F20', 'OFN.O1', 'DYAD.X1', 'RECOG.R-P3', 'RECOG.R-T1', 'RECOG.R-D1']
    disp = []
    for key in touched:
        o, n = row(base, key), row(text, key)
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded')
        disp.append(dict(key=key, disposition=state, reason=newret.get(key, 'reworded; see edit_log.json'), previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    for key in ['PROG.G8', 'GEN.D17']:
        disp.append(dict(key=key, disposition='new', reason='see edit_log.json', previous_sha256=None, current_sha256=sha(row(text, key))))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    t = text.replace('(GEN.D6); the nine', '(GEN.D1); the nine', 1); ctl('U1', 'H cites a retired/nonexistent L5 row', 'H6:GEN.D1' in h_l5_map(t)['dangling'])
    t = text + 'GEN.D2 ! D-CONV: reused\n'; ctl('U2', 'retired key reused', bool(c.run(t, m, src, cmap, idmap, retired, with_sources=False).fails()))
    t = text.replace('| v2.9 | `gen-v2.9` |', '| v2.8.9 | `gen-v2.8.9` |', 1); ctl('U3', 'SOURCES row older than manifest', bool(c.run(t, m, src, cmap, idmap, retired).fails()) or bool(stale_editions(t)))
    t = text.replace('κ_f (owner notation, GEN v2.9 §6.8) · RRF-CN05 κ ·', 'κ (atlas label κ_f) · RRF-CN05 κ ·', 1); ctl('U4', 'atlas-label wording reintroduced', bool(unlabelled_kf_atlas_label(t)))
    t = text.replace('RECOG-THM-A1B-SLIP-SCHEDULE-U THM |', 'RECOG-THM-A1B-SLIP-SCHEDULE-X THM |', 1); ctl('U5', 'new node RID misspelled against the source', bool(c.run(t, m, src, cmap, idmap, retired, with_sources=False).fails()) or ('RID: RECOG-THM-A1B-SLIP-SCHEDULE-X' not in src['RECOG']))
    t = text.replace('GEN v2.9 §6.3c G-20 records the imported C^∞ existence', 'GEN v2.8.9 §6.3c G-20 records the imported C^∞ existence', 1); ctl('U6', 'stale edition reference reintroduced', bool(stale_editions(t)))
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), controls
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas='atlas-v0.4', base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()), atlas_lines=text.count('\n') + 1,
                   source_snapshot=SNAPSHOT, changed_sources=list(MOVED), edit_operations=len(a.log), retired_keys=list(newret), new_keys=['PROG.G8', 'GEN.D17'],
                   new_nodes=new_rids[:4] + ['GEN-THM-QH-NOGO', 'GEN-THM-SINGLE-FACE-METRIC', 'GEN-THM-SOURCED-JUNCTION'], dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_controls=len(shared), focused_controls=len(controls),
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_5.py': sha(Path(__file__).read_bytes())},
                   limitations=['Structural checks only; no owner certificate rerun; new-node RIDs checked for presence in the tagged sources, not re-proved.',
                                'Impact refresh of two moved sources (GEN v2.9, RECOG v0.3.24); the other 16 domains were not re-extracted; Dyadic records (OPEN 20 LH2012 assessments) change no owner edition.',
                                'RECOG v0.3.24 §6.13b/§6.16e/§6.3/§6.5 extracted at statement level from the tagged file; proofs live in the owner cells.'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
