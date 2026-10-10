# Blustone stat-recovery guesstimate — corpus assessment (2026-10-08 refresh)

> **APPENDIX (added same day, per user request): the actual guesstimate tables —
> hero-by-hero stats (113 rows), every Episode scripted hunter tuple (117 rows),
> every scripted monster tuple (34 rows), the monster catalog, jewel set bonuses
> and samples, all multipliers, per-area campaign rewards, all 18 Episode chapter
> rewards, original-pixel reward anchors, and ~30 price/economy rows — each row
> carrying a numeric `Conf%`, a confidence word, and a notes column.** The
> appendix is at the end of this file; the analysis above explains where every
> number in it comes from.

## 0. What changed in the 2026-10-08 refresh (evidence: AGENTS.md §136–§165)

The corpus itself was already research-complete; this refresh folds in native
verifications the live client produced in the two days after the Oct-6 file.
Same format, same tables — the deltas:

1. **Grade EXP-to-max endpoints 200/400/1200/4800/24000 raised 80→95 (HIGH):**
   an in-client consumer audit (§156) corroborates all five endpoints against
   the owned hunters' native levels. Interior thresholds remain unknown.
2. **Owned-hunter stats 001–004 are now native-verified** at their live levels
   (§159 archive-2019-projection deployed; detail/BuildTeam parity, native
   strength 25904). New Table A.2. The decomposition into base+growth still
   uses fixture growth (+10/+1/+1), so Table A base rows keep their archive
   confidence; A.2 is the display-pipeline proof.
3. **Enemy-side hunter-class rows natively rendered** (§160–§165): CB0102
   Gerard HP1000, CB0103 Bear HP1700 + ally Gerard HP310, CB0201 enemy Bright
   HP900, CB0202 ally Bright HP600, CB0301 Denali HP1300, CB0302 Vincent
   HP3000. New Table C.2 — exercised rows jump to 90 (HIGH). Chapter-specific
   tuning re-confirmed (E03-M023 650/160/10 ≠ E02-M023).
4. **Wire stat growth formula closed [NATIVE]** (§158): hp/atk/def/spd at
   CSRCardStat+18/+28/+38/+8, growth +c8/+d8/+e8, helper =
   uint32(base+up×level)×multiplier, Validate receives GetStatWithoutEquip.
   **Attack-speed unit closed**: interval = (1/spd)/atk_spd_bonus, min 0.06 s.
   **Level selectors closed** (§157): no sentinel; first threshold above EXP →
   level-1. All added to Table F. Magnitudes remain fixtures.
5. **SP/Rage is mode-dependent**: live CB0102 groups measured rate 0.03/max 10
   (§160) — the chunk-9 values are not global. Skill-cost debit verified
   natively (Nene cost 3: SP 10→7.04, §161).
6. **E02 FMD1×30 receipt verified natively** (§164: free Manda 239640→239670);
   the ×30 quantity is original, the wallet mapping stays replica policy.
   Login claim path verified day3/day4 (§146/§155); Special Supply settlement
   verified for all 16 local rows (§147).
7. **Fishing settlement contract wire-verified but data-blocked**: EndWithSell
   posts `log_id:"-1"`; terminal ACK is 27/2; missing fish reference → DUMMY
   zero popup, not a legitimate catch. All 6 local LevelDB cache containers
   scanned, zero reference keys (§145).
8. Mirage no longer crashes (§136: `GetExtra.local_time` + GetInfo DTOs; the
   Oct-6 clock assertion is retired). Not a stat datum, but it un-blocks the
   Mirage mode for future content work.

Nothing was re-derived: every raise quotes its §-numbered source.

**Purpose:** a one-shot estimate of how much of the original Blustone stat/economy
model is recoverable from the analysis corpus, broken into categories with
completeness, confidence, and data-volume counts. This file is a **read-only
synthesis**: every claim is quoted or counted from the named source files. It
invents no values and changes no coverage ledger.

Confidence scale used below:

- **HIGH** — [NATIVE] parser evidence, [ORIGDATA] shipped-client data, or ≥2
  independent sources agreeing.
- **MEDIUM** — single [COMM] source, or [IMAGE-pixel] original-game pixels, or
  multi-source but era-unresolved.
- **LOW** — polluted/single visual observations, derived hypotheses, or
  provenance-unknown rows.

---

## 1. What the corpus actually is (why ceilings exist)

The decisive structural finding (`old-apk-2026-10-05.md`, `apk-diff-2026-10-05.md`,
`local-reaudit-2026-10-05.md`, `SYNTHESIS-2026-10-05.md` §5): **no APK version
carries per-entity stat tables.** Stats were served from the original server via
`/reference/*`; the client ships art, audio, dialogue, help text, UI strings, and
shared battle tuning only. Every locally available APK version was audited:

- `EQUIP.jet` = 24 textures, zero text resources.
- `LEVELING.jet` = 21 resources / 20 textual payloads of *shared* tuning only.
- 2.8.0.1 `UI_CSV.jet` ships `monsterref: []` and `stageref: []` — native
  reference hooks with empty arrays.
- 774-package JET scan: one shared tuning CSV, no per-card/per-item rows.
- `recovered-assets/` has zero `.pcap/.har/.ndjson` original-server captures.

So per-hero and per-monster base stats can only come from external/archived
sources and the one shipped exception: the Episode scripted-actor STAT table.
This caps strict completeness structurally, not by effort.

---

## 2. Data ingested — volume counts

### 2.1 Native / binary evidence surfaces
| Surface | Volume |
|---|---|
| `analysis/native-all-strings.tsv` (all printable native strings) | 515,612 lines |
| `analysis/native-evidence.tsv` (retained symbols) | 48,942 lines |
| Ghidra decomp/parse artifacts across the research tree | ~120 lane files reference them |

### 2.2 Shipped-client data (highest evidence class)
| Dataset | Rows | Numeric cells |
|---|---:|---:|
| `EPISODE_STAT_ACTORS.json` (R_EPISODE.jet STAT table) | 151 actor rows (34 `M*` + 8 monster-typed `C*` + 109 hunter rows), 86 distinct res_ids, 54 distinct hero ref_ids | ≈ 2,378 (13 stat fields × 151 + attr/role/cool_time) |
| Episode S01 catalog (`EPISODE_S01.json`) | 18 chapters, 128 stories, 147 unique IDs; 61 combat records (47 CB + 14 EVCB); 18 chapter reward declarations | ~200 structural |
| `SKILL_REF.json` | 1,070 entries × 5 locales (formula strings, no magnitudes) | 0 (text) |
| `SKILL_EFFECT.json` / `SKILL_DESC.json` | 230 / 860 entries (text only) | 0 |
| 2.8.0.1 `UI_CSV` help corpus | 95 CONTENTS records | 0 cost hits (swept, 20 patterns) |
| 1.4.4.1 help corpus | 73 records | 12 set-bonus rows |
| `CHAR_STR_RO` item/character strings | 105 item rows | 0 |
| `LEVELING.jet` chunk 19 power ladder | 56 rows (power,rank,hyper,level) | 224 |
| `LEVELING.jet` chunk 9 battle tuning | ~60 scalars + role/rank multipliers | ~75 |
| `LEVELING.jet` chunk 1 rank-up success curve | 14 rows | 42 |
| `campaign-stages.csv` | 50 stages × 6 cols | ~250 |
| `environments.csv` | 50 environments × 18 cols | ~800 |

### 2.3 External numeric sources (the two real stat mines)
| Source | Rows | Numeric cells | Era |
|---|---:|---:|---|
| 2019 Japanese hunter archive (Wayback blustone.jp) | 63 rows crosswalked to 62 catalog IDs (1 all-`???`) | **806** core cells (62 × 13 fields) + draw rarity | POST-2019-09-05 |
| VSFan `Hunter Stats [BROKEN IGNORE].xlsx` extract | 189 rows inventoried; 67 fully numeric | ≈ 871 (67 × 13) | PRE, provenance unknown (polluted) |
| Original-game pixel readings (result-screens R1–R10) | 10 screens | ~35 numerals | mixed/era-tagged |
| Official event/announcement posts | 5+ bodies | ~25 numerals | PRE-2019 |

### 2.4 Catalogue / identity metadata
| Dataset | Rows |
|---|---:|
| `card-catalogue.tsv` | 121 rows × 16 cols (113 real characters + 8 non-card) |
| `monsters.json` | 22 entries (art only, zero stats) |
| `hero-identity-crosswalk` | 113 consolidated rows (71 CONFIRMED / 35 SINGLE-SOURCE / 7 UNRESOLVED) |
| `uncovered-archive-roster-2019.tsv` | 51 rows |
| Miraheze equipment crosswalk | 282 rows (98 weapon / 90 armor / 94 accessory) |
| `skill-effect.tsv` / `tag-ref.tsv` | 230 / 142 rows (text) |

### 2.5 Visual-hunt process ledger
| Item | Count |
|---|---:|
| Observation-ledger rows in `coverage.md` | 87 |
| Per-source verdict rows in `README.md` | 56 |
| Lane/report files in this folder | 121 .md files |
| Polluted observations (`polluted-observations.md`, 191 KB) | ~100+ dated entries |
| Monster HUD tokens catalogued | ~30 (16 P J video + others), all polluted |

**Rough total: ≈ 5,300 numeric stat/economy data cells ingested from
extracted/shipped/external sources, plus ~1,000 catalogue/identity rows and ~150
process-observation records.** The densest single file is the Episode STAT table
(≈2,378 cells) — but it is per-appearance scripted tuning, not base stats.

---

## 3. Category-by-category guesstimate

### 3.1 Hero base stats — 113 catalog characters
**Strict coverage: 1/113 (0.9%)** against the 80-hero target. Only Beckhen `051`
has a source-backed HP/ATK/DEF tuple with level (Lv.30) and gear state
(no-equipment) documented, cross-validated by the archive row.

**Candidate material (identity reach): 73/113 (65%)** — 62 archive rows (2019,
POST balance) ∪ 54 heroes in Episode data, 44 overlap, 11 Episode-only, 40 in
neither. 50 distinct (hp,atk,def) tuples exist across the 62 archive rows.
Two-source shape confirmation (±15%): only 13/113 (11.5%).

**Confidence split:**
- **Identity (who is who): HIGH.** Role agreement 99/100, element 94/100 between
  archive and Episode enums; archive↔wiki rarity 61/61; crosswalk 71 CONFIRMED.
- **Values as original base stats: MEDIUM-LOW.** Archive level is "not shown" and
  gear state "not established"; era is POST-2019-rebalance. Mitigation: the
  `051` gear-invariance check shows shape features move ≤2.2% between Lv.30-nude
  panel and archive row, so the tuples are usable *as shape priors* even though
  magnitude needs the level factor.
- **Structural model: MEDIUM-HIGH** (derived from n=62, internally consistent):
  - HP pools by draw rarity: medians **1,537 / 1,624 / 1,750 / 1,955** (★1→★4),
    bands 1277–1624 / 1395–1624 / 1521–1968 / 1923–2033.
  - Role ATK/DEF split (r = ATK/DEF, min/median/max): Defense **0.66/0.76/0.92**,
    Support **0.92/1.00/1.14**, Offense **1.17/1.34/1.58**, Bomber **1.38/1.55/1.75**.
    (Offense∩Bomber overlap is real; the `s=(ATK+DEF)/HP` axis separates them.)
  - Rarity ≈ uniform **×1.30** magnitude step per grade (HP and ATK+DEF both).
  - Per-level compound ≈ **×1.0189** (per-stat 1.01879/1.01852/1.01930 over 29
    steps from the `051` anchor; per-stat variation is honest, single-g is not).
  - Transcendence (grade-up) tier scalar ≈ **×1.20** per step (25 PRE pairs,
    contaminated; measured ×1.199–1.201).
  - EVCB (event combat) rows ≈ **×1.36** of archive scale — hypothesis only, CV 13.7%.
- **Best current guesstimate for a usable hero model:** a 6-row minimal
  substitution set at HP-normalized 1000 exists (`candidate-hero-bases`):
  001 Lantern 696/429 · 002 Mowgli 517/420 · 003 Nene 415/494 · 004 Tyltyl
  463/463 · 005 Gerard 387/550 · 006 Sylvester 532/375 — in-band, all
  ATK/DEF distinct, magnitude explicitly undecided.

### 3.2 Monster stats — 22 catalog monsters
**Strict coverage: 0/22 (0%)** against 16. **Confidence as base stats: LOW; as
encounter tuning: MEDIUM.**

- Episode data carries **42 monster-like rows over 22 distinct `M*` tokens** —
  but proved to be **per-appearance scripted tuning**: `M034` spans HP
  100→16,000 (160×) across four rows; identical thumb level does not predict
  STAT; only 2/22 tokens (M001, M100) follow any art-filename convention.
- Sample scripted tuples (HP/ATK/DEF @rank): M001 150/130/100; M040 400/190/100;
  M022 450/430/180; M023 700/650/160; M062 2000/1500/210; M024 2500/1800/200;
  M058 2400/2600/200; M044 5000/4000/250; M100 16000/7000/300.
- ~30 polluted HUD tokens (current-bar readings, no monster ID, no max-HP proof).
- MON BLAST! cross-title HP/ATK pairs (Snowfox etc.) quarantined — 0 credit.
- Monster rank multipliers exist shipped: hp **2.6/2.2/1.8/1.4/1.0**,
  atk/def **1.4/1.3/1.2/1.1/1.0** (rank 1→5) — [ORIGDATA], HIGH.

### 3.3 Jewels / crystals
**Best-recovered category in the corpus. Confidence: HIGH for set bonuses,
MEDIUM for instances, LOW for prices.**

- **Set bonuses 12/12 families recovered in BOTH shipped versions** ([ORIGDATA],
  1.4.4.1 help + 2.8.0.1 help, five locales): 1.4.4.1 = HP 5% / AP 5% / DP 5% /
  Crit 4.5% / Block 4.5% / Fatal 50% / Super Block 5%(KO 9%) / Element +23 /
  Resistance +23 / Speed 1.72 / Regen 30 / Penetration 12.
  2.8.0.1 = HP 6% / AP 6% / DP 6% / Speed 1.72 / Crit 6% / Fatal 60% / Element
  35 / Penetration 16 / Block 5% / Reduction 10% / Resistance 35 / Regen 30.
  One self-contradiction preserved (Super Block locale split).
