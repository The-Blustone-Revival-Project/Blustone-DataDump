# CANDIDATE per-hero base-stat table — assembled from the two recovered numeric identity sources (2026-10-05)

## 0. What this file is, and what it is not

**This is a CANDIDATE research artefact.** It is an evidence table plus a derived
shape/band analysis. It is **not** a proposal, **not** a fixture, **not** a retune, and
**it must not be written into `server-ts/src` or any other fixture on the strength of this
file alone.** The repository owner decides any retune.

**Nothing was changed.** No server file, fixture, seed, state file, APK, emulator, phone,
Ghidra project or LevelDB was touched. `polluted-observations.md` was **not** appended
(deliberate, per the parent-mirrors-this-lane convention). The two source files were
**read** and not modified:

- `analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv`
  — 62 numeric rows.
- `analysis/recovered-reference/EPISODE_STAT_ACTORS.json`
  — 152 rows; 117 hero rows / 55 hero identities **under the `res_id`-namespace
  filter; 109 / 54 under the strict `hunter`-typed filter** (see §1.2).

**Coverage effect: none.** Heroes stay **1/113**, accessories **1/100**, monsters **0/22**
per `coverage.md`. Every row below is **IMPURE** (§1.3) and earns **zero** base-stat
coverage credit.

### 0.1 The defect this table is aimed at

`server-ts/src/bootstrap.ts:201` maps `additionalReferences` (heroes `003`, `004`, `005`,
`006`) through `ordinaryRankStats({ ...cardOneReference.stat[0] })`, so **four of the six
published heroes are byte-identical copies of card `001`'s rank-1 row**; card `002` carries
a hand-written second row. Per
[`replica-shape-error-2026-10-05.md`](replica-shape-error-2026-10-05.md):

- there are only **three** stat-literal sites in `server-ts/src` (two hero rows, one
  monster row);
- the replica's `ATK/DEF` (**2.000** for `001`, **3.000** for `002`) lies **outside the
  entire band spanned by all 62 archive heroes, `[0.659, 1.748]`**;
- `hp_up` is a **flat +10**, and `player_total_hp_max = hp + hp_up` additively, so
  **levelling changes nothing** and HP cannot be traded against ATK/DEF;
- wiring `bonus.*` would be a **regression** (`bonus.bomber` is strictly dominated by
  `bonus.offense`; every `rank_*` row has `ATK/DEF = 1.000`);
- the minimum change is **one expression** with **zero state migration and zero test
  breakage** (`grep -E '\bhp\b'` over `state.ts`/`game.ts` returns no matches; no test
  pins a hero stat value).

This file supplies the **evidence table** that one expression would consume. It does not
supply the expression, and it does not decide the magnitude (§6.3).

---

## 1. Sources, era tags, and the standing impurity warning

### 1.1 S1 — 2019 archive `blustone.jp/hunter/` (community; POST-rebalance)

| | |
|---|---|
| File | `archived-hunter-database-2019.tsv` |
| Content | **62 numeric rows**, 62 distinct `catalog_id`s, **13 numeric fields** each |
| Capture timestamps | 33 distinct values, **2019-10-15 to 2019-12-16** (latest `20191216060610`) |
| Era | **POST** the 2019-09-05 rebalance (`stat-version-context.md`) |
| Resolution | **per hero** — 20 distinct HP values, **50 distinct `(hp,atk,def)` tuples over 62 rows** |
| `level` column | literally `"not shown"` on every row |
| `gear_state` column | literally `"not established"` on every row |

### 1.2 S2 — shipped `R_EPISODE.jet` Episode STAT table (ORIGDATA; POST-rebalance, ~2 years later)

| | |
|---|---|
| File | `analysis/recovered-reference/EPISODE_STAT_ACTORS.json` |
| Content | **152 rows** (index 80 is a literal `{}`, so 151 identifiable). Filtering to hero rows (`ref_id` = 3-digit catalog id **and** `res_id` starts `C`) leaves **117 hero rows / 55 distinct `ref_id` / 64 distinct `res_id`**. ~~The 3 rows dropped for this purpose (`CB0001_M01`, `CB0001_BOSS`, `CB0002_M01`) carry `res_id` `M001` / `M034` / `M040` — they are monster-placed.~~ **CORRECTED 2026-10-06: the namespace filter drops 34 rows, not 3** — every row whose `res_id` starts `M`, over 22 distinct tokens (so `152 - 1 - 34 = 117`; the "3 rows" wording never reconciled with the 117). Of the 34, only 3 carry a hero-shaped `ref_id` (`CB0001_M01` → `001`, `CB0001_BOSS` → `040`, `CB0002_M01` → `034`), which is why a `ref_id`-only filter reads as "3 dropped" and silently inflates any hero statistic by 3. |
| Second filter this table did **not** apply | **[CORRECTED 2026-10-06]** `res_id` namespace alone is not sufficient. **8 of the 117 `C*` rows are placed `type: "monster"`** in the shipped combat records and are not hunter rows: `CB0002/0003/0004_BOSS` (`C010`) and `CB1102_006/_008/_011/_018/_019` (`C006`, `C008`, `C011`, `C018`, `C019`). Safe filter (`res_id` starts `C` **and** combat `type == "hunter"`) ⇒ **109 rows / 54 `ref_id` / 62 `res_id`**. **Every `EVCB*` statistic in this file is unaffected** (all 37 `EVCB*` rows are `hunter`-typed); the `CB*` figures are affected — see the §1.2 family row and §2.6.4. |
| Family split | **`EVCB*` 37 rows / 33 distinct `ref_id`** (coarse, `hp` 1700–5000, `rank 5`) vs **`CB*` ~~80~~ 72 rows** (wide, `hp` 170–20000, `rank` 1–5). The `80` is the `C*`-namespace `CB*` count and includes the 8 monster-typed rows above; `72` is the `hunter`-only count. |
| Era | shipped **2.8.0.1**, JET assets stamped **2021-08-01** — POST, and **~2 years after S1** |
| Enums | native `attr` (1 Fire / 2 Ice / 3 Lightning) and `role` (1 Offense / 2 Defense / 3 Bomber / 4 Support) |
| Status | the export's own manifest labels it *"Episode-only actor STAT table; **not** ordinary hunter card-base stats"*; `LoadCombat` binds actors through the Episode STAT cache |

### 1.3 IMPURITY — applies to **every** row of the candidate table

| Contaminant | S1 archive | S2 Episode |
|---|---|---|
| **Printed level** | absent (`"not shown"`) | absent |
| **Equipped / gear state** | absent (`"not established"`) | n/a (no gear model in the table) |
| **What the row actually is** | an unknown-level, unknown-gear **profile-page reading** | a **scripted per-combat actor** row |
| **Era tag** | 2019-10 to 2019-12 | 2.8.0.1 / 2021 |

=> **No candidate row below is a base stat.** What survives is the **shape**
(`ATK/DEF`, `(ATK+DEF)/HP`), for which §2.3 gives one clean invariance proof, and it is an
**n = 1** proof. The **magnitude** is unrecoverable from either source.

---

## 2. Method — why ratios, which ratios, and what tolerance

### 2.1 Why a scale-free feature is mandatory

Neither source prints a level. An absolute HP/ATK/DEF comparison is therefore not
available. Only **ratios within a single row** are. Two are used:

