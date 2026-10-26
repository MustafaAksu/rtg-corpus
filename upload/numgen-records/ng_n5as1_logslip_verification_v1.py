# Independent reimplementation: different crossing detector (sign of a
# section function, not floor-arithmetic on unwrapped phase), independent
# unwrapping, mpmath dps=60. Confirms or refutes step 33229.
import mpmath as mp
mp.mp.dps=60
SQ3=mp.sqrt(3); TWOPI=2*mp.pi
def T(p):
    r,e=p; return (r-mp.sin(e), e+(mp.e**r-1)-mp.sin(e))
def wr(a): return mp.fmod(a+mp.pi,TWOPI)-mp.pi
def Q(p):
    r,e=p; w=wr(e); return r*r-r*w+w*w
def Th(p):
    r,e=p; w=wr(e); return mp.atan2(SQ3*w,2*r-w)

# detector: count completed 2pi laps via cumulative sum of increments,
# crossing = integer part of (phi/2pi) increments
p=(mp.mpf("0.01"),mp.mpf("0.004"))
phi=Th(p); lap_prev=mp.floor(phi/TWOPI)
prev_idx=None; gaps={}; first7=None; qb=None; slips=[]
th=phi
for i in range(1,40001):
    p2=T(p); th2=Th(p2)
    phi=phi+wr(th2-th)
    lap=mp.floor(phi/TWOPI)
    if lap>lap_prev:
        if prev_idx is not None:
            g=i-prev_idx
            gaps[g]=gaps.get(g,0)+1
            if g!=6:
                slips.append((i,g))
                if g==7 and first7 is None: first7=i; qb=Q(p)
        prev_idx=i; lap_prev=lap
    p,th=p2,th2
print("independent detector, 40000 steps")
print(" gap histogram:", dict(sorted(gaps.items())))
print(" first non-6 slip:", slips[0] if slips else None)
print(" Q before first slip:", mp.nstr(qb,20) if qb else None)
print(" Q0 =", mp.nstr(Q((mp.mpf("0.01"),mp.mpf("0.004"))),20))
import math
SQ3=math.sqrt(3.0); TWOPI=2*math.pi
def wr(a): return (a+math.pi)%TWOPI-math.pi
def Th(r,e):
    w=wr(e); return math.atan2(SQ3*w,2*r-w)
def Qf(r,e):
    w=wr(e); return r*r-r*w+w*w

tau=2*math.sqrt(3)/3
Q0=0.000076
kappa=1.0/Q0                 # in six-step BLOCK units
ratio_pred=math.exp(math.pi/(3*tau))
print(f"tau = {tau:.6f}   predicted slip ratio exp(pi/(3 tau)) = {ratio_pred:.4f}")
print(f"kappa = 1/Q0 = {kappa:.1f} blocks\n")

r,e=0.01,0.004
th=Th(r,e); phi=th; lap=math.floor(phi/TWOPI)
prev=None; slips=[]; N=4_000_000
for i in range(1,N+1):
    r,e = r-math.sin(e), e+(math.exp(r)-1.0)-math.sin(e)
    th2=Th(r,e); phi+=wr(th2-th); th=th2
    l=math.floor(phi/TWOPI)
    if l>lap:
        if prev is not None:
            g=i-prev
            if g!=6: slips.append((i,g,Qf(r,e)))
        prev=i; lap=l

print(f"slips found in {N} primitive steps: {len(slips)}")
print(f"{'k':>2} {'step':>10} {'gap':>4} {'blocks M':>10} {'M+kappa':>10} {'ratio':>8} {'1/Q':>10}")
prevshift=None
for k,(s,g,q) in enumerate(slips,1):
    M=s/6.0; shift=M+kappa
    rat=(shift/prevshift) if prevshift else float('nan')
    print(f"{k:>2} {s:>10} {g:>4} {M:>10.0f} {shift:>10.0f} {rat:>8.4f} {1/q:>10.0f}")
    prevshift=shift
print(f"\nobserved ratios vs predicted {ratio_pred:.4f}")
