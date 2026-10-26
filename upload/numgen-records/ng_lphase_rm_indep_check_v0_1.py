# Independent NUMGEN-side check: r = (lifted 6-step angle) - 2pi + tau*Q from the primitive map only.
import mpmath as mp
mp.mp.dps=40
s3=mp.sqrt(3); tau=2*s3/3
def T(r,e): return r-mp.sin(e), e+mp.exp(r)-1-mp.sin(e)
def W(r,e): return mp.mpc(r-e/2, s3/2*e)
def x_of(Wc): e=2*Wc.imag/s3; return Wc.real+e/2, e
def Lam(t):  # adopted DYAD leading terms, Lambda3/r^3
    return -49*s3/72*mp.cos(t)+mp.mpf(1)/24*mp.sin(t)+23*s3/144*mp.cos(3*t)-mp.mpf(19)/48*mp.sin(3*t)
# Lambda* by dense grid + refine
N=40000; best=max(range(N),key=lambda k:abs(Lam(2*mp.pi*k/N)))
t0=mp.findroot(lambda t: mp.diff(Lam,t), 2*mp.pi*best/N); print("Lambda* =",mp.nstr(abs(Lam(t0)),12),"at",mp.nstr(t0,8))
print("Lambda3(0) + 25sqrt3/48 =", mp.nstr(Lam(0)+25*s3/48,5))
for Q in ['2.209e-3','1.6e-3','4e-4','1e-4','2.5e-5','6.25e-6']:
    Q=mp.mpf(Q); sup=0; maxstep=0
    for k in range(1440):
        th=2*mp.pi*k/1440; Wc=mp.sqrt(Q)*mp.expj(th); r,e=x_of(Wc)
        lift=0; Wp=Wc
        for j in range(6):
            r,e=T(r,e); Wn=W(r,e); d=mp.arg(Wn/Wp); 
            maxstep=max(maxstep,abs(d-mp.pi/3)/mp.sqrt(abs(Wp)**2)); lift+=d; Wp=Wn
        rm=lift-2*mp.pi+tau*Q; sup=max(sup,abs(rm)/Q**1.5)
    print("Q=",mp.nstr(Q,3)," sup|r|/Q^1.5 =",mp.nstr(sup,7)," max|dT-pi/3|/sqrtQ =",mp.nstr(maxstep,4))
