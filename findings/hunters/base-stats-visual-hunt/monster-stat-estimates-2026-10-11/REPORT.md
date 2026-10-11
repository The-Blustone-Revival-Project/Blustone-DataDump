# Monster base-stat estimates — 2026-10-11 lane

**Lane:** `findings/hunters/base-stats-visual-hunt/monster-stat-estimates-2026-10-11/`
**Question:** how much of the 22-catalog-monster ledger row
(`coverage.md` §Monsters, target 16 of 22) can be filled with a source-backed
HP/ATK/DEF tuple under the 2026-10-11 owner adjudication
("derivation from recovered mechanics plus source-backed anchors counts").

## 0. Headline

| | |
|---|---|
| Source-backed client rows recovered | **34** rows, **22 distinct monster `res_id`s**, all from `sources/client-tables/reference/EPISODE_STAT_ACTORS.json` |
| Catalog rows at `[RECOVERED]` (≥60 % point) | **12 / 22** — M001, M008, M012, M014, M015, M016, M017, M018, M019, M020, M021, M100 |
| Catalog rows at `[DERIVED-ESTIMATE]` | **10 / 22** — M002, M003, M004, M005, M006, M007, M009, M010, M011, M013 (15–45 % point) |
| Catalog rows at `[INFERRED-FIXTURE]` | **0** |
| **Coverage under the ≥60 % rule** | **12 / 22 = 54.5 %** — the 16/22 target is **not met** |
| Coverage if the denominator is re-based to real monster ids | **22 / 22 monster `res_id`s** carry a shipped HP/ATK/DEF tuple |

The single most important result of this lane is **not** the count, it is the
identity finding in §4: the ledger's "22 catalog monsters" are **22 art
packages**, not 22 monsters. Each package holds three consecutive monster ids,
so the project's monster roster is at least 64 entries, of which the shipped
client data covers 22.

---

## 1. What was re-extracted (task 1)

`EPISODE_STAT_ACTORS.json` = 152 rows. Partition:

| class | rows | how identified |
|---|---:|---|
| Monster actor rows | **34** | `res_id` starts with `M` |
| Hunter / scripted-card rows | **117** | `res_id` starts with `C` |
| Literal `{}` junk | **1** | index 80, an empty object |
| **total** | **152** | |

**Correction to the parent brief's row rule.** The brief said "32 rows WITHOUT a
`ref_id` — these are MONSTER actor rows". That filter is **wrong as a monster
discriminator**: three rows that *do* carry `ref_id` also carry a monster
`res_id`, and one of them is the only catalog-monster hit in the whole file:

```
CB0001_M01   ref_id 001  res_id M001  rank1 hp150 atk130 def100  (CB0001, power 1000, thumb L1/r1/h0/attr2)
CB0002_M01   ref_id 034  res_id M034  rank1 hp100 atk100 def100  (no combat placement - orphan row)
CB0001_BOSS  ref_id 040  res_id M040  rank1 hp400 atk190 def100  (CB0001, power 1000, thumb L1/r1/h0/attr2)
```

`ref_id` is not a namespace marker; the safe discriminator is `res_id`
starting with `M`. The correct totals are **34 monster rows / 118 other**, not
31+1/32.

The parent's otherwise-correct dump is confirmed verbatim (see
`episodes-monster-actors.tsv`). The one trailing junk entry the brief warned
about is the literal `{}` at index 80; it is skipped, not deleted.

**Positive controls (all passed before any output was written):**
`CB1201_BOSS` = M100/rank5/16000/7000/300; `CB1401_BOSS` =
M100/rank5/20000/8000/280; `CB0102_M1` = M022/rank1/450/430/180.

## 2. Stage → monster → rank context (task 2)

All 61 `EPISODE_COMBAT_*.json` files were walked; 20 of them place a monster
actor on the right side, 72 monster slots in total
(`episode-combat-stages.tsv`). Every monster slot now carries its stage `power`
and the actor's `thumb` = `{level, rank, hyper, attr}`. Every monster slot
except `CB0002_M01` resolves to a stat row in `EPISODE_STAT_ACTORS.json`.

A few structural notes:

* `CB0002_BOSS` / `CB0003_BOSS` / `CB0004_BOSS` are `res_id C010` — **Vincent,
  a hunter card tuned as an enemy** — and are excluded from the monster tables
  (the 2026-10-05 adjudication lane already flagged this class).
