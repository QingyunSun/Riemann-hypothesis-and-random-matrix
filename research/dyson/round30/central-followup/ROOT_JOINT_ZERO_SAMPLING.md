# Sampling the actual central joint pairing at true zeta zeros

2026-09-08. Root derivation, prompted by the companion zero-norm sampling argument. This is an ordinary RH-dependent identity with a vanishing comparison error. It does not estimate the resulting signed zero sum and is not a Montgomery–Dyson pair-correlation theorem. Novelty is not assessed.

## Statement with the actual weights

Retain R29's exact compact prime-error extension f and its Mellin transform, the full sharp odd Möbius polynomial M_D, and the log cofactor polynomial B_K. Let X=T squared, D and K be comparable to T with fixed positive comparison constants, and ell=log T. Fix real w in C_c^1((a,b)) for constants 0<a<b. Put
\[
G(t)=w(t/T)\widehat f(t)M_D(t)B_K(t),\qquad
Z_w=\frac1{\pi X\ell^2}\int_{\mathbb R}G(t)\,dt.
\]
Under ordinary RH,
\[
\boxed{
Z_w=\frac{2}{X\ell^3}\sum_{\gamma>0}
w(\gamma/T)\widehat f(\gamma)M_D(\gamma)B_K(\gamma)
+O\!\left(\frac1{\log\log T}\right).}
\tag{1}
\]
The ordinates are those of the actual nontrivial zeros, counted with multiplicity. All coefficients on the right are exactly the original ones evaluated at the ordinate. No zero simplicity, random-matrix law, or pointwise smallness at a zero is assumed. Negative carrier windows follow by conjugation for real original profiles.

## Paying the variation of the full product

This requires more than a theorem for the separate norm of M_D. Remove the three common phases by defining
\[
F_0(t)=e^{it\log X}\widehat f(t),\quad
M_0(t)=D^{-it}M_D(t),\quad
B_0(t)=K^{-it}B_K(t).
\]
Then
\[
G(t)=w(t/T)e^{ict}F_0(t)M_0(t)B_0(t),
\qquad c=\log(DK/X)=O(1).
\tag{2}
\]
The large separate carrier derivatives cancel in the product because DK is comparable to X. This cancellation is explicitly retained.

On I=[aT,bT], the R29 energy and mean-value bounds give
\[
\|F_0\|_{L^2(I)}+\|F_0'\|_{L^2(I)}\ll\sqrt T\,\ell,
\qquad
\|M_0\|_{L^2(I)}+\|M_0'\|_{L^2(I)}\ll T,
\tag{3}
\]
and the sharp cofactor estimate gives
\[
\|B_0\|_{L^\infty(I)}+\|B_0'\|_{L^\infty(I)}\ll\sqrt T\,\ell.
\tag{4}
\]
Here is the justification for each derivative, rather than a generic assumption about an oscillatory kernel. The derivative of F_0 is -i times the phase-shifted Mellin transform of log(x/X)f(x). Multiplying the original compact profile by log(x/X) preserves its support and all required fixed-order bounds, so the same fixed-prime-variable Selberg estimate applies. The derivative of M_0 has coefficients i mu(d)log(d/D), bounded on the original sharp interval; Montgomery–Vaughan applies to these coefficients. The derivative of B_0 has the weight i log(k)log(k/K). This weight has supremum and total variation O(ell) on [K,2K]. Partial summation in the same second-derivative exponential-sum bound therefore proves (4), since t is comparable to T and K is comparable to T. Sharp endpoints are retained throughout.

Cauchy, (2)–(4), and the product rule now prove
\[
\int_I|G(t)|dt\ll T^2\ell^2,
\qquad
\int_I|G'(t)|dt\ll T^2\ell^2.
\tag{5}
\]
The derivative of w(t/T) is smaller by a factor T. Each of the other three product derivatives has the same upper bound by (3)–(4); the bounded phase c adds only a constant multiple of the first integral. No derivative of the arithmetic function Lambda(x+h) is taken.

## True zero counting and normalization

Let N(t) count zeros with multiplicity, let
\[
L(t)=\frac{t}{2\pi}\log\frac{t}{2\pi}-\frac{t}{2\pi}+\frac78,
\qquad R(t)=N(t)-L(t).
\]
The RH zero-counting discrepancy gives
\[
\sup_{t\in I}|R(t)|\ll\frac{\ell}{\log\log T}.
\tag{6}
\]
The primary input and one-sided ordinate convention are recorded in [the companion source review](zero-moment-review/ZERO_MOMENT_APPLICABILITY.md), which checks Carneiro–Chandee–Milinovich's RH bound for S(t). Only its order of growth is needed here.

Since G has compact support inside I, Stieltjes integration by parts is valid for this complex test and gives
\[
\sum_{\gamma>0}G(\gamma)
=\int_I G(t)L'(t)dt-\int_I R(t)G'(t)dt
=\frac{\ell}{2\pi}\int_I G(t)dt
+O\!\left(\frac{T^2\ell^3}{\log\log T}\right).
\tag{7}
\]
Replacing log(t/(2 pi)) by ell costs only O(T squared times ell squared), absorbed by the displayed error. Multiplying (7) by 2/(X ell cubed), with X=T squared, proves (1), including its factor 2.

## Exact remaining obstruction

Equation (1) pays the variation cost of the actual product, so a categorical claim that only a separate zero norm can be sampled would be too restrictive. Nevertheless its right side is still an actual signed joint correlation. The prime-error transform depends on the same zeta zeros through the explicit formula; it has not been replaced by its diagonal or by an independent random variable. The reciprocal zeta function has poles at zeros, not zeros there, and no factor on the right vanishes automatically.

The test depends on T and on the actual arithmetic extension. Thus (1) is not a new unweighted pair-correlation law, an AH contradiction, or an asymptotic evaluation of the central block. A separate inequality for this exact joint zero sum would be needed to improve the central estimate. The other height, factor and shift packets, and the global threshold liminf Z_T < A-2M, would still have to be paid. This note records a verified comparison step and the limit of the attempted route.
