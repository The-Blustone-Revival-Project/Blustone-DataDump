# battle-lifecycle — `/mission/Start` and `/mission/Complete` response shapes

> Correction (2026-10-09): the older Start response closure below used the wrong
> callback candidates. See `campaign-start-response-audit.md` and proven Thumb
> `ghidra-campaign-start-success-callback.txt`: primary21822f0, invoke2182308,
> callablee8e671/evenentrye8e670. This receiver reads only result_code and admits
> scene4 on1, ignoring accepted:false. AP_EMPTY/DECK_NOT_OWNED must use non1.
> The older candidates were SetAutoProgress interiors, not this receiver.
> Historical loss discussion is also superseded by battle-completion.md.

Author: battle-lifecycle research agent. Date: 2026-10-02.
Scope: read-only. One file, `analysis/research/battle-lifecycle.md`.

**Headline result**

* `/mission/Complete` is **fully recovered**. Every key, every container shape and
  every side effect is read out of `CSRSyncMStage::ReqCompleteCB` (0xb426ac) and
  the matching request builder `CSRSyncMStage::RequestComplete` (0xb3aba8).
  Confidence: high. The only unresolved points are (a) which parent object
  carries two keys (`max_ap`, `level`) — solved defensively by sending both, and
  (b) three argument orderings inside helper calls.
* `/mission/Start` is **recovered on the request side and proven empty on the
  response side**. `CSRSyncMStage::RequestStart` (0xb39d2c) contains **no**
  `ret_data` and **no** `result_code` literal, and neither do
  `CSRSceneStageConfirm::RequestStartMission` (0xe879f8) nor any of the
  `std::function` thunks it installs. Confidence: high that `ret_data` is unused;
  the *value* of `result_code` is high-confidence too (1, per
  `AGENTS.md` §6 and the retry path in `ReqCompleteCB`).

---

## 0. Method note — offline key recovery (read this first, it is reusable)

`AGENTS.md` §11 warns that the `DAT_xxxx` labels in the older dumps are not
literal-pool pointers. They are not — but they are not useless either. Ghidra
prints a PC-relative string reference as

```c
_DAT_00b42a3c + 0xb42744
```

where `00b42a3c` is the **literal-pool slot address** and `0xb42744` is the ADD's
PC value. `analysis/ghidra-scripts/ResolvePcRelativeStrings.java` computes
`candidate = word[slot] + (add_instruction_address + 4)` and reads the string
there. Two facts make that reproducible **without Ghidra**:

1. The Ghidra address of a byte in this dump is `file_offset + 0x10000`
   (`analysis/native-evidence.tsv` header `IMAGE_BASE 00010000`, and
   `analysis/native-all-strings.tsv:1` shows `00010001 ELF`).
2. The literal-pool word in the **on-disk** `.so` already equals Ghidra's
   relocated value. Verified: slot `0xa27810` reads `0x13414af` on disk and
   `analysis/ghidra-setstage-exact.txt:6` reports `w=0x13414af`. Same for
   `0xa0d4f4 -> 0x1369a19` (`ghidra-wave-keys.txt`). The `AGENTS.md` note that
   "the on-disk value is a pre-relocation placeholder" is **not** true for these
   literal-pool slots — they are link-time PC offsets, not relocated pointers.

So `candidate = fread(slot) + 0xb42744`, then read the C string. Applied to the
`_DAT_xxxx + 0xyyyy` tokens in a decompile text this recovers every key exactly.
Applied to raw Thumb bytes (`ldr rN,[pc,#imm]` + a following `add rN,pc`,
whichever offset lands on a NUL-preceded printable string) it recovers the keys of
functions that have **no dump at all**.

I validated the raw-bytes variant against the two functions that *do* have a Ghidra
key dump: `CSRGameStage::SetStage` (0xa274d0) came back with 22/22 keys identical
to `analysis/ghidra-setstage-exact.txt:5-28`, and `CSRGameStage::SetArea`
(0xa28108) with an identical prefix. The technique is trustworthy. (It over-eagerly
prefers the largest `add` offset, so on its own it can mis-resolve between
suffix-merged strings — e.g. it reported `ap_charge_time` where the decompile says
`cur`. Where a decompile exists, trust the decompile; the raw scan is for
discovery.)

**A locked-out alternative:** `tools/resolve-thumb-strings.py` is marked UNPROVEN
in `AGENTS.md` §11. It is not needed — the arithmetic above is exact.

---

## 1. `/mission/Start`

### 1.1 The request — RECOVERED, already correct on the wire

`CSRSyncMStage::RequestStart`, **0xb39d2c**, decompiled at
`analysis/native-monster-stage.txt:5971-6719` and again at
`analysis/native-network-decomp.txt:4220-4970`.

* `native-monster-stage.txt:6354-6355` — request path literal
  `'/mission/Start'` (rodata 0x1d7b24e).
* `native-monster-stage.txt:6315-6316` — the body is
  `std::unordered_map<std::string,std::string>` built from an
  `initializer_list` of **exactly 10** pairs. The request is therefore a
  **URL-encoded form POST**, not a JSON body.
* `native-monster-stage.txt:6130-6288` — the 10 keys, in order:

