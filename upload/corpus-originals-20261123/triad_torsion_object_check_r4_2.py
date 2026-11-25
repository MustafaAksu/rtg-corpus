#!/usr/bin/env python3
"""Exact r4.2 object-typing check for the supplied T-6l producer.

Uses the producer's unmodified input/coefficient assignments (via its AST),
then independently performs numerator, angular division and coefficient tests.
No microscopic T-6a1/T-6c2/T-6e extraction or trajectory is rerun. The pinned
15-check normalization audit is not edited or imported. No new RID is assigned.
"""
from __future__ import annotations
import argparse, ast, hashlib, json, sys
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'inputs/recovered_producers/triad_analytic_phase_steering_t6l_patched.py'
AUDIT=ROOT/'scripts/triad_orientation_normalization_audit.py'

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--negative-keep-K-in-rate',action='store_true')
    args=parser.parse_args(); checks=[]
    def check(label,condition):
        ok=bool(condition);checks.append({'name':label,'pass':ok})
        print(('PASS ' if ok else 'FAIL ')+label,flush=True)
        if not ok:raise AssertionError(label)
    check('A1 recovered T-6l source bytes',hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='2e0317bf90332d1fe0ab7489710a3c8c67b772e3031dd7ef95b3163f7d7a11cd')
    check('A2 pinned N4a audit bytes unchanged',hashlib.sha256(AUDIT.read_bytes()).hexdigest()=='d5c0f698232cca6c2fe5d8321249e5d93f9bfe2c5288c7f918c3ef55d89a0e29')
    tree=ast.parse(SOURCE.read_text()); fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='run_analytic_theta_extraction')
    stop=next(i for i,n in enumerate(fn.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='numerator_raw' for t in n.targets))
    ret=ast.parse('return Qs,u,mu,nu,K,DIsc,Dwsc').body[0]
    getter=ast.FunctionDef(name='get_source_coefficients',args=fn.args,body=fn.body[:stop]+[ret],decorator_list=[])
    mod=ast.fix_missing_locations(ast.Module(body=[getter],type_ignores=[])); ns={'sp':sp}
    exec(compile(mod,str(SOURCE)+':coefficient-prefix','exec'),ns)
    Qs,u,mu,nu,K,DI,Dw=ns['get_source_coefficients']()
    v=sp.symbols('v',positive=True);Kstate=mu**2+nu**2;rt=sp.sqrt(3)
    def coefficient(f):
        expanded=sp.expand(sp.simplify(f.subs(sp.sqrt(u),v).subs(u,v**2)))
        return sp.factor(sp.Poly(expanded,v).coeff_monomial(v**2))
    scale=Qs**2*sp.sqrt(u)
    oldN=coefficient((mu*Dw-nu*DI)/scale)
    newN=coefficient((mu*(-rt*Dw)-nu*DI)/scale)
    oldA=sp.simplify(coefficient((mu*Dw-nu*DI)/(K*scale)).subs(K,Kstate))
    newA=sp.simplify(coefficient((mu*(-rt*Dw)-nu*DI)/(K*scale)).subs(K,Kstate))
    oldExpected=-3*mu**2+(21+5*rt)*mu*nu+9*rt*nu**2
    H=rt*mu**2+2*mu*nu+3*rt*nu**2
    # General amplitude cancellation explains the denominator independently of
    # the radial ledger values, which are not used in this angular calculation.
    b,di,dw,db=sp.symbols('b di dw db',real=True,nonzero=True)
    dmu=di/b-mu*db/b;dnu=dw/b-nu*db/b
    check('A3 amplitude derivative cancels from the angular numerator',sp.expand(mu*dnu-nu*dmu-(mu*dw-nu*di)/b)==0)
    check('A4 historical numerator equals K times archived rate coefficient',sp.simplify(oldN-Kstate*oldExpected)==0)
    check('A5 producer historical angular-rate coefficient reproduced',sp.simplify(oldA-oldExpected)==0)
    check('A6 N4a object is corrected numerator coefficient 3K H',sp.simplify(newN-3*Kstate*H)==0)
    check('A7 actual angular-rate coefficient is 3H',sp.simplify(newA-3*H)==0)
    check('A8 division by K commutes with large-u extraction',sp.simplify(newN/Kstate-newA)==0)
    square=3*rt*(mu+nu/rt)**2+8*rt*nu**2
    check('A9 positive sum-of-squares identity',sp.expand(newA-square)==0)
    matrix=sp.Matrix([[rt,1],[1,3*rt]])
    check('A10 strict positivity of H away from origin',matrix[0,0]>0 and matrix.det()==8)
    x=sp.symbols('x',real=True)
    ratio=sp.simplify(newA.subs(nu,x*mu)/mu**2)
    check('A11 historical-normalization ratio polynomial unchanged',sp.expand(ratio-(9*rt*x*x+6*x+3*rt))==0)
    check('A12 ratio discriminant exactly minus288',sp.discriminant(ratio,x)==-288)
    check('A13 mu=0 not covered by ratio but has positive angular coefficient',sp.expand(newA.subs(mu,0)-9*rt*nu**2)==0)
    quarter={mu:sp.Rational(1,2),nu:0};four={mu:2,nu:0}
    check('A14 off-boundary K=1/4 distinguishes numerator from angular rate',sp.simplify(newN.subs(quarter)-3*rt/16)==0 and sp.simplify(newA.subs(quarter)-3*rt/4)==0)
    check('A15 off-boundary K=4 distinguishes numerator from angular rate',sp.simplify(newN.subs(four)-48*rt)==0 and sp.simplify(newA.subs(four)-12*rt)==0)
    oncircle={mu:sp.Rational(3,5),nu:sp.Rational(4,5)}
    check('A16 K=1 masks the distinction numerically',sp.simplify((newN-newA).subs(oncircle))==0)
    lam=sp.symbols('lambda',real=True)
    check('A17 rate is degree two while its numerator is degree four in mu,nu',sp.expand(newA.subs({mu:lam*mu,nu:lam*nu},simultaneous=True)-lam**2*newA)==0 and sp.expand(newN.subs({mu:lam*mu,nu:lam*nu},simultaneous=True)-lam**4*newN)==0)
    if args.negative_keep_K_in_rate:
        check('NEGATIVE: retain numerator K as angular-rate factor off K=1',sp.simplify(newN.subs(quarter)-newA.subs(quarter))==0)
    report={'record':'r4.2 numerator/angular-rate distinction','date':'2026-10-05','checks':checks,'check_count':len(checks),'all_pass':True,
      'producer_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'historical_numerator':str(oldN),'historical_angular_rate':str(oldA),
      'corrected_numerator':str(newN),'corrected_angular_rate':str(newA),'ratio_polynomial':str(ratio),
      'domain':'Qs>0,u>0,r=0,K=mu^2+nu^2>0; ratio x additionally requires mu!=0. K=1 not imposed.',
      'method':'Source coefficient/input AST prefix; independent rate normalization and exact coefficient extraction. No raw radial or microscopic generator re-extraction.',
      'adoption':False}
    (ROOT/'evidence/TORSION_OBJECT_CHECKS_R4_2.json').write_text(json.dumps(report,indent=2)+'\n')
    print('RESULT',len(checks),'PASS')
    return 0
if __name__=='__main__':
    try:raise SystemExit(main())
    except (AssertionError,ValueError,OSError) as exc:
        print('TORSION CHECK FAILURE:',type(exc).__name__,str(exc),file=sys.stderr);raise SystemExit(1)
