# Guild Blitz and Hunter Search native consumers (2026-10-05)

**Read-only.** No server change, no fixture change, no APK build, no release, no
LevelDB open, no emulator/adb/VM operation, no Ghidra run, no catalogue edit.
Exactly one file is written: this one. `polluted-observations.md` is deliberately
**not** appended — the parent mirrors.

**Headline correction.** `help-2_8-sweep-2026-10-05.md` §2.6 records the
`CONTENTS15_8` 12-numeral Guild Blitz point table as having "**no located native
consumer**", and its conflict-register row `NEW-6` repeats "single-version, no
consumer located". **That negative is wrong on the consumer half.** The Guild
Blitz system is fully present in `libnative_core.so` as the **GVG** family, with
19 `/gvg/*` routes, a dedicated manager with named parse/dump pairs, an explicit
`POINT_INFO_TYPE` scoring enum, and a UI render path that consumes per-point
detail rows. What remains unrecovered is **the numeric values**, which are
server-supplied — not the consumer.

**No coverage credit.** Strict coverage is unchanged at **heroes 1/113,
accessories 1/100, monsters 0/22** (`coverage.md`). Nothing here is a hero,
jewel, accessory or monster stat.

**Provenance of every source used this pass**

| source | identity |
|---|---|
| `analysis/native-all-strings.tsv` | on-disk literal dump of the original `libnative_core.so`. ⚠️ **its 8-hex column is GHIDRA image addresses = ELF VA + `0x10000`, not ELF VAs** — corrected below |
| `analysis/native-evidence.tsv` | retained dynamic symbols from the same library; also Ghidra image addresses. ⚠️ its third-column `undefined` tag is **unreliable** — 36 755 of its 40 290 `[FUNCTIONS]` rows are defined dynamic symbols |
| `analysis/recovered-data/leveldb-tables/all-tables.json` | 13-table LevelDB export from the preserved working seed (`tools/mine-export-reference-tables.py`); iteration order, not sorted |
| `analysis/ghidra-search-effect-root-keys.txt` | saved `ResolvePcRelativeStrings` output for `InitEffect` (0x009c33c4) and `ShowEffect` (0x009db7b0) |

Addresses are quoted exactly as they appear in those files. Per `AGENTS.md` §16.7
item 3, **`BLUSTONE_ARM`/Ghidra differ by 0x10000**; nothing in §1 mixes the two
conventions, and every address below carries its own file's convention.

### ⚠️ CORRECTION 2026-10-05 (later pass): both TSV columns are **Ghidra**, not ELF

The provenance table above originally read "addresses are ELF VAs" for
`analysis/native-all-strings.tsv`. **That was wrong**, and it was first caught in
[`gvg-reference-2026-10-05.md`](gvg-reference-2026-10-05.md) §0.2 and has now been
measured exhaustively. See
[`address-convention-2026-10-05.md`](address-convention-2026-10-05.md) for the
definitive table and the proof.

> Every `0x0…` / `0x01d…` token in this file that was read out of
> `native-all-strings.tsv` or `native-evidence.tsv` is a **Ghidra image address**.
> To get an ELF VA, **subtract `0x10000`**. To get the *file offset* of a byte in
> the library, subtract `0x10000` **and then** apply the `PT_LOAD` mapping — for the
> second segment (`VA 0x0210e550`+, `p_offset == p_vaddr − 0x1000`) that means a
> further `− 0x1000`.

Worked example, reproduced byte-exactly: this file's `/gvg/GetInst` at
`0x1d79345` → ELF VA `0x1d69345`; `point_id` at `0x1d7985b` → ELF VA `0x1d6985b`,
where `d[0x1d6985b] == b'point_id\x00'`. **No address in this file was changed by
the correction** — the fix is to the stated convention, and every literal here was
already correct as printed *provided the reader knows the column is Ghidra*.

---

# SECTION 1 — PURE: native symbols, routes, parsers and shipped strings

Pure = literal strings, symbols, addresses and parsed key names recovered from
those sources. No balance claim, no era inference, no fixture conclusion.

## 1.1 The Guild Blitz consumer exists and is named `GVG`

`libnative_core.so` implements Guild Blitz as the **GVG** (guild-versus-guild)
family. This is the single most important finding of the pass.

**Routes — all 19, contiguous in `.rodata` at `0x01d79345`–`0x01d794d6`**:

| address | route literal |
|---|---|
| `0x01d79345` | `/gvg/GetInst` |
| `0x01d79352` | `/gvg/RegisterPending` |
| `0x01d79367` | `/gvg/ToggleAutoRegister` |
| `0x01d7937f` | `/gvg/RegisterConfirm` |
| `0x01d79394` | `/gvg/GetRef` |
| `0x01d793a0` | `/gvg/GetRegisteredMemberList` |
| `0x01d793bd` | `/gvg/GetStrategy` |
| `0x01d793ce` | `/gvg/UpdateStrategy` |
| `0x01d793fd` | `/gvg/CombatEnd` |
| `0x01d7940c` | `/gvg/GetResult` |
| `0x01d7941b` | `/gvg/CombatBegin` |
| `0x01d7942c` | `/gvg/CombatCancel` |
| `0x01d79446` | `/gvg/CombatReady` |
| `0x01d79461` | `/gvg/GetCampClearPointLog` |
| `0x01d7947b` | `/gvg/GetCampDetail` |
| `0x01d79499` | `/gvg/GetDefenderList` |
| `0x01d794ae` | `/gvg/OccupyDefender` |
| `0x01d794c2` | `/gvg/DeployDefender` |
| `0x01d794d6` | `/gvg/GetSummaryInfo` |

These map one-to-one onto the four `CONTENTS15_1` phases and the `CONTENTS15_3`/
`CONTENTS15_4` actions named in the help text: `RegisterPending`/`RegisterConfirm`
= Participation Request, `DeployDefender` = Defense Arrangement,
`CombatBegin`/`CombatEnd`/`CombatCancel`/`CombatReady` = Attack Launch,
`GetResult` + `GetCampClearPointLog` = Reward Supply.

**Manager class.** `CSRGuildBattleMgr` (singleton accessor
`_ZN17CSRGuildBattleMgr3getEv` at `0x001af698`) with these members
(`analysis/native-all-strings.tsv`):

