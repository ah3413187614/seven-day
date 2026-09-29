// Verify the actual shipped HTML, rather than only the loose source files.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const root=path.resolve(__dirname,'..'),html=fs.readFileSync(path.join(root,'dist/SeventhDay.html'),'utf8');
const scripts=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]);assert.equal(scripts.length,6);scripts.forEach((s,i)=>new vm.Script(s,{filename:'embedded-'+i+'.js'}));
assert.equal(scripts[1],fs.readFileSync(path.join(root,'src/engine.js'),'utf8'));assert.equal(scripts[2],fs.readFileSync(path.join(root,'src/journal.js'),'utf8'));assert.equal(scripts[3],fs.readFileSync(path.join(root,'src/audio.js'),'utf8'));assert.equal(scripts[4],fs.readFileSync(path.join(root,'src/prose.js'),'utf8'));assert.equal(scripts[5],fs.readFileSync(path.join(root,'src/ui.js'),'utf8'));
const context=vm.createContext({});vm.runInContext(scripts[0],context);vm.runInContext(scripts[1],context);assert.match(context.GAME_BUILD_ID,/^v0\.4\.0\+[0-9a-f]{12}$/);assert.equal(Object.keys(context.GAME_DATA.story.nodes).length,89);assert.equal(Object.keys(context.GAME_ASSETS.endingPremium).length,8);assert.equal(Object.keys(context.GAME_ASSETS.scenes).length,7);assert.ok(Object.values(context.GAME_ASSETS.scenes).every(x=>x.startsWith('data:image/jpeg;base64,')));assert.equal(context.GAME_ASSETS.characters,undefined);assert.equal(Object.keys(context.GAME_AUDIO).length,8);assert.ok(Object.values(context.GAME_AUDIO).every(x=>x.startsWith('data:audio/ogg;base64,')));const premium=context.GAME_DATA.endings.filter(e=>e.artType==='premium');assert.equal(premium.length,8);assert.ok(context.GAME_DATA.endings.every(e=>(e.artType==='premium'?!!e.artKey:e.artType==='none'&&e.artKey===null)&&e.musicKey==='ending'));assert.ok(Object.values(context.GAME_DATA.story.nodes).every(n=>Array.isArray(n.characterIds)&&n.musicKey));
assert.deepEqual(JSON.parse(JSON.stringify(context.GAME_DATA)),JSON.parse(fs.readFileSync(path.join(root,'data/bundle.json'),'utf8')));
const engine=context.SeventhDay.createEngine(context.GAME_DATA);let s=engine.initial();for(let i=0;i<7;i++)s=engine.apply(s,engine.node(s).choices[i%4]);assert.ok(engine.finish(s).title);
assert.ok(!/<script[^>]+src=/.test(html));assert.ok(!/<link[^>]+href=/.test(html));
// DOM-shell smoke test: verify all screens can render, choices advance, reload and collection work.
// This deliberately does not pretend to verify CSS layout or real browser accessibility.
const stored=new Map(),handlers={},elements={};let currentHTML='',lastInput=null;
function element(tag){const el={tag,innerHTML:'',className:'',setAttribute(){},focus(){},remove(){if(tag==='div')delete elements['#next-day'];},append(){},click(){this.onclick?.();},querySelector(sel){if(sel==='button'){const b=elements['#next-day']||{focus(){},onclick:null};elements['#next-day']=b;return b;}return null;}};if(tag==='input')lastInput=el;return el;}
const shell={set innerHTML(v){currentHTML=v;},get innerHTML(){return currentHTML;},addEventListener(k,v){handlers[k]=v;}};
const document={title:'',querySelector(sel){if(sel==='#app')return shell;if(sel==='main h1')return {focus(){}};return elements[sel]||null;},createElement:element,body:{append(){}},addEventListener(){}};
class FakeAudio{constructor(){this.paused=true;this.volume=0;}play(){this.paused=false;return Promise.resolve();}pause(){this.paused=true;}}
const runtime={document,console,window:{scrollTo(){}},localStorage:{getItem:k=>stored.get(k)||null,setItem:(k,v)=>stored.set(k,v)},Audio:FakeAudio,setInterval(){return 1;},clearInterval(){},setTimeout(){},Blob,URL,crypto:{randomUUID:()=>Math.random().toString(36)},Date,Math};
const uiContext=vm.createContext(runtime);scripts.forEach(s=>vm.runInContext(s,uiContext));
assert.ok(currentHTML.includes('翻开命运之书'));assert.ok(currentHTML.includes('音乐：待播放'));assert.equal(stored.size,0);
// The first gesture unlocks only the user's chosen audio preference.

