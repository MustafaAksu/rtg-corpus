"""
DZT-OPEN-0B: characterize the amplitude norm law  N_+(M_p) = N_{Q(zeta_p)^+/Q}(M_p).
M_p = Q_p/(i zeta_p^3),  real, in Q(zeta_p)^+.   N_full = Res(Phi_p, M_p) = N_+^2.

p=12..28 : re-extracted fresh from the Dyadic engine (audit).
p=32,36  : transcribed from the Dyadic horizon md, gated by |Q_p| against their table.
Overlap (16..28) is checked extract-vs-transcribe to validate transcription.
"""
import sympy as sp, math, cmath
from q4_extract import q4_03_cyclo
z = sp.symbols('z')

# --- transcribed polynomials from q4_03_cascade_horizon (4).md -------------
T = {}
T[16] = sp.Rational(1)*(6*z**7 -6*z**6 + sp.Rational(11,2)*z**5 - sp.Rational(7,2)*z**4
        + sp.Rational(7,2)*z**2 - sp.Rational(11,2)*z + 6)
T[20] = (-55*z**7 + sp.Rational(105,2)*z**6 + 10*z**5 - sp.Rational(39,2)*z**4
        - sp.Rational(55,2)*z**3 + sp.Rational(39,2)*z**2 + 45*z - sp.Rational(105,2))
T[24] = (47*z**7 - sp.Rational(91,2)*z**6 + 41*z**5 - sp.Rational(67,2)*z**4
        - sp.Rational(47,2)*z**3 + sp.Rational(67,2)*z**2 - 41*z + sp.Rational(91,2))
T[28] = (-sp.Rational(253,2)*z**11 + 136*z**10 - sp.Rational(25,2)*z**9 - 114*z**7
        + 110*z**6 + 27*z**5 - sp.Rational(101,2)*z**4 - 57*z**3 + sp.Rational(101,2)*z**2
        + 87*z - 110)
T[32] = (sp.Rational(95,2)*z**15 - sp.Rational(115,2)*z**14 + 65*z**13 - sp.Rational(139,2)*z**12
        + 71*z**11 - sp.Rational(139,2)*z**10 + 65*z**9 - sp.Rational(115,2)*z**8
        + sp.Rational(95,2)*z**7 - 36*z**6 + 24*z**5 - 12*z**4 + 12*z**2 - 24*z + 36)
T[36] = (-sp.Rational(469,2)*z**11 + 244*z**10 - 247*z**9 + 244*z**8 - sp.Rational(469,2)*z**7
        + sp.Rational(435,2)*z**6 + 42*z**5 - sp.Rational(167,2)*z**4 + sp.Rational(247,2)*z**3
        - sp.Rational(321,2)*z**2 + sp.Rational(385,2)*z - sp.Rational(435,2))
MOD_TABLE = {16:0.0128362,20:0.0145294,24:0.0156009,28:0.0163489,32:0.0169043,36:0.0173344}

def norm_data(p, Qpoly):
    Phi = sp.Poly(sp.cyclotomic_poly(p, z), z)
    red = lambda e: sp.rem(sp.Poly(sp.expand(e), z), Phi).as_expr()
    i_sym = z**(p//4)                       # i = zeta_p^{p/4}
    deninv = red(sp.invert(red(i_sym*z**3), Phi.as_expr(), z))
    Mp = red(Qpoly*deninv)
    is_real = sp.expand(red(Mp - Mp.subs(z, z**(p-1)))) == 0
    Nfull = sp.nsimplify(sp.resultant(Phi.as_expr(), Mp, z))
    Nplus = sp.nsimplify(sp.sqrt(sp.Abs(Nfull)))
    qn = complex(sp.N(Qpoly.subs(z, sp.exp(2*sp.I*sp.pi/p)), 40))
    return Mp, is_real, Nfull, Nplus, abs(qn)

print(f"{'p':>3} {'s=p/4':>6} {'phi/2':>6} {'|Q_p|':>11} {'M real':>7} {'N_full':>10} {'N_+':>8} {'v2(N_+)':>8} {'src':>10}")
seq = []
for p in [12,16,20,24,28,32,36]:
    if p <= 28:
        val,_,_ = q4_03_cyclo(p); src="extract"
        # if also transcribed, cross-check
        if p in T:
            Phi = sp.Poly(sp.cyclotomic_poly(p, z), z)
            diff = sp.rem(sp.Poly(sp.expand(val-T[p]),z),Phi).as_expr()
            src = "extract=md" if sp.expand(diff)==0 else "MISMATCH!"
        Q = val
    else:
        Q = T[p]; src="md(gated)"
        if abs(complex(sp.N(Q.subs(z, sp.exp(2*sp.I*sp.pi/p)),30))) - MOD_TABLE[p] > 1e-5:
            src = "GATE-FAIL"
    Mp, isreal, Nfull, Nplus, modq = norm_data(p, Q)
    v2 = sp.Rational(Nplus).q  # denominator
    v2exp = int(math.log2(v2)) if (v2 & (v2-1))==0 else None
    seq.append((p, p//4, int(sp.totient(p))//2, Nplus, v2exp))
    print(f"{p:>3} {p//4:>6} {int(sp.totient(p))//2:>6} {modq:>11.7f} {str(isreal):>7} {str(Nfull):>10} {str(Nplus):>8} {('2^-'+str(v2exp)) if v2exp is not None else '?':>8} {src:>10}")

print("\n--- norm-law pattern search ---")
print("p, s=p/4, N_+ = 2^-k :")
for p,s,half,Nplus,k in seq:
    print(f"  p={p:>3}  s={s:>2}  N_+=2^-{k}   (s mod 4={s%4}, s mod 2={s%2}, p mod 16={p%16}, #oddprimefac(s)={len(sp.factorint(s)) if s>1 else 0})")
