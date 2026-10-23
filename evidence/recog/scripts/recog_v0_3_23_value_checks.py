#!/usr/bin/env python3
"""RECOG v0.3.23 stage 1 -- value checks for the edited displays and the FC-21 illustration.

Part A (exact, sympy): the numbers printed by the stage-1 edits FB-14, FA-03, FB-15.
  A1  |G| = sqrt(481897)/90720 for G = -(43+5611*sqrt3*i)/1270080; display 0.0076520 (approx)
  A2  |G|/517 and |G|/163 displays (incompleteness windows, rows A/B)
  A3  |G|/(2*C7) displays for C7 = 100, 30 (R9 partial-budget thresholds)
  A4  max_Theta |Lambda_1(Theta)| = |G|, Lambda_1(Theta) = Im(G exp(-6 i Theta)) equals the printed form
  A5  |mu|/|c05_raw| ~ 41.2694355 (raw six-step frame), |mu|/|a05| ~ 59.1194304 (post-H2)
  A6  cot^2(pi/6) = 3 (frame scale factor at p = 6)
  A7  bound arithmetic: |M - c_iso q0| <= |G| q0 + C2 q0^2 implies |M| <= (|c_iso|+|G|) q0 + C2 q0^2
Part B ([NUM] illustration, float64; not a proof input): RECOG-THM-A1A-PHASE-EXISTENCE-U.
  For starts x0 in U = {0 < Q0 <= 1/625}: block law 2*pi - tau*Q_m + r_m with |r_m| <= (403/250) Q_m^(3/2)
  sampled (12 starts, 20000 blocks); the one-step branch bound eps <= 0.04654 sampled; the identity
  D_N - tau log N = tau*H_N + tau*sum_{m<N}(Q_m - 1/(a+m)) - sum_{m<N} r_m to rounding, with
  H_N = sum_{m<N} 1/(a+m) - log N; the psi-corrected partial series S_N = -tau*psi(a) +
  tau*sum_{m<N}(Q_m - 1/(a+m)) - sum_{m<N} r_m changes by < 5e-3 from N = 1e4 to 2e4 (the raw
  D_N - tau log N still moves by ~ tau*a/N there); H(a) = -psi(a) checked numerically (< 1e-9).

usage: python -I recog_v0_3_23_value_checks.py OUT_JSON      (exit 0 iff every check passes)
"""
import json, math, sys
import sympy as sp
import mpmath as mp

def part_a():
    out = {}
    s3 = sp.sqrt(3)
    G = -(43 + 5611*s3*sp.I)/1270080
    absG2 = sp.nsimplify(sp.expand(G*sp.conjugate(G)))
    out["A1_absG_squared_exact"] = str(absG2)
    ok1 = sp.simplify(absG2 - sp.Rational(481897, 90720**2)) == 0
    absG = sp.sqrt(sp.Rational(481897))/90720
    gv = sp.N(absG, 30)
    out["A1_absG"] = str(gv)
    ok1 = ok1 and abs(float(gv) - 0.0076520) < 5e-8 and float(gv) < 0.0076520   # display and upper bound
    w517, w163 = sp.N(absG/517, 20), sp.N(absG/163, 20)
    out["A2_windows"] = {"absG/517": str(w517), "absG/163": str(w163)}
    ok2 = abs(float(w517) - 1.4800743e-5) < 5e-13 and abs(float(w163) - 4.6944689e-5) < 5e-13
    t100, t30 = sp.N(absG/200, 20), sp.N(absG/60, 20)
    out["A3_partial_budget_thresholds"] = {"absG/(2*100)": str(t100), "absG/(2*30)": str(t30)}
    ok3 = abs(float(t100) - 3.83e-5) < 5e-8 and abs(float(t30) - 1.28e-4) < 5e-7
    th = sp.symbols("theta", real=True)
    lam1 = sp.im(sp.expand(G*(sp.cos(6*th) - sp.I*sp.sin(6*th))))
    printed = (43*sp.sin(6*th) - 5611*s3*sp.cos(6*th))/1270080
    ok4 = sp.simplify(lam1 - printed) == 0
    # amplitude of a*sin + b*cos is sqrt(a^2+b^2)
    amp = sp.sqrt(sp.Rational(43, 1270080)**2 + (5611*s3/1270080)**2)
    ok4 = ok4 and sp.simplify(amp - absG) == 0
    out["A4_max_abs_Lambda1_equals_absG"] = bool(ok4)
    mu = -sp.Rational(1, 2) - 2*s3*sp.I/3
    c05raw = -sp.Rational(61, 2160) - 43*s3*sp.I/6480
    a05 = -sp.Rational(49, 8640) - 307*s3*sp.I/25920
    r_raw = sp.N(sp.Abs(mu)/sp.Abs(c05raw), 15)
    r_nf = sp.N(sp.Abs(mu)/sp.Abs(a05), 15)
    out["A5_ratios"] = {"raw": str(r_raw), "post_H2": str(r_nf)}
    ok5 = abs(float(r_raw) - 41.2694355) < 1e-6 and abs(float(r_nf) - 59.1194304) < 1e-6
    ok5 = ok5 and round(float(r_raw), 2) == 41.27 and round(float(r_nf), 2) == 59.12
    ok6 = sp.simplify(sp.cot(sp.pi/6)**2 - 3) == 0
    q, Gs, c, C2, M = sp.symbols("q G c C2 M", positive=True)
    # |M| <= |M - c q| + |c| q  (triangle inequality); with the R9 bound this is (|c|+|G|) q + C2 q^2
    ok7 = sp.simplify((Gs*q + C2*q**2) + c*q - ((c + Gs)*q + C2*q**2)) == 0
    checks = {"A1": ok1, "A2": ok2, "A3": ok3, "A4": ok4, "A5": ok5, "A6": ok6, "A7": ok7}
    return out, checks

