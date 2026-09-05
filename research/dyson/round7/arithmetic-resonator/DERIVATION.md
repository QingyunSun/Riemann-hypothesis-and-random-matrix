# Arithmetic transfer for a fixed large-prime sector

**Status:** ordinary proof extension of the fixed symmetric-prime transfer argument, plus deterministic numerical implementation. The fixed-family transfer has received a separate [independent internal review](INDEPENDENT_REVIEW.md), including its truncations and insertion terms. This is not formal verification or external peer review. Its numerical experiment remains negative.

## 1. Fixed family and normalization

Fix ell>=1, a=ell^2, and the multiplicative coefficients

    d_ell(p^e)=(ell)_e/e!.

For n<=L set

    v_n=log(n)/log(L),
    S_k(n)=sum_(p|n, distinct) (log(p)/log(L))^k,  k>=2,
    C_L(n)=sum_(p|n) 1_(p>sqrt(L)).

Since n<=L, C_L(n) is exactly zero or one. A repeated prime p>sqrt(L) cannot divide n. Thus C^2=C without approximation. We allow a fixed polynomial

    H(v,S,C)=F(v,S)+C J(v,S),

where S denotes finitely many S_k. Fixed radial Legendre polynomials are included in this class. All variables satisfy 0<=v<=1, 0<=S_k<=1 and C in {0,1}, so H is uniformly bounded. Its coefficients do not vary with L.

The resonator coefficients and creation matrix are

    r_L(n)=d_ell(n) H(v_n,S(n),C_L(n)),
    x_n=r_L(n)/sqrt(n),
    (A_L)_(p^e m,m)=2 sin(pi e log(p)/(2log(L)))/(e sqrt(p^e)).

The normalized half-gap main term is

    Q_L = [||A_L x||^2 + x^T A_L^2 x]/[2 pi^2 ||x||^2] - 1/4.

The target is a *positive limiting value*, not a finite-L value or a positive coefficient in one summand.

## 2. General unmarked moments

For a list of labeled positive integers I=(k_1,...,k_j), write K=sum I. The existing marked-prime expansion gives

    E_v product_i S_(k_i) = v^K m_I(a),

where

    m_I(a) = [sum_(set partitions pi of {1,...,j})
                  a^(number of blocks) product_(B in pi) Gamma(sum_(i in B) k_i)]
             / (a)_K,
    m_empty(a)=1.

This follows directly by grouping equal marked primes in the product and integrating the distinct-prime logarithmic sizes. It is not an assumption of an asymptotic Poisson-Dirichlet model. The same formula may of course be interpreted using that probability distribution.

For completeness, the unmarked positive measure is

    (log L)^(-a) sum_(n>=1) d_ell(n)^2/n delta_(log(n)/log(L)),

on all n>=1. Its Laplace transform tends to C_ell t^(-a), giving local weak convergence to

    C_ell/Gamma(a) * v^(a-1) dv.

The full measure is first treated on compact logarithmic intervals, and then restricted to v<=1; it is not truncated at n=L before taking its Laplace transform. The independent review gives the explicit short-background limiting procedure.

To derive the displayed product moment, restrict every marked prime to p>=L^epsilon, apply the prime number theorem to the finitely many reciprocal-prime measures, and use the unmarked weak limit for the remaining factor. Background collisions and coincident distinct marks have an extra reciprocal prime and vanish. At n<=L,

    sum_(p|n,p<L^epsilon) (log(p)/log(L))^k <= epsilon^(k-1),

so deleting the small marked primes changes any fixed polynomial in the S_k by O_H(epsilon). First let L tend to infinity with epsilon fixed, then let epsilon tend to zero. The joint limiting densities assign zero mass to simplex cutoff boundaries. This is the same finite-mark argument as the previously reviewed S2 transfer, now with a finite general list of k>=2; it needs no uniform pointwise asymptotic at each individual prime tuple.

## 3. The new large-prime marked moment: an exact integer decomposition

There is an especially simple exact starting identity. If C_L(n)=1, then uniquely

    n=p m, p>sqrt(L), m<=L/p<p.

Hence p and m are coprime, p occurs exactly once, and

    d_ell(pm)^2 = a d_ell(m)^2,
    S_k(pm)=S_k(m)+u_p^k.

For every test function Phi on the displayed variables, exactly

    sum_(n<=L) d_ell(n)^2/n * C_L(n) Phi(v_n,S(n))
      = a sum_(p>sqrt(L),p<=L) 1/p
          sum_(m<=L/p) d_ell(m)^2/m
            Phi(v_m+u_p, S(m)+(u_p^k)_k).

There is no coprimality error in this decomposition: m<p makes it automatic. The prime variable stays in the compact logarithmic interval (1/2,1], so its limiting measure is dt/t by the prime number theorem. Combine this with the unmarked and finitely marked background weak limits from Section 2. The boundaries t=1/2 and t+w=1 have zero limiting measure. The potentially short background is included in that weak convergence; it is not replaced by an unjustified uniform asymptotic in m.

