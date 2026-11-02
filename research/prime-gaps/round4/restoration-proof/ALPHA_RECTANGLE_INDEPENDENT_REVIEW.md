# Independent audit of the positive-alpha rectangle certificate

2026-09-05. Reviewed files: ../prime-credit/alpha_credit.py, certify_alpha_rectangle.py, prime_alpha_credit.md, and the completed alpha_rectangle_certificate.json. This review is independent of their author. It reads the preserving official certificate source and inspects the completed outward receipt; it does not rerun the large contraction.

## 1. Verdict and certified scope

I found no mathematical or normalization defect in the rectangle lower-event construction or its adapter to the official outward moment engine. The following points are correct:

- the rectangle belongs to the actual deleted outer support, not merely an upper failure cover;
- the residual total law is exactly Lebesgue measure on the selected interval;
- the marked densities have no missing exponential normalizer, cap factor, or factor \(1/2\);
- the same-owner and different-owner cases are both included, once each;
- all coordinate kernel factors of \(h\) cancel against the published \((hZ)^{40}\) normalization correctly;
- the adapter uses the actual midpoint step trial, its full signed square expansion, and a valid inward radial mask;
- the completed receipt contains a positive outward lower endpoint.

The new receipt proves a lower credit of approximately

$$
\frac{c_\alpha\alpha_{\rm rect}}{I_H^+}
\ge1.50581194718\times10^{-6},
\qquad
c_\alpha=1-4\rho_*|b_h|.
\tag{1.1}
$$

The exact rational endpoint is in the receipt and in rectangle_independent_checks.json; the displayed decimal is descriptive. A simpler strictly lower rational bound is \(1.5058\times10^{-6}\).

This improves the inherited published \(k=40\) trial's certified normalized margin from approximately \(23.3604523\) ppm to at least \(24.8662642\) ppm. The published cap and loss endpoints are inherited source inputs, not recomputed by the new run. This is a strict improvement of the fixed-trial margin, not a smaller prime-gap theorem or a \(k=39\) certificate.

Our earlier restoration report correctly said the old upper ledger alone yields no positive alpha lower bound. This new, separate lower-event calculation supplies such a bound and does not conflict with that statement.

## 2. Proof that the event really is deleted

Use the exact official grid

$$
h=\frac{2742997}{258046918656},\qquad n=98264.
$$

The residual cutoff is \(b=18800h\), and the two marked intervals are

$$
P=[26400h,29100h],\qquad Q=[32400h,36700h].
$$

These intervals are strictly ordered and lie above \(b\). All residual coordinate totals are at most \(b\), so every residual fragment is at most \(b\). Hence \(p\in P\) and \(q\in Q\) are the unique two fragments above \(b\) in the entire outer root, with \(p<q\).

The source row used is the retained new-ladder row of index 24. I checked the official ladder generation and row-retention filter: this row is included among the 39 retained new rows, and its order is three. Its relevant outer condition is

$$
s\le a
\quad\text{or}\quad
\bigl(H_{\phi_D,\xi}\le A
\text{ and the opposite-root condition}\bigr),
\qquad
\phi_D(u)=\min(3u/2,L).
$$

Throughout the selected rectangle, exact rational inequalities give

$$
p>\xi,\qquad
\frac32p\le\frac32(29100h)<L,
$$

and

$$
q+p+\phi_D(p)
=q+\frac52p
\ge(32400+\tfrac52\,26400)h
=98400h>A.
\tag{2.1}
$$

The inclusive tail at the witness \(p\) contains exactly \(p+q\), because all other fragments are smaller than \(p\). Thus (2.1) violates the actual owner condition. The opposite-root condition need not be analyzed to establish failure of the conjunction.

The inward radial mask is

$$
95639\le r=\sum_i\lfloor t_i/h\rfloor\le98263.
$$

The exact core comparison is \(95638h\le a<95639h\), while the actual total satisfies

$$
s=\sum_i t_i\ge rh>a.
$$

This excludes the safe-core alternative. On the other side,

$$
s<(r+40)h\le98303h<S=98304h,
$$

and the coordinate-index sum belongs to the retained official outer cells.

Finally, every fragment is at most \(36700h\), strictly below the smallest official outer-shell cap \(46580h\). Therefore the event lies inside the actual cap domain \(H_O\), regardless of which outer shell contains its total. Combining these facts proves it lies in \(H_O\setminus O\).

The proof uses the actual row predicate, not a rounded common failure threshold from the old covering argument. Thus it is a legitimate source of lower mass.