| address | symbol |
|---|---|
| `0x001af6b5` | `CSRGuildBattleMgr::GetRef()` |
| `0x00257303` | `RequestInst(std::function<void(int)>)` |
| `0x00259c7a` | `RequestRegisterPending(...)` |
| `0x0025989e` | `RequestAutoRegister(..., unsigned char)` |
| `0x0025741d` | `RequestDeployDefender(std::string, std::string, const std::list<std::string>&, const std::function<void(int)>&, unsigned char)` |
| `0x00259931` | `RequestDefenderList(std::string, ..., unsigned char)` |
| `0x002595bd` | `RequestCombatBegin(const std::list<std::string>&, const std::function<void(int)>&)` |
| `0x0025965a` | `RequestCombatReady(std::string, const std::function<void(int)>&)` |
| `0x002598e8` | `RequestCombatCancel(...)` |
| `0x002561a9` | `RequestCombatEnd(const std::function<void(int, unsigned char)>&)` |
| `0x002590aa` | `RequestResult(..., CSRPopUpGuildBattleResult::RESULT_INFO, unsigned char)` |
| `0x002596e4` / `0x00259ad3` | `RequestGetStrategy` / `RequestUpdateStrategy` |
| `0x0025972c` | `RequestSummaryInfo(...)` |
| `0x002599ba` | `RequestGetCombatLog(unsigned char, std::string, ...)` |
| `0x00259bef` | `RequestEnemyCampDetail(...)` |
| `0x00259016` / `0x00259452` / `0x00259774` | `GetEntryList()` / `RequestEntryList` / `FindEntryListMember` |
| `0x0025940c` | `RequestEntryJoin(...)` |
| `0x00257344` | `GetCurGVGPhase()` |
| `0x00259169` | `IsNextGVGBegin()` |
| `0x00259870` | `GetNextGVGBeginTime()` |
| `0x00258a6b` | `AmIPlayGVG()` |
| `0x00258467` | `IsMyGuildPlayGVG()` |
| `0x00258492` | `IsMyPVIDGVGEnter()` |
| `0x00258e35` | `IsCommander()` |

## 1.2 The point-scoring consumer: `POINT_INFO_TYPE` is a named enum

This is the direct rebuttal of the §2.6 "no located native consumer" negative.

| evidence | address | what it is |
|---|---|---|
| `_ZSt9to_stringIN17CSRGuildBattleMgr11BATTLE_INFO15POINT_INFO_TYPEEE...` | `0x0088f9d0` | a **`std::to_string` overload instantiated for `CSRGuildBattleMgr::BATTLE_INFO::POINT_INFO_TYPE`** — the enum has a stringifier |
| `_ZN22CSRPopUpGuildBattleWin16SetPointListDataERKNSt6__ndk14listINS0_4pairIN17CSRGuildBattleMgr11BATTLE_INFO15POINT_INFO_TYPEEiEE...` | `0x00c89844` | `SetPointListData(const std::list<std::pair<POINT_INFO_TYPE,int>>&)` — the result popup renders a **list of (point-kind, integer)** |
| `_ZN22CSRPopUpGuildBattleWin7SetDataERKNSt6__ndk14pairIN17CSRGuildBattleMgr11BATTLE_INFO15POINT_INFO_TYPEEiEE` | `0x00c89db0` | per-row `SetData(std::pair<POINT_INFO_TYPE,int>)` |
| `_ZN22CSRCellGuildBattleCard14SetCombatPointEi` | `0x0088fd9c` | `SetCombatPoint(int)` — a **single integer** point per defender cell |
| `_ZN17CSRGuildBattleMgr16GetMyCombatPointEv` | `0x00ab05f4` | personal total |
| `_ZN17CSRGuildBattleMgr21GetMyCombatPointLocalEv` | `0x00ab17e2` | locally accumulated personal total |
| `_ZN17CSRGuildBattleMgr19GetGuildCombatPointEv` | `0x00ab19f0` | guild total |

The mangled names are unambiguous: the winning-point economy is modelled as an
**enumerated point kind paired with an integer magnitude**, and it is rendered by
a dedicated result popup and by the defender cell.

## 1.3 GVG wire vocabulary — the full field dictionary

Recovered as adjacent `.rodata` literals in the `SRGuildBattleNetLocal.cpp`
block (`0x01d794ea`–`0x01d798af`; the source-path literal
`…/SRGuildBattleNetLocal.cpp` is at `0x01d798af`, bounding the block).

**Point/scoring fields:**

| address | key |
|---|---|
| `0x01d7925e` | `gvg_get_deploy_point` |
| `0x01d796ec` | `point_list` |
| `0x01d796f7` | `total_point` |
| `0x01d7984e` | `point_detail` |
| `0x01d7985b` | `point_id` |
| `0x01d79864` | **`multi`** |
| `0x01d79635` | `offense_point` |
| `0x01d79643` | `defense_point` |
| `0x01d7962c` | `total_cp` |
| `0x01d795d1` / `0x01d795d8` | `min_cp` / `max_cp` |
| `0x01d796bc` | `survive_cnt` |
| `0x01d796b1` | `deploy_cnt` |
| `0x01d796d5` | `defense_cnt` |
| `0x01d796c8` | `max_deck_cnt` |
| `0x01d796a1` | `camp_status` |
| `0x01d796ad` | `mvp` |
| `0x01d79651` | `commander` |
| `0x01d7959e` | `inf_reward` |
| `0x01d795c4` | `next_gvg_dtm` |

**`point_id` + `multi` is the decisive pair.** It is exactly the schema a
per-kind point table needs: an **enumerated `point_id`** carrying a
**multiplier `multi`**. This is the native shape that `CONTENTS15_8` renders as
prose — and it is why JA/SC/TC write the per-hunter rows multiplicatively
(`x5点`, `x50分`) while EN writes "Plus 5 Points". **The locale divergence
recorded in `help-2_8-sweep` §2.7 is not a translator's liberty; it is a lossy
English rendering of a server-supplied `multi` field.**

**Phase/field identity:**

| address | key | address | key |
|---|---|---|---|
| `0x01d79532` | `min_entry_cnt` | `0x01d79540` | `teaser_begin_dtm` |
| `0x01d79551` | `register_begin_dtm` | `0x01d79564` | `matching_begin_dtm` |
| `0x01d79577` | `deploy_begin_dtm` | `0x01d79588` | `combat_begin_dtm` |
| `0x01d79599` | `calc_begin_dtm` | `0x01d795a8` | `result_begin_dtm` |
| `0x01d795b9` | `finish_dtm` | `0x01d79624` | `inf_gvg` |
| `0x01d79615` | `enemy_guild_id` | `0x01d7966f` | `enemy_camp_id` |
| `0x01d79457` | `is_myteam` | `0x01d7948e` | `is_myguild` |
| `0x01d7943e` | `camp_id` | `0x01d79683` | `link_camp` |
| `0x01d79599` | (see `calc_begin_dtm`) | `0x01d796b1` | `deploy_cnt` |

