# CUE selected-minimum background, Round14

The complete ordinary-proof draft is `SELECTED_CUE_BACKGROUND.md`. For midpoint background B_i, it proves the finite-N truncated moment bound E sum_{gap_i<=epsilon} B_i <= N^6 epsilon^3/18. The checked CUE minimum-gap law then gives B_min/N^2 tight. The existing quantified finite-circle heat lemma yields relative depth error O_p(N^(-2/3)).

This strengthens the programme's earlier qualitative finite-CUE approximation. It is not a general-beta theorem, a distributional convergence-rate estimate, an asserted literature novelty, or a zeta transfer.

`check_selected_background.py` uses standard-library exact arithmetic and one symbolic N=3 Laurent determinant calculation. Its saved JSON is PASS. Run it with Python3; it writes the adjacent check JSON. There is no grid scan or Monte Carlo experiment.

`source_receipt.json` pins the inherited finite deterministic proof and the directly checked primary extreme-gap source. Source PDFs/text are evidence for local review; they need not be republished. Independent review artifacts belong outside the frozen author manifest.
