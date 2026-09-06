# Selected-frequency complex transpose pairings of the actual prime matrix

Date: 2026-09-05. Author: Aquinas. Status: separate bounded floating follow-up submitted for independent review. The frozen `RESULTS.md` and its original `AUTHOR_RECEIPT.json` are unchanged. This note adds six calculations on the existing arrays: zero and the previously selected winning Mellin frequency for each of the three cases. There is no new prime computation, matrix, height, frequency search, profile change or mode subtraction.

The direct transpose pairing reaches **35.3%, 47.3%, and 54.8% of the operator norm** at those selected frequencies. This is a substantial finite Mellin lower-bound pairing despite the much smaller projection of the single top eigenvector onto the corresponding template plane. The earlier plane-overlap statistic alone therefore did not answer the relevant operator question. The new values do not establish an asymptotic obstruction or any theorem about the full covariance.

## 1. The quantity and the necessary distinction

Keep the actual real symmetric matrix \(C_{d,k}=f_T(dk)\), its complete odd row set \(I\), and \(N=|I|\). For a real frequency \(t\), set
\[
w_t(d)=\frac{d^{it}}{\sqrt N},\qquad
B_C(t)=w_t^{\mathsf T}Cw_t.
\tag{1}
\]
The transpose in (1) contains **no complex conjugation**. In particular it is not the Hermitian quadratic form. Since \(\|w_t\|_2=1\),
\[
|B_C(t)|=|\langle\overline{w_t},Cw_t\rangle|
\le\|C\|_{\rm op}.
\tag{2}
\]
This uses the usual complex Euclidean inner product only to justify the norm inequality; the computed quantity remains the unconjugated transpose pairing.

For the multiplicative matrix, the exact alternative formula is
\[
\boxed{B_C(t)=\frac1N\sum_m r_I(m)f_T(m)m^{it},\qquad
r_I(m)=\#\{(d,k)\in I^2:dk=m\}.}
\tag{3}
\]
Thus the test preserves every ordered product multiplicity and the actual centered prime-window coefficients. It has no Möbius or logarithmic cofactor coefficients; it is a test vector for an operator lower bound, distinct from the original fixed Möbius/log contraction.

Writing \(w_t=c+is\), with real vectors \(c,s\), gives
\[
B_C(t)=c^{\mathsf T}Cc-s^{\mathsf T}Cs
+2i\,c^{\mathsf T}Cs.
\tag{4}
\]
A projection of a leading vector onto \(\operatorname{span}\{c,s\}\) does not determine (4). For example, if a real operator is the identity on a plane with orthonormal vectors \(u,v\), then \(w=(u+iv)/\sqrt2\) has unit norm and \(w^{\mathsf T}Cw=0\), although a leading vector can lie entirely in that plane. This is an elementary algebra illustration, not a replacement model for the actual arithmetic arrays.

Conversely, the present actual matrices show that a substantial transpose pairing need not be carried by the single largest eigenvector: several eigenvectors in a closely spaced spectrum can contribute to the same template plane.

## 2. Frequency choice and observed complex values

The three positive frequencies were selected in the earlier follow-up by maximizing the **top-vector plane projection** on its declared finite grid. That choice was post-initial-data and was not made by maximizing (1). This calculation evaluates those frequencies and zero only.

The complex phases in the table use exactly \(d^{it}=\exp(it\log d)\), with no reference-point phase normalization. Rounding is for display; `transpose_pairing_results.json` retains the recorded precision.

| X | N | t | Real B_C(t) | Imaginary B_C(t) | Absolute B_C(t) | Absolute/op norm |
|---:|---:|---:|---:|---:|---:|---:|
| 1,000,000 | 150 | 0 | 7.167609882 | 0 | 7.167609882 | 0.032884922 |
| 1,000,000 | 150 | 1756.868499 | 39.170699848 | −66.162043756 | 76.887968893 | 0.352761223 |
| 4,000,000 | 300 | 0 | −40.546785757 | 0 | 40.546785757 | 0.088690528 |
| 4,000,000 | 300 | 3046.841660 | 128.967085966 | 173.817098990 | 216.436811018 | 0.473425813 |
| 16,000,000 | 600 | 0 | −57.051104003 | 0 | 57.051104003 | 0.056079184 |
| 16,000,000 | 600 | 4760.911407 | −253.735780051 | 496.807396800 | 557.852521365 | 0.548348969 |

The corresponding earlier top-vector squared plane projections were 0.131636, 0.122876 and 0.057238. These numbers measure a different quantity; no implication from one to the other was used in (1)–(4).

## 3. Two-dimensional real compressions

For each selected positive frequency, QR orthonormalization of the real cosine/sine vectors gives a matrix \(Q_t\) with two orthonormal columns. The compression \(Q_t^{\mathsf T}CQ_t\) is retained without being subtracted from C. Its two eigenvalues and norm ratios are:

| X | Compression eigenvalues | Compression norm/full norm |
|---:|---|---:|
| 1,000,000 | −51.627173385, +95.955927156 | 0.440244822 |
| 4,000,000 | −212.993603592, +219.850294618 | 0.480892340 |
| 16,000,000 | −556.151959837, +559.552145073 | 0.550019638 |

The signed structure of the plane matters: the two later compressions have large eigenvalues of opposite sign. The real-part difference and imaginary cross term in (4) retain that structure. The transpose-pairing magnitude is not the trace of this compression or a top-eigenvector projection.

These finite values make Mellin test vectors relevant to the operator discussion. They do not prove that their contribution violates the proposed uniform bound, and they do not by themselves make a vector-specific approach the only viable one. In particular, no asymptotic exponent is fitted from the three ratios.

## 4. Checks and provenance

The script `check_transpose_pairing.py` reads the frozen raw arrays and `mellin_results.json`. It uses `w @ (C @ w)`, without conjugation. Each of the six values is checked against (4), and against the grouped product identity (3). A further phase check evaluates the rotated vector \(\exp(it\log(d/d_{\rm mid}))/\sqrt N\) and restores the factor \(\exp(2it\log d_{\rm mid})\).

All checks pass. Unit-norm discrepancies are at most \(2.45\cdot10^{-15}\). The real cosine/sine expansion differs by at most \(6.36\cdot10^{-14}\) absolutely. The grouped-product calculation differs by at most \(4.26\cdot10^{-10}\); restoring the centered phase differs by at most \(1.89\cdot10^{-9}\). The latter differences reflect floating reduction of large trigonometric phases; they are much smaller than the recorded pairings, but are explicitly retained. No error is claimed to be an outward enclosure.

The six original complex vectors, pairings and compressions are stored in `arrays/transpose_pairing_X.npz`. Full stdout is `transpose_pairing_run.log`. The separate `FOLLOWUP_TRANSPOSE_RECEIPT.json` pins these new artifacts and their frozen source inputs. It does not replace the historical receipt.

Historical unchanged inputs:

* `RESULTS.md`: SHA256 `acf1ec31909cda5ef788778d10e152d9813eaee97095d9f34adcb2c2b731a722`.
* `AUTHOR_RECEIPT.json`: SHA256 `c29d6feaeaee0f1f643ee8849c8fef7a77b09d111999c1aa60ecdb6ef3f86121`.
* `mellin_results.json`: SHA256 `06624672d6b4739f0575e8125596e9020aeab44ea970b51ada16fbb43d73120e`.

The numerical conclusion is confined to these six values: the actual Mellin transpose pairing is substantially stronger than the original leading-vector-overlap diagnostic suggested. Its mathematical asymptotic control, and the strict bound for the full prime covariance, remain open in this programme.
