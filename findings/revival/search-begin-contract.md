# Search /explore/Begin: original native minimum evidence

2026-10-05. Read-only original ELF Thumb disassembly/RTTI plus retained symbols. No Ghidra/device/source/runtime actions. This is an incomplete battle-start contract, not an implementation-ready full successful receipt.

## Request and callback identity

**CSRFindShardStage::RequestBegin G90eec0** posts **/explore/Begin** (LDR90f7fc / ADD90f7fe). Exact posted map has **13 fields**: auth app_code/app_ver/market/otp/pvid plus **owner,type,ref_id,inst_id,friend_pvid,friend_leader_id,vfid,wave_info**. Important index pairs: owner90f116/90f118; type90f160/90f162; ref_id90f1a0/90f1a2; inst_id90f1d8/90f1da; friend_pvid90f21e/90f222; friend_leader_id90f22c/90f238; vfid90f312/90f314; wave_info90f34e/90f352. Later literal vocabulary **explore_complete_type/explore_complete_id** belongs to a LOCAL JSON marker named **explore_complete**, set through CSRPlayData.SetMarker at90f79a; those are NOT additional posted form fields. This corrects the earlier partial literal-only grouping.

The actual successful callback is **G91b878**. Original ELF function vtable **21468c0**, invoke slot**21468e0** (primary vptr+18), points **ELF90b879/G91b879**. Actual RTTI explicitly names CSRFindShardStage12RequestBegin / TASK_READY $_11 / second callback UlSN_SR_E0. Therefore this is positive RequestBegin attribution, not a nearby-symbol guess.

Callback checks result_code==1 at91b89e/91b8a0. It indexes **full envelope.ret_data** exactly once: LDR91b8a2 slot91b8dc word144d111 / ADD91b8a6 resolves same known ret_data literalG1d689bb. Index91b8a8 returnsr0; MOVr1,r0 at91b8ac, MOVr0,r8 at91b8ae then **ParseBegin915d6c at91b8b0**. No extra explore/begin/result wrapper. It invokes the UI callback with the HTTP result code afterward, including failure codes.

## Response parser and lifecycle

**ParseBegin G915d6c** consumes numeric **log_id** (LDR915d88/ADD915d8e), a **reward_cnt collection** (LDR915de0/ADD915de6; begin/end iterator construction915df8..915e60), and **wave_info** (LDR915f24/ADD915f28), also iterated as a collection. Do not send reward_cnt as a scalar by its name. Per-wave parsing includes strict **stage_id** (LDR915fc8/ADD915fd0), **wave** (915fde/915fe0), **enemy_hp_per** (915fe4/915fe8), **enemy_atk_per** (915fe6/915fea). Additional recovered numeric vocabulary includes **skill1..skill5** (ADD9161c0/91622c/916296/916300/91636a). Their exact parent object and complete fields were not settled from this bounded instruction pass; do not put them at root by analogy.

The first log_id conversion writes directly through the selected **CSRFindShardStage target** at manager+90 and into PLAY_DATA+10 (STRD915de2). This is selected Search-instance state. A null/missing local target is not made safe by an otherwise valid HTTP body. Recover PLAY_DATA::parse G90a900 and UI target creation/selection when shaping a real start fixture.

At the end ParseBegin calls **CSRAchieve::ParseLobbyEnter** at9165c2 with its supplied ret_data, then indexes **consume_result** (LDR9165e4/ADD9165e6) and calls **CSRInventory::UseItem** at9165f2. Thus Begin is not a harmless timer receipt: it synchronizes a battle log, stages/waves and consumption. Omit unsupported optional achievement branches only after their guards are checked; do not grant fake completions or silently claim consumed ticket quantities.

Next phases have dedicated **RequestEnd G9104bc**, **ParseEnd G9167b4**, Reward/Retry/Reset/Entrust routes. GetInst returning an idle catalog with no jobs establishes entry only. Mission Complete aliases cannot settle Search log/reward state, friend support or exploration completion modes.

## Narrow parent dump targets

