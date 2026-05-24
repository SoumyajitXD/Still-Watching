#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, subprocess, sys, zipfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import yaml

ROOT=Path(__file__).resolve().parents[2]
FACT_FILES=[ROOT/p for p in ["README.md","installation-guide.md","curseforge-description.html","latest-modlist.md"]]
PROJECT={"project_name":"Still Watching","minecraft_version":"1.20.1","loader":"Forge","java_version":"17","curseforge_project_id":"1420406","current_release":"Still Watching V1.0.9"}
SPONSOR_START="<!-- sponsor:bisecthosting:start -->"; SPONSOR_END="<!-- sponsor:bisecthosting:end -->"
SPONSOR_LINK="https://url-shortener.curseforge.com/AZDOs"
SPONSOR_BANNER="https://media.forgecdn.net/attachments/description/1420406/description_0434b1be-41ee-4fa8-a2f5-177b2fe87c95.png"
REPO_MAP=["README.md","installation-guide.md","latest-modlist.md","curseforge-description.html","Screenshots/","Releases/",".github/ISSUE_TEMPLATE/",".github/workflows/ci.yml",".github/scripts/validate.py","LICENSE"]
MOD_FIELDS=["name","category","side","side_confidence","purpose","curseforge_url","notes","server_pack_action","reason"]
SIDES={"client","server","both","unknown"}; ACTIONS={"keep","remove","verify","unknown"}

def fail(msg:str)->None:
 print(f"ERROR: {msg}",file=sys.stderr); raise SystemExit(1)
def read(path:Path)->str: return path.read_text(encoding="utf-8-sig",errors="ignore")
def yload(path:Path):
 with path.open(encoding="utf-8-sig") as h: return yaml.safe_load(h)
def line(text:str,index:int)->int: return text.count("\n",0,index)+1

def layout()->None:
 files=["README.md","installation-guide.md","latest-modlist.md","curseforge-description.html","CHANGELOG.md","LICENSE","data/project.yml","data/mods.yml",".github/scripts/generate_docs.py",".github/scripts/validate.py",".github/workflows/ci.yml","docs/release-checklist.md","docs/server-pack-guide.md"]
 dirs=[".github/ISSUE_TEMPLATE",".github/workflows","Releases","Screenshots","data","docs"]
 missing=[p for p in files if not (ROOT/p).is_file()]+[p for p in dirs if not (ROOT/p).is_dir()]
 if missing: fail("Missing required repository paths: "+", ".join(missing))
 print("Repository layout OK")

def yaml_files()->None:
 paths=sorted((ROOT/".github/workflows").glob("*.y*ml"))+sorted((ROOT/".github/ISSUE_TEMPLATE").glob("*.y*ml"))+[ROOT/"data/project.yml",ROOT/"data/mods.yml"]
 errors=[]
 for path in paths:
  try:
   if yload(path) is None: raise ValueError("file is empty")
   print(f"OK: {path.relative_to(ROOT)}")
  except Exception as exc: errors.append(f"{path.relative_to(ROOT)}: {exc}")
 if errors: fail("; ".join(errors))

def html()->None:
 class Smoke(HTMLParser): pass
 errors=[]
 for path in sorted(ROOT.glob("*.html")):
  try:
   parser=Smoke(); parser.feed(read(path)); parser.close(); print(f"OK: {path.name}")
  except Exception as exc: errors.append(f"{path.name}: {exc}")
 if errors: fail("; ".join(errors))

def metadata()->None:
 errors=[]; project=yload(ROOT/"data/project.yml"); mods_doc=yload(ROOT/"data/mods.yml")
 if not isinstance(project,dict): fail("data/project.yml must be a mapping")
 for key,expected in PROJECT.items():
  if str(project.get(key))!=expected: errors.append(f"data/project.yml {key}={project.get(key)!r}, expected {expected!r}")
 sponsor=project.get("sponsor") or {}
 for key,expected in {"bisecthosting_url":SPONSOR_LINK,"required_banner_url":SPONSOR_BANNER,"sponsor_marker_start":SPONSOR_START,"sponsor_marker_end":SPONSOR_END}.items():
  if sponsor.get(key)!=expected: errors.append(f"data/project.yml sponsor.{key} mismatch")
 mods=mods_doc.get("mods") if isinstance(mods_doc,dict) else None
 if not isinstance(mods,list) or not mods: errors.append("data/mods.yml must contain a non-empty mods list")
 else:
  names=[]; urls=[]
  for index,mod in enumerate(mods,1):
   if not isinstance(mod,dict): errors.append(f"mod #{index} must be a mapping"); continue
   for key in MOD_FIELDS:
    if key not in mod or mod[key] in (None,""): errors.append(f"mod #{index} missing {key}")
   name=str(mod.get("name","")).strip(); side=str(mod.get("side","")).lower(); action=str(mod.get("server_pack_action","")).lower(); url=str(mod.get("curseforge_url","")).strip()
   names.append(name); urls.append(url)
   if side not in SIDES: errors.append(f"{name} invalid side {side!r}")
   if action not in ACTIONS: errors.append(f"{name} invalid server_pack_action {action!r}")
   parsed=urlparse(url); parts=[part for part in parsed.path.split("/") if part]
   if parsed.scheme!="https" or parsed.netloc!="www.curseforge.com" or len(parts)<3 or parts[0]!="minecraft" or parts[1] not in {"mc-mods","texture-packs","shaders","modpacks"}: errors.append(f"{name} unexpected CurseForge URL {url}")
  errors += [f"duplicate mod name: {n}" for n,c in Counter(names).items() if n and c>1]
  errors += [f"duplicate CurseForge URL: {u}" for u,c in Counter(urls).items() if u and c>1]
 if errors: fail("; ".join(errors))
 print("Metadata YAML OK")

