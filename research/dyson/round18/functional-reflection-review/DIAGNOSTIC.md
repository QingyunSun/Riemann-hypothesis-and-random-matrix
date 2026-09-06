# Independent functional-reflection diagnostic

Date: 2026-09-05. Reviewer: Aquinas. The initial diagnostic was derived independently before reading the R18 author formula; the far-line subsection records the later independent check of the coordinator's proposal. It is an ordinary analytic check, not a claim of a new zeta estimate. The inherited quadratic packet is the frozen R17 report, SHA-256 `a7b5290a3d96d2590da42f3fe13a53c1e02499b53d066366824b9f15883a7da3`. The final coordinator proof is `research-round18/root-contour-proof/ROOT_INFINITE_CONTOUR_TRACE.md`, SHA-256 `58e103d3a5235138d1017f20577ddfae8f6f465e56298f55fd7be70c4ff79e2b`.

## 1. Functional equation and the artificial pole at zero

Use the [NIST DLMF functional equation, 25.4.2](https://dlmf.nist.gov/25.4#E2),
\[
\zeta(z)=\chi(z)\zeta(1-z),\qquad
\chi(z)=2(2\pi)^{z-1}\sin(\pi z/2)\Gamma(1-z).
\]
Put \(H=-\zeta'/\zeta\), \(A=-\chi'/\chi\). Logarithmic differentiation gives the exact meromorphic identity
\[
H(z)=A(z)-H(1-z).
\tag{D1}
\]
The minus sign in front of the second H matters.

The elementary expansions of sine, gamma, and the zeta pole give
\[
\chi(z)=\frac z2[1+(\log(2\pi)+\gamma_0)z+O(z^2)],
\]
\[
A(z)=-\frac1z-\log(2\pi)-\gamma_0+O(z),\qquad
H(1-z)=-\frac1z-\gamma_0+O(z).
\]
Their difference is regular at zero and has value \(H(0)=-\log(2\pi)\). Thus a pole in either separate term at zero is not a pole of the original reflected H.

Fix \(1/2<\sigma<1\), \(a=1-\sigma\), and the R17 weight
\[
w(t)=\frac{(t^2+a^2)^2}{W^4}\operatorname{sinc}(t/(2W))^6.
\]
After setting \(z=2\sigma-s\), the two unsigned terms
\[
H(s)A(2\sigma-s),\qquad H(s)H(s+1-2\sigma)
\]
each have residue \(+H(2\sigma)\) at \(s=2\sigma\). With the carrier and packet, the common residue is
\[
\boxed{H(2\sigma)X^\sigma w(-i\sigma).}
\tag{D2}
\]
They occur with opposite signs in (D1), so these artificial residues cancel. They are individually nonzero:
\[
w(-i\sigma)=\frac{(1-2\sigma)^2}{W^4}
\left(\frac{\sinh(\sigma/(2W))}{\sigma/(2W)}\right)^6>0,
\]
and \(H(2\sigma)>0\) by its absolutely convergent prime series. This value is not the packet's value at either of its zeros \(\pm ia\). If \(\delta=\sigma-1/2\), the polynomial multiplier is \(4\delta^2/W^4\).

Any calculation that shifts the separate gamma and arithmetic terms across \(s=2\sigma\) must retain both residues. Keeping just one creates a spurious main term. Shifting their combined original reflected factor crosses no pole at this point.

## 2. First genuine reflected trivial pole

At \(z=-2\), chi has a simple zero, so \(A(z)=-1/(z+2)+O(1)\). The other term \(H(1-z)=H(3)+O(z+2)\) is regular. Therefore \(s=2\sigma+2\) is a genuine reflected pole, with full residue
\[
\boxed{H(2\sigma+2)X^{\sigma+2}w(-i(\sigma+2)).}
\tag{D3}
\]
It is not canceled by the transformed H term. All factors in (D3) are positive real numbers for the stated parameters. With the R17 upward-line convention, crossing it contributes minus \(2\pi\) times this residue to the real-t integral. A line \(2\sigma<c<2\sigma+2\) avoids this first trivial pole; a farther shift cannot omit it.

## 3. What simultaneous arithmetic expansion actually produces

On \(\Re s=c>2\sigma\), both H factors in
\(H(s)H(s+1-2\sigma)\) have absolutely convergent Dirichlet series. Their coefficient is
\[
C_\sigma(k)=\sum_{mn=k}\Lambda(m)\Lambda(n)n^{2\sigma-1},
\tag{D4}
\]
not \(\Lambda(k)^2\) and not the unweighted convolution from R17. It is nonnegative and starts at \(k=4\). The same entire-weight transform then yields the finite arithmetic term
\[
2\pi W\sum_{Xe^{-3/W}<k<Xe^{3/W}}
C_\sigma(k)k^{-\sigma}K_{2,a/W}(W\log(k/X)).
\tag{D5}
\]
In the functional decomposition this term is subtracted. Its Fourier kernel remains signed. At \(X=1\), \(W\ge3\), (D5) is empty, just as in R17.

Taking \(2\sigma<c<2\sigma+2\) leaves a gamma-weighted linear H integral and the reflected nontrivial-zero residue sum. If \(\mathcal G_c\) denotes the upward-c-line gamma term with all carrier/packet factors, and \(\mathcal P\) denotes (D5), the schematic exact identity, with the R17 normalization, is
\[
\mathcal I_\sigma(X)=\mathcal G_c(X)-\mathcal P_\sigma(X)
-2\pi\sum_{\rho\ \mathrm{distinct}}\mathcal R_\rho(X),
\tag{D6}
\]
\[
\mathcal R_\rho(X)=m_\rho H(2\sigma-\rho)
X^{\sigma-\rho}w(-i(\sigma-\rho)).
\]
The sum counts distinct zeros because multiplicity already appears in its summand. The contour and residue convergence are those checked in R17, with the additional artificial-pole cancellation at (D2). The two prime expansions are legal on the far line; they do not delete the remaining gamma integral or reflected-zero sum.

This is a valid alternate arithmetic representation. Without further work on the remaining terms, it supplies no independent upper bound on the original positive energy. In particular, an empty finite product sum at carrier one does not imply an empty energy. The far-line argument below does eliminate the gamma integral exactly; the unknown quadratic information then remains entirely in the nontrivial-zero residue sum.

### A separately checked far-line closure

After the finite-c diagnostic above, the coordinator supplied a candidate limit through the lines
\[
c_N=2\sigma+2N+1,\qquad d_N=c_N-\sigma.
\]
I independently checked its uniform line estimate as follows. The reflected argument is \(-2N-1-it\). In the sine/gamma form of the functional equation, its cotangent is bounded in modulus by one, while the digamma argument has real part \(2N+2\). Consequently
\[
H(-2N-1-it)\ll\log(c_N+|t|+2),\qquad
H(c_N+it)\ll2^{-c_N},
\]
with absolute constants for these lines. The second estimate follows directly from the absolutely convergent prime series, by extracting \(2^{-c_N}\) and comparing the remaining sum with its value at exponent two.

For \(d\ge1\), \(a<1/2\), the elementary inequalities
\(\lvert\sin((t-id)/(2W))\rvert\le e^{d/(2W)}\) and
\(\lvert(t-id)^2+a^2\rvert\le t^2+d^2+a^2\) give the explicit majorant
\[
\boxed{|w(t-id)|\le
100W^2\frac{e^{3d/W}}{t^2+d^2}.}
\tag{D6a}
\]
Scaling \(t=du\) bounds the remaining logarithmic integral by
\[
\int_{\mathbb R}\frac{\log(c_N+|t|+2)}{t^2+d_N^2}dt
\ll\frac{\log(c_N+2)}{c_N}.
\]
At \(X=1\), the entire final vertical integral is therefore
\[
\ll W^2\exp[-c_N(\log2-3/W)]
\frac{\log(c_N+2)}{c_N}\longrightarrow0
\]
whenever \(W>3/\log2\). This condition is stronger than the empty-convolution condition \(W>3/\log4\). They must not be interchanged.

For each fixed N, take the horizontal-height limits first. Then send N to infinity. The contour crosses the first N reflected trivial zeros, in addition to the nontrivial line already present in R17. The resulting exact trace is
\[
\boxed{\mathcal E_{\sigma,W}=-2\pi\left[
\sum_{\rho\ \mathrm{distinct}}\mathcal R_\rho(1)
+\sum_{k\ge1}H(2\sigma+2k)w(-i(\sigma+2k))\right].}
\tag{D6b}
\]
The trivial-zero summands are positive. Their series converges for the same strict W condition, and satisfies the stronger useful estimate
\[
0<\sum_{k\ge1}H(2\sigma+2k)w(-i(\sigma+2k))
\ll W^{-4},\qquad W\ge6,
\]
uniformly for \(1/2<\sigma<1\). Indeed its kth summand is at most
\[
C W^{-4}(k+1)^4e^{-(2\log2-1)k},
\]
using \(H(2\sigma+2k)\ll2^{-2\sigma-2k}\) and
\(\operatorname{sinhc}(y)\le e^y\). This gives both absolute convergence and the claimed sigma-uniform trivial-tail bound. It gives no sigma-uniform bound for the nontrivial-zero sum.

Thus the gamma term can be replaced by an explicit small positive trivial-zero correction. This is a sharper exact representation than the finite-c form (D6). The nontrivial reflected sum still carries the unknown positive energy, as the following fixed-zero calculation demonstrates.

## 4. A fixed-zero diagnostic showing where the quadratic information remains

The reflected residues visibly retain the local squared zero signal. Fix a distinct nontrivial zero \(\rho=1/2+i\gamma\) of multiplicity m, assume RH, take \(X=1\), and choose a fixed \(W\ge\max(6,|\gamma|)\). This ensures \(w_{a=1/2,W}(\gamma)>0\), since its real sinc argument has magnitude at most one half, and also lies in the range of the closed trace above.

Let \(\delta=\sigma-1/2\downarrow0\), while keeping this zero and W fixed. The conjugate zero has the same multiplicity and
\[
H(2\sigma-\rho)=H(\overline\rho+2\delta)
=-\frac m{2\delta}+O_\rho(1).
\]
Analytic dependence of the packet gives
\[
\boxed{\mathcal R_\rho(1)
=-\frac{m^2}{2\delta}w_{1/2,W}(\gamma)+O_{\rho,W}(1).}
\tag{D7}
\]
In particular the real leading term is negative. Its contour contribution is
\[
-2\pi\mathcal R_\rho(1)
=\frac{\pi m^2}{\delta}w_{1/2,W}(\gamma)+O_{\rho,W}(1).
\tag{D8}
\]

This is exactly the leading local modulus-energy singularity. Indeed near the conjugate zero on the original line,
\[
H(\sigma+i(-\gamma+v))=-\frac m{\delta+iv}+O_\rho(1).
\]
For a sufficiently small fixed neighborhood of \(v=0\), rescaling the squared pole and bounding the analytic cross term gives
\[
\delta\int_{|t+\gamma|<r}|H(\sigma+it)|^2w_{a,W}(t)dt
\longrightarrow\pi m^2w_{1/2,W}(\gamma).
\tag{D9}
\]
The cross term is at most logarithmic before multiplication by delta, so it does not affect this limit. The residue correction thus retains, rather than removes, the quadratic multiplicity and local zero-energy information already present in the centered pair identity.

This is deliberately a **fixed-zero** diagnostic. It does not pass a delta limit through the infinite residue sum, assert a uniform estimate at \(\delta\asymp1/\log T\), or prove a new pair-correlation theorem. It is enough to disallow treating the reflected-zero term as a uniformly negligible gamma correction. For nontrivial carriers, the additional phase \(e^{-i\gamma\log X}\) also prevents an automatic termwise positivity assertion about the conjugate-pair residue contribution.

## 5. Source and scope record

The NIST primary page was inspected using the web tool, including equation 25.4.2. A separate attempt to save its raw TeX endpoint returned HTTP 403; no downloaded primary-byte hash is claimed. The displayed functional equation above is a mathematical transcription, not a purported raw source file. All expansions, residue calculations, and the fixed-zero diagnostic in this note are independently derived.

This note establishes exact cancellations and identifies the surviving information. It does not prove that no stronger use of the functional equation can ever work. The needed additional work remains a quantified estimate for the genuine centered energy or the full signed reflected sum that reaches the R16 Bragg target. The final source-and-formula review of the frozen R18 author text is recorded separately in `INDEPENDENT_FUNCTIONAL_REVIEW.md`.
