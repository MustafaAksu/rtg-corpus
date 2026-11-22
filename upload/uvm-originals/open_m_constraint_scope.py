"""
OPEN M / OPEN-GEN-II-7B scoping: what do the CERTIFIED results already pin about
the UV blocks (H, M_spin2), and what genuinely needs new UV input?

This is NOT an attempt to derive the UV theory. It enumerates the exact
constraints the certified scalar-M frame + 9C + single-jet [HYP] impose, and
isolates the minimal undetermined parameter(s). Honest boundary-marking.

Known certified / documented structure:
 - B-metric, J_Q (B-isometry), Delta M_f = m[[Im w,-Re w],[-Re w,-Im w]], kappa=m|w|.
 - 9C [ALG]: K = Delta M_f + M_spin2 is B-self-adjoint iff
     (M_spin2)_11 - (M_spin2)_22 = -2 m Im w.
 - single-jet [ALG-conditional]: alpha_f = c_0 |w|, c_0 = ||H|| / ||M||_op.
 - 7B target: |alpha_f| >~ 0.012 (reduced-wrapper [HYP]).
 - H(x): zeroth-order Pi_par -> Pi_perp source block (nonzero = non-block-diag).
"""
import sympy as sp
from sympy import Matrix, symbols, sqrt, simplify, Rational as R, eye

mu1,mu2,m,g = symbols('mu1 mu2 m g', real=True)  # mu1=Re w, mu2=Im w
B = Matrix([[1,-R(1,2)],[-R(1,2),1]])
DMf = m*Matrix([[mu2,-mu1],[-mu1,-mu2]])

print("="*64)
print("CONSTRAINT 1 (9C): M_spin2 diagonal splitting fixed by B-self-adjointness")
print("="*64)
A,C,D = symbols('A C D', real=True)  # M_spin2 = [[A,D],[D,C]]
Msp = Matrix([[A,D],[D,C]])
# 9C requires A - C = -2 m mu2. So the TRACE-FREE diagonal part is FIXED.
# Only the trace (A+C) and off-diagonal D remain free.
tr = symbols('t', real=True)   # trace A+C
# A = (t - 2 m mu2)/2 ... wait: A - C = -2 m mu2, A + C = t => A=(t-2 m mu2)/2, C=(t+2 m mu2)/2
A_sol = (tr - 2*m*mu2)/2; C_sol = (tr + 2*m*mu2)/2
Msp_constrained = Matrix([[A_sol, D],[D, C_sol]])
print("M_spin2 (B-self-adjoint) =")
sp.pprint(Msp_constrained)
print("Free params after 9C: trace t = A+C, and off-diagonal D.  (diagonal split FIXED)")

print()
print("="*64)
print("CONSTRAINT 2: off-diagonal D fixed by spin-2 projection sector (documented)")
print("="*64)
print("""
The DSN states (9C entry) that the off-diagonal (M_spin2)_12 = D is fixed by the
spin-2 projection sector (§6.7), not by self-adjointness. So D is determined by
EXISTING structure, not free. That leaves only the TRACE t = A+C undetermined by
the self-adjointness + spin-2 constraints.
""")

print("="*64)
print("CONSTRAINT 3: trace t enters as a uniform shift g*I (scalar part)")
print("="*64)
print("""
The scalar part of M_spin2 is exactly the 'g' of the scalar-M ansatz
(M_spin2 = g I in scalar-M). In the full theory, g = t/2 is the isotropic
spin-2 mass. The eigenvalue structure 9A used was lambda_pm = (tau - g) -/+ kappa,
so g only SHIFTS the soft-pole location tau_soft = g + kappa, it does NOT change
the residue PSD-ness (9B) or the secular reconstruction (9B-tau), which are
g-covariant. So the soft-mode physics is INDEPENDENT of the undetermined trace g.
""")

print("="*64)
print("CONSTRAINT 4: alpha_f = c_0 |w|, c_0 = ||H||/||M||_op  -- the genuine unknown")
print("="*64)
print("""
After 9C (diagonal split fixed) and spin-2 (off-diagonal fixed), the operator
norm ||M||_op of the spin-2 block is determined UP TO the scalar trace g, which
shifts all eigenvalues uniformly. ||M||_op = max|eigenvalue of M_spin2|.
Compute eigenvalues of the B-self-adjoint M_spin2 with D fixed, g free:
""")
# eigenvalues of M_spin2 (B-self-adjoint => real B-spectrum). Use B-eigenproblem.
# For B-self-adjoint M, eigenvalues solve det(M - lam B)=0.
lam = symbols('lam', real=True)
Msp_g = Matrix([[g - m*mu2, D],[D, g + m*mu2]])  # t=2g
char = simplify((Msp_g - lam*B).det())
sols = sp.solve(sp.Eq(char,0), lam)
print("B-eigenvalues of M_spin2 (trace=2g, diag split -2m mu2, offdiag D):")
for s in sols: sp.pprint(simplify(s))
print("""
So ||M||_op depends on (g, D, m, mu2). D is fixed by spin-2 sector; m,mu2 are UV
data (w); g is the isotropic spin-2 mass. ||H|| is the norm of the zeroth-order
Pi_par->Pi_perp source block -- this is the ONE object NOT constrained by any
certified result. It is the irreducible OPEN M input.
""")

print("="*64)
print("SCOPING VERDICT")
print("="*64)
print("""
DETERMINED by certified frame:
  - M_spin2 trace-free diagonal part = -2 m Im w  (9C)
  - M_spin2 off-diagonal             = spin-2 sector (§6.7, documented)
  - soft-pole residue PSD, secular eq  (9A/9B/9B-tau) -- g-covariant
PINNED UP TO the isotropic spin-2 mass g:
  - ||M||_op  (eigenvalues shift uniformly with g)
GENUINELY OPEN (irreducible OPEN M input):
  - ||H||: norm of the zeroth-order non-block-diagonal source block H(x)
  - g    : isotropic spin-2 mass (sets soft-pole location tau_soft = g + kappa)
  => alpha_f = c_0|w| = (||H||/||M||_op)|w| cannot be computed without ||H|| and g.

CONCLUSION: 7B's |alpha_f| >~ 0.012 test is BLOCKED on exactly TWO scalars
(||H||, g), not on the full UV theory. Everything else is pinned. This is the
sharp, minimal statement of what OPEN M must supply.
""")
