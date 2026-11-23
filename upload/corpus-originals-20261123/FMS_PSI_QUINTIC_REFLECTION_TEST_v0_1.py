"""FMS_PSI_QUINTIC_REFLECTION_TEST_v0_1 (SESSION, 19 Oct 2026).
Is the Z2-reflected pair m(b) = 2 m* - m(a) formally conjugate at degree 5?
Any formal conjugacy is phi = B o psi, B in Stab(f3) = T^2 x| <swap>, and (B^-1 f_b B)_5 - f_a5 must lie in Im L3 (exact
degree-5 linearity). With w = e^{i(alpha-beta)}, z = e^{-6 i beta} the left-null conditions are Laurent polynomials in (w,z).
 (P1) exact pair at kappa=1 (a=0): Groebner basis = [1] with and without swap  -> not conjugate.
 (P2) controls: identical pair gives (w^3-1, z-1); B=diag(lam,1)-conjugate gives (w^3+1, z-1)  -> solvable, as they must be.
 (P3) symbolic family a = r i mu, b = reflection partner, t in {0, 1, -1/2}: elimination ideal in r is linear with the
      single root r* = reflection fixed point (a = b).
 (P4) r and t both symbolic: elimination ideal in (r,t) = <1026 r - 17 sqrt3 - 72 sqrt3 t>, the fixed-point line m(a)=m*(t).
      Hence for every kappa (kappa=2: odd category) no nontrivial reflected pair is conjugate at degree 5.
Requires FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py and FMS_PSI_QUINTIC_KAPPA_ALL_v0_1.py in the same directory.
Exit 0 iff ALL PASS."""
import sympy as sp

import sys
src=open('FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py').read().split("iu=k(0,0,1,0)")[0]
exec(src)
iu=k(0,0,1,0); mu=k(Fr(-1,2),0,0,Fr(-2,3))
SW4=(2,3,0,1)
def nullspace(rows,ncol):  # right nullspace of matrix rows (list of lists of R)
    M=[r[:] for r in rows]; piv=[]; rk=0
    for c in range(ncol):
        p=next((r for r in range(rk,len(M)) if not M[r][c].iszero()),None)
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]; inv=M[rk][c].inv(); M[rk]=[x*inv for x in M[rk]]
        for r in range(len(M)):
            if r!=rk and not M[r][c].iszero():
                f=M[r][c]; M[r]=[x-f*y for x,y in zip(M[r],M[rk])]
        piv.append(c); rk+=1
    free=[c for c in range(ncol) if c not in piv]; out=[]
    for fc in free:
        v=[R() for _ in range(ncol)]; v[fc]=R(1)
        for i,pc in enumerate(piv): v[pc]=-M[i][fc]
        out.append(v)
    return out
# --- linear coordinate maps on (w1,w2) and S3 action --------------------------------
def X(i): e=[0,0,0,0]; e[i]=1; return {tuple(e):ONE}
def lin(a,b,c,d):  # (w1,w2) -> (a w1 + b w2, c w1 + d w2) as subs list incl. conjugates (a..d in K)
    p=padd(pscale(X(0),a),pscale(X(1),b)); q=padd(pscale(X(0),c),pscale(X(1),d))
    return [p,q,pconj(p,SW4),pconj(q,SW4)]
def act(P,L,Linv):  # (sigma.P)(w) = Linv P(L w); L,Linv = (a,b,c,d)
    s=lin(*L); Q=[compose(P[i],s,D,4) for i in range(2)]
    a,b,c,d=Linv
    return [padd(pscale(Q[0],a),pscale(Q[1],b)),padd(pscale(Q[0],c),pscale(Q[1],d))]
O=ONE; Z=ZERO; m1=k(-1)
tau=((Z,O,O,Z),(Z,O,O,Z))                 # (w1,w2)->(w2,w1)
cyc=((Z,O,m1,m1),(m1,m1,O,Z))             # (w1,w2)->(w2,w3), inverse
def S3avg(P):
    G=[P]; out=P
    els=[P]
    # group elements: c^k, tau c^k
    def ap(P,g): return act(P,g[0],g[1])
    terms=[]; Q=P
    for _ in range(3):
        terms.append(Q); terms.append(ap(Q,tau)); Q=ap(Q,cyc)
    acc=[{},{}]
    for T in terms: acc=[padd(acc[i],T[i]) for i in range(2)]
    return [pscale(acc[i],k(Fr(1,6))) for i in range(2)]
