#!/usr/bin/env python3
"""[SESSION] RECONSTRUCTED — the post hoc detuned-neighbour and threshold tables of the exploratory pilot.
The original was an inline command of the session of 11 Nov 2026 and was not saved as a file; this file repeats it
from the session transcript (same statements, argument handling added). It was run AFTER the result of analyse3.py on
pilot_N120.jsonl had been seen: it is exploratory and post hoc.
usage: python3 -I neighbour_control_reconstructed.py pilot_N120.jsonl"""
import sys, json
R=[json.loads(l) for l in open(sys.argv[1])]; N=120; TAIL=100
RES={0,30,60,90}
def w(s,m,z=1.96):
    p=s/m; d=1+z*z/m; ce=(p+z*z/(2*m))/d; h=z*((p*(1-p)/m+z*z/(4*m*m))**.5)/d; return max(0,ce-h),min(1,ce+h)
def row(name,sel):
    t=sum(r["M"]>=TAIL for r in sel); lo,hi=w(t,len(sel)); print(f"{name:52s} n={len(sel):5d} tails={t:3d} rate={t/len(sel):.4f} [{lo:.4f},{hi:.4f}]")
nores=[r for r in R if not any(x in RES for x in r["d0"])]
for dist in (1,2,3):
    NB={(a+s*dist)%N for a in RES for s in (1,-1)}
    row(f"no resonant seed, some seed at distance {dist} from one", [r for r in nores if any(x in NB for x in r["d0"])])
row("no resonant seed, no seed within 3 of one", [r for r in nores if not any(min((x-a)%N,(a-x)%N)<=3 for x in r["d0"] for a in RES)])
row("resonant seed present", [r for r in R if any(x in RES for x in r["d0"])])
# number of resonant seeds
for m in (1,2):
    sel=[r for r in R if sum(x in RES for x in r["d0"])==m]
    if sel: row(f"exactly {m} resonant seed(s)", sel)
# tails: capped vs not; first-birth time
tl=[r for r in R if r["M"]>=TAIL]
print("tails with resonant seed:", sum(any(x in RES for x in r['d0']) for r in tl), "of", len(tl), "; among capped (M>=300):", sum(any(x in RES for x in r['d0']) for r in tl if r['M']>=300), "of", sum(r['M']>=300 for r in tl))
for thr in (60,80,100,150,200,300):
    a=[r for r in R if any(x in RES for x in r["d0"])]; b=nores
    print(f"  M>={thr}: resonant {sum(r['M']>=thr for r in a)/len(a):.4f}  non-resonant {sum(r['M']>=thr for r in b)/len(b):.4f}")
