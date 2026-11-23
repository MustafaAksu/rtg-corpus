"""
mspin2_admissible_family.py — OPEN-GEN-II-9C admissible-family certificate (v2.7.6)
[RID: GEN-OPEN-MSPIN2-ANISO] + norm verification for [RID: GEN-DEF-NORM-BNATIVE]

Second independent reconstruction of the 9C B-self-adjointness criterion from
documented Sec 6.8 inputs ONLY (no reuse of prior 9-series artifacts), plus:
 - complete admissible two-parameter family M_spin2(g, D)
 - commutant collapse K = gI + (D - m Re w) P, shared B eigenframe
 - mu1 = Re w cross-check via the tau*B exclusion determinant
 - B-native vs Euclidean norm verification (CHECK-GEN-II-7B-NORM resolution)
All checks must print True/PASS.
"""
import sympy as sp
from sympy import Matrix, symbols, Rational as R, simplify, sqrt, oo

m, rew, imw, tau, lam, g, D = symbols('m rew imw tau lam g D', real=True)
B   = Matrix([[1, -R(1,2)],[-R(1,2), 1]])
DMf = m*Matrix([[imw, -rew],[-rew, -imw]])
P   = Matrix([[0,1],[1,0]])

def check(name, ok): print(f"[{'PASS' if ok else 'FAIL'}] {name}"); assert ok

# 0. B identification cross-checks (documented determinant facts)
check("det(DMf + tau*B) = (3/4)tau^2 - m*Re(w)*tau - kappa^2  (mu1 = Re w)",
      simplify(sp.det(DMf + tau*B) - (R(3,4)*tau**2 - m*rew*tau - m**2*(rew**2+imw**2))) == 0)
check("det(DMf + tau*I) = tau^2 - kappa^2",
      simplify(sp.det(DMf + tau*sp.eye(2)) - (tau**2 - m**2*(rew**2+imw**2))) == 0)

# 1. Criterion from scratch: K^T B = B K for generic symmetric M_spin2
a,b,c = symbols('a b c', real=True)
Msp = Matrix([[a,b],[b,c]]); K = DMf + Msp
comm = sp.expand(K.T*B - B*K)
check("Commutator has single scalar condition, off-diagonal b absent",
      not (comm[0,1].has(b) or comm[1,0].has(b)))
check("B-self-adjoint iff a - c = -2 m Im w",
      simplify(comm[0,1].subs(a, c - 2*m*imw)) == 0 and simplify(comm[0,1].subs(a, c)) != 0)

# 2. Admissible family and commutant collapse
Madm = Matrix([[g - m*imw, D],[D, g + m*imw]])
check("Admissible family satisfies the split", simplify((Madm[0,0]-Madm[1,1]) + 2*m*imw) == 0)
Kadm = sp.simplify(DMf + Madm)
check("K = gI + (D - m Re w) P (commutant collapse)",
      sp.simplify(Kadm - (g*sp.eye(2) + (D - m*rew)*P)) == sp.zeros(2,2))
v1, v2 = Matrix([1,1]), Matrix([1,-1])
check("K shares B eigenframe (1,1)", simplify((Kadm*v1)[0]-(Kadm*v1)[1]) == 0)
check("K shares B eigenframe (1,-1)", simplify((Kadm*v2)[0]+(Kadm*v2)[1]) == 0)
check("Soft mode at g = |D - m Re w| (eigenvalues g +/- (D - m Re w))",
      sorted([sp.simplify(e) for e in Kadm.eigenvals()], key=str) ==
      sorted([sp.simplify(g + (D - m*rew)), sp.simplify(g - (D - m*rew))], key=str))

# 3. Norms: B-native vs Euclidean (CHECK-GEN-II-7B-NORM)
char = sp.expand(sp.det(Madm - lam*B))
sols = sp.solve(sp.Eq(char, 0), lam)
lam_exact = [sp.simplify(s) for s in sols]
target = [ (2*D+4*g)/3 - R(2,3)*sqrt(4*D**2+4*D*g+g**2+3*m**2*imw**2),
           (2*D+4*g)/3 + R(2,3)*sqrt(4*D**2+4*D*g+g**2+3*m**2*imw**2) ]
check("Exact B-spectrum lambda_pm matches documented form",
      all(any(simplify(s-t)==0 for t in target) for s in lam_exact))
gp = symbols('gp', positive=True)
lims = sorted([sp.limit(s.subs(g,gp)/gp, gp, oo) for s in lam_exact])
check("Large-g B-spectrum limits {2/3, 2} -> ||M||_B -> 2g", lims == [R(2,3), 2])
ev_scalar = sp.solve(sp.Eq(sp.expand(sp.det(g*sp.eye(2) - lam*B)), 0), lam)
check("Scalar anchor ||gI||_B = 2g", sorted([simplify(s/g) for s in ev_scalar]) == [R(2,3), 2])
ev_endo = sp.solve(sp.Eq(sp.expand(sp.det(B.inv()*Madm - lam*sp.eye(2))), 0), lam)
subs0 = {g:1, m:1, imw:2, D:3}
check("B-eigenproblem == spectrum of B^{-1} M_spin2",
      sorted([sp.simplify(s.subs(subs0)) for s in sols]) ==
      sorted([sp.simplify(e.subs(subs0)) for e in ev_endo]))
ev_E = list(Madm.eigenvals())
check("Euclidean norm ||M||_E -> g (large g): eigenvalues g +/- sqrt(D^2+m^2 Im^2 w)",
      sorted([sp.simplify(e - g) for e in ev_E], key=str) ==
      sorted([sqrt(D**2+m**2*imw**2), -sqrt(D**2+m**2*imw**2)], key=str))

print("\nALL CHECKS PASS — 9C admissible family + B-native norm certificate complete.")
