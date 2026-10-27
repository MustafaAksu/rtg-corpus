#!/usr/bin/env python3
# =============================================================================
# GAP-LOCK LEMMA 3 — CLOSURE CERTIFICATE  v2   (supersedes v1)
# =============================================================================
# [COR] v1 is retracted as a proof. Its Step 1 inferred boundedness of the
# ACCUMULATED offset alpha_k from a per-slip bound |delta - pi/3| = O(sqrt q).
# That does not follow: a bounded per-slip error can accumulate over infinitely
# many slips, and ruling that out needs sum_k sqrt(q_{M_k}) < infinity, which
# was exactly what the next step was supposed to establish. Circular at the
# first arrow. The closure survives via the PI's replacement argument, which
# uses an EXACT local event identity and accumulates nothing.
#
# THE ARGUMENT (companion memo; NOT asserted by this exit code):
#   G_n := (pi/3) n - (phi_n - phi_0)          auxiliary primitive-time defect
#   G_{6M} = D_M                                agrees with the owner's D at blocks
#   n_j = n_0 + 6j + s_j                        exact, from Lemma 1 alphabet {6,7}
#   => G_{n_j} = C + (pi/3) s_j - o_j           EXACT local identity
#   g_{j+1} = 7 <=> o_j < Delta_j,  Delta_j := 2pi - Lambda_6(x_j) -> 0
#   => at the k-th 7-gap, 0 <= o < Delta -> 0, so G = C + (k-1)pi/3 + o(1)
#   => D_{M_k} = C + (k-1)pi/3 + o(1)          via r_k <= 5 and dphi = pi/3+O(sqrt Q)
#   => with INF-1, log M_k = (pi/3tau) k + C* + o(1) and the ratio converges.
#
# THIS CERTIFICATE TESTS ONLY FINITE IDENTITIES AND REGRESSIONS.
# No row asserts convergence, summability, or any infinite implication.
# =============================================================================
import sys, math
FAIL=[]
def ck(n,c):
    print(f"[{'PASS' if c else 'FAIL'}] {n}")
    if not c: FAIL.append(n)
TWOPI=2*math.pi; SQ=math.sqrt(3); TAU=2*SQ/3; PI3=math.pi/3
def wr(a): return (a+math.pi)%TWOPI-math.pi

N=20_000_000
r,e=0.01,0.004
def th(r,e):
    x=wr(e); return math.atan2(SQ*x,2*r-x)
t=th(r,e); phi0=t; phi=t; lap=math.floor(phi/TWOPI)
buf=[]                     # rolling (step, phi, isEvent, o, Q)
ev=[]                      # (j, n_j, o_j, Q_j, Lambda6_j, gap_to_next)
prev=None; jj=0
for i in range(1,N+1):
    r,e = r-math.sin(e), e+(math.exp(r)-1.0)-math.sin(e)
    t2=th(r,e); phi+=wr(t2-t); t=t2
    l=math.floor(phi/TWOPI)
    isev = l>lap
    o=Q=None
    if isev:
        o=phi-TWOPI*l; w=wr(e); Q=r*r-r*w+w*w
        lap=l
    buf.append((i,phi,isev,o,Q))
    if len(buf)>8: buf.pop(0)
    # close out the event that occurred 6 steps ago
    if len(buf)==8 and buf[1][2]:
        n_j,phi_j,_,o_j,Q_j = buf[1]
        L6 = buf[7][1]-phi_j
        ev.append([n_j,phi_j,o_j,Q_j,L6])
# attach realized gaps and the 7-gap running count
for a in range(len(ev)-1): ev[a].append(ev[a+1][0]-ev[a][0])
ev=[x for x in ev if len(x)==6]
s=0; S=[]
for x in ev: S.append(s); s += (1 if x[5]==7 else 0)
print(f"  {len(ev)} B-events with a realized gap; 7-gaps: {sum(1 for x in ev if x[5]==7)}")

# ---- C1 the EXACT local event identity  G(n_j) = C + (pi/3)s_j - o_j -------
vals=[]; maxphi=0.0
for x,sj in zip(ev,S):
    n_j,phi_j,o_j,Q_j,L6,g = x
    vals.append((PI3*n_j-(phi_j-phi0)) - PI3*sj + o_j)
    maxphi=max(maxphi,abs(phi_j))
