# Training / rank-up rules validation — 2026-10-05

**Lane:** validate BLUSTONE training/rank-up rules from archives against native
parsers and local server policy. **Read-only:** no server/APK/state changes.
**Coverage:** no change (heroes 1/113, accessories 1/100, monsters 0/22).
All numeric economy tokens are **impure rebalance context** — they never count
toward any 70% threshold.

**Sources consumed:**
- `wayback-announce-2026-10-05.md` §§1.2–1.3 (blustone.jp training + rank-up
  guides; POST-2019-09-05 captures).
- `namu-kr-blogs-2026-10-05.md` §§1.1–1.4, 2 (mirror tables; mostly
  ERA-UNKNOWN except where dated).
- Native research: `training-raise-followup.md`, `training-source-hunter-
  whitelist.md`, `skill-level-reference.md`, `skill-up-contract.md`,
  `skill-zero-level-eligibility.md`, `rank-up-partial-arithmetic.md`,
  `rank-up-implementation-audit.md`, `hunter-level-caps.md`,
  `training-public-evidence.md`.
- Local policy: `rewards-economy-2026-10-05.md` §§A/B.8.

**Era rule:** blustone.jp guide captures (2019-11-13, 2019-12-11) are
POST-rebalance. Namu mirror claims are ERA-UNKNOWN (page spans 2017–2021,
individual claims undated) unless the source itself dates them. The 2018-12
Caragublu screenshots are PRE-rebalance. Local fixture numbers carry no era.

---

## 1. Rule comparison: archive prose vs native parsers vs local server policy

