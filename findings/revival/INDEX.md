# `analysis/systems/` — content-domain specs for Gym, Ascension, Arena, Guild

Written by the content-domain research agent, 2026-10-03. **Read-only** over
`server-ts/`, `analysis/ghidra-project/`, `analysis/*.txt`, `analysis/catalogue/`,
`analysis/recovered-data/`, `instrumentation/`, `recovered-assets/`.
No adb, no Ghidra session, no Docker, no server, no git.

Provenance tags throughout, per `AGENTS.md` §15:
**[RECOVERED]** = function+address or file:line ·
**[FIXTURE]** = local compatibility data · **[UNKNOWN]** = not recoverable from what is on disk.

---

## 0. The blunt numbers

| system | routes in scope | `mock:true` today | non-mock today | parsers located & addressed | **response shapes recovered** | container types recovered |
|---|---|---|---|---|---|---|
| **Gym** | 14 | **14** | 0 | 10 | **0** | 0 |
| **Ascension** | 7 (own) | **7** | 0 | 13 | **0** | **4** |
| **Arena** | 12 | **10** | 2 (wrongly aliased) | **20** | **0** | **2** |
| **Guild** | 30 | **29** | 1 | **29** | **1** (six-key `GetGuildInfo` container) | **4** |
| total | **63** | **60** | 3 | **72** | **1** | **10** |

**One of 63 routes has a recovered shape.** That is the honest headline, and it is *not*
because the evidence is thin — it is because **72 parser functions have been located and
addressed and approximately zero have been decompiled.** The bottleneck is Ghidra time, not
knowledge. §4 turns that into a work queue.

### Session limitation, stated up front

**This agent had no shell**, so `tools/native-grep.py` and
`tools/resolve-literals-offline.py` could not be run. Every conclusion here comes from
reading `analysis/native-all-strings.tsv`, `analysis/native-evidence.tsv`,
`analysis/ghidra-*.txt`, `analysis/research/*`, the catalogue, and the community notes.
Consequently:

- **Function identities, addresses, mangled signatures, STL container types, and literal
  inventories are [RECOVERED]** — they are read directly off the evidence tables.
- **Key→function assignments are [UNKNOWN]** — those need the resolver, and I could not run it.
- Adjacency-based guesses ("the literal before a route literal is its request field") are
  labelled **[candidate, not proof]** everywhere they appear. This project has lost twelve
  rounds to plausible-but-wrong theories (`AGENTS.md` §16.7). Do not promote one to
  [RECOVERED] without a resolver pass.

---

## 1. Files

| file | system | priority |
|---|---|---|
| [`gym.md`](gym.md) | Gym / Training (`/gym/*`, `card_handler/*`) | **1** |
| [`ascension.md`](ascension.md) | Transcendence + Awakened Transcendence + Overcome | **1** |
| [`arena.md`](../systems/arena.md) | Arena / "Fight Club" (`/arena/*`) | 2 |
| [`guild.md`](../systems/guild.md) | Guild (`/guild/*`, `/lobby/GetGuildInfo`, `/reference/GetGuild*`) | 3 |

Build on, do not redo: `analysis/research/server-routes-triage.md` (route census),
`analysis/research/mail-social.md` (mail/social contracts),
`analysis/research/chest-rewards.md` (the validated `SRREWARD_INFO` response idiom),
`analysis/research/training-supply.md` (first-pass gym/supply vocabulary — **superseded**
by `gym.md` for routes and callbacks, and wrong on `gym/Awaken`: it lists
`gym/AwakenOvercome` at `01d6f951` and `gym/Awaken` at `01d6f912`; the table says the
reverse. `gym.md` §2 is correct.)

---

## 2. The three findings that change what should be built

### 2.1 🔴 Three ascension systems, not one

The brief calls this "Transcendence/Awakening". The native evidence has **three** distinct
systems with three player fields, three routes and three reference tables:

| system | field | route | reference | scene |
|---|---|---|---|---|
| Transcendence (★) | `rank`, `rank_up_cnt` | `/gym/RankUp`, `/gym/RankUpBundle` | `GetCardRankUp`, `GetCardChain` | `SR_TRAINING_HYPER` |
| Awakened Transcendence | `awk_step`, `awk_overcome` | `gym/Awaken` | `GetCardAwaken` | `SR_TRAINING_AWAKE_HYPER` |
| Overcome | `overcome_cnt` | `/gym/Overcome`, `gym/AwakenOvercome` | `GetCardOvercome` | shares the Awake screen |

