# 第七日的勇者

**七日西幻文字冒险 · 完整内容原型 v0.1**

> 昨天的选择决定今天你还能选择什么；七天的选择决定你最终成为谁。

## 先玩

解压后双击 **dist/SeventhDay.html**，选择Chrome、Edge或其他现代浏览器打开。游戏完全离线，不用安装Node、Python或依赖，不调用AI接口。

每天四选一，共七天。选定行动后阅读日落后果，再进入下一天。浏览器通常会自动保存；若本地文件存储被限制，请使用“导出本局存档”。在页面预览器不能执行脚本时，先下载到电脑再打开。

如果浏览器拒绝直接打开本地文件，可在项目目录运行：

```bash
python -m http.server 8000
```

再访问 `http://localhost:8000/dist/SeventhDay.html`。这仅为本机服务，不是公开部署。

## 已完成

- **89个完整节点、356个行动**，七日均可玩；16套基础终局加4套前史条件终局。
- **14位主要角色、8维隐藏人格、6方关系、不可撤销行为记录**。
- **24种人物弧光、168个经穷举证明可触发的称号、24份重点尾声编辑稿**。
- 确定性Ending Engine、二周目回声与真结局、存档回放、重新开始、图鉴、选择回顾。
- 首／二周目各16,384条路径穷举；额外100,000局固定种子随机模拟。
- 完整数据、正式TypeScript接口、技术文档与自动化测试。176条候选中8条储备不计入图鉴。

**数量口径**：168个称号不是168个完全不同的世界结局。世界身份有16类，称号结合行为、弧光与特殊结果；七天存在有限收拢，不是无限分叉树。

## 文档入口（有剧透）

| 想看什么 | 文件 |
|---|---|
| 游戏体验与全部系统 | docs/game_design.md |
| 历史、势力、深渊与圣剑逻辑 | docs/world_bible.md |
| 14位角色完整字段 | docs/characters.md |
| 七日全部场景、选项、数值与前置 | docs/story_reference.md |
| 人类可读分支设计／逐日表 | docs/branching_design.md、docs/branches_by_day.md |
| 程序可读路由 | data/story.json、data/choices.json；docs/edges.csv |
| 结局算法与优先级 | docs/ending_system.md |
| 168个可用称号与触发思路 | docs/ending_catalog_verified.md |
| 24份完整重点结局文字 | docs/ending_texts.md |
| 视觉与交互规格 | docs/ui_ux.md |
| 技术架构与类型 | docs/technical_architecture.md、src/models.ts |
| 额外挑战落实与边界 | docs/challenges.md |
| 真实测试结果与未验收项 | docs/qa_report.md、tests/report.json |
| 每个称号的七步复现 | tests/witnesses.json |
| 交给下一轮Codex继续开发 | docs/CODEX_HANDOFF.md |

## 修改与构建

运行游戏不需要开发环境；修改源文件和跑测试需要Python 3与Node 18+。本轮使用Python 3.12与Node 24验证。常规构建零npm依赖，**不需要npm install**。

```bash
python scripts/build.py
node tests/exhaustive.cjs
node tests/random.cjs 100000
python scripts/pack.py
node tests/package.cjs
python scripts/reports.py
```

Linux环境也可把`python`换成`python3`。

修改剧情：scripts/content.py；角色与称号：scripts/lore.py；重点尾声：scripts/epilogues.py。这些是编辑源，data中的JSON与部分文档会重新生成。修改规则：src/engine.js；修改界面：src/ui.js与style.css。不要直接修改dist然后期望下次构建保留。

引擎是可独立测试的JavaScript纯函数；models.ts提供正式接口，当前并非完整TypeScript工程。以后可直接把引擎移入React＋TypeScript＋Vite项目，不需要重写内容库。

## 验证范围与未完成项

已通过：全路线合法性／可达性、四选一、实际条件路由分叉、重大罪责不被洗掉、死亡状态延续、数值边界、非法存档拒绝、回放一致性，以及实际打包HTML的脚本与模拟DOM七日流程测试。

**真实浏览器视觉验收未完成**：本次环境缺少浏览器内核，下载也未得到可用安装包。tests/browser.cjs已提供，具备Playwright和浏览器的环境可执行：

```bash
node tests/browser.cjs
```

尚无商业级插画、音乐、云存档、多槽存档、全NPC个人关系／死亡状态系统、完整TypeScript迁移或公开托管。普通动态尾声还有继续文学化编辑的空间。

## 下一步

先在你的电脑打开离线版，完整玩两局，并运行浏览器验收。随后邀请5—8人盲玩，优先重写他们最难理解的选择与最不贴合自身经历的尾声。不要先扩充到300个称号。

把整个项目目录交给Codex，并让它从 **docs/CODEX_HANDOFF.md** 开始接手。
