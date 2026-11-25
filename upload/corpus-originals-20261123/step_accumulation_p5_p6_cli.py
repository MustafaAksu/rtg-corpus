# step_accumulation_p5_p6_cli.py
#
# RTG step-accumulation tool for p=5 / p=6 strong resonances
#
# Starting from a normalized 1-step map
#     Z' = lam*Z + A*Z^2*Zb + B*Zb^(p-1) + C*Z^3*Zb^2 + O(|Z|^6)
# iterate p times with strict degree-5 truncation and extract the p-step coefficients.
#
# ---------------------------------------------------------------------------
# INTERPRETATION NOTES
# ---------------------------------------------------------------------------
#
# For p=5:
#   This script computes the p-step map of the normalized 1-step model and is
#   used in the standard decomposition analysis.
#
# For p=6:
#   This script computes
#       F1^6 = (Phi1^{-1} o f o Phi1)^6 = Phi1^{-1} o f^6 o Phi1
#
#   This is NOT the same object as:
#       (a) the raw 6-step primitive-map coefficient from jet6_deg5.json
#       (b) the normalized 6-step map Phi6^{-1} o f^6 o Phi6
#
#   Therefore any p=6 comparison to the raw 6-step coefficient is DIAGNOSTIC ONLY.
#   It must not be labeled as a failure of the 1-step candidate.
#
# ---------------------------------------------------------------------------
# DEGREE-5 QUINTIC DECOMPOSITION
# ---------------------------------------------------------------------------
#
#   Part A: direct nu5 transport         (only C active)
#   Part B: cubic self-interaction       (only A active)
#   Part C: lattice self-contribution    (only B active)   -> [THM] = 0
#   Part D: cubic x lattice cross term   (A+B, minus singles) -> [THM] = 0
#
# [THM] C=D=0 for all p>=5:
#   The lattice harmonic monomial (0,p-1) has charge -(p-1) = 1 mod p.
#   Any product contributing to (3,2) [charge +1] from lattice terms would
#   require total degree >= 2(p-1) > 5 for p>=5, hence is truncated out.
#
# ---------------------------------------------------------------------------
# EXAMPLE USAGE
# ---------------------------------------------------------------------------
#
#   python .\step_accumulation_p5_p6_cli.py --case p6 --p6-mode solver --show-gap
#   python .\step_accumulation_p5_p6_cli.py --case p6 --p6-mode fail --show-gap
#   python .\step_accumulation_p5_p6_cli.py --case p6 --p6-mode manual --c6-re="-5/432" --c6-im="23*sqrt(3)/3888" --show-gap
#   python .\step_accumulation_p5_p6_cli.py --case all --p6-mode solver --show-gap

from __future__ import annotations
import argparse
import mpmath as mp

mp.mp.dps = 80

# -----------------------------------------------------------------------------
# Polynomial dictionary algebra
# -----------------------------------------------------------------------------
TOL = mp.mpf("1e-60")

def clean(P):
    return {k: v for k, v in P.items() if abs(v) > TOL}

def add(A, B):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, mp.mpc(0)) + v
    return clean(out)

def scale(A, c):
    return clean({k: c * v for k, v in A.items()})

def mul(A, B, d):
    out = {}
    for (a1, b1), c1 in A.items():
        for (a2, b2), c2 in B.items():
            if a1 + b1 + a2 + b2 <= d:
                m = (a1 + a2, b1 + b2)
                out[m] = out.get(m, mp.mpc(0)) + c1 * c2
    return clean(out)

def pw(A, n, d):
    r = {(0, 0): mp.mpc(1)}
    for _ in range(n):
        r = mul(r, A, d)
    return r

def compose(F, X, Y, d):
    out = {}
    for (a, b), c in F.items():
        if a + b > d:
            continue
        t = mul(pw(X, a, d), pw(Y, b, d), d)
        for k, v in t.items():
            out[k] = out.get(k, mp.mpc(0)) + c * v
    return clean(out)

def conj(P):
    return clean({(b, a): mp.conj(v) for (a, b), v in P.items()})

def gc(P, a, b):
    return P.get((a, b), mp.mpc(0))

def iterate(F1, p, d=5):
    X = {(1, 0): mp.mpc(1)}
    Y = conj(X)
    for _ in range(p):
        X = compose(F1, X, Y, d)
        Y = conj(X)
    return X

def make_map(lam, A, B, lat_mono, C):
    F = {(1, 0): lam, (2, 1): A, (3, 2): C}
    if abs(B) > TOL:
        F[lat_mono] = B
    return clean(F)

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
sqrt3 = mp.sqrt(3)
sqrt5 = mp.sqrt(5)
s5 = mp.sqrt(10 + 2 * sqrt5)

