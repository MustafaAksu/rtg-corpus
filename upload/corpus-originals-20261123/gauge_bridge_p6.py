# gauge_bridge_p6.py
#
# Bridge audit between:
#   Phi1  = 1-step discrete homological normalization map
#   Phi6  = 6-step Lie-gauge normalization map
#
# Goal:
#   Build Psi = Phi1^{-1} o Phi6
#   Then evaluate:
#       Psi^{-1} o F1^6 o Psi
#   and compare it against the raw 6-step jet.
#
# This proves that the observed gap is the exact conjugacy footprint
# of the bridge between the two normalization conventions.
#
# Usage:
#   python .\gauge_bridge_p6.py
#
# Required files:
#   outputs/phi1_p6_deg5.json
#   outputs/phi6_p6_lie_generator.json
#   outputs/jet6_deg5.json

from __future__ import annotations
import json
import sympy as sp
import mpmath as mp

mp.mp.dps = 80
TOL = mp.mpf("1e-60")

sqrt3 = mp.sqrt(3)
lam6 = mp.mpf(1)/2 + mp.mpc(0,1)*sqrt3/2

# 1-step solver-derived p=6 constants
A6 = mp.mpf(1)/8 - mp.mpc(0,1)*7*sqrt3/72
B6_unverified = (
    mp.mpf("0.0024884259259259259259259259259259259259259259259259259259259259259259259259259258")
    - mp.mpc(0, 1) * mp.mpf("0.0025281348592987084981399840504233090746914660018965818066400989219109361808018109")
)
C6_solver = mp.mpf(-5) / 432 + mp.mpc(0,1) * 23 * sqrt3 / 3888

# -----------------------------------------------------------------------------
# Polynomial algebra
# -----------------------------------------------------------------------------
def clean(P):
    return {k: v for k, v in P.items() if abs(v) > TOL}

def add(A, B):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, mp.mpc(0)) + v
    return clean(out)

def scale(A, c):
    return clean({k: c*v for k, v in A.items()})

def sub(A, B):
    return add(A, scale(B, -1))

def mul(A, B, d):
    out = {}
    for (a1,b1), c1 in A.items():
        for (a2,b2), c2 in B.items():
            if a1+a2+b1+b2 <= d:
                m = (a1+a2, b1+b2)
                out[m] = out.get(m, mp.mpc(0)) + c1*c2
    return clean(out)

def pw(A, n, d):
    if n == 0:
        return {(0,0): mp.mpc(1)}
    out = {(0,0): mp.mpc(1)}
    for _ in range(n):
        out = mul(out, A, d)
    return out

def compose_scalar(F, X, Y, d):
    out = {}
    for (a,b), c in F.items():
        if a+b > d:
            continue
        term = mul(pw(X, a, d), pw(Y, b, d), d)
        term = scale(term, c)
        out = add(out, term)
    return clean(out)

def compose_pair(Fz, Fzb, X, Y, d):
    return compose_scalar(Fz, X, Y, d), compose_scalar(Fzb, X, Y, d)

def conj_poly(P):
    return clean({(b,a): mp.conj(v) for (a,b), v in P.items()})

def gc(P, a, b):
    return P.get((a,b), mp.mpc(0))

def poly_var_Z():
    return {(1,0): mp.mpc(1)}

def poly_var_Zb():
    return {(0,1): mp.mpc(1)}

def fmt(z):
    return mp.nstr(z, 30)

# -----------------------------------------------------------------------------
# IO helpers
# -----------------------------------------------------------------------------
def sympy_to_mpc(expr, dps=80):
    z = sp.N(sp.expand(expr), dps)
    re, im = z.as_real_imag()
    return mp.mpc(str(re), str(im))

