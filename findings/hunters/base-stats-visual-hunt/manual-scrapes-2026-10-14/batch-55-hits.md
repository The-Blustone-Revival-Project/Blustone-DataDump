# Batch 55 hits (idx 2701-2750)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-55-2712.png`, `hits/batch-55-2715.png`,
`hits/batch-55-2733.png`, `hits/batch-55-2740.png` (4 HITs).
Zooms (lane folder, provenance only): `z55_2712_low`
(Strength 2059), `z55_2712_badge` (3-star gold + Lv.7),
`z55_2715_str` (Strength 8282), `z55_2715_badge` (5-star
blue ring + Lv.17), `z55_2733_low` (Strength 2107),
`z55_2733_badge` (3-star gold + Lv.1), `z55_2740_str`
(Strength 9450), `z55_2740_badge` (4-star blue ring +
Lv.1), `z55_27xx_mid` (portrait-strip work views),
`z55_2707_timer` / `z55_2722_timer` (0day glyph crops).
OCR (lane folder): `_tmp55_ocr/` (full-frame tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`).
Write/verify scripts: `_tmp55_dims.py` (dims probe),
`_tmp55_write.py`, `_tmp55_verify.py` (kept in lane
folder per rules). Dims: `_tmp55_dims.tsv`.

## HITs: 4/50

### idx 2712: Thunder Arrow Diana, Experienced Hunter Lv.7, 3-star, Strength 2059 (catalog 031)
- File: `Screenshot_20180526-213507-2853c8d138b2eb0f.jpg`
  (720x1280). Crop: `hits/batch-55-2712.png`.
- Train Teammate; Bomber-class + ice-element icons;
  3-star gold badge + Lv.7 ribbon (zoom-verified
  `z55_2712_badge`); Strength 2059 (zoom-verified
  `z55_2712_low`); Train / Transcendence /
  Skill Training / Upgrade Equipment(grey) / Story.
- ELEMENT NOTE: displayed ice vs catalog 031 Lightning.

### idx 2715: World's Best Cook Tyltyl, Master Hunter Lv.17, 5-star, Strength 8282 (catalog 004)
- File: `Screenshot_20180528-070654-29b57ca90b0d0f41.jpg`
  (1080x1920). Crop: `hits/batch-55-2715.png`.
- Train Teammate; Support-class + fire-element icons
  (match catalog 004 Support/Fire); 5-star blue ring +
  Lv.17 ribbon (zoom-verified `z55_2715_badge`);
  Strength 8282 (zoom-verified `z55_2715_str`); Train /
  Transcendence / Skill Training / Upgrade Equipment
  (grey) / Story.
- STAR NOTE: Train badge shows a 5-star blue ring but
  catalog 004 lists base rarity 1 (star-display vs
  catalog-rarity difference, recorded verbatim).

### idx 2733: Strange Old Man Dumble, Experienced Hunter Lv.1, 3-star, Strength 2107 (catalog 048)
- File: `Screenshot_20180608-103301-71cbb2314a5b512c.jpg`
  (720x1280). Crop: `hits/batch-55-2733.png`.
- Train Teammate; shield-class + snowflake-element
  icons; 3-star gold badge + Lv.1 ribbon
  (zoom-verified `z55_2733_badge`); Strength 2107
  (zoom-verified `z55_2733_low`); Train /
  Transcendence / Skill Training / Upgrade Equipment
  (grey) / Story.
- Links the recruit-ladder frame idx 2704 (Dumble
  6/80 on the Defense invitation tab).

### idx 2740: Twilight Bat Clan Rebecca, Master Hunter Lv.1, 4-star, Strength 9450 (catalog 021)
- File: `Screenshot_20180609-170641-149e033c4c17a17a.jpg`
  (720x1280). Crop: `hits/batch-55-2740.png`.
- Train Teammate; sword-class + fire-element icons
  (match catalog 021 Offense/Fire role-element, class
  icon as displayed); 4-star blue ring + Lv.1 ribbon
  (zoom-verified `z55_2740_badge`); Strength 9450
  (zoom-verified `z55_2740_str`); Train /
  Transcendence / Skill Training / Upgrade Equipment
  (grey) / Story.
- STAR NOTE: Train badge shows a 4-star blue ring but
  catalog 021 lists base rarity 2 (star-display vs
  catalog-rarity difference, recorded verbatim).

## Near-hits (full numbers, hit=no per bar rules)

### Recruit splashes with level + stars, no stats (all hit=no)
- idx 2708: Noble Spear Natalia, 3-star gold badge, no
  level ribbon, sword-class + Ice, hidden-ruins
  discovery splash (catalog 037).
- idx 2716: Airport Officer Gullveig, 3-star, Lv.1,
  Bomber + Electricity, +1000 (catalog 039).
  ELEMENT NOTE: client "Electricity" vs catalog
  "Lightning" (lane arc continues).
- idx 2717: Flame of the Battlefield Athena, 3-star,
  Lv.1, Defense + Fire, +1000 (catalog 027).
  TITLE NOTE: client "Flame of the Battlefield" vs
  catalog "Flame of Battlefield".
- idx 2743: Guardian of Fight Club Beckhen, 3-star,
  Lv.1, Offense + Ice, +1000 (catalog 051).
  SPELLING NOTE: client "Beckhen" matches catalog 051
  exactly (not Beckham).
- idx 2727: Silent Canine Patrone Lv.22 transcendence
  match, fodder 3x Lv.1 2212 (0/3 selected), mats
  88/80 + 893/800, fee 80000 vs wallet 114128
  (catalog 033); stars-unshown, fodder unselected.
- idx 2742: level-unshown Train block (bear art),
  Experienced Hunter 3-star gold Lv.MAX, Power
  2480 -> 3310, mates 1132/1250/1946/2055, fee 6000
  vs wallet 234841; full verbatim, hit=no.

## Cross-batch pairing notes

- Hunter-list scroll seq (69/72, same account): idx
  2710 (20841 head ... 3765) -> 2709 (7058 ...
  2698 dupe ... 2511 tail). Roster endpoints
  20841 -> 2511.
- Hunter-list scroll pair (31/36, same account): idx
  2719 (13192 head ... 3757) -> 2720 (5721 ...
  1562 ... 1323 tail). Endpoints 13192 -> 1323.
- Hunter-list scroll pair (65/66, same account): idx
  2729 (12886 head ... 2931) -> 2730 (2734 ...
  2094 dupe ... 2085 dupe ... cut).
- Hunter-list scroll seq (44/75, same account): idx
  2737 (24756 head ... chicken 10745 ... cut) ->
  2738 (10192 ... 2500) -> 2739 (2548 ... 2386
  dupe ... 2249 dupe ... 2076 dupe ... 940 tail,
  chat HuntingMetrons: No). Endpoints 24756 -> 940.
- Hunter-list scroll pair (64/75, same account): idx
  2744 (15366 head ... 7410) -> 2745 (7285 ...
  2600, chat knooreloo: hayy!).
- Missing-hunters Scythia trail: idx 2711 (fuel
  34/60, 29/80 + 29/80, Hard/Hard) -> 2722 (fuel
  70/60, 44/80 + 44/80, Normal/Hard).
- Fight-club same-account trails: idx 2731 (rank
  910, 2201 Point) -> 2732 (profile, 2201 Score,
  likes 2, VER. 1381); idx 2749 (70/75 roster:
  10981/10565/14625/10365/7139) -> 2750 (Prepare
  for Battle ally = same five, 1st-crown on Lv.10
  rooster, undermanned 3-slot opponent).
- Village same-account pair: idx 2746 (coins
  198593, manda 419, timers 59:29/59:05/59:12) ->
  2747 (coins 282593, manda 419 fixed, timers
  49:22/48:58/59:50, chat Mistleteinn: levko and
  yahua).
- Dumble intra-batch arc: idx 2704 recruit-ladder
  (Defense tab, Dumble 6/80) -> 2733 Train HIT
  (Lv.1, Strength 2107).
- 11-pull results: idx 2718 (4x 3-star + 7x 1-star,
  chat Maelon: wow) / idx 2726 (1x 3-star + 1x
  4-star green + 2x 2-star + 7x 1-star, chat
  Mistleteinn: wow lucky).
- Zero-glyph run: idx 2707 / 2711 / 2722 "0day"
  timers (narrow-oval glyph, batch-51 zero
  convention; full-frame OCR reads "O", zoom crop
  `z55_2707_timer` on file).

## Most valuable economy/mechanic readings

- Gacha pricing (idx 2723): Best Hunters Recruiting,
  300% CHANCE UP header with 400%UP / 200%UP card
  odds, Time Left 66:59:33; single Recruit 30 vs
  10+1 Recruit 300; wallet 777 / 0 / 1; Lottery
  Mouse flavor + Recruitment Mileage rows.
- Transcendence cost curve (idx 2727): Patrone
  Lv.22 needs 3 identical 3-star+ fodder (0/3),
  mats 88/80 + 893/800, fee 80000 vs wallet
  114128 (affordable); identical-hunter fodder
  rule quoted verbatim.
- Training fee curve (idx 2742): Lv.MAX block
  Power 2480 -> 3310 (+830), fee 6000 vs wallet
  234841; Training Mate burn warning quoted.
- Dispatch ledger (idx 2724): 9 dispatches, Team
  Level 28, 7080-to-999 spread, Rupees +709, items
  x2/x1/x2/x2.
- Trace payout (idx 2721): 10 time(s), counts
  4/3/3/3/3 + 3/3/5/5/5 (3/4/5 only).
- Fishing price ladder (idx 2706): Seaweed 10,
  Calcium Smelt 50/250/500 three-tier stacks,
  Marsh Snail 10, Mysterious note 300, White
  Barbels Catfish 200/1000, Metron Ayu 300;
  wallet 38771.
- Defense invitation ladder (idx 2704): Defense
  11/12, Bonus 11.0% -> 12.0%; Dumble 6/80,
  Papillon 63/80, Gerard 7/40, Halloween Witch
  Riko 0/40, Hard-Knock Life Riko 36/40, Captain
  taxa 198/20, Robin 260/20, Hecate 234/20.
- Fight-club defense (idx 2728): Team Strength
  86871 (18758/17394/16653/16756/17310); battle
  log Victory +10 (1821/1615, 06.04 02:24),
  Defeats -5/-6 with Revenge buttons.
- Fight-club waiting room (idx 2731): 1 Day(s)
  19:33:43 Left, tickets 0/6, 2201 triple-tie at
  ranks 908-910, Mandarin Tier 2 stars.
- Version provenance: VER. 1381 on idx 2732
  (reg 11/03/2017) and idx 2748 (reg 01/01/2070
  test-style account); footer "© VisualShower
  Corporation, All rights reserved." (idx 2748).

## Non-ASCII names (transliterated, for searchability)

- idx 2704: Papillon, Gerard, Riko, taxa, Robin,
  Hecate, Dumble, Odile. idx 2707: taxa. idx
  2708/2716/2717: Natalia, Gullveig, Athena. idx
  2711/2722: Scythia. idx 2712: Diana. idx 2713:
  ThunderBlythe. idx 2715: Tyltyl. idx 2718:
  Maelon. idx 2726/2747: Mistleteinn. idx 2727:
  Patrone. idx 2728: SuperDAMAOGOU, JingMengWuHen,
  MasterOuHuang, LaoGouBiZhongDeZhanDouBi
  (Chinese messages transliterated). idx 2731/
  2732: Yuuki, MIYAZAKI Takeshi (transliterated),
  LoremIpsum Jr. idx 2733: Dumble. idx 2734:
  AUTISTIC_MAN. idx 2736/2739: HuntingMetrons. idx
  2740: Rebecca. idx 2743: Beckhen. idx 2745:
  knooreloo. idx 2747: levko, yahua. idx 2750:
  Izko. No Korean-script names in batch.

## Contaminants

- idx 2714 is an external community tier-list image
  (by KuschiK, made by Vreeze, from PugNation),
  classified other with a brief note; no game
  digits. No OS overlays or external photos
  elsewhere: otherwise zero-contaminant batch.

## Sic list

- "Deep in the Wolf's Mouth" (idx 2707/2711/2722,
  curly apostrophe in client, kept verbatim).
- "0day" x6 (idx 2707/2711/2722 abyss+mouth
  timers, narrow-oval glyph, batch-51 zero
  convention; OCR reads "O").
- "THIS YEAR'S 4 BEST HUNTERS" + "300% CHANCE
  UP!" header over "400%UP / 200%UP" cards
  (idx 2723, kept verbatim).
- "Flame of the Battlefield" (idx 2717, client
  article vs catalog 027 "Flame of Battlefield").
- "Beckhen" (idx 2743, client = catalog 051,
  not Beckham).
- "yahua" (idx 2747 village chat "levko and
  yahua", kept verbatim).
- "hayy!" (idx 2745 chat, kept verbatim).
- "Everyone else.. Note: Because of lack of
  resources, some hunters aren't listed."
  (idx 2714 tier-list copy, kept verbatim).
- "Future ? - Blustone" (idx 2748, client
  Blustone spelling in profile name, kept
  verbatim).
