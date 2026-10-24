#!/usr/bin/env python3
"""dyad_open20_an_stage2_summary.py -- cross-run comparison of the stage-2 [NUM] scouting outputs.

Reads the scout JSON files of evidence/dyad/open20-an/stage2/ and prints, deterministically:
  1. truncation stability: for each pair (N1 < N2) the max relative difference of a_k over k <= N1 (expected 0 up to the
     stored 40 digits: the order-by-order solve does not feed back from higher orders), and the coefficient ranges;
  2. precision stability: same N, two --dps values, max relative difference of the stored midpoints and the max ball radii;
  3. the Borel-scale table per residue class and run, beside the model values;
  4. the candidate-point table of the largest run;
  5. the negative control (too small --dps): gate C3 fails and the coefficients explode;
  6. SHA-256 of every input file.
Usage: python -I -B dyad_open20_an_stage2_summary.py <dir>      (exit 0 = summary printed; 1 = an expectation failed)
"""
import sys, os, json, hashlib
sys.dont_write_bytecode = True
from mpmath import mp, mpc, mpf
mp.dps = 50


def load(d, name):
    return json.load(open(os.path.join(d, name), encoding='utf-8'))


def coeffs(info):
    return {int(k): mpc(v[0], v[1]) for k, v in info['coefficients'].items()}


def maxrel(c1, c2, kmax):
    return max(abs(c1[k] - c2[k]) / abs(c2[k]) for k in range(2, kmax + 1))


