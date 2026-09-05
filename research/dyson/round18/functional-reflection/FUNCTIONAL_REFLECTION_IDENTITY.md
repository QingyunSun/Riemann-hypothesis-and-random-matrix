# Functional reflection: finite prime products, an explicit gamma term, and a closed energy trace

Date: 2026-09-05. Status: ordinary analytic derivation submitted for independent review. No numerical experiment or parameter scan is used. The functional equation does allow two convergent prime factors after reflection, but it creates a compensating real pole and retains the quadratic nontrivial-zero residues.

There is a concrete further result at carrier X=1: the gamma contribution becomes an explicit **negative** prime series of size O(W⁻⁴), and the contour closes to an exact energy trace over all reflected zeros. This evaluates the gamma term but does not estimate the remaining nontrivial-zero sum. At carrier X=T² the closure fails and that simplification cannot be imported. No strict Bragg bound or famous conjecture is proved.

## 1. Setup and the functional equation

Assume RH and fix 1/2<σ<1, a=1−σ, δ=σ−1/2, W≥1 and X>0. Retain the R17 packet
\[
w(t)=\frac{(t^2+a^2)^2}{W^4}
\left(\frac{\sin(t/(2W))}{t/(2W)}\right)^6,
\quad H(s)=-\zeta'(s)/\zeta(s),\quad b=a/W.
\tag{1}
\]
Let B₆ be the six-uniform density from that report and
\[
K_b=(\partial_y^2-b^2)^2B_6,\qquad
\widehat w(\lambda)=2\pi W K_b(W\lambda),\qquad
\operatorname{supp}K_b\subset[-3,3].
\tag{2}
\]
Fourier convention: \(\widehat w(\lambda)=\int w(t)e^{-it\lambda}dt\). The packet is nonnegative on the real axis, has double zeros at ±ia, and has inverse-square decay on every fixed horizontal translate.

