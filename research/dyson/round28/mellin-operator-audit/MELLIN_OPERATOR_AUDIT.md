# Mellin tests for the actual product matrix: an exact necessary condition and a finite-model warning

Date: 2026-09-05. Author: Euclid. Status: bounded ordinary derivation submitted for independent review. The discrete, prime and explicit-formula identities below are unconditional. RH is used only when locating the nontrivial zeros on the critical line or importing the existing heat-energy bound. The finite Gaussian example is a model calculation, not a theorem about primes or zeta zeros.

## 1. Exact unit-vector tests, with the actual odd indices

Retain the R27 central block \(X=T^2,\ Y=\sqrt X,\ \ell=\log T\), the exact packet
\[
F(m,h)=b_T(m)\chi(m/X)V(h/Y)
\left(\frac m{m+h}\right)^T,
\]
and
\[
f_T(m)=X\ell^2\sum_{h\ {\rm even}}F(m,h)[\Lambda(m+h)-2]
\quad(m\ {\rm odd}),
\tag{1}
\]
with \(f_T(m)=0\) for even \(m\). The fixed smooth \(\chi,V\) are supported inside \((1,2)\). Every prime power is retained; the flat center \(2\) is a center on odd endpoints only.

Here the unchanged arithmetic weight is
\[
b_T(m)=\frac{T}{m^T\ell^2}\int_1^m
\omega(\log x/\ell)x^{T-2}\,dx,
\]
with the fixed nonnegative smooth \(\omega\) supported on \([7/4,9/4]\). No asymptotic replacement of this weight is used in the identities.

Let
\[
\mathcal D=\{d:D<d\le2D,\ d\ {\rm odd}\},\qquad
\mathcal K=\{k:K<k\le2K,\ k\ {\rm odd}\},
\]
\[
N_d=|\mathcal D|,\quad N_k=|\mathcal K|,\quad
C_{d,k}=f_T(dk),
\]
where \(D,K\asymp\sqrt X\) and \(DK\asymp X\). Assume the two index sets are nonempty. The original product cutoff remains in \(f_T\). Define the exact multiplicity
\[
r(m)=\#\{(d,k)\in\mathcal D\times\mathcal K:dk=m\}.
\tag{2}
\]

For every real \(t\), use the unit vectors
\[
u_t(d)=d^{it}/\sqrt{N_d},\qquad
v_t(k)=k^{it}/\sqrt{N_k}.
\]
Their bilinear transpose pairing, not their Hermitian pairing, is
\[
u_t^{\mathsf T}Cv_t
=\frac1{\sqrt{N_dN_k}}\sum_m r(m)f_T(m)m^{it}
=:\mathcal M_T(t).
\tag{3}
\]
The operator inequality is still valid because
\(u_t^{\mathsf T}Cv_t=\langle\overline{u_t},Cv_t\rangle\) and
\(\|\overline{u_t}\|_2=\|u_t\|_2=1\). Therefore
\[
\boxed{\|C\|_{\rm op}\ge\sup_{t\in\mathbb R}|\mathcal M_T(t)|.}
\tag{4}
\]
There is no continuum approximation to the odd indices or to \(r(m)\).

As an additional exact check on the all-frequency scope, the finite Dirichlet polynomial satisfies
\[
\lim_{R\to\infty}\frac1{2R}\int_{-R}^R|\mathcal M_T(t)|^2dt
=\frac1{N_dN_k}\sum_m r(m)^2|f_T(m)|^2.
\tag{4a}
\]
The off-diagonal terms vanish since \(\log(m/n)\ne0\) for \(m\ne n\). This supplies another necessary lower bound for the supremum but no numerical lower bound for the actual prime coefficients. A bounded frequency grid cannot certify the all-real supremum in (4).

In particular the proposed R27 uniform bound
\[
\|C\|_{\rm op}^2\ll X(\log X)^{2-\delta},\qquad \delta>0,
\tag{5}
\]
would require
\[
\boxed{
\sup_t\left|\sum_m r(m)f_T(m)m^{it}\right|
\ll X(\log X)^{1-\delta/2}.}
\tag{6}
\]
This is a necessary condition; it is not sufficient for (5). The sampled Mellin vectors are not an orthonormal basis of the actual rectangular matrix. A literal single mode \(f(m)=m^{it_0}\) factors into \(d^{it_0}k^{it_0}\) on an unrestricted rectangle, but the actual product cutoff need not factor, and no single-mode description of \(f_T\) is assumed.

