# A bounded positivity audit of the two-scale target

Date: 2026-09-05. This note closes one bounded proof audit; it contains no new parameter scan, arithmetic estimate, or zeta result. Round 7 files were not changed.

**Conclusion.** The known interior Montgomery band, spectral positivity, and realizable stationary point-process constraints do not imply the target \(W\geq1/16\). The obstruction is an actual determinantal point process, not merely a proposed nonnegative spectrum. The additional calculation below gives an explicit, substantially weaker lower bound using pair-measure positivity. It identifies a valid inference but does not close the arithmetic obligation.

## 1. Normalization and the formal-spectrum warning

Write
\[
A=\sinh2,\quad B=\sinh1,\qquad
K(\alpha)=Ae^{-2|\alpha|}-Be^{-|\alpha|}.
\]
For a unit-intensity stationary process, let \(\mu\) be its pair measure including the diagonal, and let \(S=\widehat\mu-\delta_0\) be its centered structure-factor measure. Assume the relevant Poisson integrals are finite. The two-scale statistic is
\[
W=\int K\,dS
 =\int J(x)\,d\mu(x)-(A-B),
\quad
J(x)=\frac{A}{1+\pi^2x^2}-\frac{2B}{1+4\pi^2x^2}.
\]
The known band is \(dS(\alpha)=|\alpha|\,d\alpha\) on \((-1,1)\); this specifies no atoms at the endpoints.

The sign change is exactly
\[
\alpha_0=\log(A/B)=\log(2\cosh1)>1.
\]
Adding arbitrarily large nonnegative atoms at \(\pm R\), for fixed \(R>\alpha_0\), leaves the interior band unchanged and sends \(\int K\,dS\) to minus infinity. This proves only that **formal spectral positivity alone** supplies no finite lower bound. Such modified spectra have not been shown to be realizable by point processes and are not used as the actual obstruction below.

Pair positivity is a meaningful extra constraint. For \(y=\pi^2x^2\),
\[
J(x)=\frac{(A-2B)+(4A-2B)y}{(1+y)(1+4y)}>0.
\]
Since \(\mu\geq\delta_0\), it immediately gives the valid but weak bound \(W\geq-B\). Thus the formal unbounded-below example cannot respect all these pair constraints.

## 2. An explicit band-limited minorant

The following stronger bound is already available from the same data. It is not claimed optimal over all positivity arguments.

Set
\[
a=2\tanh1,\qquad b=2\tanh(1/2),\qquad \kappa=2b-a>0,
\]
and define
\[
R(x)=\frac{a}{1+\pi^2x^2}-\frac{2b}{1+4\pi^2x^2},
\quad
f(x)=\cos^2(\pi x)R(x)+\kappa\operatorname{sinc}^2(x),
\quad g(x)=J(x)-f(x),
\]
with \(\operatorname{sinc}(x)=\sin(\pi x)/(\pi x)\).

**Claim:** \(f\geq0\), and \(\widehat g\) is supported on \([-1,1]\), with \(\widehat g(\pm1)=0\). Consequently
\[
W\geq \widehat g(0)+2\int_0^1\alpha\widehat g(\alpha)\,d\alpha-(A-B)
=:\mathcal B.
\tag{P}
\]
The right side is an elementary expression in exponentials and hyperbolic tangents. Its floating evaluation is \(-0.208674512963925\ldots\); the exact expression, rather than these digits, is the proved bound.

To prove nonnegativity, note \(0<b<a<2b\). Direct calculation gives \(R(x)\geq-\kappa\) for all \(x\), since
\[
R(x)+\kappa
=\frac{y\{(8b-a)+(8b-4a)y\}}{(1+y)(1+4y)}\geq0.
\]
Also \(R(x)<0\) only if \(y<\kappa/(4a-2b)<1\). There \(|\pi x|<1<\pi/2\), and \(\operatorname{sinc}^2(x)\geq\cos^2(\pi x)\). Hence
\(f\geq\cos^2(\pi x)(R+\kappa)\geq0\). Where \(R\geq0\), nonnegativity is immediate.

For the Fourier support, put \(E(\alpha)=ae^{-2|\alpha|}-be^{-|\alpha|}\). Then
\[
\widehat f(\alpha)=\tfrac12E(\alpha)
 +\tfrac14E(\alpha-1)+\tfrac14E(\alpha+1)
 +\kappa(1-|\alpha|)_+.
\]
For \(|\alpha|\geq1\), the first three terms equal \(K(\alpha)\), using
\(a\cosh^2(1)=A\) and \(b\cosh^2(1/2)=B\). Thus \(\widehat g\) vanishes there, including the endpoints. Pair-measure positivity and the known band prove (P). The \(O(x^{-2})\) decay permits these tests under the linear pair-mass bound used in Round 7.

