# Independent check of the coherent-mode curvature normalization

Date: 2026-09-05. Scope: ordinary proof audit of the complete root note, distinct from the finite-time local-deficit theorem. Accepted at the hash below. No numerical enclosure, priority claim, or zeta transfer is asserted.

I independently checked the radian-to-microscopic conversion: with s=N²t/(4π²) and q=Nθ/(2π), the phase u=4πq has u′=(8π²/N)V. Antisymmetry gives both sums of velocities and accelerations zero. At a common initial phase, differentiating the squared normalized exponential sum therefore gives B″(0)=−128π⁴N⁻³ΣV², including the factor two from differentiating a squared modulus. A common rotation changes no term.

I re-expanded the force square by unordered pairs and triples. Each unordered triple contributes −2, and replacing cotangent squares by cosecant squares gives ΣV²=2Σpairs csc²−N(N²−1)/3. The rank-N projection on 2N sites has the stated pair-inclusion probability. Summing the ordered grid displacement costs exactly 2N; it gives expected ordered cosecant sum N(N²−1)/2. The odd fourth-cosecant sum is N²(N²+2)/3, obtained by subtracting the N-grid identity from the 2N-grid identity. Consequently EΣV²=N(N²−1)/6 and EB″(0)=−(64π⁴/3)(1−N⁻²).

The N=2 check is correct: adjacent configurations have total mass 1/2 and force-square sum 2; opposite configurations have the remaining mass and zero force. The resulting expected curvature is −16π⁴. Differentiation through the expectation at fixed N is legitimate because there are finitely many initial configurations, each simple and collision-free on a positive interval.

The author's limitation is essential and is retained: this global unweighted pair statistic is not the localized Round 16 bump deficit. A fixed-N Taylor formula supplies no uniform remainder in N. The separately proved local-gap theorem supplies its own acceleration bound and finite time interval, rather than inheriting one from this curvature. Neither proof identifies the finite-circle flow with true zeta heat or transports positive-time information to H0.

Reviewed file: `../root-bragg-curvature/EXACT_COHERENT_MODE_CURVATURE.md`.
SHA256: `d8ae40d3442564644b2fe9e647f8ac6061b13f6b8ae4eedfbb618dd7036d9a76`.

The adjacent one-N float diagnostic also checks the coherent-mode constant, but the acceptance above is an algebraic proof review, independent of that diagnostic.
