from pathlib import Path
import json,hashlib,shutil,zipfile,datetime
R=Path(__file__).resolve().parents[1];W=R.parent
load=lambda p:json.loads((R/p).read_text());r=load('tests/report.json');ev=load('tests/evidence-report-v02.json');qr=load('tests/quality-report-v02.json');rr=load('tests/random-report.json')
required=['docs/playtest_v02.md','docs/narrative_polish_v02.md','docs/ending_quality_review.md','docs/visual_qa_v02.md','docs/art_direction.md','docs/audio_plan.md','CHANGELOG_V0.2.md','docs/CODEX_HANDOFF.md']
for p in required:assert (R/p).is_file() and (R/p).stat().st_size>100,p
assert r['reachableNodes']==89 and r['reachableChoices']==356 and r['detectableArcs']==24
assert rr['runs']==100000 and r['runs']['first']['paths']==16384 and r['runs']['replay']['paths']==16384
assert not r['unreachableNodes'] and not r['unreachableChoices']
for name in ['SeventhDay.html']:
 shutil.copyfile(R/'dist'/name,R/name);shutil.copyfile(R/name,W/name)
# The final player's file, source and reports are bound by a machine-readable manifest.
hashfile=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest={'version':'0.2','builtAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'nodes':89,'actions':356,'arcs':24,'reachableEndings':r['reachableTitles'],'truths':10,'conditionalSlots':len(ev['gates']),'sameDay7SceneContrasts':len(ev['sameLocationContrasts']),'firstPaths':16384,'ngPaths':16384,'randomRuns':100000,'seed':20260928,'browserQA':'blocked_not_visually_verified','sha256':{}}
for p in sorted(R.rglob('*')):
 if p.is_file() and p.suffix in ['.js','.cjs','.py','.json','.css','.ts','.html'] and not any(x in p.parts for x in ['archive','__pycache__']) and p.name!='final-build-manifest.json':manifest['sha256'][p.relative_to(R).as_posix()]=hashfile(p)
assert hashfile(R/'SeventhDay.html')==hashfile(R/'dist/SeventhDay.html')==hashfile(W/'SeventhDay.html')
(R/'tests/final-build-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
summary=f'''# 《第七日的勇者》V0.2 最终交付

已完成源码、数据、最终构建及逻辑测试。真实浏览器视觉 QA 未完成；这是可交付试玩的离线构建，不代表商业发行验收完成。

| 项目 | 最终结果 |
|---|---:|
| 节点／行动 | 89／356 |
| 可检测人物弧光 | 24 |
| 实际可达称号 | {r['reachableTitles']}（首周目 {len(r['runs']['first']['titles'])}） |
| Truth Fragment／动态条件槽 | 10／{len(ev['gates'])} |
| 同一 Day 7 场景双路线菜单对照 | {len(ev['sameLocationContrasts'])} 组 |
| 首周目／NG+ 完整枚举 | 各 16,384 |
| 知识、相遇与权限专项 | 16,384 路通过 |
| 固定种子随机模拟 | 100,000 局，seed 20260928 |
| 节点／行动死路 | 0／0 |
| 二周目真结局路径 | {r['runs']['replay']['truePaths']} |
| 浏览器视觉 QA | 未完成；无可用内核，未再下载 |

下载 SeventhDay.html，用 Chrome 或 Edge 打开；无需安装、服务器或联网。项目 ZIP 根目录也有相同 HTML，包含完整 src、data、tests、docs、scripts 与 README。构建哈希在 tests/final-build-manifest.json；模拟 DOM smoke test 不冒充真实浏览器测试。

## 本轮收尾

- 从磁盘恢复已完成的 V0.2；本次重新运行全路径、权限专项、随机模拟与最终 HTML smoke test，未重复改写场景。
- 补齐阵营信任和弧光进展对真实行动的限制；18 个条件槽的完整／受限模式均有合法路径。
- 修正三处真相来源叙述不足，并明确测量／铭牌核对所得证据；未重新大规模改写 89 场景。
- 同一 Day 7 节点的 12 组不同菜单均保存完整路线见证，不以手工注入 flag 伪造可达。
- 尾声补一句人物收束，按世界、实际相遇者、自身、七日回看、最后一句组织；不引入未见 NPC。
- 真正带重大罪责的赎罪路径有 {ev['crimeRedemptionPaths']} 条专项见证，仍保留原伤害记录；不是一次末日善举就洗白。
- 旧版 168 活跃题名逐项审查，38 个改名、24 主要尾声包重写；最终 166 可达，候选仍 176。
- failed_Corruption 因强制恐惧供能补记罪责而被更具体血债结局覆盖；godslayer_Corruption 无法同时满足腐化主导与合法停机知识。两者转 reserve，不为数量放宽权限。
- 最终引擎、数据与内嵌 HTML 字节对应检查通过；完整七日、回放、V2 存档、图鉴、重开、NG+ 与真结局逻辑验证。

## 兼容与限制

V0.2 使用独立存档键。V0.1 JSON 不被重新解释；旧键未删除，ZIP 中 archive/SeventhDay_v01.html 可回放旧存档。旧图鉴与周目不自动迁移。

当前 89 正文均为独立 2–3 段。常规称号仍共享 16 身份尾声包并结合本局事件，不宣称 166 篇完全独立世界故事。评级是开发编辑判断，尚待真实玩家验证。

真实 Chrome／Edge 七视口视觉、真机触摸、读屏、系统文件导入导出尚待实测。BGM、像素小人、优质结局立绘与 APK 均未接入，按本轮范围留给后续版本。

## V0.3 五项优先级

1. 补齐真实浏览器、真机、键盘与读屏验收。
2. 未读策划者的两种起点盲测。
3. 增加 B 级尾声的具体行动差异。
4. 扩充 NPC 价值冲突的实际拒绝／谈判。
5. 先完成可靠版本升级回顾，再按资源接入音画与分发形式。

完整审阅入口：docs/CODEX_HANDOFF.md、narrative_polish_v02.md、ending_quality_review.md、visual_qa_v02.md、playtest_v02.md。美术与音频计划也已收录。
'''
(W/'第七日的勇者_开发总览.md').write_text(summary)
# Convenient standalone change log and handoff; all other required docs are in the ZIP.
shutil.copyfile(R/'CHANGELOG_V0.2.md',W/'CHANGELOG_V0.2.md')
shutil.copyfile(R/'docs/CODEX_HANDOFF.md',W/'CODEX_HANDOFF_V0.2.md')
shutil.copyfile(R/'docs/visual_qa_v02.md',W/'visual_qa_v02.md')
zip_path=W/'SeventhDay_Project_V0.2.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(R.rglob('*')):
  if p.is_file() and not any(x in p.parts for x in ['__pycache__','node_modules','.git']) and p.suffix not in ['.pyc','.zip']:z.write(p,p.relative_to(R))
with zipfile.ZipFile(zip_path) as z:
 assert z.testzip() is None
 assert z.read('SeventhDay.html')==(W/'SeventhDay.html').read_bytes()
 for p in ['README.md','src/engine.js','data/bundle.json','tests/final-build-manifest.json',*required]:assert p in z.namelist(),p
print(json.dumps({'zip':str(zip_path),'files':len(z.namelist()),'bytes':zip_path.stat().st_size,'htmlBytes':(W/'SeventhDay.html').stat().st_size,'htmlSHA256':hashfile(W/'SeventhDay.html')},ensure_ascii=False))
