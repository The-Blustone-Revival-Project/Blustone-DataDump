# Fishing entry: bounded native contract discovery

2026-10-05. Original ELF Thumb symbols, same-register PC-relative literal
resolution and current server source only. No Ghidra/device/state/source edits.
All addresses below are Ghidra coordinates; ELF=G-0x10000. No fishing-specific
curated decomp was found by bounded filename search.

## Requests and callbacks

All requests below construct app_code/app_ver/market/pvid/otp. Exact original
route strings and additional fields are recovered, not inferred from names:

- RequestBegin **b26cbc**, ReqBeginCB **b27b38**, ParseBegin **b27d34**:
  **/fishing/Begin**, place_id (ADDb26e4e), cast_dist (b26e74), lure_id (b26e8a).
- RequestTutorialEnd **b28864** and RequestEnd **b29624**, shared ReqEndCB
  **b2a308**, ParseEnd **b2a560**: **/fishing/EndWithSell**, log_id and is_win.
  Both builders contain literal strings0/1. Do not infer a separate tutorial
  HTTP route or exact flag encoding/debit from these literals alone.
- RequestPool **b2b31c**: literal **fishing/GetFishingPool** at ADDb2b578
  (no leading slash in the original literal). Callback is not named ReqPoolCB;
  its anonymous continuation remains a targeted recovery dependency.
- RequestRecord **b2be94**, ReqRecordCB **b2c458**, **ParseRecod b2c5b8**
  (actual exported spelling): **/fishing/GetRecord**.
- RequestInven **b2c914**, ReqInvenCB **b2ced8**, ParseInven **b2d038**:
  **/fishing/GetInven**.
- RequestSell **b2d3ec**, ReqSellCB **b2db30**, ParseSell **b2b018**:
  **/fishing/SellFish**, fish_id (ADDb2d54c), grade (b2d56a), qty (b2d592).
- RequestPrice **b2dca0**, ReqPriceCB **b2e2d8**, ParsePrice **b2e438**:
  **/fishing/GetPriceRef**, fish_id (ADDb2de06).

## Response fields established, hierarchy limits

ParseBegin directly extracts full-response ret_data (ADDb27d48), then optional
achievement (b27d52), and reads log_id, init_val, max_val, dec_val, inc_val,
dec_val_on_burn. The same parser reads first_burn, burn_cool, burn_dur,
wait_time with min/max keys. Exact numeric units, nesting/object bases and
mandatory fish identity/settings still need full decomp; these literal names
alone are not an implementation-ready Begin DTO.

ParseInven also receives the full response: ret_data extraction b2d058;
achievement lookup b2d062 is conditionally applied through
Achieve.ParseAchievementsElement **8481c4** at b2d072. It then branches on
ret_data's JSON type/count (b2d076..b2d0a6), and indexes ret_data numerically
at **b2d0f6**. Row fields are **fish_id, b_cnt, s_cnt, g_cnt**. Thus a nested
guessed inven/list wrapper is not supported. Exact compatible empty outer
shape still needs confirmation, because achievement lookup precedes numeric
iteration; do not assume an ordinary bare array is safe on that mixed path.

ParseRecod similarly extracts ret_data at b2c5d8 and optionally applies
achievement at b2c5f2, then iterates its count. Row literals are **fish_id,
grade, length**. ParsePrice extracts ret_data and achievement and reads
**fish_id, b_price, s_price, g_price**. No fish grades, length units or original
prices follow from those names.

## Current fixtures and next substantive seam

Current game-routes.ts has no fishing handler. Its generic success fallback
returns ret_data={mock,route,request_keys}. Fishing is listed as a catalog
family only. That populated metadata object is not the parsed fish-record
collection, and can reach numeric indexing; successful HTTP is not compatible
native fishing state.

The smallest safe reconstruction is authenticated empty owned inventory and
empty personal records, with no catch/reward/debit invented, after pinning their
mixed achievement/collection empty-shape behavior. Parent's bounded next dumps:
**b2d038 / b2ced8** and **b2c5b8 / b2c458**. Then recover RequestPool b2b31c's
anonymous callback and local settings before claiming a usable fishing entrance.
Local settings have an exact separate source: **CSRStaticData.LoadFishingSetting
f3cb04**; place/NPC getters **f419b4/f41af8**. These may supply genuine identities
and resources, but their contents were not recovered here.

Begin/End/Sell should not grant fake catches or money while their state and
settlement remain unknown. Original fish stats, probability, lures, costs,
length grades, timers and rewards remain unresolved. No native entry was tested.

## Exact RequestPool continuation recovered

Bounded maker/literal/RTTI recovery identifies the actual state receiver at
**G b324c8 / ELF b224c8**, with Thumb function pointer **b224c9**. RequestPool's
LDR b2b728 and ADD b2b730 resolve original ELF vtable **2153c88**; offset-to-top
is0 and its invoke slot+20 contains b224c9. Its RTTI names the RequestPool$_4
TASK_READY E0 continuation. This is exact maker ownership, not a nearby-symbol
guess or whole-library pointer scan.

The earlier maker LDRb2b678/ADDb2b67a resolves vtable2153c48, invoke
**G b3219c**. That callback calls its captured HTTP JSON function and stores the
JSON result. It is not the fish-state parser and must not be mistaken for it.

At b324c8, success is GetResultCode==1 (b324ea..b324f2). Captured closure+8
contains the parsed response JSON, and closure+10 the Fishing receiver
(LDRb324e4/b324e6). Success sets receiver byte+45 to1 atb324fa, then iterates
**ret_data directly** (LDRb324f6/ADDb32500). Each row reads **lure_id STRING**
(LDRb3258a/ADDb32596, from_json b325d6) and **fish_id STRING**
(LDRb3259a/ADDb325a4, from_json b325ec), populating a
map<string,vector<string>> anchored at receiver+30/+34. This is a lure-to-fish
membership table, not recovered fish statistics or catch rewards.

Parent's precise next decompile target is **b324c8**. Nonempty published pool
membership still needs genuine local lure/fish IDs and their resource/reference
loaders; arbitrary IDs are not justified. No pool response was implemented or
tested in this lane.

## Parent parser confirmation and implementation

Targeted read-only decomp ghidra-fishing-owned-parsers.txt confirms callbacks
pass the full parsed response to ParseInven(line649) and ParseRecod(line762).
Each parser extracts ret_data, optionally reads achievement, then iterates the
same collection numerically. Existing original const JSON string-key operator
G7930f8 returns its static null fallback for arrays (gacha-single-result-contract.md);
therefore achievement is skipped for ret_data[], and array length0 skips every
fish row. A metadata object has nonzero size and is not an empty collection.
Exact recovered keys are in ghidra-fishing-inven-keys.txt and record-keys.txt.

Server now authenticates GetInven/GetRecord and returns bare empty arrays.
Other fishing requests explicitly refuse2001, without catches/bait/sales or
synthetic pools/prices. This represents the replica's no-catch account state,
not original phone inventory or reconstructed fish catalog. Focused owner/auth/
state-preservation tests, full suite, build and OpenAPI export passed. Native
fishing entry/rendering remains unverified, and no live restart occurred.
