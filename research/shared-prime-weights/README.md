# Common prime weights and zeta zero spacings

[Read the mathematical note](HANDOFF.md) or [open the four-page PDF](HANDOFF.pdf). The last section points to the full historical handoff and its quantitative supplement. The new note proves a property of a periodic arithmetic model for the fixed three-zero packet. Its shift-two calculation identifies precisely which primitive discrepancy estimate fails in that model.

Run `python3 check_common.py` from this directory. Its standard output reproduces [the exact receipt](receipt.json). The script checks primality, two atom rectangles, rational enclosures for the floors used in the second rectangle, and 120 local-product averages. The constructions use different finite twists and the rectangle tests make distinct assertions. The analytical limit is derived in the note.

To rebuild the PDF, use the repository's installed `tools/document-renderer` packages and Playwright, and run `node render.cjs` here. `DOCUMENT_NODE_MODULES` can point to the directory containing markdown-it and KaTeX. `PLAYWRIGHT_MODULE` and `PLAYWRIGHT_CHROMIUM_EXECUTABLE` can identify an installed Playwright package and browser binary. The final build rendered 109 mathematical expressions. All four PDF pages were visually checked.

The next arithmetic question is whether one can exclude the stated cancellation using the properties of a common sequence together with quantitative control of its individual pair counts. The actual von Mangoldt bounds and a strict improvement below half a mean zeta spacing remain open. Reverting this directory addition removes the companion note and its checker.
