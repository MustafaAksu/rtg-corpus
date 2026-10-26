#!/usr/bin/env python3
# =============================================================================
# BIND3 INDEPENDENT REPRODUCTION  v5 — REPRODUCTION ACHIEVED   —  N=24, three-node no-birth
# Target: BIND3-CYCLE-N24K1 (RTG_DISCRETE_GENESIS_DSN v2.12/13 Sec 6.12)
# v1 -> v2, per review:
#   (a) IC generator extended to the supplementary |d|_c>2k one-pass family, so
#       the 1728-per-row counts are REPRODUCED rather than claimed algebraically.
#   (b) the convention sweep is included here as executable code; in v1 it was
#       run ad hoc and reported only in the memo.
#   (e) [COR] v1 used the WRONG IC-STAGE SIGN PAIRING. The owner defines
#       d_AB = delta_A - delta_B (LEM-SPECCONS) and a swap sends d -> -d, so
#       eps' = eps - d is consistent with d being the PRE-SWAP relative advance.
#       v1 paired eps with d_AB = +d; v2/v3 pair it with d_AB = -d, which is
#       correct if the exported retrigger-entry state is the POST-SWAP member
#       of the dyad cycle. The owner calls these only "post-advance BIND3 ICs"
#       and does not document that stage conversion, so this is EVIDENCE for
#       the post-swap reading, not an owner-text identity.
# v3 -> v4: [COR] signed_centered boundary convention corrected against the
#       v18 source (genesis_mode_b_mc_v18.py, lines 38-46): the representative
#       lies in (-N/2, N/2], not [-N/2, N/2). The two differ at exactly one
#       argument, x = N/2 = 12 -- the antipodal boundary. v18 confirmed:
#       signed_defect_error = signed_centered((ti-tj)%N - N//2, N) (identical
#       to the "offset" variant); endpoints sorted (identical); balanced
#       double-tie returns None -> inert under bind_ties (identical).
# v2 -> v3, per review: A3 provenance split (three declared lifts is what the
#       expression decides; the all-lift statement is the memo [ALG] theorem);
#       A4 Boolean widened to cover every clause of its PASS string (median
#       preperiod and K3 now actually tested); A2 wording no longer calls the
#       extrapolated range "the full one-pass family".
#   (c) the common-token-shift quotient is CHECKED exhaustively over the whole
#       reduced space instead of being asserted as SG-2 gauge. It is a derived
#       no-birth dynamical symmetry, not the stated global-phase gauge.
#   (d) balanced path-tie is NOT an under-determined slot: the owner specifies
#       ties inert under bound_symmetric (LEM-SPECCONS). Retained as the single
#       canonical behaviour; the sweep varies it only as a sensitivity probe.
# Exit 0 iff the reproduced items pass. The cycle-statistics comparison is
# REPORTED, not asserted — it currently does not match, which is the finding.
# =============================================================================
import sys, statistics as St
from itertools import product
from collections import Counter

N=24
def sc(x,n=N):
    # v18 signed_centered: representative in (-N/2, N/2]  -- NOT [-N/2, N/2).
    # v3 used the half-open-below convention, which differs at exactly one
    # value (x = N/2 = 12), i.e. the antipodal boundary itself.
    y=x%n
    return y-n if y>n//2 else y
