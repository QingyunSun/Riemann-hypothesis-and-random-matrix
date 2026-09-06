# Round 7: actual-zeta tests for Dyson–Montgomery

Read the [integrated report](../../reports/dyson_round7.md) first. This checkpoint contains two precise conditional reductions, a negative arithmetic trial, and a dynamical obstruction. Neither required zeta inequality is proved.

| Folder | Mathematical content | Evidence |
|---|---|---|
| `poisson-resolvent/` | Two-scale log-derivative mean square cancels the AH diagonal parameter; a liminf of at least 1/16 would refute AH-Pairs under RH | Complete ordinary proof, two independent reviews across folders, exact scalar enclosures and finite-model checks |
| `dyson-frontier/` | One compact Fourier bump on [6/5,7/5], with an explicit centered prime-covariance kernel | Primary-source audit and finite kernel normalization check |
| `arithmetic-resonator/` | Fixed unique-large-prime mark, its arithmetic transfer and a 30-feature negative trial | Independent proof review, exact integer identities, full matrices, rational coefficients and finite integer evaluations |
| `true-zeta-flow/` | Gap-independent contraction, remaining boundary estimate, deterministic hard-core example and DBM noise obstruction | Ordinary derivations, exact checks and numerical force calibration |

`INTAKE_MANIFEST.json` records every received source hash, the complete local reference archive and the three publication edits. Author manifests pin the original bytes; the intake manifest pins the portable public versions. The 14 third-party PDF/text reference files are preserved locally, with public URLs and hashes in `dyson-frontier/sources/download_manifest.json`. They are not reproduced in Git.

From the repository root, run the bounded integration replay:

```text
OPENBLAS_NUM_THREADS=1 python3 research/logs/round7-integration/recheck.py
```

The replay uses a temporary copy because the original scripts write adjacent outputs. It rechecks exact identities, the two-scale thresholds, the compact prime kernel, one order-40 continuum calculation, and the frozen rational vector through L=10^6. It excludes only recorded timing fields when comparing JSON and requires identical saved matrix arrays. It does not launch a parameter scan or sample actual zeta zeros.

For direct copied-folder use, `ASTRA_PRIME_FEATURES_SOURCE` can specify the prior `general_prime_features.py` file; its expected hash is pinned in the integration script. The default path works in this repository. Python with NumPy, SciPy, SymPy and mpmath is sufficient; no model API or Rust component is needed.

The next task is an arithmetic estimate for the signed two-scale mean square or compact prime covariance. More repetitions of the same negative resonator, prime-gap sweeps, and formalization of an unclosed conjecture argument are postponed. Reverting this checkpoint removes this slice without changing the earlier handoff.
