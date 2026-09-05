# Deterministic circular Coulomb dynamics does not leak protected trace moments

**Date:** 2026-09-05. **Status:** self-contained finite-dimensional proof, supported by exact symbolic and cyclotomic checks. This is a rigorous obstruction to the proposed low-mode mechanism, not a theorem about zeta zeros and not a novelty claim.

## 1. Result and the failed proposal

The user appendix proposes that applying successive deterministic circular Coulomb derivatives to a low trace mode might increase its effective degree until ACUE lattice aliasing becomes visible. The first displayed generator ansatz in that appendix is correct. Its next inference, that weighted degree grows from \(m\) to \(2m,3m,\ldots\), is false.

For the radian convention
\[
V_k(\theta)=\sum_{j\ne k}\cot\frac{\theta_k-\theta_j}{2},
\qquad L=\sum_k V_k\partial_{\theta_k},
\qquad p_m=\sum_k e^{im\theta_k},
\]
one has
\[
\boxed{Lp_m=-m\left((N-m)p_m+\sum_{a=1}^{m-1}p_a p_{m-a}\right).}
\tag{1}
\]
The total **positive Fourier weight** of every term is exactly \(m\). Since \(L\) is a real derivation, it preserves the negative weight separately as well.

Consequently, for every \(N\), every \(1\le m\le N\), and every integer \(r\ge0\),
\[
\boxed{
\mathbb E_{\rm ACUE}L^r|p_m|^2
=\mathbb E_{\rm CUE}L^r|p_m|^2.}
\tag{2}
\]
The stronger finite-time statement is also true for the forward repulsive flow \(\Phi_t\):
\[
\boxed{
\mathbb E_{\rm ACUE}|p_m(\Phi_tX)|^2
=\mathbb E_{\rm CUE}|p_m(\Phi_tX)|^2
\quad(t\ge0,\;m\le N).}
\tag{3}
\]
Thus the proposed first distinguishing derivative \(r_*(N)\) does not exist for these protected observables; writing \(r_*=\infty\) is appropriate. No choice \(t_N\to0\), including \(t_N\asymp N^{-2}\), produces the claimed discrepancy.

This conclusion is specific about the observable algebra. It does not say the two evolved measures agree, and it does not rule out rational observables involving inverse gaps. The independently audited force energy is a concrete example outside this algebra.

## 2. Definitions and normalization

We use eigenangles in radians throughout. The appendix alternates between angles in \(\mathbb R/\mathbb Z\), cotangent with argument \(\pi(\theta_i-\theta_j)\), and traces \(e^{im\theta}\). Those conventions need a corresponding conversion in both Fourier modes and the time parameter. The conclusion about invariant degree survives any fixed nonzero time rescaling.

There is also a factor-of-two correction:
\[
\partial_{\theta_k}\log\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^2
=\sum_{j\ne k}\cot\frac{\theta_k-\theta_j}{2}=V_k.
\tag{4}
\]
It equals \(V_k\), not \(2V_k\), in this radian convention.

Let \(K=2N\), \(\zeta=e^{2\pi i/K}\), and let \(S\) be an unordered \(N\)-element subset of \(\{0,\ldots,K-1\}\). The unrotated ACUE probability is
\[
\mathbb P_{\rm A}(S)
=K^{-N}\prod_{\substack{a,b\in S\\a<b}}|\zeta^a-\zeta^b|^2.
\tag{5}
\]
One may apply a common uniform rotation to recover the rotation-invariant ACUE model. All observables audited here are balanced and unchanged by a common rotation, so the unrotated subset model suffices. Equation (5) is for unordered subsets; an ordered tuple formula contains an additional \(1/N!\).