| # | key | value |
|---|---|---|
| 1 | `app_code` | from `CPVDataMgr` |
| 2 | `app_ver` | from `CPVDataMgr` |
| 3 | `market` | `to_string(PV_MARKET)` |
| 4 | `pvid` | from `CPVDataMgr` |
| 5 | `otp` | `CPVDataMgr::GetOTP()` |
| 6 | `stage_id` | the `std::string` argument to `RequestStart` |
| 7 | `deck_inst_id_1` | `RMsprintf("%llu", lo, hi)` of `GetCurDeck()[0]` |
| 8 | `deck_inst_id_2` | `GetCurDeck()[1]` |
| 9 | `deck_inst_id_3` | `GetCurDeck()[2]` |
| 10 | `deck_inst_id_4` | `GetCurDeck()[3]` |

* `native-monster-stage.txt:6113-6117` — `CSRPlayData::GetCurDeck()` returns
  `std::vector<uint64_t>`; each entry is formatted as one `%llu` from its two
  32-bit halves. Empty deck slots therefore go out as the literal string `"0"`,
  which is exactly what `analysis/testing/report-009.md:72` observed.
* `native-monster-stage.txt:6085-6095` — a hard assertion before anything else:
  `'sStageID.size() > 1'`, `'[AST] [%s]'`, function `'RequestStart'`, source
  `'.../SR/SRMStageSync.cpp'`, line `0x43` (67). **A one-character `stage_id`
  aborts the request.** `N003` is fine; `""` and `"1"` are not.
* `native-monster-stage.txt:6622-6626` — `CPVHTTPManager::Request(...)` with the
  `TASK_ARG` built from the same `std::function`; the request method value passed
  to `CPVHTTPRequest::Create` is `2` (the same value `/mission/Complete` uses).

This matches `report-009.md` byte for byte, so **the replica's `/mission/Start`
request side needs no change.**

### 1.2 The response — RECOVERED as "no body is read"

`RequestStart` itself does not touch the response object. It only forwards it.
Verified three independent ways:

1. Reading the decompile `native-monster-stage.txt:6085-6719`: the only string
   literals in the whole function are the assertion text, `'%llu'` x3, the 10
   form keys and the path. No `ret_data`, no `result_code`.
2. Raw scan of `0xb39cd4..0xb46500` (the whole `CSRSyncMStage` module) lists the
   `ret_data` / `result_code` load sites. **None falls inside
   `0xb39d2c..0xb3a700`** (`RequestStart`). The nearest are `0xb3c72e`
   (`ReqRewardCB`) and `0xb3da02` (`ReqDeckCB`).
3. Raw scan of `0xb3a600..0xb3aba8` — the anonymous code the compiler emitted
   between the end of `RequestStart` and `RequestComplete`, which is where the
   `std::function` manager/invoke thunks live (they are the entries of the
   vtable record at `.data.rel.ro` 0x2163b48, pointing at 0xb3a618, 0xb3a658,
   0xb3a6d4, 0xb3a744, 0xb3a774, 0xb3a7a8, 0xb3ab90) — returns **zero** string
   references of any kind. They are pure forwarding/cleanup thunks.

The consumer is therefore the `std::function` that
`CSRSceneStageConfirm::RequestStartMission` (0xe879f8) installs:

* `native-monster-stage.txt:7435-7469` — a 16-byte `std::function` is heap
  allocated and its vtable word is built with the usual `_DAT_ + 0x` pair
  (`_LAB_00e87ebc + 0xe87c60`, i.e. `0x21822f0`). It captures the stage-id string
  at `param_1 + 0x788` and a `CMSpinLock<CSRDataSyncMgr>` shared_ptr, then
  `RequestStart` is called with it.
* Raw scan of the whole `CSRSceneMStageMap` + `CSRSceneStageConfirm` range
  `0xe912ac..0xe95000`: **no `ret_data`, no `result_code`.** The vtable record
  at 0x21822d0 (which contains the slot 0x21822f0) belongs to
  `CSRSceneMStageMap::SetAutoProgress` (0xe93ae0) and its neighbourhood; the only
  literals there are `'MissionAutoPlay'`, `'stage'`, `'autoplay'`,
  `'AUTO_SEL'`, `'autosel'`.

**Conclusion (RECOVERED, high confidence):** the `/mission/Start` response is
consumed only through `CPVHTTPResponse::GetResultCode()`. There is no
`ret_data` read anywhere on the expedition-start path.

That is consistent with how the battle is actually built. Per `AGENTS.md` §11,
`MakeStageInst` (0x925798) constructs both camps locally out of
`CSRPlayData::GetCurDeck()` and the `/reference/GetTargetStageMonster` wave list
(`report-009.md`'s ARM chain: `MakeCamp` -> `MakeActor` ->
`MakeBackEndActor`). Nothing in that chain needs server data, so there is nothing
for `/mission/Start` to return.

**Spec (§5.1):** answer `/mission/Start` with `result_code: 1` and an empty
`ret_data`. Keep the existing envelope fields so the shared response path is
unchanged. Do **not** invent `wave_list`/`monster` payloads there — that is
`/reference/GetTargetStageMonster`'s job.

### 1.3 [UNKNOWN] for `/mission/Start`

Not recovered, and it is the one thing a Ghidra pass should still nail down:

