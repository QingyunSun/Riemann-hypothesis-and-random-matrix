// Render the companion note with the repository's Markdown and KaTeX packages.
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const {pathToFileURL} = require('node:url');
const deps = process.env.DOCUMENT_NODE_MODULES || path.resolve(__dirname, '../../tools/document-renderer/node_modules');
const md = require(path.join(deps, 'markdown-it'))({html: false});
const katex = require(path.join(deps, 'katex'));
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');

function renderMarkdown(source) {
  const formulas = [];
  const reserve = (tex, displayMode) => {
    const html = katex.renderToString(tex.trim(), {displayMode, output: 'html', throwOnError: true});
    const id = formulas.push({html, displayMode}) - 1;
    return `MATHRESERVATION${id}END`;
  };
  if (source.includes('MATHRESERVATION')) throw Error('Formula placeholder already in Markdown');
  const masked = source.replace(/\\\[([\s\S]*?)\\\]/g, (_, tex) => '\n\n' + reserve(tex, true) + '\n\n')
    .replace(/\\\(([\s\S]*?)\\\)/g, (_, tex) => reserve(tex, false));
  let html = md.render(masked);
  for (const [i, f] of formulas.entries()) {
    const token = `MATHRESERVATION${i}END`;
    html = f.displayMode ? html.replace(`<p>${token}</p>`, `<div class="formula">${f.html}</div>`) : html.replace(token, f.html);
  }
  if (html.includes('MATHRESERVATION')) throw Error('Unresolved formula placeholder');
  return {html, formulaCount: formulas.length};
}

async function main() {
  const source = fs.readFileSync(path.join(__dirname, 'HANDOFF.md'), 'utf8');
  const {html, formulaCount} = renderMarkdown(source);
  const fontDir = pathToFileURL(path.join(deps, 'katex/dist/fonts') + '/').href;
  const mathCss = fs.readFileSync(path.join(deps, 'katex/dist/katex.min.css'), 'utf8').replaceAll('url(fonts/', `url(${fontDir}`);
  const styles = `@page{size:A4;margin:22mm 22mm 23mm}*{box-sizing:border-box}body{margin:0;color:#192b32;font:11pt/1.5 'Times New Roman',serif}h1,h2{font-family:Arial,sans-serif;line-height:1.2;color:#183c48;break-after:avoid}h1{font-size:27pt;max-width:96%;padding-bottom:12px;border-bottom:2px solid #507782}h2{font-size:17pt;margin:25px 0 12px}p{margin:0 0 10px;orphans:3;widows:3}li{margin-bottom:8px}a{color:#165769;text-decoration:none}code{font:9pt Menlo,monospace} .formula{margin:10px 0;break-inside:avoid}.katex{font-size:1.04em}.katex-display{margin:.5em 0}header{font:9pt Arial;color:#53717c}`;
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'common-weight-note-'));
  const pageFile = path.join(dir, 'note.html');
  fs.writeFileSync(pageFile, `<!doctype html><html lang="en"><meta charset="utf-8"><title>Common prime weights and zeta zero spacings</title><style>${mathCss}${styles}</style><body><header>7 November 2026 · Riemann zeros and random matrices</header>${html}</body></html>`);
  const browser = await chromium.launch({headless: true, executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE || undefined});
  try {
    const page = await browser.newPage({viewport: {width: 620, height: 930}});
    await page.goto(pathToFileURL(pageFile).href);
    await page.emulateMedia({media: 'print'});
    await page.evaluate(() => document.fonts.ready);
    const overflow = await page.evaluate(() => [...document.querySelectorAll('.formula')].filter(el => el.scrollWidth > el.clientWidth + 2).map(el => el.textContent));
    if (overflow.length) throw Error(`Overflow in ${overflow.length} formulas`);
    const footerTemplate = '<div style="font:9px Arial;color:#5a727c;width:100%;padding:0 22mm;display:flex;justify-content:space-between"><span>Common prime weights · Research handoff</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>';
    await page.pdf({path: path.join(__dirname, 'HANDOFF.pdf'), preferCSSPageSize: true, printBackground: true, displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate, tagged: true, outline: true});
    console.log(JSON.stringify({formulaCount, overflow}));
  } finally {
    await browser.close();
    fs.rmSync(dir, {recursive: true, force: true});
  }
}
main().catch(error => {console.error(error); process.exit(1);});
