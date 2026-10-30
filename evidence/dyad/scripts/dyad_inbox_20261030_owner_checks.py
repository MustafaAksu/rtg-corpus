#!/usr/bin/env python3
"""dyad_inbox_20261030_owner_checks.py -- Dyadic owner checks for the inbox round of 30 Oct 2026 (pipe items D1-D3).

Owner (Claude) checks behind records/dyad/DYAD_OWNER_DISPOSITION_INBOX_20261030.md. Inputs are the unchanged uploads of
PR #125 (branch claude/atlas-advisory-dyad-inbox), passed by path and hash-checked before use.

D1 (DYAD-THM-OPEN18, q*) -- python-flint ball arithmetic, 256 bits, canonical family (rho_0, eta_0) = (0, q):
  O1  isolation: rho_4 changes sign on [q* - 1e-30, q* + 1e-30] and d rho_4/dq excludes 0 on the whole certificate gap
      G = [1.26021320256, 1.26021520256] of open18_arb_cert_final.cpp, so q* is the unique zero of rho_4 in G; eta_4 < 0
      there, so on rho_4 = 0 the angle Theta_4 = Arg(rho + omega eta) equals -pi/3 (the ISP-funnel edge).
  O2  NUMGEN's condition: eta_6(q*) - q* excludes 0 (Dyadic's q* is not a root of eta_6(q) - q).
  O3  gap closure: for n = 3 and n = 4, dQ_n/dq > 0, N_Theta,n = rho_n eta_n' - eta_n rho_n' < 0 and the Theta
      denominator (2 rho_n - eta_n)^2 + 3 eta_n^2 > 0 on all of G (the quantities of the recovered certificate; it swept
      Gamma_3 on [0.001, inf G] and Gamma_4 on [sup G, 2] and left G to the unrecovered footprint audits).
  O4  [NUM, not a certificate] footprint reading on a uniform grid of 200 000 points of (0, 2]: the step-n split of the
      certificate (n = 3 below q*, n = 4 above) agrees with "the last step k in 1..6 whose Theta_k lies in the closed
      angular window [-2pi/3, -pi/3]", and disagrees with "the first such step" (both steps 3 and 4 lie in the window on
      (q*, q_3^-)), where q_3^- is the root of Theta_3 = -2pi/3. Also reported: Q_3 = Q_c and Q_4 = Q_c, Q_c = (arcsin ln 2)^2.
D2 (DYAD-THM-NF-REM C_7 rows) -- exact rationals from the P2-B v2 certificate.json:
  O5  value_rational_upper <= 851/10 (|z| <= 1/20) and <= 277/10 (|z| <= 1/40); both exceed the displayed 8507/100 and
      2760/100, which are therefore nearest-rounded displays, not ceilings.
D3 (DYAD-THM-LPHASE-ROWA-REMAINDER constants) -- exact rationals, by executing the unchanged row-A certificate source in a
temporary copy (its own gates run; its final JSON print and exit are skipped) and reading its variables:
  O6  c'_Q (exact) > 36915/100000 and <= 36916/100000; c_Q (exact) <= 79246/100000.
  O7  the FIN constant recomputed with the published ceilings c_Q = 0.79246, c'_Q = 0.36916 in place of the exact values
      (same Lbar, K_Theta, c_J, c_7, tau ceiling, bridge ceiling as the certificate) is <= 403/250, and the certificate's
      own gates all pass.
Negative controls (each must make the run exit 1): --control A (q* shifted by 1e-20: O1 fails); --control B
(c'_Q ceiling 0.36915: O6 fails); --control C (C_7 ceiling 85.07: O5 fails).
Usage:
  python -I -B dyad_inbox_20261030_owner_checks.py --rowa-dir <dir with dyad_numgen_lphase_rowA_cert.py, qw.py, tzw.py>
         --p2b-cert <DYAD_RETURN_ENCLOSURE_P2B_v2/outputs/certificate.json> --out owner_checks.json
Exit 0 all checks pass; 1 otherwise; 3 crash. Output JSON byte-deterministic (exact rationals and fixed-digit strings).
"""
import os, sys, json, argparse, hashlib, math, cmath, shutil, tempfile
sys.dont_write_bytecode = True
from fractions import Fraction as Fr

HASH = {'dyad_numgen_lphase_rowA_cert.py': '117484ae1a2509b6f6065d395840bfdfe2b0c977af0505f9fe6de68c13959cdb',   # DSN-recorded hashes
        'qw.py': '3a913062c1cdc6d151a2fb5b2f76d5354a367d1fa55df43f1f31d06e1b94cce8',
        'tzw.py': 'f007d42cde36d2a70115b9db25f47b107c446735fa31c66664f620c3247a5609'}
# certificate.json of P2-B v2 is inside the hash-checked zip e4e2bab0...dbe4 (DSN-recorded); its own hash is reported, not pinned
QSTAR = '1.26021420256347711487243856095650439'
GAP = ('1.26021320256', '1.26021520256')