| Feature | Definition | Invariant under |
|---|---|---|
| `r` = **ATK/DEF** | `atk / def` | any uniform scalar on all three stats; any growth curve that scales ATK and DEF together; **gear** (§2.3) |
| `s` = **(ATK+DEF)/HP** | `(atk+def)/hp` | any uniform scalar; **gear** (§2.3). *Not* invariant if the growth curve scales HP differently from ATK+DEF — that path is unmeasured |

A third, `p = ATK/(ATK+DEF)`, is carried only as a sanity cross-check in §2.3 and is
redundant given `r`.

### 2.2 The `s` finding is stronger than the `r` finding, and is new here

The defect document reported only that `r = 2.000` is outside the recovered band. The
companion feature is worse:

| | replica | archive range (n=62) | position |
|---|---|---|---|
| `r` = ATK/DEF | 2.000 (`001`) / 3.000 (`002`) | **[0.659 … 1.748]** | **above the maximum** |
| `s` = (ATK+DEF)/HP | **0.150** (`001`) / 0.160 (`002`) | **[0.842 … 1.217]** | **5.6x below the minimum** |

The replica is not merely mis-split between ATK and DEF: it is **HP-dominant by a factor
of ~5.6 on the combined offence+defence budget per point of HP**, while simultaneously
being ATK-over-DEF-heavy in the one axis that *is* role-structured. Both errors have to be
fixed by the same per-row replacement, and `s` is the better-behaved of the two because it
is what actually governs time-to-kill.

### 2.3 Gear-invariance proof for the shape — `n = 1`, and it is stated as such

`051` Beckhen is the **only** identity present in S1 and in a reading with an explicitly
gear-removed state (`analysis/catalogue/stats/051.md`, cross-validated by an exact
`24068 + 6291 = 30359` cross-screen match):

| reading | HP | ATK | DEF | `r` | `s` | `p` | stated state |
|---|---:|---:|---:|---:|---:|---:|---|
| S1 archive `051` | 1678 | 864 | 660 | 1.3091 | 0.9082 | 0.5669 | level *not shown*, gear *not established* |
| catalogue `051` | 2879 | 1471 | 1149 | 1.2802 | 0.9100 | 0.5615 | **Lv.30, no equipment** |
| deviation | **x1.7157 magnitude** | | | **2.20 %** | **0.20 %** | **0.97 %** | |
| FAQ img-8 anonymous nude | 2866 | 1522 | 1103 | 1.3799 | 0.9159 | — | gear-removed, identity/level unknown |

=> a **1.716x magnitude** change moved all three shape features by **at most 2.2 %**. Gear
therefore moves the magnitude and holds the shape. **Caveat, stated plainly: this is one
identity.** `017` Lapis is a contaminated second case (archive base card 1537/854/540 vs an
awakened Lv.30 Reddit reading 4501/2382/1789 — base vs awakened is not a clean gear
comparison) and is **not** counted.

**Consequence for this table.** The archive `r` / `s` are treated as a transferable *shape*.
The archive **numerals are not**, for two independent reasons: level is unknown, and the
only gear state that can be separated (`051`) shows gear is a **magnitude** multiplier
(x1.716 on HP) which the replica has no way to express, because all six published
references ship `equipment: []`.

### 2.4 Tolerance — defined, justified, and swept

**Primary tolerance: +/-15 %** absolute deviation on **both** `r` and `s`, **and** exact
agreement on the native `role` and `attr` enums.

Justification: the 051 intra-hero gear-state check gives an observed noise floor of
**2.20 %** on `r`, so +/-15 % is roughly 7x that floor; and the four role bands are
separated by a **0.917 to 1.382** gap (**51 %**), so +/-15 % cannot cross a role boundary.

Because that choice is a judgement call, the whole sweep is given (§6.1) so a reader can
re-pick the threshold.

### 2.5 Per-role archetype bands, measured this pass

`A` = S1 archive (n=62), `E` = S2 `EVCB` rows (n=37), `P` = pooled (n=99).

| role | n | `r` = ATK/DEF — min…max (median) | `s` = (ATK+DEF)/HP — min…max (median) |
|---|---:|---|---|
| **Defense** | A 17 / E 8 / P 25 | A **0.659…0.917** (0.765) · E 0.800…1.235 (0.913) · P 0.659…1.235 (0.831) | A **0.842…1.217** (0.925) · E 0.380…1.000 (0.847) · P 0.380…1.217 (0.909) |
| **Support** | A 13 / E 12 / P 25 | A **0.923…1.140** (**1.000**) · E 0.833…1.143 (**1.000**) · P 0.833…1.143 (**1.000**) | A 0.891…0.943 (0.909) · E 0.792…0.957 (0.909) · P 0.792…0.957 (0.909) |
| **Offense** | A 20 / E 11 / P 31 | A **1.170…1.581** (1.340) · E 1.077…1.333 (1.250) · P 1.077…1.581 (1.273) | A 0.893…0.969 (0.919) · E 0.540…1.050 (0.963) · P 0.540…1.050 (0.927) |
| **Bomber** | A 12 / E 6 / P 18 | A **1.382…1.748** (1.545) · E 1.200…2.167 (1.479) · P 1.200…2.167 (1.545) | A **1.124…1.164** (1.137) · E 0.957…1.118 (1.050) · P 0.957…1.164 (1.125) |

**Band-separation verdicts — three of the four separations hold, one does not:**

| pair | archive-only | pooled | verdict |
|---|---|---|---|
| Bomber vs **Defense** | 1.382 vs 0.917 — **no overlap** | 1.200 vs 1.235 — **overlaps by 0.035** | holds in the high-resolution source; **weakens** when the coarse Episode family is pooled |
| Support vs **Defense** | 1.140 vs 0.917 — no overlap (0.6 % margin) | 1.143 vs 1.235 — overlaps | holds, but by a thin margin |
| **Offense vs Support** | 1.170 vs 1.140 — no overlap | 1.077 vs 1.143 — overlaps | holds archive-only |
| **Offense vs Bomber** | **1.382…1.581 shared** | 1.200…1.581 shared | **does NOT separate in either source** |

=> **The brief's "Bomber 1.38–1.75 vs Defender 0.66–0.92 do not overlap" is confirmed for
the archive source. It is *not* a clean four-way separation: Offense and Bomber overlap
across 1.382–1.581, and Offense / Bomber must be told apart by `s`
(0.893–0.969 vs 1.124–1.164) rather than by `r`.**

**Secondary-field bands (archive, pooled n=62)** — for completeness; the 13-field tuples
in §4 carry these per hero:

| field | archive ladder | by role |
|---|---|---|
| `speed` | **6 / 7 / 8** (3 values) | Defense 6–7, Support 7, Offense 7–8, Bomber 7 |
| `crit` | **0 / 14 / 20 / 30 / 33** (5 values) | Offense 30–33, all others 0–20 |
| `crit_damage` | **50 / 180 / 185 / 200 / 205** | Offense 200–205, others 180–185 |
| `penetration` | **0 / 1** | `1` only on `010`, `048`, `009` |
| `block` | **0 / 14 / 20 / 30 / 33 / 36** | **Defense 0–36** (33 on 10 of 17), Offense 14–30, Support / Bomber 14 |
| `block_damage_reduction` | **30 / 40 / 42 / 45 / 50 / 52 / 55** | **Defense 30–55** |
| `element_enhance == element_resistance` | **60 / 62** rows | 29 rows 5/5, 28 rows 0/0, 3 rows 2/2; only 2 rows break the equality (0/10) |
| `hp_regen` | 32…51, **17 distinct** | Bomber 32–39 (lowest), Offense / Defense highest |
| distinct `hp` | **20** | HP is banded / quantized |

