# normalize_pstep_lie.py
#
# Tangent-to-identity Lie/log normalizer for raw p-step RTG maps.
#
# INPUT:
#   A raw p-step jet in JSON form, e.g. jet6_deg5.json
#
# MODEL:
#   F(Z, Zb) = Z + U(Z, Zb),  where U starts at degree >= 2
#
# We compute a truncated Lie-log vector field V such that
#   exp(V) ~= F
# through degree <= 5.
#
# Then we apply a simple gauge-fixing step at the vector-field level:
#   - keep selected monomials
#   - optionally kill selected monomials
#
# Finally we re-exponentiate approximately to obtain a gauge-fixed
# tangent-to-identity normalized p-step map.
#
# IMPORTANT:
# - This script does NOT assume Phi_p = Id.
# - This is a gauge-fixed normalizer, not a proof of uniqueness.
# - The default p=6 keep/kill sets are chosen to preserve (3,2) and (0,5)
#   while eliminating other degree-5 channels in the Z-component.
#
# Usage:
#   python .\normalize_pstep_lie.py --input outputs/jet6_deg5.json --p 6
#   python .\normalize_pstep_lie.py --input outputs/jet6_deg5.json --p 6 --json-out outputs/p6_lie_normalized.json
#
# Optional:
#   python .\normalize_pstep_lie.py --input outputs/jet5_deg5.json --p 5
#
# Notes:
# - JSON coefficients should be SymPy-readable strings, as in your existing jet files.
# - The script uses direct substitution-style operator composition, not the
#   semisimple 1-step resonance-denominator solver.
#
# Author intent:
#   DSN-safe exploratory normalization for tangent-to-identity p-step maps.

from __future__ import annotations
import argparse
import json
import sympy as sp
import mpmath as mp

mp.mp.dps = 80
TOL = mp.mpf("1e-60")

# -----------------------------------------------------------------------------
# Basic polynomial dictionary algebra
# -----------------------------------------------------------------------------

def poly_to_jsonable(P):
    return {str(k): str(v) for k, v in sorted(P.items())}

def clean(P):
    return {k: v for k, v in P.items() if abs(v) > TOL}

def add(A, B):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, mp.mpc(0)) + v
    return clean(out)

def scale(A, c):
    return clean({k: c * v for k, v in A.items()})

def sub(A, B):
    return add(A, scale(B, -1))

def mul(A, B, d):
    out = {}
    for (a1, b1), c1 in A.items():
        for (a2, b2), c2 in B.items():
            if a1 + a2 + b1 + b2 <= d:
                m = (a1 + a2, b1 + b2)
                out[m] = out.get(m, mp.mpc(0)) + c1 * c2
    return clean(out)

def pw(A, n, d):
    if n == 0:
        return {(0, 0): mp.mpc(1)}
    out = {(0, 0): mp.mpc(1)}
    for _ in range(n):
        out = mul(out, A, d)
    return out

def compose_scalar(F, X, Y, d):
    """
    Substitute X,Y into scalar polynomial F.
    """
    out = {}
    for (a, b), c in F.items():
        if a + b > d:
            continue
        term = mul(pw(X, a, d), pw(Y, b, d), d)
        term = scale(term, c)
        out = add(out, term)
    return clean(out)

def compose_pair(Fz, Fzb, X, Y, d):
    return compose_scalar(Fz, X, Y, d), compose_scalar(Fzb, X, Y, d)

def conj_poly(P):
    return clean({(b, a): mp.conj(v) for (a, b), v in P.items()})

def gc(P, a, b):
    return P.get((a, b), mp.mpc(0))

def poly_var_Z():
    return {(1, 0): mp.mpc(1)}

def poly_var_Zb():
    return {(0, 1): mp.mpc(1)}

def identity_pair():
    return poly_var_Z(), poly_var_Zb()

def degree_slice(P, k):
    return {m: c for m, c in P.items() if m[0] + m[1] == k}

def remove_linear(P):
    Q = dict(P)
    if (1, 0) in Q:
        Q[(1, 0)] -= 1
    return clean(Q)

def fmt(z):
    return mp.nstr(z, 30)

# -----------------------------------------------------------------------------
# SymPy -> mpmath loader
# -----------------------------------------------------------------------------
def sympy_to_mpc(expr, dps=80):
    z = sp.N(sp.expand(expr), dps)
    re, im = z.as_real_imag()
    return mp.mpc(str(re), str(im))

def load_jet(path, max_deg=5):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    Fz = {}
    for k_str, v_str in data.items():
        a, b = eval(k_str)
        if a + b <= max_deg:
            expr = sp.sympify(v_str)
            Fz[(a, b)] = sympy_to_mpc(expr, 80)
    Fz = clean(Fz)
    Fzb = conj_poly(Fz)
    return Fz, Fzb

# -----------------------------------------------------------------------------
# Vector field actions
# -----------------------------------------------------------------------------
def dz_poly(P):
    out = {}
    for (a, b), c in P.items():
        if a >= 1:
            out[(a - 1, b)] = out.get((a - 1, b), mp.mpc(0)) + c * a
    return clean(out)

