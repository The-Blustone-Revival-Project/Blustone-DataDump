# GYM — the village Training facility (`/gym/*`, `card_handler/*`)

Content-domain research spec. Read-only: nothing in `server-ts/`, `analysis/ghidra-project/`,
`analysis/*.txt` or `recovered-assets/` was modified.

Provenance tags per `AGENTS.md` §15: **[RECOVERED]** = function+address or file:line,
**[FIXTURE]** = local compatibility data, **[UNKNOWN]** = not recoverable from what is on disk.

---

## 0. Blunt summary

| metric | value |
|---|---|
| gym-family routes found in `.rodata` | **14** |
| of those, currently returning `mock:true` | **14** |
| route → callback → model-setter mappings recovered | **10 / 14** |
| **response key sets recovered** | **0 / 14** |
| request field names recovered | **6 (adjacency only — see §4, not proof)** |

The gym is the best-*mapped* and worst-*shaped* of the four systems: every route has a named
requester, a named `*CB`, and a proven downstream call into the card-instance model, but **not
one of the `Req*CB` bodies has been decompiled**, so not one response key is pinned.

---

## 1. What the system actually is (community guide)

`recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md`:

- **§Q7 L135-151 "What considerations should I take into account when selecting a hunter
  to train?"** — training is *material-consuming*: you feed **Fodder** (§Glossary L61:
  "units which are typically used either as training material for core deck units") into a
  core unit. "Always keep 1 copy of each unit so you are able to 5* them for Fate bonuses."
- **§Q11 L183** — the Locke Box event "uses spent rupees to exchange for rewards … Try to use
  this event specifically to upgrade all your hunters, either to Master Hunter or to transcend
  them! **Can also train their skills** preferably during this event duration time, or improve
  their equipment and jewels levels."
- **§Q4 L113** — "you must have to train your Offensive to be able to break theirs too".

**Semantics that must shape the fixture:** every `/gym/*` route is a *consume-and-transform*
operation on a card **instance**, it destroys fodder instances, and it can destroy item
instances (tickets). A response that does not tell the client what was consumed will leave
the client's inventory out of sync with the server — that is a *visible* bug, not a cosmetic one.

### The gym screen is `SR_TRAINING_*`, not "Gym" **[RECOVERED]**

The village building is **Training**. `.rodata` scene keys:

```
01d8b985  SR_TRAINING_PAGE              01d8b996  SR_TRAINING_PAGE_TUTORIAL
01d8b9df  SR_TRAINING_RAISE             01d8b9f1  SR_TRAINING_RAISE_TUTORIAL
01d8b63c  SR_TRAINING_SKILL
01d8ba41  SR_TRAINING_RANKUP            01d8ba91  SR_TRAINING_RANKUP_TUTORIAL
01d8bae8  SR_TRAINING_AWAKE             01d8bafa  SR_TRAINING_AWAKE_HYPER
01d8bb12  SR_TRAINING_HYPER             01d8bb24  SR_TRAINING_HYPER_RESULT
01d8bb86  SR_TRAINING_RAISE_RESULT      01d8bb9f  SR_TRAINING_RANKUP_RESULT
01d8b5c2  SR_TRAINING_CARDVIEW          01d8b5d7  SR_TRAINING_CARDVIEW_TUTORIAL
01d8b609  SR_TRAINING_RAISE_STORY       01d8b621  SR_TRAINING_RELATION_STORY
```
plus the older naming `SR_ENHANCE/…` (`01d7c8ae SR_ENHANCE/8_EN_TRCNDNCE/1_TRCNDNCE`,
`01d8584e SR_ENHANCE/5_SR_EN_EV/RANK_UP_RESULT`,
`01d83516 SR_ENHANCE/4_SR_EN_TR/1_UI_EN_T_MN`).

**Tab → route map [RECOVERED by scene key + route adjacency]:**

