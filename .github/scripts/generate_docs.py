#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def parse_project():
 d={};s={}
 for l in (ROOT/'data/project.yml').read_text().splitlines():
  if not l.strip() or l.lstrip().startswith('#'): continue
  if l.startswith('  '):
   if ':' in l: k,v=l.strip().split(':',1); s[k]=v.strip().strip('"')
  elif ':' in l:
   k,v=l.split(':',1); d[k.strip()]=v.strip().strip('"')
 d['sponsor']=s; return d

def parse_mods():
 mods=[];cur={}
 for l in (ROOT/'data/mods.yml').read_text().splitlines():
  if l.startswith('  - '):
   if cur: mods.append(cur)
   cur={};k,v=l[4:].split(':',1);cur[k.strip()]=v.strip().strip('"')
  elif l.startswith('    ') and ':' in l:
   k,v=l.strip().split(':',1); cur[k.strip()]=v.strip().strip('"')
 if cur: mods.append(cur)
 return mods

p=parse_project();mods=parse_mods()
total=len(mods);both=sum(m['side']=='both' for m in mods);client=sum(m['side']=='client' for m in mods);unknown=sum(m['side']=='unknown' for m in mods)
out=['# Latest Modlist','', '> [!WARNING]','> This is an admin reference, not a playable manifest. Use CurseForge release files for exact mod versions and truth.','',f"Current documented release: **{p['current_release']}**.",f"Minecraft: **{p['minecraft_version']}** | Loader: **{p['loader']}** | Java: **{p['java_version']}** | CurseForge Project ID: **{p['curseforge_project_id']}**",'', '## Summary','','| Metric | Count |','| --- | ---: |',f'| Total mods | {total} |',f'| Both-side count | {both} |',f'| Client candidate count | {client} |',f'| Unknown count | {unknown} |','']
cats={}
for m in mods: cats.setdefault(m['category'],[]).append(m)
n=1
for cat in sorted(cats):
 out+=[f'## {cat}','','| # | Mod | Side | Confidence | Purpose | CurseForge |','| ---: | --- | --- | --- | --- | --- |']
 for m in cats[cat]:
  out.append(f"| {n} | {m['name']} | {m['side']} | {m['side_confidence']} | {m['purpose']} | [Link]({m['curseforge_url']}) |")
  n+=1
 out.append('')
out+=['## Server pack trimming candidates','']
for i,m in enumerate([x for x in mods if x['side']=='client' or x['server_pack_action']=='remove'],1): out.append(f"{i}. **{m['name']}** — {m['reason']}")
out+=['','## Needs verification','']
for i,m in enumerate([x for x in mods if x['side']=='unknown' or x['side_confidence']=='unknown' or x['server_pack_action']=='verify'],1): out.append(f"{i}. **{m['name']}** — {m['reason']}")
(ROOT/'latest-modlist.md').write_text('\n'.join(out)+'\n')
