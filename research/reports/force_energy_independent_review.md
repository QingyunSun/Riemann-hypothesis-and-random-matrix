# Independent mathematical review of the circular force-energy audit

Date: 2026-09-05. Reviewer: residual_gram agent, independently of the flow agent's derivation.

Reviewed source: **force_energy.md**, SHA256 **526c5e7abd2c6437f3ec2d6cdcdffb27db13a134af15c4ab17464487cbdf360c**.

**Verdict: accept the stated finite-CUE/ACUE identities and the infinite CUE right-slope conclusion, with the conventions and scope already stated in the source. No remaining mathematical gap was found in the reviewed arguments.** This review does not establish novelty, any analogous zeta identity, or a consequence for AH/RH.

The most important independently checked conclusions, for radians and the deterministic repulsive drift \(V_i=\sum_{j\ne i}\cot((\theta_i-\theta_j)/2)\), are
\[
D=\sum_iV_i^2,\qquad
\mathbb E_{\rm CUE}D=\frac{N(N^2-1)}3,\qquad
\mathbb E_{\rm ACUE}D=\frac{N(N^2-1)}6,
\]
\[
\mathbb E_{\rm ACUE}LD=-\frac{2N(N^4-1)}{15},
\qquad
\lim_{t\downarrow0}
\frac{\mathbb E_{\rm CUE}D(\Phi_tX)-\mathbb E_{\rm CUE}D(X)}t
=-\infty\quad(N\ge2).
\]

## 1. Pointwise derivative and three-body reduction

With \(w_{ij}=\csc^2((\theta_i-\theta_j)/2)\), the Jacobian of \(V\) has off-diagonal entries \(w_{ij}/2\) and diagonal entries \(-\sum_{j\ne i}w_{ij}/2\). It is a negative weighted graph Laplacian. Therefore
\[
LD=2V^\mathsf T J_VV
=-\sum_{i<j}w_{ij}(V_i-V_j)^2.
\tag{1}
\]
The coefficient is exactly \(-1\) for an unordered pair sum. This verifies both the sign and the time normalization.

Independently expanding \(LQ\), with \(Q=\sum_{i\ne j}w_{ij}\), gives the pair contribution
\[
-4\sum_{i<j}(w_{ij}^2-w_{ij})
\]
plus the three-body contribution
\[
\sum_{i<j<k}
(w_{ij}w_{ik}+w_{ij}w_{jk}+w_{ik}w_{jk}).
\tag{2}
\]
The cotangent-addition rational identity used to reduce each triple was checked exactly in two independent indeterminates with SymPy. Its residual is the zero rational function.

As a normalization check, an equally spaced \(N=3\) configuration has all \(w_{ij}=4/3\). Its pair contribution is \(-16/3\), its triple contribution \(16/3\), and its total derivative is zero as required by force balance.

## 2. Three-site inclusion probability and ordering factors

For the ACUE projection process on \(M=2N\) sites, the two-site formula is
\[
\rho_2(0,d)=\frac14-\frac{\mathbf1_{d\ {\rm odd}}}{4N^2}w_d.
\]
Every triple of distinct sites contains a same-parity pair, so at least one off-diagonal kernel entry in its cyclic three-edge product vanishes. Expanding the \(3\times3\) determinant therefore gives
\[
\rho_3(0,d,e)
=\frac18-\frac1{8N^2}
\left[\mathbf1_{d\ {\rm odd}}w_d+
\mathbf1_{e\ {\rm odd}}w_e+
\mathbf1_{d-e\ {\rm odd}}w_{d-e}\right].
\tag{3}
\]
The factor \(1/(8N^2)\) is correct: each off-diagonal squared modulus is multiplied by the remaining diagonal value \(1/2\).

The unordered-pair contribution in (2) has expectation
\[
-4\frac M2\sum_{d\ne0}\rho_2(0,d)(w_d^2-w_d)
=-\frac M2(S_4-S_2)+\frac M{2N^2}(O_6-O_4).
\tag{4}
\]