* `CB1102_011/018/019/006/008` are also `res_id C0xx` (cards), not monsters.
* **`rank` in the stat block equals `thumb.rank` in the combat record in every
  row** — e.g. `CB0202` right side is rank 2 (mobs) / rank 3 (boss), and its
  stat rows read exactly 2/2/2/3. So `rank` is a per-encounter tier, not a
  per-monster property.
* Stage `power` is a strict difficulty ladder: **1000, 2200, 2700, 4500, 5000,
  9000, 25000, 26000, 30000, 33000, 40000, 68000, 85000, 90000, 95000, 100000,
  105000, 115000**.

## 3. Workspace census for M001–M021 / M100 (task 3)

`search_monster_ids.py` walked every file in the workspace:

* **30 119 files content-scanned**, 18 120 skipped by extension (48.0 GB of
  `.png/.jpg/.mp4/.apk/.qcow2/.img/.jet`-class binaries — `jet_namespace_walk.py`
  reads those properly instead), 15 skipped as >32 MB, **0 read errors**.
* Positive control: `M100` and `M001` both found in
  `sources/client-tables/reference/EPISODE_STAT_ACTORS.json` → scan is alive.
* `\bM\d{3}\b` hits for every one of M001–M021 and M100. Full inventory in
  `monster-id-workspace-census.tsv` / `.json`; classified in
  `monster-id-hit-classification.tsv`.

**Result: there is no second source of monster stat rows anywhere in the
workspace.** All M002–M021 hits fall into exactly three buckets:

1. filesystem/name lists — `catalog/legacy-catalogue-data/monsters.json`,
   `datasets/monsters/identities.json` (all `base_stats` = `null`),
   `local/migration/full-path-map.json`, the CDN pack group
   `sources/client-tables/recovered-data/cdn-manifest/cdn-pack-groups.json`
   (`monsters_M###` = `M002…M021`, `M100` — **21 pack names, and M001 is
   absent**), `assets/M0nn.jet` path entries;
2. project prose in `findings/**` that quotes the catalog id;
3. coincidental byte matches inside compressed `.jet` payloads (e.g. `M018`
   inside `C017_EFT.jet`, `M002` inside `VOICE_CDN7.jet`). These are **not**
   namespace names and were discarded — the same reasoning
   `episode05-entry-materials.md` used for base38 texture ids.

Also checked and negative: `sources/client-tables/recovered-data/campaign-stages.json`
holds only stage ids and analytics codes for `n_01_01`…`n_05_10` — **no
stage→monster link**. The local replica captures in
`local/private/recovered-assets/campaign-receipts-20261009/` and
`sources/observations/r014/` only ever publish **`M001`**; every other `M0xx`
token in them is a CDN package name in a `packages=` list or a coincidental
numeric field (`M084`, `M089` are timestamps). `r014`'s
`/reference/GetMonster` body is a local fixture ("Local compatibility test
encounter", `hp 100 / atk 10 / def 5`).

---

## 4. The identity finding: the 22 catalog rows are art packs

`datasets/monsters/catalogue/M001.md` states `res_prefix = M001` because "the
only monster art prefix in the pack is the monster id itself", and
`catalog/INDEX.md` §3 lists the 22 rows as monsters with art `M0nn.jet`.

Decoding the JET record namespaces proves this is wrong. A `.jet` file is a
24-byte outer header (`u32 size`, `u32 size` dup, `u32 packed`, `u64 record id`,
`u16 pad`, `u16 kind`) followed by records of the same 24-byte shape each
carrying `packed` bytes of raw zlib. **The record name is its `u64` id rendered
in base 38 over `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`.**

```
id 2517307526885 -> M022_R01     id 66244934539  -> M022_H1
id 2517307507366 -> M022_DIE     id 66244935011  -> M022_TH
id 138129698730429764 -> M022_SHADOW
```

Positive control on `M008.jet`: **134 records, walk ends exactly at 223 669
bytes, 33 `M022_*` names, and all eight expected families
(`M022_R01..R04`, `M022_H01..H15`, `M022_DIE`, `M022_S`, `M022_SHADOW`,
`M022_TH`) present** — byte-for-byte the numbers
`episode-cb0102-m022-original-resources.md` recorded by hand.

Walking all 22 catalog packages (`jet-monster-namespaces.tsv`, every walk ends
exact-EOF):

| pack | hosts monster `res_id`s |
|---|---|
| M001.jet | M001, M002, M003 |
| M002.jet | M004, M005, M006 |
| M003.jet | M007, M008, M009 |
| M004.jet | M010, M011, M012 |
| M005.jet | M013, M014, M015 |
| M006.jet | M016, M017, M018 |
| M007.jet | M019, M020, M021 |
| M008.jet | M022, M023, M024 |
| M009.jet | M025, M026, M027 |
| M010.jet | M028, M029, M030 |
| M011.jet | M031, M032, M033 |
| M012.jet | M034, M035, M036 |
| M013.jet | M037, M038, M039 |
| M014.jet | M040, M041, M042 |
| M015.jet | M043, M044, M045 |
| M016.jet | M046, M047, M048 |
| M017.jet | M049, M050, M051 |
| M018.jet | M052, M053, M054 |
| M019.jet | M055, M056, M057 |
| M020.jet | M058, M059, M060 |
| M021.jet | M061, M062, M063 |
| M100.jet | M100 |

Each pack hosts three consecutive monster ids, each with a complete sprite
family (`R01..R04` idle, `H01..H15` hit, `AS1..AS3` attack, `DIE`, `S`,
`SHADOW`/`SHA`, `TH`/`THN` thumbnail). `M001.jet`'s own record census:
134 records, `M001_*` 33 + `M002_*` 32 + `M003_*` 33 = 98 named.

**Proof that pack name ≠ monster id:** monster `res_id` **M022**
(`CB0102_M1`, a shipped stat row) has **no `M022.jet` anywhere on disk**, and
its namespace lives inside **M008.jet**. If pack names were monster ids then
M022's pack would be `M022.jet`. Therefore catalog row `M002` (art `M002.jet`,
which hosts M004–M006) is **not** monster M002. The catalog enumerated pack
*filenames* from the CDN group `monsters_M###` and labelled them monsters.

