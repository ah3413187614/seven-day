"""Code-native symbolic pixel markers for ordinary ending roles."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
import json
R=Path(__file__).resolve().parents[1]
categories=sorted({e['artKey'] for e in json.loads((R/'data/bundle.json').read_text())['endings'] if e['artType']=='pixel'})
p=Path(__file__).resolve().parents[1]/'assets/endings/pixel';p.mkdir(parents=True,exist_ok=True)
for i,key in enumerate(categories):
 x=5+i%4;y=4+(i//4)%4
 color=['#a99970','#768d87','#a0a699','#988277'][i%4]
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24" shape-rendering="crispEdges"><rect x="2" y="2" width="28" height="20" fill="#142428"/><rect x="4" y="4" width="24" height="16" fill="none" stroke="#5a6660"/><path fill="{color}" d="M{x} {y}h8v2h2v3h-2v6h-2v3h-4v-3h-2v-6h-2v-3h2z"/><rect x="15" y="8" width="2" height="6" fill="#d3c394"/></svg>'
 (p/f'{key}.svg').write_text(svg)
print(len(categories),'ordinary ending pixel icons')