def generated_docs()->None:
 path=ROOT/"latest-modlist.md"; before=read(path)
 result=subprocess.run([sys.executable,str(ROOT/".github/scripts/generate_docs.py")],cwd=ROOT,text=True,capture_output=True,check=False)
 if result.returncode:
  output="\n".join(part for part in [result.stdout,result.stderr] if part).strip()
  fail("generated docs step failed"+(f": {output}" if output else ""))
 if before!=read(path): fail("latest-modlist.md is stale; run python .github/scripts/generate_docs.py and commit the result")
 print("Generated docs freshness OK")

def modlist()->None:
 text=read(ROOT/"latest-modlist.md"); links=re.findall(r"(?<!!)\[[^\]\n]+\]\((https?://[^\s)]+)\)",text); rows=re.findall(r"(?m)^\|\s*(\d+)\s*\|[^\n]+\|\s*\[[^\]\n]+\]\((https?://[^\s)]+)\)\s*\|",text); errors=[]
 if "admin reference" not in text.lower() or "not a playable manifest" not in text.lower(): errors.append("latest-modlist.md must say it is an admin reference, not a playable manifest")
 if len(links)<40: errors.append(f"expected at least 40 CurseForge links, found {len(links)}")
 if len(rows)!=len(links): errors.append(f"expected every modlist link to be a table row, found {len(rows)} rows for {len(links)} links")
 nums=[int(number) for number,_href in rows]
 if nums!=list(range(1,len(rows)+1)): errors.append("modlist numbering must be continuous")
 for href in links:
  parsed=urlparse(href); parts=[part for part in parsed.path.split("/") if part]
  if parsed.scheme!="https" or parsed.netloc!="www.curseforge.com" or len(parts)<3 or parts[0]!="minecraft" or parts[1] not in {"mc-mods","texture-packs","shaders","modpacks"}: errors.append(f"unexpected CurseForge link: {href}")
 errors += [f"duplicate link: {href}" for href,count in Counter(links).items() if count>1]
 if errors: fail("; ".join(errors))
 print(f"Modlist OK: {len(rows)} entries, {len(links)} links")

def local_links()->None:
 errors=[]; pattern=re.compile(r"(?<!!)(?:\[[^\]\n]+\]|<[^>\n]+>)\(([^)\n]+)\)")
 for path in sorted(ROOT.glob("*.md"))+sorted((ROOT/"docs").glob("*.md")):
  text=read(path)
  for match in pattern.finditer(text):
   href=match.group(1).strip()
   if not href or href.startswith(("http://","https://","mailto:","#")): continue
   target=href.split("#",1)[0].split("?",1)[0].strip()
   if not target: continue
   resolved=(path.parent/target).resolve()
   try: resolved.relative_to(ROOT.resolve())
   except ValueError: errors.append(f"{path.relative_to(ROOT)}:{line(text,match.start(1))} escapes repo: {href}"); continue
   if not resolved.exists(): errors.append(f"{path.relative_to(ROOT)}:{line(text,match.start(1))} broken local link {href}")
 if errors: fail("; ".join(errors))
 print("Local markdown links OK")

def readme_docs()->None:
 text=read(ROOT/"README.md"); errors=[]
 for href in ["./installation-guide.md","./latest-modlist.md","./curseforge-description.html"]:
  if f"]({href})" not in text and f"`{href}`" not in text: errors.append(f"README.md missing required docs link: {href}")
 match=re.search(r"##\s+Repository Map\n\n\| Path \| Purpose \|\n\| --- \| --- \|\n([\s\S]*?)(?:\n---|\Z)",text)
 if not match: errors.append("README.md missing Repository Map table")
 else:
  listed=[]
  for _label,href in re.findall(r"\|\s*\[`]?([^`|]+?)[`]?\s*\]\(([^)]+)\)\s*\|",match.group(1)):
   if href.startswith("./"): listed.append(href[2:])
  for required in REPO_MAP:
   if required not in listed: errors.append(f"Repository Map missing required path: {required}")
 if errors: fail("; ".join(errors))
 print("README docs and repository map OK")