Consequences:

* The roster is **≥ 64 monsters** (M001…M063 + M100), not 22.
* The 22 episode `M*` `res_id`s (`M001, M022, M023, M024, M034, M035, M036,
  M040, M041, M042, M044, M046, M048, M049, M050, M051, M052, M054, M057,
  M058, M062, M100`) are real monster ids and all 22 carry shipped stat rows.
* The 2026-10-06 external hunt's "Two 22s — the denominator trap" reading
  (an intersection of **2**) is correct about the *IDs overlapping* but
  understates it: the correct relation is pack→monster, and **12 of 22 packs**
  contain at least one monster with a shipped row.
* `monster-stat-external-hunt-2026-10-06.md` §1.3's "M022…M062 have no art file
  anywhere locally" was a filename-only check and is superseded (it was already
  superseded for M022 by `episode-cb0102-m022-original-resources.md`; this walk
  closes it for all 20).

---

## 5. The estimation model

### 5.1 The tier ladder (fit on the 34 recovered rows)

`stage power` → `rank` is clean and monotone across all 34 rows:

| power | rank | rows |
|---|---|---|
| < 2 500 | 1 | 2 |
| 2 500–8 999 | 2 | 4 |
| 9 000–24 999 | 3 | 5 (one boss at r4) |
| 25 000–39 999 | 4 | 5 (all r4) |
| ≥ 40 000 | 5 | 18 (all r5) |

Per-rank medians (hp / atk / def) and p10–p90 bands
(`model-figures.txt` has the full table):

| rank | n | hp med [p10–p90] | atk med [p10–p90] | def med [p10–p90] |
|---|---:|---|---|---|
| 1 | 4 | 275 [115–435] | 160 [109–358] | 100 [100–156] |
| 2 | 5 | 800 [700–800] | 680 [500–692] | 160 [142–160] |
| 3 | 5 | 1000 [1000–1480] | 1200 [930–1200] | 180 [168–180] |
| 4 | 5 | 2500 [2160–3000] | 2600 [1620–3500] | 200 [200–206] |
| 5 | 15 | 7000 [5200–16000] | 6000 [4500–7000] | 280 [262–300] |
| pooled | 34 | 2750 [525–11200] | 3050 [409–6800] | 200 [139–300] |

`power` → stat log-law: `hp = 1.150·P^0.776` (MAPE 28 %),
`atk = 1.063·P^0.763` (MAPE 14 %), `def = 27.83·P^0.203` (MAPE 7 %).
`def` is nearly power-invariant; `hp`/`atk` scale strongly.

### 5.2 `stat.hp` is an unscaled combat value

The 2026-10-06 external hunt closed this falsifier: `EPISODE_COMBAT_CB0101`
ships `CB0101_009_1` at `hp 323` and `CB0101_003_1` at `hp 514`, and the device
capture `analysis/testing/episode-010/29-cb0101-after8.png` shows the untouched
red bar at exactly `514` and the damaged green bar at `311` (= 323 − 12). So a
row's `hp` is the literal on-screen combat HP, not a pre-scale constant that a
hidden level/rank formula inflates. That is what makes these rows usable as
per-encounter tuples.

