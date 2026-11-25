#!/usr/bin/env python3
"""Atlas v0.14 -> v0.15 candidate: one impact refresh for one moved source, under Atlas Method v0.3 (`atlas-method-v0.3`):
Dyadic Arithmetic-Resonance Transform v0.19 (`dzt-v0.19`, adopted 20 Nov 2026). The Atlas was at `dzt-v0.8`; this refresh
carries both DZT editions since then: v0.18 (corrections and Methodology v1.4 migration, no new claim) and v0.19 (the all-p
amplitude-norm theorem DZT-THM-CASCADE-NORM-LAW [THM] [assuming: DYAD-THM-Q403-PHASELAW], DZT-OPEN-NORM-LAW closed, the mod-4
[HYP] retired as DZT19-C01). The other 17 sources are byte-identical to the v0.14 manifest and are not re-extracted.

D2: SOURCES row and D2 header; new node DZT-THM-CASCADE-NORM-LAW (cert DZT-ART-NORMLAW-CHECK), one dependency
(<DYAD-THM-Q403-PHASELAW), the sign and p=8 outside; the finite rows (CASCADE-NORM, ANOMALY-SET) point to it as finite cases;
*DZT:mechanism HYP removed (owner [SUPERSEDED] DZT19-C01, named in the theorem node); *DZT:p40-flag removed (gone from the
owner text); DZT-HYP-MAHLER-NEARMISS FAIL kept; the imported note's 2^{-phi(q)} recorded as a wrong value, not as "no
denominator law"; the DZT import record and the reverse relation on DYAD-THM-Q403-PHASELAW restated at the owner's §7
(owner RIDs only, App F parts without RIDs); frontier: DZT-OPEN-NORM-LAW CLOSED with its result named.
L5: DZT.Q1 (note strings), DZT.Q4 (compound grades), DZT.Q5 (§1 scope) retired with reasons; H3 (only DZT.Q1) retired;
METH.M1 without DZT; PROG.G6 records the DZT edition after the Programme record. Pipes: NUMGEN.N-I1 at the new snapshot.
Run from the repository root: python3 -I evidence/atlas/build/refresh_v0_15.py
"""
from __future__ import annotations
import importlib.util, json, re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'evidence/atlas/v0.15'
ATLAS = 'atlas/RTG_STATE_ATLAS.md'
SNAPSHOT = '357b963'   # resolved to the full commit in main(); main after PR #345 (dzt-v0.19 tagged at 5f3b205, an ancestor)
BASE_TAG = 'atlas-v0.14'
BASE_SHA = 'd34e5697ae47201133f513bce5f6b2b8438ed2f4e654fe33a73048a5ca7b1e85'
METHOD_TAG, METHOD_SHA = 'atlas-method-v0.3', 'a29217352d989f75310f1c5fbb5e666cb02be9bc9a7c3b67d03d6e138115509f'
DZT_PATH = 'dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md'
MOVED = {'DZT': dict(edition='v0.19', tag='dzt-v0.19', authority='OWNER: release record `records/dzt/DZT_v0_19_RELEASE_RECORD.md` (PI adopted 20 Nov 2026, candidate 50f58c88…7442; publication transform: three status lines)')}
SHAS = {'DZT': '2b959f46b8e23363beac087183caf4946d63d1e8d5ac597bdb7d9230143bf6ce'}
CHECK_PATH, CHECK_SHA = 'evidence/dzt/norm_law_review/dzt_norm_law_review_check.py', '566867bb541cd3f5cb4fb1aa11c43ddd4f9b9c0a1e5149697c35a805ac4cebb7'
THM_HEAD = 'DZT-THM-CASCADE-NORM-LAW THM (assuming: DYAD-THM-Q403-PHASELAW; proof: written derivation) |'
HOMES = {'DZT-THM-CASCADE-NORM-LAW': ('node', THM_HEAD), 'DZT-ART-NORMLAW-CHECK': ('cert', THM_HEAD)}
PIPE_SNAPSHOT = {'closed': 80, 'dispositioned': 5, 'open': 62}
NOTE_STRINGS = ['DYAD-THM-Q403-PHASE-ALLP', 'DYAD-ALG-PHASELAW', 'DYAD-THM-P1', 'DYAD-THM-REALITY', 'DYAD-THM-LEAD', 'DYAD-THM-R ', 'DYAD-CF-Q403', 'DYAD-ALG-CASCADE-P12', 'DYAD-ART-CASCADE-Q4-03']
PATHS = ['records/dzt/DZT_v0_19_RELEASE_RECORD.md', 'records/dzt/DZT_v0_18_RELEASE_RECORD.md', 'records/dzt/DZT_NORM_LAW_OWNER_REVIEW.md',
         'records/dzt/DZT_REACTIVATION_TRIAGE.md', CHECK_PATH, 'pipes/PROG/20261120-DZT-v0-19-adopted.md', 'pipes/DYAD/20261120-DZT-v0-19-adopted.md',
         'pipes/NUMGEN/20261120-DZT-v0-19-adopted.md']

