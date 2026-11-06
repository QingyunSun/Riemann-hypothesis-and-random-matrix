# Ten is the first possible size for a survival-changing tilt

With a grid of $2N$ sites, the joint law of the complete pair-difference counts and sorted adjacent gaps, together with all protected balanced traces, determines the distribution of collision time for $N\le9$. At $N=10$ two positive laws meeting all these constraints, one of them ACUE, can have different survival distributions. One of the times $\log(73/72)$ and $\log(71/70)$ distinguishes them. The proof selects at least one of these two times; the eleven-point theorem separately certifies a single specified time.

## Exhaustive obstruction below ten

Group dihedral orbits by their static summary. Transfers from a chosen reference in each group to its other orbits span all possible orbit-mass variations preserving that joint summary law. Their dimensions are $0,0,0,0,0,3,10,44,208$ at $N=1,\ldots,9$. The corresponding protected matrix has full column rank modulo the primes listed in the receipt. All entries arise by reducing real cyclotomic integers at a primitive $2N$th root in the residue field; the full-column minors remain nonzero in characteristic zero. Thus the orbit masses, hence every invariant statistic, are fixed. On an independently uniformly rotated grid this suffices for any unlabelled circular heat survival event.

## Complement cycles at ten

Form a multigraph whose vertices are static summaries. Each complementary pair of *distinct dihedral orbits* gives one edge, oriented from its smaller canonical representative to the other. Moving mass along the edge changes the two orbit weights by equal and opposite amounts, and changes summary masses by the incidence vector of that edge. Even for different endpoint summaries, a graph circulation preserves the full summary law. All such transfers annihilate complement-even test functions and, after dihedral symmetrization, reflection-odd test functions.

There are 2,234 edges. A spanning-forest computation yields 496 independent integral fundamental cycles including 462 self-loops, with 530 distinct edges used by the cycles. A direct conservation check at every vertex is included. To form each probe row, take its oriented edge differences, then sum these with signs around each cycle.

The protected rank upper bound follows from the same exterior-Fourier-minor proof as the eleven-point note. At even $N$ the reflection action on $E$ has sign $(-1)^{h(N-h)}$, where $h$ counts its upper-half indices. The Jacobi complement operation still has sign $+1$: the two-block permutation made by shifting $E^c$ by $N$ and the subsequent reflection sign cancel because $E^c+N$ has the same number $h$ of upper-half indices as $E$. Thus the signed traces for the four involutions $1,R,C,RC$ are $(1957,87,19,129)$; complement-odd, reflection-even dimension is at most $(1957+87-19-129)/4=474$.

Evaluating protected traces with $\zeta_{20}\mapsto32$ in $\mathbb F_{101}$ gives rank 473 on the cycle basis. Append two survival rows, computed by the same certified Hermitian-inertia method at the two rational values of $e^s$ given above. The combined rank is 475, strictly greater than the characteristic-zero upper bound of 474. Therefore at least one true survival row escapes the protected span. Project that row to the protected nullspace in the cycle coordinates and take a sufficiently small multiple of the resulting signed circulation. The starting ACUE masses are positive, so this supplies a positive alternative law and proves the assertion. The modular rank 473 alone does not establish that the characteristic-zero restricted rank is 473.

Periodic lifting of these ten-point transfers extends the conclusion to all multiples of ten, with times divided by the square of the lift factor. Along each chosen cycle, the original vertices map deterministically to lifted static summaries, so cancellation at vertices descends to the lifted transfers even if distinct summaries coalesce.

Run `python3 check_first_size.py` from the directory containing `check_protected_survival.py` and compare the result with `FIRST_SIZE_RECEIPT.json`.