# sanity: f0 is S3-equivariant
assert all(not padd(S3avg(f0)[i],f0[i],-1) for i in range(2)),'f0 not S3-equivariant'
# --- chiral coordinates u = w1 + lam w2, v = w1 + lamb w2 -----------------------------
r3=k(0,0,0,1)  # i*sqrt3 ... k(a,b,c,d)= (a+b r3) + i(c+d r3): here i*sqrt3
inv_isq3=k(0,0,0,Fr(-1,3))  # 1/(i sqrt3) = -i/sqrt3 = -i sqrt3/3
# w2 = (u-v)/(i sqrt3), w1 = u - lam w2  (vars: u=0, v=1)
w2c=padd(pscale(X(0),inv_isq3),pscale(X(1),inv_isq3*m1))
w1c=padd(X(0),pscale(w2c,m1*lam))
to_w_from_uv=[w1c,w2c,pconj(w1c,SW4),pconj(w2c,SW4)]
uc=padd(X(0),pscale(X(1),lam)); vc=padd(X(0),pscale(X(1),lamb))
to_uv_from_w=[uc,vc,pconj(uc,SW4),pconj(vc,SW4)]
def to_chiral(P):  # map in w-coords -> map in (u,v) coords
    Q=[compose(P[i],to_w_from_uv,D,4) for i in range(2)]
    return [padd(Q[0],pscale(Q[1],lam)),padd(Q[0],pscale(Q[1],lamb))]
def from_chiral(Pc):
    Q=[compose(Pc[i],to_uv_from_w,D,4) for i in range(2)]
    # (w1,w2) components from (U,V): w2=(U-V)/(i sqrt3), w1=U-lam w2
    W2=padd(pscale(Q[0],inv_isq3),pscale(Q[1],inv_isq3*m1)); W1=padd(Q[0],pscale(W2,m1*lam))
    return [W1,W2]
# --- admissible space V -------------------------------------------------------------
import itertools as it
mons=[e for e in it.product(range(6),repeat=4) if sum(e)==5 and ((e[0]+e[1]-e[2]-e[3])%6==1)]
Vgen=[]; labels=[]
for e in mons:
    for c,nm in ((ONE,'1'),(iu,'i')):
        Pc=[{e:c},{}]
        P=S3avg(from_chiral(Pc))
        if any(P[i] for i in range(2)): Vgen.append(P); labels.append((e,nm))
def flat5(P): return flatten([{},{}],[degpart(P[i],5) for i in range(2)])
Vfl=[flat5(P) for P in Vgen]
keys=sorted(set().union(*[f.keys() for f in flats],*[f.keys() for f in Vfl]),key=str)
vec=lambda f:[f.get(kk,R()) for kk in keys]
# basis of V
Vrows=[vec(f) for f in Vfl]
dimV=rank(Vrows)
# independent subset
basisV=[];bl=[]
for v,l in zip(Vrows,labels):
    if rank(basisV+[v])>len(basisV): basisV.append(v); bl.append(l)
Acols=[vec(f) for f in flats]
# intersection V cap ImA: nullspace of [A | -V] (columns)
ncA=len(Acols); ncV=len(basisV)
cols_all=Acols+[[ -x for x in v] for v in basisV]
rowsM=[[c[r] for c in cols_all] for r in range(len(keys))]
ns=nullspace(rowsM,ncA+ncV)
inter=[n[ncA:] for n in ns]
dimI=rank(inter) if inter else 0
print('dim V (S3+lambda-equivariant quintic, real) =',dimV)
print('dim V cap Im A =',dimI,'  => first-order quintic moduli in S3 class =',dimV-dimI)
# functional on V (coordinates c in basisV) annihilating the intersection
ell=nullspace([r[:] for r in inter],ncV) if inter else None
print('number of independent functionals =',len(ell))
def coordsV(f):  # express key-vector of an element of V in basisV coordinates
    v=vec(f); cols=basisV+[v]
    rows=[[c[r] for c in cols] for r in range(len(keys))]
    n=nullspace(rows,ncV+1); n=[x for x in n if not x[-1].iszero()][0]
    s=n[-1].inv(); return [ -x*s for x in n[:-1]]
def I_of(f,l): 
    c=coordsV(f); acc=R()
    for x,y in zip(c,l): acc=acc+x*y
    return acc

idx=[];tmp=[]
for j,v in enumerate(Vrows):
    if rank(tmp+[v])>len(tmp): tmp.append(v); idx.append(j)
basisP=[Vgen[j] for j in idx]
def comb(c):
    acc=[{},{}]
    for x,P in zip(c,basisP):
        if not x.iszero(): acc=[padd(acc[i],pscale(P[i],K(x))) for i in range(2)]
    return acc
