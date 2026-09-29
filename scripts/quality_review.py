"""Reproducible editorial inventory; ratings are provisional design judgments."""
from pathlib import Path
from collections import Counter
import json
from systems import TITLE_REVISIONS,ARC_REVISIONS
R=Path(__file__).resolve().parents[1]
b=json.loads((R/'archive/bundle_v01.json').read_text());br=json.loads((R/'archive/report_v01.json').read_text());n=json.loads((R/'data/bundle.json').read_text());nr=json.loads((R/'tests/report.json').read_text())
old_inactive={e['id'] for e in br['unreachableTitles']};new_inactive={e['id'] for e in nr['unreachableTitles']};new={e['ending_id']:e for e in n['endings']}
D={'blood_ferryman','blood_dragonkeeper','arc_soldier_to_healer','arc_healer_to_ruler','arc_ruler_to_neighbor','arc_human_supremacist_to_peacemaker','arc_cruel_to_redeemed'}
rows=[]
for e in b['endings']:
 id=e['ending_id']
 if id in old_inactive:continue
 changed=e['title']!=new[id]['title'];isarc=id.startswith('arc_')
 if id in D:before='D';issue='旧称号／触发条件声称了未必发生的行为或身份，需要改名或收紧证据。'
 elif e['type']=='normal':before='C';issue='常规称号套用身份摘要，个人段重复起始选择；需要事件化收束，部分题名含额外断言。'
 elif isarc and id.removeprefix('arc_') in ARC_REVISIONS:before='C';issue='转变方向可用，起点措辞或中段证据不足。'
 elif e['type']=='true':before='S';issue='保留共同承担与永久制度改变；补齐来源、试验和同意权限。'
 else:before='A';issue='主题与行为组合可辨认；尾声仍需限制未遇 NPC、清理主观代言。'
 after='S' if e['type']=='true' else 'B' if e['type']=='normal' else 'A'
 action=('题名改为《'+new[id]['title']+'》；' if changed else '')+('增加早—中—晚次序与指定动作审核；' if isarc else '')+'采用 V0.2 尾声包、已遇 NPC 和本局事件。'
 if id in new_inactive:action+=' 当前权限／优先级下不可达，移出图鉴并保留为储备。'
 rows.append({'id':id,'oldTitle':e['title'],'newTitle':new[id]['title'],'before':before,'after':after,'issue':issue,'action':action,'active':id not in new_inactive,'titleChanged':changed})
counts=lambda field:dict(sorted(Counter(x[field] for x in rows).items()))
summary={'audited':len(rows),'before':counts('before'),'after':counts('after'),'titlesChanged':sum(x['titleChanged'] for x in rows),'packetsRewritten':24,'oldReachable':br['reachableTitles'],'newReachable':nr['reachableTitles'],'newlyInactive':sorted(new_inactive-old_inactive)}
(R/'tests/quality-report-v02.json').write_text(json.dumps({'summary':summary,'rows':rows},ensure_ascii=False,indent=2))
lines=['# V0.2 结局质量复审','', '这是设计编辑评级，不是玩家满意度成绩。逐项覆盖 V0.1 的 168 个活跃称号；候选总数仍为 176，没有新增凑数。','',
'评级：S＝机制与主题形成独特结果；A＝具体行为或制度冲突清楚；B＝可用但共享身份尾声，仍有模板感；C＝需要重写或补足行为证据；D＝与可能履历矛盾。所有 A/B 仍待真人阅读复核。','',
'| 口径 | 数量 |','|---|---:|',f'| 旧版活跃条目审核 | {len(rows)} |',f'| 正式称号改写 | {summary["titlesChanged"]} |','| 完整重点尾声包改写 | 24 |',f'| V0.2 穷举活跃称号 | {nr["reachableTitles"]} |','',
'| 等级 | 修改前 | 修改后 |','|---|---:|---:|']
for g in 'SABCD':lines.append(f'| {g} | {summary["before"].get(g,0)} | {summary["after"].get(g,0)} |')
lines += ['', '修改后评级仍以同一组 168 条为分母，储备项的文本评级不表示可触发。常规条目使用 16 类共享身份包与本局事件，不声称写出了 168 篇独立长结局。原 C/D 的修订可能改正文、题名或判定；不靠增加条目回避问题。','',
'## 可达性变动','', '新增储备：'+('、'.join(summary['newlyInactive']) or '无')+'。权限限制使缺少知识的全域操作改为局部结果，严格的弧光规则又优先覆盖部分普通称号。保留候选 ID 供审阅，但不列入图鉴。完整候选不可达表见 qa_report.md。','',
'新增储备的具体原因：failed_Corruption 的旧入口包含强制抽取恐惧；补记重大罪责后由 blood_failed 等更具体规则覆盖。godslayer_Corruption 缺少能同时满足前六日腐化主导与合法停机知识的路线；缺证时执行局部替代行动。二者保留候选 ID、移出活跃图鉴，是主动修正，不恢复旧漏洞。', '', '## 当前最终活跃条目快审', '', '最终活跃称号均有合法七步见证。C／D 级遗留已通过题名、条件或共享尾声包修订；B 级仍承认共享身份模板的局限，不冒充独立长结局。重大罪责仍可产生真正的行为转向结局，专项检测找到带罪责的赎罪路径并保留伤害附记。', '', '## 168 条逐项表','', '| ID | 原称号 → V0.2 | 前／后 | 问题 | 修订 |','|---|---|---|---|---|']
for x in rows:lines.append('| '+x['id']+' | '+x['oldTitle']+' → '+x['newTitle']+' | '+x['before']+'／'+x['after']+' | '+x['issue']+' | '+x['action']+' |')
(R/'docs/ending_quality_review.md').write_text('\n'.join(lines))
print(json.dumps(summary,ensure_ascii=False))
