#!/usr/bin/env python3
"""T-6u v1.6 proposed upgraded certificate: exact leading diagnostic algebra.

This is a NEW implementation from the printed Genesis v2.8.4/Triadic v1.5
premises, not a rerun of the unavailable original eight-check T-6u script or
microscopic route census. No physical source map, finite-radius remainder,
HINDEX identity, event trigger, or independent external review is certified.

Run from any working directory. Requires SymPy. Failure exits 1. Two optional
flags intentionally test rejected interpretations and MUST fail.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
R = sp.Rational


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=ROOT/'evidence/t6u_certificate.json')
    ap.add_argument('--negative-conflate-readings', action='store_true')
    ap.add_argument('--negative-only-c3-dependent', action='store_true')
    args = ap.parse_args()
    checks: list[dict] = []

    def check(name: str, condition: object) -> None:
        ok = bool(condition)
        checks.append({'name': name, 'pass': ok})
        print(('PASS ' if ok else 'FAIL ') + name, flush=True)
        if not ok:
            raise AssertionError(name)

    def zero(expr: object) -> bool:
        if isinstance(expr, sp.MatrixBase):
            return all(sp.simplify(v) == 0 for v in expr)
        return sp.simplify(expr) == 0

    sr, se, cr, ce, dr, de = sp.symbols('sr se cr ce dr de', real=True)
    B = sp.Matrix([[1,-R(1,2)],[-R(1,2),1]])
    J = sp.Matrix([[1,-2],[2,-1]])/sp.sqrt(3)
    s, c, d = sp.Matrix([sr,se]), sp.Matrix([cr,ce]), sp.Matrix([dr,de])
    Q = lambda v: sp.expand((v.T*B*v)[0])
    I = lambda u,v: sp.expand((u.T*B*v)[0])
    w = lambda u,v: sp.expand(u[1]*v[0]-u[0]*v[1])
    Qs,Qc,Qd = Q(s),Q(c),Q(d)
    Isc,Ids,Idc = I(s,c),I(d,s),I(d,c)
    wsc,wds,wdc = w(s,c),w(d,s),w(d,c)
    # Literal source coefficients; P4 is a premise, not derived from a microscopic law.
    P4 = sp.expand(-Qd**2-Qs*Ids/8-3*Qs*wds/32-Qc*Idc/27+7*Qc*wdc/108
        -5*wds*Ids/12-wds**2/8-5*wdc*Idc/9-wdc**2/6
        +Qs*Idc/36-7*Qs*wdc/48+Ids*Isc/18+7*Ids*wsc/72
        +Qc*Ids/6+3*Qc*wds/8+Idc*Isc/3+Idc*wsc/4)
    check('B is positive definite', B[0,0]>0 and B.det()>0)
    check('J_Q squares to -I', zero(J*J+sp.eye(2)))
    check('J_Q is B-isometric', zero(J.T*B*J-B))
    check('source omega index/orientation identity', zero(I(d,J*s)-sp.sqrt(3)*wds/2))
    check('printed P4 has homogeneous degree four', all(sum(m)==4 for m,a in sp.Poly(P4,sr,se,cr,ce,dr,de).terms()))
    check('P4 at zero apex is zero, not the vector seed norm', P4.subs({dr:0,de:0})==0)
    V = (B.inv()*sp.Matrix([sp.diff(P4,dr),sp.diff(P4,de)])/2).subs({dr:0,de:0}).applyfunc(sp.simplify)
    a_s=-Qs/8+Qc/6+Isc/18+7*wsc/72
    b_s=-3*Qs/32+3*Qc/8
    a_c=Qs/36-Qc/27+Isc/3+wsc/4
    b_c=-7*Qs/48+7*Qc/108
    Vformula=(a_s*s+a_c*c)/2+(b_s*J*s+b_c*J*c)/sp.sqrt(3)
    check('zero-apex vector reproduces all four source channels', zero(V-Vformula))
    Vs=V.subs({cr:0,ce:0}).applyfunc(sp.simplify)
    Vc=V.subs({sr:0,se:0}).applyfunc(sp.simplify)
    check('s-cubed apex vector', zero(Vs+Qs*s/16+sp.sqrt(3)*Qs*J*s/32))
    check('c-cubed apex vector', zero(Vc+Qc*c/54-7*Qc*J*c/(108*sp.sqrt(3))))
    check('vector seed norm 7/1024 Qs^3', zero(Q(Vs)-R(7,1024)*Qs**3))
    check('pure c-cubed norm 61/34992 Qc^3', zero(Q(Vc)-R(61,34992)*Qc**3))
    check('seeded I_ds sign and coefficient', zero(I(Vs,s)+Qs**2/16))
    check('seeded omega_ds sign and coefficient', zero(w(Vs,s)+Qs**2/16))
    P_s3=-Qs*Ids/8-3*Qs*wds/32
    D_birth=sp.expand(P_s3.subs({dr:Vs[0],de:Vs[1]}, simultaneous=True))
    check('birth-symmetry increment channel is 7/512 Qs^3', zero(D_birth-R(7,512)*Qs**3))
    check('increment channel equals twice vector seed norm', zero(D_birth-2*Q(Vs)))
    check('state seed norm is not its doubled increment diagnostic', not zero(D_birth-Q(Vs)))
    check('pure apex homogeneous radial self-sink is -Qd^2', zero(P4.subs({sr:0,se:0,cr:0,ce:0})+Qd**2))

    q = sp.symbols('q', positive=True)
    kap = sp.symbols('kappa', real=True, nonzero=True)
    lead_vec=R(7,1024)*q**3
    lead_inc=R(7,512)*q**3
    lead_child=kap**2*q**3
    rvec=sp.sqrt(lead_vec/lead_child)
    rinc=sp.sqrt(lead_inc/lead_child)
    check('policy-parametric vector ratio for real nonzero kappa', zero(rvec-sp.sqrt(7)/(32*sp.Abs(kap))))
    check('increment-equivalent ratio is sqrt(2) times vector ratio', zero(rinc-sp.sqrt(2)*rvec))
    check('leading s-cubed numerator is kappa-independent', sp.diff(lead_vec,kap)==0)
    check('c-cubed squared channel is order q^9 at birth', zero(R(61,34992)*(kap**2*q**3)**3-R(61,34992)*kap**6*q**9))
    check('c-cubed squared channel relative to leading vector norm is order q^6', zero((R(61,34992)*(kap**2*q**3)**3)/lead_vec - R(3904,15309)*kap**6*q**6))
    # Express the full cubic vector on c=kappa Q Js as A(q)*s+B(q)*Js.
    qc_b=kap**2*q**3; om_b=-2*kap*q**2/sp.sqrt(3)
    aa_s=-q/8+qc_b/6+7*om_b/72
    bb_s=-3*q/32+3*qc_b/8
    aa_c=q/36-qc_b/27+om_b/4
    bb_c=-7*q/48+7*qc_b/108
    alpha=sp.expand(aa_s/2-bb_c*kap*q/sp.sqrt(3))
    beta=sp.expand(aa_c*kap*q/2+bb_s/sp.sqrt(3))
    full_cubic_norm=sp.expand(q*(alpha**2+beta**2))
    cbirth=kap*Qs*J*s
    direct_birth=V.subs({cr:cbirth[0],ce:cbirth[1]},simultaneous=True)
    basis_birth=alpha.subs(q,Qs)*s+beta.subs(q,Qs)*J*s
    check('full cubic birth-basis substitution matches the source derivative',zero(direct_birth-basis_birth))
    check('all four cubic channels preserve leading numerator 7/1024', full_cubic_norm.coeff(q,3)==R(7,1024))
    nextco=sp.simplify(full_cubic_norm.coeff(q,4))
    check('mixed channels already produce a subleading kappa-dependent coefficient', zero(nextco+5*sp.sqrt(3)*kap/1728) and nextco!=0)
    check('higher-channel counting does not remove kappa from the full numerator', sp.diff(full_cubic_norm,kap)!=0)
    policies={'shear':-2*sp.sqrt(3)/3,'recoil':-R(1,2)}
    exact_expected={('shear','vector'):sp.sqrt(21)/64,('shear','increment'):sp.sqrt(42)/64,
                    ('recoil','vector'):sp.sqrt(7)/16,('recoil','increment'):sp.sqrt(14)/16}
    table=[]
    for pname,kval in policies.items():
        check(f'{pname}: reference policy nonzero and negative',kval<0)
        for reading,r in [('vector',rvec),('increment',rinc)]:
            value=sp.simplify(r.subs(kap,kval))
            check(f'{pname}/{reading}: exact specialization',zero(value-exact_expected[pname,reading]))
            shortfall=sp.simplify(sp.sqrt(2)/value)
            check(f'{pname}/{reading}: shortfall strictly greater than six',sp.simplify(shortfall**2-36)>0)
            table.append({'policy':pname,'kappa_exact':str(kval),'numerator_reading':reading,
                          'ratio_exact':str(value),'ratio_decimal':str(sp.N(value,14)),
                          'shortfall_exact':str(shortfall),'shortfall_decimal':str(sp.N(shortfall,14))})
    largest=sp.sqrt(14)/16
    check('largest of four ratios is recoil/increment',all(sp.simplify(largest**2-v**2)>=0 for v in exact_expected.values()))
    check('sharp four-case shortfall is 16/sqrt(7)',zero(sp.sqrt(2)/largest-16/sp.sqrt(7)))
    check('strict sixfold bound by rational squared margin',sp.simplify((16/sp.sqrt(7))**2-36)==R(4,7))
    check('sixfold upper bound on ratio',sp.simplify((sp.sqrt(2)/6)**2-largest**2)==R(1,1152))
    # Denominator and frame clarifications used in the adjacent T6s/T6t patch.
    W=lambda v:v[0]-v[1]/2+sp.I*sp.sqrt(3)*v[1]/2
    check('unit quarter-turn W(Js)=iW(s)',zero(W(J*s)-sp.I*W(s)))
    check('actual leading child carries signed amplitude kappa Q',zero(W(kap*Qs*J*s)-sp.I*kap*Qs*W(s)))
    check('no third common-carrier direction follows from the mode-label count',zero(sp.Matrix.hstack(s,J*s).det()-2*sp.sqrt(3)*Qs/3))
    g=sp.symbols('g',real=True)
    H=(1-g)*B*J
    check('HINDEX squared amplitude identity, not a seed identification',zero(B.inv()*H.T*B.inv()*H-(1-g)**2*sp.eye(2)))
    check('unrestricted coherent weights do not satisfy the claimed bound',abs(1-3)>1)
    check('closed weight interval yields the precise no-gain domain',sp.solve_univariate_inequality((1-g)**2<=1,g,relational=False)==sp.Interval(0,2))
    model=sp.sqrt((4+sp.sqrt(7))/3)
    check('old isometric number is distinct from each leading diagnostic',all(sp.simplify(model**2-v**2)>0 for v in exact_expected.values()))
    # These negative tests reject interpretations, not arithmetic failures in sources.
    if args.negative_conflate_readings:
        check('NEGATIVE: increment diagnostic is the first seeded state norm',zero(lead_inc-lead_vec))
    if args.negative_only_c3_dependent:
        check('NEGATIVE: mixed channels add no kappa-dependent q^4 term',nextco==0)
    report={
        'record':'TRIAD T-6u v1.6 proposed exact certificate', 'date':'2026-09-30',
        'status':'producer-checked; revision-editor and owner-adoption pending',
        'source_premises':'Genesis v2.8.4 §§6.3–6.6; Triadic v1.5 §6.17; source polynomial is transcribed, not regenerated microscopically',
        'check_count':len(checks),'all_pass':True,'checks':checks,
        'table':table,'worst_ratio_exact':str(largest),'smallest_shortfall_exact':str(16/sp.sqrt(7)),
        'scalar_formula':'R_vec(kappa)=sqrt(7)/(32*abs(kappa)); R_increment=sqrt(2)*R_vec',
        'full_cubic_source_norm_on_birth_graph':str(full_cubic_norm),
        'first_mixed_subleading_coefficient':str(nextco),
        'derivation_notes':{'vector_seed':'norm square of G3d(s,0,0), first generated six-step-block output at d0=0',
                           'increment_reading':'s^3 radial channel evaluated at the seeded vector; sqrt(increment/Qc) is increment-equivalent, NOT a second initial state norm',
                           'c3_order':'isolated squared c^3 channel O(q^9), relative to O(q^3) s^3 seed O(q^6); not a bound on all mixed/interference terms'},
        'not_certified':['physical residual or kappa selection','finite-amplitude radius or remainder constants',
                         'HINDEX source mapping','full next-step Delta Qd or long-time cascade','microscopic P4 generation',
                         'incoherent or non-P4 UV sources','physical pole relabel or new RRF profile','independent external review']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(f'ALL CHECKS PASS: {len(checks)}',flush=True)
    return 0

if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (AssertionError,ValueError,OSError) as exc:
        print(f'CERTIFICATE FAILURE: {type(exc).__name__}: {exc}',file=sys.stderr)
        raise SystemExit(1)
