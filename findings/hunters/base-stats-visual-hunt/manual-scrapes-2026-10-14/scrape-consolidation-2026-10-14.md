# Manual scrapes consolidation — 2026-10-14

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Outputs (this consolidation only): `scrape-hits-consolidated.tsv` (119 hit rows,
15 source cols + `batch`), this file. No other file was modified: promotion
decisions belong to the owner; evidence only.

Inputs read (not modified): `batch-01.tsv` … `batch-73.tsv`, `batch-NN-hits.md`
(x73), `hits/` crops, `../hero-at-draw-estimates-2026-10-11.tsv` (113 rows),
`catalog/legacy-catalogue-data/card-catalogue.tsv` (121 rows).

Growth model (per task): stat(L) = at_draw x (1+r)^(L-1) with HP r=1.879%,
ATK r=1.852%, DEF r=1.930% (generic 1.88% quoted in
`hero-archetype-guesstimate-2026-10-11.md`). Implied at-draw = obs / (1+r)^(L-1).
Deviation % = (implied - estimate) / estimate x 100, per stat.
Confirm bar: all three stats within +/-15% (tier B/C/D). Conflict bar: any stat
beyond +/-30%. Between 15-30% is reported as borderline, never as confirmation.

## 1. Validation

- All 73 batch TSVs present. Headers identical (15 cols) in every file.
- Row counts: 50 rows in batch-01 … batch-72, 26 rows in batch-73. Total 3626.
- idx contiguous 1-3626, no gaps, no duplicates, no out-of-range values.
  Per-batch ranges exact: batch-NN holds idx (N-1)*50+1 … N*50 (batch-73: 3601-3626).
- Filenames: no duplicates across all 3626 rows.
- Column-shift caveat (batches 03/05/18): 91 rows carry 14 fields instead of 15
  (3 in batch-03, 43 in batch-05, 45 in batch-18) — the `stars` field was omitted
  at scrape time, shifting catalog/numbers/gear/hit/confidence one slot left
  (their `hit` slot holds confidence text such as `high`). All 91 are non-panel
  screens (fight-club grids, attendance, fishing, etc.), zero contain `YES`, and
  the consolidation parser re-inserts the empty `stars` slot. No hit row is
  affected. Recommend fixing the 91 rows at source (insert empty `stars`); the
  consolidated TSV already reflects the corrected alignment.
- `manifest.tsv` present (3627 lines incl. header: idx/filename/batch).
- 73/73 `batch-NN-hits.md` files present; `hits/` holds 121 entries.

## 2. Hit census — 119 YES rows

37 batches contain hits; 36 batches contain zero (02, 04-10, 14, 21, 22, 24,
26-29, 31, 34-45, 48, 52, 65, 70-73). Batches 70-73 (tail, idx 3451-3626) have
no qualifying stat blocks per their hits.md (badge zooms only).

By catalog ID (blank = unmapped at scrape time, resolved below):

