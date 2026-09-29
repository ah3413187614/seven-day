# 第七日的勇者 · V0.2

下载并用浏览器直接打开 dist/SeventhDay.html。无需安装、无需启动服务器、无需联网。独立交付的 SeventhDay.html 与此文件相同。

七天，每天一次决定，每处固定四个选择。昨日改变今日处境，重大行为与所见证据长期保留。通关后可再走一局，图鉴只显示已发现的称号。

## 本版范围

89 场景／356 选择／14 NPC／24 弧光／10 真相片段／18 条件选项槽／24 重点尾声包。176 条候选规则中，166 个称号经穷举可触发。称号不是同等数量的独立世界结局：基础身份共 16 类，有限收拢，尾声结合本局动作与相遇生成。

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

最终交付打包：在上述测试与构建完成后运行 `python3 scripts/finalize_v02.py`。它检查报告、同步三个 HTML、生成 SHA-256 清单并验证项目 ZIP；交付文件写在工程的上一级目录。
