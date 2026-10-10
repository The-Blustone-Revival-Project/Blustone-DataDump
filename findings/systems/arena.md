# ARENA — PvP "Fight Club" (`/arena/*`)

Content-domain research spec. Read-only. Tags per `AGENTS.md` §15.

---

## 0. Blunt summary

| metric | value |
|---|---|
| `/arena/*` routes in `.rodata` | **12** |
| currently `mock:true` | **10** |
| currently aliased to the expedition fixture | **2** (`BattleStart`, `BattleComplete`) — **flagged as wrong, see §6** |
| parser functions located & addressed | **18** (best-documented of the four systems) |
| **response key sets recovered** | **0 assigned** / **40 keys inventoried** |
| container types recovered | **2** (both "arrays") |

The arena is the only one of the four systems with a **complete, named, addressed parser
family** — `CSRFCPlayData` has one `Parse*` per route. Nobody has decompiled them, but the
map from route → parser → container is already unambiguous, which makes this the cheapest
of the four to finish.

---

## 1. What the system is (community guide)

`Blustone Guide FAQ.md` — the PvP mode is called **Fight Club** (FC), colloquially "Arena":

- §Glossary L39/L55/L77 — "Attacker team in **Fight Club**", "Defensive **Fight Club**
  set-up", "time-out win against users who fight versus these decks in the **Fight Club**
  or Blitz".
- §Q4 L113 — "they can **camp** you over and over again in the Arena".
- §Q6 L133 — "If you want to have your enemy **risk his ticket** by overpowering him…" ⇒
  **entering a fight consumes a ticket**; the ticket count is a first-class player field.
- §Q16 L235 — "spare **fight club chips**"; the FC shop sells "the golden materials
  (those with a yellow trim around them) or 4* traces".
- §Q24 L440/L443 — guild join requires "a certain score in the **Fight Club** … from 0 up to
  4,000 points", and "Contributions are made through participation in the Fight Club
  (each **win guarantees you 300 points, while defeats are 250**)". ⇒ **arena rating feeds
  guild admission**, and the native guild record has exactly the keys
  `fc_point_limit` / `fc_point` (`01d78c5f`, `01d78cd6`). **Cross-system link confirmed.**
- §Q12 L201 — "World's Fight Club Championship" is a seasonal event ⇒ seasons exist.

**What the fixture must therefore model:** a rating number, a season, a defence list, a
rival list, revenge state per defence record, a rival-refresh price, and a weekly reward
cycle. It does **not** need real PvP: the battle itself is client-side (see `AGENTS.md`
§16.3 — a battle window is three dispatches and then zero server traffic).

---

## 2. Routes and parsers — **[RECOVERED]**

Owner classes: **`CSRFCPlayData`** (instance data) and **`CSRFCInfo`** (reference data).
`FC` = Fight Club. Evidence: `analysis/native-evidence.tsv:9937-9982`.