## 2. The test is an exact centered prime Mellin observable

Define a compact smooth function of the real variable \(x\),
\[
a_t(x)=\sum_{m\ {\rm odd}}r(m)m^{it}F(m,x-m).
\tag{7}
\]
The sum is finite; the extension of \(F\) by zero makes \(a_t\) smooth and supported in \((X,3X)\). Set
\[
P_X=\frac{X\ell^2}{\sqrt{N_dN_k}}.
\]
Reindexing the finite sum by \(n=m+h\) gives
\[
\boxed{\mathcal M_T(t)
=P_X\sum_{n\ {\rm odd}}a_t(n)[\Lambda(n)-2].}
\tag{8}
\]
Thus the matrix test already involves an actual prime observable, not a generic coefficient sequence.

Let \(E(x)=\Psi(x)-x\), with \(\Psi\) including all prime powers, and define the exact corrections
\[
L_t=\int a_t(x)dx-2\sum_{n\ {\rm odd}}a_t(n),\qquad
P_{2,t}=(\log2)\sum_{j\ge1}a_t(2^j).
\tag{9}
\]
Only finitely many powers of \(2\) contribute. Stieltjes integration by parts gives the unconditional identity
\[
\boxed{
\mathcal M_T(t)
=P_X\left[-\int E(x)a_t'(x)dx+L_t-P_{2,t}\right].}
\tag{10}
\]
All endpoint terms vanish because \(a_t\) is compactly supported away from \(0,1\) and infinity. The continuous prime-density term has not been dropped: it is exactly included in \(L_t\). The powers of \(2\) have not been mistaken for a negligible parity convention.

These corrections can also be bounded uniformly in all real \(t\). Since \(|m^{it}|=1\), the packet derivative bounds imply, for each fixed \(j\ge0\),
\[
\|a_t^{(j)}\|_{L^1}\ll_j Y^{1-j}/\ell^2.
\tag{11}
\]
Indeed \(\sum_mr(m)=N_dN_k\ll X\), and each \(h\)-profile has amplitude
\(O((X\ell^2)^{-1})\), length \(O(Y)\), and derivative scale \(Y\).
Poisson summation on the odd lattice yields
\[
L_t=-\sum_{\nu\ne0}(-1)^\nu\widehat a_t(\nu/2),
\quad \widehat a_t(\xi)=\int a_t(x)e^{-2\pi i\xi x}dx,
\]
\[
|L_t|\ll_j Y^{1-j}/\ell^2\quad(j\ge2).
\tag{12}
\]
Also \(r(m)\le\tau(m)\ll_\eta X^\eta\). At any fixed \(x\), only \(O(Y)\) values of \(m\) enter (7), so
\[
|P_{2,t}|\ll_\eta X^\eta Y/(X\ell^2).
\tag{13}
\]
There are \(O(1)\) powers of \(2\) in \((X,3X)\). Since \(P_X\asymp\sqrt X\,\ell^2\), the normalized corrections in (10), at \(Y=\sqrt X\), obey
\[
P_XL_t=O(X^{-1/2})\quad(j=3),\qquad
P_XP_{2,t}=O_\eta(X^\eta).
\tag{14}
\]
The second bound is intentionally crude but is smaller than the proposed scale
\(\sqrt X(\log X)^{1-\delta/2}\), for every fixed \(\delta\) and any fixed \(0<\eta<1/2\). Nothing here asserts that the corrections vanish absolutely for all \(t\).

## 3. Link to the actual R21 carrier and to the zero explicit formula

The R21 carrier was
\[
\mathscr E(v)=e^{-v/2}E(e^v),\qquad
g_T(v)=\sqrt{\omega(v/\ell)}\,\mathscr E(v).
\]
Changing variables in (10) gives exactly
\[
\int E(x)a_t'(x)dx
=\int \mathscr E(v)\,q_t(v)dv,\qquad
q_t(v)=e^{3v/2}a_t'(e^v).
\tag{15}
\]
For the actual central weight, \(\omega\) is strictly positive on a fixed neighborhood of \(2\); the support of \(q_t\) lies in
\(v/\ell=2+O(1/\ell)\). Hence for sufficiently large \(T\), (15) is exactly
\[
\int g_T(v)\,K_t(v)dv,\qquad
K_t(v)=q_t(v)/\sqrt{\omega(v/\ell)}
\tag{16}
\]
on that support, and \(K_t=0\) elsewhere. This is a compact test with no division at a zero of the cutoff. If a different weight lacks that local positivity, (15) remains valid without (16).

The known heat identity controls a weighted \(L^2\) norm of the Fourier transform of \(g_T\). It does not, on its own, control the supremum of the pairings (16) against this arithmetic family \(K_t\). Any use of Cauchy must retain the corresponding dual multiplier norm of \(K_t\), which contains the genuine product multiplicity \(r(m)\). Replacing \(r(m)\) by a smooth density requires an additional estimate at the scale of (6).

For an explicit zero representation, put
\[
\widetilde a_t(s)=\int_0^\infty a_t(x)x^{s-1}dx.
\]
The ordinary smooth explicit formula gives
\[
\sum_{n\ge1}\Lambda(n)a_t(n)
=\widetilde a_t(1)
-\sum_\rho\widetilde a_t(\rho)
-\sum_{j\ge1}\widetilde a_t(-2j),
\tag{17}
\]
where nontrivial zeros are counted with multiplicity. Both sums converge absolutely for this compact smooth test. One direct proof starts with Mellin inversion on \(\Re s=c>1\) and
\(-\zeta'/\zeta(s)=\sum\Lambda(n)n^{-s}\), where it is absolutely convergent. Shifting the contour gives the residue \(+\widetilde a_t(1)\) at the zeta pole and negative residues at its nontrivial and trivial zeros. Smooth Mellin decay permits horizontal limits through heights avoiding zeros. On left lines at negative odd integers, the functional equation gives a logarithmic bound for the log derivative; the support \(x>X>1\) makes their integrals tend to zero. There is no pole at \(s=0\) in this integrand and no endpoint term at \(x=1\).

Combining (8), (9) and (17) gives the exact identity
\[
\boxed{
\mathcal M_T(t)
=P_X\left[L_t-P_{2,t}
-\sum_\rho\widetilde a_t(\rho)
-\sum_{j\ge1}\widetilde a_t(-2j)\right].}
\tag{18}
\]
Thus the pole at \(1\) cancels against the continuous part of the original center through \(L_t\), rather than being silently omitted. The trivial-zero contribution is tiny:
\[
P_X\sum_{j\ge1}|\widetilde a_t(-2j)|
\ll YX^{-5/2}=X^{-2}.
\tag{19}
\]
This follows from \(\|a_t\|_1\ll Y/\ell^2\) and its support in \((X,3X)\).

The zero test has the exact formula
\[
\widetilde a_t(s)=
Y\sum_{m\ {\rm odd}}r(m)b_T(m)\chi(m/X)m^{s-1+it}
\int V(z)(1+Yz/m)^{s-1-T}dz.
\tag{20}
\]
Under RH, \(s=\rho=1/2+i\gamma\) in the nontrivial-zero sum. The factor \(m^{i(t+\gamma)}\) is visible in (20), but no localization to \(t\approx-\gamma\) follows without controlling the actual sampled, multiplicity-weighted Mellin sum. We do not replace it by a continuous integral or discard aliases from the integer product set. The smoothing in the \(x\)-variable, used in (11), remains valid uniformly in \(t\).

Equations (14), (18), (19) show that (5) would in particular require
\[
\boxed{
\sup_{t\in\mathbb R}
\left|\sum_\rho\widetilde a_t(\rho)\right|
\ll(\log X)^{-1-\delta/2}.}
\tag{21}
\]
This is a necessary actual-zero/prime estimate, up to the explicitly smaller correction bounds above. It is not established by RH or by the existing weighted heat-energy bound. The identities explain the extra input rather than assume it.

## 4. A finite real Gaussian Hankel model makes the extra logarithm precise

This section is an explicitly separate finite model. It is not a lower bound for the actual prime matrix.

Let \(N\ge3\) be odd. Let \(\xi_0,\ldots,\xi_{N-1}\) be independent real Gaussian variables with variance \(\sigma^2\), and define the cyclic Hankel matrix
\[
H_{jk}=\xi_{j+k\ {\rm mod}\ N},\qquad 0\le j,k<N.
\tag{22}
\]
Reflection of one index turns \(H\) into a circulant matrix, so its squared singular values are
\[
\left|\sum_{s=0}^{N-1}\xi_s e^{2\pi i rs/N}\right|^2.
\]
The unitary Fourier transform of the real Gaussian vector has one real Gaussian coordinate of variance \(\sigma^2\), and
\(n=(N-1)/2\) independent circular complex coordinates of mean square \(\sigma^2\), together with their conjugates. Consequently the exact distribution is
\[
\boxed{
\Pr\{\|H\|_{\rm op}^2\le N\sigma^2 z\}
=\operatorname{erf}(\sqrt{z/2})\,(1-e^{-z})^n,\quad z\ge0.}
\tag{23}
\]
If \(\mathsf H_n=\sum_{j=1}^n1/j\), then
\[
N\sigma^2\mathsf H_n
\le\mathbb E\|H\|_{\rm op}^2
\le N\sigma^2(\mathsf H_n+1).
\tag{24}
\]
The lower bound uses the maximum of \(n\) exponential variables; the upper bound adds the mean \(1\) of the remaining normalized real square.

Take \(X=N^2,\ Y=N,\ \sigma^2=Y\log X\). Then
\[
\|H\|_{\rm op}^2\sim \frac12X(\log X)^2
\quad\hbox{in probability},
\tag{25}
\]
and the same leading asymptotic holds for its expectation. Indeed the maximum of \(n\) independent exponentials divided by \(\log n\) tends to \(1\), while the single real square divided by \(\log n\) tends to \(0\). Thus for every fixed \(C,\delta>0\),
\[
\Pr\{\|H\|_{\rm op}^2\le C X(\log X)^{2-\delta}\}\longrightarrow0.
\tag{26}
\]
This verifies the proposed maximum-frequency extra logarithm in this precise finite analogue.

At the same time, every fixed matching Fourier bilinear contraction has mean square \(N\sigma^2=X\log X\). More generally, for any deterministic unit vectors \(u,v\),
\[
\mathbb E|u^*Hv|^2
=\sigma^2\sum_s\left|\sum_{j+k\equiv s}\overline{u_j}v_k\right|^2
\le N\sigma^2,
\tag{27}
\]
by the discrete convolution inequality and \(\|u\|_1\le\sqrt N\).
Therefore the fixed normalized contraction
\(u^*Hv/(\sqrt X\log X)\) tends to zero in \(L^2\), even though the corresponding uniform operator norm does not tend to zero. Fixed vectors must be chosen independently of the Gaussian sample in this assertion.

The cyclic wrap, equally spaced logarithmic cells and independent Gaussian cell values are additional model assumptions. The actual matrix has odd integer indices, a nonfactorable product cutoff, divisor multiplicities, and arithmetic correlations. No comparison theorem between it and (22) has been proved. In particular (26) does **not** refute (5) for actual primes. It shows why proving a uniform matrix estimate can demand a maximum-frequency saving absent from a fixed Möbius/log contraction.

## 5. Adversarial conclusion and source scope

The strongest unconditional statement about the actual matrix in this note is the exact lower test (4), with the prime/carrier/zero identities (10), (15) and (18). They retain all odd-index counts, product cutoffs, prime powers, pole centering and finite endpoints. A claim of the uniform norm saving (5) must therefore provide, at minimum, the uniform arithmetic Mellin control in (6) or (21). The existing heat-energy estimate alone supplies no such control.

The finite model rigorously supports the concern that an extra logarithm may invalidate an unnecessarily uniform target while leaving a fixed arithmetic-vector contraction small. It supplies no actual-prime counterexample. The R27 vector-specific target remains weaker than the uniform operator target, and the original strict global variance inequality remains open.

Dependencies are the frozen R27 matrix definitions and the R21 actual-carrier/heat identity. The smoothed explicit formula in Section 3 is derived from Mellin inversion and the standard meromorphic zeta log derivative on its initial absolutely convergent line; no critical-line Dirichlet series is expanded. No RH-to-GRH substitution, generic GUE transfer, or stochastic assumption about actual prime coefficients is made.

The elementary analytic ingredients used in that contour proof are recorded directly by NIST: the Dirichlet-series domain and meromorphic continuation in [DLMF §25.2](https://dlmf.nist.gov/25.2), the functional equation in [DLMF 25.4.2](https://dlmf.nist.gov/25.4.E2), and the nonzero value \(\zeta(0)=-1/2\) in [DLMF 25.6.1](https://dlmf.nist.gov/25.6.E1). These references support the standard ingredients, not a new arithmetic estimate. Retained source bytes and the exact dependency versions are pinned in the adjacent source manifest.

The small checker verifies finite index normalization, exact Gram/Fourier facts and the algebraic scale comparison. It does not sample zeta zeros, generate large prime-height data, or estimate the actual matrix norm.