* **Which function actually receives the `/mission/Start` response.** Candidate
  addresses, all in the `std::function` vtable record at `.data.rel.ro`
  **0x21822d0** whose slots are `0x00e93b19, 0x00e93b1d, 0x00e93b35,
  0x00e93b45, 0x00e93b47, 0x00e93b4b, 0x00e93b4d, 0x00e93b65, 0x00e93c09`
  (thumb targets `0xe93b18 … 0xe93c08`), plus the `RequestStart`-local thunks at
  `0xb3a618/0xb3a658/0xb3a6d4/0xb3a744/0xb3a774/0xb3a7a8/0xb3ab90`. The evidence
  above says the answer is "it only checks the result code", but naming the exact
  function is still open. Run `ResolvePcRelativeStrings.java` over
  `CSRSceneMStageMap` and over the anonymous thunks `0xe93b00..0xe93c20` and
  `0xb3a600..0xb3aba8` to close it.

---

## 2. `/mission/Complete`

### 2.1 The request — RECOVERED

`CSRSyncMStage::RequestComplete`, **0xb3aba8**,
`analysis/native-mission-complete.txt:1-1010`. Signature:

```cpp
RequestComplete(const std::string& sStageID,
                const CSRGameBase::MISSIONPLAY_INFO& info,
                const std::function<void(int, const CSRGameBase::RESULT&)>& cb)
```

* `native-mission-complete.txt:652-653` — path `'/mission/Complete'`
  (rodata 0x1d7b25d), method `2`.
* `native-mission-complete.txt:571-572` — body is again a
  `std::unordered_map<std::string,std::string>` of **exactly 8** entries.
* Keys (`native-mission-complete.txt:468, 478, 484, 495, 504, 532, 535, 565`):

| key | source |
|---|---|
| `app_code` | `CPVDataMgr` |
| `app_ver` | `CPVDataMgr` |
| `market` | `to_string(PV_MARKET)` |
| `pvid` | `CPVDataMgr` |
| `otp` | `CPVDataMgr::GetOTP()` |
| `stage_id` | the `sStageID` argument |
| `deck_type` | `to_string(CSRPlayData::GetCurDeckType())` — an int, as a string |
| `play_info` | **a JSON string**, produced by `nlohmann::json::dump()` at `native-mission-complete.txt:562-563` |

* `play_info` sub-object, from `CSRGameBase::MISSIONPLAY_INFO` (stride `0x28`):

| key | line | struct offset | type |
|---|---|---|---|
| `clear` | 152-163 | `+0x28` | byte/bool |
| `clear_time` | 166-181 | `+0x2c` | int |
| `dead_cnt` | 183-198 | `+0x30` | int |
| `player_total_hp` | 200-212 | `+0x0c` | float |
| `player_total_hp_max` | 214-226 | `+0x10` | float |
| `enemy_total_hp` | 228-240 | `+0x14` | float |
| `enemy_total_hp_max` | 242-254 | `+0x18` | float |
| `atk_total` | 256-274 | `+0x00` list, summed | int |
| `atk_cnt` | 276-291 | `+0x08` | int |
| `item_use` | 293-292, 419-439 | `+0x1c/+0x20` list | array |

  `item_use` elements (`native-mission-complete.txt:309-311, 355-371`):
  `{"inst_id": <uint64>, "ref_id": "<string>", "cur_qty": <int>}`.

`server-ts` does not need to build this — the client does — but a replica log
line will show it, and the server should at least not choke on it.

### 2.2 The response — RECOVERED

`CSRSyncMStage::ReqCompleteCB`, **0xb426ac**,
`analysis/native-mission-complete.txt:1013-2851`. `param_4` is
`ret_data` (a `const nlohmann::json&`).

#### Envelope gate — RECOVERED

`native-mission-complete.txt:1133-1237`

```c
if (CPVHTTPResponse::GetResultCode() != 1) {      // L1133-1134
    if (CSRSceneMgr::VertifyResultCode(code) != 0) goto fail;   // L1135-1137
    if (CPVHTTPRequest::GetRetryCnt() > 8) { invoke cb(code); return; }  // L1138-1151
    re-issue the request;                          // L1152-1237
    return;
}
```

Consequences for the replica:

* `result_code` **must be `1`**, or the client silently retries up to 8 times and
  then fires the completion callback with a failure and parses **nothing**.
* On a non-1 code the body is never looked at, so a rejected `Complete` is safe
  even with an empty `ret_data`.

#### The parsed keys, in execution order

`ret` = `ret_data`. Every read is `nlohmann::json const::operator[](char const*)`,
so a **missing key yields a static null json** and every `is_*()` test on it is
false — omitted keys are safe, *wrong-typed* keys are what hurt. All the string
objects returned are tested with `if (*pcVar12 == '\0')`, i.e. "absent or not a
string" → skip.

