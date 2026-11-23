#!/usr/bin/env python3
"""
prove_p5_lattice_anomaly_exact_v2.py
====================================
Exact proof that G_{lattice}(5) = |F_1^5(0,4) - F_{raw}^5(0,4)| = 0
Executes fully in Q(zeta_5) using the exact DictPoly engine.
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

def construct_base_map_deg4(F):
    Z, W = sp.symbols('Z W')
    lam = F.lam
    K = F.reduce(2 - lam - lam**(F.p - 1))
    u = F.reduce(1 / (1 - lam))
    u_bar = F.reduce(1 / (1 - lam**(F.p - 1)))
    inv_D = F.reduce(1 / (u - u_bar))

    rho = u*Z + u_bar*W
    eta = Z + W

    exp_rho_m1 = rho + rho**2/2 + rho**3/6 + rho**4/24
    sin_eta = eta - eta**3/6

    rho_prime = rho - sin_eta
    eta_prime = eta + K * exp_rho_m1 - K * sin_eta
    Z_map_raw = sp.expand((rho_prime - u_bar * eta_prime) * inv_D)

    terms = {}
    for d in range(1, 5):
        for i in range(d + 1):
            c = Z_map_raw.coeff(Z, i).coeff(W, d - i)
            if c != 0: terms[(i, d - i)] = c
    return DictPoly(F, terms)

def fixed_point_inverse(F_field, h_Z, h_W, max_deg=4):
    Id_Z = DictPoly(F_field, {(1,0): 1})
    Id_W = DictPoly(F_field, {(0,1): 1})
    Z_inv, W_inv = Id_Z, Id_W
    for _ in range(max_deg):
        Z_inv = Id_Z - h_Z.compose(Z_inv, W_inv, max_deg)
        W_inv = Id_W - h_W.compose(Z_inv, W_inv, max_deg)
    return Z_inv, W_inv

def apply_transformation(F_field, F_Z, h_Z, max_deg=4):
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

def run_exact_p5_anomaly():
    print("="*65)
    print("OPEN 9: EXACT PROOF of p=5 LATTICE ANOMALY G_{04}^{(5)} = 0")
    print("="*65)
    
    F_field = CyclotomicField(5)
    print("  -> Constructing raw map f_raw through degree 4...")
    f_raw = construct_base_map_deg4(F_field)

    print("\n1. Computing F_{raw}^5 (5-fold composition of raw map)...")
    F_raw_5 = f_raw
    for step in range(4):
        F_raw_5 = f_raw.compose(F_raw_5, F_raw_5.conjugate(), 4)
        
    print("\n2. Computing F_1 (One-Step Normal Form)...")
    F_1 = f_raw
    for deg in [2, 3, 4]:
        F_deg = F_1.extract_degree(deg)
        h_terms = {}
        for (a, b), c in F_deg.terms.items():
            if F_field.is_resonant(a, b):
                continue
            divisor = F_field.reduce(F_field.lam**a * F_field.lam**(b*4) - F_field.lam)
            h_terms[(a, b)] = F_field.reduce(c / divisor)
        if h_terms:
            F_1 = apply_transformation(F_field, F_1, DictPoly(F_field, h_terms), 4)

    print("\n3. Computing F_1^5 (5-fold composition of normal form)...")
    F_1_5 = F_1
    for step in range(4):
        F_1_5 = F_1.compose(F_1_5, F_1_5.conjugate(), 4)

    print("\n" + "="*65)
    print("EXTRACTION AND COMPARISON")
    print("="*65)
    
    c_raw_04 = F_raw_5.terms.get((0, 4), 0)
    c_norm_04 = F_1_5.terms.get((0, 4), 0)
    gap = F_field.reduce(c_norm_04 - c_raw_04)
    
    print(f"F_{{raw}}^5(0,4) = {c_raw_04}")
    print(f"F_1^5(0,4)   = {c_norm_04}")
    print(f"Gap (Difference) = {gap}")
    
    if gap == 0:
        print("\n[PASS] Exact cyclotomic cancellation verified.")
        print("Status Promotion: [NUM strong] -> [ALG]")
    else:
        print("\n[FAIL] Exact gap is non-zero.")

if __name__ == "__main__":
    run_exact_p5_anomaly()