# Central follow-up: the complete periodic Ramanujan principal is negligible

Date: 2026-09-08. Author: stationary-challenge agent. Status: ordinary mathematical derivation submitted for independent root review. This closes one proposed central-main shortcut; it does not prove a saving in the actual remaining prime-error correlation.

## 1. Definite outcome

The exact periodic progression/Ramanujan model contributes only \(O(1/\log T)\) to the central stationary pairing, even with the noncompact Mellin projection, both output aliases, and every input harmonic retained. Thus a putative nonzero limiting main obtained just by multiplying the Möbius and Ramanujan coefficients is incorrect at this normalization.

The model can be separated from the actual prime sequence by an exact identity. The resulting discrepancy is finite in the prime variable and retains the projected, d-dependent weights. Replacing that discrepancy by zero would require a new correlated arithmetic estimate. Neither ordinary PNT nor the formal principal-coefficient calculation supplies it.

## 2. Exact central object and notation

Use the corrected R29 definitions, with

\[
X=T^2,\quad Y=T,\quad \ell=\log T,\quad D,K\asymp T,
\]

and the sharp odd intervals \(D<d\le2D\), \(K<k\le2K\). Put

\[
A(x)=X\ell^2b_T(x)\chi(x/X),\quad
k(x,n)=V((n-x)/Y)(x/n)^T,
\]

\[
a(n)=(\Lambda(n)-2)\mathbf1_{n\text{ odd}},\qquad
f(x)=A(x)\sum_{n\ge1}a(n)k(x,n).
\tag{1}
\]

The support is compact in \(X<x<2X\), \(Y<n-x<2Y\). All prime powers at odd endpoints and the odd center 2 remain. For a measurable \(J\subset[\pi K,2\pi K]\), let \(P_J\) denote the exact Mellin-frequency projection, equivalently the Fourier projection of \(v\mapsto f(e^v)\):

\[
(P_Jf)(m)=\frac1{2\pi}\int_J\widehat f(t)m^{it}\,dt.
\]

Define \(Z_J\) by the exact R29 normalized integral over J. The earlier sharp stationary calculation gives

\[
Z_J=\mathcal C_J[f]+O(T^{-1/2}),
\tag{2}
\]

\[
\mathcal C_J[f]=\frac1{X\ell^2}
\sum_{d\text{ in the sharp odd interval}}\frac{\mu(d)}d
\int_{dK}^{2dK}\log(m/d)(P_Jf)(m)
\left[-e^{-\pi i m/d}+e^{-2\pi i m/d}\right]dm.
\tag{3}
\]

The endpoint corrections and omitted Poisson tail have already been bounded after integration in (2); they are not removed a second time here. No assertion about frequencies outside this band is inferred from (2).

## 3. An exact d-dependent periodic principal

For each odd d set \(q=2d\), and define, for every integer n,

\[
p_d(n)=\frac q{\varphi(q)}\mathbf1_{(n,q)=1}
-2\mathbf1_{n\text{ odd}},
\]

\[
e_d(n)=\Lambda(n)\mathbf1_{n\text{ odd}}
-\frac q{\varphi(q)}\mathbf1_{(n,q)=1}.
\tag{4}
\]

Then \(a(n)=p_d(n)+e_d(n)\) exactly. In particular, odd prime powers sharing a prime factor with d belong to \(e_d\); they have not disappeared in a coprimality restriction. The principal \(p_d\) has period q and exact mean zero over that period.

Define separately, before projecting,

\[
f_d^P(x)=A(x)\sum_n p_d(n)k(x,n),\qquad
f_d^E(x)=A(x)\sum_n e_d(n)k(x,n).
\tag{5}
\]

For every d one has \(f=f_d^P+f_d^E\), hence
\(P_Jf=P_Jf_d^P+P_Jf_d^E\). Although f is common to all d, these two summands are not. The following calculation does not substitute a single universal projected model for f.

The periodic sequence (4) is an exact algebraic model, not an asserted asymptotic for the actual primes. Its use in (5) therefore requires no PNT in growing moduli.

