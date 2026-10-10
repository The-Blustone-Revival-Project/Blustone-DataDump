# Server route triage — the mocked routes the client actually calls

Written by the **server agent**, 2026-10-02. Read-only research over
`analysis/native-evidence.tsv`, `analysis/native-all-strings.tsv`,
`analysis/ghidra-*.txt`, `analysis/native-*.txt`, `analysis/native-target-stage-cb.txt`
and `server-ts/logs/server.stdout.log`. No Ghidra, no adb, no server restart.

---

## 0. How the list was reconstructed

The collector's event ring no longer holds the wire events (19 842 events
received, ring capped at 2 000 and now entirely `artifact_uploaded` /
`heartbeat` / `touch` noise — `GET http://127.0.0.1:8099/v1/stats`). The
durable `events.ndjson` is ~1.9 GB.

The authoritative source used instead is **`server-ts/logs/server.stdout.log`**,
which `tools/start-server.ps1` redirects to. Every game response goes through
`response-dispatch <iso> <route>` (`server-ts/src/server.ts:192`). The file
currently covers two full sessions (each route appears twice), i.e. exactly the
run analysed in `analysis/testing/report-009.md` plus one more.

Method: extract the `response-dispatch` routes, replay each one through
`createApp()` on an ephemeral port, and classify the response by whether
`ret_data.mock === true`. Script was a throwaway (`server-ts/triage-probe.ts`),
deleted afterwards; nothing was left behind.

```
75 unique routes requested by the client this session
47 returned mock:true          <- report-009 said 45; see note below
28 returned real data
```

**On the 45 vs 47 discrepancy.** report-009 counted `/mirage/GetInfo` and the
relation profile route; `/pv_tracker/MarkAP` (called 8× per session, the most
frequently requested route in the whole session) is easy to miss because it is
telemetry-shaped. Both are genuinely `mock:true`. The set is 47.

**After this session's changes: 44 mocked, 31 real.**

---

## 1. The finding that matters more than the triage

**Reading the existing dumps turned up a defect on the battle path, and it
plausibly explains the whole five-empty-strings invariant.**

### 1.1 `AddStageMonster` reads `_id`, not `wave_list`

`analysis/ghidra-wave-keys.txt` resolves five literals inside
`CSRGameMob::AddStageMonster` (0x00a0d194):

```
ldr@00a0d1b0 slot=0xa0d4f4 -> 0x1d76bd1  "_id"      <-- FIRST key read, iterated
ldr@00a0d2fa slot=0xa0d500 -> 0x1d6edf2  "ref_id"
ldr@00a0d33e slot=0xa0d504 -> 0x1d658fa  "group"
ldr@00a0d390 slot=0xa0d508 -> 0x1d76bdf  "next_spawn_ms"
ldr@00a0d50c slot=0xa0d874 -> 0x1d76bed  "show_thumbnail"
```

The decompile body (`analysis/native-monster-stage.txt`, function at line 5156)
is unambiguous about the first one:

```c
pcStack_70 = json::operator[](param_3, <0x1d76bd1>);   // "_id"
while (true) { ... build STAGE_MONSTER from ref_id/group/next_spawn_ms ... }
/* then, after the loop */
pcStack_44 = json::operator[](param_3, <0x1d76bed>);   // "show_thumbnail"
...
basic_string(uStack_d0, param_2);                      // param_2 == stage id
vector<vector<STAGE_MONSTER>>(puStack_c4, uStack_60);
vector<string>(pbStack_b8, uStack_58 + 4);
m_mStageMonsterLink.emplace(param_1 + 0xc, uStack_d0 /* stage id */);
```

`param_2` is the stage id and `param_1 + 0xc` is the map, so
`AddStageMonster(stageId, record)` files into
`std::map<string, CSRGameMob::STAGE_MONSTER_LINK> m_mStageMonsterLink`.

Both literals exist in `.rodata` — `_id` at `0x1d76bd1` and `wave_list` at
`0x1d76bd5`, four bytes apart, i.e. field names of one record. But
`AddStageMonster` reads `_id`. **The replica only ever sent `wave_list`.**
`json["_id"]` on a record without it is `null`, and iterating `null` in
nlohmann yields nothing, so **no wave was ever registered** into
`m_mStageMonsterLink`.

### 1.2 Why that produces exactly five empty strings

