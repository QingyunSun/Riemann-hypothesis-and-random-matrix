# Eleven roots with identical protected moments and pair/gap data, but different collision probabilities

**Finite model theorem (computer-assisted).** On eleven-point subsets of the 22 equally spaced sites, let the reference law be Tao's ACUE. Rotate the grid uniformly if a fully rotation-invariant circular law is desired. There is a strictly positive alternative law agreeing with ACUE on:

1. the joint distribution of the entire ordered pair-difference measure and the sorted nearest-neighbor gaps;
2. every balanced product of traces with equal positive and negative weights at most 11, in expectation.

Yet the two laws give different probabilities that the attractive deterministic scalar heat flow has no collision by elapsed time $s=\log(85/84)$. The weights of the new law can be obtained by a finite real-algebraic projection, specified below. This is a finite measurement-identifiability result. It supplies no assertion about actual zeta zeros, or a stationary infinite-volume AH model.

## Static directions and protected upper bound

Write $M=2N=22$, $B=\{0,\ldots,N-1\}$ and $\zeta=e^{2\pi i/M}$. The sites in a configuration $S$ form an $N$-subset. Fix one lexicographically canonical representative per dihedral orbit. Keep each ordered pair $(A_i,B_i)$ of distinct representatives whose orbits are complementary, whose sorted gap histograms agree, and with $A_i<B_i$ lexicographically. There are 1,489 disjoint pairs. Write $\Delta_i f=f(B_i)-f(A_i)$ for a dihedral-invariant measurement. Interchanging black and white preserves every pair count by half filling, so all these transfers preserve the distribution of the complete static summary.

We will bound the dimension of the protected test vectors on the transfers. Let $F_{e,x}=\zeta^{ex}$ be the Fourier matrix in natural increasing indices. For an $N$-subset $E$ set

$$f_E(S)=\frac{\det F_{E,S}}{\det F_{B,S}}.$$

The denominator is a nonvanishing Vandermonde determinant. Every balanced protected Laurent trace polynomial is a linear combination of the $f_E$ obtained as follows. Multiply its symmetric Laurent polynomial by the alternant with exponents $N-1,\ldots,0$ and expand in alternants with decreasing distinct exponents. Subtract $N-j$ from the $j$th exponent of such an alternant. The resulting weakly decreasing sequence $\nu$ has sum zero and $\sum_j\nu_j^+\le N$. Indeed, for every $r$, the sum of the largest $r$ exponents of any expanded term is at most the sum of the largest $r$ base exponents plus $N$. This follows by selecting those same $r$ terms before sorting; the total positive increment of the original monomial is at most $N$. Take the largest partial sum after subtracting the base sequence. Reducing exponents $\nu_j+N-j$ modulo $2N$ kills repeated residues, and sorting the surviving residue sets only introduces signs.

This gives a computable set $\mathcal E$ of size 3,956, obtained by listing all pairs of partitions of $k\le11$ of total length at most 11, padding with zeros and negating the second partition in reverse order. The $f_E$ are independent as functions on all $N$-subsets: the matrix of numerator minors is the invertible $N$th exterior power of the Fourier matrix; the denominators simply rescale columns. Independence is more than is needed for the upper bound.

Two commuting involutions act on this span. Reflection $R$ sends $E$ to $N-1-E$ modulo $2N$; its possible reordering factor is $(-1)^{h(N-h)}$, where $h=|E\cap[N,2N)|$. As $N=11$ is odd, this factor always equals one. Particle-hole interchange $C$ sends $E$ to $2N-1-E^c$ with sign $+1$. To see the latter, Jacobi's complementary-minor identity and $F^{-1}=M^{-1}\overline F^{\mathsf T}$ give $f_E(S^c)=\overline{\det F_{E^c,S}/\det F_{B^c,S}}$. The cofactor sign is $+1$ because $\sum E\equiv\sum B\pmod {2N}$. Shift both numerator and denominator row indices by $N$, obtaining the base row set $B$ in the denominator. The row permutation sign is $(-1)^{h(N-h)}=1$; reflecting to remove the conjugation gives exactly $2N-1-E^c$. The enumerator checks that $\mathcal E$ is stable under both operations.

The fixed-set counts of $1,R,C,RC$ are $3956,106,22,184$, respectively. Projecting onto reflection-even, complement-odd tests gives the dimension bound

$$\frac{3956+106-22-184}{4}=964.$$

Indeed symmetrization on individual dihedral orbits kills reflection-odd components, and differences between complements kill complement-even components. The real parts of balanced trace products suffice: dihedral averaging sets their imaginary parts to zero.

## Separating the survival row

