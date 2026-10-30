#!/usr/bin/env python3
"""dyad_inbox_20261030_l902_chain.py -- exact check of the displayed decimal chain in the proof outline of
DYAD-THM-LPHASE-ROWA-REMAINDER (dyad-v6.4.22 L902), for the v6.4.23 [COR] (inbox item D3).

The proof outline displays: |r| <= 1.51632 q^{3/2}; bridge factor (1 - c_Q/20)^{-3/2} <= 1.06252; |r_m| <= 1.61112 Q^{3/2};
published ceiling 403/250. The certificate (DYAD-ART-LPHASE-ROWA) works with exact rationals and is not affected; the
question here is only whether each *displayed* number is an outward ceiling of the quantity it stands for when that
quantity is computed from the displayed component ceilings (1401/1000, 123/125, tau c'_Q, 0.50220, 157.58, c_Q).
Gates (exact Fractions; tau = 2/sqrt3 enters through the rational ceiling 11548/10000, checked by 3*tbar^2 >= 4):
  L1  the displayed 1.51632 is below the inner constant computed from the displayed ceilings with c'_Q = 0.36915 or
      0.36916 (so it is not an outward ceiling), and 1.51633 is an outward ceiling with c'_Q = 0.36916;
  L2  1.06252 is not a ceiling of (1 - 0.79246/20)^{-3/2} (1.06252^2 (1 - c_Q/20)^3 < 1), and 1.06253 is (> 1);
  L3  1.61112 is below the product of the displayed ceilings, and below the certificate's own exact C_* 1.6111209...
      (reported, read from the certificate's FIN data); 1.51633 * 1.06253 <= 1.61115 <= 403/250.
Proposed corrected chain: |r| <= 1.51633 q^{3/2}; factor <= 1.06253; |r_m| <= 1.61115 Q^{3/2} <= 403/250.
Usage: python -I -B dyad_inbox_20261030_l902_chain.py --out l902_chain.json [--control D]
--control D asserts the displayed 1.06252 as a ceiling (L2 must fail, exit 1). Exit 0 all pass; 1 otherwise.
"""
import sys, json, argparse
sys.dont_write_bytecode = True
from fractions import Fraction as F


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--out', default='l902_chain.json'); ap.add_argument('--control', choices=['D'])
    o = ap.parse_args()
    tb = F(11548, 10000); cQ = F(79246, 100000)
    def inner(cqp): return F(1401, 1000) + (F(123, 125) + tb * cqp + F(50220, 100000)) / 20 + F(15758, 100) / 8000
    i15, i16 = inner(F(36915, 100000)), inner(F(36916, 100000))
    Bd, Bn = F(106252, 100000), F(106253, 100000)
    Bclaim = Bd if o.control == 'D' else Bn
    g = {'tau_ceiling': 3 * tb * tb >= 4,
         'L1_displayed_1.51632_not_ceiling': i15 > F(151632, 100000) and i16 > F(151632, 100000),
         'L1_1.51633_ceiling_with_0.36916': i16 <= F(151633, 100000),
         'L2_displayed_1.06252_not_ceiling': Bd * Bd * (1 - cQ / 20) ** 3 < 1,
         'L2_bridge_ceiling_claimed': Bclaim * Bclaim * (1 - cQ / 20) ** 3 >= 1,
         'L3_displayed_1.61112_below_product': i16 * Bn > F(161112, 100000),
         'L3_corrected_chain': F(151633, 100000) * Bn <= F(161115, 100000) <= F(403, 250)}
    g = {k: bool(v) for k, v in g.items()}
    info = {'tau_ceiling': str(tb), 'inner_with_0.36915': '%.10f' % float(i15), 'inner_with_0.36916': '%.10f' % float(i16),
            'bridge_with_0.79246_exact_float': '%.10f' % ((1 - float(cQ) / 20) ** -1.5),
            'product_displayed_ceilings': '%.10f' % float(i16 * Bn), 'product_1.51633x1.06253': '%.10f' % float(F(151633, 100000) * Bn),
            'certificate_exact_C_star_reported': '1.6111209628541905 (DYAD-ART-LPHASE-ROWA FIN data; owner_checks.json O7)',
            'proposed_chain': '|r| <= 1.51633 q^{3/2}; factor <= 1.06253; |r_m| <= 1.61115 Q^{3/2} <= 403/250'}
    ok = all(g.values())
    for k in sorted(g): print(k, 'PASS' if g[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL')
    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': g, 'info': info, 'all_pass': ok, 'control': o.control, 'script': 'dyad_inbox_20261030_l902_chain.py'},
                  f, indent=1, sort_keys=True); f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