The relevant primary reference is [Tao, “The alternative hypothesis for unitary matrices,” 8 May 2019](https://terrytao.wordpress.com/2019/05/08/the-alternative-hypothesis-for-unitary-matrices/). It defines ACUE using the discrete Vandermonde weight and establishes matching low trace moments. The proof below independently derives exactly the finite collection of moment identities needed here.

## 3. Derivation of the generator

Set \(z_k=e^{i\theta_k}\). For distinct points,
\[
\cot\frac{\theta_k-\theta_j}{2}
=i\,\frac{z_k+z_j}{z_k-z_j}.
\]
Therefore
\[
Lp_m=-m\sum_{k<j}
\frac{(z_k^m-z_j^m)(z_k+z_j)}{z_k-z_j}.
\tag{6}
\]
The denominator cancels:
\[
\frac{x^m-y^m}{x-y}
=\sum_{a=0}^{m-1}x^{m-1-a}y^a.
\]
Collecting terms in (6) yields
\[
\sum_{k<j}\frac{(z_k^m-z_j^m)(z_k+z_j)}{z_k-z_j}
=(N-m)p_m+\sum_{a=1}^{m-1}p_a p_{m-a}.
\]
This proves (1). It holds for all positive \(m\), including \(m>N\); finite-\(N\) polynomial relations may then make a partition basis redundant, but do not invalidate the identity.

Taking complex conjugates gives
\[
Lp_{-m}
=-m\left((N-m)p_{-m}
+\sum_{a=1}^{m-1}p_{-a}p_{-(m-a)}\right).
\tag{7}
\]
There is no additional sign on the right of (7).

For partitions \(\lambda,\mu\), write
\[
p_\lambda\overline{p_\mu}
=\prod_i p_{\lambda_i}\prod_jp_{-\mu_j}.
\]
By the Leibniz rule and (1), (7), every term of its image under \(L\) has the same pair of weights
\[
(|\lambda|,|\mu|).
\tag{8}
\]
The number of factors can increase when a part splits; the sum of their indices cannot. For fixed positive weight \(m\), at most \(m\) factors can occur. In particular \(m=1\) never splits.

The weighted-degree conservation is the exact location where the appendix's proposed mechanism fails. Products of lower modes do not create higher total Fourier weight. No later iteration can reach \(2N\)-aliasing starting inside the protected band.

## 4. Explicit low-weight blocks

The positive-weight blocks are:
\[
Lp_1=-(N-1)p_1;
\]
\[
\begin{aligned}
Lp_2&=-2(N-2)p_2-2p_1^2,\\
L(p_1^2)&=-2(N-1)p_1^2;
\end{aligned}
\]
and
\[
\begin{aligned}
Lp_3&=-3(N-3)p_3-6p_1p_2,\\
L(p_1p_2)&=-(3N-5)p_1p_2-2p_1^3,\\
L(p_1^3)&=-3(N-1)p_1^3.
\end{aligned}
\tag{9}
\]
If \(G_m\) denotes the matrix on the positive partition block, the balanced block generator is the corresponding tensor sum
\[
T_m=G_m\otimes I+I\otimes G_m.
\tag{10}
\]
Its size is at most \(p(m)^2\), independent of derivative order. For \(m=1,2,3\) those sizes are \(1,4,9\).

For example, for both ensembles and \(N\ge2\),
\[
\mathbb E|p_1(\Phi_tX)|^2=e^{-2(N-1)t},
\tag{11}
\]
and
\[
\mathbb E|p_2(\Phi_tX)|^2
=2e^{-4(N-2)t}\left[1+(1-e^{-2t})^2\right].
\tag{12}
\]
Equation (12) follows from
\[
p_2(t)=e^{-2(N-2)t}
\left[p_2(0)-(1-e^{-2t})p_1(0)^2\right].
\]
The two initial terms are orthogonal and each has squared norm \(2\) in the protected moment range.

These expectations generally change with time. Deterministic Coulomb relaxation is not stationary Dyson Brownian motion; CUE stationarity must not be invoked for this deterministic flow.

## 5. Exact Haar and cyclotomic moment proof

Let \(s_\alpha\) denote a Schur polynomial, with \(\alpha\) padded to length \(N\). For Haar measure,
\[
\mathbb E_{\rm CUE}s_\alpha\overline{s_\beta}=\delta_{\alpha\beta}
\quad(\ell(\alpha),\ell(\beta)\le N).
\tag{13}
\]
For the discrete law (5), the alternant formula and Cauchy–Binet give the exact expression
\[
\boxed{
\mathbb E_{\rm ACUE}s_\alpha\overline{s_\beta}
=\det\left[
\mathbf1_{\alpha_i+N-i\equiv\beta_j+N-j\pmod{2N}}
\right]_{i,j=1}^N.}
\tag{14}
\]
Here \(i,j\) are one-based. If a partition has more than \(N\) parts, the corresponding Schur polynomial is zero.

For completeness, multiplying the two Schur alternant ratios by the squared Vandermonde weight cancels both denominators. Summing over unordered \(N\)-subsets is exactly Cauchy–Binet for the two rectangular alternant matrices. The resulting matrix entries are
\[
\frac1{2N}\sum_{a=0}^{2N-1}
\zeta^{a(\alpha_i+N-i-\beta_j-N+j)},
\]
which equal the residue indicators in (14). Taking both partitions empty also verifies normalization of (5).

If \(|\alpha|,|\beta|\le N\), every alternant exponent lies in
\[
0\le\alpha_i+N-i\le2N-1.
\]
Consequently congruence in (14) is actual equality. Each exponent list is strictly decreasing, so the determinant is \(1\) when \(\alpha=\beta\) and \(0\) otherwise. This recovers (13) in the whole required band.

Expanding power sums using symmetric-group characters,
\[
p_\lambda=\sum_{\alpha\vdash m}\chi^\alpha(\lambda)s_\alpha,
\tag{15}
\]
proves equality of every Gram entry
\[
\mathbb E_{\rm ACUE}p_\lambda\overline{p_\mu}
=\mathbb E_{\rm CUE}p_\lambda\overline{p_\mu}
\quad(|\lambda|=|\mu|=m\le N).
\tag{16}
\]
Equivalently the common Gram is diagonal, with entries
\[
z_\lambda=\prod_{j\ge1}j^{a_j}a_j!,
\]
where \(a_j\) is the number of parts equal to \(j\).

Combining (8) and (16) proves the all-orders equality (2). This proof does not rely on observing numerical agreement up to \(r=8\).

## 6. Full forward-time equality and an independent linearization

The repulsive flow exists for all \(t\ge0\) from every collision-free initial configuration. Indeed set
\[
W(\theta)=\log\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^2.
\]
By (4),
\[
\frac{dW}{dt}=\sum_kV_k^2\ge0.
\tag{17}
\]
Every pairwise factor is at most \(4\). Hence \(W(t)\ge W(0)>-\infty\) prevents any factor from approaching zero. The trajectory stays in a compact collision-free subset of the torus, where the vector field is smooth, proving global forward existence. ACUE configurations are distinct by construction, and CUE configurations are distinct almost surely.

For the vector of positive partition polynomials, \(u_m'(t)=G_m u_m(t)\), so
\[
u_m(t)=e^{tG_m}u_m(0).
\tag{18}
\]
Its balanced moment matrix evolves by applying \(e^{tG_m}\) on the two sides. Equal initial moment matrices therefore remain equal for every forward time. This proves (3). The same argument handles any symmetric trace polynomial with positive and negative weights individually at most \(N\).

There is also a useful direct linearization. Define the monic characteristic polynomial
\[
P(z,t)=\prod_{k=1}^N(z-z_k(t))
=\sum_{k=0}^N(-1)^k e_k(t)z^{N-k}.
\]
The root ODE gives
\[
\boxed{\partial_tP=z^2\partial_z^2P-(N-1)z\partial_zP.}
\tag{19}
\]
To verify this, at each root use
\[
\frac{P''(z_k)}{P'(z_k)}
=2\sum_{j\ne k}\frac1{z_k-z_j}
\]
and differentiate \(P(z_k(t),t)=0\). The degree-\(N\) coefficient on the right of (19) cancels, so equality at the \(N\) distinct roots proves the polynomial identity.

It follows coefficient by coefficient that
\[
\boxed{e_k(t)=e^{-k(N-k)t}e_k(0).}
\tag{20}
\]
Thus the elementary symmetric functions provide an independently checkable diagonal form. This is a finite characteristic-polynomial calculation; no claim is made that such a linearization is new in the literature.

**Time-direction limit.** Statements (3), (17), and global physical flow refer to repulsion and \(t\ge0\). Reversing the sign produces the attractive flow and possible collisions. The algebraic finite-dimensional exponential remains meaningful, but one must not identify its negative-time continuation with a physical real-angle flow after a collision, nor assume a common negative collision-free interval for a CUE ensemble. This audit does not prove an attractive-flow Newman-depth law.

## 7. Exact audit requested by the user

The program evaluates \(N=2,\ldots,10\), \(m=1,2,3\), and \(r=0,\ldots,8\): **243 exact moment values per ensemble**.

The exact algebraic work includes:

- Generator coefficients as integer polynomials in \(N\), for every \(m,r\).
- An assertion that every generated monomial retains biweight \((m,m)\).
- Direct rational-function verification of (1) for \(N=2,3,4\) and \(m=1,2,3\).
- Direct rational-function verification of \(Le_k=-k(N-k)e_k\) for \(N=2,3,4\) and all \(1\le k\le N\).
- Haar Schur Gram matrices and integer residue determinants (14), followed by exact character transforms.
- Direct, independent subset enumeration in the integer quotient ring \(\mathbb Z[z]/(\Phi_{2N}(z))\) for \(N=2,3,4,5\). This verifies normalization and every relevant power-sum Gram entry without using the residue determinant to compute the enumerated answer.

**234 protected cases agree exactly.** The remaining nine cases all have \(N=2,m=3>N\); this observable already distinguishes ACUE from CUE at \(r=0\). Their differences are:

| \(r\) | CUE expectation | ACUE expectation | ACUE minus CUE |
|---:|---:|---:|---:|
| 0 | 2 | 1 | −1 |
| 1 | 0 | 6 | 6 |
| 2 | 24 | −12 | −36 |
| 3 | −384 | −168 | 216 |
| 4 | 3552 | 2256 | −1296 |
| 5 | −26880 | −19104 | 7776 |
| 6 | 184704 | 138048 | −46656 |
| 7 | −1204224 | −924288 | 279936 |
| 8 | 7613952 | 5934336 | −1679616 |

The difference is \(-(-6)^r\), consistent with the exact evolved difference \(-e^{-6t}\). This is an existing out-of-band discrepancy, not dynamically created access to protected information.

For example, for \(N=2,m=3\), the Schur partition \((3)\) has alternant exponents \((4,0)\), which coincide modulo \(4\), so its ACUE squared norm vanishes. The partition \((2,1)\) has exponents \((3,1)\) and squared norm \(1\). Haar gives norm \(1\) to each. Since \(p_3=s_{(3)}-s_{(2,1)}\) in two variables, the initial values are \(1\) and \(2\).

As a further **floating, non-exact** independent check, the program directly enumerates all subsets for every \(N\le10\); the largest case has \(\binom{20}{10}=184756\) subsets. Across all these runs:

- maximum absolute Gram error: \(2.3981\times10^{-14}\);
- maximum derivative error divided by the documented absolute coefficient scale: \(2.8866\times10^{-15}\);
- maximum normalization error: \(1.7764\times10^{-15}\).

The exact conclusions depend on the integer computations and proofs, not on those floating error tolerances.

## 8. Files, reproduction, and evidence boundaries

All paths in this section are relative to the directory containing this report:

- **../dynamic-generator/generator_audit.py** — self-contained exact and floating audit.
- **../dynamic-generator/generator_audit_results.json** — full symbolic coefficients, all 243 exact comparison rows, Gram matrices, enumeration checks, runtime and dependency versions.

Reproduce from any directory:

    OPENBLAS_NUM_THREADS=1 python3 research/dynamic-generator/generator_audit.py

The observed environment was Python 3.14.3, NumPy 2.4.4, SymPy 1.14.0. No external inputs or sampling seeds are needed. The completed run took about one second on the available machine; this is an execution observation, not a general performance claim.

The source appendix was read from:

    research/incoming/dynamic_generator_proposal.md

No original source notes or repository files were modified by this audit.

## 9. Correct replacement and what to postpone

The repaired research question is not whether this generator can escape its invariant polynomial algebra. It cannot. A useful new observable must lie outside that algebra, or a genuinely different evolution must fail to preserve it.

Inverse-gap force energies are a concrete candidate. In the same radian convention the independently derived identities are
\[
\mathbb E_{\rm CUE}\sum_kV_k^2=\frac{N(N^2-1)}3,\qquad
\mathbb E_{\rm ACUE}\sum_kV_k^2=\frac{N(N^2-1)}6.
\tag{21}
\]
The force-energy audit is being independently written by the flow agent. Equation (21) separates the ensembles by a factor of two, with the same \(N^3\) total-energy scaling. It is a static rational statistic of initial velocity, not leakage into a protected trace polynomial. Its number-theoretic accessibility remains a separate question.

Accordingly:

1. Stop searching higher derivative orders for this fixed deterministic flow acting on protected trace polynomials; the invariant-algebra theorem already answers all orders.
2. Preserve the appendix's failed degree-growth and low-mode instability conjectures in the record, together with the exact point of failure.
3. Study singular observables only with their integrability and required zero-correlation information made explicit.
4. Postpone a zeta-side lift until an actual arithmetic formula for the chosen inverse-gap observable is available.
5. Do not infer an AH contradiction, RH progress, or a Montgomery–Dyson theorem from either the present obstruction or the finite-ensemble force discrepancy.

The useful structural conclusion is stronger than a failed finite search: **deterministic circular Coulomb evolution preserves the complete ACUE/CUE protected moment sector at every forward time.**
