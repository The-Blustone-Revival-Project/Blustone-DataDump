# Episode-scene routing — is the replica driving the client into the wrong scene?

Written by the **server/contract research agent**, 2026-10-02.
Read-only: `analysis/native-*.tsv`, `analysis/native-*.txt`, `analysis/ghidra-*.txt`,
`analysis/r012/server-log-r012-leg1b.txt`, `server-ts/src/*`, plus two offline analyses
of the read-only `analysis/extracted/lib/armeabi-v7a/libnative_core.so`
(`.ARM.exidx` parse and `llvm-objdump` disassembly, NDK toolchain).
No Ghidra, no adb, no server, no git, no edits to `server-ts/src/*`.

---

## 0. Headline

> **The "scene mix-up" is a mis-symbolisation, and it is falsifiable with two
> commands and no device. The crash is in `CSRMStage::MakeStageInst` — the
> *expedition* scene. `analysis/research/FALSIFIED-showthumbnail.md` §3 corrected
> a non-problem and created one.**

The mechanism: the project's symbol tables are in **Ghidra image addresses**
(ELF file vaddr `+ 0x10000`); the runtime `BLUSTONE_ARM` `offset=` and the real
PC are in **ELF file vaddrs**. `FALSIFIED-showthumbnail.md` §3 compared the
runtime offset `0xb2507b` against a Ghidra label table, got
`CSRSceneMEpisode::MakeStageInst`, and concluded the client was in an episode
scene. It is in `CSRMStage::MakeStageInst`, which is what the device's own
`dladdr` already said.

Everything downstream of that conclusion is void, including
"`MakeStageInst` resolves `episode_stage`/`episode`/`monster`" (those literals
belong to a *different* method 0x6a0 bytes away) and the "`009`-keyed table
0x4c3 from the crash PC" guess (`009` belongs to `PopUpResultWin`, 0x503 bytes
*past* the crash, a different function).

---

## 1. The address spaces, proved

**[RECOVERED]** `analysis/native-evidence.tsv`, `analysis/native-makestageinst.txt`
and the `analysis/ghidra-*.txt` dumps are in **Ghidra image addresses**.
`tools/resolve-literals-offline.py` states the bias explicitly
(`ADDR_BIAS = 0x10000`, "Ghidra image address == file offset + 0x10000").

**[RECOVERED]** The runtime offset is **not** in that space.
`analysis/r012/blustone-arm-leg1b.txt` reports `pc=0x4b2507b offset=0xb2507b`,
i.e. `runtime_offset = pc - 0x4000000` — a plain ELF file vaddr, which for this
library is also the file offset (verified: `.text addr=0x612cc0 off=0x612cc0`).

**[RECOVERED]** Proof that the two spaces differ by exactly `0x10000`, from the
library's own unwind table (no Ghidra, no heuristics):

`.ARM.exidx` (ELF `0x01bd46f8`, 0x58528 bytes, `entsize=8`, `link=13`=`.text`)
is a sorted array of prel31 function-start offsets. Decoding it (prel31 is a
**31-bit signed** value; the sign bit is bit 30, which is why a naive 32-bit
sign extension yields garbage) gives 44 482 distinct `.text` function starts.

| test | result |
|---|---|
| all table labels ≥ `.text` with an **exact** exidx start at `label - 0x10000` | 27 817 / 43 626 (63.8 %) |
| labels whose name is a `CSR*` class method | **1 254 / 1 342 (93.4 %)** — the misses are all trivially leaf methods (`GetSelectedItem`, `Rewind`, `Skip`, `SetEffectColor`) that the compiler emitted without unwind records |
| labels containing `CSR` or `CMHash` | 14 305 / 18 293 (78.2 %) — misses are dominated by `std::function`/`__shared_ptr_emplace` template instantiations and thunks, again mostly unwind-free |
| **the 10 `MakeStageInst` labels, plus 5 more `CSRMStage`/`CSRSceneMEpisode`/`CSRSceneMgr` methods** | **15 / 15 EXACT**, and each exidx extent equals the label-to-next-label gap *to the byte* |

The decisive test is the last row, not the percentages: a wrong bias would not
produce exact hits on 15/15 real game methods **and** byte-identical extents.
The percentage rows are there to show the residual misses are the expected
population (leaf functions and templates with no `.ARM.exidx` entry), not a
systematic offset.

