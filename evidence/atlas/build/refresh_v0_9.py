#!/usr/bin/env python3
"""Atlas v0.8 -> v0.9 candidate: impact refresh for three moved sources — Dyadic v6.4.23 (`dyad-v6.4.23`, adopted
30 Oct 2026), Ontological Foundations v0.12 (`ofn-v0.12`, adopted 30 Oct 2026) and Triadic v1.7 (`triad-v1.7`,
adopted 3 Nov 2026). Change-focused; no general compaction, no Methodology migration of the atlas itself.

DYAD (D2, H5, D3 RECOG nodes): source row and D2 header; new nodes DYAD-THM-OPEN18-STEP-MONOTONE (historical
DYAD-THM-OPEN18 kept with its scope note), DYAD-THM-NF-REM-C7-SHARP, DYAD-THM-LPHASE-ROWA-BRIDGE; NF-REM bracket values
and the L-PHASE proof-outline decimals carry the v6.4.23 [COR] (outward values; 403/250 unchanged); NUMGEN q* witness
typed as a different number from q_{3/4}; RECOG.R-A1 records the registrations and RECOG's pending re-check. Retired:
NUMGEN.N-Q* (answered: the two roots differ).
OFN (D1): source row and D1 header counts (5 local RESULT RIDs, 44 OFN RIDs); new node RTG-OFN-ALG-REF-CLOSURE-COMPARISON;
the class-C causal-interface identity (recorded, no RID); REF-CLOSURE narrowed to its physical reading; the 3A pointer;
the 3B evaluation frame (no standard selected); the TRIAD-CLASS isolation frame (I-comp / I-quiet / I-remove, none
selected).
TRIAD (D4a, D1.L5): source row and D4a header; model line with the two root-equivalent off-root extensions and the
coefficient-ODE clock; T-6e Gram relation typed as the degree-3 first variation; tangency node with f_s, f_c per
extension and the D remark; the coercive bound of T-6l; the held 𝒫₄ pin at the T-6u node; the 96:1 metric caveat;
the export node points at the §7.4 consumer matrix; the frontier carries the T-6r contract C1–C6 and the T-6q
coordinate sign table. L5: F11, F13, F14 reworded; F20 (+ TRIAD.T9) retired; new F30 (Genesis questions), F31
(GEN [CAND] imports), F32 (owner-recorded form debt), PROG.G9 (Programme interface rows at v1.6, no CN-05 record).
Pipes: N-I1 states after the atlas sets its three inbox items (row-check closed; two notices dispositioned).
Rev. 2 (3 Nov 2026; receiving review records/atlas/ATLAS_V0_9_CHATGPT_RECEIVING_REVIEW.md, PR #149, ACCEPT SCOPED, notes
A09-N1/N2; PI: second round): F32 narrowed to the A-1 wording (form/process debt stays in the TRIAD release record);
PROG.G9 typed D-LINK (consumer refresh, not a defect by age); N-I1 states its counts at the source snapshot. Final-review
sweep: the DYAD-DEF-BRIDGE-EXPORT-CONTRACT consumer edge names TRIAD v1.7 §7.1 (v6.4.23 repin) and GEN v2.9 §7 (v6.4.13 pin);
three stale 'GEN v2.8.9' pointers in AZ.A2 (D2, D5) and the Legacy L5 row name GEN v2.9.
Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_9.py
"""
from __future__ import annotations
import hashlib, importlib.util, json, re, subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.9'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = 'f20f080'   # origin/main after PR #145 (TRIAD v1.7 post-tag records and notices); resolved in main()
BASE_TAG = 'atlas-v0.8'
BASE_SHA = '47320ca55f25955ff0d5e73be690465c7f9e6ebad9fa6bbc09692d4cf86371b7'   # atlas-v0.8
MOVED = {'DYAD': dict(edition='v6.4.23', tag='dyad-v6.4.23', authority='OWNER: records/dyad/RTG_DYADIC_v6_4_23_RELEASE_RECORD.md at dyad-v6.4.23 (+ post-tag records/dyad/DYAD_v6_4_23_POST_TAG.md)'),
         'OFN': dict(edition='v0.12', tag='ofn-v0.12', authority='OWNER: records/ofn/OFN_v0_12_RELEASE_RECORD.md at ofn-v0.12'),
         'TRIAD': dict(edition='v1.7', tag='triad-v1.7', authority='OWNER: records/triad/TRIAD_v1_7_RELEASE_RECORD.md (+ post-tag records/triad/TRIAD_v1_7_POST_TAG.md)')}
SHAS = {'DYAD': '9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb',
        'OFN': '55ff8ba85d4bb48b52266bdd9a44aa84efcd2cc19903d059266fa406a6bb76aa',
        'TRIAD': '506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a'}
NEW_RIDS = {'DYAD': ['DYAD-THM-OPEN18-STEP-MONOTONE', 'DYAD-THM-NF-REM-C7-SHARP', 'DYAD-THM-LPHASE-ROWA-BRIDGE', 'DYAD-ART-INBOX-20261030'],
            'OFN': ['RTG-OFN-ALG-REF-CLOSURE-COMPARISON']}
