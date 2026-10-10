# Next area priority: village Supply activity reward

2026-10-04 read-only current-route/native-symbol/Capstone inspection. No source/runtime/Ghidra/original changes. Existing Snowfield/Glacier paths share the already reconstructed campaign contract; duplicating a new stage route does not add a genuinely new village system. Gym/recruitment and RankUp are active work. **Supply is the highest-value independent next area**, especially a repeatable fuel/activity reward supporting continued expeditions.

Current `game-routes.ts` implements Gym, recruitment, saved decks, mission progression and chests, but **no dedicated supply handlers**. `/supply/ActivityReward` falls through to generic result1 metadata with result/items arrays; the native reader expects user balances and a target status, so fake-success cannot acknowledge the actual claim.

## Exact missing route and callback

[RECOVERED] **/supply/ActivityReward**, `CSRSyncSupply::RequestActivityReward`0xf94a0c; six form fields app_code,app_ver,market,pvid,otp, **id**. Id is the supplied activity string, not hunter/card serial, target_inst_id, or an invented numeric fuelproduct. Literal id0xf94b5e/addPC0xf94b66, route0xf94c6e/addPC0xf94c74.

`ReqActivityRewardCB` **0xf9502c** checks transportstatus0 and responsecode1; non-success branches0xf95052/0xf9505e directly to callback0xf95a02 before mutation. It reads ret_data; optional achievement and user balances; **ret_data.target_inst.id/status** unconditionally and calls **CSRPlayData::SetActivitySupplyState**0xb6e226 at0xf95942. Thus acknowledging the matching activity id/status is structural, not merely diagnostic.

Parser-shaped AP-only success example:

```json
{"result_code":1,"ret_data":{
 "user":{"ap":{"cur":50,"ap_charge_time":1800000300}},
 "target_inst":{"id":"<existing activity id>","status":2}
}}
```

**AP50/deadline/status2 are illustrative fixtures, not recovered original reward or status meaning.** Do not ship a guessed activity id or status2 until the published activity record/enum is recovered. The string/number nesting is recovered. `user.ap.ap_charge_time` belongs **inside ap**, unlike the established mission/lobby flat charge-time fields.

Exact AP reads: user retainedr4; user.ap nulltest0xf95300..0e; re-indexap0xf95318 and cur0xf95322; re-indexap0xf953c6 then **ap_charge_time**0xf953ce. Target_inst.id indexes0xf958c8/0xf958d0 thenstringconversion0xf958de. Status indexes0xf958e8/0xf958f0 thennumericconversion; SetActivitySupplyState receives thatsameid+status0xf9593e..42.

Other optional native response branches are user.gold.cur, exp.prev/cur, iap.iap_qty/free_iap_qty, bp.cur/bp_charge_time, card_inven_max.cur, card[], item[] and special[]. Each branch requires its own complete known shape if included. Omit unrelated rewards/achievement while unmodeled; supplying generic null-adjacent metadata is not equivalent to an actual claim.

## Supply bootstrap needed before a meaningful visible claim

Native **/supply/Refresh** is separately proved by RequestRefresh0xf908f0, route literal0xf90b16/addPC0xf90b1c. ReqRefreshCB0xf98da0 and **CSRPlayData::ParseSupplyInfo**0xb6a884 are the next recoverable bootstrap seam. A scoped firstparse pass resolved **attend,attend_inst,type,cur,progress_cnt,offer_target_cnt,attend_newbie_log,activity,activity_refresh_utc**. This is existing exact parser evidence, not evidence that the whole supply response can be a bare list.

Remaining required research before implementation:

1. Pin Refresh callback's ret_data parent and the **activity[] record schema** through ParseSupplyInfo, plus its status enum/claim availability and UTC refresh rules.
2. Pin the referenced activity reward table and its actual id for fuel. `CSRRefData::GetActivitySupply`, GetActivitySupplyCnt/SetActivitySupplyThumb symbols exist; no original item/id is established by their names. `CSRSupply::GetFuelSupply`0xf48000 confirms a dedicated fuel model, not a route named FuelReward.
3. Compare the older **CSRSupply::RequestActivityReward**0xf48acc reader with the newer CSRSyncSupply lane. Both classes coexist. Determine which actual village/fuel UI sends the live request before declaring the new callback's minimal shape sufficient for every supply panel.
4. Recover item/card reward parser only if an actual activity needs them. AP-only fixtures can avoid inventing source item references while remaining useful, once an actual activity id/status is reconstructed.

Original fuel reward quantity, refresh cadence, attendance tables and timezone/day cutovers remain **[UNKNOWN]**. The preserved guide's four-hour fuel supply claim is community evidence, not a version-pinned server timer. Local AP quantity/cooldown may be explicitly documented revival fixtures after exact availability/status parsing is pinned.

## Why this adds real completeness

An implemented Supply loop would expose a new interactive village area, produce visible AP changes, persist claim/cooldown state, and support continued campaign play. It uses existing AP regeneration/charge deadlines and account persistence, with no new hunter/art/cut-in dependencies. Acceptance should be native Supply open -> actualclaim -> correctAP/status -> relaunchsamecooldown -> repeatclaimdoesnotdoublegrant. Unitchecks alone cannot establish Supply UI usability.

Keep current owned Nene/decks/progression intact. No server/asset restart, accountreset, appclear, blind tutorial bypass, guessed original rewards or new exposed service is warranted by this research report.