Form $M_{k,\lambda,\mu;i}=\Delta_i(2\operatorname{Re}(p_\lambda\overline{p_\mu}))$ with $\lambda,\mu\vdash k\le 11$ and unordered partition pairs. Evaluate $\zeta$ at the primitive order-22 element $3^9\pmod{199}$ (or any primitive order-22 root). Conjugation sends this element to its inverse. This is a ring homomorphism $\mathbb Z[\zeta]\longrightarrow\mathbb F_{199}$. The resulting matrix has rank 964. Append the integer row $d_i=\mathbf1_{D(B_i)>s}-\mathbf1_{D(A_i)>s}$, where $D$ is first-collision time. The resulting matrix has rank **965**. A nonzero modular minor lifts to a nonzero complex minor. Combined with the characteristic-zero upper bound, $d$ therefore lies outside the real protected row span.

The entries of $d$ are independently certified by interval arithmetic rather than by classifying approximate numerical roots. For each configuration compute the monic polynomial

$$P_s(z)=\sum_{j=0}^N a_j(85/84)^{j(N-j)}z^j,\qquad P_0(z)=\prod_{x\in S}(z-\zeta^x)=\sum_j a_jz^j.$$

The scalar heat flow of the real, centered trigonometric polynomial has the same zeros. Evolution preserves self-inversiveness. From its first $N-1$ Newton sums compute the Hermitian Toeplitz matrix $H_{ij}=p_{i-j}$, $0\le i,j<N$, taking negative moments by conjugation. For simple roots $H=VJV^*$, where columns of $V$ are $(1,z,\ldots,z^{N-1})$ and $J$ exchanges off-circle reciprocal-conjugate partners and fixes unit-circle roots. A positive definite $H$ is equivalent to $N$ distinct unit-circle roots (a multiple root forces deficient rank). A negative pivot certifies some root is off the circle. A configuration with all simple unit-circle roots at $s$ has been collision-free up to $s$: reverse the flow, whose angular root evolution is repulsive gradient ascent for the logarithm of the absolute Vandermonde. That bounded-above product is initially positive and cannot fall to zero. Conversely, a nonunit root requires passage through a collision from the simple initial data.

The checker verifies strict signs for every pivot it uses at 144-bit precision. In the two sets of representatives 324 and 443 survive, respectively. The differences $(-1,0,1)$ occur with multiplicities $(137,1096,256)$. The finite field computation uses these certified integers.

## An explicit prescription for a strictly positive law

Select 964 independent rows from the modular echelon computation and let $A$ be those same rows evaluated in the real cyclotomic field. These rows span the characteristic-zero constraints. Define
$$v=d^{\mathsf T}-A^{\mathsf T}(AA^{\mathsf T})^{-1}A d^{\mathsf T}.$$
Then $Av=0$ and $dv=\|v\|^2>0$. Transfer mass $\epsilon v_i$ from orbit $A_i$ to orbit $B_i$, uniformly within each orbit. For example choose $0<\epsilon<\min_q w_{\rm ACUE}(q)/(1+\max_i|v_i|)$, with $q$ running over orbit masses. All original masses are positive. Unbalanced moments vanish after an independently uniform overall rotation. The strict change in survival probability is $\epsilon\|v\|^2$.

These transfers give a 525-dimensional protected kernel within the 1,489 chosen directions, and the displayed survival event cuts it by one dimension. This does not assert that 11 is the least possible number of roots. In particular a single rank computation modulo 101 at $N=10$ is insufficient to resolve that size.

## Periodic lift to every multiple of eleven

For $N=11r$, replace each base configuration by its full preimage under $z\mapsto z^r$. This is an $N$-subset of the $2N$ grid. Distinct seed orbits give distinct lifted dihedral orbits by projecting down. The circular difference measure of the lift consists of the $r$ preimages of each seed difference, each with multiplicity multiplied by $r$. Each nearest gap is divided by $r$ in angular coordinates and repeated $r$ times. Thus pairwise equality of the joint static summaries continues to hold.

The lifted traces vanish unless $r\mid k$, in which case $p'_{rj}=r p_j$. Every protected test on the lift either vanishes or becomes a constant multiple of an eleven-root protected test. The centered real trigonometric polynomial of each lift is proportional to $Q_0(rx)$, so its first collision time is the seed time divided by $r^2$. Starting from the actual ACUE law at size $N$, transfer a sufficiently small amount of mass between the lifted orbit pairs as before. The resulting law preserves every required moment and the entire joint static summary law while changing the survival probability at $r^{-2}\log(85/84)$. No uniform lower bound on the survival-probability difference follows.

## Replay

Run `python3 check_protected_survival.py` with NumPy and python-flint (tested with python-flint 0.9.0). Compare stdout to `PROTECTED_SURVIVAL_RECEIPT.json`. The two SHA-256 digests bind the deterministically ordered orbit list and the certified signed event row. The two rank computations are over a finite field. The sole numerical stage uses outward-rounded Arb balls and rejects any inconclusive pivot.
