# Round-five evidence archive

Start with [the integrated report](../../reports/prime186_round5.md). This directory preserves the original exact certificates, numerical search, proof notes and logs. It reports no smaller prime gap.

- `exceptional-radius/`: an ordinary derivation of the variable-radius exceptional-square estimate and seven exact rational constants.
- `geometry-audit/`: fifteen exact source/cap cases, twelve accepted natural templates, the uniform one-layer trim, and proof obligations for fresh physical integrals.
- `geometry-trial/`: ten coarse and two fine cap-only 77-coefficient optimizations, including all twelve matrix archives and negative results.
- `INTAKE_MANIFEST.json`: hashes of the 53 received files and the two path-only publication edits.

For the portable replay, set `PRIME186_SOURCE` to a local copy of `prime_gap_186_certificate.py` from official commit `61340d0b74163003b32756bb16e91d9209a5e330`, then run from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 python3 research/logs/round5-integration/recheck.py
python3 tools/verify_manifest.py
```

The first command requires Python, NumPy and SciPy, checks the primary source SHA256, and runs certificate scripts in a temporary copy. Its execution logs and comparison receipt go under `research/logs/round5-integration/`. It does not rerun the full finite-matrix search or change the original evidence. A new integration run changes its own output logs, so review and record those changes before regenerating the repository manifest.

The individual scripts otherwise write adjacent outputs; use an isolated copy when replaying them. The exceptional-radius certificate itself uses only the Python standard library. The original detailed search report describes the staging source path; the published parser additionally accepts `PRIME186_SOURCE`. Its original manifest is preserved as execution provenance, while the intake and repository manifests describe the published files.

The integrated report also clarifies a numerical scope point: the smallest error/residual maxima in the original search report describe the twelve full-77 candidates. The archive contains two additional truncations per point; their full-pencil residuals can be larger. All thirty-six vectors are included in the integration receipt.
