# When the protected moments restore the missing information

## Six points, an exact obstruction

Let a configuration be a six-subset of a regular twelve-gon. Its static summary is the ordered cyclic difference-count vector jointly with the sorted list of its six adjacent gaps. Allow any law on the configurations, with an optional uniform rotation of the grid. If two laws have the same distribution of this summary and the same expectations of the three real moments

$$T_k=\operatorname{Re}(p_1p_{k-1}\overline{p_k}),\qquad k=2,3,4,$$

their pushforwards to the dihedral orbit space are identical. Consequently every rotation- and reflection-invariant measurement, including the entire law of first collision time, agrees. All three moment tests are balanced with weight at most 4 on each side, inside the protected band for six points.

**Proof.** Enumerate the $\binom{12}{6}=924$ subsets. Retain one representative per rotation/reflection orbit and group these representatives by their static summary. There are 50 orbits and 47 distinct summaries. Forty-four summaries determine a single orbit. The remaining three each contain the following pair of representatives, with site zero at the top:

| Fibre | First orbit | Second orbit |
|---|---|---|
| I | 0,1,2,4,7,8 | 0,1,2,5,6,8 |
| II | 0,1,3,4,7,9 | 0,1,3,5,6,9 |
| III | 0,1,3,6,7,10 | 0,1,3,6,8,9 |

Equality of the summary laws leaves three unknown orbit-mass changes, one per fibre, with opposing signs within the fibre. Write $z=e^{\pi i/6}=(\sqrt3+i)/2$ and $p_j(S)=\sum_{x\in S}z^{jx}$. Substitution gives the following first-minus-second differences, with rows indexed by $k$:

$$
\begin{pmatrix}
4&2&-6+4\sqrt3\\
-8&-4&-6+2\sqrt3\\
0&12&6-6\sqrt3
\end{pmatrix}.
$$

Its determinant is $864-480\sqrt3\ne0$. Thus all three changes vanish. The argument uses dihedral pushforwards of arbitrary laws and does not require the given laws themselves to be dihedrally invariant. The conclusion applies to invariant observables. It does not identify an origin-sensitive law on labelled configurations.

**Small extensions.** Enumerating the same fibres gives free orbit-mass counts of 0 at four and five points, 10 at seven points, 44 at eight and 208 at nine. At seven, eight and nine, evaluating all real parts of the balanced trace products of equal positive and negative weight at most $N$ in a finite field gives ranks 10, 44, and 208. A full-column minor remaining nonzero modulo a prime admitting a primitive $2N$th root of unity proves nonvanishing in characteristic zero via the cyclotomic ring homomorphism. Rank deficiency at a single residue prime does not certify characteristic-zero nonuniqueness.

## Why a bound at six points cannot be extrapolated to all sizes

Take $N=3m$ and write a circular binary word as alternating occupied and vacant runs. In each color use $2m$ runs, $m$ of length one and $m$ of length two. A word starting at the beginning of an occupied run is specified by two lists of lengths, hence there are $B_m^2$ such ordered encodings, with $B_m=\binom{2m}{m}$. The two color classes have the same gap histogram because the multisets of occupied and vacant run lengths agree. They also have the same pair counts by half-filling.

A self-complementary dihedral orbit admits a symmetry exchanging the colors. Once the occupied run length list, the target vacant run for the first occupied run and the orientation are specified, the entire vacant list is fixed. There are at most $4m B_m$ self-complementary encodings. A dihedral orbit has at most $4m$ different encodings with a chosen occupied-run start and orientation. After dividing by two for the complement pairs, there are thus at least $(B_m^2-4m B_m)/(8m)$ disjoint pairs of distinct dihedral orbits with identical static summaries. Independently transferring mass in each pair preserves the joint summary law exactly.

There are at most $2\sum_{k=1}^N p(k)^2$ real constraints from the balanced traces; $p(k)$ is the number of partitions. This is $\exp(O(\sqrt N))$, while the number of transfers grows exponentially in $N$. For all sufficiently large multiples of three, some nonzero real transfer annihilates every protected test. A small multiple added to ACUE gives a probability law, since every distinct-site configuration has positive ACUE mass. Making the law rotation-invariant also annihilates all unbalanced trace expectations.

**Scope.** This proves the existence, for large sizes, of positive distinct dihedral-orbit laws matching the entire protected class and the full joint static summary law. Proving a difference in collision survival requires showing that at least one survival function is outside the span of the constraints on these transfer directions. Dimension counting by itself supplies no such statement. The small-size rigidity and the large-size existence address separate claims.
