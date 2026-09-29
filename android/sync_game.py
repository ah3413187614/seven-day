"""Embed the sealed V0.3 HTML; adapt only its export button to Android SAF."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / 'SeventhDay.html'
ASSET = ROOT / 'app/src/main/assets/SeventhDay.html'
before = "function exportFile(){if(!state){toast('请先开始或继续旅程。');return;}"
after = before + "if(globalThis.AndroidBridge){AndroidBridge.saveJson(JSON.stringify(E.exportSave(state),null,2));return;}"
html = SOURCE.read_text(encoding='utf-8')
if html.count(before) != 1:
    raise SystemExit('Export hook changed; review the source before packaging.')
asset = html.replace(before, after)
ASSET.parent.mkdir(parents=True, exist_ok=True)
ASSET.write_text(asset, encoding='utf-8')
print('V0.4 source SHA-256:', hashlib.sha256(SOURCE.read_bytes()).hexdigest())
print('Android asset SHA-256:', hashlib.sha256(ASSET.read_bytes()).hexdigest())