For triples, the sum of all three central edge products equals one half of the ordered central-vertex sum. Thus its expectation is
\[
\frac M2\sum_{\substack{d,e\ne0\\d\ne e}}\rho_3(0,d,e)w_dw_e.
\tag{5}
\]
This confirms the source's \(M/2\) factor. It can alternatively be viewed as \(M/6\) for ordered triples times three equal edge-product contributions. There is no extra factor of two or three left over.

## 3. Independent reconstruction of the parity convolution

Fix an odd \(d\), put \(\alpha=\pi d/(2N)\), and let \(e=2k\), \(1\le k\le N-1\). Set \(u=\pi k/N\), \(v=\alpha-u\). The identity in the source reads
\[
\csc^2u\,\csc^2v
=\csc^2\alpha\left[
\csc^2u+\csc^2v+
2\cot\alpha(\cot u+\cot v)\right].
\]
The four sums needed over nonzero even sites are
\[
\sum\csc^2u=\frac{N^2-1}{3},\qquad
\sum\csc^2v=N^2-w_d,\qquad
\sum\cot u=0,\qquad
\sum\cot v=-\cot\alpha.
\]
Indeed \(N\alpha\) is an odd multiple of \(\pi/2\); the full shifted cosecant-square sum is \(N^2\) and the full shifted cotangent sum is zero. Removing \(k=0\) yields the displayed subtractions.

Since \(\cot^2\alpha=w_d-1\), the convolution is exactly
\[
\sum_{\substack{e\ne0\\e\ {\rm even}}}w_ew_{d-e}
=\frac{4N^2+5}{3}w_d-3w_d^2.
\tag{6}
\]

To check the complete triple correction without skipping the parity bookkeeping, its first two terms together are
\[
2\sum_{d\ {\rm odd}}w_d^2(S_2-w_d)
=2S_2O_4-2O_6.
\]
The third term has \(d-e\) odd, meaning one of \(d,e\) is odd and the other even. By (6), it is
\[
2\sum_{d\ {\rm odd}}w_d
\sum_{\substack{e\ne0\\e\ {\rm even}}}w_ew_{d-e}
=\frac{2(4N^2+5)}3O_4-6O_6.
\]
Adding them and using \(S_2=(4N^2-1)/3\) gives
\[
\frac83(2N^2+1)O_4-8O_6,
\]
exactly as claimed. Combined with (4), (5), this yields the source's final intermediate expression
\[
\mathbb E LD=\frac M{16}\left[
S_2^2-9S_4+8S_2+\frac{16}{N^2}O_6
-\frac{16(N^2+2)}{3N^2}O_4\right].
\tag{7}
\]

Exact symbolic substitution of the four trigonometric-sum polynomials into (7) simplifies to
\[
-\frac{2N(N^4-1)}{15}
\]
identically in the indeterminate \(N\). The odd-site fourth- and sixth-power polynomials were separately checked as the differences of the full \(2N\)-site and \(N\)-site sums.

## 4. CUE divergence and the actual expectation-level right slope

The CUE density has score \(V\), and the integration by parts for the first energy moment is legitimate: multiplying the Vandermonde square by a single cotangent cancels the apparent pair pole, while multiplying it by \(V_i^2\) or \(w_{ij}\) remains integrable. Equivalently, each pair density vanishes quadratically and the relevant first-moment singularities are at most quadratic. The compact polynomial form handles intersections of collision hyperplanes as well.

This reasoning is not valid for the derivative observable, which has a fourth-order pole. The source correctly does not reuse that integration by parts.

Choose a region where one pair has small positive gap \(g\), all other points stay a fixed distance from this pair and one another, and the remaining coordinates range over a set of positive measure. Then
\[
V_i-V_j=\frac4g+O(g),\qquad
w_{ij}=\frac4{g^2}+O(1).
\]
The leading contribution to (1) is \(-64/g^4\). Other pair terms have at most order \(g^{-2}\). Since the density is a positive smooth factor times \(g^2\), and \(LD\le0\) globally, the integral of \(-LD\) diverges like \(\int_0^\epsilon g^{-2}dg\). Hence
\[
\mathbb E_{\rm CUE}[-LD]=+\infty.
\]
This is a valid one-sided divergence, with no positive-negative cancellation issue.