def T(rho, eta):
    r1 = rho - math.sin(eta)
    return r1, eta + (math.exp(rho) - 1.0) - math.sin(eta)

OM = complex(-0.5, math.sqrt(3)/2)
def W(rho, eta):
    return rho + OM*eta

def orbit(rho, eta, nblocks):
    """Return per-block Q_m and the lifted six-step increments (principal one-step angles)."""
    Q, inc, eps_max = [], [], 0.0
    lam = complex(0.5, math.sqrt(3)/2)
    for _ in range(nblocks):
        w0 = W(rho, eta)
        Q.append(abs(w0)**2)
        tot = 0.0
        for _ in range(6):
            w = W(rho, eta)
            rho, eta = T(rho, eta)
            w1 = W(rho, eta)
            eps_max = max(eps_max, abs(w1/(lam*w) - 1.0))
            tot += math.atan2((w1/w).imag, (w1/w).real)
        inc.append(tot)
    return Q, inc, eps_max

DRIFT_TOL = 5e-3   # illustration threshold for the psi-corrected partial series between N=1e4 and 2e4

def part_b():
    tau = 2/math.sqrt(3)
    starts = []
    for Q0 in (1/625, 1/1000, 1/2500):
        for th in (0.0, 1.1, 2.3, 4.0):
            r = math.sqrt(Q0)
            w = r*complex(math.cos(th), math.sin(th))
            eta = w.imag/(math.sqrt(3)/2)
            rho = w.real + 0.5*eta
            starts.append((Q0, th, rho, eta))
    N_list = [2500, 5000, 10000, 20000]
    rows, ok = [], True
    for Q0, th, rho, eta in starts:
        Q, inc, eps = orbit(rho, eta, N_list[-1])
        a = 1.0/Q[0]
        r = [inc[m] - 2*math.pi + tau*Q[m] for m in range(len(Q))]
        ratio = max(abs(r[m])/Q[m]**1.5 for m in range(len(Q)))
        mp.mp.dps = 30
        psi = float(mp.digamma(a))
        Hn = lambda N: sum(1.0/(a+m) - math.log1p(1.0/(a+m)) for m in range(N)) - math.log(a) + math.log((a+N)/N)
        recs = {}
        for N in N_list:
            D = 2*math.pi*N - sum(inc[:N])
            CN = D - tau*math.log(N)
            formula_N = tau*Hn(N) + tau*sum(Q[m] - 1.0/(a+m) for m in range(N)) - sum(r[:N])
            formula_inf_H = -tau*psi + tau*sum(Q[m] - 1.0/(a+m) for m in range(N)) - sum(r[:N])
            recs[N] = {"C_N": CN, "identity_gap": CN - formula_N, "series_with_-psi": formula_inf_H}
        # H(a) = -log a + sum_{m>=0}[1/(a+m) - log(1+1/(a+m))]: partial sum to 1e5 plus the leading tail 1/(2(a+N))
        NH = 100000
        H_num = -math.log(a) + math.fsum(1.0/(a+m) - math.log1p(1.0/(a+m)) for m in range(NH)) + 0.5/(a+NH)
        H_lim_err = abs(H_num + psi)
        S = [recs[N]["series_with_-psi"] for N in N_list]
        drift = abs(S[-1] - S[-2])
        drift_raw = abs(recs[N_list[-1]]["C_N"] - recs[N_list[-2]]["C_N"])
        row = {"Q0": Q0, "theta": th, "eps_max": eps, "max_|r_m|/Q_m^1.5": ratio,
               "drift_series_10000_to_20000": drift, "drift_raw_C_N_10000_to_20000": drift_raw,
               "H_num_minus_(-psi)": H_lim_err,
               "by_N": {str(k): v for k, v in recs.items()}}
        good = (eps <= 0.04654 and ratio <= 403/250 and drift < DRIFT_TOL and H_lim_err < 1e-9 and
                all(abs(v["identity_gap"]) < 1e-8 for v in recs.values()))
        row["pass"] = good
        ok = ok and good
        rows.append(row)
    return rows, ok

def main(out_path):
    a_out, a_checks = part_a()
    b_rows, b_ok = part_b()
    res = {"part_A_exact": a_out, "part_A_checks": {k: bool(v) for k, v in a_checks.items()},
           "part_B_num_illustration": b_rows, "part_B_pass": b_ok,
           "note": "Part B is a float64 [NUM] illustration, not a proof input."}
    allok = all(a_checks.values()) and b_ok
    res["all_pass"] = allok
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1)
    for k, v in a_checks.items():
        print(k, "PASS" if v else "FAIL")
    print("B (NUM illustration)", "PASS" if b_ok else "FAIL", f"({len(b_rows)} starts)")
    print("ALL PASS" if allok else "FAILURES")
    sys.exit(0 if allok else 1)

if __name__ == "__main__":
    main(sys.argv[1])
