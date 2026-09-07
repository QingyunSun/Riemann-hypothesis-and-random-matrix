# Weighted Mellin energy of the actual centered prime window

Status: ordinary analytic derivation under RH, prepared for independent review. This note concerns the actual smooth real extension of the R27 prime-window matrix. It proves bounds with the full \(\log^2 X\) factor; it does not assert a one-block \(Y\log X\) estimate, a strict Bragg deficit, or an operator-norm saving.

## 1. Objects, scope, and verification boundary

The conceptual object is a smooth function obtained by moving a compact prime window continuously in its left endpoint. Differentiation acts on the window at fixed prime endpoint. This distinction preserves exact centering and avoids differentiating an error term in the prime number theorem.

The implementation boundary is one proof note, one small symbolic checker, and pinned source receipts. No new prime values, matrices, parameter scans, external models, or repository changes are needed. The checks verify elementary differential and normalization identities; source estimates and the analytic argument require ordinary proof review. A sharper logarithm, cancellation in the signed Möbius contraction, and control through every cofactor alias remain postponed.

Fix real \(\chi,V\in C_c^\infty((1,2))\) and the programme's fixed real smooth compact function \(\omega\), supported in \([7/4,9/4]\). Put
\[
X=T^2,\qquad Y=T,\qquad \ell=\log T,\qquad T\longrightarrow\infty.
\tag{1}
\]
For \(x>0\) define the exact inherited kernel
\[
b_T(x)=\frac{T x^{-T}}{\ell^2}
 \int_1^x\omega\!\left(\frac{\log u}{\ell}\right)u^{T-2}\,du,
\quad
F(x,y)=b_T(x)\chi(x/X)V(y/Y)
 \left(\frac{x}{x+y}\right)^T .
\tag{2}
\]
Only \(x\asymp X\) and positive \(y\asymp Y\) occur. Define
\[
f(x)=X\ell^2\sum_{\substack{n\ge1\\ n\ {\rm odd}}}
 F(x,n-x)(\Lambda(n)-2).
\tag{3}
\]
The sum is finite on the common support of the summands. The profiles vanish to every order at their support boundaries, so \(f\in C_c^\infty((0,\infty))\). At an odd integer \(m\), changing variables \(h=n-m\) proves that (3) equals the exact R27 \(f_T(m)\), with even \(h\) and flat center \(2\). Values at even integers are not used to identify the R27 convention, which sets its discrete function to zero there.

All odd prime powers are included in \(\Lambda\). This definition is not a formal infinite prime series.

Use the Mellin convention
\[
\widehat f(t)=\int_0^\infty f(x)x^{-it}\frac{dx}{x},
\qquad \mathcal D=x\partial_x .
\tag{4}
\]

**Theorem.** Assume RH. For every fixed integer \(j\ge0\), there are constants \(C_j,T_j\), depending only on \(j\) and the fixed profiles, such that for every real \(T\ge T_j\),
\[
\int_0^\infty|\mathcal D^j f(x)|^2\frac{dx}{x}
 \le C_jT^{2j}Y(\log X)^2,
\tag{5}
\]
and
\[
\int_{\mathbb R}\left(1+\frac{t^2}{T^2}\right)^j
 |\widehat f(t)|^2\,dt
 \ll_j Y(\log X)^2.
\tag{6}
\]
The constants are not asserted to be uniform as \(j\) grows with \(T\).

## 2. The exact primary-source input

