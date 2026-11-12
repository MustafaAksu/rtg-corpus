# AZ Study — Frozen Conventions Registry
# Status: [ENG] frozen for Phase 2+ execution. Any change requires a versioned
# note and re-freeze. Phase 0 [HEUR diagnostic], Phase 1 [ENG] PASS.

[CONV-AZ-GRAPH-EXPORT]
For each TDR-G run, export one or more of:
  1. G_T          : final-time defect graph at T
  2. Core(G_T)    : recurrent-core graph (see DEF-AZ-CORE) — DEFAULT primary object
  3. G_birth(w)   : birth-window graph over [t_first_birth, t_first_birth + w], default w=200
  4. G_cumulative : union of all defect edges over the run (diagnostic only; expected generic)
Edge convention: both orientations as independent directed edges.
Every spectrum MUST declare which object it used. No declaration => not reproducible => no DSN import.

[DEF-AZ-CORE]
Core(G_T) is the edge-induced subgraph of directed edges that belong to at least one
directed cycle under the non-backtracking transition rule. Equivalently: retain the
strongly-connected components of the Hashimoto transition graph that contain at least
one cycle. If implementation differs, the exact rule must be written here before Phase 2.

[CONV-AZ-SPECTRUM-MODE]
Declare per spectrum exactly one of:
  - full-spectrum : all eigenvalues (dense); R_q is full-spectrum.
  - leading-K     : top-K by magnitude (ARPACK); statistic is R_q^(K), NOT R_q.
  - trace-moment  : Tr(B^m) moments only; no eigenvalues.
No leading-K statistic may be compared to a full-spectrum statistic without a calibration study.
For N=120..720 the feasible primary observable may be leading-K or trace-moment.

[CONV-AZ-STATS-MULTITEST]
Q_N = { q : q | N, 2 <= q <= q_max },  q_max = 24 (frozen), q=1 excluded.
Registered statistic per run family is either:
  1. a preselected q justified before the run, or
  2. R_max = max_{q in Q_N} R_q.
When scanning q, significance is assessed against the null distribution of R_max,
NOT individual R_q. Candidate status requires empirical p <= 0.01 after null-ladder
correction AND stability across >= 2 large even N.

[CONV-AZ-STATS-DEFS]
R_q   = | (1/n) sum_l exp(i q theta_l) |, theta_l = arg(lambda_l).  Uniform null: E[R_q] ~ 1/sqrt(n).
rho_B = max_l |lambda_l|.  NO analytic bound imposed; null-ladder comparison only.
gap   = rho_B - |lambda_2|.  Null-ladder comparison only.
RETRACTED: C_q (fraction within pi/q arc) — null expectation was ~1 not 1/q; removed.
RETRACTED: rho(B) <= sqrt(d_max) analytic expectation — not valid for Hashimoto; removed.

[CONV-AZ-NULLS]
Null 0: directed configuration model preserving in/out-degree sequence.
Null 1: reciprocal-pair-preserving directed configuration model.
Null 2: preserves recurrent-core node/edge counts and SCC size profile.
Null 3: phase-shuffled TDR-G null preserving N,k,M_t and defect-band rule, randomizing advances (seeded).
Null 4: time/policy-shuffled null preserving M_t and birth-count trajectory, destroying policy motif correlations.
Each null carries its own manifest and seed list.
Null-count discipline: 100 nulls => [NUM diagnostic] only; >=1000 => [NUM candidate]; >=5000 => stronger.
Empirical p = (1 + #{S_null >= S_obs}) / (1 + M).

[SG-PLAN-5] Canonical vs noncanonical k/N: canonical (k/N=1/15) only for N divisible by 30, k=N/15.
            Other even N use rounded integer k, tagged [NUM diagnostic][scope: noncanonical integer-k].

[SG-PLAN-6] Graph-export convention mandatory (CONV-AZ-GRAPH-EXPORT).

[SG-PLAN-7] Core-extraction bias: a signal only in Core(G_T), absent in G_T and G_birth(w),
            is [NUM core-diagnostic] only; becomes [NUM TDR-G candidate] only if the mechanism
            explicitly depends on recurrent-core dynamics.

[STOP/ESCALATE] finite-size rule:
  - signal only N<120, gone at N=120,240   => [NUM sandbox], not a candidate
  - signal at N=120 but not N=240,360       => [NUM finite-size diagnostic]
  - signal stable across >=2 large even N    => eligible for [NUM TDR-G candidate]

[RID: AZ-RESULT-NOSIGNAL-TEMPLATE]
[NUM] [scope: tested graph-zeta observable family]
Under graph export X, null ladder Y, N-family Z, policies P, horizon T, script version V,
no TDR-G-specific arithmetic spectral signal was detected.
Forbidden interpretation: "no OPEN-P1 bridge exists."

[birth_window manifest field]
birth_window_status: available | no_birth | cap_truncated
If no_birth, no G_birth(w) spectrum exists; do not impute one.

[Phase 1 required artifacts — all present]
  cycle_L (S1)              : verified analytic, L=4,6,8
  bidirected_cycle_L (S2)   : verified by construction, L=4,6
  disjoint_cycles (S3)      : verified analytic, (k,L)=(2,4),(3,6)
  bouquet_2_4_hashimoto_matrix.json : stored
  bouquet_2_4_charpoly.txt          : stored
  az_v5_synthetic_benchmark_report.json : stored