The replica ships `spd 100 / crt_chance 5 / crt_dmg 150 / block 0 / block_dec_dmg 0 /
attr_enhance 0 / attr_resist 0` for **all six** heroes — i.e. every one of these
role-identifying ladders is currently flattened.

### 2.6 Negative findings that constrain how the table may be used

1. **Element is not an input to the core three — re-confirmed on the variant pairs, which
   is the strongest form of the test.** Of the 62 archive rows, **12 `(hp,atk,def)` tuples
   are shared by two heroes, leaving only 50 distinct tuples**. **All 12 duplicate pairs are
   same-role**, and in **10 of 12** the two members have **different elements**:
   `007`/`014` Bomber 1277/908/576 (Fire / Ice) · `026`/`004` Support 1467/679/679
   (Lightning / Fire) · `039`/`031` Bomber 1521/1021/689 · `059`/`001` Bomber 1521/1058/653 ·
   `019`/`006` Offense 1537/817/576 (Lightning / Fire) · `022`/`030` Support 1584/718/718
   (Ice / Lightning) · `005`/`009` Defense 1624/628/893 (Ice / Lightning) · `024`/`034`
   Defense 1624/682/821 (Lightning / Ice) · `032`/`002` Offense 1624/839/682 (Ice / Lightning) ·
   `060`/`035` Support 1710/828/726 · `048`/`027` Defense 1750/689/901 (Ice / Fire) ·
   `037`/`040` Offense 1750/883/755 (Ice / Lightning).
   Two of the twelve are same-element cross-character cell collisions (`031`/`039` both
   Bomber / Lightning / star 3; `035`/`060` both Support / Fire / star 3), and `059`/`001` is
   the **same character** (Lantern + Halloween costume) reading **identically** — a direct
   determinism control: *same identity + same rarity gives an identical row*.
2. **Rarity is the magnitude axis, and it acts as a near-uniform scalar.** Pooled archive
   medians by draw rarity: HP **1502 / 1624 / 1750 / 1955** and `(ATK+DEF)`
   **1393 / 1503 / 1632 / 1791** for stars 1–4 — both rise x1.30 / x1.29. `s` is essentially
   flat across rarity (0.926 / 0.925 / 0.936 / 0.911), which is the arithmetic signature of
   a scalar knob. Character-level confirmation: `021` Rebecca star 2 (1624/893/580) to
   `038` Rebecca (Christmas) star 3 (1790/992/668), and `013` Denali star 2 (1584/755/682) to
   `060` Denali (Halloween) star 3 (1710/828/726).
3. **The `EVCB` family is a per-role TEMPLATE, not a per-hero measurement.** 37 rows
   collapse to **25 distinct `(atk,def)` pairs** and **13 distinct HP values**, and the
   values are round (`1000/1000` x4, `1100/1000` x3, `1000/900` x3). Its per-hero
   resolution is far below the archive's. It is usable as an **identity and
   role / archetype corroboration**, not as a per-hero value.
4. **The `CB` family is unusable as a shape source — quantified.** Among the ~~19~~
   **18** heroes whose only Episode rows are `CB*` *and* which appear in the S1 archive,
   **only 1** (`011` Hecate, `CB1101_011_1`
   2400/1000/1250, `r` 0.800, `s` 0.938) has any row inside the archive role band on both
   features; ~~**5 of 19**~~ **4 of 18** (`003`, `010`, `012`, `054`) have a row with `r` in band but `s` out. The rest are the
   glass-cannon script shape — `001` `CB1101_001_1` = 3700/3800/240 (`r` **15.83**),
   `043` `CB1101_043_1` (`r` **12.22**), ~~`018` `CB1102_018` (`r` **12.61**)~~ **`018` `CB0701_018_1` (`r` **4.17**)**, `030`
   `CB1001_030_1` (`r` **13.33**). The `CB*` family is pinned near DEF 210–290 regardless
   of HP, which is a script artifact. => **`CB*` rows contribute identity, never shape.**

   > **CORRECTION 2026-10-06 — two corrections, conclusion unchanged.** (a) The
   > denominator `19` was the `res_id`-namespace count of `CB*`-only heroes that are
   > also in S1; the `hunter`-only count is **18**. `19` is reproducible *only* with
   > the un-filtered `C*` pool, and the extra hero is `006` (Sylvester), whose sole
   > Episode row is the **monster-typed** `CB1102_006`. (b) **`018`'s cited row
   > `CB1102_018` is a MONSTER-placed row** (`type: "monster"` in
   > `EPISODE_COMBAT_CB1102.json`, 4500/2900/230, `r` 12.61) and must not be cited as
   > hero evidence; `018`'s only *hunter* row is `CB0701_018_1` at 3100/1000/240,
   > `r` **4.167**. The point is unaffected — the row is still far out of band, just
   > for a different reason. The headline conclusion (**`CB*` contributes identity,
   > never shape**) holds on the strict filter: 18 heroes, still only `011` in band on
   > both features. **[UNRESOLVED]** the original `5 of 19` could not be reproduced
   > under any of the four filter/`s`-band variants tried (all yield 4); the replaced
   > count 4 is measured, but why the original said 5 is not established.
5. **`EVCB` vs archive is a near-uniform magnitude offset, on 22 of 25 heroes.** Taking the
   first `EVCB` row per hero and dividing its HP by the archive HP: median **1.404**,
   range 1.053–2.857 (n=25). Dropping the three rows at or above 1.6 (`023` 2.857, `029`'s
   second `EVCB` row 2.793, `013` 1.894) leaves **median 1.375, range 1.053–1.538 (n=22)** —
   a 1.46x window. This is the `P6` scale hypothesis, re-measured. It is **still a
   hypothesis**: it assumes `EVCB` and archive are the same measurement at two levels, and
   `023` breaks it outright.

---

## 3. Coverage arithmetic — the explicit answer

Denominator **113 real catalog characters** (`coverage.md`; 121 TSV rows minus 8
trainer/ticket placeholder rows). Three of the union IDs below are **costume rows**, not
distinct characters, per `card-catalogue.tsv` `owner_card_id`: `026` -> `004`,
`034` -> `024`, `085` -> `070`.

| Quantity | Raw IDs | Real characters | % of 113 |
|---|---:|---:|---:|
| S1 archive numeric rows | 62 | **60** (minus `026`, `034`) | 53.1 % |
| S2 Episode hero identities | 55 | **54** (minus `085`) | 47.8 % |
| In **BOTH** sources | 44 | **44** | 38.9 % |
| In **EITHER** source (**the headline**) | 73 | **70** | **61.9 %** |
| In neither source | — | **43** | 38.1 % |