lam5 = (sqrt5 - 1) / 4 + mp.mpc(0, 1) * s5 / 4
lam6 = mp.mpf(1) / 2 + mp.mpc(0, 1) * sqrt3 / 2

# p=5 coefficients
A5 = mp.mpc(
    "0.23277907312568348667018557662335223481799033126254139611958395241580699167713407",
    "-0.26739234457824515096807846242737210017518938407978140370696205233237020851760005",
)
B5 = mp.mpc(
    "-0.037426135365069660387119224392257038876903376731680095956883453321503692795909503",
    "0.00173404207910558568624968131202021248581561942046405644041635292124959908498528",
)
C5 = mp.mpc(
    "-0.011141842134720036022054444339019196563714982879845628314013792089017232841895394",
    "0.0072266912896357198337502443344645085347632680615315138666592915900501117219177621",
)
c21_5_exact = (75 * sqrt5 - 175) / 8 + mp.mpc(0, 1) * (50 * sqrt5 - 115) * s5 / 8

# p=6 constants
c21_6_exact = mp.mpf(-1) / 2 - mp.mpc(0, 1) * 2 * sqrt3 / 3
A6 = mp.mpf(1) / 8 - mp.mpc(0, 1) * 7 * sqrt3 / 72

# legacy p=6 sub-team candidate
B6_legacy = mp.mpf(43) / 17280 - mp.mpc(0, 1) * 227 * sqrt3 / 155520
C6_fail = mp.mpf(-7) / 108 - mp.mpc(0, 1) * 121 * sqrt3 / 3888

# solver-derived p=6 candidates
B6_solver = (
    mp.mpf("0.0024884259259259259259259259259259259259259259259259259259259259259259259259259258")
    - mp.mpc(0, 1) * mp.mpf("0.0025281348592987084981399840504233090746914660018965818066400989219109361808018109")
)
C6_solver = mp.mpf(-5) / 432 + mp.mpc(0, 1) * 23 * sqrt3 / 3888

# raw uploaded 6-step p=6 coefficient from jet6_deg5.json
RAW_P6_C32_6STEP = mp.mpf(-77) / 216 + mp.mpc(0, 1) * 97 * sqrt3 / 648

# exact cubic self-interaction at p=6
P6_CUBIC_SELF = mp.mpf(-35) / 144 + mp.mpc(0, 1) * 5 * sqrt3 / 9

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def parse_real_expr(s: str) -> mp.mpf:
    expr = s.replace("^", "**").replace("sqrt(3)", f"({mp.nstr(sqrt3, 80)})")
    return mp.mpf(str(eval(expr, {"__builtins__": {}}, {})))

def fmt(z) -> str:
    return mp.nstr(z, 30)

def pct(part: mp.mpf, total: mp.mpf) -> float:
    if abs(total) < TOL:
        return 0.0
    return float(100 * part / total)