Carneiro, Chandee, Chirre, and Milinovich, *On Montgomery's pair correlation conjecture: a tale of three integrals*, define the full von Mangoldt counting function and the Selberg integral in (1.1), then record the RH estimate in (1.3), printed page 1. We need only its fixed value \(\beta=3\):
\[
\int_1^{S^3}
 \left|\Psi(x+x/S)-\Psi(x)-x/S\right|^2
 \frac{dx}{x^2}
 \ll\frac{\log^2 S}{S}
\quad(S\longrightarrow\infty).
\tag{7}
\]
This is inside the original stated range \(1<\beta\le4\). The theorem is applied with this one fixed \(\beta\), not a moving family of test functions or an unproved uniformity in \(\beta\). See the [author-hosted primary PDF](https://www.math.ksu.edu/~chandee/20210207_PSI_Arxiv.pdf), (1.1) and (1.3). The exact retained PDF and extracted text are pinned in the source receipt.

## 3. Differentiate the kernel at fixed prime endpoint

Write
\[
W(x,y)=X\ell^2F(x,y),\qquad
A_T(x)=X\ell^2 b_T(x)\chi(x/X).
\]
For any fixed integer \(r\ge0\),
\[
|\mathcal D^r A_T(x)|\ll_r1\qquad(x\asymp X).
\tag{8}
\]
Indeed, after \(u=xv\), with \(\omega\) extended by zero,
\[
X\ell^2 b_T(x)
=\frac{TX}{x}\int_0^1
 \omega\!\left(\frac{\log x+\log v}{\ell}\right)v^{T-2}\,dv.
\tag{9}
\]
Extending the lower limit from \(1/x\) to zero is exact: its added integrand has nonpositive argument of \(\omega\). Differentiation in \(\log x\) only differentiates \(X/x\) and the fixed profile, and
\(T\int_0^1v^{T-2}dv=T/(T-1)=O(1)\).
This proves (8), including derivatives of \(\chi\), without replacing \(b_T\) by an asymptotic expression.

At fixed \(n=x+y\), the differentiation operator is
\[
\mathcal A=x(\partial_x-\partial_y),\qquad
K_j(x,y)=\mathcal A^jW(x,y).
\tag{10}
\]
It is not \(x\partial_x\) with \(y\) frozen. In particular the exact Pareto factor \(P(x,y)=(x/(x+y))^T\) satisfies
\[
\mathcal A P=TP,\qquad
\mathcal A V(y/Y)=-\frac{x}{Y}V'(y/Y).
\tag{11}
\]
Choose constants \(1<a<b<2\) and \(1<c<d<2\) containing the supports of \(\chi\) and \(V\) respectively. Leibniz' rule, (8), and \(x/Y\asymp T\) give
\[
\operatorname{supp}K_j\subset[aX,bX]\times[cY,dY],
\quad
|K_j(x,y)|\ll_jT^j,
\quad
|\partial_yK_j(x,y)|\ll_j T^j/Y.
\tag{12}
\]
For completeness, each application of \(\mathcal A\) either differentiates \(A_T\), differentiates a coefficient \(x/Y\), differentiates a fixed derivative of \(V\) at a cost \(x/Y\), or multiplies \(P\) by \(T\). Differentiating a resulting term once in \(y\) costs \(O(1/Y)\): it differentiates a \(V\) derivative or uses \(\partial_yP=-T P/(x+y)\). Thus (12) follows for every fixed \(j\). No coefficients or roots depend on a prime-counting estimate here.

Termwise differentiation in the finite sum (3) yields
\[
\mathcal D^j f(x)=
 \sum_{n\ {\rm odd}}K_j(x,n-x)(\Lambda(n)-2).
\tag{13}
\]

## 4. Exact odd centering and the two-variable short-interval bound

For real \(x>0,y\ge0\), put
\[
B_x(y)=\sum_{\substack{x<n\le x+y\\n\ {\rm odd}}}(\Lambda(n)-2).
\]
With real endpoint conventions as displayed,
\[
\begin{aligned}
B_x(y)
={}&\Psi(x+y)-\Psi(x)-y\\
&-\sum_{x<2^r\le x+y}\log2
 +y-2\#\{n\ {\rm odd}:x<n\le x+y\}.
\end{aligned}
\tag{14}
\]
The final staircase has absolute value at most \(2\). On our support \(x+y<2x\) for all sufficiently large \(T\), so at most one power of \(2\) appears; its contribution is at most \(\log2\). Thus (14) differs from the full centered \(\Psi\) increment by \(O(1)\), uniformly in both real endpoints. It discards no odd prime powers.

Partial summation, using the vanishing endpoints of \(K_j\), gives the exact formula
\[
\mathcal D^j f(x)=-\int_{cY}^{dY}B_x(y)\partial_yK_j(x,y)\,dy.
\]
Consequently
\[
|\mathcal D^j f(x)|^2
 \ll_j\frac{T^{2j}}{Y}\int_{cY}^{dY}|B_x(y)|^2\,dy.
\tag{15}
\]
The following change of variables is essential: it applies (7) to a fixed fractional increment, not to a varying one while pretending it is fixed. Put
\[
\lambda=\frac{Ty}{x},\qquad
\lambda_0=c/b,\quad\lambda_1=d/a .
\]
Positivity and \(dy=(x/T)d\lambda\) show that the full centered part of
\[
I=\int_{aX}^{bX}\frac{dx}{x}
       \int_{cY}^{dY}|B_x(y)|^2dy
\]
is bounded by
\[
\frac1T\int_{\lambda_0}^{\lambda_1}
 \int_{aX}^{bX}
 |\Psi(x+\lambda x/T)-\Psi(x)-\lambda x/T|^2
 \,dx\,d\lambda.
\tag{16}
\]
For each fixed \(\lambda\) in this compact interval set \(S=T/\lambda\).
For all sufficiently large \(T\), simultaneously for every such \(\lambda\),
\(bX<S^3\), \(\log S\asymp\log T\), and \(1/S\asymp1/T\).
Multiplying (7) by \((bX)^2\) therefore bounds the inner integral by
\[
\ll X^2\frac{\log^2 T}{T}.
\]
Uniformity is legitimate: (7) supplies one constant and one threshold for every real \(S\) above that threshold; all \(T/\lambda\) exceed it together. There is no invocation of a moving-profile estimate.
The \(O(1)\) correction in (14) contributes \(O(Y)\) to \(I\). We conclude
\[
I\ll\frac{X^2}{T^2}\log^2T+Y
 \ll Y^2(\log X)^2.
\tag{17}
\]
Combining (15) and (17) proves (5).

## 5. Weighted Mellin consequence

Set \(g(v)=f(e^v)\). Then \(g\in C_c^\infty(\mathbb R)\),
\(\widehat f(t)=\int g(v)e^{-itv}dv\), and
\(g^{(r)}(v)=\mathcal D^r f(e^v)\).
The ordinary Fourier Plancherel identity therefore gives exactly
\[
\int_{\mathbb R}t^{2r}|\widehat f(t)|^2dt
 =2\pi\int_0^\infty|\mathcal D^r f(x)|^2\frac{dx}{x}.
\tag{18}
\]
Expand \((1+t^2/T^2)^j\), apply (5) for \(0\le r\le j\), and obtain (6).
In particular, for every fixed \(j\) and \(B\ge0\),
\[
\int_{|t|\ge BT}|\widehat f(t)|^2dt
 \ll_j (1+B^2)^{-j}Y(\log X)^2.
\tag{19}
\]
This is an integral tail bound. It is not a pointwise estimate on a selected Mellin frequency, and it does not turn the logarithmic second-moment loss into a strict constant improvement.

## 6. Sharp odd-log cofactor intervals and their aliases

This separate elementary lemma is unconditional. Fix \(0<a_0<b_0\), \(0<\varepsilon<\pi\), and retain sharp endpoints:
\[
L_I(t)=\sum_{\substack{a_0T<k\le b_0T\\ k\ {\rm odd}}}
 (\log k)k^{it}.
\tag{20}
\]
For all sufficiently large \(T\) and
\(0<|t|\le(\pi-\varepsilon)a_0T\),
\[
|L_I(t)|\ll_{a_0,b_0,\varepsilon}
 \log(2T)\min\!\left(T,1+\frac{T}{|t|}\right).
\tag{21}
\]
To verify the alias normalization directly, write the successive odd terms as \(k,k+2\). The phase increments, measured in cycles, are exactly
\[
\delta_k=\frac{t}{2\pi}\log\!\left(1+\frac2k\right).
\tag{22}
\]
For \(t>0\) they decrease monotonically, and throughout any consecutive subinterval of (20),
\[
\frac{t}{\pi(b_0T+2)}
 \le\delta_k\le\frac{t}{\pi a_0T}
 \le1-\varepsilon/\pi.
\tag{23}
\]
The first inequality follows from \(\log(1+z)\ge z/(1+z)\); the second from \(\log(1+z)\le z\). The Kusmin–Landau inequality applies to monotone increments separated from integers. Its version with increasing increments is Theorem 16.5, printed page 6, of the [Montgomery–Vaughan author draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf). Decreasing increments follow by reversing the sequence and conjugating; negative \(t\) follows by conjugation. Applying it with a separation bounded below by a fixed constant times \(\min(1,|t|/T)\) bounds every partial interval sum by \(O(1+T/|t|)\).
Abel summation with the genuine endpoint terms for \(\log k\), and its total variation \(O(1)\) across \((a_0T,b_0T]\), proves (21). The trivial bound supplies the other term of the minimum. No smoothed replacement of the cofactor interval was made.

At \(t=0\), elementary summation on the odd lattice gives
\[
L_I(0)=\frac12\int_{a_0T}^{b_0T}\log u\,du+O(\log(2T)).
\tag{24}
\]
Thus on any fixed compact range
\(0<\tau_0\le |t|/T\le\tau_1<\pi a_0\), (21) is \(O(\log T)\), as compared with the \(T\log T\) size at zero.

All later aliases remain present. The exact increment resonances are
\[
t=\frac{2\pi q}{\log(1+2/k)}
 =\pi q\bigl(k+1+O(1/k)\bigr),\qquad q=1,2,\ldots .
\tag{25}
\]
In the continuous Poisson representation, the stationary points in odd-lattice Poisson summation obey
\(t/k=\pi q\). The first approximate alias band is
\([\pi a_0T,\pi b_0T]\); every \(q\ge2\) gives another band. No bound of the form (21) has been asserted through these bands. The sampling Nyquist condition of an oscillatory template is a different condition, corresponding to an increment of \(\pi\) radians rather than the \(2\pi q\) resonance in (22).

For the already frozen R28 interval \(a_0=1.05,b_0=1.35\), its three post-initial-data selected frequencies have \(t/T\) between \(1.1902\) and \(1.7569\). They lie below \(\pi a_0\), so (21) applies with fixed slack. This calculation explains a possible distinction: a large transpose contraction against two modulated Mellin vectors need not imply a large contraction against the unmodulated \(\log k\) vector. It proves no estimate for the accompanying Möbius factor and makes no finite-to-asymptotic inference from the matrices.

## 7. What this establishes for the actual signed pairing

Equations (5)–(6) supply the requested high-frequency energy control for the unchanged actual-prime function, and (21) identifies the legal nonstationary cofactor range. Prime powers, exact odd centering, \(b_T\), the Pareto factor, real endpoints, and compact support all remain in the derivation.

These statements do not bound the signed Möbius/log contraction sharply enough to produce a strict Bragg deficit. A separate low-frequency negative-Sobolev estimate, any joint estimate inside the cofactor alias bands, and a strict saving over the inherited global \(O(1)\) bound require their own proof. This note does not claim that an \(O(1)\) Mellin pairing would be new global information, or that these estimates resolve Montgomery's conjecture.

## 8. Retained dependencies and check scope

The source receipt pins the two primary PDFs and their extracted texts, the exact R27 definition, the R16 fixed bump, and the unchanged R28 selected-frequency data used only in the last paragraph of §6. No numerical matrix is regenerated.

The accompanying symbolic checker verifies the fixed-endpoint differential identity, the rescaled-kernel identity, the operator commutator used by the neighboring low-frequency calculation, the elementary changes of variables and the finite binomial expansion. These are sanity checks, not a formal proof of the RH source theorem or this analytic argument. The source and author receipts preserve exact hashes for independent review.