| catalog | n | idx |
|---|---|---|
| 001 Lantern | 3 | 1108, 2820, 3446 |
| 004 Tyltyl | 2 | 2657, 2715 |
| 005_1 Gerard (Awak.) | 3 | 831, 3415, 3416 |
| 008 Akasha | 1 | 2437 |
| 009 HITLER | 1 | 1241 |
| 010_1 Vincent (Awak.) | 1 | 3436 |
| 012 Karl Steiner | 4 | 506, 2610, 2615, 3158 |
| 016 Bruce Bang | 1 | 2824 |
| 017_1 Lapis (Awak.) | 1 | 1603 |
| 020_1 Sienna (Awak.) | 1 | 123 |
| 021 Rebecca | 1 | 2740 |
| 022 Sunny | 3 | 556, 2333, 2901 |
| 023 Hermes | 8 | 507, 642, 859, 2312, 2542, 2905, 3008, 3031 |
| 024 Riko | 1 | 2336 |
| 025 Teddy Bomber | 1 | 1221 |
| 027 Athena | 1 | 2755 |
| 028 Octavia | 4 | 880, 2416, 2647, 3394 |
| 029 Kain | 2 | 1133, 2641 |
| 031 Diana | 1 | 2712 |
| 033 Patrone | 4 | 2296, 2417, 2769, (3298 blank, mapped) |
| 036 Bear | 2 | 1204, 3320 |
| 040 Bibi | 6 | 1462, 2489, 2649, 2857, 2890, 2940 |
| 043 Papillon | 2 | 868, 2970 |
| 044 Heidi | 2 | 2767, 3163 |
| 045 Yuri | 2 | 2607, 2941 |
| 047 Lily & Lyla | 3 | 2493, 2640, 2663 |
| 048 Dumble | 1 | 2733 |
| 049 Bright | 1 | 3067 |
| 051 Beckhen | 3 | 799, 3108, 3321 |
| 052 Windblade | 6 | 1585, 2809, 2911, 2971, 3028, 3050 |
| 053 Calibur | 2 | 118, 2968 |
| 054 Dino | 2 | 864, 2821 |
| 055 Apollon | 1 | 2908 |
| 056 Genovia | 1 | 764 |
| 057 Pansy | 3 | 829, 2915, 3385 |
| 058 Crocus | 1 | 2955 |
| 061 Chichi | 1 | 621 |
| 062 Juno | 1 | 5 |
| 063 Erise | 4 | 703, 2958, 3027, 3317 |
| 064 Geranium | 1 | 2969 |
| 065 Teresa | 3 | 713, 3122, 3346 |
| 066 Mary | 1 | 3306 |
| 068 Selene | 1 mapped | (3280 blank) + 3330 recruit |
| 071 Anemone | 2 | 971, 996 |
| 079 Lawrence | 2 | 795, 3325 |
| 081 Monica | 2 | 926, 3307 |
| 083 Kamala | 1 + 1 mapped | 3151 + (3290 blank) |
| 084 Lottery Mouse | 2 | 848, 3342 |
| 089 Clara | 1 | 1601 |
| 095 Lawrence (swim) | 1 | 3302 |
| 096 Estelle | 1 | 3347 |
| (blank, resolved) | 13 | see below |

Blank-catalog hits resolved by hero name/title (kept blank in the TSV; mapping
is evidence, not source edit): 2269 Tyltyl (title In Wonderland — costume
variant, base 004 is Worlds Best Cook/Fire); 2330 Riko (Halloween Witch costume;
base 024 is Hard-Knock Life); 2342 Tyltyl (same costume); 3272 Gullveig -> 039;
3280 Selene -> 068; 3281/3286 Celine -> 069; 3288/3289 Judith -> 067; 3290
Kamala -> 083; 3298 Patrone -> 033; 3300 Blondie -> 077; 3417 Whiteheart_ ->
009_1 (displayed name is a player nickname; title Eternal Flame matches catalog
009_1 Captain Awakened).

Full-triple (HP+ATK+DEF) panels at a stated level: 22 rows (section 3). All
other hits are Strength-only or recruit-splash class (name+title+level+stars,
no HP/ATK/DEF) — census value only.

## 3. Back-calculation table (implied at-draw vs tier estimate)

`obs` = panel HP/ATK/DEF; `impl` = obs deflated by the level model; `est` =
current hero-at-draw-estimates value; `dev` = deviation %. `*` = third stat
label cut off, treated as provisional DEF. `J` = jewel/gear decomposition
available (section 5).

