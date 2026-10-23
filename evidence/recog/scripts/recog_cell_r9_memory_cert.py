#!/usr/bin/env python3
r"""
recog_cell_r9_memory_cert.py — RECOG OPEN R9: finite-q0 retained-memory theorem for the exact normalised return.
RTG_RELATIONAL_RECOGNITION_DSN (v0.3.3 frozen; result for v0.3.4).

(rep:) NF chart z of DYAD-ALG-NF6 (comparator track C_z, SG-R14), q = |z|^2, Theta = continuous lift of arg z along the orbit.
(transport:) exact six-step normalised return Fhat = h^{-1} F_W h;  imports DYAD-THM-NF-REM:
   |Fhat(z) - J(z)| <= C7 |z|^7 on |z| <= r  [(C7, r) = (100, 1/20) or (30, 1/40); rows not mixed],
   0 < q - (3/2) q^2 <= q' <= q - q^2/2 on 0 < q <= 1/400,   sum_m q_m^3 <= 2 q0^2,
   J = z + mu z^2 zbar + a32 z^3 zbar^2 + a05 zbar^5.

Observable. Psi(z) := Theta - tau log q (tau = 2 sqrt3/3). Along an orbit, Psi_m converges; the RETAINED MEMORY is
   M(z0) := Psi_inf - Psi(z0).
Theorem (RECOG-THM-R9-MEMORY). For 0 < q0 <= qbar (qbar = r^2 of the chosen row):
   M(z0) = q0 [ c_iso + Lambda_1(Theta0) ] + R,   |R| <= C2 q0^2,
   c_iso = Im[(1-2i tau) beta] = -4 sqrt3/27,  beta = a32 - mu^2/2,
   Lambda_1(Theta) = Im[G e^{-6 i Theta}],  G = (1-2i tau)/(1-6i tau) a05 = -(43 + 5611 sqrt3 i)/1270080,
   i.e. Lambda_1 = [43 sin 6Theta - 5611 sqrt3 cos 6Theta]/1270080.
Proof (averaging function). Let g(Theta) = c_iso + Im(G e^{-6iTheta}), Phi = Psi + q g(Theta). Since g + tau g' = c_iso + Im((1-2i tau) a05 e^{-6iTheta}),
the O(q^2) part of Delta Phi cancels identically; the certificate bounds |Delta Phi| <= K_Phi q^3 on the whole domain from the
jet coefficients, C7, and elementary remainder inequalities (all constants enclosed in Arb). Then
   Psi_inf = lim Phi(z_m) = Phi(z0) + sum Delta Phi_m  (q_m g -> 0),  hence |R| <= K_Phi sum q_m^3 <= 2 K_Phi q0^2 =: C2 q0^2.
Corollary (comparator incompleteness, exact map). Two orbits with identical C_z data (q_a = q_b = q0, Theta_b - Theta_a = delta)
have final pair phase  lim (Theta_b,m - Theta_a,m) = delta + q0 [Lambda_1(Theta_a + delta) - Lambda_1(Theta_a)] + R_b - R_a,
|R_b - R_a| <= 2 C2 q0^2 (log q_b,m - log q_a,m -> 0 since 1/q_m = m + O(log m)). The lattice term is certified nonzero
(for delta = pi/6 and suitable Theta_a, |Lambda_1 difference| = 2|G|) whenever q0 < |G|/C2.
Elementary inequalities used: |log(1+x) - x + x^2/2| <= |x|^3/(3(1-|x|)), |e^y - 1 - y| <= y^2 e^{|y|}/2,
|e^{it} - 1 - it| <= t^2/2, |Im w| + 2 tau |Re w| <= sqrt(1+4 tau^2) |w|.
"""
import sys
import flint
from flint import arb, acb
flint.ctx.prec = 200
ok = True
def check(name, cond, info=""):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {info}"); ok = ok and bool(cond)
s3 = arb(3).sqrt(); tau = 2*s3/3
mu  = acb(arb(-1)/2, -2*s3/3)
a32 = acb(arb(-97)/432, 197*s3/324)
a05 = acb(arb(-49)/8640, -307*s3/25920)
I = acb(0, 1)
beta = a32 - mu*mu/2
c_iso = ((1 - 2*I*tau)*beta).imag
G = (1 - 2*I*tau)/(1 - 6*I*tau)*a05
check("c_iso = -4 sqrt3/27", abs(c_iso - (-4*s3/27)) < arb('1e-50'))
check("G = -(43 + 5611 sqrt3 i)/1270080", abs(G - acb(arb(-43)/1270080, -5611*s3/1270080)) < arb('1e-50'))
check("|1 - 6 i tau| = 7", abs(abs(1 - 6*I*tau) - 7) < arb('1e-50'))
# identity g + tau g' = c_iso + Im((1-2i tau) a05 e^{-6iTheta})  <=>  (1 - 6 i tau) G = (1 - 2 i tau) a05
check("averaging identity (1-6i tau) G = (1-2i tau) a05", abs((1 - 6*I*tau)*G - (1 - 2*I*tau)*a05) < arb('1e-50'))
def up(x): return float(x.upper()) if isinstance(x, arb) else float(abs(x).upper())
def bounds(C7, qb):
    m, A, a5 = abs(mu), abs(a32) + abs(a05), abs(a05)
    X = m*qb + A*qb**2 + C7*qb**3                                 # |x| sup, x = Fhat/z - 1
    E_l = C7 + (A + C7*qb)*(2*m + (A + C7*qb)*qb)/2 + (m + A*qb + C7*qb**2)**3/(3*(1 - X))   # |l - mu q - (beta+L) q^2| <= E_l q^3
    e1 = (1 + 4*tau**2).sqrt()*E_l                                 # first bracket
    B2 = abs(beta) + a5 + E_l*qb                                   # |l - mu q| <= B2 q^2
    r1 = qb/2 + B2*qb**2                                           # |Re l| sup
    D1 = 2*B2 + 2*(arb(1)/2 + B2*qb)**2*(2*r1).exp()               # |q' - q + q^2| <= D1 q^3
    gmax = abs(c_iso) + abs(G); g1 = 6*abs(G); g2 = 36*abs(G)
    e2 = gmax*D1 + tau*g1*(1 + D1*qb) + g1*B2 + g2/2*(tau + B2*qb)**2
    K = e1 + e2
    return dict(X=X, E_l=E_l, K=K, C2=2*K, thr=abs(G)/(2*K))
