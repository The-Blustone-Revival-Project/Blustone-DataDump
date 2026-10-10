# Hero / monster stat divergence — what the replica can and cannot tell apart (2026-10-05)

> ## CORRECTION 2026-10-05 (later the same day) — the four-clean-archetype claim is WITHDRAWN
>
> Two claims below are **over-reads of this file's own evidence** and are struck in
> place: the S1 table cell at **:97** ("do not overlap") and the P1 prior at
> **:293** ("roles occupy disjoint ATK/DEF-ratio bands"). Read
> [`archetype-reconciliation-2026-10-05.md`](archetype-reconciliation-2026-10-05.md)
> for the arithmetic. Summary:
>
> - **Offense and Bomber DO overlap on ATK/DEF.** Offense `1.1695–1.5815` (n=20),
>   Bomber `1.3815–1.7483` (n=12), shared region `1.3815–1.5815` (width **0.2001**).
>   **8 of 12 Bomber rows (66.7 %) and 9 of 20 Offense rows (45.0 %) sit inside the
>   other's band** — 17 of 62 rows (27.4 %) are unassignable on `ATK/DEF` alone.
>   ":63" was literally true only about the single pair it named (Bomber vs
>   Defender); naming that pair and then listing all four ranges beside each other
>   invited — and was read as — a four-way disjointness claim that the data does
>   not support. **The four ranges are 3 groups plus one split pair, not 4 groups.**
> - **`:250–251`'s "disjoint" is false.** The word cannot stand.
>
> **What replaces it (the correct minimal archetype statement).**
> `ATK/DEF` alone yields **three** distinguishable groups —
> Defense `[0.6589, 0.9167]`, Support `[0.9231, 1.1405]`, and
> **Offense ∪ Bomber** `[1.1695, 1.7483]`. Sorted by `r`, Defense and Support are
> single unbroken blocks and *all* role interleaving is inside the Offense/Bomber
> zone. The fourth group requires a **second axis**:
> `s = (ATK+DEF)/HP` splits Bomber (`s ≥ 1.1243`, n=12) from Offense (`s ≤ 0.9691`,
> n=20) with **0 errors in the archive** — a 0.1551 gap, 16.0 % headroom. `s` does
> **not** separate all four: it overlaps on 4 of 6 pairs, and Defense `053` Calibur
> (`s = 1.2171`) sits *above the entire Bomber band*.
> **The honest model is 3 groups on one axis, or 4 only as an `r`-then-`s`
> conjunction — and the two lower `r` cuts have only 0.70 % and 2.55 % headroom.**
>
> **Also added:** the `s` axis exposes a *larger* replica error than the `ATK/DEF`
> error this file reports. See the shape-error file's headline.

**Purpose.** A read-only evidence pass over every local source that *can*
distinguish one hero or monster from another, so that a future rebalance has an
ordered, sourced divergence prior instead of the current state: **one shared
stat row for all six published heroes, one shared row for every published
monster, and a two-row team-EXP table that hard-caps Team level at 2.**

**No fixture, server file, seed, state file, APK or emulator was touched, and
none is proposed to be changed here.** This file is a statement about evidence,
not a retune instruction. The repository owner decides any retune.

**Not done this run, deliberately:** `polluted-observations.md` was **not**
appended (the parent mirrors this lane).

**Coverage effect: none.** Heroes **1/113**, accessories **1/100**, monsters
**0/22** are unchanged. Nothing below is credited as a base tuple.

## Structural-fixture premise, restated and verified

| Fact | Location | Verified this pass |
|---|---|---|
| Every non-001 reference copies card 001's stat row **verbatim** | `server-ts/src/bootstrap.ts:201` (`ordinaryRankStats({ ...cardOneReference.stat[0] })`) | yes — all six heroes 001–006 share one base row |
| Card 002's only variant differs in ATK/DEF | `bootstrap.ts:147` (`hp 1000 / atk 120 / def 40`) | yes; HP identical to 001 |
| `ordinaryRankStats` applies **no** per-rank scaling | `bootstrap.ts` | yes — it maps `[1..5].map(rank => ({...base, rank}))`, i.e. a label stamp only |
| Every published monster is one row: `hp 100 / atk 10 / def 5`, `level 1`, `rank 1`, `hp_page 100` | `bootstrap.ts:1311-1325` | yes |
| Every published stage is `enemy_atk_per 100 / enemy_hp_per 100` | `bootstrap.ts:1049-1050` | yes — all 50 stages, so **per-stage enemy scaling does not exist locally** |
| Team EXP is two threshold rows `0 / 100` ⇒ Team level ≤ 2 | `bootstrap.ts` `user:[{min_exp:0},{min_exp:100}]` | yes |