| Shape usability (real characters) | Count |
|---|---:|
| In both sources, **with a usable Episode shape row** (`EVCB`) | **25** |
| …of those, role + element enums **both** agree | **24 / 25** (sole exception `059`, element: Episode `attr 3` Lightning vs archive Fire, on a variant `res_id`) |
| …of those, Episode `r` falls **inside the archive role band** | **16 / 25** |
| …of those, **SHAPE-AGREE at +/-15 %** with enums matching | **13 / 25** |
| …of those, shape-agree at +/-20 % / +/-25 % / +/-30 % | 20 / 22 / 23 |

> **Answer to "how many could be filled from EITHER source": 70 of 113 real characters
> (61.9 %).** Identity plus HP/ATK/DEF exists for 70 heroes where today it exists for 0.
>
> **Answer to "how many from BOTH with agreement": 44 real characters carry a row in both
> sources; of the 25 whose Episode row is a usable shape row, 13 agree within +/-15 % (and
> 24/25 agree on role + element identity).** At +/-20 % the figure is 20/25.

**These are *shape* counts, not base-stat counts. `coverage.md` remains 1/113.**

---

## 4. THE CANDIDATE TABLE

**Legend.** `ARCHIVE 13` = `combat_power / hp / atk / def / speed / crit / crit_damage /
penetration / block / block_damage_reduction / element_enhance / element_resistance /
hp_regen` (S1 column order). `EPISODE 13` = `hp / atk / def / spd / crt_chance / crt_dmg /
penetration / attr_enhance / block_chance / block_dec_dmg / attr_resist / hp_regen / rank`
(S2 `stat` key order). `band(A)` = the hero's role's **archive** `r` band (§2.5).
`in A-band?` = does the Episode `r` land inside that archive band. `r / s` = the two
scale-free features of §2.1. `agree 15%` = absolute `|dr| / |ds|` in percent, or the verdict.

**Every row is IMPURE and era-tagged (S1 = 2019-10 to 12 community; S2 = 2.8.0.1 / 2021
shipped). No row is a base stat.**

### 4.1 Block A — 62 heroes with an S1 archive row

