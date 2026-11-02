# The actual support saturates positive sampling at the power scale

Date: 2026-09-05. Status: ordinary geometric proof; the inherited support count and packet constants have been independently checked. The complete proof is awaiting the coordinator's final review. No improved actual-prime bound is proved in this task.

The Q^2 term in the Round 11 **positive local sampling inequality** cannot be reduced by a power of X uniformly on the full canonical complementary-modulus support. This remains true for trigonometric polynomials supported on the actual integer-frequency interval n near X, and after including the absolute squares of the actual coefficients S_v(a/d)M_d. An explicit packet obeying the same small-arc norm and derivative bounds makes this precise.

This is **not an obstruction for the genuine-prime polynomial or for the full signed pairing**. The sampling extremizer constructed here is an artificial band polynomial, not a prime sum. The exact signed Gram formula in Section 5 retains a possible route for improvement; it cannot be rejected using the positive sampling lower bound. Accordingly the result closes one proposed geometric shortcut, not every possible use of frequency geometry.

## 1. Actual arithmetic support already established in Round 11

Write

    Q=X^(523/1000), X^(1/6)<=H<=X^(2/7).

Fix the full canonical squarefree modulus family Q_X^full defined by the balanced complementary predicates of Round 9. Fix a nonnegative nonzero v in C_c^infinity(1,2), and let m_v=integral v>0. The actual completed coefficients are

    M_d=sum_(q in Q_X^full,d|q) mu(q)/q,
    C_(a/d)=S_v(a/d) M_d,
    S_v(beta)=sum_h v(h/H)e(-beta h), e(t)=exp(2 pi i t).

The frozen Round 11 conductor construction proves the following facts, including their quantifiers. There is a subfamily F_X of admissible moduli with

    F_X subset (Q/2,Q],
    |F_X| >= c0 Q/[2(log X)^348]                            (1)

for all sufficiently large real X. Here c0 is the explicit fixed positive constant in that report. Every d in F_X has 348 distinct prime factors, mu(d)=1, and

    M_d=1/d                                                    (2)

in the **full signed family**, because no larger multiple of d fits below Q. The construction checks the actual root bounds and both large-prime predicates; it is not an unconstrained Farey model.

For each such d there are at least d/(32H) integers

    1<=a<=d/(16H), gcd(a,d)=1,

and on all those actual reduced frequencies

    |S_v(a/d)| >= m_v H/(2 sqrt(2)),
    |C_(a/d)| >= m_v H/(2 sqrt(2) Q).                       (3)

These statements hold simultaneously and uniformly in the stated H range once X is sufficiently large. Their proof uses only the ordinary prime number theorem on fixed-ratio intervals and the verified complementary predicates. No estimate about short-interval primes or actual prime exponential sums is added here.

Let Omega_X be exactly the reduced fractions just described. Distinct pairs (a,d) give distinct frequencies, by coprimality. Equations (1)–(3) yield

    Omega_X subset (0,1/(16H)],
    |Omega_X| >= c0 Q^2/[128 H(log X)^348].                 (4)

Thus this very small arc contains many actual frequencies with actual coefficient size of order H/Q, up to fixed constants.

## 2. A microscopic cluster follows without a local distribution theorem

Partition [0,1/(16H)] into intervals of length at most 1/(100X), using at most

    ceil(100X/(16H)) <= 8X/H

intervals, for all sufficiently large X. By the pigeonhole principle some interval J_X contains K_X actual reduced frequencies, with

    K_X >= c0 Q^2/[1024 X(log X)^348].                      (5)

No equidistribution of the moduli or numerators inside subintervals is assumed. The one dense cell is forced by the already proved total count. Its occupation tends to infinity, since

    Q^2/X = X^(23/500)

dominates every fixed power of log X. This lower bound is uniform in H; H cancels in the average occupation.

Let beta_X be the midpoint of J_X. Every selected frequency in this cluster has distance at most 1/(200X) from beta_X. It still has a genuine reduced denominator in F_X near Q. We have not assigned new artificial locations to any frequency.

## 3. Explicit band polynomial and a lower bound for the sampling constant

Set N=ceil(X), M=floor(X/10), and define

    P_X(beta)=H^(-1/2) sum_(n=N)^(N+M-1)
                               e(n(beta-beta_X)).          (6)

For X sufficiently large, M>=X/20, and all its integer Fourier frequencies lie in [X,11X/10]. Its coefficient magnitudes are exactly H^(-1/2), in particular at most one. The carrier is in the same positive-frequency range as the prime polynomial; this is not a test function allowed an arbitrarily high bandwidth.

For beta in J_X factor out the unit-modulus carrier e(N(beta-beta_X)). Each remaining phase has magnitude at most pi/1000. Hence the real part of their sum is at least M/2, and

    |P_X(beta)| >= M/(2 sqrt(H)) >= X/(40 sqrt(H)).         (7)

Parseval gives the exact norm

    integral_0^1 |P_X(beta)|^2 d beta=M/H.                  (8)

Combining (5), (7) and (8),

    sum_(beta in Omega_X) |P_X(beta)|^2
       / integral_0^1 |P_X(beta)|^2 d beta
          >= K_X M/4
          >= c0 Q^2/[81920(log X)^348].                    (9)

Replacing the denominator integral by its restriction to ||beta||<=1/H only makes the ratio larger. The numerator could also be restricted to J_X. Therefore any positive local sampling estimate valid for every polynomial in this positive-frequency band must have sampling constant at least Q^2 times a fixed negative logarithmic power on the actual canonical support.

In particular no uniform bound of the form

    sum_(actual frequencies in the central arc) |P(beta)|^2
          <= O(Q^2 X^(-eta)) integral_(local arc) |P(beta)|^2