def main(d):
    names = sorted(f for f in os.listdir(d) if f.endswith('.json') and (f.startswith('scout_') or f.startswith('control_')))
    print('== files')
    for f in sorted(os.listdir(d)):
        p = os.path.join(d, f)
        if os.path.isfile(p) and f not in ('SHA256SUMS.txt', 'summary_output.txt'):
            print(hashlib.sha256(open(p, 'rb').read()).hexdigest(), ' ', f)
    runs = {n: load(d, n) for n in names}
    ok = True
    print('\n== gates')
    for n in names:
        print(n, runs[n]['gates'], 'all_pass=', runs[n]['all_pass'])
        if n.startswith('scout_') and not runs[n]['all_pass']: ok = False
        if n.startswith('control_') and runs[n]['all_pass']: ok = False
    sc = [n for n in names if n.startswith('scout_')]
    print('\n== truncation stability (max relative difference of a_k, k <= min(N1,N2))')
    for i in range(len(sc)):
        for j in range(i + 1, len(sc)):
            A, B = runs[sc[i]]['info'], runs[sc[j]]['info']
            if A['N'] == B['N']: continue
            kmax = min(A['N'], B['N'])
            print(f"{sc[i]} vs {sc[j]}: k<= {kmax}: {mp.nstr(maxrel(coeffs(A), coeffs(B), kmax), 3)}")
    print('\n== precision stability (same N, different dps)')
    for i in range(len(sc)):
        for j in range(i + 1, len(sc)):
            A, B = runs[sc[i]]['info'], runs[sc[j]]['info']
            if A['N'] != B['N']: continue
            print(f"{sc[i]} vs {sc[j]}: max rel diff of stored midpoints {mp.nstr(maxrel(coeffs(A), coeffs(B), A['N']), 3)}; "
                  f"max ball radius {A['max_ball_radius_a_k']} / {B['max_ball_radius_a_k']}; residual sup (mid) {A['residual_through_N+3']['sup_abs_midpoint']} / {B['residual_through_N+3']['sup_abs_midpoint']}")
    print('\n== coefficient magnitudes |a_k| (largest run), every 6th order')
    big = max(sc, key=lambda n: runs[n]['info']['N'])
    I = runs[big]['info']
    kmin = min(range(2, I['N'] + 1), key=lambda k: mpf(I['abs_coefficients'][str(k)]))
    print('run', big, ' minimum |a_k| at k =', kmin, '=', I['abs_coefficients'][str(kmin)])
    for k in range(2, I['N'] + 1, 6):
        print(f"  k={k:4d} |a_k|={I['abs_coefficients'][str(k)]}")
    print(f"  k={I['N']:4d} |a_k|={I['abs_coefficients'][str(I['N'])]}")
    print('\n== Borel-scale estimates per residue class r (k = 3n + r); model |zeta_z| =', I['borel']['model_abs_zeta_z'][:12],
          ' model arg/pi mod 1 =', I['borel']['model_arg_zeta_over_pi_mod_1'])
    for n in sc:
        B = runs[n]['info']['borel']['classes']
        for r in ('0', '1', '2'):
            c = B[r]
            if 'abs_zeta' not in c: print(n, 'r=', r, c); continue
            print(f"{n} r={r}: fit n in {c['fit_n_range']} ({c['n_points_fit']} pts): |zeta|={c['abs_zeta'][:10]} (x{c['abs_zeta_over_model'][:8]} model), "
                  f"arg/pi mod 1={c['arg_zeta_over_pi_mod_1'][:9]} (model {I['borel']['model_arg_zeta_over_pi_mod_1'][:9]}; diff {c['arg_minus_model_over_pi_mod_1'][:9]}), "
                  f"beta={c['beta_estimate'][0][:8]}{'+' if not c['beta_estimate'][1].startswith('-') else ''}{c['beta_estimate'][1][:8]}i; "
                  f"last |s_n|/n^2: {[(x, y[:8]) for x, y in c['two_step_ratio_abs_over_n2_last'][-3:]]}")
    print('\n== local beta-free scale estimates (largest run): zeta^2 ~ 2 / (s_{n+2} - 2 s_{n+1} + s_n), s_n = c_{n+2}/c_n, c_n = a_{3n+r}')
    C = coeffs(I)
    for r in (0, 1, 2):
        ks = [k for k in range(2, I['N'] + 1) if k % 3 == r]
        cs = [C[k] for k in ks]; ns = [(k - r) // 3 for k in ks]
        s = {ns[i]: cs[i + 2] / cs[i] for i in range(len(cs) - 2)}
        loc = []
        for nn in sorted(s):
            if nn + 2 in s:
                z2 = 2 / (s[nn + 2] - 2 * s[nn + 1] + s[nn])
                loc.append((nn, abs(z2) ** mpf('0.5'), (mp.arg(z2) / 2 / mp.pi)))
        tail = loc[-12:]
        vals = [v for _, v, _ in tail]
        print(f"  r={r}: n={tail[0][0]}..{tail[-1][0]}: |zeta| local = {[mp.nstr(v, 4) for v in vals]}; min {mp.nstr(min(vals), 4)} max {mp.nstr(max(vals), 4)} mean {mp.nstr(sum(vals) / len(vals), 4)}; "
              f"arg/pi mod 1 = {[mp.nstr(a, 3) for _, _, a in tail]}")
    print('\n== Borel–Padé singularity scouting (largest run): poles of the diagonal Padé approximants of B_r(t) = sum_n c_n t^n / n!, c_n = a_{3n+r}')
    print('   (nearest poles by modulus; a string of poles marks a branch cut; the first element of each string is the branch-point estimate; NUM only)')
    print('   (doublet test: a pole whose nearest numerator zero lies within 5% of |t| is a Froissart doublet and is excluded from the estimate)')
    from mpmath import matrix, lu_solve, polyroots, factorial
    mp.dps = 120          # the stored coefficients carry 80 digits; the Hankel systems below are ill-conditioned
    C = coeffs(I)
    pade = {}
    for r in (0, 1, 2):
        ks = [k for k in range(2, I['N'] + 1) if k % 3 == r]
        b = [C[k] / factorial(i) for i, k in enumerate(ks)]
        for M in (14, 22, 30, 34):
            L = M
            if L + M + 1 > len(b): continue
            A = matrix(M, M); rhs = matrix(M, 1)
            for i in range(1, M + 1):
                for j in range(1, M + 1): A[i - 1, j - 1] = b[L + i - j]
                rhs[i - 1] = -b[L + i]
            try:
                q = lu_solve(A, rhs)
            except ZeroDivisionError:
                print(f"  r={r} Pade[{L}/{M}]: Hankel system numerically singular at the stored precision; skipped"); continue
            roots = sorted(polyroots([q[M - 1 - j] for j in range(M)] + [mpf(1)], maxsteps=400, extraprec=600), key=lambda z: abs(z))
            # numerator P(t) = [B(t) Q(t)]_{<= L}; a pole with a numerator zero closer than 5% of |t| is a Froissart doublet (spurious)
            qq = [mpf(1)] + [q[j] for j in range(M)]
            pc = [sum(qq[i] * b[j - i] for i in range(0, min(j, M) + 1)) for j in range(L + 1)]
            zeros = polyroots(list(reversed(pc)), maxsteps=400, extraprec=600) if L > 0 else []
            def dz(z): return min(abs(z - w) for w in zeros) / abs(z) if zeros else mpf(1)
            near = [(mp.nstr(abs(z), 5), mp.nstr(mp.arg(z) / mp.pi, 4), 'DOUBLET' if dz(z) < mpf('0.05') else 'pole') for z in roots[:5]]
            clean = [z for z in roots if dz(z) >= mpf('0.05')]
            pade[(r, M)] = clean
            print(f"  r={r} Pade[{L}/{M}] nearest poles (|t|, arg/pi, doublet test): {near}; nearest non-doublet pole |t|={mp.nstr(abs(clean[0]), 5) if clean else 'none'}")
    print('   model: |zeta_z| =', I['borel']['model_abs_zeta_z'][:8], 'arg/pi = -0.4357 and +0.5643 (two singularities ±zeta, design D6)')
    print('   in the xi^3 Borel variable (|t_u| = |t_z| |ell|):', 'model |t_u| = 2 pi/3 =', mp.nstr(2 * mp.pi / 3, 6), '; observed nearest |t_u| per class at the highest order:',
          [mp.nstr(abs(pade[(r, max(M for (rr, M) in pade if rr == r))][0]) * mpf(I['abs_ell']), 5) for r in (0, 1, 2) if any(rr == r for (rr, _) in pade)])
    print('\n== candidate points (largest run); direction', I['candidates']['direction'])
    print('   jump-scale bracket exp(-|zeta_z|/|z*|^3) for |zeta_z| = 17.1 (Borel–Padé [34/34] branch-point estimate, N = 216) and 21.34 (model); NUM')
    for p in I['candidates']['points']:
        z3 = mpf(p['abs_z_star']) ** 3
        print(f"  target {p['target_model_jump_scale']}: |z*|^3={mp.nstr(z3, 6)}; exp(-17.1/|z*|^3)={mp.nstr(mp.exp(-mpf('17.1') / z3), 4)}; exp(-21.34/|z*|^3)={mp.nstr(mp.exp(-mpf('21.34') / z3), 4)}")
    for p in I['candidates']['points']:
        print(f"  target {p['target_model_jump_scale']}: |xi*|={p['abs_xi_star'][:10]} z*={p['z_star'][0][:12]}{'+' if not p['z_star'][1].startswith('-') else ''}{p['z_star'][1][:12]}i |z*|={p['abs_z_star'][:10]} "
              f"least term k={p['least_term_index']} (inside range: {p['least_term_inside_range']}; model n-estimate k~{p['model_least_term_index_3n_with_n=|zeta_xi|/|xi|^3']}) |term|={p['least_term_abs']}")
    print('\n== negative control(s)')
    for n in names:
        if n.startswith('control_'):
            J = runs[n]['info']
            print(n, 'max ball radius', J['max_ball_radius_a_k'], ' |a_N| =', J['abs_coefficients'][str(J['N'])], ' C3 =', runs[n]['gates']['C3_ball_radii_below_1e-30'])
    print('\nSUMMARY', 'OK' if ok else 'EXPECTATION FAILED')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else '.'))