# -----------------------------------------------------------------------------
# Core decomposition
# -----------------------------------------------------------------------------
def decompose(
    *,
    label,
    p,
    lam,
    A,
    B,
    lat_mono,
    C,
    cubic_exact=None,
    raw_6step_target=None,
    show_gap=False,
):
    sep = "=" * 72
    print(f"\n{sep}")
    print(f"  p={p}   {label}")
    print(f"{sep}")

    # full run
    Fp = iterate(make_map(lam, A, B, lat_mono, C), p)
    c_cubic = gc(Fp, 2, 1)
    c_quintic = gc(Fp, 3, 2)
    c_lat_ps = gc(Fp, lat_mono[0], lat_mono[1])

    # direct nu5 only
    Fp_C = iterate(make_map(lam, mp.mpc(0), mp.mpc(0), lat_mono, C), p)
    q_direct_nu5 = gc(Fp_C, 3, 2)

    # cubic self only
    Fp_A = iterate(make_map(lam, A, mp.mpc(0), lat_mono, mp.mpc(0)), p)
    q_cubic_self = gc(Fp_A, 3, 2)

    # lattice self only
    Fp_B = iterate(make_map(lam, mp.mpc(0), B, lat_mono, mp.mpc(0)), p)
    q_lattice_self = gc(Fp_B, 3, 2)

    # A+B cross
    Fp_AB = iterate(make_map(lam, A, B, lat_mono, mp.mpc(0)), p)
    q_cubic_lattice_cross = gc(Fp_AB, 3, 2) - q_cubic_self - q_lattice_self

    # reconstruction
    q_recon = q_direct_nu5 + q_cubic_self + q_lattice_self + q_cubic_lattice_cross
    err_recon = abs(q_recon - c_quintic)

    # cubic check
    cubic_formula = p * (lam ** (p - 1)) * A
    err_cubic = abs(c_cubic - cubic_formula)

    # direct nu5 check
    nu5_formula = p * (lam ** (p - 1)) * C
    err_nu5 = abs(q_direct_nu5 - nu5_formula)

    print(f"\n  Lattice harmonic {lat_mono} (p-step): {fmt(c_lat_ps)}")
    print(f"  Quintic (3,2)   (p-step): {fmt(c_quintic)}")

    print(f"\n  Cubic (2,1) cross-check:")
    print(f"    p·λ^(p-1)·A       = {fmt(cubic_formula)}")
    print(f"    computed           = {fmt(c_cubic)}")
    print(f"    discrepancy        = {float(err_cubic):.2e}")
    if cubic_exact is not None:
        print(f"    [ALG] exact target = {fmt(cubic_exact)}")
        print(f"    match to [ALG]     = {float(abs(c_cubic - cubic_exact)):.2e}")

    print(f"\n  Quintic decomposition:")
    print(f"    A. Direct ν₅ transport       : {fmt(q_direct_nu5)}")
    print(f"       numeric check err         : {float(err_nu5):.2e}")
    print(f"    B. ν₃ self-interaction       : {fmt(q_cubic_self)}")
    print(f"    C. lattice self              : {fmt(q_lattice_self)}  [THM: expect 0]")
    print(f"    D. ν₃ × lattice cross        : {fmt(q_cubic_lattice_cross)}  [THM: expect 0]")
    print(f"    Reconstruction error         : {float(err_recon):.2e}")

    assert abs(q_lattice_self) < mp.mpf("1e-50"), f"[THM] VIOLATED: C != 0, got {q_lattice_self}"
    assert abs(q_cubic_lattice_cross) < mp.mpf("1e-50"), f"[THM] VIOLATED: D != 0, got {q_cubic_lattice_cross}"
    print("    [NUM + charge-selection rule] C=D=0 assertions: PASS")

    re_q = mp.re(c_quintic)
    if abs(re_q) > TOL:
        print(f"\n  Re(quintic) contributions:")
        parts = [
            ("A direct ν₅", q_direct_nu5),
            ("B ν₃ self", q_cubic_self),
            ("C lattice self", q_lattice_self),
            ("D cross", q_cubic_lattice_cross),
        ]
        print(f"    Total          : {float(re_q):+.10f}")
        for name, val in parts:
            print(f"    {name:20s}: {float(mp.re(val)):+.10f}  ({pct(mp.re(val), re_q):.1f}%)")

    # p=6 structural diagnostics only
    if raw_6step_target is not None:
        print(f"\n  Three-object reminder:")
        print("    (a) ν₅^(1-step,norm) = input C")
        print("    (b) c32^(raw,6-step) = uploaded jet6_deg5.json coefficient")
        print("    (c) ν₅^(6-step,norm) = OPEN")
        print("    this script computes F1^6 = Phi1^(-1) o F^6 o Phi1")

        print(f"\n  p=6 structural note:")
        print("    The uploaded jet6_deg5.json coefficient is a RAW 6-step coefficient.")
        print("    Therefore the comparison below is DIAGNOSTIC ONLY.")
        print("    It is NOT a pass/fail test of the 1-step candidate.")

        print(f"\n  Raw-vs-F1^6 diagnostic comparison:")
        print(f"    F1^6 quintic (this script)      = {fmt(c_quintic)}")
        print(f"    raw 6-step uploaded coefficient = {fmt(raw_6step_target)}")
        gap = c_quintic - raw_6step_target
        print(f"    gap (F1^6 - raw)                = {fmt(gap)}")
        print(f"    gap Re                          = {float(mp.re(gap)):+.10f}")
        print(f"    gap Im                          = {float(mp.im(gap)):+.10f}")

        raw_re = mp.mpf(-77) / 216
        backbone = mp.mpf(19) / 12 + 2 * raw_re
        print(f"\n  Raw-jet backbone check:")
        print(f"    19/12 + 2*Re(raw c32)          = {float(backbone):.10f}")
        print(f"    47/54                          = {float(mp.mpf(47) / 54):.10f}")
        print(f"    error                          = {float(abs(backbone - mp.mpf(47) / 54)):.2e}")

    if show_gap and p == 6:
        print(f"\n  Additional p=6 diagnostics:")
        print(f"    ν₃ self exact expected          = {fmt(P6_CUBIC_SELF)}")
        print(f"    ν₃ self from run                = {fmt(q_cubic_self)}")
        print(f"    direct ν₅ transport             = {fmt(q_direct_nu5)}")
        print(f"    F1^6 total                      = {fmt(c_quintic)}")
        print(f"    raw uploaded total              = {fmt(RAW_P6_C32_6STEP)}")
        print(f"    (F1^6 total) - (raw total)      = {fmt(c_quintic - RAW_P6_C32_6STEP)}")

    return {
        "c_quintic": c_quintic,
        "c_lattice": c_lat_ps,
        "c_cubic": c_cubic,
        "q_direct_nu5": q_direct_nu5,
        "q_cubic_self": q_cubic_self,
        "q_lattice_self": q_lattice_self,
        "q_cubic_lattice_cross": q_cubic_lattice_cross,
    }

