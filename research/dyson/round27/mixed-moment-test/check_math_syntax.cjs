const fs = require('fs');
const path = require('path');
const katex = require(process.argv[2] || '/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Research/tools/document-renderer/node_modules/katex');
const text = fs.readFileSync(path.join(__dirname, 'MIXED_MOMENT_DIRECTION_TEST.md'), 'utf8');
const expressions = [...text.matchAll(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g)];
const errors = [];
expressions.forEach((m, i) => {
  try { katex.renderToString(m[1] ?? m[2], {displayMode: m[1] !== undefined, throwOnError: true, strict: 'ignore'}); }
  catch (error) { errors.push({i, error: String(error)}); }
});
const controls = [...text].filter(c => c.charCodeAt(0) < 32 && c !== '\n' && c !== '\t').map(c => c.charCodeAt(0));
const result = {count: expressions.length, errors, control_bytes: controls, status: errors.length || controls.length ? 'FAIL' : 'PASS'};
fs.writeFileSync(path.join(__dirname, 'math_syntax_check.json'), JSON.stringify(result, null, 2) + '\n');
process.stdout.write(JSON.stringify(result) + '\n');
if (result.status !== 'PASS') process.exitCode = 1;
