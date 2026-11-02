# Removing the shift-length loss from the actual completed pairing, under RH

Date: 2026-09-05. Status: ordinary proof independently audited and accepted for the stated RH component bound; see [the separate review](SMALL_ARC_INDEPENDENT_REVIEW.md). This proves a bound for the same fixed smooth discrepancy component as Round 10, assuming RH. It does not prove the needed zeta covariance estimate, AH failure, Montgomery's conjecture, or a new prime-gap bound. No novelty claim is made for the classical small-arc method.

With the Round 10 notation

    X=T^alpha, 6/5<=alpha<=7/5,
    H=X/T=X^theta, 1/6<=theta<=2/7,
    Q=X^(523/1000),

the conclusion is

    |D_Q^V(X,T)| <<_(V,chi) sqrt[X(X+Q^2)] (log X)^5
                     << X^(1023/1000) (log X)^5.                 (1)

Compared with Round 10's unconditional bound X^(1023/1000) sqrt(H) log^4 X, this removes the factor sqrt(H), at the explicit additional assumption of RH. The saving in the exponent of X is theta/2, ranging from 1/12 to 1/7. It still leaves an X^(23/1000) power loss relative to X log X, before logarithms. Thus this is a useful component improvement, not the requested historical conjecture.

## 1. Exact object, ranges and the arithmetic input

Keep the actual squarefree family Q_X contained in (sqrt(X),Q], the discrepancy convention and the kernel from the frozen Round 10 report:

    Delta(F;h mod q) = sum_(m=h mod q) F(m)
                       - phi(q)^(-1) sum_((m,q)=1) F(m),

    w_h(u)=chi(u/X) a_u(X) a_(u+h)(X)
                         sinc_0(T log(1+h/u)),
    a_u(X)=min((u/X)^(1/2),(X/u)^(3/2)),

    D_Q^V = sum_h V(h/H) sum_(q in Q_X,(q,h)=1) mu(q)
                 Delta(Lambda(m) w_h(m-h) log((m-h)/q);h mod q), (2)

where V is fixed in C_c^infinity(1,2), chi is fixed in C_c^infinity(1,3/2), and sinc_0(x)=sin(x)/x with its removable value at zero. Functions inside Delta are zero outside their stated support. Formula (1) actually holds for any squarefree subfamily in this modulus interval; no new dense-divisibility property is assumed.

The primary analytic input is Bhowmik–Schlage-Puchta, [Mean representation number of integers as the sum of primes](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/Goldbach4.2.10.pdf), Lemma 3, printed page 3. For

    R_x(beta)=sum_(n<=x) (Lambda(n)-1) e(beta n),
    e(t)=exp(2 pi i t),

it proves under RH that

    integral_(-1/y)^(1/y) |R_x(beta)|^2 d beta
                    << (x/y) (log x)^4,  1<=y<=x.             (3)

The author's proof uses Selberg's short-interval mean square and Gallagher's lemma, including the cutoff endpoint contributions. We use this already proved centered small-arc bound, not an asymptotic pair-correlation conjecture. The fourth logarithmic power is retained.

We first treat a separated smooth amplitude f(m/X)v(h/H), with f,v compactly supported in fixed positive intervals. Restoring the actual kernel and logarithm is done in Section 6. All reduced frequencies have the complete range

    2<=d<=Q, 1<=a<d, gcd(a,d)=1, beta=a/d.                    (4)

There is no zero frequency: its centered completed contribution vanishes exactly. Neither a lower cutoff d>sqrt(X) nor an inherited cutoff on numerator a is asserted. The arc weights, rather than the original modulus lower bound, suppress small d.

## 2. Centered genuine primes, smooth weights and derivatives

For fixed smooth f supported in [c,C], with 0<c<C fixed, set

    A_f(beta)=sum_p (log p) f(p/X)e(beta p),
    B_f(beta)=sum_n f(n/X)e(beta n),
    E_f(beta)=A_f(beta)-B_f(beta).                            (5)

The sum defining B_f is over integers; this is not a silently substituted continuous main term. The polynomial E_f has genuine-prime coefficients minus the integer mean.

First apply partial summation to the Lambda-minus-one prefix polynomials in (3). Minkowski's integral inequality gives, for 1/X<<rho<=1/2,

    integral_(||beta||<=rho) |sum_n (Lambda(n)-1)
                                   f(n/X)e(beta n)|^2 d beta
                              <<_f X rho (log X)^4.          (6)

We only need rho>=1/H, so the length y=1/rho is at most H=o(X) and eventually less than every prefix endpoint x>=cX occurring in partial summation. For larger constant arcs one may equally use Parseval. The constants depend on the sup norm and total variation of f on a fixed interval.

