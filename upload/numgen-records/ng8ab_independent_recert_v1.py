#!/usr/bin/env python3
# =============================================================================
# NG-8A / NG-8B INDEPENDENT RE-CERTIFICATION  v1
# =============================================================================
# Context: RTG Number Genesis DSN v1.4 registers
#   NG_NG8A_ORBIT_CARDINAL_CERT_v1.md   (NG-8A CLOSED)
#   NG_NG8B_REBLOCK_MULT_CERT_v1.md     (NG-8B CLOSED)
# but those certificate files are not present in the project corpus (produced
# in an external reviewer sandbox). This script independently re-certifies
# both theorems at the word-algebra layer, conditional on the two imported
# premises stated below. Exit code 0 iff every assertion passes.
#
# EPISTEMIC POSITION OF THIS CERTIFICATE
#   Both NG-8A and NG-8B are [RESULT][from: ALG] claims *conditional on*
#   already-certified N-1 content. This script certifies the algebraic layer
#   exactly and records the imported premises explicitly. It does NOT re-prove
#   the premises (they have their own certificates in the corpus).
#
# PREMISE-1 (imported; source: NG_N1_UNIFIED_T_ALIGNMENT_CERT_v1.md, NG v1.4
#   changelog v0.8/v0.9): on the certified local primitive-dyad tube U_T,
#   the primitive orbit has NO finite collision: T^r x = T^s x  =>  r = s,
#   for all integers r,s >= 0, for every admissible x in U_T; and U_T is
#   forward invariant under T (hence under every T^m). Consequently the
#   history monoid is FREE MONOGENIC: a history is faithfully modelled by
#   the word T^k, i.e. by a tuple of k primitive tokens, and composition is
#   concatenation.
#
# PREMISE-2 (imported; interpretive anchor for the word "physically" in
#   NG-8A): distinct states on the tube are distinct points of the
#   gauge-reduced chart and therefore differ in certified relational
#   observables (Q_true and/or relational phase). Set-distinctness of tube
#   states equals physical distinguishability at this scope. This premise is
#   not word-checkable here; it is recorded so that NG-8A's counting
#   predicate is explicit (cf. SG-NG-11 strict-vs-counting guard).
#
# Under PREMISE-1 the physical orbit-evaluation map k |-> T^k x is faithfully
# represented by k |-> word('T'*k); all NG-8A/NG-8B content then lives at the
# word level and is certified below both by structural argument and by
# exhaustive finite verification over declared ranges plus large spot checks.
# =============================================================================

import sys

FAILURES = []


def check(name, cond):
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}")
    if not cond:
        FAILURES.append(name)


# -------------------------------------------------------------------------
# Word model of the free monogenic history monoid (PREMISE-1 layer).
# A history of k primitive events is the tuple ('T',) * k.
# Composition = tuple concatenation. Identity = ().
# -------------------------------------------------------------------------

def word(k):
    return ("T",) * k


def compose(a, b):
    return a + b


IDENT = word(0)

# -------------------------------------------------------------------------
# Section 0 — sanity of the word model itself
# -------------------------------------------------------------------------
check("S0.1 identity word is empty tuple", IDENT == ())
check("S0.2 composition = concatenation, lengths add",
      all(len(compose(word(a), word(b))) == a + b
          for a in range(0, 25) for b in range(0, 25)))
check("S0.3 word-model freeness: word(j)==word(k) iff j==k (j,k<=400)",
      all((word(j) == word(k)) == (j == k)
          for j in range(0, 401, 7) for k in range(0, 401, 11)))

# -------------------------------------------------------------------------
# Section A — NG-8A: ordinal-to-cardinal orbit-state compatibility
#   Post-event convention: S_m^+(x) = { T^k x : 1 <= k <= m },  S_0^+ = {}.
#   Claim: |S_m^+(x)| = m  (event occurrences equinumerous with newly
#   visited post-event states), via injectivity (PREMISE-1) + surjectivity
#   (by construction) of the orbit-evaluation map.
# -------------------------------------------------------------------------

def S_plus(m):
    # word-level image of the post-event visited-state collection
    return {word(k) for k in range(1, m + 1)}


M_RANGE = list(range(0, 61)) + [137, 210, 499]

check("A1 |S_m^+| = m for all m in test range (incl. m=0 empty set)",
      all(len(S_plus(m)) == m for m in M_RANGE))

check("A2 orbit-evaluation injectivity at word level (distinct k give "
      "distinct words), m<=60",
      all(len({word(k) for k in range(1, m + 1)}) == m for m in range(0, 61)))

check("A3 surjectivity by construction: image of {1..m} equals S_m^+",
      all({word(k) for k in range(1, m + 1)} == S_plus(m)
          for m in range(0, 61)))

