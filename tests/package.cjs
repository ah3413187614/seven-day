// Verify the actual shipped HTML, rather than only the loose source files.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const root=path.resolve(__dirname,'..'),html=fs.readFileSync(path.join(root,'dist/SeventhDay.html'),'utf8');
const scripts=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]);assert.equal(scripts.length,3);scripts.forEach((s,i)=>new vm.Script(s,{filename:'embedded-'+i+'.js'}));
assert.equal(scripts[1],fs.readFileSync(path.join(root,'src/engine.js'),'utf8'));assert.equal(scripts[2],fs.readFileSync(path.join(root,'src/ui.js'),'utf8'));
const context=vm.createContext({});vm.runInContext(scripts[0],context);vm.runInContext(scripts[1],context);assert.equal(Object.keys(context.GAME_DATA.story.nodes).length,89);
assert.deepEqual(JSON.parse(JSON.stringify(context.GAME_DATA)),JSON.parse(fs.readFileSync(path.join(root,'data/bundle.json'),'utf8')));
const engine=context.SeventhDay.createEngine(context.GAME_DATA);let s=engine.initial();for(let i=0;i<7;i++)s=engine.apply(s,engine.node(s).choices[i%4]);assert.ok(engine.finish(s).title);
assert.ok(!/<script[^>]+src=/.test(html));assert.ok(!/<link[^>]+href=/.test(html));
// DOM-shell smoke test: verify all screens can render, choices advance, reload and collection work.
// This deliberately does not pretend to verify CSS layout or real browser accessibility.
const stored=new Map(),handlers={},elements={};let currentHTML='';
function element(tag){return {tag,innerHTML:'',className:'',setAttribute(){},focus(){},remove(){if(tag==='div')delete elements['#next-day'];},append(){},click(){this.onclick?.();},querySelector(sel){if(sel==='button'){const b=elements['#next-day']||{focus(){},onclick:null};elements['#next-day']=b;return b;}return null;}};}
const shell={set innerHTML(v){currentHTML=v;},get innerHTML(){return currentHTML;},addEventListener(k,v){handlers[k]=v;}};
const document={title:'',querySelector(sel){if(sel==='#app')return shell;if(sel==='main h1')return {focus(){}};return elements[sel]||null;},createElement:element,body:{append(){}},addEventListener(){}};
const runtime={document,console,window:{scrollTo(){}},localStorage:{getItem:k=>stored.get(k)||null,setItem:(k,v)=>stored.set(k,v)},setTimeout(){},Blob,URL,crypto:{randomUUID:()=>Math.random().toString(36)},Date,Math};
const uiContext=vm.createContext(runtime);scripts.forEach(s=>vm.runInContext(s,uiContext));
assert.ok(currentHTML.includes('翻开命运之书'));
const clickAction=name=>handlers.click({target:{closest(sel){return sel==='[data-action]'?{dataset:{action:name}}:null;}}});
const clickChoice=id=>handlers.click({target:{closest(sel){return sel==='[data-choice]'?{dataset:{choice:id}}:null;}}});
clickAction('new');assert.ok(currentHTML.includes('第七声钟响之前'));
for(let i=0;i<7;i++){
 const choices=[...currentHTML.matchAll(/data-choice="([^"]+)"/g)].map(m=>m[1]);assert.equal(choices.length,4);
 clickChoice(choices[i%4]);elements['#next-day'].onclick();
}
assert.ok(currentHTML.includes('七日终章'));const profile=JSON.parse(stored.get('seventh-day-v2'));assert.equal(profile.completedRuns,1);assert.equal(Object.keys(profile.collection).length,1);
clickAction('collection');assert.ok(currentHTML.includes('已发现 1 /'));
clickAction('home');clickAction('continue');assert.ok(currentHTML.includes('七日终章'));assert.equal(JSON.parse(stored.get('seventh-day-v2')).completedRuns,1);
fs.writeFileSync(path.join(root,'tests/package-report.json'),JSON.stringify({passed:true,checks:['实际HTML的三个脚本语法','内嵌数据可读取','内嵌引擎七日可运行','无远程脚本与字体依赖','模拟DOM呈现标题/每日/终局/图鉴','模拟DOM七日操作与保存','继续本局不重复计次'],notCovered:['真实浏览器布局','CSS溢出','系统文件下载','读屏和焦点实际行为']},null,2));
console.log('Shipped HTML / engine / DOM-shell checks passed');