| tab | scene key | route |
|---|---|---|
| Raise (level) | `SR_TRAINING_RAISE` | `/gym/LevelUp` |
| Skill | `SR_TRAINING_SKILL` | `/gym/SkillUp`, `/gym/MultiSkillUp` |
| RankUp | `SR_TRAINING_RANKUP` | `/gym/RankUp`, `/gym/RankUpBundle` |
| Hyper (Transcendence) | `SR_TRAINING_HYPER` | `/gym/RankUp`, `/gym/RankUpBundle` |
| Awake / AwakeHyper | `SR_TRAINING_AWAKE`, `SR_TRAINING_AWAKE_HYPER` | `gym/Awaken`, `gym/AwakenOvercome` |

**Tutorial gates exist for every tab** (`*_TUTORIAL` variants). There are tutorial
enumerators `GYM`, `GYM_ACHIEVE`, `GYM_FIRST_ENTER` at `01d9049a`, `01d90502`, `01d90575`
**[RECOVERED]** — these should be added to the existing `completeTutorialList()` superset
sweep in `server-ts/src/game.ts` so the Training building is not gated.

---

## 2. Routes, owners, callbacks — **[RECOVERED]**

Owning classes: **`CSRSyncCard`** (the six `/gym/*` + the two `card_handler/*` equipment
routes), **`CSRAwake`** (`gym/Awaken`, `gym/AwakenOvercome`, `reference/GetCardAwaken`),
**`CSRCardInfoContainer`** (`reference/GetCardChain`, `GetCardRankUp`, `GetCardEnhancePrice`).

Evidence: `analysis/native-evidence.tsv` (symbol table) and
`analysis/ghidra-enemycamp-refs-01.txt:57-79` (call-graph).

| route | literal @ | requester (demangled) | addr | `*CB` | addr | callback sink type | model setter proven reached |
|---|---|---|---|---|---|---|---|
| `/gym/LevelUp` | `01d8f72c` | `CSRSyncCard::RequestLevelUp(unsigned long, vector<unsigned long>, unsigned char, function<void(LEVEL_UP_PARAM)>)` | `0x00f53698` | `ReqLevelUpCB` | `0x00f53f90` | `void(LEVEL_UP_PARAM)` **by value** | `SetCardExp` `0x00ae98a0` ← call `0x00f54330` |
| `/gym/RankUp` | `01d8f739` | `CSRSyncCard::RequestRankUp(unsigned long, vector<unsigned long>, unsigned char, function<void(RANK_UP_PARAM)>)` | `0x00f546f0` | `ReqRankUpCB` | `0x00f54fe8` | `void(RANK_UP_PARAM)` **by value** | `SetCardRank` `0x00ae9c78` ← call `0x00f5553a` |
| `/gym/SkillUp` | `01d8f74f` | `CSRSyncCard::RequestSkillUp(unsigned long, SRSKILL_TYPE, string const&, function<void(int, SKILL_UP_PARAM const&)>)` | `0x00f558e8` | `ReqSkillUpCB` | `0x00f56074` | `void(int, SKILL_UP_PARAM const&)` | `SetCardSkillLevel` `0x00aea2d0` ← call `0x00f56442` |
| `/gym/MultiSkillUp` | `01d8f7ab` | `CSRSyncCard::RequestMultiSkillUp(unsigned long, vector<SRSKILL_TYPE>, function<void(int, SKILL_UP_PARAM const&)>)` | `0x00f566c8` | `ReqMultiSkillUpCB` | `0x00f5700c` | `void(int, SKILL_UP_PARAM const&)` | `SetCardSkillLevel` ← call `0x00f5754a` |
| `/gym/RankUpBundle` | `01d8f7d4` | `CSRSyncCard::RequestGroupRankUp(uint, uint, uint, uint, uint, function<void(int)>)` | `0x00f586e4` | `ReqGroupRankUpCB` | `0x00f58da0` | `void(int)` only — **no PARAM struct** ⚠️ *corrected 2026-10-05; was wrongly `void(int,int,int)` — see `analysis/research/base-stats-visual-hunt/grouprankup-sellcard-bodies-2026-10-05.md` §1.5(1), mangling `…functionIFviEEE`* | `SetCardRank` ← call `0x00f5922e` |
| `/gym/Overcome` | `01d8f7bd` | `CSRSyncCard::RequestOvercome(unsigned long, string const&, vector<unsigned long> const&, function<void(int)>)` | `0x00f577b0` | `ReqOvercomeCB` | `0x00f57f98` | `void(int)` only | `SetCardOvercome` `0x00ae9ef0` ← call `0x00f5820a` |
| `gym/Awaken` | `01d6f951` | `CSRAwake::RequestCardAwake(unsigned long, unsigned int, string const&, function<void(int)>)` | `0x0019eb46` | *(unnamed)* | — | `void(int)` only | `SetCardAwake` `0x00aea0e4` ← `FUN_00864ae0` @ `0x00864d00` |
| `gym/AwakenOvercome` | `01d6f912` | `CSRAwake::RequestAwakeOvercome(unsigned long, unsigned int, string const&, vector<unsigned long> const&, function<void(int)>)` | `0x0019ec65` | *(unnamed)* | — | `void(int)` only | same path |
| `reference/GetCardAwaken` | `01d6f888` | `CSRAwake::RequestAwakeRef(string const&, function<void(int)>, unsigned char)` | `0x0019eb0a` | — | — | — | fills `CSRAwake::REF` container |
| `card_handler/LevelUpEquipment` | `01d8f7eb` | `CSRSyncCard::RequestEquipLevelUp(unsigned long, CSREquip::TYPE, PRICE_TYPE, string const&, function<void(shared_ptr<CPVHTTPRequest> const&, CPVHTTPResponse const&, int)>, int, int, int)` | `0x00f59380` | — | — | — | equipment level |
| `card_handler/RankUpEquipment` | `01d8f819` | `CSRSyncCard::RequestEquipRankUp(unsigned long, CSREquip::TYPE, PRICE_TYPE, vector<unsigned long>, function<void(shared_ptr<CPVHTTPRequest> const&, CPVHTTPResponse const&, int)>, int, int, int)` | `0x00f5a0bc` | — | — | — | equipment rank |
| `card_handler/EquipGem` | `01d785c6` | *(owner not retained)* | — | — | — | — | — |
| `card_handler/ToggleLock` | `01d8f9e8` | — | — | `ReqCardLockCB` | `0x00f65c8c` | — | `SetCardLock` `0x00ae9a9c` |
| `card_handler/SetLeader` | `01d8fa00` | — | — | — | — | — | deck leader |

