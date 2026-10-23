#!/usr/bin/env python3
"""recog_a1a_cd_identity_num.py -- [NUM] illustration for the A1a C_D identification (not a proof input).

Checks on exact primitive orbits (float64):
 (1) lift alignment: D_M := 2 pi M - (phi_hat_{6M} - phi_hat_0) (NUMGEN, primitive per-step lift)
     equals Theta_W(0) - Theta_W(M) (Dyadic, per-block principal Arg) to rounding;
 (2) tail-corrected estimator  C_hat(M) = D_M - tau log M + tau log(M Q_M) - P2(W_M)
     converges, and agrees with the predicted  C_pred = tau log Q_0 - P2(W_0)
     to the order of the certified P5 bound (Dyadic OPEN 21, conditional on RECOG R9).
P2 = -Delta_1 + Q[c_iso + Lambda_1] + P_W2 is Dyadic's adopted second-order primitive form.
"""
import math, cmath, json, sys
S3 = math.sqrt(3); TAU = 2*S3/3; CISO = -4*S3/27
def W(r, e): return complex(r - e/2, S3/2*e)
def T(r, e): return r - math.sin(e), e + math.expm1(r) - math.sin(e)
def D1(w):
    q = abs(w); t = cmath.phase(w)
    return q*(17*S3/36*math.cos(t) - math.sin(t)/12 - 7*S3/72*math.cos(3*t) + math.sin(3*t)/8)
def L1(t): return (43*math.sin(6*t) - 5611*S3*math.cos(6*t))/1270080
def PW2(w):
    Q = abs(w)**2; t = cmath.phase(w)
    return Q*(-5*S3/27 + 47*S3/1296*math.cos(2*t) - 19/432*math.sin(2*t) - 11*S3/324*math.cos(4*t)
              + math.sin(4*t)/54 - S3/1728*math.cos(6*t) - 5/576*math.sin(6*t))
def P2(w): return -D1(w) + abs(w)**2*(CISO + L1(cmath.phase(w))) + PW2(w)

def run(w0, Mmax, checkpoints):
    # primitive start with W(rho,eta) = w0
    e = w0.imag*2/S3; r = w0.real + e/2
    phi = 0.0; th = 0.0; wprev = W(r, e); out = []; maxalign = 0.0
    wblock = wprev
    for m in range(1, Mmax+1):
        for _ in range(6):
            r, e = T(r, e); wn = W(r, e)
            d = cmath.phase(wn/wprev)
            if not (0 < d < math.pi): sys.exit("primitive step increment outside (0,pi)")
            phi += d; wprev = wn
        th += cmath.phase(wn/wblock); wblock = wn
        DM = 2*math.pi*m - phi
        maxalign = max(maxalign, abs(DM + th))
        if m in checkpoints:
            Q = abs(wn)**2
            out.append((m, DM - TAU*math.log(m) + TAU*math.log(m*Q) - P2(wn)))
    return out, maxalign

if __name__ == "__main__":
    res = []
    for rad in (0.04, 0.02, 0.01):
        for k in range(4):
            w0 = rad*cmath.exp(1j*(0.3 + k*math.pi/4))
            Q0 = rad**2
            pred = TAU*math.log(Q0) - P2(w0)
            cps = {1000, 4000, 16000}
            out, al = run(w0, 16000, cps)
            last = out[-1][1]
            res.append({"|W0|": rad, "arg": round(0.3 + k*math.pi/4, 4), "align_maxabs": al,
                        "C_hat": {str(m): v for m, v in out}, "C_pred": pred,
                        "diff/Q0^1.5": (last - pred)/Q0**1.5,
                        "crude_diff(tau logQ0 only)/Q0^0.5": (last - TAU*math.log(Q0))/Q0**0.5})
    json.dump(res, open("a1a_cd_identity_num.json", "w"), indent=1)
    for x in res:
        print(f"|W0|={x['|W0|']:.2f} arg={x['arg']:.3f} align={x['align_maxabs']:.1e} "
              f"C_hat(16000)={x['C_hat']['16000']:.9f} (1000: {x['C_hat']['1000']:.9f}) "
              f"pred={x['C_pred']:.9f} diff/Q0^1.5={x['diff/Q0^1.5']:+.3f}")
