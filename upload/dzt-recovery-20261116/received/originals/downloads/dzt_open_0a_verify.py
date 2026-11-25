import sympy as sp
x = sp.symbols('x')
N = 2*x**6 + x**5 - 5*x**4 - 3*x**3 - 4*x**2 + 2*x + 1

print("=== (i) b=5 channel: R_(0,5)(p) = Res(Phi_p, N) ===")
print(f"{'p':>4} {'phi(p)':>7} {'Res(Phi_p,N)':>18} {'zero?':>7}")
all_nonzero = True
for p in [6, 7, 8, 10, 12, 13, 14, 30]:
    Phi = sp.cyclotomic_poly(p, x)
    R = int(sp.resultant(Phi, N))     # = prod over primitive p-th roots of N(zeta)
    z = (R == 0)
    if z: all_nonzero = False
    print(f"{p:>4} {int(sp.totient(p)):>7} {R:>18} {str(z):>7}")
print(f"\nCERTIFIED: nonzero for ALL p (cyclotomic non-division, DYAD-OPEN-B5-ALLP).")
print(f"OBSERVED all nonzero = {all_nonzero} -> {'REPRODUCES' if all_nonzero else 'CONTRADICTS'}")

print("\n=== (ii) p=12 cascade-boundary near-miss field norm ===")
s3 = sp.sqrt(3)
v = -13 + sp.Rational(15,2)*s3
vbar = -13 - sp.Rational(15,2)*s3
norm = sp.expand(v*vbar)
print(f"v    = -13 + 15*sqrt(3)/2  ~ {float(v):.6f}")
print(f"vbar = -13 - 15*sqrt(3)/2  ~ {float(vbar):.6f}")
print(f"N_(Q(sqrt3)/Q)(v) = v*vbar = {norm}")
print(f"|v| ~ {abs(float(v)):.5f}  (Dyadic records modulus ~0.0096)")
