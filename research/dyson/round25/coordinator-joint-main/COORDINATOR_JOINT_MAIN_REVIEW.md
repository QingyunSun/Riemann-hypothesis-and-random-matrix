# Independent coordinator review of the R25 joint main cancellation

Status: complete ordinary mathematical review of the full author manuscript; no formal verification, numerical asymptotic validation, novelty assessment, or global covariance bound is claimed.

## Reviewed object and scope

I read all eight sections of Euclid's `research-round25/joint-main-cancellation/JOINT_MAIN_CANCELLATION.md`, supplied as 19,377 bytes with SHA-256 `6995e95c0bf3bd0ba606385f1ee50d23f23d238fccf655f96c93230a7d856d03` under the standalone ACUE-Astra handoff directory. The receipt accompanying this review checks those bytes and freezes the reviewed copy. I have not yet read Plato's completed independent review, and this review does not rely on its reported acceptance. I did not run the finite checker or audit its code.

The accepted statement is the manuscript's fixed compact packet theorem under ordinary RH:

\[
\mathcal P=\mathcal Z_Q^{(2)}+o(1),\qquad
Q=X^{2/5},\quad X=T^\alpha,\quad 7/4\le\alpha\le9/4.
\]

The cutoffs are fixed smooth functions of `m/X` and `h/H`, supported away from zero, with `H=X/T`. The exact Pareto weight, both von Mangoldt factors, the sharp complementary divisor cutoff, and the parity center 2 are retained. This is not yet a reduction over all physical shift lengths. Constants depend on the fixed profiles; no growing family can be summed merely from uniformity in alpha.

## Checks of the full argument

1. **Exact decomposition.** The primitive/nonprimitive split in (8)-(10) agrees with the divisor identity for Lambda. The principal for d=1 is retained even though its discrepancy is zero. Complementary factors are not incorrectly required to be coprime.

2. **Actual derivative scales and completion.** The integral formula for b_T in (11) puts the T dependence in a beta-type probability mass and gives fixed-order derivatives at scale m, without a lost power of T. Differentiating the actual Pareto factor after scaling m=Xv, h=Hz gives uniformly bounded fixed derivatives. At fixed n the shifted weight has h-scale H. Poisson summation on period 2d, using J+1 derivatives, gives the claimed power saving; Q<H has a fixed margin throughout the stated parameter range. The discrepancy and primitive mask errors tend to zero for Q=X^(2/5), J=16.

3. **Exact prime-power count.** The count in (14) is valid without H much larger than p. Write a=H/(2p). For 0<a<1/2 there are no positive integers in (a,2a); for 1/2<=a<1 there is at most one, which is at most 2a; for a>=1 the count is at most a+1<=2a. Thus the count is always at most H/p. Together with p|h, at most two powers per odd prime in (X,3X), and the divisor bound, this proves (15). This supersedes my earlier caution based on an older coarse H/p+1 draft. The exact positive-integer count also works when such a p arises from a complementary cofactor, provided the other hypotheses establishing p|h and the relevant prime-power range are present.

4. **Principal mask removal.** The mean after h-completion contains the n-unit mask. The manuscript removes it separately, charges the prime powers p^j with j>=2, and retains the 1/d weight. The bound (18) follows with fixed logarithmic factors; it does not assume distribution in arithmetic progressions.

5. **Flat complementary center.** Centering the complementary term at 2 completes only the even h lattice. It therefore avoids the earlier K/H restriction from a primitive-k center. The odd r lattice in (22) genuinely supplies the extra d/X saving by two derivatives. An estimate using variation alone would not justify (23), but that is not the estimate used here.

6. **Möbius normalization and RH centering.** Equations (24)-(31) agree with the independent coordinator lemma previously submitted. The odd Dirichlet series has value 0 and derivative +2 at s=1; hence the truncated logarithmic coefficient tends to +2. Q is held fixed during differentiation in m. The error is paired with the centered odd-prime measure, whose continuous density is 1. The omitted powers of 2 do not change that density. Abel summation yields the product `(H/sqrt(X))*Q^(-1/2+epsilon)*log(X)`, rather than the generally too large absolute main term. The exponent conditions have strict margins.

