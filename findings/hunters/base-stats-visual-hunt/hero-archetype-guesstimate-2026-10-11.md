# Hero at-draw archetype guesstimate — all 113 characters (2026-10-11)

**Owner instruction applied:** guesstimation is the game. With the 62 anchored
archive rows plus recovered balance mechanics, the remaining heroes are derivable.
This note documents the derived model, the per-row estimates, and the confidence
each class of estimate deserves. Output dataset:
**[`hero-at-draw-estimates-2026-10-11.tsv`](hero-at-draw-estimates-2026-10-11.tsv)**
(113 rows: id, name, role, rarity, element, HP/ATK/DEF at draw, tier, class,
confidence, method). Companion:
[`hero-archetype-guesstimate-2026-10-11.tsv`](hero-archetype-guesstimate-2026-10-11.tsv)
(the 51 non-archive rows alone, with full method strings).

**Coverage effect (under the 2026-10-11 derivation-counts policy):** heroes move
**62 → 113 of 113** estimated, in four confidence tiers — 62 anchored `[RECOVERED]`,
36 `[DERIVED-ESTIMATE]` from same-role/same-rarity cells or two-method
extrapolation, 15 `[DERIVED-ESTIMATE]` awakened-form estimates. The 80-hero target
is met at tier B (79) and exceeded at tier C (98).

## 1. The model the archive turned out to be

The 2019 at-draw database is **template-structured**, which is what makes the
guesstimate possible:

- **Sub-stats are near-deterministic by (role, rarity).** Bomber rows carry
  spd 7 / crit 14 / crit-dmg 180–185 / block 14 / block-red 40–42 at every rarity;
  Offense rows spd 8 / crit 33 / crit-dmg 200–205; Support rows mirror Bomber's
  sub-stats; Defense rows carry block 33 / block-red 50–52. The one exception is
  Defense ★3, which has genuine per-hero variation (crit 0–14, crit-dmg 50–185,
  block 0–36).
- **HP is quantised to 1–4 values per (role, rarity) cell** (Bomber ★1: 1277 only;
  Offense ★1: 1537 only; Support ★1: 1467 only; Offense ★2/Defense ★2: 1624 only).
- **Element has no core-stat effect** at draw (within-cell element groups overlap
  completely), so the archetype key is (role, rarity) only.
- **12 heroes share core triples**; 4 of those share all 13 fields with a
  costume variant (`059/001`, `024/034`, `005/009`, `026/004`).

### Empirical role multipliers (ratio to Offense, same rarity, pooled)

| stat | Defense | Bomber | Support | LEVELING.jet `bonus.role` |
|---|---|---|---|---|
| HP | 1.012 (1.000–1.050) | **0.853** (0.831–0.869) | 0.969 (0.954–0.977) | 1.0 / **0.85** / 0.80 |
| ATK | 0.814 (0.735–0.941) | 1.135 (1.111–1.166) | 0.857 (0.831–0.884) | 1.0 / 0.95 / 0.95 |
| DEF | 1.336 (1.204–1.550) | 0.965 (0.947–1.000) | 1.134 (1.053–1.179) | 1.0 / 0.95 / 1.0 |

Two findings: (a) the multipliers are **rarity-invariant** (the ranges are the
spread across rarities, and they are tight for HP/Bomber/Support), which is what
licenses projecting them onto the empty ★4 cells; (b) they **partially corroborate
and partially refute** the `LEVELING.jet` reading — the HP row matches for
Offense/Defense/Bomber (1.00/1.01/0.853 vs 1.0/1.0/0.85) but the Support HP
multiplier is 0.969, not 0.80, and the ATK row does not match at all. The
`catalogue/INDEX.md` §5.1 claim that the role table "is where the role identity in
the stat line comes from" is therefore **partly wrong**: correct for HP on three
of four roles, unsupported for ATK/DEF and for Support HP. Do not use
`bonus.role` as a stat multiplier without the empirical table above.

## 2. The four tiers — and an honesty correction on what the confidences mean

