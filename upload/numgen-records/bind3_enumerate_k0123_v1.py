#!/usr/bin/env python3
# =============================================================================
# BIND3 FROZEN-PANEL ENUMERATION  k in {0,1,2,3}   —  DISC-1 input generator
# =============================================================================
# Prerequisites, both satisfied before this ran:
#   * BIND3-CYCLE-N24K1 reproduced exactly (bind3_repro_v5.py, exit 0)
#   * reproduced core is ONE-STEP IDENTICAL to genesis_mode_b_mc_v18.py over
#     all 24^4 reduced states for every k in {0,1,2,3} (0 mismatches)
# Frozen engineering constraints (per PI, not decided here):
#   * the SAME frozen 3456 raw k=1 seed panel at every k; no k-specific family
#   * per (seed_id,k): eventual exact cycle, counts taken CYCLE-ONLY (post-preperiod)
#   * dual_active = (n_swap>0 and n_p3>0); records retained when false
#   * seed_id is tied to the raw reduced state, so transport is literal
#   * NO bond-transfer classification is computed or exported
# Emits the declared DISC-1 contract consumed by disc1_analysis_harness_v1.py.
# =============================================================================
import sys, json
from itertools import product
from collections import Counter
N=24
def sc(x,n=N):
    y=x%n
    return y-n if y>n//2 else y
def da(D): return abs(sc(D-N//2))
def sde(ta,tb): return sc((ta-tb)%N-N//2)

def step(state,k):
    th,dl=state
    th=tuple((th[i]+dl[i])%N for i in range(3))
    E=[(i,j) for i,j in ((0,1),(0,2),(1,2)) if da((th[i]-th[j])%N)<=k]
    old=dl
    if len(E)==1:
        i,j=E[0]; d=list(dl); d[i],d[j]=old[j],old[i]; return (th,tuple(d)),'swap'
    if len(E)==2:
        nodes=[x for e in E for x in e]
        c=[v for v in set(nodes) if nodes.count(v)==2][0]
        ends=sorted(v for v in set(nodes) if v!=c); path=[ends[0],c,ends[1]]
        S=sde(th[path[0]],th[path[1]])+sde(th[path[1]],th[path[2]])
        if S<0: path=path[::-1]
        elif S==0:
            Ee=sc(old[path[2]]-old[path[0]])
            if Ee<0: path=path[::-1]
            elif Ee==0: return (th,dl),'tie'          # bound_symmetric: inert
        d=list(dl)
        for i,v in enumerate(path): d[v]=old[path[(i+1)%3]]
        return (th,tuple(d)),'p3'
    if len(E)==3: return (th,dl),'k3'
    return (th,dl),None

def canon(s):
    th,dl=s
    return ((th[0]-th[1])%N,(th[0]-th[2])%N,(dl[0]-dl[1])%N,(dl[0]-dl[2])%N)
def lift(r):
    DAB,DAC,dAB,dAC=r
    return ((0,(0-DAB)%N,(0-DAC)%N),(0,(0-dAB)%N,(0-dAC)%N))

def frozen_panel(k_ref=1):
    """The frozen raw k=1 retrigger-entry panel. Generated ONCE, reused at every k."""
    B=set(range(-k_ref,k_ref+1)); out=[]
    for d in range(-N//2,N//2):
        if d==0 or abs(sc(d))>2*k_ref: continue
        for eps in sorted(B & {b+d for b in B}):
            DAB=(N//2+eps)%N
            for DAC,dAC in product(range(N),repeat=2):
                r=(DAB,DAC,(-d)%N,(-dAC)%N)
                out.append((f"s_{r[0]}_{r[1]}_{r[2]}_{r[3]}", r))
    return out

def cycle_counts(r,k,cap=40000):
    s=lift(r); seen={}; seq=[]; t=0
    while t<cap:
        c=canon(s)
        if c in seen: break
        seen[c]=t; s,ev=step(s,k); seq.append(ev); t+=1
    pre=seen[canon(s)]; cyc=seq[pre:t]; C=Counter(cyc)
    return C['swap'], C['p3'], t-pre, pre

if __name__=="__main__":
    panel=frozen_panel()
    assert len(panel)==3456, len(panel)
    assert len({sid for sid,_ in panel})==3456, "seed ids must be unique"
    recs=[]
    for k in (0,1,2,3):
        for sid,r in panel:
            a,b,per,pre=cycle_counts(r,k)
            recs.append({"seed_id":sid,"k":k,"dual_active":(a>0 and b>0),
                         "n_swap":a,"n_p3":b,"cycle_len":per,"preperiod":pre})
    json.dump(recs,open("bind3_disc1_enumeration_k0123.json","w"))
    print(f"records: {len(recs)}  (3456 seeds x 4 k)")
    for k in (0,1,2,3):
        R=[x for x in recs if x["k"]==k]
        dact=[x for x in R if x["dual_active"]]
        from math import gcd
        cl=Counter(tuple(sorted(((x["n_swap"]//gcd(x["n_swap"],x["n_p3"])),
                                 (x["n_p3"]//gcd(x["n_swap"],x["n_p3"]))) for _ in [0]))
                   for x in dact)
        red=Counter((x["n_swap"]//gcd(x["n_swap"],x["n_p3"]),
                     x["n_p3"]//gcd(x["n_swap"],x["n_p3"])) for x in dact)
        print(f"  k={k}: dual-active {len(dact):4d}/3456   distinct reduced classes "
              f"{len(red):3d}   top {red.most_common(5)}")
