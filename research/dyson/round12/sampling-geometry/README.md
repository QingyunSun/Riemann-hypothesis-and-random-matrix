# Round 12: actual-support sampling geometry

[The report](ACTUAL_SUPPORT_SAMPLING_OBSTRUCTION.md) proves that the positive local sampling constant remains at least Q^2/(log X)^348 on actual canonical complementary-modulus frequencies. It includes the actual squared coefficient weights and an explicit test polynomial with the correct positive-frequency bandwidth and the known small-arc envelopes.

This excludes a power improvement of that **positive sampling step**. It does not establish an obstruction for the prime polynomial or full signed pairing, and it does not improve the current actual-prime bound. The report records the exact signed Gram and residue kernel that remain available for further work.

The [source receipt](source_receipt.json) pins the actual-modulus construction and the preceding completion proof. Reproduce the small exact checks with Python's standard library:

```sh
python3 check_sampling_geometry.py
```

The resulting [JSON](check_sampling_geometry.json) verifies the rational constants and 60 finite signed-kernel identities in one formal cyclotomic example. The toy moduli are used only to test algebra; no numerical realization of the asymptotic source family or prime estimate is claimed.
