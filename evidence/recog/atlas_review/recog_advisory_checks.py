#!/usr/bin/env python3
"""Bounded exact checks for the RECOG advisory, not an owner certificate replay.
Requires SymPy. The infinite-series conclusion is proved in the review note;
no finite numerical test here is offered as its proof.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
import sympy as s

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=Path('recog_advisory_check_results.json'))
    args = ap.parse_args()
    I, r = s.I, s.sqrt(3)
    R = s.Rational
    mu = -R(1, 2) - I*2*r/3
    tau = 2*r/3
    raw = -R(61, 2160) - I*43*r/6480
    nf = -R(49, 8640) - I*307*r/25920
    a32 = -R(97, 432) + I*197*r/324
    beta = s.expand(a32 - mu**2/2)
    G = -(43+5611*I*r)/1270080
    a, n, e, x = s.symbols('a n e x', positive=True)
    checks: list[dict[str, object]] = []
    def zero(key: str, expr: s.Expr) -> None:
        value = s.simplify(expr)
        checks.append({'id': key, 'result': 'PASS' if value == 0 else 'FAIL', 'residual': str(value)})
    zero('mu_norm_sq', s.expand(mu*s.conjugate(mu))-R(19,12))
    zero('averaging_identity', (1-6*I*tau)*G-(1-2*I*tau)*nf)
    zero('isotropic_coefficient', s.im(s.expand((1-2*I*tau)*beta))+4*r/27)
    zero('G_norm_sq', s.expand(G*s.conjugate(G))-R(481897,90720**2))
    zero('chart_shadow_3_16', (r/8)/tau-R(3,16))
    zero('section_shadow_3_8', (r/4)/tau-R(3,8))
    zero('reciprocal_difference_identity', 1/(a+n+e)-1/(a+n)+e/((a+n+e)*(a+n)))
    zero('log_remainder_lower_derivative', s.diff(x-s.log(1+x),x)-x/(1+x))
    zero('log_remainder_upper_derivative', s.diff(x*x/2-x+s.log(1+x),x)-x*x/(1+x))
    zero('log_remainder_at_zero', (x-s.log(1+x)).subs(x,0))
    gap = R('0.0076520')**2 - R(481897,90720**2)
    checks.append({'id':'G_rounded_ceiling','result':'PASS' if gap>0 else 'FAIL','positive_squared_gap':str(gap)})
    gap2 = R(403,250) - R('1.51632')*R('1.06252')
    checks.append({'id':'LPHASE_published_rational_ceiling','result':'PASS' if gap2>0 else 'FAIL','positive_gap':str(gap2)})
    norm = s.sqrt(s.expand(G*s.conjugate(G)))
    values = {
        'lattice_ratio_raw': str(s.N(s.sqrt(s.expand(mu*s.conjugate(mu)/(raw*s.conjugate(raw)))),25)),
        'lattice_ratio_post_H2': str(s.N(s.sqrt(s.expand(mu*s.conjugate(mu)/(nf*s.conjugate(nf)))),25)),
        'G_exact': str(norm), 'G_decimal':str(s.N(norm,25)),
        'incompleteness_A':str(s.N(norm/517,25)),
        'incompleteness_B':str(s.N(norm/163,25)),
        'partial_tail_budget_A':str(s.N(norm/200,25)),
        'partial_tail_budget_B':str(s.N(norm/60,25)),
    }
    report = {'status':'PASS' if all(c['result']=='PASS' for c in checks) else 'FAIL',
              'scope':'Finite exact algebra/inequality checks only; no inherited certificate replay; convergence proof is written separately.',
              'sympy':s.__version__, 'checks':checks, 'numerical_displays':values}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if report['status']=='PASS' else 1
if __name__=='__main__':
    sys.exit(main())
