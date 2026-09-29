"""V0.2 evidence, permissions, encounters and editorial decisions."""
TRUTHS={
'hero_identity':('旧勇者的姓名','艾德里安与被称作魔王的承压者是同一人。'),
'abyss_function':('回流的方向','深渊积存被抽离的痛苦，封印压住回流而非消灭敌人。'),
'container_system':('活体承压','容器是仍有意愿的活人；停止与交接需要替代承压。'),
'church_edit':('删改的原件','教会删去了姓名或撤回同意的记录。'),
'kingdom_succession':('王国的继任账','王庭知情并持续为候选人与现任容器调拨资源。'),
'dragon_network':('龙骨泄压网','龙骨与古渠构成支路，出口和风险必须现场核对。'),
'demon_history':('另一方的战史','魔族也有平民与受害记录，军方不等于全部族人。'),
'common_people_cost':('被转移的代价','工程与战争的代价落在具体住户身上。'),
'sword_nature':('剑不作判决','黎明回应愿付生命的意志，不能证明善恶。'),
'goddess_origin':('曙母的权限来源','古代分配意志取得强制征用权限；神性仍未证实。')}
def tids(short):return ['truth_'+s for s in short.split()]
# First-hand / primary-record evidence, awarded on arrival, never globally by day.
NODE_TRUTHS={
'd2_v':'common_people_cost','d3_c_oath':'common_people_cost','d3_c_ledger':'common_people_cost',
'd3_h_oath':'container_system','d3_h_ledger':'church_edit','d3_h_revolt':'demon_history',
'd3_h_guard':'common_people_cost','d3_w_oath':'sword_nature','d3_v_guard':'demon_history',
'd4_c_oath':'kingdom_succession container_system','d4_c_ledger':'kingdom_succession',
'd4_c_revolt':'common_people_cost','d4_c_guard':'hero_identity',
'd4_h_oath':'church_edit','d4_h_ledger':'hero_identity church_edit container_system',
'd4_h_revolt':'hero_identity container_system demon_history','d4_h_guard':'demon_history common_people_cost',
'd4_w_oath':'sword_nature','d4_w_ledger':'abyss_function dragon_network',
'd4_w_revolt':'demon_history common_people_cost','d4_w_guard':'common_people_cost',
'd4_v_oath':'common_people_cost','d4_v_ledger':'common_people_cost dragon_network',
'd4_v_revolt':'common_people_cost','d4_v_guard':'common_people_cost',
'd5_c_ledger':'common_people_cost','d5_h_ledger':'abyss_function goddess_origin',
'd5_w_oath':'hero_identity container_system','d5_w_ledger':'abyss_function dragon_network common_people_cost',
'd5_w_guard':'common_people_cost','d5_v_ledger':'common_people_cost',
'd6_h_ledger':'goddess_origin common_people_cost','d6_h_revolt':'hero_identity container_system',
'd7_h_revolt':'hero_identity container_system'}
CHOICE_TRUTHS={'discovered_abyss':'abyss_function','absorbed_abyss':'abyss_function','received_memory':'hero_identity container_system church_edit','tested_empty_channel':'dragon_network','measured_abyss':'abyss_function','studied_oracle':'goddess_origin','edited_mother_protocol':'goddess_origin','learned_containment':'container_system','tested_burden':'container_system'}
# Explicitly present characters only; names in reports/portraits do not count.
ENCOUNTERS={
'd1_start':[10], 'd2_c':[1,2,11],'d2_h':[3,4,5],'d2_w':[9],'d2_v':[5,10],
'd3_c_oath':[2],'d3_c_ledger':[11],'d3_c_revolt':[12],'d3_c_guard':[5],
'd3_h_oath':[3,4],'d3_h_ledger':[4],'d3_h_revolt':[5,7],'d3_h_guard':[4,6],
'd3_w_oath':[9],'d3_w_ledger':[9],'d3_w_guard':[8,9],
'd3_v_ledger':[5,10],'d3_v_guard':[6,10],
'd4_c_oath':[1],'d4_c_ledger':[4,11],'d4_c_revolt':[12],'d4_c_guard':[2],
'd4_h_oath':[3,4],'d4_h_ledger':[4],'d4_h_revolt':[7,13],'d4_h_guard':[4,6],
'd4_w_oath':[8,9],'d4_w_ledger':[8,9],'d4_w_revolt':[5,7,8],'d4_w_guard':[4,8,9],
'd4_v_oath':[10],'d4_v_ledger':[12],'d4_v_guard':[10],
'd5_c_oath':[1,2],'d5_c_ledger':[11,12],'d5_c_revolt':[12],'d5_c_guard':[2,7],
'd5_h_oath':[3,4],'d5_h_ledger':[4,14],'d5_h_revolt':[5,7],'d5_h_guard':[4],
'd5_w_oath':[8,13],'d5_w_ledger':[9],'d5_w_guard':[8,9],'d5_v_oath':[10],'d5_v_ledger':[6],'d5_v_guard':[10],
'd6_c_oath':[1],'d6_c_ledger':[11,12],'d6_c_revolt':[12],'d6_c_guard':[2],
'd6_h_oath':[3],'d6_h_ledger':[4,14],'d6_h_revolt':[13],'d6_h_guard':[4],
'd6_w_oath':[8],'d6_w_ledger':[9],'d6_w_guard':[9],'d6_v_oath':[10],'d6_v_ledger':[6],'d6_v_guard':[10],
'd7_c_oath':[1],'d7_c_ledger':[11,12],'d7_c_guard':[2],'d7_h_oath':[3],'d7_h_revolt':[13],
'd7_h_guard':[4],'d7_w_oath':[8],'d7_w_ledger':[9],'d7_w_guard':[8],'d7_v_guard':[10],
'd7_w_oath_sword':[8],'d7_c_oath_judgment':[1],'d7_h_oath_dissent':[3]}
INTRO={1:'摄政莱娅',2:'骑士玛伦',3:'教皇瑟文',4:'修女医师伊芙',5:'魔族信使妮娅',6:'魔族工兵萨德',7:'魔族将领瓦尔',8:'守井古龙阿瑟兰',9:'精灵地图师缇尔',10:'村长托马',11:'账房奥伦',12:'印工兼工程师维克',13:'承压者艾德里安',14:'分配意志曙母'}
# protect / sacrifice / red line / bias / error / secret / changeable / unchangeable
VALUES=[
('撤离调度','王室资产与个人权位','让灾民独担家族责任','把集中权力当作唯一效率','默认候选者会同意','父亲失败的选拔','谁持印及如何监督','不以王族身份免责'),
('眼前的护送对象','军职与清白名声','把烧村称为误会','以为纪律能约束一切','执行烧毁哨站的命令','地下平民之死','是否继续带队','罪行应被如实记录'),
('信徒与封印','教职与自身安逸','将拒绝者强推上椅','相信统一祷词能稳定人群','纵容删改退出权','知道部分答复来自机器','仪式与权力配置','不能许诺免除真实代价'),
('伤者获得救治','教职与库存','按种族停药','对政治组织缺乏耐心','曾低估私藏病历的牵连','保存两族原始病历','医院如何管理','救治不等于赦免'),
('证词与平民道路','阵营好感','别人替她答应公开坐标','起初不信人类的担保','没看出地图被军方挪用','图上有军事标记','愿与谁合作','发言权属于自己'),
('桥上的住户','双手与行动自由','把炸桥之罪抹成战绩','相信工具比谈判可靠','炸桥造成平民伤亡','自己的爆破手法','接受审判与指挥','维修不取消赔偿'),
('军队代表权','部下的利益与他人名誉','失去独占谈判位置','将平民支持等同军方授权','扣押同族粮车','和平也能作为军功','有限停火条件','不会被一句劝说放弃权力'),
('幼龙与龙巢','礼仪和有限特权','幼龙被当作无主财产','认为长寿者更有资格决定','祖辈让活人承担本族压力','祖墓是泄压管网','公开责任与轮值','不会自动原谅屠龙'),
('可复核的知识','族籍与秘密','藏起工程误差','以为准确图纸足以说服人','隐去有人居住的出口','曾保护墓地机密','图纸归属','不能删去不利测量'),
('村民休息的机会','代表席与自己的船位','替未归者宣布原谅','先照顾熟悉的住户','曾独自逃离洪灾','旧洪灾的逃生经历','谁来主持村务','普通生活值得被照料'),
('救济线与自身安全','账面名誉','立即切断病村口粮','用善果为手段开脱','让情报贩运共用粮车','救济账也是牟利账','接受外部复核','不会突然不再自辩'),
('民众掌握工具','旧制度与对手权力','钥匙再被贵族收走','把反对派视为破坏者','纵容煽动与集体处决','害怕失去胜利后的席位','是否接受受害者监督','没有自动保证永远温和'),
('停止与重新同意的权利','寿命与名声','把签名解释成永久同意','起初以为接替能终结制度','未预见继任被无限延期','七百年囚禁不是原约定','愿意再等多久','不能因称号被强迫继续'),
('系统稳定目标','被抽取者的个人利益','权限被撤销后不再执行征用','把可计算损失当作全部损失','以稳定覆盖同意','权限来自旧文明建造记录','接口权力可被人限制','神性不能凭停机被证实或否定')]
# Narrow gates replace one slot with an executable alternative; no fifth choice.
GATES={}
def gate(cid,truths,text,flag,result,role=None,all_flags=None,any_flags=None):
    GATES[cid]={'truthsAll':tids(truths),'flagsAll':all_flags or [],'flagsAny':any_flags or [],'fallback':{'text':text,'flag':flag,'consequence':result,'role':role}}