def da(D): return abs(sc(D-N//2))
FAIL=[]
def ck(n,c):
    print(f"[{'PASS' if c else 'FAIL'}] {n}")
    if not c: FAIL.append(n)

def make_step(sde_mode="offset", tie_mode="inert"):
    def sde(ta,tb):
        D=(ta-tb)%N
        return {"offset":sc(D-N//2), "neg":-sc(D-N//2), "raw":sc(D)}[sde_mode]
    def step(state,k):
        th,dl=state
        th=tuple((th[i]+dl[i])%N for i in range(3))          # CONV-TICK 1: advance
        E=[(i,j) for i,j in ((0,1),(0,2),(1,2))              # 2-4: snapshot + classify
           if da((th[i]-th[j])%N)<=k]
        old=dl
        if len(E)==1:                                        # antipodal swap
            i,j=E[0]; d=list(dl); d[i],d[j]=old[j],old[i]
            return (th,tuple(d)),'swap'
        if len(E)==2:                                        # P3 successor shift
            nodes=[x for e in E for x in e]
            c=[v for v in set(nodes) if nodes.count(v)==2][0]
            ends=sorted(v for v in set(nodes) if v!=c); path=[ends[0],c,ends[1]]
            S=sde(th[path[0]],th[path[1]])+sde(th[path[1]],th[path[2]])
            if S<0: path=path[::-1]
            elif S==0:
                Ee=sc(old[path[2]]-old[path[0]])
                if Ee<0: path=path[::-1]
                elif Ee==0:
                    if tie_mode=="inert": return (th,dl),'tie'   # owner: ties inert
                    if tie_mode=="rev": path=path[::-1]
            d=list(dl)
            for i,v in enumerate(path): d[v]=old[path[(i+1)%3]]
            return (th,tuple(d)),'p3'
        if len(E)==3: return (th,dl),'k3'
        return (th,dl),None
    return step

def canon(s):
    th,dl=s
    return ((th[0]-th[1])%N,(th[0]-th[2])%N,(dl[0]-dl[1])%N,(dl[0]-dl[2])%N)
def lift(r,c=0,b=0):
    DAB,DAC,dAB,dAC=r
    return ((c,(c-DAB)%N,(c-DAC)%N),(b,(b-dAB)%N,(b-dAC)%N))

def ics(k, family="primary"):
    """primary: |d|_c<=2k, eps in the retrigger overlap B_k cap (B_k+d).
       supplementary: |d|_c>2k, overlap empty, all eps in B_k."""
    B=set(range(-k,k+1)); out=[]
    for d in range(-N//2,N//2):
        if d==0: continue
        prim = abs(sc(d))<=2*k
        if (family=="primary") != prim: continue
        ov=sorted(B & {b+d for b in B}) if prim else sorted(B)
        for eps in ov:
            DAB=(N//2+eps)%N
            for DAC,dAC in product(range(N),repeat=2):
                out.append((lift((DAB,DAC,(-d)%N,(-dAC)%N)), sc(d)))
    return out

# --- (a) IC families reproduced, both -------------------------------------
P=ics(1,"primary"); Sup=ics(1,"supplementary")
cp=Counter(d for _,d in P); cs=Counter(d for _,d in Sup)
ck(f"A1 primary retrigger-entry family = {len(P)} ICs with per-d counts "
   f"{dict(sorted(cp.items()))} (DSN: 3456; 1152 at d=+-1, 576 at d=+-2)",
   len(P)==3456 and cp[1]==cp[-1]==1152 and cp[2]==cp[-2]==576)
ck(f"A2 the six published supplementary rows are reproduced exactly at 1728 "
   f"ICs each (d=+-3,+-4,+-5), totalling the owner's 10368. Extending the "
   f"same generator beyond the owner-tabulated range to all |d|_c>2k yields "
   f"{len(Sup)} ICs; that larger set is an UNREGISTERED EXTRAPOLATION of the "
   f"generation rule and is used in no owner comparison.",
   all(cs[sg*v]==1728 for v in (3,4,5) for sg in (1,-1))
   and sum(cs[sg*v] for v in (3,4,5) for sg in (1,-1))==10368)

# --- (c) common-token-shift quotient: derived symmetry, checked exhaustively
step=make_step()
bad=0
for r in product(range(N),repeat=4):
    a=canon(step(lift(r,0,0),1)[0])
    if a!=canon(step(lift(r,5,7),1)[0]) or a!=canon(step(lift(r,17,3),1)[0]):
        bad+=1
ck(f"A3-ID/NUM: for all {N**4} reduced states, the three DECLARED lifts "
   f"(c,b) = (0,0), (5,7), (17,3) give the same next reduced state "
   f"({bad} mismatches). This row decides those three lifts only; the "
   f"all-lift statement is the memo [ALG] theorem (a common (c,b) shift moves "
   f"every advanced phase by c+b, leaving the defect graph fixed, and "
   f"commutes with swap and the P3 successor shift) and is NOT asserted here. "
   f"The quotient is a derived no-birth dynamical symmetry, not SG-2 gauge.",
   bad==0)

# --- cycle statistics: reported, not asserted -----------------------------
def stats(step,I,k=1,cap=20000):
    pers=[];pres=[];ties=0;k3=0
    for st,_ in I:
        seen={};s=st;t=0;seq=[]
        while t<cap:
            c=canon(s)
            if c in seen: break
            seen[c]=t; s,ev=step(s,k); seq.append(ev); t+=1
        pre=seen[canon(s)]; pers.append(t-pre); pres.append(pre)
        ties+=seq[pre:t].count('tie'); k3+=seq[pre:t].count('k3')
    return pers,pres,ties,k3

print("\n--- (b) convention sweep (now executable, was memo-only in v1) ---")
print(f"{'sde':8}{'tie':7}{'medP':>6}{'maxP':>6}{'nDist':>7}{'maxPre':>8}{'ties':>7}  dominant")
best=None
for sm in ("offset","neg","raw"):
    for tm in ("inert","fwd","rev"):
        pers,pres,ties,k3=stats(make_step(sm,tm),P)
        dom=[p for p,_ in Counter(pers).most_common(6)]
        print(f"{sm:8}{tm:7}{St.median(pers):>6.0f}{max(pers):>6}"
              f"{len(set(pers)):>7}{max(pres):>8}{ties:>7}  {dom}")
        if (sm,tm)==("offset","inert"): best=(pers,pres,dom,k3)
print(f"{'DSN target':15}{138:>6}{1638:>6}{79:>7}{830:>8}{'-':>7}  [15, 48, 357, 396, 228, 1638]")
pers,pres,dom,k3=best
dom6=set([15,48,357,396,228,1638])
ck(f"A4 EXACT REPRODUCTION of BIND3-CYCLE-N24K1 cycle statistics: median "
   f"period {St.median(pers):.0f}=138, max period {max(pers)}=1638, distinct "
   f"lengths {len(set(pers))}=79, median preperiod {St.median(pres):.0f}=0, "
   f"max preperiod {max(pres)}=830, K3 events in cycles {k3}=0, and all six "
   f"published dominant periods recovered {sorted(dom6 & set(dom))}. Every "
   f"clause is decided by the expression.",
   St.median(pers)==138 and max(pers)==1638 and len(set(pers))==79
   and St.median(pres)==0 and max(pres)==830 and k3==0
   and dom6 <= set(dom))

# --- class taxonomy -------------------------------------------------------
AB=(0,1); pure=scat=xferA=xferB=0
for st,_ in P:
    seen={};s2=st;t=0;hist=[]
    while t<20000:
        c=canon(s2)
        if c in seen: break
        seen[c]=t
        th,dl=s2; thn=tuple((th[i]+dl[i])%N for i in range(3))
        E=frozenset((i,j) for i,j in ((0,1),(0,2),(1,2)) if da((thn[i]-thn[j])%N)<=1)
        s2,ev=step(s2,1); hist.append((E,ev)); t+=1
    pre=seen[canon(s2)]; cyc=hist[pre:t]
    pairs=set(); bonded=set()
    for E,ev in cyc:
        pairs|=set(E)
        if ev=='swap' and len(E)==1: bonded|=set(E)
    if pairs<={AB}: pure+=1
    else: scat+=1
    if bonded-{AB}: xferA+=1
    if len(bonded)>=2: xferB+=1
ck(f"A5 EXACT REPRODUCTION of the BIND3 class taxonomy: pure AB-bound "
   f"{pure}=124 ({100*pure/len(P):.1f}%=3.6%), multi-pair scattering "
   f"{scat}=3332 ({100*scat/len(P):.1f}%=96.4%), free/single-pair-partial 0.",
   pure==124 and scat==3332)
print(f"  [REPORT, not asserted] bond transfer is definition-sensitive and the "
      f"DSN does not define the classifier. Reading A ('a non-AB pair becomes "
      f"bonded'): {xferA} = {100*xferA/len(P):.1f}%. Reading B ('the bonded "
      f"pair identity changes'): {xferB} = {100*xferB/len(P):.1f}%. Published: "
      f"81.8%. Both computed; neither selected.")

print("-"*70)
if FAIL: print("FAILURES:",FAIL); sys.exit(1)
print("RESULT: BIND3-CYCLE-N24K1 REPRODUCED EXACTLY. Published IC cardinalities "
      "and d-resolved multiplicities reproduced (pairing supported, not "
      "owner-verified); three-lift quotient regression checked exhaustively "
      "over all reduced states (all-lift well-definedness is the companion "
      "memo [ALG] theorem); cycle statistics (median 138, max 1638, 79 "
      "distinct, median preperiod 0, max preperiod 830, K3 0, all six "
      "dominant periods) and class taxonomy (124 / 3332) reproduced exactly. "
      "Bond-transfer classifier is definition-sensitive and left unselected. "
      "GATE PASSED: k in {0,2,3} enumeration may proceed, then the frozen "
      "DISC-1B / DISC-1D harness.")
sys.exit(0)
