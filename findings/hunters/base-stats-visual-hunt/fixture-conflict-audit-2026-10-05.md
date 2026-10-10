# Fixture conflict audit — 2026-10-05

**Purpose.** One row per local `server-ts` economy/numeric fixture value, placed
beside **every** piece of recovered original evidence that bears on it, with an
explicit verdict. This is a read-only evidence audit: **no server code, fixture
value, seed, state file or APK was changed, and none is proposed to be changed
here.** The repository owner decides any retune.

**Scope.** Training (Raise / skill / RankUp / level curve), campaign economy
(clear payouts, stars, fuel, chests), **Episode**, **AP/BP**, **gacha**, **shop**,
**Supply / login bonus / special supply**, **arena**, and the battle numerics
that the base-stat lane already cares about (monsters, card stats, stage
multipliers).

**Inputs.**

| Input | Role |
|---|---|
| `transcendence-skill-cost-2026-10-05.md` | two-source cost tables ([EN-2017], [NAMU]) + [HELP-1.4.4.1] first-party help; §1.4/§1.5/§2.12 supply the replica-side readings |
| `rewards-economy-2026-10-05.md` | §A the fixture inventory; §B the RECOVERED/UNKNOWN columns |
| `training-rankup-rules-2026-10-05.md` | §1 the 15-row rule comparison (MATCH / GAP / UNIMPLEMENTED); §2a–2d the era-tagged archive numerals |
| `server-ts/src/*.ts` | the live fixture values themselves, re-read this pass so no row depends on a stale inventory |

**Verdict scale (used verbatim in every row).**

- **CORROBORATED** — recovered evidence independently supports the fixture's
  value *or* its shape: a native parser, original shipped data, first-party
  in-game help, or two independent community sources with matching numerals.
- **UNCONTRADICTED** — evidence genuinely bears on the row and is consistent with
  it, but does not confirm the value.
- **UNSUPPORTED** — no evidence constrains the value. It is unconstrained local
  policy. This is the expected verdict for most economy numbers and is **not** a
  criticism of the labelling, only of recoverability.
- **CONTRADICTED** — evidence states a different value, or excludes the fixture
  value.

**Evidence-class column.** Class is stated per row because it changes how much a
verdict can be trusted:

- **[NATIVE]** native parser / decompile / runtime — strongest available class.
- **[ORIGDATA]** data or prose shipped inside the original client (`UI_CSV`
  `HELP_DATA`, `R_EPISODE.jet`, `CHAR_STR_RO`, recovered CSV).
- **[COMM]** community prose (one source, or two that agree).
- **[SELF]** the replica's own captured receipts — proves internal coherence only.

**Era rule.** [EN-2017] and the 2018-12 Caragublu screenshots are
PRE-2019-09-05; `blustone.jp` guide captures (2019-11-13 / 2019-12-11) are POST;
the Namu wiki is ERA-UNRESOLVED. Local fixtures carry no era. Nothing in §1
decides an era-stratified conflict; §2.4 does.

**Coverage effect: none.** Heroes 1/113, accessories 1/100, monsters 0/22 are
unchanged by this file. Not one row below is a hero, accessory or monster base
stat that could be credited.

**Not done this run, deliberately:** `polluted-observations.md` was **not**
appended (the parent mirrors this file).

---

# 1. PURE — fixture value vs recovered evidence, row by row

Nothing in §1 is inference. Values are reproduced as stored; the evidence column
reproduces what each source states; the verdict is the audit's classification.
All *reasoning* is deferred to §2.

## 1.A Skill training

| # | Fixture field | Local value (source) | Recovered evidence bearing on it | Class / era | Verdict |
|---|---|---|---|---|---|
| A1 | Skill gold | `gold: 100 * (index + 1)` per level → L1=100 … L50=5000 (`skill-training.ts:20`) | [EN-2017] prices by **band**: L1–4=100, 5–9=200, 10–14=300, 15–19=400, 20–25=500, 26–29=600, 30–34=700, 35–39=800, 40–44=900, 45–49=1000 | [COMM] ×2 / PRE + ERA-UNRESOLVED | **CONTRADICTED** |
| A2 | Skill index basis | dense 50 rows/role; price getter `roleVector[destinationLevel-1]` (`skill-training.ts:18-23,31-33`) | native `GetCardSkillUpPrice(role, level)` returns `vector[level-1]`, destination = owned+1; batch sums intermediate destinations | [NATIVE] | **CORROBORATED** |
| A3 | Skill materials | `source_1..4_ref_id: ""`, all four `qty: 0`, every row, every role (`skill-training.ts:21-22`) | [EN-2017] and [NAMU] agree cell-for-cell: role material required **from level 5**; ladder `0/0/0, 1/0/0, 2/0/0, 3/0/0, 4/1/0, 5/2/0, 0/3/1, 0/4/2, 0/5/3, 0/6/4` | [COMM] ×2 / PRE + ERA-UNRESOLVED | **CONTRADICTED** |
| A4 | Skill fragments | none published — no fragment/Metron quantity appears in any skill row | [EN-2017] decadal 1–9→1, 10–19→2, 20–29→3, 30–39→4, 40–49→5; [NAMU] same after §2.4 resolution. **First-party corroboration is 1.4.4.1-ONLY and lapses:** [HELP-1.4.4.1] `CONTENTS6_1` names Metron Crystals **and** skill materials as the two Abyss currencies, but shipped [HELP-2.8.0.1] `CONTENTS6_1` names only "Metron Crystal", the skill half moved to `CONTENTS6_4` as "skill training items", and the phrase "skill material" occurs in **0** 2.8.0.1 records — the *system* identity survives across two records, the single-sentence proof does not | [COMM] ×2 (PRE + ERA-UNRESOLVED); [ORIGDATA] now **1.4.4.1-only**, not a shipped-build fact | **CONTRADICTED** — unchanged, because it rests on the two community sources; the §2.1 tally is unaffected **[corrected 2026-10-05 per `help-2_8-sweep-2026-10-05.md` §2.5(a) / §2.8 NEW-1]** |
| A5 | Skill caps per grade | `rank: Math.ceil((level+1)/10)` → 10/20/30/40/50 (`skill-training.ts:20`) | [NAMU] "hunter grade raises skill max level by 10 per grade"; [EN-2017] band 10 implies a 50 ceiling at 5★; [HELP-1.4.4.1] `CONTENTS4_4` describes the five slots | [COMM] ×2 + [ORIGDATA]; native `GetCardSkillMaxLevel` = max row.level with `row.rank ≤ hunter rank` | **CORROBORATED** |
| A6 | Zero→1 skill upgrade allowed | 0-owned slot may be initialised, priced at destination level 1 | native `Select` (`d55bfc`) has no positive-owned-level gate and passes `ownedLV+1` to the price getter; native popup null-guards unselected slots | [NATIVE] | **CORROBORATED** |
| A7 | Skill slot semantics | 5 mandatory slots, `skill_1` active-effect row only under `BLUSTONE_ACTIVE_SKILLS=fixture`, otherwise `effect: []` (`skills.ts:32-44`) | [EN-2017]'s five-skill semantics map one-to-one onto [HELP-1.4.4.1] `CONTENTS4_4` (active damage / secondary / permanent passive / chance additional / regular unique) | [COMM] + [ORIGDATA] | **CORROBORATED** (five-slot model); magnitudes remain [COMM]-free |

