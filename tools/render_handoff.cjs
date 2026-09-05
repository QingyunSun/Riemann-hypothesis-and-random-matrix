const fs=require('fs');
const path=require('path');
const MarkdownIt=require('./document-renderer/node_modules/markdown-it');
const katex=require('./document-renderer/node_modules/katex');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const root=path.resolve(__dirname,'..');
const input=path.resolve(process.argv[2] || path.join(root,'docs/handoff/ASTRA_PUBLIC_RESEARCH_HANDOFF.md'));
const output=path.resolve(process.argv[3] || path.join(root,'output/pdf/ASTRA_PUBLIC_RESEARCH_HANDOFF.pdf'));
fs.mkdirSync(path.join(root,'tmp'),{recursive:true});
fs.mkdirSync(path.dirname(output),{recursive:true});
const mathErrors=[];
function tex(src,display){
  try{return katex.renderToString(src,{displayMode:display,throwOnError:true,strict:false,trust:false,output:'html'});}
  catch(e){mathErrors.push({source:src,error:String(e)});return '<span class="math-fallback">'+escapeHtml(src)+'</span>';}
}
function escapeHtml(s){return s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');}
const md=new MarkdownIt({html:true,linkify:false,typographer:false,breaks:false});
md.inline.ruler.before('escape','math_inline',(state,silent)=>{
  const pos=state.pos; let opener,closer;
  if(state.src.startsWith('\\(',pos)){opener='\\(';closer='\\)';}
  else if(state.src[pos]==='$'&&state.src[pos+1]!=='$'){opener='$';closer='$';}
  else return false;
  let end=state.src.indexOf(closer,pos+opener.length);
  if(end<0 || (opener==='$' && state.src.slice(pos+1,end).includes('\n')))return false;
  const content=state.src.slice(pos+opener.length,end);
  if(!content.trim())return false;
  if(!silent){const t=state.push('math_inline','math',0);t.content=content;}
  state.pos=end+closer.length;return true;
});
md.renderer.rules.math_inline=(tokens,i)=>tex(tokens[i].content,false);
md.block.ruler.before('fence','math_block',(state,start,end,silent)=>{
  let line=state.src.slice(state.bMarks[start]+state.tShift[start],state.eMarks[start]).trim();
  let open,close;
  if(line.startsWith('$$')){open='$$';close='$$';}
  else if(line.startsWith('\\[')){open='\\[';close='\\]';}
  else return false;
  let content=line.slice(open.length);let last=start;let at=content.indexOf(close);
  if(at>=0)content=content.slice(0,at);
  else {
    let found=false;
    for(last=start+1;last<end;last++){
      let next=state.src.slice(state.bMarks[last],state.eMarks[last]);let j=next.indexOf(close);
      if(j>=0){content+='\n'+next.slice(0,j);found=true;break;}
      content+='\n'+next;
    }
    if(!found)return false;
  }
  if(silent)return true;
  let t=state.push('math_block','math',0);t.content=content.trim();t.map=[start,last+1];t.block=true;
  state.line=last+1;return true;
},{alt:['paragraph','reference','blockquote','list']});
md.renderer.rules.math_block=(tokens,i)=>'<div class="display-math">'+tex(tokens[i].content,true)+'</div>\n';
let source=fs.readFileSync(input,'utf8');
let html=md.render(source);
let headingNumber=0,toc=[];
html=html.replace(/<(h[12])>([\s\S]*?)<\/\1>/g,(all,tag,content)=>{
  const id='section-'+(++headingNumber);toc.push({id,tag,text:content.replace(/<[^>]+>/g,'')});
  return `<${tag} id="${id}">${content}</${tag}>`;
});
const css=fs.readFileSync(path.join(root,'tools/document-renderer/node_modules/katex/dist/katex.min.css'),'utf8')
 .replace(/url\(fonts\//g,'url(file://'+path.join(root,'tools/document-renderer/node_modules/katex/dist/fonts/'));
const archiveStart=toc.findIndex(v=>v.text.startsWith('Current report '));
const tocHtml=toc.filter((v,i)=>i>0 && (i<archiveStart||v.tag==='h1')).map(v=>
 `<li class="${v.tag}"><a href="#${v.id}">${v.text}</a></li>`).join('');
const title='ACUE · 黎曼零点 · Random Matrix · 素数间隙';
const page=`<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>${title}</title>
<style>${css}
@page {size:A4;margin:22mm 19mm 22mm 19mm;}
*{box-sizing:border-box;}body{margin:0;color:#19222c;font-family:'Songti SC','Noto Serif CJK SC','Times New Roman',serif;font-size:10.2pt;line-height:1.65;}
h1,h2,h3,h4,h5{font-family:'PingFang SC','Arial',sans-serif;line-height:1.32;color:#143444;break-after:avoid;page-break-after:avoid;}
h1{font-size:23pt;break-before:page;margin:0 0 20px;border-bottom:2px solid #235e72;padding-bottom:14px;}
h1:first-of-type{break-before:avoid;}h2{font-size:16pt;margin:29px 0 13px;}h3{font-size:12.1pt;margin:22px 0 9px;}h4{font-size:11pt;}
p{margin:0 0 10px;orphans:3;widows:3;}a{color:#185770;text-decoration:none;overflow-wrap:anywhere;}strong{font-weight:700;}
code{font-family:'SFMono-Regular','Menlo',monospace;font-size:.82em;background:#f1f4f5;padding:1px 3px;border-radius:2px;overflow-wrap:anywhere;word-break:break-word;}
pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:8.4pt;line-height:1.5;padding:10px;background:#f1f4f5;border-left:2px solid #6c919c;break-inside:auto;}pre code{background:transparent;padding:0;}
blockquote{margin:12px 0;padding:11px 15px;background:#f1f6f7;border-left:3px solid #467b8e;}
table{border-collapse:collapse;width:100%;font-size:8.7pt;line-height:1.5;table-layout:fixed;margin:15px 0;}
th,td{border-bottom:1px solid #c8d5db;vertical-align:top;padding:7px 6px;overflow-wrap:anywhere;word-break:normal;}
th{background:#e8f0f3;font-family:'PingFang SC',sans-serif;text-align:left;}tr{break-inside:avoid;}thead{display:table-header-group;}
ul,ol{padding-left:23px;margin:8px 0 12px;}li{padding-bottom:4px;}hr{border:0;border-top:1px solid #a9bdc5;margin:24px 0;}
.display-math{margin:15px 0;break-inside:avoid;max-width:100%;text-align:center;}.katex{font-size:1.05em;}.katex-display{margin:.7em 0;}.math-fallback{font-family:'Menlo',monospace;white-space:pre-wrap;font-size:8.5pt;overflow-wrap:anywhere;}
.toc{break-after:page;font-family:'PingFang SC',sans-serif;}.toc h1{break-before:avoid;}.toc ul{list-style:none;padding:0;columns:2;column-gap:24px;}.toc li{font-size:8.5pt;line-height:1.4;padding:4px 0;break-inside:avoid;}.toc .h1{font-weight:700;margin-top:8px;}.toc .h2{font-size:8pt;}
.cover{height:244mm;display:flex;flex-direction:column;justify-content:center;break-after:page;font-family:'PingFang SC',sans-serif;}
.cover .eyebrow{font-size:11pt;letter-spacing:2px;color:#42758a;margin-bottom:28px;}.cover h1{border:none;font-size:34pt;line-height:1.5;margin:0;}.cover .sub{font-size:16pt;line-height:1.8;margin:22px 0;color:#45616d;}.cover .meta{font-size:10pt;color:#566974;margin-top:35px;}.cover .rule{width:80px;height:4px;background:#246176;margin:28px 0;}
</style></head><body><div class="cover"><div class="eyebrow">RESEARCH HANDOFF · SOURCE ARCHIVE · OVERNIGHT RESEARCH</div>
<h1>ACUE 与黎曼零点<br>从谱反例走向<br>可证明的数论结果</h1><div class="rule"></div><div class="sub">完整研究接手档案<br>GPT-6 Astra × Claude Code / Fable</div>
<div class="meta">Bill (Qingyun) Sun · 2026 年 9 月 4–5 日<br>经审计主说明、公开历史 Markdown 与完整研究报告、算术相关性新路线<br>已证明、计算、猜想与失败分别标明 · Public research archive</div></div>
<nav class="toc"><h1>内容索引</h1><ul>${tocHtml}</ul></nav>${html}</body></html>`;
fs.writeFileSync(path.join(root,'tmp/handoff.html'),page);
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE ? {executablePath:process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE} : {})});
 const tab=await browser.newPage({viewport:{width:650,height:1200}});
 await tab.goto('file://'+path.join(root,'tmp/handoff.html'),{waitUntil:'load'});
 await tab.emulateMedia({media:'print'});
 await tab.evaluate(()=>document.fonts.ready);
 const qa=await tab.evaluate(()=>{
  const issues=[];const width=document.body.clientWidth;
  for(const el of document.querySelectorAll('.display-math,.katex-display,table,pre')){
   const inner=el.querySelector('.katex-html');
   if(inner && inner.getBoundingClientRect().width>el.getBoundingClientRect().width){
     let ratio=el.getBoundingClientRect().width/inner.getBoundingClientRect().width;
     el.style.fontSize=Math.max(6.5,10.2*ratio*.97)+'pt';
   }
   if(el.scrollWidth>el.clientWidth+3)issues.push({tag:el.tagName,text:el.textContent.slice(0,160),scroll:el.scrollWidth,width:el.clientWidth});
  }
  return {issues,headings:document.querySelectorAll('h1,h2,h3').length,width};
 });
 await tab.pdf({path:output,format:'A4',printBackground:true,
  displayHeaderFooter:true,headerTemplate:'<div style="width:100%;font-size:8px;color:#55717b;margin:0 19mm;border-bottom:1px solid #d0dde2;padding-bottom:5px;">ACUE / RIEMANN / RANDOM MATRIX / PRIME GAPS · AUDITED RESEARCH HANDOFF</div>',
  footerTemplate:'<div style="width:100%;font-size:8px;color:#55717b;margin:0 19mm;display:flex;justify-content:space-between;"><span>Bill (Qingyun) Sun · Astra × Fable · September 2026</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
  preferCSSPageSize:true,tagged:true,outline:true});
 fs.writeFileSync(path.join(root,'tmp/render_qa.json'),JSON.stringify({mathErrors,...qa},null,2));
 await browser.close();console.log(JSON.stringify({pdf:output,mathErrors:mathErrors.length,overflow:qa.issues.length}));
})().catch(e=>{console.error(e);process.exit(1)});
