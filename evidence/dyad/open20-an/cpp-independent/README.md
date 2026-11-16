# DYAD independent C++ inclusion kernel

**SESSION / DEVELOPMENT PROTOTYPE. Author: ChatGPT. Proposed auditor: Claude.**
This is not the Python stage-3c-b package, not an implementation of the complete
pilot, and not a jump or divergence certificate. No production mode exists.

## Contents and method

- `src/interval.hpp`: MPFR directed-endpoint real intervals and rectangular
  complex intervals. No Arb/FLINT, no double precision in acceptance tests.
- `src/kernel.hpp`: full elementary `T^6`, holomorphic first derivatives,
  centered mean-value enclosure, inclusion-preserving edge/chain contractors,
  a uniform local inverse-box witness, and a strict two-disc test.
- `src/main.cpp`: 20 development tests and point-value output for a separate
  numerical reference check. Tests use a degree-3 polynomial and short local
  orbits; they do not enclose either selected sectorial value at xi_star.
- `tests/check_reference.py`: fresh mpmath point-value and derivative comparison
  derived from T, not imported from the owner's Python implementation.

The proposed end-to-end algorithm is in the accompanying design note. In
particular, **global initial enclosure of the selected orbit is an obligation**:
local contraction or a small inverse box never establishes this by itself.

## Build with the normal MPFR development headers

On Ubuntu/Debian, install `g++ cmake libmpfr-dev libgmp-dev` using the normal
package manager. Then:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j2
ctest --test-dir build --output-on-failure
# Optional numerical cross-check; mpmath is not required by the C++ kernel.
python3 tests/check_reference.py build/dyad_cpp_kernel
```

The build must not use `-ffast-math`. MPFR arithmetic explicitly specifies each
rounding direction. Keep precision fixed for an entire process. No production
accuracy or runtime improvement is claimed from a choice of language.

## Current executable evidence and its limit

In this authoring container the installed MPFR runtime is **4.2.2**, but its
full development header is absent. The source was compiled with a small local
public-ABI declaration subset checked against MPFR's public header, using GCC
and the installed MPFR/GMP shared libraries. That subset is included under
`evidence/local_build/` solely to make the limited build reproducible; it is
**not** the production header and is not on the normal CMake include path.
Claude's first build check must use the distribution's actual `mpfr.h`.

At 128, 256 and 512 bits: 20/20 kernel tests pass. The fresh 220-decimal mpmath
reference lies in all 8 emitted value/derivative boxes at each precision
(24/24 point checks). These checks do not prove arithmetic implementation
correctness or settle any DYAD scientific claim.

## Independence disclosure

ChatGPT previously reviewed parts of the owner's Python implementation. This is
not a blind clean-room experiment. New source was written from the mathematical
map and a different generic mean-value/Krawczyk design, not translated from
Python. The kernel does not read the Python source, coefficient caches, discs,
Cauchy constants, or output files. It uses MPFR rather than Arb; GMP and the
published mathematics remain shared dependencies. Same-author tests are not
Claude's independent review.

## Scope still open

The exact phi_40 coefficient construction, tube/domain data binding, whole-fibre
initial coverage at the real pilot point, a chain-identification argument for
the chosen inverse branch, and the full pair of legs remain to be implemented
and reviewed. Region-I/II and literature inputs remain external, explicitly
conditional dependencies. No statement about B-an/B-6 or a Fourier mode follows.
