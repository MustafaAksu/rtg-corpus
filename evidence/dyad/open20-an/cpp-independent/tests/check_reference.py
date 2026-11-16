#!/usr/bin/env python3
"""Fresh mpmath point-value/derivative cross-check from the defining map.
Not the RTG owner's Python implementation and not a proof or interval certificate.
"""
import argparse
import json
import subprocess
from pathlib import Path
import mpmath as mp

mp.mp.dps = 220
om = mp.mpc(-mp.mpf(1)/2, mp.sqrt(3)/2)
ob = om.conjugate()

def raw(z, w):
    eta = (z-w)/(om-ob)
    rho = z-om*eta
    for _ in range(6):
        rho, eta = rho-mp.sin(eta), eta+mp.expm1(rho)-mp.sin(eta)
    return rho+om*eta, rho+ob*eta

mu = -mp.mpf(1)/2-2j*mp.sqrt(3)/3
c40 = -mp.mpf(1)/16+7j*mp.sqrt(3)/144
d31 = mp.mpf(1)/3-1j*mp.sqrt(3)/9
cc = -mp.mpf(61)/2160+43j*mp.sqrt(3)/6480
A, B = mu.conjugate()-2*mu, d31-2*c40
a2 = (-B-mp.sqrt(B*B-4*A*cc))/(2*A)
a3 = (1-1j*mp.sqrt(3))*(mp.mpf(1)/108-a2/6)

def p(x):
    return x*x*(a2+a3*x)

def lift(x, d):
    z, w = raw(x, p(x)+x*x*d)
    return z, (w-p(z))/(z*z)

def contained(box, z):
    return (box['re'][0] <= z.real <= box['re'][1]
            and box['im'][0] <= z.imag <= box['im'][1])

ap = argparse.ArgumentParser()
ap.add_argument('binary', type=Path)
args = ap.parse_args()
rows = []
for bits in (128,256,512):
    proc = subprocess.run([str(args.binary.resolve()), '--bits', str(bits), '--sample-map'],
                          text=True, capture_output=True, timeout=20, check=True)
    data = [json.loads(line, parse_float=mp.mpf) for line in proc.stdout.splitlines()]
    rz, rw = raw(mp.mpc('0.8','-0.4'),mp.mpc('0.05','0.07'))
    x,d = mp.mpc(mp.mpf(1)/32,mp.mpf(1)/64), mp.mpc(mp.mpf(1)/10000,-mp.mpf(1)/20000)
    f = lift(x,d)
    jac = [mp.diff(lambda xx: lift(xx,d)[k], x) for k in range(2)]
    jacd = [mp.diff(lambda dd: lift(x,dd)[k], d) for k in range(2)]
    values = [rz,rw,*f,jac[0],jacd[0],jac[1],jacd[1]]
    boxes = [data[1]['z'],data[1]['w'],*data[2]['lift'],*data[2]['jacobian']]
    checks = [bool(contained(b,z)) for b,z in zip(boxes,values)]
    rows.append({'bits':bits, 'point_and_derivative_checks':checks,'all_pass':all(checks)})
print(json.dumps({'status':'NUM cross-check only; no scientific campaign',
                  'reference':'fresh mpmath 220-decimal evaluation of T^6',
                  'tests':rows,'all_pass':all(r['all_pass'] for r in rows)},indent=2))
raise SystemExit(0 if all(r['all_pass'] for r in rows) else 1)