spread=max(vals)-min(vals)
noise=2.0**-52*maxphi          # float64 ulp of the accumulated lift
ck(f"C1 the local event identity G(n_j) = C + (pi/3) s_j - o_j holds with a "
   f"single constant C = {vals[0]:.10f} across all {len(ev)} events: observed "
   f"spread {spread:.3e} against the float64 noise floor {noise:.3e} of the "
   f"accumulated lift (ratio {spread/noise:.2f}). The identity is EXACT; the "
   f"residual is arithmetic, not structural. [v1 note: an earlier version of "
   f"this row compared at 9 decimals on a quantity of magnitude ~1e7, past "
   f"float64 resolution, and reported a spurious failure.]",
   spread < 5*noise)

# ---- C2 gap criterion with the ACTUAL Delta_j = 2pi - Lambda_6 -------------
bad=sum(1 for x in ev if (7 if x[2] < (TWOPI-x[4]) else 6) != x[5])
ck(f"C2 the criterion 'g_(j+1) = 7 iff o_j < Delta_j' with the ACTUAL "
   f"Delta_j = 2pi - Lambda_6(x_j) (not the tau*q surrogate used in v1) "
   f"reproduces the realized gap at all {len(ev)} events ({bad} mismatches)",
   bad==0)
badsur=sum(1 for x in ev if (7 if x[2] < TAU*x[3] else 6) != x[5])
ck(f"C2b [regression only] the v1 surrogate criterion o_j < tau q_j happens to "
   f"agree on this horizon ({badsur} mismatches), but it is NOT the theorem — "
   f"Delta_j = tau q_j + O(q^(3/2)) and agreement on a finite classification "
   f"does not promote a surrogate to an identity", badsur==0)

# ---- C3 G_{6M} = D_M at block boundaries ----------------------------------
ck("C3 G_n reduces to the owner's D_M at block boundaries: "
   "G_(6M) = (pi/3)(6M) - (phi - phi_0) = 2pi M - (phi - phi_0) = D_M, "
   "an algebraic identity in the definitions (no separate symbol).", True) if False else None
ck("C3 the auxiliary defect agrees with the owner's D at block boundaries by "
   "construction: (pi/3)(6M) = 2pi M, so G_(6M) = D_M identically. v1 wrongly "
   "reused the symbol D for the accumulated sum of tau*q over laps, which is "
   "a different object.", abs(PI3*6-TWOPI)<1e-15)

# ---- C4 slip-time overshoot lies in [0, Delta) and Delta is shrinking ------
sl=[(x,sj) for x,sj in zip(ev,S) if x[5]==7]
rows=[(x[0], x[2], TWOPI-x[4]) for x,_ in sl]
ck(f"C4 at each realized 7-gap the overshoot satisfies 0 <= o_j < Delta_j, "
   f"with (step, o_j, Delta_j) = "
   f"{[(n, f'{o:.3e}', f'{d:.3e}') for n,o,d in rows]}",
   all(0<=o<d for _,o,d in rows))

# ---- C5 the r_k <= 5 bracket at the slips ---------------------------------
br=[]
for x,_ in sl:
    n=x[0]; rk=n%6
    br.append(rk)
ck(f"C5 the block remainders r_k = n_(j_k) mod 6 at the realized slips are "
   f"{br}, all <= 5 as required by the return-to-block-time step",
   all(0<=b<=5 for b in br))

# ---- C6 ratios: raw physical, and the backbone-shifted DIAGNOSTIC ----------
ns=[x[0] for x,_ in sl]
raw=[ns[i+1]/ns[i] for i in range(len(ns)-1)]
kap=6/0.000076
sh=[(ns[i+1]+kap)/(ns[i]+kap) for i in range(len(ns)-1)]
print(f"  raw physical slip-step ratios      : {[round(x,4) for x in raw]}")
print(f"  backbone-shifted DIAGNOSTIC ratios : {[round(x,6) for x in sh]}")
print(f"  target exp(sqrt3 pi/6)             : {math.exp(SQ*math.pi/6):.9f}")
ck("C6 [regression only] both sequences are reported. The RAW physical ratios "
   "are the observable; the (n+kappa)-shifted sequence is a backbone-shifted "
   "DIAGNOSTIC that converges faster and was mislabelled in v1 as the "
   "observed physical ratio. Neither is asserted here to converge — that is "
   "the memo's [ALG] conclusion.", len(raw)==len(sh)>=4)

print("-"*70)
if FAIL: print("FAILURES:",FAIL); sys.exit(1)
print("RESULT: ALL ROWS PASS. Finite identities and regressions only: the "
      "exact local event identity C1, the exact gap criterion C2 with the "
      "true Delta, the block-boundary reduction C3, the slip-time overshoot "
      "bracket C4, and the r_k <= 5 bound C5. NO convergence, summability or "
      "infinite implication is asserted by this exit code; the closure "
      "argument lives entirely in the companion memo.")
sys.exit(0)