| id | name | role | band(A) | elem | star | ARCHIVE 13-field | r / s | EPISODE row | in A-band? | EPISODE 13-field | r / s | agree 15% | conf |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `001` | Lantern | Bomber | 1.382-1.748 | Fire | 3 | `8359/1521/1058/653/7/14/180/0/14/42/0/0/38` | 1.620 / 1.125 | 2 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `002` | Mowgli | Offense | 1.170-1.581 | Lightning | 2 | `8587/1624/839/682/8/33/200/0/14/42/0/0/41` | 1.230 / 0.937 | none | n/a | - | - | - | **C** |
| `003` | Nene | Defense | 0.659-0.917 | Ice | 3 | `9371/1750/726/864/7/14/180/0/33/50/0/0/48` | 0.840 / 0.909 | 3 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `004` | Tyltyl | Support | 0.923-1.140 | Fire | 1 | `6664/1467/679/679/7/14/180/0/14/42/0/0/37` | 1.000 / 0.926 | `EVCB0201_004` EVCB | Y | `2000/1000/900/7.00/14.00/200/0.00/5/14.00/40/5/45/5` | 1.111 / 0.950 | **AGREE** 11.1 / 2.6 | **A2** |
| `005` | Gerard | Defense | 0.659-0.917 | Ice | 2 | `8567/1624/628/893/7/14/180/0/33/52/0/0/41` | 0.703 / 0.937 | `EVCB0201_005` EVCB | Y | `2600/1200/1400/7.00/14.00/204/0.00/0/33.00/50/10/50/5` | 0.857 / 1.000 | drift 21.9 / 6.8 | **A1** |
| `006` | Sylvester | Offense | 1.170-1.581 | Fire | 1 | `7558/1537/817/576/8/33/200/0/14/42/0/0/38` | 1.418 / 0.906 | 1 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `007` | Metis | Bomber | 1.382-1.748 | Fire | 1 | `6624/1277/908/576/7/14/180/0/14/40/0/0/36` | 1.576 / 1.162 | 1 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `008` | Akasha | Support | 0.923-1.140 | Lightning | 3 | `8081/1710/762/762/7/14/185/0/14/40/0/0/43` | 1.000 / 0.891 | `EVCB0301_008B` EVCB | N | `2400/1000/1100/7.00/14.00/200/0.00/5/14.00/40/5/45/5` | 0.909 / 0.875 | **AGREE** 9.1 / 1.8 | **A2** |
| `009` | Captain | Defense | 0.659-0.917 | Lightning | 1 | `8567/1624/628/893/7/14/180/1/33/52/0/0/41` | 0.703 / 0.937 | `EVCB0201_009` EVCB | Y | `2400/1000/1100/7.00/14.00/204/20.00/0/33.00/50/10/50/5` | 0.909 / 0.875 | drift 29.3 / 6.6 | **A1** |
| `010` | Vincent | Offense | 1.170-1.581 | Lightning | 4 | `11252/1923/1032/718/8/30/200/1/30/42/0/0/48` | 1.437 / 0.910 | 9 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `011` | Hecate | Defense | 0.659-0.917 | Fire | 1 | `7620/1537/576/817/7/14/180/0/33/52/0/0/38` | 0.705 / 0.906 | 3 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `012` | Karl Steiner | Offense | 1.170-1.581 | Lightning | 3 | `9851/1750/1007/689/7/33/205/0/14/40/0/0/44` | 1.462 / 0.969 | 5 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `013` | Denali | Support | 0.923-1.140 | Fire | 2 | `7293/1584/755/682/7/14/180/0/14/40/2/2/40` | 1.107 / 0.907 | `EVCB0201_013` EVCB | Y | `3000/1200/1300/7.00/14.00/210/0.00/5/14.00/40/5/45/5` | 0.923 / 0.833 | drift 16.6 / 8.1 | **A1** |
| `014` | Locke | Bomber | 1.382-1.748 | Ice | 1 | `6653/1277/908/576/7/14/180/0/14/42/0/0/32` | 1.576 / 1.162 | 2 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `015` | Levi | Bomber | 1.382-1.748 | Ice | 2 | `7370/1395/1014/580/7/14/185/0/14/40/0/0/35` | 1.748 / 1.143 | none | n/a | - | - | - | **C** |
| `016` | Bruce Bang | Support | 0.923-1.140 | Ice | 1 | `6716/1467/660/715/7/14/180/0/14/40/2/2/37` | 0.923 / 0.937 | 2 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `017` | Lapis | Offense | 1.170-1.581 | Ice | 1 | `7495/1537/854/540/8/33/205/0/14/40/0/0/38` | 1.581 / 0.907 | `EVCB0301_017` EVCB | Y | `2100/1200/950/9/33.00/200/0.00/5/20.00/40/5/45/5` | 1.263 / 1.024 | drift 20.1 / 12.9 | **A1** |
| `018` | Robin | Defense | 0.659-0.917 | Ice | 1 | `7716/1537/642/751/7/14/180/0/33/52/0/0/38` | 0.855 / 0.906 | 2 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `019` | Balian | Offense | 1.170-1.581 | Lightning | 1 | `7574/1537/817/576/8/33/205/0/14/40/0/0/38` | 1.418 / 0.906 | `EVCB0301_019` EVCB | Y | `2200/1200/950/8/33.00/200/0.00/5/20.00/40/5/45/5` | 1.263 / 0.977 | **AGREE** 10.9 / 7.8 | **A2** |
| `020` | Sienna | Bomber | 1.382-1.748 | Lightning | 1 | `6565/1277/944/540/7/14/180/0/14/42/0/0/32` | 1.748 / 1.162 | 1 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `021` | Rebecca | Offense | 1.170-1.581 | Fire | 2 | `8122/1624/893/580/8/33/200/0/14/40/0/0/45` | 1.540 / 0.907 | 2 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `022` | Sunny | Support | 0.923-1.140 | Ice | 2 | `7329/1584/718/718/7/14/180/0/14/42/0/0/40` | 1.000 / 0.907 | none | n/a | - | - | - | **C** |
| `023` | Hermes | Offense | 1.170-1.581 | Fire | 3 | `9177/1750/937/653/8/33/200/0/14/40/2/2/44` | 1.435 / 0.909 | `EVCB0201_023` EVCB | N | `5000/1400/1300/7.00/33.00/224/0.00/5/14.00/40/5/45/5` | 1.077 / 0.540 | drift 24.9 / 40.6 | **A1** |
| `024` | Riko | Defense | 0.659-0.917 | Lightning | 2 | `8552/1624/682/821/7/14/185/0/33/50/0/0/41` | 0.831 / 0.925 | 1 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `025` | Teddy Bomber | Bomber | 1.382-1.748 | Fire | 2 | `7656/1395/978/646/7/14/180/0/14/42/0/0/35` | 1.514 / 1.164 | none | n/a | - | - | - | **C** |
| `026` | *(costume of 004)* | Support | 0.923-1.140 | Lightning | 1 | `6664/1467/679/679/7/14/180/0/14/42/0/0/37` | 1.000 / 0.926 | none | n/a | - | - | - | **C** |
| `027` | Athena | Defense | 0.659-0.917 | Fire | 3 | `9322/1750/689/901/7/14/180/0/33/50/5/5/48` | 0.765 / 0.909 | `EVCB0201_027B` EVCB | Y | `2500/1100/1200/7.00/14.00/204/0.00/0/70.00/50/10/50/5` | 0.917 / 0.920 | drift 19.9 / 1.3 | **A1** |
| `028` | Octavia | Offense | 1.170-1.581 | Ice | 3 | `9304/1750/901/689/8/33/205/0/14/40/5/5/44` | 1.308 / 0.909 | `EVCB0201_028B` EVCB | Y | `2000/1200/900/8.00/33.00/200/0.00/25/14.00/40/5/45/5` | 1.333 / 1.050 | drift 2.0 / 15.6 | **A1** |
| `029` | Kain | Defense | 0.659-0.917 | Lightning | 3 | `10229/1790/689/1007/7/14/185/0/36/55/5/5/45` | 0.684 / 0.947 | `EVCB0101_029A` EVCB | Y | `2200/800/1000/7/14.00/208/0.00/0/36.00/55/10/45/5` | 0.800 / 0.818 | drift 16.9 / 13.6 | **A1** |
| `030` | Acerola | Support | 0.923-1.140 | Lightning | 2 | `7321/1584/718/718/7/14/185/0/14/40/0/0/40` | 1.000 / 0.907 | 1 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `031` | Diana | Bomber | 1.382-1.748 | Lightning | 3 | `8401/1521/1021/689/7/14/180/0/14/40/5/5/38` | 1.482 / 1.124 | none | n/a | - | - | - | **C** |
| `032` | Scar | Offense | 1.170-1.581 | Ice | 2 | `8550/1624/839/682/8/33/200/0/14/40/0/0/45` | 1.230 / 0.937 | `EVCB0201_032` EVCB | Y | `2300/1300/1100/8.00/33.00/224/0.00/5/70.00/40/5/45/5` | 1.182 / 1.043 | **AGREE** 3.9 / 11.4 | **A2** |
| `033` | Patrone | Bomber | 1.382-1.748 | Ice | 3 | `8580/1521/1003/726/7/14/185/0/14/40/5/5/38` | 1.382 / 1.137 | none | n/a | - | - | - | **C** |
| `034` | *(costume of 024)* | Defense | 0.659-0.917 | Ice | 2 | `8552/1624/682/821/7/14/185/0/33/50/0/0/41` | 0.831 / 0.925 | `EVCB0103_034` EVCB | Y | `2000/850/1000/7/14.00/200/0.00/0/33.00/40/10/45/5` | 0.850 / 0.925 | **AGREE** 2.3 / 0.1 | **A2** |
| `035` | Joy | Support | 0.923-1.140 | Fire | 3 | `8236/1710/828/726/7/14/180/0/14/42/5/5/43` | 1.140 / 0.909 | none | n/a | - | - | - | **C** |
| `036` | Bear | Defense | 0.659-0.917 | Lightning | 3 | `10011/1923/755/864/7/14/180/0/33/50/5/5/32` | 0.874 / 0.842 | `EVCB0201_036B` EVCB | N | `2700/1000/1000/7.00/14.00/205/0.00/0/33.00/50/10/50/5` | 1.000 / 0.741 | **AGREE** 14.4 / 12.0 | **A2** |
| `037` | Natalia | Offense | 1.170-1.581 | Ice | 3 | `9909/1750/883/755/8/33/205/0/20/40/5/5/44` | 1.170 / 0.936 | none | n/a | - | - | - | **C** |
| `038` | Rebecca (Christmas) | Offense | 1.170-1.581 | Fire | 3 | `9666/1790/992/668/8/33/200/0/14/40/5/5/48` | 1.485 / 0.927 | `EVCB0201_038` EVCB | Y | `2700/1400/1100/8.00/33.00/300/0.00/5/14.00/40/5/45/5` | 1.273 / 0.926 | **AGREE** 14.3 / 0.2 | **A2** |
| `039` | Gullveig | Bomber | 1.382-1.748 | Lightning | 3 | `8437/1521/1021/689/7/14/180/0/14/40/5/5/38` | 1.482 / 1.124 | `EVCB0201_039` EVCB | N | `2200/1200/1000/7.00/14.00/204/0.00/10/14.00/40/0/40/5` | 1.200 / 1.000 | drift 19.0 / 11.1 | **A1** |
| `040` | Bibi | Offense | 1.170-1.581 | Lightning | 3 | `9888/1750/883/755/8/33/200/0/20/42/5/5/44` | 1.170 / 0.936 | `EVCB0301_040` EVCB | N | `2400/1100/1000/8.00/33.00/200/0.00/5/15.00/40/5/45/5` | 1.100 / 0.875 | **AGREE** 5.9 / 6.5 | **A2** |
| `041` | Edward | Defense | 0.659-0.917 | Lightning | 3 | `9495/1821/718/901/7/14/180/0/30/45/5/5/46` | 0.797 / 0.889 | 2 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `042` | Santa Clauster | Offense | 1.170-1.581 | Fire | 3 | `9659/1821/937/689/8/33/200/0/14/42/5/5/44` | 1.360 / 0.893 | `EVCB0201_042` EVCB | Y | `2800/1500/1200/8.00/58.00/224/0.00/5/14.00/40/5/45/5` | 1.250 / 0.964 | **AGREE** 8.1 / 8.0 | **A2** |
| `043` | Papillon | Defense | 0.659-0.917 | Ice | 3 | `8261/1606/726/792/7/14/185/0/33/30/5/5/44` | 0.917 / 0.945 | 1 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `044` | Heidi | Offense | 1.170-1.581 | Fire | 3 | `9764/1750/952/689/8/33/200/0/20/40/5/5/44` | 1.382 / 0.938 | none | n/a | - | - | - | **C** |
| `045` | Yuri | Offense | 1.170-1.581 | Ice | 3 | `9635/1750/937/718/8/33/200/0/14/40/5/5/44` | 1.305 / 0.946 | none | n/a | - | - | - | **C** |
| `046` | Harley | Defense | 0.659-0.917 | Ice | 4 | `11534/2033/755/1036/7/20/180/0/33/50/5/5/51` | 0.729 / 0.881 | 1 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `047` | Lily & Lyla | Offense | 1.170-1.581 | Fire | 4 | `10679/1923/996/755/8/33/200/0/14/40/5/5/48` | 1.319 / 0.911 | none | n/a | - | - | - | **C** |
| `048` | Dumble | Defense | 0.659-0.917 | Ice | 3 | `9322/1750/689/901/6/14/180/1/33/50/5/5/44` | 0.765 / 0.909 | none | n/a | - | - | - | **C** |
| `049` | Bright | Support | 0.923-1.140 | Fire | 3 | `8403/1710/828/755/7/14/180/0/14/42/5/5/43` | 1.097 / 0.926 | `EVCB0201_049B` EVCB | Y | `1800/900/800/7.00/14.00/210/0.00/5/14.00/40/5/45/5` | 1.125 / 0.944 | **AGREE** 2.6 / 2.0 | **A2** |
| `050` | Therapy | Support | 0.923-1.140 | Ice | 3 | `8428/1710/825/762/7/14/180/0/14/42/5/5/43` | 1.083 / 0.928 | none | n/a | - | - | - | **C** |
| `051` | Beckhen | Offense | 1.170-1.581 | Ice | 3 | `8709/1678/864/660/8/33/200/0/14/42/5/5/42` | 1.309 / 0.908 | `EVCB0201_051` EVCB | N | `2400/1100/1000/8.00/33.00/224/0.00/5/14.00/40/5/45/5` | 1.100 / 0.875 | drift 16.0 / 3.7 | **A1** |
| `052` | Windblade | Offense | 1.170-1.581 | Lightning | 4 | `11504/1955/992/835/8/33/205/0/14/45/5/5/49` | 1.188 / 0.935 | 1 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `053` | Calibur | Defense | 0.659-0.917 | Fire | 3 | `10162/1750/846/1284/7/0/50/0/0/50/5/5/48` | 0.659 / 1.217 | none | n/a | - | - | - | **C** |
| `054` | Dino | Bomber | 1.382-1.748 | Ice | 3 | `8921/1560/1029/744/7/14/180/0/14/42/5/5/39` | 1.383 / 1.137 | 4 rows, all `CB*` | n/a | - | - | identity only | **B** |
| `055` | Apollon | Bomber | 1.382-1.748 | Fire | 3 | `8767/1560/1054/708/7/14/180/0/14/40/5/5/43` | 1.489 / 1.129 | `EVCB0201_055B` EVCB | N | `2000/1200/900/7.00/14.00/204/0.00/10/14.00/40/0/40/5` | 1.333 / 1.050 | **AGREE** 10.4 / 7.0 | **A2** |
| `057` | Pansy | Support | 0.923-1.140 | Ice | 3 | `8394/1742/762/806/7/14/185/0/14/40/5/5/44` | 0.945 / 0.900 | `EVCB0301_C057` EVCB | Y | `2400/1000/900/7/30.00/200/0.00/5/30.00/30/5/40/5` | 1.111 / 0.792 | drift 17.5 / 12.0 | **A1** |
| `058` | Crocus | Support | 0.923-1.140 | Lightning | 3 | `8535/1710/806/806/7/14/180/0/14/40/5/5/47` | 1.000 / 0.943 | `EVCB0301_C058B` EVCB | Y | `2300/1100/1100/7.00/14.00/200/0.00/5/14.00/40/5/45/5` | 1.000 / 0.957 | **AGREE** 0.0 / 1.5 | **A2** |
| `059` | Lantern (Halloween) | Bomber | 1.382-1.748 | Fire | 3 | `8359/1521/1058/653/7/14/180/0/14/42/0/0/38` | 1.620 / 1.125 | `EVCB0105_059` EVCB | N | `1700/1300/600/7/14.00/203/0.00/10/14.00/42/0/40/5` | 2.167 / 1.118 | **ENUM-MISMATCH** role Bomber/Bomber, elem Lightning/Fire | **A0** |
| `060` | Denali (Halloween) | Support | 0.923-1.140 | Fire | 3 | `8200/1710/828/726/7/14/180/0/14/40/0/0/43` | 1.140 / 0.909 | `EVCB0105_060` EVCB | N | `1800/800/700/7/14.00/203/0.00/6/14.00/40/6/45/5` | 1.143 / 0.833 | **AGREE** 0.2 / 8.3 | **A2** |
| `061` | Chichi | Offense | 1.170-1.581 | Lightning | 3 | `10148/1821/937/798/8/33/200/0/14/40/5/5/51` | 1.174 / 0.953 | none | n/a | - | - | - | **C** |
| `062` | Juno | Defense | 0.659-0.917 | Fire | 3 | `11556/1968/743/1125/7/14/180/0/33/52/0/10/46` | 0.660 / 0.949 | none | n/a | - | - | - | **C** |
| `063` | Erise | Defense | 0.659-0.917 | Lightning | 4 | `12725/2019/933/1070/7/14/180/0/33/52/0/10/48` | 0.872 / 0.992 | none | n/a | - | - | - | **C** |