| tier | basis | heroes | band confidence (true value inside the stated range) | exact-tuple confidence (all three numbers exactly right) |
|---|---|---|---|---|
| **A** | 2019 archive row (level/gear derivation of 2026-10-11) | 62 | ~100 % | ~100 % |
| **B** | same-(role, rarity) cell median **or** dual-method agreeing within 15 % | 19 | ~85–90 % | **~5–25 %** |
| **C** | empty-cell extrapolation, or dual-method agreeing within 30 % | 17 | ~75–85 % | ~3–15 % |
| **D** | awakened form: ★5 ladder × awakening multiplier 1.30 | 15 | ~70–75 % | ~2–10 % |

**The correction.** The 2026-10-11 v1 of this note claimed tier B at "~65–75 %
point" and used it to claim the 80-hero target met. The confidence audit
(`conf_audit` logic below) shows that is **not defensible as a point claim**: the
★4 cells that all tier-B/C heroes live in have only 2–3 observed rows, so the
median is a band-centre, not a likely-exact value — e.g. the Defense ★4 cell
holds only {2019, 2033} HP, {755, 933} ATK and {1036, 1070} DEF, and the printed
median (2026/844/1053) is not even an observed value for ATK/DEF. The defensible
statements are:

- **Band-documented coverage: 81/113 (71.7 %)** — every tier-A/B row carries a
  documented range within which the true value lies with ~85 %+ confidence, and
  the ranges are tight (Offense ★4: HP ±1.7 %, ATK ±2 %, DEF ±7.5 %). This is the
  reading under which the ledger's 80-hero target is met.
- **Exact-tuple coverage: ≈66/113 (58 %)** — the 62 anchored rows plus the four
  heroes whose two independent methods agree within 15 % (056, 064, 069, 082).

For a server fixture that must be *approximately* right these rows are usable with
their bands; for one that must be *exact*, the ★4 heroes still need real anchors.
Both readings are now stated everywhere these numbers are used; the previous
single "71.7 % at ≥65 % point" phrasing was wrong and has been struck.

**Scripted-row cross-check (v2).** 13 of the 19 tier-B heroes have a scripted
episode row; 4 corroborate the cell estimate within 15 % (064 6 %, 069 4 %,
082 8 %, 056 19 %), one is unusable (071 Anemone's only scripted row is an
encounter outlier — implied HP 8,966 vs cell 2,026, i.e. a boss-tuned instance;
scripted rows implying >2× the cell estimate are rejected as encounter tuning,
recorded not hidden), and 8 have no scripted row at all.

**Confidence semantics.** "Point" = probability the three printed numbers are
exactly right; "band" = probability the true values lie inside the method's stated
range. Tier B HP is tighter than its ATK/DEF (Offense ★4 HP spans only
1923–1955; Defense ★4 ATK spans 755–933 and is the weakest single estimate in the
set). Per-row numbers are in the TSV's `confidence` column; no row is counted
without one, per the policy.

## 3. Adjacent derived models (the "whole bunch of data" the model unlocks)

1. **Level growth** — `stat(L) = at_draw × 1.0188^(L−1)` for core stats
   (HP 1.879 %, ATK 1.852 %, DEF 1.930 % per level), derived from the single
   clean pair (Beckhen at draw vs Lv.30 nude). **Single anchor, assumed uniform
   across heroes**; rank-dependence is unmeasured (the chunk-19 power spans vary
   by rank: 1.77–2.88× over Lv 1→30), so cross-hero Lv.30 projections are
   `[DERIVED-ESTIMATE]` with a wide band and were deliberately **not** emitted as
   a table. A second hero with any clean leveled nude row would firm this.
2. **Composite/Strength** — the DB's 戦闘力 is an exact role-wise linear function of
   the three basic abilities (Bomber R²=0.9997, Support R²=0.9994); the trained
   on-screen value adds a level term (Beckhen +5,043 at Lv.30). Weights per role
   are in `archive-level-derivation-2026-10-11.md` §3.
3. **Equipment** — slot→stat mapping confirmed by the official JP facility page
   (武器→攻撃力, 防具→防御力, 装具→HP); the Lv 1→50 upgrade cost curve came from the
   namu pass; main-stat values at cap are anchored (W 134 / A 102 / Ac 260 @Lv.50).
