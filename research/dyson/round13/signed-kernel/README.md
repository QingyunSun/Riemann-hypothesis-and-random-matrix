# Round 13: the actual signed kernel norm

[The report](SMOOTH_SIGNED_KERNEL_NORM.md) derives the smooth-window mean square of the exact residue kernel, with its primitive subtraction retained. It identifies the main term and a small-common-divisor CRT remainder, and bounds the norm at the available scale (X+Q^2)H log^4 X.

On the actual canonical support, a specified positive part of the signed remainder is at least a fixed multiple of Q^2 H/(log X)^696. **This is not a lower bound for the full remainder or norm:** other signed terms may cancel it. No improved prime estimate follows.

The result quantifies the cancellation still needed and explains why an unrestricted-coefficient norm estimate, even if close to its full-period main term, may be less useful than the Round 11 prime-specific bound.

Run the fixed exact checks using Python's standard library:

```sh
python3 check_signed_kernel_norm.py
```

The [JSON](check_signed_kernel_norm.json) checks 100 CRT compatibility cases, full-period mean and variance, all signed finite-window corrections, and the rational scale constants. Its small toy family and polynomial window check algebra only; the window is not C-infinity, and no rapid-decay theorem or asymptotic prime claim is tested numerically.

The [source receipt](source_receipt.json) pins the preceding exact completion, actual-support construction and sampling reports.
