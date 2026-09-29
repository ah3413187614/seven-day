from pathlib import Path
from collections import Counter
import json
R=Path(__file__).resolve().parents[1]
read=lambda p:json.loads((R/p).read_text())
d=read('data/bundle.json');r=read('tests/report.json');e=read('tests/evidence-report-v02.json');q=read('tests/quality-report-v02.json')['summary'];rr=read('tests/random-report.json');br=read('tests/browser-report-v02.json')
def write(name,text):(R/name).write_text(text,encoding='utf8')
nodes=list(d['story']['nodes'].values());lens=[len(n['scene']) for n in nodes];pars=Counter(len(n['scene'].split('\n\n')) for n in nodes)
lines=['# V0.2 叙事润色与证据系统','',f'89／89 既有节点逐一改写；仍为 356 个选项，没有新增节点或结局候选。正文 {min(lens)}–{max(lens)} 字符（含标点与换行），自然段分布：{dict(pars)}。场景唯一编辑入口为 scripts/narrative.py；content.py 保留原路由和动作结构，其旧 scene 槽不再用于构建。','',
'## 编辑规则与已落地内容','',
'移除 build.py 的第三至七日通用补长段；不再用第四日统一揭密把所有路线拉平。正文通过空行分段，由 UI 渲染独立 p；昨日实际后果放在纸面外的回声区。角色第一次实际相遇才补角色身份，画像与转述不登记相遇。','',
'王庭用印玺、军粮、账册与问责推进；圣堂用病历、誓词、同意与照护推进；龙境用接头、骨管、契约与幼龙风险推进；边境用锅、桥板、种子与撤离推进。没有给每章统一追加抒情结语。','',
'选择按钮只显示行动，不再呈现“你需要接受：必死／关系崩塌／将进入某结局”。正文保留当下合理可知的危险；选择后才显示实际日落后果。NG+ 仅在第四日多一句声音与抬头动作，不显示规律、条件或攻略。','',
'## 十种真相及授予来源','', '| ID | 片段 | 节点来源 | 行动来源 |','|---|---|---|---|']
for tid,t in d['truths'].items():
 ns=[n['node_id'] for n in nodes if tid in n['truths']];cs=[c['choice_id'] for c in d['choices'].values() if tid in c['truths']]
 lines.append('| '+tid+' | '+t['description']+' | '+', '.join(ns)+' | '+', '.join(cs)+' |')
lines += ['', '取得每条片段时保存 knowledgeLog 的 day、source、evidence。既视感不进入 truths。现有合法路线最多取得 '+str(e['maxTruths'])+'／10 项，没有任何路线自动读完世界百科。片段不是分数，也不在玩家页面显示未解锁清单。','',
'## 实际权限变化','', '| 选项槽 | 完整条件 | 证据不足时的实际行动／身份 | 完整／受限路径次数 |','|---|---|---|---|']
for cid,g in e['gates'].items():
 c=d['choices'][cid];fb=c['fallback'];lines.append('| '+cid+' | '+json.dumps(c['requirement'],ensure_ascii=False)+' | '+fb['text']+'／'+str(fb['terminal_role'] or c['next_node'])+' | '+str(g['full'])+'／'+str(g['limited'])+' |')
