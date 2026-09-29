/* V0.3 player history. Snapshots are immutable copies; recall never imports a run. */
(function(root){
'use strict';
const copy=x=>JSON.parse(JSON.stringify(x));
function normalize(p){p.saveVersion=3;p.journeys=Array.isArray(p.journeys)?p.journeys.slice(-40):[];p.onboardingSeen=!!p.onboardingSeen;return p;}
function record(p,state,ending,runId,now=new Date().toISOString()){
 normalize(p);
 if(p.journeys.some(j=>j.runId===runId))return;
 const j={runId,endingId:ending.endingId,endingTitle:ending.title,choiceIds:state.history.map(h=>h.choiceId),nodeIds:state.history.map(h=>h.nodeId),completedAt:now,version:'0.3.0',snapshot:copy(ending)};
 p.journeys.push(j);p.journeys=p.journeys.slice(-40);
 p.collection[ending.endingId]??={title:ending.title,role:ending.role,firstSeen:now.slice(0,10)};
 // Keep one complete historical representative even after the recent archive rolls over.
 p.collection[ending.endingId].journey??=copy(j);
}
function recall(p,key){const j=p.journeys.find(x=>x.runId===key)||p.collection[key]?.journey;return j?copy(j):null;}
const api={normalize,record,recall};if(typeof module!=='undefined')module.exports=api;root.SeventhDayJournal=api;
})(globalThis);
