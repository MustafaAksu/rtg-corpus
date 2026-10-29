"""OFN_PSI_KAPPA_EXTENSION_v0_1 (OFN co-owner SESSION, 19 Oct 2026).
Extends FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1 (body reused verbatim below) from kappa=1 on C to kappa != 0,1,2 via the
formal centre manifold psi3 = (1-kappa)/(kappa*lam) * (n21/3) * sum_e c_e^2 cbar_e of the hyperbolic closure mode.
Reduced map through degree 5 = kappa=1 map + E_kappa (a-independent). Checks: (i) psi3 invariance and reduced map
verified by direct 3-edge construction; (ii) single-dyad N_a == N through degree 5 for a in R*mu (identical, not
only conjugate); (iii) obstruction for a in i*R*mu persists for every sampled kappa. Exit 0 iff all hold.
Original header:
FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1 (SESSION, 19 Oct 2026)
Transported kappa=1 model f_a = P o (g_a^{-1} n g_a)^{x3} on the closure plane C, n = DYAD-ALG-NF6 one-step jet,
g_a(z) = z + a z^2 zbar (the only lambda-equivariant cubic chart change). Exact arithmetic in Q(sqrt3)(i).
Test: is f_a formally conjugate to f_0 through degree 5, allowing equivariant tangent-to-identity Phi3 and the
complex-linear stabilizer of the common cubic? (Phi2, Phi4 must vanish; Phi5 and non-equivariant parts cannot act.)
Expected: conjugate iff a in R*mu (Cent(N) clock-gauge direction); obstruction for a in i*R*mu. Exit 0 iff all checks pass."""
from fractions import Fraction as Fr
import itertools, sys
class R:  # Q(sqrt3)
    __slots__=('a','b')
    def __init__(s,a=0,b=0): s.a=Fr(a); s.b=Fr(b)
    def __add__(s,o): return R(s.a+o.a,s.b+o.b)
    def __sub__(s,o): return R(s.a-o.a,s.b-o.b)
    def __mul__(s,o): return R(s.a*o.a+3*s.b*o.b, s.a*o.b+s.b*o.a)
    def __neg__(s): return R(-s.a,-s.b)
    def iszero(s): return s.a==0 and s.b==0
    def inv(s):
        n=s.a*s.a-3*s.b*s.b; return R(s.a/n,-s.b/n)
    def __repr__(s): return f"{s.a}+{s.b}r3"
class K:  # Q(sqrt3)(i)
    __slots__=('re','im')
    def __init__(s,re=None,im=None): s.re=re or R(); s.im=im or R()
    def __add__(s,o): return K(s.re+o.re,s.im+o.im)
    def __sub__(s,o): return K(s.re-o.re,s.im-o.im)
    def __mul__(s,o): return K(s.re*o.re-s.im*o.im, s.re*o.im+s.im*o.re)
    def __neg__(s): return K(-s.re,-s.im)
    def conj(s): return K(s.re,-s.im)
    def iszero(s): return s.re.iszero() and s.im.iszero()
ZERO=K(); ONE=K(R(1))
def k(a=0,b=0,c=0,d=0): return K(R(a,b),R(c,d))
# polynomials: dict {exponent tuple: K}; variables count nv
def padd(p,q,sgn=1):
    r=dict(p)
    for e,c in q.items():
        r[e]=r.get(e,ZERO)+(c if sgn==1 else -c)
    return {e:c for e,c in r.items() if not c.iszero()}
def pmul(p,q,D):
    r={}
    for e1,c1 in p.items():
        d1=sum(e1)
        for e2,c2 in q.items():
            if d1+sum(e2)>D: continue
            e=tuple(x+y for x,y in zip(e1,e2)); r[e]=r.get(e,ZERO)+c1*c2
    return {e:c for e,c in r.items() if not c.iszero()}
def pscale(p,c): return {e:v*c for e,v in p.items() if not (v*c).iszero()}
def ppow(p,n,D,nv):
    r={tuple([0]*nv):ONE}
    for _ in range(n): r=pmul(r,p,D)
    return r
