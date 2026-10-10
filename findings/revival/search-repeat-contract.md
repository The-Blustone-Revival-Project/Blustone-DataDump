# Search Retry versus Reset: request and callback contracts

2026-10-05. Read-only original ELF Thumb/RTTI and previously recovered ParseInst. No Ghidra/device/source/runtime writes. Native two-wave win/reward/return is parent-observed; these two repeat transactions remain unsupported/unverified.

## Exact requests

**RequestRetry G912578** posts **/explore/Retry** (LDR9128ac/ADD9128ae). Outer form fields: auth5 **app_code,app_ver,market,pvid,otp**, plus **ref_id:string,price:number-string,price_type:number-string**. No log_id, owner, inst_id or clear metrics were recovered here. ref_id is the caller's string parameter (native retry-popup passes its+134 string at c08b1c). Request reads singleton **retry_price.amount+7c** and **retry_price.type+78**, the values populated by GetInst's nested retry_price object; it serializes them with to_string.

**RequestReset G91327c** posts **/explore/Reset** (LDR91357a/ADD91357c). Outer fields: auth5 plus **price,price_type**, read from singleton **reset_price.amount+74/type+70**. There is no targeted reference or battle log. Thus Retry is targeted by reference; Reset is global at the wire level. Do not reduce both routes to an alias for beginning a battle.

Recovered request key pairs: Retry ref_id9126c4/9126c8, price9126e8/9126ea, price_type912714/912716; Reset price9133d0/9133d2, price_type9133fe/913400. Server must validate posted price/type against its authoritative currently published quote before any charge; the client sends a quote, not authority to select its own fee.

## Callback and response parents

Retry callback **G91cd84**, original function vtable**ELF2146a40**, invoke**2146a60**→ELF90cd85/G91cd85; RTTI explicitly names RequestRetry TASK_READY $_15 secondcallback. It indexes full envelope **ret_data** (LDR91cdaa/slot91cdec/ADD91cdb0), checks result_code1 and calls **ParseInst915390 at91cdbe**.

Reset callback **G91d3d4**, function vtable**ELF2146ac0**, invoke**2146ae0**→ELF90d3d5/G91d3d5; RTTI explicitly names RequestReset TASK_READY $_16 secondcallback. It indexes **ret_data** (LDR91d3fa/slot91d43c/ADD91d400), then on success calls **ParseInst915390 at91d40e**. Both return the result code to their UI callback; no separate battle RESULT parser appears.

Therefore responses use **the direct GetInst ret_data shape**: inst[], play_log[], retry_log[]STRINGS, reset_price{price,price_type}, retry_price{price,price_type}, reset_cnt, cooltime, cleared_explore[]STRINGS and user. They do not use Begin's wave_info/log_id receipt or End's loot RESULT. Present play_log/retry_log collections replace their native stored vectors; present inst replaces running PLAY_DATA. Missing/null preserves guarded fields in ParseInst. user:null deliberately performs no player synchronization, appropriate only for a true zero-charge fixture; a paid operation needs the exact recovered SyncUser wallet update instead.

**GetRetryCnt G90ba88** counts matching occurrences of the given reference string in retry_log vector+84/+88. Multiple identical strings are meaningful counts; do not deduplicate this collection. play_log has LOG rows {ref_id,log_id,inst_id,owner}; retry_log is not that DTO. Reset/Retry response contents are what change these local vectors; callbacks themselves do not increment guessed counters or clear all completed logs on the client's behalf.

## Currency and legitimate UI routes

Normal Reset UI **CSRPopUpFindShardRetry::OnButtonClick Gbf8028** sums CPVDataMgr paid/free IAP quantities (bf8198/81a2), compares reset_price.amount atbf81a4, and opens NoMoney TYPE3 if insufficient (bf81cc). If sufficient, calls RequestReset at**bf8210**. This is a concrete Manda-backed normal UI path, not an AP/capsule purchase alias or inferred gold policy. The exact price_type enum beyond this path and original pricing tiers still need dedicated proof; retain a coherent local type1/Manda quote only as an explicit fixture until then.

The other popup **CSRPopUpExploreRetry::Request Gc086d8** has two native paths: targeted RequestRetry at**c08b26** with its reference string, and RequestReset at**c08b48**. It is distinct from the normal FindShardRetry popup. Recover its dispatch and eligibility checks before claiming individual retry usage limits or owned-versus-shared job support.

## Remaining server policy versus proved protocol

