# V0.2 技术架构

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