def compose(f,subs,D,nv):  # f in variables (subs list) -> polynomial in nv vars
    cache={}
    r={}
    for e,c in f.items():
        term={tuple([0]*nv):c}
        for i,ex in enumerate(e):
            if ex:
                key=(i,ex)
                if key not in cache: cache[key]=ppow(subs[i],ex,D,nv)
                term=pmul(term,cache[key],D)
        r=padd(r,term)
    return r
def pconj(p,swap):  # conj coefficients and permute exponent positions via swap
    return {tuple(e[swap[i]] for i in range(len(e))):c.conj() for e,c in p.items()}
def degpart(p,d): return {e:c for e,c in p.items() if sum(e)==d}
D=5
lam=k(Fr(1,2),0,0,Fr(1,2)); lamb=lam.conj()
n21=k(Fr(1,8),0,0,Fr(-7,72)); n32=k(Fr(-5,432),0,0,Fr(23,3888)); n05=k(Fr(43,17280),0,0,Fr(-227,155520))
# single-dyad polys in (z,Z)
def dyad_model(a):
    n={(1,0):lam,(2,1):n21,(3,2):n32,(0,5):n05}
    g={(1,0):ONE}
    if not a.iszero(): g[(2,1)]=a
    sw=[1,0]
    nb=pconj(n,sw); gb=pconj(g,sw)
    gi={(1,0):ONE}
    for _ in range(3):
        gig=compose(g,[gi,pconj(gi,sw)],D,2)
        gi=padd({(1,0):ONE}, padd(gig,gi,-1),-1)
        gi=padd(gi,{},1)
    ng=compose(n,[g,gb],D,2)
    return compose(gi,[ng,pconj(ng,sw)],D,2)
# network on C: vars (w1,w2,W1,W2)
SW4=[2,3,0,1]
def onC(N):
    w1={(1,0,0,0):ONE}; w2={(0,1,0,0):ONE}; W1={(0,0,1,0):ONE}; W2={(0,0,0,1):ONE}
    w3=padd(pscale(w1,-ONE),pscale(w2,-ONE)); W3=padd(pscale(W1,-ONE),pscale(W2,-ONE))
    v=[compose(N,[w1,W1],D,4),compose(N,[w2,W2],D,4),compose(N,[w3,W3],D,4)]
    m=pscale(padd(padd(v[0],v[1]),v[2]),k(Fr(1,3)))
    return [padd(v[0],m,-1),padd(v[1],m,-1)]
f0=onC(dyad_model(ZERO))
f3=[degpart(c,3) for c in f0]; f5=[degpart(c,5) for c in f0]
# linear unknown-building: represent unknown-linear expressions as dict monomial->{var: K}
def lin_terms(Phi_basis):  # not used
    pass
def apply_D(F,P):  # F: 2 comps polys in 4 vars; P: 2 comps polys; real derivative
    Pb=[pconj(p,SW4) for p in P]
    out=[]
    for i in range(2):
        acc={}
        for j in range(2):
            for idx,Q in ((j,P[j]),(j+2,Pb[j])):
                der={}
                for e,c in F[i].items():
                    if e[idx]:
                        ee=list(e); ee[idx]-=1; der[tuple(ee)]=der.get(tuple(ee),ZERO)+c*k(e[idx])
                acc=padd(acc,pmul(der,Q,99))
        out.append(acc)
    return out
lamv=[lam,lam,lamb,lamb]
def scale_at_lam(p):  # p(lambda w)
    r={}
    for e,c in p.items():
        f=c
        for i,ex in enumerate(e):
            for _ in range(ex): f=f*lamv[i]
        r[e]=f
    return r
def L3_of(Phi3):
    a=apply_D(f3,Phi3)
    # DPhi3(lam w)[f3]: derivative of Phi3, evaluated at lam w, applied to f3
    f3b=[pconj(p,SW4) for p in f3]
    b=[]
    for i in range(2):
        acc={}
        for idx,Q in ((0,f3[0]),(1,f3[1]),(2,f3b[0]),(3,f3b[1])):
            der={}
            for e,c in Phi3[i].items():
                if e[idx]:
                    ee=list(e); ee[idx]-=1; der[tuple(ee)]=der.get(tuple(ee),ZERO)+c*k(e[idx])
            acc=padd(acc,pmul(scale_at_lam(der),Q,99))
        b.append(acc)
    return [padd(a[i],b[i],-1) for i in range(2)]
