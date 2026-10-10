# Supply bootstrap follow-up: exact activity rows and remaining gates

2026-10-04. Read-only existing materials/original-library Capstone inspection. No source/runtime/Ghidra/original edits. **Every address below is GHIDRA image address = ELF+0x10000**, not an ELF offset.

## Recovered route family correction

- Reference bootstrap is **/reference/V2_GetSupply** (native literalG1d8fedd), CSRSyncRef::ReqSupplyCBGf84c10 ->CSRRefData::SetSupplyGddd1e8.
- Instance bootstrap is **/lobby/V2_GetSupplyInst** (literalG1d79ce1), CSRInstanceSync::ReqSupplyCBGae60e8 ->CSRPlayData::ParseSupplyInfoGb6a884.
- Status refresh is **/supply/Refresh**, RequestRefreshGf908f0 ->ReqRefreshCBGf98da0.
- Claim is **/supply/ActivityReward**, RequestActivityRewardGf94a0c ->ReqActivityRewardCBGf9502c.

These coexist with attendance/progress/newbie/special reward routes; do not invent a separate FuelReward route.

## Exact activity instance/refresh records

[RECOVERED] ParseSupplyInfo's activity sectionGb6aeb4..b6b110 reads a plain JSON collection and appends native16-byte records **id std::string+0, status uint32+12** into playdata+0x318 vector. It is **not** serialized JSON text, a scalar count, or a map keyed by status. Canonical array example:

```json
{"result_code":1,"ret_data":{
 "activity":[{"id":"<reference activity id>","status":0}],
 "activity_refresh_utc":1800000000
}}
```

Status0/time are shape placeholders, **not proved ready-state/timer values**. id literal: loadGb6af56 ->slotGb6b1d0 +PCGb6af66 ->"id"; rowstatus loadGb6af66 ->slotGb6b1d4 +PCGb6af72 ->"status". StringconversionGb6afa4; scalar conversion/storageGb6afdc..b6b038. Rowvalues appended atGb6b03a..b6b0c6.

ReqRefreshCB separately extracts ret_dataGf98ea2, reads **activity_refresh_utc** and stores playdata+0x260 atGf98f0e, then reads **activity**Gf98f16 and rows'id/status. id/status strings resolved from slotsGf99194/Gf99198. Thus the refresh response's same activity array updates status using referenced ids, rather than returning `{list:[],items:[]}` metadata.

ParseSupplyInfo also reads attend/attend_inst/type/cur/progress_cnt/offer_target_cnt/attend_newbie_log. A complete attendance/bootstrap schema is not established by this activity-only excerpt. Do not call this example a complete all-Supply replacement until the remainder is decompiled; preserving established omitted/empty branches is a separate decision.

## Activity reference records: known fields, incomplete whole minimum

SetSupplyGddd1e8 sizeG2a08 reads major groups **attend, attend_progress, attend_newbie, activity, login_bonus**. Its activity section beginsGdded98 and contains fieldlookups:

```text
id
start_time
end_time
ap
gold
group_exp
item_list[].id / .qty
card_list[].id / .qty
```

id/start_time/end_time are string-style source data; reward scalars numeric, lists follow the recovered reward-ref pattern. Particularly **start_time/end_time are not demonstrated epoch numbers**. GetFuelSupply copies firstfivecharacters of reference time strings into its display records. **HH:mm daily windows** is an inference consistent with that display behavior, not yet a complete timezone/availability computation proof.

No actual fuel/activity claim-id literal was found. **AP1 is a reward resource/item identifier in other supply paths, not an established activity.id.** Do not use AP1 as a claim key. Original activity rows appear server-authoritative; local/resource lookup REFEN/reference/V2_GetSupply should be checked if preserved reference content is available. Generic sourcefilename or AP art cannot establish an original id.