const clickAction=name=>handlers.click({target:{closest(sel){return sel==='[data-action]'?{dataset:{action:name}}:null;}}});
const clickChoice=id=>handlers.click({target:{closest(sel){return sel==='[data-choice]'?{dataset:{choice:id}}:null;}}});
clickAction('new');assert.ok(currentHTML.includes('召集令落在你家门上'));clickAction('home');const onbReload=vm.createContext(runtime);scripts.forEach(script=>vm.runInContext(script,onbReload));clickAction('continue');assert.ok(currentHTML.includes('召集令落在你家门上'),'continue must not skip onboarding');clickAction('begin');assert.ok(currentHTML.includes('第七声钟响之前'));assert.ok(currentHTML.includes('托马'));assert.ok(currentHTML.includes('class="scene-art"'));assert.ok(!currentHTML.includes('character-gallery')&&!currentHTML.includes('pixel-sprite'));
for(let i=0;i<7;i++){
 const choices=[...currentHTML.matchAll(/data-choice="([^"]+)"/g)].map(m=>m[1]);assert.equal(choices.length,4);
 assert.ok(!currentHTML.includes('将获得')&&!currentHTML.includes('将失去')&&!currentHTML.includes('stat_change')&&!currentHTML.includes('relationship_change'));
 clickChoice(choices[i%4]);elements['#next-day'].onclick();
}
assert.ok(currentHTML.includes('七日终章'));const profile=JSON.parse(stored.get('seventh-day-v2'));assert.equal(profile.completedRuns,1);const previous=profile.journeys[0];assert.equal(Object.keys(profile.collection).length,1);
const displayed=uiContext.GAME_DATA.endings.find(e=>e.ending_id===previous.endingId);if(displayed.artType==='premium')delete uiContext.GAME_ASSETS.endingPremium[displayed.artKey];clickAction('collection');assert.ok(currentHTML.includes('已发现 1 /'));assert.ok(!currentHTML.includes('art-awaiting')&&!currentHTML.includes('美术尚未制作'));assert.ok(currentHTML.includes('ending-emblem'));
clickAction('home');clickAction('continue');assert.ok(currentHTML.includes('七日终章'));assert.equal(JSON.parse(stored.get('seventh-day-v2')).completedRuns,1);
// Start another run, recall the first from both entry points, and prove storage isolation.

