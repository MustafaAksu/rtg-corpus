# OFN_PSI_REFLECTION_AUDIT_v0_1 (OFN co-owner SESSION, 19 Oct 2026). Independent audit of the Z2-reflected pair: exact left kernel of L3 over Q(sqrt3), torus phases (w,z), Groebner. Expect controls solvable, reflected pairs GB=[1].
# Independent OFN audit of the reflection question: is f_{k,b} formally conjugate (deg<=5) to f_{k,a} when m(b)=2m*-m(a)?
# Conjugacy phi = B o psi, B in Stab(f3) (torus x swap, see stab check), psi tangent to id, psi3 equivariant: exact
# condition (B^-1 f_b B)_5 - f_a,5 in Im L3 (real span). Unknown torus phases w=e^{i theta}, z=e^{-6 i beta} symbolic.
import os,sys
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'OFN_PSI_KAPPA_EXTENSION_v0_1.py')).read().split("ok=True\ndef check")[0]
exec(src)
import sympy as sp
from fractions import Fraction as Fr
S3=sp.sqrt(3)
def toS(c): return (sp.Rational(c.re.a.numerator,c.re.a.denominator)+sp.Rational(c.re.b.numerator,c.re.b.denominator)*S3
                    +sp.I*(sp.Rational(c.im.a.numerator,c.im.a.denominator)+sp.Rational(c.im.b.numerator,c.im.b.denominator)*S3))
inv=K(R(),R(0,Fr(-1,3)))
uu={(1,0,0,0):ONE}; vv={(0,1,0,0):ONE}
w2s=pscale(padd(uu,vv,-1),inv); w1s=padd(uu,pscale(w2s,lam),-1)
SUB=[w1s,w2s,pconj(w1s,SW4),pconj(w2s,SW4)]
def to_uv(F):  # 2-comp map in w-coords -> (U-comp, V-comp) polys in (u,v,U,V)
    Fu=compose(padd(F[0],pscale(F[1],lam)),SUB,9,4); Fv=compose(padd(F[0],pscale(F[1],lamb)),SUB,9,4)
    return [Fu,Fv]
def red_map(kap,a):
    f=onC(dyad_model(a)); E=extra(kap); return [padd(f[i],E[i]) for i in range(2)]
w,z=sp.symbols('w z')
def phase(comp,e,swap):
    i,j,k,l=e
    # after swap the components/variables exchange; handle by relabel before phasing
    th=(i-k-1) if comp==0 else (i-k)   # exponent of e^{i theta}: u-comp gets e^{-i alpha}, v-comp e^{-i beta}; alpha=beta+theta
    nb=(i-k+j-l-1)
    assert nb%6==0
    return w**th * z**(-(nb//6))
def deg5_uv(F):
    G=to_uv(F); return [{e:c for e,c in G[i].items() if sum(e)==5} for i in range(2)]
def keyset(vecs):
    ks=set()
    for v in vecs:
        for i in range(2): ks|={(i,e) for e in v[i]}
    return sorted(ks)
def kernel_left(cols_re):  # cols_re: list of columns (each list of R, length n); return basis of y with y.col=0 for all cols
    m=len(cols_re); n=len(cols_re[0])
    rows=[c[:] for c in cols_re]   # matrix m x n ; kernel of this matrix (as map R^n->R^m)
    piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if not rows[i][c].iszero()),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]; inv=rows[r][c].inv(); rows[r]=[x*inv for x in rows[r]]
        for i in range(m):
            if i!=r and not rows[i][c].iszero():
                f=rows[i][c]; rows[i]=[a-f*b for a,b in zip(rows[i],rows[r])]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    basisv=[]
    for fc in free:
        y=[R() for _ in range(n)]; y[fc]=R(1)
        for i,pc in enumerate(piv): y[pc]=-rows[i][fc]
        basisv.append(y)
    return basisv
