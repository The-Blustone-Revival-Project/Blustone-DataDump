# Training / Gym / Supply subsystem

Research agent notes. Read-only work: evidence comes from
`analysis/native-all-strings.tsv`, `analysis/native-evidence.tsv`, and
`server-ts/src/*`. Nothing here was derived from Ghidra or a device.

**Status: in progress (written incrementally).** Sections 1-5 have first-pass
content; confidence lines are per-finding.

Naming note discovered early and important: **"Supply" and "Gym" are two
different subsystems, not one.** `gym/*` is card growth (level / rank / skill /
awaken / overcome) and `supply/*` + `CSRPopUpSupply*` is the village
attendance/gift-box building. Both are covered here because the original task
framed them together.

---

## 1. Routes in the subsystem

Method: `python tools/native-grep.py -p <term> ...` (one streaming pass over both
evidence tables). Source of every literal below is the `strings` table unless
noted.

### 1.1 `/gym/*` - card growth (RECOVERED, literal paths)

From `analysis/native-all-strings.tsv`, the `Gym` pattern (all 16 hits, `-m 60`,
so nothing was truncated for this pattern):

| Literal path | table offset |
|---|---|
| `/gym/LevelUp` | `01d8f72c` |
| `/gym/RankUp` | `01d8f739` |
| `/gym/SkillUp` | `01d8f74f` |
| `/gym/MultiSkillUp` | `01d8f7ab` |
| `/gym/Overcome` | `01d8f7bd` |
| `/gym/RankUpBundle` | `01d8f7d4` |
| `gym/Awaken` | `01d6f912` region (`01d6f951` = `gym/AwakenOvercome`) |

Note the two leading-slash families: `/gym/LevelUp` .. `/gym/RankUpBundle`
are a contiguous run of six at `01d8f72c..01d8f7d4` (a string table of route
paths, sorted-ish). `gym/Awaken` / `gym/AwakenOvercome` at `01d6f9xx` have **no
leading slash**, and sit in a different region of the file - they are very
likely a *different* constant (e.g. a UI key or a sub-path appended to a
prefix), so **do not assume they are the literal HTTP paths**. Flagged as an
open question (section 6).

No leading-slash siblings `gym/Awaken*` were found alongside the six, i.e.
there is no `gym/LevelUp`-style unslashed form in the table. `confidence: medium`
that the six `/gym/*` strings are the literal HTTP paths (they are shaped and
grouped exactly like the confirmed route families `/reference/...`,
`/mission/...`), `confidence: high` that all six literals exist in the binary.

Other non-route `Gym` hits are animation/UI identifiers, not protocol:
`FX_GYM_ENTER`, `FX_GYM_LVUP`, `FX_GYM_RU1`, `FX_GYM_SKL` (offsets
`01d81e00`, `01d8366f`, `01d8592d`, `01d86207`) and UI keys `GYM`, `GYM_ACHIEVE`,
`GYM_FIRST_ENTER` (`01d9049a`, `01d90502`, `01d90575`). `confidence: high`
(they are unmistakably asset/UI keys, not paths).

### 1.2 `supply/*` - village attendance/gift boxes

**Honest negative from the first pass:** the pattern `Supply` in
`native-all-strings.tsv` returned 60 hits (truncated) that are *overwhelmingly
C++ symbol names* (`CSRPopUpSupply`, `CSRSyncSupply`, `CSRCellSupply2D`, ...).
The only non-symbol hits were class names. No `supply/...` or `/supply/...`
literal path appeared in the first 60 matches. This needs a narrower pass -
see section 6. Recorded here as **unresolved**, not as "does not exist".

(What *is* known: `server-ts/src/game-routes.ts:117` groups
`/^(gacha|shop|supply)\//` in its fallback shape helper, which is evidence that
a `supply/` route family was seen on the wire or in the earlier route census.)

---

## 2. Native types / classes (demangled)

Highest-value section. All demangled by hand from the mangled names in the
evidence tables; names are recovered verbatim from the binary.

### 2.1 Sync/data layer (the protocol boundary)

| Demangled name | Evidence |
|---|---|
| `CSRPlayData::ParseSupplyInfo(json const&)` | symbols `00b6a884`, strings `00268c3d` |
| `CSRInstanceSync::ReqSupplyCB(shared_ptr<CPVHTTPRequest> const&, CPVHTTPResponse&, json const&)` | `00ae60e8`, `002692d4` |
| `CSRSyncSupply::Init(void*)`, `CSRSyncSupply::Refresh()` | `001bee61`, `001bee7c` |
| `CSRSyncSupply::SPECIAL_SUPPLY_INFO` (+ dtor/ctor) | `001ba009`, `001915f3`, `00191623` |
| `CSRSyncSupply::SUPPLY_TYPE` (enum) | embedded in `__tree` key type, `001bc1ff` |
| `ACTIVITY_SUPPLY_INFO` | `001baa97`/`00275278` (`C2`=ctor), `008b3b5a` |
| `ACTIVITY_SUPPLY_INST` (in a `std::vector`) | `00294378`, `00b742a0` |
| `CSRSceneSupply::PROGRESS_INFO` (map key `unsigned`, `__tree<pair<uint, PROGRESS_INFO>>`) | `001bd86a`, `008b4242` |
| `CSRSceneSupply::ATTEND_INFO` (`std::map<SUPPLY_TYPE, std::vector<ATTEND_INFO>>`) | `001bc1ff` |
| `CSRCellSupply2D::D4INFO`, `CSRCellSupply2D::DAYCOUNT` | `00d69b74`, `00d6a564` |

