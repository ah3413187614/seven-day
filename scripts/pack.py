from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'data/bundle.json').read_text())
r=json.loads((R/'tests/report.json').read_text())
missing={e['id'] for e in r['unreachableTitles']}
for e in d['endings']:e['reachable']=e['ending_id'] not in missing
(R/'data/bundle.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
endings=json.loads((R/'data/endings.json').read_text())
for e in endings['rules']:e['reachable']=e['ending_id'] not in missing
(R/'data/endings.json').write_text(json.dumps(endings,ensure_ascii=False,indent=2),encoding='utf-8')
header='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0b1518"><title>第七日的勇者</title><style>'
html=header+(R/'src/style.css').read_text()+'</style></head><body><div id="app" class="shell"></div><noscript>需要启用 JavaScript 才能游玩。</noscript><script>globalThis.GAME_DATA='+json.dumps(d,ensure_ascii=False).replace('</','<\\/')+';</script><script>'+(R/'src/engine.js').read_text()+'</script><script>'+(R/'src/ui.js').read_text()+'</script></body></html>'
(R/'dist/SeventhDay.html').write_text(html,encoding='utf-8')
print('Built dist/SeventhDay.html; no network or build dependencies required.')
