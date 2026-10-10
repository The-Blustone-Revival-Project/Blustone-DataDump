# `/episode/*` route table — every route, its parser, its keys, its server status

Companion to `analysis/research/episode-scene-routing.md`.
Written by the **server/contract research agent**, 2026-10-02. Read-only.

## Legend

- **[RECOVERED]** — resolved from a literal or a decompile on disk; the citation is given.
- **[FIXTURE]** — local replica data, not recovered from the original server.
- **[UNKNOWN]** — not determinable from what is on disk.
- **Address columns are Ghidra image addresses** (`analysis/native-evidence.tsv`,
  `analysis/native-*.txt`). **Runtime `BLUSTONE_ARM` offsets are ELF addresses
  = Ghidra − 0x10000.** See `episode-scene-routing.md` §1.

---

## 1. The family is exactly three routes

`tools/native-grep.py --table both -p "/episode/"` returns three `.rodata` URL
literals and nothing else. `servicePrefixes` in `server-ts/src/catalog.ts:9`
lists `episode`, so all three are in the replica's catalog.

| route | `.rodata` | requester (Ghidra addr) | callback | issued by the client? |
|---|---|---|---|---|
| `/episode/GetLog` | `01d79d72` | `CSRMEpisode::RequestLog` `0x00b186d8` | `CSRInstanceSync::ReqEpisodeCB` `0x00ae62e0` | **yes — once per session, at boot** |
| `/episode/Read` | `01d7ad4e` | `CSRMEpisode::RequestRead` `0x00b19638` | none retained | **never** |
| `/episode/Reward` | `01d7ad5c` | `CSRMEpisode::RequestReward` `0x00b1979c` | none retained | **never** |

Related requester with no URL literal of its own — **[UNKNOWN]** whether it
targets one of the two above or a third path that shares them:

| function | Ghidra addr | literals resolved |
|---|---|---|
| `CSRMEpisode::RequestReadOrClear` | `0x00b178f0` | not scanned |
| `CSRMEpisode::RequestClear` | `0x00b19710` | **0** (`resolve-literals-offline.py --function 0xb19710:0xb1979c`) |

---

## 2. Server status

| route | status | evidence |
|---|---|---|
| `/episode/GetLog` | **IMPLEMENTED** | `server-ts/src/game-routes.ts:393` — `if (route === "/episode/GetLog") return state.envelope({ read_log: [], reward_log: [] });` |
| `/episode/Read` | **MOCKED** | falls through to the generic fallback at `server-ts/src/game-routes.ts:395-400` (`{mock:true, route, request_keys}`) |
| `/episode/Reward` | **MOCKED** | same |

`/episode/GetLog` is the **last explicit handler in the file** before the
fallback, so the two mocks are a fact of the file's structure, not an oversight.
Both are moot in practice — the client has never issued either in any recorded
session.

Docs: `server-ts/src/openapi.ts:375-380` (`/episode/GetLog`),
`:507` (tag list), `:585-591` (`EpisodeProgress` schema — **already correct**,
`items: {type:"object", required:["id"]}`). **[FIXTURE]** the empty arrays.

---

## 3. `/episode/GetLog` — the exact contract

### 3.1 Callback, `analysis/native-episode-log.txt` (Ghidra `0x00ae62e0`) **[RECOVERED]**

```c
if (CPVHTTPResponse::GetResultCode(response) != 1) return;
*(CSRMEpisode::get()) = 1;                                   // "episode subsystem loaded" flag
CSRMEpisode::ParseLog(CSRMEpisode::get(), json::operator[](param_4, <generated key>));
```

The callback indexes `ret_data` with **one generated key** and passes the
subtree on. Our `ret_data = { read_log, reward_log }` satisfies it.

### 3.2 Parser, `CSRMEpisode::ParseLog` (`0x00b19268`) **[RECOVERED]**

| literal | `.rodata` | single xref | role |
|---|---|---|---|
| `read_log` | `01d7ad37` | `ldr@0x00b192a8` | first top-level key |
| `id` | `01d676c3` | `DAT_00b19540 + 0xb19336` | element sub-key of `read_log` |
| `reward_log` | `01d7ad40` | `ldr@0x00b193ae` | second top-level key |
| `id` | `01d676c3` | `DAT_00b19548 + 0xb19438` | element sub-key of `reward_log` |

`read_log` and `reward_log` each have **exactly one** `.text` reference in the
whole library (`resolve-literals-offline.py --find-string`).

Both loops are `iter != end` over the array, then
`json::operator[](*it, "id")`, then `from_json(..., &std::string)`.

**Required shape:**

```json
{ "read_log":   [ { "id": "<episode id>" } ],
  "reward_log": [ { "id": "<episode id>" } ] }
```

Arrays of bare strings would **not** work: `element["id"]` on a string is
`null`, `from_json` yields `""`, and every entry files under the empty key.

**Current response `{ read_log: [], reward_log: [] }` is correct** for an
account with no episodes, and no change is required.

### 3.3 State-reset hazard **[RECOVERED]**

`ParseLog` `destroy`s two `std::map` members at `param + 0xb8` and
`param + 0xc4` and resets their sentinels *before* refilling them
(`analysis/native-episode-log.txt:65-76`). Consequence for the fix agent:
once any episode state exists, a malformed or missing element silently wipes it
on the next login rather than raising an assertion. Worth a note in
`openapi.ts` if episode state is ever implemented.