**Correction to one premise in the task brief.** The brief states that the 37
scripted monster rows are "the only local source that pairs an enemy identity
with HP+ATK+DEF". That is true for monsters, but the **same file** also pairs a
**hero** identity with HP/ATK/DEF: `analysis/recovered-reference/EPISODE_STAT_ACTORS.json`
holds **117 hunter rows across 55 distinct catalog heroes** (`ref_id` + `stat.hp/atk/def`),
alongside the 34 monster rows / 22 monster `res_id`. This second per-hero
numeric source is not described in
[`episode-stat-adjudication-2026-10-05.md`](episode-stat-adjudication-2026-10-05.md)
and is the single most useful new finding of this pass. It does **not** change
coverage — the rows are scripted per-combat tuning, not nude base stats — but it
raises the *identity* reach from 62 to **73 of 113** heroes (see §3a).

---

# 1. PURE — local sources that CAN distinguish heroes or monsters

Each row states the source, what it distinguishes, and what it demonstrably does
**not** distinguish. Everything in §1 is reproducible from the cited file.

## 1.A Sources that distinguish **heroes**

### S1 — Archived Japanese hunter database (62 heroes, 13 numeric fields)

- **Source.** `archived-hunter-database-2019.tsv` /
  [`archived-hunter-database-2019.md`](archived-hunter-database-2019.md).
  Wayback captures of `blustone.jp/hunter/` dated **2019-10-15**, **2019-11-13**
  and **2019-12-16**. 63 index links → 62 numeric profiles → 62 distinct
  `catalog_id`s (one `???` placeholder page).
