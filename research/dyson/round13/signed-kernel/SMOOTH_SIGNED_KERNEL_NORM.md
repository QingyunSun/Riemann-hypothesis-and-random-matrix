# The signed kernel norm: exact main term and a large coherent CRT remainder

Date: 2026-09-05. Status: ordinary proof draft, independent review pending. No stronger actual-prime upper bound is claimed. The finite-kernel identities and estimates here require no RH assumption; the comparison with the Round 11 prime-specific bound retains that bound's RH hypothesis.

This task derives the exact smooth-window main term for the unrestricted dual norm retained in Round 12, bounds its remainder at the currently available scale, and isolates a positive part of that actual signed remainder of size

    >> Q^2 H/(log X)^696, Q=X^.523,

on the full canonical source-supported family. Other signed terms may cancel it. Thus it is not a lower bound for the complete norm or a prime obstruction. It proves that the dangerous long-period CRT interactions really occur in the permitted support and require quantitative cancellation if one wants a smaller norm bound.

The currently proved upper bound remains

    sum_n W(n/X)|K(n)|^2 <<_(v,W) (X+Q^2)H log^4 X.       (1)

This does not improve the Round 11 prime-specific small-arc estimate. Even an ideal evaluation by the full-period main term would generally be too large for unrestricted-coefficient Cauchy–Schwarz to replace that estimate.

## 1. Exact finite kernel and its mean

Fix X large, X^(1/6)<=H<=X^(2/7), Q=X^(523/1000), a squarefree family Q_X contained in (sqrt(X),Q], and a fixed real v in C_c^infinity(1,2). Write v_h=v(h/H), and define

    V0=sum_h v_h,
    U_q=sum_((h,q)=1) v_h,
    B_q(n)=sum_(h=n mod q) v_h,
    b_q=U_q/phi(q),
    K(n)=sum_(q in Q_X) mu(q)[B_q(n)-b_q].                (2)

Take a fixed nonnegative nonzero W in C_c^infinity(1,3/2), with Fourier convention

    W_hat(t)=integral W(u)e(-tu)du, w0=W_hat(0)>0.

The norm to be estimated is N_W=sum_n W(n/X)|K(n)|^2. The coefficients in K are exactly those in Round 12. For a genuine prime n near X it is the actual completed residue discrepancy. For nonunit composite n it is the unrestricted Fourier-defined dual kernel; that distinction is not suppressed.

Define the full-period mean

    M=sum_q mu(q)[V0/q-b_q].                              (3)

The reduced-frequency representation is

    K(n)=M+sum_beta C_beta e(n beta),
    C_(a/d)=S_v(a/d) A_d,
    A_d=sum_(q in Q_X,d|q) mu(q)/q,
    S_v(beta)=sum_h v_h e(-beta h),                        (4)

over all distinct reduced fractions 2<=d<=Q, 1<=a<d. In particular

    M=-sum_beta C_beta mu(d)/phi(d).

The Round 11 first-power shift estimate sum_a |S_v(a/d)|<<_v d and |A_d|<=(1+log(Q/d))/d give

    |M|<<_v log^2(2Q),
    C2:=sum_beta |C_beta|^2<<_v H log^3(2Q).               (5)

The primitive centering is therefore present. It is not assumed equal to the unrestricted mean V0/q for each modulus.

## 2. Exact CRT covariance and main term

For q1,q2 let g=gcd(q1,q2), L=lcm(q1,q2)=q1q2/g. Simultaneous congruences n=h1 mod q1 and n=h2 mod q2 are solvable precisely when h1=h2 mod g. When compatible, denote their unique residue modulo L by r(h1,h2).

The smooth count of that progression is exactly, by Poisson summation,

    sum_(n=r mod L) W(n/X)
       = X/L sum_(k in Z) W_hat(kX/L)e(kr/L).             (6)

The zero mode is Xw0/L. The covariance after subtracting the unrestricted means V0/q_i has full-period value

    Gamma(q1,q2)
       =[g sum_(h1=h2 mod g) v_h1 v_h2 - V0^2]/(q1q2).

Let

    R_v(g)=g sum_(h1=h2 mod g) v_h1 v_h2 - V0^2
           =sum_(r=1)^(g-1) |S_v(r/g)|^2 >=0.             (7)

Grouping these frequencies by their reduced denominators yields the exact identity

    sum_(q1,q2) mu(q1)mu(q2) R_v(gcd(q1,q2))/(q1q2)
          =sum_beta |C_beta|^2=C2.                        (8)

The left side retains the actual signs and common-divisor compatibility; its individual terms cannot be treated as independent congruences. The identity follows alternatively from orthogonality over a common period. It is not an asymptotic assertion about the X-window.

Consequently the exact main term for N_W is

    X w0 (M^2+C2).                                         (9)