GetFuelSupplyGf48000 sizeG314 loops GetActivitySupplyCnt, loads each reference byordinalGde4a72 and corresponding instance status byordinalGb6e210, constructs its display/info records. Therefore **reference and instance activity rows must align in count/order**, not merely share a loosely similar id somewhere. A shorter instance vector may select a fallback or invalid entry; the getter must be decompiled before treating absent rows as safe.

## Older claim wrapper compatibility is pinned

**CSRSupply::RequestActivityRewardGf48acc delegates directly to CSRSyncSupply::RequestActivityReward atGf48e40.** It is not another independent HTTP response parser. Newer callback's AP-only balance/status contract therefore services the older wrapper at transport/mutation level. The older callback closure assembles SRREWARD_INFO/display data from the reference record; a compatible HTTP response alone does not create that missing reference/popup reward.

Newer claim reads user.ap.cur and **user.ap.ap_charge_time**, then unconditionallytarget_inst.id/status and SetActivitySupplyState. Omit unrelated achievement/card/item/special branches when unmodeled, per next-area-contract-priority.md. No extra legacy AP response wrapper is proved necessary.

## Status enum / actual ids: still unresolved

No named mapping **0=locked/1=ready/2=claimed** was proved in this pass. SetActivitySupplyState accepts the supplieduint32 and stores it; accepting a numeric status is not evidence of its UI meaning. The Fuel popup contains hashed UI controls, rather than named enum literals. Exact status comparison/click gating should be derived from its source/control flow or parent-owned Ghidra, not guessed from familiar conventions.

Original APrewardquantities, dailywindows/refreshcadence, actualidstrings and attendance rows remain unknown. A deliberately local activity fixture can be useful later, but first pin the full reference schema, status-ready/received semantics and time comparison units.

## Focused parent Ghidra dump request

Needed functions, exact known G addresses:

1. **CSRRefData::SetSupplyGddd1e8**, size0x2a08 — full reference group requirements, activity string/numeric fields and login_bonus safety.
2. **CSRPlayData::ParseSupplyInfoGb6a884**, size0x95c — full bootstrap parent/optionalgroups.
3. **CSRSyncSupply::ReqRefreshCBGf98da0** — fresh status update shape and rowhandling.
4. **CSRSupply::GetFuelSupplyGf48000**, size0x314 — reference/instance alignment and title/time/reward data construction.
5. **CSRPlayData::SetActivitySupplyStateGb6e226** and **GetActivitySupplyGb6e210** — no-match/default-record semantics.
6. **CSRPopUpSupplyFuel::OnButtonClickGd719f0**, **ReloadGd719d0** plus relevant shared Supply render/cell helper — exact ready/received state gate and actualclaimid selection.

Optional legacy wrapper **CSRSupply::RequestActivityRewardGf48acc**, size0x524, if verifying its reference-to-SRREWARD_INFO closure. No need to rederive route/transportAP nesting already pinned in the claim callbackGf9502c.

Existing dumps only listed several names; they did not provide these full decomp bodies. This report supplies verified partial schema and exact decompile targets rather than declaring an incomplete fixture ready for native use.

## Parent decomp follow-up: structurally valid AP-only fixture

Read parent-created `ghidra-supply-reference-refresh.txt`, `ghidra-supply-model.txt`, `ghidra-supply-strings.txt`, `ghidra-supply-fuel-ui.txt`, and `ghidra-supply-loginbonus-strings.txt`. They supersede the “dumps missing” limitation above.

### Reference minimum

SetSupply receives **full envelope** and indexesret_data. All five groups are **collections**:

```json
{"result_code":1,"ret_data":{
 "attend":[],"attend_progress":[],"attend_newbie":[],
 "activity":[{"id":"local_fuel_0","start_time":"00:00","end_time":"23:59",
   "ap":20,"gold":0,"group_exp":0,"item_list":[],"card_list":[]}],
 "login_bonus":[]
}}
```