lines += ['', '次数统计是一种周目中的状态到达次数，不是玩家概率。每个条件槽两种模式都有真实路径。同一 Day 7 节点的双路线菜单对照见 evidence-report-v02.json 的 sameLocationContrasts；龙巢共同监护另需龙族信任与照护经历，外堤独立守望会核查已发生的弧光转向。d7_c_revolt_3 与 d7_h_oath_dissent_2 原全域停机无法在其七日路线内取得证据，现固定为局部封存／救助，未保留虚假的全域选项。','',
'账房第六日通过龙骨支路实测图取得网络来源；圣堂第六日通过拆机铭牌与原始权限表取得曙母来源。它们只属于抵达现场的路线，不是新的全路线统一揭密。','',
'完整神谕停机须有曙母来源；完整分流须有回流与网络证据；永久共同承压另须试验、预备网与居民代价认知。医生送别艾德里安还需可用缓冲，缺证时只止痛并继续撤离。无剑时第四日改用承压器或鳞片，不凭空持剑。','',
'## 24 条弧光逐项校验','', '| ID／称号 | 早段证据 | 中段转向 | 后段确认 |','|---|---|---|---|']
for a in d['arcs']:
 w=e['arcWitnesses'][a['arc_id']];fmt=lambda h:'第'+str(h['day'])+'日 '+h['text']
 lines.append('| '+a['arc_id']+'／'+a['title']+' | '+fmt(w['early'])+' | '+fmt(w['turn'])+' | '+'；'.join(fmt(h) for h in w['late'])+' |')
lines += ['', '上述是检测见证，最终显示称号仍可能被罪责或更高优先级特殊结局覆盖。完整选择 ID 与前后状态见 evidence-report-v02.json。军人弧光必须有民兵或征马经历；求权不自动等于当过国王，援助不自动等于医师；接触灰烬不自动判为残酷。恐惧强制供能、无辜者死亡、强征与背叛均保留罪责，收束不作自赦。','',
'## NPC 与尾声','',
'14 名角色每人补齐 protects、will_sacrifice、red_line、bias、mistake、secret、can_change、cannot_change。当前在场且已有相遇的关键角色可在回声区回应冲突；尾声只迭代 metNPCs。死亡古龙不再作为活体重遇，后续由遗誓使处理事务。角色值观表是写作约束，不声称每条都有独立事件树。','',
f'旧版 168 活跃称号逐项评级；其中 {q["titlesChanged"]} 个正式题名改写，24 个重点尾声包完整重写。运行时按身份包＋本次终局行动＋实际相遇＋不可撤销伤害＋七日记录收束，不宣称 168 篇独立长文。','',
'## 全节点段落清单','', '| 节点 | 标题 | 字符 | 段数 |','|---|---|---:|---:|']
lines += [f'| {n["node_id"]} | {n["title"]} | {len(n["scene"])} | {len(n["scene"].split(chr(10)+chr(10)))} |' for n in nodes]
write('docs/narrative_polish_v02.md','\n'.join(lines))
visual='''# V0.2 视觉与无障碍验收

**自动结构测试已完成，但未完成真实浏览器视觉 QA。不能据本报告标注桌面或移动端通过。**

本环境的 Playwright 可调用，但 Chromium 可执行文件不存在。V0.2 只做了一次启动探测，随后记录 blocked；没有再次安装、没有伪造截图。tests/browser-report-v02.json 保存实际结果，tests/browser.cjs 是待执行脚本。

| 视口 | 正文／选项／结局／图鉴 | 横向溢出 | 键盘焦点 |
|---|---|---|---|
'''
for v in br['viewports']:visual+=f'| {v["width"]}×{v["height"]} | 未运行 | 未运行 | 未运行 |\n'
visual+='''
## 已做但不等于视觉验收

实际交付 HTML 的三个脚本语法、数据、引擎与模拟 DOM 的七日操作、继续旅程和图鉴保存通过。正文独立段落、回声独立容器、按钮不含成本剧透已由数据／模板检查。CSS 修改了 420px 以下导航、图鉴单列、标题换行、段距和按钮最小高度；加入跳过导航、可见焦点、日落遮罩 inert、Tab 留在下一步、Escape 收起日落、对话框关闭后恢复焦点，以及 reduced-motion。

这些是实现与逻辑证据，不是像素渲染、读屏或真实触摸证据。未输出可供视觉审查的截图。

## 获得浏览器后的必做检查

1. 运行 node tests/browser.cjs；检查七个视口的卷首、七日、长结局、展开回看与图鉴截图。自动脚本通过后仍逐张审查留白、行宽、中文断行、按钮高度与溢出。
2. Tab 从跳转链接走过导航与四选项，Enter 选择；遮罩内 Shift+Tab 与 Tab 不离开，Enter／Escape 后焦点回到新章节标题。原生弹窗取消后回到触发按钮。
3. 在最长尾声、最大系统字重、200% 页面缩放、窄屏软键盘下检查；保证自然纵向滚动，不为一屏塞完文字而缩小字号。
4. 实测存档导出、导入文件选择器、旧版拒绝提示、存储禁用与损坏文件。验证不同 file:// 浏览器的本地保存行为。
5. NVDA／VoiceOver 人工检查标题层级、四按钮读序、回声区及日落对话框。手机 Safari、安卓 Chrome 真机另测，桌面仿真不能代替真机。

状态：逻辑与打包验证通过；真实视觉、系统文件选择、读屏和真机仍为发行前阻断项。
'''
write('docs/visual_qa_v02.md',visual)
# Append actual developer replays to the before-edit log without destroying its original notes.
p=R/'docs/playtest_v02.md';s=p.read_text();mark='\n## V0.2 修改后同路回放'
if mark in s:s=s.split(mark)[0]
s+=mark+'\n\n同样属于开发者引擎逐步回放，不是浏览器或真人盲测。原始逐日视图和结局在 tests/evidence-report-v02.json。\n\n'
for name,x in e['playthroughs'].items():
 s+='### 路线 '+name+'\n\n最终《'+x['ending']['title']+'》。\n\n'
 s+='\n'.join('- 第'+str(v['view']['day'])+'日《'+v['view']['title']+'》；当时已得 '+str(len(v['truths']))+' 项真相。' for v in x['days'])+'\n\n'
