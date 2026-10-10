# Expedition-map chests: claim route, sprite state, popup, and "cannot receive"

**Status 2026-10-03 · native-analysis agent · read `AGENTS.md` §6/§8/§15 first.**

Raw dumps this report is built from (all Ghidra addresses, = ELF + `0x10000`):

| file | contents |
|---|---|
| `analysis/ghidra-chest-01-reward-route.txt` | `CSRSyncMStage::RequestReward`, `ReqRewardCB`, `CSRSceneMStageMap::SendRewardRequest`, `AchieveRewardCB`, `IsOpened`, `SetRewardVisible`, `ShowReward`, `SetClearRewardThumb`, `PopUpClearReward` |
| `analysis/ghidra-chest-02-sources.txt` | `OnRefresh`, `OnProcessCursorPress`, `OnInit`, `CSRPopUpMStageRewardShow::SetData`, `CSRPlayData::IsReceivedAchieveReward`, `SetAchieveRewardReceived`, `GetStageAchieveCnt`, `SetStageAchieve`, `CSRGameStage::SetArea` |
| `analysis/ghidra-chest-03-getters.txt` | `CSRGameStage::GetStageCnt`, `GetStageLinks`, `GetRewards`, `CSRPlayData::SetStageAchieve` |

**One-line answer up front.** Tapping a claimable chest calls
**`POST /mission/ReqAchieveReward`** with **7 form fields**; its `ret_data` must be a JSON
**object** carrying **`achieve_cnt`** that equals one of the published
`achieve_reward[].achieve_cnt` values, or the client throws the reward away and shows a
toast. The chest sprite state is **100 % client-side**, computed from two integers and one
boolean; the "simultaneously open and closed" symptom is a **fixed client/UI behaviour of
`ShowReward`** that **no server response can change**.

---

## Q1 — Which route does tapping a claimable chest actually call?

**[RECOVERED]** `CSRSceneMStageMap::SendRewardRequest()` (`0xe9a168`) ends in:

```c
CSRSyncMStage::RequestReward(this->0x7f8 /* area_id string */, uVar3 /* reward index */, cb);
// ghidra-chest-01-reward-route.txt:1662
```

`CSRSceneMStageMap::OnInit` (`0xe912ac`) sets `this->0x7f8` from
`CSRUserDB::GetCurAreaID()` (or `GetCurExploreAreaID()` when the current scene is `0x11`)
— `ghidra-chest-02-sources.txt:244-258`, and falls back to a 4-char default
(`DAT_00e91690 + 0xe91426`) if that is empty.

**[RECOVERED]** `CSRSyncMStage::RequestReward(const string& area_id, int index, cb)`
(`0xb3bf4c`) builds a `CPVHTTPRequest::Create<…, CPVHTTPMapToEncodedURLFormTransformer<unordered_map<string,string>>, CPVHTTPRequestEncryptor>`
— i.e. **URL-encoded form POST** — with **exactly 7 entries**
(`unordered_map(local_118, local_d0, 7)` at `ghidra-chest-01-reward-route.txt:168`),
then

```c
CPVHTTPRequest::Create<…>(&req, url, DAT_00b3c318 + 0xb3c23a /* "/mission/ReqAchieveReward" */, 2, map, 0);
CPVHTTPManager::Enqueue(mgr, &req, ReqRewardCB);
```

### Request keys — **[RECOVERED]**, 7 fields

| key | value | evidence |
|---|---|---|
| `app_code` | `_SR` | `ldr@0xb3bf98`, string `0x01d689d0` |
| `app_ver` | `2801` | `ldr@0xb3bfc2`, `0x01d689d9` |
| `market` | `PV_MARKET` | `ldr@0xb3bfe0`, `0x01d689ee` |
| `pvid` | numeric | `ldr@0xb3c00e`, `0x01d686aa` |
| `otp` | session OTP | slot `0xb3c30c` + addend `0xb3c046` → `0x01d689ea` (`otp`) |
| `area_id` | **the function's `const string&` arg** | `ghidra-chest-01-reward-route.txt:155-157` |
| `target_achieve_cnt` | **`to_string(GetRewards()[index].achieve_cnt)`** | `:158-160` |

`target_achieve_cnt` is **not** the raw index — it is the *reference* value, read from the
area catalog:

```c
CSRGameStage::GetRewards(&vec);                              // :82
std::to_string(&s, *(int *)((int)vec + index * 0x34));        // :158  stride 0x34
```

The callback is `function<void(int, unsigned char)>` — see Q4.

### `CSRAchieve::GetDataList` / `GoShortcut` — **NOT on this path**