**local_fuel_0,20AP,full-day window and any claim schedule are LOCAL FIXTURES**, not original game rows. Every activityref field shown is read by SetSupply and its strings/numeric/lists match the recovered parser. No original fuelid was recovered. A localid is acceptable if explicitly labeled and consistently present in reference/instance/claim ledgers.

`login_bonus` is always forwarded to ParseLoginBonusRefGf4ae7c. Explicit **emptyarray[] is supported**: its firstiterator equality skips parsingbody, with no `target_cnt`, items orcardreward reads. SetSupply's map::at errorGddf5c6 belongs the nonemptyattendance-group lookup (LABGdddb4a), **not** login_bonus missing handling. Empty attend/attend_progress/attend_newbie arrays avoid that branch. Adding attendance later requires matching type/group records, not copying this null-safe minimum blindly.

### Instance minimum differs from reference

For `/lobby/V2_GetSupplyInst`:

```json
{"result_code":1,"ret_data":{
 "activity":[{"id":"local_fuel_0","status":1}],
 "activity_refresh_utc":1800000000,
 "login_bonus":{"cur_value":0,"cycle":0,"cycle_log":[]}
}}
```

**Omit instance attend**, or supplynull, until attendance is reconstructed. Instance ParseSupplyInfo explicitly null-checksattend and then jumps toactivity; whenpresent, attend is an **object** with nestedattend_inst and logs. **attend:[] is not the safeinstance counterpart to referenceattend:[]** and can make objectfield indexing fail. Instance login_bonus is also an **object**, unlike reference login_bonusarray. The helper's exactkeys are cur_value,cycle,cycle_log and no economic mutation occurs here.

Referenceactivity rowordinal0 andinstance rowordinal0 must carrythe sameid. GetFuelSupply reads both vectorsbyordinal. SetActivitySupplyState separately findsits id byexactstring comparison and does nothing forunmatchedids; a claimstatus response cannot repair missing bootstrapownership rows.

### Refresh and claim minimum

Refresh returns `{activity_refresh_utc:<deadline>,activity:[{id:"local_fuel_0",status:<state>}]}` underret_data; login_bonus/attend fields need not be echoed to its dedicated reader. Deadline's exactlocaltimer policy remains a fixture and its units should be checkedagainst native timegate; name/32-bitnumericstorage alone is not a full originalUTCschedule.

AP-only ActivityReward success returns:

```json
{"result_code":1,"ret_data":{
 "user":{"ap":{"cur":42,"ap_charge_time":1800000300}},
 "target_inst":{"id":"local_fuel_0","status":2}
}}
```

Balance/deadline are illustrativefixtures. Echoexistingactivityid and use recoveredstatus2; persistAP/claimledgeratomically. Duplicateclaim must notgrant20APagain. OlderCSRSupply requester delegatesnewerSyncSupply, so no additionaloldHTTPwrapper is needed; theoldrewardpopup derivesits SRREWARD_INFO from this matchedAP reference row.

### Native status meaning is now pinned for0/1/2

`ghidra-supply-fuel-ui.txt` OnButtonClicklines181..187: **status0 invokesa waiting/toastpath withoutRequestActivityReward**; status2 skipsclaim; otherwise it canreachthe requester atline654. CellLoadswitchat~1090 explicitlyhascases0,1,2,3. **Case2 appliesgrayscale, setsreceivedtext, andshowsreceivedoverlay**; case1 hidesreceivedoverlay and is acceptedbyclicklogic. Thus **0=unavailable,1=ready/claimable,2=received** is supportedbytwoindependentconsumers. These are no longer guessed2Dcalendarsemantics.

Case3 has separatetext/markerbehavior and entersa non2 claim/purchasepath; its fullmeaning/paymentrules remainunresolved. Do notpublish3 in thefirstAP-only fixture. AwaittheactualnativeSupplyopen/claim/relaunchcontrol beforeclaimingtheentirefixture isfunctional.
