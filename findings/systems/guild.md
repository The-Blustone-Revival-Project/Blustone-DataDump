# GUILD (`/guild/*`, `/lobby/GetGuildInfo`, `/reference/GetGuild*`)

Content-domain research spec. Read-only. Tags per `AGENTS.md` §15.

---

## 0. Blunt summary

| metric | value |
|---|---|
| `/guild/*` routes in `.rodata` | **24** |
| `/lobby/GetGuildInfo` | 1 |
| `/reference/GetGuild*` reference routes | 5 |
| **total guild-family routes** | **30** |
| currently `mock:true` | **29** |
| currently real | **1** (`/guild/GetNotifications` → `[]`, `server-ts/src/game-routes.ts:276`) |
| parser functions located & addressed | **24** (`CSRGuild`) + 5 (`CSRSyncRef`) |
| response key sets recovered | **0 assigned** / **26 keys inventoried (INFO) + 6 (GetGuildInfo)** |
| container types recovered | **4, all decisive** |

Guild is the largest surface of the four and the one where the *containers* are fully
pinned. The route→parser map is complete. Only the key→parser assignment is missing, and
the container types are exactly the ones that crash when guessed wrong (§6).

---

## 1. What the system is (community guide)

`Blustone Guide FAQ.md` §Q24 L431-447, and the Glossary L63 "limited to 40 people".

- **Three guild kinds [RECOVERED-text]:** *Private* (invite only), *On Permission Only*
  (apply → Leader/Supervisor accepts or denies), *Public* (free-for-all).
- **Join gate [RECOVERED-text]:** "Some of these guilds will also ask for a certain score
  in the Fight Club before being able to join. This score can range from 0 up to **4,000
  points**." ⇒ native `fc_point_limit` / `fc_point` (`01d78c5f`, `01d78cd6`). **This is the
  hard link between arena and guild** — see `arena.md` §1.
- **Roles [RECOVERED-text + RECOVERED-symbol]:** Leader, Supervisor. "Supervisors have
  almost the same permissions as Leaders, however, they **cannot modify any of the
  Guild's descriptive information**." ⇒ native `MEMBER::ROLE` +
  `CSRGuild::RoleTypeToText(MEMBER::ROLE)` `0x0082787c`, and the split between
  `/guild/Update` (leader-only) and `/guild/Appoint` (leader/supervisor).
- **Leader-editable, for a fee in Manda [RECOVERED-text]:** "Flag, Name and Description,
  Score requirement, appointment of supervisors or new leaders."
- **Contribution [RECOVERED-text]:** "each win guarantees you **300** points, while defeats
  are **250**" (arena), "or by using your Guild Cooperative partners on ruins / searches
  (Roughly **75** points each)"; "Donation in rupees is an alternative way to contribute".
  ⇒ native `CSRGuild::ContributionByAction(CONTRIBUTION_ACTION)` `0x00a7fb3a` and
  `CSRGuild::CalcContributionByGold(uint)` `0x00a7fb6e`, and route `/guild/Donate`.
- **Leaving [RECOVERED-text]:** "Leaving a guild will mean you will be unable to rejoin a
  new one **for a day**." ⇒ the server must implement a **24 h rejoin cooldown** after
  `/guild/Leave`. **[UNKNOWN]** where the cooldown is published — no key for it exists in
  the INFO cluster, so it is probably enforced server-side on `/guild/Apply` only.
- **Size cap [RECOVERED-text]: 40 members.** Native `member_cnt` `01d78c7f`.
- **Fuel [RECOVERED-symbol]:** `CSRGuild::FUEL_INFO`, `GetMaxSupportCount()`,
  `GetSupportFuelCount()`, `/guild/GetFuelRequests`, `/guild/SupportFuel` — the "Guild
  Cooperative partners on ruins / searches" mechanic.

### 🔴 The Go reference server does **not** cover guild — do not expect it to

`recovered-assets/community-notes-2026-09-30/Account registration + auto-login code summary.txt:3`:

> `//   · removed: chat, guild, friend, mail, stage, CDN, HTTP framework and all other unrelated parts`

The excerpt contains **zero** guild handlers. The only guild-adjacent fact in it is a
comment at line 78: *"the guild rule 'leader offline for a long time → warning →
auto-disband' relies on it, see `dbGuildInactiveSweep`"* — i.e. the working server
**does** implement guilds, but that code was withheld. Treat the colleague's server as
**no evidence at all** for any guild wire shape. (See §7 for the one thing it does tell us.)

---

## 2. Routes — **[RECOVERED]**, all 30

### 2.1 `/guild/*` — literal addresses from `analysis/native-all-strings.tsv`

| route | literal @ | requester (demangled) | addr | `*CB` sink |
|---|---|---|---|---|
| `/guild/GetDetailInfo` | `01d78c4a` | `CSRGuild::RequestInfo(list<unsigned long>, function<void(int, list<INFO>&, function<void(int, INFO const&)>&)>, …)` | `0x00a68e94` | list<INFO> + per-guild INFO |
| `/guild/GetChattingLog` | `01d78d1f` | `CSRGuild::RequestGuildChatLog(function<void(int)>)` | `0x00a6e078` | `ParseChatLog` `0x00a681b8` |
| `/lobby/GetGuildInfo` | `01d78d35` | *(no `*CB` retained)* | — | `CSRGuild::ParseMyInfo` `0x00a685f0` + friends |
| `/guild/GetUserGuilds` | `01d78d5a` | `CSRGuild::RequestInfo` / `ParseUserGuild` | `0x00a6ba78` | |
| `/guild/Found` | `01d78d6f` | `CSRGuild::RequestBuild(string, USER::JOIN, unsigned, string, function<void(int, INFO const&)>)` | `0x00a6f8c4` | one INFO |
| `/guild/Apply` | `01d78d7c` | `CSRGuild::RequestApply(unsigned long, string, function<void(int, PLAY_DATA const&)>)` | `0x00a704f8` | PLAY_DATA |
| `/guild/CancelApplication` | `01d78d89` | `RequestCancelApply(function<void(int)>)` | `0x00a71184` | int only |
| `/guild/ConfirmInvitation` | `01d78da9` | `RequestConfirmInvite(unsigned long, unsigned char, string, function<void(int)>)` | `0x00a71cf8` | int only |
| `/guild/GetRecommendations` | `01d78dc2` | `RequestRecommandList(function<void(int, list<INFO>&)>)` | `0x00a729b8` | **list<INFO>** |
| `/guild/Leave` | `01d78ddc` | `RequestLeave(function<void(int, PLAY_DATA const&)>)` | `0x00a7352c` | PLAY_DATA |
| `/guild/Search` | `01d78df1` | `RequestSearch(string, function<void(int, list<INFO>&, list<INFO>&, ISB&)>)` | `0x00a740a0` | **two lists + a flag** |
| `/guild/ReceiveContributionReward` | `01d78dff` | `RequestContributionReward(function<void(int, SRREWARD_INFO&)>)` | `0x00a74c94` | SRREWARD_INFO |
| `/guild/Donate` | `01d78e20` | `RequestDonate(unsigned, function<void(int)>)` | `0x00a75808` | int only |
| `/guild/GetApplicants` | `01d78e2e` | `RequestAppicants(function<void(int, list<APPLY>&)>, uchar)` *(sic)* | `0x00a763fc` | **list<APPLY>** |
| `/guild/ConfirmApplication` | `01d78e4b` | `RequestConfirmApply(list<unsigned long>, uchar, function<void(int)>)` | `0x00a76f94` | int only |
| `/guild/Appoint` | `01d78e65` | `RequestNominate(unsigned, MEMBER::ROLE, function<void(int)>)` | `0x00a77f64` | int only |
| `/guild/Banish` | `01d78e74` | `RequestBanish(unsigned, function<void(int)>)` | `0x00a78c00` | int only |
| `/guild/Invite` | `01d78e82` | `RequestInvite(unsigned, function<void(int)>)` | `0x00a79804` | int only |
| `/guild/Update` | `01d78e90` | `RequestModify(string, USER::JOIN, unsigned, string, function<void(int, INFO const&)>)` | `0x00a7a408` | one INFO |
| `/guild/GetRanking` | `01d78e9e` | `RequestRank(unsigned, int, int, function<void(int, list<INFO>&)>)` | `0x00a7b03c` | **list<INFO>** |
| `/guild/GetFuelRequests` | `01d78eb0` | `RequestFuelList(function<void(int, map<unsigned, shared_ptr<FUEL_INFO>>&)>)` | `0x00a7bcdc` | **map<unsigned, FUEL_INFO>** |
| `/guild/SupportFuel` | `01d78ed2` | `RequestSupportFuel(unsigned, function<void(int, shared_ptr<FUEL_INFO>)>)` | `0x00a7c898` | one FUEL_INFO |
| `/guild/GetNotifications` | `01d78ee5` | `RequestMsgList(function<void(int, list<MSG>&)>, uchar)` | `0x00a7d48c` | **list<MSG>** |
| `/guild/ReadNotifications` | `01d78f0d` | `RequestMsgRead(list<unsigned long>, function<void(int, list<MSG>&)>, uchar)` | `0x00a7e004` | list<MSG> |
| `/guild/DeleteNotifications` | `01d78f26` | `RequestMsgRemove(list<unsigned long>, function<void(int, list<MSG>&)>, uchar)` | `0x00a7ec54` | list<MSG> |

