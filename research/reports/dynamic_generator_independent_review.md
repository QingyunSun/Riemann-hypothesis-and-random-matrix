# Independent review of the all-time protected-moment theorem

2026-09-05. Reviewed source: `research/reports/dynamic_generator.md`. Reviewer: the flow subagent, independently of the author of that report. This is a mathematical proof audit with separate diagnostic computations, not a formal proof-assistant certification or a novelty assessment.

## 1. Verdict

I found no gap in the stated all-forward-time identity

$$
\mathbb E_{\rm ACUE}|p_m(\Phi_tX)|^2
=\mathbb E_{\rm CUE}|p_m(\Phi_tX)|^2,
\qquad 1\le m\le N,\quad t\ge0,
$$

for the deterministic repulsive flow in radian coordinates

$$
\dot\theta_i=V_i=\sum_{j\ne i}\cot\frac{\theta_i-\theta_j}{2}.
$$

The invariant biweight argument, the discrete Schur Gram formula including the endpoint \(m=N\), global forward existence, and the characteristic-polynomial linearization all check out. None requires interchanging a singular generator with an expectation. In particular, the failure of such an interchange for the force-square observable does not damage the protected-polynomial theorem.

One wording clarification is advisable: “any polynomial with positive and negative weights individually at most \(N\)” means a polynomial in the **symmetric trace algebra**

$$
\mathcal A_{\le N,\le N}
=\operatorname{span}\{p_\lambda\overline{p_\mu}:
|\lambda|\le N,\ |\mu|\le N\}.
$$

It should not be read as a statement about arbitrary polynomials of labeled particles. For example, applying the generator to one labeled coordinate \(z_i\) produces uncancelled denominators; the symmetric pairwise cancellation is essential.

## 2. Independent reconstruction of the generator and its block

Write \(z_i=e^{i\theta_i}\). The identity

$$
\cot\frac{\theta_i-\theta_j}{2}
=i\frac{z_i+z_j}{z_i-z_j}
$$

has the stated sign. Hence

$$
Lp_m=-m\sum_{i<j}
\frac{(z_i^m-z_j^m)(z_i+z_j)}{z_i-z_j}.
$$

For one unordered pair, the numerator quotient equals

$$
z_i^m+z_j^m
+2\sum_{a=1}^{m-1}z_i^{m-a}z_j^a.
$$

After summing over pairs, symmetry under \(a\leftrightarrow m-a\) gives

$$
Lp_m=-m\left[(N-m)p_m+\sum_{a=1}^{m-1}p_a p_{m-a}\right].
$$

Every term has positive weight \(m\). The vector field is real on the angle torus, so \(L\overline f=\overline{Lf}\); the negative-weight formula therefore has the same sign, not the opposite sign. By the Leibniz rule, the linear span of \(p_\lambda\overline{p_\mu}\) of any fixed biweight \((a,b)\) is invariant.

At fixed weight, splitting a part increases the number of factors but never their total index. This is exactly why repeated applications cannot leave the protected sector. The number of derivatives is irrelevant.

Finite-\(N\) algebraic relations do not break the argument. One may use an overcomplete spanning vector and its explicitly specified coefficient matrix: each component still satisfies the finite linear ODE, and uniqueness gives its matrix exponential. Alternatively, quotient by the relations or use the elementary symmetric monomials.

## 3. The Schur determinant, its normalization, and the endpoint

For an unordered \(N\)-subset \(S\) of the \(2N\)-grid, the probability is

$$
(2N)^{-N}|\Delta(z_S)|^2.
$$

There is no extra \(N!\) in this subset formula. The Schur alternant cancels the Vandermonde in the measure. Cauchy–Binet over unordered subsets then yields

$$
\mathbb E_{\rm ACUE}s_\alpha\overline{s_\beta}
=\det[\mathbf1_{a_i\equiv b_j\ ({\rm mod}\ 2N)}]_{i,j=1}^N,
$$

