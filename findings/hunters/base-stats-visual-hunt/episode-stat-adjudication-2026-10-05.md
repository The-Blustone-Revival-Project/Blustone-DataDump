# Episode STAT adjudication — scripted per-appearance monster rows (2026-10-05)

**Status:** Research preparation for parent adjudication. **No coverage change
claimed.** Monster strict coverage stays **0/22**; parent decides whether any
scripted per-appearance row can ever satisfy the base-tuple definition in
`coverage.md` (source-backed HP+ATK+DEF tied to an unambiguous monster ID plus
level/rank/difficulty context).

**Sources (all local, byte-pinned):**

- `analysis/recovered-reference/EPISODE_STAT_ACTORS.json` (SHA
  `f3b8cb90372c89490467e75ed0564bfc3f8a4d094370264caa2c821b0eb13b56`),
  exported from original `R_EPISODE.jet` (SHA
  `7f4362cdf80545a6da937444094837f334c8aae4f9f791d6ff4161948d98a01e`;
  see `EPISODE_COMBAT_STAT.manifest.json`). The manifest labels this payload
  **"Episode-only actor STAT table; not ordinary hunter card-base stats"**.
- Per-appearance level/rank/hyper/attr/skill context from the shipped
  `EPISODE_COMBAT_CB*.json` / `EVCB*.json` records (same manifest, each
  "Shipped episode COMBAT record"). Thumb shape is
  `{level, rank, hyper, attr}` plus a 5-slot skill array.
- Prior lane log: `monster-fullhp-2026-10-05.md` §4 (selected rows, three
  variance examples). This file re-derives everything from disk and adds the
  full row inventory, per-appearance level context, and the catalog overlap.

**Row count reconciliation:** the file holds 152 actor rows total. 34 rows
carry a monster `res_id` (`M*`); 3 further rows carry hunter ref `C010`
(Vincent) but are placed as `type: "monster"` on the combat right side
(`CB0002/0003/0004_BOSS`). Together these are the **37 monster-like rows**
cited in §4. Four more `C010` rows are placed as `type: "hunter"` (scripted
ally Captain-side actors: `CB0302_010_1`, `CB0702_010_1`, `CB1302_C010`,
`CB1603_C010`) and are **excluded** from the monster tables below; they are
listed once in §2.7 for boundary clarity.

> **CORRECTION 2026-10-06 — the "37 monster-like rows" partition above is
> INCOMPLETE. It is not the full monster set.** Five additional `C*`-namespace
> rows are also placed `type: "monster"` in the shipped combat records, and they
> appear **nowhere** in this file:
>
> | Actor | `res_id` | `ref_id` | STAT HP/ATK/DEF @rank | thumb (in `EPISODE_COMBAT_CB1102.json`) |
> |---|---|---|---|---|
> | `CB1102_006` | `C006` | `006` | 3600/3200/240 @r5 | `level 1 / rank 5 / hyper 2 / attr 1`, right side |
> | `CB1102_008` | `C008` | `008` | 3600/2800/240 @r5 | `level 1 / rank 5 / hyper 2 / attr 3`, right side |
> | `CB1102_011` | `C011` | `011` | 4500/2800/250 @r5 | `level 1 / rank 5 / hyper 2 / attr 1`, right side |
> | `CB1102_018` | `C018` | `018` | 4500/2900/230 @r5 | `level 1 / rank 5 / hyper 2 / attr 2`, right side |
> | `CB1102_019` | `C019` | `019` | 3800/3200/240 @r5 | `level 1 / rank 5 / hyper 2 / attr 3`, right side |
>
> `CB1102` is an all-right-side, five-slot encounter; every one of its actors is
> `type: "monster"`. **Corrected exhaustive partition (2026-10-06):**
> `151` identifiable rows = `34` `M*` + **`8` monster-typed `C*`** + **`109`
> hunter-typed `C*`** (and entry index 80 is a literal `{}`). So:
>
> - **monster-like rows: 42** (was stated as 37)
> - **hero / hunter rows: 109** under the safe filter, **117** under the
>   `res_id`-starts-`C` namespace filter the rest of the corpus uses.
>
> Every §1/§2 **monster** finding that draws only on `M*` rows is unaffected
> (22 distinct `res` tokens, the 6 multi-tuple identities, the 160× `M034`
> spread, the inert secondary fields, the `2/22` catalog overlap). What changes is
> only the claim that the monster set has been *fully enumerated* — it had not: 5
> hero-art rows tuned as enemies were missing from §2, and an auditor following
> this file alone would have classified them as hero rows. Per AGENTS.md's
> strike-don't-delete rule the original 37 figure is preserved above.
> See [`episode-stat-namespace-filter-2026-10-06.md`](episode-stat-namespace-filter-2026-10-06.md).