**[RECOVERED]** `CSRAchieve::GetDataList()` (`0x847160`), `CSRAchieve::GoShortcut(const string&)`
(`0x84dcb0`) and `CSRAchieve::RequestReward2(shared_ptr<DATA>, function<void(int)>)`
(`0x845ca0`) belong to the **daily-quest / achievement-list scene**
(`CSRSceneAchieve`, `CSRSceneAchieveList`, `CSRTabAchieve`, `CSRPopUpAchieve`), not to the
expedition map. `RequestReward2`'s lambda is bound at `0x01dd6fb2`
(`PVHTTP::TASK_READY<…, RequestReward2…, …>`) — no `/mission/ReqAchieveReward` literal in
that range. **Do not implement `/achievement/Reward` expecting it to serve the chests.**

---

## Q4 — What does "cannot receive the reward" mean mechanically?

Answered first because Q2 and Q4 share the same two integers.

### The success criterion, exactly

**[RECOVERED]** `CSRSyncMStage::ReqRewardCB(function<void(int,unsigned char)> const&, int, req, resp)`
(`0xb3c674`):

```c
if (param_2 != 0)                    { cb(-1, 0); return; }        // :463-467  transport error
if (GetResultCode(resp) != 1)        { cb(-1, 0); return; }        // :468-473  non-1 result_code
j = parse(decrypt(resp));
rd = j["ret_data"];                                             // :509-511
if (rd["achievement"] != null) CSRAchieve::ParseAchievementsElement(rd["achievement"]);  // :512-520
area = CSRUserDB::GetCurAreaID();                               // :523
for (i, rw; i < GetRewards().size(); i++) {                     // :526-577
    if (rw[i].achieve_cnt == (int)rd["achieve_cnt"]) {           // :531 + :566
        CSRPlayData::SetAchieveRewardReceived(area, i);         // :570
        found = true; break;
    }
}
…apply gold/free_iap/iap/card/item/supply…
cb(found ? i : -1, supply_flag);                                 // :1256-1263
```

`if (rd["achievement"] != null)` is an **IS-NULL test on nlohmann's `value_t`**, exactly as
`AGENTS.md` §16.2 warns for `/mission/Complete`. **`achievement` must be omitted or JSON
`null` — never `[]`.**

### `AchieveRewardCB(int index, unsigned char supply)` — `0xe985c4`

**[RECOVERED]** `ghidra-chest-01-reward-route.txt:1776-1783`:

```c
if (index == -1) {
    CGMDataMgr::GetLocalizedText(&s);
    Toast(&s, '\0', …);
    return;                                   // NOTHING ELSE HAPPENS
}
```

and on success (`:1809-2210`):

```c
node = this->0x804[index];                    // unordered_map<unsigned, pair<SRREWARD_INFO,uchar>>
node->value.byte = 1;
CSRPopUpGetReward::CREATE_INFO info = { node+0x0c, +0x10, +0x14, +0x18, +0x1c, +0x20,
                                        node->+0x28 ? node->+0x28 : 0,
                                        vector<string> from node+0x2c..+0x30 filtered on *(int*)(e+0xc)!=0 };
auto popup = make_shared<CSRPopUpGetReward>();  popup->Init(&info);
if (this[0x6b4] == 1) popup->SetAutoClose();
CMEventPool<>(popup+0x74) << lambda(supply);  PauseAutoProgress(this);
CSRUIModalHandler::Push(popup, 0);
SetVisible(this->0x780 + index*0x20, 0);   // locked   sprite OFF
SetVisible(this->0x790 + index*0x20, 1);   // opened   sprite ON
SetVisible(this->0x788 + index*0x20, 0);   // anim     OFF
SetVisible(this->0x798 + index*0x20, 0);   // still    OFF
SetVisible(this->0x6a8, 0);                // thumb panel OFF
```

### The four mechanical meanings of "cannot receive"

1. **`/mission/ReqAchieveReward` is never sent at all.**
   `SendRewardRequest` returns without issuing a request when the UI-node tree at
   `this->0x678` is **empty** (`ghidra-chest-01-reward-route.txt:1511-1559` → `LAB_00e9a634`).
   That tree is populated by `ShowReward`'s `lower_bound(1)` inserts
   (`:2407-2423`, `:2473-2489`, `:2926-2942`, `:3004-3020`), which only happen if the
   chest-row view **`NEW/SR_MISSION/2_SR_UI_MS_ST/4_MS_ST_FT`** loaded
   (`CMUIView::LoadView(DAT_00e94414 + 0xe94162)`, `:2382`). **A missing UI record ⇒ zero
   requests; no response shape can fix that.**

