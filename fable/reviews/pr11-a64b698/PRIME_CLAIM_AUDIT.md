# Bounded evidence audit: the H2, H3 and H4 claims in NEW_RESULTS

Date: 2026-09-07. Repository: `galpha-ai/Alpha-devbox`. Immutable source commit: `a64b69802e8709e4cb8581440323ffbba574c9df`. The named Fable branch still pointed to this commit when queried during this audit.

This is a read-only evidence and source-code inspection, with local preservation of retrieved sources. No certificate was executed, no large tuple was regenerated or exhaustively checked, no numerical prime scan was run, and no primary-literature record comparison or full theorem verification was performed. In particular, this note does not certify three new unconditional records.

## Verdict

The repair of the old rounding objection is substantive: the committed tree now contains an actual exact-rational / Arb interval implementation, not just the old high-precision floating-point script. It is no longer accurate to dismiss the H2/H3 claim solely because `p9_certify_hp.py` uses ordinary mpmath and a slack factor. However, the current public commit does not contain the new certificate JSON files and replay logs cited by the repair report. The strongest responsible classification is a **candidate computer-assisted improvement with a concrete published repair implementation, author-reported successful certification, and incomplete independent verification in this audit**. H2 has more supporting admissibility evidence than H3; the new repair does not cover H4.

These are multi-prime interval claims. H2 concerns three primes, H3 four primes, and H4 five primes. They are not improvements of the consecutive-prime bound H1 = 186 and do not establish anything about actual zeta-zero correlations.

| Claim | What the committed evidence actually contains | Scope still needing verification |
|---|---|---|
| H2 <= 173,438 | Fixed 15,856-node tuple file; profile; original 399-row certificate; a new rational/Arb certifier; report and proposer journal giving M_15856 >= 8.00677408008999410774 without Berry–Esseen; author-reported two-implementation admissibility check over 1,847 primes. The separately committed Astra audit JSON also records a historical H2 tuple admissibility pass. | New exact certificate output is absent from this commit; no replay or full proof-chain verification here. Current record / novelty status was not checked. |
| H3 <= 13,859,802 | Fixed 923,601-entry tuple binary and checksum; original 399-row certificate; profile; the same new certifier and report giving M_923601 >= 12.00263034990571191492 without Berry–Esseen. | The repair explicitly covers the M_k part only and says the H3 tuple was not rechecked. The announcement's older two-implementation admissibility claim is not a new verification. The cited new H3 JSON and log are absent from this commit. |
| H4 <= 1,120,662,828 | Historical `p9_exact_cert_k56000000.json`, with 400 exact hexadecimal profile nodes and values, 399 certificate rows, `arb_precision_bits: 200`, `PASS: true`, and numeric lower bound 16.065482942209332. The announcement specifies the first 56,000,000 primes above k, endpoints 56,000,003 and 1,176,662,831. | No H4 application of the new D1 repair is reported. No H4 tuple/count-anchor replay or outward-enclosure verification was performed here. The serialized chain values are ordinary JSON numbers, not themselves the new exact-rational endpoint certificate. |

## Rounding repair: exact scope

The original `p9_certify_hp.py`, lines 19–20 and 79–171, sets `mp.dps = 50` and `SAFE = 1 + 10^-30`. The repair report confirms Astra's earlier objection: this is not outward-rounded interval arithmetic.

The new `overnight/fable/scripts/r1_h2_interval_cert.py` is materially different:

- `ArbBackend`, lines 98–157, converts exact fractions through `fmpq`, checks enclosure, evaluates interval transcendental functions and extracts exact dyadic lower/upper endpoints.
- The polynomial integrals, profile data and assembly use `fractions.Fraction`. The profile's float64 values are treated as fixed exact dyadic data; their numerical optimization need not be reproduced to verify the fixed test function.
- `assemble`, lines 406–430, uses upper bounds for tail probabilities and forms `max(0, 1-beta_upper)` before exact summation, which is the correct lower-bound direction in the written layer-cake argument.
- The mpmath interval implementation is explicitly a cross-check with a guard band; the report states that Arb is the backend with the claimed rigorous semantics.

I read the written layer-cake / Chernoff derivation and inspected the arithmetic path. This establishes that a genuine repair implementation is published. It does not substitute for running and independently validating its certificate or auditing all implementation details. The report's Maynard and Bombieri–Vinogradov formulations are expressly described as recalled rather than source-checked. That is a verification gap, not an additional unproved mathematical conjecture being imposed by the proposed result.

## Missing public artifacts and review status

The complete GitHub recursive tree has 685 entries and `truncated: false`. It contains no `research/riemann-rmt/overnight/fable/data/` files. In particular, the following cited artifacts are absent:

- `data/h2_k15856_interval_cert.json`
- `data/h3_k923601_interval_cert_Mk_only.json`
- `data/r1_h2_interval_cert_run.log`, `data/r1_h2_crosscheck.log`
- `data/h2_k15856_replay_arb.json` and associated replay logs
- `data/refute_D1_rigour.log`

The root `.gitignore` contains `data/`, which is consistent with this omission. The tree evidence establishes the absence; the ignore rule is a plausible explanation. The reports and scripts remain published, so this is an output/provenance gap rather than proof that the claimed runs failed or that replay is impossible.

The committed `refute_D1_rigour.py` describes useful checks: an independent exact layer, numerical characteristic-function checks, exact reassembly from upper-rounded certificate decimals, and tuple admissibility. Its header expressly says these are attempts to break the certificate, not a proof. Its target output is in the omitted `data/` directory. The available D1 harness record is the proposer's successful structured result. The current `CLAIMS.md`, lines 38–43, also preserves an earlier warning that the first D1 draft had not received its adversarial pass because of credit exhaustion. I found no later D1-specific successful refuter verdict in the committed harness journals inspected, and no D1 withdrawal or refutation. Therefore neither “the repaired H2 claim was refuted” nor “this audit found a complete committed independent refuter pass” is supported.

## Exact source locations

All repository paths below are relative to `research/riemann-rmt/` at the immutable commit above. Copies of the principal sources are retained beside the original audit in the local `incoming-new-results-a64b698/prime-claim-audit/sources/` folder. This public copy contains the audit and source hashes; it does not duplicate those source bodies.

- `NEW_RESULTS.md`, section 2.3: the outward-facing three-record statement.
- `H2_H3_record_announcement.md`, statements, hypothesis chain and verification ledger.
- `overnight/fable/r1_h2_interval_cert.md`, summary D1.3–D1.8; sections 3.6, 4, 5 and 8.
- `overnight/fable/scripts/r1_h2_interval_cert.py` and `r1_h2_reference_p9_exact_cert_scratchpad_copy.py`.
- `overnight/fable/scripts/refute_D1_rigour.py`.
- `overnight/fable/CLAIMS.md`, D1 rows and lines 38–43.
- `overnight/fable/harness_logs/wf_7b8483c5-a9b/journal.jsonl`, D1 proposer result (`agentId: a025c1cf3bfdddedc`).
- `handoff/astra-2026-09-05/audit_results.json`, historical H2 tuple check; its top-level scope says no prime-gap proof certified.
- `p9_exact_cert_k15856.json`, `p9_exact_cert_k923601.json`, `p9_exact_cert_k56000000.json`.
- `p9_tuple_k15856.npy`, `p9_tuple_k923601.npy` and `p9_tuple_k923601.npy.sha256`.

The immutable announcement can be opened at [GitHub](https://github.com/galpha-ai/Alpha-devbox/blob/a64b69802e8709e4cb8581440323ffbba574c9df/research/riemann-rmt/H2_H3_record_announcement.md); the more carefully scoped repair is [here](https://github.com/galpha-ai/Alpha-devbox/blob/a64b69802e8709e4cb8581440323ffbba574c9df/research/riemann-rmt/overnight/fable/r1_h2_interval_cert.md).

## Source hashes

SHA256 of retrieved copies:

```text
0c2bebc885a4250015b5a81270f41afeda4dbc4dd8afb7454cd3229fb3774223  H2_H3_record_announcement.md
f3bee32666e254142989ee85c54ef0eba4dc087f1879ade019d2bd64f84a5e77  r1_h2_interval_cert.md
9dd0871f172fabe8a623cf1688b171430139af5ea279ed2472016f9635178591  CLAIMS.md
aae6351013128f171890a4d94cf681fd092aed55400cf7791c2019179585b789  r1_h2_interval_cert.py
8f75b02645818551007334f55d25944e4af0aeda69d5eaf7e53c8732eabf797c  refute_D1_rigour.py
a61099ba387e3cd59374993c670b4303872eb739d7b1f8eb349c4aecee7b50fc  r1_h2_reference_p9_exact_cert_scratchpad_copy.py
d0fb7837546ea0870ab7f55281dc8be64b2b902ce0140f40107cfede5e619a33  journal.jsonl
5e8feee1123b29408dc852bf9afed3f55561a0088fbe27942c5529efc7906f6b  p9_exact_cert_k56000000.json
692bc6ef127407a5cf73842052a3409c606ff42de3fa57bea1ac5d41aa19111b  p9_certify_hp.py
1dd5f2e8461ce144733ee6769a008be34cd5c7cbd285d2acbf3c71ca7c9f9412  p9_tuple_k923601.npy.sha256
```

The repository tree and the older Astra audit JSON are also preserved as provenance evidence. No claim of independent theorem certification follows from their preservation.