Collapsing them is the most likely way to get this wrong. Detail: `ascension.md` §0.

### 2.2 🔴 It is **11** awakened cards, not 15 — and the other 4 are costumes

`analysis/catalogue/data/card-catalogue.tsv` has 15 `_1` rows:

- **11 awakened hunters** — `004_1 005_1 009_1 010_1 011_1 017_1 019_1 020_1 021_1 024_1 056_1`
  (EN name literally `"(Awakened)"`, rarity 5).
- **4 costume/skin variants** — `026_1 034_1 038_1 086_1` (EN name **empty**, rarity
  **empty**, `owner_card_id` = `026/034/038/086`).

**Independent confirmation:** community guide §Q26 L493-502 lists the recommended
awakening order as Vincent › Genovia › Balian/Lapis/Rebecca · Gerard/Captain › Hecate ›
Riko · Tyltyl · Sienna — **exactly those 11**. Eleven, no more.

Publishing all 15 as ascension targets would make `CSRAwake::HasAwake("026_1")` lie.
The four costumes belong to `/reference/GetSkinRef`.

### 2.3 🔴 The single highest-value reconciliation: `target_cnt`

Community guide, `all-tables.json:46301`:

> **"You need %d of the same hunter for Awakened Transcendence."**

`CSRAwake` `.rodata`, in address order:

```
01d6f8e7  target_inst_id
01d6f8f6  target_cnt           <-- the %d
01d6f901  src_inst_id_list
01d6f912  gym/AwakenOvercome
01d6f8a0  Card AwakeOvercome is 3      <-- three tiers, matches guide A1/A2/A3
```

and `CSRAwake::RequestAwakeOvercome(unsigned long, unsigned int, string const&,
vector<unsigned long> const&, function<void(int)>)` `0x0085e37c` takes exactly
`(target_inst_id, target_cnt, string, src_inst_id_list)`.

This is the **only** request-field set in the gym/ascension area whose members are
contiguous with the route literal *and* semantically forced by a player-facing string in the
same translation unit. Promote with
`python tools/resolve-literals-offline.py --function 0x0019ec65:0x0019ee7c`.

---

## 3. Contradictions between sources — flagged, as requested

| # | contradiction | verdict |
|---|---|---|
| 1 | **Go reference server vs native:** the colleague's working server has **no guild code in the excerpt** (header line 3 lists guild among removed sections), yet line 78 references `dbGuildInactiveSweep` — a guild inactivity auto-disband. | **The Go file is no evidence either way.** It *does* implement guilds; the code was withheld. Loud, because "the working server doesn't do guild" is the wrong conclusion and would kill the whole subsystem. |
| 2 | **Guide vs native on guild join score:** guide says the FC score gate is 0–4000; native has `fc_point_limit`/`fc_point` on the guild INFO. | **Agree.** But it means **arena rating feeds guild admission** — the two systems are not independent and `fc_point` must be kept in sync with `rating_point`. |
| 3 | **Guide vs native on transcendence count:** guide "up to 3 times"; native `Card AwakeOvercome is 3`. | **Agree**, and note they are *different counters* (`rank` vs `awk_step`) that both cap at 3. |
| 4 | **Brief vs evidence:** "15 cards have `_1` variants" ⇒ ascension. | **Refuted.** 11 + 4 costumes (§2.2). |
| 5 | **Brief/prior note vs table:** `analysis/research/training-supply.md:37` places `gym/AwakenOvercome` at `01d6f951` and `gym/Awaken` at `01d6f912`; the table says `01d6f951 = gym/Awaken`, `01d6f912 = gym/AwakenOvercome`. | **The table is right**; the prior note transposed them. |
| 6 | **Existing server code vs native:** `game-routes.ts:525` injects `{list:[], users:[]}` for `/guild/gvg/arena/relation/` — an **object** where nine guild routes and three arena routes feed a `std::list::resize(uint)`. | **Latent crash, not a cosmetic mock.** Same class as `AGENTS.md` §16.2. Highest-value cheap fix in this whole spec. |
| 7 | **Existing server code vs native:** `game-routes.ts:247-248` aliases `/arena/BattleStart`/`BattleComplete` onto `/mission/Start`/`Complete`. | **Wrong, and economically dangerous** — it credits campaign `cleared_stage_ids` and stage gold for a PvP win, and cannot move `rating_point` because it does not know `atk_max`. Replace with thin handlers. |
| 8 | **`hyper` is a false friend.** `01d74af3 hyper` sits in the *actor/AI tuning* block (`MODULE_ACTOR`, `recovery_natual`, `sp_max`, `atk_spd`). `01d7ac50 awake_hyper` sits in a stage/scenario block. | **Neither is the Transcendence key.** Do not build a fixture on either. This is the §16.6-item-8 trap (`/reference/GetLevel` is AI tuning) recurring. |
| 9 | **`rival` is a false friend.** `01d70d29 rival`, `is_user_win`, `card_id` sit between `chat_option`/`guild_chat` and `SRChatModule.cpp` (`01d71094`). | **Chat literals, not arena.** Do not use. |