```
GetTargetStageMonster  ->  AddStageMonster  ->  m_mStageMonsterLink is EMPTY
                                                     |
CSRGameBase::RequestMonsterRef (0x009c9a2c)         v
CSRSceneStageConfirm::RequestMonsterRef (0x00e7cf74)   <- Prepare for Battle
   serialises a FIXED-SIZE enemy formation of 5 slots
   -> ["", "", "", "", ""]
        |
        v
/reference/GetMonster {"list":"[\"\",\"\",\"\",\"\",\"\"]"}
   -> server replies {M001:..., "001":...}      <- neither key is ""
        |
        v
MakeCamp -> MakeActor -> MakeBackEndActor
   -> CSRGameMob::GetMonsterData("")   (0x00a0b43c)
      std::map<string,INFO>::find("") misses
      -> ASSERT SRGameMob.cpp:38  -> deref end() -> SIGSEGV
```

This is the first coherent explanation of the
`analysis/research/ORCHESTRATOR-arity-constraint.md` invariant that does **not**
require the size-5 array to be an unexplained native constant. It also explains
why the Prepare screen shows `Opponent Teammates 1` while the client asks for
five monsters: the UI reads a different, resolved count.

**Fix shipped:** `starterStageMonsters` now sends the wave array under **both**
`_id` and `wave_list`. `_id` is the only reader of that record (the sole caller
is `ReqTargetStageMonsterCB`, `analysis/native-target-stage-cb.txt`), so adding
it cannot collide with a reader expecting a scalar, and it is non-regressive
under either nesting reading.

**Residual uncertainty, stated plainly:** whether `_id` is a flat array of waves
or an array of wave *groups*. `STAGE_MONSTER_LINK`'s second member is a
`vector<vector<CSRGameMob::STAGE_MONSTER>>` (`__push_back_slow_path<const
vector<STAGE_MONSTER>&>`, 0x00a0e4ac) and `show_thumbnail` is iterated
alongside it, which is consistent with grouping. The flat form was sent because
under the grouped reading it simply registers nothing — exactly today's
behaviour — so the change cannot make anything worse.

### 1.3 Companion hedge on `/reference/GetMonster`

`/reference/GetMonster` now also publishes the monster under the key `""`.

This is not a shape guess. `CSRGameMob::GetMonsterData` (0x00a0b43c) is a
`std::map<string, INFO>::find` keyed by the id the client sends, and the client
sends five **empty strings**, byte-identically, in every run on record. If the
`_id` fix in §1.1 does not take, `GetMonsterData("")` still resolves and the
battle does not die on a null `INFO`. `CSRSyncMStage::ReqMonsterCB` (0x00b4514c)
iterates `ret_data` and calls `AddMonster` on each value
(`analysis/native-reqmonster.txt:82`), so an extra key is an extra monster in
the table and nothing else.

### 1.4 The one unresolved question in the monster container — for Ghidra

`CSRSyncMStage::ReqMonsterCB` iterates `ret_data` and calls `iter_impl::operator*()`
on each element — **it never calls `iteration_proxy_value::key()`**. Contrast
`ReqTargetStageMonsterCB` two functions later (`0x00b4606c`), which *does* call
`key()` and passes it to `AddStageMonster`. And `AddMonster` itself
(0x00a0b540) resolves **no id-like key at all** (60 literals, all of them
stat/skill/attribute fields — `analysis/ghidra-mob-keys.txt`).

So for `/reference/GetMonster` the identity has to come from somewhere neither
dump shows. Until that is settled the container kind (array vs object) and the
key derivation are both **UNKNOWN**, and the replica's two-plus-one-key hedge is
a hedge, not a reconstruction. Highest-value single decompile in the monster
area: `AddMonster`'s tail, looking for the
`__emplace_unique_key_args<string, pair<string, CSRGameMob::INFO>>` call at
0x00a0df1c and what string it is handed.

---

## 2. The other battle-path defect: `ParseUserDatailInfo` is probably fed by `/lobby/Enter`

`CSRSyncGlobal::ParseUserDatailInfo` (0x00f6e240) reads `ret_data` and then 41
keys off it (`analysis/ghidra-userdetail.txt`, all 41 resolved):

```
pvid group_exp vip_exp league_level rating_point awake
inst_id_leader ref_id_leader rank_leader rank_up_cnt_leader awk_step_leader
overcome_cnt_leader awk_overcome_leader exp_leader skin_ref_id_leader
skill_1_level_leader .. skill_5_level_leader
inst_id_  ref_id_  rank_  rank_up_cnt_  awk_step_  overcome_cnt_
awk_overcome_  exp_  skin_ref_id_  skill_1_level_ .. skill_5_level_
stage_id prev_rank win_message lose_message
```