| panel | cat/tier | L | obs HP/ATK/DEF | impl HP/ATK/DEF | est HP/ATK/DEF | dev HP/ATK/DEF |
|---|---|---|---|---|---|---|
| Sienna-123 | 020_1 D | 30 | 3772/2914/1687 | 2198/1711/969 | 2557/1681/1153 | -14.0/+1.8/-16.0 |
| Karl-506 | 012 A | 30 | 2645/1477/1027 | 1542/867/590 | 1750/1007/689 | -11.9/-13.9/-14.4 |
| Hermes-507 | 023 A | 30 | 2610/1418/968 | 1521/833/556 | 1750/937/653 | -13.1/-11.1/-14.8 |
| Sunny-556 | 022 A | 30 | 3047/1379/1577 | 1776/810/906 | 1584/718/718 | +12.1/+12.8/+26.2 |
| Chichi-621 | 061 A | 30 | 2463/1258/1008 | 1436/739/579 | 1821/937/798 | -21.2/-21.1/-27.4 |
| Hermes-642 | 023 A | 30 | 2949/1664/1133 | 1719/977/651 | 1750/937/653 | -1.8/+4.3/-0.3 |
| Teresa-713 | 065 C | 30 | 3719/1641/1902 | 2168/964/1093 | 1847/870/821 | +17.4/+10.8/+33.1 |
| Octavia-880 | 028 A | 30 | 2382/1216/960 | 1388/714/551 | 1750/901/689 | -20.7/-20.7/-20.0 |
| Anemone-996 | 071 B | 30 | 3619/1570/2372 | 2109/922/1363 | 2026/844/1053 | +4.1/+9.3/+29.4 |
| Clara-1601 | 089 C | 30 | 4197/1931/2149 | 2446/1134/1234 | 1847/870/821 | +32.4/+30.4/+50.4 |
| Lapis-1603 | 017_1 D | 30 | 4501/2382/1849 | 2623/1399/1062 | 2943/1531/1177 | -10.9/-8.6/-9.8 |
| Hermes-3008 | 023 A | 1 | 637/507/358 | 637/507/358 | 1750/937/653 | -63.6/-45.9/-45.2 |
| Hermes-3031 | 023 A | 30 | 3187/1977/1227 | 1857/1161/705 | 1750/937/653 | +6.1/+23.9/+7.9 |
| Hermes-3031J naked | 023 A | 30 | 3104/1657/1198 | 1809/973/687 | 1750/937/653 | +3.4/+3.9/+5.2 |
| Kamala-3151 | 083 B | 1 | 1323/613/892 | 1323/613/892 | 2026/844/1053 | -34.7/-27.4/-15.3 |
| Karl-3158 | 012 A | 30 | 3574/2083/1439 | 2083/1223/827 | 1750/1007/689 | +19.0/+21.5/+20.0 |
| Heidi-3163 | 044 A | 30 | 2864/1679/1296 | 1669/986/744 | 1750/952/689 | -4.6/+3.6/+8.1 |
| Selene-3280 | 068 C | 24 | 1204/1031/607 | 785/676/391 | 1692/1126/652 | -53.6/-40.0/-40.0 |
| Celine-3281 | 069 B | 30 | 2734/1257/1210 | 1593/738/695 | 1872/836/848 | -14.9/-11.7/-18.0 |
| Judith-3289 | 067 C | 1 | 994/811/532 | 994/811/532 | 1641/1113/734 | -39.4/-27.1/-27.5 |
| Kamala-3290 | 083 B | 1 | 1173/548/764 | 1173/548/764 | 2026/844/1053 | -42.1/-35.1/-27.4 |
| Patrone-3298 | 033 A | 1 | 1132/887/657 | 1132/887/657 | 1521/1003/726 | -25.6/-11.6/-9.5 |
| Lawrence-3302 | 095 B | 18 | 2994/1341/1716 | 2182/982/1240 | 2026/844/1053 | +7.7/+16.3/+17.7 |
| Pansy-3385* | 057 A | 1 | 561/369/374 | 561/369/374 | 1742/762/806 | -67.8/-51.6/-53.6 |
| Gerard-831 | 005_1 D | 8 | 3632/1463/2275 | 3188/1287/1990 | 3092/1295/1588 | +3.1/-0.6/+25.3 |
| Gerard-3415* | 005_1 D | 26 | 3910/1575/2392 | 2455/996/1483 | 3092/1295/1588 | -20.6/-23.1/-6.6 |
| Whiteheart-3417* | 009_1 D | 28 | 4266/1792/2375 | 2581/1092/1417 | 3092/1295/1588 | -16.5/-15.7/-10.7 |
| Vincent-3436 | 010_1 D | 30 | 4833/2626/2077 | 2817/1542/1193 | 2943/1531/1177 | -4.3/+0.7/+1.4 |

