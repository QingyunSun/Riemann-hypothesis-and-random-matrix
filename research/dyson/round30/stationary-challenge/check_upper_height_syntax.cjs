const fs = require("fs");
const path = require("path");
const katex = require("/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Research/tools/document-renderer/node_modules/katex");
if (typeof katex.renderToString !== "function") {
  const unavailable = {
    status: "UNAVAILABLE",
    reason: "The existing Dropbox-hosted KaTeX module does not export renderToString; syntax was not assessed.",
    observedExports: Object.keys(katex)
  };
  const json = JSON.stringify(unavailable, null, 2) + "\n";
  fs.writeFileSync(path.join(__dirname, "upper_height_syntax_checks.json"), json);
  process.stdout.write(json);
  process.exit(2);
}
const bytes = fs.readFileSync(path.join(__dirname, "UPPER_HEIGHT_BALANCED_CHECK.md"));
const badControls = [...bytes.entries()].filter(([, b]) => b < 32 && b !== 10 && b !== 9);
const errors = [];
let expressions = 0;
for (const m of bytes.toString("utf8").matchAll(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g)) {
  expressions += 1;
  try {
    katex.renderToString(m[1] ?? m[2], { displayMode: m[1] !== undefined, throwOnError: true, strict: "error" });
  } catch (err) {
    errors.push({ index: m.index, error: String(err) });
  }
}
const result = { status: badControls.length === 0 && errors.length === 0 ? "PASS" : "FAIL", expressions, controlBytes: badControls, errors };
const json = JSON.stringify(result, null, 2) + "\n";
fs.writeFileSync(path.join(__dirname, "upper_height_syntax_checks.json"), json);
process.stdout.write(json);
if (result.status !== "PASS") process.exitCode = 1;
