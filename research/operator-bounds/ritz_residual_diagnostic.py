"""One finite two-dimensional Ritz test, with no positivity assumption on K.

Uses the fixed rational symmetric-prime trial at L=100000. This is a numerical
direction diagnostic, not an asymptotic theorem or an interval certificate.
"""
from pathlib import Path
import hashlib
import json
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research/residual-gram"))
from arithmetic_operator import make_A, prime_powers


def run() -> dict:
    started = time.monotonic()
    length = 100000
    ell = 16 / 15
    n = np.arange(1, length + 1)
    mass = np.log(n) / np.log(length)
    divisor = np.ones(length)
    feature = np.zeros(length)
    for power, exponent in prime_powers(length):
        divisor[power - 1 :: power] *= (ell + exponent - 1) / exponent
        if exponent == 1:
            feature[power - 1 :: power] += (np.log(power) / np.log(length)) ** 2
    f = np.polynomial.polynomial.polyval(mass, np.array([145, 3, -116, 71, -6]) / 100)
    g = np.polynomial.polynomial.polyval(mass, np.array([-563, 1682, -2479, 1751, -488]) / 100)
    u = divisor * (f + g * feature) / np.sqrt(n)
    u /= np.linalg.norm(u)
    operator = make_A(length)

    def apply_k(x: np.ndarray) -> np.ndarray:
        ax = operator @ x
        atx = operator.T @ x
        return operator.T @ ax + (operator @ ax + operator.T @ atx) / 2

    ku = apply_k(u)
    value = float(u @ ku)
    residual = ku - value * u
    norm = float(np.linalg.norm(residual))
    assert norm > 0
    v = residual / norm
    b = float(v @ apply_k(v))
    ritz = np.array([[value, norm], [norm, b]])
    eigenvalues, eigenvectors = np.linalg.eigh(ritz)
    top = float((value + b + np.sqrt((value - b) ** 2 + 4 * norm**2)) / 2)
    new_u = u * eigenvectors[0, -1] + v * eigenvectors[1, -1]
    actual = float(new_u @ apply_k(new_u) / (new_u @ new_u))
    assert abs(u @ v) < 1e-12
    assert abs(actual - top) < 1e-11
    assert abs(eigenvalues[-1] - top) < 1e-11
    assert top >= value
    # The same Ritz formula must work for an indefinite self-adjoint matrix.
    control = np.array([[-2.0, 1.0], [1.0, 0.0]])
    assert abs(np.linalg.eigvalsh(control)[-1] - (-1 + np.sqrt(2))) < 1e-14
    source = ROOT / "research/residual-gram/arithmetic_operator.py"
    return {
        "status": "finite numerical Ritz diagnostic; no interval or asymptotic certification",
        "L": length, "ell": "16/15", "theta": 1,
        "operator_source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "initial_rayleigh": value, "residual_norm": norm,
        "residual_rayleigh": b, "compressed_matrix": ritz.tolist(),
        "ritz_top": top, "direct_new_vector_rayleigh": actual,
        "orthogonality_error": float(abs(u @ v)),
        "initial_margin": value / (2 * np.pi**2) - 0.25,
        "new_margin": top / (2 * np.pi**2) - 0.25,
        "margin_gain": (top - value) / (2 * np.pi**2),
        "threshold": float(np.pi**2 / 2),
        "seconds": time.monotonic() - started,
        "transfer_status": "K_L u contains prime-removal and cutoff-dependent sums; the fixed H=f+gS2 transfer does not automatically cover it",
    }


if __name__ == "__main__":
    result = run()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