where

$$
a_i=\alpha_i+N-i,\qquad b_j=\beta_j+N-j.
$$

Using empty partitions verifies normalization directly: the lists are \(N-1,\ldots,0\), and the determinant is 1. Thus there is no hidden factorial in the Gram identity.

For \(|\alpha|\le N\), one has

$$
0\le a_i\le \alpha_1+N-1\le2N-1.
$$

The inequalities are inclusive exactly where needed. In particular, the extremal partition \(\alpha=(N)\) gives the largest exponent \(2N-1\), which has not wrapped modulo \(2N\). The endpoint \(m=N\) is valid.

The lists \(a_i,b_j\) are strictly decreasing. Congruence inside the interval \([0,2N-1]\) is equality, so the determinant vanishes unless the lists coincide, and then it is \(+1\). Their order is the same, so there is no undetected permutation sign. Coinciding exponent lists force \(\alpha=\beta\).

Consequently the full Schur Gram agrees with Haar whenever both partition weights are individually at most \(N\), even when the two weights differ. Passing from Schur polynomials to power sums gives the required initial trace Gram. At equal weight \(m\le N\), all partitions of \(m\) have at most \(N\) rows; hence the usual full symmetric-group character orthogonality is applicable and gives the diagonal power-sum Gram \(z_\lambda\).

A random common rotation does not change any balanced observable. For unequal weights in the indicated band, both expectations already vanish by the same Schur argument, so the larger symmetric-algebra statement remains correct after rotation as well.

### Sharpness test just outside the band

For every \(N\ge2\), take \(\alpha=(N+1)\). Its exponent list is

$$
(2N,N-2,N-3,\ldots,0).
$$

The first and last exponents coincide modulo \(2N\), so

$$
\mathbb E_{\rm ACUE}|s_{(N+1)}|^2=0,\qquad
\mathbb E_{\rm CUE}|s_{(N+1)}|^2=1.
$$

Thus the uniform guarantee cannot be extended to all symmetric polynomials of the next weight. This is a pre-existing discrepancy at \(t=0\), not leakage generated from a smaller weight.

The case \(N=1\) is exceptional for this sharpness example: there is only one exponent and no duplicate row, and every balanced one-particle monomial is constant. The main theorem includes \(N=1\) correctly. An initial draft of the independent check incorrectly applied the \(N\ge2\) sharpness example to \(N=1\); its assertion caught the mistake, and the example and script now retain this exception explicitly.

## 4. Global physical flow and the exact finite-time argument

The score of the squared Vandermonde in radians is \(V\), so for

$$
W=\sum_{i<j}\log|e^{i\theta_i}-e^{i\theta_j}|^2
$$

