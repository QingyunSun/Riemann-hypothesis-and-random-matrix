# Goldston--Yıldırım constructions for the actual R26 covariance

Scope: source-statement and selected proof-step audit, plus elementary derivations below. I did not audit either complete paper or search for every later improvement. The checked second-paper version is arXiv:math/0412366v1. This note supplies tools and legal application tests; it proves no bound on Z_T.

## Primary inputs actually checked

[Paper I, published version](https://math.colgate.edu/~integers/d5/d5.pdf), (1.1), defines
\[
\Lambda_R(n)=\sum_{d\mid n,\ d\le R}\mu(d)\log(R/d).
\]
Its (1.4) mixed correlations have one genuine Lambda factor. The introduction, printed page 2, expressly leaves two distinct genuine prime factors outside its evaluated correlations. Theorems 1.3--1.4 impose cutoff and shift restrictions; their headline statements alone do not authorize the current growing physical-shift family.

[Paper II, checked v1](https://arxiv.org/pdf/math/0412366v1), (1.1), defines
\[
\lambda_R(n)=\sum_{r\le R}\frac{\mu(r)^2}{\varphi(r)}
\sum_{d\mid(r,n)}d\mu(d).
\]
Theorem 2, printed page 8, requires
\[
N^\epsilon\ll R\ll N^{\vartheta/(k-1)-\epsilon},\qquad
\max|j_i|\ll N^{1/(k-1)-\epsilon},\quad k=2,3.
\]
The distribution input allows theta=1/2 unconditionally. Section 10, printed pages 42--43, explains why summing its per-shift Bombieri--Vinogradov error fails for power-length intervals. Its replacement uses Hooley's GRH estimate (1.47); conditions (10.12)--(10.14) include `h log h=o(R)` and `sqrt(h) R=o(sqrt(N)/log^2 N)`. Theorem 3, page 9, assumes GRH and only reaches `h<<N^(1/7-epsilon)`.

These statements and the relevant displayed derivation in Section 10 were read directly. The Ramanujan interpretation on printed page 2 motivates the first construction below. None of these sources establishes the ordinary-RH upper bound required by the current programme.

## Tool 1: turn divisor coefficients into a rational-frequency basis

Use a notation distinct from the actual complementary coefficient: let
\[
\operatorname{Ram}_r(n)=\sum_{a\bmod r,\ (a,r)=1}e(an/r)
=\sum_{d\mid(r,n)}d\mu(r/d).
\]
For squarefree r, `mu(r/d)=mu(r)mu(d)`. Therefore, by a finite coefficient identity,
\[
\boxed{\lambda_R(n)=\sum_{r\le R}\frac{\mu(r)}{\varphi(r)}
\operatorname{Ram}_r(n).}
\]
There are no convergence or limiting assumptions here. The representation exposes the individual reduced rational frequencies and their exact coefficients, which can be kept together with the real physical weight.

For any fixed positive integers r,s and q=lcm(r,s), orthogonality over a full period gives
\[
\frac1q\sum_{n=1}^q\operatorname{Ram}_r(n)
\overline{\operatorname{Ram}_s(n)}
=1_{r=s}\varphi(r).
\]
Indeed only equal reduced fractions a/r=b/s survive. This is a usable exact Gram construction. A finite, smoothly weighted interval requires a separate endpoint/Poisson estimate; complete-period orthogonality must not silently replace its actual Gram matrix.

## Tool 2: retain the extra coefficient in our divisor truncation

For the actual sharp Q define
\[
D_Q(m)=\sum_{d\mid m,\ d\le Q}\mu(d),\qquad
S_Q(m)=\sum_{d\mid m,\ d\le Q}\mu(d)\log(m/d).
\]
Then the exact mapping is
\[
\boxed{S_Q(m)=\Lambda_Q(m)+\log(m/Q)D_Q(m),\quad
c_Q(m)=\Lambda(m)-\Lambda_Q(m)-\log(m/Q)D_Q(m).}
\]
This holds for real Q, with the stated integer divisor convention, and also at m=1. It does not use an asymptotic approximation. In particular, for a prime m>Q the three terms cancel exactly and c_Q(m)=0. Losing the D_Q term changes even this elementary property.

Thus using Paper I's Lambda_Q requires an augmented coefficient family containing D_Q and the actual smooth factor log(m/Q). Using Paper II's lambda_Q additionally requires a proved comparison with Lambda_Q. The two approximations are different finite arithmetic functions.

One can generate D_Q as the right derivative of Lambda_R with respect to log R, evaluated at R=Q. This is a coefficient identity for the finite sum; it does not license differentiating an asymptotic error term in a published correlation theorem. A parameter-family proof with controlled derivatives, or a direct coefficient calculation, would be needed.

## Tool 3: the exact direction of a Gram certificate

In any genuinely positive weighted Hilbert space let `G_ij=<phi_i,phi_j>` and `b_i=<phi_i,v>`, with the first argument conjugate linear. For every coefficient vector a,
\[
0\le\left\|v-\sum_i a_i\phi_i\right\|^2
=\|v\|^2-2\operatorname{Re}(a^*b)+a^*Ga.
\]
Consequently known Gram and mixed-moment entries give
\[
\|v\|^2\ge b^*G^\dagger b,
\]
where the pseudoinverse is valid because an exact Gram system has b in its range. The unmeasured orthogonal residual has nonnegative energy and no upper bound from this calculation alone.

This construction can certify a lower bound on a positive defect if an already proved identity converts that lower bound into the desired upper variance bound. Such an identity and its weights must be written down first. Applied directly to the variance vector, projection supplies a lower bound and does not by itself establish `liminf Z_T<=1-2M`. The finite calculation is not a general impossibility theorem for other sieve arguments.

## Concrete compatibility tests for the R26 family

These are deductions from the displayed source hypotheses, not claims that the whole sieve route is impossible.

- R26 has `Y>=sqrt(log T)` and `Q=Y^(2/3)`. At the bottom, Q is only `(log T)^(1/3)`, outside the printed power lower bound `R>>N^epsilon` if R is identified with Q.
- At the natural scale Y=X/T, the exponent of Y in X ranges from 3/7 to 5/9. Thus Q has exponent from 2/7 to 10/27. Paper II's unconditional k=3 cutoff requires R below X^(1/4-epsilon), so this direct identification fails throughout the natural-scale window. k=3's shift restriction also fails at and above the central scale X=T^2. A smaller auxiliary R would be a new approximation requiring its own error budget.
- Paper II's Section 10 conditions require R to exceed h log h; identifying h with Y and R with Q=Y^(2/3) fails that requirement. Its GRH input is also stronger than the programme's ordinary RH assumption. These facts preclude a direct invocation of that particular long-interval calculation.
- Even where a one-prime mixed moment applies, expanding c_Q times Lambda(m+h) retains the genuine Lambda(m)Lambda(m+h) term. Evaluating only the other mixed moments does not finish the covariance estimate.

The useful next test is therefore explicit: choose the actual positive observable to which a Gram inequality will be applied, retain the augmented coefficient family above, and compute a source-valid bound including all physical-length errors. Continue only if its inequality has the direction and strength needed for `liminf Z_T<=1-2M`, or if it rigorously controls the previously unmeasured residual. This calls for one bounded symbolic/analytic calculation, not a frequency-grid or prime-height scan.