Write the zeta functional equation as
\[
\zeta(z)=\chi_\zeta(z)\zeta(1-z),\qquad
\chi_\zeta(z)=\pi^{z-1/2}\frac{\Gamma((1-z)/2)}{\Gamma(z/2)}.
\]
Define the explicit gamma factor
\[
A(z)=-\chi_\zeta'(z)/\chi_\zeta(z)
=-\log\pi+\frac12\frac{\Gamma'}{\Gamma}(z/2)
+\frac12\frac{\Gamma'}{\Gamma}((1-z)/2).
\tag{3}
\]
Then, as a meromorphic identity,
\[
\boxed{H(z)=A(z)-H(1-z).}
\tag{4}
\]
The minus sign matters. This changes the obstruction in R17: although the two *original* reflected factors cannot simultaneously have convergent prime series, the transformed pair can.

Choose a finite line
\[
2\sigma<c<2\sigma+1,
\qquad d=c-\sigma.
\tag{5}
\]
This lies below the first reflected trivial pole 2σ+2 and to the right of the nontrivial reflected line 2σ−1/2. On this line both H(s) and H(s+1−2σ) have absolutely convergent Dirichlet series.

## 2. Exact finite product and the retained residues

Define
\[
C_\sigma(n)=\sum_{uv=n}\Lambda(u)\Lambda(v)v^{2\sigma-1},
\]
\[
\mathcal P_{\sigma,W}(X)=2\pi W
\sum_{Xe^{-3/W}<n<Xe^{3/W}}
 C_\sigma(n)n^{-\sigma}K_b(W\log(n/X)).
\tag{6}
\]
The sum is finite, includes every prime power, and starts at n=4. It is different from the unweighted Λ*Λ of R17. Its coefficients are nonnegative, but K_b is signed; for example K_b(1)<0.

Let
\[
\mathcal I_\sigma(X)=\int|H(\sigma+it)|^2X^{it}w(t)dt,
\]
\[
\mathcal G_c(X)=X^d\int H(c+it)A(2\sigma-c-it)
 X^{it}w(t-id)dt.
\tag{7}
\]
The first integral is real by conjugacy, but is positive energy only for X=1; for general X it is a cosine-weighted signed integral.

For a **distinct** nontrivial zero ρ, let mρ be its multiplicity, and put
\[
\mathcal R_\rho(X)=m_\rho H(2\sigma-\rho)
 X^{\sigma-\rho}w(-i(\sigma-\rho)),
\quad \mathcal R(X)=\sum_{\rho\ \mathrm{distinct}}\mathcal R_\rho(X).
\tag{8}
\]
Each multiplicity is inserted once. For fixed parameters this series converges absolutely, as in R17: the packet decays quadratically in the ordinate and the remaining factors have logarithmic growth. Individual terms may vanish accidentally if H(2σ−ρ)=0; the packet itself does not cancel the reflected zero line.

The exact transformed formula is
\[
\boxed{\mathcal I_\sigma(X)
=\mathcal G_c(X)-\mathcal P_{\sigma,W}(X)-2\pi\mathcal R(X).}
\tag{9}
\]
Indeed the reflected contour from σ to c crosses the nontrivial reflected-zero poles, with residues (8). The pole of H(s) at one is canceled by w; the reflected real pole at 2σ−1 lies left of σ and is also canceled by the packet. Reflected trivial poles at 2σ+2k, k≥1, lie beyond c. Applying (4) on the c-line gives (9), and expanding the two convergent factors yields (6) using the R17 Fourier shift. Both arithmetic factors are expanded only on the c-line, where Fubini is valid.

### The new real pole at s=2σ cancels between the split terms

The original reflected factor is regular at z=0. With γ₀ Euler's constant,
\[
A(z)=-1/z-\log(2\pi)-\gamma_0+O(z),
\quad H(1-z)=-1/z-\gamma_0+O(z),
\]
\[
H(z)=A(z)-H(1-z)=-\log(2\pi)+O(z).
\tag{10}
\]
Thus the two unsigned split products H(s)A(2σ−s) and H(s)H(s+1−2σ) each have residue +H(2σ) at s=2σ. After the carrier and weight are included their common residue is
\[
\boxed{\mathcal B(X)=H(2\sigma)X^\sigma w(-i\sigma),}
\]
\[
w(-i\sigma)=\frac{(1-2\sigma)^2}{W^4}
\left(\frac{\sinh(\sigma/(2W))}{\sigma/(2W)}\right)^6>0.
\tag{11}
\]
This is not a packet zero. The two residues cancel in the difference (4), so s=2σ is not a pole of the original reflected product.

If \(\mathcal G_\sigma(X)=\int H(\sigma+it)A(\sigma-it)X^{it}w(t)dt\), shifting only the gamma product gives
\[
\mathcal G_c(X)=\mathcal G_\sigma(X)+2\pi\mathcal B(X).
\tag{12}
\]
The transformed prime product acquires the same real-pole correction when moved back left, as well as the reflected nontrivial residues. Deleting the term (11) in only one of these operations creates a false main term.

## 3. An explicit single-prime representation of the gamma contribution

The digamma recurrence isolates that pole:
\[
A(2\sigma-s)=\frac1{s-2\sigma}+\widetilde G_\sigma(s),
\]
\[
\widetilde G_\sigma(s)=-\log\pi
+\frac12\frac{\Gamma'}{\Gamma}(1+\sigma-s/2)
+\frac12\frac{\Gamma'}{\Gamma}((1-2\sigma+s)/2).
\tag{13}
\]
The latter is analytic throughout σ≤Re(s)<2σ+2; its nearest poles are s=2σ−1 to the left and s=2σ+2 to the right. Its product with H has the canceled pole at one but no others in that strip under RH.

The rational contribution on the c-line is exactly the following finite single-prime-power sum. Write l=Xe^{−3/W}, U=Xe^{3/W}. Then
\[
\boxed{\mathcal Q_{\sigma,W}(X)=2\pi W
\sum_{2\le n<U}\Lambda(n)n^{-2\sigma}
\int_{\max(n,l)}^U u^{\sigma-1}K_b(W\log(u/X))du.}
\tag{14}
\]
An empty inner interval contributes zero. To derive it, use
\((s-2\sigma)^{-1}=\int_1^\infty v^{2\sigma-s-1}dv\) on c>2σ, expand H there, and apply the compact packet transform at nv. Substitution u=nv gives n^{−2σ} exactly. Fubini holds before compact support is used.

For the remaining part define the actual **linear** packet
\[
\mathcal L(Y)=\int H(\sigma+it)Y^{it}w(t)dt
=2\pi W\sum_{Ye^{-3/W}<n<Ye^{3/W}}
\Lambda(n)n^{-\sigma}K_b(W\log(n/Y)).
\tag{15}
\]
Its equality is the one-contour linear argument; the double zero of w also cancels a simple pole. It holds for every Y>0. It is a finite sum for each fixed Y, not a common finite sum for all Y.

Using the standard convergent digamma integral on the σ-line, where both arguments in (13) have positive real parts, gives
\[
\boxed{\begin{split}
\widetilde{\mathcal G}_\sigma(X)={}&-(\log\pi+\gamma_0)\mathcal L(X)\\
&+\frac12\int_0^\infty
\frac{2e^{-u}\mathcal L(X)
-e^{-(1+\sigma/2)u}\mathcal L(Xe^{u/2})
-e^{-au/2}\mathcal L(Xe^{-u/2})}{1-e^{-u}}du.
\end{split}}
\tag{16}
\]
Consequently \(\mathcal G_c=\mathcal Q_{\sigma,W}+\widetilde{\mathcal G}_\sigma\). Equations (9), (14) and (16) are a fully specified arithmetic-plus-residue formula: a finite prime product, a finite rational prime term, a convergent scale integral of linear prime packets, and the nontrivial-zero sum.

The numerator in (16) must be kept combined near u=0. Its constant term cancels. Formula (15), the Lipschitz compact spline K_b and its zero endpoint values make L(Y) locally Lipschitz in log Y, so that numerator is O(u). At infinity, \(|\mathcal L(Y)|\le\int|H(\sigma+it)|w(t)dt\) uniformly in Y, and the exponential coefficients are integrable because a>0. A rigorous interchange first truncates u away from zero; the truncated digamma integrals are bounded uniformly by Oσ(log(|t|+2)), using the elementary min((1+|t|)u,1) bound near zero. The product with H and the packet is integrable. Dominated convergence then yields (16).

The increasing-scale branch Y=Xe^{u/2} is not compact in n as u→∞. Formula (16) controls it; calling the entire gamma term a finite compact prime sum would be incorrect.

## 4. At X=1 the gamma term becomes an explicit small prime series

Assume now
\[
X=1,\qquad W>3/\log2.
\tag{17}
\]
Then e^{3/W}<2. The rational sum (14), the product sum (6), L(1), and every decreasing-scale packet L(e^{−u/2}) are empty. Only the increasing branch of (16) survives.

Expand \((1-e^{-u})^{-1}=\sum_{j\ge0}e^{-ju}\). Each surviving prime packet has u in
\((2\log n-6/W,2\log n+6/W)\), wholly inside (0,∞). Substitute y=W(log n−u/2) and use the exact Laplace transform
\[
\int e^{zy}K_b(y)dy=(z^2-b^2)^2
\left(\frac{\sinh(z/2)}{z/2}\right)^6.
\tag{18}
\]
The result is
\[
\boxed{\mathcal G_c(1)
=-2\pi\sum_{k\ge1}H(2\sigma+2k)w(-i(\sigma+2k)).}
\tag{19}
\]
In particular every term in the series after −2π is positive: H(r)=\(\sum\Lambda(n)n^{-r}>0\) for real r>1, and the imaginary packet value is positive.

For clarity, the exponents in this calculation are exact. The jth geometric term contributes \(e^{-(1+\sigma/2+j)u}\). The n factor is n^{−σ}n^{−2−σ−2j}=n^{−2σ−2−2j}, and the Laplace argument is (2+σ+2j)/W. Summing n gives H(2σ+2+2j) and (18) gives w(−i(σ+2+2j)); set k=j+1. The factor is −2π, not −π or −2πW.

Absolute convergence justifies these interchanges: H(2σ+2k)≪2^{−2k}, while the imaginary packet grows at most polynomially times e^{6k/W}. Condition (17) makes 2log2−6/W positive. Equivalently, one may majorize the prime and geometric sums before using the signed K_b; its bounded support produces the same ratio. No positivity of K_b is assumed.

Define
\[
\mathcal T_{\sigma,W}=\sum_{k\ge1}H(2\sigma+2k)w(-i(\sigma+2k))>0.
\]
For W≥6 one has the useful uniform bound
\[
\boxed{\mathcal T_{\sigma,W}\ll W^{-4}
\qquad(1/2<\sigma<1,\ W\ge6).}
\tag{20}
\]
Indeed, with q=σ+2k and a<1/2,
\[
w(-iq)=\frac{(q^2-a^2)^2}{W^4}
\left(\frac{\sinh(q/(2W))}{q/(2W)}\right)^6
\ll W^{-4}(k+1)^4e^{3q/W}.
\]
Use sinh x/x≤eˣ and H(2σ+2k)≪2^{−2k}. The kth product is bounded by a constant times
\(W^{-4}(k+1)^4e^{-(2\log2-1)k}\), uniformly in σ and W≥6. Its sum converges. For fixed σ, dominated convergence also gives
\[
W^4\mathcal T_{\sigma,W}\longrightarrow
\sum_{k\ge1}H(2\sigma+2k)
[(\sigma+2k)^2-(1-\sigma)^2]^2>0.
\tag{21}
\]
Thus the gamma term is explicitly evaluated and small. This is a genuine sign and estimate for that term, not an estimate for the full energy.

## 5. Closed trace identity and an independent far-contour proof

Let \(\mathcal E_{\sigma,W}=\mathcal I_\sigma(1)>0\). Combining (9) and (19),
\[
\boxed{\mathcal E_{\sigma,W}
=-2\pi\left[\mathcal R(1)+\mathcal T_{\sigma,W}\right].}
\tag{22}
\]
It follows that \(\mathcal R(1)<-\mathcal T_{\sigma,W}<0\) and \(\mathcal E_{\sigma,W}<-2\pi\mathcal R(1)\). These are exact inequalities; their unknown term is still the full nontrivial-zero residue sum. They do not supply an independent upper bound for that term.

There is also a direct contour proof, independent of the digamma expansion. Take
\[
c_N=2\sigma+2N+1,\qquad d_N=c_N-\sigma\ge1.
\]
On the reflected line z=−2N−1−it, the equivalent gamma formula
\[
A(z)=-\log(2\pi)-\frac\pi2\cot(\pi z/2)
+\frac{\Gamma'}{\Gamma}(1-z)
\]
has bounded cotangent (a hyperbolic tangent on this line) and logarithmic digamma growth. The transformed H(1−z) is absolutely convergent. Hence
\[
H(2\sigma-c_N-it)\ll\log(c_N+|t|+2),
\quad H(c_N+it)\ll2^{-c_N}.
\]
For real t, the packet obeys
\[
|w(t-id_N)|\ll
\frac{W^2e^{3d_N/W}}{t^2+d_N^2}.
\tag{23}
\]
This follows from |sin z|≤e^{|Im z|}, the sixth-power denominator and the degree-four numerator. Since d_N is comparable to c_N,
\[
\int\frac{\log(c_N+|t|+2)}{t^2+d_N^2}dt
\ll\frac{\log(c_N+2)}{c_N}.
\]
The final vertical integral at X=1 is therefore
\[
\ll W^2e^{-c_N(\log2-3/W)}\frac{\log(c_N+2)}{c_N}\longrightarrow0
\tag{24}
\]
under (17). First let the horizontal heights tend to infinity at each fixed N, choosing heights away from zero ordinates as in R17; then let N→∞. This avoids an unproved simultaneous boundary limit.

The crossed reflected nontrivial residues are exactly (8). The additional reflected trivial poles s=2σ+2k have residue
\(H(2\sigma+2k)w(-i(\sigma+2k))\), since each trivial zero has multiplicity one. The reflected real pole and the unreflected pole at one are packet-canceled. Absolute convergence of both residue sums now proves (22) directly.

This second proof also explains the sufficient condition in (17): the decay 2^{−c_N} of the first prime series beats the packet's imaginary growth e^{3c_N/W}. No endpoint theorem is claimed here. The independently written root proof is retained separately as [ROOT_INFINITE_CONTOUR_TRACE.md](../root-contour-proof/ROOT_INFINITE_CONTOUR_TRACE.md), with its final SHA256 recorded in the author receipt.

## 6. The remaining residues still contain quadratic zero information

The functional equation has removed the gamma integral at X=1, but not the quantity that controls energy. For a concrete diagnostic, fix a nontrivial zero ρ=1/2+iγ of multiplicity m and choose a fixed W≥max(6,|γ|). Let δ=σ−1/2↓0, keeping this zero and W fixed. Since the reflected point approaches its conjugate zero,
\[
H(2\sigma-\rho)=-\frac m{2\delta}+O_\rho(1),
\]
\[
\mathcal R_\rho(1)
=-\frac{m^2}{2\delta}w_{2,1/2,W}(\gamma)+O_{\rho,W}(1).
\tag{25}
\]
Here the limiting packet weight is strictly positive by the choice of W. Multiplication by −2π gives exactly the local positive energy singularity
\(\pi m^2w_{2,1/2,W}(\gamma)/\delta\). This is the same singularity obtained by integrating the local approximation \(|H(\sigma+it)|^2\sim m^2/(\delta^2+(t-\gamma)^2)\).

This fixed-zero calculation is not a uniform estimate for the full residue sum as δ varies with W. It demonstrates why the nontrivial residues cannot be relabeled a small linear-prime or gamma error: they retain multiplicity squares and, through H(2σ−ρ), the correlations with the other zeros.

R17 already gives the exact positive centered representation
\[
\mathcal E_{\sigma,W}=2\int w(t)[R_\delta(t)-G_\sigma(t)]^2dt
\quad(W\ge3),
\]
with the complete paired-ξ resolvent and gamma center. Equation (22) is another exact representation of that same energy. It does not produce an additional inequality controlling its unknown nontrivial pair part merely by applying the functional equation.

## 7. Carrier X=T²: what does and does not survive

The finite-c identities (9), (14) and (16) remain valid at X=T²,W=T. The transformed product sum is now supported in \((T^2e^{-3/T},T^2e^{3/T})\), of width asymptotic to 6T. It retains the nonnegative coefficients Cσ, the signed spline K_b, the explicit gamma/rational contributions and every reflected-zero residue.

The far-contour estimate acquires X^{c_N−σ}. The sufficient condition \(\log X+3/W<\log2\) makes it vanish; the displayed estimate gives no vanishing at X=T². Likewise replacing the trivial series in (22) by terms multiplied by X^{σ+2k} generally destroys convergence at such a carrier. Formula (22) is **not** an identity for the Bragg carrier. No necessity or endpoint claim is inferred from this sufficient contour estimate.

The divergent series assertion has a direct test, independent of that upper bound. For fixed σ,W,X, its kth positive summand is asymptotic to
\[
\frac{(\log2)\,2^{-2\sigma}X^\sigma W^2e^{3\sigma/W}}
{(\sigma+2k)^2}
\left(\frac{X^2e^{6/W}}4\right)^k.
\]
This follows from H(r)∼(log2)2⁻ʳ and the elementary sinh asymptotic in the packet. Thus the summands do not tend to zero when Xe^{3/W}>2, in particular at X=T²,W=T for T≥2. This is an actual divergence calculation for the proposed residue series, not an inference from failure of an upper bound.

There is a quantified elementary comparison rather than a new power saving. Since
\[
C_\sigma(n)\le n^{2\sigma-1}(\log n)^2,
\]
and K_b is uniformly bounded for 0≤b≤1/2, the finite sum alone satisfies, for X sufficiently large and W≥1,
\[
|\mathcal P_{\sigma,W}(X)|
\ll (X^\sigma+WX^{\sigma-1})\log^2(2X).
\tag{26}
\]
There are O(X/W+1) integers in its interval; the prefactor W and the coefficient bound give (26). At X=W² its scale is X^σ log²X.

For fixed σ, the existing logarithmic-derivative and zero-counting bounds in the finite-c identity give only
\[
|\mathcal P_{\sigma,W}(X)-2\pi\mathcal B(X)|
\ll_\sigma W(1+X^\delta)\log^4(W+2),\qquad X\ge1.
\tag{27}
\]
To see this, use (9) and (12), \(|\mathcal I_\sigma(X)|\le\mathcal E_{\sigma,W}\ll_\sigma W\log^4(W+2)\), and \(|\mathcal G_\sigma(X)|\ll_\sigma W\log^3(W+2)\). In (8), unit-interval zero counting and the packet envelope \(\ll_\sigma\min(1,W^2/(1+|\gamma|)^2)\) give \(|\mathcal R(X)|\ll_\sigma X^\delta W\log^3(W+2)\). These are deliberately conservative logarithmic estimates with fixed σ.

At X=W², WX^δ=X^σ. Thus (27) does not improve the power in the elementary bound (26), and its displayed logarithms are worse. It is not uniform as σ approaches 1/2, so it cannot be used at δ comparable to 1/log T without additional tracking. This is a specific failed estimate, not a no-go theorem for prime correlations.

The R16 Bragg statistic is a nonnegative frequency bump of the actual pair form factor; \(\mathcal I_\sigma(T^2)\) is a signed time oscillation and \(\mathcal P_{\sigma,W}(T^2)\) is a multiplicative prime-product sum. None is automatically that bump. A new estimate for the retained residue/covariance, with a justified kernel transfer, is still required.

## 8. Provenance and stopping point

The unchanged R17 quadratic-packet report supplies the Fourier normalization, finite contour shift and positive paired-ξ identity; the unchanged R16 Bragg report specifies the actual target. The functional-equation and digamma identities above are proved or expanded explicitly in this note. Source hashes and this report's hash are kept in the adjacent author receipt.

The completed advance is the exact functional-reflection formula, the cancellation audit at 2σ, explicit arithmetic resolution of the gamma term, and the closed energy trace with a positive O(W⁻⁴) trivial-zero correction at X=1. The proof stops at the demonstrated equivalence with the existing positive zero-pair energy and the quantified failure of the elementary bound at X=W². No strict AH/Bragg or Montgomery result is claimed.