All nonzero modes in (6), and the analogous single-modulus modes of the centering terms, constitute the remainder. The latter single-modulus modes have period at most Q=o(X), so their total is O_A(X^(-A)) for every fixed A, by smooth Poisson decay, with constants depending on finitely many derivatives of v,W. The same is true for the integer-period correction to sum_n W(n/X).

Thus

    N_W=Xw0(M^2+C2)+E_CRT+O_A(X^(-A)),                   (10)

where the explicit signed remainder is

    E_CRT=X sum_(q1,q2) mu(q1)mu(q2)/L
       sum_(k!=0) W_hat(kX/L)
       sum_(h1=h2 mod g) v_h1 v_h2 e(k r(h1,h2)/L).       (11)

This is an equality with a controlled smooth-window error; no assertion that E_CRT is negligible is made.

## 3. Only the small-common-divisor remainder survives at power scales

Choose the fixed cutoff G=X^(1/10). It lies strictly between Q^2/X=X^(23/500) and the least H=X^(1/6).

If g>=G, then

    L<=Q^2/G=X^(473/500), X/L>=X^(27/500).

The nonzero Poisson sum in (6) is therefore O_B((X/L)^(1-B)). There are at most Q^2 modulus pairs, and the absolute total h1,h2 weight is O_v(H^2). Choosing B sufficiently large for any requested A shows that the entire g>=G portion of (11) is O_A(X^(-A)). No cancellation or short-interval hypothesis is used for this removal.

The zero-mode covariance for g<G is also negligible. Since g/H<=X^(-1/15), (12)'s shift estimate from Round 11 gives, for each fixed J>=2,

    R_v(g)<<_(v,J) H^2(g/H)^(2J).

Here every nonzero r/g has distance at least 1/g from the integers, and summing r^(-2J) gives the displayed bound. Multiplying by X, using sum_(q<=Q)1/q<<log Q, and choosing J large proves that the g<G portion of the main covariance in (8) is O_A(X^(-A)). Thus the substantial full-period covariance comes from shared divisors larger than G, where the CRT averaging itself is harmless.

The problematic term is exactly

    E_small = the expression (11) restricted to gcd(q1,q2)<G,

and (10) remains true with E_small in place of E_CRT, up to O_A(X^(-A)). Small-gcd compatibility is not a reason to discard this term: it is precisely where the least common multiple can exceed X.

For comparison, the elementary finite-spacing bound on (4), applied on the support of W, proves

    N_W <<_(v,W) (X+Q^2 log(2Q))C2 + X M^2
          <<_(v,W) (X+Q^2)H log^4 X.

Combining this actual upper bound with (5), (9), and nonnegativity gives

    |E_small| <<_(v,W) (X+Q^2)H log^4 X.                  (12)

The current remainder bound exceeds the natural XH main scale by Q^2/X=X^.046, up to logarithms. The exact source root predicates have not supplied cancellation in (11).

## 4. The remainder contains actual small determinants

There is an equivalent and simpler frequency form of the remainder. By (4), smooth Poisson summation on n gives

    E_small
      = X sum_(beta!=gamma) C_beta conjugate(C_gamma)
                       W_hat(X(gamma-beta))
          + O_A(X^(-A)),                                  (13)

where all frequency differences are represented in (-1/2,1/2]; integer aliases away from this representative are negligible. Cross terms with M are negligible because every nonzero beta has distance at least 1/Q from the integers. Equal frequencies give exactly the main C2. For reduced denominators d1,d2, a common divisor at least G forces a nonzero frequency distance at least G/Q^2, so rapid Fourier decay independently makes those terms negligible. The gcd of reduced denominators is not silently identified with the gcd of arbitrary original moduli in (11). On the isolated top conductors used in Section 5, however, d_i=q_i exactly, so the identification there is legitimate.

To make the dangerous arithmetic ranges explicit, fix any small epsilon>0, for example epsilon=1/100. By rapid decay of W_hat and S_v, one may restrict (13), at a cost O_A(X^(-A)), to nonzero signed numerators r_i with

    beta=r1/d1, gamma=r2/d2,
    2<=d_i<=Q, gcd(r_i,d_i)=1,
    0<|r_i|<=X^epsilon d_i/H,
    0<|r2 d1-r1 d2|<=X^epsilon d1d2/X.                   (14)

The residues here are centered near the integers. Bounds are uniform after choosing sufficiently many fixed derivatives to absorb the polynomial number of terms. There are no terms with exactly one zero numerator in these ranges: its nonzero partner would have magnitude at least 1/Q, which exceeds X^epsilon/X. The determinant is divisible by gcd(d1,d2); its small nonzero size is the CRT resonance.

This is not a source-class distribution conclusion. The allowed-support predicates constrain prime factors of each modulus separately. They do not state cancellation in the signed determinant pairing (13)–(14). In fact the next section shows that such pairs are forced inside the full canonical support.

