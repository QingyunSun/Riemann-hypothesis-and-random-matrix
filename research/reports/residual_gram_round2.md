# Full arithmetic operator: extended spectra, Schur bounds, and prime-bin Fock models

Research round 2, 5 September 2026. This is a reproducible continuation of `research-round1/residual_gram.md`. No half-gap breakthrough or universal impossibility theorem was obtained. The strongest exact statement remains coefficient-space approximator saturation. This round tests the much larger remaining resonator problem.

## 1. Concrete result

For arbitrary resonator coefficients, the saturated half-gap main term is governed by

\[
K_L=A^*A+\tfrac12(A^2+(A^*)^2),
\qquad
A_{p^e m,m}=\frac{2\sin(\tfrac\pi2\log(p^e)/\log L)}{e\sqrt{p^e}}.
\]

The finite experiments set `log L/log T=1`, the limiting boundary of the admissible logarithmic range. The target is

\[
\limsup_{L\to\infty}\lambda_{\max}(K_L)\mathrel{?}\le\frac{\pi^2}{2}
=4.934802200544679\ldots.
\]

The normalized target is `lambda/(2 pi^2)-1/4<=0`. The raw operator is **not** being compared with `1/4`.

The full sparse eigenvalue search was extended to ten million coefficients:

| L | lambda max | normalized margin | eigenvector residual |
|---:|---:|---:|---:|
| 1,000,000 | 4.273896915919377 | -0.03348185285686 | 3.14e-12 |
| 3,000,000 | 4.299660502530880 | -0.03217665431168 | 8.37e-12 |
| 10,000,000 | 4.324089558989538 | -0.03093906385385 | 2.04e-11 |

The last creation matrix has 37,861,249 nonzero entries. `K_L` is applied as a sparse operator, not materialized. The ten-million run took approximately 27 seconds on the available machine, excluding any subsequent serialization. This timing is a recorded run, not a performance guarantee.

The values rise with L and remain negative. They neither prove a limiting upper bound nor justify extrapolating to a particular constant. A fixed finite eigenvector is not itself a valid asymptotic zeta certificate.

## 2. Finite eigenvector structure: the additional features nearly exhaust the tested problem

At `L=10^6`, the true top eigenvalue is `4.273896915919377`. We fitted its normalized Perron vector using vectors

\[
\frac{d_\ell(n)}{\sqrt n}\,v^i F(n),\qquad
v=\frac{\log n}{\log L},\quad 0\le i\le4.
\]

The first feature set is just `F=1`. The next uses `{1,S2,S3,S4}`, with `S_k=sum_{p|n}(log p/log L)^k`. Larger fits add the largest logarithmic prime factor and then the number of distinct prime factors `omega(n)`. Every reported Rayleigh quotient is evaluated again using the full finite sparse arithmetic operator.

| ell | feature set | terms | L2 fit error | Rayleigh deficit from full optimum |
|---:|---|---:|---:|---:|
| 1.08 | mass only | 5 | 0.09399054 | 0.0325942265 |
| 1.08 | symmetric prime powers | 20 | 0.01813753 | 0.0007337046 |
| 1.08 | plus largest prime factor | 30 | 0.01524505 | 0.0006332664 |
| 1.08 | plus omega and omega squared | 40 | 0.01134669 | 0.0004437114 |

The 40-term fit reaches `4.273453204513651`, within about 0.011% of the full tested maximum. The 20-term fit already reaches `4.273163211325686`.

This is evidence that the finite operator's maximizing direction has considerable multiplicative structure and is well approximated by the symmetric prime-factor family tested in round one. It is not evidence that the same finite family is asymptotically complete. The role of `omega(n)` can change with L, and a small finite-L residual does not bound unseen asymptotic directions.

The fits were also made at ell=1 and ell=1.1763; all results, including worse fits, are retained in JSON. Least-squares truncation uses an explicit numerical singular-value threshold, so these fits are not exact interval certificates.