## 4. Every Ramanujan harmonic, including the parity cancellation

Let

\[
c_q(l)=\sum_{\substack{b\bmod q\\(b,q)=1}}e^{-2\pi i lb/q}
\]

be the Ramanujan sum. The Fourier coefficients of \(p_d\) are exactly

\[
\gamma_d(l)=\frac{c_q(l)}{\varphi(q)}
-\mathbf1_{d\mid l}(-1)^{l/d},\qquad l\in\mathbb Z.
\tag{6}
\]

Indeed the first term is the discrete Fourier transform of the unit indicator. The transform of \(2\mathbf1_{n\text{ odd}}\) is \(\mathbf1_{d\mid l}(-1)^{l/d}\). For every multiple \(l=jd\), all units mod \(2d\) are odd and

\[
c_{2d}(jd)=(-1)^j\varphi(2d).
\]

Consequently

\[
\gamma_d(l)=0\quad(d\mid l),
\tag{7}
\]

including \(l=0\). When \(d\nmid l\),

\[
|\gamma_d(l)|\le\frac{(q,l)}{\varphi(q)}
\le\frac{|l|}{\varphi(q)}.
\tag{8}
\]

For completeness, \(|c_q(l)|\le(q,l)\) follows directly on prime powers and then multiplicatively. At \(q=p^a\), the three possibilities are \(\varphi(p^a)\) if \(p^a\mid l\), \(-p^{a-1}\) if \(p^{a-1}\mid l\) but \(p^a\nmid l\), and zero otherwise. Each satisfies the claimed bound.

The exact Fourier/Poisson identity for a smooth compact function of n is

\[
\sum_n p_d(n)k(x,n)
=\sum_{l\in\mathbb Z}\gamma_d(l)
\widehat{k(x,\cdot)}(l/q),
\tag{9}
\]

where \(\widehat k(\xi)=\int k(x,u)e^{-2\pi i\xi u}du\). To check the sign, expand the periodic sequence into its q Fourier modes and apply ordinary integer-lattice Poisson to each. Reindexing produces \(\gamma_d(-l)\), which equals \(\gamma_d(l)\) because the Ramanujan and parity coefficients are real and even. There is no extra q factor in (9): \(\gamma_d\) already contains the normalization \(1/q\) from the finite Fourier transform.

At fixed x, the n kernel is smooth on a section of length \(O(Y)\), and for each fixed j,

\[
\|\partial_n^j k(x,\cdot)\|_1\ll_j Y^{1-j},\qquad
|\widehat{k(x,\cdot)}(l/q)|\ll_jY(1+Y|l|/q)^{-j}.
\tag{10}
\]

These are derivatives of the exact Pareto kernel; \(T/x\asymp1/Y\). In the central geometry \(Y/q\) lies in a fixed compact subset of \((0,\infty)\). Using (7), (8), and the fixed choice \(j=4\), the full infinite harmonic series is absolutely bounded by

\[
\left|\sum_n p_d(n)k(x,n)\right|
\ll\frac Y{\varphi(q)}
\sum_{l\ne0}|l|(1+c|l|)^{-4}
\ll\frac Y{\varphi(d)}.
\tag{11}
\]

Thus no finite harmonic truncation, stationary-phase approximation, or discarded parity mode is needed for the principal estimate. Since A is bounded and compactly supported in a fixed logarithmic-coordinate interval,

\[
\boxed{\|f_d^P\|_{L^2(dx/x)}\ll\frac Y{\varphi(d)}.}
\tag{12}
\]

## 5. The noncompact projection and the entire principal contribution

The sharp Mellin projection defined by \(\mathbf1_J\) is an \(L^2(dx/x)\) contraction. Therefore

\[
\|P_Jf_d^P\|_{L^2(dx/x)}\le\|f_d^P\|_{L^2(dx/x)}.
\tag{13}
\]

The function on the left is generally not compactly supported. This causes no loss in the following calculation: the output integral in (3) is over \(dK<m\le2dK\asymp X\). Its logarithmic-coordinate length is bounded, and \(|\log(m/d)|\ll\ell\). For each alias \(r=1,2\), Cauchy gives

