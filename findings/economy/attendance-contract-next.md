# Attendance and Daily Sign In: distinct native seams

**Attribution correction, 2026-10-05:** the observed Supply28D Daily Sign In window uses **LoginBonus**, not `/supply/AttendReward`. Earlier attendance-receipt/calendar suggestions below concern a separate legacy attendance protocol and must not be deployed as a fix for this window. The zero-index failure is real, but its offered day comes from GetCurLoginBonusInfo and its cached rows from ParseLoginBonusRef. Read the corrected LoginBonus section at the end first.

2026-10-05. Read-only existing Supply dumps, native symbols/strings and original Thumb request literals. No calendar claims, private-state mutation, grants, source/adb/Ghidra operations.

## Bootstrap already recovered

Reference `/reference/V2_GetSupply` invokes CSRSyncRef::ReqSupplyCB Gf84c10 → CSRRefData::SetSupply Gddd1e8, full envelope. Named reference groups attend,attend_progress,attend_newbie,activity,login_bonus. The attendance row body reads **type,target_cnt,gold,group_exp,vip_exp,free_iap,iap,item_list[{id,qty}],card_list[{id,qty}]**. Source ghidra-supply-reference-refresh.txt + ghidra-supply-strings.txt. Nonempty attendance records are grouped by type and a later map::at expects matching group; arbitrary type numbers/partial groups cannot be safely published as a complete calendar.

Instance `/lobby/V2_GetSupplyInst` invokes CSRInstanceSync::ReqSupplyCB Gae60e8 → PlayData::ParseSupplyInfo Gb6a884, full envelope. Root ret_data.attend is null guarded. When present it is **OBJECT**, not reference-array shape. Recovered accesses include attend_inst.type.cur, attend_inst.offer_target_cnt.cur, attend_log, progress_cnt, progress_log, attend_newbie_inst.offer_target_cnt.cur, attend_newbie_log; logs read offer_target_cnt. Exact full nested ownership/count meanings should be preserved from the parser rather than guessed from names. Existing safe configuration omits instance attend and uses empty reference arrays.

Thus current0days/empty calendar is consistent with deliberately unreconstructed attendance content. It is not proof of broken native bootstrap transport. An OK crash versus safeX needs its actual button/ref lookup evidence; title alone does not establish whether28D or7D class is showing.

## Claim transport and exact new request proof

Ordinary attendance route **/supply/AttendReward**: CSRSyncSupply::RequestAttendReward Gf90e04; callback Gf91448. Original Thumb form keys are app_code,app_ver,market,pvid,otp, **offer_target_cnt**. Literal matched ADD sites Gf90e38/62/80/ae/de, countGf90f5e, routeGf91084. The unsigned input therefore travels as offer_target_cnt; do not call it day-index/target_cnt without UI/model arithmetic proof.

Separate progress claim Gf9221c/CBGf928d4 uses `/supply/AttendProgressReward`; newbie Gf93834/CBGf93e78 is separate. Their callback receipt reward/current-count/log/idempotence shapes are not recovered by this pass. Do not answer generic success to an exposedclaim until callback reward inventory/gold and log updates are pinned.

## Smallest parent decomp set

1. **CSRSupply::GetAttendSupply Gf487cc**, **RefData::GetAttendRefCnt Gde4956** / **GetAttendRef Gde499a**: maps current type/day to calendar rows, including zero/missing behavior.
2. Actual popup **Supply28D::OnButtonClick Gd68bd4**, InitPanelGd69544, InitCellGd696b0; or **Supply7D::OnButtonClick Gd6c250**, InitCellGd6d5d8 if measured primary vptr matches7D. This pins whether OK performs claimeddaylookup before request and why0days is unsafe.
3. **RequestAttendReward Gf90e04 / ReqAttendRewardCB Gf91448**: exact counters, balances, consumed/granted arrays and persistedclaimedlog receipt.
4. Alreadyavailable **SetSupply Gddd1e8** attendance portion and **ParseSupplyInfo Gb6a884** attendance portion: reconstruct only matching namedtype/refgroup/logs after UIgettercontract known. No broad newsearchneeded.

