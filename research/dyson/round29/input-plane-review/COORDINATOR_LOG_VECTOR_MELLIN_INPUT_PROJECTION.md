# The observed Mellin planes couple weakly to the actual log-cofactor input

Coordinator derivation, 2026-09-05. Submitted for independent mathematical review. This is an ordinary deterministic projection lemma and a conditional application of the existing R27 RH Frobenius bound. It is not a new strict global covariance bound or a matrix modification.

## Exact scope

Let X=T^2, ell=log T, and let I_T consist of every odd integer in (21T/20,27T/20]. Write N=|I_T|. Use the unchanged R28 actual prime-window matrix C, with the original cutoff, all prime powers, and the odd-endpoint center 2. The coefficient vectors are a_k=mu(k) and b_k=log k. The exact block target is

    Z_I = 2/(T^2 ell^2) a^T C b.

For any t in [T,2T], let R_t be the real N-by-2 matrix with columns cos(t log k) and sin(t log k), k in I_T. Let P_t be the Euclidean orthogonal projection onto its column space. The choice t=t(T) can depend on the finite matrix: every estimate below is uniform throughout [T,2T]. This interval includes the three already selected ratios t/T=1.7568685,1.5234208,1.1902279. There is no frequency optimization in this note.

## 1. Unconditional projection estimate

For all sufficiently large T, uniformly for T<=t<=2T,

    lambda_min(R_t^T R_t) >> T,
    ||P_t b||_2 << (log T)/sqrt(T).                       (1)

Here all constants depend only on the fixed endpoints 21/20,27/20.

Proof of the log-vector estimate before projection. Write k=2j+1 and use e(x)=exp(2 pi i x). The phase

    phi(j) = t/(2 pi) log(2j+1)

has monotone derivative phi'(j)=t/[pi(2j+1)]. On the full index interval,

    20/(27 pi) <= phi'(j) <= 40/(21 pi).

This interval is contained in (1/5,4/5). Thus the derivative stays a fixed distance from every integer. The first-derivative exponential-sum estimate gives a uniform O(1) bound for the sum of k^(it) over every consecutive odd subinterval of I_T. The derivative is decreasing; apply the increasing-derivative formulation to -phi and conjugate. Partial summation with log k consequently gives

    S_1(t) := sum_{k in I_T} (log k) k^(it) = O(log T).  (2)

The endpoints stay sharp and no integral approximation to the odd lattice is taken.

Proof of Gram conditioning. Put S_2(t)=sum_{k in I_T} k^(2it). Trigonometric identities give exactly

    R_t^T R_t = (1/2) [[N+Re S_2, Im S_2],
                       [Im S_2, N-Re S_2]],

whose eigenvalues are (N+|S_2|)/2 and (N-|S_2|)/2. For the doubled phase 2 phi,

    (2 phi)''(j) = -4t/[pi(2j+1)^2],

so its absolute value is between fixed positive multiples of 1/T. The second-derivative estimate, on an interval of O(T) integers, gives S_2(t)=O(sqrt T), uniformly. Since N=3T/20+O(1), the Gram minimum is bounded below by a positive multiple of T. The doubled phase can meet a first-derivative alias; this proof intentionally uses the second derivative there, not a false alias-free assumption.

Finally z=R_t^T b=(Re S_1,Im S_1)^T and

    ||P_t b||_2^2 = z^T (R_t^T R_t)^(-1) z
                 << (log T)^2/T,

which proves (1). This is an exact orthogonal projection of the actual coefficient vector, with its finite Gram matrix retained.

## 2. Application to the unchanged actual matrix

The R27 source-valid RH estimate is

    ||C||_F^2 <<_eta X^(1+eta) Y (log X)^2,

where Y=sqrt X=T. It applies to the R28 square as a submatrix of a fixed proportional R27 rectangle, and therefore yields

    ||C||_op <= ||C||_F <<_eta T^(3/2+eta) log T.        (3)

No conjectural operator improvement is used. Also ||a||_2<=sqrt N<<sqrt T, without requiring cancellation in mu. Combining (1) and (3), for every eta>0,

    |2/(T^2 ell^2) a^T C P_t b|
       <<_eta T^(-1/2+eta),                            (4)

uniformly for T<=t<=2T. In particular the term is o(1) if eta is fixed below 1/2. In X notation it is O_eta(X^(-1/4+eta/2)). The exponent calculation is

    -2 + 1/2 + (3/2+eta) - 1/2 = -1/2+eta;

the two logarithms from (1) and (3) cancel ell^2 in the target normalization.

The exact identity, retaining the whole original target, is

    Z_I = 2/(T^2 ell^2) a^T C (I-P_t)b
        + 2/(T^2 ell^2) a^T C P_t b.                  (5)

Thus (4) controls the entire contribution from that input plane, including its image outside the plane. It is not an estimate only for P_t C P_t; there is no lost output cross term. The matrix C and its coefficients have not been altered. The residual in (5) remains an actual unproved signed correlation.

## 3. Consequence and limits

Large values of w_t^T C w_t at the measured t~T are compatible with a negligible contribution of the same input plane to the normalized fixed mu/log pairing. The log-cofactor input is nearly orthogonal to those oscillatory planes, and the available coarse RH matrix bound suffices to make their input contribution vanish.

This neither proves the residual in (5) small nor shows that a finite collection of planes exhausts the matrix. It does not provide a bound for the full global Z_T, the unbalanced cofactor region, other shift scales, frequencies outside this fixed range, or an increasing family of modes. A projection onto a union of planes requires control of its full Gram matrix; individual plane bounds must not simply be summed as if the planes were orthogonal. No claim is made that an empirically chosen fixed plane explains the entire observed small mu/log contraction.

The useful next analytic question is whether a controlled family of such planes leaves a residual that is accessible to an actual affine-prime estimate. Any such extension must preserve (5) and pay the joint Gram and residual costs. Further scans are not a consequence of this note.

## Primary input and review scope

The only new analytic tools are the first-derivative and second-derivative estimates. I checked Theorem 16.5, Corollary 16.6 and Theorem 16.7 in the author-hosted Montgomery–Vaughan draft, printed pages 6–8 (PDF pages 18–20, one-based):

https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf

The frozen primary extraction already exists at research-round13/minor-arc-source/sources/montgomery-vaughan-II-author-draft.txt; the relevant statements and first-derivative proof were reread, not the entire book. The R27 Frobenius bound is imported explicitly from JOINT_DISPERSION_TEST.md equations (23)–(25), not re-proved by a numerical fit. Formulae (1)–(5) above are this coordinator's derivation and await independent review. No new prime arrays, numerical scan, software dependency, formal proof certificate, or publication is claimed.