- **Era.** All captures are **after** the 2019-09-05 rebalance threshold.
- **Distinguishes (measured this pass).**

  | Axis | Measured structure |
  |---|---|
  | Role archetype | ATK/DEF ratio ranges. **~~"do not overlap"~~ WITHDRAWN 2026-10-05 — see `archetype-reconciliation-2026-10-05.md`.** Bomber↔Defender genuinely do not overlap; **Offense↔Bomber DO**, across `1.3815–1.5815` (8/12 Bomber and 9/20 Offense rows inside the other's band). Measured: 爆撃手 `1.3815–1.7483` (n=12), 攻撃手 `1.1695–1.5815` (n=20), 守備手 `0.6589–0.9167` (n=17), ヘルパー `0.9231–1.1405` (n=13) ⇒ **three** `r` groups (Defense, Support, Offense∪Bomber); the fourth needs the second axis `s=(ATK+DEF)/HP`, which splits Bomber `1.1243–1.1642` from Offense `0.8929–0.9691` with 0 errors but overlaps on 4 of 6 role pairs |
  | Role secondary profile | 攻撃手: speed 8, crit 33, crit_damage 200. 守備手: speed 6–7, block 33–36, block_dmg_red 50. 爆撃手: ATK median 1017 (highest), HP median 1521 (lowest). ヘルパー: lowest `combat_power` median (8081) |
  | Rarity ladder | pooled medians HP 1502 / 1624 / 1750 / 1955 and `combat_power` 7105 / 8122 / 9240 / 11504 for ★1–★4; `hp+atk+def` band rises 2761–3145 → 2989–3145 → 3124–3880 → 3673–4022 |
  | HP is **quantized** | 20 distinct HP values across 62 heroes; within a role+rarity cell the **ATK+DEF sum is near-constant** (攻撃手★1: 1393/1393/1394; 爆撃手★1: 1484/1484/1484) — so **HP is banded and the ATK/DEF split is the per-hero variable** |
  | Element does **not** move the core three | **12** heroes share an exact `(hp,atk,def)` tuple with another hero of the **same role but different element** (e.g. `019`=1★攻撃手電撃 and `006`=1★攻撃手火炎 both `1537/817/576`; `005`=2★守備手冷気 and `009`=1★守備手電撃 both `1624/628/893`) |
  | `element_enhance == element_resistance` | true in **60/62** rows (29 at 5/5, 28 at 0/0, 3 at 2/2); only 2 rows break it (0/10) |
  | Discrete ladders | speed 3 values {6,7,8}; crit 5 values {0,14,20,30,33}; crit_damage 5 values {50,180,185,200,205} |

- **Does not distinguish.** No printed level; no equipped/unequipped state; no
  gear quantities; **51 of 113** heroes absent.
- **Independent consistency probe.** `combat_power` is a near-deterministic
  function of the visible fields: least squares on all 13 inputs gives max
  relative error **5.1%**, mean **1.2%**; on `hp+atk+def` alone, max **16.0%**.
  So `combat_power` is *not* an independent datum — it is a display aggregate of
  the same row, and adds no information beyond confirming internal coherence.

### S2 — Episode STAT actor table: **117 hero rows / 55 distinct heroes**

> **FILTER PRECISION NOTE 2026-10-06 (no number in this heading changes).** "117 hero
> rows / 55 distinct heroes" is the **`res_id`-namespace** count and is the figure the
> whole corpus uses; it is *not* the strict hunter count. The safe filter
> (`res_id` starts `C` **and** combat `type == "hunter"`) yields **109 rows / 54
> distinct `ref_id` / 62 distinct `res_id`**; the 8-row gap is the monster-typed `C*`
> set enumerated in the S2 correction below. Treat 117/55 as the *hero-reference-row*
> count and 109/54 as the *hunter-actor-row* count; do not mix them in one statistic.
> Note also that distinct `res_id` (64 in the `C*` namespace) exceeds distinct
> `ref_id` (55) because 9 `ref_id`s carry two `res_id`s (costume/awakened art:
> `008`, `009`, `010`, `028`, `036`, `049`, `051`, `068`, `072` → e.g. `C008`/`C008B`,
> `C051`/`C051A`).

- **Source.** `analysis/recovered-reference/EPISODE_STAT_ACTORS.json`, exported
  from the shipped `R_EPISODE.jet` (SHA `7f4362cd…`). Each row carries
  `id`, `ref_id` (catalog hero id), `res_id` (art pack, e.g. `C017`, `C036B`),
  native `attr` and `role` enums, and a full `stat` block
  (`hp/atk/def/spd/crt_chance/crt_dmg/penetration/attr_enhance/block_chance/block_dec_dmg/attr_resist/hp_regen/rank`)
  plus `skill[]` effect bodies.
- **Era.** 2.8.0.1 shipped pack (server activity 2021-06→2021-08, JET assets
  stamped 2021-08-01) ⇒ **POST** rebalance, and much later than S1.
- **Distinguishes.**
  - **55 distinct heroes** carry a resolved catalog identity plus HP/ATK/DEF and
    the full 13-field secondary profile. 11 of them (`056, 064, 068, 069, 070,
    071, 072, 078, 080, 082, 085`) are **absent from S1**, so they are
    identities S1 cannot reach.
  - The hero rows split into **two structurally different families**, and this
    split is measurable, not assumed:

    | | `EVCB*` rows (37) | `CB*` rows (80) |
    |---|---|---|
    | distinct `hp` values | 13 (1700–~~3000~~ **5000**) | ~~47~~ 46 (170–20000) |
    | distinct `atk` values | 11 (800–1500) | ~~49~~ 45 (~~100~~ **140**–4300) |
    | distinct `def` values | 12 (600–1400) | 33 (140–2100) |
    | distinct `spd` values | 3 {7,8,9} | ~~6~~ 5 {~~4,~~ 5,6,7,8,9} |
    | distinct `crt_chance` values | 5 | ~~15~~ 12 |
    | distinct `hp_regen` values | 5 | 21 |

    > **CORRECTION 2026-10-06 — the `CB*` column was filtered on `res_id` namespace
    > only.** The partition here is `EVCB*` (37) + `CB*` (80) = **117**, i.e. every row
    > whose `res_id` starts `C`. But **8 of those 117 `C*` rows are placed
    > `type: "monster"`** in the shipped combat records and are therefore not hunter
    > rows: `CB0002/0003/0004_BOSS` (all `C010`), and `CB1102_006 / _008 / _011 /
    > _018 / _019` (`C006`, `C008`, `C011`, `C018`, `C019`). Under the safe filter
    > (`res_id` starts `C` **and** combat `type == "hunter"`) the `CB*` column is
    > **72 rows**, not 80, and its distinct-value counts drop as struck above:
    > `hp` 47→46, `atk` 49→45 with the **100** floor removed (that floor is
    > `CB0002_BOSS`, a monster-typed `C010` row), `spd` 6→5 dropping the `4`,
    > `crt_chance` 15→12. **`hp_regen` 21 is unchanged and `EVCB*` is entirely
    > unchanged** (all 37 `EVCB*` rows are `hunter`-typed). The two
    > `EVCB*`-vs-`CB*` qualitative conclusions — coarse/low-variance vs
    > wide/glass-cannon — survive the stricter filter unchanged.
    > Also corrected above: the `EVCB*` `hp` ceiling is **5000**, not 3000
    > (`EVCB0201_023` is 5000/1400/1300; the 13 distinct values are
    > 1700, 1800, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 3000, 5000).
    > See [`episode-stat-namespace-filter-2026-10-06.md`](episode-stat-namespace-filter-2026-10-06.md).

    The `EVCB*` family is coarse and low-variance — consistent with a gear-free
    role template. The `CB*` family is wide and repeatedly shows a
    high-HP / low-DEF (≈200–280) glass-cannon shape, consistent with per-combat
    scripted tuning.
  - **30 of 55** hero refs have **more than one** distinct episode tuple, i.e.
    the same variance pathology already documented for monsters.
- **Identity cross-validation (new, hard).** Comparing the episode native enums
  against S1's crosswalked role/element:
  - **role agrees 99 / 100** rows. The single mismatch is `005` in
    `CB0102_005_1` (episode `role 1` Offense vs archive `守備手` Defense).
  - **`attr` agrees 94 / 100** rows. The 6 mismatches are all rows whose
    `res_id` is a variant pack (`C509`, `C510`, `C008B`, `C027B`, `C036B`,
    `C058B`) or `EVCB0105_059`; `C509/C510` rows are also the ones carrying
    `attr_resist: 99`.
- **Does not distinguish.** No nude/base guarantee; no ordinary level; not the
  ordinary reference table (`LoadCombat` binds actors through the Episode STAT
  cache, and the manifest itself labels it *"Episode-only actor STAT table; not
  ordinary hunter card-base stats"*).

### S3 — VSFan `Hunter Stats [BROKEN IGNORE].xlsx` (19 heroes, per-hero tier ladder)

- **Source.** `analysis/research/vsfan-hunter-stats-raw.tsv`, transcribed from
  `analysis/VSFan/Research/Blustone/Hunter Stats [BROKEN IGNORE].xlsx`.
  189 rows = 19 heroes × 10 tier labels (`- Base/- Max` ×
  Bronze/Silver/Gold/Green/Blue); **67 rows populated**, 122 all-`N/A`.
- **Era.** Archived APK **1.4.4.1** ⇒ **PRE** 2019-09-05, and the workbook is
  self-flagged broken.
- **Distinguishes.**
  - A **tier ladder per hero**: Base/Max within a tier is a near-constant scalar
    multiplier. Over 25 populated pairs: HP 1.137–1.261 (median **1.199**),
    ATK 1.137–1.314 (median **1.201**), DEF 1.115–1.252 (median **1.201**).
    Tier is therefore a *scalar knob*, not a per-stat rebalance.
  - **Tier progression is stat-asymmetric per hero.** Captain (tank)
    151/116/186 → 257/162/260 → 437/229/362 → 744/320/505: HP grows 4.9×.
    Lantern (attacker) 412/441/259 → 693/608/357: ATK grows 1.38× against
    HP 1.68×. This is a real divergence axis, independent of S1.
  - HP quantized again: **32** distinct values in 67 rows.
- **Does not distinguish — and this source has a hard contamination limit.**
  - **4 numeric tuples are byte-identical across two different hero names**:
    Locke ≡ Metis at `- Base Bronze` (126/201/126), `- Base Silver`
    (211/278/174), `- Max Silver` (240/336/203), `- Base Gold` (355/384/240).
    Balian ≡ Sylvester at `- Base Bronze` and `- Base Silver`. Distinct heroes
    do **not** have distinct base rows here, so **this workbook cannot be used as
    a per-hero divergence source** — only as a per-hero *ladder-shape* source.
  - Magnitudes are **not** a rescale of S1. VSFan Lapis `151/186/116` vs
    archive `017` Lapis `1537/854/540`: ratios 0.098 / 0.218 / 0.215 with the
    **ATK/DEF orientation reversed**. Different stat basis, not a scale factor.
    Do not join the two tables.

### S4 — `LEVELING.jet` chunk 9 `bonus` block (role and rank multipliers)

- **Source.** `analysis/in-game-stats/leveling-chunk09.json`, SHA-identical to
  `analysis/recovered-data/campaign-stages.raw-LEVELING-chunk9.txt`
  (`C9F9C1BB…`). Extracted from the shipped 2.8.0.1 APK.
- **Era.** 2.8.0.1 ⇒ **POST**.
- **Distinguishes — and this is the only local source that encodes role and
  rank as *mechanical* stat divergences:**

  | Key | hp | atk | def |
  |---|---:|---:|---:|
  | `bonus.none` / `offense` / `deffense` | 1.0 | 1.0 | 1.0 |
  | `bonus.bomber` | **0.85** | 0.95 | 0.95 |
  | `bonus.support` | **0.80** | 0.95 | 1.0 |
  | `bonus.rank_1` | **2.6** | 1.4 | 1.4 |
  | `bonus.rank_2` | 2.2 | 1.3 | 1.3 |
  | `bonus.rank_3` | 1.8 | 1.2 | 1.2 |
  | `bonus.rank_4` | 1.4 | 1.1 | 1.1 |
  | `bonus.rank_5` | 1.0 | 1.0 | 1.0 |
  | `bonus.atk_camp` / `def_camp` | 2.0 | 2.6 | 1.0 |

  `bonus.stage` has exactly one populated entry, `b_00_01`
  `{value {1.1,1.1,1.1}, cards: ["051"]}`.
- **Cross-check against S1 (independent agreement in direction).** The archive's
  role medians are consistent with the bomber/support HP penalties: 爆撃手 HP
  median **1521** is the lowest of the four roles, 攻撃手 and 守備手 are both
  **1750**, ヘルパー **1710**. Two independent shipped/community sources point
  the same way.
- **Does not distinguish, and is currently unused.**
  - `INDEX.md` §5.2 classifies `rank_1..rank_5` as the **monster-rank**
    multiplier, so it must **not** be applied to heroes without native proof.
  - Grep-verified this pass: **no file under `server-ts/src` consumes any of
    `bonus.rank_*`, `bonus.bomber`, `bonus.support`, `bonus.offense`,
    `bonus.deffense`, `bonus.atk_camp`, `bonus.def_camp` or `elem_bonus`.** The
    multipliers exist in shipped data and are inert in the replica.
  - `bootstrap.ts` documents the *intent* ("an Offense takes no HP penalty
    (`offense 1.0`)") but the implemented row gives Bomber 001 and Offense 002
    the **same HP 1000**, so even the intended role ratio is not applied.

### S5 — Sources that distinguish **identity only** (no numbers)

`analysis/catalogue/data/monsters.json` (22 entries: `M001`–`M021`, `M100`,
art filename + byte size only — **no stats**); `CHAR_STR_RO` titles; the
`C001`–`C085` art packs; and the identity-only portrait leads in the polluted
ledger. These can name a hero or monster and nothing more.

## 1.B Sources that distinguish **monsters**

### S6 — Episode STAT monster rows (34 rows / 22 distinct `res_id`)

- Same file as S2. Already adjudicated in
  [`episode-stat-adjudication-2026-10-05.md`](episode-stat-adjudication-2026-10-05.md);
  re-derived this pass and **confirmed**: 34 `M*` rows + 3 monster-placed `C010`
  rows = the 37 monster-like rows; 22 distinct `res` identities; **6** of them
  carry ≥2 distinct tuples, up to a **160×** HP spread (`M034` 100 → 16000).

  > **CORRECTION 2026-10-06 — "the 37 monster-like rows" is an INCOMPLETE
  > partition, not the full monster set.** `34 M* + 3 C010 = 37` omits **5 further
  > `C*`-namespace rows that are also placed `type: "monster"`**:
  > `CB1102_006` (`C006`), `CB1102_008` (`C008`), `CB1102_011` (`C011`),
  > `CB1102_018` (`C018`), `CB1102_019` (`C019`) — all five in `EPISODE_COMBAT_CB1102.json`
  > at thumb `level 1 / rank 5 / hyper 2`. The exhaustive monster-like set is
  > therefore **42 rows (34 `M*` + 8 monster-typed `C*`)**, and the exhaustive hero
  > set is **109 rows**. Because the corpus's 117-row figure is the `C*` namespace,
  > an auditor following "37 monster-like" alone would silently classify those 5
  > as hero rows. All S6 numbers that depend on the `M*` rows *only* (22 distinct
  > `res`, the 6 multi-tuple identities, the 160× spread, the inert secondary
  > fields) are **unaffected**. See
  > [`episode-stat-namespace-filter-2026-10-06.md`](episode-stat-namespace-filter-2026-10-06.md).
- **Monster secondary fields are almost entirely inert**: all 34 rows are
  `attr_enhance 0 / attr_resist 0` except 2 rows at `20 / 10`; every monster
  `skill[]` is `[0,0,0,0,0]`. So the monster rows carry **only** HP/ATK/DEF —
  which is exactly the tuple the coverage rule demands, and exactly why the
  adjudication file's recommendation (keep 0/22) still stands.
- **Catalog overlap, re-confirmed:** only `M001` and `M100` are inside the
  22-monster catalog; the other 20 `res` IDs are outside it, and `M002`–`M021`
  never appear.

### S7 — Cross-title MON BLAST! monster cards (excluded)

Snowfox 17,370/790, Pandahawk 17,460/1,110, Moonwoof 18,080/850, all
Gold Card Lv.10 MAX. `com.vshower.prd_pf` is a **different app**; no
entity/scale crosswalk exists. Recorded, usable for nothing.

## 1.C Sources that distinguish **neither** (negative results, kept explicit)

- `EQUIP.jet` — 24 `I2` texture resources, no stat table.
- `LEVELING.jet` chunks 1 / 9 / 19 — upgrade costs, shared multipliers,
  `power,rank,hyper,level` thresholds. No per-hero or per-monster tuple.
  Chunk 19's level-30 power spread (★1 4,000 / ★2 9,700 / ★3 31,200 /
  ★4 86,400 / ★5 185,900) is a *power* ladder, not a stat ladder.
- Stage percentage fields — all 50 stages are exactly `100/100`, so there is no
  per-stage divergence to read, in either direction.
- The replica's own state file — `coverage.md` rule "Do not use current replica
  fixture data as original-game evidence" still applies.

---

# 2. UNPUR[E] — prioritised divergence priors for a future rebalance

Ordered by defensibility. Every item states source, era and uncertainty. **These
are priors, not values to install.** None is a recovered base stat.

## P1 (strongest) — Role archetype sets the ATK/DEF **split**; HP is banded by rarity

> **P1 AMENDED 2026-10-05** by `archetype-reconciliation-2026-10-05.md`. The prior
> is **retained and still the strongest item in this document**; only its claim of
> band **disjointness** is corrected. Offense and Bomber share
> `1.3815–1.5815` on ATK/DEF, so the role axis is a **three-group** ordering on
> that ratio alone, with the Bomber/Offense split requiring the second
> scale-free axis `s = (ATK+DEF)/HP`. See the struck sentence below and §P1-corrected.

- **Source.** S1 (`archived-hunter-database-2019.tsv`), measured directly.
- **Era.** POST-2019-09-05 (Oct–Dec 2019 captures).
- **Prior.** Model a hero as `HP = f(rarity)` and `(ATK, DEF) = g(rarity)` split
  by role. S1 shows the ATK+DEF sum is near-constant inside a role+rarity cell
  while the HP value is drawn from a 20-step ladder; roles occupy ~~disjoint
  ATK/DEF-ratio bands (Bomber 1.38–1.75, Defender 0.66–0.92)~~
  **STRUCK 2026-10-05 as false — Offense and Bomber overlap.** Corrected: role
  **medians** are strictly ordered on ATK/DEF (Defense 0.7647 < Support 1.0000 <
  Offense 1.3396 < Bomber 1.5452), Defense and Support are **genuinely disjoint**
  from every higher role (gaps 0.0064 and 0.0290), and Offense/Bomber is resolved
  by `s` (Bomber ≥ 1.1243, Offense ≤ 0.9691) rather than by `r`.
- **Uncertainty.** Medium. Level and gear state are unknown, so this is a
  *shape*. S2's `EVCB*` family is consistent in direction but at a different
  magnitude. S4's `bomber hp 0.85 / support hp 0.80` agrees in direction and is
  shipped data, but is not proven to be the mechanism that produced S1. **New:**
  the two surviving `r` cuts have only **0.70 %** and **2.55 %** headroom, so the
  ordering is real but brittle; do not treat any single row's `r` as
  self-identifying.

## P2 — Rarity is the primary **magnitude** axis

- **Source.** S1 (rarity medians), corroborated in shape by `INDEX.md` §7.2's
  chunk-19 level-30 power spread and by S4's `rank_1..rank_5` (hp 2.6 → 1.0).
- **Era.** POST (S1) and POST (S4); the §7.2 anchor is 2.8.0.1.
- **Prior.** HP/ATK/DEF totals scale strongly with draw rarity. Current ratios
  from S1 pooled medians: HP 1502 / 1624 / 1750 / 1955 and
  `hp+atk+def` ≈ 2900 / 3140 / 3450 / 3900 for ★1–★4.
- **Uncertainty.** Medium. The replica's `recruitBirthRanks`
  (`002:2, 003:3, 004:1, 005:2, 006:1`) already agrees with S1's
  `rarity_on_draw` for all five of those IDs — a real, checkable corroboration —
  but 001 is published at rank 1 locally while S1 says ★3.

## P3 — Per-hero residual divergence **within** a role+rarity cell is small but real

- **Source.** S1's 12 exact-duplicate tuples (all same-role, cross-element)
  versus the 39 heroes whose tuple is unique.
- **Era.** POST.
- **Prior.** Most of the apparent per-hero spread is role + rarity. True
  per-hero identity divergence is the residual — roughly the difference between
  the cell median and the hero's own row, on the order of a few percent to
  ~20% depending on cell.
- **Uncertainty.** Medium-high, because level/gear contamination varies per row
  and cannot be separated without the missing context. S3's Locke ≡ Metis
  duplication is a warning that some "per-hero" differences in the wild are
  template artefacts.

## P4 — Element is **not** a divergence axis for HP/ATK/DEF

- **Source.** S1: 12 exact-duplicate `(hp,atk,def)` tuples across different
  elements; per-element pooled ranges all span the full table
  (冷気 HP 1277–2033, 火炎 1277–1968, 電撃 1277–2019).
- **Era.** POST.
- **Prior.** Give heroes element identity and `attr_enhance`/`attr_resist` (both
  usually equal, 0/0 or 5/5), but **do not** vary the core three by element.
- **Uncertainty.** Low-medium. This is a *negative* prior and is the cheapest
  one to act on, because it removes a dimension rather than adding numbers.

## P5 — Role sets the **secondary** profile, not just the core three

- **Source.** S1 role medians; S2 `EVCB*`/`CB*` families.
- **Era.** POST (both).
- **Prior.** 攻撃手 → speed 8, crit 33, crit_damage 200. 守備手 → block 33–36,
  block_dmg_red 50, speed 6–7, low crit. 爆撃手 → highest ATK, lowest HP.
  ヘルパー → lowest `combat_power`. The replica publishes
  `spd 100 / crt_chance 5 / crt_dmg 150` for **every** hero, so all of this is
  currently undifferentiated.
- **Uncertainty.** Medium. S2's `CB*` family shows the same secondary fields
  being overridden per combat, so these are template values, not constants.

## P6 — Episode `EVCB*` rows are a candidate **gear-free role template**

- **Source.** S2's family split, plus the ratio test against S1.
- **Era.** POST, but ~2 years later than S1.
- **Prior.** For the 23 shared `EVCB*` heroes whose per-hero
  `(hp,atk,def)` ratio spread stays ≤25%, the EVCB/archive ratio clusters at
  **median 1.358, mean 1.369, CV 13.7%, range 0.994–1.797** — i.e. a
  near-common scale factor. If EVCB rows are a fixed higher-level gear-free
  template, then `EVCB ÷ 1.36 ≈ archive` gives a usable first-pass per-hero
  shape. Three rows break the cluster and are excluded: `023`
  (spread 91%), `029` second row (spread 231%), and `036`/`060` at the low end.
- **Uncertainty.** **High, and this is the weakest of the "medium" items.** The
  cluster is only as good as the assumption that EVCB and archive rows are the
  same measurement at different levels. `EVCB0201_023` alone breaks it. Treat
  1.36 as a *scale hypothesis to test*, never as a constant.

## P7 — Monster divergence is **per-encounter**, not per-monster

- **Source.** S6, re-confirmed: 6 `res` IDs carry ≥2 tuples, up to 160×;
  thumb level does not predict STAT; `CB1301_M1` and `CB1501_M2` are both
  M035 at L20/r5/h2 yet read 7000/6000/300 vs 7000/6800/280; `CB1201_M1` is
  reused across `CB1201` (L10) and `CB1401` (L15) with unchanged STAT.
- **Era.** 2.8.0.1 ⇒ POST.
- **Prior.** Any monster rebalance needs **two** axes — an identity base plus a
  per-encounter difficulty scalar — or the S6 rows must be collapsed under an
  explicitly stated rule. There is no local evidence for the identity axis.
- **Uncertainty.** High, and unresolvable from current evidence. Paired rows
  (M035/M036 in three encounters with identical STAT) mean each *encounter*
  must be counted once, not each row.

## P8 — Tier is a **scalar** knob (from a contaminated source)

- **Source.** S3, 25 Base→Max pairs: median 1.199 / 1.201 / 1.201 for
  HP / ATK / DEF.
- **Era.** **PRE** (APK 1.4.4.1) and self-flagged broken.
- **Prior.** If any growth stage is modelled as a multiplier, ~1.2× is the
  observed per-tier scalar, not a per-stat curve.
- **Uncertainty.** **High.** PRE-era, from a workbook where four tuples are
  shared across two hero names. Use only as a shape hint; never as a per-hero
  source.

## P9 — Magnitude anchor for the overall stat scale

- **Source.** S1's `rarity_on_draw` HP ladder (★1 1277–1624, ★3 1521–1968) and
  `combat_power` (6565–12725), plus the anonymous FAQ image-8 gear-removed
  tuple 2,866/1,522/1,103.
- **Era.** S1 POST; FAQ image 8 PRE.
- **Prior.** A ★1 hero's base HP is on the order of **1.3k–1.6k**, not the
  replica's 1000, and ATK/DEF are on the order of **600–1000 / 540–900**, not
  100/50. That places the replica's `1000/100/50` roughly **1.5× high in HP and
  7–13× low in ATK/DEF** relative to the archive rows — i.e. the replica is not
  merely under-scaled but **mis-shaped** (far too little ATK/DEF per HP).
- **Uncertainty.** High on the absolute level (S1's level is unknown); the
  *shape* claim is the defensible part.

## P10 — What the team-EXP fixture hides

- **Source.** `bootstrap.ts` two-row `user:[{min_exp:0},{min_exp:100}]` table;
  S1's per-hero `combat_power` ladder; `leveling-chunk019.csv`.
- **Era.** fixture has no era.
- **Prior.** With a two-row threshold table, `GetUserLevel` can only ever
  return 1 or 2, so every stage's `group_exp` compresses into one step and no
  team-level-gated content can ever unlock. Any rebalance that touches
  progression needs a real ladder here first.
- **Uncertainty.** High: **no local recovered team-level ladder exists.**
  S1's `combat_power` is per-hero, and `chunk019`'s `rank` column is
  monster-rank, so neither may be repurposed as a team ladder. This is a
  fixture-shape defect with **no** evidence-side substitute.

---

# 3. What this pass separates

## 3a. Identity resolution — now possible / now closed

**Closed (new, hard).** The S2 ↔ S1 crosswalk is validated by the shipped native
enums, not by name matching:

- **role: 99/100 agreement.** The one mismatch is `005`/`CB0102_005_1`. The
  episode table is otherwise reliable for role, and this independently
  corroborates the numeric role enum (1 Offense / 2 Defense / 3 Bomber / 4
  Support) that `card-enums.md` recovered by text dispatch.
- **element: 94/100 agreement**, with all 6 mismatches on variant `res_id` packs
  or the sentinel-bearing rows.

**Now reachable.** Identity reach for *some* numeric triple rises from 62 to
**73 of 113** heroes (S1 ∪ S2, 44 shared), and 11 of the newly reachable
(`056, 064, 068, 069, 070, 071, 072, 078, 080, 082, 085`) exist **only** in S2.
**40 heroes** are in neither source.

**Still open.** `attr_resist: 99` on 10 rows is an apparent sentinel, not a
resistance value — including on the `C509`/`C510` rows whose `attr` contradicts
the archive. Those rows need a rule before their element can be trusted.

**Explicitly not closed.** Neither S1 nor S2 supplies a printed **level** or an
**equipped state**. That is the single blocker on promoting any of the 73 rows
to strict coverage, and nothing in this pass moves it.

## 3b. Magnitude priors — ranked

1. **Shape before scale** (P1, P4, P5): role splits ATK/DEF *(corrected 2026-10-05:
   three `r` groups, not four disjoint ones — see the header correction)*, rarity sets
   magnitude, element does nothing to the core three. These three are the
   cheapest and most defensible, and two of them *remove* a dimension.
2. **Scale hypothesis** (P6): EVCB ÷ ~1.36 ≈ archive shape, CV 13.7% on 23
   heroes. Test it; do not install it.
3. **Absolute scale** (P9): the replica's ATK/DEF are an order of magnitude below
   every recovered hero row while HP is only ~1.5× above. Mis-shape, not just
   mis-scale.
4. **Growth as a scalar** (P8): ~1.2× per tier, PRE-era, contaminated source.

## 3c. What remains unrecoverable from anything local

- **Any nude/base hero stat tuple** for a named hero, at a stated level, with
  gear removed. 1/113 stands.
- **Any monster identity base tuple.** S6 is the only identity+triple source and
  it is per-encounter scripted; 20 of its 22 `res` IDs are outside the catalog
  anyway. 0/22 stands.
- **The original level-growth curve.** `ordinaryRankStats` stamps a rank and
  nothing more; chunk 19 is `power,rank,hyper,level` with monster-rank;
  chunk 1 is upgrade costs. No hero level→stat curve exists locally.
- **The team-level ladder.** No local source at all (P10).
- **Which of `bonus.rank_1..rank_5` applies to heroes.** `INDEX.md` §5.2
  classifies it as monster-rank; no native proof either way.
- **Whether the 73 now-reachable identities could ever satisfy the strict
  coverage rule.** That is a definition call for the parent (level + gear
  context), exactly as in `episode-stat-adjudication` §1.5.

---

## Limits of this pass

- **Read-only.** No fixture, server file, seed, state file, APK or emulator was
  touched, and no change is proposed here.
- Every derived number in §1 and §2 is reproducible from the four cited local
  files plus `bootstrap.ts`; the derivations were computed this pass and the
  source TSV/JSON were not modified.
- **Zero coverage effect.** Heroes 1/113, accessories 1/100, monsters 0/22.
- The one substantive new finding is a **source**, not a value: S2's 117 hero
  rows / 55 identities. It supplies divergence *shape* and closes *identity* for
  11 heroes S1 cannot reach; it supplies no base stat, and its own manifest
  disclaims ordinary hunter card-base status.
- `polluted-observations.md` was **not** appended this run; the parent mirrors.