### 2.2 `/reference/GetGuild*` — all five **[RECOVERED]**

| route | literal @ | `CSRSyncRef` callback | addr | reader |
|---|---|---|---|---|
| `/reference/GetGuildPrices` | `01d9016c` | `ReqGuildPriceForActionCB` | `0x00f84f6c` | `CSRGuild::ParsePriceByActionRef` `0x00a801ac` |
| `/reference/GetGuildContributionReward` | `01d90186` | `ReqGuildContributionRewardCB` | `0x00f84fa0` | `CSRGuild::ParseContributionReward` `0x00a8043c` |
| `/reference/GetGuildContributionPoints` | `01d901ac` | `ReqGuildContributionPointsCB` | `0x00f84fd4` | `CSRGuild::ParseContributionPoints` `0x00a80c5c` |
| `/reference/GetGuildLevelBenefits` | `01d901d2` | `ReqGuildLevelBenefitsCB` | `0x00f85008` | `CSRGuild::ParseLevelBenefits` `0x00a81030` |
| `/reference/GetGuildLevelBenefitsStr` | `01d901f3` | `ReqGuildLevelBenefitsStrCB` | `0x00f8503c` | `CSRGuild::ParseLevelBenefitsString` `0x00a818bc` |

`CSRGuild::FindPrice(PAY_ACTION)` `0x00a80160` and `GetGuildLevelRef(uint)` `0x00a7fe00`
tell you these tables are keyed by an **action enum** and a **level number** respectively.

---

## 3. Container types — **[RECOVERED]**, and this is the valuable part

From the retained STL template instantiations (`analysis/native-evidence.tsv:13185-13205`):

```
13190/13194  std::list<CSRGuild::INFO>            (cctor, assign)
13116        std::list<CSRGuild::APPLY>
13120        std::list<CSRGuild::MSG>              (cctor)
13185        std::list<CSRGuild::USER>             (::__list_imp<USER>::clear)
13199-13202  std::unordered_map<unsigned, CSRGuild::INFO>
13191/13194  std::map<unsigned, std::vector<std::function<void(INFO const&)>>>
13186        std::map<CSRGuild::BENEFIT::TYPE, CSRGuild::BENEFIT::TYPE>::insert
CSRCellGuildRank::Init(const std::vector<CSRGuild::INFO>&)   0x00893ff8
CSRGuild::RequestFuelList(cb(int, std::map<unsigned,
                             std::shared_ptr<CSRGuild::FUEL_INFO>>&))   0x00a7bcdc
CSRGuild::UpdateDetail(cb(void(std::map<unsigned long,
                             std::shared_ptr<SRTARGET_USER>>&, …)))  0x00a69da0
```

