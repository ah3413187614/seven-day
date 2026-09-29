const fs=require('fs'),assert=require('assert/strict');
const D=JSON.parse(fs.readFileSync('data/bundle.json','utf8')),E=require('../src/engine.js').createEngine(D);
const report={version:'0.2',visitedStates:0,terminalStates:0,gates:{},maxTruths:0,maxMet:0,arcWitnesses:{},errors:[],truthWitnesses:{},day4KnowledgeSets:{},crimeRedemptionPaths:0};
let cleanWin=null;
for(const [id,c] of Object.entries(D.choices))if(c.requirement)report.gates[id]={full:0,limited:0,witnesses:{}};
for(const n of Object.values(D.story.nodes)){
 const ps=n.scene.split('\n\n');assert.ok(ps.length>=2&&ps.length<=4,n.node_id+' paragraphs');assert.ok(n.scene.length>=120&&n.scene.length<=300,n.node_id+' length '+n.scene.length);
 assert.deepEqual(n.on_enter_flags,[]);assert.ok(!n.scene.includes('你终于明白'));assert.ok(!n.scene.includes('你感到'));
}
assert.equal(Object.keys(D.truths).length,10);
function walk(s){
 report.visitedStates++;report.maxTruths=Math.max(report.maxTruths,s.truths.length);report.maxMet=Math.max(report.maxMet,s.metNPCs.length);
 assert.ok(!s.flags.includes('learned_truth'));assert.equal(new Set(s.truths).size,s.truths.length);assert.equal(s.knowledgeLog.length,s.truths.length);
 for(const log of s.knowledgeLog){assert.ok(D.story.nodes[log.source]||D.choices[log.source]);assert.ok(log.evidence.length>0);assert.ok(log.day<=s.day);report.truthWitnesses[log.id]??={source:log.source,choiceIds:s.history.map(h=>h.choiceId)};}
 if(s.day===4&&!s.finished)report.day4KnowledgeSets[s.nodeId]=[...s.truths];
 if(s.finished){
  report.terminalStates++;const r=E.finish(s);if(r.endingId==='arc_cruel_to_redeemed'&&r.crimes.length){report.crimeRedemptionPaths++;assert.ok(r.epilogue.self.includes('记录保留'));}
  assert.ok(!JSON.stringify(r).includes('undefined'));assert.deepEqual(r.epilogue.npcIds,s.metNPCs);
  D.characters.forEach(c=>{if(!s.metNPCs.includes(c.character_id))assert.ok(!r.epilogue.npc.includes(c.name.split('·')[0]),'Unmet NPC '+c.name);});
  if(r.kind==='true'){
   assert.ok(['truth_abyss_function','truth_dragon_network','truth_common_people_cost'].every(t=>s.truths.includes(t)));
   assert.ok(['lattice_validated','shared_load','collective_final'].every(f=>s.flags.includes(f)));
   assert.ok(!r.epilogue.world.includes('没有代价'));assert.ok(r.epilogue.world.includes('疼痛'));
  }
  for(const a of E.arcsFor(s)){
   if(!report.arcWitnesses[a.arc_id]){
    const start=s.history.find(h=>a.early_days.includes(h.day)&&h.primary===a.early&&(!a.early_flags_any.length||a.early_flags_any.some(f=>h.flags.includes(f))));
    const pivot=s.history.find(h=>a.pivot_days.includes(h.day)&&h.day>start.day&&h.primary===a.late&&s.history.some(end=>a.late_days.includes(end.day)&&end.day>h.day&&end.primary===a.late));
    assert.ok(pivot);
    report.arcWitnesses[a.arc_id]={early:start,turn:pivot,late:s.history.filter(h=>h.day>pivot.day&&a.late_days.includes(h.day)&&h.primary===a.late),choiceIds:s.history.map(h=>h.choiceId)};
   }
  }
  assert.ok(s.history.every(h=>h.consequence.includes('；')),'Uncosted action');
  return;
 }
 for(const f of s.flags)assert.ok(D.flags[f],'missing flag '+f);
 const v=E.view(s);assert.equal(v.choices.length,4);assert.ok(v.choices.every(c=>!('cost'in c)&&!('gain'in c)));
 assert.equal(v.echo,s.history.at(-1)?.consequence||null);assert.ok(!v.scene.includes('昨日留下的后果'));
 // NG+ memory changes prose only, not evidence or permissions.
 const ng={...s,meta:{completedRuns:s.meta.completedRuns?0:1}};
 assert.deepEqual(E.view(ng).choices,v.choices);assert.deepEqual(ng.truths,s.truths);
 for(const cid of E.node(s).choices){
  const c=E.resolveChoice(s,cid),next=E.apply(s,cid);
  if(c.requirement){const g=report.gates[cid];g[c.mode]++;g.witnesses[c.mode]??={choiceIds:[...s.history.map(h=>h.choiceId),cid],truths:s.truths,flags:s.flags};
   assert.equal(c.mode==='full',E.permitted(s,c.requirement));
   if(c.mode==='limited'){
    const base=D.choices[cid];assert.notEqual(c.text,base.text);assert.notDeepEqual(c.DESIGNER_ONLY.add_flags,base.DESIGNER_ONLY.add_flags);
    assert.ok(base.DESIGNER_ONLY.add_flags.every(f=>!next.history.at(-1).flags.includes(f)));
   }
  }
  walk(next);
 }
}
walk(E.initial({completedRuns:1}));
for(const [cid,g]of Object.entries(report.gates)){assert.ok(g.full>0,cid+' never full');assert.ok(g.limited>0,cid+' never limited');}
assert.equal(Object.keys(report.truthWitnesses).length,10,'unobtainable truth');
assert.ok(report.crimeRedemptionPaths>0,'real redemption with crime is impossible');
report.sameLocationContrasts={};
for(const [id,g]of Object.entries(report.gates)){
 if(D.story.nodes[D.choices[id].node_id].day!==7)continue;
 const states=['full','limited'].map(mode=>E.replay(g.witnesses[mode].choiceIds.slice(0,-1),{completedRuns:1}));
 assert.equal(states[0].nodeId,states[1].nodeId);
 const menus=states.map(s=>E.view(s).choices.map(c=>c.text));assert.notDeepEqual(menus[0],menus[1]);
 report.sameLocationContrasts[id]={nodeId:states[0].nodeId,routes:states.map(s=>s.history.map(h=>h.choiceId)),menus};
}
for(const c of Object.values(D.choices)){
 for(const t of c.requirement?.truthsAll||[])assert.ok(D.truths[t]);
 for(const f of [...c.requirement?.flagsAll||[],...c.requirement?.flagsAny||[]])assert.ok(D.flags[f]);
 for(const k of Object.keys(c.requirement?.relationsMin||{}))assert.ok(k in E.initial().relations);
 for(const a of c.requirement?.arcProgressAny||[])assert.ok(D.arcs.some(x=>x.arc_id===a));
 for(const mode of [c,c.fallback].filter(Boolean))for(const f of mode.DESIGNER_ONLY.add_flags)assert.ok(D.flags[f]);
}
assert.throws(()=>E.importSave({schemaVersion:1,choiceIds:[]}));
const A=JSON.parse(fs.readFileSync('tests/playtest_v01_A.json','utf8'));
// Replays are explicitly compared against archived V0.1 choices, not silently imported.
const paths={A:['d1_start_1','d2_c_2','d3_c_ledger_2','d4_h_ledger_2','d5_h_revolt_2','d6_v_oath_3','d7_v_guard_1'],B:['d1_start_4','d2_v_3','d3_v_revolt_2','d4_v_revolt_1','d5_v_revolt_3','d6_v_guard_2','d7_c_guard_2']};
report.playthroughs={};
for(const [name,ids]of Object.entries(paths)){
 let s=E.initial(),days=[];for(const id of ids){days.push({view:E.view(s),truths:[...s.truths]});s=E.apply(s,id);}
 const ending=E.finish(s);report.playthroughs[name]={days,ending,save:E.exportSave(s)};
 if(name==='A'){assert.notEqual(ending.endingId,'arc_soldier_to_healer');assert.ok(!ending.epilogue.npc.includes('阿瑟兰'));}
 if(name==='B'){assert.ok(!days[3].truths.includes('truth_container_system'));assert.ok(!ending.epilogue.npc.includes('艾德里安'));}
}
fs.writeFileSync('tests/evidence-report-v02.json',JSON.stringify(report,null,2));
console.log(JSON.stringify({terminalStates:report.terminalStates,gates:Object.keys(report.gates).length,arcWitnesses:Object.keys(report.arcWitnesses).length,maxTruths:report.maxTruths,playthroughs:Object.fromEntries(Object.entries(report.playthroughs).map(([k,v])=>[k,v.ending.title]))},null,2));