RequestBegin **90eec0**, ParseBegin **915d6c**, PLAY_DATA::parse **90a900**, callback **91b878**, plus exact matched-register literals. Needed before successful Begin: full wave_info row schema/monster collection and helpers; skill1..5 parent; selected target prerequisites; request wave_info/explore_complete serialization; consumption receipt shape and auth/owner/helper validation. A locally chosen target card/stage/cost/timer/reward can remain a marked fixture, but guessed enum/parent shapes would risk another pre-battle native failure.

No complete successful Begin JSON is recommended from this partial evidence. Preserve existing entry-only behavior and explicit unsupported-start refusal until the parser and lifecycle gaps above are closed. Native Search entry rendering is owned by the parent/tester and is not claimed by this read-only report.

## Parent decomp closure: schema and smallest lifecycle

New authoritative ghidra-find-shard-begin.txt/-begin-keys.txt closes the response row parents. **ret_data.reward_cnt is an array of numeric uint values** appended after resetting target PLAY_DATA+30/+34/+38 vector. **ret_data.wave_info is an array of rows**, each containing strict stage_id:string and numeric **wave,enemy_hp_per,enemy_atk_per,skill1,skill2,skill3,skill4,skill5**. Skill fields belong to EACH WAVE ROW, not root or a helper-profile object. The parser constructs native WAVE {stage_id+0,wave+c,hp_per+10,atk_per+14,skills vector+18}. It groups the collected vector under a stage-id key at manager+18; keep all rows' stage_id coherent for a minimal one-stage fixture.

Request wave_info is a **cache-miss scalar flag string**, not serialized wave rows: initial value"0"; if target INFO.target_stage_id has no WAVE-map entry it uses"1" (90f36a), then posts the field. The server should supply the full wave_info rows on a cold request, and cache/replay consistently. Empty wave_info is parser-skippable but does not prove a fight can start without its cached waves.

PLAY_DATA.parse G90a900 consumes inst_id(uint64,+8), pvid(uint64,+18), nickname(strict string,+20), end_datetime(numeric,+2c), cur_retry_cnt(numeric,+3c), cur_play_cnt(numeric,+40), **ref_id(strict string)**. It resolves ref_id against CSRFindShardStage's INFO map and stores shared INFO at+68/control+6c; missing identity leaves a null INFO. Begin derives owner from target.pvid (90f108), inst_id from target.inst_id (90f1ce), type/id/target_stage from target.INFO. A server response cannot repair a missing selected local target or unknown ref_id after this request construction.

An entry-created normal target may have zero owner/instance until its lifecycle starts; exact own/helper selection policy must be validated from native UI packets, not forced to authpvid or synthetic inst_id by analogy. No extra PLAY_DATA is created by ParseBegin; it updates the selected target's log_id and reward/wave caches.

Schema-ready single-row receipt skeleton (all values other than recovered keys/types are local policy placeholders):

```json
{"log_id":1,"reward_cnt":[0],"wave_info":[{"stage_id":"n_01_07","wave":0,"enemy_hp_per":100,"enemy_atk_per":100,"skill1":0,"skill2":0,"skill3":0,"skill4":0,"skill5":0}],"consume_result":[]}
```

**Wave0 and skill0 are NOT yet consumer-validated values** and must not be promoted as a safe battle fixture solely because they parse. Wave ordinal, skill integers, reward-count cardinality and eventual Search End consumption/reward semantics remain gaps. Stage/monster references must exist for the chosen stage. Keep optional achievement branches omitted until their parser guard is honored; ParseBegin itself contains no recovered AP/BP resynchronization.

Own-party Search combat uses **deckCASE1**, proved by CSRFindShard::MakeStageInst G906402 MOVr2,#1 before GetDeckInfo906404. Preserve the persisted mission party and source protections; do not fabricate CASE5. Before one actual attempt, recover InitBeforeOpen905c88 / MakeStageInst90610c and dedicated RequestEnd9104bc / ParseEnd9167b4. The smallest complete lifecycle needs an account-bound selected target, one stable log/attempt receipt, supported wave cache, and a dedicated End settlement/replay path; Begin-only support is insufficient to claim playable Search.