| route | literal @ | parser | addr | container it fills |
|---|---|---|---|---|
| `/arena/Enter` | `01d8f8cc` | `CSRFCPlayData::ParseEnter(json const&)` | `0x00942c3c` | the whole `LEAGUE` struct |
| — | | `CSRFCPlayData::ParseSeason(json const&)` | `0x00942e24` | season block |
| — | | `CSRFCPlayData::ParseUser(json const&)` | `0x009430f8` | `BATTLE_USER` (me) |
| `/arena/GetMyRank` | `01d8f920` | `CSRFCPlayData::ParseMe(json const&)` | `0x00946994` | my rank row |
| `/arena/GetGlobalRankList` | `01d8f93c` | `CSRFCPlayData::ParseWorldRanking(json const&)` | `0x00945e9c` | **`std::list<BATTLE_ENEMY>::resize(uint)`** ⇒ ARRAY |
| `/arena/GetFriendRankList` | `01d8f955` | `CSRFCPlayData::ParseFriendRanking(json const&)` | `0x0094616c` | list ⇒ ARRAY |
| `/arena/PrevSeasonRanking` | `01d8f96e` | `CSRFCPlayData::ParsePrevRanking(json const&)` | `0x00946568` | list ⇒ ARRAY |
| `/arena/GetDefenseList` | `01d8f90a` | `CSRFCPlayData::ParseDefender(json const&)` | `0x00943958` | `BATTLE_ENEMY` |
| — | | `CSRFCPlayData::ParseDefenseRecords(json const&)` | `0x0094570c` | **`std::list<BATTLE_DEFENSE_RECORD>::resize(uint)`** ⇒ ARRAY |
| — | | `CSRFCPlayData::ParseDefenseRecord(json const&)` | `0x00945a28` | one defence record |
| `/arena/FindRival` | `01d8f9c3` | `CSRFCPlayData::ParseFindRival(json const&)` | `0x00947318` | `BATTLE_ENEMY` |
| `/arena/RefreshRival` | `01d8f9d4` | `CSRFCPlayData::ParseRefreshRival(json const&)` | `0x00947540` | `BATTLE_ENEMY` |
| — | | `CSRFCPlayData::ParseRefreshCost(json const&)` | `0x009476bc` | `refresh_price` |
| `/arena/BattleStart` | `01d8f8d9` | `CSRFCPlayData::ParseTargetEnemy(json const&)` | `0x009438d8` | opponent `BATTLE_ENEMY` |
| — | | `CSRFCPlayData::ParseFreindlyBattleRival(json const&)` *(sic)* | `0x00944790` | `/world/GetFriendlyBattleInfo` |
| `/arena/BattleComplete` | `01d8f8f4` | `CSRFCPlayData::ParseBattleResult(json const&)` | `0x00944e68` | result + card exp |
| — | | `CSRFCPlayData::ParseBattleResultLog(json const&)` | `0x00944d40` | `RESULT_LOG` |
| — | | `CSRFCPlayData::ParseApBp(json const&)` | `0x00943750` | AP/BP deltas |
| `/arena/WeeklyReward` | `01d8f9a7` | `CSRFCPlayData::ParseReward(json const&)` | `0x00946a2c` | `SRREWARD_INFO` |
| `/arena/SaveComment` | `01d8f994` | *(no parser retained)* | — | **[UNKNOWN]** |
| *(reference)* | | `CSRFCInfo::ParseBattleLeague(json const&)` | `0x00948438` | `std::vector<CSRFCInfo::LEAGUE_INFO>` ⇒ ARRAY |
| *(reference)* | | `CSRFCInfo::ParseBattleWeeklyRwd(json const&)` | `0x00948b48` | weekly reward table ⇒ ARRAY |

Supporting:
- `CSRFCPlayData::GetEnemyByPVID(unsigned long, unsigned char) const` `0x0094266c`
- `CSRFCPlayData::MakeMyInfoToEnemy() const` `0x009447d8` — the client builds its own
  "enemy" copy of itself for defence display; **the defence list the player sees is partly
  client-generated.**
- `CSRFCPlayData::SetDefenseLogToCanNotRevange(unsigned, unsigned char)` `0x009478f4`
- `CSRFC::GetLeagueDesc(CSRFCPlayData::LEAGUE&)` `0x0094798c`, with the guard string
  `CSRFCPlayData::LEAGUE is not availd` (`01d73533`).

### 2.1 Proven cross-check: `/lobby/Enter` already carries arena state **[RECOVERED]**

`CSRSyncGlobal::ParseUserDatailInfo` (`0x00f6e240`, keys resolved in
`analysis/ghidra-userdetail.txt`) reads **`league_level`, `rating_point`, `prev_rank`,
`win_message`, `lose_message`** off `ret_data`. Four of those five literals reappear
verbatim inside the `CSRFCPlayData` `.rodata` cluster (§3) — i.e. **the arena state is
duplicated at the top level of `/lobby/Enter`.** `server-ts/src/bootstrap.ts:103-109`
already publishes `league_level: 1, rating_point: 0` via `partyProfile()`. That is correct
and is the reason the Arena tab can open at all. **Do not remove it.**