2. **The request is sent but the response is rejected.**
   `result_code != 1`, or a transport error ⇒ `cb(-1,0)` ⇒ toast. **Diagnostic: count the
   requests.** One request + toast = a *shape* problem. A burst (the 8× silent retry seen
   with `/mission/Complete`) = a transport / `result_code` problem. `ReqRewardCB` itself
   has no retry loop; repeats come from `CPVHTTPManager::Enqueue`.

3. **`ret_data.achieve_cnt` does not match any `achieve_reward[].achieve_cnt`.**
   ⇒ `SetAchieveRewardReceived` never runs, `found` stays false, `cb(-1, 0)`, toast,
   **and the chest never flips to the opened state.** This is the single most likely cause
   with the current fixture: the request sends
   `target_achieve_cnt = GetRewards()[index].achieve_cnt` (a *reference* value) and the
   handler matches the *response* against the same array. Echo it back verbatim.

4. **`result_code == 1` but `ret_data` is not a JSON object.** The handler dispatches on
   `*ret_data` (`== 1` object, `== 2` array) and takes an error path otherwise
   (`:586-600`, `:604-612`). Send an object, always.

---

## Q2 — What drives the chest sprite state?

### Short answer: **client-side. Not one byte of server data selects the sprite.**

**[RECOVERED]** `CSRSceneMStageMap::SetRewardVisible(int index, REWARD_STATE state)`
(`0xe95eb8`) — `ghidra-chest-01-reward-route.txt:2273-2285`:

```c
CMUpdatable::SetVisible(this->0x780 + index*0x20, state == 0);
CMUpdatable::SetVisible(this->0x790 + index*0x20, state == 2);
CMUpdatable::SetVisible(this->0x788 + index*0x20, state == 1);
CMUpdatable::SetVisible(this->0x798 + index*0x20, state == 1);   // ← SAME state as the previous line
```

Four sprite slots per chest, **stride `0x20`, base `0x780`**, and **two of them share
state `1`**.

### What each slot actually is — **[RECOVERED]**, `ShowReward` `0xe9413c`

| slot | filled by | res-name built | state |
|---|---|---|---|
| `+0x00` | `CMUIView::GetSprite(base + "1")` `:2863-2870` | `MS_RW_<L>1` | 0 |
| `+0x08` | `CMUIView::GetAnimation(base)` `:2943-2951` | `MS_RW_<L>` (**animation**) | **1** |
| `+0x10` | `CMUIView::GetSprite(base + "8")` `:3021-3039` | `MS_RW_<L>8` | 2 |
| `+0x18` | `GetSprite(base + "8")` `:3077-3084` | `MS_RW_<L>8` (**again**) | **1** |

`base = "MS_RW_" + letter`, literals at `0x01d730a0` (`MS_RW_`), `0x01d7309e` (`G`),
`0x01d7309c` (`S`), `0x01d72e40` (`B`), `0x01d6b5ea` (`1`), `0x01d8af1c` (`8`)
(`tools/resolve-literals-offline.py --function e9413c:e9539c`).

### ⇒ THE "BOTH OPEN AND CLOSED" BUG — **explained, and NOT server-fixable**

**When a chest is in state 1 (claimable) the client makes two distinct nodes visible: the
`MS_RW_<L>` *animation* and the `MS_RW_<L>8` *trailing still*.** The animation's own first
frame is the closed chest; the `_8` still is the open chest. Both draw. That is literally
"open and closed at the same time", it is hard-coded in `ShowReward`/`SetRewardVisible`, and
**no response we can send turns it off.**

The only state in which the artifact disappears is **state 2** (`AchieveRewardCB` sets
`+0x00`/`+0x08`/`+0x18` off and `+0x10` on — `:2204-2207`) — i.e. **after a successful
claim**.

Corroboration that this is *by design*, not a fixture artefact: `ShowReward` also renders
`MN_NC`, `PA_THUMB2`, `RE_ITEM`, `UI_MS_ST_BOX%s`, `PA_PRO_BG`, `FMD1`, `reward_show`, and
loads the chest row from `4_MS_ST_FT` — the very layout record `map-backdrop.md` §5.1
already catalogued as declaring all three states in one document.

### Which state each chest lands in — the two integers + one boolean

**[RECOVERED]** `CSRSceneMStageMap::OnInit` (`0xe912ac`) —
`ghidra-chest-02-sources.txt:323-368`:

```c
this->0x76c = CSRGameStage::GetStageCnt(area_id);          // :325   ← S
this->0x770 = 0;                                           // :326
for (link : CSRGameStage::GetStageLinks(area_id, &out)) {  // :328
    int n = CSRPlayData::GetStageAchieveCnt(link->stage_id);// :335
    this->0x770 += n;                                      // :337
    this->0x7e4[ link->serial ] = n;                       // :336-365  std::map<int,int>
}
```

**[RECOVERED]** `ShowReward` `:2536-2572` — the **three chest labels**:

```c
this->0x7ec.push_back( this->0x76c );              // :2539-2548
this->0x7ec.push_back((this->0x76c * 6) / 3 );     // :2552-2562   == 2·S
this->0x7ec.push_back( this->0x76c * 3 );          // :2564-2572   == 3·S
```

⇒ **labels = `[S, 2S, 3S]` where `S = GetStageCnt(area_id)`.** The observed `3 / 6 / 9`
means `S == 3`. `3S == 9` is also the denominator of the star counter, so **`5/9` is
`this->0x770 / (3·this->0x76c)`.**

**[RECOVERED]** `ShowReward` `:3207-3231` — the state decision, per chest `i ∈ {0,1,2}`:

```c
SRREWARD_INFO info = GetRewards()[i];                       // :3183-3205
if (info has any content) {
    bool received = CSRPlayData::IsReceivedAchieveReward(this->0x844 /*area*/, i);  // :3215
    int have = this->0x770;                                 // :3217
    int need = this->0x76c * (i + 1);                        // :3218
    if (received != 1) {
        SetVisible(slot+0x00, have <  need);   // 0  locked     (MS_RW_<L>1)
        SetVisible(slot+0x10, 0);              // 2  opened
        SetVisible(slot+0x08, need <= have);   // 1  claimable  (MS_RW_<L>  anim)
        SetVisible(slot+0x18, need <= have);   // 1  claimable  (MS_RW_<L>8 still)   ← BOTH
    } else {
        SetVisible(slot+0x00, 0);
        SetVisible(slot+0x10, 1);              // 2  opened     (MS_RW_<L>8)
        SetVisible(slot+0x08, 0);
        SetVisible(slot+0x18, 0);
    }
    this->0x804[i] = { info, (uchar)(received == 1) };       // :3232-3247
}
```

`[RECOVERED]` `SendRewardRequest` `:1572-1574` gates the actual request on the *same*
inequality: `if (this->0x770 < this->0x76c * (i+1)) → next index`.

### Arithmetic for the observed screen (`S=3`, `this->0x770 = 5`)

| chest | `need = S·(i+1)` | `5 >= need`? | state drawn | sprites |
|---|---|---|---|---|
| 0 | 3 | **yes** | **1 claimable** | `MS_RW_<L>` **anim** + `MS_RW_<L>8` **still** |
| 1 | 6 | no | 0 locked | `MS_RW_<L>1` |
| 2 | 9 | no | 0 locked | `MS_RW_<L>1` |

⇒ **Exactly one chest should be half-open.** The user reads the row as inconsistent, and
chest 0 is the one that cannot be claimed. **Both reports have one cause: `this->0x770`.**

### `IsReceivedAchieveReward` — where the boolean comes from

**[RECOVERED]** `CSRPlayData::IsReceivedAchieveReward(const string& area, int i)` (`0xb6d14c`,
`ghidra-chest-02-sources.txt:436-481`):

```c
std::map<std::string, CSRPlayData::AREA_ACHIEVE_INFO> area_achieve;   // CSRPlayData + 0x288
if (area_achieve.count(area) == 0) return 0;
return area_achieve[area][ i + 0x28 ];        // a BYTE array inside AREA_ACHIEVE_INFO
```

`CSRPlayData::SetAchieveRewardReceived(area, i)` (`0xb6d0fc`, `:484-514`):
`area_achieve[area]` (emplace, does **not** clobber an existing key) then
`*(uint8*)(value + i + 0x28) = 1`.

**⇒ the container is `area_achieve`, keyed by area id, holding a byte array indexed by chest
index. The JSON key `area_achieve` is at `0x01d7c017`.** `tools/resolve-literals-offline.py
--find-string area_achieve` returns **0 refs**, i.e. it is read through a DAT-mediated
access the literal-pool scanner cannot see — same signature as `achieve_cnt`
(`0x01d7773c`), which *is* provably read in `ReqRewardCB` `:531`. Marked
**[INFERRED]** that `/lobby/Enter`'s `area_achieve` populates `CSRPlayData+0x288`;
**[UNKNOWN]** which sub-keys name the byte array. Publishing `"area_achieve": {}` is the
safe minimum (see §Spec).

### `IsOpened(int)` — a different, throw-on-miss map

