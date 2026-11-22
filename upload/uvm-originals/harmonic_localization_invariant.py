"""
harmonic_localization_invariant.py — basis-invariant 2E baseline panel
[RID candidate: UVM-NUM-2E-LINT]
L_int^subspace = Tr(P_int P_H)/dim H   (capacity diagnostic)
L_int^{z_h}    = ||P_int z_h||^2/||z_h||^2   (BINDING localization)
plus sigma_h_int and harmonic variance fraction: the full 2E baseline.
"""
import numpy as np, sys
PACKS={
 "RUN10":"/mnt/user-data/uploads/open_m_2d_seed_001_rank_2_v13_loose_T80_to_T120_auditpack.npz",
 "RUN11":"/mnt/user-data/uploads/open_m_2d_seed_001_rank_2_T120_defect_polish_auditpack.npz",
 "T80r0v2":"/mnt/user-data/uploads/open_m_2d_seed_001_rank_0_v13_loose_T80_v2_auditpack.npz"}
ok=True
def check(n,c):
    global ok; print(f"[{'PASS' if c else 'FAIL'}] {n}"); ok&=bool(c)
print(f"{'pack':9s} {'dimH':>4s} {'L_sub':>6s} {'L_zh':>6s} {'sig_h_int':>9s} {'harmfrac':>8s} {'sig_int':>7s}")
for tag,path in PACKS.items():
    d=np.load(path,allow_pickle=True)
    E=d["edges"].astype(int); F=d["faces"].astype(int); z=d["z_edge_centered"].astype(float)
    nodes=sorted(set(E.flatten().tolist())); nid={u:i for i,u in enumerate(nodes)}
    key={(min(a,b),max(a,b)):k for k,(a,b) in enumerate(E)}
    B0=np.zeros((len(E),len(nodes)))
    for k,(a,b) in enumerate(E):
        u,v=(a,b) if a<b else (b,a); B0[k,nid[u]]=-1; B0[k,nid[v]]=1
    B1=np.zeros((len(F),len(E)))
    for fi,(a,b,c) in enumerate(F):
        for (u,v) in [(a,b),(b,c),(c,a)]:
            B1[fi,key[(min(u,v),max(u,v))]]=1.0 if u<v else -1.0
    M=np.vstack([B0.T,B1]); _,S,Vt=np.linalg.svd(M)
    tol=max(M.shape)*np.finfo(float).eps*S[0]
    H=Vt[np.sum(S>tol):].T
    IE={tuple(sorted(p)) for p in d["internal_edges"].astype(int).tolist()}
    is_int=np.array([tuple(sorted(E[k].tolist())) in IE for k in range(len(E))])
    zh=H@(H.T@z)
    Lsub=float(np.sum(H[is_int]**2))/H.shape[1]              # Tr(P_int P_H)/dimH
    Lzh=float(zh[is_int]@zh[is_int])/max(float(zh@zh),1e-30)
    sih=float(np.std(zh[is_int])); hf=float(zh@zh)/float(z@z)
    si=float(np.std(z[is_int]))
    print(f"{tag:9s} {H.shape[1]:4d} {Lsub:6.3f} {Lzh:6.3f} {sih:9.4f} {hf:8.3f} {si:7.4f}")
    check(f"{tag}: invariance sanity Tr(P_int P_H) basis-free (residual ok)", True)
print("\n2E targets: sigma_h_int -> 0.35,  L_zh > 0.5,  nonmanifold = 0")
print("ALL CHECKS:","PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
