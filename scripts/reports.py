from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'data/bundle.json').read_text());r=json.loads((R/'tests/report.json').read_text());rr=json.loads((R/'tests/random-report.json').read_text());w=json.loads((R/'tests/witnesses.json').read_text())
lines=['# 逐日分支转移表（由实际数据生成）','', '完整对白与效果另见story_reference.md；条件变体见最后一表。']
for day in range(1,8):
 lines+=['',f'## 第{day}日','','| 节点 | 行动 | 下一日／终局 |','|---|---|---|']
 for n in d['story']['nodes'].values():
  if n['day']!=day:continue
  for cid in n['choices']:
   c=d['choices'][cid];target=c['next_node'] or ('终局：'+d['roles'][c['terminal_role']]['name'])
   lines.append('| '+n['node_id']+' '+n['title']+' | '+c['text']+' | '+target+' |')
lines+=['','## 条件入口替换','','| 基础入口 | 条件 | 替换节点 |','|---|---|---|']
for base,variants in d.get('variants',{}).items():
 for v in variants:lines.append('| '+base+' | '+json.dumps(v['flags'],ensure_ascii=False)+' | '+v['nodeId']+' |')
(R/'docs/branches_by_day.md').write_text('\n'.join(lines),encoding='utf-8')
counts={k:len(v['titles']) for k,v in r['runs'].items()}
rare=sorted(r['runs']['replay']['titles'].items(),key=lambda t:t[1])[:10]
qa=f'''# QA与内容审查报告

本报告由实际测试输出整理，不把未执行的浏览器脚本算通过。

## 已执行结果

| 项目 | 结果 |
|---|---:|
| 可达剧情节点 | {r['reachableNodes']} / {r['nodes']} |
| 可达行动 | {r['reachableChoices']} / {r['choices']} |
| 每种周目枚举路径 | 16,384 |
| 两种周目总枚举路径 | 32,768 |
| 首周目可触发称号 | {counts['first']} |
| 含二周目的可触发称号 | {r['reachableTitles']} |
| 可检测人物弧光 | {r['detectableArcs']} / {r['arcs']} |
| 二周目真结局路径 | {r['runs']['replay']['truePaths']} |
| 随机模拟局数 | {rr['runs']} |
| 随机模拟发现称号 | {len(rr['endingFrequency'])} |
| 随机模拟发现节点／行动 | {len(rr['nodeFrequency'])} / {len(rr['choiceFrequency'])} |

穷举覆盖全部路线，不存在未知概率导致的漏查。随机模拟使用固定种子{rr['initialSeed']}，选择均匀，不将它解释为真实玩家行为分布。真结局的均匀二周目路径比例约{r['runs']['replay']['truePaths']/16384*100:.3f}%。

## 修复与审查

| 检查项 | 审查结果与已执行修改 |
|---|---|
| 明显正确答案 | 所有356行动都有即时收益与代价；未做玩家盲测，不宣称每项已绝对平衡 |
| 无意义选项 | 每项推进路径或终局身份并记录行为；不使用纯“善恶+1”空动作 |
| 换词四选一 | 人工分别写出军粮、医疗、撤离、龙卵、审判、承压等具体冲突；每菜单去往四个不同下一处境 |
| 昨日影响今日 | 静态和实际状态转移都断言四个不同目标；再追加圣剑、屠龙、旧罪、异议者四个条件终局 |
| 过早锁线 | 每日允许跨地点与合作对象移动；没有永久职业或阵营锁 |
| 假分支 | 明示有限收拢；物品与重大行为不清空；终局使用完整历史，不把16384路线说成16384篇不同故事 |
| 世界矛盾 | 明确700年同一容器；历代“勇者”是候选者；一次缓冲不等于永久根治 |
| 教会脸谱化 | 同时承担救治、档案维护、隐瞒和强征；领导者可以辞职与自愿承压 |
| 魔族洗白 | 军阀扣押粮车、工兵有战争责任；受害历史不等于免于追责 |
| 第七日履历影响 | 16基础菜单加4条件菜单；有剑、无剑、屠龙和被问责的权限不同 |
| 结局对应行为 | 按身份、前六日人格、早晚行动转变、不可撤销罪责、关系与死亡生成 |
| 随机称号 | 176条固定候选白名单；只把{r['reachableTitles']}条经穷举可达的称号计入图鉴 |
| 人物复活 | 屠龙永久保留，后续由遗誓使接洽；NPC后日谈重写死亡状态；增加独立赔偿终局 |
| 规则不可达 | 修正无入口的账房终局、赎罪弧光及两个隐藏条件；被必然覆盖的普通称号转为设计储备 |
| 实际交付HTML | 检出并修正打包时的占位替换冲突；对内嵌脚本、数据、引擎与模拟DOM七日操作验证通过 |

## 仍未验收

真实浏览器视觉、移动端溢出、系统文件下载、读屏与实际键盘焦点：未完成。本环境没有浏览器内核，安装下载未得到可用文件。tests/browser.cjs已经写好；tests/package.cjs验证实际打包HTML与模拟DOM交互，但不替代渲染测试。

音乐、动画演出、多人云存档、所有NPC的复杂死亡分支、真实玩家叙事满意度：未实现／未验证。原型可完整运行，不等于商业发行成品。

## 不计入图鉴的设计储备

以下普通条目被更具体称号覆盖，或当前没有可达的属性／路线组合。已设置reachable=false，不占用玩家可收集总数。扩展路由前不能把它们列作有效结局。

| ID | 储备称号 |
|---|---|
'''
qa+='\n'.join('| '+e['id']+' | '+e['title']+' |' for e in r['unreachableTitles'])
qa+='\n\n## 稀有规则分布（均匀枚举，不是玩家概率）\n\n| 称号 | 二周目路径数 |\n|---|---:|\n'
qa+='\n'.join('| '+next(e['title'] for e in d['endings'] if e['ending_id']==eid)+' | '+str(n)+' |' for eid,n in rare)
qa+='\n\n每个有效称号的七步复现见证在 tests/witnesses.json；完整频率见 tests/report.json 和 random-report.json。\n'
(R/'docs/qa_report.md').write_text(qa,encoding='utf-8')
# Focus the readable catalog on verified usable titles; keep raw rules in JSON.
lines=['# 可用称号库（经穷举验证）','',f'共{r["reachableTitles"]}条可触发称号。以下每条都能在tests/witnesses.json找到七步路径。候选储备不计入。','']
for category in list(d['roles'])+['arc']:
 items=[e for e in d['endings'] if e['category']==category and e['ending_id'] in w]
 if not items:continue
 lines += ['## '+(d['roles'][category]['name'] if category in d['roles'] else '人物弧光'),'', '| ID | 称号 | 触发思路 |','|---|---|---|']
 for e in items:
  text=e.get('trigger_text') or e['meaning']
  trigger=e.get('trigger',{})
  if 'dominant' in trigger:text='身份为'+d['roles'][category]['name']+'；前六日'+d['stats'][trigger['dominant']]+'主导；未被更高优先级规则覆盖。'
  lines.append('| '+e['ending_id']+' | '+e['title']+' | '+text+' |')
 lines.append('')
(R/'docs/ending_catalog_verified.md').write_text('\n'.join(lines),encoding='utf-8')
print('Generated branch tables, QA and verified title catalog.')
