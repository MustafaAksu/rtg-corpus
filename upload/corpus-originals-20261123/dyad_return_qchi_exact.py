# Exact arithmetic in Q(chi), chi^2=-3 (chi = i*sqrt3). Numbers are (a,b) meaning a + b*chi, a,b Fraction.
from fractions import Fraction as Fr
from collections import defaultdict
class Q:
    __slots__=('a','b')
    def __init__(s,a=0,b=0): s.a=Fr(a); s.b=Fr(b)
    def __add__(s,o): o=o if isinstance(o,Q) else Q(o); return Q(s.a+o.a,s.b+o.b)
    __radd__=__add__
    def __neg__(s): return Q(-s.a,-s.b)
    def __sub__(s,o): return s+(-(o if isinstance(o,Q) else Q(o)))
    def __rsub__(s,o): return (o if isinstance(o,Q) else Q(o))-s
    def __mul__(s,o):
        o=o if isinstance(o,Q) else Q(o)
        return Q(s.a*o.a-3*s.b*o.b, s.a*o.b+s.b*o.a)
    __rmul__=__mul__
    def conj(s): return Q(s.a,-s.b)
    def inv(s):
        n=s.a*s.a+3*s.b*s.b; return Q(s.a/n,-s.b/n)
    def __truediv__(s,o): o=o if isinstance(o,Q) else Q(o); return s*o.inv()
    def iszero(s): return s.a==0 and s.b==0
    def __eq__(s,o): o=o if isinstance(o,Q) else Q(o); return s.a==o.a and s.b==o.b
    def __repr__(s):
        if s.b==0: return f"{s.a}"
        return f"({s.a}) + ({s.b})*i√3"
    def sym(s):
        import sympy as sp
        return sp.Rational(s.a.numerator,s.a.denominator)+sp.Rational(s.b.numerator,s.b.denominator)*sp.I*sp.sqrt(3)

# Sparse polynomial in (z, zb): dict {(a,b): Q}
class P:
    def __init__(s,d=None,N=6): s.d={k:v for k,v in (d or {}).items() if not v.iszero()}; s.N=N
    def __add__(s,o):
        r=defaultdict(Q)
        for k,v in s.d.items(): r[k]=r[k]+v
        for k,v in o.d.items(): r[k]=r[k]+v
        return P(r,max(s.N,o.N))
    def __sub__(s,o): return s+o.scale(Q(-1))
    def scale(s,c): return P({k:v*c for k,v in s.d.items()},s.N)
    def __mul__(s,o):
        r=defaultdict(Q); N=min(s.N,o.N)
        for (a1,b1),v1 in s.d.items():
            for (a2,b2),v2 in o.d.items():
                if a1+a2+b1+b2<=N: r[(a1+a2,b1+b2)]=r[(a1+a2,b1+b2)]+v1*v2
        return P(r,N)
    def conj(s): return P({(b,a):v.conj() for (a,b),v in s.d.items()},s.N)
    def pw(s,n):
        r=P({(0,0):Q(1)},s.N)
        for _ in range(n): r=r*s
        return r
    def compose(s,g,gb):
        # s(z,zb) with z->g, zb->gb
        r=P({},s.N)
        gp={0:P({(0,0):Q(1)},s.N)}; gbp={0:P({(0,0):Q(1)},s.N)}
        for k in range(1,s.N+1): gp[k]=gp[k-1]*g; gbp[k]=gbp[k-1]*gb
        for (a,b),v in s.d.items():
            r=r+(gp[a]*gbp[b]).scale(v)
        return r
    def deg(s,n): return P({k:v for k,v in s.d.items() if sum(k)==n},s.N)
    def get(s,k): return s.d.get(k,Q(0))