---

## 4. Recommended implementation order

Ordered by *visible player outcome ÷ risk*. Each step is independently shippable and
independently revertible. Steps 1-4 are **container fixes only** — they change no field
name, so they cannot be wrong in the way a guessed key is wrong.

### Step 1 — `/lobby/GetGuildInfo`: the one recovered shape **[DO FIRST]**
Six keys, six parsers of the same name (`my_guild`/`ParseMyInfo`, `guilds`/`ParseGuilds`,
`user_guilds`/`ParseUserGuild`, `applicants`/`ParseApplicants`,
`fuel_requests`/`ParseFuel`, `guild_notifications`/`ParseNoties`).
`fuel_requests: {}` is the safe answer under both candidate containers.
**Tester:** open the village → Guild. Expect a guild screen with an empty member list and
a "create / search / recommended" prompt, **no assertion, no `Cannot find` spam, no crash.**

### Step 2 — arena container split (5 minutes, 10 routes)
`[]` for `GetGlobalRankList`, `GetFriendRankList`, `PrevSeasonRanking`, `GetDefenseList`,
`GetChattingLog`-equivalent lists; `{}` for the single-record routes. This removes the
`{mock:true,…,list:[],users:[]}` object from ten `std::list` consumers.
**Tester:** Arena tab → each sub-tab. Expect empty lists and a reachable "no data" state
where there previously would have been a fault. **Watch logcat for `type_error` and for
`ASSERTION` — the count must not increase.**

### Step 3 — the remaining guild container split (24 routes)
`[]` for the nine `std::list` routes; `{}` for `GetFuelRequests`, `GetDetailInfo`, and the
single-record mutations. **Leave `/guild/GetNotifications` as `envelope([])` — it is already
correct.**
**Tester:** Guild → Applicants / Ranking / Search / Notifications. Each must render an
empty state, not a fault.

### Step 4 — ascension reference tables → `{}`
`/reference/GetCardAwaken` and `/reference/GetCardOvercome` from
`{mock,route,request_keys,list:[],items:[]}` to `{}`. `FindAwakeRef` is a
`std::map<std::string, std::vector<shared_ptr<REF>>>::find` — an array is the wrong shape
outright, and the injected `list`/`items` keys are meaningless to it.
**Tester:** card detail → Transcend tab. Expect "no rows" instead of an empty list; no
new assertions. (`FindAwakeRef` misses are silent, so a *screenshot* is the only oracle.)

### Step 5 — `/arena/Enter` full key set, behind a flag
The 40-key inventory in `arena.md` §3. Send it **behind
`BLUSTONE_ARENA_ENTER_SHAPE=1`**, and send `league_level`/`rating_point` **both** nested
and at the top level (the `GetArea` precedent, `AGENTS.md` §11).
**Tester:** Arena tab. Expect: a season number, a league badge, a rating of 0, and empty
Global/Friend/Defence lists. **Diagnostic:** if the header is blank while `/lobby/Enter`
still reports `league_level: 1`, the parser reads the top level — hoist and re-test.

### Step 6 — decompile queue (this is where the real answers are)
One resolver/Ghidra pass each, in this order. Each unblocks a whole screen.

| # | function range | unlocks |
|---|---|---|
| 1 | `0x0085d494:0x0085d54c` `CSRAwake::FindAwakeRef` | the `(birthrank, hyper)` composite **key format** → the entire awaken reference table |
| 2 | `0x00f53f90:0x00f546f0` `CSRSyncCard::ReqLevelUpCB` | the gym response shape; then `0x00f54fe8:0x00f558e8` RankUp, `0x00f56074:0x00f566c8` SkillUp, `0x00f5700c:0x00f577b0` MultiSkillUp, `0x00f57f98:0x00f586e4` Overcome, `0x00f58da0:0x00f59380` GroupRankUp |
| 3 | `0x00a6a384:0x00a6b340` `CSRGuild::ParseGuild` + `ParseMembers` | settles guild INFO Reading A vs Reading B (`guild.md` §7.3) |
| 4 | `0x00942c3c:0x00942e24` `CSRFCPlayData::ParseEnter` + `ParseSeason` | settles the arena nesting question for step 5 |
| 5 | `0x00f53698:0x00f53f90` etc. — the six `CSRSyncCard::Request*` **request builders** | gym *request* field names (`gym.md` §4) |

