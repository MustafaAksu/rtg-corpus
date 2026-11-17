"""
DZT-side independent audit of DYAD-ART-CASCADE-Q4-03 + first DZT-OPEN-0B norm data.

For each p (4|p) we:
  1. reproduce Q_p from the Dyadic extraction (their script, fresh from raw F^p),
  2. check the phase law  arg(Q_p) = 90 + 1080/p  degrees,
  3. form M_p = Q_p / (i*z^3)   [i = z^(p/4) since 4|p], verify M_p is REAL
     (fixed under z->z^{-1} mod Phi_p), i.e. M_p in Q(zeta_p)^+,
  4. compute the field norm of M_p:
        N_full = N_{Q(zeta_p)/Q}(M_p) = Res(Phi_p, M_p)   (the SAME resultant object DZT uses)
     and the real-subfield norm N_plus with N_full = N_plus^2 (M_p real).
This is the norm-mechanism datum: does small M_p come with a small field norm?
"""
import sympy as sp
from q4_extract import q4_03_cyclo

z = sp.symbols('z')

def conj_mod(poly_in_z, p, Phi):
    # complex conjugation on Q(zeta_p): z -> z^{-1} = z^{p-1}
    e = sp.expand(poly_in_z.subs(z, z**(p-1)))
    return sp.rem(sp.Poly(e, z), Phi).as_expr()

print(f"{'p':>4} {'phi':>4} {'arg(deg)':>10} {'law 90+1080/p':>14} {'|Q_p|=M_p':>12} {'M real?':>8} {'N_full(M)':>16} {'N_plus(M)':>14}")
rows = []
for p in [8, 12, 16, 20, 24, 28]:
    val, zz, Phi = q4_03_cyclo(p)          # Q_p as polynomial in z mod Phi_p
    Phi = sp.Poly(sp.cyclotomic_poly(p, z), z)
    # numeric Q_p
    qn = complex(sp.N(val.subs(z, sp.exp(2*sp.I*sp.pi/p)), 40))
    arg_deg = (sp.arg(sp.nsimplify(qn)) if False else __import__('math').degrees(__import__('cmath').phase(qn)))
    law = 90 + 1080.0/p
    modQ = abs(qn)

    # M_p = Q_p / (i z^3), with i = z^(p/4)
    i_sym = z**(p//4)
    denom = sp.rem(sp.Poly(sp.expand(i_sym*z**3), z), Phi).as_expr()
    denom_inv = sp.invert(denom, Phi.as_expr(), z)
    Mp = sp.rem(sp.Poly(sp.expand(val*denom_inv), z), Phi).as_expr()
    # is M_p real? (fixed under conjugation)
    is_real = sp.expand(Mp - conj_mod(Mp, p, Phi)) == 0
    # field norm N_{Q(zeta_p)/Q}(M_p) = Res(Phi_p, M_p)
    Nfull = sp.resultant(Phi.as_expr(), Mp, z)
    Nfull = sp.nsimplify(Nfull)
    # real-subfield norm: N_full = N_plus^2 for M real
    Nplus = sp.sqrt(sp.Abs(Nfull)) * (1 if Nfull >= 0 else sp.nan)
    Nplus_s = sp.nsimplify(Nplus)
    rows.append((p, modQ, Nfull, Nplus_s))
    print(f"{p:>4} {int(sp.totient(p)):>4} {arg_deg:>10.4f} {law:>14.4f} {modQ:>12.7f} {str(is_real):>8} {str(Nfull):>16} {str(Nplus_s):>14}")

print("\n--- p=12 cross-check against the original DZT-ALG-P12-NORM (Q(sqrt3) reduced norm = 1/4) ---")
# at p=12, Q(zeta_12)^+ = Q(sqrt3); M_12 should be |Q_12| and its Q(sqrt3) norm the relevant one
p=12
val,_,_ = q4_03_cyclo(p)
v12 = sp.nsimplify(complex(sp.N(val.subs(z, sp.exp(2*sp.I*sp.pi/p)),40)).real, [sp.sqrt(3)])
print(f"Q_12 (real part, recognized) = {v12}")
print(f"matches -13+15*sqrt(3)/2 ? {sp.simplify(v12 - (-13+sp.Rational(15,2)*sp.sqrt(3)))==0}")
