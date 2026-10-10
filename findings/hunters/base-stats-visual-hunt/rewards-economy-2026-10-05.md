# Rewards / economy lane log — 2026-10-05

**Lane:** mission clear payouts, first-clear vs replay, capsule drops, trace
thresholds, gacha prices, AP/BP shop tiers, login calendar, Special Supply,
Episode chapter rewards, chest rewards, training costs, arena receipts.
**Rule:** every value below is tagged **RECOVERED** (native parser / original
shipped data / public video frame), **FIXTURE** (local `server-ts` policy), or
**UNKNOWN**. Local server values (10 gold, 30 XP, 10 AP, 100 gold/day, ...) are
**never** original-game facts.
**Read-only:** no server/APK/state changes in this lane.

Related: `AGENTS.md` 16-18 (economy fixtures), 84-85 (capsule/trace),
90 (Special Supply), 93 (E05), `analysis/research/base-stats-visual-hunt/README.md`,
`analysis/research/vsfan-material-index.md`.

---

## A. Local fixture inventory (FIXTURE — do not cite as original)

Sourced from `server-ts/src/*.ts` + `openapi.ts` descriptions, read 2026-10-05.
These are the numbers the replica currently pays; none is a recovered original
balance.

| System | Fixture value | Source file |
|---|---|---|
| Mission first-clear gold | **10** (`FIXTURE_STAGE_CLEAR_GOLD`) | `state.ts:258`, paid at `state.ts:1892` |
| Mission first-clear user EXP | **30** (`FIXTURE_STAGE_CLEAR_EXP`) | `state.ts:259`, paid at `state.ts:1893` |
| Mission star floor / first-clear stars | **3** (`FIXTURE_STAGE_CLEAR_STARS`) | `state.ts:260` |
| Mission hunter (card) EXP | **10** per participant, up to 4 snapshotted party members, replays included | `bootstrap.ts:1046-1047`, `openapi.ts:788` |
| Replay gold/user-EXP | **0** (first-clear only); replays can earn missing star flags without re-paying gold/XP | `state.ts:1892-1893`, AGENTS 21 |
| Star-flag evaluation rules (Complete / Under60s / <=1 straggler) | **local policy** evaluated from native metrics | AGENTS 21 |
| Search capsule earning | **1 x AIRSHIP_TICKET per new matching normal campaign victory** (incl. new replay attempts); no loss/duplicate/standalone/retroactive grants | `search-capsules.ts`, `search-capsule-earning.md` |
| Search Begin cost | **1 capsule** debited once; one initial guided attempt at capsule 0 is a LOCAL recovery waiver (earned stage8 + actual 37/0 ack + pending 37/1) | `openapi.ts` Begin entry, `search-battle.ts` |
| Search Retry / Reset quotes | **Retry 10 / Reset 30 Manda**, type1, free-first — fixtures | `hunter-search.ts:22`, `openapi.ts` GetInst/Reset entries |
| Trace thresholds | **Sylvester 006: 10, Gerard 005: 20** (`collect_qty`) — local navigation fixtures | `hunter-traces.ts:9-10` |
| Trace exchange debit | `count x collect_qty`; `cnt` = hunters requested, not traces spent (mechanism RECOVERED, quantities FIXTURE) | `trace-exchange.ts:29`, `trace-recruitment-contract.md:44-46` |
| Gacha nonstandard counts/prices | only 1 and 11 supported; anything else refused | `openapi.ts` Gacha entry, `game.ts:308` |
| AP shop | **local_ap, +10 AP**, Manda tier **5** / gold tier **100** per buy-count 1..3; shared **3 purchases/resource/UTC-day** across currencies | `shop-fuel.ts:1-5`, `openapi.ts:336` |
| BP shop | **local_bp, +5 BP**, Manda **5** / gold **100**, 3/resource/day | `openapi.ts:336` |
| Supply daily fuel | **local_fuel_0, +10 AP**, once per UTC day | `supply.ts:5-6,24-25,30`, `openapi.ts:351` |
| Login Bonus calendar | **28 entries x 100 gold**, one observed-UTC-visit per day, no catch-up/cycle | `login-bonus.ts:2`, `openapi.ts:656` |
| Special Supply earning | **10 gold** per future newly accepted matching explicit normal-stage first victory, independent of capsule capacity | `special-supply-implementation.md:4-8` |
| Area chest payouts | **300 / 200 / 100** gold tiers — fixture amounts; claim mechanism is RECOVERED (B.6) | `openapi.ts:880` |
| Raise training | **100 gold/source**, source XP **100 x level**, cumulative target XP **100 x (level-1)**, cap Lv30 | `openapi.ts:367`, `gym-legitimate-donor-budget.md` |
| Skill training | **100 x destinationLevel gold**, zero materials; caps 10/20/30/40/50 per grade (community inference) | `skill-training.ts:20`, `openapi.ts:310,318` |
| RankUp | **1000 gold/source**, +5% stat bonus per credited material; capacity = current rank (community rule) | `openapi.ts:326` |
| Arena settlement | **honor 10, rating +10 win / -10 loss, 6 wins per league**; league/weekly row rewards fixtures | `openapi.ts:630`, `arena-lobby-contract.md:80` |
| Starter wallet balances seen live | gold **11230**, paid **240000** / free **~239940** Manda — research-state balances, not original economy | `gym-legitimate-donor-budget.md:3` |
| AP/BP regen intervals | **300 s AP / 1800 s BP** — fixtures | AGENTS 18 |