gate('d4_w_oath_1','','接受同伴对承压器的否决权，先不用圣剑作保证。','limited_power','同伴保有叫停权；决策要经过协商。',all_flags=['took_holy_sword'])
gate('d4_w_oath_4','','用脱落鳞片试接阵列，记录仍缺少的剑身数据。','tested_scale_lattice','完成低功率试接；还不能声称验证了圣剑。',all_flags=['took_holy_sword'])
for cid in ['d6_w_ledger_1','d6_c_ledger_1']:
 gate(cid,'abyss_function dragon_network','只启动已有签名的试验支路，留下全网待检记录。','partial_load','局部得到缓冲；全网仍未通过安全与同意核验。',all_flags=['lattice_validated'])
gate('d6_w_oath_2','abyss_function dragon_network','请工程队先辨认备用管道，自己维持原有接口。','requested_channel_audit','工程队收到检修请求；今晚没有增加可用分流。')
gate('d6_h_oath_3','goddess_origin church_edit','封存这座圣堂的征用令，请证人核对总核心来源。','oracle_audit','本堂暂缓征用；其他教区仍使用旧神谕。')
# Global operations need technical provenance; on-site instructions still allow local rescues.
for cid,role in [('d7_w_ledger_1','hero'),('d7_c_ledger_1','hero'),('d7_w_oath_3','hero')]:
 gate(cid,'abyss_function dragon_network','按已核实的局部线路稳住出口，护送维修队撤离。','local_rescue','一段撤离路保住了；全域峰值仍由别处维护。',role)
