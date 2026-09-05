# A fixed interaction between two large prime divisors

Date: 2026-09-05. Status: written ordinary arithmetic transfer extending the previously reviewed fixed-prime-moment argument. This new note awaits a separate full proof review. The diagnostic is negative and floating; no zeta-spacing theorem or numerical enclosure is claimed.

## 1. Exact arithmetic object

Fix tau=1/3, ell>=1 and a=ell^2. Write d=d_ell, with d(p^e)=(ell)_e/e!, and, for n<=L, define

    v_n=log(n)/log(L),
    S_k(n)=sum_(distinct p|n) (log(p)/log(L))^k, k>=2,
    C_L(n)=number of distinct prime divisors p|n with p^3>L,
    D_L(n)=C_L(n)(C_L(n)-1)/2.

There are at most two such distinct primes. Thus C takes values 0,1,2 and D takes values 0,1, with

    C^2=C+2D,  CD=2D,  D^2=D.

The new coefficient family is

    r_L(n)=d(n) H(v_n,S(n),D_L(n)),
    H(v,S,D)=F(v,S)+D J(v,S),

where F and J are fixed polynomials in finitely many variables. Every H in this family is uniformly bounded on n<=L. Its coefficients, threshold, number of marks and degree remain fixed as L tends to infinity. This is not a growing occupation-state limit.

The trial fixes ell=27/25. F has groups 1,S2,S3,S2^2, each multiplied by the five Legendre polynomials P_j(2v-1), 0<=j<=4. J has groups 1,S2, each multiplied by P_j(6v-5). There are 20 unmarked and 10 D-marked coefficients. The marked radial basis is scaled to [2/3,1], since D vanishes below total mass 2/3.

This D interaction is nonmultiplicative. On configurations with respectively zero, one and two large prime divisors, it takes values 0,0,1. It cannot be introduced by replacing each individual prime by one common scalar multiplier. It also jumps when the second large prime crosses the fixed threshold. No fixed finite polynomial in the continuous S_k variables realizes that jump on the relevant open prime-size configurations. The computational baseline is nevertheless only the specified 20-dimensional span: the new 30-dimensional span does not contain the old best 48-dimensional span.

## 2. Unmarked and singly marked measures

For a labeled index list I=(k_1,...,k_j), put |I|=sum k_i and

    m_I(a) = Gamma(a)/Gamma(a+|I|)
        * sum_(set partitions pi of the labeled indices)
              a^(number of blocks) product_(B in pi) Gamma(sum_(i in B) k_i),
    m_empty(a)=1.

The previously reviewed finite-mark arithmetic argument gives E_v product_i S_(k_i)=v^|I| m_I(a). Here E_v denotes the resulting conditional moment functional, not an assumed random-matrix model. The unmarked positive measures are first defined on all n>=1:

    (log L)^(-a) sum_(n>=1) d(n)^2/n delta_(log(n)/log(L)).

Their local weak limit is C_ell/Gamma(a) v^(a-1) dv. Restriction to v<=1 occurs after this limit; the full measure is not truncated before taking its Laplace transform. Small polynomial marks can be deleted uniformly because sum_(p|n,p<L^epsilon) u_p^k<=epsilon^(k-1). Fix epsilon, use the prime number theorem and the unmarked weak limit on the finite collection of marks, then send epsilon to zero.

For any polynomial P in the S_k, the C-marked limit is

    E_v[C P(S)]
      = a v^(1-a) integral_(tau)^v (v-t)^(a-1)/t
            E_(v-t)[P(S+(t^k)_k)] dt,

with value zero for v<=tau. Unlike the Round 7 threshold 1/2, this is generally an ASYMPTOTIC identity, not an exact coprime decomposition: p>L^(1/3) can divide the remaining factor m when n=pm.

Here is the required error explicitly. For ell>=1, d(pk)<=ell d(k), including when p divides k; hence

    sum_(m<=L,p|m) d(m)^2/m
        <= a/p sum_(k<=L) d(k)^2/k.