---

## B. RECOVERED native / original-data values

### B.1 Gacha prices — RECOVERED (native constants)

- **Single = 30, bundle (10+1 / 11 cards) = 300**, direct wire units, no x100
  divisor. `CSRDataMgr::Init 8b1d60` constant vector `[100, 300, 11, 30]`;
  `CSRSceneLottery::OnClickRequestGachaByManda e40824` loads price 300/count 11
  and price 30/count 1; `PurchaseConfirm::SetData` renders price via
  `to_string<unsigned>` with no division. Affordability = price <= paid + free
  (summed wallet). Consumption order (free-first vs paid-first) is UNKNOWN;
  server free-first is local policy. Source: `recruitment-price-currency.md`.
- Single-result shape is count-dependent: cnt1 yields single OBJECT, cnt>1
  yields ARRAY, cnt0 yields null (`CSRSyncLottery::ReqGachaPremiumCB f753f8`).
  Mechanism RECOVERED; pool contents/probabilities are FIXTURE (one
  deterministic bundle + last-draw 3-star-guarantee substitution). Sources:
  `gacha-single-result-contract.md`, AGENTS 26, 59.

### B.2 Mission Complete wire contract — RECOVERED (shapes/mechanism, not amounts)

- 8-field form POST; `play_info` JSON string with 10 alphabetically-serialised
  keys (`atk_cnt, atk_total, clear, clear_time, dead_cnt, enemy_total_hp,
  enemy_total_hp_max, item_use, player_total_hp, player_total_hp_max`).
  `result_code: 1` on **every** outcome incl. defeat; loss is carried by payload
  (`achieve: []`, `gold.prev == gold.cur`), never by the code.
- `achieve[]` = ARRAY of `{order: 0..2}` — the **only** progression write
  (`SetStageAchieve`); star/prev_star/is_first_clear are client-derived.
- Reward carriers: `user.gold.{prev,cur}` (village counter),
  `user.exp.{prev,cur}`, `user.{ap,bp}.{prev,cur}` + charge times,
  `card[<serial>].{prev,cur}` absolute EXP map, `item[]` additive
  `{inst_id, ref_id, added}` delta. `detect`/`achievement`/`scenario` omission
  is load-bearing (null-guarded branches). Sources: `battle-lifecycle.md` 2-5,
  `battle-completion.md`, AGENTS 16.5.
- Live native `play_info` examples (LOCAL fixture receipts, not original
  balance): stage2 win `atk_cnt1, atk_total181, clear1, clear_time1, dead0`;
  stage5 win `clear1, time118`; Search End `atk_cnt2, atk_total362, clear1,
  cleared_wave2, enemyHP0/max200`. Sources: AGENTS 16.5, 21-22, 32, 74, 80.

### B.3 Capsule identity — RECOVERED (ID only)

