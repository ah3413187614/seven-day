from pathlib import Path
import json,sys
from content import *
from lore import *
from epilogues import TEXT
from narrative import SCENES
from systems import *
ROOT=Path(__file__).resolve().parents[1]
def dump(p,v): (ROOT/p).write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
# Keep every final access reachable; this is the accounting-specific preparation.
D6['c_ledger'][2][0]=D6['c_ledger'][2][0].replace('|v_ledger|','|c_ledger|')
FACTIONS={'王国':'Kingdom','教会':'Church','魔族':'Demons','同伴':'Companions','龙族':'Dragons','民众':'People'}
violent={'killed_demon_child','killed_dragon','killed_innocent','sacrificed_innocent','enslaved_core'}
crimes={'killed_demon_child','killed_innocent','sacrificed_innocent','forced_volunteers','forced_load','betrayed_strangers','enslaved_core','fed_on_fear','claimed_abyss'}
flags={}; choices={}; nodes={}
def effect(primary,flag,dest,day):
    stats={primary:3}; rel={}
    if dest in CONTEXTS: rel[FACTIONS[CONTEXTS[dest][2]]]=1
    if flag in crimes:
        stats['Corruption']=stats.get('Corruption',0)+2; stats['Mercy']=stats.get('Mercy',0)-1
        rel['People']=rel.get('People',0)-2;rel['Companions']=rel.get('Companions',0)-1
    if flag=='killed_dragon': rel['Dragons']=-4
    if flag=='saved_demon_child': rel.update({'Demons':2,'Church':-1})
    if flag in ['befriended_dragon','kept_dragon_care','shared_dragon_care']: rel['Dragons']=2
    if flag in ['betrayed_companion','betrayed_strangers']:rel['Companions']=-3
    if primary=='Sacrifice': rel['Companions']=rel.get('Companions',0)+1
    return stats,rel

def add_node(day,key,title,scene,rows):
    nid=f'd{day}_{key}'; ids=[]
    for i,row in enumerate(rows):
        text,dest,primary,flag,consequence=row.split('|') if isinstance(row,str) else row
        cid=f'{nid}_{i+1}';ids.append(cid)
        actual=consequence.split('；'); gain=actual[0];cost='；'.join(actual[1:]) or '你放弃同日其他三项行动。'
        stats,rel=effect(primary,flag,dest,day)
        next_id=f'd{day+1}_{dest}' if day<7 else None
        flags.setdefault(flag,{'id':flag,'description':text,'irreversible':True,'isCrime':flag in crimes,'isViolent':flag in violent})
        choices[cid]={'choice_id':cid,'node_id':nid,'visibility':'PLAYER_VISIBLE','text':text,'understanding':gain+'，同时接受：'+cost,'consequence':consequence,'gain':gain,'cost':cost,'DESIGNER_ONLY':{'primary':primary,'stat_change':stats,'relationship_change':rel,'add_flags':[flag],'remove_flags':[], 'arc_tags':[primary.lower()]+(['harm'] if flag in crimes else []),'long_term':('下一日获得'+CONTEXTS[dest][1]+'的入口；行为永久保留在弧光与结局证据中。') if dest in CONTEXTS else ('下一日进入'+dest+'起始路线。') if day<7 else '终局身份为'+ROLES[dest][0]+'；前六天人格与罪责继续覆盖称号。'},'next_node':next_id,'terminal_role':dest if day==7 else None}
    nodes[nid]={'node_id':nid,'day':day,'title':title,'scene':SCENES[nid],'location':CONTEXTS[key][0] if key in CONTEXTS else {'start':'故乡岔路','c':'王都','h':'圣辉教会','w':'精灵旧林','v':'故乡渡口'}.get(key,key),'visibility':'PLAYER_VISIBLE','previous_requirement':{'day':day,'any_previous_choice':[]},'on_enter_flags':[],'choices':ids}
add_node(1,'start','第七声钟响之前','召集令钉在故乡的门上，雨水把“勇者”两个字浸得发黑。七天后，魔王的封印将崩塌。王国承诺土地、金钱与史书中的名字，教会承诺祝福。托马没有承诺任何东西，只把一箱修桥的工具放在门边。你还没有被谁选中，也不知道召集令背后隐藏着什么。天亮以后，你只能赶往一个地方。',D1)
for day,data in [(2,D2),(3,D3),(4,D4),(5,D5),(6,D6),(7,D7)]:
    for key,(title,scene,rows) in data.items():add_node(day,key,title,scene,rows)
variants={}
for parent,suffix,condition,title,scene,rows in FINAL_VARIANTS:
    key=parent+'_'+suffix
    add_node(7,key,title,scene,rows)
    nodes['d7_'+key]['location']=CONTEXTS[parent][0]
    nodes['d7_'+key]['previous_requirement']['flags']=condition
    variants.setdefault('d7_'+parent,[]).append({'nodeId':'d7_'+key,'flags':condition})