### Two structural facts that constrain every fixture **[RECOVERED]**

1. **`LEVEL_UP_PARAM` / `RANK_UP_PARAM` / `SKILL_UP_PARAM` are passed *by value* into
   `std::function`.** A by-value `std::function<void(P)>` sink is only satisfiable by a
   **default-constructible, copyable plain struct** — these are *not* `json` subobjects.
   Consequence: **the callback can be invoked with a default-constructed PARAM** if the
   response is empty. That is why an empty `ret_data` will not crash here, and it is also
   why an empty `ret_data` will silently produce a **zero-value** result popup. Do not treat
   "no crash" as "correct".
2. **`ReqSkillUpCB` / `ReqMultiSkillUpCB` sinks are `void(int, SKILL_UP_PARAM const&)`** —
   an `int` precedes the param. **[UNKNOWN]** whether that `int` is a result code, a count,
   or an index. `ReqMultiSkillUpCB` carries the assert string
   `vMultiSkillUpInfo has not any element` (`01d8f75c`), i.e. **it asserts the response
   contains a non-empty element list**, so an *empty* multi-skill-up response will trip
   that assertion.

---

## 3. Complete `.rodata` literal inventory for the `CSRSyncCard` TU **[RECOVERED as literals]**

`.rodata` window `0x01d8f71b … 0x01d8f8c8` is the whole gym TU. Every printable literal in
it, classified:

| addr | literal | classification |
|---|---|---|
| `01d8f71b` | `source_inst_list` | **request field** (candidate: `/gym/LevelUp` or `/world/ConfirmPMKey` — ambiguous, see §4) |
| `01d8f72c` | `/gym/LevelUp` | route |
| `01d8f739` | `/gym/RankUp` | route |
| `01d8f745` | `skill_idx` | request field → `/gym/SkillUp` |
| `01d8f74f` | `/gym/SkillUp` | route |
| `01d8f75c` | `vMultiSkillUpInfo has not any element` | **assert tag** for `ReqMultiSkillUpCB` |
| `01d8f782` | `RequestMultiSkillUp` | function-name string |
| `01d8f796` | `mulit_skill_up_count` | **response key candidate** (sic — typo in the original) |
| `01d8f7ab` | `/gym/MultiSkillUp` | route |
| `01d8f7bd` | `/gym/Overcome` | route |
| `01d8f7cb` | `src_rank` | request field → `/gym/RankUpBundle` |
| `01d8f7d4` | `/gym/RankUpBundle` | route |
| `01d8f7e6` | `part` | request field → `card_handler/RankUpEquipment` |
| `01d8f7eb` | `card_handler/LevelUpEquipment` | route |
| `01d8f809` | `source_inst_ids` | request field → `card_handler/RankUpEquipment` |
| `01d8f819` | `card_handler/RankUpEquipment` | route |
| `01d8f836` | `ReqLevelUpCB` | assert tag |
| `01d8f843` | `target_inst` | **response key candidate** (the instance that changed) |
| `01d8f84f` | `removed_inst_list` | **response key candidate** (fodder instances consumed) |
| `01d8f861` | `ReqRankUpCB` | assert tag |
| `01d8f86d` | `ReqSkillUpCB` | assert tag |
| `01d8f87a` | `skill_%u_level` | **printf key format** → builds `skill_1_level` … `skill_5_level` |
| `01d8f889` | `ReqMultiSkillUpCB` | assert tag |
| `01d8f8a4` | `skill_%s_level` | **printf key format**, `SRSKILL_TYPE` rendered as a string |
| `01d8f8aa` | `removed_card` | **response key candidate** (fodder card *ref ids* consumed) |
| `01d8f8b7` | `removed_inst_id_list` | **response key candidate** (fodder instance *ids* consumed) |

**The three `removed_*` / `target_inst` keys are the important finding.** They are exactly
the shape the community guide predicts: consume fodder, tell the client what went away.
Their presence is why the `skill_%u_level` format string matters — `SetCardSkillLevel`
takes `(inst_id, skill_type, level)` **values**, so `skill_%u_level` must be used to *read*
the per-slot level out of the response by formatted key.

---

## 4. Request fields — **[UNKNOWN]**, with adjacency candidates

Every `/gym/*` request also carries the standard envelope
`app_code=_SR app_ver=2801 market=<int> pvid=<int> otp=<string>` (see
`analysis/research/chest-rewards.md` §"Request").

| route | requester signature ⇒ implied fields | adjacency candidate **[not proof]** |
|---|---|---|
| `/gym/LevelUp` | `(unsigned long inst, vector<unsigned long> src, uchar)` | `inst_id`, `source_inst_list`, plus the `is_xxx` bool |
| `/gym/RankUp` | `(unsigned long inst, vector<unsigned long> src, uchar)` | `inst_id`, `source_inst_list` |
| `/gym/SkillUp` | `(unsigned long inst, SRSKILL_TYPE type, string)` | `inst_id`, **`skill_idx`**, a `string` (fodder selector?) |
| `/gym/MultiSkillUp` | `(unsigned long inst, vector<SRSKILL_TYPE>)` | `inst_id`, `mulit_skill_up_count`, `skill_%u_level`-family |
| `/gym/RankUpBundle` | `(uint, uint, uint, uint, uint)` | `inst_id`, **`src_rank`**, `target_rank`, `card_cnt`, `target_cnt` |
| `/gym/Overcome` | `(unsigned long, string, vector<unsigned long>)` | `inst_id`, `src_inst_id_list` |
| `gym/Awaken` | `(unsigned long, unsigned int, string)` | `inst_id`, `awake_step`/`target_step`, |
| `gym/AwakenOvercome` | `(unsigned long, unsigned int, string, vector<unsigned long>)` | **`target_inst_id`**, **`target_cnt`**, **`src_inst_id_list`** (`01d6f8e7`/`01d6f8f6`/`01d6f901`) |

