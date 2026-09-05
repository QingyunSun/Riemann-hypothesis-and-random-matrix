#!/usr/bin/env python3
"""Compare signed FLINT products with independent Python integer convolution.

The original PrimeGaps186 startup checks run unchanged. This program never
substitutes a different multiplication routine into the official certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import platform
import random
import sys
import time
from pathlib import Path

import flint
from flint import fmpz_poly


def classical(a: list[int], b: list[int]) -> list[int]:
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def cases():
    yield [], []
    yield [0], [1, -1]
    yield [1, -1, 0, 1], [0, -3, 2]
    # Include limb boundaries and the original 509/510-bit failure.
    for n in (1, 2, 3, 7, 16, 31, 64, 129):
        for bits in (1, 63, 64, 65, 127, 255, 509, 510, 511, 512, 1023, 1024):
            a = (1 << bits) - 1
            b = (1 << (bits + 1)) - 1
            for signs in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                yield [signs[0] * a] * n, [signs[1] * b] * n
    rng = random.Random(186390509)
    for _ in range(80):
        n, m = rng.randrange(1, 100), rng.randrange(1, 100)
        bits = rng.choice((63, 64, 127, 255, 509, 510, 1023, 2047))
        a = [rng.getrandbits(bits) * rng.choice((-1, 1)) for _ in range(n)]
        b = [rng.getrandbits(bits) * rng.choice((-1, 1)) for _ in range(m)]
        yield a, b


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--official-script", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit("Use a new output path; receipts are never overwritten.")
    started = time.monotonic()
    report = {
        "python": sys.version,
        "executable": sys.executable,
        "platform": platform.platform(),
        "python_flint": flint.__version__,
        "flint": flint.__FLINT_VERSION__,
        "flint_module": flint.__file__,
        "official_source_sha256": hashlib.sha256(args.official_script.read_bytes()).hexdigest(),
        "checks": [],
        "full_products_checked": 0,
        "truncated_products_checked": 0,
        "passed": False,
    }
    try:
        spec = importlib.util.spec_from_file_location("official_prime186", args.official_script)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        module.check_flint_signed_fft()
        report["checks"].append("original signed FFT regression passed unchanged")
        module._cap_check_environment()
        report["checks"].append("original floating point environment check passed unchanged")
        for a, b in cases():
            expected = classical(a, b)
            p, q = fmpz_poly(a), fmpz_poly(b)
            if p * q != fmpz_poly(expected):
                raise ArithmeticError(f"Full convolution mismatch at case {report['full_products_checked']}")
            report["full_products_checked"] += 1
            for cutoff in sorted({0, 1, len(expected) // 2, len(expected), len(expected) + 3}):
                if p.mul_low(q, cutoff) != fmpz_poly(expected[:cutoff]):
                    raise ArithmeticError(f"Truncated convolution mismatch at cutoff {cutoff}")
                report["truncated_products_checked"] += 1
        report["checks"].append("independent classical integer convolution comparisons passed")
        report["passed"] = True
    except Exception as exc:
        report["error"] = f"{type(exc).__name__}: {exc}"
    report["seconds"] = time.monotonic() - started
    report["scope"] = "Finite regression tests; not a proof of all library arithmetic or any prime-gap theorem."
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