---

## 1. Per-appearance variance analysis + catalog overlap

### 1.1 The variance finding

Six `res` identities appear under **two or more** actor rows with different
fixed HP/ATK/DEF. The values therefore read as per-combat scripted tuning, not
one base tuple per monster:

| `res` | Appearances (STAT HP / ATK / DEF @ rank; thumb level/rank/hyper) | Spread |
|---|---|---|
| M034 | `CB0002_M01` 100/100/100 @r1, **no combat placement** (orphan, see §1.3) · `CB1501_M1` 7000/6800/280 @r5, L20/r5/h2 · `CB1002_M3` 13000/5500/280 @r5, L20/r5/h1 · `CB1301_M3` 16000/7000/300 @r5, L20/r5/h2 | HP 100→16000 (**160x**); 4 distinct tuples |
| M035 | `EVCB0102_M1` 3000/3500/200 @r4, L1/r4/h0 · `CB1002_M1` 5500/4500/280 @r5, L20/r5/h1 · `CB1301_M1` 7000/6000/300 @r5, L20/r5/h2 · `CB1501_M2` 7000/6800/280 @r5, L20/r5/h2 | HP 3000→7000; note `CB1301_M1` vs `CB1501_M2` share HP 7000 but ATK differs 6000 vs 6800 and DEF 300 vs 280 at identical thumb L20/r5/h2 |
| M036 | `EVCB0102_M2` 3000/3500/200 @r4, L1/r4/h0 · `CB1002_M2` 5500/4500/280 @r5, L20/r5/h1 · `CB1301_M2` 7000/6000/300 @r5, L20/r5/h2 | Same ladder as M035 (paired encounters; see §1.2) |
| M023 | `CB0201_M1` 700/400/130 @r2, L5/r2/h0 · `CB0301_M1` 700/650/160 @r2, L30/r2/h0 | Same HP, ATK 400→650 and DEF 130→160 as thumb level rises 5→30 at constant rank 2 |
| M062 (boss, twice) | `CB0202_BOSS` 1800/750/160 @r3, L20/r3/h0 · `CB0501_BOSS` 2000/1500/210 @r4, L1/r4/h0 | ATK doubles 750→1500 while HP barely moves |
| M100 (boss, twice) | `CB1201_BOSS` 16000/7000/300 @r5, L10/r5/h2 · `CB1401_BOSS` 20000/8000/280 @r5, L15/r5/h2 | HP +25%, ATK +14%, DEF *falls* 300→280 as thumb level rises 10→15 |
| M040 | `CB0001_BOSS` 400/190/100 @r1, L1/r1/h0 · `CB1201_M1`… no — `CB1201_M2` 6500/6000/300 @r5, L10/r5/h2 | HP 400→6500 (16x) across ranks 1→5 |
| C010 as enemy | `CB0002_BOSS` 1000/100/250 @r4 · `CB0003_BOSS` 2000/140/200 @r4 · `CB0004_BOSS` 2000/120/160 @r4, all thumb L1/r4/h0 | Same displayed hunter, three tunings; DEF *falls* 250→200→160 while HP doubles |

Two further observations against a base-tuple reading:

1. **Thumb level does not functionally determine STAT.** `CB0501_BOSS`
   (M062) at thumb L1 hits harder (ATK 1500) than `CB0202_BOSS` (same M062)
   at thumb L20 (ATK 750). `EVCB0102` rank-4 rows at L1 and `CB0501` rank-3
   rows at L20 coexist without any visible level-scaling law. The thumb
   `{level, rank, hyper}` is display/progression context for a scripted
   fight, not inputs to a base-stat formula present in local evidence.
2. **Identical thumb context, different STAT.** `CB1301_M1` (M035) and
   `CB1501_M2` (M035) are both thumb L20/r5/h2 yet read 7000/6000/300 vs
   7000/6800/280. Same monster, same displayed level/rank, different ATK/DEF.
   No per-entity base tuple survives this pair without an extra per-combat
   difficulty parameter — which is exactly what scripted Episode tuning is.

