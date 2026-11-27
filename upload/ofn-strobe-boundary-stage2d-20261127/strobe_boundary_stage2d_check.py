#!/usr/bin/env python3
"""Stage 2D SESSION. Exact symbolic and finite-jet controls, not owner replay."""
from math import factorial
import sympy as sp
from sympy import QQ


def need(ok, label):
    if not ok:
        raise AssertionError(label)


def symbolic_fixed_action():
    x,y,k=sp.symbols('x y k')
    a,b,c,d,e,f=sp.symbols('a b c d e f')
    R=sp.Matrix([[1,-1],[k,1-k]])
    u=sp.Matrix([x,y]); ru=R*u
    H=sp.Matrix([a*x*x+b*x*y+c*y*y,d*x*x+e*x*y+f*y*y])
    Hr=H.subs(dict(zip(u,ru)),simultaneous=True)
    eq=Hr-R*H-sp.Matrix([0,k*x*x])
    coeff=[sp.Poly(z,x,y).coeff_monomial(m) for z in eq for m in (x*x,x*y,y*y)]
    mat,rhs=sp.linear_eq_to_matrix(coeff,(a,b,c,d,e,f))
    determinant=sp.factor(mat.det())
    need(determinant!=0,'quadratic homological matrix')
    sol=sp.solve(coeff,(a,b,c,d,e,f)); H=H.subs(sol).applyfunc(sp.factor)
    need(all(sp.cancel(z)==0 for z in eq.subs(sol)),'quadratic equation')
    residual=sp.factor(k*sp.diff(H[0],y).subs(dict(zip(u,ru)),simultaneous=True))
    need(sp.cancel(residual+2*(k-2)*y/(k-3))==0,'fixed-action residual')
    print('FIXED_ACTION_SYMBOLIC_PASS; det =',determinant,'; residual/(2 eps rho^q) =',residual,flush=True)


