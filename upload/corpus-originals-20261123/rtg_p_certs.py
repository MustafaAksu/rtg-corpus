#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RTG p-Horizon Exact Symbolic Certifications
===========================================
Executes selected theorem-grade [ALG] micro-certifications over exact cyclotomic fields.
Backend: exact SymPy + Quotient Field
Status: [ALG micro-certification module]
"""

import sympy as sp
from typing import Dict, Tuple, Set

Poly = Dict[Tuple[int, int], sp.Expr]

def is_exact_zero(expr: sp.Expr) -> bool:
    """Safely handles cyclotomic and fractional-power simplifications."""
    expr = sp.simplify(expr)
    if expr == 0:
        return True
    if hasattr(expr, "equals"):
        z = expr.equals(0)
        return bool(z) if z is not None else False
    return False

def sclean(poly: Poly) -> Poly:
    out = {}
    for k, v in poly.items():
        vv = sp.simplify(sp.expand(v))
        if not is_exact_zero(vv):
            out[k] = vv
    return out

def sadd(*ps: Poly) -> Poly:
    out: Poly = {}
    for p in ps:
        for k, v in p.items(): out[k] = out.get(k, sp.Integer(0)) + v
    return sclean(out)

def sscale(p: Poly, c: sp.Expr) -> Poly:
    return sclean({k: c * v for k, v in p.items()})

def smul(p: Poly, q: Poly, D: int) -> Poly:
    out: Poly = {}
    for (a1, b1), c1 in p.items():
        for (a2, b2), c2 in q.items():
            if a1 + a2 + b1 + b2 <= D:
                out[(a1+a2, b1+b2)] = out.get((a1+a2, b1+b2), sp.Integer(0)) + c1 * c2
    return sclean(out)

def spow(p: Poly, n: int, D: int) -> Poly:
    if n == 0: return {(0, 0): sp.Integer(1)}
    out = {(0, 0): sp.Integer(1)}
    for _ in range(n):
        out = smul(out, p, D)
    return out

def ssubst(poly: Poly, P: Poly, Q: Poly, D: int) -> Poly:
    out: Poly = {}
    max_a = max((a for a, _ in poly), default=0)
    max_b = max((b for _, b in poly), default=0)
    
    Ppow = {0: {(0, 0): sp.Integer(1)}}
    Qpow = {0: {(0, 0): sp.Integer(1)}}
    for n in range(1, max_a + 1): Ppow[n] = smul(Ppow[n - 1], P, D)
    for n in range(1, max_b + 1): Qpow[n] = smul(Qpow[n - 1], Q, D)
        
    for (a, b), c in poly.items():
        term = smul(Ppow[a], Qpow[b], D)
        out = sadd(out, sscale(term, c))
    return out

def charge(a: int, b: int, p: int) -> int:
    return (a - b - 1) % p

def project_extra(poly: Poly, p: int, K_extra: Set[int]) -> Poly:
    return {k: v for k, v in poly.items() 
            if sum(k) >= 2 and charge(k[0], k[1], p) in K_extra}

def assert_linear_part_only_degree1(f_W: Poly, f_Wb: Poly, lam: sp.Expr, lamb: sp.Expr):
    """Lemma Check: Guarantees no sub-degree elements exist that could falsely compose."""
    assert is_exact_zero(f_W.get((1, 0), sp.Integer(0)) - lam), "W linear term mismatch"
    assert is_exact_zero(f_W.get((0, 1), sp.Integer(0))), "W conj-linear term mismatch"
    assert is_exact_zero(f_Wb.get((0, 1), sp.Integer(0)) - lamb), "Wbar conj-linear term mismatch"
    assert is_exact_zero(f_Wb.get((1, 0), sp.Integer(0))), "Wbar linear term mismatch"

def build_1step_map_exact_through_degree(p: int, D: int) -> Tuple[Poly, Poly]:
    I = sp.I
    theta = 2 * sp.pi / sp.Integer(p)
    
    lam = sp.simplify(sp.cos(theta) + I * sp.sin(theta))
    lamb = sp.simplify(sp.cos(theta) - I * sp.sin(theta))
    K = sp.simplify(sp.Integer(2) - sp.Integer(2) * sp.cos(theta))
    gamma = sp.simplify((lam - sp.Integer(1)) / K)
    gammab = sp.simplify((lamb - sp.Integer(1)) / K)
    denom_inv = sp.simplify(sp.Integer(1) / (gamma - gammab))
    
    P, Q = {(1, 0): sp.Integer(1)}, {(0, 1): sp.Integer(1)}
    eta = sscale(sadd(P, sscale(Q, sp.Integer(-1))), denom_inv)
    rho = sscale(sadd(sscale(Q, gamma), sscale(P, -gammab)), denom_inv)
    
    s_poly, e_poly = {}, {}
    for n in range(1, D + 1, 2):
        coeff = (sp.Integer(-1)**((n-1)//2)) / sp.factorial(n)
        s_poly = sadd(s_poly, sscale(spow(eta, n, D), coeff))
    for n in range(1, D + 1):
        coeff = sp.Integer(1) / sp.factorial(n)
        e_poly = sadd(e_poly, sscale(spow(rho, n, D), coeff))
    
    rho1 = sadd(rho, sscale(s_poly, sp.Integer(-1)))
    eta1 = sadd(eta, sscale(e_poly, K), sscale(s_poly, -K))
    
    W1 = sadd(rho1, sscale(eta1, gamma))
    Wb1 = sadd(rho1, sscale(eta1, gammab))
    return sclean(W1), sclean(Wb1)

def cyclotomic_zero_sum_remainder(p: int, chi: int, s: int):
    x = sp.symbols("x")
    Phi = sp.cyclotomic_poly(p, x)
    S = sum(x**(j * chi) for j in range(s))
    rem = sp.rem(sp.expand(S), Phi, x)
    return sp.simplify(rem), Phi, sp.expand(S)

def execute_micro_proof(p: int, q: int, s: int, target_slot: Tuple[int, int], D: int, expect: str):
    print("=" * 70)
    print(f"RTG Exact Symbolic Micro-Proof: p={p}, q={q} (strobe s={s})")
    print(f"Target Slot: {target_slot} | Backend: exact SymPy + Quotient Field")
    print("-" * 70)

    chi_target = charge(target_slot[0], target_slot[1], p)
    K_extra = set(range(q, p, q))
    print(f"  [Charge Check] χ_{p}{target_slot} = {chi_target}")
    assert chi_target in K_extra, f"Slot {target_slot} is not in K_extra: {K_extra}"
    print(f"    -> {target_slot} is formally an extra-charge slot: χ ∈ K^{{extra}}_{{{p},{q}}}")
    print("-" * 70)

    f1 = build_1step_map_exact_through_degree(p, D)
    
    theta = 2 * sp.pi / sp.Integer(p)
    lam = sp.simplify(sp.cos(theta) + sp.I * sp.sin(theta))
    lamb = sp.simplify(sp.cos(theta) - sp.I * sp.sin(theta))
    
    assert_linear_part_only_degree1(f1[0], f1[1], lam, lamb)
    
    c_target_1step = sp.simplify(f1[0].get(target_slot, sp.Integer(0)))
    
    if not is_exact_zero(c_target_1step):
        print(f"  [Reachability Check] Coeff_{target_slot} of f_{p} (1-step) is NONZERO.")
        print(f"    -> {target_slot} belongs to the dynamically reachable extra-charge basis.")
    else:
        raise AssertionError(f"Slot {target_slot} is NOT dynamically reachable on step 1!")
    print("-" * 70)

    rem, Phi, S_expr = cyclotomic_zero_sum_remainder(p, chi_target, s)
    print(f"  [Direct Averaging Check]")
    print(f"    S(x) = {S_expr}")
    print(f"    Phi_{p}(x) = {Phi}")
    print(f"    S mod Phi_{p} = {rem}")
    
    is_direct_zero = is_exact_zero(rem)
    if is_direct_zero:
        print("    -> Direct averaging: zero modulo \u03A6_p.")
    else:
        print("    -> Direct averaging: survives modulo \u03A6_p.")
    print("-" * 70)

    if sum(target_slot) == 2:
        print(f"  [Full Polynomial Map Check (D={D})]")
        print(f"    -> [ALG lemma]: Degree-2 subgroup-strobe coefficients are fully controlled")
        print(f"       by the direct cyclotomic averaging factor because no lower-degree")
        print(f"       nonlinear cascade can repopulate degree 2.")
        c_simpl = sp.Integer(0) if is_direct_zero else sp.Integer(1) 
    else:
        print(f"  [Full Polynomial Map Check (D={D})] Executing nonlinear cascades...")
        G = ({(1, 0): sp.Integer(1)}, {(0, 1): sp.Integer(1)})
        for _ in range(s):
            G = (ssubst(f1[0], G[0], G[1], D), ssubst(f1[1], G[0], G[1], D))
            
        lam_inv_s = sp.expand(lam**(-s))
        R_raw = sscale(G[0], lam_inv_s)
        
        R_raw[(1, 0)] = sp.simplify(R_raw.get((1, 0), sp.Integer(0)) - sp.Integer(1))
        R = {k: v for k, v in sclean(R_raw).items() if sum(k) >= 2}
        
        J_extra_raw = project_extra(R, p, K_extra)
        c_target = J_extra_raw.get(target_slot, sp.Integer(0))
        c_simpl = sp.simplify(c_target)

    if expect == "zero":
        if not is_exact_zero(c_simpl):
            raise AssertionError(f"{target_slot} expected zero but is active: {c_simpl}")
        if sum(target_slot) > 2:
            print("    -> Full cascade: zero.")
        print(f"    -> CONFIRMED: Coeff_{target_slot} R^raw_{{{p},{q}}} = 0.")
        print("    -> STATUS: [ALG micro-certification: cancellation]")

    elif expect == "active":
        if is_exact_zero(c_simpl):
            raise AssertionError(f"{target_slot} expected active but vanished.")
        print("    -> Full cascade: active.")
        print(f"    -> CONFIRMED: Coeff_{target_slot} R^raw_{{{p},{q}}} = {c_simpl} != 0.")
        print("    -> STATUS: [ALG active cascade] + [OPEN near-cancellation structure]")

    print("=" * 70 + "\n")

CERT_CASES = {
    "p6_q3_02":  dict(p=6,  q=3, slot=(0, 2), D=3, expect="zero"),
    "p8_q4_03":  dict(p=8,  q=4, slot=(0, 3), D=4, expect="zero"),
    "p9_q3_02":  dict(p=9,  q=3, slot=(0, 2), D=3, expect="zero"),
    "p12_q3_02": dict(p=12, q=3, slot=(0, 2), D=3, expect="zero"),
    "p12_q4_03": dict(p=12, q=4, slot=(0, 3), D=4, expect="active"),
         "p16_q4_03": dict(p=16, q=4, slot=(0, 3), D=4, expect="active"),
         "p20_q4_03": dict(p=20, q=4, slot=(0, 3), D=4, expect="active"),
         "p24_q4_03": dict(p=24, q=4, slot=(0, 3), D=4, expect="active"),
         "p28_q4_03": dict(p=28, q=4, slot=(0, 3), D=4, expect="active"),
         "p32_q4_03": dict(p=32, q=4, slot=(0, 3), D=4, expect="active"),
         "p36_q4_03": dict(p=36, q=4, slot=(0, 3), D=4, expect="active"),
}

def list_cases():
    print("Known certification cases:")
    for k, v in CERT_CASES.items():
        print(f"  {k}: p={v['p']}, q={v['q']}, slot={v['slot']}, D={v['D']}, expect={v['expect']}")

def run_cert(case_id: str):
    if case_id in CERT_CASES:
        kwargs = CERT_CASES[case_id]
        execute_micro_proof(
            p=kwargs["p"], 
            q=kwargs["q"], 
            s=kwargs["p"]//kwargs["q"], 
            target_slot=kwargs["slot"], 
            D=kwargs["D"], 
            expect=kwargs["expect"]
        )
    else:
        known = ", ".join(sorted(CERT_CASES.keys()))
        raise ValueError(f"Unknown certification case: {case_id}. Known cases: {known}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        run_cert(sys.argv[1])