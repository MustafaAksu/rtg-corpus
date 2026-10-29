# Independent check of FMS closed form c(kappa,a): coefficient of u^3 vbar^3 in deg-6 part of A(F6)-A, A=|u|^2
src=open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'OFN_PSI_KAPPA_EXTENSION_v0_1.py')).read().split("ok=True\ndef check")[0]
exec(src)
from fractions import Fraction as Fr
import sys
D6=6
def red_map(kap,a):
    f=onC(dyad_model(a)); E=extra(kap)
    return [padd(f[i],E[i]) for i in range(2)]
def full4(F):  # components (w1,w2,W1,W2) images
    return [F[0],F[1],pconj(F[0],SW4),pconj(F[1],SW4)]
def comp(F,G,D=5):  # F∘G, both 2-comp maps in 4 vars, truncated deg D
    g=full4(G)
    return [compose(F[i],g,D,4) for i in range(2)]
def six(F):
    G=F
    for _ in range(5): G=comp(F,G)
    return G
lam_=lam; lamb_=lamb
s3=R(0,1)
def coeff_c(kap,a):
    F6=six(red_map(kap,a))
    u_of=lambda P: padd(P[0],pscale(P[1],lam_))
    uF=u_of(F6); UF=pconj(uF,SW4)
    Av=pmul(uF,UF,D6)
    u0={(1,0,0,0):ONE, (0,1,0,0):lam_}; U0=pconj(u0,SW4)
    d=padd(Av,pmul(u0,U0,D6),-1)
    d6={e:c for e,c in d.items() if sum(e)==6}
    # substitute w in terms of (u,v): w2=(u-v)/(lam-lamb), w1=u-lam*w2 ; vars (u,v,U,V)
    den=(lam_-lamb_)   # = i*sqrt3
    # inverse of den: den = K(0, sqrt3) -> 1/den = -i/sqrt3 = K(0,-1/sqrt3) ; 1/sqrt3 = sqrt3/3
    inv=K(R(),R(0,Fr(-1,3)))
    assert (den*inv - ONE).iszero()
    uu={(1,0,0,0):ONE}; vv={(0,1,0,0):ONE}
    w2=pscale(padd(uu,vv,-1),inv); w1=padd(uu,pscale(w2,lam_),-1)
    W1=pconj(w1,SW4); W2=pconj(w2,SW4)
    P=compose(d6,[w1,w2,W1,W2],6,4)
    return P.get((3,0,0,3),ZERO)
mu=k(Fr(-1,2),0,0,Fr(-2,3)); iu=k(0,0,1,0)
def fms(kap,a):
    t=(1-kap)/kap
    m=(a*mu.conj()).im   # Im(a mubar) as R
    re=R(Fr(-1,486)+Fr(7,648)*t)
    im=R(0,Fr(17,2916))+R(0,Fr(2,81)*t)-m*R(Fr(2,9))
    return K(re,im)
ok=True
for kap in (Fr(1),Fr(1,2),Fr(3)):
    for a in (ZERO, iu*mu, k(2,0,5,0), k(0,0,3,0)):
        c=coeff_c(kap,a); f=fms(kap,a)
        good=(c-f).iszero(); ok&=good
        print('kappa',kap,'a',(a.re,a.im),'c=',(c.re,c.im),'match' if good else 'MISMATCH', (f.re,f.im))
print('ALL MATCH' if ok else 'SOME MISMATCH'); sys.exit(0 if ok else 1)