Excluded from back-calc (no usable triple): Teresa-3122 (HP 6.0% is a Hunter
Bonus toast, not a stat); Celine-3286 (HP 12.0% toast, digit cut); Gerard-3416
(same-session duplicate of 3415, identical values — counted once).

## 4. Tier-promotion evidence (B/C/D, all three stats within 15%)

- Vincent-3436 (010_1, D): -4.3/+0.7/+1.4 — STRONG. Clean Lv.30 5-star triple,
  skills 50/50 x5. Supports tier-D awakened x1.45 construction for 010_1.
- Lapis-1603 (017_1, D): -10.9/-8.6/-9.8 — CONFIRM. Lv.30 5-star triple,
  skills 50/50 x5. Directly retires part of the Reddit gear-polluted anchor
  range (1.30-1.93) for Awakened Lapis: this panel implies an awakened factor
  ~1.29-1.33 against its base, at the bottom of the old polluted band.
- Sienna-123 (020_1, D): -14.0/+1.8/-16.0 — BORDERLINE confirm. HP inside,
  ATK near-exact, DEF 1 point outside the bar; panel shows equipped gear
  (50/50 x6), so the naked-base truth is lower and DEF would move further out.
  Keep at D-pending; needs a naked-base decomposition as in section 5.
- Anemone-996 (071, B): HP +4.1 / ATK +9.3 confirm; DEF +29.4 borderline-high
  (inside the 30% conflict bar but far outside 15%). Tier-B median triple
  (2026/844/1053) can stand, but the shared B-ladder DEF leg (1053) looks
  ~25-30% light against this panel. Evidence for B, with a DEF-method flag.
- Celine-3281 (069, B): -14.9/-11.7/-18.0 — BORDERLINE. First direct Celine
  triple (recruit->trained pair with 3286, +2 days). HP/ATK confirm the
  dual-method B point (1872/836/848); DEF 3 points outside.
- Lawrence-3302 (095, B): +7.7/+16.3/+17.7 — BORDERLINE (mid-curve L18,
  skills 50/50 x5). HP confirms; ATK/DEF sit just above the bar. Consistent
  with B, not promotion-grade alone.
- Gerard-831 (005_1, D): HP +3.1 / ATK -0.6 confirm; DEF +25.3 borderline-high
  (fate materials partial 43/50 + 45/50, so panel may carry material bonuses).
  Supports D for 005_1 on two legs; DEF leg unresolved.
- Whiteheart-3417 (009_1, D): -16.5/-15.7/-10.7 (provisional DEF) — just
  outside on HP/ATK, inside on DEF. Title-matched to 009_1 (nickname display).
  Weak-support for D, provisional only.

No tier-A row is promotion-relevant (archive ~100%); Tier-A deviations are
model/gear diagnostics (section 5).

## 5. Conflicts (>30% deviation) — explicit, no overwrites

- Clara-1601 (089, C): +32.4/+30.4/+50.4 on ALL THREE legs — CONFLICT with the
  tier-C archetype point (1847/870/821). Caveat: panel carries skills 50/50 x5
  with unknown gear; gear inflates the observed side, so a naked-base
  decomposition (as done for Hermes-3031) could reconcile part of it — but
  reconciling +50% DEF needs ~35% gear inflation, above every measured quantum
  (section 6: +2-19%). Verdict: genuine conflict pending gear decomposition;
  do NOT silently keep C on this hero without that check.
- Teresa-713 (065, C): DEF +33.1 CONFLICT; HP +17.4 / ATK +10.8 confirm-ish.
  Same gear caveat (skills 50/50 x5). The C archetype DEF leg (821) is the
  disputed leg; HP/ATK legs stand.
- Selene-3280 (068, C): -53.6/-40.0/-40.0 — NUMERICAL conflict, but the panel
  is 4-star at Lv.24 with partial skills (40/40, 32/40, 30/40, 30/40, 5th
  locked): it is NOT in the 5-star state the ladder-anchored C point assumes.
  Verdict: star-state effect, not estimate refutation. Needs a 5-star Selene
  panel before any conclusion on 068.