\[
\left|\int_{dK}^{2dK}\log(m/d)(P_Jf_d^P)(m)e^{-\pi i rm/d}dm\right|
\ll X\ell\,\frac Y{\varphi(d)}.
\tag{14}
\]

Let \(\mathcal C_J^P\) mean (3) with the d-th summand using \(f_d^P\). Then

\[
|\mathcal C_J^P|\ll\frac Y\ell
\sum_{D<d\le2D}\frac1{d\varphi(d)}.
\tag{15}
\]

The elementary reciprocal-totient mean bound supplies

\[
\sum_{D<d\le2D}\frac1{d\varphi(d)}\ll\frac1D.
\tag{16}
\]

Here is a direct proof. The multiplicative identity

\[
\frac n{\varphi(n)}=\sum_{a\mid n}\frac{\mu(a)^2}{\varphi(a)}
\]

gives

\[
\sum_{n\le2D}\frac n{\varphi(n)}
\le2D\sum_{a\ge1}\frac{\mu(a)^2}{a\varphi(a)}
=2D\prod_p\left(1+\frac1{p(p-1)}\right)\ll D.
\]

The product converges by comparison with \(\sum_{n\ge2}n^{-2}\). Divide by \(D^2\) on the dyadic interval to prove (16). It is harmless to include even d and nonsquarefree d in this upper bound.

Combining (15), (16) yields the promised unconditional model estimate

\[
\boxed{\mathcal C_J^P\ll\frac{Y}{D\ell}\ll\frac1\ell=o(1).}
\tag{17}
\]

It controls all projected output cross terms and all input Ramanujan harmonics. It does not need a pointwise bound for the projected function or compactness of its output.

For squarefree odd d, the first two isolated coefficients do satisfy
\(\mu(d)(-1)^r\gamma_d(r)=\mu(d)^2/\varphi(d)\), \(r=1,2\), when \(d>2\). That coefficient is nonnegative. It does not turn the full integral into a positive quantity, and its total contribution is subject to (17). A missing \(\varphi(d)\) or a missing normalization logarithm can incorrectly turn this small model term into an apparent order-one main.

## 6. The finite actual discrepancy, with the projection moved legally

The root investigator supplied the useful bilinear transpose formulation below; I independently checked its sign and normalization. Write \(v=\log m\), \(\widetilde f(v)=f(e^v)\), and

\[
g_d(v)=e^v\log(e^v/d)\mathbf1_{dK<e^v\le2dK}
\left[-e^{-\pi i e^v/d}+e^{-2\pi i e^v/d}\right].
\tag{18}
\]

The sharp endpoint convention in this ordinary integral changes no Lebesgue integral. The bilinear identity, with no conjugates inserted, is

\[
\int_{\mathbb R}g_d(v)(P_J\widetilde f)(v)dv
=\int_{\mathbb R}\widetilde f(v)(P_{-J}g_d)(v)dv.
\tag{19}
\]

The sign is \(-J\), not J. In Fourier coordinates the bilinear pairing is \((2\pi)^{-1}\int\widehat g_d(-t)\widehat{\widetilde f}(t)dt\), so the multiplier \(\mathbf1_J(t)\) moves to \(\mathbf1_{-J}(-t)\) on the other factor. Both functions are in \(L^2\); the bilinear integrals converge by Cauchy. No pointwise tail argument is needed.

Define

\[
L_{d,J}(n)=\int_0^\infty A(x)k(x,n)(P_{-J}g_d)(\log x)\frac{dx}{x}.
\tag{20}
\]

This weight is zero unless \(X<n<2X+2Y<3X\). Although \(P_{-J}g_d\) is generally noncompact, the exact factors A and k keep the original prime-variable support finite. Its dependence on d and J remains, and it is not replaced by an unprojected weight.

Apply (19) separately to each of (5). The exact residual is