**[RECOVERED]** `CSRSceneMStageMap::IsOpened(int) const` (`0xe9857c`,
`ghidra-chest-01-reward-route.txt:2239-2270`):

```c
if (i == 1) return true;                       // index 1 hard-coded true
… std::map<int,int> at this+0x7e4 …           // the per-chapter totals from OnInit
return 0 < node->value;
FUN_006d8570(DAT_00e985c0 + 0xe985bc);          // 'map::at:  key not found'
```

`this->0x7e4` is keyed by the stage link's leading int (`OnInit :338-353`), i.e. the
`serial` field of `stage[]`. **`IsOpened` throws if a serial is absent.**
[INFERRED, actionable] publish `serial: 0,1,2` on the three links so the key domain is
complete.

### `ACHIEVE_REWARD` layout — resolved, double-corroborated

**[RECOVERED]** `CSRGameStage::GetRewards(area)` (`0xa29c34`) walks
`CSRGameStage+0x24 … +0x28`, **stride `0x34` (52 bytes)**, filtering on the string at
`+0x04`. `ShowReward :3183-3205` reads `+0x04`/`+0x08` (the NDK *short-string* size/flag
bytes — this is why they look like two separate strings), `+0x1c` and `+0x28` as
`vector<pair<string,uint>>`.

```c
struct CSRGameStage::ACHIEVE_REWARD {   // 0x34 = 52 bytes
    int32_t                     achieve_cnt;   // +0x00   ← RequestReward sends THIS as target_achieve_cnt
    std::string                 area_id;       // +0x04   ← GetRewards filters on THIS
    vector<pair<string,uint32>> item_list;     // +0x1c
    vector<pair<string,uint32>> card_list;     // +0x28
};
```

`CSRGameStage::STAGE_LINK` is **0x1c (28 bytes) = `{int32 serial; std::string id;}`**
(stride proven at `ghidra-chest-03-getters.txt:60` `iVar4 = iVar4 + 0x1c`).

### `SetArea` keys — **[RECOVERED]**, `0xa28108`

`ret_data` → `area[]`; per area: `id, type, serial, level_limit, title, desc, dialog_id,
resource_id, explore_id`, then `stage[]` (each `{area_id, stage_id, serial}`) and
`achieve_reward[]` (each `{area_id, achieve_cnt, gold, free_iap, iap, item_list, card_list}`).
All resolved from real `operator[]` sites at `0xa28152 … 0xa28c5c`
(`analysis/ghidra-chest-02-sources.txt:1669-1818`, `:2052-2084`).

### `[UNKNOWN-4]` — which JSON key fills `STAGE_LINK`'s string

`GetStageCnt(x)` and `GetStageLinks(x, &out)` both **compare the link's single string
against their argument** (`ghidra-chest-03-getters.txt:20-59` and `:96-122`). But `OnInit`
feeds the *same* string to `CSRPlayData::GetStageAchieveCnt`, which is keyed in
`CSRPlayData+0x27c` (`std::map<std::string, STAGE_INFO>`, `ghidra-chest-02-sources.txt:543`)
— the **stage** map. Both readings cannot be literally true of one field.

Observed `S == 3` and `n_01` has exactly three `stage[]` links (`N001..N003`,
`AGENTS.md` §11), which favours *"the link string is the `area_id`"*, i.e. `GetStageCnt` =
**number of `stage[]` links in the area**. **[INFERRED]**, one probe to settle it:
decompile `CSRGameStage::CreateArea` (`0xe91f0c`) or the `stage[]` push at
`ghidra-chest-02-sources.txt:1874-1888` and see whether `puVar39`'s string comes from the
`area_id` or the `stage_id` `from_json`.

**This does not block the fix** — whichever key it is, the server publishes all three, and
the arithmetic above is unaffected.

---

## Q3 — What renders inside the popup?

**No route is involved. The popup is fed entirely by `/reference/GetArea`'s
`achieve_reward[]`.**

### `PopUpClearReward(const string& a, const string& b)` — `0xe964e0`

**[RECOVERED]** `ghidra-chest-01-reward-route.txt:3889-3954`:

```c
if (a.empty() && b.empty()) {
    RMTrace(2, "[ERR] [%s] " + "ClearRewardInfo Not Found");   // :3899-3918
    return;                                                   // nothing shown
}
if (this->0x6a8 == 0) return;                                 // :3928
auto p = make_shared<CSRPopUpMStageRewardShow>();
CSRPopUpMStageRewardShow::SetData(p, a, b);                  // :3931
CSRScene::InitScene(p, a + b + "CSRPopUpMStageRewardShow", 0);// :3933-3944
PauseAutoProgress(this);
if (this[0x6b4] == 1) p->SetAutoClose();
```

