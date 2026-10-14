# Batch 54 hits (idx 2651-2700)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-54-2657.png`, `hits/batch-54-2663.png` (2 HITs).
Zooms (lane folder, provenance only): `z54_2652_badge`
(Papillon 3-star gold + Lv.1), `z54_2657_badge` (Tyltyl 1-star
bronze + Lv.1), `z54_2663_badge` (Lily & Lyla 4-star green
ring + Lv.1), `z54_2681_nums` (5803 -> 7398), `z54_2696_prices`
(Fight Chips ladder).
OCR (lane folder): `_tmp54_ocr/` (zoom-crop tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`).
Write script: `_tmp54_write.py` (kept in lane folder per rules).

## HITs: 2/50

### idx 2657: In Wonderland Tyltyl, Amateur Hunter Lv.1, 1-star, Strength 289 (catalog 004)
- File: `Screenshot_20180501-110229-427c9c613fb3468b.png`
  (1080x1920). Crop: `hits/batch-54-2657.png`.
- Train Teammate; 1-star bronze badge + Lv.1 ribbon
  (zoom-verified `z54_2657_badge`); offense-hand icon;
  Train / Transcendence / Skill Training /
  Upgrade Equipment / Story.
- TITLE NOTE: client "In Wonderland" vs catalog 004
  "World's Best Cook" (intra-client title discrepancy
  class, recorded verbatim).

### idx 2663: Strange Twins Lily & Lyla, Proficient Hunter Lv.1, 4-star, Strength 4785 (catalog 047)
- File: `Screenshot_20180505-182058-c00afc509b30c2f9.png`
  (1440x2560). Crop: `hits/batch-54-2663.png`.
- Train Teammate; name rendered "Lily & Lyl"
  (right-edge cut, identity unambiguous with twin art);
  4-star green-ring badge + Lv.1 ribbon (zoom-verified
  `z54_2663_badge`); bomber two-finger icon.
- Cross-ref: the same twins are rated 0.07% in the
  recruit-probability notice idx 2668 and wanted at
  0/160 traces in idx 2691.

## Near-hits (full numbers, hit=no per bar rules)

### Recruit splashes with level + stars, no stats (all hit=no)
- idx 2652: Notorious Jail-breaker Papillon, 3-star gold
  badge + Lv.1 ribbon (zoom-verified `z54_2652_badge`;
  OCR "apilton" vs visual "Papillon", zoom wins),
  Defense + Ice, +1000 (catalog 043).
- idx 2676: Girl with Two Faces Heidi, 3-star, Lv.1,
  Offense + Fire, +1000 (catalog 044).
- idx 2678: Silent Canine Patrone, 3-star, Lv.1,
  Bomber + Ice, +1000 (catalog 033).
- idx 2679: Flame of the Battlefield Athena, 3-star,
  Lv.1, Defense + Fire, +1000 (catalog 027).
  TITLE NOTE: client "Flame of the Battlefield" vs
  catalog "Flame of Battlefield" (article).
- idx 2686: The Frost Witch Octavia, 3-star, Lv.1,
  Offense + Ice, +1000 (catalog 028). TITLE NOTE:
  client "The Frost Witch" vs catalog "Frost Witch"
  (extends the batch-51 arc).

### Transcendence result screens (named + Lv.MAX + stats, no star rank, hit=no)
- idx 2653: Wandering Fighter Balian, Lv.MAX, Strength
  16654 -> 18286 (+1632); Attack 1137 -> 1232;
  Defense 808 -> 876; Life 2139 -> 2317. TITLE NOTE:
  client "Wandering Fighter" vs catalog 019 "Wandering
  Swordsman" (catalog 032 Scar holds "Wandering
  Fighter").
- idx 2672: Wolf Child Bibi, Lv.MAX, Strength 18212 ->
  20210 (+1998); Attack 1116 -> 1218; Defense 971 ->
  1060; Life 2175 -> 2373. Title matches catalog 040.
- idx 2693: Silent Canine Patrone, Lv.MAX, Strength
  18860 -> 20777 (+1917); AP 1432 -> 1551; Defense
  1062 -> 1151; Life 2171 -> 2352. Stat labels are
  AP/Defense/Life (not ATK/DEF/HP).
- idx 2681: Proficient Hunter Lv.MAX 5803 -> Master
  Hunter Lv.1 7398 (+1595, x1.275, zoom-verified
  `z54_2681_nums`; OCR missed digits, zoom wins); New
  Skill Unlocked Cleaning Fairy. No hero name on frame.

## Cross-batch pairing notes

- Patrone intra-batch arc: idx 2673 ruins discovery
  (Patrone's ruins, JohnRiver) -> idx 2678 recruit
  splash (Silent Canine Patrone, 3-star, Lv.1) ->
  idx 2693 transcendence (Lv.MAX, 18860 -> 20777).
- Build-team scroll pair: idx 2689 (top team
  5891/4357/1287/457 + grid 7148/6438/6286) ->
  idx 2690 (scrolled grid 3064/3019/2750 ...
  2254/2181/1287 Exploring checked).
- Hunter-list scroll pair (36/45, same account): idx
  2699 (head 8268 ... 8444 Leader mid-grid) -> 2700
  (tail 3731/3704/3389 ... 2348 quadruple-dupe ...
  2068/1878). Roster endpoints 8444 -> 1878.
- Fishing story pair (Ornithopter Platform): idx 2685
  (X_man_20000, fuel 190/60) -> idx 2687 (Alaiko +
  Tyltyl fishing-era beat, fuel 31/60); different
  sessions.
- Discovery-banner ladder: idx 2671 (Solarxrays, Joy)
  / idx 2673 (JohnRiver, Patrone) / idx 2675
  (Eligar, Joy + 57/15/13 background traces).
- Missing-hunter window ladder: abyss 0day timers
  (2665 Cryogenic 00:57:02 / 2666 00:58:22 / 2670
  Electric 00:59:04 / 2680 00:26:35 / 2694 00:42:45)
  vs canyon windows 12day 01:22:58 (2670) / 10day
  04:31:25 (2680) / 3day 08:16:28 (2694, Search
  Complete on abyss row).
- Fight-club pair (Mandarin Tier, Begin Battle 1):
  idx 2683 (USER241BCE, tickets 7/10, single-Lv.1
  opponent) / idx 2684 (LastQuarter, tickets 1/10,
  3x Lv.MAX opponent).
- 11-pull result (idx 2677): 6x 1-star / 2x 2-star /
  3x 3-star; "One more time! 300".

## Most valuable economy/mechanic readings

- Fight Chips price ladder (idx 2696, top-6
  zoom-verified): Special Request x1 1500 / Metron
  Crystal x1 1000 / Karl Steiner's / Octavia's /
  Heidi's Traces x5 375 / Scar's / Gerard's /
  Acerola's Traces x5 75 / Unusual Metal Piece x5
  100; wallet 1825; list refresh 03:54:43. Trace
  tiers 375 vs 75 (5x ratio).
- Recruit probability notice (idx 2688): 3-star total
  4.76% over 18 hunters (9 New + 9 Original);
  Original 0.32% / New 0.21%; Lily & Lyla 4-star
  0.07% (= 1/3 of New 3-star) via Midgard 300%
  event.
- Trace-collection costs (idx 2691): Offense 11/12;
  Critical Damage Bonus 11.0% -> 12.0%; per-hunter
  costs 160 (Vincent 0 / Lily & Lyla 0) vs 80
  (Natalia 3 / Bibi 29 / Heidi 0 / Yuri 34);
  Bibi 29/80 + Yuri 34/80 nearest completion.
- Transcendence setup cost (idx 2659, Hermes): 3/3
  fodder (Lv.1 2338 x3), mats 95/80 + 433/800,
  80000 coins, wallet 81597.
- Advancement delta (idx 2681): Lv.MAX 5803 ->
  Lv.1 7398 (+1595), Cleaning Fairy skill unlock.
- Transcendence deltas: Balian +1632 (x1.098),
  Bibi +1998 (x1.110), Patrone +1917 (x1.102).
- Shop promo (idx 2656): Very Successful Purchase
  1600% x80000 coins + Veteran Point Gift
  Certificate 3.
- Trace payout (idx 2682): 5x finished, traces
  3/5/5/3/5 ("large number of hunter traces").

## Non-ASCII names (transliterated, for searchability)

- idx 2651: Singh Sajid Ahmed. idx 2652: Papillon.
  idx 2653: Balian. idx 2657/2685/2687: Tyltyl.
  idx 2659: Hermes. idx 2665/2670: Scythia. idx 2666/
  2694: taxa. idx 2671: Solarxrays (Joy). idx 2672:
  Bibi. idx 2673: JohnRiver (Patrone). idx 2675:
  Eligar (Joy). idx 2676: Heidi. idx 2678/2693:
  Patrone. idx 2679: Athena. idx 2680: Meltdowns.
  idx 2683: USER241BCE. idx 2684: LastQuarter.
  idx 2685: X_man_20000. idx 2686: Octavia. idx 2687:
  Alaiko. idx 2691: Vincent, Lily & Lyla, Natalia,
  Bibi, Heidi, Yuri. idx 2692: Dr_BubbleBurst.
  idx 2696: Karl Steiner, Octavia, Heidi, Scar,
  Gerard, Acerola. idx 2697: Joefilms. No
  Korean-script names in batch (idx 2661 placeholder
  string not transcribed as a name).

## Contaminants

- idx 2667: blue X selection marks are an external
  player annotation over the dispatch grid (not game
  UI), noted; numbers transcribed verbatim.
- idx 2668: OS status bar (20%, 3:13 PM) over the
  rate notice, transcribed and flagged non-game.
- No wiki/Discord contaminants, no error pairs.

## Sic list

- "Resets in 0" (idx 2658, zero-digit counters).
- "0day" x8 (idx 2665/2666/2670/2680/2694 abyss and
  Wolf's-Mouth timers, zero not letter O).
- "Wolfs Mouth" (idx 2665/2666, no apostrophe).
- "Lily & Lyl" (idx 2663, right-edge name cut).
- "Isnt" (idx 2685, no apostrophe); "T-Tyltyl"
  stutter kept verbatim.
- "Group Advancen" (idx 2697/2698/2699/2700, button
  cut at frame edge).
- "Flame of the Battlefield" (idx 2679, client
  article vs catalog 027).
- "The Frost Witch" (idx 2686, client article vs
  catalog 028).
- "Wandering Fighter" Balian (idx 2653, client title
  vs catalog 019 "Wandering Swordsman").
- "In Wonderland" Tyltyl (idx 2657, client title vs
  catalog 004 "World's Best Cook").
