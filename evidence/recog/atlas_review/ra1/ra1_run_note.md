# RECOG.R-A1 re-check — run note

**Run by:** Claude, Atlas owner, 3 November 2026, on the Atlas host.
**Environment:** Python 3.13.16, numpy 2.5.3, mpmath 1.3.0, sympy 1.14.0, Linux x86_64 (glibc 2.39).
**Sources:** `main` at `d340282`; the eight A1c scripts at the hashes registered in `recog-v0.3.26` (checked).

## How the trees were produced

The two trees (`orig`, `patch`) were run before the driver `recog_ra1_cprime_recheck.py` was written, with a shell loop that ran the same steps:
- the same eight scripts in the same order;
- the repository layout;
- `python3 -I`.

The patched script is byte-identical to the one the driver's `build` step produces: SHA-256 `c731cf1b7105bf70d4e5ce4f1d993f5009bbeb0cdcc9c82144dde7ddc93dff24`, the only change being L55 `I("0.36915")` → `I("0.36916")`.

There are two differences from the driver:
1. **Part 1b orbit length.** Part 1b was first run at its default orbit length of 1,800,000 steps. The committed part-1b output was made with 6,000,000 steps (`argv[2]`; the JSON field `G5.N_steps`), so part 1b was rerun at 6,000,000 steps in both trees. Those reruns are the ones compared.
   - The downstream certificates import part 1b's functions, not its JSON, so the orbit length does not reach them.
2. **Standard error.** The loop merged stderr into `*_output.txt`. Only the drift proof table writes to stderr: progress lines starting `PT1 ` / `PT2 ` …. These lines were removed before the comparison. The driver writes stderr to a separate file.

`compare` was then run on these trees. Its output is `ra1_recheck_summary.json`.

## Wall time per tree

| Certificate | Seconds |
|---|---|
| tail averaging (part 1b, 6M steps) | about 60 |
| start offset | 156 |
| unknown-a interval | 159 |
| in-block angular | 108 |
| combined tail | 148 |
| joint transfer | 1,686 |
| drift centring | 225 |
| drift proof table | 627 |

The patch tree's times were within 1 % of these.

## Propagation check

The C term of part 1b is linear in c′_Q. Its relative change is 2.709 × 10⁻⁵ at every table point, which equals (0.36916 − 0.36915)/0.36915. So the change reached the certificate.

The start-offset β(a) rises by exactly 0.00001 · 256/225 = 1.138 × 10⁻⁵.
