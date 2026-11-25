"""
open_m_2f_zh2_weighted.py — OPEN-M-2F step 2: z_h^2-weighted band loading
[RID: UVM-OPEN-2F]
f_4D^{zh} = sum_{internal, x>=0.70} z_h^2 / sum_{internal} z_h^2   (corridor source frac)
f_3D^{zh} = sum_{internal, 0.28<=x<0.70} z_h^2 / sum_{internal} z_h^2 (window source frac)
Raw corridor fraction is geometry; f^{zh} is the actual SOURCE amplitude admissibility.
x_link is Pre-Legacy-ladder-normalized (ERR-M-2F-CONV resolved).
"""
import numpy as np, sys, os
def band(x): return 0 if x<0.28 else 1 if x<0.70 else 2 if x<1.55 else 3
SERIES=[("T80","open_m_2d_seed_001_rank_2_mid40_to_T80_minref"),
        ("T89","open_m_2d_seed_001_rank_2_T80_to_T89_2e_loadtest"),
        ("T90","open_m_2d_seed_001_rank_2_T80_to_T90_2e_loadtest"),
        ("T91","open_m_2d_seed_001_rank_2_T80_to_T91_2e_loadtest"),
        ("T92","open_m_2d_seed_001_rank_2_T80_to_T92_2e_loadtest"),
        ("T93","open_m_2d_seed_001_rank_2_T80_to_T93_2e_loadtest"),
        ("T94","open_m_2d_seed_001_rank_2_T80_to_T94_2e_loadtest"),
        ("T100","open_m_2d_seed_001_rank_2_T80_to_T100_gentle"),
        ("T120","open_m_2d_seed_001_rank_2_v13_loose_T80_to_T120")]
ok=True
def check(n,c):
    global ok; print(f"[{'PASS' if c else 'FAIL'}] {n}"); ok&=bool(c)
def hodge(GE,GF,z):
    nodes=sorted({n for e in GE for n in e}); nid={u:i for i,u in enumerate(nodes)}
    eidx={e:k for k,e in enumerate(GE)}; nE,nF,N=len(GE),len(GF),len(nodes)
    B0=np.zeros((nE,N))
    for k,(a,b) in enumerate(GE):
        u,v=(a,b) if a<b else (b,a); B0[k,nid[u]]=-1; B0[k,nid[v]]=1
    B1=np.zeros((nF,nE))
    for fi,(a,b,c) in enumerate(GF):
        for (u,v) in [(a,b),(b,c),(c,a)]: B1[fi,eidx[tuple(sorted((u,v)))]]=1.0 if u<v else -1.0
    M=np.vstack([B0.T,B1]); _,S,Vt=np.linalg.svd(M)
    dimH=int(nE-np.sum(S>max(M.shape)*np.finfo(float).eps*S[0]))
    return (Vt[nE-dimH:].T@(Vt[nE-dimH:].T.T@z)) if dimH>0 else np.zeros(nE)

print("OPEN-M-2F step2 :: z_h^2-weighted band source fractions\n")
print(f"{'stage':5s} {'rawCorr':>7s} {'f3D_zh':>7s} {'f4D_zh':>7s} {'f2D_zh':>7s} {'sig_h_int':>9s} {'nm':>3s}")
rows=[]
for tag,stub in SERIES:
    fp=f"/mnt/user-data/uploads/{stub}_microstate.npz"
    if not os.path.exists(fp): continue
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
    is_int=np.array([inc.get(e,0)>=2 for e in GE]); nm=sum(1 for v in inc.values() if v>2)
    zh=hodge(GE,GF,z)
    bands=np.array([band(xv) for xv in x])
    zh2=zh**2; tot=zh2[is_int].sum()
    f2=zh2[is_int&(bands==0)].sum()/max(tot,1e-30)
    f3=zh2[is_int&(bands==1)].sum()/max(tot,1e-30)
    f4=zh2[is_int&(bands>=2)].sum()/max(tot,1e-30)
    rawcorr=(is_int&(bands>=2)).sum()/max(is_int.sum(),1)
    shi=np.std(zh[is_int]) if is_int.sum()>1 else 0
    print(f"{tag:5s} {rawcorr:7.3f} {f3:7.3f} {f4:7.3f} {f2:7.3f} {shi:9.4f} {nm:3d}")
    rows.append((tag,rawcorr,f3,f4,shi,nm))
f4s=np.array([r[3] for r in rows]); raws=np.array([r[1] for r in rows])
print(f"\nf4D_zh in near-pass packs: T100={[r for r in rows if r[0]=='T100'][0][3]:.3f}  "
      f"T120={[r for r in rows if r[0]=='T120'][0][3]:.3f}")
print(f"mean f4D_zh - mean rawCorr = {f4s.mean()-raws.mean():+.3f}  "
      f"({'loading concentrates IN corridor' if f4s.mean()>raws.mean() else 'loading avoids corridor'})")
check("step2 computed across series", len(rows)>=7)
print("\nALL CHECKS:","PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