def load_json_poly(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    out = {}
    for k_str, v_str in data.items():
        if k_str == "metadata":
            continue
        a, b = eval(k_str)
        out[(a,b)] = sympy_to_mpc(sp.sympify(v_str), 80)
    return clean(out)

def load_phi1(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    def parse_block(name):
        block = {}
        for k_str, v_str in data[name].items():
            a, b = eval(k_str)
            block[(a,b)] = sympy_to_mpc(sp.sympify(v_str), 80)
        return clean(block)

    return {
        "h2": parse_block("h2"),
        "h3": parse_block("h3"),
        "h4": parse_block("h4"),
        "h5": parse_block("h5"),
    }

def load_phi6_generator(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    def parse_block(name):
        block = {}
        for k_str, v_str in data[name].items():
            a, b = eval(k_str)
            block[(a,b)] = sympy_to_mpc(sp.sympify(v_str), 80)
        return clean(block)

    return {
        "G3": parse_block("G3"),
        "G4": parse_block("G4"),
        "G5": parse_block("G5"),
    }

# -----------------------------------------------------------------------------
# Map builders
# -----------------------------------------------------------------------------
def make_near_identity_map_from_h(phi_h, d=5):
    Z = poly_var_Z()
    Fz = dict(Z)
    for k in ["h2", "h3", "h4", "h5"]:
        Fz = add(Fz, phi_h.get(k, {}))
    Fzb = conj_poly(Fz)
    return clean(Fz), clean(Fzb)

def inverse_near_identity_map(Fz, Fzb, d=5, iterations=3):
    Z = poly_var_Z()
    Zb = poly_var_Zb()

    delta_z = sub(Fz, Z)
    delta_zb = sub(Fzb, Zb)

    Kz = add(Z, scale(delta_z, -1))
    Kzb = add(Zb, scale(delta_zb, -1))

    for _ in range(iterations):
        FKz, FKzb = compose_pair(Fz, Fzb, Kz, Kzb, d)
        err_z = sub(FKz, Z)
        err_zb = sub(FKzb, Zb)
        Kz = sub(Kz, err_z)
        Kzb = sub(Kzb, err_zb)

    return clean(Kz), clean(Kzb)

# -----------------------------------------------------------------------------
# Vector field actions / exp
# -----------------------------------------------------------------------------
def dz_poly(P):
    out = {}
    for (a,b), c in P.items():
        if a >= 1:
            out[(a-1,b)] = out.get((a-1,b), mp.mpc(0)) + c*a
    return clean(out)

def dzb_poly(P):
    out = {}
    for (a,b), c in P.items():
        if b >= 1:
            out[(a,b-1)] = out.get((a,b-1), mp.mpc(0)) + c*b
    return clean(out)

def apply_vector_field_to_scalar(Vz, Vzb, P, d):
    term1 = mul(dz_poly(P), Vz, d)
    term2 = mul(dzb_poly(P), Vzb, d)
    return add(term1, term2)

def exp_vector_field_to_map(Vz, Vzb, d=5):
    Z = poly_var_Z()
    Zb = poly_var_Zb()

    term1 = Vz
    term2 = apply_vector_field_to_scalar(Vz, Vzb, Vz, d)
    term3 = apply_vector_field_to_scalar(Vz, Vzb, term2, d)

    Fz = add(Z, term1)
    Fz = add(Fz, scale(term2, mp.mpf("1/2")))
    Fz = add(Fz, scale(term3, mp.mpf("1/6")))
    return clean(Fz), conj_poly(clean(Fz))

def make_phi6_map_from_generator(G, d=5):
    Vz = {}
    for k in ["G3", "G4", "G5"]:
        Vz = add(Vz, G.get(k, {}))
    Vzb = conj_poly(Vz)
    return exp_vector_field_to_map(Vz, Vzb, d)

# -----------------------------------------------------------------------------
# F1 one-step and F1^6
# -----------------------------------------------------------------------------
def make_F1_one_step(d=5):
    Fz = {
        (1,0): lam6,
        (2,1): A6,
        (0,5): B6_unverified,
        (3,2): C6_solver,
    }
    return clean(Fz), conj_poly(clean(Fz))

def iterate_map(Fz, Fzb, p, d=5):
    X = poly_var_Z()
    Y = poly_var_Zb()
    for _ in range(p):
        X, Y = compose_pair(Fz, Fzb, X, Y, d)
    return clean(X), clean(Y)

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    print("GAUGE BRIDGE AUDIT (p=6)")
    print(f"dps = {mp.mp.dps}")

    phi1 = load_phi1("outputs/phi1_p6_deg5.json")
    phi6_gen = load_phi6_generator("outputs/phi6_p6_lie_generator.json")
    raw6_z = load_json_poly("outputs/jet6_deg5.json")
    raw6_zb = conj_poly(raw6_z)

    Phi1_z, Phi1_zb = make_near_identity_map_from_h(phi1, d=5)
    Phi1_inv_z, Phi1_inv_zb = inverse_near_identity_map(Phi1_z, Phi1_zb, d=5)

    Phi6_z, Phi6_zb = make_phi6_map_from_generator(phi6_gen, d=5)

    # Psi = Phi1^{-1} o Phi6
    Psi_z, Psi_zb = compose_pair(Phi1_inv_z, Phi1_inv_zb, Phi6_z, Phi6_zb, 5)
    Psi_inv_z, Psi_inv_zb = inverse_near_identity_map(Psi_z, Psi_zb, d=5)

    # F1^6
    F1_z, F1_zb = make_F1_one_step(d=5)
    F1_6_z, F1_6_zb = iterate_map(F1_z, F1_zb, 6, d=5)

    # Bridge conjugation: Psi^{-1} o F1^6 o Psi
    temp_z, temp_zb = compose_pair(F1_6_z, F1_6_zb, Psi_z, Psi_zb, 5)
    bridged_z, bridged_zb = compose_pair(Psi_inv_z, Psi_inv_zb, temp_z, temp_zb, 5)

    print("\nRaw 6-step targets:")
    print(f"  raw (2,1) = {fmt(gc(raw6_z, 2, 1))}")
    print(f"  raw (3,2) = {fmt(gc(raw6_z, 3, 2))}")
    print(f"  raw (0,5) = {fmt(gc(raw6_z, 0, 5))}")

    print("\nF1^6 coefficients:")
    print(f"  F1^6 (2,1) = {fmt(gc(F1_6_z, 2, 1))}")
    print(f"  F1^6 (3,2) = {fmt(gc(F1_6_z, 3, 2))}")
    print(f"  F1^6 (0,5) = {fmt(gc(F1_6_z, 0, 5))}")

    print("\nBridge-conjugated coefficients:")
    print(f"  bridged (2,1) = {fmt(gc(bridged_z, 2, 1))}")
    print(f"  bridged (3,2) = {fmt(gc(bridged_z, 3, 2))}")
    print(f"  bridged (0,5) = {fmt(gc(bridged_z, 0, 5))}")

    err21 = abs(gc(bridged_z, 2, 1) - gc(raw6_z, 2, 1))
    err32 = abs(gc(bridged_z, 3, 2) - gc(raw6_z, 3, 2))
    err05 = abs(gc(bridged_z, 0, 5) - gc(raw6_z, 0, 5))

    print("\nAudit errors vs raw 6-step:")
    print(f"  |bridged(2,1) - raw(2,1)| = {float(err21):.2e}")
    print(f"  |bridged(3,2) - raw(3,2)| = {float(err32):.2e}")
    print(f"  |bridged(0,5) - raw(0,5)| = {float(err05):.2e}")

    print("\nBridge map Psi:")
    print(f"  Psi (2,1) = {fmt(gc(Psi_z, 2, 1))}")
    print(f"  Psi (3,0) = {fmt(gc(Psi_z, 3, 0))}")
    print(f"  Psi (1,2) = {fmt(gc(Psi_z, 1, 2))}")
    print(f"  Psi (0,3) = {fmt(gc(Psi_z, 0, 3))}")
    print(f"  Psi (4,1) = {fmt(gc(Psi_z, 4, 1))}")
    print(f"  Psi (3,2) = {fmt(gc(Psi_z, 3, 2))}")
    print(f"  Psi (0,5) = {fmt(gc(Psi_z, 0, 5))}")

if __name__ == "__main__":
    main()