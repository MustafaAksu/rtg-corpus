"""
open_m_2e_panel.py — canonical OPEN-M-2E audit panel (one pack -> full panel)
[RID candidate: UVM-ENG-2E-PANEL]
Usage: python open_m_2e_panel.py <auditpack.npz> [<previous_stage_pack.npz>]

Frozen 2E criteria (RESULT-M-2E-LINT pre-registration):
  nonmanifold = 0
  L_int^{z_h} > 0.5            (binding localization)
  sigma_h_int in 0.28-0.35     (0.28 empirical floor / 0.35 conservative)
  sigma_int >= 0.8 as CONSEQUENCE (reported, never optimized)
  density guard E_bnd/E_int <= 1.2
  SG-M-14: internal identity change <= 10% per stage (if previous pack given)
Panel: beta1, dimH, sigma_h_int, L_zh, L_sub, harm fraction, sigma_int(+SE),
       nonmanifold, density ratio, overlap.
"""
import numpy as np, sys
def load(path):
    d=np.load(path,allow_pickle=True)
    E=d["edges"].astype(int); F=d["faces"].astype(int); z=d["z_edge_centered"].astype(float)
    nodes=sorted(set(E.flatten().tolist())); nid={u:i for i,u in enumerate(nodes)}
    key={(min(a,b),max(a,b)):k for k,(a,b) in enumerate(E)}
    B0=np.zeros((len(E),len(nodes)))
    for k,(a,b) in enumerate(E):
        u,v=(a,b) if a<b else (b,a); B0[k,nid[u]]=-1; B0[k,nid[v]]=1
    B1=np.zeros((len(F),len(E)))
    inc=np.zeros(len(E),int)
    for fi,(a,b,c) in enumerate(F):
        for (u,v) in [(a,b),(b,c),(c,a)]:
            kk=key[(min(u,v),max(u,v))]; B1[fi,kk]=1.0 if u<v else -1.0; inc[kk]+=1
    IE={tuple(sorted(p)) for p in d["internal_edges"].astype(int).tolist()}
    is_int=np.array([tuple(sorted(E[k].tolist())) in IE for k in range(len(E))])
    return dict(E=E,F=F,z=z,B0=B0,B1=B1,inc=inc,is_int=is_int,iedges=IE,
                nbnd=int((~is_int).sum()),nint=int(is_int.sum()),
                N=len(nodes),comps=len(set(d["comp_ids"].tolist())) if "comp_ids" in d.files else 1)
def panel(p):
    M=np.vstack([p["B0"].T,p["B1"]]); _,S,Vt=np.linalg.svd(M)
    H=Vt[np.sum(S>max(M.shape)*np.finfo(float).eps*S[0]):].T
    z=p["z"]; ii=p["is_int"]
    zh=H@(H.T@z)
    out={}
    out["beta1_graph"]=len(p["E"])-p["N"]+p["comps"]
    out["dimH"]=H.shape[1]
    out["L_sub"]=float(np.sum(H[ii]**2))/max(H.shape[1],1)
    out["L_zh"]=float(zh[ii]@zh[ii])/max(float(zh@zh),1e-30)
    out["sigma_h_int"]=float(np.std(zh[ii]))
    out["harm_frac"]=float(zh@zh)/float(z@z)
    out["sigma_int"]=float(np.std(z[ii])); out["SE"]=out["sigma_int"]/np.sqrt(2*ii.sum())
    out["nonmanifold"]=int((p["inc"]>=3).sum())
    out["density"]=p["nbnd"]/max(p["nint"],1)
    return out
p=load(sys.argv[1]); P=panel(p)
print(f"== OPEN-M-2E PANEL :: {sys.argv[1].split('/')[-1]} ==")
for k,v in P.items(): print(f"  {k:12s} = {v:.4f}" if isinstance(v,float) else f"  {k:12s} = {v}")
verdict=[]
verdict.append(("nonmanifold=0", P["nonmanifold"]==0))
verdict.append(("L_zh>0.5", P["L_zh"]>0.5))
verdict.append(("sigma_h_int>=0.28 (floor)", P["sigma_h_int"]>=0.28))
verdict.append(("density<=1.2", P["density"]<=1.2))
verdict.append(("[consequence] sigma_int>=0.8", P["sigma_int"]>=0.8))
if len(sys.argv)>2:
    prev=load(sys.argv[2])
    ov=len(p["iedges"]&prev["iedges"])/max(len(prev["iedges"]),1)
    print(f"  SG-M-14 internal identity retention vs previous stage = {ov:.3f}")
    verdict.append(("SG-M-14 retention>=0.9", ov>=0.9))
print("-- criteria --")
allpass=True
for name,c in verdict:
    print(f"  [{'PASS' if c else 'FAIL'}] {name}"); allpass&=c
print(f"== 2E VERDICT: {'A-CANDIDATE' if allpass else 'not yet'} ==")
sys.exit(0)