`GetCurGVGPhase()` is fed by these **eight absolute datetimes**, which is the
native phase clock. `min_entry_cnt` is the participant-count field behind the
`GVG_최소 필요 인원` / "Least Needed Members" UI (§1.6).

**Combat-state vocabulary** (`0x01d793e5`–`0x01d7947b`):
`dmg`, `heal`, `tank`, `remain_hp` — the four values of the combat-log row
consumed by `/gvg/CombatEnd` and `BATTLE_DAMAGE_LOG`
(`AddCombatDamageLog` at `0x002561ef`, `GetCampCombatLog` at `0x0025922a`).

**Deck/entry vocabulary** (`0x01d7965b`–`0x01d797c7`): `deployed_list`,
`card_`, `card_%d`, `my_`, `enemy_`, `my_101`…`my_110`, `enemy_101`…`enemy_110`,
`auto_register`, `enemy_list`.

**`my_101..110` / `enemy_101..110` is a native enumeration of exactly ten camp
slots per side** — a first-party corroboration of `CONTENTS15_3`'s "10 areas"
(§3.1).

**Preset/toggle vocabulary**: `PRESET_GVGDEF` (`0x01d7919a`),
`toggle_gvg_atk` (`0x01d715c8`), `toggle_gvg_def` (`0x01d715d7`),
`gvg_deck_cnt` (`0x01d791a8`), `gvg_preset` (`0x01d920df`),
`GVG_DEFAULT_DECK_NUM` (`0x01d9104f`), `GVG_MIN_DECK_NUM` (`0x01d91064`),
`gvg_current_camp_order` (`0x01d79108`), `gvg_stage` (`0x01d790ce`),
`gvg_enter_first` (`0x01d81b40`), `gvg_result_first_` (`0x01d81cf5`),
`dymmyServer` (`0x01d7978a` — note the shipped typo).

**Reference-request callback.** `_ZN15CSRSyncRef11ReqGVGRefCBERK...` at
`0x003600f0` — `/gvg/GetRef` has a dedicated reference callback, so the GVG
reference data is a genuine separate table, not a reuse of the mission stage
reference.

**Two error strings** confirm server-side gating of participation
(`0x01d69ea5`, `0x01d69ec0`): `ERROR_GVG_NEED_TO_REGISTER`,
`ERROR_GVG_ALREADY_REGISTERED`.

**Assertion strings**: `%s RefID Is not My GVG Deck` (`0x01d7986a`),
`%s Defence Card Duplication` (`0x01d795ea`) beside
`SetDefenceCard` (`0x01d79606`).

## 1.4 Point-display UI vocabulary

Two distinct naming families, both shipped:

- Node names: `IT_WINPOINT` (`0x01d70525`), `TX_WINPOINT` (`0x01d70469`),
  `+%s` (`0x01d70475` — the "+N" per-point popup format), `IT_ST_LIMIT`
  (`0x01d79181`), `ST_LIMIT_NUM` (`0x01d7918d`), `PA_DECK_GVG_DEF`
  (`0x01d79157`), `PA_DECK_GVG_ATK` (`0x01d79171`), `PA_TOGGLE_GVG`
  (`0x01d79250`), `IT_LAST_CONNECTION` (`0x01d705fd`), `IT_CONTRIBUTION`
  (`0x01d7060f`), `VE_POINT` (`0x01d706ba`), `occupied` (`0x01d70531`),
  `atk_abivable` (`0x01d7053a`), `atk_clear` (`0x01d70548`),
  `deploying` (`0x01d704f2`), `SetDefCount` (`0x01d704ca`).
- **Localized message ids**, immediately after the GVG block at
  `0x01d79908`/`0x01d79918`: **`IMT_GV_WINPOINT`** and **`GV_WINPOINT`**. This
  prefix-plus-key pair is the same idiom as `IMT_VIP1`/`IMT_GUILD1` in the
  preserved fuel-layout XML, so `GV_WINPOINT` is a **localization key for the
  winning-point label** — the client asks the server/localizer for the word
  "point", it does not hardcode it. Directly adjacent is `SR_COMMON/ST_APPEAR2`
  (`0x01d79926`), and immediately after that the block switches to `help_data`/
  `help_link`/`category`/`desc1`/`desc2` (`0x01d7993b`+) — i.e. the GVG strings
  and the help table are **separate** regions, which is consistent with
  §2.2's finding that no help record is GVG data.

## 1.5 The combat scene, deck handler and network layer

| address | symbol |
|---|---|
| `0x00255dcc` | `CSRGuildBattle::PopUpPause()` |
| `0x00255dee` | `CSRGuildBattle::MakeStageInst()` |
| `0x00255e13` | `CSRGuildBattle::InitBackground()` |
| `0x00255e5f` | `CSRGuildBattle::PopUpResultWin(const CSRGameBase::RESULT&)` |
| `0x00255f68` | `CSRGuildBattle::ProcessKeyInput(float, int, unsigned char)` |
| `0x00255fb8` | `CSRGuildBattle::SetBGM()` |
| `0x00255fd5` | `CSRGuildBattle::OnFinish(unsigned char)` |
| `0x00256063` | `CSRGuildBattle::OpenStage()` |
| `0x001a34a2` | `CSRCardAnalyzer::LoadForGVGERKN12CSRGameActor10ACTOR_INFOE` |
| `0x0025880a` | `_Z22_GBCardInstToGVGHunterNSt6__ndk110shared_ptrIK7CSRCardEEh` — the **card→GVG-hunter converter**, the counterpart of `FindCard`/`SetRefID` in ordinary battles |
| `0x00257547`–`0x00257800` | `CSRGuildBattleDeckHandler` (`InitLayout`, `SaveEntry`, `LoadEntry`, `LoadThumbnail`, `OnClickTop/Bottom`, `GetTogglePanel`) |
| `0x00260f13`/`0x00260f7a` | `CSRGuildBattleNetLocal::Open(std::string)`, `OnCopy()` |
| `0x00255e9c` | `CSRGuildBattle::OnProcDamageLog(ERROR&, const nlohmann::json&)` — the local damage-log packet, the same loopback mechanism as mission combat (§16.3 of `AGENTS.md`) |
| `0x0025a39f` | `CSRGuildBattleNetLocal::C1(char const*)` |

