# Audit of the singular-series input to the signed main term

6 November 2026. This note audits the source of the singular-series mean used in MAIN_TERM_THEOREM.md. It does not prove the localized prime-pair discrepancy hypothesis.

## Source and exact scope

Fazzari–Gerspach, *The third moment of the logarithm of zeta*, arXiv:2412.20099v1, Lemma 2.7, equation (2.29), printed pp.17–18, states uniformly in y and n that
\[
\sum_{1\le h\le y}\mathfrak S_n(h)-y
=-\frac12\min\{\Lambda(n),\log y\}
+O((\log y)^{2/3}).
\]
Here the surrounding section takes n=q^a, a prime power. Its opening paragraph explicitly treats odd q>2 in the proofs and says the q=2 case follows by modification. Use y≥2, or write log(2y) in the error if the integration reaches bounded y.

This is an unconditional singular-series statement. The preceding Lemma 2.6 assumes RH, but Lemma 2.7 does not inherit that hypothesis implicitly: its proof invokes Friedlander–Goldston's unconditional singular-series mean. This is independent of the endpoint defect in the paper's Conjecture 1.8.

Primary sources:
- [FG Lemma 2.7](https://arxiv.org/pdf/2412.20099v1#page=17).
- [Friedlander–Goldston (1995), DOI 10.1215/ijm/1255986635](https://doi.org/10.1215/ijm/1255986635).
- [Author-uploaded copy](https://www.researchgate.net/publication/254209041_Some_singular_series_averages_and_the_distribution_of_Goldbach_numbers_in_short_intervals).

The FG v1 PDF text and its section context were read directly. The publisher's FG95 PDF endpoint returned a security interstitial in this audit; the author-uploaded text was readable. Its Proposition 1 includes an x≥r condition and discusses an extra factor for removing that restriction. Therefore one should not claim that an arbitrary-r uniform estimate was independently re-proved here.

## A separate prime-modulus check

Let S(h) denote the ordinary two-prime singular series, extended by zero to odd h. Write
\[
A(y)=\sum_{1\le h\le y}S(h).
\]
The ordinary Friedlander–Goldston estimate is
\[
A(y)=y-\tfrac12\log y+O((\log(2y))^{2/3})\quad(y\ge1).
\]
For an odd prime q define
\[
a_q=\frac{q-1}{q-2},\quad r_q=a_q-1=\frac1{q-2},\quad
B_q(y)=\sum_{\substack{h\le y\\q\nmid h}}S(h).
\]
Then the local factors give S_{q^a}(h)=a_q S(h)1_{q∤h}. Grouping h by its q-adic valuation gives the exact recurrence
\[
A(y)-A(y/q)=B_q(y)+r_q B_q(y/q).
\]
This uses S(q^v u)=a_q S(u) for q∤u and v≥1.

Put D_q(y)=a_qB_q(y)-y. For y≥q,
\[
D_q(y)=-\frac{a_q}{2}\log q-r_qD_q(y/q)
 +O((\log(2y))^{2/3}),
\]
where the coefficient of y cancels exactly:
\[
a_q(1-1/q)-1-r_q/q=0.
\]

If y<q, then B_q(y)=A(y), so
\[
D_q(y)=-\tfrac12\log y+O((\log(2y))^{2/3}),
\]
uniformly q≥5: the additional errors y/(q−2) and log(y)/(q−2) are bounded.

For q≤y<q², substitution of this base case yields
\[
D_q(y)+\tfrac12\log q
=-\frac{r_q}{2}\log(q^2/y)+O((\log(2y))^{2/3}),
\]
and r_q log q is uniformly bounded. For y≥q² the residual
D_q(y)+½log q recurs with multiplier −r_q. When q≥5, |r_q|≤1/3, so its error is bounded by a geometric series. This independently derives
\[
D_q(y)=-\tfrac12\min(\log q,\log y)
 +O((\log(2y))^{2/3})
\]
uniformly over odd primes q≥5 from the ordinary mean A(y). It avoids applying FG95 at an auxiliary argument y/q below q.

The q=3 recurrence has |r_q|=1, so this geometric-error proof does not establish the sharp cited q=3 remainder. The weaker argument below shows that this sharp fixed-prime remainder is unnecessary for the packet theorem.

## The q=2 case has an elementary reduction

For h odd, S_{2^a}(h)=S(2h), and for h even it is zero. Since S(4k)=S(2k),
\[
\sum_{h\le y}S_{2^a}(h)=A(2y)-A(y)
=y-\tfrac12\log2+O((\log(2y))^{2/3})
\]
for y≥2. This supplies the missing even-prime modification without introducing a new prime-pair hypothesis.

## A weaker q=3 bound is enough for the packet

At q=3 the exact recurrence and the ordinary singular-series mean give, for y≥3,
\[
D_3(y)=-\log3-D_3(y/3)+O((\log(2y))^{2/3}).
\]
Iterate until the argument lies in [1,3). There are O(log(2y)) steps, the terminal value is bounded, and the sum of absolute errors is
\[
\ll\sum_{0\le j\le\log_3 y}(\log(2y/3^j))^{2/3}
\ll(\log(2y))^{5/3}.
\]
The constant terms are bounded by an alternating geometric sum (even the cruder O(log y) bound suffices). Thus
\[
D_3(y)=O((\log(2y))^{5/3}).
\tag{A1}
\]
This is weaker than the cited sharp lemma but follows from the ordinary mean and the exact recurrence alone.

For the even Schwartz kernel K in MAIN_TERM_THEOREM.md, with integral zero, integration by parts now yields
\[
\sum_{h\ne0}\mathfrak S_{3^a}(h)K(h/H)
=-\frac2H\int_0^\infty D_3(y)K'(y/H)\,dy
=O_K((\log(2+H))^{5/3}).
\tag{A2}
\]
The extension for y<1 is bounded and causes no problem. All integrals converge by Schwartz decay.

The packet only contains n=3^a≥R=T^{\beta-\eta}, so
\[
\sum_{\substack{a\ge1\\3^a\ge R}}\frac1{3^a}=O(R^{-1}).
\]
Using (A2), the logarithmic x-integral O(L), and the factor L^{-3} in the main term, all such twists contribute
\[
O\big(T^{-(\beta-\eta)}L^{-1/3}\big)=o(1)
\]
to its linearized singular-series packet. The nonlinear replacement error was already controlled uniformly in n. Replacing these terms by the formal −log3 main expression changes the result by a still smaller power-saving quantity.

Consequently the packet theorem can be based on the independently derived uniform q≥5 estimate, the elementary q=2 reduction, and this weak q=3 bound. It does not need the unexpanded sharp q=3 case of FG Lemma 2.7. This does not amount to an independent proof of that sharper fixed-prime statement.

## Implication for the packet argument

The packet n≈T^β contains prime powers; the singular series depends on their underlying prime q. In the central contributing region the shift scale H≈T^(α+β−1) exceeds n≈T^β because α>1. The uniform version is nevertheless useful when smoothing through smaller h.

The critical point is the secondary logarithmic term, not merely the leading mean y. Replacing S_n by its mean loses exactly the signed signal the packet calculation is designed to retain. The audit supports using the cited lemma with its stated prime-power scope. It does not convert the unproved localized Λ-pair estimate into a theorem.