### 4.2 Block B — 11 heroes with an S2 Episode row only (no S1 archive row)

| id | name | role (enum) | elem (enum) | family | row | EPISODE 13-field | r / s | in archive band? | pooled band | conf |
|---|---|---|---|---|---|---|---|---|---|---|
| `082` | Mary (Christmas) | Offense (1) | Lightning (3) | EVCB | `EVCB0201_082` | `2700/1450/1150/8.00/33.00/240/0.00/5/20.00/50/99/65/5` | 1.261 / 0.963 | Y | 1.077-1.581 | **D2** |
| `080` | Westfield | Support (4) | Lightning (3) | EVCB | `EVCB0201_080` | `2300/1000/1200/7.00/14.00/204/0.00/0/33.00/50/10/50/5` | 0.833 / 0.957 | N | 0.833-1.143 | **D2** |
| `072` | Audrey | Bomber (3) | Lightning (3) | EVCB x2 | `EVCB0103_072A` | `1800/1200/700/7/28.00/200/0.00/10/28.00/40/0/45/5` | 1.714 / 1.056 | Y | 1.200-2.167 | **D2** |
| `070` | Alia | Support (4) | Lightning (3) | EVCB | `EVCB0301_070` | `2000/1000/900/7.00/14.00/200/0.00/5/14.00/40/5/45/5` | 1.111 / 0.950 | Y | 0.833-1.143 | **D2** |
| `085` | *(costume of 070)* | Support (4) | Fire (1) | EVCB | `EVCB0301_C085` | `2200/1000/1000/7.00/14.00/200/0.00/5/14.00/40/5/45/5` | 1.000 / 0.909 | Y | 0.833-1.143 | **D2** |
| `069` | Celine | Support (4) | Ice (2) | EVCB | `EVCB0201_069A` | `2600/1100/1200/7.00/14.00/210/0.00/5/14.00/40/5/45/5` | 0.917 / 0.885 | N | 0.833-1.143 | **D2** |
| `078` | Teresa (Halloween) | Support (4) | Ice (2) | EVCB | `EVCB0101_078` | `2200/1000/1000/7/14.00/208/0.00/5/14.00/40/5/48/5` | 1.000 / 0.909 | Y | 0.833-1.143 | **D2** |
| `071` | Anemone | Offense (1) | Fire (1) | CB* only (1) | `CB1502_071` median pick | script-shaped, see 2.6.4 | 8.214 / 0.184 | N | 1.077-1.581 | **D1** |
| `056` | Genovia | Offense (1) | Ice (2) | CB* only (3) | `CB1402_C056` median pick | script-shaped, see 2.6.4 | 1.600 / 0.867 | N | 1.077-1.581 | **D1** |
| `064` | Geranium | Bomber (3) | Lightning (3) | CB* only (2) | `CB1602_C064` median pick | script-shaped, see 2.6.4 | 1.357 / 1.179 | N | 1.200-2.167 | **D1** |
| `068` | Selene | Bomber (3) | Ice (2) | EVCB | `EVCB0301_C068A` | `2000/1300/800/7.00/14.00/200/0/10/14.00/40/0/45/5` | 1.625 / 1.050 | Y | 1.200-2.167 | **D2** |