def dzb_poly(P):
    out = {}
    for (a, b), c in P.items():
        if b >= 1:
            out[(a, b - 1)] = out.get((a, b - 1), mp.mpc(0)) + c * b
    return clean(out)

def apply_vector_field_to_scalar(Vz, Vzb, P, d):
    """
    V(P) = P_Z * Vz + P_Zb * Vzb
    """
    term1 = mul(dz_poly(P), Vz, d)
    term2 = mul(dzb_poly(P), Vzb, d)
    return add(term1, term2)

def apply_vector_field_to_pair(Vz, Vzb, X, Y, d):
    return (
        apply_vector_field_to_scalar(Vz, Vzb, X, d),
        apply_vector_field_to_scalar(Vz, Vzb, Y, d),
    )

# -----------------------------------------------------------------------------
# Formal exp/log for tangent-to-identity maps
# -----------------------------------------------------------------------------
def map_delta(Fz):
    """
    U = F - Id
    """
    Z = poly_var_Z()
    return sub(Fz, Z)

def compose_delta(Ua, Ub, d):
    """
    Treat Ua,Ub as tangent maps: Ta = Id + Ua, Tb = Id + Ub
    Return U_ab such that (Id+Ua) o (Id+Ub) = Id + U_ab
    """
    Z = poly_var_Z()
    Zb = poly_var_Zb()
    Ta_z = add(Z, Ua)
    Ta_zb = add(Zb, conj_poly(Ua))
    Tb_z = add(Z, Ub)
    Tb_zb = add(Zb, conj_poly(Ub))

    Tab_z, _ = compose_pair(Ta_z, Ta_zb, Tb_z, Tb_zb, d)
    return sub(Tab_z, Z)

def operator_apply_U(U, P, d):
    """
    Delta_U(P) = P(Id+U) - P
    where U is tangent part of map (scalar Z-component), and conjugate is used for Zb.
    """
    Z = poly_var_Z()
    Zb = poly_var_Zb()
    X = add(Z, U)
    Y = add(Zb, conj_poly(U))
    return sub(compose_scalar(P, X, Y, d), P)

def log_map_from_raw(Fz, d=5):
    """
    Compute truncated formal log V = log(F) as vector field pair (Vz, Vzb).
    Approximation strategy:
      Let U = F - Id.
      Compute V degree-by-degree using:
        V2 = U2
        V3 = U3
        V4 = U4 - 1/2 * V2(V2 on coords)
        V5 = U5 - [V2,V3] contribution - 1/2 * V3(V2 on coords) - ...
    For current RTG use, U2 is usually zero in the p-step jets, so the dominant exact relation is:
        V3 = U3
        V4 = U4
        V5 = U5 - 1/2 * V3^2(coords)
    which is the same conceptual correction already discussed in notes.
    """
    Z = poly_var_Z()
    Zb = poly_var_Zb()

    U = map_delta(Fz)
    U2 = degree_slice(U, 2)
    U3 = degree_slice(U, 3)
    U4 = degree_slice(U, 4)
    U5 = degree_slice(U, 5)

    # Degree 2, 3, 4
    V2 = U2
    V3 = U3
    V4 = U4

    # Compute V3^2 acting on coordinates
    V3z, V3zb = V3, conj_poly(V3)
    V3_on_Z, _ = apply_vector_field_to_pair(V3z, V3zb, Z, Zb, d)
    V3sq_on_Z, _ = apply_vector_field_to_pair(V3z, V3zb, V3_on_Z, spoly_zero(), d)

    # But V3_on_Z = V3 itself, so V3^2(Z) = V3(V3)
    V3sq_on_Z = apply_vector_field_to_scalar(V3z, V3zb, V3, d)

    V5 = sub(U5, scale(degree_slice(V3sq_on_Z, 5), mp.mpf("1/2")))

    Vz = add(add(V2, V3), add(V4, V5))
    Vzb = conj_poly(Vz)
    return clean(Vz), clean(Vzb)

def exp_vector_field_to_map(Vz, Vzb, d=5):
    """
    Compute truncated exp(V)(Z):
      Z' = Z + V(Z) + 1/2 V^2(Z) + 1/6 V^3(Z) + ...
    Through degree 5, only finitely many terms matter.
    """
    Z = poly_var_Z()
    Zb = poly_var_Zb()

    term1 = Vz
    term2 = apply_vector_field_to_scalar(Vz, Vzb, Vz, d)
    term3 = apply_vector_field_to_scalar(Vz, Vzb, term2, d)

    Fz = add(Z, term1)
    Fz = add(Fz, scale(term2, mp.mpf("1/2")))
    Fz = add(Fz, scale(term3, mp.mpf("1/6")))
    return clean(Fz), conj_poly(clean(Fz))

# -----------------------------------------------------------------------------
# Gauge projection
# -----------------------------------------------------------------------------
def default_keep_set(p):
    return {(2,1), (3,2), (0, p - 1)}

