# Fight Club lobby: corrected native Enter / FindRival contract

2026-10-04. Read-only curated dumps, retained symbols and parent-generated exact instructions/literals. Research artifact only; no source/Ghidra/adb/runtime edits or arena implementation. **Lobby schemas are now recovered; genuine BP battle start/complete contract and native lobby rendering remain unverified.**

2026-10-10 native continuation: testing/arena-entry-001/report.md verifies Enter,
GetMyRank, original Waiting Room rendering, fixture season countdown and return
to Village. FindRival/defender/combat/reward rendering remains unverified. The
historical opening status describes the original source-only audit.

2026-10-10 follow-up: testing/arena-navigation-001/report.md verifies native
defense5 rendering after repairing its missing deck, and FindRival preparation.
Attacking uses4; defense uses5. Defense history remains generic compatibility;
no arena combat/reward/ranking/market validation follows from these screens.

## Evidence and corrections

Authoritative inputs: `ghidra-arena-enter-rival.txt` and strings; `ghidra-arena-lobby-helpers.txt`; **ghidra-arena-corrected-strings.txt**; `ghidra-arena-helper-key-instructions.txt`; `ghidra-arena-league-reference.txt`. Old `systems/arena.md` grouped literal adjacency without assignments. Its status0/flat-root battle example cannot populate the active lobby, and its FindRival is_auto adjacency was not a recovered request.

The old helper resolver paired unrelated ADD registers and emitted false **using**, **h_price**, and league item **_id** keys. Correct exact pairs are:

- ParseSeason LDR0x942e34/slot0x9430d8, **r1 ADD0x942e42** ->season_no.
- ParseUser LDR0x943106/slot0x9433ec, **r1 ADD0x943112** ->pvid. The adjacent r0 ADD0x94310c is a different pointer.
- ParseDefender LDR0x943966/slot0x943c80, **r1 ADD0x943974** ->chain_bonus. The adjacent r0 ADD0x94396c is unrelated.
- League item quantity LDR0x948532/slot0x948778, **r1 ADD0x948538** ->qty, independently of id's ADD0x948534.
- Defender slot0x943c88 is tuple/insertion metadata, **not a JSON field**; the mangled type-name output was a false key.

Use corrected output and raw register evidence, not those historical strings.

## Enter request and exact response hierarchy — verified

**RequestEnter0xf5cdfc posts /arena/Enter** with five auth fields app_code,app_ver,market,pvid,otp. **ReqEnterCB0xf5d3b4** parses result_code1, takes **ret_data** at0xf5d47c and passes it to **ParseEnter0x942c3c**.

Exact response hierarchy:

```text
ret_data
  arena
    status                 numeric1 required for active parsing
    season                 ParseSeason record below
  user
    battle                 ParseUser record below
    is_weekly_reward       numeric/bool flag
  deck                     optional ordinary ParseDeckSetting array
```

ParseEnter resolves arena0x942c5a, arena.status0x942c70, arena.season0x942cca; user0x942cf6, **user.battle**0x942d1c; user.is_weekly_reward0x942d7a. If arena.status!=1, it returns without populating season/user/deck. Optional deck is **root ret_data.deck**0x942dc6, passed to PlayData.ParseDeckSetting; it is not user.deck here. ReqEnter passes the parsed league-state result to its UI callback; transport/application success alone does not establish active league state.

**ParseSeason0x942e24** consumes numeric fields season_no,weekly_no,start_datetime,end_datetime,next_datetime,weekly_start_datetime,weekly_end_datetime,weekly_next_datetime. Season/weekly identifiers are32-bit conversions; date fields use64-bit numeric conversion, also accepting numeric strings. They do not require SQL date strings through ParseTime. Exact epoch/window interpretation and original schedule remain a separate timing policy; choose a bounded coherent local season only as an explicit fixture and test its UI.

**ParseUser0x9430f8** consumes numeric pvid(uint64),rank,season_no,weekly_no,league_level,rating_point,league_win,win,lose,refresh_datetime (numeric64), plus strict **start_message,win_message,lose_message strings**. Rank is arena ranking, not hunter grade. Match season identifiers to the published season and own pvid/profile; don't replace ranked user state with a mission-completion DTO.

## FindRival request and exact hierarchy — verified

Actual method name is **RequestFindOpponent0xf63464**, but its URL literal is **/arena/FindRival**. Its form map contains exactly **four** fields app_code,market,pvid,otp (`unordered_map(...,4)`). No app_ver or is_auto is emitted on this request; signature only takes callback. Retain ordinary authentication validation without requiring an invented mandatory field.

**ReqFindOpponentCB0xf639a0** passes successful envelope.ret_data into **ParseFindRival0x947318**. Shape:

```text
ret_data
  arena
    rival_list             ARRAY of ParseDefender records
  refresh_price
    price_type             numeric
    price                  numeric
  achievement              omit until its own shape is modeled
```

Exact keys arena0x947352/rival_list0x94735a; root refresh_price0x947436, nested price_type0x947440 and price0x947490. Rival entries call ParseDefender, not GetCardInven. A present nonnull achievement enters its parser, so omit it rather than send[] for a no-achievement fixture.

## Rival record / roster — verified shape, fixture identities separate

**ParseDefender0x943958** reads each rival record directly:

- **chain_bonus[]** of `{ref_id:string, atk:number, def:number, hp:number}`. Empty array skips its strict ref_id parsing. Bonus scaling/fidelity is not established by naming these fields.
- **card_book** object with numeric atk,def,hp,crt_dmg,crt_chance. Crit fields share this same card_book parent, not rival root.
- Strict strings **nickname,thumbnail,profile_status,country_code**. These replace old guesses nick/img/country; no original thumbnail mapping is inferred here.
- Numeric **status,user_exp,vip_exp**.
- **battle**, passed to the exact ParseUser record above; this is where the rival's pvid/ranking/season/league state resides.
- **deck**, an object keyed **inst_1,inst_2,...**, not an array of raw IDs.
- **gem[]**, passed to CSRGem.ParseGem if nonempty; empty skips unreconstructed gem instance semantics.

Deck format is independently proved by raw instructions0x944080..0x9440da and decompile: prefix inst_ from slot0x9443c8/ADD0x9440ac, ordinal starts0 and is incremented before to_string; it iterates the deck container's size and indexes inst_N by ordinal. For a five-slot record publish **exactly inst_1..inst_5**, without extra metadata keys that increase objectsize. Each entry must be a full recovered card-instance object with **inst_id**. Zero inst_id skips ParseCardInst and appends a default empty card; nonzero invokes **PlayData.ParseCardInst0xb69598** and needs the existing complete instance/reference/skill/equipment compatibility fields. Native parser acceptance of empty slots does not prove every fight scene tolerates them.

A local rival can use already downloaded/published hunter references, local synthetic pvid/name and fresh rival-local instance IDs; those are fixture choices, not original opponents or real matchmaking. Enemy cards are parsed into rival records, not automatically evidence of owned inventory mutation. No attack/reward claim is made from a populated lobby.

## League/weekly reference arrays — verified parser seam

**ReqBattleLeagueCB0xf83a38** receives full envelope, indexes **ret_data.league[]** and **ret_data.weekly_reward[]**, and calls **ParseBattleLeague0x948438** and **ParseBattleWeeklyRwd0x948b48**. The original route vocabulary contains `/reference/GetBattle`; exact callback/path association should be corroborated by request registration/native trace before promoting a route mapping from adjacency alone.

League row keys: **league_level,max_win,user_exp,gold,free_iap,iap,honor**, and **item_list[] {id:string,qty:number}**. Weekly row keys: **min_ranking,max_ranking,user_exp,gold,honor,free_iap**, item_list with the same strict id/numeric qty. Empty item lists avoid creating fabricated reward items. Reward quantities, max-win thresholds, ranking bands and rating/progression are original-data unknowns and must remain labeled local fixtures.

**GetLeagueDesc0x94798c** switches league enum1..6 to localized descriptions; it is not a league-vector lookup. Do not use its missing-reference theory as proof. Other lobby reward/progress UI consumers may still require populated reference rows; native observation is necessary before claiming those controls work.

## Remaining seam and acceptance limits

These recovered envelopes are sufficient to build a coherent **local Fight Club lobby/rival selection** model with explicit fixture seasons/rewards/opponents. They are not native runtime validation. Confirm Enter status1 populates its season and own battle profile, known-art rival rows render without strict-string/reference faults, configured deck survives reload, and refresh-price presentation agrees with whatever supported refresh policy is published.

**BP battle start/complete is not recovered in this lane.** Current mission aliases for arena/BattleStart/BattleComplete do not prove Fight Club gameplay: arena opponents, bid/revenge state, BP spending and rating/rewards have distinct parsers. Next exact targets: **RequestBattleWith0xf5d534**, **ParseTargetEnemy0x9438d8**, **ParseApBp0x943750**, **ParseBattleResultLog0x944d40**, **ParseBattleResult0x944e68**, plus start/complete callbacks identified from retained symbols. GetMyRank/ranking/defense/revenge/weekly reward transaction routes likewise remain separate controls; don't inherit the mission schemas.

Transitive card/gem targets if roster issues arise: ParseCardInst0xb69598, existing CSRCard.parse evidence, CSRGem.ParseGem0xa5c2f4. This report creates only durable research corrections; no source implementation, automatic battle, reward grant, BP debit or client patch is proposed.
