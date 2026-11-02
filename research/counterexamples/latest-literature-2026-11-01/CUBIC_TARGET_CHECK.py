"""Exact finite projection-count checks for the cubic CUE/ACUE target."""

import json


def cumulant_counts(n, m, cyclic):
    occupied = set(range(n))

    def shift(amount):
        if cyclic:
            return {(j + amount) % (2 * n) for j in occupied}
        return {j + amount for j in occupied}

    overlap_m = len(occupied & shift(m))
    overlap_2m = len(occupied & shift(2 * m))
    triple_plus = len(occupied & shift(m) & shift(2 * m))
    triple_minus = len(occupied & shift(m) & shift(-m))
    return {
        "overlap_m": overlap_m,
        "overlap_2m": overlap_2m,
        "triple_plus": triple_plus,
        "triple_minus": triple_minus,
        "cubic": n - 2 * overlap_m - overlap_2m + triple_plus + triple_minus,
    }


records = []
for n in (3, 4, 5, 6, 10, 15, 20, 25):
    for m in range(1, n):
        line = cumulant_counts(n, m, False)
        circle = cumulant_counts(n, m, True)
        assert line["cubic"] == max(0, 2 * m - n), (n, m, line)
        assert circle["cubic"] == 0, (n, m, circle)
        if 2 * m > n:
            assert line["triple_plus"] == line["triple_minus"] == 0
            assert circle["triple_plus"] == circle["triple_minus"] == 0
            assert line["overlap_m"] == circle["overlap_m"] == n - m
            assert line["overlap_2m"] == 0
            assert circle["overlap_2m"] == 2 * m - n
        records.append({"N": n, "m": m, "CUE": line, "ACUE": circle})

targets = []
for n in (5, 10, 15, 20, 25, 50):
    m = 3 * n // 5
    cue = cumulant_counts(n, m, False)["cubic"]
    acue = cumulant_counts(n, m, True)["cubic"]
    assert 5 * cue == n and acue == 0 and 2 * m > n
    targets.append({"N": n, "m": m, "raw_CUE": cue, "raw_ACUE": acue,
                    "normalized_CUE": "1/5", "normalized_ACUE": "0"})

print(json.dumps({"status": "passed", "all_mode_cases": len(records),
                  "target_cases": len(targets), "targets": targets,
                  "counts": records,
                  "limitation": "Exact projection counts only; no arithmetic transfer certified."},
                 indent=2))
