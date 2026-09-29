const fs=require('fs'),path=require('path'),assert=require('assert/strict');
const data=JSON.parse(fs.readFileSync(path.resolve(__dirname,'../data/bundle.json'),'utf8'));
const E=require('../src/engine.js').createEngine(data);const count=Number(process.argv[2]||100000);let seed=Number(process.argv[3]||20260928)>>>0;
assert.ok(Number.isInteger(count)&&count>0&&count<=1000000);
const random=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296;};
const stats={runs:count,initialSeed:seed,endingFrequency:{},nodeFrequency:{},choiceFrequency:{}};
for(let i=0;i<count;i++){
 let state=E.initial({completedRuns:i%2});
 for(let day=1;day<=7;day++){
  const n=E.node(state);stats.nodeFrequency[n.node_id]=(stats.nodeFrequency[n.node_id]||0)+1;
  const cid=n.choices[Math.floor(random()*4)];stats.choiceFrequency[cid]=(stats.choiceFrequency[cid]||0)+1;state=E.apply(state,cid);
 }
 const r=E.finish(state);stats.endingFrequency[r.endingId]=(stats.endingFrequency[r.endingId]||0)+1;
}
fs.writeFileSync(path.resolve(__dirname,'random-report.json'),JSON.stringify(stats,null,2));
console.log(JSON.stringify({runs:count,seed:stats.initialSeed,titles:Object.keys(stats.endingFrequency).length,nodes:Object.keys(stats.nodeFrequency).length,choices:Object.keys(stats.choiceFrequency).length}));
