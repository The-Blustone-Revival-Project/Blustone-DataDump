# ASCENSION — Transcendence, Awakened Transcendence, Overcome

Content-domain research spec. Read-only. Tags per `AGENTS.md` §15.

---

## 0. Blunt summary, and one correction to the brief

The brief calls this "the game's Transcendence/'Awakening' system". **The native evidence
says there are three, not one**, with three different routes, three different player
fields and three different reference tables. Collapsing them is the single most likely way
to get this wrong:

| # | system | player field | route | reference route | UI scene |
|---|---|---|---|---|---|
| 1 | **Transcendence** (★ rank-up, "hyper") | `rank`, `rank_up_cnt` | `/gym/RankUp`, `/gym/RankUpBundle` | `/reference/GetCardRankUp`, `/reference/GetCardChain` | `SR_TRAINING_HYPER`, `SR_TRAINING_RANKUP` |
| 2 | **Awakened Transcendence** (each성, `awk_step`) | `awk_step`, `awk_overcome` | `gym/Awaken` | `/reference/GetCardAwaken` | `SR_TRAINING_AWAKE_HYPER`, `SR_TRAINING_AWAKE` |
| 3 | **Overcome** (`overcome_cnt`) | `overcome_cnt` | `/gym/Overcome`, `gym/AwakenOvercome` | `/reference/GetCardOvercome` | (no distinct scene; shares the Awake screen) |

| metric | value |
|---|---|
| ascension-owned routes | **7** |
| currently `mock:true` | **7** (3 more — `GetCardChain`, `GetCardRankUp`, `GetCardEnhancePrice` — already return `{}`) |
| **container types recovered** | **4** (all in `CSRAwake`) |
| response key sets recovered | **0** |
| reference-record key inventory recovered | **yes, 21 keys** |

---

## 1. What the systems do (community guide + `CHAR_STR_RO`)

Source: `recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md` and
`analysis/recovered-data/leveldb-tables/all-tables.json` (`CHAR_STR_RO`).

### Transcendence **[RECOVERED — player-facing text]**

- `all-tables.json:54628` — `CHAR_STR_RO` row: **"Transcendence"** (KO `자기극복`, JA `キャパ超越`).
- `:54650` — **"To transcend the hunter above, only identical hunters\\ncan be used as
  fodder. The used hunter will disappear."**
- `:54661` — **"Insufficient grade to use transcendence."** ⇒ there is a grade gate ⇒
  `card_required_rank` (`01d6fa33`).
- `:44893` — **"You can transcend a hunter up to 3 times. Same hunters are needed for
  transcendence."**
- `:35723 / :35745 / :35767 / :35789` — **item rows "★2 Transcendence Ticket",
  "★3 Transcendence Ticket", "★4 Transcendence Ticket"** with tooltip
  *"A special ticket you can use when you want to transcend a ★N hunter."* ⇒ **Transcendence
  consumes item instances** (note `★2/★3/★4` — there is no ★1/★5 ticket: only ★2 and up can
  transcend).
- Guide §Q8 L157-167 — Transcendence raises base HP/ATK/DEF and **skills by ~7 % per tier**;
  §Q10 L175 — it is paid for in **Manda**; §Q8 L159 — "it's better to first get your hunters
  to 5*".

### Awakened Transcendence ("Awakening", the 2021 patch) **[RECOVERED — player-facing text]**

- `all-tables.json:46213` — **"Awakened Transcendence"** (KO `각성 극복`, JA `覚醒超越`).
- `:46290` — **"Successfully transcended."**
- `:46301` — **"You need %d of the same hunter for Awakened Transcendence."** ⇒ the
  required-fodder count is a **server-supplied number**.
- `:49612` — **"All transcendence is complete."**
- Guide §Q26 L485-504 — costs **A1 = 30 crystals + 30 000 rupees, A2 = 50 + 100 000,
  A3 = 100 + 150 000** (total 180 crystals + 280 000 rupees) **+ 9 elemental hearts**;
  materials are "elemental hearts" obtainable from daily sign-in (3 of each element) or
  purchase. Three tiers — matching the native assert **`Card AwakeOvercome is 3`**
  (`01d6f8a0`, in the `CSRAwake` TU).