for c in choices.values():
    if c['next_node']: nodes[c['next_node']]['previous_requirement']['any_previous_choice'].append(c['choice_id'])
    for v in variants.get(c['next_node'],[]): nodes[v['nodeId']]['previous_requirement']['any_previous_choice'].append(c['choice_id'])
assert set(nodes)==set(SCENES), 'Every existing node must have exactly one V0.2 scene'
for nid,n in nodes.items():
    n['truths']=tids(NODE_TRUTHS.get(nid,''))
    n['encounters']=[f'npc_{i:02}' for i in ENCOUNTERS.get(nid,[])]
    if '_c_guard' in nid:n['location']='撤离山路'
    if '_v_revolt' in nid:n['location']='安全领与城外营地'
    if nid=='d6_v_guard':n['location']='临时灶与末班渡口'
for cid,c in choices.items():
    if cid in FIXED_LOCAL:
        f=FIXED_LOCAL[cid];c.update(text=f['text'],consequence=f['consequence'],gain=f['consequence'].split('；')[0],cost=f['consequence'].split('；')[1],terminal_role=f['role'])
        c['DESIGNER_ONLY']['add_flags']=[f['flag']]
        flags[f['flag']]={'id':f['flag'],'description':f['text'],'irreversible':True,'isCrime':False,'isViolent':False}
    old=c['DESIGNER_ONLY']['add_flags'][0]
    if old=='measured_abyss':
        c['consequence']='测量显示黑潮沿管道回流，活体负荷随支路泄压下降；全城看见圣灯熄灭。'
    if old=='studied_oracle':
        c['consequence']='学者用建造铭牌与权限表核对出曙母的分配来源；各方争抢解释权。'
    if old in ['measured_abyss','studied_oracle']:
        c['gain'],c['cost']=c['consequence'].split('；')

    if old=='learned_truth':
        new='held_succession_record' if cid=='d4_c_oath_2' else 'published_original_record'
        c['DESIGNER_ONLY']['add_flags']=[new]
        flags[new]={'id':new,'description':c['text'],'irreversible':True,'isCrime':False,'isViolent':False}
    c['truths']=tids(CHOICE_TRUTHS.get(old,''))
    c['encounters']=[f'npc_{i:02}' for i in CHOICE_ENCOUNTERS.get(old,[])]
    if cid=='d4_v_guard_3':c['text']='循记忆中的旧渠，去查山腹里是谁在传来回声。'
    if cid in GATES:
        g=GATES[cid];fb=g['fallback'];d=c['DESIGNER_ONLY'].copy()
        d.update(add_flags=[fb['flag']],remove_flags=[],long_term='采用证据不足时的局部行动；不会授予原操作成果。')
        d['stat_change'],d['relationship_change']=effect(d['primary'],fb['flag'],fb['role'] or c['next_node'].removeprefix('d'+str(nodes[c['node_id']]['day']+1)+'_'),nodes[c['node_id']]['day']) if c['next_node'] else effect(d['primary'],fb['flag'],fb['role'],7)
        result=fb['consequence'].split('；')
        c['requirement']={k:v for k,v in g.items() if k!='fallback'}
        c['fallback']={'text':fb['text'],'consequence':fb['consequence'],'gain':result[0],'cost':'；'.join(result[1:]),'DESIGNER_ONLY':d,'truths':[],'encounters':[],'terminal_role':fb['role'] or c['terminal_role']}
        flags[fb['flag']]={'id':fb['flag'],'description':fb['text'],'irreversible':True,'isCrime':False,'isViolent':False}
flags.pop('learned_truth',None)
for c in choices.values():
    c['understanding']=c['gain']+'，同时接受：'+c['cost']
    if c['terminal_role']:c['DESIGNER_ONLY']['long_term']='终局身份为'+ROLES[c['terminal_role']][0]+'；条件不齐时执行 fallback，罪责仍保留。'

FIRST_MEETING_LABELS=['摄政 · 主持王庭事务', '骑士队长 · 护送召集者', '教皇 · 主持圣堂', '修女医师 · 照护伤病者', '魔族信使 · 在边境传递消息', '魔族工兵 · 熟悉工事', '魔族将领 · 代表诸部', '古龙 · 守着龙井', '学者 · 绘制地图与管道', '村长兼木匠 · 留守故乡', '账房 · 核对账册', '印工兼工程师 · 修造与印刷', '封印中的承压者', '神谕中的声音']
characters=[]
for i,row in enumerate(NPCS):
    characters.append(dict(zip(['name','race','identity','personality','surface_goal','true_goal','secret','possible_relations','fates','related_endings','routes','signature_line'],row),character_id=f'npc_{i+1:02}'))
