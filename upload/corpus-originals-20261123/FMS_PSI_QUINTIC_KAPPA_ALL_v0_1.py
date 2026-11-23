"""FMS_PSI_QUINTIC_KAPPA_ALL_v0_1 (SESSION, 19 Oct 2026). Exceptional-kappa test for the iRmu quintic obstruction.
Reduced six-step map on the formal centre manifold: f5(kappa) = f5(1) + t*E, t=(1-kappa)/kappa (psi3 of the closure mode).
kappa enters only through the stabilizer columns. After projecting out the kappa-free Phi3 block, a 9x9 minor of
[Q*Phi1(t) | Q*b] is a nonzero constant, while Q*Phi1 has only 8 columns => b is never in the span: obstruction for
all t, i.e. all kappa with a hyperbolic closure mode (kappa not in {0,2}). Requires FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py
in the working directory. Exit 0 iff PASS."""
exec(open('FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py').read().split("iu=k(0,0,1,0); mu=")[0])
import sympy as sp
iu=k(0,0,1,0); mu=k(Fr(-1,2),0,0,Fr(-2,3))
f5base=[dict(x) for x in f5]
def vars4():
    w1={(1,0,0,0):ONE}; w2={(0,1,0,0):ONE}; W1={(0,0,1,0):ONE}; W2={(0,0,0,1):ONE}
    w3=padd(pscale(w1,-ONE),pscale(w2,-ONE)); W3=padd(pscale(W1,-ONE),pscale(W2,-ONE))
    return [(w1,W1),(w2,W2),(w3,W3)]
def psi3_t():  # psi3 with (1-kappa)/kappa factored out as t
    M={}
    for c,C in vars4(): M=padd(M,pmul(pmul(c,c,9),C,9))
    return pscale(M,n21*k(Fr(1,3))*lamb)
def extra_t():
    psi=psi3_t(); psib=pconj(psi,SW4); v=[]
    for c,C in vars4():
        v.append(pscale(padd(pscale(pmul(pmul(c,C,9),psi,9),k(2)), pmul(pmul(c,c,9),psib,9)),n21))
    m=pscale(padd(padd(v[0],v[1]),v[2]),k(Fr(1,3)))
    return [padd(v[0],m,-1),padd(v[1],m,-1)]
E1=extra_t()
# cross-check against direct 3-edge centre-manifold construction at kappa=1/2 (t=1) and kappa=3 (t=-2/3)
def direct(kap):
    t=(1-kap)/kap; psi=pscale(psi3_t(),k(t)); psib=pconj(psi,SW4); N=dyad_model(ZERO)
    v=[compose(N,[padd(c,psi),padd(C,psib)],D,4) for c,C in vars4()]
    S=padd(padd(v[0],v[1]),v[2]); F=[padd(x,pscale(S,k(-kap/3))) for x in v]
    mean=pscale(padd(padd(F[0],F[1]),F[2]),k(Fr(1,3)))
    inv= not padd(degpart(mean,3),pscale(psi,lam),-1)
    red=[padd(F[i],mean,-1) for i in range(2)]
    ok5=all(not padd(degpart(red[i],5),padd(f5base[i],pscale(E1[i],k(t))),-1) for i in range(2))
    return inv,ok5
for kap in (Fr(1,2),Fr(3),Fr(7,5)): print('kappa',kap,'(invariance, quintic=f5+tE):',direct(kap))
# columns: L3 (kappa-free), Phi1: v3 kappa-free, v5 = L1(f5base) + t L1(E1)
def to_sp(r): return sp.Rational(r.a.numerator,r.a.denominator)+sp.Rational(r.b.numerator,r.b.denominator)*sp.sqrt(3)
t=sp.symbols('t')
colsA=[];
for kind,P in basis:
    if kind=='3': colsA.append((flatten([{},{}],L3_of(P)),None))
    else: colsA.append((flatten(L1_of(P,f3),L1_of(P,f5base)),flatten([{},{}],L1_of(P,E1))))
b=d5_of(iu*mu)
keys=sorted(set().union(*[c[0].keys() for c in colsA],*[c[1].keys() for c in colsA if c[1]],b.keys()),key=str)
def col(c): 
    base=[to_sp(c[0].get(kk,R())) for kk in keys]
    if c[1] is None: return sp.Matrix(base)
    return sp.Matrix([x+t*to_sp(c[1].get(kk,R())) for x,kk in zip(base,keys)])
A=sp.Matrix.hstack(*[col(c) for c in colsA]); bv=sp.Matrix([to_sp(b.get(kk,R())) for kk in keys])
# eliminate: kappa-free L3 columns first (exact), then small t-dependent system
L3m=A[:, :24]; Pm=A[:,24:]
# left null space of L3 block: rows annihilating L3
NL=L3m.T.nullspace()
Q=sp.Matrix.hstack(*NL).T   # (96-rank) x 96
QP=sp.simplify(Q*Pm); Qb=sp.simplify(Q*bv)
assert L3m.rank()==23
# reduce QP rows: keep independent rows of [QP|Qb] generically
M=QP.row_join(Qb)
# generic row selection, then t-dependence of the 9x9 minor
Msub=M.subs(t,sp.Rational(3,7)); rk=Msub.rank(); assert rk==9 and QP.subs(t,sp.Rational(3,7)).rank()==8
ridx=[]; cur=sp.zeros(0,M.shape[1])
for i in range(M.shape[0]):
    trial=cur.col_join(Msub[i,:])
    if trial.rank()>cur.rank(): cur=trial; ridx.append(i)
    if len(ridx)==rk: break
d=sp.simplify(M.extract(ridx,list(range(9))).det())
print('9x9 minor of [Q*Phi1(t) | Q*b], t=(1-kappa)/kappa :',d)
ok = d!=0 and sp.diff(d,t)==0
print('PASS: minor is a nonzero constant in t => obstruction for every kappa outside {0,2}' if ok else 'FAIL')
sys.exit(0 if ok else 1)
