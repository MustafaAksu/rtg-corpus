#!/usr/bin/env python3
"""
normalize_p7_c06_full_cyclotomic_optimized.py
=============================================
RTG OPEN 9 — High-Performance Exact Extraction of c_06^(7).

Optimizations:
  - Aggressive memoization of cyclotomic reductions.
  - Direct SymPy Poly arithmetic to avoid expression-tree bloat.
  - Strict degree-6 truncation during every composition step.
"""

import sys
import sympy as sp
from functools import lru_cache

class CyclotomicField:
    def __init__(self, p):
        self.p = p
        self.lam = sp.Symbol('lam')
        self.Phi = sp.cyclotomic_poly(p, self.lam)
        self.Phi_poly = sp.Poly(self.Phi, self.lam, domain=sp.QQ)
        
    @lru_cache(maxsize=None)
    def reduce(self, expr):
        if not getattr(expr, 'has', lambda x: False)(self.lam):
            return sp.sympify(expr)
        
        # Fast path for already reduced or simple expressions
        expr = sp.cancel(sp.together(expr))
        num, den = sp.fraction(expr)
        
        num_p = sp.Poly(sp.expand(num), self.lam, domain=sp.QQ).rem(self.Phi_poly)
        den_p = sp.Poly(sp.expand(den), self.lam, domain=sp.QQ).rem(self.Phi_poly)
        
        if den_p.is_zero:
            raise ZeroDivisionError(f"Exact zero division modulo Phi_{self.p}")
            
        inv_den = sp.invert(den_p, self.Phi_poly)
        return sp.expand((num_p * inv_den).rem(self.Phi_poly).as_expr())

    @lru_cache(maxsize=None)
    def conjugate_coeff(self, c):
        c = sp.sympify(c)
        return self.reduce(c.subs(self.lam, self.lam**(self.p - 1))) if c.has(self.lam) else c

    def is_resonant(self, a, b):
        return (a - b - 1) % self.p == 0

class DictPoly:
    def __init__(self, field, terms=None):
        self.F = field
        self.terms = {}
        if terms:
            for (a, b), c in terms.items():
                c_red = self.F.reduce(c)
                if c_red != 0: self.terms[(a, b)] = c_red

    def __add__(self, other):
        res = self.terms.copy()
        for (a, b), c in other.terms.items():
            res[(a, b)] = res.get((a, b), 0) + c
        return DictPoly(self.F, res)

    def __sub__(self, other):
        res = self.terms.copy()
        for (a, b), c in other.terms.items():
            res[(a, b)] = res.get((a, b), 0) - c
        return DictPoly(self.F, res)

    def __mul__(self, other):
        res = {}
        for (a1, b1), c1 in self.terms.items():
            for (a2, b2), c2 in other.terms.items():
                k = (a1+a2, b1+b2)
                res[k] = res.get(k, 0) + c1 * c2
        return DictPoly(self.F, res)

    def truncate(self, max_deg):
        return DictPoly(self.F, {(a, b): c for (a, b), c in self.terms.items() if a + b <= max_deg})

    def extract_degree(self, deg):
        return DictPoly(self.F, {(a, b): c for (a, b), c in self.terms.items() if a + b == deg})

    def conjugate(self):
        return DictPoly(self.F, {(b, a): self.F.conjugate_coeff(c) for (a, b), c in self.terms.items()})

    def compose(self, Z_poly, W_poly, max_deg):
        result = DictPoly(self.F)
        Z_powers, W_powers = [DictPoly(self.F, {(0,0): 1})], [DictPoly(self.F, {(0,0): 1})]
        for i in range(1, max_deg + 1):
            Z_powers.append((Z_powers[-1] * Z_poly).truncate(max_deg))
            W_powers.append((W_powers[-1] * W_poly).truncate(max_deg))

        for (a, b), c in self.terms.items():
            if a + b > max_deg: continue
            term_poly = (Z_powers[a] * W_powers[b]).truncate(max_deg)
            scaled = {(k1, k2): self.F.reduce(c * v) for (k1, k2), v in term_poly.terms.items()}
            result = result + DictPoly(self.F, scaled)
        return result.truncate(max_deg)