assert.equal(previous.choiceIds.length,7);assert.equal(previous.nodeIds.length,7);
clickAction('new');const secondChoice=[...currentHTML.matchAll(/data-choice="([^"]+)"/g)][1][1];clickChoice(secondChoice);elements['#next-day'].onclick();
const activeBefore=stored.get('seventh-day-v2');
const recallClick=(key,value)=>handlers.click({target:{closest(sel){return sel==='[data-ending], [data-run]'?{dataset:{[key]:value}}:null;}}});
clickAction('collection');assert.ok(currentHTML.includes('data-ending='));recallClick('ending',previous.endingId);
assert.ok(currentHTML.includes('历史回看'));assert.ok(currentHTML.includes(previous.endingTitle));assert.equal((currentHTML.match(/class="history-row"/g)||[]).length,7);
assert.equal(stored.get('seventh-day-v2'),activeBefore);
clickAction('journeys');assert.ok(currentHTML.includes('data-run='));recallClick('run',previous.runId);assert.equal(stored.get('seventh-day-v2'),activeBefore);
clickAction('continue');assert.ok(currentHTML.includes('DAY 2 / VII'));assert.equal(stored.get('seventh-day-v2'),activeBefore);
for(let day=2;day<=7;day++){const id=[...currentHTML.matchAll(/data-choice="([^"]+)"/g)][0][1];clickChoice(id);elements['#next-day'].onclick();}
const finalProfile=JSON.parse(stored.get('seventh-day-v2'));assert.equal(finalProfile.completedRuns,2);assert.equal(finalProfile.journeys.length,2);
assert.ok(finalProfile.journeys.every(j=>j.snapshot.epilogue.last&&j.snapshot.summary));
const afterTwo=stored.get('seventh-day-v2');const reloaded=vm.createContext(runtime);scripts.forEach(s=>vm.runInContext(s,reloaded));clickAction('journeys');assert.ok(currentHTML.includes(previous.endingTitle));recallClick('run',previous.runId);assert.equal(stored.get('seventh-day-v2'),afterTwo);
// Import the same Day 3 save twice and complete two distinct continuations.
const all=Object.values(JSON.parse(fs.readFileSync(path.join(root,'tests/witnesses.json'),'utf8')));
let pair;
for(const w of all){const match=all.find(v=>v!==w&&v.choiceIds.slice(0,2).join('|')===w.choiceIds.slice(0,2).join('|')&&v.title!==w.title);if(match){pair=[w,match];break;}}
assert.ok(pair,'two endings sharing a Day 3 prefix');
const partial=engine.replay(pair[0].choiceIds.slice(0,2),{completedRuns:1});
const file={size:300,text:async()=>JSON.stringify(engine.exportSave(partial))};
const importPartial=async()=>{clickAction('import');lastInput.files=[file];await lastInput.onchange();assert.ok(currentHTML.includes('DAY 3 / VII'));};
const complete=ids=>{for(const id of ids.slice(2)){clickChoice(id);elements['#next-day'].onclick();}assert.ok(currentHTML.includes('七日终章'));};
(async()=>{
 await importPartial();complete(pair[0].choiceIds);
 const beforeA=JSON.parse(stored.get('seventh-day-v2'));const runA=beforeA.journeys.at(-1);
 await importPartial();complete(pair[1].choiceIds);
 const afterB=JSON.parse(stored.get('seventh-day-v2'));const runB=afterB.journeys.at(-1);
 assert.notEqual(runA.runId,runB.runId,'each import creates a fresh run');
 assert.notEqual(runA.endingId,runB.endingId,'distinct continuations yield distinct endings');
 assert.ok(afterB.journeys.some(j=>j.runId===runA.runId));
 assert.equal(afterB.journeys.length,4);
 fs.writeFileSync(path.join(root,'tests/package-report.json'),JSON.stringify({passed:true,checks:['实际HTML的六个脚本语法及数据和素材嵌入','内嵌数据可读取','内嵌引擎七日可运行','无远程脚本与字体依赖','模拟DOM呈现标题/每日/终局/图鉴','模拟DOM七日操作与保存','继续本局不重复计次','开场可进入第一日','首周目与NG+完整七日','图鉴和档案均可回看完整结局','回看不改变第二局存档','两局各保存一次档案','8首离线BGM且无日常像素人物内嵌','Premium结局美术数据和无图安全回退','无日常像素角色；普通结局仅小纹章','缺失Premium Art时无开发占位','同一Day3存档重复导入生成两条独立旅程'],notCovered:['真实浏览器布局','CSS溢出','系统文件下载','读屏和焦点实际行为']},null,2));
console.log('Shipped HTML / engine / DOM-shell checks passed');
})().catch(e=>{console.error(e);process.exitCode=1;});