### 🔴 THE HIGHEST-VALUE RECONCILIATION IN THIS DOCUMENT **[RECOVERED]**

Guide `:46301` — *"You need **%d** of the same hunter for Awakened Transcendence."*
Native `CSRAwake` TU literals, in address order:

```
01d6f8e7  target_inst_id
01d6f8f6  target_cnt          <-- the "%d" in the player-facing string
01d6f901  src_inst_id_list
01d6f912  gym/AwakenOvercome
```

and

```
01d6f8a0  Card AwakeOvercome is 3
01d6f8b8  RequestAwakeOvercome
01d6f8cd  Card Doesn't Exist : (%d)
```

`CSRAwake::RequestAwakeOvercome(unsigned long, unsigned int, string const&,
vector<unsigned long> const&, function<void(int)>)` (`0x0085e37c`) takes
`(target_inst_id, target_cnt, string, src_inst_id_list)`. **The three request fields are
`target_inst_id`, `target_cnt`, `src_inst_id_list`** — this is the *only* request-field set
in the whole gym/ascension area whose members are contiguous with the route literal and
semantically forced by a player-facing string in the same TU. Confidence: **high**, but
still [RECOVERED-by-inference]; promote with
`python tools/resolve-literals-offline.py --function 0x0019ec65:0x0019ee7c`.

### 🔴 CORRECTION TO THE BRIEF: it is **11** awakened cards, not 15

The brief says "15 cards have `_1` variants". `analysis/catalogue/data/card-catalogue.tsv`
has exactly 15 `_1` rows — but they split cleanly in two:

| group | ids | evidence |
|---|---|---|
| **Awakened hunters** (11) | `004_1 005_1 009_1 010_1 011_1 017_1 019_1 020_1 021_1 024_1 056_1` | EN name is literally `"(Awakened)"`, rarity `5`, and the catalogue resolved a full skill/gear row |
| **Costume/skin variants** (4) | `026_1 034_1 038_1 086_1` | EN name **empty**, rarity **empty**, `owner_card_id` = `026/034/038/086`, `inferred_owner` = `yes` |

**Cross-check that settles it:** guide §Q26 L493-502 lists the recommended awakening
priority order as *Vincent › Genovia › Balian/Lapis/Rebecca · Gerard/Captain › Hecate ›
Riko · Tyltyl · Sienna* — **exactly the 11 ids above** (`010 056 019 017 021 005 009 011
024 004 020`). Eleven, no more.

The other four are the Boutique costumes (`all-tables.json:46213` neighbourhood; guide §Q25
L457-469 "Boutique Store … unlocked by paying Manda or by chance while using Manda"), and
`analysis/catalogue/stats/found/faq-image08-unidentified-card-equip-KO.png` +
`faq-image04*` are costume art. **Do not publish `026_1 034_1 038_1 086_1` as ascension
targets.** They belong to `/reference/GetSkinRef`, not `/reference/GetCard`.

---

## 2. Routes, owners, parsers — **[RECOVERED]**

Owner: **`CSRAwake`** (a `CMSingleton`), plus `CSRCardInfoContainer` for the non-awake
reference tables. Evidence: `analysis/native-evidence.tsv:7113-7228`.

### 2.1 `CSRAwake` function inventory (demangled, with addresses)

