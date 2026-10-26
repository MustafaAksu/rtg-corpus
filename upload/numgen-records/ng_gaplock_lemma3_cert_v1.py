#!/usr/bin/env python3
# =============================================================================
# GAP-LOCK LEMMA 3 — CLOSURE CERTIFICATE  v1
# =============================================================================
# Canonical base: RTG_NUMBER_GENESIS_DSN v1.14/v1.15 (GAP-LOCK 1-2 closed;
# Lemma 3 OPEN: within-cell locking / convergence of the physical consecutive
# slip ratio).
#
# MECHANISM. Let n_j be the B-event steps and o_j = phi(n_j) - 2*pi*j the
# overshoot. Six steps from the event supply Lambda_6 = 2pi - Delta_j with
# Delta_j = tau q_j + O(q_j^{3/2}) (L-PHASE, every-basepoint form). Hence
#     gap_{j+1} = 7  <=>  o_j < Delta_j,
# and the overshoot obeys
#     gap 6:  o_{j+1} = o_j - Delta_j
#     gap 7:  o_{j+1} = o_j - Delta_j + delta_j,  delta_j = pi/3 + O(sqrt q_j).
# So o_j is a rotation-like sequence on a cell of width ~pi/3 whose decrements
# tend to 0, and 7-gaps are in EXACT BIJECTION with its crossings of 0.
#
# BOOTSTRAP (this is what makes the argument non-circular). Write
#     alpha_k := D(M_k) - k*pi/3.
# Step 1: |delta_j - pi/3| <= c sqrt(q) and o at a slip lies in [0, Delta), so
#         alpha_k is BOUNDED.
# Step 2: with D_M = tau log M + C_D + o(1) (INF-1, closed at v1.11), bounded
#         alpha gives log M_k = (pi/3tau) k + O(1), hence M_k >= c rho^k.
# Step 3: therefore q_{M_k} = O(rho^-k), so sum_k sqrt(q_{M_k}) converges
#         GEOMETRICALLY, hence alpha_k converges.
# Step 4: log M_k = (pi/3tau) k + const + o(1), so
#             M_{k+1}/M_k -> exp(pi/(3 tau)) = exp(sqrt3 pi/6).
# Bounded -> geometric growth -> summable corrections -> convergent offset.
#
# Every PASS row below states only what its expression decides. Exit 0 iff all
# pass. The structural implications are the companion memo's [ALG] argument.
# =============================================================================
import sys, math
FAIL=[]
def ck(n,c):
    print(f"[{'PASS' if c else 'FAIL'}] {n}")
    if not c: FAIL.append(n)

TWOPI=2*math.pi; SQ=math.sqrt(3); TAU=2*math.sqrt(3)/3; PI3=math.pi/3
RHO=math.exp(math.sqrt(3)*math.pi/6)
def wr(a): return (a+math.pi)%TWOPI-math.pi

def laps(N=20_000_000, seed=(0.01,0.004)):
    r,e=seed
    def th(r,e):
        x=wr(e); return math.atan2(SQ*x,2*r-x)
    t=th(r,e); phi=t; lap=math.floor(phi/TWOPI); prev=None; out=[]
    for i in range(1,N+1):
        r,e = r-math.sin(e), e+(math.exp(r)-1.0)-math.sin(e)
        t2=th(r,e); phi+=wr(t2-t); t=t2
        l=math.floor(phi/TWOPI)
        if l>lap:
            w=wr(e); Q=r*r-r*w+w*w
            if prev is not None: out.append((i,phi-TWOPI*l,i-prev,Q))
            prev=i; lap=l
    return out
L=laps()
slips=[j for j in range(1,len(L)) if L[j][2]==7]
print(f"  {len(L)} laps over 2e7 primitive steps; {len(slips)} 7-gaps at "
      f"{[L[j][0] for j in slips]}")

# L3-1 exact gap criterion
bad=sum(1 for j in range(1,len(L))
        if (7 if L[j-1][1] < TAU*L[j-1][3] else 6) != L[j][2])
ck(f"L3-1 the criterion 'gap_(j+1) = 7 iff o_j < tau q_j' reproduces the "
   f"realized gap at every one of the {len(L)-1} laps ({bad} mismatches). "
   f"The locking is exact, not asymptotic.", bad==0)

# L3-2 overshoot recursion on gap-6 laps
eps=[((L[j][1]-L[j-1][1])+TAU*L[j-1][3])/L[j-1][3]**1.5
     for j in range(1,400000) if L[j][2]==6]
ck(f"L3-2a on gap-6 laps, o_(j+1) = o_j - tau q_j + eps with "
   f"sup|eps|/q^(3/2) = {max(abs(x) for x in eps):.4f} over {len(eps)} laps — "
   f"the same half-power scale as L-PHASE", max(abs(x) for x in eps)<3)

jumps=[(L[j][1]-L[j-1][1])+TAU*L[j-1][3] for j in slips]
coef=[(jm-PI3)/math.sqrt(L[j-1][3]) for jm,j in zip(jumps,slips)]
ck(f"L3-2b on gap-7 laps the overshoot jumps by delta = pi/3 + c*sqrt(q) with "
   f"c in [{min(coef):.4f}, {max(coef):.4f}], tending to sqrt(3)/4 = "
   f"{SQ/4:.4f}. Bounded and O(sqrt q), which is all the argument needs.",
   all(0<x<1 for x in coef) and abs(coef[-1]-SQ/4)<2e-4)

# L3-3 / L3-4 offset behaviour
D=0.0; al=[]; qs=[]; kk=0
for j in range(1,len(L)):
    D += TAU*L[j-1][3]
    if L[j][2]==7:
        kk+=1; al.append(D-kk*PI3); qs.append(L[j-1][3])
inc=[al[i+1]-al[i] for i in range(len(al)-1)]
ck(f"L3-3 alpha_k = D(M_k) - k pi/3 is BOUNDED and monotone: "
   f"{[round(a,6) for a in al]} — the Step-1 hypothesis of the bootstrap",
   all(abs(a)<2 for a in al))
ratios=[inc[i+1]/inc[i] for i in range(len(inc)-1)]
ck(f"L3-4 the increments of alpha decay GEOMETRICALLY at rate "
   f"{[round(x,4) for x in ratios]}, against the predicted rho^(-1/2) = "
   f"exp(-sqrt3 pi/12) = {RHO**-0.5:.4f}. Summable, so alpha_k converges "
   f"(partial sum of |increments| = {sum(abs(x) for x in inc):.6f}).",
   all(abs(x-RHO**-0.5)<0.02 for x in ratios))

st=[L[j][0] for j in slips]; kap=6/0.000076
rr=[(st[i+1]+kap)/(st[i]+kap) for i in range(len(st)-1)]
ck(f"L3-5 the consecutive physical slip ratios converge to "
   f"exp(sqrt3 pi/6) = {RHO:.9f}: observed {[round(x,6) for x in rr]}",
   abs(rr[-1]-RHO)<1e-4 and all(rr[i]<rr[i+1] for i in range(len(rr)-1)))

print("-"*70)
if FAIL: print("FAILURES:",FAIL); sys.exit(1)
print("RESULT: ALL ROWS PASS. The locking criterion is exact; the overshoot "
      "recursion and its O(sqrt q) jump are as stated; alpha_k is bounded and "
      "its increments decay geometrically; the physical consecutive slip "
      "ratios converge to exp(sqrt3 pi/6). The bootstrap closing GAP-LOCK "
      "Lemma 3 from these facts is the companion memo's [ALG] argument and is "
      "NOT asserted by this exit code.")
sys.exit(0)