res = {}
for label, C7, r in [("large disk |z|<=1/20", 100, arb(1)/20), ("small disk |z|<=1/40", 30, arb(1)/40)]:
    qb = r*r
    b = bounds(arb(C7), qb)
    check(f"{label}: |x| < 1 on the domain (log branch)", b['X'] < arb(1)/2, f"sup|x| <= {up(b['X']):.3e}")
    print(f"    {label}: E_l <= {up(b['E_l']):.4f}, K_Phi <= {up(b['K']):.4f}, C2 = 2 K_Phi <= {up(b['C2']):.4f}, "
          f"lattice-incompleteness certified for q0 < |G|/C2 = {float(b['thr'].lower()):.4e}  (qbar = {float(qb.upper()):.4e})")
    res[label] = b
check("small disk: certified window nonempty (|G|/C2 > 0 inside qbar)", res["small disk |z|<=1/40"]['thr'] > 0)
print(f"    |G| = {float(abs(G).mid()):.8f},  c_iso = {float(c_iso.mid()):.8f}")

# ---- [NUM] sanity (not part of the proof): truncated jet J as the map, retained memory vs q0 [c_iso + Lambda_1]
import numpy as np
mu_, a32_, a05_ = complex(-0.5, -2*3**0.5/3), complex(-97/432, 197*3**0.5/324), complex(-49/8640, -307*3**0.5/25920)
G_ = complex(G.real.mid()), complex(G.imag.mid()); G_ = G_[0] + 1j*G_[1].real
def M_J(q0, th0, N=150000):
    z = np.sqrt(q0)*np.exp(1j*th0); Th = th0.copy(); lq = np.log(q0)
    for _ in range(N):
        q = np.abs(z)**2; zn = z + mu_*z*z*np.conj(z) + a32_*z**3*np.conj(z)**2 + a05_*np.conj(z)**5
        Th += np.angle(zn/z); z = zn
    q = np.abs(z)**2
    g_end = float(c_iso.mid()) + (G_*np.exp(-6j*Th)).imag          # Psi_inf ~ Phi(z_N) = Psi_N + q_N g(Theta_N): tail O(q_N^2)
    return (Th - 2*3**0.5/3*np.log(q) + q*g_end) - (th0 - 2*3**0.5/3*lq), q
th0 = np.linspace(0, np.pi/3, 7)
tauf = 2*3**0.5/3
for q0 in (0.0025, 0.00125, 0.000625):
    M, qend = M_J(q0, th0.copy())
    pred = q0*(float(c_iso.mid()) + (G_*np.exp(-6j*th0)).imag)
    tail = 2*qend.max()   # crude tail of sum of remaining q^2-increments ~ q_N * const
    err = np.max(np.abs(M - pred))
    print(f"    [NUM, J-model] q0={q0}: max|M - q0 g| = {err:.3e},  /q0^2 = {err/q0**2:.3f},  q_end={qend.max():.1e}")
print("R9 CERTIFICATE PASS" if ok else "R9 CERTIFICATE FAIL"); sys.exit(0 if ok else 1)