- **Mounted jewel instances: 6/6 sampled Lv.15 panels transcribed** (main +
  4 substats each, e.g. Weapon ATK +29, Crit Dmg +3.13, Block 0.72, ElemRes
  1.44, BlockRes 0.50). Full crystal catalog unknown; per-star per-level crystal
  values missing entirely (Namu section empty).
- **Polish/sell/disassemble price schemas** [NATIVE]-recovered (6-field rows,
  three routes) with **zero original row values**; polish is probability-tuned
  in LEVELING.jet res-1 (ranks 2–15 curve).
- Removal fee 40,000 gold + 40 (single image, era unknown).
- Equipment gates 10/20/30/40 (+1 slot at 20) triple-sourced; 2019-09-05
  rebalance: equipment +50%, crystal mains +30%/+50%, substats +50% [official].

### 3.4 Multipliers
**Confidence: HIGH for shipped battle tuning; MEDIUM for measured combat scalars.**

- [ORIGDATA] battle tuning (LEVELING.jet chunk 9): SP first **1.5**, regen
  **0.21/s**, +**2.0**/kill, +**0.02**/attack, max **10**; role multipliers
  Bomber hp **0.85**, Support hp **0.80**, others 1.0; `atk_camp` **2.0/2.6/1.0**;
  stage bonus **1.1** ×3 for `051`.
- [NATIVE] `enemy_atk_per`/`enemy_hp_per`: **100 = 100%**, neutral (proven, and
  prevents a classic "100×" misread).
- Transcendence stat multiplier at T3: measured **×1.30** (Hermes exactly 3/3
  fields), flat ladder fits 8/9; cumulative ×1.716 hypothesis **refuted**; T1/T2
  per-step ×1.10/×1.20 **untested**. Do not implement.
- Power↔stats law: best-fit 12-weight OLS **R²=0.996** but portal-derived,
  not a recovered formula; one exactly-determined integer:
  `block_damage_reduction` = 18 cp units (portal-derived).
- Skill-effect magnitudes: **0/230 recovered numerically** — magnitudes live in
  formula strings (e.g. `-1*(stat*(8+2*rank))*(value+value_up*skill_level)/10000`)
  with coefficient columns unrecovered; two live skill samples (Crocus enemy-Max-HP
  8.75%→9.00%; Lawrence DEF 20%, Leon Summer HP 13%) are polluted pixels.

### 3.5 Rewards
**Confidence: HIGH for declarations/mechanisms; LOW for amounts.**

- [ORIGDATA] **all 18 Episode chapter reward declarations** (E01 GC2×3 …
  E18 RP1×100,000); four settlements implemented, 15 chapters unimplemented
  against *known* declarations.
- [NATIVE] star mechanism: 3 conditions per stage, chest thresholds
  **10/20/30** = area stage-count × (i+1); defeat does **not** consume fuel
  ([ORIGDATA] help, 4 locales). Chest *amounts* unknown.
- [IMAGE-pixel] original payouts: Search +1,400/+2,000/+2,000 rupees with item
  lists; co-op +21,000; recruitment mileage 3/10/25/40 (sum 78).
- [COMM multi-source] grade EXP-to-max ladder **200/400/1,200/4,800/24,000**
  (= 200·R!), 3–6 sources per rung; local 2,900 fixture contradicted 8–14×.
- [COMM×4] cruise rate **11 EXP per 6 fuel** (levels 36–40).
- All first-clear gold/EXP, per-stage payouts, per-star conditions: **14
  documented unknowns** (`rewards-economy` §D) — replica values are fixtures.

### 3.6 Prices / economy
**Confidence: HIGH for gacha; MEDIUM for training/episode; LOW for shops/arena.**

Verified against the fixture-conflict audit (91 rows): **26 CORROBORATED /
4 CONTRADICTED / 3 UNCONTRADICTED / 58 UNSUPPORTED** (the file's own headline
says 29/~78; the strict table count is 26/58).

| System | Corroborated | Unsupported | Confidence |
|---|---:|---:|---|
| Gacha (F) | 4 (prices 30/300, counts 1/11, ★3+ guarantee, result shape) | 3 (pools/pity/probabilities) | **HIGH** |
| Skill training (A) | 4 (50-row price vector shape, caps 10/20/30/40/50, zero-init, 5 slots) | 0 (but 3 CONTRADICTED: gold formula, materials-from-Lv5 ladder, fragments) | MEDIUM (values LOW) |
| Training/RankUp (B) | 4 (cap 30, materials=current rank, 5-partner max, fodder whitelist) | 9 | MEDIUM mechanism / LOW values |
| Campaign rewards (C) | 3 | 11 | LOW |
| Episode (D) | 6 | 4 | MEDIUM-HIGH |
| Search/traces (E) | 2 | 8 (1 CONTRADICTED: trace thresholds 10/20 vs 20/40) | LOW |
| AP/BP/Supply (G) | 1 (shared buy-limit shape) | 8 | LOW |
| Arena/Fight Club (H) | **0** | **8** | **LOWEST** |
| Battle numerics (I) | 2 (percentage semantics, enums) | 7 | LOW |

**Strongest recovered price points:**
- Gacha **30 / 300** single/10+1, counts 1 and 11 only, ★3+ bundle guarantee —
  [NATIVE]+[COMM], multi-source.
- Skill training **800 rupees** + materials 4/4/2 at Lv.35 (pixel, PRE);
  community band ladder **100→1,000** rupees contradicts the local 100×level
  formula (agree at L1 only) — [COMM×2].
- Rank-up **8,000/12,000** rupees (2/3 fodder) pixel vs local 1,000/source —
  scale flagged 8–12× off, no per-source anchor.
- Transcendence **9,000 rupees** + 9 gems/90 crystals (pixel); two-source
  cost ladder 5/50/5,000 → 110/1,100 across grades (39 shared cells, 2 sites).
- Equipment Lv.49→50: **50,000** + 320/27 toolboxes (pixel).
- Jewel removal **40,000** gold + 40 (pixel).
- Fight Club: tier rewards 100–200 chips + 2 Manda, scoring +15/−8, 31-band
  rank table to 30,000+ — [COMM], single-source mostly, **zero native value
  agreement** (9 documented gaps).
- GvG: 12 shipped help numerals (150 deploy, 25 clear, +50/+25 attacks, ×5
  per hunter, 2,250/occupied area, +50 defense team) — [ORIGDATA].

---

## 4. Proven negatives (do not re-attempt — SYNTHESIS §5, 31 items)

Highlights: no embedded per-entity stat tables in any APK (stats were
server-side); the 2019 JP archive is a **closed set** (0 new rows on re-fetch);
help corpora contain **no cost tables** (95+73 records swept, 20 patterns,
zero hits); monster base stats from battle HUD are **exhausted**; accessory/
jewel image search **exhausted by name collision**; audio/dialogue surfaces
carry **zero numerals**; `attr_resist: 99` is a sentinel, not a value.

## 5. Honest bottom line

| Category | Strict completeness | Usable-model completeness | Confidence |
|---|---|---|---|
| Hero base stats | 1/113 (0.9%) | ~73/113 identity + 62 numeric tuples + full shape model | Identity HIGH / values MEDIUM-LOW |
| Monster stats | 0/22 (0%) | 42 scripted encounter rows, 0 base tuples | LOW (base) / MEDIUM (tuning) |
| Jewel set bonuses | 12/12 families, both versions | 100% | **HIGH** |
| Jewel instances/prices | 6/6 samples; 0 price rows | Sample only | MEDIUM / LOW |
| Multipliers | Shipped tuning fully in hand | ~95% of battle model (wire growth + attack-speed unit now [NATIVE]) | HIGH (shipped) / MEDIUM (measured) |
| Rewards | 18/18 declarations, mechanisms | ~40% (amounts missing) | MEDIUM |
| Prices/economy | 26/91 fixture rows corroborated | ~29% | Gacha HIGH → Arena LOW |

The corpus is **structurally asymmetric**: what shipped inside the client
(help text, Episode data, tuning) is recovered at HIGH confidence; what lived
on the original server (base stats, per-stage rewards, shop/arena prices,
gacha pools) is mostly unrecoverable except through the 2019 archive — which
supplies 62 of 113 hero tuples at POST-rebalance magnitude, the single
largest stat asset in the workspace, and it is now proven closed.
---

# APPENDIX — the guesstimate tables (2026-10-06)

**How to read the confidence columns.** `Conf%` = estimated probability that the row's core numbers (HP/ATK/DEF and, where present, the other published fields) sit within ±10% of the original game's values in the stated context. Word scale: **HIGH** >=75, **MEDIUM** 50–74, **LOW** 25–49, **VERY LOW** <25, **CONTESTED** = two sources disagree (word carries the row regardless of %). Evidence classes: [ORIGDATA] shipped client data, [NATIVE] parser evidence, [COMM] community, [PIXEL] original-game pixels, [DERIVED] computed here from the corpus priors (never a source by itself).

Every derived number below is a **guesstimate for reconstruction**, not recovered data. Era rule: anything dated before 2019-09-05 is PRE-rebalance; the 2019 JP archive rows are POST; the two eras must never be merged into one table without a scale bridge.

## A. Per-hero stat guesstimates — all 113 catalog characters (121 rows incl. awakened)

Core sources: 2019 JP archive (62 numeric rows, POST-era) > Episode STAT (scripted, rank>1 usually) > derived priors. Column order: identity, core tuple, substats, confidence.