one has \(W'=\sum_iV_i^2\ge0\). Let \(J=\binom N2\). For \(N\ge2\), each summand is at most \(\log4\), and therefore each individual summand is bounded below by

$$
W(0)-(J-1)\log4.
$$

For a fixed initial configuration this gives a strictly positive lower bound on every chordal distance along the whole forward trajectory. It rules out finite-time collision and even asymptotic approach to the collision set. Compactness of the torus and ordinary smooth-ODE continuation give global forward existence. For \(N=1\), the vector field is zero and the assertion is immediate.

No lower gap bound uniform over all CUE initial configurations is being asserted or needed. The bound is configuration dependent. The CUE initial law is collision free almost surely; every ACUE configuration is collision free.

Let \(u_a\) be the positive partition-polynomial vector of weight \(a\). Its pathwise equation is \(u_a'=G_a u_a\), so \(u_a(t)=e^{tG_a}u_a(0)\). For fixed weights \(a,b\), the matrix of products is thus a finite linear combination of the initial products. Equal initial Gram entries imply equal expectations at every fixed \(t\ge0\).

This proof uses neither a Taylor series justified only locally nor differentiation under an expectation. Each protected generator iterate is itself a Laurent polynomial extending continuously over collision configurations, and hence bounded on the compact torus. The singular denominators have cancelled before expectations enter. This is materially different from the rational force energy.

The conclusion remains valid for every choice of a finite time \(t_N\ge0\) depending on \(N\). It does not identify the two full pushforward probability measures.

## 5. Independent check of the characteristic PDE and sign

From the same cotangent identity,

$$
\dot z_i=-z_i\sum_{j\ne i}\frac{z_i+z_j}{z_i-z_j}
=-2z_i^2\sum_{j\ne i}\frac1{z_i-z_j}+(N-1)z_i.
$$

For the monic polynomial \(P(z,t)=\prod_i(z-z_i(t))\),

$$
\frac{P''(z_i)}{P'(z_i)}
=2\sum_{j\ne i}\frac1{z_i-z_j}.
$$

Differentiating \(P(z_i(t),t)=0\) therefore shows

$$
P_t(z_i)=z_i^2P''(z_i)-(N-1)z_iP'(z_i).
$$

The leading \(z^N\) term of the right side cancels. Since \(P_t\) also has degree at most \(N-1\), equality at the \(N\) distinct roots proves

$$
P_t=z^2P_{zz}-(N-1)zP_z.
$$

The coefficient of \(z^{N-k}\) is multiplied by

$$
(N-k)(N-k-1)-(N-1)(N-k)=-k(N-k),
$$

so indeed

$$
e_k(t)=e^{-k(N-k)t}e_k(0).
$$

This also shows \(e_N\) is conserved, as required by \(\sum_iV_i=0\). It has the correct physical two-particle limit: for a gap \(g\), \(g'=2\cot(g/2)\), and therefore \(\cos(g(t)/2)=e^{-t}\cos(g(0)/2)\). The first elementary coefficient decays by \(e^{-t}\) when \(N=2\), in agreement with the PDE.

Changing the flow to attraction changes the exponent signs. The resulting polynomial continuation exists for all real times as a coefficient formula, but its roots may leave the circle after a collision. The draft correctly restricts its physical all-time conclusion to repulsion and nonnegative time.

## 6. Independent computations and their limits

The companion script dynamic_generator_independent_review.py does not import the original audit program or read its computed answers. Its JSON is saved with the script in `research/dynamic-generator/`.

The integer portion checks every residue Gram entry between all partitions of weights \(0,\ldots,N\), for each \(N=1,\ldots,10\). It checks the endpoint exponent lists and the next-weight counterexample separately. All checks passed. At \(N=10\), this includes 139 partitions and 19,321 exact integer Gram entries.

The numerical portion independently evaluates \(Lp_m\) directly from the angle vector field for \(m=1,\ldots,N+2\); evaluates \(Le_k\) by differentiating elementary symmetric polynomials; and integrates the actual angle ODE at \(N=2,3,5,8\) to compare its characteristic coefficients with the exponential formula. It uses times \(0.03,0.1,0.3\). The largest observed errors were:

- direct trace-generator identity: less than \(3.4\times10^{-14}\);
- elementary-coefficient generator identity: less than \(1.6\times10^{-14}\);
- integrated characteristic coefficients: less than \(4.1\times10^{-12}\).

These last checks use floating-point arithmetic and numerical ODE integration; they are diagnostics, not exact computations or proofs. The mathematical arguments above establish the statements independently of those tolerances.

## 7. Required editorial changes and remaining scope

There is no mathematical change required to the central theorem. Clarify the symmetric trace-algebra scope of “any polynomial.” Retain the distinction between the finite-dimensional polynomial continuation and physical negative-time angle evolution. Preserve the finite-\(N\), finite-ensemble nature of the result.

The result disproves the proposed mechanism in which repeated deterministic Coulomb differentiation of a protected trace polynomial generates an observable outside the matched band. It does not establish that a different flow or a singular statistic can be evaluated arithmetically. It is not an AH contradiction or a theorem about zeta-zero distributions.
