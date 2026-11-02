"""Bounded publication checks for the renewed counterexample/literature package.

This checks saved replays, source receipts, local links and math syntax. It does
not repeat the experiments or certify analytic proofs. Run from the repo root.
"""

from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = Path(__file__).resolve().parent
LIT = PACKAGE / "latest-literature-2026-11-01"
PAIR = PACKAGE / "pair-matched-flow"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


replays = [
    (PAIR / "AGENT_PAIR_CHECK_OUTPUT.json", PAIR / "ROOT_PAIR_REPLAY.json"),
    (LIT / "CUBIC_TARGET_CHECK_OUTPUT.json", LIT / "ROOT_CUBIC_REPLAY.json"),
    (LIT / "CLIPPED_GRAM_CHECK_OUTPUT.json", LIT / "ROOT_CLIPPED_GRAM_REPLAY.json"),
]
for original, replay in replays:
    assert json.loads(original.read_text()) == json.loads(replay.read_text()), original

receipt = json.loads((PAIR / "AGENT_PAIR_RECEIPT.json").read_text())
for row in receipt["artifacts"]:
    p = ROOT / row["path"]
    assert p.stat().st_size == row["bytes"] and digest(p) == row["sha256"], p

python_files = sorted(PACKAGE.rglob("*.py"))
for p in python_files:
    compile(p.read_text(), str(p), "exec")

math = []
checked_links = 0
markdown_files = sorted(PACKAGE.rglob("*.md"))
for p in markdown_files:
    text = re.sub(r"```.*?```", "", p.read_text(), flags=re.S)
    for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
        if re.match(r"(?:https?://|mailto:|#)", target):
            continue
        file_part = unquote(target.split("#", 1)[0].strip("<>"))
        if file_part:
            assert (p.parent / file_part).exists(), (p, target)
            checked_links += 1
    for pattern, display in ((r"\\\[(.*?)\\\]", True), (r"\\\((.*?)\\\)", False), (r"\$\$(.*?)\$\$", True)):
        for match in re.finditer(pattern, text, flags=re.S):
            math.append({"path": str(p.relative_to(ROOT)), "latex": match.group(1), "display": display})

node_code = r'''
const fs = require('fs');
const katex = require('./tools/document-renderer/node_modules/katex');
const items = JSON.parse(fs.readFileSync(0, 'utf8'));
const errors = [];
for (const item of items) {
  try { katex.renderToString(item.latex, {throwOnError: true, strict: 'ignore', displayMode: item.display}); }
  catch (error) { errors.push({path: item.path, latex: item.latex, error: String(error)}); }
}
process.stdout.write(JSON.stringify({version: katex.version, expressions: items.length, errors}));
'''
render = subprocess.run(["node", "-e", node_code], input=json.dumps(math), text=True,
                        cwd=ROOT, capture_output=True, timeout=60, check=True)
syntax = json.loads(render.stdout)
assert not syntax["errors"], syntax["errors"]

print(json.dumps({
    "status": "PASS",
    "python": sys.version.split()[0],
    "python_files_parsed": len(python_files),
    "markdown_files": len(markdown_files),
    "local_markdown_links": checked_links,
    "math_syntax": syntax,
    "math_delimiters_covered": ["\\[...\\]", "\\(...\\)", "$$...$$"],
    "replayed_json_pairs": [{"original": str(a.relative_to(ROOT)), "replay": str(b.relative_to(ROOT)),
                              "equal_json": True} for a, b in replays],
    "pair_receipt_hashes_verified": len(receipt["artifacts"]),
    "limitations": ["No formal proof certification", "No external full Lean rebuild",
                    "No remote-link availability assertion", "No performance benchmark claim",
                    "No whole historical archive rescan"]
}, indent=2))
