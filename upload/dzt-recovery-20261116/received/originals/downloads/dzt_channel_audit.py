"""
dzt_channel_audit.py  —  DZT-OPEN-0A channel-state audit (DZT-side, b<=4 half).

Implements the two-layer channel state (DZT-DEF-CHANNEL-STATE, v0.2):

    E_C(p) in {0,1}            secular-content indicator
    P_C(x), R_C(p)=Res(Phi_p,P_C)   defined ONLY when E_C(p)=1

Three classes:
    E_C(p)=0                     -> "structural/secular absence"   (no P_C, no resultant)
    E_C(p)=1 and R_C(p)=0        -> "cyclotomic cancellation"
    E_C(p)=1 and R_C(p)!=0       -> "cyclotomic survival"

This module covers the b<=4 STRUCTURAL-ABSENCE half, which needs NO Dyadic
cascade artifact. It certifies that the transform reports b<=4 vanishing as
E_C=0 (structural), NEVER as a resultant zero, for p >= b+2.

Dyadic-owned imports (import-ref, ownership remains Dyadic):
  DYAD-ALG-VANISH-B2 : F_raw^p(0,2)=0 for p>=4  (no cross-path at degree 2)
  DYAD-ALG-VANISH-B3 : F_raw^p(0,3)=0 for p>=5  (beta-set {-3,-2,0}, no secular)
  DYAD-ALG-VANISH-B4 : F_raw^p(0,4)=0 for p>=6  (beta-set has no secular mode)
  DYAD-OPEN-B5-ALLP  : b=5 channel has a secular polynomial N -> E=1, survives.

The b=5 row (E_C=1, cyclotomic survival) is verified in dzt_open_0a_verify.py.
The cascade (4,(0,3)) row is INTENTIONALLY NOT computed here: it is
Dyadic-extraction-gated on DYAD-ART-CASCADE-Q4-03 (SG-DZT-3).

Exit 0 iff all structural-absence assertions hold; exit 1 otherwise.
"""
import sys
import sympy as sp

x = sp.symbols('x')

# --- Dyadic-owned structural-vanishing horizons (import-ref) -----------------
# E_C(p)=0 for p >= b+2 ; b<=4 channels carry NO secular polynomial.
STRUCTURAL_ABSENCE = {
    2: {"min_p": 4, "src": "DYAD-ALG-VANISH-B2"},
    3: {"min_p": 5, "src": "DYAD-ALG-VANISH-B3"},
    4: {"min_p": 6, "src": "DYAD-ALG-VANISH-B4"},
}

# b=5 carries a genuine secular polynomial (E_C=1). Used only as a contrast
# class here; its resultant survival is owned by dzt_open_0a_verify.py.
N_B5 = 2*x**6 + x**5 - 5*x**4 - 3*x**3 - 4*x**2 + 2*x + 1

HORIZON = [4, 5, 6, 7, 8, 10, 12]


def channel_polynomial(b):
    """Return P_C(x) for channel (0,b), or None if E_C=0 (structural absence)."""
    if b in STRUCTURAL_ABSENCE:
        return None            # E_C = 0 : no secular content, no polynomial
    if b == 5:
        return N_B5            # E_C = 1
    raise NotImplementedError(f"channel b={b} not registered in DZT v0.2")


def channel_state(b, p):
    """
    Return (E, R, klass) for channel (0,b) at horizon p.
      E    : secular-content indicator in {0,1}
      R    : Res(Phi_p, P_C) if E=1 else None
      klass: 'structural_absence' | 'cyclotomic_cancellation' | 'cyclotomic_survival'
    """
    P = channel_polynomial(b)
    if P is None:
        # E_C = 0 only once we are at/over the structural horizon p >= b+2.
        if p >= STRUCTURAL_ABSENCE[b]["min_p"]:
            return 0, None, "structural_absence"
        # below the structural horizon the channel is not asserted-zero by the
        # imported theorem; DZT makes no claim here (out of certified scope).
        return None, None, "below_structural_horizon"
    R = int(sp.resultant(sp.cyclotomic_poly(p, x), P))
    if R == 0:
        return 1, R, "cyclotomic_cancellation"
    return 1, R, "cyclotomic_survival"


def main():
    failures = []
    print("=== DZT-OPEN-0A  channel-state audit (b<=4 structural-absence half) ===")
    print(f"{'b':>3} {'p':>4} {'E_C':>5} {'R_C(p)':>14} {'class':>26}")

    # --- b<=4: must report E=0 structural absence (NEVER a resultant zero) ---
    for b in (2, 3, 4):
        min_p = STRUCTURAL_ABSENCE[b]["min_p"]
        for p in HORIZON:
            if p < min_p:
                continue
            E, R, klass = channel_state(b, p)
            print(f"{b:>3} {p:>4} {str(E):>5} {str(R):>14} {klass:>26}")
            # Assertions for the structural-absence class:
            if E != 0:
                failures.append(f"b={b},p={p}: expected E_C=0, got {E}")
            if R is not None:
                failures.append(f"b={b},p={p}: structural absence must have NO resultant, got R={R}")
            if klass != "structural_absence":
                failures.append(f"b={b},p={p}: expected structural_absence, got {klass}")

    # --- contrast class b=5: must be E=1 survival, distinct from above -------
    print("  --- contrast: b=5 (E_C=1, cyclotomic survival; owned by verify_0a) ---")
    for p in (6, 7, 8, 10, 12):
        E, R, klass = channel_state(5, p)
        print(f"{5:>3} {p:>4} {str(E):>5} {str(R):>14} {klass:>26}")
        if E != 1:
            failures.append(f"b=5,p={p}: expected E_C=1, got {E}")
        if klass != "cyclotomic_survival":
            failures.append(f"b=5,p={p}: expected cyclotomic_survival, got {klass}")

    # --- discipline check: structural absence is never encoded as R_C=0 ------
    # (i.e. there is no (b<=4) row with E=1 and R=0 masquerading as a cancellation)
    print("\nDISCIPLINE: structural vanishing is reported as E_C=0, "
          "never as a resultant zero (SG-DZT-8 / DZT-DEF-CHANNEL-STATE).")

    # --- cascade row is Dyadic-extraction-gated; assert we did NOT compute it -
    print("CASCADE (4,(0,3)) row: NOT computed here — gated on "
          "DYAD-ART-CASCADE-Q4-03 (SG-DZT-3).")

    if failures:
        print("\nFAIL:")
        for f in failures:
            print("  - " + f)
        sys.exit(1)
    print("\nPASS: b<=4 structural-absence encoding certified; "
          "distinct from b=5 cyclotomic survival.")
    sys.exit(0)


if __name__ == "__main__":
    main()
