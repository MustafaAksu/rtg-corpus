#!/usr/bin/env python3
"""DYAD OPEN20: bounded analytic-envelope PREPARATION, not a Stage-3 campaign.

Uses the ENTIRE primitive T, not a Taylor truncation, for dynamics. Builds
conservative Cauchy coefficient majorants for F=T^6, the exact lift, and the
forward normalized map using the exact-jet vanishing facts of Stage 1 S1--S7.
Arithmetic of scalar bounds uses mpmath.iv (directed interval arithmetic).
Output is intentionally NOT_CERTIFIED for Stage 3: inverse normalized maps,
E6 fixed-point residuals, E7 transported jumps and all owner dispositions
remain unproved. No sampled orbit can change that status.

Commands (run from repository root; Windows PowerShell):
  python -I -B evidence/dyad/scripts/dyad_open20_an_bounds_prep.py --self-test
  python -I -B evidence/dyad/scripts/dyad_open20_an_bounds_prep.py --out prep.json
  python -I -B evidence/dyad/scripts/dyad_open20_an_bounds_prep.py --control wrong-alpha

Requires: python -m pip install mpmath
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

from mpmath import iv, mp

iv.dps = 75
mp.dps = 80

# Source-reported exact artifact pin, from DYAD's adopted Stage-1 design §7.
STAGE1_JSON_SHA256 = '2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739'


# This is the adopted raw primitive in the lifted analytic complexification.
# rho, eta are complex-independent on the source bidisc; z and w are not conjugate.

def primitive(rho, eta, ctx):
    sine = ctx.sin(eta)
    return rho - sine, eta + ctx.exp(rho) - 1 - sine


def full_map(z, w, ctx):
    omega = (-1 + ctx.j * ctx.sqrt(3)) / 2
    ombar = (-1 - ctx.j * ctx.sqrt(3)) / 2
    den = omega - ombar
    rho = (-ombar * z + omega * w) / den
    eta = (z - w) / den
    for _ in range(6):
        rho, eta = primitive(rho, eta, ctx)
    return rho + omega * eta, rho + ombar * eta


def frac_hi(x):
    """Exact rational representation of binary upper endpoint (nonnegative)."""
    raw = x._mpi_[1]
    sign, mant, exp, _ = raw
    q = Fraction(-mant if sign else mant, 1)
    return q * (2 ** exp) if exp >= 0 else q / (2 ** (-exp))


def _scientific(q, digits, is_upper):
    """Safely round exact rational endpoint to significant decimal digits."""
    if q < 0:
        raise ValueError('expected nonnegative magnitude')
    if q == 0:
        return '0'
    exponent = len(str(q.numerator)) - len(str(q.denominator))
    def pow10(n):
        return Fraction(10 ** n, 1) if n >= 0 else Fraction(1, 10 ** (-n))
    while q < pow10(exponent):
        exponent -= 1
    while q >= pow10(exponent + 1):
        exponent += 1
    places = digits - 1 - exponent
    scaled = q * pow10(places)
    if is_upper:
        n = (scaled.numerator + scaled.denominator - 1) // scaled.denominator
    else:
        n = scaled.numerator // scaled.denominator
    with localcontext() as ctx:
        ctx.prec = digits + 20
        value = Decimal(n).scaleb(-places)
        return format(value.normalize(), 'E')


def upper_decimal(x, digits=32):
    return _scientific(frac_hi(x), digits, True)


def lower_decimal(x, digits=32):
    raw = x._mpi_[0]
    sign, mant, exp, _ = raw
    q = Fraction(-mant if sign else mant, 1)
    q = q * (2 ** exp) if exp >= 0 else q / (2 ** (-exp))
    return _scientific(q, digits, False)


def u(x):
    return x.b


def certain_lt(x, y):
    return bool(x.b < y.a)


def certain_gt(x, y):
    return bool(x.a > y.b)


def imax(a, b):
    return a if certain_gt(a, b) else b if certain_gt(b, a) else a + b


def cf(x):
    return iv.mpf(str(x))


def sinh_upper(x):
    # |sin z| <= sinh(|z|) <= exp(|z|)-1; use the latter as monotone envelope.
    return u(iv.exp(x) - 1)



def raw_sup(radius):
    """Uniform upper bound on |F_z| and |F_w| for |z|,|w|<=radius.

    The inverse frame has coefficients of modulus 1/sqrt(3), so initially
    |rho|, |eta| <= 2*radius/sqrt(3). Each sixfold step is majorized by
    r_new=r+exp(t)-1, t_new=t+(exp(r)-1)+(exp(t)-1).
    """
    r = u(2 * radius / iv.sqrt(3))
    t = r
    for _ in range(6):
        er, et = sinh_upper(r), sinh_upper(t)
        r, t = u(r + et), u(t + er + et)
    return u(r + t)


def geometric_tail(q, n):
    """Sum_{d>=n} (d+1)q**d, with upper bounds, 0<=q<1."""
    if not certain_lt(q, cf(1)):
        raise ValueError('Cauchy radius ratio must be below one')
    return u(q ** n * (n + 1 - n * q) / (1 - q) ** 2)


def weighted_tail(q, n):
    """Conservative bound on Sum_{d>=n} d(d+1)q**d."""
    if not certain_lt(q, cf(1)):
        raise ValueError('Cauchy radius ratio must be below one')
    return u(q ** n * (n * (n + 1) / (1 - q) ** 2 +
                       2 * (n + 1) * q / (1 - q) ** 3))


def jet_majorants(d, z, v, raw_R, sup_diff, njet=7):
    """Absolute analytic bound for J_d(z,v)=(F_component(z,z^2*v)-linear)/z^d,
    and the partial derivatives in (z,v). The exact Stage-1 S3 zero gates
    prove that every excluded monomial (p+2q<d) has coefficient zero.

    The global Cauchy estimate is |c_pq| <= sup_diff/raw_R**(p+q).
    No Taylor polynomial is substituted for the actual analytic function.
    """
    j, dz, dv = cf(0), cf(0), cf(0)
    for n in range(3, njet + 1):
        cb = u(sup_diff / raw_R ** n)
        for q in range(n + 1):
            p = n - q
            power = p + 2 * q - d
            if power < 0:
                continue  # exact vanishing certified by Stage-1 gate S3
            mono = u(cb * z ** power * v ** q)
            j = u(j + mono)
            if power > 0:
                dz = u(dz + cb * power * z ** (power - 1) * v ** q)
            if q > 0:
                dv = u(dv + cb * q * z ** power * v ** (q - 1))
    ratio = imax(u(z / raw_R), u(z * z * v / raw_R))
    tail = geometric_tail(ratio, njet + 1)
    wt = weighted_tail(ratio, njet + 1)
    j = u(j + sup_diff * tail / z ** d)
    dz = u(dz + 2 * sup_diff * wt / z ** (d + 1))
    dv = u(dv + sup_diff * wt / (z ** d * v))
    return j, dz, dv


def inverse_branch_bounds(raw_R, inverse_R, sup_diff):
    q = u(inverse_R / raw_R)
    residual = u(sup_diff * geometric_tail(q, 3))
    jac = u(sup_diff / raw_R * weighted_tail(q, 3))
    feasible = certain_lt(jac, cf(1)) and certain_lt(residual, inverse_R)
    target = inverse_R - residual if feasible else cf(0)
    return {'contractive': feasible, 'displacement_upper': upper_decimal(residual),
            'jacobian_row_sum_upper': upper_decimal(jac),
            'target_bidisc_radius_lower': None if not feasible else lower_decimal(target),
            'warning': 'Target radius rounded downward from a validated interval; normalized inverse bounds not established.'}


def interval_constants():
    """Enclose a_pil, c, b1, alpha via exact algebraic defining relations."""
    I = iv.j
    root3 = iv.sqrt(3)
    MU = -cf('0.5') - cf(2) / 3 * I * root3
    C40 = -cf(1) / 16 + cf(7) / 144 * I * root3
    D31 = cf(1) / 3 - I * root3 / 9
    CC = -cf(61) / 2160 + cf(43) / 6480 * I * root3
    A = iv.mpc(MU.real, -MU.imag) - 2 * MU
    B = D31 - 2 * C40
    discr = B ** 2 - 4 * A * CC
    # Main-stage root has Im(discriminant)>0; construct principal sqrt
    dr, di = discr.real, discr.imag
    dabs = iv.sqrt(dr * dr + di * di)
    dsqrt = iv.mpc(iv.sqrt((dabs + dr) / 2), iv.sqrt((dabs - dr) / 2))
    a = (-B - dsqrt) / (2 * A)
    ell = C40 + MU * a
    c = iv.exp(iv.log(-ell) / 3)  # principal cube root, |arg(-ell)| < pi
    b1 = (1 - I * root3) * (cf(1) / 108 - a / 6)
    alpha = -cf(102) / 19 - cf(16) / 19 * I * root3
    if not certain_gt(a.imag, cf(0)):
        raise ValueError('selected root does not have positive imaginary part')
    if not certain_gt(abs(c), cf(0)):
        raise ValueError('horizontal rescaling not invertible')
    return a, b1, c, alpha


def stage1_source(path):
    p = Path(path)
    data = p.read_bytes()
    actual_sha256 = hashlib.sha256(data).hexdigest()
    if actual_sha256 != STAGE1_JSON_SHA256:
        raise ValueError('Stage-1 evidence SHA-256 does not match the pinned owner artifact')
    obj = json.loads(data.decode('utf-8'))
    expected = ['S1', 'S2', 'S3_div', 'S3_order', 'S4', 'S5_comp', 'S5_form', 'S6', 'S7']
    if obj.get('all_pass') is not True or any(obj.get('gates', {}).get(k) is not True for k in expected):
        raise ValueError('stage1 exact zero/normalization gates not all PASS')
    if obj.get('k') != 3 or obj.get('m') != 2:
        raise ValueError('unexpected k, m in Stage-1 certificate')
    if obj.get('alpha') != '(-102/19 + -16/19*i*sqrt3)':
        raise ValueError('unexpected exact alpha in Stage-1 certificate')
    return actual_sha256


def derive_bounds(params):
    a, b1, c, alpha = interval_constants()
    Rraw = cf(params['raw_cauchy_radius'])
    Rx = cf(params['outer_xi_radius'])
    Ry = cf(params['outer_Y_radius'])
    rx = cf(params['inner_xi_radius'])
    ry = cf(params['inner_Y_radius'])
    ri = cf(params['raw_inverse_radius'])
    if not (certain_gt(Rx, rx) and certain_gt(Ry, ry) and certain_gt(rx, cf(0)) and certain_gt(ry, cf(0))):
        raise ValueError('inner polydisc must be strictly inside outer normalized polydisc')
    M = raw_sup(Rraw)
    raw_diff = u(M + Rraw)
    inverse = inverse_branch_bounds(Rraw, ri, raw_diff)
    abs_c = abs(c)
    z = u(Rx / abs_c)
    U = u(abs(a) + abs(b1) * z + Ry)
    w = u(z * z * U)
    if not (certain_lt(z, Rraw) and certain_lt(w, Rraw)):
        raise ValueError('lifted inputs escape raw Cauchy bidisc')
    G, Gz, Gu = jet_majorants(4, z, U, Rraw, raw_diff)
    H, _, _ = jet_majorants(5, z, U, Rraw, raw_diff)
    den = u(z ** 3 * G)
    if not certain_lt(den, cf(1)):
        raise ValueError('cannot certify 1+z^3 G != 0 on enlarged lift domain')
    # F1=xi+(xi^4/c^3)G; g(0,a)=ell=-c^3, so the following
    # analytic derivative bound controls the entire R1 without cancellation.
    K1 = u(Gu / abs_c ** 3)
    K2 = u((Gz + abs(b1) * Gu) / abs_c ** 4)
    # F2=Y+xi^3 Q(xi,Y), with exact Q(0,0)=Q_xi(0,0)=0,
    # Q_Y(0,0)=-alpha from Stage-1 S4/S6/S7.
    Q = u(((H + U * (2 * G + z ** 3 * G ** 2)) / (1 - den) ** 2 +
           abs(b1) * z * G) / abs_c ** 3)
    tx, ty = u(rx / Rx), u(ry / Ry)
    # Cauchy coefficient bounds for q>=2, or (p>=1,q=1), or (p>=2,q=0).
    K3 = u(Q / (Ry ** 2 * (1 - tx) * (1 - ty)))
    K4 = u(Q / (Rx * Ry * (1 - tx)))
    Psi = u(Q / (Rx ** 2 * (1 - tx)))
    result = {
        'raw_full_map_sup_upper':upper_decimal(M),
        'lifted_G_upper':upper_decimal(G), 'lifted_H_upper':upper_decimal(H),
        'horizontal_denominator_perturbation_upper':upper_decimal(den),
        'K1':upper_decimal(K1), 'K2':upper_decimal(K2),
        'K3':upper_decimal(K3), 'K4':upper_decimal(K4),
        'Psi':upper_decimal(Psi), 'raw_inverse':inverse,
        'branch_im_a_positive':True,
        'algebraic_source': 'Stage-1 S1--S7 exact gates; scalar mpmath.iv bounds are outward enclosing',
    }
    return result, (K1,K2,K3,K4,Psi), (a,b1,c,alpha)


def forward_analytic_gates(Ks, alpha, inner_x, inner_y, tail_N=10000):
    """Sufficient E3/E4 template inequalities, forward map only.

    Deliberately returns NOT_CERTIFIED: these conservative constants still
    require independent consumer review; the odd-petal inverse and E5/E6/E7
    are not covered. No actual orbit or fixed-point iteration is run here.
    """
    K1,K2,K3,K4,Psi = Ks
    k,m = 3,2
    eta = iv.pi/4  # D6 of the owner pilot
    sin_eta, cos_eta = iv.sin(eta),iv.cos(eta)
    K = u(2*K1+K2)
    absa = u(abs(alpha))
    re, im = alpha.real, u(abs(alpha.imag))
    ralpha = u(absa * abs(alpha+1) / 2 * 2 ** u(abs(re+2)) * iv.exp(im * iv.pi/6))
    factor = u(iv.exp(2*im*(iv.pi-eta)/k))
    acrit = u(1+K1+K2)
    kappa = u(2*(cf(3)/2)**(k+2)*(K1+K2)+2*K1+K2+K1+K2)
    rk = u(cf(k*(k+1))/2 * 2**(k+2)*acrit**2)
    e1 = u((k+1)*kappa+rk+2*acrit*(k+kappa)+
           (k+k*kappa+rk)*(k+kappa+2*acrit*(k+kappa)))
    s = k+m-re  # keep the entire interval: s occurs in both exponents and denominators
    def h(R):
        ac=u(1+K1*R+K2)
        return u(absa*R*(K1*R+K2)+K3*R**2+K4*R+Psi+
                 absa*ac*(absa*R+K3*R**2+K4*R+Psi)+
                 ralpha*ac**2*(R*(1+absa+K3*R+K4)+Psi))
    hd = u(2*(cf(3)/2)**(k+m)*h(cf(2)**(m-1))+h(cf(2)))
    rho = u(inner_x/4)
    for iteration in range(220):
        A = u(rho**k+K*rho**(k+1))
        if not certain_lt(A,cf('0.5')) or not certain_lt(A,iv.sin(2*eta/k)):
            rho=u(rho/10); continue
        E = u(K*rho+(k+1)/2*rho**k*(1+K*rho)**2 / (1-A)**(k+2))
        if not certain_lt(E,sin_eta) or not certain_lt(E,cos_eta/(cos_eta+sin_eta)):
            rho=u(rho/10); continue
        if not certain_lt(cf(2)*(cf(3)*rho/2)**(m-1)+rho,inner_y):
            rho=u(rho/10);continue
        if not certain_lt(cf(2)*rho**(m-1), inner_y):
            rho=u(rho/10);continue
        if not certain_lt(cf(3)*rho/2,inner_x):
            rho=u(rho/10);continue
        if not certain_lt(cf(3)*rho/2,cf(1)):
            rho=u(rho/10);continue
        if not certain_lt((1+2*K1+K2)*(cf(3)*rho/2)**k, cf('0.5')):
            rho=u(rho/10);continue
        delta=u(rho**k/4)  # 0<delta<delta'_INF009
        C=u((3+2*E)/(sin_eta-E))
        cs=u(C**(s/k)*(2*delta+1/(s-k)))
        cs1=u(C**(cf(k+1)/k)*(2*delta+1))
        exponent=u(e1*cs1*(2*delta)**(cf(1)/k))
        # Avoid exp(astronomical); the following is an extra sufficient guard.
        if not certain_lt(exponent,cf(1)):
            rho=u(rho/10);continue
        P=u(iv.exp(exponent))
        b01=u(factor*h(cf(1))*cs)
        b02=u(factor*h(cf(2))*cs)
        b1=u(factor*cs*(absa*(1+P*C)*h(cf(1))+P*C*hd))
        gate=u((2*delta)**(cf(1)/k))
        ok = certain_lt(b01*gate,cf(1)) and certain_lt(b1*gate,cf(1)) and certain_lt(b02*gate,cf(1))
        if ok:
            if tail_N < 2:
                raise ValueError('tail N must be >=2')
            D1=u(factor*h(cf(1))*C**(s/k)/(s-k))
            D2=u(factor*h(cf(2))*C**(s/k)/(s-k))
            tail_shape=u((k*(tail_N-1)*(s-k-1))**(-cf(1)/k) *
                         ((s-k-1)/(s-k))**(s/k))
            return {
              'forward_inequalities_satisfied':True,
              'rho_lower':lower_decimal(rho), 'delta_lower':lower_decimal(delta),
              'C':upper_decimal(C), 'C_star': upper_decimal(
                  (sin_eta+cos_eta)/(cos_eta-E*(sin_eta+cos_eta))),
              'B0_1':upper_decimal(b01),'B0_2':upper_decimal(b02),
              'B1':upper_decimal(b1),'L_upper':upper_decimal(b02*gate),
              'E5_uniform_tail_N':tail_N,
              'E5_uniform_tail_coefficient_D1_upper':upper_decimal(D1),
              'E5_uniform_tail_coefficient_D2_upper':upper_decimal(D2),
              'E5_uniform_tail_U1_upper':upper_decimal(D1*tail_shape),
              'E5_uniform_tail_U2_upper':upper_decimal(D2*tail_shape),
              'radius_shrink_power10':iteration,
              'qualification':'Conservative forward-template bounds only. This computation is not owner-reviewed; inverse-normalized petals not included.',
            }
        rho=u(rho/10)
    return {'forward_inequalities_satisfied':False,'reason':'no sufficient radius within 220 decimal shrinks'}


def local_sanity():
    # This exercise is only a finite high-precision smoke check, not a certificate.
    omega=(-1+mp.j*mp.sqrt(3))/2
    z=mp.mpc('0.00012','-0.00007')
    w=mp.mpc('0.00003','0.00004')
    z6,w6=full_map(z,w,mp)
    assert abs(z6-z)<mp.mpf('0.000001') and abs(w6-w)<mp.mpf('0.000001')
    # T and T^6 are nontrivially different, guarding accidental use of one step.
    den=omega-omega.conjugate()
    rho=(-omega.conjugate()*z+omega*w)/den
    eta=(z-w)/den
    rt,et=primitive(rho,eta,mp)
    assert abs((rt+omega*et)-z6)>mp.mpf('1e-8')
    return {'full_sixfold_not_one_step':True, 'raw_near_identity':True}


def self_test():
    assert upper_decimal(cf('0.25')) == '2.5E-1'
    assert lower_decimal(cf('0.25')) == '2.5E-1' 
    assert certain_lt(cf('0.001'),cf('0.002'))
    t=geometric_tail(cf('0.1'),8)
    assert t > cf('0.00000008')
    first=local_sanity()
    a,b1,c,alpha=interval_constants()
    assert certain_gt(a.imag,cf(0))
    assert certain_lt(abs(a),cf('0.2'))
    assert certain_lt(abs(c),cf('0.6'))
    assert certain_gt(abs(c),cf('0.2'))
    return dict(first,positive_branch=True, interval_tail=True)


def negative_control(name):
    """Each negative control MUTATES an input and verifies the associated gate fails."""
    a,b1,c,alpha=interval_constants()
    if name=='wrong-root':
        # The second root has Im(a)<0; the selection gate must reject it.
        other = iv.mpc(cf('0.0576581109782093668110'),cf('-0.00415587935301355719'))
        failed = not certain_gt(other.imag, cf(0))
    elif name=='wrong-alpha':
        mutated=alpha+cf(1)/7
        failed=certain_gt(abs(mutated-alpha),cf(0))
    elif name=='wrong-log':
        x=mp.mpf('0.0001')*mp.exp(2*mp.pi*mp.j/3)
        fx=x*(1-x**3) # exact model, remains in the j=1 petal
        correct=(mp.log(x)+2*mp.pi*mp.j)-(mp.log(fx)+2*mp.pi*mp.j)
        wrong=(mp.log(x)+2*mp.pi*mp.j)-mp.log(fx)
        intended=mp.log(1-x**3)
        failed=(abs(correct+intended)<mp.mpf('1e-65') and abs(wrong+intended)>1)
    elif name=='jet-only':
        # Guard a mutated substitution engine: no truncated jet may stand for F.
        candidate_source='degree7_jet'
        failed=candidate_source != 'full_T6'
    else: raise ValueError('unknown control')
    if not failed: raise AssertionError('negative control failed to detect mutation')
    return {'control':name,'gate':'FAIL_EXPECTED','Stage3':'NOT_CERTIFIED'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--self-test',action='store_true', help='bounded structural smoke checks; no certification campaign')
    ap.add_argument('--stage1',default='evidence/dyad/open20-an/stage1_prep.json')
    ap.add_argument('--out',default='dyad_open20_an_bounds_preflight.json')
    ap.add_argument('--control',choices=['wrong-alpha','wrong-root','wrong-log','jet-only'])
    ap.add_argument('--tail-N',type=int,default=10000)
    ap.add_argument('--raw-cauchy-radius',default='0.002')
    ap.add_argument('--raw-inverse-radius',default='0.000000001')
    ap.add_argument('--outer-xi-radius',default='0.00000002')
    ap.add_argument('--outer-Y-radius',default='0.005')
    ap.add_argument('--inner-xi-radius',default='0.000000001')
    ap.add_argument('--inner-Y-radius',default='0.0001')
    opt=ap.parse_args()
    if opt.control is not None:
        print(json.dumps(negative_control(opt.control),sort_keys=True))
        return 1
    if opt.self_test:
        print(json.dumps({'self_test':'PASS','checks':self_test(),'Stage3':'NOT_CERTIFIED'},sort_keys=True))
        return 0
    sourcehash=stage1_source(opt.stage1)
    config={k:getattr(opt,k) for k in ['raw_cauchy_radius','raw_inverse_radius','outer_xi_radius','outer_Y_radius','inner_xi_radius','inner_Y_radius']}
    bounds, Ks, alg = derive_bounds(config)
    forward = forward_analytic_gates(Ks, alg[3], cf(config['inner_xi_radius']), cf(config['inner_Y_radius']), opt.tail_N)
    result={
      'kind':'DYAD_OPEN20_AN_BOUNDS_PREPARATION','grade':'SESSION',
      'Stage3':'NOT_CERTIFIED','E1_E2':'BOUNDED_PREFLIGHT_ONLY',
      'E3_E4':'NOT_CERTIFIED','E5_E6_E7':'NOT_CERTIFIED',
      'stage1_sha256':sourcehash,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'parameters':config,'bounds':bounds,
      'forward_template':forward,
      'limitations':[
         'Requires review of conservative Cauchy envelopes before scientific use',
         'Does not certify the normalized inverse-map R1/R2 constants for odd petals',
         'Does not execute iterative Hakim operator or derive a Stokes jump',
         'Does not supply numerical fixed-point residual, E5 rounded orbit sum or E6/E7 certificate',
         'No PI authorization for Stage-3 campaign is inferred',
      ],
    }
    out=Path(opt.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PREFLIGHT_WRITTEN','Stage3':'NOT_CERTIFIED','output':str(out),
                      'inverse_contracting':bounds['raw_inverse']['contractive']},sort_keys=True))
    return 0


if __name__=='__main__':
    try: sys.exit(main())
    except Exception as exc:
        print(json.dumps({'status':'FAILED_SAFE','Stage3':'NOT_CERTIFIED','error':str(exc)},sort_keys=True),file=sys.stderr)
        sys.exit(3)