| ID | Name | Title | Draw★ | Role | Elem | HP | ATK | DEF | CP | SPD | Crit% | CritDmg% | Pen | Block% | BlockRes | EEnh | ERes | HPReg | Conf% | Word | Notes |
|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 001 | Lantern | First Ever Hunter | 3 | Bomber | Fire | 1521 | 1058 | 653 | 8359 | 7 | 14 | 180 | 0 | 14 | 42 | 0 | 0 | 38 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 390/200/180@r4; 3700/3800/240@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums / NATIVE-VERIFIED display at owned Lv4: 1561/1062/657/SPD7 (§159) |
| 002 | Mowgli | Forgotten Forest | 2 | Offense | Lightning | 1624 | 839 | 682 | 8587 | 8 | 33 | 200 | 0 | 14 | 42 | 0 | 0 | 41 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / NATIVE-VERIFIED display at owned Lv3: 1654/842/685/SPD8 (§159) |
| 003 | Nene | Walking Disaster | 3 | Defense | Ice | 1750 | 726 | 864 | 9371 | 7 | 14 | 180 | 0 | 33 | 50 | 0 | 0 | 48 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 525/160/250@r4; 514/333/394@r3; 4500/3300/280@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums / NATIVE-VERIFIED display at owned Lv3: 1780/729/867/SPD7 (§159) |
| 004 | Tyltyl | World's Best Cook | 1 | Support | Fire | 1467 | 679 | 679 | 6664 | 7 | 14 | 180 | 0 | 14 | 42 | 0 | 0 | 37 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2000/1000/900@r5; 2700/1200/1100@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums / NATIVE-VERIFIED display at owned Lv9: 1557/688/688/SPD7 (§159) |
| 004_1 | Tyltyl (Awakened) | Legendary Chef | 5 | Support | Fire | 2542 | 1155 | 1155 | 14979 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 40.0 | 2.0 | 2.0 | 43.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2000/1000/900@r5; 2700/1200/1100@r5 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 005 | Gerard | Invincible One | 2 | Defense | Ice | 1624 | 628 | 893 | 8567 | 7 | 14 | 180 | 0 | 33 | 52 | 0 | 0 | 41 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2600/1200/1400@r5; 1000/280/260@r2; 310/210/290@r2 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 005_1 | Gerard (Awakened) | Indomitable Warrior | 5 | Defense | Ice | 2542 | 1019 | 1333 | 16075 | 7.0 | 14.0 | 180.0 | 0.0 | 33.0 | 50.0 | 0.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2600/1200/1400@r5; 1000/280/260@r2; 310/210/290@r2 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 006 | Sylvester | Undying Soldier | 1 | Offense | Fire | 1537 | 817 | 576 | 7558 | 8 | 33 | 200 | 0 | 14 | 42 | 0 | 0 | 38 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 3600/3200/240@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 007 | Metis | Fiery Soul | 1 | Bomber | Fire | 1277 | 908 | 576 | 6624 | 7 | 14 | 180 | 0 | 14 | 40 | 0 | 0 | 36 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2300/1400/200@r4 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 008 | Akasha | Maiden of Gods | 3 | Support | Lightning | 1710 | 762 | 762 | 8081 | 7 | 14 | 185 | 0 | 14 | 40 | 0 | 0 | 43 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 3600/2800/240@r5; 2400/1000/1100@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 009 | Captain | Captain | 1 | Defense | Lightning | 1624 | 628 | 893 | 8567 | 7 | 14 | 180 | 1 | 33 | 52 | 0 | 0 | 41 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2400/1000/1100@r5; 4000/1300/2000@r5; 5000/1400/2100@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 009_1 | Captain (Awakened) | Eternal Flame | 5 | Defense | Fire | 2542 | 1019 | 1333 | 16075 | 7.0 | 14.0 | 180.0 | 0.0 | 33.0 | 50.0 | 0.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2400/1000/1100@r5; 4000/1300/2000@r5; 5000/1400/2100@r5 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 010 | Vincent | Renegade | 4 | Offense | Lightning | 1923 | 1032 | 718 | 11252 | 8 | 30 | 200 | 1 | 30 | 42 | 0 | 0 | 48 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / 4-star: gear-eligibility risk (gear unlocks at 4-star+) - gear contamination not excluded for 5 live rows / Episode scripted tuples: 5000/2200/1800@r5; 5000/2200/1800@r5; 2000/120/160@r4 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 010_1 | Vincent (Awakened) | Despair of a Millennium | 5 | Offense | Ice | 2542 | 1338 | 999 | 15777 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 5000/2200/1800@r5; 5000/2200/1800@r5; 2000/120/160@r4 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 011 | Hecate | Protector | 1 | Defense | Fire | 1537 | 576 | 817 | 7620 | 7 | 14 | 180 | 0 | 33 | 52 | 0 | 0 | 38 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 3300/900/250@r4; 2400/1000/1250@r5; 4500/2800/250@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 011_1 | Hecate (Awakened) | Counterattack Flame | 5 | Defense | Fire | 2542 | 1019 | 1333 | 16075 | 7.0 | 14.0 | 180.0 | 0.0 | 33.0 | 50.0 | 0.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 3300/900/250@r4; 2400/1000/1250@r5; 4500/2800/250@r5 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 012 | Karl Steiner | Immortal One | 3 | Offense | Lightning | 1750 | 1007 | 689 | 9851 | 7 | 33 | 205 | 0 | 14 | 40 | 0 | 0 | 44 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2500/850/220@r4; 1150/750/550@r4; 1150/750/533@r4 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 013 | Denali | Clean Fairy | 2 | Support | Fire | 1584 | 755 | 682 | 7293 | 7 | 14 | 180 | 0 | 14 | 40 | 2 | 2 | 40 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 3000/1200/1300@r5; 1300/500/160@r3 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 014 | Locke | Locke and Cash CEO | 1 | Bomber | Ice | 1277 | 908 | 576 | 6653 | 7 | 14 | 180 | 0 | 14 | 42 | 0 | 0 | 32 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 3700/4200/240@r5; 3200/2800/220@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 015 | Levi | Lieutenant | 2 | Bomber | Ice | 1395 | 1014 | 580 | 7370 | 7 | 14 | 185 | 0 | 14 | 40 | 0 | 0 | 35 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 016 | Bruce Bang | Death Metal Preacher | 1 | Support | Ice | 1467 | 660 | 715 | 6716 | 7 | 14 | 180 | 0 | 14 | 40 | 2 | 2 | 37 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2400/1000/220@r4; 8600/2200/250@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 017 | Lapis | Speedy Swordsman | 1 | Offense | Ice | 1537 | 854 | 540 | 7495 | 8 | 33 | 205 | 0 | 14 | 40 | 0 | 0 | 38 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 9000/2400/240@r5; 2100/1200/950@r5; 1500/280/180@r4 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 017_1 | Lapis (Awakened) | Supersonic Swordsman | 5 | Offense | Ice | 2542 | 1338 | 999 | 15777 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 9000/2400/240@r5; 2100/1200/950@r5; 1500/280/180@r4 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 018 | Robin | King of Survival | 1 | Defense | Ice | 1537 | 642 | 751 | 7716 | 7 | 14 | 180 | 0 | 33 | 52 | 0 | 0 | 38 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 4500/2900/230@r5; 3100/1000/240@r4 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 019 | Balian | Wandering Swordsman | 1 | Offense | Lightning | 1537 | 817 | 576 | 7574 | 8 | 33 | 205 | 0 | 14 | 40 | 0 | 0 | 38 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 3800/3200/240@r5; 2200/1200/950@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 019_1 | Balian (Awakened) | Thunderbringer | 5 | Offense | Lightning | 2542 | 1338 | 999 | 15777 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 3800/3200/240@r5; 2200/1200/950@r5 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 020 | Sienna | Firepower Maniac | 1 | Bomber | Lightning | 1277 | 944 | 540 | 6565 | 7 | 14 | 180 | 0 | 14 | 42 | 0 | 0 | 32 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 4500/3300/260@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 020_1 | Sienna (Awakened) | Railgun Shooter | 5 | Bomber | Lightning | 2542 | 1754 | 1135 | 18038 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 42.0 | 0.0 | 0.0 | 38.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 4500/3300/260@r5 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 021 | Rebecca | Twilight Bat Clan | 2 | Offense | Fire | 1624 | 893 | 580 | 8122 | 8 | 33 | 200 | 0 | 14 | 40 | 0 | 0 | 45 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 450/180/200@r4; 4100/2600/260@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 021_1 | Rebecca (Awakened) | Raging Flames of Iron | 5 | Offense | Fire | 2542 | 1338 | 999 | 15777 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 450/180/200@r4; 4100/2600/260@r5 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 022 | Sunny | Experiment 2 | 2 | Support | Ice | 1584 | 718 | 718 | 7329 | 7 | 14 | 180 | 0 | 14 | 42 | 0 | 0 | 40 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 023 | Hermes | Elite Messenger | 3 | Offense | Fire | 1750 | 937 | 653 | 9177 | 8 | 33 | 200 | 0 | 14 | 40 | 2 | 2 | 44 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 5000/1400/1300@r5; 2800/1600/1100@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 024 | Riko | Hard-Knock Life | 2 | Defense | Lightning | 1624 | 682 | 821 | 8552 | 7 | 14 | 185 | 0 | 33 | 50 | 0 | 0 | 41 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 5000/2400/280@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 024_1 | Riko (Awakened) | Sparkling Blade Claws | 5 | Defense | Lightning | 2542 | 1019 | 1333 | 16075 | 7.0 | 14.0 | 180.0 | 0.0 | 33.0 | 50.0 | 0.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 5000/2400/280@r5 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 025 | Teddy Bomber | Teddy Bear Terrorist | 2 | Bomber | Fire | 1395 | 978 | 646 | 7656 | 7 | 14 | 180 | 0 | 14 | 42 | 0 | 0 | 35 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 026 |  | In Wonderland | 1 | Support | Lightning | 1467 | 679 | 679 | 6664 | 7 | 14 | 180 | 0 | 14 | 42 | 0 | 0 | 37 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 026_1 |  | In Wonderland |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 10 | VERY LOW | rarity unresolved - magnitude cannot even be banded / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 027 | Athena | Flame of Battlefield | 3 | Defense | Fire | 1750 | 689 | 901 | 9322 | 7 | 14 | 180 | 0 | 33 | 50 | 5 | 5 | 48 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2500/1100/1200@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 028 | Octavia | Frost Witch | 3 | Offense | Ice | 1750 | 901 | 689 | 9304 | 8 | 33 | 205 | 0 | 14 | 40 | 5 | 5 | 44 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2000/1200/900@r5; 4300/3800/240@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 029 | Kain | Steely Bodyguard | 3 | Defense | Lightning | 1790 | 689 | 1007 | 10229 | 7 | 14 | 185 | 0 | 36 | 55 | 5 | 5 | 45 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2200/800/1000@r5; 5000/1050/850@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 030 | Acerola | Biologist | 2 | Support | Lightning | 1584 | 718 | 718 | 7321 | 7 | 14 | 185 | 0 | 14 | 40 | 0 | 0 | 40 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 5500/3600/270@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 031 | Diana | Thunder Arrow | 3 | Bomber | Lightning | 1521 | 1021 | 689 | 8401 | 7 | 14 | 180 | 0 | 14 | 40 | 5 | 5 | 38 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 032 | Scar | Wandering Fighter | 2 | Offense | Ice | 1624 | 839 | 682 | 8550 | 8 | 33 | 200 | 0 | 14 | 40 | 0 | 0 | 45 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2300/1300/1100@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 033 | Patrone | Silent Canine | 3 | Bomber | Ice | 1521 | 1003 | 726 | 8580 | 7 | 14 | 185 | 0 | 14 | 40 | 5 | 5 | 38 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 034 |  | Halloween Witch | 2 | Defense | Ice | 1624 | 682 | 821 | 8552 | 7 | 14 | 185 | 0 | 33 | 50 | 0 | 0 | 41 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2000/850/1000@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 034_1 |  | Halloween Witch |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 10 | VERY LOW | rarity unresolved - magnitude cannot even be banded / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 035 | Joy | Walking Infirmary | 3 | Support | Fire | 1710 | 828 | 726 | 8236 | 7 | 14 | 180 | 0 | 14 | 42 | 5 | 5 | 43 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 036 | Bear | Nature's Gift | 3 | Defense | Lightning | 1923 | 755 | 864 | 10011 | 7 | 14 | 180 | 0 | 33 | 50 | 5 | 5 | 32 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2700/1000/1000@r5; 2500/1000/1000@r5; 1700/330/220@r3 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 037 | Natalia | Noble Spear | 3 | Offense | Ice | 1750 | 883 | 755 | 9909 | 8 | 33 | 205 | 0 | 20 | 40 | 5 | 5 | 44 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 038 | Rebecca (Christmas) | Santa Girl | 3 | Offense | Fire | 1790 | 992 | 668 | 9666 | 8 | 33 | 200 | 0 | 14 | 40 | 5 | 5 | 48 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2700/1400/1100@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 038_1 |  | Twilight Santa Girl |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 10 | VERY LOW | rarity unresolved - magnitude cannot even be banded / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 039 | Gullveig | Airport Officer | 3 | Bomber | Lightning | 1521 | 1021 | 689 | 8437 | 7 | 14 | 180 | 0 | 14 | 42 | 5 | 5 | 38 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2200/1200/1000@r5; 3200/2800/230@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 040 | Bibi | Wolf Child | 3 | Offense | Lightning | 1750 | 883 | 755 | 9888 | 8 | 33 | 200 | 0 | 20 | 42 | 5 | 5 | 44 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 4000/900/240@r5; 2400/1100/1000@r5; 6500/4300/230@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 041 | Edward | Robot Engineer | 3 | Defense | Lightning | 1821 | 718 | 901 | 9495 | 7 | 14 | 180 | 0 | 30 | 45 | 5 | 5 | 46 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 20000/1900/280@r5; 6500/3100/280@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 042 | Santa Clauster | Santa Clauster | 3 | Offense | Fire | 1821 | 937 | 689 | 9659 | 8 | 33 | 200 | 0 | 14 | 42 | 5 | 5 | 44 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2800/1500/1200@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 043 | Papillon | Notorious Jail-breaker | 3 | Defense | Ice | 1606 | 726 | 792 | 8261 | 7 | 14 | 185 | 0 | 33 | 30 | 5 | 5 | 44 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 4600/3300/270@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 044 | Heidi | Girl with Two Faces | 3 | Offense | Fire | 1750 | 952 | 689 | 9764 | 8 | 33 | 200 | 0 | 20 | 40 | 5 | 5 | 44 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 045 | Yuri | Ice Skating Fairy | 3 | Offense | Ice | 1750 | 937 | 718 | 9635 | 8 | 33 | 200 | 0 | 14 | 40 | 5 | 5 | 44 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 046 | Harley | Man of Justice | 4 | Defense | Ice | 2033 | 755 | 1036 | 11534 | 7 | 20 | 180 | 0 | 33 | 50 | 5 | 5 | 51 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / 4-star: gear-eligibility risk (gear unlocks at 4-star+) - gear contamination not excluded for 5 live rows / Episode scripted tuples: 3600/1400/1100@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 047 | Lily & Lyla | Strange Twins | 4 | Offense | Fire | 1923 | 996 | 755 | 10679 | 8 | 33 | 200 | 0 | 14 | 40 | 5 | 5 | 48 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / 4-star: gear-eligibility risk (gear unlocks at 4-star+) - gear contamination not excluded for 5 live rows |
| 048 | Dumble | Strange Old Man | 3 | Defense | Ice | 1750 | 689 | 901 | 9322 | 6 | 14 | 180 | 1 | 33 | 50 | 5 | 5 | 44 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 049 | Bright | Little Match Boy | 3 | Support | Fire | 1710 | 828 | 755 | 8403 | 7 | 14 | 180 | 0 | 14 | 42 | 5 | 5 | 43 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 1800/900/800@r5; 900/300/140@r3; 600/356/333@r3 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 050 | Therapy | Diabolic Physiotherapist | 3 | Support | Ice | 1710 | 825 | 762 | 8428 | 7 | 14 | 180 | 0 | 14 | 42 | 5 | 5 | 43 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 051 | Beckhen | Guardian of Fight Club | 3 | Offense | Ice | 1678 | 864 | 660 | 8709 | 8 | 33 | 200 | 0 | 14 | 42 | 5 | 5 | 42 | 85 | HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / ONLY strict row: archive cross-validates the Lv.30 no-equipment panel (2879/1471/1149); gear-invariance shown, shape drift <=2.2% / Episode scripted tuples: 2400/1100/1000@r5; 2400/1100/1000@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 052 | Windblade | Windy Soul | 4 | Offense | Lightning | 1955 | 992 | 835 | 11504 | 8 | 33 | 205 | 0 | 14 | 45 | 5 | 5 | 49 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / 4-star: gear-eligibility risk (gear unlocks at 4-star+) - gear contamination not excluded for 5 live rows / Episode scripted tuples: 6000/2100/240@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 053 | Calibur | Revenant | 3 | Defense | Fire | 1750 | 846 | 1284 | 10162 | 7 | 0 | 50 | 0 | 0 | 50 | 5 | 5 | 48 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 054 | Dino | Genius Climatologist | 3 | Bomber | Ice | 1560 | 1029 | 744 | 8921 | 7 | 14 | 180 | 0 | 14 | 42 | 5 | 5 | 39 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2400/1600/1200@r5; 2700/1800/1100@r5; 7500/2700/210@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 055 | Apollon | Singing Poet | 3 | Bomber | Fire | 1560 | 1054 | 708 | 8767 | 7 | 14 | 180 | 0 | 14 | 40 | 5 | 5 | 43 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2000/1200/900@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 056 | Genovia | Atoner | 4 | Offense | Ice | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | 5 | VERY LOW | archive page renders ??? placeholders (Genovia) - no numeric transcription exists / Episode scripted tuples: 3000/1600/1000@r5; 3400/1800/1450@r5; 7000/2800/260@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 056_1 | Genovia (Awakened) | Condemner | 5 | Offense | Ice | 2542 | 1338 | 999 | 15777 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 3000/1600/1000@r5; 3400/1800/1450@r5; 7000/2800/260@r5 / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 057 | Pansy | Animal Lover | 3 | Support | Ice | 1742 | 762 | 806 | 8394 | 7 | 14 | 185 | 0 | 14 | 40 | 5 | 5 | 44 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 4500/3800/240@r5; 2400/1000/900@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 058 | Crocus | Necromancer | 3 | Support | Lightning | 1710 | 806 | 806 | 8535 | 7 | 14 | 180 | 0 | 14 | 40 | 5 | 5 | 47 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 2300/1100/1100@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 059 | Lantern (Halloween) | Jack O' Lantern | 3 | Bomber | Fire | 1521 | 1058 | 653 | 8359 | 7 | 14 | 180 | 0 | 14 | 42 | 0 | 0 | 38 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 1700/1300/600@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 060 | Denali (Halloween) | Broom Witch | 3 | Support | Fire | 1710 | 828 | 726 | 8200 | 7 | 14 | 180 | 0 | 14 | 40 | 0 | 0 | 43 | 75 | MEDIUM-HIGH | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / Episode scripted tuples: 1800/800/700@r5 / identity cross-check: role 99/100, element 94/100 agreement between archive and Episode enums |
| 061 | Chichi | Girl with Super Strength | 3 | Offense | Lightning | 1821 | 937 | 798 | 10148 | 8 | 33 | 200 | 0 | 14 | 40 | 5 | 5 | 51 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 062 | Juno | Aircraft Mechanic | 3 | Defense | Fire | 1968 | 743 | 1125 | 11556 | 7 | 14 | 180 | 0 | 33 | 52 | 0 | 10 | 46 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished |
| 063 | Erise | Prestigious Tailor | 4 | Defense | Lightning | 2019 | 933 | 1070 | 12725 | 7 | 14 | 180 | 0 | 33 | 52 | 0 | 10 | 48 | 65 | MEDIUM | 2019 JP archive [ORIGDATA-web]; POST-2019-09-05 era; level unstated (approx Lv.1 per 051 anchor x1.716 over 29 levels); gear state unestablished / 4-star: gear-eligibility risk (gear unlocks at 4-star+) - gear contamination not excluded for 5 live rows |
| 064 | Geranium | Artifact Collector | 4 | Bomber | Lightning | 1955 | 1349 | 873 | 12608 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 42.0 | 0.0 | 0.0 | 38.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2700/1600/850@r5; 2800/1900/1400@r5 |
| 065 | Teresa | Runaway Bride | 4 | Support | Fire | 1955 | 888 | 888 | 10238 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 40.0 | 2.0 | 2.0 | 43.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 066 | Mary | Little Reaper | 4 | Offense | Fire | 1955 | 1029 | 768 | 11027 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 067 | Judith | Red Shadow | 4 | Bomber | Fire | 1955 | 1349 | 873 | 12608 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 42.0 | 0.0 | 0.0 | 38.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 068 | Selene | White Darkness | 4 | Bomber | Ice | 1955 | 1349 | 873 | 12608 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 42.0 | 0.0 | 0.0 | 38.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2600/1700/850@r5; 2000/1300/800@r5; 2800/2500/1200@r5 |
| 069 | Celine | Diva of Midgard | 4 | Support | Ice | 1955 | 888 | 888 | 10238 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 40.0 | 2.0 | 2.0 | 43.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2600/1100/1200@r5 |
| 070 | Alia | Electrotherapist | 4 | Support | Lightning | 1955 | 888 | 888 | 10238 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 40.0 | 2.0 | 2.0 | 43.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2000/1000/900@r5 |
| 071 | Anemone | Great General | 4 | Defense | Fire | 1955 | 784 | 1025 | 11262 | 7.0 | 14.0 | 180.0 | 0.0 | 33.0 | 50.0 | 0.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 14000/2300/280@r5 |
| 072 | Audrey | Dangerous Gambler | 4 | Bomber | Lightning | 1955 | 1349 | 873 | 12608 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 42.0 | 0.0 | 0.0 | 38.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2300/1200/1000@r5; 1800/1200/700@r5 |
| 073 | Sofia | Fantastic Light | 4 | Support | Fire | 1955 | 888 | 888 | 10238 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 40.0 | 2.0 | 2.0 | 43.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 074 | Leon | Veteran Army Surgeon | 4 | Support | Ice | 1955 | 888 | 888 | 10238 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 40.0 | 2.0 | 2.0 | 43.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 075 | Bella | Dancing Sword | 4 | Offense | Ice | 1955 | 1029 | 768 | 11027 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 076 | Junia | Prayer | 4 | Defense | Ice | 1955 | 784 | 1025 | 11262 | 7.0 | 14.0 | 180.0 | 0.0 | 33.0 | 50.0 | 0.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 077 | Blondie | Gunslinger | 4 | Bomber | Fire | 1955 | 1349 | 873 | 12608 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 42.0 | 0.0 | 0.0 | 38.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 078 | Teresa (Halloween) | Ghost Bride | 4 | Support | Ice | 1955 | 888 | 888 | 10238 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 40.0 | 2.0 | 2.0 | 43.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2200/1000/1000@r5 |
| 079 | Lawrence | Defense Knight | 4 | Defense | Fire | 1955 | 784 | 1025 | 11262 | 7.0 | 14.0 | 180.0 | 0.0 | 33.0 | 50.0 | 0.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 080 | Westfield | Legendary Coach | 4 | Support | Lightning | 1955 | 888 | 888 | 10238 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 40.0 | 2.0 | 2.0 | 43.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2300/1000/1200@r5 |
| 081 | Monica | Master of Counterattack | 4 | Defense | Lightning | 1955 | 784 | 1025 | 11262 | 7.0 | 14.0 | 180.0 | 0.0 | 33.0 | 50.0 | 0.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 082 | Mary (Christmas) | Little Santa | 4 | Offense | Lightning | 1955 | 1029 | 768 | 11027 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 30 | LOW | NO numeric source; core = rarity-HP median x role r/s priors (n=62 archive); substats = role medians; CP via approximate law (R2=0.996, coarse) / Episode scripted tuple exists: 2700/1450/1150@r5 |
| 083 | Kamala | Leader of the White Forest | 4 | Defense | Ice | 1955 | 784 | 1025 | 11262 | 7.0 | 14.0 | 180.0 | 0.0 | 33.0 | 50.0 | 0.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 084 | Lottery Mouse | Master of Recruitment | 4 | Bomber | Ice | 1955 | 1349 | 873 | 12608 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 42.0 | 0.0 | 0.0 | 38.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 085 |  | Lunar New Year |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 10 | VERY LOW | rarity unresolved - magnitude cannot even be banded |
| 086 | Genovia (Valentine) | Valentine | 4 | Offense | Fire | 1955 | 1029 | 768 | 11027 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 086_1 |  | Valentine Condemner |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 10 | VERY LOW | rarity unresolved - magnitude cannot even be banded / awakened variant: 5-star extrapolation = 1955 x 1.30; awakened-element rule holds 9/11 (82%) |
| 087 |  | Florist Lady |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 10 | VERY LOW | rarity unresolved - magnitude cannot even be banded |
| 088 |  | Florist |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 10 | VERY LOW | rarity unresolved - magnitude cannot even be banded |
| 089 | Clara | Post Office Supervisor | 4 | Support | Lightning | 1955 | 888 | 888 | 10238 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 40.0 | 2.0 | 2.0 | 43.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 090 | Katrina | Owner of Saw Blade | 4 | Offense | Lightning | 1955 | 1029 | 768 | 11027 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 091 | Anemone (Kid) | Little General | 4 | Defense | Lightning | 1955 | 784 | 1025 | 11262 | 7.0 | 14.0 | 180.0 | 0.0 | 33.0 | 50.0 | 0.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 092 | Themis | Monster Sniper | 4 | Bomber | Fire | 1955 | 1349 | 873 | 12608 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 42.0 | 0.0 | 0.0 | 38.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 093 | Bella (Summer) | Midsummer Sword Dancer | 4 | Offense | Fire | 1955 | 1029 | 768 | 11027 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 094 | Leon (Summer) | Lifeguard | 4 | Support | Lightning | 1955 | 888 | 888 | 10238 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 40.0 | 2.0 | 2.0 | 43.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 095 |  | Knight of Swimming Pool |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 10 | VERY LOW | rarity unresolved - magnitude cannot even be banded |
| 096 | Estelle | Midgard’s Finest Sword | 4 | Offense | Fire | 1955 | 1029 | 768 | 11027 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 097 | Lily & Lyla (Christmas) | Santa Twins | 4 | Offense | Lightning | 1955 | 1029 | 768 | 11027 | 8.0 | 33.0 | 200.0 | 0.0 | 14.0 | 40.0 | 5.0 | 5.0 | 44.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |
| 098 | Selene (Valentine) | Valentine | 4 | Bomber | Lightning | 1955 | 1349 | 873 | 12608 | 7.0 | 14.0 | 180.0 | 0.0 | 14.0 | 42.0 | 0.0 | 0.0 | 38.0 | 20 | VERY LOW | NO numeric source anywhere; core = rarity-HP median x role r/s priors; substats = role medians; CP via approximate law |