Wire targeting, quote fields, callback shape, local-vector replacement and normal Reset wallet comparison are proved. **Original Retry/Reset rules for which completed logs are removed, whether limits reset on victory/loss, INFO.period/reset-calendar policy, paid/free priority and which usage counts survive are not fully recovered.** GetInst.cooltime is now proved to be an absolute server-seconds deadline below. No evidence here says Reset restores daily virtual-helper availability: those flags come from GetHelperList/PlayData's separate maps, and these callbacks only ParseInst. Do not clear helpers, grant a capsule, claim a trace/hunter or alter campaign stars as an inferred side effect.

One-ref local implementation could choose a marked policy (e.g. targeted eligibility reopening versus global log/cooltime reset), but must preserve account/log settlement, reject active combat, bound quote/counter mutation and cache replay without repeat charge. Successful paid receipts must synchronize the native wallet with the correct SyncUser DTO. The lack of a transaction nonce and semantic retry-window collisions need an explicit local idempotency policy; parser shape does not solve that problem.

Parent's narrow next dump targets: **RequestRetry912578**, **RequestReset91327c**, callbacks**91cd84/91d3d4**, **GetRetryCnt90ba88**, **CSRPopUpFindShardRetry.SetData bf796c/SetCurrency bf7a80/SetTimer bf7ea0/OnButtonClick bf8028**, and **CSRPopUpExploreRetry.Request c086d8/SetData c08e6c**. Existing **SyncUser b7047c** decomp needs exact wallet literals if charging. No successful Repeat receipt JSON is certified from original economy in this report.

## Continuation: timer and paid-wallet semantics closed

**GetInst.cooltime is an absolute timestamp in server seconds**, not a millisecond timestamp or duration. ParseInst writes it into singleton+54. **FindShardRetry.SetTimer Gbf7ea0** reads+54 atbf7ebe, calls GetCurServerTime bf7ef6, subtracts deadline−now atbf7efa and formats the positive seconds with CMTimeToStr atbf7f28. If remaining<=0 it invokes the popup's close method+4c at**bf7f8e..bf7f96**. Thus current idle cooltime0 does not merely render0: the normal Reset popup closes immediately. A local period restriction needs its actual server-second expiry if the UI is intended to offer Reset while that restriction is active; its duration/calendar must still be labeled a local policy.

The paid SyncUser wallet DTO is now exact from **ghidra-find-shard-sync-user.txt and matched original PC-relative literals**:

```text
ret_data.user.iap       = {prev:paid_before, cur:paid_after}
ret_data.user.free_iap  = {prev:free_before, cur:free_after}
```

free_iap LDRb70734/slotb707f0/ADDb70736; both prev/cur must be present for its guarded branch, then **STRb7085c→CPVDataMgr+a0**. iap LDRb70868/slotb70af4/ADDb7086a; guarded prev/cur, then **STRb7093c→CPVDataMgr+9c**. It computes returned reward deltas afterward. Gold, if used in another supported path, similarly uses **user.gold{prev,cur}**, not a scalar or Shop's iap_qty/free_iap_qty DTO. Omit other wallet fields so their guarded branches preserve balances. This proves synchronization shape, not original paid/free spending priority or a particular fee.

Neither Retry nor Reset callback directly changes the completed-log vectors outside ParseInst. Successful responses must deliberately publish the correct authoritative play_log[]/retry_log[]/reset_cnt/cooltime snapshot for the chosen policy. A parser-compatible vector clear is not proof of an original rule that Reset removes every loss/win or grants extra capacity. Current-ref retries can be counted by repeated retry_log IDs, but the native code does not establish a server reset tier price.

## Preserved guide evidence and its limit

Read only the narrow **MISSING HUNTER RUINS** section in recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md, lines257..265, plus limited search hits; did not load the13MB guide wholesale. It describes displayed personal ruins as completable **a certain number of times each day**, friend-hunter borrowing and possible new ruin discovery after attempts. It explicitly dates a reward/currency change to **April1,2019**, naming traces/metron fragments and Helium Capsules instead of fuel. This is historical community gameplay evidence, not a 2.8.0.1 server policy table.

The section gives **no precise daily count, Reset/Retry Manda fee, fee escalation, clock timezone, log-clearing order or paid/free priority**. Other narrow hits mention roughly two-week limited hunter searches and guild partner contributions; those do not resolve these transactions. Therefore a replica's current one-hour period/capsule1/trace1 must not be presented as original daily reset fidelity.

The safely implementable seam is the exact targeted/global request distinction, quote validation, deadline display, wallet pairs and resulting log snapshot. Further native UI eligibility/dispatch decomp or original authenticated server receipts are needed to claim the historical economic rules. No server implementation or live Repeat/Reset was performed by this research continuation.