**Two reading caveats on the tables above.**

1. **`in A-band?` and `agree 15%` are different tests and can disagree at a band edge.**
   `036` (AGREE 14.4 %, `in A-band? N`), `055` (AGREE 10.4 %, `N`) and `060` (AGREE 0.2 %,
   `N`, by **0.003**) all sit within 15 % of their archive row yet just outside the archive
   band edge, because a band-edge test and a relative-deviation test are not the same
   predicate. Conversely `005` is `in A-band? Y` yet drifts 21.9 % from its own archive row.
   Neither column supersedes the other.
2. **`082` carries `attr_resist 99`**, an apparent sentinel rather than a resistance value
   (`hero-stat-divergence-2026-10-05.md` §3a). Its element cannot be trusted until a rule
   exists. `072` and `068` also carry `block_chance 28.00` / `crt_chance 28.00` values that
   sit off both recovered ladders.

---

## 5. Confidence roll-up

| Tier | Definition — *exactly which sources attest it* | Real chars | Rows |
|---|---|---:|---|
| **A2** | S1 archive row **+** S2 `EVCB` row; native `role` **and** `attr` enums both match; `\|dr\| <= 15 %` **and** `\|ds\| <= 15 %` — **two-source shape confirmation** | **13** | `004 008 019 032 034 036 038 040 042 049 055 058 060` |
| **A1** | S1 archive row **+** S2 `EVCB` row; enums match but shape drifts > 15 % — **two-source identity, shape contested** | **11** | `005 009 013 017 023 027 028 029 039 051 057` |
| **A0** | S1 archive row **+** S2 `EVCB` row; **enum mismatch** — treat element as unreliable for this hero | **1** | `059` |
| **B** | S1 archive row **+** S2 `CB*` rows only — identity attested twice, **shape attested once** (§2.6.4) | **19** | `001 003 006 007 010 011 012 014 016 018 020 021 024 030 041 043 046 052 054` |
| **C** | S1 archive row only — **single community source, unknown level and gear** | **18** | `002 015 022 025 026* 031 033 035 037 044 045 047 048 050 053 061 062 063` |
| **D2** | S2 `EVCB` row only — **single shipped source, but the gear-free-template family** | **7** | `068 069 070 072 078 080 082` |
| **D1** | S2 `CB*` rows only — **single shipped source, script-shaped; §2.6.4 says unusable as shape** | **3** | `056 064 071` |

Tier rows sum: 13 + 11 + 1 + 19 + 18 = **62** (Block A) and 7 + 3 = **10** (Block B real
characters). Two bookkeeping notes so the counts reconcile against the tables:

- `*` `026` is a costume row of `004` and `034` is a costume row of `024`. Both appear in
  Block A and are counted in the raw 62, but they are excluded from the 70-character
  figure — so Block A's 62 rows are 60 real characters, and the `C` tier's 18 rows are 17
  real characters.
- Block B shows **8** `D2` rows but the tier is counted as **7** real characters, because
  `085` (a costume of `070`) is present in the table and excluded from the count.

**Only 13 of 113 real characters (11.5 %) have two independent sources agreeing on the
shape.** That is the honest ceiling of what these two sources can certify, and it is why
§6's substitution set is small.

---

## 6. The minimal substitution set, and what it deliberately does not decide

### 6.1 Tolerance sweep (so the threshold can be re-picked)

Absolute deviation, on the **25** heroes with both an archive row and an `EVCB` row:

| tolerance | `\|dr\|` within | `\|ds\|` within | **both** | **both + enums match** |
|---:|---:|---:|---:|---:|
| +/-10 % | 9 / 25 | 17 / 25 | 7 / 25 | **7** |
| **+/-15 % (primary)** | 14 / 25 | 23 / 25 | 13 / 25 | **13** |
| +/-20 % | 20 / 25 | 24 / 25 | 20 / 25 | **20** |
| +/-25 % | 23 / 25 | 24 / 25 | 22 / 25 | **22** |
| +/-30 % | 24 / 25 | 24 / 25 | 23 / 25 | **23** |

`|dr|` median **14.3 %** (max 33.7 %, `059`); `|ds|` median **7.0 %** (max 40.6 %, `023`).
`s` is the better-behaved feature — consistent with §2.2 and with `EVCB` HP being a
near-uniform x1.375 offset while its ATK/DEF are authored on round numbers (§2.6.3).

> **Process note, kept because the project has been bitten by this class of error.** My
> first two implementations of this sweep computed `Abs(ratioE)/ratioA - 1`, which is a
> **signed** quantity, so every negative drift passed the tolerance test unconditionally
> and the sweep reported 14/18/22-of-25 instead of 7/13/20. The per-hero verdict list was
> unaffected (it wrapped the whole expression), which is why the discrepancy surfaced only
> when the two passes were cross-checked against each other. The numbers above are the
> corrected ones.

### 6.2 Minimal substitution set — **6 rows**, using **only** the two evidence sources

The defect is that four of six published heroes share one row. The minimum that makes
per-hero balance **exist** is therefore **one row per published hero**, i.e. **6 rows**,
filled entirely from S1 (all six have an archive row; `004` and `005` additionally have an
`EVCB` row).

The normalization below is **HP-neutral by construction**: each hero's archive
`ATK/HP` and `DEF/HP` are applied to the replica's **existing** `hp = 1000`, so the
substitution changes **ATK and DEF only** and leaves HP untouched. This keeps the decision
independent of the coupled monster-HP question (`O2` in the defect document), which is
progression-visible and therefore explicitly the owner's call.