def curseforge_id_consistency()->None:
 pattern=re.compile(r"(?:/curseforge/(?:v|dt)/|attachments/description/|Project\s+ID[^\d]{0,20})(\d+)",re.I); errors=[]
 for path in FACT_FILES:
  ids=sorted(set(pattern.findall(read(path))))
  if ids and ids!="1420406".split(): errors.append(f"{path.name} has CurseForge IDs {ids}, expected [1420406]")
 if errors: fail("; ".join(errors))
 print("CurseForge project ID consistency OK (1420406)")

def release_facts()->None:
 errors=[]; versions={}; facts={"Still Watching":r"\bStill\s+Watching\b","Minecraft 1.20.1":r"\b1\.20\.1\b","Forge":r"\bForge\b","Java 17":r"\bJava\b[\s\S]{0,100}\b17\b|\b17\b[\s\S]{0,100}\bJava\b","Project ID 1420406":r"\b1420406\b"}; version_re=re.compile(r"\b(?:Still\s+Watching\s+V|Current\s+(?:documented\s+)?release[\s\S]{0,120}\bV|Latest\s+(?:documented\s+)?Version[\s\S]{0,120}\bV?)(\d+\.\d+\.\d+)\b",re.I)
 for path in FACT_FILES:
  text=read(path)
  for label,pattern in facts.items():
   if path.name!="latest-modlist.md" and not re.search(pattern,text,re.I): errors.append(f"{path.name} missing {label}")
  for match in version_re.finditer(text): versions.setdefault(match.group(1),[]).append(path.name)
 if len(versions)>1: errors.append(f"release/version text is inconsistent: {versions}")
 if errors: fail("; ".join(errors))
 print("Release facts OK")

def issue_templates()->None:
 template_dir=ROOT/".github/ISSUE_TEMPLATE"; errors=[]; config=template_dir/"config.yml"
 if not config.is_file() or (yload(config) or {}).get("blank_issues_enabled") is not False: errors.append("config.yml must exist and set blank_issues_enabled: false")
 forms=[p for p in sorted(template_dir.glob("*.y*ml")) if p.name!="config.yml"]
 if not forms: errors.append("no issue form files found")
 for path in forms:
  data=yload(path)
  if not isinstance(data,dict): errors.append(f"{path.name} must be a mapping"); continue
  for key in ["name","description","title","labels","body"]:
   if not data.get(key): errors.append(f"{path.name} missing {key}")
  if not any(isinstance(item,dict) and (item.get("validations") or {}).get("required") is True for item in data.get("body") or []): errors.append(f"{path.name} needs at least one required user field")
 if errors: fail("; ".join(errors))
 print("Issue templates OK")

def sponsor_guard()->None:
 readme=read(ROOT/"README.md"); desc=read(ROOT/"curseforge-description.html"); errors=[]
 for label,value in {"start marker":SPONSOR_START,"end marker":SPONSOR_END,"link":SPONSOR_LINK,"banner":SPONSOR_BANNER}.items():
  if value not in readme: errors.append(f"README.md missing sponsor {label}")
 if SPONSOR_LINK not in desc or SPONSOR_BANNER not in desc: errors.append("curseforge-description.html missing sponsor link or banner")
 if errors: fail("; ".join(errors))
 print("BisectHosting sponsor guard OK")

def release_zips()->None:
 errors=[]
 for archive in sorted((ROOT/"Releases").glob("*.zip")):
  try:
   with zipfile.ZipFile(archive) as zf:
    bad=zf.testzip(); names=[info.filename.lower() for info in zf.infolist()]
    if bad: raise zipfile.BadZipFile(f"corrupt entry: {bad}")
    if not names: raise zipfile.BadZipFile("empty archive")
    if any(name=="overrides/" or name.startswith("overrides/") for name in names) and "manifest.json" not in names: raise zipfile.BadZipFile("overrides/ exists without manifest.json")
    print(f"OK: {archive.relative_to(ROOT)}")
  except zipfile.BadZipFile as exc: errors.append(f"{archive.relative_to(ROOT)}: {exc}")
 if errors: fail("; ".join(errors))
 print("Release ZIP audit OK")

def all_checks()->None:
 for check in [layout,yaml_files,html,metadata,generated_docs,local_links,readme_docs,curseforge_id_consistency,release_facts,issue_templates,modlist,sponsor_guard,release_zips]: check()

def main()->None:
 checks={"all":all_checks,"layout":layout,"yaml":yaml_files,"html":html,"metadata":metadata,"generated-docs":generated_docs,"modlist":modlist,"markdown-links":local_links,"readme-docs":readme_docs,"curseforge-id":curseforge_id_consistency,"release-zips":release_zips,"release-facts":release_facts,"issue-templates":issue_templates,"sponsor":sponsor_guard}
 parser=argparse.ArgumentParser(); parser.add_argument("check",choices=checks); checks[parser.parse_args().check]()
if __name__=="__main__": main()
