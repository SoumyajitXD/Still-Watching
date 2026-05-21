#!/usr/bin/env python3
from pathlib import Path
import re,sys,zipfile
from html.parser import HTMLParser

ROOT=Path(__file__).resolve().parents[2]
REQ_DOCS=['docs/release-checklist.md','docs/server-pack-guide.md']
FACT_FILES=['README.md','installation-guide.md','curseforge-description.html','latest-modlist.md']

def die(msg): print('ERROR:',msg,file=sys.stderr); raise SystemExit(1)
def read(p): return (ROOT/p).read_text(encoding='utf-8',errors='ignore')

def parse_project():
 t=read('data/project.yml');d={};s={}
 for i,l in enumerate(t.splitlines(),1):
  if not l.strip() or l.lstrip().startswith('#'): continue
  if l.startswith('  '):
   if ':' in l: k,v=l.strip().split(':',1); s[k]=v.strip().strip('"')
  elif ':' in l:
   k,v=l.split(':',1); d[k.strip()]=v.strip().strip('"')
 d['sponsor']=s; return d

def parse_mods():
 mods=[];cur={}
 for l in read('data/mods.yml').splitlines():
  if l.startswith('  - '):
   if cur: mods.append(cur)
   cur={};k,v=l[4:].split(':',1);cur[k.strip()]=v.strip().strip('"')
  elif l.startswith('    ') and ':' in l:
   k,v=l.strip().split(':',1);cur[k.strip()]=v.strip().strip('"')
 if cur:mods.append(cur)
 return mods

def layout():
 req=['README.md','installation-guide.md','latest-modlist.md','curseforge-description.html','CHANGELOG.md','data/project.yml','data/mods.yml','.github/scripts/generate_docs.py']+REQ_DOCS
 miss=[p for p in req if not (ROOT/p).exists()]
 if miss: die('Missing required files: '+', '.join(miss))
 print('layout OK')

def html_smoke():
 class P(HTMLParser):pass
 for p in ROOT.glob('*.html'): P().feed(p.read_text(errors='ignore'))
 print('html OK')

def links():
 pat=re.compile(r'\[[^\]]+\]\((\.?/?[^)\s]+)\)')
 for f in ['README.md']+REQ_DOCS+['installation-guide.md','latest-modlist.md']:
  txt=read(f)
  for m in pat.finditer(txt):
   href=m.group(1)
   if href.startswith('http') or href.startswith('#'): continue
   tgt=(ROOT/f).parent / href.split('#')[0]
   if not tgt.exists(): die(f'{f}:{txt.count("\n",0,m.start())+1} broken link {href}')
 print('markdown links OK')

def metadata():
 p=parse_project()
 for f in FACT_FILES:
  t=read(f)
  for key in ['project_name','minecraft_version','loader','java_version','curseforge_project_id','current_release']:
   if p[key] not in t: die(f'{f} missing metadata value {key}={p[key]}')
 print('metadata consistency OK')

def modlist_consistency():
 import subprocess
 subprocess.check_call([sys.executable,str(ROOT/'.github/scripts/generate_docs.py')])
 print('modlist regenerated from data/mods.yml')

def sponsor_guard():
 p=parse_project();t=read('README.md')+read('curseforge-description.html')
 for x in [p['sponsor']['sponsor_marker_start'],p['sponsor']['sponsor_marker_end'],p['sponsor']['bisecthosting_url'],p['sponsor']['required_banner_url']]:
  if x not in t: die('sponsor guard missing '+x)
 print('sponsor guard OK')

def release_zip_audit():
 for z in (ROOT/'Releases').glob('*.zip'):
  with zipfile.ZipFile(z) as f:
   if not f.namelist(): die(f'{z} empty zip')
 print('release zip audit OK')

def changelog():
 p=parse_project(); t=read('CHANGELOG.md')
 if p['current_release'].split()[-1] not in t: die('CHANGELOG missing current release')
 print('changelog OK')

if __name__=='__main__':
 checks=[layout,html_smoke,links,metadata,modlist_consistency,sponsor_guard,release_zip_audit,changelog]
 for c in checks:c()
 print('all checks passed')
