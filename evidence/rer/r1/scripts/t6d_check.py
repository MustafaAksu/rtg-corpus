import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, mpc, sqrt, im, re, conj
import carrier_check as C
mp.dps = 80; r3 = sqrt(3)
def obs(ws):
    z = ws[0]; d = (ws[1]-ws[2])/2
    Qs, Qc, I, S = abs(z)**2, abs(d)**2, re(z*conj(d)), im(z*conj(d))
    return dict(Qs=Qs, Qc=Qc, I=I, S=S, N=3*Qs/2+2*Qc)
def C12(o):
    Qs,Qc,I,S,N = o['Qs'],o['Qc'],o['I'],o['S'],o['N']
    return dict(Qs=Qs**2/4+Qs*Qc/3+2*S**2/3-4*r3/9*I*S, Qc=Qs*Qc/4+Qc**2/3+S**2/2+r3/3*I*S,
                I=N*I/6+r3*(Qs/6-2*Qc/9)*S, S=N*S/3, N=N**2/6+2*S**2)
def inc(z, d, eps):
    ws = [eps*z, eps*(-z/2+d), eps*(-z/2-d)]
    o0 = obs(ws); o1 = obs(C.F6(ws, mpf(0)))
    return {k: (o1[k]-o0[k])/eps**4 for k in o0}
worst = 0; refl = 0
for z, d in [(mpc(1,0), mpc('0.3','0.5')), (mpc('0.2','-0.9'), mpc('-0.6','0.1')), (mpc('0.7','0.7'), mpc('0.4','-0.8'))]:
    a = inc(z, d, mpf('1e-6')); b = inc(z, d, mpf('2e-6'))
    got = {k: 2*a[k]-b[k] for k in a}; ref = C12(obs([z, -z/2+d, -z/2-d]))
    worst = max(worst, max(abs(got[k]-ref[k]) for k in ref))
    # reflection: c -> -c (edge slots 2<->3); F(s,-c) = (F_s, -F_c)
    eps = mpf('1e-2'); ws = [eps*z, eps*(-z/2+d), eps*(-z/2-d)]; wr = [ws[0], ws[2], ws[1]]
    f = C.F6(ws, mpf(0)); fr = C.F6(wr, mpf(0))
    refl = max(refl, abs(fr[0]-f[0]), abs(fr[1]-f[2]), abs(fr[2]-f[1]))
print('C12 quartic increments (Qs,Qc,I,S,N), 3 states, max err:', float(worst))
print('slot-2/3 reflection identity at finite eps=1e-2, max err:', float(refl))