| # | path | line | shape | consumed by |
|---|---|---|---|---|
| 1 | `ret_data` | 1299-1300 | object | the whole rest of the function |
| 2 | `ret_data.consumed_inst_list` | 1313-1316 | **[UNKNOWN]** — passed whole to `CSRInventory::UseItem(const json&)` | `CSRInventory::UseItem` |
| 3 | `ret_data.stage_id` | 1332-1346 | string | stored; used for `GetStageAchieveCnt`, `SetStageAchieve`, `IsMainStreamPopup`, and the `star_action` marker |
| 4 | `ret_data.user` | 1351-1352 | object | — |
| 5 | `ret_data.user.gold` | 1353-1354 | object | — |
| 6 | `ret_data.user.gold.prev` | 1355-1357 | int | read, discarded |
| 7 | `ret_data.user.gold.cur` | 1384-1386 | int | `playdata[+0x154]` (L1413-1416) — **the village gold counter** |
| 8 | `ret_data.user.exp.prev` | 1419-1421 | int | read, discarded |
| 9 | `ret_data.user.exp.cur` | 1448-1480 | int | `playdata[+0x14c]` — **the user exp counter** |
| 10 | `ret_data.user.max_ap` | 1481-1483 | object, string-tested | — |
| 11 | `…max_ap.prev` | 1484-1486 | int | `SetMarker("increase_ap","prev", v)` L1560-1567 |
| 12 | `…max_ap.cur` | 1513-1515 | int | `playdata[+0x13c]` L1543-1545 **and** `SetMarker("increase_ap","cur", v)` L1546-1553 |
| 13 | `ret_data.level` | 1575-1576 | object | — |
| 14 | `ret_data.level.prev` | 1577-1579 | int | — |
| 15 | `ret_data.level.cur` | 1606-1608 | int | **only** to set flag bit 1 when `prev != cur` (L1635-1637) — i.e. the level-up marker |
| 16 | `ret_data.user.ap` | 1638-1640 | object, string-tested | — |
| 17 | `…user.ap.prev` | 1641-1643 | int | read, discarded |
| 18 | `…user.ap.cur` | 1670-1672 | int | `SyncAP(ap_cur, ap_charge_time)` L1699-1731 |
| 19 | `ret_data.user.ap_charge_time` | 1702-1704 | number (to long) | `SyncAP` arg 3 |
| 20 | `ret_data.user.bp` | 1733-1735 | object, string-tested | — |
| 21 | `…user.bp.cur` | 1738-1740 | int | `SyncBP(bp_cur, bp_charge_time)` L1767-1796 |
| 22 | `ret_data.user.bp_charge_time` | 1767-1769 | number (to long) | `SyncBP` arg 3 |
| 23 | `ret_data.achieve` | 1808-1809 | **ARRAY** of objects | iterated with `nlohmann::detail::iter_impl` L1836-1897 |
| 24 | `…achieve[i].order` | 1835-1868 | int | `CSRPlayData::SetStageAchieve(stage_id, order)` L1869-1872, and a local `bool[order] = 1` L1873 |
| 25 | `ret_data.card` | 1909 | **OBJECT keyed by the decimal card serial** (`to_string(uint64)` at L1921) | per deck entry |
| 26 | `…card[<serial>].prev` | 1999-2030 | int | old card exp |
| 27 | `…card[<serial>].cur` | 2031-2062 | int | `CSRInventory::SetCardExp(..., cur, ...)` L2075-2076 |
| 28 | `ret_data.item` | 2249-2250 | **ARRAY** of objects | iterated L2279-2415 |
| 29 | `…item[i].inst_id` | 2277-2311 | number -> long | `CSRInventory::AddItem` arg 2 |
| 30 | `…item[i].added` | 2278-2340 | int | `CSRInventory::AddItem` arg 4 |
| 31 | `…item[i].ref_id` | 2341-2347 | string | `CSRInventory::AddItem` arg 3 |
| 32 | `ret_data.scenario` | 2416-2417 | string, tested non-empty | `CSRPlayData::AddScenario(scenario)` L2450-2472; also sets flag bit 0 |
| 33 | `ret_data.detect` | 2603-2605 | object, tested non-empty | branches the AP/BP re-sync (see below) |
| 34 | `ret_data.detect.card_ref_id` | 2772-2776 | string | stored, flag bit 3 |
| 35 | `ret_data.detect.end_datetime` | 2788-2817 | number -> long | stored, flag bit 3 |
| 36 | `ret_data.achievement` | 2823-2825 | anything, tested non-empty | `CSRAchieve::ParseAchievementsElement` L2826-2828 — **see the warning below** |

Two derived facts worth stating explicitly:

* **`prev_star` / `star` / `is_first_clear` are NOT in the response.** Lines
  2477-2602 *build* a json object and write it to a client-side marker. The
  three values are, reading the register flow:
  * `prev_star` = `CSRPlayData::GetStageAchieveCnt(stage_id)` read at
    `native-mission-complete.txt:1347-1350` — i.e. the stage's achieve count
    **before** this clear, because it is read before the `SetStageAchieve` calls.
  * `star` = `new_count - prev_count` = the number of **newly granted** `achieve`
    orders in this response (L2530, `iVar21 - iVar11`).
  * `is_first_clear` = `(prev_count == 0)` (L2564, `(iVar6 == 0)` where `iVar6`
    was set at L1349).

  It is then stored as `SetMarker(playdata, "star_action", obj)` (L2577-2582) and
  `SetMarker(playdata, "mission_auto", "is_first_clear", 1)` (L2586-2593).

  **So the star rating is carried entirely by `ret_data.achieve[].order`.** A
  three-star clear is `achieve: [{order:0},{order:1},{order:2}]`; a one-star clear
  is `achieve: [{order:0}]`; a replay with no new orders is `achieve: []`.
  Corrected 2026-10-09: the native flag bounds are0..2, not the historical1..3.

* The `if (iVar21 != iVar11)` at L2477 is a Ghidra artefact — both operands are a
  rodata pointer and a heap pointer, so the test is always true. The real
  condition is almost certainly "this clear granted at least one new order", and
  it does not change the wire shape, so I have not marked it `[UNKNOWN]` in the
  table above; it only matters if a future Ghidra pass wants to explain why a
  replay does not re-fire the new-stage effect.

#### Cross-check: what the map reads back