def _load(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
R10 = _load('refresh_v0_10')   # Edit base class, h_l5_map, checker, pipe_states, git, sha, at, wjson, ROW
R13 = _load('refresh_v0_13')   # Edit with cut(), K1, LOC, k1_violations, node, RID
git, sha, at, wjson, h_l5_map, checker, pipe_states = R10.git, R10.sha, R10.at, R10.wjson, R10.h_l5_map, R10.checker, R10.pipe_states
K1, LOC, k1_violations, node, RID = R13.K1, R13.LOC, R13.k1_violations, R13.node, R13.RID

class Edit(R13.Edit):
    def rep(self, old, new, finding, where):
        R10.Edit.rep(self, old, new, finding, where); self.log[-1]['id'] = f'AR15-{len(self.log):03d}'

THM_NODE = (THM_HEAD + ' ∀p=4s≥12: |N_+(M_p)|=ℓ(p)²/2^{d_p}, d_p=φ(p)/4+[p=2^k]+[p=3·2^k]; ℓ(p)=ℓ if p=8ℓ^a (ℓ an odd prime, ℓ^a≡1 mod 4), ℓ(p)=1 otherwise; '
 'so the odd-prime anomalies are exactly p=8ℓ^a, ℓ^a≡1 mod 4 (20 for p≤1000; p=40 the only one on the 14-point table), with |N_+(M_{8ℓ^a})|=ℓ²/2^{φ(ℓ^a)}, and the denominator is always 2^{d_p}; '
 'the mod-4 gate is the order of L^{s−2} (for p=8q: q if q≡1 mod 4, 2q if q≡3 mod 4); proof by cyclotomic norms N(1−η)=Φ_n(1)^{φ(p)/φ(n)} on A_s=(I−1)L²(1−L^{s−2}) | '
 '¬ the sign of N_+(M_p) (not part of the statement); ¬ p=8 (Q₈=0, outside the statement); ¬ unconditional (the imported Dyadic closed form is assumed); ¬ a bearing on RH or prime distribution (SG-DZT-4) | '
 'contains as finite cases: DZT-ALG-CASCADE-NORM (p=12–64) and DZT-ALG-CASCADE-ANOMALY-SET (p≤1000) | closes DZT-OPEN-NORM-LAW (0B-R) | '
 'retires the earlier [HYP] reading of the mod-4 gate as the reality of ℚ(√q)⊂ℚ(ζ_q)⁺ (owner [SUPERSEDED] DZT19-C01: no quadratic subfield enters; fails at q=9, p=72) | '
 '<DYAD-THM-Q403-PHASELAW (the closed form of Q_p and M_p=Q_p/(iζ_p³)∈ℚ(ζ_p)⁺; owned by DYAD) | '
 'proof sources (owner §9): the recovered DZT proof notes (odd support; denominator), the LIT note DZT_NORM_LAW_PROOF_NOTE.md (rtg-lit 8e2fb5cb), the owner review records/dzt/DZT_NORM_LAW_OWNER_REVIEW.md, the independent review 5983698371; grade, RID and entry by edition: PI, 20 Nov 2026 | '
 'cert DZT-ART-NORMLAW-CHECK (evidence/dzt/norm_law_review/dzt_norm_law_review_check.py, in the repository: exact integer resultants for 12≤p≤4000, every norm of the proof and the law, signed products p≤1000, six negative controls; '
 'run for the owner review on 19 Nov 2026, not rerun here; a finite check, not the proof) @DZT§6.3')

IMPORT_NODE = ('*DZT:imports-dyad (import record; no DZT claim; grades are the owner\'s) | DZT §7 imports from DYAD v6.4.24 by owner RID only: DYAD-THM-Q403-PHASELAW, with its parts named without separate RIDs as DYAD App F classifies them '
 '(universal direction λ^{−s}=ζ_p^{−p/4}=−i ∀4|p; reality relation f^{W̄}_{(b,a)}=conj f^W_{(a,b)}, J(f^s)=(Jf)^s, J realized by σ₋₁; leading (0,3) accumulation Σ_{k=0}^{s−1}ζ_p^{−4k}=0 (s≥2), so Q_p is the subleading remainder and Q₈=0; '
 'remainder relation σ₋₁(A_p)=ζ_p^{−6}A_p; the closed form, DZT-checked against the extractor at p=12,16,20,24,40,44,60, source-reported) · DYAD-ART-Q403-EXTRACT (Case-V values p=8–64; correspondence by content only: '
 'DZT\'s hashes ecdb805f…05eac2 and 14526cf1…7bec16 name files not in the repository, no byte identity) · DYAD-ART-Q403-CERT (not in the repository, not rerun) · DYAD-ALG-B5-ALLP-NONVANISHING · DYAD-ALG-VANISH-B2/B3/B4 · DYAD-ALG-P6-FACEFLUX; '
 'the p=8 and p=12 cascade values have no owner RID and are cited as text; the note labels of the dzt-v0.8 text are gone from the owner text | @DZT§7')

def refresh(a: Edit):
    I, D, P = 'identity', 'DZT v0.19', 'pipes'
    G = 'reviewed item (grade, qualifier or diagnostic change)'
    # ---- identity ----
    a.rep('# RTG STATE ATLAS v0.14\n', '# RTG STATE ATLAS v0.15\n', I, 'title')
    a.rep('evidence/atlas/v0.14/source_manifest.json', 'evidence/atlas/v0.15/source_manifest.json', I, 'SOURCES header')
    a.rep('*END — RTG STATE ATLAS v0.14.', '*END — RTG STATE ATLAS v0.15.', I, 'end line')
    a.line('| DZT | RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN | v0.8 |', '| DZT | RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN | v0.19 | `dzt-v0.19` | canonical Tier 3 |', I, 'SOURCES row DZT')
    a.rep('· DZT v0.8 · AZ v0.10 Thread A.', '· DZT v0.19 (Methodology v1.4 declared; Level A) · AZ v0.10 Thread A.', I, 'D2 header, DZT')
    a.rep('DZT aliases [import-ref]=[DEF][scope: reference-only], [NUM diagnostic].)',
          'DZT alias [NUM diagnostic]=[NUM][scope: named diagnostic campaign]; DZT\'s [import-ref] is a reference label, not a status tag.)', LOC, 'D2 header: DZT tag aliases as the owner states them (Local Tag Aliases)')

    # ================= DZT (D2) =================
    a.sub_in_line('DYAD-THM-Q403-PHASELAW THM (proof: exact algebraic identity) |',
                  'DZT (prints the historical note label DYAD-THM-Q403-PHASE-ALLP, not an owner RID; L5 DZT.Q1)',
                  'DZT (the assumption of DZT-THM-CASCADE-NORM-LAW and of the norm object; cited by this RID at dzt-v0.19 §7, its parts without separate RIDs)', D, 'phase law: reverse relation toward DZT at the owner\'s §7')
    a.line('*DZT:imports-dyad-note THM(import; phantom RIDs !) |', IMPORT_NODE, D, 'DZT import record restated at §7: owner RIDs only')
    a.sub_in_line('DZT-ALG-P12-NORM ALG |', 'Mahler mechanism HYP only (DZT-RETRACT-MAHLER-RESULT retracted the RESULT voice)',
                  'the Mahler reading: its RESULT voice retracted (DZT-RETRACT-MAHLER-RESULT), its family form DZT-HYP-MAHLER-NEARMISS falsified at p=40; the value survives', G, 'p=12 norm: the Mahler reading traced to the FAIL record')
    a.line('*DZT:norm-object THM/ALG(import)·all p |',
           '*DZT:norm-object ALG (sc: object level, all p=4s≥12) | Q_p=iζ_p³M_p with M_p=Q_p/(iζ_p³)∈ℚ(ζ_p)⁺ (DYAD THM, imported) ⇒ N_+(M_p)∈ℚ well-defined for all p=4s≥12; M_p real, its sign not asserted; values and anomaly pattern: DZT-THM-CASCADE-NORM-LAW | <DYAD-THM-Q403-PHASELAW | @DZT§6.3',
           G, 'norm object: compound head unpacked into the owner\'s [ALG] (sc: object level); the imported factorization stays DYAD\'s [THM]')
    a.line('DZT-ALG-CASCADE-NORM ALG·validation table |',
           'DZT-ALG-CASCADE-NORM ALG·validation table p=12–64 (14 points) | |N_+(M_p)| (absolute values; the sign of N_+(M_p) is not determined by DZT), p=12,16,…,64: ¼, ⅛, ¼, ⅛, ⅛, 1/32, ⅛, 25/16, 1/32, 1/32, 1/64, 1/64, 1/16, 1/512; pure 2-power except p=40 (5²·2⁻⁴) | '
           'canonical computation: the p≤1000 closed-form audit (DZT-ALG-CASCADE-ANOMALY-SET); a finite case of DZT-THM-CASCADE-NORM-LAW | cert dzt_casev_norm_audit.py (DZT-ART-CASEV-AUDIT; exit 1 by design: falsifier fires at p=40) | @DZT§6.3',
           G, 'cascade norm: absolute values (owner v0.18), scope of the table, finite case of the theorem')
    a.sub_in_line('DZT-ALG-CASCADE-ANOMALY-SET ALG·finite horizon', ' (20 points), numerator exactly ℓ²', ' (20 points), |N_+| numerator exactly ℓ²', G, 'anomaly set: absolute values')
    a.sub_in_line('DZT-ALG-CASCADE-ANOMALY-SET ALG·finite horizon', ' | COR: "p=40 isolated" horizon-local; "every odd prime power" false (q≡3 mod 4: p=24,56,88,152,184,216 clean); no denominator law (2^{−φ(q)} fails) |',
                  ' | the p≤1000 case of DZT-THM-CASCADE-NORM-LAW | COR (of the imported note): "p=40 isolated" horizon-local; "every odd prime power" false (q≡3 mod 4: p=24,56,88,152,184,216 clean); '
                  'the note\'s value N_+=2^{−φ(q)} wrong (on the set only its denominator exponent is right: |N_+(M_{8ℓ^a})|=ℓ²/2^{φ(ℓ^a)}; denominators in general: DZT-THM-CASCADE-NORM-LAW) |', G, 'anomaly set: finite case of the theorem; the denominator correction as the owner states it')
    a.after_line('DZT-ALG-CASCADE-ANOMALY-SET ALG·finite horizon', [THM_NODE], D, 'new node: DZT-owned [THM] [assuming: DYAD-THM-Q403-PHASELAW]')
    a.drop_line('*DZT:mechanism HYP |', G, 'mod-4 [HYP] removed: owner [SUPERSEDED] DZT19-C01 (named in the theorem node)')
    a.drop_line('*DZT:p40-flag OBS(historical) |', D, 'p=40 courtesy flag removed: not in the owner text since v0.18')
    a.sub_in_line('*DYAD:OPEN9-micro ALG |', '(cascade boundary; no RID; DZT prints DYAD-ALG-CASCADE-P12, an unmatched consumer string, not an owner RID)',
                  '(cascade boundary; no RID; DZT cites it as text)', D, 'OPEN 9 micro: DZT no longer prints the unmatched string')
    a.rep('FAIL (DZT) | DZT-HYP-MAHLER-NEARMISS (2-power norm law) · "every odd prime power" anomaly reading · denominator law 2^{−φ(q)}\n',
          'FAIL (DZT) | DZT-HYP-MAHLER-NEARMISS (2-power norm law) · "every odd prime power" anomaly reading · the imported note\'s value N_+=2^{−φ(q)}\n', G, 'FAIL list: the wrong value, not a denominator law')
    a.sub_in_line('**arithmetic transforms** DZT-OPEN-REPRODUCTION-AUDIT (0A)',
                  'DZT-OPEN-NORM-LAW (0B-R) ACTIVE: prove/reject N_+(M_{8q}) has odd-prime support ⟺ q=ℓ^a, q≡1 mod 4, numerator ℓ² (DZT-native cyclotomic resultant identity for Res(Φ_{8q},A_s); falsifier: violation p≤1000 (none) or beyond)',
                  'DZT-OPEN-NORM-LAW (0B-R) CLOSED by DZT-THM-CASCADE-NORM-LAW (all p=4s≥12, assuming DYAD-THM-Q403-PHASELAW; D2.L2)', D, 'frontier: norm law closed, result named')
    a.sub_in_line('**DZT guards** SG-DZT-1', 'norm is rational per point, 2-power law falsified, no k_p formula;',
                  'the amplitude-norm law is [THM] only under DYAD-THM-Q403-PHASELAW and says nothing about the sign of N_+(M_p); the 2-power law is falsified;', D, 'DZT high-risk ledger at §5')
    # ---- L5 ----
    a.drop_line('H3 D-RID high — consumer strings that are not owner RIDs:', G, 'H3 retired (it summarised DZT.Q1 only)')
    a.drop_line('DZT.Q1 D-RID |', G, 'DZT.Q1 retired')
    a.drop_line('DZT.Q4 D-GRADE |', G, 'DZT.Q4 retired')
    a.drop_line('DZT.Q5 D-SCOPE |', G, 'DZT.Q5 retired')
    a.sub_in_line('METH.M1 D-GRADE (programme pattern):', 'persist in DZT, OPEN-M, FMS session labels (TDR-G v2.13 declares Methodology v1.4 and carries none)',
                  'persist in OPEN-M, FMS session labels (TDR-G v2.13 and DZT v0.19 declare Methodology v1.4 and carry none)', G, 'METH.M1: DZT leaves the row')
    a.sub_in_line('PROG.G6 D-STALE (owner-recorded):', 'not executed for Pre-Legacy, DZT, AZ (after that record, at the AZ edition of this snapshot:',
                  'not executed for Pre-Legacy, DZT, AZ (after that record, at the DZT edition of this snapshot: Methodology v1.4 declared, after a reactivation triage and the v0.18 corrections edition; at the AZ edition of this snapshot:', D, 'PROG.G6: DZT state after the Programme record')
    # ---- pipes census at the new snapshot ----
    a.line('NUMGEN.N-I1 D-LINK (pipe states, receiver side) |', 'NUMGEN.N-I1 D-LINK (pipe states, receiver side) | at the source snapshot 357b963, pipes_index --check passes with 147 items in 20 inboxes — 80 closed, 5 dispositioned, 62 open. Open at the snapshot, by receiver: '
           'DYAD (AZ v0.10, LIT reply on LH2012 Prop. 5.3 scope, DZT v0.19) · ER2B (OFN v0.11, DYAD N16–N21) · FMS (OFN v0.11, v0.12) · GEN (LIT Regge interface inputs, PROG v1.4, DYAD v6.4.24) · '
           'LIT (DYAD LH2012 use report, DZT norm-law use report, SAT coil physical-coil channel) · NUMGEN (TDR-G v2.12.14 and v2.12.15, RECOG v0.3.26 and v0.3.27, DYAD v6.4.23 and v6.4.24, OFN v0.11 and v0.12, PROG v1.4, DZT v0.18 and v0.19) · '
           'OFN (DYAD v6.4.23 and v6.4.24, GEN v2.10, TRIAD v1.7, PROG v1.4, RECOG v0.3.27, TDR-G v2.12.15 and v2.13, DZT v0.18) · PREL (SAT finding on K₃ degeneracy and lift) · '
           'PROG (SAT satellite interface, AZ v0.7, v0.8, v0.9 and v0.10, TDR-G v2.12.15 and v2.13, DZT v0.18 and v0.19) · RECOG (DYAD v6.4.24) · RER (RECOG v0.3.26, DYAD N16–N21) · '
           'RRF (RECOG v0.3.26, OFN v0.11 and v0.12, DYAD N16–N21, GEN v2.10, TRIAD v1.7) · TRIAD (DYAD bridge-note recovery, GEN 𝒫₄-identity and birth-symmetry answers, GEN v2.10, PROG v1.4, DYAD v6.4.24) · '
           'UVM (GEN κ_f/B_*/sourced-junction items, DYAD N16–N21, GEN v2.10, TRIAD v1.7). ATLAS, AZ, DZT and TDRG have no open inbox item. A filed item is not adopted use; each receiver decides at its own checkpoint (CONVENTIONS §7).', P, 'pipe census at 357b963')

STALE = [r'`dzt-v0\.8` \|', r'\| v0\.8 \| `dzt', r'DZT v0\.8', r'PHASE-ALLP', r'DYAD-ALG-PHASELAW', r'DYAD-CF-Q403', r'CASCADE-P12', r'CASCADE-Q4-03', r'DYAD-THM-P1\b', r'DYAD-THM-REALITY', r'DYAD-THM-LEAD',
         r'\bDZT\.Q[145]\b', r'\*DZT:mechanism', r'p40-flag', r'phantom RIDs', r'NORM-LAW \(0B-R\) ACTIVE', r'no denominator law', r'denominator law 2\^', r'no k_p formula', r'persist in DZT',
         r'Mahler mechanism HYP', r'THM/ALG', r'consumer strings that are not owner RIDs', r'evidence/atlas/v0\.14/', r'snapshot a5826ac']
def stale_editions(text):
    return [l[:90] for l in text.split('\n') if not l.startswith('*ATLAS:checked-') and any(re.search(p, l) for p in STALE)]

def scope_guards(text):
    bad = []; need = lambda cond, msg: None if cond else bad.append(msg)
    deps = lambda l, sig: [g for g in l.split(' | ') if g.startswith(sig)]
    th = node(text, THM_HEAD)
    need(th.rstrip().endswith('@DZT§6.3') and 'cert DZT-ART-NORMLAW-CHECK (' in th, 'theorem: DZT-owned, one node, owner locator')
    need('∀p=4s≥12: |N_+(M_p)|=ℓ(p)²/2^{d_p}, d_p=φ(p)/4+[p=2^k]+[p=3·2^k]' in th and 'ℓ^a≡1 mod 4' in th and '|N_+(M_{8ℓ^a})|=ℓ²/2^{φ(ℓ^a)}' in th, 'theorem: statement as the owner gives it')
    need('¬ the sign of N_+(M_p) (not part of the statement)' in th and '¬ p=8 (Q₈=0, outside the statement)' in th and '¬ unconditional (the imported Dyadic closed form is assumed)' in th, 'theorem: sign, p=8 and the assumption kept outside')
    need([g.split(' (')[0] for g in deps(th, '<')] == ['<DYAD-THM-Q403-PHASELAW'], 'theorem: one dependency, the Dyadic phase law')
    need('a finite check, not the proof' in th and 'closes DZT-OPEN-NORM-LAW (0B-R)' in th and 'DZT19-C01' in th, 'theorem: check is not the proof; closure and the retired reading named')
    need(len([l for l in text.split('\n') if re.match(r'(?:DZT|DYAD)-THM-CASCADE-NORM-LAW', l)]) == 1, 'theorem: one home')
    need(not [l for l in text.split('\n') if l.startswith('*DZT:mechanism')], 'mod-4 [HYP] not current')
    need(bool(node(text, 'DZT-HYP-MAHLER-NEARMISS FAIL |')) and 'DZT-HYP-MAHLER-NEARMISS (2-power norm law)' in node(text, 'FAIL (DZT) |'), 'FAIL record kept apart')
    cn = node(text, 'DZT-ALG-CASCADE-NORM ALG·validation table p=12–64 (14 points) |')
    need('|N_+(M_p)| (absolute values; the sign of N_+(M_p) is not determined by DZT)' in cn and 'a finite case of DZT-THM-CASCADE-NORM-LAW' in cn, 'cascade norm: absolute values, finite case')
    an = node(text, 'DZT-ALG-CASCADE-ANOMALY-SET ALG·finite horizon p≤1000 (249 points, 4|p) |')
    need('the p≤1000 case of DZT-THM-CASCADE-NORM-LAW' in an and '|N_+| numerator exactly ℓ²' in an and 'ℓ²/2^{φ(ℓ^a)}' in an, 'anomaly set: finite case, denominator correction')
    fr = node(text, '**arithmetic transforms** DZT-OPEN-REPRODUCTION-AUDIT (0A)')
    need('DZT-OPEN-NORM-LAW (0B-R) CLOSED by DZT-THM-CASCADE-NORM-LAW' in fr and fr.count('DZT-OPEN-NORM-LAW') == 1 and 'DZT-OPEN-LOCAL-FORMAL-ZETA (B1)' in fr and 'DZT-OPEN-ANALYTIC-ZETA (B2, deferred)' in fr, 'frontier: closed with result; B1, B2 open')
    no = node(text, '*DZT:norm-object ALG (sc: object level, all p=4s≥12) |'); need('its sign not asserted' in no, 'norm object: owner grade, sign not asserted')
    ph = node(text, 'DYAD-THM-Q403-PHASELAW THM (proof: exact algebraic identity) |')
    need('DZT (the assumption of DZT-THM-CASCADE-NORM-LAW' in ph and not any(s in ph for s in NOTE_STRINGS), 'phase law: reverse relation, no note string')
    im = node(text, '*DZT:imports-dyad (import record; no DZT claim; grades are the owner\'s) |')
    need(bool(im) and not any(s in im for s in NOTE_STRINGS) and 'no byte identity' in im, 'import record: owner RIDs only, no byte identity claimed')
    need('DZT' not in node(text, 'METH.M1 D-GRADE (programme pattern):').split('(TDR-G v2.13')[0], 'METH.M1 without DZT')
    need('at the DZT edition of this snapshot' in node(text, 'PROG.G6 D-STALE (owner-recorded):'), 'PROG.G6: DZT recorded')
    need(not [l for l in text.split('\n') if re.match(r'H3 ', l)], 'H3 retired')
    need(bool(node(text, 'AZ.A5 ~ D-LINK / SG trap:')) and bool(node(text, 'AZ.A5 ~ D-LINK / SG trap |')), 'AZ.A5 kept (both rows)')
    need('says nothing about the sign of N_+(M_p)' in node(text, '**DZT guards** SG-DZT-1'), 'high-risk: sign')
    return bad

def homes_check(text, new):
    bad = []; lines = text.split('\n')
    for r in sorted(new):
        if r not in HOMES: bad.append(('no declared home', r)); continue
        kind, pre = HOMES[r]; hl = [l for l in lines if l.startswith(pre)]
        if len(hl) != 1: bad.append(('home line count', r, len(hl))); continue
        if kind == 'node' and len([l for l in lines if re.match(re.escape(r) + r'(?![A-Za-z0-9-])', l)]) != 1: bad.append(('node count', r))
        if kind == 'cert' and (len(re.findall(r'cert ' + re.escape(r) + r'(?![A-Za-z0-9-])', text)) != 1 or ('cert ' + r) not in hl[0]): bad.append(('cert home', r))
    return bad

def main():
    snap = git('rev-parse', SNAPSHOT + '^{commit}').decode().strip()
    base = at(BASE_TAG, ATLAS).decode(); assert sha(base) == BASE_SHA
    assert sha(at(METHOD_TAG, 'atlas/RTG_STATE_ATLAS_METHOD.md')) == METHOD_SHA and at(snap, 'atlas/RTG_STATE_ATLAS_METHOD.md') == at(METHOD_TAG, 'atlas/RTG_STATE_ATLAS_METHOD.md')
    a = Edit(base); refresh(a); text = a.text
    assert not k1_violations(a.log), k1_violations(a.log)
    assert not stale_editions(text), stale_editions(text)
    assert not scope_guards(text), scope_guards(text)
    # ---- manifest ----
    old = json.loads(at(BASE_TAG, 'evidence/atlas/v0.14/source_manifest.json'))
    m = json.loads(json.dumps(old))
    for s in m['sources']:
        for k in [k for k in s if k.startswith('v0_13_')]: del s[k]
    m.update(atlas='v0.15', frozen_at='2026-11-21', repository_snapshot=snap, previous_atlas_tag=BASE_TAG, method_tag=METHOD_TAG, method_edition='v0.3', method_sha256=METHOD_SHA)
    for s in m['sources']:
        prev = next(x for x in old['sources'] if x['key'] == s['key'])
        s['v0_14_edition'] = prev['edition']; s['v0_14_input_sha256'] = prev['sha256']
        oldbytes = at(prev['tag'], prev['path']); assert sha(oldbytes) == prev['sha256'], s['key']
        if s['key'] in MOVED:
            mv = MOVED[s['key']]; data = at(mv['tag'], s['path'])
            s.update(edition=mv['edition'], tag=mv['tag'], commit=git('rev-parse', mv['tag'] + '^{commit}').decode().strip(), sha256=sha(data), authority=mv['authority'])
        data = at(s['tag'], s['path']); resolved = git('rev-parse', s['tag'] + '^{commit}').decode().strip()
        assert sha(data) == s['sha256'] and resolved == s['commit'], s['key']
        assert data == at(snap, s['path']), ('snapshot/tag divergence', s['key'])
        newest = git('tag', '--list', s['tag'].rsplit('-v', 1)[0] + '-v*', '--sort=v:refname').decode().split()[-1]
        assert newest == s['tag'], ('a newer source tag exists', s['key'], newest)
        s['v0_14_input_equality'] = 'EQUAL' if data == oldbytes else 'CHANGED'
    assert Counter(x['v0_14_input_equality'] for x in m['sources']) == {'EQUAL': 17, 'CHANGED': 1}
    assert {x['key'] for x in m['sources'] if x['v0_14_input_equality'] == 'CHANGED'} == set(MOVED)
    for k, h in SHAS.items(): assert next(s for s in m['sources'] if s['key'] == k)['sha256'] == h, k
    assert git('cat-file', '-t', 'dzt-v0.19').decode().strip() == 'tag'
    wjson(OUT / 'source_manifest.json', m)
    # ---- H -> L5 ----
    hm = h_l5_map(text); assert not hm['dangling'], hm['dangling']
    wjson(OUT / 'h_l5_map.json', dict(convention='Every HEADLINE line cites L5 row ids only (many-to-one allowed). High L5 rows cited by no H are listed here and dispositioned in the release record.', **hm))
    # ---- retired keys (cumulative) ----
    oldret = json.loads(at(BASE_TAG, 'evidence/atlas/v0.14/retired_l5_keys.json'))
    newret = {'DZT.Q1': 'DZT v0.18/v0.19 (dzt-v0.19 §7): the row recorded nine DYAD strings printed by DZT v0.8 §7 that are not owner RIDs. At dzt-v0.19 §7 cites DYAD v6.4.24 by owner RID only (DYAD-THM-Q403-PHASELAW, DYAD-ART-Q403-EXTRACT, DYAD-ART-Q403-CERT, DYAD-ALG-B5-ALLP-NONVANISHING, DYAD-ALG-VANISH-B2/B3/B4, DYAD-ALG-P6-FACEFLUX), names the parts of the phase law without separate RIDs as DYAD App F classifies them, and cites the p=12 value as text; none of the nine strings occurs in the owner text. Nothing of the row remains. H3, which summarised it, is retired with it.',
              'DZT.Q4': 'DZT v0.18 (Methodology v1.4 migration): the row recorded the compound grades [THM/ALG] and [HEUR/ALG finite horizon]. At dzt-v0.19 no compound grade token occurs; the norm object is [ALG] [scope: object-level, all p=4s≥12] with the imported factorization DYAD\'s [THM], and DZT-ALG-CASCADE-ANOMALY-SET is [ALG] [scope: finite horizon p≤1000] in every section (the only [HEUR] is the Dirichlet diagnostic of §1). Nothing of the row remains.',
              'DZT.Q5': 'DZT v0.18/v0.19 (§1): the row recorded that the §1 table covered p=12–52 against §6.3 p=12–64, and that §1 stated "pure 2-powers except p=40" without the p≤1000 correction. At dzt-v0.19 §1 states the validation table as p=12–64, 14 points, with the p≤1000 closed-form audit as the canonical computation, and states the all-p law with all 20 anomaly points p≤1000. Nothing of the row remains.'}
    for k in newret: assert not re.search(r'(?<![A-Za-z0-9_.-])' + re.escape(k) + r'(?![A-Za-z0-9_-])', text), k
    assert not set(newret) & set(oldret['retired'])
    retired = oldret['retired'] + list(newret) + [k.replace('.', ' ') for k in newret if '.' in k]
    wjson(OUT / 'retired_l5_keys.json', dict(retired=retired, note='Keys not reused; v0.15 reasons in dispositions.json.'))
    # ---- shared checker (Method §7) ----
    c = checker(); src = c.load_sources(m)
    cmap = json.loads(at(BASE_TAG, 'evidence/atlas/v0.14/coverage_map.json'))
    cmap.pop('_note_v0_14', None)
    cmap['_note_v0_15'] = 'coverage_map.json of atlas-v0.14, unchanged in its homes. The checker\'s coverage check extracts Dyadic RIDs only; the homes of the two DZT identifiers new since dzt-v0.8 are asserted by the builder (verification_summary.json, moved_source_homes). The Dyadic RIDs DZT newly cites at dzt-v0.19 §7 already have their Dyadic homes.'
    wjson(OUT / 'coverage_map.json', cmap)
    idmap = json.loads(at('atlas-v0.2', 'evidence/atlas/owner_identifier_map_v0_2.json'))
    report = c.run(text, m, src, cmap, idmap, retired)
    meta = dict(atlas=ATLAS, atlas_sha=sha(text), manifest='evidence/atlas/v0.15/source_manifest.json')
    c.write_report(report, str(OUT / 'atlas_check_report.md'), meta)
    wjson(OUT / 'atlas_check_report.json', dict(meta=meta, rows=report.rows))
    assert not report.fails(), report.fails()
    shared = c.self_test(m, src, cmap, idmap, retired, text)
    wjson(OUT / 'shared_controls.json', [dict(name=n, item=i, as_expected=bool(b)) for n, i, b in shared]); assert all(x[2] for x in shared), shared
    base_report = c.run(base, old, c.load_sources(old), json.loads(at(BASE_TAG, 'evidence/atlas/v0.14/coverage_map.json')), idmap, oldret['retired'])
    # ---- identifiers of the moved source ----
    d8 = at('dzt-v0.8', DZT_PATH).decode(); d19 = src['DZT']
    own = lambda t: {r for r in RID(t) if r.startswith('DZT-')}
    assert own(d8) <= own(d19), own(d8) - own(d19)
    new = own(d19) - own(d8)
    assert new == set(HOMES), (sorted(new - set(HOMES)), sorted(set(HOMES) - new))
    hc = homes_check(text, new); assert not hc, hc
    dyad_cited = sorted(r for r in RID(d19) - RID(d8) if r.startswith('DYAD-'))
    owner_facts = dict(
        dzt_methodology_v1_4='**DSN Methodology:** v1.4 (`methodology-v1.4`)' in d19,
        dzt_theorem_tags='`[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]` `[proof: written derivation]` `[RID: DZT-THM-CASCADE-NORM-LAW]`' in d19,
        dzt_theorem_formula='d_p=\\frac{\\varphi(p)}{4}+[p=2^k]+[p=3\\cdot2^k]' in d19 and '\\ell^a\\equiv1\\!\\pmod4' in d19 and '\\lvert N_+(M_{8\\ell^a})\\rvert=\\ell^2/2^{\\varphi(\\ell^a)}' in d19,
        dzt_sign_outside='The sign of $N_+(M_p)$ is not part of the statement.' in d19,
        dzt_p8_degeneracy='at $p=8$, $n=1$ and $Q_8=0$' in d19,
        dzt_gate_order='The mod-4 gate is the order of $L^{s-2}$' in d19,
        dzt_open_closed='[RID: DZT-OPEN-NORM-LAW] :: CLOSED' in d19,
        dzt_mechanism_superseded='`[SUPERSEDED]` **DZT19-C01**' in d19 and 'no quadratic subfield enters' in d19,
        dzt_fail_kept='`[FAIL | RID: DZT-HYP-MAHLER-NEARMISS]`' in d19 and '`[FAIL]` `[RID: DZT-HYP-MAHLER-NEARMISS]`' in d19,
        dzt_finite_cases='It contains DZT-ALG-CASCADE-NORM and DZT-ALG-CASCADE-ANOMALY-SET as finite cases.' in d19 and 'It is the $p\\le1000$ case of DZT-THM-CASCADE-NORM-LAW.' in d19,
        dzt_note_value='The note\'s formula $N_+=2^{-\\varphi(q)}$ is also wrong as a value' in d19 and 'only its denominator exponent is right' in d19,
        dzt_absolute_values='The values are absolute values' in d19 and 'the sign of $N_+(M_p)$ is not determined by DZT' in d19,
        dzt_norm_object='`[ALG]` `[scope: object-level, all p=4s≥12]`' in d19,
        dzt_no_compound=not re.search(r'\[[A-Z]{2,7}/[A-Z]{2,7}', d19),
        dzt_no_note_strings=not any(s.strip() in d19 for s in NOTE_STRINGS) and 'DYAD-THM-R]' not in d19,
        dzt_courtesy_gone='courtesy' not in d19,
        dzt_high_risk='a sign of $N_+(M_p)$ read off the tables or the law' in d19 and 'the law without its Dyadic assumption' in d19,
        dzt_check_registered='[RID: DZT-ART-NORMLAW-CHECK]' in d19 and 'a finite check, not the proof' in d19 and CHECK_SHA in d19,
        dzt_check_in_repo=sha(at(snap, CHECK_PATH)) == CHECK_SHA,
        dzt_p12_survives='survives the family falsification' in d19,
        dzt_s1_table='`[scope: validation table p=12–64, 14 points]`' in d19 and '(20 for $p\\le1000$; on the 14-point table only $p=40$)' in d19,
        dzt_import_pin='All imports are from `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 (`dyad-v6.4.24`)' in d19 and 'no byte identity is claimed' in d19,
        dzt_level_a='Maturity **Level A**' in d19,
        dzt_b1_b2_open=d19.count('Status: OPEN') == 2)
    assert all(owner_facts.values()), [k for k, v in owner_facts.items() if not v]
    for p in PATHS: assert at(snap, p), p
    n_snap, st_snap = pipe_states(snap); assert n_snap == 147 and st_snap == PIPE_SNAPSHOT, (n_snap, st_snap)
    # ---- dispositions ----
    def row(t, key):
        ls = [l for l in t.split('\n') if l.startswith(key + ' ')]; return '\n'.join(ls) if ls else None
    bl_ = base.split('\n'); i0 = bl_.index('### D2.L5 DIAGNOSTICS'); dztkeys = []
    for l in bl_[i0 + 1:]:
        if l.startswith('## ') or l.startswith('---'): break
        mm = R10.ROW.match(l)
        if mm and mm.group(1).startswith('DZT.'): dztkeys.append(mm.group(1))
    touched = list(dict.fromkeys(dztkeys + ['AZ.A5', 'METH.M1', 'PROG.G6', 'NUMGEN.N-I1']))
    disp = []
    for key in touched:
        o = row(base, key); n = row(text, key); assert o, key
        state = 'retired' if key in newret else ('retained' if n == o else 'reworded'); assert (n is None) == (key in newret), key
        why = [e['where'] for e in a.log if key in e['where'] or e['old'].startswith(key + ' ')]
        reason = newret.get(key) or ('reworded; operations: ' + '; '.join(why) if state == 'reworded' else
                 ('unchanged: AZ v0.10 and DZT v0.19 both keep the anomaly set p=8ℓ^a and the 4|q rule apart (SG-DZT-1, SG-AZ-7); the theorem does not create a relation' if key == 'AZ.A5' else 'unchanged: what it records is unchanged at the v0.15 sources'))
        disp.append(dict(key=key, disposition=state, reason=reason, previous_sha256=sha(o), current_sha256=sha(n) if n else None))
    disp.append(dict(key='H3', disposition='retired (headline)', reason='H3 summarised DZT.Q1 only (DZT\'s note strings; AZ and PROG already cited the owner RID). With DZT.Q1 retired nothing of it remains. H-numbers are display order only; H4–H12 keep theirs.',
                     previous_sha256=sha([l for l in base.split('\n') if l.startswith('H3 ')][0]), current_sha256=None))
    wjson(OUT / 'dispositions.json', disp)
    # ---- focused negative controls ----
    controls = []
    def ctl(cid, what, detected): controls.append(dict(id=cid, what=what, detected=bool(detected)))
    run = lambda t, with_sources=True: bool(c.run(t, m, src, cmap, idmap, retired, with_sources=with_sources).fails())
    def sw(old, new_, n=1):
        assert text.count(old) >= 1, old[:60]; return text.replace(old, new_, n)
    homes = lambda t: bool(homes_check(t, new))
    has = lambda msgs, msg: msg in msgs
    ctl('W1', 'the theorem without its Dyadic assumption', has(scope_guards(sw('¬ unconditional (the imported Dyadic closed form is assumed); ', '')), 'theorem: sign, p=8 and the assumption kept outside'))
    ctl('W2', 'a sign read into the theorem', has(scope_guards(sw('¬ the sign of N_+(M_p) (not part of the statement); ', '')), 'theorem: sign, p=8 and the assumption kept outside'))
    ctl('W3', 'the theorem extended to p=8', has(scope_guards(sw('¬ p=8 (Q₈=0, outside the statement); ', '')), 'theorem: sign, p=8 and the assumption kept outside'))
    ctl('W4', 'the finite check presented as the proof', has(scope_guards(sw('; a finite check, not the proof) @DZT§6.3', ') @DZT§6.3')), 'theorem: check is not the proof; closure and the retired reading named'))
    ctl('W5', 'the theorem made dependent on its own finite case', has(scope_guards(sw('| <DYAD-THM-Q403-PHASELAW (the closed form', '| <DZT-ALG-CASCADE-ANOMALY-SET | <DYAD-THM-Q403-PHASELAW (the closed form')), 'theorem: one dependency, the Dyadic phase law'))
    ctl('W6', 'the theorem under a DYAD locator', has(scope_guards(sw('a finite check, not the proof) @DZT§6.3', 'a finite check, not the proof) @DYAD§6.11')), 'theorem: DZT-owned, one node, owner locator'))
    ctl('W7', 'a second home for the theorem', has(scope_guards(text + 'DZT-THM-CASCADE-NORM-LAW THM | duplicate\n'), 'theorem: one home') and homes(text + 'DZT-THM-CASCADE-NORM-LAW THM | duplicate\n'))
    ctl('W8', 'the check artifact cited twice as a certificate', homes(sw('| cert dzt_casev_norm_audit.py (', '| cert DZT-ART-NORMLAW-CHECK | cert dzt_casev_norm_audit.py (')))
    ctl('W9', 'the mod-4 [HYP] restored as current', has(scope_guards(text + '*DZT:mechanism HYP | mod-4 gate = reality of ℚ(√q)\n'), 'mod-4 [HYP] not current') and stale_editions(text + '*DZT:mechanism HYP | mod-4 gate = reality of ℚ(√q)\n'))
    ctl('W10', 'the FAIL record dropped', has(scope_guards('\n'.join(l for l in text.split('\n') if not l.startswith('DZT-HYP-MAHLER-NEARMISS FAIL |'))), 'FAIL record kept apart'))
    ctl('W11', 'the norm law shown as still open', stale_editions(sw('DZT-OPEN-NORM-LAW (0B-R) CLOSED by DZT-THM-CASCADE-NORM-LAW', 'DZT-OPEN-NORM-LAW (0B-R) ACTIVE')) and has(scope_guards(sw('DZT-OPEN-NORM-LAW (0B-R) CLOSED by DZT-THM-CASCADE-NORM-LAW', 'DZT-OPEN-NORM-LAW (0B-R) ACTIVE')), 'frontier: closed with result; B1, B2 open'))
    ctl('W12', 'the closed frontier item listed twice', has(scope_guards(sw('· DZT-OPEN-LOCAL-FORMAL-ZETA (B1)', '· DZT-OPEN-NORM-LAW (0B-R) OPEN · DZT-OPEN-LOCAL-FORMAL-ZETA (B1)')), 'frontier: closed with result; B1, B2 open'))
    ctl('W13', '"no denominator law" restored', stale_editions(sw('the note\'s value N_+=2^{−φ(q)} wrong (on the set only', 'no denominator law (2^{−φ(q)} fails) (on the set only')))
    ctl('W14', 'the tabulated norms read as signed values', has(scope_guards(sw('|N_+(M_p)| (absolute values; the sign of N_+(M_p) is not determined by DZT), p=12', 'N_+(M_p), p=12')), 'cascade norm: absolute values, finite case'))
    ctl('W15', 'a note string restored on the phase-law reverse relation', stale_editions(sw('cited by this RID at dzt-v0.19 §7', 'cited as DYAD-THM-Q403-PHASE-ALLP at dzt-v0.19 §7')) and has(scope_guards(sw('cited by this RID at dzt-v0.19 §7', 'cited as DYAD-THM-Q403-PHASE-ALLP at dzt-v0.19 §7')), 'phase law: reverse relation, no note string'))
    ctl('W16', 'byte identity claimed for the Dyadic extractor', has(scope_guards(sw('name files not in the repository, no byte identity)', 'name files not in the repository)')), 'import record: owner RIDs only, no byte identity claimed'))
    ctl('W17', 'retired DZT.Q1 reused', run(text + 'DZT.Q1 D-RID: reused\n', False) and stale_editions(text + 'DZT.Q1 D-RID: reused\n'))
    ctl('W18', 'METH.M1 still lists DZT', stale_editions(sw('persist in OPEN-M, FMS session labels (TDR-G v2.13 and DZT v0.19', 'persist in DZT, OPEN-M, FMS session labels (TDR-G v2.13 and DZT v0.19')))
    ctl('W19', 'SOURCES row older than the manifest (DZT)', run(sw('| v0.19 | `dzt-v0.19` |', '| v0.8 | `dzt-v0.8` |')) and stale_editions(sw('| v0.19 | `dzt-v0.19` |', '| v0.8 | `dzt-v0.8` |')))
    ctl('W20', 'the compound head restored on the norm object', stale_editions(sw('*DZT:norm-object ALG (sc: object level, all p=4s≥12) |', '*DZT:norm-object THM/ALG(import)·all p |')))
    ctl('W21', 'AZ.A5 dropped', has(scope_guards('\n'.join(l for l in text.split('\n') if not l.startswith('AZ.A5 ~ D-LINK / SG trap:'))), 'AZ.A5 kept (both rows)'))
    ctl('W22', 'the sign caveat dropped from the high-risk ledger', has(scope_guards(sw(' and says nothing about the sign of N_+(M_p)', '')), 'high-risk: sign'))
    wjson(OUT / 'negative_controls.json', controls); assert all(x['detected'] for x in controls), [x for x in controls if not x['detected']]
    wjson(OUT / 'edit_log.json', a.log)
    r = Edit(base); refresh(r); assert r.text == text   # replay
    (ROOT / ATLAS).write_text(text, encoding='utf-8')
    unresolved = lambda rep: sum(1 for x in rep.rows if 'unresolved' in json.dumps(x, ensure_ascii=False).lower())
    summary = dict(status='DRAFT_REVIEW_READY', base_atlas=BASE_TAG, base_sha256=BASE_SHA, atlas_sha256=sha(text), atlas_bytes=len(text.encode()), atlas_lines=text.count('\n'),
                   base_bytes=len(base.encode()), base_lines=base.count('\n'), source_snapshot=snap, method=dict(tag=METHOD_TAG, sha256=METHOD_SHA), changed_sources=list(MOVED),
                   edit_operations=len(a.log), operations_by_finding=dict(Counter(e['finding'] for e in a.log)),
                   span_deletions_rule_4_1=dict(count=0, bytes_removed=0), span_deletions_rule_4_7=0,
                   retired_keys=list(newret), retired_headlines=['H3'], new_keys=[], moved_source_homes={r: dict(kind=k, home=p) for r, (k, p) in HOMES.items()},
                   new_identifiers=sorted(new), dyad_rids_newly_cited_by_dzt=dyad_cited, rids_at_tag=dict(DZT=len(RID(d19)), DZT_owned=len(own(d19))),
                   owner_facts=owner_facts, pipes=dict(items=n_snap, snapshot=st_snap), dispositions=dict(Counter(d['disposition'] for d in disp)),
                   shared_counts={ch: dict(report.count(ch)) for ch in c.CHECKS}, shared_counts_at_base={ch: dict(base_report.count(ch)) for ch in c.CHECKS},
                   shared_controls=len(shared), focused_controls=len(controls),
                   h_l5=dict(dangling=hm['dangling'], high_without_h=hm['high_l5_without_h'], l5_rows=hm['l5_rows']),
                   tool_sha256={'tools/atlas_check.py': sha((ROOT / 'tools/atlas_check.py').read_bytes()), 'evidence/atlas/build/refresh_v0_15.py': sha(Path(__file__).read_bytes()),
                                'evidence/atlas/build/refresh_v0_13.py': sha(Path(__file__).with_name('refresh_v0_13.py').read_bytes()),
                                'evidence/atlas/build/refresh_v0_10.py': sha(Path(__file__).with_name('refresh_v0_10.py').read_bytes())},
                   limitations=['Structural checks only; no owner certificate was rerun, and DZT-ART-NORMLAW-CHECK was not rerun here; the new identifiers are checked for presence in the tagged source and for one home each, not re-proved.',
                                'Impact refresh of one moved source; the other 17 sources were not re-extracted. DZT v0.19 was read in full; the v0.8→v0.18 changes were read through the owner text at v0.19, its Appendices A and B and the v0.18 and v0.19 release records.',
                                'The shared checker\'s coverage check extracts Dyadic RIDs only; the homes of the two DZT identifiers are asserted by this builder.',
                                'DYAD\'s OPEN 9 frontier line (near-cancellation of −13+15√3/2; exact large-p behaviour of |Q_p| OPEN) is a DYAD statement and is not changed; DZT\'s theorem is about |N_+(M_p)|, not |Q_p|.',
                                'H3 is retired and the other headlines keep their numbers (display order only).'])
    wjson(OUT / 'verification_summary.json', summary)
    print(json.dumps({k: v for k, v in summary.items() if k not in ('owner_facts', 'moved_source_homes', 'limitations')}, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
