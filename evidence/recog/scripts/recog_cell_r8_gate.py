#!/usr/bin/env python3
"""
recog_cell_r8_gate.py — exit-coded audit gate for the R8 certificate (RECOG-THM-P2-HET).
Usage: python3 recog_cell_r8_gate.py recog_cell_r8_hetero_enclosure.py r8_cert.jsonl 4096
Checks (all must pass, exit 0):
 0 Stage 1 local quadratic-cusp lemma re-verified from the recorded delta, kappa (lam_+ must match the record)
 1 piece ids exactly 0..N-1, no omissions, no duplicates
 2 initial pieces tile [-delta, -delta/lam_+] exactly: exact-rational endpoints, contiguous, ordered
 3 every piece reached at least one leaf with Arb-certified 0 < Q_entry <= 1/625 (the transport aborts otherwise)
 4 every pre-entry enclosure had Arb-certified inf det DT > 0 (the transport aborts otherwise)
 5 backend is Arb (frames exact points, inverses enclosed) for every record
 6 every record carries the sha256 of the supplied transport script; one parameter set
The transport script's built-in `summary` mode is deprecated (a stale report line raises after its gates); use this gate.
"""
import sys, json, hashlib, importlib.util
from fractions import Fraction as F
tp, res, N = sys.argv[1], sys.argv[2], int(sys.argv[3])
spec = importlib.util.spec_from_file_location("r8", tp); r8 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r8)
lines = [json.loads(l) for l in open(res)]
metas = [m for m in lines if m.get('meta')]; recs = [r for r in lines if not r.get('meta')]
here = hashlib.sha256(open(tp, 'rb').read()).hexdigest()
g = {}
ids = [r['piece'] for r in recs]
g['1'] = sorted(ids) == list(range(N)) and len(ids) == N
g['6'] = {m['script_sha256'] for m in metas} == {here} and len({(m['delta'], m['kappa'], m['lam_plus'], m['npieces']) for m in metas}) == 1 and metas[0]['npieces'] == N
m0 = metas[0]; d, kap, lp = F(m0['delta']), F(m0['kappa']), F(m0['lam_plus'])
ok1, s1 = r8.stage1(d, kap); g['0'] = ok1 and s1['lam_p'] == lp
by = {r['piece']: r for r in recs}
g['2'] = g['1'] and F(by[0]['sa']) == -d and F(by[N-1]['sb']) == -d/lp and all(F(by[k]['sb']) == F(by[k+1]['sa']) for k in range(N-1)) and all(F(by[k]['sa']) < F(by[k]['sb']) for k in range(N))
g['3'] = all(r['ok'] and r['leaves'] >= 1 for r in recs) and min(r['q_lo'] for r in recs) > 0 and max(r['q_hi'] for r in recs) <= 1/625
g['4'] = all(r['ok'] for r in recs) and min(r['min_det'] for r in recs) > 0
g['5'] = all('arb' in m['backend'] for m in metas)
names = {'0': 'stage 1 lemma re-verified', '1': 'ids 0..N-1 exact', '2': 'exact tiling of the shell', '3': '0 < Q_entry <= 1/625 for every leaf',
         '4': 'inf det DT > 0 pre-entry', '5': 'Arb backend', '6': 'script hash + single parameter set'}
for k in sorted(g): print(f"[{'PASS' if g[k] else 'FAIL'}] {k} {names[k]}")
print(f"transport sha256 {here}; flint {m0['flint_version']}, {m0['prec_bits']} bits; delta={m0['delta']}, kappa={m0['kappa']}, pieces={N}")
print(f"steps to entry {min(r['max_steps'] for r in recs)}..{max(r['max_steps'] for r in recs)}; min det {min(r['min_det'] for r in recs):.6f}; "
      f"max width {max(r['max_width'] for r in recs):.3e}; splits {sum(r['splits'] for r in recs)}; entry Q in [{min(r['q_lo'] for r in recs):.10f}, {max(r['q_hi'] for r in recs):.10f}]")
if 'dyad_dsn_v6_4_10_sha256' in m0: print(f"Dyadic DSN v6.4.10 sha256 {m0['dyad_dsn_v6_4_10_sha256']}")
ok = all(g.values()); print("R8 CERTIFICATE PASS" if ok else "R8 CERTIFICATE FAIL"); sys.exit(0 if ok else 1)