The numbered suffixes are built by string concatenation, so this is a loop over
slot indices. `SetRefID` is called from exactly two sites inside it —
**0x00f6e62e** (numbered loop) and **0x00f6eda2** (`_leader`)
(`analysis/ghidra-setrefid-callers.txt`) — so `_leader` + four numbered slots =
**five `SetRefID` calls = the five `SRCard.cpp:731` assertions**, exactly.

report-009 §7 measured this key set on `/lobby/Enter`'s response and found
**every one of the card keys absent**, while `/relation/GetTargetUserInfo`
already carried them and still produced a byte-identical `list`. So
`ParseUserDatailInfo` is almost certainly dispatched with `/lobby/Enter`, not
with the relation route.

**Fix shipped:** the full key set is now published at the top level of
`/lobby/Enter`'s `ret_data`, alongside the existing `user` / `deck` objects,
plus `pvid` and `nick_name`. Purely additive — a parser not dispatched with
this response ignores the keys, and the parser demonstrably tolerates missing
keys (an absent `ref_id_<n>` yields `""` rather than throwing).

---

## 3. The full list of 47 mocked routes, ranked

Ranking key: **(a)** likelihood of affecting the battle scene opening,
**(b)** confidence of a recoverable shape from on-disk evidence.

Legend for *Shape*: `RECOVERED` = the key set is resolved from native literals
on disk. `UNKNOWN` = the route's parser has no resolved key list on disk.

### Tier 1 — battle path, evidence in hand → **implemented**

| # | route | shape | action |
|---|---|---|---|
| 1 | `/reference/GetTargetStageMonster` | **RECOVERED** `AddStageMonster` 0xa0d194 → `_id` array + `ref_id`/`group`/`next_spawn_ms`; `ReqTargetStageMonsterCB` 0xb4606c → `ret_data` is an object keyed by stage id | added `_id` (§1.1) |
| 2 | `/reference/GetMonster` | container **UNKNOWN**; element **RECOVERED** `AddMonster` 0xa0b540 (60 keys) | added `""` key (§1.3) |
| 3 | `/lobby/Enter` | **RECOVERED** `ParseUserDatailInfo` 0xf6e240 (41 keys) | publish the key set (§2) |
| 4 | `/relation/GetTargetUserInfo` | **RECOVERED**, same parser | `pvid` echoes the request, `nick_name` is the account nickname (Task 3) |

`/reference/GetStageMonster`, `/reference/GetCard`, `/reference/GetStage`,
`/reference/GetArea`, `/lobby/GetCardInven`, `/lobby/GetItemInven`,
`/mission/Start` were already real and are unchanged except for the monster
change above.

### Tier 2 — card/gem reference tables, container type recovered → **implemented as empty**

| # | route | evidence | action |
|---|---|---|---|
| 5 | `/reference/GetCardChain` | `CSRSyncRef::ReqCardChainCB` 0x00f84ce4 → `CSRCardInfoContainer::SetCardChain` 0x0087e110: `ret_data["r"+gen] → target_rank, title, desc, related_list[] → effect → atk, def, hp` | `envelope({})` |
| 6 | `/reference/GetCardRankUp` | `ReqCardRankUpCB` 0x00f84ca0 → `SetCardRankUp` 0x0087ec9c: `ret_data["e"+gen] → src_cnt, stat_bonus` | `envelope({})` |
| 7 | `/reference/GetCardEnhancePrice` | `ReqCardEnhancePriceCB` 0x00f84cc2 → `SetCardEnhancePrice` 0x0087f048: `ret_data[gen] → level, rank` | `envelope({})` |

All three index `ret_data` with a **generated** key (a one-character literal
concatenated with something), which proves the container is an object. The
index range is not knowable from outside, so they stay empty — but an empty
object is the truthful answer and is strictly safer than the previous mock,
because every key the parser can ask for now resolves to `null` instead of to
`mock` / `route` / `request_keys`.

### Tier 3 — battle-adjacent, parser located but keys **UNKNOWN** → left mocked

