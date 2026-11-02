// Syntax only; this does not validate analytic inequalities.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const katex = require('/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Research/tools/document-renderer/node_modules/katex');
const file = path.join(__dirname, 'ZERO_MOMENT_APPLICABILITY.md');
const text = fs.readFileSync(file, 'utf8');
let count = 0;
const errors = [];
for (const match of text.matchAll(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g)) {
  ++count;
  try { katex.renderToString(match[1] ?? match[2], {displayMode: match[1] !== undefined, throwOnError: true, strict: 'error'}); }
  catch (error) { errors.push({line: text.slice(0, match.index).split('\n').length, error: String(error)}); }
}
const controls = [...text].map((c,i)=>[c.charCodeAt(0),i]).filter(([c])=>c<32 && ![9,10].includes(c));
const result = {status: errors.length || controls.length ? 'FAIL' : 'PASS', mathExpressions: count,
  errors, controls, katexVersion: katex.version, reportSha256: crypto.createHash('sha256').update(text).digest('hex'),
  scope: 'Mathematical syntax only; ordinary argument and source applicability reviewed separately.'};
fs.writeFileSync(path.join(__dirname, 'math_syntax_checks.json'), JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
if (result.status !== 'PASS') process.exitCode=1;
