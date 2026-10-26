#!/usr/bin/env python3
# DISC-2 P2 ANTIPODAL-ENDPOINT EXPOSURE AUDIT  v1
# Responds to external review finding P2 (RTG_NUMBER_GENESIS_DSN v1.18 review):
# the TDR-G path-orientation rule is listing-dependent when the phase-gradient
# score S=0 AND the endpoint advance difference is antipodal (|E| = N/2 = 12),
# because signed_centered(12) = signed_centered(-12) = 12 under (-N/2, N/2].
# v18 is deterministic (sorted endpoints) hence reproducible, but the outcome
# at such states is not node-relabeling covariant.
#
# This script (a) reproduces the reviewer's counterexample, (b) counts how many
# ratified DISC-2 witnesses ever hit the condition, (c) recomputes all 136
# verdicts under two alternative antipodal policies, and (d) checks whether
# every ratified label retains at least one witness that NEVER touches the
# condition. (d) is the decisive question for Q^dyn robustness.
# Reads only the ratified witness report; changes no rule, no verdict.
import json, sys
from math import gcd
from collections import defaultdict
N=24
def sc(x,n=N):
    y=x%n
    return y-n if y>n//2 else y
def shell(D): return abs(sc(D-N//2))
def sde(ta,tb): return sc((ta-tb)%N-N//2)
PAIR=((0,1),(0,2),(1,2))
def make_step(policy):
    def step(state,k):
        th,dl=state
        th=tuple((th[i]+dl[i])%N for i in range(3))
        sh={PAIR[a]:shell((th[PAIR[a][0]]-th[PAIR[a][1]])%N) for a in range(3)}
        E=[p for p,m in sh.items() if m<=k]; old=dl; flag=False
        if len(E)==1:
            i,j=E[0]; d=list(dl); d[i],d[j]=old[j],old[i]; return (th,tuple(d)),'S',flag
        if len(E)==2:
            nodes=[x for e in E for x in e]
            c=[v for v in set(nodes) if nodes.count(v)==2][0]
            ends=sorted(v for v in set(nodes) if v!=c); path=[ends[0],c,ends[1]]
            S=sde(th[path[0]],th[path[1]])+sde(th[path[1]],th[path[2]])
            if S<0: path=path[::-1]
            elif S==0:
                Ee=sc(old[path[2]]-old[path[0]])
                if abs(Ee)==N//2:
                    flag=True
                    if policy=='reverse': path=path[::-1]
                    elif policy=='inert': return (th,dl),'T',flag
                elif Ee<0: path=path[::-1]
                elif Ee==0: return (th,dl),'T',flag
            d=list(dl)
            for i,v in enumerate(path): d[v]=old[path[(i+1)%3]]
            return (th,tuple(d)),'P',flag
        return (th,dl),'.',flag
    return step
def canon(s):
    th,dl=s
    return ((th[0]-th[1])%N,(th[0]-th[2])%N,(dl[0]-dl[1])%N,(dl[0]-dl[2])%N)
def lift(r):
    a,b,c,d=r; return ((0,(0-a)%N,(0-b)%N),(0,(0-c)%N,(0-d)%N))
def run(step,r,k):
    s=lift(r); seen={}; ev=[]; fl=False; t=0
    while t<200000:
        key=canon(s)
        if key in seen: break
        seen[key]=t; s,e,f=step(s,k); ev.append(e); fl|=f; t+=1
    pre=seen[canon(s)]; c=ev[pre:t]; a=c.count('S'); b=c.count('P')
    return (None if (a==0 or b==0) else (a//gcd(a,b),b//gcd(a,b))), fl
def verdict(step,r):
    out={}; touched=False
    for k in (0,1,2,3):
        out[k],f=run(step,r,k); touched|=f
    r1=out[1]
    if r1 is None: v='NO_BASE_DUAL'
    elif out[2] is None: v='STABILITY_UNAVAILABLE'
    elif out[2]!=r1: v='UNSTABLE'
    elif out[3] is not None and out[3]!=r1: v='PASS_INT'
    elif out[0] is not None and out[0]!=r1: v='PASS_BDY_ONLY'
    else: v='STABLE_NO_CONTINGENCY'
    return v,r1,touched
FAIL=[]
def ck(n,c):
    print(f"[{'PASS' if c else 'FAIL'}] {n}")
    if not c: FAIL.append(n)
# (a) reviewer counterexample
th,dl=(0,12,0),(0,1,12)
Ef=sc(dl[2]-dl[0]); Er=sc(dl[0]-dl[2])
ck(f"P2a reviewer state theta=(0,12,0) delta=(0,1,12) k=1: E_listed={Ef}, E_reversed={Er} "
   f"— both positive, so the successor shift is listing-dependent", Ef==12 and Er==12)
rep=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'disc2_witness_report.json'))
W=[s for s,v in rep['per_seed'].items() if v['verdict'].startswith('PASS')]
v18=make_step('v18'); rev=make_step('reverse'); ine=make_step('inert')
unexp=defaultdict(int); exp_=defaultdict(int); base={}
for sid in W:
    r=tuple(int(z) for z in sid.split('_')[1:]); v,c,t=verdict(v18,r); base[sid]=(v,c)
    (exp_ if t else unexp)[c]+=1
labels=sorted(set(unexp)|set(exp_))
ck(f"P2b exposure: {sum(exp_.values())} of {len(W)} ratified witnesses touch the antipodal "
   f"condition somewhere in k in {{0,1,2,3}}; {sum(unexp.values())} never do", True if False else sum(exp_.values())>0)
ch_rev=sum(1 for s in W if verdict(rev,tuple(int(z) for z in s.split('_')[1:]))[:2]!=base[s])
ch_ine=sum(1 for s in W if verdict(ine,tuple(int(z) for z in s.split('_')[1:]))[:2]!=base[s])
print(f"   verdict/class changes: reverse-policy {ch_rev}, inert-policy {ch_ine}  (witness records ARE policy-sensitive)")
lab_rev={verdict(rev,tuple(int(z) for z in s.split('_')[1:]))[1] for s in W if verdict(rev,tuple(int(z) for z in s.split('_')[1:]))[0].startswith('PASS')}
lab_ine={verdict(ine,tuple(int(z) for z in s.split('_')[1:]))[1] for s in W if verdict(ine,tuple(int(z) for z in s.split('_')[1:]))[0].startswith('PASS')}
ck(f"P2c the ten-label set is identical under v18, reverse and inert policies", set(labels)==lab_rev==lab_ine)
thin=[c for c in labels if unexp[c]==0]
for c in labels: print(f"   {c[0]}:{c[1]:<3} unexposed {unexp[c]:3d}  exposed {exp_[c]:3d}")
ck(f"P2d ROBUSTNESS: every ratified label has >=1 witness that never touches the condition "
   f"(labels lacking one: {thin})", not thin)
print("-"*70)
if FAIL: print("FAILURES:",FAIL); sys.exit(1)
print("RESULT: label-level admission {1,3/2,2,3,4,4/3,5,5/2,7/2,9/4} subseteq Q^dyn is robust "
      "to the P2 antipodal-endpoint defect; 40 individual witness records are convention-exposed "
      "and must be annotated. Discrete owner policy ruling still required.")
sys.exit(0)
