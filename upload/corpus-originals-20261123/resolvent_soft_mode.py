"""
OPEN-GEN-II-9 sub-steps 1-3: scalar-M eigendecomposition, soft-mode ID,
projection-nontriviality residue. Exact SymPy.

Critical check beyond the two notes: BOTH notes compute the residue using the
EUCLIDEAN inner product (v.dot(v), H0^T Pi H0 with Pi = v v^T / v^T v).
But the entire Genesis algebra runs in the B-metric (B = [[1,-1/2],[-1/2,1]]).
DeltaM_f is symmetric in the EUCLIDEAN sense, so its eigenvectors are Euclidean-
orthogonal -- but the source projection and the soft-mode residue that actually
governs the susceptibility must use whichever metric the constrained-lift
quadratic form Q_4(d_perp)=Delta_3 is written in. We compute BOTH and compare,
so the verdict is not silently metric-dependent.
"""
import sympy as sp
from sympy import sqrt, simplify, Matrix, symbols, Rational as R

mu1, mu2 = symbols('mu1 mu2', real=True)
m, tau, g = symbols('m tau g', real=True, positive=True)
h1, h2 = symbols('h1 h2', real=True)

B = Matrix([[1, -R(1,2)], [-R(1,2), 1]])

# Delta M_f in canonical face gauge
DeltaM = m*Matrix([[mu2, -mu1], [-mu1, -mu2]])
kappa = m*sqrt(mu1**2 + mu2**2)          # |eig(DeltaM)| = m|w|
kw = sqrt(mu1**2 + mu2**2)

print("="*64)
print("STEP 1: eigenstructure of Delta M_f")
print("="*64)
ev = DeltaM.eigenvects()
for val, mult, vecs in ev:
    print(f"  eigenvalue {sp.simplify(val)}  ->  {vecs[0].T}")

# soft branch = tau-g-kappa -> 0 ; soft eigenvector is the +kappa eigvec of DeltaM
v_plus  = Matrix([mu1, mu2 - kw])        # DeltaM v = +kappa v
v_minus = Matrix([mu1, mu2 + kw])        # DeltaM v = -kappa v
assert simplify(DeltaM*v_plus  - kappa*v_plus)  == Matrix([0,0])
assert simplify(DeltaM*v_minus + kappa*v_minus) == Matrix([0,0])
print("  soft eigenvector v_+ (eig +kappa):", v_plus.T)

print()
print("="*64)
print("STEP 2: are the eigenvectors B-orthogonal as well as Euclidean?")
print("="*64)
eucl = simplify(v_plus.dot(v_minus))
bdot = simplify((v_plus.T*B*v_minus)[0])
print(f"  v_+ . v_-      (Euclidean) = {eucl}")
print(f"  v_+^T B v_-    (B-metric)   = {bdot}")
print("  => Euclidean-orthogonal; B-NON-orthogonal unless that expr is 0.")

print()
print("="*64)
print("STEP 3: residue H0^T Pi_soft H0, both metrics")
print("="*64)
H0 = Matrix([h1, h2])

# Euclidean projector (as in both notes)
Pi_eucl = (v_plus*v_plus.T) / (v_plus.dot(v_plus))
res_eucl = simplify((H0.T*Pi_eucl*H0)[0])
print("\n(a) Euclidean residue (both notes' formula):")
sp.pprint(res_eucl)
print("  vanishes iff  v_+ . H0 = 0 :", simplify(v_plus.dot(H0)), "= 0")

# B-metric projector: oblique projector onto v_+ along v_- , then B-quadratic form.
# Spectral resolution of resolvent uses LEFT eigenvectors. For A=DeltaM symmetric
# in Euclidean sense, the correct residue weighting for chi = H0^T (L)^-1 H0 with
# the Euclidean source pairing is the Euclidean one. We ALSO report the B-metric
# source norm in case the physical pairing is B.
res_B_quad = simplify((H0.T*B*Pi_eucl*H0)[0])  # if source pairs through B on one side
print("\n(b) B-weighted residue H0^T B Pi_soft H0 (if physical pairing is B-on-source):")
sp.pprint(sp.factor(res_B_quad))

print()
print("="*64)
print("STEP 4: substitute the physical Bridge-Theorem source direction")
print("="*64)
# Bridge theorem: source aligned with J_Q s_* . Use corrected J_Q = (1/sqrt3)[[1,-2],[2,-1]].
sqrt3 = sqrt(3)
JQ = Matrix([[1,-2],[2,-1]])/sqrt3
s1, s2 = symbols('s1 s2', real=True)
s_star = Matrix([s1, s2])
H0_phys = JQ*s_star
print("  H0_phys = J_Q s_* =", simplify(H0_phys.T))

res_phys = simplify((H0_phys.T*Pi_eucl*H0_phys)[0])
print("\n  Euclidean residue at H0 = J_Q s_*:")
sp.pprint(sp.factor(res_phys))

# vanishing condition in physical direction
van = simplify(v_plus.dot(H0_phys))
print("\n  vanishes iff v_+ . (J_Q s_*) = 0:")
sp.pprint(sp.factor(van))

print()
print("="*64)
print("STEP 5: verdict")
print("="*64)
# Is the vanishing locus codimension-1 (a single alignment) in (s1,s2) for generic w?
print("  Euclidean residue is a perfect square / |v_+|^2  => >= 0 always.")
print("  It vanishes ONLY on the codim-1 locus v_+ . H0 = 0.")
print("  For H0 = J_Q s_*, that locus is a single line in s_* space per fixed w.")
print("  => Generic physical birth direction gives R_soft > 0 (nontrivial).")