OFN_RID_COUNT = 44     # 17 DEF + 1 HYP + 5 RESULT + 21 OPEN
TRIAD_RID_COUNT = 46   # unchanged from v1.6.1
PIPE_SNAPSHOT = {'closed': 14, 'dispositioned': 3, 'open': 36}
PIPE_BRANCH = {'closed': 15, 'dispositioned': 5, 'open': 33}
PATHS = ['records/dyad/RTG_DYADIC_v6_4_23_RELEASE_RECORD.md', 'records/dyad/DYAD_v6_4_23_POST_TAG.md', 'records/ofn/OFN_v0_12_RELEASE_RECORD.md',
         'records/triad/TRIAD_v1_7_RELEASE_RECORD.md', 'records/triad/TRIAD_v1_7_POST_TAG.md', 'records/triad/TRIAD_SOURCE_RECOVERY_LIST.md',
         'records/atlas/ATLAS_TRIAD_v1_7_29_ROW_CHECK_OWNER.md', 'records/atlas/ATLAS_TRIAD_v1_7_29_ROW_CHECK_CHATGPT.md',
         'pipes/GEN/20261103-TRIAD-p4-identity-question.md', 'pipes/GEN/20261103-TRIAD-birth-symmetry-grade-question.md',
         'pipes/GEN/20261103-TRIAD-v1-7-adopted.md', 'pipes/PROG/20261103-TRIAD-v1-7-adopted.md', 'pipes/RECOG/20261030-DYAD-v6-4-23-adopted.md',
         'pipes/DYAD/20261029-RECOG-c7-ceilings-registration.md', 'pipes/DYAD/20261029-RECOG-d5-bridge-constants-registration.md',
         'evidence/triad/scripts/tetrahedral_six_step_cross_phase_t6c2_patched.py', 'evidence/triad/scripts/triad_analytic_phase_steering_t6l_patched.py']

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
        self.log.append(dict(id=f'AR09-{len(self.log)+1:03d}', finding=finding, where=where, old_sha256=sha(old), new_sha256=sha(new), old=old, new=new))
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
    D, O, T = 'DYAD v6.4.23', 'OFN v0.12', 'TRIAD v1.7'
    # ---- identity ----
    a.rep('# RTG STATE ATLAS v0.8\n', '# RTG STATE ATLAS v0.9\n', 'identity', 'title')
    a.rep('full identities in evidence/atlas/v0.8/source_manifest.json', 'full identities in evidence/atlas/v0.9/source_manifest.json', 'identity', 'SOURCES header')
    a.rep('| DYAD | RTG_DYADIC_OSCILLATOR_DSN | v6.4.22 | `dyad-v6.4.22` | canonical Tier 3 |', '| DYAD | RTG_DYADIC_OSCILLATOR_DSN | v6.4.23 | `dyad-v6.4.23` | canonical Tier 3 |', D, 'SOURCES DYAD row')
    a.rep('| OFN | RTG_ONTOLOGICAL_FOUNDATIONS | v0.11 | `ofn-v0.11` | canonical Tier 2 |', '| OFN | RTG_ONTOLOGICAL_FOUNDATIONS | v0.12 | `ofn-v0.12` | canonical Tier 2 |', O, 'SOURCES OFN row')
    a.rep('| TRIAD | RTG_TRIADIC_BIRTH_LIFT_DSN | v1.6.1 | `triad-v1.6.1` | canonical Tier 3 |', '| TRIAD | RTG_TRIADIC_BIRTH_LIFT_DSN | v1.7 | `triad-v1.7` | canonical Tier 3 |', T, 'SOURCES TRIAD row')
    a.rep('*END — RTG STATE ATLAS v0.8. Noncanonical; owner DSNs govern.*', '*END — RTG STATE ATLAS v0.9. Noncanonical; owner DSNs govern.*', 'identity', 'footer')
    # ---- HEADLINE ----
    a.sub_in_line('H5 D-LINK high —', 'the (D5) constants and the C₇ ceilings remain [assuming:] until Dyadic registers them (RECOG.R-A1).',
                  'Dyadic v6.4.23 registers both: DYAD-THM-LPHASE-ROWA-BRIDGE (c_Q=0.79246, c′_Q=0.36916 outward; the certified majorant is 0.3691523…, so the 0.36915 RECOG assumes lies below it) and DYAD-THM-NF-REM-C7-SHARP (C₇=85.1 / 27.7); RECOG\'s blocks keep [assuming:] until RECOG re-checks them against the registered rows (RECOG.R-A1).', D, 'H5 registrations')
    # ---- D1 (OFN) ----
    a.sub_in_line('(owners: OFN v0.11 adopted 2026-10-30 canonical,', 'OFN v0.11 adopted 2026-10-30 canonical', 'OFN v0.12 adopted 2026-10-30 canonical', O, 'D1 header edition')
    a.sub_in_line('(owners: OFN v0.12 adopted 2026-10-30 canonical,', '1 HYP RID, 4 local RESULT RIDs, 21 OPEN (20 ACTIVE + 1 PARTIAL), 43 OFN RIDs;',
                  '1 HYP RID, 5 local RESULT RIDs, 21 OPEN (20 ACTIVE + 1 PARTIAL), 44 OFN RIDs;', O, 'D1 header counts')
    a.after_line('RTG-OFN-ALG-RAW-STANDARD-C-NOGO RES(from ALG) |', [
        'RTG-OFN-ALG-REF-CLOSURE-COMPARISON RES(from ALG) (v0.12) | sc: abelian carrier group H; connected graph G for (i); cycle graph C_n with coherent orientation for (ii)–(iv); OFN custody | d:H^V→H^E, (ds)_ij=s_i−s_j; Q_node=H^V/H_diag; C₀⊆H^E closure sector (zero oriented sum around every cycle); Q_edge=H^E/H^E_diag · (i) d induces a canonical iso Q_node≅C₀ (isomorphic constructions, not the same operation) · (ii) forgetting one edge is a bijection C₀→H^{E∖{e₀}}, a lossless parametrization; on all of H^E it loses exactly the holonomy · (iii) κ_n:C₀↪H^E↠Q_edge has ker≅H[n], coker≅H/nH ⇒ iso iff multiplication by n is bijective on H; K₃: yes over ℝ^d, no over U(1) (globally 3-to-1, locally a diffeomorphism), ℤ_N with 3|N, ℤ; edge-dependent isomorphisms C₀≅Q_edge exist for every abelian H and are a different comparison · (iv) diagonal node action fixes every edge; diagonal edge action by c preserves C₀ iff nc=0; equal cardinalities do not decide (iii) | ¬ non-abelian carriers, cycles of different lengths/orientations for (iii)–(iv), geometric SO(d) reference, any physical reading of reference consumption (stays with the §2.4 [HYP] and RTG-OFN-OPEN-REF-CLOSURE) | >TRIAD-OPEN-T6R C1 (a carrier using "three node-difference edges minus one closure relation" declares its coefficient group; the Triadic planar carrier is real; D4a.L3) | cert ofn_ref_closure_check.py (R1–R5) | @OFN§2.4',
        '*OFN:causal-interface ALG (recorded inside the §5.5.4 formal-properties [ALG], no RID; v0.12) | class C, b_e=Σ_{j≠e}N(z_j): F_e−N(z_e)=−(κ/3)(N(z_e)+b_e) exactly, no symmetry or truncation used; κ≠0: b_e is a one-step sufficient interface for edge e, minimal in the quotient sense; the dyad law holds on edge e iff b_e=−N(z_e): on the lock surfaces every nonzero edge has an active compensating interface (b₁=−N(z) on 𝒮₀, whose zero edge has b₃=0), while under zero total interface b_e=0 the edge obeys (1−κ/3)N, not the dyad law | ¬ closed reduced dynamics (fails for a diagnostic polynomial, not shown for C2); interface vocabulary of numgen-v1.21 §6.2 N-1A2, its closure not imported | cert ofn_isolation_interface_check.py | @OFN§5.5.4'], O, 'new OFN result node and causal-interface record')
    a.sub_in_line('RTG-OPEN-TRIAD-PRIMACY-ONTO (P2A) ≡ RTG-OFN-OPEN-PRIMACY-3A', 'OFN owns; technical results constrain only',
                  'OFN owns; technical results constrain only; next artifact (OFN v0.12): an explicit completeness/observability criterion, with one operational ingredient available — a sufficient causal interface (*OFN:causal-interface), which for class C separates recovery under a compensating interface from recovery in a quiet or removed environment; completeness is not thereby defined, and full edge autonomy everywhere is a stronger demand than Q3a', O, 'P2A/3A next artifact')
    a.sub_in_line('P2B-CRITERION node (one criterion, three citers:', '| no technical owner assigned |',
                  '| OFN v0.12 evaluation frame for OPEN-OFN-3B (recorded, no standard selected): U-form (recipe G↦T₃[G] fixed on a declared class of single-edge laws) · U-class (that class uses no nonlinear T-data) · C0 (embedding in the declared carrier without a T-derived rechart) · C1 (embedding with T-derived structure) · J (coupling form justified without presupposing recovery of T); class C: U-form passes (T₃[G]=P_κ∘G^{×3}), U-class T-free for ι₀ and relative to the linear data ω=A², A=DT(0) for the chiral pair, C0 fails for the named raw mean-feedback family under Standard C (RTG-OFN-ALG-RAW-STANDARD-C-NOGO, within its scope; separately the raw map is not odd, T(−x)+T(x)=(0,2(coshρ−1)), excluding only the named embedding ι₀ for the raw recipe), C1 passes (T-relative), J open; candidate standards (a) U-form + C1 + reduction witness · (b) also U-class without nonlinear T-data and C0 · (c) also J; class C meets (a), meets (b) only in part, (c) not shown; no primacy conclusion | no technical owner assigned |', O, 'P2B 3B evaluation frame')
    a.sub_in_line('RTG-OFN-OPEN-TRIAD-CLASS (registered at the v0.10 adoption) |', ' | next: the physical selection, isolation and chirality obligations;',
                  ' | isolation frame (OFN v0.12; recorded, none selected): I-comp — dyad law on a balanced invariant regime with a compensating interface (class C meets it exactly; the exact I-comp witness satisfies Standard C, which is not equivalent to I_e≡0) · I-quiet — dyad law under zero total interface (class C fails for κ≠0) · I-remove — dyad law after the environment is removed from the model (needs a declared size-indexed family of laws; class C does not supply one, its normalization κ/3 presupposes three edges) | next: the physical selection, isolation and chirality obligations; the isolation artifact is a contract declaring the intervention class, preserved observables, retained boundary data and, for I-remove, the size-indexed law;', O, 'TRIAD-CLASS isolation frame')
    a.line('RTG-OFN-OPEN-REF-CLOSURE |', 'RTG-OFN-OPEN-REF-CLOSURE (narrowed v0.12) | which reference operation, if any, is the physical (rotational) reference consumption of the §2.4 [HYP]; the mathematical comparison is settled at the scope of RTG-OFN-ALG-REF-CLOSURE-COMPARISON | closure: a stated physical reading with its action (on nodes, on edges, or geometric) in a declared carrier and encoding, shown to coincide with one of the compared constructions, or with none; matching counts alone insufficient | next: a physical reading of the reference operation and the carrier declaration of each branch that uses the counting argument', O, 'REF-CLOSURE narrowed')
    a.after_line('PROG.G8 D-SCOPE', ['PROG.G9 D-LINK (consumer synchronization; Programme maintenance): the Programme v1.3 §7.2 interface rows IF07 TRIAD→GEN and IF11 TRIAD→UVM carry Triadic v1.6 as their recorded pin, and Programme records no CN-05 disposition (TRIAD v1.7 §7.4 matrix: "not recorded"; no receipt inferred; Programme v1.3 is the pass-two edition). An older intentional pin is not a defect by age; the open item is the consumer refresh, which the receiver decides on the filed TRIAD v1.7 notice (pipes/PROG/20261103-TRIAD-v1-7-adopted.md, open).'], T, 'new PROG.G9')
    # ---- D2 (DYAD) ----
    a.sub_in_line('(sources: DYAD v6.4.22 · NUMGEN v1.21', 'DYAD v6.4.22 · NUMGEN v1.21', 'DYAD v6.4.23 · NUMGEN v1.21', D, 'D2 header edition')
    a.sub_in_line('DYAD-THM-NF-REM THM |', 'row A |z|≤1/20: C₇=100 (cert 85.07), C_D=1000 (812.89); row B |z|≤1/40: 30 (27.60), 250 (216.77);',
                  'row A |z|≤1/20: C₇=100 (certified bound 85.0732, rounded up), C_D=1000 (812.894); row B |z|≤1/40: 30 (27.6023), 250 (216.77) (bracket values are the certificate\'s exact upper bounds rounded up, v6.4.23 [COR] of nearest-rounded displays);', D, 'NF-REM bracket values')
    a.after_line('DYAD-THM-NF-REM THM |', ['DYAD-THM-NF-REM-C7-SHARP THM (v6.4.23) | sc: chart and norm of DYAD-THM-NF-REM; rows not mixed | |F̂(z)−J(z)|≤C₇|z|⁷ with C₇=85.1 on |z|≤1/20 and C₇=27.7 on |z|≤1/40 (exact-rational certificate bounds 85.0731933471…, 27.6022209836…) | the DYAD-THM-NF-REM constants (C₇=100/30, C_D=1000/250) are unchanged and remain the inputs of every proof that cites them; the certificate\'s C_D bounds were computed with C₇=100/30 and are not re-derived | >RECOG-THM-R9-SHARPENED-ROWS-C7 (RECOG keeps its [assuming:] until its own re-check; RECOG.R-A1) | cert DYAD-ART-RE-P2B2, DYAD-ART-INBOX-20261030 (O5) | @DYAD§6.14'], D, 'new NF-REM-C7-SHARP node')
    a.sub_in_line('DYAD-THM-LPHASE-ROWA-REMAINDER THM |', '|r|≤1.51632q^{3/2}, bridge factor ≤1.06252 ⇒ 1.61112',
                  '|r|≤1.51633q^{3/2}, bridge factor ≤1.06253 ⇒ 1.61115 (outward decimals, v6.4.23 [COR] of nearest-rounded displays; certificate FIN 1.6111210…; 403/250 unchanged)', D, 'L-PHASE outline decimals')
    a.after_line('DYAD-THM-LPHASE-ROWA-REMAINDER THM |', ['DYAD-THM-LPHASE-ROWA-BRIDGE THM (v6.4.23) | sc: row-A disk |z|≤1/20 of the DYAD-THM-NF-INV chart, used at block base points in U; branch control (B) on U_T | (i) ALG: under (B), r=Λ₃(z)+[S_Θ−L_Θ]+τ[D_Q−D₃]+[Arg(J/z)+τq]+Arg(F̂/J) exactly, Λ₃=L_Θ+τD₃ · (ii) |D_Q|≤c_Qq^{3/2} with c_Q=0.79246 and |D_Q−D₃|≤c′_Qq² with c′_Q=0.36916 (certified exact values 0.7924576152…, 0.3691523046…; the earlier proof-outline display 0.36915 lay below the majorant) | ¬ chart coefficient transferred to NUMGEN L1 (SG-19); L-PHASE and L1 stay NUMGEN-owned | >RECOG-THM-A1C-SHARPENED-SCHEDULE, RECOG-ALG-A1C-LOGFREE-ENVELOPE (RECOG keeps [assuming:] with 0.36915 until its own re-check; RECOG.R-A1) | cert DYAD-ART-LPHASE-ROWA (P-a1, P-a2), DYAD-ART-INBOX-20261030 (O6, O7) | @DYAD§6.14'], D, 'new LPHASE-ROWA-BRIDGE node')
    a.sub_in_line('DYAD-THM-OPEN18 THM-ALG(IA) |', 'DYAD-THM-OPEN18 THM-ALG(IA) |',
                  'DYAD-THM-OPEN18 THM-ALG(IA) (historical first-footprint formulation; text and grade kept with the owner scope note; current form DYAD-THM-OPEN18-STEP-MONOTONE) |', D, 'OPEN18 historical scope')
    a.after_line('DYAD-THM-OPEN18 THM-ALG(IA) (historical', ['DYAD-THM-OPEN18-STEP-MONOTONE THM-ALG(IA) (v6.4.23) | sc: canonical family (ρ₀,η₀)=(0,q); step-indexed; the labels Γ₃:=(0,q_{3/4}], Γ₄:=[q_{3/4},2] are a presentation convention, not a footprint-branch claim | Q_n=ρ_n²−ρ_nη_n+η_n², Θ_n=Arg(ρ_n+ωη_n), ω=e^{2πi/3}, unwrapped η: dQ₃/dq>0, dΘ₃/dq<0 on (0,1.26021520256]; dQ₄/dq>0, dΘ₄/dq<0 on [1.26021320256,2]; in G=[1.26021320256,1.26021520256] ρ₄ has exactly one zero q_{3/4}∈[1.260214202563477114872438560955, 1.260214202563477114872438560958], Θ₄(q_{3/4})=−π/3 (the ISP-funnel edge); uniqueness stated in G only | q_{3/4} ≠ NUMGEN q_* (a root of η₆(q)−q): η₆(q_{3/4})−q_{3/4}≈−0.5537 | cert DYAD-ART-OPEN18 (macro sweeps n=3 on [0.001, inf G] and n=4 on [sup G, 2], micro strip on (0,0.001]; the program exits 0 unconditionally, its result is read from its printed lines), DYAD-ART-INBOX-20261030 (O1–O3) | @DYAD§6.8'], D, 'new OPEN18-STEP-MONOTONE node')
    a.sub_in_line('*DYAD:closed-modules |', 'OPEN 18 closed | @DYAD§2', 'OPEN 18 closed (current form DYAD-THM-OPEN18-STEP-MONOTONE) | @DYAD§2', D, 'closed-modules OPEN 18')
    a.sub_in_line('*NUMGEN:qstar-witness NUM(HP) |', '~ DYAD-THM-OPEN18 q=q* branch split (same q*?: atlas link, verify)',
                  '≠ DYAD q_{3/4} (DYAD-THM-OPEN18-STEP-MONOTONE: η₆(q_{3/4})−q_{3/4}≈−0.5537; two different numbers under one symbol; NUMGEN defers the cross-citation, v1.21 NC-17)', D, 'NUMGEN q* typed')
    a.sub_in_line('NUMGEN.N-A + DYAD.X10 ~ D-LINK |', 'atlas-checked: 403/250=1.612≥1.61112.',
                  'atlas-checked: 403/250=1.612≥1.61115 (the v6.4.23 outward chain; certificate FIN 1.6111210…).', D, 'N-A + X10 check value')
    a.drop_line('NUMGEN.N-Q* ~ D-LINK |', D, 'NUMGEN.N-Q* answered (retired)')
    a.line('RECOG.R-A1 D-LINK (cross-owner dependency) |', 'RECOG.R-A1 D-LINK (cross-owner dependency) | RECOG v0.3.25/v0.3.26 prove RECOG-THM-A1C-SHARPENED-SCHEDULE, the A1c decoder blocks and RECOG-ALG-A1C-LOGFREE-ENVELOPE [assuming: the Dyadic (D5) row-A bridge proof constants 0.79246, 0.36915 of the LPHASE row-A proof] and RECOG-THM-R9-SHARPENED-ROWS-C7 [assuming: C₇≤85.1 / 27.7]. Dyadic v6.4.23 answers both registration requests (DYAD pipe items closed): DYAD-THM-NF-REM-C7-SHARP registers C₇=85.1 / 27.7 as RECOG assumes; DYAD-THM-LPHASE-ROWA-BRIDGE registers c_Q=0.79246 and c′_Q=0.36916 with the exact remainder decomposition (accept with change: the certified majorant is 0.3691523…, so the assumed 0.36915 lies below it). RECOG may drop [assuming:] only after its own re-check against the registered rows (c′_Q=0.36916); the DYAD notice is filed (pipes/RECOG/20261030-DYAD-v6-4-23-adopted.md, open; the receiver decides). RECOG-ALG-A1C-RECIPROCAL-DRIFT uses adopted Dyadic rows only (DYAD-ALG-NF6, DYAD-THM-NF-REM); its K_ε is 98 % the C₇=100 ceiling, so a Dyadic orbit bound on Re(ρ₇/z) would lower it (informational, pipes/DYAD/20261029-RECOG-v0-3-26-adopted.md). RECOG still pins NUMGEN v1.20.8 (repin to v1.21 is RECOG\'s separate maintenance).', D, 'RECOG.R-A1 reworded')
    a.sub_in_line('RECOG-THM-R9-MEMORY THM |', 'not Dyadic theorem statements, registration requested]', 'not Dyadic theorem statements, registration requested] (Dyadic v6.4.23 registers C₇=85.1 / 27.7 as DYAD-THM-NF-REM-C7-SHARP; RECOG.R-A1)', D, 'R9 sharpened rows cross-note')
    a.sub_in_line('RECOG-ALG-A1C-LOGFREE-ENVELOPE ALG·c (v0.3.26) |', 'proof constants, not theorem rows; registration requested]',
                  'proof constants, not theorem rows; registration requested] (Dyadic v6.4.23 registers c_Q=0.79246, c′_Q=0.36916 in DYAD-THM-LPHASE-ROWA-BRIDGE; 0.36915 lies below the certified majorant 0.3691523…; RECOG.R-A1)', D, 'LOGFREE envelope cross-note')
    a.line('NUMGEN.N-I1 D-LINK (pipe states, receiver side) |', 'NUMGEN.N-I1 D-LINK (pipe states, receiver side) | at the source snapshot f20f080 with this edition\'s three ATLAS state changes, pipes_index --check passes with 53 items in 20 inboxes (the LIT inbox then held none) — 15 closed, 5 dispositioned, 33 open; items filed after the snapshot (e.g. the DYAD and LIT items of PR #148) enter the next refresh. closed: the seven DYAD inbox items (NUMGEN\'s q* question and v1.21 notice; RECOG\'s two registration requests and v0.3.26 notice; OFN\'s v0.11 and v0.12 notices; after dyad-v6.4.23), OFN\'s three inbox items (NUMGEN, TDR-G, RECOG notices), NUMGEN\'s request and notice to TDR-G, RECOG\'s A1b notice to NUMGEN, RECOG\'s v0.3.26 notice to ATLAS (atlas-v0.8), TRIAD\'s v1.7 row-check request to ATLAS (answered by records/atlas/ATLAS_TRIAD_v1_7_29_ROW_CHECK_OWNER.md and …_CHATGPT.md) · dispositioned: NUMGEN\'s finding and notice to RECOG; OFN\'s v0.12 notice to TRIAD (no action); the DYAD v6.4.23 and TRIAD v1.7 notices to ATLAS (accept; carried by this edition, closed by the atlas owner after its tag) · open: DYAD v6.4.23 notices to NUMGEN, OFN, RECOG; TRIAD v1.7 notices to GEN, OFN, PROG, RRF, UVM and its two questions to GEN (𝒫₄ identity, birth-symmetry grade; F30); OFN v0.11 notices to ER2B, FMS, GEN, NUMGEN, PROG, RECOG, RRF, TDRG and OFN v0.12 notices to FMS, GEN, NUMGEN, PROG, RRF; OFN\'s token-sum label finding to TDR-G; NUMGEN v1.21 notice and cyclic-average offer to GEN; TDR-G v2.12.14 notices to NUMGEN and AZ; RECOG v0.3.26 notices to NUMGEN, RER, RRF; GEN\'s κ_f items to PROG and UVM. A filed item is not adopted use; each receiver decides at its own checkpoint (CONVENTIONS §7).', 'pipes', 'NUMGEN.N-I1')
    # ---- D4a (TRIAD) ----
    a.sub_in_line('(sources: GEN v2.9 primitive/triad/K3/K4/phase parts ·', 'TRIAD v1.6.1 · RER v0.2 nc', 'TRIAD v1.7 · RER v0.2 nc', T, 'D4a header edition')
    a.sub_in_line('TRIAD models (SG-3;', '· M_orient^corr Ω̇=−√3ω̇_raw, formal 5-variable extension, coefficient level, no physical K<1 carrier ·',
                  '· M_orient^corr Ω̇=−√3ω̇_raw, formal 5-variable extension, coefficient level, no physical K<1 carrier; the off-root extension is not unique — (a) literal ΔQ_c^(1)=Q_cq₁ with independent Q_c, (b) Q_c-free (Q_c replaced by Q̂_c=(I_sc²+Ω²)/Q_s) — root-equivalent, fixed only by the T-6r contract C3; time = continuous coefficient-ODE time in six-step-block units, not the exact discrete six-step map ·', T, 'models: extensions and clock')
    a.sub_in_line('TRIAD-ALG-T6E-ORIENTATION-NORMALIZATION ALG·dx |', '| uses archived T-6a2/T-6c radial ledgers (not regenerated) |',
                  '| typed (v1.7): the Gram relation is the first-variation (degree-3) coefficient of the exact identity Δ𝒢≡0 for actual planar pairs (weights Q_s,Q_c,I,Ω 1 and r ½; every retained r^j increment homogeneous of degree 2); the exact finite increment adds the degree-4 terms ΔQ_sΔQ_c−(ΔI)²−(ΔΩ)² and Q×(next-order increments), discarded by the retained six-step expansion; a coefficient-level identity, not an exact discrete conservation law of the six-step map; RID kept | uses archived T-6a2/T-6c radial ledgers (not regenerated) |', T, 'T-6e Gram typing')
    a.line('*TRIAD:K1-tangency ALG·dx |', '*TRIAD:K1-tangency ALG·dx | corrected 5-variable extension (domain Q_s, Q_c>0): 𝒢=Q_sQ_c−I²−Ω², 𝒢̇=(f_s/Q_s)𝒢; K̇=(1−K)f_c/Q_c ⇒ K̇=0 on K=1 at all retained r orders, in both root-equivalent extensions (no inward/outward sectors); (b) Q_c-free: f_s=Q̇_s, f_c=Q̇_c; (a) literal: f_s=Q̇_s+rQ_sq₁, f_c=Q̇_c−rQ_cq₁, q₁=6(5√14Ω−√42I)/(7√Q_s) | remark (no RID; sc: truncated coefficient ODE, diagnostic): D=𝒢/Q_s=Q_c(1−K); (b) Ḋ=0, a first integral of the truncated field; (a) Ḋ=rq₁D, constant only on the r¹-free field and on special solutions such as D≡0 (K=1), in general only the sign of D (K<1, K=1, K>1) preserved | ¬ stability, escape, basin, physical K<1 carrier; ¬ conserved physical mode; ¬ statement about the exact six-step map; which extension the historical downstream code used is not checkable from the repository | atlas-checked exact (2 Nov 2026, by hand and by rerun of the owner scripts triad_reconciliation_row1_extension_check.py, triad_coowner_row1_row3_check.py, PASS): (a) Ḋ=rq₁D and the 𝒢̇, K̇ forms with the stated f_s, f_c | @§6.18', T, 'tangency: extensions and D remark')
    a.sub_in_line('TRIAD-ALG-T6L-NORMALIZED-TORSION-SIGN ALG |', '>0 for (μ,ν)≠0 (any K>0);',
                  '>0 for (μ,ν)≠0 (any K>0); coercive (v1.7, leading coefficient only): A_θ^corr=(μ,ν)M_θ(μ,ν)ᵀ, M_θ=[[3√3,3],[3,9√3]], eigenvalues 6√3±6 ⇒ 6(√3−1)K≤A_θ^corr≤6(√3+1)K; no sign persistence at finite u or r≠0, and no trajectory, basin or global statement, without a proved uniform remainder below 6(√3−1)K;', T, 'T-6l coercive bound')
    a.sub_in_line('TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC ALG |', '(from V_d=½B⁻¹∇_d𝒫₄, premises G₂=0, 𝒫₄=2dᵀBG_{3,d})',
                  '(from V_d=½B⁻¹∇_d𝒫₄, premises G₂=0, 𝒫₄=2dᵀBG_{3,d}; the 𝒫₄ identity keeps its gen-v2.8.7 claim-level pin in TRIAD v1.7 §7.2, not printed at gen-v2.9, F30)', T, 'T-6u held pin')
    a.sub_in_line('TRIAD-EXPORT-PROTOCOL-2 DEF |', '| @TRIAD§6.14,§7.3',
                  '| consumer state per recipient: TRIAD v1.7 §7.4 matrix (10 rows: CN × recipient, Triadic claim-level pin, cited edition, queue, statement accepted, adopted use, remaining gate); the recorded receipts are of the v1.6 notices — a v1.6 receipt is not acceptance of the v1.6.1 or v1.7 delta; Programme CN-05 not recorded (PROG.G9); RRF convention-only; OFN reference-only; GEN imports T-6s/t/u at [CAND] (F31) | @TRIAD§6.14,§7.3,§7.4', T, 'export: consumer matrix')
    a.sub_in_line('*TRIAD:return-coefficients ALG |', '96:1 same-object correspondence (generator/mode/observable/time-block/extraction) OPEN;',
                  '96:1 same-object correspondence (generator/mode/observable/time-block/extraction) OPEN; the ratio is not invariant under an unproved metric/observable dictionary (same planar vectors, B_T=2B_G: in a hypothetical common model the same arithmetic gives 192; not a new ratio; TRIAD v1.7 §1 is the single statement);', T, '96:1 metric caveat')
    a.sub_in_line('TRIAD: T6R corrected orientation model/domain', 'TRIAD: T6R corrected orientation model/domain (carrier for any K<1 diagnostic, corrected Ω̇, finite-u/r vector field or exact map, event guards, model/observable transport; then decide if basin test is meaningful; no rescaling of history) · T6Q typed sign/action table (σ, folded/unfolded angle, M_root vs M_orient) ·',
                  'TRIAD: T6R corrected orientation model/domain — acceptance contract (TRIAD v1.7 §2; all six required): C1 carrier, metric and coefficient group (RTG-OFN-ALG-REF-CLOSURE-COMPARISON enters as an interface constraint: the K₃ reference comparison is an iso over ℝ^d, not over U(1), ℤ_N with 3|N, or ℤ; the Triadic planar carrier is real) · C2 encoding and reduction maps to (Q_s,Q_c,I_sc,Ω,r) and back · C3 full evolution including how each coefficient extends off the root (fixes f_s, f_c and the fate of D) · C4 primitive or six-step clock and phase convention · C5 event and contact predicates, event guards, regularity · C6 covariance under the declared complete-state action (T6Q); RRF and OFN model classes are interface constraints, not an identification with the physical birth carrier; only then decide whether a basin/escape calculation is meaningful; no rescaling of historical trajectories; no corrected-field trajectory campaign is decisive before the contract · T6Q coordinate sign table recorded (TRIAD v1.7 §2, ALG, coordinate bookkeeping on an identified planar pair): (s,c)↦(c,s) Q_s↔Q_c, I_sc kept, Ω negated, (μ,−ν), σ flips · (s,c)↦(−s,c) I_sc and Ω negated, (−μ,−ν), σ flips · (s,c)↦(−s,−c) all kept; K invariant under each; not a node-exchange gauge action, dynamical symmetry, carrier isomorphism or branch continuation; open: a typed action on the complete state of the chosen corrected model, intertwining with its dynamics ·', T, 'frontier: T-6r contract, T-6q table')
    a.sub_in_line('F11 D-CONV (TRIAD.T7):', '(obligation, not applied).',
                  '(obligation, not applied). TRIAD v1.7 §1 adds that the 96:1 ratio is not invariant under this dictionary (hypothetical 192); RRF v0.8.4 §3.1 records B_T^plane=2B_G as convention-only with the Q_c^T conversion an unapplied obligation.', T, 'F11 metric caveat')
    a.sub_in_line('F13 D-RID/D-LINK (ER2B.Z8, RER.E8, GEN.D7, TRIAD.T3):', 'TRIAD imports birth-leading, chrono-protection, P4, birth-symmetry by locator.',
                  'TRIAD imports birth-leading, chrono-protection, P4, birth-symmetry by locator (TRIAD v1.7 §7.2: re-read at gen-v2.9, the nine "RID unavailable" imports still have no result RID there, and Genesis records no response to the REQ-T16 requests).', T, 'F13 RID state')
    a.sub_in_line('F14 D-PROOF (TRIAD.T5, GEN.D3 primitive part):', '(a) T-6m argument session-only.',
                  '(a) T-6m argument session-only. TRIAD custody (v1.7 header; records/triad/TRIAD_SOURCE_RECOVERY_LIST.md): the v1.6 evidence package evidence/accepted_r4_2/ is held by the PI, not in the repository, and the hashes printed in TRIAD §8 remain the identities; the T-6e H₁, H₂ producer bytes are missing; the T-6c2 and T-6l producers are in the repository (evidence/triad/scripts/, hash-equal to TRIAD §8, recovered from commit 9df0319).', T, 'F14 custody')
    a.drop_line('F20 D-STALE (TRIAD.T9):', T, 'F20 fixed by the owner (retired)')
    a.after_line('F29 ~ D-LINK (RER.E2 follow-up):', [
        'F30 D-PIN/D-GRADE (TRIAD.T11; questions to the GEN owner): TRIAD v1.7 §7.2 holds the radial-polynomial import at its gen-v2.8.7 claim-level pin, because the identity 𝒫₄=2dᵀBG_{3,d} used with it is not printed at gen-v2.9 (only the c-mode analogue ΔQ_c^(4)=2cᵀBG_{3,c}, GEN-THM-DELTA-QC); and it imports the birth-symmetry theorem as [THM] while gen-v2.9 states it [THM] in §6.6 (L987) and [ALG] in the §1 and §2 summaries (L80, L419) and in the GEN-ART-JQ-PHASEDRIFT row (L1246). Both are filed as questions (pipes/GEN/20261103-TRIAD-p4-identity-question.md, pipes/GEN/20261103-TRIAD-birth-symmetry-grade-question.md; open, the receiver decides); no Triadic grade changes.',
        'F31 D-GRADE (consumer side; TRIAD.T12): GEN v2.9 imports T-6s, T-6t and T-6u at [CAND] (gen-v2.9 §2 for TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY and TRIAD-ALG-T6T-JACOBI-MODE-SIGNS; GEN-CAND-APEX-T6U for TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC), below the Triadic owner [ALG], with Triadic v1.6 import pins; that is the receiver\'s grading of its own use. The TRIAD v1.7 notice is filed (pipes/GEN/20261103-TRIAD-v1-7-adopted.md, open).',
        'F32 D-STALE (low; TRIAD.T13): the TRIAD v1.7 §2 T-6u record keeps v1.6-era wording ("registered by this owner release", "Exact-candidate review and owner publication are complete"), which reads as v1.7 in the v1.7 file (owner note A-1; scientific content unchanged; deferred by the PI as nonblocking). The other open TRIAD form notes (F-1 qualifier syntax, F-2 status-summary length, row 29 history_appendix profile with PR #113) are process debt recorded in records/triad/TRIAD_v1_7_RELEASE_RECORD.md, not atlas diagnostics.'], T, 'new F30, F31, F32')
    # ---- rev. 2: final-review sweep (pointer currency) ----
    a.sub_in_line('DYAD-DEF-BRIDGE-EXPORT-CONTRACT DEF |', '>TRIAD v1.6.1 §7.1 and GEN v2.8.9 (both pin DYAD v6.4.13)', '>TRIAD v1.7 §7.1 (item 1, claim-level repin to DYAD v6.4.23) and GEN v2.9 §7 (item 1, historical pin DYAD v6.4.13)', T, 'rev2: export-contract consumer edge')
    a.sub_in_line('AZ.A2 D-STALE (Thread A) |', '(current v2.8.9)', '(current GEN v2.9)', 'currency', 'rev2: AZ.A2 (D2) GEN pointer')
    a.sub_in_line('AZ.A2 D-STALE: §4.1.2', '(current GEN v2.8.9)', '(current GEN v2.9)', 'currency', 'rev2: AZ.A2 (D5) GEN pointer')
    a.rep('— verify against GEN v2.8.9; routing', '— verify against GEN v2.9; routing', 'currency', 'rev2: Legacy row GEN pointer (verify)')
    a.rep('recheck REQ-L07-06 against GEN v2.8.9.', 'recheck REQ-L07-06 against GEN v2.9.', 'currency', 'rev2: Legacy row GEN pointer (recheck)')

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

