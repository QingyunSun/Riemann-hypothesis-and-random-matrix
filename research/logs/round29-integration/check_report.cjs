// Check only the new editorial report; do not overwrite frozen source checks.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const root = path.resolve(__dirname, '../../..');
const katex = require(path.join(root, 'tools/document-renderer/node_modules/katex'));
const target = path.join(root, 'research/reports/dyson_round29.md');
const source = fs.readFileSync(target, 'utf8');
const errors = [];
let expressions = 0;
for (const m of source.matchAll(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g)) {
  expressions++;
  try {
    katex.renderToString(m[1] ?? m[2], { displayMode: m[1] !== undefined, throwOnError: true, strict: 'error' });
  } catch (e) { errors.push(String(e)); }
}
const targets = [];
for (const m of source.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)) {
  if (m[1].includes('://')) continue;
  const p = path.resolve(path.dirname(target), m[1].split('#')[0]);
  targets.push(path.relative(root, p));
  if (!fs.existsSync(p)) errors.push('Missing target: ' + p);
}
const controls = [...source].filter(c => c.charCodeAt(0) < 32 && ![9,10].includes(c.charCodeAt(0)));
const result = {
  status: errors.length || controls.length ? 'FAIL' : 'PASS',
  scope: 'New R29 editorial report syntax and local links only; no mathematical proof or visual PDF verification.',
  sha256: crypto.createHash('sha256').update(source).digest('hex'),
  mathExpressions: expressions,
  localLinks: targets,
  errors,
  controlBytes: controls.length
};
fs.writeFileSync(path.join(__dirname, 'REPORT_CHECK.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result, null, 2));
if (result.status !== 'PASS') process.exitCode = 1;
