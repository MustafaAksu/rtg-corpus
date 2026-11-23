#!/usr/bin/env python3
# N-5A-S1 LONG-HORIZON RECHECK v1
# Stage A: 60-dps exact-map recheck of the first rare 7-gap.
# Stage B: double-precision 12-section sweep to show the short-horizon alias
#          is not specific to Theta_0 = 0.
# Exit 0 only if the decisive high-precision counterexample is reproduced.

import sys, math
import mpmath as mp

# ---------------- Stage A: 60 dps, section Theta_0 = 0 ----------------
mp.mp.dps = 60
SQ3 = mp.sqrt(3)
TWOPI = 2*mp.pi

def T_mp(p):
    r,e=p
    return (r-mp.sin(e), e+(mp.e**r-1)-mp.sin(e))

def wrap_mp(a):
    return mp.fmod(a+mp.pi,TWOPI)-mp.pi

def theta_mp(p):
    r,e=p; w=wrap_mp(e)
    return mp.atan2(SQ3*w,2*r-w)

def q_mp(p):
    r,e=p; w=wrap_mp(e)
    return r*r-r*w+w*w

p=(mp.mpf("0.01"),mp.mpf("0.004"))
th=theta_mp(p); phi=th
prev=None
short=set()
first7=None
q_before7=None

for i in range(40000):
    p2=T_mp(p)
    th2=theta_mp(p2)
    phi2=phi+wrap_mp(th2-th)
    a,b=phi,phi2
    k=mp.floor(a/TWOPI)
    if b >= (k+1)*TWOPI:
        idx=i+1
        if prev is not None:
            g=idx-prev
            if idx <= 240:
                short.add(g)
            if g==7 and first7 is None:
                first7=idx
                q_before7=q_mp(p)
        prev=idx
    p,th,phi=p2,th2,phi2

print("STAGE A — 60 dps exact primitive map")
print("short-horizon distinct gaps through 240 steps:", sorted(short))
print("first 7-gap primitive step:", first7)
print("Q immediately before first 7-gap:", mp.nstr(q_before7,30))
print("Q0:", mp.nstr(mp.mpf("0.000076"),30))

assert short == {6}
assert first7 == 33229
assert q_before7 < mp.mpf("0.000076")

# ---------------- Stage B: 12-section exploratory long sweep ----------------
SQ3F=math.sqrt(3.0); TWOPIF=2*math.pi
def wrap_f(a): return (a+math.pi)%TWOPIF-math.pi
def T_f(r,e): return (r-math.sin(e), e+(math.exp(r)-1.0)-math.sin(e))
def theta_f(r,e):
    w=wrap_f(e)
    return math.atan2(SQ3F*w,2*r-w)

r,e=0.01,0.004
th=theta_f(r,e); phi=th
phis=[phi]
for _ in range(200000):
    r,e=T_f(r,e)
    th2=theta_f(r,e)
    phi=phi+wrap_f(th2-th)
    th=th2
    phis.append(phi)

print("STAGE B — 12-section 200000-step exploratory sweep")
all_have_7=True
for s in range(12):
    theta0=s*TWOPIF/12
    prev=None; ds=set(); first=None
    for i in range(len(phis)-1):
        a=phis[i]-theta0; b=phis[i+1]-theta0
        k=math.floor(a/TWOPIF)
        if b >= (k+1)*TWOPIF:
            idx=i+1
            if prev is not None:
                g=idx-prev; ds.add(g)
                if g==7 and first is None: first=idx
            prev=idx
    print(f"section {s:02d}: distinct={sorted(ds)}, first7={first}")
    all_have_7 &= (7 in ds)

assert all_have_7
print("RESULT: PASS")
print("The 240-step constant-6 word is a finite-horizon alias.")
print("HYP-N5AS1-GAP is falsified by a 7-step return deeper in the contracted regime.")
sys.exit(0)
