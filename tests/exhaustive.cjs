const fs=require('fs'),path=require('path'),assert=require('assert/strict');
const root=path.resolve(__dirname,'..'),data=JSON.parse(fs.readFileSync(path.join(root,'data/bundle.json'),'utf8'));
const E=require('../src/engine.js').createEngine(data);
const report={version:1,nodes:Object.keys(data.story.nodes).length,choices:Object.keys(data.choices).length,candidateTitles:data.endings.length,arcs:data.arcs.length,runs:{},assertions:[],limitations:[]};
assert.equal(new Set(data.endings.map(e=>e.title)).size,data.endings.length,'Duplicate titles');
for(const n of Object.values(data.story.nodes)){
 assert.equal(n.choices.length,4);assert.equal(new Set(n.choices).size,4);
 assert.ok(n.scene.length>=100&&n.scene.length<=400,`${n.node_id} scene ${n.scene.length}`);
 assert.equal(new Set(n.choices.map(id=>data.choices[id].text)).size,4);
 if(n.day<7){assert.equal(new Set(n.choices.map(id=>data.choices[id].next_node)).size,4,'same successor within menu');
 for(const id of n.choices){const c=data.choices[id];assert.equal(data.story.nodes[c.next_node].day,n.day+1);assert.ok(data.story.nodes[c.next_node].previous_requirement.any_previous_choice.includes(id));}}
}
const union=new Set(),witnesses={},nodeSeen=new Set(),choiceSeen=new Set(),arcSeen=new Set();
for(const completedRuns of [0,1]){
 const r={paths:0,titles:{},roles:{},arcEvidence:{},badges:{},deadDragonPaths:0,truePaths:0};
 function walk(state){
  if(state.finished){
   r.paths++;assert.equal(state.history.length,7);
   const ending=E.finish(state);union.add(ending.endingId);r.titles[ending.endingId]=(r.titles[ending.endingId]||0)+1;r.roles[ending.role]=(r.roles[ending.role]||0)+1;
   if(!witnesses[ending.endingId])witnesses[ending.endingId]={completedRuns,choiceIds:state.history.map(h=>h.choiceId),title:ending.title};
   for(const a of ending.arcs){arcSeen.add(a);r.arcEvidence[a]=(r.arcEvidence[a]||0)+1;}
   for(const [k,v]of Object.entries(ending.badges))if(v)r.badges[k]=(r.badges[k]||0)+1;
   if(ending.status.dragon==='dead'){r.deadDragonPaths++;assert.ok(ending.epilogue.npc.includes('阿瑟兰已经死去'));}
   if(ending.kind==='true'){r.truePaths++;assert.ok(completedRuns>0);assert.equal(ending.crimes.length,0);}
   if(ending.crimes.length)assert.ok(ending.endingId.startsWith('blood_')||['arc_hero_to_tyrant','arc_merciful_to_cruel','arc_cruel_to_redeemed'].includes(ending.endingId)||ending.role==='tyrant','crime washed');
   for(const v of Object.values(state.stats))assert.ok(Number.isFinite(v)&&v>=-21&&v<=35);
   return;
  }
  nodeSeen.add(state.nodeId);const view=E.view(state);assert.equal(view.choices.length,4);
  if(state.day<7)assert.equal(new Set(E.node(state).choices.map(id=>E.apply(state,id).nodeId)).size,4,'conditional routes collapsed');
  if(state.flags.includes('killed_dragon'))assert.ok(!view.scene.includes('阿瑟兰说'));
  for(const id of E.node(state).choices){choiceSeen.add(id);const before=JSON.stringify(state),next=E.apply(state,id);assert.equal(JSON.stringify(state),before,'input mutated');walk(next);}
 }
 walk(E.initial({completedRuns}));assert.equal(r.paths,4**7);report.runs[completedRuns?'replay':'first']=r;
}
report.reachableTitles=union.size;report.reachableNodes=nodeSeen.size;report.reachableChoices=choiceSeen.size;report.detectableArcs=arcSeen.size;
report.unreachableTitles=data.endings.filter(e=>!union.has(e.ending_id)).map(e=>({id:e.ending_id,title:e.title}));
report.undetectedArcs=data.arcs.filter(a=>!arcSeen.has(a.arc_id)).map(a=>a.arc_id);
report.unreachableNodes=Object.keys(data.story.nodes).filter(id=>!nodeSeen.has(id));
report.unreachableChoices=Object.keys(data.choices).filter(id=>!choiceSeen.has(id));
// Reject wrong-node selection, corrupted saves, unfinished endings, or double action.
assert.throws(()=>E.apply(E.initial(), 'd7_c_oath_1'));assert.throws(()=>E.finish(E.initial()));assert.throws(()=>E.importSave({schemaVersion:9,choiceIds:[]}));assert.throws(()=>E.importSave({schemaVersion:1,choiceIds:['not-a-choice']}));
for(const witness of Object.values(witnesses)){const state=E.replay(witness.choiceIds,{completedRuns:witness.completedRuns});assert.deepEqual(E.importSave(E.exportSave(state)),state);assert.throws(()=>E.apply(state,'d1_start_1'));}
report.assertions=['所有节点均为四选一','每次选择严格推进一天','同菜单四个选择去往四个不同处境','首周目和二周目各穷举 16384 条路线','重大罪责不能被普通人格称号覆盖','死亡状态不复活','非法选择/损坏存档/重复终局拒绝','事件回放存档与原状态相同','输入状态不可变、数值有界'];
report.limitations=['均匀路径频率不是人类玩家实际概率','非杀戮徽记仅表示没有直接致死动作，不代表全世界无人伤亡','全员存活仅指本版具名角色与玩家的已实现死亡状态','纯文本语义多样性仍需真人阅读与试玩评审'];
fs.writeFileSync(path.join(__dirname,'report.json'),JSON.stringify(report,null,2));fs.writeFileSync(path.join(__dirname,'witnesses.json'),JSON.stringify(witnesses,null,2));
console.log(JSON.stringify({pathsPerMode:16384,reachableTitles:union.size,unreachableNodes:report.unreachableNodes,unreachableChoices:report.unreachableChoices,detectableArcs:arcSeen.size,undetectedArcs:report.undetectedArcs,truePaths:report.runs.replay.truePaths},null,2));
assert.equal(report.unreachableNodes.length,0);assert.equal(report.unreachableChoices.length,0);assert.ok(union.size>=100,'fewer than 100 titles reachable');assert.ok(report.runs.replay.truePaths>0,'true ending unreachable');
