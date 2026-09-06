# Final v2 visual review and inherited page coverage

Reviewer: Aquinas (`/root/yau_flow`). Date: 2026-09-05.

**Status: PASS for the complete final body's visual coverage, through exact inheritance plus individual inspection of every unmatched page.** The v1 table truncation and blank-page defects are repaired. No remaining material clipping, overlap, hidden table text, unreadable glyph, or broken report boundary was observed in the completed checks below.

Final PDF: `ASTRA_ROUNDS_6_14_HANDOFF.pdf`, **313 pages**.

Verified current-file SHA-256:

`1092c6f1e81a9c13bc3106ffe3943f15ff742c7c794729c99233c8ebc805033a`

The original v1 render receipt identifies the 314-page PDF as:

`137d90f269dd91df9e6f6d7b96dbcbebf334a6f091465442403a8faba015b987`

This is an artifact-layout and visible-content review. It does not upgrade any mathematical result's proof status, novelty status, numerical certification, or scope.

## Exact comparison and reproducibility

`compare_page_bodies.py` checks both directories' page counts against their rendering receipts, requires consecutive page-image numbering, and recomputes the current final PDF hash. It hashes the RGB pixel bytes and dimensions of every page body, without resampling, numerical tolerance, or text normalization.

The rendered pages are 703 by 994 pixels at 85 dpi. The crop is the entire width and vertical pixel interval `[54, 940)`: 45 PDF points removed at each end, rounded outward to 54 pixels. The comparison therefore excludes running headers and footers, including changed page-count numerals. It does not exclude any horizontal portion of the page body. Individual visual inspections use the complete uncropped images.

Results:

- **263 final bodies match a unique old body exactly.** There are no ambiguous hash matches.
- **50 final bodies do not match exactly.** Every one was reopened and visually inspected individually at the original render resolution.
- The exact matches before the removed blank page are v2/v1 pages 1–12, 18–69, and 76–199. All later exact matches map v2 page `n` to v1 page `n+1`; the full disjoint ranges and every page-level mapping are in the JSON.
- Eleven unmatched pages have substantial reflow: **13–17 and 70–75**.
- The remaining **39 unmatched pages** differ from their aligned v1 page `n+1` in only **1–8 RGB pixels per page**, 117 pixels in total, with maximum absolute channel difference 34. These remain classified as *unmatched*, not as pixel-identical pages. The tiny raster differences were still covered by individual visual inspection.

For unmatched-page diagnostics only, the script infers a candidate offset from the next proved exact match, or the last preceding exact match at the end. This diagnostic alignment never upgrades an unmatched page to an exact match and is not used as a substitute for visual inspection.

Reproduce from any working directory:

```sh
python3 '/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Local-Archive/rounds6-14-pdf-qa/v2/compare_page_bodies.py'
```

Evidence hashes:

- Script: `2a5d2bffefed08c2cee44e783bc8817db2b6b646528c6772e2f5ff10baa489fb`.
- `page_body_comparison.json`: `a8d7ac3fddc22ab6e6ea0353d299a4ecd1b6977f66b88eb382fd2ac97df8da4b`.

The JSON records all 627 input PNG hashes, cropped-body hashes, complete mappings, unmatched pages, dimensions and difference diagnostics. Pillow is required by the script. No PDF or input PNG is altered.

## Complete visual coverage

The retained v1 reviews cover every original page via contact sheets: Aquinas pages 1–160, Euclid pages 161–314, with their separately listed full-page samples. The 263 exact final-body matches inherit those observations. The header/footer-only v1 page 200 is not inherited by any final page.

Individually inspected **all 50 unmatched v2 pages**:

**13, 14, 15, 16, 17, 70, 71, 72, 73, 74, 75, 200, 203, 204, 208, 209, 211, 215, 217, 220, 226, 227, 239, 242, 244, 252, 257, 264, 266, 267, 268, 269, 271, 272, 278, 282, 285, 287, 289, 290, 291, 292, 293, 296, 299, 303, 304, 306, 309, 313.**

Also inspected v2 pages **199 and 201** individually, completing the three-page boundary check around page 200. Thus this reviewer reopened 52 complete final page images. This is not a claim to have individually reopened all 313 final images; complete body coverage uses the exact inheritance described above.

The v1 review notes remain unchanged:

- `../v1/visual-review-aquinas.md`, SHA-256 `413e08a473a59f19c7acada56a3b88a0053cfc921e385dc0615118b7561a3d7a`.
- `../v1/visual-review-euclid.md`, SHA-256 `156e3906818a97fb91eaeff7b160783e5b8791b0d492f30c590cc2a0b1408f96`.

## Specific repairs and observations

**Page 70:** All three formerly truncated rows are now complete within the table. The Montgomery row shows both absolute-value expressions, its negative exponent and RH/low-band qualifications. The higher-correlation row shows the complete summed absolute-value support condition with threshold 2. The quantitative row shows the full lower bound, including both subtractions and its GRH qualifier. The remaining rows, citations and following paragraph are visible. The wrapping of the last formula inside its cell loses no term.

**Pages 71–75:** The following report text reflows cleanly after the repaired table. Display equations, boxed obligations, lists and closing paragraphs remain legible, with no collisions or clipping.

**Pages 13–17:** The presentation-repair explanation is legible, and the source index runs continuously through entries 1–69. Repeated table headers, long source titles and row divisions are intact.

**Pages 199–201:** Report 39 ends on page 199; report 40 begins immediately on page 200 with its heading, provenance, verdict and opening argument. Page 201 continues normally. The old blank page is removed without an observed omitted paragraph or broken boundary.

**Other inspected pages:** Dense formulas, boxed inequalities, code blocks, source hashes, long report headings and continued tables fit inside the page. Sparse closing pages remain intentional consequences of starting each complete report on a new page. Such whitespace is not treated as missing content or a failure.

Euclid independently compared the repaired table with its raw source and inspected the same report boundary; see `table-semantic-review-euclid.md`. That separate check also records verification of all 69 embedded source bodies and 297 associated Git objects. This review does not claim to have independently rerun that source-coverage checker.

The comparison deliberately excludes running header/footer pixels. Their layout is visible on all 52 pages reopened here; all-page metadata, font and mechanical checks are separately retained in this folder and by the coordinator. Original Markdown remains the preferred machine-readable record of the mathematics; PDF text-extraction artifacts are not conflated with visible missing glyphs.

No source report, Markdown assembly, renderer, PDF, or input page image was edited by this reviewer. Only the comparison script, its JSON result and this review were written.