def comp4(F,G): return [compose(F[i],[G[0],G[1],pconj(G[0],SW4),pconj(G[1],SW4)],D,4) for i in range(2)]
def six(f):
    g=f
    for _ in range(5): g=comp4(f,g)
    return g
def Delta6(f,which):  # degree-6 part of |X|^2 o F6 - |X|^2, X = u (0) or v (1), chiral coords
    Fc=to_chiral(six(f))
    X=Fc[which]; Xb=pconj(X,SW4)
    full=pmul(X,Xb,6)
    return {e:c for e,c in full.items() if sum(e)==6}
U3V3=(3,0,0,3); V3U3=(0,3,3,0)
def inv(f):
    dA=Delta6(f,0); dB=Delta6(f,1)
    return dA.get(U3V3,ZERO), dB.get(U3V3,ZERO)
def kf(c): return f"({c.re}) + i({c.im})"

iu=k(0,0,1,0); mu=k(Fr(-1,2),0,0,Fr(-2,3))

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


idx=[];tmp=[]
for j,v in enumerate(Vrows):
    if rank(tmp+[v])>len(tmp): tmp.append(v); idx.append(j)
basisP=[Vgen[j] for j in idx]
def comb(c):
    acc=[{},{}]
    for x,P in zip(c,basisP):
        if not x.iszero(): acc=[padd(acc[i],pscale(P[i],K(x))) for i in range(2)]
    return acc
def comp4(F,G): return [compose(F[i],[G[0],G[1],pconj(G[0],SW4),pconj(G[1],SW4)],D,4) for i in range(2)]
def six(f):
    g=f
    for _ in range(5): g=comp4(f,g)
    return g
def Delta6(f,which):  # degree-6 part of |X|^2 o F6 - |X|^2, X = u (0) or v (1), chiral coords
    Fc=to_chiral(six(f))
    X=Fc[which]; Xb=pconj(X,SW4)
    full=pmul(X,Xb,6)
    return {e:c for e,c in full.items() if sum(e)==6}
U3V3=(3,0,0,3); V3U3=(0,3,3,0)
def inv(f):
    dA=Delta6(f,0); dB=Delta6(f,1)
    return dA.get(U3V3,ZERO), dB.get(U3V3,ZERO)
def kf(c): return f"({c.re}) + i({c.im})"

iu=k(0,0,1,0); mu=k(Fr(-1,2),0,0,Fr(-2,3))

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

def to_sp(r): return sp.Rational(r.a.numerator,r.a.denominator)+sp.Rational(r.b.numerator,r.b.denominator)*sp.sqrt(3)
def ksp(c): return to_sp(c.re)+sp.I*to_sp(c.im)
s=k(0,Fr(17,513)); b_par=s*iu*mu
fa=f0
FaC=to_chiral([degpart(fa[0],5),degpart(fa[1],5)])
L3c=[to_chiral(L3_of(P)) for kind,P in basis if kind=='3']
import itertools as _it
allm=[e for e in _it.product(range(6),repeat=4) if sum(e)==5 and (e[0]+e[1]-e[2]-e[3])%6==1]
keys=[(i,e) for i in range(2) for e in allm]
def rvec(C):  # real flatten exact (R entries)
    out=[]
    for (i,e) in keys:
        c=C[i].get(e,ZERO); out+= [c.re,c.im]
    return out
cols=[rvec(C) for C in L3c]
rows=[[col[r] for col in cols] for r in range(2*len(keys))]   # matrix (2K x 24)
# left null: y with y^T A = 0  <=> nullspace of A^T
At=[[rows[r][c] for r in range(len(rows))] for c in range(len(cols))]
Y=nullspace(At,len(rows)); print('left null dim',len(Y))
w,z=sp.symbols('w z')
def delta_entries(C,swap):
    if swap: C=[{(e[1],e[0],e[3],e[2]):c for e,c in C[1].items()},{(e[1],e[0],e[3],e[2]):c for e,c in C[0].items()}]
    ent={}
    for i in range(2):
        for e,c in C[i].items():
            n1=e[0]-e[2]; n2=e[1]-e[3]; kk=(n1-1) if i==0 else n1; eps=1 if (n1+n2)==-5 else 0
            ent[(i,e)]=ksp(c)*w**kk*z**eps
    return ent
def chiral_lin(f,s1,s2):  # B f B^{-1}, B=diag(s1,s2) in chiral coords, |s|=1
    fc=to_chiral(f); sub=[pscale(X(0),s1.conj()),pscale(X(1),s2.conj()),pscale(X(2),s1),pscale(X(3),s2)]
    g=[compose(fc[j],sub,D,4) for j in range(2)]; return from_chiral([pscale(g[0],s1),pscale(g[1],s2)])
