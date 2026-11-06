# Protected trace moments and collision survival

The finite counterexample programme now preserves **all three conditions at once**. Two positive probability laws agree on the complete joint law of pair-difference counts and sorted nearest-neighbor gaps, agree on every protected trace moment, and have different scalar-heat survival probabilities.

- [The first possible grid size is ten](FIRST_SIZE.md). The separating time is at least one of two stated times.
- [Eleven gives one specified time](ELEVEN_POINT_PROTECTED_SURVIVAL.md). The protected matrix has exact rank 964 and adjoining the certified survival indicator raises the rank to 965.
- [Six-point rigidity](SIX_POINT_RIGIDITY.md) and [its independent integer checker](check_six.py) explain the earlier example’s obstruction.
- [Independent algebraic audit](n11-rank-review.md), [minimum-size audit](n10-review.md) and [Cayley/Sturm flow audit](n11-flow-review.md) give separately implemented checks.
- [One-value actual-zeta isolation test](MIDPOINT_ISOLATION.md) and [independent Hardy-function computation](midpoint-review.md) concern known finite pairs. The missing selected-height prime estimate is stated explicitly.
- [The Fable and Inoue source audit](fable-review.md) corrects the determinant phase and resolves a numerical rank ambiguity.
- [The prime-gap audit](prime-review.md) separates the external 182 manuscript from a replay of finite tuple obstructions.
- [Complete Markdown handoff](../../docs/handoff/HANDOFF_2026-11-06.md) and [complete PDF](../../output/pdf/HANDOFF_2026-11-06.pdf) include the reports after round 14 and all 705 previous historical pages.

The periodic-lift construction applies at arbitrarily large multiples of ten or eleven. The change in event probability may tend to zero. Asymptotic point-process separation, real zeta correlation laws, a density of isolated sub-half zeta gaps and an improved prime-gap theorem remain open.

## Replay

Python 3.12 with python-flint 0.8.0, NumPy and SymPy was used for the coordinator replay. The author’s initial runs also passed python-flint 0.9.0. These scripts use exact finite fields or Arb intervals. Each sign used to classify a polynomial is strict.

    python -m pip install python-flint==0.8.0 numpy sympy
    python check_six.py
    python check_protected_survival.py
    python check_first_size.py
    python check_sturm.py
    python check_sturm.py --ten
    python n11_symmetry_replay.py
    python n10_symmetry_replay.py
    python n10_small_minimality.py
    python n10_cycles_independent.py
    python trace_rank_replay.py
    python prime_tuple_cores.py
    python check_midpoint.py
    python check_midpoint.py --bits 224

The expected receipts are in this folder. Provider version labels may differ between the separate implementations. All finite counts, ranks, class labels and hashes use the documented fixed ordering. The midpoint JSON contains outward-rounded intervals, with the decisions agreeing at both tested precisions. Quantitative timing and algorithmic efficiency are outside the theorem.

Mathematical proof, independent computation and formal proof are separate verification stages. This checkpoint supplies the first two. Its priority relative to the full literature remains subject to an external review.

The submitted changes are a research packet on a separate branch. Removing the packet and the two handoff files reverts this checkpoint. The earlier archive is retained unchanged.