def project_vector_field(Vz, p, keep_set=None):
    """
    Keep only selected monomials in Vz.
    Default keep set:
      degree 3: (2,1)
      degree 5: (3,2), (0,p-1)
    """
    if keep_set is None:
        keep_set = default_keep_set(p)
    out = {}
    for m, c in Vz.items():
        if m in keep_set:
            out[m] = c
    return clean(out), conj_poly(clean(out))

# -----------------------------------------------------------------------------
# tiny helper
# -----------------------------------------------------------------------------
def spoly_zero():
    return {}

# -----------------------------------------------------------------------------
# Reporting
# -----------------------------------------------------------------------------
def print_degree_block(P, title, monos):
    print(f"\n{title}")
    for m in monos:
        print(f"  {m}: {fmt(gc(P, *m))}")

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Lie/log-based tangent-to-identity normalizer for raw p-step jets.")
    parser.add_argument("--input", type=str, required=True, help="Path to raw p-step JSON jet, e.g. outputs/jet6_deg5.json")
    parser.add_argument("--p", type=int, required=True, help="Resonance order p, e.g. 6")
    parser.add_argument("--json-out", type=str, default=None, help="Optional JSON output path")
    args = parser.parse_args()

    print("LIE / LOG NORMALIZER FOR RAW p-STEP MAP")
    print(f"dps = {mp.mp.dps}")
    print(f"input = {args.input}")
    print(f"p = {args.p}")

    Fz, Fzb = load_jet(args.input, max_deg=5)

    print(f"\nLoaded raw p-step jet.")
    print(f"  linear (1,0) = {fmt(gc(Fz,1,0))}")
    print(f"  cubic  (2,1) = {fmt(gc(Fz,2,1))}")
    print(f"  quintic(3,2) = {fmt(gc(Fz,3,2))}")
    print(f"  quintic(0,{args.p-1}) = {fmt(gc(Fz,0,args.p-1))}")

    raw_deg5 = [(5,0),(4,1),(3,2),(2,3),(1,4),(0,args.p-1)]
    print_degree_block(Fz, "Raw degree-5 monomials", raw_deg5)

    # Lie log
    Vz, Vzb = log_map_from_raw(Fz, d=5)
    print_degree_block(Vz, "Lie-log vector field V degree-3/4/5 monomials",
                       [(2,1),(3,0),(1,2),(0,3),(4,0),(3,1),(2,2),(1,3),(0,4),(5,0),(4,1),(3,2),(2,3),(1,4),(0,args.p-1)])

    # Gauge projection at vector-field level
    NVz, NVzb = project_vector_field(Vz, args.p)
    print_degree_block(NVz, "Projected / gauge-fixed vector field NV",
                       [(2,1),(3,2),(0,args.p-1)])


    G3 = degree_slice(NVz, 3)
    G4 = degree_slice(NVz, 4)
    G5 = degree_slice(NVz, 5)

    export_gen = {
        "metadata": {
            "type": "lie_gauge_generator",
            "source": "normalize_pstep_lie",
            "frame": "Z6",
            "order": 5,
            "map_meaning": "Phi6 = exp(G), with G = G3 + G4 + G5"
        },
        "G3": poly_to_jsonable(G3),
        "G4": poly_to_jsonable(G4),
        "G5": poly_to_jsonable(G5),
    }

    with open("outputs/phi6_p6_lie_generator.json", "w", encoding="utf-8") as f:
        json.dump(export_gen, f, indent=2)

    print("\nExported Lie generator to outputs/phi6_p6_lie_generator.json")




    # Re-exponentiate
    Gz, Gzb = exp_vector_field_to_map(NVz, NVzb, d=5)
    print_degree_block(Gz, "Gauge-fixed normalized p-step map degree-5 monomials", raw_deg5)

    # Targets
    nu3 = gc(Gz, 2, 1)
    nu5 = gc(Gz, 3, 2)
    clat = gc(Gz, 0, args.p - 1)

    print("\nRetained coefficients in this Lie gauge:")
    print(f"  nu3^(p-step,norm,gauge) = {fmt(nu3)}")
    print(f"  nu5^(p-step,norm,gauge) = {fmt(nu5)}")
    print(f"  c0,{args.p-1}^(p-step,norm,gauge) = {fmt(clat)}")

    if args.json_out:
        out = {
            "raw_degree5": {str(m): str(gc(Fz, *m)) for m in raw_deg5},
            "lie_log": {str(m): str(c) for m, c in sorted(Vz.items())},
            "projected_vector_field": {str(m): str(c) for m, c in sorted(NVz.items())},
            "normalized_degree5": {str(m): str(gc(Gz, *m)) for m in raw_deg5},
            "nu3_norm_gauge": str(nu3),
            "nu5_norm_gauge": str(nu5),
            f"c0{args.p-1}_norm_gauge": str(clat),
        }
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
        print(f"\nWrote JSON report to {args.json_out}")

if __name__ == "__main__":
    main()