The factors H and any fixed polynomial in the marks are bounded, and C<=2 on n<=L. Replacing d(pm)^2 by a d(m)^2 and using the additive mark insertion outside the coprime set therefore costs at most a fixed constant times

    (sum_(k<=L) d(k)^2/k) * sum_(p>L^tau) p^(-2)
       = O_H,ell((log L)^a L^(-tau)).

After normalization this tends to zero. This same estimate handles a large designated prime appearing again among the polynomial background marks. Thus the formula does not import the stronger, false automatic-coprimality statement at the one-third threshold.

## 3. The genuinely new double mark has an exact decomposition

If D_L(n)=1, n has a unique unordered pair p<q of distinct divisors exceeding L^(1/3). Writing n=pqm gives

    m <= L/(pq) < L^(1/3) < min(p,q).

Consequently p and q occur exactly once and are automatically coprime to m. In particular

    d(pqm)^2=a^2 d(m)^2,
    S_k(pqm)=S_k(m)+u_p^k+u_q^k.

For every test polynomial Phi, exactly

    sum_(n<=L) d(n)^2/n D_L(n) Phi(v_n,S(n))
      = a^2 sum_(L^tau<p<q,pq<=L) 1/(pq)
          sum_(m<=L/(pq)) d(m)^2/m
            Phi(v_m+u_p+u_q,S(m)+(u_p^k+u_q^k)_k).

Applying the same finite-product measure limit yields

    E_v[D P(S)]
      = (a^2/2) v^(1-a)
          integral_(t>tau,s>tau,t+s<v)
            (v-t-s)^(a-1)/(ts)
            E_(v-t-s)[P(S+(t^k+s^k)_k)] dt ds.

It vanishes for v<=2tau. The factor 1/2 converts the unique unordered pair into an ordered integral. The removed equal-prime diagonal has an extra reciprocal-prime factor, is O((log L)^a L^(-tau)) before normalization, and also has zero limiting two-dimensional measure.

All prime thresholds stay fixed. The planes t=tau, s=tau, t+s+v=1, and the corresponding operator-insertion planes have zero limiting measure. No uniform pointwise estimate for every short background cutoff is asserted: use the joint product-measure weak limit first, restrict away from the total-mass boundary, and then remove this restriction. The residual density w^(a-1) is locally integrable for a>0; the already available uniform total-mass bound controls the discarded shrinking background strip. This includes m near one.

## 4. Insertions and the three-state interpolation

Let chi(u)=1_(u>tau). For a prime multiplier not already dividing the input integer,

    C -> C+chi(u),
    D -> D+C chi(u).

For two distinct new prime multipliers,

    C -> C+chi(u)+chi(w),
    D -> D+C(chi(u)+chi(w))+chi(u)chi(w).

The polynomial S_k inserts u^k, or u^k+w^k, as usual. Define H0, Hu, Hw and Huw by these exact rules together with their total-mass arguments v, v+u, v+w and v+u+w.

The code does not treat C as binary. For an insertion product q(C)P(S), its three possible background values determine it exactly:

    E_v[q(C)P(S)] = q(0) E_v[P]
       + (q(1)-q(0)) E_v[C P]
       + (q(2)-2q(1)+q(0)) E_v[D P].

For marked factors on the left and right, the code sets

    q(c) = choose(c+number of large left insertions,2)^(left mark)
           * choose(c+number of large right insertions,2)^(right mark).

The exponents are zero or one. The interpolation identity is only used at c=0,1,2, where it is exact even if the expression for q is a higher-degree polynomial. Impossible background/insertion configurations have zero measure by the total-mass constraint. This construction retains the mixed terms involving a single background large prime as well as the event with two large inserted primes.

## 5. The arithmetic limiting quadratic forms

