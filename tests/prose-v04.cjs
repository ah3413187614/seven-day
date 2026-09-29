const assert=require('node:assert/strict');
const D=require('../data/bundle.json');
const E=require('../src/engine.js').createEngine(D);
const P=require('../src/prose.js');
const matches={};
const requested=new Set(Object.values(D.proseVariants).flatMap(r=>r.flatMap(x=>x.incomingChoiceIds||[])));
let truthYes=null,truthNo=null;
const seenNodes=new Set();let renderedStates=0;
function visit(state){
 if(state.finished)return;
 const base=E.view(state).scene,rendered=P.scene(D,state,base);
 assert.ok(rendered.endsWith(base)&&!rendered.includes('undefined'));
 assert.ok(!rendered.includes('魔族孩子魔族信使'));
 seenNodes.add(state.nodeId);renderedStates++;
 if(state.nodeId==='d7_w_ledger'){
  if(state.truths.includes('truth_dragon_network'))truthYes??=state;
  else truthNo??=state;
 }
 if(state.day===7)return;
 for(const id of E.node(state).choices){
  const next=E.apply(state,id);
  if(requested.has(id))matches[id]=next;
  visit(next);
 }
}
visit(E.initial());
for(const [node,rules] of Object.entries(D.proseVariants))for(const rule of rules){
 if(!rule.incomingChoiceIds)continue;
 for(const id of rule.incomingChoiceIds){
  const state=matches[id];assert.ok(state,`unreachable variant ${id}`);assert.equal(state.nodeId,node);
  const base=E.view(state).scene;
  const rendered=P.scene(D,state,base);
  assert.ok(rendered.startsWith(rule.text+'\n\n'));
  assert.ok(rendered.endsWith(base));
 }
}
for(const node of ['d4_c_oath','d4_c_guard','d5_h_guard','d6_v_oath']){
 const [one,two]=D.proseVariants[node];
 assert.notEqual(P.scene(D,matches[one.incomingChoiceIds[0]],'共同正文'),P.scene(D,matches[two.incomingChoiceIds[0]],'共同正文'));
}
assert.ok(truthYes&&truthNo,'truth fragment variants have both witnesses');
assert.ok(P.scene(D,truthYes,'共同正文').includes('龙骨支路'));
assert.ok(!P.scene(D,truthNo,'共同正文').includes('龙骨支路'));
const sample=matches['d3_v_ledger_3'];const generic={...sample,nodeId:'d4_h_guard'};
assert.ok(P.scene(D,generic,'共同正文').includes('次日，你从边境抵达教会。'));
assert.equal(P.scene(D,E.initial(),'第一日正文'),'第一日正文');
assert.equal(seenNodes.size,89);
console.log(JSON.stringify({reachableIncomingVariants:Object.keys(matches).length,truthYes:!!truthYes,truthNo:!!truthNo,comparedNodes:4,renderedStates,seenNodes:seenNodes.size}));
