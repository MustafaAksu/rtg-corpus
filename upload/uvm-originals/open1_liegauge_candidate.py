"""
OPEN 1 candidate #2: dyadic Lie-gauge projected moments.

Structure (documented, dyadic DSN v6.0):
 - Lie strict-kernel gauge is a near-identity NF transformation with h3 = 0
   (structural) and leading generator h4 (exact over Q(sqrt3)).
 - Hence the gauge projection shifts any constituent phase by
      |delta_theta| <= C * r^3 = C * Q^{3/2},
   with documented coefficient scale C ~ |c_theta^(6)| = 119*sqrt(3)/648 ~ 0.318.
 - The Genesis relative phase phi_ds therefore shifts by
      |Delta| <= C * (Qs^{3/2} + Qd^{3/2}).

Candidate #2 moments = candidate #1 (plateau) moments rotated by Delta:
   <cos(phi+D)> = cosD <cos phi> - sinD <sin phi>,  etc.
Test the lever L = <cos> + (sqrt3/2)<sin> for sign robustness.
"""
import math
SQRT3=math.sqrt(3)

# Candidate #1 plateau moments (certified, v2.7.4; worst/best across seeds)
plateau = {1e-3:(-0.6293,-0.7617), 1e-2:(-0.6605,-0.7437), 2e-2:(-0.6813,-0.7280)}
def lever(c,s): return c + (SQRT3/2)*s

# (1) Exact tolerance: plateau phase arc [220.9, 267.2] deg must stay inside the
# favorable window (130.9, 310.9) deg under a uniform shift eps.
arc_lo, arc_hi = 220.9, 267.2
win_lo, win_hi = 130.9, 310.9
eps_neg = math.radians(arc_lo - win_lo)   # how far we may shift DOWN
eps_pos = math.radians(win_hi - arc_hi)   # how far we may shift UP
print(f"(1) shift tolerance keeping entire arc favorable: eps in (-{eps_neg:.3f}, +{eps_pos:.3f}) rad")

# (2) gauge-shift bound at the race amplitudes
C_doc = 119*SQRT3/648            # documented coefficient scale 0.318
C_safe = 10*C_doc                # x10 safety factor
Qs_max, Qd_max = 0.1, 1.17e-2
for C,lab in [(C_doc,'documented scale'),(C_safe,'x10 safety')]:
    D = C*(Qs_max**1.5 + Qd_max**1.5)
    print(f"(2) |Delta| <= {D:.4f} rad  [{lab}]   (tolerance margin x{eps_pos/D:.0f})")

# (3) explicit rotated lever at worst-case shift, both signs
print("\n(3) Lie-gauge projected lever L_NF = L(plateau arc rotated by ±Delta):")
D = C_safe*(Qs_max**1.5 + Qd_max**1.5)
print(f"{'Qs0':>6} {'L_plateau':>10} {'L_NF(-D)':>10} {'L_NF(+D)':>10}")
for q,(c,s) in plateau.items():
    for sign in [0,-1,+1]:
        dd = sign*D
        cn = math.cos(dd)*c - math.sin(dd)*s
        sn = math.sin(dd)*c + math.cos(dd)*s
        if sign==0: L0=lever(c,s)
        elif sign<0: Lm=lever(cn,sn)
        else: Lp=lever(cn,sn)
    print(f"{q:>6.0e} {L0:>10.4f} {Lm:>10.4f} {Lp:>10.4f}")

print("\nVERDICT: with h3=0, the Lie-gauge projection is an O(Q^{3/2}) phase")
print("rotation; even at x10 the documented coefficient scale the lever shifts by")
print("|dL| <= (sqrt7/2)*Delta ~ 0.14 and stays deep in L<0. Candidate #2 verdict")
print("IDENTICAL to candidate #1: leading-favorable, threshold-insufficient.")
print("Structural statement: the leading-order cascade lever is INVARIANT (to")
print("O(Q^{3/2})) across the Lie-gauge frame class precisely because h3=0.")