is possible for any fixed eta>0 in this class. Nor can the Q^2 term be replaced by X times any fixed logarithmic power: the ratio Q^2/X is the positive power X^.046. Allowing a smooth nonnegative arc cutoff which equals one on [0,1/(16H)] does not change this lower bound.

An analogous lower bound holds with the actual squared coefficient weights retained. By (3) and (9),

    sum_(all actual beta) |C_beta|^2 |P_X(beta)|^2
        / integral_0^1 |P_X(beta)|^2 d beta
          >= c0 m_v^2 H^2/[655360(log X)^348].              (10)

All omitted terms here are nonnegative. Thus cancellation between different signed moduli cannot remove this weighted quadratic lower bound: on the selected conductors their merged coefficient is exactly 1/d, and elsewhere the quadratic sum only increases. In the natural top-conductor normalization (Q/H)^2 |C_beta|^2, equation (10) again gives a sampling constant at least a fixed multiple of Q^2/(log X)^348. It concerns that positive weighted sampling operator; it does not assert that every possible reweighting or Cauchy-Schwarz arrangement is sharp, and it does not concern the signed linear pairing.

## 4. The packet even obeys the known small-arc envelopes

For every rho>=1/H, nonnegativity and (8) show

    integral_(||beta||<=rho) |P_X(beta)|^2 d beta
                    <= M/H << X rho.

Differentiating (6) coefficient by coefficient and applying Parseval gives

    integral_0^1 |P_X'(beta)|^2 d beta
        =4 pi^2 H^(-1) sum_(n=N)^(N+M-1) n^2
                    << X^3/H.

Therefore, simultaneously for every such rho,

    integral_(||beta||<=rho) |P_X'(beta)|^2 d beta
                    << X^3 rho.                            (11)

These are stronger than the log^4 versions supplied by the RH centered-prime input in Round 11. On the other hand (5) and (7) give

    sum_(beta in Omega_X) |P_X(beta)|^2
                    >> X Q^2/[H(log X)^348].               (12)

Consequently the already known norm and derivative envelopes, the positive integer-frequency band, and the actual dense-divisibility support together do not force a power improvement of the sampled energy. The location of the packet depends on the actual frequency cluster, as a worst-case operator test may.

The crucial limitation is equally explicit: P_X is **not** the centered genuine-prime polynomial E_f for a fixed smooth f. Its coefficients are phase-tuned across all integers. Equations (9)–(12) say nothing about whether E_f concentrates at this cell. A new bound excluding such concentration specifically for the prime coefficients, or a bound for the signed coefficient pairing, remains possible.

## 5. What signed weights could still accomplish

The positive sampling step bounds a sum of absolute squares. The actual completed expression is instead

    L(F)=sum_beta C_beta [F(beta)-r_beta F(0)],
    r_(a/d)=mu(d)/phi(d).                                  (13)

For F(beta)=sum_(n in I) b_n e(n beta), its exact dual coefficient sequence is

    K(n)=sum_beta C_beta [e(n beta)-r_beta],
    L(F)=sum_(n in I) b_n K(n).                             (14)

Thus the squared norm of this signed functional on the coefficient space is exactly

    sum_(n in I) |K(n)|^2
     =sum_(beta,gamma) C_beta conjugate(C_gamma)
          sum_(n in I) [e(n beta)-r_beta]
                        [e(-n gamma)-r_gamma].             (15)

The off-diagonal terms in (15) have signs and phases. Nothing in the lower bound for the diagonal positive sampling operator implies a lower bound for (15), or for its value on the actual prime coefficients. In particular, the packet in (6) is not asserted to align with the full coefficient vector C_beta.

Using the exact completion from Round 10, K has the arithmetic form

    K(n)=sum_(q in Q_X^full) mu(q)
       [sum_(h=n mod q) v(h/H)
          -phi(q)^(-1) sum_((h,q)=1) v(h/H)].               (16)

This finite identity holds coefficient by coefficient. When n is a genuine prime near X it is a unit modulo every q, so (16) is exactly the corresponding residue-discrepancy kernel. For arbitrary n, (16) is the Fourier-defined kernel in (14); it need not be identified with the original progression discrepancy with its additional nonunit restrictions.

For the actual prime pairing the coefficients are b_p=(log p)f(p/X) on primes and zero elsewhere. The primitive subtraction in (13)–(16) is retained. An improved estimate exploiting the full signed Gram (15), or cancellation between the prime coefficients and (16), could therefore improve Round 11. Such an estimate would analyze actual correlations of the permitted moduli, their varying residues and/or primes. It is not supplied by a larger minimum spacing, fewer frequencies in the central arc, or a smaller positive sampling norm.

## 6. Bounded decision and quantifier limits

No sharper upper bound for the actual prime pairing was obtained in this task. What is now ruled out is precise: a **uniform positive sampling or absolute-weight sampling improvement by a power**, based only on the Round 11 arc envelopes and canonical factorization support. The Q^2 sampling term is sharp up to logarithmic powers in that class, including on the correct integer-frequency band.

This does not rule out a deliberately pruned modulus family, a specially chosen signed shift profile, a direct signed-Gram argument, an improved prime-specific concentration theorem, or cancellation in the full genuine-prime pairing. In particular, it is not a proof that the remaining X^.023 in the actual arithmetic bound is unavoidable. Treating a worst-case artificial polynomial as the prime polynomial would be a logical error.

The small companion script checks exact exponent differences, the constants derived from the Round 11 count, and the finite completion identity on one fixed toy modulus family using formal cyclic Fourier arithmetic. That toy identity checks the placement of the primitive term, not the large-X support construction or a prime estimate. The actual support construction is an ordinary asymptotic proof already pinned in the source receipt. No parameter search or large computation was performed.
