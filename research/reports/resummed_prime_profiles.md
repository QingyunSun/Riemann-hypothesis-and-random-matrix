# Resummed symmetric prime profiles: a stable negative variational experiment

Research round 2, 2026-09-05. This is a bounded continuum experiment suggested by the residual-Gram agent's arithmetic operator. It is not a zeta theorem, a certified interval optimization, or a proof of optimality.

## Outcome

The family below removes the ill-conditioned large symmetric-feature Gram matrix by resumming a multiplicative prime-factor profile. It reproduces the unmodified one-variable benchmark and improves that restricted benchmark, but does not exceed the better polynomial prime-feature result obtained by the other agent. No half-gap crossing occurs in the validated trials.

| Prime profile | Radial degree / quadrature order | Half-gap margin |
|---|---|---:|
| $g=1$, optimized original parameter | 6 / 32 | -0.0153579821816782 |
| $g(u)=\exp(c_2u^2)$ | 7 / 32 | -0.0147198770500968 |
| $g(u)=\exp(c_2u^2+c_3u^3)$ | 9 / 40 | -0.0146705663327385 |
| Three nontrivial coefficients, through $u^4$ | 9 / 40 | -0.0146638642779015 |
| Five coefficients, through $u^6$; local continuation | 9 / 40 | -0.0146638632200778 |

The last two searches are local continuations, not global optimizations; one hit its iteration budget. The radial Gram condition numbers in the high-precision-density runs were between approximately 1.6 and 2.4. Increasing radial degree and quadrature order changes the displayed negative margins only slightly. This offers a stable independent check that these natural prime-factor tilts recover a small fraction of the deficit, not an arithmetic advance past one half.

## The family and its continuum density

Consider the formal asymptotic family

$$
r(n)=d_\ell(n)\prod_{p\mid n}g\left(\frac{\log p}{\log L}\right)
 f\left(\frac{\log n}{\log L}\right),
\qquad
 g(u)=\exp\left(\sum_{k=2}^d c_ku^k\right),
\quad a=\ell^2.
$$

The product is symmetric in the prime factors. In the squarefree leading continuum model, a linear exponent in $g$ is redundant with the radial profile $f$ and is therefore omitted; this is not an exact finite-integer identity for a product over distinct prime divisors. Prime-power conventions require a precise choice in an eventual arithmetic theorem; their effect on the leading continuum formula must be justified, not assumed away.

Under the same Poisson–Dirichlet continuum model used for the prime-feature trial, the squared-coefficient density is proportional to

$$
R(v)=v^{a-1}H(v),
\qquad
H(v)=\mathbb E\exp\left(2\sum_{k=2}^dc_kS_k\right),
$$

where the partition has total mass $v$. This resums all powers of the chosen symmetric statistics, rather than truncating a polynomial in $S_2,S_3,\ldots$.

Write

$$
g(u)^2=\sum_{n\ge0}d_nu^n,
\qquad H(v)=\sum_{n\ge0}H_nv^n.
$$

The coefficient recurrence used in the experiment is

$$
H_0=1,
\qquad
\boxed{
H_n=\frac an\sum_{k=1}^n
k d_k B(k,a+n-k)H_{n-k}.
}
$$

One derivation uses the formal Laplace transform of the convolution exponential with kernel $a(g(u)^2-1)/u$. If $B_n$ are the coefficients of

$$
\exp\left(a\sum_{k\ge1}d_k\Gamma(k)z^k\right),
$$

then $H_n=\Gamma(a)B_n/\Gamma(a+n)$; differentiating the generating series gives the displayed normalized recurrence. This is a formal power-series identity: the factorial-weighted intermediate series need not have a nonzero analytic convergence radius. The final density series is evaluated with an explicit truncation comparison in the experiment.

For example, when $g(u)=e^{cu^2}$, the linear coefficient in $c$ is

$$
H(v)=1+\frac{2c}{a+1}v^2+O(c^2),
$$

in agreement with the Poisson–Dirichlet moment of $S_2$.

## The changed variational form

Use $v$ for the background mass and $u,w$ for inserted prime masses. Relative to the original one-variable form:

- Replace the background measure $v^{a-1}dv$ by $v^{a-1}H(v)dv$ in both numerator and norm.
- Multiply the two distinct-prime insertion integrand by $g(u)g(w)$.
- The same-prime diagonal insertion term has no extra factor $g(u)^2$: its resonator coefficient lives on the background integer, not the newly inserted output prime.
- A linear insertion, away from the exact half-gap boundary, acquires $g(u)$.

The distinction in the third item is essential. Inserting an extra $g(u)^2$ there would change the arithmetic operator and could manufacture a false improvement.

The case $c_2=\cdots=c_d=0$ reduces exactly to the independently reproduced Inoue form, which the code checks to numerical precision. Passing from these coherent continuum formulas to a zeta theorem would still require the weighted-integer asymptotics and error accounting for this new coefficient family.

## Numerical controls and failure record

The initial implementation evaluated the density series entirely in binary64. It reproduced the first two improved trials, but a higher-dimensional optimizer found a parameter vector for which the 32-node validation rejected the density truncation. That run was not accepted as a result.

The revised implementation computes the density coefficients and evaluations with 55 decimal digits, checks 110 versus 140 terms, and also checks the endpoint $v=1$ rather than only quadrature nodes. The final Rayleigh matrices and generalized eigenvalue computations remain floating point. This fixes the identified density-evaluation weakness but does not make the experiment a rigorous interval certificate.

The most accurate recorded five-coefficient local continuation uses

$$
\ell=1.0820458998724858,
$$

$$
\begin{aligned}
c_2&=-0.9407908108421177,\\
c_3&=1.17145568664247,\\
c_4&=-2.268580431289358,\\
c_5&=0.0000165244269937828,\\
c_6&=-0.0000964571420071413.
\end{aligned}
$$

Its tiny newly added coefficients reflect the chosen local continuation and should not be interpreted as proof that those directions are useless.

Files are in `research/prime-profiles/`:

- `euler_profile.py`: basic continuum operator and initial floating implementation;
- `euler_profile.json`: accepted initial trials before the rejected higher-dimensional run;
- `euler_profile_precise.py`: higher-precision density implementation;
- `euler_profile_precise.json`: validated negative trials and full coefficients.

Reproduction:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 euler_profile_precise.py
```

The main research effort should now return to the missing arithmetic mixed information. This experiment provides a stable resummed family and a negative result, not grounds for spending an indefinite budget on additional decimals of the same variational frontier.
