exec(open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)),"OFN_PSI_INVARIANT_C_CHECK_v0_1.py")).read().split("\nok=True\nfor kap")[0])
from fractions import Fraction as Fr
def c_of_map(F):
    F6=six(F)
    uF=padd(F6[0],pscale(F6[1],lam_)); UF=pconj(uF,SW4)
    u0={(1,0,0,0):ONE,(0,1,0,0):lam_}; U0=pconj(u0,SW4)
    d=padd(pmul(uF,UF,D6),pmul(u0,U0,D6),-1); d6={e:c for e,c in d.items() if sum(e)==6}
    inv=K(R(),R(0,Fr(-1,3))); uu={(1,0,0,0):ONE}; vv={(0,1,0,0):ONE}
    w2=pscale(padd(uu,vv,-1),inv); w1=padd(uu,pscale(w2,lam_),-1)
    P=compose(d6,[w1,w2,pconj(w1,SW4),pconj(w2,SW4)],6,4)
    return P.get((3,0,0,3),ZERO)
ok=True
for kap in (Fr(1,2),Fr(3)):
    F=red_map(kap,ZERO); c0=c_of_map(F)
    f3k=[degpart(F[i],3) for i in range(2)]
    # L3 uses global f3 (kappa-independent cubic) -- verify equals reduced cubic
    assert all(not padd(f3k[i],f3[i],-1) for i in range(2))
    bad=0
    for kind,P in basis:
        if kind!='3': continue
        d=L3_of(P); Fp=[padd(F[i],d[i]) for i in range(2)]
        if not (c_of_map(Fp)-c0).iszero(): bad+=1
    print('kappa',kap,': cubic generators moving c:',bad,'of 24'); ok&= bad==0
    # torus element diag(lam,1) in (u,v): B w = ?  u=w1+lam w2, v=w1+lamb w2 ; build B in w coords
    # w as function of (u,v): w2=(u-v)/(lam-lamb), w1=u-lam w2 ; apply u->lam u
    inv=K(R(),R(0,Fr(-1,3)))
    def Bmap(al,be):
        # returns linear map in w-coords as 2-comp polys: w -> w(al*u(w), be*v(w))
        w1v={(1,0,0,0):ONE}; w2v={(0,1,0,0):ONE}
        u=padd(w1v,pscale(w2v,lam_)); v=padd(w1v,pscale(w2v,lamb_))
        u2=pscale(u,al); v2=pscale(v,be)
        nw2=pscale(padd(u2,v2,-1),inv); nw1=padd(u2,pscale(nw2,lam_),-1)
        return [nw1,nw2]
    B=Bmap(lam_,ONE); Bi=Bmap(lamb_,ONE)
    Fc=comp(Bi,comp(F,B))
    cB=c_of_map(Fc)
    print('  diag(lam,1): c_B == -c ?',(cB+c0).iszero(),'; |c| invariant:', (cB*cB.conj()-c0*c0.conj()).iszero())
    ok&=(cB+c0).iszero()
print('PASS' if ok else 'FAIL')
