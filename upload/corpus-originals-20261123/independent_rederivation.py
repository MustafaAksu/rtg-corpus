"""
INDEPENDENT CLEAN-ROOM RE-DERIVATION of the scalar-M 9-series.
No import of source_pairing.py / index_placement_trace.py / tau_coupling_trace.py
/ secular_numerator_trace.py. Objects rebuilt from defining properties where
possible, and cross-checked against v2.7.2's stated claims at the end.

Claims under test (from v2.7.2):
 [C1] J_Q = (1/sqrt3)[[1,-2],[2,-1]] is a B-isometry (J^T B J = B), J^2 = -I,
      and a^T B J b = (sqrt3/2) omega_ab.
 [C2] Delta M_f is Euclidean-symmetric but NOT B-self-adjoint;
      (Delta M_f)^2 = kappa^2 I with kappa = m|w|.
 [C3] det(Delta M_f + tau I) = tau^2 - kappa^2 ; det(Delta M_f + tau B) != that.
 [C4] Full secular: with K = tau I - Delta M_f, Euclidean constraint d^T d=Delta3,
      Euclidean unit source S_f = sigma_f r_phi:
        Delta3 (tau^2-kappa^2)^2 = sigma_f^2 (tau^2 + 2 a tau + kappa^2),
      a = r_phi^T Delta M_f r_phi.
 [C5] Soft residue PSD: with S_f = B c_f (lowered), c_f = beta J_Q s_*,
      residue c_f^T B Pi_+ B c_f = |Pi_+ B c_f|^2 >= 0, where Pi_+ is the
      Euclidean-orthogonal projector onto the +kappa eigenspace of Delta M_f.
 [C6] 9C: K = Delta M_f + Mspin2 is B-self-adjoint iff
      (Mspin2)_11 - (Mspin2)_22 = -2 m Im w.
"""
import sympy as sp
from sympy import Matrix, symbols, sqrt, simplify, eye, factor, Rational as R

print("CLEAN-ROOM RE-DERIVATION — no reuse of prior artifacts\n")

# --- Rebuild B from its DEFINING property, not by copying ---------------------
# B is the K2/dyad Gram metric: the amplitude form on the 2D mode plane with
# unit diagonal and the RTG inner-product angle giving off-diagonal -1/2.
# Define it as the Gram matrix of two unit vectors at 120 degrees (cos120=-1/2):
b12 = sp.cos(sp.rad(120))
B = Matrix([[1, b12],[b12, 1]])
print("B (rebuilt from 120-deg Gram) =", B.tolist())

# --- Rebuild J_Q from a DEFINING property: the B-isometry that rotates by the
# RTG quarter-turn. Instead of copying, SOLVE for a 2x2 real J with J^T B J = B,
# J^2 = -I, and orientation +. Then compare to the claimed matrix. ------------
a,b,c,d = symbols('a b c d', real=True)
Jgen = Matrix([[a,b],[c,d]])
eqs = []
M = Jgen.T*B*Jgen - B
eqs += [M[0,0], M[0,1], M[1,1]]
J2 = Jgen*Jgen + eye(2)
eqs += [J2[0,0], J2[0,1], J2[1,0], J2[1,1]]
sol = sp.solve(eqs, [a,b,c,d], dict=True)
print("\nSolutions of {J^T B J = B, J^2 = -I}:")
for s in sol:
    Js = Jgen.subs(s)
    # orientation: det>0 and pick the one matching +omega convention
    print("  J =", Js.tolist(), " det =", simplify(Js.det()))

claimed_JQ = Matrix([[1,-2],[2,-1]])/sqrt(3)
match_JQ = any(simplify(Jgen.subs(s) - claimed_JQ)==Matrix([[0,0],[0,0]]) for s in sol)
print(f"\n[C1] claimed J_Q is among independent solutions: {match_JQ}")
# verify the omega identity independently
x1,x2,y1,y2 = symbols('x1 x2 y1 y2', real=True)
av=Matrix([x1,x2]); bv=Matrix([y1,y2])
omega = x1*y2 - x2*y1   # standard symplectic
lhs = simplify((av.T*B*claimed_JQ*bv)[0])
print(f"[C1] a^T B J_Q b - (sqrt3/2) omega_ab = {simplify(lhs - (sqrt(3)/2)*omega)}")
print(f"[C1] J_Q^2 + I = {simplify(claimed_JQ*claimed_JQ + eye(2))}")