PlayData getters/flags are retained: GetAttendGb6e044, IsReceivedAttendRewardGb6e048, SetAttendRewardReceivedGb6e06c; progress getterGb6e0ac andflag/settersGb6e0b0/Gb6e0d2/Gb6e0d8; newbieGb6e1a8/1ac/1d0. These indicate separate receivedlogs fromeligibledaycount, not a simplefalse/truecalendar toggle.

Original reward values/calendar cadence/type enums/daily reset/offline catchup remainunknown. An eventual calendarfixture must be explicitlylocal, align reference andinstance types/offer counts, refuse zero/out-of-range/duplicateclaims, persist receipt atomically, and validate native claim+reload. No attendancefixture or claim attempted here.

## Fresh UI/claim evidence: zero-day is unsafe before HTTP

Source `ghidra-attendance-ui-claim.txt`/keys.

Supply28D OnButtonClick reads offered count, checks received state, then calls GetAttendSupply and computes **index=offer_target_cnt-1**. In dump around294..305, day0 underflows toUINT_MAX and the vector bounds check throws out_of_range before any claim request. Getter Gf487cc simply returns CSRSupply+0x18 cached vector; it does not rebuild missing references. This independently explains how an empty0days calendar's OK can be unsafe whileX closes normally. Exact observed popup class still needs primary vptr corroboration.

RefData.GetAttendRef Gde499a has a related hazard: matching type and count>=requested lets requested0 through, then computes **begin+requested*0x4c-0x4c**. Thus even a newly nonempty calendar must never publish/current-select day0. Missing type returns defaultrecord, but adding a matching type withday0 can expose a differentunderflow. Requirepositive1-basedofferedcount within matchingdensecalendar/cachelength.

## Structurally minimal neutral claim receipt

ReqAttendRewardCB Gf91448 success checks1, parses optional achievement and unconditionally ParseLobbyEnter(ret_data). User is null guarded; supplied gold/exp/free_iap/iap/vip/AP/BP/cardcapacity entries have own guards and use absolutecur pairs. Card and item grant collections are optional; omit whileunknown. Receipt completion unconditionally reads **ret_data.attend.offer_target_cnt scalar**, calls SetAttendRewardReceived, then **ret_data.progress_cnt.cur**, calls SetAttendProgressDayCnt. Progress is directly underret_data, not nestedattend.

Zero-economic-change candidate fragment, with local exampleday1:

```
{"result_code":1,"ret_data":{
  "attend":{"offer_target_cnt":1},
  "progress_cnt":{"cur":1}
}}
```

Day/counter example is aLOCAL calendarpolicy, not originalschedule. This is parser-minimum candidate only; legacy reward wrapper/result-popup rendering must be verified before calling it a native-safe emptyreward. Do not send a changedcurrencypair or item/card award for aneutralclaim. Duplicate/out-of-rangeclaim mustrefuse before servermutation and persist receiveddaylog+progressatomically for restartprojection.

## Minimal calendar constraints (parent owns exact bootstrap nesting/type)

Use matchingreferenceattendtype/currentinstanceattend_inst.type.cur, dense1-basedtarget_cnt rows and **positivecurrentoffer_target_cnt**. For a28D window, acomplete28rowneutral calendar is a safercoherentfixturecandidate than oneclaimablerow withmissingfuturelookupdefaults; exactrequiredrowcount is determined byparentInitPanel/InitCell/modelcache proof. Each row's known numericrewardfields can be0 and lists[], but thumbnail/result-no-reward guards remain a distinct UIcondition—do not claim0currencyrowsrendercorrectlyfrom parser proof alone.

Legacy claim wrapper **CSRSupply::RequestLoginReward** and cachedattendance rebuild **CSRSupply::Init/Refresh** are nextsmallfunctions if currentdumpdoesnotestablish neutralresultthumb/cacheproduction. Supply7D uses separate progress/newbie flow; its OK cannot automatically be implemented withordinaryAttendReward solelybecause bothdrawdaycells. Existingrecordtype enum/rewardcadence remainunknown.