## 3. Residual measure and the missing-factor audit

The source's coordinate measure is

$$
\nu_c=e^\gamma c\,\mathcal L(\Pi_c),
$$

where \(\Pi_c\) is the Poisson point process of intensity \(du/u\) on \((0,c]\). For \(b<c\), the probability of no points in \((b,c]\) is \(b/c\). Hence

$$
\nu_c\big|_{\{\max X\le b\}}=\nu_b.
\tag{3.1}
$$

This identity includes the normalizing factor: \(e^\gamma c\cdot(b/c)=e^\gamma b\). It must not be followed by an additional \(b/c\) or \(e^{-\gamma}\) factor.

The total-size pushforward of \(\nu_b\) is

$$
\rho_D(x/b)\,dx.
$$

For \(0\le x\le b\), \(\rho_D(x/b)=1\). Consequently the selected residual total has exactly the measure \(dx\). It is not a probability-uniform density \(dx/b\); its mass on this interval is \(b\).

For a coordinate with one selected large fragment, Poisson decomposition adds \(dp/p\) or \(dq/q\). For a coordinate with both, it adds \(dp\,dq/(pq)\). Since \(P\) and \(Q\) are disjoint, the two selected fragments have unique labels determined by their intervals. There is no \(1/2!\): one may derive the same fact by first using the unordered two-point density with \(1/2!\), then summing its two disjoint orderings.

Across all coordinates the event measure is therefore

$$
\prod_{i=1}^{40}dx_i\,\frac{dp\,dq}{pq},
$$

with the chosen marks assigned to their coordinate owners. The interval restrictions and total caps merely restrict this measure.

## 4. Owner counting: the same-coordinate term is essential

There are two disjoint owner classes:

1. \(p\) and \(q\) belong to different coordinates: \(40\cdot39=1560\) ordered choices.
2. Both belong to one coordinate: 40 choices.

The owners are ordered by the labels \(p\in P\) and \(q\in Q\). An additional factor two would duplicate configurations. Omitting the second class would lose genuine positive mass.

For the moment computation, let \(u_j,v_j,w_j,z_j\) be the four coordinate cell measures for no mark, only \(p\), only \(q\), and both marks. The ring

$$
\mathbb R[a,b]/(a^2,b^2)
$$

with coordinate element \(u+av+bw+abz\) has product rule

$$
(u,v,w,z)(u',v',w',z')
=
(uu',\,vu'+uv',\,wu'+uw',\,
zu'+uz'+vw'+wv').
$$

The coefficient of \(ab\) in its 40-fold product is precisely the sum of same-owner and different-owner assignments. For constant integrated channel masses it is

$$
40zu^{39}+40\cdot39vwu^{38}.
$$

This is exactly the official SourceJets “palm” multiplication and “both” channel. Those factors are already generated by the ring and must not be applied again outside the contraction.

The equality between some integrated channel masses does not permit replacing the same-owner cell kernel by a product of the separate-owner kernels. The same-owner total is \(x+p+q\), and it requires the separate three-variable box kernel used in the adapter.

## 5. Exact box volumes and normalization by \(hZ\)

Replace \(1/(pq)\) on the marked rectangle by its lower constant

$$
\frac1{P_+Q_+},\qquad P_+=29100h,\quad Q_+=36700h.
$$

This produces one coherent positive submeasure. Since the final integrand is \(F_{\rm step}^2\ge0\), its integral is a lower bound on the event's mass.

Scale all variables by \(h\). A coordinate with one mark has two integration variables \(x,p\), so its cell measure is

$$
\frac{h^2}{29100h}\,
\operatorname{Vol}\{(x',p'):
0\le x'\le18800,\ 26400\le p'\le29100,\
j\le x'+p'<j+1\}.
$$

Dividing by \(h\), as needed for the normalized coordinate array, leaves the two-dimensional volume divided by 29100. The analogous \(q\) channel divides by 36700.

The same-owner channel has three integration variables and two mark denominators. Its cell measure is \(h\) times the corresponding three-dimensional volume divided by \(29100\cdot36700\). Thus the four dimensionless arrays in the adapter are exactly cell mass divided by \(h\).

The inclusion-exclusion routine returns \(d!\) times the \(d\)-dimensional cell volume. Therefore the denominators

$$
1,\quad 2\cdot29100,\quad 2\cdot36700,\quad
6\cdot29100\cdot36700
$$

are correct.

On an actual coordinate cell, the official step profile contributes \(g_j^2\). The adapter's weight is

