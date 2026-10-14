# Batch 56 hits (idx 2751-2800)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-56-2755.png`, `hits/batch-56-2767.png`,
`hits/batch-56-2769.png` (3 HITs).
Zooms (lane folder, provenance only): `z56_2755_name`,
`z56_2767_name`, `z56_2769_name` (recruit 3-star ribbons),
`z56_2758_setup` (transcend fodder rule), `z56_2762_result`
(Bibi result), `z56_2772_stats` / `z56_2772_stats3`
(equipment constellation + stat panel), `z56_2775_name` /
`z56_2775_badge` / `z56_2775_stats` (Revenant train block),
`z56_2769_badge`, `z56_2755_badge` (art crops).
OCR (lane folder): `_tmp56_ocr/` (full-frame tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`) plus
plate-crop OCR attempts (stylized font failed, visual wins).
Write script: `_tmp56_write.py` (kept in lane folder per rules).

## HITs: 3/50 (all recruit rule: name + title + level + stars)

### idx 2755: Flame of the Battlefield Athena, Lv.1, 3-star (catalog 027)
- File: `Screenshot_20180613-210421-54f8d094edd71311.jpg`
  (720x1280). Crop: `hits/batch-56-2755.png`.
- Recruited splash; 3-star gold ribbon (zoom-verified
  `z56_2755_name`; OCR fragment "Flame of the Battlefield /
  Athena / Defense / Fire"); Defense + Fire icons; coins
  +1000; See Details / Okay / Share.
- TITLE NOTE: client "Flame of the Battlefield" vs catalog
  027 "Flame of Battlefield" (article; consistent with the
  2780 ticket tab spelling).

### idx 2767: Girl with Two Faces Heidi, Lv.1, 3-star (catalog 044)
- File: `Screenshot_20180620-013408-4271543ac9748753.png`
  (1080x1920). Crop: `hits/batch-56-2767.png`.
- Recruited splash; 3-star gold ribbon (zoom-verified
  `z56_2767_name`; OCR "Girl with Two Faces / Heidi /
  Offense / Fire"); Offense + Fire icons; +1000.
- Title/name match catalog 044 exactly.

### idx 2769: Silent Canine Patrone, Lv.1, 3-star (catalog 033)
- File: `Screenshot_20180620-113409-a07003137a95cbef.jpg`
  (720x1280). Crop: `hits/batch-56-2769.png`.
- Recruited splash; 3-star gold ribbon (zoom-verified
  `z56_2769_name`); art: purple braid, wolf ears,
  Panzerfaust, blue-checkered shemagh (matches catalog
  White Wolf Combat Uniform + Blue Checkered Shemagh);
  Bomber + Ice icons; +1000.
- SPELL NOTE: client "Patrone" vs catalog 033 "Patrone";
  client spelling OCR-anchored in the 2781 bomber ticket
  tab ("Silent Canine Patrone").

## Near-hits (full numbers, hit=no per bar rules)

### Train block with obscured identity (hit=no)
- idx 2775: "The Revenant ..." Proficient Hunter Lv.21,
  4-star green badge + Lv.21 ribbon (zoom-verified
  `z56_2775_name` / `z56_2775_badge`); HP 1216, AP 696,
  DP 1121 (zoom wins over OCR "7121"), Attacking Speed 7;
  Crit Chance 0 / Crit Damage 50 / Armor Pen 0 / Block
  Chance 0 / Damage Reduction Block 50 / Elemental
  Enhancement 4 / Elemental Resistance 4 / HP Regen 29
  (zoom-verified `z56_2775_stats`); offense fist +
  elemental icons. Name remainder hidden behind star
  badge; no catalog title "The Revenant" (catalog_id
  blank, flagged uncatalogued). Deleted the provisional
  `hits/batch-56-2775.png` crop (hit=no).

### Transcendence setup + result (named + Lv.MAX + stats, no star rank, hit=no)
- idx 2758: Maiden of Gods Akasha (catalog 008), wallet
  14787, fodder candidates 3x Lv.1 2047, selected 0/3;
  rule verbatim "To transcend the hunter above, only
  identical hunters who are 3-star or above can be used
  as fodder. The used hunter will disappear."; mats
  23/80 + 214/800 (OCR); fee 80000 (zoom
  `z56_2758_setup`). Title matches catalog 008.
- idx 2762: Wolf Child Bibi (catalog 040), Strength 20257
  -> 22426 (+2169); AP 1239 -> 1343; Defense 1087 ->
  1177; Life 2457 -> 2661; Successfully transcended!
  (zoom `z56_2762_result`, OCR-confirmed). Stat labels
  AP/Defense/Life.
- idx 2783: Patrone advancement (art + skill identify,
  catalog 033): Proficient Hunter Lv.MAX 8136 -> Master
  Hunter Lv.1 11124 (+2988); New Skill Unlocked Silent
  Canine (OCR-confirmed 8136/11124).

## Cross-batch pairing notes

- Levko same-account trail: idx 2753 fight-club viewer
  (My Rank ribbon, Lv.53, 2161 Point) -> idx 2773 11-pull
  chat (Levko).
- Alex777 same-account trail: idx 2757 friend entry
  (Lv.22, Connecting) -> idx 2764/2765 village owner
  (fuel 32/60 pair, 9s apart).
- Scroll trios: idx 2759 -> 2760 (38/42, 8s apart,
  7856/6478/4275 continuity, Locked tail); idx 2784 ->
  2785 -> 2786 (30/36, 10s/17s apart, endpoints 17137 ->
  299); idx 2787 -> 2788 -> 2789 (61/66, 36s/55s apart,
  endpoints 19548 -> cut; Nene 2435 triple + Athena 2354
  triple + Kain 2629 pair).
- Server-error pair: idx 2770 (village behind, Search
  Complete! 2Day 4:17:35, X_man_20000) vs 2771 (1Day
  23:16:04, chat-head contaminant), 35h apart,
  different sessions.
- Village pair: idx 2764 -> 2765 (timers 00:07:52 ->
  00:07:43, Rewards 06:00:32 -> 06:00:23, fuel 32/60,
  298/510 constant).
- Fight-club league contrast: idx 2753 (21xx band,
  Mandarin 1 star lit, viewer Levko 53) vs 2754 (27xx
  band, Mandarin 0 lit, viewer Xiithaera 64), 216s
  apart, different accounts.
- Build-team contrast: idx 2752 (checked
  6856/5242/2793/2705) vs 2792 (checked
  7530/6788/6538/5979, LynxAin), different teams.
- Ticket-menu ladder (00:13xx run, same session): idx
  2779 (offense) -> 2780 (defense) -> 2781 (bomber) ->
  2782 (healer).
- Patrone intra-batch arc: idx 2769 recruit splash ->
  idx 2781 ticket anchor (spelling) -> idx 2783
  advancement (8136 -> 11124). Akasha pair: 2758 setup
  + 2782 ticket.

## Most valuable economy/mechanic readings

- Transcendence setup cost (idx 2758, Akasha): 3x Lv.1
  2047 identical-fodder candidates (3-star-or-above
  rule), mats 23/80 + 214/800, fee 80000, wallet 14787
  (fee exceeds wallet, setup unexecutable state).
- Transcendence delta (idx 2762, Bibi): +2169 Strength
  (x1.107); AP +104 / Defense +90 / Life +204.
- Advancement delta (idx 2783, Patrone): Lv.MAX 8136 ->
  Lv.1 11124 (+2988, x1.367), Silent Canine unlock.
- Fresh-gear stat block (idx 2772): Strength 18331
  (edge-cut), HP 2290 / AP 1179 / DP 924 / AS 8, all
  +0; 3x Lv.1 equipped + 6 locked slots.
- Veteran ladders: Guru 1 12130/27520 (idx 2756 goals)
  vs Expert 1 1380/2560 with 1180 left (idx 2768;
  1380+1180=2560 arithmetic check); Expert perk ladder
  (Auto-combat 30 consecutive, fuel/support/exchange/
  invitation +5/+7 band).
- Goals ladder (idx 2756): Bonus 5/7 (gem x5 + ticket
  x1 + fleur x20); Recruit 0/2 (scroll x1); Supplies
  1/2 + BONUS row (fuel x30).
- Fishing economy (idx 2795): High-quality Bait 9 on
  hand, Daily Purchase 12/12 capped, Manda-6 bulk
  price, gem 323.
- Pull distributions: 2773 (7/2/2), 2777 (6/2/3),
  2790 reveal (5/4/1), 2791 (6/1/3), 2797 gold-less
  10-pull (7/3/0); "One more time! 300" on all grids.
- Fight-club ranks: 596-600 band at 2160-2162 (2753)
  vs 107-110 band at 2769-2775 (2754); like counts
  25-253; Lv.53-67 nearby-level matchmaking.
- Roster endpoints: batch max 19548 (2787, 61/66) and
  14510 Leader (2774, 40/51); rookie tails 339/311/299
  (2786), 327/317/308/266 (2794), 320/317/293 (2798);
  new accounts 6/12 (2796) and 11/12 (2794) with empty
  slots.
- Zero-digit run (idx 2793): Westfield helper Current
  Amount 0, OCR-verified.

## Element / title wording tallies

- No "Electricity" vs "Lightning" word tokens in batch;
  elements appear as icons only (Fire/Ice on 2755,
  2767, 2769 splashes).
- Thunder-wording title: "Thunder Arrow" Diana (2781
  ticket).
- Title discrepancies: "Flame of the Battlefield"
  (2755 splash + 2780 ticket) vs catalog 027 "Flame of
  Battlefield"; "Patrone" (2769 + 2781 OCR) vs catalog
  033 "Patrone"; client "The Frost Witch" (2779 ticket)
  extends the batch-51/54 article arc vs catalog 028
  "Frost Witch".
- Title gaps: Joy title unshown (2782 healer tab);
  "The Revenant" uncatalogued (2775, catalog_id blank).

## Non-ASCII names (transliterated, for searchability)

- idx 2753: Helloha, Levko, SeriaZ. idx 2754:
  Xiithaera. idx 2757/2764/2765: Alex777. idx 2759:
  Oh_Sangwoo. idx 2760: Jolteon21. idx 2761: Bixby
  (OS). idx 2764/2765: WraithyBatsard, Avork,
  twinklebutt (chat). idx 2768: none. idx 2770:
  X_man_20000. idx 2772: Shoylia. idx 2773: Levko.
  idx 2774: Cajus. idx 2776: Kuschik, Vreeze,
  DinoMaster (external). idx 2777: Alaiko. idx 2788:
  Kain. idx 2789: Nene. idx 2792: LynxAin. Korean-
  script names kept verbatim in TSV (2753
  598, 2754 110) with CJK in rows 2754 (107/108),
  plus Westfield Korean tutorial bubble (2772).

## Contaminants

- idx 2761: Samsung Bixby Vision share sheet + "Select
  a teammate to train" toast (OS overlays).
- idx 2771/2790/2797: Messenger chat-head overlay(s)
  with unread badges (OS; 2797 badge 2).
- idx 2776: third-party tier list in Galaxy Apps
  browser (external community content, dated
  2018.06.24).
- idx 2766: orphan 294x337 zoom crop (uncertain
  provenance, not game-frame UI).

## Sic list

- "Flame of the Battlefield" (2755/2780, client
  article vs catalog 027).
- "Patrone" (2769/2781 OCR, client spelling vs
  catalog 033 "Patrone").
- "The Frost Witch" (2779, client article vs catalog
  028).
- "The Revenant ..." (2775, badge-obscured, no
  catalog match).
- "lL-evel 14" (2778, chat line-break split).
- "cooperati-on." (2754, chat line-break hyphen).
- "Midgard" storm flavor (2763, sic-neutral fantasy
  spelling kept).
- "Westfields basic training" (2793, plural sic).
- "(-_- )" (2753), "Hmm. c. u m at me" (2753),
  "PANDA POWEEER!!" (2753), "o" / "累了" (2754 CJK
  kept), "half life 3 confirmed ..." (2774),
  "BIG NEWS at the Suspi..." (2777), "I fail..."
  (2792) chat verbatim.
- DP "1121" zoom-vs-OCR ("7121") adjudication (2775,
  zoom wins).
