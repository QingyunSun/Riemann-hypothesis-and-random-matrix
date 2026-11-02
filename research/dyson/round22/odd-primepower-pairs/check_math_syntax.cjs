// Syntax-only check; this is neither a mathematical proof nor a PDF layout audit.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const katexPath = process.argv[2] || '/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Research/tools/document-renderer/node_modules/katex';
const katex = require(katexPath);
const report = path.join(__dirname, 'ALL_ODD_PRIMEPOWER_PAIRS.md');
const text = fs.readFileSync(report, 'utf8');
const errors = [];
let count = 0;
for (const match of text.matchAll(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g)) {
  count++;
  try {
    katex.renderToString(match[1] ?? match[2], {
      displayMode: match[1] !== undefined,
      throwOnError: true,
      strict: 'error',
    });
  } catch (error) {
    errors.push({ line: text.slice(0, match.index).split('\n').length, message: String(error) });
  }
}
const controls = [...text].map((c, i) => [c.charCodeAt(0), i]).filter(([c]) => c < 32 && ![9, 10].includes(c));
const result = {
  status: errors.length === 0 && controls.length === 0 ? 'PASS' : 'FAIL',
  scope: 'KaTeX syntax and control-byte check only; not mathematical or visual proof.',
  katexVersion: katex.version,
  mathExpressions: count,
  errors,
  controls,
  reportSha256: crypto.createHash('sha256').update(text).digest('hex'),
};
fs.writeFileSync(path.join(__dirname, 'math_syntax_checks.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result, null, 2));
if (result.status !== 'PASS') process.exitCode = 1;
