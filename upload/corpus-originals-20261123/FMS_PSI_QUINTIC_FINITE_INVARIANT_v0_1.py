"""FMS_PSI_QUINTIC_FINITE_INVARIANT_v0_1 (SESSION, 19 Oct 2026).
Upgrade of the phase-harmonic functional c to an invariant under ALL formal conjugacies (no S3 or first-order restriction).
Let f, f' be odd, lambda- and S3-equivariant reduced maps with the same cubic f3, phi any formal conjugacy, phi = B o psi.
 (E) Lie Stab(f3) = diagonal phase torus (dim_R 2)  =>  Stab(f3) = T^2 x| <swap>  (identity component is normal;
     its normalizer in GL2(C) is the monomial group; p,q != 0 force unit moduli).
 (F) psi tangent to identity: the degree-5 change is exactly f5 + L3(psi3) (quadratic psi3 terms cancel because the linear
     part is the scalar lam; non-equivariant psi5 vanishes by the completeness lemma). c_A, c_B depend only on the 5-jet.
     Check: every one of the 24 real equivariant cubic generators (non-S3 included), at two scales, and a large random
     non-S3 finite cubic conjugacy leave c_A and c_B exactly unchanged.
 (G) B in T^2: c_A -> exp(3i(beta-alpha)) c_A; swap: c_A -> conj(c_B) = c_A for S3 maps. Checked on f_{i mu}.
 => |c(kappa,a)|^2 is a formal conjugacy invariant of the class. With Re c fixed by kappa, f_a and f_b (same kappa) are
    formally non-conjugate unless Im c(b) = +/- Im c(a)  (finite a, any formal conjugacy).
Requires FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py in the same directory. Exit 0 iff ALL PASS."""
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


import sympy as sp
OK=True
def chk(lbl,b):
    global OK; OK&=bool(b); print(('PASS ' if b else 'FAIL ')+lbl)
# (E) Lie algebra of Stab(f3), computed from the actual chiral cubic
f3c=to_chiral(f3)
u_,v_,U_,V_=sp.symbols('u v U V')
def tosp(c): return to_sp(c.re)+sp.I*to_sp(c.im)
def to_sp(r): return sp.Rational(r.a.numerator,r.a.denominator)+sp.Rational(r.b.numerator,r.b.denominator)*sp.sqrt(3)
fs=[sum(tosp(c)*u_**e[0]*v_**e[1]*U_**e[2]*V_**e[3] for e,c in f3c[i].items()) for i in range(2)]
m=sp.symbols('m0:4'); nb=sp.symbols('n0:4')
M=sp.Matrix([[m[0],m[1]],[m[2],m[3]]]); Mb=sp.Matrix([[nb[0],nb[1]],[nb[2],nb[3]]])
Mx=M*sp.Matrix([u_,v_]); Mxb=Mb*sp.Matrix([U_,V_]); eqs=[]
for i in range(2):
    lhs=sum(sp.diff(fs[i],s)*d for s,d in zip((u_,v_),Mx))+sum(sp.diff(fs[i],s)*d for s,d in zip((U_,V_),Mxb))
    eqs+=sp.Poly(sp.expand(lhs-(M*sp.Matrix(fs))[i]),u_,v_,U_,V_).coeffs()
ra=sp.symbols('a0:4',real=True); rb=sp.symbols('b0:4',real=True)
sub={**{m[j]:ra[j]+sp.I*rb[j] for j in range(4)},**{nb[j]:ra[j]-sp.I*rb[j] for j in range(4)}}
re=[]
for e in eqs: e=sp.expand(e.subs(sub)); re+=[sp.re(e),sp.im(e)]
Amat=sp.Matrix([[sp.diff(e,s) for s in ra+rb] for e in re]); ns=Amat.nullspace()
diag_only=all(all(n[j]==0 for j in (0,1,2,3,5,6)) for n in ns)
chk('(E) dim_R Lie Stab(f3) = 2, diagonal phases only', len(ns)==2 and diag_only)
# (F) all equivariant cubic generators, finite
def c_AB(f):
    Fc=to_chiral(six(f)); return [pmul(Fc[w],pconj(Fc[w],SW4),6).get(U3V3,ZERO) for w in (0,1)]
def conj_by(Phi,f):
    idp=[X(0),X(1)]; phi=[padd(idp[i],Phi[i]) for i in range(2)]; phii=[padd(idp[i],pscale(Phi[i],m1)) for i in range(2)]
    for _ in range(3):
        c=comp4(Phi,phii); phii=[padd(idp[i],pscale(c[i],m1)) for i in range(2)]
    return comp4(phi,comp4(f,phii))
fim=onC(dyad_model(iu*mu)); cA0,cB0=c_AB(fim)
chk('(S3) c_B = conj(c_A) for f_{i mu}', (cB0-cA0.conj()).iszero())
allok=True
for kind,P in basis:
    if kind!='3': continue
    for s in (ONE,k(3)):
        a_,b_=c_AB(conj_by([pscale(P[0],s),pscale(P[1],s)],fim)); allok&=(a_-cA0).iszero() and (b_-cB0).iszero()
chk('(F) 24 real equivariant cubic generators x 2 scales: c_A, c_B unchanged', allok)
import random; random.seed(5)
Phi=[{mm:k(random.randint(-5,5),random.randint(-3,3),random.randint(-5,5),random.randint(-3,3)) for mm in mons3} for _ in range(2)]
a_,b_=c_AB(conj_by(Phi,fim)); chk('(F) random large non-S3 finite cubic conjugacy: unchanged', (a_-cA0).iszero() and (b_-cB0).iszero())
# (G) torus and swap in chiral coordinates
def lin_chiral(f,Bc):  # f' = B f B^{-1}, B given in chiral coords as function on (U,V) maps
    fc=to_chiral(f); return from_chiral(Bc(fc))
def torus(s1,s2):
    i1,i2=s1.conj(),s2.conj()  # unit moduli: inverse = conj
    def Bc(fc):
        sub=[pscale(X(0),i1),pscale(X(1),i2),pscale(X(2),i1.conj()),pscale(X(3),i2.conj())]
        g=[compose(fc[j],sub,D,4) for j in range(2)]
        return [pscale(g[0],s1),pscale(g[1],s2)]
    return Bc
def swapc(fc):
    sub=[X(1),X(0),X(3),X(2)]; g=[compose(fc[j],sub,D,4) for j in range(2)]; return [g[1],g[0]]
for (s1,s2,ph,lbl) in ((lam,ONE,k(-1),'diag(lam,1): c -> -c'),(ONE,lam,k(-1),'diag(1,lam): c -> -c'),(lam*lam,ONE,ONE,'diag(lam^2,1): c -> c')):
    a_,_=c_AB(lin_chiral(fim,torus(s1,s2))); chk('(G) '+lbl, (a_-cA0*ph).iszero())
a_,b_=c_AB(lin_chiral(fim,swapc)); chk('(G) swap: c_A -> conj(c_B) = c_A', (a_-cB0.conj()).iszero() and (a_-cA0).iszero())
print('|c|^2 invariant; c(i mu) =',kf(cA0))
print('ALL PASS' if OK else 'SOME FAIL'); sys.exit(0 if OK else 1)
