#!/usr/bin/env python3
"""
Genesis II exact K4 / tetrahedral-shadow route census
=====================================================

Purpose
-------
Exact SymPy engine for the smooth Genesis primitive six-step cubic return:

    G3(Z) = sum_{j=0}^5 L^(5-j) F3(L^j Z)
          + sum_{0<=k<j<=5} L^(5-j) DF2(L^j Z) L^(j-1-k) F2(L^k Z)

It supports:
  1. standalone T3 triad check;
  2. embedded K4 tetrahedral-shadow ΔQ_c^(4) census;
  3. K4 vector apex seeding G_{3,d}(s,c,0) channel extraction;
  4. K4 shadow ΔQ_s^(4) cross-check.

Layer warning
-------------
This is primitive smooth Genesis algebra. It is not TDR-G, not a dyadic normal-form
script, and not an observable-layer simulation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Iterable, Sequence

import sympy as sp

R = sp.Rational

# -----------------------------------------------------------------------------
# Primitive dyad jets and invariants
# -----------------------------------------------------------------------------

B = sp.Matrix([[1, R(-1, 2)], [R(-1, 2), 1]])
A = sp.Matrix([[1, -1], [1, 0]])


def N2_pair(x: sp.Matrix) -> sp.Matrix:
    """Quadratic primitive dyad jet N2(r) = (0, rho^2/2)."""
    rho, _eta = x
    return sp.Matrix([0, rho**2 / 2])


def N3_pair(x: sp.Matrix) -> sp.Matrix:
    """Cubic primitive dyad jet N3(r) = (eta^3/6, (rho^3+eta^3)/6)."""
    rho, eta = x
    return sp.Matrix([eta**3 / 6, (rho**3 + eta**3) / 6])


def qform(x: sp.Matrix) -> sp.Expr:
    return sp.expand((x.T * B * x)[0])


def inner_B(x: sp.Matrix, y: sp.Matrix) -> sp.Expr:
    return sp.expand((x.T * B * y)[0])


def omega(x: sp.Matrix, y: sp.Matrix) -> sp.Expr:
    # omega_ab = a_eta b_rho - a_rho b_eta
    return sp.expand(x[1] * y[0] - x[0] * y[1])


def clean_factor(expr: sp.Expr) -> sp.Expr:
    return sp.factor(sp.cancel(sp.expand(expr)))


# -----------------------------------------------------------------------------
# Route engine
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class ModeSystem:
    name: str
    E: sp.Matrix
    projection_factors: tuple[sp.Rational, ...]
    mode_names: tuple[str, ...]

    @property
    def m(self) -> int:
        return self.E.shape[1]

    @property
    def variables(self) -> sp.Matrix:
        names = []
        for mode in self.mode_names:
            names.extend([f"{mode}_rho", f"{mode}_eta"])
        return sp.Matrix(sp.symbols(" ".join(names)))

    @property
    def L(self) -> sp.Matrix:
        return sp.diag(*([A] * self.m))

    def pair(self, Z: sp.Matrix, mode_index: int) -> sp.Matrix:
        return sp.Matrix([Z[2 * mode_index], Z[2 * mode_index + 1]])

    def mode_vector(self, Z: sp.Matrix, mode_name: str) -> sp.Matrix:
        idx = self.mode_names.index(mode_name)
        return self.pair(Z, idx)

    def project_edge_jets(self, Z: sp.Matrix, jet) -> sp.Matrix:
        """Build F2 or F3 by applying dyad jet on every edge and projecting back."""
        pairs = [self.pair(Z, u) for u in range(self.m)]
        outs = [sp.Matrix([0, 0]) for _ in range(self.m)]

        for e in range(self.E.shape[0]):
            r_edge = sp.Matrix([0, 0])
            for u in range(self.m):
                r_edge += self.E[e, u] * pairs[u]
            n_edge = jet(r_edge)
            for u in range(self.m):
                outs[u] += self.projection_factors[u] * self.E[e, u] * n_edge

        return sp.Matrix([component for out in outs for component in out])

    def F2(self, Z: sp.Matrix) -> sp.Matrix:
        return self.project_edge_jets(Z, N2_pair)

    def F3(self, Z: sp.Matrix) -> sp.Matrix:
        return self.project_edge_jets(Z, N3_pair)

    def G3_split(self) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
        """Return direct, quadratic-composition, and total six-step cubic vector drift."""
        Z = self.variables
        L = self.L
        F2_Z = self.F2(Z)
        JF2_Z = F2_Z.jacobian(Z)

        direct = sp.zeros(2 * self.m, 1)
        comp = sp.zeros(2 * self.m, 1)

        for j in range(6):
            LjZ = (L**j) * Z
            direct += (L ** (5 - j)) * self.F3(LjZ)

        for j in range(6):
            LjZ = (L**j) * Z
            JF2_j = JF2_Z.subs(dict(zip(Z, LjZ)), simultaneous=True)
            for k in range(j):
                LkZ = (L**k) * Z
                comp += (L ** (5 - j)) * JF2_j * (L ** (j - 1 - k)) * self.F2(LkZ)

        total = sp.simplify(direct + comp)
        return sp.simplify(direct), sp.simplify(comp), total

    def delta_Q(self, G: sp.Matrix, mode_name: str, substitutions: dict | None = None) -> sp.Expr:
        Z = self.variables
        idx = self.mode_names.index(mode_name)
        x = self.pair(Z, idx)
        gx = sp.Matrix([G[2 * idx], G[2 * idx + 1]])
        expr = sp.expand(2 * (x.T * B * gx)[0])
        if substitutions:
            expr = expr.subs(substitutions)
        return sp.expand(expr)


def standalone_triad_system() -> ModeSystem:
    # r_AB=s, r_BC=-s/2+c, r_CA=-s/2-c
    E = sp.Matrix([
        [1, 0],
        [R(-1, 2), 1],
        [R(-1, 2), -1],
    ])
    # E.T E = diag(3/2, 2)
    return ModeSystem(
        name="standalone_T3",
        E=E,
        projection_factors=(R(2, 3), R(1, 2)),
        mode_names=("s", "c"),
    )


def tetrahedral_k4_system() -> ModeSystem:
    # Edge order: AB, BC, CA, AD, BD, CD
    E = sp.Matrix([
        [1, 0, 0],
        [R(-1, 2), 1, 0],
        [R(-1, 2), -1, 0],
        [R(1, 2), R(1, 3), 1],
        [R(-1, 2), R(1, 3), 1],
        [0, R(-2, 3), 1],
    ])
    # E.T E = diag(2, 8/3, 3)
    return ModeSystem(
        name="tetrahedral_K4_shadow",
        E=E,
        projection_factors=(R(1, 2), R(3, 8), R(1, 3)),
        mode_names=("s", "c", "d"),
    )


# -----------------------------------------------------------------------------
# Formula checks
# -----------------------------------------------------------------------------

def invariant_symbols_for_sc(system: ModeSystem):
    Z = system.variables
    s = system.mode_vector(Z, "s")
    c = system.mode_vector(Z, "c")
    return s, c, qform(s), qform(c), inner_B(s, c), omega(s, c)


def verify_standalone(verbose: bool = True) -> bool:
    sys = standalone_triad_system()
    _direct, _comp, total = sys.G3_split()
    s, c, Qs, Qc, Isc, wsc = invariant_symbols_for_sc(sys)

    delta = sys.delta_Q(total, "c")
    expected = sp.expand(R(1, 3) * Qc**2 + R(1, 4) * (Isc + wsc) ** 2 + R(5, 16) * wsc**2)
    ok = clean_factor(delta - expected) == 0

    if verbose:
        print("\n[standalone T3] ΔQ_c^(4)")
        print("  expected = 1/3 Qc^2 + 1/4 (Isc+wsc)^2 + 5/16 wsc^2")
        print(f"  verification: {'PASS' if ok else 'FAIL'}")
    return ok


def verify_shadow(verbose: bool = True) -> bool:
    sys = tetrahedral_k4_system()
    direct, comp, total = sys.G3_split()
    Z = sys.variables
    s, c, Qs, Qc, Isc, wsc = invariant_symbols_for_sc(sys)
    zero_d = {Z[4]: 0, Z[5]: 0}

    delta_dir = sys.delta_Q(direct, "c", zero_d)
    delta_comp = sys.delta_Q(comp, "c", zero_d)
    delta = sp.expand(delta_dir + delta_comp)

    expected_dir = sp.expand(
        R(5, 6) * Qc**2
        + R(5, 8) * Isc**2
        + R(5, 24) * Isc * wsc
        + R(5, 32) * wsc**2
    )
    expected_comp = sp.expand(
        -R(1, 2) * Qc**2
        - R(3, 8) * Isc**2
        + R(3, 16) * Isc * wsc
        + R(5, 32) * wsc**2
    )
    expected = sp.expand(
        R(1, 3) * Qc**2
        + R(1, 4) * Isc**2
        + R(19, 48) * Isc * wsc
        + R(5, 16) * wsc**2
    )
    expected_square = sp.expand(
        R(1, 3) * Qc**2
        + R(1, 4) * (Isc + R(19, 24) * wsc) ** 2
        + R(359, 2304) * wsc**2
    )

    ok_dir = clean_factor(delta_dir - expected_dir) == 0
    ok_comp = clean_factor(delta_comp - expected_comp) == 0
    ok_net = clean_factor(delta - expected) == 0
    ok_square = clean_factor(expected - expected_square) == 0

    if verbose:
        print("\n[K4 shadow] ΔQ_c^(4)")
        print("  direct expected = 5/6 Qc^2 + 5/8 Isc^2 + 5/24 Isc*wsc + 5/32 wsc^2")
        print(f"  direct verification: {'PASS' if ok_dir else 'FAIL'}")
        print("  comp expected   = -1/2 Qc^2 - 3/8 Isc^2 + 3/16 Isc*wsc + 5/32 wsc^2")
        print(f"  comp verification:   {'PASS' if ok_comp else 'FAIL'}")
        print("  net expected    = 1/3 Qc^2 + 1/4 Isc^2 + 19/48 Isc*wsc + 5/16 wsc^2")
        print(f"  net verification:    {'PASS' if ok_net else 'FAIL'}")
        print("  square form     = 1/3 Qc^2 + 1/4(Isc+19/24 wsc)^2 + 359/2304 wsc^2")
        print(f"  square check:        {'PASS' if ok_square else 'FAIL'}")

    return ok_dir and ok_comp and ok_net and ok_square


def verify_shadow_Qs(verbose: bool = True) -> bool:
    """Check one Pluecker gauge for K4 shadow ΔQ_s at d=0."""
    sys = tetrahedral_k4_system()
    _direct, _comp, total = sys.G3_split()
    Z = sys.variables
    _s, _c, Qs, Qc, Isc, wsc = invariant_symbols_for_sc(sys)
    zero_d = {Z[4]: 0, Z[5]: 0}

    delta = sys.delta_Q(total, "s", zero_d)
    expected = sp.expand(
        R(1, 4) * Qs**2
        + R(5, 9) * Qs * Qc
        - R(2, 9) * Isc**2
        - R(19, 36) * Isc * wsc
    )
    ok = clean_factor(delta - expected) == 0
    if verbose:
        print("\n[K4 shadow] ΔQ_s^(4), one Pluecker gauge")
        print("  expected = 1/4 Qs^2 + 5/9 Qs*Qc - 2/9 Isc^2 - 19/36 Isc*wsc")
        print(f"  verification: {'PASS' if ok else 'FAIL'}")
    return ok


def channel_extract(vec: sp.Matrix, variables: Sequence[sp.Symbol], s_power: int, c_power: int) -> sp.Matrix:
    sr, se, cr, ce = variables[:4]
    ts, tc = sp.symbols("ts tc")
    scaled = {sr: ts * sr, se: ts * se, cr: tc * cr, ce: tc * ce}
    out = []
    for component in vec:
        poly = sp.Poly(sp.expand(component.subs(scaled)), ts, tc)
        out.append(sp.expand(poly.coeff_monomial(ts**s_power * tc**c_power)))
    return sp.Matrix(out)


def verify_G3d_seed(verbose: bool = True) -> bool:
    sys = tetrahedral_k4_system()
    _direct, _comp, total = sys.G3_split()
    Z = sys.variables
    zero_d = {Z[4]: 0, Z[5]: 0}
    G0 = sp.Matrix([sp.expand(x.subs(zero_d)) for x in total])
    Gd = sp.Matrix([G0[4], G0[5]])
    s = sys.mode_vector(Z, "s")
    c = sys.mode_vector(Z, "c")
    Qs = qform(s)
    Qc = qform(c)

    channels = {
        "s3": channel_extract(Gd, Z, 3, 0),
        "s2c": channel_extract(Gd, Z, 2, 1),
        "sc2": channel_extract(Gd, Z, 1, 2),
        "c3": channel_extract(Gd, Z, 0, 3),
    }

    expected_s3 = sp.Matrix([
        Qs * (2 * Z[1] - 3 * Z[0]) / 32,
        -Qs * (Z[1] + 2 * Z[0]) / 32,
    ])
    expected_c3 = sp.Matrix([
        Qc * (Z[2] - 14 * Z[3]) / 324,
        Qc * (14 * Z[2] - 13 * Z[3]) / 324,
    ])
    expected_s2c = sp.Matrix([
        (
            14 * Z[3] * Z[1] ** 2
            - 10 * Z[3] * Z[1] * Z[0]
            + 5 * Z[3] * Z[0] ** 2
            - 5 * Z[2] * Z[1] ** 2
            + 10 * Z[2] * Z[1] * Z[0]
            - Z[2] * Z[0] ** 2
        ) / 144,
        (
            13 * Z[3] * Z[1] ** 2
            - 18 * Z[3] * Z[1] * Z[0]
            + 9 * Z[3] * Z[0] ** 2
            - 9 * Z[2] * Z[1] ** 2
            + 18 * Z[2] * Z[1] * Z[0]
            - 14 * Z[2] * Z[0] ** 2
        ) / 144,
    ])
    expected_sc2 = sp.Matrix([
        -(
            6 * Z[3] ** 2 * Z[1]
            - 5 * Z[3] ** 2 * Z[0]
            - 10 * Z[3] * Z[2] * Z[1]
            + 10 * Z[3] * Z[2] * Z[0]
            + 5 * Z[2] ** 2 * Z[1]
            - 9 * Z[2] ** 2 * Z[0]
        ) / 24,
        (
            3 * Z[3] ** 2 * Z[1]
            + Z[3] ** 2 * Z[0]
            + 2 * Z[3] * Z[2] * Z[1]
            - 2 * Z[3] * Z[2] * Z[0]
            - Z[2] ** 2 * Z[1]
            + 6 * Z[2] ** 2 * Z[0]
        ) / 24,
    ])

    expected = {
        "s3": expected_s3,
        "s2c": expected_s2c,
        "sc2": expected_sc2,
        "c3": expected_c3,
    }
    checks = {
        key: all(clean_factor(channels[key][i] - expected[key][i]) == 0 for i in range(2))
        for key in channels
    }

    qd1_s3 = clean_factor((channels["s3"].T * B * channels["s3"])[0])
    qd1_ok = clean_factor(qd1_s3 - R(7, 1024) * Qs**3) == 0

    if verbose:
        print("\n[K4 shadow] vector apex seeding G_{3,d}(s,c,0)")
        for key in ("s3", "s2c", "sc2", "c3"):
            print(f"  {key:4s}: ({sp.factor(channels[key][0])}, {sp.factor(channels[key][1])})")
            print(f"        verification: {'PASS' if checks[key] else 'FAIL'}")
        print("  Qd1[s3] expected = 7/1024 Qs^3")
        print(f"  Qd1[s3] verification: {'PASS' if qd1_ok else 'FAIL'}")

    return all(checks.values()) and qd1_ok



def verify_pure_d_checksum(verbose: bool = True) -> bool:
    """Check pure-d axis: direct +Qd^2, composition -2Qd^2, total -Qd^2."""
    sys = tetrahedral_k4_system()
    direct, comp, total = sys.G3_split()
    Z = sys.variables
    zero_sc = {Z[0]: 0, Z[1]: 0, Z[2]: 0, Z[3]: 0}
    d = sys.mode_vector(Z, "d")
    Qd = qform(d)
    dq_dir = sys.delta_Q(direct, "d", zero_sc)
    dq_comp = sys.delta_Q(comp, "d", zero_sc)
    dq_total = sys.delta_Q(total, "d", zero_sc)
    ok_dir = clean_factor(dq_dir - Qd**2) == 0
    ok_comp = clean_factor(dq_comp + 2 * Qd**2) == 0
    ok_total = clean_factor(dq_total + Qd**2) == 0
    if verbose:
        print("\n[K4] pure-d checksum")
        print("  direct expected = +Qd^2")
        print(f"  direct verification: {'PASS' if ok_dir else 'FAIL'}")
        print("  comp expected   = -2 Qd^2")
        print(f"  comp verification:   {'PASS' if ok_comp else 'FAIL'}")
        print("  total expected  = -Qd^2")
        print(f"  total verification:  {'PASS' if ok_total else 'FAIL'}")
    return ok_dir and ok_comp and ok_total


def main() -> None:
    parser = argparse.ArgumentParser(description="Genesis II exact K4 route-census checks")
    parser.add_argument(
        "--case",
        choices=["all", "standalone", "shadow", "qs", "g3d", "checksum"],
        default="all",
        help="which verification block to run",
    )
    args = parser.parse_args()

    checks: list[bool] = []
    if args.case in ("all", "checksum"):
        checks.append(verify_pure_d_checksum())
    if args.case in ("all", "standalone"):
        checks.append(verify_standalone())
    if args.case in ("all", "shadow"):
        checks.append(verify_shadow())
    if args.case in ("all", "qs"):
        checks.append(verify_shadow_Qs())
    if args.case in ("all", "g3d"):
        checks.append(verify_G3d_seed())

    print("\nSummary")
    print("-------")
    print("PASS" if all(checks) else "FAIL")


if __name__ == "__main__":
    main()