---

## 3. The arena key cluster — **[RECOVERED as literals, 0 assignments]**

`.rodata` window `0x01d73290 … 0x01d73591`. Note `rival` / `is_user_win` / `card_id` at
`01d70d29` are **chat** literals (`SRChatModule.cpp` is at `01d71094`) — **false leads, do
not use them.**

```
rival_pvid                          defense
can-not-exist-bonus-data (msg)       complete_datetime
arena                               is_win
status                              is_friendship
season                              is_revenge
battle                              delta_rating_point
is_weekly_reward                    bid
combat_info                         revenged
defense_list                        tried_revenge
season_no                    01d73328   CSRFCPlayData::LEAGUE is not availd
rating_point               01d73328   GetLeagueDesc
win                        01d73335   defense_id
lose                       01d73339   max_win
country                    01d7333e   min_ranking
nick                       01d73346   max_ranking
img                        01d7334b
arena_prev_ranking        01d7334f
weekly_no                  01d73362
start_datetime             01d7336c
next_datetime              01d7337b
weekly_start_datetime      01d73389
weekly_end_datetime        01d7339f
weekly_next_datetime       01d733b3
league_level               01d733c8
league_win                 01d733d5
refresh_datetime           01d733e0
start_message              01d733f1
win_message                01d733ff
lose_message               01d7340b
ranking                    01d73418
rival_list                 01d73420
refresh_price              01d7342b
chain_bonus                01d73439
card_book                  01d73445
thumbnail                  01d7344f
user_exp                   01d73459
inst_                      01d73462   <- format prefix, builds inst_1..inst_5
```

**40 keys.** Two things are worth calling out:

1. **`inst_` at `01d73462` is a key *prefix***, exactly like `skill_%u_level` in the gym TU
   and `inst_id_` / `ref_id_` in `ParseUserDatailInfo`. The arena deck is the same
   five-slot structure. **[RECOVERED]** that the concatenation happens; **[UNKNOWN]** the
   exact suffix format.
2. **`defense` and `defense_list` and `arena_prev_ranking` and `ranking` and `rival_list`
   are five different container keys.** `ParseWorldRanking`/`ParseFriendRanking`/
   `ParsePrevRanking`/`ParseDefenseRecords` each resize a `std::list`, so all five are
   **JSON arrays**. This is the strongest container statement in this document.

Recover the assignments with one resolver pass per parser (the ranges are contiguous and
non-overlapping):

```
for p in 0x00942c3c 0x00942e24 0x009430f8 0x00943750 0x009438d8 0x00943958 \
         0x00944790 0x00944d40 0x00944e68 0x0094570c 0x00945a28 0x00945e9c \
         0x0094616c 0x00946568 0x00946994 0x00946a2c 0x00947318 0x00947540 \
         0x009476bc 0x00948438 0x00948b48 ; do
  python tools/resolve-literals-offline.py --function $p:$((p+0x400))
done
```

**This session had no shell; none were run.**

---

## 4. Request fields — **[UNKNOWN]**, adjacency candidates only

Envelope: `app_code=_SR app_ver=2801 market=<int> pvid=<int> otp=<string>`.

`.rodata` request TU window `0x01d8f8cc … 0x01d8f9e8`:

| addr | literal | immediately precedes | verdict |
|---|---|---|---|
| `01d8f8ec` | `atk_max` | `/arena/BattleComplete` (`01d8f8f4`) | **strong** — "max attack reached" is a *result*, not a request. `/arena/BattleComplete` → `atk_max` |
| `01d8f931` | `page_scale` | `/arena/GetGlobalRankList` (`01d8f93c`) | **strong** — paging, and `CSRGuild::RequestRank(uint, int, int, …)` uses the same idea |
| `01d8f987` | `comment_info` | `/arena/SaveComment` (`01d8f994`) | **strong** |
| `01d8f9bb` | `is_auto` | `/arena/FindRival` (`01d8f9c3`) | **strong** |