- Kamala-3151/3290 (083, B): two independent Lv.1 4-star draws agree with each
  other (HP 1323 vs 1173, ATK 613 vs 548, DEF 892 vs 764: 12-17% apart) but sit
  -35/-27/-15 and -42/-35/-27 under the tier-B point. Lv.1-caveat applies
  (section 6): Lv.1 draw-state panels are proven NOT to be in at-draw units
  (Hermes-3008 vs ~100% archive). Verdict: conflict-with-caveat; the pair
  caps any B-point revision (their mean 1248/580/828 is the draw-state floor).
- Judith-3289 (067, C): -39.4/-27.1/-27.5 at Lv.1 4-star draw state (85-min
  recruit->trained pair with 3288). Same Lv.1 caveat; HP leg exceeds 30% but
  the estimand mismatch dominates. First direct Judith triple regardless.

## 6. Gear / star-state calibration (why sections 4-5 are hedged)

Same-hero same-level spreads (gear/skill/client noise) reach 35-40%, i.e. the
15% confirm bar sits INSIDE demonstrated gear noise:

- Hermes-023 Lv.30 5-star x3: implied 1521/833/556 (507, no gear) vs
  1719/977/651 (642, +13/+17/+17%) vs 1857/1161/705 (3031, jewel-loaded).
  Batch-13 hits.md explicitly flags 507->642 as a gear delta.
- Karl-012 Lv.30 5-star x2: 1542/867/590 (506, 2018 client, no gear) vs
  2083/1223/827 (3158, 2020, skills 50/50 x5 + Equipment red-dot):
  +35/+41/+40% spread.
- Bibi re-train pair (2857 -> 2890, batch-58 hits.md): Strength 9444 -> 10127
  (+7.2%) with identical hero/level/stars and no advancement — pure
  gear/skill noise floor on Strength.
- Measured gear quanta: idx 2897 equipment screen (+222 HP / +157 ATK / +69 DEF
  on ~2821/1411/1266: +8/+11/+5%); batch-61 Hermes jewel decomposition
  (+83/+320/+29 on 3104/1657/1198: +3/+19/+2%); transcendence strips +12%
  (batch-61 idx 3009/3026).
- Gold-standard decomposition — Hermes-3031: jewel screen idx 3033 gives the
  naked base 3104/1657/1198, whose implied values (1809/973/687) land
  +3.4/+3.9/+5.2% on the ~100%-confidence archive row (1750/937/653). This
  single panel validates the archive row AND the 1.88%-class growth model
  simultaneously. All future promotions should aim for this decomposition
  standard (naked-base triple + stated level + 5-star).
- Lv.1 panels are NOT in at-draw units: Hermes-3008 Lv.1 3-star triple
  (637/507/358) sits -64/-46/-45% under its own ~100% archive row; Pansy-3385
  Lv.1 3-star (561/369/prov-374) sits -68/-52/-54%. Draw-state display excludes
  whatever the archive/at-draw estimand includes (transcendence ladder,
  bonuses). Consequence: Lv.1-implied values (Kamala, Judith, Patrone-3298 at
  4-star: -26/-12/-10 vs archive) must NOT be used as promotion evidence
  without a star-state correction; they are first-direct-panel census plus a
  draw-state floor.

## 7. Growth-shape findings (mid-curve + pairs)

- Gerard-005_1 is the ONLY within-star-state level pair: L8 (831:
  3632/1463/2275, fate mats partial) vs L26 (3415: 3910/1575/prov-2392, skills
  50/50). Under gear-equal assumption the pair implies ~0.4%/level, far under
  the 1.88% model (which predicts L26/L8 HP ratio 1.40 vs observed 1.08).
  Gear-equal is likely false (different sessions/years/clients), so the pair
  instead bounds combined model+gear uncertainty at ~25-30% over 18 levels.
  Needs a gear decomposition, not a model rewrite — but the model cannot be
  confirmed from this pair.