### 1.2 Pairing structure (why M035/M036 move together)

M035 and M036 are paired in three encounters (`EVCB0102`, `CB1002`,
`CB1301`) with **identical** STAT in each encounter (3000/3500/200,
5500/4500/280, 7000/6000/300 respectively). Their thumbs differ only in
`attr` (1 vs 3). This is encounter-design symmetry (two-flanker script),
not two independent base-stat observations. A future rebalance use must count
each encounter once, not each row once.

Similarly `CB1201_M1/M2/M3` (M041/M040/M042) share one tuple
6500/6000/300 at L10/r5/h2, and `CB0501_M1..M4` (M046/M052/M048/M054) share
1000/1200/180 at L20/r3/h0. Four rows, one tuning each.

### 1.3 Orphan row: `CB0002_M01`

`CB0002_M01` (M034, 100/100/100 @r1) is defined in the STAT table but is
**referenced by zero** shipped combat records (full-text search over all 60
`EPISODE_COMBAT_*.json` files, 2026-10-05). The actual `CB0002` fight fields
only `CB0002_BOSS` (enemy Vincent). The 100/100/100 row is therefore a
defined-but-unplaced datum: it has identity and numbers but no battle
context at all, the weakest of the 37 for any coverage purpose. (Hypothesis,
not fact: leftover tutorial mob from a cut wave. Do not cite.)

### 1.4 Catalog overlap table

Monster catalog denominator (`analysis/catalogue/INDEX.md` §4.2, 22 monsters):
`M001`–`M021` plus `M100`. Distinct `res` across the 34 M-rows:

`M001, M022, M023, M024, M034, M035, M036, M040, M041, M042, M044, M046,
M048, M049, M050, M051, M052, M054, M057, M058, M062, M100` — 22 distinct.

| Scope | `res` IDs | Count |
|---|---|---|
| Inside 22-catalog | **M001, M100** | **2 / 22** |
| Outside 22-catalog | M022, M023, M024, M034, M035, M036, M040, M041, M042, M044, M046, M048, M049, M050, M051, M052, M054, M057, M058, M062 | 20 |
| Catalog rows with zero Episode rows | M002–M021 except none present (no M002..M021 appear at all) | 20 / 22 catalog IDs absent |

So even if parent ruled scripted rows eligible, only **2 of 22** catalog
monsters would gain any row, and one of those (M001, single L1 tutorial row
150/130/100) has exactly one appearance while M100's two appearances
disagree (16000/7000/300 vs 20000/8000/280). The remaining 20 Episode `res`
IDs are outside the catalog and cannot credit it under the current
denominator. No video ties any fixed value to an observed full bar, and
native Episode combat rendering remains unverified (AGENTS.md §91/97 scope).

### 1.5 What parent must rule

