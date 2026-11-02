from pathlib import Path
import json,hashlib,re,subprocess,sys
root=Path(__file__).resolve().parents[3]
expected=json.loads(Path(__file__).with_name('expected-source-inventory-euclid.json').read_text())
index_path=root/'docs/handoff/ROUNDS_6_14_ARCHIVE_INDEX.json'
idx=json.loads(index_path.read_text()); md_path=root/idx['assembled_markdown']['path']; md=md_path.read_text()
hashbytes=lambda x:hashlib.sha256(x).hexdigest()
assert idx['source_commit']=='2a9ec8192ca8aed1cfdd1bad648c3a3a429e31ba'
assert len({r['path'] for r in idx['reports']})==len(idx['reports'])==69
assert {r['path'] for r in expected}=={r['path'] for r in idx['reports']}
exp={r['path']:r for r in expected}; detailed=[]
for r in idx['reports']:
 raw=(root/r['path']).read_bytes(); text=raw.decode(); assert hashbytes(raw)==r['sha256']==exp[r['path']]['sha256']; assert len(raw)==r['bytes']
 # Reconstruct the eight recorded semantics-preserving table bar substitutions.
 raw_text=text
 changes=r.get('table_math_replacements',[])
 if changes:
  assert r['path']=='research/dyson/round7/dyson-frontier/DYSON_ACTUAL_ZETA_FRONTIER.md'
  assert len(changes)==8
  assert [z['source_line'] for z in changes]==[46]*4+[47]*2+[50]*2
  ls=text.splitlines(keepends=True)
  for z in reversed(changes):
   line=z['source_line']-1; col=z['source_character_column']-1
   assert ls[line][col:col+len(z['old'])]==z['old']
   assert z['old']=='|' and z['new']=='\\vert ' and z['inline_math_delimiter']=='$'
   assert z['source_inline_math'] in raw_text.splitlines()[line]
   ls[line]=ls[line][:col]+z['new']+ls[line][col+len(z['old']):]
  text=''.join(ls)
  assert text.replace('\\vert ','|')==raw_text
 # Reconstruct only the recorded link substitutions, not the assembler's resolver.
 rewrites=iter(r['link_rewrites']); next_rw=next(rewrites,None); lines=[]; fence=None
 pattern=re.compile(r'(?P<image>!?)(?P<label>\[[^\]\n]*\])\((?P<target><[^>\n]+>|[^)\n]+)\)')
 for line in text.splitlines(keepends=True):
  marker=re.match(r'^\s{0,3}(`{3,}|~{3,})',line)
  if marker:
   if fence is None: fence=marker[1][0]
   elif marker[1][0]==fence: fence=None
   lines.append(line); continue
  if fence: lines.append(line); continue
  def repl(m):
   global next_rw
   if next_rw is not None and m['target']==next_rw['old']:
    new=m['image']+m['label']+'('+next_rw['new']+')'; next_rw=next(rewrites,None); return new
   return m[0]
  lines.append(pattern.sub(repl,line))
 assert next_rw is None,(r['path'],'unconsumed link rewrites')
 display=''.join(lines)
 # None of the legacy diagram replacements should apply to these later rounds.
 assert '\\text{bad adversarial state}' not in display
 assert '\\text{distance to collision at }t=0' not in display
 display=re.sub(r'\A---\n(.*?)\n---\n',lambda m:'> Source metadata: '+m[1].replace('\n','; ')+'\n\n',display,flags=re.S)
 display=re.sub(r'^([#]{1,5}) ',r'\1# ',display,flags=re.M)
 display=re.sub(r':chatgpt-content-reference\{index="(\d+)"\}',r'[historical attachment \1; see local source archive]',display)
 display=re.sub(r'cite.*?','[historical retrieval reference; check the original source]',display)
 assert hashbytes(display.encode())==r['display_body_sha256'],(r['path'],'display hash mismatch')
 marker=f'<a id="report-{r["number"]:02d}"></a>'
 assert md.count(marker)==1
 start=md.index(marker); start=md.index(f'**Original bytes:** {r["bytes"]}.\n\n',start)+len(f'**Original bytes:** {r["bytes"]}.\n\n')
 end_marker=f'\n\n<a id="report-{r["number"]+1:02d}"></a>' if r['number']<69 else '\n\n# Source index and artifact receipt'
 end=md.index(end_marker,start); actual=md[start:end]
 assert actual==display,(r['path'],'embedded body mismatch')
 # Exact displayed block mathematics is not changed by the presentation layer.
 for pat in (r'\\\[.*?\\\]',r'\$\$.*?\$\$'):
  assert re.findall(pat,text,re.S)==re.findall(pat,actual,re.S),(r['path'],'displayed mathematics changed')
 detailed.append({'path':r['path'],'source_sha256':r['sha256'],'body_sha256':r['display_body_sha256'],'embedded_exactly_after_documented_transform':True,'display_math_unchanged':True,'equivalent_table_bar_replacements':len(changes)})
# Independently compare all indexed associated objects to a single Git batch read.
artifacts=idx['repository_artifacts']; assert len({r['path'] for r in artifacts})==len(artifacts)==297
query=''.join(idx['source_commit']+':'+r['path']+'\n' for r in artifacts).encode()
data=subprocess.check_output(['git','cat-file','--batch'],cwd=root,input=query); pos=0
for r in artifacts:
 e=data.index(b'\n',pos); sha,typ,size=data[pos:e].decode().split(); size=int(size); blob=data[e+1:e+1+size]; pos=e+1+size+1
 assert typ=='blob' and sha==r['git_blob']; assert len(blob)==r['bytes']; assert hashbytes(blob)==r['sha256']; assert blob==(root/r['path']).read_bytes()
assert pos==len(data)
assert idx['unresolved_local_markdown_links_preserved']==[]
assert hashbytes(md_path.read_bytes())==idx['assembled_markdown']['sha256']
result={'status':'PASS','source_commit':idx['source_commit'],'expected_sources':len(expected),'raw_source_bytes':sum(r['bytes'] for r in expected),'complete_embedded_bodies_checked':len(detailed),'associated_git_objects_checked':len(artifacts),'equivalent_table_bar_replacements':sum(len(r.get('table_math_replacements',[])) for r in idx['reports']),'unresolved_local_markdown_links':0,'assembled_markdown_sha256':hashbytes(md_path.read_bytes()),'archive_index_sha256':hashbytes(index_path.read_bytes()),'source_body_checks':detailed,'scope':'Coverage, exact preservation after documented presentation transforms, displayed mathematical block identity, source checkpoint; no numerical or new mathematical theorem validation.'}
Path(__file__).with_name('source-coverage-euclid.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='source_body_checks'},indent=2))