def Rs(x): return sp.Rational(x.a.numerator,x.a.denominator)+sp.Rational(x.b.numerator,x.b.denominator)*S3
def run(kap,a,b,label,expect_solvable,fb_override=None):
    fa=red_map(kap,a); fb=red_map(kap,b) if fb_override is None else fb_override
    A5=deg5_uv(fa); B5=deg5_uv(fb)
    cols=[deg5_uv(L3_of(P)) for kind,P in basis if kind=='3']
    out={}
    for swap in (False,True):
        Bv=B5
        if swap:
            Bv=[{(e[1],e[0],e[3],e[2]):c for e,c in B5[1].items()},{(e[1],e[0],e[3],e[2]):c for e,c in B5[0].items()}]
        ks=keyset([A5,Bv]+cols); n=len(ks)
        cre=[[c[i].get(e,ZERO).re for (i,e) in ks]+[c[i].get(e,ZERO).im for (i,e) in ks] for c in cols]
        Y=kernel_left(cre)
        eqs=[]
        for y in Y:
            # eta_k = y_re_k + i y_im_k ; equation Re( sum conj(eta_k) d_k ) = 0
            accB={}; accA=ZERO
            for kidx,(i,e) in enumerate(ks):
                eta=K(y[kidx],y[n+kidx]); ce=eta.conj()
                bk=Bv[i].get(e,ZERO); ak=A5[i].get(e,ZERO)
                if not bk.iszero():
                    ph=phase(i,e,False)  # monomial w^p z^q (swap already applied to data)
                    accB[ph]=accB.get(ph,ZERO)+ce*bk
                accA=accA+ce*ak
            expr=sum(toS(v)*ph for ph,v in accB.items())-toS(accA)
            conjexpr=sum(toS(v.conj())*(1/ph) for ph,v in accB.items())-toS(accA.conj())
            e_=sp.expand(expr+conjexpr)
            if e_!=0: eqs.append(sp.expand(sp.numer(sp.together(e_))))
        if not eqs: out[swap]='solvable (no constraints)'; continue
        Gb=sp.groebner(eqs,w,z,order='lex',extension=[S3,sp.I])
        out[swap]='NOT solvable (GB=[1])' if list(Gb.exprs)==[1] else 'solvable: '+str([sp.factor(g,extension=[S3,sp.I]) for g in Gb.exprs])[:160]
    solv=any(not v.startswith('NOT') for v in out.values())
    ok=(solv==expect_solvable)
    print(('PASS ' if ok else 'FAIL ')+label, out, flush=True)
    return ok
mu=k(Fr(-1,2),0,0,Fr(-2,3)); iu=k(0,0,1,0)
def full4(F): return [F[0],F[1],pconj(F[0],SW4),pconj(F[1],SW4)]
def comp(F,G): g=full4(G); return [compose(F[i],g,5,4) for i in range(2)]
def Bmap(al,be):
    w1v={(1,0,0,0):ONE}; w2v={(0,1,0,0):ONE}
    u=padd(w1v,pscale(w2v,lam)); v=padd(w1v,pscale(w2v,lamb))
    u2=pscale(u,al); v2=pscale(v,be)
    nw2=pscale(padd(u2,v2,-1),inv); nw1=padd(u2,pscale(nw2,lam),-1)
    return [nw1,nw2]
ok=True
for kap in (Fr(1),Fr(1,2),Fr(3)):
    t=(1-kap)/kap
    mstar=R(0,Fr(17,648))+R(0,t/9)
    sref=K(mstar*R(Fr(24,19)))
    b=iu*mu*sref
    ok&=run(kap,ZERO,ZERO,f'kappa={kap}: control identical pair',True)
    fa=red_map(kap,ZERO); fc=comp(Bmap(lamb,ONE),comp(fa,Bmap(lam,ONE)))
    ok&=run(kap,ZERO,ZERO,f'kappa={kap}: control torus-conjugated pair diag(lam,1)',True,fb_override=fc)
    ok&=run(kap,ZERO,b,f'kappa={kap}: reflected pair m(b)=2m*-m(a)',False)
    ok&=run(kap,iu*mu*K(R(Fr(1,7))),b+iu*mu*K(R(Fr(-1,7))),f'kappa={kap}: reflected pair, a off zero',False)
print('ALL PASS' if ok else 'SOME FAIL'); sys.exit(0 if ok else 1)
