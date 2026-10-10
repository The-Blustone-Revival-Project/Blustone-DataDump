# Genuine Fight Club Start / Complete contract

2026-10-04. Read-only parent-generated eight-function battle dump/literals, arena lobby research and native symbols. No source/adb/Ghidra/runtime changes. Ghidra code addresses. **No native Fight Club battle has been validated here. Original BP cost, rating/rewards and matchmaking remain fixture-policy gaps.**

## Exact requests and battle identity

**RequestBattleWith0xf5d534 posts /arena/BattleStart**. Form fields: app_code,app_ver,market,pvid,otp, **target_pvid,is_revenge,is_friendship,bid**. Target/bid are uint64 decimal strings; two flags are selected0/1 strings. Its retained signature is `(uint64,byte,byte,uint64,callback)`; exact literals are in the fresh strings dump. It has no stage_id or mission battle_id.

**RequestBattleComplete0xf5de80 posts /arena/BattleComplete**. Form fields: same five auth fields, **target_pvid,is_revenge,play_info**. Play_info is a JSON **string** with **is_win**, clear_time,dead_cnt,player_total_hp,player_total_hp_max,enemy_total_hp,enemy_total_hp_max,atk_max,atk_total,atk_cnt. It does not use mission's clear field spelling. Atk_max is genuinely a request metric; old adjacency note calling it a result field is retracted. Metric units/value derivation beyond the shared MISSIONPLAY_INFO structure should not be invented.

**No bid or is_friendship is sent on Complete.** Bid is Start input, not a recovered newly returned completion nonce. None of the inspected Start response parsers consumes a returned bid. Its exact revenge/history provenance remains unresolved. Do not make a native completion require a fabricated battle_id, or claim an ignored response field is an idempotency token.

A local model needs its own persisted authenticated active-arena identity/target/flags and roster snapshot. Reject unsupported friendship/revenge modes before spending resources until modeled. Normal target lookup should match a known published rival; do not let mission stage fallback choose n_01_01 for target_pvid. Retry correlation is a real issue: Complete's callback retries some failures up to retrycount>8, and no native transaction nonce was recovered. A duplicate already accepted completion should return its preserved receipt without paying twice; identical intentional future battles cannot simply be deduplicated globally by body forever.

## Start success: flat resources and a full enemy

**ReqBattleWithCB0xf5dca8** on successful response indexes **ret_data** separately for **ParseApBp0x943750**, **ParseRefreshCost0x9476bc**, and **ParseTargetEnemy0x9438d8**, then optional achievement. It invokes its success callback with updated FCPlayData, not a mission Start DTO.

Exact resource snapshot consumed by ParseApBp:

```json
"user": {
  "ap": 35, "ap_charge_time": 1790000300,
  "bp": 9,  "bp_charge_time": 1790001800
}
```

Values above illustrate shape only. **All four are direct scalars under user.** They are not prev/cur objects and charge times are not nested inside ap/bp. ParseApBp reads user0x94375c, ap0x943766, ap_charge_time0x9437b8, bp0x943804, bp_charge_time0x943850, then calls **SyncAP and SyncBP unconditionally**. Omitting AP on a BP battle can reset the native AP snapshot to0. Send current AP unchanged plus its real deadline, and post-debit BP plus its deadline. Use the existing recovered next-charge deadline/server-seconds convention; this numeric parser does not establish separate season datetime units.

ParseTargetEnemy reads **ret_data.arena.combat_info** (arena0x94390e, combat_info0x943916), passes the **full record** to ParseDefender0x943958, and stores the resulting target enemy. Use the complete known record from `arena-lobby-contract.md`: strict identity/profile strings, nested battle user, chain_bonus[], card_book stats, deck.inst_1..N full valid card instances and gem[]. Target battle.pvid must match the requested target. A generic rival ID/list or a mission monster record is insufficient.

Start also invokes **ParseRefreshCost0x9476bc**, now independently recovered in `ghidra-arena-refresh-cost.txt` and strings. It reads root **ret_data.refresh_price{price_type,price}**; optional **user.iap{iap_qty,free_iap_qty}** uses scalar current balances and optional **user.gold.cur** updates gold. These wallet branches can be omitted when Start spends only BP. This closes the mandatory transitive Start parser gap; don't confuse its optional wallet shape with Complete's Manda reward prev/cur pairs.

## Complete success: exact result pairs, no resource resync

**ReqBattleCompleteCB0xf5f174** gets ret_data, optional achievement and **ParseBattleResultLog0x944d40**. ResultLog calls **ParseBattleResult0x944e68**, moves its RESULT_LOG into a client-side rolling list capped at3 entries, then invokes success callback. There is **no extra JSON log wrapper or bid key** in ResultLog.

