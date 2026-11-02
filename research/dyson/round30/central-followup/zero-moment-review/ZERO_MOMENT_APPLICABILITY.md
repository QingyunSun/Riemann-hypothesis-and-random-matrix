# Zero sampling of the sharp central Möbius polynomial

Date: 2026-09-08 UTC. Status: bounded ordinary source/applicability investigation. No famous conjecture or strict signed correlation improvement is proved. The result below is an elementary application of existing RH zero-counting and Dirichlet-polynomial estimates, with no novelty claim.

The exact central polynomial is
\[
M_D(t)=\sum_{\substack{D<d\le2D\\d\ {\rm odd}}}\mu(d)d^{it},
\qquad D\asymp T,\quad X=T^2.
\]
Its coefficients and sharp endpoints are unchanged. The R29 target contains the integral of \(\widehat f(t)M_D(t)B_K(t)\), normalized by \(\pi X(\log T)^2\). A theorem for the separate values of \(M_D\) at zero ordinates is not automatically an estimate for that joint integral.

## 1. An exact primary discrete theorem applies, but its error is too large

Bui, Florea and Milinovich, *Negative discrete moments of the derivative of the Riemann zeta-function*, Theorem 3.1, states under RH, for arbitrary complex coefficients and every \(x\ge2\),
\[
\begin{split}
\sum_{0<\gamma\le H}\left|\sum_{n\le x}a_n n^{-\rho}\right|^2
={}&N(H)\sum_{n\le x}\frac{|a_n|^2}{n}
-\frac H\pi\Re\sum_{kn\le x}
\frac{\overline{a_{kn}}a_n\Lambda(k)}{kn}\\
&+O\!\left(x\log^2(xH)\sum_{n\le x}\frac{|a_n|^2}{n}\right).
\tag{1}
\end{split}
\]
Here \(\rho=1/2+i\gamma\), with multiplicities. This theorem has no formal \(x<T^{1/2}\) restriction. Its displayed error, rather than a universal short-polynomial rule, determines usefulness. The original theorem and complete surrounding proof were checked in the retained primary preprint, printed pages 8–10; the journal statement agrees. [Primary journal theorem](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.13092), [author preprint](https://arxiv.org/abs/2310.03949).

Set \(x=2D\) and
\[
a_n=\sqrt n\,\mu(n)\mathbf1_{D<n\le2D,\ n\ {\rm odd}},
\qquad A_2=\sum_{D<n\le2D,\ n\ {\rm odd}}\mu(n)^2.
\]
Then the left side of (1) is exactly \(\sum|M_D(\gamma)|^2\), since the coefficients are real and changing the phase sign conjugates the polynomial. Coefficient growth of \(\sqrt n\) is allowed by the stated theorem and is fully charged in its norm.

The entire prime-power cross term in (1) is zero. Indeed, if both \(a_n\) and \(a_{kn}\) are nonzero and \(k\ge2\), then \(n>D\) gives \(kn>2D\), a contradiction. The \(k=1\) term has \(\Lambda(1)=0\). This argument retains the endpoints and does not discard an oscillatory term by sign.

Applying (1) at \(H=c_1T,c_2T\), for fixed \(0<c_1<c_2\), and subtracting gives the applicable conclusion
\[
\sum_{c_1T<\gamma\le c_2T}|M_D(\gamma)|^2
=\bigl[N(c_2T)-N(c_1T)\bigr]A_2
+O\bigl(DA_2\log^2(DT)\bigr).
\tag{2}
\]
For \(D\asymp T\), \(A_2\ll D\), this error is \(O(T^2\log^2T)\), whereas the diagonal has scale \(T A_2\log T\). Thus (2) gives no logarithmic improvement. An asymptotic from this particular error requires \(D\log T=o(T)\). For example \(D\le T/(\log T)^{1+\varepsilon}\) suffices for fixed \(\varepsilon>0\). This is an error comparison, not a proof that all critical-length discrete mean values are inaccessible.

## 2. A sharper critical-length comparison follows directly from zero counting

The dyadic support allows a useful improvement over the crude error in (2), while still giving no joint gain. Fix \(0<a<b\), let \(w\in C_c^1((a,b))\) be real, and allow arbitrary complex coefficients \(c_d\) on the same sharp odd interval. Write
\[
P(t)=\sum_d c_d d^{it},\qquad A_2=\sum_d|c_d|^2.
\]
Then under RH,
\[
\boxed{
\sum_{\gamma>0}w(\gamma/T)|P(\gamma)|^2
=\frac{\log T}{2\pi}\int_0^\infty w(t/T)|P(t)|^2dt
+O_{w,a,b}\!\left((T+D)A_2\frac{\log T}{\log\log T}\right).}
\tag{3}
\]
The constant is uniform in all these coefficients. In particular, (3) is applicable at \(D\asymp T\). No simplicity or zero-spacing assumption is required.

Proof. Use the exact counting function with multiplicities, and set
\[
L(t)=\frac{t}{2\pi}\log\frac{t}{2\pi}-\frac{t}{2\pi}+\frac78,
\qquad R(t)=N(t)-L(t).
\]
The Riemann–von Mangoldt formula and the RH bound for \(S(t)\) give
\[
\sup_{aT\le t\le bT}|R(t)|\ll_{a,b}\frac{\log T}{\log\log T}.
\tag{4}
\]
One can use right-continuous \(N\) and its one-sided values at zeros; these satisfy the same bound by passage to one-sided limits. This avoids requiring a special convention for the averaged value of \(S\) at an ordinate. A precise primary input is Carneiro–Chandee–Milinovich, *Bounding S(t) and S1(t) on the Riemann hypothesis*, equation (1), printed page 1, and Theorem 2, printed page 2. Only its order bound is used here. [Primary preprint](https://arxiv.org/abs/1309.1526).

Remove the irrelevant common phase:
\[
Q(t)=D^{-it}P(t)=\sum_d c_d e^{it\log(d/D)}.
\]
Its frequencies belong to \((0,\log2]\). Montgomery–Vaughan mean value, on the containing interval \([aT,bT]\), gives
\[
\int|Q|^2dt\ll_{a,b}(T+D)A_2,
\qquad
\int|Q'|^2dt\ll_{a,b}(T+D)A_2,
\tag{5}
\]
because the second coefficient norm is at most \((\log2)^2A_2\). This is the usual finite Dirichlet-polynomial theorem applied to \(c_d\log(d/D)\); the phase removal preserves absolute values. The existing R29 mean-value source supplies precisely this translated-interval estimate.

For \(H(t)=w(t/T)|Q(t)|^2\), Cauchy and the product rule imply
\[
\begin{split}
\int|H'(t)|dt
&\le\frac{\|w'\|_\infty}{T}\int|Q|^2dt
+2\|w\|_\infty\left(\int|Q|^2dt\int|Q'|^2dt\right)^{1/2}\\
&\ll_{w,a,b}(T+D)A_2.
\tag{6}
\end{split}
\]
Stieltjes integration by parts has zero outer boundary terms because \(w\) is compactly supported. Therefore
\[
\sum_{\gamma>0}H(\gamma)
=\int H(t)L'(t)dt-\int R(t)H'(t)dt.
\]
Insert (4)–(6), and use
\(L'(t)=(2\pi)^{-1}\log(t/(2\pi))=(2\pi)^{-1}\log T+O_{a,b}(1)\).
The last replacement costs \(O((T+D)A_2)\), absorbed by the error in (3). This proves the assertion, retaining every multiplicity. \(\square\)

For the actual Möbius coefficients and \(D\asymp T\), (3) gives
\[
\sum_\gamma w(\gamma/T)|M_D(\gamma)|^2\ll_w T^2\log T
\quad(w\ge0),
\tag{7}
\]
and more precisely
\[
\frac{2\pi}{\log T}\sum_\gamma w(\gamma/T)|M_D(\gamma)|^2
=\int w(t/T)|M_D(t)|^2dt+O_w(T^2/\log\log T).
\tag{8}
\]
Thus density-normalized sampling at actual zeros reproduces the continuous norm up to an additive \(o(T^2)\) error. This is an absolute error: a relative \(o(1)\) assertion requires an independently established lower bound of order \(T^2\) for that continuous norm. No such lower bound for every short carrier window is asserted here. The comparison does not reduce that continuous norm by a power of a logarithm. The continuous integral at critical length still contains its actual coefficient correlations; it was not replaced by its diagonal in this proof.

For comparison, if \(D=o(T)\), weighted Montgomery–Vaughan gives
\[
\int w(t/T)|P(t)|^2dt
=T A_2\int w(u)du+O_w(DA_2).
\]
Indeed apply the translated-interval mean-value formula to cumulative integrals and integrate by parts against the fixed profile. For \(w\ge0\), \(\int w>0\), (3) consequently gives the usual positive diagonal asymptotic with relative error \(O_w(D/T+1/\log\log T)\). No improvement of the generic sampled norm can follow merely from the fact that the sample points are zeta zeros, even for these actual shorter Möbius annuli. This statement does not assert a lower asymptotic for the central \(D\asymp T\) interval.

## 3. The actual Möbius-prefix theorem is also not a smallness theorem

Milinovich–Ng, *A note on a conjecture of Gonek*, Proposition (2.3), proves under RH for fixed \(0<\theta<1\), \(\xi=T^\theta\),
\[
\sum_{0<\gamma\le T}
\left|\sum_{n\le\xi}\mu(n)n^{-1/2-i\gamma}\right|^2
=\frac3{\pi^3}(\theta+\theta^2)T\log^2T+O(T\log T).
\tag{9}
\]
The separate reciprocal-derivative result in that paper additionally assumes simplicity; (9) itself does not. Its discussion of general polynomials of length \(\xi\le T\) is not a coefficient-uniform endpoint asymptotic. The proof in §4 has a horizontal contour error \(O(\xi\log^2T)\). [Primary author PDF](https://home.olemiss.edu/~mbmilino/Gonek.pdf), printed pages 3–4 and 7.

Equation (9) concerns a prefix, the weight \(n^{-1/2}\), and a fixed exponent below one. Our polynomial is a sharp odd annulus with no \(n^{-1/2}\) weight and length comparable to \(T\). Passing between them requires sharp endpoint differences and an amplitude partial summation; values or cross moments of all these prefixes are not supplied for free. Moreover (9) has a positive main term of the natural sampled size. Its statement gives no reason to expect the relevant Möbius polynomial to vanish at the sample ordinates.

The suggested identity \(1/\zeta(1/2+i\gamma)=0\) is false. If \(\rho\) is a zero of multiplicity \(m\), write \(\zeta(s)=(s-\rho)^m g(s)\) with \(g(\rho)\ne0\); its reciprocal has a pole of order \(m\). At a simple zero its residue is \(1/\zeta'(\rho)\), exactly the residue used in the cited paper. The reciprocal vanishes at the pole \(s=1\) of \(\zeta\). A sharply truncated finite polynomial is entire and satisfies no automatic vanishing relation at either set of points.

## 4. What the source-valid comparison does and does not buy

There is an actual applicable theorem here: (3) controls the critical-length zero sampling using the narrow multiplicative support and RH zero-counting discrepancy. It improves the crude separate discrete upper bound coming from (1). After dividing by zero density, however, (7) returns the same \(O(T^2)\) Möbius norm already used in R29. Substitution into a separately bounded Cauchy argument cannot produce the missing logarithmic saving.

The R29 prime-error factor is built from the same actual zeros. Replacing it by its explicit formula introduces its oscillatory phases and a kernel relating the integration frequency to zero ordinates. Neither (1), (3), nor (9) controls those correlations or by itself authorizes replacing that kernel by point evaluation at \(t=\gamma\). The separate proof of (3) uses a positive quadratic observable. Applying Stieltjes integration to the full product requires its own derivative estimate, which the subsequent companion argument below does supply.

The unwindowed square \(|D^{-it}M_D(t)|^2\) has frequencies \(\log(d/e)\in[-\log2,\log2]\), a fixed width compared with the increasing zero density of order \(\log T\). This explains why its smooth sampling comparison needs only low-frequency zero counting. Multiplication by the actual prime-error phase changes that test. The fixed smooth window itself is not claimed to be exactly band-limited.

### Subsequent exact joint-sampling comparison

The root investigator then supplied [a complete joint-variation proof](../ROOT_JOINT_ZERO_SAMPLING.md), which I read and independently checked. For the fixed positive smooth carrier window and original R29 factors, it proves
\[
\frac1{\pi X\ell^2}\int w(t/T)\widehat f(t)M_D(t)B_K(t)dt
=\frac2{X\ell^3}\sum_{\gamma>0}w(\gamma/T)
\widehat f(\gamma)M_D(\gamma)B_K(\gamma)
+O(1/\log\log T).
\tag{J}
\]
The error is absolute. All three large common phases cancel except \(\log(DK/X)=O(1)\). The centered derivative of \(\widehat f\) is the phase-shifted Mellin transform of \(-i\log(x/X)f(x)\); its \(L^2\) bound follows already from Plancherel and bounded \(\log(x/X)\) on the compact support. The centered derivatives of the two polynomials have weights \(i\mu(d)\log(d/D)\) and \(i\log k\log(k/K)\). Their mean-value and sharp partial-summation bounds retain the original endpoints. Cauchy then gives both the product's \(L^1\) norm and its derivative's \(L^1\) norm as \(O(T^2\ell^2)\). Equation (4) and Stieltjes integration yield (J), including the factor two.

This pays the actual joint variation cost and supersedes any categorical suggestion that only the separate norm can be sampled. The right side remains the same signed prime-error/Möbius correlation evaluated at actual zeros; it is not smaller by this comparison, and no coefficient vanishes automatically. Negative carrier windows follow by conjugation for the original real profiles. There is no asymptotic evaluation of the joint zero sum.

The remaining obligation is therefore an estimate for the actual signed prime-error/Möbius kernel, beyond density-normalized separate norms. No RH impossibility theorem is asserted: another argument exploiting their joint arithmetic could still improve the carrier. No sub-half gap, AH contradiction, or strict global variance deficit follows from this note.

## 5. Additional requested height-localization check

The complete companion `UPPER_HEIGHT_BALANCED_CHECK.md` was read. Its inequalities remain uniform for \(2\le\alpha\le9/4\), with \(X=T^\alpha\): the separation \(\delta>0\) enters only when converting the final high-band bound into a vanishing power. Thus for the stated full unmasked balanced block, with uniformly controlled fixed profiles and factor comparison constants, its proof supplies
\[
|Z(X)|\ll\frac{T^{-141/800}}{\sqrt{\log T}}+
\left(\frac{T^2}{X}\right)^{3/4}.
\tag{10}
\]
At \(\alpha=2\), the second term is one. The Selberg containment, correction debts, Perron range, low-frequency cutoff comparison, and high-band sum all remain valid at that endpoint; none claims vanishing there.

For a specified uniformly controlled dyadic family \(X_j=2^jT^2\), with \(j\ge J\) and \(X_j\le T^{9/4}\), summing (10) gives
\[
\sum_{j\ge J}|Z(X_j)|
\ll T^{-141/800}\sqrt{\log T}+2^{-3J/4}.
\]
There are \(O(\log T)\) low-term copies and a convergent geometric high-term sum. Hence the limsup is \(O(2^{-3J/4})\). This is tightness for that specified balanced family, not elimination of its fixed \(j=0,1,\ldots\) blocks or identification with the masked, unbalanced, and shift-dependent R26 collection.

## 6. Verification boundary

The new proof is ordinary analysis. Primary statements and the relevant surrounding arguments were read; the source PDFs and extracted texts are retained with hashes. No large scan, model call, numerical estimate for actual zeros, formal verification, Git mutation, or novelty claim is part of this bounded investigation. The source receipt pins the R29 target and the companion height proof used above.
