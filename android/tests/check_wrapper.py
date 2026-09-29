"""Static checks; an Android SDK and device are still required for binary QA."""
from pathlib import Path
import re, hashlib, zipfile, json
ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT.parent / 'SeventhDay.html').read_text(encoding='utf-8')
ASSET = (ROOT / 'app/src/main/assets/SeventhDay.html').read_text(encoding='utf-8')
HOOK = "if(globalThis.AndroidBridge){AndroidBridge.saveJson(JSON.stringify(E.exportSave(state),null,2));return;}"
assert ASSET.count(HOOK) == 1
assert ASSET.replace(HOOK, '') == SOURCE, 'The asset must differ solely by export hook.'
assert len(re.findall(r'<script>', ASSET)) == 5
assert 'GAME_AUDIO=' in ASSET and 'GAME_SFX={}' in ASSET
assert '<script src=' not in ASSET and 'https://' not in ASSET
java = (ROOT / 'app/src/main/java/com/seventhday/game/MainActivity.java').read_text()
for s in ('setDomStorageEnabled(true)', 'setMediaPlaybackRequiresUserGesture(true)',
          'setAllowFileAccess(false)', 'ACTION_OPEN_DOCUMENT', 'ACTION_CREATE_DOCUMENT',
          'addJavascriptInterface', 'shouldInterceptRequest'):
    assert s in java
manifest = (ROOT / 'app/src/main/AndroidManifest.xml').read_text()
assert 'android.permission.INTERNET' not in manifest
assert 'usesCleartextTraffic="false"' in manifest
report = {'staticChecksPassed': True, 'apkBuilt': False, 'deviceTested': False,
          'sourceSha256': hashlib.sha256(SOURCE.encode()).hexdigest(),
          'assetSha256': hashlib.sha256(ASSET.encode()).hexdigest(),
          'assetBytes': len(ASSET.encode()), 'notes': 'Android toolchain unavailable in this workspace.'}
(ROOT / 'tests/wrapper-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
print('Android wrapper static checks passed; binary and device remain unverified.')
