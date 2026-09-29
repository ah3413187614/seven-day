# CODEX_HANDOFF · V0.2

## 接手前先读

README → playtest_v02 → narrative_polish_v02 → ending_quality_review → visual_qa_v02 → data/bundle.json 与 src/engine.js。V0.1 实际包、数据与报告在 archive/，两条修改前试玩在 tests/playtest_v01_A.json、B.json。

## 已完成与未完成

已完成 89 节点、356 行动的既有工程改写；24 弧光次序判定；10 有来源真相；18 双模式条件槽；14 角色八项约束；24 重点尾声包与旧版 168 称号逐项审查。现在可达 166 称号，首周目 165，二周目真结局 22 条路径。不可达节点 0，选项 0；全部 24 弧光可检测。

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


## 最终续跑验收（2026-09-29T01:01:46.441113+00:00）

基于磁盘最终源码重新执行：首周目与 NG+ 各 16,384 路；权限证据专项 16,384 路；固定种子 20260928 随机 100,000 局；重新构建后的 HTML smoke test 通过。89 节点、356 行动、24 弧光、166 可达称号；首周目 165，NG+ 166，真结局 22 条路径。18 条件槽的完整和受限模式全部可达，12 组同终局地点菜单对照通过。10 项 Truth 均有路线见证，单局最多 7 项。未发现节点或行动死路。

本次未重复修改已完成剧情。补入可复现交付脚本 scripts/finalize_v02.py，生成构建哈希与完整 ZIP。再次启动真实浏览器失败（缺少 Chromium），视觉 QA 仍未完成，不计为通过。
