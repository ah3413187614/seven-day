/** Authoritative data contracts. Runtime uses plain JS for dependency-free file:// playback. */
export type Stat = 'Courage'|'Reason'|'Mercy'|'Ambition'|'Faith'|'Freedom'|'Sacrifice'|'Corruption';
export type Faction = 'Kingdom'|'Church'|'Demons'|'Companions'|'Dragons'|'People';
export type EndingKind = 'normal'|'growth'|'contradictory'|'secret'|'true'|'bad';
export type Visibility = 'PLAYER_VISIBLE'|'DESIGNER_ONLY';
export type Role = 'savior'|'hero'|'vessel'|'guardian'|'king'|'pontiff'|'godslayer'|'wanderer'|'ordinary'|'martyr'|'exile'|'tyrant'|'witness'|'ferryman'|'dragonkeeper'|'failed';
export type StatChange = Partial<Record<Stat,number>>;
export type RelationshipChange = Partial<Record<Faction,number>>;
export interface FlagRequirement {all?:string[]; any?:string[]; none?:string[];}
export interface Snapshot {stats:Record<Stat,number>;relations:Record<Faction,number>;}
export interface HistoryEntry {day:number;nodeId:string;choiceId:string;mode:"full"|"limited";stat_change:StatChange;primary:Stat;text:string;consequence:string;flags:string[];before:Snapshot;after:Snapshot;}
export interface GameState extends Snapshot {schemaVersion:2;nodeId:string|null;day:number;flags:string[];truths:string[];knowledgeLog:{id:string;day:number;source:string;evidence:string}[];metNPCs:string[];encounterLog:{id:string;day:number;nodeId:string;choiceId?:string}[];history:HistoryEntry[];finished:boolean;role:Role|null;meta:{completedRuns:number};}
export interface Permission {truthsAll:string[];flagsAll:string[];flagsAny:string[];relationsMin?:RelationshipChange;arcProgressAny?:string[];}
export interface Choice {requirement?:Permission;fallback?:Partial<Choice>;truths:string[];encounters:string[];choice_id:string;node_id:string;visibility:Visibility;text:string;understanding:string;consequence:string;gain:string;cost:string;DESIGNER_ONLY:{primary:Stat;stat_change:StatChange;relationship_change:RelationshipChange;add_flags:string[];remove_flags:string[];arc_tags:string[];long_term:string};next_node:string|null;terminal_role:Role|null;}
export interface StoryNode {node_id:string;day:number;title:string;scene:string;location:string;visibility:Visibility;previous_requirement:{day:number;any_previous_choice:string[];flags?:FlagRequirement};on_enter_flags:string[];truths:string[];encounters:string[];choices:[string,string,string,string];}
export interface CharacterArc {arc_id:string;title:string;early:Stat;late:Stat;roles:Role[];early_flags_any:string[];late_flags_any:string[];priority:number;early_days:number[];late_days:number[];early_min:number;late_min:number;pivot_required:boolean;pivot_days:number[];}
export interface EndingRule {ending_id:string;title:string;category:string;type:EndingKind;priority:number;trigger?:{role?:Role;dominant?:Stat;anyCrime?:boolean}|CharacterArc;trigger_text?:string;meaning:string;visibility:Visibility;}
export interface Epilogue {number:string;title:string;main:string;npc:string;world:string;self:string;last:string;}
export interface EndingResult {endingId:string;title:string;summary:string;role:Role;kind:EndingKind;dominant:Stat;arcs:string[];crimes:string[];violent:string[];evidence:{day:number;text:string;consequence:string}[];status:{dragon:string;previousHero:string;player:string};reason:string;metNPCs:string[];relations:Record<Faction,number>;epilogue:Epilogue;badges:{zeroDirectKill:boolean;allNamedAlive:boolean;swordless:boolean;independent:boolean};}
export interface SaveFile {schemaVersion:2;meta:{completedRuns:number};choiceIds:string[];}
export interface EndingEngine {initial(meta?:{completedRuns:number}):GameState;apply(state:GameState,choiceId:string):GameState;finish(state:GameState):EndingResult;resolveChoice(state:GameState,id:string):Choice & {mode:"full"|"limited"};permitted(state:GameState,requirement?:Permission):boolean;replay(ids:string[],meta?:{completedRuns:number}):GameState;importSave(save:SaveFile):GameState;exportSave(state:GameState):SaveFile;}
