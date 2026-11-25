Owner probes of the co-owner's centred evaluator (`centered_evaluator.hpp`, SHA-256 b868f945…a04a894), 16 November 2026.

Build (from a directory holding `independent_core.cpp` as reviewed and `ce_local.hpp` = `centered_evaluator.hpp` without its
`#include "independent_core.cpp"` line), Boost.Multiprecision/Config 1.83 headers, standalone mode:

    g++ -std=c++17 -O2 -DBOOST_MP_STANDALONE -Imp/include -Icfg/include -o cprobe probe_raw_point.cpp
    g++ -std=c++17 -O2 -DBOOST_MP_STANDALONE -Imp/include -Icfg/include -o cprobe2 probe_broad_disk.cpp

The endpoint files are the integer endpoints (scale 2^256) the probes printed. The two oracle checks were run inline with
mpmath 1.3.0 (360 and 120 digits), iterating the raw map T with its analytic variational equation; results are stated in the
owner review record, section 7. OWNER-RUN, SESSION.
