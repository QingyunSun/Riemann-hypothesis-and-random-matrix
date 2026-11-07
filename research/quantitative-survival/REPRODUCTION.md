# Reproduction and review receipt

6 November 2026. This packet contains mathematical derivations, internally checked finite certificates, numerical diagnostics, and source audits. They have different evidential roles.

## Exact finite law and interval checks

The fixed input is finite/candidate.json, SHA-256:

`879a342d7c9a79aed72dae2bf72bd79c1fc7ad670a8f25124429237eb5edd76c`

Its hexadecimal floats define exact dyadic rationals. The probability law is defined by an exact cyclotomic linear solve. The interval computation proves that this solve exists, stays strictly positive, preserves the stated moments, and changes survival by more than 0.0175.

Root replay environment: Python 3.12, NumPy 2.5.4, SciPy 1.18.1, python-flint 0.8.0, with one BLAS thread. Independent replay used 224-bit interval precision and a different numerical inverse call. The 160-bit verifier's numerical inverse is only a preconditioner; its validity is checked with outward-rounded intervals.

Run from this directory:


```sh
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export PYTHONDONTWRITEBYTECODE=1
python finite/certify.py
python finite/baseline.py
python finite/check_weights.py
python check_lift.py
python bounded/check.py
python arithmetic/check_normalizations.py
```


The first five commands passed in the root replay, and all six commands passed again in an isolated-copy review immediately before publication. The regenerated JSON receipts matched after excluding elapsed-time fields:

- 964 selected constraints, the independently derived dimension bound, positivity and survival shift were certified.
- All 16,159 ACUE dihedral orbits were included in the probability baseline.
- All 1,489 selected orbit-pair weights were independently checked by Fourier-projection Gram determinants.
- 2,548 direct lift identities and 1,924 pair-fibre membership cases were checked; the general statements are proved in the accompanying note.
- 1,356 deterministic supplementary checks support the bounded-probe derivations.

In `finite/certificate.json`, `exact_definition` describes the base perturbation. The reported strongest law uses that perturbation multiplied by the separately recorded `magnification` factor \(99/50\). Its positivity and survival gain are the `magnified_*` fields; no magnification of the base ACUE probabilities themselves is intended.

The last command gives floating diagnostics of a known singular-series average and the packet convolution. It is not an interval proof, a prime-pair experiment, or verification of the missing arithmetic hypothesis. Quadrature orders 128 and 256 were compared; finite-cutoff differences are retained in the receipt rather than suppressed.

For the additional artificial counting-measure example, run `python arithmetic/check_sieve_rows.py` and compare its standard output to `arithmetic/sieve_checks.json`. The standard-library checker uses exact rational arithmetic and a piecewise-linear test density. It checks 576 twist/shift/modulus rows, 71,424 integer jumps and 142,848 primitive endpoint values. These finite tests support the discretization and local sieve argument, not the limiting prime-number-theorem calculation. An independent review checked that flooring preserves the primitive bound rather than a total-variation bound and that the same surrogate works for each fixed height test, without uniformity in varying tests.

## Optional discovery reproduction

The files finite/quantify.py, finite/pivot.py and finite/export_candidate.py record how the compact seed was obtained. Running them sequentially creates floating.npz and pivots.npz and exports candidate.reconstructed.json. These are a floating search, not the proof.

The exporter was checked against the original search matrices and reconstructs the committed seed object exactly. A new LP/QR run may select different coordinates on another numerical-library build. It must undergo its own interval verification before supporting a theorem.

The original approximately 57 MiB of search matrices are retained in the local Dropbox checkpoint's discovery-data folder, with hashes. They are deliberately excluded from Git because the 89 KB seed is sufficient for the independent certificate replay. This is a size decision, not a mathematical dependency omitted from the verifier.

## Analytical review

Two independent agents derived the signed singular-series main term. The root checked Fourier signs, the two shift signs, the 1/n density factor, packet support margins, the nonlinear-kernel replacement and the PNT convolution. The result uses Fazzari-Gerspach Lemma 2.7, not the endpoint-defective full two-sign formulation of Conjecture 1.8.

A further adversarial review checked the general support conditions and corrected the low-packet wording: the matched single variable is shorter than \(T\); near-comparable products inherit that bound, while non-comparable products are handled by Fourier decay. The concrete \((1.2,0.2)\) packet was unaffected. These reviews are internal AI-assisted checks, not external peer review.

The count-moment step was checked in two ways. Rudnick-Sarnak counts multiplicities and its starred sum uses distinct indices; a separate positive-majorant and Dirichlet-polynomial argument also proves the required fixed moments under RH.

The source refresh is a provenance and hypothesis audit. The external 0.67353820 calculation, complete Lean builds and the prime-gap projects were not independently rerun here. See source_refresh/SOURCE_RECEIPT.json for exact pins and limitations.

## Rebuild the integrated Markdown and PDF


```sh
python build_handoff.py
node render_pdf.cjs
```


The renderer uses the repository's existing tools/document-renderer packages (markdown-it and KaTeX), plus Playwright. Install the existing lockfile with npm ci in tools/document-renderer if needed. DOCUMENT_NODE_MODULES can point to an installed node_modules directory; PLAYWRIGHT_MODULE can point to the Playwright module; PLAYWRIGHT_CHROMIUM_EXECUTABLE can specify an existing Chrome/Chromium binary.

PDF generation fails on KaTeX errors or detected horizontal overflow. RENDER_QA.json records these checks. Structural page checks and rendered-page inspection are recorded separately in VALIDATION.json. The integrated Markdown preserves historical stages and marks the subsequent completion explicitly.

## Scope, risks and rollback

No runtime speed or memory-efficiency improvement is claimed; these are not benchmark results. Application npm/Rust infrastructure is unchanged.

The finite results have internal ordinary proofs and interval certificates, not an external peer review or a Lean formalization. The zeta conclusion remains conditional on a precise arithmetic input. The source papers' bounds and computational claims retain their own dependencies. The phase convention is ordinary attractive scalar heat throughout the finite certificate; circular DBM and real-line Gaussian regularization are separate processes.

Reverting this research-directory addition is the rollback. A full external proof review, formalization, an actual bound on the signed prime error, a large-N perturbation of positive mass, and a new prime-gap theorem remain future work.