for cid,role in [('d7_h_ledger_1','guardian'),('d7_h_revolt_2','guardian'),('d7_w_ledger_2','witness'),('d7_c_revolt_3','witness'),('d7_h_oath_dissent_2','hero'),('d7_w_oath_sword_2','guardian')]:
 gate(cid,'goddess_origin','封住已经辨清的本地征用接口，把未知线路留给复核者。','isolated_local_oracle','本地征用暂时停止；总核心仍在运转，记录交给了复核者。',role)
gate('d7_v_ledger_1','abyss_function dragon_network common_people_cost','维持本地木闸和轮值，只接回已经确认的一段水路。','local_shared_watch','本地洪峰被缓住；单一容器制度仍未结束。','guardian',all_flags=['lattice_validated','shared_load'])
gate('d7_v_oath_1','abyss_function dragon_network common_people_cost','签下本地共同守桥协议，从第一班夜岗开始。','local_shared_watch','桥头有了共同看守；承压网络没有因此贯通。','guardian',all_flags=['lattice_validated'],any_flags=['shared_load','protected_refusal','called_volunteers'])
gate('d7_h_revolt_3','hero_identity container_system abyss_function','先续接止痛管，陪医师寻找他能够安全停止的时刻。','supported_previous_hero','疼痛暂时减轻；停止请求尚未兑现，居民撤离继续。','hero',any_flags=['personal_buffer','opened_backup_channel','shared_load','lattice_validated'])
# Named NPC responses: present NPCs can oppose the actual action without abandoning all aid.
REACTIONS={
'killed_demon_child':('npc_05','妮娅收起地图，不再让你代她说明族人的意愿。'),
'sacrificed_innocent':('npc_11','奥伦把被关在外环的住户另抄一册，拒绝将他们只记作损耗。'),
'killed_innocent':('npc_12','维克收走名单；这次处决进入了新政权自己的档案。'),
'forced_volunteers':('npc_10','托马拿走“志愿”二字，要求把征用人的命令写全。'),
'betrayed_strangers':('npc_04','伊芙留下翻到姓名的那一页，不为这次交换作救治证明。'),
'killed_dragon':('npc_08','龙族联络此后改由遗誓使接手；没有人替死者给出宽恕。'),
'fed_on_fear':('npc_09','缇尔要求封存抽取记录，不把功率上升写成无代价的进步。'),
'dragon_priority':('npc_08','阿瑟兰履行承压承诺，人类照护者把不平等条款留在记录中。'),
'lied_for_good':('npc_04','伊芙继续救治，但要求事实另留原件，不能只剩对外说法。')}
# Replace claims unsupported by the former stat-only naming rule.
TITLE_REVISIONS={
'savior_Sacrifice':'曾把自己排在最后的救世主','hero_Ambition':'把权欲带到终点的勇者',
'hero_Freedom':'几度自择道路的勇者','hero_Corruption':'曾借危险力量的勇者',
'vessel_Ambition':'曾争掌控的容器','vessel_Freedom':'带着异议接班的魔王',
'guardian_Corruption':'曾试危险力量的守护者','king_Courage':'几度涉险的国王',
'king_Freedom':'曾经抗命的国王','pontiff_Courage':'愿意涉险的教会领袖',
'pontiff_Sacrifice':'先付过代价的教会领袖','pontiff_Corruption':'曾越过限幅的教会领袖',
'godslayer_Ambition':'曾想掌权的弑神者','godslayer_Faith':'带着旧誓停机的人',
'wanderer_Reason':'惯于求证的远行者','wanderer_Ambition':'带着未竟野心远行的人',
'wanderer_Sacrifice':'几度让步后远行的人','ordinary_Faith':'把旧誓带回日常的人',
'ordinary_Freedom':'自择归处的普通人','ordinary_Corruption':'试过危险力量的普通人',
'martyr_Corruption':'从危险力量走向终夜的人','exile_Faith':'带着旧约离开的人',
'exile_Sacrifice':'付出过代价的流亡者','tyrant_Courage':'曾敢于涉险的暴君',
'tyrant_Mercy':'曾向人伸手的暴君','tyrant_Sacrifice':'付出过自己也征用别人的暴君',
'witness_Sacrifice':'几度付出后的见证者','ferryman_Freedom':'几度抗命的摆渡人',
'dragonkeeper_Corruption':'曾越过界限的养龙人','failed_Reason':'计算之外的失控者',
'blood_ferryman':'载着旧债的摆渡人','blood_dragonkeeper':'仍欠受害者交代的养龙人'}
ARC_REVISIONS={
'coward_to_brave':{'title':'曾经离开，后来折返的人'},
'cruel_to_redeemed':{'title':'交出危险力量的人','early_days':[1,2,3,4],'early_flags_any':['ate_ash','absorbed_abyss']},
'human_supremacist_to_peacemaker':{'title':'从军令走向共同守望','early_flags_any':['requisitioned_horses','formed_militia']},
'conqueror_to_keeper':{'title':'从争取掌控到照料他人'},
'soldier_to_healer':{'early_flags_any':['formed_militia','requisitioned_horses']},
'healer_to_ruler':{'title':'曾经照料别人，如今掌权的人'},
'ruler_to_neighbor':{'title':'放下掌控，另择道路的人'},
'hero_to_tyrant':{'title':'曾敢前行，如今令人跪下'},
'hero_to_demon_king':{'title':'从迎险到接替的人'}
}
ARC_REVISIONS.update({
'selfish_to_selfless':{'title':'从争取掌控到承担代价'},
'faithful_to_heretic':{'early_flags_any':['sought_prophecy','obeyed_church']},
'follower_to_leader':{'early_flags_any':['obeyed_kingdom','obeyed_church']}
})
CHOICE_ENCOUNTERS={'met_previous_hero':[13],'carried_medicine':[13],'befriended_dragon':[8],'learned_containment':[8],'bound_dragon_pact':[8]}
# Traversal-audited revisions: evidence can be learned from concrete late records;
# impossible global actions become fixed local actions, rather than fake locked content.
NODE_TRUTHS['d6_c_ledger']='dragon_network'
NODE_TRUTHS['d6_h_oath']='goddess_origin'
GATES['d6_c_ledger_1']['flagsAll']=[]
GATES['d7_h_revolt_3']['flagsAny'].append('surrendered_power')
GATES['d7_v_oath_1']['flagsAny'].append('open_lattice')
FIXED_LOCAL={cid:GATES.pop(cid)['fallback'] for cid in ['d7_c_revolt_3','d7_h_oath_dissent_2']}
# Final closure: trust and an already evidenced change of conduct also affect affordances.
gate('d7_w_guard_1','','把孩子交给已有的共同照护人，先回营地照顾相识的住户。','assisted_existing_carers','孩子得到有资历者照护；你没有取得龙巢的共同监护权。','ordinary',any_flags=['protected_egg','warmed_egg','raised_dragon','shared_dragon_care','rotating_watch','befriended_dragon'])
GATES['d7_w_guard_1']['relationsMin']={'Dragons':2}
gate('d7_v_guard_3','','与邻人排好三班守夜，先守住最靠近的堤口。','shared_local_shift','近堤有人轮班；你没有独自接下整个外堤的长期守望。','guardian')
GATES['d7_v_guard_3']['arcProgressAny']=['free_to_responsible','selfish_to_selfless','ash_to_restraint']