Spot check (`label` = Ghidra, `elf` = `label - 0x10000`):

```
CSRSceneMEpisode::MakeStageInst  label=0xb23f60 elf=0xb13f60 exidx_start=0xb13f60 size=0xb8c  EXACT
CSRMStage::MakeStageInst         label=0xb33f84 elf=0xb23f84 exidx_start=0xb23f84 size=0x16cc EXACT
CSRMStage::C1                    label=0xb33ca8 elf=0xb23ca8 exidx_start=0xb23ca8 size=0x24   EXACT
CSRMStage::PopUpPause            label=0xb35650 elf=0xb25650 exidx_start=0xb25650 size=0x514  EXACT
CSRSceneMEpisode::SetBGM         label=0xb25930 elf=0xb15930 exidx_start=0xb15930 size=0x1a4  EXACT
```

A second, independent cross-check on the same conclusion:
`resolve-literals-offline.py --find-string BGM_BATTLE1` returns **8** code
references, one per battle scene's `SetBGM` — `0xb25982` (inside
`CSRSceneMEpisode::SetBGM` = `[0xb25930,0xb25ad4)`) and `0xb362ec` (inside
`CSRMStage::SetBGM` = `[0xb362d4,0xb36348)`). Both land inside their
table-attributed extent only under the `0x10000` label convention.

**Rule to adopt before any more symbolisation work in this project:**
`Ghidra label = ELF/runtime offset + 0x10000`. Write it on the artefact.

---

## 2. The crash, located exactly

**[RECOVERED]** `0xb2507b` (ELF) = `0xb3607b` (Ghidra) is inside
`CSRMStage::MakeStageInst`, at **+0x10f7**:

```
elf 0xb23f84 .. 0xb25650   exidx extent, size 0x16cc
ghidra label 0xb33f84      = _ZN9CSRMStage13MakeStageInstEv  (native-evidence.tsv)
crash elf 0xb2507b         -> +0x10f7 into that function
```

`analysis/r012/blustone-arm-leg1b.txt` and `-leg2.txt` both print
`symbol=_ZN9CSRMStage13MakeStageInstEv`, and `dladdr` works on ELF addresses —
so **the device was right and the offline re-symbolisation was wrong.**

### 2.1 The faulting instruction

`llvm-objdump --triple=thumbv7a-linux-androideabi` over ELF `0xb25040..0xb250e0`:

```asm
b2506a: bl   0x8f4604  __hash_table<...>::__emplace_unique_key_args<...>   ; map at this+0x264
b2506e: ldr  r1, [sp, #0xe8]      ; returned __hash_node*
b25070: ldr  r0, [sp, #0x34]
b25072: ldr  r1, [r1, #0x20]      ; -> list<list<ACTOR_INFO>>::__last_
b25074: mls  r0, r0, r6, r8       ; r0 = a - b*c
b25078: ldr  r1, [r1, #0x8]       ; -> *( ... )  == 0
b2507a: str  r0, [r1, #0x4c]      ; <-- FAULT
b2507c: ldrb.w r0, [sp, #0x48]
```

Three independent coincidences, all satisfied:

| observed (r011/r012, twice) | instruction |
|---|---|
| `fault=0x4c` | store at `[r1 + 0x4c]` |
| `r1=00000000` | `r1` is the store's base register |
| `r0=0000000a` | `r0` is the value computed by the immediately preceding `mls` and about to be stored |

The reported `pc=0x4b2507b` is **odd**, which a Thumb instruction address cannot
be — it is the conventional `pc | 1` Thumb marker, so the true faulting
instruction is `0xb2507a`. That also explains the off-by-one the reports could
not account for.

### 2.2 The same statement in decompiled source — already on disk

**[RECOVERED]** `analysis/native-makestageinst.txt` decompiles **all ten**
`MakeStageInst` functions, including the crashed one, at
`analysis/native-makestageinst.txt:5689` (`===== 00b33f84 MakeStageInst`).
Line **6959** is the crash, verbatim:

```c
*(int *)(*(int *)(*(int *)(local_80 + 0x20) + 8) + 0x4c) = iVar29 - local_134 * (iVar12 + -1);
```

Context:

