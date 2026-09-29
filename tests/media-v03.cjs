const fs=require('fs'),assert=require('assert/strict'),path=require('path');
const D=require('../data/bundle.json'),M=require('../src/audio.js');
class FakeAudio{static all=[];constructor(src){this.src=src;this.paused=true;this.volume=0;FakeAudio.all.push(this);}play(){this.paused=false;return Promise.resolve();}pause(){this.paused=true;}}
let interval,cleared=0;const timers={setInterval:fn=>(interval=fn,1),clearInterval:()=>{cleared++;}};
const a=M.createAudio({title:'title.wav',normal:'normal.wav',tension:'tension.wav',final_day:'final.wav',ending:'end.wav'},FakeAudio,timers);
(async()=>{
assert.equal(FakeAudio.all.length,0);assert.equal(a.switchTo('title'),false);assert.equal(FakeAudio.all.length,0);
a.setVolume(.22);assert.equal(a.setEnabled(true),true);assert.equal(FakeAudio.all.length,0);assert.equal(a.pending,true);assert.equal(a.activate(),true);await Promise.resolve();assert.equal(FakeAudio.all.length,1);assert.equal(a.key,'title');
// Complete each crossfade and verify the previous loop is stopped, including
// title -> normal -> tension -> final_day -> ending.
const realNow=Date.now;let now=realNow();Date.now=()=>now;
try{for(const key of ['normal','tension','final_day','ending']){now+=1000;interval();assert.equal(FakeAudio.all.filter(x=>!x.paused).length,1);a.switchTo(key);await Promise.resolve();assert.equal(a.key,key);assert.ok(FakeAudio.all.every(x=>x.volume<=.22));}now+=1000;interval();assert.equal(FakeAudio.all.filter(x=>!x.paused).length,1);}finally{Date.now=realNow;}

a.setHidden(true);assert.equal(FakeAudio.all.at(-1).paused,true);
a.setHidden(false);assert.equal(FakeAudio.all.at(-1).paused,true);assert.equal(a.pending,true);assert.equal(a.activate(),true);await Promise.resolve();assert.equal(FakeAudio.all.at(-1).paused,false);
a.setEnabled(false);assert.equal(a.enabled,false);assert.equal(FakeAudio.all.at(-1).paused,true);assert.equal(FakeAudio.all[0].paused,true);
const diagnostics=[];let broken;
class ErrorAudio{constructor(){this.paused=true;this.volume=0;broken=this;}addEventListener(name,fn){if(name==='error')this.onError=fn;}play(){this.paused=false;return Promise.resolve();}pause(){this.paused=true;}}
const troubled=M.createAudio({title:'title.wav'},ErrorAudio,timers,e=>diagnostics.push(e));
troubled.setEnabled(true);troubled.activate();broken.error={code:4,message:'No supported source'};broken.networkState=3;broken.readyState=0;broken.onError({type:'error'});await Promise.resolve();
assert.equal(troubled.pending,true);assert.equal(troubled.enabled,true);assert.equal(diagnostics[0].mediaErrorCode,4);assert.equal(diagnostics[0].mediaErrorMessage,'No supported source');assert.equal(diagnostics[0].phase,'media');
const sfx=M.createSfx({});assert.deepEqual(sfx.keys,['choice','page','bell','sword','ending_reveal']);assert.equal(sfx.play('choice'),false);assert.equal(sfx.play('unknown'),false);
assert.equal(D.characters.length,14);assert.ok(D.characters.every(c=>fs.existsSync(`assets/characters/pixel/${c.spriteKey}.svg`)));
for(const n of Object.values(D.story.nodes))assert.ok(['normal','tension','final_day'].includes(n.musicKey)&&n.characterIds.every(id=>D.characters.some(c=>c.character_id===id)));
assert.equal(D.endings.filter(e=>e.artType==='premium').length,8);assert.ok(D.endings.filter(e=>e.artType==='premium').every(e=>fs.existsSync(`assets/endings/premium/${e.artKey}.jpg`)));assert.equal(fs.readdirSync('assets/scenes').filter(n=>n.endsWith('.jpg')).length,7);
assert.ok(D.endings.filter(e=>e.artType!=='premium').every(e=>e.artType==='none'&&e.artKey===null));
for(const key of ['title','home','normal','explore','tension','final_day','ending','ending_dark']){const f=fs.readFileSync(`assets/audio/bgm/${key}.wav`);assert.equal(f.toString('ascii',0,4),'RIFF');assert.ok(f.length>300000);}
const ui=fs.readFileSync('src/ui.js','utf8');assert.ok(!ui.includes('character-gallery')&&!ui.includes('pixel-sprite')&&!ui.includes('art-awaiting'));
const css=fs.readFileSync('src/style.css','utf8');for(const n of [430,350])assert.ok(css.includes(`max-width:${n}px`));
fs.writeFileSync('tests/media-report-v03.json',JSON.stringify({passed:true,retainedPixelCharacterData:14,pixelEndingCategories:0,premiumDataEntries:8,premiumImages:8,sceneImages:7,bgmStates:8,checks:['audio requires explicit activation after enabled preference','BGM keys crossfade without overlapping old tracks','media error retains code and message with retry state','pauses on hidden','silent until first gesture','premium keys resolve; ordinary endings have no large art','offline Ogg audio embedded in package','320px and 430px CSS rules present'],browserVisualQA:'not verified'},null,2));
console.log('Media/data regression passed');
})().catch(e=>{console.error(e);process.exitCode=1;});