# Off-by-one convention guard (the [GUARD] in NG-8A):
#   position-set {x, Tx, ..., T^(m-1)x} has m positions but m-1 transitions;
#   post-event set S_m^+ has m states for m transitions/events.


def position_set(m):
    return {word(k) for k in range(0, m)}  # includes the initial state word(0)


check("A4 position-set convention: |{x,...,T^(m-1)x}| = m positions, "
      "transitions inside = m-1 (m>=1)",
      all(len(position_set(m)) == m and (m - 1) == (len(position_set(m)) - 1)
          for m in range(1, 61)))
check("A5 conventions differ exactly by the initial state: "
      "position_set(m) = S_(m-1)^+ union {id}",
      all(position_set(m) == (S_plus(m - 1) | {IDENT}) for m in range(1, 61)))

# -------------------------------------------------------------------------
# Section B — NG-8B: multiplication by physical re-blocking
#   B_m = T^m.  Claims:
#     (i)  <B_m> is free:  (B_m)^j = (B_m)^k  =>  j = k   (m >= 1);
#     (ii) (T^m)^k = T^(mk) as IDENTITY OF THE SAME ORDERED HISTORY under
#          two groupings (not merely endpoint equality);
#     (iii) re-blocking introduces no second independent event type:
#          every <B_m> word is a word in the single primitive token.
# -------------------------------------------------------------------------

def block(m):
    return word(m)


def block_power(m, k):
    w = IDENT
    for _ in range(k):
        w = compose(w, block(m))
    return w


MK_RANGE = [(m, k) for m in range(1, 21) for k in range(0, 21)]
MK_SPOT = [(137, 89), (89, 137), (1, 500), (500, 1), (37, 0), (2, 250)]

check("B1 grouping identity (T^m)^k == T^(mk) as literal word equality "
      "(exhaustive m<=20,k<=20 + large spot checks)",
      all(block_power(m, k) == word(m * k) for (m, k) in MK_RANGE + MK_SPOT))

check("B2 <B_m> freeness: block_power(m,j)==block_power(m,k) iff j==k "
      "(m in 1..12, j,k in 0..30)",
      all((block_power(m, j) == block_power(m, k)) == (j == k)
          for m in range(1, 13) for j in range(0, 31) for k in range(0, 31)))

check("B3 length homomorphism argument: len((B_m)^j)=mj, and mj==mk => j==k "
      "for m>=1 (integer cancellation, checked m<=200, j,k<=200 sampled)",
      all(((m * j == m * k) == (j == k))
          for m in range(1, 201, 13) for j in range(0, 201, 17)
          for k in range(0, 201, 19)))

# Grouped-history model: a k-fold m-block history as an explicit list of
# blocks; flattening must reproduce EXACTLY the primitive history word.


def grouped(m, k):
    return [block(m) for _ in range(k)]


def flatten(groups):
    w = IDENT
    for g in groups:
        w = compose(w, g)
    return w


check("B4 'same ordered history, different grouping': flatten of k m-blocks "
      "== primitive word T^(mk); grouping metadata differs (k parts vs mk "
      "tokens) whenever m>=2,k>=1",
      all(flatten(grouped(m, k)) == word(m * k) for (m, k) in MK_RANGE + MK_SPOT)
      and all(len(grouped(m, k)) == k != m * k
              for m in range(2, 8) for k in range(1, 8)))

check("B5 no second event type: every <B_m> word uses only the primitive "
      "token 'T' (m,k <= 20)",
      all(set(block_power(m, k)) <= {"T"} for (m, k) in MK_RANGE))

check("B6 edge cases: (T^m)^0 = id = T^0; (T^1)^k = T^k",
      all(block_power(m, 0) == IDENT for m in range(1, 30))
      and all(block_power(1, k) == word(k) for k in range(0, 60)))

# -------------------------------------------------------------------------
# Section C — guard-consistency checks (SG-NG-20 alignment)
#   A pair (T^m, T^n) is one certified stream under two blockings: both
#   flatten into the SAME primitive token alphabet and their generated
#   words all lie inside the single ambient monogenic word monoid.
# -------------------------------------------------------------------------
check("C1 (T^m,T^n) generate words inside the single primitive alphabet "
      "(no new generator appears)",
      all(set(compose(block_power(m, j), block_power(n, k))) <= {"T"}
          for m in (2, 3, 5) for n in (3, 4, 7)
          for j in range(0, 6) for k in range(0, 6)))

# -------------------------------------------------------------------------

print("-" * 70)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILURE(S):")
    for f in FAILURES:
        print("   -", f)
    sys.exit(1)
print("RESULT: ALL ASSERTIONS PASS — NG-8A and NG-8B are independently "
      "re-certified at the word-algebra layer, conditional on PREMISE-1 "
      "(N-1 non-collision/free monogenic tube) and with PREMISE-2 recorded "
      "as the explicit physical-distinguishability counting predicate.")
sys.exit(0)
