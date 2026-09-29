/* Deterministic game core. No DOM, randomness, network, or stored stat trust. */
(function(root){
'use strict';
function createEngine(data){
  const statKeys=Object.keys(data.stats), factionKeys=['Kingdom','Church','Demons','Companions','Dragons','People'];
  const clone=x=>JSON.parse(JSON.stringify(x));
  const roleOrder=Object.keys(data.roles);
  function initial(meta={}) {return {schemaVersion:1,nodeId:data.story.start,day:1,stats:Object.fromEntries(statKeys.map(k=>[k,0])),relations:Object.fromEntries(factionKeys.map(k=>[k,0])),flags:[],history:[],finished:false,role:null,meta:{completedRuns:Math.max(0,Math.min(100000,Number(meta.completedRuns)||0))}};}
  function node(state){ if(state.finished)return null;const n=data.story.nodes[state.nodeId];if(!n||n.day!==state.day)throw Error('剧情状态无效');return n; }
  function apply(state,choiceId){
    if(state.finished)throw Error('本局已经结束');
    const n=node(state), c=data.choices[choiceId];
    if(!n.choices.includes(choiceId)||!c)throw Error('不能选择当前节点之外的行动');
    const next=clone(state), before={stats:clone(state.stats),relations:clone(state.relations)};
    const d=c.DESIGNER_ONLY;
    for(const [k,v] of Object.entries(d.stat_change))next.stats[k]=Math.max(-21,Math.min(35,(next.stats[k]||0)+v));
    for(const [k,v] of Object.entries(d.relationship_change))next.relations[k]=Math.max(-20,Math.min(20,(next.relations[k]||0)+v));
    next.flags=[...new Set([...next.flags,...n.on_enter_flags,...d.add_flags])];
    next.history.push({day:state.day,nodeId:n.node_id,choiceId,primary:d.primary,text:c.text,consequence:c.consequence,flags:[...d.add_flags],before,after:{stats:clone(next.stats),relations:clone(next.relations)}});
    if(c.next_node){next.nodeId=c.next_node;for(const v of data.variants?.[c.next_node]||[]){const req=v.flags;if((!req.all||req.all.every(f=>next.flags.includes(f)))&&(!req.any||req.any.some(f=>next.flags.includes(f)))&&(!req.none||req.none.every(f=>!next.flags.includes(f)))){next.nodeId=v.nodeId;break;}}next.day++;if(!data.story.nodes[next.nodeId])throw Error('缺失后续节点');next.flags=[...new Set([...next.flags,...data.story.nodes[next.nodeId].on_enter_flags])];}
    else {if(state.day!==7||!c.terminal_role)throw Error('不能提前结局');next.finished=true;next.role=c.terminal_role;next.nodeId=null;}
    return next;
  }
  const any=(a,b)=>a.some(x=>b.includes(x));
  function arcsFor(state){
    const early=state.history.filter(h=>h.day<=3), late=state.history.filter(h=>h.day>=5);
    const earlyFlags=early.flatMap(h=>h.flags),lateFlags=late.flatMap(h=>h.flags);
    return data.arcs.filter(a=>a.roles.includes(state.role)&&early.filter(h=>h.primary===a.early).length>=a.early_min&&late.filter(h=>h.primary===a.late).length>=a.late_min&&(!a.early_flags_any.length||any(a.early_flags_any,earlyFlags))&&(!a.late_flags_any.length||any(a.late_flags_any,lateFlags))).sort((a,b)=>b.priority-a.priority||a.arc_id.localeCompare(b.arc_id));
  }
  function dominant(state){
    // Day 7 defines identity, never single-handedly rewrites the earlier personality.
    const scores=Object.fromEntries(statKeys.map(k=>[k,0]));
    for(const h of state.history.filter(h=>h.day<7))for(const [k,v]of Object.entries(data.choices[h.choiceId].DESIGNER_ONLY.stat_change))scores[k]+=v;
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
      if(role==='savior'&&state.meta.completedRuns>=1&&['lattice_validated','shared_load','collective_final'].every(has)&&!any(['forced_load','forced_volunteers','forced_volunteers','enslaved_core'],f)) {id='special_cycle_ended';kind='true';reason='试验、知情同意、共同执行与已解锁记忆共同完成，结束单一容器制度。';}
    }
    const rule=data.endings.find(e=>e.ending_id===id);if(!rule)throw Error('未定义称号 '+id);
    const evidence=state.history.map(h=>({day:h.day,text:h.text,consequence:h.consequence}));
    const status={dragon:has('killed_dragon')?'dead':'alive',previousHero:has('released_previous_hero')?'dead':(role==='vessel'||kind==='true'?'released':'supported'),player:role==='martyr'?'dead':role==='failed'?'lost':role==='vessel'?'bound':'alive'};
    return {endingId:id,title:rule.title,role,kind,dominant:dom,arcs:arcs.map(a=>a.arc_id),crimes,violent,evidence,status,reason,relations:clone(state.relations),epilogue:epilogue(state,id,kind,status,crimes),badges:{zeroDirectKill:violent.length===0,allNamedAlive:status.dragon!=='dead'&&status.previousHero!=='dead'&&status.player!=='dead'&&status.player!=='lost',swordless:!has('took_holy_sword'),independent:!any(['obeyed_kingdom','obeyed_church','accepted_crown','accepted_crosier','forced_volunteers'],f)}};
  }
  function epilogue(state,id,kind,status,crimes){
    const packetMap={'special_cycle_ended':16,'special_swordless':17,'special_forgotten':18,'special_never_drew':19,'special_gods_blade':20,'arc_coward_to_brave':21,'arc_coward_to_martyr':22,'arc_cruel_to_redeemed':23};
    let p=clone(data.packets[packetMap[id]??roleOrder.indexOf(state.role)]);
    // Featured examples are not automatically true for a random personality.
    if(!packetMap.hasOwnProperty(id)&&p.title!==data.endings.find(e=>e.ending_id===id)?.title){
      p.main=data.roles[state.role].world+' '+state.history[6].consequence;
      p.self=state.role==='martyr'?'你没有走出这次最后的守护。留下的人必须自己决定怎样记住你。':state.role==='failed'?'你失去了完整的自我；此前的行动仍然留下真实后果。':'你记得第一天的选择：“'+state.history[0].text+'”七天后，那个决定没有被后来的身份抹去。';
      p.world=data.roles[state.role].world;
    }
    const npc=[];
    if(status.dragon==='dead')npc.push('阿瑟兰已经死去。龙族遗誓使接替其联络职责；新的共同照护不会让这场死亡从记录里消失。');
    else if(state.relations.Dragons>=2)npc.push('龙族愿意继续谈判，但把照护责任与违约追责一起写进契约。');
    else npc.push('龙族仍保留自己的立场，没有因你的终局身份自动与你和解。');
    if(status.previousHero==='dead')npc.push('艾德里安按自己确认的意愿停止承压，平静死去；缓冲只保证这次冲击不会直接吞没撤离人群。');
    else if(status.previousHero==='released')npc.push('艾德里安获准休息；照护队接手他的余生，他不再被强迫继续承担容器职责。');
    else npc.push('艾德里安仍由留守队支撑；你的局部救援没有自动解决容器的长期困境。');
    npc.push(state.relations.Companions<0?'同伴保留对你的质询，救援功绩没有自动修复受损的信任。':'同行者各自回到需要他们的地方；他们仍有拒绝你下一次请求的权利。');
    p.npc=npc.join('\n\n');
    if(crimes.length){p.world+=' 尚未清偿的重大伤害仍须追责。';p.self+=' 记录保留了这些行为：'+crimes.map(k=>data.flags[k].description).join('；')+'。';p.last='幸存者可以感谢你，受害者不必因此原谅你。';}
    if(kind==='true')p.world=data.packets[16].world;
    return p;
  }
  function view(state){
    const n=node(state);if(!n)return null;let scene=n.scene;
    const last=state.history.at(-1);
    if(last)scene='昨日留下的后果：'+last.consequence+'\n\n'+scene;
    if(state.flags.includes('killed_dragon'))scene=scene.replaceAll('阿瑟兰','龙族遗誓使').replaceAll('古龙说','遗誓使转述古龙生前说过的话：').replaceAll('古龙','龙族代表');
    if(state.meta.completedRuns>0&&state.day===4)scene+='\n\n【回声】上一段旅程里未能听懂的仪表声，如今显出规律。记忆能提示你寻找验证，却不能替别人签下同意。';
    return {day:n.day,title:n.title,location:n.location,scene,choices:n.choices.map(id=>{const c=data.choices[id];return {id,text:state.flags.includes('killed_dragon')?c.text.replaceAll('古龙','龙族代表').replaceAll('阿瑟兰','龙族遗誓使'):c.text,cost:c.cost,gain:c.gain};})};
  }
  function replay(choiceIds,meta={}){if(!Array.isArray(choiceIds)||choiceIds.length>7||choiceIds.some(x=>typeof x!=='string'))throw Error('存档选择列表无效');return choiceIds.reduce((s,id)=>apply(s,id),initial(meta));}
  function exportSave(state){return {schemaVersion:1,meta:state.meta,choiceIds:state.history.map(h=>h.choiceId)};}
  function importSave(raw){if(!raw||raw.schemaVersion!==1)throw Error('不支持的存档版本');return replay(raw.choiceIds,raw.meta||{});}
  return {initial,apply,node,view,finish,replay,exportSave,importSave,arcsFor,dominant};
}
if(typeof module!=='undefined'&&module.exports)module.exports={createEngine};else root.SeventhDay={createEngine};
})(globalThis);