for i,c in enumerate(characters):
    c["firstMeetingLabel"]=FIRST_MEETING_LABELS[i]
    c['values']=dict(zip(['protects','will_sacrifice','red_line','bias','mistake','secret','can_change','cannot_change'],VALUES[i]))
    c['introduction']=INTRO[i+1]
endings=[]
for role,row in TITLE_ROWS.items():
    assert len(row.split('|'))==8
    for stat,title in zip(STATS,row.split('|')):
        endings.append({'ending_id':f'{role}_{stat}','title':title,'category':role,'type':'normal','priority':10,'trigger':{'role':role,'dominant':stat},'meaning':ROLES[role][1],'visibility':'DESIGNER_ONLY'})
BLOOD=['染血的救世主','有瑕疵的勇者','背负罪责的魔王','欠着名字的守护者','以他人代价加冕的国王','仍须受审的教会领袖','不能自赦的弑神者','带着欠债远行的人','不能洗去过去的普通人','不能以死抵罪的殉道者','仍被旧债追赶的流亡者','被歌颂的刽子手','也在证词之中的见证者','曾经拒渡的摆渡人','欠人类一场道歉的养龙人','把别人也拖入深渊的人']
for (role,_),title in zip(ROLES.items(),BLOOD):
    endings.append({'ending_id':'blood_'+role,'title':title,'category':role,'type':'contradictory','priority':90,'trigger':{'role':role,'anyCrime':True},'meaning':'最后救援不抹去重大罪责；尾声保留具体伤害证据。','visibility':'DESIGNER_ONLY'})
arcs=[]
for aid,title,early,late,roles,early_flags,late_flags,priority in ARCS:
    arc={'arc_id':aid,'title':title,'early':early,'late':late,'roles':roles,'early_flags_any':early_flags,'late_flags_any':late_flags,'priority':priority,'early_days':[1,2,3],'late_days':[5,6,7],'early_min':1,'late_min':2}
    arc.update(ARC_REVISIONS.get(aid,{}))
    arc['pivot_required']=True
    arc['pivot_days']=[3,4,5,6]
    title=arc['title']
    arcs.append(arc)
    endings.append({'ending_id':'arc_'+aid,'title':title,'category':'arc','type':'growth','priority':70,'trigger':arc,'meaning':f'早段有{early}行动，后段至少两次{late}行动，并符合身份与特定行为证据。','visibility':'DESIGNER_ONLY'})
specials=[('cycle_ended','终结轮回的人','true','savior','二周目已通关至少一次；lattice_validated + shared_load + collective_final；持回流、龙骨网络、平民代价三项来源证据；无强征、重大罪责。'),('swordless','没有圣剑的勇者','secret','hero','拒绝过圣剑；从未取得；终局为勇者。'),('forgotten','被世界遗忘的守护者','secret','guardian','erased_hero_credit；此前至少三次牺牲行动；终局守护者。'),('never_drew','从未拔剑的勇者','secret','hero','从未取得圣剑、无暴力行为、广场主动降温且取消讨伐护送。'),('gods_blade','神明的利剑','secret','hero','持圣剑，早六日信仰行动至少三次，终局救援且无罪责。'),('clear_mad','清醒的疯子','bad','failed','失控结局且理智为早六日最高维度。'),('last_ordinary','最后的普通人','secret','ordinary','拒绝召集+拒绝一切封号；最终选择普通人生。'),('ash_restrained','清醒地封住深渊的人','secret','vessel','吸收黑潮+交出控制权、自毁锁或自断腐化；自愿成为容器。')]
for eid,title,typ,role,trigger in specials:endings.append({'ending_id':'special_'+eid,'title':title,'category':role,'type':typ,'priority':100 if eid=='cycle_ended' else 80,'trigger_text':trigger,'meaning':ROLES[role][1],'visibility':'DESIGNER_ONLY'})
PREMIUM_ENDINGS={'special_cycle_ended','special_forgotten','special_clear_mad','arc_coward_to_martyr','arc_hero_to_tyrant','vessel_Mercy','tyrant_Mercy','special_swordless'}
for c in characters:c['spriteKey']=c['character_id']
for n in nodes.values():
    n['characterIds']=list(n.get('encounters',[]))
    n['musicKey']='final_day' if n['day']==7 else 'tension' if n['day']==6 else 'normal'
for e in endings:
    e['artType']='premium' if e['ending_id'] in PREMIUM_ENDINGS else 'none'
    e['artKey']=e['ending_id'] if e['artType']=='premium' else None
    e['musicKey']='ending'
for e in endings:
    e['title']=TITLE_REVISIONS.get(e['ending_id'],e['title'])
    if e['type']=='growth': e['meaning']='早段行动、其后中段转向、晚段至少两次行动及终局身份共同验证；不以最终分数代替经历。'