# -----------------------------------------------------------------------------
# Main CLI
# -----------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="RTG step-accumulation tool for p=5 / p=6 strong resonances."
    )
    parser.add_argument("--case", choices=["all", "p5", "p6"], default="all")
    parser.add_argument("--p6-mode", choices=["fail", "solver", "manual"], default="solver")
    parser.add_argument("--c6-re", type=str, default=None)
    parser.add_argument("--c6-im", type=str, default=None)
    parser.add_argument("--b6-re", type=str, default=None)
    parser.add_argument("--b6-im", type=str, default=None)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--show-gap", action="store_true")
    args = parser.parse_args()

    mp.mp.dps = args.dps

    print("RTG STEP-ACCUMULATION TOOL  (CLI, canonical)")
    print(f"dps = {mp.mp.dps}")

    # p=6 coefficient selection
    if args.p6_mode == "fail":
        B6 = B6_legacy
        C6 = C6_fail
        p6_label = "1:6 resonance — legacy FAIL candidate"
    elif args.p6_mode == "solver":
        B6 = B6_solver
        C6 = C6_solver
        p6_label = "1:6 resonance — solver-derived 1-step candidate"
    else:
        if args.c6_re is None or args.c6_im is None:
            raise ValueError("--p6-mode manual requires --c6-re and --c6-im")

        c6_re = parse_real_expr(args.c6_re)
        c6_im = parse_real_expr(args.c6_im)
        C6 = c6_re + mp.mpc(0, 1) * c6_im

        if args.b6_re is not None and args.b6_im is not None:
            b6_re = parse_real_expr(args.b6_re)
            b6_im = parse_real_expr(args.b6_im)
            B6 = b6_re + mp.mpc(0, 1) * b6_im
        else:
            B6 = B6_solver

        p6_label = "1:6 resonance — manual 1-step candidate"

    if args.case in ("all", "p5"):
        out5 = decompose(
            label="1:5 resonance",
            p=5,
            lam=lam5,
            A=A5,
            B=B5,
            lat_mono=(0, 4),
            C=C5,
            cubic_exact=c21_5_exact,
            raw_6step_target=None,
            show_gap=False,
        )
        print(f"\n  p=5 summary:")
        print(f"    c_quintic^(5-step,norm) = {fmt(out5['c_quintic'])}")
        print(f"    2Re                     = {float(2 * mp.re(out5['c_quintic'])):.8f}")
        print(f"    c_lat^(5-step,norm)     = {fmt(out5['c_lattice'])}")
        print(f"    2Re(c_lat)              = {float(2 * mp.re(out5['c_lattice'])):.8f}")

    if args.case in ("all", "p6"):
        out6 = decompose(
            label=p6_label,
            p=6,
            lam=lam6,
            A=A6,
            B=B6,
            lat_mono=(0, 5),
            C=C6,
            cubic_exact=c21_6_exact,
            raw_6step_target=RAW_P6_C32_6STEP,
            show_gap=args.show_gap,
        )

        print(f"\n  p=6 summary:")
        print(f"    chosen C6                = {fmt(C6)}")
        print(f"    chosen B6                = {fmt(B6)}")
        print(f"    F1^6 quintic^(6-step)    = {fmt(out6['c_quintic'])}")
        print(f"    raw c32^(6-step) target  = {fmt(RAW_P6_C32_6STEP)}")
        print(f"    Re(F1^6)                 = {float(mp.re(out6['c_quintic'])):+.10f}")
        print(f"    Re(raw target)           = {float(mp.re(RAW_P6_C32_6STEP)):+.10f}")
        print(f"    gap Re                   = {float(mp.re(out6['c_quintic'] - RAW_P6_C32_6STEP)):+.10f}")
        print(f"    gap Im                   = {float(mp.im(out6['c_quintic'] - RAW_P6_C32_6STEP)):+.10f}")

if __name__ == "__main__":
    main()