_113 rows. 62 carry 2019-archive numbers (806 source cells), 13 are two-source shape-confirmed, ~45 are derived priors, ~6 Episode-only, 1 placeholder (056)._

## A.2 Native-verified live display stats — owned hunters (2026-10-08)

Rendered in the instrumented client against the deployed archive-2019
projection; detail view and BuildTeam agree, and these exact stats fought and
won CB0102/CB0103/CB0201/CB0202/CB0301 (§159–§165). These verify the **display
pipeline and the base+up×level formula**, not original magnitudes — the
per-level growth increments are fixtures.

| Ref | Hero | Owned level | HP | ATK | DEF | SPD | Conf% | Word | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 001 | Lantern | 4 | 1561 | 1062 | 657 | 7 | 85 | HIGH | native detail view + BuildTeam (§159); growth +10/+1/+1 per level is a fixture |
| 002 | Mowgli | 3 | 1654 | 842 | 685 | 8 | 85 | HIGH | same pipeline proof (§159) |
| 003 | Nene | 3 | 1780 | 729 | 867 | 7 | 85 | HIGH | same pipeline proof (§159) |
| 004 | Tyltyl | 9 | 1557 | 688 | 688 | 7 | 85 | HIGH | same pipeline proof (§159) |

Native BuildTeam strength across the full four-hunter party: **25904**
(§159). Wins §160–§165 were fought with exactly these numbers — local
projection playability is proven; original balance is NOT claimed.

## B. Episode scripted hunter tuples — every hunter-typed row (117 rows / 54 heroes)

These are per-appearance story tuning, NOT base stats. Kept complete because they are the only shipped numeric pairing of a hero identity with HP/ATK/DEF.