Consequences, all **[RECOVERED]**:

| sink | container | JSON shape |
|---|---|---|
| `list<INFO>` — GetRecommendations, GetRanking, Search (1st list) | `std::list` | **ARRAY** of INFO |
| `list<INFO>` — Search (2nd list) | `std::list` | **ARRAY** of INFO |
| `list<APPLY>` — GetApplicants | `std::list` | **ARRAY** |
| `list<MSG>` — Get/Read/DeleteNotifications | `std::list` | **ARRAY** |
| `list<USER>` | `std::list` | **ARRAY** |
| `vector<INFO>` — CSRCellGuildRank | `std::vector` | **ARRAY** |
| `map<unsigned, FUEL_INFO>` — GetFuelRequests | `std::map`, **unsigned** key | **OBJECT keyed by decimal pvid string** |
| `map<unsigned, SRTARGET_USER>` — member detail | `std::map`, **unsigned long** key | **OBJECT keyed by decimal pvid string** |
| `unordered_map<unsigned, INFO>` | `std::unordered_map<unsigned,…>` | **OBJECT keyed by decimal pvid string** |

> **The three `std::map<unsigned, …>` sinks are the crash-prone ones.** They are the exact
> shape that killed `/reference/GetMonster` and `/relation/BlockList` in this project. An
> array there yields `key() == ""` for every element and silently registers nothing; and
> the **key name** (`fuel_requests`? `user_detail`?) is **[UNKNOWN]**.

---

## 4. The INFO key cluster — **[RECOVERED as literals, 0 assignments]**

`.rodata` window `0x01d78c2d … 0x01d78cf8`, immediately surrounding the
`/guild/GetDetailInfo` literal:

```
guild_id  newbie  contribution            [ /guild/GetDetailInfo ]
fc_point_limit  region  emblem_id  member_cnt  gvg_win_cnt  gvg_inf_win_cnt
members  banished  rejected  exited  invited_guests  fc_point  applied
expdate  supports  supported
```

26 addresses, 20 keys. Two readings are live and **I am not going to pick one**:

- **Reading A:** the run is one `CSRGuild::INFO` record's key set, and
  `/guild/GetDetailInfo` merely sits in the middle of the TU's literals. Under A,
  `ParseGuild` reads the 9 scalars and `ParseMembers` reads the 6 arrays
  (`members`, `banished`, `rejected`, `exited`, `invited_guests`, `supports`, `supported`,
  `applied`) **from the same object**.
- **Reading B:** the three before the route literal are `CSRGuild::PLAY_DATA`'s keys and the
  fifteen after are `INFO`'s. `PLAY_DATA::parse` `0x00a823b0` **does** exist and
  `PLAY_DATA::dump` `0x00a8257c` exists, so a separate PLAY_DATA record is real.

Reading A is favoured by `ParseMyInfo`/`ParseGuild`/`ParseMembers` all taking a single
`json const&` — but that is an argument, not evidence.

### `/lobby/GetGuildInfo` container keys — **[RECOVERED]**

`.rodata` `0x01d7905f … 0x01d79094`, a *separate* run well clear of the INFO cluster:

```
my_guild  guilds  user_guilds  applicants  fuel_requests  guild_notifications
```

Six keys, and they are exactly the six top-level sections a guild home screen needs.
`ParseMyInfo` `0x00a685f0` + `ParseGuilds` `0x00a6b340` + `ParseUserGuild` `0x00a6ba78` +
`ParseApplicants` `0x00a6b680` + `ParseFuel` `0x00a6c4d0` + `ParseNoties` `0x00a6bf08` =
**six readers, six keys.** This mapping is the closest thing to a recovered shape in the
whole guild system: *the name of every parser equals the name of a key.*