`CSRSceneMStageMap::CreateArea`, 0xe91f0c,
`analysis/native-stage-map-scene.txt:1904-1941`:

```c
basic_string(_DAT_00e92d00 + 0xe92a58);   // "star_action"
basic_string(_DAT_00e92d04 + 0xe92a62);   // "is_first_clear"
if (CSRPlayData::GetMarker(playdata, "star_action", "is_first_clear") == 1)
        CSRStageMarker::SetNewStageEffect(marker);
```

That is the chapter-shield / "new stage" behaviour on the map. So a `Complete`
that omits `achieve` leaves the stage's achieve count untouched, and the map's
`3/9` progress and the star shields will not move — exactly the failure mode
`AGENTS.md` §11 warns about. `SetStageAchieve` is the only progression write in
`ReqCompleteCB`; there is **no** `SetStageID`, so the "current stage" pointer is
*not* advanced by this route (it comes from `/lobby/GetMissionInst`).

`GetAreaStarCnt` is also called at `native-mission-complete.txt:1800-1804` but its
return value is discarded, so the area star total is **not** set here.

#### The `detect` branch — concrete consequence

`native-mission-complete.txt:2603-2770`. The structure is:

```c
if (ret_data["detect"] is absent/empty) {          // L2605
        uVar26 = ret_data["user"];                  // L2606-2607
        if (user["ap"] non-empty) {                 // L2608-2610
            SyncAP(user.ap.cur, user.ap_charge_time);      // L2672-2701
            if (user["bp"] non-empty)                      // L2703-2706
                SyncBP(user.bp.cur, user.bp_charge_time);   // L2738-2767
        }
} else {                                            // L2770-2817
        card_ref_id = (string)detect["card_ref_id"];
        end_datetime = to_long(detect["end_datetime"]);
        flag |= 8;
}
```

`detect` belongs to the find-shard / explore-end flow. For a plain expedition
clear the replica should **omit `detect`** so that the `user.ap` / `user.bp`
resync branch runs. Note that the `user.ap` / `user.bp` sync then happens
**twice** — once at L1638-1796 and once at L2606-2767 — so there is no
conflict in populating `user.ap` / `user.bp`.

#### `achievement` — do not send it

`CSRAchieve::ParseAchievementsElement` is at 0x8481c4
(`native-evidence.tsv`). A raw string scan of `0x8481c4..0x848a00` shows it
builds a **request**: `app_code`, `app_ver`, `market`, `pvid`, `otp`,
`'/dailyquest/GetInstList'`. Calling it from inside a response callback would
fire an unsolicited HTTP request. Send `achievement` as an **empty array** (or
omit it) and let the `*pcVar12 == '\0'` guard at L2825 skip the call.

`CSRAchieve::ParseLobbyEnter` (0x844918), called unconditionally with the whole
`ret_data` at L2820-2822, reads only `dailyquest_min_stage`, `daily_quest` and
`linear_quest` (raw scan of `0x844918..0x844c00`). All three are safe to omit.

### 2.3 Container shapes — summary table

| route / field | shape | status |
|---|---|---|
| `/mission/Complete` body | URL-encoded **form POST**, 8 fields | RECOVERED (`RequestComplete`, 0xb3aba8) |
| `/mission/Complete` `play_info` | a **JSON string** inside a form field | RECOVERED |
| `/mission/Start` body | URL-encoded **form POST**, 10 fields | RECOVERED (`RequestStart`, 0xb39d2c) |
| `ret_data` | **object** | RECOVERED |
| `ret_data.consumed_inst_list` | **[UNKNOWN]** | inferred only — see §4 |
| `ret_data.user` | object | RECOVERED |
| `ret_data.user.{gold,exp,ap,bp,max_ap}` | object with `prev` and/or `cur` ints | RECOVERED |
| `ret_data.user.{ap,bp}_charge_time` | number | RECOVERED |
| `ret_data.level` | object `{prev, cur}` | RECOVERED (parent ambiguous, see §4) |
| `ret_data.max_ap` | object `{prev, cur}` | RECOVERED (parent ambiguous, see §4) |
| `ret_data.achieve` | **ARRAY** of `{order:int}` | RECOVERED |
| `ret_data.card` | **OBJECT keyed by the decimal card serial** | RECOVERED |
| `ret_data.item` | **ARRAY** of `{inst_id:number, added:int, ref_id:string}` | RECOVERED |
| `ret_data.scenario` | string | RECOVERED |
| `ret_data.detect` | object `{card_ref_id, end_datetime}` | RECOVERED |
| `ret_data.achievement` | array | RECOVERED, but **recommended empty** |

Cross-referenced against the `AGENTS.md` §6 warnings: nothing on this path is a
bare array at the top level, and nothing is a positional container. `achieve` and
`item` are the only bare arrays and both are iterated generically
(`iter_impl`), so an *object* would also iterate — but each value would then need
its own `order` / `inst_id` key, which no server would send. **Send arrays.**

---

## 3. Battle result / reward / star — the consolidated answer

There is no `result`, `win`, `stars`, `drop` or `clear_reward` key anywhere in
`ReqCompleteCB`. The whole result model is:

| concept | wire field | client effect |
|---|---|---|
| win/lose | **implied by HTTP success** | `result_code: 1` means the mission was won. A loss is not a `Complete` at all: the entire `/mission/` literal set in `analysis/native-all-strings.tsv` is `EntrustByIAP, Start, Complete, ReqAchieveReward, Entrust, RefreshEntrust, SkipEntrust, EndEntrust` - no abort, fail or retry route exists under `/mission/`. (`/explore/Retry` and `/explore/Reset` do exist, but that is the explore/abyss feature, not the expedition map.) |
| star rating | `achieve[].order` | `SetStageAchieve(stage_id, order)` per entry; `star` = count of new entries; `prev_star` = `GetStageAchieveCnt(stage_id)` before; `is_first_clear` = that was 0 |
| chapter shield / new-stage effect | client-derived, stored at marker `star_action` | `CSRSceneMStageMap::CreateArea` reads `GetMarker("star_action","is_first_clear") == 1` and calls `SetNewStageEffect()` |
| currency reward | `user.gold.{prev,cur}` | `playdata[+0x154]`, the village gold readout |
| exp reward | `user.exp.{prev,cur}` | `playdata[+0x14c]` |
| level-up | `level.{prev,cur}` differ | flag bit 1 |
| item drops | `item[]` -> `CSRInventory::AddItem` | inventory |
| card exp | `card[<serial>].{prev,cur}` -> `CSRInventory::SetCardExp` | card instances |
| AP/BP refill | `user.ap.{prev,cur}` + `user.ap_charge_time`, `user.bp.cur` + `user.bp_charge_time` | `CSRPlayData::SyncAP` / `SyncBP` |
| AP delta bookkeeping | `user.max_ap.{prev,cur}` | `SetMarker("increase_ap", …)` |
| consumed items | `consumed_inst_list` | `CSRInventory::UseItem` |
| cutscene after a clear | `scenario` | `CSRPlayData::AddScenario` |

`AGENTS.md` §11 mentions star-rated chapter shields on the map; that is
`CSRStageMarker::SetStarCnt` (`analysis/native-stage-map-scene.txt:2122`), fed
from the same `GetStageAchieveCnt` store, so the `achieve` array is the single
source of truth for both the node numbers and the shields.

---

## 4. Open points, stated precisely

**[UNKNOWN-1] `consumed_inst_list` shape.** It is handed whole to
`CSRInventory::UseItem(const nlohmann::json&)` at
`native-mission-complete.txt:1315-1316`. `CSRInventory::UseItem` is not in any
dump; find it in the symbol table and read the keys it indexes. *Mitigation: it is
read unconditionally, so the safe fixture is an empty array `[]` — a no-op that
cannot crash. Do not send an object.*

**[UNKNOWN-2] parent node of `max_ap` and `level`.** In the decompile,
`ret_data["user"]` lives in `uVar26` and is the receiver for
`gold`/`exp`/`ap`/`bp`/`ap_charge_time`/`bp_charge_time` (lines 1353, 1417, 1639,
1704, 2607, 2707, 2740), but `max_ap` (L1481) and `level` (L1575) are shown with
`uVar8` as the receiver, and Ghidra's header for this function carries
`/* WARNING: Globals starting with '_' overlap smaller symbols at the same
address */` (`native-mission-complete.txt:1015`) — its sibling
`RequestComplete` in the same file carries `/* WARNING: Type propagation
algorithm not settling */` (line 3), so register allocation in this module is
known-unreliable. Semantically both belong under `user`, and
`/abyss/Start`'s `CSRSyncExplore::ReqAbyssStartCB` (0x91fda4) uses exactly the
`user.{ap,ap_charge_time,bp,bp_charge_time}` layout, which supports `user.*`.
*Mitigation: send `max_ap` and `level` at **both** `ret_data.*` and
`ret_data.user.*`. Extra keys are free — a present key is read, an absent one
yields a null json that fails every `is_*` guard. This is the same
"send both forms" trick that recovered the chapter shields for `GetArea`.*

**[UNKNOWN-3] `CSRInventory::AddItem` argument order.** The recovered call is
`AddItem(inventory, <int `inst_id`>, <string `ref_id`>, <int `added`>)`
(`native-mission-complete.txt:2359-2372`) against the mangled signature
`_ZN12CSRInventory7AddItemEyRKNSt6__ndk112basic_stringIc...j` =
`(unsigned long, const basic_string&, unsigned)`. The *keys* are certain; which
value is the numeric id and which is the count is not. *Mitigation: for the
expedition, gold is the only reward that matters and it comes from
`user.gold.cur`, so `item[]` can be sent as `[]` until the battle actually runs.*

**[UNKNOWN-4] the `add` pc-offset in my raw scanner.** For sites that have a
decompile this is moot (§0). For undumped functions the scanner prefers the
largest `add` offset and can therefore resolve a suffix-merged neighbour (it said
`ap_charge_time` where the decompile says `cur`). Treat raw-scan key *names* as
hints and raw-scan key *presence* as evidence.

---

## 5. Implementation spec for `server-ts`

Envelope for both routes is unchanged
(`{result_code:1, protocol_code:0, code:0, ret_data:{…}, data:{…}}`).

### 5.1 `/mission/Start`

```jsonc
{
  "result_code": 1,          // [RECOVERED] mandatory; non-1 => 8 silent retries
                             //   (analysis/native-mission-complete.txt:1133-1151)
  "protocol_code": 0,        // [FIXTURE] existing envelope convention
  "code": 0,                 // [FIXTURE] existing envelope convention
  "ret_data": {}             // [RECOVERED] EMPTY IS CORRECT. Nothing on the
                             //   expedition-start path reads it.
}
```