DOM=sp.QQ.algebraic_field(sp.sqrt(3),sp.I)
def test(fb,label):
    FbC=to_chiral([degpart(fb[0],5),degpart(fb[1],5)]); out={}
    for swap in (False,True):
        ent=delta_entries(FbC,swap); eqs=[]
        for y in Y:
            expr=0
            for n,(i,e) in enumerate(keys):
                D=ent.get((i,e),0)-ksp(FaC[i].get(e,ZERO))
                Dc=sp.conjugate(D).subs({sp.conjugate(w):1/w,sp.conjugate(z):1/z})
                yr=to_sp(y[2*n]); yi=to_sp(y[2*n+1])
                if yr!=0: expr+=yr*(D+Dc)/2
                if yi!=0: expr+=yi*(D-Dc)/(2*sp.I)
            num=sp.expand(sp.numer(sp.together(sp.expand(expr))))
            if num!=0: eqs.append(num)
        if not eqs: out[swap]=False; print(label,'swap',swap,'all equations vanish identically'); continue
        G=sp.groebner(eqs,w,z,order='lex',domain=DOM)
        out[swap]=(list(G.exprs)==[1]); print(label,'swap',swap,'#eqs',len(eqs),'G=[1]:',out[swap],'' if out[swap] else [sp.factor(g) for g in G.exprs][:3])
    return out

OK=True
r_=test(onC(dyad_model(b_par)),'(P1) REFLECTED PAIR kappa=1, a=0, b=(17sqrt3/513) i mu:'); OK&=all(r_.values())
r_=test(fa,'(P2) CONTROL identical pair:'); OK&=(not r_[False])
r_=test(chiral_lin(fa,lam,ONE),'(P2) CONTROL B=diag(lam,1) conjugate:'); OK&=(not r_[False])
E1=extra_t()
r=sp.symbols('r',real=True)
# chiral quintic of f_{t, a} for a = x * i mu is polynomial in x; get it by exact interpolation in x (degree <= 2 expected)
def chq(t,x):
    fa_=onC(dyad_model(k(x)*iu*mu)); f=[padd(fa_[i],pscale(E1[i],k(t))) for i in range(2)]
    return to_chiral([degpart(f[0],5),degpart(f[1],5)])
def interp(t):
    pts=[Fr(0),Fr(1),Fr(2),Fr(3)]
    data=[chq(t,x) for x in pts]; poly={}
    for (i,e) in keys:
        ys=[ksp(d[i].get(e,ZERO)) for d in data]
        p=sp.expand(sp.interpolate(list(zip([sp.Rational(x) for x in pts],ys)),r))
        if p!=0: poly[(i,e)]=p
    return poly
ok_sym=True
for t in (Fr(0),Fr(1),Fr(-1,2)):
    P=interp(t)
    degs={sp.degree(p,r) for p in P.values()}
    # reference model a: x=r ; partner b: x = R(r) with m(b)=2m*-m(a); m(x i mu)=x|mu|^2=19x/12
    mstar=sp.Rational(17,648)*sp.sqrt(3)+sp.sqrt(3)*sp.Rational(t.numerator,t.denominator)/9
    Rb=sp.expand((2*mstar-sp.Rational(19,12)*r)/sp.Rational(19,12))
    out={}
    for swap in (False,True):
        eqs=[]
        for y in Y:
            expr=0
            for n,(i,e) in enumerate(keys):
                pa=P.get((i,e),0); pb=P.get((i,e),0)
                if swap:
                    i2=1-i; e2=(e[1],e[0],e[3],e[2]); pb=P.get((i2,e2),0)
                n1=e[0]-e[2]; n2=e[1]-e[3]; kk=(n1-1) if i==0 else n1; eps=1 if (n1+n2)==-5 else 0
                Dv=(pb.subs(r,Rb) if pb!=0 else 0)*w**kk*z**eps - pa
                Dc=sp.conjugate(Dv).subs({sp.conjugate(w):1/w,sp.conjugate(z):1/z,sp.conjugate(r):r})
                yr=to_sp(y[2*n]); yi=to_sp(y[2*n+1])
                if yr!=0: expr+=yr*(Dv+Dc)/2
                if yi!=0: expr+=yi*(Dv-Dc)/(2*sp.I)
            num=sp.expand(sp.numer(sp.together(sp.expand(expr))))
            if num!=0: eqs.append(num)
        G=sp.groebner(eqs,w,z,r,order='lex',domain=DOM)
        el=[g for g in G.exprs if not g.has(w) and not g.has(z)]
        print(f't={t} swap={swap} deg_r(f5)={degs} #eqs={len(eqs)} elimination ideal in r:',[sp.factor(g) for g in el] if el else 'none', ' G=[1]:',list(G.exprs)==[1])
        out[swap]=el
    # exceptional r: real roots of elimination polynomials
    for swap,el in out.items():
        if el and el!=[1]:
            sols=sp.solve(el,r); fixed=sp.nsimplify(sp.solve(sp.Rational(19,12)*r-mstar,r)[0])
            print('   solutions r:',sols,'  reflection fixed point r* =',fixed,'  only fixed point:',all(sp.simplify(x-fixed)==0 for x in (sols.values() if isinstance(sols,dict) else [v for d in sols for v in d.values()])))
            ok_sym&= all(sp.simplify(x-fixed)==0 for x in (sols.values() if isinstance(sols,dict) else [v for d in sols for v in d.values()]))