- `local_80` is the sret result of
  `std::__hash_table<...>::__emplace_unique_key_args<...>(&local_80, (CMHashID *)(this + 0x264), ...)`
  at line 6955, keyed by `CSRLevelData::GetMonsterGroupID()` (line 6950).
  The container type is
  **`std::unordered_map<CMHashID, std::list<std::list<CSRGameActor::ACTOR_INFO>>>`
  as the member `this + 0x264` of `CSRMStage`.**
- The right-hand side is `iVar29 - local_134 * (iVar12 + -1)`, where
  `local_134 = (int)((*(float *)(iVar29 + 0x20) * fVar51) / fVar50)` (line 6899),
  `iVar29 = CSRDataMgr::GetStaticData()` (line 6897) — a **spawn-count /
  spawn-position** computation. `iVar29` is dereferenced at `+0x20` first, so
  `iVar29` is valid; the **null is in the map node's nested-list chain**.
- Twenty lines earlier (6900–6937) an almost identical `+0x4c` / `+0x50` write is
  performed inside `if (piVar22 != (int *)0x0)` over `this + 0x26c`. **The crash
  store at 6959 has no such guard.**

**This answers `analysis/testing/report-012.md` §9 follow-up 4** ("what is at
offset `0x4c` of the null record? if it is a member of `CSRGameMob::INFO`, the
monster table is empty"): **no.** It is a field of the CSRMStage virtual-deck
map's last inner `list<CSRGameActor::ACTOR_INFO>` element, and the null is an
unpopulated inner list for this monster group — not the monster table.

### 2.3 What feeds `GetMonsterGroupID()` — and it is not a server route

**[RECOVERED]** `CSRLevelData::LoadLevelData(const std::string&)`
(`native-evidence.tsv`, label `0x00a178c4`) resolves 54 literals
(`tools/resolve-literals-offline.py --function 0xa178c4:0xa19000`):

```
'.JSON'   'left'  'right'  'run_accl'  'actor'  'def_backend_bb'  'atk_range_scl'
'waiting' 'idle_time'  'run_spd'  'walk_spd'  'fall_spd'
'emergency_by_remain_time'  'spawn_y'  'ai_exchange_cool'
'death_time_increase_sp_per_sec'  'death_time_increase_atk_ratio'
'death_time_cond_hp'  'sp_increase_spd_per_sec'  'sp_increase_per_kill'
'sp_increase_per_atk'  'sp_increase_per_dmg'  'sp_max'
'fever_increase_per_touch'  'fever_cooltime'  'max_fever_point'
'fever_deceleration'  'fever_acceleration'  'fever_decrease_spd'
'step_1'..'step_4'  'fever_step_cond'  'fever_step_spd'  'fever_step_auto_dash'  'normal'
```

It appends `".JSON"` and opens the file through the **local** CM database
(`CMLocalDB::Open(const string&, RMF_DIR, MODE, ...)`,
`native-evidence.tsv:000ff1b7`/`000ff221`). **So the per-battle level data,
`CSRLevelData`, and therefore the monster-group ids that key the map at the
crash site, come from a client-side resource file — not from any `/reference/*`
route.**

> **[inferred-and-unverified]** the string `LoadLevelData` is handed is most
> likely one of the per-stage fields `CSRGameStage::SetStage` already reads
> (`.value` or `.res_prefix`; `AGENTS.md` §11 / `analysis/ghidra-setstage-exact.txt`).
> Our fixture sends `value: 0` and `res_prefix: ""` (`server-ts/src/bootstrap.ts`).
> **One decompile of `LoadLevelData`'s caller settles it.** That is the single
> highest-value next decompile in the project and it is not in the batch queue.

---

## 3. Deliverable 1 — the `/episode/*` route family

### 3.1 The complete family: three routes

**[RECOVERED]** `tools/native-grep.py -p "/episode/"` over
`analysis/native-all-strings.tsv` returns exactly three URL literals:

| route | .rodata | requester | note |
|---|---|---|---|
| `/episode/GetLog` | `01d79d72` | `CSRMEpisode::RequestLog` `0x00b186d8` | the only one ever issued |
| `/episode/Read` | `01d7ad4e` | `CSRMEpisode::RequestRead` `0x00b19638` | never issued in any recorded session |
| `/episode/Reward` | `01d7ad5c` | `CSRMEpisode::RequestReward` `0x00b1979c` | never issued in any recorded session |

Full table, keys and mock status: **`analysis/research/episode-route-table.md`**.

### 3.2 Mocked vs implemented

**[RECOVERED]** `server-ts/src/game-routes.ts:393`:

```ts
if (route === "/episode/GetLog") return state.envelope({ read_log: [], reward_log: [] });
```

This is the **last explicit handler before the generic mock fallback** in that
file, so:

- `/episode/GetLog` — **IMPLEMENTED**, not mocked.
- `/episode/Read`, `/episode/Reward` — **MOCKED** (fall through to
  `{mock:true, route, request_keys}`). Moot: the client has never issued either.

`server-ts/src/openapi.ts:375-380` documents `/episode/GetLog`;
`server-ts/src/openapi.ts:585-591` already specifies the element shape
correctly (§3.4 below). No doc fix needed.

### 3.3 Which are on the battle path — **none**, and this is a hard negative

**[RECOVERED]** from `analysis/r012/server-log-r012-leg1b.txt` (leg 1b, full
session, 74 distinct routes):

```
16:51:20.788Z  /reference/GetExtra
16:51:23.050Z  /lobby/Enter
16:51:23.977Z  /episode/GetLog          <-- the ONLY /episode/* request, 0.93 s after /lobby/Enter
16:51:31.294Z  /relation/GetTargetUserInfo
16:53:05.693Z  /relation/GetTargetUserInfo      (node tap)
16:54:02.287Z  /reference/GetTargetStageMonster  (Begin Battle)
16:54:47.984Z  /mission/Start
16:54:48.755Z  /reference/GetTargetStageMonster  (re-issued)
16:54:48.908Z  CRASH (elf 0xb2507b)
```

`/episode/GetLog` is issued **once per session, 2 min 25 s before the crash**,
inside the boot reference block. **No `/episode/*` route is anywhere in the
battle window.** The window is exactly the four routes in
`analysis/testing/report-012.md` §3.1 and nothing else.

This is the load-bearing negative for the whole hypothesis: a scene selected by
an `/episode/*` response is **impossible**, because no such response is in the
window.

### 3.4 `/episode/GetLog` — verified, and the existing response is correct

**[RECOVERED]** `analysis/native-episode-log.txt` dumps two functions.

`CSRInstanceSync::ReqEpisodeCB` (label `0x00ae62e0`) — the `/episode/GetLog`
callback:

```c
if (CPVHTTPResponse::GetResultCode(response) != 1) return;
*(CSRMEpisode::get()) = 1;                                   // "episode data loaded" flag
CSRMEpisode::ParseLog(CSRMEpisode::get(),
                      json::operator[](param_4, <key>));     // one ret_data[key]
```

Note the callback indexes `ret_data` with **one generated key** and hands the
resulting subtree to `ParseLog` — so `ret_data` itself is an object and
`ParseLog` receives one of its values. Our `ret_data = {read_log, reward_log}`
satisfies that.

`CSRMEpisode::ParseLog` (label `0x00b19268`) — two arrays, each of **objects**:

| resolved literal | .rodata | code reference | meaning |
|---|---|---|---|
| `read_log` | `01d7ad37` | `ldr@0x00b192a8` (**exactly one** xref in `.text`) | first top-level key |
| `id` | `01d676c3` | via `DAT_00b19540 + 0xb19336` | element sub-key of `read_log` |
| `reward_log` | `01d7ad40` | `ldr@0x00b193ae` (**exactly one** xref) | second top-level key |
| `id` | `01d676c3` | via `DAT_00b19548 + 0xb19438` | element sub-key of `reward_log` |

The decompile shows `iter != end` over `ret_data[key]`, then
`json::operator[](*it, <"id">)` then `from_json(..., &std::string)`. So:

```json
{ "read_log":   [ { "id": "..." } ],
  "reward_log": [ { "id": "..." } ] }
```

**Verdict: `AGENTS.md` §6's "wants `{read_log: [], reward_log: []}`" is
correct**, and the elements are objects with an `id` string, not bare strings —
which `openapi.ts:589` already documents. `[]` is the right answer for a fresh
account, so **the existing implementation needs no change.** One forward-looking
note: `ParseLog` `destroy`s the two maps at `param+0xb8` and `param+0xc4`
(lines 65-76) *before* refilling them, so if the account ever gains an episode
the shape must be `[{id}]` or the state is wiped on every login.

Two further recovered details, for completeness:

- `CSRMEpisode::RequestRead` (label `0x00b19638`) loads the **generated** key
  literal `'r_'` (`.rodata 01d7ad4b`) — `"/episode/Read"` takes a concatenated
  key, the same pattern as `GetCardChain`'s `"r"+gen`.
  `RequestClear` (label `0x00b19710`) resolves **zero** literals.
- `RequestLog`/`RequestReward` load only the standard request-envelope keys
  (`app_code`, `app_ver`, `market`, plus the framework's `pvid`/`otp`).

---

## 4. Deliverable 2 — the scene/mode selector

### 4.1 What the selector actually is: a client-side enum

**[RECOVERED]** Nine concrete battle scenes are constructed by
`make_shared<...>(CSRGameBase::MODE, CSRSceneGame*)`:

| class | `make_shared` | constructor |
|---|---|---|
| `CSRSceneMEpisode` | `0x00e3da44` | `0x00b23c14` |
| `CSRMStage` (expedition) | `0x00e3ddbc` | `0x00b33ca8` |
| `CSRExploreMirage` | `0x00e3d91c` | `0x00925044` |
| `CSRExploreAbyss` | `0x00e3d6cc` | `0x008ffea4` |
| `CSRFindShard` | `0x00e3d7f4` | `0x00905c64` |
| `CSRFCE` | `0x00e3db6c` | `0x009414f4` |
| `CSRGuildBattle` | `0x00e3dc94` | `0x00a94418` |
| `CSRTutorialPrologue` | `0x00e3d354` | `0x00f054e0` |
| `CSRTutorialMStageSkill` | `0x00e3d47c` | `0x00efd778` |
| `CSRTutorialSupportSkill` | `0x00e3d5a4` | `0x00f0f1b0` |

**[RECOVERED]** `CSRSceneMgr::LoadGameScene(CSRGameBase::MODE)` (label
`0x00eb22b8`, exidx size **0x4c**) disassembles to the whole of its body:

```asm
ea22cc: bl  CSRTextureCache::get
ea22d0: movs r1, #1
ea22d2: bl  CSRTextureCache::ClearTextureCache(TEX_CACHE_TYPE)
ea22d6: bl  CSRTextureCache::get
ea22da: movs r1, #2
ea22dc: bl  CSRTextureCache::ClearTextureCache(TEX_CACHE_TYPE)
ea22e4: bl  std::make_shared<CSRSceneGame>(const CSRGameBase::MODE&)
ea22ec: strd r0, r1, [r4]
```

**It reads no JSON at all.** It clears two texture-cache classes, constructs the
generic `CSRSceneGame` *container* from the MODE, and stores it. The switch that
picks the **concrete** subclass is therefore in some other function.

**[UNKNOWN]** where the `MODE` value comes from. A full-`.text` scan for Thumb
`BL` to `LoadGameScene` returns **0 direct call sites**, so it is reached
through a PLT/vtable or from a statically-indirect site; and the concrete
`make_shared<CSRSceneMEpisode>` / `make_shared<CSRMStage>` calls are likewise not
in any function we have dumped. I could not recover the MODE source without
Ghidra and I am not going to guess at it.

### 4.2 Strong negative: **no response field anywhere names a mode or scene**

**[RECOVERED]** `tools/native-grep.py --table both` over **both** 400 k-line
tables (`native-all-strings.tsv` *and* `native-evidence.tsv`) returns **zero
hits** for every one of:

```
play_type   mission_type   stage_type   game_mode   scene_id
```

Those are the plausible spellings. Nothing. There is no `mode`, `scene`,
`chapter` or `play_type` JSON key in this client to be a selector.

`episode_stage` (`.rodata 01d75942`) does exist, but it is **not** a response
field: in `CSRSceneMEpisode::MakeStageInst` it is `assign`ed to `this + 0x244`
with a length of `0xd` — a **member of the scene object**, i.e. a local
database / resource key. The other hits for the string are mangled symbol names
(`EPISODE_STAGEDATA`).

### 4.3 `/lobby/Enter` and `/mission/Start` carry no selector

Read in full (`server-ts/src/state.ts:314-393` and `:426-489`, read-only):

- `lobbyEnter` publishes `partyProfile()` (the 41-key `ParseUserDatailInfo` set
  from `analysis/ghidra-userdetail.txt`), `nick_name`, `nickname`, `tuto`,
  `area_achieve`, `user{ap,bp,gdp,max_*,gold,honor,group_exp,vip_exp,
  card_inven_max,ap_charge_time,bp_charge_time,leader_inst_id,is_newbiew,
  is_dailyquest_newbie,is_shared,pm_key,tuto,area_achieve}`,
  `battle{league_level,rating_point,rank,league_win,maintenance,
  battle_server_maintenance,server_maintenance,state}`, `deck`,
  `iap_bonus`, `iap_achieve_reward`, `special`, `nickname_list`.
  **No mode, chapter, story, episode or scene field.**
- `startMission` publishes `accepted`, `stage_id`, `battle_id`, `ap`,
  `battle{...}`, `mission_id`. **No mode field.**
- `completeTutorialList()` (`server-ts/src/game.ts`) emits only
  `{type, step, is_cleared}` rows.

Per-stage story linkage exists and is a real candidate:
`CSRGameStage::SetStage` reads `.story_id`, `.begin_dialog_id`, `.end_dialog_id`
(`analysis/ghidra-setstage-exact.txt`), and our fixture sends all three as the
**empty string** (`server-ts/src/bootstrap.ts:216-218`). But a stage record
field cannot select a *class* for the current battle — it is read by the
already-chosen scene. **Labelled as a plausible-but-unverified lever, not a
finding.**

---

## 5. Deliverable 3 — verdict on expedition reachability

**The expedition campaign is reachable, and the client is running it right now.**
The crash is inside the expedition scene's own method.

Evidence, in order of strength:

1. **[RECOVERED]** The crash is in `CSRMStage::MakeStageInst` (§2). `CSRMStage`
   is the expedition/mission scene; its `OpenStage` (label `0x00b36348`,
   0x14 bytes) tail-calls `CSRGameBase::OpenStage`. The episode scene has no
   `OpenStage` at all.
2. **[RECOVERED]** The wire shows an expedition mission: the client navigated to
   the Snowfield stage map, tapped a node, pressed Begin Battle, and issued
   `/mission/Start {"stage_id":"N002"}` — which is `CSRMStage::RequestStart`
   (`AGENTS.md` §11), the expedition request. `CSRSceneMEpisode`'s clear/reward
   requests are `/episode/Read` and `/episode/Reward`, neither of which fires.
3. **[RECOVERED]** No `/episode/*` route is in the battle window (§3.3).
4. **[RECOVERED]** There is no response field that could select a scene (§4.2).
5. **[RECOVERED]** The two scenes build participants from **different** data and
   the crash sits in the expedition one. `CSRMStage::MakeStageInst` calls
   `CSRGameMob::GetStageMonsterLinkData` and `CSRLevelData::GetMonsterGroupID`
   (`analysis/native-makestageinst.txt:6629/6651/6755/6760/6950/6955`);
   `CSRSceneMEpisode::MakeStageInst` calls `CSRMEpisode::get()` /
   `GetCombat()` instead (`:5033-5034`), i.e. it reads the local
   `CSREpisodeData` graph loaded from `CSRMEpisode::ReadJson(const string&)`.

So: **not "the replica's bootstrap selects episode".** There is no such defect.
The device control leg that supposedly falsified the shape work was reading a
correct symbolisation; the re-symbolisation introduced afterwards is what needs
retracting.

### 5.1 What actually blocks the battle scene

Not the monster table. Not the card table. Not a scene mix-up. The crash is a
**null-pointer 32-bit store into an unpopulated inner
`list<CSRGameActor::ACTOR_INFO>` of `CSRMStage`'s CMHashID-keyed virtual-deck
map (`this + 0x264`), immediately after emplacing the key returned by
`CSRLevelData::GetMonsterGroupID()`**, with no null guard
(`analysis/native-makestageinst.txt:6959`).

`CSRLevelData` is loaded from a **local `<id>.JSON` file**
(`CSRLevelData::LoadLevelData`, §2.3) — so the immediate next questions are:

1. **Which `<id>.JSON`?** [inferred-and-unverified] one of `SetStage`'s
   `.value` / `.res_prefix`; our fixture sends `value: 0`, `res_prefix: ""`.
   One decompile of `LoadLevelData`'s caller answers it and is worth more than
   every `GetTargetStageMonster` field experiment so far combined.
2. **Does that `.JSON` exist in the CDN we serve?** It is a `CMLocalDB::Open`
   path, i.e. a `CMDB` record, not necessarily a `.pkg` file — check the
   `CMDB`/LevelDB side, not `BLUSTONE_PACKAGE_NAMES`.
3. **`CSRDataMgr::GetStaticData()->[+0x20]`** is read as a float and divided by a
   count to produce `local_134` (line 6899). If that static table is empty,
   `local_134` is garbage and the guarded sibling loop at 6900-6937 silently
   does nothing while the unguarded store at 6959 still runs.

---

## 6. Retractions this file asserts

| claim | source | status |
|---|---|---|
| "PC `+0xb2507b` is `CSRSceneMEpisode::MakeStageInst`, the **episode** scene" | `FALSIFIED-showthumbnail.md` §3, and the two `analysis/*.md` items derived from it | **WRONG — retract.** ELF `0xb2507b` → Ghidra `0xb3607b` → `CSRMStage::MakeStageInst`. It is the expedition scene. |
| "`CSRSceneMEpisode::MakeStageInst` resolves `episode_stage`, `episode`, `monster`" | `FALSIFIED-showthumbnail.md` §3, from `--function 0xb23f60:0xb27d34` | **TRUE but irrelevant.** Those literals are real, but they are in `MakeStageInst` `[0xb23f60,0xb24aec)` — a *different* function, 0x6a0 bytes below the crash. The scan window spanned five methods. |
| "`'009'` is the only literal in `0xb25000..0xb25600`, 0x4c3 from the crash PC — an indexed access off a `009`-keyed table" | `FALSIFIED-showthumbnail.md` §3.1 | **VOID.** `009` is loaded at Ghidra `0xb2553e`, inside `PopUpResultWin` `[0xb2547c,0xb25930)`. It is 0x503 bytes *past* the crash and in a different function. `OnFinish` and `PopUpPause` resolve **zero** string literals. |
| "the replica may be driving the client into the wrong scene entirely" | `FALSIFIED-showthumbnail.md` §3 | **NO.** No `/episode/*` route is in the battle window and no response field names a mode or scene. |
| "PC `+0xb2507b` = `CSRMStage::MakeStageInst()`" | `analysis/testing/report-011.md`, `report-012.md` | **CORRECT — reinstate.** The device's `dladdr` was right all along; the error was introduced offline. |
| "`/reference/GetTargetStageMonster` shape work is aimed at dead code because `AddStageMonster` is never reached" | `FALSIFIED-showthumbnail.md` §2 | **NOT ESTABLISHED — still open.** Nothing here bears on it. The stage-monster route is still in the window and still unaccounted for. I am not claiming it is dead. |

## 7. What I did not do

- No Ghidra, so no `LoadGameData`/`GetSceneGameFactory` decompile. §4.1's
  `MODE` source stays **[UNKNOWN]**.
- No edits to `server-ts/src/*`. `/episode/GetLog` needs none (§3.4).
- No device leg, no server restart, no git.
- I did not touch `/reference/GetTargetStageMonster` — the `_id` / `wave_list`
  / `show_thumbnail` question is untouched and unresolved by this file.

## 8. Reproduction (read-only, ~2 s each)

```powershell
# 1. address-space proof + the crash's containing function  (~60 s, parses .ARM.exidx)
#    see the script body quoted in §1; drop at %TEMP%\exidx.py

# 2. per-method literal windows for the whole CSRSceneMEpisode block
python tools\resolve-literals-offline.py --function 0xb23f60:0xb24aec   # episode_stage episode monster monster
python tools\resolve-literals-offline.py --function 0xb24f40:0xb2547c   # resolved: 0
python tools\resolve-literals-offline.py --function 0xb2547c:0xb25930   # '009'

# 3. the faulting instruction  (NDK llvm-objdump)
tools\android-sdk\ndk\29.0.14206865\toolchains\llvm\prebuilt\windows-x86_64\bin\llvm-objdump.exe `
  -d --triple=thumbv7a-linux-androideabi --start-address=0xb25040 --stop-address=0xb250e0 `
  analysis\extracted\lib\armeabi-v7a\libnative_core.so
#   -> b2507a: str r0, [r1, #0x4c]

# 4. the same store, decompiled and already on disk
#    analysis\native-makestageinst.txt:6959

# 5. no mode/scene key exists
python tools\native-grep.py --table both -p play_type -p mission_type -p stage_type -p game_mode -p scene_id
```
