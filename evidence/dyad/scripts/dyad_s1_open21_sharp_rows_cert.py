#!/usr/bin/env python3
"""dyad_s1_open21_sharp_rows_cert.py -- S1: OPEN 21 primitive-variable phase remainder on RECOG's unconditional sharpened
R9 rows (exact-rational certificate of the constants).

Premise (statement level, checked as text in the governing editions passed on the command line):
  - DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (dyad-v6.4.23 §6.14): for 0<|W_0|<=w_j,
      |M_W - P_2(W_0)| <= K'_j Q_0^{3/2} + C_{2,j} (256/225)^2 Q_0^2   (primary),
    where the only R9 input of the bound is |E| <= C_{2,j} q_0^2 + K_2 q_0^{3/2} of the chart-variable memory law, with
    q_0 <= (256/225) Q_0; K'_j collects K_2 and the P5 terms and does not depend on C_{2,j} (recorded distinction (ii)).
    The secondary constant is K_j = ceiling of K'_j + C_{2,j}(256/225)^2 w_j, built from the published K'_j.
  - RECOG-THM-R9-SHARPENED-ROWS (recog-v0.3.26 §6.13a): RECOG-THM-R9-MEMORY holds with (C_2, q_max) = (259.2, 1/400)
    on |z|<=1/20 and (81.49, 1/1600) on |z|<=1/40, same scope and windows; it uses the adopted DYAD-THM-NF-REM C_7 = 100/30.
    The -C7 rows (221.4 / 75.69, RECOG-THM-R9-SHARPENED-ROWS-C7) are NOT used.
Gates:
  G0  input text: the OPEN 21 table rows and the sharpened-rows statement occur verbatim in the files given
  G1  reproduction: the adopted C_{2,j}(256/225)^2 (33882112/50625, 10682368/50625) and K_j (8831/250, 883/100) are
      recomputed from K'_j, C_{2,j}, w_j (K_j is an outward ceiling, and below it by less than one unit of its last digit)
  G2  windows: q_max of each sharpened row equals the squared chart radius of the NF-REM row (1/400, 1/1600)
  G3  new primary constants C'_{2,j}(256/225)^2, exact
  G4  new secondary constants: S_j = K'_j + C'_{2,j}(256/225)^2 w_j exact; published 3-decimal ceilings 19.680 (A) and
      6.357 (B) are outward and minimal at 3 decimals
  G5  improvement: S_j < K_j for both rows; the -C7 values are not inputs
Negative controls (each exit 1): --control C7 (-C7 rows used), MIX (rows swapped), FLOOR (published value rounded down),
NOFACTOR ((256/225)^2 dropped), W2 (w_j^2 in place of w_j).
usage: python -I -B dyad_s1_open21_sharp_rows_cert.py --dsn <dyad-v6.4.23 DSN> --recog <recog-v0.3.26 DSN> --out s1.json
Exit 0 all gates pass; 1 otherwise. Output JSON byte-deterministic.
"""
import sys, json, argparse, hashlib
sys.dont_write_bytecode = True
from fractions import Fraction as F

ROW_A = "| A | $\\lvert z\\rvert\\le\\tfrac1{20}$ | $\\tfrac3{64}$ | $\\tfrac{3951}{1000}$ | $517$ | $\\tfrac{33882112}{50625}$ | $\\tfrac{8831}{250}$ |"
ROW_B = "| B | $\\lvert z\\rvert\\le\\tfrac1{40}$ | $\\tfrac3{128}$ | $\\tfrac{971}{250}$ | $163$ | $\\tfrac{10682368}{50625}$ | $\\tfrac{883}{100}$ |"
SHARP = "Both theorems hold with $(C_2,q_{\\max})=(259.2,\\tfrac1{400})$ on $|z|\\le\\tfrac1{20}$ and $(81.49,\\tfrac1{1600})$ on $|z|\\le\\tfrac1{40}$"
PUB = {"A": F(19680, 1000), "B": F(6357, 1000)}