`CSRPopUpMStageRewardShow::SetData` (`0xd1421a`) just copies `a → this+0xb4`,
`b → this+0xc0` — `ghidra-chest-02-sources.txt:392-433`. **It fetches nothing.**

`"CSRPopUpMStageRewardShow"` is 24 chars (`0x18`, `0x01d8af55`), appended to `a+b`. So the
scene instance name is **`a + b + "CSRPopUpMStageRewardShow"`**.

⇒ **[INFERRED] the empty popup is the empty-string guard.** If `a` and `b` (the two strings
`ShowReward` harvested from the reward record's vectors) are both empty for the third
chest's reward, the popup is skipped entirely and `RMTrace(2, …)` is the only trace.
**Note the channel: `RMTrace`, level 2 — not `[ERR] [RES]`.** That is why
`map-backdrop.md` §5.3 could not find `'ClearRewardInfo Not Found'` in `r015/logcat-all.txt`;
grep the run for **`RMTrace` / trace level 2**, not for `[ERR] [RES]`.

### `SetClearRewardThumb(uchar flag, const string& a, const string& b)` — `0xe95f00`

**[RECOVERED]** `ghidra-chest-01-reward-route.txt:3549-3654`:

```c
if (this->0x678 empty || first_key != 1 || this->0x6a8 == 0) return;   // :3562-3563
SetVisible(this->0x6a8, 0);
if (a.empty() && b.empty()) { RMTrace(2, "SetClearRewardThumb Not Found"); return; }  // :3575-3597
if (flag == 1) return;                                                  // :3601
SetVisible(this->0x6a8, 1);
if (!b.empty()) {
    auto th = make_shared<CSRItemThumb>();
    CSRItemThumb::Init(th, &CREATE_INFO{ ref = b, … });
    CSRItemThumb::SetContents(th, 0x21);
    CSRItemThumb::SetAlign(th, 2, 2);
    CSRItemThumb::SetScl(th, {0.9f, 0.9f});
    CSRItemThumb::SetDetailOpen(th, 0);
    AttachChild(this->0x6a8, "RE_ITEM_THUMB", th);
}
```

UI nodes: `RE_ITEM_THUMB` (`0x01d7c9e2`) and `RE_HUNT_THUMB` (`0x01d8b028`).

⇒ **The popup body is one `CSRItemThumb` whose ref string is `b`, an item id straight out
of the reward record.** No item ⇒ no thumb ⇒ an empty white circle. **If the owning package
for `MS_RW_*` is still unknown (`map-backdrop.md` §5.2), the circle will be blank even with
perfect data.** Two independent gaps stack here.

### The post-claim popup (`CSRPopUpGetReward`) is different and is well fed

`AchieveRewardCB` builds `CSRPopUpGetReward::CREATE_INFO` from
`SRREWARD_INFO` (`0x44` bytes, node `+0x0c … +0x2c`, read at `:1864-1946`) — again pure
reference data, again no route.

---

## Per-route spec for the server agent

### 1. `POST /mission/ReqAchieveReward` — **implement this one**

**Request** — URL-encoded form, exactly 7 keys:

```
app_code=_SR  app_ver=2801  market=<int>  pvid=<int>  otp=<string>
area_id=<area id>            # e.g. "n_01"
target_achieve_cnt=<int>     # = this area's achieve_reward[index].achieve_cnt, verbatim
```

**Response** — encrypted JSON body. `result_code` **must** be `1`.

```jsonc
{
  "result_code": 1,
  "ret_data": {                       // MUST be a JSON object (client tests value_t == 1)
    "achieve_cnt": 3,                 // MUST equal one of achieve_reward[].achieve_cnt
                                      // number. THIS is what flips the chest to "opened".
    "gold":     { "prev": 0, "cur": 0 },   // object; applied only if prev != 0
    "free_iap": { "cur": 0 },             // object; applied only if CPVDataMgr+0x58/0x5c != 0
    "iap":      { "cur": 0 },             // object; same gate
    "card":     [],                      // ARRAY of card-instance objects (ParseCardInst each)
    "item":     [],                      // ARRAY of { ref_id: string, inst_id: int, qty: number }
    "supply":   0,                       // number; nonzero becomes the callback's 2nd arg
    "achievement": null                  // OMIT or null. NEVER [] (IS-NULL test, AGENTS §16.2)
  }
}
```

Rules, each traced to a line in `ghidra-chest-01-reward-route.txt`:

| rule | why | line |
|---|---|---|
| `ret_data` is an object | `if (*rd == 1) … else if (*rd == 2) … else error` | `:586-612` |
| `achieve_cnt` present and matching | `SetAchieveRewardReceived` is the only thing that persists the claim; a miss ⇒ `cb(-1,0)` ⇒ toast | `:531,:566,:570,:1259` |
| `achievement` omitted / `null` | `if (*v != (json)0x0) ParseAchievementsElement` — a `value_t` IS-NULL test, and that function is a `/dailyquest/GetInstList` **request builder** | `:517-520` |
| `gold.prev` non-zero for the credit to land | `switch(*prev){…}` guards the `cur` read | `:629-717` |
| `card` / `item` are arrays | both are iterated with `iter_impl::operator!=` | `:880-1020`, `:1085-1235` |
| `item[]` elements are objects with `ref_id`, `inst_id`, `qty` | three adjacent literal slots `0xb3d0a4/0xa8/0xac` resolve to `0x01d6edf2 / 0x01d6eec9 / 0x01d6edf9` | `:1081-1149` |

**Minimum non-crashing fixture** (safe, shows nothing, still claims the chest):

```jsonc
{ "result_code": 1, "ret_data": { "achieve_cnt": <echo request.target_achieve_cnt> } }
```

`ret_data` object with a single numeric `achieve_cnt` walks every guard without entering a
branch: no `achievement`, no `gold` (the `find<char[5]>("gold")` miss jumps past
`:618`), no `card`/`item` loops, `supply` null ⇒ 0. **This is the smallest shape that makes
the chest flip to the opened sprite** — i.e. it fixes both "cannot receive" *and* the
double-sprite artifact.

**Server-side bookkeeping** — on `result_code == 1`, append
`(area_id, target_achieve_cnt)` to that area's claimed set, and **clear it when
`/lobby/Enter` is generated**, so `area_achieve` and the client agree.

### 2. `/lobby/Enter` — the two fields that decide the whole screen

**[RECOVERED]** containers:

* `CSRPlayData+0x27c` — `std::map<std::string, STAGE_INFO>`, keyed by **stage id**. Feeds
  `GetStageAchieveCnt` ⇒ **`this->0x770`, the star-counter numerator.** It returns `0`
  safely when the key is absent (`count_unique` guard, no throw).
* `CSRPlayData+0x288` — `std::map<std::string, AREA_ACHIEVE_INFO>`, keyed by **area id**,
  value carries a byte array at `+0x28` indexed by chest index. Feeds
  `IsReceivedAchieveReward` ⇒ **which chest is "opened" vs "claimable" vs "locked"**.

**[INFERRED]** these are the JSON keys `stage[]` and `area_achieve` (`0x01d7c017`).
**[UNKNOWN]** the key names inside `AREA_ACHIEVE_INFO` that name the byte array, and
whether `STAGE_INFO`'s count is a plain int or a string (its `+0x1c` field is a
`std::string` and `GetStageAchieveCnt` copies it into a temporary — likely a serialised
count). Minimum safe fixture: `"area_achieve": {}` and a `stage[]` with a plain integer per
entry.