**This is the fourth battle mode.** `SRGameStage.cpp`'s mode string table
(`0x01d782f7`–`0x01d78340`) reads `MISSION`, `BATTLE`, `MIRAGE`, `ABYSS`,
`EXPLORE`, `TUTORIAL`, `CINEMA`, `EPISODE`, `TUTORIAL_NEW`, **`GVG`** — so
Guild Blitz combat is a peer of mission combat, not a mission variant.

## 1.6 LevelDB `UI_TEXT_RO`: 146 shipped GVG strings

The recovered LevelDB contains **146 `GVG_*`/`설정_gvg_*` keys**. Verbatim `EN`
values (locale rows exist for all five locales; KO differs and is not
reproduced except where it carries a distinct numeral). Selected rows, chosen
because each maps to a `CONTENTS15_*` claim:

| key | `EN` |
|---|---|
| `BT_현재 승점` | Winning Point |
| `GVG_공격 승점` | Attack Points |
| `GVG_방어 승점` | Defense Points |
| `GVG_지역 점령` | Domination |
| `GVG_생존 헌터 보너스` | Surviving Units |
| `GVG_여유 보너스` | Undeployed Units |
| `GVG_한번의 공격으로 격퇴` | First Attempt |
| `GVG_두번의 공격으로 격퇴` | Second Attempt |
| `GVG_획득 승점` | Points Gained |
| `GVG_총 승점 획득` | Total Winning Points |
| `GVG_최종 획득 보상` | Total Winning Points |
| `GVG_방어 횟수` | Number of Blitz %s |
| `GVG_내 팀원` | Number of Hunters |
| `GVG_현재 참가인원` | Currently Participating |
| `GVG_필요 참가인원` | Least Needed Members |
| `GVG_최상위 4개 협회 중` | You are participating in the Infinite Guild Blitz as one of the top 4 strongest Guilds in Midgard! |
| `GVG_4000이하_헌터` | You can only select a hunter with 4000 or more Strength. |
| `GVG_동일 헌터 중 가장 강한 1명만 출격할 수 있습니다.` | If there are many identical hunters, only 1 hunter with the highest strength will take part. |
| `GVG_방어팀 설정을 위해선 4명의 헌터가 필요합니다` | There must be 4 hunters for the Defense Team. |
| `GVG_방어팀엔 만드시 4명의 헌터가 준비되어야 합니다.` | You must deploy 4 hunters to make a Defense Team. |
| `GVG_한번 공격에 사용한 헌터는 다시 사용할 수 없습니다` | A hunter who already made an attack cannot fight again. |
| `GVG_한번 설정한 방어팀은 변경 불가능하며` | The hunters deployed in the Defense Team cannot be changed. They cannot be deployed during Attack Launch. |
| `GVG_적의 체력은 공격 전으로 돌아가지만` | Any damage dealt to the opponent will be removed and the hunters who made an attack will be unable to make an attack. |
| `GVG_현재 상태로 쟁탈전에 참여하시겠습니까?` | Do you want to participate in the Blitz in the current state? |
| `GVG_쟁탈전 중엔 참가 신청 시점의 전투력으로 고정됩니다.` | The participating hunters' ability will be fixed as of this moment. It cannot be cancelled after the confirmation. |
| `GVG_보상은 참가인원의 전투력 합계로 결정됩니다.` | The rewards will be decided by the participating Guild Members' Total Strength. The Blitz rewards decrease partially with defeat. |
| **`GVG_참가기록이 있는 유저만 보상을 획득할 수있습니다.`** | **The Guild's total gained winning points need to be 3000 or more to receive the rewards.** |
| `GVG_결과 보상 미지급` | Rewards cannot be received due to not enough required points. |
| `GVG_토스트 수정권한이 없습니다` | Only the Blitz Commander can write the Command Message. Check the "Blitz Commander" in the "Help" page. |
| `GVG_신청 기간이 아닙니다.` | It is not the Blitz Participation Request period. |
| `GVG_인원이 부족하여 쟁탈전에 참여하지 못했습니다.` | More Guild Members are needed to participate in the Blitz. |
| `GVG_현재 정산 중입니다.` | The Blitz results are currently being counted. |
| `GVG_제한 시간이 종료되었습니다.` | The time limit has ended. |
| `GVG_참가 신청 마감까지` | Time Left for a Participation |
| `GVG_방어 준비 마감까지` | Time Left to Deploy |
| `GVG_공격 마감까지` | Time Left for Attack Launch |
| `GVG_쟁탈전 시작까지` | Time Left for Blitz Start |
| `GVG_신규 쟁탈전 시작까지` | Time Left for the Next Blitz |
| `GVG_쟁탈전 메인 지역 이름` / `GVG_타이틀_필드` | Metron Strip Mine |
| `GVG_로비 상단 문구` | A new Metron Strip Mine is found!\nWin the Blitz against other Guilds to get a ton of rewards! |
| `GVG_무제한 쟁탈전` (+4 siblings) | Infinite Guild Blitz / Rewards / Victory / ongoing / participation text |

**Two hard, ship-independent numerals appear in the LevelDB that the help table
does not contain:**

- **`4000`** — the minimum hunter Strength deployable as a Defense Team
  (`GVG_4000이하_헌터`, and the adjacent `.rodata` literal `GVG_4000` at
  `0x01d791c9`). This is a **deployment power floor**, not a point value.
- **`4`** — the Defense Team size (`GVG_방어팀엔 만드시 4명의 헌터가 준비되어야
  합니다.`, `GVG_방어팀 설정을 위해선 4명의 헌터가 필요합니다`), and separately
  the number of strongest guilds in the "Infinite Blitz" bracket.

**A complete 10-row camp roster**, one row per camp, each with distinct content:

| key | `EN` |
|---|---|
| `GVG_1호 캠프` | Excavator Camp 1 |
| `GVG_2호 캠프` | Excavator Camp 2 |
| `GVG_3호 캠프` | Carrier Camp 1 |
| `GVG_4호 캠프` | Carrier Camp 2 |
| `GVG_5호 캠프` | Supply Station Camp 1 |
| `GVG_6호 캠프` | Supply Station Camp 2 |
| `GVG_7호 캠프` | Command Post Camp 1 |
| `GVG_8호 캠프` | Command Post Camp 2 |
| `GVG_9호 캠프` | Landing Station Camp 1 |
| `GVG_10호 캠프` | Landing Station Camp 2 |