def L1_of(Phi1,F):
    sub=compose_lin(Phi1,F)
    d=apply_D(F,Phi1)
    return [padd(sub[i],d[i],-1) for i in range(2)]
def compose_lin(Phi1,F):  # Phi1 linear complex (in w1,w2 only) applied to F
    out=[]
    for i in range(2):
        acc={}
        for e,c in Phi1[i].items():
            j=0 if e==(1,0,0,0) else 1
            acc=padd(acc,pscale(F[j],c))
        out.append(acc)
    return out
# basis of unknowns: each unknown is (complex coefficient real part, imag part) on a basis map
mons3=[(2,0,1,0),(2,0,0,1),(1,1,1,0),(1,1,0,1),(0,2,1,0),(0,2,0,1)]
basis=[]  # list of (kind, pair-of-polys)
for comp in range(2):
    for m in mons3:
        for unit in (ONE,k(0,0,1,0)):
            P=[{},{}]; P[comp]={m:unit}; basis.append(('3',P))
lin=[(1,0,0,0),(0,1,0,0)]
for comp in range(2):
    for m in lin:
        for unit in (ONE,k(0,0,1,0)):
            P=[{},{}]; P[comp]={m:unit}; basis.append(('1',P))
cols=[]
for kind,P in basis:
    if kind=='3': v5=L3_of(P); v3=[{},{}]
    else: v5=L1_of(P,f5); v3=L1_of(P,f3)
    cols.append((v3,v5))
def flatten(v3,v5):  # -> dict key->R (real & imag parts)
    out={}
    for tag,v in (('3',v3),('5',v5)):
        for i in range(2):
            for e,c in v[i].items():
                out[(tag,i,e,'re')]=c.re; out[(tag,i,e,'im')]=c.im
    return out
def rank(rows):  # rows: list of list of R ; gaussian elimination over Q(sqrt3)
    rows=[r[:] for r in rows]; rk=0; ncol=len(rows[0]) if rows else 0
    for c in range(ncol):
        piv=None
        for r in range(rk,len(rows)):
            if not rows[r][c].iszero(): piv=r; break
        if piv is None: continue
        rows[rk],rows[piv]=rows[piv],rows[rk]
        inv=rows[rk][c].inv()
        rows[rk]=[x*inv for x in rows[rk]]
        for r in range(len(rows)):
            if r!=rk and not rows[r][c].iszero():
                fac=rows[r][c]; rows[r]=[x-fac*y for x,y in zip(rows[r],rows[rk])]
        rk+=1
    return rk
flats=[flatten(*c) for c in cols]
def system_rank(rhss):
    keys=sorted(set().union(*[f.keys() for f in flats],*[r.keys() for r in rhss]),key=str)
    A=[[f.get(kk,R()) for f in flats] for kk in keys]
    Ab=[row+[r.get(kk,R()) for r in rhss] for row,kk in zip(A,keys)]
    return rank(A),rank(Ab)
def d5_of(a):
    fa=onC(dyad_model(a))
    assert all(not padd(degpart(fa[i],3),f3[i],-1) for i in range(2)), 'cubic differs'
    assert all(not degpart(fa[i],d) for i in range(2) for d in (2,4)), 'even terms'
    return flatten([{},{}],[padd(degpart(fa[i],5),f5[i],-1) for i in range(2)])

iu=k(0,0,1,0); mu=k(Fr(-1,2),0,0,Fr(-2,3))
f5base=[dict(x) for x in f5]
W_=None
def vars4():
    w1={(1,0,0,0):ONE}; w2={(0,1,0,0):ONE}; W1={(0,0,1,0):ONE}; W2={(0,0,0,1):ONE}
    w3=padd(pscale(w1,-ONE),pscale(w2,-ONE)); W3=padd(pscale(W1,-ONE),pscale(W2,-ONE))
    return [(w1,W1),(w2,W2),(w3,W3)]