## 1.B Raise, character levels, RankUp

| # | Fixture field | Local value (source) | Recovered evidence bearing on it | Class / era | Verdict |
|---|---|---|---|---|---|
| B1 | Raise cost | `trainingPrices.level = [100]` → 100 gold/source (`training.ts:5`) | none. `training-rankup` §1 row 15: "no numbers on the training guide page" | — | **UNSUPPORTED** |
| B2 | Source XP | `upgrade_exp: 100 * (index + 1)` (`hunter-levels.ts:9`) | none; native `GetCardRaiseExp` consumes the row, the row is fixture | [NATIVE] mechanism only | **UNSUPPORTED** |
| B3 | Cumulative target XP | `min_exp: 100 * index` (`hunter-levels.ts:8`) | none | [NATIVE] mechanism only | **UNSUPPORTED** |
| B4 | Ordinary level cap | 30 rows per rank, ranks 1–5 (`hunter-levels.ts:6-7`) | [NAMU] fn36 "Lv30 regardless of grade"; Caragublu 2018-12 Natalia 3★ Lv30MAX + 3★MAX→4★Lv1 screenshots; native `GetCardMaxLevel` returns the **last row's level** (configurable) | [COMM] + [ORIGDATA] image; native gives shape | **CORROBORATED** |
| B5 | `sell_price` | `0` for all 30×5 rows (`hunter-levels.ts:10`) | [blustone.jp 2019-11-13 POST] 1–2★ sell for rupees, 3★+ yield secret-corner coins; [NAMU] same direction (Lily&Lala 12 coins → 5 traces) | [COMM] ×2 / POST + ERA-UNRESOLVED | **UNSUPPORTED** (and no sell/release route exists, so the 0 is inert) |
| B6 | RankUp material count | `src_cnt: index < 4 ? index + 1 : 0` → 1/2/3/4 for ranks 1–4 (`training.ts:10`) | [blustone.jp POST] "N same-★ partners for ★N" (★3→★4 = three ★3s); [NAMU] "자신과 같은 등급의 캐릭터를 자신의 등급의 수만큼"; native capacity `C` from `GetCardRankUpSrcCnt(currentrank)`, `GetSrcCnt` returns new sources `n` | [COMM] ×2 / POST + ERA-UNRESOLVED, [NATIVE] shape | **CORROBORATED** (ranks 1–4) |
| B7 | RankUp terminal row | rank 5 published with `src_cnt: 0` | no native terminal-UI evidence; guide says ★5 is the ceiling but not what row 5 looks like | [COMM] only | **UNSUPPORTED** |
| B8 | RankUp cost | `trainingPrices.rank = [1000]` → 1000 gold per new source (`training.ts:5`) | only recovered price points are Caragublu 2018-12 rank-up previews **8000 / 12000** (source count in the preview not recoverable) | [ORIGDATA] image / PRE | **UNSUPPORTED** |
| B9 | RankUp stat bonus | `stat_bonus: 5` → ×1.05 per credited material (`training.ts:10`) | native `CSRCard::Validate` computes `promotion_factor = 1 + (stat_bonus/100) × rank_up_cnt` | [NATIVE] formula only | **UNSUPPORTED** (coefficient) |
| B10 | RankUp EXP/counter transition | promote: rank+1, `rank_up_cnt`→0, EXP→0; partial: retain (`training.ts:27-29`) | native `SetPromotion(L)` resets level→1 + rank+1 **in the preview analyzer**; no captured partial/full server response exists | [NATIVE] preview only | **UNSUPPORTED** |
| B11 | RankUp and skills | promotion preserves trained skills; no auto-unlock; newly eligible zero slots must be trained by a real `SkillUp` | native `SetRank` changes max level but does **not** call `SetSkillLV`; `ReqRankUpCB` parses no skill levels; [blustone.jp POST] guide states a new skill is learned on rank-up | [NATIVE] + [COMM] / POST | **UNCONTRADICTED** |
| B12 | Partners per Raise | refuses >5 before any mutation | [blustone.jp 2019-12-11 POST] "1回で最大5人"; native five-source limit in selection (`G101de2e..3c`) | [COMM] / POST + [NATIVE] | **CORROBORATED** |
| B13 | Fodder eligibility | publishes 005/006 as eligible sources; 001–004 excluded; filter = whitelist + minimum STAT rank | native `SearchStuff` ctor `101f9bc` builds the rank1 and rank2 whitelists and filters on minimum STAT rank, not recruit grade; [blustone.jp POST] "★1–★2 recommended" | [NATIVE] + [COMM] / POST | **CORROBORATED** (direction) |
| B14 | Rank-up live preview | 500 gold for five LV1 partners, target LV2→LV7 | AGENTS §60 — a local receipt, no original anchor | [SELF] | **UNSUPPORTED** |

## 1.C Campaign / mission economy

