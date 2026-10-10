# Search End and deferred Reward: native contract

2026-10-05. Read-only ghidra-find-shard-battle-end.txt/-keys.txt plus original ELF Thumb/RTTI for Reward and callback identity. No source/Ghidra/device/runtime mutations.

## End request and exact callback

**RequestEnd G9104bc** posts /explore/End (LDR910d78/ADD910d7a). Its outer form map has exactly8 fields: **app_code,app_ver,market,pvid,otp,log_id,cleared_wave,play_info** (decomp unordered_map count8). log_id is the selected target's Begin-assigned battle-log identity; cleared_wave is the numeric caller argument. They are not campaign stage_id/bid.

**play_info is serialized JSON**, containing **clear,clear_time,dead_cnt,player_total_hp,player_total_hp_max,enemy_total_hp,enemy_total_hp_max,atk_total,atk_cnt,item_use**. Native literals do not include atk_max here. item_use is its own collection of **inst_id,ref_id,cur_qty** records; empty input represents no reported item use. Do not move these fields into the outer form or replace clear with Arena is_win.

Actual callback **G91bec4** is positively identified by original ELF function vtable**2146940**, invoke slot**2146960**→ELF90bec5/G91bec5. RTTI names CSRFindShardStage::RequestEnd / TASK_READY $_13 / second callback. It creates an ordinary RESULT, parses successful envelope.ret_data, calls **ParseEnd G9167b4 at91bf98**, then supplies result_code and RESULT to the UI callback. Result-construction fields are not additional response keys.

## End response parents

ParseEnd reads its ret_data object with these exact parents:

- **achievement** optional; omit when not reconstructed. A present nonnull value calls ParseAchievementsElement. Full ret_data is also passed to ParseLobbyEnter.
- **consume_result** passed to CSRInventory.UseItem. Empty array reports no consumption.
- **wave:{cleared_wave:number,max_wave:number}**, optional parent; values populate result counters. They are not root scalar fields and do not grant campaign stars.
- **item[]:{inst_id:uint64,ref_id:string,added:number}**. Nonempty rows invoke Inventory.AddItem and construct result loot; identities must resolve published item references. Use added, not guessed qty, for actual inventory delta.
- **gem[]**, nonempty entries invoke CSRGem.ParseGem. Empty avoids unreconstructed gem mechanics.
- **special[]**, nonempty entries invoke SyncSupply.ParseSpecialSupply and PlayData.AddSpecialSupply. Empty avoids supply-reference grants.
- **reward_item[]:{ref_id:string,qty:number}**, collected into up to four result/display slots. This is separate from item[] actual AddItem mutation; don't claim a displayed reward count is an inventory award.
- **detect**, omit or null for no discovery. A present nonnull object requires strict **ref_id:string** resolving an existing Search INFO, plus numeric **end_datetime**. Missing INFO is dereferenced while building the detected target-card announcement. **detect:[] is unsafe**, not an empty-discovery alias.

The literals **user/card_id** at91731c/91736e belong to a LOCAL chat-announcement JSON built after nonnull detect. They are not indexed from the server receipt. ParseEnd contains no recovered SyncUser, AP/BP synchronization, team/hunter EXP, gold or direct hunter grant parser. Do not import mission-completion DTOs into this response.

Result.stage_id is copied from the selected target INFO.target_stage_id, not a root receipt key. A valid selected target/INFO must still exist until the callback completes.

Minimal zero-loot receipt candidate:

```json
{"wave":{"cleared_wave":0,"max_wave":1},"consume_result":[],"item":[],"gem":[],"special":[],"reward_item":[],"detect":null}
```

The sample counters are placeholders: derive them from the accepted attempt's configured waves and the actual native completion, not a forced win. Empty rewards are an explicit local policy, not recovered original economy. Keep campaign AP/stars and hunter ownership unchanged by Search settlement unless a distinct proven grant parser/policy is implemented.

## Deferred Reward is a separate transaction

**RequestReward G9118b8** posts /explore/Reward (LDR911ba6/ADD911ba8), with auth5 plus **ref_id and inst_id**. This uses the selected Search reference/instance, not Begin.log_id or mission.stage_id. Request method currently has no separately recovered owner field.

Actual callback **G91c5f0** has original function vtable**ELF21469c0**, invoke**21469e0**→ELF90c5f1/G91c5f1; RTTI explicitly names RequestReward TASK_READY $_14 secondcallback. It indexes full envelope.ret_data (LDR91c618/ADD91c61e→known ret_data literal), on success removes the claimed selected instance from the local PLAY_DATA map (erase91c680) and calls **ParseReward917c04 at91c6b2**. It returns the ret_data JSON to its UI callback.

ParseReward starts with **ret_data.item[]**, with exact **inst_id,ref_id,added** vocabulary. Its full transitive nonempty reward behavior still needs parent decomp; an empty **{item:[]}** skips item iteration but does not prove a complete claim screen or original reward economy. RequestReward must be account-bound and settle a real claimable instance once; no synthetic running job is needed for entry-only Search. UI reward claims remain untested.

## Smallest coherent lifecycle and remaining evidence

Begin needs a selected valid INFO/PLAY_DATA and one server log; an accepted End needs that same account/log/target, bounded configured wave count and an exact repeatable cached receipt. Protect the real CASE1 mission party during the active attempt. Dedicated Search End must not call mission Complete or award campaign stars merely because its target_stage_id reuses a campaign battle reference. Bind native helper/owner choices only after their request path is recovered.

To support discoveries or claim awards, first decompile **RequestReward9118b8**, **callback91c5f0**, **ParseReward917c04** and **LOG.parse90b2e8**. Nonempty gem/special/achievement branches require their own already named parsers and references; empty fixtures avoid those unmodeled mechanics. End callback91bec4 and Reward callback91c5f0 keys can be independently corroborated by the parent's corrected resolver. Native fight wave/skill consumers remain owned by the MakeStageInst/InitBeforeOpen research lane.

Source balance values, discovery chance, original timer/claim quantities and restart policy are not recovered here. Parser compatibility alone is not a native Search battle/Reward PASS.