---

## 4. Request shapes **[RECOVERED where listed, otherwise UNKNOWN]**

| route / function | Ghidra addr | resolved request literals |
|---|---|---|
| `CSRMEpisode::RequestLog` | `0x00b186d8` | `app_code`, `app_ver`, `market` (+ framework-supplied `pvid`, `otp`) |
| `CSRMEpisode::RequestRead` | `0x00b19638` | **`r_`** (generated key, concatenated) |
| `CSRMEpisode::RequestClear` | `0x00b19710` | none |
| `CSRMEpisode::RequestReward` | `0x00b1979c` | `app_code`, `app_ver` |

`RequestReward`'s full mangled signature is
`…(const string&, const function<void(int, SRREWARD_INFO&)>&)`, so the reward
callback receives an `SRREWARD_INFO`. **[UNKNOWN]** — no decompile on disk.

---

## 5. The episode data model, for whoever implements it

Symbols retained in `analysis/native-evidence.tsv` (Ghidra addresses):

| symbol | addr | note |
|---|---|---|
| `CSREpisodeData::LINK`, `ACTOR`, `COMBAT` | ctors at `0x00b153cc`, `0x00b139d4`, `0x00b13fe0` | the graph node types |
| `CSRMEpisode::RecursiveParser` | `0x00b1b45c` | builds the LINK tree |
| `CSRMEpisode::LoadData` / `ReadJson(const string&)` | `0x00b1a618` / `0x00b1a8b0` | **loads from a local JSON file, not from a route** |
| `CSRMEpisode::GetAvailableEvent` / `GetNeedReadItem` / `GetNeedClearItem` | `0x00b1c828` / `0x00b1d2f4` / `0x00b1d290` | drives the "New Episode" popup |
| `CSRMEpisode::IsReadDataById` / `IsClearedDataById` / `IsGotRewardById` | `0x00b1c7f8` / `0x00b1c810` / `0x00b1a600` | per-id state |
| `CSREpisodeData::ParseReward` / `ParseRequireItem` | `0x00b16028` / `0x00b15ca4` | **`ParseReward` has no resolved key list on disk** |
| `CSRGameBase::PopUpNewEpisode` / `RefreshForEpisode` | `0x009d8e30` / `0x009d16fc` | the boot popup |

**Consequence for the scene question:** `CSREpisodeData` — everything the
`CSRSceneMEpisode` battle reads — comes from `ReadJson(const string&)`, i.e.
a **local resource**, exactly like `CSRLevelData::LoadLevelData`
(`episode-scene-routing.md` §2.3). There is no server route that supplies
episode *content*. Only the **progress** (`/episode/GetLog`) and the
read/reward mutations (`/episode/Read`, `/episode/Reward`) are server-side.

That is the structural reason an "episode scene selected by a server response"
hypothesis cannot hold on this replica: the scene's data is local, its only
server inputs are read/reward bookkeeping, and none of those routes fires in the
battle window (`episode-scene-routing.md` §3.3).

---

## 6. Scenes and their `MakeStageInst` — for the record

Ten `MakeStageInst` methods exist. All ten are decompiled in
`analysis/native-makestageinst.txt`. **Ghidra address, exidx size, and the data
source each reads:**

| class | Ghidra addr | size | participant source | decompile |
|---|---|---|---|---|
| `CSRExploreAbyss` | `0x009002b8` | `0x1048` | — | `:1` |
| `CSRFindShard` | `0x0090610c` | — | — | `:945` |
| `CSRExploreMirage` | `0x00925798` | `0xcfc` | — | `:2324` |
| `CSRFCE` | `0x009418b0` | — | — | `:3131` |
| `CSRGuildBattle` | `0x00a95060` | — | — | `:4001` |
| **`CSRSceneMEpisode`** | `0x00b23f60` | `0xb8c` | **`CSRMEpisode::get()->GetCombat()`** (local `CSREpisodeData` graph); literals `episode_stage`, `episode`, `monster` ×2 | `:4910` |
| **`CSRMStage` (expedition)** | `0x00b33f84` | `0x16cc` | **`CSRGameMob::GetStageMonsterLinkData` + `CSRLevelData::GetMonsterGroupID`** | `:5689` |
| `CSRTutorialMStageSkill` | `0x00efdb6c` | — | — | `:7039` |
| `CSRTutorialPrologue` | `0x00f06e50` | — | — | `:8346` |
| `CSRTutorialSupportSkill` | `0x00f0f744` | — | also calls `CSRMEpisode::get()->GetCombat()` (`:9353`) | `:9232` |
**`CSRSceneMEpisode::MakeStageInst` does not read any server response.** It
sets `this + 0x244 = "episode_stage"` (a 13-char literal, i.e. a scene member),
then `GetCombat()` → the COMBAT map, then builds a virtual deck keyed by
`CMHashID("episode" + n)` emplaced into
`unordered_map<CMHashID, list<list<ACTOR_INFO>>>` at `this + 0x250`. Its four
string literals are its own keys and the episode-graph sub-keys.

The crash is in the **expedition** row — `analysis/native-makestageinst.txt:6959`
— which is the second row, and it is the *second* structure (at `this + 0x264`,
keyed by monster group id) that faults.