| # | Fixture field | Local value (source) | Recovered evidence bearing on it | Class / era | Verdict |
|---|---|---|---|---|---|
| C1 | First-clear gold | `FIXTURE_STAGE_CLEAR_GOLD = 10`, paid once (`state.ts:258,1949`) | none. Native applies `reward.user.gold.cur`; no original amount exists on hand | [NATIVE] carrier only | **UNSUPPORTED** |
| C2 | First-clear user EXP | `FIXTURE_STAGE_CLEAR_EXP = 30` (`state.ts:259,1950`) | none | [NATIVE] carrier only | **UNSUPPORTED** |
| C3 | Hunter EXP per win | `character_exp: 10` per snapshotted participant, ≤4, replays included (`bootstrap.ts:1047`, `state.ts:1916-1929`) | none; native `card[<serial>].{prev,cur}` absolute-EXP map is recovered, its amount is not | [NATIVE] carrier only | **UNSUPPORTED** |
| C4 | Per-stage published economy fields | `gold: 10, character_exp: 10, group_exp: 10` on every stage record (`bootstrap.ts:1046-1048`) | field names recovered from `CSRGameStage::SetStage`; values invented | [NATIVE] field set only | **UNSUPPORTED** |
| C5 | Stars per clear | `FIXTURE_STAGE_CLEAR_STARS = 3` → `achieve[]` length 3, `order` 0..2 (`state.ts:260,274-276`) | native `SetStageAchieve(stage_id, order)` write-through; `GetStageAchieveCnt` sums exactly **three** bytes | [NATIVE] | **CORROBORATED** (three-condition structure) |
| C6 | The three star conditions | Mission Complete / Under 60 s / ≤1 Straggler, evaluated from native metrics (`rewards-economy` §A; AGENTS §21) | original per-stage `achieve_condition` text ships but is undecoded as a rule; no original thresholds recovered | — | **UNSUPPORTED** |
| C7 | Replay payout | 0 gold / 0 user EXP on replay; missing flags still creditable | no original replay split recovered | — | **UNSUPPORTED** |
| C8 | Stage entry fuel | `ap_cost: 1` on every published stage (`bootstrap.ts:1045`); `ap_spent: 1` snapshotted at Start (`state.ts:1794`) | native reads `ap_cost` per stage; no original per-stage table exists on hand | [NATIVE] field only | **UNSUPPORTED** |
| C9 | Defeat fuel settlement | a matching active loss returns exactly the snapshotted charge, bounded by capacity or recorded overflow (`state.ts:1908-1910`) | final original `UI_CSV.jet` `HELP_DATA/CONTENTS2_3`: ordinary defeat/forfeit **does not consume fuel** (KO/JA/SC/TC; EN says returned) | [ORIGDATA] | **CORROBORATED** (mechanism); amount inherits C8 |
| C10 | Area chest gold | 300 / 200 / 100 (`bootstrap.ts:523-525`) | mechanism recovered: `achieve_cnt == GetStageCnt(area) × (i+1)` → 10/20/30; receipt applies `gold.cur` only when `gold.prev != 0`. Amounts are not recovered | [NATIVE] mechanism only | **UNSUPPORTED** |
| C11 | Chest item identity | 914 ★4 / 913 ★3 / 912 ★2 "Transcendence Ticket", qty 1 | ids 912/913/914 are `CHAR_STR_RO` rows titled ★2/★3/★4 Transcendence Ticket; both community tables stop at a 4★ self-overcoming ceiling (no 5★ row) | [ORIGDATA] ids + [COMM] ceiling | **CORROBORATED** (ids) / **UNCONTRADICTED** (top chest = ★4) / qty 1 **UNSUPPORTED** |
| C12 | Area `level_limit` | `0` on every area (`campaign.ts:217-218`) | native `CSRSceneAreaSel::SetAreaState` gates on `area.level_limit` vs `GetUserLevel()`; the primary gate (previous area's last stage cleared) is client-side | [NATIVE] mechanism | **UNSUPPORTED** (deliberate safety clamp) |
| C13 | Capsule drop rate | 1 × `AIRSHIP_TICKET` per accepted normal-campaign victory (`search-capsules.ts:22-32`) | original tutorial line (preserved, tutorial 66) states capsules are acquired by clearing general stages. Rate/quantity unknown | [ORIGDATA] for the source, none for the rate | **UNSUPPORTED** (rate); source itself **CORROBORATED** |
| C14 | Special Supply earning | `SPECIAL_CLEAR_GOLD = 10` per future matching first clear (`special-supply.ts:3,19-22`) | none; `SpecialListReward` transport is native-recovered, quantities are not | [NATIVE] transport only | **UNSUPPORTED** |

## 1.D Episode

| # | Fixture field | Local value (source) | Recovered evidence bearing on it | Class / era | Verdict |
|---|---|---|---|---|---|
| D1 | E01 declaration | original `reward.item[]`: **GC2 × 3** (`episode-progress.ts` reads `EPISODE_S01.json` unchanged) | `R_EPISODE.jet` SHA `7f4362cd…`, 18 chapters / 128 stories / 147 ids | [ORIGDATA] | **CORROBORATED** |
| D2 | E01 redemption | unimplemented — coupon gacha refuses with local `GACHA_COUPON_UNRECONSTRUCTED` | native `Lottery.OnClickRequestGachaByCoupon` `Ge40020` → `LotteryShot` → `/shop/GachaPremium` with `item_inst_id` proves the path exists; pool/tier/prices unknown | [NATIVE] path, none for values | **UNSUPPORTED** (deliberate refusal) |
| D3 | E02 declaration | **FMD1 × 30** | original declaration | [ORIGDATA] | **CORROBORATED** |
| D4 | E02 settlement | 30 free-Manda wallet units via `user.free_iap{prev,cur}` | native `ParseLoginBonusRef` synthesises FMD1 as the free-Manda **display identity**; original Episode settlement unavailable | [NATIVE] identity only | **UNSUPPORTED** (explicit replica policy) |
| D5 | E05 declaration | **AIRSHIP_TICKET × 20** | original declaration | [ORIGDATA] | **CORROBORATED** |
| D6 | E05 gate | **all 8 descendant stories** recorded cleared | native chapter claim checks the parent story's clear; parent aggregation is unproved | [NATIVE] parent check | **UNCONTRADICTED** (locally stricter) |
| D7 | E18 declaration | **RP1 × 100000** | original declaration | [ORIGDATA] | **CORROBORATED** |
| D8 | E18 settlement | credited as `user.gold.{prev,cur}` with no RP1 item stack | native `ParseLoginBonusRef` synthesises RP1 as the gold **display identity**; generic `Inventory.AddItem` does not credit gold; `Episode.ParseReward` applies item and user receipts separately | [NATIVE] identity only | **UNSUPPORTED** (explicit replica policy) |
| D9 | E03, E04, E06–E17 (15 chapters) | not implemented; `/episode/Reward` refuses | original declarations recovered: GC3×3+GC4×3, GC8×1, OV1×10, CERUM01/02/03×20, SK13×30+SK23×30, SK33×30+SK43×30, EM02×2000, LCOIN×20, OV1×30, GC9×1, GC10×1, GC11×1 | [ORIGDATA] | **UNSUPPORTED** (unimplemented against known original values) |
| D10 | Episode read/clear encoding | `r_<id>` for Read, bare `<id>` for Clear; `GetLog` retains both in `read_log` (`episode-progress.ts:35-47`) | native `RequestRead` `b19638` prepends `r_`, `RequestClear` `b19710` sends the bare id to the same route; `GetLog.read_log` must retain encoded read **and** clear ids | [NATIVE] | **CORROBORATED** |
| D11 | EV05 event schedule | not reopened; treated as expired 2020/2021 | original declared schedule | [ORIGDATA] | **CORROBORATED** |

## 1.E Hunter Search / traces

| # | Fixture field | Local value (source) | Recovered evidence bearing on it | Class / era | Verdict |
|---|---|---|---|---|---|
| E1 | Capsule identity | `AIRSHIP_TICKET` (`search-capsules.ts:6`) | native Search `UpdateCurrency` direct inventory lookup; tutorial line 66 | [NATIVE] + [ORIGDATA] | **CORROBORATED** |
| E2 | Capsule display name | `"Helium Capsule"`, `use_type: 0`, empty effect (`search-capsules.ts:8-10`) | FAQ: missing-hunter ruins use "Helium Capsules", and since 2019-04-01 reward traces + Metron fragments only. The Helium↔`AIRSHIP_TICKET` crosswalk is recorded **UNPROVED** | [COMM] | **UNSUPPORTED** |
| E3 | Begin cost | 1 capsule per attempt (`hunter-search.ts:16`) | FAQ: ruins consume Helium Capsules (kind of cost corroborated, amount not); tutorial: capsules come from stages | [COMM] + [ORIGDATA] | **UNSUPPORTED** |
| E4 | Onboarding cost waiver | one free **initial** guided attempt, gated on earned stage8 + real `37/0` ack + pending `37/1` + a known selected helper (`search-battle.ts:161-168`) | none | — | **UNSUPPORTED** (local recovery policy) |
| E5 | Search entry limits | `max_join_cnt: 1`, `max_play_cnt: 1`, `max_retry_cnt: 1`, `period: 3600` s (`hunter-search.ts:14-16`) | none | [NATIVE] field names only | **UNSUPPORTED** |
| E6 | Retry / Reset quotes | `retry_price` 10 Manda (type 1), `reset_price` 30 Manda (type 1) (`hunter-search.ts:22`) | none; original prices unknown | [NATIVE] shape only | **UNSUPPORTED** |
| E7 | Abyss reset economy | Abyss list/reset price published **empty**; no reset mechanic | **[HELP-1.4.4.1]-ONLY**, `CONTENTS6_1`: "you can excavate 1 time on a set day, but you can do a **reset up to 3 times** depending on your **Veteran rank**". Shipped [HELP-2.8.0.1] publishes **no reset count and no Veteran-rank cap anywhere** in the Abyss block — it replaces the mechanism with "number of entries every day" regulation plus Manda-bought extra entries | [ORIGDATA] **1.4.4.1-only**; the shipped 2.8.0.1 help is a **negative** for the same claim | **UNSUPPORTED** — and the mechanic is **historical, not current-playable**: the replica's empty reset price is no longer a *first-party-proven* gap on 2.8.0.1, and the reset quantity is unrecoverable from help text in **either** era **[corrected 2026-10-05 per `help-2_8-sweep-2026-10-05.md` §2.5(a) / §2.8 NEW-2]** |
| E8 | Trace thresholds | Sylvester 006 = **10**, Gerard 005 = **20** `collect_qty` (`hunter-traces.ts:9-10`) | [NAMU §1.3] fixed-recruit trace ladder **1★ 20 / 2★ 40 / 3★ 80 / 4★ 160** (stated formula 2^n×10) | [COMM] / ERA-UNRESOLVED | **CONTRADICTED** (see §2.5) |
| E9 | Trace exchange arithmetic | `cnt` = hunters requested; max = `floor(owned_qty / collect_qty)`; capacity pre-check (`trace-exchange.ts`) | native `RequestShardExchange` `Gf8a894` key set; `ReqPieceExchangeCB` `Gf8af68` card ARRAY + `consumed_inst_list` delta; max computed at `Gce1252..1262` | [NATIVE] | **CORROBORATED** |
| E10 | Ordinary Search trace reward | 1 trace per victory (`search-battle.ts:214`) | none | — | **UNSUPPORTED** |
| E11 | Guided Search trace reward | `collect_qty` (10) per guided victory, legacy receipts kept at `[1, 10]` (`search-battle.ts:8,57,214`) | none; the value reuses the *recruitment threshold* as a *reward quantity* | — | **UNSUPPORTED** |

## 1.F Gacha

| # | Fixture field | Local value (source) | Recovered evidence bearing on it | Class / era | Verdict |
|---|---|---|---|---|---|
| F1 | Prices | single 30 / bundle 300 (`game.ts:321-322`) | native `CSRDataMgr::Init` `8b1d60` constant vector `[100, 300, 11, 30]`; `CSRSceneLottery::OnClickRequestGachaByManda` `e40824` loads 300/count 11 and 30/count 1; `PurchaseConfirm::SetData` renders via `to_string<unsigned>`, no divisor; [NAMU] 30/300; FAQ 4,800 Manda / 16 pulls ⇒ 300/pull | [NATIVE] + [COMM] ×2 | **CORROBORATED** |
| F2 | Supported counts | only 1 and 11; any other count refuses | native publishes no other count; the two constants are the whole vocabulary | [NATIVE] | **CORROBORATED** |
| F3 | Bundle grade floor | last draw substitutes an already-published born-grade **3+** reference | native confirmation screen observed live (AGENTS §59) proving a three-star-or-above guarantee | [NATIVE] UI + [SELF] | **CORROBORATED** |
| F4 | Pool contents / probabilities / pity | one deterministic bundle; no probability model | FAQ: 4-star banner guarantee after 16 pulls; mileage 78 scrolls — a **different, unimplemented** guarantee axis | [COMM] | **UNSUPPORTED** |
| F5 | Gacha coupon via `item_inst_id` | refuses any nonzero/malformed `item_inst_id`; zero/omitted keeps paid single/bundle | native coupon path exists (D2) but no tier/pool/odds | [NATIVE] path | **UNSUPPORTED** |
| F6 | Wallet seeds | paid 300,000 + free 300,000 Manda; gold 10,000 (`game.ts:268,297-298,310`) | none; the live research balance (gold 11,230 / 240,000 / ~239,940) is [SELF] | [SELF] | **UNSUPPORTED** |
| F7 | Count-dependent result shape | cnt1 → single OBJECT; cnt>1 → ARRAY; cnt0 → null | native `CSRSyncLottery::ReqGachaPremiumCB` `f753f8` | [NATIVE] | **CORROBORATED** |
| F8 | Affordability / debit order | price ≤ paid + free, **free-first** | native affordability is the summed wallet; consumption order is UNKNOWN | [NATIVE] rule, order not | **UNCONTRADICTED** |

## 1.G AP / BP / Supply / login bonus / resources

| # | Fixture field | Local value (source) | Recovered evidence bearing on it | Class / era | Verdict |
|---|---|---|---|---|---|
| G1 | AP shop item | `local_ap`, `use_type 1`, `effect "10"` → **+10 AP** per purchase (`shop-fuel.ts:4-5,27`) | none. VSFan 2017-08 screenshot shows Veteran **Expert** benefits "Special Support Fuel +5, Fuel Recharge +7" — VIP benefit magnitudes, not shop prices | [ORIGDATA] adjacent only | **UNSUPPORTED** |
| G2 | AP shop prices | Manda 5 / gold 100, tiers for buy-count 1..3 (`shop-fuel.ts:7,32-34`) | none | [NATIVE] lookup rule only | **UNSUPPORTED** |
| G3 | Shared purchase limit | one `buy_limit` = **3** consumed across all currencies (`shop-fuel.ts:6,31`); missing tier ⇒ price 0 ⇒ refuse | native `UpdateText` subtracts GOLD+MANDA+TICKET buy counts from **one** `buy_limit` (+VIP); native `GetGlobalItemPrice` `0xaf155c` matches exact `buy_cnt` with no cap-to-last fallback | [NATIVE] | **CORROBORATED** (shape) / **UNSUPPORTED** (the value 3) |
| G4 | BP shop item | `local_bp`, `use_type 2`, `effect "5"` → **+5 BP**, same prices/limit (`shop-fuel.ts:8-9,28`) | none; BP as an economy is entirely unrecovered | — | **UNSUPPORTED** |
| G5 | Supply free fuel | `local_fuel_0`, **+10 AP**, once per UTC day, `00:00`–`23:59` (`supply.ts:5-6,24-25`) | none; `ParseSupplyInfo` fuel statuses 0/1/2 and the UTC reset field are native-recovered, contents are not | [NATIVE] shape only | **UNSUPPORTED** |
| G6 | Login bonus contents | 28 entries × **100 gold**, one observed-UTC-visit per day, no catch-up, `cycle: 1` (`login-bonus.ts:4-5,32-33`) | native reference rows `{target_cnt, gold, free_iap, item_list, card_list}` dense 1..N, zero-index claim crashes before HTTP; `ParseLoginBonusReward` receipt is `reward.user.gold.cur` | [NATIVE] structure | **UNSUPPORTED** (28, 100, cadence, cycle) |
| G7 | AP/BP regen | 300 s / 1800 s (`game.ts:436`, published at `game-routes.ts:361`) | native resource charge times are next deadlines in server seconds; the interval values are not recovered | [NATIVE] units only | **UNSUPPORTED** |
| G8 | Resource caps | `max_ap: 50`, `max_bp: 10` (`game.ts:266`, `game-routes.ts:361`) | none | [NATIVE] field only | **UNSUPPORTED** |
| G9 | Chest / supply AP overlap | AP is obtainable three ways (kill refill, shop, free Supply) | none | — | **UNSUPPORTED** |

## 1.H Arena (Fight Club)

| # | Fixture field | Local value (source) | Recovered evidence bearing on it | Class / era | Verdict |
|---|---|---|---|---|---|
| H1 | Entry cost | `ARENA_BP_COST = 1` (`arena.ts:7`) | none; native Start carries flat `ap/ap_charge_time/bp/bp_charge_time` scalars | [NATIVE] carrier only | **UNSUPPORTED** |
| H2 | Honor | +10 per win (`arena-service.ts:83`) | none | [NATIVE] pair shape only | **UNSUPPORTED** |
| H3 | Rating | +10 win / −10 loss, floor 0 (`arena-service.ts:83,89`) | none | [NATIVE] pair shape only | **UNSUPPORTED** |
| H4 | League ladder | 6 leagues, `max_win: 6`, promotion at 6 league wins, cap at league 6 (`arena.ts:95-96`, `arena-service.ts:84-86`) | native `ret_data.arena.status == 1` gate, `season`, `user.battle`, `user.is_weekly_reward`, optional `deck`; league row schema recovered | [NATIVE] shape only | **UNSUPPORTED** |
| H5 | League / weekly reward rows | six league rows + one weekly row, every amount **0** (`arena.ts:95-98`) | none | [NATIVE] shape only | **UNSUPPORTED** |
| H6 | Rival refresh price | `price_type 2, price 100` (`arena-service.ts:9`) | `ReqRefreshCost` optional wallet branches recovered | [NATIVE] shape only | **UNSUPPORTED** |
| H7 | Rank / season identity | `rank: 1`, `season_no: 1`, `weekly_no: 1` (`arena.ts:67,76-77`) | native `ReqMyRankCB` `Gf600d8` reads `ret_data.rank`; season datetime arithmetic is seconds (`/86400`) | [NATIVE] field/unit only | **UNSUPPORTED** |
| H8 | Synthetic rival | pvid 9,000,001, all stats 0, deck = published reference 002 (`arena.ts:5,82-92`) | `ParseDefender` iterates `inst_1..inst_N` by container size — shape recovered | [NATIVE] shape only | **UNSUPPORTED** |

## 1.I Battle numerics (the base-stat lane's own subject matter)

| # | Fixture field | Local value (source) | Recovered evidence bearing on it | Class / era | Verdict |
|---|---|---|---|---|---|
| I1 | Stage multipliers | `enemy_atk_per: 100`, `enemy_hp_per: 100` = 100 % / neutral (`bootstrap.ts:1049-1050`) | `analysis/research/stage-multipliers.md`: 100 means 100 %, proven HP/damage paths do not scale by it | [NATIVE] | **CORROBORATED** |
| I2 | Monster base stats | **identical for every published monster**: `hp "100"`, `atk "10"`, `def "5"`, `level 1`, `rank 1` (`bootstrap.ts:1311-1317`) | none. Monster coverage is **0/22**. The only published monster figures anywhere are MON BLAST! (a **different app**, `com.vshower.prd_pf`): Snowfox 17,370/790, Pandahawk 17,460/1,110, Moonwoof 18,080/850, all Lv.10 MAX Gold Card — no entity/scale crosswalk exists | [ORIGDATA] cross-title only | **UNSUPPORTED** |
| I3 | Monster `hp_page` | `100` on every monster (`bootstrap.ts:1325`) | semantics unresolved; proven HP/damage/death functions do not multiply by it | — | **UNSUPPORTED** |
| I4 | Card 001 stat row | `hp 1000, atk 100, def 50, spd 100, crt_chance 5, crt_dmg 150, hp_up 10, atk_up 1, def_up 1` (`bootstrap.ts:90-93`) | the source comment itself says these are **invented**; `catalogue/INDEX.md` §7.2 states base HP/ATK/DEF are published nowhere. Nearest recovered anchors: FAQ image 8 anonymous gear-removed tuple 2,866/1,522/1,103 and the 2019 archive row for `051` (Beckhen) | [ORIGDATA]/[COMM] adjacent | **UNSUPPORTED** |
| I5 | Card 002–006 stat rows | every non-001 reference copies card 001's row verbatim: `stat: ordinaryRankStats({ ...cardOneReference.stat[0] })` (`bootstrap.ts:201`; 002 variant at `:147` differs only in ATK/DEF) | none; no base stat is published for any of the 113 heroes except `051` | [ORIGDATA] one row | **UNSUPPORTED** — all six heroes also share one base row, so per-hero balance does not exist locally |
| I6 | Role / attribute assignment | 001 Bomber3/Fire1, 002 Offense1/Lightning3, 003 Ice2/Defense2, 004 Fire1/Support4, 005 Ice2/Defense2, 006 Fire1/Offense1 | numeric dispatch (roles 1 Offense/2 Defense/3 Bomber/4 Support; attrs 0 None/1 Fire/2 Ice/3 Lightning) is native text-dispatch-proven; the per-hunter assignment is catalogue/community metadata | [NATIVE] enums + [COMM] assignment | **CORROBORATED** (enums) / **UNSUPPORTED** (per-hunter rows) |
| I7 | Card roster size | 6 references published (001–006) | 113 heroes exist in `CHAR_STR_RO` and on disk; only 4 are in the original whitelist family | [ORIGDATA] | **UNSUPPORTED** |
| I8 | Gems | inventory and all five reference tables published as valid empty collections; every gem mutation refuses | 12 jewel set-bonus families, 10/12 numeric tokens recovered (FAQ image 10); Super Block KO 9 % vs other locales 5 %; FAQ refine budget ≥600k rupees | [COMM]/[ORIGDATA] | **UNSUPPORTED** — an empty table cannot contradict anything, but nothing is served either |
| I9 | Equipment / awakening / release | not implemented (no routes) | [COMM]: enhancement breakpoints 500→1,000→5,000→15,000→30,000→100,000 at Lv10/20/30/40/50; toolbox 130/10 per level at 40–49; remodel every 10 levels; awakening A1/A2/A3 = 30/50/100 crystals + 30k/100k/150k rupees; ★4+ equipment gate | [COMM] ×2 | **UNSUPPORTED** |

---

# 2. UNPUR[E] — reconciliation, adjudication, ledger

Everything here is inference, reconciliation or conflict reasoning. Each item
cites §1 rows plus the underlying sources.

## 2.1 Verdict tally

| Verdict | Rows | Where |
|---|---|---|
| CONTRADICTED | **4** | A1, A3, A4, E8 |
| UNCONTRADICTED | 3 | B11, D6, F8 |
| CORROBORATED | **29** | A2, A5, A6, A7, B4, B6, B12, B13, C5, C9, C11(ids), D1, D3, D5, D7, D10, D11, E1, E9, F1, F2, F3, F7, G3(shape), I1, I6(enums) |
| UNSUPPORTED | remainder (~78) | the entire economy, all shops, all supply, arena, all combat stats |

The shape of that tally **is** the finding: the replica's *protocol shapes* are
overwhelmingly corroborated and its *numbers* are overwhelmingly unrecovered.
Four rows are actively contradicted, and they cluster in exactly one system —
skill training — plus one trace threshold.

## 2.2 The three conflicts the parent flagged

### (i) Skill price: `100 × level` vs banded 100–1000 — **CONTRADICTED, soft**

`[EN-2017]`'s top band (L45–49 = 1000) is roughly **5× cheaper** than the local
equivalent level (L45 = 4500). The two agree **at L1 only**.

The important qualifier, and the reason this is *not* a simple "wrong formula"
finding: native evidence pins only the **indexing**, not the value.
`GetCardSkillUpPrice` returns `roleVector[destinationLevel-1]`, which requires a
**dense per-level vector** — and a dense vector whose `gold` is *constant inside
each 5-level band* satisfies both native indexing **and** the banded community
table simultaneously. So the contradiction is against the local **formula**
(`100 × level`, strictly linear and never repeating), **not** against the local
**row density**. Retuning to banded-constant values inside the existing dense
vector would be internally consistent; that is a statement about feasibility, not
a recommendation, and the retune decision belongs to the owner.

Residual risk: [EN-2017] is PRE-2019-09-05 and its band 10 (`45-49`) leaves level
50 uncovered, while [NAMU]'s `45-50` covers it. If the banded reading is right,
the local 50-row table's last row prices a level that may not have existed in
that form.

### (ii) Zero skill materials — **CONTRADICTED, and the cleanest conflict here**

This is the "least ambiguous discrepancy" the parent flagged, and the audit
agrees, for three separable reasons:

1. **Two independent sources agree on the same ladder**, cell for cell, in two
   languages on two sites (30/30 material cells identical), with a shared-ancestor
   explanation that makes agreement far more likely than convergent invention.
2. **The conflict is with the local *quantity*, not with a schema choice.** The
   native row schema *does* carry four `source_N_{ref_id,qty}` pairs, and the
   native popup provably skips the item lookup when a qty is 0 — so qty 0 is a
   *legal* value, and the fixture's zero is a deliberate economy statement, not a
   schema dodge.
3. **The requirement starts at level 5**, so rows 1–4 are unconstrained by both
   sources. The contradiction is confined to levels 5–50 of all four roles
   (184 rows). Level 25 is additionally contested *between the two sources*
   (4+1 vs 5+2) — so even a corrected table would have one genuinely unknown cell.

The `0/0/0` first band also means the local table contradicts only the *upper*
bands; a corrected table would need [NAMU]'s ladder, which supplies **no
fragments** count per band in its material row — the fragment column is a
separate row with the decadal 1/2/3/4/5 resolution. Any faithful retune must
decide which of the four `source_N` slots carries the fragment and which carries
the role material; **no evidence in hand fixes that assignment.**

### (iii) Skill caps 10/20/30/40/50 — **CORROBORATED (confidence raised, value unchanged)**

Confirmed and worth stating precisely: [NAMU] asserts "+10 per grade" directly;
[EN-2017]'s band-10 row implies a 50 ceiling at 5★; [HELP-1.4.4.1] `CONTENTS4_4`
independently describes the five-slot model; native `GetCardSkillMaxLevel` is
configurable and agrees in *shape* (max row level with `row.rank ≤ hunter rank`).
This raises confidence in an existing fixture and changes nothing.

## 2.3 The fourth contradiction the parent did not flag: trace thresholds

`local_sylvester_trace.collect_qty = 10` (rank 1) and
`local_gerard_trace.collect_qty = 20` (rank 2) are **exactly half** the [NAMU]
§1.3 fixed-recruit ladder **1★ 20 / 2★ 40** (stated formula 2^n×10). Both
published fixtures sit at the same exponent below NAMU's, which is the pattern of
one index convention rather than two independent guesses — note that it is
**equally** the pattern of NAMU's own exponent being one higher
(see the correction below).

**[CORRECTED 2026-10-05 — the factor-2 claim is NOT UPHELD as a demonstrated
error.]** The `10/20` vs `20/40` gap is an **exponent-convention (one-index)
offset against a single ERA-UNRESOLVED source that contradicts itself at ★1 and
★3**, not a demonstrated scaling error. NAMU §1.3's exact semantics are still
unpinned (it may be a generic "fixed-recruit" ladder rather than a per-hunter
recruit cost), and the only external anchors — two official 10-trace ★3 grants
and two official 40-trace ★3 maxima/grants — fit the **local** ladder. The
ladder **shape** (doubling per star) is corroborated uniquely; the **absolute
values** are not corroborated (rank 1 = 10 only partially; rank 2 = 20 has no
support and no contradiction). Recorded in the §2.6 register as **X3**. The
original **item-reference recovery is STILL OPEN** and nothing here retunes
10/20. Superseding evidence: `trace-threshold-2026-10-05.md` §2.6 verdict table
and §2.9 closing steps.

It matters beyond bookkeeping because `collect_qty` is reused as the
guided-Search reward quantity (E11), so one wrong constant propagates into two
systems.

## 2.4 The era problem — why most rows cannot be closed

- **PRE-2019-09-05** evidence: [EN-2017] skill/transcendence tables, Caragublu
  2018-12 rank-up previews (8,000 / 12,000), the 2018 Lv30 screenshots.
- **POST-2019-09-05** evidence: `blustone.jp` training (2019-12-11) and rank-up
  (2019-11-13) guides; the TapTap rebalance announcement (equipment +50 %,
  crystal mains +30 %/+50 %, substats +50 %).
- **ERA-UNRESOLVED**: the entire Namu wiki, including the trace ladder (E8) and
  the skill material grid (A3).
- **No era**: every local fixture.

Consequence: **A1 and A3 cannot be settled by the current evidence set at all.**
The one original-era change that is documented (2019-09-05) touches equipment and
crystals, and says nothing about skill-training gold or materials. A
pre-rebalance community table is therefore the best available bound and is not a
2.8.0.1 fact. The cheapest real resolution the transcendence audit identified — the
shipped 2.8.0.1 `UI_CSV.jet` `CONTENTS12_*` … `CONTENTS15_*` sections that do not
exist in the 1.4.4.1 corpus — has now been **swept, and came back empty**: zero
cost numerals across **all 95** shipped `CONTENTS` records, **20 patterns, 0
hits**, so the shipped help is a **second-version negative** stacked on the
1.4.4.1 one. That is why A1/A3 still cannot be settled: help sweeping is
exhausted as a route to them, and the remaining resolution is the original
reference rows. **[stale item closed 2026-10-05 per
`help-2_8-sweep-2026-10-05.md` §2.1 Q1, §2.8 C1/C2/C4 ("swept and empty"), §2.9]**

## 2.5 Scale-plausibility ledger (inference, not evidence)

These rows are **UNSUPPORTED**, but their magnitude is far from the only adjacent
recovered figure. They are listed separately because "no evidence" and "evidence
that says this is the wrong order of magnitude" are different research states.

| Fixture | Value | Nearest recovered adjacent figure | Ratio | Reading |
|---|---|---|---|---|
| Skill gold at L45–49 | 4,500–5,000 | [EN-2017] band 10 = 1,000 | ~5× | soft contradiction, see §2.2(i) |
| RankUp cost per source | 1,000 | Caragublu PRE previews 8,000 / 12,000 | 8–12× (unnormalisable) | implausible as an original scale; the preview's source count is unknown, so no per-source conversion is possible |
| Trace threshold 1★ | 10 | [NAMU] 1★ = 20 | 0.5× | factor-2 soft contradiction, §2.3 |
| Card 001 Lv1 HP | 1,000 | FAQ image 8 anonymous gear-removed 2,866; archive `051` row | ~3× at an unknown level/rank | the local base row is a placeholder by its own comment; no normalisation is legitimate. Note `bootstrap.ts:201` copies this same row into 002–006, so **all six heroes are one stat line** |
| Monster HP | 100 (all monsters, Lv1) | MON BLAST! Lv10 MAX 17,370–18,080 (**different app**) | ~170× | unusable: no entity/scale crosswalk; monsters remain 0/22 |
| Team EXP thresholds | 0 / 100 only ⇒ Team level ≤ 2 | archived team-rank ladders and every observed "Team Lv" reading in the pollution ledger are far higher | — | the two-row curve is a fixture that visibly truncates progression |
| Raise / level curve | 100·level everywhere | none | — | genuinely unconstrained; not implausible, simply unknown |

Two of these deserve emphasis. **The Team level curve** (`bootstrap.ts:350`,
`user: [{min_exp:0},{min_exp:100}]`) is a two-row threshold table, so the
replica's team level is hard-capped at 2 and every stage EXP is compressed into
one step; it is the least visible and most structurally limiting fixture in the
economy. And the **identical monster stat row across every published monster**
means monster difficulty is a constant, so per-area escalation does not exist in
the replica at all.

## 2.6 Conflict register

Extends the transcendence audit's C1–C9 where it overlaps.

| ID | Item | Local | Evidence | Status |
|---|---|---|---|---|
| **X1** | Skill materials zero at L5–50 | `source_N_qty: 0` (all rows) | both sources: role material required from L5 | **OPEN**, least ambiguous; needs the slot↔material assignment recovered |
| **X2** | Skill gold formula | `100 × level` | [EN-2017] banded 100…1000 | **OPEN**, soft; reconcilable with native dense indexing |
| **X3** | Trace thresholds | 10 / 20 | [NAMU] 20 / 40 | **OPEN (index ambiguity, not a demonstrated factor-2 error)**; shape CORROBORATED, absolute value UNRECOVERED. Per `trace-threshold-2026-10-05.md` §2.6/§2.9 **[2026-10-05]**: the gap is a one-index exponent offset against one self-inconsistent ERA-UNRESOLVED source, and the item-reference recovery that would close it is **still open**. No retune recommended |
| **X4** | RankUp 1,000 gold/source | 1,000 | only 8,000 / 12,000 previews (PRE, unnormalisable) | **OPEN**; implausible scale, no per-source anchor |
| **X5** | Skill level 25 materials | 0 | [EN-2017] 4+1 vs [NAMU] 5+2 (inherited C1) | **OPEN**, upstream of X1 |
| **X6** | Band-10 top level | 50 rows published | [EN-2017] `45-49` vs [NAMU] `45-50` (inherited C2) | **OPEN** |
| **X7** | `sell_price: 0` for all ranks | 0 | archive: 1–2★ sell for rupees, 3★+ secret-corner coins | inert gap; no sell route exists |
| **X8** | Abyss reset economy | empty | first-party help, up to 3 VIP-scaled resets/day — **[HELP-1.4.4.1]-ONLY** (`CONTENTS6_1`) | **HISTORICAL, not a current gap.** The clause was **removed, not restated**, by 2.8.0.1, which publishes daily-entry regulation + Manda-bought extra entries and **no reset count or Veteran cap anywhere**. So this is no longer an unimplemented *first-party-proven* mechanic for the shipped client, and no reset quantity is recoverable in **either** era **[corrected 2026-10-05 per `help-2_8-sweep-2026-10-05.md` §2.5(a) / §2.8 NEW-2]** |
| **X9** | Battle rank-up shortcut | refused below max level | [blustone.jp POST] ★1–★2 batch rank-up without max level | **GAP** (inherited rule 8) |
| **X10** | ★3 release → Chu-coin → trainer loop | no release/sell/market route | [blustone.jp POST] 8 coins → two ★3 trainers | **UNIMPLEMENTED** (inherited rule 9) |
| **X11** | Episode chapters E03–E17 | refused | 15 chapters of recovered original declarations | unimplemented against known values |
| **X12** | E01 coupon redemption | refused | native coupon path `Ge40020` exists; tier/odds unknown | unimplemented against a known path |
| **X13** | Capsule display name | "Helium Capsule" | FAQ Helium↔`AIRSHIP_TICKET` crosswalk UNPROVED | naming risk only |

## 2.7 What would close each contradicted row

| Row | Cheapest decisive next step |
|---|---|
| X1 / X2 / X5 / X6 | ~~sweep the shipped 2.8.0.1 `UI_CSV.jet` `CONTENTS12_*`–`CONTENTS15_*` records for cost numerals~~ — **DONE 2026-10-05, negative**: **95** shipped `CONTENTS` records, **20 patterns, 0 hits**, i.e. no help-cost numerals in either shipped version (`help-2_8-sweep-2026-10-05.md` §2.1 Q1, §2.8 C1/C2/C4 "swept and empty"). **All four verdicts stay exactly as they were (OPEN)** — the sweep closed the step, not the rows. The surviving step is unchanged: recover the network `GetLevel.skill` price/material rows the native getter indexes — the value question is a data question, not a formula question |
| X3 | **STILL OPEN** — recover a real `/reference/GetItem` row for a genuine trace id (`use_type 3`, `effect` = a hunter `base.id`) and read its `collect_qty`, **or** one native `ShardExchangeConfirm` panel capture (threshold stored at popup+`E4`), ideally for ★2 and ★3 to settle the index question. Local searches for the item row are already negative (`trace-threshold-2026-10-05.md` §1.8), so this needs an archived response/capture, not more grepping **[status re-scoped 2026-10-05, §2.9]** |
| X4 | recover `GetCardRankUpPrice` rows; the *mechanism* is already native-recovered (sum over new real sources, placeholders skipped) |
| X7 / X10 | recover a release/sell route + its currency (Chu-coins) |
| X8 | recover the Abyss `reset_price`/entry branches — **re-scoped 2026-10-05 per `help-2_8-sweep-2026-10-05.md` §2.5(a)/§2.8 NEW-2**: 2.8.0.1 help states an **entry** model (once daily, Veteran-scaled extra entries bought with Manda) and publishes **no reset branch at all**, so target the entry branches, not a VIP-reset branch |
| X11 / X12 | recover item reference rows for `GC*`/`FMD1`/`SK*`/`EM02`/`LCOIN`/`OV1`/`CERUM*` tiers |
| I2 / I4 / I5 | continue the base-stat hunt; note the archive's 62 hero rows still lack level/gear context, so they cannot be promoted into fixture rows yet |

## 2.8 Limits of this audit

- **No fixture was changed and none is recommended here.** Every row is a
  statement about evidence, not a retune instruction.
- **Most economy numerals are not recoverable from anything currently in hand.**
  78+ UNSUPPORTED rows are an honest state, not a backlog of known-wrong values.
- **Only two evidence classes can close rows**: native parsers and original
  shipped data. Community prose can raise or lower confidence (A5, B4, B12) but
  cannot by itself promote a fixture to "recovered" — the project's honesty rules
  still apply.
- **Two contradictions (X1, X3) rest on a single ERA-UNRESOLVED wiki or on
  PRE-rebalance prose.** They are flagged because the local values are *also*
  unsupported and demonstrably off by a clean factor, not because the community
  table is authoritative.
- **Cross-title evidence is excluded.** MON BLAST! figures were read and are
  recorded as unusable; they do not move monster coverage off 0/22.
- **Zero coverage effect.** Heroes 1/113, accessories 1/100, monsters 0/22.
- **`polluted-observations.md` was not appended this run**; the parent mirrors
  this file.
- No server, APK, seed, state file or emulator action was taken.