# Requested Mellin-template follow-up on existing arrays

This is a transparently post-initial-result check requested by the coordinator before R28 freeze. It was not part of the original three-matrix plan. No new prime computation, matrix, height, profile, or mode subtraction is permitted.

For each saved matrix of dimension n, use exactly 4n uniformly spaced frequencies from zero through t_max = pi/min_j(log d[j+1]-log d[j]). This reaches the largest local Nyquist scale of the nonuniform log-coordinate samples; a nonuniform grid has no unique global alias-free Nyquist frequency. Record also pi/max_j(delta log d) and pi/mean_j(delta log d). The grid is a finite oversampled template test, not an optimization over every real frequency or an aliasing theorem.

At each t, project the saved unit leading eigenvector onto span{cos(t log d),sin(t log d)}. Evaluate the equivalent rotated basis using log(d/d_mid) for numerical stability. At t=0 the span is the constant vector alone. For positive t use the full 2-by-2 Gram inverse, retain the smallest Gram eigenvalue and reject any unhandled rank deficiency. Verify the winning projection independently by QR. Record all frequencies, squared overlaps and Gram diagnostics, along with the winning frequency and dimensionless frequency t/T. Since the saved matrix is real symmetric, left and right top singular vectors differ only by the sign of its eigenvalue, so their squared template projections are identical; check this explicitly.

Freeze one script and one result/array set. Interpret a large winning projection only as coherence of this finite leading vector in the tested templates. Do not infer an asymptotic operator lower bound or remove that mode from the target.
