const fs = require("fs");
const path = require("path");
const katex = require("/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Research/tools/document-renderer/node_modules/katex");
const bytes = fs.readFileSync(path.join(__dirname, "WEIGHTED_MELLIN_ENERGY.md"));
const badControls = [...bytes.entries()].filter(([i, b]) => b < 32 && b !== 10 && b !== 9);
const text = bytes.toString("utf8");
const errors = [];
let count = 0;
for (const m of text.matchAll(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g)) {
  count += 1;
  try {
    katex.renderToString(m[1] ?? m[2], {
      displayMode: m[1] !== undefined,
      throwOnError: true,
      strict: "error"
    });
  } catch (err) {
    errors.push({ index: m.index, error: String(err) });
  }
}
const result = {
  status: badControls.length === 0 && errors.length === 0 ? "PASS" : "FAIL",
  expressions: count,
  controlBytes: badControls,
  errors
};
const json = JSON.stringify(result, null, 2) + "\n";
fs.writeFileSync(path.join(__dirname, "syntax_checks.json"), json);
process.stdout.write(json);
if (result.status !== "PASS") process.exitCode = 1;