| # | Rule | Archive prose | Native parser evidence | Local server policy | Verdict |
|---|---|---|---|---|---|
| 1 | Max 5 partners per training session | blustone.jp training guide (POST, 2019-12-11): 1回で最大5人 | Five-source limit in native selection (`G101de2e..3c` per AGENTS §60); `trainCard` boundary | Refuses >5 before any mutation; tests incl. 6-refuse/5-accept | **MATCH** — three-way agreement |
| 2 | ★1–★2 partners recommended as fodder | Same guide: ★1–★2 fodder recommendation | `SearchStuff` ctor `101f9bc` builds rank1 whitelist (006/007/011/014/016/017/018/019/020) + rank2 whitelist (005/013/015/021/024/025/030/032); predicate removes off-list IDs; min-rank filter uses minimum STAT rank, not recruit grade | Publishes 005 Gerard / 006 Sylvester as eligible sources; old 001–004 excluded | **DIRECTION MATCH** — whitelist mechanism recovered; "★1–★2" as such is guide advice, native key is whitelist+min-rank |
| 3 | Rank-up possible to ★5 for every hunter | blustone.jp rank-up guide (POST, 2019-11-13): ★5 ceiling; ★1-drawn hunters raise far | `GetCardRankUpSrcCnt` capacity table; terminal rank5 `src_cnt:0` is a local table policy, native terminal-UI path unproved | Ordinary ranks 1–4 with `src_cnt` 1/2/3/4; rank5 refused as terminal | **SUPPORTED** as policy; terminal-row native rendering still needs a control |
| 4 | Material count = current star count (★3→★4 needs three ★3 same-★ partners) | Rank-up guide example; Namu hunter page: "자신과 같은 등급의 캐릭터를 자신의 등급의 수만큼" | Capacity C from `GetCardRankUpSrcCnt(currentrank)` (`0x87f348`, scene+0x65c); `GetSrcCnt` returns n (new sources), NOT C; credited p synthetic entries `0..p-1` via `SetCardPromotion` | `src_cnt` 1/2/3/4 = current rank (community rule); `p+n<C` retains / `==C` promotes | **MATCH** as community-supported reconstruction; C values are not a captured original table |
| 5 | Level resets to 1 on rank-up | Rank-up guide | Preview path `SetPromotion(L)` resets level→1 + rank+1 in the cloned analyzer; server transition itself unproved (no captured partial/full response) | `p+n==C`: rank+1, counter→0, EXP→next-rank level-1 threshold | **MECHANISM PARTIAL** — preview reset is native; the persisted EXP-reset policy is `[INFERRED]`, honestly labeled |
| 6 | A new skill is learned on rank-up | Rank-up guide | `SetRank` changes max hunter/skill level but does NOT call `SetSkillLV`; `ReqRankUpCB` parses no skill levels; newly eligible zero slots init via real `SkillUp` prev0/cur1 | Preserves trained skills across promotion; no invented unlock fields | **PARTIAL** — slot-eligibility metadata (`target_rank`) remains a fixture convention; fifth-slot rank5 gate has FAQ corroboration only |
| 7 | ★4+ unlocks equipment | Rank-up guide | No direct native proof in this lane; adjacent: VSFan `CONTENTS11_7` mounts jewels onto equipment; 4★ jewel gate follows from the equipment gate (inference, not proof) | No equipment system implemented | **UNPROVED native** — archive-only rule; do not present as recovered |
| 8 | Batch rank-up for ★1–★2 without max level | Rank-up guide | Ordinary `RequestRankUp` path checks max level server-side (local); no native batch-rank path audited (`RequestMultiSkillUp` is the skill route, not rank) | Underlevel targets refused | **GAP** — guide claims an onboarding shortcut the replica does not implement; needs native batch-rank parser work before any implementation |
| 9 | Releasing ★3 → 8 Chu-coins → two ★3 trainers (Secret Market); feed ranked-up ★3s, not naturals | Rank-up guide economy (POST) | No Chu-coin currency, release/sell path, or Secret Market route in native evidence reviewed | `sell_price` rows exist as fixtures (0); no release/sell handler | **UNIMPLEMENTED** — pure archive economy lead; Namu corroborates direction (1–2★ sell for rupees, 3★+ give secret-corner currency; Lily&Lala 12 coins→5 traces) |
| 10 | Character max level 30 regardless of grade | Namu hunter fn36 (ERA-UNKNOWN); Caragublu Dec-2018 Natalia 3★ Lv30MAX + 3★MAX→4★Lv1 screenshots (PRE) | `GetCardMaxLevel` returns last-row level (configurable, not a fixed 30); `GetCardLevel` walks `min_exp` thresholds | Dense 30-row curves per rank 1–5, preserving rank1 0/100 so owned Lv2 survives | **SUPPORTED** as provenance-labeled fixture; not a captured server row |
| 11 | Skill max +10 per hunter grade (caps 10/20/30/40/50) | Namu skill-training bands 1–4, 5–9, …45–50 (ERA-UNKNOWN) | `GetCardSkillMaxLevel` = max row.level with row.rank ≤ hunter rank (configurable); price getter indexes `roleVector[destinationLevel-1]`; zero-material price guards proved | Dense per-role rows; caps 10/20/30/40/50 as community inference | **SUPPORTED** as inference; per-rank cutoffs and all prices/materials are fixtures |
| 12 | Skill-up price = f(destination level) | — (no archive price) | `GetCardSkillUpPrice(role, level)` returns `vector[level-1]`; destination = owned+1 (`skill-zero-level-eligibility.md`); batch sums intermediate destinations | `100 × destinationLevel` gold, zero materials | **MECHANISM RECOVERED**, amounts fixture |
| 13 | Rank-up cost charged once per new source; credited p not recharged | — (no archive price) | `UpdateRankupInfo` sums discounted `GetCardRankUpPrice(source.rank)` over new real sources only; placeholders (serial<C) skipped; guild sale-benefit type3 hook exists, unmodeled | `1000 × n` gold; credited p free | **MECHANISM RECOVERED**, amounts fixture |
| 14 | Stat growth per credited material is linear | — | `CSRCard::Validate`: `promotion_factor = 1 + (stat_bonus/100) × rank_up_cnt` (three primary stats) | `stat_bonus:5` fixture → p1 = ×1.05, p2 = ×1.10 | **FORMULA RECOVERED**, coefficient fixture |
| 15 | Raise: each source contributes its own XP; cost per source | — (no numbers on the training guide page) | `UpdateTraningInfo` derives each source's awake/rank/exp; `GetCardRaiseExp` uses source rank+level `upgrade_exp`; card curve rows are rank/level/min_exp/upgrade_exp/sell_price | 100 gold/source; source XP 100×level; cumulative target XP 100×(level−1) | **MECHANISM RECOVERED**, curve and costs fixture |