| # | route | parser to decompile | battle relevance |
|---|---|---|---|
| 8 | `/lobby/GetSkinInst` | `CSRInstanceSync::ReqSkinInstCB` 0x00ae62ac (thunk 0x002699e3) → `CSRSkin::ParseInstanceDefaultSkin` **0x00f29d70** | **high** — `MakeStageInst` calls `CSRSkin::FindWornSkinByCardRefId` right after `SetRefID` |
| 9 | `/reference/GetSkinRef` | `CSRSyncRef::ReqSkinRefCB` 0x00f85070 → `CSRSkin::ParseReferenceDefaultSkin` **0x00f29338** | high — the table `FindWornSkinByCardRefId` searches |
| 10 | `/reference/GetItem` | `CSRSyncRef::ReqItemCB` 0x00f83a14 (thunk 0x003621ac); `CSRInstanceSync::ReqItemCB` 0x00ae6080 | medium |
| 11 | `/reference/GetNpc` | `CSRSyncRef::ReqNPCCB` 0x00f84d28 | medium — `SetRefID` is called from `SetEnemy`/`SetAlly`, not NPC; but NPC names show on the prep screen |
| 12 | `/reference/GetDialog` | `CSRSyncRef::ReqDialogCB` 0x00f84c36 | medium — mission story |
| 13 | `/reference/GetScenario` | `CSRSyncRef::ReqScenarioCB` 0x00f84c58; `CSRSyncMStage::ReqScenarioReadCB` 0x00b3f900 | medium |
| 14 | `/reference/GetGem` | `CSRSyncRef::ReqGemCB` 0x00f84e54 | medium — socketed gems on battle cards |
| 15 | `/reference/GetCardOvercome` | `ReqOvercomeCB` 0x00f84de6 → `SetCardOvercome` 0x00ae9ef0 (resolves only warn strings, so a helper does the reading) | low |
| 16 | `/reference/GetCardAwaken` | `ReqAwakeRefCB` 0x00f850a4 → `SetCardAwake` 0x00aea0e4 (same situation) | low |
| 17 | `/reference/GetAbyss`, `/lobby/GetAbyss` | `CSRSyncRef::ReqAbyssCB` 0x00f84dc0 | low (separate mode) |
| 18 | `/reference/GetCardEquipmentLevelUpPrice` | `ReqEquipLevelUpPriceCB` 0x00f84e08 | low |
| 19 | `/reference/GetCardEquipmentRankUpPrice` | `ReqEquipRankUpPriceCB` 0x00f84e2e | low |

**If exactly one more decompile is affordable, take #8 (`CSRSkin::ParseInstanceDefaultSkin`,
0x00f29d70).** It is the only unresolved parser on the battle path, it is
already named, and an empty skin list is the semantically correct answer for a
fresh account — so a resolved shape here is close to free.

### Tier 4 — economy / gacha / guild / fishing / IAP, no battle relevance → left mocked

All **UNKNOWN**. None of these is on the path from `/mission/Start` to the
battle scene, and none is worth a wrong-shape risk.

| route | parser if known | family |
|---|---|---|
| `/reference/GetGemCombinationEffect` | `ReqGemCombiEffectCB` 0x00f84e76 | gem |
| `/reference/GetGemSellPrice` | `ReqGemSellPriceCB` 0x00f84e98 | gem |
| `/reference/GetGemLevelUpPrice` | `ReqGemLevelUpPriceCB` 0x00f84eba | gem |
| `/reference/GetGemDisassemblePrice` | `ReqGemDisassemblePriceCB` 0x00f84edc | gem |
| `/reference/GetPaidGemGacha` | `ReqGemGachaBasicCB` 0x00f84efe | gacha |
| `/reference/GetMileageGemGacha` | `ReqGemGachaMileageCB` 0x00f84f22 | gacha |
| `/reference/GetDailyFreeGemGacha` | `ReqGemGachaOnedayFreeCB` 0x00f84f46 | gacha |
| `/reference/GetShop` | `CSRSyncRef::ReqShopCB` 0x00f84d06 | shop |
| `/reference/GetGacha` | `CSRSyncRef::ReqGachaCB` 0x00f84d4e | gacha |
| `/reference/GetGuildPrices` | `ReqGuildPriceForActionCB` 0x00f84f6c | guild |
| `/reference/GetGuildContributionReward` | `ReqGuildContributionRewardCB` 0x00f84fa0 | guild |
| `/reference/GetGuildContributionPoints` | `ReqGuildContributionPointsCB` 0x00f84fd4 | guild |
| `/reference/GetGuildLevelBenefits` | `ReqGuildLevelBenefitsCB` 0x00f85008 | guild |
| `/reference/GetGuildLevelBenefitsStr` | `ReqGuildLevelBenefitsStrCB` 0x00f8503c | guild |
| `/lobby/GetGuildInfo` | no `*CB` symbol retained | guild |
| `/lobby/GetGachaMileage` | `CSRInstanceSync::ReqGachaMileageCB` 0x00ae6178 | gacha |
| `/lobby/GetGemGachaInfo` | `CSRInstanceSync::ReqGemGachaInstCB` 0x00ae61bc | gacha |
| `/reference/V2_GetSupply`, `/lobby/V2_GetSupplyInst` | `CSRSyncRef::ReqSupplyCB` 0x00f84c10; `CSRSyncSupply::RequestRefresh` 0x00f908f0 | supply |
| `/dailyquest/GetRefList` | `CSRSyncRef::ReqDailyQuestCB` 0x00f84d9a | daily quest |
| `/fishing/GetInven`, `/fishing/GetRecord`, `/fishing/GetPriceRef`, `/fishing/GetFishingPool` | none retained (only `CSRMFishing`, `CSRSceneMFishing`, `CSRTableMFishingInven`) | fishing |
| `/explore/GetRef` | none retained (`CSRSyncExplore` exists) | explore |
| `/gvg/GetRef` | `CSRSyncRef::ReqGVGRefCB` 0x00f8525c | GvG |
| `/scenario/GetList` | none retained | scenario |
| `/v2/purchase/ReqIAPRef` | `CPVPurchase::RequestIAPInfo` 0x0080df6c | IAP |
| `/world/GetIapMainIcon` | `CSRIAPHotDeal::GetRequirementDataList` 0x00adaef4 | IAP |
| `/mirage/GetInfo` | `CSRExploreMirageInfo::RequestInfo` 0x0092b30c | **separate mode — see `mirage-getinfo.md`** |
| `/pv_tracker/MarkAP` | no parser; called 8×/session; telemetry ack | tracker |

