# Search attempt persistence and wave-zero control

2026-10-05. Read-only original LOG.parse Thumb and parent's battle-end/wave-consume decomp. No source/Ghidra/device/runtime changes. Native Begin packet is parent-observed; fixture balance values remain distinct from original mechanics.

## Observed normal Begin identity

Parent captured a native request after choosing the nonowned Lantern template: **owner0,type1,ref_id017,inst_id0,friend_pvid0,friend_leader_id0,vfidlocal_lantern_helper,wave_info1**, plus auth5. It survived the server's explicit unsupported2001 reply. This corroborates the normal freshly constructed target lifecycle: a type1 candidate starts without a running GetInst instance, and helper identity is carried by vfid. Do not require owner==authpvid or inst_id>0 for this normal packet; authenticate/bind the server attempt to the actual account independently.

## GetInst play-log row is exact

**CSRFindShardStage::LOG.parse G90b2e8** consumes:

```json
{"ref_id":"017","log_id":1,"inst_id":0,"owner":0}
```

ref_id is a strict string and resolves the existing INFO reference map through90b326; absent identity leaves its shared INFO null (90b348/34a). log_id,inst_id,owner are numeric64 conversions stored atLOG+8/+10/+18 respectively. Exact original literal pairs:

- ref_id LDR90b308 / slot90b4b4 / ADD90b30e.
- log_id LDR90b38a / slot90b4b8 / ADD90b38e.
- inst_id LDR90b3d4 / slot90b4bc / ADD90b3dc.
- owner LDR90b422 / slot90b4c0 / ADD90b42a.

GetInst **ret_data.play_log[]** creates these LOG records and replaces its log vector when present. Row IDs/log values above are local examples; use the account's actual persisted accepted attempt and preserve its normal zero owner/instance identity when that is the native input. Reference017 must remain published across restart to avoid a null LOG.INFO on UI access.

**Correction to the earlier entry report: ret_data.retry_log is an array of STRICT STRINGS, not LOG objects.** ParseInst's retry_log branch (index9157fe) uses from_json<string> at decomp line1405 and stores string vector+84/+88/+8c. Only play_log invokes LOG::parse (line1276). Keep retry_log:[] until a real retry policy is implemented; don't copy play-log DTOs there. cleared_explore[] is also strings, a separate completion-ID map; populate only actual accepted completed Search outcomes if that policy is recovered/implemented.

ret_data.inst[] remains PLAY_DATA job rows, separate from play_log. A normal in-progress battle need not create a fabricated timed PLAY_DATA instance merely to persist its log. Normal selection reconstructs its transient target from reference; Begin replay/End log settlement is a server ledger responsibility. The LOG parser alone does not prove crash-resume automatically reenters combat.

## First wave and skill-zero semantics

**FindExploreWave G90bf1c** looks up the vector by target stage string and selects by **zero-based vector index**, returning null when absent/out of range. It does not search for JSON WAVE.wave numeric value. Thus the first cache row is index0, and a single actual monster-link wave can use a single matching cache row.

MakeStageInst90610c gets native stageMonsterlink waves and iterates their outer index, fetching the corresponding Search WAVE with FindExploreWave (battle-end decomp947). When no WAVE exists it creates fallback multipliers100/100 (985..986). It applies cached enemy_atk_per/100 and enemy_hp_per/100 to calculated monster stats (1089..1094). Match cache row count/order to the actual existing stage's monster-link wave count rather than inventing a second monster/wave.

The **JSON wave field** is numerically parsed into WAVE+c, but this accessor and the inspected MakeStageInst path select by vector position. Setting wave0 is compatible with the first-row convention; don't claim that this numeric field chooses the monster-link index itself.

skill1..5 become five integer values in WAVE.skills. MakeStageInst iterates them and **stores the values directly under actor skill-map keys1..5** (1098..1136), without a positive-value requirement in this assignment. Therefore zeros are structurally accepted and map to zero skill levels; basic monster combat/stat calculation remains a separate path. This is a neutral local special-skill fixture, not recovered original Search enemy skill balance. Native battle outcome still needs actual observation; no guaranteed attack behavior is claimed from the assignment alone.

## Minimum account-bound persistence policy

Persist the accepted normal target/reference/stage, vfid, actual selected CASE1 member IDs, one positive log_id and one capsule debit/Begin receipt per active attempt. Replay an identical accepted Begin without a second capsule debit. End must settle that exact account/log once and replay the cached receipt; it must not grant mission stars merely because the reused battle stage is a campaign stage. Capsule cost and trace award quantity are marked local policies; no manual grant/tutorial clear is implied.

Publish actual play_log rows on fresh GetInst; keep idle inst/retry_log arrays empty where no timed job/retry exists and use user:null for the proven no-user-write entry path. Attempt→log-list inclusion and removal rules beyond parser shape are server policy until original behavior is recovered. Returning a log record is not a direct scene jump or automatic resume mechanism.

Sources: ghidra-find-shard-battle-end.txt (MakeStageInst), ghidra-find-shard-wave-consume.txt (FindExploreWave), ghidra-find-shard-inst-contract.txt (ParseInst), original LOG.parse Thumb; parent's observed native Begin packet. No tests or runtime actions by this lane.

## Addendum: victory wave count and capsule consumption delta

**Single-wave victory sends cleared_wave1; first-wave loss sends0.** This is distinct from the zero-index wave-cache lookup.

CSRFindShard::OnFinish G907ce4 locates the monster GROUP_DATA record. At **907e88** it starts with fieldoffset1c; **907e8e compares clear to1**, **907e92 selects offset24 on equality**, then **907e98 loads that field** and passes it as RequestEnd'sr1 at907ec8. Exact field identity is independently proved by MakeFrontGroup: GetCurrentWave called **9d5576**, stored GROUP_DATA+1c at**9d557c**; GetWaveSize called **9d5580**, stored+24 at**9d5586**. ActorGroup.GetCurrentWave9a3250 reads its zero-based current index; GetWaveSize9a30cc derives actual vector length by12-byte stride. Therefore complete victory reports total wave COUNT; incomplete/loss reports current index, which equals the number of earlier waves already cleared. Do not require cleared_wave0 for a win merely because the first lookup index is0.

**consume_result.qty is the consumed DELTA, not the new quantity.** JSON UseItem Gaea5f8 parses inst_id and qty and delegates to the numeric overload **Gaea714**. That overload finds inst_id in the inventory tree+68, loads quantity argument's lowword intoIP ataea736, then for a found record: LDR currentqty at**aea7fa** (record+18), SUBcurrent−IP at**aea7fc**, STR at**aea800**. Thus consuming one helium capsule requires a receipt row `{inst_id:ACTUAL_STACK_ID,qty:1}`, even if the new stack balance is0. qty0 would leave the native balance unchanged.

The found path has no underflow clamp and does not erase the zero-quantity native instance; absent instance takes the existing diagnostic logging branch. Server validation/debit must require sufficient actual stack quantity and replay the identical receipt only for an actual retransmitted accepted operation. Do not grant a new stack, substitute a ref_id-only record or use remaining quantity as qty. Current capsule1 fixture fits the native32-bit quantity arithmetic; larger local quantities need compatible bounds if ever introduced.