STALE = [r'`dyad-v6\.4\.22` \|', r'\| v6\.4\.22 \| `dyad', r'`triad-v1\.6\.1` \|', r'\| v1\.6\.1 \| `triad', r'`ofn-v0\.11` \|', r'\| v0\.11 \| `ofn',
         r'\(cert 85\.07\)', r'⇒ 1\.61112', r'≥1\.61112', r'bridge factor ≤1\.06252', r'plausibly the same q\*', r'same q\*\?: atlas link',
         r'consumer acceptance pending', r'TRIAD v1\.6\.1 ·', r'4 local RESULT RIDs', r'43 OFN RIDs',
         r'edge-closure reduction vs reference consumption = same construction\?', r'remain \[assuming:\] until Dyadic registers them',
         r'DYAD v6\.4\.22 · NUMGEN', r'TRIAD v1\.6\.1 §7\.1', r'current v2\.8\.9', r'current GEN v2\.8\.9', r'against GEN v2\.8\.9', r'at this edition pipes_index',
         r'PROG\.G9 D-STALE', r'F32 D-STALE \(low; owner-recorded form debt']

def stale_editions(text):
    # *ATLAS:checked-* lines are dated evidence records ("sources as then read", EV-NOT-RERUN) and are left as recorded
    return [l[:90] for l in text.split('\n') if not l.startswith('*ATLAS:checked-') and any(re.search(p, l) for p in STALE)]