| Combat ID | Hero ref | res_id | Rank | HP | ATK | DEF | SPD | Crit | CritDmg | Pen | Block | BlockRes | EEnh | ERes | HPReg | Conf% | Word | Notes |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| EVCB0201_042 | 042 Santa Clauster | C042 | 5 | 2800 | 1500 | 1200 | 8.00 | 58.00 | 224 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_038 | 038 Rebecca (Christmas) | C038 | 5 | 2700 | 1400 | 1100 | 8.00 | 33.00 | 300 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_082 | 082 Mary (Christmas) | C082 | 5 | 2700 | 1450 | 1150 | 8.00 | 33.00 | 240 | 0.00 | 20.00 | 50 | 5 | 99 | 65 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_023 | 023 Hermes | C023 | 5 | 5000 | 1400 | 1300 | 7.00 | 33.00 | 224 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_013 | 013 Denali | C013 | 5 | 3000 | 1200 | 1300 | 7.00 | 14.00 | 210 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_005 | 005 Gerard | C005 | 5 | 2600 | 1200 | 1400 | 7.00 | 14.00 | 204 | 0.00 | 33.00 | 50 | 0 | 10 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_032 | 032 Scar | C032 | 5 | 2300 | 1300 | 1100 | 8.00 | 33.00 | 224 | 0.00 | 70.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_080 | 080 Westfield | C080 | 5 | 2300 | 1000 | 1200 | 7.00 | 14.00 | 204 | 0.00 | 33.00 | 50 | 0 | 10 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_051 | 051 Beckhen | C051 | 5 | 2400 | 1100 | 1000 | 8.00 | 33.00 | 224 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_051A | 051 Beckhen | C051A | 5 | 2400 | 1100 | 1000 | 8.00 | 33.00 | 224 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_039 | 039 Gullveig | C039 | 5 | 2200 | 1200 | 1000 | 7.00 | 14.00 | 204 | 0.00 | 14.00 | 40 | 10 | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_072 | 072 Audrey | C072 | 5 | 2300 | 1200 | 1000 | 7.00 | 14.00 | 204 | 0.00 | 14.00 | 40 | 10 | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_027B | 027 Athena | C027B | 5 | 2500 | 1100 | 1200 | 7.00 | 14.00 | 204 | 0.00 | 70.00 | 50 | 0 | 10 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_009 | 009 Captain | C009 | 5 | 2400 | 1000 | 1100 | 7.00 | 14.00 | 204 | 20.00 | 33.00 | 50 | 0 | 10 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_055B | 055 Apollon | C055B | 5 | 2000 | 1200 | 900 | 7.00 | 14.00 | 204 | 0.00 | 14.00 | 40 | 10 | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_070 | 070 Alia | C070 | 5 | 2000 | 1000 | 900 | 7.00 | 14.00 | 200 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_C085 | 085  | C085 | 5 | 2200 | 1000 | 1000 | 7.00 | 14.00 | 200 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_C058B | 058 Crocus | C058B | 5 | 2300 | 1100 | 1100 | 7.00 | 14.00 | 200 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_004 | 004 Tyltyl | C004 | 5 | 2000 | 1000 | 900 | 7.00 | 14.00 | 200 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_069A | 069 Celine | C069A | 5 | 2600 | 1100 | 1200 | 7.00 | 14.00 | 210 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_036B | 036 Bear | C036B | 5 | 2700 | 1000 | 1000 | 7.00 | 14.00 | 205 | 0.00 | 33.00 | 50 | 0 | 10 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_036 | 036 Bear | C036 | 5 | 2500 | 1000 | 1000 | 7.00 | 14.00 | 205 | 0.00 | 33.00 | 50 | 0 | 10 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_028B | 028 Octavia | C028B | 5 | 2000 | 1200 | 900 | 8.00 | 33.00 | 200 | 0.00 | 14.00 | 40 | 25 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0201_049B | 049 Bright | C049B | 5 | 1800 | 900 | 800 | 7.00 | 14.00 | 210 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1701_C510 | 010 Vincent | C510 | 5 | 5000 | 2200 | 1800 | 8.00 | 40.00 | 240 | 50.00 | 50.00 | 60 | 10 | 99 | 48 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1702_C510 | 010 Vincent | C510 | 5 | 5000 | 2200 | 1800 | 8.00 | 40.00 | 220 | 50.00 | 50.00 | 50 | 10 | 99 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1702_C509 | 009 Captain | C509 | 5 | 4000 | 1300 | 2000 | 7.00 | 30.00 | 200 | 30.00 | 50.00 | 50 | 0 | 99 | 48 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1706_C509 | 009 Captain | C509 | 5 | 5000 | 1400 | 2100 | 7.00 | 30.00 | 200 | 40.00 | 40.00 | 60 | 0 | 99 | 48 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0101_029A | 029 Kain | C029A | 5 | 2200 | 800 | 1000 | 7 | 14.00 | 208 | 0.00 | 36.00 | 55 | 0 | 10 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0104_029A | 029 Kain | C029A | 5 | 5000 | 1050 | 850 | 7 | 30.00 | 250 | 0.00 | 40.00 | 50 | 0 | 10 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0101_078 | 078 Teresa (Halloween) | C078 | 5 | 2200 | 1000 | 1000 | 7 | 14.00 | 208 | 0.00 | 14.00 | 40 | 5 | 5 | 48 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0103_034 | 034  | C034 | 5 | 2000 | 850 | 1000 | 7 | 14.00 | 200 | 0.00 | 33.00 | 40 | 0 | 10 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0103_072A | 072 Audrey | C072A | 5 | 1800 | 1200 | 700 | 7 | 28.00 | 200 | 0.00 | 28.00 | 40 | 10 | 0 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0105_059 | 059 Lantern (Halloween) | C059 | 5 | 1700 | 1300 | 600 | 7 | 14.00 | 203 | 0.00 | 14.00 | 42 | 10 | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0105_060 | 060 Denali (Halloween) | C060 | 5 | 1800 | 800 | 700 | 7 | 14.00 | 203 | 0.00 | 14.00 | 40 | 6 | 6 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1501_C041 | 041 Edward | C041 | 5 | 20000 | 1900 | 280 | 7.00 | 30.00 | 250 | 0 | 40.00 | 60 | 20 | 10 | 250 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1502_071 | 071 Anemone | C071 | 5 | 14000 | 2300 | 280 | 7.00 | 30.00 | 250 | 0 | 0.00 | 60 | 20 | 20 | 180 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1402_C046 | 046 Harley | C046 | 5 | 3600 | 1400 | 1100 | 7.00 | 20.00 | 200 | 15 | 35.00 | 40 | 0 | 10 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1402_C056 | 056 Genovia | C056 | 5 | 3000 | 1600 | 1000 | 8.00 | 35.00 | 200 | 15 | 30.00 | 40 | 5 | 99 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1602_C056 | 056 Genovia | C056 | 5 | 3400 | 1800 | 1450 | 8.00 | 30.00 | 230 | 0 | 30.00 | 50 | 5 | 40 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1402_C064 | 064 Geranium | C064 | 5 | 2700 | 1600 | 850 | 8.00 | 30.00 | 180 | 15 | 20.00 | 35 | 10 | 0 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1602_C064 | 064 Geranium | C064 | 5 | 2800 | 1900 | 1400 | 8.00 | 14.00 | 200 | 15 | 14.00 | 40 | 10 | 0 | 90 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1402_C068 | 068 Selene | C068 | 5 | 2600 | 1700 | 850 | 7.00 | 20.00 | 200 | 15 | 20.00 | 35 | 10 | 0 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_C068A | 068 Selene | C068A | 5 | 2000 | 1300 | 800 | 7.00 | 14.00 | 200 | 0 | 14.00 | 40 | 10 | 0 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1602_C068 | 068 Selene | C068 | 5 | 2800 | 2500 | 1200 | 7.00 | 18.00 | 210 | 0 | 15.00 | 40 | 10 | 0 | 90 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0003_C003 | 003 Nene | C003 | 4 | 525 | 160 | 250 | 7.00 | 20.00 | 180 | 0 | 30.00 | 50 | 0 | 0 | 35 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0003_C021 | 021 Rebecca | C021 | 4 | 450 | 180 | 200 | 8.00 | 30.00 | 200 | 0 | 20.00 | 40 | 0 | 0 | 30 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0003_C001 | 001 Lantern | C001 | 4 | 390 | 200 | 180 | 7.00 | 20.00 | 180 | 0 | 20.00 | 40 | 0 | 0 | 26 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0004_BOSS | 010 Vincent | C010 | 4 | 2000 | 120 | 160 | 5.00 | 15.00 | 150 | 0 | 15.00 | 30 | 0 | 99 | 0 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0003_BOSS | 010 Vincent | C010 | 4 | 2000 | 140 | 200 | 5.00 | 25.00 | 200 | 0 | 25.00 | 50 | 0 | 99 | 0 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0002_BOSS | 010 Vincent | C010 | 4 | 1000 | 100 | 250 | 4.00 | 0.00 | 0 | 0 | 30.00 | 50 | 0 | 99 | 8 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0001_C009 | 009 Captain | C009 | 1 | 170 | 140 | 205 | 7.00 | 10.00 | 180 | 1.00 | 25.00 | 52 | 0 | 6 | 17 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0002_C009 | 009 Captain | C009 | 1 | 170 | 140 | 205 | 7.00 | 10.00 | 180 | 1.00 | 25.00 | 52 | 0 | 6 | 5 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1302_C009 | 009 Captain | C009 | 5 | 2747 | 1062 | 1553 | 7.00 | 14.00 | 201 | 20.00 | 33.00 | 52 | 0 | 10 | 41 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1601_C009 | 009 Captain | C009 | 5 | 3230 | 1240 | 1787 | 7.00 | 14.00 | 202 | 25.00 | 33.00 | 52 | 0 | 10 | 41 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1604_C009 | 009 Captain | C009 | 5 | 4000 | 1300 | 1900 | 8.00 | 20.00 | 200 | 20.00 | 40.00 | 70 | 0 | 10 | 41 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1601_C023 | 023 Hermes | C023 | 5 | 2800 | 1600 | 1100 | 9.0 | 33.00 | 200 | 15.00 | 20.00 | 50 | 6 | 6 | 100 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0101_009_1 | 009 Captain | C009 | 2 | 323 | 229 | 320 | 7.00 | 11.00 | 183 | 1.00 | 27.00 | 52 | 0 | 7 | 9 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0101_003_1 | 003 Nene | C003 | 3 | 514 | 333 | 394 | 7.00 | 12.00 | 180 | 0.00 | 29.00 | 50 | 0 | 8 | 17 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0102_005_1 | 005 Gerard | C005 | 2 | 1000 | 280 | 260 | 5.00 | 20.00 | 180 | 0.00 | 25.00 | 25 | 0 | 0 | 5 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0103_005_1 | 005 Gerard | C005 | 2 | 310 | 210 | 290 | 7.00 | 11.00 | 180 | 0.00 | 27.00 | 52 | 0 | 0 | 9 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0103_036_1 | 036 Bear | C036 | 3 | 1700 | 330 | 220 | 5.00 | 20.00 | 200 | 0.00 | 20.00 | 30 |  | 0 | 0 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0601_036_1 | 036 Bear | C036 | 4 | 2800 | 850 | 200 | 5.00 | 30.00 | 200 | 0.00 | 30.00 | 30 |  | 0 | 0 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0602_040_1 | 040 Bibi | C040 | 5 | 4000 | 900 | 240 | 5.00 | 30.00 | 200 | 0.00 | 30.00 | 40 |  | 0 | 120 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_040 | 040 Bibi | C040 | 5 | 2400 | 1100 | 1000 | 8.00 | 33.00 | 200 | 0.00 | 15.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0201_049_1 | 049 Bright | C049 | 3 | 900 | 300 | 140 | 5 | 20 | 200 | 0 | 30 | 40 |  | 0 | 8 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0701_011_1 | 011 Hecate | C011 | 4 | 3300 | 900 | 250 | 5 | 20 | 200 | 0 | 30 | 40 |  | 0 | 80 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1101_011_1 | 011 Hecate | C011 | 5 | 2400 | 1000 | 1250 | 7 | 20 | 200 | 0 | 50 | 50 |  | 10 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1101_043_1 | 043 Papillon | C043 | 5 | 4600 | 3300 | 270 | 6 | 30 | 200 | 0 | 60 | 60 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1101_003_1 | 003 Nene | C003 | 5 | 4500 | 3300 | 280 | 6 | 30 | 200 | 0 | 40 | 40 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1101_028_1 | 028 Octavia | C028 | 5 | 4300 | 3800 | 240 | 7 | 40 | 200 | 0 | 30 | 30 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1101_014_1 | 014 Locke | C014 | 5 | 3700 | 4200 | 240 | 6 | 30 | 200 | 0 | 30 | 30 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1101_001_1 | 001 Lantern | C001 | 5 | 3700 | 3800 | 240 | 6 | 30 | 200 | 0 | 30 | 30 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1102_011 | 011 Hecate | C011 | 5 | 4500 | 2800 | 250 | 6 | 30 | 200 | 0 | 50 | 40 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1102_018 | 018 Robin | C018 | 5 | 4500 | 2900 | 230 | 6 | 30 | 200 | 0 | 40 | 40 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1102_019 | 019 Balian | C019 | 5 | 3800 | 3200 | 240 | 7 | 40 | 200 | 0 | 30 | 30 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_019 | 019 Balian | C019 | 5 | 2200 | 1200 | 950 | 8 | 33.00 | 200 | 0.00 | 20.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1102_006 | 006 Sylvester | C006 | 5 | 3600 | 3200 | 240 | 7 | 40 | 200 | 0 | 30 | 30 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1102_008 | 008 Akasha | C008 | 5 | 3600 | 2800 | 240 | 6 | 30 | 200 | 0 | 30 | 30 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_008B | 008 Akasha | C008B | 5 | 2400 | 1000 | 1100 | 7.00 | 14.00 | 200 | 0.00 | 14.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0701_018_1 | 018 Robin | C018 | 4 | 3100 | 1000 | 240 | 5 | 30 | 200 | 0 | 30 | 40 |  | 0 | 80 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0701_007_1 | 007 Metis | C007 | 4 | 2300 | 1400 | 200 | 5 | 20 | 200 | 0 | 20 | 30 |  | 0 | 80 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0701_016_1 | 016 Bruce Bang | C016 | 4 | 2400 | 1000 | 220 | 5 | 20 | 200 | 0 | 20 | 30 |  | 0 | 80 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1502_016 | 016 Bruce Bang | C016 | 5 | 8600 | 2200 | 250 | 7 | 30 | 200 | 0 | 30.00 | 30 | 20 | 10 | 120 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0202_049_1 | 049 Bright | C049 | 3 | 600 | 356 | 333 | 7 | 12.00 | 180 | 0.00 | 12.00 | 42 |  | 3 | 15 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1202_C036 | 036 Bear | C036 | 5 | 7500 | 4100 | 250 | 7 | 30.00 | 200 | 0.00 | 40.00 | 40 | 0 | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1202_C040 | 040 Bibi | C040 | 5 | 6500 | 4300 | 230 | 7 | 40.00 | 250 | 0.00 | 30.00 | 30 | 0 | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1202_C057 | 057 Pansy | C057 | 5 | 4500 | 3800 | 240 | 7 | 30.00 | 200 | 0.00 | 30.00 | 30 | 0 | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_C057 | 057 Pansy | C057 | 5 | 2400 | 1000 | 900 | 7 | 30.00 | 200 | 0.00 | 30.00 | 30 | 5 | 5 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1201_C054 | 054 Dino | C054 | 5 | 2400 | 1600 | 1200 | 7 | 14.00 | 200 | 0.00 | 14.00 | 40 | 5 | 5 | 30 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1602_C054 | 054 Dino | C054 | 5 | 2700 | 1800 | 1100 | 7 | 14.00 | 200 | 15.00 | 14.00 | 40 | 10 | 0 | 90 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1502_054 | 054 Dino | C054 | 5 | 7500 | 2700 | 210 | 7 | 30.00 | 200 | 0.00 | 30.00 | 30 | 20 | 10 | 120 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1502_054_1 | 054 Dino | C054 | 5 | 7500 | 2700 | 210 | 7 | 30.00 | 200 | 0.00 | 30.00 | 30 | 20 | 10 | 120 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0301_013_1 | 013 Denali | C013 | 3 | 1300 | 500 | 160 | 5.00 | 20.00 | 200 | 0.00 | 20.00 | 30 |  | 0 | 10 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1602_C004 | 004 Tyltyl | C004 | 5 | 2700 | 1200 | 1100 | 7.00 | 14.00 | 202 | 15.00 | 14.00 | 42 | 5 | 5 | 80 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0302_010_1 | 010 Vincent | C010 | 4 | 3000 | 310 | 210 | 5.00 | 30.00 | 200 | 10.00 | 30.00 | 30 |  | 99 | 0 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0702_010_1 | 010 Vincent | C010 | 5 | 3700 | 1800 | 260 | 5.00 | 30.00 | 200 | 5.00 | 30.00 | 40 |  | 0 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1302_C010 | 010 Vincent | C010 | 5 | 3200 | 1601 | 1149 | 8.00 | 30.00 | 221 | 20.00 | 30.00 | 42 | 5 | 5 | 48 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1603_C010 | 010 Vincent | C010 | 5 | 4000 | 1900 | 1400 | 8.00 | 30.00 | 222 | 20.00 | 30.00 | 42 | 5 | 5 | 48 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0801_052_1 | 052 Windblade | C052 | 5 | 6000 | 2100 | 240 | 6.00 | 40.00 | 200 | 0.00 | 40.00 | 50 |  | 0 | 0 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0802_056_1 | 056 Genovia | C056 | 5 | 7000 | 2800 | 260 | 6.00 | 40.00 | 200 | 0.00 | 40.00 | 50 |  | 50 | 0 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0901_024_1 | 024 Riko | C024 | 5 | 5000 | 2400 | 280 | 6.00 | 30.00 | 200 | 0.00 | 40.00 | 40 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0901_021_1 | 021 Rebecca | C021 | 5 | 4100 | 2600 | 260 | 6.00 | 40.00 | 200 | 0.00 | 30.00 | 30 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0901_039_1 | 039 Gullveig | C039 | 5 | 3200 | 2800 | 230 | 6.00 | 30.00 | 200 | 0.00 | 30.00 | 30 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0901_014_1 | 014 Locke | C014 | 5 | 3200 | 2800 | 220 | 6.00 | 30.00 | 200 | 0.00 | 30.00 | 30 |  | 0 | 40 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0902_041_1 | 041 Edward | C041 | 5 | 6500 | 3100 | 280 | 6.00 | 30.00 | 200 | 0.00 | 40.00 | 80 |  | 0 | 100 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0902_020_1 | 020 Sienna | C020 | 5 | 4500 | 3300 | 260 | 6.00 | 30.00 | 200 | 0.00 | 30.00 | 40 |  | 0 | 100 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0502_012_1 | 012 Karl Steiner | C012 | 4 | 2500 | 850 | 220 | 5.00 | 30.00 | 200 | 0 | 30.00 | 40 |  | 0 | 0 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0601_012_1 | 012 Karl Steiner | C012 | 4 | 1150 | 750 | 550 | 7.00 | 33.00 | 200 | 0 | 13.00 | 40 |  | 0 | 30 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0601_012_1 | 012 Karl Steiner | C012 | 4 | 1150 | 750 | 533 | 7.00 | 31.00 | 210 | 0 | 13.00 | 40 |  | 0 | 26 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1303_C012 | 012 Karl Steiner | C012 | 5 | 2800 | 2000 | 1100 | 7.00 | 58.00 | 226 | 0.00 | 14.00 | 40 | 5 | 5 | 44 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1001_012_1 | 012 Karl Steiner | C012 | 5 | 8000 | 3500 | 280 | 6.00 | 30.00 | 250 | 0.00 | 40.00 | 40 |  | 20 | 100 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1001_030_1 | 030 Acerola | C030 | 5 | 5500 | 3600 | 270 | 6.00 | 30.00 | 200 | 0.00 | 30.00 | 40 |  | 20 | 100 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB1502_017 | 017 Lapis | C017 | 5 | 9000 | 2400 | 240 | 8.00 | 40.00 | 220 | 0.00 | 40.00 | 40 | 20 | 10 | 120 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| EVCB0301_017 | 017 Lapis | C017 | 5 | 2100 | 1200 | 950 | 9 | 33.00 | 200 | 0.00 | 20.00 | 40 | 5 | 5 | 45 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0401_017_1 | 017 Lapis | C017 | 4 | 1500 | 280 | 180 | 6.00 | 30.00 | 200 | 0.00 | 20.00 | 30 |  | 0 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |
| CB0401_005_1 | 005 Gerard | C005 | 4 | 2000 | 240 | 200 | 5.00 | 20.00 | 200 | 0.00 | 30.00 | 30 |  | 0 | 50 | 40 | LOW | scripted story context; rank is display thumb context, not progression; attr_resist 99 on 10 rows is a sentinel |

