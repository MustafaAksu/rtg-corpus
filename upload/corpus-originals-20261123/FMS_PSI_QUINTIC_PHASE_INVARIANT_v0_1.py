"""FMS_PSI_QUINTIC_PHASE_INVARIANT_v0_1 (SESSION, 19 Oct 2026).
Explicit invariant for the quintic psi-modulus of the transported kappa-family (reduced map on the formal centre manifold).
c(kappa,a) := coefficient of u^3 vbar^3 in the degree-6 part of |u|^2 o F6 - |u|^2, F6 = f^6, u = w1 + lam w2, v = w1 + lamb w2.
Checks: (A) S3 class has 8 first-order quintic moduli; chart line is one direction.
(B) c vanishes on V cap Im A (all first-order gauge directions).  (C) c unchanged under finite random S3 cubic conjugacies.
(D) c(kappa,a) = -1/486 + 7t/648 + i[17 sqrt3/2916 + 2 sqrt3 t/81 - (2/9) Im(a conj(mu))], t=(1-kappa)/kappa, exactly, finite a.
Requires FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py and FMS_PSI_QUINTIC_KAPPA_ALL_v0_1.py in the same directory.
--- derived from the cokernel-count preamble below ---
kappa=1 reduced map f_a. Explicit cokernel functional I for the first-order quintic conjugacy problem.
(1) V = S3-equivariant, lambda-equivariant quintic perturbations (u-component chiral monomials; v-component by S3).
(2) dim V / (V cap Im A) = number of first-order quintic moduli in the S3 class.
(3) I = the unique (up to scale) functional on V vanishing on V cap Im A, printed on chiral monomials.
(4) I(delta5(a)) as a real-linear function of a: must vanish on R*mu.
Requires FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py in the same directory."""
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

assert dimV-dimI==8
E1=extra_t()
OK=True
def chk(lbl,b):
    global OK; OK&=b; print(('PASS ' if b else 'FAIL ')+lbl)
U=K(R(),R(1))
# (B) first-order gauge directions
for c in inter:
    P=comb(c); Pc=to_chiral([degpart(P[0],5),degpart(P[1],5)])
    du=pscale(Pc[0],lamb*k(6)); t_=pmul({(0,0,1,0):ONE},du,6); dA=padd(t_,pconj(t_,SW4))
    chk('(B) gauge direction leaves u^3 vbar^3 coefficient fixed', U3V3 not in dA)
import random; random.seed(11)
def Imamub(a): return (a*mu.conj()).im
for t in (Fr(0),Fr(1),Fr(-2,3),Fr(-1,2),Fr(3,7)):
    tt=k(t)
    def fk(a): fa=onC(dyad_model(a)); return [padd(fa[i],pscale(E1[i],tt)) for i in range(2)]
    def pred(a): return K(R(Fr(-1,486))+R(Fr(7,648))*R(t), R(0,Fr(17,2916))+R(0,Fr(2,81))*R(t)+R(Fr(-2,9))*Imamub(a))
    for a in (ZERO,mu,iu*mu,k(0,0,3,0),k(2,0,5,0),k(0,Fr(4),-11,0)):
        chk(f'(D) t={t} a={kf(a)} closed form', (inv(fk(a))[0]-pred(a)).iszero())
    Phi=S3avg([{m:k(random.randint(-3,3),random.randint(-2,2),random.randint(-3,3),random.randint(-1,1)) for m in mons3} for _ in range(2)])
    idp=[X(0),X(1)]; phi=[padd(idp[i],Phi[i]) for i in range(2)]; phii=[padd(idp[i],pscale(Phi[i],m1)) for i in range(2)]
    for _ in range(3):
        c=comp4(Phi,phii); phii=[padd(idp[i],pscale(c[i],m1)) for i in range(2)]
    fp=comp4(phi,comp4(fk(iu*mu),phii))
    chk(f'(C) t={t} finite S3 cubic conjugacy preserves c', (inv(fp)[0]-inv(fk(iu*mu))[0]).iszero())
print('ALL PASS' if OK else 'SOME FAIL'); sys.exit(0 if OK else 1)