The Complete callback does **not call ParseApBp** and ParseBattleResult does not parse AP/BP. Native resource debit/snapshot comes from Start; Complete AP/BP additions would be ignored by this parser chain. Preserve mission/AP state independently and don't apply a second BP debit on successful completion.

Exact result hierarchy, using illustrative fixture counters:

```json
{
  "result_code": 1,
  "ret_data": {
    "user": {
      "battle": {
        "league_level": {"prev":1,"cur":1},
        "win": {"prev":0,"cur":1},
        "lose": {"prev":0,"cur":0},
        "league_win": {"prev":0,"cur":1},
        "rating_point": {"prev":1000,"cur":1010}
      },
      "honor": {"prev":0,"cur":20}
    },
    "card": {
      "2": {"prev":70,"cur":80},
      "4": {"prev":70,"cur":80},
      "1": {"prev":70,"cur":80},
      "5": {"prev":170,"cur":180}
    }
  }
}
```

All balances/increments above are **examples, not original values or a performed fight**. User.battle is retained independently of user: league_level/win/lose/league_win/rating_point pairs are inside battle. Honor pair is **user.honor**, outside battle. League/total win/loss counters must agree with accepted **play_info.is_win**, not a successful HTTP status alone. Preserve actual current values on a zero-reward fixture; omitted pair members parse0 and can destroy displayed progress.

Optional **user.free_iap** and **user.iap** are `{prev,cur}` pairs here (different from ShopBuyGlobal's user.iap{iap_qty,free_iap_qty}). Native branches update CPVDataMgr free/paid balances if those fields are present. Omit them if no Manda reward is modeled. No gold/userEXP/item grant/deck branch is recovered in ParseBattleResult; do not assume mission completion reward fields are consumed or fabricate gifts merely because reference tables advertise potential rewards.

Optional achievement should remain omitted until supported; any nonnull value invokes its parser. Empty[] is not a generally safe substitute. Preserve result1 only for genuinely accepted transactions; non1 follows native error/retry handling.

## Hunter EXP is case4 and is parsed on either outcome

At the end of ParseBattleResult, **ret_data.card** is indexed directly as a map keyed by decimal hunter serials. Entries contain direct **prev/cur absolute EXP**, not exp nesting. Native calls **PlayData.GetDeckInfo(type4)** and iterates that roster, then SetCardExp for nonnull entries. This differs from mission Complete's current mission deck. Missing/null per-ID entry skips its EXP mutation; publish card:{} explicitly for a no-hunter-XP fixture.

**The card map loop is not conditional on winning.** A defeat can return preserved prev==cur or a documented local loss reward; original win/loss XP rule is unknown. Never apply EXP to mission case1 just because its members happen to match current arena team. Before genuine battle, persist/configure real owned **case4** team with known references; keep mission case1 and its active stage/achievements untouched. Empty/default card slots accepted by the rival parser are not proof every Fight Club scene supports an empty attacking team.

Native result initialization/reward log fields and FCPlayData current profile assignments are in the dump; these are distinct from lobby ParseUser's scalar record. Do not pass lobby user.battle scalar values where Complete expects pairs, or reinterpret the result's rank-related pairs as hunter rank promotion. If a particular in-memory field offset is needed, verify its actual register/object base; decompile's SRET/in_r1 aliases are not sufficient pointer-layout evidence.

## Minimal scaffold and remaining fidelity

The recovered seam supports a persisted **separate Arena attempt**: authenticate, select published full rival, validate owned case4 roster, apply a marked local BP cost once (original magnitude unknown), preserve AP and mission state, return Start's flat resource snapshots/full target, then accept matching Complete telemetry once and return exact pair/map receipt. Replays must not advance wins/EXP/wallet twice. Publish resulting scalar own arena data via Enter and valid owned decks via the usual persistence path; don't overwrite successful mission progress or transport/session credentials.

League/weekly reference arrays and lobby records are already recovered in `arena-lobby-contract.md`; rewards/league promotion must stay within published supported rows and explicit local fixtures. Original economy, dates/season schedule, defense/revenge bid rules, friendship charging, reward formulas and enemy stat-bonus scaling remain unknown. RefreshCost0x9476bc is recovered; counterpart battle UI setup/outcome/result consumers are still needed if native behavior contradicts this response model. In particular, don't derive an enemyHP0-only victory rule from the response parser without checking FC.OnFinish0x947ad4 / native time-over behavior.

Implementation acceptance: Start wire target/flags/bid matches the selected rival; BP changes once and AP stays unchanged; player's case4 team and full enemy references render; real win/loss emits is_win telemetry; Complete pairs/HunterEXP/rating/honor and receipt agree; duplicate request/restart preserve once-only state; returning to campaign preserves mission party/stars/AP. Until those native controls pass, this is reconstructed protocol, not verified functional Fight Club combat.