Replacing Lambda by genuine primes subtracts the finite polynomial supported on p^j near X with j>=2. Its absolute value is at most

    sum_(p^j near X,j>=2) log p << sqrt(X) (log X)^2.

Its squared integral on this arc is therefore O(X rho log^4 X). Consequently (6) holds for E_f itself. There is no use of a critical-strip prime Dirichlet series here.

The derivative is exactly

    E_f'(beta)=2 pi i X E_(u f(u))(beta).

Applying the same argument with u f(u) proves

    integral_(||beta||<=rho) |E_f'(beta)|^2 d beta
                              <<_f X^3 rho (log X)^4.        (7)

This controls the frequency derivative by another source-backed centered prime polynomial. No small L2 estimate has been differentiated formally.

## 3. Sampling the small arc at distinct Farey frequencies

Distinct reduced fractions in (4) are separated on the circle by at least Q^(-2). Around each selected frequency choose a disjoint interval of length comparable to Q^(-2). For any continuously differentiable F, the fundamental theorem of calculus applied to |F|^2, followed by averaging on each such interval, gives

    sum_(beta in selected frequencies) |F(beta)|^2
      << Q^2 integral_U |F(t)|^2 dt
          + integral_U |F(t) F'(t)| dt,                      (8)

where U is their union. One direct proof is to bound |F(beta)|^2 by the interval average plus 2 integral |F F'| and then sum over the disjoint intervals. This is a local estimate; the integrals do not need to run over the whole circle.

If ||beta||<=rho, then U lies inside ||t||<=rho+O(Q^(-2)). Throughout our range rho>=1/H and Q^2>>H, this enlargement is O(rho). At arcs reaching the whole circle use Parseval for F and F'. Inserting (6)–(7) into (8), and applying Cauchy–Schwarz only to its derivative integral, gives

    sum_(d,a as in (4), ||a/d||<=rho) |E_f(a/d)|^2
                  <<_f X (Q^2+X) rho (log X)^4.              (9)

This is the arithmetic gain: centering and the RH prime mean square supply the factor rho. Merely knowing that the number of frequencies is smaller would not justify (9) with this factor. The local sampling argument does not replace the minimum spacing Q^(-2) by a larger spacing.

## 4. Dyadic frequency tails, with every coefficient retained

For the separated shift weight put

    S_v(beta)=sum_h v(h/H)e(-beta h),
    M_d=sum_(q in Q_X,d|q) mu(q)/q,
    C_(a/d)=S_v(a/d) M_d.                                   (10)

Round 10's exact completion gives the pairing

    sum_(d,a as in (4)) C_(a/d)
                 [A_f(a/d)-mu(d)A_f(0)/phi(d)].              (11)

We use only |M_d|<=(1+log(Q/d))/d. Finite summation by parts gives, for each fixed integer J>=2,

    |S_v(beta)| <<_(v,J) H(1+H||beta||)^(-J).                (12)

Partition all nonzero reduced frequencies into the central arc I_0 with ||beta||<=1/H and the annular bands

    I_j: 2^(j-1)/H < ||beta|| <= min(2^j/H,1/2), j>=1,      (13)

stopping when the circle has been covered. For each band, the numerator condition is exactly on min(a,d-a). In the central arc it is min(a,d-a)<=d/H; in I_j it lies between 2^(j-1)d/H and 2^j d/H, with the upper half-circle clipping. Nonempty arcs with upper radius rho require d>=1/rho. This treats low denominators, not just the top block.

For fixed d the number of fractions in an arc of upper radius rho<=1/2 is at most 2 rho d, even before imposing coprimality. Using (12), the divisor-coefficient bound, and summing 1/d proves

    sum_(beta in I_j) |C_beta|^2
                  <<_(v,J) H 2^((1-2J)j) (log(2Q))^3,      (14)

with j=0 interpreted as the central arc. The factors implicit in the first annulus are absolute constants. No sharp truncation of S_v has been made.

Apply (9) with rho at most 2^j/H, or with the whole-circle Parseval bound at the final band. Cauchy–Schwarz on I_j gives

    |sum_(beta in I_j) C_beta E_f(beta)|
      <<_(f,v,J) sqrt[X(Q^2+X)]
                    2^((1-J)j) (log X)^(7/2).              (15)

The series over j converges already for J=2. Therefore

    |sum_beta C_beta E_f(beta)|
                   <<_(f,v) sqrt[X(Q^2+X)] log^(7/2) X.     (16)

Unlike the unweighted Round 10 sampling, this retains the concentration in a width 1/H arc and also bounds every tail band.

## 5. Both mean terms in the completed pairing

Two terms remain after A_f is replaced by E_f. They are different and are bounded separately.

First, B_f is a smooth integer polynomial. Poisson summation gives, for each fixed A>0,

    |B_f(beta)| <<_(f,A) X(1+X||beta||)^(-A).