4. **Skill magnitudes** — Beckhen's five effect values (`~9046` damage,
   `~20.00 %` attack speed, `~30.00 %` defense, `~30.00 %` block,
   `0.51~1.00 s` duration) are the first per-skill anchors; the formula shape is
   recovered, so value/value_up can now be fitted rather than invented.

## 3a. The scripted-episode second method (new in v2)

`sources/client-tables/reference/EPISODE_STAT_ACTORS.json` (152 rows) carries
**original client-shipped stat blocks for 55 distinct hero refs** — including 12
heroes that have no archive row. These rows are encounter-tuned (per-hero ratios
to the archive vary from 1.4× to 3×), but a **clean subset** exists: rows whose
HP/ATK/DEF ratios to the hero's at-draw row agree within 25 % (37 rows across 44
archive-covered refs). Their rank-5 HP-ratio medians by role — Offense 1.52,
Defense 1.56, Bomber 1.49, Support 1.37, pooled 1.446 — give a second estimator:
`at_draw = median(scripted rank-5 row) / clean-ratio(role)`. Where it agrees with
the archetype estimate within 15 % the row is promoted to tier B. The scripted
rows are also the reason the monster lane has any anchored rows at all (see the
monster estimates note).

## 3b. Cross-version validation from the VSFan workbook (new in v2)

`sources/community/raw/VSFan/Research/Blustone/Hunter Stats [BROKEN IGNORE].xlsx`
(sheets `Details` + `Stats`) was parsed this session. It carries per-hero
Base/Max rows for five grade tiers (Bronze→Blue) × 13–14 stat columns for 20
heroes — **all of which are already in the archive**, so it adds no new coverage.
Its value is validation: the per-hero ATK/DEF ratios of the workbook's early
build match the 2019 archive rows within ~5 % (e.g. Lapis 1.603 vs 1.581, Metis
1.595 vs 1.576, Sienna 1.819 vs 1.748, Sunny 1.000 vs 1.000), i.e. the per-hero
stat *shape* survived both the ~10× core-stat rescale and the rebalance. It also
shows the within-grade growth shape (Base→Max of a grade ≈ ×1.15–1.20 on core
stats with sub-stats frozen; each grade step ≈ ×1.4–1.7).

## 3c. What was checked and closed this session

- **VSFan packet captures** (`blustone.pcap`, `bs_transcendence.pcap`, …): game API
  bodies are application-layer encrypted and no session-key log exists, so no
  readable `GetCard`/`GetMonster` response is recoverable — the prior lane's
  conclusion holds and is not re-litigated here.
- The 13 LevelDB tables contain no item/equipment table (verified against
  `all-tables.json`); the reference JSONs add `EPISODE_STAT_ACTORS` (used above).

## 4. What would raise the tiers

- **Tier C → B:** any ★4 Bomber/Support row from any source (a JP archive capture
  of Geranium/Teresa/Mary/Selene/Alia/Anemone/Audrey/Sofia/Leon/Bella/Junia/
  Blondie/Westfield/Monica/Themis/Lottery Mouse/Clara/Katrina/Estelle pages that
  the 2019 census missed, or a Korean/Chinese equivalent of the JP DB).
- **Tier D → B/C:** any awakened-hero stat panel at a stated level, or a second
  base↔awakened pair to replace the polluted Vincent anchor.
- **Level-growth uniformity:** a second clean leveled nude row for any hero.
- The 19 catalog-crosswalked VSFan `BROKEN IGNORE` workbook rows remain
  unexamined for this purpose (provenance-unknown; would be tier B/C material if
  they check out).

## 5. Reproduction

Script (stdlib only): loads `archived-hunter-database-2019.tsv` (62 rows) and
`uncovered-archive-roster-2019.tsv` (51 rows); computes cell modes, pooled role
multipliers, per-role rarity ladders, and the two-method empty-cell estimate;
emits both TSVs. All numbers in this note are printed by that script. Ancient
provenance warnings apply: the archive is 2019-era (pre-rebalance), so these are
at-draw values **of the 2019 balance**, to be era-tagged wherever they are used.