7. **Both singular-series marginals.** The real hinge sum is sufficient for the compact packet estimate. Since f and its derivatives vanish at both support endpoints, the linear term and the log(H) multiple of the linear term integrate to zero against f''. Applying this independently to F(m,h) and F(n-h,h) retains the shifted endpoint correctly. The final odd-m lattice completion has the factor 2 in (38), so all three large terms in (32) cancel the corresponding terms in (37).

8. **Parameter ledger.** The worst exponents in (40) agree with the stated alpha interval: discrepancy 2/35; Q/H margin 1/35; cofactor-grid saving 29/45; RH centered saving 158/1125; nonprimitive saving 391/900. The fixed logarithms do not consume those positive margins. All estimates are for finite arithmetic sums before any later all-shift assembly.

Conclusion: I find no mathematical gap in this fixed-profile RH reduction. Its useful new content for the current programme is the removal of the joint one-prime mains, including the central scale X=T^2. The genuinely signed covariance Z remains unbounded at the needed fluctuation scale.

## Source-backed R26 refinement: retain the first correction

I independently reopened Montgomery--Soundararajan, *Primes in short intervals*, arXiv:math/0409258v1, and checked the statement of (47) on printed page 16, together with (16) on printed page 4 and the definition of B. These are unconditional singular-series statements, not the paper's conjectural prime-pair hypothesis. Source: <https://arxiv.org/pdf/math/0409258v1>.

Let

\[
B_2(y)=\sum_{h\ge1,\ h\text{ even}}(y-h)_+[\mathfrak S(h)-2].
\]

The stronger input yields, for fixed epsilon in (0,1/2),

\[
B_2(y)=-\tfrac12y\log y+c_2y+O_\epsilon(y^{1/2+\epsilon}),\quad y\ge1,
\qquad c_2=\frac{3-\gamma-\log(2\pi)}2.
\]

Here is a direct check of the otherwise potentially hidden real-endpoint and parity terms. The singular-series hinge is piecewise linear between consecutive integers. Linear interpolation of the smooth polynomial/logarithmic main term in (47) costs O(1), because its second derivative is bounded for y>=1. For delta={y/2},

\[
2\sum_{h\text{ even}}(y-h)_+
=\frac{y^2}{2}-y+2\delta(1-\delta).
\]

Subtracting this exact even-lattice baseline from half of (47) gives the displayed c_2 and a bounded periodic remainder, absorbed by the stated error. The linear coefficient will cancel for the compact weights below, but recording it avoids disguising endpoint terms.

For every f in C_c^2((1,infinity)), the exact hinge identity and two integrations by parts now give

\[
\boxed{\sum_{h\text{ even}}[\mathfrak S(h)-2]f(h)
=-\frac12\int_0^\infty\frac{f(y)}y\,dy
+O_\epsilon\!\left(\int_0^\infty y^{1/2+\epsilon}|f''(y)|\,dy\right).}
\]

This does not differentiate an O-term. It integrates the bounded remainder against f''. Both boundary terms vanish, and `(y log y)''=1/y`. For f supported in (Y,2Y), Y>=1, amplitude A_f and two derivatives bounded by A_f*Y^(-j), the remainder is O_epsilon(A_f*Y^(-1/2+epsilon)). The leading integral is typically of order A_f and must be retained when summing many packets. The error, in contrast, is geometrically summable over dyadic Y once those actual derivative bounds and all other arithmetic debts have been established. Near-zero packets require their own endpoint treatment.

### Sign diagnostic for the two marginals

For a compact packet set `K_-(m)=int F(m,h)/h dh` and `K_+(n)=int F(n-h,h)/h dh`. The leading correction to the manuscript's flat approximation to M_S is exactly

\[
-\sum_{m\text{ odd}}\Lambda(m)K_-(m)
-\sum_{n\text{ odd}}\Lambda(n)K_+(n)
+2\sum_{m\text{ odd}}K_-(m).
\]

Thus, if the appropriate global PNT and partition errors are separately justified, these three terms have continuum combination `-int K_-(m) dm`: each prime-weighted sum has density 1 and the final odd integer sum has density 1/2. Since P subtracts M_S, the induced correction in P-Z would have the **positive** sign. This is a sign check on the algebra, not a claim that the required global interchange, all-shift completion, small-length estimates, or identification with any earlier constant M has been proved.

The remaining work is precisely the variable-length partition with summable constants, the small- and large-shift tails, and an actual bound on the resulting signed covariance. No further exact-zero-margin finite-window profile search is suggested.