| key | reader | container |
|---|---|---|
| `my_guild` | `ParseMyInfo` `0x00a685f0` | **object** (one INFO) — **`null`/absent if not in a guild** |
| `guilds` | `ParseGuilds` `0x00a6b340` | **array** (list<INFO>) |
| `user_guilds` | `ParseUserGuild` `0x00a6ba78` | **array** (list<INFO> or list<USER>) |
| `applicants` | `ParseApplicants` `0x00a6b680` | **array** (list<APPLY>) |
| `fuel_requests` | `ParseFuel` `0x00a6c4d0` | **array**, or **object keyed by pvid** — see §3; **[UNKNOWN]** |
| `guild_notifications` | `ParseNoties` `0x00a6bf08` | **array** (list<MSG>) |

**`fuel_requests` is the one genuinely ambiguous container** — `RequestFuelList`'s callback
is `map<unsigned, shared_ptr<FUEL_INFO>>` (⇒ object) while `ParseFuel` lives in the
array-reading family (⇒ array). Send it as an **empty object `{}`**: an empty object both
has zero elements *and* yields no bogus key, so it is safe under either reading. That is
the one place where "empty" is not ambiguous — it is the intersection of both readings.

### Other guild literals worth knowing **[RECOVERED]**

```
01d78d49  target_pvid_list          request field, /guild/GetDetailInfo
01d78da2  agreed                    request field, /guild/ConfirmInvitation
01d78de9  keyword                   request field, /guild/Search
01d78e43  granted                   request field, /guild/ConfirmApplication
01d78ec7  request_id                request field, /guild/SupportFuel
01d78efd  notification_id           request field, /guild/Read|DeleteNotifications
01d78f41  action                    (after the route table — /reference/GetGuildPrices)
01d78f48  equipment_level_up        BENEFIT::TYPE enum names
01d78f5b  gem_level_up              ″
01d78f68  traning                   ″  [sic — typo in the original binary]
01d78f70  intrust                   ″
01d78f78  sender                    MSG field
01d78f7f  supplement                MSG field
01d78f8a  read                      MSG field
01d78f6f  sent                      MSG field
```

---

## 5. 🔴 FLAG: guild chat and fuel are **WebSocket**, not HTTP

**[RECOVERED]** from the symbol set:

- `CSRGuild::CreateFuelJson(CSRChatModule::COMMANDER, FUEL_INFO const&)` `0x00a82024`
- `CSRGuild::CreateBanishJson(CSRChatModule::COMMANDER, SRTARGET_USER const&)` `0x00a822a4`
- `CSRGuild::ParseFuelMsg(std::string const&)` `0x00a6da48` — parses a **string**
- `CSRGuild::UpdateGuildMessage(std::shared_ptr<CHATDATA>)` `0x00a6c8ec`
- `CSRChat::OnGuildMessage(int, std::vector<unsigned>)` `0x008a81a8`
- `CSRGuild::GetChatLogGuildID() const` `0x00a68972`, `SetChatLogGuildID(unsigned)` `0x00a68978`
- assert tag `Parse Error:` `01d78d02`, function tag `ParseFuelMsg` `01d78d12`

⇒ A guild *fuel request* is **posted into the guild chat channel as a `COMMANDER` JSON
message**, and the server replies **on the chat WebSocket** with a `CHATDATA` blob.
`/guild/SupportFuel` is the HTTP *acknowledgement*, and its callback returns a single
`FUEL_INFO`. **`/guild/GetChattingLog` returns the persisted history, not live messages.**

Consequence for the replica: `/guild/SupportFuel` and `/guild/GetFuelRequests` cannot be
made fully live without the chat WebSocket. Shipping them as static fixtures is honest;
shipping them as *stateful* is not, because the authoritative update arrives on a channel
the replica does not implement. **Say so in `openapi.ts`.**