For x_n=r_L(n)/sqrt(n), retain the exact arithmetic creation matrix

    (A_L)_(p^e m,m)
      = 2 sin(pi e log(p)/(2log(L)))/(e sqrt(p^e)),  p^e m<=L.

Define

    I = integral_0^1 v^(a-1) E_v[H0^2] dv,

    M2 = (2 ell^2/pi^2) integral_(v+u+w<=1)
            v^(a-1) sin(pi u/2)/u sin(pi w/2)/w
            E_v[H0 Huw+Hu Hw] dv du dw,

    M3 = (2/pi^2) integral_(v+u<=1)
            v^(a-1) sin^2(pi u/2)/u E_v[H0^2] dv du.

Then, for fixed H with I>0,

    [||A_L x||^2+x^T A_L^2 x]/[2pi^2 ||x||^2]-1/4
       -> (M2+M3)/I-1/4.

The inherited proof is applicable because the added marks are bounded and their thresholds fixed. More explicitly, remove operator primes below L^epsilon and prime powers with e>=2 using the previously proved weighted Schur bounds, valid uniformly for arbitrary signed vectors:

    ||A_L||=O_ell(1),
    ||A_(p<L^epsilon)||=O_ell(sqrt(epsilon)+(log L)^(-1/2)),
    ||A_(e>=2)||=O_ell((log L)^(-1/2)).

The standard norm inequalities for A*A and A^2 show that the normalized quadratic forms change by o(1)+O(sqrt(epsilon)). With retained primes, collisions with the background or another designated prime have the reciprocal-square error just described. The fixed polynomial marks and bounded C,D do not invalidate that estimate. The ordered distinct-prime terms then use d(mp)d(mq)=a d(m)^2 and d(m)d(mpq)=a d(m)^2 on the coprime part, yielding the two terms of M2 with the displayed coefficients.

There are two different diagonals. In A*A, p=q gives r_L(m)^2/(mp) and survives: this is M3 with uninserted H0 squared. In A^2, repeated p gives the extra p^(-2) and vanishes after the retained-prime restriction. No g(u)^2 or inserted D is attached to M3. First let L tend to infinity at fixed epsilon, then send epsilon to zero. This completes the written fixed-family extension; it has no growing-family or uniform-in-degree assertion.

The source interface remains Inoue, arXiv:2604.05733v1, Theorems 3 and 4 / combined Proposition 3 under RH, with L=floor(T/(log T)^2). The previously audited coefficient-uniform normalized error and theta=log L/log T ->1 comparison are unchanged by this bounded fixed resonator. A positive limiting margin could feed that source argument. The present negative trial supplies no such consequence. In particular it supplies neither a gap bound nor an AH refutation; multiplicities and near-zero AH pairs would still need the correct treatment after any future successful small-gap argument.

## 6. Quadrature and verification boundary

For the C moment set delta=v-tau and t=v-delta z. Its endpoint factor is delta^a; the remaining z integral has Jacobi weight z^(a-1). For the D moment put

    delta=v-2tau,
    t=tau+delta(1-z)s,
    w=tau+delta(1-z)(1-s),
    background=delta z.

The Jacobian is delta^2(1-z), so the endpoint factor is delta^(a+1), with residual weight z^(a-1)(1-z)/(tw). The coefficient remains a^2/2. These are the substitutions implemented in `marked_values`.

The v integration is divided at tau and 2tau. For each v slab, the u integration is divided at tau and 1-v-tau in their correct order, and the w integration is divided at tau where present. No positive-weight quadrature cell straddles an inserted-prime step. The v endpoint powers above are absorbed by Jacobi rules. Norm and M3 use the same three-state decomposition with no inserted large primes.

This is deterministic quadrature, not a rigorous error enclosure. A 20/32 comparison and independent raw adaptive integrals check its implementation but do not certify the small observed gain. The separate exact checks establish finite arithmetic identities only. Full coefficients, M/G arrays, a frozen rational vector and the actual-integer operator evaluation are retained; none of these numeric checks is substituted for the transfer argument.
