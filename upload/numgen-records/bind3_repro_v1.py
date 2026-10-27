#!/usr/bin/env python3
# BIND3 independent reproduction — N=24, k=1, three-node no-birth
# Target: BIND3-CYCLE-N24K1 (RTG_DISCRETE_GENESIS_DSN v2.12/13, Sec 6.12)
# Conventions implemented from the DSN: CONV-TICK, defect band D_k,
# antipodal swap, CONV-P3CYC successor shift, path orientation rule.
import sys
from itertools import product

N=24
def sc(x,n=N):                      # signed_centered: representative in [-n/2, n/2)
    return ((x+n//2) % n) - n//2
def dist_anti(D,n=N):               # dist to N/2
    return abs(sc(D-n//2,n))
def sde(ta,tb,n=N):                 # signed_defect_error: signed offset of Delta from antipodal
    return sc((ta-tb)-n//2,n)

def step(state,k,tie_mode="inert"):
    """state=(th,dl) tuples len 3. Returns (newstate, ev) ev in {None,'swap','p3','tie','k3'}"""
    th,dl=state
    th=tuple((th[i]+dl[i])%N for i in range(3))        # 1. advance
    E=[(i,j) for i,j in ((0,1),(0,2),(1,2))            # 2-3. defect edges
       if dist_anti((th[i]-th[j])%N)<=k]
    old=dl; ev=None
    if len(E)==1:                                       # isolated edge -> antipodal swap
        i,j=E[0]; d=list(dl); d[i],d[j]=old[j],old[i]; dl=tuple(d); ev='swap'
    elif len(E)==2:                                     # P3 -> successor shift
        nodes=[x for e in E for x in e]
        c=[v for v in set(nodes) if nodes.count(v)==2][0]
        ends=sorted(v for v in set(nodes) if v!=c)
        path=[ends[0],c,ends[1]]
        S=sde(th[path[0]],th[path[1]])+sde(th[path[1]],th[path[2]])
        if S<0: path=path[::-1]
        elif S==0:
            Eend=sc(old[path[2]]-old[path[0]])
            if Eend<0: path=path[::-1]
            elif Eend==0:
                if tie_mode=="inert": return (th,dl),'tie'
                # alt: apply the listed orientation
        d=list(dl)
        for i,v in enumerate(path): d[v]=old[path[(i+1)%3]]
        dl=tuple(d); ev='p3'
    elif len(E)==3:
        ev='k3'
    return (th,dl),ev

def canon(s):
    th,dl=s
    return ((th[0]-th[1])%N,(th[0]-th[2])%N,(dl[0]-dl[1])%N,(dl[0]-dl[2])%N)

def orbit(state,k,tie_mode="inert",cap=20000):
    seen={}; seq=[]; s=state; t=0
    while t<cap:
        c=canon(s)
        if c in seen:
            pre=seen[c]; return pre, t-pre, seq
        seen[c]=t; s,ev=step(s,k,tie_mode); seq.append(ev); t+=1
    return None,None,seq

def ics(k):
    """retrigger-entry family: eps in B_k cap (B_k+d) if nonempty else B_k."""
    B=set(range(-k,k+1)); out=[]
    for d in range(-N//2,N//2):
        if d==0: continue
        ov=sorted(B & {b+d for b in B})
        if abs(sc(d))>2*k:            # one-pass supplementary family
            continue
        if not ov: continue
        for eps in ov:
            DAB=(N//2+eps)%N
            for DAC,dAC in product(range(N),repeat=2):
                th=(0,(0-DAB)%N,(0-DAC)%N)
                dl=(0,(0-d)%N,(0-dAC)%N)
                out.append(((th,dl),d,eps))
    return out

if __name__=="__main__":
    k=1
    I=ics(k)
    print(f"IC family size: {len(I)}   (DSN target 3456)")
    from collections import Counter
    bd=Counter(sc(d) for _,d,_ in I)
    print("  per-d IC counts:",dict(sorted(bd.items())))
    pers=[]; pres=[]; ties=0; k3=0; swaps_any=0; p3_any=0; dual=0
    ev_counts=[]
    for st,d,eps in I:
        pre,per,seq=orbit(st,k)
        if per is None: print("NO CYCLE"); sys.exit(1)
        cyc=seq[pre:pre+per]
        c=Counter(cyc); pers.append(per); pres.append(pre)
        ties+=c['tie']; k3+=c['k3']
        if c['swap']: swaps_any+=1
        if c['p3']: p3_any+=1
        if c['swap'] and c['p3']: dual+=1
        ev_counts.append((c['swap'],c['p3']))
    import statistics as S
    print(f"  median period {S.median(pers)}  max {max(pers)}  distinct {len(set(pers))}")
    print(f"  median preperiod {S.median(pres)}  max {max(pres)}")
    print(f"  dominant periods {[p for p,_ in Counter(pers).most_common(6)]}")
    print(f"  K3 components in cycles: {k3}   (DSN target 0)")
    print(f"  orientation ties encountered: {ties}")
    print(f"  ICs with swap in cycle {swaps_any}, with P3 {p3_any}, DUAL-ACTIVE {dual}")
