/* Offline BGM: an enabled preference is not permission to autoplay. */
(function(root){
'use strict';
function createAudio(urls,AudioCtor=root.Audio,timers={setInterval:(...args)=>root.setInterval(...args),clearInterval:id=>root.clearInterval(id)},onError=()=>{},onStatus=()=>{}){
 let enabled=false,activated=false,volume=.40,key=null,current=null,previous=null,fade=null,hidden=false,lastError=null,lastInterruption=null;
 const clamp=x=>Math.max(0,Math.min(1,Number(x)||0));
 function stopFade(){if(fade!==null){timers.clearInterval(fade);fade=null;}}
 // A pending play() owns its Audio instance until the Promise settles. Muting it
 // is safe; pause() before settlement causes Edge's observed AbortError.
 function retire(track){if(!track)return;track.retired=true;track.audio.volume=0;if(track.settled){track.audio.pause();track.audio.currentTime=0;}}
 function stop(){stopFade();retire(previous);retire(current);previous=null;current=null;}
 function describe(reason,track,phase){
  const audio=track?.audio,media=audio?.error;
  return {name:reason?.name||'MediaError',message:reason?.message||media?.message||String(reason?.type||reason||'Unknown audio error'),mediaErrorCode:media?.code??null,mediaErrorMessage:media?.message||null,networkState:audio?.networkState??null,readyState:audio?.readyState??null,key:track?.key||key,phase};
 }
 function failed(track,reason,phase='play'){
  if(current!==track||track.retired)return;
  stopFade();retire(track);current=previous;previous=null;
  if(current)current.audio.volume=volume;
  activated=false;
  if(reason?.name==='AbortError'){lastError=null;lastInterruption=describe(reason,track,'interrupted');}
  else {lastError=describe(reason,track,phase);onError(lastError);}
  onStatus();
 }
 function fadeIn(track){
  const old=previous,from=old?.audio.volume||0,started=Date.now();
  stopFade();fade=timers.setInterval(()=>{
   if(current!==track){stopFade();return;}
   const f=Math.min(1,(Date.now()-started)/900);
   track.audio.volume=volume*f;
   if(old&&!old.retired)old.audio.volume=Math.min(volume,from*(1-f));
   if(f>=1){stopFade();if(previous===old){retire(old);previous=null;}}
  },40);
 }
 function switchTo(nextKey){
  key=nextKey;
  if(!enabled||!activated||hidden)return false;
  if(current&&!current.retired&&current.key===nextKey)return true; // pending and playing are both single-flight
  if(!urls[nextKey]||typeof AudioCtor!=='function'){
   activated=false;lastError=describe(new Error(!urls[nextKey]?'Missing BGM source':'Audio API unavailable'),null,'setup');onError(lastError);onStatus();return false;
  }
  stopFade();retire(previous);previous=null;
  if(current){
   if(current.settled&&current.playing)previous=current;
   else retire(current); // deferred pause if its play() has not settled
  }
  let track;
  try{
   const audio=new AudioCtor(urls[nextKey]);audio.loop=true;audio.preload='none';audio.volume=0;
   track={audio,key:nextKey,settled:false,playing:false,retired:false};current=track;
   audio.addEventListener?.('error',event=>{
    if(track.retired||current!==track)return;
    if(track.settled)failed(track,event,'media');else track.mediaFailure=event;
   });
   const result=audio.play();
   Promise.resolve(result).then(()=>{
    track.settled=true;
    if(track.retired||current!==track){retire(track);return;}
    if(track.mediaFailure){failed(track,track.mediaFailure,'media');return;}
    track.playing=true;lastError=null;lastInterruption=null;fadeIn(track);onStatus();
   },error=>{
    track.settled=true;
    if(track.retired||current!==track){retire(track);return;}
    failed(track,error);
   }).catch(error=>{
    // Exceptions in fade/status callbacks also belong to the play lifecycle.
    track.settled=true;
    if(track.retired||current!==track){retire(track);return;}
    failed(track,error,'play_chain');
   });
   return true;
  }catch(error){
   if(track){track.settled=true;failed(track,error,'play_throw');}
   else {activated=false;lastError=describe(error,null,'setup');onError(lastError);onStatus();}
   return false;
  }
 }
 function setEnabled(value){enabled=!!value;if(!enabled){activated=false;stop();return true;}return activated?switchTo(key||'title'):true;}
 function activate(){if(!enabled||hidden)return false;activated=true;return switchTo(key||'title');}
 function setVolume(value){volume=clamp(value);if(current?.playing)current.audio.volume=volume;if(previous)previous.audio.volume=Math.min(previous.audio.volume,volume);return volume;}
 function setHidden(value){hidden=!!value;if(hidden){activated=false;stop();}}
 return {switchTo,setEnabled,activate,setVolume,setHidden,get enabled(){return enabled;},get playing(){return !!current?.playing&&!current.audio.paused;},get starting(){return !!current&&!current.settled;},get pending(){return enabled&&!activated;},get lastError(){return lastError;},get lastInterruption(){return lastInterruption;},get volume(){return volume;},get key(){return key;}};
}
const SFX_KEYS=Object.freeze(['choice','page','bell','sword','ending_reveal']);
function createSfx(urls={},AudioCtor=root.Audio){return {keys:SFX_KEYS,play(key){if(!SFX_KEYS.includes(key)||!urls[key]||typeof AudioCtor!=='function')return false;try{const sound=new AudioCtor(urls[key]);sound.volume=.2;const result=sound.play();result?.catch?.(()=>{});return true;}catch{return false;}}};}
const api={createAudio,createSfx,SFX_KEYS};if(typeof module!=='undefined')module.exports=api;root.SeventhDayAudio=api;
})(globalThis);