- `AIRSHIP_TICKET` is the original Hunter Search capsule reference, proved by
  HunterSearch `UpdateCurrency` direct inventory lookup. Preserved tutorial
  line 66 visibly says capsules come from clearing general stages. Drop
  amount/rate/shop price/`use_type`/metadata are UNKNOWN; server `use_type0`
  is fixture. Sources: `search-capsule-content.md`, `search-capsule-earning.md`,
  `episode-reward-materials.md:17`.
- No invented capsule purchase/price exists
  (`search-capsule-purchase-contract.md`).

### B.4 Trace exchange mechanics — RECOVERED (route/shape/arithmetic, not counts)

- Route `/shop/PieceExchange`, keys `app_code app_ver market pvid otp
  item_inst_id cnt` (`RequestShardExchange Gf8a894`). Success returns card
  **ARRAY** (even single award) + `consumed_inst_list[{inst_id, qty}]` delta
  (`ReqPieceExchangeCB Gf8af68`); `cnt` = hunters requested;
  max = floor(owned_qty / collect_qty) (`Gce1252..1262`); capacity pre-check.
  Threshold values (10/20) are FIXTURE (A). Source: `trace-recruitment-contract.md`.

### B.5 Episode chapter rewards — RECOVERED (original declarations)

From `analysis/recovered-reference/EPISODE_S01.json` (original `R_EPISODE.jet`,
SHA `7f4362cd...`, 18 episodes / 128 stories / 147 unique IDs). Exact original
`reward.item[].ref_id/qty` declarations, all with `free_iap: 0`:

| Chapter | Reward (original) |
|---|---|
| E01 | **GC2 x3** |
| E02 | **FMD1 x30** |
| E03 | GC3 x3 + GC4 x3 |
| E04 | GC8 x1 |
| E05 | **AIRSHIP_TICKET x20** |
| E06 | OV1 x10 |
| E07 | CERUM01 x20 |
| E08 | CERUM02 x20 |
| E09 | CERUM03 x20 |
| E10 | SK13 x30 + SK23 x30 |
| E11 | SK33 x30 + SK43 x30 |
| E12 | EM02 x2000 |
| E13 | LCOIN x20 |
| E14 | OV1 x30 |
| E15 | GC9 x1 |
| E16 | GC10 x1 |
| E17 | GC11 x1 |
| E18 | RP1 x100000 |

Identities proved: GC2 = owned Lottery coupon (inventory lookup `SetCurrency
Ge3e43c`, coupon branch `OnClickRequestGachaByCoupon Ge40020`); FMD1 =
free-Manda display identity, RP1 = gold display identity
(`ParseLoginBonusRef Gf4ae7c` synthesises both); exact coupon tier/prices and
whether Episode-item-form FMD1 credits currency are UNKNOWN. Item
`use_type`/`effect`/`collect_qty` for all of these are UNKNOWN — do not invent
reference rows from reward IDs. Only E05/AIRSHIP_TICKET has a server claim
(all-8-leaf-cleared gate is conservative LOCAL policy). Event EV05 schedule
2020/2021 is expired — do not reopen. Sources: `episode-reward-materials.md`,
`episode-reward-contract.md`, AGENTS 91-93.

### B.6 Chest/area-reward mechanics — RECOVERED (mechanism, not amounts)

- `achieve_reward[]` rows `{area_id, achieve_cnt, gold, free_iap, iap,
  item_list, card_list}`; three chests drawn per area; `achieve_cnt` MUST equal
  `GetStageCnt(area) x (i+1)` (i.e. **10/20/30** for 10-stage areas).
- Claim route 7-field form (`area_id, target_achieve_cnt` = reference value, not
  index); receipt `achieve_cnt` must match a published row or the chest never
  opens (`cb(-1,0)` then toast). Gold lands only when `gold.prev != 0`.
  Payout **amounts** 300/200/100 are FIXTURE. Sources: `chest-rewards.md`,
  `openapi.ts` chest entries, AGENTS 21 (claimed-chest row shape).

### B.7 Shop/price lookup mechanics — RECOVERED (matching rules, not values)