Every nonzero fraction in (4) has ||beta||>=1/Q, while X/Q is a positive power of X. Also (12) implies

    sum_(a=1)^(d-1) |S_v(a/d)| <<_v d                       (17)

for every d: compare with an integral when d>=H, and use the convergent a^(-J) sum when d<H. It follows that sum_beta |C_beta|<<Q log(2Q). Thus the B_f contribution is at most

    O_(f,v,A)(X Q log(2Q) (X/Q)^(-A)),                      (18)

which is negligible with a fixed sufficiently large A. This estimate uses the discrete integer mean itself, so no continuous/discrete substitution error is hidden.

Second, the exact primitive Ramanujan principal term in (11) is bounded by

    |A_f(0)| sum_(d<=Q) |M_d| |mu(d)|/phi(d)
                                   sum_(a,d)=1 |S_v(a/d)|
         <<_f,v X log(2Q) sum_(d<=Q) 1/phi(d)
         <<_f,v X (log(2Q))^2.                             (19)

Here |A_f(0)|<<_f X follows from Chebyshev, and the elementary reciprocal-totient sum is O(log Q). Using a global Cauchy–Schwarz bound for this principal term would unnecessarily reintroduce an H loss; (19) avoids it without asserting cancellation.

Together (16), (18), and (19) prove the separated pairing estimate. Frequencies d=1 remain absent because their completed centered contribution is identically zero, not because a large term was discarded by hand.

## 6. The actual logarithm, smooth kernel, and prime-power discrepancy

The log q version of M_d costs one extra logarithm. Its analogue of (14) has log^5 rather than log^3, so (16) has log^(9/2). The corresponding principal term (19) costs at most log^3. The factor log X is treated explicitly in the same way.

For the actual amplitude, use epsilon=1/T, y=m/X, z=h/H. The frozen Round 10 proof and its independent kernel audit show that it is exactly

    V(z) chi(y-epsilon z) y^(-3/2) (y-epsilon z)^(-3/2)
        sinc_0(integral_0^z du/(y-epsilon u)),                (20)

and that this function and its product with log(y-epsilon z) have uniformly bounded mixed derivatives of every fixed order on a fixed rectangle. The source identity

    log((m-h)/q)=log X-log q+log(y-epsilon z)

is retained. Expand the smooth amplitudes in a two-variable Fourier series with fixed outer cutoffs. Unlike the earlier global sampling proof, the constants here depend on the variation of the m-factor as well as the derivatives of the h-factor. Both costs grow polynomially in the two Fourier indices, and the uniform rapid decay of the coefficients absorbs both. Thus the bound sums for the actual kernel, with no approximation error or unrecorded oscillatory derivative loss. We round log^(9/2) up to log^5.

The exact completion used genuine primes to make every m near X a unit modulo q. The original discrepancy (2), however, contains Lambda. The frozen Round 10 argument bounds the change in both its progression and principal sums by

    O_eta(H X^(1/2+eta) log^3 X + H sqrt(X) log^4 X).        (21)

This is logically distinct from subtracting the finite prime-power polynomial in (6). The former makes the modulus completion exact; the latter identifies the centered prime polynomial used in the source mean-square estimate. Both are included. Fixing eta=1/100 makes (21) o(X log X) uniformly for H<=X^(2/7), so it is smaller than (1). This completes the proof.

## 7. Quantitative decision and remaining arithmetic task

The improved exponent is 1.023 throughout the entire specified theta range. At theta=1/6 the previous exponent was 3319/3000=1.106333..., and at theta=2/7 it was 8161/7000=1.165857.... The conditional power savings are respectively 1/12 and 1/7. They are comparisons between an RH consequence and the earlier unconditional component estimate; the assumption change is material.

After the actual covariance normalization 1/(X log T), a bound of this size is still O(X^.023 log^4 X), which does not tend to zero. Ordinary RH small-arc control therefore removes the shift-length loss but does not settle the selected divisor component at the required precision. Replacing (3) by a conjectural sharp variance asymptotic would not by itself remove the Q^2 sampling scale used in this proof.

The remaining task is quantitative cancellation in the actual signed pairing of the conductor coefficients M_d and the centered genuine-prime exponential sums, or another argument improving the aggregate top-conductor contribution beyond this sampling/Cauchy–Schwarz bound. No statement that such cancellation is impossible is made. The independent conductor lane checks whether the source support removes high d; this proof does not assume that it does.

The only computation here is a small exact check of exponents, finite arc counting, and the dyadic geometric factors. The proof uses no fitted constants, zeta-zero sample, coefficient search, or unbounded scan. Other divisor pieces and omitted covariance ranges remain outside its scope.
