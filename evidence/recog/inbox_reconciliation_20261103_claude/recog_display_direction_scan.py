#!/usr/bin/env python3
"""recog_display_direction_scan.py -- direction-aware check of displayed RECOG constants against certificate values (recog-v0.3.26).

NONCANONICAL session evidence (RECOG co-owner, Claude; reconciliation of the inbox round, 3 Nov 2026). Prompted by
R2-PRECISION-01 (PR #172): the display c_7^R = 100.23 lies below the certified value 100.2300196... of its own formula.
A displayed CEILING must not lie below the certified upper value; a displayed WINDOW (a certified region q0 < w) must not
lie above the certified window; a reported VALUE (an enclosure printed for information, not stated with <=) has no
direction requirement. The limit display beta -> 0.792 is a rounded limit, not a ceiling, and is not listed. Every row below pairs one DSN display string with the certificate JSON value it reports.
The list is not exhaustive: it covers the A1c, drift and B1 constants that have a JSON counterpart. Scripts use the exact
intervals, never the displays (checked separately by grep: no display literal is an input), so a failing row is a display
correction, not a certificate defect.
usage (repository root): python -I evidence/recog/inbox_reconciliation_20261103_claude/recog_display_direction_scan.py OUT_JSON
"""
import json, sys
D = open("dsn/RTG_RELATIONAL_RECOGNITION_DSN.md", encoding="utf-8").read()
J = lambda p: json.load(open(p))
dd = J("evidence/recog/a1c_drift/a1c_drift_centering_cert.json"); pt = J("evidence/recog/a1c_drift/a1c_drift_proof_table_cert.json")
ct = J("evidence/recog/a1c_comb/a1c_combined_tail_cert.json")["G2_constants"]; ib = J("evidence/recog/a1c_inblock/a1c_inblock_angular_cert.json")["G2_constants"]
p1 = J("evidence/recog/a1c_1b/a1c_tail_averaging_cert.json")["G2_constants"]; so = J("evidence/recog/a1c_so/a1c_start_offset_cert.json")["G1"]
q1 = J("evidence/recog/a1c_3/a1c_q1prime_fiber_cert.json")["G2_constants"]; b1 = J("evidence/recog/b1_l1l2/b1_l1l2_sharpened_rows_cert.json")
rw = {r["row"]: r for r in b1["G3_rows"]}
g0 = p1["gamma0"][1] if isinstance(p1["gamma0"], list) else p1["gamma0"]
# (name, kind, DSN display string, displayed value, certified value, source)
ROWS = [
 ("gamma_2 (RECIPROCAL-DRIFT)", "ceiling", "\\gamma_2=212.6", 212.6, dd["G2_constants"]["gamma2"], "a1c_drift G2"),
 ("K_eps(625)", "ceiling", "K_\\epsilon=0.7203", 0.7203, dd["G2_constants"]["K_eps"]["625"]["K"], "a1c_drift G2"),
 ("K_eps(1000)", "ceiling", "$0.4513$", 0.4513, dd["G2_constants"]["K_eps"]["1000"]["K"], "a1c_drift G2"),
 ("K_eps(2500)", "ceiling", "$0.1860$", 0.1860, dd["G2_constants"]["K_eps"]["2500"]["K"], "a1c_drift G2"),
 ("c_J^R (COMBINED-TAIL)", "ceiling", "c_J^R=0.5008", 0.5008, ct["c_J^R"], "a1c_comb G2"),
 ("c_7^R (COMBINED-TAIL)", "ceiling", "c_7^R=100.23", 100.23, ct["c_7^R"], "a1c_comb G2"),
 ("sup|d| (COMBINED-TAIL)", "ceiling", "0.2955", 0.2955, ct["sup|d|"], "a1c_comb G2"),
 ("gamma_0 (TAIL-HARMONICS)", "ceiling", "\\gamma_0=0.17715", 0.17715, g0, "a1c_1b G2"),
 ("gamma_1 (TAIL-HARMONICS)", "ceiling", "\\gamma_1=205.15", 205.15, p1["gamma1"], "a1c_1b G2"),
 ("c_delta (INBLOCK-ANGLE)", "ceiling", "c_\\delta=0.793", 0.793, ib["c_delta_on_U_T"], "a1c_inblock G2"),
 ("beta(625) (START-OFFSET)", "ceiling", "\\beta(625)=0.799", 0.799, so["beta(625)"], "a1c_so G1"),
 ("c_Psi (PHASE-C1-FIBER)", "ceiling", "c_\\Psi=11.13", 11.13, q1["cPsi(=bound/q*)"], "a1c_3 G2"),
 ("Xi (PHASE-C1-FIBER)", "ceiling", "\\Xi=0.027", 0.027, q1["Xi"], "a1c_3 G2"),
 ("K_Phi L1 large (reported enclosure, not stated with <=)", "value", "258.4848", 258.4848, rw["L1 large"]["K_Phi_upper"], "b1 G3"),
 ("K_Phi L1 small (reported enclosure, not stated with <=)", "value", "81.4328", 81.4328, rw["L1 small"]["K_Phi_upper"], "b1 G3"),
 ("K_Phi L1+L2 large", "ceiling", "220.8471", 220.8471, rw["L1+L2 large"]["K_Phi_upper"], "b1 G3"),
 ("K_Phi L1+L2 small", "ceiling", "75.6392", 75.6392, rw["L1+L2 small"]["K_Phi_upper"], "b1 G3"),
 ("window L1 large", "window", "2.952\\times10^{-5}", 2.952e-5, rw["L1 large"]["window_new"], "b1 G3"),
 ("window L1 small", "window", "9.390\\times10^{-5}", 9.390e-5, rw["L1 small"]["window_new"], "b1 G3"),
 ("window L1+L2 large", "window", "3.456\\times10^{-5}", 3.456e-5, rw["L1+L2 large"]["window_new"], "b1 G3"),
 ("window L1+L2 small", "window", "1.011\\times10^{-4}", 1.011e-4, rw["L1+L2 small"]["window_new"], "b1 G3"),
] + [(f"C({a},5) (LOGFREE-ENVELOPE)", "ceiling", s, float(s), pt["PT3"][f"a={a},r=5"]["C_total"], "a1c_drift PT3") for a, s in (("625", "58.0"), ("1000", "61.0"), ("2500", "75.1"))]
out = []
for name, kind, disp, shown, val, src in ROWS:
    ok = True if kind == "value" else (shown >= val if kind == "ceiling" else shown <= val)
    out.append({"constant": name, "kind": kind, "display": disp, "in_dsn": disp in D, "displayed": shown, "certified": val, "source": src,
                "direction_ok": ok})
res = {"object": "recog-v0.3.26 dsn/RTG_RELATIONAL_RECOGNITION_DSN.md", "rows": out,
       "wrong_direction": [r["constant"] for r in out if not r["direction_ok"]], "all_displays_found": all(r["in_dsn"] for r in out)}
json.dump(res, open(sys.argv[1] if len(sys.argv) > 1 else "display_direction_scan.json", "w"), indent=1)
for r in out: print(f"{r['constant']:30s} {r['kind']:7s} shown {r['displayed']!s:>11}  certified {r['certified']:.10g}  {'ok' if r['direction_ok'] else 'WRONG DIRECTION'}  in-DSN={r['in_dsn']}")
print("wrong direction:", res["wrong_direction"])