For the expected trajectory, define
\[
A_t(X)=\frac{D(X)-D(\Phi_tX)}t,\qquad t>0.
\]
Global repulsive existence and (1) imply \(A_t\ge0\). Also \(A_t(X)\to-LD(X)\) for every initially distinct configuration, and \(\mathbb ED(X)<\infty\). Applying Fatou along any sequence \(t_n\downarrow0\),
\[
\liminf_n\mathbb EA_{t_n}\ge\mathbb E[-LD]=+\infty.
\]
Since the sequence was arbitrary, \(\mathbb EA_t\to+\infty\) as \(t\downarrow0\). Moreover,
\[
\mathbb EA_t=\frac{\mathbb ED(X)-\mathbb ED(\Phi_tX)}t
\]
is well-defined because \(0\le D(\Phi_tX)\le D(X)\). This proves the source's actual infinite negative right slope. It is not a formal derivative-integral interchange.

The \(N=2\) truncated integral formulas were also checked directly. Their coefficients agree with the chosen drift normalization.

## 5. Independent exact finite checks

The companion program **force_energy_review.py** uses exact rational arithmetic in cyclotomic quotient rings for \(N=2,3,4\). This is independent of the source's float64 enumeration and independent of its determinantal pair/triple expectation reduction.

At every subset, the program constructs the original force via
\[
V_i=iB_i,\qquad
B_i=\sum_{j\ne i}\frac{\zeta^{s_i-s_j}+1}{\zeta^{s_i-s_j}-1}.
\]
It evaluates the dissipative derivative directly as
\[
LD=\sum_{i<j}w_{ij}(B_i-B_j)^2.
\]
The sign change comes from \(i^2=-1\); no numerical complex arithmetic is used. It then checks the pair/triple reduction pointwise and sums the original Vandermonde weights exactly.

| \(N\) | Subsets | Exact \(\mathbb ED\) | Exact \(\mathbb ELD\) |
|---:|---:|---:|---:|
| 2 | 6 | 1 | −4 |
| 3 | 20 | 4 | −32 |
| 4 | 70 | 10 | −136 |

All pointwise identities, normalizations and expectations passed. The all-\(N\) conclusion remains based on the analytic derivation and symbolic polynomial identities, not extrapolation from this table.

Evidence files in `research/force-energy/`:

- **force_energy_review.py** — exact symbolic and cyclotomic checks.
- **force_energy_review_results.json** — results.
- Dependency: **dynamic-generator/generator_audit.py**, only its small CyclotomicRing implementation. Importing it does not run its main audit.

Reproduction:

    OPENBLAS_NUM_THREADS=1 python3 research/force-energy/force_energy_review.py

## 6. Accepted scope and limits

The accepted result is an exact finite-ensemble distinction for a singular force observable, plus a nonanalytic initial expectation response in CUE. It is compatible with the independently proved persistence of protected trace moments: \(D\) and \(LD\) are not in that bounded Fourier-weight polynomial algebra.

The source correctly identifies that \(D\) collapses to a singular two-point kernel. The mean of \(LD\), after reduction, involves up to three points, but still with singular kernels. No bound for the corresponding arithmetic zero sums has been supplied.

No additional caveat is needed for differentiating the ACUE average: after removing the irrelevant global rotation it is a finite sum over distinct configurations. A finite derivative at zero follows from the smooth local flow at each of those configurations.

The stated observations do not prove dynamical low-mode leakage, AH failure, RH, or a new prime-gap bound. They also do not establish that the finite-ensemble formulas are previously unknown. Within those limits, this review accepts the report.

Integration note: the reviewed-source SHA identifies the original staging report. The public copy changes only evidence paths; the preserved local source and Git manifest identify both versions.
