# Round 8: the centered-prime residual

Read the [integrated report](../../reports/dyson_round8.md). This slice proves an RH-dependent short-prime projection identity for the actual zeta logarithmic derivative, and writes the remaining signed two-scale energy using the same centered prime error. The required lower bound remains open.

`resolvent-arithmetic/` contains the full contour/continuation proof, an independent audit accepting the final author hash, exact scalar certificates and bounded finite diagnostics. `spectral-positivity/` contains a fixed minorant, an actual determinantal-process obstruction, independent review and thirteen exact symbolic checks. The minorant gives only a weak bound and does not reach the target.

All ten received files are copied verbatim and pinned by `INTAKE_MANIFEST.json`; their local originals are preserved in the adjacent archive. From the repository root:

```text
python3 research/logs/round8-integration/recheck.py
```

The replay copies evidence into a temporary folder, compares both complete output JSON files, and adds eight exact rational endpoint cases, including a prime-power and a prime cutoff. Python, mpmath and SymPy suffice. Low-height numerical examples and scalar certificates do not verify a large-T zeta estimate. The analytic proofs remain ordinary proofs with internal review, without a novelty claim or formal verification.

Further coefficient-positivity arguments, generic point-process scans and parameter optimization are postponed. The remaining task is an arithmetic estimate for the displayed shared-error energy, or Round 7's compact prime-covariance target. Reverting this checkpoint removes this bounded slice without changing Round 7.