## 5. A positive coherent part of the actual signed Gram has the large scale

For this lower bound on a **part** of the remainder, specialize to the full canonical family and a fixed nonnegative nonzero v. Let m_v=integral v. The frozen Round 11–12 arithmetic construction supplies a set Omega_X of actual reduced frequencies such that

    Omega_X subset (0,1/(16H)],
    |Omega_X|>=c0 Q^2/[128H(log X)^348],
    d in (Q/2,Q], A_d=1/d,
    |C_beta|>=m_v H/(2sqrt(2)Q),
    arg C_beta in [-pi/4,0].                              (15)

The phase statement follows directly from v_h>=0 and H<h<2H: each term in S_v(beta) lies in that sector. The identity A_d=1/d holds in the full signed family, so it is not changed by other negative-Mobius moduli.

Partition the small arc into at most J<=8X/H cells of length at most 1/(100X), and let m_j be their actual occupations. Since |Omega_X|/J tends to infinity,

    sum_j m_j(m_j-1) >= |Omega_X|^2/J-|Omega_X|
       >= c0^2 Q^4/[262144 XH(log X)^696]                 (16)

for all sufficiently large X, uniformly in H. This counts ordered pairs of distinct actual frequencies in the same cell.

On each such pair, |X(gamma-beta)|<=1/100. In the integral for W_hat, u lies in (1,3/2), so the added phase has magnitude at most 3pi/100. Together with the coefficient phase difference at most pi/4, the total is at most 7pi/25<pi/3. Consequently

    Re[X C_beta conjugate(C_gamma)
                          W_hat(X(gamma-beta))]
         >= X w0 |C_beta C_gamma|/2
         >= X w0 m_v^2 H^2/(16Q^2).                      (17)

Let E_coherent be exactly the sub-sum of (13) over these ordered within-cell pairs, without any other terms. Equations (16)–(17) prove

    E_coherent >= c0^2 w0 m_v^2 Q^2 H
                       /[4194304(log X)^696].             (18)

This is an actual contribution with the actual merged coefficient signs; it is not obtained by replacing the full remainder by absolute values. Its definition is symmetric in beta,gamma and it is real.

Moreover, distinct fractions with denominators d1,d2 satisfy

    |beta-gamma|>=gcd(d1,d2)/(d1d2).

Every pair used in (18) therefore has

    gcd(d1,d2)<=Q^2/(100X)<G.                             (19)

Its reduced CRT period is at least 100X. Thus these are precisely nonzero long-period modes in the small-gcd region, not harmless diagonal or large-gcd contributions. The root support cannot make this region empty.

**Equation (18) is not a lower bound for E_small or N_W.** All remaining signed pairs define E_other=E_small-E_coherent and may cancel it. For example, a norm estimate N_W<<XH log^A X would force

    E_other=-E_coherent+O_(v,W,A)(XH log^max(A,4) X),       (20)

up to the negligible errors already stated. Since Q^2/X=X^.046 dominates log^(696+A) X, this would be cancellation at the scale of the coherent block. We have identified and quantified the missing cancellation, not proved that it is unavailable.

## 6. Why the unrestricted norm may be the wrong target

The full-period coefficient norm in (9) satisfies C2>>_v H/(log X)^348 on the canonical family, by Round 11, and C2<<_v H log^3 X. If one could show that the smooth-window remainder is small compared with this main term, the resulting unrestricted norm would therefore have size XH up to logarithmic powers.

Ordinary Cauchy–Schwarz against the genuine-prime coefficient vector, whose squared norm is O_f(X log X), would then only give Xsqrt(H) times logarithms. This is already worse in the present H range than the Round 11 prime-specific small-arc bound X^1.023 log^5 X. Reaching o(X log X) by unrestricted-coefficient Cauchy–Schwarz would instead require N_W=o(X log X), subject to matching a window majorizing the coefficient support. That is far below the natural full-period main scale.

This is a conditional scale comparison, not a proved lower bound for N_W: (11) may have negative signed contributions. It explains why evaluating the dual norm alone need not attack the desired prime correlation. A stronger argument may need the alignment of the actual prime vector with K, rather than its largest value on all coefficient vectors.

The bounded result is (10)–(12) together with the explicit actual coherent block (18). There is no new power-saving upper bound. The remaining obligation is a signed small-determinant/CRT correlation estimate, or a prime-specific pairing estimate that avoids the unrestricted norm. No root factorization, common-divisor independence or Mobius cancellation was assumed without proof.

## 7. Verification scope

The companion exact-arithmetic check verifies the CRT mean/covariance identities and finite-window remainder on one fixed small squarefree family, with all signs and primitive subtractions retained. It also checks the rational cutoff exponents and the coherent-block counting constants. These are algebraic checks, not a numerical realization of the asymptotic modulus family or evidence for the required cancellation. No parameter scan, numerical prime experiment, or previous-round edit was performed.