| addr | symbol | notes |
|---|---|---|
| `0x0085d3c0` | `CSRAwake::HasAwake(std::string const&) -> unsigned` | predicate: does this ref have an awaken row |
| `0x0085d494` | `CSRAwake::FindAwakeRef(std::string const&) -> unsigned` | **`std::map` lookup by string** |
| `0x0085d54c` | `CSRAwake::CalculateAwakeCombatPoint(unsigned)` | CP contribution |
| `0x0085d7f8` | `CSRAwake::RequestAwakeRef(std::string const&, function<void(int)>, unsigned char)` | → `reference/GetCardAwaken` |
| `0x0085e37c` | `CSRAwake::RequestAwakeOvercome(unsigned long, unsigned int, std::string const&, std::vector<unsigned long> const&, function<void(int)>)` | → `gym/AwakenOvercome` |
| `0x0085f480` | `CSRAwake::RequestCardAwake(unsigned long, unsigned int, std::string const&, function<void(int)>)` | → `gym/Awaken` |
| `0x00860348` | `CSRAwake::ParseAwakeRefBase(json const&)` | **the reader for `/reference/GetCardAwaken`** |
| `0x008605dc` | `CSRAwake::REF::parse(json const&)` | one awaken-reference row |
| `0x00860bec` | `CSRAwake::ParseAwakeOvercomeEffect(json const&)` | `/reference/GetCardOvercome` reader |
| `0x00860fcc` | `CSRAwake::ParseAwakeOvercomeSrc(json const&)` | `/reference/GetCardOvercome` reader |
| `0x00861208` | `CSRAwake::SRC_REF::parse(json const&)` | one overcome-source row |
| `0x0086154c` | `CSRAwake::GetOvercomeEffect(unsigned, unsigned)` | |
| `0x008617bc` | `CSRAwake::get()` | singleton |
| `0x00861820` | `CSRAwake::GetAwakeOvercomeEffect(unsigned)` | |
| `0x008618c6` | `CSRAwake::GetOvercomeSrc(std::string const&) -> unsigned` | **map lookup by string** |
| `0x00861980` | `CSRAwake::GetOvercomeSrc(unsigned, unsigned)` | map lookup by **(rank, step)** |
| `0x00861cb8` | `CSRAwake::SetOvercome(json const&)` | |

Card-side sinks:

| addr | symbol |
|---|---|
| `0x00aea0e4` | `CSRInventory::SetCardAwake(unsigned long, unsigned int)` — **(inst_id, awk_step)** |
| `0x0086809c` | `CSRCard::SetAwake(unsigned int)` |
| `0x00867e60` | `CSRCard::GetAwakeStep() const` |
| `0x00867e66` | `CSRCard::GetAwakeOvercome() const` |
| `0x00ae9ef0` | `SetCardOvercome` (called from `CSRSyncCard::ReqOvercomeCB` @ `0x00f5820a`) |

### 2.2 Container types — **[RECOVERED] from the retained STL template instantiations**

These are unambiguous: the mangled names spell out the key type and the value type.

```
0x00862fe0  std::map<std::string, std::vector<std::shared_ptr<CSRAwake::REF>>>::find
0x00865740  ...::emplace_unique_key_args        <- proves insertion by string key
0x008660a0  std::map<std::string, std::vector<std::shared_ptr<CSRAwake::SRC_REF>>>::find
0x00865d5c  ...::emplace_unique_key_args
0x00866cc0  std::map<unsigned,        std::shared_ptr<CSRAwake::EFFECT>>::destroy
0x008662de  std::map<std::pair<unsigned,unsigned>, CSRAwake::HYPER_SRC>::emplace_unique_key_args
0x00866c64  ...::destroy
```

⇒ **`/reference/GetCardAwaken` `ret_data` is a JSON OBJECT whose keys are STRINGS and whose
values are ARRAYS of reference rows.**

```
{ "<key>": [ {REF}, {REF}, … ], "<key2>": [ … ] }
```

**[UNKNOWN]** what `<key>` is. The assert string
`can not find reference (birthrank: %s, hyper: %s` (`01d6f98b`, same TU) says the lookup key
is the **pair (birthrank, hyper)**, so `<key>` is almost certainly a formatted composite
such as `"<birthrank>_<hyper>"` or `"<birthrank>-<hyper>"`. **Do not guess the separator.**
Recover it with:

