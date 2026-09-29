from pathlib import Path
import json,hashlib,shutil,zipfile,datetime
R=Path(__file__).resolve().parents[1];W=R.parent
read=lambda p:json.loads((R/p).read_text())
a=read('tests/report.json');assert a['reachableTitles']==166 and not a['unreachableNodes'] and not a['unreachableChoices']
assert read('tests/package-report.json')['passed'] and read('tests/journal-report-v03.json')['passed'] and read('tests/media-report-v03.json')['passed'] and read('tests/autoplay-report-v03.json')['passed'] and read('tests/audio-race-report-v03.json')['passed']
for dest in [R/'SeventhDay.html',W/'SeventhDay.html']:shutil.copyfile(R/'dist/SeventhDay.html',dest)
for src,dst in [('CHANGELOG_V0.3.md','CHANGELOG_V0.3.md'),('docs/CODEX_HANDOFF.md','CODEX_HANDOFF_V0.3.md'),('docs/playtest_v03.md','playtest_v03.md')]:shutil.copyfile(R/src,W/dst)
hashfile=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m={'version':'0.3.0-final','builtAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'firstPaths':a['runs']['first']['paths'],'ngPaths':a['runs']['replay']['paths'],'reachableEndings':166,'browserQA':'blocked; 7 viewports not run','randomTest':'V0.2 historical only; engine unchanged','sha256':{}}
for p in sorted(R.rglob('*')):
 if p.is_file() and p.suffix in ['.js','.css','.json','.py','.html','.cjs','.svg','.wav'] and not any(x in p.parts for x in ['archive','__pycache__']) and p.name!='final-build-manifest.json':m['sha256'][str(p.relative_to(R))]=hashfile(p)
(R/'tests/final-build-manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2))
zpath=W/'SeventhDay_Project_V0.3.zip'
with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(R.rglob('*')):
  if p.is_file() and not any(x in p.parts for x in ['__pycache__','node_modules','.git']) and p.suffix not in ['.zip','.pyc']:z.write(p,p.relative_to(R))
with zipfile.ZipFile(zpath) as z:
 assert z.testzip() is None
 assert z.read('SeventhDay.html')==(W/'SeventhDay.html').read_bytes()
 for name in ['README.md','src/journal.js','data/bundle.json','tests/journal-v03.cjs','tests/audio-race-v03.cjs','docs/CODEX_HANDOFF.md','CHANGELOG_V0.3.md','docs/art_prompts_v03.md','docs/audio_system_v03.md','docs/mobile_qa_v03.md','docs/visual_qa_v03.md','tests/media-report-v03.json','tests/autoplay-report-v03.json','tests/audio-race-report-v03.json','tests/package-report.json','tests/final-build-manifest.json']:assert name in z.namelist()
print(json.dumps({'htmlBytes':(W/'SeventhDay.html').stat().st_size,'zipBytes':zpath.stat().st_size,'files':len(z.namelist()),'sha256':hashfile(W/'SeventhDay.html')}))
