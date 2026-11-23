"""
OPEN-GEN-II-9 sub-step 4: scalar-M susceptibility in both source pairings.
  chi_E(tau) = H0^T L^{-1} H0
  chi_B(tau) = H0^T B L^{-1} H0
L = (tau-g)I - DeltaM,  DeltaM = m[[mu2,-mu1],[-mu1,-mu2]],  kappa = m|w|.
Spectral form: L^{-1} = Pi_+/(tau-g-kappa) + Pi_-/(tau-g+kappa).
Extract soft-pole (tau-g-kappa) residues R^{(E)}_+ , R^{(B)}_+ and test
generic nonvanishing at H0 = J_Q s_*.
"""
import sympy as sp
from sympy import sqrt, simplify, factor, Matrix, symbols, Rational as R, cancel

mu1, mu2, s1, s2, tau, g, m = symbols('mu1 mu2 s1 s2 tau g m', real=True)
h1, h2 = symbols('h1 h2', real=True)

B  = Matrix([[1,-R(1,2)],[-R(1,2),1]])
kw = sqrt(mu1**2+mu2**2)            # |w|
kappa = m*kw
DeltaM = m*Matrix([[mu2,-mu1],[-mu1,-mu2]])
I2 = Matrix.eye(2)
L  = (tau-g)*I2 - DeltaM

# Euclidean spectral projectors
Pi_p = (I2 + DeltaM/kappa)/2     # onto +kappa eigenspace (soft branch tau-g-kappa)
Pi_m = (I2 - DeltaM/kappa)/2

# sanity: L^{-1} reconstruction
Linv = sp.simplify(Pi_p/(tau-g-kappa) + Pi_m/(tau-g+kappa))
assert sp.simplify(Linv*L - I2) == Matrix([[0,0],[0,0]]), "spectral L^{-1} failed"
print("spectral L^{-1} verified against L.")

H0 = Matrix([h1,h2])

# ---- chi_E ----
chiE = sp.simplify((H0.T*Linv*H0)[0])
# soft residue = lim (tau-g-kappa)*chiE  = H0^T Pi_p H0
RE_p = sp.simplify((H0.T*Pi_p*H0)[0])
RE_m = sp.simplify((H0.T*Pi_m*H0)[0])

# ---- chi_B ----
chiB = sp.simplify((H0.T*B*Linv*H0)[0])
RB_p = sp.simplify((H0.T*B*Pi_p*H0)[0])
RB_m = sp.simplify((H0.T*B*Pi_m*H0)[0])

print("\n=== Euclidean soft residue R^{(E)}_+ = H0^T Pi_+ H0 ===")
sp.pprint(factor(RE_p))
print("\n=== B-pairing soft residue R^{(B)}_+ = H0^T B Pi_+ H0 ===")
sp.pprint(factor(RB_p))

# ---- substitute physical source H0 = J_Q s_* (corrected J_Q) ----
JQ = Matrix([[1,-2],[2,-1]])/sqrt(3)
H0phys = JQ*Matrix([s1,s2])
sub = {h1:H0phys[0], h2:H0phys[1]}

REp_phys = factor(simplify(RE_p.subs(sub)))
RBp_phys = factor(simplify(RB_p.subs(sub)))
print("\n================ physical direction H0 = J_Q s_* ================")
print("\nR^{(E)}_+(J_Q s_*):"); sp.pprint(REp_phys)
print("\nR^{(B)}_+(J_Q s_*):"); sp.pprint(RBp_phys)

# numerator factors that can vanish
numE = sp.numer(sp.together(REp_phys))
numB = sp.numer(sp.together(RBp_phys))
print("\nEuclidean soft-residue vanishing locus (numerator = 0):")
sp.pprint(factor(numE))
print("\nB-pairing soft-residue vanishing locus (numerator = 0):")
sp.pprint(factor(numB))

# Are the two vanishing loci the same line in (s1,s2)? Compare linear forms.
def linform(expr):
    e = sp.expand(expr)
    return e.coeff(s1), e.coeff(s2)
# pull the linear factor out (residues are squares of a linear form, possibly /const)
def linear_factor(num):
    f = factor(num)
    # collect the (… s1 + … s2) factor
    polys = sp.Poly(sp.expand(num), s1, s2)
    return polys
print("\n--- proportionality of the two vanishing lines ---")
# extract linear form whose square is the numerator
sqrtE = sp.sqrt(factor(numE))
sqrtB = sp.sqrt(factor(numB))
try:
    LE = sp.nsimplify(sqrtE)
except Exception:
    LE = sqrtE
# Just compare via a generic numeric w to see if loci differ
import random
test = {mu1: R(2,1), mu2: R(1,1), m: R(1,1), g: R(0), tau: R(5,1)}
formE = sp.expand((H0phys.T*Pi_p*H0phys)[0].subs(test))
formB = sp.expand((H0phys.T*B*Pi_p*H0phys)[0].subs(test))
# vanishing lines:
print("\nAt (mu1,mu2)=(2,1): Euclidean soft-residue as quadratic in (s1,s2):")
sp.pprint(factor(formE))
print("\nAt (mu1,mu2)=(2,1): B-pairing soft-residue as quadratic in (s1,s2):")
sp.pprint(factor(formB))
