# Independent numerical check of ER-2B v0.2 C15B/C19/C20 (Claude, RER R1). Direct iteration of the model; no source formula used in the map.
from mpmath import mp, mpf, mpc, sqrt, sin, exp, im, re, conj, fabs
mp.dps = 80
r3 = sqrt(3); lam = mpc(mpf(1)/2, r3/2)
def toW(r, e): return mpc(r - e/2, r3*e/2)
def fromW(w): e = 2*im(w)/r3; return re(w) + e/2, e
def TW(w):
    r, e = fromW(w); return toW(r - sin(e), e + exp(r) - 1 - sin(e))
def h2(z):  # Genesis normalizer (ER-2B v0.2 C15B), tested below against L_A h2 = -q_G
    zb = conj(z); return -(1+1j*r3)/12*z**2 - z*zb/3 + (1-1j*r3)/24*zb**2
def make(sig):
    H = lambda z: z + sig*h2(z)
    def Hinv(y):
        z = y
        for _ in range(200):
            zn = y - sig*h2(z)
            if fabs(zn - z) < mpf(10)**(-mp.dps+5): return zn
            z = zn
        return z
    return H, Hinv
def step(ws, sig):
    H, Hinv = make(sig)
    t = [Hinv(TW(H(w))) for w in ws]; m = sum(t)/3
    return [x - m for x in t]
def F6(ws, sig):
    for _ in range(6): ws = step(ws, sig)
    return ws
def NS(ws): return sum(abs(w)**2 for w in ws), im(ws[0]*conj(ws[1]))
def quartic(a, b, sig, f):
    vals = []
    for eps in (mpf('1e-6'), mpf('2e-6')):
        ws = [eps*a, eps*b, -eps*(a+b)]; N0, S0 = NS(ws); N1, S1 = NS(F6(ws, sig))
        d = (N1 - N0) if f == 'N' else (S1 - S0)
        vals.append(d / eps**4)
    return 2*vals[0] - vals[1]   # Richardson: remove O(eps^5)
# 1) homological equation in W frame: L_A h2 = A h2 - h2(A z) = -q_G
z = mpc('0.3', '-0.7'); r, e = fromW(z); qG = toW(0, r**2/2)
print('L_A h2 + q_G residual:', abs(lam*h2(z) - h2(lam*z) + qG))
# 2) closure sum of (t,t,-2t)
t = mpf('1e-8'); s = sum(z + h2(z) for z in (t, t, -2*t)); print('sum H(z_e)/t^2:', s/t**2, ' claim:', -(9+3j*r3)/4)
# 3) sigma family: dN_4 = a N^2 + 2 S^2, dS_4 = (2/3)(-1/2+k^2) N S, a = -1/2 + 2k^2/3
states = [(mpc(1,0), mpc('0.4','0.0')), (mpc(1,0), lam**2), (mpc('0.3','0.8'), mpc('-0.9','0.2')), (mpc(1,0), mpc('-0.5','0.9'))]
worst = 0
for sig in (mpf(0), mpf('0.1'), 1-r3/2, mpf('0.2'), 1-1/sqrt(2), mpf('0.5'), mpf(1)):
    k = 1 - sig; a = -mpf(1)/2 + 2*k**2/3
    for (A, B) in states:
        ws = [A, B, -(A+B)]; N, S = NS(ws)
        dN = quartic(A, B, sig, 'N'); dS = quartic(A, B, sig, 'S')
        eN = abs(dN - (a*N**2 + 2*S**2)); eS = abs(dS - mpf(2)/3*(-mpf(1)/2 + k**2)*N*S)
        worst = max(worst, eN, eS)
    print(f'sigma={float(sig):.6f}  max|err| so far={float(worst):.2e}')