### 3. `/reference/GetArea` — `achieve_reward[]` drives the popup, and `stage[]` drives `S`

Per `SetArea` (`0xa28108`, keys resolved above):

```jsonc
{ "id": "n_01", "serial": 0, "level_limit": 1, "title": "Snowfield", "desc": "…",
  "dialog_id": "…", "resource_id": "MAP_ZONE_1", "explore_id": "…",
  "stage": [ { "area_id":"n_01", "stage_id":"N001", "serial":0 },
             { "area_id":"n_01", "stage_id":"N002", "serial":1 },
             { "area_id":"n_01", "stage_id":"N003", "serial":2 } ],
  "achieve_reward": [
    { "area_id":"n_01", "achieve_cnt":3, "gold":100, "free_iap":0, "iap":0,
      "item_list":[{"id":"<item ref id>","qty":1}], "card_list":[] },
    { "area_id":"n_01", "achieve_cnt":6, … }, { "area_id":"n_01", "achieve_cnt":9, … }
  ] }
```

**Consistency contract the server must honour** — this is the whole bug in one sentence:

> `achieve_reward[i].achieve_cnt` **must** equal `GetStageCnt(area) · (i+1)`, and
> `Σ_lobby/Enter stage[].achieve` **must** be a real count in `[0, 3·GetStageCnt(area)]`.

If the labels say `3 / 6 / 9` and the numerator says `5`, chest 0 is claimable and the
claim can never be acknowledged unless `ret_data.achieve_cnt` echoes `3`.

