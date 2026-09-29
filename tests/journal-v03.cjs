const assert=require('assert/strict'),fs=require('fs');
const D=require('../data/bundle.json'),E=require('../src/engine.js').createEngine(D),J=require('../src/journal.js');
const p=J.normalize({schemaVersion:2,completedRuns:1,collection:{old:{title:'旧称号'}},countedRuns:['old'],run:E.exportSave(E.initial()),runId:'active'});
assert.equal(p.saveVersion,3);assert.ok(p.collection.old);assert.equal(J.recall(p,'old'),null);
let s=E.initial();for(let i=0;i<7;i++)s=E.apply(s,E.node(s).choices[i%4]);const ending=E.finish(s),before=JSON.stringify(p.run);
J.record(p,s,ending,'one');J.record(p,s,ending,'one');assert.equal(p.journeys.length,1);
const snap=J.recall(p,'one');assert.deepEqual(snap.snapshot,ending);snap.snapshot.title='mutated';assert.equal(J.recall(p,'one').snapshot.title,ending.title);assert.equal(JSON.stringify(p.run),before);
for(let i=0;i<50;i++)J.record(p,s,ending,'run-'+i);
assert.equal(p.journeys.length,40);assert.ok(J.recall(p,ending.endingId));assert.equal(JSON.stringify(p.run),before);
assert.equal(D.characters.length,14);assert.ok(D.characters.every(c=>c.firstMeetingLabel&&c.firstMeetingLabel.length<25));
for(const ids of Object.values(require('./witnesses.json'))){const st=E.replay(ids.choiceIds,{completedRuns:ids.completedRuns});assert.ok(st.finished);}
fs.writeFileSync('tests/journal-report-v03.json',JSON.stringify({passed:true,checks:['旧版记录保留','档案幂等','40局上限','图鉴独立保留完整记录','回看副本不可改写档案','当前存档隔离','14人物短身份标签','全部结局见证仍可回放']},null,2));
console.log('V0.3 journal tests passed');