At fixed total v<=1, the resulting moment is zero for v<=1/2. For v>1/2 it is

    E_v[C product_(i in I) S_(k_i)]
      = a v^(1-a) sum_(A subset of the labeled index set I) m_(I\A)(a)
          integral_(1/2)^v
            t^(sum_(i in A) k_i - 1)
            (v-t)^(a-1+sum_(i notin A) k_i) dt.

Repeated entries of I are still labeled in this subset sum, so their binomial multiplicities are retained. Every product involving C^r, r>=1, uses this same moment because C^2=C. The formula therefore evaluates all norm and insertion moments of the fixed family F+CJ.

An independent internal reviewer checked this formula and uniqueness at the half threshold. The exact integer decomposition above provides its arithmetic justification independently of any probability-model interpretation.

## 4. Insertion rules and the two distinct diagonal mechanisms

Put chi(u)=1_(u>1/2). On the simplex v+u+w<=1, define

    H0  = H(v,     S,                  C),
    Hu  = H(v+u,   S+(u^k)_k,          C+chi(u)),
    Hw  = H(v+w,   S+(w^k)_k,          C+chi(w)),
    Huw = H(v+u+w, S+(u^k+w^k)_k,      C+chi(u)+chi(w)).

At most one of the background and inserted primes can exceed the half threshold. These are precisely the changes of the distinct-prime statistic away from the already negligible operator/background coincidences.

The limiting forms are

    I = integral_0^1 v^(a-1) E_v[H0^2] dv,

    M2 = (2 ell^2/pi^2) integral_(v+u+w<=1)
           v^(a-1) sin(pi u/2)/u * sin(pi w/2)/w
           E_v[H0 Huw + Hu Hw] dv du dw,

    M3 = (2/pi^2) integral_(v+u<=1)
           v^(a-1) sin^2(pi u/2)/u * E_v[H0^2] dv du.

With I>0,

    Q_L -> (M2+M3)/I - 1/4.

To check the normalization and indexing, first restrict A_L to prime multipliers p>=L^epsilon. Then

    ||A x||^2 = sum_(n<=L) 1/n sum_(p,q|n) alpha_p alpha_q
                     r_L(n/p) r_L(n/q),

    x^T A^2 x = sum_(mpq<=L) alpha_p alpha_q/(mpq)
                     r_L(m) r_L(mpq),

with alpha_p=2 sin(pi log(p)/(2log L)). The ordered distinct-prime terms give the two displayed M2 products, with no additional factor of two.

The p=q terms in A^*A have n=mp and contain r_L(m)^2. They survive and give M3 with **H0 squared**, not an inserted H_u. Conversely, p=q in A^2 costs p^(-2); its retained-prime contribution vanishes. This distinction is unchanged by adding the large-prime mark and is implemented explicitly.

The uniform operator truncation estimates from the previous transfer proof apply to every vector x:

    ||A_L||=O_ell(1),
    ||A_(p<L^epsilon)||=O_ell(sqrt(epsilon)+1/sqrt(log L)),
    ||A_(prime powers e>=2)||=O_ell(1/sqrt(log L)).

They follow by the positive Schur weight d_ell(n)/sqrt(n), the logarithmic-derivative divisor identity and submultiplicativity for ell>=1. They do not require H to be nonnegative or continuous as a function of a mark. After these truncations, coincidences are negligible by the same reciprocal-square bounds and uniform boundedness of H. Every remaining discontinuity is at a fixed prime-size threshold with zero limiting mass. This completes the extension of the fixed-family arithmetic limit.

## 5. Interface with actual zeta zeros

The source is [Inoue, arXiv:2604.05733v1, Theorems 3 and 4](https://arxiv.org/html/2604.05733v1#S3). The paper's theorem assumes RH and permits arbitrary resonator coefficients subject to its product cutoff. Use L=floor(T/(log T)^2), so theta=log L/log T tends to one; the same Schur comparison controls replacement of theta by one in the sine kernel. No finite integer table is used as a substitute for that limit.

A fixed strictly positive limiting margin at phi=1/2 would make a half-gap improvement a meaningful next consequence after handling the source's continuity and error terms. This trial's margin is negative, so there is no new zero-spacing theorem. Even a successful small-gap statement must preserve the distinction between zeros counted with multiplicity and a gap interval separated from zero; it cannot automatically refute every half-lattice formulation of the Alternative Hypothesis.

## 6. Numerical quadrature adapted to the discontinuity

The unmarked block is the ordinary smooth simplex integral. For every block with at least one C factor, the M2 integrand is supported only in three disjoint sectors:

1. v>1/2: the background can contain the unique large prime; u,w<1/2 automatically.
2. u>1/2: the inserted u-prime is large, and v,w<1/2.
3. w>1/2: the symmetric inserted-prime sector.

In the first sector the marked moment factors as `(v-1/2)^a` times a smooth function, so a Jacobi rule absorbs that factor. The other two sectors use the usual v^(a-1) Jacobi weight and smooth triangular substitutions. No quadrature cell crosses a step in chi. M3's marked block only uses the first, background sector.

This is why the order-20, order-28 and order-40 calculations are stable without a dense multidimensional mesh. Their agreement is a useful independent numerical check, not a rigorous error enclosure.