## 3. A scalar Cauchy majorant for the full operator

This section gives a candidate analytic bound with explicit derivation. Its numerical optimization does not reach the desired threshold.

Write `a_q=2 sin((pi/2) log q/log L)/(e sqrt(q))` for `q=p^e`. The divisor identity

\[
\sum_{q\mid n}\Lambda(q)=\log n
\]

and Cauchy–Schwarz give

\[
\|Ax\|^2\le
\sum_{m\le L}|x_m|^2\sum_{q\le L/m}
\frac{a_q^2\log(qm)}{\Lambda(q)}.
\tag{B1}
\]

For the other part, take a positive function Y on `(0,1]`, and set `v_n=log n/log L`. Applying `2ab<=a^2+b^2` to each product gives

\[
\begin{aligned}
\operatorname{Re}\langle x,A^2x\rangle
\le{}&\frac{(\log L)^2}{2}
\sum_m|x_m|^2\sum_{kl\le L/m}
\frac{a_k^2a_l^2}{\Lambda(k)\Lambda(l)}Y(v_{klm})\\
&+\sum_n\frac{|x_n|^2}{2Y(v_n)(\log L)^2}
\sum_{kl\mid n}\Lambda(k)\Lambda(l).
\end{aligned}
\tag{B2}
\]

Terms without prime-power factors are zero. Since the pairs `kl|n` are a subset of pairs of divisors of n,

\[
\sum_{kl\mid n}\Lambda(k)\Lambda(l)\le(\log n)^2.
\]

Let

\[
f(u)=\frac{\sin^2(\pi u/2)}{u^2},\qquad f(0)=\pi^2/4,
\]

and

\[
B(v)=4\int_0^{1-v}(v+u)f(u)\,du.
\]

Replacing the prime sums in (B1)–(B2) by their elementary prime-number asymptotics suggests the explicit bound

\[
\limsup_L\lambda_{\max}(K_L)
\le\sup_{0\le v\le1}\left[
B(v)+\frac{v^2}{2Y(v)}
+8\int_{u+w\le1-v}f(u)f(w)Y(v+u+w)\,du\,dw
\right].
\tag{B3}
\]

For a fixed positive smooth Y bounded away from zero, the passage from the finite inequalities to (B3) can be justified uniformly by partial summation. Contributions of powers `p^e`, `e>=2`, are `O(1/log L)`: use the small-argument bound for sine and convergence of the corresponding prime-power reciprocal sums. One should write those uniform remainder estimates in a final proof rather than cite this numerical note as their formal verification. Profiles vanishing at v=0 can first be regularized by adding a fixed positive epsilon.