- Mid-curve anchors are Strength-only except Selene-3280 (L24, triple, 4-star
  — section 5) and Lawrence-3302 (L18, triple, 5-star — section 4): Diana L7
  (2712), Windblade L10 (2809), Lily & Lyla L16 (2493), Tyltyl L17 (2715),
  Octavia L15 (2647, Strength-only), Dino L28 (2821), Geranium L28 (2969),
  Whiteheart L28 (3417, triple, prov-DEF), Gerard L26 (3415, triple, prov-DEF).
  They trace the Strength curve qualitatively only; no HP/ATK/DEF shape
  constraint except the Gerard pair.
- L1 <-> L30 spans star states (3-star card-detail 3008 vs 5-star 3031:
  4.9x HP over 29 levels = 5.6%/level effective) — transcendence/star
  multipliers dominate raw level growth. The 1.88% model is valid WITHIN a
  fixed star/transcendence state only (as validated by 3031-naked).
- Re-train pair Bibi 9444 -> 10127 (+7.2%, no advancement) and recruit->trained
  pairs Anemone (971 splash -> 996 L30 triple), Celine (3286 splash -> 3281 L30
  triple, +2 days), Judith (3288 splash -> 3289 L1 triple, +85 min) document
  draw->train transitions; Celine's is the only draw-to-maxed-5-star chain.

## 8. Special-attention answers

(a) Awakened forms: Sienna-020_1 (123, borderline-confirm), Gerard-005_1
(831 + 3415/3416 pair, HP/ATK-confirm), Lapis-017_1 (1603, confirm; retires
the top of the old polluted band), Vincent-010_1 (3436, strong confirm),
Whiteheart->009_1 (3417, weak-support, provisional DEF). No Anemone-095 panel
exists — 095 is Knight-of-Swimming-Pool Lawrence (3302, tier B), not an
awakened form; nothing to pair.
(b) Tier-C first direct panels: Teresa-065 (L30 triple, DEF-conflict +
HP/ATK-ok), Monica-081 (L1 recruits 926/3307, no triple), Celine-069 is tier B
(L30 triple, borderline), Judith-067 (L1 triple 3289, first ever), Selene-068
(L24 triple 3280, 4-star + L1 recruit 3330), Kamala-083 is tier B (L1 triples
x2), Patrone-033 is tier A (L1 triple 3298), Blondie-077 (L1 splash 3300 only),
Clara-089 (L30 triple 1601, full conflict), Katrina-090 (ZERO hits — gap),
Estelle-096 (L1 splash 3347 only). Erise-063: L30 Strength-only (703: 30155)
+ L1 recruits — no triple, no back-calc.
(c) Mid-curve: see section 7. Only Selene-L24 and Lawrence-L18 carry triples.
(d) Pairs: Bibi 9444 -> 10127 re-train (+7.2%, section 6); Hermes 507/642/3031
gear-delta trio (section 6); Anemone / Celine / Judith recruit->trained chains
(section 7).

## 9. Remaining gaps

- Katrina-090 (tier B): zero hits across all 3626 rows. Highest-priority gap
  among named task heroes.
- Tier-B/C/D heroes with hits but NO triple (recruit/Strength-only, no
  back-calc possible): 056 Genovia, 064 Geranium (L28 Strength-only), 066 Mary,
  079 Lawrence (base), 081 Monica, 084 Lottery Mouse, 096 Estelle, 077 Blondie,
  063 Erise, plus 095-swim needs an L30 mate for its L18 panel.
- 36 zero-hit batches (section 2); tail batches 70-73 structurally hit-free
  (no stat panels: badge zooms, trace screens, selects).
- 13 blank-catalog hits need catalog-side resolution (costume variants
  Tyltyl-In-Wonderland, Riko-Halloween-Witch; nickname Whiteheart_; batch-66
  crew mappable to 039/067/068/069/077/083/033 as listed in section 2).
- Method upgrades for promotion-grade evidence: naked-base (jewel/gear-off)
  decompositions a la Hermes-3031/idx-3033 for every section-4/5 hero;
  a 5-star Selene panel; an L30 mate for Lawrence-095-L18; a same-state level
  pair (a la Gerard L8/L26) with documented equal gear to pin the growth rate.
