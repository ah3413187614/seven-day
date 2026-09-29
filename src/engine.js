/* Deterministic game core. No DOM, randomness, network, or stored stat trust. */
(function(root){
'use strict';
function createEngine(data){
  const statKeys=Object.keys(data.stats), factionKeys=['Kingdom','Church','Demons','Companions','Dragons','People'];
  const clone=x=>JSON.parse(JSON.stringify(x));
  const roleOrder=Object.keys(data.roles);
  function grant(state,ids,source,evidence){
    for(const id of ids||[])if(!state.truths.includes(id)){
      if(!data.truths[id])throw Error('未定义真相 '+id);
      state.truths.push(id);state.knowledgeLog.push({id,day:state.day,source,evidence});
    }
  }
  function enter(state){
    const n=data.story.nodes[state.nodeId];
    grant(state,n.truths,n.node_id,n.scene);
    for(const id of n.encounters||[]){
      if(id==='npc_08'&&state.flags.includes('killed_dragon'))continue;
      if(!state.metNPCs.includes(id)){state.metNPCs.push(id);state.encounterLog.push({id,day:state.day,nodeId:n.node_id});}
    }
    return state;
  }
  function initial(meta={}) {return enter({schemaVersion:2,nodeId:data.story.start,day:1,stats:Object.fromEntries(statKeys.map(k=>[k,0])),relations:Object.fromEntries(factionKeys.map(k=>[k,0])),flags:[],truths:[],knowledgeLog:[],metNPCs:[],encounterLog:[],history:[],finished:false,role:null,meta:{completedRuns:Math.max(0,Math.min(100000,Number(meta.completedRuns)||0))}});}
  function arcProgress(state,id){
    const a=data.arcs.find(a=>a.arc_id===id);if(!a)return false;
    return state.history.some(h=>a.early_days.includes(h.day)&&h.primary===a.early&&(!a.early_flags_any.length||a.early_flags_any.some(f=>h.flags.includes(f)))&&state.history.some(p=>p.day>h.day&&a.pivot_days.includes(p.day)&&p.primary===a.late));
  }
  function permitted(state,r){return !r||((r.truthsAll||[]).every(t=>state.truths.includes(t))&&(r.flagsAll||[]).every(f=>state.flags.includes(f))&&(!(r.flagsAny||[]).length||r.flagsAny.some(f=>state.flags.includes(f)))&&Object.entries(r.relationsMin||{}).every(([k,v])=>(state.relations[k]||0)>=v)&&(!(r.arcProgressAny||[]).length||r.arcProgressAny.some(id=>arcProgress(state,id))));}
  function resolveChoice(state,id){const c=data.choices[id];if(!c)throw Error('未定义行动');return permitted(state,c.requirement)?{...c,mode:'full'}:{...c,...c.fallback,mode:'limited'};}
  function node(state){ if(state.finished)return null;const n=data.story.nodes[state.nodeId];if(!n||n.day!==state.day)throw Error('剧情状态无效');return n; }
  function apply(state,choiceId){
    if(state.finished)throw Error('本局已经结束');
    const n=node(state), c=resolveChoice(state,choiceId);
    if(!n.choices.includes(choiceId)||!c)throw Error('不能选择当前节点之外的行动');
    const next=clone(state), before={stats:clone(state.stats),relations:clone(state.relations)};
    const d=c.DESIGNER_ONLY;
    for(const [k,v] of Object.entries(d.stat_change))next.stats[k]=Math.max(-21,Math.min(35,(next.stats[k]||0)+v));
    for(const [k,v] of Object.entries(d.relationship_change))next.relations[k]=Math.max(-20,Math.min(20,(next.relations[k]||0)+v));
    next.flags=[...new Set([...next.flags,...n.on_enter_flags,...d.add_flags])];
    grant(next,c.truths,choiceId,c.consequence);
    for(const id of c.encounters||[])if(!next.metNPCs.includes(id)&&!(id==='npc_08'&&next.flags.includes('killed_dragon'))){next.metNPCs.push(id);next.encounterLog.push({id,day:state.day,nodeId:n.node_id,choiceId});}
    next.history.push({day:state.day,nodeId:n.node_id,choiceId,mode:c.mode,stat_change:clone(d.stat_change),primary:d.primary,text:c.text,consequence:c.consequence,flags:[...d.add_flags],before,after:{stats:clone(next.stats),relations:clone(next.relations)}});
    if(c.next_node){next.nodeId=c.next_node;for(const v of data.variants?.[c.next_node]||[]){const req=v.flags;if((!req.all||req.all.every(f=>next.flags.includes(f)))&&(!req.any||req.any.some(f=>next.flags.includes(f)))&&(!req.none||req.none.every(f=>!next.flags.includes(f)))){next.nodeId=v.nodeId;break;}}next.day++;if(!data.story.nodes[next.nodeId])throw Error('缺失后续节点');next.flags=[...new Set([...next.flags,...data.story.nodes[next.nodeId].on_enter_flags])];}
    if(c.next_node)enter(next);
    else {if(state.day!==7||!c.terminal_role)throw Error('不能提前结局');next.finished=true;next.role=c.terminal_role;next.nodeId=null;}
    return next;
  }
  const any=(a,b)=>a.some(x=>b.includes(x));
  function arcsFor(state){
    return data.arcs.filter(a=>{
      if(!a.roles.includes(state.role))return false;
      const early=state.history.filter(h=>a.early_days.includes(h.day));
      const late=state.history.filter(h=>a.late_days.includes(h.day));
      const starts=early.filter(h=>h.primary===a.early&&(!a.early_flags_any.length||any(a.early_flags_any,h.flags)));
      const ends=late.filter(h=>h.primary===a.late);
      if(starts.length<a.early_min||ends.length<a.late_min||a.late_flags_any.length&&!any(a.late_flags_any,late.flatMap(h=>h.flags)))return false;
      // A turn needs an earlier act, a distinct intervening act, and later reinforcement.
      return starts.some(start=>state.history.some(p=>a.pivot_days.includes(p.day)&&p.day>start.day&&p.primary===a.late&&ends.some(end=>end.day>p.day)));
    }).sort((a,b)=>b.priority-a.priority||a.arc_id.localeCompare(b.arc_id));
  }
  function dominant(state){
    // Day 7 defines identity, never single-handedly rewrites the earlier personality.
    const scores=Object.fromEntries(statKeys.map(k=>[k,0]));
    for(const h of state.history.filter(h=>h.day<7))for(const [k,v]of Object.entries(h.stat_change))scores[k]+=v;
    const first=k=>{const i=state.history.findIndex(h=>h.primary===k);return i<0?99:i;};
    return statKeys.slice().sort((a,b)=>scores[b]-scores[a]||first(a)-first(b)||statKeys.indexOf(a)-statKeys.indexOf(b))[0];
  }
  function finish(state){
    if(!state.finished||state.history.length!==7)throw Error('必须完成七次选择');
    const f=state.flags,has=x=>f.includes(x),role=state.role,dom=dominant(state), arcs=arcsFor(state);
    const crimes=f.filter(k=>data.flags[k]?.isCrime),violent=f.filter(k=>data.flags[k]?.isViolent);
    let id=role+'_'+dom,kind='normal',reason='前六日主要行动倾向与最终身份相结合。';
    if(arcs.length){id='arc_'+arcs[0].arc_id;kind='growth';reason='早期与后期行动发生可核对的转变。';}
    const harmfulArc=arcs.find(a=>['hero_to_tyrant','merciful_to_cruel'].includes(a.arc_id));
    if(crimes.length){const redemption=arcs.find(a=>a.arc_id==='cruel_to_redeemed');id=harmfulArc?'arc_'+harmfulArc.arc_id:redemption?'arc_'+redemption.arc_id:role==='tyrant'?role+'_'+dom:'blood_'+role;kind='contradictory';reason='重大伤害永久保留，不被终局功绩抵消。';}
    if(!crimes.length){
      let special=null;
      if(role==='hero'&&has('refused_holy_sword')&&!has('took_holy_sword'))special='swordless';
      if(role==='guardian'&&has('erased_hero_credit')&&state.history.filter(h=>h.primary==='Sacrifice').length>=3)special='forgotten';
      if(role==='hero'&&!has('took_holy_sword')&&!violent.length&&has('deescalated_square')&&has('cancelled_hunt'))special='never_drew';
      if(role==='hero'&&has('took_holy_sword')&&state.history.filter(h=>h.day<7&&h.primary==='Faith').length>=3)special='gods_blade';
      if(role==='failed'&&dom==='Reason')special='clear_mad';
      if(role==='ordinary'&&has('refused_summons')&&has('refused_all_titles'))special='last_ordinary';
      if(role==='vessel'&&has('absorbed_abyss')&&any(['power_kill_switch','accepted_restraint','broke_corruption'],f))special='ash_restrained';
      if(special){id='special_'+special;kind=special==='clear_mad'?'bad':'secret';reason='满足经过审核的特殊行为组合。';}
      if(role==='savior'&&state.meta.completedRuns>=1&&['lattice_validated','shared_load','collective_final'].every(has)&&['truth_abyss_function','truth_dragon_network','truth_common_people_cost'].every(t=>state.truths.includes(t))&&!any(['forced_load','forced_volunteers','forced_volunteers','enslaved_core'],f)) {id='special_cycle_ended';kind='true';reason='试验、知情同意、共同执行与已走过一次七日的经历共同完成，结束单一容器制度。';}
    }
    const rule=data.endings.find(e=>e.ending_id===id);if(!rule)throw Error('未定义称号 '+id);
    const evidence=state.history.map(h=>({day:h.day,text:h.text,consequence:h.consequence}));
    const status={dragon:has('killed_dragon')?'dead':'alive',previousHero:has('released_previous_hero')?'dead':(role==='vessel'||kind==='true'?'released':'supported'),player:role==='martyr'?'dead':role==='failed'?'lost':role==='vessel'?'bound':'alive'};
    return {endingId:id,title:rule.title,summary:arcs.length?'你的道路出现了转向：'+arcs[0].title+'；七日的旧事仍一并保留。':'从“'+state.history[0].text+'”开始，你最终选择了“'+state.history[6].text+'”',role,kind,dominant:dom,arcs:arcs.map(a=>a.arc_id),crimes,violent,evidence,status,reason,metNPCs:[...state.metNPCs],relations:clone(state.relations),epilogue:epilogue(state,id,kind,status,crimes),badges:{zeroDirectKill:violent.length===0,allNamedAlive:status.dragon!=='dead'&&status.previousHero!=='dead'&&status.player!=='dead'&&status.player!=='lost',swordless:!has('took_holy_sword'),independent:!any(['obeyed_kingdom','obeyed_church','accepted_crown','accepted_crosier','forced_volunteers'],f)}};
  }
  function epilogue(state,id,kind,status,crimes){
    const packetMap={'special_cycle_ended':16,'special_swordless':17,'special_forgotten':18,'special_never_drew':19,'special_gods_blade':20,'arc_coward_to_brave':21,'arc_coward_to_martyr':22,'arc_cruel_to_redeemed':23};
    let p=clone(data.packets[packetMap[id]??roleOrder.indexOf(state.role)]);
    // Each role packet describes only its shared consequence; append this run's concrete action.
    p.main+='\n\n'+state.history[6].consequence;
    const npc=[],met=id=>state.metNPCs.includes('npc_'+String(id).padStart(2,'0')),has=f=>state.flags.includes(f);
    const notes={
      1:has('accepted_crown')?'莱娅把维修预算留在议事桌上；印玺易手不取消旧令的复核。':'莱娅继续清点撤离名单，仍要为王庭签过的命令作答。',
      2:has('submitted_maren')||has('took_maren_post')?'玛伦进入共同审判程序。护送记录与烧毁哨站的记录分别保存。':'玛伦的护送仍被记下，她承认过的旧罪也没有撤档。',
      3:state.role==='pontiff'?'瑟文退到信徒席，留下可被质询的旧祷词原件。':'瑟文仍需回答删改与选拔的问题，祝福没有成为免于追责的凭证。',
      4:state.relations.Companions<0?'伊芙继续救治，拒绝替你的全部决定出具谅解。':'伊芙把救治簿与追责材料分开保存，缺药的条目仍未划掉。',
      5:has('killed_demon_child')?'妮娅保留少年被处决的证词，未让后来的救援替那一页结案。':'妮娅保管自己的证词，下一次是否公开坐标仍由她回答。',
      6:has('saved_officer')?'萨德带着未能治愈的伤继续整理维修方法；残损的手没有被称号治好。':'萨德留下修补方法，也保留对自己炸桥行为的供述。',
      7:has('exposed_var')?'瓦尔必须回应扣押粮车的证据，仍试图保住谈判席位。':'瓦尔没有因你的结局自动交权，军方与平民的利益仍需分别谈判。',
      8:status.dragon==='dead'?'阿瑟兰已经死去。遗誓使接手联络，照护与赔偿不会撤去死亡记录。':has('shared_dragon_care')?'阿瑟兰把照护权交给共同名单，仍逐项追问孩子的安全。':'阿瑟兰继续保护幼龙；与你合作过，也不等于接受你的每一道命令。',
      9:has('open_lattice')||kind==='true'?'缇尔将图纸交给各地维修者，误差与失败记录一同开放。':'缇尔保存本轮测量，尚未验证的部分仍留白。',
      10:has('forced_volunteers')?'托马保留强征名单，不让它在纪念册里改称志愿。':'托马收起村里的工具，按留下的人手重新安排轮值。',
      11:'奥伦的救济账与情报款仍可分别查验，他不能只拿出其中一本。',
      12:has('killed_innocent')?'维克将处决列入新政权的记录，印坊并没有因此获得清白。':'维克仍要交代印坊与工程中的决定，工具由谁保管仍是公开的问题。',
      13:status.previousHero==='dead'?'艾德里安在请求获确认、缓冲落实后停止承压，平静死去。':status.previousHero==='released'?'艾德里安离开承压椅，照护者把药和水移到普通病床边。':'艾德里安仍由留守队支撑；本局的局部救援没有自动结束他的职责。',
      14:state.role==='godslayer'?'曙母的强制分配核心停机，存档没有据此宣称已证明或否定神性。':kind==='true'?'曙母不再握有独占的活体征用接口；未知回应仍留作未解记录。':'曙母的权限变动保留在维修记录中，关于其神性的争论仍未结束。'
    };
    for(let i=1;i<=14;i++)if(met(i))npc.push(notes[i]);
    p.npc=npc.length?npc.join('\n\n'):'本局没有可追述的具名相遇。留下的人各自继续生活。';
    p.npcIds=[...state.metNPCs];
    const start=state.history[0],pivot=state.history.find(h=>h.day>=3&&h.day<=6&&h.primary!==start.primary);
    p.self+='\n\n第一日，你选择了“'+start.text+'”'+(pivot?'第'+pivot.day+'日，又选择了“'+pivot.text+'”':'')+'这些动作保留在下面的七日记录中。';
    if(crimes.length){p.world+=' 尚未清偿的重大伤害仍须追责。';p.self+=' 记录保留了这些行为：'+crimes.map(k=>data.flags[k].description).join('；')+'。';p.last='幸存者可以感谢你，受害者不必因此原谅你。';}
    if(kind==='true')p.world=data.packets[16].world;
    return p;
  }
  function view(state){
    const n=node(state);if(!n)return null;let scene=n.scene;
    const last=state.history.at(-1);
    const dead=state.flags.includes('killed_dragon');
    const livingText=t=>dead?t.replaceAll('阿瑟兰','遗誓使').replaceAll('古龙','龙族代表'):t;
    if(dead&&n.node_id!=='d7_w_guard_dragon_debt')scene=livingText(scene);
    for(const encounter of state.encounterLog.filter(x=>x.day===state.day)){
      const c=data.characters.find(c=>c.character_id===encounter.id),short=c.name.split('·')[0];
      if(scene.includes(short)&&!scene.includes(c.introduction))scene=scene.replace(short,c.introduction);
    }
    const memory=state.meta.completedRuns>0&&state.day===4?'门轴轻响了两下。你在声音停下之前，抬头看了一眼。':null;
    const reaction=last?.flags.map(f=>data.reactions[f]).find(r=>r&&state.metNPCs.includes(r[0]));
    return {day:n.day,title:n.title,location:n.location,scene,echo:last?.consequence||null,memory,reaction:reaction?.[1]||null,choices:n.choices.map(id=>{const c=resolveChoice(state,id);return {id,text:livingText(c.text)};})};
  }
  function replay(choiceIds,meta={}){if(!Array.isArray(choiceIds)||choiceIds.length>7||choiceIds.some(x=>typeof x!=='string'))throw Error('存档选择列表无效');return choiceIds.reduce((s,id)=>apply(s,id),initial(meta));}
  function exportSave(state){return {schemaVersion:2,meta:state.meta,choiceIds:state.history.map(h=>h.choiceId)};}
  function importSave(raw){if(!raw||raw.schemaVersion!==2)throw Error('此为其他版本存档；V0.1 存档请用项目 archive 中的旧版打开，新版不会改写旧存档');return replay(raw.choiceIds,raw.meta||{});}
  return {initial,apply,node,view,finish,replay,exportSave,importSave,arcsFor,dominant,resolveChoice,permitted};
}
if(typeof module!=='undefined'&&module.exports)module.exports={createEngine};else root.SeventhDay={createEngine};
})(globalThis);
