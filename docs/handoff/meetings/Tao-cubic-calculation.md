# Removing the pair diagonals from the cubic trace

This companion calculation examines a static three-point test alongside the heat-flow question in the [discussion handout](Tao-ACUE-brief.md). Both are consequences of the finite determinantal formulas in [Tao’s 2019 note, Remarks 5–6](https://terrytao.wordpress.com/2019/05/08/the-alternative-hypothesis-for-unitary-matrices/).

Set $p_k=\sum_j e^{ik\theta_j}$ and let $a,b>0$ with $a+b<2N$. Denote by $D(a,b)$ the ordered sum of $e^{i(a\theta_i+b\theta_j-(a+b)\theta_k)}$ over pairwise distinct $i,j,k$. Inclusion–exclusion gives
$$
D(a,b)=p_a p_b\overline{p_{a+b}}-|p_{a+b}|^2-|p_a|^2-|p_b|^2+2N.
$$

For either projection ensemble expand its three-point determinant in Fourier modes from $I=\{0,\ldots,N-1\}$. Only the two three-cycles contribute, since none of the three frequencies is zero in the dual group. Each cycle counts the translates of a three-site pattern fitting into $I$. The two patterns agree up to reflection and translation. On the line the sites are $0,a,a+b$, giving $(N-a-b)_+$ translates. On the cycle of length $2N$ the gaps have lengths $a,b,2N-a-b$. Each gap $g>N$ allows $g-N$ translates, and at most one such gap exists. Thus
$$
\mathbb E_{\rm CUE}D=2(N-a-b)_+,\qquad
\mathbb E_{\rm ACUE}D=2\big[(N-a-b)_++(a-N)_++(b-N)_+\big].
$$

Take $10\mid N$. At $a=b=3N/5$ these expectations both vanish. The entire difference of the raw cubic comes from the pair observable at $2m$, with means $N$ in CUE and $2N-2m$ in ACUE. At $(a,b)=(11N/10,N/10)$ the factorial means divided by $N$ are instead zero in CUE and $1/5$ in ACUE. Even here the difference is expressible using the pair form factors: for $0<q<2N$ the CUE minus ACUE pair form-factor gap in unnormalized trace units is $(q-N)_+$. Thus a signal surviving removal of the repeated indices can still carry only a known numerical combination of pair predictions in these two models. For an arbitrary point process its pair function alone need not determine its third correlation.

A direct finite check enumerated all six permutations in the three-point determinant and all frequency assignments in $I^3$, testing exact integer conservation or conservation modulo $2N$ as appropriate. The two examples at $N=10$ gave ordered distinct sums $(0,0)$ and $(0,2)$ in CUE/ACUE order. The general expressions above follow from the interval counts.