- `GetGlobalItemPrice 0xaf155c`: exact `(buy_cnt == requestedCount)` match, no
  cap-to-last fallback; missing match returns 0 = must refuse, never free.
  `GetItemInven` shape `ret_data{item[], global_item[{item_id, price_type,
  buy_cnt}]}` scalar counters. AP effect is a STRING ("10"). Amounts/prices/
  reset/limits are FIXTURE. Source: `shop-fuel-price-and-inventory.md`.
- LoginBonus reference rows `{target_cnt, gold, free_iap, item_list(JSON str),
  card_list(JSON str)}`, dense 1..N; zero-index claim crashes before HTTP.
  Receipt `reward.user.gold.cur`. Calendar **contents** (28x100) are FIXTURE.
  Source: `attendance-contract-next.md:61-86`.
- Special Supply claim: `SpecialListReward` with `id_list` JSON-array STRING;
  receipt `target_inst_id[]` numerics + `user.gold prev/cur`. Quantities are
  FIXTURE (gold-only so far). Sources: `special-supply-contract.md`,
  `special-supply-implementation.md`.

### B.8 Training reference mechanics — RECOVERED (keys/indexing, not economy)

- Skill price indexes `roleVector[destinationLevel-1]` (destination = owned+1);
  batch sums intermediate destinations. Rank caps 10/grade are community
  inference; prices/materials/XP curve are FIXTURE. Sources:
  `skill-level-reference.md`, `skill-zero-level-eligibility.md`, AGENTS 23, 32.
- Character cap **30 regardless of grade** is historical community evidence
  (Namu fn36 + 2018 Lv30MAX screenshot), not a captured server row; XP curve
  and costs remain FIXTURE. Sources: `hunter-level-caps.md`, AGENTS 24.
- RankUp partial arithmetic (`p+n<C` retains, `==C` promotes) is inferred from
  native math; thresholds/costs/bonuses are FIXTURE. Sources: `rank-up-*.md`.

---

## C. Public-source reward rows (provenance each)

### C.1 Community FAQ guide — `recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md` (13 MB)

Text-guide mechanics (content evidence, not wire proof). Line numbers from grep
2026-10-05:

| # | Claim | FAQ location | Status |
|---|---|---|---|
| 1 | 4-star banner guarantee after **16 pulls (4,800 Manda)** — implies **300/pull**, consistent with native 30/300 scale | L175 | SUPPORTS native 300 price; guarantee rule itself is community text |
| 2 | 10-gem pull **250 Manda**; gem inventory cap **300** | L368 | Community evidence, no native confirmation in this lane |
| 3 | Mileage: **78 scrolls total** (any 1-3/2-3/3-4-star, selection or not) to legendary scroll | L291 | Community evidence |
| 4 | Awakening costs **A1 = 30 crystals + 30k rupees, A2 = 50 + 100k, A3 = 100 + 150k** (total 180 crystals + 280k rupees + 9 hearts) | L502-504 | Community evidence (historical balance, version-sensitive) |
| 5 | Jewel refine risk rises after Lv9+; budget **>=600k rupees** | L426 | Community evidence |
| 6 | Best farming stages **450-490+**; stages ending **6/7/8/9** drop Attacker/Defender/Bomber/Healer materials; **Rupee tickets gather at any stage** | L239-249 | Community evidence |
| 7 | Missing-hunter ruins: since **2019-04-01**, rewards are **traces + metron fragments only** (crystals, scrolls, large rupee amounts removed); ruins use **Helium Capsules, not fuel** | L265 | Community evidence; Helium-to-AIRSHIP_TICKET crosswalk UNPROVED — keep separate |
| 8 | Ruins/Co-op original loot + mileage photos embedded as images image1-image6 | L267-293 | Unmined image lead (see E) |
| 9 | 4-star traces buyable in Mirage/Blitz shops; Fight Club shop: golden-trim materials or 4-star traces | L235 | Community evidence |
| 10 | Guild-leave lockout **1 day**; rupee donation "extremely expensive, NOT recommended" | L445-447 | Community evidence |
| 11 | 28-day Legendary 4-star Selection scroll exists (Genovia/Lottery Mouse advice) | L87-89 | Existence only, no reward-table values |

