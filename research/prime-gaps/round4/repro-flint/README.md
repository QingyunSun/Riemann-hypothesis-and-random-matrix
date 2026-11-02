# Corrected arithmetic runtime for the prime-186 interval certificate

2026-09-05. This removes a specific reproducibility obstacle. It does not prove a prime-gap bound, discharge a Lean axiom, or replace the source certificate's checks.

The unchanged official signed-convolution regression fails with the previously installed Python-FLINT 0.9.0 / FLINT 3.6.0 wheel. A separate source-built FLINT 3.6.0 with the upstream correction passes that regression. Python-FLINT is built from source against the corrected prefix. No monkeypatch, replacement convolution, disabled assertion, or edited official certificate is used.

## Pinned inputs

* FLINT v3.6.0 archive: <https://codeload.github.com/flintlib/flint/tar.gz/refs/tags/v3.6.0>, SHA256 `4307a504622702bf0be6d8969791f7d7ff378645cf2ae3bb5a7a2b56653d97f1`.
* [Upstream signed FFT fix](https://github.com/flintlib/flint/commit/7ad753d51c82fdec115cb179b41d0e581f1cb0ec), from [PR2790](https://github.com/flintlib/flint/pull/2790). Download its `.patch` URL as `flint-7ad753d.patch`; SHA256 `333788fe3d7fe1c24ca10e5ef33f492eae68de6202568e75e18e1bcd7bfb71ff`.
* Official PrimeGaps186 source at `61340d0b74163003b32756bb16e91d9209a5e330`; `prime_gap_186_certificate.py` SHA256 `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`.
* Host build: Apple Silicon macOS, clang, Python 3.12.9, Python-FLINT 0.9.0, NumPy 2.2.6, Homebrew GMP 6.3.0 and MPFR 4.2.2. FLINT was configured with `--enable-assert --disable-static`.

The upstream fix corrects the conversion of a residue near the halfway point of the FFT coefficient ring into a signed integer. Testing only the leading limbs misses boundary cases with nonzero lower limbs. The patch contains both the correction and targeted native test cases. The version string remains 3.6.0; the patch hash and actual linked-library path distinguish this runtime from the failing wheel.

## What passed

1. Native FLINT suites `fmpz_vec`, `fmpz_poly`, `arb`, `arb_poly`.
2. The original certificate's `check_flint_signed_fft()` and `_cap_check_environment()`, called unchanged.
3. 467 full products and 2,188 truncated products compared with an independently implemented Python integer double loop. These include both signs, limb boundaries, the original 509/510-bit failure, zero polynomials, and deterministic random coefficients. The comparison took approximately 0.80 seconds here.
4. Ten selected Python binding tests for the integer/rational polynomial and Arb APIs used by the certificate.

`otool -L` confirms that the extension loads the corrected isolated `libflint.24.0.dylib`. The old wheel remains available and fails as a negative control, as recorded in `negative-wheel-control.json`.

## A separately disclosed full-suite failure

The **complete** Python-FLINT suite did not pass: with native assertions enabled, `test_fmpz_functions` aborts in `_n_jacobi_unsigned`. Its test table invokes `fmpz(2).jacobi(n)` at zero and even denominators. The installed FLINT source documentation for `fmpz_jacobi` specifies an odd positive denominator and says parity/sign are not checked. The Python wrapper forwards the input without enforcing that precondition.

The certificate uses no Jacobi call. The native integer/polynomial and Arb suites, its own regression, and the selected binding tests passed independently. We retain the abort logs and keep assertions enabled; we do not claim that all Python-FLINT tests passed or that the library has been universally verified. Resolving the separate Jacobi wrapper/test contract is postponed.

## Reproduction on this host

The source/build/install cache is separate from the Dropbox research record. The original PrimeGaps186 clone is unchanged. For a fresh directory without spaces:

```sh
bash build_runtime.sh DOWNLOAD_DIRECTORY BUILD_DIRECTORY
bash build_python_binding.sh BUILD_DIRECTORY PYTHON_EXECUTABLE
BUILD_DIRECTORY/venv/bin/python signed_convolution_check.py \
  --official-script PATH_TO_UNCHANGED_CERTIFICATE \
  --output NEW_RECEIPT.json
```

The first script verifies both source download hashes, refuses to overwrite an existing checkout, applies the upstream patch, compiles, runs the four native suites, and installs to `BUILD_DIRECTORY/prefix`. The second creates a fresh virtual environment and builds the binding with the needed macOS GMP link path. GMP, MPFR, autoconf, automake and libtool must already be installed. The script assumes the Homebrew paths used on this host; other platforms should adjust the toolchain paths while preserving source hashes and the regression.

On this run the usable interpreter is:

```text
/Users/qingyunsun/.cache/astra-research/flint-3.6.0-patched/venv/bin/python
```

The binding build first encountered two configuration errors: the optional `add_flint_rpath` setting emitted a linker flag unsupported by Apple's linker; without it, the transitive GMP library still needed an explicit `-L` path. The successful build omits the former and supplies the latter. These errors and the exact successful commands are retained in their separate logs. They caused no change to the mathematics or the official certificate.

## Acceptance and limits

The purpose of this runtime is to execute new outward-enclosed integrals with the original arithmetic safeguards. Round four's first application is a positive lower integral on one genuine outer failure rectangle. It does not require recomputing all 149 existing upper integrals merely to validate the new rectangle; combining the new credit with the old final margin explicitly inherits the published upper endpoints.

Full new `k=39` support restoration, complete physical-integral replay, a portable binary distribution, and proof-assistant verification remain separate work. The runtime can be abandoned by using another interpreter; the original wheel and official source were not overwritten.
