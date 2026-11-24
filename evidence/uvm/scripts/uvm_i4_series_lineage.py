"""
uvm_i4_series_lineage.py -- [SESSION] lineage facts for the nine open_m_2f_trajectory.py SERIES packs

Reads, from a directory holding the PI-supplied upload/uvm-i4-microstates files:
  * the grown_faces of the nine SERIES microstates (allow_pickle=False) and prints
    the face-set overlap matrix |F_row & F_col| / |F_row| and consecutive nesting;
  * step 81 of the T93 and T100 growth logs;
  * created_at and input_cluster from the T80/T93/T100 audit-pack JSONs and the
    T100 cluster JSON.
No ESM computation. Usage: python3 -I uvm_i4_series_lineage.py <dir>
"""
import sys, os, json, csv, numpy as np
D = sys.argv[1]; P = 'open_m_2d_seed_001_rank_2_'
S = [("T80","mid40_to_T80_minref"),("T89","T80_to_T89_2e_loadtest"),("T90","T80_to_T90_2e_loadtest"),
     ("T91","T80_to_T91_2e_loadtest"),("T92","T80_to_T92_2e_loadtest"),("T93","T80_to_T93_2e_loadtest"),
     ("T94","T80_to_T94_2e_loadtest"),("T100","T80_to_T100_gentle"),("T120","v13_loose_T80_to_T120")]
F = {}
for t, s in S:
    d = np.load(os.path.join(D, f'{P}{s}_microstate.npz'), allow_pickle=False)
    F[t] = {tuple(sorted(map(int, f))) for f in d['grown_faces']}
tags = [t for t, _ in S]
print('face-set overlap |F_row & F_col| / |F_row|')
print('      ' + ' '.join(f'{t:>5s}' for t in tags))
for a in tags:
    print(f'{a:5s} ' + ' '.join(f'{len(F[a] & F[b]) / len(F[a]):5.2f}' for b in tags))
for i in range(len(tags) - 1):
    a, b = tags[i], tags[i + 1]
    print(f'{a}->{b}: nested={F[a] <= F[b]} shared={len(F[a] & F[b])}/{len(F[a])}')
print('\ngrowth log, first row (step 81):')
for s in ("T80_to_T93_2e_loadtest", "T80_to_T100_gentle"):
    with open(os.path.join(D, f'{P}{s}_growth_log.csv'), newline='') as fh:
        row = next(csv.DictReader(fh))
    print(f"  {s:24s} step={row['step']} Q={row['Q']} C={row['C']} nm={row['nm']}")
print('\nprovenance metadata:')
for s in ("mid40_to_T80_minref", "T80_to_T93_2e_loadtest", "T80_to_T100_gentle"):
    m = json.load(open(os.path.join(D, f'{P}{s}_auditpack.json'), encoding='utf-8'))['meta']
    print(f"  {s:24s} auditpack created_at={m['created_at']}")
g = json.load(open(os.path.join(D, 'grown_cluster_v13_rank2_T80_to_T100_gentle.json'), encoding='utf-8'))
print(f"  T80_to_T100_gentle input_cluster={g['params']['input_cluster']}")