> **Adjacency is not proof.** This project has already lost twelve rounds to
> plausible-but-wrong theories (`AGENTS.md` §16.7). The `.rodata` ordering
> "field, then route" holds for *some* pairs in this TU (`skill_idx` → `/gym/SkillUp`,
> `src_rank` → `/gym/RankUpBundle`, `part` → `card_handler/RankUpEquipment`) and is
> self-evidently wrong for others (`source_inst_list` sits between
> `/world/ConfirmPMKey` and `/gym/LevelUp` and could belong to either).
> **Do not ship a request-field name from this table.** To promote a row to
> **[RECOVERED]**, run the hardened resolver over the *Request\** function range and
> require the `ldr` to be the immediately preceding instruction of a real
> `bl` to the request-argument builder:
>
> ```
> python tools/resolve-literals-offline.py --function 0x00f53698:0x00f53f90   # LevelUp
> python tools/resolve-literals-offline.py --function 0x00f546f0:0x00f54fe8   # RankUp
> python tools/resolve-literals-offline.py --function 0x00f558e8:0x00f56074   # SkillUp
> python tools/resolve-literals-offline.py --function 0x00f566c8:0x00f5700c   # MultiSkillUp
> python tools/resolve-literals-offline.py --function 0x00f586e4:0x00f58da0   # GroupRankUp
> python tools/resolve-literals-offline.py --function 0x00f577b0:0x00f57f98   # Overcome
> ```
>
> And the *response* keys need the `Req*CB` ranges instead (`0x00f53f90:0x00f546f0`,
> `0x00f54fe8:0x00f558e8`, `0x00f56074:0x00f566c8`, `0x00f5700c:0x00f577b0`,
> `0x00f57f98:0x00f586e4`, `0x00f58da0:0x00f59380`).
>
> **This session had no shell, so none of those were run.** That is the single highest-value
> next action for the gym.

---

## 5. Response fixtures

### 5.1 What is safe today — **[UNKNOWN]**, minimal safe fixture

Because every `Req*CB` sink is a by-value struct or an `int`, and because nlohmann
`operator[]` on a missing key yields `null` (which `get<int>()`/iteration tolerate as a
zero-length range), the **smallest non-crashing answer is an empty object**:

```jsonc
// ALL /gym/* mutations, until §4 is resolved:
{ "result_code": 1, "ret_data": {} }
```

Do **not** send `[]` for a `/gym/*` mutation: `ReqMultiSkillUpCB`'s assert is on element
count, and a `[]` ret_data makes `ret_data["x"]` a type error on an array in every nlohmann
version this client links (see `AGENTS.md` §16.2 for the identical `type_error.305` failure
that killed the mission path). **`{}` is object-typed and therefore strictly safer than the
current `{mock:true, route, request_keys}`.**

### 5.2 Target shape once §4 is resolved — **[UNKNOWN]**, do not ship yet

The recovered key *inventory* (not the assignment) says a gym response must be able to
express all of:

```
target_inst          number   instance that was transformed
removed_inst_list    array    consumed fodder instances (objects)
removed_inst_id_list array    consumed fodder instance ids (numbers)
removed_card         array    consumed fodder card ref ids (strings)
removed_item         array    consumed item instances  <- `removed_item` @ 01d6fa74
skill_1_level .. skill_5_level   number, per-slot skill level
mulit_skill_up_count number    multi-skill-up echo (sic)
```

`removed_item` @ `01d6fa74` sits in the **card-instance** literal run
(`01d6f95c … 01d6fb79`), which is the run that also holds `regdate`, `rank`, `rank_up_cnt`,
`awaken`, `awk_step`, `awk_overcome`, `overcome_cnt`, `weapon_rank`, `weapon_level`,
`armor_rank`, `armor_level`, `accessory_rank`, `accessory_level`, `skill_1_level` …
`skill_5_level`. **[RECOVERED]** that run is the card-instance field set (see
`ascension.md` §3 for the full list). `removed_item` is therefore a card-instance key, i.e.
it belongs on the *changed instance record* the gym responses embed, not on `ret_data`.