def node(text, prefix):
    ls = [l for l in text.split('\n') if l.startswith(prefix)]
    return ls[0] if len(ls) == 1 else ''

def scope_guards(text):
    """Owner scope that must survive in the refreshed nodes (focused, statement-level)."""
    bad = []
    b = node(text, 'DYAD-THM-LPHASE-ROWA-BRIDGE THM')
    if 'c′_Q=0.36916' not in b or 'c′_Q=0.36915' in b: bad.append('LPHASE bridge constant')
    k = node(text, '*TRIAD:K1-tangency')
    if '(a) Ḋ=rq₁D, constant only on the r¹-free field' not in k or '(a) Ḋ=0' in k or '(b) Ḋ=0, a first integral' not in k or '¬ conserved physical mode' not in k: bad.append('D remark extension dependence')
    e = node(text, 'TRIAD-ALG-T6E-ORIENTATION-NORMALIZATION')
    if 'not an exact discrete conservation law of the six-step map' not in e or 'degree-4' not in e: bad.append('Gram relation typing')
    f = node(text, 'TRIAD: T6R corrected orientation model/domain')
    if not all(f'· C{i} ' in f or f': C{i} ' in f for i in range(1, 7)): bad.append('T-6r contract C1–C6')
    if 'not a node-exchange gauge action' not in f: bad.append('T-6q bookkeeping label')
    for pre, w in [('RTG-OFN-OPEN-TRIAD-CLASS', 'none selected'), ('P2B-CRITERION node', 'no standard selected')]:
        if w not in node(text, pre): bad.append(f'{pre}: {w}')
    if 'iso iff multiplication by n is bijective' not in node(text, 'RTG-OFN-ALG-REF-CLOSURE-COMPARISON'): bad.append('REF-CLOSURE (iii)')
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
    old = json.loads(at(BASE_TAG, 'evidence/atlas/v0.8/source_manifest.json'))
    m = json.loads(json.dumps(old))
    for s in m['sources']:
        for k in [k for k in s if k.startswith('v0_7_')]: del s[k]
    m.update(atlas='v0.9', frozen_at='2026-11-03', repository_snapshot=SNAPSHOT, previous_atlas_tag=BASE_TAG, method_tag='atlas-v0.2', method_edition='v0.2')
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_8_edition'] = prev['edition']; s['v0_8_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] in MOVED:
            mv = MOVED[s['key']]; data = at(mv['tag'], s['path'])
            s.update(edition=mv['edition'], tag=mv['tag'], commit=git('rev-parse', mv['tag'] + '^{commit}').decode().strip(), sha256=sha(data), authority=mv['authority'])
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(SNAPSHOT, s['path']), ('snapshot/tag divergence', s['key'])
        s['v0_8_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_8_input_equality'] for x in m['sources']) == {'EQUAL': 15, 'CHANGED': 3}
    assert {x['key'] for x in m['sources'] if x['v0_8_input_equality'] == 'CHANGED'} == set(MOVED)
    for k, h in SHAS.items(): assert next(s for s in m['sources'] if s['key'] == k)['sha256'] == h, k
    wjson(OUT / 'source_manifest.json', m)
    # ---- H -> L5 ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys ----
    oldret = json.loads(at(BASE_TAG, 'evidence/atlas/v0.8/retired_l5_keys.json'))
    newret = {'NUMGEN.N-Q*': 'DYAD v6.4.23 (D1; pipes/DYAD/20261026-NUMGEN-q-star-branch-split.md closed, accept with change): DYAD-THM-OPEN18-STEP-MONOTONE isolates q_{3/4}≈1.2602142026 (ρ₄=0, Θ₄=−π/3); NUMGEN q*≈0.3156258837 is the root of η₆(q)−q; η₆(q_{3/4})−q_{3/4}≈−0.5537 — different numbers under one symbol. The NUMGEN-side note stays at *NUMGEN:qstar-witness.',
              'F20': 'TRIAD v1.7 (rows 9–11): the §1 "consumer acceptance pending" wording and the §2 send queue are gone; §7.4 carries a per-recipient consumer matrix, recorded at the TRIAD-EXPORT-PROTOCOL-2 node with PROG.G9 and F31.',
              'TRIAD.T9': 'Co-key of F20; retired with it.'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    assert not set(newret) & set(oldret['retired'])
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret if '.' in k]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.9 reasons in dispositions.json.'))
    # ---- shared checker ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at('atlas-v0.2', 'evidence/atlas/coverage_map_v0_2.json'))
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.9/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    # ---- RID presence in the tagged sources (naming check, not certificate replay) ----
    presence = {f'{k}:{r}': (('RID: ' + r) in src[k]) for k, rs in NEW_RIDS.items() for r in rs}
    assert all(presence.values()), [k for k, v in presence.items() if not v]
    for r in NEW_RIDS['DYAD'] + NEW_RIDS['OFN']: assert r in text, r
    ofn_rids = sorted(set(re.findall(r'RID: (RTG-OFN-[A-Z0-9-]+)', src['OFN']))); assert len(ofn_rids) == OFN_RID_COUNT, len(ofn_rids)
    triad_rids = sorted(set(re.findall(r'\[RID: (TRIAD-[A-Z0-9-]+)\]', src['TRIAD']))); assert len(triad_rids) == TRIAD_RID_COUNT, len(triad_rids)
    old_triad = sorted(set(re.findall(r'\[RID: (TRIAD-[A-Z0-9-]+)\]', at('triad-v1.6.1', 'dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md').decode()))); assert triad_rids == old_triad
    for p in PATHS: assert at(SNAPSHOT, p), p
    n_snap, st_snap = pipe_states(SNAPSHOT); assert n_snap == 53 and st_snap == PIPE_SNAPSHOT, (n_snap, st_snap)
    n_items, states = pipe_states(None); assert n_items == 53 and states == PIPE_BRANCH, (n_items, states)
    # ---- dispositions ----
    def row(t, key):   # all rows of a key, joined (AZ.A2 has a D2 and a D5 row)
        ls = [l for l in t.split('\n') if l.startswith(key + ' ')]; return '\n'.join(ls) if ls else None
    touched = ['NUMGEN.N-Q*', 'F20', 'TRIAD.T9', 'NUMGEN.N-A', 'NUMGEN.N-I1', 'RECOG.R-A1', 'F11', 'F13', 'F14', 'F18', 'OFN.O6', 'OFN.O9', 'OFN.O10', 'OFN.O11', 'OFN.O14', 'PROG.G5', 'PROG.G6', 'PROG.G8', 'AZ.A2', 'PREL.P1']
    disp = []
    for key in touched:
        o = row(base, key) if key != 'TRIAD.T9' else row(base, 'F20')
        n = row(text, key) if key != 'TRIAD.T9' else None
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded')
        disp.append(dict(key=key, disposition=state, reason=newret.get(key, 'unchanged: the owner state it records is unchanged at the v0.9 sources' if state == 'retained' else 'reworded; see edit_log.json'),
                         previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    for key in ['PROG.G9', 'F30', 'F31', 'F32']:
        disp.append(dict(key=key, disposition='new', reason='see edit_log.json', previous_sha256=None, current_sha256=sha(row(text, key))))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    t = text.replace('until RECOG re-checks them against the registered rows (RECOG.R-A1).', 'until RECOG re-checks them against the registered rows (RECOG.R-A1, NUMGEN.N-Q*).', 1); ctl('U1', 'H cites a retired L5 row', 'H5:NUMGEN.N-Q*' in h_l5_map(t)['dangling'])
    t = text + 'F20 D-STALE: reused\n'; ctl('U2', 'retired key reused', bool(c.run(t, m, src, cmap, idmap, retired, with_sources=False).fails()))
    t = text.replace('| v1.7 | `triad-v1.7` |', '| v1.6.1 | `triad-v1.6.1` |', 1); ctl('U3', 'SOURCES row older than manifest', bool(c.run(t, m, src, cmap, idmap, retired).fails()) or bool(stale_editions(t)))
    t = text.replace('DYAD-THM-OPEN18-STEP-MONOTONE THM-ALG(IA) (v6.4.23)', 'DYAD-THM-OPEN18-STEP-MONOTONIC THM-ALG(IA) (v6.4.23)', 1); ctl('U4', 'new DYAD RID misspelled against the source (shared checker links FAIL)', bool(c.run(t, m, src, cmap, idmap, retired).fails()))
    t = text.replace('⇒ 1.61115 (outward decimals', '⇒ 1.61112 (outward decimals', 1); ctl('U5', 'nearest-rounded L-PHASE decimal reintroduced', bool(stale_editions(t)))
    t = text.replace('c′_Q=0.36916 (certified exact values', 'c′_Q=0.36915 (certified exact values', 1); ctl('U6', 'below-majorant c′_Q shown as the registered Dyadic constant', bool(scope_guards(t)))
    t = text.replace('(a) Ḋ=rq₁D, constant only', '(a) Ḋ=0, constant only', 1); ctl('U7', 'D claimed constant in the literal extension', bool(scope_guards(t)))
    t = text.replace('; a coefficient-level identity, not an exact discrete conservation law of the six-step map;', ';', 1); ctl('U8', 'Gram relation typed as an exact six-step law', bool(scope_guards(t)))
    t = text.replace('RTG-OFN-ALG-REF-CLOSURE-COMPARISON RES(from ALG) (v0.12)', 'RTG-OFN-ALG-REF-CLOSURE-COMPARE RES(from ALG) (v0.12)', 1); ctl('U9', 'new OFN RID misspelled against the source (shared checker links FAIL)', bool(c.run(t, m, src, cmap, idmap, retired).fails()))
    t = text.replace(' · C3 full evolution including how each coefficient extends off the root (fixes f_s, f_c and the fate of D)', '', 1); ctl('U10', 'T-6r contract item dropped', bool(scope_guards(t)))
    t = text.replace('F14 D-PROOF (TRIAD.T5', 'F19 D-STALE: TRIAD §1 says CN-01–CN-05 "consumer acceptance pending"\nF14 D-PROOF (TRIAD.T5', 1); ctl('U11', 'stale consumer-status wording reintroduced', bool(stale_editions(t)))
    t = text.replace('isolation frame (OFN v0.12; recorded, none selected)', 'isolation frame (OFN v0.12; I-comp selected)', 1); ctl('U12', 'isolation contract shown as selected', bool(scope_guards(t)))
    t = text.replace('(current GEN v2.9)', '(current GEN v2.8.9)', 1); ctl('U13', 'stale GEN edition pointer reintroduced', bool(stale_editions(t)))
    t = text.replace('>TRIAD v1.7 §7.1 (item 1', '>TRIAD v1.6.1 §7.1 (item 1', 1); ctl('U14', 'stale TRIAD consumer pin on the export contract', bool(stale_editions(t)))
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), controls
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas=BASE_TAG, base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()), atlas_lines=text.count('\n') + 1,
                   source_snapshot=SNAPSHOT, changed_sources=list(MOVED), edit_operations=len(a.log), retired_keys=list(newret), new_keys=['PROG.G9', 'F30', 'F31', 'F32'],
                   new_node_rids=NEW_RIDS, ofn_rids_at_tag=len(ofn_rids), triad_rids_at_tag=len(triad_rids),
                   pipes=dict(items=n_items, snapshot=st_snap, branch=states), dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_controls=len(shared), focused_controls=len(controls),
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_9.py': sha(Path(__file__).read_bytes())},
                   limitations=['Structural checks only; no owner certificate rerun for this edition; new RIDs checked for presence in the tagged sources, not re-proved. The TRIAD row-1 algebra was checked by hand and the owner row-1–3 scripts rerun in the Atlas row check of 2 Nov 2026 (records/atlas/ATLAS_TRIAD_v1_7_29_ROW_CHECK_OWNER.md).',
                                'Impact refresh of three moved sources (DYAD v6.4.23, OFN v0.12, TRIAD v1.7); the other 15 domains were not re-extracted; pipe items cited as filed, receiver dispositions are not atlas sources.',
                                'DYAD v6.4.23 §§6.8, 6.14, 8; OFN v0.12 §§2.4, 5.5.4, 9; TRIAD v1.7 §§1, 2, 6.4, 6.9, 6.18, 7.2, 7.4, 8 and the release records extracted at statement level from the tagged files; proofs live in the owner cells.'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