```
python tools/resolve-literals-offline.py --function 0x0085d494:0x0085d54c   # FindAwakeRef
python tools/resolve-literals-offline.py --function 0x00860348:0x008605dc   # ParseAwakeRefBase
```

The composite-key format is the **only** thing standing between the current state and a
populated awaken table. It is the single highest-value decompile in this document.

### 2.3 The card-instance field set — **[RECOVERED as a literal run, assignment UNKNOWN]**

`.rodata` window `0x01d6f95c … 0x01d6fb79` is the card-instance run. Ordered:

```
hp_percent  atk_percent  def_percent  card_ref_id
awake(?)    awk_step     role         attr         res_prefix
src_list    skill_list   src_card_cnt effect       src
target_base_rank  overcome_cnt  card_required_rank  card_cnt
base  overcome  overcome_src_list  deck  removed_item  awaken
regdate  rank  rank_up_cnt  mirage_remain_hp  equipment_exp  awk_overcome
skin_ref_id  skin_id  skin_total_count
weapon_rank weapon_level armor_rank armor_level accessory_rank accessory_level
skill_1_level skill_2_level skill_3_level skill_4_level skill_5_level
```

then, immediately after, `analysis/ghidra-card-keys.txt` continues with
`Cannot find Ref Data: ID:%s` / `SRCard.cpp` / `sRefID.length() > 0` / `SetRefID` — i.e.
**the run ends where `CSRCard::SetRefID` begins**, which independently confirms it is the
`CSRCard`/`CSRInventory` record parser.

**This is the field set `/lobby/GetCardInven` and every gym/ascension mutation response
must satisfy.** `[UNKNOWN]`: which of these 37 keys belong to *which* reader. The
run is contiguous, so adjacency cannot disambiguate.

> The fields `hp_percent` / `atk_percent` / `def_percent` are almost certainly what
> Transcendence writes — they are literally "the percentages Transcendence raises"
> (guide §Q8: "It affects life points, damage output and defense", "~7 % per tier").
> **[INFERRED], not [RECOVERED]** — but it is a cheap and safe thing for the server to
> emit, because a missing key and a zero key are indistinguishable to the client.

---

## 3. Request fields

| route | recovered | note |
|---|---|---|
| `gym/AwakenOvercome` | **`target_inst_id`, `target_cnt`, `src_inst_id_list`** | §1, high confidence |
| `gym/Awaken` | `inst_id`, one `unsigned`, one `string` | `RequestCardAwake(unsigned long, unsigned int, string const&, …)`. The `unsigned int` is `awk_step`; the `string` is **[UNKNOWN]** — possibly the ref id or a target key. Do not guess. |
| `/gym/RankUp` | see `gym.md` §4 | **[UNKNOWN]** |
| `/gym/RankUpBundle` | `src_rank` adjacency candidate | **[UNKNOWN]** |
| `/gym/Overcome` | see `gym.md` §4 | **[UNKNOWN]** |
| `reference/GetCardAwaken` | a ref id (`RequestAwakeRef(string const&, …)`) | **[UNKNOWN]** which field name carries it |

**Note on the unslashed literals.** `gym/Awaken`, `gym/AwakenOvercome` and
`reference/GetCardAwaken` (`01d6f951`, `01d6f912`, `01d6f888`) have **no leading slash**,
whereas `CSRSyncCard`'s `/gym/LevelUp` … do. Two readings: (a) the client concatenates a
`"/"` prefix at request-build time, in which case they *are* `/gym/Awaken`,
`/gym/AwakenOvercome`, `/reference/GetCardAwaken`; (b) they are UI/asset keys. Reading (a)
is far more likely — they sit inside the `CSRAwake` TU next to assert strings and next to
request-field names. **This matters**: if the server registers `/gym/Awaken` and the client
sends `gym/Awaken` without a slash, the catch-all still answers, but any future route
allowlist would miss it. Register **both** spellings.

---

## 4. Response fixtures

### 4.1 Safe, shippable today