def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def d1_checks(control):
    from flint import arb, ctx
    ctx.prec = 256
    def step(r, e, dr, de):
        s, c = e.sin(), e.cos(); ex = r.exp()
        return r - s, e + ex - 1 - s, dr - c * de, de + ex * dr - c * de
    def orb(q, n):
        r, e, dr, de = arb(0), q, arb(0), arb(1)
        for _ in range(n): r, e, dr, de = step(r, e, dr, de)
        return r, e, dr, de
    lo, hi = arb(GAP[0]).lower(), arb(GAP[1]).upper()
    G = arb((lo + hi) / 2, (hi - lo) / 2)
    qs = arb(QSTAR) + (arb('1e-20') if control == 'A' else 0)
    eps = arb('1e-30')
    rm = orb(qs - eps, 4)[0]; rp = orb(qs + eps, 4)[0]
    _, e4, d4, _ = orb(G, 4)
    out, ok = {}, {}
    ok['O1_sign_change'] = bool((rm > 0 and rp < 0) or (rm < 0 and rp > 0))
    ok['O1_derivative_nonzero_on_gap'] = bool(not d4.contains(0))
    ok['O1_eta4_negative_on_gap'] = bool(e4 < 0)
    out['O1'] = {'q_star_36_digits': QSTAR, 'enclosure_half_width': '1e-30', 'rho4_at_q*-1e-30': rm.str(6), 'rho4_at_q*+1e-30': rp.str(6),
                 'drho4_dq_on_gap': d4.str(8), 'eta4_on_gap': e4.str(8)}
    r6, e6, _, _ = orb(arb(QSTAR), 6)
    ok['O2_eta6_minus_q_nonzero'] = bool(not (e6 - arb(QSTAR)).contains(0))
    out['O2'] = {'eta6(q*)-q*': (e6 - arb(QSTAR)).str(10), 'numgen_q*_prefix': '0.3156258836595616'}
    o3 = {}
    for n in (3, 4):
        r, e, dr, de = orb(G, n)
        dQ = (2 * r - e) * dr + (2 * e - r) * de; N = r * de - e * dr; den = (2 * r - e) ** 2 + 3 * e * e
        ok['O3_n%d' % n] = bool(dQ > 0 and N < 0 and den > 0)
        o3['n=%d' % n] = {'dQ_dq': dQ.str(6), 'N_Theta': N.str(6), 'denominator': den.str(6)}
    out['O3'] = o3
    # O4: [NUM] grid reading (double precision)
    w = complex(-0.5, math.sqrt(3) / 2); qsf = float(QSTAR)
    def forb(q, n=6):
        r, e = 0.0, q; o = [(r, e)]
        for _ in range(n): r, e = r - math.sin(e), e + math.expm1(r) - math.sin(e); o.append((r, e))
        return o
    inwin = lambda t: -2 * math.pi / 3 <= t <= -math.pi / 3
    M = 200000; last_ok = first_ok = 0; sets = {}
    for i in range(1, M + 1):
        q = 2.0 * i / M; o = forb(q)
        ks = [k for k in range(1, 7) if inwin(cmath.phase(complex(o[k][0], 0) + w * o[k][1]))]
        expn = 3 if q < qsf else 4
        last_ok += bool(ks) and max(ks) == expn; first_ok += bool(ks) and min(ks) == expn
        sets[str(ks)] = sets.get(str(ks), 0) + 1
    import mpmath as mp
    mp.mp.dps = 30
    wm = (-1 + mp.sqrt(3) * 1j) / 2; Qc = mp.asin(mp.log(2)) ** 2
    def morb(q, n):
        r, e = mp.mpf(0), q
        for _ in range(n): r, e = r - mp.sin(e), e + mp.expm1(r) - mp.sin(e)
        return r, e
    th = lambda p: mp.arg(p[0] + wm * p[1]); Qf = lambda p: p[0] ** 2 - p[0] * p[1] + p[1] ** 2
    q3w = mp.findroot(lambda q: th(morb(q, 3)) + 2 * mp.pi / 3, 1.3)
    q3c = mp.findroot(lambda q: Qf(morb(q, 3)) - Qc, 1.35); q4c = mp.findroot(lambda q: Qf(morb(q, 4)) - Qc, 1.95)
    out['O4_NUM'] = {'grid_points': M, 'last_window_step_matches_split': last_ok, 'first_window_step_matches_split': first_ok,
                     'window_step_sets': dict(sorted(sets.items())), 'Theta_3=-2pi/3_at_q': mp.nstr(q3w, 15),
                     'Q_3=Q_c_at_q': mp.nstr(q3c, 15), 'Q_4=Q_c_at_q': mp.nstr(q4c, 15), 'Q_c': mp.nstr(Qc, 15),
                     'status': 'NUM reading only; not a certificate of branch legality'}
    return ok, out