## C. Episode scripted monster tuples — the 34 M* rows (42 monster-like rows incl. 8 monster-typed C* placements)

| Combat ID | Monster | Rank | HP | ATK | DEF | SPD | Crit | CritDmg | Pen | Block | BlockRes | HPReg | Cool(ms) | Conf% | Word | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| CB1501_M1 | M034 | 5 | 7000 | 6800 | 280 | 0 | 50.00 | 300 | 0.00 | 40.00 | 40 | 120 | 8000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1501_M2 | M035 | 5 | 7000 | 6800 | 280 | 0 | 50.00 | 300 | 0.00 | 40.00 | 40 | 120 | 8000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0002_M01 | M034 | 1 | 100 | 100 | 100 | 0.00 | 25 | 175 | 0 | 0 | 0 | 0 | 99000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0001_BOSS | M040 | 1 | 400 | 190 | 100 | 0.00 | 25 | 175 | 0 | 0 | 0 | 0 | 99000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0001_M01 | M001 | 1 | 150 | 130 | 100 | 0.00 | 25 | 175 | 0 | 0 | 0 | 0 | 99000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0102_M1 | M022 | 1 | 450 | 430 | 180 | 0 | 20.00 | 180 | 0.00 | 10.00 | 10 | 5 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0201_M1 | M023 | 2 | 700 | 400 | 130 | 0 | 20.00 | 200 | 0.00 | 20.00 | 20 | 8 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0602_M1 | M024 | 4 | 2500 | 1800 | 200 | 0 | 30.00 | 200 | 0.00 | 30.00 | 30 | 20 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0202_M1 | M050 | 2 | 800 | 680 | 160 | 0 | 20.00 | 200 | 0.00 | 20.00 | 20 | 15 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0202_M2 | M049 | 2 | 800 | 680 | 160 | 0 | 20.00 | 200 | 0.00 | 20.00 | 20 | 15 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0202_M3 | M051 | 2 | 800 | 700 | 160 | 0 | 20.00 | 200 | 0.00 | 20.00 | 20 | 15 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0202_BOSS | M062 | 3 | 1800 | 750 | 160 | 0 | 30.00 | 200 | 0.00 | 30.00 | 30 | 25 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0501_M1 | M046 | 3 | 1000 | 1200 | 180 | 0 | 30.00 | 200 | 0.00 | 20.00 | 20 | 20 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0501_M2 | M052 | 3 | 1000 | 1200 | 180 | 0 | 30.00 | 200 | 0.00 | 20.00 | 20 | 20 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0501_M3 | M048 | 3 | 1000 | 1200 | 180 | 0 | 30.00 | 200 | 0.00 | 20.00 | 20 | 20 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0501_M4 | M054 | 3 | 1000 | 1200 | 180 | 0 | 30.00 | 200 | 0.00 | 20.00 | 20 | 20 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0501_BOSS | M062 | 4 | 2000 | 1500 | 210 | 0 | 30.00 | 200 | 0.00 | 20.00 | 30 | 30 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0702_M1 | M058 | 4 | 2400 | 2600 | 200 | 0 | 30.00 | 200 | 0.00 | 30.00 | 30 | 50 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| EVCB0102_M1 | M035 | 4 | 3000 | 3500 | 200 | 0 | 30.00 | 300 | 0.00 | 30.00 | 30 | 50 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| EVCB0102_M2 | M036 | 4 | 3000 | 3500 | 200 | 0 | 30.00 | 300 | 0.00 | 30.00 | 30 | 50 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1002_M1 | M035 | 5 | 5500 | 4500 | 280 | 0 | 40.00 | 200 | 0.00 | 30.00 | 30 | 50 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1002_M2 | M036 | 5 | 5500 | 4500 | 280 | 0 | 40.00 | 200 | 0.00 | 30.00 | 30 | 50 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| EVCB0301_M044 | M044 | 5 | 5000 | 4000 | 250 | 0 | 30.00 | 200 | 0.00 | 30.00 | 30 | 50 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| EVCB0301_M057 | M057 | 5 | 4000 | 4500 | 200 | 0 | 30.00 | 200 | 0.00 | 30.00 | 30 | 50 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1002_M3 | M034 | 5 | 13000 | 5500 | 280 | 0 | 40.00 | 250 | 0.00 | 40.00 | 40 | 100 | 10000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1301_M1 | M035 | 5 | 7000 | 6000 | 300 | 0 | 40.00 | 200 | 0.00 | 30.00 | 30 | 50 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1301_M2 | M036 | 5 | 7000 | 6000 | 300 | 0 | 40.00 | 200 | 0.00 | 30.00 | 30 | 50 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1301_M3 | M034 | 5 | 16000 | 7000 | 300 | 0 | 40.00 | 250 | 0.00 | 35.00 | 35 | 100 | 10000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1201_BOSS | M100 | 5 | 16000 | 7000 | 300 | 0 | 40.00 | 200 | 0.00 | 30.00 | 30 | 100 | 10000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1401_BOSS | M100 | 5 | 20000 | 8000 | 280 | 0 | 40.00 | 250 | 0.00 | 30.00 | 30 | 150 | 10000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1201_M1 | M041 | 5 | 6500 | 6000 | 300 | 0 | 40.00 | 200 | 0.00 | 30.00 | 30 | 70 | 10000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1201_M2 | M040 | 5 | 6500 | 6000 | 300 | 0 | 40.00 | 200 | 0.00 | 30.00 | 30 | 70 | 10000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB1201_M3 | M042 | 5 | 6500 | 6000 | 300 | 0 | 40.00 | 200 | 0.00 | 30.00 | 30 | 70 | 10000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |
| CB0301_M1 | M023 | 2 | 700 | 650 | 160 | 0 | 20.00 | 200 | 0.00 | 20.00 | 20 | 10 | 5000 | 55 | MEDIUM | per-encounter tuning [ORIGDATA]; M034 spans 160x across rows; only 2/22 tokens map to catalog art names |

_Additional monster placements not shown: `CB1102_006/_008/_011/_018/_019` (C006/C008/C011/C018/C019) and 3 monster-placed `C010` rows — 8 monster-typed C* rows (SYNTHESIS correction, 2026-10-06)._

## C.2 Enemy/allied hunter-class rows — natively exercised combats (2026-10-08)

The `C*`-namespace rows the Episode combats place outside the player party. Where §-evidence exists the row was seen live in the instrumented client at exactly these values, which raises confidence above the scripted-data baseline.

| Combat ID | Hero ref | res_id | Rank | HP | ATK | DEF | SPD | Block | BlockRes | HPReg | Conf% | Word | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| CB0102_005_1 | 005 Gerard | C005 | 2 | 1000 | 280 | 260 | 5.00 | 25.00 | 25 | 5 | 90 | HIGH | rendered HP1000→0 in the live native win (§160) |
| CB0103_005_1 | 005 Gerard | C005 | 2 | 310 | 210 | 290 | 7.00 | 27.00 | 52 | 9 | 90 | HIGH | Bear rendered HP1700→0, original cut-in followed (§161–162) |
| CB0103_036_1 | 036 Bear | C036 | 3 | 1700 | 330 | 220 | 5.00 | 20.00 | 30 | 0 | 90 | HIGH | Bear rendered HP1700→0, original cut-in followed (§161–162) |
| CB0201_049_1 | 049 Bright | C049 | 3 | 900 | 300 | 140 | 5 | 30 | 40 | 8 | 90 | HIGH | enemy Bright rendered HP900→0 (§164) |
| CB0202_049_1 | 049 Bright | C049 | 3 | 600 | 356 | 333 | 7 | 12.00 | 42 | 15 | 90 | HIGH | ally Bright HP600 held alive through the win (§164) |
| CB0301_013_1 | 013 Denali | C013 | 3 | 1300 | 500 | 160 | 5.00 | 20.00 | 30 | 10 | 90 | HIGH | Denali rendered HP1300→0 in the live native win (§165) |
| CB0302_010_1 | 010 Vincent | C010 | 4 | 3000 | 310 | 210 | 5.00 | 30.00 | 30 | 0 | 90 | HIGH | Vincent rendered HP3000 — combat pending (§165) |
| CB1102_006 | 006 Sylvester | C006 | 5 | 3600 | 3200 | 240 | 7 | 30 | 30 | 40 | 55 | MEDIUM | not yet exercised in play |
| CB1102_008 | 008 Akasha | C008 | 5 | 3600 | 2800 | 240 | 6 | 30 | 30 | 40 | 55 | MEDIUM | not yet exercised in play |
| CB1102_011 | 011 Hecate | C011 | 5 | 4500 | 2800 | 250 | 6 | 50 | 40 | 40 | 55 | MEDIUM | not yet exercised in play |
| CB1102_018 | 018 Robin | C018 | 5 | 4500 | 2900 | 230 | 6 | 40 | 40 | 40 | 55 | MEDIUM | not yet exercised in play |
| CB1102_019 | 019 Balian | C019 | 5 | 3800 | 3200 | 240 | 7 | 30 | 30 | 40 | 55 | MEDIUM | not yet exercised in play |

_12 rows extracted from EPISODE_STAT_ACTORS.json (151-row STAT table); monster-typed CB1102 rows included for completeness. M* rows remain in Table C._

## D. Monster catalog — 22 IDs (identity only; zero base-stat sources)

| ID | Art pack | Bytes | Conf% | Word | Notes |
|---|---|---:|---:|---|---|
| M001 | M001.jet | 170026 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M002 | M002.jet | 191824 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M003 | M003.jet | 971019 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M004 | M004.jet | 453959 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M005 | M005.jet | 373324 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M006 | M006.jet | 539796 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M007 | M007.jet | 528366 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M008 | M008.jet | 223669 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M009 | M009.jet | 276230 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M010 | M010.jet | 693789 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M011 | M011.jet | 833087 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M012 | M012.jet | 866108 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M013 | M013.jet | 1187818 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M014 | M014.jet | 1557994 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M015 | M015.jet | 1096524 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M016 | M016.jet | 1597837 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M017 | M017.jet | 943115 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M018 | M018.jet | 837454 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M019 | M019.jet | 929190 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M020 | M020.jet | 925674 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M021 | M021.jet | 1015930 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |
| M100 | M100.jet | 584684 | 90 | HIGH | identity/art [ORIGDATA]; NO stat source exists — strict coverage 0/22 |

## E. Jewel set bonuses — all 12 families, both shipped versions [ORIGDATA]

