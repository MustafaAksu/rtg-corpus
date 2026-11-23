"""
HINDEX independent verification (v2.7.7).
[V1] Covector reading: ||H||_B^2 = lam_max(B^{-1} H^T B^{-1} H) from S=Hx covector.
[V2] Checksum H=sigma*B -> double root sigma^2 (norm |sigma|, no hidden factor).
[V3] FAIL alternative (vector reading B^{-1}H^T B H): at H=sigma*B gives
     {9 sigma^2/4, sigma^2/4} -- concrete hidden normalization fork.
[V4] Unification: on the 9C admissible family, HINDEX singular spectrum equals
     squared B-native eigenvalue spectrum => ||H||_B and ||M||_B are ONE convention.
"""
import sympy as sp
from sympy import Matrix, symbols, Rational as R, simplify, sqrt, eye

B = Matrix([[1,-R(1,2)],[-R(1,2),1]]); Binv = B.inv()
sigma,g,D,m,mu2 = symbols('sigma g D m mu2', real=True)

# V2 checksum
ok2 = simplify(Binv*(sigma*B).T*Binv*(sigma*B) - sigma**2*eye(2)) == sp.zeros(2,2)
# V3 fail alternative
ev3 = sorted([simplify(k/sigma**2) for k in (Binv*(sigma*B).T*B*(sigma*B)).eigenvals()], key=str)
# V4 unification on admissible family
s3=Matrix([[1,0],[0,-1]]); s1=Matrix([[0,1],[1,0]])
M = g*eye(2) - m*mu2*s3 + D*s1
specBM = [simplify(e) for e in (Binv*M).eigenvals()]
specS  = [simplify(e) for e in (Binv*M.T*Binv*M).eigenvals()]
sq = [simplify(e**2) for e in specBM]
ok4 = all(any(simplify(a-b)==0 for b in sq) for a in specS)
print("V2 double-root sigma^2:", ok2)
print("V3 vector-reading eigenvalues / sigma^2:", ev3, " (expected [1/4, 9/4])")
print("V4 norm-convention unification:", ok4)
assert ok2 and ok4 and set(map(str,ev3))=={'1/4','9/4'}
print("ALL HINDEX VERIFICATION CHECKS PASS")