### 5.3 Server-side state effects a correct fixture must have **[FIXTURE-design]**

These are *design* requirements, not recovered wire facts, but they are what makes the screen
behave:

- `/gym/LevelUp` → increment that instance's `level`, add `exp`, recompute stats.
- `/gym/RankUp` → increment `rank` (★) and `rank_up_cnt`; reset `level`/`exp` per game rules.
- `/gym/RankUpBundle` → same, for up to five instances at once (5-uint requester).
- `/gym/SkillUp` / `MultiSkillUp` → increment `skill_N_level` for the requested slots.
- all of the above → **remove** every inst id in the consumed-fodder list from the inventory.
- every one → return the changed instance record so `SetCardExp` / `SetCardRank` /
  `SetCardSkillLevel` land.

---

## 6. Reference tables the gym depends on — **[RECOVERED container types]**

From `analysis/ghidra-card-keys.txt` (resolved `ldr` sites, not guesses):

| route | parser | container | keys |
|---|---|---|---|
| `/reference/GetCardChain` | `CSRSyncRef::ReqCardChainCB` `0x00f84ce4` → `CSRCardInfoContainer::SetCardChain` `0x0087e110` | **OBJECT** — `ret_data["r" + <generated>]` | `target_rank`, `title`, `desc`, `related_list[]` → `effect` → `atk`, `def`, `hp` |
| `/reference/GetCardRankUp` | `ReqCardRankUpCB` `0x00f84ca0` → `SetCardRankUp` `0x0087ec9c` | **OBJECT** — `ret_data["e" + <generated>]` | `src_cnt`, `stat_bonus` |
| `/reference/GetCardEnhancePrice` | `ReqCardEnhancePriceCB` `0x00f84cc2` → `SetCardEnhancePrice` `0x0087f048` | **OBJECT** — `ret_data[<generated>]` | `level`, `rank` |
| `/reference/GetCard` | `ReqCardCB` `0x00f839f2` → `CSRCardInfoContainer::SetCard` `0x0087baa4` | **ARRAY**, keyed on `base.id` | `base{is_main, id, char_id, name, attr, role, res_prefix, is_source, source_field}`, `stat[]{type, rank, cool_time}`, `skill`, `dialog`, `dialog_id`, `target_rank`, `chain_id`, `equipment`, and the literal ids `902 903 904 912 913 914` |

`SetCard` reads **32** literals (all resolved). Note `902/903/904/912/913/914` — these are
the **skin/costume** reference ids (`analysis/catalogue/cards/9xx.md`), which is why the
four nameless `_1` costume variants (`026_1 034_1 038_1 086_1`) are **not** ascension
targets. See `ascension.md` §2.

The first three already return `{}` in `server-ts/src/game-routes.ts:309,313,318` — that is
correct and should not change.

---

## 7. Risk register

| risk | severity | detail |
|---|---|---|
| Shipping `ret_data: []` on a `/gym/*` mutation | **HIGH** | nlohmann `type_error.305`, no exception handler — same mechanism that killed the mission path (`AGENTS.md` §16.2). Use `{}`. |
| `mulit_skill_up_count` / `removed_*` element types guessed | **HIGH** | ints vs objects vs strings is unobservable from `.rodata`; a wrong element type is an immediate `type_error`. |
| Making `/gym/*` mutate server state before the shape is recovered | **MEDIUM** | the client will believe the level-up happened and re-render from a value the server never stored; that desync is worse than the current no-op. |
| Leaving `GYM`, `GYM_ACHIEVE`, `GYM_FIRST_ENTER` out of `completeTutorialList()` | **MEDIUM** | the Training building may stay gated. |
| Assuming all 15 `_1` card ids are ascension targets | **MEDIUM** | 4 of the 15 are skins. |