```jsonc
// POST /reference/GetCardAwaken
{ "result_code": 1, "ret_data": {} }      // OBJECT, per §2.2
//   ^ replaces { mock:true, route, request_keys, list:[], items:[] }
//   ^ the `list`/`items` keys the generic /reference/ fallback injects are MEANINGLESS to
//     FindAwakeRef, which looks up a string key and then iterates a vector.

{ "result_code": 1, "ret_data": {} }      // POST /reference/GetCardOvercome — same argument

// All five ascension MUTATIONS (gym/Awaken, gym/AwakenOvercome, /gym/RankUp,
// /gym/RankUpBundle, /gym/Overcome):
{ "result_code": 1, "ret_data": {} }
```

`{}` is **strictly better than the current mock** for all seven routes: every key the
client can ask for then resolves to `null` instead of to the string `"mock"`, and the
container is object-typed so no `type_error.305` is reachable. That is the same argument
`server-ts/src/game-routes.ts:292-318` already makes for `GetCardChain`/`GetCardRankUp`/
`GetCardEnhancePrice`.

### 4.2 Target shape — **[UNKNOWN]**, do not ship

`/reference/GetCardAwaken`, once §2.2's `<key>` format is recovered:

```jsonc
{ "result_code": 1, "ret_data": {
    "<birthrank>_<hyper>": [ { /* CSRAwake::REF — keys resolved by
                                  tools/resolve-literals-offline.py over
                                  0x008605dc:0x00860bec, NOT yet known */ } ]
} }
```

`/reference/GetCardOvercome` — **[UNKNOWN]** whether the two readers
(`ParseAwakeOvercomeEffect` `0x00860bec`, `ParseAwakeOvercomeSrc` `0x00860fcc`) consume
one object or two; they are separate functions over separate `std::map`s
(`map<unsigned, shared_ptr<EFFECT>>` and `map<pair<unsigned,unsigned>, HYPER_SRC>`), so
**two different sub-objects or two different routes are both live hypotheses.**
`/reference/GetCardOvercome` is a *single* route, which favours "one object, two sections".

### 4.3 Server-side state effects **[FIXTURE-design]**

- `rank` / `rank_up_cnt` — Transcendence; cap **3** per the player-facing string.
- `awk_step` — Awakened Transcendence; cap **3** (`Card AwakeOvercome is 3`).
- `awk_overcome` — Awakened-Transcendence overcome counter, distinct from `overcome_cnt`.
- `overcome_cnt` — plain Overcome counter.
- Every ascension route **consumes** `src_inst_id_list` instances and (for Transcendence)
  a `★N Transcendence Ticket` item instance. The ticket consumption is why
  `removed_item` exists on the card-instance record (§2.3).

---

## 5. Risk register

| risk | severity | detail |
|---|---|---|
| Guessing the `<birthrank><sep><hyper>` key format | **HIGH** | a wrong key makes `FindAwakeRef` miss *silently*; the screen shows an empty awaken list with no error. Ship `{}` instead. |
| Publishing `ret_data` as an **array** for `GetCardAwaken` | **HIGH** | `std::map<string, vector<…>>::find` needs a string key. An array yields `key()` = `""` at best and `type_error` at worst. |
| Treating the 4 costume `_1` ids as ascension targets | **HIGH** | publishes 4 rows that have no `REF`; would make `HasAwake("026_1")` lie. |
| Collapsing Transcendence / Awakened Transcendence / Overcome into one route | **MEDIUM** | three distinct player fields, three distinct reference tables. |
| Making ascension mutations mutate server state at `{}` shape | **MEDIUM** | client re-renders from a value the server never stored. |
| Registering only `/gym/Awaken` and not `gym/Awaken` | **LOW** | catch-all currently covers it; a future allowlist would not. |
| Emitting `hp_percent`/`atk_percent`/`def_percent` as strings | **MEDIUM** | these are almost certainly numeric; a string breaks `get<double>()`. Emit numbers, or omit. |