### C.2 Official balance-era anchor — TapTap announcement (RECOVERED text, no per-item values)

- Posted **2019-09-04**, effective after 2019-09-05: equipment stats **+50%**;
  1-3-star crystal mains **+30%**; 4-5-star mains **+50%**; all crystal substats
  **+50%**; larger gains after equipment Lv20; set bonuses raised (no delta).
  URL: `https://www.taptap.io/post/73656`. No per-item/hero/monster anchors —
  stratify pre/post-2019-09-05 screenshots as separate eras. Does not change any
  payout value. Source: `stat-version-context.md`.

### C.3 HungryApp review — checked, no reward values

- 5 gameplay images (story dialogue, Bella recruit, battle HUD, twin-recruit
  victory art, guild victory-reward screen with guild-wide total-power
  thresholds). No individual payout/reward table. Article prose not used as
  stat evidence. Source: visual-hunt `README.md` HungryApp row.

### C.4 VSFan archive — economy context, no payout tables

- `Bugs/Screenshot_20170813-164411.png`: Veteran **Expert 1, 1290/2560 pts**;
  benefits incl. Special Support Fuel +5, Fuel Recharge +7, Rupee Exchange +7,
  Challenge Invitations Recharge +7. One 2017 account state, not canonical rates.
- Story-to-Fate screen: account HP/Atk/Def bonuses **1-4%**; one visible Fate
  row **Health +2%** with "Less than 30 sec." condition.
- `Screenshot_20170820-224858`: **Collect Hunter Traces** event (Lottery Mouse,
  1- and 3-trace options) — event UI only, no exchange price.
- `Screenshot_20170820-225950`: **Teddy Bomber's Trace x30** — collectible
  description, not hunter stats or price.
- Captures are TLS/encrypted bodies; endpoint list only (Extra/Area/Stage/Card/
  Item/Supply/Monster/StageMonster/Level/CardRankUp/CardEnhancePrice/Shop/Gacha/
  Battle/Abyss...). No numeric payout recovered. Source:
  `vsfan-research-material.md:71-87,101-102`.
- 1.4.4.1 in-game help: all 12 jewel set bonuses (Super Block KO 9% vs other
  locales 5%) — set-bonus catalog only, no economy. Source:
  `vsfan-material-index.md:22`.

### C.5 Video result screens — observed receipts (LOCAL fixture amounts)

Native-rendered victory/result frames from local-replica runs. They prove
**result-screen rendering and receipt plumbing**, not original payouts:

| Observation | Source | Status |
|---|---|---|
| "Victory!" + 3 star conditions + Team Lv1 + Collected Rupees 0 (exit-door win, monster alive 138 HP) | `analysis/r017-03-AFTER-EXIT-8s.png`, AGENTS 16.1 | RENDER proof; 0-rupee receipt is fixture behavior |
| Stage7 result: **4 hunter XP bars + 10 Rupees**, flags 0/2 | testing screenshot 14, AGENTS 34 | Fixture receipt (+10 char EXP each) |
| 20-star chest claim pays local **200 gold** (gold 10660 final path) | AGENTS 69 | Fixture payout |
| First Search victory trace receipt: trace inst6 qty1, then qty2 after funded run | AGENTS 74, 80 | Fixture accrual (1/victory local rule) |
| Ordinary n_01_07 victory earned AIRSHIP_TICKET inst7 qty1; Search136 showed capsule1; costed Begin debited 1 to 0 exactly once | AGENTS 80 | Fixture earn/spend plumbing proof |
| Guided Search win awards published `collect_qty` **10** (vs ordinary 1) | AGENTS 85 | Fixture policy (`attempt.guided` split) |
| External videos (CGPMobile Part 1, Errorflame ep1, Ryu33s Twins/Windblade, P J 46-50, Suhugame 3-star summons) | visual-hunt README rows | Sampled: gacha/recruit/victory-rating frames seen; **no legible gold/XP/reward numerals transcribed** in this lane — result-screen mining is the open video task (see E) |

---

## D. UNKNOWN list (do not fill without evidence)