`page_scale` appears once for three rank-list routes, which is consistent with all three
sharing one paging helper. `/arena/BattleStart` has **no** adjacent unique literal; its
target is almost certainly a shared `target_pvid` / `rival_pvid` key.

**`atk_max` is the important one.** It is the first recovered arena *result* field, and it
sits in the same family as the `play_info` blob that `/mission/Complete` sends
(`analysis/research/battle-lifecycle.md` §5). Expect `/arena/BattleComplete` to use a
**JSON-string `play_info`-style blob or a flat object of result counters**, with `atk_max`
as one of its keys. **[UNKNOWN]** which.

---

## 5. Response fixtures

### 5.1 Safe, shippable today

**Ranking / list routes — send `[]`.** `ParseWorldRanking` et al. do
`list<…>::resize(uint)` on an `unsigned` taken from the payload; `[]` gives `0`, the loop
body never runs, the callback fires with an empty list. This is the same
"empty array is a valid answer" rule that already fixed `/relation/GetList`
(`server-ts/src/game-routes.ts:268-273`).

```jsonc
// ALL of:
{ "result_code": 1, "ret_data": [] }   // GetGlobalRankList, GetFriendRankList,
                                       // PrevSeasonRanking, GetDefenseList
```

**Single-record routes — send `{}`.** `ParseEnter`, `ParseMe`, `ParseFindRival`,
`ParseRefreshRival`, `ParseTargetEnemy`, `ParseRefreshCost`, `ParseReward` each take one
`json const&` and index it by name. `{}` makes every index `null`, every `get<>` yield the
type's zero value, and the callback fire.

```jsonc
{ "result_code": 1, "ret_data": {} }   // Enter, GetMyRank, FindRival, RefreshRival,
                                       // BattleStart, WeeklyReward, SaveComment
```

**`/arena/WeeklyReward`** should reuse the already-validated reward idiom from
`analysis/research/chest-rewards.md` §"Per-route spec", because its sink is
`SRREWARD_INFO`:

```jsonc
{ "result_code": 1, "ret_data": {
    "gold":   { "prev": 0, "cur": 0 },
    "free_iap": { "cur": 0 },
    "iap":    { "cur": 0 },
    "card":   [],
    "item":   [],
    "supply": 0
} }
```
`achievement` must be **omitted or `null` — never `[]`** (there is an explicit
`value_t` IS-NULL test).

> These two rules are strictly better than today's fallback, which for `/arena/*` injects
> `{ mock:true, route, request_keys, list:[], users:[] }` — an **object** where the client
> wants an array, with two invented keys. An object where a `resize(uint)` is applied is a
> `type_error`, i.e. the §16.2 crash class.

### 5.2 Target shape — the one that makes the Arena screen real **[INFERRED, one pass away]**

`/arena/Enter`, using the §3 inventory. **Every key is a real literal; the *grouping* is
inferred.** Confidence: medium-high, because `ParseEnter`/`ParseSeason`/`ParseUser` are
three separate functions over three separate structs, so a single flat object is more
likely than three nested ones:

```jsonc
{ "result_code": 1, "ret_data": {
    "arena":      { "status": 0 },
    "season":     { "season_no": 1, "start_datetime": 0, "next_datetime": 0 },
    "battle":     { "league_level": 1, "rating_point": 0, "league_win": 0,
                    "refresh_datetime": 0, "refresh_price": 0,
                    "start_message": "", "win_message": "", "lose_message": "" },
    "weekly":     { "is_weekly_reward": 0, "weekly_no": 0,
                    "weekly_start_datetime": 0, "weekly_end_datetime": 0,
                    "weekly_next_datetime": 0 },
    "ranking":       [],
    "rival_list":    [],
    "defense_list":  [],
    "arena_prev_ranking": [],
    "combat_info":   {},
    "card_book":     [],
    "chain_bonus":   {},
    "nick": "", "country": "", "img": "",
    "user_exp": 0, "win": 0, "lose": 0
} }
```