Also **[RECOVERED]**: `CSRGuild::GetErrorStr(int, std::string const&)` `0x00a67ce4` —
guild actions return **domain error codes** through a per-code message lookup, not through
`result_code`. That means most `/guild/*` mutations should return `result_code: 1` with an
error code *inside* `ret_data`, **[UNKNOWN]** under which key.

---

## 6. Response fixtures

### 6.1 Safe, shippable today — the single highest-value change in the guild system

```jsonc
// POST /lobby/GetGuildInfo        <-- do this one first
{ "result_code": 1, "ret_data": {
    "my_guild": null,          // null == "not in a guild"; an object here would be a lie
    "guilds": [],
    "user_guilds": [],
    "applicants": [],
    "fuel_requests": {},
    "guild_notifications": []
} }
```

Why this beats the status quo: today `/lobby/GetGuildInfo` falls into the generic
`/lobby/` fallback and receives
`{ mock:true, route, request_keys, card_list:[], item_list:[], gem_list:[], mission_list:[] }`
— an object with **four keys the guild reader never asks for and none of the six it does**.
Six named readers now each find their own section.

`my_guild: null` is deliberate: the guide's first-run experience is *not in a guild*, and
`CSRGuild::CheckUserStatus(unsigned)` `0x00a67ede` / `IsInvitable()` `0x00a67eb8` branch on
membership. `null` is also safe if the reader tests `is_null()` — and if it does not, a
missing key would be `null` anyway, so `null` is exactly the "no guild" answer.

```jsonc
// ARRAY routes — one uniform rule:
{ "result_code": 1, "ret_data": [] }
// GetRecommendations, Search, GetRanking, GetApplicants,
// GetNotifications, ReadNotifications, DeleteNotifications,
// GetUserGuilds, GetChattingLog

// OBJECT-keyed routes:
{ "result_code": 1, "ret_data": {} }
// GetFuelRequests, GetDetailInfo (map<unsigned, SRTARGET_USER> section)

// SINGLE-RECORD routes:
{ "result_code": 1, "ret_data": {} }
// Found, Update, Leave, Apply, ConfirmApplication, Appoint, Banish, Invite,
// CancelApplication, ConfirmInvitation, Donate, SupportFuel
```

**The array/object split is not cosmetic — it is the crash boundary.** Today every
`/guild/*` route falls into `/^\/(guild|gvg|arena|relation)\//.test(route)` and gets
`{ mock:true, route, request_keys, list:[], users:[] }`, i.e. an **object**. Feeding an
object to `std::list<INFO>::resize(...)` / a range-for over `ret_data` is the
`type_error.305`-with-no-handler class described in `AGENTS.md` §16.2. Every guild route
whose sink is a `std::list` — i.e. `GetRecommendations`, `Search`, `GetRanking`,
`GetApplicants`, `GetNotifications`, `ReadNotifications`, `DeleteNotifications`,
`GetUserGuilds`, `GetChattingLog`: **nine routes** — is currently one wrong container type
away from a SIGSEGV. Fixing the container is cheap and is the single most valuable guild
change available.

### 6.2 `/guild/GetNotifications` is already right

`server-ts/src/game-routes.ts:276` returns `envelope([])`. `RequestMsgList`'s sink is
`list<MSG>&` ⇒ array ⇒ **`[]` is correct. Do not change it.**

### 6.3 Target shape for a playable one-guild replica **[FIXTURE-design]**

A single pre-built guild costs nothing and makes every screen non-empty. It needs:

```jsonc
// /lobby/GetGuildInfo
{ "result_code": 1, "ret_data": {
  "my_guild": {
    "guild_id": 1, "newbie": 0, "contribution": 0,
    "region": 1, "emblem_id": 1, "member_cnt": 1,
    "gvg_win_cnt": 0, "gvg_inf_win_cnt": 0,
    "fc_point": 0, "fc_point_limit": 4000,     // guide: 0..4000
    "expdate": 0, "applied": 0, "supports": 0, "supported": 0,
    "members": [ /* one MEMBER: the player, role = leader */ ],
    "banished": [], "rejected": [], "exited": [], "invited_guests": []
  },
  "guilds": [ /* the same INFO, for the ranking list */ ],
  "user_guilds": [], "applicants": [], "fuel_requests": {},
  "guild_notifications": []
} }
```

Every key above is a real literal (§4). The **grouping** (all in one INFO object) is
Reading A and is **not proven**. Mitigate by sending the scalars **both** at the top level
of `ret_data` and inside `my_guild` — the same belt-and-braces hedge `server-ts` already
uses for `/reference/GetArea` (`AGENTS.md` §11) and which is non-regressive because a
reader that does not ask for a key ignores it.

Guide-derived values that are safe to hard-code as **[FIXTURE]**:
`fc_point_limit: 4000` (guide §Q24 L440), `member_cnt` cap 40 (Glossary L63).

---

## 7. Contradictions and gaps — flagged loudly

1. 🔴 **The Go reference server contains no guild code.** File header line 3 lists guild
   among the removed sections. A colleague reading that file will conclude "the working
   server doesn't do guild" — it does (`dbGuildInactiveSweep`, line 78 comment), the code
   was just withheld. **Do not cite it as evidence either way.**
2. 🔴 **`/guild/Leave` must impose a 24 h rejoin cooldown** (guide §Q24 L447) but **no key
   in the INFO cluster can express it.** The cooldown must be enforced on
   `/guild/Apply` server-side, and it is **[UNKNOWN]** what the client is told.
3. 🟠 **Reading A vs Reading B for the INFO key cluster is unresolved** and it changes the
   fixture shape. One resolver pass over `ParseGuild` (`0x00a6a384:0x00a6b1f4`) and
   `ParseMembers` (`0x00a6b1f4:0x00a6b340`) settles it.
4. 🟠 **`fuel_requests` container is genuinely ambiguous** (array vs pvid-keyed object).
   `{}` is safe under both; `[]` is not.
5. 🟠 **Domain error codes**: `GetErrorStr(int, string)` implies `/guild/*` mutations
   signal failure *inside* `ret_data`. Returning `result_code: 1` unconditionally will make
   failed actions look successful to the client.
6. 🟡 **Fuel needs a WebSocket** (§5). Static fixtures only.
7. 🟡 **`/guild/Update` costs Manda** (guide §Q24 L441). `CSRGuild::FindPrice(PAY_ACTION)`
   + `/reference/GetGuildPrices` imply a price table keyed by a `PAY_ACTION` enum whose
   member names are the literals at `01d78f48`–`01d78f70`
   (`equipment_level_up`, `gem_level_up`, `traning`, `intrust`).

---

## 8. Risk register

| risk | severity | detail |
|---|---|---|
| Leaving `/guild/*` responses as objects | **HIGH** | six routes feed a `std::list::resize(uint)`/range-for with an object ⇒ `type_error.305` ⇒ SIGSEGV. §6.1 fixes it for free. |
| Guessing the `map<unsigned,…>` key name on `GetFuelRequests` / member detail | **HIGH** | a wrong key registers nothing, silently. `{}` is the safe answer. |
| Sending `my_guild` as an object for a fresh account | **MEDIUM** | lies about membership; `CheckUserStatus`/`IsInvitable` will branch wrongly. |
| Enforcing no rejoin cooldown after `/guild/Leave` | **MEDIUM** | contradicts documented game behaviour; low visibility, high "wrongness". |
| Publishing `result_code: 1` for a failed guild action | **MEDIUM** | `GetErrorStr` says failures are in-band. |
| Making fuel stateful | **MEDIUM** | the authoritative channel is a chat WebSocket the replica lacks. |
| Selecting Reading A only, without the top-level hedge | **LOW** | recoverable; costs one extra A/B run. |