This is related to the weighted elementary inequalities in [Inoue–Kobayashi–Toma, arXiv:2510.14309](https://arxiv.org/html/2510.14309v1), but it treats the quadratic operator of the newer resonance-correlation method. Their existing linear-method barrier cannot simply be reused as an upper bound for K.

### Numerical result: this majorant still fails

A constant Y gives a best sampled bound near `5.28075150`, larger than `pi^2/2`. Allowing Y to vary leads to a backward Volterra equation. With

\[
C(s)=8\int_0^s f(u)f(s-u)\,du,
\]

the equality profile at a proposed upper bound lambda satisfies

\[
Y(v)=\frac{v^2}{2\left[\lambda-B(v)-\int_v^1C(t-v)Y(t)\,dt\right]}.
\tag{V}
\]

A discretized backward recursion and bisection gave:

| grid intervals | numerical threshold lambda |
|---:|---:|
| 250 | 5.2073898741 |
| 500 | 5.2073943491 |
| 1,000 | 5.2073954679 |
| 2,000 | 5.2073957475 |
| 4,000 | 5.2073958175 |

The corresponding normalized bound is approximately `+0.01380975`. It cannot prove a half-gap no-go. These are numerical values for the majorant search, not a certified global optimum over Y. The failure is preserved because it identifies a specific loss: separately estimating the norm square and the holomorphic term by Cauchy loses the compatibility of their near-extremizers. More precision in the same grid would not close a gap of this size.

## 4. Prime bins and a finite bosonic creation model

A second approach is to retain more of the prime-factor combinatorics.

Divide logarithmic prime sizes into bins `((j-1)/N,j/N]`, `1<=j<=N`, and set

\[
c_j^2=\int_{(j-1)/N}^{j/N}\frac{4\sin^2(\pi u/2)}u\,du.
\]

Use occupation vectors `k=(k_1,...,k_N)` with the rounded-up energy restriction

\[
\sum_{j=1}^N j k_j\le N.
\]

The finite bosonic matrix is

\[
(A_N)_{k+e_j,k}=c_j\sqrt{k_j+1}
\]

whenever the new state remains in the energy set. Form

\[
K_N=A_N^*A_N+\tfrac12(A_N^2+(A_N^*)^2).
\]

Every mode and every occupation vector retained by this construction is explicit. The rounding restricts the support; it is not an upper discretization of the full continuum norm.

| bins N | state dimension | largest eigenvalue | normalized margin |
|---:|---:|---:|---:|
| 12 | 272 | 3.9285784722 | -0.0509758896 |
| 20 | 2,714 | 4.0882405964 | -0.0428873119 |
| 28 | 18,460 | 4.1870051368 | -0.0378838418 |
| 36 | 99,133 | 4.2539816177 | -0.0344907736 |
| 40 | 215,308 | 4.2800240103 | -0.0331714506 |

At N=40 the creation matrix has 963,320 nonzero entries. Its eigenvector residual is approximately `1.6e-11`. No positive half-gap certificate occurs in these models.

### A proposed fixed-bin arithmetic lower-transfer proof

There is a concrete route from each fixed finite bin model to arithmetic resonators; this is more modest than identifying the entire limiting operator norm.

For every occupation vector, take the normalized vector supported on squarefree integers whose prime factors have those bin counts, with coefficient proportional to the product of their prime weights `a_p`. Rounded-up energy ensures that all such integers are at most L. Different occupation vectors have disjoint supports.

If `E_k` is the elementary symmetric sum of order k in one bin's squared prime weights, the exact raising coefficient between its collective vectors is

\[
(k+1)\sqrt{E_{k+1}/E_k}.
\]

For fixed bin resolution and fixed k, the prime-number theorem gives the total squared weight tending to `c_j^2`; the maximum individual squared weight tends to zero. Consequently

\[
E_k\longrightarrow (c_j^2)^k/k!,
\]

and the raising coefficient tends to `c_j sqrt(k+1)`. This handles repeated occupation of a bin through **distinct primes**. It does not pretend that repeated copies of the same prime are independent bosons.

Let P project onto the retained collective squarefree vectors. The exact inequality

\[
PA^*AP\ge (PAP)^*(PAP)
\]

retains the nonnegative loss from intermediate states outside the subspace. Raising twice cannot leave the rounded-energy set and later return. Squareful states created by a repeated prime or a prime power cannot return to the squarefree subspace by further multiplication. These observations give the expected convergence of the holomorphic compressed term to `A_N^2`. The proposed conclusion is

\[
\liminf_{L\to\infty}\lambda_{\max}(K_L)
\ge\lambda_{\max}(K_N)
\quad\text{for every fixed N}.
\tag{FT}
\]

This argument is a proof draft requiring independent line-by-line review and a complete statement of the finite-bin normalizations. It gives a **lower** search mechanism. It gives no upper bound for the full arithmetic operator and no equality with a limiting Fock norm. A positive rationally certified finite-bin value above `pi^2/2` would be a concrete success criterion, but all values computed here are below that threshold.

## 5. Why the continuum limit is delicate: the small-prime cloud

The divisor-family resonators suggest an infrared phenomenon. Under the `d_ell(n)^2/n` weighting, the number of logarithmically small prime factors grows on the scale `ell^2 log log L`, while their total logarithmic mass remains bounded. Therefore a finite-particle or coarse energy-bin model can converge slowly even when the creation kernel itself is square-integrable. One cannot infer a precise limit from the modest bin table.

A useful candidate representation uses the scaled Poisson–Dirichlet partition of mass v, with parameter `a=ell^2`, as the reference measure. In that representation the creation operator acts by removing a part u with coefficient `2 sin(pi u/2)/ell`, while its adjoint inserts a part with intensity `2 ell sin(pi u/2) du/u`, subject to total mass at most one. The symmetric prime-moment polynomials of round one are a natural Galerkin family in this representation.

This description explains the algebraic insertion formulas and suggests a more stable basis. It is **not** a proved statement that every asymptotic arithmetic resonator belongs to one such representation, that different ell sectors exhaust the full norm, or that finite-bin spectra converge to the desired universal operator. Those are separate operator-limit problems. The original PD arithmetic asymptotic transfer also remains under independent audit.

## 6. Files, dependencies, and commands

Round-two files are in `research-round2/residual-gram/`. They refer to the round-one `arithmetic_operator.py` implementation through a relative path. The source snapshot is not modified.

* `extended_arithmetic.py` and `extended-arithmetic-results.json`: reproduce the 3-million and 10-million full spectra. The wrapper writes only round-two outputs.
* `eigenvector_features.py` and `eigenvector-feature-results.json`: fit the round-one million-dimensional Perron vector and re-evaluate each candidate using the full operator.
* `first_upper_bound.py`, `first-upper-bound-results.json`: constant-weight scalar majorant.
* `volterra_upper_search.py`, `volterra-upper-results.json`, `volterra-upper-profile.npz`: variable-weight majorant search.
* `boson_cutoff.py`, `boson-cutoff-results.json`: all finite prime-bin models listed above.
* `*-run.log`: retained execution records.

Dependencies are Python, NumPy, and SciPy. The runs used the machine's `python3` (Homebrew Python 3.14), not the bundled PDF runtime. The rational certificate in round one additionally requires SymPy. For reproducibility, use the same environment that ran the round-one numerical files; no private service, GPU, or new model invocation is required.

```text
OPENBLAS_NUM_THREADS=1 python3 research-round2/residual-gram/extended_arithmetic.py
OPENBLAS_NUM_THREADS=1 python3 research-round2/residual-gram/eigenvector_features.py
OPENBLAS_NUM_THREADS=1 python3 research-round2/residual-gram/first_upper_bound.py
OPENBLAS_NUM_THREADS=1 python3 research-round2/residual-gram/volterra_upper_search.py
OPENBLAS_NUM_THREADS=1 python3 research-round2/residual-gram/boson_cutoff.py
```

The 10-million eigenvector archive is about 85 MB and is optional research data. It should not be included in a small source-code PR by default. Pass `--save-largest` to the wrapper to regenerate it. The eigenvalue JSON and scripts are sufficient to reproduce the reported values. The fitting script uses the smaller, already archived round-one eigenvector.

## 7. What this round rules out, and what it leaves open

The exact saturation theorem rules out constant main-term recovery by changing only the approximator inside the fixed product space. The sparse-tail lemma rules out a specified separated-tail tactic for divisor-bounded coefficients. Those are genuine statements with explicitly limited scopes.

The new negative finite spectra, the near-optimal finite fits, the negative bosonic bins, and the failed Schur majorant are **not** universal no-go theorems. Together they make a large hidden gain from a routine reparameterization less plausible, but that judgment is a research inference rather than a proof.

A precise next analytic success criterion is an explicit positive comparison profile or an operator identity proving a uniform upper below `pi^2/2`, with every prime-power and cutoff error included. A precise alternative success criterion is a finite prime-bin or other explicit coefficient family with a certified limiting Rayleigh quotient above that value. Merely extending the grid or reporting another negative optimized decimal would not meet either criterion.
