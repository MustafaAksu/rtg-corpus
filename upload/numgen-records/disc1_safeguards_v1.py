#!/usr/bin/env python3
# =============================================================================
# DISC-1 PROVENANCE SAFEGUARDS  v1  — archived as explicit artifacts
# =============================================================================
# Two checks were reported in NG_DISC1_RESULT_v1 but not archived as runnable
# scripts. Both are reproduced here so the exposed artifact set is sufficient
# to re-verify the DISC-1 result without trusting the memo.
#   S1  exhaustive ONE-STEP differential test of the reproduced transition core
#       against genesis_mode_b_mc_v18.py over all 24^4 reduced states, for
#       every k in {0,1,2,3}.  Run BEFORE the enumeration was generated.
#   S2  independent recount of every DISC-1D passing seed at all four k by
#       driving v18.step_universe directly and reading v18's own
#       single_edge_swaps / path_interactions counters.
#   S3  the within-band and fixed-period controls for audit item 3.
# Requires v18.py (a copy of genesis_mode_b_mc_v18.py) alongside.
# Exit 0 iff all three pass.
# =============================================================================
import sys, json, itertools
from math import gcd
from collections import Counter
sys.argv=['x']
import v18
N=24
FAIL=[]
def ck(n,c):
    print(f"[{'PASS' if c else 'FAIL'}] {n}")
    if not c: FAIL.append(n)

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
            elif Ee==0: return (th,dl),'tie'
        d=list(dl)
        for i,v in enumerate(path): d[v]=old[path[(i+1)%3]]
        return (th,tuple(d)),'p3'
    if len(E)==3: return (th,dl),'k3'
    return (th,dl),None
def canon(s):
    th,dl=s
    return ((th[0]-th[1])%N,(th[0]-th[2])%N,(dl[0]-dl[1])%N,(dl[0]-dl[2])%N)
def lift(r,c=0,b=0):
    DAB,DAC,dAB,dAC=r
    return ((c,(c-DAB)%N,(c-DAC)%N),(b,(b-dAB)%N,(b-dAC)%N))

# ---------------- S1 exhaustive one-step differential ----------------------
def v18_step(r,k):
    DAB,DAC,dAB,dAC=r
    u=v18.Universe(N=N,k=k,theta={0:0,1:(0-DAB)%N,2:(0-DAC)%N},
                             delta={0:0,1:(0-dAB)%N,2:(0-dAC)%N})
    v18.step_universe(u,multistar_policy="bound_symmetric")
    t,d=u.theta,u.delta
    return ((t[0]-t[1])%N,(t[0]-t[2])%N,(d[0]-d[1])%N,(d[0]-d[2])%N)
allr=list(itertools.product(range(N),repeat=4))
tot=0
for k in (0,1,2,3):
    bad=sum(1 for r in allr if canon(step(lift(r),k)[0])!=v18_step(r,k))
    print(f"    k={k}: {bad} mismatches / {len(allr)}")
    tot+=bad
ck(f"S1 reproduced core is ONE-STEP IDENTICAL to v18 over all {len(allr)} "
   f"reduced states for every k in {{0,1,2,3}} ({tot} total mismatches)", tot==0)

# ---------------- S2 v18 recount of the passing seeds ----------------------
recs=json.load(open('bind3_disc1_enumeration_k0123.json'))
tab={(r['seed_id'],r['k']):r for r in recs}
def red(r):
    a,b=r['n_swap'],r['n_p3']
    if a<=0 or b<=0: return None
    g=gcd(a,b); return (a//g,b//g)
base=[s for s in {r['seed_id'] for r in recs} if tab[(s,1)]['dual_active']]
E=set(s for s in base if tab[(s,2)]['dual_active'] and red(tab[(s,2)])==red(tab[(s,1)]))
P=sorted(s for s in E if tab[(s,3)]['dual_active'] and red(tab[(s,3)])!=red(tab[(s,1)]))
def v18_counts(r,k,cap=40000):
    DAB,DAC,dAB,dAC=r
    u=v18.Universe(N=N,k=k,theta={0:0,1:(0-DAB)%N,2:(0-DAC)%N},
                             delta={0:0,1:(0-dAB)%N,2:(0-dAC)%N})
    seen={};hist=[];t=0
    while t<cap:
        key=((u.theta[0]-u.theta[1])%N,(u.theta[0]-u.theta[2])%N,
             (u.delta[0]-u.delta[1])%N,(u.delta[0]-u.delta[2])%N)
        if key in seen: break
        seen[key]=t
        s0,p0=u.single_edge_swaps,u.path_interactions
        v18.step_universe(u,multistar_policy="bound_symmetric")
        hist.append((u.single_edge_swaps-s0,u.path_interactions-p0)); t+=1
    key=((u.theta[0]-u.theta[1])%N,(u.theta[0]-u.theta[2])%N,
         (u.delta[0]-u.delta[1])%N,(u.delta[0]-u.delta[2])%N)
    pre=seen[key]
    return sum(a for a,_ in hist[pre:t]), sum(b for _,b in hist[pre:t])
bad=0
for s in P:
    rr=tuple(int(x) for x in s.split('_')[1:])
    for k in (0,1,2,3):
        if (a:=v18_counts(rr,k))!=(tab[(s,k)]['n_swap'],tab[(s,k)]['n_p3']): bad+=1
ck(f"S2 independent v18 recount of all {len(P)} DISC-1D passing seeds at four "
   f"k, via v18's own single_edge_swaps / path_interactions counters: "
   f"{bad} mismatches", bad==0 and len(P)==22)

# ---------------- S3 item-3 controls, incl. the fixed-period control -------
L=lambda s,k: tab[(s,k)]['cycle_len']
rows=[]
for lo,hi in [(0,20),(20,60),(60,150)]:
    sim=[s for s in base if lo<=L(s,1)<hi and sum(red(tab[(s,1)]))<=4]
    cpx=[s for s in base if lo<=L(s,1)<hi and sum(red(tab[(s,1)]))>4]
    rows.append((f"[{lo},{hi})",sum(s in E for s in sim),len(sim),
                 sum(s in E for s in cpx),len(cpx)))
p54s=[s for s in base if L(s,1)==54 and sum(red(tab[(s,1)]))<=4]
p54c=[s for s in base if L(s,1)==54 and sum(red(tab[(s,1)]))>4]
rows.append(("period 54 exactly",sum(s in E for s in p54s),len(p54s),
             sum(s in E for s in p54c),len(p54c)))
for lbl,a,b,c,d in rows:
    print(f"    {lbl:20s} simple {a:3d}/{b:4d}   complex {c:3d}/{d:4d}")
ck("S3 class simplicity predicts survival within every short-period band and "
   "at exactly period 54, where both class types coexist — residual period "
   "distribution inside the <150 window does not rescue the "
   "'just short cycles' explanation", all(c==0 and a>0 for _,a,b,c,d in rows))

# ---------------- transport archetypes ------------------------------------
arch=Counter(tuple((tab[(s,k)]['n_swap'],tab[(s,k)]['n_p3']) for k in (1,2,3)) for s in P)
print("\n  transport archetypes among the 22 passes (k=1,2,3 event counts):")
for a,n in arch.items(): print(f"    {a}  x{n}")
ck(f"S4 the 22 passing seeds reduce to {len(arch)} event-count transport "
   f"archetypes, one per admitted class — prevalence, not 22 independent "
   f"mechanisms", len(arch)==2)
print("-"*70)
if FAIL: print("FAILURES:",FAIL); sys.exit(1)
print("RESULT: ALL SAFEGUARDS PASS.")
sys.exit(0)