1. Original mission clear gold / user EXP / hunter EXP per stage or per area.
2. Original first-clear vs replay split (gold once? stars re-earnable? — replay
   flag improvement is RECOVERED mechanism; original replay *amounts* unknown).
3. Original star-condition definitions per stage (default 3-condition set is
   local policy; `achieve_condition` per-stage text is shipped but undecoded
   as reward rules).
4. Original capsule drop source/rate/quantity (per-stage? ruin-only?
   Helium crosswalk?).
5. Original trace thresholds per hunter (10/20 are fixtures); original
   PieceExchange cnt/slider/price semantics beyond recovered arithmetic.
6. Original gacha pool contents, probabilities, pity/mileage values (16-pull
   and 78-scroll rules are community text, not native proof).
7. Original AP/BP shop amounts, prices, limits, reset cadence; BP economy as a
   whole; ticket path.
8. Original login/attendance calendar contents, cadence, catch-up, cycle.
9. Original Special Supply triggers/amounts/cadence (gold-only local row is a
   seed, not history).
10. Original Episode material settlement for GC*/FMD1/SK*/EM02/LCOIN/OV1/CERUM*/
    beyond E05 capsules (reference rows + redemption handlers missing).
11. Original chest payout amounts per threshold.
12. Original Raise/Skill/RankUp XP curves and gold costs (all current numbers
    are fixtures preserving old thresholds, not captures).
13. Original arena league/weekly rewards, rating formula, honor economy.
14. Original AP cost per stage entry (replica charges 1; native cost field
    `ap_cost` exists per stage but no original per-stage table is published),
    defeat-refund policy ("fuel returned" loss text seen live, amount unknown).

---

## E. Sources checked / negative results and next leads

- `AGENTS.md` full read (economy-relevant 16-18, 21, 23-24, 26, 28-29, 32-36,
  59, 66-67, 69, 72-74, 80-85, 87-90, 91-95); `base-stats-visual-hunt/README.md`
  full (all gallery/video rows); `vsfan-material-index.md`,
  `vsfan-research-material.md` (economy grep); `episode-reward-materials.md`,
  `recruitment-price-currency.md`, `shop-fuel-price-and-inventory.md`,
  `search-capsule-earning.md`, `trace-recruitment-contract.md`,
  `battle-lifecycle.md` 390-509, `chest-rewards.md` 340-419,
  `special-supply-implementation.md`, `attendance-contract-next.md`,
  server-ts `state.ts`, `supply.ts`, `shop-fuel.ts`, `login-bonus.ts`,
  `hunter-traces.ts`, `hunter-search.ts`, `search-capsules.ts`,
  `skill-training.ts`, `bootstrap.ts`, `openapi.ts` descriptions.
- Web: `Blustone mission clear reward gold XP star victory rupees` (no usable
  payout source — Facebook event posts, Shadowverse, gameplay videos without
  transcribed numbers); `"Blustone" hunter recruit cost manda single 10+1
  gacha price` (no usable source — spam-dominated results). No URLs invented.
- NOT yet mined (concrete next leads, no claim made here):
  1. FAQ embedded images image1-image6 (ruins/co-op loot tables, mileage
     phases) — extract pixel values.
  2. FAQ equipment/jewel cost screenshots (toolbox/upgrade tiers, gem detail
     panels) — economy-adjacent costs.
  3. YouTube result-screen sampling: CGPMobile `4VMg-VMJudU`, Errorflame
     `9fUxOnlmwxg`, Ruh33s `8fEo7cb7fTk`, P J `Ot72M6h4OUI` victory/rating
     frames — transcribe visible Rupees/EXP/stars with timestamps.
  4. Namu hunter-gym gallery (6 images, 503-blocked) — training/rank-up costs
     if it recovers.
  5. VSFan `Intro.mp4` + 30s startup capture — check for visible balances.
  6. 2019 Japanese hunter-database profiles — no economy, skip for this lane.
  7. Caragublu guide images 2-6 (already stat-screened; recheck for visible
     cost/reward numerals without touching prose claims).

---

*Written 2026-10-05. No server/APK/state changes. All fixture amounts are local
policy; all original balances remain UNKNOWN except the Episode chapter table
(B.5) and native price constants 30/300 (B.1).*
