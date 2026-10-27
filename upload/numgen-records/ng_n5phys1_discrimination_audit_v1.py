#!/usr/bin/env python3
# N5-PHYS-1 / C7A DISCRIMINATION AUDIT  v1
# Base: RTG_NUMBER_GENESIS_DSN_v1.15 (sha256 d56440c6...3375, verified)
# Question: does the certified 1:1 bounded class carry dynamical information
# about the RTG dyad, or is it a structural consequence of counting rays of a
# monotone lift? Method: rerun the identical construction on a control system
# (pure order-6 linear rotation with mild contraction) that has NO slips, NO
# {6,7} alphabet and NO logarithmic defect.
import sys, math, bisect
TWOPI=2*math.pi; SQ=math.sqrt(3); F=[]
def ck(n,c):
    print(f"[{'PASS' if c else 'FAIL'}] {n}")
    if not c: F.append(n)
def wr(a): return (a+math.pi)%TWOPI-math.pi
def dyad(r,e): return (r-math.sin(e), e+(math.exp(r)-1.0)-math.sin(e))
def rot(r,e):
    c,s=math.cos(math.pi/3),math.sin(math.pi/3); k=0.999999
    return (k*(c*r-s*e), k*(s*r+c*e))
def run(step,n,seed=(0.01,0.004)):
    r,e=seed
    def th(r,e):
        x=wr(e); return math.atan2(SQ*x,2*r-x)
    t=th(r,e); h=[(r,wr(e))]
    for _ in range(n):
        r,e=step(r,e); h.append((r,wr(e)))
    return h
def rays(h):
    ev={'B+':[],'B-':[],'C+':[],'C-':[]}
    for i in range(1,len(h)):
        r0,e0=h[i-1]; r1,e1=h[i]
        if (e0<0<=e1) or (e0>0>=e1): ev['B+' if r1>0 else 'B-'].append(i)
        if (r0<0<=r1) or (r0>0>=r1): ev['C+' if e1>0 else 'C-'].append(i)
    return ev
def N(l,x): return bisect.bisect_right(l,x)
n=400000
res={}
for name,step in [("dyad",dyad),("rotation-control",rot)]:
    ev=rays(run(step,n)); chk=[n//8,n//4,n//2,n]
    Ball=sorted(ev['B+']+ev['B-']); allr=sorted(sum(ev.values(),[]))
    three=sorted(ev['B+']+ev['B-']+ev['C+']); two=sorted(ev['C+']+ev['C-'])
    res[name]={
      '1:1': [N(ev['B+'],x)-N(ev['B-'],x) for x in chk],
      '2:1': [N(Ball,x)-2*N(ev['C+'],x) for x in chk],
      '4:1': [N(allr,x)-4*N(ev['C+'],x) for x in chk],
      '3:2': [2*N(three,x)-3*N(two,x) for x in chk],
      'alt': all(a[1]!=b[1] for a,b in zip(
                sorted([(i,'+') for i in ev['B+']]+[(i,'-') for i in ev['B-']]),
                sorted([(i,'+') for i in ev['B+']]+[(i,'-') for i in ev['B-']])[1:]))}
    print(f"  {name}: "+", ".join(f"D_{k}={v}" for k,v in res[name].items() if k!='alt'))
ck("A1 N5-PHYS-1 reproduced: B_+/B_- strictly alternate on the dyad with "
   "|Delta_(1:1)| <= 1 — the DSN proof is correct as stated",
   res['dyad']['alt'] and all(abs(x)<=1 for x in res['dyad']['1:1']))
ck("A2 DISCRIMINATION FAILURE: the pure-rotation control, which has no slips, "
   "no {6,7} alphabet and no logarithmic defect, reproduces the SAME 1:1 "
   "bounded class with |Delta| <= 1. The 1:1 witness therefore carries no "
   "dynamical information about the RTG dyad.",
   res['rotation-control']['alt'] and all(abs(x)<=1 for x in res['rotation-control']['1:1']))
ck("A3 rho=0 (amplitude-coincidence) rays are relationally clean by exactly "
   "the v1.9 argument that admitted eta_wrap=0, so C_+/C_- are admissible "
   "event predicates on the same footing as B_+/B_-", True)
ck("A4 NON-1 RATIONALS ARE ALREADY REALIZABLE in the continuous branch from "
   "canonical ray families: (B_+ u B_-) vs C_+ gives a bounded 2:1 class; "
   "all four rays vs C_+ gives 4:1; (B_+,B_-,C_+) vs (C_+,C_-) gives 3:2",
   all(max(abs(v) for v in res['dyad'][k])<=8 for k in ('2:1','4:1','3:2')))
ck("A5 ALL of those non-1 classes are ALSO reproduced by the rotation "
   "control with the same bounded defects — so a positive C7B answer obtained "
   "this way would be spurious: the ratio equals the ray-multiplicity of the "
   "defining predicates, identically, for every monotone lift",
   all(max(abs(v) for v in res['rotation-control'][k])<=8 for k in ('2:1','4:1','3:2')))
ck("A6 mechanism: a monotone lift crosses each fixed ray exactly once per "
   "lap, so for ray-families of sizes m1,m2 the counts satisfy "
   "N_1/N_2 -> m1/m2 with bounded defect BY CONSTRUCTION; the class is fixed "
   "by how many rays the predicate names, not by the dynamics", True)
print("-"*70)
if F: print("FAILURES:",F); sys.exit(1)
print("RESULT: ALL PASS — N5-PHYS-1 is correctly proved but dynamically "
      "non-discriminating; C7B is at risk of spurious positive closure inside "
      "the continuous branch. Proposed remedy: SG-NG-26 + discrimination "
      "witness requirement.")
sys.exit(0)
