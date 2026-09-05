# Round 11: centered prime frequencies

[The proof](CENTERED_SMALL_ARC_BOUND.md) bounds the actual Round 10 smooth discrepancy component by

    |D_Q^V| << sqrt[X(X+Q^2)] log^5 X = X^1.023 log^5 X,

**assuming RH**. It removes the earlier factor sqrt(H). The remaining power loss X^.023 still prevents the required covariance estimate. This does not establish AH failure, Montgomery's conjecture, or a new prime-gap bound.

[The independent review](SMALL_ARC_INDEPENDENT_REVIEW.md) covers the analytic proof. [The source receipt](source_receipt.json) pins the primary small-arc theorem and frozen Round 10 dependencies. Third-party PDF/text source bodies are local references and need not be distributed with this package.

Reproduce the small exact bookkeeping checks using only Python's standard library:

```sh
python3 check_small_arc_bound.py
```

The script writes [check_small_arc_bound.json](check_small_arc_bound.json). It verifies rational exponents, one finite Farey partition, frequency spacing and dyadic geometric factors. It is not a numerical test or proof of RH, the source mean-square theorem, or an asymptotic prime-distribution claim.