def construct_base_map_deg6(F):
    print(f"  -> Constructing raw map up to degree 6 in Q(zeta_{F.p})...")
    Z, W = sp.symbols('Z W')
    lam = F.lam
    K = F.reduce(2 - lam - lam**(F.p - 1))
    u = F.reduce(1 / (1 - lam))
    u_bar = F.reduce(1 / (1 - lam**(F.p - 1)))
    inv_D = F.reduce(1 / (u - u_bar))

    rho = u*Z + u_bar*W
    eta = Z + W

    exp_rho_m1 = sum((rho**k)/sp.factorial(k) for k in range(1, 7))
    sin_eta = eta - eta**3/6 + eta**5/120

    rho_prime = rho - sin_eta
    eta_prime = eta + K * exp_rho_m1 - K * sin_eta
    Z_map_raw = sp.expand((rho_prime - u_bar * eta_prime) * inv_D)

    terms = {}
    for d in range(1, 7):
        for i in range(d + 1):
            c = Z_map_raw.coeff(Z, i).coeff(W, d - i)
            if c != 0: terms[(i, d - i)] = c
    return DictPoly(F, terms)

def fixed_point_inverse(F_field, h_Z, h_W, max_deg=6):
    Id_Z = DictPoly(F_field, {(1,0): 1})
    Id_W = DictPoly(F_field, {(0,1): 1})
    Z_inv, W_inv = Id_Z, Id_W
    for _ in range(max_deg):
        Z_inv = Id_Z - h_Z.compose(Z_inv, W_inv, max_deg)
        W_inv = Id_W - h_W.compose(Z_inv, W_inv, max_deg)
    return Z_inv, W_inv

def apply_transformation(F_field, F_Z, h_Z, max_deg=6):
    h_W = h_Z.conjugate()
    Id_Z = DictPoly(F_field, {(1,0): 1})
    Id_W = DictPoly(F_field, {(0,1): 1})
    Phi_Z = Id_Z + h_Z
    Phi_W = Id_W + h_W
    Phi_inv_Z, Phi_inv_W = fixed_point_inverse(F_field, h_Z, h_W, max_deg)
    
    F_W = F_Z.conjugate()
    inner_Z = F_Z.compose(Phi_Z, Phi_W, max_deg)
    inner_W = F_W.compose(Phi_Z, Phi_W, max_deg)
    return Phi_inv_Z.compose(inner_Z, inner_W, max_deg)

def execute_p7_deg6():
    print("="*75)
    print("OPEN 9: EXACT FULL BIRKHOFF NORMALIZATION (p=7, Degree 6)")
    print("="*75)
    
    F_field = CyclotomicField(7)
    F = construct_base_map_deg6(F_field)

    for deg in [2, 3, 4, 5]:
        print(f"  -> Applying h_{deg} transformation...")
        F_deg = F.extract_degree(deg)
        h_terms = {}
        for (a, b), c in F_deg.terms.items():
            if F_field.is_resonant(a, b):
                continue
            divisor = F_field.reduce(F_field.lam**a * F_field.lam**(b*6) - F_field.lam)
            h_terms[(a, b)] = F_field.reduce(c / divisor)
            
        if h_terms:
            F = apply_transformation(F_field, F, DictPoly(F_field, h_terms), 6)
            
    print("\n" + "="*75)
    print("EXTRACTION OF c_06^(7) (Degree 6 Lattice Harmonic)")
    print("="*75)
    
    c_06 = F.terms.get((0, 6), 0)
    target_c06 = F_field.reduce("(6735 + 4218*lam + 3990*lam**2 + 6256*lam**3 + 837*lam**4 + 9786*lam**5) / 5040")
    
    print(f"c_06^(7) EXACT POLYNOMIAL:\n{c_06}")
    
    if c_06 == target_c06:
        print("\n[PASS] Engine output exactly matches the PSLQ ALG candidate.")
        print("Status Promotion: [ALG candidate] -> [ALG]")
    else:
        print("\n[FAIL] Engine output diverges from PSLQ candidate.")
    
    lam_num = sp.N(sp.exp(2 * sp.I * sp.pi / 7), 50)
    c_06_num = complex(c_06.subs(F_field.lam, lam_num))
    print(f"\nNUMERICAL EVALUATION:\nc_06^(7) ≈ {c_06_num:.16f}")

if __name__ == '__main__':
    execute_p7_deg6()