| # | Family | Mount | 1.4.4.1 (PRE) | 2.8.0.1 (POST) | Conf% | Word | Notes |
|---|---|---|---|---|---:|---|---|
| 1 | HP | 2 | 5% | 6% | 95 | HIGH | HP/AP/DP x1.20 between versions |
| 2 | Offensive (AP) | 2 | 5% | 6% | 95 | HIGH |  |
| 3 | Defensive (DP) | 2 | 5% | 6% | 95 | HIGH |  |
| 4 | Critical (crit chance) | 2 | 4.5% | 6% | 95 | HIGH | x1.333 |
| 5 | Block (block chance) | 2 | 4.5% | 5% | 95 | HIGH | x1.111 |
| 6 | Fatal (crit damage) | 4 | 50% | 60% | 95 | HIGH | x1.20 |
| 7 | Super Block (block-dmg reduction) | 4 | 5% (KO 9%) | 10% (SC 9%) | 60 | CONTESTED | CONTESTED: shipped client disagrees with itself across locales |
| 8 | Element (enhancement) | 4 | +23 flat | 35 | 95 | HIGH | decimal ambiguity resolved for the SET effect only |
| 9 | Resistance | 4 | +23 flat | 35 | 95 | HIGH |  |
| 10 | Speed (attack speed) | 4 | 1.72 | 1.72 | 95 | HIGH | unchanged |
| 11 | Regeneration (HP regen) | 4 | 30 | 30 | 95 | HIGH | unchanged; no unit printed anywhere |
| 12 | Penetration | 4 | 12 | 16 | 95 | HIGH | x1.333 |

_Confidence 95 = [ORIGDATA] help text in five locales, two shipped versions. These are HELP-STRING values, not engine constants; a help table can lag live balance (proven in-client)._

## E.2 Mounted jewel samples — 6 transcribed Lv.15 panels [PIXEL, era-unknown]

| Panel | Slot | Main | Sub 1 | Sub 2 | Sub 3 | Sub 4 | Conf% | Word | Notes |
|---|---|---|---|---|---|---|---:|---|---|
| img22 Radiant Speed | Weapon | ATK +29 | Crit Dmg +3.13 | Block Ch +0.72 | Elem Resist +1.44 | Dmg Red Blk +0.50 | 60 | MEDIUM | single FAQ sample n=6, 5-star Highest Class Lv.15/15; removal footer 40000 gold + 40 |
| img23 Radiant Offensive | Weapon | ATK +29 | DEF +11 | Dmg Red Blk +0.38 | Elem Enh +1.65 | ATK +11 | 60 | MEDIUM | single FAQ sample n=6, 5-star Highest Class Lv.15/15; same jewel name yields different mains by slot |
| img24 Radiant Offensive | Accessory | Max HP +58 | ATK +12 | Max HP +21 | Elem Resist +1.69 | Block Ch +0.56 | 60 | MEDIUM | single FAQ sample n=6, 5-star Highest Class Lv.15/15;  |
| img25 Radiant Speed | Accessory | Max HP +58 | Max HP +18 | Crit Dmg +3.87 | Block Ch +0.56 | ATK +13 | 60 | MEDIUM | single FAQ sample n=6, 5-star Highest Class Lv.15/15;  |
| img26 Radiant Speed | Armor | Block Ch +2.30 | Block Ch +0.56 | Max HP +21 | Dmg Red Blk +0.50 | DEF +11 | 60 | MEDIUM | single FAQ sample n=6, 5-star Highest Class Lv.15/15;  |
| img27 Radiant Speed | Armor | DEF +29 | Crit Ch +0.67 | Dmg Red Blk +0.38 | ATK +11 | Crit Dmg +3.86 | 60 | MEDIUM | single FAQ sample n=6, 5-star Highest Class Lv.15/15;  |

## F. Multipliers — shipped battle tuning and measured combat scalars

| Multiplier | Values | Applies to | Class | Conf% | Word | Notes |
|---|---|---|---|---:|---|---|
| Monster rank (hp) | 2.6 / 2.2 / 1.8 / 1.4 / 1.0 | rank 1-5 | LEVELING.jet chunk 9 [ORIGDATA] | 95 | HIGH | monster-rank, not hero rank |
| Monster rank (atk/def) | 1.4 / 1.3 / 1.2 / 1.1 / 1.0 | rank 1-5 | LEVELING.jet chunk 9 [ORIGDATA] | 95 | HIGH |  |
| Role bonus (hp) | Bomber 0.85, Support 0.80, others 1.0 | battle camps | [ORIGDATA] | 95 | HIGH |  |
| atk_camp | 2.0 / 2.6 / 1.0 | attack camp scaling | [ORIGDATA] | 95 | HIGH | semantics per-camp index |
| Stage bonus | 1.1 x3 (hp/atk/def) for cards 051 | bonus.stage b_00_01 | [ORIGDATA] | 90 | HIGH | single entry only |
| SP economy | first 1.5, regen 0.21/s, +2.0/kill, +0.02/attack, max 10 — **mode-dependent**: live CB0102 groups measured rate 0.03/max 10 (§160) | battle SP | [ORIGDATA] chunk 9 + [NATIVE] live read | 95 | HIGH | do not assume chunk-9 values globally; skill-cost debit natively verified (Nene cost 3: SP10→7.04, §161) |
| Rarity magnitude step | approx x1.30 HP and ATK+DEF per grade | hero draw grade | [DERIVED] n=62 archive | 70 | MEDIUM | HP and ATK+DEF both x1.29-1.30; substats NOT scaled |
| Per-level compound | x1.0189 avg (HP 1.01879 / ATK 1.01852 / DEF 1.01930) | hero level 1-30 | [DERIVED] 051 anchor, 29 steps | 60 | MEDIUM | single-g misses panel by 6.6 cp; Natalia conflict 1.0101 unresolved |
| enemy_atk_per / enemy_hp_per | 100 = 100% (neutral) | stage scalars | [NATIVE] | 99 | HIGH | proven: paths do not scale by it; do not "fix" to 1 |
| Transcendence T3 | x1.30 (Hermes exact 3/3; flat ladder fits 8/9) | grade-up to 5-star | [PIXEL] measured 3 heroes | 55 | MEDIUM | cumulative x1.716 REFUTED; T1/T2 per-step x1.10/x1.20 UNTESTED; do not implement |
| Tier scalar (PRE pairs) | x1.199 / 1.201 / 1.201 (HP/ATK/DEF) | Base-to-Max 25 pairs | [COMM] contaminated | 40 | LOW | Locke=Metis duplicate rows; PRE era |
| EVCB event scale | approx x1.36 (median 1.358-1.375, CV 13.7%) | event combat vs archive | [DERIVED] hypothesis | 30 | LOW | test only, never install |
| 2019-09-05 rebalance | equipment +50%; crystal main +30% (1-3-star) / +50% (4-5-star); substats +50%; substat upgrades fixed at max | equipment/crystals | official announcement | 95 | HIGH | no per-item delta; era boundary for every dated visual |
| Power law (approx) | cp = -7884 + 3.060hp + 5.206atk + 5.822def + 43.56spd + 33.08crit + 5.28critdmg + 34.01pen + 31.93blk + 10.13blkred - 16.67eenh + 10.46eres - 4.91regen | combat power | [DERIVED] OLS n=59 R2=0.996 | 40 | LOW | portal-derived fit, not a recovered formula; max residual ~81 cp |
| block_damage_reduction cp weight | exactly 18 cp units | combat power | [DERIVED] collision pairs | 45 | LOW | portal-derived, exactly determined in 2 roles |
| Wire stat growth formula | hp/atk/def/spd stored at CSRCardStat+18/+28/+38/+8, growth at +c8/+d8/+e8; helper = uint32(base + up×level) × multiplier; Validate receives GetStatWithoutEquip | hero stat pipeline | [NATIVE] §158 | 90 | HIGH | formula shape proven; magnitudes/growth increments remain fixtures |
| Attack-speed unit | actor interval = (1/spd)/atk_spd_bonus, then buff, minimum 0.06 s; LevelData+254 = 0.8 (chunks 9/10/11/12/14) or 1.0 (17), omitted elsewhere | attack interval | [NATIVE] §158 | 90 | HIGH | do not infer the selected chunk from field presence |
| Hunter level selectors | GetCardLevel = first threshold above EXP returns row.level-1 (min 1), else last row.level; GetCardMaxLevel = last row.level; RaiseExp indexes level-1, clamped | level lookup | [NATIVE] §157 | 90 | HIGH | no sentinel row needed; interior XP thresholds still unknown |
| Stat consumer getters | GetAtk = base(+38)×buff(+38), upper clamp 3, lower unresolved, final min 1; GetDef at +40; GetAtkSpd at +3c product | combat stat read | [NATIVE] §156 | 85 | HIGH | bounded readonly audit of original Thumb |
| Active-skill activation | native press→eventpool→ReserveSkill→SP debit; Nene cost 3: SP 10→7.04, pause2/state4→resume | skill economy | [NATIVE] §161 | 85 | HIGH | numeric effect damage NOT isolated amid ordinary hits/healing |

## G. Per-area campaign rewards — 5 expedition areas x 10 stages (50 stages, [RECOVERED] structure)

Stage/area/serial structure is recovered from `LEVELING.jet` chunk 0. All AMOUNTS are local fixtures unless marked; originals are unknown. Stars: 3 conditions per stage (native), default rules Complete/Under-60s/<=1 straggler are local policy.

| Area | Title | Stages | Stage IDs | First-clear gold (fixture) | First-clear user EXP (fixture) | Hunter EXP/win (fixture) | AP cost (fixture) | Chest thresholds | Chest amounts | Conf% | Word | Notes |
|---|---|---|---|---|---|---|---|---|---|---:|---|---|
| n_01 | Snowfield | 10 | n_01_01, n_01_02, n_01_03, n_01_04, n_01_05, n_01_06, n_01_07, n_01_08, n_01_09, n_01_10 | 10 gold | 30 EXP | 10 EXP | 1 | 10 / 20 / 30 stars | UNKNOWN (fixture 300/200/100 gold) | 90 · HIGH | Title: measured on screen | structure [RECOVERED] n=10 stages serial 1..10; chest mechanism [NATIVE] achieve_cnt=stage_cnt x (i+1); all amounts fixtures |
| n_02 | Glacier | 10 | n_02_01, n_02_02, n_02_03, n_02_04, n_02_05, n_02_06, n_02_07, n_02_08, n_02_09, n_02_10 | 10 gold | 30 EXP | 10 EXP | 1 | 10 / 20 / 30 stars | UNKNOWN (fixture 300/200/100 gold) | 90 · HIGH | Title: measured on screen | structure [RECOVERED] n=10 stages serial 1..10; chest mechanism [NATIVE] achieve_cnt=stage_cnt x (i+1); all amounts fixtures |
| n_03 | Red Rock | 10 | n_03_01, n_03_02, n_03_03, n_03_04, n_03_05, n_03_06, n_03_07, n_03_08, n_03_09, n_03_10 | 10 gold | 30 EXP | 10 EXP | 1 | 10 / 20 / 30 stars | UNKNOWN (fixture 300/200/100 gold) | 90 · HIGH | Title: measured on screen | structure [RECOVERED] n=10 stages serial 1..10; chest mechanism [NATIVE] achieve_cnt=stage_cnt x (i+1); all amounts fixtures |
| n_04 | Aurora Tundra | 10 | n_04_01, n_04_02, n_04_03, n_04_04, n_04_05, n_04_06, n_04_07, n_04_08, n_04_09, n_04_10 | 10 gold | 30 EXP | 10 EXP | 1 | 10 / 20 / 30 stars | UNKNOWN (fixture 300/200/100 gold) | 15 · VERY LOW | Title: fixture | structure [RECOVERED] n=10 stages serial 1..10; chest mechanism [NATIVE] achieve_cnt=stage_cnt x (i+1); all amounts fixtures |
| n_05 | Deep Cavern | 10 | n_05_01, n_05_02, n_05_03, n_05_04, n_05_05, n_05_06, n_05_07, n_05_08, n_05_09, n_05_10 | 10 gold | 30 EXP | 10 EXP | 1 | 10 / 20 / 30 stars | UNKNOWN (fixture 300/200/100 gold) | 15 · VERY LOW | Title: fixture | structure [RECOVERED] n=10 stages serial 1..10; chest mechanism [NATIVE] achieve_cnt=stage_cnt x (i+1); all amounts fixtures |

_Capsule drop: AIRSHIP_TICKET x1 per qualifying normal victory is a LOCAL rule; the tutorial proves capsules come from clearing general stages but not the rate. Loss refunds fuel ([ORIGDATA] help, 4 locales) — replica implements reservation-based refund._


## G.2 Per-stage reward guesstimates — all 50 campaign stages

Structure [RECOVERED] (stage id, area, serial from `LEVELING.jet` chunk 0). Every AMOUNT column is a local fixture shown for completeness; the original per-stage amounts are unknown (14 documented unknowns in `rewards-economy-2026-10-05.md` §D). Stars: 3 conditions/stage (native); wave contents are NOT recovered — no original stage→monster mapping exists locally.