**Net assessment:** the archives confirm the replica's structural choices
(5-partner cap, count-equals-rank materials, Lv30 cap, 10/grade skill caps,
whitelist-direction fodder) but contribute **zero** original price/XP/curve
numbers. Every gold/XP/bonus figure in the local training system is a labeled
fixture. The two genuine functional gaps the archives expose are batch
★1–★2 rank-up without max level (rule 8) and the ★3 release → Chu-coin →
trainer loop (rule 9) — both need native parser work first, not fixture
invention.

---

## 2. UNPURE — numeric economy tokens (impure rebalance context, NO coverage credit)

Every token below is supplementary rebalancing/economy context only. None
counts toward the 70% hero/jewelry/monster thresholds. Era tags follow the
2019-09-05 rebalance threshold.

### 2a. Training / rank-up core (blustone.jp guides, POST era)

| Token | Value | Source | Era | Status |
|---|---|---|---|---|
| Max partners per training session | 5 | [トレーニング 2019-12-11](https://web.archive.org/web/20191211104454/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0) | POST | Rule context; matches native 5-cap |
| Fodder recommendation | ★1–★2 | Same | POST | Qualitative advice, not a price |
| Max hunter rank | ★5 (all hunters; ★1-born raise far) | [ランクアップ 2019-11-13](https://web.archive.org/web/20191113131941/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97) | POST | Rule context |
| Material count rule | N same-★ partners for ★N (★3→★4 = three ★3s) | Same | POST | Matches community C=rank rule |
| Level on rank-up | resets to 1 | Same | POST | Policy context |
| Equipment unlock | ★4+ | Same | POST | Unproved native; new lead |
| Batch rank-up | ★1–★2 without max level | Same | POST | Unimplemented gap |
| ★3 release yield | 8 Chu-coins (チュウコイン) | Same | POST | New numeric lead, unproved server-side |
| Trainer purchase | two ★3 trainers per 8 coins (→ 4 coins/trainer) at Secret Market | Same | POST | New numeric lead; no market route |
| Rank-up feeding advice | ranked-up ★3s cheaper than natural ★3s | Same | POST | Qualitative economy advice |

### 2b. Namu hunter/text lane (ERA-UNKNOWN unless dated)

| Token | Value | Source | Era | Status |
|---|---|---|---|---|
| Grade titles | 1★ Novice / 2★ Lower / 3★ Intermediate / 4★ Advanced / 5★ Master; natural-born max 4★ | [Namu hunter mirror](https://d.namu.moe/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0) §1.1 | UNKNOWN | Cross-checks GameAppCH/Mugen generic rank labels |
| Character cap | Lv30 regardless of grade | Same, fn36 | UNKNOWN (visual anchor PRE 2018-12) | Fixture basis, not wire proof |
| Fixed-recruit traces | 1★ 20 / 2★ 40 / 3★ 80 / 4★ 160 (formula 2^n×10) | Same §1.3 | UNKNOWN | Economy context |
| Self-overcoming (3★+) metron crystal/fragment per step | 1★ 5/50, 15/150, 45/450; 2★ 7/70, 25/250; 3★ 9/90, 30/300, 80/800; 4★ 12/120, 40/400, 110/1100 (fragment = 10× crystal) | Same §1.3 | UNKNOWN | Economy context |
| Skill-training materials | metron fragments + role mats (metal shards/shells/fire stones/herbs, rusty→sharp→strange); role mat from Lv5, +1 per 5 levels; skill max +10/grade | Same §1.3 | UNKNOWN | Bands corroborate 10/grade inference; item IDs not mapped |
| Equipment enhancement (added 6/22, year unstated; 4★+ unlock) | rupee breakpoints 500→1000→5000→15000→30000→100000 at Lv10/20/30/40/50; toolbox 130/10 per level at 40–49; remodel every 10 levels; guild discount single-digit % except remodel | Same §1.3 (full grid at mirror lines ~280–420) | UNKNOWN | Cost table, not transcribed cell-by-cell here |
| Sell rule | 1–2★ sell for rupees; 3★+ give secret-corner (첨쥐) coins; Lily&Lala traces 12 coins → 5 | Same §1.3 | UNKNOWN | Direction corroboration for Chu-coin loop |
| Gacha price | 30 single / 300 bundle (10+1, 11 total); occasional consecutive-pull discount | Same §1.4 | UNKNOWN text (native 30/300 RECOVERED separately) | Text corroboration only |
| Stim-pack (스팀팩, ex-신기한 물약) | + button charges 3000 (literal "3000천" preserved; likely 3000) | Same §1.2 | 2019-04 change = PRE | Price context |
| Rage costs | attackers/defenders 3, bombers/helpers 4; Lily&Lala + Bear (036) cost 4 despite role | Same §1.2 | UNKNOWN | Cost context |
| Lantern (001) crit skill 4 | 10,000+ single hit at 5★ + DEF-down | Same §1.2 | UNKNOWN | Skill-magnitude context |
| Gullveig / Hermes / Karl attack speed | Gullveig +7.5% ally AS; Hermes +15% → 22.5% stacked; +Karl skill → 37.5%; Karl base AS 7 w/o skill (attacker exception vs 8.00 hypothesis) | Same §1.2 | UNKNOWN | Magnitude context |
| Bond bonuses | Haisen 4★ 8% / 5★ 16%; Chirrchirr (Alice) 4★ 10% | Same §1.2 | UNKNOWN | Magnitude context |
| Beckhen (051) Fight Club bonus | +10% ATK/DEF/HP in Fight Club only; traces via Fight Chip shop (375 chips / 5 traces, restock 6h) | Same §1.2 | UNKNOWN | Bonus/shop context |

### 2c. Screenshot-anchored rank-up prices (PRE era, NOT promotion proof)

| Token | Value | Source | Era | Status |
|---|---|---|---|---|
| Rank-up preview prices | 8000 / 12000 (both destination badges four-star; faded two-source preview is NOT partial-promotion proof) | [Caragublu Dec-2018 guide](https://www.caragublu.com/2018/12/blustone-game-guide.html) advance screenshot; see `rank-up-partial-arithmetic.md` retraction | PRE (2018-12) | Historical price points; must NOT become universal 2.8.0.1 balance |
| Rank-up value pair | 7,092 → 11,277 (generic Middle→Advanced Hunter, LvMAX→Lv1, new additional-damage skill) | [FreeGame Mugen 2017-09-13](https://freegame-mugen.jp/spapp/game_6433.html) rank-up image | PRE (2017) | Field likely Power-rating; polluted progression only |
| Rank-up value pair | 1,417 → 2,389 + Block Chance Up (generic Amateur→Novice) | [GameAppCH review](https://gameappch.com/app/?app=04374) image 16 | PRE (2017) | Polluted progression only |

### 2d. Local fixture numbers (NO era — explicitly not original)

| Token | Value | Source | Status |
|---|---|---|---|
| Raise cost / XP | 100 gold/source; source XP 100×level; cumulative 100×(level−1) | `openapi.ts:367`, `gym-legitimate-donor-budget.md` | FIXTURE preserving old thresholds |
| Skill-up cost | 100×destinationLevel gold; zero materials | `skill-training.ts:20` | FIXTURE |
| Rank-up cost / bonus | 1000 gold/source; +5% stat bonus per credited material | `openapi.ts:326` | FIXTURE |
| Rank-up preview prices on live account | 500 gold preview for five LV1 partners (target5 LV2→LV7) | AGENTS §60 | Fixture receipt, not original |

---

## 3. Files written

- This file (new): `training-rankup-rules-2026-10-05.md`.
- `polluted-observations.md`: appended §"Training/rank-up impure economy
  tokens (2026-10-05)" summarizing §2a–2d with source URLs + era tags.
- No coverage-count change; no server/APK change.
