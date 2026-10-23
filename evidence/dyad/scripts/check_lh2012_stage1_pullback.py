#!/usr/bin/env python3
"""Receiving check of the stage-1 pullback, pinned to the reviewed owner bytes.

Original mode must exit 1 at the identified jet-fidelity gates.
--diagnostic-delay-cut applies a one-line repair IN MEMORY ONLY; expected exit 0.
No owner file is edited. Uses the owner's exact coefficient arithmetic and raw
T^6 engine, with a different, direct coordinate-substitution route. It is not
an independent primitive engine or an infinite-order analytic certificate.

Run:
 python -I -B check_stage1_pullback.py --source PATH --out RESULT.json
 python -I -B check_stage1_pullback.py --source PATH --diagnostic-delay-cut --out FIX.json
"""
import argparse
import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys

PIN='c3c110543e0ea768109377de8781a9849dd9b61caf89195c1075561b91112cc4'
OLD='Fzl = Ser(FzS.d, 7, NY).compose(Xb, W2); Fwl = Ser(FwS.d, 7, NY).compose(Xb, W2)'
NEW='Fzl = FzS.compose(Xb, W2); Fwl = FwS.compose(Xb, W2)'


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',required=True)
    ap.add_argument('--out',required=True)
    ap.add_argument('--diagnostic-delay-cut',action='store_true')
    args=ap.parse_args()
    path=Path(args.source).resolve(); out=Path(args.out).resolve()
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=PIN:
        raise ValueError('owner source differs from reviewed pin')
    text=raw.decode('utf-8')
    if text.count(OLD)!=1 or text.count('return 0 if ok else 1')!=1:
        raise ValueError('diagnostic transform is not exact-once')
    if args.diagnostic_delay_cut:
        text=text.replace(OLD,NEW)
    # Expose the owner's computed jets for cross-checking. Do not alter its gates.
    text=text.replace('return 0 if ok else 1','return locals()')
    ns={'__name__':'receiving_diagnostic','__file__':str(path)}
    sys.path.insert(0,str(path.parent))
    exec(compile(text,str(path),'exec'),ns)
    saved=sys.argv[:]
    try:
        sys.argv=[str(path),'--out',str(out.with_suffix('.owner.json'))]
        with contextlib.redirect_stdout(io.StringIO()):
            local=ns['main']()
    finally:
        sys.argv=saved
    Ser,Ec,E_,Qs=(ns[n] for n in ['Ser','Ec','E_','Qs'])
    a=ns['A_E']; alpha=ns['ALPHA']; b1=local['a3'];b2=local['a4']
    c=local['Cc'];cinv=local['Cinv']
    X=local['X'];Y=local['Yv']
    # One direct substitution into the FULL degree-seven raw jet:
    # z=xi/c, w=(xi/c)^2*(a+b1*xi/c+Y). Cut output, not raw w powers.
    xx=Ser({(1,0):Ec.c(1)},7,2)
    yy=Ser({(0,1):Ec.c(1)},7,2)
    z=xx*cinv;w=z*z*(Ec.c(a)+z*Ec.c(b1)+yy)
    znext=local['FzS'].compose(z,w)
    wnext=local['FwS'].compose(z,w)
    def divide_x(s,power):
        if any(i<power for i,j in s.d):
            raise ValueError('direct pullback lacks required divisibility')
        return Ser({(i-power,j):v for (i,j),v in s.d.items()},5,2)
    direct1=(znext*c).trunc(5,2)
    ratio=divide_x(znext*c,1)
    t=ratio-1
    ratio_inv_square=1-2*t+3*t*t
    direct2=(divide_x(wnext,2)*c*c*ratio_inv_square
             -Ec.c(a)-znext.trunc(5,2)*Ec.c(b1))
    expected=Ec.c((alpha-2)*b2)*cinv*cinv
    d13=local['Fw'][(1,3)]
    monomial=Ec.c(E_(d13)*a*a*a)
    for _ in range(5):monomial=monomial*cinv
    psi0=local['F2'].coef(5,0)
    # Compare the returned inverse against the direct true-map jet.
    Ix,Iy=local['Ix'],local['Iy']
    inverse_matches=(direct1.compose(Ix,Iy)==X and direct2.compose(Ix,Iy)==Y
                     and Ix.compose(direct1,direct2)==X and Iy.compose(direct1,direct2)==Y)
    gates={
        'P0_owner_gates_all_pass':all(local['G'].values()),
        'P1_horizontal_direct_match':local['F1']==direct1,
        'P2_vertical_direct_match':local['F2']==direct2,
        'P3_graph_psi_relation':psi0==expected,
        'P4_direct_graph_psi_relation':direct2.coef(5,0)==expected,
        'P5_owner_inverse_of_actual_jet':inverse_matches,
    }
    changes=[]
    for ij in sorted(set(local['F2'].d)|set(direct2.d)):
        if local['F2'].coef(*ij)!=direct2.coef(*ij):
            changes.append({'monomial':list(ij),'owner':repr(local['F2'].coef(*ij)),
                            'direct':repr(direct2.coef(*ij)),
                            'direct_minus_owner':repr(direct2.coef(*ij)-local['F2'].coef(*ij))})
    result={
        'source_sha256':PIN,
        'diagnostic_delay_cut':args.diagnostic_delay_cut,
        'owner_gates':local['G'],
        'receiving_gates':gates,
        'all_pass':all(gates.values()),
        'd13':repr(d13),
        'b1':repr(b1),'b2':repr(b2),
        'owner_psi0':repr(psi0),'graph_expected_psi0':repr(expected),
        'direct_psi0':repr(direct2.coef(5,0)),
        'omitted_contribution':repr(monomial),
        'defect_equals_omitted':expected-psi0==monomial,
        'changed_vertical_coefficients':changes,
        'scope':'finite exact jet; shared primitive engine and field arithmetic, separate direct coordinate route',
    }
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    for gate,passed in gates.items():print(gate,'PASS' if passed else 'FAIL')
    print('RESULT','PASS' if result['all_pass'] else 'FAIL')
    return 0 if result['all_pass'] else 1


if __name__=='__main__':
    try:sys.exit(main())
    except SystemExit:raise
    except Exception as exc:
        print('CRASH',type(exc).__name__,exc)
        sys.exit(3)