Also publish **`serial: 0,1,2`** on the links so `IsOpened`'s `map::at` (`0x01d694f3`,
`map::at:  key not found`) cannot throw.

**Minimum non-crashing fixture:** `"stage": [{"area_id":"n_01","stage_id":"N001","serial":0}]`,
`"achieve_reward": [{"area_id":"n_01","achieve_cnt":1,"gold":0,"item_list":[]}]`.

### 4. Routes that are **NOT** on this path — do not spend time here

`/explore/Reward` (`0x01d72a8e`), `/achievement/Reward` (`0x01d6ef28`),
`/random_box/Reward`, `/random_box/RewardList`, `/shop/RewardGachaMileage`,
`/mirage/Reward`, `/episode/Reward`, `/shop/IAPAchieveReward` (`0x01d902f3`).
`/achievement/Reward`'s only builder is `CSRAchieve::RequestAchievementsReward`
(`0x0084ad98`), used by `CSRSceneAchieve::RequestAchievementReward` (`0x00df76e0`) and
`CSRTabAchieve::RequestAchievementReward` (`0x00fa2240`) — both in the **Achievement
scene**, and its callback takes `CSRAchieve::INFO`, not the expedition `SRREWARD_INFO`.

### 5. `/mission/Complete` — keep `achievement` omitted

Unchanged from `AGENTS.md` §16.2, and this report **independently confirms** the mechanism:
`ReqRewardCB :517-520` uses the same `if (*json != null)` guard around the same
`CSRAchieve::ParseAchievementsElement`.

---

## Answers in one line each

* **Q1** — `POST /mission/ReqAchieveReward`, form-encoded, 7 keys: `app_code, app_ver,
  market, pvid, otp, area_id, target_achieve_cnt`. Not `CSRAchieve::GetDataList` /
  `GoShortcut` — those are the daily-quest scene.
* **Q2** — **Client-side.** `SetRewardVisible(index, state)` picks among 4 sprites per
  chest; `state` = f(`this->0x76c` = `GetStageCnt(area)`, `this->0x770` =
  `Σ GetStageAchieveCnt(link)`, `IsReceivedAchieveReward(area, i)`).
  `this->0x76c` and `this->0x770` come from `/reference/GetArea`'s `stage[]` and
  `/lobby/Enter`'s `stage[]`. **The "open and closed at once" is states 1 drawing both
  `MS_RW_<L>` and `MS_RW_<L>8` — inherent, not data-driven.**
* **Q3** — **Reference data, no route.** `CSRPopUpMStageRewardShow::SetData(a,b)` +
  `CSRScene::InitScene(a + b + "CSRPopUpMStageRewardShow")`, plus one `CSRItemThumb` whose
  ref is a string from `achieve_reward[]`. Empty ⇒ `RMTrace(2, …)`, not an `[ERR] [RES]`
  line. If `MS_RW_*`'s owning package stays unknown, the circle stays blank anyway.
* **Q4** — "Cannot receive" = `AchieveRewardCB(-1, …)` ⇒ `Toast()` and nothing else.
  `-1` happens when the request was never sent (empty UI-node tree at `this->0x678` ⇒ the
  `4_MS_ST_FT` layout did not load), or `result_code != 1` / transport error, or
  **`ret_data.achieve_cnt` did not match any `achieve_reward[].achieve_cnt`**. No retry loop
  in `ReqRewardCB` — repeats mean `Enqueue` saw a transport failure, not a shape problem.

## Honest limits

* `[UNKNOWN-4]` which of `area_id` / `stage_id` fills `STAGE_LINK`'s one string (§Q2).
  Affects nothing the server ships; both keys are published.
* `[UNKNOWN]` the JSON sub-keys of `AREA_ACHIEVE_INFO` that name the received-flag byte
  array, and whether `STAGE_INFO`'s achieve count is an int or a serialised string. One
  `CSRPlayData` lobby-enter decompile would settle both.
* `[INFERRED]` that `/lobby/Enter`'s `stage[]` / `area_achieve` are the two `CSRPlayData`
  maps at `+0x27c` / `+0x288`. Proven for the maps; the JSON key names are not, and the
  literal-pool scanner reports **0 refs** for `area_achieve`.
* The `MS_RW_*` owning package is still **[UNKNOWN]** (inherited from
  `map-backdrop.md` §5.2). Not a server-route problem.
* **No claim is made that any of this has been seen on device.** Every statement above is
  from static analysis of `libnative_core.so`; the `S=3 / 0x770=5` arithmetic is the only
  thing tied to a screenshot, and it is labelled as such.