### 5.3 `rank` counts **UP** — catalog §5.2's direction is refuted

`catalog/INDEX.md` §5.2 infers from `LEVELING.jet` chunk 9 `bonus.rank_1..5`
that "rank 1 = toughest band, rank 5 = weakest", reasoning that `rank_5` being
all-1.0 makes it the baseline. The shipped episode data runs the other way:

| rank | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| median hp | 275 | 800 | 1000 | 2500 | **7000** |
| hp relative to rank 5 | 0.039 | 0.114 | 0.143 | 0.357 | 1.000 |
| LEVELING `bonus.rank_N` hp | 2.6 | 2.2 | 1.8 | 1.4 | 1.0 |

The ratio is **0.039**, not 2.6. In `EPISODE_STAT_ACTORS.json` `rank` is the
monster's star tier and **rank 5 is the toughest band**. Either `bonus.rank_*`
is not applied to these shipped rows, or it is keyed on a different axis (e.g. a
difficulty band) than the stat block's `rank`. The INDEX.md §5.2 inference
should be revised, and the §8 placeholder note ("multiply HP by the rank factor
from §5.2") should not be applied to these rows.

### 5.4 Confidence rule (mechanical, not asserted)

* `[RECOVERED]` = **95 %**. The value is a verbatim shipped literal for one
  identified monster in one identified encounter with stage `power`,
  `thumb.level/rank/hyper/attr` and an element all recorded. It is not a
  "base stat" in the sense of a monster's own permanent tuple — see §6 — but it
  does satisfy `coverage.md`'s promotion clause as written.
* `[DERIVED-ESTIMATE]` point confidence =
  `100 · (1 − log10(hp-bracket ratio) / log10 200)`, floored at 15, capped at
  45. The ten derived rows come out at 45 % (M002–M007, bracket 150–2500 =
  16.7×) and 15 % (M009–M011, 450–16000 = 35.6×; M013, 400–16000 = 40×).
* `[INFERRED-FIXTURE]` = **0 rows**. Nothing here is invented.

The point value for a derived row is the **median of every recovered row for the
two bracketing anchored packs** (nearest anchored pack below and above in pack
order), and the band is that bracket's min–max. Rank, level and stage placement
for those monsters are genuinely undetermined and are recorded as `unknown`.

### 5.5 What is *not* in the model

* `LEVELING.jet` `bonus.role_*` (bomber 0.85 hp / support 0.80 hp) is **not
  applied**: the episode rows are already-final values and the monster
  `role` field (observed values 1 and 2) has no recovered mapping to
  offense/deffense/bomber/support. `attr` is recorded verbatim (1/2/3) and maps
  to the Fire/Ice/Lightning cycle only by symmetry with the card data.
* `bonus.stage` `b_XX_YY` per-stage multipliers are **not** applied. `b_00_01`
  whitelists card `051` and is a boss-stage modifier, not a monster stat
  source. Its only observed use is the replica receipt
  `b_00_01_n_01_01_M001`.

---

## 6. Honest limits on what these rows mean

1. **They are per-encounter, not per-monster.** The 2026-10-05 adjudication lane
   established this and nothing here overturns it: `M034` appears with four
   different tuples (`100/100/100`, `7000/6800/280`, `13000/5500/280`,
   `16000/7000/300`); `M035` with four; `CB1301_M1` and `CB1501_M2` are the
   *same* monster at the *same* thumb L20/r5/h2 and read `7000/6000/300` vs
   `7000/6800/280`. Quoting `M001 = 150/130/100` as "M001's base stats" is
   still wrong; the correct sentence is "monster `M001`, as tuned for stage
   `CB0001` (power 1000, thumb L1/r1/h0/attr2), has hp 150 / atk 130 / def 100".
   The ledger clause "a source-backed HP, ATK, and DEF tuple tied to an
   unambiguous monster ID plus level/rank/difficulty context" is satisfied
   **as written**; a stricter "base stat" clause would not be, and the owner
   should decide which reading governs.
2. **The replica `872 HP` anchor in the task brief is retracted.**
   `findings/hunters/in-game-stats.md` §4 proves, on four independent lines,
   that the `872` in the r016 frame was the **player's** HP and that the
   monster's HP is displayed byte-for-byte as sent (the fixture's `100`).
   `catalog/INDEX.md` §8's sanity check ("the level-1 monster `M001` showed
   **872** HP") and `report-016` §1 both repeat that misattribution. It is
   **not** used as an anchor here, and it must not be differenced against the
   shipped `150` — that comparison is explicitly forbidden by
   `monster-stat-external-hunt-2026-10-06.md` §2.3 and by
   `coverage.md` ("Do not use current replica fixture data as original-game
   evidence").
3. **`attr`/`role` on the anchor rows are recorded, not interpreted.** The
   replica's `GetMonster` returns `attr 1` for `M001` while the shipped client
   row says `attr 2`; the replica value is fixture data and loses.

---

## 7. What remains genuinely unknowable from shipped data

1. **42 of the ≥64 monsters have no shipped stat row at all** — M002…M021,
   M025…M033, M037…M039, M043, M045, M047, M053, M055, M056, M059, M060, M061,
   M063. In pack terms these are packs M002–M007, M009, M010, M011, M013.
2. **Why:** the episode/story table is the only monster stat table in the APK,
   and `findings/revival/hasmonsterdata.md` proves `CSRGameMob::m_mMonsters` has
   exactly one writer — the `/reference/GetMonster` response callback. The
   expedition monsters' stats were therefore **server-authoritative and never
   shipped**. The project holds no original-server capture of that response
   (the only bodies on disk are the local replica's `M001`-only fixture).
3. **The only two things that would close the gap** are both server-side: an
   original-server `/reference/GetMonster` (or `/reference/GetTargetStageMonster`)
   capture, or the original expedition stage→monster table linking `n_01_01`…
   `n_05_10` to monster ids. Neither exists locally. No amount of local mining
   can recover them, and nothing in this lane claims otherwise.
4. **Per-monster identity** (display name, element, role) stays `[UNKNOWN]` for
   all 22 rows. `catalog/findings.json` and `datasets/monsters/identities.json`
   agree: `base_stats` = `null` everywhere.

---

## 8. Tier counts and coverage

| tier | rows | ids |
|---|---:|---|
| `[RECOVERED]` | **12** | M001, M008, M012, M014, M015, M016, M017, M018, M019, M020, M021, M100 |
| `[DERIVED-ESTIMATE]` | **10** | M002–M007, M009, M010, M011, M013 (45 % × 6, 15 % × 4) |
| `[INFERRED-FIXTURE]` | **0** | — |
| **≥60 % point** | **12 / 22 = 54.5 %** | target 16 / 22 — **not met** |

Under the current denominator the lane lands **4 rows short** of the target.
The four nearest misses are the packs whose monsters are bracketed most
tightly (M013 at 15 % is the worst, because both neighbours span 400–16000).

Two honest options for the ledger owner:

* **(a) keep the denominator and accept 12/22**, recording why the remaining 10
  cannot reach 60 % (their rank/stage placement is not in any shipped file); or
* **(b) re-base the denominator to monster ids**, where all **22** episode
  monster `res_id`s carry a shipped HP/ATK/DEF tuple and coverage is
  **22/22 at 95 %**, while noting that this covers 22 of ≥64 monsters.

Option (b) is the more defensible reading of "a source-backed HP, ATK and DEF
tuple tied to an unambiguous monster ID", and the pack→monster crosswalk in
§4 is the evidence for it. This lane does not unilaterally edit the ledger.

---

## 9. Deliverables in this folder

| file | contents |
|---|---|
| `monster-stat-estimates-2026-10-11.tsv` | the 22 catalog rows: identity, hosted monster ids, rank/hp/atk/def, tier, point confidence, band, method, source file + locator |
| `episode-monster-recovered-rows.tsv` | the 34 recovered client rows, verbatim, with full stage + thumb context (32 columns) |
| `jet-monster-namespaces.tsv` / `.json` | the pack → monster-namespace crosswalk, all 22 packages |
| `episodes-monster-actors.tsv` | all 152 actors partitioned; 34 monster rows |
| `episode-combat-stages.tsv` | all 408 actor slots across 61 stages with `power` + thumb |
| `monster-id-workspace-census.tsv` / `.json` | every `M0nn` workspace hit, file + line + context |
| `monster-id-hit-classification.tsv` | data-row vs prose split per catalog id |
| `model-figures.txt` | the fitted ladder, printed |
| `extract_episode_actors.py` | task 1 + 2 extraction, with positive controls |
| `search_monster_ids.py`, `classify_hits.py` | task 3 workspace census |
| `jet_namespace_walk.py` | base38 JET record-name decoder + pack crosswalk |
| `fit_rank_ladder.py` | rank ladder and power→rank fit |
| `build_monster_estimates.py` | emits the two TSVs and `model-figures.txt` |

Nothing outside this folder was written or modified. No git command was run.
No device was operated.