## Correct Daily Sign In/28D LoginBonus contract

Fresh `ghidra-login-bonus-contract.txt`, `ghidra-login-bonus-keys.txt`, plus original Thumb callback attribution correct the displayed-window mapping. Supply28D InitPanel Gd69544 uses GetCurLoginBonusInfo; its claim buttonhashCD1BC65B reads that object's current value/log, then GetAttendSupply's cached INFO vector. Despite legacy accessor names HasRewardAttend/GetAttendSupply, **ParseLoginBonusRef** is the cache producer and RequestLoginReward is the actual claim function. No speculative title attribution is needed now.

**RequestLoginReward Gf49410 → /supply/LoginBonusReward**, exact target field **target_cnt** plus app_code/app_ver/market/pvid/otp. Route matchedADDGf498e6; targetcntADDGf4978a. It uses its own PVHTTP task callbacks, not CSRSyncSupply::ReqAttendRewardCB.

Reference ret_data.login_bonus is an array. Each row: **target_cnt,gold,free_iap,item_list[{ref_id,qty}],card_list[{ref_id,qty}]**. ParseLoginBonusRef Gf4ae7c synthesizes currency display entries RP1/FMD1 and builds cached32-byte INFO rows atCSRSupply+18. target_cnt rows must be denseordered1..N; curday0 is unsafe. A28rowgold100/daycalendar is an explicit **localbalance fixture**, not recovered originalrewards. Earlier recommendation to fill ret_data.attend for thiswindow is retracted.

Bootstrap instance login_bonus remains **{cur_value,cycle,cycle_log:[numeric entries]}**; fields are exact ParseLoginBonusInst Gf4ac0c. Preservecycle/logmeaningfromnativecountercode; do not guess original dailytimezone/reset/offlinecatchup. Positive currentoffer1 and matching28refrows avoidtheknown0/emptycacheindexunderflow, subjecttocorrectcountercycleprojection.

### Callback and exact response ownership

Request hidden callback addresspoint **G218c290** from slotGf49b2c+PCGf49a94; invoke+18 is Thumb **Gf4e43c**. Checks response result1 atGf4e464, indexes **ret_data** Gf4e46e (literal slotGf4e4dc +PCGf4e470 originalbytesret_data), forwards it to **ParseLoginBonusReward Gf4e47c**, then CSRAchieve.ParseLobbyEnter(ret_data) Gf4e486.

ParseLoginBonusReward receives ret_data directly. It reads **reward** object, optional reward.item[] withinst_id/ref_id/added, then **reward.user**. Gold is **reward.user.gold.cur**, not reward.gold and not rootret_data.user. Optional paid/freeManda usesreward.user.iap.paid/free prev/cur; AP/BP nestedchargefields differfromlegacyglobaluserfields. Finally it reads root **inst**, nullguard, calls ParseLoginBonusInst torefreshclaimlogs.

Gold-only parser-compatible receipt candidate withlocalexamplevalues:

```
{"result_code":1,"ret_data":{
  "reward":{"user":{"gold":{"cur":11130}}},
  "inst":{"cur_value":1,"cycle":0,"cycle_log":[1]}
}}
```

Numericgold/cycle/dayvaluesillustrativeonly;actualsuccessmustreturnpersistedabsolutegoldandtruthfulcurrentinstance. Do not grantRP1inventoryitem merelybecause it iscurrencythumbnail; capturedreferenceSRREWARD_INFO drivesrewarddisplay. Atclaimday1 appendclaimedlog1 whilecurrenteligiblevalue staystruthful; don'tadvanceoffer2solelytoallowanothersamedayclaim. Persistgold+claimlogatomically andrejectduplicatesbeforemutation. A repeat's non1 callback avoidsmutations; requesthasnoexpectedversion/nonce.

Parent finalsmalldecomp **Gf4e43c** preserves fullnetworkret_dataownershipproof. Current rootinstance/logperiodpolicy and nativeclaim/reload control remain outstanding; this lane didnotclaim orchangebalances. All earlier AttendRewardshape observations remainvalidforseparatelegacyrouteonly.
