# Genesis ER-2B — six-step cubic jet / separability audit

Date: 2026-10-09. Status: independent scoped algebra check; noncanonical. No owner file or scientific result grade changed.

## Input contract

Continuous 2D primitive edge map

    T(rho,eta) = (rho-sin eta, eta+exp rho-1-sin eta).

Three oriented edges `(a,b,-a-b)`, each in `R^2`. One primitive coupled step:

    N = P_C o T^{x3}, P_C = I - (1/3) 11^T.

The six-step map is `N^6`, on the four real independent edge coordinates `(a1,a2,b1,b2)`. Truncate primitive components at degree three, and retain total polynomial degree <=3 after **each** composition; this is exact for the six-step three-jet.

## Exact source split

    T(x) = A x + T2(x) + T3(x) + O(|x|^4),
    A = [[1,-1],[1,0]],
    T2(rho,eta) = (0,rho^2/2),
    T3(rho,eta) = (eta^3/6,(rho^3+eta^3)/6).

The full six-step map has exactly zero quadratic jet and 64 nonzero cubic coordinate-monomial coefficients across its four independent outputs. Its first nonzero nonlinear term is the cubic `G3`. The saved machine JSON includes all four `G3` coordinate polynomials, not just the obstruction.

Define the mixed-derivative obstruction on the fixed edge chart:

    Omega6^k[a_i,b_j] = partial_{a_i} partial_{b_j} (N^6_1-N^6_2)_k.

All eight leading linear expressions reproduce the user-provided table. This independently checks the coefficient vectors, including the off-diagonal blocks and their edge-exchange antisymmetry.

**New scoped deduction:** replacing `T` by `A+T2` reproduces the **entire eight-entry Omega6 leading table**. Replacing `T` by `A+T3` gives zero in all entries. At degree three in the return, the full `G3` equals the sum of the quadratic-composition contribution and the direct cubic contribution. Thus, in this exact model and clock, the first nonseparable six-step term is produced by compositions of the primitive quadratic edge term, not the direct primitive cubic edge term. This does not say the full G3 is independent of T3.

## Recursive certificate for the mechanism split

Write the one-step **four-dimensional coupled map** as

    N(x)=A4 x+N2(x)+N3(x)+O(|x|^4),

where `A4=diag(A,A)`. If its j-th iterate has homogeneous degree-two and degree-three terms `B_j,C_j`, then

    B_0=C_0=0,
    B_{j+1}=A4 B_j+N2(A4^j x),
    C_{j+1}=A4 C_j + D N2(A4^j x) B_j + N3(A4^j x).

This separates the contributions algebraically. It is a model/clock decomposition, not an invariant division into geometry and dynamics.

## Covariance

Since `N^6(x)=x+G3(x)+O(|x|^4)` with no quadratic term, any origin-preserving local diffeomorphism `H(x)=Lx+O(|x|^2)` gives

    H^{-1} N^6 H(x)=x+L^{-1}G3(Lx)+O(|x|^4).

Thus the leading cubic vector-valued tensor is well-defined up to linear frame transport. The entire Omega6 function need not be a tensor under nonlinear changes. Its linear homogeneous leading derivative data are compatible with edgewise linear frame transport preserving the three-edge/closure structure; arbitrary linear mixtures of the edge slots generally change the definition of the decomposition.

Two additional exact checks passed: `G3(A4 x)=A4 G3(x)` (a consequence of commutation of the primitive map and its sixth iterate), and covariance under cyclic permutation of oriented edges. These are structural symmetries within the model, not proof of physical primitivity or curvature.

## Evidence boundary

`check_genesis_sixjet_scope.py` is an independently written pure-Python `Fraction` sparse polynomial implementation. It does not use supplied SymPy jets, new owner scripts, or historical certificates. `genesis_sixjet_obstruction_audit.json` contains the four full cubic components, every obstruction entry for the original and isolated-order controls, and validation flags. One intermediate script assertion initially failed only because the printed summands were sorted differently, not because coefficients differed; it was corrected to the exact output ordering. A subsequent coding error shadowed the `Fraction` alias during extra validation; that was corrected. The final run exits zero and includes all checks.

No finite-amplitude analytic remainder, source norm, physical incidence, generalized first-integral, or selected physical resonance mechanism is certified by this jet check.
