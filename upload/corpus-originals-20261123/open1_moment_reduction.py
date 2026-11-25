"""
OPEN 1 tractability reduction: which moments of the phase distribution does
<P4> depend on?

P4(Qs,Qc,Qd; phases) is built from invariants I_ab, omega_ab that are
I_ab = R_ab cos(phi_ab), omega_ab = (2/sqrt3) R_ab sin(phi_ab),
with R_ab = sqrt(Qa Qb), for pairs (d,s),(d,c),(s,c).

If we average P4 over a phase distribution M_phase on (phi_ds, phi_dc, phi_sc),
<P4> depends ONLY on the trigonometric moments
  <cos phi_ab>, <sin phi_ab>, <cos^2 phi_ab>, <sin^2 phi_ab>, <sin phi cos phi>,
and cross-moments if phases are correlated. Enumerate exactly which appear.
This turns the cascade condition <P4> > 0 into a FINITE moment inequality.
"""
import sympy as sp
from sympy import symbols, cos, sin, sqrt, expand, Rational as R, simplify

SQRT3 = sqrt(3)
Qs,Qc,Qd = symbols('Qs Qc Qd', positive=True)
pds,pdc,psc = symbols('phi_ds phi_dc phi_sc', real=True)

def inv(qa,qb,phi):
    Rr = sqrt(qa*qb)
    return Rr*cos(phi), (2/SQRT3)*Rr*sin(phi)

Ids,wds = inv(Qd,Qs,pds)
Idc,wdc = inv(Qd,Qc,pdc)
Isc,wsc = inv(Qs,Qc,psc)

# Full P4 (the certified primitive quartic drift, all channels)
P4 = (
    -Qd*Qd -R(1,8)*Qs*Ids -R(3,32)*Qs*wds
    -R(1,27)*Qc*Idc +R(7,108)*Qc*wdc
    -R(5,12)*wds*Ids-R(1,8)*wds*wds
    -R(5,9)*wdc*Idc -R(1,6)*wdc*wdc
    +R(1,36)*Qs*Idc -R(7,48)*Qs*wdc
    +R(1,18)*Ids*Isc+R(7,72)*Ids*wsc
    +R(1,6)*Qc*Ids  +R(3,8)*Qc*wds
    +R(1,3)*Idc*Isc +R(1,4)*Idc*wsc
)
P4 = expand(P4)

# Collect by trig monomials in the three phases. Substitute symbolic moment vars.
c_ds,s_ds,c_dc,s_dc,c_sc,s_sc = symbols('c_ds s_ds c_dc s_dc c_sc s_sc', real=True)
P4m = P4.subs({cos(pds):c_ds, sin(pds):s_ds, cos(pdc):c_dc,
               sin(pdc):s_dc, cos(psc):c_sc, sin(psc):s_sc})
P4m = expand(P4m)

# enumerate the distinct trig monomials (products of c_*,s_*) appearing
poly = sp.Poly(P4m, c_ds,s_ds,c_dc,s_dc,c_sc,s_sc)
monoms = poly.monoms()
print("Distinct phase-trig monomials in P4 (exponents over [c_ds,s_ds,c_dc,s_dc,c_sc,s_sc]):")
names=['c_ds','s_ds','c_dc','s_dc','c_sc','s_sc']
seen=set()
for mexp in monoms:
    term = '*'.join(f'{names[i]}^{e}' for i,e in enumerate(mexp) if e>0) or '1'
    seen.add(term)
for tterm in sorted(seen):
    print("   ", tterm)

print("\nNumber of distinct phase monomials:", len(seen))

# Now: averaging over M_phase replaces each monomial by its MOMENT.
# Identify the minimal moment set. Single-phase pieces vs cross-phase products:
single = [t for t in seen if t.count('_')<=1 or len(set(x.split('^')[0][-2:] for x in t.split('*')))==1]
print("\nThe averaged <P4> is LINEAR in these phase moments; cascade condition")
print("<P4> > 0 is therefore a finite linear inequality in the moment vector.")
