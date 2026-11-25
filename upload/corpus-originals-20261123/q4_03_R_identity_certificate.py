#!/usr/bin/env python3
"""
q4_03_R_identity_certificate.py

Exact certificate for the q=4,(0,3) cascade phase law remainder relation.

For p=4s, s>=2, let L=zeta_p and I=L^s=i.  Let
    Q_p = [lambda^{-s} f^s]^W_(0,3) = [calH_s]^W_(0,3)
for calH_s=L^{-s} f^s.  The certificate derives Q_p from the degree-3
near-identity recursion
    (calH_s)_3 = sum_j H_{j,3} + sum_{j<k} D H_{k,2} . H_{j,2}
with H_j=L^{-j} h L^j, h=L^{-1} f.

It proves the closed expression
    Q(L,I) = L^5*(I*L^2 + I - L^2 + 1)
             / (2*(L+1)^4*(L^2+L+1))
then verifies
    sigma(Q) = -L^{-6} Q,
where sigma: L -> L^{-1}, I -> -I.
Equivalently Q = I*L^3*M with M in the real subfield, and the nonzero
phase law is Q_p=i*zeta_p^3*M_p.

Denominator guard for p=4s, s>=2: L is a primitive p-th root, so L!=-1
and L^2+L+1!=0.  The p=8 zero degeneracy is included by the formula.
"""
import argparse
import sympy as sp

L, I = sp.symbols("L I")


def ipow(c: int):
    return {0: sp.Integer(1), 1: I, 2: sp.Integer(-1), 3: -I}[c % 4]


def S(c: int):
    """Collapsed S_c=sum_{j=0}^{s-1} L^{c j} at L^s=I, for c != 0."""
    if c == 0:
        raise ValueError("S(0)=s is secular; it is not needed in this certificate")
    num = ipow(c) - 1
    if num == 0:
        return sp.Integer(0)
    return sp.cancel(num / (L**c - 1))


def S_order(a: int, b: int):
    """Collapsed ordered sum sum_{0<=j<k<=s-1} L^{a*j+b*k}."""
    if a == 0:
        raise ValueError("a=0 ordered secular case is not needed in this certificate")
    return sp.cancel((S(a + b) - S(b)) / (L**a - 1))


def sigma(expr):
    """Complex conjugation on Q(I)(L): L -> L^{-1}, I -> -I."""
    return sp.cancel(expr.xreplace({L: 1 / L, I: -I}))


def build_Q():
    """Build Q=[calH_s]^W_(0,3) from the exact degree-3 path formula."""
    # Needed h=L^{-1}f coefficients in W/Wbar coordinates.
    hW03 = (2*L**3 - 4*L**2 + 3*L - 1) / (6*(L + 1)**3)
    hW02 = (L**2 - L) / (2*(L + 1)**2)
    hB02 = (-L**3 + L**2) / (2*(L + 1)**2)
    hW11 = (L - 1) / ((L + 1)**2)

    # Charges for W component: chi_W(a,b)=a-b-1.
    # Charges for Wbar component: chi_B(a,b)=a-b+1.
    # Single cubic path: hW03 has charge -4 and cancels by S(-4)=0.
    single = hW03 * S(-4)

    # Ordered quadratic-quadratic paths feeding W_(0,3):
    # 1) derivative of W_(0,2) wrt Wbar times Wbar_(0,2).
    #    charges j=-1, k=-3, derivative factor b=2.
    path_db = 2 * hW02 * hB02 * S_order(-1, -3)

    # 2) derivative of W_(1,1) wrt W times W_(0,2).
    #    charges j=-3, k=-1, derivative factor a=1.
    path_dw = hW11 * hW02 * S_order(-3, -1)

    Q = sp.cancel(single + path_db + path_dw)
    return sp.factor(Q)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--horizon", nargs="*", type=int, default=[8,12,16,20,24,28,32,36,40,44,48,52])
    args = ap.parse_args()

    Q = build_Q()
    expected = sp.factor(L**5*(I*L**2 + I - L**2 + 1)/(2*(L+1)**4*(L**2+L+1)))
    print("Q(L,I) =")
    print(Q)
    print("\nclosed-form match:", sp.simplify(Q - expected) == 0)

    # Remainder relation for Q: sigma(Q) = -L^-6 Q.
    diff_Q = sp.factor(sp.cancel(sigma(Q) + L**(-6)*Q))
    print("\nidentity sigma(Q) + L^-6 Q =")
    print(diff_Q)
    if diff_Q != 0:
        raise SystemExit(1)

    # A=L^s Q=I Q satisfies sigma(A)=L^-6 A.
    A = sp.cancel(I*Q).subs(I**2, -1)
    diff_A = sp.factor(sp.cancel(sigma(A) - L**(-6)*A).subs(I**2, -1))
    print("\nidentity sigma(A) - L^-6 A =")
    print(diff_A)
    if diff_A != 0:
        raise SystemExit(1)

    # Real-amplitude check: M=Q/(I L^3) is conjugation fixed.
    M = sp.cancel(Q/(I*L**3)).subs(I**2, -1)
    diff_M = sp.factor(sp.cancel(sigma(M) - M).subs(I**2, -1))
    print("\nM(L,I)=Q/(I L^3) is real-subfield fixed; sigma(M)-M =")
    print(diff_M)
    if diff_M != 0:
        raise SystemExit(1)

    print("\nDenominator guard: (L+1)^4*(L^2+L+1) is nonzero for primitive p-th roots with p=4s, s>=2.")

    print("\nHorizon numeric check:")
    for p in args.horizon:
        if p % 4 != 0:
            raise SystemExit(f"p={p} is not divisible by 4")
        val = complex(sp.N(Q.subs({L: sp.exp(2*sp.pi*sp.I/p), I: sp.I}), 30))
        print(f"  p={p:2d}: {val.real:+.15f}{val.imag:+.15f}i |Q|={abs(val):.15f}")

    print("\nCERTIFICATE PASS")


if __name__ == "__main__":
    main()