* Do **not** add `stage_id`, `wave_list`, `monster`, `ap` or `battle_id` to
  `ret_data`. `RequestStart` (0xb39d2c) contains no `ret_data`/`result_code`
  literal, `RequestStartMission` (0xe879f8) contains none, and the
  `std::function` thunks it installs reference no string at all.
* The request side is already correct: 10 form fields, `deck_inst_id_1..4` as
  decimal strings with `"0"` for empty slots, `stage_id` longer than one
  character.
* Server-side bookkeeping the replica should still do (not because the client
  asks, but because the game model needs it and it is invisible on the wire):
  decrement AP, set the active battle, record the deck instance ids. That is what
  `startMission` already does.
* Keep the `stage_id` fallback in `state.ts:404-408` only as a safety net, but
  note that an empty/one-character `stage_id` now trips a hard client-side
  assertion at `SRMStageSync.cpp:67`.

### 5.2 `/mission/Complete`

Assumptions used below, all **[FIXTURE]**: the stage being cleared is `stage_id`
from the request; the clear is a 3-star win; the current AP/BP/gold/exp come from
the `game` object in `server-ts/src/state.ts` (`createLocalGameState()` currently
`ap:50, bp:10, gold:10_000`). The `prev` values are the pre-increment snapshots
and `cur` the post-increment ones; the client only ever *stores* `cur`, so a
one-shot `prev == cur - delta` is sufficient and exact.

```jsonc
{
  "result_code": 1,                       // [RECOVERED] ReqCompleteCB L1133
  "protocol_code": 0, "code": 0,          // [FIXTURE] envelope convention

  "ret_data": {
    // ---- star / progression. THE ONLY thing that advances the stage. -------
    // [RECOVERED] ReqCompleteCB L1808-1897, native-mission-complete.txt
    "achieve": [                          // [RECOVERED] ARRAY of objects
      { "order": 1 },                     // [RECOVERED] key 'order' (L1835)
      { "order": 2 },                     // [FIXTURE] 3-star clear
      { "order": 3 }                      // [FIXTURE] 3-star clear
    ],

    // ---- currency / progress. ---------------------------------------------
    "user": {                             // [RECOVERED] L1351
      "gold": {                           // [RECOVERED] L1353
        "prev": 10000,                    // [RECOVERED] key, [FIXTURE] value
        "cur":  10050                     // [RECOVERED] key -> playdata+0x154
      },                                 //            [FIXTURE] value
      "exp": {                            // [RECOVERED] L1417
        "prev": 0,                        // [RECOVERED] key, [FIXTURE] value
        "cur":  120                       // [RECOVERED] key -> playdata+0x14c
      },                                 //            [FIXTURE] value
      // [FIXTURE] the +50 gold / +120 exp are local balance guesses.
      // AGENTS.md §15: these are NOT recovered production numbers.

      // AP delta bookkeeping. Also sent at the top level to cover UNKNOWN-2.
      "max_ap": {                         // [RECOVERED] L1481 (parent ambiguous)
        "prev": 50,                       // [RECOVERED] key
        "cur":  50                        // [RECOVERED] key -> playdata+0x13c
                                         //   + SetMarker("increase_ap",…)
      },

      // AP / BP clock resync. [RECOVERED] L1638-1796 AND L2606-2767.
      "ap": {                             // [RECOVERED] key 'ap'  (L1639)
        "prev": 47,                       // [RECOVERED] key
        "cur":  50                        // [RECOVERED] key -> SyncAP arg 1
      },
      "ap_charge_time": 0,                // [RECOVERED] key -> SyncAP arg 2
      "bp": {                             // [RECOVERED] key 'bp'  (L1734)
        "cur": 10                         // [RECOVERED] key -> SyncBP arg 1
      },
      "bp_charge_time": 0                 // [RECOVERED] key -> SyncBP arg 2
    },

    // ---- level-up marker: prev != cur sets flag bit 1. [RECOVERED] L1575-1637
    "level": {                            // [RECOVERED] key (parent ambiguous)
      "prev": 30,                         // [RECOVERED] key
      "cur":  30                          // [RECOVERED] key
    },                                    // equal => no level-up. [FIXTURE] values

    // ---- dropped items. [RECOVERED] L2249-2415 -------------------------
    "item": [],                           // [RECOVERED] ARRAY, keys per element:
                                         //   'inst_id'(num) 'added'(int)
                                         //   'ref_id'(string) -> AddItem.
                                         // [FIXTURE] empty: gold already arrives
                                         // via user.gold.cur, and UNKNOWN-3
                                         // leaves the arg order unpinned.

    // ---- card exp, OBJECT keyed by the decimal card serial. [RECOVERED]
    "card": {},                           // [RECOVERED] key 'card' (L1909),
                                         // keyed by to_string(deck serial)
                                         // (L1921), values {prev,cur} (L1999-2062)
                                         // [FIXTURE] empty

    // ---- consumed items. [UNKNOWN-1]; an empty ARRAY is the safe no-op.
    "consumed_inst_list": [],             // [RECOVERED] key (L1313)
                                         // [FIXTURE] empty array; shape unknown

    // ---- post-clear scenario / cutscene id. [RECOVERED] L2416-2472
    "scenario": "",                       // [RECOVERED] key, string-tested.
                                         // [FIXTURE] empty => no cutscene

    // ---- find-shard/explore-end branch. MUST be absent. [RECOVERED]
                                         //   L2603-2770: when 'detect' is
                                         //   non-empty the user.ap/user.bp
                                         //   resync is SKIPPED.
    // "detect": { "card_ref_id": "", "end_datetime": 0 },

    // ---- achievement. Send empty: the non-empty path calls
    //      CSRAchieve::ParseAchievementsElement (0x8481c4), which is a
    //      /dailyquest/GetInstList REQUEST builder. [RECOVERED] L2823-2828
    "achievement": []                     // [RECOVERED] key, array

    // ---- UNKNOWN-2 hedge: the same two objects, hoisted to the top level.
    "max_ap": { "prev": 50, "cur": 50 },  // [FIXTURE] duplicate for safety
    "level": { "prev": 30, "cur": 30 }    // [FIXTURE] duplicate for safety
  }
}
```