| id | name | role | elem | star | S1 raw | ATK/HP | DEF/HP | **candidate @ hp 1000** | `r` | archive role band | in band | S2 cross-check |
|---|---|---|---|---:|---|---:|---:|---|---:|---|:--:|---|
| `001` | Lantern | Bomber | Fire | 3 | 1521/1058/653 | 0.6956 | 0.4293 | **1000 / 696 / 429** | **1.622** | 1.382–1.748 | **IN** | `CB*` only — shape not attested (`r` 15.83) |
| `002` | Mowgli | Offense | Lightning | 2 | 1624/839/682 | 0.5166 | 0.4200 | **1000 / 517 / 420** | **1.231** | 1.170–1.581 | **IN** | **no Episode row at all** |
| `003` | Nene | Defense | Ice | 3 | 1750/726/864 | 0.4149 | 0.4937 | **1000 / 415 / 494** | **0.840** | 0.659–0.917 | **IN** | `CB*` only — `r` 0.845 in band but `s` 1.414 out |
| `004` | Tyltyl | Support | Fire | 1 | 1467/679/679 | 0.4628 | 0.4628 | **1000 / 463 / 463** | **1.000** | 0.923–1.140 | **IN** | **`EVCB0201_004` 2000/1000/900 — tier A2, AGREE (11.1 % / 2.6 %)** |
| `005` | Gerard | Defense | Ice | 2 | 1624/628/893 | 0.3867 | 0.5499 | **1000 / 387 / 550** | **0.704** | 0.659–0.917 | **IN** | `EVCB0201_005` 2600/1200/1400 — tier A1, drift 21.9 % / 6.8 %; role enum **agrees** |
| `006` | Sylvester | Offense | Fire | 1 | 1537/817/576 | 0.5316 | 0.3748 | **1000 / 532 / 375** | **1.419** | 1.170–1.581 | **IN** | `CB*` only — shape not attested (`r` 13.33) |

Properties of this 6-row set, all checked:

- **6 distinct triples from 2 today** — and all six `ATK/DEF` values are mutually distinct
  (0.704 / 0.840 / 1.000 / 1.231 / 1.419 / 1.622).
- **All six land inside their own archive role band.** The replica's current 2.000
  (`001`) and 3.000 (`002`) land outside the **entire** 62-row range.
- `s` moves from 0.150 to **1.125 / 0.937 / 0.909 / 0.926 / 0.937 / 0.906**, all inside the
  archive's `[0.842 … 1.217]` — the 5.6x error of §2.2 is removed.
- The role ordering is reproduced by the data itself, not imposed:
  Bomber 1.622 > Sylvester 1.419 > Mowgli 1.231 > Support 1.000 > Nene 0.840 > Gerard 0.704.
- **Zero state migration, zero migration risk, zero test breakage** — per the defect
  document §1.1.f / §1.1.g, no derived stat is persisted and no test pins a hero stat value.
- The `minRank` filter at `:202` is untouched, so `tests/roster.ts:28` and
  `tests/hunter-traces.ts:22` are unaffected.

### 6.3 What this substitution set explicitly does **not** decide

1. **The magnitude.** `hp = 1000` is inherited from the replica, not recovered. S1's own
   HP runs 1277–2033 at unknown level with unknown gear. Choosing an archive *numeral*
   would both break the `coverage.md` rule and be **unobservable**: per `R2` / `R5` the
   published monster `hp` (100) is the whole enemy HP budget, so a level-1 hero with
   ~1.5 k HP still one-taps. **Magnitude is `O2` / `O3`, and it is a separate,
   progression-visible owner decision.**
2. **Whether TTK should exceed one attack.** Nothing in either source recovers it. Monster
   coverage is 0/22, so any chosen monster HP pool is a fixture.
3. **`bonus.*`.** Not used and **not recommended** as a standalone change — the defect
   document's §1.5.e computes that `bonus.rank_*` pushes `ATK/HP` from 0.100 to **0.054**
   (rank 1) to **0.100** (rank 5), i.e. *away* from the recovered band, with `rank 5` an
   all-`1.0` identity row; and `bonus.bomber (0.85, 0.95, 0.95)` is strictly dominated by
   `bonus.offense (1.0, 1.0, 1.0)`.
4. **The secondary fields.** §2.5's ladders (`speed` 6/7/8, `crit` 0–33, `block` 0–36,
   `block_dec_dmg` up to 55, `attr_enhance` / `attr_resist` 5/5 on 29 of 62) are a
   **same-evidence, no-new-dimension** opportunity the 6-row set above leaves on the table.
   They are safe (the 13 archive fields align one-for-one with the native card-stat keys and
   are read as numeric strings) but they are a separate edit.
5. **Any row outside the 6.** The remaining 64 archive-backed and 10 Episode-only characters
   are recorded in §4 / §5 so a later pass can extend the table, but a substitution set
   scoped to what the replica actually publishes is the minimum that makes the defect
   disappear.

---

## 7. Limits of this file

- **Read-only.** Nothing was modified anywhere. Both source files were read only. No
  emulator, phone, APK, seed or Ghidra action.
- **Not a proposal, not a fixture, not a retune.** §6.2 is a *candidate* set for the owner.
- **Zero coverage effect.** Heroes 1/113, accessories 1/100, monsters 0/22. Every row is
  IMPURE (§1.3) and era-tagged. Nothing here may be counted as a base tuple.
- **`polluted-observations.md` was not appended**, deliberately.
- **Every derived number is reproducible** from `archived-hunter-database-2019.tsv`,
  `EPISODE_STAT_ACTORS.json`, `card-catalogue.tsv`, `coverage.md`,
  `hero-stat-divergence-2026-10-05.md`, `replica-shape-error-2026-10-05.md`,
  `stat-version-context.md` and `analysis/catalogue/stats/051.md`. The four new
  derivations in this file are: the `s` = (ATK+DEF)/HP axis and the **5.6x-below-minimum**
  replica position (§2.2); the **CB-family band-usability count** of 1-of-19 (§2.6.4); the
  **12-duplicate-tuple / 50-distinct-tuple** determinism count (§2.6.1); and the
  **`EVCB` coarseness count** of 25 distinct `(atk,def)` pairs over 37 rows (§2.6.3). All
  four should be re-run by whoever adopts them.
- **The gear-invariance proof is n = 1** (`051`). It is strong (at most 2.2 % shape change
  across a 1.716x magnitude change, with an exact cross-screen validation on the gear-removed
  side) but it is **one identity**, and `017` is a contaminated second case.
- **Absolute magnitudes remain unrecoverable.** No source prints a level.
- **The Offense / Bomber bands do not separate on `r`** in either source. Any per-hero model
  that assumes four clean `ATK/DEF` archetypes is over-reading the evidence.
- **The `EVCB` vs archive x1.375 scale is a hypothesis, not a constant** — it fails on
  `023`, on `029`'s second row, and on `013`.
- **S1 is a community source** (a Wayback capture of a third-party Japanese site), not an
  original-server trace. Its strength here is internal determinism (§2.6.1), not
  authenticity.
- **`EVCB` rows were selected by lowest `id` per hero** where a hero has several (4 heroes:
  `029`, `036`, `051`, `072`). For `051` both `EVCB` rows are byte-identical; for `029`,
  `036` and `072` the second row differs materially, so those heroes' candidate shape is
  **row-order dependent** and is flagged as `A1` or `D2` rather than `A2`.
