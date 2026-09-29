const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const html=fs.readFileSync(path.resolve(__dirname,'../dist/SeventhDay.html'),'utf8');
const scripts=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(x=>x[1]);
const stored=new Map([['seventh-day-v2',JSON.stringify({schemaVersion:2,saveVersion:3,completedRuns:0,collection:{},run:null,runId:null,countedRuns:[],journeys:[],onboardingSeen:false,audioSettings:{enabled:true,volume:.34}})]]);
const handlers={},elements={};let screen='';const audioButton={textContent:'',attributes:{},setAttribute(k,v){this.attributes[k]=v;if(k==='title')this.title=v;},removeAttribute(k){delete this.attributes[k];if(k==='title')delete this.title;}};
function element(tag){return {tag,innerHTML:'',className:'',setAttribute(){},focus(){},remove(){},append(){},click(){},querySelector(){return {focus(){}}}};}
const app={set innerHTML(v){screen=v;const button=v.match(/<button data-action="audio"([^>]*)>([^<]+)<\/button>/);audioButton.textContent=button?.[2]||'';audioButton.removeAttribute('title');const title=button?.[1].match(/ title="([^"]*)"/);if(title)audioButton.setAttribute('title',title[1]);},get innerHTML(){return screen;},addEventListener(k,fn){handlers[k]=fn;}};
const doc={title:'',hidden:false,querySelector(sel){if(sel==='#app')return app;if(sel==='main h1')return {focus(){}};if(sel==='[data-action=audio]')return audioButton;return elements[sel]||null;},createElement:element,body:{append(){}},addEventListener(k,fn){handlers['document:'+k]=fn;}};
class FakeAudio{static all=[];static attempts=0;constructor(src){this.src=src;this.paused=true;this.volume=0;FakeAudio.all.push(this);}play(){FakeAudio.attempts++;if(FakeAudio.attempts===1){this.paused=true;const error=new Error('User gesture required');error.name='NotAllowedError';return Promise.reject(error);}this.paused=false;return Promise.resolve();}pause(){this.paused=true;}}
const warnings=[];const runtime={document:doc,window:{scrollTo(){}},localStorage:{getItem:k=>stored.get(k)||null,setItem:(k,v)=>stored.set(k,v)},Audio:FakeAudio,setInterval(){return 1;},clearInterval(){},setTimeout(){},Blob,URL,crypto:{randomUUID:()=>String(Math.random())},Date,Math,console:{warn:(...args)=>warnings.push(args),log:console.log}};
const context=vm.createContext(runtime);scripts.forEach(s=>vm.runInContext(s,context));
const click=action=>handlers.click({target:{closest(sel){if(sel==='[data-action]')return {dataset:{action}};if(sel==='[data-action=audio]'&&action==='audio')return {dataset:{action}};return null;}}});
const settings=()=>JSON.parse(stored.get('seventh-day-v2')).audioSettings;
const settle=async()=>{for(let i=0;i<6;i++)await Promise.resolve();};
(async()=>{
 assert.equal(FakeAudio.all.length,0,'load must not instantiate audio');
 assert.ok(screen.includes('音乐：待播放'));
 click('new');await settle();
 assert.equal(FakeAudio.attempts,1);assert.equal(settings().enabled,true,'rejected play must preserve preference');assert.equal(audioButton.textContent,'音乐：重试');assert.ok(audioButton.title.includes('NotAllowedError'));assert.equal(warnings.at(-1)[1].message,'User gesture required');
 click('audio');await settle();
 assert.equal(settings().enabled,true,'retry must not turn preference off');assert.equal(FakeAudio.attempts,2,'audio button retries failed play');assert.equal(audioButton.textContent,'音乐：开');assert.ok(!audioButton.title,'successful play clears old diagnostic');assert.ok(FakeAudio.all.some(a=>!a.paused));
 handlers.input({target:{dataset:{volume:''},value:'55'}});assert.equal(settings().volume,.55);
 click('audio');assert.equal(settings().enabled,false);assert.equal(audioButton.textContent,'音乐：关');assert.ok(FakeAudio.all.every(a=>a.paused),'off stops all crossfade tracks');
 click('audio');assert.equal(settings().enabled,true);assert.ok(FakeAudio.attempts>=3);
 const volumeReload=vm.createContext(runtime);scripts.forEach(s=>vm.runInContext(s,volumeReload));
 assert.equal(settings().volume,.55);assert.ok(screen.includes('value="55"'),'volume survives reload');
 // New profile defaults to enabled but creates no audio until the first gesture.
 stored.clear();FakeAudio.all=[];FakeAudio.attempts=1;
 const fresh=vm.createContext(runtime);scripts.forEach(s=>vm.runInContext(s,fresh));
 assert.equal(FakeAudio.all.length,0);assert.ok(screen.includes('音乐：待播放'));
 click('audio');await settle();assert.equal(FakeAudio.attempts,2,'pending-state button starts BGM');assert.equal(audioButton.textContent,'音乐：开');
 click('new');assert.equal(settings().enabled,true);
 click('audio');assert.equal(settings().enabled,false);const stopped=FakeAudio.attempts;
 click('home');click('new');assert.equal(FakeAudio.attempts,stopped,'explicit off survives navigation');
 const disabledReload=vm.createContext(runtime);scripts.forEach(s=>vm.runInContext(s,disabledReload));
 assert.ok(screen.includes('音乐：关'));click('continue');assert.equal(FakeAudio.attempts,stopped,'explicit off survives reload');
 // Actual UI gesture chain: pointerdown -> click -> render, then change scene
 // while the first play Promise has not settled.
 stored.clear();
 class PendingAudio{static all=[];constructor(){this.paused=true;this.volume=0;this.pauses=0;this.plays=0;PendingAudio.all.push(this);}play(){this.plays++;return new Promise(resolve=>{this.resolve=()=>{this.paused=false;resolve();};});}pause(){this.pauses++;this.paused=true;}}
 const pendingContext=vm.createContext({...runtime,Audio:PendingAudio});scripts.forEach(s=>vm.runInContext(s,pendingContext));
 handlers['document:pointerdown']({target:{closest(){return null;}}});click('new');click('home');
 assert.equal(PendingAudio.all.length,1,'pointerdown/click/render use one pending track');assert.equal(PendingAudio.all[0].plays,1);
 click('continue');click('begin');assert.equal(PendingAudio.all.length,2);assert.equal(PendingAudio.all[0].pauses,0,'scene switch defers pause until play resolves');
 PendingAudio.all[0].resolve();await settle();assert.equal(PendingAudio.all[0].pauses,1);
 PendingAudio.all[1].resolve();await settle();assert.equal(audioButton.textContent,'音乐：开');
 assert.ok(!warnings.some(x=>x[1]?.name==='AbortError'));
 fs.writeFileSync(path.resolve(__dirname,'autoplay-report-v03.json'),JSON.stringify({passed:true,checks:['no audio created on load','rejected play retains enabled preference, error name and message','failed-state button retries without toggling off','pending-state button starts BGM','successful play updates button to on','playing-state button turns off','off-state button enables and plays','volume survives reload','toggle off stops all tracks','explicit off survives navigation and reload','pointerdown/click/render share one pending play','scene change defers pause until first play settles']},null,2));
 console.log('Autoplay regression passed');
})().catch(e=>{console.error(e);process.exitCode=1;});