def arithmetic():
    count=0; cases=0
    for p in range(12,257,4):
        n=p//2; h=n&-n; m=n//h
        roots=[j for j in range(n) if (2*h*j-h)%n==0]
        need(len(roots)==h,'root count')
        for k in range(1,m+1,2):
            if m%k: continue
            ell=h*k
            eroot=[j for j in range(n) if (2*j-ell)%n==0]
            need(eroot==sorted([ell//2,(ell//2+n//2)%n]),'half return root count')
            for j in roots:
                need((ell*j-ell//2)%n==n//2,'complement twist')
                cases+=1
        count+=1
    print(f'ROOT_AND_TWIST_ARITHMETIC_PASS {count}/{count} horizons; {cases} root/orbit-length pairs',flush=True)


class Jets:
    def __init__(self,K,N):
        self.K=K;self.N=N; self.zero=K.zero; self.one=K.one
        self.x={(1,0):self.one};self.y={(0,1):self.one};self.id=(self.x,self.y)
    def scale(self,p,a):
        a=self.K.convert(a)
        return {m:c*a for m,c in p.items() if c*a}
    def add(self,a,b):
        z=a.copy()
        for m,c in b.items():
            v=z.get(m,self.zero)+c
            if v:z[m]=v
            elif m in z:del z[m]
        return z
    def mul(self,a,b):
        z={}
        for (i,j),u in a.items():
            for (k,l),v in b.items():
                if i+j+k+l<=self.N:
                    m=(i+k,j+l);z[m]=z.get(m,self.zero)+u*v
        return {m:c for m,c in z.items() if c}
    def comp(self,F,G):
        n=self.N; px=[{(0,0):self.one},G[0]];py=[{(0,0):self.one},G[1]]
        for k in range(2,n+1):
            px.append(self.mul(px[-1],G[0]));py.append(self.mul(py[-1],G[1]))
        used=set(F[0])|set(F[1]);mon={m:self.mul(px[m[0]],py[m[1]]) for m in used}
        result=[]
        for f in F:
            z={}
            for m,c in f.items():z=self.add(z,self.scale(mon[m],c))
            result.append(z)
        return tuple(result)
    def submap(self,F,G):
        return tuple(self.add(f,self.scale(g,-1)) for f,g in zip(F,G))
    def power(self,F,k):
        G=self.id
        while k:
            if k&1:G=self.comp(F,G)
            k//=2
            if k:F=self.comp(F,F)
        return G
    def fractional(self,P,t):
        t=sp.Rational(t);z=self.id;d=self.id;binom=sp.S.One
        for k in range(1,self.N+1):
            d=self.submap(self.comp(d,P),d)
            if not any(d):return z
            binom=binom*(t-k+1)/k
            z=tuple(self.add(a,self.scale(b,binom)) for a,b in zip(z,d))
        raise AssertionError('nonterminating nilpotent difference')
    def jet(self,F,k):return tuple({m:c for m,c in f.items() if sum(m)<=k} for f in F)
    def inverse_shear(self,F,k):
        # inverse of R=[[1,-1],[k,1-k]], determinant one
        def ri(G):
            return (self.add(self.scale(G[0],1-k),G[1]),self.add(self.scale(G[0],-k),G[1]))
        G=ri(self.id)
        for _ in range(2,self.N+1):G=self.submap(G,ri(self.submap(self.comp(F,G),self.id)))
        need(self.comp(F,G)==self.id and self.comp(G,F)==self.id,'inverse')
        return G


def full_jets(p):
    n=p//2; h=n&-n; m=n//h; q=n-1; N=q+1
    K=QQ.algebraic_field(2*sp.cos(2*sp.pi/p)); k=2-K.unit
    V=Jets(K,N); eps=K.convert(sp.Rational(1,7))
    def f(sign):
        G={(j,0):K.convert(sp.Rational(1,factorial(j))) for j in range(1,N+1)}
        G[q,0]+=sign*eps
        S={(0,j):K.convert(sp.Rational((-1)**((j-1)//2),factorial(j))) for j in range(1,N+1,2)}
        return V.add(V.x,V.scale(S,-1)), V.add(V.y,V.scale(V.add(G,V.scale(S,-1)),k))
    plus,minus=f(1),f(-1)
    A=V.comp(minus,plus); P=V.power(A,n)
    need(V.jet(P,2)==V.id,'owner cubic leading order')
    J=V.comp(A,V.fractional(P,sp.Rational(-1,n)))
    need(V.power(J,n)==V.id,'J finite order')
    kap=V.power(J,n//2)
    need(V.power(kap,2)==V.id,'involution')
    need(V.comp(A,kap)==V.comp(kap,A),'centralizer')
    need(V.jet(kap,1)==(V.scale(V.x,-1),V.scale(V.y,-1)),'negative derivative')
    km=V.comp(V.comp(plus,kap),V.inverse_shear(plus,k))
    need(V.power(km,2)==V.id,'negative parity involution')
    need(V.comp(km,plus)==V.comp(plus,kap) and V.comp(kap,minus)==V.comp(minus,km),'covariance')
    need(V.jet(km,q)==V.jet(kap,q) and km!=kap,'first parity-action difference')
    j=pow(2,-1,m) if m>1 else 0
    g=V.comp(V.power(J,j),V.fractional(P,sp.Rational(1,p)))
    need(V.comp(g,kap)==V.comp(kap,g),'target involution')
    need(V.power(g,2*h)==V.power(A,h),'root')
    for r in range(1,m+1,2):
        if m%r:continue
        ell=h*r;D=V.power(A,ell//2)
        need(V.power(g,ell)==V.comp(kap,D),'opposite-sign half return')
    print(f'P={p} ORDER={N} FULL_JETS_PASS; J order, involutions, covariance, first split at {q+1}, product twist',flush=True)


if __name__=='__main__':
    print('SymPy',sp.__version__,flush=True)
    symbolic_fixed_action();arithmetic();full_jets(12);full_jets(16)
    print('ALL_STAGE2D_CHECKS_PASS',flush=True)