Here is a closed finite expression for reproducing \(\mathcal B\). For each triple \((r,c,d)\) in \(\{(2,A,a),(1,-B,-b)\}\), define
\[
u=c-d(1/2+e^{-r}/4),\quad v=-de^{-r}/4,
\]
\[
I_-(r)=\frac{1-(1+r)e^{-r}}{r^2},\qquad
I_+(r)=\frac{(r-1)e^r+1}{r^2}.
\]
Then
\[
\boxed{\mathcal B=
\sum_{(r,c,d)}\{u(1+2I_-(r))+v(1+2I_+(r))\}
-\frac43\kappa-(A-B).}
\]
For the one-parameter correction \(f_c=\cos^2(\pi x)R+c\operatorname{sinc}^2(x)\), positivity at zero requires \(c\geq\kappa\). Since the bound decreases by \(4c/3\), the chosen correction is optimal **within this particular one-parameter family**, not among all minorants or point processes.

## 3. The obstruction is a genuine point process

On \(\mathbb Z\), take the determinantal process with kernel
\[
Q(j,k)=\int_{-1/4}^{1/4}e^{2\pi i(j-k)t}\,dt
=\begin{cases}1/2,&j=k,\\
\sin(\pi(j-k)/2)/(\pi(j-k)),&j\ne k.
\end{cases}
\]
This is the orthogonal projection onto a frequency interval of length \(1/2\), so it defines an actual determinantal probability measure; see [Lyons, *Determinantal probability measures*](https://www.numdam.org/articles/10.1007/s10240-003-0016-0/). If \(\mathcal X\subset\mathbb Z\) is its random occupied set and \(U\) is independently uniform on \([0,1)\), then
\[
\{(j+U)/2:j\in\mathcal X\}
\]
is a stationary, simple, unit-intensity point process on the line. Stationarity follows from integer-translation invariance of the discrete process and uniform random translation within one lattice cell.

Its Palm pair measure is exactly
\[
\mu_A=\delta_0+\frac12\sum_{k\ne0}
 \left(1-\operatorname{sinc}^2(k/2)\right)\delta_{k/2}.
\]
Indeed the discrete pair occupation probability is \(1/4-|Q(0,k)|^2\), and conditioning on the occupied point divides by \(Q(0,0)=1/2\). All pair weights are nonnegative. In particular, \(\mu_A([-R,R])\leq1+2R\), giving the required linear cumulative bound. The process has a hard core of one half.

Poisson summation gives its centered spectrum
\[
dS_A(\alpha)=\operatorname{dist}(\alpha,2\mathbb Z)\,d\alpha
 +\sum_{m\ne0}\delta_{2m}.
\]
Thus it has exactly the prescribed Montgomery data on \((-1,1)\), and satisfies spectral positivity, diagonal normalization, pair-measure positivity, simplicity, and the cumulative pair bound. The nonzero even-frequency atoms must be retained.

Its Poisson variance and two-scale statistic are
\[
V_A(r)=\frac{2\tanh(r/2)}{r^2}+\frac2{e^{2r}-1},
\]
\[
W_A=\frac{e^2}{4}+\frac5{4e^2}-e-\frac2e+\frac32
\in(0.06239,0.06240)<\frac1{16}.
\]
The exact constant enclosure is already certified in the frozen Round 7 artifact. No new decimal scan is needed. This gives the realizable obstruction to the proposed inference. It is not a construction of actual zeta zeros and is not claimed to satisfy every arithmetic identity known about zeta.

## 4. The remaining arithmetic obligation

For any fixed pair of positive smoothing scales, this same process remains compatible with the stated low-band and point-process assumptions. A statistic whose proved lower bound would exclude its value therefore cannot follow from those assumptions alone. Changing the scales may improve the size or shape of the target; it does not add the missing arithmetic information.

For the present scales, the unresolved requirement is an actual-zeta estimate for the signed out-of-band contribution
\[
\int_{|\alpha|\geq1}
 \left(Ae^{-2|\alpha|}-Be^{-|\alpha|}\right)dS_\zeta(\alpha),
\]
or its finite-height counterpart with controlled errors. The negative tail beyond \(\log(2\cosh1)\) prevents simply discarding the unknown part. The concrete arithmetic identity proposed for this contribution must be audited on its own; generic positivity and another random-matrix calculation cannot replace it.
