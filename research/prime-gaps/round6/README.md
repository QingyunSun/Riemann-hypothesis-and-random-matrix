# Full cap-operator residual checkpoint

Read [the integrated report](../../reports/prime186_round6.md). The new fine-grid cap quotient is approximately 0.99446782090, a numerical improvement of 71.42 ppm, still below one. The frozen radial direction has a separate exact outside-span certificate. No arithmetic support restoration or smaller prime gap is proved.

- `operator-proof/`: full signed operator, true mass/adjoint, fragment-layer invariance and radial convolution derivation.
- `residual-audit/`: independent projection/error audit and exact rational model checks.
- `residual-trial/`: bounded numerical construction, all candidate data, compaction/provenance receipts, and 2-by-2 versus 78-dimensional comparison.
- `operator-diagnostic/`: independent marked-space regression, exact outside-span certificate and saved-array energy plot.

Set `PRIME186_SOURCE` to the pinned official `prime_gap_186_certificate.py` file, and set `PRIME186_TRIAL_ROOT` to this repository's `research/prime-gaps/round4/k39-trial` directory. The former must have SHA256 `7f71bdefcfe3bb5ca76a143929b3cb3f4156c21dc483253cda3077420f1e5de4`.

From the repository root, the bounded integration check is:

```sh
OPENBLAS_NUM_THREADS=1 python3 research/logs/round6-integration/recheck.py
python3 research/logs/round6-integration/archive_check.py
```

The first command supplies the old-trial directory automatically, runs in a temporary copy, and records its own logs without replacing original evidence. It requires NumPy, SciPy and SymPy. The second checks hashes and retained arrays, then replays the exact rational/modular independence certificate in a copy. Add `--full-array-directory PATH` to compare against the four full local archives when available. The optional plot uses Matplotlib. Regenerate the repository manifest only after reviewing new run logs.

Compact witnesses omit only the regenerable D density cache. Original full files are retained locally in `Astra-Local-Archive/round6-full-data`; public hash receipts identify them. The source scripts can regenerate that cache and the full integrals. Historical run metadata is preserved as recorded, including the distinction between early runs and later source-path/hash additions.
