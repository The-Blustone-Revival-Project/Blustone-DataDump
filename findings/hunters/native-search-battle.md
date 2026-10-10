# Native Hunter Search loop verified — 2026-10-05

Native Search now runs from village through reference/instance load, normal
selection, original Lapis story, preparation, virtual partner selection, two
actual combat waves, dedicated End, Search Complete result and village return.
The original APK/phone were untouched; instrumented+8 was not rebuilt or cleared.

## Dedicated backend

search-battle.ts persists an account-bound monotone log, CASE1 snapshot, helper
usage and settlement. Normal owner0/type1/ref017/inst0/helper packet is recovered
and was actually emitted (86). Search normally spends one earned AIRSHIP_TICKET;
quantity decrement uses consume_result.inst_id/qty1. Search End has its own wave,
item delta and reward_item display fields. It never calls mission Complete or
changes campaign stars/AP/BP/gold/EXP/hunter ownership/tutorial flags.

One initial guided attempt at capsule0 is an EXPLICIT LOCAL recovery waiver.
Earned stage8, actual37/0 acknowledgement, pending37/1, selected known helper,
no previous Search settlement and unused waiver are required. Original economics
are unknown. The native guide reaches Begin at capsule0 and blocks Airport
(92), so this policy restores that onboarding path without a manual item grant,
retroactive reward or tutorial flag clear. Once accepted, it is persisted and
cannot fund another attempt. Replaying the SAME pending log is allowed.

Normal capsule1, trace1 per victory, one-hour reference period and helper use per
UTCday are local policies. Original balance/rates/timers remain missing. Replay
receipts omit inventory deltas so native AddItem/UseItem cannot apply twice.
Without a recovered request nonce, loss of the FIRST response may need a normal
inventory refresh; native transport exactly-once delivery is not promised.

CASE1 edits refuse while active; both training source protections include the
Search snapshot. Campaign/arena starts are mutually exclusive with Search.
Source quantities and new item/log allocators refuse at supported limits.
Old saves receive an empty Search model; strict normalization preserves valid
logs/receipts and rejects malformed records. Pending helpers remain selectable
for that same log; only completed plays enter play_log history. No fake job is
created in GetInst.inst[]. Reward/Retry/Reset/Entrust and trace recruitment remain
explicitly unsupported.

## The one-wave assertion and its repair

First accepted Begin log1 (2938) rendered actors but stopped at ShowEffect / 
SRGameBase.cpp2006. A first early tap was suspected. Preserved restart3768 replayed
log1 with no additional debit/reward and NOINPUT12s reproduced the assertion
(106), disproving early tapping as the sole cause. Assertions were never closed.

Original mode4 Search OnProcWaveChange formats IG_WAVE(current+1)_(total).
InitEffect registers totals2,3,4 only; single-wave Search asks for unregistered
IG_WAVE1_1. The instruction/decomp proof is in search-effect-root-contract.md.
Added unlinked local_search_017 and two actual nested monster-link waves, backed
by existing M001 art/stats, plus two matching Begin rows. Campaign links and
single-wave references remain unchanged. Pending log1's incompatible n_01_07
fixture migrates to that reference/wave_count2; its party/cost/log/waiver are
preserved, and completed receipts are not rewritten. No native patch/effect
suppression or new client release was needed.

## Native win and exact deltas

Preserved boot4644 loaded the new stage/links and resumed log1. Warning effect
then full combat HUD1/2 rendered (113/114). Two ordinary taps at540,850 defeated
both M001 enemies; no exit-door input. Screenshot115 captures a death/impact
frame at2/2. Native End at00:33:29.912Z sends log1/cleared_wave2 and:

- clear1, atk_cnt2, atk_total362, dead_cnt0, item_use[].
- enemy_total_hp0, enemy_total_hp_max200.
- player_total_hp4552.5, player_total_hp_max5120, clear_time0.

End HTTP200/plaintext478 accepted and persisted one local_sylvester_trace,
instance6/qty1. activeSearch became null. Gold10660, TeamEXP360,10owned hunters,
party, skills, campaign flags and Manda stayed unchanged. Private before/active/
after snapshots and crash logs are under recovered-assets/search-battle-2026-10-05.
Never publish those account/session snapshots.

Post-win original story (117/118) and free Skip produced Search Complete / Reached
level2/2 / collected item1 / SylvesterTraces1/10 (120). Okay fetched GetInst and
returned Collect Traces1/10, EntranceLimit0/1 (121). Close/Home returned village
and an empty Daily Sign In Supply popup (122); closing its X safely returned the
responsive village31/150 (123), same4644 alive. Daily attendance is still not
reconstructed; its prior OK path caused a separate process death. No supply
claim was made here. No new native tuto/Clear was observed after this win, so
37/1 must not be claimed server-cleared.

Full npm test/build pass. Meaningful checks cover earned versus guided cost,
auth/owner/helper identity, logs/restart, replay deltas, cross-account/stale End,
party/source protections, outcome/wave agreement, loss/no reward, allocator
capacity, separate campaign references and pending migration. Ordinary capsule
earning/spending, native defeat, repeat/reset/dispatch/recruitment and relaunch
of the completed trace display remain follow-up work.