def ceil_dec(x, d):
    s = 10 ** d
    return F(-((-x.numerator * s) // x.denominator), s)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dsn", required=True); ap.add_argument("--recog", required=True)
    ap.add_argument("--out", default="s1.json"); ap.add_argument("--control", choices=["C7", "MIX", "FLOOR", "NOFACTOR", "W2"])
    o = ap.parse_args()
    D = open(o.dsn, encoding="utf-8").read(); R = open(o.recog, encoding="utf-8").read()
    G, info = {}, {}
    G["G0_input_text"] = D.count(ROW_A) == 1 and D.count(ROW_B) == 1 and R.count(SHARP) == 1
    info["inputs_sha256"] = {"dsn": hashlib.sha256(D.encode()).hexdigest(), "recog": hashlib.sha256(R.encode()).hexdigest()}
    fac = F(1) if o.control == "NOFACTOR" else F(256, 225) ** 2
    rows = {"A": {"Kp": F(3951, 1000), "w": F(3, 64), "C2": F(517), "Kj": F(8831, 250), "C2f": F(33882112, 50625), "r": F(1, 20),
                  "C2s": F(2592, 10), "qmax": F(1, 400), "C2_C7": F(2214, 10)},
            "B": {"Kp": F(971, 250), "w": F(3, 128), "C2": F(163), "Kj": F(883, 100), "C2f": F(10682368, 50625), "r": F(1, 40),
                  "C2s": F(8149, 100), "qmax": F(1, 1600), "C2_C7": F(7569, 100)}}
    wf = (lambda w: w * w) if o.control == "W2" else (lambda w: w)
    g1 = g2 = g4 = g5 = True; out = {}
    for j, x in rows.items():
        # G1: reproduce the adopted table
        c2f = x["C2"] * fac; kj_exact = x["Kp"] + c2f * wf(x["w"])
        digits = 3 if j == "A" else 2
        g1 &= c2f == x["C2f"] and ceil_dec(kj_exact, digits) == x["Kj"]
        # G2: windows
        g2 &= x["qmax"] == x["r"] ** 2
        # G3/G4: new constants
        y = rows["B" if j == "A" else "A"] if o.control == "MIX" else x
        c2s = (y["C2_C7"] if o.control == "C7" else y["C2s"]) * fac
        s_exact = x["Kp"] + c2s * wf(x["w"])
        pub = PUB[j] - (F(1, 1000) if o.control == "FLOOR" else 0)
        g4 &= s_exact <= pub and pub - s_exact < F(1, 1000)
        g5 &= s_exact < x["Kj"] and o.control != "C7"
        out[j] = {"C2_sharp": str(y["C2s"]), "primary_C2_sharp_times_factor": str(c2s), "primary_float": "%.10f" % float(c2s),
                  "secondary_exact": str(s_exact), "secondary_float": "%.10f" % float(s_exact), "secondary_published": str(pub),
                  "adopted_K_j": str(x["Kj"]), "adopted_secondary_exact_float": "%.10f" % float(kj_exact)}
    G["G1_adopted_table_reproduced"] = g1; G["G2_windows_match_rows"] = g2
    G["G3_primary_constants_exact"] = all(F(out[j]["primary_C2_sharp_times_factor"]) == rows[j]["C2s"] * F(256, 225) ** 2 for j in rows)
    G["G4_published_ceilings_outward_minimal"] = g4; G["G5_improvement_unconditional_rows"] = g5
    G = {k: bool(v) for k, v in G.items()}; ok = all(G.values())
    for k in sorted(G): print(k, "PASS" if G[k] else "FAIL")
    print("RESULT", "PASS" if ok else "FAIL")
    with open(o.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"gates": G, "rows": out, "info": info, "control": o.control, "all_pass": ok,
                   "script": "dyad_s1_open21_sharp_rows_cert.py"}, f, indent=1, sort_keys=True); f.write("\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
