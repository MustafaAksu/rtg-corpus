"""
open_m_2f_trajectory.py — OPEN-M-2F trajectory test across a growth series
[RID: UVM-OPEN-2F]  Does internal harmonic loading rise WITH corridor fraction
(x_link>=0.70) along a single growth trajectory? Within-object test (the n=3
snapshot test could not separate trajectory from seed/topology differences).
"""
import numpy as np, sys, os
def band(x): return 0 if x<0.28 else 1 if x<0.70 else 2 if x<1.55 else 3
SERIES=[("T80",  "open_m_2d_seed_001_rank_2_mid40_to_T80_minref"),
        ("T89",  "open_m_2d_seed_001_rank_2_T80_to_T89_2e_loadtest"),
        ("T90",  "open_m_2d_seed_001_rank_2_T80_to_T90_2e_loadtest"),
        ("T91",  "open_m_2d_seed_001_rank_2_T80_to_T91_2e_loadtest"),
        ("T92",  "open_m_2d_seed_001_rank_2_T80_to_T92_2e_loadtest"),
        ("T93",  "open_m_2d_seed_001_rank_2_T80_to_T93_2e_loadtest"),
        ("T94",  "open_m_2d_seed_001_rank_2_T80_to_T94_2e_loadtest"),
        ("T100", "open_m_2d_seed_001_rank_2_T80_to_T100_gentle"),
        ("T120", "open_m_2d_seed_001_rank_2_v13_loose_T80_to_T120")]
ok=True
def check(n,c):
    global ok; print(f"[{'PASS' if c else 'FAIL'}] {n}"); ok&=bool(c)

def hodge_panel(GE,GF,z,is_int):
    nodes=sorted({n for e in GE for n in e}); nid={u:i for i,u in enumerate(nodes)}
    eidx={e:k for k,e in enumerate(GE)}; nE,nF,N=len(GE),len(GF),len(nodes)
    B0=np.zeros((nE,N))
    for k,(a,b) in enumerate(GE):
        u,v=(a,b) if a<b else (b,a); B0[k,nid[u]]=-1; B0[k,nid[v]]=1
    B1=np.zeros((nF,nE))
    for fi,(a,b,c) in enumerate(GF):
        for (u,v) in [(a,b),(b,c),(c,a)]:
            B1[fi,eidx[tuple(sorted((u,v)))]]=1.0 if u<v else -1.0
    M=np.vstack([B0.T,B1]); _,S,Vt=np.linalg.svd(M)
    dimH=int(nE-np.sum(S>max(M.shape)*np.finfo(float).eps*S[0]))
    zh=np.zeros(nE)
    if dimH>0:
        H=Vt[nE-dimH:].T; zh=H@(H.T@z)
    return dimH,zh

print("OPEN-M-2F trajectory :: corridor fraction vs harmonic loading along growth\n")
print(f"{'stage':5s} {'nint':>4s} {'corrFrac':>8s} {'sig_h_int':>9s} {'sig_h_corr':>10s} {'sig_h_win':>9s} {'nm':>3s} {'dimH':>4s}")
rows=[]
for tag,stub in SERIES:
    fp=f"/mnt/user-data/uploads/{stub}_microstate.npz"
    if not os.path.exists(fp): print(f"{tag}: missing"); continue
    ms=np.load(fp,allow_pickle=True)
    fe=[tuple(sorted((int(a),int(b)))) for a,b in ms["edges"]]
    xf={e:float(ms["x_link"][i]) for i,e in enumerate(fe)}
    GE=[tuple(sorted((int(a),int(b)))) for a,b in ms["grown_edges"]]
    GF=[tuple(sorted((int(a),int(b),int(c)))) for a,b,c in ms["grown_faces"]]
    z=ms["z_edge_centered"].astype(float)
    x=np.array([xf.get(e,np.nan) for e in GE])
    inc={}
    for (a,b,c) in GF:
        for (u,v) in [(a,b),(b,c),(c,a)]:
            k=tuple(sorted((u,v))); inc[k]=inc.get(k,0)+1
    is_int=np.array([inc.get(e,0)>=2 for e in GE])
    nm=sum(1 for v in inc.values() if v>2)
    dimH,zh=hodge_panel(GE,GF,z,is_int)
    bands=np.array([band(xv) for xv in x])
    corr=is_int&(bands>=2); win=is_int&(bands==1)
    cf=corr.sum()/max(is_int.sum(),1)
    sh_int=np.std(zh[is_int]) if is_int.sum()>1 else 0
    sh_corr=np.std(zh[corr]) if corr.sum()>1 else float('nan')
    sh_win=np.std(zh[win]) if win.sum()>1 else float('nan')
    print(f"{tag:5s} {int(is_int.sum()):4d} {cf:8.3f} {sh_int:9.4f} {sh_corr:10.4f} {sh_win:9.4f} {nm:3d} {dimH:4d}")
    rows.append((tag,cf,sh_int,sh_corr,nm))
cfs=np.array([r[1] for r in rows]); shs=np.array([r[2] for r in rows])
nms=np.array([float(r[4]) for r in rows])
print(f"\ncorr(corridorFrac, sigma_h_int) along trajectory = {np.corrcoef(cfs,shs)[0,1]:+.3f}")
print(f"corr(corridorFrac, nonmanifold)  along trajectory = {np.corrcoef(cfs,nms)[0,1]:+.3f}")
print(f"corr(sigma_h_int, nonmanifold)    along trajectory = {np.corrcoef(shs,nms)[0,1]:+.3f}")
check("trajectory computed for full series", len(rows)>=7)
print("\nALL CHECKS:","PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