`confidence: high` for all of the above - these are verbatim demangled symbol
names, not interpretations.

The `__tree` / `__map_value_compare` symbol for `ATTEND_INFO` is the useful one:
it proves the **local** attendance model is
`map<SUPPLY_TYPE, vector<ATTEND_INFO>>`, i.e. attendance rows are grouped by
supply type. That is a *client-side* structure, so it is evidence about the
response shape only by analogy - see section 5.

### 2.2 Growth-parameter structs (card growth)

| Demangled name | Evidence |
|---|---|
| `CSRSyncCard::LEVEL_UP_PARAM` | `002e9f18`/`0037e691` region: `CSRSyncCard14LEVEL_UP_PARAM` |
| `CSRSyncCard::RANK_UP_PARAM` | `00383a84`: `CSRSyncCard13RANK_UP_PARAM` |
| `CSRSyncCard::SKILL_UP_PARAM` | `002e9f18`: `CSRSyncCard14SKILL_UP_PARAM` |

**This is the most important structural finding in the subsystem.** The gym
routes each take a *typed parameter struct that is passed by const reference to
a callback*, and the callbacks are not the request functions:

- `CSRTableLevelUp::OnTrainingLevelUpEnd(CSRSyncCard::LEVEL_UP_PARAM const&)`
  - `0101e598` / `0037e691`
- `CSRTableRankUp::OnTrainingRankUpEnd(CSRSyncCard::RANK_UP_PARAM const&)`
  - `0103b554` / `00383a84`
- `CSRPopUpSkillUp::OnTrainingSkillUpEnd(int, CSRSyncCard::SKILL_UP_PARAM const*)`
  - `00d59554` / `002e9f18`

`confidence: high` on the signatures (verbatim), `confidence: high` on the
inference that **each gym route's response is parsed into a distinct PARAM
struct** rather than a shared one - three different callback types for three
different routes is not something a single parser would produce.

### 2.3 UI layer (naming the flows)

`CSRPopUpCardDetail::SetTrainingButton(int,int,int,float)` `00dd26bc`;
`CSRPopUpCardDetail::OnSelectedTrainingButton(int,int)` `00dcd5a0`;
`CSRPopUpCardDetail::SetDeatilInfoAtTraining(float)` `00dce270` *(sic, typo
`Deatil` is in the original symbol)*; `CSRCardBundle::IsTrainingCard() const`
`0087888c` / `001a630d`.

Supply UI: `CSRPopUpSupply2D` (`OnInit`, `InitPanel`, `InitCell`, `Reload`,
`OnButtonClick`, `OnProcessPopUpBackKey`), `CSRPopUpSupplyFuel::Reload`,
`CSRCellSupply2D::DayCheck(uint)`, `CSRCellSupply2D::PopReceived(SRREWARD_INFO)`,
`CSRSupplySecretQuiz::get` / `::SetKey(string const&)`, `CSRSupply::get`,
`CSRSupply::ParseLoginBonusInst(json const&)`.

`confidence: high` (verbatim symbols). The UI symbols explain the vocabulary:
`CSRCardBundle::IsTrainingCard()` implies **some cards are flagged as
"training cards"** - a per-card reference property, not a player field.

### 2.4 Game-model accessors (`CSRPlayData` / `CSRRefData`)

Supply: `AddSpecialSupply`, `ParseSpecialSupply`, `FindGemInstInSpecialSupply`,
`GetSpecialSupply`, `FindSpecialSupply`, `GetActivitySupply`,
`SetActivitySupplyState(string const&, SUPPLY_STATE)`, `RemoveSpecialSupply`,
`IsSupplyNoti`, `ParseSupplyInfo` (`001ed451`-`00290213`, `00b6873c`-`00b70464`).

Reference data: `CSRRefData::GetActivitySupply(unsigned)` `00275207`,
`CSRRefData::GetActivitySupplyCnt()` `0027522c`.
=> there is **static reference data for supplies**, distinct from the player's
instance list. `confidence: high` on the existence of both.

Local persistence: `CSRLocalDB::Get/PutNewSupplyByActive(uint)`,
`::Get/PutNewSupplyByAttend(uint)`, `::Get/PutNewSupplyBySpecial(uint)` at
`00274aa6`-`00274c65` / `00afead4`-`00afee74`.
=> the client caches a **"new supply" seen-flag per category (active / attend /
special)**, each a single `uint`. `confidence: high`.

---

*(sections 3-7 appended below as the search continues)*