def d2_checks(path, control):
    d = json.load(open(path, encoding='utf-8'))['profiles']
    cA = Fr(8507, 100) if control == 'C' else Fr(851, 10)
    vA = Fr(d['enlarged']['value_rational_upper']); vB = Fr(d['small']['value_rational_upper'])
    ok = {'O5_row_1/20_le_ceiling': vA <= cA and d['enlarged']['radius'] == '1/20',
          'O5_row_1/40_le_277/10': vB <= Fr(277, 10) and d['small']['radius'] == '1/40',
          'O5_displayed_values_not_ceilings': vA > Fr(8507, 100) and vB > Fr(2760, 100)}
    out = {'certificate_json_sha256': sha(path), 'C7_upper_row_1/20': '%.13f' % float(vA), 'C7_upper_row_1/40': '%.13f' % float(vB),
           'ceilings_tested': [str(cA), '277/10'], 'adopted_constants_unchanged': [d['enlarged']['C7_NF_vec'], d['small']['C7_NF_vec']]}
    return ok, out


def d3_checks(rowa_dir, control):
    src = os.path.join(rowa_dir, 'dyad_numgen_lphase_rowA_cert.py')
    hs = {f: sha(os.path.join(rowa_dir, f)) for f in ('dyad_numgen_lphase_rowA_cert.py', 'qw.py', 'tzw.py')}
    hash_ok = all(hs[f] == HASH[f] for f in hs)
    tmp = tempfile.mkdtemp(prefix='rowa_')
    for f in hs: shutil.copy(os.path.join(rowa_dir, f), tmp)
    text = open(os.path.join(tmp, 'dyad_numgen_lphase_rowA_cert.py'), encoding='utf-8').read()
    cut = text.index('txt = json.dumps(out, indent=1, sort_keys=True); print(txt)')
    cwd = os.getcwd(); os.chdir(tmp); sys.path.insert(0, tmp)
    ns = {'__name__': 'rowa_cert'}
    try:
        exec(compile(text[:cut], 'dyad_numgen_lphase_rowA_cert.py', 'exec'), ns)
    finally:
        os.chdir(cwd); sys.path.remove(tmp); shutil.rmtree(tmp)
        for m in ('qw', 'tzw'): sys.modules.pop(m, None)
    tail_c, cQ, Cstar, Cpub = ns['tail_c'], ns['cQ'], ns['Cstar'], ns['Cpub']
    cQp_pub = Fr(36915, 100000) if control == 'B' else Fr(36916, 100000); cQ_pub = Fr(79246, 100000)
    inner2 = ns['Lbar'] + (ns['KThA'] + ns['tau_hi'] * cQp_pub + ns['cJ']) / 20 + ns['c7'] / 8000
    yb2 = 1 / (1 - cQ_pub / 20); C2 = inner2 * yb2 * ns['sqrt_hi'](yb2)
    ok = {'O6_input_hashes': hash_ok, 'O6_certificate_gates_pass': all(ns['g_'].values()) and not any(ns['neg'].values()),
          'O6_cQprime_exact_gt_0.36915': tail_c > Fr(36915, 100000), 'O6_cQprime_exact_le_ceiling': tail_c <= cQp_pub,
          'O6_cQ_exact_le_0.79246': cQ <= cQ_pub, 'O7_FIN_with_published_ceilings_le_403/250': C2 <= Fr(403, 250),
          'O7_certificate_FIN_published_is_403/250': Cpub == Fr(403, 250)}
    out = {'input_sha256': hs, 'cQprime_exact': '%.15f' % float(tail_c), 'cQ_exact': '%.15f' % float(cQ),
           'C_star_exact': '%.12f' % float(Cstar), 'C_star_with_published_ceilings': '%.12f' % float(C2),
           'margin_403/250_minus_that': '%.6e' % float(Fr(403, 250) - C2), 'ceilings_tested': [str(cQ_pub), str(cQp_pub)],
           'imported_row_A_C7': str(ns['C7A'])}
    return ok, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--rowa-dir', required=True); ap.add_argument('--p2b-cert', required=True)
    ap.add_argument('--out', default='owner_checks.json'); ap.add_argument('--control', choices=['A', 'B', 'C'])
    o = ap.parse_args()
    G, info = {}, {}
    g, i = d1_checks(o.control); G.update(g); info['D1'] = i
    g, i = d2_checks(o.p2b_cert, o.control); G.update(g); info['D2'] = i
    g, i = d3_checks(o.rowa_dir, o.control); G.update(g); info['D3'] = i
    G = {k: bool(v) for k, v in G.items()}
    ok = all(G.values())
    for k in sorted(G): print(k, 'PASS' if G[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': G, 'info': info, 'all_pass': ok, 'control': o.control, 'script': 'dyad_inbox_20261030_owner_checks.py'},
                  f, indent=1, sort_keys=True, ensure_ascii=False); f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        import traceback; traceback.print_exc(); print('CRASH', type(ex).__name__, ex); sys.exit(3)
