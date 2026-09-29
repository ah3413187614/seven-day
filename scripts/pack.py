from pathlib import Path
import json,base64,hashlib
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'data/bundle.json').read_text())
r=json.loads((R/'tests/report.json').read_text())
missing={e['id'] for e in r['unreachableTitles']}
for e in d['endings']:e['reachable']=e['ending_id'] not in missing
(R/'data/bundle.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
endings=json.loads((R/'data/endings.json').read_text())
for e in endings['rules']:e['reachable']=e['ending_id'] not in missing
(R/'data/endings.json').write_text(json.dumps(endings,ensure_ascii=False,indent=2),encoding='utf-8')
uri=lambda p,m:'data:'+m+';base64,'+base64.b64encode(p.read_bytes()).decode('ascii')
assets={'endingPremium':{},'scenes':{}}
for e in d['endings']:
 if e['artType']!='premium':continue
 key=e['artKey']
 for suffix,mime in [('jpg','image/jpeg'),('svg','image/svg+xml')]:
  file=R/'assets/endings/premium'/f'{key}.{suffix}'
  if file.is_file():assets['endingPremium'][key]=uri(file,mime);break
for file in sorted((R/'assets/scenes').glob('*.jpg')):
 assets['scenes'][file.stem]=uri(file,'image/jpeg')
audio={key:uri(R/'assets/audio/bgm/ogg'/f'{key}.ogg','audio/ogg') for key in ['title','home','normal','explore','tension','final_day','ending','ending_dark']}
sources=[R/'data/bundle.json',R/'src/style.css']+[R/'src'/name for name in ['engine.js','journal.js','audio.js','prose.js','ui.js']]
sources+=sorted((R/'assets/scenes').glob('*.jpg'))+sorted((R/'assets/endings/premium').glob('*.jpg'))+sorted((R/'assets/audio/bgm/ogg').glob('*.ogg'))
build_id='v0.4.0+'+hashlib.sha256(b''.join(p.read_bytes() for p in sources)).hexdigest()[:12]
header='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0b1518"><title>第七日的勇者</title><style>'
data_script='globalThis.GAME_BUILD_ID='+json.dumps(build_id)+';globalThis.GAME_DATA='+json.dumps(d,ensure_ascii=False).replace('</','<\\/')+';globalThis.GAME_ASSETS='+json.dumps(assets,ensure_ascii=False)+';globalThis.GAME_AUDIO='+json.dumps(audio)+';globalThis.GAME_SFX={};'
html=header+(R/'src/style.css').read_text()+'</style></head><body><div id="app" class="shell"></div><noscript>需要启用 JavaScript 才能游玩。</noscript><script>'+data_script+'</script>'+''.join('<script>'+(R/'src'/name).read_text()+'</script>' for name in ['engine.js','journal.js','audio.js','prose.js','ui.js'])+'</body></html>'
(R/'dist/SeventhDay.html').write_text(html,encoding='utf-8')
(R/'SeventhDay.html').write_text(html,encoding='utf-8')
print('Built',build_id,'offline HTML with scene art, premium art and 8 embedded BGM loops.')