def psi3(kap):
    M={}
    for c,C in vars4(): M=padd(M,pmul(pmul(c,c,9),C,9))
    return pscale(M,k(Fr(1)-kap)*n21*k(Fr(1,3))*lamb*K(R(Fr(1)/kap)))
def extra(kap):
    psi=psi3(kap); psib=pconj(psi,SW4); v=[]
    for c,C in vars4():
        v.append(pscale(padd(pscale(pmul(pmul(c,C,9),psi,9),k(2)), pmul(pmul(c,c,9),psib,9)),n21))
    m=pscale(padd(padd(v[0],v[1]),v[2]),k(Fr(1,3)))
    return [padd(v[0],m,-1),padd(v[1],m,-1)]
def direct(kap,a):
    N=dyad_model(a); psi=psi3(kap); psib=pconj(psi,SW4)
    v=[compose(N,[padd(c,psi),padd(C,psib)],D,4) for c,C in vars4()]
    S=padd(padd(v[0],v[1]),v[2]); F=[padd(x,pscale(S,k(-kap/3))) for x in v]
    mean=pscale(padd(padd(F[0],F[1]),F[2]),k(Fr(1,3)))
    return (not padd(degpart(mean,3),pscale(psi,lam),-1)), [padd(F[i],mean,-1) for i in range(2)]
ok=True
def check(label,cond):
    global ok; ok&=bool(cond); print(('PASS ' if cond else 'FAIL ')+label)
check('N_a == N through degree 5 for a=mu and a=mu/6', not padd(dyad_model(mu),dyad_model(ZERO),-1) and not padd(dyad_model(lamb*n21),dyad_model(ZERO),-1))
check('N_a != N for a=i*mu', bool(padd(dyad_model(iu*mu),dyad_model(ZERO),-1)))
for kap in (Fr(1,2),Fr(3)):
    inv,Cp=direct(kap,ZERO); E=extra(kap)
    check(f'kappa={kap}: centre-manifold invariance at degree 3', inv)
    check(f'kappa={kap}: reduced cubic kappa-independent', all(not padd(degpart(Cp[i],3),f3[i],-1) for i in range(2)))
    check(f'kappa={kap}: reduced quintic = f5(kappa=1) + E_kappa', all(not padd(degpart(Cp[i],5),padd(f5base[i],E[i]),-1) for i in range(2)))
    inva,Cpa=direct(kap,iu*mu); fa=onC(dyad_model(iu*mu))
    check(f'kappa={kap}: E_kappa is a-independent (a=i*mu)', all(not padd(degpart(Cpa[i],5),padd(degpart(fa[i],5),E[i]),-1) for i in range(2)))
def d5b(a):
    fa=onC(dyad_model(a)); return flatten([{},{}],[padd(degpart(fa[i],5),f5base[i],-1) for i in range(2)])
for kap in (Fr(1),Fr(1,2),Fr(3,2),Fr(7,5),Fr(3),Fr(-1)):
    E=extra(kap); f5=[padd(f5base[i],E[i]) for i in range(2)]
    cols=[]
    for kind,P in basis:
        if kind=='3': v5=L3_of(P); v3=[{},{}]
        else: v5=L1_of(P,f5); v3=L1_of(P,f3)
        cols.append((v3,v5))
    flats=[flatten(*c) for c in cols]
    check(f'kappa={kap}: a=i*mu obstructed on reduced map', system_rank([d5b(iu*mu)])==(31,32))
    check(f'kappa={kap}: a in C gives exactly one real obstruction direction', system_rank([d5b(ONE),d5b(iu)])==(31,32))
    check(f'kappa={kap}: negative control random quintic obstructed', system_rank([flatten([{},{}],[{(3,0,2,0):k(1)},{}])])==(31,32))
print('ALL PASS' if ok else 'SOME FAIL'); sys.exit(0 if ok else 1)
