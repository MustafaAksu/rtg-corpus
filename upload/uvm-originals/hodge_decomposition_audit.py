"""
hodge_decomposition_audit.py — Legacy Screening-Theorem decomposition on 2D packs
[RID candidate: UVM-NUM-2D-HODGE]
z = z_exact (im d0, gauge-screenable gradient) + z_curl (im d1^T, face-sourced)
  + z_harm (harmonic, dim = E - rank(B0) - rank(B1) = beta1 of 2-complex;
    Four Pillars: UNSCREENABLE = topological matter).
Tests: (1) harmonic dimension per pack; (2) variance split (eta_irr-style);
(3) is the dirty pack's defect-adjacent sigma excess harmonic-borne?
(4) clean vs dirty harmonic content on internal edges.
"""
import numpy as np, sys
PACKS={
 "RUN10 (nm=7, pass)":"/mnt/user-data/uploads/open_m_2d_seed_001_rank_2_v13_loose_T80_to_T120_auditpack.npz",
 "RUN11 (nm=0, fail)":"/mnt/user-data/uploads/open_m_2d_seed_001_rank_2_T120_defect_polish_auditpack.npz",
 "T80r0v2 (clean)":"/mnt/user-data/uploads/open_m_2d_seed_001_rank_0_v13_loose_T80_v2_auditpack.npz"}
ok=True
def check(n,c):
    global ok; print(f"[{'PASS' if c else 'FAIL'}] {n}"); ok&=bool(c)
for tag,path in PACKS.items():
    d=np.load(path,allow_pickle=True)
    E=d["edges"].astype(int); F=d["faces"].astype(int); z=d["z_edge_centered"].astype(float)
    nodes=sorted(set(E.flatten().tolist())); nid={u:i for i,u in enumerate(nodes)}
    N,nE,nF=len(nodes),len(E),len(F)
    key={(min(a,b),max(a,b)):k for k,(a,b) in enumerate(E)}
    B0=np.zeros((nE,N))           # gradient: (d0 phi)_e = phi_v - phi_u for e=(u,v), u<v order
    for k,(a,b) in enumerate(E):
        u,v=(a,b) if a<b else (b,a)
        B0[k,nid[u]]=-1; B0[k,nid[v]]=+1
    B1=np.zeros((nF,nE))          # curl: oriented triangle sum
    for fi,(a,b,c) in enumerate(F):
        for (u,v) in [(a,b),(b,c),(c,a)]:
            k=key[(min(u,v),max(u,v))]
            B1[fi,k]= 1.0 if u<v else -1.0
    # projections via least squares
    ze=B0@np.linalg.lstsq(B0,z,rcond=None)[0]
    zc=B1.T@np.linalg.lstsq(B1.T,z-ze,rcond=None)[0]
    zh=z-ze-zc
    # orthogonality + dimension certificates
    r0=np.linalg.matrix_rank(B0); r1=np.linalg.matrix_rank(B1)
    dimh=nE-r0-r1
    check(f"{tag}: components orthogonal (|<ze,zh>|,|<zc,zh>| < 1e-8)",
          abs(ze@zh)<1e-8 and abs(zc@zh)<1e-8)
    IE={tuple(sorted(p)) for p in d["internal_edges"].astype(int).tolist()}
    is_int=np.array([tuple(sorted(E[k].tolist())) in IE for k in range(nE)])
    vt=z@z
    print(f"--- {tag}: N={N} E={nE} F={nF}  graph_b1={nE-N+1}  rank(B1)={r1}  HARMONIC DIM = {dimh}")
    print(f"    variance split: exact {ze@ze/vt:.3f}  curl {zc@zc/vt:.3f}  harmonic {zh@zh/vt:.3f}"
          f"   (eta_irr-style = curl+harm = {(zc@zc+zh@zh)/vt:.3f})")
    print(f"    internal sigma: total {np.std(z[is_int]):.4f}  exact-part {np.std(ze[is_int]):.4f}"
          f"  curl-part {np.std(zc[is_int]):.4f}  harm-part {np.std(zh[is_int]):.4f}")
    # defect-adjacency overlap for RUN10
    inc=np.zeros(nE,int)
    for (a,b,c) in F:
        for (u,v) in [(a,b),(b,c),(c,a)]: inc[key[(min(u,v),max(u,v))]]+=1
    if (inc>=3).sum()>0:
        nmn=set(E[inc>=3].flatten().tolist())
        adj=np.array([(E[k,0] in nmn or E[k,1] in nmn) for k in range(nE)])
        for nm_,comp in [("exact",ze),("curl",zc),("harm",zh)]:
            print(f"    defect-adjacent internal sigma[{nm_}] = {np.std(comp[is_int&adj]):.4f}"
                  f"   web-core internal sigma[{nm_}] = {np.std(comp[is_int&~adj]):.4f}")
print("\nALL CHECKS:","PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
