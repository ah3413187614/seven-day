/* Presentation-only continuity. Conditions inspect replayable facts; no gameplay effects. */
(function(root){
'use strict';
function scene(data,state,base){
 const last=state.history.at(-1);
 if(!last)return base;
 const rules=data.proseVariants?.[state.nodeId]||[];
 const match=rules.find(r=>(!r.incomingChoiceIds||r.incomingChoiceIds.includes(last.choiceId))&&(!r.truthsAll||r.truthsAll.every(t=>state.truths.includes(t)))&&(!r.flagsAll||r.flagsAll.every(f=>state.flags.includes(f))));
 if(match)return match.text+'\n\n'+base;
 const from=data.story.nodes[last.nodeId]?.location,to=data.story.nodes[state.nodeId]?.location;
 const region=s=>/王庭|王都/.test(s)?'王庭':/教会|圣辉/.test(s)?'教会':/龙境|旧林/.test(s)?'龙境':/故乡|渡口|边境|山路|安全领|营地/.test(s)?'边境':s;
 if(from&&to&&region(from)!==region(to))return '次日，你从'+from+'抵达'+to+'。\n\n'+base;
 return base;
}
const api={scene};if(typeof module!=='undefined')module.exports=api;root.SeventhDayProse=api;
})(globalThis);