packets=[]
for line in TEXT.strip().splitlines():
    cols=line.split('|');assert len(cols)==7,line
    packets.append(dict(zip(['number','title','main','npc','world','self','last'],cols)))
# The packet featured title is an authored display variant; actual runtime title is always the resolved rule.
dump('data/story.json',{'schemaVersion':2,'start':'d1_start','nodes':list(nodes.values()),'variants':variants})
dump('data/choices.json',{'schemaVersion':2,'choices':list(choices.values())})
dump('data/characters.json',{'characters':characters})
dump('data/endings.json',{'schemaVersion':2,'rules':endings,'roles':{k:{'name':v[0],'world':v[1]} for k,v in ROLES.items()},'stats':dict(zip(STATS,STAT_CN))})
dump('data/arcs.json',{'arcs':arcs})
dump('data/flags.json',{'flags':list(flags.values())})
dump('data/epilogues.json',{'packets':packets})
bundle={'story':{'start':'d1_start','nodes':nodes},'choices':choices,'characters':characters,'endings':endings,'roles':{k:{'name':v[0],'world':v[1]} for k,v in ROLES.items()},'arcs':arcs,'flags':flags,'packets':packets,'stats':dict(zip(STATS,STAT_CN)),'variants':variants,'truths':{'truth_'+k:{'id':'truth_'+k,'name':v[0],'description':v[1]} for k,v in TRUTHS.items()},'reactions':REACTIONS}
bundle['proseVariants']=json.loads((ROOT/'data/prose_variants.json').read_text(encoding='utf-8'))
dump('data/truths.json',bundle['truths'])
dump('data/bundle.json',bundle)
# Generated reference docs are data-derived; editable authoring source stays under scripts/.
(ROOT/'docs/characters.md').write_text('# 角色圣经（DESIGNER_ONLY）\n\n'+'\n\n'.join('## '+c['name']+'\n\n'+'\n'.join('- **'+k+'**：'+str(v) for k,v in c.items() if k not in ['name','character_id']) for c in characters),encoding='utf-8')
(ROOT/'docs/story_reference.md').write_text('# 七日全节点策划（DESIGNER_ONLY）\n\n'+'\n\n'.join('## '+n['node_id']+' · '+n['title']+'\n\n'+n['scene']+'\n\n前置：'+(' / '.join(n['previous_requirement']['any_previous_choice']) or '开始游戏')+'\n\n'+'\n\n'.join('### '+choices[c]['choice_id']+' · '+choices[c]['text']+'\n\n当下理解：'+choices[c]['understanding']+'\n\n实际后果：'+choices[c]['consequence']+'\n\n下一节点：'+str(choices[c]['next_node'])+'；终局身份：'+str(choices[c]['terminal_role'])+'\n\n策划效果：`'+json.dumps(choices[c]['DESIGNER_ONLY'],ensure_ascii=False)+'`' for c in n['choices']) for n in nodes.values()),encoding='utf-8')
(ROOT/'docs/ending_catalog.md').write_text('# 结局称号库（DESIGNER_ONLY）\n\n这是候选规则库；实际可达性以 tests/report.json 为准，不以条目数冒充可达数量。\n\n| ID | 称号 | 类型 | 触发条件 |\n|---|---|---|---|\n'+'\n'.join('| '+e['ending_id']+' | '+e['title']+' | '+e['type']+' | '+json.dumps(e.get('trigger',e.get('trigger_text')),ensure_ascii=False).replace('|','／')+' |' for e in endings),encoding='utf-8')
(ROOT/'docs/ending_texts.md').write_text('# 24 份重点结局正式文案\n\n核心文本是尾声模块；程序始终追加实际行为证据，NPC段落只由本局 encounterLog 中的相遇、死亡、关系与行为生成。包内 NPC 栏是生成约定，不是无条件播出的范文。不能把预写范文当作无条件事实。\n\n'+'\n\n'.join('## '+p['number']+'《'+p['title']+'》\n\n'+'\n\n'.join('**'+k+'**\n\n'+p[f] for k,f in [('主结局','main'),('NPC 后日谈','npc'),('世界后日谈','world'),('个人后日谈','self'),('最后一句','last')]) for p in packets),encoding='utf-8')
# complete edge list and separate compact chapter diagrams
(ROOT/'docs/edges.csv').write_text('from,choice,to\n'+'\n'.join(f"{c['node_id']},{c['choice_id']},{c['next_node'] or ('END:'+c['terminal_role'])}" for c in choices.values()),encoding='utf-8')
print(json.dumps({'nodes':len(nodes),'choices':len(choices),'rules':len(endings),'arcs':len(arcs),'characters':len(characters),'packets':len(packets)},ensure_ascii=False))