**Recommendation: ship §5.1 first, measure, then ship §5.2 as a single A/B with
`BLUSTONE_ARENA_ENTER_SHAPE=1`.** The risk of the nested form is that `ParseEnter` may index
`ret_data["league_level"]` at the top level instead; if the first test shows the season
header blank and `league_level` 0 despite `/lobby/Enter` publishing 1, that is the
diagnosis, and the fix is to hoist the five scalars to the top level — the same "send both
forms" hedge `server-ts` already uses for `/reference/GetArea`
(`AGENTS.md` §11, top-level + nested `stage[]`).

### 5.3 Defensive list, semantically **[FIXTURE-design]**

A `BATTLE_DEFENSE_RECORD` needs (guide §Q4 L113 camping, §Q6 L133 tickets):
`complete_datetime`, `is_win`, `is_friendship`, `is_revenge`, `revenged`,
`tried_revenge`, `delta_rating_point`, `defense_id`, `nick`, `country`, `img`,
`user_exp`, `thumbnail`, and the deck as `inst_1..inst_5`.
`CSRFCPlayData::MakeMyInfoToEnemy()` means **one defence record can be synthesised from the
player's own card instances** — a single self-defence record is enough to make the screen
non-empty, and it requires no second account.

---

## 6. 🔴 FLAG: `/arena/BattleStart` and `/arena/BattleComplete` are wired to the wrong handler

`server-ts/src/game-routes.ts:247-248`:

```ts
if (route === "/arena/BattleStart")   return state.startMission(payload, headers);
if (route === "/arena/BattleComplete") return state.completeMission(payload, headers);
```

This is honestly labelled in `server-ts/src/openapi.ts:471-478` as a local alias, and
`server-routes-triage.md` does not contradict it — but it is **wrong in a way that will
bite**, and it should be replaced rather than kept:

1. It makes the arena award **expedition** rewards (gold, mission clear, AP cost) for a PvP
   win. `/mission/Complete` writes `cleared_stage_ids` and pays stage gold — arena wins
   must not touch the campaign progression.
2. `/arena/BattleComplete` almost certainly takes **`atk_max`** (§4). `startMission` /
   `completeMission` know nothing about it, so the arena rating can never move.
3. It hides the fact that the arena has **its own** result parser
   (`CSRFCPlayData::ParseBattleResult` `0x00944e68`), which — per
   `analysis/ghidra-enemycamp-refs-01.txt:53` — is *also* a caller of `SetCardExp`
   (`0x00ae98a0`), i.e. **arena battles grant card exp too**.

**Recommendation:** give `/arena/BattleStart` and `/arena/BattleComplete` their own thin
handlers that (a) echo `atk_max`, (b) update only `rating_point` / `win` / `lose` /
`league_win` / `delta_rating_point`, and (c) **do not** touch `cleared_stage_ids`. Keep
the seam, drop the alias. That is a strictly larger change than the other recommendations
here, so it is last in the order, not first.

---

## 7. Risk register

| risk | severity | detail |
|---|---|---|
| Sending an **object** where the client calls `list::resize(uint)` | **HIGH** | `type_error.305` with no handler → SIGSEGV. All five list routes must be `[]`, not `{}`. Today they are `{mock:true,…,list:[],users:[]}` — an object. **This is a latent crash, not just a cosmetic mock.** |
| `/arena/BattleStart` crediting campaign progression | **HIGH** | economy corruption, not a crash. |
| Shipping the nested `/arena/Enter` form without a flag | **MEDIUM** | could read as all-zeros; recoverable, but confusing. |
| `achievement: []` in a reward response | **MEDIUM** | explicit IS-NULL test; `[]` parses it as a `/dailyquest/GetInstList` request. Already documented in `chest-rewards.md`. |
| Inventing a rival pvid that has no `BATTLE_USER` | **MEDIUM** | `GetEnemyByPVID` is a lookup; a miss leaves the opponent panel blank. Self-defence (§5.3) avoids this entirely. |
| `inst_` suffix format guessed wrong | **MEDIUM** | the defence deck renders empty; recoverable. |