1. Whether a scripted per-appearance row can ever satisfy the coverage.md
   monster rule ("tied to an unambiguous monster ID **plus level/rank/
   difficulty context**") — the level/rank context *is* present in the
   thumbs, so this is purely a definition call, not a data gap.
2. If yes: whether the unit of credit is the `res` (collapsing variance,
   which then needs a base-vs-script reconciliation rule) or the appearance
   (in which case M034 alone yields 4 rows and the 16-monster target needs a
   re-think).
3. Whether the orphan `CB0002_M01` and the paired-duplicate rows
   (M035/M036 encounters, CB1201 trio, CB0501 quartet) count independently.

Recommendation from this session (non-binding): keep **0/22** until at least
one row is tied to an observed full-HP bar or a native combat win receipt;
meanwhile preserve the full table below as rebalance material.

---

## 2. UNPURE raw table — all 37 monster-like Episode rows (rebalance material, NOT coverage)

**Impurity warning (read first):** every row below is a **scripted
per-appearance tuning** from the Episode-only STAT table, not a nude/base
stat. Same-`res` rows disagree by up to 160x; thumb level does not predict
STAT (§1.1); most `res` IDs sit outside the 22-monster catalog (§1.4); no
row is tied to an observed full-HP bar or native combat rendering. These
values are preserved **only** for future encounter-rebalance/scaling
estimates. **They contribute 0/22 monster coverage and must never be quoted
as base stats.** Mirrored to `polluted-observations.md` (§"Episode scripted
monster rows").

Skill-slot arrays are the combat record's 5-slot unlock flags
(`1` = slot used), not skill IDs; full skill bodies live in the STAT row.
`attr` in thumbs is the encounter-displayed element, which may differ from
the STAT row's own `attr` field (both preserved where they differ).

### 2.1 Single-appearance catalog insider: M001

| Actor | res | HP | ATK | DEF | STAT rank | Thumb (combat file) | Skill slots |
|---|---|---:|---:|---:|---|---|---|
| CB0001_M01 | M001 | 150 | 130 | 100 | 1 | L1/r1/h0/attr2 (`CB0001`, x4 placements) | [0,0,0,0,0] |

STAT-row attr: magneto-adjacent numeric fields per JSON (`attr` on actor
row); encounter attr 2. Tutorial fight; weakest scripted enemy in the table.

### 2.2 Single-appearance non-catalog rows

| Actor | res | HP | ATK | DEF | STAT rank | Thumb (combat file) | Skill slots |
|---|---|---:|---:|---:|---|---|---|
| CB0102_M1 | M022 | 450 | 430 | 180 | 1 | L5/r1/h0/attr2 (`CB0102`, x2) | [0,0,0,0,0] |
| CB0602_M1 | M024 | 2500 | 1800 | 200 | 4 | L1/r4/h0/attr3 (`CB0602`, x4) | [0,0,0,0,0] |
| CB0702_M1 | M058 | 2400 | 2600 | 200 | 4 | L30/r4/h0/attr2 (`CB0702`, x4) | [0,0,0,0,0] |
| CB0202_M1 | M050 | 800 | 680 | 160 | 2 | L10/r2/h0/attr1 (`CB0202`) | [0,0,0,0,0] |
| CB0202_M2 | M049 | 800 | 680 | 160 | 2 | L10/r2/h0/attr2 (`CB0202`) | [0,0,0,0,0] |
| CB0202_M3 | M051 | 800 | 700 | 160 | 2 | L10/r2/h0/attr3 (`CB0202`) | [0,0,0,0,0] |
| CB0501_M1 | M046 | 1000 | 1200 | 180 | 3 | L20/r3/h0/attr2 (`CB0501`; also `EVCB0101` L1/r3/h0/attr2) | [0,0,0,0,0] |
| CB0501_M2 | M052 | 1000 | 1200 | 180 | 3 | L20/r3/h0/attr2 (`CB0501`; also `EVCB0101` L1/r3/h0/attr2 x2) | [0,0,0,0,0] |
| CB0501_M3 | M048 | 1000 | 1200 | 180 | 3 | L20/r3/h0/attr3 (`CB0501`) | [0,0,0,0,0] |
| CB0501_M4 | M054 | 1000 | 1200 | 180 | 3 | L20/r3/h0/attr3 (`CB0501`; also `EVCB0101` L1/r3/h0/attr3 x2) | [0,0,0,0,0] |
| EVCB0301_M044 | M044 | 5000 | 4000 | 250 | 5 | L1/r5/h0/attr1 (`EVCB0303`, x2) | [0,0,0,0,0] |
| EVCB0301_M057 | M057 | 4000 | 4500 | 200 | 5 | L1/r5/h0/attr3 (`EVCB0303`, x2) | [0,0,0,0,0] |
| CB1201_M1 | M041 | 6500 | 6000 | 300 | 5 | L10/r5/h2/attr1 (`CB1201` x2; also `CB1401` L15/r5/h2/attr1 x2 reusing same actor) | [0,0,0,0,0] |
| CB1201_M3 | M042 | 6500 | 6000 | 300 | 5 | L10/r5/h2/attr3 (`CB1201`; also `CB1401` L15/r5/h2/attr3 x2 reusing same actor) | [0,0,0,0,0] |

Notes: `CB0501_M1..M4` share one tuning (1000/1200/180) — one design point,
four rows. `CB1201_M1/M3` actor rows are **reused across two combats**
(`CB1201` at L10 and `CB1401` at L15) with unchanged STAT — the cleanest
local proof that thumb level and STAT are decoupled. `EVCB0301` actors are
addressed through `EVCB0303` placements (file/combat-ID mismatch preserved
verbatim; do not "correct").

### 2.3 Multi-appearance rows: M023, M034, M035, M036, M040, M062, M100

| Actor | res | HP | ATK | DEF | STAT rank | Thumb (combat file) | Skill slots |
|---|---|---:|---:|---:|---|---|---|
| CB0201_M1 | M023 | 700 | 400 | 130 | 2 | L5/r2/h0/attr1 (`CB0201`, x3) | [0,0,0,0,0] |
| CB0301_M1 | M023 | 700 | 650 | 160 | 2 | L30/r2/h0/attr1 (`CB0301`, x3) | [0,0,0,0,0] |
| CB0002_M01 | M034 | 100 | 100 | 100 | 1 | **orphan — zero combat placements** | n/a |
| CB1501_M1 | M034 | 7000 | 6800 | 280 | 5 | L20/r5/h2/attr2 (`CB1501` x2; also `EVCB0301` L1/r5/h0/attr2) | [0,0,0,0,0] |
| CB1002_M3 | M034 | 13000 | 5500 | 280 | 5 | L20/r5/h1/attr2 (`CB1002`) | [0,0,0,0,0] |
| CB1301_M3 | M034 | 16000 | 7000 | 300 | 5 | L20/r5/h2/attr2 (`CB1301`) | [0,0,0,0,0] |
| EVCB0102_M1 | M035 | 3000 | 3500 | 200 | 4 | L1/r4/h0/attr1 (`EVCB0102`, x3) | [0,0,0,0,0] |
| CB1002_M1 | M035 | 5500 | 4500 | 280 | 5 | L20/r5/h1/attr1 (`CB1002`, x2) | [0,0,0,0,0] |
| CB1301_M1 | M035 | 7000 | 6000 | 300 | 5 | L20/r5/h2/attr1 (`CB1301`, x2) | [0,0,0,0,0] |
| CB1501_M2 | M035 | 7000 | 6800 | 280 | 5 | L20/r5/h2/attr1 (`CB1501`, x2) | [0,0,0,0,0] |
| EVCB0102_M2 | M036 | 3000 | 3500 | 200 | 4 | L1/r4/h0/attr3 (`EVCB0102` x3; also `EVCB0301` L1/r4/h0/attr3 x3) | [0,0,0,0,0] |
| CB1002_M2 | M036 | 5500 | 4500 | 280 | 5 | L20/r5/h1/attr3 (`CB1002`, x2) | [0,0,0,0,0] |
| CB1301_M2 | M036 | 7000 | 6000 | 300 | 5 | L20/r5/h2/attr3 (`CB1301`, x2) | [0,0,0,0,0] |
| CB0001_BOSS | M040 | 400 | 190 | 100 | 1 | L1/r1/h0/attr2 (`CB0001`) | [0,0,0,0,0] |
| CB1201_M2 | M040 | 6500 | 6000 | 300 | 5 | L10/r5/h2/attr2 (`CB1201`) | [0,0,0,0,0] |
| CB0202_BOSS | M062 | 1800 | 750 | 160 | 3 | L20/r3/h0/attr1 (`CB0202`) | [0,0,0,0,0] |
| CB0501_BOSS | M062 | 2000 | 1500 | 210 | 4 | L1/r4/h0/attr1 (`CB0501`; also `EVCB0101` L1/r4/h0/attr1) | [0,0,0,0,0] |
| CB1201_BOSS | M100 | 16000 | 7000 | 300 | 5 | L10/r5/h2/attr2 (`CB1201`) | [0,0,0,0,0] |
| CB1401_BOSS | M100 | 20000 | 8000 | 280 | 5 | L15/r5/h2/attr2 (`CB1401`) | [0,0,0,0,0] |

All monster skill-slot arrays in this table are `[0,0,0,0,0]` (no scripted
skills flagged on monsters in the sampled combats); STAT-row skill bodies
exist in the JSON but are encounter mechanics, not base-stat evidence, and
are not transcribed here.

### 2.4 Enemy-Vincent rows (C010 placed as monster — scripted, not hero data)

| Actor | res | HP | ATK | DEF | STAT rank | Thumb (combat file) | Skill slots |
|---|---|---:|---:|---:|---|---|---|
| CB0002_BOSS | C010 | 1000 | 100 | 250 | 4 | L1/r4/h0/attr3 (`CB0002`) | [1,0,0,1,0] |
| CB0003_BOSS | C010 | 2000 | 140 | 200 | 4 | L1/r4/h0/attr3 (`CB0003`) | [1,0,0,1,0] |
| CB0004_BOSS | C010 | 2000 | 120 | 160 | 4 | L1/r4/h0/attr3 (`CB0004`) | [1,0,0,1,0] |

These are the same hunter ref (`C010` Vincent) scripted as the enemy. They
are neither monster-catalog rows nor hero base stats. Preserved because an
enemy-side HP/ATK/DEF ladder with falling DEF (250→200→160) is rebalance
context for early-Episode difficulty curves.

### 2.5 Boss rows among the 37

Boss-flagged actors (`*_BOSS`): `CB0001_BOSS` (M040), `CB0202_BOSS` (M062),
`CB0501_BOSS` (M062), `CB1201_BOSS` (M100), `CB1401_BOSS` (M100),
`CB0002/0003/0004_BOSS` (C010). Seven of 37. No boss intro card or name
panel is tied to any of these in video evidence (per the P J contact-sheet
negative result).

### 2.6 Rebalance-use caveats (normative)

1. Never collapse same-`res` rows into one tuple without stating the rule
   (mean? latest chapter? max?). The table preserves appearances precisely
   so no collapse is smuggled in.
2. Never join these HP values to P J video bar tokens (`2,551`, `1,253`):
   identity, chapter/difficulty, and full-vs-current semantics are all
   unproved on the video side.
3. Era-tag these PRE/POST 2019-09-05 with **unknown**: the source pack is
   recovered but its balance vintage is not established in local
   evidence. Do not assume either era.
4. The STAT rows carry full secondary fields (`spd`, `crt_chance`,
   `crt_dmg`, `penetration`, `attr_enhance`, `block_chance`,
   `block_dec_dmg`, `attr_resist`, `hp_regen`) plus skill `base_number`
   effect bodies. They are omitted here for table legibility, not absent
   from the source — consult the JSON for encounter rebuilds.

### 2.7 Boundary: hunter-placed C010 rows (excluded from the 37)

For the record, so a future auditor does not "find" extra monster rows:
`CB0302_010_1` (3000/310/210 @r4, thumb hunter L1/r4/h0),
`CB0702_010_1` (3700/1800/260 @r5, thumb hunter L30/r5/h0),
`CB1302_C010` (3200/1601/1149 @r5, thumb hunter L1/r5/h2),
`CB1603_C010` (4000/1900/1400 @r5, thumb hunter L30/r5/h2).
Scripted ally-side actors; hero-base status equally unproved; not counted
anywhere.

---

## 3. Provenance and limits

- All numbers re-derived from disk 2026-10-05 by enumerating
  `EPISODE_STAT_ACTORS.json` (152 rows; 34 `M*` res + 3 monster-placed
  `C010`) and joining every combat file's `thumb`/skill slots. The §4
  "37 monster-like rows" figure is confirmed as 34 + 3.
  **[CORRECTED 2026-10-06: that enumeration filtered on `res_id` namespace
  only and therefore missed 5 further monster-placed `C*` rows
  (`CB1102_006/_008/_011/_018/_019`). Exhaustive: 34 `M*` + 8 monster-typed
  `C*` = 42 monster-like rows, 109 hunter-typed `C*` hero rows.]**
- **[RETRACTED 2026-10-05] "→ art mapping is by filename convention"
  is FALSE.** It was first retracted for `M034` alone
  (`m034-variance-2026-10-05.md` §3.3 item 1) and then **measured across all
  22 tokens** in `episode-res-crosswalk-2026-10-05.md` §1.3 / §3.1. No
  `M034.jet` exists, and no `M0xx` pack exists for **20 of 22** tokens; the
  convention is real only for the `C*` namespace (**64/64** tokens match
  `<res_id>.jet`), not the `M*` namespace (**2/22**, and both survivors are
  the tokens whose own catalogue rows are admitted identity UNKNOWNs).
  `M001`↔`M001.jet` and `M100`↔`M100.jet` holding is what made the rule look
  general. There is no local binding table of any kind, and `ref_id` is a
  hunter-card namespace (120/120 to cards, 0 to monsters) so it cannot
  substitute. **Replacement statement:** the `M*` Episode `res` token is an
  opaque, data-only per-appearance script token — a grouping label inside
  `EPISODE_STAT_ACTORS.json`, not a resolvable monster identity. Any future
  join needs a recovered binding table, never filename similarity. Do not
  over-claim the join. Superseding evidence:
  `episode-res-crosswalk-2026-10-05.md` §1.3 + §3.1.
- No server/APK changes were made in this session. No native Episode combat
  was played or rendered. Coverage files untouched except the mirrored
  impure note in `polluted-observations.md`.