---

## 4. What "recoverable from existing evidence" actually means here

The honest headline of this triage is a **negative result**, and it is worth
stating plainly because it changes what the team should ask Ghidra for.

Key sets have been resolved for **twelve** functions on disk, all of them
`CSRGame*` / `CSRCardInfoContainer` / `CSRSyncGlobal` internals:

```
AddMonster          0x00a0b540    AddStageMonster     0x00a0d194
SetRefID            0x0086c30c    SetCard             0x0087baa4
SetCardChain        0x0087e110    SetCardRankUp       0x0087ec9c
SetCardEnhancePrice 0x0087f048    SetStage            0x00a274d0
SetArea             0x00a28108    ParseUserDatailInfo 0x00f6e240
Parse_InstEnemy     0x0092dff4    ReqMonsterCB        0x00b4514c
ReqTargetStageMonsterCB 0x00b4606c
```

Every one of them is an internal model method that a `*CB` callback calls. **Not
one of the 171 retained `*CB` callback symbols has its own resolved key list.**
The `*CB` functions take `nlohmann::json const&` and delegate; the reading
happens one or two frames down. So "the route's callback is known" is not
sufficient for triage — the model method it calls has to have been dumped, and
only a dozen have been.

Consequence: 44 of the 47 mocked routes cannot be responsibly shaped from what
is on disk today. Three were shaped because their model methods happened to be
dumped. The rest need new decompiles, and §3 says which ones are worth it.

---

## 5. Server-side changes made by this session

Files changed (all under `server-ts/src/`):

| file | change |
|---|---|
| `src/bootstrap.ts` | new `partyProfile()` (the `ParseUserDatailInfo` key set); `starterStageMonsters` now emits `_id` **and** `wave_list`; typed `StageWave` / `StageMonsterRecord` |
| `src/game-routes.ts` | `GetTargetStageMonster` uses the typed record; `GetMonster` publishes under `M001`, `001` **and** `""`; `GetCardChain` / `GetCardRankUp` / `GetCardEnhancePrice` return `{}`; `GetTargetUserInfo` echoes the requesting `pvid` and the real nickname; new `profilePvid()` / `profileNickname()` helpers |
| `src/state.ts` | `/lobby/Enter` publishes `partyProfile()` + `nick_name` at the top level of `ret_data` |

**A server restart is required for any of this to reach the client.** Agent E
owns the running process (`tools/stop-server.ps1` then
`tools/start-server.ps1`) — the server agent did not touch it.

`npm test` passes: *"TypeScript smoke test passed with 285 recovered routes"*,
plus the persistence and resource suites.

### Not done, deliberately

- **No regression test for the new keys.** `tests/` is outside this agent's
  ownership and agent E may be mid-run. The change is additive and
  `npm test` already passes, but a test asserting
  `/lobby/Enter.ret_data.ref_id_1 === "001"` and
  `GetTargetStageMonster.ret_data.N003._id` would be worth adding by whoever owns
  `tests/`.
- **No invented shapes.** 44 routes still return `mock:true`. That is the
  correct state given §4.