$$
\frac{g_j^2}{Z}\frac{\text{cell mass}}h
=\frac{g_j^2\,\text{cell mass}}{hZ}.
$$

Multiplication across 40 coordinates supplies exactly the companion paper's \((hZ)^{-40}\) normalization. No extra \(h\), \(40\), \(Z\), or physical-scale multiplier belongs after the moment contraction.

This point distinguishes the new norm lower integral from the official source-loss routines, some of which integrate an extra erased coordinate and accordingly have additional factors. The adapter correctly uses only the coordinate product law needed here.

## 6. Actual step trial and signed-square coherence

I checked that the official CapEngine aliases its signature and coefficient arrays directly to the printed rational trial data. Its square_groups are obtained by the exact full quadratic expansion of the 77 coefficients, including a factor two for distinct coefficient pairs.

The radial polynomial argument is

$$
(r+20)h-\frac9{10},
$$

the sum of the 40 coordinate midpoints minus the fixed center. The angular moments use the same coordinate midpoints. Hence the adapter evaluates the published **step trial**, not a continuous polynomial approximation at the original real totals.

Every kernel channel, radial mask, and signature uses the same positive lower submeasure. Some coefficients of the polynomial-square expansion are negative, but their sum represents the nonnegative square. The adapter:

- obtains two-sided outward intervals for the positive moment coefficients;
- multiplies by two-sided intervals for the signed radial polynomial;
- uses the official signed interval product and outward reduction;
- adds all 53 signed signature contributions before testing the final lower endpoint.

It does not freeze upper moment bounds and then multiply them by negative coefficients, and it does not clamp negative signature terms to zero. Several negative partial sums in the run log are consistent with the necessary signed cancellation.

The proof therefore rests on ordinary interval enclosure of one fixed coherent integral. Independence between numerical interval errors is not required.

## 7. Independent checks performed

The companion rectangle_independent_checks.py does not import CapEngine, SourceJets, or the rectangle certifier as a module.

It reconstructs all three marked cell-numerator arrays by a different exact method: decompose each integer-length interval into unit intervals, convolve their integer location counts using prefix sums, and finish with the Eulerian unit-cube cell-volume numerators

$$
(1,1)\quad\text{in dimension two},\qquad
(1,4,1)\quad\text{in dimension three}.
$$

All 98,264 entries of each reconstructed array agree exactly with the proposed inclusion-exclusion routine. Their sums are respectively

$$
101520000,\quad161680000,\quad1309608000000.
$$

The script also verifies the owner expansion with exact fractions on a four-coordinate, three-cell toy measure, using a nonconstant squared trial and a radial mask. The ring contraction equals a separate explicit sum over all 4 same-owner and 12 different-owner choices. This checks more than the unweighted total mass.

Finally, it checks the completed receipt's endpoint ordering, positive lower endpoint, alpha normalization by the published \(I_H^+\), and multiplication by the exact coefficient \(c_\alpha\), all using exact fractions.

These checks passed. The source adapter hash and receipt hash are stored in rectangle_independent_checks.json.

## 8. Completed outward receipt and evidence boundary

The receipt records:

- the unmodified mandatory signed-convolution regression passed;
- 160-bit Arb working precision and 224-bit fixed-point source arrays;
- one worker thread;
- all 53 signed signatures completed;
- a final normalized rectangle interval approximately

$$
[3.569723878940875\times10^{-20},
\ 3.569723886815550\times10^{-20}].
$$

Using the source-inherited bound \(I_H^+=23685317890\cdot10^{-24}\), the exact lower endpoint gives

$$
\frac{\alpha_{\rm rect}}{I_H^+}
\ge1.50714628172\times10^{-6},
$$

and the exact \(c_\alpha\) gives (1.1). The contraction took about 92.6 seconds according to its receipt.

This is stronger evidence than the earlier randomized-QMC estimate: it is a completed outward enclosure of the explicit lower submeasure. The QMC code's proposal factors, owner split, and midpoint evaluation are also consistent with this same integral, but its standard errors were never deterministic certificates and are not used here.

The remaining trust boundary is the official outward arithmetic implementation and the corrected runtime that passed its unchanged regression, together with the published denominator and previous upper-loss inputs. This review checks the mathematical adapter, event inclusion, normalization, and scalar receipt; it is not a formal verification of FLINT or a fresh proof of all 149 original physical bounds.

The improved \(k=40\) margin follows by adding this lower credit once to Proposition 4.6 while retaining all existing outer and inner debts. It does not justify removing the mixed-term debt, transferring the mass to dimension 39, or adding the same credit again through a separately restored denominator.
