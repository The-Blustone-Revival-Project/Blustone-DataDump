# Replica combat SHAPE error — code paths, the shipped `bonus.*` table, and shape-correcting options (2026-10-05)

> ## HEADLINE ADDITION 2026-10-05 — the `s = (ATK+DEF)/HP` axis, and a 5.61x error that is worse than the ATK/DEF error
>
> This document's headline ratio error (§1.5.c) is stated on `ATK/DEF`:
> replica `2.000` sits **1.14x above** the recovered maximum `1.7483`. **That is
> the smaller of the two errors.** The companion axis
> `s = (ATK+DEF)/HP` — the combined offence+defence budget per point of HP, and
> the quantity that actually governs time-to-kill — is not stated anywhere below,
> and it is worse by a factor of nearly four:
>
> | | replica | archive range (62 rows) | position |
> |---|---|---|---|
> | `r = ATK/DEF` | **2.000** (`001`) / 3.000 (`002`) | `[0.6589 … 1.7483]` | **1.14x above the maximum** |
> | `s = (ATK+DEF)/HP` | **0.150** (`001`) / 0.160 (`002`) | `[0.8419 … 1.2171]` | **5.61x below the minimum** |
>
> Arithmetic: `s(001) = (100+50)/1000 = 0.150`; archive minimum is `036` Bear at
> `(755+864)/1923 = 1.619/1.923 = 0.8419`; `0.8419 / 0.150 = 5.61`. For card `002`,
> `(120+40)/1000 = 0.160`, and `0.8419/0.160 = 5.26`. It is also invariant to the
> `+hp_up 10` additive (R1): `(101+51)/1010 = 0.1505`, still 5.60x low.
>
> **Reading.** The replica is not merely mis-split between ATK and DEF — it is
> **HP-dominant by ~5.6x on the offence+defence budget**, while *simultaneously*
> being ATK-over-DEF-heavy in the one axis that is role-structured. Both errors
> must be fixed by the same per-row replacement, and any option that fixes only
> `r` (O4/O5 as previously framed) leaves the larger error untouched.
> Source and full derivation: `candidate-hero-bases-2026-10-05.md` §2.2 and
> `archetype-reconciliation-2026-10-05.md`.
>
> ### Companion correction, same date — three over-reads in this file are struck in place
>
> 1. **§1.5.b `:271` "4 clean groups" is WITHDRAWN.** Measured, `ATK/DEF` gives
>    **three** groups — Defense `[0.6589, 0.9167]`, Support `[0.9231, 1.1405]`,
>    Offense ∪ Bomber `[1.1695, 1.7483]` — because **Offense and Bomber overlap
>    across `1.3815–1.5815`** (8/12 Bomber and 9/20 Offense rows inside the
>    other's band; 17/62 rows unassignable on `r` alone). The n = 17/20/12/13 role
>    counts are unaffected.
> 2. **§1.5.b `:294`'s EVCB Offense range `1.077–22.500` is CONTAMINATED.** The
>    `EVCB*` prefix filter admits rows whose `res_id` is a **monster** id:
>    `EVCB0301_M057` (`res_id M057`, 4000/4500/200, r **22.500**),
>    `EVCB0301_M044`, `EVCB0102_M1`, `EVCB0102_M2`. That is why §1.5.b's `n = 41`
>    exceeds the 37 hero rows. Restricting to `ref_id` = 3-digit catalog
>    id **and** `res_id` starting `C` gives Offense **n = 11, range `1.077–1.333`**.
>    The Offense median is unchanged (`1.263`); only the maximum was wrong.
> 3. **§2.5 O5 `:560`'s band list is corrected in place** — it named
>    "Offense ≈ 1.17–1.58, Bomber ≈ 1.38–1.75" without noting that those two
>    ranges intersect.

**Purpose.** Locate, in `server-ts/src`, the *exact* code paths that produce the
replica's hero and monster HP/ATK/DEF, transcribe the shipped `LEVELING.jet` chunk-9
`bonus.*` multiplier table verbatim, and set out a prioritised list of shape-correcting
options with their evidence, assumptions and uncertainty.

**Nothing was changed.** No server file, fixture, seed, state file, APK or emulator was
touched, and **no change is proposed as an instruction** — §2 is an options list for the
repository owner. This is a statement about shape, not a retune.

**Not done deliberately:** `polluted-observations.md` was **not** appended (the parent
mirrors this lane).

**Coverage effect: none.** Heroes **1/113**, accessories **1/100**, monsters **0/22**
are unchanged. Not one number in this file is credited as a base tuple.

---

# 1. PURE — what the code and the shipped data actually say

Everything in §1 is reproducible from the cited files. Derived arithmetic is marked as
such and the derivation is given so it can be re-run.

## 1.1 The complete set of code paths that produce HP/ATK/DEF

An exhaustive search of `server-ts/src` for stat-literal sites returns **exactly three**
(`grep -E 'hp: *"|atk: *"|def: *"'` → `bootstrap.ts:90`, `:147`, `:1315/:1316/:1317`).
Two of them are hero rows; the third is the monster row. The three `0`-valued sites
(`arena.ts:86`, `bootstrap.ts:343`) and `bootstrap.ts:251` are **not** stats and are
listed separately below so they are not miscounted.

### 1.1.a Hero rows — there are only TWO in the entire server

| # | file:line | what it produces |
|---|---|---|
| H1 | `server-ts/src/bootstrap.ts:57-59` | `ordinaryRankStats(base)` → `[1,2,3,4,5].map(rank => ({ ...base, rank }))`. **A rank label stamp.** The same `base` object is spread into all five rows; only `rank` differs. Its own doc comment (`:55-56`) says *"Original stats are missing. Keep rank1 values unchanged; higher ranks reuse these local bases and let native rank arithmetic apply its scaling."* |
| H2 | `server-ts/src/bootstrap.ts:90-93` | card `001` (`FIXTURE_CARD_ID`, declared `:45`) base stat row: `hp "1000"`, `atk "100"`, `def "50"`, `spd "100"`, `crt_chance "5"`, `crt_dmg "150"`, `penetration "0"`, `block_chance "0"`, `block_dec_dmg "0"`, `attr_enhance "0"`, `attr_resist "0"`, `hp_regen "0"`, `hp_up "10"`, `atk_up "1"`, `def_up "1"`; wrapped by H1. |
| H3 | `server-ts/src/bootstrap.ts:147-150` | card `002` (`gachaCardStat`): `hp "1000"`, `atk "120"`, `def "40"`, `spd "110"`, then **byte-identical tail** to H2. Wrapped by H1. The doc comment at `:110-114` states the values are *"**invented**, not recovered"* and that they *"follow the `LEVELING.jet` §5.1 guidance the catalogue recommends — an Offense takes no HP penalty (`offense 1.0`)"*. **That intent is not implemented**: `bonus.offense` is 1.0/1.0/1.0 and card `001` (Bomber, `bonus.bomber` 0.85) receives the same `hp 1000`. |
| H4 | **`server-ts/src/bootstrap.ts:195-203`, line `:201`** | **the defect itself.** `additionalReferences` (`:187-194`, heroes `003`/`004`/`005`/`006` with identity + native `attr`/`role` + `minRank`) is mapped with `stat: ordinaryRankStats({ ...cardOneReference.stat[0] })` — i.e. **every one of `003`, `004`, `005`, `006` copies card `001`'s rank-1 row verbatim**, then `:202` filters rows by `row.rank >= card.minRank`. |
| H5 | `server-ts/src/bootstrap.ts:205-207` | `starterReference` assembles `cardOneReference` + `gachaCardReference` + `additionalReferences`, de-duplicated by `base.id`. |

### 1.1.b The wire

| # | file:line | route |
|---|---|---|
| W1 | `server-ts/src/game-routes.ts:327-333` | `/reference/GetCard` returns `starterReference` **verbatim** (a bare array — the native `SetCard` indexes `ret_data` itself). |
| W2 | `server-ts/src/game-routes.ts:359` | `/reference/GetLevel` returns `starterLevels` (`bootstrap.ts:349-355`). |
| W3 | `server-ts/src/game-routes.ts:391-423` | `/reference/GetMonster` returns `starterMonsterTable`. |

### 1.1.c Monster row — ONE row for every published monster

| # | file:line | what it produces |
|---|---|---|
| M1 | `server-ts/src/bootstrap.ts:1292-1330` (`starterMonsterFor`) | `attr 1` (`:1306`), `role 1` (`:1307`), `rank 1` (`:1311`), `level 1` (`:1312`), **`hp "100"` (`:1315`), `atk "10"` (`:1316`), `def "5"` (`:1317`)**, `crt_chance "0"`, `crt_dmg "100"`, `penetration/block_chance/block_dec_dmg/attr_enhance/attr_resist "0"`, **`hp_page "100"` (`:1325`)**. |
| M2 | `server-ts/src/bootstrap.ts:1038-1064` (`stageRecord`) | every stage publishes `enemy_atk_per 100` / `enemy_hp_per 100` (`:1049-1050` — 100 % / neutral, **CORROBORATED** by `analysis/research/stage-multipliers.md`), plus `ap_cost 1`, `gold 10`, `character_exp 10`, `group_exp 10`. **No per-stage enemy scaling exists locally.** |

### 1.1.d Progression rows that do **NOT** touch stats

| # | file:line | why it is listed |
|---|---|---|
| N1 | `server-ts/src/hunter-levels.ts:6-10` | 30 rows × 5 ranks of `min_exp` / `upgrade_exp` / `sell_price` only. **Level changes nothing about HP/ATK/DEF** — see §1.4. |
| N2 | `server-ts/src/training.ts:5`, `:9-11`, `:35-45` | `trainingPrices`; `rankUpRows` with `stat_bonus: 5` (a **preview-only** `promotion_factor`, native `CSRCard::Validate`); `trainingCurve` reads XP only. |
| N3 | `server-ts/src/bootstrap.ts:341-345` | `starterBookReference` — every card-book `effect` is `{atk:0,def:0,hp:0,crt_chance:0,crt_dmg:0}`. Collection bonuses are **all zero**. |
| N4 | `server-ts/src/arena.ts:82-92` | `arenaRival`: `card_book` all zeros (`:86`); the deck reuses **already-published** references (`ref` chosen `:83`, instance `:91`) — so the Fight Club opponent inherits hero row H2/H3 too. |

### 1.1.e Sites that are **not** stats (recorded so they are not miscounted)

- `server-ts/src/bootstrap.ts:251` — `mirage_remain_hp: 1000` on a card **instance**. This is the Mirage HP-lock field (`CSRCard::parse` reads it), not a battle stat.
- `server-ts/src/bootstrap.ts:343` / `arena.ts:86` — card-book collection-effect zeros (N3, N4).
- `server-ts/src/search-helpers.ts` — **contains no `hp`/`atk`/`def`/`stat` token at all**; the Search helper is published by `card_ref_id`, so it inherits H2.

### 1.1.f A fact that changes the risk profile of every option

`grep -E '\bhp\b' server-ts/src/state.ts server-ts/src/game.ts` → **no matches**. The
replica stores **no derived stat anywhere in persistent state**; every HP/ATK/DEF value is
built fresh from `bootstrap.ts` at boot and served from `/reference/GetCard` /
`/reference/GetMonster`. Card **instances** (`bootstrap.ts:248-258`) carry only
`rank`, `exp`, `lock`, gear levels and skill levels.

⇒ **Any correction confined to the reference rows in `bootstrap.ts` is a pure
reference-table change: zero state migration, zero migration risk, no owned-instance,
deck, card-book, wallet or progression field is touched.**

### 1.1.g Test surface

`grep -E 'starterReference|\.stat|ordinaryRank'` over `server-ts/tests/` shows the tests
assert `stat.map(row => row.rank)` — the **rank list**, not values (`tests/roster.ts:28`,
`tests/hunter-traces.ts:22`). Exactly **one** test pins a stat *value*:
`tests/smoke.ts:325` asserts `monsters.M001.hp === "100"`. **No test pins any hero stat
value.** So a hero-row correction is test-invisible; a monster-row correction touches
one assertion.

## 1.2 The shipped `bonus.*` table, transcribed verbatim

Source: `analysis/in-game-stats/leveling-chunk09.json` (4 022 bytes), which
`hero-stat-divergence-2026-10-05.md` §S4 pins as SHA-identical to
`analysis/recovered-data/campaign-stages.raw-LEVELING-chunk9.txt` (`C9F9C1BB…`), extracted
from the shipped 2.8.0.1 APK ⇒ **POST** the 2019-09-05 rebalance.

```json
"bonus": {
  "none":       { "hp": 1.0, "atk": 1.0, "def": 1.0 },
  "offense":    { "hp": 1.0, "atk": 1.0, "def": 1.0 },
  "deffense":   { "hp": 1.0, "atk": 1.0, "def": 1.0 },
  "bomber":     { "hp": 0.85, "atk": 0.95, "def": 0.95 },
  "support":    { "hp": 0.8,  "atk": 0.95, "def": 1.0 },
  "atk_camp":   { "hp": 2.0, "atk": 2.6, "def": 1.0, "ct_chance": 1.0, "ct_dmg": 1.0 },
  "def_camp":   { "hp": 2.0, "atk": 2.6, "def": 1.0, "ct_chance": 1.0, "ct_dmg": 1.0 },
  "rank_1":     { "hp": 2.6, "atk": 1.4, "def": 1.4, "ct_chance": 1.0, "ct_dmg": 1.0 },
  "rank_2":     { "hp": 2.2, "atk": 1.3, "def": 1.3, "ct_chance": 1.0, "ct_dmg": 1.0 },
  "rank_3":     { "hp": 1.8, "atk": 1.2, "def": 1.2, "ct_chance": 1.0, "ct_dmg": 1.0 },
  "rank_4":     { "hp": 1.4, "atk": 1.1, "def": 1.1, "ct_chance": 1.0, "ct_dmg": 1.0 },
  "rank_5":     { "hp": 1.0, "atk": 1.0, "def": 1.0, "ct_chance": 1.0, "ct_dmg": 1.0 },
  "stage": {
    "b_00_01": { "value": { "hp": 1.1, "atk": 1.1, "def": 1.1, "ct_chance": 1.0, "ct_dmg": 1.0 },
                 "cards": [ "051" ] }
  },
  "stage_buff": {}
}
```

Two transcription points that correct the earlier table in
`hero-stat-divergence-2026-10-05.md` §S4:

1. **`ct_chance` and `ct_dmg` are present on `atk_camp`, `def_camp` and all five `rank_*`
   rows** (with the shipped `crt_`→`ct_` typo) and were omitted from that table. They are
   1.0 everywhere, so they are inert as multipliers — but they are real schema.
2. **`atk_camp` and `def_camp` are byte-identical to each other.** A PvP side-wide table
   in which both sides carry the same `2.0 / 2.6 / 1.0` would make one of them inert for
   whichever side it was not meant to modify. That is an oddity in the shipped data, not a
   replica decision, and is recorded rather than interpreted.

### 1.2.a The other shape-relevant keys in the same chunk

These were not in the earlier table and bear directly on the shape question:

```json
"elem_bonus": 20,  "elem_def_bonus": 10,
"actor":  { "def_backend_bb": "165, 180", "atk_range_scl": "1.9" },
"left":   { "first_sp": 1.5,  "wave_spawn": "screen/2, 550", ... },
"right":  { "first_sp": 1.45, "wave_spawn": "screen/2+163, 550", ... },
"waiting":{ "idle_time": 4.0, "walk_spd": 140, "run_spd": 50, "fall_spd": 1000,
            "spawn_y": 100, "emergency_by_remain_time": 0.23 },
"sp_increase_per_kill": ..., "sp_increase_per_atk": ..., "sp_increase_per_dmg": ..., "sp_max": ...
```

- `elem_bonus 20` / `elem_def_bonus 10` are **scalars, not objects** — the elemental
  *bonus magnitude*. This cross-links to the Episode monster rows, whose only
  non-zero `attr_enhance`/`attr_resist` pair is exactly **20 / 10**
  (`hero-stat-divergence-2026-10-05.md` §S6). It is **not** the same quantity as a hero's
  own `attr_enhance`/`attr_resist` stat (see §1.5c).
- This chunk is otherwise **battle/AI/SP/fever tuning** (`AGENTS.md` §16.6 item 8), which is
  consistent with `INDEX.md` §5.2 classifying `rank_1..5` as the **monster**-rank
  multiplier.

## 1.3 The exhaustive negative: `bonus.*` is inert in the replica

`grep -E 'bonus|elem_bonus|elem_def' server-ts/src` returns 20 hits, of which the only
values are: `stat_bonus` (the RankUp field name, `training.ts:10`, `game-routes.ts:350`),
`chain_bonus: []` (arena), `iap_bonus: []` (empty), `login_bonus` (the 28-day login-reward
system, a different thing entirely), and two prose comments.

**Not one** of `bonus.none`, `bonus.offense`, `bonus.deffense`, `bonus.bomber`,
`bonus.support`, `bonus.atk_camp`, `bonus.def_camp`, `bonus.rank_1..5`, `bonus.stage`,
`bonus.stage_buff`, `elem_bonus`, `elem_def_bonus` is read anywhere in `server-ts/src`.
Confirmed.

Nor is chunk 9 loaded at runtime. The only runtime file reads in `server-ts/src` are
`analysis/recovered-reference/*.json` (`episode-progress.ts:23`) and
`analysis/native-all-strings.tsv` (`catalog.ts:40-42`).

## 1.4 [RECOVERED] native semantics that constrain every option

These are the hard constraints, and they are *recovered*, not inferred:

| # | fact | source | consequence |
|---|---|---|---|
| R1 | **`player_total_hp_max` = `hp + hp_up`, additive, no multiplier** — card `1000 + 10 = 1010.0`, confirmed on **three** independent captures | `analysis/research/in-game-stats.md:298-300, :420, :444`; matches `analysis/testing/report-017.md:110` (`player_total_hp_max: 1010.0`) | `hp_up`/`atk_up`/`def_up` are **flat additions**, not per-level increments. **The level curve changes no stat at all.** |
| R2 | **`enemy_total_hp_max` = `/reference/GetMonster` `hp` verbatim** — *"There is no level scaling, no rank multiplier, no party multiplication and no ×10 on monster HP. `AddMonster`'s `hp` is the whole story. **[recovered, 2/2 with a 2.5× change]**"* | `in-game-stats.md:249-260` (published 250 → bar read 250 → `enemy_total_hp_max 250.0`); matches every receipt (`enemy_total_hp_max 100.0`) | The published monster row is the entire HP budget of a battle. |
| R3 | **The shipped `bonus.*` multipliers are NOT applied by the client on the monster path.** Monster `M001` is `rank 1, role 1`; published `hp 250` displayed as **250**, where `bonus.rank_1.hp 2.6` would have given 260 | `in-game-stats.md:262-273` | Any `bonus.*` application must be **server-side** to have any effect. And note the probe is a *negative* on client-side application, **not** a positive on server-side application — nothing shows the original server applied them either. |
| R4 | **Damage to the player scales with the monster's `atk`** — monster `atk 10 → 44` (4.4×) moved the player HP drain `1.9 → 6.2 HP/s` (3.3×) | `in-game-stats.md:318-322` | `atk` is live damage input, not decoration. |
| R5 | **`atk_total` is a live damage total** and, at the fixture's ATK, **every recorded win is a single tap**: `atk_cnt 1` with `atk_total` 181 / 202 / 272 / 303 / 352 against `enemy_total_hp_max 100.0` | `analysis/testing/report-017.md:104-110`; `revival-004/stage2-and-autoadvance-wire.txt:4`; `revival-005/stage3-wire.txt:4`; `revival-006/stage4-timed-wire.txt:3`; `revival-008/stage6-7-transitions.txt:4,8`; `revival-010/source-campaign-wire.txt:6,10`; `episode-009/glacier-earned/dispatch-interruption-audit.md:9` | At `atk 100`, one ordinary tap deals ~181 against 100 monster HP ⇒ **TTK is one attack**. |
| R6 | **`enemy_total_hp_max` sums over waves.** The Search battle reported `enemy_total_hp_max 200.0` for `local_search_017`, whose two waves are two `M001` monster links at `hp 100` | `AGENTS.md` §74; `server-ts/src/search-stage.ts:3` | Wave count is an HP multiplier. [INFERRED-strong] from R2 + the wave construction. |

**R2 + R5 together are the single most important constraint in this document:** any
correction that raises hero ATK **must** raise monster HP in the same change, or every
battle stays a one-tap kill and the shape correction buys nothing observable.

## 1.5 Ratio arithmetic — the replica against every recovered source

Ratios are used throughout because they are the only scale-free statement available:
no recovered source prints a level, so an absolute comparison is not available, but a
ratio *within one row* is.

### 1.5.a The replica's own ratios

| row | HP | ATK | DEF | ATK/HP | DEF/HP | ATK/DEF |
|---|---:|---:|---:|---:|---:|---:|
| card `001` Bomber3 (H2) | 1000 | 100 | 50 | **0.100** | **0.050** | **2.000** |
| card `002` Offense1 (H3) | 1000 | 120 | 40 | 0.120 | 0.040 | **3.000** |
| cards `003`–`006` (H4 copy of `001`) | 1000 | 100 | 50 | 0.100 | 0.050 | 2.000 |
| every monster (M1) | 100 | 10 | 5 | 0.100 | 0.050 | 2.000 |
| card `001` after native additive `hp_up 10` (R1) | 1010 | 101 | 51 | 0.100 | 0.050 | 1.980 |

The hero row, its four copies, and the monster row are **the same three ratios**. There is
one shape in the whole replica.

### 1.5.b Two independent recovered sources, measured this pass

**S1 — archived Japanese hunter database, 62 numeric rows**
(`analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv`, Wayback
captures 2019-10-15 / 2019-11-13 / 2019-12-16, i.e. POST-rebalance). Derived this pass:

| | min | median | max |
|---|---:|---:|---:|
| HP | 1277 | 1651 | 2033 |
| ATK | 576 | 839 | 1058 |
| DEF | 540 | 722 | 1284 |
| **ATK/HP** | **0.3714** | **0.6654** | **0.7392** |
| **DEF/HP** | **0.3513** | **0.4652** | **0.7337** |
| **ATK/DEF** | **0.6589** | **1.4317** | **1.7483** |

Per role (groups identified by their ratio signature; the `role_ja` column is mojibake
but stable, ~~4 clean groups of n = 17/20/12/13~~ **"clean" WITHDRAWN 2026-10-05 —
these are 4 role *labels*, not 4 disjoint `r` groups; Offense ∪ Bomber share
`1.3815–1.5815` (see the header correction). The n = 17/20/12/13 role counts are
correct**). These reproduce the role bands already
published in `hero-stat-divergence-2026-10-05.md` §S1 independently:

| role | n | HP med | ATK/HP med | DEF/HP med | ATK/DEF med (range) |
|---|---:|---:|---:|---:|---|
| Defense 守備手 | 17 | 1750 | 0.394 | 0.515 | **0.765** (0.659–0.917) |
| Support ヘルパー | 13 | 1710 | 0.463 | 0.453 | **1.000** (0.923–1.140) |
| Offense 攻撃手 | 20 | 1750 | 0.525 | 0.394 | **1.340** (1.170–1.581) |
| Bomber 爆撃手 | 12 | 1521 | 0.696 | 0.452 | **1.545** (1.382–1.748) |

**S2 — shipped `R_EPISODE.jet` Episode STAT rows**
(`analysis/recovered-reference/EPISODE_STAT_ACTORS.json`, 152 rows, SHA `7f4362cd…`,
2.8.0.1 ⇒ POST). Its `EVCB*` family ~~(n = 41)~~ **(n = 37 hero rows) — CORRECTED
2026-10-06** is the gear-free-template candidate per
`hero-stat-divergence-2026-10-05.md` §S2. Grouped by the **native-recovered `role` enum**
(1 Offense / 2 Defense / 3 Bomber / 4 Support):

> **CORRECTION 2026-10-06 — `EVCB*` Offense medians were also contaminated, not just the
> range.** The `Offense` row's HP median and ATK/HP median were still the `n = 15`
> monster-mixed values, and the parenthetical claim *"Median 1.263 unaffected"* is
> **false**. Measured with the safe filter (`res_id` starts `C` **and** the combat
> record's `type` is `hunter`): `n = 11`, HP median **2400**, ATK/HP median **0.536**,
> ATK/DEF median **1.250**. All **37** `EVCB*` `C*` rows are `hunter`-typed, so
> `EVCB*` needs no `type` filter and `n` is 37, not 41. **Missing filter:** this table
> filtered on the `EVCB*` id-prefix only, which admits `M*` `res_id` rows.
> See [`episode-stat-namespace-filter-2026-10-06.md`](episode-stat-namespace-filter-2026-10-06.md).

| role | n | HP med | ATK/HP med | ATK/DEF med (range) |
|---|---:|---:|---:|---|
| Defense (2) | 8 | 2500 | 0.408 | **0.913** (0.800–1.235) |
| Support (4) | 12 | 2250 | 0.449 | **1.000** (0.833–1.143) |
| Offense (1) | ~~15~~ **11** | ~~2700~~ **2400** | ~~0.565~~ **0.536** | **1.250** (1.077–~~22.500~~ **22.500 is a MONSTER row — CONTAMINATED 2026-10-05**. Correct for hero rows: n = **11**, range `1.077–1.333`. The 4 extra Offense rows are `EVCB*` monsters `M057` (r 22.500), `M044`, `M035`, `M036`. ~~Median 1.263 unaffected~~ **CORRECTED 2026-10-06 — the median is NOT unaffected**: monster-mixed 1.263, hero-only **1.250**; HP median 2700 → **2400** and ATK/HP median 0.565 → **0.536** on the same 4-row subtraction**) |
| Bomber (3) | 6 | 2000 | 0.625 | **1.479** (1.200–2.167) |

**The two sources — one [ORIGDATA] shipped 2.8.0.1, one [COMM] 2019 — agree on the role
ORDER (Defense < Support < Offense < Bomber in ATK/DEF and in ATK/HP) and land within
~0.2 of each other on the medians**, with Support landing on **exactly 1.000 in both**.
That is the strongest cross-validation available in this workspace, and it is *not* in the
prior documents.

### 1.5.c The gap, stated correctly

> **Correction to the premise in P9.** `hero-stat-divergence-2026-10-05.md` §P9 says the
> replica is *"roughly 1.5× high in HP and 7–13× low in ATK/DEF"*. Measured against the 62
> archive rows, **HP is not high — it is low**: replica 1000 vs archive minimum **1277**
> (1.28× low) and median **1651** (1.65× low). HP is the one axis that is roughly in the
> right order of magnitude. The error is entirely in ATK/DEF:

| axis | replica | archive min | archive median | replica vs min | replica vs median | in band? |
|---|---:|---:|---:|---:|---:|---|
| HP | 1000 | 1277 | 1651 | 1.28× **low** | 1.65× low | below the whole range |
| ATK | 100 | 576 | 839 | **5.76× low** | **8.39× low** | no |
| DEF | 50 | 540 | 722 | **10.80× low** | **14.44× low** | no |
| ATK/HP | 0.100 | 0.3714 | 0.6654 | **3.71× below the LOWEST of 62** | 6.65× | no |
| DEF/HP | 0.050 | 0.3513 | 0.4652 | **7.03× below the LOWEST of 62** | 9.30× | no |
| ATK/DEF | 2.000 | 0.6589 | 1.4317 | **1.14× ABOVE the HIGHEST of 62** | 1.40× | **outside the entire recovered range** |
| **(ATK+DEF)/HP** (`s`) — **ADDED 2026-10-05** | **0.150** | **0.8419** | 0.9277 | **5.61× below the LOWEST of 62** | 6.19× | **outside the entire recovered range, by the largest factor in this table** |

The sharpest form of the finding: **the replica's `ATK/DEF` is not merely mis-scaled, it is
on the wrong side — 2.000 (and 3.000 for card `002`) lies outside the band spanned by all
62 recovered heroes, `[0.659, 1.748]`.** Card `002` is 1.72× above the recovered maximum.

**And the `s` row above is the larger error.** `s = (ATK+DEF)/HP` is the quantity that
governs time-to-kill, and the replica is **5.61× below its minimum** — worse than
`ATK/DEF`'s 1.14× overshoot and worse than `ATK/HP`'s 3.71× undershoot. Archive minimum
`s = 0.8419` is `036` Bear, `(755+864)/1923`; archive maximum is `053` Calibur (Defense)
at `1.2171`. Per-role `s` medians are **not** monotone in the role order
(Defense 0.9255 > Offense 0.9190 > Support 0.9088 < Bomber 1.1366), which is why `s` is
reported here only as a replica-defect magnitude and not as a role axis — for the role-axis
question see `archetype-reconciliation-2026-10-05.md`.

### 1.5.d Gear/jewel scaling cannot be the explanation — a hard cross-check

The one identity that exists in **both** S1 and a reading with a *stated, gear-removed*
state:

| source | HP | ATK | DEF | ATK/HP | DEF/HP | ATK/DEF | stated state |
|---|---:|---:|---:|---:|---:|---:|---|
| S1 archive, `051` Beckhen | 1678 | 864 | 660 | 0.515 | 0.393 | 1.309 | level "not shown", gear "not established" |
| `analysis/catalogue/stats/051.md` | 2879 | 1471 | 1149 | **0.511** | **0.399** | **1.280** | **Lv.30, no equipment** (gear-removed; the white column, cross-validated by `24068 + 6291 = 30359`) |

The two readings differ by a **magnitude scalar of 1.716×** while the three ratios agree to
**−0.77% / +1.47% / −2.20%**. A second reading, the anonymous gear-removed tuple from FAQ
image 8 (2 866 / 1 522 / 1 103), gives **0.531 / 0.385 / 1.379** — mid-band again.

`017` Lapis is a *contaminated* version of the same test (archive base card
1537/854/540 = 0.556/0.351/1.581 vs an awakened Lv.30 Reddit reading 4501/2382/1789 =
0.529/0.397/1.331; scalar 2.93×, ratio deltas −4.8% / **+13.1%** / **−15.8%**) — base vs
awakened is not a clean gear comparison, so it is recorded as corroborating direction only,
not as a second clean case.

**Reading.** In the one case where both states are known, the *ratios* were invariant while
the *magnitude* moved by 1.72×. Gear/jewel scaling is therefore the variable that was held
constant. HP:ATK:DEF shape is a **gear-invariant identity property**, and the S1 ratio band
is approximately the nude band — which is why the replica's 0.100 lies outside it at *any*
gear state. Note also that all six published hero references carry `equipment: []`
(`bootstrap.ts:89`, `:160`), so the replica's battle numbers are nude numbers with zero
gear; gear cannot be added later to fix a ratio that gear does not move.

### 1.5.e What `bonus.*` can and cannot express, computed

Derived by applying the §1.2 table to the replica's own `1000/100/50` row:

| | role HP | role ATK | role DEF | ⇒ role **ATK/DEF** | role **ATK/HP** |
|---|---:|---:|---:|---:|---:|
| `none` / `offense` / `deffense` | 1.00 | 1.00 | 1.00 | **1.000** | 0.100 |
| `bomber` | 0.85 | 0.95 | 0.95 | **1.000** | 0.112 |
| `support` | 0.80 | 0.95 | 1.00 | **0.950** | 0.119 |

| | HP | ATK | DEF | ⇒ **ATK/DEF** | **ATK/HP** |
|---|---:|---:|---:|---:|---:|
| `rank_1` | 2.6 | 1.4 | 1.4 | **1.000** | 0.538 |
| `rank_2` | 2.2 | 1.3 | 1.3 | **1.000** | 0.591 |
| `rank_3` | 1.8 | 1.2 | 1.2 | **1.000** | 0.667 |
| `rank_4` | 1.4 | 1.1 | 1.1 | **1.000** | 0.786 |
| `rank_5` | 1.0 | 1.0 | 1.0 | **1.000** | 1.000 |

Two hard consequences:

1. **Every `bonus.rank_*` row has `ATK/DEF = 1.000`, and so do three of the four role
   rows.** The whole table can express an ATK/DEF spread of **1.000 → 0.950**, i.e. **5%**.
   The two recovered sources measure a role spread of **0.659 → 1.748** (Defense → Bomber),
   i.e. **2.65×**. `bonus.*` is therefore **an HP-penalty table with a 5% ATK/DEF nudge**,
   and it *cannot* be the mechanism that produced the recovered role ATK/DEF split.
2. **Applying `bonus.rank_*` to the current base row makes the shape WORSE, not better.**
   `ATK/HP` moves from 0.100 to **0.054 (rank 1) … 0.100 (rank 5)** — rank 1 pushes it
   *further* from the recovered band `[0.371, 0.739]`, and **rank 5 is an identity row
   (`1.0/1.0/1.0`, identical to `none`)**, so the row that matters most for a high-grade
   hero changes nothing. Computed per hero (base A = `1000/100/50` shared by
   `001,003,004,005,006`; base B = `1000/120/40` for `002`):

   | hero | role | rank 1 | rank 2 | rank 3 | rank 4 | rank 5 |
   |---|---|---|---|---|---|---|
   | `001` | Bomber3 | 2210/133/66 | 1870/124/62 | 1530/114/57 | 1190/105/52 | **850/95/48** |
   | `002` | Offense1 | 2600/140/70 | 2200/130/65 | 1800/120/60 | 1400/110/55 | **1000/100/50** |
   | `003` | Defense2 | 2600/140/70 | 2200/130/65 | 1800/120/60 | 1400/110/55 | **1000/100/50** |
   | `004` | Support4 | 2080/133/70 | 1760/124/65 | 1440/114/60 | 1120/105/55 | **800/95/50** |
   | `005` | Defense2 | 2600/140/70 | 2200/130/65 | 1800/120/60 | 1400/110/55 | **1000/100/50** |
   | `006` | Offense1 | 2600/140/70 | 2200/130/65 | 1800/120/60 | 1400/110/55 | **1000/100/50** |

   Note `bonus.bomber` is `(0.85, 0.95, 0.95)`: **strictly dominated** by
   `offense`/`none` `(1.0, 1.0, 1.0)` on *all three* stats. Wiring the role row alone makes
   the Bomber archetype a strictly worse Offense — the opposite of what both recovered
   sources show (Bomber = highest ATK/HP, lowest HP).
3. **Distinct-row count after wiring role × rank.** With bases A (`001,003,004,005,006`)
   and B (`002`): `001` → 5 rows, `002` → 5 rows, `003 ≡ 005 ≡ 006` → **5 rows shared by
   three heroes**, `004` → 5 rows. **20 distinct triples over 30 cells; heroes `003`, `005`
   and `006` remain byte-identical to each other at every rank.**

### 1.5.f Corroboration that `bonus.*` does carry one real signal

`bonus.bomber.hp 0.85` vs the archive's role HP medians: Bomber **1521** / Offense
**1750** = **0.869** — a **2.2 %** error against the shipped 0.85. Two independent sources
(2.8.0.1 shipped data, 2019 community archive) agree on the bomber HP penalty.

`bonus.support.hp 0.80` vs the same: Support **1710** / Offense **1750** = **0.977** — a
**22 %** error. **The support HP penalty is NOT corroborated.** Reported honestly as a
one-sided result: the bomber HP penalty is corroborated, the support HP penalty is not, and
the two must not be treated as equally supported.

### 1.5.g A second, independent shape error on the *secondary* fields

Not previously reported. The card-stat key set is native-recovered
(`analysis/research/gem-reference-contract.md:37`, `analysis/native-all-strings.tsv`
`01d701e3 hp_up` / `01d701e9 atk_up` / `01d701f0 def_up`), and both recovered sources use
the same 13 quantities under the same names. Measured this pass:

| field | replica (all six) | S1 archive (62 rows) | S2 Episode rows |
|---|---|---|---|
| `spd` | **100** | 6 / 7 / 8 (3 discrete values) | `"8.00"` (3–9) |
| `crt_chance` | **5** | 0 / 14 / 20 / 30 / 33 | `"14.00"`–`"58.00"` |
| `crt_dmg` | **150** | 50 / 180 / 185 / 200 / 205 | `"180"`–`"224"` |
| `block_chance` | **0** | 0–36 (Defense role 33–36) | `"0.00"`–`"14.00"` |
| `block_dec_dmg` | **0** | 0–52 (Defense role 50) | up to `"40"` |
| `attr_enhance` / `attr_resist` | **0 / 0** | 29 rows at 5/5, 28 at 0/0, 3 at 2/2 | mostly `"5"` / `"5"` |

`spd 100` is a **~12.5× outlier** against *both* sources, which agree on ≈ 8. `crt_chance 5`
and `crt_dmg 150` sit off the recovered ladders. And `block_chance`/`block_dec_dmg` — the
fields that make the Defense archetype identifiable (archive Defense block 33–36, reduction
50) — are **0 for every published hero**. The elemental axis is also lost: 29 of 62 archive
heroes carry `5/5` and the replica publishes `0/0` for all six, so a **free,
already-recovered differentiator is being thrown away**. (Distinct from
`elem_bonus 20 / elem_def_bonus 10` in §1.2.a, which is the bonus magnitude, not the hero's
own stat.)

**Caveat, and it is a real one:** the `50` displayed under the portrait on the prep screen
is *not* a stat field and its consumer is undecompiled
(`analysis/research/in-game-stats.md:212-231`). So this table is a **scale disagreement
between the replica row and two independent recovered sources**, not a proven client-side
mis-render. Its consequence — that `spd` and the crit/block/element axes are currently
undifferentiated *or* mis-scaled — holds either way.

---

# 2. UNPURE — prioritised shape-correcting options

Ordered by defensibility per unit of risk. Each item states evidence, assumption and
uncertainty. **These are options for the owner, not instructions.** Nothing here has been
applied.

## 2.1 O1 — Per-hero base rows (the minimum; required before anything else can show)

- **What.** Replace the copy at `bootstrap.ts:201` — `ordinaryRankStats({ ...cardOneReference.stat[0] })`
  — with a per-card base object for `003`/`004`/`005`/`006`, and replace card `002`'s
  hand-written row (`:147-150`) with a member of the same per-hero table.
- **Evidence.** The copy at `:201` is the single line that makes four of six heroes
  byte-identical (`card-reference-shape-audit.md:15` states the same: *"003/004 reuse 001's
  exact stat values"*). `hero-stat-divergence-2026-10-05.md` §1 row I5 / `fixture-conflict-audit`
  row **I5** already log this as UNSUPPORTED-with-no-per-hero-balance. The archive has
  **identified rows for all six locally published heroes**, with role-consistent ratios
  (measured §1.5.a/§1.5.b) and with the role/element enums cross-validated **99/100 and
  94/100** against the shipped Episode table — a *hard* identity crosswalk, not name
  matching.
- **Assumption.** That the archive's **ratios** transfer to a nude base row. Supported by
  the 051 gear-invariance cross-check (§1.5.d: ratios moved ≤ 2.2 % while magnitude moved
  71.6 %). **Not** assumed for the archive's absolute magnitudes.
- **Uncertainty.** *Medium.* The honest form of this option is **a per-hero SHAPE with a
  stated local magnitude**, not the archive numerals pasted in. Publishing
  `1521/1058/653` for `001` would both (a) exceed the coverage rule (level and gear state
  unstated, `coverage.md`) and (b) put a level-1 hero at a level-30-ish HP pool while the
  monster row stays at 100 (R2) — i.e. an unobservable change. The **shape** is what the
  evidence supports; the **level** is what nobody has.
- **Risk.** **Zero.** §1.1.f: no derived stat is persisted. §1.1.g: no test pins a hero stat
  value. Reference-row-only, additive, identity-preserving for every owned instance, deck,
  card book, wallet and progression field. The `minRank` filter at `:202` is untouched, so
  `tests/roster.ts:28` and `tests/hunter-traces.ts:22` continue to pass.

## 2.2 O2 — Pair every hero-ATK change with a monster-HP change (mandatory coupling, not optional)

- **What.** Any O1/O3/O4 shape correction must land together with a monster `hp` correction
  in `starterMonsterFor` (`bootstrap.ts:1315`).
- **Evidence.** R2 (`enemy_total_hp_max` = published `hp` verbatim, 2/2), R5 (every recorded
  win is `atk_cnt 1` at ~181 damage against 100 HP), R6 (waves sum), R4 (ATK is live damage).
  At the corrected Bomber-band `ATK/HP ≈ 0.696`, a 1000-HP hero has ATK ≈ 696 and would deal
  ~1 250 per tap against a 100 HP monster.
- **Assumption.** That TTK should be more than one attack. Nothing recovers the original
  TTK; **there is no local evidence for how many attacks a stage should take.**
- **Uncertainty.** *High on the target.* The only ordering anchors are the Episode monster
  rows at rank 5 (`13 000`–`20 000` HP) and the cross-title MON BLAST! Lv.10-MAX figures
  (17 370–18 080, a **different app** — unusable). Monster coverage stays **0/22**, so any
  chosen HP pool is a fixture.
- **Note.** This also touches the **only** value-pinning test in the suite,
  `tests/smoke.ts:325` (`monsters.M001.hp === "100"`). It changes battle difficulty, so it
  is **not** a drop-in: it invalidates the recorded one-tap clear times that earned
  `achieve[].order 1` (*Under 60 s*) in existing saves. That is a progression-visible
  consequence and the owner's call.

## 2.3 O3 — Wire `bonus.rank_*` server-side (real axis, ~zero shape value)

- **What.** Load `analysis/in-game-stats/leveling-chunk09.json` at runtime (the same
  `readFileSync`-relative pattern as `episode-progress.ts:23`) and multiply the per-hero
  base by `bonus.rank_N` inside `ordinaryRankStats` (`bootstrap.ts:57-59`).
- **Evidence.** [ORIGDATA] shipped 2.8.0.1 table, §1.2. `rank_5` being the all-`1.0`
  identity row is exactly why `INDEX.md:370-374` reads rank 1 as the toughest band.
- **Effect on shape.** **Negative.** §1.5.e(2): `ATK/HP` goes from 0.100 to
  0.054 (rank 1) … 0.100 (rank 5) — *away* from the recovered band, and unchanged for
  rank 5. **Do not present O3 as a shape fix.**
- **Effect on differentiation.** Converts the rank *label* into a real *magnitude* axis:
  6 heroes × 5 ranks = 30 cells. But see O5 for why that is not the axis that matters.
- **Assumption.** That the original server applied these. **Unproven.** R3 is a *negative*
  on client application; it says nothing about the server. `INDEX.md` §5.2 classifies
  `rank_1..5` as the **monster**-rank multiplier, which is why applying it to heroes would
  be a new claim.
- **Uncertainty.** **High.** This is the option with the widest gap between "it is shipped
  data" and "it is a hero multiplier". `sp_max`, `sp_increase_*`, `fever_*`,
  `atk_range_scl`, `def_backend_bb`, `left/right/waiting` in the same chunk are plainly
  battle-tuning, which raises the prior that `bonus.*` is a **monster/encounter** table
  (§16.6 item 8 already rules `/reference/GetLevel` a different class).
- **Placement note, if pursued.** Applying `bonus.rank_N` to the **monster** row instead is
  the reading `INDEX.md` §5.2 actually supports, and it is *coupled to the O2 monster-HP
  decision anyway* — one change, one place.

## 2.4 O4 — Wire `bonus.<role>` — **recommend against as a standalone change**

- **What.** Multiply the per-hero base by `bonus.bomber` / `bonus.support` /
  `bonus.none` using the native-recovered `role` enum already in `base.role`
  (`bootstrap.ts:84-85`, `:155-156`, `:199`).
- **Evidence for.** [ORIGDATA] §1.2; corroborated in direction *and* magnitude for bomber
  HP (0.85 vs measured 0.869, §1.5.f); `bootstrap.ts:110-114` already documents the intent.
- **Evidence against — and it is decisive.**
  1. `bomber` scales ATK and DEF **identically** (0.95/0.95) and so does every `rank_*`
     row, so the table's entire expressible ATK/DEF spread is **5 %** against a measured
     **2.65×** role spread (§1.5.e(1)). It *cannot* carry the ATK/DEF split — which is the
     one role axis both recovered sources agree on (§1.5.b).
  2. `bomber` is **strictly dominated** by `offense` on all three stats, so wiring it
     alone makes the Bomber a strictly worse Offense — the inverse of both sources.
  3. `bonus.support.hp 0.80` is **not** corroborated (measured 0.977, a 22 % error).
- **Assumption.** That `bonus.<role>` is a hero base-row multiplier. Given (1), it is more
  plausibly an **encounter/camp** modifier, which is also how `INDEX.md:357-358` reads
  `atk_camp`/`def_camp`.
- **Uncertainty.** **High.** **Verdict: do not wire without O1 first.** With O1 in place the
  role rows could layer on top of per-hero bases as a *small* HP tilt; on their own they
  are a regression.

## 2.5 O5 — Use the archive role bands in the per-hero base rows (the highest-value shape lever)

- **What.** Choose each per-hero base triple's ATK/DEF **split** from the role band
  (Defense ≈ 0.66–0.92, Support ≈ 0.92–1.14, **Offense ∪ Bomber ≈ 1.17–1.75**, then
  split Bomber from Offense inside that top group with `s = (ATK+DEF)/HP`:
  Bomber `s ≥ 1.124`, Offense `s ≤ 0.969`) and then pick a magnitude. This is the
  *only* mechanism in the evidence that can produce the measured role ATK/DEF
  ordering. **Band list CORRECTED 2026-10-05:** the previous wording listed
  "Offense ≈ 1.17–1.58, Bomber ≈ 1.38–1.75" as if they were separate bands;
  **those two ranges intersect over `1.3815–1.5815`**, so `ATK/DEF` alone yields
  three groups, not four.
- **Evidence.** §1.5.b: **two independent sources** — [ORIGDATA] 2.8.0.1 Episode rows
  grouped by the native `role` enum, and [COMM] 2019 archive — agree on the ordering and
  land within ~0.2 on the medians, with Support at exactly 1.000 in both. Role agreement
  between the two sources is **99/100** (the single mismatch being `005` in
  `CB0102_005_1`), and element agreement **94/100**.
- **Assumption.** That Episode-scripted and ordinary base rows express the same role
  grammar. Supported by the EVCB family's own tightness (A/D spread ≤ 0.23 within a role
  except where a boss row intrudes) but **not proved**.
- **Uncertainty.** **Medium.** This is P1 in the prior document, and the new Episode
  evidence raises it from "medium on one community source" to "medium on one community
  source plus one shipped source". It remains a *shape*, not a value set.
- **Explicitly out of scope.** `hero-stat-divergence-2026-10-05.md` **§P4** (element does
  **not** move HP/ATK/DEF — 12 exact-duplicate tuples across different elements, both
  sources) must survive this. Do not add an element axis to the core three.

## 2.6 O6 — Restore the lost secondary axes (cheapest per unit of evidence, adds no dimension)

- **What.** Publish the archive/Episode secondary bands instead of one shared neutral row:
  `spd` ≈ 6/7/8 by role (Defense 6–7, Offense 8) rather than `100`; `crt_chance`
  0/14/20/30/33 and `crt_dmg` 50/180/185/200/205 rather than `5`/`150`;
  `block_chance` 33–36 + `block_dec_dmg` 50 for Defense heroes rather than `0`/`0`;
  `attr_enhance`/`attr_resist` `5`/`5` for the ~29/62 archive heroes that carry it rather
  than `0`/`0`.
- **Evidence.** §1.5.g, measured this pass from two sources; prior document §P5.
- **Assumption.** That the 13 archive fields and the 13 native card-stat keys are the same
  quantities. Well supported — the key sets align one-for-one and `SRSKILL_INFO`/`CSRCardStat.parse`
  read them as **numeric strings** (`gem-reference-contract.md:37`).
- **Uncertainty.** **Medium-low on the ladder, high on `spd`.** The discrete ladders are
  crisp (5 distinct crit values across 62 heroes); `spd 100` vs ≈ 8 is a **12.5× scale
  disagreement** that only the undecompiled prep-screen `50` consumer could explain, and
  `in-game-stats.md:212-231` rules that `50` out as a stat readout. Treat `spd` as needing
  its own decision, separate from the crit/block/element work, which is safe.
- **Why it is worth listing even though §P4 says element adds nothing.** Element adds
  nothing to **HP/ATK/DEF**; it is `attr_enhance`/`attr_resist`, a different field, and it
  is currently 0/0 for every hero where most recovered heroes are 5/5. That is a
  **recoverable** axis being discarded, which is a different complaint from P4.

## 2.7 O7 — `bonus.stage.b_00_01` is the shipped precedent for a per-card multiplier (design note, not an action)

- **What.** §1.2's `bonus.stage.b_00_01` = `{value 1.1/1.1/1.1/1.0/1.0, cards: ["051"]}`
  proves the shipped data is addressable **per card id** *and* per stage, and that it
  targets **051 — the one hero with an identified, gear-removed base row**.
- **Why it matters for option design.** A "per-hero base row + a per-hero bonus row" shape
  is therefore **shipped data's own shape**, not an invention. If the owner wants
  per-hero differentiation to be *data-driven* rather than hard-coded, this is the native
  addressing format for it.
- **Assumption / uncertainty.** **High on everything else.** One populated entry;
  the `b_XX_YY` stage namespace was never decoded and is distinct from `n_XX_YY`;
  `stage_buff` is empty; and R3 means the client demonstrably does not read the sibling
  `rank_*` rows, so if anything read `bonus.stage` it was the original **server**. Listed
  as design provenance only.

## 2.8 Not an option: raising HP to fix ATK/DEF

`player_total_hp_max = hp + hp_up` is **additive** (R1) and `hp_up` is a **flat** `10`
(not a per-level increment). So HP cannot be traded against ATK/DEF by any growth path —
level 1 and level 30 publish the *same* row. Any "fix" that raises HP to lift the ratios
must also raise ATK and DEF by hand, which is O1/O5 with extra steps. **Recorded because
the additive finding contradicts the natural reading of `hp_up`/`atk_up` as per-level
growth, and that misreading would produce a wrong retune.**

---

# 3. The three explicit questions

## 3.1 Is the ATK/DEF-vs-HP gap explainable by gear/jewel scaling?

**No. It is a genuine modelling error.**

1. **The gap is in the wrong direction for gear.** To move a nude `ATK/HP` of 0.100 up to
   the recovered band's floor of 0.3714, gear would have to add **3.71× more ATK than HP,
   relative to the base** — i.e. gear would have to be *ATK-hungry*. Gear then *reduces*
   the gap; it cannot be what created it. The replica's row is HP-dominant relative to a
   state that gear has never been observed to produce.
2. **The one clean controlled case shows ratio invariance.** For `051` Beckhen, a
   `1678/864/660` reading and a **gear-removed Lv.30 `2879/1471/1149`** reading differ by a
   **1.716× magnitude scalar** while all three ratios agree to **≤ 2.2 %**
   (§1.5.d). Gear/jewel contribution is the variable that was held constant; the shape did
   not move when the magnitude did. A third gear-removed reading (FAQ image 8, anonymous)
   sits mid-band at 0.531/0.385/1.379.
3. **The `ATK/DEF` ratio is outside the recovered band entirely.** `2.000` (and `3.000` for
   card `002`) exceeds the maximum of all 62 recovered heroes, `1.7483`. Gear does not have
   to explain a value that sits outside every observed gear state.
4. **The replica has no gear to apply.** All six references publish `equipment: []`
   (`bootstrap.ts:89`, `:160`). There is no local gear system to attribute the gap to, and
   the one gear delta that *is* recovered (`051`, `+437 HP / +317 ATK / +154 DEF`) is
   itself **HP-heaviest** — consistent with gear lowering `ATK/HP`, not raising it.
5. **The only recovered "HP-dominant" rows are per-combat boss tunings.** The shipped
   Episode table contains rows at `ATK/HP` 0.06–0.12 (`CB0002_BOSS` 1000/100/250,
   `CB0003_BOSS` 2000/140/200, `CB0302_010_1` 3000/310/210) — so the replica's shape is not
   *unrepresentable*; it is the shape of the narrow `CB0*_BOSS` script family, adopted as
   the universal ordinary-card and monster row. Note also that the `CB*` family pins DEF
   near 200–300 regardless of HP, which is a script artifact, not an archetype.

## 3.2 Would wiring the shipped `bonus.*` multipliers change per-hero differentiation?

**No — not given `ordinaryRankStats` stamps one shared row. And two of the three
`bonus.*` groups would make things worse.**

1. **`ordinaryRankStats` (`bootstrap.ts:57-59`) is `[1,2,3,4,5].map(rank => ({...base, rank}))`** —
   the same `base` spread into five rows with only the `rank` label changed. Any multiplier
   applied to that `base` is applied **once per rank, identically for every hero that shares
   the base**. Four of six heroes share it, via the copy at `:201`.
2. **Distinct-row arithmetic (computed, §1.5.e(3)).** Distinct bases are A
   (`1000/100/50`, heroes `001`/`003`/`004`/`005`/`006`) and B (`1000/120/40`, hero `002`).
   With `bonus.<role>` × `bonus.rank_N` wired, `003`, `005` and `006` are **byte-identical to
   each other at every rank** — they all take role `none` (Defense → the `deffense` row is
   all `1.0`; Offense is all `1.0`) on base A. Total distinct triples: **20 over 30 cells.**
   Per-hero identity differentiation contributed by `bonus.*`: **zero for `003`/`005`/`006`,
   and only the HP axis for the rest.**
3. **`bonus.<role>` cannot carry the identity at all.** Every `rank_*` row and three of the
   four role rows have `ATK/DEF = 1.000`; only `support` differs, at 0.950. The table's whole
   expressible ATK/DEF spread is **5 %**, against the **2.65×** role spread that two
   independent recovered sources measure. Worse, `bomber (0.85, 0.95, 0.95)` is **strictly
   dominated** by `offense (1.0, 1.0, 1.0)` on all three stats, so wiring it makes the
   Bomber archetype strictly worse — inverting the measured role identity.
4. **`bonus.rank_*` actively worsens the shape.** Applied to the current base, `ATK/HP` goes
   0.100 → 0.054 (rank 1) … 0.100 (rank 5); the recovered band is `[0.371, 0.739]`.
   `rank_5` is the all-`1.0` identity row, so the highest-grade hero changes nothing.
5. **What `bonus.*` *is* good for, honestly stated.** Two things, neither of which is
   per-hero: (a) turning `rank` from a label into a **magnitude** axis — O3; (b) the
   **bomber HP penalty**, which is corroborated in direction *and* magnitude (shipped 0.85
   vs measured 0.869, a 2.2 % error). The **support** HP penalty is **not** corroborated
   (0.80 vs measured 0.977, 22 % error) — one corroborated signal out of two role rows.
6. **Placement is unproven and leans against the hero reading.** R3 recovered a *negative*:
   the client does **not** apply `bonus.rank_1` to a rank-1 monster (published 250 displayed
   as 250, not 260). So the multipliers are either server-side-only, or read on a path the
   local campaign never exercises. `INDEX.md` §5.2 classifies `rank_1..5` as the
   **monster**-rank multiplier; §16.6 item 8 rules `/reference/GetLevel` a different class.
   If any of them were ever applied to heroes, it was server-side, and nothing recovered
   says it was.

## 3.3 What is the minimum change that would make per-hero balance exist locally?

**One expression: replace the copy at `bootstrap.ts:201`.**

```ts
// today — every one of 003/004/005/006 becomes card 001:
skill: fixtureSkillSlots(card.id), stat: ordinaryRankStats({ ...cardOneReference.stat[0] })
```

Giving each of `003`/`004`/`005`/`006` its **own base object** — instead of inheriting
`cardOneReference.stat[0]` — is the minimum, because *per-hero balance means the heroes
differ, and today four of six do not*. That single change yields six distinct identity rows
instead of two. Nothing else in the option list is required for per-hero balance to
**exist**; everything else improves its *quality*:

| step | what it buys | needed for per-hero balance to… |
|---|---|---|
| **O1** — per-hero base rows at `:201` | 6 distinct identity rows (from 2) | **exist** |
| **O5** — role ATK/DEF bands inside those bases | correct archetype shape | be *meaningful* |
| **O2** — paired monster HP | observable combat effect | be *visible* |
| O3 — `bonus.rank_N` | rank becomes a magnitude axis (not a label) | scale across grades |
| O6 — secondary axes | role identity in crit/block/element | be *legible in the UI* |

**Why O1 alone is also the safest option in this document.** §1.1.f: `grep -E '\bhp\b'`
over `state.ts` and `game.ts` returns **no matches** — the replica persists **no** derived
stat. Card instances (`bootstrap.ts:248-258`) carry only `rank`, `exp`, `lock`, gear levels
and skill levels. §1.1.g: the suite asserts `stat.map(row => row.rank)` (the rank *list*),
and **no test pins any hero stat value** — the only value-pinning assertion is
`tests/smoke.ts:325` on `monsters.M001.hp`. And `:202`'s `minRank` filter is untouched, so
`tests/roster.ts:28` and `tests/hunter-traces.ts:22` keep passing.

⇒ **O1 is a pure reference-table change: zero state migration, zero migration risk, no
owned instance, deck, card book, wallet, AP/BP, campaign star or tutorial flag is touched,
and no test needs to change.** O2, by contrast, changes battle difficulty and therefore
invalidates the recorded one-tap clear times behind existing `achieve[].order 1` (*Under
60 s*) stars — so O2 is the owner's call, not a free win.

**What O1 must not become.** It must not publish archive *numerals* verbatim. The coverage
rule forbids it (level and gear state unstated, `coverage.md`), and it would put a level-1
hero at a level-30 HP pool against a 100 HP monster — an unobservable change (R2/R5). The
evidence supports **a per-hero shape with a stated local magnitude**; it does not support a
per-hero magnitude.

---

# 4. Limits of this document

- **Read-only.** No server code, fixture, seed, state file, APK or emulator was changed,
  and no change is proposed as an instruction. The owner decides any retune.
- **Every derived number in §1 is reproducible** from `server-ts/src/bootstrap.ts`,
  `server-ts/src/{hunter-levels,training,game-routes,arena}.ts`,
  `analysis/in-game-stats/leveling-chunk09.json`,
  `analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv`,
  `analysis/recovered-reference/EPISODE_STAT_ACTORS.json`,
  `analysis/catalogue/stats/051.md`, `analysis/research/in-game-stats.md` and the
  `analysis/testing/**` receipts. The TSV/JSON sources were read, not modified.
- **Two claims are new in this file** and are derived arithmetic, not recovered data:
  §1.5.b's two-source role-band agreement, and §1.5.g's secondary-field scale
  disagreement. Both should be re-run by whoever adopts them.
- **§1.5.d's clean case is n = 1.** The 051 gear-invariance cross-check is the *only*
  controlled gear-state pair available. It is strong (ratios ≤ 2.2 % over a 1.716×
  magnitude change, with an exact `24068 + 6291 = 30359` cross-screen validation on the
  gear-removed side) but it is **one identity**. `017` is a contaminated second case and is
  reported as such.
- **Absolute magnitudes remain unrecoverable.** No recovered source prints a level. §1.5.c
  corrects P9's "HP ~1.5× high" to "HP ~1.3–1.65× **low**" — HP is the axis that is roughly
  right; ATK and DEF are 5.8× and 10.8× below even the archive minimum.
- **`bonus.*` remains the weakest-evidenced part of this file.** Two of its three groups
  (`rank_*`, `role`) are contradicted or unexpressive for heroes, one of its two role rows
  is corroborated and one is not, R3 recovered a negative on client application, and
  `INDEX.md` §5.2 classifies the rank rows as monster-rank. It is transcribed because the
  brief asks for it and because it is the only shipped per-stat-multiplier table — not
  because it is safe to wire.
- **Monster coverage stays 0/22 and hero coverage stays 1/113.** Nothing in this file is a
  base tuple for any hero or monster. `051` remains the single identified gear-removed row,
  and §1.5.d does not change its status — it changes what can be inferred about *ratio*
  invariance from it, which is a different claim.
- **`polluted-observations.md` was not appended this run**; the parent mirrors.