print('(P3) symbolic reflected family: only the fixed point solves:',ok_sym); OK&=ok_sym
r,T=sp.symbols('r T',real=True)  # P4: symbolic t
def chq(t,x):
    fa_=onC(dyad_model(k(x)*iu*mu)); f=[padd(fa_[i],pscale(E1[i],k(t))) for i in range(2)]
    return to_chiral([degpart(f[0],5),degpart(f[1],5)])
# bilinear interpolation: f5 affine in x and in t
pts=[(Fr(0),Fr(0)),(Fr(1),Fr(0)),(Fr(0),Fr(1)),(Fr(1),Fr(1)),(Fr(2),Fr(3))]
data={p:chq(p[1],p[0]) for p in pts}
P={}
for key in keys:
    i,e=key; v=lambda x,t: ksp(data[(x,t)][i].get(e,ZERO))
    c00=v(Fr(0),Fr(0)); cx=v(Fr(1),Fr(0))-c00; ct=v(Fr(0),Fr(1))-c00; cxt=v(Fr(1),Fr(1))-c00-cx-ct
    poly=sp.expand(c00+cx*r+ct*T+cxt*r*T)
    assert sp.simplify(poly.subs({r:2,T:3})-v(Fr(2),Fr(3)))==0, 'not bilinear'
    if poly!=0: P[key]=poly
print('f5 bilinear in (r,t): verified at check point')
mstar=sp.Rational(17,648)*sp.sqrt(3)+sp.sqrt(3)*T/9
Rb=sp.expand((2*mstar-sp.Rational(19,12)*r)/sp.Rational(19,12))
ok4=True
for swap in (False,True):
    eqs=[]
    for y in Y:
        expr=0
        for n,(i,e) in enumerate(keys):
            pa=P.get((i,e),0)
            pb=P.get((1-i,(e[1],e[0],e[3],e[2])),0) if swap else P.get((i,e),0)
            n1=e[0]-e[2]; n2=e[1]-e[3]; kk=(n1-1) if i==0 else n1; eps=1 if (n1+n2)==-5 else 0
            Dv=(pb.subs(r,Rb) if pb!=0 else 0)*w**kk*z**eps - pa
            Dc=sp.conjugate(Dv).subs({sp.conjugate(w):1/w,sp.conjugate(z):1/z,sp.conjugate(r):r,sp.conjugate(T):T})
            yr=to_sp(y[2*n]); yi=to_sp(y[2*n+1])
            if yr!=0: expr+=yr*(Dv+Dc)/2
            if yi!=0: expr+=yi*(Dv-Dc)/(2*sp.I)
        num=sp.expand(sp.numer(sp.together(sp.expand(expr))))
        if num!=0: eqs.append(num)
    G=sp.groebner(eqs,w,z,r,T,order='lex',domain=DOM)
    el=[sp.factor(g) for g in G.exprs if not (g.has(w) or g.has(z))]
    print('swap',swap,' elimination ideal in (r,t):',el)
    fixed=sp.expand(sp.Rational(19,12)*r-mstar)
    ok4&= len(el)>0 and all(sp.rem(sp.expand(sp.numer(sp.together(g))), sp.expand(fixed*sp.Rational(12,19)*1026),r)==0 or sp.simplify(sp.numer(sp.together(g))/ (fixed))  .is_number for g in el)
print('(P4) symbolic (r,t): elimination ideal = fixed-point line only:',ok4)

OK&=ok4
print('ALL PASS' if OK else 'SOME FAIL'); sys.exit(0 if OK else 1)