Exactly **ten**, five facility types × two. This matches `my_101..110` /
`enemy_101..110` in §1.3 and refines `CONTENTS15_3`'s "the ally areas are
separated into 10 areas total" (§3.1).

**Two 7-step in-game tutorial chains** (`GVG_TUTO_방어_치르치르_1..7` and
`GVG_TUTO_공격_치르치르_1..7`) ship the whole flow in player prose, including
`GVG_TUTO_공격_치르치르_5` / `_6`: "If you occupy the final defense line, you win
more points than other areas." / "If you want to go for a flawless victory, you
must occupy the final defense line!" — the rear-area point advantage, stated
outside the help system entirely.

## 1.7 The Hunter Search consumer: `/explore/*`, fully present

The **Hunter Search is native `EXPLORE`**, not a replica invention. Route
vocabulary at `0x01d728d3`–`0x01d72ac7`:

| address | route |
|---|---|
| `0x01d72969` | `/explore/GetRef` |
| `0x01d72979` | `/explore/GetInst` |
| `0x01d729e0` | `/explore/Begin` |
| `0x01d72a81` | `/explore/End` |
| `0x01d72a8e` | `/explore/Reward` |
| `0x01d72aa9` | `/explore/Retry` |
| `0x01d72ab8` | `/explore/Reset` |
| `0x01d72ac7` | `/explore/Entrust` |

**The 4-battle structure is a native field pair.** `cleared_wave`
(`0x01d72a6a`) and `max_wave` (`0x01d72b8c`) are separate keys, and
`cleared_explore` (`0x01d72b16`), `reward_cnt` (`0x01d72b26`), `play_cnt`
(`0x01d72c1e`) and `retry_cnt` (`0x01d72c27`) sit beside them. The client cannot
know "4" from these keys — it is a **server-supplied `max_wave`**.

**The native wave-banner families bound the Search wave count.** From
`analysis/ghidra-search-effect-root-keys.txt`, `InitEffect` (0x009c33c4)
registers `IG_WAVE%s_%s` at exactly three sites (`0x009c6a82`, `0x009c6bf6`,
`0x009c6d56`), and `search-effect-root-contract.md` line 43-49 resolves those
three loops as totals **2, 3 and 4** — i.e. the registered families are
`IG_WAVE1_2`/`2_2`, `1_3`/`2_3`/`3_3`, `1_4`/`2_4`/`3_4`/`4_4`, and **no total-1
family exists**.

**Other recovered EXPLORE fields**: `target_card_id`, `target_stage_id`,
`max_join_cnt`, `max_play_cnt`, `max_retry_cnt`, `period`, `cost`,
`end_datetime`, `cur_retry_cnt`, `cur_play_cnt`, `log_id`, `owner`,
`wave_info`, `explore_complete`, `explore_complete_type`, `explore_complete_id`,
`friend_pvid`, `friend_leader_id`, `vfid`, `play_log`, `retry_log`,
`reset_price`, `retry_price`, `reset_cnt`, `cooltime`, `detect`, `detect_id`,
`event_ref`, `difficulty`, `position`, `temple_id`, `temple_type`,
`finder_nickname`, `consume_result`, `reward_item`.

**`max_join_cnt` is the native home of `CONTENTS12_4`'s friend cap**, and
`cooltime` is the native home of the 1-hour event window. `max_play_cnt` is the
native home of `CONTENTS12_6`'s per-hunter daily limit. None of these are client
constants.

**Native classes**: `CSRFindShardStage` — `FindExploreRef` (`0x0090b140`),
`FindExploreInst` (`0x0090be3c`), `FindExploreWave` (`0x0090bf1c`),
`IsExploreCleared` (`0x0090bf9a`), `RefreshExploreInfo` (`0x00917640`);
`CSRGameUIExploreCardPiece`; `CSRSyncExplore` request/callback pairs;
`CSRExploreCardPieceStageInfo::ParseInfo` (`0x00917f00`) and
`GetStageIDToDiff(LEVELE)` (`0x00918830`). UI: `SEARCH/MAIN_EV_C`,
`SEARCH/MAIN_NOR_C`, `PA_CELL`, `SEC_%dBG`, `SPR_STAR`/`SPR_STAR1`/`SPR_STAR3`,
`TX_TOP`, `UI_MS_FT_TXT`, `00:00:00`, `%H:%M:%S`.

## 1.8 Explicit negatives — what is **not** in the binary

Stated so a future pass does not re-derive them:

- **No native literal equals any `CONTENTS15_8` numeral.** `150`, `25`, `50`, `5`,
  `2250` and `450` appear nowhere in `.rodata` as GVG scoring constants. A
  whole-file numeric sweep returns only unrelated hits (see §3.3).
- **No native `Wednesday`, `Sunday`, `Monday` or `Saturday` consumer** for the
  Guild Blitz schedule. `weekday-ui-2026-10-05.md` §1.2's negative stands; the
  GVG clock is the eight `*_dtm` server fields of §1.3, and
  `weekday-ui-2026-10-05.md` §2.5's open question "Are Wednesday's two texts
  driven by the same weekly cycle as Sunday's?" is answered **no** — GVG has a
  server-supplied absolute phase clock with no weekday logic client-side.
- **No native reference data for `CONTENTS12_*` Search quantities.** No capsule
  cost, no trace requirement, no drop rate, no per-grade cost table. `cost`
  (`0x01d72921`) and `max_play_cnt` are *field names*, not values.
- **No `/gvg/*` route is implemented in this replica.** `game-routes.ts:570`
  matches `/^\/(guild|gvg|arena|relation)\//` only to inject `list: []` and
  `users: []` — the compatibility-fixture fallback described in `AGENTS.md` §6.
- **`2250` is not recoverable** from any local artefact. It is not in
  `LEVELING.jet`, not in any of the 774 recovered JET packages, and not in the
  LevelDB tables.

---

# SECTION 2 — UNPURE: every numeral, with source and era

**Every numeral in this section is impure.** None is a recovered stat, none
changes a fixture, none contributes to any coverage denominator. Era tags per
`stat-version-context.md` (threshold **2019-09-05**):

- **[HELP-2.8.0.1]** — `UI_CSV.jet` from the shipped build. POST-threshold.
- **[DB-2.8.0.1]** — the recovered LevelDB `UI_TEXT_RO`/`UI_JSON_RO` tables.
  Same shipped client lineage. POST-threshold.
