# Reproducing the three-height actual-prime variance diagnostic

This guide describes the frozen R20 computation at **T=100, 300, 1000 only**. It adds no calculation, parameter, mathematical claim or replacement result. The author report, scripts, data and `AUTHOR_RECEIPT.json` remain unchanged. A separate `DOCUMENTATION_RECEIPT.json` pins this guide and the existing artifacts it references.

The mathematical definition and limitations are in [ACTUAL_PRIME_VARIANCE_DIAGNOSTIC.md](ACTUAL_PRIME_VARIANCE_DIAGNOSTIC.md). In particular, the reported analytic-only lower and upper values are **not numerical intervals enclosing all rounding errors**.

## Environment and an isolated output directory

The recorded environment was:

| Component | Version |
|---|---|
| Python | 3.14.3, Clang 17.0.0 build |
| NumPy | 2.4.4 |
| mpmath | 1.3.0 |
| SymPy | 1.14.0 |
| KaTeX, optional syntax check only | 0.18.5 |

The numeric scripts do not need SciPy, a zeta-zero package, network access, an API key, a model call, or a browser. Dependency installation may need network access. Python's ordinary standard library supplies the remaining imports. Node.js is needed only for the optional KaTeX check.

From this package directory, use the following commands to create a scratch environment and retain the frozen package untouched. If the package is elsewhere, change into its directory before starting. These commands are instructions for a future replay; they were not executed to produce this guide.

```sh
R20_SOURCE="$(pwd -P)"
R20_REPLAY="$(mktemp -d "${TMPDIR:-/tmp}/astra-r20-replay.XXXXXX")"
python3.14 -m venv "$R20_REPLAY/venv"
"$R20_REPLAY/venv/bin/python" -m pip install \
  'numpy==2.4.4' 'mpmath==1.3.0' 'sympy==1.14.0'
mkdir -p "$R20_REPLAY/output"

"$R20_REPLAY/venv/bin/python" \
  "$R20_SOURCE/compute_prime_variance.py" \
  --output-dir "$R20_REPLAY/output" \
  > "$R20_REPLAY/output/actual_prime_variance.log"

"$R20_REPLAY/venv/bin/python" \
  "$R20_SOURCE/check_prime_variance.py" \
  --data-dir "$R20_REPLAY/output" \
  --output-dir "$R20_REPLAY/output" \
  > "$R20_REPLAY/output/prime_variance_checks.log"
```

Use `python3` in the environment-creation line if it resolves to the intended Python installation. A different Python build or platform should be recorded as such; it is not the original environment. Do not remove the `--output-dir` arguments when working in the frozen source directory: both scripts otherwise write beside themselves.

Neither script accepts a height, seed, epsilon, or grid-resolution argument. The fixed parameters are in the frozen source: epsilon=1/4, 16,384 alpha bins, Simpson resolutions 4096 and 2048, and degree-12 small-cell series. Changing those constants creates a different experiment and invalidates the source-hash comparison below.

## Expected outputs and finite results

The numeric replay produces the following files in the scratch output directory:

| Artifact | Contents |
|---|---|
| `actual_prime_variance.json`, `.log` | Three numerical summaries, exact cutoff counts, diagnostics, provenance and timing |
| `variance_T100_bins.csv` | Every one of the 16,384 bins for T=100 |
| `variance_T300_bins.csv` | Every one of the 16,384 bins for T=300 |
| `variance_T1000_bins.csv` | Every one of the 16,384 bins for T=1000 |
| `prime_powers.npz` | Exact arrays `n`, `prime_base`, `exponent` |
| `seed_autocorrelation.csv` | All 8193 nonnegative seed-autocorrelation grid values at both resolutions |
| `seed_quadrature.json` | Seed moments and rational analytic approximation bounds |
| `prime_variance_checks.json`, `.log` | Exact algebraic controls and bounded high-precision comparisons |

Both JSON summaries should report `PASS`. The main log ends with a statement that only the three requested heights were evaluated. Expected principal values are:

| T | Positive variance diagnostic | Integration cells | Relevant integer cutoff |
|---:|---:|---:|---:|
| 100 | 0.12040603689230812 | 22,390 | 31,939 |
| 300 | 0.13610580052150242 | 75,568 | 375,809 |
| 1000 | 0.15427941816818927 | 762,447 | 5,629,036 |

The shared prime-power array has 389,500 entries, including 448 entries with exponent greater than one, and is sieved to 5,629,037. The individual calculations apply their own support cutoffs. The largest included prime powers are 31,907, 375,799 and 5,629,009, respectively; the integer cutoffs in the table are not asserted to be prime powers themselves.

Each CSV row preserves its alpha and x endpoints, event-cell count, positive unweighted mass, prime-square contribution, mixed center, continuous square center, both seed endpoint weights, and analytic-only weighted bounds. No bins are omitted. The replay does not regenerate the author report or its original receipt.

## Comparison rules

There are three different comparisons, which should not be conflated.

1. **Frozen-file integrity.** `AUTHOR_RECEIPT.json` records the original bytes. Those hashes must match when validating the original package. The exact frozen source hashes are:

   - Author report: `5fd0ecfa3f31785e84e60be55d661f35fbac456bd8038819a9ffc635599677a9`.
   - Main script: `d6d13914220ffb30b059abf7bc4d923cfb20bd240f54fc838741dc7635f6e71f`.
   - Independent checker: `051d7f740e03183919bd65bca9d8a441f0c19ec111820973543d8b12dafd88fb`.
   - Original author receipt: `8283380e92274db4c3595a55979bbc0ed9b238e5029dfdea151f3c60d01adb53`.