Each is a **contiguous, non-overlapping range** and the hardened resolver accepts
`--function 0xSTART:0xEND`. None needs the Ghidra project lock.

### Step 7 — `/arena/BattleStart` / `BattleComplete` un-aliasing
New thin handlers: echo `atk_max`, update only `rating_point`/`win`/`lose`/`league_win`/
`delta_rating_point`, **never** touch `cleared_stage_ids`. Do this *after* steps 1-5 so a
regression is attributable.

### Step 8 — tutorial gates
Add `GYM`, `GYM_ACHIEVE`, `GYM_FIRST_ENTER` (literals `01d9049a`, `01d90502`, `01d90575`)
to `completeTutorialList()` in `server-ts/src/game.ts`.
**Tester:** the village Training building must be enterable without a tutorial popup.

---

## 5. Things I would *not* do

- **Do not** make any `/gym/*` or ascension mutation mutate server state before step 6. The
  client will re-render from a value the server never stored; that desync is worse than
  today's honest no-op.
- **Do not** guess the `map<unsigned,…>` key names (`GetFuelRequests`, guild member
  detail). `{}` is safe; a wrong key is silently inert.
- **Do not** publish `026_1 034_1 038_1 086_1` as ascension targets.
- **Do not** send `ret_data: []` to any `/gym/*` mutation (object-typed sinks; and
  `ReqMultiSkillUpCB` asserts on element count).
- **Do not** send `achievement: []` in any reward-shaped response — there is an explicit
  `value_t` IS-NULL test (`analysis/research/chest-rewards.md`).
- **Do not** treat "no crash" as "correct". Every by-value `PARAM` sink means an empty
  `ret_data` invokes the callback with a **zero-valued** result and renders a plausible-
  looking wrong popup. The screenshot is the oracle, not the assertion count.

---

## 6. Method notes for whoever picks this up

1. **Adjacency is not proof.** The `.rodata` "field, then route" ordering is real
   (`skill_idx`→`/gym/SkillUp`, `src_rank`→`/gym/RankUpBundle`, `page_scale`→
   `/arena/GetGlobalRankList`, `comment_info`→`/arena/SaveComment`, `is_auto`→
   `/arena/FindRival`, `atk_max`→`/arena/BattleComplete`, `keyword`→`/guild/Search`,
   `request_id`→`/guild/SupportFuel`) and is *also* visibly wrong elsewhere
   (`source_inst_list` sits between `/world/ConfirmPMKey` and `/gym/LevelUp`).
   Every such row in these four documents is marked **[candidate]**.
2. **`.rodata` runs are per-translation-unit and the run boundaries are informative.**
   `0x01d8f71b:0x01d8f8c8` = `CSRSyncCard`; `0x01d6f888:0x01d6fb79` = `CSRAwake` +
   `CSRCard`; `0x01d73290:0x01d73591` = `CSRFC`; `0x01d78c2d:0x01d79094` = `CSRGuild` +
   the `GetGuildInfo` keys. A run that ends where a named function's assert tag begins
   (`0x01d6fb87 "Cannot find Ref Data: ID:%s"` → `SetRefID`) is a record-parser run —
   that is how the 37-key card-instance set in `ascension.md` §2.3 was bounded.
3. **The best container evidence is the retained STL template instantiations**, not the
   decompiler. `std::map<std::string, std::vector<shared_ptr<CSRAwake::REF>>>` spells out
   key *and* value types in the mangled name. That is how the ascension object→array
   nesting and all four guild containers were recovered without a single decompile.
   Prefer Ghidra's raw listing over its decompiler for anything with nested iterators or
   a `std::map` (`AGENTS.md` §16.7 item 7).
4. **The community guide is the best source of *semantics* in the project** and it
   repeatedly names fields: `%d` fodder counts, the 0–4000 FC gate, the 40-member cap, the
   24 h leave cooldown, three awaken tiers. When a player-facing string and a native literal
   agree, that is a **[RECOVERED]** shape claim (§2.3). When they disagree, say so — §3.
5. **The Go reference server's value is exhausted** for these four systems: account/login
   only. Do not spend time re-reading it.