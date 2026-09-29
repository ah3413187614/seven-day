const fs=require('fs'),path=require('path'),assert=require('assert/strict');
const {createAudio}=require('../src/audio.js');
function deferred(){let resolve,reject;const promise=new Promise((a,b)=>{resolve=a;reject=b;});return {promise,resolve,reject};}
class SlowAudio{
 static all=[];
 constructor(src){this.src=src;this.paused=true;this.volume=0;this.plays=0;this.pauses=0;this.start=deferred();SlowAudio.all.push(this);}
 play(){this.plays++;return this.start.promise.then(()=>{this.paused=false;});}
 pause(){this.pauses++;this.paused=true;}
}
const tick=async()=>{await Promise.resolve();await Promise.resolve();await Promise.resolve();};
// Edge rejects detached Window timer methods with "Illegal invocation".
// Test the default timer adapter against host methods that require their receiver.
const nativeSetInterval=globalThis.setInterval,nativeClearInterval=globalThis.clearInterval;
let hostFadeTick=null,hostTimerCalls=0;
globalThis.setInterval=function(fn){assert.equal(this,globalThis);hostTimerCalls++;hostFadeTick=fn;return 37;};
globalThis.clearInterval=function(id){assert.equal(this,globalThis);assert.equal(id,37);hostFadeTick=null;};
const hostErrors=[];
const hostBgm=createAudio({title:'title'},SlowAudio,undefined,e=>hostErrors.push(e));
globalThis.setInterval=nativeSetInterval;
globalThis.clearInterval=nativeClearInterval;
const errors=[],statuses=[];let fadeTick;
const timers={setInterval:fn=>(fadeTick=fn,1),clearInterval(){fadeTick=null;}};
const bgm=createAudio({title:'title',normal:'normal',ending:'ending'},SlowAudio,timers,e=>errors.push(e),()=>statuses.push(bgm.key));
(async()=>{
 // Install receiver-sensitive APIs while fadeIn executes, after play settles.
 globalThis.setInterval=function(fn){assert.equal(this,globalThis);hostTimerCalls++;hostFadeTick=fn;return 37;};
 globalThis.clearInterval=function(id){assert.equal(this,globalThis);assert.equal(id,37);hostFadeTick=null;};
 try{
  hostBgm.setEnabled(true);hostBgm.activate();SlowAudio.all[0].start.resolve();await tick();
  assert.equal(hostBgm.playing,true);assert.equal(hostTimerCalls,1);assert.equal(hostErrors.length,0);
  hostFadeTick();hostBgm.setEnabled(false);assert.equal(hostFadeTick,null);
 }finally{globalThis.setInterval=nativeSetInterval;globalThis.clearInterval=nativeClearInterval;SlowAudio.all.length=0;}
 bgm.setEnabled(true);bgm.switchTo('title');assert.equal(SlowAudio.all.length,0);
 bgm.activate();bgm.activate();bgm.switchTo('title');
 assert.equal(SlowAudio.all.length,1,'pointerdown/click/render must share one pending play');
 assert.equal(SlowAudio.all[0].plays,1);
 bgm.switchTo('normal');assert.equal(SlowAudio.all.length,2);
 assert.equal(SlowAudio.all[0].pauses,0,'old pending play must not be paused during switch');
 assert.equal(SlowAudio.all[0].volume,0,'retired pending track must be muted');
 SlowAudio.all[0].start.resolve();await tick();
 assert.equal(SlowAudio.all[0].pauses,1,'retired track pauses only after play settles');
 SlowAudio.all[1].start.resolve();await tick();
 assert.equal(bgm.playing,true);assert.equal(bgm.key,'normal');
 assert.equal(errors.length,0);assert.ok(fadeTick);
 bgm.switchTo('ending');const third=SlowAudio.all[2];
 bgm.setEnabled(false);assert.equal(third.pauses,0,'off must not pause an in-flight play');
 third.start.resolve();await tick();assert.equal(third.pauses,1);
 assert.equal(bgm.enabled,false);assert.equal(errors.length,0);

 // A genuine AbortError from an active request is an internal interruption,
 // not a browser autoplay rejection or a permanent disabled preference.
 bgm.setEnabled(true);bgm.activate();const fourth=SlowAudio.all[3];
 const abort=new Error('play interrupted by pause');abort.name='AbortError';fourth.start.reject(abort);await tick();
 assert.equal(bgm.enabled,true);assert.equal(bgm.pending,true);assert.equal(bgm.lastError,null);
 assert.equal(bgm.lastInterruption.name,'AbortError');assert.equal(errors.length,0);
 bgm.activate();const fifth=SlowAudio.all[4];fifth.start.resolve();await tick();
 assert.equal(bgm.playing,true);assert.equal(bgm.lastInterruption,null);
 assert.ok(statuses.length>=3);
 fs.writeFileSync(path.join(__dirname,'audio-race-report-v03.json'),JSON.stringify({passed:true,checks:['host-bound default timers fade without Illegal invocation','same-key pending play is single-flight','switch before settlement mutes without pause','retired promise resolution pauses after settlement','off while pending defers pause','AbortError is not reported as autoplay refusal','next gesture can recover','status updates do not start audio']},null,2));
 console.log('Audio race regression passed');
})().catch(e=>{console.error(e);process.exitCode=1;});
