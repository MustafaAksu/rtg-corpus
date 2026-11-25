"""Fast exact (0,3) value of R^raw_{p,4}=lam^{-s} f_p^s - Id via cyclotomic symbol z (Phi_p(z)=0).
Polynomial-in-z arithmetic reduced mod Phi_p; avoids slow radical simplify.
Charge/projection identical to canonical rtg_p_certs engine. Calibrated p=8->0, p=12->-13+15sqrt3/2."""
import sys, sympy as sp

def q4_03_cyclo(p, D=4):
    q=4; s=p//q
    z = sp.symbols('z')
    Phi = sp.Poly(sp.cyclotomic_poly(p, z), z)
    def red(e):
        return sp.rem(sp.Poly(sp.expand(e), z), Phi).as_expr()
    def inv(elt):
        return red(sp.invert(red(elt), Phi.as_expr(), z))
    lam=z; lamb=red(z**(p-1))
    K = red(2 - z - z**(p-1))
    Kinv=inv(K)
    assert red(K*Kinv)==1
    gamma=red((lam-1)*Kinv); gammab=red((lamb-1)*Kinv)
    denom=red(gamma-gammab); denom_inv=inv(denom)
    assert red(denom*denom_inv)==1
    def cl(P):
        out={}
        for k,v in P.items():
            vv=red(v)
            if sp.expand(vv)!=0: out[k]=vv
        return out
    def add(*ps):
        out={}
        for P in ps:
            for k,v in P.items(): out[k]=out.get(k,sp.Integer(0))+v
        return cl(out)
    def scale(P,c):
        c=red(c); return cl({k:v*c for k,v in P.items()})
    def mul(P,Q,D):
        out={}
        for (a1,b1),c1 in P.items():
            for (a2,b2),c2 in Q.items():
                if a1+a2+b1+b2<=D:
                    kk=(a1+a2,b1+b2); out[kk]=out.get(kk,sp.Integer(0))+red(c1*c2)
        return cl(out)
    def powp(P,n,D):
        out={(0,0):sp.Integer(1)}
        for _ in range(n): out=mul(out,P,D)
        return out
    def subst(poly,P,Q,D):
        out={}
        ma=max((a for a,_ in poly),default=0); mb=max((b for _,b in poly),default=0)
        Pp={0:{(0,0):sp.Integer(1)}}; Qp={0:{(0,0):sp.Integer(1)}}
        for n in range(1,ma+1): Pp[n]=mul(Pp[n-1],P,D)
        for n in range(1,mb+1): Qp[n]=mul(Qp[n-1],Q,D)
        for (a,b),c in poly.items():
            out=add(out, scale(mul(Pp[a],Qp[b],D),c))
        return out
    Pm={(1,0):sp.Integer(1)}; Qm={(0,1):sp.Integer(1)}
    eta=scale(add(Pm,scale(Qm,sp.Integer(-1))),denom_inv)
    rho=scale(add(scale(Qm,gamma),scale(Pm,-gammab)),denom_inv)
    s_poly={}; e_poly={}
    for n in range(1,D+1,2):
        s_poly=add(s_poly, scale(powp(eta,n,D),(sp.Integer(-1)**((n-1)//2))/sp.factorial(n)))
    for n in range(1,D+1):
        e_poly=add(e_poly, scale(powp(rho,n,D),sp.Integer(1)/sp.factorial(n)))
    rho1=add(rho,scale(s_poly,sp.Integer(-1)))
    eta1=add(eta,scale(e_poly,K),scale(s_poly,-K))
    W1=add(rho1,scale(eta1,gamma)); Wb1=add(rho1,scale(eta1,gammab))
    f1=(cl(W1),cl(Wb1))
    G=({(1,0):sp.Integer(1)},{(0,1):sp.Integer(1)})
    for _ in range(s):
        G=(subst(f1[0],G[0],G[1],D), subst(f1[1],G[0],G[1],D))
    lam_inv_s = red(z**(((-s)%p)))
    R=scale(G[0], lam_inv_s)
    R[(1,0)]=red(R.get((1,0),sp.Integer(0))-1)
    R=cl({k:v for k,v in R.items() if sum(k)>=2})
    def charge(a,b): return (a-b-1)%p
    K_extra=set(range(q,p,q))
    J={k:v for k,v in R.items() if sum(k)>=2 and charge(k[0],k[1]) in K_extra}
    val = J.get((0,3), sp.Integer(0))
    return red(val), z, Phi

if __name__=="__main__":
    import time
    p=int(sys.argv[1]); t=time.time()
    val,z,Phi = q4_03_cyclo(p)
    num=complex(sp.N(val.subs(z, sp.exp(2*sp.I*sp.pi/p)),40))
    print(f"p={p}  time={round(time.time()-t,1)}s")
    print(f"  value-in-z (mod Phi_{p}): {val}")
    print(f"  numeric: {num}")
    print(f"  |value|: {abs(num)}")
    with open(f"valz_p{p}.txt","w") as fh: fh.write(sp.srepr(val))