- **[BINARY]** — a native literal or field name. **Era-neutral**: the binary is
  the build under study and carries no independent date, but the GVG system is
  absent from 1.4.4.1, so it is by construction the 2.8-era feature.
- **[CONTENTS15_8]** — the help table of `help-2_8-sweep-2026-10-05.md` §2.6.
  [HELP-2.8.0.1], single-version.

## 2.1 Guild Blitz point table — all 12 numerals, each with a native home

| # | numeral | help claim | native status | era |
|---|---|---|---|---|
| 1 | **150** | Defense Team Deployment | `gvg_get_deploy_point` field exists (`0x01d7925e`); **no literal 150 in binary**; value is server-supplied | [CONTENTS15_8] / [BINARY] field only |
| 2 | **25** | Victory over Defense Team | no native literal; plausibly the base `point_id` value | [CONTENTS15_8] |
| 3 | **1** | 1st-attack bonus | `atk_clear`/`occupied` state keys (`0x01d70531`/48) and `GVG_한번의 공격으로 격퇴` "First Attempt"; the *attempt ordinal* is native, the +50 is not | [CONTENTS15_8] / [DB-2.8.0.1] |
| 4 | **50** | 1st-attack bonus | as above | [CONTENTS15_8] |
| 5 | **2** | 2nd-attack bonus | `GVG_두번의 공격으로 격퇴` "Second Attempt" — the *2nd attempt exists natively*; the +25 is not | [CONTENTS15_8] / [DB-2.8.0.1] |
| 6 | **25** | 2nd-attack bonus | as above | [CONTENTS15_8] |
| 7 | **5** | per surviving hunter | `survive_cnt` (`0x01d796bc`) + `GVG_생존 헌터 보너스` "Sururviving Units"; `multi` (`0x01d79864`) is where a ×5 lives. **No literal 5.** | [CONTENTS15_8] / [BINARY] structure |
| 8 | **5** | per undeployed unit | `deploy_cnt`/`max_deck_cnt` (`0x01d796b1`/`c8`) + `GVG_여유 보너스` "Undeployed Units"; same `multi` mechanism | [CONTENTS15_8] / [BINARY] structure |
| 9 | **1** | per occupied area | `camp_status`/`link_camp`/`enemy_camp_id`; `my_101..110` area enumeration | [CONTENTS15_8] / [BINARY] structure |
| 10 | **2250** | per occupied area, ×2 on the 3 rearmost | **no native literal, no local data source at all.** The rear-area advantage is independently attested by `GVG_TUTO_공격_치르치르_5`/`_6`, but its magnitude is not | [CONTENTS15_8] only |
| 11 | **3** | rearmost areas that double | no native literal. The camp roster gives **5 facility types × 2 = 10** (§1.6), which does *not* obviously yield "3 rearmost" — the mapping is unproven | [CONTENTS15_8] |
| 12 | **50** | per deployed Defense Team in the occupied area | as #7, via `multi` | [CONTENTS15_8] |

**Conclusion for the 12-numeral table: eleven of twelve now have a named native
field, enum or UI string that models the quantity; the twelfth (`2250`) has none,
and none of the twelve values is present in the binary.** The table is a
**server-side reference row set**, not a client constant — which is exactly what
the `point_id` + `multi` pair implies.

## 2.2 The 3000-point reward floor — now double-attested, still impure

| source | text | era |
|---|---|---|
| `CONTENTS15_6` `desc1` | "The Guild's total gained winning points need to be **3000** or more to receive the Blitz Rewards. Also, any individual Guild Member with **0** points cannot receive the reward." | [HELP-2.8.0.1] |
| `UI_TEXT_RO` `GVG_참가기록이 있는 유저만 보상을 획득할 수있습니다.` | "The Guild's total gained winning points need to be **3000** or more to receive the rewards." | [DB-2.8.0.1] |

**Two independent shipped corpora carry the same numeral with the same
threshold and near-identical wording.** That is stronger than the single-source
§2.6 record, and it survives `help-2_8-sweep`'s finding that help copy can lag
balance: this pair is help-table *and* live UI string. It is still **display
copy**, not a parser binding, and no native code reads `3000` for GVG. The `0`-point
individual exclusion appears **only** in `CONTENTS15_6`, not in the LevelDB row.

