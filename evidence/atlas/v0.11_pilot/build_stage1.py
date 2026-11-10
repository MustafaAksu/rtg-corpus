#!/usr/bin/env python3
"""Atlas v0.11 D3 pilot, stage 1: six second-home record lines become typed cross-reference lines (not a compaction).
Base: atlas/RTG_STATE_ATLAS.md at atlas-v0.10. Output: stage-1 text and its movement map, both under this directory.
Run from the repository root: python3 -I evidence/atlas/v0.11_pilot/build_stage1.py
"""
import hashlib, json, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]; OUT = Path(__file__).resolve().parent
BASE_SHA = '443b5990e6082599d1f43fca7d4d24e512e7a632ec395aa56f05bed16f53dbf7'
REF = '(cross-domain reference, not a node; the node is in {d})'
# (line number in the base, expected SHA-256 prefix of the base line, base occurrence key, replacement line)
OPS = [
 (373, '07357b826616', 'RECOG-ALG-CHART-LAWS#1', '→ RECOG-ALG-CHART-LAWS ' + REF.format(d='D3') + ' | D2 use: chart laws of the finite normal-form jet J_NF (D2 notation; the same defined polynomial jet as J(z) of the node — not F̂, the raw jet or the archival Lie-gauge object) | chart phase coefficient opposite in sign to c_θ^(6); 245/216≠47/54 (SG-19) | <RECOG-ALG-CHART-LAWS (D3) | @RECOG§6.14'),
 (392, '7b9ec0236849', 'RECOG-THM-R9-MEMORY#1', '→ RECOG-THM-R9-MEMORY ' + REF.format(d='D3') + ' | D2 use: C_z-track retained-memory law M(z₀) behind the OPEN 3 / OPEN 21 return-phase results | Atlas reading, not owner text: resonant (0,5) slot carries the comparator-invisible phase | G=(1−2iτ)a₀₅/(1−6iτ) and its value: RECOG-ALG-LATTICE-MEMORY (D3) | ¬ physical inheritance; ¬ C_W^(h) | <RECOG-THM-R9-MEMORY (D3), RECOG-ALG-LATTICE-MEMORY (D3) | @RECOG§6.13a'),
 (419, 'b2ca3a7bfa0c', 'RECOG-THM-P2-HET#1', '→ RECOG-THM-P2-HET ' + REF.format(d='D3') + ' | D2 use: W^u_−(P₂)∖{P₂}⊂basin(P₁), entering the PRIM-CTR tube | <RECOG-THM-P2-HET (D3) | @RECOG§6.11'),
 (420, 'ea000995ffe1', 'RECOG-THM-P2-C0-FIRST#1', '→ RECOG-THM-P2-C0-FIRST ' + REF.format(d='D3') + ' | D2 use: first outward encounter of W^u_+(P₂) with C₀ unique and transverse, 2.03334<ρ*<2.03342 | <RECOG-THM-P2-C0-FIRST (D3) | @RECOG§6.11'),
 (462, '33985171274b', 'RECOG-ALG-NU3-CLOSED-FORM#1', '→ RECOG-ALG-NU3-CLOSED-FORM ' + REF.format(d='D3') + ' | D2 use: closed form of ν₃(λ) for the declared K_p family (Z-frame, cubic) | radial identity Re(λ̄ν₃(e^{iθ}))=−sin²(θ/2) and Re μ_p^Z=−p sin²(π/p)<0: *RECOG:radial-identity (D3); k_ret(p)=3 ∀p≥5: RECOG-ALG-NU3-NONVANISHING (D3) | ¬ universal healing across generators/amplitudes | <RECOG-ALG-NU3-CLOSED-FORM (D3), RECOG-ALG-NU3-NONVANISHING (D3) | @RECOG§6.10'),
 (1351, 'fc0cc8b3e3c6', 'NUMGEN-N3D-FINITE-CHAR#2', '→ NUMGEN-N3D-FINITE-CHAR ' + REF.format(d='D2') + " | D5 use: res_N:Ĝ→Ĉ_N, G_T/NG_T≅ℤ_N, N may be TDR-G's even phase size; pure representation theory | ¬ dynamics/coefficient/observable transfer, ¬ continuum limit (SG-NG-3/4) | <NUMGEN-N3D-FINITE-CHAR (D2) | @NUMGEN§6.4"),
]
REMAP = ['RECOG-ALG-CHART-LAWS', 'RECOG-THM-R9-MEMORY', 'RECOG-THM-P2-HET', 'RECOG-THM-P2-C0-FIRST', 'RECOG-ALG-NU3-CLOSED-FORM']   # full node: base #2 -> candidate #1
sha = lambda b: hashlib.sha256(b).hexdigest()
base = subprocess.check_output(['git', '-C', str(ROOT), 'show', 'atlas-v0.10:atlas/RTG_STATE_ATLAS.md']); assert sha(base) == BASE_SHA
lines = base.split(b'\n'); recs, ins = [], []
for n, h, key, new in OPS:
    assert sha(lines[n - 1]).startswith(h), (n, 'base line identity'); assert lines[n - 1].startswith(key.split('#')[0].encode() + b' ')
    lines[n - 1] = new.encode('utf-8')
    recs.append(dict(base=key, cand=None, reason='stage 1: second home of the claim replaced by a typed cross-reference (dispositions record §4)'))
    ins.append(dict(cand=f'L{n}', reason=f'stage 1: cross-reference line replacing {key}'))
for rid in REMAP: recs.append(dict(base=f'{rid}#2', cand=f'{rid}#1', reason='full node unchanged; it is the only record occurrence after stage 1'))
# two raw lines follow the full RECOG-THM-P2-C0-FIRST node; their anchor key is renumbered with it (#2 -> #1), so the tool wants them mapped
for n in (754, 755): recs.append(dict(base=f'L{n}', cand=f'L{n}', reason='raw line unchanged in place; its anchor record RECOG-THM-P2-C0-FIRST is renumbered #2 -> #1 by stage 1'))
cand = b'\n'.join(lines)
(OUT / 'RTG_STATE_ATLAS_stage1.md').write_bytes(cand)
mp = dict(base_sha256=BASE_SHA, candidate_sha256=sha(cand), stage='v0.11 D3 pilot, stage 1', records=recs, inserts=ins)
(OUT / 'stage1_movement_map.json').write_text(json.dumps(mp, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('stage1', sha(cand), len(cand), 'bytes; base', len(base))