\[
\boxed{
\mathcal C_J^E=
\frac1{X\ell^2}\sum_{d\text{ in the sharp odd interval}}
\frac{\mu(d)}d\sum_{X<n<3X} e_d(n)L_{d,J}(n).}
\tag{21}
\]

All interchanges in this display are over finite n and d sums and an absolutely convergent bilinear \(L^2\) integral. Consequently (2) and (17) prove

\[
\boxed{Z_J=\mathcal C_J^E+O(1/\ell)+O(T^{-1/2}).}
\tag{22}
\]

Negative t is handled by conjugation for the real original data: the symmetric band contributes \(2\operatorname{Re}Z_J\). Equations (17), (22) are therefore equally valid for the paired real contribution with the obvious factor two.

## 7. The precise failed implication in the proposed bridge

The finite periodic model is negligible, but there is no estimate here of

\[
\sum_{d\sim D,\ d\text{ odd}}\frac{\mu(d)}d
\sum_n e_d(n)L_{d,J}(n)=o(X\ell^2).
\tag{23}
\]

Proving (23) would give a genuine \(o(1)\) bound for this stationary band. Conversely, (22) shows that an \(o(1)\) bound for this band implies (23). This equivalence concerns only the specified central band, not the global variance or its strict threshold.

On a reduced residue class a modulo \(q=2d\), the discrepancy in (4) is exactly the prime sequence minus \(q/\varphi(q)\) times the integer lattice on that class. On a nonreduced odd class, it retains the actual prime powers. Hence (21) really is a progression-model error with a d-dependent, projected test. Computing the principal Fourier coefficients does not estimate this error.

Replacing this error by zero on the grounds that primes should be uniform in residues would introduce an unproved assertion at \(q\asymp\sqrt X\) for these particular oscillatory tests and their Möbius-weighted sum. Ordinary RH concerns the Riemann zeta function; no estimate for all required Dirichlet-L-function progression errors has been assumed or derived. In addition, replacing the discrete unit-class model by a continuous class-independent integral at this oscillation scale would itself need a lattice-error calculation. Equations (6)–(17) kept that lattice exactly.

There is therefore a definite answer to the attempted shortcut. The principal calculation is legal after the d-dependent split and is small. The noncompact projection is manageable and does not force infinite prime support. The proposed transition from a Ramanujan principal to a signed estimate for the actual zeta statistic fails at (23), not at an endpoint or a hidden projection identity. No signed gain for (23) is claimed.

## 8. Verification scope

This note proves the periodic Fourier formula, full-harmonic bound, reciprocal-totient mean estimate, and projection transpose directly. Its only inherited analytic input is the already reviewed central representation (2) and the exact smooth-kernel derivative estimates. The companion checker verifies finite Fourier coefficients, cancellation of parity modes, Ramanujan bounds, reciprocal-totient identities, and finite Fourier-projection transpose signs. It does not certify the asymptotic proof or run prime experiments.

Programme dependencies:

- Corrected R29 `signed-mellin-test/SIGNED_MELLIN_BLOCK_BOUND.md`, SHA256 `753f116b8ebc5d6cc7d7a4e148c98e9b8ef9df97d4327efe2fa094507aa13492`.
- R30 `stationary-challenge/SHARP_ODD_STATIONARY_CHALLENGE.md`, SHA256 `0d480d4f35ca1ce0c36c31deffd2a8e6bd39f6ddc1420180f9a32f70b829fcf7`, especially its exact first-band representation and integrated error.
- Root investigator's communicated bilinear transpose identity, independently checked in (18)–(21), is attributed here rather than presented as a new independent discovery.

The finite checker passed 66 exact Fourier cases, 10 cancelled parity modes, 401 Ramanujan bounds, 50 reciprocal-totient identities, and one bilinear transpose identity with an incorrect-same-sign control rejected. Root read all eight sections and found no substantive gap; its sole wording correction, now incorporated, states the contraction for the sharp multiplier \(\mathbf1_J\) actually defined here. This records ordinary independent review, not formal certification.

No new external model, numerical prime scan, Git mutation, or syntax-runtime repair was performed for this follow-up.
