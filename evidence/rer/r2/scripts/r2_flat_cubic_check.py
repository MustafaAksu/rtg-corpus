"""Bounded R2 algebra check: supplied class-C cubic, not a network certificate."""
import sympy as S

x, y, p, q, b = S.symbols('x y p q b', real=True)
z, d = x + S.I*y, p + S.I*q
mu = -S.Rational(1, 2) - 2*S.I*S.sqrt(3)/3
Q, C = S.expand(z*S.conjugate(z)), S.expand(d*S.conjugate(d))
w = (z, -z/2+d, -z/2-d)
f = [S.expand(mu*v*v*S.conjugate(v)) for v in w]
fs, fc = S.expand(f[0]-sum(f)/3), S.expand((f[1]-f[2])/2)
fs0 = mu*(3*Q*z/4 + d*d*S.conjugate(z)/3 + 2*C*z/3)
fc0 = mu*(z*z*S.conjugate(d)/4 + Q*d/2 + C*d)
assert S.simplify(fs-fs0) == 0 and S.simplify(fc-fc0) == 0
print('projected cubic modal components: PASS')
DI = S.expand(S.re(fs*S.conjugate(d)+z*S.conjugate(fc)))
plus = DI.subs({p:-y, q:x}, simultaneous=True)
minus = DI.subs({p:y, q:-x}, simultaneous=True)
assert S.simplify(plus-S.sqrt(3)*Q**2/9) == 0
assert S.simplify(minus+S.sqrt(3)*Q**2/9) == 0
print('unsigned Gram opposite-orientation quartic difference: 2*sqrt(3)*Q**2/9')
B = S.expand(S.I*b*Q*z)
parent = S.simplify(fs.subs({p:0, q:0}))
child = S.Poly(S.expand(fc.subs({p:S.re(B), q:S.im(B)}, simultaneous=True)), x, y)
child5 = S.Add(*(c*x**i*y**j for (i,j),c in child.terms() if i+j == 5))
DB = S.expand(S.diff(B,x)*S.re(parent)+S.diff(B,y)*S.im(parent))
assert S.simplify(child5-DB-b*(-S.sqrt(3)/3+S.I)*Q**2*z) == 0
print('cubic-birth graph degree-five defect: b*(-sqrt(3)/3+i)*Q**2*z')
print('PASS; exact coefficient check only; no raw certificate or source script rerun')
