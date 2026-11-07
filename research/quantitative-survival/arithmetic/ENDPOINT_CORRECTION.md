# Endpoint correction to a cited two-sign prime-pair formulation

6 November 2026. Independently checked against the rendered original PDF, printed page 7, Conjecture 1.8 of Fazzari–Gerspach, *The third moment of the logarithm of zeta and a twisted pair correlation conjecture*, arXiv:2412.20099v1. [Primary PDF, page 7](https://arxiv.org/pdf/2412.20099v1#page=7)

## What is printed, and the exact endpoint check

The displayed formula uses the same main term for both signs:

\[
\sum_{m\le x}\Lambda(m/n)\Lambda(m\pm h)
=\frac{\mathfrak S_n(h)}n x+O_\varepsilon(x^{1/2+\varepsilon}),
\qquad 1\le h,n\le x^{1-\varepsilon}.
\tag{1}
\]

This is visible in the original PDF, not an OCR substitution. Under the usual convention that the von Mangoldt function vanishes away from positive prime powers, set \(n=1\) and define

\[
A_+(x,h)=\sum_{1\le m\le x}\Lambda(m)\Lambda(m+h),\qquad
A_-(x,h)=\sum_{h<m\le x}\Lambda(m)\Lambda(m-h).
\]

Changing variables gives the exact identity

\[
A_-(x,h)=A_+(x-h,h).
\tag{2}
\]

Choose \(\varepsilon=1/10\), and take an even integer \(h\sim x^{3/4}\). Both \(h\le x^{9/10}\) and \(h\le(x-h)^{9/10}\) hold for large \(x\). Applying the two printed estimates to (2) would force

\[
\mathfrak S(h)h=O(x^{3/5}).
\]

For even \(h\), the singular series defined immediately above (1) is bounded below by the fixed positive twin-prime constant \(2\prod_{p>2}(1-(p-1)^{-2})\). Thus the left side is bounded below by a positive constant times \(x^{3/4}\), a contradiction.

The two signs cannot simultaneously have the printed common main term throughout that stated range. A source interpretation using an unstated even extension of \(\Lambda\) to negative integers would change the sum and would not be the conventional prime-pair assertion; our work uses only positive prime powers.

## Consistent formulation and relevance to our packet

The ordinary endpoint-aware main term for a signed shift \(h\) is

\[
\frac{\mathfrak S_n(h)}n\,(x-\max(0,-h))_+.
\tag{3}
\]

In particular the minus-sign main term at \(n=1\) is \(\mathfrak S(h)(x-h)_+\). This restores consistency with the exact identity. No claim is made here that the square-root remainder in this repaired global formulation is proved, or that every theorem in the cited paper has now been checked with it.

For our near-product packet the needed scales are

\[
x\asymp X,\qquad |h|\asymp X/T,\qquad
X\le T^{1.4+\eta},\quad \eta<.05.
\]

They satisfy \(X/T\ll X^{1/2}\) with a fixed power margin. Even allowing a small power enlargement of the effective shift range preserves this inequality. The endpoint difference is at most \(\mathfrak S_n(h)|h|/n\), which is absorbed by a localized \(O_\varepsilon(X^{1/2+\varepsilon})\) discrepancy bound. On the actual integration region \(x\asymp X\gg |h|\), the derivative of (3) is exactly \(\mathfrak S_n(h)/n\), so the partial-summation main integral is unchanged.

Accordingly, `CONDITIONAL_NEXT.md` now defines discrepancy against (3) and assumes a consistent **independent local estimate** only on the needed near shifts. It does not adopt the full printed assertion (1). The conditional error exponent and the unevaluated signed singular-series main term are unchanged.

## Scope of this correction

This is an endpoint defect in a particular written uniform two-sign formulation. It is **not a refutation of the Hardy–Littlewood prime-pair conjecture**, not a new prime-distribution result, and not a claim that the paper's intended conditional conclusions are false. The correction removes an inconsistent premise from our own research notes and makes their remaining assumptions explicit.

Updated companion files: `REPORT.md` and `CONDITIONAL_NEXT.md`.