Explicitly **omitted** and why:

* `star`, `prev_star`, `is_first_clear` — client-derived
  (`native-mission-complete.txt:2477-2602`); sending them is inert.
* `star_action` — a *marker* the client writes, not a response field.
* `result`, `win`, `stars` — not read by `ReqCompleteCB`. The current
  `MissionCompleteResponse` in `server-ts/src/openapi.ts:534` and the body at
  `state.ts:495-506` should be reshaped to the table above; the old fields can be
  kept alongside for a few runs if agent C wants a diff-friendly change, but they
  are `[FIXTURE]` with no native support.
* `battle_id` — the native protocol has no such field.

### 5.3 What the replica should do with the request

`/mission/Complete` arrives as a form POST whose `play_info` field is a JSON
**string**. To make the replica's own trace useful, parse
`form.play_info` and log at least `stage_id`, `play_info.clear`,
`play_info.clear_time`, `play_info.dead_cnt`, `play_info.atk_total`,
`play_info.atk_cnt` and `play_info.player_total_hp` / `enemy_total_hp` — the last
two are the first real combat telemetry the project will get, and
`BLUSTONE_LOG_GAME_VALUES=1` currently logs nothing for this route because the
existing handler never looks at the body.

### 5.4 Idempotence

`ReqCompleteCB` applies whatever the response says, unconditionally — it has no
"already cleared" branch. Replays are therefore **not** safe by design; the
replica must not replay an old `Complete` body, and should make its own handler
idempotent (it already partly is, at `state.ts:475-478`) so a retried request
cannot double-grant. Note that the *client* will not retry a `result_code: 1`
response, so the replica should answer 1 even for a duplicate clear and simply
report `prev == cur` (no gold, no new `achieve` orders) — that reproduces the
original server's behaviour and is the safest way to make the second run's map
state identical to the first.

---

## 6. What the Ghidra agent still needs to decompile

In priority order. All are single functions; none needs a new script beyond
`ResolvePcRelativeStrings.java`.

1. **`CSRInventory::UseItem(const nlohmann::json&)`** — the only way to pin
   `consumed_inst_list`. It is called unconditionally from
   `native-mission-complete.txt:1315`. Grep the symbol table for `UseItem` under
   `CSRInventory`.
2. **`CSRInventory::AddItem(unsigned long, const basic_string&, unsigned)`** —
   confirms which of `item[].inst_id` / `item[].added` is the id and which is the
   count.
3. **`ReqCompleteCB` register recovery for `max_ap` and `level`** — either a
   Ghidra decompile of 0xb426ac with decompiler register recovery, or a plain
   disassembly of `0xb42a90..0xb42ab8` (the `max_ap` site) and
   `0xb42bd0..0xb42c10` (the `level` site) to see which register holds the
   `ret_data["user"]` pointer. This decides whether the top-level duplicates in
   §5.2 can be dropped.
4. **The `/mission/Start` response consumer** — run
   `ResolvePcRelativeStrings.java` over the `std::function` vtable record at
   `.data.rel.ro` **0x21822d0** (slots `0x00e93b19, 0x00e93b1d, 0x00e93b35,
   0x00e93b45, 0x00e93b47, 0x00e93b4b, 0x00e93b4d, 0x00e93b65, 0x00e93c09`) and
   over the `RequestStart`-local thunks `0xb3a618 0xb3a658 0xb3a6d4 0xb3a744
   0xb3a774 0xb3a7a8 0xb3ab90`, plus `CSRSceneStageConfirm` and
   `CSRSceneMStageMap`. The evidence says only `GetResultCode()` is read; naming
   the function makes that airtight.
5. **`CSRPlayData::GetStageAchieveCnt(const std::string&)`** — needed to know the
   legal range of `achieve[].order` (how many stars the game supports and
   therefore how many entries `achieve` may carry). `SetStageAchieve`
   (0xb6cedc, `analysis/native-setstage.txt:3275`) resolves no JSON keys, as
   expected, and is not the place to look.
6. **Optional, high value for the next milestone:**
   `CSRGameActorMob::MakeBackEndActor` (see the `report-009.md` ARM chain) is
   *not* mine — it belongs to the enemy-actor agents. But once the battle opens,
   `CSRPopUpGameResultWin::MissionClearEvent()` (look it up in
   `analysis/native-evidence.tsv`; only its type string
   `_ZN21CSRPopUpGameResultWin17MissionClearEventEv` appears in
   `analysis/native-all-strings.tsv` at 0x2b8b1e, which is a strtab offset and
   *not* its code address) is the function that will render the star display off
   the `star_action` marker, and it is worth dumping alongside the Complete work.