2. **Exact structure on replay.** Heights, integer cutoffs, prime-power arrays, integer identities, symbolic identities, rational analytic constants, row counts and integration-cell counts should agree exactly. The `script_sha256` fields should agree if the source files are unchanged. The NPZ container hash identifies the frozen file; its logical arrays are the portable comparison. Their schema is `n: int32`, `prime_base: int32`, `exponent: uint8`, all with shape `(389500,)`. The recorded hash of the concatenated array bytes, in that key order on the original little-endian platform, is `492dd4b01e0bedccd60ab4111f53c43dd58f57e30e57f3db307bd65e3e045c47`. On another byte order, compare the integer values or normalize to the recorded dtypes before hashing.

3. **Floating numerical replay.** The same library build and machine arithmetic should reproduce the numerical CSV values. Another platform or math-library build can change the last digits. Compare the three principal totals and the full per-bin data numerically, and record discrepancies. Agreement of principal totals to an absolute tolerance of 1e-10 is a useful diagnostic screen, not a proved error bound. Investigate larger discrepancies before interpreting the output. Do not silently discard a failing cell, a failed assertion or a negative computed positive mass.

Do not compare complete replay JSON or logs byte for byte without first separating metadata. `elapsed_seconds` changes on every run, and `python_version` can change with the interpreter build. These differences propagate into file hashes. Per-bin hashes can also differ if floating values are serialized differently; that requires a numerical comparison, not a change to the frozen reference hashes. Exact source provenance must remain visible even when a result agrees numerically.

The independent checker's frozen JSON and log are identical to each other, with SHA256 `8399f0f2bdf59646af73bf77ae6f79feec6f94c7d4366de1d9d2776167baea0e`. A different SymPy or mpmath version can change printed expressions or high-precision formatting. The decisive exact controls are their zero differences and rational identities; the high-precision comparisons remain numerical diagnostics.

## What is analytically bounded, and what is not

The report proves bounds for three approximation steps in **ideal exact arithmetic**:

- Monotonicity of the fixed autocorrelation supplies endpoint Darboux bounds for the positive mass in each alpha bin.
- Exact derivative-polynomial bounds give a uniform error below 1.878e-7 for the ideal Simpson autocorrelation ratio. After weighting and summing, the allowance in the three variance totals is below 8e-8.
- The degree-12 stable-cell series has exact rational truncation bounds below 4.2e-36 for the entire requested range.

The machine evaluation also uses floating logarithms, exponentials, division, interval positions, seed values and accumulated sums. These rounding errors have **not** been enclosed. Therefore the displayed `analytic_only_lower` and `analytic_only_upper` fields are not rigorous numerical intervals for the true integral.

The 70-decimal T=100 calculation independently uses the direct antiderivative, high-precision endpoints and prime-power prefix differences. It agrees with the primary diagnostic by about 2.1e-16; six high-precision seed checks agree by less than 3.6e-17. These checks are strong consistency tests, but they are not directed-rounding proofs and do not certify all arithmetic at T=300 or T=1000.

The finite computation itself assumes neither RH nor AH. Their role is only in the separate R19 asymptotic interpretation. No finite-height result here establishes a limiting variance deficit, a zero-pair bound, or a refutation of AH.

## Workload and the optional syntax check

The frozen main JSON records about **1.23 seconds** for its complete internal run on the original machine. Its individual height stages recorded about 0.157, 0.162 and 0.324 seconds; the total also includes shared seed, sieve and output work. The independent checker took about **2.7 seconds** in the observed local process execution, including its one full T=100 high-precision comparison. That second observation is process timing, not a timing field stored by the checker.

These are local observations, not portable speed guarantees or a benchmark against other implementations. A replay should be a small seconds-to-minutes workload on an ordinary development machine after dependencies are installed. The numeric output occupies roughly 17 MB, mostly the three complete CSV files. Memory usage was not measured; the code allocates a sieve through 5.63 million integers and processes the seed quadrature in fixed batches. No large-T scan is part of the commands.

For an optional syntax-only check, copy the report and checker into the scratch tree because this utility writes beside itself. Explicitly pass the KaTeX module path; the original checker's default module path belongs to the author's machine.

```sh
mkdir -p "$R20_REPLAY/syntax"
cp "$R20_SOURCE/check_math_syntax.cjs" \
  "$R20_SOURCE/ACTUAL_PRIME_VARIANCE_DIAGNOSTIC.md" \
  "$R20_REPLAY/syntax/"
npm install --prefix "$R20_REPLAY/syntax" --no-save 'katex@0.18.5'
node "$R20_REPLAY/syntax/check_math_syntax.cjs" \
  "$R20_REPLAY/syntax/node_modules/katex" \
  > "$R20_REPLAY/syntax/math_syntax.log"
```

The expected result is 24 parsed mathematical expressions with zero syntax errors and zero control bytes. This checks mathematical typesetting syntax only; it is neither a proof check nor a PDF layout audit. No PDF build or browser is required.