s+='A 不再误判“放下军令”；未遇阿瑟兰不入尾声；艾德里安在第四日实际访问后才入相遇记录。B 第四日仍只有地方代价等有限认知，未获容器机制；临时灶解释了营地与家人会合，山口地点已改正；未遇艾德里安不入尾声。按钮不再提前播出死亡后果。\n\n仍待：两位以上未读设计文档的真人各完整游玩一次，记录理解偏差、停顿与情绪，而非让开发者代替他们打分。\n'
p.write_text(s)
write('CHANGELOG_V0.2.md',f'''# V0.2 · 2026-09-29

继承 V0.1 单文件架构与既有七日路由，没有改成新工程。

- 89 个场景全部重写为 {min(lens)}–{max(lens)} 字符、2–3 自然段；移除统一补长与全路线第四日揭密。
- 新增 10 类有来源的真相、18 个同槽条件行动；两种模式均可达。2 个无真实证据路径的全域行动改为固定局部行动。
- 24 弧光使用早段、其后中段转向、再后段确认；军人、医师、君主与残酷起点不再无依据归类。
- 14 NPC 补齐八类价值约束；建立相遇与知识日志，只播实际相遇者后日谈；强制吸取恐惧也纳入重大伤害。
- 审核旧版 168 活跃称号，改写 {q['titlesChanged']} 个题名与全部 24 重点尾声包。候选仍 176，现穷举活跃 {r['reachableTitles']}；没有扩量。
- 昨日回声与正文分离，去掉选项成本剧透与终章人格标签；NG+ 仅保留感官既视感。
- 添加窄屏布局、跳过导航、焦点样式、遮罩背景 inert；真实浏览器／读屏验收未完成。
- 存档 schemaVersion 2，使用 seventh-day-v2；V0.1 键未被删除，旧存档明确拒绝重解释。archive/SeventhDay_v01.html 可用于旧版回放。
- 首／二周目各 16,384 路穷举，100,000 局固定种子模拟，以及 16,384 路证据专项通过；HTML 打包与模拟 DOM 通过。

详见 docs/CODEX_HANDOFF.md 与 tests/*report*.json。日志中的通过不包含真实浏览器视觉质量。
''')
write('README.md',f'''# 第七日的勇者 · V0.2

下载并用浏览器直接打开 dist/SeventhDay.html。无需安装、无需启动服务器、无需联网。独立交付的 SeventhDay.html 与此文件相同。

七天，每天一次决定，每处固定四个选择。昨日改变今日处境，重大行为与所见证据长期保留。通关后可再走一局，图鉴只显示已发现的称号。

## 本版范围

89 场景／356 选择／14 NPC／24 弧光／10 真相片段／18 条件选项槽／24 重点尾声包。176 条候选规则中，{r['reachableTitles']} 个称号经穷举可触发。称号不是同等数量的独立世界结局：基础身份共 16 类，有限收拢，尾声结合本局动作与相遇生成。

真实浏览器视觉、移动端与读屏 QA 尚未完成。逻辑与实际打包 HTML 的模拟 DOM 测试已通过，不代替真实渲染。音频、额外插画与真人盲测未实装／未执行。

## 保存与旧版

新版自动保存使用独立键 seventh-day-v2。建议在重要进度处导出 JSON；浏览器对 file:// 本地保存的行为可能不同。

V0.1 存档不能直接导入 V0.2，以免相同 choice ID 被解释成不同操作。旧键不删除；项目 archive/SeventhDay_v01.html 保留旧引擎，可导入旧 JSON。新版图鉴与周目从新版独立累计，没有自动把旧结局视为新规则已完成。

## 项目入口

| 内容 | 路径 |
|---|---|
| 可直接游玩 | dist/SeventhDay.html |
| 交接与限制 | docs/CODEX_HANDOFF.md |
| 修改前双路线与修改后回放 | docs/playtest_v02.md |
| 89 节点、真相、权限、24 弧光审核 | docs/narrative_polish_v02.md |
| 168 结局逐项评级 | docs/ending_quality_review.md |
| 真实视觉 QA 状态 | docs/visual_qa_v02.md |
| 美术／音频计划 | docs/art_direction.md、docs/audio_plan.md |
| 完整文案与事件数据 | scripts/、data/、docs/story_reference.md |
| 版本改动 | CHANGELOG_V0.2.md |

## 开发构建（玩家不需要）

需要 Python 3 与 Node；本体无运行依赖。

```sh
python3 scripts/build.py
node tests/exhaustive.cjs
node tests/random.cjs 100000 20260928
node tests/evidence-v02.cjs
python3 scripts/pack.py
node tests/package.cjs
python3 scripts/reports.py
python3 scripts/quality_review.py
python3 scripts/reports_v02.py
```

有现成 Playwright 与浏览器后另运行 node tests/browser.cjs。脚本不会替你下载浏览器。报告生成使用最近的 browser-report-v02.json；如尚未真实运行，保留 blocked，不可改成通过。
''')
write('docs/CODEX_HANDOFF.md',f'''# CODEX_HANDOFF · V0.2

## 接手前先读

README → playtest_v02 → narrative_polish_v02 → ending_quality_review → visual_qa_v02 → data/bundle.json 与 src/engine.js。V0.1 实际包、数据与报告在 archive/，两条修改前试玩在 tests/playtest_v01_A.json、B.json。

## 已完成与未完成

已完成 89 节点、356 行动的既有工程改写；24 弧光次序判定；10 有来源真相；18 双模式条件槽；14 角色八项约束；24 重点尾声包与旧版 168 称号逐项审查。现在可达 {r['reachableTitles']} 称号，首周目 {len(r['runs']['first']['titles'])}，二周目真结局 {r['runs']['replay']['truePaths']} 条路径。不可达节点 0，选项 0；全部 24 弧光可检测。

未完成真实浏览器视觉／读屏／系统导入导出／移动真机／真人盲测。没有新插画或音频。不要把 package.cjs 的模拟 DOM 写成浏览器 QA。

## 唯一编辑入口

- scripts/narrative.py：89 正文，空行是段落边界。content.py 的旧 scene 槽为 V0.1 路由兼容占位，构建不读取其正文；标题与四行动仍在 content.py。
- scripts/systems.py：真相来源、条件权限与替代动作、NPC 相遇与价值、题名修订。修改门槛后检查每个模式是否可达，避免“全操作永远解不开”。
- scripts/lore.py：稳定 ID、基本角色、常规题名与弧光初稿；systems.py 覆盖已复审的部分。不要只改生成 JSON。
- scripts/epilogues.py：24 个完整尾声包。NPC 栏不直接展示，由实际 metNPCs、flags、status 生成。
- src/engine.js：纯状态推进与结局；src/ui.js：四选、日落、存档、图鉴；style.css：保留原视觉基础的响应式补丁。
- scripts/build.py → data/；pack.py → dist/SeventhDay.html。pack 依赖当前穷举报告标记活跃称号，不能跳过穷举直接打包。

## 状态与权限

schemaVersion=2。truths 与 knowledgeLog 只在抵达具体节点或执行指定动作时授予。encounterLog 与 metNPCs 分开记录亲历相遇，名字出现在画上不算。resolveChoice 必须同时用于 UI 与 apply；fallback 有自己真实的文字、flag、后果与终局身份。不可先播全操作、后台偷偷执行局部行动。

弧光必须符合早段动作、晚段次数、角色、特定 flag，并存在早段之后且最后确认之前的转向。dom 仍由前六天行为取主导，但前台不展示人格诊断。罪责比一般称号优先，赎罪类不会移除旧 flag。

真结局：已完成过新版一局＋lattice_validated＋shared_load＋collective_final＋回流／龙骨网／平民代价知识，无重大罪责或强征。仍失去旧文明部分恒温与无痛便利，没有全员无代价完美方案。

## 存档策略

seventh-day-v2 与 V0.1 键隔离。导入只接受 V2 的 choiceIds、meta，按规则重新回放，不信任外部 stats。旧 JSON 请用 archive/SeventhDay_v01.html。禁止静默把旧路径当作新行为；没有自动迁移旧图鉴与周目。

## 验证与出包

按 README 的开发顺序运行。已执行：两周目共 32,768 路穷举；另 16,384 路证据与模式专项；100,000 局 seed 20260928 模拟；交付 HTML 与模拟 DOM。各条称号的路径在 witnesses.json，各弧光及每个权限双模式的路径在 evidence-report-v02.json。

最终报告新增不可达称号不得藏起来；应记录是权限、角色或优先级造成。真实浏览器缺失时只标未完成，不重试安装来消耗任务时间。

## V0.3 优先级（最多五项）

1. 在真实浏览器与真机完成七视口截图、键盘、读屏及存档验收。
2. 找未读策划的玩家做两种起点盲测，记录对证据与选项的理解。
3. 给 B 级共享身份尾声增加基于具体中段行动的差异，保持称号数量克制。
4. 把更多 NPC 价值冲突写成可重复核对的拒绝／谈判事件，避免只停在角色表。
5. 完成旧存档的只读回顾界面与可靠升级提示，再评估是否迁移图鉴。
''')
write('docs/technical_architecture.md','''# V0.2 技术架构

本体延续纯 JavaScript 引擎＋模板 UI＋JSON 数据，打包为无外部请求的 HTML。沒有引入框架或服务端。

| 层 | 职责 |
|---|---|
| narrative/content/lore/systems/epilogues | 可审核的写作、路由、规则与条件数据 |
| build.py | 展开 89 节点、356 选择及日志字段，生成设计参考 |
| engine.js | initial → enter → resolveChoice → apply → finish；只读输入后复制新状态 |
| ui.js | 渲染玩家字段；一个日落遮罩阻止重复选择；V2 事件存档与发现图鉴 |
| pack.py | 将 CSS、数据、引擎、UI 内嵌，使用穷举输出标记可达规则 |

GameState.schemaVersion=2：原有日数、节点、属性、关系、flag、历史之外，新增 truths、knowledgeLog、metNPCs、encounterLog。History 保存当时实际 mode、text、stat_change 和后果，主导行动使用已执行效果，不能回读基础选择冒充受限模式。

条件选择保留原 choice_id 和下一日入口。relationsMin 让实际阵营关系影响操作资格；arcProgressAny 仅检查前六日已经发生的早段与转向，不伪造尚未完成的弧光。完整／受限模式在显示与执行时同样解析；有限模式有独立 flag 与终局身份，不授予原全域操作成果。所有模式通过合法路径见证，不能靠直接塞 flag 证明可达。

SaveFile 仅保存 schemaVersion、choiceIds 与周目元信息。导入按 V2 从初始状态重放，拒绝跨版本、不合法节点和超过七次行动。V1 引擎单独归档；不隐式迁移旧选择含义。

数据全部随本体离线提供；策划隐藏指不在玩家 UI 揭露，不是加密。用户可以检查或编辑自己的 HTML／存档，本作没有服务端防作弊目标。

验证分工：exhaustive 检查图与称号；evidence-v02 检查来源、权限双模式、相遇与弧光时序；random 用固定种子抽样；package 检查实际 HTML 的模拟 DOM；browser 需要真实内核，当前未验收。
''')
write('docs/ending_system.md',f'''# V0.2 结局解析约定

七次选择完成才结算。第七日决定实际身份（受限行动可以改变原基础身份），前六日行动维度决定普通称号候选。弧光按具体的早段—中段转向—晚段确认检测；重大伤害持续覆盖一般人格评价；特殊／真结局需要明列证据与准备。

候选 176，现活跃 {r['reachableTitles']}；图鉴只计 reachability=true。旧版 168 条逐项审核见 ending_quality_review.md，不为恢复数量弱化权限。世界身份仍 16 类，称号不等于独立世界。

尾声：身份／特例包 → 本次第七日实际后果 → 仅实际相遇 NPC 的行为、关系、死亡响应 → 世界延续 → 起始与一次转向记录 → 七日完整回看。罪责附记不会被救援或自我牺牲抵消。

阿瑟兰死亡永久保留；实际遇见他后才能在 NPC 尾声提到他。艾德里安仅在缓冲落实且停止请求被执行时死亡；成为新容器或真结局时获交接，其余局部救援不自动解放他。所有 NPC 不因世界身份自动变成朋友。

称号内仍有编辑评价，前台没有八维分数、主导人格标签或满足条件清单。全部 ID 的可重放见证在 tests/witnesses.json。
''')
write('docs/ui_ux.md','''# V0.2 阅读与操作

正文是独立 2–3 段纸面；昨日后果与已遇人物回应在外侧回声区。四个行动按钮只含行动，不列将来死亡、关系变化或隐藏结局。合理可知的危险留在场景里，执行后读实际结果。

卷首 → 七日逐日场景 → 日落结果 → 终章。终章含收束、相遇者、世界、个人和可展开七日回看；不展示人格测试。图鉴只显示已发现的题名与时间，未知条件封存。

窄屏单列四选项，420px 下导航换行、图鉴单列，正文不为塞进一屏而缩小。允许自然纵向滚动。键盘有跳过导航、焦点样式；日落隔离背景并约束 Tab，下一步回到章节标题；原生对话框关闭恢复触发焦点。

新存档键 seventh-day-v2；导出／导入供离线使用，导入上限 100KB。旧版 JSON 说明性拒绝，未完成本局重开与导入会询问替换。损坏存储提示可导出，不宣称浏览器一定允许 file:// 永久保存。

以上为已实现设计。真实浏览器布局、键盘、触摸、读屏与文件选择器仍未验收，不能用模拟 DOM 的通过代替。
''')
print('V0.2 docs generated:', {'sceneCharacters':(min(lens),max(lens)),'paragraphs':dict(pars),'active':r['reachableTitles']})
