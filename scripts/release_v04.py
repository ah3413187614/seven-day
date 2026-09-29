"""One ordered release entry point; source -> HTML -> Android asset -> ZIP."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys,zipfile
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent

def run(*args,cwd=ROOT):
    subprocess.run(args,cwd=cwd,check=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

run(sys.executable,'scripts/build.py')
for name in ['tests/exhaustive.cjs','tests/evidence-v02.cjs','tests/journal-v03.cjs','tests/prose-v04.cjs']:
    run('node',name)
run(sys.executable,'scripts/pack.py')
for name in ['tests/media-v03.cjs','tests/autoplay-v03.cjs','tests/audio-race-v03.cjs','tests/package.cjs']:
    run('node',name)
run(sys.executable,'tests/audio_quality_v03.py')
run(sys.executable,'tests/audio_decode_v04.py')
run(sys.executable,'android/sync_game.py')
run('node','tests/check_web_asset.cjs',cwd=ROOT/'android')
run(sys.executable,'android/tests/check_wrapper.py')
run('node','tests/browser.cjs')
html=ROOT/'SeventhDay.html';dist=ROOT/'dist/SeventhDay.html';asset=ROOT/'android/app/src/main/assets/SeventhDay.html'
assert html.read_bytes()==dist.read_bytes(),'Root and dist differ'
before="function exportFile(){if(!state){toast('请先开始或继续旅程。');return;}"
after=before+"if(globalThis.AndroidBridge){AndroidBridge.saveJson(JSON.stringify(E.exportSave(state),null,2));return;}"
assert html.read_text().count(before)==1
assert asset.read_text()==html.read_text().replace(before,after),'Android asset differs beyond documented export bridge'
report=json.loads((ROOT/'tests/report.json').read_text())
assert report['reachableTitles']==166 and not report['unreachableNodes'] and not report['unreachableChoices']
marker=__import__('re').search(r'GAME_BUILD_ID="(v0\.4\.0\+[0-9a-f]{12})"',html.read_text())
assert marker and marker.group(1) in asset.read_text()
manifest={'buildId':marker.group(1),'builtAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'firstRunPaths':report['runs']['first']['paths'],'ngPlusPaths':report['runs']['replay']['paths'],
 'reachableEndings':166,'htmlSha256':sha(html),'androidAssetSha256':sha(asset),
 'audioCodec':'Ogg Vorbis; WAV masters in source','browserQA':json.loads((ROOT/'tests/browser-report-v04.json').read_text())['status'],
 'apk':'not built in current environment','sourceFileSha256':{}}
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.suffix in ['.js','.css','.json','.py','.html','.cjs','.jpg','.ogg','.wav'] and not any(part in p.parts for part in ['.git','__pycache__','archive','build']):
        if p.name!='final-build-manifest-v04.json':manifest['sourceFileSha256'][str(p.relative_to(ROOT))]=sha(p)
(ROOT/'tests/final-build-manifest-v04.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
zipfile_path=OUT/'SeventhDay_Project_V0.4.zip'
with zipfile.ZipFile(zipfile_path,'w',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and not any(part in p.parts for part in ['.git','__pycache__','build','node_modules']) and p.suffix not in ['.zip','.pyc']:
            z.write(p,p.relative_to(ROOT))
with zipfile.ZipFile(zipfile_path) as z:
    assert z.testzip() is None
    assert z.read('SeventhDay.html')==html.read_bytes()
    assert z.read('dist/SeventhDay.html')==html.read_bytes()
    assert z.read('android/app/src/main/assets/SeventhDay.html')==asset.read_bytes()
(OUT/'SeventhDay_V0.4.html').write_bytes(html.read_bytes())
print(json.dumps({'buildId':manifest['buildId'],'htmlBytes':html.stat().st_size,'zipBytes':zipfile_path.stat().st_size,'htmlSha256':sha(html),'androidAssetMatches':True},ensure_ascii=False))