| Stage | Area | Serial | First-clear gold (fixture) | First-clear user EXP (fixture) | Hunter EXP (fixture) | AP cost (fixture) | Stars | Conf% | Word | Notes |
|---|---|---:|---|---|---|---|---|---:|---|---|
| n_01_01 | n_01 Snowfield | 1 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_01_02 | n_01 Snowfield | 2 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_01_03 | n_01 Snowfield | 3 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_01_04 | n_01 Snowfield | 4 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_01_05 | n_01 Snowfield | 5 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_01_06 | n_01 Snowfield | 6 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_01_07 | n_01 Snowfield | 7 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_01_08 | n_01 Snowfield | 8 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_01_09 | n_01 Snowfield | 9 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_01_10 | n_01 Snowfield | 0 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_02_01 | n_02 Glacier | 1 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_02_02 | n_02 Glacier | 2 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_02_03 | n_02 Glacier | 3 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_02_04 | n_02 Glacier | 4 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_02_05 | n_02 Glacier | 5 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_02_06 | n_02 Glacier | 6 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_02_07 | n_02 Glacier | 7 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_02_08 | n_02 Glacier | 8 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_02_09 | n_02 Glacier | 9 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_02_10 | n_02 Glacier | 0 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_03_01 | n_03 Red Rock | 1 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_03_02 | n_03 Red Rock | 2 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_03_03 | n_03 Red Rock | 3 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_03_04 | n_03 Red Rock | 4 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_03_05 | n_03 Red Rock | 5 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_03_06 | n_03 Red Rock | 6 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_03_07 | n_03 Red Rock | 7 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_03_08 | n_03 Red Rock | 8 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_03_09 | n_03 Red Rock | 9 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_03_10 | n_03 Red Rock | 0 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_04_01 | n_04 Aurora Tundra | 1 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_04_02 | n_04 Aurora Tundra | 2 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_04_03 | n_04 Aurora Tundra | 3 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_04_04 | n_04 Aurora Tundra | 4 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_04_05 | n_04 Aurora Tundra | 5 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_04_06 | n_04 Aurora Tundra | 6 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_04_07 | n_04 Aurora Tundra | 7 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_04_08 | n_04 Aurora Tundra | 8 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_04_09 | n_04 Aurora Tundra | 9 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_04_10 | n_04 Aurora Tundra | 0 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_05_01 | n_05 Deep Cavern | 1 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_05_02 | n_05 Deep Cavern | 2 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_05_03 | n_05 Deep Cavern | 3 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_05_04 | n_05 Deep Cavern | 4 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_05_05 | n_05 Deep Cavern | 5 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_05_06 | n_05 Deep Cavern | 6 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_05_07 | n_05 Deep Cavern | 7 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_05_08 | n_05 Deep Cavern | 8 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_05_09 | n_05 Deep Cavern | 9 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |
| n_05_10 | n_05 Deep Cavern | 0 | 10 gold | 30 EXP | 10 EXP | 1 | 3 conditions | 15 | VERY LOW | structure 95/HIGH, amounts fixtures; enemy waves/scaling per stage unpublished (enemy_atk_per/enemy_hp_per all 100 = neutral in fixtures) |

_Area chest anchors: thresholds 10/20/30 stars per area ([NATIVE] achieve_cnt = stage_cnt x (i+1)); payout amounts unknown. Chest item identities 912/913/914 = 2/3/4-star Transcendence Tickets ([ORIGDATA])._
## H. Episode chapter rewards — all 18 declarations [ORIGDATA, exact]

| Chapter | Stories | Declared reward | Settled? | Conf% | Word | Notes |
|---|---:|---|---|---:|---|---|
| E01 | 7 | GC2 x3 (GC2 (Lottery coupon)) | YES (implemented) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E02 | 8 | FMD1 x30 (FMD1 (free-Manda identity)) | YES (30 free Manda) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E03 | 7 | GC3 x3, GC4 x3 (GC3 (material) + GC4 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E04 | 4 | GC8 x1 (GC8 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E05 | 8 | AIRSHIP_TICKET x20 (AIRSHIP_TICKET (Helium capsule (crosswalk UNPROVED))) | YES (20 capsules) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E06 | 7 | OV1 x10 (OV1 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E07 | 5 | CERUM01 x20 (CERUM01 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E08 | 7 | CERUM02 x20 (CERUM02 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E09 | 7 | CERUM03 x20 (CERUM03 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E10 | 7 | SK13 x30, SK23 x30 (SK13 (material) + SK23 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E11 | 8 | SK33 x30, SK43 x30 (SK33 (material) + SK43 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E12 | 7 | EM02 x2000 (EM02 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E13 | 8 | LCOIN x20 (LCOIN (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E14 | 7 | OV1 x30 (OV1 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E15 | 8 | GC9 x1 (GC9 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E16 | 9 | GC10 x1 (GC10 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E17 | 9 | GC11 x1 (GC11 (material)) | NO (refuses; item row missing) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |
| E18 | 5 | RP1 x100000 (RP1 (gold display identity)) | YES (100000 gold) | 95 | HIGH | exact original declaration, SHA-pinned R_EPISODE.jet; settlement mapping for E02/E05/E18 is explicit replica policy |

## I. Original-pixel reward anchors [PIXEL]

| Anchor | Value | Context | Conf% | Word | Notes |
|---|---|---|---:|---|---|
| Search payout | +1400 Rupees + scroll 5 / leaf 4 / trace 40 / orb 1 | Volcanic Abyss, team lvl 40 | 60 | MEDIUM | first original Search payout pixels ever transcribed |
| Search payout | +2000 Rupees + crystals 8 / stones 5 / trace 40 / scroll 1 | Electric Abyss, team lvl 62 | 60 | MEDIUM |  |
| Search payout | +2000 Rupees + leaf 5 / orb 3 / trace 3 / scroll 1 | Volcanic Abyss, lvl 55 | 60 | MEDIUM |  |
| Co-op reward | 21000 Rupees, 3 stars, rank 210 | Co-op Exploration | 60 | MEDIUM | single screen |
| Recruitment mileage | 3 / 10 / 25 / 40 pulls (sum 78) | mileage phases | 70 | MEDIUM | original pixels, phases split |
| Skill training cost | 800 Rupees + materials 4/4/2 | skill Lv.35 | 60 | MEDIUM | PRE-era, single account |
| Transcendence cost | 9000 Rupees + 9 gems / 90 crystals | transcend button | 60 | MEDIUM | matches two-source ladder 9/90/9000 at 3-star |
| Advancement cost | 8000 (2 fodder) / 12000 (3 fodder) | 3-star to 4-star | 60 | MEDIUM | cost varies with fodder count; no formula inferred |
| Equipment upgrade | 50000 Rupees + 320/27 toolboxes | armor Lv.49 to 50 | 60 | MEDIUM |  Vincent 010 screen |
| Jewel removal fee | 40000 gold + 40 (second currency unknown) | jewel panel footer | 40 | LOW | single image, era unknown |

## J. Price / economy guesstimates

| Item | Value | Class | Conf% | Word | Notes |
|---|---|---|---:|---|---|
| Gacha single draw | 30 Manda | [NATIVE]+[COMM] | 95 | HIGH | native constant vector [100,300,11,30]; counts 1 and 11 only |
| Gacha 10+1 bundle | 300 Manda, guaranteed 3-star or above | [NATIVE]+[PIXEL] | 95 | HIGH | guarantee seen on device |
| Gacha pools / probabilities / pity | UNKNOWN | - | 5 | VERY LOW | community prose only (4-star at 16 pulls uncorroborated) |
| Gacha boost events | limited 3-star 400%/500%, all 3-star 200% | official event posts | 80 | HIGH | per-scope reading; no base rate published |
| AP refill item | +10 AP, 5 Manda or 100 gold, 3/day shared | fixture | 15 | VERY LOW | original amount/prices/reset unknown; VSFan +5/+7 is VIP benefit not price |
| BP refill item | +5 BP, 5 Manda or 100 gold, 3/day shared | fixture | 15 | VERY LOW | BP mechanism [NATIVE] but values unknown |
| Skill training gold | banded 100 to 1000 per decade of levels (L1-4=100 ... L45-49=1000) | [COMM] x2 | 55 | CONTESTED | vs local 100xlevel formula (agree at L1 only); CONTESTED against fixture, sources agree with each other |
| Skill training materials | role material from Lv5: 0/0/0, 1/0/0, 2/0/0, 3/0/0, 4/1/0, 5/2/0, 0/3/1, 0/4/2, 0/5/3, 0/6/4 per decade | [COMM] x2 (30/30 cells agree) | 75 | HIGH | decadal fragments 1-5; skill Lv.25 contested 4+1 vs 5+2 |
| Skill level caps | 10 / 20 / 30 / 40 / 50 by grade | [COMM]+[ORIGDATA]+native shape | 90 | HIGH | INFERRED from 10-per-grade rule |
| Raise (training) cost | UNKNOWN per-source (fixture 100 gold) | [COMM] pixels 8000/12000 at 2/3 fodder | 25 | LOW | fixture 1000/source is 8-12x off pixel previews; no per-source anchor |
| Rank-up materials | N same-star partners for rank N (1/2/3/4) | [COMM] x2 + native capacity shape | 90 | HIGH | rank 5 terminal row unpublished |
| Rank-up stat bonus | formula 1 + (stat_bonus/100) x rank_up_cnt | [NATIVE] formula | 85 | HIGH | coefficient 5% is a fixture |
| Transcendence ladder | 1-star: 5/50/5000, 15/150/15000, 45/450/45000; 2-star: 7/70/7000, 25/250/25000, 60/600/60000; 3-star: 9/90/9000, 30/300/30000, 80/800/80000; 4-star: 12/120, 40/400, 110/1100 (crystal/fragment/rupees) | [COMM] x2, 39 cells agree | 70 | MEDIUM | fragment:crystal 10:1 table-scoped; 2-star T3 60/600 single-source; era unresolved |
| Transcendence duplicates | 1 / 2 / 3 per T1/T2/T3 | [COMM] x2 | 70 | MEDIUM | same hunter consumed, fodder 3-star floor |
| Trace exchange threshold | per-hunter star-graded (fixture 10/20); Namu ladder 20/40/80/160 | [COMM] era-unresolved | 30 | CONTESTED | shape (doubling) corroborated; absolute value unrecovered; local 10/20 NOT upheld as error |
| Fight Club entry | 1 BP (fixture) | fixture | 10 | VERY LOW | BP economy native shape only, zero value agreements |
| Fight Club tier rewards | Silver/Gold 100 chips + 2 Manda; Emerald/Metron 150+2; Mandarin 200+2 | [COMM] single-source | 40 | LOW | Bronze row unrecorded (not zero) |
| Fight Club scoring | win +15, loss -8, defense loss -5 to -6, revenge/forfeit -8 | [COMM] x2 | 65 | MEDIUM | two-source agreement |
| Fight Club rank rewards | 31 bands: rank 1 = 2500 chips + 800 Manda, descending 100 chips/band to 30000+ = 100 chips + 1 fuel coupon | [COMM] single-source | 35 | LOW | band 551-720 pays 255 (sic, preserved anomaly); Manda ends at rank 4700 |
| Arena rival refresh | UNKNOWN (fixture price_type 2 / 100) | fixture | 10 | VERY LOW | no table vocabulary for refresh_price |
| Attendance events | Sep 2018: 30 Manda/day x 9 = 270; Halloween: 20/day x 15 = 300 | official posts | 80 | HIGH | event-parameterised; no fixed daily number exists |
| Lootbox | 1 box per 30 Manda or 200 fuel; 11 prizes, no probability column | official post | 60 | MEDIUM | 300 fuel is itself a prize |
| Weekly first-purchase bonus | 1 Special Request + 40 traces | official post | 60 | MEDIUM | two independent 2018 events granted 10 per 10+1 |
| Login calendar | UNKNOWN (fixture 28 days x 100 gold; day3/day4 claimed natively at 100 gold + 20 VIP EXP, §146/§155) | fixture + [NATIVE] claim path | 15 | VERY LOW | claim/receipt mechanics native-verified; the 100-gold amounts remain local fixture |
| Episode material settlement | E01 GC2x3 pending claim; **E02 FMD1x30 natively credited (free Manda 239640→239670, §164)**; E03-E17 need item rows GC3/GC4/GC8/OV1/CERUM01-03/SK13/23/33/43/EM02/LCOIN/GC9-11 | [ORIGDATA] declarations + [NATIVE] receipt | 75 | MEDIUM-HIGH | quantity x30 is original; the wallet mapping is replica policy; E01 auto-request was correctly refused (§162) |
| Team EXP ladder | UNKNOWN (fixture two-row 0/100 caps team level 2) | [COMM] EXP-to-max 200/400/1200/4800/24000 = 200 x R! | 35 | LOW | grade ladder multi-source; per-level step min_exp unrecovered from 7 corpora |
| Grade EXP-to-max | 1-star 200, 2-star 400, 3-star 1200, 4-star 4800, 5-star 24000 | [COMM] x3-6 + in-client corroboration (§156) | 95 | HIGH | ratio 1:2:6:24:120 = 200 x R!; endpoints verified against owned native levels; interior thresholds remain unknown |
| Star-advancement rupees | 1000 / 3000 / 12000 unanimous; 4-star to 5-star 60000 (x5) vs 15000 (x1 dissent) | [COMM] x6 | 65 | MEDIUM | different axis from transcendence; fodder 1/2/3/4 same-grade |
| Equipment upgrade breakpoints | 500/1000/5000/15000/30000/100000 at Lv 10/20/30/40/50 (community) | [COMM] | 45 | LOW | garbled Namu toolbox costs 500/1000/5000 NOT transcribed as exact |
| Polish / gem prices | UNKNOWN (schema [NATIVE]: level, price_type, price, possibility, failed_compensation, add_sub_ability) | [NATIVE] schema | 50 | MEDIUM | zero original row values; polish is probabilistic, fail loses rupees only |
| Gem mining price | UNKNOWN — no native route isolated | negative | 5 | VERY LOW | Check10GatchOverGemMineLimit is a limit check, not a price |
| Chest payouts (10/20/30 stars) | UNKNOWN (fixture 300/200/100 gold) | [NATIVE] mechanism, amounts missing | 15 | VERY LOW | chest item identities 912/913/914 = 2/3/4-star Transcendence Tickets [ORIGDATA] |
| Fishing settlement | BLOCKED — original fish item reference missing; EndWithSell posts log_id:"-1" (wire-verified); terminal ACK is 27/2 | [NATIVE] wire + [ORIGDATA] parser | 50 | MEDIUM | missing reference falls back to DUMMY zero INFO — NOT a legitimate catch; no empty-catch success until a real fish row exists (§143–145) |

## K. Non-card catalogue rows (items, no stats)

| ID | Meaning | Conf% | Word | Notes |
|---|---|---:|---|---|
| 901/902/903/904 | premium/free currency display identities | 80 | HIGH | Manda display identities [ORIGDATA] |
| 912/913/914 | 2/3/4-star Transcendence Tickets (area chests) | 90 | HIGH | CHAR_STR_RO rows; quantities unknown |
| x914 | variant of 914 | 60 | MEDIUM | |