`GVG_결과 보상 미지급` ("Rewards cannot be received due to not enough required
points") is the shipped error toast for failing the floor — so the floor is
client-visible and enforced somewhere, but the enforcement site was not located.

## 2.3 The "10 areas" and "10 members" numerals — independently confirmed

| numeral | help claim | independent shipped corroboration |
|---|---|---|
| **10** | `CONTENTS15_2`: "at least **10** Guild Members need to make a participation request" | `min_entry_cnt` field (`0x01d79532`) + `GVG_필요 참가인원` "Least Needed Members" + `GVG_인원이 부족하여…` "More Guild Members are needed to participate in the Blitz." The **field is native; the value 10 is not in the binary.** |
| **10** | `CONTENTS15_3`: "The ally areas are separated into **10** areas total" | **Exactly ten `GVG_N호 캠프` rows** (§1.6), each a distinct named camp, plus the native `my_101..110`/`enemy_101..110` enumeration. **This is a real independent confirmation of the numeral 10 as a count.** |

The 10-area confirmation is the strongest numeral result in this pass: two
independent artefacts (a 10-row localized text roster and a 10-slot native
enumeration) agree with the help prose. It still says nothing about *points*.

## 2.4 The Wednesday cadence (`TIP_8`) — no consumer, and GVG explains why

`weekday-ui-2026-10-05.md` §1.3 records `TIP_8`: "Guild Blitz participation
requests can be made every Wednesday." That file's §2.2 leaves open whether
Wednesday is driven by a shared weekly cycle.

**Answer: it is not, because there is no client weekday logic at all.** The GVG
phase clock is eight **absolute server datetimes** (§1.3): `teaser_begin_dtm`,
`register_begin_dtm`, `matching_begin_dtm`, `deploy_begin_dtm`,
`combat_begin_dtm`, `calc_begin_dtm`, `result_begin_dtm`, `finish_dtm`, plus
`next_gvg_dtm`. `GetCurGVGPhase()` derives the phase from those, and
`GetNextGVGBeginTime()`/`IsNextGVGBegin()` read them. The five shipped countdown
strings (`GVG_참가 신청 마감까지`, `GVG_방어 준비 마감까지`,
`GVG_공격 마감까지`, `GVG_현재 정산 중입니다.`, `GVG_신규 쟁탈전 시작까지`)
render whatever the server sent.

**Consequence:** "every Wednesday" is a **server-side scheduling promise
presented as display copy**, not a client rule. A replica must not implement a
Wednesday gate; it must publish `register_begin_dtm`/`finish_dtm`. This
resolves `weekday-ui-2026-10-05.md` §2.5's third open question in the negative
and is consistent with `arena-season-time-units.md`'s finding that season
endings are absolute server seconds.

## 2.5 The Hunter Search numerals — all still server-supplied

| numeral | source | claim | native status |
|---|---|---|---|
| **4** | `CONTENTS12_2` | a Hunter Search is four consecutive battles; max 4 reward boxes | `max_wave`/`cleared_wave` fields exist; **and** `InitEffect` registers wave-banner totals **2, 3 and 4 only** (§1.7). A 4-wave Search is natively renderable; a 1-wave Search is not (§3.2) |
| **1** | `CONTENTS12_3` | one Helium Capsule | `cost` field exists; no value |
| **1 hour** | `CONTENTS12_4` | event Search open to friends 1 hour | `cooltime` field; no value |
| **10** | `CONTENTS12_4` | max 10 friends participate | `max_join_cnt` field; no value |
| **per 2 friends** | `CONTENTS12_4` | extra trace per two friends | **no native field found** |
| **2 days** | `CONTENTS13_3` | Contribution-reward blackout after leaving a guild | no native field located this pass |
| **5** / **60** | `CONTENTS13_4` | max 5 guildmates, 60 Fuel total | `/guild/GetFuelRequests` (`0x01d78eb0`) + `/guild/SupportFuel` (`0x01d78ed2`) + `request_id` (`0x01d78ec7`) exist; no value |
| **10** | `CONTENTS15_2` | (see §2.3) | `min_entry_cnt`; no value |

**Only one Search numeral has any native support, and it is a bound rather than
a value:** the wave-banner family set implies Search wave counts of 2, 3 or 4
are renderable. That is consistent with "four battles" being the real value, and
it is the single piece of native evidence bearing on §3.2.

## 2.6 GVG numerals the help table does **not** contain

| numeral | shipped text | meaning | era |
|---|---|---|---|
| **4000** | `GVG_4000이하_헌터` "You can only select a hunter with 4000 or more Strength." (+ `.rodata` `GVG_4000` at `0x01d791c9`) | minimum hunter Strength to be deployed as a Defense Team | [DB-2.8.0.1] / [BINARY] key |
| **4** | `GVG_방어팀엔 만드시 4명의 헌터…` | Defense Team size | [DB-2.8.0.1] |
| **4** | `GVG_최상위 4개 협회 중` | guilds in the "Infinite Blitz" bracket | [DB-2.8.0.1] |
| **5 × 2** | the 10-row camp roster | five facility types × two camps | [DB-2.8.0.1] |
| **7 × 2** | two `GVG_TUTO_*_1..7` chains | defense-phase and attack-phase tutorial length | [DB-2.8.0.1] |

These are the numerals that actually **would** populate a `/gvg/GetRef` fixture
and about which the help sweep is silent.

---

# SECTION 3 — VERDICTS

## 3.1 Guild Blitz: the system is native and its data model is recovered; the balance is not

**Verdict: `CONTENTS15_8`'s "no located native consumer" is FALSIFIED.**

Guild Blitz is `GVG`, with 19 routes, a dedicated manager, an explicit
`POINT_INFO_TYPE` enum with a `std::to_string` overload, a `(point-kind, int)`
result-popup renderer, and a `point_id` + `multi` wire pair. The consumer is not
merely present — it is *named*.

But the consumer being present does **not** recover the values. Eleven of the
twelve numerals have a native field that models their quantity; **none** of the
twelve values is in the binary, and `2250` has no local data source at all. The
honest statement is:

> The Guild Blitz point economy is a **server-supplied reference table**
> (`point_id` + `multi` per scoring event, aggregated into `point_list` /
> `total_point`, rendered by `CSRPopUpGuildBattleWin::SetPointListData`). The
> shipped help text is a prose rendering of that table. Nothing in the client or
> in any recovered local artefact fixes the magnitudes.

**Practical upshot for a future fixture:** `/gvg/GetRef` is the seam
(`ReqGVGRefCB` at `0x003600f0`), and the two numerals a fixture can legitimately
take from shipped evidence are the **10-camp roster** (§2.3, doubly attested)
and the **4000 Strength deployment floor** (§2.6). `min_entry_cnt` should be a
**field**, not a literal 10.

**One correction to `CONTENTS15_3` worth recording:** "the ally areas are
separated into 10 areas total" is right in count but the camps are **not
identical** — the shipped roster names five distinct facility types, each twice
(Excavator/Carrier/Supply Station/Command Post/Landing Station × 1/2). Any model
that treats the ten areas as exchangeable is already wrong, and the "3 rearmost
areas double" rule has no visible correspondence to that roster.

## 3.2 Hunter Search: `CONTENTS12_2` **CORROBORATES** the replica's 2-wave fixture being renderable, and contradicts its *balance* — while leaving the 4-vs-2 question open

This is the question the parent asked, and it has a three-part answer.

**(a) The 4-battle structure is native and server-driven.** `/explore/*` is fully
present, and `cleared_wave`/`max_wave` are separate keys (§1.7). The client
cannot know "4"; `max_wave` is server-supplied. So `CONTENTS12_2`'s "four
consecutive battles" is a claim about **server content**, not about the client.

**(b) `InitEffect` independently bounds Search waves to 2, 3 or 4.**
`ghidra-search-effect-root-keys.txt` shows exactly three `IG_WAVE%s_%s`
registration sites, and `search-effect-root-contract.md` resolves them as totals
2, 3, 4 — with **no total-1 family**. This is the decisive corroboration for the
replica's repair: `search-effect-root-contract.md` concluded that the one-wave
fixture was incompatible *because* it requested the unregistered `IG_WAVE1_1`,
and `SEARCH_WAVE_COUNT = 2` (`search-stage.ts:4`) is therefore **correct against
the native UI contract**, not merely a workaround. Two waves is inside the
supported set.

**(c) But 2 is a local choice, and 4 is the documented original.** Nothing in
the binary supplies a value for `max_wave`, so the replica's 2-wave
`local_search_017` remains a **local reconstruction**, exactly as
`search-effect-root-contract.md` line 51 already labelled it ("two-wave content
is a marked local reconstruction choice constrained by original UI support").
That file's own wording is vindicated: the constraint it identified is real and
native.

**Verdict on the "four battles, max 4 boxes" question:**

- **Corroborates** the replica's structural model: `cleared_wave`/`max_wave` and
  per-wave `wave_info` rows are the native mechanism, and a Search *is* a
  multi-wave sequence.
- **Corroborates** the 2-wave repair as native-legal.
- **Does not contradict** the replica's trace/capsule awarding, because those are
  driven by `cleared_wave` vs `max_wave` equality
  (`search-battle.ts:65` rewards exactly when `cleared_wave === max_wave`), which
  is the right shape for "a reward box per battle completed, max 4". **But the
  help text says a box is awarded *per completed battle*, and the replica's
  rule awards on full-clear only.** That is a genuine divergence between the
  fixture and `CONTENTS12_2`, and it is **not** visible on the current 2-wave
  fixture (both readings coincide at 2 waves with a full clear). It becomes
  observable the moment a Search is lost partway.

**That is the single most actionable finding in this pass.** If the replica ever
moves to the documented 4-wave Search, the current settlement rule would
contradict the shipped "a reward box is given with each battle completed … if you
are defeated, you receive only the boxes earned from complete battles". Do not
change the rule on the strength of help prose alone — but do not forget that it
is now contradicted, and that `reward_cnt` (`0x01d72b26`) and
`cleared_explore` (`0x01d72b16`) are the native fields that would express it.

## 3.3 What `2250` is not

§2.1 row 10 is worth isolating because `help-2_8-sweep` §2.6 offered the
`2250 = 450 × 5` reading as an arithmetic observation. The pass strengthens the
negative rather than the arithmetic:

- `2250` is **not** in the binary as a GVG constant.
- `450` is **not** in the binary as a GVG constant.
- `150` and `25` and `50` are **not** in the binary as GVG constants.
- There is **no** recovered local artefact containing any of them.

A whole-file sweep for these numerals returns only unrelated matches (ELF
offsets, OpenSSL/EC symbols, ffmpeg strings — e.g. `0x003b2250` is
`EVP_PKEY_CTX_set_data`, `0x01dab860`-area weekday strings are unbound libc/curl
per `weekday-ui` §1.2). So the `450 × 5` factorisation remains an **observation
about the shipped text** and nothing more. Combined with the 10-camp roster, it
is tempting to read 2250 as "per camp × camps", but **the camp count is 10, not
5**, and the five-fold factor is not explained by the roster. Recorded as a
coincidence, explicitly not a rule.

## 3.4 Corrections and retractions this pass forces

1. **`help-2_8-sweep-2026-10-05.md` §2.6 "no located native consumer" —
   RETRACTED.** The consumer is `CSRGuildBattleMgr::BATTLE_INFO::POINT_INFO_TYPE`
   with `CSRPopUpGuildBattleWin::SetPointListData`, and the system has 19 routes.
   Conflict-register row `NEW-6`'s "no consumer located" is likewise retracted.
2. **"single-version" for the Blitz point schedule — still true, but for a
   different reason than stated.** The schedule is single-version because GVG does
   not exist in 1.4.4.1, not because the client lacks a consumer.
3. **§2.7's locale-divergence reading of the `x5`/`Plus 5` split should be
   upgraded.** It is not a translation liberty; `multi` (`0x01d79864`) is a
   native field, so EN is a lossy prose rendering of a multiplier. This is an
   interpretation change, not a numeral change.
4. **`weekday-ui-2026-10-05.md` §2.5's third open question is answered:** the
   Wednesday text is not backed by any client weekday cycle; GVG runs on eight
   absolute server datetimes.

---

# SECTION 4 — Limits, and what was not done

- **No value is recovered.** §1 recovers the *consumers* and the *field names*.
  Every numeral remains server-side. Nothing here may be turned into a fixture.
- **No Ghidra run this pass.** All function-level claims in §1.2 come from
  mangled-symbol names already present in `native-evidence.tsv`; the names are
  unambiguous, but no body was decompiled and **no parser key order inside
  `BATTLE_INFO::parse` was verified**. The `point_id`/`multi` adjacency is
  `.rodata` adjacency, not a proven parse pair.
- **`POINT_INFO_TYPE`'s enumerator names are unknown.** `std::to_string` is
  instantiated for the type, so the enum has members, but their names and
  numeric values were not read. The `to_string` return-value table would give
  the point kinds directly and is the cheapest next decompilation.
- **No GVG reference row was located**, in `LEVELING.jet`, any of the 774 JET
  packages, or the LevelDB. `ReqGVGRefCB`'s data source is unknown.
- **LevelDB provenance caveat.** `all-tables.json` comes from the preserved
  working seed, which this project has already had to patch for EN records; the
  146 GVG strings are KO/EN/JA/SC/TC-complete rows, but whether any GVG row was
  touched by a prior seed delta was **not** audited here. Row *values* are used
  only as shipped-copy evidence, never as protocol.
- **`2250` has no data source of any kind** — not binary, not JET, not LevelDB.
- **Zero coverage credit.** Heroes 1/113, accessories 1/100, monsters 0/22
  unchanged. No goal completion is implied; the base-stat goal remains far from
  its 70% thresholds.
- **No fixture, test, server value, APK, seed, state file or emulator was
  touched.** No `polluted-observations.md` append.

## 4.1 Suggested follow-ups for the parent (not applied here)

1. Mirror §2.1/§2.2/§2.6 into `polluted-observations.md`, marked impure, with no
   coverage effect — the 4000 deployment floor and the 10-camp roster are the two
   numerals worth carrying forward.
2. Record `NEW-6` as **resolved-on-consumer, open-on-value** in the
   `help-2_8-sweep` conflict register, with the §3.4 retractions.
3. Answer `weekday-ui-2026-10-05.md` §2.5 Q3 from §2.4 above.
4. If a GVG fixture is ever attempted, the seam is `/gvg/GetRef` via
   `ReqGVGRefCB` (`0x003600f0`); the point kinds come from the
   `POINT_INFO_TYPE` → `std::to_string` table, and the two ship-attested numbers
   are 10 camps and the 4000 Strength floor. **Do not** import the §2.1 numerals.
5. Separately, note in the Search settlement notes that the
   `cleared_wave === max_wave` award rule diverges from `CONTENTS12_2`'s
   per-battle box rule at any wave count > 2 (§3.2c).