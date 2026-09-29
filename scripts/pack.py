from pathlib import Path
import json,base64
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
assets={'endingPremium':{}}
for e in d['endings']:
 if e['artType']!='premium':continue
 key=e['artKey']
 file=R/'assets/endings/premium'/f'{key}.svg'
 if file.is_file():assets['endingPremium'][key]=uri(file,'image/svg+xml')
audio={key:uri(R/'assets/audio/bgm'/f'{key}.wav','audio/wav') for key in ['title','normal','tension','final_day','ending']}
header='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0b1518"><title>第七日的勇者</title><style>'
data_script='globalThis.GAME_DATA='+json.dumps(d,ensure_ascii=False).replace('</','<\\/')+';globalThis.GAME_ASSETS='+json.dumps(assets,ensure_ascii=False)+';globalThis.GAME_AUDIO='+json.dumps(audio)+';globalThis.GAME_SFX={};'
html=header+(R/'src/style.css').read_text()+'</style></head><body><div id="app" class="shell"></div><noscript>需要启用 JavaScript 才能游玩。</noscript><script>'+data_script+'</script>'+''.join('<script>'+(R/'src'/name).read_text()+'</script>' for name in ['engine.js','journal.js','audio.js','ui.js'])+'</body></html>'
(R/'dist/SeventhDay.html').write_text(html,encoding='utf-8')
print('Built offline text-first HTML with optional premium art and 5 embedded BGM loops.')
